# Clarify — Resolve Consequential Decisions

Use Clarify when a meaningful outcome exists but intent, scope, resulting behavior, constraints, success evidence, terminology, or delegated decisions still admit materially different outcomes.

## Starting points do not select the mode

A sentence, document, proposed refactor, deployment request, folder, existing system, or conversation is a starting point, not evidence of clarity. Its source, format, domain, lifecycle phase, and size do not trigger or skip Clarify.

First inspect the relevant current state, materials, conventions, code or files, and authoritative sources. Let established facts and safe inherited defaults resolve agent-owned details. Surface remaining choices whose realistic answers would change the outcome, scope, validation, risk, or external commitments. A low-risk or easy implementation can still encode a user preference worth exploring when the user asks to find omissions; do not equate ease of implementation with clarity of intent.

If the starting point contains a visible contradiction, false assumption, or consequential defect, state the finding through Challenge instead of disguising it as a clarification question. Continue Clarify only for the owner decisions that remain after the defect is exposed.

## Evidence gate before a working hypothesis

Before prescribing a frame or asking for a commitment, test whether current-state evidence could materially change the diagnosis or option set. If it could, inspect that evidence first. When it is unavailable, name and request the smallest source pointer, then keep any dependent frame `candidate`; do not turn a reported symptom into an assumed cause or target design.

Examples of such evidence include recent change paths, actual wait stages, frequency and severity distributions, current exceptions, usage traces, and authoritative constraints. The list is illustrative: request only evidence with enough information value to change the next decision.

Once the evidence supports a useful question or assessment, return to the discussion. State the relevant finding and its limit, then expose the choice it creates. Further investigation can follow the answer; a complete source tour is not a prerequisite for an owner decision.

## The bar for a question

Ask only when at least two realistic answers would change the frame, deliverable, resulting behavior, validation, or hard-to-reverse decision. If likely answers lead to the same action, do not ask.

Facts are not user questions. Inspect provided materials, code, documentation, connected sources, official sources, and history first. The user owns intent and trade-offs; the agent owns safe factual reconnaissance.

When the relevant evidence is not accessible, request the smallest pointer or source that would make it inspectable: a repository path, document, metric view, example record, or responsible source. Do not ask the user to manually reconstruct code paths, file inventories, current metrics, or process facts that an agent could inspect from such a source. Lived experience that is not encoded anywhere may still require user input; label it as experience, not verified current state.

## Build an attackable working hypothesis

Present a concise hypothesis only after there is enough evidence to choose a frame:

1. **Outcome** — the change the user is trying to create, not merely the requested mechanism.
2. **Named traps** — one or two task-specific ways the current framing could fail.
3. **Current sketch** — the consequential decisions you would apply if work started now, tagged internally as `confirmed`, `assumed`, or unresolved.

If the request is a solution (“add Redis”, “make a dashboard”, “book a villa”), trace it back to the problem and test whether the solution actually serves it. Do not spend the session tuning parameters on top of an unexamined premise.

Before favoring a solution, identify any unconfirmed goal or trade-off that would reverse the recommendation. Explain options conditionally until that premise is settled. Current behavior is evidence about the starting point, not proof of the behavior the user wants next.

Keep the hypothesis compact and easy to reject. A sentence that would survive unchanged in an unrelated task is filler.

## Find the material forks

Stress-test the hypothesis adaptively:

- desired outcome and stakeholder;
- scope and explicit exclusions;
- observable success evidence;
- failure modes and negative requirements;
- dependencies and constraints;
- terminology or domain boundaries;
- long-term fit and reversibility.

These are lenses, not required headings. Surface only what could reroute the result.

Pay attention to familiar words whose meaning may change: “success”, “complete”, “active”, or “available” can refer to different stages or audiences. Explain the observable difference before treating a technical change as behavior-preserving.

## Ask with dependency awareness

For independent forks, ask 2–4 concrete questions together, ordered by impact. For a dependency chain, ask the parent decision alone and let its answer determine the next question.

Each question should make three things clear:

- what part of the working hypothesis it tests;
- how realistic answers would change the outcome;
- the recommended default and why, when the user has enough basis to evaluate it.

If only the recommendation changes based on another independent answer, keep both in the batch and make the recommendation conditional. If the question's existence or option set changes, defer it to the next turn.

For taste, wording, naming, interaction, or other recognition-based choices, show 2–4 concrete alternatives rather than asking the user to invent a description.

## Follow the answer, not a checklist

After each answer set:

1. State only the delta in the shared model.
2. Admit a follow-up only when the new answer exposed it; name the answer and the fork it opened.
3. Update only the decisions the answer addresses, invalidating superseded assumptions and leaving unanswered recommendations provisional.
4. Converge when no material follow-up remains.

A useful dependent follow-up has this shape:

> “You said writes must be visible immediately. That rules out plain TTL, so the remaining decision is invalidate-on-write versus no cache for this query.”

Do not manufacture extra rounds to appear thorough. If new forks grow as fast as they close, the request contains multiple efforts; preserve the fog, propose a split, and clarify only the first meaningful unit.

For example, a user asks: “列表加个导出按钮，帮我看看有没有遗漏。” After checking the existing filters, ask whether export means the current filtered results or all accessible records, explaining how the outputs differ. If they choose filtered results, keep any unanswered format or size-limit recommendation provisional. “继续” continues that discussion; it does not authorize adding the button. If the user already asked to implement after resolving these choices, honor that authorization when the choices are settled.

## Completion

Clarify completes when every material fork is:

- `confirmed` by the user or an authoritative constraint;
- delegated as an `assumed` default the user can see;
- explicitly `deferred`; or
- converted into a research/prototype action because it is not yet answerable.

Render a Clarity Memo, Decision Brief, or Requirements Brief only when it helps the user or downstream consumer. Confirmation applies to the shared decisions, not to a mandatory document shape.
