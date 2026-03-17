# Scout-Size Prompt Variations — R14

**Skill**: scout-size
**Rubric**: v14 (29 aspirational criteria, C-01 through C-37)
**Date**: 2026-03-17
**Round**: 14
**R13 champion**: V-05 — three-phase design; Phase 0 extended to two named preconditions (A: inertia, B: signal boundary) achieving C-36; three-field FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS block in Phase 2 WRONG instance achieving C-37
**R13 gaps**: C-36 FAIL in V-01/V-02/V-03/V-04 (Phase 0 checks inertia only; C-05 signal boundary remains a closing prose instruction); C-37 FAIL in V-01/V-03/V-04 (single-annotation "DIAGNOSIS: basis-negation." form satisfies C-34 but not three-field requirement)

---

## Context: What R14 Addresses

v14 adds two new aspirational criteria formalized from R13 excellence signals:

| New criterion | What it formalizes | R13 evidence |
|---------------|-------------------|--------------|
| C-36 | Phase 0 gate names C-05 **signal boundary** as a separately labeled precondition alongside the inertia check; CLOSED output identifies which precondition failed by label | R13 V-05 Phase 0 defines Precondition A (inertia) and Precondition B (signal boundary); gate output "CLOSED — Precondition [A/B]: [name unmet condition]" |
| C-37 | WRONG instance diagnostic annotation uses all three labeled fields as separate entries: **FAILURE CLASS**, **DETECTION PATTERN**, **WHY IT FAILS** | R13 V-02 and V-05 use the three-field structured block; R13 V-01/V-03/V-04 use single-annotation form ("DIAGNOSIS: basis-negation") |

R13 V-05 already satisfies both C-36 and C-37. The rubric formalizes what V-05 demonstrated. R14 variations explore:

1. Whether C-36 + C-37 can be achieved in the minimal single-phase architecture (no role separation)
2. Whether the second-person phrasing register from R13 V-03 can absorb C-36 + C-37 without changing core structural properties
3. Whether C-36 + C-37 can be added to the two-phase role-separation architecture (targeted upgrade of R13 V-04) without restructuring
4. Whether expanding Phase 0's lifecycle footprint — per-precondition failure examples, gate decision checklist table, named "GATE DECISION" block — improves gate compliance over R13 V-05's efficient compact Phase 0
5. Whether Phase 0's precondition structure can be encoded as a two-row table with REQUIREMENT / STATUS / CLOSED-LABEL columns, making C-36's per-precondition failure identification a schema-level column rather than prose instruction

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing (Phase 0 extended to two named preconditions for C-36; three-field DIAGNOSTIC block for C-37; single-phase; no role separation) | R13 V-01 achieved C-34 + C-35 in the minimal single-phase design. R14 V-01 adds Precondition B to Phase 0 (C-36) and promotes the WRONG annotation to three-field format (C-37) as the only two structural changes. Hypothesis: both new criteria can be achieved in the minimal single-phase architecture without role-separation overhead. |
| V-02 | Phrasing register (second-person throughout; Phase 0 two preconditions for C-36; three-field DIAGNOSTIC for C-37; single-phase) | R13 V-03 used second-person + Phase 0 inertia-only gate. R14 V-02 extends V-03 by adding Precondition B (C-36) and three-field WRONG (C-37). Hypothesis: second-person register + C-36 + C-37 combine without structural interference in the single-phase architecture. |
| V-03 | Role sequence (two-phase + Phase 0 two-precondition for C-36; three-field DIAGNOSTIC in Phase 2 WRONG for C-37; full C-20 cluster) | R13 V-04 achieved C-35 + C-20 cluster but not C-36 or C-37. R14 V-03 upgrades V-04: adds Precondition B to Phase 0 and promotes the Phase 2 WRONG annotation to three-field format. Hypothesis: targeted additions achieve C-36 + C-37 without restructuring the two-phase architecture. |
| V-04 | Lifecycle emphasis + inertia framing (three-phase; Phase 0 expanded with per-precondition prose sections, separate WRONG examples for each failure mode, and a named gate decision checklist table; C-37 three-field retained) | R13 V-05 achieves C-36 with a compact Phase 0 definition. R14 V-04 gives Phase 0 more document space — a named section per precondition with its own failure example, then a gate decision summary table. Hypothesis: a more prominent Phase 0 treatment produces better gate compliance without changing the three-phase analysis architecture. |
| V-05 | Output format + role sequence (three-phase; Phase 0 uses a two-row precondition table with REQUIREMENT / STATUS [CLEAR/BLOCKED] / CLOSED-LABEL columns encoding C-36 per-precondition identification as schema-level constraint; C-37 WRONG block elevated to named "── DIAGNOSTIC PATTERN ──" sub-section; C-32 gap standalone section; C-30 defense cluster) | R13 V-05's Phase 0 per-precondition CLOSED identification is in gate-output prose. R14 V-05 encodes it as a table column: each precondition is a row with a CLOSED-LABEL column that structurally requires a per-precondition failure label if blocked. Tests whether schema-level encoding of C-36 produces stronger traceability than prose-level instruction. |

