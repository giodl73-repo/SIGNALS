---
name: simulate
description: "Simulate the technical behavior of a system. Combines flow + trace into a complete
behavioral simulation covering both domain process and platform mechanics.

Covers:
- flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
- flow-conversation -> multi-turn agent conversation with dead-end and loop detection
- trace-state       -> state machine transitions with preconditions and invariants
- trace-contract    -> expected vs actual output comparison with mismatch severity
- trace-permissions -> RBAC walk-through with privilege escalation detection

Output: a simulation findings report with identified gaps, exception paths, and
state machine anomalies. Each finding includes system boundary and severity.

Use when you have a spec and want to know what breaks before writing code. The
simulate output becomes the baseline for test scenario design.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: analysis
---
Simulate the technical behavior of: {{topic}}

Run the full simulation suite covering system dynamics before implementation:

1. **flow-lifecycle** — trace the complete business process lifecycle
2. **flow-conversation** — simulate conversational flows if applicable
3. **trace-state** — hand-compile state transitions with preconditions and invariants
4. **trace-contract** — verify implementation against spec contract
5. **trace-permissions** — trace access control through the permission model

For each skill: run against the spec/design artifacts for {{topic}}.
Final output: simulation report at simulations/{{topic}}/simulate-{{date}}.md
with all findings ranked by blast radius.
