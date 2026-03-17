# Scout-Size Prompt Variations — R11

**Skill**: scout-size
**Rubric**: v11 (23 aspirational criteria, C-01 through C-31)
**Date**: 2026-03-17
**Round**: 11
**R10 champion**: V-01 (~96.19) — single-phase with C-28 self-test in Step 7; C-30 and C-31 passed by design
**R10 gaps**: C-19 FAIL (examples follow table rows in Steps 1–7; only Step 9 is pre-slot); C-20/C-23/C-24/C-25/C-26/C-27/C-29 FAIL (no role separation)

---

## Context: What R11 Addresses

v11 adds two new aspirational criteria extracted from R10 V-01's excellence signals:

| New criterion | What it formalizes | R10 evidence |
|---------------|-------------------|--------------|
| C-30 | All three defense mechanisms (C-22 label, C-28/C-25 self-test, C-21 WRONG+CORRECT) must **converge on the same gap field section** — distributed mechanisms leave failure modes the absent co-located mechanism would have caught | V-01 passes C-15 because all three are active within Step 7; individually satisfying them in different sections does not pass C-30 |
| C-31 | When a C-17-scoped field lives in a markdown table and C-19 pre-slot placement is not achieved, a **named gate block** (label + self-test + WRONG/CORRECT) must appear after the last table row and before the next section header | V-01's "Before finalizing your Confidence Gap:" block in Step 7 is the reference implementation: labeled, contains C-28 query, contains C-21 examples — all before Step 8 begins |

R10 V-01 already satisfies C-30 and C-31. The rubric formalizes what it demonstrated. R11 variations explore:
1. Whether C-19 can be achieved alongside C-30 and C-31 without sacrificing single-phase simplicity
2. Whether two-phase and three-phase designs can satisfy C-30 in their Phase 2 gap section while also gaining the full role-separation cluster (C-20, C-23, C-24, C-25, C-26, C-27, C-29)

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format (pre-slot placement throughout) | Extending Step 9's C-19-compliant pattern to all fields — including the gap — achieves C-19 for every C-17-scoped field. C-30 is preserved because all three mechanisms remain in the gap section, now all appearing before the output slot. |
| V-02 | Lifecycle emphasis (gap field as standalone checkpoint) | The C-19 failure stems from the gap being a table cell — pre-row insertion is awkward in markdown. Extracting the gap field into a standalone prose checkpoint before the output compilation makes C-19 trivially achievable and positions the full C-30 cluster naturally, without needing C-31 as mitigation. |
| V-03 | Phrasing register (imperative second-person, active self-interrogation) | The "Before finalizing" gate reads as a suggestion when phrased passively. Reframing it as an imperative self-check ("Ask yourself now:") activates the gate as a thinking step rather than a rule reminder. C-30 and C-31 are maintained; the hypothesis is that register alone changes generation-time engagement. |
| V-04 | Role sequence + lifecycle emphasis (two-phase + C-30 defense cluster in Phase 2) | Single-phase designs cap out at 15/23 aspirational. Adding role separation gains C-20/C-23/C-24/C-25/C-26/C-27/C-29 (7 criteria) at the cost of C-28 (1 criterion — N/A in two-phase). Embedding the full C-30 cluster in Phase 2's gap section — with WRONG/CORRECT before the table (C-19 via pre-slot), C-25 self-test in charter body, and C-22 label in column header — should reach 22/23 aspirational. |
| V-05 | Inertia framing + role sequence + output format (three-phase + maximum structural encoding) | Promoting inertia to Phase 0 makes the cost-of-not-building a gate rather than a section — sizing cannot begin without it. Role-tagged column headers (C-26) make ownership structural rather than prose-only. Combined with Phase 2's C-30 cluster, this tests whether the three-phase architecture introduces overhead that undermines earlier mechanism guarantees or whether it strengthens them through clean phase isolation. |

---

## V-01 — Axis: Output format (Pre-slot example placement throughout)

**Variation axis**: Output format — WRONG/CORRECT examples precede every output field they govern, not follow it
**Hypothesis**: R10 V-01 is internally inconsistent on C-19: Step 9 places examples before the sensitivity table (C-19 compliant) but Steps 2, 3, 6, 7 place examples after the table rows (C-19 non-compliant). The fix is mechanical: apply the Step 9 pre-slot pattern to all fields. For the gap field, moving the defense cluster before the table achieves C-19 while preserving C-30 (all three mechanisms remain in the same gap section) and making C-31 vacuously satisfied (C-31 applies only when C-19 is not achieved).

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Tier vocabulary — assign exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", "medium-high", and "complex" all fail; downstream tools parse these four tokens only.

Work through the following steps in order. Complete each step before moving to the next.

---

### Step 1: Inertia Check

The cost of building must be compared against the cost of NOT building before sizing begins.

