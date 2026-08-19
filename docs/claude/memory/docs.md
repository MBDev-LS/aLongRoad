# D — Documentation and explanation preferences

How to write for these two. See `PROTOCOL.md` before editing.

---

### D1 · [Damian] Keep documents short

Louis's instruction when briefing a handover note for Damian: "He doesn't like super long documents. Keep it as brief as you can while clearly getting across the key details." Default to the shortest version that lands the point when writing anything Damian will read.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### D2 · [Louis] Enough detail to edit and extend, within a stated cap

Louis asks for a length bound and expects it respected — "4-5 A4 pages worth of markdown max", "clear and concise while providing enough detail". His test for a document is whether he can understand, edit and extend the work from it alone. Detail that serves that test earns its space; recap of what the code already says plainly does not.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### D3 · [both] Tailor explanations to the reader's own work

Louis explicitly asked that Damian's handover be framed against what Damian built and what's in his notes — his class names, his script, his instincts. Explain a change as a delta from what that reader already did, not as an abstract description of the result.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### D5 · [both] Generated documents go in `docs/claude/output/`

Handovers, structure write-ups and any other document produced for a person to read belong in `docs/claude/output/`, not `docs/notes/`. `docs/notes/` holds the developers' own files — `damiansThoughts.md` and `louisThoughts.md` are personal space, never written into by an agent.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`

---

### D4 · [Louis] Explain the why, including what was tried and rejected

Louis reads documentation and comes back with questions about specific mechanisms. Record approaches that were attempted and abandoned along with the constraint that killed them — the `content-visibility` paint-containment finding is the example — so nobody re-attempts them. Write these so they answer the question before it's asked.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`
