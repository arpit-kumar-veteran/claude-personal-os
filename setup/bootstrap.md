# Bootstrap: Personal Claude OS guided setup

This is the master instruction file for the setup flow. When the user types "start", follow these phases in order, without skipping any.

The rules governing this entire session are in the root `CLAUDE.md`. Read it before beginning. Key points:
- One question at a time. Always.
- Every response ends with a trigger word (**continue** by default).
- Every phase ends with a summary block before the next phase begins.
- If the user goes off-topic, answer briefly, then re-anchor with "Back to setup: [phase, question, restate]."
- Track which phase and question you are on. If the user returns after a break, tell them exactly where they left off.

---

## Phase 1: Welcome and roadmap

Say exactly this (adapt tone slightly to match the user, but keep this structure):

> Hi. I am Claude, and I am going to set up your Personal Claude OS over the next 30 minutes.
>
> **What is a Personal AI OS?** It is a folder on your computer that tells Claude who you are, how you work, and what you are working on. Instead of starting every conversation from zero, Claude reads your files at the start of each session and already knows your context, your rules, and your open threads. The folder is your operating system. It lives on your machine, not in any cloud service, and it belongs entirely to you.
>
> Before the first question, here is the full picture of what we are doing together — so you know exactly where we are headed at every step:
>
> **Phase 1 — Welcome (now):** I show you the roadmap. You know what is coming before we start.
>
> **Phase 2 — File drop (optional, 2-5 min):** You can share your LinkedIn PDF, resume, or any document that describes you. I read it and use it to pre-fill answers, so you type less.
>
> **Phase 3 — Identity (5 questions, ~5 min):** I learn who you are, what you do, and what you want this OS to help you with most.
>
> **Phase 4 — Voice and preferences (4 questions, ~3 min):** I learn how you want me to write on your behalf, and what to avoid.
>
> **Phase 5 — Workstation selection (~5 min):** I show you all 16 available workstations — domains of your life I can help you manage. Based on what you told me in Phases 3 and 4, I recommend 2 to 3. You pick 1 to 3 to install.
>
> **Phase 6 — Cadence (3 questions, ~2 min):** I set up a weekly audit and a session-close routine.
>
> **Phase 7 — Build (~5 min):** I create your OS folder, fill in your files, and tell you exactly what was created and where.
>
> **Phase 8 — Handoff:** Your OS is live. I show you what was built and give you three things to try immediately.
>
> A few things to know before we start:
> - I will ask one question at a time. Answer in plain English. No right or wrong answers.
> - At the end of every phase I will summarise what was captured and tell you what comes next.
> - At the end of every response you will see a trigger word — usually **continue**. Type it to move forward. You never have to guess what to say next.
> - You can pause any time. If you stop and come back later, type **start** again. I will find your progress and resume from where you left off.
> - If you want to ask me something in the middle of setup, go ahead. I will answer and then bring us back to where we were.
>
> Ready?
>
> → Type **continue** when you are ready to begin.

WAIT. Do not proceed until the user responds. If they ask questions, answer them. Then re-anchor with the trigger.

---

## Phase 2: File ingestion

Say:

> Before the questions, do you have any of these?
>
> - LinkedIn profile (PDF export from LinkedIn, or paste your LinkedIn URL)
> - Resume or CV (PDF or Word)
> - Pitch deck or bio that describes your work
> - A voice guide or writing style document you use
> - Anything else that describes who you are
>
> Drag and drop files into this chat now, or paste a URL. If you have nothing ready, just type **skip** and we move straight to the questions.

WAIT. If files arrive, follow `setup/ingest.md` to read them. Then say:

> I read your [document name]. Here is what I found:
> - [Name / role / company / years of experience / location — pull what is there]
> I will use this to pre-fill some of the upcoming questions. You can correct anything that looks wrong.
>
> → Type **continue** to start the questions.

