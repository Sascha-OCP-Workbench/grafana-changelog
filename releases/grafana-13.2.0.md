# Grafana v13.2.0

_Veroeffentlicht: 2026-08-18_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.0)

_Uebersicht: [What's new in v13.2.0](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v13-2/)_

## Breaking Changes
- **Alerting:** Das Feature-Flag `alertingSaveStateCompressed` wurde entfernt; Konfigurationen, die es setzen, muessen bereinigt werden ([#129135](https://github.com/grafana/grafana/pull/129135)).
- **Dashboards:** Scripted Dashboards sind deprecated und standardmaessig deaktiviert — bei weiterer Nutzung muss die Option explizit aktiviert bzw. migriert werden ([#130207](https://github.com/grafana/grafana/pull/130207)).
- **Alerting:** Die Notifications-API wurde auf `v1beta1` migriert; Automatisierungen gegen die alte API-Version muessen angepasst werden ([#124702](https://github.com/grafana/grafana/pull/124702)).
- **Alerting:** Bei Provenance-Mismatch auf Contact Points liefert die API nun 403 statt 500 — Fehlerbehandlung in Skripten pruefen ([#127699](https://github.com/grafana/grafana/pull/127699)).
- **Unified Storage:** Der Default fuer den Garbage-Collection-Dry-Run steht jetzt auf `false`, d.h. GC laeuft real ([#130533](https://github.com/grafana/grafana/pull/130533)).
- **Home:** Die neue vereinheitlichte Homepage ist fuer alle Nutzer aktiv, das zugehoerige Feature-Flag entfaellt ([#129054](https://github.com/grafana/grafana/pull/129054)). → [What's new](https://grafana.com/whats-new/2026-08-18-revamped-homepage-for-grafana/)
- **Dashboards:** Die neuen View-Panel-Controls sind standardmaessig aktiv und aendern das Bedienverhalten ([#129187](https://github.com/grafana/grafana/pull/129187)). → [What's new](https://grafana.com/whats-new/2026-08-11-explore-busy-panels-with-the-new-view-panel-sidebar/)
- **Dashboard:** Dashboard-Settings-Tabs leiten auf die Sidebar-Entsprechungen um; verlinkte URLs koennen sich aendern ([#125966](https://github.com/grafana/grafana/pull/125966)).
- **Provisioning:** Git-Sync-Conventions und User-Attribution sind per Default aktiv (Public Preview) ([#130670](https://github.com/grafana/grafana/pull/130670), [#130671](https://github.com/grafana/grafana/pull/130671)).

## Hilfreiche neue Funktionen
- **Provisioning:** Commits koennen als Signer authored bzw. der Git-Sync-Commit-Autor ueberschrieben werden ([#127969](https://github.com/grafana/grafana/pull/127969), [#130547](https://github.com/grafana/grafana/pull/130547)). → [What's new](https://grafana.com/whats-new/2026-08-18-authoring-commits-in-git-sync/)
- **Provisioning:** Webhooks fuer GitLab und Bitbucket inkl. UI stehen zur Verfuegung ([#127204](https://github.com/grafana/grafana/pull/127204), [#128649](https://github.com/grafana/grafana/pull/128649), [#127806](https://github.com/grafana/grafana/pull/127806)). → [What's new](https://grafana.com/whats-new/2026-08-18-webhooks-available-for-gitlab-and-bitbucket/)
- **Provisioning:** Jobs werden Autor und Herkunft zugeordnet und in den Recent Jobs angezeigt ([#128819](https://github.com/grafana/grafana/pull/128819), [#128820](https://github.com/grafana/grafana/pull/128820), [#127984](https://github.com/grafana/grafana/pull/127984)).
- **Provisioning:** Resources-Tab mit Filter fuer Out-of-Sync-Ressourcen, faltbarem Baum und Sync-Status fuer Playlists ([#128456](https://github.com/grafana/grafana/pull/128456), [#128453](https://github.com/grafana/grafana/pull/128453), [#127021](https://github.com/grafana/grafana/pull/127021)).
- **Provisioning:** Migration nach GitOps unterstuetzt Branch-Auswahl, Paginierung, Ordnerpfade und Job-Fehleranzeige ([#128562](https://github.com/grafana/grafana/pull/128562), [#128356](https://github.com/grafana/grafana/pull/128356), [#128042](https://github.com/grafana/grafana/pull/128042), [#127936](https://github.com/grafana/grafana/pull/127936)).
- **Provisioning:** Vollstaendiger Pull statt inkrementellem Sync erzwingbar sowie konfigurierbares Per-Resource-Write-Timeout ([#128330](https://github.com/grafana/grafana/pull/128330), [#127862](https://github.com/grafana/grafana/pull/127862)).
- **Provisioning:** Webhooks lassen sich pro Repository/Connection deaktivieren ([#126790](https://github.com/grafana/grafana/pull/126790)).
- **Alerting:** Neuer Import-Tab in den Alerting-Settings inkl. Import-to-GMA-Wizard mit Notification-Templates, Promote/Auto-Sync, Staged-Config-Uebersicht und Revert ([#129051](https://github.com/grafana/grafana/pull/129051), [#128329](https://github.com/grafana/grafana/pull/128329), [#126907](https://github.com/grafana/grafana/pull/126907), [#129204](https://github.com/grafana/grafana/pull/129204), [#129243](https://github.com/grafana/grafana/pull/129243)).
- **Tracing:** Neuer File-Exporter schreibt Traces als OTLP/JSON, inklusive Dokumentation ([#128679](https://github.com/grafana/grafana/pull/128679), [#129339](https://github.com/grafana/grafana/pull/129339)). → [What's new](https://grafana.com/whats-new/2026-08-18-export-traces-of-grafana-to-a-file-for-easier-troubleshooting/)
- **Azure Monitor:** Backend-Implementierung der Azure Metrics Batch API sowie Caching von Subscription-Lookups ([#123696](https://github.com/grafana/grafana/pull/123696), [#123556](https://github.com/grafana/grafana/pull/123556)). → [What's new](https://grafana.com/whats-new/2026-08-18-azure-monitor-batch-api/)
- **QueryVariable:** Der Query-Variable-Editor wurde neu gestaltet ([#127048](https://github.com/grafana/grafana/pull/127048)). → [What's new](https://grafana.com/whats-new/2026-07-13-create-query-variables-more-easily-with-the-redesigned-editor/)
- **Dashboards:** Thresholds unterstuetzen jetzt Variablen-Interpolation ([#128451](https://github.com/grafana/grafana/pull/128451)). → [What's new](https://grafana.com/whats-new/2026-07-29-panel-thresholds-variable-interpolation/)
- **Dashboards:** Verschachtelungstiefe auf 4 erhoeht, nested Tabs moeglich; Query-Fehler und Notices werden gebuendelt angezeigt ([#129174](https://github.com/grafana/grafana/pull/129174), [#127436](https://github.com/grafana/grafana/pull/127436)).
- **Live:** `ha_engine_address` unterstuetzt `redis://` und `rediss://` (TLS) Verbindungs-URLs ([#129938](https://github.com/grafana/grafana/pull/129938)).
- **Plugins:** Neues Feature-Toggle zum Erzwingen von TLS 1.3 ([#130390](https://github.com/grafana/grafana/pull/130390)).
- **Logs:** Mehr Suggested Fields mit Anbindung an die neue Logs Table; Debug-Level nun in Grau ([#128002](https://github.com/grafana/grafana/pull/128002), [#129896](https://github.com/grafana/grafana/pull/129896)).
- **CloudWatch Logs:** Frontend-Unterstuetzung fuer Abfragen nach Data Source ([#123742](https://github.com/grafana/grafana/pull/123742)).
- **Table/DashList/Trace View:** Dynamische Höhe fuer Cell-Tooltips, Dashboard-Beschreibung als Tooltip und Trace-to-Logs-Button nur bei vorhandenen Logs ([#127107](https://github.com/grafana/grafana/pull/127107), [#130006](https://github.com/grafana/grafana/pull/130006), [#128702](https://github.com/grafana/grafana/pull/128702)).
- **Folder API:** Legacy-Access-Control-Logik durch App-Platform-API-Aufruf ersetzt ([#125642](https://github.com/grafana/grafana/pull/125642)).

## Hilfreiche Informationen
- **Security:** Behebung von CVE-2026-17183; kein dokumentierter Konfigurationsaufwand, Update empfohlen.
- **Go:** Die Build-Toolchain wurde auf Go 1.26.5 aktualisiert ([#128011](https://github.com/grafana/grafana/pull/128011)).
- **SQLite:** Der Journal-Mode wird zurueckgesetzt, wenn WAL deaktiviert ist ([#130695](https://github.com/grafana/grafana/pull/130695)).
- **Auth:** Parallele Login-Pings werden dedupliziert und Session-Token-Rotation bei nicht-session-authentifizierten Requests uebersprungen ([#129927](https://github.com/grafana/grafana/pull/129927), [#129920](https://github.com/grafana/grafana/pull/129920)).
- **PostgreSQL:** Data-Source-Init scheitert nicht mehr bei `maxOpenConns=0`; Epoch-ms-Strings werden korrekt geparst ([#122556](https://github.com/grafana/grafana/pull/122556), [#122693](https://github.com/grafana/grafana/pull/122693)).
- **Provisioning:** Zahlreiche Stabilitaetsfixes u.a. bei Job-Lease-Erneuerung, Claim-Ownership in Multi-Pod-Setups, idempotenter GitHub-Webhook-Erstellung und Export von v0-Dashboards als v1 ([#127786](https://github.com/grafana/grafana/pull/127786), [#127783](https://github.com/grafana/grafana/pull/127783), [#128068](https://github.com/grafana/grafana/pull/128068), [#128357](https://github.com/grafana/grafana/pull/128357)).
- **Alerting:** Fixes fuer geloeschte Time Intervals in managed Routes, faelschlich angezeigten "Inhibited"-Status und Provenance-Verlust beim Zuruecksetzen der Default-Route ([#129247](https://github.com/grafana/grafana/pull/129247), [#130264](https://github.com/grafana/grafana/pull/130264), [#130553](https://github.com/grafana/grafana/pull/130553)).
- **Alerting:** Das Feature-Toggle `AlertingCentralHistory` wurde entfernt ([#130164](https://github.com/grafana/grafana/pull/130164)).
- **Transformations:** Fixes bei Filter-by-value mit Regex und Null-Werten, Extract-fields-Deduplizierung, Inner Join und Gazetteer-Lookups; Merge series/tables bleibt bei einer einzelnen Serie verfuegbar ([#129572](https://github.com/grafana/grafana/pull/129572), [#129889](https://github.com/grafana/grafana/pull/129889), [#129576](https://github.com/grafana/grafana/pull/129576), [#129568](https://github.com/grafana/grafana/pull/129568), [#129569](https://github.com/grafana/grafana/pull/129569)).
- **Logs Table:** Fixes fuer Datenexport, fehlende Ergebnisse beim Streaming, Feld-/Displayname-Vermischung und haengende Filter ([#130245](https://github.com/grafana/grafana/pull/130245), [#128870](https://github.com/grafana/grafana/pull/128870), [#128677](https://github.com/grafana/grafana/pull/128677), [#128398](https://github.com/grafana/grafana/pull/128398)).
- **Dashboards:** Fixes fuer Panel-Header-Abstaende, Ladeindikator-Clipping, stale Daten bei verketteten Dashboard-Datasources und Datasource-Picker-Hervorhebung ([#128910](https://github.com/grafana/grafana/pull/128910), [#128040](https://github.com/grafana/grafana/pull/128040), [#126378](https://github.com/grafana/grafana/pull/126378), [#126948](https://github.com/grafana/grafana/pull/126948)).
- **Navigation:** Die `orgId` wird nun bei allen Navigationen mitgegeben ([#120978](https://github.com/grafana/grafana/pull/120978)).
- **Accessibility:** Verbesserte Screenreader-Ansagen fuer `InlineToast`, Variablen-Edit-Seiten und `aria-current` in der Pagination ([#128488](https://github.com/grafana/grafana/pull/128488), [#130706](https://github.com/grafana/grafana/pull/130706), [#128494](https://github.com/grafana/grafana/pull/128494)).
- **Plugin-Entwicklung:** `PageLoader` ist in `@grafana/ui` verfuegbar; Fixes fuer Combobox-Doppelanfragen und Tag-Crash bei ungueltigem `colorIndex` ([#124597](https://github.com/grafana/grafana/pull/124597), [#129788](https://github.com/grafana/grafana/pull/129788), [#129579](https://github.com/grafana/grafana/pull/129579)).
- **SqlExpressions:** Tabellennamen mit Leerzeichen werden korrekt geparst ([#117615](https://github.com/grafana/grafana/pull/117615)).

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- Git Sync Support fuer GitHub Enterprise (inkl. Webhooks, Dashboard Previews) — irrelevant, da nur Enterprise. → [What's new](https://grafana.com/whats-new/2026-08-18-git-sync-support-for-github-enterprise/)
- Alert enrichment — irrelevant, da nur Enterprise/Cloud. → [What's new](https://grafana.com/whats-new/2026-08-24-alert-enrichment/)
- Provisioning: OAuth-App-Connections fuer GitLab und Bitbucket sowie GitLab-Webhook-Lifecycle (Enterprise-Anteile) — irrelevant, da nur Enterprise.
- Reporting: Template-Variablen ohne Typ-Allowlist und gebuendelte Dashboard-Lookups — irrelevant, da nur Enterprise.
- Auditing/Analytics: Benutzername in Audit-Logs bei User-Loeschung, Public-Dashboard-UID in Loki-Usage-Insights — irrelevant, da nur Enterprise.
- Secrets: RBAC-Fix fuer die AWS-Keeper-Creation-Route — irrelevant, da nur Enterprise.
