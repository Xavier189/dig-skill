---
name: dig
description: Socratic requirements excavation before starting work. Use BEFORE substantial tasks — new features, new projects, architecture or technology decisions, refactors, complex configuration changes — and BEFORE entering plan mode for such tasks. Also use whenever a request contains vague goals, hidden decisions, or underspecified details. Decomposes the request, surfaces hidden decisions and ambiguities, asks batched precise questions, and produces a clarity memo the user confirms before any work begins. Skip for small fixes, single-point edits, and purely informational questions.
---

# Dig — Socratic Requirements Excavation

Surface what the user actually wants before any work begins. The stated request is a starting clue, not the requirement. Hidden intent, unstated constraints, and decisions silently delegated to you are where delivered work goes wrong.

<HARD-RULE>
Do not start implementation, write code, or present a final plan until the clarity memo (Step 4) is confirmed by the user. If already in plan mode (or your platform's planning flow), complete the dig before writing the plan — the memo is the plan's input.
</HARD-RULE>

Match the user's language; keep technical terms in their original form.

## The bar every question must clear

Ask only what would change what you build. Before asking anything, name two realistic answers that would lead to different approaches; if every likely answer leads to the same action, you already know enough — don't ask. And a fact you can look up yourself — in the code, the docs, the git history — never goes to the user, however much it would change the approach: look it up; questions are reserved for decisions, which are the user's alone. This bar outranks every step below: a step performed without it is theater.

## Process

### 0. CONTEXT — absorb before hypothesizing

Read what's relevant: files the task touches, project docs, and — if your platform keeps persistent memory — stored long-term goals and recurring preferences. Look for the user's bigger picture — a deliverable that is technically correct but misaligned with their long-term plans is still a failure.

Reading has the same bar as asking: read only what could change the hypothesis or the questions, and stop once you can name the traps and forks — full understanding is the work phase's job, not this step's. Depth follows the task: for diagnose-and-rework requests the excavation IS the point — dig until the mechanism is pinned, and say what you are about to read and why, so the silence before the first question is accounted for; for new features read structure, entry points, and neighboring conventions, leaving implementation detail to the work phase; for direction or technology calls the docs may be all you need.

### 1. HYPOTHESIZE — commit to an interpretation the user can attack

Before asking anything, present a working hypothesis in three parts. Write every part so the user could point at a line and say "no — that's wrong". Self-test: if a sentence would survive unchanged in a different task's hypothesis, it is filler — delete it.

1. **What you actually want** — the outcome behind the stated request, in one or two sentences. If the request is a solution ("add a Redis cache"), state the problem you believe it is meant to solve ("the list page is slow at peak") — the gap between those two is where digs pay off.
2. **Where this goes wrong** — the one or two places THIS task is most likely to fail or be misread: a named trap ("paginated filtered lists are the worst case for caching — key explosion, low hit rate"), never a generic risk ("scope may creep").
3. **If forced to start now, I would…** — a concrete sketch, one decision per line, each line marked:
   - ✅ explicit — the user already said it
   - 🔍 delegated — you'd default to X, but the user should ratify (technology choice, structure, trade-offs, anything hard to reverse); recommend, never silently decide
   - ❓ ambiguous — you can't even pick a default

Keep the whole hypothesis under ~15 lines — it must be correctable on sight. The sketch is bait: a concrete plan draws corrections that an abstract list of unknowns never will.

Before showing it, stress-test it from six angles: real goal (is the ask a means to something unstated?), scope (what does the user assume is in or out that you don't?), success criteria (would you both agree it worked?), failure (what breaks first, and who notices?), dependencies & constraints (what must exist, or must not change?), long-term fit (does the sketch fight the user's bigger picture?). These are attack angles, not sections to fill — never write one line per angle. Most angles won't bite; the two or three that could overturn part 1 or reroute part 3 are exactly where your questions come from.

If the stress-test leaves more than ~8 unresolved forks, the task is too big for one dig — propose splitting it into sub-tasks instead of interrogating.

### 2. ASK — batched questions grown from the weakest points

Present the hypothesis, then ask — via AskUserQuestion in Claude Code, or as a numbered list in a single message on platforms without a structured question tool: up to 4 questions per batch, ordered by impact, each with concrete options and a recommendation. Never drip-feed one question per turn. Ask everything you already know is open now — the loop below exists for questions born from answers, not for rationing known ones. And batch only independent questions: one whose existence or option set depends on how another question in this batch is answered is not askable yet — hold it for the loop, where it is exactly a question born from that answer and passes the gate by citing it. Recommendation-only coupling is not dependence: keep the question in the batch and write the recommendation conditionally ("if peak-only, X; otherwise Y").

Every question must:

- name what it tests — which part of the hypothesis, which 🔍/❓ fork. A question you can't tie to the hypothesis (including "anything else I should know?" filler) is a checklist reflex: cut it.
- clear the bar above — some realistic answer must change the approach.
- refuse solutions disguised as requirements — trace "add a cache" back to the slowness it is meant to fix before designing the cache.

Some forks cannot be asked, only shown. When a fork is a taste call the user will only recognize on sight — visual style, interaction feel, wording, naming — an abstract question buys nothing ("what style do you want?" returns "not sure"): attach 2-4 concrete sketches for the user to react to (as option previews in AskUserQuestion on Claude Code; inline in the message elsewhere) instead of asking for a description they cannot give.

If the stress-test leaves no 🔍 or ❓ standing, say so and go straight to the memo — a dig with zero questions is a legitimate outcome, not a failure to perform.

Calibrate every batch against **Shallow vs deep** at the end of this file.

### 3. LOOP — dig until answers stop moving the hypothesis

Each answer can expose a fork that was invisible before it. A loop of batches is not drip-feeding: a new round is justified only by new information from the last one. After every batch:

1. **Update the hypothesis out loud, delta only** — "your answer on X changes the sketch: …". Never restate what didn't move.
2. **Admission gate for follow-ups** — a new question earns its place only if it states, inside itself: (a) which answer opened it — quote or closely paraphrase the user's words — and (b) which fork it decides. Shape: "You said writes must be visible immediately — that rules out plain TTL, so: invalidate on write, or drop caching for this query?" If you can't fill both slots, you are re-running a checklist, not following a thread: drop it.
3. **Converge** when a round's answers open no admissible follow-ups and every 🔍/❓ is resolved or explicitly deferred. Say you've converged and move to the memo — never pad a final round to look thorough. There is no round cap and no round quota: one round often suffices; the gate decides, not ambition.
4. **Too big?** If two consecutive rounds each open as many new forks as they close, stop interrogating — the request is several tasks wearing one sentence. Propose a split and dig only the first sub-task.
5. **Escape hatch** — if the user says "开工", "start", "just do it", or equivalent, stop asking immediately: fold every unresolved item into the memo's Open items with the default you will apply, and present the memo for its usual confirmation.

### 4. SYNTHESIZE — the clarity memo

Present a memo the user can verify in ~10 seconds, exactly five sections:

- **Goal（真实目标）** — the actual objective, one or two sentences
- **Decisions（已拍板）** — each ratified decision, one line each
- **Boundaries（明确不做）** — explicit exclusions
- **Success criteria（成功标准）** — checks the result can be verified against; prefer measurable over sentiment ("p95 under 500ms", not "feels fast")
- **Open items（开放项）** — deferred questions, risks, remaining assumptions

Get explicit confirmation. Then hand off: into plan mode for large builds, or straight to implementation for contained work. The memo is the downstream input, and it travels with one standing rule — no dig catches every fork before work starts: when implementation hits a fork the memo does not cover, take the conservative option, log it under a `Deviations` note, and keep going; but stop and come back to ask when it touches a data model, a public interface, or anything hard to reverse.

### 5. SETTLE — persist what outlives the task

- Long-lived information only: cross-task goals (e.g. an ongoing side project this task serves), recurring preferences, domain background. Nothing task-local.
- At most 1-2 memory writes per dig; check existing memories first and prefer updating over creating. No persistent memory on your platform? Skip the writes.
- Clearly cross-project facts: suggest the user add them to the global instructions file (CLAUDE.md, AGENTS.md, or your platform's equivalent) — do not edit global config yourself.
- Memo persistence is OFF by default. When the user asks to save (or a harness integration requests it), write to `docs/clarity/YYYY-MM-DD-<slug>.md` with frontmatter `task`/`date`/`status` and the five memo sections as fixed headings — that structure is the machine-readable contract.

## Shallow vs deep — calibrate here

User request: "Our user list page takes 3-4 seconds at peak. Add a Redis cache for it — give me an implementation plan."

Shallow — each looks professional; none changes whether caching is even the right move:

- "Redis or Caffeine?"
- "What TTL — 5 minutes or 30?"
- "Cache the full page response, or per-user entries?"

These pick parameters on top of an unexamined plan; they accept the disguised solution as the requirement.

Deep — each names the fork it decides:

- "Is the page slow only at peak, or always?" — always-slow points at the query itself, where an index might fix it outright; peak-only points at pool/concurrency, where a cache barely helps. Decides whether Redis is the right project at all.
- "After someone edits a user, how stale may the list be?" — "must be fresh immediately" makes invalidation the real project and query optimization probably cheaper; "minutes are fine" makes plain TTL viable. Decides the shape — or the existence — of the cache design.
- "Has anyone measured where the 3-4 seconds go?" — if not, the sketch starts with EXPLAIN and pool metrics, not Redis; a 30-minute index beats a permanent consistency tax. Decides step 1 of the work.

A legitimate round-2 follow-up, in the admissible shape:

- "You said it's only slow at peak and the connection pool maxes out — that moves the diagnosis from 'slow query' to 'connection starvation', so: raise the pool, or first find what's hogging connections?"

Copy the moves, never the content. The deep moves are: trace the intent, price the consequence, attack your own sketch. Never reuse these literal questions on a task that is not this task.
