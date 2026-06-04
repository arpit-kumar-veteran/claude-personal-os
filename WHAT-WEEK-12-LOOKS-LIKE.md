# What Week 12 Looks Like

Three months in. Here is what a mature deployment actually looks like, and what changed to get there.

## The system

By week 12, a typical deployment has:

- 8 to 12 active workstations, each with a tight Identity and a populated MEMORY.md.
- A routing map that routes correctly on the first attempt, most of the time.
- 6 to 10 registered skills. The recurring tasks that used to need re-explanation now run consistently from the skill file.
- 2 to 4 scheduled tasks running automatically. At minimum: weekly audit and monthly close.
- An ARCHIVE.md in every workstation that had completed projects or superseded decisions.
- MEMORY.md files that stay under 150 lines because memory-consolidation runs quarterly.

The system is not impressive at week 12 because of its size. It is impressive because it stays clean.

## What a session looks like

You open the OS folder. Claude reads your CLAUDE.md and MEMORY.md. No re-orientation. No "just to remind you, I am working on..."

You say what you need. Claude routes to the right workstation. If it routes wrong, you know your routing map needs tightening — and you fix it in five minutes instead of wondering why Claude keeps missing context.

At the end of the session, you say "run session-close." Claude produces three to five memory proposals. You approve two, decline one, and close. Total time: four minutes.

On Fridays, the audit runs automatically. You review the report on Monday morning. Most weeks: zero CRITICAL, two or three WARNING, a handful of INFO. You fix the warnings in 20 minutes.

## What changed between week 1 and week 12

**Week 1:** One workstation. Rough MEMORY.md. The routing map has two rows. You are still re-explaining context in some sessions.

**Week 4:** Three workstations. Memory is growing but still readable. You have run session-close five or six times and the habit is forming. The audit caught two routing map mismatches you had not noticed.

**Week 8:** Six workstations. The first MEMORY.md hit 120 lines. You ran memory-consolidation and it came down to 80. Two skills are registered. One scheduled task is running. You stopped re-explaining yourself in sessions weeks ago.

**Week 12:** The system runs. You spend your time on decisions, not on housekeeping. The OS is a background system, not a project.

## What did not work for some users

Some deployments stalled between week 4 and week 8. The common causes:

**Too many workstations too fast.** Adding workstations speculatively before the first ones were stable. The fix: no new workstation until the existing ones route correctly and have at least one month of real sessions.

**Skipping session-close.** The memory stopped growing. Sessions started feeling stateless again. The fix: make session-close non-optional. It takes four minutes. There is no good reason to skip it.

**MEMORY.md that never got consolidated.** Files grew past 150 lines. Claude started missing entries. The fix: run memory-consolidation. It is faster than the drift it prevents.

**Voice principles that were never written.** The humanizer and voice-check skills had nothing to check against. Content still sounded generic. The fix: write three to five concrete voice rules, even rough ones. Rough rules outperform no rules.

## The compound effect

The system gets easier to maintain as it matures, not harder. That is the design. Each week of clean session-close builds a MEMORY.md that requires less consolidation later. Each skill registered reduces the variance in how recurring tasks run. Each audit cycle catches drift before it compounds.

At week 12, you are not managing the system. The system is managing itself. You approve or decline what it surfaces.

That is what done looks like.
