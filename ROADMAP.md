# Roadmap

This is a versioned pattern, not a finished product. Each release adds one substantial capability. Plans change as people use it. Full detail for every shipped version is in [CHANGELOG.md](CHANGELOG.md).

## Shipped

| Version | What it added |
|---|---|
| v0.1 | Generic templates with placeholders, the audit skill, five prompts, eight ADRs, two example scripts, a manual setup guide. |
| v0.2 | Filled-in workstation examples, the skills registry, the first-week guide, the integrations reference. |
| v0.3 | Advanced workstations, research and outreach skills, archive and scheduled-task infrastructure. |
| v0.4 | The guided setup wizard. Type `start` and Claude interviews you and builds your OS. Skills catalog. |
| v0.5 | More workstation examples and rules brought across from the private system (see ADR 0009). |
| v0.5.1 | Setup wizard fixes: Skills phase, phase numbering, resume from the OS folder, app-path corrections. |

## Next

- **Releases.** Tag every version on GitHub so a non-technical user can download a stable ZIP with release notes.
- **Setup demo.** A short screen recording of typing `start` and finishing setup, shown at the top of the README.
- **Automated checks.** A GitHub Action that flags broken links, em dashes, and workstation counts that do not match the catalog.
- **Quick start.** A 10-minute setup path: one workstation, no file drop, defaults for everything else.
- **First real case study.** One sanitised deployment written up using `case-studies/early-adopter-template.md`.

## Exploratory

Not committed. Each needs its own ADR before any work starts.

- Team variant: shared root, individual layers, scoped workstations, attribution on every approved change.
- Voice capture on mobile that writes back into the system.
- Smaller model for routine audits, larger model for design work.
- A compliance score reported as a single number alongside the audit.

## How decisions get made

A new release plan or scope change is proposed as a GitHub Issue first. If the change is non-obvious, a new ADR captures the reasoning. Items only move from exploratory to committed once their ADR is written.
