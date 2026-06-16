# Skills Catalog

Skills are reusable instruction sets that Claude follows the same way every time you invoke them. Where a workstation defines *where* work happens and *what* it owns, a skill defines *how* to do a specific task consistently — the same steps, the same checks, the same output format, every time.

Skills do not replace judgment. They replace repetition.

---

## Core skills

These ten skills ship with every Personal Claude OS installation. No setup required — just say the trigger phrase.

| Skill | What it does | Best for | Invoke by saying... |
|---|---|---|---|
| **session-close** | Scans the session for uncaptured decisions, facts, and changes. Proposes exact memory writes. Waits for approval before writing anything. | Ending any working session cleanly | "close the session", "session close", "wrap up" |
| **audit-system** | Checks every CLAUDE.md, MEMORY.md, and workstation file for structural integrity, orphaned sections, and rule drift. Reports what is correct and what needs attention. | Weekly health check, after major edits | "run the audit", "audit the OS", "health check" |
| **voice-check** | Reads any written text against your voice principles. Flags tone mismatches, register errors, and phrases that do not sound like you. | Before sending an email, publishing content, or submitting any external document | "check my voice", "voice check this", "does this sound like me?" |
| **memory-consolidation** | Cleans a MEMORY.md file that has grown stale, duplicated, or over the line ceiling. Proposes merges, deletions, and archives. | When a MEMORY.md is approaching its line limit | "consolidate memory", "clean up MEMORY.md", "memory is getting long" |
| **humanizer** | Removes AI-writing tells from any text — passive voice, hedging phrases, hollow openers, robotic rhythm. Rewrites to sound natural and human-authored. | Any AI-generated draft that still sounds like it was written by a model | "humanize this", "make this sound more human", "remove the AI tells" |
| **deep-research** | Fans out across multiple search angles, fetches primary sources, adversarially verifies every major claim, and synthesises a cited report with confidence levels. | Any decision that depends on accurate external facts | "research this", "deep research on...", "verify this claim" |
| **outreach** | Drafts cold or warm outreach messages: email, LinkedIn, WhatsApp, or other channels. Adapts tone and format to the relationship and the ask. Keeps it short. One ask per message. | First contact, follow-up, or reactivating a dormant relationship | "draft an outreach to...", "write a cold email to..." |
| **workstation-create-full** | Runs a full guided interview to create a new workstation with complete, placeholder-free CLAUDE.md, MEMORY.md, and resources/ folder. No blank templates — every field is filled from your answers. | Adding a new domain to your OS at any time | "create a new workstation", "add a workstation for..." |
| **content-repurpose** | Turns one long-form piece (article, transcript, talk, report) into multiple formats — social post, thread, newsletter, short video script, summary — each rewritten for the platform, not just clipped. | After publishing or recording something worth spreading further | "repurpose this", "turn this into social posts", "extract a thread from this" |
| **scheduled-task** | Sets up a recurring automated task: weekly audit, monthly close, digest processing, or any routine that should fire on a cadence without manual prompting. | Any task you want to happen automatically on a schedule | "set up a weekly audit", "schedule this to run every Monday", "automate this task" |

---

## Community skills

Community skills extend the OS beyond the core ten. They are built and maintained by OS users and distributed separately. Install any skill by dropping its `SKILL.md` into your `skills/` folder and adding a row to `skills/skills-index.md`.

| Skill area | What it does | Technical level | Find it by searching... |
|---|---|---|---|
| **Social media** | Manages LinkedIn, Twitter/X, and Instagram workflows: voice-builder, post calendar, carousel design, analytics, hook writing, and content scripts | None | "social media skill Claude OS" |
| **UI / frontend design** | Designs, redesigns, audits, and ships frontend interfaces: landing pages, dashboards, components. Commands for audit, polish, animate, bolder/quieter | None | "impeccable skill Claude OS" or "frontend design skill" |
| **Marketing** | 40+ individual sub-skills: CRO, SEO, ad creative, cold email, competitor profiling, launch plans, lead magnets, pricing strategy, referral programs | None | "marketing skills Claude OS" |
| **AI second brain** | Builds a personal knowledge system in Obsidian: imports AI chat history, builds a linked wiki from existing notes | Minimal (Obsidian install) | "second brain skill Claude OS" |
| **Programmatic video** | Builds React-based programmatic video: product launches, portfolio animations, data-driven motion graphics. Uses Remotion framework | Technical (Node.js) | "remotion skill Claude OS" |
| **Web automation** | Automates multi-page web research, structured data extraction across many URLs, and tasks that require navigating many pages programmatically | Technical (CLI setup) | "agent browser skill Claude OS" |
| **Photo / file sort** | Sorts, organises, and deduplicates photos and videos into date-based or named folder structures | None | "photo sort skill Claude OS" |
| **Premium visual design** | Creates landing pages, portfolios, and redesigns that must not look templated or AI-generic. Applies real aesthetic judgment rather than default patterns | None | "design taste skill Claude OS" |

---

## Skills by workstation

Use this table when you first set up or add a new workstation to know which skills matter most.

| Workstation | Strongly recommended | Also worth having |
|---|---|---|
| career-hq | outreach, deep-research | humanizer, voice-check |
| brand-hq / content-hq | content-repurpose, humanizer, voice-check | social media (community) |
| finances-hq | deep-research, scheduled-task | — |
| health-hq | deep-research | — |
| consulting-hq | outreach, content-repurpose, deep-research | voice-check |
| meeting-hq | session-close | scheduled-task |
| intel-hq | deep-research, scheduled-task | — |
| thinking-hq | deep-research | — |
| learning-hq | deep-research | — |
| venture-hq | deep-research, outreach | — |
| email-hq | humanizer, voice-check | — |
| expense-hq / property-hq | scheduled-task | — |
| life-transition-hq | deep-research | — |
| relationship-hq | outreach | — |
| **Any workstation** | session-close, audit-system | memory-consolidation |

---

## Installing a skill

All ten core skills are pre-installed. For community skills:

1. Download the `SKILL.md` file for the skill you want.
2. Copy it to your `skills/` folder.
3. Add a row to `skills/skills-index.md` with the skill name, file path, and a one-line trigger description.
4. Optionally add it to `skills/skills-watchlist.md` before installing — mark it "Unevaluated" so Claude surfaces it the next time a matching task comes up.
5. Test it: say the trigger phrase and confirm Claude reads the skill file before acting.

---

## Building your own skill

If you repeat the same task five or more times the same way, it is a skill candidate.

1. Create `skills/[skill-name].skill.md`.
2. Structure: YAML frontmatter (`name`, `description`), then `When to use`, then numbered `Steps`.
3. Add a row to `skills/skills-index.md`.
4. Register only when the pattern is stable. Two or three similar executions is not enough — the steps should be settled.
