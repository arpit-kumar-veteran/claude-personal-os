# ADR 0010: Basic and Advanced editions

## Context

By v0.5.0 the public repository carried almost everything from the Advanced edition: all twenty workstation examples, the full governance template, and most skills. The Advanced edition differed only by three skills, five prompts, six resource files, and one guide. There was no real reason to move from one to the other, and the public README did not mention the Advanced edition at all.

A first-time user also faced a catalog of twenty workstations during setup. Most people need two or three.

## Decision

Split the pattern into two editions with a clear line between them.

- **Basic (public):** the guided setup, seven foundation workstations plus thinking-hq, six core skills, five prompts, the core governance rules, and all docs and ADRs.
- **Advanced:** everything in Basic plus twelve more workstations, seven more skills, five more prompts, eight advanced governance rules, pre-built resource files, and the week 4 guide.

The public README explains the difference and how to get the Advanced edition.

## Consequences

- The setup catalog in Basic is shorter and easier to choose from.
- Advanced has a distinct value that is easy to explain in one table.
- Content removed from Basic remains visible in the public git history of earlier versions. The split applies from v0.6.0 forward.
- Shared files (setup wizard, core template, docs) must be kept in step across both repositories. Fixes land in Basic first, then are ported to Advanced.

## Alternatives considered

- Keep everything public and drop the Advanced edition. Rejected for now. The owner wants a separate tier.
- Rewrite git history to remove advanced content from Basic. Rejected. It is risky, breaks existing forks and downloads, and those copies would keep the content anyway.
