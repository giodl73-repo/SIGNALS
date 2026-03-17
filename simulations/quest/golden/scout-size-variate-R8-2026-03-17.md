---
skill: quest-variate
skill_target: scout-size
round: 8
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v8-2026-03-17.md
axes_explored: [structural-amend-directive, dedicated-failure-mode-blocks, minimal-combination-26-27, full-integration-27, dual-enforcement-27]
r7_champion: V-04/V-05 (18/19 on v8 rubric — fail C-26 only)
r7_gap: C-26 absent from V-01/V-03/V-04/V-05; C-27 absent from V-01/V-02/V-03
r8_target: C-26 (synthesis carries a written structural re-evaluation directive independent of whether AMEND fires), C-27 (every aspirational section with a nontrivial pass condition carries a dedicated labeled FAILURE MODE block)
---

# scout-size — Prompt Variations R8

Five complete, runnable skill body prompts targeting the v8 rubric (27 criteria). Single-axis first (V-01 through V-02), minimal combination (V-03), full integration (V-04), dual enforcement (V-05).

## Context: what informed this round

R7 produced V-04/V-05 as the variations scoring 17/17 on the v7 rubric. Under the v8 rubric (27 criteria), both score 18/19 — they fail only C-26. The v8 rubric formalizes two additional structural mechanisms sourced from R7 cross-variation analysis:

| New criterion | What it requires | R7 gap |
|---------------|-----------------|--------|
| **C-26** (structural AMEND directive) | Synthesis carries a written re-evaluation rule that applies independent of whether AMEND fires — the rule is a template property of the section, not a conditional instruction. An AMEND INSTRUCTION that reads "If an AMEND directive is present in this invocation...it fails C-16" is conditional and criterion-referenced, not structural. The structural form must state that re-evaluation applies on every invocation and frame non-compliance as a structural failure of the section's integrity, not a criterion failure. | R7 V-04/V-05 have a conditional AMEND INSTRUCTION ("it fails C-16") — behavioral, not structural. Only R7 V-02 carries the structural form (AMEND INSTRUCTION without criterion reference, framed as a section integrity rule). V-01/V-03/V-04/V-05 all fail C-26. |
| **C-27** (dedicated FAILURE MODE blocks) | Every aspirational section with a nontrivial pass condition — synthesis and open unknowns minimum — carries a dedicated labeled FAILURE MODE block or blockquote. Inline failure-mode text ("Restating sections is juxtaposition" inside a prose blockquote, or "a generic placeholder fails" as a trailing sentence) does not satisfy C-27 even if C-17 passes. The block must be structurally separate and labeled so that its absence is a visible structural gap, not an omission detectable only by re-reading. | R7 V-04/V-05 carry FAILURE MODE blockquotes in both STEP 6 OPEN UNKNOWNS and STEP 7 SYNTHESIS — they pass C-27. V-01/V-02/V-03 have only inline anti-pattern language — they fail C-27. |

**R8 design consequence**: C-26 and C-27 are orthogonal and have different structural homes:

- C-26 lives in SYNTHESIS — the structural directive replaces or supplements the conditional AMEND INSTRUCTION. A variation can add the directive without touching any other section.
- C-27 lives in OPEN UNKNOWNS and SYNTHESIS simultaneously — both sections must carry dedicated labeled blocks. A variation can add the blocks without changing any other structural mechanism.

**Under v8 rubric, R7 expected scores:**
- V-01 (gate + chain, no bilateral closure): 13/19 — fails C-20, C-23, C-25, C-26, C-27 (and C-24 due to no structured trace in that base)
- V-02 (bilateral closure + AMEND directive, no gate hypothesis): 14/19 — fails C-21, C-22, C-24, C-25, C-27
- V-03 (minimal combination, no failure-mode blocks): 15/19 — fails C-24, C-25, C-26, C-27
- V-04/V-05 (structured trace + FAILURE MODE blocks): 18/19 — fails C-26 only

