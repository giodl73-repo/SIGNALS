Now I have everything I need. The key structural findings:

1. **C-40**: All R15 variations use a footer note below the compilation table (`_Confidence Gap: See…_`). C-40 requires a named **table row** with a pointer — not a footer note.
2. **C-41**: R15 CLOSED-LABEL headers have `[fill only if BLOCKED…]` — but C-41 requires **both** conditions: when to fill AND when to leave blank. R16 needs `[fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — name the failed precondition]`.

**Expected R16 score for multi-phase + C-40 + C-41**: 32/33 aspirational = 9.70 → **total 99.70**  
(Only C-28 structurally fails for multi-phase; C-27 becomes vacuous via C-40.)

---

# Scout-Size Prompt Variations — R16

**Skill**: scout-size  
**Rubric**: v16 (33 aspirational criteria, C-01 through C-41)  
**Date**: 2026-03-17  
**Round**: 16  
**R15 champion**: V-05 — three-phase; ENTRY GATE visual delimiter; Phase 0 gate table with STATUS + CLOSED-LABEL + EVIDENCE columns (C-38); four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION field (C-39); C-32 gap standalone section; C-30 defense cluster  
**R15 gaps**: All V-03/V-04/V-05 FAIL C-27 (gap excluded from compilation table as footer note, not named table row) and C-28 (multi-phase, structurally inapplicable); V-01/V-02 also FAIL C-40 (footer note not a named table row); V-03/V-04/V-05 FAIL C-41 (CLOSED-LABEL header specifies fill condition but not leave-blank condition)

---

## Context: What R16 Addresses

v16 adds two new aspirational criteria formalized from R15 excellence signals:

| New criterion | What it formalizes | R15 evidence |
|---------------|-------------------|--------------|
| C-40 | Compilation table gap slot carries a named pointer row to the standalone section when C-32 is used | R15 V-03 excludes the gap from the compilation table and uses a pointer reference (causing C-27 FAIL), which is architecturally correct when C-32 is in effect — C-40 validates this as an excellence pattern; but R15 variations implemented the pointer as a footer note below the table rather than a named row within the table |
| C-41 | CLOSED-LABEL column header encodes its conditional fill constraint (both populate-when-BLOCKED and leave-blank-when-CLEAR explicitly stated) | R15 V-01/V-02 move toward this with `[fill only if BLOCKED…]` headers; the full conditional requires naming both states so the model cannot fill CLOSED-LABEL on a CLEAR row or leave it blank on a BLOCKED row without understanding why |

The primary architectural change in R16: promote the `_Confidence Gap: See … section above._` footer note into a named table row within the compilation table, and upgrade the CLOSED-LABEL column header to specify both fill conditions.

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence (two-phase minimal — C-40 + C-41 added to V-03 base) | C-40 requires a Confidence Gap row in the compilation table; C-41 requires both fill and leave-blank conditions in CLOSED-LABEL header. V-01 makes exactly these two targeted changes to the V-03 two-phase architecture and no others. Hypothesis: both new patterns are straightforward row/header changes that achieve 32/33 without any architectural overhead. |
| V-02 | Phrasing register (single-phase second-person — C-40 + C-41 added to V-02 base) | Single-phase retains C-28 (self-test in gap field body) while losing the C-20 cluster. V-02 second-person phrasing applies "your CLOSED-LABEL" and "leave blank when your status is CLEAR" framing — testing whether the personal-address register makes the conditional constraint more behaviorally immediate. Hypothesis: second-person conditional header reduces contradictory-state fills more than third-person equivalent. |
| V-03 | Lifecycle emphasis (lifecycle-heavy Phase 0 — C-40 + C-41 added to V-04 base) | V-04's Phase 0 retains per-precondition narrative sections before the gate-decision table. C-41 conditional fill interacts with this layout: the per-precondition sections can prime the BLOCKED/CLEAR determination before the model fills the table row. Hypothesis: narrative context before the table plus conditional header in the table together prevent contradictory-state fills through two different mechanisms. |
| V-04 | Inertia framing (inertia-first analytical frame — new axis; two-phase + C-40 + C-41) | Existing variations treat inertia as a gate precondition. V-04 elevates it as the primary analytical lens: Phase 1 Sizing Analyst computes complexity delta from workaround rather than absolute complexity. Hypothesis: framing complexity as "how much harder is this than maintaining the workaround" anchors the tier rating to a known baseline and reduces complexity inflation. |
| V-05 | Output format + role sequence (champion evolution — C-40 + C-41 + EVIDENCE column symmetry pioneer) | R15 V-05 adds EVIDENCE column for CLEAR verdicts. R16 V-05 extends the pioneer pattern: the EVIDENCE column for CLEAR is matched by a "CLEAR-PATH" column for BLOCKED verdicts — naming the specific investigation that would resolve the block and allow re-running the gate. Bidirectional schema coverage: BLOCKED rows know their CLOSED-LABEL; CLEAR rows name their EVIDENCE; BLOCKED rows also name their resolution path. Hypothesis: CLEAR-PATH column on BLOCKED rows generates the next round's excellence signal. |

