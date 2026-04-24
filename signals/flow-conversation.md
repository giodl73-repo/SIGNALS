Simulate a multi-turn agent conversation through a topic graph. Walk the dialog path: user intents, agent responses, topic transitions, fallback handling, session state. Identify: dead ends (no valid next intent), infinite loops, intent collisions (same utterance maps to multiple topics), missing fallbacks. Stock roles: Copilot Studio domain expert.

Write artifact to: signals/flow/conversation/{topic}-conversation-{date}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
