# Grafana v12.4.4

_Veroeffentlicht: 2026-06-09_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.4)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- **LibraryPanels:** Bei unzureichenden Berechtigungen wird nun HTTP 403 statt 500 zurueckgegeben, was Fehlerauswertung und Monitoring erleichtert ([#123470](https://github.com/grafana/grafana/pull/123470)).
- **Plugins:** Header-Werte werden auf druckbares ASCII bereinigt, um gRPC-Kompatibilitaetsprobleme zu vermeiden ([#122474](https://github.com/grafana/grafana/pull/122474)).
- **Browse dashboards:** Elemente bleiben beim Zoomen sichtbar und ordnen sich besser an ([#120678](https://github.com/grafana/grafana/pull/120678)).
- **Graphite:** Bei erkanntem `aliasSub`-Wrapping wird der getaggte Pfad aus `tags.name` entfernt ([#122619](https://github.com/grafana/grafana/pull/122619)).

## Hilfreiche Informationen
- **Security:** Das Release behebt CVE-2026-9029, CVE-2026-33382, CVE-2026-42127, CVE-2026-42129, CVE-2026-10601, CVE-2026-8609 und CVE-2026-8595; ein Update wird empfohlen.
- **Basis-Images/Runtime:** Alpine-basierte Docker-Images auf 3.23.4 und Go auf 1.26.3 angehoben ([#123027](https://github.com/grafana/grafana/pull/123027), [#124456](https://github.com/grafana/grafana/pull/124456)).
- **Alerting:** Sichtbarkeit des AlertManagerPicker prueft jetzt vorhandene Alertmanager-Datenquellen ([#124073](https://github.com/grafana/grafana/pull/124073)).
- **Alerting:** Ein "not found"-Fehler beim Abruf von Plugins wird als "nicht installiert" behandelt ([#122989](https://github.com/grafana/grafana/pull/122989)).
- **DashboardDS:** Mixed-Panels aktualisieren sich wieder bei Zeitbereichsaenderungen trotz veralteter Upstreams ([#124893](https://github.com/grafana/grafana/pull/124893)).
- **Jaeger:** Zeitstempel-Einheitenumrechnung fuer Log-Events in der Trace-Ansicht korrigiert ([#123711](https://github.com/grafana/grafana/pull/123711)).
- **PostgreSQL:** `sql_engine` liefert nun Ergebnisse fuer EXPLAIN-Queries ([#123245](https://github.com/grafana/grafana/pull/123245)).
