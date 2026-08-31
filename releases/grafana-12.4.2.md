# Grafana v12.4.2

_Veroeffentlicht: 2026-03-25_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.2)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- **Plugins:** AWS-SDK-Credential-Chain-Umgebungsvariablen werden nun an externe AWS-Plugins weitergereicht ([#120209](https://github.com/grafana/grafana/pull/120209)).
- **Dashboards:** Anzeigenamen in der Version History werden anhand der Identity aufgeloest ([#120273](https://github.com/grafana/grafana/pull/120273)).
- **Dashboards a11y:** Das Time-Zone-Menue oeffnet sich nicht mehr allein beim Fokussieren ([#120388](https://github.com/grafana/grafana/pull/120388)).
- **Public Dashboards:** Unbeabsichtigte CRUD-Operationen ueber Organisationsgrenzen hinweg werden verhindert ([#120457](https://github.com/grafana/grafana/pull/120457)).

## Hilfreiche Informationen
- **Security:** Behebt CVE-2026-27876, CVE-2026-27877, CVE-2026-27879, CVE-2026-27880, CVE-2026-28375 und CVE-2026-33375 — Update wird empfohlen.
- **IAM:** NULL-Werte in der Spalte `team_member.external` werden korrekt behandelt, wodurch fehlschlagendes Laden von Dashboards behoben ist ([#120179](https://github.com/grafana/grafana/pull/120179)).
- **Plugins:** `PLUGIN_UNIX_SOCKET_DIR` wird an Plugin-Prozesse weitergegeben und behebt Probleme mit dem tmp-Verzeichnis in restriktiven Umgebungen ([#120275](https://github.com/grafana/grafana/pull/120275)).
- **Plugins:** Fehlerhafte `IsDisabled`-Bedingung im Installer korrigiert ([#120568](https://github.com/grafana/grafana/pull/120568)).

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- **Analytics tab:** Verbesserte Voice-over-Accessibility — irrelevant, da nur Enterprise.
