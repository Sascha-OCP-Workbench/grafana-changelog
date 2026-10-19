# Grafana v13.2.4 — Tabellen-Variante

_Veroeffentlicht: 2026-10-13_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.4)

**Spalten:**
1. **Version**
2. **Kategorie (Upstream)** — Einordnung aus dem GitHub-Release-Changelog: `Breaking change` · `Feature/Enhancement` · `Bug fix` · `Security` · `Plugin development`
3. **Aenderungstitel** — vereinheitlichter englischer Titel der Aenderung (nah an den Original-PR-Ueberschriften, bei Sammelpunkten KI-formuliert; < 20 Woerter)
4. **Beschreibung (aus den PRs) / What's new** — kurze englische Zusammenfassung aus den verlinkten Pull-Requests (What/Why), dazu What's-new-Deep-Links und Upstream-PR-Links
5. **Platform** — Sicht des Plattform-Betreibers/Hosters der Grafana-Instanz (inkl. Nutzung der Instanz fuers OpenShift-Plattform-Monitoring); bewusst leer, vom Kunden zu bewerten
6. **User** — Sicht eines Projekt-Team-Nutzers der Grafana-Instanz (ohne administrativen Grafana-Zugriff); bewusst leer, vom Kunden zu bewerten
7. **Deine deutsche Bewertung** — Icon(s) + ggf. kurze Zusatzeinschaetzung

**Legende (Spalte 7):** 🚧 harter Breaking Change (von Grafana offiziell gekennzeichnet) · ℹ️ Hilfreiche neue Funktion · 🔷 Hilfreiche Information · 🔧 neuer Default (Verhalten ab jetzt standardmaessig aktiv/geaendert) · ⚠️ Doku-Anpassung noetig / potenziell breaking (nicht offiziell als Breaking Change gekennzeichnet, kann aber Bestehendes brechen)

