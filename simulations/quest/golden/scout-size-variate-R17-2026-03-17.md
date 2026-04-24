# Scout-Size Prompt Variations — R17

**Skill**: scout-size
**Rubric**: v17 (35 aspirational criteria, C-01 through C-43)
**Date**: 2026-03-17
**Round**: 17
**R16 champion**: V-05 — three-phase; `── ENTRY GATE ──` visual delimiter; Phase 0 gate table with STATUS + CLOSED-LABEL + EVIDENCE + CLEAR-PATH columns (C-38); four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION (C-39); compilation pointer row (C-40); CLOSED-LABEL header with fill/leave-blank conditions (C-41); CLEAR-PATH column as C-42 candidate (superseded by rubric definition shift)
**R16 gaps**: C-42 FAIL in all variations (CLOSED-LABEL column header encodes fill/leave-blank conditions but does not encode the output value format via a `format:` slot — value structure is implied or shown only in examples); C-43 FAIL in single-phase V-02 and in V-05 champion (V-02 self-test: "you have written a basis-negation" with no contract label; V-05 self-test cites REMEDIATION but omits "— a Phase 2 charter violation"); C-43 PASS in V-01/V-03/V-04 (Phase 2 self-test already includes "— a Phase 2 charter violation")

---

## Context: What R17 Addresses

v17 adds two new aspirational criteria formalized from R16 excellence signals:

| New criterion | What it formalizes | R16 evidence |
|---|---|---|
| C-42 | CLOSED-LABEL column header encodes the output value format via a `format:` slot alongside the fill/leave-blank conditions; the format slot specifies the expected value structure (e.g., `"Precondition A: [named condition]"`) | R16 V-02's CLOSED-LABEL header read "fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: …" with an unspecified ellipsis; the format: slot named the slot but did not fill the value template; without a concrete format template, a BLOCKED model may produce free-form prose ("the workaround cost direction is not stated") rather than the structured traceable label (`"Precondition A: cost direction absent"`) that C-38's row-level identifiability depends on |
| C-43 | Self-test affirmative branch names the violated architectural contract alongside the failure class | R16 V-01's Phase 2 self-test: "If yes: you have written a basis-negation — a Phase 2 charter violation." — the contract label upgrades the diagnostic from content-level (what error was made) to structural-level (which guarantee is now broken), enabling targeted correction ("address a dimension Phase 1 did not confirm") rather than generic revision; also makes the failure traceable at the output level without cross-referencing the charter definition |

R16 V-01, V-03, V-04 already satisfy C-43 (Phase 2 self-test includes "— a Phase 2 charter violation"). R16 V-05 champion's self-test cites REMEDIATION but omits the contract label — C-43 is a targeted fix. C-42 requires adding the value template to the format: slot in all variations. R17 variations explore:

1. Whether C-42 + C-43 can be achieved in the minimal single-phase architecture (no role separation), and what the appropriate contract label is for a single-phase gap field
2. Whether the second-person register absorbs C-43's contract label without friction
3. Whether C-42 is a mechanical addition to the two-phase design — one targeted change achieves the maximum attainable score
4. Whether the lifecycle-heavy Phase 0 creates a triple-mechanism BLOCKED/CLEAR determination: narrative context + fill/leave-blank condition + value format all resolvable from the column header alone
5. What structural patterns beyond C-42 + C-43 the champion can push toward — specifically whether the self-test can prescribe a corrective action scope alongside the contract label as a C-44 candidate

**Axes selected:**

