# Scheduled Task: Monthly Close

## Task definition

```
TASK NAME: Monthly: OS close
SCHEDULE: 0 10 1 * *   (1st of every month at 10:00)
DESCRIPTION: Monthly health check across all workstations. Runs audit, checks MEMORY.md line counts, flags any workstation that needs consolidation or archiving, proposes CHANGELOG updates. Does not write without approval.
READS: All CLAUDE.md and MEMORY.md files, skills-index.md, any live dashboard or tracking files
PRODUCES: Monthly summary report with proposed actions
MODEL: sonnet
```

## Task prompt

Paste this as the scheduled task's instruction:

---

Run the monthly OS close.

Follow these steps:

1. Run the full audit-system skill. Report CRITICAL and WARNING findings with proposed fixes.
2. Check every MEMORY.md for line count. Flag any file over 120 lines (approaching the 150-line ceiling) as a consolidation candidate.
3. Check every workstation for stale entries: projects that completed, contacts that are no longer relevant, decisions that were superseded. List them by workstation.
4. Check skills-index.md: does every skill listed have a corresponding file on disk? Flag any mismatch.
5. Check the routing map: does every row have a matching folder? Does every folder have a routing map row? Flag mismatches.
6. Produce a monthly summary:
   - Audit findings: CRITICAL count, WARNING count, INFO count.
   - MEMORY.md files approaching ceiling: list with line counts.
   - Stale entries flagged: count by workstation.
   - Skills index: any mismatches.
   - Routing map: any mismatches.
7. For each finding, propose the exact action. Do not write anything. Present and wait for approval.

This is a read-only run. All changes require explicit approval.

---

## Setup instructions

**Claude Cowork:** Name the task "Monthly: OS close". Set the schedule to `0 10 1 * *`. Paste the prompt above.

**Manual fallback:** First of every month, paste the prompt into your OS session.

## Stacking note

This task runs on the 1st at 10:00. If you have other monthly tasks, stack them at 11:00 and 12:00. Do not stack more than three monthly tasks on the same day.
