# Scout-Size Prompt Variations — R6
**Skill**: scout-size
**Rubric**: v6 (20 criteria, C-01 through C-20)
**Date**: 2026-03-16

---

## V-01 — Role Sequence

**Variation axis**: Role sequence (two named roles with explicit charters, sequential production)
**Hypothesis**: Sequential role execution with explicit non-overlap charters between Sizing Analyst and Risk Assessor structurally prevents confidence basis/gap conflation (C-15, C-20) by making conflation a charter violation rather than a rule violation. The Risk Assessor's charter statement is the structural guard — violating C-15 requires the assessor to break their own explicitly stated mandate.

---

You are running a **scout-size** sizing signal for the feature described below. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Complexity tier vocabulary** — use exactly one, no substitutions: **LOW / MEDIUM / HIGH / XL**

---

## Phase 1 — Sizing Analyst

**Your charter**: Enumerate what exists and what must be touched. Produce structural facts. Do not produce the confidence gap — that is the Risk Assessor's charter in Phase 2.

### 1.1 Surface Area

Name each integration point individually and provide a total count.

Format: "API endpoint (auth), event bus subscription (order-placed), DB schema migration — 3 integration points"

Required: named individual points AND a count. A general description such as "several API layers" without named points and a count fails this field.

### 1.2 Complexity Tier

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**

Then name the one or two factors that most drive this rating. "It's complex" is not a complexity driver.

### 1.3 Team-Size Signal

Name the specialist disciplines needed — not just headcount.

Format: "1 backend engineer, 1 platform engineer, 0.5 PM" — not "3 engineers"

### 1.4 Timeline Signal

Give a sprint range. Not a calendar date. Not a single fixed number. The range communicates appropriate uncertainty.

Format: "3–5 sprints"

### 1.5 Confidence Basis

State your confidence level (HIGH / MEDIUM / LOW) and name what IS established or verified — the specific dimension that supports the rating.

Format: "MEDIUM — surface area is fully enumerated and the API contract is established; webhook delivery semantics under load have not been verified."

A bare "confidence: HIGH" with no basis fails.

**Stop here. Do not produce the confidence gap. That is the Risk Assessor's charter.**

---

## Phase 2 — Risk Assessor

**Your charter**: Name what the Sizing Analyst did NOT verify or establish. You are explicitly prohibited from restating or negating what the Analyst confirmed. The gap must address a different dimension of confidence than the basis — not the same dimension with opposite polarity.

Charter violation test: If your gap says "X is not confirmed" and the Analyst's basis says "X is established," you have violated your charter. Start over and name a different dimension.

### 2.1 Confidence Gap

Name the specific thing that is NOT yet known or verified — the primary source of residual uncertainty.

This must address a different aspect than the Analyst's basis. If the Analyst confirmed the API contract, the gap must name something else — delivery guarantees, error semantics, rate limiting behavior, load characteristics.

Format: "Gap: webhook delivery guarantees under concurrent load are unverified — at-least-once vs exactly-once semantics affect the error handling surface area."

### 2.2 Inertia Check

Name the current workaround (or state "no workaround exists") and give a directional cost judgment.

Format: "[Workaround name] — building is [cheaper / comparable / more expensive] than maintaining. [One sentence of reasoning.]"

An output that mentions the workaround without a cost direction fails this field.

### 2.3 Sensitivity Conditions

State one condition that would push the complexity tier **up** and one that would push it **down**.

Each condition must be:
- A single, named, specific scenario — not a list of factors
- Named with the explicit destination tier (LOW / MEDIUM / HIGH / XL)
- Falsifiable — a reader must be able to state what investigation would settle it
- Landing on a tier **different** from the currently assigned tier

Format:
- Tier rises to [LEVEL] if: [single named condition — how to confirm: ...]
- Tier drops to [LEVEL] if: [single named condition — how to confirm: ...]

### 2.4 Confidence Calibration

State what information or investigation result would materially raise or lower the stated confidence level.

