#!/usr/bin/env bash
# Erzeugt aus der TABELLEN-Fassung releases/grafana-<version>-table.md eine LOKAL
# gefilterte Fassung, in der alle Tabellenzeilen mit Stichwoertern aus einer
# Blacklist entfernt sind. Arbeitet ausschliesslich auf dem Tabellen-Changelog
# (nicht auf der Prosa-Fassung grafana-<version>.md).
#
# Sinn: Fuer bestimmte Zielgruppen irrelevante Themen (z.B. "azure", "alerting")
# ausblenden, ohne den offiziellen Changelog zu veraendern. blacklist.txt und der
# Ausgabeordner filtered/ bleiben lokal (per .gitignore), werden also nie gepusht.
#
# Verwendung:
#   scripts/filter-changelog.sh 13.2.0
#   scripts/filter-changelog.sh v13.2.0            # fuehrendes v ist egal
#   BLACKLIST=andere.txt scripts/filter-changelog.sh 13.2.0
#
# Blacklist-Format (blacklist.txt im Repo-Root):
#   - ein Stichwort pro Zeile, Teilstring-Match, Gross/Klein egal
#   - Zeilen mit fuehrendem '#' und Leerzeilen werden ignoriert (Kommentare)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

[ $# -ge 1 ] || { echo "Usage: $0 <version>  (z.B. 13.2.0)" >&2; exit 1; }

# Version normalisieren: 'grafana-' / fuehrendes 'v' / '-table' / '.md' abstreifen.
ver="$1"; ver="${ver#grafana-}"; ver="${ver#v}"; ver="${ver%.md}"; ver="${ver%-table}"
SRC="releases/grafana-${ver}-table.md"
[ -f "$SRC" ] || { echo "Nicht gefunden: $SRC (nur Tabellen-Changelogs werden gefiltert)" >&2; exit 1; }

BLACKLIST="${BLACKLIST:-blacklist.txt}"
OUT_DIR="filtered"; mkdir -p "$OUT_DIR"
OUT="${OUT_DIR}/grafana-${ver}-table.md"

# Blacklist bereinigen: Kommentare (#...) und Leerzeilen raus, trailing Space weg.
terms="$(mktemp)"; trap 'rm -f "$terms"' EXIT
if [ -f "$BLACKLIST" ]; then
  grep -vE '^[[:space:]]*(#|$)' "$BLACKLIST" | sed 's/[[:space:]]*$//' > "$terms" || true
fi

if [ -s "$terms" ]; then
  # Filtern via awk (Teilstring, case-insensitiv). Bewusst KEIN 'grep -i': der
  # msys/git-bash-grep stuerzt mit -i reproduzierbar ab (SIGABRT).
  # Gehaltene Zeilen -> $OUT, entfernte Zeilen -> $dropped (fuer die Auflistung).
  dropped="$(mktemp)"; trap 'rm -f "$terms" "$dropped"' EXIT
  removed=$(awk -v termsfile="$terms" -v out="$OUT" -v dropfile="$dropped" '
    BEGIN { n=0; while ((getline t < termsfile) > 0) if (length(t)) terms[++n]=tolower(t) }
    { low=tolower($0); hit=0; for (i=1;i<=n;i++) if (index(low, terms[i])) { hit=1; break }
      if (hit) { removed++; if (length($0)) print > dropfile } else print > out }
    END { print removed+0 }
  ' "$SRC")
  used="$(paste -sd, "$terms")"
  {
    echo; echo "---"
    echo "_Lokal gefiltert aus ${SRC##*/}: ${removed} Zeile(n) entfernt (Blacklist: ${used})._"
    if [ -s "$dropped" ]; then
      echo
      echo "<details><summary>Weggefilterte Eintraege (${removed})</summary>"
      echo
      # Weggefilterte Eintraege als Tabelle: Kopfzeile + Trennzeile aus der Quelle,
      # dann die entfernten Tabellenzeilen (Reihenfolge bleibt erhalten). Markdown
      # rendert Tabellen auch innerhalb von <details>, sofern eine Leerzeile davor
      # steht (die echo oben liefert sie).
      hdr="$(grep -m1 -E '^\| *Version ' "$SRC" || true)"
      sep="$(grep -m1 -E '^\|[-: |]+$' "$SRC" || true)"
      rows="$(grep -E '^\|' "$dropped" || true)"
      if [ -n "$hdr" ] && [ -n "$sep" ] && [ -n "$rows" ]; then
        printf '%s\n%s\n%s\n' "$hdr" "$sep" "$rows"
      else
        # Fallback (keine Tabellenzeilen erkannt): als einfache Liste ausgeben.
        sed -E 's/^[[:space:]]*[-*][[:space:]]+//' "$dropped" | sed 's/^/- /'
      fi
      echo
      echo "</details>"
    fi
  } >> "$OUT"
else
  removed=0
  cp "$SRC" "$OUT"
  echo "Hinweis: keine Stichwoerter in '$BLACKLIST' (leer/fehlt) -> unveraenderte Kopie." >&2
fi

echo "geschrieben: $OUT (${removed} Zeile(n) gefiltert)"
