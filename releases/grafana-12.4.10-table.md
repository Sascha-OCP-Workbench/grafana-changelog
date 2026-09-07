# Grafana v12.4.10 — Tabellen-Variante

_Veroeffentlicht: 2026-09-02_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.4.10)

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
| 12.4.10 | Security | **Security:** Fix CVE-2026-14199 and CVE-2026-19475 | Das Patch-Release behebt zwei Sicherheitsluecken; ein Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Das Patch-Release behebt zwei Sicherheitsluecken; ein Update wird empfohlen (keine PR-Referenzen im Release-Body). |
| 12.4.10 | Bug fix | **Dashboards:** Fix adhoc and groupby variable datasource on UI import | **Dashboards:** Fix adhoc and groupby variable datasource on UI import — PR: [#131821](https://github.com/grafana/grafana/pull/131821) | | | 🔷 Beim Import von Dashboards ueber die UI wird die Datasource fuer adhoc- und groupby-Variablen korrekt gesetzt. |
| 12.4.10 | Bug fix | **Dashboards:** Fix version dates and user display names in the legacy version history page | **Dashboards:** Fix version dates and user display names in the legacy version history page — PR: [#131808](https://github.com/grafana/grafana/pull/131808) | | | 🔷 In der alten Versionshistorie werden Datumsangaben und Benutzernamen wieder korrekt angezeigt. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
