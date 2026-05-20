# ADR 0002: File edit guards

## Context

An assistant given write access to its own governance files can drift. Small unrequested edits accumulate. Heading levels change. Sections get renamed. Bullets become numbered lists. After a few weeks the structure no longer matches what other parts of the system expect.

The drift is hardest to spot because each individual edit looks reasonable. Only the aggregate is wrong.

## Decision

No edit to any CLAUDE.md or MEMORY.md without explicit per-session permission. The assistant proposes the exact file, the exact section, and the exact text in chat. The user approves with a single word. Then the assistant writes.

This applies uniformly. Not just for major changes. Not just for new sections. Every edit, including a one-line fact added to a Memory Log, passes through the propose-approve cycle.

Section structure is immutable. Heading levels, table column structure, bullet style, and meta-notes are preserved on every edit. The assistant does not normalise or reformat.

## Consequences

- All structural changes are visible to the user before they happen.
- The assistant cannot quietly modify its own constraints.
- Drift is reduced to near zero. What is in the file is what the user explicitly approved.
- Slight friction on small edits is accepted as the cost of structural integrity.
- The user becomes the audit trail. The chat log shows what was approved and when.

## Alternatives considered

- Auto-write with diff. Rejected. Diffs are easy to miss in a long conversation. Drift accumulates anyway.
- Block all writes. Rejected. File edits are the point of having governance files. Blocking them defeats the purpose.
- Targeted auto-write for well-defined categories. Adopted later as a narrow exception for one workstation's factual entries. See ADR 0005. The exception is bounded and documented; it does not expand by precedent.
