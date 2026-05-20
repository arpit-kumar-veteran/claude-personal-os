# Architecture Decision Records

This folder holds the design decisions behind the operating system pattern. Each ADR is one page. Each captures four sections: Context, Decision, Consequences, Alternatives considered. The point is to make non-obvious choices visible and revisitable.

## Index

| # | Title | Summary |
|---|---|---|
| [0001](0001-two-tier-memory.md) | Two-tier memory | Root memory plus per-workstation memory. Loaded by scope. |
| [0002](0002-file-edit-guards.md) | File edit guards | No edit to governance files without explicit per-session permission. |
| [0003](0003-generic-templates-over-personal-mirror.md) | Generic templates over personal mirror | Publish the pattern, not a sanitised personal copy. |
| [0004](0004-scheduled-audit-cadence.md) | Scheduled audit cadence | Weekly compliance check runs automatically. |
| [0005](0005-no-auto-write-default.md) | No auto-write default | Assistant proposes, user approves, then assistant writes. |
| [0006](0006-single-repo-not-per-workstation.md) | Single repo, not per workstation | One root for cross-cutting concerns. Workstations are folders. |
| [0007](0007-skills-registry.md) | Skills registry | Recurring patterns become Markdown skills indexed in a registry. |
| [0008](0008-interview-driven-personalisation.md) | Interview-driven personalisation | A setup skill interviews the cloner and fills placeholders. |

## Why ADRs

Personal AI systems are full of small choices that look obvious in hindsight and were not at the time. Recording the reasoning behind each one means three things.

A future session, or a fork, understands not just the rule but the reason. The rule alone is brittle. The reasoning lets a fork judge whether the rule still applies in new circumstances.

Decisions can be revisited deliberately. If circumstances change, find the ADR, weigh the new context against the old, decide consciously rather than by drift.

The set of ADRs is itself a portfolio of design thinking. It is the part of the system most worth reading first.

## How to add an ADR

- Number sequentially. No deletions. If a decision is reversed, write a new ADR that supersedes it and link both ways.
- One page maximum. If it does not fit on one page, it is two decisions.
- Four sections, always in this order: Context, Decision, Consequences, Alternatives considered.
- Plain language. No marketing words. No motivational closers.
- Add a row to the index above.
