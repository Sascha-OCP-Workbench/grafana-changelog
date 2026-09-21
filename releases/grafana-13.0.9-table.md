# Grafana v13.0.9 — Tabellen-Variante

_Veroeffentlicht: 2026-09-15_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.9)

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
| 13.0.9 | Security | **Security:** Fix CVE-2026-15815, CVE-2026-76154 and CVE-2026-79656 | Dieses Patch-Release behebt drei CVEs; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Dieses Patch-Release behebt drei CVEs; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). |
| 13.0.9 | Bug fix | **Dashboards:** Preserve query variable refresh setting on v2 dashboard import | Fixes v2 dashboard import so remapping a query variable's datasource preserves the author's original refresh setting instead of hardcoding onDashboardLoad; 'never' is still upgraded since options are cleared. — PR: [#132088](https://github.com/grafana/grafana/pull/132088) | | | 🔷 Beim Import von v2-Dashboards bleibt die refresh-Einstellung von Query-Variablen erhalten. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **Adaptive Logs: Suggested recommendations** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-18-suggested-recommendations-for-adaptive-logs/)
- **Secrets management GA with AWS Secrets Manager support** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-14-secrets-management-is-generally-available-with-aws-secrets-manager-support/)
- **Observability home page for full-stack monitoring** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-10-monitor-your-full-stack-from-the-observability-home-page/)
- **SLOs: Let Grafana propose SLOs for your service** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-10-let-grafana-propose-slos-for-your-service/)
- **Application Observability: Knowledge graph included by default** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-07-application-observability-now-includes-the-knowledge-graph-by-default/)
- **k6: Query test result metrics with PromQL in your own stack** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-07-query-k6-test-result-metrics-with-promql-in-your-own-stack/)
- **SLOs: Track and create SLOs from your service entities** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-09-02-track-and-create-slos-from-your-service-entities/)
- **Older catalog entries (June–August 2026)** — weitere Enterprise/Cloud-Eintraege des Katalogs stammen aus frueheren Release-Zeitraeumen und sind fuer dieses Patch-Release ohne Belang; keine PRs im Release-Body.
---