| Variation | Axis | Hypothesis |
|---|---|---|
| V-01 | Inertia framing (single-phase minimal; C-42 format: slot in CLOSED-LABEL header; C-43 single-phase contract label: "gap field production contract violation") | R16 single-phase V-02 scored 27/33 aspirational = 8.18. R17 V-01 makes exactly two structural changes to R16 V-02: (a) CLOSED-LABEL header adds `format: "Precondition [A/B]: [named condition]"` slot (C-42); (b) self-test affirmative branch adds contract label `"— a gap field production contract violation"` (C-43). Hypothesis: C-42 is mechanical — it fills in the template that R16 left as an ellipsis; C-43 for single-phase names the gap field's own production guarantee rather than a phase charter. Both fit the minimal single-phase architecture without role-separation overhead. |
| V-02 | Phrasing register (second-person throughout; single-phase; C-42 format: slot in second-person CLOSED-LABEL; C-43 contract label in second-person direct address) | R16 V-02 second-person register already had "Your CLOSED-LABEL [fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: …]". C-42 fills the format template in second-person voice: `format: "Precondition [A/B]: [named condition]"`. C-43's contract label in second-person becomes a direct personal diagnostic: "you have written a basis-negation — a gap field production contract violation." Hypothesis: second-person register makes C-43 more confrontational than third-person — "you have violated" names a personal production failure, not just a category error; this directness may reduce the rate at which the model produces generic revisions rather than dimension-specific corrections. |
| V-03 | Role sequence (two-phase; Phase 0 C-42 format: slot added to CLOSED-LABEL header; Phase 2 C-43 already present from R16 V-01; one targeted structural change) | R16 V-01 two-phase design scored 32/33 aspirational = 9.70, with C-43 already present ("— a Phase 2 charter violation"). R17 V-03 makes exactly one structural change: CLOSED-LABEL column header adds `format: "Precondition [A/B]: [named condition]"` (C-42). Hypothesis: C-42 is a mechanical addition to the two-phase design — filling the value template in the existing format: slot. Expected outcome: 34/35 aspirational (C-28 FAIL only, structurally inapplicable to multi-phase), the maximum attainable score for a multi-phase variation, achievable with one targeted change. |
| V-04 | Lifecycle emphasis (three-phase; expanded per-precondition Phase 0 narrative sections + gate-decision summary table upgraded to C-42 format: slot; Phase 2 C-43 confirmed; triple-mechanism BLOCKED/CLEAR determination) | R16 V-03 lifecycle-heavy Phase 0 (per-precondition narrative sections with inline failure examples) + C-41 conditional header created a dual-mechanism BLOCKED/CLEAR determination: narrative context primes the condition, column header enforces fill/leave-blank behavior. R17 V-04 adds C-42's format: slot to create a triple-mechanism: (a) narrative section primes the precondition requirement, (b) C-41 fill/leave-blank in header, (c) C-42 value template in header — all three independently signal the expected behavior on a BLOCKED row without requiring model cross-reference to examples. Hypothesis: three independent signals in the column header reduce malformed CLOSED-LABEL values more than two signals alone. |
| V-05 | Output format + role sequence (three-phase; R16 champion evolution; C-42 format: slot; C-43 contract label added alongside REMEDIATION reference; C-44 candidate: self-test affirmative branch prescribes corrective scope by name) | R16 V-05 champion: ENTRY GATE delimiter; STATUS + CLOSED-LABEL + EVIDENCE + CLEAR-PATH gate table; four-field DIAGNOSTIC PATTERN with REMEDIATION; compilation pointer row. C-43 gap: self-test said "Apply the REMEDIATION above" without naming the architectural contract. R17 V-05 fixes C-43 by adding the contract label AND extends it: "If yes: you have written a basis-negation — a Phase 2 charter violation. Address a dimension Phase 1 did not confirm. See REMEDIATION above." The self-test affirmative branch now carries: (1) failure class, (2) architectural contract, (3) corrective scope ("address a dimension Phase 1 did not confirm"), (4) recovery mechanism reference ("See REMEDIATION above"). Hypothesis: (3) is a C-44 candidate — it prescribes not just what error was made but what corrective action resolves it at the structural level, without the model needing to infer the correction from the failure class alone. |

---

## V-01 — Axis: Inertia framing (Single-phase; C-42 format: slot in CLOSED-LABEL; C-43 single-phase contract label; no role separation)

**Variation axis**: Inertia framing — the status-quo cost is featured in Phase 0 as the first precondition (Precondition A), requiring an explicit workaround name, ongoing cost, and cost direction before any sizing analysis begins. Phase 0 gate table satisfies C-38 (STATUS + CLOSED-LABEL columns per precondition row); CLOSED-LABEL header upgraded to C-42 compliance by adding `format:` slot specifying value template. Self-test adds C-43 contract label: "— a gap field production contract violation." Single-phase analysis; no role separation.