> **WRONG**: "Teams currently use spreadsheets." — Workaround named; cost direction absent. Fails.
> **CORRECT**: "Manual CSV export + re-import per team — building is **cheaper** to maintain long-term; the workaround requires ~45 min/sprint/team and that overhead grows linearly with team count."

Name the current workaround and state a directional cost judgment: **cheaper / comparable / more expensive** to build vs. maintain. If no workaround exists, state the cost of operating without the feature.

| Field | Value |
|-------|-------|
| Current Workaround | [name the workaround — or "None: [cost of absence]"] |
| Ongoing Cost | [describe the friction or overhead users absorb today] |
| Cost Direction [cheaper / comparable / more expensive] | |
| Key Driver | [one-sentence explanation of why] |

---

### Step 2: Surface Area

> **WRONG**: "The feature touches several API layers and some UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth API endpoint, event-bus subscription (order-placed), DB schema migration (orders table), admin UI form — **4 integration points**"

Name each integration point individually. Count is mandatory — a general description without named points and a count fails.

| Integration Point [name each individually — "several API layers" is not a named point] | Type [API / hook / event / DB / UI / service / other] |
|----------------------------------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total integration points [numeric count required]** | |

---

### Step 3: Complexity Tier + Primary Driver

> **WRONG tier**: "MODERATE" / "medium-high" / "3 out of 5" — Not on-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "It's a complex feature." — Not a driver; names no causal factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback behavior without a distributed transaction coordinator."

Assign exactly one tier and name the factors that most drive it.

| Complexity Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named factors — "it's complex" fails] |
|----------------------------------------------------------|----------------------------------------------------------------------|
| | |

---

### Step 4: Team-Size Signal

> **WRONG**: "2–3 engineers" — No specialist disciplines named. Fails.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

Name the specialist disciplines needed — headcount alone is insufficient.

| Specialist Discipline [name the role — "engineer" alone fails] | FTE Fraction |
|----------------------------------------------------------------|--------------|
| | |
| | |
| **Total FTEs** | |

---

### Step 5: Timeline Signal

> **WRONG**: "Q3" / "6 weeks" / "4 sprints" — Calendar date; calendar range; point estimate. All fail.
> **CORRECT**: "3–5 sprints"

Give a sprint range. Not a calendar date. Not a single number.

| Sprint Range [N–M format — not a calendar date, not a single number — e.g., "3–5 sprints"] |
|---------------------------------------------------------------------------------------------|
| |

---

### Step 6: Confidence Level + Basis

> **WRONG**: "Confidence: HIGH" — No basis named. Fails.
> **CORRECT**: "MEDIUM — surface area is fully enumerated and the auth API contract is stable; webhook delivery guarantees under concurrent load have not been spiked."

State confidence (HIGH / MEDIUM / LOW) and name what IS established or verified. What is NOT yet known belongs in Step 7 — do not merge them here.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS specifically established or verified — a bare level with no basis fails] |
|----------------------------------------|---------------------------------------------------------------------------------------------------------|
| | |

---

### Step 7: Confidence Gap

The gap names the primary source of residual uncertainty — something the sizing has not yet verified. It must address a **different dimension** than the basis above.

> **WRONG**: Basis = "Auth API contract is stable." Gap = "Auth API contract has not been confirmed." — Same dimension, negated. A reader derives this directly from the basis by negation. This is a restatement, not a gap.
> **CORRECT**: Basis = "Auth API contract is stable." Gap = "Webhook delivery ordering under concurrent writes is unverified — at-least-once vs. exactly-once semantics affect the error-handling surface area and may require an idempotency layer." — Names a dimension the basis did not reach.

**Before writing your gap**, ask: Could a reader derive this gap by negating something confirmed in the basis above — reversing "X is confirmed" to "X has not been confirmed"? If yes, it is a negation of the basis, not a genuine gap. Restate to name a different dimension.

| Confidence Gap [must address a dimension NOT covered by the Confidence Basis above — not a negation or restatement of what the basis confirmed] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

---

### Step 8: Confidence Calibration

What information or investigation result would materially raise or lower the stated confidence level?

| What Would Raise Confidence | What Would Lower Confidence |
|-----------------------------|-----------------------------|
| | |

---

### Step 9: Tier Sensitivity

Each sensitivity direction must be a single, named, falsifiable condition with an explicit tier destination that differs from the currently assigned tier.

> **WRONG tier-up**: "Tier rises to HIGH if scope grows." — Not falsifiable; "scope grows" is a deferral. Fails.
> **WRONG tier-up**: "Several factors could push the tier up." — Not a single named condition; no tier stated. Fails.
> **CORRECT tier-up**: "Tier rises to XL if offline-sync support is required — confirmable by reviewing the PRD offline-sync section with the PM this sprint."
>
> **WRONG tier-down**: "Tier drops to MEDIUM if the integration is simpler than expected." — Not falsifiable. Fails.
> **CORRECT tier-down**: "Tier drops to MEDIUM if the legacy auth layer exposes a documented event-hook API — confirmable by reading the auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — not a list, not a hedge — name what investigation settles it] | Destination Tier [must differ from current tier — fill with LOW / MEDIUM / HIGH / XL — a tier that maps to itself is vacuous] |
|-----------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Output Compilation

