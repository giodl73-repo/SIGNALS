# Scout-Size Prompt Variations — R15

**Skill**: scout-size
**Rubric**: v15 (31 aspirational criteria, C-01 through C-39)
**Date**: 2026-03-17
**Round**: 15
**R14 champion**: V-05 — three-phase; Phase 0 as formal two-row precondition table with STATUS and CLOSED-LABEL columns (C-38); `── DIAGNOSTIC PATTERN ──` named sub-section wrapping the three-field WRONG block (C-39); C-32 gap standalone section; C-30 defense cluster
**R14 gaps**: C-38 FAIL in V-01/V-02/V-03/V-04 (Phase 0 gate uses prose or prose/table hybrid for C-36; per-precondition STATUS and CLOSED-LABEL are not co-located schema columns); C-39 FAIL in V-01/V-02/V-03/V-04 (three-field DIAGNOSTIC block embedded in CHECKPOINT or WRONG section without a named diagnostic container)

---

## Context: What R15 Addresses

v15 adds two new aspirational criteria formalized from R14 excellence signals:

| New criterion | What it formalizes | R14 evidence |
|---------------|-------------------|--------------|
| C-38 | Phase 0 gate encoded as a formal precondition table with STATUS and CLOSED-LABEL columns per precondition row | R14 V-05 Phase 0 uses a two-row precondition table with columns: Precondition / Requirement / Status [CLEAR/BLOCKED] / CLOSED Label [fill if BLOCKED] — the CLOSED reason is readable from the row without parsing prose |
| C-39 | Three-field diagnostic block enclosed in a named section header that labels its architectural role as a diagnostic pattern | R14 V-05 wraps the three-field WRONG block in `### ── DIAGNOSTIC PATTERN ──` sub-section with introductory framing; V-01 through V-04 embed the block in a CHECKPOINT or WRONG blockquote section without a named diagnostic container |

R14 V-05 already satisfies both C-38 and C-39. The rubric formalizes what V-05 demonstrated. R15 variations explore:

1. Whether C-38 + C-39 can be achieved in the minimal single-phase architecture (no role separation)
2. Whether the second-person register absorbs C-38 + C-39 with structural reinforcement in phrasing
3. Whether C-38 + C-39 integrate cleanly into the two-phase role-separation architecture
4. Whether the lifecycle-heavy Phase 0 from R14 V-04 is compatible with C-38's table schema
5. What structural patterns beyond C-38 + C-39 the champion variation can push toward

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing (Phase 0 formal two-row STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` named section for C-39; single-phase; no role separation) | R14 V-01 achieved C-36 + C-37 in the minimal single-phase design. R15 V-01 makes exactly two structural changes: (a) Phase 0 prose gate → formal two-row precondition table with STATUS and CLOSED-LABEL columns (C-38); (b) WRONG block in gap checkpoint → wrapped in `── DIAGNOSTIC PATTERN ──` named sub-section (C-39). Hypothesis: C-38 + C-39 can be achieved in the minimal single-phase architecture without role-separation overhead. |
| V-02 | Phrasing register (Second-person throughout; Phase 0 formal STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` named section for C-39; single-phase) | R14 V-02 applied second-person framing to C-36 + C-37 without structural interference. R15 V-02 extends to C-38 + C-39. The second-person register has a structural implication for the C-39 diagnostic section: DETECTION PATTERN and WHY IT FAILS can be phrased as observer-stance diagnoses directed at the model ("your gap is derivable…" / "you have consumed the gap field…"). Hypothesis: second-person phrasing and C-38 + C-39 structural encoding reinforce each other — the named diagnostic section and the second-person observer stance together position the model as a diagnostician, not just a producer. |
| V-03 | Role sequence (Two-phase; Phase 0 formal STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` in Phase 2 gap checkpoint for C-39; full C-20 cluster) | R14 V-03 achieved C-36 + C-37 with targeted additions to the two-phase architecture. R15 V-03 makes two further targeted changes: (a) Phase 0 prose gate → formal STATUS/CLOSED-LABEL table (C-38); (b) Phase 2 WRONG block → wrapped in `── DIAGNOSTIC PATTERN ──` (C-39). Hypothesis: C-38 + C-39 are straightforward additions to the two-phase architecture; the targeted structural changes preserve the full C-20 cluster while achieving both new criteria. |
| V-04 | Lifecycle emphasis (Three-phase; Phase 0 retains expanded per-precondition narrative sections; gate-decision summary table upgraded to STATUS/CLOSED-LABEL schema for C-38; `── DIAGNOSTIC PATTERN ──` in Phase 2 for C-39) | R14 V-04's gate-decision summary table used PRECONDITION / REQUIREMENT / RESULT columns — satisfying C-35 and C-36 but not C-38 because RESULT is a single merged column, not a STATUS + CLOSED-LABEL split with the failure reason co-located at the row level. R15 V-04 upgrades the gate-decision table to C-38 compliance by splitting RESULT into STATUS [CLEAR/BLOCKED] and CLOSED-LABEL columns. Hypothesis: the lifecycle-heavy Phase 0 treatment is compatible with C-38's table schema; upgrading the summary table columns achieves C-38 without removing the lifecycle footprint. |
| V-05 | Output format + role sequence (Three-phase; Phase 0 wrapped in `── ENTRY GATE ──` visual delimiter; gate table extended with EVIDENCE column beyond C-38 minimum for C-40 candidate; four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION field for C-41 candidate) | R14 V-05 achieves C-38 and C-39 at their minimum requirements. R15 V-05 pushes two structural patterns beyond the rubric's current criteria: (a) Phase 0 gate table extended with an EVIDENCE column for Precondition B — naming the specific artifact examined when producing a CLEAR verdict, making CLEAR verifiable at the schema level, not only CLOSED; (b) `── DIAGNOSTIC PATTERN ──` block extended with a REMEDIATION field as a fourth entry, closing the diagnostic loop from class → detection → cause → correction. Additionally wraps Phase 0 in `── ENTRY GATE ──` visual delimiter, applying the same structural signaling as `── CONFIDENCE GAP CHECKPOINT ──` to the gate phase. These patterns are candidates for C-40 and C-41. |

---

## V-01 — Axis: Inertia framing (Single-phase; Phase 0 formal STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` section for C-39; no role separation)