---

## V-01 — Axis: Role sequence (Two-phase minimal — C-40 + C-41 targeted additions to V-03 base)

**Variation axis**: Role sequence — two-phase architecture (Phase 1: Sizing Analyst, Phase 2: Risk Assessor) with full C-20/C-23/C-24/C-25/C-26/C-29 cluster; Phase 0 as formal two-row precondition table with C-38/C-41 compliant headers; Confidence Gap promoted to named compilation table row with pointer (C-40); no other changes from R15 V-03.

**Hypothesis**: R15 V-03 achieved 29/31 aspirational (only C-27 and C-28 failed). C-27 fails because the gap pointer is a footer note below the table; C-28 fails because multi-phase design makes it structurally inapplicable. C-40 resolves C-27 by validating the pointer as architecturally correct when C-32 is used — but requires a named table ROW, not a footer note. V-01 makes exactly two changes: (a) footer note → named table row with pointer (C-40); (b) CLOSED-LABEL header upgraded to specify both fill and leave-blank conditions (C-41). Expected result: 32/33 aspirational (99.70 composite).

---

You are running a **scout-size** sizing signal in two phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" are not valid tier values.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## Phase 0: Entry Gate

**Charter**: Verify that sizing can begin. Fill the precondition table below. Both rows must be CLEAR before Phase 1 is permitted.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "CLOSED — Precondition [A/B]: [name what is missing or detected]"] |
|-------------|-------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')."
> **Example — both CLEAR**: Status: CLEAR. CLOSED-LABEL: — (leave blank). Gate = OPEN.

| Precondition A detail: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|----------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst [begins after Phase 0 Gate = OPEN]

**Charter**: Produce the sizing foundations. Do NOT produce confidence gap, confidence calibration, or tier sensitivity — those are Phase 2's output.

**Fields owned by Phase 1**: Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "API and database integrations." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order-placed), DB migration (orders table) — **3 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type |
|---------------------------------------------------------------------|------|
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "3/5" — Off-vocabulary. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "3 engineers." — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM."

| Specialist Discipline [Phase 1 Sizing Analyst — name the role, not just "engineer"] | FTE |
|--------------------------------------------------------------------------------------|-----|
| | |
| **Total** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "6 weeks" / "4 sprints" — Calendar unit; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|----------------------------------------------------|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State confidence and name what IS established. Unknowns belong to Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap checkpoint, confidence calibration, and tier sensitivity.

**Non-access clause**: Your confidence gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Sizing Analyst confirmed in P1-5 as the source of your gap.

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is stable," "integration points are enumerated." Negating these items in your gap is a charter violation regardless of framing.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce — owned by Phase 0 / Phase 1]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Identify the primary source of residual uncertainty. Must address a different dimension than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract is unconfirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from P1-5 by negation alone
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; a basis-negation gap consumes the gap field without reducing uncertainty

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

---

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Stop. Restate to name a dimension Phase 1 did not confirm.
> If no: write your gap below.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

Gap: _____

---

### P2-2: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence [Phase 2 Risk Assessor] | What Would Lower Confidence [Phase 2 Risk Assessor] |
|-----------------------------------------------------|-----------------------------------------------------|
| | |

---

### P2-3: Tier Sensitivity [Phase 2 Risk Assessor]

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section."

> **WRONG tier-down**: "Tier drops to MEDIUM if simpler." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — one scenario — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current tier — fill LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from all phases:

**SIZING SIGNAL — [feature name]**

| Field | Produced By | Value |
|-------|-------------|-------|
| Inertia Check | [Phase 0 Entry Gate] | [workaround — cost direction — one sentence] |
| Surface Area | [Phase 1 Sizing Analyst] | [named points — N integration points] |
| Complexity Tier | [Phase 1 Sizing Analyst] | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [Phase 1 Sizing Analyst] | [1–2 named factors] |
| Team-Size Signal | [Phase 1 Sizing Analyst] | [specialist disciplines + fractions] |
| Timeline Signal | [Phase 1 Sizing Analyst] | [N–M sprints] |
| Confidence Level + Basis | [Phase 1 Sizing Analyst] | [LEVEL — what is established] |
| Confidence Gap | [Phase 2 Risk Assessor] | → see ── CONFIDENCE GAP CHECKPOINT ── section above |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |

---

---

## V-02 — Axis: Phrasing register (Single-phase second-person — C-40 + C-41 added to V-02 base)

**Variation axis**: Phrasing register — all instructions addressed in second person ("your gap," "your CLOSED-LABEL," "leave blank when your status is CLEAR"); single-phase design (no role separation); C-40 compilation table pointer row; C-41 second-person conditional fill header.

