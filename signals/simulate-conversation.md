Keep total output under 2000 words. If --compact: under 800 words.

You are running /simulate-conversation for: {{topic}}

Simulate a multi-turn user conversation through the feature's dialog or interaction graph.

---

## PHASE 1 -- DIALOG MAP

Map the key conversation paths for {{topic}}:
- Entry points: how users first encounter this feature
- Core flow: the happy path dialog sequence (3-5 turns minimum)
- Topic transitions: how the conversation moves between feature areas
- Session state: what is tracked across turns

---

## PHASE 2 -- FAILURE SIMULATION

Walk each path and identify:
- **Dead ends**: no valid next step exists for a plausible user intent
- **Infinite loops**: user can get stuck cycling between states
- **Intent collisions**: same input maps to multiple conflicting outcomes
- **Missing fallbacks**: what happens when the expected input is not received

For each issue found:
```
F-NN: [issue type]
Location: [dialog step or state]
User path: [what the user did to reach here]
What breaks: [specific failure behavior]
Fix: [concrete recommendation]
```

---

## PHASE 3 -- SESSION STATE AUDIT

Review what state is maintained across turns:
- What persists (user context, prior choices, in-progress actions)
- What resets (session timeout behavior, error recovery paths)
- What can be corrupted (concurrent sessions, abandoned flows)

---

## PHASE 4 -- AMEND

Three targeted fixes:
1. [Address the most critical dead end or loop]
2. [Strengthen the fallback handling]
3. [Clarify session state boundaries]

Write artifact to: signals/simulate/conversation/{{topic}}-conversation-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-conversation-{date}.md). No namespace subdirectory.
Include frontmatter: skill: simulate-conversation, topic: {{topic}}, date: {{date}}
