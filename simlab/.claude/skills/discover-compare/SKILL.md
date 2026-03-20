---
name: discover-compare
description: "Compare two or more implementation options with inertia (status quo) always as Option 0. LEDGER GATE enforces token completion before matrix assembly. AMEND supports add-option, weight-dimension, and register-override."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /discover-compare for topic: {{topic}}.

Compare two or more implementation options for {{topic}}. Inertia (status quo / do nothing) is always Option 0 and is assessed first.

---

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
BODY-ORDER-LAYER: active

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

---

Declare register (REG):
  exec       -> ROI, risk, strategic alignment framing
  pm         -> adoption, market, user value framing
  engineering -> implementation, technical debt, scalability framing
  general    -> balanced framing (default)

Token: `REG: {register}`

---

Declare the status quo anchor -- why teams do nothing today:

Token: `ANCHOR[0]: {one sentence: specific mechanism keeping status quo in place}`

FAULT: compare every option against ANCHOR[0] only -- inter-option comparison without anchoring to status quo is an error.

---

For each option (A, B, ...) being compared:

REG-framed.
Token: `FEAS-{X}: {rating: HIGH/MEDIUM/LOW} -- {one sentence}`

REG-framed.
Token: `INERT-{X}: {rating: HIGH/MEDIUM/LOW} -- {mechanism: why teams resist this option}`
FAULT: assess INERT-{X} against ANCHOR[0] only -- not against other options.

REG-framed.
Token: `RISK-{X}: {risk1/rating}, {risk2/rating}`

REG-framed.
Token: `COMP-{X}: {positioning vs market / status quo}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

AMEND-HALT: "any of the above tokens is absent"

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if {AMEND-HALT}.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if {AMEND-HALT}.**

Re-score from tokens. Update RECOMMENDATION if it changes.

---

Write artifact to: signals/discover/compare/{{topic}}-compare-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-compare-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-compare, topic: {{topic}}, date: {{date}}, recommendation: [option], reg: [register]
