---
mode: agent
description: "Preview all installed Signal skills grouped by namespace. Shows binding type, skill list with descriptions, and quick start suggestion. DISPLAY ONLY."
---
You are running /tools-preview.

Preview what Signal skills are installed in this workspace and what they do.

DISPLAY ONLY -- no file written.

---

## STEP 1: SCAN INSTALLED SKILLS

Glob: .claude/skills/*/SKILL.md

For each installed skill, read the first 3 lines of the body to extract the skill's purpose.

---

## STEP 2: DISPLAY PREVIEW TABLE

Group by namespace (inferred from skill name prefix):

```
INSTALLED SIGNAL SKILLS
========================
Binding: [FLAT / BARE / SIGNAL / GROUPED] (detected from naming pattern)
Total:   N skills

DISCOVER (N skills)
  /discover-competitors    Scout inertia and named competitors
  /discover-feasibility    Assess technical and resource feasibility
  /discover-hypothesis     State a falsifiable hypothesis
  ...

SPECIFY (N skills)
  /specify-spec            Write a spec from intent
  /specify-proposal        Write a stakeholder alignment proposal
  ...

[repeat for each namespace]

SIGNAL + TOOLS (N skills)
  /signal                  Route to any skill by description
  /signal-health           Check workspace health
  /tools-coverage          Show coverage statistics
  /tools-preview           This skill -- shows installed skills
  ...
```

---

## STEP 3: QUICK START SUGGESTION

Based on what skills are installed, suggest the 3-command quick start:

```
QUICK START for this workspace:
  1. /discover-competitors <your-feature>   Scout inertia + competitors
  2. /specify-spec <your-feature>           Write the spec
  3. /tools-coverage <your-feature>         Check what signals are missing
```
