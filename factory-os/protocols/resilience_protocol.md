# Resilience & Circuit Breaker Protocol (v1.0)

## 1. The Pivot Principle
The Agentic Forge is an **Asynchronous Agile Factory**. A single story failure must NEVER block the entire pipeline.

## 2. Failure Handling (The 3-Strike Rule)
1. **Strike 1-2:** Automatic retry within the Ralph Loop.
2. **Strike 3:** The "Circuit Breaker" triggers.
   - **Action A:** Story status in `sprint-status.yaml` moves to `blocked`.
   - **Action B:** A **Human Intervention Task** is created on the Kanban (or reported via Telegram).
   - **Action C:** The Orchestrator **skips** this task and immediately triggers the next `ready-for-dev` story.

## 3. Human Escalation Handshake
- **Trigger:** `fail_count >= 3`.
- **Payload:** 
  - Vision Seed
  - Story File
  - Last 3 Verification Failure Logs
- **Resolution:** Human reviews the logs, fixes the TDD or Story, and resets `fail_count` to `0` to re-enter the loop.
