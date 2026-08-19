# W — Workflow preferences

Process: commits, models, verification, when to ask. See `PROTOCOL.md` before editing.

---

### W1 · [Louis] [pinned] Never commit unless explicitly asked

Louis commits himself, and has declined a commit offer directly ("Not yet"). Across a long session of fixes he committed once, on his own, at a point of his choosing. Do the work, report it, and leave the tree dirty unless he says otherwise. Offering is fine; acting isn't.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### W2 · [Louis] Opus plans, Sonnet implements — and the commit says so

Louis switched models deliberately between planning and implementation, and required the commit message to make clear which model did which. Attribution is a stated project principle, not bookkeeping: `README.md` §3 wants the specific model named in the `Co-Authored-By` trailer, never a bare "Claude".

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### W3 · [both] Verify in a real browser before claiming a fix works

Layout claims need measurement, not reasoning. This project has no Playwright; `puppeteer-core` driving the system Chrome at `/usr/bin/google-chrome` is the working setup, launched headless with `--no-sandbox`. Measure element rects across breakpoints and read the screenshot — several fixes in this project looked correct in the CSS and were not.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### W4 · [Louis] Report trade-offs honestly, including residual cost

Louis wants the cost of a fix stated, not buried — where a change makes something slightly worse, at which widths, and why it was still the right call. He responds well to a clear recommendation with its downside attached, and badly to a claim of success that later turns out qualified.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`

---

### W5 · [Louis] Auto-accept once a plan is approved

Louis reviews plans carefully up front, then hands over: he approved the `index2.html` plan and asked for it to run with auto-accept. Once he has approved an approach, work through it without stopping for confirmation at each step — save the check-ins for genuine decision points he hasn't already settled.

`src: Louis · Claude Code · Sonnet 5 · 2026-08-19`
