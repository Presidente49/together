# Button

A square, solid call to action: `orange-ink` fill, `on-orange` label, Condensed 800 uppercase.

## Variants
- **Default**: 44px tall (`tap-target`), `button` style, no radius. "Join GatorBait", "Send message".
- **`gb-button--ghost`**: transparent with a 2px `shadow-ring` in the text colour, for secondary actions beside a default button.
- **`gb-button--compact`**: 40px, 14px type; the masthead's Join.

## Use it
- One default button per view; the rest are MoreLinks or ghost.
- Labels are verb-led: "Join GatorBait", "Send message".
- Use `<a>` for navigation and `<button>` for forms.

## Don't
- Don't use `orange` (3.5:1 with white) for the fill; `orange-ink` is the fill that carries white text.
- **Flag:** at night `orange-ink` is the plain brand orange and white text on it is 3.5:1. The live site ships it that way; fix by switching night buttons to `ink` on `orange` (5.1:1) when the desk approves.