**Three axes for R8:**
- **Axis A (V-01)**: Structural AMEND re-evaluation directive — adds STRUCTURAL AMEND RE-EVALUATION DIRECTIVE to synthesis as a section-level invariant, making C-26 the single-axis target; OPEN UNKNOWNS and SYNTHESIS retain inline anti-pattern language (C-27 intentionally absent). Base: R7 V-03 (passes C-01–C-25).
- **Axis B (V-02)**: Dedicated FAILURE MODE blocks — adds dedicated labeled FAILURE MODE blockquotes to both OPEN UNKNOWNS and SYNTHESIS, making C-27 the single-axis target; no structural AMEND directive present (C-26 intentionally absent). Base: R7 V-03.
- **Axis C (V-03)**: Minimal combination — adds both C-26 structural directive and C-27 FAILURE MODE blocks to R7 V-03 base, without self-check machinery.

---

## V-01 — Axis: Structural AMEND re-evaluation directive (C-26)

**Variation axis**: Behavior/structural mandate — synthesis carries a written re-evaluation rule framed as a section-level invariant that applies on every invocation, not only when AMEND fires. This is the single-axis test for C-26.

**Hypothesis**: C-26 is achievable by adding a structural directive to synthesis without any other changes. The key discriminator between C-26 PASS and FAIL is whether the AMEND handling is framed as a conditional instruction ("if AMEND is present, do X") or as a structural property of the section ("this section carries a re-evaluation requirement"). A directive that says "this requirement is a structural property of this section, not a conditional check" and frames non-compliance as "a structural failure of this section's integrity" satisfies C-26 regardless of whether AMEND fires. C-27 is intentionally absent: SYNTHESIS retains the inline `> **Anti-pattern**` blockquote, OPEN UNKNOWNS retains the inline "A generic placeholder fails" sentence. Expected pass: C-01–C-25, C-26. Expected fail: C-27.

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
  Failing: "2 engineers" — no disciplines, no ownership named.
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

A generic placeholder like "dependencies may exist" fails.

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

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds in light of the amendment. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Dedicated FAILURE MODE blocks (C-27)

**Variation axis**: Structure — both OPEN UNKNOWNS and SYNTHESIS carry dedicated labeled FAILURE MODE blockquotes as standalone structural elements, not inline anti-pattern language embedded in prose or trailing requirement sentences. This is the single-axis test for C-27.

**Hypothesis**: C-27 is achievable by adding dedicated FAILURE MODE blockquotes to OPEN UNKNOWNS and SYNTHESIS without any other changes to the R7 V-03 base. The discriminator is structural form, not content: the FAILURE MODE block must be a separate labeled element that a reader cannot scan past without noticing, making its absence a visible structural gap. Inline anti-pattern text in a prose blockquote (`> **Anti-pattern**: Restating sections is juxtaposition...`) passes C-17 but fails C-27 because it is embedded in the section instructions, not a standalone block. C-26 is intentionally absent — no structural AMEND directive appears in synthesis; only the inline content (commitment chain + verdict) is present. Expected pass: C-01–C-25, C-27. Expected fail: C-26.

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
  Failing: "2 engineers" — no disciplines, no ownership named.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here — unknowns belong in OPEN UNKNOWNS, not in the confidence basis.

---

## OPEN UNKNOWNS

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge placed in this section fails exactly as silently as an absent section — the structural separation from CONFIDENCE exists to make omissions visible, not to create a section that can be filled with vague language.

Canonical home for unverified items.
Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — unknowns belong here, not in those sections.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [specific unverified item — concrete, not generic]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

---

## SYNTHESIS

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here — they belong in OPEN UNKNOWNS. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

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

## V-03 — Axes: Structural AMEND directive (C-26) + dedicated FAILURE MODE blocks (C-27) — minimal combination

**Variation axes**: C-26 (structural AMEND re-evaluation directive in synthesis) + C-27 (dedicated labeled FAILURE MODE blocks in OPEN UNKNOWNS and SYNTHESIS) — both R8 mechanisms added to the R7 V-03 base (which already passes C-01–C-25), without self-check machinery.

**Hypothesis**: V-01 and V-02 test C-26 and C-27 independently. V-03 tests whether combining both on the R7 V-03 base achieves 19/19 without requiring the full step-labeled structure and self-check of R7 V-04/V-05. The gate forward-reference, bilateral closure mesh, navigational guards, and structured commitment-chain trace carry over from R7 V-03 unchanged. OPEN UNKNOWNS gains a dedicated FAILURE MODE blockquote before the field requirements (C-27 for unknowns). SYNTHESIS gains both a dedicated FAILURE MODE blockquote (C-27 for synthesis) and a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE after the commitment chain (C-26). If V-03 achieves 19/19 cleanly, it becomes the new minimum prompt for the v8 rubric. Expected risk: without a self-check, the FAILURE MODE blockquote in SYNTHESIS might be populated as content rather than treated as a structural instruction; the blockquote marker `>` and the labeled header `**FAILURE MODE FOR THIS SECTION**` are the primary guards.

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
  Failing: "2 engineers" — no disciplines, no ownership named.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here — unknowns belong in OPEN UNKNOWNS, not in the confidence basis.

