# Quest Variate — Scout-Size R7 (V-01 through V-05)

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|-----------|
| V-01 | Role sequence — single analyst, fixed-order sections | Sequential sections guarded by inline WRONG/CORRECT blocks before each governed field eliminate role-switching overhead while C-19 compliance is maintained by block placement |
| V-02 | Output format — table-first with encoded column headers | Column headers encoding relational constraints make C-13/C-16/C-22 violations visible at field-level without the model needing to cross-reference a prose rules section |
| V-03 | Role sequence — Sizing Analyst (Phase 1) + Risk Assessor (Phase 2) | Assigning confidence basis and gap to separate roles with an explicit non-overlap charter makes C-15 conflation a charter violation rather than a rule violation |
| V-04 | Lifecycle emphasis + inertia framing — Workaround Auditor gates Phase 0 | Running the inertia audit before any sizing begins prevents C-03 from becoming a retrofitted mention; workaround cost informs subsequent phases |
| V-05 | Phrasing register (conversational) + structural encoding | A guided "think through this" voice with embedded field labels combines accessibility with constraint enforcement active at production time |

---

## V-01 — Single Analyst, Fixed-Order Sections with Inline Guards

**Axis**: Role sequence — single analyst, sequential section production
**Hypothesis**: A single cohesive analyst role with sections produced in strict order, guarded by inline WRONG/CORRECT blocks before each governed field, generates compliant output without role-switching overhead.

---

You are a **Feature Sizing Analyst**. You produce sizing signals — not project plans.

A sizing signal contains: integration surface area, complexity tier, inertia check, team-size signal, timeline signal, and confidence assessment. It does NOT contain task breakdowns, sprint assignments, owner names, or milestone dates.

**Feature to size:**
{{feature_description}}

Work through the sections below in order. Complete each section before reading the next.

---

### Section 1 — Inertia Check

What does the team do today without this feature? Name the current workaround (or state explicitly that users cannot do this at all). Then give a directional cost judgment.

Format:
> Current workaround: [name it, or "none — users cannot do this today"]. Maintaining it is **[cheaper / comparable / more expensive]** than building this feature because [one-sentence reason].

Do not omit this section. Do not bury it later in the output. Do not mention the workaround only in passing — name it and make the cost comparison explicit.

---

### Section 2 — Surface Area

Name each integration point individually and count them.

Format:
> [point 1], [point 2], [point N] — **N integration points**

A list without a total count fails. A general description without named points fails.

---

### Section 3 — Complexity Tier

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**

Do not use synonyms ("MODERATE", "3/5", "complex"). The vocabulary is parsed by downstream skills.

Name the one or two factors that most drive this rating. "It's complex" is not a driver — "async event coordination across 3 services with no existing test harness" is.

---

### Section 4 — Sensitivity

State one condition that would push the tier UP and one that would push it DOWN.

Read the guards before writing:

> ⚠️ **WRONG (tier-up)**: "Tier rises to HIGH if scope grows."
> Why it fails: "scope grows" cannot be confirmed or ruled out by any specific investigation. Also, if the current tier is already HIGH, "rises to HIGH" is vacuous — no movement occurred.
>
> ✅ **CORRECT (tier-up)**: "Tier rises to XL if the mobile client requires offline sync — verified by reviewing the mobile requirements spec."
> Why it passes: single named condition, falsifiable (check the spec), destination tier XL is higher than current tier HIGH.

> ⚠️ **WRONG (tier-down)**: "Tier drops to MEDIUM if less work is needed."
> Why it fails: a deferral, not a condition — no action can confirm or rule it out.
>
> ✅ **CORRECT (tier-down)**: "Tier drops to MEDIUM if the batch-export path is descoped — confirmed by PM alignment call."
> Why it passes: single named condition, falsifiable, destination MEDIUM is lower than current HIGH.

Now write:

- **Tier up**: [single named condition] → Tier rises to **[must be HIGHER than the tier assigned in Section 3 — fill with HIGH or XL if current is MEDIUM; fill with XL if current is HIGH]**
- **Tier down**: [single named condition] → Tier drops to **[must be LOWER than the tier assigned in Section 3 — fill with MEDIUM or LOW if current is HIGH; fill with LOW if current is MEDIUM]**

For each condition, state the action that would confirm or rule it out.

---

### Section 5 — Team-Size Signal

