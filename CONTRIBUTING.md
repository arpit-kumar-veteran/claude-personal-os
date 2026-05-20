# Contributing

This repository is designed to be forked and personalised, not contributed to directly. The pattern is yours once you clone it. The version on this repository stays generic.

That said, two kinds of contributions are welcome.

## Documentation fixes

Typo, broken link, unclear instruction, mistake in an ADR. Open a pull request with the fix. Small PRs review quickly.

## New generic patterns

Prompts, skills, ADRs, or template improvements that anyone could reuse without changing the core design. Examples that would qualify:

- A new prompt covering a working cycle the existing five do not.
- A new skill addressing a pattern several users have requested.
- An ADR capturing a non-obvious decision missing from the current set.
- A new generic workstation template for a domain that recurs across deployments.

Examples that would not qualify (these belong in your fork):

- Your specific workstation contents.
- Custom rules from your own working style.
- Domain-specific scripts or data.

## How to propose a change

1. Open a GitHub Issue first. Describe the change in two or three paragraphs. Reference the ADR that the change either supports or supersedes.
2. Wait for a short discussion. The Issue closes with either "go" or "not now".
3. If go, open a pull request that references the Issue.

The PR template at `.github/PULL_REQUEST_TEMPLATE.md` lists the checks each change must pass.

## What is not negotiable

The principles in the ADRs are stable. In particular:

- No personal information in this repository.
- No auto-write of governance files.
- Voice rules: short sentences, no em dashes, no marketing words, no motivational closers.

A PR that violates these will be closed. Open an Issue first if you want to propose a change to one of these principles, and write the ADR that supersedes the current one.