---

## OPEN UNKNOWNS

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge placed here fails exactly as silently as an absent section — the structural separation from CONFIDENCE exists to make omissions visible, not to create a section that can be filled with vague language.

Canonical home for unverified items.
Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — unknowns belong here, not in those sections.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [specific unverified item — concrete, not generic]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

---

## SYNTHESIS

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here — they belong in OPEN UNKNOWNS. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines. A prose paragraph that folds the same information into a single sentence fails C-24 — the chain must be scannable without re-reading.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from analysis sections bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation. The recommendation must require both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds in light of the amendment. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — All R8 mechanisms + failure mode blockquotes + 27-criterion self-check

**Variation axes**: C-26 (structural AMEND re-evaluation directive) + C-27 (dedicated FAILURE MODE blocks in STEP 6 and STEP 7) + all R7 V-04 mechanisms (bilateral closure mesh, navigational guards, gate forward-reference, structured commitment-chain trace) + self-check updated to 27 criteria (adding C-26 and C-27 items).

**Hypothesis**: V-03 is the minimal combination achieving all 19 criteria. V-04 adds the step-labeled structure, WRONG/CORRECT examples in STEP 1 and STEP 3, failing-forms table in STEP 3, and the 27-criterion self-check. The C-26 self-check item defines what makes a directive structural vs. conditional ("a directive that ends 'it fails C-16' is conditional and criterion-referenced, not structural"). The C-27 self-check item defines what makes a block dedicated vs. inline ("an inline anti-pattern sentence embedded in a prose blockquote fails C-27 — the FAILURE MODE block must be a structurally separate labeled element"). The STEP 7 SYNTHESIS carries the STRUCTURAL AMEND RE-EVALUATION DIRECTIVE (not the old conditional AMEND INSTRUCTION), making C-26 a template property rather than a behavioral instruction. Expected risk: STEP 7 is now the longest section; the FAILURE MODE blockquote, commitment chain, and structural directive must all be present and distinguishable.

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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines. A prose paragraph that folds the same information into a single sentence fails C-24 — the chain must be scannable without re-reading.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1–6 bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 27 CRITERIA**

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
- [ ] C-15: Preliminary hypothesis (complexity tier + timeline range) is a field INSIDE PRE-FLIGHT GATE; synthesis explicitly confirms or revises it
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields; includes stop instruction
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5) and at least one adjacent to scope exclusion canonical home (STEP 2 or STEP 3) carry explicit prohibition rules
- [ ] C-20: Every plausible recipient for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) and unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition rule
- [ ] C-21: Preliminary hypothesis is a field INSIDE PRE-FLIGHT GATE — not in a standalone section after the gate; synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises the commitment
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both the anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") and in the verdict close form ("The preliminary hypothesis committed in PRE-FLIGHT GATE...")
- [ ] C-23: For at least one canonical field type (scope exclusions, open unknowns), prohibition guards in adjacent sections name the canonical home by label — "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" not "do not include scope exclusions here"
- [ ] C-24: Synthesis includes a Commitment chain block with three labeled lines (Gate commitment: / Analysis: / Verdict:) on separate lines; a prose paragraph that contains the same information fails C-24
- [ ] C-25: PRE-FLIGHT GATE (after the STOP instruction) names at least two downstream sections responsible for enforcing scope exclusions AND names the section responsible for hypothesis confirmation or revision
- [ ] C-26: Synthesis contains a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE that applies independent of whether AMEND is present — not a conditional instruction ("If an AMEND directive is present...it fails C-16"). The passing form must state that the requirement "applies on every invocation, independent of whether an AMEND directive is present" and frame non-compliance as "a structural failure of this section's integrity."
- [ ] C-27: Both OPEN UNKNOWNS (STEP 6) and SYNTHESIS (STEP 7) carry a dedicated labeled FAILURE MODE block (`> **FAILURE MODE FOR THIS SECTION**:`). An inline anti-pattern sentence embedded in a prose blockquote (`> **Anti-pattern**: Restating...`) fails C-27 even if C-17 passes — the block must be a structurally separate labeled element, not part of the section's instruction prose.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full integration + dual enforcement + structural definitions for C-26/C-27

