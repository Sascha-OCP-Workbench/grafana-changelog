# Grafana v13.2.1 — Tabellen-Variante

_Veroeffentlicht: 2026-09-02_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.1)

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
| 13.2.1 | Security | **Security:** Fix CVE-2026-12704 and CVE-2026-14199 | Zwei Sicherheitsluecken wurden behoben; ein Update wird empfohlen. | | | 🔷 Zwei Sicherheitsluecken wurden behoben; ein Update wird empfohlen. |
| 13.2.1 | Bug fix | **Dashboards:** Fix adhoc and groupby variable datasource on UI import | **Dashboards:** Fix adhoc and groupby variable datasource on UI import — PR: [#131819](https://github.com/grafana/grafana/pull/131819) | | | 🔷 Beim Import ueber die UI wird die Datasource von adhoc- und groupby-Variablen wieder korrekt gesetzt. |
| 13.2.1 | Bug fix | **Packaging:** Fix issue with bundled plugins not being moved properly | **Packaging:** Fix issue with bundled plugins not being moved properly — PR: [#131037](https://github.com/grafana/grafana/pull/131037) | | | 🔷 Mitgelieferte Plugins werden beim Packaging wieder korrekt verschoben. |
| 13.2.1 | Bug fix | **PanelEditor:** Fix options pane not resizable beyond the preview's content width | **PanelEditor:** Fix options pane not resizable beyond the preview's content width — PR: [#131608](https://github.com/grafana/grafana/pull/131608) | | | 🔷 Der Optionsbereich im Panel-Editor laesst sich wieder ueber die Breite des Preview-Inhalts hinaus vergroessern. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