**Variation axis**: Inertia framing — Phase 0 is encoded as a formal two-row precondition table with STATUS and CLOSED-LABEL columns, achieving C-38 by making each precondition's failure reason readable from the row itself. The `── DIAGNOSTIC PATTERN ──` named sub-section wraps the three-field WRONG block in the gap checkpoint, achieving C-39. Single-phase analysis throughout; no role separation.

**Hypothesis**: R14 V-01 achieved C-36 and C-37 in the minimal single-phase design — two-precondition Phase 0 in prose/table hybrid, three-field WRONG block in blockquote form inside the gap section. The two remaining gaps were: (a) Phase 0 STATUS and CLOSED-LABEL were not co-located schema columns; (b) the three-field block had no named diagnostic container. R15 V-01 adds exactly those two structural changes and no others. Hypothesis: C-38 + C-39 can be achieved in the minimal single-phase architecture without role-separation overhead.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before any analysis begins. Proceed through each step in order.

---

## Phase 0: Entry Gate

Fill the precondition table below. Both rows must be CLEAR before Step 1 begins.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if BLOCKED — format: "CLOSED — Precondition [A/B]: [name what is missing or detected]"] |
|-------------|-------------|--------------------------|------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')."
> **Example — both CLEAR**: Gate = OPEN.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Step 1 begins only if Gate = OPEN._

---

## Sizing Steps [Gate must be OPEN before proceeding]

### Step 1: Surface Area

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each individually — "API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|---------------------------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total integration points [numeric count required]** | |

---

### Step 2: Complexity Tier + Primary Driver

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| | |

---

### Step 3: Team-Size Signal

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|----------------------------------------------------------------|--------------|
| | |
| | |
| **Total FTEs** | |

---

### Step 4: Timeline Signal

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a calendar date, not a single number] |
|-----------------------------------------------------------------------|
| |

---

### Step 5: Confidence Basis

State only what IS established here. What is NOT known gets its own section next.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|----------------------------------------|-----------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Must address a **different dimension** than the Step 5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation):

Step 5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required to produce this gap; a reader can derive it from Step 5 by negation alone
> **WHY IT FAILS**: a reader learns nothing from this gap that the Step 5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty

**CORRECT** (genuine gap):

Step 5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension the basis did not verify. Not derivable from Step 5 by negation.

---

**Self-test — run before writing your gap:**

> Ask: if I reversed something from my Step 5 basis ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation.** Restate to name a dimension the basis did not address.
> If no: proceed.

**Your Confidence Gap** [must address a dimension not covered by Step 5 — not a negation of it]:

Gap: _____

---

### Step 6: Confidence Calibration

| What Would Raise Confidence | What Would Lower Confidence |
|-----------------------------|-----------------------------|
| | |

---

