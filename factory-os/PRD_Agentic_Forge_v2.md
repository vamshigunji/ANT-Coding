# PRD: The Agentic Forge (v2.0)
**Project Title:** Agentic Manufacturing Unit (AMU)  
**Status:** Strategic Blueprint  
**Date:** February 11, 2026

---

## 🏛️ Chain of Thought: Architectural Intent
The AMU is designed as a **Self-Eliciting Factory**. 

**The core logic shift:**
In traditional "Agentic Workflows," the human is the bottleneck—the one providing the context. In the **Forge v2.0**, the agents are the primary researchers. They use **BMAD-style Elicitation** to discover requirements by interviewing each other and the Internet, and only bringing "High-Entropy" conflicts to the human.

**Context Preservation:**
We utilize the **"Artifact Chain"** protocol. Every stage must result in a durable markdown/yaml file. These files act as the "Common Knowledge" (CK) of the factory, eliminating the need for long, drift-prone chat histories.

---

## 1. Executive Summary
The **Agentic Manufacturing Unit (AMU)** is an end-to-end software production system built on OpenClaw. It integrates the **BMAD methodology** for context-rich planning and the **Ant Farm Ralph Loop** for verified, session-isolated execution. The unit minimizes human taxation by automating research, elicitation, and design, while maintaining a resilient, agile assembly line that continues production even when individual tasks fail.

## 2. Human-in-the-Loop (HITL) Protocol
Human intervention is restricted to **Strategic Arbitration**.

### When to Invoke Human Input:
1.  **Conflict Resolution:** When the Architect and PM agents hit a deadlock (e.g., "Feature A is desirable but technically unfeasible at scale").
2.  **Ratification Gates:** Final approval of the PRD v1.0 and the TDD (Technical Design Document) before coding begins.
3.  **Circuit Breaker Escalation:** When a story fails verification 3 times, it is tagged `🙋 @Human_Review` on the Kanban board.
4.  **Directional Steering:** Periodic check-ins to pivot the "Vision Seed" if market research suggests a new gap.

**HITL Mechanism:** Human tasks are created as P0 tickets on the **Claw Control** board. Agents pause that specific ticket but **continue working on other non-dependent stories** in parallel.

---

## 3. Stage 1: Autonomous Brainstorming (The Discovery Lab)

### The Workforce (No-Code Swarm)
*   **Analyst:** Internet-enabled researcher. Performs competitive analysis and macro-trend mapping.
*   **PM:** Enforces the "Product Constitution" and business value.
*   **Solutions Architect:** Defines the high-level logic flow.
*   **Functional Architect:** Maps user journeys and business rules.
*   **Cloud/Testing Architect:** Defines the infrastructure and quality baseline.
*   **UI Designer:** Crafts layouts using **Pencil UI** (generating `.epz` or detailed spec exports).
*   **UX Expert:** Conducts "Persona Journeys" to stress-test the empathy map.

### The BMAD Elicitation Workflow
1.  **Vision Seeding:** User provides a raw idea.
2.  **Autonomous Research:** Analyst and PM crawl the web for similar products and technical blockers.
3.  **Advanced Elicitation:** Agents execute BMAD's structured question sets across five categories:
    - *Market Truths* (Analyst lead)
    - *User Struggles* (UX Expert lead)
    - *Organizational Capability* (Cloud Architect lead)
    - *Strategic Intent* (PM lead)
    - *Historical Evidence* (Solutions Architect lead)
4.  **Conflict Report:** Instead of asking the user 50 questions, the swarm generates a report of "deadlocks" for the human to arbitrate.
5.  **Output:** **PRD v1.0** (The Product Constitution).

---

## 4. Stage 2: Artifact Codification (The Blueprint)

### The Workflow Example: "Feature → Story"
- **Step 1:** The Architect reads the PRD and writes the **TDD.md** (database schemas, API contracts).
- **Step 2:** The **Scrum Master Agent** reads the TDD and initializes the **`sprint-status.yaml`**.
- **Step 3:** The SM generates individual **Story Files** in `backlog/stories/STORY-XXX.md`.

### Sprint Status Management (BMAD Inspired)
The `sprint-status.yaml` acts as the **Global State Machine**:
```yaml
project: AMU_MVP
status: in-progress
current_sprint: 1
stories:
  - id: STORY-101
    title: "Auth Gateway"
    status: ready-for-dev
    failure_count: 0
    artifacts: [PRD.md, TDD.md, STANDARDS.md]
```
The SM Agent monitors this file. When a story hits `ready-for-dev`, it triggers the **Implementation Loop**.

---

## 5. Stage 3: Implementation & Verification (The Factory)

### The Developer's Context Package
A common failure in agentic coding is providing *too little* context. Our Developer Agent receives:
1.  **The Task:** The specific `STORY-XXX.md` file.
2.  **The Logic:** The `TDD.md` (How it *must* be built).
3.  **The Vision:** The `PRD.md` (Why we are building it).
4.  **The Environment:** `STANDARDS.md` (Coding style, linting rules, library versions).
5.  **The Codebase:** Read-access to existing files to ensure pattern matching.

### The Ralph Loop (Ant Farm Implementation)
1.  **Isolation:** A **fresh OpenClaw session** is spawned for the story.
2.  **Execution:** Developer writes the code and unit tests.
3.  **Verification:** A **Verifier Agent** in a *separate* session attempts to run the code and tests.
4.  **The Circuit Breaker:**
    - If `FAIL`: `failure_count` incremented. Developer retries.
    - If `failure_count == 3`: The story is marked `status: blocked`. 
    - **RESILIENCE:** The Orchestrator **immediately moves to the next `ready-for-dev` story**. The factory does not stop.
    - A human task is created to investigate the blockage.

---

## 6. Project Outcomes (The Yield)
At the end of a project run, the Forge produces:
1.  **A Hardened Repository:** All code is verified and mapped 1:1 to artifacts.
2.  **Architectural Integrity:** No code exists that wasn't first defined in the TDD.
3.  **Documentation as a Byproduct:** PRDs, TDDs, and Sprint Reports are auto-generated and always up-to-date.
4.  **Zero-Drift History:** Because sessions are isolated, the final story is as high-quality as the first.

---
**Next Step for User:**
Review this V2.0 Blueprint. If it meets your standards for "Agentic Manufacturing," say **"Proceed."** 

*(Note: No author was mentioned in the creation of this document per protocol.)*