---

## Output Structure

Produce two clearly labeled sections: **Phase 1 — Sizing Analyst** and **Phase 2 — Risk Assessor**. Do not merge them. Do not reorder the phases.

---

---

## V-02 — Structural Format Encoding

**Variation axis**: Output format (schema-level structural constraints via column headers and field labels)
**Hypothesis**: Encoding constraints as column headers and named field slots makes violations observable at the field level without requiring the reader to cross-reference prose rules. A column labeled `[destination tier — must differ from current: LOW / MEDIUM / HIGH / XL]` is harder to violate than a prose note, because a violation is visible in the output skeleton itself before scoring begins.

---

You are running a **scout-size** sizing signal for the feature described below. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

This signal feeds `program-plan`. Downstream skills parse the complexity tier. **Use exactly**: LOW / MEDIUM / HIGH / XL — no substitutions ("MODERATE", "3/5", and "complex" all fail).

Complete the following structured output. Constraints are embedded in the field labels — satisfy them as schema requirements, not as suggestions.

---

### SURFACE AREA

| Integration Point [name individually] | Type |
|---------------------------------------|------|
| | [API / hook / event / DB / UI / other] |
| | |
| **Total** | **[N] integration points** |

The Total row is required. "Several API interactions" is not a named integration point.

---

### COMPLEXITY TIER

**Tier [exactly one: LOW / MEDIUM / HIGH / XL]**:

**Primary driver [one or two named factors — not "it's complex"]**:

---

### TEAM-SIZE SIGNAL

| Specialist Type [name the discipline] | FTE Fraction |
|---------------------------------------|--------------|
| | |
| **Total FTEs** | |

"3 engineers" alone fails — name the disciplines.

---

### TIMELINE SIGNAL

**Sprint range [N–M format — not a calendar date, not a single number]**:

---

### CONFIDENCE

**Level [HIGH / MEDIUM / LOW]**:

**Basis [what IS established or verified — name the dimension]**:

**Gap [what is NOT yet known — must address a DIFFERENT dimension than the Basis field above]**:

> Non-overlap rule: The gap field cannot negate or restate the basis. If the basis names "API contract is established," the gap must name a different dimension — delivery behavior, error semantics, rate limiting, load characteristics. A gap that says "API contract is not yet confirmed" when the basis says "API contract is established" violates this rule.

---

### SENSITIVITY

| Direction | Destination Tier [must differ from current tier: fill with LOW / MEDIUM / HIGH / XL] | Single Named Condition [falsifiable — state how to confirm] |
|-----------|---------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Tier rises to | [must be HIGHER than the tier assigned above] | |
| Tier drops to | [must be LOWER than the tier assigned above] | |

Conditions that cannot be investigated ("if requirements change," "if scope grows") fail the falsifiability requirement. Each condition must name what action would settle it.

---

### INERTIA CHECK

**Current workaround [name it, or "none"]**:

**Cost direction [building is: cheaper / comparable / more expensive than maintaining the workaround]**:

**Reasoning [one sentence]**:

An output that mentions the workaround without a cost direction fails this field.

---

### CONFIDENCE CALIBRATION

**What would materially raise confidence**:

**What would materially lower confidence**:

---

---

## V-03 — Inline Failure Examples

**Variation axis**: Inline failure examples preceding output fields (C-17, C-19)
**Hypothesis**: Placing WRONG/CORRECT blocks immediately before each high-risk field — not in a post-output checklist — makes the failure mode active at generation time. A model that encounters the failure example before completing the field cannot satisfy the field without the constraint being active. Post-output checklists may catch failures during human review; they cannot prevent generation-time drift.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan.

**Signal boundary**: No task breakdowns, sprint assignments, owner names, or milestone dates. This signal answers "how big?" — not "who does what when?"

This signal feeds `program-plan`. The tier vocabulary is parsed downstream. Use only: **LOW / MEDIUM / HIGH / XL**.

---

### Field 1 — Surface Area

