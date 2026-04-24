---
skill: quest-variate
skill_target: scout-size
round: 7
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v7-2026-03-17.md
axes_explored: [structured-synthesis-trace, gate-forward-reference, minimal-combination-24-25, full-integration-25, dual-enforcement-25]
r6_champion: V-04/V-05 (17/17 on v7 rubric)
r6_gap: C-24/C-25 absent from V-01 and V-02; V-03 absent from both
r7_target: C-24 (synthesis provides structured three-step trace on labeled lines), C-25 (PRE-FLIGHT GATE names its downstream enforcement sections)
---

# scout-size — Prompt Variations R7

Five complete, runnable skill body prompts targeting the v7 rubric (25 criteria). Single-axis first (V-01 through V-02), minimal combination (V-03), full integration (V-04), dual enforcement (V-05).

## Context: what informed this round

R6 produced V-04/V-05 as the variations that score 17/17 on the v7 rubric. The v7 rubric formalizes two additional structural mechanisms sourced from R6 excellence analysis:

| New criterion | What it requires | R6 gap |
|---------------|-----------------|--------|
| **C-24** (structured synthesis trace) | Synthesis surfaces the three-step commitment chain (gate commitment / analysis result / verdict) on separate labeled lines — not folded into a prose paragraph. C-22 prose reference ("The preliminary hypothesis committed in PRE-FLIGHT GATE...") satisfies C-22 but leaves the chain embedded in a sentence the reader must parse to verify. A labeled trace block (Gate commitment: / Analysis: / Verdict:) makes the chain auditable at a glance. | R6 V-03 passes C-22 (names PRE-FLIGHT GATE at both ends in prose) but does not provide a scannable three-step trace. V-04/V-05 already achieve C-24 because the self-check machinery forces a structured form. V-01 and V-02 fail C-24 entirely — no structured trace block present. |
| **C-25** (gate forward-reference) | PRE-FLIGHT GATE names the downstream sections that enforce its scope exclusions and hypothesis commitment — the outbound direction of the navigational mesh. C-23 closes the inbound direction (guards name canonical home); C-25 closes the outbound direction (canonical home names its guards). A gate without a forward-reference is a declaration that assumes its enforcement sections exist; a gate with one is a contract that names its guarantors. | R6 V-03 passes C-23 (navigational guards name PRE-FLIGHT GATE) but the gate itself has no forward-reference list. V-04/V-05 already achieve C-25 because the gate opens with "preconditions for all analysis sections, including STEP 1 through STEP 7" — an implicit forward-reference. The targeted form names sections explicitly and differentiates scope enforcement from hypothesis enforcement. |

**R7 design consequence**: C-24 and C-25 are orthogonal and have different structural homes:

- C-24 lives in SYNTHESIS (or STEP 7) — the structured trace block replaces or supplements the prose verdict close. A variation can add the trace block without touching PRE-FLIGHT GATE.
- C-25 lives in PRE-FLIGHT GATE — the forward-reference list names enforcement sections after the STOP instruction. A variation can add the forward-reference without changing the synthesis structure.

**Under v7 rubric, R6 expected scores:**
- V-01 (synthesis named chain, C-22 only): 13/17 — passes C-21, C-22; fails C-20, C-23, C-24, C-25
- V-02 (navigational guards, C-23 only): 13/17 — passes C-20, C-23; fails C-21, C-22, C-24, C-25
- V-03 (minimal combination, no self-check): 15/17 — passes C-01–C-23; fails C-24, C-25
- V-04/V-05 (with self-check machinery): 17/17 — passes all

**Three axes for R7:**
- **Axis A (V-01)**: Structured synthesis trace — adds labeled three-step trace block (Gate commitment / Analysis / Verdict) to synthesis, making C-24 the single-axis target; no PRE-FLIGHT GATE forward-reference (C-25 intentionally absent); bare exclusion guards in SURFACE AREA and COMPLEXITY kept from R6 V-01 (C-20/C-23 expected failures isolated)
- **Axis B (V-02)**: Gate forward-reference — adds forward-reference list naming enforcement sections to PRE-FLIGHT GATE after STOP instruction, making C-25 the single-axis target; prose synthesis verdict close retained (C-22 compliant), no trace block (C-24 intentionally absent); standalone hypothesis in MANDATORY OPENING (C-21/C-22 expected failures isolated)
- **Axis C (V-03)**: Minimal combination — adds both C-24 structured trace and C-25 gate forward-reference to R6 V-03 base (which already passes C-01–C-23), without failure-mode blockquotes or self-check machinery

