# Prompt: Consolidate memory

**Use this when:** a MEMORY.md file has accumulated entries over weeks or months and may contain duplication, stale facts, or drift. Run this periodically: quarterly is a reasonable default.

## Prompt

Consolidate the memory file at: `[PATH/TO/MEMORY.md]`

Walk through it section by section. For each section, produce four lists.

### 1. DUPLICATES

Entries that say the same thing in different words, or two entries that should be merged into one. Group them and propose a single merged entry. Quote the originals so the source is visible.

### 2. STALE

Entries that are likely no longer true:

- Dates that have passed without a follow-up.
- Decisions superseded by a later entry.
- Contacts whose status has likely changed (moved roles, projects ended).
- Project statuses that conflict with newer entries.

For each, note why it looks stale and propose either a delete or a rewrite. Do not guess: if you cannot tell whether something is stale, list it under section 3 instead.

### 3. PROMOTABLE OR MISPLACED

Entries that have outgrown the section or sit in the wrong place:

- Entries that are really rules (belong in CLAUDE.md).
- Entries that are really active projects (belong in Active Projects, not Memory Log).
- Entries that have grown into their own subdomain and should split into a new workstation.
- Entries that fit a different section in the same file.

For each, propose where it should move and quote the original.

### 4. CLEAN

Entries that are fresh, correctly placed, and worth keeping. Report a count only: do not list individually. The count is for sanity-checking that the consolidation has not lost anything.

### After review

Propose the rewritten file in full. Preserve:

- The exact header.
- Every section in its original order.
- Every formatting convention (tables, bullets, italicised meta-notes).

Do not invent new sections. Do not add a "Change Log" section. Do not summarise what you changed inside the file itself: that goes in the chat, not in MEMORY.md.

Wait for approval before writing.

## How to customise

- If your MEMORY.md has more than two sections (e.g., a separate "Open Decisions" or "Watchlist"), extend the section walk to cover them.
- For team-shared memory files, add a fifth list: "ATTRIBUTION GAPS": entries that lack who-made-the-call context.
- If you want the rewrite to be conservative, instruct it to keep anything ambiguous in the file unchanged.
