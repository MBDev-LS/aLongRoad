# docs/claude/ — how this workspace works

**Read this first if you are an AI agent working on this project.** Then read `project-bible.md` in full before changing anything.

This folder is a **tracked, human-readable workspace** for plans, decisions and context. It is committed to the repository like any other project file and pushed to GitHub. It exists because this project has two contributors and many AI agent sessions that share no memory with each other — a decision made in one chat transcript is invisible to everyone else. This folder is where that thinking becomes durable and shared.

**Revision 1** — 18 August 2026, against branch `Issue-1` @ `d47ba39`. Written at Louis's request when he created this folder.

---

## 0. Status markers apply here too

This document uses the same markers as `project-bible.md` §0, and for the same reason:

| Marker | Meaning |
|---|---|
| `[DECIDED]` | Settled by Louis, or already true in the repo. Build on it. |
| `[PROPOSED]` | A recommendation, not yet agreed by both contributors. Follow it, but say it's provisional if challenged. |
| `[OPEN]` | Undecided. Do not invent an answer. |

Much of the process below is `[PROPOSED]` because Louis set the principles and an agent drafted the mechanism. Damian has not signed off. Marking that honestly is the point — a governance document that quietly asserts its own authority is the first thing to go wrong.

## 1. The two problems this solves

`[DECIDED]` Louis's stated principles, in his words: everything should have a **clear blame**; it should be clear to humans and agents **what changed and by whom/what**; and structure matters because **the risk is AI-assisted work ballooning the codebase into something unmanageable.**

Two failure modes follow from those:

1. **Lost context.** Decisions that live only in a chat transcript are per-session and per-person. They don't survive.
2. **Uncontrolled growth.** Agents produce text and code quickly, and speed without discipline produces sprawl: duplicate documents, abandoned drafts, the same decision recorded in three places quietly drifting apart, and a codebase that gets harder to reason about the more work goes into it.

Worth stating plainly: the repository is currently **42 tracked files** excluding `node_modules`, with no models, no tests and one view. The ballooning risk is entirely ahead of us. That makes this the cheap moment to set the discipline, and it means the rules below should feel slightly over-engineered for the code that exists today. That's intended.

## 2. What lives in this folder

`[PROPOSED]` Two kinds of thing, and deliberately no third.

**Tier 1 — canonical living documents.** Currently three:

- **`project-bible.md`** — the single source of truth for project decisions. Status-marked throughout.
- **`design-plan.html`** — the visual and architectural argument behind those decisions. Open it in a browser.
- **`README.md`** (this file) — process for the folder itself.

These are **edited in place, never duplicated.** When something changes, revise the existing document; do not create a second file to hold the update. Each carries a **Revision line** at the top — number, date, `branch @ commit`, and one sentence on what changed — following the pattern `project-bible.md` already set. Bump it on every substantive edit.

`project-bible.md` §16 is the **index** of everything canonical here. A new document is added to §16 in the same commit that creates it; a removed one leaves §16 in the same commit. A file in this folder that §16 doesn't list is a bug: index it or delete it.

**Tier 2 — frozen exports.** `project-bible.pdf` and `long-road-open-questions.pdf` are point-in-time snapshots for sharing, not living documents. A fresh export **replaces** the file at the same name. Never accumulate `-v2`, `-final`, `-updated`.

