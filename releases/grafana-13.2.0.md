# Grafana v13.2.0

_Veroeffentlicht: 2026-08-18_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.0)

_Uebersicht: [What's new in v13.2.0](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v13-2/)_

## Breaking Changes
- **Alerting:** Das Feature-Flag `alertingSaveStateCompressed` wurde entfernt; entsprechende Konfigurationseintraege muessen bereinigt werden ([#129135](https://github.com/grafana/grafana/pull/129135)).
- **Dashboards:** Scripted Dashboards sind deprecated und standardmaessig deaktiviert; bei weiterer Nutzung ist ein explizites Aktivieren noetig, Entfernung in Grafana 14 geplant ([#130207](https://github.com/grafana/grafana/pull/130207)).
- **Alerting:** Die Notifications-API wurde auf `v1beta1` migriert; API-Clients und Provisionierung muessen angepasst werden ([#124702](https://github.com/grafana/grafana/pull/124702)).
- **Alerting:** Bei Provenance-Konflikten an Contact Points wird nun HTTP 403 statt 500 zurueckgegeben, was Automatisierungen mit Fehlerbehandlung betreffen kann ([#127699](https://github.com/grafana/grafana/pull/127699)).
- **Unified Storage:** Der Default fuer den Garbage-Collection-Dry-Run wurde auf `false` gesetzt, d. h. GC loescht jetzt tatsaechlich ([#130533](https://github.com/grafana/grafana/pull/130533)).
- **Home:** Die neue Unified Homepage ist ohne Feature-Flag fuer alle Nutzer aktiv ([#129054](https://github.com/grafana/grafana/pull/129054)) → [What's new](https://grafana.com/whats-new/2026-08-18-revamped-homepage-for-grafana/)
- **Dashboards:** Die neuen View-Panel-Controls sind standardmaessig aktiv ([#129187](https://github.com/grafana/grafana/pull/129187)) → [What's new](https://grafana.com/whats-new/2026-08-11-explore-busy-panels-with-the-new-view-panel-sidebar/)
- **Dashboard:** Die Dashboard-Settings-Tabs leiten auf die neuen Sidebar-Pendants um; Deep-Links auf Tabs koennen betroffen sein ([#125966](https://github.com/grafana/grafana/pull/125966)).
- **Provisioning:** Git-Sync-Conventions, User-Attribution und der GitHub-Enterprise-Provider sind standardmaessig aktiviert ([#130670](https://github.com/grafana/grafana/pull/130670), [#130671](https://github.com/grafana/grafana/pull/130671), [#128376](https://github.com/grafana/grafana/pull/128376)).
- **Alerting:** `AlertingCentralHistory`-Feature-Toggle entfernt ([#130164](https://github.com/grafana/grafana/pull/130164)).

## Hilfreiche neue Funktionen
- **Tracing:** Neuer File-Exporter schreibt Traces als OTLP/JSON zur einfacheren Fehlersuche, inkl. Doku ([#128679](https://github.com/grafana/grafana/pull/128679), [#129339](https://github.com/grafana/grafana/pull/129339)) → [What's new](https://grafana.com/whats-new/2026-08-18-export-traces-of-grafana-to-a-file-for-easier-troubleshooting/)
- **Azure Monitor:** Backend-Implementierung der Azure Metrics Batch API sowie Caching von Subscription-Lookups ([#123696](https://github.com/grafana/grafana/pull/123696), [#123556](https://github.com/grafana/grafana/pull/123556)) → [What's new](https://grafana.com/whats-new/2026-08-18-azure-monitor-batch-api/)
- **Provisioning:** Commits koennen als Signer authored bzw. der Git-Sync-Commit-Author ueberschrieben werden ([#127969](https://github.com/grafana/grafana/pull/127969), [#127970](https://github.com/grafana/grafana/pull/127970), [#130547](https://github.com/grafana/grafana/pull/130547)) → [What's new](https://grafana.com/whats-new/2026-08-18-authoring-commits-in-git-sync/)
- **Provisioning:** Webhook-Unterstuetzung und -UI fuer GitLab und Bitbucket ([#127204](https://github.com/grafana/grafana/pull/127204), [#128649](https://github.com/grafana/grafana/pull/128649), [#127806](https://github.com/grafana/grafana/pull/127806)) → [What's new](https://grafana.com/whats-new/2026-08-18-webhooks-available-for-gitlab-and-bitbucket/)
- **Provisioning:** Jobs werden Autor und Herkunft zugeordnet und in "Recent jobs" angezeigt ([#128819](https://github.com/grafana/grafana/pull/128819), [#128820](https://github.com/grafana/grafana/pull/128820), [#127984](https://github.com/grafana/grafana/pull/127984)).
- **Provisioning:** Migration zu GitOps unterstuetzt Branch-Auswahl, Paginierung, Ordnerpfade, Filter fuer out-of-sync Ressourcen und einen erzwingbaren Full Pull ([#128562](https://github.com/grafana/grafana/pull/128562), [#128356](https://github.com/grafana/grafana/pull/128356), [#128042](https://github.com/grafana/grafana/pull/128042), [#128454](https://github.com/grafana/grafana/pull/128454), [#128456](https://github.com/grafana/grafana/pull/128456), [#128330](https://github.com/grafana/grafana/pull/128330)).
- **Provisioning:** Per-Resource-Write-Timeout beim Sync ist konfigurierbar und Webhooks lassen sich pro Repository deaktivieren ([#127862](https://github.com/grafana/grafana/pull/127862), [#126790](https://github.com/grafana/grafana/pull/126790)).
- **Alerting:** Neuer Import-Tab in den Alerting-Settings inkl. Import-to-GMA-Wizard mit Notification-Templates, Promote/Auto-Sync, Staged-Config-Uebersicht und Revert ([#129051](https://github.com/grafana/grafana/pull/129051), [#128329](https://github.com/grafana/grafana/pull/128329), [#126907](https://github.com/grafana/grafana/pull/126907), [#129204](https://github.com/grafana/grafana/pull/129204), [#129243](https://github.com/grafana/grafana/pull/129243)).
- **Live:** `ha_engine_address` unterstuetzt jetzt `redis://` und `rediss://` (TLS) ([#129938](https://github.com/grafana/grafana/pull/129938)).
- **Plugins:** Neues Feature-Toggle zum Erzwingen von TLS 1.3 fuer Plugin-Verbindungen ([#130390](https://github.com/grafana/grafana/pull/130390)).
- **Dashboards:** Thresholds unterstuetzen Variablen-Interpolation ([#128451](https://github.com/grafana/grafana/pull/128451)) → [What's new](https://grafana.com/whats-new/2026-07-29-panel-thresholds-variable-interpolation/)
- **QueryVariable:** Neu gestalteter Query-Variable-Editor ([#127048](https://github.com/grafana/grafana/pull/127048)) → [What's new](https://grafana.com/whats-new/2026-07-13-create-query-variables-more-easily-with-the-redesigned-editor/)
- **Dashboards:** Verschachtelungstiefe auf 4 erhoeht, verschachtelte Tabs moeglich, Panel-Fehler und -Hinweise in einer UI zusammengefasst ([#129174](https://github.com/grafana/grafana/pull/129174), [#127436](https://github.com/grafana/grafana/pull/127436)).
- **Logs:** Mehr Suggested Fields mit Integration in die neue Logs Table sowie angepasste Farben fuer Debug-Level und Log-Highlighting ([#128002](https://github.com/grafana/grafana/pull/128002), [#129896](https://github.com/grafana/grafana/pull/129896), [#130516](https://github.com/grafana/grafana/pull/130516)).
- **CloudWatch Logs:** Frontend-Unterstuetzung fuer Abfragen nach Data Source ([#123742](https://github.com/grafana/grafana/pull/123742)).
- **Folder API:** Legacy-Access-Control-Logik durch App-Platform-API-Aufruf ersetzt ([#125642](https://github.com/grafana/grafana/pull/125642)).
- **Table/DashList/Trace View:** Dynamisch hohe Cell-Tooltips, Dashboard-Beschreibung als Tooltip in DashList und Trace-to-Logs-Button nur bei vorhandenen Logs ([#127107](https://github.com/grafana/grafana/pull/127107), [#130006](https://github.com/grafana/grafana/pull/130006), [#128702](https://github.com/grafana/grafana/pull/128702)).
- **Transformations:** "Merge series/tables" bleibt auch bei einer einzelnen Datenserie verfuegbar ([#129569](https://github.com/grafana/grafana/pull/129569)).

## Hilfreiche Informationen
- **Security:** Das Release enthaelt einen Fix fuer CVE-2026-17183.
- **Go:** Aktualisierung der Go-Version auf 1.26.5 ([#128011](https://github.com/grafana/grafana/pull/128011)).
- **SQLite:** Der Journal-Mode wird zurueckgesetzt, wenn WAL deaktiviert ist ([#130695](https://github.com/grafana/grafana/pull/130695)).
- **PostgreSQL:** Fix fuer fehlgeschlagene Datenquellen-Initialisierung bei `maxOpenConns=0` sowie korrektes Parsen von Epoch-ms-Strings (kein NaN mehr) ([#122556](https://github.com/grafana/grafana/pull/122556), [#122693](https://github.com/grafana/grafana/pull/122693)).
- **Auth:** Gleichzeitige Login-Pings werden dedupliziert und Session-Token-Rotation wird bei nicht-session-authentifizierten Requests uebersprungen ([#129927](https://github.com/grafana/grafana/pull/129927), [#129920](https://github.com/grafana/grafana/pull/129920)).
- **Alerting:** Fixes fuer faelschlich angezeigtes "Inhibited", Provenance-Verlust beim Zuruecksetzen der Default-Route und Pruefung managed Routes beim Loeschen von Time Intervals ([#130264](https://github.com/grafana/grafana/pull/130264), [#130553](https://github.com/grafana/grafana/pull/130553), [#129247](https://github.com/grafana/grafana/pull/129247)).
- **Provisioning:** Zahlreiche Stabilitaetsfixes fuer Job-Leases, Multi-Pod-Betrieb, idempotente GitHub-Webhook-Erstellung, Export von v0-Dashboards als v1 und Multi-Org-Usage-Stats ([#127783](https://github.com/grafana/grafana/pull/127783), [#127786](https://github.com/grafana/grafana/pull/127786), [#128068](https://github.com/grafana/grafana/pull/128068), [#128357](https://github.com/grafana/grafana/pull/128357), [#127465](https://github.com/grafana/grafana/pull/127465)).
- **Logs Table:** Fixes fuer Datenexport, fehlende Ergebnisse beim Streaming, Feld-/Anzeigenamen-Mix und haengenbleibende Filter ([#130245](https://github.com/grafana/grafana/pull/130245), [#128870](https://github.com/grafana/grafana/pull/128870), [#128677](https://github.com/grafana/grafana/pull/128677), [#128398](https://github.com/grafana/grafana/pull/128398)).
- **Transformations:** Fixes fuer Filter-by-value-Regex mit Null-Werten, Gazetteer-Field-Lookup, Feldnamen-Deduplizierung in "Extract fields" und Inner Join bei verworfenen Frames ([#129572](https://github.com/grafana/grafana/pull/129572), [#129568](https://github.com/grafana/grafana/pull/129568), [#129889](https://github.com/grafana/grafana/pull/129889), [#129576](https://github.com/grafana/grafana/pull/129576)).
- **Dashboards/Panels:** Fixes fuer Gauge-Gradienten bei negativen Thresholds, Panel-Header-Abstaende, Ladeindikator-Clipping, veraltete Daten bei verketteten Dashboard-Datasources und Datasource-Picker-Highlighting ([#128532](https://github.com/grafana/grafana/pull/128532), [#128910](https://github.com/grafana/grafana/pull/128910), [#128040](https://github.com/grafana/grafana/pull/128040), [#126378](https://github.com/grafana/grafana/pull/126378), [#126948](https://github.com/grafana/grafana/pull/126948)).
- **Navigation:** Die `orgId` wird bei allen Navigationen injiziert ([#120978](https://github.com/grafana/grafana/pull/120978)).
- **SqlExpressions:** Tabellennamen mit Leerzeichen werden korrekt geparst ([#117615](https://github.com/grafana/grafana/pull/117615)).
- **Azure Monitor:** Fix der Migration von Dimension-Filtern ([#128786](https://github.com/grafana/grafana/pull/128786)).
- **Accessibility:** `InlineToast` wird von Screenreadern angesagt und Section-Headings auf Variablen-Seiten korrekt ausgegeben ([#128488](https://github.com/grafana/grafana/pull/128488), [#130706](https://github.com/grafana/grafana/pull/130706)).
- **Plugin-Entwicklung:** `PageLoader` ist in `@grafana/ui` verfuegbar, Combobox-Fixes bei asynchronen Requests, `aria-current` in Pagination und Crash-Fix im `Tag`-Component ([#124597](https://github.com/grafana/grafana/pull/124597), [#129788](https://github.com/grafana/grafana/pull/129788), [#128494](https://github.com/grafana/grafana/pull/128494), [#129579](https://github.com/grafana/grafana/pull/129579)).
- **ColorScale:** Live-`hoverValue` entfernt, auch aus dem HeatMap-Tooltip ([#128812](https://github.com/grafana/grafana/pull/128812)).
- **Alerting:** Notification History steht laut What's-new-Katalog auch in Open Source zur Verfuegung → [What's new](https://grafana.com/whats-new/2026-08-24-alerting-notification-history/)

## Nur Enterprise/Cloud (irrelevant fuer Open Source)
- Git Sync Support fuer GitHub Enterprise inkl. Webhooks und Dashboard Previews — irrelevant, da nur Enterprise → [What's new](https://grafana.com/whats-new/2026-08-18-git-sync-support-for-github-enterprise/)
- Provisioning: OAuth-App-Verbindungen fuer GitLab und Bitbucket sowie GitLab-Webhook-Implementierung (Enterprise-Anteile) — irrelevant, da nur Enterprise.
- Analytics: Public-Dashboard-UID in Loki-Usage-Insights-Events — irrelevant, da nur Enterprise.
- Auditing: Benutzername in Audit-Logs bei Benutzerloeschung — irrelevant, da nur Enterprise.
- Reporting: Template-Variablen ohne Typ-Allowlist sowie gebuendelte Dashboard-Lookups beim Auflisten von Reports — irrelevant, da nur Enterprise.
- Secrets: RBAC-Fix fuer die AWS-Keeper-Erstellungsroute — irrelevant, da nur Enterprise.
- Alert enrichment — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-08-24-alert-enrichment/)
- Adaptive Metrics Recommendations Configuration — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-08-18-further-optimize-metrics-costs-with-adaptive-metrics-recommendations-configuration/)
- K6 Studio 2.0 (Browser Test Authoring, Autocorrelation) — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-08-19-k6-studio-20--browser-test-authoring-and-autocorrelation-are-generally-available/)