---

## V-01 — Axis: Structured synthesis trace (C-24)

**Variation axis**: Lifecycle emphasis — synthesis exposes the three-step commitment chain on separate labeled lines (Gate commitment / Analysis / Verdict), making the logic auditable without re-reading the prose. This is the single-axis test for C-24.

**Hypothesis**: C-24 is achievable independently of C-25. A synthesis section that replaces the prose verdict close with a labeled trace block — keeping every other structural mechanism from R6 V-01 unchanged — should pass C-24. C-25 is intentionally absent: PRE-FLIGHT GATE has no forward-reference list. C-20 and C-23 are also intentionally absent (bare exclusion guards, INERTIA CHECK unguarded) — this isolates the C-24 axis. The critical structural risk is whether the labeled block is treated as a template to fill (producing real trace output) or as a structural annotation the model skips. The block opening "Commitment chain:" and the three mandatory labeled lines (Gate commitment: / Analysis: / Verdict:) with explicit failure-mode prohibition on prose-embedding are the primary guards. Expected pass: C-21 (hypothesis in gate), C-22 (verdict close names PRE-FLIGHT GATE), C-24 (structured trace on labeled lines). Expected fail: C-20 (INERTIA CHECK unguarded, COMPLEXITY unguarded for unknowns), C-23 (bare exclusion guards, no canonical home redirect), C-25 (no gate forward-reference).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## PRE-FLIGHT GATE

Resolve all three fields before filling any analysis section. This gate is a structural precondition — scope boundary, break-even, and preliminary hypothesis must be committed from repo context before any sizing reasoning begins. Do not proceed to INERTIA CHECK until all three fields contain specific responses.

Out-of-scope boundary:
[Name at least one sub-system, behavior, or integration explicitly NOT covered by this sizing. If genuinely full scope: "No exclusions — full scope assumed." "TBD" or blank fails.]

Break-even signal:
[At what adoption level does building recover its cost vs. the current workaround? Rough signal is sufficient. If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit to a range now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to INERTIA CHECK or any section below until this gate is fully resolved.

---

## INERTIA CHECK

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word required]

---

## SURFACE AREA

Do not include scope exclusions here.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. A general description without named points fails.

---

## COMPLEXITY TIER AND DRIVER

Tier: [exactly one of: LOW / MEDIUM / HIGH / XL — no other values]
Primary driver: [the one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Do not include scope exclusions here.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines, no ownership named.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints" — not a point estimate, not a calendar date]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here. Unknowns go in OPEN UNKNOWNS below.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, not generic]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

A generic placeholder like "dependencies may exist" fails.

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence ("Complexity is HIGH. Timeline is 4–6 sprints.") is juxtaposition — it fails this section. Do not embed unknowns here. Do not include scope exclusions here.

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis before analysis opened. State whether the analysis confirms, revises, or partially revises that commitment using the structured commitment-chain trace below. All three labeled lines are required. A prose paragraph that contains the same information fails C-24 — the chain must be on separate lines, scannable without re-reading.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from the analysis sections bearing on the commitment — name at least two signal dimensions such as surface area count, complexity driver, or inertia cost]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state — it must not be derivable from any single dimension alone.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Gate forward-reference (C-25)

**Variation axis**: Lifecycle emphasis — PRE-FLIGHT GATE includes an explicit forward-reference list naming the downstream sections that enforce its scope exclusions and hypothesis commitment, making the outbound direction of the navigational mesh explicit. This is the single-axis test for C-25.