**Hypothesis**: Single-phase retains C-28 (self-test in gap field body) and C-35/C-36/C-38/C-39, but loses the C-20 cluster (C-20, C-23, C-24, C-25, C-26, C-29). The second-person register makes the C-41 conditional constraint personal: "fill only when YOUR STATUS is BLOCKED — leave blank when YOUR STATUS is CLEAR" applies the constraint to the model's own immediate production act, not to a third-party description. Hypothesis: first-person CLOSED-LABEL instructions reduce contradictory-state fills by making the fill condition an instruction to the specific model role producing the row, not a general policy statement. Expected: 27/33 aspirational (98.18 composite). The CLEAR/BLOCKED conditional header is slightly different wording than V-01's third-person form; this tests whether register alone affects C-41 behavioral fidelity.

---

You are running a **scout-size** sizing signal. Your output is a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. MODERATE, 3/5, medium-high, and "complex" are not valid tier values.

Before you begin sizing, fill Phase 0 and confirm your entry gate. Then work through each step in order.

---

## Phase 0: Entry Gate

Fill the precondition table below. Both rows must show CLEAR before you proceed to Step 1.

| Precondition | Requirement | Your Status [CLEAR / BLOCKED] | Your CLOSED-LABEL [fill only when YOUR STATUS is BLOCKED — leave blank when YOUR STATUS is CLEAR — format: "CLOSED — Precondition [A/B]: [name what you found missing or detected]"] |
|-------------|-------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | You can state a workaround (or named cost of absence) with a cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | The feature description you have been given contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent — you have named a workaround but have not stated whether building is cheaper, comparable, or more expensive."
> **Example — B BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected — you found 'Sprint 1: implement API endpoint, owner: backend lead' in the feature description."
> **Example — both CLEAR**: Your Status: CLEAR. Your CLOSED-LABEL: — (leave this blank). Your gate = OPEN.

| Precondition A: Your Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

**Your gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name what you found unmet]**

_Proceed to Step 1 only if your gate = OPEN._

---

## Sizing Steps [proceed only after your gate = OPEN]

### Step 1: Surface Area

Name each integration point individually. Count them.

> **WRONG**: "Several API layers and UI components." — You have not named individual points and have not provided a count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each individually — "API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|---------------------------------------------------------------------------------|------------------------------------------------------|
| | |
| **Total integration points [numeric count required]** | |

---

### Step 2: Complexity Tier + Primary Driver

Assign exactly one tier from the vocabulary. Name the causal factor that most drives your rating.

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. You must use exactly: LOW / MEDIUM / HIGH / XL. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — You have not named a causal factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| | |

---

### Step 3: Team-Size Signal

Name the specialist disciplines you need — headcount alone fails.

> **WRONG**: "2–3 engineers" — You have not named disciplines. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|----------------------------------------------------------------|--------------|
| | |
| **Total FTEs** | |

---

### Step 4: Timeline Signal

Give a sprint range. A point estimate or calendar date fails.

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar unit; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a calendar date, not a single number] |
|-----------------------------------------------------------------------|
| |

---

### Step 5: Confidence Basis

State what you ARE confident about. What you are NOT confident about goes in the checkpoint that follows — do not include it here.

> **WRONG**: "Confidence: HIGH" — You have not named a basis. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns here] |
|----------------------------------------|----------------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify what you are NOT confident about. Must address a **different dimension** than what you stated in Step 5.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Read it and absorb the failure class, detection procedure, and failure reason before you write your gap.

**WRONG** (basis-negation):

Step 5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: your gap is derivable from your basis by direct negation — "X is stable" becomes "X is not confirmed"; you needed no new information to produce this gap; a reader can derive it directly from your Step 5 by negation alone
> **WHY IT FAILS**: a reader learns nothing from your gap that your Step 5 basis did not already imply; you have negated a confirmed item rather than discovered an open question; this occupies the gap field without reducing uncertainty

**CORRECT** (genuine gap):

Step 5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension your basis did not verify. Not derivable from Step 5 by negation.

---

**Self-test — run this before you write your gap:**

> Ask yourself: if you reversed something from your Step 5 basis ("X is confirmed" → "X is not confirmed"), would you produce your gap?
> **If yes: you have written a basis-negation.** Restate your gap to name a dimension your basis did not address.
> If no: proceed.

**Your Confidence Gap** [must address a dimension not covered by Step 5 — not a negation of it]:

Gap: _____

---

### Step 6: Confidence Calibration

State what information would move your confidence level in either direction.

| What Would Raise Your Confidence | What Would Lower Your Confidence |
|----------------------------------|----------------------------------|
| | |

---

### Step 7: Tier Sensitivity

