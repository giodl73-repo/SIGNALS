---
name: quest-rubric
description: "Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.
"
allowed-tools: [Read, Write, Glob]
---
---
name: quest-rubric
description: "Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.
"
allowed-tools: [Read, Write, Glob]
---
## Purpose

Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.


## Parameters

**Inputs**: SkillSpec, TraceOutput
**Outputs**: Rubric

## Algorithm

Implementation for quest-rubric.
