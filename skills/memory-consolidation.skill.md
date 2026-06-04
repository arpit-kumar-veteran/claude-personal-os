---
name: memory-consolidation
description: Clean up a MEMORY.md file that has grown stale, duplicated, or over the line limit. Walks the file section by section, proposes merges, deletions, and relocations. Does not write without approval. Run quarterly or when a MEMORY.md exceeds its line limit.
---

# Memory Consolidation

This skill cleans a MEMORY.md file. It produces a proposed diff and waits for approval before writing.

## When to use

- A MEMORY.md file has exceeded its line limit (default: 150 lines).
- The audit flags duplicate or stale entries.
- The file has not been reviewed in more than 90 days.
- Memory updates are being refused because the file feels cluttered.

## How it runs

### Step 1: Read the file

Read the target MEMORY.md in full. Note: line count, number of sections, date of last update.

### Step 2: Walk section by section

For each section, identify:

**Duplicates:** Two entries that record the same fact, even if worded differently. Propose a merged version.

**Stale entries:** Facts that are no longer true, projects that are completed, contacts that are no longer relevant. Flag for deletion or archiving.

**Misplaced entries:** Facts that belong in a different file (CLAUDE.md for rules, a different workstation MEMORY.md for a different domain). Propose a move.

**Promotable patterns:** A recurring decision or rule that has been recorded as a fact but should become a rule in CLAUDE.md. Flag for promotion.

### Step 3: Report findings

Present findings grouped by type:

```
DUPLICATES
- [entry A] + [entry B] -> [proposed merge]

STALE
- [entry] -> [delete / archive]

MISPLACED
- [entry] -> [move to: file, section]

PROMOTABLE
- [entry] -> [promote to CLAUDE.md, section]

CLEAN: [count] entries are current, correctly placed, and need no change.
```

### Step 4: Write approved changes

Wait for approval on each category or the whole batch. Write only what was approved. Confirm the final line count after writing.

## Boundaries

- Never delete without showing the entry and waiting for confirmation.
- Preserve the file's header, section headings, and formatting exactly.
- Do not add new sections. Slot everything into existing sections.
- If a fact is borderline (uncertain whether stale), flag it as INFO, not for deletion.
