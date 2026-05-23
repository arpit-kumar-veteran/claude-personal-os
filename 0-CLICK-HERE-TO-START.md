# Start Here

You just downloaded Personal Claude OS. This file walks you through setting up your own copy in about 30 minutes. You do not need to be a coder. You will not type a single line of code.

## What you need first

1. **A Claude desktop app installed.** See "Pick your Claude app" below for the three options.
2. **This folder on your computer.** If you used `git clone`, you already have it. If you don't know what git is, see "Two ways to download this" below.
3. **30 to 45 minutes of quiet time.** You can pause and resume any time.

That's the whole list. No Python required. No GitHub account required.

## Pick your Claude app

There are three ways to talk to Claude on your computer. Pick the one that matches your comfort level.

### Option 1 (Recommended for everyone): Claude Cowork desktop app

**Best for:** non-coders, first-time users, anyone who wants the smoothest experience.

Claude Cowork is the app Anthropic built specifically for people doing real work who are not writing code. It has the friendliest interface, the cleanest file handling, and the best support for the skills and plugins this OS uses.

If you don't have it installed yet, download from `claude.com` and pick the Cowork desktop app. Install, sign in, and you are ready.

This is the recommended path. The rest of this guide assumes you are using Cowork unless you tell Claude otherwise.

### Option 2: Claude Code desktop app

**Best for:** people who already have Claude Code installed for other work, or who prefer its slightly more developer-oriented interface.

Claude Code is also a desktop app. It originated for software development but works for any task. The setup flow works the same way.

If you don't have it installed yet, download from `claude.com/code`.

### Option 3 (Developer only): Claude Code CLI

**Not recommended for non-technical users.** This option requires you to be comfortable with the terminal and basic command-line work.

The Claude Code CLI runs in your terminal. You install it via `npm install -g @anthropic-ai/claude-code` (you need Node.js installed first), then run `claude` inside the folder.

If you are not sure what any of the above sentence means, skip this option entirely and use Option 1 or Option 2. There is no functional difference in the end result.

## Two ways to download this folder

Both options below give you the same folder. Pick whichever feels easier.

### Easy way (no git knowledge needed)

1. Go to `https://github.com/arpit-kumar-veteran/claude-personal-os`
2. Click the green **Code** button near the top right of the file list.
3. Click **Download ZIP**.
4. Unzip the downloaded file. You will get a folder called `claude-personal-os-main` (or similar).
5. Move that folder somewhere you can find again. `~/Documents/` works fine.

### Developer way (if you already know git)

```
git clone https://github.com/arpit-kumar-veteran/claude-personal-os.git
```

## The three steps

### Step 1: Open this folder in your Claude app

The mechanics are slightly different per app, but the idea is the same: tell your Claude app that you want to work inside the folder you just downloaded.

- **In Claude Cowork:** open the app, then point it at the folder you downloaded. Cowork will read the files in the folder so it knows the context.
- **In Claude Code desktop:** launch the app. From the top menu choose **File** > **Open Folder**. Pick the folder you downloaded (`claude-personal-os-main` or `claude-personal-os`).
- **In Claude Code CLI:** in your terminal, `cd` into the folder and run `claude`.

You should see a list of files in the app. If you see `README.md`, `0-CLICK-HERE-TO-START.md` (this file), and a few folders, you are in the right place.

### Step 2: Paste this single line

In the chat box, paste this exactly:

> Follow setup/bootstrap.md and walk me through setting up my own Personal Claude OS step by step.

Press enter.

### Step 3: Answer Claude's questions

Claude will now:

1. Introduce itself and explain what's about to happen.
2. Offer you a chance to share files (LinkedIn PDF, resume, pitch deck, voice guide, anything that describes you or your work). You can drag and drop them into the chat. Claude will read them and use what it finds to skip questions later.
3. Ask you 15 to 25 short questions, one at a time. Plain English. You answer in the chat.
4. Suggest a name and location for your personal OS folder.
5. Show you exactly what it's about to create. You approve before anything is written.
6. Create the folder, fill in the templates with your answers, set up your first workstation.
7. Tell you exactly what was created, where, and how to use it from now on.

You can stop at any point and resume later. Tell Claude you want to pause. It will save where you are.

## What you end up with

A new folder somewhere on your computer (you pick where) that holds your personal AI operating system. Inside it:

- A `CLAUDE.md` file with your preferences, voice rules, and routing map. Yours, editable any time.
- A `MEMORY.md` file with your profile and the facts Claude needs to remember about you.
- One starter workstation folder for the first domain you chose to set up (job search, finance, meetings, whatever you picked).
- A weekly audit you can run by asking Claude "run the audit".

That's it. No application installed, no cloud service, no database. The folder is yours. You can move it, edit it, back it up, or delete it with no special tools.

## If something goes wrong

Tell Claude exactly what you saw on screen and what you expected. Claude will diagnose. If you cannot proceed, take a screenshot and open an issue at `https://github.com/arpit-kumar-veteran/claude-personal-os/issues`. Paste the screenshot and what happened. Someone will respond.

## What to do after setup

The first time you open your new OS folder in your Claude app, just say "hi". Claude will read your CLAUDE.md and MEMORY.md and know who you are. From there:

- To save a fact: say "remember this" and tell Claude. It will propose where to save it and wait for your approval.
- To run the weekly audit: say "run the audit".
- To add another workstation: say "create a new workstation for [domain]".
- To work in a specific workstation: say "I'm working on [domain]" and start.

## What this is not

This is not a chatbot. This is a folder of files that Claude reads to understand who you are and how you want to work. The files belong to you. You can edit them by hand any time, or ask Claude to edit them on your behalf (it will always ask first). The system is yours.

When you're ready, do Step 1.
