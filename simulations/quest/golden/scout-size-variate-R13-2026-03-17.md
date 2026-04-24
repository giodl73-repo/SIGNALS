# Scout-Size Prompt Variations -- R13

**Skill**: scout-size
**Rubric**: v13 (30 aspirational criteria, C-01 through C-38)
**Date**: 2026-03-17
**Round**: 13
**R12 champion candidate**: V-05 R12 (TBD score under v13)
**R12 gaps under v13**:
- C-36: R12 V-01 achieves full coverage; V-03/V-04 at minimum; V-05 may lack Cost Trajectory tag
- C-37: R12 V-02 uses "+~N%/quarter" notation; C-37 specifies "accelerating / stable / plateauing / reversing" shape vocabulary
- C-38: R12 SEALED items use presence-only confirmations; embedding exact disqualifying forms strengthens compliance

---

## Context: What R13 Addresses

v13 adds three new criteria from R12 excellence signals. No single R12 variation achieves all three simultaneously.

| ID | New criterion | R13 fix |
|----|---------------|---------|
| C-36 | Constraint tags cover ALL vocabulary-constrained fields | Extend to Cost Trajectory column |
| C-37 | Inertia uses 5-field format with Cost Trajectory | Align vocabulary: accelerating / stable / plateauing / reversing |
| C-38 | PHASE SEALED blocks at end of each phase | Embed exact disqualifying forms inside each checklist item |

**Variation axes:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing (C-37 vocabulary correction) | R12 V-02 used "+~N%/quarter". C-37 specifies accelerating/stable/plateauing/reversing. V-01 aligns Cost Trajectory to this vocabulary with [FAIL:] tag. C-36 minimum; Phase 0 SEALED only. |
| V-02 | Output format (C-36 full coverage) | Tags every vocab-constrained column: Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Up/Down Destination. 4-field inertia. C-38 absent. Tests: every appearing vocab column tagged. |
| V-03 | Lifecycle emphasis (C-38 SEALED items with disqualifying forms) | Embeds exact disqualifying form inside each SEALED checkbox. C-37 absent; C-36 minimum. Tests: disqualifying forms in SEALED items eliminate vocab drift at phase transitions. |
| V-04 | Combined: V-01 + V-03 (C-37 vocabulary + C-38 enhanced items) | 5-field inertia with shape vocabulary + PHASE SEALED items with disqualifying forms. C-36 minimum. |
| V-05 | Combined: V-01 + V-02 + V-03 -- champion attempt | All three new criteria. Third-person institutional register. |

---

## V-01 -- Axis: Inertia framing (C-37 vocabulary: accelerating / stable / plateauing / reversing)

**Variation axis**: Inertia framing -- Cost Trajectory uses C-37 rubric vocabulary with [FAIL:] tag; 5-field format

**Hypothesis**: R12 V-02 introduced Cost Trajectory using "+~N%/quarter" quantified-rate notation. The C-37 rubric specifies a controlled shape vocabulary: accelerating / stable / plateauing / reversing. V-01 aligns the Cost Trajectory column to this vocabulary, adds an inline [FAIL:] tag naming every disqualifying form, and updates Phase 0 SEALED to confirm the shape label. C-36 at minimum (C-01/C-02 only); Phase 1/2 verbal handoffs only. Hypothesis: vocabulary alignment is the minimum fix for C-37 compliance.

---

You are running a **scout-size** sizing signal -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** -- exactly one. "MODERATE", "medium-high", "3/5" are invalid.

This signal is produced in three phases. Complete each phase before proceeding.

---

### Phase 0 -- Inertia Analyst

**Charter -- you own exactly one section: Inertia Check.**
**Charter -- you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Phase 0 establishes five dimensions: specific workaround, friction cost, Cost Direction (which way), Cost Trajectory (what shape), causal factor. Direction and Trajectory are distinct fields.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth

| Workaround [Phase 0 -- name the specific substitute] | Ongoing Cost [Phase 0 -- at minimum: one time or error-rate dimension] | Cost Direction [Phase 0 -- FAIL: "neutral", "similar", "a wash", "worsening", "improving" -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Phase 0 -- FAIL: "+~20%/quarter" without shape label, "worsening" alone, "getting worse" alone, any non-vocabulary term -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Phase 0 -- one causal sentence] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

Before Phase 1 opens, confirm ALL:

  [ ] Workaround: specifically named
  [ ] Ongoing Cost: at least one concrete dimension
  [ ] Cost Direction: exactly one of: cheaper / comparable / more expensive
  [ ] Cost Trajectory: exactly one of: accelerating / stable / plateauing / reversing
        ("+~N%/quarter" without shape label does not satisfy)
  [ ] Key Driver: names causal factor, not restatement of cost

