---
skill: quest-variate
skill_target: scout-size
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-size-rubric-v3-2026-03-16.md
axes_explored: [lifecycle-emphasis-two-phase, output-format-tier-transition-table, phrasing-register-socratic, combined-table+two-phase, full-integration]
r2_champions: [V-04-table+split, V-05-full-integration]
r2_gap: C-13 and C-14 absent from structural enforcement in V-01 (STEP 5 lacked [LEVEL] in template); C-14 covered only in V-02/V-05 via anti-pattern language, not universally via structural mechanism
r3_target: enforce C-13 and C-14 through independent structural routes across all 5 variations; establish multiple mechanisms so if one drifts, another catches it
---

# scout-size — Prompt Variations R3

Five complete, runnable skill body prompts targeting the v3 rubric (14 criteria). Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

## Context: what informed this round

R2 produced two champions at high confidence (V-04 table+split, V-05 full-integration). The v3 rubric adds two Aspirational criteria extracted from R2 excellence signals:

| New criterion | What it requires | R2 near-miss that exposed the gap |
|---------------|------------------|-----------------------------------|
| C-13 (explicit tier destination) | Each sensitivity condition states the destination tier explicitly — `Tier rises to [LEVEL]` with [LEVEL] filled | V-01 R2: STEP 5 required "one named condition" but template lacked `[LEVEL]`, so outputs could satisfy C-12's intent while leaving destination ambiguous |
| C-14 (falsifiable conditions) | Each condition is a verifiable scenario — a reader can state what action would settle it; "if requirements change" fails, "if offline sync is required" passes | V-02 R2: had a passing forms / failing forms table that approximated this, but did not require a verification action — the testability criterion was implied, not structural |

R3 design consequence: C-13 requires `[LEVEL]` to appear in the output, not just in the rule. C-14 requires the model to name what a colleague would actually do to settle the condition. Neither is achieved by stating the rule — both require structural slots that force the content.

**Three single-axis bets for R3:**
- **Axis A (V-01)**: Lifecycle emphasis — sensitivity as two explicit phases: Phase 1 names the condition and fills `[LEVEL]`; Phase 2 names the verification action. The two-phase structure separates the "what would change the tier" question from the "how would you know" question.
- **Axis B (V-02)**: Output format — tier-transition table with columns [Direction | Condition | Current Tier | Destination Tier | Verify by]. Structural columns make C-13 (Destination Tier) and C-14 (Verify by) impossible to omit without a visible blank cell.
- **Axis C (V-03)**: Phrasing register — conversational/Socratic with workaround-as-protagonist and an explicit "colleague test" for falsifiability. The colleague test asks "could someone on your team actually go investigate this?" — a question form that naturally surfaces unfalsifiable conditions before they reach the output.

---

## V-01 — Axis: Lifecycle Emphasis (Sensitivity as Two Phases)

**Hypothesis**: Splitting the sensitivity section into two mandatory phases — Phase 1: name the condition and state the destination tier; Phase 2: name the verification action — prevents both C-13 and C-14 failures by making them structurally separate. In Phase 1, the template `Tier rises to [LEVEL] if [condition]` with `[LEVEL]` required closes the V-01 R2 near-miss: the prompt now explicitly states that [LEVEL] is a mandatory fill (not implied). In Phase 2, the "This condition can be settled by: [action]" field forces the model to prove the condition is falsifiable before it writes the artifact — if it cannot name an action, the incompleteness is visible. Expected risk: Phase 2 may be filled with an overly generic action ("talk to PM") that technically occupies the field but does not pass a real falsifiability test; the anti-pattern examples for failing Phase 2 forms guard against the most common generic hedges.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal for the topic. A sizing signal answers: how much work is this, and how confident are we in that answer? It does NOT produce a project plan.

---

STEP 1 — INERTIA CHECK

Before assessing complexity, name what exists today. What do teams or users do instead of this feature?

  Workaround: [name the specific alternative currently in use]
  Cost direction: [cheaper / comparable / more expensive — choose one]
  Basis: [one sentence supporting the direction]

