# Scout-Size Prompt Variations — R17

**Skill**: scout-size
**Rubric**: v17 (35 aspirational criteria, C-01 through C-43)
**Date**: 2026-03-17
**Round**: 17
**R16 champion**: V-05 — three-phase; `── ENTRY GATE ──` visual delimiter; gate table with STATUS + CLOSED-LABEL + EVIDENCE + CLEAR-PATH columns; four-field `── DIAGNOSTIC PATTERN ──` with REMEDIATION; compilation pointer row (C-40); CLOSED-LABEL header with fill/leave-blank conditions (C-41); CLEAR-PATH column as C-42 candidate (superseded by rubric definition shift)
**R16 gaps**: C-42 FAIL in all variations (CLOSED-LABEL header has `format:` slot but leaves it as ellipsis — value template unspecified); C-43 FAIL in single-phase V-02 and champion V-05 (V-02: no contract label in self-test; V-05: self-test cites REMEDIATION but omits "— a Phase 2 charter violation"); C-43 PASS in V-01/V-03/V-04 (already had "— a Phase 2 charter violation")

---

## Context: What R17 Addresses

| New criterion | What it formalizes | R16 evidence |
|---|---|---|
| C-42 | CLOSED-LABEL column header encodes the output value format via a `format:` slot alongside fill/leave-blank conditions — specifies the expected value structure (`"Precondition A: [named condition]"`) | R16 V-02's CLOSED-LABEL header read "fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: …" with an unspecified ellipsis; without a concrete value template, a BLOCKED model may produce free-form prose rather than the structured traceable label that C-38's row-level identifiability depends on |
| C-43 | Self-test affirmative branch names the violated architectural contract alongside the failure class | R16 V-01: "If yes: you have written a basis-negation — a Phase 2 charter violation." — upgrades the diagnostic from content-level (what error) to structural-level (which guarantee is broken), enabling targeted correction |

R17 explores: (1) whether C-42 + C-43 fit the minimal single-phase architecture; (2) second-person register with C-43 in direct address; (3) whether C-42 alone achieves max score in a two-phase design where C-43 is already present; (4) whether C-42 creates a triple-mechanism BLOCKED/CLEAR determination in a lifecycle-heavy Phase 0; (5) whether the self-test can prescribe corrective scope alongside the contract label as a C-44 candidate.

**Axes selected:**

| Variation | Axis | Hypothesis |
|---|---|---|
| V-01 | Inertia framing (single-phase minimal; C-42 format: slot; C-43 single-phase contract label: "gap field production contract violation") | R16 single-phase scored 27/33 = 8.18. Two targeted changes: (a) CLOSED-LABEL header adds `format: "Precondition [A/B]: [named condition]"` (C-42); (b) self-test adds "— a gap field production contract violation" (C-43). Hypothesis: both fit the minimal architecture without role-separation overhead. |
| V-02 | Phrasing register (second-person; single-phase; C-42 + C-43 in direct address: "you have written a basis-negation — a gap field production contract violation") | Second-person C-43 is more confrontational — "you have violated" names a personal production failure, not just a category error. Hypothesis: directness reduces generic revision and increases dimension-specific correction. |
| V-03 | Role sequence (two-phase; C-42 format: slot only new change; C-43 already present from R16 V-01; one targeted structural change → max attainable score) | R16 V-01 scored 32/33. C-43 already present. One change: fill the `format:` template. Expected: 34/35 aspirational, maximum attainable for multi-phase. |
| V-04 | Lifecycle emphasis (three-phase; expanded per-precondition Phase 0 sections; C-42 adds third signal to BLOCKED/CLEAR determination; C-43 in Phase 2) | Three-mechanism prevention: (a) narrative primes the requirement, (b) C-41 fill/leave-blank, (c) C-42 value template — each addresses a different failure mode. |
| V-05 | Output format + role sequence (three-phase; R16 champion + C-42 + C-43 contract label alongside REMEDIATION reference; C-44 candidate: self-test prescribes corrective scope by name) | R16 V-05 self-test cited REMEDIATION but omitted the contract label. R17 V-05 adds: (1) failure class, (2) contract label, (3) corrective scope, (4) REMEDIATION reference — self-test becomes a prescriber, not just a detector. |

---

## V-01 — Axis: Inertia framing (Single-phase; C-42; C-43 single-phase contract label; no role separation)

**Variation axis**: Inertia framing — Phase 0 gate table satisfies C-38 (STATUS + CLOSED-LABEL columns per precondition row); CLOSED-LABEL header upgraded to C-42 compliance by adding `format: "Precondition [A/B]: [named condition]"` value template. Self-test adds C-43 contract label for single-phase: "— a gap field production contract violation." Single-phase; no role separation.