| Version | Kategorie (Upstream) | Aenderungstitel | Beschreibung (aus den PRs) / What's new | Platform | User | Deine deutsche Bewertung |
|---|---|---|---|---|---|---|
| 13.2.4 | Feature/Enhancement | **Provisioning:** Allow resource previews in unsynced folders | Routes non-folder reads on a non-configured ref to a preview authorization path, so Git Sync can preview new, existing, and moved folder-scoped resources before their destination folders are synced. — PR: [#134391](https://github.com/grafana/grafana/pull/134391) | | | ℹ️ Vorschauen provisionierter Ressourcen funktionieren jetzt auch in Ordnern, die noch nicht synchronisiert sind. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Show last checked time in Pull status | Adds a "Last checked" row to the Pull status tile showing when Git Sync last checked the repository, hidden when the timestamp is missing or zero for backend compatibility. — PR: [#134483](https://github.com/grafana/grafana/pull/134483) | | | ℹ️ Der Pull-Status zeigt zusaetzlich den Zeitpunkt der letzten Pruefung an. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Support legacy paths and diagnose missing source annotations | Resolves repository resource paths via the shared metadata accessor, preferring grafana.app/sourcePath with fallback to legacy grafana.app/repoPath for delete and move jobs, and logs resource identity plus known annotation keys when unresolvable. — PR: [#133779](https://github.com/grafana/grafana/pull/133779) | | | ℹ️ Alte Pfade werden weiterhin unterstuetzt und fehlende Source-Annotationen werden diagnostiziert. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Write terminal sync status back to repository and respect Git Sync polling intervals after unchanged refs | Writes terminal sync status back to the repository when sync jobs fail early, and respects Git Sync polling intervals after unchanged refs. — PR: [#134478](https://github.com/grafana/grafana/pull/134478) | | | ℹ️ Endgueltige Sync-Zustaende werden auch bei fruehen Job-Fehlern ins Repository zurueckgeschrieben, und unveraenderte Refs respektieren die konfigurierten Polling-Intervalle. |
| 13.2.4 | Feature/Enhancement | **Git Sync:** Clarify repository links for pure Git | Clarifies repository links for pure Git repositories. — PR: [#134253](https://github.com/grafana/grafana/pull/134253) | | | ℹ️ ⚠️ Repository-Links werden fuer reine Git-Repositories eindeutiger dargestellt; ggf. Doku/Screenshots anpassen. |
| 13.2.4 | Security | **Security:** Fix CVE-2026-15577, CVE-2026-33374, CVE-2026-93294 und CVE-2026-95502 | Vier Sicherheitsluecken wurden behoben; Update empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Vier Sicherheitsluecken wurden behoben; Update empfohlen (keine PR-Referenzen im Release-Body). |
| 13.2.4 | Feature/Enhancement | **Alerting:** Strip sensitive headers from oauth2 cross-host redirects | Strips sensitive headers from OAuth2 redirects that cross hosts. — PR: [#134433](https://github.com/grafana/grafana/pull/134433) | | | 🔷 ⚠️ Sensible Header werden bei OAuth2-Redirects auf andere Hosts entfernt, was bestehende Integrationen mit Header-Weitergabe beeinflussen kann. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Reject invalid resource names before API calls | Validates resource names during parsing using IsValidGrafanaName() before resolving a client or calling the resource API, returning a metadata.name field error so sync jobs warn and the files API returns HTTP 400 instead of 500. — PR: [#133776](https://github.com/grafana/grafana/pull/133776) | | | 🔷 ⚠️ Ungueltige Ressourcennamen werden bereits vor dem API-Aufruf abgelehnt, wodurch bisher akzeptierte Namen nun zu Fehlern fuehren koennen. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Skip previews for pull requests from forks | Skips previews for pull requests originating from forks and posts a structured comment plus job status explaining that fork previews are unsupported; the job completes successfully. — PR: [#133799](https://github.com/grafana/grafana/pull/133799) | | | 🔷 Fuer Pull Requests aus Forks werden keine Vorschauen mehr erzeugt. |
| 13.2.4 | Feature/Enhancement | **Provisioning:** Stop PR previews when refs disappear | Stops pull request previews when the referenced Git refs no longer exist. — PR: [#133855](https://github.com/grafana/grafana/pull/133855) | | | 🔷 Vorschauen werden beendet, sobald der zugehoerige Ref nicht mehr existiert. |
| 13.2.4 | Feature/Enhancement | **Dashboard:** Fall back when collection deletion is unsupported | Falls back to an alternative path when collection deletion is not supported. — PR: [#134224](https://github.com/grafana/grafana/pull/134224) | | | 🔷 Beim Loeschen nicht unterstuetzter Collections greift nun ein Fallback statt eines Fehlers. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **IAM: Fix SCIM (CVE-2026-92539)** — Sicherheitsfix im SCIM-Bereich — irrelevant, da nur Enterprise (keine PR-Referenz im Release-Body).
- **IRM: Investigate alerts and incidents with Grafana Assistant** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-15-investigate-alerts-and-incidents-with-grafana-assistant-in-irm/)
- **Service Center: Discover and organize your services** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-discover-and-organize-your-services-in-service-center/)
- **IRM: Send alerts to the device you choose** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-send-grafana-irm-alerts-to-the-device-you-choose/)
- **Metrics: Choose connection KPIs to control metrics cost** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-choose-connection-kpis-to-control-metrics-cost/)
- **Frontend Observability: Session replay is now available for everyone** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-session-replay-is-now-available-for-everyone/)
- **IRM: Fill in incident custom fields without leaving Slack** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-fill-in-incident-custom-fields-without-leaving-slack/)
- **IRM: Filter and sort alert groups by date** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-13-filter-and-sort-alert-groups-by-date-in-grafana-irm/)
- **Alerting: Improve alert rule quality** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-improve-alert-rule-quality/)
- **IRM: Silences now last as long as you set them** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-silences-in-grafana-irm-now-last-as-long-as-you-set-them/)
- **IRM: New escalation options** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-new-escalation-options-in-grafana-irm/)
- **Reporting: Custom headers and footers for report PDFs** — irrelevant, da nur Enterprise → [What's new](https://grafana.com/whats-new/2026-10-09-custom-headers-and-footers-for-report-pdfs/)
---
