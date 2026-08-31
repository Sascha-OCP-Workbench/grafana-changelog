# Grafana v13.0.4

_Veroeffentlicht: 2026-07-21_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.4)

## Breaking Changes
- Alerting: Bei Provenance-Mismatch an Contact Points wird nun HTTP 403 statt 500 zurueckgegeben — Clients/Automatisierungen, die auf 500 reagieren, muessen angepasst werden ([#127815](https://github.com/grafana/grafana/pull/127815)).

## Hilfreiche neue Funktionen
- Provisioning: Verbesserte Fehlermeldungen in den Formularen fuer GitHub-Verbindungen ([#128209](https://github.com/grafana/grafana/pull/128209)).

## Hilfreiche Informationen
- Go-Version auf 1.26.5 aktualisiert ([#128016](https://github.com/grafana/grafana/pull/128016)).
- Dashboard: Fehler bei Interval-Variablen mit Auto-Wert behoben ([#127053](https://github.com/grafana/grafana/pull/127053)).
- Provisioning: Anlegen von GitHub-Webhooks ist jetzt idempotent; Repositories bleiben nicht mehr mit HTTP 422 im Status "unhealthy" haengen ([#128196](https://github.com/grafana/grafana/pull/128196)).
- Alerting: ORM-Table-Mapping-Bug behoben, der auf PostgreSQL zu SELECT von alert_rule-Spalten aus der Tabelle user fuehrte ([#128751](https://github.com/grafana/grafana/pull/128751)).
