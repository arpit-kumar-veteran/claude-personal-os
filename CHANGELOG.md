# Changelog

All notable changes to this pattern are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/). Version numbers follow [Semantic Versioning](https://semver.org/) loosely: major versions reflect substantial changes to the pattern, minor versions add capabilities, patch versions fix bugs in examples or documentation.

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
- `setup/bootstrap.md` — the master interactive setup prompt. The user pastes one line into Claude Code and Claude walks them through 9 phases: welcome, file ingestion, identity, voice, workstations, cadence, confirm-and-create, show-and-explain, save-and-exit. Asks one question at a time. Confirms before every file write. Tells the user exactly what got created and where.
- `setup/ingest.md` — defines how Claude handles uploaded LinkedIn PDFs, resumes, pitch decks, voice guides, and "about me" documents. Pre-fills upcoming answers from what it reads. Default privacy-conservative.
- `setup/interview.md` — reference list of every question asked during bootstrap and which template placeholder it fills.

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