**Hypothesis**: C-25 is achievable independently of C-24. A gate that explicitly states which downstream sections are responsible for enforcing its scope and hypothesis commitment — immediately after the STOP instruction — should pass C-25 without requiring a structured trace in synthesis. C-24 is intentionally absent: synthesis uses the prose verdict close (C-22 compliant, single sentence per form). C-21 is also intentionally absent (standalone MANDATORY OPENING, C-22 prerequisite unmet) to isolate C-25 from gate-hypothesis coupling. A reader arriving at the gate immediately sees: "Scope exclusions committed here are enforced in: INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS. Hypothesis committed here is confirmed or revised in: SYNTHESIS." The risk is that a forward-reference without bilateral closure (C-23 guards) creates a one-way declaration rather than a complete mesh. Expected pass: C-20 (full bilateral closure from R5/R6 V-02 base), C-23 (navigational guards name canonical home), C-25 (gate names enforcement sections). Expected fail: C-21 (hypothesis in standalone MANDATORY OPENING, not inside gate), C-22 (C-21 prerequisite unmet; synthesis references MANDATORY OPENING, not PRE-FLIGHT GATE), C-24 (prose synthesis, no labeled trace block).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## PRE-FLIGHT GATE

Resolve both fields before proceeding. Scope boundary and break-even are structural preconditions for all analysis sections.

Out-of-scope boundary:
[Name at least one sub-system, behavior, or integration explicitly NOT covered by this sizing. If full scope: "No exclusions — full scope assumed." "TBD" fails.]

Break-even signal:
[At what adoption level does building recover its cost vs. the current workaround? Rough signal is sufficient. If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

STOP: Do not proceed to MANDATORY OPENING until both fields contain specific responses.

Scope exclusions committed here are enforced in: INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS — each of those sections carries an explicit prohibition against scope content.
Hypothesis committed here is confirmed or revised in: SYNTHESIS — that section names MANDATORY OPENING by label and explicitly confirms or revises the commitment.

---

## MANDATORY OPENING: PRELIMINARY HYPOTHESIS

After PRE-FLIGHT GATE, commit to a preliminary estimate before analysis begins. You will confirm or revise it in SYNTHESIS.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — commit now]
Hypothesis — timeline: [N–M sprints — commit now]
Reasoning: [one sentence]

Failing: "Hard to say." If uncertain, pick LOW and note the uncertainty.

---

## INERTIA CHECK

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word, required]

Do not add scope qualifications here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

---

## SURFACE AREA

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps. Noting them here creates a duplicate record outside their canonical home.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here — unknowns belong in OPEN UNKNOWNS below, not in analysis sections. Embedding them here creates a record outside the canonical home.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership area per role]
  Failing: "2 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns API + event schema), 0.5 PM (owns stakeholder alignment)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work]

Do not list unknowns here — unknowns belong in OPEN UNKNOWNS below, not in the confidence basis. Listing an unknown here creates a second, structurally invisible record outside the canonical home that OPEN UNKNOWNS provides.

---

## OPEN UNKNOWNS

Canonical home for unverified items.

Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — unknowns belong here, not in those sections.

If no unknowns remain: "No open unknowns — confidence is fully grounded."

For each open unknown:

Unknown: [the specific unverified item — concrete, not generic]
Impact: [complexity / timeline / team / confidence]
Movement: [specific action or result that closes this]

A generic placeholder like "dependencies may exist" fails.

---

## SYNTHESIS

Do not embed unknowns here — unknowns belong in OPEN UNKNOWNS, not in synthesis.
Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

> **Anti-pattern**: Restating sections in sequence is juxtaposition — it fails this section. The conclusion must require two or more signal dimensions to produce.

First: look back at MANDATORY OPENING: PRELIMINARY HYPOTHESIS — it committed [tier] at [sprint range] before analysis. State whether the analysis confirms, revises, or partially revises that commitment:

- "Hypothesis confirmed: [tier] at [N–M sprints] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior] to [current] because [reason]"
- "Hypothesis partially revised: [what held]; [what changed] because [reason]"

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation that requires both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update or explicitly reaffirm it. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axes: Structured trace + gate forward-reference (minimal combination)

**Variation axes**: C-24 (structured three-step trace on labeled lines in synthesis) + C-25 (PRE-FLIGHT GATE forward-references enforcement sections) — both new R7 mechanisms combined in the simplest possible structure, without failure-mode blockquotes or self-check machinery.

