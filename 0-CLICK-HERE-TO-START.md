# Start Here

You downloaded Personal Claude OS. Three steps.

---

## Step 1: Open this folder in your Claude app

This works on the **Claude Pro plan ($20/month)**. If you do not have a Claude account yet, go to `claude.ai`, sign up, and upgrade to Pro. That is all you need.

Pick the path that matches how you use Claude:

---

### Path A: Claude desktop app — recommended for most people

The Claude desktop app is the smoothest path. It is included in your $20 Pro plan.

1. Download the Claude desktop app from `claude.ai/download` if you do not have it already.
2. Open the app and sign in.
3. In the left sidebar, find **Projects** and create a new one. Give it any name — "Personal Claude OS setup" works.
4. Inside the project, look for an option to **add files** or **upload context**. Upload everything from the `claude-personal-os-main` folder you unzipped.
5. Start a new conversation inside that project. You will see the files are active as context.

You are ready. Go to Step 2.

---

### Path B: Claude.ai web — also works on Pro

1. Go to `claude.ai` in your browser and sign in.
2. In the left sidebar, click **Projects** and create a new project.
3. Inside the project, upload the files from the `claude-personal-os-main` folder using the file upload option.
4. Open a conversation inside that project.

**Note:** You cannot drag a folder directly into the web chat window — it will not work. Use Projects, as described above.

---

### Path C: Claude Code (developers only, API credits required)

Claude Code is a separate developer tool that bills on API usage — it is not included in the $20 Pro plan.

- **Claude Code desktop:** Open the app. File → Open Folder → pick `claude-personal-os-main`. `CLAUDE.md` loads automatically.
- **Claude Code CLI:** Open your terminal, navigate into the folder (`cd claude-personal-os-main`), and run `claude`.

---

You will know it worked when Claude is active, the files are in context, and you are ready to chat.

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

The setup takes about 30 minutes. You can pause at any point.

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

---

## What you end up with

A folder on your computer — you choose where — that contains your personal AI operating system:

- **`CLAUDE.md`** — your voice, preferences, and routing map. Claude reads this at the start of every session.
- **`MEMORY.md`** — your profile and the facts Claude remembers about you. Grows session by session.
- **1-3 workstation folders** — rules and memory for the domains you chose (job search, finance, health, meetings, etc.).
- **A weekly audit** — say "run the audit" any time. Claude checks that everything is correctly structured and reports back.

The folder belongs to you. No cloud service, no subscription, no app required to use it. Edit files directly anytime, or ask Claude to edit on your behalf (it will always show you what it intends to change and wait for a yes).

---

## If something is not working

Tell Claude exactly what you saw and what you expected. Claude will diagnose. If you cannot get past Step 1, open an issue at `https://github.com/arpit-kumar-veteran/claude-personal-os/issues` and paste a screenshot of what you are seeing.

---

When you are ready, do Step 1. Then type `start`.
