# Grafana v13.1.1

_Veroeffentlicht: 2026-07-21_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.1)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- Provisioning: Der Write-Timeout pro Ressource beim Sync ist nun konfigurierbar ([#127868](https://github.com/grafana/grafana/pull/127868)).
- Provisioning: Verbesserte Fehlermeldungen im Formular fuer GitHub-Connections ([#128177](https://github.com/grafana/grafana/pull/128177)).

## Hilfreiche Informationen
- Go-Version auf 1.26.5 aktualisiert ([#128015](https://github.com/grafana/grafana/pull/128015)).
- Bugfix Provisioning: Anlegen von GitHub-Webhooks ist jetzt idempotent, Repos bleiben nicht mehr mit HTTP 422 im Status "unhealthy" haengen ([#128201](https://github.com/grafana/grafana/pull/128201)).
- Bugfix DashboardDS: Verkettete Panels mit Dashboard-Datenquelle zeigen keine veralteten Daten mehr ([#127248](https://github.com/grafana/grafana/pull/127248)).
- Accessibility: Inhalte von `InlineToast` werden von Screenreadern angekuendigt ([#128687](https://github.com/grafana/grafana/pull/128687)).
- Plugin-Entwicklung: `Pagination` setzt `aria-current` auf der aktiven Seite ([#128518](https://github.com/grafana/grafana/pull/128518)).
