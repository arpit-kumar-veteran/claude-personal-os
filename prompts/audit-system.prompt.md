# Prompt: Audit the OS

**Use this when:** you want to manually trigger a system-wide audit without invoking the registered skill. Useful during development of new rules, when testing audit logic, or when you want the audit on demand outside its scheduled cadence.

## Prompt

You are auditing my personal AI operating system. Walk the file tree starting at the OS root and produce a categorised report with three sections: CRITICAL, WARNING, INFO.

CRITICAL findings:
- Any workstation folder missing CLAUDE.md or MEMORY.md.
- Any workstation CLAUDE.md missing one of the four required sections in order: Identity, Resources, Workflow, Editorial Rules.
- Any MEMORY.md missing its header line or required Contacts and Key Decisions sections.
- Any file containing tokens from the personal-information blocklist (phone, email, account numbers, PAN, Aadhaar, residential address).

WARNING findings:
- Any row in the Routing Map without a matching folder on disk.
- Any folder on disk without a matching row in the Routing Map.
- Any CLAUDE.md over its declared line limit.
- Any MEMORY.md containing change logs, version notes, or duplicate facts.
- Any path referenced in a Resources table that does not exist.

INFO findings:
- MEMORY.md last-updated date older than the expected cadence.
- Skills referenced in skills-index.md that do not exist on disk.
- Two workstations with overlapping Identity scope.

For each finding state three fields, pipe-separated. `file:line` | the problem in one sentence | the suggested fix in one sentence.

Do not modify any file. The audit is read-only. Propose edits only; wait for approval before any write.

If a section has no findings, write "None." Do not invent findings to fill a section. An empty section is the goal.

After the report, ask whether to walk the CRITICAL findings one by one for fixes.

## How to customise

- Add domain-specific checks under WARNING (e.g., a finance workstation may need "every account in the holdings file has a matching tax category").
- The personal-information blocklist is yours to define. Keep it in a separate file referenced by the root CLAUDE.md and the audit will load it dynamically.
- Adjust the cadence threshold under INFO to match your own review rhythm.
