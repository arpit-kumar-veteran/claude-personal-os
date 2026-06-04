---
name: humanizer
description: Remove AI-writing signals from any text. Makes Claude-drafted content sound natural and human-authored. Use after any draft Claude produces that will be sent, posted, or published under the user's name.
---

# Humanizer

This skill removes common AI-writing patterns from text. It does not change meaning. It changes how the writing reads.

## When to use

- After Claude drafts an email, post, article, or message you will send as yourself.
- When text feels polished but not personal.
- Before any external publish or send.

## What it fixes

### Hard patterns (always remove)

- **Em dashes used as parentheticals.** Replace with a comma, a colon, or a restructured sentence.
- **Rule of three.** "X, Y, and Z" constructions that pad rather than add. Cut to the strongest one or two.
- **Motivational closers.** "Excited to...", "Looking forward to...", "Hope this helps." Cut or replace with a direct close.
- **AI vocabulary words.** Delve, leverage, utilize, robust, seamless, transformative, cutting-edge, impactful, actionable, holistic, elevate, unlock, empower, navigate. Replace with plain verbs and nouns.
- **Filler openers.** "Certainly!", "Absolutely!", "Great question!", "Of course." Delete entirely.
- **Excessive hedging.** "It is worth noting that...", "It is important to remember that...", "One might argue..." Cut the hedge; state the point.
- **Passive voice where active works.** "It was decided that" becomes "We decided." "Errors were found" becomes "I found errors."

### Softer patterns (fix where present)

- Over-structured text (every paragraph has a bold header when prose would read better).
- Nominal style: "make a decision" becomes "decide"; "provide assistance" becomes "help".
- Vague subject: "This means that..." Replace with the specific agent doing the thing.
- Inflated framing: "In today's fast-paced world..." Delete the setup. Start with the point.

## How it runs

### Step 1: Scan

Read the text. List every hard pattern found with the exact quote.

### Step 2: Propose fixes

For each hard pattern: quote the original, state the pattern, show the fix.

### Step 3: Rewrite

Produce the full rewritten version with all fixes applied. Do not change meaning, order, or key facts. Only change how it reads.

### Step 4: Confirm

Present original and rewritten versions side by side (or sequentially for long texts). Wait for approval before the rewritten version is used.

## Boundaries

- Do not change technical content, facts, or the user's intended meaning.
- Do not make the text more casual than the user's stated voice level.
- Do not flag patterns that are not in the list above. Check the list, not personal taste.
