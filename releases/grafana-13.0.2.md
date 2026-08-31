# Grafana v13.0.2

_Veroeffentlicht: 2026-06-09_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.2)

## Breaking Changes
- **LibraryPanels:** Bei unzureichenden Berechtigungen liefert die API nun HTTP 403 statt 500, was Clients mit Status-Code-Auswertung betreffen kann ([#123467](https://github.com/grafana/grafana/pull/123467)).
- **Provisioning:** Die Eindeutigkeit von Repositories wird jetzt ueber die Kombination (URL, branch, path) bestimmt; bestehende Repository-Definitionen sind entsprechend zu pruefen ([#124121](https://github.com/grafana/grafana/pull/124121)).

## Hilfreiche neue Funktionen
- **Provisioning:** Neue Instanz-Einstellung `public_root_url` fuer externe URLs ([#124258](https://github.com/grafana/grafana/pull/124258)).
- **Provisioning:** Validierungsfehler wie zu lange Folder-UIDs und weitere 4xx werden als Sync-Warnungen sichtbar gemacht ([#123888](https://github.com/grafana/grafana/pull/123888)).
- **Provisioning:** Ordner werden nicht mehr allein wegen `_folder.json`-Metadaten als "pending" markiert ([#124139](https://github.com/grafana/grafana/pull/124139)).
- **Provisioning:** Ruleset-Bypass wird bei der Validierung des Write-Workflows beruecksichtigt ([#124128](https://github.com/grafana/grafana/pull/124128)).
- **Provisioning:** Git-Pushes verhandeln receive-pack-Capabilities ([#124130](https://github.com/grafana/grafana/pull/124130)); zudem Per-Verb-Fallback fuer die files-Subresource ([#123900](https://github.com/grafana/grafana/pull/123900)).
- **Dashboards:** Anzeige des k8s-Formats beim Speichern provisionierter Dashboards ([#123045](https://github.com/grafana/grafana/pull/123045)).
- **Homepage:** Unterstuetzung fuer v2-Dashboards, wenn sie per Datei definiert sind ([#123029](https://github.com/grafana/grafana/pull/123029)).

## Hilfreiche Informationen
- **Security:** Behobene CVEs: CVE-2026-9029, CVE-2026-33382, CVE-2026-42127, CVE-2026-42129, CVE-2026-10601, CVE-2026-8609, CVE-2026-8595.
- **Basis-Images/Runtime:** Alpine-basierte Docker-Images auf 3.23.4 ([#122938](https://github.com/grafana/grafana/pull/122938)) und Go auf 1.26.3 ([#124454](https://github.com/grafana/grafana/pull/124454)) angehoben.
- **DashboardDS:** Mixed-Panels aktualisieren sich wieder bei Zeitbereichswechsel mit veralteten Upstreams ([#124894](https://github.com/grafana/grafana/pull/124894)).
- **K8s Dashboards:** Ordner-Berechtigungspruefung nutzt nun `dashboards:create` ([#124942](https://github.com/grafana/grafana/pull/124942)).
- **PostgreSQL:** `sql_engine` liefert wieder Ergebnisse fuer EXPLAIN-Queries ([#123246](https://github.com/grafana/grafana/pull/123246)).
- **Jaeger:** Korrekte Einheitenumrechnung von Log-Event-Timestamps in der Trace-Ansicht ([#123707](https://github.com/grafana/grafana/pull/123707)).
- **Provisioning:** nanogit auf v0.17.0 aktualisiert, behebt Pushes bei Repositories mit Git-Modulen ([#124140](https://github.com/grafana/grafana/pull/124140)).
- **RBAC (Enterprise):** Quick Fix fuer globale Datasource-Berechtigungen.