**Hypothesis**: V-01 and V-02 test C-24 and C-25 independently. V-03 tests whether combining both in the R6 V-03 base structure (which already passes C-01–C-23) achieves all 17 criteria without requiring the full failure-mode blockquotes and self-check machinery from R6 V-04/V-05. The gate adds the forward-reference list after STOP (C-25). SYNTHESIS replaces the prose verdict close with a labeled Commitment chain block (C-24). All other mechanisms carry over from R6 V-03 unchanged. If V-03 passes all 17 criteria cleanly, it becomes the new minimum prompt. Expected risk: without failure-mode blockquotes, the labeled trace block in synthesis may be populated with prose rather than genuinely separate labeled values; the explicit "A prose paragraph that contains the same information fails — the chain must be on separate labeled lines" prohibition is the primary structural guard against that regression.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## PRE-FLIGHT GATE

Resolve all three fields before filling any analysis section. This gate is a structural precondition — scope boundary, break-even, and preliminary hypothesis must be committed from repo context before any sizing reasoning begins. Do not proceed to INERTIA CHECK until all three fields contain specific responses.

Out-of-scope boundary:
[Name at least one sub-system, behavior, or integration explicitly NOT covered by this sizing. If genuinely full scope: "No exclusions — full scope assumed." "TBD" or blank fails.]

Break-even signal:
[At what adoption level does building recover its cost vs. the current workaround? Rough signal is sufficient. If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit to a range now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to INERTIA CHECK or any section below until this gate is fully resolved.

This gate's commitments are enforced downstream:
- Scope exclusions: held in INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS — each carries an explicit prohibition against scope content.
- Hypothesis: confirmed or revised in SYNTHESIS — that section names PRE-FLIGHT GATE by label at both the anchor and the verdict close.

---

## INERTIA CHECK

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word required]

Do not add scope boundary notes here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

---

## SURFACE AREA

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here — unknowns belong in OPEN UNKNOWNS, not in analysis sections.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here — unknowns belong in OPEN UNKNOWNS, not in the confidence basis.

---

## OPEN UNKNOWNS

Canonical home for unverified items.
Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — unknowns belong here, not in those sections.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [specific unverified item — concrete, not generic]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence ("Complexity is HIGH. Timeline is 4–6 sprints.") is juxtaposition — it fails this section. Do not embed unknowns here — unknowns belong in OPEN UNKNOWNS. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines. A prose paragraph that folds the same information into a single sentence fails C-24 — the chain must be scannable without re-reading.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from analysis sections bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation. The recommendation must require both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: All R7 mechanisms + failure mode blockquotes + 25-criterion self-check

**Variation axes**: C-24 (structured synthesis trace) + C-25 (gate forward-reference) + all R6 V-04 mechanisms (failure mode blockquotes in SYNTHESIS and OPEN UNKNOWNS, AMEND cascade, signal boundary check) + self-check updated to 25 criteria (adding C-24 and C-25 items)

**Hypothesis**: V-03 is the minimal combination achieving all 17 criteria. V-04 adds the failure-mode blockquotes (C-17) and the AMEND cascade (C-16), then updates the self-check to 25 criteria including explicit C-24 and C-25 items. The C-24 self-check item defines the exact disqualifying form ("a prose paragraph that folds the chain into one sentence fails C-24 — the three lines must be scannable independently"). The C-25 self-check item defines what counts as a complete forward-reference vs. a bare gate-only declaration. The structured trace block in STEP 7 uses the same labeled format as V-03. The gate forward-reference after STOP names all four enforcement sections explicitly and distinguishes scope-enforcement from hypothesis-enforcement. Expected risk: prompt length increases; the sequential STEP ordering and the stop instruction in the gate are the primary guards against section confusion.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE — complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve them from repo context now. Do not proceed until all three fields contain specific responses — "TBD" or blank fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If genuinely full implementation scope: "No exclusions — full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? State a rough signal or explicitly: "Cannot assess — [specific reason]." Absence fails C-10 before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this gate is fully resolved.

This gate's commitments are enforced downstream:
- Scope exclusions: STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY, and STEP 7 SYNTHESIS each carry an explicit prohibition against scope content.
- Hypothesis: STEP 7 SYNTHESIS names this gate by label at both the anchor ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." — No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team — building is **more expensive** upfront but **cheaper** to maintain; workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive — one word, required]

