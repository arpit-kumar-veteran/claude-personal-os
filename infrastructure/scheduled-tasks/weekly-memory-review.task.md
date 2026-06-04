# Scheduled Task: Weekly Memory Review

## Task definition

```
TASK NAME: Weekly: memory review
SCHEDULE: 0 11 * * 5   (Friday at 11:00)
DESCRIPTION: Scans recent sessions for uncaptured facts, decisions, and patterns. Proposes MEMORY.md updates across active workstations. Does not write without approval.
READS: All active workstation MEMORY.md files, recent session context
PRODUCES: Proposed memory updates, grouped by workstation
MODEL: sonnet
```

## Task prompt

Paste this as the scheduled task's instruction:

---

Run a weekly memory review across all active workstations.

Follow these steps:

1. Read root MEMORY.md and all workstation MEMORY.md files. Note the last-updated date on each.
2. For any workstation whose MEMORY.md has not been updated in more than 14 days, flag it as potentially stale.
3. Identify facts, decisions, or status changes from the past week that should be captured but are not yet in any MEMORY.md. Sources: any session context available, any files touched recently.
4. For each proposed update: state the target file, the target section, and the exact proposed text. Format:
   ```
   FILE: [path]
   SECTION: [heading]
   ADD: [exact text]
   ```
5. Present all proposals. Do not write anything. Wait for approval on each.
6. After approval: write only the approved entries. Confirm each write with the file and section name.

Do not delete any existing entry. Do not rewrite existing entries unless explicitly asked.

---

## Setup instructions

**Claude Cowork:** Name the task "Weekly: memory review". Set the schedule to `0 11 * * 5`. Paste the prompt above as the task instruction.

**Manual fallback:** Friday at 11:00, paste the prompt into your OS session and run it.

## Stacking note

This task runs Friday at 11:00, after the OS audit at 10:00. If the audit surfaces issues that affect memory, handle the audit first, then run this review.