Phase 1 OPENS only when all five items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter -- you own**: Surface Area, Complexity Tier, Primary Driver, Team-Size, Timeline, Confidence Level + Basis, Tier-Up/Down Sensitivity, Confidence Calibration.
**Charter -- you do NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- resolve before any Phase 1 analysis field**

Out-of-scope boundary: [named exclusion, or "No exclusions -- full scope assumed."]
Break-even signal: [at what level building recovers cost, or "Cannot assess -- [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL -- commit now]
  Timeline: [N-M sprints -- commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area, Complexity, Synthesis (each prohibits).
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not populate any field below until gate is complete.

---

#### Surface Area [Phase 1]

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

| Integration Point [name each individually -- category labels fail] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1]

| Complexity Tier [Phase 1 -- FAIL: MODERATE, medium-high, 3/5 -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1-2 named causal factors] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1]

| Specialist Discipline [name the role] | FTE | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1]

| Sprint Range [Phase 1 -- FAIL: calendar reference, single-number estimate -- N-M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1]

| Confidence Level [Phase 1 -- FAIL: MEDIUM-HIGH, 3/5, "acceptable" -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1]

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

Phase 1 complete. Proceed to Phase 2.

---

### Phase 2 -- Risk Assessor

**Charter -- you own exactly one field: Confidence Gap.**
**Self-test**: "Could a reader derive my gap from Phase 1 by negating something Phase 1 confirmed?" If yes: charter violation.

| Confidence Gap [Phase 2 -- must name a dimension Phase 1 did not reach] |
|---|
| Gap: [specific named unknown] -- [why it matters] |

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction] / [trajectory: accel/stable/plateau/reverse] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5] | 1 | [level -- basis] |
| Confidence Gap | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here.

Unknown: / Impact: / Movement:

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis. Cross-referencing two+ dimensions required.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two dimensions]
Verdict: ["committed in PRE-FLIGHT GATE" phrase required at anchor and verdict]

Cross-signal directional observation after the verdict.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is present and amended dimension appears in cross-signal conclusion -- re-evaluate before closing.

---

### Per-Criterion Self-Check

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-37 | Five named fields; Cost Trajectory: accelerating/stable/plateauing/reversing | "+~N%/quarter" without shape label; "worsening" as trajectory | | |
| C-36 | Every vocab-constrained column header has [FAIL:] tag (minimum exceeded for appearing fields) | C-01/C-02 + Cost Direction + Cost Trajectory tagged; Confidence Level, Tier-Destination untagged | PARTIAL | |
| C-38 | PHASE SEALED at Phase 0, 1, and 2 | Phase 0 SEALED only; Phases 1/2 verbal handoffs | FAIL -- single-axis; V-01 tests C-37 only | |

*(All other self-check entries as per R12 V-05 baseline.)*

---

---

## V-02 -- Axis: Output format (C-36 full constraint tag coverage)

**Variation axis**: Output format -- [FAIL:] tags on ALL vocabulary-constrained column headers; 4-field inertia (C-37 absent); no PHASE SEALED

**Hypothesis**: R12 V-01 tagged six vocab fields. C-37 adds Cost Trajectory -- but C-37 is absent in V-02, so Cost Trajectory column does not appear. V-02 tests: C-36 is satisfied by tagging every vocab column that does appear. Tags cover: Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Up/Down Destination. C-38 absent. Hypothesis: C-36 coverage is complete when every appearing vocab column is tagged.

---

You are running a **scout-size** sizing signal -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. Downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** -- exactly one. Any other form is a hard fail.

Work through the following steps in order.

---

### Step 1: Inertia Check

> **WRONG**: "Teams manage this manually." -- No specific workaround; no cost. Fails.
> **CORRECT**: "Manual CSV export + re-import -- building cheaper long-term; ~45 min/sprint/team. Key Driver: team-count growth."

| Workaround [name the specific substitute] | Ongoing Cost [at minimum: one dimension] | Cost Direction [FAIL: "neutral", "similar", "a wash", "worsening", "improving" -- exactly one: cheaper / comparable / more expensive] | Key Driver [one causal sentence] |
|---|---|---|---|
| | | | |

---

### PRE-FLIGHT GATE

