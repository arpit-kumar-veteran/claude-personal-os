# Getting Started

This guide walks you through deploying the personal AI operating system pattern on your own machine. It is written for a non-coder. The longest single step is reading this guide.

## Prerequisites

You need:

- The Claude desktop app installed (Claude Code or the equivalent client).
- Python 3.10 or higher.
- A folder on your machine that will host your operating system.
- A GitHub account (optional, only if you want to fork this repository).

Total prerequisites install time: 5 minutes if you already have Python and Claude installed, 20 minutes if you do not.

## Quick start (10 minutes)

The fastest path to a working system:

1. Clone the repository:
   ```
   git clone https://github.com/arpitkumar007/personal-ai-operating-system.git
   cd personal-ai-operating-system
   ```
2. Copy the root template files into a new working folder:
   ```
   mkdir ~/my-ai-os
   cp templates/CLAUDE.md.template ~/my-ai-os/CLAUDE.md
   cp templates/MEMORY.md.template ~/my-ai-os/MEMORY.md
   ```
3. Open `~/my-ai-os/` in Claude Code.
4. Tell Claude: "Read CLAUDE.md and walk me through every `{{REPLACE: ...}}` marker. Ask me one question per marker and write my answer in."
5. Claude goes through each placeholder. Answer each one. The file fills in.

You now have a working root governance file personalised to you. Workstations come next.

## Full install (30 minutes)

The full install creates the root files plus your first workstation.

1. Complete steps 1 through 5 of Quick start above.
2. Pick your first workstation. Common starting choices are `career`, `finance`, `health`, or `meetings`. Pick whichever domain is most active for you.
3. Create the workstation folder:
   ```
   mkdir ~/my-ai-os/[name]
   cp templates/workstation/CLAUDE.md.template ~/my-ai-os/[name]/CLAUDE.md
   cp templates/workstation/MEMORY.md.template ~/my-ai-os/[name]/MEMORY.md
   ```
4. Tell Claude: "I created the `[name]` workstation. Walk me through every `{{REPLACE: ...}}` marker in its CLAUDE.md and MEMORY.md. Ask me one at a time."
5. Once filled, ask Claude to propose the new row for your root CLAUDE.md Routing Map. Approve it. Claude writes the row.
6. Optionally, copy `skills/audit-system.skill.md` into your working folder and personalise the `{{PATH_TO_OS_ROOT}}` placeholder. This is the audit skill referenced in ARCHITECTURE.md.

You now have a working operating system with one workstation. Add more workstations the same way as needed.

## Verifying your install

Three checks confirm the system is set up correctly.

1. Ask Claude: "Read my CLAUDE.md and tell me what workstations are listed in the routing map." Claude lists the workstations you created.
2. Ask Claude: "Run the audit on my OS." Claude walks your tree and produces a CRITICAL, WARNING, INFO report. If you only have one workstation, the report is short and mostly clean.
3. Open your root MEMORY.md. Confirm your Profile section reads correctly and your name appears where you placed it.

If all three pass, the install is working.

## Troubleshooting

The five most likely issues:

- **Claude does not see your files.** Confirm your working folder is the one you opened in Claude Code. Run `pwd` in a terminal at the folder to verify.
- **A `{{REPLACE: ...}}` marker remains after you thought you filled it.** Ask Claude to grep your files for `{{REPLACE`. Anything still there is unfilled.
- **The routing map points at a folder that does not exist.** Either create the folder or remove the row. The audit catches this automatically when you run it.
- **The Python scripts fail with "No module named pandas".** Run `pip install pandas openpyxl` in your terminal.
- **You broke a section in your CLAUDE.md.** The structure is load-bearing. Open `templates/CLAUDE.md.template` side by side and compare. The sections must match.

## Where to ask questions

Open an Issue on this repository. The issue template asks for context, expected behaviour, and what you tried. Use it.
