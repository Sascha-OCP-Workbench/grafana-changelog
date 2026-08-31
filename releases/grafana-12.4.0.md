# Grafana v12.4.0

_Veroeffentlicht: 2026-02-25_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.0)

_Uebersicht: [What's new in v12.4.0](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-4/)_

## Breaking Changes
- **Dashboards:** Die veralteten Dashboard-Endpunkte auf Basis interner IDs wurden entfernt ([#117227](https://github.com/grafana/grafana/pull/117227)) — Integrationen muessen auf UID-basierte Endpunkte umgestellt werden.
- **DataSources:** API-Routen mit Namen und internen IDs sind deprecated ([#116391](https://github.com/grafana/grafana/pull/116391)); zusaetzlich nutzt die SQL-Datenquelle nun UID statt interner ID ([#116461](https://github.com/grafana/grafana/pull/116461)).
- **DashboardsAPI:** `/api/dashboards/home` ist deprecated ([#115333](https://github.com/grafana/grafana/pull/115333)).
- **Chore:** Die experimentelle Restore-Dashboard-API ist deprecated ([#116256](https://github.com/grafana/grafana/pull/116256)) und die experimentelle API `/dashboards/calculate-diff` wurde entfernt ([#114151](https://github.com/grafana/grafana/pull/114151)).
- **Datasources:** Experimentelle API-Gruppennamen verwenden jetzt vollstaendige Plugin-IDs ([#112961](https://github.com/grafana/grafana/pull/112961)) — Clients gegen diese API-Gruppen anpassen.
- **Feature Toggles entfernt:** `pinNavItems`, `unifiedHistory`, `logRequestsInstrumentedAsUnknown`, `individualCookiePreferences`, `permissionsFilterRemoveSubquery`, `postgresDSUsePGX`, `logRowsPopoverMenu`, `logsInfiniteScrolling`, `exploreMetricsRelatedLogs` sowie `web_vitals_attribution_enabled` (Faro v2) — entsprechende Konfiguration bereinigen.
- **CloudMigrations:** Das Feature-Toggle wurde entfernt und durch eine Config-Einstellung zum Deaktivieren ersetzt ([#114223](https://github.com/grafana/grafana/pull/114223)).
- **Alerting:** Die OpsGenie-Integration ist deprecated ([#117085](https://github.com/grafana/grafana/pull/117085)).
- **Alerting:** Standard-Benachrichtigungskonfiguration nutzt nun einen leeren Receiver ([#116368](https://github.com/grafana/grafana/pull/116368)); Regeln koennen nicht mehr in git-synchronisierte Ordner gespeichert werden ([#114944](https://github.com/grafana/grafana/pull/114944)).
- **Alerting:** DB-Migrationen aendern die Kollation der Spalten `alert_rule.namespace_uid` und `rule_group` auf binaer ([#115152](https://github.com/grafana/grafana/pull/115152), [#114365](https://github.com/grafana/grafana/pull/114365)).
- **Alerting:** Pending Period wird jetzt auch auf NoData- und Error-Alerts angewendet ([#117024](https://github.com/grafana/grafana/pull/117024)) — geaendertes Alarmverhalten pruefen.
- **Chore:** Deprecated `language_provider`-Methoden im Prometheus-Paket wurden entfernt ([#114361](https://github.com/grafana/grafana/pull/114361)) — betrifft Plugin-Entwicklung.
- **Panels:** Das Datagrid-Panel ist deprecated ([#116071](https://github.com/grafana/grafana/pull/116071)), das Radialbar-Gauge-Plugin wurde entfernt ([#116722](https://github.com/grafana/grafana/pull/116722)) und der `Gauge`-Export in `grafana/ui` ist deprecated ([#116436](https://github.com/grafana/grafana/pull/116436)).
- **Cleanup:** Die CSV-Drag-and-Drop-Snapshot-Query-Funktion wurde entfernt ([#113645](https://github.com/grafana/grafana/pull/113645)).
- **Correlations:** Unterstuetzung fuer `org_id=0` entfernt ([#116877](https://github.com/grafana/grafana/pull/116877)).
- **GrafanaBootData:** `config.apps` und `config.panels` sind deprecated ([#115610](https://github.com/grafana/grafana/pull/115610), [#116918](https://github.com/grafana/grafana/pull/116918)) — Plugins anpassen.
- **Library Elements:** Query-Parameter `folderFilter` ist deprecated, stattdessen `folderFilterUIDs` verwenden ([#116048](https://github.com/grafana/grafana/pull/116048)).
- **Folders:** Die Methode `getFolderByUID` ist deprecated ([#113173](https://github.com/grafana/grafana/pull/113173)).
- **Chore:** Das Feature-Toggle `localeFormatPreference` ist deprecated ([#116621](https://github.com/grafana/grafana/pull/116621)).
- **New Logs Panel:** Die neue Logs-Visualisierung ist standardmaessig aktiv ([#113340](https://github.com/grafana/grafana/pull/113340)) — Darstellung bestehender Dashboards pruefen.
- **PanelChrome:** Neues Panel-Padding ist standardmaessig aktiv ([#114492](https://github.com/grafana/grafana/pull/114492)).
- **Short URL:** Standard-Ablaufzeit fuer Short URLs ist jetzt "never" ([#115029](https://github.com/grafana/grafana/pull/115029)).
- **Avatar:** Avatar-Endpunkt erfordert nun Anmeldung ([#116891](https://github.com/grafana/grafana/pull/116891)).
- **Grafana Monitoring:** Native HTTP-Histogramme sind standardmaessig aktiv, klassische Histogramme werden konfigurierbar ([#116534](https://github.com/grafana/grafana/pull/116534)) — Dashboards/Recording Rules pruefen.
- **Config:** `skip migrations` ist in der `defaults.ini` gesetzt ([#114007](https://github.com/grafana/grafana/pull/114007)) — Konfiguration beim Upgrade verifizieren.
- **CloudWatch:** Der "Match exact"-Toggle ist standardmaessig deaktiviert ([#113314](https://github.com/grafana/grafana/pull/113314)) und Logs-Abfragen nutzen `logGroupIdentifiers` nur noch fuer Monitoring Accounts ([#113137](https://github.com/grafana/grafana/pull/113137)).
- **Chore:** Drilldown Investigations wurde entfernt ([#115471](https://github.com/grafana/grafana/pull/115471)).

## Hilfreiche neue Funktionen
- **Dashboard provisioning:** Unterstuetzung fuer das v2-Schema ([#113620](https://github.com/grafana/grafana/pull/113620)).
- **Provisioning:** Dashboards koennen ueber das JSON-Modell bearbeitet werden ([#115420](https://github.com/grafana/grafana/pull/115420)), GitHub-App-Verbindungen sind in den Wizard integriert ([#116547](https://github.com/grafana/grafana/pull/116547)).
- **Dashboards:** Per-Panel-Filterung fuer Timeseries ([#114499](https://github.com/grafana/grafana/pull/114499)) und Regex fuer die Anzeige von Variablenwerten ([#114426](https://github.com/grafana/grafana/pull/114426)).
- **Dashboard:** Neue experimentelle Time-Range-Zoom-Shortcuts und Time-Range-Pan sind als GA aktiviert ([#114190](https://github.com/grafana/grafana/pull/114190), [#116970](https://github.com/grafana/grafana/pull/116970)).
- **Dynamic Dashboards:** Neuer "Add panel"-Button mit Drag & Drop, standardmaessig geoeffnete Outline und ausgegraute versteckte Variablen ([#116276](https://github.com/grafana/grafana/pull/116276), [#114146](https://github.com/grafana/grafana/pull/114146), [#115723](https://github.com/grafana/grafana/pull/115723)).
- **Alerting:** Neue Tab-Navigation fuer Alert Rules, gespeicherte Suchen und eine Alert-Activity-Karte auf der Alerting-Startseite ([#116253](https://github.com/grafana/grafana/pull/116253), [#115001](https://github.com/grafana/grafana/pull/115001), [#115822](https://github.com/grafana/grafana/pull/115822)).
- **Alerting:** Import-Wizard fuer Prometheus-Regeln nach Grafana Alerting inkl. konfigurierbarer Default-Datenquelle ([#116924](https://github.com/grafana/grafana/pull/116924), [#115665](https://github.com/grafana/grafana/pull/115665)).
- **Alerting:** Protected Fields fuer Contact Points und dedizierte Permission fuer die Template-Testing-API ([#115442](https://github.com/grafana/grafana/pull/115442), [#115032](https://github.com/grafana/grafana/pull/115032)).
- **Alerting:** Alert-Labels werden als Tags an Annotations uebernommen ([#116244](https://github.com/grafana/grafana/pull/116244)).
- **Alerting:** Komprimiertes periodisches Speichern von Alert-Instances und Performance-Verbesserungen der Alerts-Seite ([#111803](https://github.com/grafana/grafana/pull/111803), [#113391](https://github.com/grafana/grafana/pull/113391)).
- **Alerting:** Label `folder_uid` an der Metrik `grafana_alerting_rule_group_rules` ([#115129](https://github.com/grafana/grafana/pull/115129)).
- **Alerting:** Groessenlimits fuer expandierte Notification-Templates ([#115242](https://github.com/grafana/grafana/pull/115242)).
- **Auth:** SSO-Settings-PATCH-Endpunkt sowie Validierung von OAuth-ID-Token-Signaturen ([#117346](https://github.com/grafana/grafana/pull/117346), [#116442](https://github.com/grafana/grafana/pull/116442)).
- **IAM:** Refresh Tokens koennen bei aktiviertem `use_refresh_token` optional erzwungen werden ([#114174](https://github.com/grafana/grafana/pull/114174)).
- **Grafana CLI:** Neues Kommando `admin flush-rbac-seed-assignment` ([#116716](https://github.com/grafana/grafana/pull/116716)).
- **Plugins:** Experimenteller Sandbox-Modus fuer Community-Plugins ([#115936](https://github.com/grafana/grafana/pull/115936)).
- **Live:** Konfigurierbare `client_queue_max_size` ([#114225](https://github.com/grafana/grafana/pull/114225)).
- **Elasticsearch:** Serverless-Verbindungen, Raw-Query-Editor fuer DSL und konfigurierbarer Default-Query-Mode ([#114855](https://github.com/grafana/grafana/pull/114855), [#114066](https://github.com/grafana/grafana/pull/114066), [#112540](https://github.com/grafana/grafana/pull/112540)).
- **PostgreSQL/MySQL:** Unterstuetzung fuer Variable-Query-Editoren ([#115974](https://github.com/grafana/grafana/pull/115974), [#116900](https://github.com/grafana/grafana/pull/116900)).
- **MSSQL:** Authentifizierung als aktueller Benutzer ([#113977](https://github.com/grafana/grafana/pull/113977)).
- **Prometheus:** Gefiltertes `/series`-Endpoint fuer Versionen ohne `match[]`-Parameter und optimierte Regex fuer Multi-Value-Label-Matcher ([#116648](https://github.com/grafana/grafana/pull/116648), [#116233](https://github.com/grafana/grafana/pull/116233)).
- **CloudWatch:** `cloudwatchBatchQueries` ist GA, Anomaly-Command-Unterstuetzung und Log-Group-Auswahl fuer OpenSearch SQL-Queries ([#117448](https://github.com/grafana/grafana/pull/117448), [#113311](https://github.com/grafana/grafana/pull/113311), [#116222](https://github.com/grafana/grafana/pull/116222)).
- **Cloud Monitoring:** Unterstuetzung fuer Google Cloud `universe_domain` ([#115931](https://github.com/grafana/grafana/pull/115931)).
- **Logs Panel:** Transformationen bei Infinite Scrolling, unwrapped Logs mit optionalen Spalten und client-seitige Suche im Popover-Menue ([#116528](https://github.com/grafana/grafana/pull/116528), [#117402](https://github.com/grafana/grafana/pull/117402), [#114653](https://github.com/grafana/grafana/pull/114653)).
- **Explore:** Neue Table-Komponente, Keyboard-Shortcut zum Ausfuehren von Queries und persistierte Sortierreihenfolge in der URL ([#111463](https://github.com/grafana/grafana/pull/111463), [#115811](https://github.com/grafana/grafana/pull/115811), [#114350](https://github.com/grafana/grafana/pull/114350)).
- **Geomap:** Min/Max-Zoom-Optionen und Variablen-Unterstuetzung im XYZ-Tile-Layer ([#114947](https://github.com/grafana/grafana/pull/114947), [#116654](https://github.com/grafana/grafana/pull/116654)).
- **Heatmap:** Unterstuetzung fuer lineare Y-Achse ([#113337](https://github.com/grafana/grafana/pull/113337)).
- **SQL Expressions:** Neuer Schema-Inspector-Panel und `NOT`-Keyword in der Allow-List ([#113545](https://github.com/grafana/grafana/pull/113545), [#116802](https://github.com/grafana/grafana/pull/116802)).
- **FieldColor:** Barrierefreie Farbpaletten ([#114424](https://github.com/grafana/grafana/pull/114424)).
- **Playlists:** Graduierung auf v1-APIs ([#117638](https://github.com/grafana/grafana/pull/117638)).
- **Folders:** Owner References werden verwaltet und auf den Ordner-Detailseiten angezeigt ([#117426](https://github.com/grafana/grafana/pull/117426), [#116843](https://github.com/grafana/grafana/pull/116843)).
- **Dashboard/AppChrome:** Sidebar wird in Kiosk-Modus, bei laufender Playlist und mobil im View-Modus ausgeblendet ([#115387](https://github.com/grafana/grafana/pull/115387), [#115414](https://github.com/grafana/grafana/pull/115414), [#117369](https://github.com/grafana/grafana/pull/117369)).
- **Plugin Metrics:** Verbesserte Metriken fuer langlaufende Queries ([#116371](https://github.com/grafana/grafana/pull/116371)).

## Hilfreiche Informationen
- **Security:** HTML in der TraceView wird sanitisiert ([#117853](https://github.com/grafana/grafana/pull/117853)) und bei deaktivierter Zeitauswahl wird die Dashboard-Zeitspanne verwendet ([#117854](https://github.com/grafana/grafana/pull/117854)).
- **API:** Fehlende Scope-Pruefung bei Dashboards ergaenzt ([#116885](https://github.com/grafana/grafana/pull/116885)).
- **Dependencies:** Go wurde auf 1.25.5 bis 1.25.7 aktualisiert ([#114749](https://github.com/grafana/grafana/pull/114749), [#116394](https://github.com/grafana/grafana/pull/116394), [#117470](https://github.com/grafana/grafana/pull/117470)).
- **Dashboards:** Memory Leak in der CUE-Validierung behoben durch begrenzte Kontext-Wiederverwendung ([#114818](https://github.com/grafana/grafana/pull/114818)).
- **Dashboard:** Float-Werte fuer x/y/w/h werden beim Import gerundet ([#117072](https://github.com/grafana/grafana/pull/117072)).
- **Graphite:** Aenderungen an der Namenskonvention wurden zurueckgenommen ([#117158](https://github.com/grafana/grafana/pull/117158)).
- **Prometheus:** Aenderung "Min Step hat Vorrang" wurde revertiert ([#116959](https://github.com/grafana/grafana/pull/116959)); robusteres Unmarshalling von `PromQueryFormat` ([#116670](https://github.com/grafana/grafana/pull/116670)).
- **Cloudwatch:** Fehlende Default-Region wird als Downstream-Fehler markiert ([#117551](https://github.com/grafana/grafana/pull/117551)); `grafana-aws-sdk` auf 1.4.2 aktualisiert ([#115855](https://github.com/grafana/grafana/pull/115855)).
- **Azure Monitor:** Verbesserte Spaltenbehandlung und Filter-Reset im Logs-Query-Builder ([#114667](https://github.com/grafana/grafana/pull/114667), [#116329](https://github.com/grafana/grafana/pull/116329)).
- **Elasticsearch:** Keyed Filter Buckets werden korrekt verarbeitet und der Code-Editor wird beim Wechsel des Query-Typs geleert ([#113478](https://github.com/grafana/grafana/pull/113478), [#116318](https://github.com/grafana/grafana/pull/116318)).
- **Preferences:** API-Validierung ergaenzt und Doku aktualisiert ([#116045](https://github.com/grafana/grafana/pull/116045)).
- **Live:** Verwendet nun Namespace statt OrgID ([#117275](https://github.com/grafana/grafana/pull/117275)).
- **Search:** Experimentelles `panelTitleSearch` von searchV2 in die Unified Search verschoben ([#116326](https://github.com/grafana/grafana/pull/116326)).
- **Chore:** Verbessertes `packaging/docker/run.sh` ([#114012](https://github.com/grafana/grafana/pull/114012)).
- **Neue Feature Flags:** u.a. `alertingSyncNotifiersApiMigration` ([#117946](https://github.com/grafana/grafana/pull/117946)), `secretsKeeperUI` ([#117427](https://github.com/grafana/grafana/pull/117427)) und `timeRangePan` ([#112988](https://github.com/grafana/grafana/pull/112988)).
- **Restore dashboards:** Verbesserte Berechtigungspruefung ([#116266](https://github.com/grafana/grafana/pull/116266)).
- **News Panel:** `pubDate` faellt bei Bedarf auf das Updated-Datum zurueck ([#113329](https://github.com/grafana/grafana/pull/113329)).
- Hinweis: Der What's-new-Katalog enthaelt fuer dieses Release keine passenden datierten Eintraege; die Einordnung basiert ausschliesslich auf den Release Notes.

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- **Alerting Enrichment:** Neue RBAC-Permissions sowie UI fuer Enrichments (Scoping, Query-Visualisierung) — irrelevant, da nur Enterprise.
- **Alerting:** AI-Helper in Triage und Assistant-basierte Template-Buttons — irrelevant, da nur Enterprise.
- **Auditing:** Konfigurierbare Loki-Retries/Timeouts und UID-basiertes Tracking von Dashboard-Endpunkten — irrelevant, da nur Enterprise.
- **Datasources Auth Service** inkl. Unterstuetzung fuer AWS-Temp-Credentials — irrelevant, da nur Enterprise.
- **Feat:** Experimenteller Sandbox-Modus fuer Community- & PPT-Plugins (Enterprise-Variante) — irrelevant, da nur Enterprise.
- **Reporting:** Entfernung des `newPDFRendering`-Flags, dynamische Schriftverkleinerung fuer PDF-Tabellen und Template-Variablen fuer Dashboards v2 — irrelevant, da nur Enterprise.
- **Secrets Keeper:** UI-Shell mit Tab-Navigation — irrelevant, da nur Enterprise.
- **Chore:** Access API mit zusaetzlichen Query-Parametern — irrelevant, da nur Enterprise.