Save all extracted facts to `setup/answers.md` (this file is gitignored — it never leaves the user's machine).

If they skipped, say:

> No problem. We will go through everything in the questions.
>
> → Type **continue** to start.

---

## Phase 3: Identity — 5 questions

Say before the first question:

> **Phase 3 of 8 — Identity**
> 5 short questions. I am learning who you are and what you want this OS to help you with.

Then ask one question at a time. If you pre-filled an answer from ingested files, present the value and ask "Does this look right, or do you want to change it?"

**Question 3.1:**
> What name should I use for you?

**Question 3.2:**
> What is your primary role, or what do you spend most of your work time doing?

**Question 3.3:**
> What is the single biggest thing you want this OS to help you with?

**Question 3.4:**
> Write me 2 to 3 sentences about yourself that a future Claude session should know — your background, what you are working on, what matters to you. (Or say "use what you read from my files".)

**Question 3.5 — choosing your root folder**

Before asking, say this:

> **One decision that deserves a moment of thought: where your OS lives.**
>
> Your Personal AI OS is not an app. It is a folder. That folder is the entire operating system. Every session, when you open it in Claude, two files inside it are read automatically — `CLAUDE.md` (your preferences and rules) and `MEMORY.md` (your profile and remembered facts). Your workstations are subfolders inside the same root. Everything compounds from this one location.
>
> This means a few things for how you choose it:
>
> **It should be permanent.** Claude will need to find this folder every session. Pick a location you will not move, delete, or restructure. Think of it like your home folder — it does not move.
>
> **It should be accessible.** You will open this folder every time you start a working session. `~/Documents/` or your home directory (`~/`) are ideal on Mac. A top-level folder on `C:\` works well on Windows.
>
> **It should not be inside the repo you just downloaded.** That repo is the installer. Your OS is the output. Keep them separate.
>
> **Suggested names** — short, hyphenated, no spaces:
> - `personal-claude-os` (default, clear)
> - `my-claude-os`
> - `command-center`
> - `brain`
> - `my-os`
>
> **Good locations:**
> - Mac / Linux: `~/personal-claude-os/` or `~/Documents/personal-claude-os/`
> - Windows: `C:\personal-claude-os\` or `C:\Users\YourName\Documents\personal-claude-os\`
>
> **What to avoid:**
> - Paths with spaces (e.g., `My Folder/AI stuff`) — use hyphens instead
> - The Desktop — it gets cluttered and this folder is meant to be permanent
> - Deep nested paths buried inside project or work folders — this is a root-level thing, not a subfolder of something else
> - Inside a cloud sync folder you frequently wipe or restore — iCloud, Dropbox, and OneDrive are fine if you are careful, but know that your OS will sync to the cloud too
>
> You can move the folder later. If you do, just tell Claude the new path at the start of the next session.

Then ask:

> Where do you want your OS to live? You can accept the default or give me a custom path.
>
> Default: `~/personal-claude-os/` on Mac or Linux, `C:\personal-claude-os\` on Windows.

After all five answers are collected, emit the phase-end summary:

> ✓ **Phase 3 complete — here is what I captured:**
> - Name: [answer]
> - Role: [answer]
> - Primary goal for this OS: [answer]
> - About you: [answer]
> - OS folder location: [answer]
>
> **Next up — Phase 4:** 4 quick questions about how you want me to communicate on your behalf. Voice, length, things to avoid.
>
> → Type **continue** when ready.

WAIT.

---

## Phase 4: Voice and preferences — 4 questions

Say before the first question:

> **Phase 4 of 8 — Voice and preferences**
> 4 questions. I am learning how you want me to write when I write on your behalf.

Ask one at a time.

**Question 4.1:**
> How do you want me to write when I draft emails, messages, or documents for you? Examples: professional, conversational, blunt, formal, warm. Or describe it in your own words.

**Question 4.2:**
> How long should my responses be by default? Options:
> - Short (under 100 words — quick answers, no elaboration)
> - Medium (100 to 300 words — the default for most people)
> - Long (no limit — full detail every time)

**Question 4.3:**
> Any words, phrases, or habits I should never use? For example: jargon you dislike, filler phrases like "certainly" or "great question", emojis, exclamation marks. Type "none" if you have no restrictions.

**Question 4.4:**
> Do you already have a voice guide or writing style document? If yes, tell me where the file is and I will reference it. If not, type "no" and I will build voice rules from your answers here.

After all four answers, emit the phase-end summary:

> ✓ **Phase 4 complete — here is what I captured:**
> - Tone: [answer]
> - Default response length: [answer]
> - Words or phrases to avoid: [answer]
> - Voice guide: [yes/no and path if yes]
>
> **Next up — Phase 5:** The workstation catalog. I will show you all 16 available workstations and recommend which ones fit you based on what you just told me.
>
> → Type **continue** when ready.

WAIT.

---

## Phase 5: Workstation selection

Say before the catalog:

> **Phase 5 of 8 — Workstation selection**
>
> A workstation is one domain of your life that I help you manage — job search, personal finance, health, meetings, contacts. Each workstation is a folder with its own rules and memory. You can start with 1 to 3 and add more any time.
>
> Here are all 16 available workstations. I have marked the ones I recommend for you based on what you told me.

Then present the catalog. Use the interview answers from Phases 3 and 4 to determine which 2 to 3 to mark as recommended. Add a one-line "Why for you:" under each recommended one.

> ### Foundation workstations
> These seven cover the most common needs for any professional.
>
> | Workstation | What it covers |
> |---|---|
> | **career-hq** | Resume, cover letters, job applications, interview prep, outreach to employers and contacts |
> | **email-hq** | Email drafting, reply tone-matching, thread discipline, avoiding inbox overwhelm |
> | **brand-hq** | LinkedIn positioning, content creation, public identity — how you show up professionally online |
> | **meeting-hq** | Meeting notes, transcript capture, action item extraction, follow-up tracking |
> | **expense-hq** | Monthly burn tracking, bank and card reconciliation, spending category taxonomy |
> | **property-hq** | Property or asset management, maintenance tracking, cost records, tenant or rental admin |
> | **learning-hq** | Courses, books, skill development, personal knowledge capture |
>
> ### Advanced workstations
> Add these when a domain keeps coming up in sessions and Claude keeps losing context.
>
> | Workstation | What it covers |
> |---|---|
> | **thinking-hq** | Structured reasoning: coach mode, strategist mode, devil's advocate, big decisions |
> | **finances-hq** | Net worth, investments, FIRE planning, asset allocation, financial source-of-truth |
> | **health-hq** | Family health tracking, lab results, supplements, conditions — one folder for everyone |
> | **consulting-hq** | Freelance pipeline, proposals, client deliverables, billing and invoicing |
> | **venture-hq** | Side business or startup: co-founder search, market intel, investor conversations |
> | **life-transition-hq** | Relocation, career pivots, major decisions with long horizons and low reversibility |
> | **intel-hq** | Recurring newsletter and digest processing: extract signals, discard noise, route to right places |
> | **relationship-hq** | Personal CRM, network hygiene, follow-up cadence, conversation prep |
> | **content-hq** | Content pipeline: writing, repurposing, scheduling, cross-platform publishing |
>
> ---
> Based on what you told me, I recommend:
>
> ⭐ **[Recommended workstation 1]** — [one-sentence reason drawn from their interview answers]
> ⭐ **[Recommended workstation 2]** — [one-sentence reason]
> ⭐ **[Recommended workstation 3 if applicable]** — [one-sentence reason]
>
> Which 1 to 3 do you want to install? You can pick from my recommendations, choose others from the list, or mix. Just name them.

WAIT for the user's selection.

Once they confirm their selection, for each chosen workstation ask:

> For **[workstation name]**:
> Is there anything specific I should know about how you want to use this workstation — any files, links, tools, or rules I should build in from the start? Or say "use defaults" and I will set it up from the template.

After all workstation details are collected, emit the phase-end summary:

> ✓ **Phase 5 complete — here is what I captured:**
> - Workstations to install: [list]
> - Custom details: [summary per workstation, or "defaults" if they skipped]
>
> **Next up — Phase 6:** 3 short questions about your weekly rhythm — an automated audit and a session-close routine.
>
> → Type **continue** when ready.

WAIT.

---

## Phase 6: Cadence — 3 questions

Say before the first question:

> **Phase 6 of 8 — Cadence**
> 3 quick questions to set up your recurring routines.

**Question 6.1:**
> Do you want a weekly automated audit? It checks your OS for drift — missing memory entries, stale routing, uncaptured decisions — and proposes fixes. Takes about 5 minutes once a week. Recommended: yes.

**Question 6.2 (ask only if yes):**
> What day and time should the audit run? Default: Friday at 10:00 am. Change if you prefer.

**Question 6.3:**
> Do you want a session-close routine at the end of each working session? It reviews what changed during the session, proposes memory updates, and lists any open threads you should not forget. Recommended: yes.

After all answers, emit the phase-end summary:

> ✓ **Phase 6 complete — here is what I captured:**
> - Weekly audit: [on/off, day and time if on]
> - Session-close routine: [on/off]
>
> **Next up — Phase 7:** The build. I am going to create your OS folder and write all your files. I will show you exactly what I am about to create and wait for your yes before writing anything.
>
> → Type **continue** when ready.

WAIT.

---

## Phase 7: Confirm and create

Before writing a single file, emit the full confirmation:

> **Phase 7 of 8 — Build**
>
> Here is exactly what I am about to create for you:
>
> 📁 **New folder at:** `[path]`
>
> Inside it:
> - `CLAUDE.md` — your voice rules, preferences, routing map, and the [N] governance rules that protect your memory files.
> - `MEMORY.md` — your profile and everything I learned from our conversation today.
> - `[workstation-name]/` — [one-line description], with its own CLAUDE.md and MEMORY.md.
> - [repeat per workstation]
> - `skills/audit-system.skill.md` — the weekly audit routine, ready to run.
>
> Nothing is written until you say yes. Do you want me to create all of this now?

WAIT for explicit yes.

Then create files in this order:

1. The OS root folder.
2. Root `CLAUDE.md` — filled in from `templates/CLAUDE.md.template` with all answers from Phases 3-6.
3. Root `MEMORY.md` — filled in from `templates/MEMORY.md.template` with identity and profile.
4. For each workstation: the folder, then `CLAUDE.md` (from `workstation-examples/[name]/CLAUDE.md`), then `MEMORY.md` (from `workstation-examples/[name]/MEMORY.md`). Replace example content with the user's specifics where they provided them. Keep template defaults where they said "use defaults."
5. Copy `skills/audit-system.skill.md` into `[os-root]/skills/` and replace `{{PATH_TO_OS_ROOT}}` with the actual path.

After creating each file, say:

> ✓ Created `[path]` — [one-line description of what is inside].

After all files are written, emit:

> ✓ **Phase 7 complete — build done.**
>
> **Next up — Phase 8:** I show you what we just built and give you three things to try immediately.
>
> → Type **continue** when ready.

WAIT.

---

## Phase 8: Handoff

Say:

> **Phase 8 of 8 — Handoff**
>
> Your Personal Claude OS is live at `[path]`.
>
> Here is what we built together:
>
> - **`CLAUDE.md`** — Your voice, preferences, [N] governance rules, and routing map. Claude reads this at the start of every session.
> - **`MEMORY.md`** — Your profile and what Claude knows about you. This grows session by session as you say "remember this."
> - [For each workstation: **`[name]/`** — [one-line description of what was set up]]
> - **`skills/audit-system.skill.md`** — Run it any time by saying "run the audit."
>
> **Three things to try right now:**
>
> 1. Open your OS folder in Claude and say **"hi"**. Claude will greet you by name, describe what it knows about you, and ask what you want to work on.
> 2. Tell Claude something you want remembered. Say **"remember [fact]"**. It will propose exactly where to save it and wait for your approval before writing.
> 3. Say **"run the audit"**. Claude will check that your OS is correctly structured and report back in about 2 minutes.
>
> Your first-week guide is at `FIRST-WEEK.md` in the repository you downloaded. It has a day-by-day plan for the first 7 days.
>
> Want me to do a quick demo of any of these three things now, using your actual files?

WAIT. If they want a demo, do it with their real data. If they are done, proceed to Phase 9.

---

## Phase 9: Save and exit

Write a setup log to `[their-os-folder]/setup-log.md` with:

- Date and time of setup
- Files ingested (filenames only — never their contents)
- Decisions made: name, role, goal, voice rules, workstations chosen, cadence
- Path to the new OS folder

Then say:

> Your setup log is saved at `[their-os-folder]/setup-log.md`.
>
> Your OS is at `[path]`. Next time you work, open that folder in Claude — not this one — and say "hi."
>
> You are done. Welcome to your Personal Claude OS.

---

## Recovery: resuming an interrupted setup

If the user returns after stopping mid-setup and types **start**:

1. Check whether `setup/answers.md` exists and read it.
2. If it does, say: "Welcome back. You got as far as [phase name], question [N]. Here is what I captured so far: [summary]. Ready to continue from [next question]?"
3. Continue from the next unanswered question with the standard trigger-word format.

If `setup/answers.md` does not exist, begin from Phase 1 and explain that no saved progress was found.

---

## Notes for Claude

- `setup/answers.md` is gitignored. It is never committed to the repository.
- Never modify files in the `claude-personal-os` repo folder. All writes go to the user's OS folder.
- The user owns every file created. They can edit anything by hand at any time.
- If the user asks you to do something not covered by this bootstrap, defer to them. Do not invent phases.
- The workstation examples in `workstation-examples/` are the source templates. Read the relevant one before writing a workstation's files.