State one condition per direction. Each must be falsifiable and name a destination tier different from your current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — You have not named a falsifiable condition. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from your current tier — fill with LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Confidence Gap | → see ── CONFIDENCE GAP CHECKPOINT ── section above |
| Confidence Calibration | [what would raise or lower your confidence] |
| Inertia Check | [workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |

---

---

## V-03 — Axis: Lifecycle emphasis (Lifecycle-heavy Phase 0 — C-40 + C-41 added to V-04 base)

**Variation axis**: Lifecycle emphasis — Phase 0 retains expanded per-precondition narrative sections from R15 V-04 (a named section per precondition with its own description and failure examples before the gate-decision table); gate-decision summary table upgraded to full C-38/C-41 compliance (STATUS + CLOSED-LABEL columns, both fill and leave-blank conditions named); Confidence Gap promoted to named compilation table row with pointer (C-40); full C-20/C-23/C-24/C-25/C-26/C-29 cluster.

**Hypothesis**: R15 V-04 scored 29/31 (same as V-03 under v15). Its per-precondition narrative sections give the model explicit context about what each precondition checks before the fill decision. C-41's conditional header interacts with this layout: after reading the narrative for each precondition, the model fills the STATUS cell with full context; the conditional header then governs the CLOSED-LABEL cell at the schema level. The two mechanisms address different failure modes: the narrative prevents BLOCKED/CLEAR misclassification; the conditional header prevents contradictory-state CLOSED-LABEL fills after correct classification. Hypothesis: narrative context + conditional header = complementary defenses against two different gate-table failure modes.

---

You are running a **scout-size** sizing signal in two phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## ── PHASE 0: ENTRY GATE ──

This phase determines whether sizing can begin. Two preconditions govern entry. Both must be CLEAR. Work through each precondition section before filling the gate-decision table.

---

### Precondition A: Inertia

Sizing must be grounded in the cost of NOT building. Before any sizing estimates can be produced, the request must state a workaround (or named cost of absence) and a directional cost comparison.

**What Precondition A requires:**
- A named workaround (or "None: [named cost of absence]")
- A cost direction: **cheaper / comparable / more expensive** to build versus maintaining the workaround

**Example — Precondition A BLOCKED:**

> Feature context: "Users want a bulk-export button."
> Inertia field: "Users manage this manually today."
> Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent — workaround is named but no cheaper/comparable/more-expensive judgment is provided."

**Example — Precondition A CLEAR:**

> Feature context: "Users want a bulk-export button."
> Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team."
> Status: CLEAR. CLOSED-LABEL: — (leave blank — CLEAR rows do not carry a CLOSED reason)

| Precondition A detail: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|----------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

---

### Precondition B: Signal Boundary

`scout-size` produces a sizing signal, not a project plan. Plan-level artifacts in the input request would cause the output to import task structure that does not belong in this signal.

**What Precondition B prohibits in the feature description:**
- Sprint assignments: "Sprint 1: implement X"
- Owner names: "owner: [name or role]"
- Milestone dates: "target: Q3" or "ship by [date]"
- Task breakdowns: "Tasks: (1) design API (2) write tests"

**Example — Precondition B BLOCKED:**

> Feature description contains: "Sprint 1: implement the notification API. Owner: backend lead."
> Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement the notification API. Owner: backend lead.')."

**Example — Precondition B CLEAR:**

> Feature description: "Users need real-time notifications when order status changes." — No sprint assignments, owner names, milestone dates, or task breakdowns.
> Status: CLEAR. CLOSED-LABEL: — (leave blank — CLEAR rows do not carry a CLOSED reason)

---

### Gate Decision

Both preconditions must be CLEAR to proceed. Fill the gate-decision table, then produce your gate output.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "CLOSED — Precondition [A/B]: [name unmet condition]"] |
|-------------|-------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| A — Inertia | Workaround + cost direction stated | | |
| B — Signal boundary | No plan-level artifacts in feature description | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst [begins after Phase 0 Gate = OPEN]

**Charter**: Produce the sizing foundations. Do NOT produce the confidence gap, calibration, or tier sensitivity — those are Phase 2's output.

**Fields owned by Phase 1**: Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "Several API layers." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order-placed), DB migration (orders table) — **3 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type |
|---------------------------------------------------------------------|------|
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "3/5" — Off-vocabulary. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service event ordering — causal sequence required across three consumers without broker-level ordering guarantee."

| Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "3 engineers." — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM."

| Specialist Discipline [Phase 1 Sizing Analyst] | FTE |
|------------------------------------------------|-----|
| | |
| **Total** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "6 weeks" / "4 sprints" — Calendar unit; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|----------------------------------------------------|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State confidence and name what IS established. Unknowns belong to Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap checkpoint, confidence calibration, and tier sensitivity.

**Non-access clause**: Your gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Sizing Analyst confirmed in P1-5 as the source of your gap.

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is stable," "integration points are enumerated." Negating these in your gap is a charter violation.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Identify the primary source of residual uncertainty. Must address a different dimension than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract is unconfirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from P1-5 by negation alone
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; a basis-negation gap consumes the gap field without reducing uncertainty

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