**Hypothesis**: R16 single-phase V-02 scored 27/33 = 8.18 aspirational. R17 V-01 makes exactly two structural changes: (a) CLOSED-LABEL column header adds `format: "Precondition [A/B]: [named condition]"` filling the template that R16 left as an ellipsis (C-42); (b) self-test affirmative branch adds the contract label "— a gap field production contract violation" alongside the failure class (C-43). For single-phase, the violated contract is the gap field's own production guarantee: name a dimension the basis did not verify. Both changes fit the minimal single-phase design without role-separation overhead.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before any analysis begins. Proceed through each step in order.

---

## Phase 0: Entry Gate

Fill the precondition table. Both rows must show CLEAR before Step 1 begins.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|---|
| **A — Inertia** | Workaround (or named cost of absence) stated with a cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')."
> **Example — both CLEAR**: Gate = OPEN.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---|---|---|---|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Step 1 begins only if Gate = OPEN._

---

## Sizing Steps [Gate must be OPEN before proceeding]

### Step 1: Surface Area

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each individually — "API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
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
|---|---|
| | |

---

### Step 3: Team-Size Signal

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| | |
| **Total FTEs** | |

---

### Step 4: Timeline Signal

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a calendar date, not a single number] |
|---|
| |

---

### Step 5: Confidence Basis

State only what IS established here. What is NOT known gets its own section below.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|---|---|
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
> **If yes: you have written a basis-negation — a gap field production contract violation.** Restate to name a dimension the Step 5 basis did not verify.
> If no: proceed.

**Your Confidence Gap** [must address a dimension not covered by Step 5 — not a negation of it]:

Gap: _____

---

### Step 6: Confidence Calibration

| What Would Raise Confidence | What Would Lower Confidence |
|---|---|
| | |

---

### Step 7: Tier Sensitivity

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Value |
|---|---|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Inertia Check | [workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise / what would lower] |
| Confidence Gap | → See `── CONFIDENCE GAP CHECKPOINT ──` section above |

---

---

## V-02 — Axis: Phrasing register (Second-person throughout; single-phase; C-42 format: slot in second-person CLOSED-LABEL; C-43 contract label in direct address)

**Variation axis**: Phrasing register — all instructions and constraint language addressed in second person throughout ("you are running," "your gate," "your gap"); Phase 0 formal two-row precondition table with STATUS and CLOSED-LABEL columns (C-38); CLOSED-LABEL header upgraded to C-42 compliance in second-person voice: `"Your CLOSED-LABEL [fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: 'Precondition [A/B]: [named condition]']"`; self-test affirmative branch names both the failure class and the violated contract in second person (C-43). Single-phase; no role separation.

**Hypothesis**: R16 V-02 second-person register already had "Your CLOSED-LABEL [fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: …]" — the format: slot existed but held an ellipsis. C-42 fills the template. The second-person register has a structural implication for C-43: "you have written a basis-negation" becomes "you have written a basis-negation — a gap field production contract violation" — the contract label in second-person is a personal violation ("you have violated"), not a category label. This directness may reduce the rate at which the model produces generic revisions rather than dimension-specific corrections. Hypothesis: second-person C-43 reinforces the diagnostic-observer stance already established by the second-person DETECTION PATTERN ("your gap is derivable by negation from your Step 5 basis").

---

You are running a **scout-size** sizing signal. Your output is a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. MODERATE, 3/5, medium-high, and "complex" are not valid tier values.

Before you begin sizing, fill Phase 0 and close your entry gate. Then work through each step in order.

---

## Phase 0: Entry Gate

Fill the precondition table below. Both rows must show CLEAR before you proceed to Step 1.

| Precondition | Requirement | Your Status [CLEAR / BLOCKED] | Your CLOSED-LABEL [fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|---|
| **A — Inertia** | You can state a workaround (or named cost of absence) with a cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | The feature description you have been given contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "Precondition A: cost direction absent — you have named a workaround but have not stated whether building is cheaper, comparable, or more expensive."
> **Example — B BLOCKED**: Your Status: BLOCKED. Your CLOSED-LABEL: "Precondition B: plan-level artifact detected — you found 'Sprint 1: implement API endpoint, owner: backend lead' in the feature description."
> **Example — both CLEAR**: Your gate = OPEN.

| Precondition A: Your Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost [friction you observe today] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---|---|---|---|
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
|---|---|
| | |
| | |
| **Total integration points [numeric count required]** | |

---

### Step 2: Complexity Tier + Primary Driver

Assign exactly one tier. Name the causal factor that most drives your rating.

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. You must use exactly: LOW / MEDIUM / HIGH / XL.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — You have not named a causal factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors — "it's complex" fails] |
|---|---|
| | |