After completing all steps above, produce the final signal:

**SIZING SIGNAL — [feature name]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Confidence Gap | [specific named unknown — why it matters] |
| Inertia Check | [workaround — cost direction — one-sentence reasoning] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

---

---

## V-02 — Axis: Lifecycle emphasis (Gap field as standalone checkpoint, not a table cell)

**Variation axis**: Lifecycle emphasis — the confidence gap field is extracted from the output table and given its own named checkpoint section between the confidence basis and the output compilation
**Hypothesis**: The C-19 failure in prior rounds is structural: when the gap field is a table cell, markdown syntax makes pre-row example insertion awkward — the table header, separator, and slot appear in one block, and inserting WRONG/CORRECT rows before the output row produces a malformed or confusing table. Extracting the gap to a standalone section removes this constraint entirely. Examples, self-test, and field prompt appear in natural prose order with no table formatting to navigate. C-19 compliance is a consequence of the section structure, not an additional design effort. C-30 is satisfied by co-location in the checkpoint. C-31 is vacuously satisfied because C-19 is achieved.

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

### Section 3: Complexity

> **WRONG tier**: "MODERATE" or "3/5" — Off-vocabulary. Fails.
> **WRONG driver**: "It has a lot of moving pieces." — Not a named factor. Fails.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service event ordering — three consumers must process in causal sequence without a broker-level ordering guarantee."

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

State confidence and name what IS established.

> **WRONG**: "MEDIUM confidence." — No basis. Fails.
> **CORRECT**: "MEDIUM — integration points are enumerated and the auth API contract is stable. Webhook delivery semantics under concurrent load have not been spiked."

State only what IS known here. What is NOT known gets its own checkpoint next.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS established — do not include what is unknown] |
|----------------------------------------|-----------------------------------------------------------------------------|
| | |

---

## ── CONFIDENCE GAP CHECKPOINT ──

This checkpoint isolates the primary source of residual uncertainty before any output is compiled. It must address a **different dimension** than the basis in Section 6.

**What a failing gap looks like:**

> **WRONG**: Section 6 basis says "Auth API contract is stable." Gap says "Auth API contract has not been confirmed."
> Why it fails: same dimension, opposite polarity. The gap is derivable from the basis by negation — no new information required. This is a restatement.

**What a passing gap looks like:**

> **CORRECT**: Section 6 basis says "Auth API contract is stable." Gap says "Webhook delivery ordering under concurrent writes is unverified — at-least-once vs. exactly-once semantics affect error-handling surface area and may require an idempotency layer."
> Why it passes: names a dimension the basis didn't reach. A reader cannot derive this from Section 6.

**Self-check before writing**: Ask — if I reversed something from my Section 6 basis ("X is established" → "X is not established"), would I get my gap? If yes, I have written a basis-negation, not a gap. Restate to name a dimension the basis did not address.

**Your Confidence Gap** [must address a dimension not covered by the Section 6 basis — not a negation of it]:

Gap: ___

*(Why it matters to the sizing: ___)*

---

### Section 7: Tier Sensitivity

> **WRONG up**: "Tier rises to HIGH if the scope expands." — Not falsifiable; no named investigation. Fails.
> **CORRECT up**: "Tier rises to XL if offline-sync is required — confirm by reviewing the PRD offline-sync section with the PM."
>
> **WRONG down**: "Tier drops if things are simpler." — Not named; not falsifiable. Fails.
> **CORRECT down**: "Tier drops to MEDIUM if the legacy auth layer exposes a documented webhook API — confirm by reading the auth team's API reference."

| Direction | Single Named Falsifiable Condition [one scenario — name what settles it] | Destination Tier [must differ from current: LOW / MEDIUM / HIGH / XL] |
|-----------|--------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Section 8: Confidence Calibration

| What would raise confidence | What would lower confidence |
|-----------------------------|-----------------------------|
| | |

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
| Confidence Gap | [from checkpoint above — specific named unknown — why it matters] |
| Inertia Check | [workaround — cost direction — one-sentence reasoning] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

**Signal boundary check**: No task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-03 — Axis: Phrasing register (Imperative second-person, active self-interrogation)

