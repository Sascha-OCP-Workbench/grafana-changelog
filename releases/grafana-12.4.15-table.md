# Grafana v12.4.15 — Tabellen-Variante

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.15)

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
| 12.4.15 | Security | **Security:** Fix CVE-2026-102589, CVE-2026-106472, CVE-2026-106475, CVE-2026-107365, CVE-2026-107509, CVE-2026-111000, CVE-2026-81843, CVE-2026-82014 | Dieses Patch-Release behebt acht CVEs; ein Update wird empfohlen. | | | 🔷 Dieses Patch-Release behebt acht CVEs; ein Update wird empfohlen. |
| 12.4.15 | Feature/Enhancement | **DateTime:** Bump moment-timezone to 0.6.6 for 2026 time zone changes | Updates moment-timezone from 0.5.47 to 0.6.6 (tzdata 2025a to 2026f) in the root, @grafana/data and @grafana/prometheus packages, correcting times in British Columbia, Alberta, Northwest Territories, Manitoba and Cuba from November 2026. — PR: [#136947](https://github.com/grafana/grafana/pull/136947) | | | 🔷 Aktualisierte Zeitzonendatenbank beruecksichtigt die Zeitzonenaenderungen 2026. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