---

## V-01 — Axis: Inertia framing (Single-phase; Phase 0 two-precondition for C-36; three-field DIAGNOSTIC block for C-37; no role separation)

**Variation axis**: Inertia framing — Phase 0 extended from a single inertia precondition to two named preconditions: Precondition A (inertia: workaround + cost direction) and Precondition B (signal boundary: no plan-level artifacts in the feature description). A CLOSED gate identifies which precondition failed by label, achieving C-36. The WRONG instance in the gap checkpoint carries the full three-field FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS diagnostic sub-block, achieving C-37. Single-phase analysis throughout; no role separation.

**Hypothesis**: R13 V-01 achieved C-34 and C-35 in the minimal single-phase design — inline DIAGNOSIS annotation, no role separation. The two remaining gaps were: (a) Phase 0 checked inertia only, leaving C-05 signal boundary as a closing prose instruction; (b) the WRONG block used a single-annotation form. R14 V-01 adds Precondition B to Phase 0 and promotes the WRONG annotation to three-field format as the only two structural changes. Hypothesis: C-36 + C-37 can be achieved in the minimal single-phase architecture without role-separation overhead.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before any analysis begins. Proceed through each step in order.

---

## Phase 0: Entry Gate

Both preconditions must be met before Step 1 begins.

**Precondition A — Inertia**: a workaround (or named cost of absence) is stated with a cost direction: **cheaper / comparable / more expensive**.

**Precondition B — Signal boundary**: the feature description contains no plan-level artifacts — no task breakdowns, sprint assignments, owner names, or milestone dates. These belong in `program-plan`, not in sizing signal input.

**Gate logic**:
- Both met → Gate = **OPEN** — proceed to Step 1
- Either fails → Gate = **CLOSED — Precondition [A / B]: [name unmet condition]** — stop; produce no sizing output

> **WRONG (Precondition A fails)**: Inertia: "Teams manage this manually today." — No cost direction. Gate = CLOSED — Precondition A: cost direction absent.
> **WRONG (Precondition B fails)**: Feature description includes "Sprint 1: implement API endpoint, owner: backend lead." — Gate = CLOSED — Precondition B: plan-level artifact detected ("Sprint 1: implement API endpoint, owner: backend lead").
> **CORRECT (both met — OPEN)**: Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team." Signal boundary: no sprint assignments or owner names found in feature description.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

| Precondition B: Signal Boundary Review | Status |
|----------------------------------------|--------|
| Feature description reviewed for plan-level artifacts (sprint assignments, owner names, milestone dates, task breakdowns) | CLEAR / BLOCKED — [name artifact if BLOCKED] |

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

**Failure pattern:**