**Variation axis**: Phrasing register — instructions shift from declarative/descriptive to imperative second-person; the gate label shifts from passive ("Before finalizing your Confidence Gap:") to active command ("Confidence Gap — check this now before writing:")
**Hypothesis**: The C-31 gate passes structurally in R10 V-01, but "Before finalizing" reads as a suggestion — the model encounters it after filling the field slot, which means the gate is advisory rather than generative. Reframing the gate as an explicit imperative command ("Stop. Ask yourself:") activates it as a thinking step the model must perform, not a checklist item to acknowledge. Pre-slot placement (C-19) is maintained throughout, so the gate fires before the field value is produced. The hypothesis is that register — not structure — is the binding variable for generation-time compliance with the self-test.

---

Produce a **scout-size** sizing signal for the feature below.

Do not produce a project plan. No task breakdowns. No sprint assignments. No owner names. No milestone dates. This is a sizing signal — it feeds `program-plan`.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — use exactly one. MODERATE, 3/5, and medium-high are not on the scale and break downstream parsing.

Work through the steps below. Complete each step before moving on.

---

### Step 1 — Inertia Check

Before sizing the build, name what the team is doing instead of having this feature, and decide whether building is worth it.

> **WRONG**: "Teams use Excel today." — No cost direction. Does not pass.
> **CORRECT**: "Manual CSV re-export per analyst — building is cheaper long-term; the workaround takes ~1 hour per analyst per sprint and scales with headcount."

Name the workaround. State the cost direction: **cheaper / comparable / more expensive** to build than to keep maintaining the workaround. Add one sentence explaining why.

| Workaround | Cost Direction [cheaper / comparable / more expensive] | One-sentence reason |
|------------|-------------------------------------------------------|---------------------|
| | | |

---

### Step 2 — Surface Area

Name every integration point individually. Include a total count.

> **WRONG**: "The feature touches several backend and frontend layers." — No named points; no count.
> **CORRECT**: "Auth API endpoint, event-bus topic (user.created), DB schema migration (users), admin settings form — **4 integration points**"

| Integration Point [name it — no general descriptions] | Type [API / hook / event / DB / UI / service / other] |
|------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total** | **[N] integration points** |

---

### Step 3 — Complexity Tier

Pick exactly one: **LOW / MEDIUM / HIGH / XL**

Do not use MODERATE. Do not use 3/5. Do not use a descriptor. Pick one of the four.

Name the 1–2 factors that most drive this rating.

> **WRONG driver**: "The complexity comes from the many moving parts." — Not a named factor.
> **CORRECT driver**: "Auth service owns session state — any write to the user model requires two-phase coordination with the session service or risks stale session tokens."

| Tier [LOW / MEDIUM / HIGH / XL — nothing else] | Primary Complexity Driver [name 1–2 causal factors — vague descriptions fail] |
|------------------------------------------------|-------------------------------------------------------------------------------|
| | |

---

### Step 4 — Team-Size Signal

Name the specialist roles needed. Headcount alone is not enough.

> **WRONG**: "2 engineers" — No disciplines.
> **CORRECT**: "1 backend engineer (auth domain), 1 platform engineer, 0.5 PM"

| Specialist Discipline | FTE |
|-----------------------|-----|
| | |
| **Total** | |

---

### Step 5 — Timeline Signal

Give a sprint range. Not a date. Not a single number.

> **WRONG**: "Q3 delivery" / "4 sprints" — Calendar reference; point estimate.
> **CORRECT**: "3–5 sprints"

| Sprint Range [write it as N–M — e.g., "3–5 sprints"] |
|-------------------------------------------------------|
| |

---

### Step 6 — Confidence Level + Basis

State how confident you are in the sizing and name what you know.

> **WRONG**: "Confidence: MEDIUM." — No basis. Fails.
> **CORRECT**: "MEDIUM — integration surface is bounded at four points with stable contracts; the auth coordination pattern is documented."

| Level [HIGH / MEDIUM / LOW] | Basis [state what IS established — don't include what's unknown here] |
|-----------------------------|-----------------------------------------------------------------------|
| | |

---

### Step 7 — Confidence Gap

**Stop. Read this before you write anything.**

> **WRONG gap**: Basis = "Auth API contract is stable." → Gap = "The auth API contract hasn't been confirmed."
> This fails. It's a negation of the basis — the same dimension, reversed. A reader derives it from Step 6 by flipping one phrase.

> **CORRECT gap**: Basis = "Auth API contract is stable." → Gap = "Concurrent write behavior — whether the event bus guarantees at-least-once or exactly-once delivery under load — is unverified. If the guarantee is weak, an idempotency layer becomes a required integration point."
> This passes. It names a dimension Step 6 didn't touch.

**Now check your draft**: Ask yourself — if I took something from my Step 6 basis and negated it, would I get this gap? If yes, throw it out and name a genuinely different dimension.

| Confidence Gap [must name a dimension Step 6 did NOT establish — negating the basis fails this field] |
|---|
| Gap: [specific unknown] — [why it matters to the sizing] |

---

### Step 8 — Confidence Calibration

| What would raise confidence | What would lower confidence |
|-----------------------------|-----------------------------|
| | |

---

