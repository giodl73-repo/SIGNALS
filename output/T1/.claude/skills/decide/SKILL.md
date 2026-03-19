---
name: decide
description: "Run the full pre-commitment decision campaign. Orchestrates: scout-competitors, scout-feasibility, scout-risk, prove-hyp"
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


You are running /rhythm-decide for: {{topic}}

Run the full pre-commitment decision campaign. This orchestrates 6 skills in sequence.
Each produces an artifact. At the end, synthesize into a decision brief.

---

## CAMPAIGN SEQUENCE

Execute in order. Pass each output to the next step as context.

### Step 1: Inertia and Competition
Run discover-inertia and discover-competitors for {{topic}}.
Key question: why would teams do nothing? What named alternatives exist?

### Step 2: Feasibility and Risk  
Run discover-feasibility and discover-risk for {{topic}}.
Key question: can this be built? What are the top risks?

### Step 3: Evidence
Run discover-hypothesis for {{topic}}.
Frame the core claim and its falsification conditions.
Run discover-websearch to gather 3+ external sources.

### Step 4: Synthesis
Synthesize findings into a decision brief:

**Decision Brief: {{topic}}**

| Dimension | Signal | Confidence |
|-----------|--------|-----------|
| Inertia threat | [HIGH/MED/LOW] — [why] | HIGH/MED/LOW |
| Feasibility | [assessment] | HIGH/MED/LOW |
| Top risk | [risk name] — [mitigation] | HIGH/MED/LOW |
| Hypothesis | [core claim] | HIGH/MED/LOW |
| Evidence | [key finding] | HIGH/MED/LOW |

**Recommendation**: COMMIT | PAUSE | PIVOT | ABANDON

**Rationale**: [2-3 sentences connecting the signals to the recommendation]

**Inertia verdict**: [explicitly state why inertia loses, or why it wins]

---

Write campaign artifact to: simulations/rhythm/decide/{{topic}}-decide-{{date}}.md
Include frontmatter: skill: rhythm-decide, topic: {{topic}}, date: {{date}},
  campaign: [discover-inertia, discover-competitors, discover-feasibility,
             discover-risk, discover-hypothesis, discover-websearch]
