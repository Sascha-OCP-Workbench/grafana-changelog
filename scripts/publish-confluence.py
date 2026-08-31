#!/usr/bin/env python3
"""
Publiziert einen Changelog (Markdown) als Seite in Confluence **Data Center/Server**
(nicht Cloud) via REST-API. Nur Python-Standardbibliothek -> keine pip-Installation
noetig. Ein gesetzter Proxy (Env http_proxy/https_proxy) wird automatisch genutzt.

Beispiele:
  # Seite aus einem Changelog anlegen/aktualisieren (Titel = "Grafana v13.2.0")
  CONFLUENCE_PASSWORD=... python scripts/publish-confluence.py 13.2.0 \\
      --base-url https://confluence.firma.de --space DOCS --user sascha

  # Beliebige Datei, eigener Titel, unter einer Elternseite
  python scripts/publish-confluence.py releases/grafana-13.2.0.md \\
      --base-url https://confluence.firma.de --space DOCS --user sascha \\
      --title "Grafana Release 13.2.0" --parent-id 123456

  # Personal Access Token statt Passwort (Data Center)
  CONFLUENCE_TOKEN=... python scripts/publish-confluence.py 13.2.0 \\
      --base-url https://confluence.firma.de --space DOCS

  # Nur das erzeugte Storage-XHTML ansehen, nichts senden
  python scripts/publish-confluence.py 13.2.0 --dry-run

Auth (Data Center):
  --user + Passwort (--password oder Env CONFLUENCE_PASSWORD; sonst interaktive Abfrage)
    -> HTTP Basic Auth
  ODER  --token / Env CONFLUENCE_TOKEN  -> Bearer (Personal Access Token)

Verhalten:
  Existiert im Space bereits eine Seite mit gleichem Titel (oder wird --page-id
  angegeben), wird sie aktualisiert (Version +1), sonst neu angelegt.
"""
from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# --- Markdown -> Confluence Storage (XHTML-Subset) --------------------------

def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _inline(text: str) -> str:
    """Inline-Markdown -> XHTML. Reihenfolge: erst escapen, dann Tags einsetzen."""
    text = _esc(text)
    # Inline-Code `...` (zuerst, damit ** darin nicht greift)
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", text)
    # Links [text](url)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>',
        text,
    )
    # **fett**
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: f"<strong>{m.group(1)}</strong>", text)
    # _kursiv_ nur an Wortgrenzen -> laesst z.B. ha_engine_address unangetastet
    text = re.sub(r"(?<![A-Za-z0-9])_(?!_)([^_]+?)_(?![A-Za-z0-9])",
                  lambda m: f"<em>{m.group(1)}</em>", text)
    return text


def md_to_storage(md: str, keep_first_h1: bool = False) -> str:
    """Konvertiert den fuer die Grafana-Changelogs genutzten Markdown-Subset in
    Confluence-Storage-Format. Unterstuetzt: #/##/### Headings, - Listen,
    > Blockquote, --- (hr), <details>/<summary> (-> Heading + Inhalt),
    Inline: **fett**, `code`, [text](url). Alles andere wird als Absatz gerendert."""
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    in_ul = False
    in_quote = False
    first_h1_seen = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def close_quote():
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        # <details>/<summary>/</details> -> Storage kennt das nicht
        if stripped.startswith("<details"):
            close_ul(); close_quote()
            continue
        if stripped.startswith("</details>"):
            close_ul(); close_quote()
            continue
        m = re.match(r"<summary>(.*?)</summary>", stripped)
        if m:
            close_ul(); close_quote()
            out.append(f"<h3>{_inline(m.group(1))}</h3>")
            continue

        if not stripped:
            close_ul(); close_quote()
            continue

        if stripped == "---" or re.match(r"^-{3,}$", stripped):
            close_ul(); close_quote()
            out.append("<hr/>")
            continue

        hm = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if hm:
            close_ul(); close_quote()
            level = len(hm.group(1))
            content = hm.group(2)
            if level == 1 and not first_h1_seen:
                first_h1_seen = True
                if not keep_first_h1:
                    continue  # Titel steht schon in der Seiten-Ueberschrift
            level = min(max(level, 1), 6)
            out.append(f"<h{level}>{_inline(content)}</h{level}>")
            continue

        lm = re.match(r"^[-*]\s+(.*)$", stripped)
        if lm:
            close_quote()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_inline(lm.group(1))}</li>")
            continue

        qm = re.match(r"^>\s?(.*)$", stripped)
        if qm:
            close_ul()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append(f"<p>{_inline(qm.group(1))}</p>")
            continue

        # normaler Absatz
        close_ul(); close_quote()
        out.append(f"<p>{_inline(stripped)}</p>")

    close_ul(); close_quote()
    return "\n".join(out)


