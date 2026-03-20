---
mode: agent
description: "Requirements extraction with MoSCoW prioritization and dependency graph."
---
Extract and prioritize requirements from a product concept. Search for prior scout signals in BOTH signals/scout/ (real runs) AND signals/trace/skill/ (hand-compiled traces) -- never silently skip the trace directory. MoSCoW prioritization. Dependency graph (which requirements block others). Ambiguity flags (requirements needing clarification). Suspicious silences (areas with no requirements). Stock roles: PM (user-facing), Architect (technical), UX (usability), Compliance (regulatory).

Write artifact to: signals/scout/requirements/{topic}-requirements-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