### Step 9 — Tier Sensitivity

For each direction: name one specific condition, state the destination tier explicitly, make it falsifiable.

> **WRONG up**: "If the project scope expands, the tier could rise." — Not falsifiable; no tier named.
> **CORRECT up**: "Tier rises to XL if real-time sync is required — confirm by checking the product spec's sync requirements section."
>
> **WRONG down**: "Tier drops if it's simpler than anticipated." — Not named; not falsifiable.
> **CORRECT down**: "Tier drops to MEDIUM if the auth service exposes a documented event-hook — confirm by reading the auth team's API reference this sprint."

| Direction | One Condition [name it — name what settles it] | Destination Tier [must differ from current: LOW / MEDIUM / HIGH / XL] |
|-----------|------------------------------------------------|-----------------------------------------------------------------------|
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
| Confidence Gap | [specific named unknown — why it matters] |
| Inertia Check | [workaround — cost direction — one-sentence reasoning] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

Final check: Remove any task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-04 — Combined: Role sequence + Lifecycle emphasis (Two-phase + C-30 defense cluster in Phase 2)

**Variation axis**: Role sequence + Lifecycle emphasis (combined)
**Hypothesis**: Single-phase designs cap at ~15/23 aspirational (failing the entire role-separation cluster: C-20/C-23/C-24/C-25/C-26/C-27/C-29). Adding two-phase role separation gains 7 criteria at the cost of 1 (C-28 is N/A in two-phase; C-25 is its Phase 2 equivalent). The net gain is ~6 aspirational criteria. The design challenge: Phase 2 must contain the full C-30 defense cluster (C-22 label in column header + C-25 self-test in charter body + C-21 WRONG+CORRECT) within the same section, all before the gap table row (C-19 via pre-slot). C-31 named gate after the table row provides belt-and-suspenders. C-23 is satisfied by exhaustive field enumeration in both charters with explicit exclusion lists (C-29 satisfied by Phase 1 listing what it excludes). C-24 is satisfied by naming the prohibited content categories in Phase 2's non-access clause. C-26 is satisfied by role labels in compilation table column headers. C-27 is satisfied by encoding the C-15 non-overlap constraint in the gap column header of the compilation table.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in two phases by two analyst roles. Complete Phase 1 entirely before reading Phase 2. Each role produces exactly the fields in its charter.

---

## Phase 1 — Sizing Analyst

**Charter — you own these 10 fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + fractions)
5. Timeline Signal (sprint range)
6. Confidence Level (HIGH / MEDIUM / LOW)
7. Confidence Basis (what IS established)
8. Inertia Check (workaround + cost direction)
9. Tier-Up Sensitivity (single named falsifiable condition → explicit tier destination)
10. Tier-Down Sensitivity (single named falsifiable condition → explicit tier destination)
11. Confidence Calibration (what would raise or lower confidence)

**Charter — you do NOT produce**: Confidence Gap. That field belongs to Phase 2.

---

### 1.1 Inertia Check

> **WRONG**: "Teams use a spreadsheet." — No cost direction. Fails.
> **CORRECT**: "Manual CSV export + re-import — building is **cheaper** long-term; the workaround requires ~45 min/sprint/team and scales linearly with team count."

| Workaround [name it] | Cost Direction [cheaper / comparable / more expensive] | Key Driver [one sentence] |
|----------------------|-------------------------------------------------------|--------------------------|
| | | |

---

### 1.2 Surface Area

> **WRONG**: "Several API and UI integrations." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (user.created), DB migration (users table) — **3 integration points**"

| Integration Point [name individually] | Type |
|--------------------------------------|------|
| | |
| | |
| **Total** | **[N] integration points** |

---

### 1.3 Complexity Tier + Primary Driver

> **WRONG tier**: "MODERATE" — Off-vocabulary.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "The feature is technically complex." — No causal factor named.
> **CORRECT driver**: "Auth coordination — writes to the user model require two-phase agreement with the session service to prevent stale token issuance."

| Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [1–2 named factors — vague descriptions fail] |
|----------------------------------------------|--------------------------------------------------------------|
| | |

---

### 1.4 Team-Size Signal

> **WRONG**: "3 engineers" — Disciplines not named.
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

| Specialist Discipline | FTE |
|-----------------------|-----|
| | |
| **Total** | |

---

### 1.5 Timeline Signal

> **WRONG**: "Q3" / "4 sprints" — Calendar reference; point estimate.
> **CORRECT**: "3–5 sprints"

| Sprint Range [N–M format] |
|---------------------------|
| |

---

### 1.6 Confidence Level + Basis

> **WRONG**: "Confidence: MEDIUM" — No basis.
> **CORRECT**: "MEDIUM — integration points are bounded at three stable endpoints; auth coordination pattern is documented."

Name what IS established here. What is NOT known belongs to Phase 2.

