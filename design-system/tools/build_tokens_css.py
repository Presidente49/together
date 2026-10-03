"""Compile tokens.json into tokens.css for local use of the design system.

The published Design System artifact generates its own tokens.css; this script
produces the same custom properties so the previews and bundle.css work from
this repository too. Run from anywhere: python3 design-system/tools/build_tokens_css.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tokens = json.loads((ROOT / "tokens.json").read_text())


def color_value(value):
    alias = re.fullmatch(r"\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}", value)
    return f"var(--{alias.group(1)})" if alias else value


themes = [t["id"] for t in tokens["color"]["themes"]]
first = themes[0]


def theme_value(token, theme):
    value = token["value"]
    if isinstance(value, dict):
        return value.get(theme, value.get(first))
    return value


lines = ["/* Generated from tokens.json by tools/build_tokens_css.py. Do not edit by hand. */", ""]

for font in tokens["type"]["fonts"]:
    lines += [
        "@font-face {",
        f'  font-family: "{font["family"]}";',
        f'  src: url("{font["file"]}") format("woff2");',
        f'  font-weight: {font["weight"]};',
        f'  font-style: {font.get("style", "normal")};',
        "  font-display: swap;",
        "}",
    ]
lines.append("")

for i, theme in enumerate(themes):
    selector = f':root, [data-theme="{theme}"]' if i == 0 else f'[data-theme="{theme}"]'
    lines.append(selector + " {")
    for token in tokens["color"]["tokens"]:
        lines.append(f'  --{token["name"]}: {color_value(theme_value(token, theme))};')
    for token in tokens.get("shadow", {}).get("tokens", []):
        lines.append(f'  --{token["name"]}: {theme_value(token, theme)};')
    lines.append("}")
lines.append("")

lines.append(":root {")
for family, stack in tokens["type"]["families"].items():
    lines.append(f"  --font-{family}: {stack};")
for key, group in tokens.items():
    if key in ("name", "version", "meta", "color", "type", "shadow") or not isinstance(group, dict):
        continue
    for token in group.get("tokens", []):
        lines.append(f'  --{token["name"]}: {token["value"]};')
lines.append("}")
lines.append("")

for group in tokens["type"]["groups"]:
    for style in group["styles"]:
        family = style.get("family", group["family"])
        lines.append(f'.{style["name"]} {{')
        lines.append(f"  font-family: var(--font-{family});")
        lines.append(f'  font-size: {style["fontSize"]};')
        lines.append(f'  line-height: {style["lineHeight"]};')
        lines.append(f'  font-weight: {style["fontWeight"]};')
        if "letterSpacing" in style:
            lines.append(f'  letter-spacing: {style["letterSpacing"]};')
        lines.append("}")

(ROOT / "tokens.css").write_text("\n".join(lines) + "\n")
print(f"wrote {ROOT / 'tokens.css'}")
