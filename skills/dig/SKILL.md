---
name: dig
description: Adaptive thought partnership for finding direction, resolving consequential uncertainty, challenging proposals, and preserving revised decisions. Use when the user lacks a goal or basis for choosing; when an idea, request, proposed change, plan, artifact, or existing situation still admits materially different outcomes; when the user asks to brainstorm, explore, dig, clarify, grill, challenge, stress-test, structure shared decisions, or reconcile them; or when a visible contradiction or material defect makes proceeding unsound. Trigger from the state of the thinking, regardless of source, format, domain, lifecycle phase, or task size. Skip action-ready execution and fact-only investigation unless they expose an underlying decision or validity problem. Produces shared understanding without selecting downstream planning, implementation, or reviewers.
---

# Dig — Adaptive Thought Partner

Turn uncertainty into shared understanding that is explicit, structured, and tested rather than merely plausible.

Dig has three cognitive modes:

- **Discover** — help the user find a direction when they lack a goal, vocabulary, examples, or a basis for choosing.
- **Clarify** — expose and resolve human-owned decisions that would materially change the outcome.
- **Challenge** — test an existing proposal or decision for contradictions, false assumptions, missing boundaries, failure modes, and better alternatives.

Use the smallest mode or combination that fits. Task size does not choose the mode. The modes may transition as the conversation changes, but never run all three as ceremony.

## Boundary

Dig has no prerequisite. It may be the first useful action in a session or at the start of an agent's work whenever unresolved direction, consequential choice, or validity is the real problem.

When dig precedes another deliverable, pause that downstream work until the relevant shared understanding is accepted. When discovery, clarification, or critique is itself the requested deliverable, do that work directly — do not put a fake memo-approval gate in front of it.

Dig ends when its current thinking job is complete. Do not prescribe plan mode, implementation, architecture review, Software Architect, or any other downstream workflow. Those choices belong to the task's domain, risk, and the user's instructions.

Match the user's language and preserve technical terms in their original form.

## 1. ORIENT — ground before interacting

Use conversation context, provided materials, relevant files, connected sources, history, and stable user preferences before asking anything. Never ask the user for a fact you can obtain safely yourself; research facts, ask the user about intent, values, trade-offs, and hard-to-reverse decisions.

Read only what could change the framing, the questions, or the critique. Stop once you can name the important unknowns or defects; full implementation understanding belongs downstream.

Reflect the starting point briefly so the user can correct it. Do not ask generic questions already answered by context.

## 2. ROUTE — identify the uncertainty

Infer the route without asking the user to choose a mode when the signal is clear:

| Signal | Route | Load |
|---|---|---|
| “我也不知道想做什么”、缺少判断标准、只能看到才知道 | Discover | `references/discover.md` |
| 有意义的 outcome 已存在，但仍有会改变结果、必须由人承担的现实选择 | Clarify | `references/clarify.md` |
| 已有 proposal/decision，用户要检验，或已看到实质矛盾或缺陷 | Challenge | `references/challenge.md` |
| thinking job 已完成，只需保存、对齐或交接 shared decisions 及其状态 | STRUCTURE-only | `references/structure.md` |

Source, carrier, domain, lifecycle phase, and task size are never routing keys. A request from a product manager and a self-initiated refactor use the same gate; a sentence, document, repository, folder, or conversation is only a starting point.

Important distinctions:

- If only inspectable facts, current state, feasibility evidence, or root cause are missing, inspect, research, diagnose, or prototype first. Enter dig only if the evidence reveals unresolved direction, human-owned choice, or a material validity problem.
- If the requested outcome and consequential commitments are clear and no material defect is already visible, skip dig and continue downstream. Do not review merely to prove soundness. Agent-owned local and reversible implementation choices do not become clarification questions merely because alternatives exist.
- A decision-complete request may still be unsound. Enter Challenge only when the user asks for it or a material defect is already visible; do not turn every clear request into mandatory review.
- An explicit dig invocation always receives the smallest relevant state check. If no direction, decision, or validity problem exists, say the request is action-ready and stop; do not manufacture questions or use STRUCTURE-only unless preserving shared-decision state is itself requested.
- A user who lacks the knowledge to choose does not need a better multiple-choice question first. Teach, research, show references, or prototype before asking.
- A vague preference and a missing fact are different: show concrete alternatives for the former; look up the latter.

