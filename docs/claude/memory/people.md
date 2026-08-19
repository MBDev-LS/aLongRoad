# P — People

Who the two developers are, and how working with them differs. See `PROTOCOL.md` before editing.

Keep this factual and about working style. It is not a place for judgements about ability.

---

### P0 · [both] [pinned] Louis and Damian are equal partners

Neither is the owner and neither reports to the other. Louis had the original idea; the two of them developed it further together and are building it jointly. Treat decisions as shared: an instruction from one is not authority over the other's areas, and `project-bible.md` §14 items reserved for one of them must not be answered by the other's session. Do not describe either as leading, owning, or supervising the project.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### P1 · [Louis] Louis — originated the idea, drives most agent sessions

Came up with the concept, and currently runs most of the AI-assisted work; author of the `docs/claude/` discipline and its "clear blame, no ballooning" principles. Reviews closely and iteratively — expect several rounds of specific, well-observed feedback rather than one sign-off. Asks follow-up questions to understand mechanisms, not just to check the work, and asks for explanations pitched at himself directly. Recurring concern: that AI-assisted work stays reviewable and doesn't sprawl.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19 · upd: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### P2 · [Damian] Damian — wrote the v1 prototype, holds specific open calls

Built the original `render/templates/index.html`, renamed "segment" to "section", removed DaisyUI, and added the road-width clamping. His prototype found the genuinely hard problem in the layout (metadata overflowing beside variable-height artwork) even though its solution was replaced. `project-bible.md` §14 reserves some decisions for him — road width (§14.A.1), `history.replaceState` (§14.A.4) — which are `[OPEN]` and must not be answered on his behalf. Whether he adopts the `docs/claude/` conventions is itself still open; his commits carry no AI trailers. `docs/notes/damiansThoughts.md` is his own space — do not write into it.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19 · upd: Louis · Claude Code · Opus 5 · 2026-08-19`