### Step 7: Tier Sensitivity

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from current tier — fill with LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
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
| Inertia Check | [workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

_Confidence Gap: See ── CONFIDENCE GAP CHECKPOINT ── section above._

---

---

## V-02 — Axis: Phrasing register (Second-person throughout; Phase 0 formal STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` named section for C-39; single-phase)

**Variation axis**: Phrasing register — all instructions and constraint language addressed in second person ("you have reviewed," "your gate," "you have written a basis-negation"); Phase 0 formal two-row STATUS/CLOSED-LABEL table (C-38); `── DIAGNOSTIC PATTERN ──` named sub-section wrapping the three-field WRONG block (C-39); single-phase with no role separation.

**Hypothesis**: R14 V-02 extended the second-person register to C-36 + C-37 without structural interference. R15 V-02 extends further to C-38 + C-39. The second-person framing has a structural implication for the C-39 diagnostic section: DETECTION PATTERN and WHY IT FAILS can be phrased as observer-stance diagnoses directed at the model — "your gap is derivable from your basis by direct negation" rather than "the gap is derivable from the basis by direct negation." Hypothesis: second-person phrasing and the named diagnostic section create a reinforcing diagnostic-observer stance: the section header labels the block's architectural role at the document level, and the second-person DETECTION PATTERN makes the detection procedure personal and immediate.

---

You are running a **scout-size** sizing signal. Your output is a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. MODERATE, 3/5, medium-high, and "complex" are not valid tier values.

Before you begin sizing, fill Phase 0 and close your entry gate. Then work through each step in order.

---

## Phase 0: Entry Gate

Fill the precondition table below. Both rows must show CLEAR before you proceed to Step 1.

| Precondition | Requirement | Your Status [CLEAR / BLOCKED] | Your CLOSED-LABEL [fill only if BLOCKED — format: "CLOSED — Precondition [A/B]: [name what you found missing or detected]"] |
|-------------|-------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | You can state a workaround (or named cost of absence) with a cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | The feature description you have been given contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent — you have named a workaround but have not stated whether building is cheaper, comparable, or more expensive."
> **Example — B BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected — you found 'Sprint 1: implement API endpoint, owner: backend lead' in the feature description."
> **Example — both CLEAR**: Your gate = OPEN.

| Precondition A: Your Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost [friction you observe today] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------------|--------------------------|
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
| | |
| **Total integration points [numeric count required]** | |

---

### Step 2: Complexity Tier + Primary Driver

Assign exactly one tier. Name the causal factor that most drives your rating.

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

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|----------------------------------------|-----------------------------------------------------------------------|
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
| Inertia Check | [workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower your confidence] |

_Your Confidence Gap: See ── CONFIDENCE GAP CHECKPOINT ── section above._

---

---

## V-03 — Axis: Role sequence (Two-phase; Phase 0 formal STATUS/CLOSED-LABEL table for C-38; `── DIAGNOSTIC PATTERN ──` in Phase 2 for C-39; full C-20 cluster)

**Variation axis**: Role sequence — two-phase role separation (Phase 1: Sizing Analyst, Phase 2: Risk Assessor) retains the full C-20/C-23/C-24/C-25/C-26/C-27/C-29 cluster from R14 V-03; Phase 0 upgraded from prose/table hybrid to formal two-row STATUS/CLOSED-LABEL table (C-38); Phase 2 gap checkpoint three-field WRONG block wrapped in `── DIAGNOSTIC PATTERN ──` named sub-section (C-39).

**Hypothesis**: R14 V-03 achieved C-36 + C-37 with targeted additions to the two-phase architecture — Precondition B added to Phase 0; WRONG block promoted to three-field format in Phase 2. The two remaining gaps were: (a) Phase 0 STATUS and CLOSED-LABEL not co-located as schema columns; (b) three-field block without named diagnostic container. R15 V-03 makes exactly two targeted changes: (a) Phase 0 table upgraded to STATUS + CLOSED-LABEL columns; (b) Phase 2 WRONG block wrapped in `── DIAGNOSTIC PATTERN ──`. Hypothesis: C-38 + C-39 are straightforward structural additions to the two-phase architecture; the targeted changes preserve the full C-20 cluster while achieving both new criteria.

---

You are running a **scout-size** sizing signal in three stages. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Stage sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 is OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## Phase 0: Entry Gate

**Charter**: Verify that sizing can begin. Fill the precondition table. Both rows must be CLEAR before Phase 1 is permitted.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if BLOCKED — format: "CLOSED — Precondition [A/B]: [name unmet condition]"] |
|-------------|-------------|--------------------------|------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround stated but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')."
> **Example — both CLEAR**: Gate = OPEN.

