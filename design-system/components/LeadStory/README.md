# LeadStory

The front page's one dominant story: a photograph beside the lead copy, which opens under a 4px `orange` rule.

## Anatomy
- Figure: the photo at `ratio-lead` (at most 430px tall), `object-fit: contain` on `stone`, with a `gb-caption` credit ("At the Florida Gators podium · Photo: Tim Casey / GatorCountry.com").
- Copy: Kicker, the headline in `lead-headline` (fluid 29 to 36px), a `deck` in `slate` capped at `measure-deck`, a `meta` line ("Buddy Martin · September 22, 2026") and a ReadLink.
- Grid `.9fr / 1.1fr` with a `space-24` gap. At 1100px the photo stacks above the copy at 16/10; at 820px it is 230px tall and the headline 28px.

## Use it
- One per page. Buddy Martin's newest column leads, with the kicker "The Buddy Martin column"; any other lead gets "The Big Read".
- Print the full headline, never truncated. Keep the photographer's credit.
- The consumer supplies the story: title, deck, author, date, canonical URL, photo, alt text and credit.