# --- Confluence REST --------------------------------------------------------

class Confluence:
    def __init__(self, base_url: str, user: str | None, password: str | None,
                 token: str | None, verify_tls: bool = True):
        self.base = base_url.rstrip("/")
        self.api = f"{self.base}/rest/api"
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
        elif user is not None:
            cred = base64.b64encode(f"{user}:{password or ''}".encode("utf-8")).decode("ascii")
            self.headers["Authorization"] = f"Basic {cred}"
        else:
            raise SystemExit("Fehlende Auth: --user (+Passwort) oder --token angeben.")
        self.ctx = None
        if not verify_tls:
            self.ctx = ssl.create_default_context()
            self.ctx.check_hostname = False
            self.ctx.verify_mode = ssl.CERT_NONE

    def _req(self, method: str, url: str, payload: dict | None = None) -> dict:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers=self.headers)
        try:
            with urllib.request.urlopen(req, context=self.ctx) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            raise SystemExit(f"HTTP {e.code} {e.reason} bei {method} {url}\n{detail}")
        except urllib.error.URLError as e:
            raise SystemExit(f"Verbindungsfehler zu {url}: {e.reason}\n"
                             f"(Proxy gesetzt? http_proxy/https_proxy; TLS-CA ok? sonst --insecure)")

    def find_page(self, space: str, title: str) -> dict | None:
        q = urllib.parse.urlencode({"spaceKey": space, "title": title, "expand": "version"})
        res = self._req("GET", f"{self.api}/content?{q}")
        results = res.get("results", [])
        return results[0] if results else None

    def get_page(self, page_id: str) -> dict:
        return self._req("GET", f"{self.api}/content/{page_id}?expand=version,space")

    def create(self, space: str, title: str, storage: str, parent_id: str | None) -> dict:
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": space},
            "body": {"storage": {"value": storage, "representation": "storage"}},
        }
        if parent_id:
            payload["ancestors"] = [{"id": str(parent_id)}]
        return self._req("POST", f"{self.api}/content", payload)

    def update(self, page: dict, title: str, storage: str) -> dict:
        page_id = page["id"]
        new_ver = int(page["version"]["number"]) + 1
        payload = {
            "id": page_id,
            "type": "page",
            "title": title,
            "version": {"number": new_ver},
            "body": {"storage": {"value": storage, "representation": "storage"}},
        }
        return self._req("PUT", f"{self.api}/content/{page_id}", payload)


# --- CLI --------------------------------------------------------------------

def resolve_source(arg: str) -> Path:
    p = Path(arg)
    if p.is_file():
        return p
    ver = arg
    for pref in ("grafana-", "v"):
        if ver.startswith(pref):
            ver = ver[len(pref):]
    ver = ver[:-3] if ver.endswith(".md") else ver
    cand = REPO_ROOT / "releases" / f"grafana-{ver}.md"
    if cand.is_file():
        return cand
    raise SystemExit(f"Changelog nicht gefunden: weder Datei '{arg}' noch {cand}")


