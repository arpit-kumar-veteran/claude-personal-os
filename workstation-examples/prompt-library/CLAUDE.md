# Prompt Library

## Identity

This workstation is a registry and execution layer for reusable, high-leverage prompts — named workflows you run repeatedly enough that they deserve a stable definition. Route here when you name a use case by its prompt title or say "run the [name] prompt." Each prompt is a standalone `.md` file in `prompts/`. Do not route here for one-off tasks that do not match an existing prompt — those stay in the relevant workstation.

When a prompt is invoked, read the matching `.md` file, fill the variables provided, and execute. If a prompt is a placeholder with no body yet, surface that and ask whether to populate it now or skip.

## Resources

| Resource | Read when... |
|---|---|
| `prompts/01-content-performance-analyzer.md` | Analysing content or post analytics performance |
| `prompts/02-batch-document-generator.md` | Generating batched outputs (summaries, proposals, cover letters) at scale |
| `prompts/03-meeting-prep-from-calendar.md` | Preparing for a client meeting, interview, or important call |
| `prompts/04-transcript-to-strategy-engine.md` | Turning a recording, podcast, or debrief into a strategy document |
| `prompts/05-file-organization-system.md` | Organising documents, research notes, or project files |
| `prompts/06-competitive-intelligence-report.md` | Running a scan on a competitor, target employer, or market player |
| `prompts/07-email-outreach-generator.md` | Drafting cold or warm outreach at scale |
| `prompts/08-weekly-operations-prep.md` | Weekly pipeline review, monitoring, and prep schedule |
| `prompts/09-content-repurposing-pipeline.md` | Turning long-form content into posts, newsletters, or talking points |
| `prompts/10-research-synthesis-report.md` | Deep-dive research or pre-meeting investigation |
| `prompts/11-pipeline-analyzer.md` | Reviewing a deal pipeline, tracker, or performance dataset |
| `prompts/12-personal-brand-campaign-builder.md` | Planning a 30-day content campaign across channels |

## Workflow

1. Identify the prompt by name or use case.
2. Read the matching `prompts/*.md` file from the Resources table.
3. If the file is a placeholder with no body yet, confirm whether to populate it now or skip.
4. Ask for any variables the prompt requires: audience, target list, date range, etc.
5. Execute the prompt. Match voice principles and the prompt's own editorial rules.
6. Route the output to the relevant downstream workstation. Do not leave outputs in prompt-library itself.

## Editorial Rules

Follow the central voice rules in `00_Resources/voice-principles.md` (or your equivalent voice file).

- Prompts execute consistently. If a prompt has its own editorial rule, follow it exactly — do not improvise.
- Cite sources for any market figure, benchmarked claim, or named-counterparty assertion. Apply the confidence-level rule.
- For content outputs: blunt, opinionated, first-person. No buzzwords, no hedging.
- For research outputs: lead with the answer, then context, then sources.
- When a prompt produces output that will be reused, save it to the relevant workstation — not here.
