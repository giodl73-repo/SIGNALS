Round 4 variations written to `simulations/quest/variations/discover-causal-variations-R4-2026-03-17.md`.

---

## Summary

**5 variations targeting v4 rubric gaps:**

| Variation | Axis | Primary Targets |
|-----------|------|-----------------|
| **V-01** | Phrasing Register — Formal Three-Branch Routing Tree | C-17 (three legal values with revision path as named branch, not implied stop) |
| **V-02** | Output Format — Effect Size Column in Mechanism Table | C-09 (effect size made structurally required; "unknown" alone disqualifies) |
| **V-03** | Inertia Framing — Inertia as Quantified Competitor | C-09 (comparison forces magnitude), C-16/C-18 (per-dimension delta) |
| **V-04** | Role Sequence + Lifecycle — Explicit Auditor Role | C-19 (Auditor's sole job is to name disqualifications and recount qualifying minimums) |
| **V-05** | Output Format + Phrasing Register + Inertia Framing | C-09, C-17, C-18, C-19 simultaneously — full structural enforcement |

**Key design decisions:**

- **C-09 gap (unsolved through R3):** V-02 attacks it directly via column enforcement. V-03 attacks it indirectly — comparison between Competitor 0 and Competitor X is meaningless without magnitudes, so quantification becomes natural. V-05 combines both angles.
- **C-17 upgrade:** V-01 uses a decision tree with routing arrows rather than a field with enumerated values — forces active branch selection, not passive field completion.
- **C-19 upgrade:** V-04 isolates the audit as a named role (The Auditor) so the disqualification requirement has a single, unambiguous owner. Prior variations embedded auditing as a style suggestion; this makes it a job.
evised and re-routed.
```

Record your selection:

```
INERTIA VERDICT:    [NO / PARTIAL / YES]
INERTIA REASONING:  [one sentence]
AUTHORIZED SCOPE:   [copy the exact branch label verbatim]
```

Do not begin Step 2 until this block is complete and a branch is selected. Branch C terminates the analysis.

---

**STEP 2 — MECHANISM TRACE**

Authorized by the Scope Routing Tree. Respect the Authorized Scope.

| Step | From | Mechanism Process (named — "causes" fails) | To | Disqualified? |
|------|------|--------------------------------------------|----|-|
| 1 | X | | M1 | [Yes if process unnamed — state reason] |
| 2 | M1 | | M2 | |
| 3 (if needed) | M2 | | Y | |

Requirements:
- Minimum two qualifying steps (X → M1 → M2 → Y)
- Each mechanism must name the process, not assert the link
- Branch B: marginal steps only — baseline steps do not count toward minimum
- A step with no named process is disqualified. Name it explicitly.

DISQUALIFIED STEPS: [list, or "none"]
QUALIFYING STEPS: [count — minimum 2 required]

---

**STEP 3 — FALSIFICATION CONDITIONS**

Produce at least two valid falsification conditions. All three columns required per row.

| # | WHAT (observable signal of failure) | HOW (measurement method) | WHEN TO OBSERVE (stage/window/protocol) | Valid? |
|---|-------------------------------------|--------------------------|----------------------------------------|--------|
| 1 | | | | [Yes / No — name missing field] |
| 2 | | | | |
| 3 (optional) | | | | |

A row with any empty cell is invalid and does not count toward the minimum. Name the missing field.

DISQUALIFIED ROWS: [list row numbers, or "none"]
QUALIFYING CONDITIONS: [count of valid rows — minimum 2 required]

---

**STEP 4 — EVIDENCE AND CONFOUNDERS**

```
SUPPORTING EVIDENCE: [one comparable case where this mechanism held, or "none found — first-principles claim"]

CONFOUNDER 1: [alternative explanation that produces Y without X, independent of inertia]
```

---

**STEP 5 — MARGINAL CONTRIBUTION** (required if INERTIA VERDICT was PARTIAL or YES; skip entirely if NO)

State what X contributes beyond baseline. Each axis occupies one labeled slot. Prose combining dimensions into one sentence is disqualified.

```
DIMENSION 1: [axis name] — [specific claim about X's contribution on this axis]
DIMENSION 2: [axis name] — [specific claim about X's contribution on this axis]
DIMENSION 3 (if applicable): [axis name] — [claim]

DISQUALIFIED DIMENSIONS: [list any prose entries that collapse multiple axes, or "none"]
QUALIFYING DIMENSIONS: [count — minimum 2 required]
```

---

**STEP 6 — SECTION COMPLIANCE**

Explicitly surface the completion status of each section.

| Section | Status | Gap (if any) |
|---------|--------|-------------|
| Scope Routing Tree | [Complete / Terminated at Branch C] | |
| Mechanism Trace | [N qualifying steps / Incomplete] | [name specific gap] |
| Falsification Conditions | [N qualifying rows / Incomplete] | |
| Evidence and Confounders | [Complete / Incomplete] | |
| Marginal Contribution | [Complete / N/A — inertia NO / Incomplete] | |

---

**AMEND**

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrowed, mechanism-specific, more falsifiable — must differ from original]
MECHANISM: [authorized chain — X → M1 → M2 → Y, one line, using process names from Step 2]
FALSIFIES IF: [most specific qualifying row from Step 3 — WHAT + HOW + WHEN TO OBSERVE]
MARGINAL CONTRIBUTION:
  DIMENSION 1: [axis] — [X's contribution]
  DIMENSION 2: [axis] — [X's contribution]
  (or: "Full effect — inertia NO, Branch A selected")
```

AMENDED must name the mechanism and be visibly narrower than ORIGINAL.

---

## V-02 — Axis: Output Format (Effect Size Column in Mechanism Table)

**Hypothesis:** Placing EFFECT SIZE as a required column in the causal chain table — with an explicit prompt for direction, magnitude, and confidence tier — forces C-09 by making quantification structurally required rather than stylistically optional. The column cannot be left blank without triggering disqualification; writing "unknown" requires a first-principles directional estimate.

---

You are running `/discover-causal`. Produce five structured artifacts in sequence.

**INPUT:** A hypothesis "X causes Y."

---

**ARTIFACT 1 — SCOPE DECLARATION**

```
INERTIA VERDICT:   [NO / PARTIAL / YES]
INERTIA REASONING: [one sentence — what mechanism produces Y at baseline, if any]
AUTHORIZED SCOPE:  [mark exactly one]
  [ ] "Full mechanism — Y does not occur without X. Full causal chain authorized."
  [ ] "Marginal contribution only — dimensions: [list]. X modifies baseline Y; trace the delta only."
  [ ] "Hypothesis requires revision before proceeding — defect: [name the specific defect]."
```

Mark exactly one. If "requires revision": state the defect and return a revised hypothesis. Do not begin Artifact 2 until hypothesis is corrected.

---

**ARTIFACT 2 — CAUSAL CHAIN TABLE**

Trace the causal pathway from X to Y through at least two qualifying intermediate steps.

| Step | From | Mechanism Process | To | Effect Size | Confidence |
|------|------|------------------|----|-------------|------------|
| 1 | X | [named process — what X does to produce M1] | M1 | [base rate or typical magnitude] | [Low / Medium / High] |
| 2 | M1 | [named process — what M1 does to produce M2] | M2 | [expected delta if X is present] | [Low / Medium / High] |
| 3 | M2 | [named process — what M2 does to produce Y] | Y | [net effect reaching Y] | [Low / Medium / High] |

**Column definitions:**
- **Mechanism Process:** name the causal mechanism. "Leads to" or "causes" does not qualify.
- **Effect Size:** rough quantification — percentage change, rate comparison, order of magnitude, or frequency. If unknown, write: "unknown — first-principles estimate: [direction + rough bound]." Leaving this field blank or writing only "unknown" is disqualifying.
- **Confidence:** Low = heuristic guess; Medium = analogous evidence exists; High = direct data supports it.

DISQUALIFIED STEPS: [list any rows missing Mechanism Process or Effect Size, or "none"]
QUALIFYING STEPS: [count — minimum 2 required]

---

**ARTIFACT 3 — FALSIFICATION CONDITIONS**

Minimum two valid rows. All four columns required per row.

| # | WHAT | HOW | WHEN TO OBSERVE | Valid? |
|---|------|-----|-----------------|--------|
| 1 | | | | [Yes / No — name missing field] |
| 2 | | | | |
| 3 (optional) | | | | |

DISQUALIFIED ROWS: [list row numbers with missing fields, or "none"]
QUALIFYING CONDITIONS: [count of Yes rows — minimum 2 required]

---

**ARTIFACT 4 — EVIDENCE AND CONFOUNDERS**

```
SUPPORTING EVIDENCE: [one comparable case where this mechanism held, or "none found — first-principles claim"]
EVIDENCE EFFECT SIZE: [if evidence cited, what magnitude did it show? Otherwise "no benchmark"]

CONFOUNDER 1: [alternative explanation for Y independent of X and inertia]
```

---

**ARTIFACT 5 — AMENDED HYPOTHESIS**

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrower, mechanism-specific, falsifiable — must differ from original]
MECHANISM: [Step 1 → Step 2 → Step 3 in one line, using process names from Artifact 2]
EFFECT SIZE: [net effect on Y from Artifact 2 — with confidence tier]
FALSIFIES IF: [most specific qualifying row from Artifact 3 — WHAT + HOW + WHEN]
MARGINAL CONTRIBUTION:
  DIMENSION 1: [axis name] — [what X adds over baseline on this axis]
  DIMENSION 2: [axis name] — [second axis, independently labeled]
  (omit this section entirely if INERTIA VERDICT was NO)
```

---

## V-03 — Axis: Inertia Framing (Inertia as Quantified Competitor)

**Hypothesis:** Framing inertia as "Competitor 0" and requiring its mechanism to be traced first — before X's mechanism — forces C-09 because the comparison between Competitor 0's mechanism and X's mechanism is meaningless without magnitudes. Quantification becomes natural rather than optional when the analysis is structurally built around a comparison between two competing mechanisms.

---

You are running `/discover-causal`. Your job is to determine whether X's causal mechanism beats the mechanism of doing nothing.

**THE STRUCTURE:** You have two competitors — Competitor 0 (inertia, the status quo) and Competitor X (the feature). Trace Competitor 0 first. Then trace Competitor X. Then decide what X actually contributes.

**INPUT:** A hypothesis "X causes Y."

---

**ROUND 0 — COMPETITOR 0: INERTIA**

Before evaluating X, trace the baseline mechanism. How does Y happen — or fail to happen — without X?

```
INERTIA MECHANISM:
  Does Y occur at baseline? [Yes / Partially / No]
  Step 1: [what force or process moves toward Y without X, if any]
  Step 2: [what sustains or limits that movement]
  Baseline Y Level: [fraction, rate, or magnitude of Y reached without X — rough estimate]

INERTIA VERDICT: [NO / PARTIAL / YES]
  NO:      Competitor 0 produces none of Y. X would own the full causal story.
  PARTIAL: Competitor 0 produces [fraction/level] of Y. X must compete for the delta.
  YES:     Competitor 0 produces all of Y. X's claim is not additional.
```

Competitor 0's mechanism and baseline level determine the scope for Competitor X.

---

**SCOPE DECLARATION**

Based on Competitor 0:

```
AUTHORIZED SCOPE: [select exactly one]
  - "Full mechanism — X traces the complete causal chain. Competitor 0 produces none of Y."     [INERTIA: NO]
  - "Marginal contribution only — dimensions: [list axes X affects beyond baseline]."            [INERTIA: PARTIAL]
  - "Hypothesis requires revision before proceeding — X does not add to Y beyond Competitor 0."  [INERTIA: YES]
    DEFECT: [specific statement of what is wrong]
    REVISED HYPOTHESIS: [form that can proceed to evaluation]
```

If AUTHORIZED SCOPE is "hypothesis requires revision," stop here.

---

**ROUND X — COMPETITOR X: THE FEATURE**

Trace X's mechanism. Respect the Authorized Scope.

```
X's MECHANISM:
  Step 1: [what X does immediately — named process, not assertion]
  Step 2: [how Step 1 propagates — named process]
  Step 3 (if needed): [how it reaches Y — named process]

EFFECT SIZE COMPARISON:
  Competitor 0 reaches Y at: [level from Round 0 — copy it]
  Competitor X reaches Y at: [estimated level]
  X's net addition:          [delta — quantify even if rough: %, rate, order of magnitude]
  Confidence:                [Low / Medium / High]

CONFOUNDER 1: [a third mechanism — not Competitor 0, not X — that could produce Y]
```

---

**FALSIFICATION CONDITIONS**

Name at least two conditions that would prove X's mechanism specifically fails (not Competitor 0's).

| # | WHAT | HOW | WHEN TO OBSERVE | Valid? |
|---|------|-----|-----------------|--------|
| 1 | | | | [Yes / No — name any missing field] |
| 2 | | | | |

DISQUALIFIED ROWS: [list, or "none"]
QUALIFYING CONDITIONS: [count — minimum 2 required]

---

**SUPPORTING EVIDENCE**

```
EVIDENCE: [comparable case where X's type of mechanism held in a similar context — cited. Or "none found."]
EVIDENCE EFFECT SIZE: [if evidence cited, what magnitude did it show?]
```

---

**AMEND**

```
ORIGINAL:    [original hypothesis]
AMENDED:     [narrowed, mechanism-specific, falsifiable]
MECHANISM:   [X → M1 → M2 → Y — one line using Round X process names]
EFFECT SIZE: [X's net addition from Round X comparison — with confidence tier]
FALSIFIES IF: [most specific qualifying condition — WHAT + HOW + WHEN TO OBSERVE]
MARGINAL CONTRIBUTION:
  DIMENSION 1: [axis name] — [X adds [delta] on [axis] beyond Competitor 0]
  DIMENSION 2: [axis name] — [second axis — independently labeled slot]
  (omit if INERTIA VERDICT was NO)
```

---

## V-04 — Axes: Role Sequence + Lifecycle Emphasis (Three Roles with Explicit Auditor)

**Hypothesis:** Adding a named Auditor role whose exclusive job is to inspect completed sections for missing required components, name disqualified entries, and recount qualifying minimums is the first design that structurally produces C-19 — because C-19 requires output-level self-audit, which no prior variation has made a role's explicit and sole responsibility.

---

You are running `/discover-causal`. Three analyst roles execute in sequence, then an Auditor reviews all deliverables. A role may not begin until prior deliverables are complete.

**INPUT:** A hypothesis "X causes Y."

---

**ROLE 1 — THE GATEKEEPER**

Job: determine the authorized scope of analysis before any mechanism work begins.

**Deliverable: SCOPE CERTIFICATE**

```
INERTIA VERDICT:   [NO / PARTIAL / YES]
INERTIA REASONING: [one sentence]
AUTHORIZED SCOPE:  [select exactly one]
  Option A: "Full mechanism — inertia NO. Full causal chain authorized."
  Option B: "Marginal contribution only — dimensions: [list]. Inertia PARTIAL; trace delta only."
  Option C: "Hypothesis requires revision before proceeding — defect: [name defect]."

ROUTING:
  Option A → Role 2 is authorized to trace the full mechanism.
  Option B → Role 2 is authorized to trace the marginal mechanism only.
  Option C → Role 2 does not begin. Gatekeeper returns a revised hypothesis.
```

REVISED HYPOTHESIS (Option C only): [amended form ready for re-routing]

---

**ROLE 2 — THE ARCHITECT**

Job: build the causal pathway authorized by the Scope Certificate.

**Deliverable: MECHANISM REPORT**

```
CAUSAL CHAIN:
  Step 1: X → [mechanism process name] → M1
  Step 2: M1 → [mechanism process name] → M2
  Step 3 (if needed): M2 → [mechanism process name] → Y

EFFECT SIZE ESTIMATE:
  Direction: [increases / decreases / accelerates / converts — choose one]
  Magnitude: [rough quantification — %, rate, order of magnitude, or frequency]
  Basis:     [what evidence or logic grounds this estimate]
  Confidence: [Low / Medium / High]
  Note: "unknown" without a directional bound is not acceptable. Write:
  "unknown — first-principles estimate: [direction + rough bound]" if no data exists.

CONFOUNDER 1: [alternative explanation for Y independent of X and inertia]
```

---

**ROLE 3 — THE OBSERVER**

Job: produce falsification conditions, evidence, and marginal contribution analysis.

**Deliverable: FALSIFICATION AND EVIDENCE REPORT**

**Falsification Conditions (minimum 2 valid rows):**

| # | WHAT | HOW | WHEN TO OBSERVE | Provisional Status |
|---|------|-----|-----------------|-------------------|
| 1 | | | | [Tentative — pending Auditor review] |
| 2 | | | | [Tentative — pending Auditor review] |
| 3 (optional) | | | | [Tentative — pending Auditor review] |

**Evidence:**
```
SUPPORTING EVIDENCE: [comparable case, or "none found — first-principles claim"]
```

**Marginal Contribution** (required if Scope Certificate was Option B):
```
DIMENSION 1: [axis name] — [claim about X's unique contribution on this axis]
DIMENSION 2: [axis name] — [claim about X's unique contribution on this axis]
DIMENSION 3 (if applicable): [axis name] — [claim]
```

---

**ROLE 4 — THE AUDITOR**

Job: inspect every structured entry from Roles 2 and 3 for missing required components. Disqualify and recount. Do not leave gaps unnamed.

**Deliverable: AUDIT REPORT**

```
MECHANISM STEPS AUDIT:
  Step 1: [Qualified / Disqualified — reason if disqualified: no named process / no content]
  Step 2: [Qualified / Disqualified — reason]
  Step 3: [Qualified / Disqualified / N/A]
  QUALIFYING STEPS: [count — minimum 2 required; flag if minimum is not met]

EFFECT SIZE AUDIT:
  [Quantified with magnitude / Directional estimate only / "Unknown" without bound — disqualified]

FALSIFICATION CONDITIONS AUDIT:
  Row 1: [Qualified / Disqualified — name any missing field: WHAT / HOW / WHEN TO OBSERVE]
  Row 2: [Qualified / Disqualified — name any missing field]
  Row 3: [Qualified / Disqualified / N/A]
  QUALIFYING CONDITIONS: [count — minimum 2 required; flag if minimum is not met]

MARGINAL CONTRIBUTION AUDIT:
  Dimension 1: [Qualified / Disqualified: prose combining dimensions / N/A]
  Dimension 2: [Qualified / Disqualified / N/A]
  Note: a sentence containing two dimension names is Disqualified for both — each must be its own labeled slot.
  QUALIFYING DIMENSIONS: [count — minimum 2 required if Option B; flag if minimum is not met]

SECTION COMPLIANCE SUMMARY:
  Scope Certificate:        [Complete / Terminated at Option C]
  Mechanism Report:         [Complete — N qualifying steps / Incomplete — gap: ...]
  Falsification Report:     [Complete — N qualifying conditions / Incomplete — gap: ...]
  Evidence:                 [Present / Explicit absence stated / Missing]
  Marginal Contribution:    [Complete — N qualifying dimensions / N/A / Incomplete — gap: ...]
  Effect Size:              [Quantified / Estimated with bound / Absent or "unknown" only]
```

---

**SYNTHESIS — AMEND BLOCK**

After all four deliverables are complete:

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrowed, mechanism-specific, falsifiable — must differ from original]
MECHANISM: [authorized chain from Architect's report — one line using process names]
EFFECT SIZE: [from Architect's estimate, with Auditor's qualification status noted]
FALSIFIES IF: [most specific qualifying condition from Auditor's recount — WHAT + HOW + WHEN]
MARGINAL CONTRIBUTION:
  DIMENSION 1: [axis] — [claim]
  DIMENSION 2: [axis] — [claim]
  (or: "Full effect — Scope Certificate was Option A")
```

AMENDED must be visibly more specific and falsifiable than ORIGINAL. An amended hypothesis that could have been written before the analysis fails.

---

## V-05 — Axes: Output Format + Phrasing Register + Inertia Framing (Full Structural Enforcement)

**Hypothesis:** Combining a formal three-branch routing tree (C-17), labeled independent dimension slots (C-18), explicit row-disqualification with recounting (C-19), an effect size column in the mechanism table (C-09), and inertia-as-competitor framing produces the highest total v4 rubric coverage possible in a single prompt — because each of the four persistent structural gaps is targeted from a distinct angle within one coherent architecture.

---

You are running `/discover-causal`. This skill produces five artifacts. Every structured entry has required components. Missing components are explicitly disqualified and not counted toward minimums.

**INPUT:** A hypothesis "X causes Y."

---

**ARTIFACT 1 — INERTIA AND SCOPE**

Start by tracing the baseline. What does the status quo produce without X?

```
BASELINE MECHANISM:
  Does Y occur without X? [Yes / Partially / No]
  How: [one sentence — what process moves toward Y at baseline, if any]
  Baseline Y Level: [rough estimate — %, rate, "none", "most", or comparable measure]

INERTIA VERDICT: [NO / PARTIAL / YES]

SCOPE ROUTING — select exactly one branch:

  BRANCH A — Inertia: NO
    Baseline produces none of Y. X owns the complete causal story.
    AUTHORIZED SCOPE: "Full mechanism — X traces the complete chain to Y."
    → Proceed to Artifact 2 (full mechanism authorized).

  BRANCH B — Inertia: PARTIAL
    Baseline produces [level] of Y. X must justify its marginal contribution.
    AUTHORIZED SCOPE: "Marginal contribution only — dimensions: [list axes X affects beyond baseline]."
    → Proceed to Artifact 2 (marginal steps only — baseline steps are context, not qualifying).

  BRANCH C — Inertia: YES
    Baseline produces all of Y. X's claim is not additional as stated.
    AUTHORIZED SCOPE: "Hypothesis requires revision before proceeding."
    DEFECT: [specific statement of what is wrong with the hypothesis]
    REVISED HYPOTHESIS: [amended form that routes correctly on re-evaluation]
    → Stop. Do not proceed to Artifact 2 until hypothesis is re-submitted and re-routed.

SELECTED BRANCH: [A / B / C]
AUTHORIZED SCOPE: [copy the exact scope statement from the selected branch]
```

---

**ARTIFACT 2 — CAUSAL CHAIN WITH EFFECT SIZE**

Trace the mechanism authorized in Artifact 1. Every row requires all five columns.

| Step | From | Mechanism Process (named — "causes" / "leads to" fails) | To | Effect Size | Confidence |
|------|------|----------------------------------------------------------|----|-------------|------------|
| 1 | X | | M1 | [base rate or delta — rough quantification] | [Low/Med/High] |
| 2 | M1 | | M2 | [expected change at this step] | [Low/Med/High] |
| 3 | M2 | | Y | [net effect reaching Y] | [Low/Med/High] |

**Disqualification rules applied per row:**
- Unnamed Mechanism Process → Disqualified. Mark: "DISQUALIFIED — mechanism not named."
- Empty Effect Size → Disqualified unless written as: "unknown — first-principles estimate: [direction + rough bound]"
- Branch B: baseline-only steps (before X's marginal action begins) are context and do not count toward minimum

DISQUALIFIED STEPS: [list any with reason — or "none"]
QUALIFYING STEPS: [count after disqualifications — minimum 2 required]

---

**ARTIFACT 3 — FALSIFICATION CONDITIONS**

Produce at least two valid rows. All four columns required per row.

| # | WHAT (observable signal of mechanism failure) | HOW (measurement or detection method) | WHEN TO OBSERVE (stage, window, or test protocol) | Valid? |
|---|-----------------------------------------------|---------------------------------------|---------------------------------------------------|--------|
| 1 | | | | [Yes / No — name missing field] |
| 2 | | | | |
| 3 (optional) | | | | |

**Row validity rule:** any empty cell disqualifies the row. The row is not counted toward the minimum and must be named as non-qualifying.

DISQUALIFIED ROWS: [list row numbers with reason — name each missing field — or "none"]
QUALIFYING CONDITIONS: [count after disqualifications — minimum 2 required]

---

**ARTIFACT 4 — EVIDENCE, CONFOUNDERS, AND MARGINAL CONTRIBUTION**

```
SUPPORTING EVIDENCE: [one comparable case where this mechanism held, or "none found — first-principles claim"]
EVIDENCE EFFECT SIZE: [magnitude implied by cited evidence — or "not applicable"]

CONFOUNDER 1: [mechanism that produces Y without X and without inertia — a third explanation]

MARGINAL CONTRIBUTION (required if Branch B or C; omit entirely if Branch A):
  DIMENSION 1: [axis name] — [specific claim: X adds [what] on this axis beyond the baseline]
  DIMENSION 2: [axis name] — [specific claim: X adds [what] on this axis beyond the baseline]
  DIMENSION 3 (if applicable): [axis name] — [claim]

  Disqualification rule: prose combining multiple axes into one sentence is disqualified for each
  axis it claims to cover. Each dimension must occupy its own independently verifiable labeled slot.

  DISQUALIFIED DIMENSIONS: [list any with reason — or "none"]
  QUALIFYING DIMENSIONS: [count after disqualifications — minimum 2 required if Branch B or C]
```

---

**ARTIFACT 5 — SECTION COMPLIANCE AND AMENDED HYPOTHESIS**

**Compliance Check:**

| Section | Status | Gap or Disqualification |
|---------|--------|------------------------|
| Artifact 1 — Scope Routing | [Complete — Branch selected / Terminated at Branch C] | |
| Artifact 2 — Mechanism Chain | [N qualifying steps / Incomplete] | [name gap] |
| Artifact 2 — Effect Size | [Quantified / First-principles estimate / Absent] | |
| Artifact 3 — Falsification | [N qualifying conditions / Incomplete] | |
| Artifact 4 — Evidence | [Cited / Explicit absence / Missing] | |
| Artifact 4 — Marginal Contribution | [N qualifying dimensions / N/A Branch A / Incomplete] | |

**Amended Hypothesis:**

```
ORIGINAL:    [original hypothesis]
AMENDED:     [narrowed, mechanism-specific, more falsifiable — must differ from original]
MECHANISM:   [Artifact 2 chain — X → M1 → M2 → Y, one line, using process names]
EFFECT SIZE: [net effect on Y — from Artifact 2, with confidence tier]
FALSIFIES IF: [most specific qualifying row from Artifact 3 — WHAT + HOW + WHEN TO OBSERVE]
MARGINAL CONTRIBUTION:
  DIMENSION 1: [axis] — [claim from Artifact 4]
  DIMENSION 2: [axis] — [claim from Artifact 4]
  (or: "Full effect — Branch A, inertia NO")

AMEND VALIDITY CHECK:
  [ ] AMENDED is narrower than ORIGINAL
  [ ] AMENDED names the mechanism, not just the outcome
  [ ] AMENDED includes a falsification condition
  [ ] MARGINAL CONTRIBUTION covers all qualifying dimensions from Artifact 4
```
