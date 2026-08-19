# Note from Louis

Hello. Just decided to go nuts and write out a long specification for Claude Opus and then implement it using Sonnet. It produced a v2 page based on your work (which I didn't want to overwrite). Feel free to either work off of this page or just take the bits you like. It deliberately doesn't have the loading system yet, but does have the start of a backup no-JS version. (Just as a placeholder and also so we can have it in the final one as a backup given it already exists.)

You'll notice that it's not finished and there's certainly things I'd changed, but I went through serveral revisions with Claude and it works in mobile layout as well. (Incl. the sliding animation.)

Claude wrote the rest of this, but I told it to be as concise as possible.


# Handover: the `/v2/` road page

18 August 2026, from work Louis and I (Claude) did on top of your prototype. Short version: your `index.html` is untouched, still live at `/`. This is a second page — `render/index2.html` at `/v2/` — same layout idea, restructured so the infinite-scroll loader (issue #7) has something solid to build on. Worth comparing the two side by side.

## What we kept

- The three-column shape: numeral / artwork / metadata, metadata top-aligned, not centred. That's exactly the layout diagram, and you had it right.
- `width` / `height` / `loading="lazy"` / `decoding="async"` on every image.
- The read that a stranger's description can overflow the space beside their art — that's genuinely the hard part of this layout, and you found it. We solved it differently (below), but finding it was the work.
- No copy-pasted markup ahead of a loop.

## What changed, and why

- **One shared grid, not one `grid-cols-100` per section.** Nothing in your version guarantees section *n* and *n+1* resolve the same column width — a one-pixel drift becomes a visible step once sections chain edge-to-edge. `/v2/` is one `<ol>`, every `<li>` sharing the same tracks off one variable (`--road-w`), so every section is provably identical width.
- **`aspect-ratio` instead of `w-full h-full` + `items-stretch`.** Stretching the art to fill the row distorts the drawing and breaks the anchor-point math the chain needs. Each section now reserves its own intrinsic ratio — no stretch, no shift on load.
- **CSS clamp + a small "More/Less" toggle, instead of the `ResizeObserver` script.** The script itself was a careful piece of work — debounced, reads-then-writes, avoids layout thrash — but it only recalculates on resize, never fires for a section that loads in later, is O(n) over every image on screen each time it does fire, and silently breaks if `line-height` ever computes to `normal`. Six lines now clip in plain CSS (`-webkit-line-clamp`), no script needed for the clip itself; a button reveals the rest by scrolling internally, and only appears when a description is actually cut off.
- **`<ol reversed><li value="N">`, not `<div>`s.** Screen readers get "item N of an ordered list" for free, and the visual numeral can be purely decorative.
- **Nothing is ever `hidden` on mobile.** `md:hidden` on your numeral and metadata meant a phone visitor got drawings and no text. `/v2/` instead tucks the text behind a tap — a real disclosure button, one section open at a time — so it's reachable, just collapsed.
- **One section partial, `_section.html`**, rendered for the first page load and for every batch a future loader fetches — so nobody ends up duplicating this markup in JS later. That's the main point of the rebuild: `fixtures.py` stands in for the model, `/v2/road/?before=<slot>` returns the next batch, and with JS off it degrades to a plain "Continue down the road" link.
- **`.road-*` class names, not `.segment-*`** — matching the "section" rename you'd already made in the template copy.

## Where it stands

Also has: a mobile-specific layout (separately fixed across a few rounds — narrow viewports had real bugs at first), a masthead, "jump to the end of the road", placeholder tiles for vacant/reserved slots that draw their own connecting line, and the road is now ~20% wider on large monitors than the first pass.

**Not built yet, on purpose:** the actual scroll loader, real fonts, the light/dark toggle control, unloading offscreen sections, the report dialog. All deferred to their proper phase, not forgotten — see the design plan.

**One gap to flag:** `project-bible.md` / `design-plan.html` got their revision bump when `/v2/` first landed, but haven't been re-touched for the mobile fixes since. Worth a pass before `/v2/` replaces `/`.

— Claude Sonnet 5 (Directed by Louis)
