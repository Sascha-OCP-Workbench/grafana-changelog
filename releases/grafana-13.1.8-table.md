# Grafana v13.1.8 — Tabellen-Variante

_Veroeffentlicht: 2026-10-13_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.8)

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
| 13.1.8 | Feature/Enhancement | **Dashboard:** Fall back when collection deletion is unsupported | **Dashboard:** Fall back when collection deletion is unsupported — PR: [#134225](https://github.com/grafana/grafana/pull/134225) | | | ℹ️ Das Loeschen von Collections faellt auf ein alternatives Verfahren zurueck, wenn der Backend-Storage die Operation nicht unterstuetzt. |
| 13.1.8 | Feature/Enhancement | **Alerting:** Strip sensitive headers from oauth2 cross-host redirects | **Alerting:** Strip sensitive headers from oauth2 cross-host redirects — PR: [#134428](https://github.com/grafana/grafana/pull/134428) | | | 🔷 ⚠️ Bei OAuth2-Redirects auf andere Hosts werden sensible Header entfernt; Integrationen, die auf deren Weitergabe angewiesen sind, koennen betroffen sein. |
| 13.1.8 | Security | **Security:** Fix CVE-2026-15577, CVE-2026-33374, CVE-2026-93294 and CVE-2026-95502 | Vier Sicherheitsluecken wurden behoben; Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Vier Sicherheitsluecken wurden behoben; Update wird empfohlen (keine PR-Referenzen im Release-Body). |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **IAM: Fix SCIM (CVE-2026-92539)** — Sicherheitsfix in der SCIM-Implementierung — irrelevant, da nur Enterprise (keine PR-Referenz im Release-Body).
- **IRM: Investigate alerts and incidents with Grafana Assistant** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-15-investigate-alerts-and-incidents-with-grafana-assistant-in-irm/)
- **Service Center: Discover and organize your services** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-discover-and-organize-your-services-in-service-center/)
- **IRM: Send Grafana IRM alerts to the device you choose** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-send-grafana-irm-alerts-to-the-device-you-choose/)
- **Metrics: Choose connection KPIs to control metrics cost** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-choose-connection-kpis-to-control-metrics-cost/)
- **Frontend Observability: Session replay is now available for everyone** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-session-replay-is-now-available-for-everyone/)
- **IRM: Fill in incident custom fields without leaving Slack** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-14-fill-in-incident-custom-fields-without-leaving-slack/)
- **IRM: Filter and sort alert groups by date** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-13-filter-and-sort-alert-groups-by-date-in-grafana-irm/)
- **Alerting: Improve alert rule quality** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-improve-alert-rule-quality/)
- **IRM: Silences now last as long as you set them** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-silences-in-grafana-irm-now-last-as-long-as-you-set-them/)
- **IRM: New escalation options** — irrelevant, da nur Cloud → [What's new](https://grafana.com/whats-new/2026-10-12-new-escalation-options-in-grafana-irm/)
---
