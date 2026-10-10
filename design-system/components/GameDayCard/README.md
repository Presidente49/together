# GameDayCard

The share graphic for pregame, final, halftime and quote moments. The real cards are PNGs rendered from `assets/gameday/` in the GatorBait repo (1200×675 landscape, 1080×1350 portrait, 1080×1080 square); this component is the in-page miniature, shown as the Florida vs. South Carolina game-day card.

## Anatomy
- Top band `gator-blue` with the typeset wordmark and kicker, closed by an 8px `orange` rule.
- Status row: a `pill` (Final, Halftime or Game Day) and the date and venue.
- Score rows: team name in `board-score` family at 78px; rank in `orange-ink` and record in `ink-2`; the focus team (Florida) in `link`, the opponent in `ink-2`.
- Footer `hub` strip: site name left, source credit right ("Score: ESPN"). A card made from sample data carries an `orange-ink` "Sample data" tag so it is never posted by mistake.

## Use it
- Facts come from ESPN's summary endpoint (scores, records, ranks, line, stats); nothing is typed by hand.
- Render with `node assets/gameday/render.mjs final --event <id>`; outputs are checked for exact pixel size.

## Don't
- No logos or photos on the cards.
