# Clarify — Resolve Material Requirement Decisions

Use Clarify when a meaningful goal exists but intent, scope, behavior, constraints, success evidence, terminology, or delegated decisions still admit materially different outcomes.

## The bar for a question

Ask only when at least two realistic answers would change the frame, deliverable, behavior, validation, or hard-to-reverse decision. If likely answers lead to the same action, do not ask.

Facts are not user questions. Inspect provided materials, code, documentation, connected sources, official sources, and history first. The user owns intent and trade-offs; the agent owns safe factual reconnaissance.

## Build an attackable working hypothesis

Present a concise hypothesis only after there is enough evidence to choose a frame:

1. **Outcome** — the change the user is trying to create, not merely the requested mechanism.
2. **Named traps** — one or two task-specific ways the current framing could fail.
3. **Current sketch** — the consequential decisions you would apply if work started now, tagged internally as `confirmed`, `assumed`, or unresolved.

If the request is a solution (“add Redis”, “make a dashboard”, “book a villa”), trace it back to the problem and test whether the solution actually serves it. Do not spend the session tuning parameters on top of an unexamined premise.

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
3. Update the structured state immediately, invalidating superseded assumptions.
4. Converge when no material follow-up remains.

A useful dependent follow-up has this shape:

> “You said writes must be visible immediately. That rules out plain TTL, so the remaining decision is invalidate-on-write versus no cache for this query.”

Do not manufacture extra rounds to appear thorough. If new forks grow as fast as they close, the request contains multiple efforts; preserve the fog, propose a split, and clarify only the first meaningful unit.

## Completion

Clarify completes when every material fork is:

- `confirmed` by the user or an authoritative constraint;
- delegated as an `assumed` default the user can see;
- explicitly `deferred`; or
- converted into a research/prototype action because it is not yet answerable.

Render a Clarity Memo or Requirements Brief only when it helps the user or downstream consumer. Confirmation applies to the shared decisions, not to a mandatory document shape.
