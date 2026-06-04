# TLE snapshots

These `*.txt` files are daily snapshots of Celestrak orbital element groups,
written by `.github/workflows/update-tle.yml`. The app loads them **same-origin**
(`fetch('data/<group>.txt')`) so the full constellations are available without
hammering the live CORS API.

| File | Celestrak group | What it is |
| --- | --- | --- |
| `starlink.txt` | `starlink` | Full Starlink constellation (~7–8k objects) |
| `gps.txt` | `gps-ops` | Operational GPS / NAVSTAR |
| `galileo.txt` | `galileo` | EU Galileo (MEO) |
| `geo.txt` | `geo` | Geostationary belt |
| `stations.txt` | `stations` | ISS + other crewed/large stations |

Format is standard 3-line TLE (name line, line 1, line 2). The page parses them
with `parseTLE()` and propagates with SGP4 in a Web Worker.

**Seeding:** until the scheduled job first runs, these files are absent and the
app falls back to the live TLE API automatically. To populate immediately, run
the **Update TLE snapshots** workflow manually (Actions → Run workflow).
