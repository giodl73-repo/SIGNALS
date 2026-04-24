Written to `simulations/quest/variations/scout-size-variations-R5-2026-03-17.md`.

---

# scout-size — Prompt Variations R5

**Five complete variations targeting C-20 and C-21 (v5 rubric, 21 criteria).**

## What R4 left open

Both R4 champions (V-04, V-05) scored 100/100 on v4 but have two structural gaps for v5:

| Gap | Root cause |
|-----|-----------|
| **C-20 fails** | INERTIA CHECK has no prohibition against scope exclusion drift; COMPLEXITY TIER has no prohibition against unknowns drift. Every other plausible recipient was guarded, but not these two. |
| **C-21 fails** | MANDATORY OPENING: PRELIMINARY HYPOTHESIS is a standalone section *after* the gate. C-21 requires the hypothesis to be a field *inside* the gate — the gate becomes the atomic commitment block. |

## Variation axes

| ID | Primary axis | C-20 bet | C-21 bet |
|----|-------------|----------|----------|
| **V-01** | C-21 single-axis: hypothesis as field 3 inside gate | Low — INERTIA CHECK, COMPLEXITY unguarded | **High** |
| **V-02** | C-20 single-axis: INERTIA CHECK + COMPLEXITY prohibition guards added | **High** | Low — hypothesis in MANDATORY OPENING after gate |
| **V-03** | Minimal combination: both axes, no self-check | **High** | **High** |
| **V-04** | Full integration: R4 V-04 base + C-21 + C-20 + 21-criterion self-check | **High** | **High** |
| **V-05** | Full integration + dual enforcement: R4 V-05 base + C-21 + C-20 + 21-criterion self-check with explicit structural definitions | **High** | **High** |

## Key structural changes from R4

**For C-21**: PRE-FLIGHT GATE now contains three fields — scope boundary, break-even, *and* preliminary hypothesis — as one atomic block with a single STOP instruction. SYNTHESIS explicitly references "the hypothesis committed in PRE-FLIGHT GATE" by name.

**For C-20**: Two previously unguarded sections now carry explicit prohibition rules:
- INERTIA CHECK → "Do not add scope boundary notes or exclusion qualifications here — scope was resolved in PRE-FLIGHT GATE"
- COMPLEXITY TIER AND DRIVER → "Do not embed unknowns here — they belong in STEP 6 OPEN UNKNOWNS. Tier sensitivity conditions are specific external events, not uncertainty statements"
recipient sections remain unguarded for their respective canonical homes. |
| **C-21** (pre-flight gate elicits preliminary hypothesis) | The preliminary hypothesis (complexity tier + timeline range) is a FIELD INSIDE the pre-flight gate — not a standalone section that follows it. The gate becomes the site of the commitment: scope boundary, break-even, and hypothesis are resolved together as one atomic precondition block. An output that passes C-18 (gate exists) and C-15 (hypothesis exists) independently does not satisfy C-21 if the hypothesis is outside the gate. | R4 V-04 and V-05 place MANDATORY OPENING: PRELIMINARY HYPOTHESIS as a separate section after PRE-FLIGHT GATE, connected by a stop instruction. The hypothesis is structurally independent of the gate — a model could satisfy C-18 and omit the hypothesis (failing C-15) because the gate does not itself demand the commitment. |

**R5 design consequence**: C-20 and C-21 are orthogonal. C-20 governs coverage (prohibition guards on every plausible recipient section). C-21 governs placement (hypothesis is inside the gate, not adjacent to it). An output can pass C-21 and still fail C-20 if INERTIA CHECK or COMPLEXITY carry no prohibition rules. R5 tests each independently first.

**Two single-axis bets for R5:**
- **Axis A (V-01)**: Gate-embedded hypothesis — PRE-FLIGHT GATE gains a third required field: preliminary complexity tier and timeline range committed inside the gate, after scope boundary and break-even are resolved. SYNTHESIS references "the hypothesis committed in PRE-FLIGHT GATE" by name. C-21 single-axis; no change to bilateral guard coverage beyond R4 V-03's existing guards.
- **Axis B (V-02)**: Full bilateral closure — adds explicit prohibition rules to INERTIA CHECK (against scope exclusion drift) and COMPLEXITY TIER AND DRIVER (against unknowns drift), completing the containment mesh. Keeps MANDATORY OPENING: PRELIMINARY HYPOTHESIS as a standalone section after the gate (C-15 satisfied, C-21 not targeted). C-20 single-axis.