**Variation axes**: All R8 V-04 axes + self-check items for C-26 and C-27 extended with structural disqualifying conditions naming the exact written form that fails each criterion, mirroring the dual-enforcement pattern from R5/R6/R7 V-05.

**Hypothesis**: V-04 adds C-26 and C-27 to the 27-criterion self-check with definition-level descriptions. V-05 extends those definitions with the exact structural disqualifying condition — the same pattern that made V-05 the highest-reliability variation in every round since R5. For C-26, the disqualifying condition is: "a directive reading '**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis...Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16' fails C-26 even if it is present in synthesis — 'in this invocation' makes it conditional, 'it fails C-16' makes it criterion-referenced rather than a structural property of the section." For C-27, the disqualifying condition is: "a FAILURE MODE blockquote that reads `> **Anti-pattern**: Restating sections in sequence is juxtaposition` fails C-27 even if it is present in synthesis — it is a structural annotation inside the section's instructions, not a dedicated labeled block that is absent with a visible gap." The self-check item for each criterion names the exact disqualifying form so the model can identify violations before writing, not discover them through scoring. V-05 is the highest-reliability form of the v8 rubric: structural mechanisms prevent violations during generation; the 27-criterion checklist with structural definitions catches residuals before the artifact is written.

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

The verdict close must name PRE-FLIGHT GATE by label — not a hypothesis constructed after the sections were filled, but the specific commitment made in the gate. Writing "my earlier estimate was confirmed" fails C-22. Writing the verdict as a prose paragraph that contains all three chain steps fails C-24.

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 27 CRITERIA**

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
- [ ] C-15: Preliminary hypothesis (complexity tier + timeline range) is a field INSIDE PRE-FLIGHT GATE — not in a standalone section after the gate. Synthesis explicitly confirms or revises it, naming the changed dimension.
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields with specific responses; includes stop instruction; inline reminders inside sections do not count
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5) and at least one adjacent to the scope exclusion canonical home (STEP 2 or STEP 3) carry an explicit prohibition rule
- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) carries an explicit prohibition. Every plausible recipient section for unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition. Any single unguarded plausible recipient fails C-20.
- [ ] C-21: Preliminary hypothesis is a field inside PRE-FLIGHT GATE — not in a standalone section after the gate. Synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises it. Passing C-18 and C-15 independently still fails C-21 if the hypothesis is outside the gate block.
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both ends: (1) anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") AND (2) verdict close ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). Disqualifying form: "My earlier estimate was confirmed" fails C-22 — it refers to the hypothesis without naming the structural site.
- [ ] C-23: For at least one canonical field type, prohibition guards in adjacent sections name the canonical home by label. Passing: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps." Failing: "do not include scope exclusions here" — excludes without redirecting.
- [ ] C-24: Synthesis includes a Commitment chain block with three labeled lines on separate lines: Gate commitment: / Analysis: / Verdict:. Disqualifying form: a sentence reading "The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3–5 sprints) is confirmed: surface area is LOW and inertia cost is HIGH" fails C-24 even if it passes C-22 — the three chain steps are embedded in one sentence, not independently scannable.
- [ ] C-25: PRE-FLIGHT GATE (after the STOP instruction) includes an enforcement contract that names at least two downstream sections responsible for scope exclusions AND names the section responsible for hypothesis confirmation or revision. Disqualifying form: "All three fields above are preconditions for STEP 1 through STEP 7" fails C-25 — naming steps as a continuation instruction is not an enforcement contract distinguishing scope vs. hypothesis enforcement.
- [ ] C-26: Synthesis contains a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE stating the requirement applies on every invocation "independent of whether an AMEND directive is present" and framing non-compliance as "a structural failure of this section's integrity." Disqualifying form: "**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis...Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16" fails C-26 — "in this invocation" makes it conditional; "it fails C-16" makes it criterion-referenced rather than a structural property. Both disqualifiers must be absent for C-26 to pass.
- [ ] C-27: Both STEP 6 OPEN UNKNOWNS and STEP 7 SYNTHESIS carry a dedicated labeled FAILURE MODE block (`> **FAILURE MODE FOR THIS SECTION**:`) as a structurally separate element. Disqualifying form: a blockquote reading `> **Anti-pattern**: Restating sections in sequence is juxtaposition` in SYNTHESIS fails C-27 even if C-17 passes — it is a structural annotation embedded in the section's instruction prose, not a dedicated block whose absence creates a visible structural gap. Similarly, an inline sentence "A generic placeholder fails" at the end of OPEN UNKNOWNS's requirements list fails C-27 — it is embedded in the requirements prose, not a standalone labeled block.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axes | C-26 | C-27 | Self-check |
|----|------|------|------|------------|
| V-01 | Structural AMEND directive only | **PASS** — written as section-level invariant, applies independent of AMEND | **FAIL** (intentional) — inline `> **Anti-pattern**` in SYNTHESIS, inline "generic placeholder fails" in OPEN UNKNOWNS | None |
| V-02 | Dedicated FAILURE MODE blocks only | **FAIL** (intentional) — no AMEND directive present | **PASS** — dedicated `> **FAILURE MODE FOR THIS SECTION**:` blocks in both OPEN UNKNOWNS and SYNTHESIS | None |
| V-03 | Minimal combination (C-26 + C-27) | **PASS** | **PASS** | None |
| V-04 | All R8 mechanisms + 27-criterion self-check | **PASS** | **PASS** | 27 criteria |
| V-05 | Full integration + structural definitions for C-26/C-27 | **PASS** | **PASS** | 27 criteria + disqualifying forms |

