# ADR 0006: Single repository, not per workstation

## Context

A personal operating system with ten workstations invites an obvious-looking design: one git repository per workstation. Each domain becomes a versionable unit. Each can be backed up, shared, or archived independently.

The reality is messier. Workstations are not independent. Routing logic crosses them. Voice rules are shared. Skills work across all of them. Cross-cutting edits become merge problems if each workstation is its own repo.

## Decision

One repository (or no repository) at the root of the operating system. Workstations are folders, not separate repos. Cross-workstation files (root CLAUDE.md, voice principles, skills registry) sit at the root and stay coherent in a single commit.

Public artefacts derived from this system live in entirely separate repositories at a different location on disk. They do not share a parent folder with the private system.

## Consequences

- Cross-cutting changes happen in one place. A rule change in the root CLAUDE.md is one commit, not ten.
- The audit can walk the entire tree in one pass.
- Routing-map integrity stays trivial. The map and the folders sit side by side.
- Per-workstation git history is lost. Accepted. Workstations evolve together more often than separately.
- Privacy is uniform. The whole private tree is private. The public artefact lives elsewhere entirely and shares no parent with the private tree.

## Alternatives considered

- One repo per workstation. Rejected. Cross-cutting edits fragment into ten commits across ten repos. Routing-map integrity becomes a manual sync problem.
- Monorepo with workspace subprojects. Rejected. Overkill for non-code working files. Adds tooling without buying anything.
- No git at all. Rejected. History and backup matter even for prose. A single repo at the root is the minimum useful versioning.
- Submodules. Rejected. Submodules are a high-cost coordination primitive. They make sense for shared code dependencies, not for personal workstations that simply share a parent context.
