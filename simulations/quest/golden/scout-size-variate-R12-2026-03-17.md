# Scout-Size Prompt Variations — R12

**Skill**: scout-size
**Rubric**: v12 (25 aspirational criteria, C-01 through C-33)
**Date**: 2026-03-17
**Round**: 12
**R11 champion**: V-02 (~TBD) — standalone gap checkpoint (`── CONFIDENCE GAP CHECKPOINT ──`) satisfies C-32 evidence; "I have written a basis-negation" satisfies C-33 evidence
**R11 gaps**: C-19 PARTIAL (gap section achieves pre-slot, but some step fields still post-row); C-20/C-23/C-24/C-25/C-26/C-27/C-29 FAIL (no role separation in V-01 through V-03)

---

## Context: What R12 Addresses

v12 adds two new aspirational criteria extracted from R11 V-02's excellence signals:

| New criterion | What it formalizes | R11 evidence |
|---------------|-------------------|--------------|
| C-32 | The confidence gap is **removed from the output table** and placed in a dedicated named section with a visual delimiter (`── CONFIDENCE GAP CHECKPOINT ──`), positioned between the confidence basis and the sensitivity section. C-31 compensates for in-table gaps; C-32 eliminates the problem architecturally. | R11 V-02's standalone checkpoint section — the first design to extract the gap from the table entirely |
| C-33 | The self-test's affirmative branch must **name the failure class** — e.g., "If yes, you have written a basis-negation" — not only issue a correction directive. Naming the failure class enables pattern-level correction rather than retry-level correction. | R11 V-02's "If yes, I have written a basis-negation, not a gap" — the phrase names the failure class rather than saying "If yes, restate." |

R11 V-02 already satisfies both evidence precursors. The rubric formalizes what V-02 demonstrated. R12 variations explore:

1. Whether pre-slot placement throughout (C-19) can be achieved simultaneously with C-32 and C-33 in a single-phase design
2. Whether C-33's failure-class label can be structurally elevated — from inline prose to a dedicated `DIAGNOSIS:` block — without losing the C-30 defense cluster convergence
3. Whether second-person diagnostic register ("you are in a basis-negation pattern") produces different generation-time behavior than first-person ("I have written a basis-negation")
4. Whether two-phase role separation can gain C-20/C-23/C-24/C-25/C-26/C-27/C-29 while co-locating C-32 + C-33 in Phase 2's standalone gap section
5. Whether three-phase design with inertia as Phase 0 gate achieves clean ownership boundaries that reinforce C-32 + C-33 without introducing overhead that undermines earlier guarantees

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format (pre-slot placement throughout + C-32 standalone gap + C-33 named failure class) | R11 V-01 achieved pre-slot for Steps 1–9 but had the gap as a table row in the output compilation. R12 V-01 removes the gap from the compilation table (C-32) and adds the failure-class label "you have written a basis-negation" to the checkpoint self-test (C-33). Compilation table footnotes reference the standalone section. This should achieve C-19 + C-32 + C-33 simultaneously in a single-phase design with no role-separation overhead. |
| V-02 | Lifecycle emphasis (gap checkpoint as structured diagnostic station with named DIAGNOSIS block for C-33) | R11 V-02's C-33 evidence embedded "basis-negation" inline in the self-test prose. V-02 for R12 promotes the failure-class label to a dedicated `DIAGNOSIS:` sub-block within the checkpoint — a structural elevation that makes the failure class visible at the document-structure level. The hypothesis: a labeled DIAGNOSIS block produces stronger pattern-recognition priming than an inline clause because the model encounters the failure-class label as a section event, not as a conditional subordinate clause. |
| V-03 | Phrasing register (second-person imperative throughout; C-33 failure class in second-person diagnostic address) | R11 V-02 uses first-person self-test framing ("Ask — if I reversed... would I get my gap? If yes, I have written a basis-negation"). V-03 uses second-person: "If yes: you are in a basis-negation pattern." The shift from first-person introspection to second-person diagnosis tests whether addressed-voice register changes generation-time engagement with the constraint. Second-person makes the diagnosis external and observable; first-person makes it self-reflective. |
| V-04 | Role sequence + lifecycle emphasis (two-phase; C-32 standalone gap as Phase 2 primary output; C-33 in Phase 2 charter self-test) | Single-phase designs cannot satisfy C-20/C-23/C-24/C-25/C-26/C-27/C-29 (7 role-separation criteria). Two-phase design gains all seven. Phase 2 owns the gap checkpoint section (C-32) — the standalone section IS Phase 2's primary production. Phase 2 charter embeds the C-33 failure-class label in the non-access clause self-test. Role-tagged compilation table achieves C-26. This tests whether the full role-separation cluster can coexist with C-32 + C-33 without charter overhead crowding out the defense mechanisms. |
| V-05 | Inertia framing + output format + role sequence (three-phase; Phase 0 inertia gate; maximum structural encoding; C-32 + C-33 in Phase 2) | Demoting inertia to a section allows sizing to proceed before the cost-of-not-building is established. Phase 0 as a named gate closes this gap architecturally. Three-phase design (Phase 0: Inertia Assessor, Phase 1: Sizing Analyst, Phase 2: Risk Assessor) adds explicit phase-gate language and role-tagged column headers throughout (C-26). C-32 and C-33 live in Phase 2's standalone gap section. Tests whether three-phase structural overhead amplifies the enforcement guarantees of C-32 + C-33 through clean phase isolation, or whether it introduces friction that degrades earlier-gained criteria. |

