# Personal Claude OS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Last commit](https://img.shields.io/github/last-commit/arpit-kumar-veteran/claude-personal-os)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arpit_Kumar-0A66C2?logo=linkedin)](https://www.linkedin.com/in/arpit-kumar-veteran)
![Built with Claude](https://img.shields.io/badge/Built_with-Claude-D97757)

You use Claude every day. Every conversation starts from zero. Your context, your preferences, your history: gone. This fixes that.

## The difference

**Before this OS:** Claude is capable but context-blind. Every session you re-explain your role, your projects, your communication style. You get good answers, but always from a stranger.

**After this OS:** Claude opens each session knowing your workstations, your voice rules, your open threads, and what you decided last week. It routes work correctly, proposes memory updates, audits itself weekly, and compounds over time.

The system is Markdown files. No app, no cloud service, no subscription. The folder is yours.

## What this is

A set of Markdown templates, skills, prompts, workstation examples, and runnable scripts that describe how to organise Claude around your real working life. You clone the repo, run an interactive 30-minute setup, and end with a working personal AI operating system tuned to you. Zero personal information ships in this repository. All of it is yours to add.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full design rationale and system diagram.

In one paragraph: two tiers of memory (root plus per-workstation), strict file edit guards, a weekly scheduled audit, a skills registry for recurring patterns, and a voice principles layer that enforces tone. Workstations are folders. Governance is Markdown. The Python scripts consume the data the Markdown describes.

## What is in this repo

```
.
├── README.md                          (this file)
├── 0-CLICK-HERE-TO-START.md           (non-coder entry point. Click this first.)
├── FIRST-WEEK.md                      (day-by-day guide for your first 7 days)
├── INTEGRATIONS.md                    (which tools connect to which workstations)
├── setup/                             (interactive bootstrap flow)
│   ├── bootstrap.md                   (the master setup prompt Claude follows)
│   ├── ingest.md                      (how Claude handles LinkedIn, resume, pitch deck)
│   └── interview.md                   (the question reference)
├── GETTING-STARTED.md                 (manual install guide, for developers)
├── ARCHITECTURE.md                    (design overview + Mermaid diagram)
├── METRICS.md                         (what to expect at week 1, week 4, and month 3)
├── ROADMAP.md                         (current and planned versions)
├── CHANGELOG.md                       (release notes)
├── CONTRIBUTING.md                    (how to contribute)
├── SETUP-SKILL.md                     (v0.2 design spec for the auto-installing skill)
├── LICENSE                            (MIT)
├── templates/                         (root and workstation blank templates)
│   ├── CLAUDE.md.template
│   ├── MEMORY.md.template
│   └── workstation/
│       ├── CLAUDE.md.template
│       └── MEMORY.md.template
├── workstation-examples/              (7 filled-in workstation examples)
│   ├── README.md
│   ├── career-hq/
│   ├── email-hq/
│   ├── brand-hq/
│   ├── meeting-hq/
│   ├── expense-hq/
│   ├── property-hq/
│   └── learning-hq/
├── skills/                            (6 registered skills)
│   ├── skills-index.md                (registry: what exists, when to use it)
│   ├── audit-system.skill.md
│   ├── session-close.skill.md
│   ├── voice-check.skill.md
│   ├── memory-consolidation.skill.md
│   ├── humanizer.skill.md
│   └── scheduled-task.skill.md
├── prompts/                           (5 reusable prompts + README)
├── docs/decisions/                    (8 Architecture Decision Records + index)
├── scripts/                           (2 runnable example scripts + sample data)
├── screenshots/                       (architecture diagram source + render)
└── case-studies/                      (placeholder for future case studies)
```

## How to set up

Two paths. Same destination.

**Recommended for everyone.** Download this repo (green Code button, then Download ZIP, or `git clone`), then open [0-CLICK-HERE-TO-START.md](0-CLICK-HERE-TO-START.md). It walks you through picking a Claude app, opening the folder, and pasting one line. Claude interviews you, reads your LinkedIn or resume if you share it, and creates your personalised OS folder. About 30 minutes.

**For developers who want manual control.** Read [GETTING-STARTED.md](GETTING-STARTED.md). Copy templates by hand, replace `{{REPLACE: ...}}` markers yourself, build your routing map directly.

After setup: read [FIRST-WEEK.md](FIRST-WEEK.md) for a day-by-day guide to getting value in the first 7 days.

## What it does not do

- It does not install an app or run a server. It creates a folder of files.
- It does not guarantee productivity gains. It guarantees that Claude knows who you are and how you work. What you do with that is up to you.
- It does not manage itself. You run the weekly audit. You close sessions. You decide what gets remembered. The system enforces your rules; you still make the rules.

## Want more?

This repository is the free tier. An advanced version with 12 mature workstations, 8 additional skills, scheduled task templates, MCP integration guides, and a full case study is available separately. See [ROADMAP.md](ROADMAP.md) for what is planned and what is already built.

## Credits

Designed and built by **Arpit Kumar**, Commander Indian Navy (Retd), 15.5 years across naval engineering, operations leadership, and IT program management. This repository is one artefact from a longer project to run a personal life and work on a Claude-based system. The pattern is what travels. Everything personal stays private.

LinkedIn: [https://www.linkedin.com/in/arpit-kumar-veteran](https://www.linkedin.com/in/arpit-kumar-veteran)

## License

MIT. See [LICENSE](LICENSE).