| Confidence Level [HIGH / MEDIUM / LOW] | Confidence Basis [name what IS verified — do not address what is unknown] |
|----------------------------------------|--------------------------------------------------------------------------|
| | |

---

### 1.7 Tier-Up Sensitivity

> **WRONG**: "Tier rises if the scope expands." — Not falsifiable.
> **CORRECT**: "Tier rises to XL if real-time sync is required — confirm by reviewing the PRD sync section with the PM."

| Single Named Condition [one scenario — name what settles it] | Destination Tier [must be HIGHER than current tier: HIGH or XL] |
|--------------------------------------------------------------|----------------------------------------------------------------|
| | Tier rises to [ ] |

---

### 1.8 Tier-Down Sensitivity

> **WRONG**: "Tier drops if things are simpler." — Not falsifiable.
> **CORRECT**: "Tier drops to MEDIUM if the auth layer exposes a documented webhook API — confirm by reading the auth team's reference."

| Single Named Condition [one scenario — name what settles it] | Destination Tier [must be LOWER than current tier: LOW or MEDIUM] |
|--------------------------------------------------------------|------------------------------------------------------------------|
| | Tier drops to [ ] |

---

### 1.9 Confidence Calibration

| What would raise confidence | What would lower confidence |
|-----------------------------|-----------------------------|
| | |

---

**Phase 1 complete. Proceed to Phase 2.**

---

## Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**

**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Complexity Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Inertia Check, Tier-Up Sensitivity, Tier-Down Sensitivity, Confidence Calibration. All of those belong to Phase 1.

**Non-access rule — prohibited content categories:**
You are explicitly prohibited from citing as the gap any of the following categories that the Sizing Analyst confirmed in Phase 1:
- The **integration points** the Sizing Analyst enumerated as the surface area
- The **API contract status** the Sizing Analyst confirmed as established
- The **complexity tier drivers** the Sizing Analyst named
- The **team and timeline signals** the Sizing Analyst produced

These categories constitute the confirmed basis. Your gap must identify a dimension Phase 1 did not reach.

**Self-test — apply this before writing your gap:**
Ask: "Could a reader look only at Phase 1 output and derive my gap by negating something the Sizing Analyst confirmed — reversing 'X is established' to 'X has not been confirmed'?" If yes, it is a restatement and a charter violation. Restate to name a genuinely new dimension.

---

Read both examples, then write your gap:

> **WRONG gap** (charter violation — basis negation):
> Phase 1 basis: "Auth API contract is stable — established baseline."
> Gap: "Auth API contract has not been confirmed." — Same dimension, negated. Directly derivable from Phase 1 by negation. Charter violation.

> **CORRECT gap** (new dimension Phase 1 did not reach):
> Phase 1 basis: "Auth API contract is stable — three endpoints with documented schemas."
> Gap: "Auth API rate-limiting behavior under sustained concurrent event load is undocumented — if the rate limit falls below expected event volume, a backpressure or queuing layer becomes a required integration point, expanding surface area and potentially shifting the tier." — Independent dimension. Cannot be derived from Phase 1.

