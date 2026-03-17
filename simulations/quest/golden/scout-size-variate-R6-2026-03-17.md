---
skill: quest-variate
skill_target: scout-size
round: 6
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v6-2026-03-17.md
axes_explored: [synthesis-named-chain, navigational-guards, minimal-combination, full-integration-23, dual-enforcement-23]
r5_champion: V-03/V-04/V-05 (100/100 on v5 rubric, 15/15 on v6 rubric)
r5_gap: C-22/C-23 absent from V-01 and V-02 — new criteria sourced from R5 scoring analysis
r6_target: C-22 (synthesis names PRE-FLIGHT GATE at both anchor and verdict close), C-23 (prohibition guards name canonical home by label, not bare exclusion)
---

# scout-size — Prompt Variations R6

Five complete, runnable skill body prompts targeting the v6 rubric (23 criteria). Single-axis first (V-01 through V-02), minimal combination (V-03), full integration (V-04), dual enforcement (V-05).

## Context: what informed this round

R5 produced V-03/V-04/V-05 as the variations that pass all 13 aspirational criteria on v5 (13/13). The v6 rubric formalizes two additional structural mechanisms sourced from R5 excellence analysis:

| New criterion | What it requires | R5 gap |
|---------------|-----------------|--------|
| **C-22** (synthesis names gate at both ends) | Synthesis explicitly names PRE-FLIGHT GATE when anchoring the prior commitment ("the hypothesis committed in PRE-FLIGHT GATE") AND when stating the verdict close — each template must include "PRE-FLIGHT GATE" by label, not "my earlier estimate" | R5 V-01 passes C-21 (hypothesis in gate, synthesis confirms it) but the verdict close templates use a form like "Hypothesis confirmed: [tier]..." without the structural label. C-22 requires the label at both the anchor instruction AND the verdict template close. R5 V-02 fails C-22 entirely because hypothesis is in standalone MANDATORY OPENING — synthesis references that section, not PRE-FLIGHT GATE |
| **C-23** (prohibition guards name canonical home) | Prohibition guards in adjacent sections do not merely exclude ("do not include scope exclusions here") but navigate ("do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps"). At least one guard per canonical field type names the home section by label. Bare exclusions are dead ends; navigational redirects complete the containment chain | R5 V-01 fails C-23 because the existing guards in SURFACE AREA and COMPLEXITY use bare exclusion form without naming PRE-FLIGHT GATE as the home. R5 V-02 passes C-23 because its full bilateral closure guards include navigational references — the INERTIA CHECK guard reads "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" |

**R6 design consequence**: C-22 and C-23 are orthogonal and have different prerequisites:

- C-22 requires C-21 (hypothesis in gate) as structural prerequisite — you cannot name the gate in the verdict close if the hypothesis was never committed there. A variation that fails C-21 automatically fails C-22. Testing C-22 in isolation means starting from a base that already passes C-21.
- C-23 does not require C-20 (full bilateral closure). The criterion requires at least one guard (per canonical field type) to use the navigational form — not all adjacent sections. A variation can pass C-23 with only some guards while failing C-20 if other sections remain unguarded.

**Under v6 rubric, R5 expected scores:**
- V-01 (gate-embedded hypothesis): 13/15 — passes C-21, C-22; fails C-20 (INERTIA CHECK unguarded, COMPLEXITY unguarded for unknowns), C-23 (bare exclusion guards)
- V-02 (full bilateral closure): 13/15 — passes C-20, C-23; fails C-21 (hypothesis standalone), C-22 (hypothesis not in gate, synthesis references MANDATORY OPENING)
- V-03/V-04/V-05: 15/15 — all criteria pass

**Three axes for R6:**
- **Axis A (V-01)**: Synthesis named chain — gate-embedded hypothesis (C-21) with verdict close templates that explicitly include "PRE-FLIGHT GATE" by label (C-22); bare exclusion guards kept (C-23 expected fail); INERTIA CHECK left unguarded (C-20 expected fail)
- **Axis B (V-02)**: Navigational guards — all prohibition guards redirect to canonical home by name (C-23); standalone hypothesis after gate (C-21 fail); synthesis references MANDATORY OPENING, not PRE-FLIGHT GATE (C-22 fail)
- **Axis C (V-03)**: Minimal combination — gate-embedded hypothesis + synthesis named chain + navigational guards, no self-check machinery

---

## V-01 — Axis: Synthesis named chain (C-22)

**Variation axis**: Synthesis — verdict close templates explicitly include "PRE-FLIGHT GATE" by label at both the anchor instruction and the template close, making the gate-to-synthesis chain structurally traceable at both ends.

