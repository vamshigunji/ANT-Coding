const fs = require('fs');
const path = require('path');

/**
 * Sprint Watcher v1.0
 * The brain of the Agentic Forge. 
 * Responsibilities:
 * 1. Parse sprint-status.yaml
 * 2. Determine current phase and story status
 * 3. Trigger the next OpenClaw session (sessions_spawn)
 */

function pollSprintStatus() {
    const statusPath = path.join(__dirname, '../artifacts/sprint-status.yaml');
    
    if (!fs.existsSync(statusPath)) {
        console.error("❌ ERROR: sprint-status.yaml not found at " + statusPath);
        return;
    }

    const content = fs.readFileSync(statusPath, 'utf8');
    
    // Simple regex-based parsing to avoid heavy yaml dependencies in v1
    const phaseMatch = content.match(/current_phase:\s*(\w+)/);
    const currentPhase = phaseMatch ? phaseMatch[1] : 'unknown';

    console.log(`🏗️  AGENTIC FORGE: Current Phase is [${currentPhase.toUpperCase()}]`);

    // Logic: Look for the first story that is 'todo'
    const stories = content.split('stories:')[1];
    if (stories) {
        const todoMatch = stories.match(/(\w+-\d+\.\d+):[\s\S]*?status:\s*todo/);
        if (todoMatch) {
            const nextStoryId = todoMatch[1];
            console.log(`🚀 NEXT ACTION: Initialize [${nextStoryId}]`);
            return nextStoryId;
        }
    }

    console.log("✅ FACTORY IDLE: All current stories processed.");
    return null;
}

// Running once for verification
const nextAction = pollSprintStatus();
if (nextAction) {
    // In a live environment, this would call sessions_spawn
    process.exit(0);
} else {
    process.exit(1);
}
