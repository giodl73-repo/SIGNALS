Extract and prioritize requirements from a product concept. Search for prior scout signals in BOTH signals/scout/ (real runs) AND signals/trace/skill/ (hand-compiled traces) -- never silently skip the trace directory. MoSCoW prioritization. Dependency graph (which requirements block others). Ambiguity flags (requirements needing clarification). Suspicious silences (areas with no requirements). Stock roles: PM (user-facing), Architect (technical), UX (usability), Compliance (regulatory).

Write artifact to: signals/scout/requirements/{topic}-requirements-{date}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
