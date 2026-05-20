# ADR 0005: No auto-write default

## Context

The temptation to let the assistant write changes "when it is sure" is constant. Each individual auto-write feels harmless. The aggregate is a loss of control over what is in the user's own files.

The assistant is also routinely wrong about confidence. What looks obvious from inside a session is often wrong in light of context the assistant does not have.

## Decision

No auto-write by default. The assistant proposes the change in chat with the exact file, the exact section, and the exact text. The user approves with a single word. Then the assistant writes.

This applies even to changes that look obviously correct. The propose-approve-write cycle is not negotiable for routine work.

One narrow exception is permitted. A workstation may declare that specific categories of factual entries (e.g., "applied to role X on date Y") can be auto-written at session close without per-edit approval. The exception is documented in that workstation's CLAUDE.md. It is bounded to objective facts in a stated format. It does not expand by precedent.

## Consequences

- Every structural change passes through human attention at least once.
- The assistant becomes a recommendation engine, not an autonomous editor.
- The user retains complete authority over what their files contain.
- The exception is a known feature, not a leak. It is small, named, and limited.
- Cost: small daily friction on routine updates. The user types "yes" several times a session.

## Alternatives considered

- Full auto-write with rollback. Rejected. Rollback is theoretical. In practice the user does not review the diff carefully enough to catch problems.
- Auto-write with a confidence threshold. Rejected. Confidence is hard to calibrate. False positives accumulate. The threshold drifts upward as the assistant gets bolder.
- Manual write only, no propose step. Rejected. Slows the work for no safety gain. The propose step is fast and gives the user a clean approval gate.
