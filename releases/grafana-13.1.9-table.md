# Grafana v13.1.9 — Tabellen-Variante

_Veroeffentlicht: 2026-10-27_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.1.9)

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
| 13.1.9 | Feature/Enhancement | **Provisioning:** Default save from a branch preview to the previewed branch | Pre-fills the Branch field with the previewed branch when opening Save, Delete, or Move drawers from a branch preview, keeping the configured branch as a disabled read-only option when writes are not allowed. — PR: [#135175](https://github.com/grafana/grafana/pull/135175) | | | ℹ️ 🔧 Beim Speichern aus einer Branch-Preview wird nun standardmaessig der zuvor betrachtete Branch als Ziel vorausgewaehlt. |
| 13.1.9 | Security | **Security:** Fix CVE-2026-100105, CVE-2026-88858 and CVE-2026-88967 | Das Patch-Release behebt drei Sicherheitsluecken; ein Update wird empfohlen. | | | 🔷 Das Patch-Release behebt drei Sicherheitsluecken; ein Update wird empfohlen. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
