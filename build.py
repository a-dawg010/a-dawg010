#!/usr/bin/env python3
"""Render assets/src/*.svg into light + dark variants in assets/.

Each source SVG contains the literal token __VARS__ where its CSS custom
properties go. Everything else about the file is shared between themes, so a
visual change is made once, here or in the source, never twice.
"""
import pathlib

FONTS = {
    "mono": "ui-monospace,SFMono-Regular,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace",
}

DARK = {
    "bg": "#0B0E13", "bg2": "#111720", "bg3": "#161E29",
    "grid": "#1B2532", "stroke": "#26303D", "stroke2": "#33404F",
    "text": "#E6EDF3", "dim": "#93A1B1", "faint": "#61707F",
    "accent": "#2DD4BF", "accent2": "#7DD3FC",
    "warn": "#F59E0B", "vio": "#A78BFA", "glow": "0.10",
}

LIGHT = {
    "bg": "#FFFFFF", "bg2": "#F6F8FA", "bg3": "#EDF1F5",
    "grid": "#E3E9EF", "stroke": "#D3DBE3", "stroke2": "#B9C4CF",
    "text": "#0E1620", "dim": "#55606C", "faint": "#7D8996",
    "accent": "#0D9488", "accent2": "#0369A1",
    "warn": "#B45309", "vio": "#6D28D9", "glow": "0.07",
}


def css_vars(theme):
    pairs = {**FONTS, **theme}
    return ":root{" + "".join(f"--{k}:{v};" for k, v in pairs.items()) + "}"


def main():
    root = pathlib.Path(__file__).parent
    src, out = root / "assets" / "src", root / "assets"
    files = sorted(src.glob("*.svg"))
    assert files, "no sources in assets/src"
    for f in files:
        text = f.read_text()
        assert "__VARS__" in text, f"{f.name}: missing __VARS__ marker"
        for name, theme in (("dark", DARK), ("light", LIGHT)):
            dest = out / f"{f.stem}-{name}.svg"
            dest.write_text(text.replace("__VARS__", css_vars(theme)))
            print(f"  {dest.relative_to(root)}  {dest.stat().st_size // 1024}k")


if __name__ == "__main__":
    main()
