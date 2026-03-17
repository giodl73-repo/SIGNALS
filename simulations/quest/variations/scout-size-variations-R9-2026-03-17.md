Written to `simulations/quest/variations/scout-size-variations-R9-2026-03-17.md`.

---

## R9 Variations — scout-size (Round 9)

**Rubric**: v9 (29 criteria) | **New targets**: C-28, C-29 | **Baseline**: R8 V-03/V-04/V-05 (all 19/19 under v8)

### Variation summary

| ID | Axis | C-26 | C-27 | C-28 | C-29 | v9 score |
|----|------|------|------|------|------|----------|
| **V-01** | Structural AMEND directive only | PASS | **FAIL** (intentional — inline anti-pattern) | FAIL | FAIL | 16/21 (97.62) |
| **V-02** | Dedicated FAILURE MODE blocks only | **FAIL** (intentional — no directive) | PASS | FAIL | FAIL | 16/21 (97.62) |
| **V-03** | C-26 + C-27 combined, no self-check | PASS | PASS | **FAIL** | FAIL | 19/21 (99.05) |
| **V-04** | All V-03 + 29-criterion self-check, exact disqualifying forms for C-26/C-27 only | PASS | PASS | PASS | **FAIL** | 20/21 (99.52) |
| **V-05** | Full integration — uniform structural precision across C-18–C-27 | PASS | PASS | PASS | PASS | **21/21 (100.00)** |

### What each variation tests

**V-01 (single axis — inertia framing)**: Establishes that the structural AMEND directive alone (C-26) does not produce the section-level FAILURE MODE blocks (C-27) or the collective self-check (C-28). The inline `> **Anti-pattern**:` blockquote in SYNTHESIS and the trailing "A generic placeholder fails" sentence in OPEN UNKNOWNS are structurally embedded in instruction prose — the missing dedicated block is the discriminating signal.

**V-02 (single axis — output format)**: Establishes that dedicated FAILURE MODE blocks (C-27) do not produce the structural AMEND directive (C-26) or the collective self-check (C-28). Section-level structural elements and a collective audit artifact are different things.

**V-03 (single axis — lifecycle emphasis)**: Establishes the C-28/C-29 gap cleanly. C-27's FAILURE MODE blocks are section-level; C-28 requires a *distinct collective artifact*. V-03 is the new minimum for the v8 rubric but reveals the two new v9 gaps.

**V-04 (combined — phrasing register + output format)**: Self-check covers all 29 criteria with explicit Status+Evidence per criterion (satisfies C-28). Exact disqualifying forms appear only for C-26 and C-27 — the latest-round criteria. C-18–C-21 have pass conditions only. C-28/C-29 are definition-level. This is the natural incremental pattern that falls one step short of C-29.

**V-05 (full integration — role sequence + lifecycle emphasis + output format)**: Self-check with exact disqualifying forms for *all* structural criteria C-18–C-27 uniformly, plus exact disqualifying forms for C-28 and C-29 themselves. Coverage uniformity across all structural criteria regardless of which round introduced them is the R9 gold standard.
ny content section.
- C-29 requires uniform structural precision inside the self-check — a variation can achieve C-28 with a complete trace and still fail C-29 if the structural disqualifying forms cover only the latest-round criteria.

**Under v9 rubric, R8 expected scores:**
- V-01 (structural AMEND directive only): 16/21 — fails C-27, C-28, C-29
- V-02 (dedicated FAILURE MODE blocks only): 16/21 — fails C-26, C-28, C-29
- V-03 (C-26 + C-27, no self-check): 19/21 — fails C-28, C-29
- V-04 (C-26 + C-27 + self-check, C-26/C-27 exact disqualifying forms only): 20/21 — fails C-29
- V-05 (full integration + uniform structural precision C-18–C-27): 21/21

**Three axes for R9:**
- **Axis A (V-01)**: Structural AMEND directive only — C-27 intentionally absent; no self-check.
- **Axis B (V-02)**: Dedicated FAILURE MODE blocks only — C-26 intentionally absent; no self-check.
- **Axis C (V-03)**: Minimal combination — C-26 and C-27 both present; no self-check. Tests whether section-level structural mechanisms alone reach C-28 (they do not).

