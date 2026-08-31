# Grafana v12.4.3

_Veroeffentlicht: 2026-04-14_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.3)

## Breaking Changes
- **Alerting:** Das Praefix der Cluster-Metriken des HA-Alertmanagers hat sich mit Grafana 12.4 geaendert und ist nun dokumentiert — bestehende Dashboards, Recording Rules und Alerts auf diese Metriken muessen angepasst werden ([#121481](https://github.com/grafana/grafana/pull/121481)).

## Hilfreiche neue Funktionen
- Keine.

## Hilfreiche Informationen
- **Analytics:** Die interne Dashboard-ID wird beibehalten, wodurch Analytics-/Usage-Daten konsistent bleiben ([#121417](https://github.com/grafana/grafana/pull/121417)).
- **Go:** Update der Go-Toolchain auf 1.25.9 (Wartungs- und Sicherheitsstand des Runtimes) ([#122095](https://github.com/grafana/grafana/pull/122095)).
- Reines Patch-Release ohne weitere funktionale Aenderungen fuer die Open-Source-Variante.

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- **Reporting:** `appSubURL` wird bei Requests auf die Report-Einstellungen korrekt angewendet — irrelevant, da nur Enterprise.
