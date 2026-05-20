# ADR 0003: Generic templates over personal mirror

## Context

A personal AI operating system is, by definition, personal. Publishing it for others to learn from raises an immediate question. Do you sanitise your own working system and publish the artefact? Or do you generalise the pattern and publish a template that others personalise?

Both produce a public repository. They produce very different artefacts.

## Decision

Generalise. Publish templates with explicit placeholders. Personal answers stay private and are filled at clone-time by each new user.

The repository carries zero personal information by construction. Not by scrubbing. A cloner who reads any file finds either a pattern, a rule, an example with fictional data, or a placeholder. They never find a name, an address, a vendor, or a private fact.

## Consequences

- The published artefact is reusable by anyone. The repo is a starter, not a memoir.
- Cloners do their own interview. They get a system tuned to them, not to me.
- The template is testable. Anyone can clone, run the personalisation flow, and verify the result.
- The repo can be updated and re-released without re-scrubbing each version. There is nothing to scrub.
- Cost: more upfront work to identify what is generic and what is mine. The boundary is not always obvious.

## Alternatives considered

- Publish a sanitised mirror of the personal system. Rejected. Sanitisation is fragile. Even after careful work, one missed token leaks private information. The result is also "my" system, not "yours". A reader cannot use it directly.
- Publish an essay describing the pattern, no code. Rejected. An essay alone gives no working starter. No concrete artefact to fork. The pattern stays abstract.
- Publish a fork-and-edit guide alongside a personal copy. Rejected. Splits attention. Both halves are weaker. The reader does not know whether to read the guide or copy the example.