Out-of-scope boundary: [named exclusion, or "No exclusions -- full scope assumed."]
Break-even signal: [at what level building recovers cost, or "Cannot assess -- [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL -- commit now]
  Timeline: [N-M sprints -- commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area, Complexity, Synthesis (each prohibits).
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not proceed until gate is complete.

---

### Step 2: Surface Area

Do not include scope exclusions here.

| Integration Point [name each individually -- category labels fail] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

### Step 3: Complexity

| Complexity Tier [FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate" -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1-2 named causal factors] |
|---|---|
| | |

---

### Step 4: Team-Size Signal

| Specialist Discipline [name the role] | FTE [FAIL: "part-time", "TBD" -- numeric fraction required] | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

### Step 5: Timeline Signal

| Sprint Range [FAIL: any calendar reference, any single-number estimate -- N-M sprints only] |
|---|
| |

---

### Step 6: Confidence Level + Basis

| Confidence Level [FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence" -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified] |
|---|---|
| | |

---

### Step 7: Tier Sensitivity

| Direction | Single Named Falsifiable Condition | Destination Tier [FAIL: same as current, MODERATE, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Step 8: Confidence Gap

**Self-test**: If reversing a Step 6 item ("X confirmed" -> "X unconfirmed") produces the gap -- basis-negation. Restate.

| Confidence Gap [FAIL: any dimension Step 6 confirmed -- must name a dimension Step 6 did not reach] |
|---|
| Gap: [specific named unknown] -- [why it matters] |

---

### Step 9: Confidence Calibration

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Value |
|---|---|
| Inertia Check | [workaround -- cost direction -- key driver] |
| Surface Area | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | [tier] |
| Primary Complexity Driver | [1-2 named factors] |
| Team-Size Signal | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate -- only: N-M sprints] | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | [level -- basis] |
| Confidence Gap | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, MODERATE -- must differ: LOW / MEDIUM / HIGH / XL] | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, MODERATE -- must differ: LOW / MEDIUM / HIGH / XL] | Tier drops to [ ] if [ ] |
| Confidence Calibration | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here.

Unknown: / Impact: / Movement:

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Steps 1-8 -- at least two dimensions]
Verdict: ["committed in PRE-FLIGHT GATE" phrase required]

Cross-signal directional observation after the verdict.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is present and amended dimension appears in cross-signal conclusion -- re-evaluate before closing.

---

### Per-Criterion Self-Check

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-36 | Every vocab-constrained column header present carries [FAIL:] tag: Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Up/Down Destination | Any vocab-constrained column present without [FAIL:] tag -- including Cost Direction (4-field inertia) | | |
| C-37 | 5-field inertia with Cost Trajectory | 4-field inertia -- C-37 intentionally absent | FAIL -- single-axis | |
| C-38 | PHASE SEALED blocks | No PHASE SEALED -- C-38 intentionally absent | FAIL -- single-axis | |

*(All other self-check entries as per R12 V-05 baseline.)*

---

---

## V-03 -- Axis: Lifecycle emphasis (C-38 PHASE SEALED items embed exact disqualifying forms)

**Variation axis**: Lifecycle emphasis -- PHASE SEALED at Phase 0, 1, and 2; each item embeds the exact disqualifying form; 4-field inertia; C-36 minimum

**Hypothesis**: R12 V-03 SEALED items confirm presence with vocabulary labels. V-03 embeds the exact disqualifying form inside each checkbox: "[ ] Cost Direction: cheaper/comparable/more expensive -- FAIL: neutral, similar, a wash, worsening". This aligns SEALED items with C-29's exact-disqualifying-form standard. C-37 absent; C-36 minimum. Hypothesis: disqualifying forms in SEALED items eliminate vocab drift at phase transitions.

---

You are running a **scout-size** sizing signal -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** -- exactly one. "MODERATE", "medium-high", "3/5" are invalid.

Three phases. Each phase must be SEALED before the next opens.

---

### Phase 0 -- Inertia Analyst

**Charter**: You produce exactly one section: Inertia Check.
**You do NOT produce**: Surface Area, Complexity Tier, Team-Size, Timeline, Confidence, Gap, Sensitivities, Calibration.

| Workaround [name the specific substitute] | Ongoing Cost [at minimum: one time or error-rate dimension] | Cost Direction [FAIL: neutral / similar / a wash / worsening / improving -- exactly one: cheaper / comparable / more expensive] | Key Driver [one causal sentence] |
|---|---|---|---|
| | | | |

---

```
-- PHASE 0 SEALED --

Confirm ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" without naming tool/workflow
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead" (no measurable dimension)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving",
        "increasing cost", "moderate impact", any non-vocabulary paraphrase
  [ ] Key Driver: names the causal factor, not a cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

Phase 1 OPENS only when all four items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter**: Produces: Surface Area, Complexity Tier, Primary Driver, Team-Size, Timeline, Confidence Level + Basis, Tier-Up/Down Sensitivity, Confidence Calibration.
**Does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE**

Out-of-scope boundary: [named exclusion, or "No exclusions -- full scope assumed."]
Break-even signal: [at what level building recovers cost, or "Cannot assess -- [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL -- commit now]
  Timeline: [N-M sprints -- commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area, Complexity, Synthesis (each prohibits).
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not populate fields below until gate is complete.

---

#### Surface Area [Phase 1]

Do not include scope exclusions here.

| Integration Point [name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1]

| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1-2 named causal factors] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1]

| Specialist Discipline | FTE | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1]

| Sprint Range [FAIL: calendar reference, single-number estimate -- N-M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1]

| Confidence Level [FAIL: MEDIUM-HIGH, 3/5, "acceptable" -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1]

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

Confirm ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: category labels; count absent
  [ ] Complexity Tier: exactly LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate"
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many dependencies", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time" or "TBD"
  [ ] Timeline: N-M sprint range --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate); range absent
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: unfalsifiable condition; destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: unfalsifiable condition; destination matches current tier
  [ ] Confidence Calibration: at least one entry per column --
        FAIL: either column empty

Phase 2 OPENS only when all nine items are confirmed.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter**: Produces exactly one field: Confidence Gap.
**Self-test**: "Could a reader derive my gap from Phase 1 by negation?" If yes: charter violation.

| Confidence Gap [must name a dimension Phase 1 did not reach] |
|---|
| Gap: [specific named unknown] -- [why it matters] |

---

```
-- PHASE 2 SEALED --

Confirm ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 1 Confidence Basis by negation --
        FAIL: reversing any Phase 1 basis item produces this gap
  [ ] Gap names the dimension Phase 1 did not reach --
        FAIL: naming a dimension Phase 1 addressed, even with different framing

Output Compilation OPENS only when all three items are confirmed.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check | 0 | [workaround -- cost direction -- key driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5] | 1 | [level -- basis] |
| Confidence Gap | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here.

Unknown: / Impact: / Movement:

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two dimensions]
Verdict: ["committed in PRE-FLIGHT GATE" phrase required]

