---
name: workstation-create-full
description: Full guided interview for creating a new workstation. Asks five sequential questions, generates complete CLAUDE.md and MEMORY.md with real content (not placeholders), adds the routing map row, and runs the audit on the new workstation before confirming. More thorough than the basic prompt-based workstation creation.
---

# Workstation Create (Full)

This skill creates a production-ready workstation through a structured interview. Output is complete files, not templates with placeholders.

## When to use

- Creating a new workstation that will handle complex or recurring work.
- When you want the workstation built correctly the first time, not iterated into shape.
- After identifying a domain where Claude has been losing context across multiple sessions.

## How it runs

### Step 1: Pre-check

Before the interview, check:
- Does a workstation for this domain already exist in the routing map? If yes, surface it and ask whether to extend the existing one or create a new one.
- Does this domain meet the workstation threshold? The work must create its own pipeline, taxonomy, or recurring deliverable. If it does not, suggest a resource file in an existing workstation instead.

### Step 2: Interview (five questions, one at a time)

Ask each question separately. Wait for the full answer before moving to the next.

**Question 1 — Name**
What should this workstation be called? Keep it lowercase with hyphens (e.g. `career-hq`, `health-hq`). The name should describe the domain, not the tool or task.

**Question 2 — Identity**
Write the Identity paragraph for this workstation. It needs three things:
- What routes here (specific triggers, not general descriptions).
- What does NOT route here (the counter-examples, which are as important as the inclusions).
- The boundary with adjacent workstations.

If the answer is vague, ask one more question: "Name two tasks that belong here and two tasks that definitely do not."

**Question 3 — Resources**
What files, links, or reference materials does this workstation need to read regularly? For each one, what is the trigger condition for reading it?

If none yet, that is acceptable. The resources table starts empty and grows.

**Question 4 — Workflow**
Walk me through the primary task in this workstation, step by step. Aim for 4 to 7 steps. Each step should be an action, not a heading.

**Question 5 — Editorial rules**
What specific rules apply to writing or behaviour in this workstation that are not already in the root CLAUDE.md? Aim for 3 to 5 rules. Each rule must be short and testable.

### Step 3: Generate files

Produce the complete CLAUDE.md and MEMORY.md using the answers:
- CLAUDE.md: all four required sections in order (Identity, Resources, Workflow, Editorial Rules). No placeholders.
- MEMORY.md: correct header, Contacts table (empty, ready to populate), Key Decisions (one starter entry noting the workstation creation date and context).

Present both files in full. Do not create them yet.

### Step 4: Routing map

Produce the new row for the root CLAUDE.md Routing Map:

```
| [workstation-name] | [routing trigger in plain language] |
```

### Step 5: Confirm and create

Ask: "Ready to create all of this?"

On yes: create the workstation folder, write both files, add the routing map row to root CLAUDE.md.

After each file write, confirm what was created.

### Step 6: Audit

Run the audit-system skill scoped to the new workstation only. Report any CRITICAL or WARNING findings. Fix before closing the session if possible.

## Boundaries

- Do not create a workstation that duplicates an existing one. Check the routing map first.
- Do not create files with placeholder content. Every field in the output must be filled.
- The routing map update requires writing to root CLAUDE.md: confirm this explicitly before writing.
- If the interview answers are too thin to produce a complete Identity, ask again rather than generating a weak one.
