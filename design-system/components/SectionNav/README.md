# SectionNav

The ruled nav under the ticker: section links on desktop and the score bug (last game, next game) everywhere.

## Anatomy
- Bar: `paper` with a 1px `rule` underline; 52px tall on phones, 56px from 821px.
- Links (from 821px): `nav` style, 44px tall; the current page in `orange-ink` with the 3px orange underline (`shadow-underline`). Links drop right to left when the bar is narrow so Store and the bug always remain.
- Score bug: the **last game** half is `gator-blue` with white `board-score`-style numbers; the **next game** half is `surface` with a 4px `orange` left rule and a `orange-ink` NEXT tag. A live game swaps the tag to `live-red`.

## Use it
- On phones the bug takes the full bar width, edge to edge (negative gutter margins).
- Scores and kickoff come from the same ESPN feed as the front page; don't hand-type them.

## Don't
- No dropdown menus; the phone drawer is the site's own.
