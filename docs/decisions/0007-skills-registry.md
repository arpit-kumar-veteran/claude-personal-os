# ADR 0007: Skills registry

## Context

As patterns emerge in working with the assistant, the temptation is to re-prompt the same instructions every time the pattern recurs. The audit, the session close, the workstation creation flow: each gets re-typed or paraphrased. The result is drift between instances of the "same" task, and the loss of institutional memory about how the task should run.

The assistant has a skills mechanism: a directory of Markdown files with frontmatter (name, description, trigger language), automatically loaded at session start. A skill triggers when the user's intent matches its description.

## Decision

Promote a recurring pattern into a registered skill once it has been run a few times and the shape is stable. Each skill is one Markdown file with frontmatter describing when to trigger and the steps to follow. A skills registry (`skills/skills-index.md`) indexes every skill with a one-line trigger description.

Skills are read end to end by the user before approval. They are not magic. The skill file is the single source of truth for how that pattern runs.

## Consequences

- Recurring tasks run the same way every time. No drift between instances.
- The skill description becomes the single source of truth for when this pattern applies. Disagreements about scope get settled by editing the description.
- The user can read every skill in the registry and know everything the assistant might do unprompted.
- The registry grows over time. Periodic pruning keeps it readable. Skills that are no longer used get archived, not silently kept.
- Cost: one file per skill, one entry in the registry, and one judgement call about when a pattern is mature enough to promote.

## Alternatives considered

- No registry, just freeform prompts each time. Rejected. Drift accumulates. The same task gets done three different ways.
- One large skill file containing all patterns. Rejected. Readability collapses past three patterns. Loses the one-skill-one-trigger boundary.
- External tooling for skill management. Rejected. Adds infrastructure for no clear gain over plain Markdown files in a folder.
- Auto-promotion of any repeated task. Rejected. The judgement call about when a pattern is stable enough to be a skill is important. Auto-promotion fills the registry with half-formed patterns.
