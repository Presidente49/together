# Ticker

A 38px strip of the latest headlines and scores, scrolling slowly on a loop.

## Anatomy
- Band `band` (white by day, near-black at night), text `band-ink`, `ticker` style (Condensed 700, 13px, uppercase).
- Tag: `orange-ink` fill with `on-orange` text, tracked wide.
- Items: `tk-label` bold lead-in word ("Final", "Next"), then the text; an orange diamond separates items.

## Use it
- Four to eight items, newest first. Lead-in words are one word.
- Respect `prefers-reduced-motion`: the strip stops and scrolls by hand.

## Don't
- Don't put links on a second row; one line only, truncated with an ellipsis at 70vw per item.