Use exactly those words for cost direction. "It depends" and "unclear" are not accepted. Pick the closest word and note qualifying conditions in parentheses if needed.

---

STEP 2 — SURFACE AREA

Name each integration point the feature touches: every API endpoint, auth hook, event bus subscription, data model change, config surface, or cross-service contract. Name each one individually. Then state the total.

  - [Integration point name] — [one-line description]
  ...
  Total: N integration points

A general description without named points fails. The total count is required.

---

STEP 3 — COMPLEXITY TIER AND DRIVER

Assign exactly one tier: LOW / MEDIUM / HIGH / XL
Use exactly those words. "MODERATE", "3/5", "complex", "non-trivial" all fail.

  Complexity: [LOW / MEDIUM / HIGH / XL]
  Primary driver: [the one or two factors most responsible for this tier — not a list]

---

STEP 4 — SENSITIVITY (TWO PHASES: NAME, THEN VERIFY)

For each tier direction, complete BOTH phases. A sensitivity entry with only one phase fails.

TIER UP:
  Phase 1 — Condition and destination:
    Tier rises to [LEVEL] if [single named condition].
    [LEVEL] must be one of: LOW / MEDIUM / HIGH / XL — fill it in. Writing "tier would rise" without a destination fails.

  Phase 2 — Verification:
    This condition can be settled by: [the specific action, conversation, spike, or document review that would confirm or rule it out]

TIER DOWN:
  Phase 1 — Condition and destination:
    Tier falls to [LEVEL] if [single named condition].
    [LEVEL] must be one of: LOW / MEDIUM / HIGH / XL — fill it in.

  Phase 2 — Verification:
    This condition can be settled by: [the specific action, conversation, spike, or document review that would confirm or rule it out]

Phase 2 must name a concrete action. Failing forms that will not be accepted:
  - "Further investigation needed" — names no action
  - "Talk to stakeholders" — too generic; what question, with whom?
  - "It will become clearer in planning" — a deferral, not a verification
  - "Revisit when requirements are finalized" — not an investigation, a wait

Passing Phase 2 forms:
  - "Confirm whether offline sync is required in a requirements session with PM"
  - "Spike the webhook delivery contract with the auth team this sprint"
  - "Review legacy auth API docs to determine if the delivery callback is exposed"
  - "Ask platform lead whether multi-tenant support is in scope for v1"

---

STEP 5 — TEAM AND TIMELINE SIGNAL

Name specialist disciplines, not headcount. Then give a sprint range.

  Team signal: [specialist types + FTE fractions — e.g., "1 backend engineer, 1 platform engineer, 0.5 PM"]
  Timeline signal: [sprint range — e.g., "3–5 sprints"]

"3 engineers" fails (no specialist types). "Q3 2026" fails (calendar date). "4 sprints" fails (not a range).

---

STEP 6 — CONFIDENCE ANATOMY

Both halves are required. A confidence section that fills only one half fails.

  HALF 1 — BASIS (what IS known):
    Confidence: [HIGH / MEDIUM / LOW]
    Basis: [specific evidence or reasoning that supports this rating — what IS known]

  HALF 2 — GAP (what is NOT known):
    Gap: [the specific thing NOT yet verified — the primary unknown that limits confidence — different from Basis]
    What would raise it: [specific investigation result that would materially increase confidence]

The Basis answers: "What supports this rating?" The Gap answers: "What is the one thing I do not yet know that most limits this rating?" These are different questions.

---

STEP 7 — SIGNAL BOUNDARY

This output is a sizing signal, not a project plan. Remove any task breakdowns, sprint assignments, owner names, or milestone dates before writing the artifact.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Output Format (Tier-Transition Table with Verify-by Column)

