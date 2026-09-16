#!/usr/bin/env python3
"""Render README.md through GitHub's markdown API into readme-render.html for local checking."""
import json, re, urllib.request, pathlib

root = pathlib.Path(__file__).parent
md = (root / "README.md").read_text()
req = urllib.request.Request(
    "https://api.github.com/markdown",
    data=json.dumps({"text": md, "mode": "markdown"}).encode(),
    headers={"Content-Type": "application/json", "Accept": "application/vnd.github+json",
             "User-Agent": "local-preview"})
html = urllib.request.urlopen(req).read().decode()
# The API wraps images in a lightbox anchor; repo README rendering keeps <img> a direct child of
# <picture>, which is what makes the dark/light swap work. Strip it so the preview matches.
html = re.sub(r'<a target="_blank" rel="noopener noreferrer" href="[^"]*">(<img[^>]*>)</a>', r"\1", html)

tpl = """<!doctype html><meta charset=utf-8><base href="/"><title>README render</title>
<style>
:root{--c:#0d1117;--f:#e6edf3;--b:#30363d;--l:#4493f8;--m:#8b949e}
body{margin:0;background:#010409;font:16px/1.6 -apple-system,'Segoe UI',Helvetica,Arial,sans-serif}
.pane{max-width:918px;margin:0 auto;padding:32px;background:var(--c);color:var(--f)}
.pane.light{--c:#fff;--f:#1f2328;--b:#d1d9e0;--l:#0969da;--m:#59636e}
img{max-width:100%;box-sizing:border-box}
h2{border-bottom:1px solid var(--b);padding-bottom:.3em;font-size:1.5em;margin-top:24px}
a{color:var(--l);text-decoration:none}
hr{border:0;border-top:1px solid var(--b);margin:24px 0}
blockquote{border-left:.25em solid var(--b);color:var(--m);padding:0 1em;margin:0 0 16px}
table{border-collapse:collapse;margin-bottom:16px}
th,td{border:1px solid var(--b);padding:6px 13px}
details{margin-bottom:16px}summary{cursor:pointer}
sub{color:var(--m)}
code{background:rgba(110,118,129,.4);padding:.2em .4em;border-radius:6px;font-size:85%}
.bar{max-width:918px;margin:0 auto;padding:6px 32px;background:#222;color:#fff;font:12px monospace;letter-spacing:2px}
</style>
<div class=bar>DARK</div><div class="pane">__HTML__</div>
<div class=bar>LIGHT</div><div class="pane light">__HTML__</div>
""".replace("__HTML__", html)
(root / "readme-render.html").write_text(tpl)
print("readme-render.html written")
