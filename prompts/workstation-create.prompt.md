# Prompt: Create a new workstation

**Use this when:** you want to spin up a new workstation following the system's four-section pattern, and you want the structure enforced from the first file.

## Prompt

I want to create a new workstation. Walk me through the standard pattern, one question at a time. Do not ask all questions at once.

Ask me in this order:

1. The workstation name (folder name, kebab-case, lowercase).
2. The Identity. One paragraph: what this workstation does, what routes here, what does not. Probe for the boundary explicitly: what counter-example does NOT belong here. If I give a vague answer, push back with one clarifying question. Specificity is the point.
3. The first set of Resources. Paths or URLs this workstation should read, with a trigger condition for each. Can be empty for now.
4. A Workflow of 3 to 7 steps for the primary task this workstation will handle. Each step in action form.
5. Three to five Editorial Rules specific to this domain, on top of the central voice rules.

After collecting all answers, propose the exact contents of two files:

- `[workstation-name]/CLAUDE.md`: with sections Identity, Resources, Workflow, Editorial Rules in that order.
- `[workstation-name]/MEMORY.md`: with header `[Workstation Name] Memory`, last-updated line, and sections Contacts and Key Decisions.

State both file paths and the full proposed contents inline. Wait for explicit approval before writing.

After approval, write both files. Then propose the exact diff for the root CLAUDE.md Routing Map: the new row to add: and wait for approval again before writing.

After both writes, run the audit skill against the new workstation and report any structural issues immediately.

## How to customise

- If you want a third file (a domain-specific reference or starter script), add it as step 6 and write it alongside the two governance files.
- If your routing map lives somewhere other than the root CLAUDE.md, point this prompt at the right file.
- If you have a naming convention for workstations (prefix, suffix, character limit), state it at the top so the prompt enforces it.