**Hypothesis**: Replacing the single-template line for sensitivity with a structured table where columns are [Direction | Named Condition | Current Tier | Destination Tier | Verify by] makes both C-13 and C-14 structurally impossible to omit. The "Destination Tier" column is a dedicated cell that requires one of LOW / MEDIUM / HIGH / XL — it cannot be implied, hedged, or left blank without producing a visibly incomplete row. The "Verify by" column is the structural slot for C-14 — any row where this cell says "further investigation" rather than naming an action is visibly deficient. A secondary benefit: the "Current Tier" column makes the starting tier explicit in the same row, so the model cannot accidentally write a tier transition that starts from the wrong level. Expected risk: a four-column table row may cause the model to compress the condition cell to a short phrase that passes form (single, named) but is too abstract to pass substance; the failing/passing examples guard against this.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. Follow the sections below. Every section is required.

---

## 1. INERTIA CHECK

Before any sizing: what do teams or users do instead of this feature? Name the workaround. Give a directional cost verdict.

  Workaround: [what currently substitutes for this feature — name it specifically]
  Cost direction: cheaper / comparable / more expensive [choose one]
  Reasoning: [one sentence justifying the direction]

---

## 2. SURFACE AREA

Enumerate every integration point individually: API endpoints, auth hooks, event bus subscriptions, data model changes, config surfaces, cross-service contracts. List each:

  - [Name] — [what it is]

  Surface area total: N integration points

---

## 3. COMPLEXITY TIER AND PRIMARY DRIVER

  Tier: [exactly one of: LOW / MEDIUM / HIGH / XL]
  Primary driver: [the one or two factors most responsible for this tier]

---

## 4. SENSITIVITY — TIER TRANSITION TABLE

Fill every cell. A blank cell in any column fails the row.

| Direction | Named Condition | Current Tier | Destination Tier | Verify by |
|-----------|----------------|-------------|-----------------|-----------|
| UP | [single named condition — one specific scenario absent today] | [current tier] | [destination tier] | [specific action that would confirm or rule this out] |
| DOWN | [single named condition — one specific scenario that would simplify scope] | [current tier] | [destination tier] | [specific action that would confirm or rule this out] |

Column rules:
- **Named Condition**: one specific scenario. Failing forms: "several factors", "if requirements expand", "if scope grows", "if integration proves complex". Passing forms name a requirement, decision, or discovery that is absent today and would concretely change the implementation scope.
- **Current Tier** and **Destination Tier**: each must be exactly one of: LOW / MEDIUM / HIGH / XL. They must differ — if they are the same, the condition does not shift the tier and must be replaced.
- **Verify by**: names a concrete, actionable investigation — a specific conversation, spike, document review, or prototype. Failing: "further investigation", "talk to stakeholders", "will be clearer later". Passing: "spike the webhook contract with the auth team", "confirm offline sync requirement with PM in sprint planning", "review multi-tenancy requirements doc with platform lead".

---

## 5. TEAM AND TIMELINE SIGNAL

  Team signal: [list specialist disciplines with FTE fractions]
    Passing: "1 backend engineer, 1 frontend engineer, 0.5 PM"
    Failing: "3 engineers" — no specialist types named

  Timeline signal: [sprint range]
    Passing: "3–5 sprints"
    Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

## 6. CONFIDENCE

  Confidence: [HIGH / MEDIUM / LOW]
  Basis: [what is known that supports this rating]
  Gap: [the specific thing NOT yet verified — what limits confidence]
  What would raise it: [specific investigation or result]

---

## SIGNAL BOUNDARY

No task breakdowns, sprint assignments, owner names, or milestone dates. This is a sizing signal that feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axis: Phrasing Register (Conversational/Socratic, Workaround-as-Protagonist)

**Hypothesis**: A conversational register that treats the workaround as the protagonist — the thing the feature must beat — produces more authentic sizing because every estimate is naturally calibrated against the cost of inaction. When the prompt asks "What are people doing today instead? What does that cost them? Now: is building this cheaper, comparable, or more expensive?" the model reasons about the actual decision, not an abstracted build estimate. The "colleague test" for falsifiability ("could a colleague on your team actually go investigate this?") makes C-14 into a question rather than a template — producing richer reasoning about what is and isn't discoverable. The C-13 requirement is embedded as a direct constraint inside the question: "Where does the tier land? Name the level." Expected risk: question-form prompts feel more optional than directives; a short structural scaffold after each question section anchors the required output fields and prevents the conversational tone from eroding completeness.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Before you start: this is NOT a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. You are producing a sizing signal — an estimate of how much work this is and how confident you are in that answer.

