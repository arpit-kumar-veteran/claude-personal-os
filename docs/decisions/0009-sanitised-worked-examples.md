# ADR 0009: Sanitised worked examples alongside templates

Partially supersedes [ADR 0003](0003-generic-templates-over-personal-mirror.md).

## Context

ADR 0003 chose generic templates with placeholders over a sanitised copy of the private system. It argued that sanitisation is fragile and that a copy of "my" system is not usable by anyone else.

Early users struggled with blank templates. They did not know what a good workstation looked like after a few weeks of use. From v0.2 onward the repo shipped filled-in workstation examples. v0.3.0 and v0.5.0 went further and brought rules and workflows across from the private system, rewritten in generic form.

The repo now does something ADR 0003 rejected. That needs to be recorded, not left as drift.

## Decision

Keep templates as the thing a user fills in. Also publish worked examples drawn from the private system, under three conditions:

1. Every example is rewritten generically before it is committed. Names, organisations, amounts, places, and dates are replaced with fictional or generic values.
2. The redaction-token rule applies. Before any file is committed, the list of private tokens is checked against it and the result shown.
3. Examples show structure and rules, not personal history. MEMORY.md examples stay short and fictional.

Templates remain the source of truth for setup. Examples are reference material the setup wizard reads from.

## Consequences

- New users see what "good" looks like, which blank templates could not show.
- The leak risk that ADR 0003 warned about is real. It is managed by the redaction-token check rather than avoided by construction.
- Each release that brings content across from the private system needs a personal-information sweep before it is pushed.

## Alternatives considered

- Stay with templates only (ADR 0003 as written). Rejected. Users did not get value until weeks in.
- Publish the private system with light scrubbing. Rejected for the same reasons ADR 0003 gives.
