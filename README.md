# together

## GatorBait Media design system

`design-system/` holds the GatorBait Media design system, extracted from
[Presidente49/gatorbait-media-redesign](https://github.com/Presidente49/gatorbait-media-redesign)
at `d696498`.

- `README.md` is the brand book: voice, color, type, layout, rules, imagery, motion.
- `tokens.json` holds the tokens (30 colors, 23 Barlow type styles, spacing, radius, borders, layout, breakpoints, ratios). `tokens.css` is generated from it with `python3 design-system/tools/build_tokens_css.py`.
- `components/bundle.css` holds the component classes (`gb-*`). Each `components/<Name>/` folder has usage guidelines and a static preview.
- `fonts/` has Barlow 400, 500, 700 and 800 (SIL OFL), and `assets/` has the wordmark and preview photography.

Previews load images from the published design system's asset store (`/_blob/…`), so the photos show only there. Locally, open a preview to check layout and type.
