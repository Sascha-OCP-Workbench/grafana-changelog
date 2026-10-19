# Grafana v12.4.13 — Tabellen-Variante

_Veroeffentlicht: 2026-10-13_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.13)

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
| 12.4.13 | Feature/Enhancement | **Dashboard:** Fall back when collection deletion is unsupported | **Dashboard:** Fall back when collection deletion is unsupported (#128259) — PR: [#134229](https://github.com/grafana/grafana/pull/134229) | | | ℹ️ Dashboards greifen auf ein Fallback zurueck, wenn das Loeschen von Collections nicht unterstuetzt wird. |
| 12.4.13 | Security | **Security:** Fix CVE-2026-15577, CVE-2026-33374 and CVE-2026-93294 | Dieses Patch-Release behebt drei Sicherheitsluecken; ein Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Dieses Patch-Release behebt drei Sicherheitsluecken; ein Update wird empfohlen (keine PR-Referenzen im Release-Body). |
| 12.4.13 | Feature/Enhancement | **Alerting:** Strip sensitive headers from oauth2 cross-host redirects | **Alerting:** Strip sensitive headers from oauth2 cross-host redirects — PR: [#134424](https://github.com/grafana/grafana/pull/134424) | | | 🔷 ⚠️ Bei OAuth2-Redirects auf andere Hosts werden sensible Header entfernt, was bestehende Integrationen mit Host-uebergreifenden Redirects beeinflussen kann. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **IAM: Fix CVE-2026-92539 in SCIM endpoints** — Sicherheitsfix fuer SCIM-Endpunkte — irrelevant, da nur Enterprise (keine PR-Referenz im Release-Body).
---