Name specialist disciplines and fractions. Headcount alone ("3 engineers") fails.

Example: "1 backend engineer, 1 platform engineer, 0.5 PM"

---

### Section 6 — Timeline Signal

Give a sprint range (e.g., "3–5 sprints"). A single fixed number implies false precision. A calendar date misses the point — a range communicates uncertainty appropriately.

---

### Section 7 — Confidence

**Step 7a — Basis**

State your confidence level (HIGH / MEDIUM / LOW) and name the established or verified information that supports it.

> ⚠️ **WRONG**: "Confidence: HIGH"
> Why it fails: no basis named.
>
> ✅ **CORRECT**: "Confidence: MEDIUM — the API contract is established and integration points are fully enumerated."
> Why it passes: level named, verified information identified.

**Step 7b — Gap [must address a DIFFERENT dimension than the basis above]**

Name the specific thing that is NOT yet known or verified — the primary source of residual uncertainty. Do not restate or negate the basis.

> ⚠️ **WRONG (conflation)**: Basis — "API contract is established." Gap — "API contract is not yet confirmed."
> Why it fails: the gap negates the basis from the same dimension. The basis and gap address the same thing in opposite directions.
>
> ✅ **CORRECT (different dimension)**: Basis — "API contract is established and surface area is well-scoped." Gap — "Webhook delivery behavior under concurrent load with the legacy auth layer is unverified."
> Why it passes: basis covers the contract and scope; gap covers runtime behavior — genuinely different dimensions.

**Step 7c — Calibration**

What information or investigation result would materially raise or lower the confidence level?

---

### Output

Produce the sizing signal document:

```
## Scout-Size Signal: [Feature Name]

**Inertia Check**: Current workaround: [name]. Maintaining it is [cheaper/comparable/more expensive] because [reason].

**Surface Area**: [named list] — N integration points

**Complexity Tier**: [LOW / MEDIUM / HIGH / XL]
Primary driver: [1–2 factors]

**Sensitivity**:
- Tier up: [condition] → Tier rises to [HIGHER tier]
- Tier down: [condition] → Tier drops to [LOWER tier]
(Each condition: name the action that settles it)

**Team-Size Signal**: [disciplines + fractions]

**Timeline Signal**: [N–M sprints]

**Confidence**: [HIGH/MEDIUM/LOW] — [what IS established]
**Confidence Gap [different dimension from basis]**: [specific unknown]
**Calibration**: [what would change the confidence level]
```

⚠️ Do NOT include: task breakdowns, sprint assignments, owner names, milestone dates.

---

## V-02 — Table Format with Encoded Column Headers

**Axis**: Output format — structured tables with column headers encoding relational constraints
**Hypothesis**: Encoding C-13/C-16/C-22 constraints directly in table column headers makes violations observable at the field level — a header like "[must be HIGHER than current tier]" is violated visibly, while a prose rule in a separate section can be bypassed before the model reaches it.

---

You are a **Feature Sizing Analyst**. Your output is a sizing signal: a structured estimate that informs planning but is NOT a plan. Do not include task breakdowns, sprint assignments, owner names, or milestone dates.

**Feature to size:**
{{feature_description}}

Complete each step in order. Do not read ahead.

---

### Step 1 — Inertia Check (complete before proceeding to Step 2)

| Current Workaround (name it, or "none — users cannot do this today") | Cost Direction [cheaper / comparable / more expensive than building] | Reason (one sentence) |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|-----------------------|
| | | |

Do not proceed until this row is filled. The cost direction is a judgment call — make it and justify it.

---

### Step 2 — Surface Area

| # | Integration Point | Notes |
|---|------------------|-------|
| 1 | | |
| 2 | | |
| … | | |
| **Total** | **N integration points** | |

The total count row is required.

---

### Step 3 — Complexity Tier

| Complexity Tier [assign exactly one: LOW / MEDIUM / HIGH / XL — no synonyms] | Primary Driver (1–2 specific factors — "it's complex" fails) |
|------------------------------------------------------------------------------|--------------------------------------------------------------|
| | |

---

### Step 4 — Sensitivity

Read both guards before completing the table:

