---
skill: quest-variate
skill_target: scout-size
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-size-rubric-v2-2026-03-16.md
axes_explored: [confidence-anatomy-split, single-condition-template, inertia-framing, combined-table+split+template, full-integration]
r1_champions: [V-04-interrogative, V-05-combination]
r1_gap: C-11 and C-12 absent from V-01/V-02/V-03; V-04/V-05 likely pass both via "What is unverified?" and "Open gap" row
r2_target: confirm C-11/C-12 coverage across all 5 variations; close V-01/V-02/V-03-class weaknesses structurally
---

# scout-size — Prompt Variations R2

Five complete, runnable skill body prompts targeting the v2 rubric (12 criteria). Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

## Context: what informed this round

R1 produced two co-champions at 100/100 (V-04 interrogative, V-05 combination). The v2 rubric adds two Aspirational criteria extracted from R1 excellence signals:

| New criterion | What it requires | R1 mechanism that already covers it |
|---------------|------------------|--------------------------------------|
| C-11 (confidence gap named) | Explicitly name the specific thing NOT yet verified — separate from C-04 basis | V-04 Q6 "What is unverified?"; V-05 TABLE 3 "Open gap" row |
| C-12 (single-condition sensitivity) | Each tier direction is one specific named condition — not a list, not a hedge | V-04 Q4 "What SINGLE condition would push this tier..."; V-05 "Tier UP / DOWN condition \| Required" rows |

R2 design consequence: V-04 and V-05 from R1 likely already satisfy C-11 and C-12. R2 explores three new single-axis mechanisms that produce the same guarantees at different structural leverage points, then recombines. The goal is to establish multiple independent structural routes to C-11 and C-12 compliance — so that if one mechanism drifts, another catches it.

**Three single-axis bets for R2:**
- **Axis A (V-01)**: Confidence anatomy split — separate BASIS and GAP into two labeled mandatory fields, making C-04 and C-11 structurally distinct
- **Axis B (V-02)**: Single-condition naming template — provide a fill-in-the-blank template that forecloses vague hedges and wrong-dimension sensitivity
- **Axis C (V-03)**: Inertia-as-anchor with mandatory cost-direction verdict — tighten C-03 to prevent the "mentioned in passing" failure mode while keeping the rest clean

---

## V-01 — Axis: Confidence Anatomy Split

**Hypothesis**: Splitting the confidence output into two labeled mandatory sub-fields — BASIS (what is known) and GAP (what is NOT known / unverified) — makes C-04 and C-11 structurally impossible to conflate. Any output that does not fill both fields is visibly incomplete. The split forces the model to answer a different question in each field: "What supports the rating?" vs "What limits it?" — preventing the common failure of writing only the positive evidence and calling it a confidence section. Expected risk: if the BASE-section description is too similar in wording to the gap description, the model may copy-restate; the "distinct from Basis" instruction is the guard.

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

Use exactly those words for cost direction. "It depends" and "unclear" are not accepted. Pick the closest directional word and note any qualifying condition.

---

STEP 2 — SURFACE AREA

Name each integration point the feature touches: every API endpoint, auth hook, event bus subscription, data model change, config surface, or cross-service contract. Name each one individually. Then state the total.

Format:
- [Integration point name] — [one-line description]
- [Integration point name] — [one-line description]
...
Total: N integration points

A general description without named points fails. The total count is required.

---

STEP 3 — COMPLEXITY TIER AND DRIVER

Assign exactly one tier from this scale: LOW / MEDIUM / HIGH / XL
Use exactly those words. "MODERATE", "3/5", "complex", "significant" all fail.

Then name the one or two factors most responsible for this tier. These are the primary drivers.

Complexity: [LOW / MEDIUM / HIGH / XL]
Primary driver: [the factor or factors most responsible — not a list]

---

STEP 4 — TEAM AND TIMELINE SIGNAL

Name specialist disciplines, not headcount. Then give a sprint range.

