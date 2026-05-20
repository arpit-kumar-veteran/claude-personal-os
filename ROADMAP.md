# Roadmap

This is a versioned pattern, not a finished product. Each release adds one substantial capability. The list below is the current plan. It will change as v0.1 gets used.

## v0.1: Initial release (current)

Shipped:

- Generic root and workstation templates with explicit placeholders.
- Reusable skill: `audit-system`.
- Reusable prompts library covering audit, session close, workstation create, voice check, and memory consolidation.
- Eight Architecture Decision Records.
- Two runnable example scripts (expense pipeline, net worth dashboard) with fictional sample data.
- A non-coder-friendly `GETTING-STARTED.md` deployment guide.

Personalisation is manual in this release. The cloner replaces each `{{REPLACE: ...}}` marker by hand following the guide.

## v0.2: Self-installing setup skill (next)

A Claude skill that:

- Walks the cloner through an interview of around 30 questions across six sections.
- Captures answers to a local file (gitignored).
- Substitutes every `{{REPLACE: ...}}` marker across the templates from the captured answers.
- Prints a diff before writing.
- Re-runnable. Existing answers are preserved; new questions added in future versions are asked once.

The design spec is already in this repository at [`SETUP-SKILL.md`](SETUP-SKILL.md). v0.2 is the implementation.

## v0.3: A second worked example

A complete worked example of a second domain (suggested: a meeting-notes workstation with a transcript-to-action-items pipeline). Demonstrates how a workstation grows from one folder to a full pipeline.

Includes:

- The workstation's CLAUDE.md and MEMORY.md, personalised with example content.
- A Python script that processes sample transcripts into structured output.
- A skill that runs the pipeline on demand.
- A CHANGELOG entry showing how a workstation evolves between releases.

## v0.4: Team variant

A variant of the pattern for two-person workflows. The two-tier memory becomes three: shared root, individual layers, scoped workstations. File edit guards extend to attribution (who proposed what, who approved).

This is exploratory. The single-user pattern is the focus through v0.3. A team variant should not slow the single-user release cycle.

## v0.5 and beyond: exploratory

Items being considered for later releases. Not committed. Each is a candidate for its own ADR before any code is written.

- Voice capture on mobile that writes back into the system.
- Multi-model fallback (use a smaller model for routine audits, larger for design work).
- A web reader that renders the entire OS as a static site for review.
- A compliance score reported as a single number alongside the audit.

## How decisions get made

A new release plan or scope change is proposed as a GitHub Issue first. If the change is non-obvious, a new ADR captures the reasoning. Roadmap items only move from exploratory to committed once their ADR is written.