def default_title(src: Path) -> str:
    text = src.read_text(encoding="utf-8")
    m = re.match(r"^#\s+(.*)$", text.lstrip().splitlines()[0]) if text.strip() else None
    if m:
        return m.group(1).strip()
    stem = src.stem  # grafana-13.2.0
    return "Grafana " + stem.replace("grafana-", "")


def main() -> None:
    ap = argparse.ArgumentParser(description="Changelog als Confluence-Seite publizieren (Data Center).")
    ap.add_argument("source", help="Changelog-Datei ODER Version (z.B. 13.2.0)")
    ap.add_argument("--base-url", default=os.environ.get("CONFLUENCE_BASE_URL"),
                    help="Confluence-Basis-URL, z.B. https://confluence.firma.de (Env CONFLUENCE_BASE_URL)")
    ap.add_argument("--space", default=os.environ.get("CONFLUENCE_SPACE"),
                    help="Space-Key (Env CONFLUENCE_SPACE)")
    ap.add_argument("--title", help="Seitentitel (Default: aus dem Changelog abgeleitet)")
    ap.add_argument("--parent-id", help="ID der Elternseite (optional)")
    ap.add_argument("--page-id", help="Bestehende Seite gezielt per ID aktualisieren")
    ap.add_argument("--user", default=os.environ.get("CONFLUENCE_USER"),
                    help="Benutzername fuer Basic Auth (Env CONFLUENCE_USER)")
    ap.add_argument("--password", default=os.environ.get("CONFLUENCE_PASSWORD"),
                    help="Passwort (besser Env CONFLUENCE_PASSWORD; sonst interaktive Abfrage)")
    ap.add_argument("--token", default=os.environ.get("CONFLUENCE_TOKEN"),
                    help="Personal Access Token -> Bearer (Env CONFLUENCE_TOKEN)")
    ap.add_argument("--keep-title-heading", action="store_true",
                    help="Erste '# '-Ueberschrift im Body behalten (Default: entfernen)")
    ap.add_argument("--insecure", action="store_true", help="TLS-Zertifikat nicht pruefen")
    ap.add_argument("--dry-run", action="store_true", help="Nur Storage-XHTML ausgeben, nichts senden")
    args = ap.parse_args()

    src = resolve_source(args.source)
    title = args.title or default_title(src)
    storage = md_to_storage(src.read_text(encoding="utf-8"), keep_first_h1=args.keep_title_heading)

    if args.dry_run:
        print(f"# Titel: {title}\n# Quelle: {src}\n# --- Storage-XHTML ---")
        print(storage)
        return

    if not args.base_url or not args.space:
        raise SystemExit("--base-url und --space sind erforderlich (oder via Env setzen).")

    password = args.password
    if not args.token and args.user and not password:
        if sys.stdin.isatty():
            password = getpass.getpass(f"Confluence-Passwort fuer {args.user}: ")
        else:
            raise SystemExit("Kein Passwort/Token: --password, Env CONFLUENCE_PASSWORD oder --token setzen.")

    cf = Confluence(args.base_url, args.user, password, args.token, verify_tls=not args.insecure)

    if args.page_id:
        page = cf.get_page(args.page_id)
        res = cf.update(page, title, storage)
        action = "aktualisiert"
    else:
        existing = cf.find_page(args.space, title)
        if existing:
            res = cf.update(existing, title, storage)
            action = "aktualisiert"
        else:
            res = cf.create(args.space, title, storage, args.parent_id)
            action = "angelegt"

    page_id = res.get("id", "?")
    webui = ((res.get("_links") or {}).get("base", cf.base)) + \
            ((res.get("_links") or {}).get("webui", ""))
    ver = ((res.get("version") or {}).get("number", "?"))
    print(f"Seite {action}: '{title}' (id={page_id}, Version {ver})")
    print(f"URL: {webui}")


if __name__ == "__main__":
    main()