---

## V-01 — Axis: Structural AMEND re-evaluation directive only (C-26)

**Variation axis**: Behavior/structural mandate — synthesis carries a written re-evaluation rule framed as a section-level invariant that applies on every invocation. This is the single-axis test for C-26.

**Hypothesis**: C-26 is achievable by adding a structural directive to synthesis without any other changes. C-27 is intentionally absent: SYNTHESIS retains an inline `> **Anti-pattern**:` blockquote; OPEN UNKNOWNS retains an inline "A generic placeholder fails" sentence. C-28 and C-29 are intentionally absent: no per-criterion self-check block is present. Expected pass: C-01–C-25, C-26. Expected fail: C-27, C-28, C-29. Score under v9: 16/21 aspirational.

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

> **Anti-pattern**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. Do not embed unknowns here — they belong in OPEN UNKNOWNS. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from analysis sections bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds in light of the amendment. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Dedicated FAILURE MODE blocks only (C-27)

**Variation axis**: Structure — OPEN UNKNOWNS and SYNTHESIS each carry a dedicated labeled `> **FAILURE MODE FOR THIS SECTION**:` blockquote as a standalone structural element, not inline anti-pattern language. This is the single-axis test for C-27.

**Hypothesis**: C-27 is achievable by adding dedicated FAILURE MODE blockquotes to OPEN UNKNOWNS and SYNTHESIS without any other changes. C-26 is intentionally absent — no STRUCTURAL AMEND RE-EVALUATION DIRECTIVE appears in synthesis. C-28 and C-29 are intentionally absent. Expected pass: C-01–C-25, C-27. Expected fail: C-26, C-28, C-29. Score under v9: 16/21 aspirational.

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

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section — the structural separation from CONFIDENCE exists to make omissions visible, not to create a section that can be filled with vague language.

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

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from analysis sections bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axes: C-26 + C-27 combined, no self-check

**Variation axes**: Structural AMEND re-evaluation directive (C-26) + dedicated FAILURE MODE blocks in OPEN UNKNOWNS and SYNTHESIS (C-27) — both R8 mechanisms on the baseline, without self-check machinery.

**Hypothesis**: V-01 and V-02 test C-26 and C-27 independently. V-03 confirms that combining both achieves 19/19 under v8 and establishes the C-28/C-29 gap cleanly: section-level FAILURE MODE blocks (C-27) are distinct from the collective per-criterion audit artifact required by C-28. Expected pass: C-01–C-27. Expected fail: C-28, C-29. Score under v9: 19/21 aspirational.

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

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section — the structural separation from CONFIDENCE exists to make omissions visible, not to create a section that can be filled with vague language. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE. Do not include break-even observations here — break-even was resolved in PRE-FLIGHT GATE.

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

First: look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis (tier and timeline) before analysis opened. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from analysis sections bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant recommendation.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds in light of the amendment. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — C-26 + C-27 + 29-criterion self-check with exact disqualifying forms for C-26/C-27 only

