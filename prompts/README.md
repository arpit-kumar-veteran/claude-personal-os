# Prompts library

This folder holds reusable prompts that demonstrate the operating system's working patterns. Each prompt is a complete, copy-pasteable instruction that can be run inside Claude Code without invoking a registered skill.

The same patterns appear in `/skills/` as skill files when they benefit from automatic triggering. The difference: prompts are explicit and called by hand; skills are implicit and triggered by natural-language requests. Some patterns work better one way, some the other. The five below have been useful as manual prompts during development and refinement.

## What is here

| Prompt | What it does |
|---|---|
| [audit-system.prompt.md](audit-system.prompt.md) | Manual trigger for the system-wide audit. Produces a categorised report and proposes fixes. |
| [session-close.prompt.md](session-close.prompt.md) | Structured end-of-session close-out: checksum, memory proposals, open threads, and pattern candidates. |
| [workstation-create.prompt.md](workstation-create.prompt.md) | Guided creation of a new workstation following the four-section pattern. |
| [voice-check.prompt.md](voice-check.prompt.md) | Screens a draft against your voice principles before you send or publish. |
| [memory-consolidation.prompt.md](memory-consolidation.prompt.md) | Walks an aging MEMORY.md and proposes dedup, stale removal, and promotions. |

## How to use

1. Open the prompt file you want.
2. Copy the prompt body: the section under `## Prompt`.
3. Paste into Claude Code or your Claude client.
4. Fill any bracketed inputs (file paths, drafts to check, workstation context).
5. Run.

## How to customise

Every prompt is plain Markdown. Edit the prompt body freely. The voice-check and memory-consolidation prompts reference file paths: replace those with your own. The session-close prompt is the most opinionated; soften the four-block structure if you want a less rigorous close-out.

Each prompt has a `How to customise` section at the bottom with specific suggestions for adapting it to your own workflow.

## Why these five

These cover the operating system's core working cycles:

- Audit: periodic compliance check.
- Session close: daily hygiene.
- Workstation create: structural growth.
- Voice check: content quality gate.
- Memory consolidation: periodic cleanup.

You will likely add others over time. Keep one file per prompt. Keep the structure consistent (title, "use this when," prompt body, customisation notes). If a prompt grows past two pages, that is a sign it should be split, not extended.
