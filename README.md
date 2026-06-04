# Earth → Orbit

An interactive 3D globe you can pull away from — watching Earth shrink among the stars as you climb from the surface, past the Kármán line, through the satellite shells, out to the Moon. Satellites are **live**, propagated in real time from real orbital tracking data. Built with [Three.js](https://threejs.org/) and [satellite.js](https://github.com/shashwatak/satellite-js), runs entirely in the browser, no build step.

🌍 **Live:** https://siglerventures.github.io/orbit/

## Features

- **Photoreal Earth** — NASA Blue Marble day texture, city lights blended onto the night side, ocean specular highlights, surface relief via normal map, and a separate drifting cloud layer. The globe rotates at true sidereal time.
- **Live satellites** — real positions propagated in real time with SGP4:
  - **ISS** — tracked exactly by catalog number, with its real orbit trail drawn.
  - **Starlink** — a live ~600-satellite sample of the ~12,000-strong constellation.
  - **GPS** — the live operational constellation (~19–31 satellites).
  - **GEO** — shown as a representative ring (geostationary satellites are effectively fixed relative to Earth).
- **Atmosphere glow** — a fresnel shader renders the blue limb you see from space.
- **Starfield** — 7,000 procedurally placed stars with realistic color and brightness variation, plus a tilted Milky Way band.
- **Fly-to presets** — jump between Surface, ISS, Starlink, GPS, GEO, and the Moon.
- **Time control** — Live / 60× / 600× to speed up orbital motion.
- **Live HUD** — current camera altitude (mi), region you're in, satellites tracked, and sim time (UTC).
- **Click for detail** — tap any satellite or the Moon for a quick fact card.
- **Graceful fallback** — if the orbital-data API is unreachable, the globe automatically shows representative orbit shells instead of breaking.

## Controls

| Action | Input |
| --- | --- |
| Rotate | Drag |
| Zoom | Scroll / pinch |
| Inspect | Click a satellite or the Moon |
| Jump to altitude | Buttons, top right |
| Time speed | Buttons in the HUD, bottom left |

## Run locally

It's a single static file. Serve it (recommended, so the CDN and API requests resolve cleanly):

```bash
python -m http.server 8000
# then open http://localhost:8000
```

## Deploy on GitHub Pages

1. Push `index.html` to the repo's default branch.
2. Go to **Settings → Pages**.
3. Under **Source**, select your branch (`main`) and the `/ (root)` folder.
4. Save. The site goes live at `https://<username>.github.io/<repo>/` within a minute or so.

## Tech notes

- **Three.js r160** and **satellite.js 5.0.0**, loaded as ES modules via import map from jsDelivr / esm.sh — no bundler, no `node_modules`.
- **Textures** are served from the Three.js examples set on jsDelivr with permissive CORS headers, so they load correctly when hosted on GitHub Pages.
- **Orbital data** is fetched at runtime from the [TLE API](https://tle.ivanstanojevic.me/) (Celestrak-derived, CORS-enabled). TLEs are parsed and propagated client-side with SGP4 — satellites keep moving correctly between data refreshes.
- Earth is rotated by Greenwich Mean Sidereal Time so satellites sit in their correct inertial orbits; positions are computed in Earth-centered inertial (ECI) coordinates and scaled with Earth's radius = 1 scene unit.
- Earth day/night blending uses a small `onBeforeCompile` shader injection that mixes the city-lights texture in based on sun angle.
- Altitudes reference Earth's mean radius (3,959 mi / 6,371 km). At true scale the Moon sits ~60 Earth-radii out — roughly 960× the ISS — which is why fly-to presets are used to reach the far shells.

## Roadmap

- ✅ **Live satellite positions** — ISS, GPS, and Starlink from real TLE data (done).
- **Exaggerated / logarithmic altitude mode** — a toggle to lift the LEO shells off the surface so LEO, MEO, and GEO are individually navigable instead of clustering near Earth.
- **Real star catalog** — swap the procedural field for the HYG database so constellations are accurate.
- **Full Starlink constellation** — option to load all ~12,000 satellites (with instanced rendering for performance).
- **Ground tracks** — project satellite paths onto the Earth's surface.

## Credits

Earth and Moon imagery from the Three.js examples texture set (NASA-derived Blue Marble and lunar maps). Orbital elements via the ivanstanojevic TLE API (Celestrak data). Propagation by satellite.js. Rendering by Three.js.
