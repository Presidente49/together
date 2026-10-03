# Field

A labelled form control plus the full-width submit button, as on the contact page.

## Use it
- Label above in `body-small` (`ink-body`). Inputs and textareas are 16px so iOS doesn't zoom, on `paper-white` with a `rule-soft` border, square, at least `tap-target` tall (textareas 100px).
- Stack fields with `space-18` in a form at most `measure-form` wide, and finish with a `gb-button--block` that says what happens ("Send message").
- Keep the platform's native submit handling; this is styling only.
- The consumer supplies labels, ids, values and validation messages.

## Known gap
`rule-soft` is 1.6:1 on `paper-white`, under the 3:1 a control border needs. The focus ring (3px `orange`) does meet it.
