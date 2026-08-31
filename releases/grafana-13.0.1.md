# Grafana v13.0.1

_Veroeffentlicht: 2026-04-17_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.1)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- Dashboard: Die Zeitzonen-Einstellung des Users bleibt bei der Konvertierung von Dashboard-Schema V1 nach V2 erhalten ([#122673](https://github.com/grafana/grafana/pull/122673)).
- Provisioning: Dashboard-Validierungsfehler werden nun als Kommentar im zugehoerigen Pull Request ausgegeben ([#122433](https://github.com/grafana/grafana/pull/122433)).

## Hilfreiche Informationen
- Unified storage: Migrationen werden uebersprungen, wenn der dualwrite-State sie bereits als ausgefuehrt markiert ([#122880](https://github.com/grafana/grafana/pull/122880)).
- Reines Patch-Release ohne Security-Hinweise in den Release Notes; Download unter [grafana.com/grafana/download/13.0.1](https://grafana.com/grafana/download/13.0.1).
