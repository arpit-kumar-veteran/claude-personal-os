# ADR 0008: Interview-driven personalisation

## Context

Templates with placeholders are useful but only halfway there. A new cloner still has to find every placeholder, decide what to write, and remember to be consistent across files. Many give up before finishing. The drop-off is highest in the first ten minutes after clone.

The pattern that works in other domains: a structured interview that asks the user one question at a time, captures the answers, and substitutes them across the template files automatically.

## Decision

Ship a setup skill (v0.2 of this repository) that interviews the cloner with around thirty questions across six sections (identity, voice, workstations, cadence, integrations, naming). The skill captures answers in a local file (gitignored), then walks every template and substitutes each `{{REPLACE: ...}}` marker with the matching answer. Idempotent. Re-runnable. Always prints a diff before writing.

v0.1 ships without the skill. Placeholders are filled manually by following GETTING-STARTED.md. v0.2 ships next, after v0.1 feedback has shaped which questions matter.

## Consequences

- A new cloner can have a working personalised system in under an hour instead of half a day.
- Every placeholder traces to exactly one question. The system is auditable end to end.
- The interview file is itself a Markdown file. It is extendable and forkable. It is not buried inside compiled code.
- The skill never overwrites without printing a diff first. Idempotent re-runs are safe.
- Splitting into v0.1 and v0.2 lets the v0.1 release ship faster and use real feedback to shape v0.2.
- Cost: the question set has to be designed carefully. Questions that are too vague produce useless answers. Questions that are too narrow miss real diversity in how people work.

## Alternatives considered

- Auto-detect-and-replace based on heuristics. Rejected. Magic. Not auditable. Hard to debug when it gets something wrong.
- A web form that emits a YAML answers file. Rejected. Adds infrastructure. Breaks the "stay in Claude Code" simplicity that makes the system possible for non-coders.
- Skip personalisation entirely. Users edit by hand. Rejected for v0.2. Adopted as v0.1 to ship faster, with the manual flow documented in GETTING-STARTED.md.
- Ship the skill in v0.1 from the start. Rejected. Doubles the time-to-ship for v0.1. Delays public feedback. Two posts from one project beats one post from a project that took twice as long.