---

### Step 3: Team-Size Signal

Name the specialist discipline for each role you identify.

> **WRONG**: "2–3 engineers" — You have not named disciplines. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| | |
| **Total FTEs** | |

---

### Step 4: Timeline Signal

Give a sprint range, not a calendar date, not a single number.

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a calendar date, not a single number] |
|---|
| |

---

### Step 5: Confidence Basis

State only what IS established. What is NOT known goes in your confidence gap below.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|---|---|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify your primary source of residual uncertainty. It must address a **different dimension** than your Step 5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb it before producing your gap.

**WRONG** (basis-negation):

Step 5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: your gap is derivable from your Step 5 basis by direct negation — "X is stable" becomes "X is not confirmed"; you did not investigate a new dimension; a reader can produce your gap by negating your basis
> **WHY IT FAILS**: your reader learns nothing from your gap that your Step 5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty

**CORRECT** (genuine gap):

Step 5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: you have named a dimension your basis did not verify. Your reader cannot derive it from Step 5 by negation.

---

**Self-test — run before writing your gap:**

> Ask yourself: if I reversed something from my Step 5 basis ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a gap field production contract violation.** Restate to name a dimension your Step 5 basis did not verify.
> If no: proceed.

**Your Confidence Gap** [must address a dimension not covered by your Step 5 — not a negation of it]:

Gap: _____

---

### Step 6: Confidence Calibration

| What Would Raise Your Confidence | What Would Lower Your Confidence |
|---|---|
| | |

---

### Step 7: Tier Sensitivity

Each direction: one single named falsifiable condition with an explicit tier destination that differs from your current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from your current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Your Value |
|---|---|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what you established] |
| Inertia Check | [your workaround — cost direction — key driver] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise / what would lower your confidence] |
| Confidence Gap | → See your `── CONFIDENCE GAP CHECKPOINT ──` section above |

---

---

## V-03 — Axis: Role sequence (Two-phase; Phase 0 C-42 format: slot; Phase 2 C-43 already present; one targeted structural change from R16 V-01)

**Variation axis**: Role sequence — Phase 1 Sizing Analyst produces surface area, complexity tier, team-size, timeline, and confidence basis; Phase 2 Risk Assessor produces confidence gap, calibration, and tier sensitivity. Phase 0 gate table upgraded to C-42 compliance by adding `format:` slot to CLOSED-LABEL column header (the only structural change from R16 V-01). Phase 2 self-test retains C-43-compliant contract label from R16 V-01: "— a Phase 2 charter violation." Full C-20 cluster with role charters, field exclusion lists, and role ownership tags.

**Hypothesis**: R16 V-01 scored 32/33 aspirational = 9.70, with C-43 already present in the Phase 2 self-test ("— a Phase 2 charter violation") and all other aspirational criteria passing. The only gap under v17 is C-42: CLOSED-LABEL header needs the value format template. R17 V-03 makes exactly one structural change — fills `format: …` with `format: "Precondition [A/B]: [named condition]"`. Expected outcome: 34/35 aspirational (C-28 structurally inapplicable to multi-phase design; all other 34 criteria pass), the maximum attainable score for a multi-phase variation, achieved with one targeted addition.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before beginning Phase 1. Phases run in sequence: Phase 0 → Phase 1 → Phase 2.

---

## Phase 0: Entry Gate

Fill the precondition table. Both rows must show CLEAR before Phase 1 begins.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "Precondition [A/B]: [named condition]"] |
|---|---|---|---|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')."
> **Example — both CLEAR**: Gate = OPEN.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---|---|---|---|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst

**Charter**: Produce P1-1 through P1-5 and P1-7 below. Do NOT produce confidence gap, confidence calibration, or tier sensitivity here — those are reserved for Phase 2.