---

THE STATUS QUO: THE FEATURE'S PRIMARY COMPETITOR

The first question is not "how big is this?" The first question is: what are people doing TODAY instead of this feature?

Name it. Then ask: is building this feature cheaper, comparable, or more expensive than continuing to live with the workaround? Pick one. "It depends" is not an answer — make the call, qualify it if needed.

  Workaround: [name it — what specifically do teams or users do]
  Maintenance cost: [what does running this workaround cost — time, errors, manual effort, or qualitative]
  Verdict: [cheaper / comparable / more expensive — choose one]

Every sizing number that follows is calibrated against this. The workaround is the feature's primary competitor. The verdict is the opening judgment.

---

HOW MUCH DOES IT TOUCH?

Name every integration point the feature reaches: API endpoints, auth hooks, event subscriptions, data model changes, config surfaces, cross-service contracts. Don't describe them in aggregate — list them individually.

  - [Integration point] — [what it is]
  ...
  Total: N integration points

---

HOW COMPLEX IS IT?

Assign one tier: LOW / MEDIUM / HIGH / XL. Exactly those words — "significant", "non-trivial", "moderate" all fail.

  Complexity: [LOW / MEDIUM / HIGH / XL]

What's most driving this? Name the factor or two that are most responsible — the real reason the tier is what it is, not a general statement about complexity.

  Primary driver: [the one or two factors]

---

WHAT WOULD CHANGE YOUR ESTIMATE?

Two questions. For each, answer two sub-questions: what is the condition, and could a colleague actually go investigate it?

Question 1 — What single condition, if true, would push the complexity tier higher?
  Name the condition. Name where the tier would land. Both are required.

  Tier rises to [LEVEL] if: [name the one condition]
  [LEVEL] must be one of: LOW / MEDIUM / HIGH / XL. "Tier would rise" without naming the destination fails.

  Colleague test: could a teammate actually investigate this? What would they do?
  A colleague could settle this by: [the specific action — a conversation, a spike, a doc review, a prototype]

  If you cannot answer the colleague test, your condition is a hedge, not a scenario. Replace it.

Question 2 — What single condition, if true, would let you simplify?
  Name the condition. Name where the tier would land.

  Tier falls to [LEVEL] if: [name the one condition]
  [LEVEL] must be one of: LOW / MEDIUM / HIGH / XL.

  A colleague could settle this by: [the specific action]

Conditions that pass the colleague test: "Tier rises to XL if offline sync is required — a colleague could verify this by asking the PM in the next requirements session." "Tier falls to MEDIUM if the feature only needs single-tenant support — confirm with platform lead by reviewing the v1 scope document."

Conditions that fail the colleague test: "Tier rises if scope grows." "Tier rises to HIGH if things are more complex than expected." Neither names what a colleague would actually do.

---

WHO AND HOW LONG?

Name the specialists, not just a headcount.

  Team: [specialist types + FTE fractions — e.g., "1 backend engineer, 0.5 infra, 0.5 PM"]
  Timeline: [sprint range — e.g., "3–5 sprints" — not a calendar date, not a single number]

---

HOW CONFIDENT ARE YOU?

Answer two separate questions. Do not answer Question 2 by restating Question 1.

  Question 1 — What supports this rating?
    Confidence: [HIGH / MEDIUM / LOW]
    Basis: [what IS known — specific evidence, prior work, or verified reasoning]

  Question 2 — What limits it?
    Gap: [the one specific thing NOT yet known or verified — the primary unknown]
    What would raise confidence: [the specific investigation that would resolve the gap]

---

SIGNAL BOUNDARY

Scan before writing: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: Tier-Transition Table + Two-Phase Sensitivity (Output Format + Lifecycle Emphasis)