**Hypothesis**: R5 V-01 passes C-21 (hypothesis inside gate, synthesis confirms it) but the verdict close templates do not embed "PRE-FLIGHT GATE" as a required label in the written output. The synthesis instruction says "look back at PRE-FLIGHT GATE" at the anchor, but the closing templates read "Hypothesis confirmed: [tier] at [sprint range] because..." — the gate label disappears at the verdict. C-22 requires the gate to be named TWICE in the output: once when anchoring the prior commitment, once in the verdict close. The fix is mechanical: verb the verdict close templates to start with "The preliminary hypothesis committed in PRE-FLIGHT GATE..." so the model cannot write a verdict that does not name the gate. Expected pass: C-21 (hypothesis in gate), C-22 (gate named at anchor + verdict close). Expected fail: C-20 (INERTIA CHECK unguarded, COMPLEXITY unguarded for unknowns drift), C-23 (guards are bare exclusions — they exclude but do not redirect). The guard failure is intentional: this is a single-axis test for C-22 only.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## PRE-FLIGHT GATE

Resolve all three fields before filling any section below. This is a structural gate — scope boundary, break-even, and preliminary hypothesis must be committed from repo context before analysis begins. Do not proceed until all three fields contain specific responses.

Out-of-scope boundary:
[Name at least one sub-system, behavior, integration, or phase explicitly NOT covered by this sizing. If genuinely full scope: "No exclusions — full scope assumed." Do not say "TBD." Blank fails.]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? Rough signal is sufficient: "breaks even at 3+ teams using weekly." If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit to a range now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to INERTIA CHECK or any section below until this gate is fully resolved.

---

## INERTIA CHECK

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, or qualitative estimate]
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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises that commitment. Use exactly one of the following forms. The gate label is required in the verdict close:

- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

"My earlier estimate was confirmed" fails C-22 — it names no structural site. The verdict close must include "PRE-FLIGHT GATE" by label.

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state — it must not be derivable from any single dimension alone.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Navigational guards (C-23)

**Variation axis**: Output format — all prohibition guards are navigational redirects, naming the canonical home section by label rather than stating a bare exclusion. Tests whether C-23 can be achieved without C-21 (standalone hypothesis) and confirms that C-23 is independent of gate structure.

**Hypothesis**: R5 V-02 achieves full bilateral closure (C-20) with guards that already include navigational form in some sections ("scope was resolved in PRE-FLIGHT GATE, not in analysis steps"). The C-23 test for R5 V-02 is whether those guards consistently name the home across ALL canonical field types (scope exclusions to PRE-FLIGHT GATE, unknowns to OPEN UNKNOWNS). V-02 here starts from the standalone-hypothesis structure (hypothesis in MANDATORY OPENING after gate, not inside gate block) — this intentionally fails C-21 and C-22 to isolate the C-23 single-axis test. The SCOPE EXCLUSIONS canonical home is at the end (like R4 V-02), but all adjacent section guards point to it by name. Expected pass: C-20 (full bilateral closure), C-23 (every guard names the canonical home). Expected fail: C-21 (hypothesis outside gate), C-22 (C-21 prerequisite unmet — synthesis references MANDATORY OPENING, not PRE-FLIGHT GATE).

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

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE, not in analysis steps. Noting them here creates a duplicate record outside their canonical home (SCOPE EXCLUSIONS below).

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

## SCOPE EXCLUSIONS

Canonical home for out-of-scope items. Do not put scope exclusions in SURFACE AREA, COMPLEXITY, INERTIA CHECK, or SYNTHESIS — those sections are closed against scope content; this section is their canonical home.

State at least one explicit exclusion, assumption, or boundary. If full scope: "No exclusions — full scope assumed."

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axes: Synthesis named chain + navigational guards (minimal combination)

**Variation axes**: C-22 (synthesis names PRE-FLIGHT GATE at both anchor and verdict close) + C-23 (all prohibition guards are navigational redirects naming canonical home) — both new R6 mechanisms combined in the simplest possible structure, without self-check machinery.

**Hypothesis**: V-01 and V-02 test C-22 and C-23 independently. V-03 tests whether combining both in the minimal structure achieves all 15 criteria without requiring the full failure-mode blockquote and self-check machinery from R5 V-04/V-05. The gate is three-field (scope boundary → break-even → preliminary hypothesis → STOP), so C-21 is preserved. The synthesis templates include "PRE-FLIGHT GATE" at both the anchor instruction and the verdict close forms, so C-22 is preserved. All prohibition guards use the navigational redirect form naming the canonical home, so C-23 is preserved. The full bilateral coverage guards INERTIA CHECK and COMPLEXITY against all plausible recipients, so C-20 is preserved. If V-03 passes all 15 criteria cleanly, it becomes the new minimum prompt. Expected risk: without failure-mode blockquotes or checklist enforcement, synthesis may revert to juxtaposition under execution; the verdict close template rigidity (requiring "committed in PRE-FLIGHT GATE" as a written phrase) is the primary structural guard against that regression.

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

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE. Use exactly one of the following forms. The phrase "preliminary hypothesis committed in PRE-FLIGHT GATE" is required in the verdict close:

- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation. The recommendation must require both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: All R6 mechanisms + failure mode blockquotes + 23-criterion self-check

**Variation axes**: C-22 (synthesis named chain) + C-23 (navigational guards) + all R5 V-04 mechanisms (failure mode blockquotes in SYNTHESIS and OPEN UNKNOWNS, AMEND cascade, 21-criterion self-check) + self-check updated to 23 criteria (adding C-22 and C-23 items)

**Hypothesis**: V-03 is the minimal combination achieving all 15 criteria. V-04 adds the failure-mode blockquotes (naming anti-patterns in SYNTHESIS and OPEN UNKNOWNS — C-17) and the AMEND cascade (C-16), then updates the self-check to 23 criteria including explicit C-22 and C-23 items. The dual-enforcement pattern from R5 V-04 is preserved: structural mechanisms prevent violations during generation, while the 23-criterion checklist catches residuals before writing. The C-22 self-check item defines the exact disqualifying form ("'My earlier estimate was confirmed' fails C-22 — it names no structural site"). The C-23 self-check item defines what counts as a navigational redirect vs. a bare exclusion. Expected risk: the prompt length increases; the sequential ordering (PRE-FLIGHT GATE → STEP 1–7 → SIGNAL BOUNDARY CHECK → 23-criterion SELF-CHECK) and the stop instruction in the gate are the primary guards against section confusion.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE — complete before any analysis begins**

All three fields below are preconditions for all analysis sections. Resolve them from repo context now. Do not proceed until all three fields contain specific responses — "TBD" or blank fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If genuinely full implementation scope: "No exclusions — full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? State a rough signal or explicitly: "Cannot assess — [specific reason]." Absence fails C-10 before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit to one tier now]
Timeline: [N–M sprints — commit now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this gate is fully resolved.

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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE. Use exactly one of the following forms. The phrase "preliminary hypothesis committed in PRE-FLIGHT GATE" is required in the verdict close — "my earlier estimate was confirmed" fails because it names no structural site:

- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

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

**SELF-CHECK — ALL 23 CRITERIA**

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
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both the anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") and in the verdict close template form ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). "My earlier estimate was confirmed" fails — it names no structural site. The gate label must appear in what is written, not only in the instruction.
- [ ] C-23: For at least one canonical field type (scope exclusions, open unknowns), the prohibition guards in adjacent sections name the canonical home by label — "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" not "do not include scope exclusions here." A guard that only excludes without redirecting fails C-23.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full integration + dual enforcement + structural definitions for C-22/C-23

**Variation axes**: All R6 V-04 axes + self-check items for C-22 and C-23 extended with structural definitions that name exact disqualifying conditions, mirroring the structural definition pattern from R5 V-05 for C-20/C-21.

**Hypothesis**: V-04 adds C-22 and C-23 to the 23-criterion self-check with definition-level descriptions. V-05 extends those definitions to include the exact structural disqualifying condition — the same dual-enforcement pattern that made R5 V-05 the highest-reliability variation: the checklist items for C-20 and C-21 named the exact sections required and the exact conditions that disqualify a pass, making compliance self-auditable before writing. For C-22, the disqualifying condition is "synthesis references the hypothesis without naming its structural site ('my earlier estimate' instead of 'PRE-FLIGHT GATE') — this fails C-22 even if C-21 is satisfied." For C-23, the disqualifying condition is "guards that state exclusion without naming the destination fail C-23 — 'do not include scope exclusions here' with no 'scope was resolved in PRE-FLIGHT GATE' is a dead end, not a navigational redirect." The self-check item for each criterion names the exact disqualifying form so the model can identify violations before writing, not discover them through scoring. V-05 is the highest-reliability form of the v6 rubric: structural mechanisms prevent violations during generation; the 23-criterion checklist with structural definitions catches any residuals.

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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE. Use exactly one of the following forms. The phrase "preliminary hypothesis committed in PRE-FLIGHT GATE" is required in the verdict close:

- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

The verdict close must name PRE-FLIGHT GATE by label — not a hypothesis constructed after the sections were filled, but the specific commitment made in the gate. Writing "my earlier estimate was confirmed" fails C-22 because it does not identify the structural site where the commitment was made.

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

**SELF-CHECK — ALL 23 CRITERIA**

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
- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY, STEP 7 SYNTHESIS) carries an explicit prohibition. Every plausible recipient section for unknowns content (STEP 3 COMPLEXITY, STEP 5 CONFIDENCE, STEP 7 SYNTHESIS) carries an explicit prohibition. Any single unguarded plausible recipient fails C-20 — C-19 minimum-pass coverage is not sufficient.
- [ ] C-21: Preliminary hypothesis (complexity tier + timeline range) is a field inside PRE-FLIGHT GATE — not in MANDATORY OPENING or any standalone section after the gate. Synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises it. Passing C-18 (gate present) and C-15 (hypothesis present) independently still fails C-21 if the hypothesis is outside the gate block.
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both ends of the verification chain: (1) at the anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") AND (2) in the verdict close template form ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). The disqualifying form: "My earlier estimate was confirmed" fails C-22 even if C-21 passes — it refers to the hypothesis without naming the structural site. The gate label must appear in what the model writes in the verdict, not only in the instruction.
- [ ] C-23: For at least one canonical field type (scope exclusions, open unknowns), the prohibition guards in adjacent sections name the canonical home by label. Passing: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps." Failing: "do not include scope exclusions here" — this is a dead end that excludes without redirecting. An output can pass C-20 (all adjacent sections guarded) and still fail C-23 if no guard names where the excluded content belongs.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axes | C-21 | C-22 | C-20 | C-23 | Self-check |
|----|------|------|------|------|------|------------|
| V-01 | Synthesis named chain only | **High** — hypothesis in gate | **High** — verdict close templates require "PRE-FLIGHT GATE" label | Low — INERTIA CHECK unguarded | Low — bare exclusion guards, no home reference | None |
| V-02 | Navigational guards only | Low — standalone MANDATORY OPENING | Low — C-21 prerequisite unmet | **High** — full bilateral closure | **High** — all guards redirect to canonical home by name | None |
| V-03 | Named chain + navigational guards (minimal) | **High** | **High** | **High** | **High** | None |
| V-04 | Named chain + navigational guards + failure modes + 23-criterion self-check | **High** | **High** | **High** | **High** | 23 criteria |
| V-05 | Full integration + 23-criterion self-check + structural definitions for C-22/C-23 | **High** | **High** | **High** | **High** | 23 criteria + definitions |

