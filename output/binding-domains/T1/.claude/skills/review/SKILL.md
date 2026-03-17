---
name: review
description: "Review namespace -- 4 skills for design and code validation.

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: full
---
Multi-expert review of a design artifact through 6 standard disciplines and auto-selected domain experts. Auto-select 3-5 domain experts from content signals (e.g., spec mentioning RBAC selects a security architect). Per-reviewer findings with P1/P2/P3 severity. Consensus analysis (2+ reviewers flag same thing), split opinions, unique catches. Amend: address findings one by one, re-run specific reviewers on changed sections. Stock: 6 disciplines (architect, code-quality, documentation, testing, process, implementation) + domain experts.

Write artifact to: simulations/review/design/{topic}-design-{date}.md