**Variation axes**: All V-03 mechanisms + step-labeled structure + 29-criterion self-check (extending R8 V-05's 27-criterion list to cover C-28 and C-29) with exact structural disqualifying forms for C-26 and C-27. Structural criteria C-18 through C-25 carry pass conditions only. C-28 and C-29 carry definition-level descriptions without exact disqualifying forms.

**Hypothesis**: Adding a complete per-criterion self-check trace covering all 29 aspirational criteria satisfies C-28 — it is a collective audit artifact distinct from the section-level FAILURE MODE blocks in STEP 6 and STEP 7. C-29 is the discriminating gap: exact disqualifying forms appear only for C-26 and C-27 (the most recently formalized criteria), not for C-18 through C-25 or C-28/C-29. This is the natural incremental pattern — each round extends precision to its newest criteria. Expected pass: C-01–C-28. Expected fail: C-29 (C-18–C-25 lack uniform structural precision). Score under v9: 20/21 aspirational.

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
- Scope exclusions: STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY TIER AND DRIVER, and STEP 7 SYNTHESIS each carry an explicit prohibition against scope content.
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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines are required on separate lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1–6 bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present. When AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this section — update it or explicitly reaffirm that it still holds. This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 29 CRITERIA**

This block is a per-criterion audit artifact. It is distinct from the FAILURE MODE blocks in STEP 6 and STEP 7 — those are section-level structural elements; this is a collective output-level verification protocol. For each criterion below, record Status (PASS / FAIL) and Evidence (the specific output location or content that satisfies or violates the criterion).

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form. Evidence: ___
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date. Evidence: ___
- [ ] C-03: Surface area table has a Total row with a specific number. Evidence: ___
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive. Evidence: ___
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence. Evidence: ___
- [ ] C-06: Team signal names specialist disciplines (not headcount only). Evidence: ___
- [ ] C-07: Primary driver accompanies the complexity tier. Evidence: ___
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default. Evidence: ___
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named — must appear in PRE-FLIGHT GATE (canonical location). Evidence: ___
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]". Evidence: ___
- [ ] C-11: Each named specialization includes an implementation ownership area. Evidence: ___
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated. Evidence: ___
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion. Evidence: ___
- [ ] C-14: Open unknowns appear in STEP 6 OPEN UNKNOWNS with Unknown: / Impact: / Movement: typed fields; STEP 5 explicitly closed. Evidence: ___
- [ ] C-15: Preliminary hypothesis (tier + timeline range) is a field INSIDE PRE-FLIGHT GATE; synthesis explicitly confirms or revises it. Evidence: ___
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default. Evidence: ___
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided. Evidence: ___
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields with specific responses; includes stop instruction. Evidence: ___
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5) and at least one adjacent to the scope exclusion canonical home (STEP 2 or STEP 3) carry an explicit prohibition rule. Evidence: ___
- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) carries an explicit prohibition. Every plausible recipient section for unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition. Evidence: ___
- [ ] C-21: Preliminary hypothesis is a field inside PRE-FLIGHT GATE — not in a standalone section after the gate. Synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises it. Evidence: ___
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both the anchor instruction AND the verdict close. Evidence: ___
- [ ] C-23: For at least one canonical field type, prohibition guards in adjacent sections name the canonical home by label — "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" not "do not include scope exclusions here." Evidence: ___
- [ ] C-24: Synthesis includes a Commitment chain block with three labeled lines (Gate commitment: / Analysis: / Verdict:) on separate lines. Evidence: ___
- [ ] C-25: PRE-FLIGHT GATE (after STOP) names at least two downstream sections responsible for scope exclusions AND names the section responsible for hypothesis confirmation or revision. Evidence: ___
- [ ] C-26: Synthesis contains a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE that applies independent of whether AMEND is present. The passing form states the requirement "applies on every invocation, independent of whether an AMEND directive is present" and frames non-compliance as "a structural failure of this section's integrity." Disqualifying form: "**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully...Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16" fails C-26 — "in this invocation" makes it conditional; "it fails C-16" makes it criterion-referenced rather than a structural property. Both disqualifiers must be absent for C-26 to pass. Evidence: ___
- [ ] C-27: Both STEP 6 OPEN UNKNOWNS and STEP 7 SYNTHESIS carry a dedicated labeled FAILURE MODE block (`> **FAILURE MODE FOR THIS SECTION**:`). Disqualifying form: a blockquote reading `> **Anti-pattern**: Restating sections in sequence is juxtaposition` in SYNTHESIS fails C-27 even if C-17 passes — it is embedded in the section's instruction prose, not a standalone labeled block whose absence creates a visible structural gap. An inline sentence "A generic placeholder fails" at the end of OPEN UNKNOWNS's requirements list also fails C-27. Evidence: ___
- [ ] C-28: This output includes a SELF-CHECK block that is distinct from the FAILURE MODE blocks in STEP 6 and STEP 7. The block covers all 29 aspirational criteria by ID with Status (PASS/FAIL) and Evidence per criterion. Evidence: ___
- [ ] C-29: Self-check items for all structural criteria (C-18 through C-27) include both a pass condition and an exact structural disqualifying form. Evidence: ___

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full integration: 29-criterion self-check with uniform structural precision across C-18–C-27