---

## V-01 — Axis: Output format (Pre-slot examples throughout + C-32 standalone gap + C-33 failure-class label)

**Variation axis**: Output format — WRONG/CORRECT examples precede every output slot; gap extracted from compilation table into standalone section (C-32); self-test affirmative branch names the failure class (C-33)

**Hypothesis**: R11 V-01 applied pre-slot examples to all production steps but the output compilation table still included a "Confidence Gap" row — making C-32 fail because the gap appeared as a table cell. R12 V-01 removes the gap row from the compilation table and references the standalone checkpoint section instead. C-33 adds the failure-class label "you have written a basis-negation" to the self-test's affirmative branch. These are mechanical changes that should achieve C-19 + C-32 + C-33 without altering the single-phase structure that made R11 V-01 the candidate champion.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail.

Work through the following steps in order. Complete each step before moving to the next.

---

### Step 1: Inertia Check

The cost of building must be compared against the cost of NOT building before sizing begins.

> **WRONG**: "Teams currently use spreadsheets." — Workaround named; cost direction absent. Fails.
> **CORRECT**: "Manual CSV export + re-import per team — building is **cheaper** long-term; workaround overhead grows linearly with team count (~45 min/sprint/team)."

Name the current workaround and state a cost direction: **cheaper / comparable / more expensive**.

| Field | Value |
|-------|-------|
| Current Workaround | [name it — or "None: [cost of absence]"] |
| Ongoing Cost | [describe friction absorbed today] |
| Cost Direction [cheaper / comparable / more expensive] | |
| Key Driver | [one sentence] |

---

### Step 2: Surface Area

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each individually — "API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|---------------------------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total integration points [numeric count required]** | |

---

### Step 3: Complexity Tier + Primary Driver

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| | |

---

### Step 4: Team-Size Signal

> **WRONG**: "2–3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|----------------------------------------------------------------|--------------|
| | |
| | |
| **Total FTEs** | |

---

### Step 5: Timeline Signal

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a calendar date, not a single number] |
|-----------------------------------------------------------------------|
| |

---

### Step 6: Confidence Basis

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable; webhook delivery semantics under concurrent load have not been spiked."

State only what IS established here. What is NOT known gets its own section next.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include unknowns] |
|----------------------------------------|-----------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

This section identifies the primary source of residual uncertainty. It must address a **different dimension** than the confidence basis in Step 6.

**What a failing gap looks like:**

