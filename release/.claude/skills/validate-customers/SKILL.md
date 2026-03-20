---
name: validate-customers
description: 12 customer personas (C-01 through C-12) evaluate a feature for usefulness, clarity, and would-adopt (all 1-5). Primary
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


If --lightweight flag provided: run 4 personas only (C-01 maker, C-02 enterprise PM,
  C-07 startup founder, C-11 regulated industry) and skip weighted scoring table.
  Output: 4 persona cards + top adoption blocker + verdict. Faster, smaller output.

You are running /validate-customers for: {{topic}}

12 customer personas evaluate this feature for usefulness, clarity, and adoption likelihood. Primary audience weighted 3x, secondary 2x, non-target 1x.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-spec* or signals/**/{topic}-design* or signals/**/{topic}-competitors*
Read available artifacts to understand what the feature does and who it is for.
If no prior signals: infer from topic description.

---

## PHASE 2 -- 12-PERSONA EVALUATION

Personas:
- C-01 Maria Chen (Maker / indie developer): values speed and simplicity
- C-02 James Park (Enterprise PM): values alignment and evidence
- C-03 Sofia Rodriguez (UX designer): cares about user flows and friction
- C-04 Amir Hassan (DevOps engineer): cares about reliability and operational cost
- C-05 Priya Patel (Data scientist): needs clear data outputs and auditability
- C-06 Tom Mueller (Security architect): flags access control and compliance
- C-07 Lin Wei (Startup founder): values speed, hates overhead
- C-08 Diana Brooks (Enterprise buyer): evaluates ROI, procurement, support
- C-09 Carlos Mendez (Support engineer): predicts tickets and post-ship friction
- C-10 Yuki Tanaka (Junior developer): clarity and time-to-first-value
- C-11 Elena Kovacs (PM, regulated industry): compliance and audit trail
- C-12 Frank Hoffmann (Regulator / compliance officer): legal and policy alignment

Per-persona card:
```
[C-NN] {Name} -- {archetype}
Usefulness:   [1-5]  Why: [one sentence]
Clarity:      [1-5]  Why: [one sentence]
Would adopt:  [1-5]  Why: [one sentence]
Audience:     [primary / secondary / non-target]
Top concern:  [what could block adoption for this persona]
Delight:      [what this persona would love -- or None]
```

---

## PHASE 3 -- WEIGHTED SCORING

| Persona | Audience | Weight | Usefulness | Clarity | Would-Adopt | Weighted avg |
|---------|----------|--------|------------|---------|-------------|--------------|

Weighted aggregate = sum(persona_avg x weight) / sum(weights)
Threshold: 3.5/5 for ship-ready

---

## PHASE 4 -- SIGNAL EXTRACTION

Adoption blockers (primary persona would-adopt < 3):
  [C-NN] [persona] -- [specific blocker]

Positioning leaks (non-target confused about who this is for):
  [C-NN] [persona] -- [confusion signal]

Delight signals (any persona usefulness = 5):
  [C-NN] [persona] -- [what delighted them]

Verdict: SHIP-READY / REVISE / MAJOR-REVISION-REQUIRED

---

## PHASE 5 -- AMEND

1. [Address the highest-severity adoption blocker]
2. [Fix the most common positioning leak]
3. [Amplify the strongest delight signal]

Write artifact to: signals/validate/customers/{{topic}}-customers-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-customers-{date}.md). No namespace subdirectory.
Include frontmatter: skill: validate-customers, topic: {{topic}}, date: {{date}}, weighted_score: [N], verdict: [verdict]