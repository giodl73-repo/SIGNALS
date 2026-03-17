Simulate a multi-turn agent conversation through a topic graph. Walk the dialog path: user intents, agent responses, topic transitions, fallback handling, session state. Identify: dead ends (no valid next intent), infinite loops, intent collisions (same utterance maps to multiple topics), missing fallbacks. Stock roles: Copilot Studio domain expert.

Write artifact to: simulations/flow/conversation/{topic}-conversation-{date}.md
