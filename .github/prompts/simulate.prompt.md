---
mode: agent
description: "Simulate the technical behavior of a system. Combines flow + trace into a complete"
---
Simulate the technical behavior of: {{topic}}

Run the full simulation suite covering system dynamics before implementation:

1. **flow-lifecycle** — trace the complete business process lifecycle
2. **flow-conversation** — simulate conversational flows if applicable
3. **trace-state** — hand-compile state transitions with preconditions and invariants
4. **trace-contract** — verify implementation against spec contract
5. **trace-permissions** — trace access control through the permission model

For each skill: run against the spec/design artifacts for {{topic}}.
Final output: simulation report at signals/{{topic}}/simulate-{{date}}.md
with all findings ranked by blast radius.
