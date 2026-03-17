# Scout-Size Prompt Variations — R8

**Skill**: scout-size
**Rubric**: v8 (24 criteria, C-01 through C-24)
**Date**: 2026-03-16
**Round**: 8
**R7 champion**: V-03 (~100 speculative) — role-separated production added C-20
**R7 gap**: V-03's charters covered only the basis/gap pair (C-23 fail); Phase 2 prohibition named structural property only, not content category (C-24 fail)

---

## Context: What R8 addresses

R7 established role-separated production (C-20) as the path to 100. The scorecard caveat was exact: "role-switching overhead may create new failure modes if role boundaries introduce ambiguity about which role owns OTHER fields." The v8 rubric extracts that caveat as two new criteria:

| New criterion | What it requires | R7 failure mode |
|---------------|-----------------|-----------------|
| C-23 | Every output field in exactly one role's charter as a named production responsibility | V-03 separated only the basis/gap pair; all other fields were implicitly Phase 1's — implicit is not charter |
| C-24 | Phase 2 non-access clause names the **prohibited content category**, not only the structural property ("address a different dimension") | V-03's prohibition was structural: "address a different dimension." A named prohibition — "do not cite the API contract status the Analyst confirmed" — is falsifiable at the role level without cross-referencing Phase 1 output |

**R8 design requirement**: Every variation must pass C-20 + C-23 + C-24. Single-axis variations target one mechanism for each new criterion. Combinations chain them.

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Charter completeness (explicit field lists in both charters) | Enumerating every field by name in Phase 1's charter, with named exclusions in Phase 2's charter, satisfies C-23 without restructuring the two-phase design |
| V-02 | Named category prohibition with falsifiability test | Phase 2's non-access clause names the specific content categories Phase 1 is expected to confirm, then adds a falsifiability gate: if the gap could be verified from Phase 1 output alone, it is a restatement |
| V-03 | Role-tagged column headers (C-23 via structural encoding) | Embedding role ownership in every column header satisfies C-23 at the output-skeleton level — no separate charter document to skip or misread |
| V-04 | Reversed role sequence + complete charter enumeration | Running the Risk Assessor first (gap identified before basis is established) prevents basis anchoring; full charter enumeration in both phases satisfies C-23 regardless of order |
| V-05 | Three-phase + inertia-first + full charter + named prohibition + table encoding | Separating inertia (Phase 0) promotes the cost-of-not-building to a gate; full charter enumeration across three roles satisfies C-23; named category prohibition with basis-content reference satisfies C-24; table encoding makes all of this structural |

---

## V-01 — Axis: Charter Completeness (Explicit Field Lists)

**Variation axis**: Role sequence / Lifecycle emphasis (full field ownership enumeration in both charters)
**Hypothesis**: The R7 V-03 caveat was not about role separation itself but about what "phase 1" implicitly owned without being told so. Naming every field explicitly in Phase 1's charter, and having Phase 2's charter name both what it owns and what it is prohibited from naming as the gap, closes C-23 and C-24 without changing the V-03 two-phase structure. The explicit field list is the structural device — it eliminates implicit ownership by requiring the charter to be exhaustive.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the complexity tier vocabulary.

**Complexity tier vocabulary** — use exactly one, no substitutions: **LOW / MEDIUM / HIGH / XL**

You will complete this in two phases. Finish Phase 1 entirely before reading Phase 2.

---

## Phase 1 — Sizing Analyst

**Charter — you OWN these fields and produce them here:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Inertia Check (workaround named, cost direction stated)
8. Tier-Up Sensitivity (single named condition → explicit tier destination)
9. Tier-Down Sensitivity (single named condition → explicit tier destination)
10. Confidence Calibration (what would materially raise or lower confidence)

**Charter — you do NOT produce**: Confidence Gap. That field belongs to Phase 2.

---

### 1.1 Surface Area

Name each integration point individually and provide a total count.

Format: `[point 1], [point 2], [point N] — **N integration points**`

> **WRONG**: "The feature touches several API layers and some UI components." (no named points, no count)
> **CORRECT**: "API endpoint (auth), event bus subscription (order-placed), DB schema migration — **3 integration points**"

Required: named individual points AND a count. A general description without named points and a count fails.

**Your output:**

---

### 1.2 Complexity Tier

Assign exactly one: **LOW / MEDIUM / HIGH / XL**

> **WRONG**: "MODERATE" / "3/5" / "complex" — none of these are on the permitted scale.
> **CORRECT**: "HIGH"

**Your tier:**

**Primary complexity driver** [one or two named factors — "it's complex" is not a driver]:

---

### 1.3 Team-Size Signal

