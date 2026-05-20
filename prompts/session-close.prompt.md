# Prompt: Session close

**Use this when:** you are wrapping a working session and want a structured close-out: checksum of changes, proposed memory updates, open threads carried forward, and any patterns worth promoting to rules or skills.

## Prompt

Wrap this session. Produce four blocks in this order.

### 1. CHECKSUM

List every file you edited, deleted, created, or moved during this session. For each, one sentence describing what changed and why. If no files were touched, write "No file changes." Do not list files you only read.

### 2. PROPOSED MEMORY UPDATES

For each workstation touched in this session, propose the exact text to add or update in its MEMORY.md. State:

- The file path.
- The section (Contacts or Key Decisions).
- The proposed line, ready to paste.

If a workstation was discussed but does not need an update, say "[workstation-name]: current." If no workstation was touched, say "No memory updates needed."

Do not write to any MEMORY.md. Surface the proposals and wait for a single-word approval.

### 3. OPEN THREADS

List anything left unresolved that a future session should pick up. One bullet per thread. Each bullet states:

- What is open.
- Why it stopped here (waiting on input, blocked, deferred by choice, etc.).
- What the concrete next step would be.

If nothing is open, write "All threads closed."

### 4. RULE OR PATTERN CANDIDATES

If anything that happened this session looked like a reusable pattern: a rule that belongs in CLAUDE.md, a skill, a template, a prompt: surface it. One bullet per candidate. Phrase it as a proposal, not a write.

If nothing emerged, write "No new patterns surfaced."

### Final

After the four blocks, ask whether to write the approved memory updates. Wait. Do not auto-write.

## How to customise

- If you have an auto-write exception for certain MEMORY.md files (e.g., a job-tracking workstation where factual entries can land without approval), say so in this prompt and the close-out will respect it.
- Add a fifth block if you want: for example, "PUBLISH" for content drafts that are ready to send. Keep the structure tight; do not add blocks for their own sake.