> **WRONG**: "The feature touches several API layers and some UI components."
> **CORRECT**: "API endpoint (auth), event bus subscription (order-placed), DB schema migration, UI form component — 4 integration points."

Required: named individual points AND a count. General descriptions without named points fail.

**Your output**:

---

### Field 2 — Complexity Tier

> **WRONG**: "MODERATE complexity" — not on scale.
> **WRONG**: "Complexity: 3/5" — not on scale.
> **WRONG**: "This is a complex feature" — no tier assigned.
> **CORRECT**: "HIGH"

Assign exactly one: **LOW / MEDIUM / HIGH / XL**

**Your tier**:

**Primary complexity driver** [one or two named factors — not "it's complex"]:

---

### Field 3 — Team-Size Signal

> **WRONG**: "3 engineers"
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

Name the specialist disciplines, not just headcount.

**Your output**:

---

### Field 4 — Timeline Signal

> **WRONG**: "Q3 delivery"
> **WRONG**: "4 sprints" — single number, no range
> **CORRECT**: "3–5 sprints"

Give a sprint range.

**Your output**:

---

### Field 5 — Confidence Basis

> **WRONG**: "Confidence: HIGH" — no basis stated.
> **CORRECT**: "MEDIUM — surface area is fully enumerated and the API contract is established; webhook delivery semantics under load have not been verified."

State your confidence level (HIGH / MEDIUM / LOW) and name what IS established or verified.

**Your output**:

---

### Field 6 — Confidence Gap

> **WRONG** (violates non-overlap — same dimension, opposite polarity):
> Basis: "API contract is established." Gap: "API contract has not been confirmed."
>
> **CORRECT** (different dimension):
> Basis: "API contract is established." Gap: "Webhook delivery guarantees under concurrent load are unverified — at-least-once vs exactly-once semantics affect error handling surface area."

Name the specific thing that is NOT yet known. This must address a DIFFERENT dimension than Field 5 (the basis). The gap cannot negate or restate the basis.

**Your output**:

---

### Field 7 — Sensitivity: Tier-Up Condition

> **WRONG** (vague, not a condition): "Several factors could push the tier up."
> **WRONG** (not falsifiable): "If requirements change."
> **WRONG** (same tier as current — vacuous): Current tier is HIGH. "Tier rises to HIGH if offline sync is required."
> **CORRECT**: "Tier rises to XL if offline sync with conflict resolution is required — confirm by reviewing the offline mode section of the product spec."

State one single, named, falsifiable condition that would push the tier HIGHER. Name the destination tier explicitly. The destination must differ from the current tier.

**Format**: "Tier rises to [LEVEL] if: [single named condition — how to confirm: ...]"

**Your output**:

---

### Field 8 — Sensitivity: Tier-Down Condition

> **WRONG** (same tier as current — vacuous): Current tier is MEDIUM. "Tier drops to MEDIUM if the auth layer is already abstracted."
> **CORRECT**: "Tier drops to LOW if the auth layer exposes a pre-built hook that handles all session management — confirm by reviewing the auth team's API surface documentation."

State one single, named, falsifiable condition that would push the tier LOWER. Name the destination tier explicitly. The destination must differ from the current tier.

**Format**: "Tier drops to [LEVEL] if: [single named condition — how to confirm: ...]"

**Your output**:

---

### Field 9 — Inertia Check

> **WRONG**: "Users currently use a spreadsheet." — workaround named, no cost direction.
> **CORRECT**: "Current workaround: manual CSV export plus spreadsheet reconciliation. Cost direction: building is cheaper — the workaround costs approximately 2 hours per team per week and does not scale past 100 records."

Name the current workaround and give a directional cost judgment: cheaper / comparable / more expensive than building.

**Your output**:

---

### Field 10 — Confidence Calibration

State what would materially raise or lower the stated confidence level.

**Your output**:

---

---

## V-04 — Inertia Framing