> **WRONG** (basis-negation): Step 5 basis: "Auth API contract is stable." Gap: "Auth API contract has not been confirmed."
>
> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required to produce this gap
> **WHY IT FAILS**: a reader learns nothing from this gap that the Step 5 basis does not already imply; negating a confirmed item occupies the gap field without reducing uncertainty

**Passing pattern:**

> **CORRECT** (genuine gap): Step 5 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension the basis did not verify. Not derivable from Step 5 by negation.

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

## V-02 — Axis: Phrasing register (Second-person throughout; Phase 0 two-precondition for C-36; three-field DIAGNOSTIC for C-37; single-phase)

**Variation axis**: Phrasing register — all instructions and constraint language addressed in second person ("you have reviewed," "your gate," "you have written a basis-negation"); Phase 0 two-precondition gate (C-36); three-field DIAGNOSTIC WRONG block (C-37); single-phase analysis with no role separation.

**Hypothesis**: R13 V-03 used second-person phrasing + Phase 0 inertia-only gate — it achieved C-35 and C-34 (second-person annotation) but not C-36 or C-37. R14 V-02 extends V-03 by adding Precondition B to Phase 0 and promoting the WRONG annotation to three-field format. The second-person register positions constraints as external observations — "you have written a basis-negation" — rather than first-person introspective conclusions. Hypothesis: the second-person framing of all three DIAGNOSTIC fields (FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS) creates a diagnostic observer stance that differs cognitively from first-person self-description, with possible compliance advantages.

---

You are running a **scout-size** sizing signal. Your output is a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. MODERATE, 3/5, medium-high, and "complex" are not valid tier values.

Before you begin sizing, close the entry gate. Then work through each step in order.

---

## Phase 0: Entry Gate

You must verify two preconditions before any sizing begins.

**Precondition A — Inertia**: you can state a workaround (or named cost of absence) and a cost direction — **cheaper / comparable / more expensive** — for the feature.

**Precondition B — Signal boundary**: the feature description you have been given contains no plan-level artifacts — no task breakdowns, sprint assignments, owner names, or milestone dates. These belong in `program-plan`, not in sizing signal input.

**Your gate decision**:
- Both preconditions met → your gate = **OPEN** — proceed to Step 1
- Either fails → your gate = **CLOSED — Precondition [A / B]: [name what you found unmet]** — stop; do not produce sizing output

> **WRONG (Precondition A fails — your gate closes)**: "Teams manage this manually today." — You have not stated a cost direction. Your gate = CLOSED — Precondition A: cost direction absent.
> **WRONG (Precondition B fails — your gate closes)**: Your feature description contains "Sprint 1: implement API endpoint, owner: backend lead." — You have detected a plan-level artifact. Your gate = CLOSED — Precondition B: plan-level artifact detected ("Sprint 1: implement API endpoint, owner: backend lead").
> **CORRECT (both met — your gate opens)**: Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team." Signal boundary: you reviewed the feature description and found no sprint assignments or owner names.

| Precondition A: Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost [friction you observe today] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------------|--------------------------|
| | | | |

| Precondition B: Signal Boundary Review | Your Status |
|----------------------------------------|-------------|
| You have reviewed the feature description for plan-level artifacts (sprint assignments, owner names, milestone dates, task breakdowns) | CLEAR / BLOCKED — [name the artifact you found if BLOCKED] |

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

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — You have not named a factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| | |

---

### Step 3: Team-Size Signal

Name the specialist disciplines needed — headcount alone fails.

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

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
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

**Failure pattern — what you must avoid:**

> **WRONG** (basis-negation): Step 5 basis: "Auth API contract is stable." Gap: "Auth API contract has not been confirmed."
>
> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: your gap is derivable from your basis by direct negation — "X is stable" becomes "X is not confirmed"; you needed no new information to produce this gap
> **WHY IT FAILS**: a reader learns nothing from your gap that your Step 5 basis did not already imply; you have negated a confirmed item rather than discovered an open question

