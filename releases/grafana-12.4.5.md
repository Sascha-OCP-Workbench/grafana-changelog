# Grafana v12.4.5

_Veroeffentlicht: 2026-06-23_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.5)

## Breaking Changes
- **Datasources:** `PUT /api/datasources/uid/:uid` liefert jetzt HTTP 400, wenn die UID im Payload nicht mit der UID in der URL uebereinstimmt — Automatisierungen und Provisioning-Skripte, die abweichende UIDs senden, muessen angepasst werden ([#125769](https://github.com/grafana/grafana/pull/125769)).

## Hilfreiche neue Funktionen
- Keine.

## Hilfreiche Informationen
- **Docker:** Die Alpine-basierten Images wurden auf 3.24.1 angehoben ([#126538](https://github.com/grafana/grafana/pull/126538)).
- Reines Patch-Release mit einem Bugfix und einem Image-Update; weitere Aenderungen sind in der Quelle nicht aufgefuehrt.