Name the specialist disciplines needed — not just headcount.

Format: `1 backend engineer, 0.5 PM, 1 platform engineer`

> **WRONG**: "3 engineers" (disciplines not named)
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

**Your output:**

---

### 1.4 Timeline Signal

Give a sprint range. Not a calendar date. Not a single fixed number.

Format: `N–M sprints`

> **WRONG**: "Q3" / "6 weeks" / "3 sprints" (calendar date; calendar range; point estimate)
> **CORRECT**: "3–5 sprints"

**Your output:**

---

### 1.5 Confidence Level + Basis

State your confidence level and name what IS established or verified — the specific dimension that supports the rating.

Format: `[HIGH / MEDIUM / LOW] — [what is established/verified]`

> **WRONG**: "Confidence: HIGH" (no basis — bare level fails)
> **CORRECT**: "MEDIUM — surface area is fully enumerated and the API contract is stable; webhook delivery guarantees under concurrent load have not been spiked."

A confidence level without a named basis fails. State only what IS known here; what is NOT known belongs to Phase 2.

**Your output:**

---

### 1.6 Inertia Check

Name the current workaround and give a directional cost judgment.

Format: `[Workaround] — building is [cheaper / comparable / more expensive] than maintaining. [One-sentence reasoning.]`

> **WRONG**: "Users currently use a spreadsheet." (workaround named; no cost direction)
> **CORRECT**: "Manual CSV export + import via spreadsheet — building is cheaper to maintain long-term; the workaround requires 45 minutes per team per sprint and grows with team count."

An output that names the workaround without a cost direction fails. If there is no workaround, state: "No established workaround — cost of operating without this feature is [describe]."

**Your output:**

---

### 1.7 Tier-Up Sensitivity

State ONE specific, named, falsifiable condition that would push the complexity tier UP.

Constraints — all four must be satisfied:
- Single scenario (not a list or vague hedge)
- Destination tier stated explicitly: **Tier rises to [HIGH or XL — must be HIGHER than your assigned tier]**
- Falsifiable: name what concrete investigation would settle this condition
- Destination tier is different from your currently assigned tier

> **WRONG**: "Tier rises to HIGH if scope grows." (not falsifiable — "scope grows" is a deferral, not a condition)
> **WRONG**: "Several factors could push the complexity tier up." (not a single named condition; no tier stated)
> **CORRECT**: "Tier rises to XL if offline-sync support is required — confirmable by reviewing the PRD offline-sync section with the PM this sprint."

**Your output: Tier rises to [\_\_] if:**

---

### 1.8 Tier-Down Sensitivity

State ONE specific, named, falsifiable condition that would push the complexity tier DOWN.

Same constraints: single scenario, destination tier stated explicitly as **Tier drops to [LOW or MEDIUM — must be LOWER than your assigned tier]**, falsifiable, destination differs from current tier.

> **WRONG**: "Tier drops to LOW if the integration is simpler than expected." (not falsifiable — "simpler than expected" names no investigation)
> **CORRECT**: "Tier drops to MEDIUM if the legacy auth layer exposes a documented event-hook API — confirmable by reading the auth team's API reference."

**Your output: Tier drops to [\_\_] if:**

---

### 1.9 Confidence Calibration

State what information or investigation result would materially raise or lower the stated confidence level.

**Your output:**

---

**Stop here. Do not proceed to Phase 2 until Phase 1 is complete.**

---

## Phase 2 — Risk Assessor

**Charter — you OWN this field and produce it here:**
- Confidence Gap (the specific thing NOT yet known or verified)

**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level + Basis, Inertia Check, Tier-Up Sensitivity, Tier-Down Sensitivity, Confidence Calibration. All of those belong to Phase 1.

**Non-access rule — named category prohibition:**
You are explicitly prohibited from citing as the gap any of the following categories of content that the Sizing Analyst confirmed in Phase 1:
- The integration points the Analyst enumerated (e.g., "the API endpoint is not yet confirmed")
- The API contract status the Analyst established (e.g., "the API contract has not been verified")
- The complexity tier drivers the Analyst named
- The team and timeline signals the Analyst produced

These are the established basis. Your gap must name a dimension Phase 1 did not reach.

Charter violation test: If your gap says "[X] is not confirmed" and the Phase 1 basis says "[X] is established" — that is the same dimension with opposite polarity. Start over and name a genuinely different dimension.

> **WRONG**: Phase 1 basis = "API contract is stable and surface area is enumerated." Gap = "API contract status has not been confirmed." (Same dimension, negated — charter violation)
> **CORRECT**: Phase 1 basis = "API contract is stable and surface area is enumerated." Gap = "Webhook delivery ordering guarantees under concurrent writes are unverified — at-least-once vs. exactly-once semantics affect the error-handling surface area and may require an idempotency layer."