> **WRONG** (basis-negation): Step 6 basis says "Auth API contract is stable." Gap says "Auth API contract has not been confirmed."
> Why it fails: same dimension, reversed polarity. A reader can derive this gap from Step 6 by negation alone — no new information required.

**What a passing gap looks like:**

> **CORRECT** (genuine gap): Step 6 basis says "Auth API contract is stable." Gap says "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension the basis did not reach. Not derivable by negating Step 6.

**Self-test — run before writing your gap:**

> Ask: if I reversed something from my Step 6 basis ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation.** Restate to name a dimension the basis did not address.
> If no: proceed.

**Your Confidence Gap** [must address a dimension not covered by the Step 6 basis — not a negation of it]:

Gap: _____

---

### Step 7: Confidence Calibration

| What Would Raise Confidence | What Would Lower Confidence |
|-----------------------------|-----------------------------|
| | |

---

### Step 8: Tier Sensitivity

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable; "scope grows" is a deferral. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with the PM."

> **WRONG tier-down**: "Tier drops to MEDIUM if integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what investigation settles it] | Destination Tier [must differ from current tier — fill with LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Output Compilation

After completing all steps, compile the final signal:

**SIZING SIGNAL — [feature name]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Inertia Check | [workaround — cost direction — one sentence] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

_Confidence Gap is documented in the ── CONFIDENCE GAP CHECKPOINT ── section above._

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

---

---

## V-02 — Axis: Lifecycle emphasis (Gap checkpoint as diagnostic station with named DIAGNOSIS block)

**Variation axis**: Lifecycle emphasis — the confidence gap checkpoint includes a dedicated `DIAGNOSIS:` sub-block that names the failure class as a structural element rather than an inline conditional clause

**Hypothesis**: R11 V-02 embedded "I have written a basis-negation" inside a self-check sentence — the failure-class label was present but functioned as a clause subordinate to the conditional ("If yes, I have written..."). V-02 for R12 promotes the failure class to a dedicated `DIAGNOSIS:` label on its own line within the checkpoint, making the failure class visible as a document-structure event rather than as a subordinate clause. The hypothesis: a labeled `DIAGNOSIS:` block provides stronger generation-time pattern priming — the model encounters the named failure class as a section heading before it produces the gap field, not as a conditional it evaluates after the fact. C-32 is satisfied by the standalone section. C-33 is satisfied by the explicit `DIAGNOSIS:` block naming `basis-negation`. C-30 is preserved because all three defense mechanisms (section-header constraint, self-test, WRONG/CORRECT) remain within the same checkpoint section.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

Complete each section in order.

---

### Section 1: Inertia Check

Compare building against NOT building before sizing begins.

> **WRONG**: "Users manage this with a spreadsheet today." — No cost direction. Fails.
> **CORRECT**: "Manual CSV upload per team — building is **cheaper** long-term; overhead grows with team count (~45 min/sprint/team)."

| Workaround [name it — or "No workaround: [cost of absence]"] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|--------------------------------------------------------------|-------------------------------------------------------|--------------------------|
| | | |

---

### Section 2: Surface Area

> **WRONG**: "API and database integrations." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (user-created), DB migration (users table) — **3 integration points**"

| Integration Point [name individually — general descriptions fail] | Type |
|------------------------------------------------------------------|------|
| | |
| | |
| **Total** | **[N] integration points** |

---

### Section 3: Complexity Tier + Driver

> **WRONG tier**: "MODERATE" or "3/5" — Off-vocabulary. Fails.
> **WRONG driver**: "It has a lot of moving pieces." — Not a named factor. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service event ordering — three consumers must process in causal sequence without broker-level ordering guarantee."

| Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------|------------------------------------------------------------------|
| | |

---

### Section 4: Team-Size Signal

> **WRONG**: "3 engineers" — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM"

| Specialist Discipline | FTE |
|-----------------------|-----|
| | |
| **Total** | |

---

### Section 5: Timeline Signal

> **WRONG**: "6 weeks" / "4 sprints" — Calendar unit; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a date, not a single number] |
|-------------------------------------------------------------|
| |

---

