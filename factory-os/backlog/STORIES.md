# Agentic Forge: Detailed Stories

### EPIC-01: Foundation & Sprint Orchestrator
- **STORY-1.1: [OS] Directory & Schema Initialization**
  - Create `factory-os/protocols`, `factory-os/workflows`, and `factory-os/artifacts` directories.
  - Define the `sprint-status.yaml` schema to track agent IDs, story states, and failure counts.
- **STORY-1.2: [OS] Sprint Watcher Workflow**
  - Codify the "Watcher" logic that parses `sprint-status.yaml` to determine the next session trigger.
  - Implement the "Handover" mechanism between story completion and next story initialization.
- **STORY-1.3: [OS] Persona Hub Initialization**
  - Create the `factory-os/personas/` directory.
  - Define the "Persona Schema" (instructions, tone, constraints) to ensure agents can be retargeted for different IDEs/Standards (Claude, Cursor, etc.).

### EPIC-02: The Discovery Lab
- **STORY-2.1: [LAB] A2A Handshake Codification**
  - Define the `handshake.md` format that allows an Analyst to pass context to a PM without drift.
- **STORY-2.2: [LAB] Internet Research Toolset**
  - Configure the Analyst persona with `web_search` and `web_fetch` priority rules.

### EPIC-03: The Blueprint Engine
- **STORY-3.1: [BLUEPRINT] Artifact Templates**
  - Create the standard `PRD_v1_Template.md` and `TDD_v1_Template.md` inspired by BMAD v5.
- **STORY-3.2: [BLUEPRINT] Automated Story Gen**
  - Logic to parse a TDD and generate individual Story MD files with injected vision context.

### EPIC-04: The Production Line
- **STORY-4.1: [PROD] Ralph Loop Implementation**
  - Create the orchestrator script that uses `sessions_spawn` to isolate each implementation task.
- **STORY-4.2: [PROD] Verifier Agent Protocol**
  - Define the "Bouncer" instructions: Verifier must only have access to the code and the tests, not the developer session.

### EPIC-05: Resilience
- **STORY-5.1: [RESILIENCE] Circuit Breaker Logic**
  - Implement the `fail_count > 3` check and the state-update that triggers the next story.
- **STORY-5.2: [RESILIENCE] Arbiter Escalation**
  - Logic to auto-generate a human task on Claw Control when a story is blocked.
