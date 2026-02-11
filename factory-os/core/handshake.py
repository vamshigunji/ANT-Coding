import os
import json
from datetime import datetime

class A2AHandshake:
    """
    Agent-to-Agent Handshake Protocol (v2.3).
    Ensures context preservation via Markdown-Structured Data (MSD).
    """
    
    def __init__(self, artifacts_dir="factory-os/artifacts"):
        self.artifacts_dir = artifacts_dir

    def create_brief(self, source_agent, mission_brief, research_data=None):
        """
        Creates a PROJECT_BRIEF.md for the next agent in the chain.
        """
        path = os.path.join(self.artifacts_dir, "PROJECT_BRIEF.md")
        
        content = f"""# A2A PROJECT BRIEF: {source_agent}
**Timestamp:** {datetime.utcnow().isoformat()}Z
**Source Agent:** {source_agent}

## 1. Mission Brief
{mission_brief}

## 2. Research Data
{research_data if research_data else "No external research data attached."}

## 3. Handover Instructions
The target agent should use this brief as the primary context for the next phase.
"""
        with open(path, 'w') as f:
            f.write(content)
        
        return path

    def verify_brief(self):
        """
        Checks if a brief exists and is valid.
        """
        path = os.path.join(self.artifacts_dir, "PROJECT_BRIEF.md")
        return os.path.exists(path)

if __name__ == "__main__":
    handshake = A2AHandshake()
    brief_path = handshake.create_brief(
        source_agent="Analyst-01",
        mission_brief="Build a landing page for the Agentic Forge.",
        research_data="- Competitor A: Linear pricing\n- Competitor B: Usage-based pricing"
    )
    print(f"✅ Handshake Brief Created: {brief_path}")