**Passing pattern — what you should aim for:**

> **CORRECT** (genuine gap): Step 5 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension the basis did not verify. Not derivable from Step 5 by negation.

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

State one condition per direction. Each condition must be falsifiable and name a tier destination different from your current tier.

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

## V-03 — Axis: Role sequence (Two-phase + Phase 0 two-precondition for C-36; three-field DIAGNOSTIC in Phase 2 WRONG for C-37; full C-20 cluster)

**Variation axis**: Role sequence — two-phase role separation (Phase 1: Sizing Analyst, Phase 2: Risk Assessor) retains the full C-20/C-23/C-24/C-25/C-26/C-27/C-29 cluster from R13 V-04; inertia framing — Phase 0 extended to two named preconditions (C-36: adds Precondition B signal boundary alongside Precondition A inertia); output format — Phase 2 gap checkpoint WRONG block promoted to three-field FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS format (C-37).

**Hypothesis**: R13 V-04 demonstrated the full role-separation cluster (C-35 + C-20 through C-29) but failed C-36 (inertia-only Phase 0) and C-37 (single-annotation DIAGNOSIS). R14 V-03 makes exactly two targeted additions: (a) Precondition B added to Phase 0, updating the CLOSED output format to identify which precondition failed; (b) the Phase 2 WRONG annotation promoted from single-label to three-field format. Hypothesis: targeted additions achieve C-36 + C-37 without restructuring the two-phase architecture, confirming that the role-separation cluster and the two new criteria are independently satisfiable.

---

You are running a **scout-size** sizing signal in three stages. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Stage sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 is OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## Phase 0: Entry Gate

**Charter**: Verify that sizing can begin. Two preconditions must both be satisfied before Phase 1 is permitted.

**Precondition A — Inertia**: a workaround or named cost of absence is stated with a cost direction (cheaper / comparable / more expensive).

**Precondition B — Signal boundary**: the feature description contains no plan-level artifacts — no sprint assignments, owner names, milestone dates, or task breakdowns.

**Gate logic**:
- Both preconditions met → Gate = **OPEN** — proceed to Phase 1
- Either fails → Gate = **CLOSED — Precondition [A / B]: [name unmet condition]** — stop; do not produce Phase 1 or Phase 2 output

> **WRONG (Precondition A fails)**: "Teams manage this manually today." — No cost direction. Gate = CLOSED — Precondition A: cost direction absent.
> **WRONG (Precondition B fails)**: Feature description contains "Sprint 1: implement API endpoint, owner: backend lead." — Gate = CLOSED — Precondition B: plan-level artifact detected ("Sprint 1: implement API endpoint, owner: backend lead").
> **CORRECT (both met — OPEN)**: Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team." Signal boundary: no plan-level artifacts found in feature description.

| Precondition A: Workaround [Phase 0 — name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver |
|-------------------------------------------------------------------------------|--------------|--------------------------------------------------------|------------|
| | | | |

| Precondition B: Signal Boundary Review | Status |
|----------------------------------------|--------|
| Feature description reviewed for sprint assignments, owner names, milestone dates, task breakdowns | CLEAR / BLOCKED — [name artifact if BLOCKED] |

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
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Your gap is a restatement of Phase 1 confirmed content in negative form. Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce — owned by Phase 0 / Phase 1]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Phase 2's primary output. Identify the primary source of residual uncertainty. Must address a different dimension than the P1-5 confidence basis.

**Failure pattern:**

> **WRONG** (basis-negation — Phase 2 charter violation): P1-5 basis: "Auth API contract is stable." Gap: "Auth API contract is unconfirmed."
>
> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; this is the violation the non-access clause prohibits

**Passing pattern:**

> **CORRECT** (genuine gap): P1-5 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

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

## V-04 — Axis: Lifecycle emphasis + inertia framing (Three-phase; Phase 0 expanded with per-precondition sections and gate decision checklist; C-37 three-field DIAGNOSTIC retained)

