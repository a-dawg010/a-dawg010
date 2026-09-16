# How this profile is put together

Everything that moves on the profile page is a hand-authored SVG animated with SMIL
(`<animate>`, `<animateMotion>`) and CSS `@keyframes` declared inside the file itself. That
constraint is not aesthetic — GitHub strips `<script>`, `<style>` blocks and most inline
`style=` attributes from a README, but an SVG referenced through `<img src="…">` keeps its own
internal stylesheet and animation timeline. So the SVG has to be self-contained and committed to
this repo; third-party stat generators are slower, rate-limited, and make the page look templated.

The sources are in [`assets/src/`](../assets/src) — one file per panel: `hero.svg` (the agent
orchestration pipeline), `graph.svg` (the threat/asset/mitigation knowledge graph),
`stack.svg` (the layered capability rails) and `timeline.svg` (the career track). Each one
contains the literal token `__VARS__` where its CSS custom properties belong. Running
`python3 build.py` substitutes the dark and light palettes — both defined at the top of
`build.py`, nowhere else — and writes `assets/<name>-dark.svg` and `assets/<name>-light.svg`.
The README picks between them with `<picture>` + `prefers-color-scheme`. **Edit the file in
`assets/src/`, never the built output, then re-run `build.py` and commit both.** To retune the
whole profile's colour, change the `DARK` / `LIGHT` dicts in `build.py` and rebuild; every panel
follows.

To check your work, run `python3 -m http.server` at the repo root and open
`preview.html?n=hero` (or `stack`, `graph`, `timeline`). It renders each panel in both themes at
GitHub's ~850px content column and at phone width, which is where text overflow and illegible
labels show up. The viewBoxes are 880 units wide; anything smaller than about 10px inside them
stops being readable on a phone.

`docs/` is the GitHub Pages site — a single `index.html` with no dependencies: a canvas
force-directed map of the same system, with a query runner that lights the path through it.
Enable it under **Settings → Pages → Deploy from a branch → `main` / `/docs`**. The node data,
the edge list and the four query scripts are three arrays (`N`, `L`, `Q`) at the top of the
`<script>` block — adding a skill or a query means adding one row, not touching the renderer.