**Hypothesis**: The two most structurally reliable mechanisms for C-13 and C-14 are the tier-transition table (V-02) and the two-phase split (V-01). The table enforces C-13 via the Destination Tier column — a cell that cannot be filled without naming a level. The two-phase split enforces C-14 via Phase 2 — a mandatory "Settle by" sub-field beneath each table row that requires a concrete investigation action. Together, they provide two independent structural handles on C-13 and C-14: the table's column structure prevents omission; the phase-2 field inside each row prevents generic filler (because the phase-2 field is prose, not a table cell, the model cannot meet it by filling in "LOW" — it must write a sentence). The table format also carries forward R2 V-04's success on C-01 through C-12 via TABLE 1 (surface area), TABLE 2 (sizing dimensions), and TABLE 3 (confidence anatomy). Expected risk: the combination of table rows plus phase-2 sub-fields may produce verbose sensitivity entries; the "Phase 2 must be one sentence" constraint guards against this.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. Follow the structure below. Every section is required. Every labeled row in every table is required. Missing rows fail the signal.

---

## INERTIA: STATUS QUO

| Workaround | Maintenance cost | Cost direction |
|------------|-----------------|----------------|
| [What teams/users do instead — be specific] | [hours/sprint or qualitative] | cheaper / comparable / more expensive |

Cost direction: choose exactly one of those three words. "It depends" is not a cost direction.

---

## TABLE 1: SURFACE AREA

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| 2 | ... | | |
| **Total** | | | **N integration points** |

The Total row is required. N must be a specific number.

---

## TABLE 2: SIZING DIMENSIONS

| Dimension | Value | Notes |
|-----------|-------|-------|
| Complexity tier | [LOW / MEDIUM / HIGH / XL] | Exactly this vocabulary — no other values |
| Primary driver | [the one or two factors most responsible] | The main thing — not a generic list |
| Team signal | [specialist types + FTE fractions] | e.g., "1 backend engineer, 0.5 PM" — "3 engineers" fails |
| Timeline signal | [sprint range] | e.g., "3–5 sprints" — no calendar dates, no point estimate |

---

## SENSITIVITY — TIER TRANSITION TABLE WITH VERIFICATION

For each direction: fill the table row, then complete Phase 2 beneath it. Both are required.

| Direction | Named Condition | Current Tier | Destination Tier |
|-----------|----------------|-------------|-----------------|
| UP | [single named condition — one specific scenario absent today] | [current tier] | [destination tier: LOW / MEDIUM / HIGH / XL] |
| DOWN | [single named condition — one specific scenario that would simplify scope] | [current tier] | [destination tier: LOW / MEDIUM / HIGH / XL] |

Rules for the table:
- **Named Condition**: one specific scenario. "Several factors" fails. "If requirements expand" fails.
- **Current Tier** and **Destination Tier**: both required, both from LOW / MEDIUM / HIGH / XL. They must differ.
- Destination Tier must be explicitly named — "tier would rise" with no level stated fails C-13.

Phase 2 — Verification (required for each row, one sentence each):

  TIER UP — Settle by: [the specific action that would confirm or rule out the UP condition]
  TIER DOWN — Settle by: [the specific action that would confirm or rule out the DOWN condition]

Phase 2 must name a concrete action. Failing forms: "further investigation needed", "talk to stakeholders", "will become clear in planning". Passing forms: "confirm with PM whether offline sync is in scope", "spike the webhook contract with the auth team", "review multi-tenancy requirements with platform lead".

If you cannot name a settling action for a condition, that condition is a hedge. Replace it with one that passes the test.

---

## TABLE 3: CONFIDENCE ANATOMY

All four rows are required. Basis and Gap must not be restatements of each other.

| Field | Content |
|-------|---------|
| Confidence level | [HIGH / MEDIUM / LOW] |
| Basis | [what IS known that supports this rating — specific evidence or verified reasoning] |
| Gap | [the specific thing NOT YET verified — the primary unknown that limits confidence — different question from Basis] |
| What would raise it | [specific investigation result or verification that would materially increase confidence] |