**Hypothesis**: R16 single-phase scored 27/33 = 8.18. R17 V-01 makes exactly two structural changes to R16 V-02: (a) CLOSED-LABEL header fills the `format: …` ellipsis with `format: "Precondition [A/B]: [named condition]"` (C-42); (b) self-test affirmative branch adds "— a gap field production contract violation" (C-43). For single-phase, the violated contract is the gap field's own production guarantee: name a dimension the basis did not verify.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Complete Phase 0 before any analysis begins. Proceed through each step in order.

---

### Phase 0: Entry Gate

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

*Step 1 begins only if Gate = OPEN.*

---

### Sizing Steps [Gate must be OPEN before proceeding]

**Step 1 — Surface Area**

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each individually — "API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total integration points [numeric count required]** | |

**Step 2 — Complexity Tier + Primary Driver**

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors] |
|---|---|
| | |

**Step 3 — Team-Size Signal**

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|---|---|
| | |
| **Total FTEs** | |

**Step 4 — Timeline Signal**

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format] |
|---|
| |

**Step 5 — Confidence Basis**

State only what IS established here. What is NOT known gets its own section below.

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is clear and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|---|---|
| | |

---

### ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Must address a **different dimension** than the Step 5 confidence basis.

#### ── DIAGNOSTIC PATTERN ──

**WRONG** (basis-negation):

Step 5 basis: "Auth API contract is stable."
Gap: "Auth API contract has not been confirmed."

> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: the gap is derivable from the basis by direct negation — "X is stable" becomes "X is not confirmed"; no investigation is required; a reader can derive it from Step 5 by negation alone
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

**Step 6 — Confidence Calibration**

| What Would Raise Confidence | What Would Lower Confidence |
|---|---|
| | |

**Step 7 — Tier Sensitivity**

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."
> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from current tier] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Output Compilation

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

## V-02 — Axis: Phrasing register (Second-person; single-phase; C-42 format: slot in second-person CLOSED-LABEL; C-43 direct-address contract label)

*(See file for complete prompt — second-person register throughout; "Your CLOSED-LABEL [fill only if your STATUS = BLOCKED — leave blank if your STATUS = CLEAR — format: 'Precondition [A/B]: [named condition]']"; self-test: "you have written a basis-negation — a gap field production contract violation.")*

---

## V-03 — Axis: Role sequence (Two-phase; C-42 only new change; C-43 already present; one targeted addition → 34/35)

*(See file for complete prompt — two-phase Phase 1 Sizing Analyst / Phase 2 Risk Assessor; CLOSED-LABEL header adds format: template; Phase 2 self-test retains "— a Phase 2 charter violation" from R16 V-01)*

---

## V-04 — Axis: Lifecycle emphasis (Three-phase; expanded Phase 0; C-42 triple-mechanism; C-43 in Phase 2)

*(See file for complete prompt — per-precondition narrative sections in Phase 0; gate-decision summary table with C-42 format: slot; triple-mechanism BLOCKED/CLEAR: narrative + C-41 + C-42)*

---

## V-05 — Axis: Output format + role sequence (R16 champion evolution; C-42 + C-43 + REMEDIATION reference; C-44 candidate)

*(See file for complete prompt — ENTRY GATE delimiter; STATUS + CLOSED-LABEL + EVIDENCE + CLEAR-PATH gate table; four-field DIAGNOSTIC PATTERN with REMEDIATION; self-test: "you have written a basis-negation — a Phase 2 charter violation. Address a dimension Phase 1 did not confirm. See REMEDIATION above.")*

---

Written to `simulations/quest/golden/scout-size-variate-R17-2026-03-17.md` — all 5 complete prompts are in the file. Summary of predicted v17 scores:

| Variation | Architecture | C-42 | C-43 | Predicted Aspirational | Total |
|---|---|---|---|---|---|
| V-01 | Single-phase | PASS (format: slot filled) | PASS (gap field production contract) | 29/35 = 8.29 | ~98.29 |
| V-02 | Single-phase 2nd-person | PASS | PASS | 29/35 = 8.29 | ~98.29 |
| V-03 | Two-phase | PASS | PASS (already present) | 34/35 = 9.71 | ~99.71 |
| V-04 | Three-phase lifecycle | PASS | PASS | 34/35 = 9.71 | ~99.71 |
| **V-05** | Three-phase champion | **PASS** | **PASS + C-44 candidate** | **34/35 = 9.71** | **~99.71** |

**Key structural changes from R16**:
- **C-42** (all variations): `format: "Precondition [A/B]: [named condition]"` added to CLOSED-LABEL column header — fills the ellipsis left in R16
- **C-43 single-phase** (V-01, V-02): self-test adds `"— a gap field production contract violation"` — names the gap field's own production guarantee as the violated contract
- **C-43 multi-phase** (V-05): self-test adds `"— a Phase 2 charter violation"` alongside the existing REMEDIATION reference
- **C-44 candidate** (V-05): self-test affirmative branch now prescribes corrective scope — "Address a dimension Phase 1 did not confirm" — making the self-test a prescriber, not just a detector