**Variation axes**: All V-04 axes + exact structural disqualifying forms extended uniformly to ALL structural criteria C-18 through C-27. C-18 through C-21 gain exact disqualifying forms (pass conditions only in V-04). C-22 through C-27 retain their exact disqualifying forms from prior rounds. C-28 and C-29 gain exact disqualifying forms.

**Hypothesis**: V-04 adds a complete 29-criterion self-check with exact disqualifying forms for C-26/C-27 only — the natural incremental approach. V-05 extends structural precision uniformly: every structural criterion C-18 through C-27 carries both a pass condition and an exact disqualifying form. C-28 and C-29 also receive exact disqualifying forms, making the self-check uniformly precise across all structural criteria regardless of when they were added to the rubric. The discriminator from V-04 is coverage uniformity: V-04 has precision for the latest criteria; V-05 has it for all. Expected pass: C-01–C-29. Score under v9: 21/21 — the R9 gold standard.

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
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA (prohibits scope exclusions), STEP 3 COMPLEXITY TIER AND DRIVER (prohibits scope exclusions), and STEP 7 SYNTHESIS (prohibits scope exclusions) — each section is explicitly closed against scope content.
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

First: look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate lines. A single sentence that mentions the tier, the analysis, and the verdict is juxtaposition-in-miniature — the chain must be scannable at a glance.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1–6 bearing on the commitment — name at least two signal dimensions]
Verdict: [use exactly one of the following forms — the phrase "committed in PRE-FLIGHT GATE" is required in the verdict line]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior value] to [current value] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

The verdict close must name PRE-FLIGHT GATE by label — not "my earlier estimate" and not "the preliminary hypothesis" without naming its structural site.

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

**SELF-CHECK — ALL 29 CRITERIA**