---

## V-01 — Axis: Gate-embedded hypothesis (C-21 single-axis)

**Variation axis**: Structural placement — preliminary hypothesis is the third required field inside PRE-FLIGHT GATE, resolved as a precondition alongside scope boundary and break-even before any analysis section opens

**Hypothesis**: In R4 V-04 and V-05, PRE-FLIGHT GATE and MANDATORY OPENING: PRELIMINARY HYPOTHESIS are sequential sections connected by a stop instruction. The hypothesis is committed after the gate resolves scope boundary and break-even — but it remains a separate section that could theoretically be omitted without breaking the gate. C-21 requires the hypothesis to be inside the gate: the gate becomes a single atomic block that forces scope + break-even + hypothesis together before analysis. When the hypothesis is a third gate field, scope boundary and break-even are known inputs before the complexity tier and timeline range are committed — the hypothesis cannot contradict the scope because the scope is resolved three lines above it in the same block. SYNTHESIS explicitly references "the hypothesis committed in PRE-FLIGHT GATE," making the gate-to-synthesis chain structurally verifiable. Expected risk: a combined gate field may produce a less-committed hypothesis than a standalone section; the "Failing form: 'Hard to say'" guard and the "commit to one tier, pick LOW if uncertain" instruction from R4 are preserved inside the hypothesis field.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section is required.

---

## PRE-FLIGHT GATE

Complete all three fields before filling any analysis section. This is a structural gate — scope boundary, break-even, and preliminary hypothesis must all be resolved before any analysis section opens.

Out-of-scope boundary:
[Name at least one sub-system, behavior, integration, or phase explicitly NOT covered by this sizing. If genuinely full scope: "No exclusions — full scope assumed." Do not say "TBD." Do not leave blank.]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost relative to continuing the current workaround? A rough signal is sufficient: "breaks even at 3+ teams using weekly." If break-even cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

Preliminary hypothesis:
  Complexity tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now, before analysis. Failing form: "Hard to say without more analysis." If genuinely uncertain, pick LOW and note the uncertainty.]
  Timeline: [N–M sprints — commit to a range now, before analysis. A point estimate or calendar date fails.]
  Reasoning: [One sentence: what signals this scope level before detailed analysis begins?]

STOP: Do not proceed to INERTIA CHECK or any section below until all three fields contain specific responses. The SYNTHESIS section will confirm or revise the preliminary hypothesis committed here.

---

## INERTIA CHECK

Workaround: [the specific alternative currently in use — name it, do not describe it generically]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative estimate]
Cost direction: [choose exactly one: cheaper / comparable / more expensive]

The cost direction is a verdict. "It depends" is not a verdict.

---

## SURFACE AREA

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE above.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. A general description without named points fails.

---

## COMPLEXITY TIER AND DRIVER

Tier: [exactly one of: LOW / MEDIUM / HIGH / XL — no other values]
Primary driver: [the one or two factors most responsible for this tier]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition — one specific, testable scenario absent today].
- Falls to [LEVEL] if [single named condition — one specific, testable scenario absent today].

"If requirements expand" fails — not a testable condition.

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE above.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines, no ownership named.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints" — not a point estimate, not a calendar date]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning that supports this rating]

Do not list unknowns here. Unknowns belong in OPEN UNKNOWNS below.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are closed against unknowns.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — name it concretely]
Impact: [which sizing dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that would close this unknown]

A generic placeholder like "dependencies may exist" fails.

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4-6 sprints." — is juxtaposition, not synthesis. Do not embed unknowns here (they go in OPEN UNKNOWNS). Do not re-state scope exclusions here (they were resolved in PRE-FLIGHT GATE).

First: look back at PRE-FLIGHT GATE. State whether the analysis confirms, revises, or partially revises the preliminary hypothesis committed there:
- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

Then: cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a directional observation. The conclusion must require both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Full bilateral closure (C-20 single-axis)

**Variation axis**: Output structure — every section adjacent to every canonical home carries an explicit prohibition rule, completing the containment mesh that R4 V-03 left partially open