### Section 6: Confidence Basis

State confidence and name what IS established. Do not include unknowns here — those get their own checkpoint next.

> **WRONG**: "MEDIUM confidence." — No basis. Fails.
> **CORRECT**: "MEDIUM — integration points are enumerated and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include what is unknown] |
|----------------------------------------|-----------------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

**Purpose**: Identify the primary source of residual uncertainty in this sizing. Must address a dimension the Section 6 basis does not reach.

**Failure pattern — DIAGNOSIS: basis-negation**

> **WRONG**: Section 6 basis: "Auth API contract is stable." Gap: "Auth API contract is unconfirmed."
> **DIAGNOSIS: basis-negation.** The gap is produced by reversing a confirmed item from the basis ("X is stable" → "X is not confirmed"). A reader needs no new information — they derive the gap from Section 6 by negation alone. A basis-negation is a restatement, not a gap. It tells the reader nothing that the basis did not already imply.

**Passing pattern — genuine gap**

> **CORRECT**: Section 6 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension the basis did not verify. A reader cannot derive it from Section 6 by negation or inference.

**Self-test — run before writing your gap:**

> Ask: if I negated a statement from my Section 6 basis ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes → DIAGNOSIS: basis-negation detected.** Your gap is a restatement. Restate to name a dimension the basis did not address.
> **If no → proceed.**

**Your Confidence Gap** [must address a dimension not reached by the Section 6 basis — not a negation of it]:

Gap: _____

---

### Section 7: Confidence Calibration

| What Would Raise Confidence | What Would Lower Confidence |
|-----------------------------|-----------------------------|
| | |

---

### Section 8: Tier Sensitivity

Each direction: one single named falsifiable condition with an explicit tier destination that differs from the current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section with PM."

> **WRONG tier-down**: "Tier might decrease if simpler." — No named condition; no tier destination. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition | Destination Tier [must differ from current — fill LOW / MEDIUM / HIGH / XL] |
|-----------|-------------------------------------|-----------------------------------------------------------------------------|
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
| Inertia Check | [workaround — cost direction — one sentence] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

_Confidence Gap [with DIAGNOSIS]: See ── CONFIDENCE GAP CHECKPOINT ── section above._

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

---

---

## V-03 — Axis: Phrasing register (Second-person imperative throughout; C-33 failure class in direct-address diagnostic register)

**Variation axis**: Phrasing register — all instructions are direct second-person imperative; the C-33 failure-class label uses "you are in a basis-negation pattern" rather than first-person introspective framing

**Hypothesis**: R11 V-02 uses first-person in the self-test ("Ask — if I reversed something from my Section 6 basis... would I get my gap? If yes, I have written a basis-negation"). V-03 shifts the diagnostic voice to second-person: "If yes: you are in a basis-negation pattern." First-person framing requires the model to adopt a reflective self-narrator role; second-person framing positions the constraint as an external observation the model receives. The hypothesis: second-person diagnostic address activates the constraint as a detection event rather than a self-assessment, which may reduce the rate of compliant-but-vacuous gaps that satisfy the self-test linguistically while violating the intent. C-32 is preserved (standalone section). C-33 is preserved (failure class named). All phrasing is compressed and imperative throughout.

---

Run a **scout-size** sizing signal for the feature below.

You are producing a sizing signal — not a project plan. Strip out any task breakdowns, sprint assignments, owner names, or milestone dates before you finish.

**Tier vocabulary**: assign exactly one of **LOW / MEDIUM / HIGH / XL** — use these tokens and nothing else. MODERATE, 3/5, and medium-high are not valid tier values.

Work through each step. Do not skip ahead.

---

### Step 1: Inertia Check

Before you size anything, establish what NOT building costs.

> **WRONG**: "Teams use Excel today." — You have named the workaround but not judged the cost. Fails.
> **CORRECT**: "Manual CSV re-export per analyst — building is cheaper long-term; overhead scales with headcount (~1 hr/analyst/sprint)."

Name the workaround. State the cost direction — **cheaper / comparable / more expensive** — and give one sentence explaining why.

