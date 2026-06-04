# Integrations

Which external tools connect to which workstations, and what each one adds.

This file is a reference, not a setup guide. It describes what becomes possible when you connect a tool. None of these integrations are required. The OS works without any of them.

## What integrations do

By default, Claude works with files in your OS folder. Integrations extend that: they let Claude read from and act on tools you already use (your email, calendar, note-taking app, broker account). Each integration is a connection between a workstation and a live data source.

The principle: only connect tools that are already part of your workflow. Do not add an integration to use a new tool. Add an integration to get more from a tool you already use.

## Meeting tools

**Granola (AI meeting notes)**
Route to: meeting-hq
Adds: automatic transcript capture and structured meeting summaries delivered to the workstation without manual copy-paste.

**Notion**
Route to: meeting-hq, any workstation that tracks projects or decisions
Adds: two-way sync between workstation MEMORY.md and a Notion database. Useful when you share context across a team.

## Communication

**Gmail / Google Workspace**
Route to: email-hq
Adds: Claude can read thread history before drafting. Removes the need to paste email context manually.

**Calendar (Google Calendar or equivalent)**
Route to: meeting-hq, career-hq
Adds: Claude can check your schedule when proposing meeting times or reviewing what is coming up.

## Finance

**Brokerage or portfolio app** (e.g. Kite, INDmoney, Robinhood, or similar)
Route to: finances workstation (advanced tier)
Adds: live portfolio data without manual export. Claude can read current positions and prices.

Note: integrations to financial tools are read-only by default. Never allow a connector to execute trades or move money on your behalf.

## Productivity and knowledge

**Figma**
Route to: brand-hq, any workstation that produces visual assets
Adds: Claude can read designs and generate visual artefacts directly.

**Apify / web scrapers**
Route to: any workstation that needs external data (career-hq for job listings, intel-hq for market signals)
Adds: structured web data pulled into the OS without manual research.

## Security note

Every MCP integration carries a small risk of indirect prompt injection: malicious content in a document, email, or web page processed by an integration can embed hidden instructions. Before connecting any tool:

1. Only connect to data sources you trust.
2. Scope access to the minimum required (read-only where possible).
3. If an integration produces unexpected instructions, disconnect it and investigate before reconnecting.

## Setting up integrations

MCP integrations are configured in your Claude app, not in this folder. The steps differ slightly per app:

- **Claude Cowork:** use the Integrations panel in the app settings.
- **Claude Code:** add MCP server definitions to your `.claude/settings.json` file.

Refer to the Claude documentation for current setup steps. The connection method may change between versions.