**Expected scores under v6:**

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 5/5 | 3/3 | 13/15 (fails C-20, C-23) | 98.67 |
| V-02 | 5/5 | 3/3 | 13/15 (fails C-21, C-22) | 98.67 |
| V-03 | 5/5 | 3/3 | 15/15 | **100** |
| V-04 | 5/5 | 3/3 | 15/15 | **100** |
| V-05 | 5/5 | 3/3 | 15/15 | **100** |

**Key design differences from R5:**

- **C-22 mechanism**: R5 V-01/V-03/V-04/V-05 achieve C-21 and C-22 (under v6) because synthesis says "look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there." R6 V-01 makes the verdict close templates mechanically enforce the label: each template begins "The preliminary hypothesis committed in PRE-FLIGHT GATE..." so the gate label is required in what the model writes, not only in the instruction preamble. The synthesis instruction alone is not sufficient for reliable C-22 compliance — the template form is the structural enforcement.

- **C-23 mechanism**: R5 V-02/V-03/V-04/V-05 achieve C-23 because the INERTIA CHECK guard reads "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" — naming the canonical home, not just stating exclusion. R6 makes this pattern explicit in all adjacent sections and both canonical field types. The pattern distinction is dead-end vs. navigational: "do not include scope exclusions here" closes a door; "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" closes the door AND points to the room.

- **V-01 single-axis design**: Intentionally leaves INERTIA CHECK unguarded (C-20 fails) and uses bare exclusion form in SURFACE AREA/COMPLEXITY guards (C-23 fails). Tests whether the synthesis named chain alone (C-22) is achievable without the navigational guard pattern. The gate remains three-field atomic (C-21 preserved).

- **V-02 single-axis design**: Intentionally places hypothesis in standalone MANDATORY OPENING after the gate (C-21, C-22 fail). Tests whether navigational guards alone (C-23) and full bilateral closure (C-20) are achievable without gate-embedded hypothesis. Includes SCOPE EXCLUSIONS as a canonical section at the end (like R4/R5 V-02 structure), but all adjacent section guards now use the navigational redirect form.

- **Self-check evolution**: R5 V-05 has a 21-criterion self-check. R6 V-04 adds C-22 and C-23 as explicit self-check items with definition-level descriptions. R6 V-05 extends those definitions with structural definitions that name the exact disqualifying forms — mirroring how R5 V-05 defined disqualifying conditions for C-20 ("any single unguarded plausible recipient fails C-20") and C-21 ("passing C-18 and C-15 independently still fails C-21 if the hypothesis is outside the gate block"). This pattern has consistently been the highest-reliability enforcement mechanism across R3, R4, and R5.