| Precondition A detail: Workaround [Phase 0 — name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver |
|---------------------------------------------------------------------------------------|--------------|--------------------------------------------------------|------------|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

---

## Phase 1: Sizing Analyst [begins after Phase 0 gate = OPEN]

**Charter**: Produce the sizing foundations — surface area, complexity tier, team-size signal, timeline signal, and confidence basis. Do NOT produce the confidence gap, confidence calibration, or tier sensitivity; those are reserved for Phase 2.

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

**Non-access clause**: Your confidence gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Phase 1 Sizing Analyst confirmed in P1-5 as the source of your gap.

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

**Your Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

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

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from all stages:

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
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |

_Confidence Gap [Phase 2 Risk Assessor]: See ── CONFIDENCE GAP CHECKPOINT ── section above._

---

---

## V-04 — Axis: Lifecycle emphasis (Three-phase; Phase 0 expanded per-precondition sections retained; gate-decision table upgraded to STATUS/CLOSED-LABEL schema for C-38; `── DIAGNOSTIC PATTERN ──` in Phase 2 for C-39)

**Variation axis**: Lifecycle emphasis — Phase 0 retains expanded per-precondition narrative sections from R14 V-04 (a named section per precondition, each with its own description and failure example); the gate-decision summary table at the end of Phase 0 is upgraded from PRECONDITION / REQUIREMENT / RESULT columns to the C-38-compliant STATUS / CLOSED-LABEL split; `── DIAGNOSTIC PATTERN ──` named sub-section wraps the three-field WRONG block in Phase 2 (C-39). Three-phase architecture throughout.

**Hypothesis**: R14 V-04's gate-decision summary table used a merged RESULT column (MET/UNMET or CLEAR/BLOCKED), which satisfied C-35 and C-36 but not C-38 because the CLOSED reason was produced separately in the gate output prose rather than co-located as a column in the same row as the precondition. R15 V-04 upgrades the summary table by splitting RESULT into STATUS [CLEAR/BLOCKED] and CLOSED-LABEL columns — the minimum schema required by C-38. The expanded per-precondition sections are retained for lifecycle emphasis. Hypothesis: the lifecycle-heavy Phase 0 treatment is compatible with C-38's table schema; the per-precondition sections provide context, and the upgraded summary table provides structure.

---

You are running a **scout-size** sizing signal in three phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 is OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## ── PHASE 0: ENTRY GATE ──

This phase determines whether sizing can begin. Two preconditions govern entry. Both must be CLEAR. Work through each before filling the gate-decision table.

---

### Precondition A: Inertia

Sizing must be grounded in the cost of NOT building. Before any sizing estimates can be produced, state a workaround (or named cost of absence) and a directional cost comparison.

**What Precondition A requires:**
- A named workaround (or "None: [named cost of absence]")
- A cost direction: **cheaper / comparable / more expensive**

**Example — Precondition A fails (A BLOCKED):**

> Feature context: "Users would like a bulk-export button."
> Inertia field: "Users manage this manually."
> Result: CLOSED — Precondition A: cost direction absent. Sizing halted.

**Example — Precondition A passes (A CLEAR):**

> Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team." Cost direction present; key driver named.

| Precondition A: Workaround [Phase 0 — name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|--------------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

---

### Precondition B: Signal Boundary

`scout-size` analyzes a feature description — not a project plan. If the input contains plan-level artifacts, the gate closes before sizing begins, because the input has already bypassed the signal boundary this skill enforces.

**Plan-level artifacts that trigger BLOCKED:**
- Sprint assignments: "Sprint 1: implement X"
- Owner names: "owner: [name or role]"
- Milestone dates: "target: Q3" or "ship by [date]"
- Task breakdowns: "Tasks: (1) design API (2) write tests"

**Example — Precondition B fails (B BLOCKED):**

> Feature description contains: "Sprint 1: implement the notification API. Owner: backend lead. Sprint 2: build UI."
> Result: CLOSED — Precondition B: plan-level artifact detected ("Sprint 1: implement the notification API. Owner: backend lead.").

**Example — Precondition B passes (B CLEAR):**

> Feature description: "Users need real-time notifications when order status changes." — No sprint assignments, owner names, milestone dates, or task breakdowns.

| Precondition B: Signal Boundary Review | Status |
|----------------------------------------|--------|
| Feature description reviewed for plan-level artifacts (sprint assignments, owner names, milestone dates, task breakdowns) | CLEAR / BLOCKED — [name artifact if BLOCKED] |

---

### Gate Decision

Both preconditions must be CLEAR to proceed. Fill the gate-decision table, then produce your gate output.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill if BLOCKED — "CLOSED — Precondition [A/B]: [name unmet condition]"] |
|-------------|-------------|--------------------------|----------------------------------------------------------------------------------------|
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

> **WRONG**: "Confidence: HIGH" — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap, confidence calibration, and tier sensitivity.

**Non-access clause**: Your gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Phase 1 Sizing Analyst confirmed in P1-5.

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is stable," "integration points are enumerated." Negating these in your gap is a charter violation.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Must address a different dimension than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract is unconfirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from P1-5 by negation alone
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; this is the violation the non-access clause prohibits

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

---

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Stop. Restate to name a dimension Phase 1 did not confirm.
> If no: write your gap below.

**Your Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

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

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

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
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |

_Confidence Gap [Phase 2 Risk Assessor]: See ── CONFIDENCE GAP CHECKPOINT ── section above._

---

---

## V-05 — Axis: Output format + role sequence (Three-phase; Phase 0 with `── ENTRY GATE ──` delimiter and EVIDENCE column beyond C-38 minimum; four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION for C-41 candidate; C-40/C-41 push)

**Variation axis**: Output format — Phase 0 is enclosed in an `── ENTRY GATE ──` visual delimiter header, applying the same structural signaling used for `── CONFIDENCE GAP CHECKPOINT ──` to the gate phase itself; the Phase 0 gate table extends beyond C-38 minimum by adding an EVIDENCE column for Precondition B — naming the specific artifact examined when producing a CLEAR verdict, making CLEAR verifiable at the schema level and not only CLOSED. The `── DIAGNOSTIC PATTERN ──` block extends beyond C-39 minimum by adding a REMEDIATION field as a fourth labeled entry, closing the diagnostic loop: class → detection → cause → correction. Role sequence — three-phase with full C-20 cluster retained.

**Hypothesis**: R14 V-05 achieves C-38 at minimum (STATUS + CLOSED-LABEL columns) and C-39 at minimum (named `── DIAGNOSTIC PATTERN ──` sub-section). The EVIDENCE column applies the C-38 structural-encoding principle to the CLEAR verdict — a CLEAR determination without named evidence is an assertion; a CLEAR determination with a named evidence item is a schema-level verifiable claim. The REMEDIATION field closes the diagnostic loop that C-39's three-field block opens: a model absorbing FAILURE CLASS + DETECTION PATTERN + WHY IT FAILS has everything needed to recognize a failure; REMEDIATION gives it the specific correction procedure targeting that failure class, so no derivation from the self-test query is required. These patterns are candidates for C-40 (EVIDENCE column extends CLEAR verifiability to schema level) and C-41 (REMEDIATION closes the diagnostic loop within the named section).

---

You are running a **scout-size** sizing signal in three phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## ── ENTRY GATE ──

**Charter**: Verify two preconditions before sizing begins. Each precondition occupies one table row. A blocked row requires a CLOSED-LABEL naming the precondition and what was unmet. A clear row requires an EVIDENCE entry naming the specific artifact examined to confirm the CLEAR verdict.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill if BLOCKED — "CLOSED — Precondition [A/B]: [name what is missing or detected]"] | EVIDENCE [fill if CLEAR — name the specific artifact or passage you examined to confirm this verdict] |
|-------------|-------------|--------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)." EVIDENCE: —
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement notification API, owner: backend lead')." EVIDENCE: —
> **Example — both CLEAR**: Status: CLEAR. EVIDENCE (A): "Inertia stated: 'Manual CSV export per team — building is cheaper long-term; overhead grows ~45 min/sprint/team.'" EVIDENCE (B): "Feature description reviewed: 'Users need real-time notifications when order status changes' — no sprint assignments, owner names, milestone dates, or task breakdowns detected." Gate = OPEN.

| Precondition A detail: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst [begins after Phase 0 Gate = OPEN]

**Charter**: Produce sizing foundations. Do NOT produce confidence gap, calibration, or tier sensitivity — those are Phase 2's output.

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

> **WRONG**: "Confidence: HIGH" — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess residual risk not covered by Phase 1. Produce the confidence gap, confidence calibration, and tier sensitivity.

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

The following pattern names and diagnoses the most common failure for this field, and provides the targeted correction. Absorb all four fields before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract is unconfirmed."

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

**Your Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-5 confirmed set — not derivable by negating P1-5]**:

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

Compile the final signal from all three phases:

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
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |

_Confidence Gap [Phase 2 Risk Assessor]: See ── CONFIDENCE GAP CHECKPOINT ── section above._
