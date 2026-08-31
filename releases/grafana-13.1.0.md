# Grafana v13.1.0

_Veroeffentlicht: 2026-07-01_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.0)

## Breaking Changes
- **Prometheus:** Azure- und SigV4-Authentifizierung wurden aus der Core-Prometheus-Datenquelle entfernt ([#123089](https://github.com/grafana/grafana/pull/123089)) — bestehende Datenquellen mit dieser Auth-Konfiguration muessen umgestellt werden.
- **Prometheus:** Das Paket `@grafana/prometheus` wurde entfernt ([#123035](https://github.com/grafana/grafana/pull/123035)); Plugins mit Abhaengigkeit darauf muessen angepasst werden.
- **Zipkin:** Die Zipkin-Datenquelle ist kein Core-Plugin mehr ([#124148](https://github.com/grafana/grafana/pull/124148)) und muss bei weiterer Nutzung separat installiert werden.
- **Removal:** Die GroupAttributeSync-Routen wurden entfernt ([#126247](https://github.com/grafana/grafana/pull/126247)).
- **Dashboard/DTO:** Die Property `isStarred` wurde aus dem Dashboard-DTO entfernt ([#122118](https://github.com/grafana/grafana/pull/122118)).
- **Alerting:** Die Provisioning-Endpunkte fuer Notifications sind als deprecated markiert ([#121995](https://github.com/grafana/grafana/pull/121995)) — Migration einplanen.
- **Feature Toggles entfernt:** `dashboardScene`/`publicDashboardsScene` ([#121781](https://github.com/grafana/grafana/pull/121781)), `logsPanelControls` ([#122114](https://github.com/grafana/grafana/pull/122114)), `alertRuleUseFiredAtForStartsAt` ([#124677](https://github.com/grafana/grafana/pull/124677)) sowie das Toggle fuer das neue Panel-Padding ([#124870](https://github.com/grafana/grafana/pull/124870)).
- **Datasources:** `PUT /api/datasources/uid/:uid` liefert nun 400, wenn die UID im Payload nicht zur URL passt ([#125398](https://github.com/grafana/grafana/pull/125398)).
- **Provisioning:** Die GET-Methode des Webhook-Connectors wurde entfernt ([#125539](https://github.com/grafana/grafana/pull/125539)) und bei Aenderung der Provisioning-URL ist ein neuer Token erforderlich ([#125525](https://github.com/grafana/grafana/pull/125525)); zudem wird die Repository-Eindeutigkeit auf (URL, Branch, Pfad) eingeschraenkt ([#123498](https://github.com/grafana/grafana/pull/123498)).
- **CloudWatch Logs:** Data Links wurden aus den Ergebnissen entfernt ([#120348](https://github.com/grafana/grafana/pull/120348)).
- **Stats:** Die Dashboard-Version-Metrik wurde entfernt ([#121900](https://github.com/grafana/grafana/pull/121900)) — betrifft bestehende Dashboards/Alerts auf diese Metrik.
- **Migration:** `team.updated` wird auf MySQL auf `DATETIME(3)` erweitert ([#124314](https://github.com/grafana/grafana/pull/124314)) — Schema-Migration beim Upgrade.
- **Alerting:** E-Mail-Kontaktpunkte sind auf Org-Mitglieder beschraenkt ([#123173](https://github.com/grafana/grafana/pull/123173)); Reporting-E-Mails koennen ebenfalls per Config auf Org-Mitglieder begrenzt werden (Enterprise).
- **Enterprise:** Die Legacy-`CsvExportPage` wurde entfernt.

## Hilfreiche neue Funktionen
- **Git Sync:** Verified Commits mit GPG-, SSH- und S/MIME-Signaturschluesseln inkl. Konfigurations-UI ([#126023](https://github.com/grafana/grafana/pull/126023)).
- **Git Sync:** Dashboard-Import direkt in provisionierte Ordner sowie Sync auf Root-Ebene ohne uebergeordneten Ordner (GA).
- **Git Sync:** `README.md` aus dem Repository wird in provisionierten Ordnern angezeigt (Public Preview).
- **Provisioning:** Robustheits- und Sicherheitsverbesserungen wie periodische Rotation des Webhook-Secrets ([#122797](https://github.com/grafana/grafana/pull/122797)), Replay-Schutz fuer GitHub-Webhooks ([#125550](https://github.com/grafana/grafana/pull/125550)), Validierung des `ref`-Query-Parameters ([#125551](https://github.com/grafana/grafana/pull/125551)) und Full Sync bei zu grossem Diff ([#123127](https://github.com/grafana/grafana/pull/123127)).
- **Provisioning:** Neue Instanz-Einstellung `public_root_url` fuer externe URLs ([#123613](https://github.com/grafana/grafana/pull/123613)).
- **Auth:** JWT-Authentifizierung unterstuetzt nun Inline-Public-Keys ([#126184](https://github.com/grafana/grafana/pull/126184)); Requests an Grafana.com nutzen einen dedizierten Token ([#122269](https://github.com/grafana/grafana/pull/122269)).
- **Alerting:** Kontaktpunkt-Integrationstypen koennen eingeschraenkt werden ([#118858](https://github.com/grafana/grafana/pull/118858)) und Speicher-/Bulk-Delete-Fehler werden in der UI sichtbar ([#123211](https://github.com/grafana/grafana/pull/123211), [#123690](https://github.com/grafana/grafana/pull/123690)).
- **Alerting:** Grafana-managed Rules koennen ohne Gruppe erstellt werden ([#120228](https://github.com/grafana/grafana/pull/120228)), neues Feature Flag `alerting.rulesAPIV2` ([#122606](https://github.com/grafana/grafana/pull/122606)) und Alert-Rule-Drawer direkt aus dem Panel-Menue ([#125712](https://github.com/grafana/grafana/pull/125712)).
- **Alerting:** Vorschau des Notification-Routings in der Alert-Instances-Tabelle ([#121699](https://github.com/grafana/grafana/pull/121699)) sowie Auto-Sync-Konfiguration fuer Mimir Alertmanager auf der Settings-Seite ([#124855](https://github.com/grafana/grafana/pull/124855)).
- **Alerting:** Sender-Metriken fuer externe Alertmanager enthalten nun Datenquellen-UIDs ([#121996](https://github.com/grafana/grafana/pull/121996)); Plugin-Rule-Origin wird als `X-Rule-Origin`-Header propagiert ([#125206](https://github.com/grafana/grafana/pull/125206)).
- **Alerting:** Bearbeiten von Plugin-bereitgestellten und provisionierten Rule Groups ist blockiert ([#123214](https://github.com/grafana/grafana/pull/123214)).
- **Dashboards:** Neue Panel-Screenshot-API ([#124045](https://github.com/grafana/grafana/pull/124045)) und Annotation-CRUD in der Mutation-API ([#123939](https://github.com/grafana/grafana/pull/123939)).
- **Dashboards:** Quick Filters und Group-by-Control, Panel-Styles inkl. Copy/Paste, Section-Level-Variablen fuer Rows/Tabs, Multi-Property-Variablen, Annotations-Clustering und die "Time series to table"-Transformation sind GA.
- **Dashboards:** Neue Series-visibility-Filter in der Time-Series-Visualisierung sowie Sidebar-/Toolbar-Verbesserungen im neuen Dashboard-Erlebnis.
- **Dashboards:** Nested Tables mit ueberarbeitetem "Group to nested tables"-Editor und Field Overrides in Sub-Tables (Public Preview, [#121646](https://github.com/grafana/grafana/pull/121646)).
- **Query Editor:** Ueberarbeiteter Query-Editor in Public Preview mit Multi-Select, Bulk-Aktionen und Stacked View.
- **Data Source:** Neue Option `forward_user_agent` zur Weitergabe des Client-User-Agents ([#124244](https://github.com/grafana/grafana/pull/124244)).
- **Logs:** Erweiterte Log Details (Ein-/Ausklappen, Keyboard-Navigation, Ad-hoc-Filter), Kopieren von Logeintraegen als JSON, sticky Log-Line-Menue, optionaler Download in Dashboards und neues Log Level "unspecified".
- **Expressions:** Memory-Limit fuer binaere Operationen in Math-Expressions ([#121945](https://github.com/grafana/grafana/pull/121945)).
- **Pyroscope:** Unterstuetzung der Heatmap-Query-API ([#120995](https://github.com/grafana/grafana/pull/120995)).
- **Grafana Assistant:** In Grafana Enterprise vorinstalliert (Public Preview) und unterstuetzt acht neue Datenquellen (u. a. Snowflake, MongoDB, Oracle, Elasticsearch, Dynatrace, Zabbix, Jira).
- **PDC:** Private Data Source Connect unterstuetzt nun MQTT, GitHub und IBM Db2 (Cloud/Enterprise).
- **Accessibility:** Farbfehlsichtigkeitsfreundliche Linienmuster ([#121386](https://github.com/grafana/grafana/pull/121386)), barrierefreie Dashboard-Variablen ([#120758](https://github.com/grafana/grafana/pull/120758)) und diverse Kontrast-/ARIA-Verbesserungen.
- **Secrets Keeper (Enterprise):** Keeper koennen ueber die UI erstellt (AWS-Wizard), bearbeitet, aktiviert/deaktiviert und geloescht werden.

## Hilfreiche Informationen
- **Security:** Die Security-Patches vom Mai 2026 wurden eingespielt ([#124824](https://github.com/grafana/grafana/pull/124824)).
- **Security:** Gravatar-E-Mail-Identifier nutzen nun SHA-256 ([#122319](https://github.com/grafana/grafana/pull/122319)); der `redirectTo`-Cookie im OAuth-Login wird URL-encodiert ([#121953](https://github.com/grafana/grafana/pull/121953)).
- **Basis-Images/Runtime:** Alpine-Images auf 3.23.4 bzw. 3.24.1 aktualisiert ([#122930](https://github.com/grafana/grafana/pull/122930), [#126529](https://github.com/grafana/grafana/pull/126529)), Go auf 1.25.9 ([#122094](https://github.com/grafana/grafana/pull/122094)), Scenes auf v8 ([#123698](https://github.com/grafana/grafana/pull/123698)).
- **Datasources:** InfluxDB, MSSQL, PostgreSQL, Tempo und Graphite wurden in Backend und Frontend entkoppelt ([#119167](https://github.com/grafana/grafana/pull/119167), [#119169](https://github.com/grafana/grafana/pull/119169), [#119110](https://github.com/grafana/grafana/pull/119110), [#119106](https://github.com/grafana/grafana/pull/119106)).
- **Alerting-Bugfixes:** Behoben wurden u. a. ein ORM-Table-Mapping-Fehler auf PostgreSQL ([#124935](https://github.com/grafana/grafana/pull/124935)), Crashes bei leeren Rule-Group-Arrays ([#122704](https://github.com/grafana/grafana/pull/122704)), fehlende Permission-Pruefung der Routing-Preview ([#122344](https://github.com/grafana/grafana/pull/122344)) sowie case-insensitive Redaction von Contact-Point-Settings ([#124955](https://github.com/grafana/grafana/pull/124955)).
- **Provisioning-Bugfixes:** nanogit auf v0.17.0 fuer Pushes mit Git-Modulen ([#124114](https://github.com/grafana/grafana/pull/124114)), Fix fuer doppelte Ordner beim Full Sync ([#124256](https://github.com/grafana/grafana/pull/124256)) und fuer PR-Kommentare in Multi-Org-Instanzen ([#126700](https://github.com/grafana/grafana/pull/126700)).
- **Datenbank-Fixes:** Fehlerhafte MySQL-Query in der `datasource_type`-Spaltenmigration korrigiert ([#126821](https://github.com/grafana/grafana/pull/126821)); Unified-Storage-Migrationen werden bei bereits migriertem Dualwrite-State uebersprungen ([#122866](https://github.com/grafana/grafana/pull/122866)).
- **API-Verhalten:** Library Panels liefern bei fehlenden Rechten 403 statt 500 ([#123407](https://github.com/grafana/grafana/pull/123407)); Ordner-Permission-Check fuer K8s-Dashboards nutzt `dashboards:create` ([#124612](https://github.com/grafana/grafana/pull/124612)).
- **Weitere Fixes:** Home-Page-Redirect unter Subpath ([#124557](https://github.com/grafana/grafana/pull/124557)), Tempo gRPC Basic Auth ohne TLS ([#123026](https://github.com/grafana/grafana/pull/123026)), PostgreSQL EXPLAIN-Ergebnisse ([#122739](https://github.com/grafana/grafana/pull/122739)) und Loki Step-Option fuer alle Query-Typen ([#122184](https://github.com/grafana/grafana/pull/122184)).
- **Plugin-Entwicklung:** Verbesserungen an `Card`, `Combobox`, `DataLinkInput`, `RadioButton(Group)` und `TimeOfDayPicker`; `datasourceSrv` wird durch neue asynchrone APIs/Hooks ersetzt ([#123037](https://github.com/grafana/grafana/pull/123037)).
- **Sonstiges:** `en-US`-Localization-Ressourcen werden nicht mehr geladen ([#125327](https://github.com/grafana/grafana/pull/125327)); Plugin-Header-Werte werden fuer gRPC auf druckbares ASCII sanitisiert ([#122237](https://github.com/grafana/grafana/pull/122237)).
- Empfohlene Vorgehensweise beim Upgrade steht im offiziellen Upgrade Guide und im [What's-new-Dokument zu v13.1](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v13-1/).