Basis answers: "What supports this rating?" Gap answers: "What is the one specific thing I do not yet know that most limits this rating?" Do not answer both with the same information.

---

## SIGNAL BOUNDARY

No task breakdowns, sprint assignments, owner names, or milestone dates.

---

## SELF-CHECK

- [ ] Inertia: workaround named; cost direction is: cheaper / comparable / more expensive
- [ ] TABLE 1: Total row present with a specific number
- [ ] Complexity tier is exactly: LOW / MEDIUM / HIGH / XL
- [ ] TIER UP table row: Destination Tier cell is filled with LOW / MEDIUM / HIGH / XL (not implied, not blank)
- [ ] TIER UP Phase 2: "Settle by" names a concrete, actionable investigation (not "further investigation")
- [ ] TIER DOWN table row: Destination Tier cell is filled with LOW / MEDIUM / HIGH / XL
- [ ] TIER DOWN Phase 2: "Settle by" names a concrete, actionable investigation
- [ ] TABLE 3 Basis and Gap: both non-empty and not restatements of each other
- [ ] No task breakdowns or sprint assignments in output

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full Integration (All R3 Mechanisms + C-13/C-14 Anti-Pattern Tables + 14-Criterion Self-Check)

**Hypothesis**: The three most structurally reliable failure modes for v3 criteria are: (a) sensitivity states the direction without naming the destination tier — "tier would rise" passes C-12 but fails C-13; (b) sensitivity condition is named and singular but cannot actually be investigated — passes C-12 on form but fails C-14 on substance; (c) confidence section names basis without a distinct gap — fails C-11. Each failure mode has a named anti-pattern that appears in real outputs. Making those anti-patterns explicit — not just stating the rule but showing the exact wrong form next to the correct form — reduces failures because the model can self-check against concrete examples. This variation combines all structural mechanisms from V-01 through V-04, adds dedicated anti-pattern tables for C-13 and C-14, and extends the self-check from R2's 12 criteria to all 14 v3 criteria. Expected risk: the longest variation in this round; may cause individual rules to lose imperative force in the overall length; mitigated by placing the self-check last so the model reviews compliance against every criterion before writing.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan.

Signal boundary: no task breakdowns, no sprint assignments, no owner names, no milestone dates. Scan for violations before writing the artifact.

Follow every step. Every labeled row and field is required.

---

**MANDATORY OPENING: INERTIA CHECK**

Write this before anything else. Omitting it fails the signal.

  Workaround: [name the specific alternative currently in use]
  Maintenance cost: [estimate — hours/sprint, error rate, or qualitative]
  Cost direction: [choose exactly one: cheaper / comparable / more expensive]

"It depends" is not a verdict. One of the three words is always defensible. Pick the closest and note qualifying conditions in parentheses if needed.

---

**STEP 1: SURFACE AREA**

Name each integration point individually.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

The Total row is required. "Several integration points" is not an enumeration.

---

**STEP 2: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible — not a generic list]

No other tier values. "MODERATE", "3/5", "complex", "non-trivial", "significant" all fail.

---

**STEP 3: SENSITIVITY — CONDITION, DESTINATION, AND VERIFICATION**

State one condition that would push the tier up and one that would push it down. For each: name the condition, state the destination tier explicitly, and name the verification action.

TIER UP:
  Condition: Tier rises to [LEVEL] if [single named condition].
  Settle by: [specific action that would confirm or rule this out — one sentence]

TIER DOWN:
  Condition: Tier falls to [LEVEL] if [single named condition].
  Settle by: [specific action that would confirm or rule this out — one sentence]

**C-13 anti-patterns — destination tier missing or implied:**

| Failing form | Problem |
|---|---|
| "Tier would rise if offline sync is added" | No destination tier — where does it rise TO? |
| "This could bump the tier higher" | No condition, no destination |
| "Tier rises if the scope expands" | Vague condition AND no destination level |
| "Complexity would increase" | Neither condition nor destination — fails C-09, C-12, C-13 |