Cross-signal directional observation after the verdict.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is present and amended dimension appears in cross-signal conclusion -- re-evaluate before closing.

---

### Per-Criterion Self-Check

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-38 | PHASE SEALED at Phase 0, 1, and 2; each checklist with min 3 items naming specific fields and embedding exact disqualifying forms | Items use "all fields complete" (generic); items name field but omit disqualifying form; single terminal block | | |
| C-37 | 5-field inertia with Cost Trajectory vocabulary | 4-field inertia -- C-37 intentionally absent | FAIL -- single-axis | |
| C-36 | Full constraint tag coverage | Minimum only (C-01/C-02 + Cost Direction) | PARTIAL | |

*(All other self-check entries as per R12 V-05 baseline.)*

---

---

## V-04 -- Combined: V-01 + V-03 (C-37 vocabulary + C-38 enhanced checklist items)

**Variation axis**: Inertia framing (C-37 correct vocabulary) + Lifecycle emphasis (C-38 SEALED items with disqualifying forms); C-36 minimum

**Hypothesis**: V-01 fixes C-37 vocabulary. V-03 embeds disqualifying forms in SEALED items. Combined: Phase 0 SEALED confirms "Cost Trajectory: accelerating/stable/plateauing/reversing -- FAIL: +~N%/quarter without shape, worsening alone". Orthogonal failure modes. C-36 at minimum. Hypothesis: C-37 + C-38 cover the two most impactful failure modes; C-36 full coverage added in V-05.

---

The **Sizing Engineer** produces a **scout-size** sizing signal -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** -- exactly one per tier field.

Three phases. Phase N does not open until Phase N-1 is SEALED.

---

### Phase 0 -- Inertia Analyst

**Charter**: The Inertia Analyst produces exactly one section: Inertia Check.
**Does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size, Timeline, Confidence, Gap, Sensitivities, Calibration.

Cost Direction (which way) and Cost Trajectory (what shape) are distinct fields. A combined "Cost Trend" field fails C-37.

| Workaround [Inertia Analyst -- name the specific substitute] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "worsening", "improving" -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" without shape label, "worsening" alone, direction statement without shape, any non-vocabulary term -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: category label without tool or workflow name
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead" (no measurable dimension)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving",
        "increasing cost", "moderate impact", any non-vocabulary paraphrase
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" (directional, not shape); "getting worse" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

