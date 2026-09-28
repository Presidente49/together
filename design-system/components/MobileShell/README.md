# MobileShell

The only phone header: a sticky `paper-white` bar with a 4px `gator-orange` top, the wordmark left and a Menu trigger right. The trigger opens a drawer from the right.

## Anatomy
- **Bar** (`gb-shell`): 64px tall (60px at 420px and below), `space-8` by `space-12` padding, `shell-line` below, `shadow-shell` on the front page. Add `gb-shell--inner` on inner pages for no shadow.
- **Trigger** (`gb-shell__trigger`): 44px tall, 78px wide, `control-line` border, square, three 2px `gator-blue` bars and "MENU".
- **Drawer** (`gb-drawer`): `min(88vw, 360px)` wide, slides in over `scrim` in 240ms with `shadow-drawer` on its edge. Items are 50px, 800 16px `navy-deep`; the current item gets a 4px `gator-orange` left marker on `wash`. The Join Button (`gb-button--signal`) closes the list, and `slate-ui` footer text follows.

## Use it
- Appears at `bp-phone` (820px) and below and replaces the Masthead; never show both.
- Lock page scroll while the drawer is open. Close it from the × (a 44px circle), the scrim and Escape.
- The consumer supplies the nav items, the current route and the open state (`aria-expanded`).

## Known gap
The source rings focus here in `peach-focus`, 1.7:1 on `paper-white`, and the `control-line` borders are 1.8:1. Both are under the 3:1 non-text minimum.