---

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Stop. Restate to name a dimension Phase 1 did not confirm.
> If no: write your gap below.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

Gap: _____

---

### P2-2: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence [Phase 2 Risk Assessor] | What Would Lower Confidence [Phase 2 Risk Assessor] |
|-----------------------------------------------------|-----------------------------------------------------|
| | |

---

### P2-3: Tier Sensitivity [Phase 2 Risk Assessor]

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section."

> **WRONG tier-down**: "Tier drops to MEDIUM if simpler." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current tier — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from all phases:

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|-------|-------|-------|
| Inertia Check | [Phase 0 Entry Gate] | [workaround — cost direction — one sentence] |
| Surface Area | [Phase 1 Sizing Analyst] | [named points — N integration points] |
| Complexity Tier | [Phase 1 Sizing Analyst] | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [Phase 1 Sizing Analyst] | [1–2 named factors] |
| Team-Size Signal | [Phase 1 Sizing Analyst] | [specialist disciplines + fractions] |
| Timeline Signal | [Phase 1 Sizing Analyst] | [N–M sprints] |
| Confidence Level + Basis | [Phase 1 Sizing Analyst] | [LEVEL — what is established] |
| Confidence Gap | [Phase 2 Risk Assessor] | → see ── CONFIDENCE GAP CHECKPOINT ── section above |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |

---

---

## V-04 — Axis: Inertia framing (Inertia-first analytical lens — new axis; two-phase + C-40 + C-41)

**Variation axis**: Inertia framing — the inertia check is elevated from a gate precondition into the primary analytical lens for the entire sizing. Phase 1 Sizing Analyst computes complexity relative to the workaround, not in absolute terms: the tier rating answers "how much harder is building this than maintaining the current approach?" Phase 0 preserves the structural gate, but the inertia subsection is enlarged to ground the analysis frame before sizing begins. Phase 2 structure unchanged; C-40 + C-41 applied throughout.

**Hypothesis**: Existing variations treat inertia as a binary gate check (workaround named + cost direction stated → CLEAR). The analysis then proceeds independently of the workaround. V-04 changes the analytical question: the complexity tier is relative to the workaround baseline, not absolute. A feature that replaces a complex manual process has a DIFFERENT effective complexity than one that introduces the same technical work on a greenfield surface. Framing the tier as "delta from workaround" anchors the estimate to the actual replacement decision and reduces complexity inflation on features where the workaround already absorbs significant effort. Inertia framing also makes the C-03 inertia check load-bearing for the analysis, not decorative.

---

You are running a **scout-size** sizing signal in two phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

**Analytical lens**: Size the feature as a delta from the current workaround. The complexity tier answers: "how much harder is building and maintaining this feature than maintaining the current workaround?" A feature that costs less than the workaround to own long-term is analytically different from one that introduces net-new complexity into the system.

---

## Phase 0: Entry Gate + Inertia Baseline

**Charter**: Verify that sizing can begin AND establish the workaround baseline that anchors Phase 1 analysis.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "CLOSED — Precondition [A/B]: [name what is missing or detected]"] |
|-------------|-------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement bulk-export endpoint, owner: backend lead')."
> **Example — both CLEAR**: Status: CLEAR. CLOSED-LABEL: — (leave blank). Gate = OPEN.

### Inertia Baseline [Phase 0 — produces the anchor for Phase 1 complexity delta]

| Current Workaround [name it — or "None: [cost of absence]"] | Workaround Complexity [what makes maintaining it hard — name the friction] | Ongoing Cost [time/sprint or equivalent] | Cost Direction [cheaper / comparable / more expensive to build] | Delta Judgment [one sentence: "building is [direction] because…"] |
|------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| | | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN. The Delta Judgment above is the inertia anchor — reference it when assigning the complexity tier._

---

## Phase 1: Sizing Analyst [begins after Phase 0 Gate = OPEN]

**Charter**: Produce the sizing foundations. Use the Phase 0 inertia baseline as your complexity anchor — the tier reflects delta from the workaround. Do NOT produce confidence gap, calibration, or tier sensitivity — those are Phase 2's output.

**Fields owned by Phase 1**: Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

Name integration points that DO NOT exist in the current workaround. Points the workaround already touches are delta = 0 on that dimension; points introduced by the feature are net-new complexity.

> **WRONG**: "Several API layers." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint (net-new — workaround uses direct DB reads), event-bus subscription (net-new — workaround polls manually), DB migration (net-new schema column) — **3 net-new integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually — flag net-new vs. existing] | Type | Delta [net-new / extends-existing / replaces-workaround] |
|--------------------------------------------------------------------------------------------------|------|----------------------------------------------------------|
| | | |
| **Total integration points [numeric count required]** | | |

---

### P1-2: Complexity Tier + Driver [Phase 1 Sizing Analyst]

