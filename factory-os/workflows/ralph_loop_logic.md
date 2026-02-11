# Ralph Loop Orchestration (v1.0)
**Core Logic:** Fresh Session Isolation

## 1. Trigger
The Loop starts when a Story in `sprint-status.yaml` moves to `ready-for-dev`.

## 2. Session Spawn (Developer)
`sessions_spawn` command initializes a Developer session with:
- **Workspace:** `source/`
- **Context:** `VISION.md`, `PRD.md`, `TDD.md`, `STORY-XXX.md`
- **Goal:** Implement and self-test.

## 3. Session Spawn (Verifier)
Once Developer reports completion, `sessions_spawn` command initializes a Verifier session:
- **Action:** `exec` testing suite.
- **Output:** Writes result to `VERIFICATION_REPORT.md`.

## 4. Retrial Logic
- If Verifier == FAIL:
  - Increment `fail_count` in YAML.
  - RE-TRIGGER Step 2 with the failure log.
- If Verifier == PASS:
  - Mark Story as `done`.
  - Trigger next Story.