| Workaround [name it — or "None: [cost of absence]"] | Ongoing Cost [describe friction today] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|------------------------------------------------------|----------------------------------------|--------------------------------------------------------|--------------------------|
| | | | |

---

### Step 2: Surface Area

Name every integration point individually. Count them. A general description fails.

> **WRONG**: "Various APIs and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order-placed), DB migration (orders table), admin UI form — **4 integration points**"

| Integration Point [name each one — "various APIs" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|-------------------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total integration points [numeric count required]** | |

---

### Step 3: Complexity Tier + Driver

Assign exactly one tier. Name what drives it.

> **WRONG tier**: "MODERATE" / "3/5" — Not valid tier vocabulary. Fails.
> **WRONG driver**: "It's complex." — Name the cause. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service transaction semantics — rollback agreement across three services without a distributed coordinator."

| Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1–2 named causal factors — "it's complex" fails] |
|----------------------------------------------|------------------------------------------------------------------|
| | |

---

### Step 4: Team-Size Signal

Name the specialist disciplines you need — headcount alone is not enough.

> **WRONG**: "2–3 engineers." — No disciplines named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM."

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|----------------------------------------------------------------|--------------|
| | |
| **Total FTEs** | |

---

### Step 5: Timeline Signal

Give a sprint range. Not a calendar date. Not a single sprint.

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints."

| Sprint Range [N–M format] |
|---------------------------|
| |

---

### Step 6: Confidence Basis

State your confidence level and name what supports it — what IS established or verified. Do not include what is unknown here; that comes next.

> **WRONG**: "High confidence." — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified — do not include unknowns here] |
|----------------------------------------|--------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

You are now identifying the primary source of residual uncertainty in your sizing. This gap must name a dimension your Step 6 basis does not reach.

**What you must not do:**

> **WRONG**: Step 6 basis: "Auth API contract is stable." Your gap: "Auth API contract is unconfirmed."
> Why this fails: you have reversed a statement from your own basis. You have produced a basis-negation. A reader needs no new information — they can derive your gap directly from Step 6 by negation. That is not a gap; it is a restatement.

**What you must do:**

> **CORRECT**: Step 6 basis: "Auth API contract is stable." Your gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why this passes: you have named a dimension your basis did not reach. A reader cannot derive it from Step 6 by negation or inference.

**Run this check now — before you write your gap:**

> Ask: if you negated a statement from your Step 6 basis, would you produce your gap?
> **If yes: you are in a basis-negation pattern.** Stop. You are restating the basis in negative form. Name a dimension your basis did not address.
> **If no: write your gap below.**

**Your Confidence Gap** [a dimension your Step 6 basis did not address — not a negation of it]:

Gap: _____

---

### Step 7: Confidence Calibration

What would materially change your confidence level?

| What Would Raise Confidence | What Would Lower Confidence |
|-----------------------------|-----------------------------|
| | |

---

### Step 8: Tier Sensitivity

For each direction: name one falsifiable condition and state the tier destination. The destination must differ from your current tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — "Scope grows" is not falsifiable. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync is required — confirm by reviewing PRD offline-sync section."