**Hypothesis**: R4 V-03 and V-04 close the highest-risk adjacent sections (SURFACE AREA and COMPLEXITY against scope exclusions; CONFIDENCE against unknowns; SYNTHESIS against both) but leave two plausible recipients unguarded: INERTIA CHECK could receive scope exclusion content ("the workaround applies only to teams inside this scope; we are excluding department X from this sizing") and COMPLEXITY TIER sensitivity could receive unknowns content ("uncertainty about auth integration may push the tier up"). These are low-probability but structurally unguarded drift sites. C-20 requires zero unguarded plausible recipients, not merely low probability. Adding explicit prohibitions to INERTIA CHECK and COMPLEXITY TIER AND DRIVER — without changing gate placement or hypothesis structure — tests whether C-20 is achievable by extending guard coverage alone. MANDATORY OPENING: PRELIMINARY HYPOTHESIS remains as a standalone section after the gate (satisfying C-15 independently, not inside the gate). Expected risk: the INERTIA CHECK prohibition may read as redundant; phrasing "Do not add scope qualifications or exclusion notes here — scope was resolved in PRE-FLIGHT GATE" makes the guard feel purposive rather than mechanical.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section is required.

---

## PRE-FLIGHT GATE

Resolve both fields before proceeding. This gate fires before all other sections — scope boundary and break-even must be answered from repo context before any analysis section is filled.

Out-of-scope boundary:
[Name at least one sub-system, behavior, integration, or phase explicitly NOT covered by this sizing. "TBD" or blank fails. If genuinely full scope: "No exclusions — full scope assumed."]

Break-even signal:
[At what adoption level, team count, or time horizon does building recover its cost vs. the current workaround? A rough signal is sufficient. If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

STOP: Do not proceed to MANDATORY OPENING until both fields contain specific responses.

---

## MANDATORY OPENING: PRELIMINARY HYPOTHESIS

After PRE-FLIGHT GATE, commit to a preliminary estimate. You will confirm or revise it in SYNTHESIS.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — one specific tier, commit. Failing form: "Hard to say without more analysis." If uncertain, pick LOW and note it.]
Hypothesis — timeline: [sprint range — "N–M sprints" — one range]
Reasoning: [one sentence: what signals this scope before detailed analysis?]

---

## INERTIA CHECK

Workaround: [the specific alternative in use — name it]
Maintenance cost: [hours/sprint, error rate, or qualitative estimate]
Cost direction: [cheaper / comparable / more expensive — one word required]

Do not add scope qualifications or exclusion notes here — scope boundary was resolved in PRE-FLIGHT GATE. Any note of the form "this workaround applies outside the scoped area" belongs in PRE-FLIGHT GATE, not here.

---

## SURFACE AREA

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE. Noting an exclusion in this section creates a duplicate record outside the canonical home.

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
- Rises to [LEVEL] if [single named condition — specific, testable].
- Falls to [LEVEL] if [single named condition — specific, testable].

Do not include scope exclusions here — scope boundary was resolved in PRE-FLIGHT GATE. Do not embed unknowns here (e.g., "uncertainty about X integration may raise the tier") — unknowns belong in OPEN UNKNOWNS below. Tier sensitivity conditions name specific external events, not internal uncertainty states.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership area per role]
  Failing: "2 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns API + event schema), 0.5 PM (owns alignment)"

Timeline signal: [sprint range — "N–M sprints" form required]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work that supports this rating]

Do not list unknowns here. Unknowns belong in OPEN UNKNOWNS below. Listing an unknown in the confidence basis creates a second, structurally invisible record — the separation this section enforces is what makes OPEN UNKNOWNS detectable as complete or incomplete.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are explicitly closed against unknowns. Do not list scope exclusions here — they were resolved in PRE-FLIGHT GATE.

If no unknowns remain: "No open unknowns — confidence is fully grounded."

For each open unknown:

Unknown: [the specific unverified item — concrete, not generic]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [what investigation resolves this — specific action or result]

A generic placeholder like "dependencies may exist" fails.

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence is juxtaposition, not synthesis. Do not embed unknowns here — they belong in OPEN UNKNOWNS. Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

First: look back at MANDATORY OPENING: PRELIMINARY HYPOTHESIS. State whether the analysis confirms, revises, or partially revises it:
- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

Then: cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a directional observation that requires both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axes: Gate-embedded hypothesis + Full bilateral closure (minimal combination)

**Variation axes**: C-21 (hypothesis inside gate) + C-20 (all adjacent sections closed) — combined in the simplest possible structure, without R3 self-indictment machinery or a self-check

