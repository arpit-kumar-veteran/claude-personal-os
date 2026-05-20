# ADR 0004: Scheduled audit cadence

## Context

Governance rules only matter if they are enforced. Self-enforcement decays. Without a scheduled check, the structure drifts until something visibly breaks. By then the gap has been growing for weeks.

The user is unlikely to run an audit on their own schedule. They get busy. They forget. The system needs to remind itself.

## Decision

Run an automated audit on a fixed cadence. Weekly is the default. The audit walks the entire operating system tree, produces a categorised report (CRITICAL, WARNING, INFO), and proposes fixes. It writes nothing on its own.

The audit is implemented as a skill (`audit-system.skill.md`). The cadence is implemented as a scheduled task that triggers the skill.

## Consequences

- Drift surfaces within seven days rather than at the next observed failure.
- The audit report doubles as a status digest. The user sees what is healthy and what needs attention in one place each week.
- Compliance is measured in numbers, not in vibes. "Three CRITICAL, two WARNING, twelve INFO" is something a user can act on.
- The audit must stay fast and read-only. If it becomes slow or writes files, users will disable it. The discipline of "report only, never modify" is load-bearing.
- Cost: a scheduled task to maintain, and the user discipline to read the report. If the report is ignored for several cycles, the audit loses value.

## Alternatives considered

- Audit on every session close. Rejected. Too noisy. Reduces signal. Most session closes do not change the system structure.
- Audit only on demand. Rejected. The user forgets. Drift wins by default.
- Continuous lint hooks on every edit. Rejected. Slows the work. Blocks legitimate ad-hoc changes that the user is mid-way through.
- Daily audit. Considered, then rejected. Most weeks have no structural change. Daily reports become routine and the user stops reading them.