| Confidence Gap [Phase 2: Risk Assessor — PROHIBITED: integration points Analyst enumerated, API contract status Analyst confirmed, complexity drivers Analyst named, team/timeline signals Analyst established — must name a dimension Phase 1 did not reach — not derivable from Phase 1 by negation] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before finalizing your Confidence Gap**: Run the self-test one more time. If your gap negates anything the Sizing Analyst confirmed in Phase 1, it is a charter violation. Restate.

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|-------|-------|-------|
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier | 1 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal | 1 | [N–M sprints] |
| Confidence Level + Basis | 1 | [LEVEL — what is established] |
| Confidence Gap [must address a different dimension than Phase 1 Confidence Basis — not a negation of what Phase 1 confirmed] | 2 | [specific named unknown — why it matters] |
| Inertia Check | 1 | [workaround — cost direction — reasoning] |
| Tier-Up Sensitivity | 1 | Tier rises to [LEVEL] if [condition] |
| Tier-Down Sensitivity | 1 | Tier drops to [LEVEL] if [condition] |
| Confidence Calibration | 1 | [what would raise or lower confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-05 — Combined: Inertia framing + role sequence + output format (three-phase + maximum structural encoding)

**Variation axis**: Inertia framing + role sequence + output format (combined)
**Hypothesis**: Four mechanisms combine: (1) Phase 0 promotes inertia analysis to a gate — sizing cannot begin until the cost-of-not-building is stated, making it structurally primary rather than a supplementary step that can be deferred or abbreviated; (2) three-phase charter enumeration provides clean field ownership across three roles with explicit exclusion lists in all phases (C-23, C-29); (3) role-tagged column headers encode ownership structurally in every table (C-26) rather than relying on charter prose alone; (4) Phase 2's C-30 defense cluster — C-22 label in column header, C-25 self-test in charter body before the table, C-21 WRONG+CORRECT before the table, and C-31 named gate block after the table row — provides maximum protection depth for the highest-risk field. The three-phase architecture tests whether adding Phase 0 overhead improves or undermines overall mechanism coherence by forcing earlier deliberate engagement with the build/no-build question.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in three phases. Each phase has an analyst role with a charter. Complete each phase fully before reading the next.

---

## Phase 0 — Inertia Analyst

**Charter — you own exactly one field: Inertia Check.**
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

The cost of building must be compared against the cost of NOT building before sizing begins. A build estimate in isolation cannot tell you whether the effort is worthwhile.

> **WRONG**: "Teams currently use manual exports." — No cost direction. Fails.
> **CORRECT**: "Manual CSV export + re-import — building is **cheaper** long-term; the workaround requires ~45 min/sprint/team and scales linearly with team count."

| Inertia Check [Phase 0: Inertia Analyst — name the workaround AND state cheaper / comparable / more expensive — cost direction is required] |
|---|
| [Workaround] — building is [cheaper / comparable / more expensive] than maintaining. [One-sentence reasoning.] |

---

**Phase 0 complete. Proceed to Phase 1.**

---

## Phase 1 — Sizing Analyst

**Charter — you own these nine fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Tier-Up Sensitivity (single named falsifiable condition → explicit tier destination)
8. Tier-Down Sensitivity (single named falsifiable condition → explicit tier destination)
9. Confidence Calibration (what would raise or lower confidence)

**Charter — you do NOT produce**: Inertia Check (owned by Phase 0). Confidence Gap (owned by Phase 2).

---

### Surface Area [Phase 1: Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count.
> **CORRECT**: "Auth endpoint, event-bus subscription (user.created), DB migration (users table) — **3 integration points**"

| Integration Point [Phase 1: Sizing Analyst — name each individually — "several API layers" fails] | Type [API / hook / event / DB / UI / service / other] |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total** | **[N] integration points** |

---

### Complexity [Phase 1: Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" — Off-vocabulary.
> **WRONG driver**: "It has many moving parts." — Not a causal factor.
> **CORRECT**: Tier: HIGH | Driver: "Cross-service coordination — three services must reach consensus on rollback without a distributed transaction coordinator."

| Tier [Phase 1: Sizing Analyst — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1: Sizing Analyst — 1–2 named causal factors — vague descriptions fail] |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

### Team-Size Signal [Phase 1: Sizing Analyst]

> **WRONG**: "3 engineers" — Disciplines not named.
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 1 PM"

| Specialist Discipline [Phase 1: Sizing Analyst — name the role] | FTE |
|-----------------------------------------------------------------|-----|
| | |
| **Total** | |

---

### Timeline Signal [Phase 1: Sizing Analyst]

> **WRONG**: "Q3" / "4 sprints" — Calendar reference; point estimate.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1: Sizing Analyst — N–M format — not a date, not a single number] |
|---------------------------------------------------------------------------------------|
| |

---

### Confidence Level + Basis [Phase 1: Sizing Analyst]

> **WRONG**: "Confidence: MEDIUM." — No basis.
> **CORRECT**: "MEDIUM — integration points bounded at three stable endpoints with documented contracts; auth coordination pattern is established."

Name only what IS established. What is NOT yet known belongs to Phase 2.

| Confidence Level [Phase 1: Sizing Analyst — HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1: Sizing Analyst — what IS verified — do not include what is unknown] |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| | |

---

### Tier Sensitivity [Phase 1: Sizing Analyst]

> **WRONG up**: "Tier rises if the scope grows." — Not falsifiable.
> **CORRECT up**: "Tier rises to XL if real-time sync is required — confirm by reviewing the PRD sync section."
>
> **WRONG down**: "Tier drops if things simplify." — Not named; not falsifiable.
> **CORRECT down**: "Tier drops to MEDIUM if the auth layer exposes a documented webhook API — confirm by reading the auth team's reference."

| Direction | Single Named Condition [Phase 1: Sizing Analyst — one scenario — name what settles it] | Destination Tier [Phase 1: Sizing Analyst — must differ from current: LOW / MEDIUM / HIGH / XL] |
|-----------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

### Confidence Calibration [Phase 1: Sizing Analyst]

| What would raise confidence | What would lower confidence |
|-----------------------------|-----------------------------|
| | |

---

**Phase 1 complete. Proceed to Phase 2.**

---

## Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**
**Charter — you do NOT produce**: Inertia Check (Phase 0), Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Tier-Up Sensitivity, Tier-Down Sensitivity, Confidence Calibration (Phase 1).

**Non-access rule — prohibited content categories:**
The Sizing Analyst confirmed the following in Phase 1. You are explicitly prohibited from citing any of these as the gap:
- The **integration points** the Sizing Analyst enumerated
- The **API contract status** the Sizing Analyst confirmed as established
- The **complexity tier drivers** the Sizing Analyst identified
- The **team and timeline signals** the Sizing Analyst produced