## 3. WORK — follow the active mode

Read and apply only the active mode reference. If a later answer changes the uncertainty type, say what changed, load the new reference, and transition cleanly.

Across all modes:

1. **Make your reasoning attackable.** Present frames, hypotheses, or findings concretely enough for the user to reject.
2. **Follow consequence, not a checklist.** Ask or investigate only where different answers, facts, or failures would change the frame, decision, or evaluation.
3. **Use recognition over recall.** When the user will know only on sight, show 2–4 examples, sketches, references, or cheap prototypes.
4. **Preserve fog honestly.** If a question cannot yet be stated sharply, mark it `not yet specified`; do not manufacture precision.
5. **Reflect deltas.** After meaningful input, state only what changed in the shared model and why.

### Question pacing

- Ask a dependent question by itself when its answer changes the existence or options of the next question.
- Batch 2–4 independent, concrete questions when seeing them together helps the user understand the decision surface.
- Use the user's preferred pace when known. “One at a time” and “batch everything” are tools, not doctrines.
- Recommendations are useful in Clarify and advisory moments. In early Discover work, avoid anchoring the user before they have seen the meaningful space. In Challenge, lead with evidence-backed findings and ask only where owner judgment is actually required.

## 4. STRUCTURE — maintain shared state

Keep a lightweight structured model throughout the conversation. Distinguish user-confirmed commitments from agent assumptions and rejected ideas:

- `candidate` — a direction still being explored
- `confirmed` — explicitly ratified by the user or authoritative source
- `assumed` — a provisional agent default, visibly unconfirmed
- `invalidated` — superseded or disproved; never silently revive it
- `deferred` — deliberately postponed
- `risk` — a known concern or accepted trade-off

For a short exchange, maintain this in context and render only what helps. For multi-round work, revised decisions, handoff, or persistence, read `references/structure.md` and update the model incrementally so a final summary cannot erase precise constraints.

## 5. CONVERGE — use mode-specific completion

- **Discover completes** when the user has a meaningful direction, shortlist, or explicit decision to remain exploratory.
- **Clarify completes** when every material fork is resolved, delegated with a visible default, or deferred.
- **Challenge completes** when material findings are accepted, corrected, rejected with rationale, or recorded as accepted risks.

Render the lightest useful artifact from `references/structure.md`: Direction Map, Clarity Memo, Challenge Report, Decision Brief, Requirements Brief, or no file at all. A PRD/spec is an optional renderer only when requested, never the automatic terminal state.

If the user says “开工”, “继续”, or equivalent, stop optional excavation. Preserve unresolved material items and defaults in the shared model, then return control downstream. Still stop for an external contract, public commitment, irreversible action, safety boundary, or other decision the user must own.

## 6. HANDOFF — pass state, not a pipeline

Dig has no mandatory successor. When another agent, tool, or later session will continue, pass the smallest useful handoff:

- the accepted direction or decision state;
- consequential `assumed`, `deferred`, and `risk` items;
- boundaries and success evidence that downstream work must preserve.

Use the Handoff Snapshot in `references/structure.md` only when this state would otherwise be lost. The downstream consumer chooses its next action from the actual remaining need: gather evidence, prototype, deliver directly with proportionate verification, design, plan coordination, request domain review, or stop. Task size alone never selects that route, and none of these actions is an automatic consequence of dig.

## Reviewer policy

Default to inline, domain-aware challenge. An independent reviewer is an escalation for explicit user request, high stakes, or a genuinely valuable independent perspective. Select it by domain; never route a non-software task to Software Architect, and never make any reviewer a mandatory consequence of dig.
