# Changelog

All notable changes to this pattern are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/). Version numbers follow [Semantic Versioning](https://semver.org/) loosely: major versions reflect substantial changes to the pattern, minor versions add capabilities, patch versions fix bugs in examples or documentation.

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