The `[LEVEL]` slot must be filled: LOW / MEDIUM / HIGH / XL. A direction without a destination fails C-13.

**C-14 anti-patterns — condition is not falsifiable:**

| Failing form | Why it fails | What to replace it with |
|---|---|---|
| "Tier rises to XL if requirements expand" | Cannot investigate — what specifically expands? | "Tier rises to XL if the feature must support offline sync" |
| "Tier falls to MEDIUM if scope is reduced" | Not specific — what reduction? | "Tier falls to MEDIUM if multi-tenant support is deferred to v2" |
| "Tier rises to HIGH if integration proves complex" | Restates the tier — nothing to discover | "Tier rises to HIGH if the auth layer does not expose a webhook callback" |
| "Tier falls to LOW if the team is experienced" | Team assumption, not a verifiable requirement | "Tier falls to LOW if the feature reuses the existing notification queue without schema changes" |

A condition passes C-14 when you can fill in: "Settle by: [action]" with something concrete. If you cannot, replace the condition.

Passing forms for "Settle by":
- "Confirm with PM whether offline sync is required in the next requirements session"
- "Spike the webhook delivery contract with the auth team this sprint"
- "Review the multi-tenancy requirements doc with the platform lead to confirm v1 scope"
- "Check the legacy auth API docs for an exposed delivery callback endpoint"

---

**STEP 4: TEAM AND TIMELINE**

Team signal: [specialist types with FTE fractions]
  Passing: "1 backend engineer, 1 platform engineer, 0.5 PM"
  Failing: "3 engineers" — no specialist types named

Timeline signal: [sprint range]
  Passing: "3–5 sprints"
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE ANATOMY — TWO HALVES REQUIRED**

Both halves are required. A confidence section that fills only one half fails.

HALF 1 — BASIS (what IS known):
  Confidence: [HIGH / MEDIUM / LOW]
  Basis: [specific evidence or reasoning that supports this rating — what IS known]

HALF 2 — GAP (what is NOT known):
  Gap: [the specific thing NOT yet verified — the primary unknown that limits confidence]
  What would raise it: [specific investigation result that would move confidence up]

Failing form (blends basis and gap into one sentence):
  "Confidence: MEDIUM — surface area is clear but the auth layer behavior is unverified."
  This is one sentence. The gap is not named distinctly. It fails C-11.

Passing form (distinct halves):
  Confidence: MEDIUM
  Basis: Surface area is fully mapped from prior work on the notification system.
  Gap: Webhook delivery contract with the legacy auth layer is unverified.
  What would raise it: Spike with auth team confirms the webhook contract this sprint.

The Basis answers: "What supports this rating?" The Gap answers: "What is the one specific thing I do not yet know that most limits this rating?" Do not answer both with the same information.

---

**SIGNAL BOUNDARY CHECK**

Scan before writing:
- [ ] No task breakdowns ("Step 1: implement X" is a plan)
- [ ] No sprint assignments ("Sprint 2: auth integration")
- [ ] No owner names ("Alice owns the backend work")
- [ ] No milestone dates ("Targeting March delivery")

Remove any violations found.

---

**SELF-CHECK — ALL 14 CRITERIA**

