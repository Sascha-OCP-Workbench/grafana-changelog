# Grafana v12.3.9

_Veroeffentlicht: 2026-07-21_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.3.9)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- Alerting: Bei Provenance-Konflikten an Contact Points liefert die API nun HTTP 403 statt 500, was Provisioning-Fehler klarer erkennbar macht.

## Hilfreiche Informationen
- Alerting: Bugfix eines ORM-Table-Mapping-Fehlers, der auf PostgreSQL `alert_rule`-Spalten gegen die Tabelle `user` selektierte.
- Go-Toolchain auf Version 1.26.5 aktualisiert (enthaltene Upstream-Fixes wirken sich auf das Grafana-Binary aus).
- Reines Patch-Release ohne neue Konfigurations- oder Migrationsschritte; Download unter [grafana.com/grafana/download/12.3.9](https://grafana.com/grafana/download/12.3.9).

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- Keine.
