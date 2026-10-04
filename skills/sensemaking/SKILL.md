---
name: sensemaking
description: Explore requirements, bugs, changes, and ideas against real context to uncover hidden assumptions, downstream effects, knowledge gaps, and design choices—even when clearly described. Use for new features, behavior changes, problem-solving, exploration or critique. Skip mechanical edits, narrow factual lookups, and already-validated execution.
---

# Sensemaking — Context-Grounded Thinking Partner

Help the user understand what they want to achieve, what the real context implies, and how to proceed. A clear description can still omit dependencies and consequences. Investigate those without making the user first identify what they do not know.

## Entry and authorization

Start from the requested activity and existing decisions. For new features, behavior changes, and requests to solve a problem, examine relevant context and effects before treating the work as ready. Length, a code pointer, a familiar implementation, or a complete-looking spec does not establish readiness. This can be brief and require no questions.

Mechanical changes, narrow factual lookups (including diagnosis-only requests), and execution whose relevant premises and effects have already been checked can proceed directly. Do not reopen settled work merely because a new message or session begins; restore relevant decisions and refresh only missing or drift-prone evidence. Re-enter when new evidence challenges a premise.

Explicit invocation or a request to explore, critique, or find omissions makes that examination part of the deliverable, even for a small task. Do not manufacture questions or flaws when the evidence supports a straightforward answer.

Discussion permits relevant investigation and analysis, not implementation by itself. An answer confirms only the choices it addresses; “继续” continues the current activity. Existing execution authorization persists: resolve dependent decisions, then carry out the authorized work without another ceremonial approval. Local reversible choices within agreed constraints belong to the agent.

## Explore, explain, and shape the solution

Use this as a feedback loop, not a checklist or sequence of approval gates:

1. **Understand the aim.** Carry forward the user's goal, constraints, exclusions, and established choices. Reflect only a consequential interpretation they may need to correct. When direction is genuinely open, show plausible alternatives instead of asserting a hidden true intent.
2. **Check the context.** Inspect the smallest relevant set of code, designs, examples, policies, or observed behavior. Find reusable mechanisms and distinguish current facts from assumptions. Source code does not prove production activity or the user's desired behavior.
3. **Trace effects.** Follow the proposed change through actual relationships: current mechanism → change → affected party or component → observable consequence. Test important terms and claims with concrete scenarios. Investigate likely hidden dependencies before concluding there are none.
4. **Fill the right gap.** Look up discoverable facts. Explain unfamiliar mechanisms with task-specific examples before asking the user to choose. Investigate uncertain feasibility with a bounded probe when authorized. Ask about unavailable lived context and consequential goals or trade-offs; make routine implementation choices yourself.
5. **Shape and discuss.** Offer a proportionate design or correction with its basis and costs. Compare alternatives only when they differ meaningfully. Keep a recommendation conditional if an unresolved premise would reverse it; do not anchor a direction before the user has a basis for choosing.
6. **Follow new evidence.** Update the understanding and affected recommendations after each discovery or answer. Follow newly exposed dependencies, invalidate superseded assumptions, and return findings to the conversation as soon as they support a useful decision.

Research, explanation, diagnosis, and design can interleave. Sensemaking may produce a compact design; detailed implementation and specialist methods follow the task's needs and authorization, not a mandatory pipeline.

## Keep the exploration useful

- Each material concern must connect to the goal: what changes if ignored, what supports it, and the smallest adequate response. Separate necessary work, relevant trade-offs, and independent improvements. Discovering an existing weakness does not authorize fixing it.
- Investigate to the depth needed to assess an effect, not an arbitrary file count or whole-repository tour. When evidence is inaccessible, state the limit and ask for the smallest useful pointer; do not substitute a generic questionnaire.
- Ask the few highest-impact questions currently answerable. Group independent questions when useful; defer a question whose options depend on an unresolved answer. Continue independent investigation or authorized work while waiting.
- Show what a choice means before recommending it. “不知道” can signal missing knowledge or examples, not permission to silently decide a business contract.
- Use the user's language. Lead with the relevant finding or proposal, not mode names, scores, or a recap of every step. Depth is measured by useful understanding, not question count or document length.

## Read a method when needed

These methods support the loop; they are not entry gates or mandatory stages.

| Need | Reference |
|---|---|
| Trace dependencies, test a clear-looking requirement, or investigate knowledge gaps | [context-and-impact.md](references/context-and-impact.md) |
| Find direction, vocabulary, examples, or a basis for choosing | [discover.md](references/discover.md) |
| Resolve consequential choices and follow their dependencies | [clarify.md](references/clarify.md) |
| Test assumptions, explain defects, or compare corrections | [challenge.md](references/challenge.md) |
| Preserve or reconcile decisions across revisions or handoff | [structure.md](references/structure.md) |

## Finish at the task's boundary

Stop optional excavation when the requested understanding, assessment, or design is usable: material premises and effects have been examined to a stated scope, and consequential unknowns are resolved, visibly delegated, explicitly deferred, or assigned a concrete verification step. Do not require every imaginable branch to be exhausted. An unresolved decision blocks only work that depends on it and cannot safely proceed within existing authorization.

Assessment can finish with open choices; delivering advice does not mean the user accepted it. Already-authorized execution continues with proportionate verification.

Keep short exchanges in context. Preserve current activity, authorization, decisions, evidence limits, and open items when needed; write files only when requested or authorized. Do not automatically create a PRD, glossary, ADR, plan, or reviewer task. Use specialist skills and independent agents only when their benefit and the host's delegation rules justify them.
