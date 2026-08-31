# Grafana v12.4.6

_Veroeffentlicht: 2026-07-21_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.6)

## Breaking Changes
- **Alerting:** Die Provisioning-API prueft nun die Autorisierung fuer protected fields, wodurch bisher erfolgreiche Provisioning-Aufrufe abgelehnt werden koennen ([#127940](https://github.com/grafana/grafana/pull/127940)).
- **Alerting:** Bei Provenance-Konflikten an Contact Points liefert die API jetzt HTTP 403 statt 500, was Fehlerbehandlung in Automatisierungen betreffen kann ([#127814](https://github.com/grafana/grafana/pull/127814)).

## Hilfreiche neue Funktionen
- **Jaeger:** Komprimierte API-Antworten (gzip, deflate, brotli) werden nun verarbeitet ([#128062](https://github.com/grafana/grafana/pull/128062)).

## Hilfreiche Informationen
- **Go:** Update der Go-Version auf 1.26.5 ([#128017](https://github.com/grafana/grafana/pull/128017)).
- **Alerting:** Fehler im ORM-Table-Mapping behoben, der auf PostgreSQL zu `SELECT`-Abfragen von alert_rule-Spalten gegen die Tabelle `user` fuehrte ([#128753](https://github.com/grafana/grafana/pull/128753)).
- Bezugsquellen: [Download-Seite 12.4.6](https://grafana.com/grafana/download/12.4.6) und [What's new](https://grafana.com/docs/grafana/latest/whatsnew/); eine spezifische What's-new-Doku zu diesem Patch-Release liegt nicht vor.