**Variation axis**: Lifecycle emphasis — Phase 0 is given expanded document space: a named section per precondition, each with its own WRONG failure example; a gate decision checklist table summarizing both preconditions before the gate output; a named "GATE DECISION:" label. Inertia framing — same two-precondition design as R13 V-05 (C-36), but Phase 0's per-precondition treatment is more prominent. Three-phase architecture throughout. C-37 three-field DIAGNOSTIC retained from R13 V-05.

**Hypothesis**: R13 V-05 achieves C-36 with a compact Phase 0: the two preconditions are stated in a brief charter, two WRONG examples cover both failure modes in one block, and the gate output format follows. R14 V-04 tests whether giving Phase 0 more lifecycle footprint — named sub-sections for each precondition, separate failure examples for each failure mode — produces better gate compliance without changing the three-phase analysis architecture that delivers the C-20 cluster. The downside hypothesis: expanded Phase 0 prose may crowd the prompt and reduce attention on Phase 1/Phase 2 analysis sections.

---

You are running a **scout-size** sizing signal in three phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 is OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## ── PHASE 0: ENTRY GATE ──

This phase determines whether sizing can begin. Two preconditions govern entry. Both must be met. Work through each before committing a gate decision.

---

### Precondition A: Inertia

Sizing must be grounded in the cost of NOT building. Before any sizing estimates can be produced, state a workaround (or named cost of absence) and a directional cost comparison.

**What Precondition A requires:**
- A named workaround (or "None: [named cost of absence]")
- A cost direction: **cheaper / comparable / more expensive**

**Example — Precondition A fails (gate closes on A):**

> Feature context: "Users would like a bulk-export button."
> Inertia field: "Users manage this manually."
> Result: CLOSED — Precondition A: cost direction absent. Sizing halted.

**Example — Precondition A passes:**

> Inertia: "Manual CSV export per team — building is **cheaper** long-term; overhead grows ~45 min/sprint/team." Cost direction present; key driver named.

| Precondition A: Workaround [Phase 0 — name it — or "None: [cost of absence]"] | Ongoing Cost | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|--------------------------------------------------------------------------------|--------------|--------------------------------------------------------|--------------------------|
| | | | |

---

### Precondition B: Signal Boundary

`scout-size` analyzes a feature description — not a project plan. If the input contains plan-level artifacts, the gate closes before sizing begins, because the input has already bypassed the signal boundary that this skill enforces.

**Plan-level artifacts that trigger CLOSED:**
- Sprint assignments: "Sprint 1: implement X"
- Owner names: "owner: [name or role]"
- Milestone dates: "target: Q3" or "ship by [date]"
- Task breakdowns: "Tasks: (1) design API (2) write tests"

**Example — Precondition B fails (gate closes on B):**

> Feature description contains: "Sprint 1: implement the notification API. Owner: backend lead. Sprint 2: build UI."
> Result: CLOSED — Precondition B: plan-level artifact detected ("Sprint 1: implement the notification API. Owner: backend lead.").

**Example — Precondition B passes:**

> Feature description: "Users need real-time notifications when order status changes." — No sprint assignments, owner names, milestone dates, or task breakdowns.

| Precondition B: Signal Boundary Review | Status |
|----------------------------------------|--------|
| Feature description reviewed for plan-level artifacts (sprint assignments, owner names, milestone dates, task breakdowns) | CLEAR / BLOCKED — [name artifact if BLOCKED] |

---

### Gate Decision

Both preconditions must pass to proceed.

| Precondition | Requirement | Result |
|-------------|-------------|--------|
| A — Inertia | Workaround + cost direction stated | MET / UNMET |
| B — Signal boundary | No plan-level artifacts in feature description | CLEAR / BLOCKED |

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

**Failure pattern:**

