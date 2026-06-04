# Changelog

All notable changes to this pattern are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/). Version numbers follow [Semantic Versioning](https://semver.org/) loosely: major versions reflect substantial changes to the pattern, minor versions add capabilities, patch versions fix bugs in examples or documentation.

## [0.3.0] - 2026-06-04

### Added

- Nine additional workstation examples: `thinking-hq` (four structured reasoning modes), `finances-hq` (net worth, FIRE planning, source-of-truth hierarchy), `health-hq` (multi-person with index-first architecture), `consulting-hq` (freelance pipeline), `venture-hq` (startup and co-founder), `life-transition-hq` (major decisions), `intel-hq` (recurring digest processing), `relationship-hq` (personal CRM with entity mirroring), `content-hq` (content production pipeline). Brings total workstation examples to 16.
- Four additional skills: `deep-research.skill.md` (multi-source adversarial research), `outreach.skill.md` (cold and warm outreach across domains), `workstation-create-full.skill.md` (full interview-driven workstation creation), `content-repurpose.skill.md` (one piece into multiple formats). Brings total skills to 10.
- `infrastructure/` folder: `ARCHIVE.md.template` (per-workstation archive for completed projects and superseded decisions), `auto-memory-system.md` (four-type memory model with index pattern and line ceiling discipline), and three ready-to-run scheduled task templates (`weekly-audit.task.md`, `weekly-memory-review.task.md`, `monthly-close.task.md`).
- `WHAT-WEEK-12-LOOKS-LIKE.md`: what a mature deployment looks like at month 3. Covers structural metrics, what sessions feel like, what changed between week 1 and week 12, and the compound effect.
- `case-studies/early-adopter-template.md`: structured template for documenting a real deployment with sanitised data.

### Changed

- `CLAUDE.md.template`: eight advanced governance rules added: entity mirroring (same contact, different modes across workstations), working-files-in-workstation rule, archiving and version-control rule, session-close cadence tiers, scheduled task stacking standards, paid connector credit-spend guard, cross-workstation trigger system, Thinking HQ invocation protocol.
- `skills/skills-index.md`: updated with four new skill entries.
- `workstation-examples/README.md`: updated to show all 16 examples split into foundation (7) and advanced (9) groups.
- `README.md`: updated file tree. Removed "Want more?" section as this repo now contains the full pattern.

### Why this release

v0.2 proved the foundation. v0.3 adds the compounding layer: the workstations that matter for complex professional lives, the skills that handle high-stakes recurring tasks, and the infrastructure that keeps a mature OS clean. Everything that was previously in a separate private release is now here.

## [0.2.0] - 2026-06-04

### Added

- `FIRST-WEEK.md`: day-by-day guide for the first seven days after setup. Covers confirming the install, running the first session close, setting up the weekly audit, and building the right habits before week two.
- `INTEGRATIONS.md`: reference guide mapping external tools (Granola, Notion, Gmail, Figma, financial connectors) to the workstations they support. Includes a security note on MCP prompt injection risk.
- `workstation-examples/`: seven filled-in workstation examples showing what a working CLAUDE.md and MEMORY.md look like after personalisation. Workstations included: career-hq, email-hq, brand-hq, meeting-hq, expense-hq, property-hq, learning-hq. Each has a fully written Identity, Workflow, and Editorial Rules section.
- `skills/session-close.skill.md`: end-of-session skill for capturing changes, proposing memory updates, and emitting a compact session log. Does not write without approval.
- `skills/voice-check.skill.md`: pre-publish skill that checks any text against the user's voice principles. Surfaces hard violations first, softer issues second, full rewrite only if violations exist.
- `skills/memory-consolidation.skill.md`: quarterly cleanup skill for MEMORY.md files that have grown stale or over the line limit. Walks section by section, proposes merges, deletions, and relocations.
- `skills/humanizer.skill.md`: post-draft skill that removes AI-writing patterns (em dashes, filler openers, AI vocabulary, passive voice, rule of three) from any text before it is sent or published.
- `skills/scheduled-task.skill.md`: skill for designing and registering recurring automated tasks. Produces a task definition, a task prompt, and integration instructions. Includes stacking defaults for Friday and Monday cadences.
- `skills/skills-index.md`: registry of all available skills with trigger conditions. Referenced from root CLAUDE.md so Claude checks it before starting any task.

### Changed

- `README.md`: rewritten with a problem-first hook, a before/after section, and an updated file tree reflecting all new additions. Removed the orphaned line "5. Run the audit. Iterate from there." that appeared mid-paragraph in v0.1.
- `templates/CLAUDE.md.template`: five governance rules added to the Rules section: direct communication (no hedging), confidence-level sourcing, source transparency tagging, clean-replace on corrections, and source-of-truth hierarchy. A new Source-of-Truth Hierarchy section added with four ranked placeholder slots.
- `setup/bootstrap.md` Phase 8: rewritten as a celebration close. Lists what was created, names three first things to try, points to FIRST-WEEK.md.
- `METRICS.md`: rewritten as a progression story across week 1, week 4, and month 3. Each stage describes what the system feels like and what the structural metrics typically show.

### Why this release

v0.1 proved the pattern works. v0.2 makes it accessible to users who do not already know what "good" looks like. The seven workstation examples, the skills registry, and the first-week guide close the gap between "I have set this up" and "I know how to get value from it."

## [0.1.4] - 2026-05-24

### Fixed

- Three em dashes in the v0.1.1 CHANGELOG entries (lines describing `setup/bootstrap.md`, `setup/ingest.md`, and `setup/interview.md`). The em-dash purge in Phase 8 of the original build covered every file in the repo at that time, but the v0.1.1 commit reintroduced three em dashes inside its own CHANGELOG entries. Now replaced with colons. Voice rule: zero em dashes anywhere in the repo, including the changelog.
- `setup/bootstrap.md` Phase 4 question 3 named two specific banned words as concrete examples of words to avoid. Those words are themselves on the project's banned list, so naming them inside the example pattern-matched against the voice sweep. Rewritten to use neutral wording ("jargon you dislike, common marketing-deck words") that preserves the question's intent without including any trigger word.

### Why this release

A full repo audit (CRITICAL / WARNING / INFO categorisation following the system's own audit skill) found two voice-rule violations. Both were small and neither broke the system. Fixing them keeps the repo perfectly aligned with the rules it preaches.

## [0.1.3] - 2026-05-21

### Changed

- Renamed `START-HERE.md` to `0-CLICK-HERE-TO-START.md`. The new name does two things at once: the `0-` prefix forces the file to the top of every alphabetically-sorted file list (Finder, GitHub web, Claude Code tree, Claude Cowork tree), and the verb phrase tells a non-technical user what action to take. Old name only identified the file; new name instructs the action.
- Updated `README.md` (file tree + "How to adapt for yourself" link) and `GETTING-STARTED.md` (banner link) to point at the new filename.

### Why this release

A user opening the unzipped folder for the first time scans the file list looking for "what do I open first?". The previous filename `START-HERE.md` answered that question only if the user noticed the all-caps signal. `0-CLICK-HERE-TO-START.md` answers it visually (sort order) and verbally (the action verb is in the filename).

## [0.1.2] - 2026-05-21

### Changed

- `START-HERE.md` now opens with a "Pick your Claude app" section that names three install paths and ranks them by user-friendliness:
  1. **Claude Cowork desktop app** (recommended for everyone, including non-coders)
  2. **Claude Code desktop app** (also user-friendly, alternative to Cowork)
  3. **Claude Code CLI** (explicitly marked "developer only", placed third, not recommended for non-technical users)
- Step 1 of the three-step flow now shows the slightly different "open the folder" mechanics for each of the three apps.
- `README.md` "How to adapt for yourself" section rewritten to reflect the new app hierarchy and direct everyone to START-HERE.md by default.

### Why this release

User feedback after a second install attempt: the previous version of `START-HERE.md` said "open the folder in Claude Code" without distinguishing Cowork (the most user-friendly app for non-coders) from Code (developer-oriented) from the CLI (terminal). For non-technical users, this ambiguity adds friction at exactly the moment they need the smoothest experience. v0.1.2 makes the choice explicit and ranked.

## [0.1.1] - 2026-05-21

### Added

- `START-HERE.md` at the repository root. The single-file non-coder entry point. Three concrete steps, plain language, includes the Download-ZIP option for users who do not know git.
- `setup/bootstrap.md`: the master interactive setup prompt. The user pastes one line into Claude Code and Claude walks them through 9 phases: welcome, file ingestion, identity, voice, workstations, cadence, confirm-and-create, show-and-explain, save-and-exit. Asks one question at a time. Confirms before every file write. Tells the user exactly what got created and where.
- `setup/ingest.md`: defines how Claude handles uploaded LinkedIn PDFs, resumes, pitch decks, voice guides, and "about me" documents. Pre-fills upcoming answers from what it reads. Default privacy-conservative.
- `setup/interview.md`: reference list of every question asked during bootstrap and which template placeholder it fills.

### Changed

- `README.md` "How to adapt for yourself" section now leads with the non-coder path (`START-HERE.md`) and points developers at `GETTING-STARTED.md` as the manual fallback.
- `GETTING-STARTED.md` reframed as the manual install path, with a banner at the top directing non-developers to `START-HERE.md`.

### Why this release

Real user testing exposed v0.1 as a developer's release dressed up as a non-coder release. The templates carried plain-English placeholders, but installation still required the user to copy files, paste prompts, and remember to confirm writes. v0.1.1 adds a single-prompt bootstrap that walks any user through setup with one-question-at-a-time pacing, explicit confirmation before every file write, and the option to share files (LinkedIn, resume, pitch deck) so Claude can pre-fill answers automatically.

This is NOT v0.2. v0.2 ships the bootstrap as a registered skill that auto-triggers from natural language. v0.1.1 is the same flow expressed as a Markdown prompt the user pastes manually. Same result, less engineering.

## [0.1.0] - 2026-05-20

### Added

- Root templates: `templates/CLAUDE.md.template`, `templates/MEMORY.md.template`.
- Workstation templates: `templates/workstation/CLAUDE.md.template`, `templates/workstation/MEMORY.md.template`.
- Reusable skill: `skills/audit-system.skill.md`.
- Reusable prompts library in `prompts/` covering the five core working cycles (audit, session close, workstation create, voice check, memory consolidation), plus a README.
- Eight Architecture Decision Records in `docs/decisions/`, plus an index.
- Two runnable example scripts in `scripts/` (`expense_pipeline_example.py`, `net_worth_dashboard_example.py`) with fictional sample data in `scripts/sample_data/`.
- `GETTING-STARTED.md` non-coder-friendly deployment guide.
- `ARCHITECTURE.md` design overview with Mermaid diagram.
- `METRICS.md` describing what to expect from a running deployment.
- `ROADMAP.md` listing planned versions through v0.5.
- `SETUP-SKILL.md` design spec for the v0.2 interview-driven personaliser.
- `CONTRIBUTING.md` describing what is and is not a welcome contribution.
- `.github/ISSUE_TEMPLATE.md` and `.github/PULL_REQUEST_TEMPLATE.md`.

### Notes

- v0.1 is a manual-personalisation release. The interview-driven setup skill ships in v0.2.
- All placeholders use the `{{REPLACE: ...}}` marker convention.
- Personal data is excluded by construction. The repository contains no real names, contacts, or facts.
