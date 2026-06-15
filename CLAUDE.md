# Personal Claude OS — Setup Repository

This is the Personal Claude OS setup repository. It is not the user's personal OS. It is the template and installer that creates one.

## When the user types "start"

Read `setup/bootstrap.md` and begin Phase 1 immediately. Do not explain what you are about to do first — the bootstrap handles the welcome.

## Setup session rules

These rules govern the entire setup session from "start" to final handoff.

1. **Track state.** Know which phase and question you are on at all times. If the session is interrupted and the user returns, read `setup/answers.md` (if it exists) and tell them exactly where you left off before asking anything.

2. **Trigger word at the end of every response.** Every response you send during setup must end with the next trigger — a bolded word or short phrase the user can type to continue. Use **continue** as the default. Vary the framing ("→ Type **continue** when ready", "→ Say **continue** or ask me anything first") but keep the word consistent so the user learns it once.

3. **Phase-end summary before moving on.** At the end of every phase, before asking the first question of the next phase, emit a summary block in this format:
   ```
   ✓ Done: [bullet list of what was captured in this phase]
   Next up: [one sentence describing the next phase and how many questions]
   → Type continue when ready.
   ```

4. **Off-track protocol.** If the user sends a message that is not a direct answer to the current question or the trigger word:
   - Respond to what they said (do not ignore it).
   - Then write on a new line: "**Back to setup:** We are on [Phase Name], question [N] of [M]. [Restate the exact question that was pending.]"
   - Wait for their answer before proceeding.

5. **One question at a time.** Never list multiple questions in one response. Never move to the next question until the current one is answered.

6. **No files written to this repository.** All files created during setup go to the user's chosen OS folder. Never write to or modify any file in the `claude-personal-os` repo folder itself.

7. **Plain language always.** Assume zero technical background. Define any term the first time you use it.
