# File ingestion guide

When the user shares a file during bootstrap, follow this protocol.

## What to read

| File type | What to extract |
|---|---|
| LinkedIn PDF export | Name, headline, current role, employer, years of experience, key skills, location (city or region only) |
| LinkedIn URL | Same as above. Use WebFetch if available; otherwise ask the user to paste an export or summary. |
| Resume or CV (PDF or Word) | Same as LinkedIn, plus education, certifications, notable projects |
| Pitch deck | Company name, value proposition, target market, the user's role in the company |
| Voice guide | All rules and examples. Store the file path so you can reference it later. Do not try to memorise the entire contents. |
| Generic "about me" document | Whatever the user wrote. Take it at face value. |

## What to do with what you read

1. Acknowledge in plain language what you found. "I read your LinkedIn. You are a `[role]` at `[company]`, with `[X]` years in `[field]`."
2. Pre-fill the answers to upcoming interview questions with what you extracted.
3. When you reach a question that you have pre-filled, show the pre-filled answer and ask: "Does this look right, or do you want to change it?"
4. Never assume something not in the document. If LinkedIn does not say their preferred tone, ask. Do not guess.

## What NOT to extract

Default privacy-conservative:

- Phone numbers
- Email addresses
- Home street address (city or region OK; specific street or apartment not OK)
- Salary figures
- Names of family members (unless the user is creating a workstation specifically about a family member's care)
- Anything tagged "confidential" or "private"

The user can override any exclusion. But default is privacy-conservative. If unsure, ask: "I see X in your file. Want me to record it, or skip it?"

## After bootstrap

The ingested files stay in the user's chat session. They are not copied into the OS folder. The OS folder holds only what the user explicitly chose to record there.

The setup-log written at the end records only the filenames of ingested files, never their contents.

## Boundaries

- Never share an extracted fact across chat sessions unless the user explicitly saved it to MEMORY.md.
- Never email, post, or otherwise transmit any extracted content anywhere.
- If a file looks like it contains another person's private data (e.g., the user shared their team's contact list by mistake), surface the concern and ask before reading further.
