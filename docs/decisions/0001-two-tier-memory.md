# ADR 0001: Two-tier memory

## Context

Personal AI assistants need persistent memory across sessions. A single monolithic memory file becomes unmanageable past a few months. Cross-cutting governance gets mixed with domain-specific facts. Loading the entire file at every session start wastes context and blurs scope.

## Decision

Memory lives in two tiers.

The root tier holds CLAUDE.md (governance rules, preferences, routing) and MEMORY.md (active projects, profile, cross-cutting facts). These load on every session.

Each workstation holds its own CLAUDE.md (Identity, Resources, Workflow, Editorial Rules) and MEMORY.md (Contacts, Key Decisions). These load only when the workstation is in scope for the current task.

The routing map in the root CLAUDE.md decides which workstation is in scope.

## Consequences

- Memory stays scoped. Only the workstation relevant to the current task contributes its detail to the session.
- Adding a new domain does not bloat existing files. It adds one folder.
- Cross-cutting concerns have exactly one home. They do not get duplicated across workstations.
- Routing logic becomes a load-bearing component. If the routing map is wrong, the right memory does not load.

## Alternatives considered

- Single monolithic memory file. Rejected. Grows unbounded. Becomes unreadable past six months. Loading it costs context every session whether it is relevant or not.
- Per-task memory at finer granularity. Rejected. Too granular. Loses the shared context that makes a workstation cohesive.
- External database with a query layer. Rejected. Adds infrastructure. Breaks the "edit a Markdown file" simplicity that makes the system possible for a non-coder to maintain.
