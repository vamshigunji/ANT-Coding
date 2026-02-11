# PRD: The Agentic Forge (v2.3)
**Project Title:** Agentic Manufacturing Unit (AMU)  
**Status:** Strategic Blueprint (Interoperable & Portable)  
**Date:** February 11, 2026

---

## 🏛️ Chain of Thought: Architectural Intent
The AMU is a **Portable Self-Eliciting Factory**. 

**Core Logic Shifts (v2.3):**
1.  **Project-Level Encapsulation:** The Forge is no longer a global singleton. It is installed *inside* each project. This ensures that agents are strictly context-bound to the project scope and that the entire project (Source + Factory OS) is portable between different OpenClaw instances or Clawdbots.
2.  **Decoupled Persona Layer:** Personas and characteristics are removed from the A2A protocol code. They live in a standalone directory (`/personas/`) as markdown files. This allows for rapid hot-swapping or fine-tuning to meet specific IDE standards (VSCode, Cursor, Claude) without touching the orchestration logic.

---

## 1. Executive Summary
The **Agentic Manufacturing Unit (AMU)** is an end-to-end software production system built on OpenClaw. V2.3 prioritizes **Interoperability and Portability**. Each project is a self-contained unit containing its own specific Forge OS, ensuring that context never leaks and that the project remains functional regardless of where it is hosted.

---

## 2. Visualizing the Factory (Diagrams)

### 2.1 Portable Project Architecture (v2.3)
```mermaid
graph TD
    subgraph "Portable Project Container"
        subgraph "Factory OS (Local Engine)"
            MC[Sprint Orchestrator]
            State[sprint-status.yaml]
            Workflows[Workflows/]
        ├───
        subgraph "Personas (Externalized)"
            P_Markdown[Persona Markdown Files]
            Traits[Standardization Specs: Cursor/Claude/VSCode]
        end
        ├───
        subgraph "Artifacts (Project Context)"
            PRD[PRD v2.3]
            TDD[Technical Design]
            Backlog[Stories/]
        end
        ├───
        subgraph "Source Code (The Product)"
            Code[App Source]
            Tests[Test Suite]
        end
    end

    A2A[A2A Protocol Layer] -->|Fetches Traits| P_Markdown
    A2A -->|Executes| Workflows
    Workflows -->|Context Bound| PRD
```

---

## 3. Portability & Interoperability Standards

### 3.1 Initialization Protocol
For every new project, the Forge must be initialized locally:
1.  `factory-os/` is cloned into the project root.
2.  Agents are spawned with their `HOME` and `WORKSPACE` environment variables strictly limited to the project directory.
3.  This "Project-in-a-Box" model allows a user to `zip` the directory and move it to a different OpenClaw instance without losing the factory state.

### 3.2 Decoupled Personas
Agents do not have hardcoded system prompts in the Python/JS code. 
*   **Location:** `factory-os/personas/*.md`
*   **Mechanism:** The A2A protocol layer reads the markdown file at runtime.
*   **IDE Interop:** By modifying the `standards/` or `personas/` files, the same Forge can be tuned to follow Cursor's `.cursorrules` or Claude's specific instruction formatting.

---

## 4. Stage 1: Autonomous Brainstorming (The Discovery Lab)
(Context-bound to project-local artifacts)

---

## 5. Stage 2: Artifact Codification (The Blueprint)
(Templates stored locally within the project to ensure schema consistency during moves)

---

## 6. Stage 3: Implementation & Verification (The Factory)
(Ralph Loop executes in isolated sessions with project-only read access)

---

## 7. Stage 4: Operational Governance & Telemetry (The Flywheel)
(Telemetry data stored in `factory-os/telemetry/` to preserve growth history during migration)

---

## 8. Project Outcomes (The Yield)
1.  **Zero-Leak Context:** Agents only see what is inside the project container.
2.  **Universal Portability:** The project and its manufacturing engine move as one.
3.  **Cross-IDE Interop:** Persona and Standard files allow the Forge to adapt to any development environment.

---
**Next Step for User:**
Review the **V2.3 Blueprint**. This satisfies the requirements for **Project Encapsulation** and **Persona Decoupling**. If the portability strategy matches your intent, say **"Proceed to V2.3 Implementation."**
