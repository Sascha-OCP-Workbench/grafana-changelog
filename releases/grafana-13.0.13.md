# Grafana v13.0.13

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.13)

> Legende: ⚠️ Doku-Anpassung noetig / potenziell breaking (von Grafana nicht als Breaking Change gekennzeichnet, kann aber Bestehendes brechen oder eine Doku-Anpassung erfordern) · 🔧 neuer Default (Verhalten ab jetzt standardmaessig aktiv/geaendert)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- **Provisioning: Allow same-host URL change on connection-backed repositories** — Bei connection-backed Repositories kann die URL nun innerhalb desselben Hosts geaendert werden ([#137092](https://github.com/grafana/grafana/pull/137092)).

## Hilfreiche Informationen
- **Security: Fix CVE-2026-102589, CVE-2026-107365, CVE-2026-107509, CVE-2026-110992, CVE-2026-111024, CVE-2026-13721, CVE-2026-14242, CVE-2026-82014** — Acht Sicherheitsluecken wurden behoben; ein Update wird empfohlen.
- ⚠️ **DateTime: Bump moment-timezone to 0.6.6 for 2026 time zone changes** — Aktualisierte Zeitzonendaten fuer 2026 koennen Zeitzonen-Offsets in Dashboards und Abfragen veraendern ([#136948](https://github.com/grafana/grafana/pull/136948)).

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- Keine.

---

## ⚠️ Automatischer Vollstaendigkeits-Check

Diese Quell-Eintraege tauchen **nicht** in der Zusammenfassung oben auf — **wurde nicht beruecksichtigt, manuell pruefen**:

### What's-new-Katalog (nicht beruecksichtigt)
- 2026-11-09 [nur Enterprise/Cloud] More control over how you explore and display table data — https://grafana.com/whats-new/2026-11-09-more-control-over-how-you-explore-and-display-table-data/
- 2026-11-09 [nur Enterprise/Cloud] Connect synthetic monitoring checks to your frontend applications — https://grafana.com/whats-new/2026-11-09-connect-synthetic-monitoring-checks-to-your-frontend-applications/
- 2026-11-06 [nur Enterprise/Cloud] A simpler way to manage metrics and recommendations in adaptive metrics — https://grafana.com/whats-new/2026-11-06-a-simpler-way-to-manage-metrics-and-recommendations-in-adaptive-metrics/
- 2026-11-05 [nur Enterprise/Cloud] Automatic self monitoring in fleet management — https://grafana.com/whats-new/2026-11-05-automatic-self-monitoring-in-fleet-management/
- 2026-11-05 [OSS] Group and delete multiple panels from the dashboard — https://grafana.com/whats-new/2026-11-05-group-and-delete-multiple-panels-from-the-dashboard/
- 2026-11-04 [nur Enterprise/Cloud] Adaptive metrics audit log — https://grafana.com/whats-new/2026-11-04-adaptive-metrics-audit-log/
- 2026-11-03 [OSS] Undo and redo dashboard changes — https://grafana.com/whats-new/2026-11-03-undo-and-redo-dashboard-changes/
- 2026-11-03 [OSS] Keep more of your dashboard visible with grafana assistant — https://grafana.com/whats-new/2026-11-03-keep-more-of-your-dashboard-visible-with-grafana-assistant/
- 2026-10-30 [nur Enterprise/Cloud] Redesigned grafana cloud homepage — https://grafana.com/whats-new/2026-10-30-redesigned-grafana-cloud-homepage/
- 2026-10-28 [nur Enterprise/Cloud] Real user context in browser checks  see if a failing browser check is hitting real users — https://grafana.com/whats-new/2026-10-28-real-user-context-in-browser-checks--see-if-a-failing-browser-check-is-hitting-real-users/
- 2026-10-27 [OSS] Revamped query editor  now generally available — https://grafana.com/whats-new/2026-10-27-revamped-query-editor--now-generally-available/
- 2026-10-27 [nur Enterprise/Cloud] Announcement banners can now be dismissible — https://grafana.com/whats-new/2026-10-27-announcement-banners-can-now-be-dismissible/
- 2026-10-26 [OSS] New dashboard mode selector — https://grafana.com/whats-new/2026-10-26-new-dashboard-mode-selector/
- 2026-10-26 [OSS] Grafana visual ui refresh — https://grafana.com/whats-new/2026-10-26-grafana-visual-ui-refresh/
- 2026-10-26 [nur Enterprise/Cloud] Get check suggestions in synthetic monitoring  experimental — https://grafana.com/whats-new/2026-10-26-get-check-suggestions-in-synthetic-monitoring--experimental/
- 2026-10-23 [OSS] Sort by multiple fields in the sort by transformation — https://grafana.com/whats-new/2026-10-23-sort-by-multiple-fields-in-the-sort-by-transformation/
- 2026-10-23 [OSS] Keep transformation chains stable with static refids — https://grafana.com/whats-new/2026-10-23-keep-transformation-chains-stable-with-static-refids/
- 2026-10-23 [OSS] Connect git sync repositories with an oauth app — https://grafana.com/whats-new/2026-10-23-connect-git-sync-repositories-with-an-oauth-app/
- 2026-10-23 [OSS] Git sync folder docs gain tabs and mermaid diagrams — https://grafana.com/whats-new/2026-10-23-git-sync-folder-docs-gain-tabs-and-mermaid-diagrams/
- 2026-10-22 [OSS] Alloy v121 — https://grafana.com/whats-new/2026-10-22-alloy-v121/
- 2026-10-22 [OSS] New alertrule and recordingrule apis for grafana managed alerts — https://grafana.com/whats-new/2026-10-22-new-alertrule-and-recordingrule-apis-for-grafana-managed-alerts/
- 2026-10-22 [OSS] Manage prometheus mimir and loki alerting with a dedicated plugin — https://grafana.com/whats-new/2026-10-22-manage-prometheus-mimir-and-loki-alerting-with-a-dedicated-plugin/
- 2026-10-21 [nur Enterprise/Cloud] Archive logs with adaptive logs — https://grafana.com/whats-new/2026-10-21-archive-logs-with-adaptive-logs/
- 2026-10-21 [nur Enterprise/Cloud] Private data source connect over tailscale now in public preview — https://grafana.com/whats-new/2026-10-21-private-data-source-connect-over-tailscale-now-in-public-preview/
- 2026-10-20 [OSS] Combine findings from across grafana and share them with notebooks — https://grafana.com/whats-new/2026-10-20-combine-findings-from-across-grafana-and-share-them-with-notebooks/
- 2026-10-19 [nur Enterprise/Cloud] Assistant watchers are now generally available in grafana cloud — https://grafana.com/whats-new/2026-10-19-assistant-watchers-are-now-generally-available-in-grafana-cloud/
- 2026-10-19 [nur Enterprise/Cloud] Grafana managed sandboxes  from root cause to pull request  without leaving grafana — https://grafana.com/whats-new/2026-10-19-grafana-managed-sandboxes--from-root-cause-to-pull-request--without-leaving-grafana/
- 2026-10-19 [nur Enterprise/Cloud] Introducing grafana pages  build anything on your data  right inside grafana — https://grafana.com/whats-new/2026-10-19-introducing-grafana-pages--build-anything-on-your-data--right-inside-grafana/
- 2026-10-19 [nur Enterprise/Cloud] Send opentelemetry traces to agent observability  no sdk required — https://grafana.com/whats-new/2026-10-19-send-opentelemetry-traces-to-agent-observability--no-sdk-required/
- 2026-10-15 [nur Enterprise/Cloud] Investigate alerts and incidents with grafana assistant in irm — https://grafana.com/whats-new/2026-10-15-investigate-alerts-and-incidents-with-grafana-assistant-in-irm/
- 2026-10-14 [nur Enterprise/Cloud] Discover and organize your services in service center — https://grafana.com/whats-new/2026-10-14-discover-and-organize-your-services-in-service-center/
- 2026-10-14 [OSS] Define variables once  use them across dashboards — https://grafana.com/whats-new/2026-10-14-define-variables-once--use-them-across-dashboards/
- 2026-10-14 [nur Enterprise/Cloud] Send grafana irm alerts to the device you choose — https://grafana.com/whats-new/2026-10-14-send-grafana-irm-alerts-to-the-device-you-choose/
- 2026-10-14 [nur Enterprise/Cloud] Choose connection kpis to control metrics cost — https://grafana.com/whats-new/2026-10-14-choose-connection-kpis-to-control-metrics-cost/
- 2026-10-14 [nur Enterprise/Cloud] Session replay is now available for everyone — https://grafana.com/whats-new/2026-10-14-session-replay-is-now-available-for-everyone/
- 2026-10-14 [nur Enterprise/Cloud] Fill in incident custom fields without leaving slack — https://grafana.com/whats-new/2026-10-14-fill-in-incident-custom-fields-without-leaving-slack/
- 2026-10-13 [nur Enterprise/Cloud] Automate incident response and operations with grafana workflows — https://grafana.com/whats-new/2026-10-13-automate-incident-response-and-operations-with-grafana-workflows/
- 2026-10-13 [nur Enterprise/Cloud] Filter and sort alert groups by date in grafana irm — https://grafana.com/whats-new/2026-10-13-filter-and-sort-alert-groups-by-date-in-grafana-irm/
- 2026-10-12 [nur Enterprise/Cloud] Improve alert rule quality — https://grafana.com/whats-new/2026-10-12-improve-alert-rule-quality/
- 2026-10-12 [nur Enterprise/Cloud] Silences in grafana irm now last as long as you set them — https://grafana.com/whats-new/2026-10-12-silences-in-grafana-irm-now-last-as-long-as-you-set-them/
- 2026-10-12 [nur Enterprise/Cloud] New escalation options in grafana irm — https://grafana.com/whats-new/2026-10-12-new-escalation-options-in-grafana-irm/
- 2026-10-09 [nur Enterprise/Cloud] Custom headers and footers for report pdfs — https://grafana.com/whats-new/2026-10-09-custom-headers-and-footers-for-report-pdfs/
- 2026-10-08 [OSS] Connect synthetic monitoring checks to your services with knowledge graph — https://grafana.com/whats-new/2026-10-08-connect-synthetic-monitoring-checks-to-your-services-with-knowledge-graph/
- 2026-10-08 [nur Enterprise/Cloud] Synthetic monitoring folders are now generally available — https://grafana.com/whats-new/2026-10-08-synthetic-monitoring-folders-are-now-generally-available/
- 2026-10-06 [OSS] Plan your dashboard before building it with grafana assistant — https://grafana.com/whats-new/2026-10-06-plan-your-dashboard-before-building-it-with-grafana-assistant/
- 2026-10-02 [nur Enterprise/Cloud] Role managers can revoke access they do not hold — https://grafana.com/whats-new/2026-10-02-role-managers-can-revoke-access-they-do-not-hold/
- 2026-10-01 [nur Enterprise/Cloud] Run database observability on clustered grafana alloy — https://grafana.com/whats-new/2026-10-01-run-database-observability-on-clustered-grafana-alloy/
- 2026-09-30 [OSS] Build data driven dashboards with the updated text visualization — https://grafana.com/whats-new/2026-09-30-build-data-driven-dashboards-with-the-updated-text-visualization/
- 2026-09-30 [nur Enterprise/Cloud] Recommended usage alerts — https://grafana.com/whats-new/2026-09-30-recommended-usage-alerts/
- 2026-09-29 [nur Enterprise/Cloud] Create an slo from a synthetic monitoring check — https://grafana.com/whats-new/2026-09-29-create-an-slo-from-a-synthetic-monitoring-check/
- 2026-09-29 [OSS] Estimate distinct log values with approx — https://grafana.com/whats-new/2026-09-29-estimate-distinct-log-values-with-approx/
- 2026-09-25 [nur Enterprise/Cloud] Auto apply is generally available in grafana cloud — https://grafana.com/whats-new/2026-09-25-auto-apply-is-generally-available-in-grafana-cloud/
- 2026-09-25 [nur Enterprise/Cloud] Knowledge graph mapping activates automatically with observability solutions — https://grafana.com/whats-new/2026-09-25-knowledge-graph-mapping-activates-automatically-with-observability-solutions/
- 2026-09-25 [OSS] New panel query errors and notices ui — https://grafana.com/whats-new/2026-09-25-new-panel-query-errors-and-notices-ui/
- 2026-09-24 [OSS] Panel time settings and time comparison are now generally available — https://grafana.com/whats-new/2026-09-24-panel-time-settings-and-time-comparison-are-now-generally-available/
- 2026-09-24 [nur Enterprise/Cloud] Show all entities search in the knowledge graph — https://grafana.com/whats-new/2026-09-24-show-all-entities-search-in-the-knowledge-graph/
- 2026-09-21 [OSS] Import of alertmanager configuration to grafana alerting — https://grafana.com/whats-new/2026-09-21-import-of-alertmanager-configuration-to-grafana-alerting/
- 2026-09-21 [OSS] Try dashboard changes confidently with grafana assistant undo — https://grafana.com/whats-new/2026-09-21-try-dashboard-changes-confidently-with-grafana-assistant-undo/
- 2026-09-18 [nur Enterprise/Cloud] Suggested recommendations for adaptive logs — https://grafana.com/whats-new/2026-09-18-suggested-recommendations-for-adaptive-logs/
- 2026-09-18 [nur Enterprise/Cloud] Fleet managed adaptive logs in public preview — https://grafana.com/whats-new/2026-09-18-fleet-managed-adaptive-logs-in-public-preview/
- 2026-09-15 [nur Enterprise/Cloud] Catch pipeline issues on your services — https://grafana.com/whats-new/2026-09-15-catch-pipeline-issues-on-your-services/
- 2026-09-14 [OSS] Make panels easier to understand with subtitles — https://grafana.com/whats-new/2026-09-14-make-panels-easier-to-understand-with-subtitles/
- 2026-09-14 [nur Enterprise/Cloud] Secrets management is generally available with aws secrets manager support — https://grafana.com/whats-new/2026-09-14-secrets-management-is-generally-available-with-aws-secrets-manager-support/
- 2026-09-10 [nur Enterprise/Cloud] Monitor your full stack from the observability home page — https://grafana.com/whats-new/2026-09-10-monitor-your-full-stack-from-the-observability-home-page/
- 2026-09-10 [nur Enterprise/Cloud] Let grafana propose slos for your service — https://grafana.com/whats-new/2026-09-10-let-grafana-propose-slos-for-your-service/
- 2026-09-07 [nur Enterprise/Cloud] Application observability now includes the knowledge graph by default — https://grafana.com/whats-new/2026-09-07-application-observability-now-includes-the-knowledge-graph-by-default/
- 2026-09-07 [nur Enterprise/Cloud] Query k6 test result metrics with promql in your own stack — https://grafana.com/whats-new/2026-09-07-query-k6-test-result-metrics-with-promql-in-your-own-stack/
- 2026-09-02 [nur Enterprise/Cloud] Track and create slos from your service entities — https://grafana.com/whats-new/2026-09-02-track-and-create-slos-from-your-service-entities/
- 2026-08-27 [OSS] Cross filter on more visualizations — https://grafana.com/whats-new/2026-08-27-cross-filter-on-more-visualizations/
- 2026-08-26 [nur Enterprise/Cloud] Investigate database performance with grafana assistant — https://grafana.com/whats-new/2026-08-26-investigate-database-performance-with-grafana-assistant/
- 2026-08-24 [nur Enterprise/Cloud] Alert enrichment — https://grafana.com/whats-new/2026-08-24-alert-enrichment/
- 2026-08-24 [OSS] Alerting notification history — https://grafana.com/whats-new/2026-08-24-alerting-notification-history/
- 2026-08-19 [nur Enterprise/Cloud] K6 studio 20  browser test authoring and autocorrelation are generally available — https://grafana.com/whats-new/2026-08-19-k6-studio-20--browser-test-authoring-and-autocorrelation-are-generally-available/
- 2026-08-18 [nur Enterprise/Cloud] Further optimize metrics costs with adaptive metrics recommendations configuration — https://grafana.com/whats-new/2026-08-18-further-optimize-metrics-costs-with-adaptive-metrics-recommendations-configuration/
- 2026-08-18 [OSS] Authoring commits in git sync — https://grafana.com/whats-new/2026-08-18-authoring-commits-in-git-sync/
- 2026-08-18 [nur Enterprise/Cloud] Git sync support for github enterprise — https://grafana.com/whats-new/2026-08-18-git-sync-support-for-github-enterprise/
- 2026-08-18 [OSS] Webhooks available for gitlab and bitbucket — https://grafana.com/whats-new/2026-08-18-webhooks-available-for-gitlab-and-bitbucket/
- 2026-08-18 [OSS] Revamped homepage for grafana — https://grafana.com/whats-new/2026-08-18-revamped-homepage-for-grafana/
- 2026-08-18 [OSS] Export traces of grafana to a file for easier troubleshooting — https://grafana.com/whats-new/2026-08-18-export-traces-of-grafana-to-a-file-for-easier-troubleshooting/
- 2026-08-18 [OSS] Azure monitor batch api — https://grafana.com/whats-new/2026-08-18-azure-monitor-batch-api/
