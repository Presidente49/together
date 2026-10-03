# ReadLink

The text link that takes a reader to the full story: 700 12px Barlow in `gator-blue`, 44px tall, arrow last.

## Use it
- **`gb-read`** under the lead story: "Read the story →". Wrap the arrow in `<span aria-hidden="true">` so it slides `space-4` on hover (160ms, fine pointers only, off under reduced motion).
- **`gb-more`** under a list: "All stories →", in the surrounding ink.
- **`gb-panel-link`** stacks panel links: "Open the magazine →", "Watch GatorBait TV →".
- The consumer supplies the label and the canonical article URL. Never link a duplicate copy of a story.