This block is a per-criterion audit artifact — distinct from the FAILURE MODE blocks in STEP 6 and STEP 7. Those blocks are section-level structural elements. This block is a collective output-level verification protocol. For each criterion below, record Status (PASS / FAIL) and Evidence (the specific output location or content that satisfies or violates the criterion). Fix any FAIL before writing the artifact.

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form. Evidence: ___
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date. Evidence: ___
- [ ] C-03: Surface area table has a Total row with a specific number. Evidence: ___
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive. Evidence: ___
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence. Evidence: ___
- [ ] C-06: Team signal names specialist disciplines (not headcount only). Evidence: ___
- [ ] C-07: Primary driver accompanies the complexity tier. Evidence: ___
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default. Evidence: ___
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named — must appear in PRE-FLIGHT GATE (canonical location). Evidence: ___
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]". Evidence: ___
- [ ] C-11: Each named specialization includes an implementation ownership area. Evidence: ___
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated. Evidence: ___
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion; fails if derivable from any single field alone. Evidence: ___
- [ ] C-14: Open unknowns appear in STEP 6 OPEN UNKNOWNS with Unknown: / Impact: / Movement: typed fields; STEP 5 explicitly closed against unknowns. Evidence: ___
- [ ] C-15: Preliminary hypothesis (tier + timeline range) is a field INSIDE PRE-FLIGHT GATE — not in a standalone section after the gate. Synthesis explicitly confirms or revises it, naming the changed dimension. Evidence: ___
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default. Evidence: ___
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided. Evidence: ___
- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary hypothesis fields with specific responses; includes stop instruction. Disqualifying form: a PRE-FLIGHT GATE that contains all three field types but omits the stop instruction ("Do not proceed until all three fields are resolved") fails C-18 — the stop instruction is the structural gate element, not just a heading. A gate that elides break-even (present but positioned elsewhere, e.g., inside INERTIA CHECK) also fails C-18 — all three fields must be inside the gate block. Evidence: ___
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5) and at least one adjacent to the scope exclusion canonical home (STEP 2 or STEP 3) carry an explicit prohibition rule. Disqualifying form: a section that is simply silent about which content types it does not accept fails C-19 even if the model places content correctly — the prohibition must be written explicitly in the section, not inferred from correct behavior. A prohibition limited to one adjacent section (e.g., only STEP 5 closed against unknowns, STEP 3 unclosed) also fails C-19. Evidence: ___
- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7) carries an explicit prohibition. Every plausible recipient section for unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition. Disqualifying form: STEP 7 SYNTHESIS carrying prohibitions against both scope exclusions and unknowns satisfies its own closure but fails C-20 if STEP 1 INERTIA CHECK carries no prohibition against scope qualifications — any single unguarded plausible recipient section fails C-20. Evidence: ___
- [ ] C-21: Preliminary hypothesis is a field inside PRE-FLIGHT GATE — not in a standalone section adjacent to or after the gate. Synthesis references "PRE-FLIGHT GATE" by name and explicitly confirms or revises the commitment. Disqualifying form: a prompt with PRE-FLIGHT GATE (C-18 PASS) and a standalone PRELIMINARY HYPOTHESIS section placed directly after the gate (C-15 PASS independently) fails C-21 if the hypothesis is not a field inside the gate block — "adjacent but outside" is structurally distinct from "inside." Evidence: ___
- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both ends: (1) anchor instruction ("look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there") AND (2) verdict close ("The preliminary hypothesis committed in PRE-FLIGHT GATE..."). Disqualifying form: "My earlier estimate was confirmed" fails C-22 — it refers to the hypothesis by implication without naming its structural home. "The preliminary hypothesis is confirmed" also fails — it names the commitment type but not the structural location. Only "The preliminary hypothesis committed in PRE-FLIGHT GATE" satisfies C-22. Evidence: ___
- [ ] C-23: For at least one canonical field type, prohibition guards in adjacent sections name the canonical home by label. Disqualifying form: "Do not include scope exclusions here" fails C-23 — it closes a door without naming the room. Only "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" (or equivalent that names the canonical home by section label) satisfies C-23. Evidence: ___
- [ ] C-24: Synthesis includes a Commitment chain block with three labeled lines on separate lines: Gate commitment: / Analysis: / Verdict:. Disqualifying form: a single sentence reading "The preliminary hypothesis committed in PRE-FLIGHT GATE (HIGH, 4–6 sprints) is confirmed: surface area is LOW and inertia cost is HIGH" fails C-24 even if it satisfies C-22 — the three chain steps are embedded in one sentence, making them unscannable without re-reading. The three steps must appear on separate labeled lines. Evidence: ___
- [ ] C-25: PRE-FLIGHT GATE (after STOP) includes an enforcement contract that names at least two downstream sections responsible for scope exclusions AND names the section responsible for hypothesis confirmation or revision. Disqualifying form: "All three fields above are preconditions for STEP 1 through STEP 7" fails C-25 — this is a continuation instruction, not an enforcement contract that distinguishes which sections hold the scope prohibition from which section confirms or revises the hypothesis. Evidence: ___
- [ ] C-26: Synthesis contains a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE stating the requirement applies on every invocation "independent of whether an AMEND directive is present" and framing non-compliance as "a structural failure of this section's integrity." Disqualifying form: "**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully...Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16" fails C-26 — "in this invocation" makes it conditional; "it fails C-16" makes it criterion-referenced rather than a structural property. Both disqualifiers must be absent. Evidence: ___
- [ ] C-27: Both STEP 6 OPEN UNKNOWNS and STEP 7 SYNTHESIS carry a dedicated labeled FAILURE MODE block (`> **FAILURE MODE FOR THIS SECTION**:`) as a structurally separate element. Disqualifying form: a blockquote reading `> **Anti-pattern**: Restating sections in sequence is juxtaposition` in SYNTHESIS fails C-27 even if C-17 passes — it is an anti-pattern annotation embedded in the section's instruction prose, not a standalone labeled block whose absence creates a visible structural gap. An inline sentence "A generic placeholder fails" at the end of OPEN UNKNOWNS's requirements list also fails for the same reason. Evidence: ___
- [ ] C-28: This output includes a SELF-CHECK block that is distinct from the FAILURE MODE blocks in STEP 6 and STEP 7. The block covers all 29 aspirational criteria by ID with Status (PASS/FAIL) and Evidence per criterion. Disqualifying form: the FAILURE MODE blocks in STEP 6 and STEP 7 satisfy C-27 but do not satisfy C-28 — they are section-level structural elements bound to specific sections; the SELF-CHECK is a post-output collective audit artifact covering all criteria simultaneously. A self-check that covers only a subset of aspirational criteria (e.g., C-09 through C-27 but not C-28 and C-29) fails C-28 even if it is structurally distinct. Evidence: ___
- [ ] C-29: Self-check items for all structural criteria (C-18 through C-27 minimum) include both a pass condition and an exact structural disqualifying form — a specific structural pattern that looks like compliance but fails. Disqualifying form: a self-check that includes exact disqualifying forms for C-26 and C-27 (the R7 criteria) but states only pass conditions for C-18 through C-25 (the R3–R6 criteria) fails C-29 — coverage must be uniform across all structural criteria regardless of which round introduced them. A self-check that achieves uniform coverage for C-18–C-27 but states only a definition-level description for C-28 and C-29 (the current-round criteria) also fails C-29 — the newest criteria must receive the same treatment as all others. Evidence: ___

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | C-26 | C-27 | C-28 | C-29 | Expected v9 score |
|----|------|------|------|------|-------------------|
| V-01 | **PASS** — structural directive, unconditional scope, structural framing | **FAIL** (intentional) — inline `> **Anti-pattern**:` in SYNTHESIS, inline "fails" trailing sentence in OPEN UNKNOWNS | **FAIL** — no self-check block | **FAIL** — no self-check block | 16/21 (97.62) |
| V-02 | **FAIL** (intentional) — no AMEND directive of any kind | **PASS** — dedicated `> **FAILURE MODE FOR THIS SECTION**:` standalone blocks in both STEP 6 and SYNTHESIS | **FAIL** — no self-check block | **FAIL** — no self-check block | 16/21 (97.62) |
| V-03 | **PASS** | **PASS** | **FAIL** — FAILURE MODE blocks satisfy C-27; no collective per-criterion audit artifact exists | **FAIL** — no self-check block | 19/21 (99.05) |
| V-04 | **PASS** | **PASS** | **PASS** — 29-criterion self-check with Status+Evidence per criterion, distinct from FAILURE MODE blocks | **FAIL** — C-18–C-25 have pass conditions only; C-26/C-27 have exact disqualifying forms; C-28/C-29 are definition-level without disqualifying forms | 20/21 (99.52) |
| V-05 | **PASS** | **PASS** | **PASS** | **PASS** — exact disqualifying forms for all C-18–C-27 uniformly + exact disqualifying forms for C-28 and C-29 | **21/21 (100.00)** |

