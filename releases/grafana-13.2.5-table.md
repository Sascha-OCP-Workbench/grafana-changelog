# Grafana v13.2.5 — Tabellen-Variante

_Veroeffentlicht: 2026-10-27_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.2.5)

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
| 13.2.5 | Feature/Enhancement | **Git Sync:** Ignore hidden paths in repository scans and diffs | Git Sync now skips dot-prefixed files and directories (for example .ci/ and .github/workflows/) in repository tree listings and diffs at any depth, across Git, GitHub, staged Git, and local readers and all sync targets. — PR: [#135028](https://github.com/grafana/grafana/pull/135028) | | | ℹ️ ⚠️ Versteckte Pfade (z.B. `.github/`) werden bei Repository-Scans und Diffs nicht mehr beruecksichtigt, was bisher synchronisierte Inhalte ausschliessen kann. |
| 13.2.5 | Feature/Enhancement | **Provisioning:** Default save from a branch preview to the previewed branch | The Save, Delete, and Move drawers opened from a branch preview now pre-fill the Branch field with the previewed branch instead of the repository's configured branch. — PR: [#135174](https://github.com/grafana/grafana/pull/135174) | | | ℹ️ 🔧 ⚠️ Beim Speichern aus einer Branch-Preview ist nun standardmaessig der jeweils betrachtete Branch vorausgewaehlt. |
| 13.2.5 | Feature/Enhancement | **Provisioning:** Never replace the repository root folder during incremental sync | Incremental sync now ignores a root-level folder.json and never schedules the repository root folder for replacement or deletion, which previously always failed. — PR: [#135463](https://github.com/grafana/grafana/pull/135463) | | | ℹ️ Der Root-Ordner eines Repositories wird beim inkrementellen Sync nicht mehr ersetzt. |
| 13.2.5 | Security | **Security:** Fix CVE-2026-100105, CVE-2026-103506, CVE-2026-88858 and CVE-2026-88967 | No description available. | | | 🔷 Vier Sicherheitsluecken wurden behoben; Update empfohlen. |
| 13.2.5 | Bug fix | **Plugins:** Don't report loaded plugins as not registered when a request times out | Plugins are no longer reported as not registered when a request times out. — PR: [#135665](https://github.com/grafana/grafana/pull/135665) | | | 🔷 Geladene Plugins werden bei Request-Timeouts nicht mehr faelschlich als nicht registriert gemeldet. |
| 13.2.5 | Bug fix | **Provisioning:** Fix PR dashboard previews when served from a sub-path | Fixes Git Sync pull request dashboard previews rendering the wrong page when Grafana runs under a sub-path, by correctly stripping the sub-path from the screenshot URL path. — PR: [#135559](https://github.com/grafana/grafana/pull/135559) | | | 🔷 Dashboard-Previews aus Pull Requests funktionieren jetzt auch bei Betrieb unter einem Sub-Path. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

- **Real user context in browser checks** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-10-28-real-user-context-in-browser-checks--see-if-a-failing-browser-check-is-hitting-real-users/)
- **Announcement banners can now be dismissible** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-10-27-announcement-banners-can-now-be-dismissible/)
- **Get check suggestions in synthetic monitoring (experimental)** — irrelevant, da nur Enterprise/Cloud → [What's new](https://grafana.com/whats-new/2026-10-26-get-check-suggestions-in-synthetic-monitoring--experimental/)
---
