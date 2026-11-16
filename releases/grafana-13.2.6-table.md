# Grafana v13.2.6 — Tabellen-Variante

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.6)

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
| 13.2.6 | Feature/Enhancement | **Provisioning:** Handle repository build timeouts and branch outages | Adds a 30-second deadline to repository Build calls, classifies timeouts with the ErrServerUnavailable sentinel, and marks affected repositories unhealthy with Ready=False and reason ServiceUnavailable. — PR: [#135723](https://github.com/grafana/grafana/pull/135723) | | | ℹ️ Git-Sync-Repositories behandeln Build-Timeouts und zeitweise nicht erreichbare Branches robuster. |
| 13.2.6 | Feature/Enhancement | **Provisioning:** Allow same-host URL change on connection-backed repositories | Allows changing the URL of connection-backed repositories as long as the host stays the same. — PR: [#137091](https://github.com/grafana/grafana/pull/137091) | | | ℹ️ Bei verbindungsgebundenen Repositories kann die URL innerhalb desselben Hosts geaendert werden. |
| 13.2.6 | Security | **Security:** Fix CVE-2026-102589, CVE-2026-107509, CVE-2026-110992, CVE-2026-111024, CVE-2026-13721, CVE-2026-14242 | Sechs CVEs wurden behoben; ein Update der Instanzen wird empfohlen. | | | 🔷 Sechs CVEs wurden behoben; ein Update der Instanzen wird empfohlen. |
| 13.2.6 | Feature/Enhancement | **DateTime:** Update moment-timezone and easy-tz for 2026 time zone changes | Updates moment-timezone to 0.6.6 (with a resolutions pin) and the vendored easy-tz tables to tzdata 2026e, plus regression tests, so zones that abolished DST in 2026 show correct times. — PR: [#136950](https://github.com/grafana/grafana/pull/136950) | | | 🔷 ⚠️ Aktualisierte Zeitzonendaten fuer 2026, dadurch koennen sich Zeitangaben in betroffenen Zeitzonen aendern. |
| 13.2.6 | Bug fix | **Unified search:** Fix empty results when all query words are under 3 chars | Makes free-text search on unified storage (Bleve) fall back to a title prefix wildcard when every word in the query is shorter than three characters, which previously returned no results. — PR: [#137309](https://github.com/grafana/grafana/pull/137309) | | | 🔷 Suchanfragen aus ausschliesslich kurzen Begriffen (< 3 Zeichen) liefern wieder Ergebnisse. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **Tables: More control over how you explore and display table data** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-09-more-control-over-how-you-explore-and-display-table-data/)
- **Synthetic Monitoring: Connect synthetic monitoring checks to your frontend applications** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-11-09-connect-synthetic-monitoring-checks-to-your-frontend-applications/)
- **Adaptive Metrics: A simpler way to manage metrics and recommendations** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-11-06-a-simpler-way-to-manage-metrics-and-recommendations-in-adaptive-metrics/)
- **Fleet Management: Automatic self monitoring** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-11-05-automatic-self-monitoring-in-fleet-management/)
- **Adaptive Metrics: Audit log** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-11-04-adaptive-metrics-audit-log/)
---