Phase 1 OPENS only when all five items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter**: Produces: Surface Area, Complexity Tier, Primary Driver, Team-Size, Timeline, Confidence Level + Basis, Tier-Up/Down Sensitivity, Confidence Calibration.
**Does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE**

Out-of-scope boundary: [named exclusion, or "No exclusions -- full scope assumed."]
Break-even signal: [at what level building recovers cost, or "Cannot assess -- [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL -- commit now]
  Timeline: [N-M sprints -- commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area, Complexity, Synthesis.
- Hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at anchor and verdict.

Do not populate any field below until gate is complete.

---

#### Surface Area [Sizing Analyst]

Do not include scope exclusions here.

| Integration Point [Sizing Analyst -- name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5 -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst] | FTE [FAIL: "part-time", "TBD" -- numeric required] | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: calendar reference, single-number estimate -- N-M format required] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5 -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: category labels; count absent
  [ ] Complexity Tier: exactly LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate"
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many dependencies"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: headcount only; FTE as "part-time" or "TBD"
  [ ] Timeline: N-M sprint range --
        FAIL: calendar reference; point estimate; range absent
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: unfalsifiable condition; destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: unfalsifiable condition; destination matches current tier
  [ ] Confidence Calibration: at least one entry per column --
        FAIL: either column empty

Phase 2 OPENS only when all nine items are confirmed.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter**: Produces exactly one field: Confidence Gap.
**Self-test**: "Could a reader derive my gap from Phase 1 by negation?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- must name a dimension Phase 1 did not reach] |
|---|
| Gap: [specific named unknown] -- [why it matters] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 1 by negation --
        FAIL: reversing any Phase 1 basis item produces this gap
  [ ] Gap names the dimension Phase 1 did not reach --
        FAIL: naming a dimension Phase 1 addressed
  [ ] Self-test applied and gap survived

Output Compilation OPENS only when all four items are confirmed.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction] / [trajectory: accel/stable/plateau/reverse] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5] | 1 | [level -- basis] |
| Confidence Gap | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here.

Unknown: / Impact: / Movement:

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two dimensions, including at least one Phase 0 inertia dimension]
Verdict: ["committed in PRE-FLIGHT GATE" phrase required at anchor and verdict]

Cross-signal directional observation after the verdict.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is present and amended dimension appears in cross-signal conclusion -- re-evaluate before closing.

---

### Per-Criterion Self-Check

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-37 | Five named fields; Cost Trajectory: accelerating/stable/plateauing/reversing; Direction and Trajectory structurally distinct | "+~N%/quarter" without shape; "worsening" as trajectory; Direction+Trajectory conflated | | |
| C-38 | PHASE SEALED at Phase 0, 1, and 2; each checklist with min 3 items naming specific fields and embedding exact disqualifying forms | Generic items; items name field but omit disqualifying form; single terminal block | | |
| C-36 | Every vocab-constrained column carries [FAIL:] tag | Cost Direction untagged; Confidence Level untagged; Tier-Destination untagged | PARTIAL -- minimum | |

*(All other self-check entries as per R12 V-05 baseline.)*

---

---

## V-05 -- Combined: V-01 + V-02 + V-03 -- Champion Attempt (C-37 + C-36 + C-38)

**Variation axis**: Inertia framing (C-37: accelerating/stable/plateauing/reversing) + Output format (C-36: [FAIL:] tags on ALL vocab-constrained columns) + Lifecycle emphasis (C-38: SEALED items embed disqualifying forms); third-person institutional register

**Hypothesis**: Maximum encoding for all three new v13 criteria. C-37: Cost Trajectory uses rubric vocabulary with [FAIL:] tag on every disqualifying form. C-36: every vocab-constrained column is tagged -- Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, Tier-Up/Down Destination. C-38: PHASE SEALED items embed exact disqualifying forms in every checkbox. Third-person institutional register frames the output as a specification to be satisfied. Three mechanisms address orthogonal failure modes and compose without interference. Champion attempt.

---

The **Sizing Engineer** produces a **scout-size** sizing signal for the named feature -- not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** -- exactly one form per tier field. Any other phrasing invalidates the field.

Three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional -- it is a structural gate.

---

### Phase 0 -- Inertia Analyst

**Charter governs this role. The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

Five dimensions required. Cost Direction (which way) and Cost Trajectory (what shape) are structurally separate fields. A combined "Cost Trend" field fails C-37.

> **WRONG**: "Teams use manual exports and things are getting harder." -- Cost absent; Direction absent; Trajectory absent; Key Driver absent.
> **CORRECT**: Workaround: Manual CSV export + re-import per sprint/team | Cost: ~45 min/sprint/team | Direction: more expensive | Trajectory: accelerating | Driver: team-count growth eliminates per-team variable if built

