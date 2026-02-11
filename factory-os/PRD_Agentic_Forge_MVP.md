# PRD: The Agentic Forge MVP (v0.1)
**Project Title:** Agentic Manufacturing Unit (AMU)  
**Status:** Draft / Strategic Proposal  
**Author:** Subu (AI Systems Architect)  
**Date:** February 11, 2026

---

## 1. Executive Summary
The **Agentic Forge MVP** is a high-fidelity software manufacturing unit built on **OpenClaw**. It leverages the context-extraction power of the **BMAD-METHOD** and the mechanical reliability of the **Ant Farm Ralph Loop**. The goal is to move from "AI as a Chatbot" to "AI as an Autonomous Factory," where a user provides a single "Vision Seed" and the system produces a verified, tested, and documented codebase with minimal human intervention.

## 2. The Problem Statement
Current AI development workflows suffer from three "Taxes":
1.  **The Elicitation Tax:** The human must spend hours answering granular questions to build a PRD.
2.  **The Context Decay Tax:** Long sessions lead to model "drift" where the agent forgets the original architecture.
3.  **The Hallucination Loop:** Agents fix bugs by creating new ones, requiring constant human debugging.

## 3. The Vision: "Lights-Out Software Factory"
The AMU will automate the transition from **Vision to Verified Code** using a multi-agent hierarchy. The human role shifts from "Inputs Provider" to "Strategic Arbiter."

---

## 4. Core Workflows (The Assembly Line)

### Stage 1: Autonomous Elicitation (The Lab)
*   **Method:** BMAD "Party Mode" using *First Principles Thinking*.
*   **Workflow:** 
    1.  User submits a **Vision Seed**.
    2.  OpenClaw spawns an **Analyst Agent** and a **PM Agent**.
    3.  The agents interview each other and query the **Workspace Memory** to fill gaps.
    4.  **Output:** A high-quality **Project Brief** and **PRD v1.0**.

### Stage 2: Artifact Codification (The Blueprint)
*   **Method:** A2A Handshake Protocol.
*   **Workflow:** 
    1.  The PRD is handed to the **Architect Agent**.
    2.  The Architect produces a **Technical Design Document (TDD)** and **Mermaid Diagrams**.
    3.  A **Scrum Master Agent** decomposes the TDD into granular **User Stories** stored as individual markdown files.
    4.  **Output:** A versioned directory of **Implementation Artifacts**.

### Stage 3: Verified Implementation (The Factory)
*   **Method:** The Ralph Loop (Ant Farm).
*   **Workflow:** 
    1.  For *every story*, OpenClaw spawns a **Fresh Session**.
    2.  **Developer Agent** implements the code based *only* on the TDD and the Story.
    3.  **Verifier Agent** (separate session) runs `npm test` or `pytest`.
    4.  If failed, the Developer gets a **Retry Signal** with the log.
    5.  **Output:** A verified Pull Request (PR) merged into the master branch.

---

## 5. Agent Personas (The Workforce)

| Role | Persona Name | Key Responsibility |
| :--- | :--- | :--- |
| **Coordinator** | **Mission Control** | Orchestrates sub-agents via `sessions_spawn`; manages the Kanban board. |
| **Analyst** | **The Elicitor** | Uses BMAD techniques to extract hidden requirements from the Vision Seed. |
| **PM** | **The Guardian** | Enforces the "Product Constitution"; manages Epics/Stories. |
| **Architect** | **Logic-Touch** | Designs the system schema and ensures technical feasibility. |
| **Lead Dev** | **The Builder** | Directs Implementation sub-agents; handles complex logic. |
| **Verifier** | **The Bouncer** | Automated code review and test execution; provides the "Gate" for merging. |

---

## 6. Technical Architecture (The OS)
The Forge runs on the **OpenClaw Agentic OS**:
*   **Mission Control:** Integrated with the **Claw Control** Kanban dashboard.
*   **Persistence:** All artifacts stored in a structured `artifacts/` folder (Git-tracked).
*   **Inter-Agent Comms:** Using the **A2A Protocol** (Google ADK compatible) for standardized handshakes.
*   **Circuit Breaker:** A logic-gate that stops the loop if a story fails verification 3 times, escalating to the Human.

---

## 7. Success Metrics (The Yield)
*   **Human Input Reduction:** User spends < 10% of total project time on chat/elicitation.
*   **First-Pass Yield:** > 80% of stories implemented and verified without human debugging.
*   **Documentation Integrity:** 1:1 mapping between User Stories, TDD, and actual Code.

## 8. Expected Outcomes
By the end of this MVP setup, you can expect:
1.  **An Autonomous Assembly Line:** A folder structure and set of script triggers that move an idea to code automatically.
2.  **A Self-Updating Kanban Board:** Real-time visibility into which agent is working on which story.
3.  **A "Hardened" Codebase:** Every line of code is backed by an Architect's design and a Verifier's test pass.

---
**Next Action for the User:**
*   **Ratify this PRD** by saying "Proceed." 
*   I will then begin codifying the `Workflows/` directory and initializing the **Mission Control** logic.
