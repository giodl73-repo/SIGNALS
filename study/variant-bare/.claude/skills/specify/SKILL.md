---
name: specify
description: "Generate the complete specification suite for a topic. Covers the full draft namespace.

Covers:
- draft-spec      -> technical specification with guided section structure and self-review
- draft-proposal  -> proposal or ADR with three-option minimum and recommendation rationale
- draft-pitch     -> pitch deck narrative in exec, developer, and maker versions

Output: a spec package -- the technical spec as the source of truth, the proposal as
the decision record, and the pitch as the communication layer. All three are grounded
in the same topic signals.

Use when you have enough scout and prove signals to begin writing. The spec package
is the complete written artifact set for a feature before engineering begins.
"
allowed-tools: [Read, Write, Edit, Glob]
param_set: standard
---
Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Guided section authoring: purpose, requirements (from scout-requirements if available), design, constraints, open questions. Self-review on completion: flag open questions, gaps, and ambiguity. Stock role: Architect.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