Team signal: [specialist types + FTE fractions — e.g., "1 backend engineer, 1 platform engineer, 0.5 PM"]
Timeline signal: [sprint range — e.g., "3–5 sprints"]

"3 engineers" fails (no specialist types). "Q3 2026" fails (calendar date). "4 sprints" fails (not a range).

---

STEP 5 — SENSITIVITY

State one condition that would push the complexity tier one step up. State one condition that would push it one step down. Each must be a single named condition — not a list, not a hedge.

Tier UP: [the one condition that would push this tier higher — name it specifically]
Tier DOWN: [the one condition that would push this tier lower — name it specifically]

"Several factors could push this to XL" is not a named condition. "If offline sync is required" is a named condition.

---

STEP 6 — CONFIDENCE ANATOMY

The confidence section has two mandatory halves. Both are required. A confidence section that fills only one half fails.

HALF 1 — BASIS (what IS known):
State the confidence level: HIGH / MEDIUM / LOW (or a percentage band like "60–70%").
Then name what SUPPORTS that rating — the specific evidence, verified reasoning, or prior work that grounds the estimate.

  Confidence: [HIGH / MEDIUM / LOW]
  Basis: [specific evidence or reasoning that supports this rating]

HALF 2 — GAP (what is NOT known):
Name the specific thing that is NOT yet verified or known — the primary source of residual uncertainty. This is what LIMITS confidence, not what supports it. It is a different question from the Basis.

  Gap: [the specific thing not yet verified — the primary unknown]

The Gap must not restate the Basis. If your Gap says the same thing as your Basis in different words, you have not identified the gap. Name the one specific unknown that, if resolved, would most raise your confidence.

Also state:
  What would raise it: [specific investigation result or verification that would materially increase the confidence level]

---

STEP 7 — SIGNAL BOUNDARY

This output is a sizing signal, not a project plan. Remove any:
- Task breakdowns ("Step 1: implement X")
- Sprint assignments ("Sprint 2: auth integration")
- Owner names ("Alice owns backend")
- Milestone dates ("Targeting March delivery")

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Single-Condition Naming Template

