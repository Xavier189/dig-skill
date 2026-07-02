---
name: dig
description: Socratic requirements excavation before starting work. Use BEFORE substantial tasks — new features, new projects, architecture or technology decisions, refactors, complex configuration changes — and BEFORE entering plan mode for such tasks. Also use whenever a request contains vague goals, hidden decisions, or underspecified details. Decomposes the request, surfaces hidden decisions and ambiguities, asks batched precise questions, and produces a clarity memo the user confirms before any work begins. Skip for small fixes, single-point edits, and purely informational questions.
---

# Dig — Socratic Requirements Excavation

Surface what the user actually wants before any work begins. The stated request is a starting clue, not the requirement. Hidden intent, unstated constraints, and decisions silently delegated to you are where delivered work goes wrong.

<HARD-RULE>
Do not start implementation, write code, or present a final plan until the clarity memo (Step 4) is confirmed by the user. If already in plan mode, complete the dig before writing the plan — the memo is the plan's input.
</HARD-RULE>

Match the user's language; keep technical terms in their original form.

## Why decompose before asking

Questions asked before decomposition hit surface parameters, not load-bearing decisions. Shallow one-at-a-time questioning is the exact failure mode this skill exists to fix: decompose first, then ask everything that matters in one batch.

## Process

### 0. CONTEXT — absorb before decomposing

Read what's relevant: files the task touches, project docs, and memory (long-term goals, recurring preferences). Look for the user's bigger picture — a deliverable that is technically correct but misaligned with their long-term plans is still a failure.

### 1. DECOMPOSE — break the request into decisions

Split the request into its constituent sub-decisions and unknowns. Mark each:

- ✅ explicit — the user already specified it
- 🔍 delegated — has a reasonable default, but is a decision the user should ratify (technology choice, structure, trade-offs, anything hard to reverse)
- ❓ ambiguous — genuinely unclear or missing

### 2. CHECKLIST — sweep for blind spots

Run the decomposition against six dimensions; add any 🔍/❓ items the sweep uncovers:

1. **Real goal** — why this, and what will it be used for once built?
2. **Scope & boundaries** — what is explicitly NOT included?
3. **Success criteria** — how do we know it worked?
4. **Failure & risk scenarios** — what does failure look like, who notices?
5. **Dependencies & constraints** — what must exist first; time/compatibility/compliance limits?
6. **Long-term fit** — does this align with the user's bigger picture and existing habits?

### 3. ASK — batched, precise, anchored

First present the decomposition compactly (one line per item with its ✅🔍❓ mark) so the user can correct your understanding on sight.

Then ask ALL open items via AskUserQuestion in batches of up to 4, ordered by impact, each with concrete options and a recommendation. Never drip-feed one question per turn.

Question quality rules (hard):

- Every question must anchor to a specific 🔍 or ❓ item. No "anything else?" filler.
- Never accept a solution disguised as a requirement — trace "I need a button" back to the problem it solves.
- Surface delegated decisions (🔍) even when you have a good default: recommend, don't silently decide.
- If open items exceed ~8, the task is too big — propose decomposing it into sub-tasks instead of interrogating.

Stop condition: all 🔍/❓ resolved or explicitly deferred → converge. A second round only if answers open a new major fork. Hard cap: two rounds.

### 4. SYNTHESIZE — the clarity memo

Present a memo the user can verify in ~10 seconds, exactly five sections:

- **Goal（真实目标）** — the actual objective, one or two sentences
- **Decisions（已拍板）** — each ratified decision, one line each
- **Boundaries（明确不做）** — explicit exclusions
- **Success criteria（成功标准）**
- **Open items（开放项）** — deferred questions, risks, remaining assumptions

Get explicit confirmation. Then hand off: into plan mode for large builds, or straight to implementation for contained work. The memo is the downstream input.

### 5. SETTLE — persist what outlives the task

- Long-lived information only: cross-task goals (e.g. an ongoing side project this task serves), recurring preferences, domain background. Nothing task-local.
- At most 1-2 memory writes per dig; check existing memories first and prefer updating over creating.
- Clearly cross-project facts: suggest the user add them to global CLAUDE.md — do not edit global config yourself.
- Memo persistence is OFF by default. When the user asks to save (or a harness integration requests it), write to `docs/clarity/YYYY-MM-DD-<slug>.md` with frontmatter `task`/`date`/`status` and the five memo sections as fixed headings — that structure is the machine-readable contract.
