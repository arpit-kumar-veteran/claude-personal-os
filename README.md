# Personal AI Operating System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Last commit](https://img.shields.io/github/last-commit/arpit-kumar-veteran/personal-ai-operating-system)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arpit_Kumar-0A66C2?logo=linkedin)](https://www.linkedin.com/in/arpit-kumar-veteran)
![Built with Claude](https://img.shields.io/badge/Built_with-Claude-D97757)

A clonable pattern for running your own personal AI operating system on top of Claude.

## What this is

A small set of Markdown templates, prompts, skills, and runnable example scripts that together describe how to organise a personal AI assistant around your real working life. You clone the repository, follow [GETTING-STARTED.md](GETTING-STARTED.md), and end with a working system tuned to you. Zero personal information ships in this repository. All of it is yours to add.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the design rationale and the system diagram.

In one paragraph: two tiers of memory (root plus per-workstation), strict file edit guards, a weekly scheduled audit, a skills registry for recurring patterns, and a voice principles layer that enforces tone. Workstations are folders. Governance is Markdown. The Python scripts consume the data the Markdown describes.

## What is in this repo

```
.
├── README.md                       (this file)
├── GETTING-STARTED.md              (5 to 30 minute deployment guide)
├── ARCHITECTURE.md                 (design overview + Mermaid diagram)
├── METRICS.md                      (what to expect from a running deployment)
├── ROADMAP.md                      (current and planned versions)
├── CHANGELOG.md                    (release notes)
├── CONTRIBUTING.md                 (how to contribute, what stays in your fork)
├── SETUP-SKILL.md                  (v0.2 design spec for interview-driven setup)
├── LICENSE                         (MIT)
├── templates/                      (root and workstation templates)
│   ├── CLAUDE.md.template
│   ├── MEMORY.md.template
│   └── workstation/
│       ├── CLAUDE.md.template
│       └── MEMORY.md.template
├── skills/
│   └── audit-system.skill.md       (weekly compliance audit)
├── prompts/                        (5 reusable prompts + README)
├── docs/decisions/                 (8 Architecture Decision Records + index)
├── scripts/                        (2 runnable example scripts + sample data)
├── screenshots/                    (architecture diagram source + render)
└── case-studies/                   (placeholder for future case studies)
```

## How to adapt for yourself

1. Clone the repository.
2. Read [GETTING-STARTED.md](GETTING-STARTED.md). The Quick start gets you running in about 10 minutes.
3. Personalise the templates by replacing every `{{REPLACE: ...}}` marker.
4. Create your first workstation following the same pattern.
5. Run the audit. Iterate from there.

v0.1 of this repository requires manual personalisation. v0.2 (ships next week) adds a setup skill that runs the entire personalisation as an interview. See [ROADMAP.md](ROADMAP.md).

## What this is not

- A finished product. It is a versioned pattern. The system evolves; the principles are stable.
- A coding tutorial. The Python scripts are runnable examples, but the system itself is Markdown-first. Most of the value lives in the rules, not the code.
- A guarantee of time saved. The system pays for itself once it is set up, but the first few days take work. The cost is defining your own workstations and answering placeholder questions honestly.

## Credits

Designed and built by **Arpit Kumar**, Commander Indian Navy (Retd), 15.5 years experience across naval engineering, operations leadership, and IT program management. This repository is one of the artefacts that came out of a longer project to run a personal life and work on a Claude-based system. The pattern is the part that travels. Everything personal stays private.

LinkedIn: [https://www.linkedin.com/in/arpit-kumar-veteran](https://www.linkedin.com/in/arpit-kumar-veteran)

## License

MIT. See [LICENSE](LICENSE).