**Hypothesis**: Providing a mandatory fill-in-the-blank template for sensitivity directions eliminates both failure modes that attacked R1: (1) the wrong-dimension failure (V-03's sprint sensitivity instead of tier sensitivity) because the template explicitly names the tier and the level, and (2) the vague-hedge failure ("several factors could raise this") because a list of factors cannot fill a single-condition template. The template is: "Tier rises to [LEVEL] if [single named condition]." You cannot fill this with a hedge. If you write "Tier rises to XL if several integration points are complex" it becomes visible that the condition is not named. The template creates a legibility test that exposes failures at generation time. Expected risk: the model fills the template correctly on the tier direction but gets the level wrong (e.g., already at HIGH, writes "rises to HIGH").

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. Follow the sections below. Every section is required.

---

## 1. INERTIA CHECK

Before any sizing: what do teams or users do instead of this feature? Name the workaround. Give a directional cost verdict.

Workaround: [what currently substitutes for this feature]
Cost direction: cheaper / comparable / more expensive [choose one]
Reasoning: [one sentence justifying the direction]

---

## 2. SURFACE AREA

Enumerate every integration point individually: API endpoints, auth hooks, event bus subscriptions, data model changes, config surfaces, cross-service contracts.

List each:
- [Name] — [what it is]

Surface area total: N integration points

---

## 3. COMPLEXITY TIER AND PRIMARY DRIVER

Tier: [exactly one of: LOW / MEDIUM / HIGH / XL]
Primary driver: [the one or two factors most responsible for this tier]

---

## 4. SENSITIVITY — SINGLE-CONDITION FORM

State one condition that would push the tier up. State one condition that would push it down.

Use this exact template for each direction. Fill it in. Do not modify the structure.

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

The condition is ONE thing. Failing forms that will not be accepted:
- "Several integration points could push this higher" — not a single named condition
- "If requirements expand" — not specific enough to test
- "If the timeline changes" — wrong dimension (timeline, not tier)
- "If integration is complex" — restates the tier, names nothing new

A named condition is a specific scenario, decision, or requirement that is absent today but would concretely change the scope. Example: "Tier rises to XL if the feature must support offline sync." You can test whether offline sync is required. You cannot test "if requirements expand."

If you cannot identify a single named condition, write: "Tier rises to [LEVEL] if [condition — requires investigation to specify]" and flag it as a gap in the confidence section.

---

## 5. TEAM AND TIMELINE SIGNAL

Team signal: [list specialist disciplines with FTE fractions]
  Example: "1 backend engineer, 1 frontend engineer, 0.5 PM"
  "3 engineers" fails — no specialist types named.

Timeline signal: [sprint range]
  Example: "3–5 sprints"
  A single sprint count fails. A calendar date fails.

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

## V-03 — Axis: Inertia Framing (anchor-first, cost-direction mandatory)

**Hypothesis**: Making the inertia check the structural anchor — requiring it to appear before any sizing output, with both a named workaround AND a directional cost verdict using exactly the words cheaper / comparable / more expensive — prevents the "mentioned in passing" failure mode (C-03 partial) and produces a richer estimate overall because every sizing number is calibrated against the cost of NOT building. When the model anchors against status-quo cost first, the complexity tier and team signal emerge relative to a concrete alternative rather than in a vacuum. The directional vocabulary constraint (those three words, no hedging) forces a defensible judgment. Expected risk: inertia section may become long and crowd out depth in the complexity and confidence sections; the "one sentence" constraint on the reasoning field guards against this.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

THE FIRST QUESTION IS NOT "HOW BIG IS THIS?" — IT IS "WHAT EXISTS TODAY?"

Before you write a single sizing number, answer this: what do teams or users do instead of this feature? Name the workaround. Estimate what it costs to keep running it. Then decide: is building this feature cheaper, comparable, or more expensive than the alternative of never building it?

This is the inertia check. It is the structural anchor of the sizing signal. Write it first.

---

## INERTIA: THE STATUS QUO COST

Workaround: [name the specific alternative currently in use — be specific about what teams do]
Maintenance cost: [estimate the ongoing cost — hours/sprint, error rate, manual effort, or qualitative]
Cost direction verdict: [choose exactly one: cheaper / comparable / more expensive]

The verdict must be one of those three words. "It depends" is not a verdict. "Unclear" is not a verdict. If you are uncertain, pick the closest word and note the qualifying condition in parentheses.

This section is the primary competitor to building the feature. Every number that follows is calibrated against it.

---

## SURFACE AREA

Name each integration point the feature touches. Name them individually. Count them.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

---

## COMPLEXITY AND DRIVERS

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [the one or two factors most responsible for this tier]

Tier sensitivity:
- Rises to [LEVEL] if: [one named condition — one specific scenario that is absent today]
- Falls to [LEVEL] if: [one named condition — one specific scenario that, if confirmed, would simplify scope]

Each sensitivity is one condition. "Several factors" is not a condition.

---

## TEAM AND TIMELINE SIGNAL

Team: [specialist disciplines with FTE fractions — e.g., "1 backend engineer, 0.5 infra, 0.5 PM"]
Timeline: [sprint range — e.g., "3–5 sprints" — not a calendar date, not a single number]

---

## CONFIDENCE

Level: [HIGH / MEDIUM / LOW]
Basis: [what is known that supports this rating — specific, not generic]
Gap: [the specific thing NOT yet verified — the primary unknown that limits this rating]
What would raise it: [specific investigation or verification result]

The Basis names what IS known. The Gap names what IS NOT known. They are different. If your Gap restates your Basis, you have not identified the gap.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This output feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: Confidence Anatomy Split + Single-Condition Template (Combined)

**Hypothesis**: The two new v2 criteria (C-11 and C-12) both require structural enforcement to be reliably achieved. V-01 establishes a structural enforcement for C-11 (two mandatory labeled fields). V-02 establishes structural enforcement for C-12 (fill-in-the-blank template). This variation carries forward the R1 V-05 table base — which already passes all 10 R1 criteria — and grafts both new mechanisms onto it: TABLE 3 gains a split-row anatomy (Basis row + Gap row as distinct labeled entries) and the tier sensitivity rows use the template form. The table format enforces completeness at the column level; the template and split enforce content quality within the fields. Expected risk: two new table rows (Basis, Gap) in TABLE 3 may cause the model to write a sparse Gap by treating it as a short form field rather than a substantive named unknown; the explicit "not a restatement" instruction guards against this.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. Follow the structure below. Every section is required. Every labeled row in every table is required. Missing rows fail the signal.

---

## INERTIA: STATUS QUO

This section is mandatory. Omitting it fails the signal.

| Workaround | Maintenance cost | Cost direction |
|------------|-----------------|----------------|
| [What teams/users do instead — name it specifically] | [hours/sprint or qualitative] | cheaper / comparable / more expensive |

Cost direction: choose exactly one of those three words.

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
| Primary driver | [the one or two factors most responsible] | Not a list — the main thing |
| Team signal | [specialist types + FTE fractions] | e.g., "1 backend engineer, 0.5 PM" — "3 engineers" fails |
| Timeline signal | [sprint range] | e.g., "3–5 sprints" — no calendar dates, no point estimate |
| Tier UP condition | Tier rises to [LEVEL] if [single named condition]. | Fill this template exactly. One condition. "Several factors" fails. |
| Tier DOWN condition | Tier falls to [LEVEL] if [single named condition]. | Fill this template exactly. One condition. "Several factors" fails. |

For the tier sensitivity rows: fill the template with a specific, testable scenario — something that is absent today but would concretely change the implementation scope if true. If you write "several factors" or "requirements expand," replace it with one named condition.

---

## TABLE 3: CONFIDENCE ANATOMY

All four rows are required. The Basis and Gap rows are distinct. Do not restate the Basis in the Gap row.

| Field | Content |
|-------|---------|
| Confidence level | [HIGH / MEDIUM / LOW] |
| Basis | [what IS known that supports this rating — specific evidence or verified reasoning] |
| Gap | [the specific thing NOT YET verified — the primary unknown that limits confidence — this is a different question from Basis] |
| What would raise it | [specific investigation result or verification that would materially increase confidence] |

The Basis answers: "What supports this rating?"
The Gap answers: "What is the one specific thing I do not yet know that most limits this rating?"

These are different questions. Do not answer both with the same information.

---

## SIGNAL BOUNDARY

This output is a sizing signal, not a project plan. Do not include task breakdowns, sprint assignments, owner names, or milestone dates.

---

## SELF-CHECK

Before writing the artifact, confirm:
- [ ] Inertia workaround is named and cost direction is: cheaper / comparable / more expensive
- [ ] TABLE 1 Total row is present with a specific number
- [ ] Complexity tier is exactly: LOW / MEDIUM / HIGH / XL
- [ ] Tier UP row uses template: "Tier rises to [LEVEL] if [single named condition]" — not a list, not a hedge
- [ ] Tier DOWN row uses template: "Tier falls to [LEVEL] if [single named condition]" — not a list, not a hedge
- [ ] TABLE 3 Basis and Gap rows are both non-empty and not restatements of each other
- [ ] No task breakdowns or sprint assignments in output

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full Integration (all axes + explicit anti-patterns + expanded self-check)

**Hypothesis**: The three most reliable failure modes for v2 criteria are: (a) confidence section names only basis without a distinct gap (C-11 failure), (b) sensitivity conditions are vague hedges or wrong-dimension (C-12 failure), and (c) inertia is present but cost direction is hedged or absent (C-03 failure). Each failure mode has a named anti-pattern that appears in real outputs. Making those anti-patterns explicit in the prompt — not just stating the rule but naming the exact wrong form — reduces them in the output because the model has been shown what failure looks like and can self-check against it. This variation combines all structural mechanisms from V-01 through V-04 and adds an anti-pattern block and a 9-item self-check that covers all 12 rubric criteria. Expected risk: the longest variation in this round; may cause the model to lose the imperative force of individual rules in the overall length.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan.

Signal boundary: no task breakdowns, no sprint assignments, no owner names, no milestone dates. Anything that looks like a plan violates the signal boundary and must be removed before the artifact is written.

Follow every step. Every labeled row is required.

---

**MANDATORY OPENING: INERTIA CHECK**

Write this before anything else. What do teams or users do instead of this feature? This check is structural. Omitting it fails the signal.

  Workaround: [name the specific alternative currently in use]
  Maintenance cost: [estimate the ongoing cost to keep running the workaround]
  Cost direction: [choose exactly one: cheaper / comparable / more expensive]

The cost direction is a directional verdict. "It depends" is not a verdict. "Unclear" is not a verdict. Pick the closest word and note qualifying conditions in parentheses if needed. One of the three words is always defensible.

---

**STEP 1: SURFACE AREA**

Name each integration point individually: API endpoints, auth hooks, event bus subscriptions, data model changes, config surfaces, cross-service contracts.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

The Total row is required. "Several integration points" is not an enumeration.

---

**STEP 2: COMPLEXITY TIER AND DRIVER**

Assign exactly one tier:  LOW / MEDIUM / HIGH / XL

No other values. "MODERATE", "3/5", "complex", "non-trivial" all fail.

Primary driver: the one or two factors most responsible for this tier. Not a list. The main thing.

---

**STEP 3: SENSITIVITY — SINGLE-CONDITION FORM**

State one condition that would push the tier up. State one condition that would push it down.

Use this exact template. Fill it in:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Failing forms — if your sensitivity output looks like any of these, replace it:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not a named condition — "several factors" names nothing |
| "If requirements expand" | Not specific — cannot be tested |
| "If integration proves complex" | Restates the tier — names no new condition |
| "If the timeline slips, this may take longer" | Wrong dimension — timeline sensitivity, not tier sensitivity |

A named condition is a specific scenario or requirement that is absent today but would concretely change implementation scope if true. "If offline sync is required" — testable. "If the feature must work across 3 tenants in a shared schema" — testable. Fill the template with one of these.

---

**STEP 4: TEAM AND TIMELINE**

Team signal: list specialist disciplines with FTE fractions.
  Passing: "1 backend engineer, 1 platform engineer, 0.5 PM"
  Failing: "3 engineers" — no specialist types named

Timeline signal: sprint range.
  Passing: "3–5 sprints"
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE ANATOMY — TWO HALVES REQUIRED**

The confidence section has two halves. Both are required. A confidence section that fills only one half fails the signal.

HALF 1 — BASIS (what IS known):
  Confidence: [HIGH / MEDIUM / LOW or percentage band]
  Basis: [the specific evidence, prior work, or reasoning that supports this rating]

HALF 2 — GAP (what is NOT known):
  Gap: [the specific thing not yet verified — the primary unknown that limits confidence]

  What would raise it: [specific investigation result that would move confidence up]

The Basis and Gap are different. The Basis answers "What supports this rating?" The Gap answers "What is the one thing I do not yet know that most limits this rating?"

Failing form that will not be accepted:
  "Confidence: MEDIUM — surface area is clear but the auth layer behavior is unverified."
  This is one sentence. It blends basis and gap. The gap is not separately named.

Passing form:
  Confidence: MEDIUM
  Basis: Surface area and data model changes are fully mapped from prior work on the notification system.
  Gap: The webhook delivery contract with the legacy auth layer is unverified — this is the primary unknown.
  What would raise it: Spike on the auth layer webhook API confirms the delivery contract.

---

**SIGNAL BOUNDARY CHECK**

Scan the output for violations before proceeding:
- [ ] No task breakdowns ("Step 1: implement X" is a plan)
- [ ] No sprint assignments ("Sprint 2: auth integration")
- [ ] No owner names ("Alice owns the backend work")
- [ ] No milestone dates ("Targeting March delivery")

Remove any violations found.

---

**SELF-CHECK — ALL 12 CRITERIA**

Verify before writing the artifact:
- [ ] C-01: Surface area table has a Total row with a specific number
- [ ] C-02: Complexity tier is exactly: LOW / MEDIUM / HIGH / XL (no other form)
- [ ] C-03: Inertia workaround is named; cost direction is exactly: cheaper / comparable / more expensive
- [ ] C-04: Confidence section has a Basis field with specific supporting evidence
- [ ] C-05: No task breakdowns, sprint assignments, owner names, or milestone dates
- [ ] C-06: Team signal names specialist types with FTE fractions (not headcount only)
- [ ] C-07: Timeline is a sprint range (N–M sprints), not a calendar date and not a point estimate
- [ ] C-08: Primary driver names the one or two factors most responsible (not a generic list)
- [ ] C-09: Both tier UP and tier DOWN conditions are present
- [ ] C-10: "What would raise it" field is present and names a specific investigation
- [ ] C-11: Gap field is present, non-empty, and names a specific unknown (not a restatement of Basis)
- [ ] C-12: Tier UP condition uses template: "Tier rises to [LEVEL] if [single named condition]"; Tier DOWN uses same template; neither is a list or hedge

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axis | Primary Bet | Expected C-03 | Expected C-09 | Expected C-11 | Expected C-12 |
|----|------|-------------|---------------|---------------|---------------|---------------|
| V-01 | Confidence anatomy split | Two mandatory labeled fields (BASIS/GAP) force C-04 and C-11 separation | High (explicit step) | High (explicit step) | **High (structural split)** | Medium (no template) |
| V-02 | Single-condition template | Fill-in-the-blank template forecloses hedge and wrong-dimension failure modes | High (explicit section) | High (template enforces tier axis) | High (Gap field present) | **High (template forecloses hedges)** |
| V-03 | Inertia-as-anchor | Inertia first with mandatory 3-word vocabulary closes "mentioned in passing" failure | **High (structural anchor)** | High (sensitivity step) | High (Gap field present) | High (one-condition per direction) |
| V-04 | Confidence split + template | TABLE 3 Basis/Gap rows + template syntax in TABLE 2 tier rows | High (table) | High (template rows) | **High (distinct table rows)** | **High (template rows)** |
| V-05 | Full integration | All axes + anti-pattern block + 12-criterion self-check | **High (failure language)** | **High (template + self-check)** | **High (split + anti-pattern + C-11 in self-check)** | **High (template + anti-pattern + C-12 in self-check)** |

**Key design differences from R1:**

- **C-11 mechanism**: R1 used "What is unverified?" (V-04 Q6) and "Open gap" row (V-05). R2 names the structural distinction explicitly — Basis = what IS known, Gap = what IS NOT known — and adds anti-pattern language showing what a failing confidence section looks like (V-05).
- **C-12 mechanism**: R1 used "What SINGLE condition would push this tier...?" (V-04 Q4) and "Required" annotation on table rows (V-05). R2 uses a fill-in-the-blank template that cannot be filled with a hedge, plus a table of failing forms (V-05) that names the exact outputs to reject.
- **Cross-coverage**: V-01 through V-03 each achieve C-11 and C-12 through different structural mechanisms, meaning R2 tests whether the guarantees are achievable without full integration — establishing independent routes to compliance.
