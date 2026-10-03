# Masthead

The desktop header shared by the front page and every inner page: wordmark, tagline and Join button, then a shallow section nav under a 3px `navy` rule.

## Anatomy
- Brand row: the wordmark at `logo-width` (250px, `ratio-logo`), the tagline "Independent voices. / **Unmistakably GatorBait.**" behind a `rule-soft` divider, and the default Button pushed right.
- Section nav: 700 13px, 24px gaps, `border-3` `navy` above, `border-1` `rule` below, 48px tall. The current section carries `aria-current` and turns `orange-text`.
- A skip link ("Skip to stories") sits first and appears on focus.

## Use it
- Nav items, in this order: Front Page, Latest, Magazine, GatorBait TV, Podcasts, Message Board, Store, Sign in. One row, no dropdowns.
- Hidden at 820px and below, where the MobileShell is the only header.
- The consumer supplies the current route.