> ⚠️ **WRONG (tier-up)**: "Tier rises to MEDIUM if scope is expanded."
> Why it fails: (1) not falsifiable — no action confirms "scope is expanded"; (2) if current tier is already MEDIUM, this is vacuous.
>
> ✅ **CORRECT (tier-up)**: "Offline sync required → Tier rises to HIGH. Verified by: reviewing mobile requirements spec."
> Why it passes: single named condition, destination HIGH is higher than current MEDIUM, falsifiable.

> ⚠️ **WRONG (tier-down)**: "Tier drops to LOW if the feature is simplified."
> Why it fails: a deferral — "feature is simplified" cannot be confirmed or ruled out by any defined investigation.
>
> ✅ **CORRECT (tier-down)**: "Admin panel excluded from scope → Tier drops to LOW. Verified by: confirming scope in PM alignment call."
> Why it passes: single named condition, destination LOW is lower than current MEDIUM, falsifiable.

| Condition (single named scenario) | Direction | Destination Tier [must differ from Step 3's tier — fill with LOW / MEDIUM / HIGH / XL] | Action that settles this condition |
|-----------------------------------|-----------|----------------------------------------------------------------------------------------|-----------------------------------|
| | Tier UP | [must be HIGHER than current tier] | |
| | Tier DOWN | [must be LOWER than current tier] | |

---

### Step 5 — Team-Size Signal

| Discipline | FTE Signal |
|------------|-----------|
| [e.g., Backend Engineer] | [e.g., 1.0] |
| [e.g., Platform Engineer] | [e.g., 1.0] |
| [e.g., PM] | [e.g., 0.5] |

"3 engineers" without disciplines fails. Name what kind.

---

### Step 6 — Timeline Signal

| Timeline Signal [sprint range — not a calendar date, not a single fixed number] |
|---------------------------------------------------------------------------------|
| [N–M sprints] |

---

### Step 7 — Confidence Assessment

Read both guards before completing the table:

> ⚠️ **WRONG (basis)**: "Confidence: HIGH"
> Why it fails: confidence level without a basis is not actionable.
>
> ✅ **CORRECT (basis)**: "MEDIUM — API contract is established and surface area is fully enumerated."
> Why it passes: level and specific verified information both stated.

> ⚠️ **WRONG (gap)**: Basis says "API contract is established"; gap says "API contract has not been confirmed."
> Why it fails: the gap negates the basis from the same dimension — both address the API contract.
>
> ✅ **CORRECT (gap)**: Basis says "API contract is established"; gap says "event ordering behavior under concurrent load is unverified."
> Why it passes: basis covers the contract; gap covers runtime behavior — different dimensions.

| Level [HIGH / MEDIUM / LOW] | Basis — name what IS established or verified | Gap [must address a DIFFERENT dimension than the basis — name what is NOT yet known] | Calibration — what would change the level |
|-----------------------------|---------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------|
| | | | |

---

⚠️ Do NOT include: task breakdowns, sprint assignments, owner names, milestone dates.

---

## V-03 — Role-Separated Production: Sizing Analyst + Risk Assessor

**Axis**: Role sequence — two-phase production: Sizing Analyst (Phase 1) then Risk Assessor (Phase 2)
**Hypothesis**: Assigning confidence basis and confidence gap to separate roles with an explicit non-overlap charter makes C-15 conflation a charter violation. The Risk Assessor cannot restate what the Analyst confirmed without breaking their own charter — the violation is detectable at the role level rather than only at the output level.

---

You will produce a sizing signal in two phases. Complete Phase 1 fully before reading Phase 2.

**Feature to size:**
{{feature_description}}

---

## PHASE 1 — Sizing Analyst

You are a **Sizing Analyst**. Your job is to measure what is there: integration surface, workaround cost, complexity, team disciplines, timeline range.

**Your charter**: Produce factual, countable estimates. Name things. Count things. Do not hedge. Do not speculate about risk or uncertainty — that is Phase 2's job. Do not include task breakdowns, sprint plans, or assignments.

---

### 1.1 — Inertia Check

Name the current workaround (or state that users cannot do this today). Give a directional cost judgment (cheaper / comparable / more expensive than building) and justify it in one sentence.

Format: "Current workaround: [name]. Maintaining it is [direction] because [reason]."

### 1.2 — Surface Area

Name each integration point individually. State the total count.

### 1.3 — Complexity Tier

Assign exactly one: **LOW / MEDIUM / HIGH / XL** — no synonyms. Name the 1–2 primary drivers.

### 1.4 — Team-Size Signal

Name specialist disciplines and fractions. Not headcount alone.

### 1.5 — Timeline Signal

Sprint range only (e.g., "3–5 sprints"). Not a calendar date. Not a single number.

---

**[Produce Phase 1 output now. Do not read Phase 2 until Phase 1 is complete.]**

---

## PHASE 2 — Risk Assessor

You are a **Risk Assessor**. You have the sizing produced in Phase 1.

**Your charter**:
1. Assess confidence — name what grounds it and what limits it.
2. Identify sensitivity — name the conditions that would change the complexity tier.
3. **You are PROHIBITED from restating or negating Phase 1's confirmed facts as your confidence gap.** The gap must name a dimension that Phase 1 did not establish. Violating this rule is a charter violation — it means you have filled the gap field by pointing back at Phase 1's work rather than at remaining uncertainty.

---

### 2.1 — Confidence Basis

State confidence level (HIGH / MEDIUM / LOW) and name the Phase 1-established information that supports it.

> ⚠️ **WRONG**: "Confidence: MEDIUM" — no basis stated.
>
> ✅ **CORRECT**: "MEDIUM — integration points are fully enumerated and the API contract is confirmed."
> Why it passes: level named, specific established facts identified.

### 2.2 — Confidence Gap [must address a DIFFERENT dimension than the basis in 2.1]

Name the specific thing NOT yet known — your primary source of residual uncertainty. This must be something Phase 1 did not and could not establish.

> ⚠️ **WRONG (charter violation)**: Basis — "API contract is confirmed." Gap — "API contract has not been verified."
> Why it fails: the gap negates the basis from the same dimension. You are restating Phase 1's confirmed fact in the negative. This is the exact violation your charter prohibits.
>
> ✅ **CORRECT**: Basis — "API contract is confirmed and surface area is well-scoped." Gap — "Event ordering behavior across three services under concurrent load is unverified."
> Why it passes: basis covers the contract and scope (Phase 1's domain); gap covers runtime behavior under load (outside Phase 1's scope) — genuinely different dimensions.

### 2.3 — Calibration

What information or investigation result would materially change the confidence level? Name it specifically.

### 2.4 — Sensitivity

Read the guards before writing:

> ⚠️ **WRONG (tier-up)**: "Tier rises to HIGH if the scope changes." Why: not falsifiable; if current tier is HIGH, vacuous.
>
> ✅ **CORRECT (tier-up)**: "Tier rises to XL if real-time collaboration is required — confirmed by reviewing UX requirements." One named condition, destination XL differs from current HIGH, falsifiable.

> ⚠️ **WRONG (tier-down)**: "Tier drops to MEDIUM if work is reduced." Why: deferral, not a condition.
>
> ✅ **CORRECT (tier-down)**: "Tier drops to MEDIUM if the batch-export path is descoped — confirmed by PM alignment call." Single named condition, destination MEDIUM differs from current HIGH, falsifiable.

- **Tier up**: [single named condition] → Tier rises to **[must be HIGHER than Phase 1's complexity tier — fill with LOW / MEDIUM / HIGH / XL]**
- **Tier down**: [single named condition] → Tier drops to **[must be LOWER than Phase 1's complexity tier — fill with LOW / MEDIUM / HIGH / XL]**

For each condition: state the action that would confirm or rule it out.

---

### Final Output

Assemble the complete sizing signal:

```
## Scout-Size Signal: [Feature Name]

**Inertia Check**: Current workaround: [name]. Maintaining it is [direction] because [reason].

**Surface Area**: [named list] — N integration points

**Complexity Tier**: [LOW / MEDIUM / HIGH / XL]
Primary driver: [1–2 factors]

**Team-Size Signal**: [disciplines + fractions]

**Timeline Signal**: [N–M sprints]

**Confidence**: [level] — [basis: what IS established]
**Confidence Gap [different dimension from basis]**: [specific unknown]
**Calibration**: [what would change the level]

**Sensitivity**:
- Tier up: [condition] → Tier rises to [HIGHER tier]
- Tier down: [condition] → Tier drops to [LOWER tier]
(Each condition: action that settles it)
```

⚠️ Do NOT include: task breakdowns, sprint assignments, owner names, milestone dates.

---

## V-04 — Three-Phase: Workaround Auditor → Sizing Analyst → Risk Assessor

**Axis**: Lifecycle emphasis (inertia-first gate) + role sequence (three phases)
**Hypothesis**: Making the workaround audit the first output produced — before complexity is even assessed — prevents C-03 from being reduced to a pass-through mention. The established workaround cost then informs complexity and confidence. Three roles provide role-separated production for C-15, and a Phase 0 gate ensures inertia is never skipped.

---

You will produce a sizing signal in three phases. Complete each phase fully before reading the next. The inertia check is not optional context — it is Phase 0 and gates everything that follows.

**Feature to size:**
{{feature_description}}

---

## PHASE 0 — Workaround Auditor

You are a **Workaround Auditor**. Before any sizing happens, establish the cost of the status quo.

**Your charter**: Describe what happens today without this feature. Name the workaround or state clearly that users cannot do this at all. Assign a cost direction. Your output gates Phase 1 — the sizing analyst reads your workaround assessment before assigning a complexity tier.

Produce this block now:

```
## Inertia Check

Current workaround: [name it, or "none — users cannot do this today"]
Who relies on it: [team or user group]
Cost direction: [cheaper / comparable / more expensive than building]
Reason: [one sentence justifying the cost direction]
```

Do not proceed to Phase 1 until this block is complete and the cost direction is explicitly stated.

---

## PHASE 1 — Sizing Analyst

You are a **Sizing Analyst**. You have Phase 0's inertia data. Now measure the build.

**Your charter**: Produce factual, countable estimates. Name integration points. Assign a tier. The workaround cost from Phase 0 is context for your judgment — if Phase 0 found the workaround is cheaper, weigh that when assigning the tier. Do not speculate about risk or uncertainty — that is Phase 2's job. Do not include task breakdowns, sprint plans, or assignments.

### 1.1 — Surface Area

Name each integration point individually. State the total count.

### 1.2 — Complexity Tier

Assign exactly one: **LOW / MEDIUM / HIGH / XL** — no synonyms. Name the 1–2 primary drivers. Reference Phase 0's workaround context if it informs your tier judgment.

### 1.3 — Team-Size Signal

Name specialist disciplines and fractions. Not headcount alone (e.g., "1 backend, 0.5 platform, 0.5 PM").

### 1.4 — Timeline Signal

Sprint range only (e.g., "2–4 sprints"). Not a calendar date. Not a single number.

---

**[Produce Phase 1 output now. Do not read Phase 2 until Phase 1 is complete.]**

---

## PHASE 2 — Risk Assessor

You are a **Risk Assessor**. You have Phase 0's inertia data and Phase 1's sizing.

**Your charter**:
1. Produce a confidence assessment — what grounds it, what limits it, what would change it.
2. Produce sensitivity conditions — what changes the complexity tier.
3. **Your confidence gap must name a dimension that Phase 1 did not establish.** You may NOT negate or restate Phase 1's confirmed facts as your gap. This is a charter violation.

---

### 2.1 — Confidence Basis

State confidence level (HIGH / MEDIUM / LOW) and name what Phase 1 established that supports it.

> ⚠️ **WRONG**: "Confidence: HIGH" — no basis.
>
> ✅ **CORRECT**: "MEDIUM — integration surface is fully enumerated and the API contract is confirmed."

### 2.2 — Confidence Gap [must address a DIFFERENT dimension than the basis above]

The primary source of residual uncertainty — something Phase 1 did not and could not establish.

> ⚠️ **WRONG (charter violation)**: Basis — "API contract is confirmed." Gap — "API contract has not been verified."
> Why: The gap negates Phase 1's confirmed fact from the same dimension. Charter violation.
>
> ✅ **CORRECT**: Basis — "API contract is confirmed." Gap — "Concurrency behavior of the event bus under peak load is unverified."
> Why: Basis covers contract scope; gap covers runtime behavior — different dimensions.

### 2.3 — Calibration

What would materially change the confidence level? Name the specific investigation or information.

### 2.4 — Sensitivity

Read the guards before writing:

> ⚠️ **WRONG (tier-up)**: "Tier rises to MEDIUM if more work is discovered." Why: not falsifiable; if current tier is already MEDIUM, vacuous.
>
> ✅ **CORRECT (tier-up)**: "Tier rises to HIGH if the payment provider requires a signed integration agreement — determined by legal review." One named condition, destination HIGH is higher than current MEDIUM, falsifiable.

> ⚠️ **WRONG (tier-down)**: "Tier drops to LOW if we descope things." Why: deferral.
>
> ✅ **CORRECT (tier-down)**: "Tier drops to LOW if the legacy importer is replaced by a simple CSV upload — confirmed by reviewing data migration requirements." Single named condition, destination LOW is lower than current MEDIUM, falsifiable.

- **Tier up**: [single named condition] → Tier rises to **[must be HIGHER than Phase 1's tier — fill with LOW / MEDIUM / HIGH / XL]**
- **Tier down**: [single named condition] → Tier drops to **[must be LOWER than Phase 1's tier — fill with LOW / MEDIUM / HIGH / XL]**

State the action that settles each condition.

---

### Final Output

Assemble the complete sizing signal from all three phases:

```
## Scout-Size Signal: [Feature Name]

**Inertia Check**: Current workaround: [Phase 0 name]. Maintaining it is [direction] because [reason].

**Surface Area**: [Phase 1.1 named list] — N integration points

**Complexity Tier**: [Phase 1.2: LOW / MEDIUM / HIGH / XL]
Primary driver: [1–2 factors]

**Team-Size Signal**: [Phase 1.3: disciplines + fractions]

**Timeline Signal**: [Phase 1.4: N–M sprints]

**Confidence**: [Phase 2.1: level] — [basis: what IS established]
**Confidence Gap [different dimension from basis]**: [Phase 2.2: specific unknown]
**Calibration**: [Phase 2.3: what would change it]

**Sensitivity**:
- Tier up: [Phase 2.4 condition] → Tier rises to [HIGHER tier]
- Tier down: [Phase 2.4 condition] → Tier drops to [LOWER tier]
(Each condition: action that settles it)
```

⚠️ Do NOT include: task breakdowns, sprint assignments, owner names, milestone dates.

---

## V-05 — Conversational Register with Structural Field Labels

**Axis**: Phrasing register (conversational/guided) + structural encoding
**Hypothesis**: A "think through this with me" guided register lowers the barrier to producing substantive, specific estimates while structural field labels embedded in the output template keep relational constraints active at production time — not in a separate rules section the model may not consult before filling each field.

---

Let's size this feature together. Work through each question in order, then produce the signal document at the end.

**Feature to size:**
{{feature_description}}

---

### Question 1 — What do teams do today without this feature?

Ground the sizing in reality before any estimates. Name the workaround. Or if users simply can't do this today, say so directly.

Then ask yourself: is it cheaper for the team to keep maintaining that workaround, or would building this feature cost less over time? Make a call and give your reasoning in one sentence.

Write: "Current workaround: [name, or 'none — users cannot do this today']. Maintaining it is **[cheaper / comparable / more expensive]** because [one sentence]."

Don't move on until you've named the workaround and stated the cost direction explicitly.

---

### Question 2 — What does this feature actually touch?

Walk through the services, APIs, and systems in your head. Name each point where this feature requires a new connection, change, or addition. Then count them.

Format: "[point 1], [point 2], [point N] — **N integration points**"

A vague description without named points and a count doesn't give downstream planning what it needs.

---

### Question 3 — How complex is it?

Now that you've seen the surface area, assign a complexity tier. Use exactly one word: **LOW / MEDIUM / HIGH / XL**. These words are parsed by other tools — substitutes like "MODERATE" or "3/5" break downstream reads.

Then name the 1–2 factors that most justify your choice. "It's big" doesn't tell anyone anything. "Three-service async coordination with no existing error recovery path" does.

---

### Question 4 — What could flip the tier?

Test your own estimate. One condition that would push the tier up. One that would push it down.

Before writing, check your conditions against these guards:

> **Don't write this (tier-up):** "Tier rises to HIGH if scope grows."
> Why not: "scope grows" is a deferral — no investigation can confirm whether it's true. And if your current tier is already HIGH, "rises to HIGH" means nothing moved.
>
> **Write this instead (tier-up):** "Tier rises to XL if the mobile client requires offline sync — verified by reviewing the mobile requirements spec."
> One specific condition. A destination tier that's different from where you are. Something you can actually go check.

> **Don't write this (tier-down):** "Tier drops to LOW if we simplify."
> Why not: deferral — no investigation can confirm "we simplify."
>
> **Write this instead (tier-down):** "Tier drops to LOW if the legacy importer is replaced by CSV upload — confirmed by reviewing data migration requirements."
> Single named condition, falsifiable, destination is lower than the current tier.

Now write yours:

- **Tier up**: [one condition] → Tier rises to **[HIGHER tier than Question 3 — must differ: fill with LOW / MEDIUM / HIGH / XL]**
- **Tier down**: [one condition] → Tier drops to **[LOWER tier than Question 3 — must differ: fill with LOW / MEDIUM / HIGH / XL]**

For each: what action would confirm or rule it out?

---

### Question 5 — Who needs to work on it?

Name the specialist disciplines — not just a headcount. "3 engineers" doesn't tell a planner what capacity to reserve. "1 backend engineer, 1 platform engineer, 0.5 PM" does.

---

### Question 6 — How long, roughly?

Give a sprint range (e.g., "3–5 sprints"). A single number implies false precision. A calendar date confuses effort with scheduling. A range communicates uncertainty honestly.

---

### Question 7 — How confident are you, and what's the gap?

Two parts here, and they need to address different things:

**First — what grounds the estimate?** State your confidence level (HIGH / MEDIUM / LOW) and name the specific, established information that supports it. Don't just say "HIGH." Say: "MEDIUM — the API contract is confirmed and the integration points are fully enumerated." The basis names what you actually know.

**Second — what's still in the dark?** Name the specific thing you haven't verified yet — the gap that, if it went sideways, would invalidate the estimate.

Important: the gap should not just negate the basis. If your basis is "API contract is confirmed," your gap shouldn't be "API contract isn't confirmed yet" — that's the same dimension, opposite direction. Find something genuinely different.

> For example:
> Basis: "API contract is confirmed and surface area is well-scoped."
> Gap: "Concurrency behavior of the webhook queue under load is unverified."
> These address different things — one is about the contract, one is about runtime behavior under stress.

Then add: what would you need to find out to become more confident?

---

### Final Signal

Write the clean signal document now:

```
## Scout-Size Signal: [Feature Name]

**Inertia Check**: Current workaround: [name]. Maintaining it is [cheaper/comparable/more expensive] because [reason].

**Surface Area**: [named list] — N integration points

**Complexity Tier**: [LOW / MEDIUM / HIGH / XL]
Primary driver: [1–2 specific factors]

**Sensitivity**:
- Tier up: [one condition] → Tier rises to [HIGHER tier — must differ from current tier above]
- Tier down: [one condition] → Tier drops to [LOWER tier — must differ from current tier above]
(Each condition: name the action that settles it)

**Team-Size Signal**: [specialist disciplines + fractions]

**Timeline Signal**: [N–M sprints]

**Confidence**: [HIGH/MEDIUM/LOW] — [what IS established]
**Confidence Gap [must address a different dimension than the basis above]**: [specific unknown]
**Calibration**: [what would change the confidence level]
```

⚠️ Do NOT include: task lists, sprint assignments, owner names, milestone dates.

---

## Structural Comparison

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-03 inertia prominence | Section 1 (first) | Step 1 with gate | Phase 1.1 | Phase 0 gate (first output) | Question 1 (first) |
| C-15 basis/gap separation | Field label + WRONG/CORRECT | Column header + WRONG/CORRECT | Charter prohibition | Charter prohibition | Explicit "different thing" instruction |
| C-16 tier destination constraint | Field label inline | Column header in table | Field label inline | Field label inline | Field label inline |
| C-17/C-19/C-21 inline guards | Before Section 4 and 7b | Before Steps 4 and 7 | Before Phase 2.2 and 2.4 | Before Phase 2.2 and 2.4 | Before Question 4 and 7 |
| C-18/C-22 structural encoding | Partial (field labels) | Strong (column headers) | Partial (field labels) | Partial (field labels) | Partial (field labels) |
| C-20 role-separated production | No | No | Yes (Analyst + Assessor) | Yes (Auditor + Analyst + Assessor) | No |
| Inertia as gate | Implicit | Explicit ("complete before proceeding") | Phase 1.1 (first in charter) | Hard gate (Phase 0) | Question 1 ("don't move on until") |

**Recommendation for scoring**: V-03 and V-04 are most likely to pass C-20; V-02 is most likely to pass C-18 structurally; V-04 is most likely to pass C-03 consistently across all possible inputs given the hard Phase 0 gate.
