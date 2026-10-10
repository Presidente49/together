# GatorBait Media design system

The system behind the live GatorBait Media front page: **Gator Day**, a white page with Gator blue, orange and white, set entirely in Barlow and Barlow Condensed. **Swamp Night** is the dark variant of the same tokens (`data-theme="night"`). Rebuilt Oct. 10, 2026 from the live front-page stylesheet, the Oct. 4 masthead fix and the Oct. 2026 type standard; it replaces the Sept. 28 "Paper" system.

## Look
- **White first.** The everyday page is `paper` white with `ink` text, `hub` tint behind modules and `gator-blue` as the one big colour field (masthead, game-day board). "That navy blue is too dark": navy is not part of the day look.
- **Orange is a rule and a signal.** Use `orange` for rules, the focus ring and the roundel ring; use `orange-ink` for any fill that carries white text and for small orange text.
- **Rules, not shadows.** Everything is square (`radius-0`); only inset rings (`shadow-ring`, `shadow-underline`) exist.
- **Swamp Night** (`data-theme="night"`) swaps the same names to a deep navy; it is the preview look (`?gbm_fp=night`) and the one-line rollback, not the default.

## Color
Every colour has a day and a night value; reference tokens by name, never by hex.
- Page and text: `paper` ground; `ink` for headlines and copy; `ink-2` for meta, captions and teasers; `link` for kickers, timestamps and links. `hub` and `card` sit behind modules; `chip` fills chips and photo placeholders; `rule` is hairlines only.
- Brand: `gator-blue` is fixed `#0021a5`. `mast` is the masthead band (blue by day, navy at night); `deep` is the stage ground (blue by day, near-black at night). White text only on `mast` and `deep`: `on-mast`, `on-deep`, `mast-sub`, `deep-ink`, `deep-body`, `deep-label`.
- Orange: `orange` (rules, focus, roundel ring, never text and never under white text, 3.5:1); `orange-ink` (fills and small text with `on-orange`, 4.8:1 by day); `tk-label` for ticker lead-ins; `live-red` only while a game is live.
- Contrast: every day pair is at least 4.5:1. **Flagged, kept exact from the live source:** at night `orange-ink` is the brand orange, so white text on night buttons, pills and ticker tags is 3.5:1, and `orange-ink` text on `card` is 4.3:1. Proposed fix: ink on orange (5.1:1) for night fills.

## Type
Two families, nothing else.
- **Barlow Condensed** (600/700/800) is display: the wordmark, headlines, kickers, nav, ticker, buttons, numerals and the drop cap. The lead headline is editorial normal case at 700; hub and stage titles are uppercase 800 with 0 tracking.
- **Barlow** (400–800) is text. Article body is weight **500**, 19px desktop / 17.5px phone; the lede (first paragraph) is 20px / 18.5px and carries the orange Condensed 800 drop cap (4.6em floated, 4.15em on phones); the dek is Condensed 700, 30px / 25px, with no drop cap. Front-page excerpts are 400 at 16px.
- Tokens: `Display`, `Labels`, `Copy`, `Meta` groups in `tokens.json`; each style names its use and its phone size.

## Space, edges, grid
- Gutter steps with the viewport: `pad-phone` 16 → `pad-tablet` 24 (600px) → `pad-desktop` 32 (821px) → `pad-wide` 64 (1100px); content stops at `measure-wrap` 1440px.
- Every link and button is at least `tap-target` 44px tall.
- Rule weights: `border-2` kicker dash and underline, `border-3` focus ring, `border-4` pull-quote bar and the board's foot.
- Mobile-first breakpoints `bp-tablet`, `bp-desktop`, `bp-wide`, plus 429 / 374 / 360 for the masthead and score bug.

## The masthead (phone fix)
One slim `mast` band: typeset `wordmark` (clamp 34–44px on phones, 56px desktop), the tracked "MEDIA" label (hidden under 430px) and a compact Join button. No dateline row, no logo image, no white block behind the lettering. The old `gatorbait-wordmark.webp` in `assets/Logos` is kept for reference only.

## Components
Fourteen, all in `components/bundle.css`, each with a README and a live preview in both themes:
Masthead, SectionNav (links and score bug), Ticker, GameBoard, Kicker, Button, MoreLink, LeadStory (with the article type spec), LatestList, ColumnistRail, PullQuote, HubHead, Chips, GameDayCard. Wrap a page in `class="gb"`; switch to night with `data-theme="night"`.

## Game-day cards
The pregame, final, halftime and quote share graphics follow this system (white card, `gator-blue` band, 8px orange rule, Condensed names and numerals). They are rendered as PNGs by `assets/gameday/` in the GatorBait repo from ESPN data; a sample-data card carries an "orange-ink Sample data" tag. `GameDayCard` is the in-page miniature.

## Don't
- No navy fields, no Paper cream ground, no other font families, no radius, no gradients or shadows.
- No white text on `orange` or on `paper`-coloured fills; no orange small text on white.
- No dateline above the masthead; no second Join button.

## Provenance
Extracted from `Presidente49/gatorbait-media-redesign`: `sports-live/src/front-page.css` (Gator Day look, commit `172a231`; masthead `ebcc797`), `assets/sitewide-type-condensed.css` and `docs/TYPE-STANDARD-2026-10.md`, and `assets/gameday/`. Photos in `assets/Photography` are third-party editorial images used only in previews; confirm rights before reuse. `tokens.css` is generated from `tokens.json` by `tools/build_tokens_css.py`.