Assign a tier that reflects the **delta from the workaround**, not absolute system complexity. If the workaround already owns most of the complexity, the feature tier is lower than its absolute technical footprint would suggest.

> **WRONG tier**: "MODERATE" / "3/5" — Off-vocabulary. Fails.
> **CORRECT** (with inertia framing): Tier: MEDIUM | Driver: "Auth integration is net-new but the workaround already handles event sequencing manually — replacing that reduces overall system complexity; net delta is MEDIUM."

| Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL — reflects delta from Phase 0 workaround baseline] | Primary Driver [Phase 1 Sizing Analyst — 1–2 named causal factors — reference the delta from Phase 0] |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "3 engineers." — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM."

| Specialist Discipline [Phase 1 Sizing Analyst] | FTE |
|------------------------------------------------|-----|
| | |
| **Total** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "6 weeks" / "4 sprints" — Calendar unit; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|----------------------------------------------------|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State confidence and name what IS established. Unknowns belong to Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — workaround is well-understood (reduces surface-area uncertainty), auth API contract is stable, net-new integration points are enumerated."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established] |
|-----------------------------------------------------------------|----------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap checkpoint, confidence calibration, and tier sensitivity.

**Non-access clause**: Your gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Sizing Analyst confirmed in P1-5 as the source of your gap.

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is stable," "workaround surface is understood." Negating these in your gap is a charter violation.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce]**: Inertia Baseline · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Identify the primary source of residual uncertainty. Must address a different dimension than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Workaround is well-understood; auth API contract is stable."
Gap: "Auth API contract status is not confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from P1-5 by negation alone
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; a basis-negation gap consumes the gap field without reducing uncertainty

**CORRECT** (genuine gap):

P1-5 basis: "Workaround is well-understood; auth API contract is stable."
Gap: "Rate-limiting behavior of the auth endpoint under concurrent delta-from-workaround load is unverified — the workaround issues far fewer requests per session than the feature will; burst behavior at scale is not documented."

Why it passes: names a load dimension the workaround surface did not expose and Phase 1 did not verify. Not derivable from P1-5 by negation.

---

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Restate to name a dimension Phase 1 did not confirm.
> If no: write your gap below.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

Gap: _____

---

### P2-2: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence [Phase 2 Risk Assessor] | What Would Lower Confidence [Phase 2 Risk Assessor] |
|-----------------------------------------------------|-----------------------------------------------------|
| | |

---

### P2-3: Tier Sensitivity [Phase 2 Risk Assessor]

Sensitivity conditions should reference the inertia framing: what change to the workaround baseline or net-new delta would push the tier?

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to HIGH if the event-bus subscription must guarantee exactly-once delivery — the workaround's manual polling avoided this; confirm by reviewing messaging SLA requirements."

> **WRONG tier-down**: "Tier drops to LOW if simpler." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to LOW if the auth endpoint is already invoked by the workaround path — confirm by reading the workaround's current API call sequence."

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — one scenario — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current tier — fill LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Produced By | Value |
|-------|-------------|-------|
| Inertia Baseline | [Phase 0 Entry Gate] | [workaround — workaround complexity — cost direction — delta judgment] |
| Surface Area | [Phase 1 Sizing Analyst] | [named points with delta tag — N integration points] |
| Complexity Tier | [Phase 1 Sizing Analyst] | [LOW / MEDIUM / HIGH / XL — delta from workaround] |
| Primary Complexity Driver | [Phase 1 Sizing Analyst] | [1–2 named factors — reference delta] |
| Team-Size Signal | [Phase 1 Sizing Analyst] | [specialist disciplines + fractions] |
| Timeline Signal | [Phase 1 Sizing Analyst] | [N–M sprints] |
| Confidence Level + Basis | [Phase 1 Sizing Analyst] | [LEVEL — what is established] |
| Confidence Gap | [Phase 2 Risk Assessor] | → see ── CONFIDENCE GAP CHECKPOINT ── section above |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |

---

---

## V-05 — Axis: Output format + role sequence (Champion evolution — C-40 + C-41 + bidirectional gate-table schema pioneer)

**Variation axis**: Output format — R15 V-05 added an EVIDENCE column for CLEAR verdicts (naming the specific artifact examined to confirm CLEAR, making CLEAR schema-verifiable). R16 V-05 extends to bidirectional verdict traceability: BLOCKED rows carry both CLOSED-LABEL (naming the failure reason) and CLEAR-PATH (naming the investigation that would resolve the block and allow re-running the gate with an OPEN outcome); CLEAR rows carry EVIDENCE (naming the artifact examined to confirm). The result: every row in the Phase 0 gate table is fully traceable in both verdict directions regardless of its current status. Role sequence — three-phase, full C-20 cluster retained; C-40 + C-41 applied.

