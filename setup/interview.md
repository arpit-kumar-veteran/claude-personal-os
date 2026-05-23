# Interview question reference

Master list of questions used by the bootstrap flow. Each question is tagged with the template placeholder or file destination it fills.

This file exists for two reasons:

1. Anyone reading the repo can see the full question set without walking through `bootstrap.md`.
2. v0.2 of this project will programmatically reference these questions for the self-installing setup skill.

## Section 1: Identity (5 questions)

| # | Question | Fills |
|---|---|---|
| 1.1 | What name should I use for you? | `{{USER_NAME}}` across templates |
| 1.2 | Your primary role or main work focus | Root `MEMORY.md` Profile section |
| 1.3 | The single biggest thing you want this OS to help you with | Root `MEMORY.md` Profile section |
| 1.4 | 2-3 sentence "about me" | Root `MEMORY.md` Profile section |
| 1.5 | Where to create your OS folder | OS root path |

## Section 2: Voice and preferences (4 questions)

| # | Question | Fills |
|---|---|---|
| 2.1 | Tone preference | Root `CLAUDE.md` Preferences (first item) |
| 2.2 | Response length default | Root `CLAUDE.md` Preferences (second item) |
| 2.3 | Words or phrases to never use | Root `CLAUDE.md` Editorial Rules |
| 2.4 | Path to existing voice guide file (optional) | Root `CLAUDE.md` References table |

## Section 3: Workstations (repeated per workstation)

| # | Question | Fills |
|---|---|---|
| 3.1 | Workstation name (kebab-case folder name) | Folder name |
| 3.2 | One paragraph identity: what goes in, what does not | Workstation `CLAUDE.md` Identity section |
| 3.3 | Main task you want help with in this workstation | Workstation `CLAUDE.md` Workflow (first step) |
| 3.4 | Resources or files for this workstation (optional) | Workstation `CLAUDE.md` Resources table |

## Section 4: Cadence (3 questions)

| # | Question | Fills |
|---|---|---|
| 4.1 | Do you want a weekly audit? | Scheduled task on/off |
| 4.2 | Day and time for the audit | Scheduled task config |
| 4.3 | Do you want a session-close routine? | Root `CLAUDE.md` Rules |

## Total

Around 12 + (4 per workstation) questions. For a user starting with 2 workstations: 20 questions. For 3 workstations: 24. Most take under 30 seconds to answer.

## When to add a question

- The question must fill a specific placeholder or rule. If it does not, do not ask.
- The question must be answerable in under 60 seconds. If it needs longer, split into two.
- The question must be answerable by a non-technical user. If it uses jargon, simplify or remove.

## When to remove a question

- If repeated user feedback shows people skip it or get confused, remove it.
- If a more direct file ingestion path makes it redundant, remove it.
