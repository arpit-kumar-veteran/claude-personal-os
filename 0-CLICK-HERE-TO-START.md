# Start Here

You downloaded Personal Claude OS. Three steps.

---

## Step 1: Open this folder in your Claude app

This works on the **Claude Pro plan ($20/month)**. If you do not have a Claude account yet, go to `claude.ai`, sign up, and upgrade to Pro. That is all you need.

Pick the path that matches your setup:

---

### Path A: Claude desktop app via Cowork — recommended for everyone

The easiest path. Works on the $20 Pro plan. No technical knowledge needed.

**On macOS:**
1. Download the Claude desktop app from `claude.ai/download` if you do not have it.
2. Open the app and sign in.
3. In the **top left corner**, click the **Cowork** tab.
4. Look for the attachment or upload icon in the chat area. Click it, then select the `claude-personal-os-main` folder you unzipped. If it does not accept a whole folder, open the folder first and select all the files inside it (press Cmd+A to select all, then attach). Wait until you see the files listed as attached in the chat.
5. Type `start` in the chat.

**On Windows:**
1. Download the Claude desktop app from `claude.ai/download` if you do not have it.
2. Open the app and sign in.
3. In the **top left corner**, click the **Cowork** tab.
4. Look for the attachment or upload icon in the chat area. Click it, then select the `claude-personal-os-main` folder you unzipped. If it does not accept a whole folder, open the folder first and select all the files inside it (press Ctrl+A to select all, then attach). Wait until you see the files listed as attached in the chat.
5. Type `start` in the chat.

---

### Path B: Claude Code via the Claude desktop app — macOS only

Use this if you already have the Claude desktop app and want the Claude Code experience with the folder auto-loaded.

**On macOS:**
1. Open the Claude desktop app.
2. In the **top left corner**, switch to the **Claude Code** tab.
3. Open the `claude-personal-os-main` folder — `CLAUDE.md` loads automatically.
4. Type `start`.

**On Windows:** Claude Code is not available inside the Claude desktop app on Windows. Use Path A or Path C instead.

---

### Path C: Claude Code via the terminal — advanced, for coders only

This path requires comfort with the command line. It bills on API usage — not included in the $20 Pro plan.

**On macOS:**
1. Open Terminal.
2. Run: `cd ~/Downloads/claude-personal-os-main` (adjust the path to wherever you unzipped the folder).
3. Run: `claude`
4. Type `start`.

**On Windows:**
1. Open Command Prompt or PowerShell.
2. Run: `cd C:\Users\YourName\Downloads\claude-personal-os-main` (adjust to wherever you unzipped).
3. Run: `claude`
4. Type `start`.

If you do not have Claude Code installed, run `npm install -g @anthropic-ai/claude-code` first (requires Node.js).

---

You will know it worked when Claude is active, reads the setup context, and is ready to chat.

---

## Step 2: Type `start`

In the chat box, type the word `start` and press Enter. Nothing else. Just that word.

Claude will take it from here.

---

## Step 3: Follow Claude's lead

Claude will guide you through the entire setup. Here is what to expect:

- **Every response tells you what just happened** — what was captured, what was created.
- **Every response tells you what comes next** — the next phase, how many questions.
- **Every response ends with a trigger word** — usually **continue**. Type it to move forward. You will never be left wondering what to type.
- **If you go off-track** — ask a question, share something, go on a tangent — Claude will answer and then bring you back with a clear "Back to setup: [where we are]."
- **If you stop midway** — close the app, come back tomorrow — type `start` again. Claude will find your progress and resume from where you left off.

The setup takes about 35 minutes. You can pause at any point.

---

## What the setup covers

Claude walks you through these phases, one at a time:

| Phase | What happens | Time |
|---|---|---|
| 1. Welcome | Claude explains what a Personal AI OS is and shows the full setup roadmap. You know the whole journey before step one. | 1 min |
| 2. File drop | Share your LinkedIn PDF, resume, or any doc. Claude reads it and skips questions it can already answer. Optional. | 2-5 min |
| 3. Identity | 5 questions. Your name, role, what you want this OS to help with most — and where on your computer to build your OS. Claude walks you through how to choose the right root folder before asking. | 5 min |
| 4. Voice | 4 questions. How you want Claude to write on your behalf, response style, things to avoid. | 3 min |
| 5. Workstations | Claude shows all 16 available workstations with descriptions. Recommends 2-3 based on your answers. You pick which to install. | 5 min |
| 6. Cadence | 3 questions. Weekly audit, session-close routine. | 2 min |
| 7. Build | Claude creates your OS folder, fills in your files. Tells you exactly what was created and where. | 5 min |
| 8. Handoff | What was built, how to use it from now on, three things to try immediately. | 2 min |
| 9. Skills | Claude opens the Skills Catalog and recommends 2-3 skills matched to your workstations. You choose: install now, bookmark for later, or skip entirely. Skills can always be added after setup — this phase is optional. | 3-5 min |

---

## What you end up with

A folder on your computer — you choose where — that contains your personal AI operating system:

- **`CLAUDE.md`** — your voice, preferences, and routing map. Claude reads this at the start of every session.
- **`MEMORY.md`** — your profile and the facts Claude remembers about you. Grows session by session.
- **1-3 workstation folders** — rules and memory for the domains you chose (job search, finance, health, meetings, etc.).
- **A `skills/` folder** — ten core skills pre-installed: session-close, audit-system, deep-research, humanizer, and more. Add community skills any time.
- **A weekly audit** — say "run the audit" any time. Claude checks that everything is correctly structured and reports back.

The folder belongs to you. No cloud service, no subscription, no app required to use it. Edit files directly anytime, or ask Claude to edit on your behalf (it will always show you what it intends to change and wait for a yes).

---

## If something is not working

Tell Claude exactly what you saw and what you expected. Claude will diagnose. If you cannot get past Step 1, open an issue at `https://github.com/arpit-kumar-veteran/claude-personal-os/issues` and paste a screenshot of what you are seeing.

---

When you are ready, do Step 1. Then type `start`.
