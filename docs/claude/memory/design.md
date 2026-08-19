# V — Design and visual preferences

Visual, layout and UX taste. See `PROTOCOL.md` before editing.

---

### V1 · [Louis] Restraint in sizing changes

When Louis asks for something bigger or wider, he means proportionally, not dramatically — "not loads, as per design". He gave an explicit figure for the road width (~20% more) and expects it applied as stated rather than rounded up to something that reads as a redesign. Ask for a number, or propose one, rather than guessing large.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### V2 · [Louis] Accent colour is blue, not green

The original `#1E5B3E` green was replaced with `#1E4E7A` (light) / `#7AB0DE` (dark). The accent drives the numeral hover, focus rings, link hovers, head-tile hover and vacant-slot hover from one token in `tokens.css`. Louis judged the green by how it looked on the large left-hand numerals specifically.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### V3 · [Louis] Check narrow viewports before reporting done

Louis resizes the browser and finds mobile breakage fast — he has reported it in detail more than once, as concrete symptoms rather than CSS terms. Test at 320/375/639/640px and expand a section before saying a UI change is complete.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### V4 · [Louis] Controls must not crowd the content they act on

A toggle that reserved space inside the description box was rejected as "annoying when trying to scroll and read", and when the actions row wrapped he wanted More/Less on the line nearest the text it controls. Proximity and footprint both matter: a control belongs near what it affects, without taking space from it.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`
