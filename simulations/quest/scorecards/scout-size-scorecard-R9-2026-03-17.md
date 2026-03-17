Now I have everything. Let me produce the full scorecard.

---

# Quest Scorecard — scout-size R9 × v9 Rubric

**Date**: 2026-03-17 | **Skill**: scout-size | **Rubric**: v9 (29 criteria: 5 essential, 3 recommended, 21 aspirational) | **Denominator**: aspirational / 21

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 21 * 10)
```

---

## Per-Variation Criterion Evaluation

### Essential Criteria (C-01–C-05) — All Variations

All 5 variations are built on the same structural backbone and pass all essential criteria uniformly.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-01** Complexity tier | PASS | PASS | PASS | PASS | PASS | All templates require `Tier: [LOW / MEDIUM / HIGH / XL]` with no alternative vocabulary |
| **C-02** Sprint range | PASS | PASS | PASS | PASS | PASS | `Timeline signal: [sprint range — "N–M sprints"]`; V-04/V-05 add explicit failing form `"4 sprints" (point estimate)` |
| **C-03** Surface area table + Total row | PASS | PASS | PASS | PASS | PASS | All include the `| **Total** | | | **N integration points** |` required row |
| **C-04** Inertia check + cost direction | PASS | PASS | PASS | PASS | PASS | All include `Workaround / Maintenance cost / Cost direction: [cheaper / comparable / more expensive]` |
| **C-05** Confidence with basis | PASS | PASS | PASS | PASS | PASS | All include `Confidence: [HIGH / MEDIUM / LOW]` + `Basis: [what IS known]` |

**Essential subtotal: 5/5 all variations → 60 pts**

---

### Recommended Criteria (C-06–C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-06** Specialization names | PASS | PASS | PASS | PASS | PASS | All templates include `Failing: "2 engineers" — no disciplines... Passing: "1 backend engineer (owns...)"` inline example mandating role names |
| **C-07** Complexity driver | PASS | PASS | PASS | PASS | PASS | All include `Primary driver: [one or two factors most responsible]` as required field; V-04/V-05 add table of failing sensitivity forms |
| **C-08** AMEND modifies output | PASS | PASS | PASS | PASS | PASS | Default pass — no AMEND directive invoked in any template; structural AMEND directive in V-01/V-03/V-04/V-05 makes cascade behavioral |

**Recommended subtotal: 3/3 all variations → 30 pts**

---

### Aspirational Criteria (C-09–C-29) — Per Variation

#### Block 1: C-09 – C-17 (Depth/Behavior) — All Variations Pass

| Criterion | All 5 | Evidence |
|-----------|-------|----------|
| **C-09** Scope exclusions named | PASS | PRE-FLIGHT GATE mandates `Out-of-scope boundary: [Name at least one...]; "TBD" or blank fails` |
| **C-10** Break-even signal | PASS | PRE-FLIGHT GATE mandates `Break-even signal: [...]; absence fails` in all 5; V-04/V-05 add explicit failing form `"Absence fails C-10"` |
| **C-11** Specialization ownership | PASS | Team signal field explicitly requires `implementation ownership per role` with failing/passing inline exemplars in all 5 |
| **C-12** Confidence names unknowns | PASS | OPEN UNKNOWNS section with typed fields (Unknown/Impact/Movement) exists in all 5; CONFIDENCE is closed against unknowns |
| **C-13** Cross-signal synthesis | PASS | All templates require commitment-chain Verdict using exactly one of three forms that mandates cross-signal cross-reference; "cross-signal directional observation" required after verdict |
| **C-14** Unknowns in dedicated section | PASS | All 5 have OPEN UNKNOWNS section (or STEP 6) with typed fields; CONFIDENCE section carries prohibition `"Do not list unknowns here"` |
| **C-15** Hypothesis confirmed/revised | PASS | PRE-FLIGHT GATE includes `Preliminary hypothesis: Tier / Timeline / Reasoning`; SYNTHESIS mandates confirmation/revision verdict with three labeled lines |
| **C-16** AMEND cascades to synthesis | PASS | Default pass — no AMEND invoked; V-01/V-03/V-04/V-05 structural directive makes this a structural property, not just default |
| **C-17** At least one section names failure mode | PASS | V-01: `> **Anti-pattern**: Restating sections in sequence...` in SYNTHESIS names the anti-pattern; V-02–V-05 have dedicated FAILURE MODE blocks which exceed the C-17 minimum |

#### Block 2: C-18 – C-25 (Structure) — All Variations Pass

| Criterion | All 5 | Evidence |
|-----------|-------|----------|
| **C-18** Pre-analysis gate | PASS | PRE-FLIGHT GATE precedes all analysis sections with STOP instruction; contains all 3 required fields |
| **C-19** Prohibition guards (minimum one) | PASS | All 5: INERTIA CHECK, SURFACE AREA, COMPLEXITY, CONFIDENCE each carry `"Do not [X] here"` prohibitions |
| **C-20** Bilateral closure mesh | PASS | All 5: scope exclusions closed in INERTIA CHECK, SURFACE AREA, COMPLEXITY, SYNTHESIS; unknowns closed in COMPLEXITY, CONFIDENCE, SYNTHESIS, OPEN UNKNOWNS (bidirectional) |
| **C-21** Gate elicits hypothesis | PASS | `Preliminary hypothesis: Tier / Timeline / Reasoning` is inside PRE-FLIGHT GATE; SYNTHESIS explicitly confirms/revises naming the gate |
| **C-22** Synthesis names gate at both ends | PASS | SYNTHESIS opens with `"look back at PRE-FLIGHT GATE"` and Verdict form requires `"committed in PRE-FLIGHT GATE"` phrase |
| **C-23** Guards name canonical home | PASS | INERTIA CHECK reads `"scope was resolved in PRE-FLIGHT GATE, not in analysis steps"` — canonical home named, not just bare exclusion |
| **C-24** Structured commitment-chain trace | PASS | SYNTHESIS has three labeled lines: `Gate commitment: / Analysis: / Verdict:` on separate lines in all 5 |
| **C-25** Gate forward-references enforcement sections | PASS | PRE-FLIGHT GATE (after STOP) reads: `"Scope exclusions: held in INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS... Hypothesis: confirmed or revised in SYNTHESIS"` in all 5 |

#### Block 3: C-26 – C-29 (New R8/R9 Criteria) — Variation-Discriminating

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-26** Structural AMEND directive in SYNTHESIS | PASS | **FAIL** | PASS | PASS | PASS |
| **C-27** Dedicated FAILURE MODE blocks in every aspirational section | **FAIL** | PASS | PASS | PASS | PASS |
| **C-28** Per-criterion self-check trace covering all 29 criteria | **FAIL** | **FAIL** | **FAIL** | PASS | PASS |
| **C-29** Self-check items for all structural criteria include exact disqualifying forms (C-18–C-27 uniform) | **FAIL** | **FAIL** | **FAIL** | **FAIL** | PASS |

**C-26 evidence per variation:**
- **V-01 PASS**: SYNTHESIS contains `**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**... applies on every invocation, independent of whether an AMEND directive is present... structural failure of this section's integrity` — the full structural mandate form.
- **V-02 FAIL**: SYNTHESIS carries `> **FAILURE MODE FOR THIS SECTION**:` block (C-27 mechanism) but contains no STRUCTURAL AMEND RE-EVALUATION DIRECTIVE whatsoever. Passes C-17 through the FAILURE MODE block; does not pass C-26.
- **V-03/V-04/V-05 PASS**: Identical to V-01 for this criterion — structural directive present in SYNTHESIS with the required `"every invocation"` and `"structural property"` language.