**Fields owned by Phase 1 [Phase 1 Sizing Analyst]**: Surface Area (P1-1) · Complexity Tier + Driver (P1-2) · Team-Size Signal (P1-3) · Timeline Signal (P1-4) · Confidence Basis (P1-5) · Tier Sensitivity (P1-7)

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Primary Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|---|---|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Phase 1 Sizing Analyst — name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| | |
| **Total FTEs** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format — not a calendar date, not a single number] |
|---|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State only what IS established. The confidence gap — what is NOT known — is reserved for Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established] |
|---|---|
| | |

---

### P1-7: Tier Sensitivity [Phase 1 Sizing Analyst]

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [Phase 1 Sizing Analyst — one scenario] | Destination Tier [Phase 1 Sizing Analyst — must differ from current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Phase 2: Risk Assessor

**Charter**: Assess residual uncertainty. Produce P2-6 (confidence gap) and P2-6b (calibration). Do NOT re-assess surface area, tier, team-size, timeline, or any item in the P1-5 confirmed set.

**Fields owned by Phase 2 [Phase 2 Risk Assessor]**: Confidence Gap (P2-6) · Confidence Calibration (P2-6b)

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., if Phase 1 stated "the auth API contract is stable," Phase 2 must not produce "auth API contract is unconfirmed." That is a basis-negation.

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Must address a **different dimension** than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb it before producing your gap.

**WRONG** (basis-negation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the P1-5 basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required; a reader can derive it from P1-5 by negation alone
> **WHY IT FAILS**: a reader learns nothing from this gap that the P1-5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension the P1-5 basis did not verify. Not derivable from P1-5 by negation.

---

**Self-test — run before writing your gap:**

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Address a dimension Phase 1 did not confirm.
> If no: proceed.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension not covered by P1-5 — not a negation of it]**:

Gap: _____

---

### P2-6b: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence | What Would Lower Confidence |
|---|---|
| | |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Value | Produced By |
|---|---|---|
| Surface Area | [named points — N integration points] | Phase 1 Sizing Analyst |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] | Phase 1 Sizing Analyst |
| Primary Complexity Driver | [1–2 named factors] | Phase 1 Sizing Analyst |
| Team-Size Signal | [specialist disciplines + fractions] | Phase 1 Sizing Analyst |
| Timeline Signal | [N–M sprints] | Phase 1 Sizing Analyst |
| Confidence Level + Basis | [LEVEL — what is established] | Phase 1 Sizing Analyst |
| Inertia Check | [workaround — cost direction — key driver] | Phase 0 Gate |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Confidence Calibration | [what would raise / what would lower] | Phase 2 Risk Assessor |
| Confidence Gap | → See `── CONFIDENCE GAP CHECKPOINT ──` section above | Phase 2 Risk Assessor |

---

---

## V-04 — Axis: Lifecycle emphasis (Three-phase; expanded Phase 0 per-precondition narrative sections; gate-decision table upgraded to C-42 format: slot; Phase 2 C-43 contract label; triple-mechanism BLOCKED/CLEAR determination)

**Variation axis**: Lifecycle emphasis — Phase 0 receives expanded document space with a named section per precondition, each containing a requirement statement, failure example, and clear example before the model fills the precondition row. The gate-decision summary table at the end of Phase 0 is upgraded to C-42 compliance: CLOSED-LABEL column header includes `format: "Precondition [A/B]: [named condition]"` alongside fill/leave-blank conditions. Phase 1 Sizing Analyst and Phase 2 Risk Assessor retain full C-20 cluster. Phase 2 self-test includes C-43 contract label. Triple-mechanism BLOCKED/CLEAR determination: (a) per-precondition narrative primes the requirement, (b) C-41 fill/leave-blank condition in column header, (c) C-42 value format template in column header.

**Hypothesis**: R16 V-03 lifecycle-heavy Phase 0 created a dual-mechanism: narrative sections primed each precondition's requirement before the model reached the gate table, and the C-41 conditional header enforced fill/leave-blank behavior at the schema level. C-42 adds a third mechanism: the value format template makes the expected CLOSED-LABEL value structure derivable from the column header alone — a BLOCKED row does not need to parse examples to know the format is `"Precondition A: cost direction absent"`. The three mechanisms together address three different failure modes: failure to understand the requirement (narrative), failure to leave blank when CLEAR (C-41), failure to use the structured format when filling (C-42). C-43 is present from R16 V-03 equivalent. Expected: 34/35 aspirational.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before beginning Phase 1. Phases run in sequence: Phase 0 → Phase 1 → Phase 2.

