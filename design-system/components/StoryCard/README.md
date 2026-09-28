# StoryCard

A linked story teaser: photo, meta and headline, stacked, with the whole card as one link.

## Variants
- **Default** (`gb-story`): support and coverage rows. `ratio-story` photo, `meta`, `story-headline` (23px; 19px on phones). Two across inside a `gb-row`, which draws a `rule` above.
- **`gb-story--wire`**: the Latest grid. `ratio-card` photo, `meta`, `wire-headline` (16px).
- **`gb-story--feed`**: the Blog feed. `ratio-card` photo, headline, then `meta`, with a `hairline-cool` separator. Three across, two at 820px, one at 520px with 16:9 photos.

## Use it
- Photos sit on `photo-well` with `object-fit: contain`, so portraits and wide shots keep their full frame in the same box. One ratio per row.
- Full headlines always; nothing is clamped or truncated. Newest first.
- The consumer supplies title, author, date, canonical URL, photo and alt text. No category chips.
