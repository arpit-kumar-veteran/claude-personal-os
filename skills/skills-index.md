# Skills Index

A registry of every skill available in this OS. Before starting any task, check here. If a matching skill exists, use it rather than improvising.

For full descriptions of each skill, when to use it, and how to invoke it, see [SKILLS-CATALOG.md](SKILLS-CATALOG.md). For community skills not yet installed, see [skills-watchlist.md](skills-watchlist.md).

## How to use

Say: "Use the [skill-name] skill." Or say what you want to do in plain language and Claude will match it to the right skill.

## Available skills

| Skill | File | Use when... |
|---|---|---|
| audit-system | `skills/audit-system.skill.md` | Running a compliance check, health check, or post-change verification of the entire OS |
| session-close | `skills/session-close.skill.md` | Ending a working session: capturing changes, proposing memory updates, logging open threads |
| voice-check | `skills/voice-check.skill.md` | Checking any written content against your voice principles before sending or publishing |
| memory-consolidation | `skills/memory-consolidation.skill.md` | Cleaning up a MEMORY.md file that has grown stale, duplicated, or over the line limit |
| humanizer | `skills/humanizer.skill.md` | Removing AI-writing tells from any text to make it sound natural and human-authored |
| scheduled-task | `skills/scheduled-task.skill.md` | Setting up a recurring automated task (weekly audit, monthly review, digest processing) |
| deep-research | `skills/deep-research.skill.md` | Multi-source, adversarially verified research on any topic you will act on |
| outreach | `skills/outreach.skill.md` | Drafting cold or warm outreach messages across job search, partnerships, venture, or network |
| workstation-create-full | `skills/workstation-create-full.skill.md` | Full guided interview to create a new workstation with complete, placeholder-free files |
| content-repurpose | `skills/content-repurpose.skill.md` | Turning one long-form piece into multiple formats rewritten for each platform |

## Adding a new skill

When you identify a task you do repeatedly and want consistent execution, capture it as a skill:

1. Create a new file: `skills/[skill-name].skill.md`
2. Use the structure: frontmatter (name, description), When to use, Steps.
3. Add a row to this index.
4. Confirm with the user before writing.

Skills should be registered only when the pattern is stable. A task you have done twice is not yet a skill candidate. A task you have done five or more times the same way is.
