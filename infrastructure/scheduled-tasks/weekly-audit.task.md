# Scheduled Task: Weekly OS Audit

## Task definition

```
TASK NAME: Weekly: OS audit
SCHEDULE: 0 10 * * 5   (Friday at 10:00)
DESCRIPTION: Runs the audit-system skill across the full OS. Reports findings. Proposes fixes but does not write without approval.
READS: All CLAUDE.md and MEMORY.md files, skills-index.md, routing map
PRODUCES: CRITICAL / WARNING / INFO findings report with proposed fixes
MODEL: sonnet
```

## Task prompt

Paste this as the scheduled task's instruction:

---

Run the audit-system skill across the entire OS.

Follow these steps in order:

1. Walk every workstation folder. List every CLAUDE.md and MEMORY.md with line counts.
2. Run all compliance checks: structure (CRITICAL on failure), quality (WARNING on failure), hygiene (INFO).
3. Produce the report in three sections: CRITICAL, WARNING, INFO. Format each finding as: `[path:line] | [problem] | [suggested fix]`.
4. For every CRITICAL and WARNING finding, produce the exact proposed edit: file, section, and replacement text. Do not write anything. Present and wait for approval.
5. Check whether any MEMORY.md is approaching 150 lines. If yes, flag it as WARNING and suggest running memory-consolidation.

Do not modify any file. This is a read-only audit. All fixes require explicit approval.

---

## Setup instructions

**Claude Cowork:** Open the scheduling panel. Name the task "Weekly: OS audit". Set the cron schedule to `0 10 * * 5`. Paste the task prompt above as the task instruction. Save.

**Claude Code:** Add the task definition to your scheduled tasks configuration. The prompt above becomes the task's instruction field.

**Manual fallback:** Set a calendar reminder every Friday at 10:00 with the subject "Run OS audit." Paste the prompt above into your OS session and run it.

## Stacking note

This task runs Friday at 10:00. If you have other Friday tasks, stack them at 11:00, 12:00, 13:00 to avoid overlap.