---

## Phase 0: Entry Gate

Both preconditions must be met before Phase 1 begins. Read each precondition section before filling the gate-decision table.

---

### Precondition A — Inertia

**Requirement**: A workaround (or named cost of absence) is stated with a cost direction: cheaper / comparable / more expensive than building the feature.

The inertia check is the sizing signal's most durable anchor. Every feature competes with the cost of not building it. A feature that is cheaper to build than the workaround has different priority economics than a feature that is more expensive. Without a cost direction, the sizing signal cannot feed program-plan's priority triage.

> **WRONG (A fails)**: "Teams manage this with a spreadsheet today." — Workaround named; cost direction absent. Gate = CLOSED — Precondition A: cost direction absent.
> **CORRECT (A passes)**: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team and scales with team count."

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---|---|---|---|
| | | | |

---

### Precondition B — Signal Boundary

**Requirement**: The feature description contains no plan-level artifacts — no task breakdowns, sprint assignments, owner names, or milestone dates. These belong in `program-plan`, not in sizing signal input.

If the feature description includes plan-level artifacts, the sizing signal's scope is polluted. Size the feature intent, not someone else's preliminary plan. If the description includes "Sprint 1: implement API endpoint," the sizing analysis will anchor to that decomposition rather than derive its own surface area estimate.

> **WRONG (B fails)**: Feature description includes "Sprint 1: implement API endpoint, owner: backend lead, due: March 30." — Gate = CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead, due: March 30').
> **CORRECT (B passes)**: Feature description describes capability and integration requirements without sprint assignments, owner names, or milestone dates.

---

### Gate-Decision Table

Fill both rows. Advance to Phase 1 only when both rows show CLEAR.

| Precondition | Requirement Summary | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "Precondition [A/B]: [named condition]"] |
|---|---|---|---|
| **A — Inertia** | Workaround + cost direction present | | |
| **B — Signal boundary** | No plan-level artifacts in feature description | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

---

## Phase 1: Sizing Analyst

**Charter**: Produce P1-1 through P1-5 and P1-7. Do NOT produce confidence gap, confidence calibration, or tier sensitivity here — those are reserved for Phase 2.

**Fields owned by Phase 1 [Phase 1 Sizing Analyst]**: Surface Area · Complexity Tier + Driver · Team-Size Signal · Timeline Signal · Confidence Basis · Tier Sensitivity

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Primary Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|---|---|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Phase 1 Sizing Analyst — name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| | |
| **Total FTEs** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|---|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State only what IS established. What is NOT known is reserved for Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established] |
|---|---|
| | |

---

### P1-7: Tier Sensitivity [Phase 1 Sizing Analyst]

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [Phase 1 Sizing Analyst — one scenario] | Destination Tier [Phase 1 Sizing Analyst — must differ from current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Phase 2: Risk Assessor

**Charter**: Assess residual uncertainty. Produce confidence gap (P2-6) and calibration (P2-6b). Do NOT produce any item from the P1-5 confirmed set — including negations of confirmed items.

**Fields owned by Phase 2 [Phase 2 Risk Assessor]**: Confidence Gap · Confidence Calibration

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is unconfirmed" when P1-5 states "API contract is stable" is a basis-negation and a Phase 2 charter violation.

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Must address a **different dimension** than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field. Absorb it before producing your gap.

**WRONG** (basis-negation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the P1-5 basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required; a reader can derive it from P1-5 by negation alone
> **WHY IT FAILS**: a reader learns nothing from this gap that the P1-5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension the P1-5 basis did not verify. Not derivable from P1-5 by negation.

---

**Self-test — run before writing your gap:**

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Address a dimension Phase 1 did not confirm.
> If no: proceed.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension not covered by P1-5 — not a negation of it]**:

Gap: _____

---

### P2-6b: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence | What Would Lower Confidence |
|---|---|
| | |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Value | Produced By |
|---|---|---|
| Surface Area | [named points — N integration points] | Phase 1 Sizing Analyst |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] | Phase 1 Sizing Analyst |
| Primary Complexity Driver | [1–2 named factors] | Phase 1 Sizing Analyst |
| Team-Size Signal | [specialist disciplines + fractions] | Phase 1 Sizing Analyst |
| Timeline Signal | [N–M sprints] | Phase 1 Sizing Analyst |
| Confidence Level + Basis | [LEVEL — what is established] | Phase 1 Sizing Analyst |
| Inertia Check | [workaround — cost direction — key driver] | Phase 0 Gate |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Confidence Calibration | [what would raise / what would lower] | Phase 2 Risk Assessor |
| Confidence Gap | → See `── CONFIDENCE GAP CHECKPOINT ──` section above | Phase 2 Risk Assessor |

