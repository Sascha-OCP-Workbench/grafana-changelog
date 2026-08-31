# Grafana v12.2.10

_Veroeffentlicht: 2026-06-23_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.2.10)

## Breaking Changes
- `PUT /api/datasources/uid/:uid` antwortet jetzt mit HTTP 400, wenn die UID im Payload nicht mit der UID in der URL übereinstimmt — betrifft Automatisierung/Provisionierung, die bisher abweichende UIDs sendet ([#125518](https://github.com/grafana/grafana/pull/125518)).

## Hilfreiche neue Funktionen
- Keine.

## Hilfreiche Informationen
- Die Alpine-basierten Docker-Images wurden auf Alpine 3.24.1 aktualisiert ([#126546](https://github.com/grafana/grafana/pull/126546)).
- Reines Patch-Release ohne weitere gemeldete Änderungen.