**Variation axis**: Inertia framing prominence (status-quo as the opening analytical lens)
**Hypothesis**: Making the inertia check the first analytical step — before surface area or complexity — anchors all subsequent fields in status-quo comparison. When the cost of maintaining the workaround is established first, complexity and confidence fields are interpreted relative to a concrete baseline, producing more grounded judgments and making C-03's requirement emerge from the analytical structure rather than as a late checklist obligation.

---

You are running a **scout-size** sizing signal. This signal answers: "How big is this relative to the status quo?" — not "What is the project plan?"

**Signal boundary**: No task breakdowns, sprint assignments, owner names, or milestone dates.

Complexity tier vocabulary is parsed downstream. Use exactly: **LOW / MEDIUM / HIGH / XL**.

---

## Step 1 — Status-Quo Baseline (Run This First)

Before estimating the feature, name what exists today.

**Current workaround** [or "none"]:
Name what users or the system does today to compensate for this feature's absence.

**Cost direction**:
Is building this feature cheaper, comparable, or more expensive than maintaining the current workaround? Give one sentence of reasoning.

An output that mentions the workaround without a cost direction fails this field.

> The rest of this output is interpreted relative to this baseline. A HIGH complexity signal against a cheap, stable workaround is a strong signal to defer. A HIGH complexity signal against an expensive or fragile workaround may still justify building. Name the workaround cost first so the sizing numbers carry that context.

---

## Step 2 — Surface Area

Name each integration point the feature must touch. Provide a total count.

Format: "[Point 1], [Point 2], [Point 3] — N integration points"

A general description without named points and a count fails this field.

---

## Step 3 — Complexity Tier

Assign exactly one: **LOW / MEDIUM / HIGH / XL**

Name the one or two factors that most drive this rating. "It's complex" is not a complexity driver.

---

## Step 4 — Team-Size Signal

Name the specialist disciplines needed. Headcount alone fails.

Format: "1 backend engineer, 1 platform engineer, 0.5 PM"

---

## Step 5 — Timeline Signal

Give a sprint range — not a calendar date, not a single fixed number.

Format: "N–M sprints"

---

## Step 6 — Confidence

**Level** [HIGH / MEDIUM / LOW]:

**Basis** [what IS established or verified — name the specific dimension that supports the rating]:

**Gap** [what is NOT yet known — the primary source of residual uncertainty]:

Non-overlap requirement: Basis and gap must address different dimensions. The basis names what makes you confident in what you do know; the gap names what you cannot yet confirm. If your basis is "API contract is established," your gap must name a different dimension — delivery behavior, error semantics, load characteristics — not "API contract is unconfirmed."

**Calibration** [what investigation result would materially raise or lower the confidence level]:

---

## Step 7 — Sensitivity

Two conditions: one that pushes the tier up, one that pushes it down.

Each condition must:
- Be a single named scenario — not a list, not a hedge
- Name the destination tier explicitly (LOW / MEDIUM / HIGH / XL)
- Land on a tier **different** from the currently assigned tier
- Be falsifiable: name what action would settle it

"If requirements change" is not a condition — it is a deferral. A condition names a specific, discoverable fact that would cause the tier to move.

Format:
- Tier rises to [LEVEL] if: [single named condition — how to confirm: ...]
- Tier drops to [LEVEL] if: [single named condition — how to confirm: ...]

---

---

## V-05 — Multi-Axis Combination

**Variation axes**: Role sequence + structural format encoding + inline failure examples preceding output fields
**Hypothesis**: Combining all three architectural mechanisms — (1) role separation making basis/gap conflation a charter violation rather than a rule violation, (2) schema-level column headers making tier violations visible in the output skeleton, and (3) inline WRONG/CORRECT blocks placed before each high-risk field making failure modes active at generation time — produces the strongest multi-layer constraint satisfaction across the full rubric. Each mechanism guards a different failure mode; together they remove the three largest vectors for rubric drift.

---

