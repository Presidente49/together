# Masthead

The site header: one slim band with the typeset wordmark and the Join button. It is a header, not a broadsheet nameplate: no dateline row, no logo image, no white block behind the lettering (the phone fix, Oct. 4).

## Anatomy
- Band: `mast` (Gator blue by day, deep navy at night), text `on-mast`. Padding `space-12` on phones, 18/16px from 821px.
- Wordmark: `wordmark` style, uppercase, `on-mast`. Phones scale it with clamp(34px, 10vw, 44px); 56px from 821px. The small tracked "MEDIA" beside it is `mast-sub` and hides under 430px so the wordmark never wraps.
- Right side: a "Sign in" link (from 821px) and the Join button at compact size (40px; 13px type under 375px; 44px/15px on desktop).

## Use it
- Exactly one masthead per page, first in the document. Next comes the Ticker, then the SectionNav.
- Keep the wordmark text, not an image: the old logo webp carried an opaque white box that showed as a block on blue.
- The Join button is the one orange-ink element in the band; there is no second call to action.

## Don't
- No dateline, edition line or tagline row above or below the wordmark.
- Don't put the wordmark on `paper`; it is white on blue.