**Expected scores under v8:**

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 5/5 | 3/3 | 18/19 (fails C-27) | 99.47 |
| V-02 | 5/5 | 3/3 | 18/19 (fails C-26) | 99.47 |
| V-03 | 5/5 | 3/3 | 19/19 | **100** |
| V-04 | 5/5 | 3/3 | 19/19 | **100** |
| V-05 | 5/5 | 3/3 | 19/19 | **100** |

**Key design differences from R7:**

- **C-26 mechanism**: R7 V-04/V-05 have a conditional AMEND INSTRUCTION ("If an AMEND directive is present in this invocation...it fails C-16") — the phrase "in this invocation" makes the directive conditional on AMEND firing; "it fails C-16" frames it as a behavioral criterion reference. R8 V-01/V-03/V-04/V-05 replace this with a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE that explicitly states the requirement "applies on every invocation, independent of whether an AMEND directive is present" and frames non-compliance as "a structural failure of this section's integrity." These two discriminators — unconditional scope and structural (not criterion) framing — are the minimum structural properties required for C-26 to pass.

- **C-27 mechanism**: R7 V-01/V-02/V-03 have inline failure-mode language in SYNTHESIS (`> **Anti-pattern**: Restating sections is juxtaposition`) and either inline text or no failure-mode coverage in OPEN UNKNOWNS. R8 V-02/V-03/V-04/V-05 replace these with dedicated `> **FAILURE MODE FOR THIS SECTION**:` blockquotes placed before the field requirements in each section, so that the block is present as a structurally independent element whose absence would leave a visible gap. R7 V-04/V-05 already had this form and pass C-27 unchanged.

- **V-01 single-axis design**: Intentionally keeps OPEN UNKNOWNS inline ("A generic placeholder fails" trailing sentence) and SYNTHESIS inline (`> **Anti-pattern**:` blockquote). Tests whether the STRUCTURAL AMEND RE-EVALUATION DIRECTIVE alone achieves C-26 without dedicated FAILURE MODE blocks. All other R7 V-03 mechanisms preserved.

- **V-02 single-axis design**: Intentionally omits any AMEND directive from SYNTHESIS (C-26 fails by absence). Tests whether adding dedicated FAILURE MODE blocks to both OPEN UNKNOWNS and SYNTHESIS alone achieves C-27 without a structural AMEND directive. All other R7 V-03 mechanisms preserved.

- **Self-check evolution**: R7 V-05 has a 25-criterion self-check. R8 V-04 adds C-26 and C-27 as explicit self-check items with definition-level descriptions. R8 V-05 extends those definitions with structural disqualifying forms — naming exactly what written output fails each criterion, so the model can identify violations before writing rather than discover them through external scoring.