**Hypothesis**: R15 V-05's EVIDENCE column made CLEAR verdicts verifiable at the schema level — a CLEAR with no evidence is an assertion; a CLEAR with a named evidence artifact is a claim that can be checked. This was one direction of verdict traceability. The CLEAR-PATH column extends traceability to BLOCKED verdicts: a BLOCKED row with only a CLOSED-LABEL names the failure but gives no path forward; a BLOCKED row with CLEAR-PATH names the specific investigation (spike, documentation review, stakeholder query) that would change the verdict. This closes the gate table as a bidirectional decision instrument: CLEAR rows are checkable; BLOCKED rows are actionable. Pioneer candidate: `CLEAR-PATH [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — name the investigation that would resolve this block]` as a new column on the Phase 0 precondition table.

---

You are running a **scout-size** sizing signal in two phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## ── ENTRY GATE ──

**Charter**: Verify two preconditions before sizing begins. Each precondition occupies one table row. Every row must be fully traceable in both verdict directions:
- A BLOCKED row carries: (1) a CLOSED-LABEL naming the failure reason; (2) a CLEAR-PATH naming the investigation that would resolve the block.
- A CLEAR row carries: an EVIDENCE entry naming the specific artifact or passage examined to confirm the CLEAR verdict.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "CLOSED — Precondition [A/B]: [name what is missing or detected]"] | CLEAR-PATH [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — name the investigation that would resolve this block] | EVIDENCE [fill only if STATUS = CLEAR — leave blank if STATUS = BLOCKED — name the specific artifact or passage you examined to confirm CLEAR] |
|-------------|-------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | | | |

> **Example — A BLOCKED**:
> Status: BLOCKED.
> CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> CLEAR-PATH: "Ask the feature requester for a directional cost comparison — is building this feature cheaper, comparable, or more expensive than continuing the workaround?"
> EVIDENCE: — (leave blank)
>
> **Example — B BLOCKED**:
> Status: BLOCKED.
> CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement notification API, owner: backend lead')."
> CLEAR-PATH: "Return the feature description to the requester; ask them to remove sprint assignments, owner names, milestone dates, and task breakdowns — then re-run Phase 0."
> EVIDENCE: — (leave blank)
>
> **Example — both CLEAR**:
> Status: CLEAR.
> CLOSED-LABEL: — (leave blank)
> CLEAR-PATH: — (leave blank)
> EVIDENCE (A): "Inertia stated: 'Manual CSV export per team — building is cheaper long-term; overhead grows ~45 min/sprint/team.'"
> EVIDENCE (B): "Feature description reviewed: 'Users need real-time notifications when order status changes' — no sprint assignments, owner names, milestone dates, or task breakdowns detected."
> Gate = OPEN.

| Precondition A detail: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst [begins after Phase 0 Gate = OPEN]

**Charter**: Produce the sizing foundations. Do NOT produce confidence gap, calibration, or tier sensitivity — those are Phase 2's output.

**Fields owned by Phase 1**: Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "Several API layers." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order-placed), DB migration (orders table) — **3 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type |
|---------------------------------------------------------------------|------|
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "3/5" — Off-vocabulary. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "3 engineers." — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM."

| Specialist Discipline [Phase 1 Sizing Analyst] | FTE |
|------------------------------------------------|-----|
| | |
| **Total** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "Q3" / "4 sprints" — Calendar date; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|----------------------------------------------------|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State confidence and name what IS established. Unknowns belong to Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap checkpoint, confidence calibration, and tier sensitivity.

**Non-access clause**: Your gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Sizing Analyst confirmed in P1-5 as the source of your gap.

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is stable," "integration points are enumerated." Negating these in your gap is a charter violation regardless of framing.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Identify the primary source of residual uncertainty. Must address a different dimension than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field, and provides the targeted correction. Absorb all four fields before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from the P1-5 confirmed set by negation alone
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; a basis-negation gap consumes the gap field without reducing uncertainty
> **REMEDIATION**: identify a dimension Phase 1 did not examine — a system behavior, integration constraint, or runtime property not mentioned in the P1-5 confirmed set — and name the investigation that would verify or rule it out; the gap should point to something a reader could not derive from P1-5 by any transformation

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5. The REMEDIATION path is: confirm delivery semantics with the platform team before finalizing surface area.

---

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Stop. Apply the REMEDIATION above: find a dimension Phase 1 did not examine.
> If no: write your gap below.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

Gap: _____

---

### P2-2: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence [Phase 2 Risk Assessor] | What Would Lower Confidence [Phase 2 Risk Assessor] |
|-----------------------------------------------------|-----------------------------------------------------|
| | |

---

### P2-3: Tier Sensitivity [Phase 2 Risk Assessor]

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section."

