# Auto-Memory System

How to structure memory so it stays useful as the OS scales. This is the advanced memory architecture used in mature deployments.

## The problem this solves

A basic MEMORY.md works well for the first few months. It breaks down when:

- The file exceeds 100-150 lines and Claude starts missing entries.
- Facts, rules, contacts, and project status are all mixed together.
- Session-close keeps proposing the same stale entry that was never cleaned up.
- You cannot tell at a glance whether something is current or historical.

## The four-type model

Every memory entry belongs to one of four types. Knowing the type tells you where it lives and how long it stays.

### Type 1: User facts

What is permanently true about you or your context: background, credentials, stable preferences, long-term goals. These change rarely. They live in root MEMORY.md under Profile.

Examples: your role, your location, your experience, your communication preference.
Lifespan: months to years.

### Type 2: Feedback and patterns

How Claude has learned to work with you over time: things you corrected, patterns you reinforced, rules that emerged from sessions. These live in root CLAUDE.md as rules, or in the relevant workstation CLAUDE.md.

If an entry says "Claude tends to do X but I prefer Y," it should be a rule in CLAUDE.md, not a fact in MEMORY.md.
Lifespan: permanent once promoted to a rule.

### Type 3: Project and decision state

The current status of active work: open projects, recent decisions, in-flight conversations. These live in workstation MEMORY.md. They are the most frequently updated and the most frequently stale.

Examples: "application sent to X on date Y," "decided to pause venture A," "meeting with B scheduled."
Lifespan: until the project closes or the decision is superseded. Then move to ARCHIVE.md.

### Type 4: Reference facts

Specific facts that are not permanent but are too important to lose: a contact's preference, a vendor's pricing, a regulation that applies to a decision. These live in workstation MEMORY.md or in a resource file, depending on how often they are needed.

Lifespan: until superseded. Note the source and date so you know when to check for updates.

## The index pattern

When a workstation covers multiple people, projects, or entities, do not load all records at session start. Use an index file:

`[workstation]/resources/index.md` — lists every record with a one-line description and a file path.

At session start, Claude reads the index. It loads the specific record only when the session needs it. This keeps context efficient and prevents irrelevant data from crowding the session.

Example: health-hq covers five family members. The index lists all five with paths to their baseline files. Claude loads only the one in scope for the current session.

## The line ceiling rule

Every MEMORY.md has a hard ceiling of 150 lines. When a file approaches 150 lines:

1. Run the memory-consolidation skill.
2. Move completed projects and superseded decisions to ARCHIVE.md.
3. Promote patterns to CLAUDE.md rules.
4. Delete duplicates.

Do not raise the ceiling. Compress instead. A 150-line MEMORY.md that is precise outperforms a 400-line one that is noisy.

## When to use ARCHIVE.md vs delete

**Move to ARCHIVE.md:** decisions that were made and might be re-questioned, completed projects with lessons, inactive contacts who might re-emerge.

**Delete:** facts that are simply wrong and have been corrected, duplicate entries, noise entries that should never have been recorded.

If unsure, archive. Deletion is permanent.

## Session-close and memory quality

The session-close skill is the primary mechanism for keeping memory current. Every session that produces a new fact, decision, or status change should end with session-close. The skill extracts, proposes, and waits for approval before writing. This is the gate that keeps low-quality entries out.

The weekly audit checks for MEMORY.md files approaching the line ceiling and flags them before they overflow.