Do not add scope boundary notes or exclusion qualifications here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity — use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here (e.g., "uncertainty about X may raise the tier") — unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here — unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. Listing an unknown here creates a second, structurally invisible record outside the canonical home.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section — the structural separation from STEP 5 exists to make omissions visible, not to create a section that can be filled with vague language. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE. Do not include break-even observations here — break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here — they belong in STEP 6. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required. A prose paragraph that folds the same information into a single sentence fails C-24 — the chain must be scannable without re-reading.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1–6 bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it in light of the amendment. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 25 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named — appears in PRE-FLIGHT GATE (canonical location)
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in STEP 6 OPEN UNKNOWNS with Unknown: / Impact: / Movement: typed fields; STEP 5 explicitly closed
- [ ] C-15: Preliminary hypothesis is field 3 inside PRE-FLIGHT GATE; synthesis explicitly confirms or revises it, naming the changed dimension
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields; includes stop instruction
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5 CONFIDENCE) and at least one section adjacent to scope exclusion canonical home (STEP 2 or STEP 3) carry explicit prohibition rules
- [ ] C-20: Every plausible recipient for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) and unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition rule — any single unguarded plausible recipient fails C-20
- [ ] C-21: Preliminary hypothesis (complexity tier + timeline range) is a field INSIDE PRE-FLIGHT GATE — not in MANDATORY OPENING or any standalone section after the gate; synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises the commitment
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both the anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") and in the verdict close form ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). "My earlier estimate was confirmed" fails — it names no structural site.
- [ ] C-23: For at least one canonical field type (scope exclusions, open unknowns), the prohibition guards in adjacent sections name the canonical home by label — "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" not "do not include scope exclusions here."
- [ ] C-24: Synthesis includes a structured Commitment chain block with three labeled lines (Gate commitment: / Analysis: / Verdict:) on separate lines. A prose paragraph that mentions PRE-FLIGHT GATE twice and contains the same information fails C-24 — the chain must be scannable without re-reading any sentence.
- [ ] C-25: PRE-FLIGHT GATE (after the STOP instruction) names at least two downstream sections responsible for enforcing its scope exclusions and names the section responsible for confirming or revising its hypothesis. A gate that commits scope and hypothesis without naming enforcement sections fails C-25 even if those sections carry guards back to the gate.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full integration + dual enforcement + structural definitions for C-24/C-25

**Variation axes**: All R7 V-04 axes + self-check items for C-24 and C-25 extended with structural definitions naming exact disqualifying conditions, mirroring the structural definition pattern from R5/R6 V-05 for C-20/C-21/C-22/C-23.

**Hypothesis**: V-04 adds C-24 and C-25 to the 25-criterion self-check with definition-level descriptions. V-05 extends those definitions to include the exact structural disqualifying condition — the same dual-enforcement pattern that made R5 V-05 and R6 V-05 the highest-reliability variations. For C-24, the disqualifying condition is: "synthesis that says 'The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3–5 sprints) is confirmed because surface area is LOW and inertia cost is HIGH' fails C-24 even if C-22 passes — the three-step chain is embedded in one sentence, not on separate scannable lines." For C-25, the disqualifying condition is: "PRE-FLIGHT GATE that says 'Resolve these fields before proceeding to STEP 1 through STEP 7' fails C-25 — naming the steps as a continuation instruction is not the same as naming enforcement sections and distinguishing scope enforcement from hypothesis enforcement." The self-check item for each criterion names the exact disqualifying form so the model can identify violations before writing, not discover them through scoring. V-05 is the highest-reliability form of the v7 rubric: structural mechanisms prevent violations during generation; the 25-criterion checklist with structural definitions catches residuals.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE — complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve them from repo context now. Do not proceed until all three fields contain specific responses — "TBD" or blank fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If genuinely full implementation scope: "No exclusions — full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? State a rough signal or explicitly: "Cannot assess — [specific reason]." Absence fails C-10 before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS (prohibits scope exclusions) — each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." — No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team — building is **more expensive** upfront but **cheaper** to maintain; workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive — one word, required]

