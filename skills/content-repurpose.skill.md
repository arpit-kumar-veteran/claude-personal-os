---
name: content-repurpose
description: Turn one piece of content into multiple formats for different platforms. Maps the repurpose chain, rewrites each format from scratch for its native context, runs humanizer on each output, and logs to the content calendar. Use after publishing any long-form piece (article, essay, transcript, case study).
---

# Content Repurpose

This skill rewrites existing content into new formats. It does not reformat. Each output is written for its native context.

## When to use

- After publishing or completing a long-form piece (article, essay, case study, recording transcript).
- When you want to reach a platform audience that does not read long-form.
- When a piece performed well and you want to extend its reach.

## How it runs

### Step 1: Source assessment

Read the source piece. Identify:
- The core idea (one sentence).
- The strongest three to five specific facts, numbers, or moments.
- The most quotable sentence.
- The natural angle for each platform.

If the piece does not have a clear core idea, flag it. Repurposing a vague piece produces vague outputs.

### Step 2: Map the repurpose chain

Propose the chain based on the source format and available platforms. Standard chain for a long-form article:

```
Article (source)
  -> LinkedIn post (distilled angle, 200-250 words)
  -> LinkedIn carousel (5-7 slides, visual storytelling)
  -> Short-form thread (5-7 punchy points)
  -> Newsletter section (reader-personalised, conversational)
```

Present the chain. Ask which formats to proceed with. Do not draft everything speculatively.

### Step 3: Draft each format

Write each approved format from scratch. Rules per format:

**LinkedIn post:** Lead with the strongest specific insight, not the article title. Under 250 words. No link in the body (add in first comment). End with one question or one direct close.

**Carousel:** Slide 1 is the hook (single bold claim). Slides 2-6 are one idea each, visually digestible. Final slide is the takeaway or CTA. Each slide under 20 words.

**Thread:** Opening tweet is the thesis. Each subsequent post advances the argument or adds one specific point. No filler posts. 5 to 7 posts maximum.

**Newsletter section:** More conversational than the source. Assume the reader knows you. Add one sentence of personal context the article does not have.

### Step 4: Humanize each output

After drafting, run the humanizer skill on each format. Present the humanized version, not the raw draft.

### Step 5: Log and schedule

Propose entries for `content-hq/resources/content-calendar.md`: one row per format, with draft date, platform, and status (ready / needs review / scheduled). Wait for approval before writing.

## Boundaries

- Each format is a full rewrite, not a cut-paste. If the output reads like an extract, rewrite it.
- Do not repurpose a piece that was not approved or published without asking.
- Platform-specific rules (word limits, hashtag conventions, link placement) apply. Note them in the draft.
- If the source piece is thin, say so. A 300-word post cannot be repurposed into five formats without padding.
