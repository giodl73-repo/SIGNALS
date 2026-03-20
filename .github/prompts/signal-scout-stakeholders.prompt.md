---
mode: agent
description: "Stakeholder mapping with power/interest grid and veto risk ranking."
---
Map the stakeholder landscape for a product decision. If CODEOWNERS is absent, extract org context from the invocation string. If invocation context is also insufficient, ask one question: "What org or team is this decision for?" Never silently infer an org structure. Power/interest grid, veto risks ranked by probability, champion identification, communication strategy per quadrant. Stock roles: PM (power/interest mapping), Strategy (conflicts), UX (journeys).

Write artifact to: signals/scout/stakeholders/{topic}-stakeholders-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