Do not add scope boundary notes or exclusion qualifications here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity — use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here (e.g., "uncertainty about X may raise the tier") — unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here — unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This section is explicitly closed against unknowns — listing one here creates a second, unguarded record outside the canonical home that STEP 6 provides.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section — the structural separation from STEP 5 exists to make omissions visible, not to create a section that can be filled with vague language. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE. Do not include break-even observations here — break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here — they belong in STEP 6. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate lines. A single sentence that mentions the tier, the analysis, and the verdict is juxtaposition-in-miniature — the chain must be scannable at a glance, with each step independently readable.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1–6 bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict line]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

The verdict close must name PRE-FLIGHT GATE by label — not a hypothesis constructed after the sections were filled, but the specific commitment made in the gate. Writing "my earlier estimate was confirmed" fails C-22 because it does not identify the structural site. Writing the verdict as a prose paragraph that happens to contain all three chain steps fails C-24 because the chain is not scannable independently.

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 25 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named — must appear in PRE-FLIGHT GATE (canonical location); also acceptable anywhere else in the output
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion; fails if derivable from any single field alone
- [ ] C-14: Open unknowns appear in STEP 6 OPEN UNKNOWNS with Unknown: / Impact: / Movement: typed fields; STEP 5 explicitly closed against unknowns
- [ ] C-15: Preliminary hypothesis (complexity tier + timeline range) is a field INSIDE PRE-FLIGHT GATE — not in MANDATORY OPENING or any standalone section after the gate. Synthesis explicitly confirms or revises it, naming the changed dimension. An output that passes C-18 (gate present) and has a hypothesis elsewhere still fails C-15 if hypothesis is not inside the gate block.
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields with specific responses; includes stop instruction; inline reminders inside sections do not count
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (specifically STEP 5 CONFIDENCE) and at least one section adjacent to the scope exclusion canonical home (STEP 2 SURFACE AREA or STEP 3 COMPLEXITY) carry an explicit prohibition rule — not just that canonical sections exist, but that their neighbors are explicitly closed
- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) carries an explicit prohibition. Every plausible recipient section for unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition. Any single unguarded plausible recipient fails C-20 — C-19 minimum-pass coverage is not sufficient.
- [ ] C-21: Preliminary hypothesis (complexity tier + timeline range) is a field inside PRE-FLIGHT GATE — not in MANDATORY OPENING or any standalone section after the gate. Synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises it. Passing C-18 (gate present) and C-15 (hypothesis present) independently still fails C-21 if the hypothesis is outside the gate block.
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both ends of the verification chain: (1) at the anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") AND (2) in the verdict close form ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). The disqualifying form: "My earlier estimate was confirmed" fails C-22 even if C-21 passes — it refers to the hypothesis without naming the structural site. The gate label must appear in what the model writes in the verdict, not only in the instruction.
- [ ] C-23: For at least one canonical field type (scope exclusions, open unknowns), the prohibition guards in adjacent sections name the canonical home by label. Passing: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps." Failing: "do not include scope exclusions here" — this is a dead end that excludes without redirecting. An output can pass C-20 (all adjacent sections guarded) and still fail C-23 if no guard names where the excluded content belongs.
- [ ] C-24: Synthesis includes a Commitment chain block with three labeled lines on separate lines: Gate commitment: / Analysis: / Verdict:. The disqualifying form: a sentence reading "The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3–5 sprints) is confirmed: surface area is LOW and inertia cost is HIGH, so proceeding is low-risk" fails C-24 even if it passes C-22 — the three chain steps are embedded in one sentence, not independently scannable. The model must be able to verify gate commitment, analysis evidence, and verdict each by reading one line, not one paragraph.
- [ ] C-25: PRE-FLIGHT GATE (after the STOP instruction) includes an enforcement contract that names at least two downstream sections responsible for scope exclusions AND names the section responsible for hypothesis confirmation or revision. The disqualifying form: "All three fields above are preconditions for STEP 1 through STEP 7" fails C-25 — naming the steps as a continuation instruction is not an enforcement contract. The gate must name sections by label and distinguish which sections enforce scope vs. which section enforces the hypothesis. A gate that commits both without naming its guarantors separately fails C-25 even if those sections carry C-23 navigational guards back to it.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axes | C-21 | C-22 | C-23 | C-24 | C-25 | Self-check |
|----|------|------|------|------|------|------|------------|
| V-01 | Structured synthesis trace only | **High** — hypothesis in gate | **High** — verdict templates require "PRE-FLIGHT GATE" label | Low — bare exclusion guards, no home reference | **High** — Commitment chain block with labeled lines | Low — no gate forward-reference | None |
| V-02 | Gate forward-reference only | Low — standalone MANDATORY OPENING | Low — C-21 prerequisite unmet | **High** — all guards redirect to canonical home | Low — prose synthesis, no trace block | **High** — enforcement contract names scope sections + hypothesis section | None |
| V-03 | Structured trace + gate forward-reference (minimal) | **High** | **High** | **High** | **High** | **High** | None |
| V-04 | All R7 mechanisms + failure modes + 25-criterion self-check | **High** | **High** | **High** | **High** | **High** | 25 criteria |
| V-05 | Full integration + 25-criterion self-check + structural definitions for C-24/C-25 | **High** | **High** | **High** | **High** | **High** | 25 criteria + definitions |

