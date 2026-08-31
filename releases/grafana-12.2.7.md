# Grafana v12.2.7

_Veroeffentlicht: 2026-03-09_ · [Release auf GitHub](https://github.com/grafana/grafana/releases/tag/v12.2.7)

## Breaking Changes
- Keine.

## Hilfreiche neue Funktionen
- **Rendering:** Der Image Renderer unterstuetzt nun eigene CA-Zertifikate, was den Betrieb hinter interner PKI bzw. TLS-Interception erleichtert ([#118911](https://github.com/grafana/grafana/pull/118911)).

## Hilfreiche Informationen
- **Go:** Die Build-Toolchain wurde auf Go 1.25.8 aktualisiert ([#119696](https://github.com/grafana/grafana/pull/119696)).
- **Dashboards:** Der `start`-Parameter der List-Versions-API funktioniert im K8s-Backend wieder korrekt ([#119398](https://github.com/grafana/grafana/pull/119398)).
- Reines Patch-Release ohne dokumentierte What's-new-Highlights.
