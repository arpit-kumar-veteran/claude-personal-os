---
name: voice-check
description: Check any written content against the user's voice principles. Surfaces hard rule violations first, then softer tone issues, then produces a clean rewrite if needed. Use before sending an email, publishing a post, or finalising any external-facing document.
---

# Voice Check

This skill validates written content against your voice principles. It does not rewrite unless there are hard violations.

## When to use

- Before sending any email you did not write yourself.
- Before publishing any post, article, or external document.
- After Claude drafts anything on your behalf and you are not sure it sounds like you.
- As a final check after editing.

## How it runs

### Step 1: Load voice principles

Read the voice principles file referenced in the root CLAUDE.md. If no voice principles file exists, ask the user to describe their voice rules before continuing.

### Step 2: Check for hard violations

Hard violations are explicit rules in your voice principles that the content breaks. For each violation:

- Quote the offending text exactly.
- State which rule it breaks.
- Propose a one-line fix.

Format:

```
VIOLATION: "[quoted text]"
RULE: [which rule this breaks]
FIX: [proposed replacement]
```

### Step 3: Note softer issues

Softer issues are tone misalignments: hedging, filler phrases, passive voice where active is preferred, vague verbs, or a register that does not match your stated style. These are observations, not violations. List them briefly.

### Step 4: Rewrite (only if hard violations exist)

If Step 2 found hard violations, produce a full clean rewrite with all violations corrected. If Step 2 found nothing, do not produce a rewrite. A clean check report is the output.

## Boundaries

- Do not flag style preferences that are not in the voice principles file. Check against the rules, not personal taste.
- Do not silently rewrite. Always show the check report before producing a rewrite.
- If the voice principles file has not been populated yet, say so and stop.
