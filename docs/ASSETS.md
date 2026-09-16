# How this profile is put together

The only moving thing on the README is `assets/src/hero.svg`, a hand-authored SVG animated with
SMIL inside the file. That is the constraint, not a preference: GitHub strips `<script>`,
`<style>` blocks and inline `style=` from a README, but an SVG loaded through `<img>` keeps its
own stylesheet and timeline. The source carries a `__VARS__` token where its colours go;
`python3 build.py` writes `assets/hero-dark.svg` and `assets/hero-light.svg`, and the README's
`<picture>` picks one by `prefers-color-scheme`. Edit the source, never the built files; to
re-colour everything, change the `DARK` / `LIGHT` dicts at the top of `build.py` and rebuild.
`python3 -m http.server` then `preview.html?n=hero` shows both themes at desktop and phone width.

`docs/` is the GitHub Pages site (Settings → Pages → `main` / `/docs`): one dependency-free
`index.html` — the same statement, a Now / Before / Next row, links, and a canvas background
of slow signals. Copy lives in the HTML; there is nothing to build.
