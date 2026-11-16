# Grafana v13.1.10 — Tabellen-Variante

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.10)

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
| 13.1.10 | Feature/Enhancement | **Provisioning:** Allow same-host URL change on connection-backed repositories | **Provisioning:** allow same-host URL change on connection-backed repositories → [What's new](https://grafana.com/whats-new/2026-10-23-connect-git-sync-repositories-with-an-oauth-app/) — PR: [#137090](https://github.com/grafana/grafana/pull/137090) | | | ℹ️ Bei Repositories, die ueber eine bestehende Connection (z. B. OAuth-App) angebunden sind, kann die Repository-URL nun geaendert werden, solange der Host gleich bleibt. |
| 13.1.10 | Security | **Security:** Fix seven CVEs (CVE-2026-102589, -107365, -107509, -110992, -111024, -13721, -14242) | Patch-Release mit mehreren Sicherheitsfixes; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Patch-Release mit mehreren Sicherheitsfixes; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **Tables: More control over how you explore and display table data** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-09-more-control-over-how-you-explore-and-display-table-data/).
- **Synthetic Monitoring: Connect checks to your frontend applications** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-09-connect-synthetic-monitoring-checks-to-your-frontend-applications/).
- **Adaptive Metrics: Simpler management of metrics and recommendations** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-06-a-simpler-way-to-manage-metrics-and-recommendations-in-adaptive-metrics/).
- **Fleet Management: Automatic self monitoring** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-05-automatic-self-monitoring-in-fleet-management/).
- **Adaptive Metrics: Audit log** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-11-04-adaptive-metrics-audit-log/).
---
