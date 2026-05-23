# Bootstrap: Personal Claude OS interactive setup

This is the master instruction file. When the user pastes a line like "Follow setup/bootstrap.md and walk me through setting up my own Personal Claude OS step by step," you (Claude) follow these phases in order.

## Operating principles for this entire flow

- Ask ONE question at a time. Wait for the answer. Never list five questions in one message.
- Use plain language. Assume the user has zero technical background.
- Confirm important decisions before writing files. "I am about to create a folder at `~/personal-claude-os/`. Sound good?"
- After every file write, tell the user exactly what changed. "I just created `~/personal-claude-os/CLAUDE.md` with your preferences."
- Never use jargon without explaining it the first time you use it.
- If the user seems lost, slow down, summarise where you are, ask if they want to continue or pause.
- Never write to any file outside the user's chosen OS folder.
- Never edit files in this template repository itself.

## Phase 1: Welcome and orient

Say (adapt to the user's tone, but keep this shape):

> Hi. I am going to set up your Personal Claude OS over the next 20 to 30 minutes. Here is what is going to happen:
>
> 1. I will offer you a chance to share files (LinkedIn, resume, pitch deck) so I can pre-fill some answers.
> 2. I will ask 15 to 25 short questions about you, your work, and how you want this system to behave. One question at a time.
> 3. I will suggest a name and location for your OS folder. You confirm or change.
> 4. I will create the folder and write your personalised files into it. I will tell you exactly what got written and where.
> 5. I will show you how to use the system from now on.
>
> You can pause any time. Just tell me. I will save your progress and resume where we left off when you come back.
>
> Ready to start?

WAIT for confirmation. If they want more context, give it. Do not proceed until they say yes.

## Phase 2: File ingestion

Say:

> Before the questions, do you have any of these files? It will save typing.
>
> - LinkedIn profile (PDF export from LinkedIn, or paste the URL)
> - Resume or CV (PDF or Word)
> - Pitch deck or one-pager about you or your work
> - Voice guide or style document you have written for yourself
> - Anything else that describes who you are or how you work
>
> Drag and drop into this chat now, or paste a URL. If you have nothing, just say "skip" and we will go through the questions.

WAIT. If files arrive, follow `setup/ingest.md` to read them. Tell the user what you extracted in plain language:

> I read your LinkedIn. I see you are a [role] at [company], with [X] years in [field], based in [city]. I will use this to pre-fill some of the upcoming questions, and you can correct anything that is wrong.

Save extracted facts to `setup/answers.md` as you go (this file is gitignored).

## Phase 3: Identity (5 questions)

Ask one at a time. Pre-fill from ingested files where possible. For pre-filled answers, present the value and ask "does this look right, or do you want to change it?".

1. What name should I use for you?
2. What is your primary role, or what do you spend most of your work time on?
3. What is the single biggest thing you want this OS to help you with?
4. Write me 2-3 sentences about yourself that a future Claude session should know. (Or say "use what you read from my files".)
5. Where on your computer should I create your OS folder? Suggest a default: `~/personal-claude-os/` on Mac or Linux, `C:\personal-claude-os\` on Windows. Confirm or change.

## Phase 4: Voice and preferences (4 questions)

1. How do you want me to write when I write on your behalf? Examples: professional, conversational, blunt, formal. Or describe in your own words.
2. How long should my responses be by default? Short (under 100 words), Medium (100-300 words), or Long (no limit).
3. Any words or phrases I should never use? Examples: jargon you dislike, common marketing-deck words, emojis, exclamation marks.
4. If you already have a voice guide file, point me at it. Otherwise skip.

## Phase 5: Workstations

Say:

> A workstation is one domain of your life that I help you manage. Common examples: career or job search, personal finance, health, meetings and notes, contacts, property, household operations. Each workstation is a folder with two files. You can have anywhere from 1 to 10. Most people start with 1 to 3 and add more once they get comfortable.
>
> Which 1 to 3 domains do you want to start with?

WAIT.

For each workstation chosen, ask:

A. What does this workstation cover? One paragraph. What goes in, what does not go in.
B. What is the main task you want help with in this workstation?
C. Any files, links, or resources I should know about for this workstation? Skip if none.

## Phase 6: Cadence (3 questions)

1. Do you want a weekly automated audit that checks for drift in your OS? Recommend: yes.
2. What day and time should the audit run? Suggest: Friday at 10:00.
3. Do you want a session-close routine at the end of each working session? It reviews what changed, proposes memory updates, and lists open threads. Recommend: yes.

## Phase 7: Confirm and create

Before writing anything, summarise:

> Here is what I am about to create for you:
>
> - A new folder at `[path]`.
> - A root `CLAUDE.md` with your voice, preferences, and routing map.
> - A root `MEMORY.md` with your profile and what I learned from your files.
> - `[N]` workstation folder(s) for `[list of workstation names]`, each with their own CLAUDE.md and MEMORY.md.
> - A weekly audit reminder.
>
> Should I create all of this now?

WAIT for explicit yes.

Then create the files in this order:

1. The OS root folder.
2. Root `CLAUDE.md` (filled in from templates/CLAUDE.md.template).
3. Root `MEMORY.md` (filled in from templates/MEMORY.md.template).
4. For each workstation: the folder, the workstation CLAUDE.md, the workstation MEMORY.md.
5. Optional: copy `skills/audit-system.skill.md` into the new folder with `{{PATH_TO_OS_ROOT}}` replaced.

After each file write, say:

> Created `[path]`. It has `[brief description of what is in it]`.

## Phase 8: Show and explain

When all files are created, say:

> Done. Your Personal Claude OS is at `[path]`.
>
> Here is how to use it from now on:
>
> 1. To start any session: open the folder in Claude Code and say "hi". I will read your CLAUDE.md and MEMORY.md and know who you are.
> 2. To save something new: say "remember this" and tell me. I will propose where to save it and wait for your approval.
> 3. To run the weekly audit: say "run the audit".
> 4. To add another workstation: say "create a new workstation for [domain]".
>
> Want me to do a quick demo of any of these? Or shall we wrap here?

If the user wants a demo, do it. Use their actual files. Show, do not just describe.

## Phase 9: Save and exit

Whether they wanted a demo or not, before closing, save a setup log to `[their-folder]/setup-log.md` with:

- Date and time of setup
- Files ingested (filenames only, never their contents)
- Decisions made (workstations, cadence, voice rules)
- Path to the new OS folder

Print the path one more time so they have it for next time. Done.

## Recovery: resuming a paused setup

If the user pauses mid-flow and comes back later in a new session, they can paste:

> Resume my Personal Claude OS setup. Read setup/answers.md if it exists and tell me where we left off.

You should:

1. Read `setup/answers.md` to see what is already captured.
2. Tell the user the current state. "You answered through Phase 4. We were about to start Phase 5 (workstations)."
3. Continue from the next unanswered question.

## Notes

- `setup/answers.md` is gitignored. It never gets committed.
- The user owns every file you create. They can edit anything by hand at any time.
- If at any point the user asks you to do something this bootstrap does not cover, defer to them. Do not invent steps.