**Hypothesis**: V-01 and V-02 test C-21 and C-20 independently. V-03 tests whether combining both in the minimal structure — gate with embedded hypothesis, prohibition guards on all plausible recipient sections — achieves both criteria without requiring the full step-labeled machinery from R4 V-04/V-05. The combination is expected to be non-interfering: the gate-embedded hypothesis resolves temporal placement (scope + break-even + hypothesis all committed before analysis), while the full bilateral guards resolve spatial coverage (no unguarded adjacent section for any canonical home). They address different failure modes on different structural dimensions. Without the R3 self-indictment machinery, synthesis may revert to post-hoc juxtaposition — a minimal anti-pattern blockquote is included as a lightweight guard. Expected risk: the absence of a self-check means any guard omission persists silently into the written artifact; this is the intentional structural limitation of the minimal combination.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section is required.

---

## PRE-FLIGHT GATE

Resolve all three fields before filling any analysis section. This gate is a structural precondition — scope boundary, break-even, and preliminary hypothesis must all be committed before analysis begins.

Out-of-scope boundary:
[Name at least one sub-system, phase, or integration explicitly NOT covered. "TBD" or blank fails. If genuinely full scope: "No exclusions — full scope assumed."]

Break-even signal:
[At what usage level or time horizon does building recover its cost vs. the current workaround? Rough signal accepted. If cannot assess: "Cannot assess — [specific reason]." Blank fails.]

Preliminary hypothesis:
  Complexity tier: [LOW / MEDIUM / HIGH / XL — commit now. "Hard to say" fails. Pick LOW if uncertain and note it.]
  Timeline: [N–M sprints — commit now. Point estimate or calendar date fails.]
  Reasoning: [One sentence: what about the known scope signals this tier?]

STOP: All three fields must contain specific responses. Do not proceed to INERTIA CHECK or any section below until this gate is fully resolved. The SYNTHESIS section will confirm or revise the hypothesis committed here.

---

## INERTIA CHECK

Workaround: [the specific alternative in use — name it]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word]

Do not add scope boundary notes here — scope was resolved in PRE-FLIGHT GATE.

---

## SURFACE AREA

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

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
- Rises to [LEVEL] if [single named condition — specific, testable].
- Falls to [LEVEL] if [single named condition — specific, testable].

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE. Do not embed unknowns here — unknowns belong in OPEN UNKNOWNS below. Sensitivity conditions are specific external events, not uncertainty statements.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work]

Do not list unknowns here. Unknowns belong in OPEN UNKNOWNS below.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are closed against unknowns. Do not list scope exclusions here — they were resolved in PRE-FLIGHT GATE.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [specific unverified item — name it concretely]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4-6 sprints." — is juxtaposition. Do not embed unknowns here (they go in OPEN UNKNOWNS). Do not re-state scope exclusions here (they were resolved in PRE-FLIGHT GATE).

First: look back at PRE-FLIGHT GATE. State whether the analysis confirms, revises, or partially revises the preliminary hypothesis committed there:
- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

Then: cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a directional observation that requires both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: All R4 V-04 axes + gate-embedded hypothesis + full bilateral closure + 21-criterion self-check

**Variation axes**: C-21 (hypothesis inside gate) + C-20 (complete bilateral mesh) + all R4 V-04 mechanisms (STEP-labeled sections, AMEND cascade, self-indictment blockquotes, 17-criterion self-check updated to 21)

**Hypothesis**: R4 V-04 scored 100/100 on the v4 rubric. Its two structural gaps for v5 are: (1) MANDATORY OPENING is a standalone section after the gate — C-21 requires the hypothesis INSIDE the gate; (2) INERTIA CHECK and COMPLEXITY TIER carry no prohibition rules — C-20 requires complete bilateral coverage. V-04 R5 addresses both by: collapsing MANDATORY OPENING into a third gate field (the gate sequence becomes scope boundary -> break-even -> preliminary hypothesis -> STOP, one atomic block), and adding prohibition guards to STEP 1 INERTIA CHECK ("do not add scope qualifications here") and STEP 3 COMPLEXITY TIER AND DRIVER ("do not embed unknowns here"). The 17-criterion self-check is updated to 21 items: C-18 and C-19 checklist items from R4 V-05 are preserved, and two new items are added for C-20 (specifying STEP 1 and STEP 3 as the previously unguarded sections) and C-21 (specifying that the hypothesis must be inside the gate block, and that synthesis must reference "the hypothesis committed in PRE-FLIGHT GATE" by name). Expected risk: the prompt is long; the ordering PRE-FLIGHT GATE -> STEP 1-7 -> SIGNAL BOUNDARY CHECK -> 21-criterion SELF-CHECK is the primary guard against section confusion.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

