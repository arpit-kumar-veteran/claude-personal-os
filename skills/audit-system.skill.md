---
name: audit-system
description: Audit the entire personal AI operating system for compliance, organisation, and rule adherence. Use whenever the user asks to "audit the system", "run an audit", "check if everything is in order", "health-check the OS", "review the operating system", "what is broken in the OS", or any request to validate the state of the workspace. Also trigger after major structural changes, after a workstation is created or refactored, or when the user says something seems off with the system.
---

# Audit System

This skill runs a structured compliance audit across the entire personal AI operating system. It produces a categorised report and proposes fixes. It does not modify any file on its own.

## When to use

- The user asks for an audit, health check, or system review.
- Immediately after a workstation is created, renamed, or restructured.
- After a multi-file refactor across CLAUDE.md / MEMORY.md files.
- On a scheduled cadence (weekly is a reasonable default).

## How it runs

### Step 1: Inventory

Walk `{{PATH_TO_OS_ROOT}}/` and produce a clean list of:

- Every workstation folder.
- Every CLAUDE.md and MEMORY.md file (path + line count).
- Every script and skill file.
- Every scheduled task definition.
- Every reference file pointed to by the root CLAUDE.md.

Print the inventory in a collapsed block. Do not analyse yet.

### Step 2: Compliance checks

Run the checks below. Each check produces a CRITICAL, WARNING, or INFO finding.

**Structure (CRITICAL on failure):**

- Every workstation has both a CLAUDE.md and a MEMORY.md.
- Every workstation CLAUDE.md has all four required sections in order: Identity, Resources, Workflow, Editorial Rules.
- Every MEMORY.md has its header line and required sections.
- No file contains tokens from the user-defined personal-information blocklist (phone, email, account numbers, etc.).

**Quality (WARNING on failure):**

- Every workstation listed in the root Routing Map has a matching folder.
- Every workstation folder has a row in the Routing Map.
- No CLAUDE.md exceeds its declared line limit.
- No MEMORY.md contains change logs, version notes, or duplicate facts.
- Every file referenced in a Resources table exists on disk or at the linked URL.

**Hygiene (INFO):**

- MEMORY.md last-updated date is within the expected cadence.
- Skills referenced in skills-index.md exist on disk.
- Scheduled tasks defined externally have a matching documented trigger.
- No two workstations duplicate the same Identity scope.

### Step 3: Report

Produce a report with three sections in this order:

```
## CRITICAL
- [path:line] | [problem] | [suggested fix]

## WARNING
- [path:line] | [problem] | [suggested fix]

## INFO
- [path:line] | [observation]
```

If a section is empty, write "None." Do not invent findings to fill a section. The point of an empty section is to confirm the system is clean on that axis.

### Step 4: Propose fixes (do not write)

For each CRITICAL and WARNING finding, propose the exact edit. State the file, the section, the line range, and the proposed replacement text. Do not write any file as part of the audit. Wait for the user to approve each proposed fix one by one or in a batch.

## Boundaries

- Read-only by default. The audit never modifies a file on its own.
- Never propose deletions without surfacing the affected file path and waiting for explicit confirmation.
- Audit findings are advisory. The user's judgement is final.
- If the audit cannot determine whether something is a violation, report it as INFO with a question, not as WARNING.