### 2.1 Confidence Gap

Name the specific thing that is NOT yet known or verified — the primary source of residual uncertainty. Address a dimension Phase 1 did not establish.

Format: `Gap: [specific named unknown] — [why it matters to the sizing]`

**Your output:**

---

## Output Compilation

After completing both phases, produce the final signal as:

**SIZING SIGNAL — [feature name]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [specialist disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Confidence Gap | [specific named unknown from Phase 2] |
| Inertia Check | [workaround — cost direction — one-sentence reasoning] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

**Signal boundary check**: Remove any task breakdowns, sprint assignments, owner names, or milestone dates before finalizing.

---

---

## V-02 — Axis: Named Category Prohibition with Falsifiability Gate

**Variation axis**: Lifecycle emphasis (Phase 2 non-access clause — named category + falsifiability test)
**Hypothesis**: C-24 fails when the prohibition is structural ("address a different dimension") because a model can satisfy the letter while violating the intent — it can frame a negation of Phase 1 content as a "different dimension" if the prohibition lacks specificity. The fix is two-part: (1) name the specific content categories Phase 1 is expected to produce (API contracts, integration points, complexity drivers, team/timeline signals), and (2) add a falsifiability gate — if a reader could identify the gap by looking only at Phase 1 output, the gap is a restatement, not a new uncertainty. The falsifiability gate makes the prohibition self-enforcing: the Risk Assessor must ask "could this be derived from what the Analyst already said?" before writing.

---

You are running a **scout-size** sizing signal for the feature described below. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Complexity tier vocabulary** — assign exactly one: **LOW / MEDIUM / HIGH / XL** — nothing else.

Complete Phase 1 fully before reading Phase 2.

---

## Phase 1 — Sizing Analyst

**Charter — you own all sizing fields except the Confidence Gap.** Produce each of the following in sequence:

**[Phase 1 Field 1] Surface Area**

Name every integration point individually and provide a total count. Count is mandatory.

> **WRONG**: "Several API and UI integrations" — no named points, no count.
> **CORRECT**: "Auth API endpoint, event-bus subscription (user-created), DB schema migration (users table), admin UI form — **4 integration points**"

---

**[Phase 1 Field 2] Complexity Tier**

Assign exactly one: **LOW / MEDIUM / HIGH / XL**

**[Phase 1 Field 3] Primary Complexity Driver**

Name the 1–2 factors most driving the tier. "It's complex" is not a driver.

---

**[Phase 1 Field 4] Team-Size Signal**

Name specialist disciplines. Not headcount alone.

> **WRONG**: "2–3 engineers"
> **CORRECT**: "1 backend engineer, 1 platform engineer, 0.5 PM"

---

**[Phase 1 Field 5] Timeline Signal**

Sprint range. Not a calendar date. Not a single number.

> **WRONG**: "6–8 weeks" / "4 sprints" (calendar range; point estimate)
> **CORRECT**: "3–5 sprints"

---

**[Phase 1 Field 6] Confidence Level + Basis**

State confidence (HIGH / MEDIUM / LOW) and name what IS established.

> **WRONG**: "Confidence: MEDIUM" (no basis)
> **CORRECT**: "MEDIUM — the integration points are enumerated and the existing auth API contract is stable; no spike has been run on webhook delivery behavior."

The basis names what IS verified. What is NOT verified goes to Phase 2. Do not merge them here.

---

**[Phase 1 Field 7] Inertia Check**

Name the workaround and state the cost direction: cheaper / comparable / more expensive to build vs. maintain.

> **WRONG**: "Teams use spreadsheets today." (no cost direction)
> **CORRECT**: "Manual CSV export per team — building is cheaper long-term; spreadsheet maintenance costs grow linearly with team count."

---

**[Phase 1 Field 8] Tier-Up Sensitivity [must resolve to a tier HIGHER than your assigned tier]**

One specific, named, falsifiable condition. State the destination tier explicitly.

> **WRONG**: "Tier rises to HIGH if the project expands." (not falsifiable)
> **CORRECT**: "Tier rises to XL if real-time sync is required — confirm by reviewing the product spec with the PM."

---

**[Phase 1 Field 9] Tier-Down Sensitivity [must resolve to a tier LOWER than your assigned tier]**

One specific, named, falsifiable condition. Destination tier must differ from current tier.

> **WRONG**: "Tier drops to MEDIUM if things are simpler." (not falsifiable; no named condition)
> **CORRECT**: "Tier drops to MEDIUM if the legacy layer exposes a documented webhook API — confirm by reading the auth team's API reference."

---

**[Phase 1 Field 10] Confidence Calibration**

What investigation result would materially raise or lower confidence?

---

**Phase 1 complete. Stop. Proceed to Phase 2.**

---

## Phase 2 — Risk Assessor

**Charter — you own one field only: Confidence Gap.**

You do not produce any Phase 1 fields.

**Non-access rule — named categories + falsifiability gate:**

The Sizing Analyst confirmed the following categories of content in Phase 1. You are prohibited from naming any of these as the gap:

- **Integration points** the Analyst enumerated as the surface area
- **API contract status** the Analyst confirmed as stable
- **Complexity tier drivers** the Analyst named
- **Team and timeline signals** the Analyst established

**Falsifiability gate**: Before writing the gap, ask: "Could a reader derive this gap from the Phase 1 output alone — because it negates something the Analyst already confirmed?" If yes, it is a restatement. Start over.

> **WRONG**: Phase 1 confirmed "auth API contract is stable." Gap = "The auth API contract has not been verified." (Derivable from Phase 1 by negation — restatement, not a gap. Charter violation.)
>
> **CORRECT**: Phase 1 confirmed "auth API contract is stable." Gap = "Rate-limiting behavior of the auth API under sustained concurrent load is undocumented — if the limit is below the expected event volume, a backpressure mechanism becomes a required integration point, raising surface area and tier." (Independent dimension — a reader cannot derive this from Phase 1.)

**[Phase 2 Field 11] Confidence Gap**

Name the specific thing NOT yet known or verified. This must be a dimension the Sizing Analyst did not establish — a new uncertainty, not a negation of Phase 1 facts.

Format: `Gap: [specific named unknown] — [why it matters to the sizing]`

---

## Output Compilation

Produce the complete signal as:

**SIZING SIGNAL — [feature]**

| Field | Phase | Value |
|-------|-------|-------|
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier | 1 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal | 1 | [N–M sprints] |
| Confidence Level + Basis | 1 | [LEVEL — what is established] |
| Inertia Check | 1 | [workaround — cost direction — reasoning] |
| Tier-Up Sensitivity | 1 | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | 1 | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | 1 | [what would raise or lower confidence] |
| Confidence Gap | 2 | [specific named unknown — why it matters] |

The Phase column is informational — it shows which role produced each value. Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-03 — Axis: Role-Tagged Column Headers (C-23 via Structural Encoding)

**Variation axis**: Output format (structural encoding — role ownership embedded in column headers)
**Hypothesis**: C-23 requires every field to appear in exactly one role's charter. The charter document is prose — it can be skimmed or bypassed. Encoding role ownership directly in the output skeleton's column headers makes ownership a structural fact observable at field-production time: when the model fills a cell, the column header names the role responsible. This is a C-18/C-22-style architectural technique applied to C-23: instead of a prose charter saying "Phase 1 owns surface area," the table column says "[Sizing Analyst]" and the model fills it in that context. C-24 is handled by naming prohibited categories in the Confidence Gap column header itself, so the prohibition is active at the moment the gap cell is produced.

---

You are running a **scout-size** sizing signal. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

The output is two structured tables. Fill them in role order: complete the **Sizing Analyst** table entirely before producing the **Risk Assessor** table.

---

## Sizing Analyst Table

Fill each cell. Constraints are in the column headers.

### Surface Area

| Integration Point [name each individually — no general descriptions] | Type |
|----------------------------------------------------------------------|------|
| | [API / hook / event / DB / UI / service / other] |
| | |
| **Total** | **[N] integration points** |

The Total row is required. "Several API interactions" is not a named integration point.

---

### Complexity

| Tier [exactly one: LOW / MEDIUM / HIGH / XL — no other vocabulary] | Primary Driver [1–2 named factors — "it's complex" fails] |
|--------------------------------------------------------------------|-----------------------------------------------------------|
| | |

---

### Team-Size Signal

| Specialist Discipline [name the role — not just "engineer"] | FTE Fraction |
|-------------------------------------------------------------|--------------|
| | |
| **Total** | |

"2 engineers" fails. Name the discipline.

---

### Timeline Signal

| Sprint Range [N–M format — not a calendar date, not a single number] |
|----------------------------------------------------------------------|
| |

---

### Confidence — Sizing Analyst produces: Level, Basis, Inertia, Tier Sensitivity, Calibration

| Field [Sizing Analyst] | Value |
|------------------------|-------|
| Confidence Level [HIGH / MEDIUM / LOW] | |
| Confidence Basis [what IS established — name the specific dimension] | |
| Inertia Check [name the workaround — state: building is cheaper / comparable / more expensive than maintaining — one-sentence reasoning] | |
| Tier-Up Sensitivity [Tier rises to \_\_ — must be HIGHER than your assigned tier: fill with HIGH or XL] if [single named falsifiable condition — name what action would confirm it] | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [Tier drops to \_\_ — must be LOWER than your assigned tier: fill with LOW or MEDIUM] if [single named falsifiable condition — name what action would confirm it] | Tier drops to [ ] if [ ] |
| Confidence Calibration [what investigation result would materially raise or lower confidence] | |

Sensitivity notes:
- "Tier rises to HIGH if scope grows" fails — not falsifiable; "scope grows" is not a condition.
- "Tier drops to MEDIUM if the integration is simpler than expected" fails — not falsifiable; name what action would settle it.
- Destination tier must differ from the tier assigned above — a tier that maps to itself is vacuous.

---

**Sizing Analyst table complete. Proceed to Risk Assessor table.**

---

## Risk Assessor Table

The Risk Assessor owns exactly one field: Confidence Gap.

> ⛔ **WRONG gap** — derivable from Sizing Analyst output by negation:
> Basis = "Auth API contract is stable." Gap = "Auth API contract has not been confirmed." (Same dimension, opposite polarity — restatement, not a gap. Charter violation.)
>
> ✅ **CORRECT gap** — names a dimension the Sizing Analyst did not establish:
> Basis = "Auth API contract is stable." Gap = "Rate-limiting behavior of the auth API under concurrent load is undocumented — sustained event volume may trigger throttling that becomes a required integration point."

| Confidence Gap [Phase 2: Risk Assessor — PROHIBITED: do not cite integration points the Analyst enumerated, API contract status the Analyst confirmed, complexity drivers the Analyst named, team/timeline signals the Analyst established — name a dimension Phase 1 did not reach] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

---

**Signal boundary check**: Review both tables. Remove any task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-04 — Axis: Reversed Role Sequence + Complete Charter Enumeration

**Variation axis**: Role sequence (Risk Assessor runs Phase 1; Sizing Analyst runs Phase 2) + complete charter enumeration (C-23)
**Hypothesis**: In the standard V-03/V-01 sequence, the Sizing Analyst runs first and produces a rich basis. The Risk Assessor then operates under anchoring pressure — the basis frame is already established, making it easier to produce a gap that contrasts the basis rather than identifies a genuinely new dimension. Reversing the sequence liberates the gap from the basis frame: the Risk Assessor names what is unknown before the Analyst has named what is known. The Analyst's non-access rule then applies in the opposite direction — the Analyst cannot frame the Phase 1 gap dimension as the confidence basis. C-23 is satisfied by fully enumerating both charters: Phase 1 owns exactly one field (Confidence Gap); Phase 2 owns exactly ten fields (listed by name). C-24 is satisfied by the Sizing Analyst's non-access rule, which names the content category Phase 1 identified as the dynamic prohibition source.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one, no substitutions.

Two phases. Complete Phase 1 entirely before reading Phase 2.

---

## Phase 1 — Risk Assessor

**Charter — you OWN this field and produce it here:**
- Confidence Gap

**Charter — you do NOT produce these fields (they belong to Phase 2):**
Surface Area, Complexity Tier, Primary Complexity Driver, Team-Size Signal, Timeline Signal, Confidence Level + Basis, Inertia Check, Tier-Up Sensitivity, Tier-Down Sensitivity, Confidence Calibration.

Your sole task: name the primary source of residual uncertainty for this feature. What is NOT yet known or verified that matters to sizing?

Rules:
- Name a specific unverified dimension — not a generic hedge ("we don't know everything")
- Do not produce a status update on something already established — a gap names what investigation has not yet reached
- State it as: `Gap: [specific unknown] — [why it matters to the sizing estimate]`

> **WRONG**: "The technical feasibility of the integration has not been confirmed." (Generic — doesn't name a specific dimension)
> **WRONG**: "The API contract has not been confirmed." (If the API contract is a known baseline, this is a status note — it names what should be confirmed, not what is specifically uncertain)
> **CORRECT**: "Gap: Event deduplication behavior under concurrent webhook delivery is unverified — if the integration layer does not guarantee idempotency, a separate deduplication store becomes a required integration point, expanding surface area and potentially shifting the tier."

**Your Confidence Gap:**

---

**Phase 1 complete. Proceed to Phase 2.**

---

## Phase 2 — Sizing Analyst

**Charter — you OWN these fields and produce them here:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Inertia Check (workaround named, cost direction stated)
8. Tier-Up Sensitivity (single named falsifiable condition → explicit tier destination)
9. Tier-Down Sensitivity (single named condition → explicit tier destination)
10. Confidence Calibration (what would raise or lower confidence)

**Charter — you do NOT produce**: Confidence Gap (owned by Phase 1).

**Non-access rule — named category**: The Risk Assessor in Phase 1 named a specific unverified dimension. You are prohibited from confirming that same dimension as established in your Confidence Basis. If Phase 1 identified "event deduplication behavior under concurrent webhook delivery" as the gap, your Confidence Basis must name a different dimension — the integration points, the API contract, the team's familiarity with the stack. You may not state "event deduplication behavior is established" as your basis when Phase 1 named it as the gap.

> **WRONG**: Phase 1 gap = "event deduplication under concurrent load is unverified." Phase 2 basis = "event deduplication semantics are established." (Same dimension, opposite polarity — the basis colonizes the gap.)
> **CORRECT**: Phase 1 gap = "event deduplication under concurrent load is unverified." Phase 2 basis = "Surface area is bounded — three stable API endpoints with documented schemas; team has delivered two prior webhook integrations." (Gap and basis address genuinely different dimensions.)

---

### 2.1 Surface Area

Named integration points + total count. Count is mandatory.

> **WRONG**: "The feature touches a few API layers." (no named points, no count)
> **CORRECT**: "Auth API endpoint, event-bus subscription (user-created), DB schema migration — **3 integration points**"

**Your output:**

---

### 2.2 Complexity Tier

Exactly one: **LOW / MEDIUM / HIGH / XL**

**Tier:**

**Primary complexity driver** [1–2 named factors — not "it's complex"]:

---

### 2.3 Team-Size Signal

Disciplines + fractions. Not headcount alone.

> **WRONG**: "2–3 engineers"
> **CORRECT**: "1 backend engineer, 0.5 platform engineer, 0.5 PM"

**Your output:**

---

### 2.4 Timeline Signal

Sprint range. Not a calendar date. Not a single number.

> **CORRECT**: "3–5 sprints"

**Your output:**

---

### 2.5 Confidence Level + Basis

State confidence (HIGH / MEDIUM / LOW) and name what IS established. Your basis must address a different dimension than the Phase 1 gap.

> **CORRECT**: "MEDIUM — surface area is enumerated across three stable API endpoints; team has delivered two prior webhook integrations. [Basis addresses surface area and team familiarity — a different dimension than Phase 1's gap about deduplication semantics.]"

**Your output:**

---

### 2.6 Inertia Check

Name the workaround + cost direction.

> **WRONG**: "Teams use a manual process." (no cost direction)
> **CORRECT**: "Manual CSV export per team — building is cheaper long-term; overhead grows with team count at ~45 min/sprint/team."

**Your output:**

---

### 2.7 Tier-Up Sensitivity [destination must be HIGHER than your assigned tier]

One named falsifiable condition. Destination tier stated explicitly. Must differ from current tier.

> **WRONG**: "Tier rises if scope expands." (not falsifiable)
> **CORRECT**: "Tier rises to XL if real-time sync support is required — confirm by reviewing the product spec's sync requirements section with the PM."

**Your output: Tier rises to [\_\_] if:**

---

### 2.8 Tier-Down Sensitivity [destination must be LOWER than your assigned tier]

One named falsifiable condition. Destination tier stated explicitly. Must differ from current tier.

> **WRONG**: "Tier drops if the integration is straightforward." (not falsifiable)
> **CORRECT**: "Tier drops to MEDIUM if the legacy auth layer exposes a documented event-hook API — confirm by reading the auth team's current API reference."

**Your output: Tier drops to [\_\_] if:**

---

### 2.9 Confidence Calibration

What investigation result would materially raise or lower the confidence level?

**Your output:**

---

## Output Compilation

**SIZING SIGNAL — [feature]**

| Field | Value |
|-------|-------|
| Surface Area | [named points — N integration points] |
| Complexity Tier | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | [1–2 named factors] |
| Team-Size Signal | [disciplines + fractions] |
| Timeline Signal | [N–M sprints] |
| Confidence Level + Basis | [LEVEL — what is established] |
| Confidence Gap | [from Phase 1 — specific named unknown] |
| Inertia Check | [workaround — cost direction — reasoning] |
| Tier-Up Sensitivity | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | [what would raise or lower confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

---

## V-05 — Combined: Three-Phase + Inertia-First + Full Charter + Named Prohibition + Table Encoding

**Variation axis**: Inertia framing + role sequence + structural encoding (combined)
**Hypothesis**: Four mechanisms converge: (1) Phase 0 elevates inertia analysis from a section to a gate — the feature must be compared against its alternative before sizing begins, making the cost-of-not-building primary rather than supplementary; (2) three-phase charter enumeration satisfies C-23 without ambiguity — Phase 0 owns exactly one field, Phase 1 owns nine fields, Phase 2 owns one field, all enumerated by name; (3) the Phase 2 prohibition names the specific content categories Phase 1 is expected to confirm (integration points, API contracts, complexity drivers, team/timeline signals), making C-24 falsifiable at the role level; (4) table format with role-tagged column headers makes field ownership structural rather than prose-only. Combining these mechanisms means no single mechanism failure causes a C-23 or C-24 miss — the structural encoding backs up the charter prose.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

Three phases. Complete each phase entirely before reading the next.

---

## Phase 0 — Inertia Analyst

**Charter — you OWN**: Inertia Check (exactly one field)
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level + Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

The cost of building this feature must be compared against the cost of NOT building it before sizing begins. Sizing without the inertia check produces a build estimate in isolation — it cannot tell you whether the effort is worthwhile.

Name the current workaround and state the cost direction.

> **WRONG**: "Teams manually export CSVs." (workaround named; cost direction absent)
> **CORRECT**: "Manual CSV export + re-import per team — building is cheaper long-term; the workaround requires ~45 min/sprint/team and that overhead grows linearly with team count."

| Inertia Check [Phase 0: Inertia Analyst — name the workaround AND state: building is cheaper / comparable / more expensive than maintaining] |
|---|
| [Workaround] — building is [cheaper / comparable / more expensive] than maintaining. [One-sentence reasoning.] |

---

**Phase 0 complete. Proceed to Phase 1.**

---

## Phase 1 — Sizing Analyst

**Charter — you OWN these nine fields:**
1. Surface Area
2. Complexity Tier
3. Primary Complexity Driver
4. Team-Size Signal
5. Timeline Signal
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**Charter — you do NOT produce**: Inertia Check (owned by Phase 0) or Confidence Gap (owned by Phase 2).

Fill the following tables in order.

---

### Surface Area Table [Phase 1: Sizing Analyst]

| Integration Point [name individually — no general descriptions] | Type [API / hook / event / DB / UI / service / other] |
|-----------------------------------------------------------------|------------------------------------------------------|
| | |
| | |
| **Total** | **[N] integration points** |

The Total row is required. A row entry of "several API layers" fails — name the specific point.

---

### Complexity Table [Phase 1: Sizing Analyst]

| Tier [exactly one: LOW / MEDIUM / HIGH / XL] | Primary Complexity Driver [1–2 named factors — "it's complex" fails] |
|----------------------------------------------|----------------------------------------------------------------------|
| | |

---

### Team-Size Table [Phase 1: Sizing Analyst]

| Specialist Discipline [name the role] | FTE Fraction |
|---------------------------------------|--------------|
| | |
| **Total FTEs** | |

"2 engineers" fails — name the discipline.

---

### Timeline Table [Phase 1: Sizing Analyst]

| Sprint Range [N–M format — not calendar date, not single number] |
|------------------------------------------------------------------|
| |

---

### Confidence + Sensitivity Table [Phase 1: Sizing Analyst]

| Field [Phase 1: Sizing Analyst] | Value |
|--------------------------------|-------|
| Confidence Level [HIGH / MEDIUM / LOW] | |
| Confidence Basis [what IS established — name the specific dimension; do NOT address the gap dimension Phase 2 will identify] | |
| Tier-Up Sensitivity [Tier rises to \_\_ — must be HIGHER than assigned tier: HIGH or XL] if [single named falsifiable condition — name what action confirms it] | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity [Tier drops to \_\_ — must be LOWER than assigned tier: LOW or MEDIUM] if [single named falsifiable condition — name what action confirms it] | Tier drops to [ ] if [ ] |
| Confidence Calibration [what investigation result would raise or lower confidence] | |

Sensitivity constraint notes:
- Each condition must be a single named scenario — not a list, not a hedge.
- Destination tier must differ from the currently assigned tier. A tier rising to itself is vacuous.
- Falsifiability: "if scope grows" and "if things are simpler" are deferrals, not conditions. Name what a teammate would actually investigate.

> **WRONG tier-up**: "Tier rises to HIGH if complexity increases." (not falsifiable; destination already assigned above if current = HIGH)
> **CORRECT tier-up**: "Tier rises to XL if the offline-sync requirement is confirmed — check PRD offline-sync section with PM."
>
> **WRONG tier-down**: "Tier drops to LOW if the integration is simpler than anticipated." (not falsifiable)
> **CORRECT tier-down**: "Tier drops to MEDIUM if the legacy auth layer exposes a documented event-hook API — read auth team's API reference."

---

**Phase 1 complete. Proceed to Phase 2.**

---

## Phase 2 — Risk Assessor

**Charter — you OWN**: Confidence Gap (exactly one field)
**Charter — you do NOT produce**: Inertia Check (Phase 0), Surface Area, Complexity Tier, Primary Driver, Team-Size, Timeline, Confidence Basis, Tier Sensitivities, Confidence Calibration (Phase 1).

**Non-access rule — named category prohibition + falsifiability gate:**

The Sizing Analyst confirmed the following categories of content in Phase 1. You are explicitly prohibited from citing any of these as the gap:

- **Integration points** the Sizing Analyst named and enumerated
- **API contract status** the Sizing Analyst confirmed as established
- **Complexity tier drivers** the Sizing Analyst identified
- **Team and timeline signals** the Sizing Analyst produced

**Falsifiability gate**: Before writing the gap, ask: "If a reader looked only at the Phase 1 output, could they derive my gap by negating something the Analyst confirmed?" If yes — that is a restatement and a charter violation.

> ⛔ **WRONG gap** (charter violation):
> Phase 1 confirmed: "Auth API contract is stable — established baseline."
> Gap = "Auth API contract has not been verified." ← Same dimension, negated. A reader derives this directly from Phase 1 by negation.
>
> ✅ **CORRECT gap** (new dimension Phase 1 did not reach):
> Phase 1 confirmed: "Auth API contract is stable — three endpoints with documented schemas."
> Gap = "Auth API rate-limiting behavior under sustained concurrent event load is undocumented — if the rate limit is below the expected event volume, a backpressure or queuing layer becomes a required integration point, expanding surface area and potentially shifting the tier."
> ← Independent dimension. A reader cannot derive this from Phase 1.

| Confidence Gap [Phase 2: Risk Assessor — PROHIBITED categories: integration points Analyst enumerated, API contract status Analyst confirmed, complexity drivers Analyst named, team/timeline signals Analyst established — gap must name a dimension Phase 1 did not reach; verify it is not derivable from Phase 1 by negation before writing] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

---

## Output Compilation

After completing all three phases, produce the final Sizing Signal:

**SIZING SIGNAL — [feature]**

| Field | Phase | Value |
|-------|-------|-------|
| Inertia Check | 0 | [workaround — cheaper / comparable / more expensive — reasoning] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier | 1 | [LOW / MEDIUM / HIGH / XL] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal | 1 | [N–M sprints] |
| Confidence Level + Basis | 1 | [LEVEL — what is established] |
| Tier-Up Sensitivity | 1 | Tier rises to [LEVEL] if [single named falsifiable condition] |
| Tier-Down Sensitivity | 1 | Tier drops to [LEVEL] if [single named falsifiable condition] |
| Confidence Calibration | 1 | [what would raise or lower confidence] |
| Confidence Gap | 2 | [specific named unknown — why it matters] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates anywhere in this output.

---

```json
{
  "skill": "scout-size",
  "round": 8,
  "rubric": "v8",
  "variations": 5,
  "new_criteria_targeted": ["C-23", "C-24"],
  "baseline_maintained": "C-01 through C-22",
  "axes": {
    "V-01": "charter-completeness-explicit-field-lists",
    "V-02": "named-category-prohibition-with-falsifiability-gate",
    "V-03": "role-tagged-column-headers-structural-C23",
    "V-04": "reversed-role-sequence-gap-first-complete-charters",
    "V-05": "three-phase-inertia-first-full-charter-named-prohibition-table-encoding"
  },
  "c23_mechanism": {
    "V-01": "prose charter lists all 10 Phase 1 fields by name + Phase 2 exclusion list",
    "V-02": "field-level [Phase N Field N] labels in each section header",
    "V-03": "column headers tag role ownership for every table column",
    "V-04": "Phase 1 charter lists 1 field + 10 exclusions; Phase 2 charter lists 10 fields + 1 exclusion",
    "V-05": "three charters enumerate all 11 fields across three roles; column headers back up prose"
  },
  "c24_mechanism": {
    "V-01": "Phase 2 prohibition names 4 content categories (integration points, API contracts, complexity drivers, team/timeline signals)",
    "V-02": "Phase 2 prohibition names 4 categories + falsifiability gate (cannot derive from Phase 1 by negation)",
    "V-03": "Gap column header names 4 prohibited categories inline at production point",
    "V-04": "Phase 2 (Sizing Analyst) prohibition dynamically references the specific dimension Phase 1 identified; names content class",
    "V-05": "Phase 2 prohibition names 4 categories + falsifiability gate; column header names all 4 categories at production point"
  }
}
```
