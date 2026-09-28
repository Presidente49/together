# Button

A square, solid call to action: `navy` fill, `on-navy` label, 700 13px Barlow, no radius.

## Variants
- **Default**: "Join GatorBait →" in the masthead. Hover fills `gator-blue` over 160ms on fine pointers only.
- **`gb-button--block`**: full width, 15px/1.4, at least `tap-target` tall. Membership plan buttons and the contact form's "Send message".
- **`gb-button--signal`**: the mobile drawer's Join. `gator-orange` fill with a `navy-deep` label (5.2:1), uppercase, 48px tall.

## Use it
- One button per view; everything else is a ReadLink or panel link.
- Labels are verb-led and exact: "Join GatorBait", "Send message", "Explore membership". An arrow (→) follows a label that leaves the page.
- The consumer supplies the label and an `href` (use `<a>`), or a native `<button>` for forms.

## Don't
- No rounding, shadows or gradients; the source strips Wix's own.
- Don't put white text on `gator-orange` (3.5:1).
