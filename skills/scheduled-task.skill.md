---
name: scheduled-task
description: Set up a recurring automated task inside the OS. Covers weekly audits, monthly reviews, digest processing, and any pattern that should run on a fixed cadence without manual prompting. Produces a task definition file and integration instructions.
---

# Scheduled Task

This skill designs and registers a recurring automated task. It does not run the task; it documents how to configure it.

## When to use

- You want something to happen every week (audit, review, digest check) without manually triggering it.
- You want a monthly summary or close to run automatically.
- You are setting up a new workstation that has a regular cadence.

## How it runs

### Step 1: Gather requirements

Ask (one at a time if not already stated):

1. What should this task do? One sentence.
2. How often should it run? Weekly, monthly, or custom.
3. What day and time? (Suggest: weekly on Friday at 10:00 for retrospective tasks; Monday at 08:00 for forward-looking tasks.)
4. What files does it need to read?
5. What should it produce or propose?

### Step 2: Define the task

Produce a task definition block:

```
TASK NAME: [short-label]
SCHEDULE: [cron expression, e.g. "0 10 * * 5" for Friday 10:00]
DESCRIPTION: [one sentence]
READS: [list of files or folders]
PRODUCES: [what the task outputs: a report, memory proposals, a summary]
MODEL: [default: sonnet]
```

### Step 3: Write the task prompt

Produce a concise task prompt: the exact instruction the scheduled agent will follow each time it runs. This prompt lives in the task definition.

### Step 4: Integration instructions

Tell the user how to register this task in their Claude environment:

- **Claude Cowork / Claude Code:** Paste the task prompt into the scheduling interface. Set the cron schedule. Name the task using the convention: "Weekly: [label]" or "Monthly: [label]".
- **Manual fallback:** If automated scheduling is not available, create a calendar reminder at the scheduled time with the task prompt ready to paste.

### Step 5: Stacking check

Before confirming the schedule, check whether any existing task already runs at the proposed time. If so, suggest an adjacent slot to avoid overlap.

## Stacking defaults

Use these time slots when setting defaults:

- Retrospective weekly tasks (audits, hygiene scans): Friday at 10:00, 11:00, 12:00, 13:00. No two tasks at the same hour.
- Forward-looking weekly tasks (planning, briefs): Monday at 07:00, 08:00, 09:00.
- Monthly tasks: 1st of the month at 10:00, 11:00, 12:00.

## Boundaries

- Produce the definition and prompt. Do not configure the scheduler directly unless the user asks.
- Never schedule a task that writes to CLAUDE.md or MEMORY.md without a confirmation step inside the task prompt itself.
- If the user has not defined what the task should produce, ask before proceeding.
