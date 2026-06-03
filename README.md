# Earth → Orbit

An interactive 3D globe you can pull away from — watching Earth shrink among the stars as you climb from the surface, past the Kármán line, through the satellite shells, out to the Moon. Built with [Three.js](https://threejs.org/), runs entirely in the browser, no build step.

## Features

- **Photoreal Earth** — NASA Blue Marble day texture, city lights blended onto the night side, ocean specular highlights, surface relief via normal map, and a separate drifting cloud layer.
- **Atmosphere glow** — a fresnel shader renders the blue limb you see from space.
- **Starfield** — 7,000 procedurally placed stars with realistic color and brightness variation, plus a tilted Milky Way band.
- **Satellites at true altitude** — ISS, the Starlink shell, the GPS constellation, and geostationary satellites are positioned at their real relative altitudes (Earth radius = 1 unit). The gaps between them are accurate.
- **Fly-to presets** — jump between Surface, ISS, Starlink, GPS, GEO, and the Moon.
- **Live HUD** — current camera altitude (mi / km) and the atmospheric region you're in, updating as you zoom.
- **Click for detail** — tap any satellite or the Moon for a quick fact card.

## Controls

| Action | Input |
| --- | --- |
| Rotate | Drag |
| Zoom | Scroll / pinch |
| Inspect | Click a satellite or the Moon |
| Jump to altitude | Buttons, top right |

## Run locally

It's a single static file. Open `index.html` in a browser, or serve it:

```bash
python -m http.server 8000
# then open http://localhost:8000
```

A local server is recommended over opening the file directly, so the CDN texture requests resolve cleanly.

## Deploy on GitHub Pages

1. Push `index.html` to the repo's default branch.
2. Go to **Settings → Pages**.
3. Under **Source**, select your branch (`main`) and the `/ (root)` folder.
4. Save. The site goes live at `https://<username>.github.io/<repo>/` within a minute or so.

## Tech notes

- **Three.js r160**, loaded as an ES module via import map from jsDelivr — no bundler, no `node_modules`.
- **Textures** are served from the Three.js examples set on jsDelivr with permissive CORS headers, so they load correctly when hosted on GitHub Pages.
- Earth day/night blending is done with a small `onBeforeCompile` shader injection that mixes the city-lights texture in based on the sun angle.
- Altitudes use Earth's mean radius of 3,959 mi as the reference. At true scale the Moon sits ~60 Earth-radii out — roughly 960× the ISS — which is why the fly-to presets, rather than a linear zoom, are used to reach the far shells.

## Roadmap (v2)

- **Live satellite positions** — replace the representative shells with real orbits propagated from [Celestrak](https://celestrak.org/) TLE data using [satellite.js](https://github.com/shashwatak/satellite-js). The actual Starlink constellation is ~8,000 objects.
- **Logarithmic zoom mode** — spread the near-Earth shells apart so LEO, MEO, and GEO are individually navigable instead of clustering near the surface.
- **Real star catalog** — swap the procedural field for the HYG database so constellations are accurate.
- **Time controls** — scrub forward/back to watch orbits propagate.

## Credits

Earth and Moon imagery from the Three.js examples texture set (NASA-derived Blue Marble and lunar maps). Rendering by Three.js.
