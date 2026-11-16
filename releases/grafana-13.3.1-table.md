# Grafana v13.3.1 — Tabellen-Variante

_Veroeffentlicht: 2026-11-10_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v13.3.1)

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
| 13.3.1 | Feature/Enhancement | **Provisioning:** Allow same-host URL change on connection-backed repositories | Allows changing the URL of connection-backed provisioning repositories as long as the host stays the same. — PR: [#137083](https://github.com/grafana/grafana/pull/137083) | | | ℹ️ Bei Connection-basierten Repositories kann die URL nun innerhalb desselben Hosts geaendert werden. |
| 13.3.1 | Security | **Security:** Fix CVE-2026-102589, CVE-2026-107509, CVE-2026-110992, CVE-2026-111024, CVE-2026-13721 and CVE-2026-14242 | Patch-Release mit sechs behobenen Sicherheitsluecken; Update wird empfohlen. | | | 🔷 Patch-Release mit sechs behobenen Sicherheitsluecken; Update wird empfohlen. |
| 13.3.1 | Feature/Enhancement | **DateTime:** Update moment-timezone and easy-tz for 2026 time zone changes | Updates moment-timezone to 0.6.6 (tzdata 2026f) and the vendored easy-tz tables to tzdata 2026e, so times and zone labels are correct in Canadian zones that abolished DST in 2026. — PR: [#136951](https://github.com/grafana/grafana/pull/136951) | | | 🔷 ⚠️ Zeitzonendaten wurden auf die Aenderungen von 2026 aktualisiert, wodurch sich Zeitzonen-Offsets in Dashboards aendern koennen. |

## Nur Enterprise/Cloud (irrelevant fuer Open Source)

Diese Punkte sind nur in Enterprise/Cloud relevant und daher nicht in der Tabelle bewertet:

---
