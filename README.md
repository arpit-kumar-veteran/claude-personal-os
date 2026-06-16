# Personal Claude OS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Last commit](https://img.shields.io/github/last-commit/arpit-kumar-veteran/claude-personal-os)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arpit_Kumar-0A66C2?logo=linkedin)](https://www.linkedin.com/in/arpit-kumar-veteran)
![Built with Claude](https://img.shields.io/badge/Built_with-Claude-D97757)

You use Claude every day. Every conversation starts from zero. Your context, your preferences, your history: gone. This fixes that.

## Three steps to get started

**1. Download this repo.**
Click the green **Code** button above, then **Download ZIP**. Unzip it. You get a folder called `claude-personal-os-main`.

**2. Open the folder in your Claude app.**

This works on the **Claude Pro plan ($20/month)**. No API key or separate subscription needed for the two recommended paths below.

- **Recommended — Claude desktop app (Pro, $20/month):** Download from `claude.ai/download` if you do not have it. Open the app, create a new Project, and upload the files from the unzipped `claude-personal-os-main` folder into it. Start a conversation inside that project and type `start`.
- **Claude.ai web (Pro, $20/month):** Go to `claude.ai`, create a new Project under your account, and upload the files from the unzipped folder. Open a conversation in that project and type `start`. Note: you cannot drag a folder directly into a web chat window — use Projects.
- **Claude Code desktop or CLI (developers, API credits required):** File → Open Folder → pick `claude-personal-os-main`, or `cd claude-personal-os-main` then `claude` in your terminal. `CLAUDE.md` auto-loads. Type `start`.

**3. Type: `start`**

That is the entire entry point. One word. Claude takes it from there.

---

## What happens after you type "start"

Claude walks you through a guided setup in about 30 minutes. Every response tells you what just happened, what comes next, and what to type to continue. You are never left guessing.

The flow:

1. **Welcome** — Claude shows you the full setup roadmap so you know what to expect.
2. **File drop (optional)** — Share your LinkedIn PDF, resume, or any document about yourself. Claude reads it and skips questions it can answer from there.
3. **Identity interview** — 5 short questions. Who you are, what you do, what you want this OS to help with most.
4. **Voice and preferences** — 4 short questions. How you want Claude to write on your behalf, response length, words to avoid.
5. **Workstation catalog** — Claude shows all 16 available workstations with a one-line description of each. Based on your interview answers, it marks 2-3 as "Recommended for you" and explains why. You pick 1-3 to start.
6. **Cadence** — 3 questions. Weekly audit, session-close routine.
7. **Build** — Claude creates your OS folder, fills in your files, and tells you exactly what it created and where.
8. **Handoff** — You get a working personal OS, a first-week guide, and the three things to try right now.

If you go off-topic during setup, Claude answers and brings you back. If you stop midway and return later, type `start` again — Claude will find where you left off and resume from there.

---

## What you end up with

A folder on your computer that holds your personal AI operating system:

- **`CLAUDE.md`** — your preferences, voice rules, and routing map. Claude reads this at the start of every session.
- **`MEMORY.md`** — your profile and the facts Claude needs to remember about you. Grows over time.
- **1-3 workstation folders** — domain-specific rules and memory for the areas you chose (job search, finance, health, etc.).
- **A weekly audit routine** — run it by saying "run the audit". Claude checks that everything is correctly structured and reports back.

No app installed. No cloud service. No database. The folder is yours. Move it, back it up, edit it by hand anytime.

---

## The difference

**Before:** Claude is capable but context-blind. Every session you re-explain your role, your projects, your communication style. You get good answers, always from a stranger.

**After:** Claude opens each session knowing your workstations, your voice rules, and what you decided last week. It routes work correctly, proposes memory updates, audits itself weekly, and compounds over time.

---

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full design rationale and system diagram.

In brief: two tiers of memory (root plus per-workstation), strict file edit guards, weekly scheduled audit, skills registry for recurring patterns, and a voice principles layer that enforces tone. Workstations are folders. Governance is Markdown.

---

## What is in this repo

```
.
├── CLAUDE.md                          (auto-loaded: makes "start" work)
├── README.md                          (this file)
├── 0-CLICK-HERE-TO-START.md           (non-coder guide: what to do after download)
├── FIRST-WEEK.md                      (day-by-day guide for your first 7 days)
├── WHAT-WEEK-12-LOOKS-LIKE.md         (what a mature deployment looks like at month 3)
├── INTEGRATIONS.md                    (which tools connect to which workstations)
├── setup/
│   ├── bootstrap.md                   (the guided setup flow Claude follows)
│   ├── ingest.md                      (how Claude reads LinkedIn, resume, pitch deck)
│   └── interview.md                   (full question reference)
├── GETTING-STARTED.md                 (manual install guide, for developers)
├── ARCHITECTURE.md                    (design overview + Mermaid diagram)
├── METRICS.md                         (what to expect at week 1, week 4, and month 3)
├── ROADMAP.md                         (current and planned versions)
├── CHANGELOG.md                       (release notes)
├── CONTRIBUTING.md                    (how to contribute)
├── LICENSE                            (MIT)
├── templates/                         (blank CLAUDE.md and MEMORY.md templates)
├── workstation-examples/              (16 filled-in workstation examples)
├── skills/                            (10 registered skills)
├── infrastructure/                    (scheduled task templates and archive system)
├── prompts/                           (5 reusable prompts)
├── docs/decisions/                    (Architecture Decision Records)
├── scripts/                           (example Python scripts)
└── case-studies/                      (early-adopter deployment template)
```

---

## Manual setup (developers only)

If you want full control over the file structure without the guided flow, read [GETTING-STARTED.md](GETTING-STARTED.md). Copy templates by hand, replace `{{REPLACE: ...}}` markers yourself, build your routing map directly.

---

## Credits

Designed and built by **Arpit Kumar**, Commander Indian Navy (Retd), 15.5 years across naval engineering, operations leadership, and IT program management.

LinkedIn: [https://www.linkedin.com/in/arpit-kumar-veteran](https://www.linkedin.com/in/arpit-kumar-veteran)

---

## License

MIT. See [LICENSE](LICENSE).