**Self-test — apply this before writing your gap:**
"Could a reader look only at Phase 1 output and derive my gap by negating something the Sizing Analyst confirmed — turning 'X is established' into 'X has not been confirmed'?" If yes, it is a charter violation. Name a dimension Phase 1 did not reach.

---

Read both examples, then write your gap:

> **WRONG gap** (charter violation — basis negation):
> Phase 1 basis: "Auth API contract is stable — established baseline."
> Gap: "Auth API contract has not been confirmed." — Same dimension, opposite polarity. Directly derivable from Phase 1.

> **CORRECT gap** (new dimension Phase 1 did not address):
> Phase 1 basis: "Auth API contract is stable — three endpoints documented."
> Gap: "Auth API rate-limiting under sustained concurrent event load is undocumented — if the rate limit falls below expected event volume, a backpressure layer becomes a required integration point, expanding surface area." — Independent dimension Phase 1 did not reach.

| Confidence Gap [Phase 2: Risk Assessor — PROHIBITED: integration points Analyst enumerated, API contracts Analyst confirmed, complexity drivers Analyst named, team/timeline signals Analyst produced — must name a dimension Phase 1 did not reach — verify it is NOT derivable from Phase 1 by negation before writing] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before finalizing your Confidence Gap**: Run the self-test one more time. If your gap negates anything in Phase 1's Confidence Basis, it is a charter violation. Restate to name a genuinely different dimension.

---

## Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|-------|-------|-------|
| Inertia Check | 0 | [workaround — cost direction — reasoning] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier | 1 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal | 1 | [N–M sprints] |
| Confidence Level + Basis | 1 | [LEVEL — what is established] |
| Confidence Gap [must address a different dimension than Phase 1 Confidence Basis — not a negation of what Phase 1 confirmed] | 2 | [specific named unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [LEVEL] if [condition] |
| Tier-Down Sensitivity | 1 | Tier drops to [LEVEL] if [condition] |
| Confidence Calibration | 1 | [what would raise or lower confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates anywhere in this output.

---

```json
{
  "skill": "scout-size",
  "round": 11,
  "rubric": "v11",
  "variations": 5,
  "new_criteria_targeted": ["C-30", "C-31"],
  "aspirational_denominator": 23,
  "axes": {
    "V-01": "output-format-pre-slot-placement-all-fields",
    "V-02": "lifecycle-emphasis-gap-as-standalone-checkpoint",
    "V-03": "phrasing-register-imperative-self-interrogation",
    "V-04": "combined-role-sequence-lifecycle-two-phase-C30-in-phase2",
    "V-05": "combined-inertia-framing-role-sequence-output-format-three-phase-max-encoding"
  },
  "c30_mechanism": {
    "V-01": "all three mechanisms in Step 7 section — WRONG/CORRECT before table, self-test query before table, C-22 label in column header",
    "V-02": "all three mechanisms in CONFIDENCE GAP CHECKPOINT standalone section — no table, natural pre-slot order",
    "V-03": "all three mechanisms in Step 7 section — imperative framing; WRONG/CORRECT and self-test before table",
    "V-04": "all three mechanisms in Phase 2 gap section — WRONG/CORRECT before table (C-19), C-25 self-test in Phase 2 charter body before table, C-22 in column header",
    "V-05": "all three mechanisms in Phase 2 gap section — same as V-04; Phase 0 separation adds inertia gate"
  },
  "c31_mechanism": {
    "V-01": "vacuously satisfied — C-19 is achieved (examples before table); no in-table gap field without pre-slot examples exists",
    "V-02": "vacuously satisfied — gap field is not in a table at all; C-19 trivially achieved",
    "V-03": "vacuously satisfied — C-19 is achieved (examples before table)",
    "V-04": "belt-and-suspenders — 'Before finalizing your Confidence Gap:' named gate block after table row, before Phase 2 section closes; C-19 also achieved via pre-slot",
    "V-05": "belt-and-suspenders — 'Before finalizing your Confidence Gap:' named gate block after table row in Phase 2; C-19 achieved via pre-slot"
  },
  "expected_aspirational_passes": {
    "V-01": "~15/23 (gains C-19; retains C-09-18, C-21-22, C-28, C-30-31; no role separation)",
    "V-02": "~15/23 (C-19 trivially achieved via prose checkpoint; same role-separation profile as V-01)",
    "V-03": "~15/23 (register change; same structural profile as V-01)",
    "V-04": "~22/23 (gains C-20/C-23/C-24/C-25/C-26/C-27/C-29 from role separation; C-28 N/A in two-phase design)",
    "V-05": "~22/23 (same as V-04; Phase 0 adds inertia gate; C-28 N/A in three-phase design)"
  }
}
```