Verify before writing the artifact:
- [ ] C-01: Surface area table has a Total row with a specific number
- [ ] C-02: Complexity tier is exactly: LOW / MEDIUM / HIGH / XL (no other form)
- [ ] C-03: Inertia workaround is named; cost direction is exactly: cheaper / comparable / more expensive
- [ ] C-04: Confidence section has a Basis field with specific supporting evidence
- [ ] C-05: No task breakdowns, sprint assignments, owner names, or milestone dates
- [ ] C-06: Team signal names specialist types with FTE fractions (not headcount only)
- [ ] C-07: Timeline is a sprint range (N–M sprints), not a calendar date and not a point estimate
- [ ] C-08: Primary driver names one or two specific factors (not "it's complex")
- [ ] C-09: Both tier UP and tier DOWN conditions are present
- [ ] C-10: "What would raise it" field names a specific investigation
- [ ] C-11: Gap field is present, non-empty, and names a specific unknown (not a restatement of Basis)
- [ ] C-12: Each tier condition is a single named condition — not a list, not a hedge
- [ ] C-13: Each tier condition states the destination tier explicitly: Tier rises to [LEVEL] / Tier falls to [LEVEL] — [LEVEL] filled with LOW / MEDIUM / HIGH / XL, not implied
- [ ] C-14: Each condition has a "Settle by" action that names a concrete investigation a colleague could actually perform

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axis | Primary Bet | C-13 Mechanism | C-14 Mechanism | Expected Risk |
|----|------|-------------|----------------|----------------|---------------|
| V-01 | Lifecycle emphasis (two-phase sensitivity) | Phase 1 names condition + destination; Phase 2 names verification action — two structurally separate questions | Template requires `[LEVEL]` fill + explicit "Writing 'tier would rise' without a destination fails" | Phase 2 "Settle by:" field is mandatory — anti-pattern examples show failing/passing forms | Phase 2 filled with overly generic action ("talk to PM"); anti-patterns guard against most common forms |
| V-02 | Output format (tier-transition table) | Destination Tier column is a dedicated cell — cannot be implied or left blank without visible gap | **Structural**: Destination Tier column requires LOW / MEDIUM / HIGH / XL | **Structural**: "Verify by" column requires concrete action in every row | Four-column row may compress condition cell to abstract phrase that passes form but not substance |
| V-03 | Phrasing register (Socratic, workaround-as-protagonist) | "Colleague test" question makes falsifiability a reasoning step, not a template fill | `[LEVEL]` required in template + "naming the destination fails" embedded in question form | "Could a teammate actually go investigate this? What would they do?" surfaces unfalsifiable conditions pre-output | Question form feels optional vs directives; structural scaffold anchors required output fields |
| V-04 | Output format + lifecycle emphasis (combined) | Table provides structural column enforcement; Phase 2 provides prose enforcement — two independent handles | **Dual**: Destination Tier column (table) + Phase 1 template with `[LEVEL]` | **Dual**: Phase 2 "Settle by" sub-field beneath each row + failing/passing examples | Combination may produce verbose sensitivity entries; "one sentence" constraint on Phase 2 guards |
| V-05 | Full integration | All axes + dedicated anti-pattern tables for C-13/C-14 + 14-criterion self-check | C-13 anti-pattern table (4 failing forms shown) + self-check item C-13 | C-14 anti-pattern table (4 failing forms + replacements) + "Settle by" in template + self-check item C-14 | Longest variation; may dilute imperative force of individual rules; mitigated by final self-check |

**Key design differences from R2:**

- **C-13 mechanism**: R2's V-02 and V-03 used fill-in templates that required `[LEVEL]` — this worked, but the mechanism was implicit (V-01 failed precisely because the template was present but `[LEVEL]` was not enforced). R3 makes `[LEVEL]` enforcement explicit in every variation: V-01 states "Writing 'tier would rise' without a destination fails"; V-02 uses a dedicated Destination Tier column; V-03 embeds the constraint inside the question; V-04 uses both; V-05 adds an anti-pattern table that shows four forms of C-13 failure.

- **C-14 mechanism**: R2 had no structural slot for C-14 — it relied on anti-pattern language (V-02, V-05). R3 adds a mandatory "Settle by" / "Verify by" field in every variation, making falsifiability a required output rather than a quality bar applied post-generation. The "Settle by" sub-field creates a legibility test at generation time: if you cannot fill it with an action, the condition is a hedge.

- **Independence**: V-01 through V-03 test three independent mechanisms for C-13 and C-14. V-01 uses a phase split (lifecycle). V-02 uses table columns (format). V-03 uses a question register (phrasing). R3 establishes whether C-13/C-14 compliance is achievable through any single structural route — not just the full integration approach that worked in R2 V-04/V-05.
