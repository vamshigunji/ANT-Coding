import os
import re
from persona_loader import PersonaLoader

class ForgeOrchestrator:
    """
    Main Orchestrator for Agentic Forge (v2.3).
    Binds the project context, personas, and execution logic.
    """
    
    def __init__(self, project_root="."):
        self.project_root = project_root
        self.status_path = os.path.join(project_root, "factory-os/artifacts/sprint-status.yaml")
        self.loader = PersonaLoader(personas_dir=os.path.join(project_root, "factory-os/personas"))

    def get_next_task(self):
        """
        Parses sprint-status.yaml to find the first 'todo' story.
        """
        if not os.path.exists(self.status_path):
            return None

        with open(self.status_path, 'r') as f:
            content = f.read()

        # Find the first story block with status: todo
        # Non-greedy match that doesn't cross into the next story definition
        story_pattern = r'(\w+-\d+\.\d+):(?:(?!\w+-\d+\.\d+:).)*?status:\s*todo'
        match = re.search(story_pattern, content, re.DOTALL)
        
        if match:
            story_id = match.group(1)
            # Find the title for this story
            title_pattern = rf'{story_id}:[\s\S]*?title:\s*"(.*)"'
            title_match = re.search(title_pattern, content)
            title = title_match.group(1) if title_match else "Untitled Story"
            
            return {"id": story_id, "title": title}
        
        return None

    def prepare_agent_session(self, story_id, persona_name):
        """
        Loads the persona and prepares the mission for the sub-agent.
        """
        try:
            system_prompt = self.loader.load_persona(persona_name)
            
            # Construct the task prompt
            task_prompt = f"""
            PROJECT CONTEXT: {self.project_root}
            STORY_ID: {story_id}
            
            MISSION: 
            Execute the assigned story according to the Technical Design (TDD.md) 
            and Product Requirements (PRD.md) found in the artifacts directory.
            
            REQUIRED ACTION:
            1. Read artifacts/PRD_Agentic_Forge_v2.md (or relevant project PRD).
            2. Implement the logic for {story_id}.
            3. Update the artifacts/sprint-status.yaml to 'done' once verified.
            """
            
            return {
                "persona": system_prompt,
                "task": task_prompt
            }
        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    orch = ForgeOrchestrator()
    task = orch.get_next_task()
    if task:
        print(f"🚀 FOUND TODO: {task['id']} - {task['title']}")
        # For demo/test, we assume STORY-1.1 uses the Elicitor
        session_data = orch.prepare_agent_session(task['id'], "persona_elicitor")
        print("\n--- GENERATED AGENT TASK ---")
        print(session_data['task'])
    else:
        print("✅ No pending stories in sprint-status.yaml.")