> **WRONG** (basis-negation — Phase 2 charter violation): P1-5 basis: "Auth API contract is stable." Gap: "Auth API contract is unconfirmed."
>
> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery
> **WHY IT FAILS**: the gap is derivable from P1-5 by negation with no new information; the Phase 2 charter exists precisely to prevent this substitution; this is the violation the non-access clause prohibits

**Passing pattern:**

> **CORRECT** (genuine gap): P1-5 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

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

## V-05 — Axis: Output format + role sequence (Three-phase; Phase 0 precondition table with REQUIREMENT / STATUS / CLOSED-LABEL columns; C-37 DIAGNOSTIC as named "── DIAGNOSTIC PATTERN ──" sub-section; C-32 gap standalone section; C-30 defense cluster)

**Variation axis**: Output format — Phase 0 uses a two-row precondition table with columns: Precondition | Requirement | Status [CLEAR/BLOCKED] | CLOSED Label [fill if BLOCKED]; this encodes C-36's per-precondition CLOSED identification as a schema-level column rather than prose instruction. Role sequence — three-phase (Phase 0: Entry Gate, Phase 1: Sizing Analyst, Phase 2: Risk Assessor) with full C-20 cluster. C-37 — WRONG block elevated to a named "── DIAGNOSTIC PATTERN ──" sub-section within the gap checkpoint, giving the three-field structure its own visual delimiter rather than embedding it inside a blockquote. C-32 — gap in standalone section. C-30 — all three enforcement mechanisms (label, self-test, WRONG/CORRECT) in the same gap section.

**Hypothesis**: R13 V-05 achieves C-36 via prose gate output format ("CLOSED — Precondition [A/B]: [condition]"). R14 V-05 encodes that same requirement as a table column — each precondition is a row, and the CLOSED-LABEL column structurally requires a per-precondition failure label if blocked, making C-36's identification visible at the schema level without requiring the reader to parse prose. C-37's three-field block is promoted from an annotated WRONG blockquote to a named visual sub-section with a delimiter, paralleling C-32's standalone gap section treatment. Hypothesis: schema-level encoding of C-36 (column header constraint) and section-level encoding of C-37 (named diagnostic sub-section) together push structural clarity to its maximum for both new criteria.

---

You are running a **scout-size** sizing signal in three phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. Phase 1 may not begin until Phase 0 Gate = OPEN. Phase 2 may not begin until Phase 1 is complete.

---

## Phase 0: Entry Gate

**Charter**: Verify two preconditions before sizing begins. Each precondition occupies a table row. A blocked row requires a CLOSED label naming the precondition and what was unmet.

| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED Label [fill only if BLOCKED — format: "CLOSED — Precondition [A/B]: [name what is missing or detected]"] |
|-------------|-------------|--------------------------|------------------------------------------------------------------------------------------------------------------|
| **A — Inertia** | Workaround (or named cost of absence) stated with cost direction: cheaper / comparable / more expensive | | |
| **B — Signal boundary** | Feature description contains no plan-level artifacts: no sprint assignments, owner names, milestone dates, or task breakdowns | | |

> **Example — A blocked**: Status: BLOCKED. CLOSED Label: "CLOSED — Precondition A: cost direction absent (workaround named but no cheaper/comparable/more-expensive judgment)."
> **Example — B blocked**: Status: BLOCKED. CLOSED Label: "CLOSED — Precondition B: plan-level artifact detected ('Sprint 1: implement notification API, owner: backend lead')."
> **Example — both CLEAR**: Gate = OPEN.

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

The following pattern names and diagnoses the most common failure for this field. Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):

P1-5 basis: "Auth API contract is stable."
Gap: "Auth API contract is unconfirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the Risk Assessor reversed a P1-5 confirmed item — "X is stable" → "X is not confirmed" — using negation as a substitute for genuine risk discovery; the gap requires no investigation to produce; a reader can derive it directly from the P1-5 confirmed set by negation alone
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