**C-27 evidence per variation:**
- **V-01 FAIL**: SYNTHESIS carries `> **Anti-pattern**: Restating sections in sequence...` — an inline blockquote embedded in section instruction prose, not a standalone labeled `> **FAILURE MODE FOR THIS SECTION**:` block. OPEN UNKNOWNS carries only `"A generic placeholder like 'dependencies may exist' fails"` — an inline closing sentence. Neither is a dedicated labeled block; omission of either would not create a visible structural gap. C-17 PASSES (anti-pattern is named), but C-27 requires the dedicated block form.
- **V-02 PASS**: SYNTHESIS carries `> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence...` as a standalone block. OPEN UNKNOWNS carries `> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder...` as a standalone block. Both are labeled, both are standalone — a reader cannot scan past their absence without noticing the gap.
- **V-03/V-04/V-05 PASS**: Identical FAILURE MODE block structure to V-02 — both sections carry dedicated labeled blocks.

**C-28 evidence per variation:**
- **V-01/V-02/V-03 FAIL**: No SELF-CHECK block exists in any of the three. The section-level FAILURE MODE blocks (V-02/V-03) and the structural AMEND directive (V-01/V-03) are content-section mechanisms, not a collective per-criterion audit artifact. A reader cannot verify criterion-by-criterion compliance without re-reading the full output.
- **V-04/V-05 PASS**: `**SELF-CHECK — ALL 29 CRITERIA**` block is explicitly present as a distinct output-level verification layer after all STEP sections. It covers every criterion C-01 through C-29 with `Status (PASS/FAIL)` and `Evidence` per criterion. The block's preamble explicitly distinguishes it from section-level FAILURE MODE blocks: `"This block is a per-criterion audit artifact... distinct from the FAILURE MODE blocks in STEP 6 and STEP 7."`

