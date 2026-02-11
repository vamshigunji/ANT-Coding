# A2A Handshake Contract (v1.0)
**Scope:** Discovery Lab to Solutioning  
**Protocol:** Markdown-Structured Data (MSD)

## 1. Overview
The Handshake Contract ensures that context generated during the **Discovery Lab** (Analyst/PM) is perfectly preserved when passed to the **Architect Swarm**. It eliminates "Drift" by using mandatory schema fields.

## 2. Handover Schema (The Manifest)
Every handover from Stage 1 to Stage 2 MUST include the following blocks:

### 2.1 Context Metadata
```yaml
source_agent: [Agent ID]
target_agent: [Agent ID]
timestamp: [ISO-8601]
project_context_path: artifacts/VISION_SEED.md
```

### 2.2 The Project Brief (Extracted Logic)
- **Problem Statement:** The core struggle identified.
- **Critical Requirements:** P0 features only.
- **Constraints:** (Technical, Legal, or Financial).

### 2.3 The Conflict Log (Arbitration Results)
- List all agent deadlocks and the resulting Human-in-the-Loop decision.

### 2.4 Research Citations
- List all `web_fetch` URLs used for competitive analysis.

## 3. Handshake Execution Protocol
1.  **Preparation:** Sending Agent (Analyst) writes the MSD to `artifacts/PROJECT_BRIEF.md`.
2.  **Notification:** Sending Agent updates `sprint-status.yaml` status to `review`.
3.  **Consumption:** Receiving Agent (PM/Architect) reads the file and initializes their session with it as the primary system context.
