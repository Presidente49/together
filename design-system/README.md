GatorBait Media is an independent Florida Gators publisher: a free sports-news front page, GatorBait Magazine, GatorBait TV and The Buddy Martin Show, led by Buddy Martin's column. The system reads as a real sports newsroom and magazine. It is photography first, set in one family (Barlow), printed in navy on warm paper, and organized by rules instead of cards and shadows. Orange and Gator blue are accents, never floods.

## Content fundamentals

**Voice.** Plain, confident and knowledgeable, like a beat writer who has covered the program for decades. Short declarative lines. No hype words, exclamation marks or emoji anywhere in the interface.

- Tagline: "Independent voices. **Unmistakably GatorBait.**"
- Section promises: "The voices you come for.", "Beyond the final score.", "Gator conversation, from people who know the program."
- Actions name the destination and end with an arrow when they leave the page: "Read the story →", "All stories →", "Open the magazine →", "Join GatorBait →", "Watch GatorBait TV →".
- Honest status: "The GatorBait Message Board is being prepared. Discussion is not open yet." Never claim live, scheduled or open when the product doesn't back it.

**Headlines** run exactly as published, in the writer's own casing, and are never truncated or clamped: "The Med School Dropout Who Made Auburn Bleed Orange and Blue", "Sumrall Cussing: His Wife Wants Him To Please Stop. Damn!".

**Kickers** are two to four words in title or sentence case ("The Buddy Martin column", "The Big Read", "Only at GatorBait", "Game Week Reference", "Watch & Listen"); CSS sets them uppercase.

**Meta** is "Author · Month D, YYYY": "Buddy Martin · September 24, 2026". **Captions** name the game and the photographer: "Florida at Auburn · Photo: Chris Spears".

**Names** are exact: GatorBait (one word, capital B), GatorBait Media, GatorBait Magazine, GatorBait Magazine Newsletter (not "GatorBait Weekly"), GatorBait TV, The Buddy Martin Show, the Message Board.

**Editorial order.** Buddy Martin's newest column leads the front page, and he leads Magazine packages. Every other list is newest first. Each story has one canonical URL and one home; never show the same story twice on a page.

## Visual foundations