Resolve all three fields from repo context before proceeding. This gate is a structural precondition -- scope boundary, break-even, and preliminary hypothesis must all be committed before STEP 1 or any other analysis section opens.

Out-of-scope boundary:
[What is explicitly NOT included in this sizing? Name at least one sub-system, phase, or integration excluded. If full scope: "No exclusions -- full scope assumed." Blank or "TBD" fails.]

Break-even signal:
[When does building this feature recover its cost vs. continuing the workaround? State a rough signal -- usage level, team count, or time horizon -- or explicitly: "Cannot assess -- [specific reason]." Absence fails.]

Preliminary hypothesis:
  Complexity tier: [LOW / MEDIUM / HIGH / XL -- one specific tier, commit. Failing form: "Hard to say without more analysis." If genuinely uncertain, pick LOW as default and note the uncertainty.]
  Timeline: [sprint range -- "N-M sprints" -- one range, commit.]
  Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: Do not proceed to STEP 1 or any STEP below until all three fields above contain specific responses. STEP 7 SYNTHESIS will confirm or revise the preliminary hypothesis committed here.

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- Workaround named; cost direction absent. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain long-term; the workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE. Do not embed unknowns here (e.g., "uncertainty about X may raise the tier") -- unknowns belong in STEP 6 OPEN UNKNOWNS. Tier sensitivity conditions are specific, testable external events, not uncertainty statements about internal scope.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension -- timeline sensitivity, not tier sensitivity |
| "Uncertainty about auth contracts may push to HIGH" | Embeds an unknown in sensitivity -- belongs in STEP 6 |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here. They go in STEP 6. Listing unknowns in the confidence section creates a second, unguarded record outside the canonical home -- this section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section. Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE. Do not include break-even observations here -- they were resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. Do not embed unknowns here -- they belong in STEP 6. Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE.

First, look back at PRE-FLIGHT GATE. State whether the analysis confirms, revises, or partially revises the preliminary hypothesis committed there:

- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation that requires both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it in light of the amendment. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction -- it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 21 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL -- no other form
- [ ] C-02: Timeline is a sprint range (N-M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent -> pass by default
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named -- must appear in PRE-FLIGHT GATE (canonical location)
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess -- [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in a named section separate from confidence basis, with Unknown: / Impact: / Movement: typed fields
- [ ] C-15: Preliminary hypothesis committed before analysis begins; synthesis explicitly confirms or revises it, naming the dimension that changed
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap -> pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains both scope boundary and break-even fields with specific responses; includes a stop instruction; inline reminders inside sections do not count
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (specifically STEP 5 CONFIDENCE) and at least one section adjacent to the scope exclusion canonical home (STEP 2 SURFACE AREA or STEP 3 COMPLEXITY) carry an explicit prohibition rule
- [ ] C-20: Every section that could plausibly receive scope exclusion content (STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY, STEP 7 SYNTHESIS) carries an explicit prohibition pointing to PRE-FLIGHT GATE as canonical home; every section that could plausibly receive unknowns content (STEP 3 COMPLEXITY, STEP 5 CONFIDENCE, STEP 7 SYNTHESIS) carries an explicit prohibition pointing to STEP 6 OPEN UNKNOWNS as canonical home. Any single unguarded plausible recipient fails C-20 -- minimum-pass C-19 coverage is insufficient.
- [ ] C-21: Preliminary hypothesis (complexity tier + timeline range) is a field INSIDE PRE-FLIGHT GATE -- not in MANDATORY OPENING or any standalone section after the gate. Synthesis references "the hypothesis committed in PRE-FLIGHT GATE" by name and explicitly confirms or revises it. Passing C-18 and C-15 independently does not satisfy C-21 if the hypothesis is outside the gate block.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full integration + dual enforcement + 21-criterion self-check

**Variation axes**: All R4 V-05 axes (gate, bilateral guards, preliminary hypothesis, self-indictment, AMEND cascade, 19-criterion self-check) + C-21 (hypothesis folded into gate) + C-20 (all plausible recipient sections closed) + self-check updated to 21 criteria with explicit structural definitions for C-20 and C-21

**Hypothesis**: R4 V-05 achieved 100/100 on v4 by combining structural mechanisms (prevent violations during generation) with a 19-criterion self-check (catch residuals before writing). V-05 R5 extends V-04 R5 in two ways: (1) the self-check items for C-20 and C-21 include explicit structural definitions that name the specific sections required and the specific conditions that disqualify a pass -- matching the dual-enforcement precision that C-18 and C-19 items achieved in R4 V-05; (2) the prohibition guards are maximally explicit: each prohibition names not just what is excluded but where that content belongs ("they were resolved in PRE-FLIGHT GATE" for scope exclusions; "they belong in STEP 6 OPEN UNKNOWNS" for unknowns), making the canonical home visible inside the guard itself. The dual-enforcement structure -- structural mechanisms prevent violations during generation; checklist with location-specific pass conditions catches residuals before writing -- was R4 V-05's core pattern. Applying it to C-20 and C-21 closes the loop for R5. Expected risk: length is the primary failure mode; the sequential label system (PRE-FLIGHT GATE -> STEP 1-7 -> SIGNAL BOUNDARY CHECK -> 21-criterion SELF-CHECK) and the stop instruction in the gate are the primary guards.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for every analysis step. Resolve them from repo context now. Do not proceed to STEP 1 or any STEP until all three fields contain specific responses -- "TBD" or blank fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10 before analysis begins.]

Preliminary hypothesis:
  Complexity tier: [LOW / MEDIUM / HIGH / XL -- one specific tier, commit now. Failing form: "Hard to say without more analysis." If genuinely uncertain, pick LOW as default and note the uncertainty.]
  Timeline: [sprint range -- "N-M sprints" -- one range, commit now. Point estimate or calendar date fails.]
  Reasoning: [one sentence -- what about the known scope signals this tier before analysis begins?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP until this gate is fully resolved. STEP 7 SYNTHESIS will confirm or revise the preliminary hypothesis committed here -- not a hypothesis constructed after sections are filled.

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain; workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE. Any note of the form "this workaround only applies within the scoped area" belongs in PRE-FLIGHT GATE, not here.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE, not in analysis steps. Noting a scope exclusion here creates a duplicate record outside the canonical home.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE, not in analysis steps. Do not embed unknowns or uncertainty statements here (e.g., "uncertainty about X may raise the tier") -- they belong in STEP 6 OPEN UNKNOWNS. Tier sensitivity conditions are specific external events that could become true, not statements about current uncertainty. This step is explicitly closed against both scope exclusion content and unknowns content.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension |
| "Uncertainty about auth contracts may push to HIGH" | Embeds an unknown -- belongs in STEP 6 |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here. They go in STEP 6. This section is explicitly closed against unknowns -- listing one here creates a second, unguarded record outside the canonical home that STEP 6 provides. The structural separation is what makes STEP 6 detectable as complete or incomplete.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section -- the structural separation from STEP 5 exists to make omissions visible, not to create a section that can be filled with vague language. Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE. Do not include break-even observations here -- they were resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6. Do not include scope exclusions here -- they were resolved in PRE-FLIGHT GATE. This step is explicitly closed against unknowns content and scope exclusion content.

First, look back at PRE-FLIGHT GATE. State whether the analysis confirms, revises, or partially revises the preliminary hypothesis committed there -- not a hypothesis formed after the sections were filled, but the specific commitment made in the gate:

- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction -- it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 21 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL -- no other form
- [ ] C-02: Timeline is a sprint range (N-M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent -> pass by default
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named -- must appear in PRE-FLIGHT GATE (canonical location); also acceptable anywhere else in the output
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess -- [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in a named section separate from confidence basis, with Unknown: / Impact: / Movement: typed fields
- [ ] C-15: Preliminary hypothesis committed before analysis begins; synthesis explicitly confirms or revises it, naming the dimension that changed
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap -> pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains both scope boundary and break-even fields with specific responses; includes a stop instruction; **inline reminders inside sections do not count**
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (specifically STEP 5 CONFIDENCE) and at least one section adjacent to the scope exclusion canonical home (STEP 2 SURFACE AREA or STEP 3 COMPLEXITY) carry an explicit prohibition rule -- not just that the canonical sections exist, but that their neighbors are closed
- [ ] C-20: **Every** plausible recipient section for scope exclusion content (STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY, STEP 7 SYNTHESIS) carries an explicit prohibition pointing to PRE-FLIGHT GATE as canonical home; **every** plausible recipient section for unknowns content (STEP 3 COMPLEXITY, STEP 5 CONFIDENCE, STEP 7 SYNTHESIS) carries an explicit prohibition pointing to STEP 6 OPEN UNKNOWNS as canonical home. Any single unguarded plausible recipient fails C-20 -- C-19 minimum-pass coverage is not sufficient.
- [ ] C-21: Preliminary hypothesis (complexity tier + timeline range) is a **field inside PRE-FLIGHT GATE** -- not in MANDATORY OPENING or any standalone section after the gate. Synthesis references "the hypothesis committed in PRE-FLIGHT GATE" by name and explicitly confirms or revises it. An output that passes C-18 (gate present) and C-15 (hypothesis present) independently still fails C-21 if the hypothesis is outside the gate block.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axes | C-20 bet | C-21 bet | C-09 | C-10 | C-14 | C-15 | C-18 | C-19 |
|----|------|----------|----------|------|------|------|------|------|------|
| V-01 | Gate-embedded hypothesis only | Low -- INERTIA CHECK and COMPLEXITY unguarded | **High** -- hypothesis is field 3 inside PRE-FLIGHT GATE | High | High | High | High -- synthesis references gate by name | High | High |
| V-02 | Full bilateral closure only | **High** -- INERTIA CHECK + COMPLEXITY guards added | Low -- hypothesis in MANDATORY OPENING after gate, not inside gate | High | High | High | High -- MANDATORY OPENING present | High | High |
| V-03 | Gate-embedded hypothesis + full bilateral closure (minimal) | **High** | **High** | High | High | High | High | High | High |
| V-04 | All R4 V-04 axes + C-21 + C-20 + 21-criterion self-check | **High** | **High** | **High** | **High** | **High** | **High** | **High** | **High** |
| V-05 | All R4 V-05 axes + C-21 + C-20 + dual enforcement + 21-criterion self-check | **High** | **High** | **High** | **High** | **High** | **High** | **High** | **High** |

**Key structural changes from R4:**

- **C-21 mechanism**: R4 V-04 and V-05 place MANDATORY OPENING: PRELIMINARY HYPOTHESIS as a separate section after PRE-FLIGHT GATE. The stop instruction prevents proceeding past the gate before scope/break-even are filled -- but the hypothesis is in a structurally independent section. R5 V-01, V-03, V-04, V-05 fold the hypothesis into PRE-FLIGHT GATE as a third required field: the gate sequence becomes scope boundary -> break-even -> preliminary hypothesis -> STOP. The hypothesis is now resolved inside the same atomic block as scope and break-even. SYNTHESIS explicitly references "the hypothesis committed in PRE-FLIGHT GATE" by name.

- **C-20 mechanism**: R4 V-04 and V-05 close SURFACE AREA, COMPLEXITY, and SYNTHESIS against scope exclusions; close CONFIDENCE and SYNTHESIS against unknowns. The unguarded plausible recipients are INERTIA CHECK (scope exclusion drift) and COMPLEXITY TIER sensitivity (unknowns drift). R5 V-02, V-03, V-04, V-05 add explicit prohibition guards to both: INERTIA CHECK ("Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE") and COMPLEXITY TIER AND DRIVER ("Do not embed unknowns here... they belong in STEP 6 OPEN UNKNOWNS. Tier sensitivity conditions are specific external events, not uncertainty statements").

- **V-02 single-axis design**: MANDATORY OPENING: PRELIMINARY HYPOTHESIS remains as a standalone section after the gate. This tests whether complete bilateral guard coverage (C-20) can be achieved without gate-embedded hypothesis (C-21). The known limitation: the hypothesis is in a standalone section after the gate, so C-21 is not targeted. This is the C-20 single-axis test.

- **Self-check evolution**: R4 V-05 has 19-criterion self-check. R5 V-04 adds C-20 and C-21 to reach 21 criteria, keeping R4 V-04's pattern (structural mechanisms without checklist definitions for the new items) to isolate structural mechanisms from dual enforcement. R5 V-05 updates checklist items to 21 with explicit structural definitions: C-20 names the specific sections that must be guarded (STEP 1, STEP 2, STEP 3, STEP 7 for scope exclusions; STEP 3, STEP 5, STEP 7 for unknowns); C-21 states that passing C-18 and C-15 independently does not satisfy C-21 if the hypothesis is outside the gate block.