**Expected scores under v7:**

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 5/5 | 3/3 | 15/17 (fails C-20, C-23, C-25) | 98.82 |
| V-02 | 5/5 | 3/3 | 15/17 (fails C-21, C-22, C-24) | 98.82 |
| V-03 | 5/5 | 3/3 | 17/17 | **100** |
| V-04 | 5/5 | 3/3 | 17/17 | **100** |
| V-05 | 5/5 | 3/3 | 17/17 | **100** |

**Key design differences from R6:**

- **C-24 mechanism**: R6 V-03/V-04/V-05 pass C-22 by embedding the gate label in verdict close templates — "The preliminary hypothesis committed in PRE-FLIGHT GATE..." — but the three-step chain (gate commitment, analysis evidence, verdict) is inside a single sentence. R7 V-01/V-03/V-04/V-05 add a `Commitment chain:` labeled block with `Gate commitment:`, `Analysis:`, and `Verdict:` on separate lines. The block structure makes all three steps independently readable without parsing sentence boundaries. The prohibition "A prose paragraph that folds the same information into a single sentence fails C-24" is the structural enforcement against silent regression to sentence form.

- **C-25 mechanism**: R6 V-04/V-05 implicitly forward-reference enforcement sections via "preconditions for all analysis sections, including STEP 1 through STEP 7" — a continuation instruction that names the steps but does not distinguish what each step enforces. R7 adds an explicit "Enforcement contract" block after STOP that names scope-enforcement sections (STEP 1/2/3/7) separately from hypothesis-enforcement (STEP 7 SYNTHESIS). The distinction matters for C-25 pass condition: "names at least two downstream sections" is met by the scope-enforcement list alone, but the most reliable form separates scope vs. hypothesis enforcement so a reader can verify compliance by section type, not just section name.

- **V-01 single-axis design**: Intentionally keeps bare exclusion guards in SURFACE AREA and COMPLEXITY (C-23 fails) and leaves INERTIA CHECK unguarded (C-20 fails). Tests whether the structured trace block alone achieves C-24 without requiring navigational guards or gate forward-reference. The gate remains three-field atomic (C-21 preserved) with verdict close templates (C-22 preserved).

- **V-02 single-axis design**: Intentionally places hypothesis in standalone MANDATORY OPENING after the gate (C-21/C-22 fail) and uses prose synthesis verdict close (C-24 fails). Tests whether the gate forward-reference alone achieves C-25 without a structured trace block. Uses full bilateral closure and navigational guards from R6 V-02/V-03 base (C-20/C-23 preserved).

- **Self-check evolution**: R6 V-05 has a 23-criterion self-check. R7 V-04 adds C-24 and C-25 as explicit self-check items with definition-level descriptions. R7 V-05 extends those definitions with structural disqualifying forms — naming exactly what written output fails each criterion. This pattern has been the highest-reliability enforcement mechanism across R3, R4, R5, and R6: the self-check item names the disqualifying form so the model can identify violations before writing, not discover them through external scoring.
