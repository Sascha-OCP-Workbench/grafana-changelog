# Grafana v13.0.13 — Tabellen-Variante

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.0.13)

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
| 13.0.13 | Feature/Enhancement | **Provisioning:** Allow same-host URL change on connection-backed repositories | Allows changing a connection-backed repository URL in provisioning when the new URL points to the same host. — PR: [#137092](https://github.com/grafana/grafana/pull/137092) | | | ℹ️ Bei connection-backed Repositories kann die URL nun innerhalb desselben Hosts geaendert werden. |
| 13.0.13 | Security | **Security:** Fix CVE-2026-102589, CVE-2026-107365, CVE-2026-107509, CVE-2026-110992, CVE-2026-111024, CVE-2026-13721, CVE-2026-14242, CVE-2026-82014 | Acht Sicherheitsluecken wurden behoben; ein Update wird empfohlen. | | | 🔷 Acht Sicherheitsluecken wurden behoben; ein Update wird empfohlen. |
| 13.0.13 | Feature/Enhancement | **DateTime:** Bump moment-timezone to 0.6.6 for 2026 time zone changes | Updates moment-timezone from 0.5.47 to 0.6.6 (tzdata 2025a to 2026f) in the root, @grafana/data and @grafana/prometheus manifests so times in British Columbia, Alberta, Northwest Territories, Manitoba and Cuba are correct from November 2026. — PR: [#136948](https://github.com/grafana/grafana/pull/136948) | | | 🔷 ⚠️ Aktualisierte Zeitzonendaten fuer 2026 koennen Zeitzonen-Offsets in Dashboards und Abfragen veraendern. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