### Color
- Ground is `paper` (#fffdf9) everywhere; ink is `navy`. Use `ink-body` for article paragraphs, `slate` for decks, `slate-meta` for bylines and `slate-caption` for credits.
- `orange` is a rule color: the 4px top on section titles, lead copy, panels and plan cards, and the focus ring. It is 3.8:1 on paper, too light for small text, so kickers and the current nav item use `orange-text`.
- `gator-blue` is for links that move the reader on (the Read link, drawer links) and the Join button's hover.
- `gator-orange` belongs to the mobile shell: its 4px top border, the drawer's current-item marker and the mobile Join fill, labelled in `navy-deep`.
- `navy` fills exactly one block per page, the Magazine promo panel, with `on-navy` text and a `peach` kicker. `navy-deep` is the footer.
- `stone` grounds the voices band and letterboxes the lead photo; `photo-well` letterboxes every other photo.
- One theme, Paper. Dark broadcast-dashboard styling and pale-blue headings are rejected directions; don't add them.

### Type
- Barlow only: 400 for reading (`copy`), 700 for UI (`ui`), 800 for every headline (`display`), with `-0.025em` tracking on headlines and `text-wrap: pretty`. Never set Georgia, Times New Roman or Montserrat.
- Scale: `lead-headline` 36px (fluid from 29px), `page-title` 36px, `panel-headline` 31px, `band-headline` 29px, `story-headline` 23px, `card-headline` 21px, `section-title` 18px, `wire-headline` 16px.
- Reading: `article-body` 17px/1.68 on a 940px measure (16px/1.62 on phones), `deck` 15px/1.6 capped at 70ch.
- Labels: `kicker` 11px 700 uppercase at 0.1em, `meta` 11px, `caption` 10px, `edition` 10px at 0.12em.
- Phones: the lead headline drops to 28px/1.12, page titles to 28px (article titles 25px), story headlines to 19px. Everything fits 390px with no clipping and no sideways scroll.

### Layout
- Page measure `measure-page` (1240px); gutters `space-28` on desktop, `space-18` on phones, `space-14` at 360px and below.
- Front page: the main column and right rail split `2.1fr / 1fr` (rail at least 260px) with a `space-32` gap. Story rows are two across with `space-24` gaps.
- Breakpoints: `bp-tablet` 1100px stacks the lead photo; `bp-phone` 820px swaps the Masthead for the MobileShell and drops every grid to one column; `bp-small` 520px makes the Blog feed one column.
- One landscape ratio per module: `ratio-story` 16/9 for support rows, `ratio-card` 16/10 for the Latest grid, Blog and Magazine cards, `ratio-lead` 4/5 for the lead, `ratio-cover` 4/3 for the Magazine cover.
- Reserve image geometry before load so nothing jumps.

### Rules, borders, corners
- Hierarchy of rules: `border-4` `orange` starts a module; `border-3` `navy` frames the section nav and the Magazine cover; `border-2` `navy` frames the voices band; `border-1` in `rule`, `rule-soft` or `hairline` divides.
- Corners are square (`radius-0`) on every button, card, panel, input and photo. The only exceptions are the drawer's round close button (`radius-circle`) and the menu glyph's bars (`radius-bar`).
- No shadows on the page. Only the mobile shell (`shadow-shell`) and the open drawer (`shadow-drawer`) lift.

### Imagery
- Real, current editorial photography leads. Approved GatorBait and staff photographers first, never generated faces, helmets, logos or uniforms.
- Photos are shown whole: `object-fit: contain` on `stone` or `photo-well`, so portraits and wide shots share a box without cropping.
- Keep captions and credits. Texture, when used at all, is sparse: grain, paper, halftone or archive treatment, never lens flares or particles.

### Motion and states
- Motion is small and optional: button fills and the Read arrow ease over 160ms, only on fine pointers, and only when `prefers-reduced-motion` allows. The drawer slides in 240ms over a 200ms scrim fade.
- No entrance animations, no content that starts hidden, no autoplay story swapping, no scroll hijacking.
- Hover: links underline at a 4px offset on fine pointers. Current: `orange-text` in the nav, a 4px `gator-orange` marker in the drawer.
- Focus: a solid 3px `orange` outline at a 3px offset (`orange-focus` on the front page). Every link row, button and control is at least `tap-target` (44px) tall.

## Iconography

There is no icon set. Direction is a typed arrow (→), set `aria-hidden` when it follows a label. The menu glyph is three 2px `gator-blue` bars drawn in CSS, and close is a × in a circle. No emoji, no icon fonts.

The logo is the GatorBait script wordmark (`assets/Logos/gatorbait-wordmark.webp`, 900 × 241), blue with an orange outline. Show it at 250px in the masthead, 240px on the Magazine mast, up to 190px in the mobile shell and 168px in the drawer, always on a light ground, always from the file. Never redraw, recolor or re-letter it.

## Surfaces

- **Front page**: Masthead, LeadStory, a support row of two StoryCards, WireList, VoicesBand, "More from the newsroom" StoryCards, and PromoPanels in the rail.
- **Blog feed**: StoryCard `gb-story--feed` in a three-column grid. Wix keeps its categories, search and pagination.
- **Article**: `page-title` headline, `article-body` copy, 940px measure.
- **Magazine**: MagazineCover, then inside cards. The Magazine is separate from the free front page.
- **Membership and contact**: PlanCard and Field restyle Wix's native plans and forms without replacing them.
- **Phones**: MobileShell is the only header on every route.

## Accessibility notes

Every text pair above holds 4.5:1. Three source pairs miss the 3:1 non-text minimum and are kept as shipped: `peach-focus` as a ring on `paper-white` (1.7:1), the `control-line` borders on the menu trigger and close button (1.8:1), and `rule-soft` input borders (1.6:1). Use `orange` for rings and a darker border when you next touch those controls.

## Not synced

From Presidente49/gatorbait-media-redesign at d696498, not carried over: the retired dark "ESPN+/Athletic" Wix theme (`custom-css-LIVE.css`) and the Newsroom and Gazette previews' Georgia headline stacks, all superseded; the Wix-hosted live logo file, which could not be fetched (the repository's own 900 × 241 wordmark, the same size the live masthead reserves, is used instead); the newsletter's MJML email templates and the TV hub page, which have their own layouts. Components are static renditions of the site's HTML and CSS patterns in `components/bundle.css`; the site renders them from vanilla JavaScript embeds, so there is no component library to build.
