# C — Code preferences

Implementation and code-style. See `PROTOCOL.md` before editing.

---

### C1 · [both] CSS over JavaScript wherever CSS can do the job

Reach for a CSS mechanism before a scripted one. Damian's `ResizeObserver` text-clamp was replaced with `-webkit-line-clamp` because the script couldn't see sections loaded later, was O(n) per fire, and broke silently if `line-height` computed to `normal`. Recorded as a standing rule in `project-bible.md` §15.6.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### C2 · [both] Fix causes structurally, not symptoms

When several bugs share a root cause, find it and fix it once. Three separate mobile symptoms (detached images, misplaced head tile, blank expand area) were one grid-column bug. When asked how to balance two conflicting constraints, Louis wants the option that dissolves the conflict — moving the More/Less toggle out of the description box removed both the overlap and the crowding, where styling either in place would have traded one for the other.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### C3 · [both] Progressive enhancement — content parity is non-negotiable

Base state must work without JavaScript; script only adds interaction. Mobile drawers default open in CSS and collapse only once `road.js` marks itself ready. Nothing may be `hidden` at a breakpoint — hiding metadata below `md` was called the most serious defect in the original prototype (`project-bible.md` §11, §15.3).

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### C4 · [Louis] No "AI-slop" styling

Stated directly in the original brief: do not resort to AI/Claude-type styling. Follow the project's own visual language in `design-plan.html` — restrained, editorial, one flourish. No gradient-heavy cards, no emoji headings, no generic component-library look.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### C5 · [both] Self-documenting code over long comments

Make intent legible from names and structure first; a comment is the fallback, not the plan. Where a constraint genuinely isn't visible in the code (a spec quirk, an approach that was tried and failed), keep the note short and put the full rationale in the design plan or `docs/claude/output/`, linked by name — not in a fifteen-line block comment. Louis corrected an earlier version of this entry that had licensed exactly that: the CSS in `components/meta.css` still carries over-long comments from before the correction.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19 · upd: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### C7 · [both] Weigh maintainability explicitly, for humans *and* agents

Ask how easily the next reader — another developer or another AI agent — can understand, edit and extend what you write, and let that judgement change the design, not just the comments. Louis names both audiences deliberately: this project expects many agent sessions that share no memory, so structure that only makes sense to whoever wrote it is a real cost.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### C6 · [both] One markup source — never duplicate templates into JS

`_section.html` serves the server-rendered first batch and every batch the loader will later fetch. Duplicating section markup into a JS template is named in the bible, the design plan and `README.md` as the most likely source of drift in this project.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`
