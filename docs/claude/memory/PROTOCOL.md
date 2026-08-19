# Memory protocol

**Read this only when writing or changing a memory.** Reading memory needs `INDEX.md` alone.

**Revision 1** — 19 August 2026, `Issue-1` @ `06e80e3`.

## 1. What belongs here — and what doesn't

This system stores **how Louis and Damian want to be worked with**. Nothing else.

| Belongs in memory | Belongs elsewhere |
|---|---|
| Stated preferences, corrections, working style | Project decisions → `project-bible.md` |
| Recurring feedback across sessions | Visual/architectural reasoning → `design-plan.html` |
| Who prefers what, and how they differ | What changed and when → `git log` |
| Approaches a developer has rejected, and why | Task state, todos, session summaries → nowhere; they're transient |

The hard boundary: **memory never decides anything about the project.** If a session settles a technical question, that goes in the bible with a status marker, exactly as `README.md` §5 requires. Memory records that Louis prefers CSS to JavaScript; the bible records that this project uses `-webkit-line-clamp`. Keeping that line clean is what stops this becoming a competing source of truth.

## 2. Entry format

Group files hold entries. One entry = one preference. Format is fixed:

```markdown
### C7 · [Louis] Short imperative title

One to three sentences. State the preference, then why it matters — the
reasoning is what makes it transferable to a situation you haven't seen.

`src: Louis · Claude Code · Opus 5 · 2026-08-19`
```

- **ID** — group letter + next unused number. **Never reuse an ID**, even after deletion; `INDEX.md` and past commits refer to them.
- **Scope tag** — `[both]`, `[Louis]` or `[Damian]`. Whose preference it is. Default to the person who expressed it; only use `[both]` when it genuinely applies to the project rather than a person.
- **Provenance line** — `src:` is *whose session* created it, which agent, which model, and the date. On update, append a second clause:

```
`src: Louis · Claude Code · Opus 5 · 2026-08-19 · upd: Damian · Claude Code · Sonnet 5 · 2026-09-02`
```

Only the most recent update is kept — git holds the rest. Agent field is whatever you actually are (`Claude Code`, `claude.ai`, `Cursor`, …); model is the specific model (`Opus 5`, `Sonnet 5`).

Optional markers, placed after the scope tag:

- `[pinned]` — load-bearing; never prune in a consolidation pass.
- `[disputed]` — Louis and Damian disagree, or an agent's inference was challenged. Never silently resolve one of these; ask.

## 3. When to write

Write **during** the session, at the moment the preference is expressed — not in an end-of-session sweep, which is where detail gets lost. Triggers:

- A developer corrects you, or rejects an approach.
- A developer states a preference explicitly ("I prefer…", "always…", "don't…").
- A developer approves something after previously rejecting alternatives.
- You notice you're being told the same thing a second time — that's the strongest signal, and it means the memory was missing or wrong.

Do **not** write an entry for: one-off task instructions, anything already in the bible, or your own guesses about what someone might want. A memory asserting a preference nobody stated is worse than no memory, because the next session will act on it.

## 4. Update, don't accumulate

This is the failure mode Anthropic's own memory work identifies: stores drift into duplicates, contradictions and stale entries because every write is local and incremental.

Before adding an entry, check the group's existing entries. Then:

- **Same preference, more detail** → edit the existing entry, refresh `upd:`.
- **Preference has changed** → rewrite the entry's body to the new value. Don't keep the old one alongside it; git has the history.
- **Genuinely new** → add it, and add its one-line summary to `INDEX.md` in the same edit.

`INDEX.md` and the group files must never disagree. If they do, the group file wins and the index gets fixed.

## 5. Consolidation

When a group file passes **~12 entries**, or a developer asks, do a consolidation pass over that file:

1. Merge entries saying the same thing in different words.
2. Replace contradicted entries with the current value.
3. Delete entries overtaken by events — a preference about code that no longer exists is noise.
4. Promote a pattern: if three entries are instances of one broader principle, write the principle and remove the instances.
5. Rebuild that group's section of `INDEX.md`.

Never prune `[pinned]`. Never resolve `[disputed]` without asking. Say in your reply that you consolidated and what you removed — silent deletion of someone's stated preference is not acceptable.

## 6. How developers request changes

Louis and Damian can direct this system in plain language — no syntax required. "Forget that", "that's not right, I actually prefer X", "that applies to me not Damian", "pin that one". Act on it in the same session, and confirm which entry changed by ID.

They may also edit the files by hand. If you find an entry that doesn't match this format, fix the format, keep their content.

## 7. Cost discipline

The read path is one small file. Keep it that way:

- `INDEX.md`: one line per entry, no bodies. If a line needs two lines, the entry title is too vague.
- Group files: bodies of one to three sentences. Long rationale belongs in the bible or design plan, linked by name.
- Don't re-read a group file you've already read this session.
- Don't restate memory contents back to the developer unless asked — act on them.
