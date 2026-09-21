# Grafana v13.1.6 — Tabellen-Variante

_Veroeffentlicht: 2026-09-15_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.6)

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
| 13.1.6 | Security | **Security:** Fix CVE-2026-15815, CVE-2026-76154 and CVE-2026-79656 | Das Patch-Release behebt drei Sicherheitsluecken; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). | | | 🔷 Das Patch-Release behebt drei Sicherheitsluecken; ein zeitnahes Update wird empfohlen (keine PR-Referenzen im Release-Body). |
| 13.1.6 | Bug fix | **Dashboards:** Preserve query variable refresh setting on v2 dashboard import | Preserves a query variable's original refresh setting when importing v2 dashboards instead of hardcoding onDashboardLoad during datasource remapping; 'never' is still upgraded since options are cleared on that path. — PR: [#132090](https://github.com/grafana/grafana/pull/132090) | | | 🔷 Beim Import von v2-Dashboards bleibt die Refresh-Einstellung von Query-Variablen jetzt erhalten. |
| 13.1.6 | Bug fix | **Provisioning:** Fix folder rename UID collision during full sync | Fixes a UID collision that occurred when renaming folders during a full provisioning sync. — PR: [#132164](https://github.com/grafana/grafana/pull/132164) | | | 🔷 UID-Kollisionen beim Umbenennen von Ordnern waehrend eines Full Sync treten nicht mehr auf. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
