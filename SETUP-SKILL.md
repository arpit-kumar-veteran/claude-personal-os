# Self-installing setup skill: v2 in progress

**Status:** Designed, not yet implemented. Ships in v0.2. Tracked publicly in the v2 GitHub Issue linked from the repo Issues tab.

This file documents the v2 setup skill that will interview a new cloner and personalise the templates automatically. v1 ships without it; placeholders in the templates are filled manually following GETTING-STARTED.md. v2 ships next week.

## What it will do

A single skill the cloner invokes after cloning the repo. It reads a structured interview file, asks each question in turn, captures answers to a local file (gitignored), and substitutes every `{{REPLACE: ...}}` marker across the templates with the user's answer. Every placeholder traces to one question. No hidden state.

## Why this is in v1 as a design spec

To make the v2 release concrete and reviewable before implementation. The questions, flow, and output schema below are stable. The implementation is what changes. A cloner reading this file in v1 can run the v2 flow manually by walking the questions themselves and filling the placeholders by hand.

## Interview structure

Six sections, around thirty questions in total.

### Section 1: Identity (5 questions)

- Your name (used in MEMORY.md profile).
- Your primary role.
- The main responsibility you want help with.
- A short "about me" paragraph that future sessions should know.
- The line limit you want for your root CLAUDE.md (default: 300).

### Section 2: Voice (4 questions)

- Tone preference (professional, conversational, blunt, formal, or other).
- Maximum response length default in words.
- One word or phrase you want Claude to avoid using.
- Path to your voice principles file, if you have one.

### Section 3: Workstations (6 questions)

- How many workstations do you want to create (1 to 10).
- For each: name, one-line identity, primary trigger condition.
- Whether you want a routing map row generated for each automatically.

### Section 4: Cadence (4 questions)

- Which workstations need a weekly audit.
- Which need a monthly close.
- What day and time should weekly tasks fire.
- What day of the month should monthly tasks fire.

### Section 5: Integrations (5 questions)

- Do you use a cloud drive? If yes, the local mount path.
- Do you use a notes app? If yes, which one.
- Do you use a meeting notes tool? If yes, which one.
- Do you use a personal calendar? If yes, which one.
- Where do you want skill definitions to live.

### Section 6: Naming (6 questions)

- How should Claude address you.
- What term do you want for "workstation" if not "workstation".
- What do you call your operating system root folder.
- What is your preferred date format (YYYY-MM-DD, DD MMM YYYY, or other).
- What currency symbol or code is your default.
- Anything else Claude should know about how you name things.

## Output schema

Answers are written to `setup/answers.md` (gitignored) in this shape:

```yaml
identity:
  name: ...
  role: ...
  responsibility: ...
voice:
  tone: ...
  max_words: 300
workstations:
  - name: ...
    identity: ...
    trigger: ...
cadence:
  weekly_audit: [...]
  monthly_close: [...]
integrations:
  cloud_drive: ...
naming:
  date_format: YYYY-MM-DD
```

The skill then walks every `templates/**/*.template` file, replaces every `{{REPLACE: ...}}` marker with the matching answer, and writes the result to the corresponding non-template path.

## Idempotent re-runs

The skill can be re-run any time. Existing answers are kept. New questions added in future versions are asked once. Each re-run prints a diff before writing anything.

## Why this design

- One skill. One file output. No hidden state. Auditable.
- The interview file is human-readable so anyone can extend it without touching code.
- Placeholders are explicit, so a cloner can fill them manually in v1 and still get the same result.
- The skill never overwrites a file without printing a diff first.
