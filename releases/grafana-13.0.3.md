# Grafana v13.0.3

_Veroeffentlicht: 2026-06-23_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.3)

## Breaking Changes
- Die API `PUT /api/datasources/uid/:uid` liefert nun HTTP 400, wenn die UID im Payload nicht der UID in der URL entspricht — automatisierte Clients/Skripte muessen entsprechend konsistente UIDs senden.

## Hilfreiche neue Funktionen
- Provisioning: Beim Anlegen von Dashboards in neuen Ordnern wird jetzt eine `_folder.json` geschrieben.
- Provisioning: Auch beim Verschieben von Dashboards in neue Ordner wird eine `_folder.json` geschrieben.

## Hilfreiche Informationen
- Docker: Die Alpine-basierten Images wurden auf 3.24.1 aktualisiert (enthaelt aktuelle Base-Image-Patches).
- Provisioning: PR-Kommentare funktionieren jetzt korrekt auf Grafana-Instanzen mit mehreren Organisationen.
- Provisioning: PR-Links sind korrekt, wenn ein Ordner ueber die UI umbenannt wird.
- Provisioning: Repositories im Status "terminating" werden bei der Validierung des Loeschens einer Connection ignoriert.
- Fehlerhafte MySQL-Query in der Migration der Spalte `datasource_type` wurde korrigiert — relevant fuer Upgrades mit MySQL-Backend.