**There is no Tier 3.** No session notes, no `ideas.md`, no per-agent working files, no dated one-off logs. Before creating any new file here, the test is: **does this belong in an existing document instead?** Almost always it does. A new file is justified only for a genuinely large freestanding topic that fits neither existing document and will be maintained — a formal CSAM or takedown protocol, say. It is *not* justified for a summary of what you did this session (that's the commit message and the revision line), or a draft of something destined for the bible (edit the bible, marking the unsettled parts `[PROPOSED]`).

## 3. Blame: how to tell what changed and who did it

`[DECIDED]` **Git is the ledger.** Do not build a parallel attribution system — `git log` and `git blame` already answer this, and a hand-maintained changelog would rot within a fortnight.

`[DECIDED]` **The commit author is the human who was driving** — Louis or Damian, never "Claude." AI involvement is recorded in a trailer, and it does not transfer accountability for the change.

`[PROPOSED]` **Commits with substantive AI-authored work carry the model-naming co-author trailer.** The repository already contains these, on Louis's commits:

```
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

Note that it names the **model**, not just "Claude". That is what makes it serve Louis's "by whom **and what**" principle: author gives you the person, trailer gives you the tool and its version. Don't reduce it to a bare `Claude`, and never strip it.

`[OPEN]` This convention is currently only on Louis's commits — Damian's carry no trailers. Whether Damian adopts it, and whether he points his own agent at this folder, is his call. **The whole scheme only works if both contributors do it**, so this needs raising with him rather than assuming. Logged in `project-bible.md` §14.

To answer "what changed here recently", in decreasing granularity:

```bash
git log --oneline -- docs/claude/          # what moved in the workspace
git log -p --follow -- docs/claude/project-bible.md   # how a document evolved
git blame docs/claude/project-bible.md     # who last touched a specific line
git log --format='%h %an %s%n  %(trailers:only=true)'  # which commits had AI involvement
```

`[PROPOSED]` **Contested or provisional points get inline attribution, not a new file.** If you want to flag something as your own read rather than settled fact — a recommendation, or a disagreement with what another instance concluded — write it inline at the exact point it concerns, as `[flagged by Claude/Louis, 2026-08-18]`. This keeps the blame next to the claim instead of in a separate note a reader has to go and find.

## 4. Keeping the *code* from ballooning

`[PROPOSED]` This is the principle Louis is most worried about, and it applies to the repository, not just to this folder.

**The target file structure already exists — use it.** Design plan §9.6 specifies exactly where things go: `theme/static_src/src/` with `tokens.css`, `base.css` and a `components/` directory; templates and static namespaced under `render/`; one `road.js` ES module. New code lands **in that structure**, not beside it. If what you're writing has no home there, that's a signal to stop and ask, not to invent a directory.

**One section partial, not two.** The loader contract (bible §8) requires that `_section.html` serve both the server-rendered first batch and every loaded batch. Duplicating section markup into a JS template is the single most likely source of drift in this project — it is called out in the bible, the design plan and here.

**The same "does this belong in an existing file?" test applies to code.** Prefer extending a module to adding one. Prefer a fixture to a new scratch script. The repo already carries the evidence of what happens otherwise: eight orphaned images and a stray `test.py`/`dynamicLoaderDesign.txt`, all flagged in bible §2.1 as deletable.

**No speculative generality.** Don't build the abstraction you think a later phase will want. The design plan's phases are a **sequence, not a menu** — working ahead produces code with no consumer, which is the purest form of the sprawl being guarded against.

**Delete superseded things in the commit that supersedes them.** Documents, code, scaffolding, abandoned experiments. Git history preserves every prior version, so a stale copy in the working tree costs a future reader time and buys nothing. If you notice leftovers from earlier AI-assisted work while doing something else, flag or remove them.

**Commit messages are part of the structure.** The established convention is `#N` plus a present-tense summary — `#1 removes DaisyUI, adds clamping to the road width, adds documentation`. The log is the blame mechanism, so a scannable log is load-bearing, not cosmetic.

## 5. Working protocol

`[PROPOSED]` For any agent session on this project:

1. **Read `project-bible.md` in full before changing anything.** Respect the markers: don't relitigate `[DECIDED]`, don't invent answers to `[OPEN]`.
2. **If your work resolves an `[OPEN]` question, update the bible in the same session** — move it out of §14, mark it, note who decided and when. Don't leave the answer in the transcript.
3. **If your work raises a new question, add it to §14 before you finish.** If it isn't written where the other contributor and their agent will see it, it didn't happen.
4. **Don't silently overwrite another instance's conclusion.** Correct stale facts freely — a wrong file path, a moved commit. For judgement calls, flag inline (§3) and leave it to a human.
5. **Check this folder before large structural changes** — the domain model (bible §4), the chain contract (§5), or anything shared. `index.html` in particular is flagged in bible §13.2 as a file both contributors edit.

## 6. Do and don't

**Do**

- Edit Tier 1 documents in place and bump the revision line.
- Keep bible §16 and the real folder contents in sync, in the same commit.
- Use git and the model-naming trailer for attribution — the mechanism already exists.
- Fold resolved and newly-raised questions into the bible as you go, not "later".
- Put new code in the structure design plan §9.6 already specifies.
- Delete superseded material in the commit that supersedes it.
- Ask, or log it in §14, rather than guessing.

**Don't**

- Create a file for a session summary, a draft, or anything that could be a section edit.
- Let a resolved question live only in a conversation.
- Strip or shorten the `Co-Authored-By` trailer, or otherwise obscure AI involvement.
- Silently overwrite a `[PROPOSED]` recommendation or a flagged disagreement.
- Build ahead of the current phase, or add an abstraction with no present consumer.
- Duplicate section markup between Django templates and JavaScript.
- Treat this folder as a second decision-making channel competing with the bible. One source of truth per topic.

---

**Index:** `project-bible.md` (the reference) · `design-plan.html` (the argument) · this file (the process).
