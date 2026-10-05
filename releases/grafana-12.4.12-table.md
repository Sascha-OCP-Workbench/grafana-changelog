# Grafana v12.4.12 — Tabellen-Variante

_Veroeffentlicht: 2026-09-29_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.12)

**Spalten:**
1. **Version**
2. **Kategorie (Upstream)** — Einordnung aus dem GitHub-Release-Changelog: `Breaking change` · `Feature/Enhancement` · `Bug fix` · `Security` · `Plugin development`
3. **Aenderungstitel** — vereinheitlichter englischer Titel der Aenderung (nah an den Original-PR-Ueberschriften, bei Sammelpunkten KI-formuliert; < 20 Woerter)
4. **Beschreibung (aus den PRs) / What's new** — kurze englische Zusammenfassung aus den verlinkten Pull-Requests (What/Why), dazu What's-new-Deep-Links und Upstream-PR-Links
5. **Platform** — Sicht des Plattform-Betreibers/Hosters der Grafana-Instanz (inkl. Nutzung der Instanz fuers OpenShift-Plattform-Monitoring); bewusst leer, vom Kunden zu bewerten
6. **User** — Sicht eines Projekt-Team-Nutzers der Grafana-Instanz (ohne administrativen Grafana-Zugriff); bewusst leer, vom Kunden zu bewerten
7. **Deine deutsche Bewertung** — Icon(s) + ggf. kurze Zusatzeinschaetzung

**Legende (Spalte 7):** 🚧 harter Breaking Change (von Grafana offiziell gekennzeichnet) · ℹ️ Hilfreiche neue Funktion · 🔷 Hilfreiche Information · 🔧 neuer Default (Verhalten ab jetzt standardmaessig aktiv/geaendert) · ⚠️ Doku-Anpassung noetig / potenziell breaking (nicht offiziell als Breaking Change gekennzeichnet, kann aber Bestehendes brechen)

| Version | Kategorie (Upstream) | Aenderungstitel | Beschreibung (aus den PRs) / What's new | Platform | User | Deine deutsche Bewertung |
|---|---|---|---|---|---|---|
| 12.4.12 | Security | **Security:** Fix CVE-2026-13719, CVE-2026-13720, CVE-2026-81841 and CVE-2026-81842 | Das Patch-Release behebt vier Sicherheitsluecken; ein zeitnahes Update wird empfohlen. | | | 🔷 Das Patch-Release behebt vier Sicherheitsluecken; ein zeitnahes Update wird empfohlen. |
| 12.4.12 | Bug fix | **Unified Storage:** Return 403 instead of 500 on namespace mismatch | **Unified Storage:** Return 403 instead of 500 on namespace mismatch — PR: [#133595](https://github.com/grafana/grafana/pull/133595) | | | 🔷 ⚠️ Bei einem Namespace-Mismatch liefert Unified Storage jetzt HTTP 403 statt 500, was Clients und Monitoring auf den geaenderten Statuscode einstellen sollten. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