---

---

## V-05 — Axis: Output format + role sequence (Three-phase; R16 champion evolution; C-42 format: slot; C-43 contract label + corrective scope; C-44 candidate: self-test prescribes recovery by REMEDIATION reference)

**Variation axis**: Output format + role sequence — retains all R16 V-05 champion structural patterns: `── ENTRY GATE ──` visual delimiter wrapping Phase 0; gate table with STATUS + CLOSED-LABEL + EVIDENCE + CLEAR-PATH columns (C-38, bidirectional operational schema); four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION as fourth field (C-39, extends minimum). Adds C-42: CLOSED-LABEL column header filled with `format: "Precondition [A/B]: [named condition]"` value template. Adds C-43: Phase 2 self-test now includes "— a Phase 2 charter violation" alongside the REMEDIATION reference. C-44 candidate: self-test affirmative branch prescribes corrective scope AND names the recovery mechanism: "you have written a basis-negation — a Phase 2 charter violation. Address a dimension Phase 1 did not confirm. See REMEDIATION above."

**Hypothesis**: R16 V-05's self-test said "Apply the REMEDIATION above" — it cited the recovery mechanism but omitted the architectural contract label, failing C-43. R17 V-05 fixes C-43 by adding "— a Phase 2 charter violation" and extends it further: the affirmative branch now carries four elements: (1) failure class (`basis-negation`), (2) architectural contract (`Phase 2 charter violation`), (3) corrective scope (`Address a dimension Phase 1 did not confirm` — prescribes what to do, not just what went wrong), (4) recovery mechanism reference (`See REMEDIATION above`). Element (3) is a C-44 candidate: it prescribes the corrective action at the structural level, making the self-test not just a detector but a prescriber. The REMEDIATION field in the four-field DIAGNOSTIC PATTERN enables this — without a named recovery field in the pattern, element (4) would have no target to reference.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before beginning Phase 1. Phases run in sequence: Phase 0 → Phase 1 → Phase 2.

---

## ── ENTRY GATE ──

Fill the precondition table. Both rows must show CLEAR before Phase 1 begins.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED-LABEL [fill only if STATUS = BLOCKED — leave blank if STATUS = CLEAR — format: "Precondition [A/B]: [named condition]"] | EVIDENCE [fill only if STATUS = CLEAR — name the artifact or observation that confirms this precondition] | CLEAR-PATH [fill only if STATUS = BLOCKED — name the specific investigation that would resolve this block and permit CLEAR] |
|---|---|---|---|---|---|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | | | |

> **Example — A BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)." CLEAR-PATH: "Ask the PM for the inertia framing: 'Is building cheaper, comparable, or more expensive than the current workaround?'"
> **Example — B BLOCKED**: Status: BLOCKED. CLOSED-LABEL: "Precondition B: plan-level artifact detected ('Sprint 1: implement API endpoint, owner: backend lead')." CLEAR-PATH: "Request a revised feature description scoped to intent and integration requirements only — no sprint assignments or owner names."
> **Example — A CLEAR**: Status: CLEAR. EVIDENCE: "Feature brief section 2: 'Manual CSV export per team — building is cheaper long-term; overhead grows ~45 min/sprint/team.'" CLEAR-PATH: (leave blank).
> **Example — both CLEAR**: Gate = OPEN.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---|---|---|---|
| | | | |

**Gate output [produce exactly one]**: **OPEN** / **CLOSED — Precondition [A / B]: [name unmet condition]**

_Phase 1 begins only if Gate = OPEN._

