# How this profile is put together

Everything that moves in the README is a hand-authored SVG animated with SMIL inside the file
itself. That is a constraint, not a preference: GitHub strips `<script>`, `<style>` blocks and
inline `style=` from a README, and an SVG loaded through `<img>` is also blocked from fetching
anything external — no Google Fonts, no stylesheets. So each panel carries its own typography.
`assets/fonts/` holds four cuts subset down to the characters actually used (Archivo instanced
at Expanded Black and at text weight, Martian Mono, Instrument Serif italic), and `build.py` inlines them as
base64 `@font-face` blocks. Only the faces a source really uses get embedded, which is why the
built files land around 55–60 KB rather than 200.

The sources are in [`assets/src/`](../assets/src) — `hero.svg`, one `chN-*.svg` per project channel,
and `signoff.svg` —
and each contains two tokens: `__FONTS__` where the font faces go and `__VARS__` where that
theme's CSS custom properties go. Running `python3 build.py` writes a `-dark` and a `-light`
variant of each, and the README's `<picture>` elements pick between them with
`prefers-color-scheme`. **Edit the file in `assets/src/`, never the built output.** To retune the
whole palette, change the `DARK` / `LIGHT` dicts at the top of `build.py` and rebuild; every
panel follows. One rule worth keeping: a `<picture>` must never be wrapped in a link — GitHub's
themed-picture wrapper ejects the `<img>` out of the anchor and breaks both the link and the
theme swap. Put the link on a line of its own underneath.

To check your work, run `python3 -m http.server` at the repo root and open
`preview.html?n=hero` (or `ch1-threebody` … `ch6-deadwax`, `signoff`), which renders each panel in both themes at
GitHub's ~850 px content column and at phone width. `python3 render-readme.py` pushes README.md
through GitHub's own markdown API and writes `readme-render.html` so you can see the real page
before pushing.

`docs/` is the GitHub Pages site (Settings → Pages → `main` / `/docs`): a single dependency-free
`index.html` using the same palette and type, loaded from Google Fonts since a real page is
allowed to. It is built as a broadcast: the name decodes and tears on hover, the oscilloscope
reacts to the pointer, and the channel set switches with a static burst on click, the number
keys, the arrow keys or a swipe. Each channel is an `<article>` plus a small block in the script that draws
its readout; adding a project means one more of each, one more dial button, and a slot in the hero's
program guide (three across, two rows). Channel order is deliberate: security work first,
retrieval next, product craft last. Renumbering means the `CH.0N` badge, the ghost numeral and
the aria-label in the source, the file name, and the README block.
