---
mode: agent
description: "Generate the complete specification suite for a topic. Covers the full draft namespace."
---
Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Guided section authoring: purpose, requirements (from scout-requirements if available), design, constraints, open questions. Self-review on completion: flag open questions, gaps, and ambiguity. Stock role: Architect.

Write artifact to: signals/draft/specs/{topic}-spec-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