| Workaround [Inertia Analyst -- name the specific substitute; "None" requires cost-of-absence] | Ongoing Cost [Inertia Analyst -- at minimum: one time or error-rate dimension] | Cost Direction [Inertia Analyst -- FAIL: "neutral", "similar", "a wash", "moderate impact", "worsening", "improving", "getting worse", any non-vocabulary paraphrase -- exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst -- FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing] | Key Driver [Inertia Analyst -- one causal sentence -- restatement of cost is not a driver] |
|---|---|---|---|---|
| | | | | |

---

```
-- PHASE 0 SEALED --

The Inertia Analyst confirms ALL before Phase 1 opens:

  [ ] Workaround: specifically named --
        FAIL: "manual process" (category label); "some workaround" (not named)
  [ ] Ongoing Cost: at least one concrete dimension --
        FAIL: "significant overhead"; "some time" (no specificity)
  [ ] Cost Direction: exactly one of cheaper / comparable / more expensive --
        FAIL: "neutral", "similar", "a wash", "worsening", "improving", "more painful",
        "increasing cost", "moderate impact", any paraphrase not in vocabulary
  [ ] Cost Trajectory: exactly one of accelerating / stable / plateauing / reversing --
        FAIL: "+~20%/quarter" without shape label;
        "worsening" or "getting worse" (directional, not shape);
        "growing" (directional, not shape);
        Direction and Trajectory in single combined field
  [ ] Key Driver: names causal factor, not cost restatement --
        FAIL: "it takes too much time"; "the process is inefficient"

Phase 1 OPENS only when all five items are confirmed.
-- PHASE 0 CLOSED --
```

---

### Phase 1 -- Sizing Analyst

