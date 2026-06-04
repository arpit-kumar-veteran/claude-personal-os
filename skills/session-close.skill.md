---
name: session-close
description: End a working session cleanly. Scans the conversation for uncaptured changes, decisions, and new context. Proposes exact writes to the right files. Waits for approval. Writes approved items. Emits a compact session log. Use whenever wrapping up a session that touched any workstation, made decisions, or produced outputs.
---

# Session Close

This skill closes a working session cleanly. It does not write anything without approval.

## When to use

- Ending any session that touched a workstation file.
- After making a decision worth recording.
- After completing a task that produced outputs.
- On a recurring cadence: run this at the end of every working session as a habit.

## How it runs

### Step 1: Scan the conversation

Read back through this session. Identify:

- Files created, edited, or deleted.
- Decisions made (and the reasoning, if stated).
- New contacts or entities introduced.
- Facts, conditions, or statuses that changed.
- Rules or patterns that emerged and are worth keeping.
- Open threads: things started but not finished, questions not answered.

Do not summarise. Extract specifics.

### Step 2: Propose memory updates

For each item worth recording, state:

- The target file (exact path).
- The target section (exact heading).
- The proposed text (exact wording, ready to paste).

Format:

```
FILE: [path]
SECTION: [heading]
ADD: [exact text]
```

Do not write anything yet. Present the full list and wait for a single-word approval or line-by-line review.

### Step 3: Write approved items

Write only what was approved, exactly as proposed. Confirm each write with the file and section name.

### Step 4: Emit session log

Print a compact log:

```
Session close: [date]
Files touched: [list]
Memory updates: [count written / count proposed]
Open threads: [one line each]
```

Done. The session is closed.

## Boundaries

- Never write to CLAUDE.md or MEMORY.md without explicit approval.
- Never modify a file that was not touched in this session unless the user asks.
- If nothing needs recording, confirm explicitly: "No updates required. Files are current."
- Open threads are informational only. Do not create tasks or reminders without being asked.
