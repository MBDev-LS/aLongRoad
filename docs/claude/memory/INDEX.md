# Memory index

**This is the only memory file you load by default.** It is deliberately small. Read it at the start of every session; open a group file below only when the task actually touches that group.

**Revision 1** — 19 August 2026, `Issue-1` @ `06e80e3`. Created at Louis's request.

If you are about to **write or change** a memory, read `PROTOCOL.md` first. If you are only reading, you do not need it.

| Group | File | Covers |
|---|---|---|
| `C` | `code.md` | Implementation and code-style preferences |
| `V` | `design.md` | Visual, layout and UX taste |
| `D` | `docs.md` | Writing, explaining and documenting |
| `W` | `workflow.md` | Process: commits, models, verification, when to ask |
| `P` | `people.md` | Who Louis and Damian are, and how they differ |
| `T` | `tooling.md` | Tooling and environment gotchas — traps, not preferences |

Entries are `[both]`, `[Louis]` or `[Damian]` — whose preference it encodes, **not** who wrote it down. A `[Louis]` entry does not automatically apply to Damian's sessions.

---

## C — Code (`code.md`)

- `C1` [both] CSS over JavaScript wherever CSS can do the job.
- `C2` [both] Fix causes structurally, don't patch symptoms.
- `C3` [both] Progressive enhancement — no-JS must never lose content.
- `C4` [Louis] No "AI-slop" styling; follow the project's own visual language.
- `C5` [both] Self-documenting code over long comments.
- `C6` [both] One markup source — never duplicate templates into JS.
- `C7` [both] Weigh maintainability explicitly, for humans and agents alike.

## V — Design (`design.md`)

- `V1` [Louis] Restraint in sizing changes — "not loads, as per design".
- `V2` [Louis] Accent colour is blue, not green.
- `V3` [Louis] Notices mobile/narrow-viewport breakage quickly; check it before reporting done.
- `V4` [Louis] Controls must not crowd the content they act on.

## D — Docs (`docs.md`)

- `D1` [Damian] Keep documents short; he dislikes long ones.
- `D2` [Louis] Wants enough detail to edit and extend independently, within a stated length cap.
- `D3` [both] Tailor explanations to the reader's own prior work and vocabulary.
- `D4` [Louis] Explain *why*, including approaches tried and rejected.
- `D5` [both] Generated documents go in `docs/claude/output/`.

## W — Workflow (`workflow.md`)

- `W1` [Louis] Never commit unless explicitly asked.
- `W2` [Louis] Opus plans, Sonnet implements; commit messages must say which did what.
- `W3` [both] Verify in a real browser before claiming a UI fix works.
- `W4` [Louis] Report honestly, including trade-offs and residual costs.
- `W5` [Louis] Comfortable with auto-accept once a plan is approved.

## P — People (`people.md`)

- `P0` [both] Louis and Damian are equal partners — neither owns the project.
- `P1` [Louis] Originated the idea; drives most agent sessions, reviews closely.
- `P2` [Damian] Wrote the v1 prototype; holds specific `[OPEN]` calls.

## T — Tooling (`tooling.md`)

- `T1` [both] `md2pdf` silently swallows conversion errors on literal `{{ }}`/`{% %}` — wrap in `{% raw %}`/`{% endraw %}`.