**Key design differences from R8:**

- **C-28 mechanism**: R8 V-04/V-05 have a 27-criterion checklist that satisfies C-28 when the model fills each item with a pass/fail verdict and evidence. R9 V-04/V-05 make the Status+Evidence requirement explicit in the self-check preamble ("For each criterion below, record Status (PASS / FAIL) and Evidence"), ensuring the per-criterion audit trace is an explicit structural output requirement rather than an implicit expectation of checklist formatting.

- **C-29 discriminator — V-04 vs V-05**: V-04's self-check items for C-18–C-25 state only pass conditions (what the output must contain). V-05 extends each structural criterion item with an exact disqualifying form — the specific structural pattern that looks like compliance but fails. The disqualifying forms for C-18–C-21 are new in V-05; the disqualifying forms for C-22–C-27 carry over from R8 V-05. Uniformity across all structural criteria, regardless of the round that introduced them, is the V-05 discriminator.

- **C-28/C-29 self-check items**: V-04 includes C-28 and C-29 as definition-level items (what they require) without exact disqualifying forms. V-05 adds exact disqualifying forms for C-28 ("FAILURE MODE blocks satisfy C-27 but not C-28") and C-29 ("exact forms for latest-round criteria only fails C-29 — coverage must be uniform") — closing the self-check items against the most natural failure modes for the newest criteria.

- **Self-check evolution**: R8 V-05 had a 27-criterion checklist with exact disqualifying forms for C-22–C-27 (six of ten structural criteria). R9 V-04 extends to 29 criteria with exact disqualifying forms for C-26/C-27 (latest-round criteria only). R9 V-05 achieves full uniform coverage: every structural criterion C-18–C-27 plus C-28 and C-29 carry both pass conditions and exact disqualifying forms, completing the structural precision that C-29 requires.