**C-29 evidence per variation:**
- **V-01/V-02/V-03 FAIL**: No self-check exists; C-29 is vacuously inapplicable.
- **V-04 FAIL**: Self-check is present (C-28 PASS). C-26 item carries exact disqualifying form: `"Both disqualifiers must be absent for C-26 to pass"` with `"in this invocation" makes it conditional... fails C-26` specified. C-27 item carries `"a blockquote reading > **Anti-pattern**: Restating sections in sequence is juxtaposition in SYNTHESIS fails C-27 even if C-17 passes"`. But C-18 through C-25 items carry only pass conditions — no exact structural disqualifying form for any of them. The natural incremental pattern: only the round's newest criteria get structural precision.
- **V-05 PASS**: Self-check extends exact disqualifying forms uniformly to ALL structural criteria C-18 through C-27. C-18 item includes a disqualifying form (e.g., inline reminder in a section vs. a pre-write gate that fires before analysis). C-19–C-25 each carry equivalent structural disqualifying forms. C-28/C-29 also receive exact disqualifying forms. Coverage uniformity regardless of which round introduced the criterion is the discriminator.

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| **V-01** | 5/5 (60) | 3/3 (30) | 18/21 (8.57) | **98.57** | Gold |
| **V-02** | 5/5 (60) | 3/3 (30) | 18/21 (8.57) | **98.57** | Gold |
| **V-03** | 5/5 (60) | 3/3 (30) | 19/21 (9.05) | **99.05** | Gold |
| **V-04** | 5/5 (60) | 3/3 (30) | 20/21 (9.52) | **99.52** | Gold |
| **V-05** | 5/5 (60) | 3/3 (30) | 21/21 (10.00) | **100.00** | Gold |

**All essential pass: YES (all 5 variations)**

> **Score table discrepancy note**: The v9 rubric's expected-scores table lists V-01 and V-02 at 97.62 (= 16/21 aspirational, implying 5 aspiration fails each). My criterion-by-criterion evaluation finds V-01 fails C-27/C-28/C-29 (3 fails → 18/21) and V-02 fails C-26/C-28/C-29 (3 fails → 18/21), yielding 98.57 for both. I cannot identify 2 additional failing criteria in either template consistent with the rubric's stated discriminating axes. V-03/V-04/V-05 scores match exactly. I'm reporting my computed values; the discrepancy should be investigated if these variations are re-run against actual model outputs.

---

## Variation Ranking

1. **V-05** — 100.00 — 21/21 aspirational. Only variation to achieve uniform structural disqualifying-form coverage across all structural criteria.
2. **V-04** — 99.52 — 20/21. Adds complete self-check (C-28 PASS); exact disqualifying forms limited to C-26/C-27 only (C-29 FAIL).
3. **V-03** — 99.05 — 19/21. Both FAILURE MODE blocks (C-27) and AMEND directive (C-26) present; no self-check machinery at all.
4. **V-01 / V-02** — 98.57 (tied) — 18/21. Single-axis tests: V-01 has C-26 without C-27; V-02 has C-27 without C-26. Both lack self-check.

---

## Excellence Signals from V-05

Three patterns from V-05 that distinguish it above V-04:

**Pattern 1 — Uniform structural disqualifying-form coverage**
V-04 achieves exact disqualifying forms for C-26 and C-27 (the most recently added criteria) but leaves C-18 through C-25 with pass conditions only. V-05 extends the same precision retroactively to every structural criterion regardless of which round introduced it. The key insight: each round's new criteria naturally receive attention; older criteria regress to pass-only descriptions as the denominator grows. V-05's self-check resists this regression explicitly.

**Pattern 2 — Self-referential structural precision in C-28 and C-29 self-check items**
V-04 achieves C-28 (self-check exists) but C-28 and C-29 in the self-check itself carry only definition-level descriptions. V-05 applies exact disqualifying forms to C-28 and C-29 within the self-check — the self-check audits the self-check's own structural requirements. This closes the final asymmetry: C-28/C-29 are structural criteria and receive the same treatment as C-18–C-27.

**Pattern 3 — Step-labeled structure as INERTIA CHECK precision anchor**
V-04/V-05 rename sections to `STEP N:` labels and add failing-form tables to INERTIA CHECK and COMPLEXITY TIER. This is not discriminating for C-26–C-29 specifically, but it makes the criterion-boundary for C-04 and C-07 structurally visible in the same way FAILURE MODE blocks make C-13/C-14 visible — the "what the wrong answer looks like" form is embedded as a structural element, not buried in prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Uniform structural disqualifying-form coverage extended retroactively to all structural criteria C-18–C-27, not just latest-round additions — prevents regression to pass-only descriptions as denominator grows", "Self-referential structural precision: C-28 and C-29 self-check items carry exact disqualifying forms for the self-check mechanism itself, closing the asymmetry where the audit artifact audits content but not itself"]}
```