You are running a **scout-size** sizing signal for the feature described below. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`.

**Tier vocabulary** — parsed downstream, no substitutions: **LOW / MEDIUM / HIGH / XL**

---

# PHASE 1 — Sizing Analyst

**Your charter**: Enumerate what exists and what must be touched. Produce structural facts. Do not produce the confidence gap — that is the Risk Assessor's charter in Phase 2. Producing the gap in Phase 1 is a charter violation.

---

### 1. Surface Area

> **WRONG**: "The feature touches several API layers and some UI components."
> **CORRECT**: "API endpoint (auth), event bus subscription (order-placed), DB schema migration, UI form — 4 integration points."

| Integration Point [name each individually] | Type |
|---------------------------------------------|------|
| | [API / hook / event / DB / UI / other] |
| | |
| **Total** | **[N] integration points** |

---

### 2. Complexity Tier

> **WRONG**: "MODERATE" / "3/5" / "complex"
> **CORRECT**: "HIGH"

**Tier [exactly one: LOW / MEDIUM / HIGH / XL]**:

**Primary driver [one or two named factors — not "it's complex"]**:

---

### 3. Team-Size Signal

> **WRONG**: "3 engineers"
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Type [name the discipline] | FTE Fraction |
|---------------------------------------|--------------|
| | |
| **Total FTEs** | |

---

### 4. Timeline Signal

> **WRONG**: "Q3 delivery" / "4 sprints"
> **CORRECT**: "3–5 sprints"

**Sprint range [N–M format]**:

---

### 5. Confidence Basis

> **WRONG**: "Confidence: HIGH" — no basis stated.
> **CORRECT**: "MEDIUM — surface area is fully enumerated and the API contract is established; webhook delivery under load has not been verified."

**Level [HIGH / MEDIUM / LOW]**:

**Basis [what IS established — name the specific dimension]**:

**STOP. Do not produce the confidence gap. Pass to Phase 2.**

---

# PHASE 2 — Risk Assessor

**Your charter**: Name what the Sizing Analyst did NOT verify. You are explicitly prohibited from restating or negating what the Analyst confirmed. The gap must address a different dimension of confidence than the basis.

**Charter violation test**: If your gap says "X is not confirmed" and the Analyst's basis says "X is established," you have violated your charter. Stop and name a different dimension entirely.

---

### 6. Confidence Gap

> **WRONG** (charter violation — same dimension, opposite polarity):
> Basis: "API contract is established."
> Gap: "API contract has not been confirmed."
>
> **CORRECT** (different dimension):
> Basis: "API contract is established."
> Gap: "Webhook delivery guarantees under concurrent load are unverified — at-least-once vs exactly-once semantics affect the error handling surface area."

**Gap [what is NOT yet known — different dimension than the Analyst's basis]**:

---

### 7. Inertia Check

> **WRONG**: "Users currently use a spreadsheet." — named but no cost direction.
> **CORRECT**: "Workaround: manual CSV export plus spreadsheet reconciliation. Cost direction: building is cheaper — costs ~2 hr/team/week and does not scale past 100 records."

**Current workaround [or "none"]**:

**Cost direction [building is: cheaper / comparable / more expensive]**:

**Reasoning [one sentence]**:

---

### 8. Sensitivity

> **WRONG** (vague): "Several factors could push the tier up."
> **WRONG** (not falsifiable): "If requirements change."
> **WRONG** (same tier as current — vacuous): Current tier is HIGH. "Tier rises to HIGH if offline sync is required."
> **CORRECT**: "Tier rises to XL if offline sync with conflict resolution is required — confirm by reviewing the offline mode section of the product spec."

| Direction | Destination Tier [fill with LOW / MEDIUM / HIGH / XL — must DIFFER from current tier] | Single Named Condition [falsifiable — state how to confirm] |
|-----------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Tier rises to | [must be HIGHER than the tier in Field 2] | |
| Tier drops to | [must be LOWER than the tier in Field 2] | |

---

### 9. Confidence Calibration

**What would materially raise confidence**:

**What would materially lower confidence**:
