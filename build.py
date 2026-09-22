#!/usr/bin/env python3
"""Render assets/src/*.svg into light + dark variants in assets/.

Each source carries two tokens:
  __FONTS__  where @font-face blocks go. GitHub renders README SVGs through
             <img>, which blocks external font files, so the four cuts in
             assets/fonts/ are inlined as base64. Only the faces a source
             actually uses (--disp / --body / --serif / --mono) get embedded.
  __VARS__   where that theme's CSS custom properties go.
"""
import base64, pathlib

FACES = {
    # css var -> (family name, file, weight, style)
    "disp":  ("APDisplay", "display.woff2",      "900", "normal"),
    "body":  ("APBody",    "body.woff2",         "500", "normal"),
    "serif": ("APSerif",   "serif-italic.woff2", "400", "italic"),
    "mono":  ("APMono",    "mono.woff2",         "500", "normal"),
}

STACKS = {
    "disp":  "'APDisplay',Georgia,serif",
    "body":  "'APBody',Helvetica,sans-serif",
    "serif": "'APSerif',Georgia,serif",
    "mono":  "'APMono',ui-monospace,Menlo,monospace",
}

DARK = {   # CRT: near-black, bone, one acid signal colour
    "paper": "#0A0A0B", "card": "#111113", "sunk": "#0D0D0F",
    "ink": "#EDEBE4", "dim": "#8E8B83", "faint": "#5A5852",
    "rule": "#232326", "rule2": "#36363C",
    "acid": "#D4FF3A", "atext": "#0A0A0B", "hot": "#FF4F2E", "violet": "#8B6CFF",
    "trace": "#D4FF3A", "grain": "0.06", "scan": "0.07",
}

LIGHT = {  # print: bone paper, black ink, the same acid used only as a fill
    "paper": "#EDEBE4", "card": "#F6F4EE", "sunk": "#E3E0D7",
    "ink": "#0A0A0B", "dim": "#55534D", "faint": "#8D897F",
    "rule": "#D6D2C7", "rule2": "#BDB8AA",
    "acid": "#D4FF3A", "atext": "#0A0A0B", "hot": "#E0391A", "violet": "#5B3DF5",
    "trace": "#E0391A", "grain": "0.045", "scan": "0",
}


def font_css(used):
    out = []
    for key in used:
        family, file, weight, style = FACES[key]
        data = base64.b64encode((pathlib.Path("assets/fonts") / file).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
                   f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return "".join(out)


def css_vars(theme, used):
    pairs = {k: STACKS[k] for k in used}
    pairs.update(theme)
    return ":root{" + "".join(f"--{k}:{v};" for k, v in pairs.items()) + "}"


def main():
    root = pathlib.Path(__file__).parent
    src, out = root / "assets" / "src", root / "assets"
    files = sorted(src.glob("*.svg"))
    assert files, "no sources in assets/src"
    for f in files:
        text = f.read_text()
        for token in ("__FONTS__", "__VARS__"):
            assert token in text, f"{f.name}: missing {token} marker"
        used = [k for k in FACES if f"var(--{k})" in text]
        assert used, f"{f.name}: uses none of the font vars"
        fonts = font_css(used)
        for name, theme in (("dark", DARK), ("light", LIGHT)):
            dest = out / f"{f.stem}-{name}.svg"
            dest.write_text(text.replace("__FONTS__", fonts)
                                .replace("__VARS__", css_vars(theme, used)))
            print(f"  {dest.relative_to(root)}  {dest.stat().st_size // 1024}k")


if __name__ == "__main__":
    main()
