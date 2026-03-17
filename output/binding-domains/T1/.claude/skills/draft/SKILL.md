---
name: draft
description: "Draft namespace -- 4 skills for authoring design artifacts.

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your artifact and the most relevant draft skill will run.
"
allowed-tools: [Read, Write, Edit, Glob]
param_set: standard
---
Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Guided section authoring: purpose, requirements (from scout-requirements if available), design, constraints, open questions. Self-review on completion: flag open questions, gaps, and ambiguity. Stock role: Architect.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
