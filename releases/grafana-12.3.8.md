# Grafana v12.3.8

_Veroeffentlicht: 2026-06-23_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.3.8)

## Breaking Changes
- `PUT /api/datasources/uid/:uid` liefert jetzt HTTP 400, wenn die UID im Request-Body nicht der UID in der URL entspricht — Automatisierungen/Provisioning-Skripte, die abweichende UIDs senden, muessen angepasst werden ([#125523](https://github.com/grafana/grafana/pull/125523)).

## Hilfreiche neue Funktionen
- Keine.

## Hilfreiche Informationen
- Die Alpine-basierten Docker-Images wurden auf 3.24.1 aktualisiert, wodurch Basis-Image-Patches inkl. Sicherheitsupdates enthalten sind ([#126545](https://github.com/grafana/grafana/pull/126545)).
- Reines Patch-Release: ausser dem Datasource-API-Fix und dem Image-Bump sind keine weiteren Aenderungen dokumentiert.

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- Google workload identity federation for BigQuery and Google Cloud Monitoring — irrelevant, da nur Enterprise → [What's new](https://grafana.com/whats-new/2026-06-24-google-workload-identity-federation-for-bigquery-and-google-cloud-monitoring/)
- Create browser tests from plain language user journeys — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-06-24-create-browser-tests-from-plain-language-user-journeys/)
- Alerting: Grafana Cloud nutzt den internen Alertmanager fuer Grafana-managed Alerts standardmaessig — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-06-24-alerting--grafana-cloud-uses-the-internal-alertmanager-for-grafana-managed-alerts-by-default/)
- Organize your synthetic monitoring checks in folders — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-06-23-organize-your-synthetic-monitoring-checks-in-folders/)
- Grafana Assistant ist in Grafana Enterprise vorinstalliert — irrelevant, da nur Enterprise → [What's new](https://grafana.com/whats-new/2026-06-23-grafana-assistant-is-now-pre-installed-in-grafana-enterprise/)
