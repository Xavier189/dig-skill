# Challenge — Stress-Test Proposals and Decisions

Use Challenge when the user explicitly asks for critique, review, grilling, stress-testing, or design validation, or when an already-visible material defect makes silent execution unsound.

The same starting point may contain both missing owner decisions and visible defects. Use Clarify for the former and Challenge for contradictions, invalid assumptions, untestable claims, or unsafe boundaries. Source, format, domain, lifecycle phase, and size do not determine validity.

Challenge is not a software architecture ceremony. It applies to product ideas, policies, meetings, writing structures, operating procedures, technical designs, and any other consequential proposal.

## Start from the claim, not a questionnaire

Understand the proposal, its intended outcome, and the evidence or constraints it relies on. Read relevant sources before judging. Then lead with concrete findings; do not turn every flaw you can already explain into a question.

For a tentative idea, test its claims while clarifying the premises that would change the recommendation. Do not treat the supplied mechanism as an accepted direction. A finding supported independently of the user's preferences can be stated directly; a preferred repair that depends on an unconfirmed goal or risk tolerance should remain conditional.

Verify how an alternative differs from the current state before recommending it. Name the behavior it changes and the evidence supporting the expected benefit. Keep causal explanations provisional when source inspection shows only a plausible mechanism; guarantees require evidence for their preconditions and failure cases.

Use questions only when:

- the finding depends on the user's intent or risk tolerance;
- multiple repairs embody different values;
- an assumption cannot be verified externally;
- the user must accept an external commitment or irreversible consequence.

## Select the relevant lenses

Choose the few lenses most likely to change the conclusion. Do not print or mechanically fill this list:

- **Goal fit** — does the proposal solve the actual problem, or optimize a proxy?
- **Internal consistency** — do requirements, terms, states, or sections contradict one another?
- **Assumptions and evidence** — what must be true, and what supports it?
- **Boundaries and negative cases** — what is explicitly excluded; what happens at limits?
- **Failure and recovery** — how does it fail, who notices, and can it recover safely?
- **Stakeholders and incentives** — who benefits, pays, operates, approves, or can undermine it?
- **Terminology and domain model** — are important terms vague, overloaded, or inconsistent with reality?
- **Success and testability** — could two reasonable people agree whether it worked?
- **Reversibility and option value** — what is costly to undo; what experiment could buy information cheaply?
- **Alternatives** — is there a simpler framing or a materially different approach worth comparing?

Apply named methods only when they sharpen the relevant lens:

- pre-mortem for plausible failure paths;
- inversion for hidden enabling conditions;
- counterexample for universal claims and boundary rules;
- first principles for inherited assumptions;
- stakeholder mapping for conflicting incentives;
- prototype or simulation for behavior the user must see to judge.

## Finding format

For each material finding, provide:

1. **Finding** — the precise defect, blind spot, or tension.
2. **Basis** — evidence, contradiction, counterexample, or explicit inference.
3. **Consequence** — what fails or changes if it remains.
4. **Recommendation** — the smallest effective correction or experiment.
5. **Owner decision** — only when the user must choose a trade-off.

Use severity sparingly:

- `blocking` — proceeding would contradict the goal, violate a hard constraint, or create an unacceptable irreversible risk;
- `material` — likely to cause rework, failure, or a different outcome;
- `watch` — worth recording but not worth delaying work.

Do not mistake stylistic preference for a defect. Do not overstate an inference as fact; label it and say what evidence would resolve it.

## Adversarial pass without adversarial tone

Attack the proposal, not the user. Preserve good choices and explain why they survive. A useful review identifies strengths, not only flaws, because retained strengths constrain the repair.

When proposing alternatives, compare what each optimizes and sacrifices. Do not replace the user's design with the agent's preferred design without exposing the trade-off.

## Completion

Challenge completes when each material finding is:

- corrected;
- rejected with rationale;
- converted into an owner decision;
- deferred with an explicit consequence; or
- recorded as an accepted `risk`.

Render a Challenge Report, revised Decision Brief, Requirements Brief, or proposal when useful. Do not automatically invoke a reviewer, write an implementation plan, or begin implementation.