## ── END ENTRY GATE ──

---

## Phase 1: Sizing Analyst

**Charter**: Produce P1-1 through P1-5 and P1-7. Do NOT produce confidence gap, confidence calibration, or tier sensitivity here — those are reserved for Phase 2.

**Fields owned by Phase 1 [Phase 1 Sizing Analyst]**: Surface Area · Complexity Tier + Driver · Team-Size Signal · Timeline Signal · Confidence Basis · Tier Sensitivity

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration

---

### P1-1: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [Phase 1 Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total integration points [Phase 1 Sizing Analyst — numeric count required]** | |

---

### P1-2: Complexity Tier + Primary Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [Phase 1 Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [Phase 1 Sizing Analyst — 1–2 named causal factors] |
|---|---|
| | |

---

### P1-3: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [Phase 1 Sizing Analyst — name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| | |
| **Total FTEs** | |

---

### P1-4: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1 Sizing Analyst — N–M format] |
|---|
| |

---

### P1-5: Confidence Basis [Phase 1 Sizing Analyst]

State only what IS established. What is NOT known is reserved for Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established] |
|---|---|
| | |

---

### P1-7: Tier Sensitivity [Phase 1 Sizing Analyst]

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [Phase 1 Sizing Analyst — one scenario] | Destination Tier [Phase 1 Sizing Analyst — must differ from current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Phase 2: Risk Assessor

**Charter**: Assess residual uncertainty. Produce confidence gap (P2-6) and calibration (P2-6b). Do NOT produce any item from the P1-5 confirmed set — including negations of confirmed items.

**Fields owned by Phase 2 [Phase 2 Risk Assessor]**: Confidence Gap · Confidence Calibration

**Prohibited content category**: any item in the P1-5 confirmed set — e.g., "API contract is unconfirmed" when P1-5 states "API contract is stable" is a basis-negation and a Phase 2 charter violation.

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Must address a **different dimension** than the P1-5 confidence basis.

---

### ── DIAGNOSTIC PATTERN ──

The following pattern names, diagnoses, and prescribes the recovery for the most common failure in this field. Absorb all four fields before producing your gap.

**WRONG** (basis-negation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the P1-5 basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required; a reader can derive it from P1-5 by negation alone
> **WHY IT FAILS**: a reader learns nothing from this gap that the P1-5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty
> **REMEDIATION**: restate the gap to name a dimension Phase 1 did not assess — not a re-examination of what Phase 1 confirmed, but an orthogonal unknown (e.g., concurrent behavior, failure semantics, scaling boundary, external dependency state)

**CORRECT** (genuine gap):

P1-5 basis: "Auth API contract is stable."
Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."

Why it passes: names a dimension the P1-5 basis did not verify. Not derivable from P1-5 by negation. Not a re-examination of the confirmed API contract — an orthogonal unknown (concurrent delivery semantics).

---

**Self-test — run before writing your gap:**

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation. Address a dimension Phase 1 did not confirm. See REMEDIATION above.**
> If no: proceed.

**Confidence Gap [Phase 2 Risk Assessor — must address a dimension not covered by P1-5 — not a negation of it]**:

Gap: _____

---

### P2-6b: Confidence Calibration [Phase 2 Risk Assessor]

| What Would Raise Confidence | What Would Lower Confidence |
|---|---|
| | |

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Value | Produced By |
|---|---|---|
| Surface Area | [named points — N integration points] | Phase 1 Sizing Analyst |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] | Phase 1 Sizing Analyst |
| Primary Complexity Driver | [1–2 named factors] | Phase 1 Sizing Analyst |
| Team-Size Signal | [specialist disciplines + fractions] | Phase 1 Sizing Analyst |
| Timeline Signal | [N–M sprints] | Phase 1 Sizing Analyst |
| Confidence Level + Basis | [LEVEL — what is established] | Phase 1 Sizing Analyst |
| Inertia Check | [workaround — cost direction — key driver] | Phase 0 Gate |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] | Phase 1 Sizing Analyst |
| Confidence Calibration | [what would raise / what would lower] | Phase 2 Risk Assessor |
| Confidence Gap | → See `── CONFIDENCE GAP CHECKPOINT ──` section above | Phase 2 Risk Assessor |
