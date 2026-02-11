# Agentic Forge Core (v2.3)

This directory contains the orchestration engine for the Agentic Manufacturing Unit (AMU).

## Components

1.  **`persona_loader.py`**: Parses markdown files in `factory-os/personas/` into structured system prompts.
2.  **`orchestrator.py`**: The "Brain" of the factory. Scans `sprint-status.yaml` and prepares the mission for the next agent.
3.  **`handshake.py`**: Implements the A2A protocol for context-preserving handovers.

## Usage

To find the next pending task:
```bash
python3 factory-os/core/orchestrator.py
```

To create a project-level encapsulation, simply copy the `factory-os` directory into any new project root. The orchestrator will automatically bind to the local context.
