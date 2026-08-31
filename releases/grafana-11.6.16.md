# Grafana v11.6.16

_Veroeffentlicht: 2026-06-23_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v11.6.16)

## Breaking Changes
- `PUT /api/datasources/uid/:uid` antwortet nun mit HTTP 400, wenn die UID im Payload nicht der UID in der URL entspricht — Automatisierungen/Provisionierungs-Skripte, die abweichende UIDs senden, muessen angepasst werden ([#125516](https://github.com/grafana/grafana/pull/125516)).

## Hilfreiche neue Funktionen
- Keine.

## Hilfreiche Informationen
- Die Alpine-basierten Docker-Images wurden auf Alpine 3.24.1 aktualisiert ([#126547](https://github.com/grafana/grafana/pull/126547)).
- Reines Patch-Release: ein Bugfix (Datasource-API-Validierung) und ein Base-Image-Update, keine weiteren Aenderungen dokumentiert.