**Charter governs this role. The Sizing Analyst produces:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1-2 named factors)
4. Team-Size Signal (specialist disciplines + FTE + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE -- the Sizing Analyst resolves these before any analysis field**

Out-of-scope boundary:
[At least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions -- full scope assumed." "TBD" fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. inertia baseline? "Cannot assess -- [specific reason]" is valid. Absence fails C-10.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- committed before any analysis field]
Timeline: [N-M sprints -- committed before any analysis field]
Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

Scope exclusions do not appear here -- scope was resolved in PRE-FLIGHT GATE. Open unknowns do not appear here.

| Integration Point [Sizing Analyst -- name each individually -- "API layers", "database components" are category labels] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

Scope exclusions do not appear here.

| Complexity Tier [Sizing Analyst -- FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary phrasing -- exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst -- 1-2 named causal factors -- "it's complex", "many dependencies" fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

| Specialist Discipline [Sizing Analyst -- name the role; "engineer" alone fails] | FTE [Sizing Analyst -- FAIL: "part-time", "TBD", "as needed" -- numeric fraction required] | Implementation Ownership [Sizing Analyst -- what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

| Sprint Range [Sizing Analyst -- FAIL: any calendar reference (month/quarter/week), any single-number estimate ("4 sprints"), vague range ("a few sprints") -- N-M sprints only] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

| Confidence Level [Sizing Analyst -- FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", any non-tier phrasing -- exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified -- unknowns belong in Phase 2] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

| Direction | Single Named Falsifiable Condition | Destination Tier [Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
-- PHASE 1 SEALED --

The Sizing Analyst confirms ALL before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with numeric total --
        FAIL: "API layers" (category label); count absent
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL --
        FAIL: MODERATE, medium-high, 3/5, "complex", "intermediate", any non-vocabulary form
  [ ] Primary Driver: at least one named causal factor --
        FAIL: "it's complex", "many moving parts", "cross-system integration"
  [ ] Team-Size: at least one named discipline with numeric FTE --
        FAIL: "3 engineers" (no discipline); FTE as "part-time", "TBD", "as needed"
  [ ] Timeline: N-M sprint range --
        FAIL: "Q3 2026" (calendar); "4 sprints" (point estimate);
        "a few sprints" (no range); "6 weeks" (calendar unit)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with basis sentence --
        FAIL: level only, no basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition, higher destination --
        FAIL: "if scope expands" (unfalsifiable); destination matches current tier
  [ ] Tier-Down Sensitivity: one falsifiable condition, lower destination --
        FAIL: "if simpler than expected" (unfalsifiable); destination matches current tier
  [ ] Confidence Calibration: at least one entry in each column --
        FAIL: either column empty; single entry covering both

Phase 2 OPENS only when all nine items are confirmed.
-- PHASE 1 CLOSED --
```

---

### Phase 2 -- Risk Assessor

**Charter governs this role. The Risk Assessor produces exactly one field: Confidence Gap.**
**Does NOT produce**: Inertia Check (Phase 0), any Phase 1 field.

**Non-access rule**: Prohibited from citing as the gap: integration points Phase 1 enumerated, contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced, inertia dimensions Phase 0 established.

**Self-test**: "Could a reader look at Phase 0 and Phase 1 and derive this gap by reversing something either phase confirmed?" If yes: charter violation.

| Confidence Gap [Risk Assessor -- FAIL: any dimension Phase 0 or Phase 1 confirmed -- must name a dimension no phase reached -- must survive the self-test] |
|---|
| Gap: [specific named unknown] -- [why it matters to the sizing] |

---

```
-- PHASE 2 SEALED --

The Risk Assessor confirms ALL before Output Compilation:

  [ ] Gap names a specific unknown --
        FAIL: "further investigation needed"; "dependencies may exist"; category hedges
  [ ] Gap cannot be derived from Phase 0 or Phase 1 by negation --
        FAIL: reversing any Phase 0 or Phase 1 confirmed item produces this gap
  [ ] Gap names the dimension neither phase reached --
        FAIL: naming a dimension either phase addressed, even with different framing
  [ ] Self-test applied and gap survived it

Output Compilation OPENS only when all four items are confirmed.
-- PHASE 2 CLOSED --
```

---

### Output Compilation

**SIZING SIGNAL -- [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia (5-field) | 0 | [workaround] / [cost] / [direction: cheaper/comparable/more expensive] / [trajectory: accelerating/stable/plateauing/reversing] / [driver] |
| Surface Area | 1 | [named points -- N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 -- only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1-2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate -- only: N-M sprints] | 1 | [N-M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 -- only: HIGH / MEDIUM / LOW] | 1 | [level -- basis] |
| Confidence Gap [must name dimension no phase reached] | 2 | [unknown -- why it matters] |
| Tier-Up Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [FAIL: same tier, non-vocabulary -- must differ: LOW / MEDIUM / HIGH / XL] | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Scope exclusions do not appear here. Confidence Gap does not appear here.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence is juxtaposition. The cross-signal conclusion must require two or more dimensions to state.

The Sizing Engineer confirms or revises the preliminary hypothesis committed in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines appear on separate lines.

Commitment chain:
Gate commitment: [tier from PRE-FLIGHT GATE] / [sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0-2 -- at least two signal dimensions, including at least one Phase 0 inertia dimension]
Verdict: [one standard form -- "committed in PRE-FLIGHT GATE" required at anchor AND verdict]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict: cross-signal directional observation combining at least two dimensions.

Scope exclusions do not appear here. Open unknowns do not appear here.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This directive applies on every invocation. When AMEND is absent -- confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion or verdict -- re-evaluate before closing.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion by ID with PASS / PARTIAL / FAIL and cites evidence. Separate verification artifact.

**Essential criteria (C-01 through C-05):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-01 | Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex", "intermediate" as tier label | | |
| C-02 | Timeline: sprint range with both bounds | Calendar date; point estimate; "a few sprints"; any non-N-M format | | |
| C-03 | Surface area: names or counts at least 2 distinct integration points | "Moderate surface area"; "several integrations" with no named points | | |
| C-04 | Labeled inertia section: workaround + at least one cost dimension | Section absent; names only the feature request | | |
| C-05 | Confidence level stated AND at least one reason given | "Confidence: MEDIUM" with no follow-on sentence | | |

**Recommended criteria (C-06 through C-08):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-06 | Team-size: at least one role/specialization named | "3 engineers" with no role labels | | |
| C-07 | At least one sentence names what pushed the complexity tier | Bare tier label with no justification | | |
| C-08 | If AMEND present: substantive change traceable to directive. Default PASS if absent | AMEND invoked; output identical to non-amended run | | |

**Aspirational criteria (C-09 through C-38):**

| ID | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|
| C-09 | At least one explicit exclusion or out-of-scope boundary | Only inclusions listed; no boundary statement | | |
| C-10 | Break-even estimate OR "cannot assess -- [reason]" | Inertia cost described; no break-even reference | | |
| C-11 | At least one named specialization includes implementation scope | Role list with no ownership area | | |
| C-12 | At least one concrete unknown that would move confidence if resolved | "LOW due to uncertainty" with no named unknown | | |
| C-13 | At least one sentence cross-referencing two+ dimensions for directional observation | "Complexity is HIGH. Timeline is 4-6 sprints." (sequential restatement) | | |
| C-14 | Named section with Unknown/Impact/Movement fields or "No open unknowns" | Unknowns embedded in confidence basis; no separate section | | |
| C-15 | Prior hypothesis stated before analysis; synthesis explicitly confirms/revises/partially revises | Synthesis matching hypothesis with no confirmation statement | | |
| C-16 | If AMEND changes synthesis-cited dimension: synthesis re-evaluated. Default PASS if no AMEND | AMEND changes complexity; synthesis unchanged and not reaffirmed | | |
| C-17 | At least one aspirational section names the anti-pattern being avoided | Section avoiding failure mode with no statement of what it is | | |
| C-18 | Structural gate before Surface Area, Complexity, Confidence fields | Inline reminder substituted for structural gate | | |
| C-19 | At least one adjacent section carries explicit prohibition against canonical field type | Confidence basis with no prohibition against unknowns | | |
| C-20 | Every section that could receive canonical field type is explicitly closed | Synthesis with no prohibition against scope exclusions | | |
| C-21 | Gate requires tier + timeline commitment before first analysis section | Gate with scope only; no hypothesis commitment | | |
| C-22 | Synthesis names PRE-FLIGHT GATE at commitment anchor AND at verdict | "My earlier estimate" without structural label | | |
| C-23 | At least one prohibition guard names canonical home by label | "Do not include scope here" without naming home | | |
| C-24 | Gate commitment, analysis evidence, verdict on separate labeled lines | Single prose paragraph containing all three steps | | |
| C-25 | PRE-FLIGHT GATE names at least two downstream enforcement sections | Gate with scope but no mention of enforcement sections | | |
| C-26 | Synthesis contains written directive requiring re-evaluation when AMEND affects cited dimension | C-16 behavioral compliance but no written structural directive | | |
| C-27 | Every aspirational section with nontrivial pass condition has dedicated labeled FAILURE MODE block | Anti-pattern awareness in prose; no dedicated block | | |
| C-28 | Separate self-check block traces each aspirational criterion by ID with pass/fail + evidence | Self-check absent; collapsed into content sections | | |
| C-29 | C-18 through C-27, C-33, C-35, C-36, C-38 items have pass condition + disqualifying form | Structural criterion entry with pass condition only | | |
| C-30 | C-09 through C-17, C-34, C-37 items have pass condition + disqualifying form | Depth criterion entry with pass condition only | | |
| C-31 | Self-check includes C-01 through C-08 in addition to C-09-C-38 | Self-check covers C-09-C-38 with C-01-C-08 absent | | |
| C-32 | C-01 through C-08 self-check items have pass condition + disqualifying form | Essential criterion entry with evidence but no disqualifying form | | |
| C-33 | Inertia section in document order before complexity tier, timeline, surface area, confidence | Inertia after PRE-FLIGHT GATE preliminary tier is committed | | |
| C-34 | Inertia entry: Workaround, Ongoing Cost, Cost Direction, Key Driver as named fields | Workaround + cost named; Key Driver absent | | |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline column headers | Any vocab-constrained column present without [FAIL:] tag | | |
| C-36 | Every vocab-constrained column carries [FAIL:] tag: Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory, Tier-Up/Down Destination | Satisfying C-35 minimum while leaving Cost Trajectory, Confidence Level, or Tier-Destination untagged | | |
| C-37 | Five named fields: Workaround, Ongoing Cost, Cost Direction, Cost Trajectory (accelerating/stable/plateauing/reversing), Key Driver; Direction and Trajectory structurally distinct | "+~N%/quarter" without shape label; "worsening" as trajectory; Direction+Trajectory conflated in single field | | |
| C-38 | PHASE SEALED at Phase 0, 1, and 2; each checklist with min 3 items naming specific fields and embedding exact disqualifying forms | Single terminal block; generic items; items name field but omit disqualifying form | | |

---

```json
{
  "skill": "scout-size",
  "round": 13,
  "rubric": "v13",
  "aspirational_denominator": 30,
  "r12_champion_candidate": "V-05 R12 (unscored under v13)",
  "r13_target": "30/30 aspirational -- all three new criteria in a single variation",
  "axes": {
    "V-01": "inertia-framing-C37-vocabulary-correction",
    "V-02": "output-format-C36-full-coverage",
    "V-03": "lifecycle-emphasis-C38-sealed-items-with-disqualifying-forms",
    "V-04": "combined-C37-plus-C38",
    "V-05": "combined-all-three-C37-C36-C38-champion-attempt"
  }
}
```