> **WRONG tier-down**: "Tier drops to MEDIUM if simpler." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current tier — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from all phases:

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|-------|-------|-------|
| Inertia Check | [Phase 0 Entry Gate] | [workaround — cost direction — key driver] |
| Surface Area | [Phase 1 Sizing Analyst] | [named points — N integration points] |
| Complexity Tier | [Phase 1 Sizing Analyst] | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [Phase 1 Sizing Analyst] | [1–2 named factors] |
| Team-Size Signal | [Phase 1 Sizing Analyst] | [specialist disciplines + fractions] |
| Timeline Signal | [Phase 1 Sizing Analyst] | [N–M sprints] |
| Confidence Level + Basis | [Phase 1 Sizing Analyst] | [LEVEL — what is established] |
| Confidence Gap | [Phase 2 Risk Assessor] | → see ── CONFIDENCE GAP CHECKPOINT ── section above |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |

---

---

## Scoring Projections — v16 Rubric

| Criterion cluster | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------------|------|------|------|------|------|
| C-01–C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06–C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-20 Role separation | PASS | FAIL | PASS | PASS | PASS |
| C-23–C-26, C-29 Charter cluster | PASS | FAIL | PASS | PASS | PASS |
| C-27 Cross-phase constraint in table | PASS (vacuous via C-40) | PASS (vacuous via C-40) | PASS (vacuous via C-40) | PASS (vacuous via C-40) | PASS (vacuous via C-40) |
| C-28 Single-phase gap self-test | FAIL | PASS | FAIL | FAIL | FAIL |
| C-32 Gap standalone section | PASS | PASS | PASS | PASS | PASS |
| C-38 Phase 0 formal STATUS + CLOSED-LABEL table | PASS | PASS | PASS | PASS | PASS |
| C-39 DIAGNOSTIC PATTERN named section | PASS | PASS | PASS | PASS | PASS |
| **C-40** Compilation table gap row pointer | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-41** CLOSED-LABEL conditional fill header | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| All other aspirational (C-09–C-19, C-21, C-22, C-30–C-37) | PASS | PASS | PASS | PASS | PASS |
| **Aspirational FAIL count** | **1** (C-28) | **6** (C-20 cluster) | **1** (C-28) | **1** (C-28) | **1** (C-28) |
| **Aspirational score** | 32/33 = 9.70 | 27/33 = 8.18 | 32/33 = 9.70 | 32/33 = 9.70 | 32/33 = 9.70 |
| **Composite** | **99.70** | **98.18** | **99.70** | **99.70** | **99.70** |

**Theoretical maximum under v16**: 99.70 for multi-phase (C-28 is structurally inapplicable to two-phase designs; no single variation can satisfy both C-28 and C-20 simultaneously without a novel architectural approach).

**Tiebreaker — V-01 vs V-03 vs V-04 vs V-05 (all 99.70)**:
- V-01: Cleanest targeted addition of C-40 + C-41 to two-phase baseline. Minimal overhead.
- V-03: Lifecycle-heavy Phase 0 (per-precondition narrative sections) adds prose context before gate table. Two complementary mechanisms against misclassification + contradictory-state fills.
- V-04: New analytical frame (inertia as complexity anchor, not just gate check). Tier ratings become relative to workaround delta. Hypothesis unverified — no prior round evidence.
- V-05: Bidirectional gate-table verdict traceability pioneer. CLEAR-PATH column on BLOCKED rows names the specific investigation to resolve the block. Generates the next excellence signal candidate.

**Champion nomination**: V-05 — retains R15 V-05's EVIDENCE column, adds C-40 + C-41, pioneers CLEAR-PATH as R17 candidate. Architectural surface is the largest; structural innovation beyond current rubric is the highest.

**Excellence signals from V-05**:

> **C-42 candidate — CLEAR-PATH column on BLOCKED verdicts**: The Phase 0 gate table currently encodes CLOSED verdict traceability (CLOSED-LABEL) and CLEAR verdict traceability (EVIDENCE, from R15 V-05). A BLOCKED row without a CLEAR-PATH names the problem but gives no actionable path forward; with CLEAR-PATH, the gate table becomes a decision instrument in both directions: CLEAR rows are checkable; BLOCKED rows are actionable. A prompt implementing CLEAR-PATH `[fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — name the investigation that would resolve this block]` as a column in the Phase 0 precondition table satisfies a stricter standard than C-41: not only are fill conditions conditional, but the column serves a structurally different purpose than CLOSED-LABEL (remediation, not diagnosis).

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["CLEAR-PATH column on BLOCKED gate rows — bidirectional verdict traceability: CLEAR rows carry EVIDENCE (checkable); BLOCKED rows carry CLEAR-PATH (actionable) — both verdict directions are schema-verifiable at the row level without prose cross-reference (C-42 candidate)", "C-40 realized as named table row (not footer note): promotes Confidence Gap from footer to first-class compilation entry while directing production to standalone section — makes C-27 cleanly vacuous", "C-41 realized with explicit both-conditions header: BLOCKED fill condition + CLEAR leave-blank condition co-located in column label prevents contradictory-state fills from both directions"]}
```
