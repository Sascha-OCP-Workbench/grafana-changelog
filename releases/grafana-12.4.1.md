# Grafana v12.4.1

_Veroeffentlicht: 2026-03-09_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.1)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- Der Image Renderer unterstuetzt nun eigene CA-Zertifikate, was den Betrieb hinter internen TLS-Terminierungen bzw. mit privater PKI erleichtert ([#118859](https://github.com/grafana/grafana/pull/118859)).
- Beim Loeschen einer Datenquelle wird der Scope-Resolver-Cache im AccessControl invalidiert, sodass Berechtigungen nicht auf veralteten Scopes basieren ([#118741](https://github.com/grafana/grafana/pull/118741)).

## Hilfreiche Informationen
- Patch-Release ohne Funktionsumbrueche; enthaelt im Wesentlichen Wartungsarbeiten und Bugfixes.
- Go-Toolchain auf 1.25.8 aktualisiert ([#119693](https://github.com/grafana/grafana/pull/119693)).
- Alerting: Der Scope beim Testen neuer Receiver nutzt jetzt einen unterstuetzten Resource Type ([#118495](https://github.com/grafana/grafana/pull/118495)).
- Alerting: Migration `CollateAlertRuleGroup` fuer MariaDB-Kompatibilitaet korrigiert — relevant fuer Installationen mit MariaDB-Backend ([#119028](https://github.com/grafana/grafana/pull/119028)).

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- AccessControl: Korrektur eines Test-Utilities fuer das Aufraeumen von Datenquellen-Loeschberechtigungen — irrelevant, da nur Enterprise.
