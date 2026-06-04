# First Week

You just set up your Personal Claude OS. This guide tells you what to do in the first seven days to get real value quickly and build the right habits.

The goal of week one is not productivity. It is habituation. Getting comfortable opening the OS folder instead of a blank chat. By day 7, if it feels slightly strange to talk to Claude without opening your folder first, you are on track.

## Day 1: Confirm your setup is working

Open your OS folder in your Claude app. Say "hi."

Claude should greet you by name, describe your role, and mention your first workstation. If it does not, check that your CLAUDE.md and MEMORY.md are in the root of the folder Claude is reading.

Then say: "run the audit."

The audit will walk your folder structure and report any CRITICAL, WARNING, or INFO findings. On day 1, you want zero CRITICAL findings. A few INFO items are normal.

**Time: 10 minutes.**

## Day 2: Work one real task through the OS

Pick something you would normally do in a blank chat. A short email, a quick decision, a note you want captured. Do it through the OS instead.

Notice what is different. Claude knows who you are. It routes to the right workstation. It does not ask you to re-explain your role or preferences.

If Claude routes to the wrong workstation or behaves unexpectedly, note it. You will fix the routing map tomorrow.

**Time: 15 minutes of real work.**

## Day 3: Fix anything the first two days exposed

Go back to your routing map in CLAUDE.md. Is it routing correctly? Are the workstation Identity descriptions clear enough?

If something routed wrong, the most common cause is an ambiguous Identity paragraph. Tighten the boundary. Add one counter-example to the Identity section of the relevant workstation.

Propose the change. Wait for Claude to confirm before writing.

**Time: 10 minutes.**

## Day 4: Run your first session close

At the end of any working session today, say: "run the session-close skill."

Claude will scan the conversation, extract what changed, and propose exact updates to your MEMORY.md. Review the proposals. Approve what is accurate.

This is the most important habit in the OS. Session close is how the system learns. Do it every session from now on.

**Time: 5 minutes.**

## Day 5: Add a second workstation (if ready)

If you hit a domain on days 2 or 3 where Claude kept losing context, now is the time to add a workstation for it.

Say: "create a new workstation for [domain]."

Claude will ask a few questions and propose the CLAUDE.md and MEMORY.md. Review them. Confirm. The new workstation is live.

If one workstation is enough for now, skip this day.

**Time: 20 minutes if adding a workstation.**

## Day 6: Test your memory

Say "what do you remember about me?"

Claude should pull from your root MEMORY.md and any workstation MEMORY.md files and give you a summary. If anything is wrong or missing, say "remember this: [correction]" and Claude will propose the update.

This tests two things: that memory is being captured correctly, and that Claude is reading it at session start.

**Time: 10 minutes.**

## Day 7: Set up the weekly audit cadence

If you have not already set up a weekly audit, do it today. Say: "use the scheduled-task skill to set up a weekly audit."

Claude will produce a task definition and scheduling instructions. Set it for Friday at a time that works for you. Weekly maintenance takes 5 to 10 minutes once the system is stable.

Then read `METRICS.md` for a sense of what your system should look like at week 4 and month 3.

**Time: 15 minutes.**

## What to do from week 2 onward

- Run session close at the end of every session. Without this habit, the system stops learning.
- Run the audit once a week. It catches drift before it compounds.
- Add workstations as you hit domains where Claude keeps losing context. Do not add them speculatively.
- When a recurring task becomes repetitive, ask Claude whether it qualifies as a skill.

The system compounds over time. The work you put in during week one pays off in months two and three, not tomorrow.
