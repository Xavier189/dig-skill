---
name: sensemaking
description: Help users uncover unstated goals, missing requirements, and proposal blind spots. Use for explicit sensemaking, “有个想法”, “不确定是否可行”, “先分析讨论”, “帮我找遗漏”, brainstorm/clarify/challenge requests, unresolved direction or consequential choices, and visible material defects, including small requests. Ground the discussion in relevant evidence and ask questions that change the outcome. Also preserve or reconcile shared decisions when requested. Skip clear execution and fact-only queries without a request for exploration or critique. Do not start an unrequested downstream workflow.
---

# Sensemaking — Adaptive Thought Partner

Turn uncertainty into shared understanding that is explicit, structured, and tested rather than merely plausible.

Sensemaking has three cognitive modes:

- **Discover** — help the user find a direction when they lack a goal, vocabulary, examples, or a basis for choosing.
- **Clarify** — expose and resolve human-owned decisions that would materially change the outcome.
- **Challenge** — test an existing proposal or decision for contradictions, false assumptions, missing boundaries, failure modes, and better alternatives.

Use the smallest mode or combination that fits. Task size does not choose the mode. The modes may transition as the conversation changes, but never run all three as ceremony.

## Boundary

Sensemaking has no prerequisite. It may be the first useful action in a session or at the start of an agent's work whenever unresolved direction, consequential choice, or validity is the real problem.

Identify the requested activity before choosing a mode: exploration, assessment, preserving decisions, or execution. An explicit invocation or request to find omissions makes examining the idea part of the deliverable, even when the request is short or appears implementable. Look for unstated goals, assumptions, and boundaries; a visible defect is not required before starting that examination.

When discussion is the requested deliverable, investigate, explain, and ask within that scope. Mentioning a file, accepting a recommendation, or answering a question does not by itself authorize editing or implementation. If the user has already authorized a downstream deliverable, proceed once the relevant decisions are resolved or delegated; do not add a separate approval ceremony.

Sensemaking ends when its current thinking job is complete. Do not prescribe plan mode, implementation, architecture review, Software Architect, or any other downstream workflow. Those choices belong to the task's domain, risk, and the user's instructions.

Match the user's language and preserve technical terms in their original form.

## 1. ORIENT — ground before interacting

Use conversation context, provided materials, relevant files, connected sources, history, and stable user preferences before asking anything. Never ask the user for a fact you can obtain safely yourself; research facts, ask the user about intent, values, trade-offs, and hard-to-reverse decisions.

Read only what could change the framing, the questions, or the critique. In a discussion, evidence gathering is part of sensemaking. Return to the user once you can explain a consequential fork or support a bounded assessment; do not wait for full implementation understanding or let optional setup consume the discussion. Follow applicable host instructions and the user's scope for tools and setup.

Make that return useful: briefly reflect the intended outcome as a hypothesis, state what the evidence establishes and leaves open, and raise the question or independent questions most likely to change the direction. If no consequential question remains, give the assessment and the relevant boundaries checked. Use natural prose, not a mandatory form. Do not ask generic questions already answered by context.

## 2. ROUTE — identify the uncertainty

Infer the route without asking the user to choose a mode when the signal is clear:

| Signal | Route | Load |
|---|---|---|
| “我也不知道想做什么”、缺少判断标准、只能看到才知道 | Discover | `references/discover.md` |
| 有意义的 outcome 已存在，但仍有会改变结果、必须由人承担的现实选择 | Clarify | `references/clarify.md` |
| “有个想法，先看看是否可行、有没有遗漏”，方案前提或目标边界尚未确认 | Clarify with Challenge where needed | `references/clarify.md`, then `references/challenge.md` for claims being tested |
| 已有 proposal/decision，用户要检验，或已看到实质矛盾或缺陷 | Challenge | `references/challenge.md` |
| thinking job 已完成，只需保存、对齐或交接 shared decisions 及其状态 | STRUCTURE-only | `references/structure.md` |

Source, carrier, domain, lifecycle phase, and task size are never routing keys. A request from a product manager and a self-initiated refactor use the same gate; a sentence, document, repository, folder, or conversation is only a starting point.

Important distinctions:

- For an explicit invocation or a request to explore, discuss, or find omissions, examine the relevant assumptions and outcome boundaries before deciding that the request is clear. Technical feasibility alone does not establish that the proposed result matches the user's intent. If the examination finds no consequential issue, briefly report its basis and finish within the requested scope; do not manufacture questions.
- If the user wants only inspectable facts, current state, feasibility evidence, or root cause, investigate and answer that factual request. Enter sensemaking if the evidence reveals unresolved direction, human-owned choice, or a material validity problem. When the user also asks to discuss the idea, bring those facts back into the discussion.
- For execution requests without a request for exploration or critique, skip sensemaking when the outcome and consequential commitments are clear and no material defect is visible. Agent-owned local and reversible implementation choices do not become clarification questions merely because alternatives exist.
- A decision-complete request may still be unsound. Enter Challenge only when the user asks for it or a material defect is already visible; do not turn every clear request into mandatory review.
- A user who lacks the knowledge to choose does not need a better multiple-choice question first. Teach, research, show references, or prototype before asking.
- A vague preference and a missing fact are different: show concrete alternatives for the former; look up the latter.

## 3. WORK — follow the active mode

Read and apply only the active mode reference. If a later answer changes the uncertainty type, say what changed, load the new reference, and transition cleanly.

Across all modes:

1. **Make your reasoning attackable.** Separate observed facts, causal hypotheses, and user choices. Present findings concretely enough to reject; state what evidence is missing before claiming a cause or guarantee.
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

“继续”, “go on”, and similar continuations inherit the current activity: continue discussing, investigating, or executing as appropriate. An answer confirms only the choices it addresses; it does not ratify all recommendations or authorize a different activity.

When the user requests implementation, or earlier authorization already covers it, stop optional excavation and return control downstream once the relevant decisions are resolved or delegated. Preserve remaining assumptions and deferred items. An unresolved consequential decision the user must own still needs an answer; do not reopen settled decisions or request the same authorization again.

## 6. HANDOFF — pass state, not a pipeline

Sensemaking has no mandatory successor. When another agent, tool, or later session will continue, pass the smallest useful handoff:

- the accepted direction or decision state;
- consequential `assumed`, `deferred`, and `risk` items;
- boundaries and success evidence that downstream work must preserve.

Use the Handoff Snapshot in `references/structure.md` only when this state would otherwise be lost. The downstream consumer chooses its next action from the actual remaining need: gather evidence, prototype, deliver directly with proportionate verification, design, plan coordination, request domain review, or stop. Task size alone never selects that route, and none of these actions is an automatic consequence of sensemaking.

## Reviewer policy

Default to inline, domain-aware challenge. An independent reviewer is an escalation for explicit user request, high stakes, or a genuinely valuable independent perspective. Select it by domain; never route a non-software task to Software Architect, and never make any reviewer a mandatory consequence of sensemaking.
