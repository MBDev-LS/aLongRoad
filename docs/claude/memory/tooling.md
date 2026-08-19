# T — Tooling and environment gotchas

Recurring traps in the tools and environment around this project — not preferences, not project decisions, but things that will bite again if forgotten. See `PROTOCOL.md` before editing.

---

### T1 · [both] `md2pdf` silently swallows conversion errors on literal template syntax

Any markdown file run through `md2pdf` (`docs/claude/output/*.md` → PDF) is first passed through Jinja2's `Template(...).render()`. Literal `{{ ... }}` or `{% ... %}` text — e.g. Django template snippets quoted as documentation — gets parsed as real Jinja directives; `{% include %}` throws `TypeError: no loader for this environment specified`. The CLI's `ThreadPoolExecutor` discards the submitted `Future` and never calls `.result()`, so the exception is silently swallowed: it still prints "🚀 Output files generated" and exits 0 with no PDF written. Fix: wrap the whole file in `{% raw %}` (first line) / `{% endraw %}` (last line) at draft time, before the first conversion attempt, whenever the doc quotes `{{ }}` or `{% %}`. To confirm a conversion actually worked, don't trust the CLI's success message — check the output file exists, or call `md2pdf.core.md2pdf(...)` directly in Python.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`
