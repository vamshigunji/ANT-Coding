import os
import re

class PersonaLoader:
    """
    Decoupled Persona Loader for Agentic Forge (v2.3).
    Parses markdown personas into structured system prompts.
    """
    
    def __init__(self, personas_dir="factory-os/personas"):
        self.personas_dir = personas_dir

    def load_persona(self, persona_name):
        """
        Loads a persona markdown file and returns a structured string.
        """
        path = os.path.join(self.personas_dir, f"{persona_name}.md")
        if not os.path.exists(path):
            # Fallback for relative paths from project root
            path = os.path.join(os.getcwd(), self.personas_dir, f"{persona_name}.md")
            
        if not os.path.exists(path):
            raise FileNotFoundError(f"Persona file not found: {path}")

        with open(path, 'r') as f:
            content = f.read()

        return self._parse_markdown(content)

    def _parse_markdown(self, content):
        """
        Converts markdown sections into a clean system prompt.
        """
        # Extract title
        title_match = re.search(r'# PERSONA: (.*)', content)
        title = title_match.group(1) if title_match else "Unknown Agent"

        # Extract sections
        sections = re.split(r'## \d+\.', content)
        
        system_prompt = f"IDENTITY: {title}\n\n"
        
        for section in sections[1:]:  # Skip the part before the first ##
            lines = section.strip().split('\n')
            header = lines[0].strip()
            body = '\n'.join(lines[1:]).strip()
            system_prompt += f"--- {header.upper()} ---\n{body}\n\n"

        return system_prompt

if __name__ == "__main__":
    # Test loading the elicitor
    loader = PersonaLoader(personas_dir="factory-os/personas")
    try:
        prompt = loader.load_persona("persona_elicitor")
        print("--- LOADED SYSTEM PROMPT ---")
        print(prompt)
    except Exception as e:
        print(f"Error: {e}")