> **WRONG tier-down**: "Could drop if it turns out to be simpler." — No named condition; no tier destination. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what settles it] | Destination Tier [must differ from current — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Output Compilation

Compile your sizing signal. Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

**SIZING SIGNAL — [feature name]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Inertia Check | [workaround — cost direction — one sentence] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

_Confidence Gap is documented in the ── CONFIDENCE GAP CHECKPOINT ── section above._

---

---

## V-04 — Axis: Role sequence + lifecycle emphasis (Two-phase; C-32 standalone gap as Phase 2 primary output; C-33 in Phase 2 charter)

**Variation axis**: Role sequence — two-phase design where Phase 2 Risk Assessor owns the gap checkpoint section as its primary output; C-32 is achieved through phase ownership of a standalone section; C-33 is embedded in Phase 2's charter self-test

**Hypothesis**: Single-phase designs satisfy 15–18 of 25 aspirational criteria but cannot reach C-20/C-23/C-24/C-25/C-26/C-27/C-29 (7 role-separation criteria). Two-phase design gains all seven at the cost of C-28 (which becomes N/A, replaced by C-25). The innovation in R12: Phase 2's primary production IS the standalone gap checkpoint section (C-32), not a table row within a larger Phase 2 output. The Phase 2 charter embeds the C-33 failure-class label in its non-access self-test ("If yes: you have written a basis-negation — a Phase 2 charter violation"). This makes the failure-class label a charter-level enforcement mechanism, not just a field-body instruction. Role-tagged column headers in the compilation table achieve C-26 structurally. Compilation table references the gap section rather than duplicating it (C-32).

---

You are running a **scout-size** sizing signal in two phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

---

## Phase 1: Sizing Analyst

**Charter**: Produce the sizing foundations — inertia check, surface area, complexity tier, team-size signal, timeline signal, and confidence basis. Do NOT produce the confidence gap, confidence calibration, or tier sensitivity; those are reserved for Phase 2.

**Fields owned by Phase 1**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

**Fields reserved for Phase 2 [do not produce here]**: Confidence Gap · Confidence Calibration · Tier Sensitivity

---

### P1-1: Inertia Check [Phase 1 Sizing Analyst]

Compare building against NOT building before sizing begins.

> **WRONG**: "Users use spreadsheets." — No cost direction. Fails.
> **CORRECT**: "Manual CSV export per team — building is **cheaper** long-term; overhead grows linearly with team count (~45 min/sprint/team)."

| Workaround [name it — or "None: [cost of absence]"] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|------------------------------------------------------|-------------------------------------------------------|--------------------------|
| | | |

---

### P1-2: Surface Area [Phase 1 Sizing Analyst]

> **WRONG**: "API and database integrations." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order-placed), DB migration (orders table) — **3 integration points**"

| Integration Point [name each individually] | Type |
|--------------------------------------------|------|
| | |
| **Total integration points [numeric count required]** | |

---

### P1-3: Complexity Tier + Driver [Phase 1 Sizing Analyst]

> **WRONG tier**: "MODERATE" / "3/5" — Off-vocabulary. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service event ordering — causal sequence required across three consumers without broker-level ordering."

| Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1–2 named causal factors] |
|----------------------------------------------|------------------------------------------|
| | |

---

### P1-4: Team-Size Signal [Phase 1 Sizing Analyst]

> **WRONG**: "3 engineers." — Disciplines not named. Fails.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM."

| Specialist Discipline | FTE |
|-----------------------|-----|
| | |
| **Total** | |

---

### P1-5: Timeline Signal [Phase 1 Sizing Analyst]

> **WRONG**: "6 weeks" / "4 sprints" — Calendar unit; point estimate. Both fail.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format — not a date, not a single number] |
|-------------------------------------------------------------|
| |

---

### P1-6: Confidence Basis [Phase 1 Sizing Analyst]

State confidence and name what IS established. Do not include unknowns — those belong to Phase 2.

> **WRONG**: "Confidence: HIGH" — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include what is unknown] |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor

**Charter**: Assess the residual risk not covered by Phase 1. Produce the confidence gap checkpoint, confidence calibration, and tier sensitivity.

**Non-access clause**: Your confidence gap must address a dimension Phase 1 did NOT confirm. Specifically, you may not cite items the Phase 1 Sizing Analyst confirmed in P1-6 — confirmed API contracts, enumerated integration points, stable component interfaces are already established. Citing them as your gap is a charter violation.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-6 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Your gap is a restatement of Phase 1's confirmed content in negative form. Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce — owned by Phase 1]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty in the Phase 1 sizing. This is Phase 2's primary output. Must address a different dimension than the P1-6 confidence basis.

**What a failing gap looks like (basis-negation — Phase 2 charter violation)**:

> **WRONG**: P1-6 basis: "Auth API contract is stable." Gap: "Auth API contract is unconfirmed."
> Why it fails: same dimension, reversed polarity. The Phase 2 Risk Assessor has negated the Phase 1 Sizing Analyst's confirmed item. This is the exact charter violation defined in the Phase 2 non-access clause: **a basis-negation**.

**What a passing gap looks like (genuine gap)**:

> **CORRECT**: P1-6 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-6.

**Self-test (required before writing your gap)**:

> Ask: could a reader produce this gap by negating a statement from P1-6?
> **If yes: you have written a basis-negation.** This violates your Phase 2 charter. Restate to name a dimension Phase 1 did not confirm.
> If no: proceed.

**Your Confidence Gap [Phase 2 Risk Assessor — must address a dimension outside the P1-6 confirmed set — not a negation of it]**:

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

| Direction | Single Named Falsifiable Condition [one scenario — name what settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current tier — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from Phase 1 and Phase 2:

**SIZING SIGNAL — [feature name]**

| Field | Produced By | Value |
|-------|-------------|-------|
| Surface Area | [Phase 1 Sizing Analyst] | [named points — N integration points] |
| Complexity Tier | [Phase 1 Sizing Analyst] | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [Phase 1 Sizing Analyst] | [1–2 named factors] |
| Team-Size Signal | [Phase 1 Sizing Analyst] | [specialist disciplines + fractions] |
| Timeline Signal | [Phase 1 Sizing Analyst] | [N–M sprints] |
| Confidence Level + Basis | [Phase 1 Sizing Analyst] | [LEVEL — what is established] |
| Inertia Check | [Phase 1 Sizing Analyst] | [workaround — cost direction — one sentence] |
| Tier-Up Sensitivity | [Phase 2 Risk Assessor] | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | [Phase 2 Risk Assessor] | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [Phase 2 Risk Assessor] | [what would raise or lower confidence] |

_Confidence Gap [Phase 2 Risk Assessor]: See ── CONFIDENCE GAP CHECKPOINT ── section above._

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

---

---

## V-05 — Axis: Inertia framing + output format + role sequence (Three-phase; Phase 0 inertia gate; role-tagged column headers; C-32 + C-33 in Phase 2)

**Variation axis**: Inertia framing — inertia is promoted from a section to a mandatory Phase 0 gate that must be closed before Phase 1 sizing begins; combined with three-phase role separation and role-tagged column headers throughout

**Hypothesis**: In all prior designs, the inertia check is a section the model fills in as part of an ordered list — it can be skipped if the model decides not to engage with it carefully, or treated as a checkbox. Promoting it to a Phase 0 gate with an explicit gate-status field ("CLOSED / OPEN") creates a hard prerequisite: the model must state whether the gate is closed before proceeding to sizing. Three-phase design (Phase 0: Inertia Assessor, Phase 1: Sizing Analyst, Phase 2: Risk Assessor) provides the cleanest ownership boundaries of any design in this series. Role-tagged column headers in all tables achieve C-26 structurally — every field carries a role tag at the label level, not only in charter prose. C-32 and C-33 are embedded in Phase 2's standalone gap section. The hypothesis: three-phase structure with explicit gate semantics amplifies the enforcement guarantees of C-32 + C-33 by ensuring sizing cannot proceed without inertia context, and Phase 2's gap is produced with full awareness of Phase 1's confirmed set.

---

You are running a **scout-size** sizing signal in three phases. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

**Phase sequence**: Phase 0 → Phase 1 → Phase 2. You may not begin Phase 1 until the Phase 0 gate is CLOSED. You may not begin Phase 2 until Phase 1 is complete.

---

## Phase 0: Inertia Assessor [Gate — complete before sizing begins]

**Charter**: Establish the cost of NOT building. Sizing without an inertia check produces a build estimate in a vacuum. Close this gate before Phase 1 begins.

**Gate-close condition**: a named workaround (or named cost of absence) AND a stated cost direction (cheaper / comparable / more expensive). Both required. Gate remains OPEN without them.

> **WRONG (gate remains OPEN)**: "Teams manage this manually today." — Workaround named; cost direction absent. Gate not closed.
> **CORRECT (gate CLOSED)**: "Manual CSV export per team — building is **cheaper** long-term; overhead grows with team count (~45 min/sprint/team)."

| Workaround [Phase 0 Inertia Assessor — name it — or "None: [cost of absence]"] | Ongoing Cost [describe friction absorbed today] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|---------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------|--------------------------|
| | | | |

**Gate status**: [ CLOSED — cost direction stated and workaround named ] / [ OPEN — do not proceed to Phase 1 ]

---

## Phase 1: Sizing Analyst [begins after Phase 0 gate is CLOSED]

**Charter**: Produce the sizing foundations — surface area, complexity tier, team-size signal, timeline signal, and confidence basis. Do NOT produce the confidence gap, calibration, or tier sensitivity; those are reserved for Phase 2.

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

> **WRONG**: "MEDIUM confidence." — No basis. Fails.
> **CORRECT**: "MEDIUM — surface area is enumerated and the auth API contract is stable."

| Confidence Level [Phase 1 Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1 Sizing Analyst — name what IS established — do not include unknowns] |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

## Phase 2: Risk Assessor [begins after Phase 1 is complete]

**Charter**: Assess the residual risk not covered by Phase 1. Produce the confidence gap, confidence calibration, and tier sensitivity.

**Non-access clause**: Your gap must address a dimension Phase 1 did NOT confirm. You may not cite any item the Phase 1 Sizing Analyst confirmed in P1-5 as the source of your gap — confirmed API contracts, enumerated integration points, and stable component interfaces are established territory. Citing them is a charter violation.

**Self-test (required — apply before writing your gap)**:

> Ask: if I reversed a statement from P1-5 ("X is confirmed" → "X is not confirmed"), would I produce my gap?
> **If yes: you have written a basis-negation — a Phase 2 charter violation.** Your gap is a restatement of Phase 1's confirmed content in negative form. Restate to name a dimension Phase 1 did not verify.
> If no: proceed.

**Fields owned by Phase 2**: Confidence Gap · Confidence Calibration · Tier Sensitivity

**Fields excluded from Phase 2 [do not re-produce — owned by Phase 0 / Phase 1]**: Inertia Check · Surface Area · Complexity Tier · Primary Driver · Team-Size Signal · Timeline Signal · Confidence Basis

---

## ── CONFIDENCE GAP CHECKPOINT ──

Identify the primary source of residual uncertainty. Phase 2's primary output. Must address a different dimension than the P1-5 confidence basis.

**What a failing gap looks like:**

> **WRONG** (basis-negation — Phase 2 charter violation): P1-5 basis: "Auth API contract is stable." Gap: "Auth API contract is unconfirmed."
> **Failure class: basis-negation.** The Risk Assessor has reversed the Sizing Analyst's confirmed item. This is the charter violation defined in Phase 2's non-access clause. A reader derives it from P1-5 by negation with no new information.

**What a passing gap looks like:**

> **CORRECT** (genuine gap): P1-5 basis: "Auth API contract is stable." Gap: "Webhook delivery ordering under concurrent writes is unverified — exactly-once vs. at-least-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension Phase 1 did not verify. Not derivable by negating P1-5.

**Self-test (required before writing your gap):**

> Ask: could a reader produce this gap by negating a statement from P1-5?
> **If yes: you have written a basis-negation.** You are in a basis-negation pattern. This violates your Phase 2 charter. Stop. Restate to name a dimension Phase 1 did not confirm.
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

> **WRONG tier-down**: "Tier might drop if simpler." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if legacy auth exposes a documented event-hook API — confirm by reading auth API reference."

| Direction | Single Named Falsifiable Condition [Phase 2 Risk Assessor — name what investigation settles it] | Destination Tier [Phase 2 Risk Assessor — must differ from current — fill LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

## Output Compilation

Compile the final signal from all three phases:

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|-------|-------|-------|
| Inertia Check | [Phase 0 Inertia Assessor] | [workaround — cost direction — one sentence] |
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

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.
