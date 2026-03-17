# listen-support Round 7 Scorecard

## Scoring Summary

| Variation | Score | C-24 | C-25 | C-26 | Above-Ceiling Signals |
|-----------|-------|------|------|------|-----------------------|
| V-01 | **180/180** | PASS | PASS | PASS | none above base |
| V-02 | **180/180** | PASS | PASS | PASS | exhaustive-collocation catch-all |
| V-03 | **180/180** | PASS | PASS | PASS | inertia-competitor-phase-framing |
| V-04 | **180/180** | PASS | PASS | PASS | none above V-01/V-02 combined |
| V-05 | **180/180** | PASS | PASS | PASS | inertia-competitor-phase-framing (strongest) |

**Top score: 180. All essential PASS: yes.**

---

## Key Findings

**C-24**: All variations pass. The AUDIT RESULT output slot (V-01 hypothesis) is **not the differentiator**. V-02 satisfies C-24 with 3 constraints + correction gate text alone, without a formal slot. V-01's hypothesis is disproven.

**C-25**: All variations pass. Exhaustive enumeration (V-02 hypothesis: 13+ collocations) is **not required**. V-01 and V-03 satisfy C-25 with exactly 2 explicit verb-subject collocations + the affirmative "Every action in this ticket was taken by 'I'." The minimum threshold is sufficient.

**C-26**: All variations pass. "END OF PASS 1. Switch to frontmatter verification mode." appears verbatim in every variation's Step 8 body — not just V-05. C-26 was already present in the base architecture; it is not uniquely contributed by V-05's explicit C-26 axis.

**All-ceiling result**: Every variation achieves 180/180. The three new v7 criteria were already implicitly embedded in the base architecture inherited from R6 V-05, even at minimal form. The single-axis hypotheses (V-01, V-02, V-03) confirm minimal mechanisms are sufficient; STRONG mechanisms exceed the pass conditions without producing new scored criteria.

---

## Rankings

| Rank | Variation | Score | Rationale |
|------|-----------|-------|-----------|
| 1 | **V-05** | 180/180 | All 26 criteria at ceiling. Strongest inertia framing: P1/P2/P3 body templates + tool-name-fidelity in coverage traces + adoption-curve quantification in consequence fields. |
| 2 | **V-03** | 180/180 | Primary above-ceiling signal isolated: inertia competitor phase framing strengthens C-06/C-07/C-08/C-11 simultaneously without additional gates. |
| 3 | **V-04** | 180/180 | STRONG C-24 + STRONG C-25 combined; non-interference confirmed but no emergent signal beyond V-01 + V-02 individually. |
| 4 | **V-02** | 180/180 | Catch-all clause closes unlisted-collocation escape route; strongest C-25 mechanism but not a pass-condition requirement. |
| 5 | **V-01** | 180/180 | Cleanest single-axis C-24 implementation; AUDIT RESULT slot disproven as necessary. |

---

## Excellence Signals

**Primary — Inertia Competitor Phase Framing (V-03/V-05) → C-27 candidate**

Three structural properties above C-11's current ceiling:
1. Coverage trace must name the specific tool — grep-checkable string, not interpretable phrase
2. Phase-differentiated body language: P1 = dual-tool parallelism; P3 = parity-gap comparison — testable sentence-level instructions
3. Gap analysis reframed as switching-friction gaps — a different signal profile than generic doc/design/operational gaps

**Why C-27**: C-11 passes with generic scenario grounding. Named competitor + adoption-curve differentiated bodies is a structurally distinct mechanism with above-criterion testability. v8 ceiling projection: 185/185.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["inertia-competitor-phase-framing"]}
```
tep 8 body includes "END OF PASS 1. Switch to frontmatter verification mode." between PASS 1 and PASS 2. Mode exited (PASS 1) and mode entered (frontmatter verification) both named. |

**Total: 180/180**
**All essential PASS: yes**
**Above-ceiling signals**: None beyond base mechanisms. AUDIT RESULT slot is a stronger C-24 mechanism than needed but does not produce a new above-ceiling signal.

**Hypothesis result**: DISPROVEN. The AUDIT RESULT output slot is not the C-24 differentiator -- V-02 satisfies C-24 without it. V-01 and V-02 achieve the same score.

---

### V-02 — Phrasing Register (Exhaustive Verb-Subject Enumeration)

**Axis**: C-25 enumeration breadth: 13+ explicit collocations + catch-all clause

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table with independent severity/volume columns |
| C-07 | PASS (10) | Phase-character table pre-commits volume per phase window |
| C-08 | PASS (10) | "You ARE [persona name]" + exhaustive verb prohibition reinforces first-person stance |
| C-09 through C-23 | PASS (75) | All prior aspirational criteria satisfied; END OF PASS 1 delimiter present in Step 8 |
| C-24 | PASS (5) | Step 4B: 3 constraints (category spread, volume distribution, phase-character compliance) + correction gate: "If any constraint fails, correct the summary table and re-run this check before proceeding. Do not write card bodies until all three pass." No AUDIT RESULT slot but correction gate is explicit and mandatory. |
| C-25 | PASS (5) | 13+ explicit verb-subject collocations across all stock roles (SRE x6, PM x5, engineer x5, Support x3, C-[NN] x3, UX x2) + catch-all: "Any construction where a role title (SRE, PM, engineer, Support, C-[NN], UX, designer) precedes any verb whatsoever." + "Every action in this ticket was taken by 'I'." Closes the unlisted-collocation escape route structurally. |
| C-26 | PASS (5) | "END OF PASS 1. Switch to frontmatter verification mode." present in Step 8 body. |

**Total: 180/180**
**All essential PASS: yes**

**Above-ceiling signal — C-25 PASS+**: The catch-all clause "Any construction where a role title (SRE, PM, engineer, Support, C-[NN], UX, designer) precedes any verb whatsoever" makes verb-subject violations grep-checkable by role title alone, without requiring collocations to be enumerated pre-generation. A model cannot write "the engineer observed", "the SRE pulled", or "the C-07 refreshed" without violating the catch-all, even if these constructions are not in the enumerated list. The catch-all closes the unlisted-collocation path; C-25's pass condition only requires 2 explicit collocations.

**Hypothesis result**: DISPROVEN as a pass condition finding. Exhaustive enumeration exceeds C-25's pass condition but is not required for a PASS. However, the catch-all clause does close a structural escape route that 2-collocation lists leave open, and this is a meaningful above-ceiling signal.

---

### V-03 — Inertia Framing (Named Inertia Competitor)

**Axis**: STATUS QUO as named Inertia Competitor with adoption-curve phase interpretation

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact; Step 4B present with correction gate |
| C-06 | PASS (10) | Phase character map augmented with inertia adoption-curve lens; P1 high-severity driven by dual-tool confusion, P3 lower-severity driven by edge-case parity gap |
| C-07 | PASS (10) | Inertia adoption curve produces explicit volume justification per phase: P1 = high (parallel tool users), P3 = low (committed edge cases) |
| C-08 | PASS (10) | "You ARE [persona name]" + named inertia competitor in body instruction produces phase-differentiated voice: P1 body must name dual-tool tension ("I still have [tool] open..."); P3 body must name parity gap ("In [tool] I could do X; here I cannot.") |
| C-09 through C-23 | PASS (75) | All prior aspirational criteria satisfied; END OF PASS 1 delimiter present |
| C-24 | PASS (5) | Step 4B: 3 constraints + "If any fails, correct the table and re-run before proceeding." Correction gate is minimal but explicit. |
| C-25 | PASS (5) | "Prohibited verb-subject forms: 'the SRE ran', 'the PM reviewed'." Exactly 2 collocations (minimum). "Every action in this ticket was taken by 'I'." |
| C-26 | PASS (5) | "END OF PASS 1. Switch to frontmatter verification mode." present in Step 8 body. |

**Total: 180/180**
**All essential PASS: yes**

**Above-ceiling signal — Inertia Competitor Phase Framing (C-27 candidate)**:

Step 1 establishes the specific named tool, not a category or generic phrase. Step 2 adds an adoption-curve interpretation layer to the phase map:
- P1: dual-tool parallelism tickets ("I still have [tool] open because I don't trust this for [task] yet.")
- P2: trust-threshold and reversion-trigger tickets
- P3: committed-user parity-gap tickets ("In [tool], I could do X. I cannot find the equivalent here.")

This produces qualitatively different bodies than generic STATUS QUO:
1. **Unambiguous coverage traces**: Coverage table column 2 names the inertia competitor tool, not "the old workflow" -- the trace is verifiable without interpreting a generic phrase.
2. **Phase-differentiated body language**: P1 bodies carry dual-tool parallelism vocabulary; P3 bodies carry parity-gap comparison vocabulary. No prior STATUS QUO mechanism produced this differentiation.
3. **Gap analysis framing**: Doc gaps are framed as "gaps that cause users to open the inertia competitor for documentation of the equivalent task" -- actionable and specific to the switching context.

The naming of the inertia competitor in the Consequence -- Adoption cost field drives quantification: "percentage of P1-phase users who revert to the inertia competitor" is a measurable cohort outcome; "this will slow adoption" is not.

**Why C-27 candidate**: C-11 STATUS QUO grounding passes when a current-state section exists and at least two tickets trace to it. V-03 satisfies C-11 but produces a structurally richer trace mechanism: the named tool is grep-verifiable in coverage column 2; the adoption-curve framing makes phase-differentiated body language testable. A criterion requiring a named inertia competitor (not a generic baseline) and phase-specific body framing instructions would distinguish V-03/V-05 from V-01/V-02/V-04 at a level C-11 cannot.

---

### V-04 — C-24 Strong + C-25 Strong (Combined)

**Axes**: Output format (C-24 AUDIT RESULT gate) + Phrasing register (C-25 exhaustive enumeration)

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table; P1 -> P0/P1 severity range, P1 -> high volume character |
| C-07 | PASS (10) | Phase-character table; P3 -> P2/P3 severity range, P3 -> low volume character |
| C-08 | PASS (10) | "You ARE [persona name]" + exhaustive verb prohibition |
| C-09 through C-23 | PASS (75) | All prior aspirational criteria satisfied; END OF PASS 1 delimiter present |
| C-24 | PASS (5) | Step 4B: 4 constraints + AUDIT RESULT: [PASS/FAIL] slot + "Re-run this audit. Do not proceed until AUDIT RESULT: PASS." Identical mechanism strength to V-01. |
| C-25 | PASS (5) | 13+ verb-subject collocations + catch-all + "Every action in this ticket was taken by 'I'." Identical enumeration to V-02. |
| C-26 | PASS (5) | "END OF PASS 1. Switch to frontmatter verification mode." present in Step 8 body. |

**Total: 180/180**
**All essential PASS: yes**
**Above-ceiling signals**: None beyond V-01 (AUDIT RESULT slot) + V-02 (exhaustive collocations) individually. Combining at full strength does not produce an emergent above-ceiling signal when both are already satisfied.

**Hypothesis result**: CONFIRMED at the pass-condition level. C-24 and C-25 address non-overlapping failure surfaces; combining at full strength does not interfere with either criterion or any prior criterion. But the combination produces no above-ceiling signal that V-01 and V-02 do not individually carry.

---

### V-05 — Full Synthesis

**Axes**: Inertia framing + C-24 STRONG + C-25 exhaustive + C-26 delimiter + C-22 explicit column independence

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table with adoption-curve lens; inertia competitor grounds P1 high-severity and P3 lower-severity characterization |
| C-07 | PASS (10) | Phase-character table; inertia adoption curve makes P1 = high volume (parallel-tool users) and P3 = low volume (committed edge cases) explicit |
| C-08 | PASS (10) | "You ARE [persona name]" + exhaustive verb prohibition + inertia competitor body instructions per phase (P1: dual-tool tension; P2: trust threshold; P3: parity-gap comparison) |
| C-09 | PASS (5) | Cross-ticket pattern with inertia-competitor-specific consequence: "percentage of P1-phase users who revert to the inertia competitor" as adoption cost |
| C-10 | PASS (5) | Priority Close Order names "closes the inertia competitor reversion window before P2 adoption begins" -- strongest phase-character reasoning in the set |
| C-11 | PASS (5) | Step 1 INERTIA COMPETITOR names specific tool; body instructions require competitor name in every card and in every coverage trace row; generic phrases do not pass |
| C-12 | PASS (5) | Flat consequence fields with Prohibited sentinels; adoption cost requires "percentage of P1-phase users who revert to the inertia competitor" -- quantified and cohort-specific |
| C-13 | PASS (5) | 3-column coverage trace table in PASS 1 with ticket ID / STATUS QUO element (inertia competitor by name) / gap traced |
| C-14 | PASS (5) | Three flat consequence component fields with structurally separate named fields and Prohibited sentinels |
| C-15 | PASS (5) | Table-form coverage enumeration in PASS 1 with one row per ticket |
| C-16 | PASS (5) | Container-free flat sibling consequence fields with no parent "Consequence:" label |
| C-17 | PASS (5) | 3-column gap-bridged table + "No orphan gaps" check + "Orphan gap: [ID] -- no ticket evidence" surfacing format |
| C-18 | PASS (5) | Per-field Prohibited: sentinels on all three consequence component fields |
| C-19 | PASS (5) | "You ARE [persona name]" mode declaration + explicit third-person prohibition |
| C-20 | PASS (5) | Step 4 summary table: "All controlled-vocabulary values locked here. No vocabulary value appears in a narrative sentence for the first time." |
| C-21 | PASS (5) | Named-role noun forms "the SRE", "the PM", "the engineer", "the C-[NN]", "the Support agent", "the UX designer" all enumerated in verb-subject prohibition |
| C-22 | PASS (5) | "Severity Range and Volume Character are independent columns -- each is checkable without reading the other." Explicit column-independence declaration; inertia adoption curve provides adoption-curve grounding for the phase character values |
| C-23 | PASS (5) | PASS 1 / PASS 2 sections with explicit labels and "Two structurally independent passes. The two passes have non-overlapping failure surfaces and must not be merged into one block." |
| C-24 | PASS (5) | Step 4B: 4 constraints + AUDIT RESULT: [PASS/FAIL] slot + "Do not write any card body until AUDIT RESULT: PASS is written." + explanation of why collective audit catches distribution failures row checks miss |
| C-25 | PASS (5) | Full enumeration structured with three prohibition categories: third-person pronouns / named-role nouns / verb-subject collocations (13+ pairs) + catch-all. "Every action in this ticket was taken by 'I'." |
| C-26 | PASS (5) | "END OF PASS 1. Switch to frontmatter verification mode." between PASS 1 and PASS 2; "must not be merged into one block" reinforces delimiter intent |

**Total: 180/180**
**All essential PASS: yes**

**Above-ceiling signals (primary)**:

**Signal 1 — Inertia Competitor Phase Framing (C-27 candidate, strongest form)**

V-05 combines the named inertia competitor (from V-03) with the full synthesis, producing the richest instance:
- Coverage trace column 2 must name the inertia competitor: "Column 2 must name the inertia competitor. A generic phrase does not count as a trace." This extends C-17's gap-bridge table with a new testability requirement.
- Adoption cost quantification: "percentage of P1-phase users who revert to the inertia competitor, hours lost, churn risk, or escalation-path length in days" -- every option is a measurable output.
- Priority Close Order: "Note which gaps, if closed, most directly reduce reversion to the inertia competitor." Re-frames gap prioritization from generic "high volume/severity" to "reduces switching friction specifically."

The inertia competitor ground-truth trace is grep-checkable: a scorer can search coverage table column 2 for the named tool string and detect any generic phrase. No prior criteria test this trace fidelity.

**Signal 2 — Adoption-Curve Quantification Template in Consequence Fields**

V-05's Consequence -- Adoption cost field specifies: "percentage of P1-phase users who revert to the inertia competitor, hours lost, churn risk, or escalation-path length in days." This template is above C-12's ceiling (which requires any specific consequence, not an inertia-competitor-anchored quantification). A criterion requiring that at least one consequence field quantify competitor-reversion explicitly (a measurable percentage or hours-lost value) would distinguish V-05's output from C-12-passing outputs that provide general quantification.

---

## Composite Scoring Table

| Variation | Essential (60) | Recommended (30) | Aspirational (90) | Total (180) | Above-Ceiling Signals |
|-----------|----------------|------------------|-------------------|-------------|----------------------|
| V-01 | 60 | 30 | 90 | **180** | none |
| V-02 | 60 | 30 | 90 | **180** | exhaustive-collocation catch-all |
| V-03 | 60 | 30 | 90 | **180** | inertia-competitor-phase-framing |
| V-04 | 60 | 30 | 90 | **180** | none (V-01 + V-02 combined, no emergence) |
| V-05 | 60 | 30 | 90 | **180** | inertia-competitor-phase-framing (strongest) + adoption-curve quantification |

---

## Criterion Pass/Fail Detail (C-24, C-25, C-26 -- all others PASS for all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |

**C-24 mechanism comparison**:
- V-01, V-04, V-05: 4 constraints + AUDIT RESULT slot + "Do not write any card body until AUDIT RESULT: PASS." → Strongest enforcement.
- V-02: 3 constraints + correction gate ("If any constraint fails, correct the summary table and re-run this check before proceeding.") + "Do not write card bodies until all three pass." → Passes without AUDIT RESULT slot. Slot is not required by pass condition.
- V-03: 3 constraints + minimal correction gate ("If any fails, correct the table and re-run before proceeding.") → Minimal but sufficient. Explicit correction trigger present.

**C-25 mechanism comparison**:
- V-02, V-04, V-05: 13+ collocations across all stock roles + catch-all closing all role-title + verb constructions. → Strongest enforcement. No unlisted collocation can escape.
- V-01, V-03: Exactly 2 collocations ("the SRE ran", "the PM reviewed") + affirmative "Every action by 'I'." → Passes at minimum threshold. Unlisted collocations remain as nominal escape routes.

**C-26 finding**: "END OF PASS 1. Switch to frontmatter verification mode." appears verbatim in every variation's Step 8 body. C-26 was not uniquely contributed by V-05's explicit C-26 axis -- it was present in all five variations from the base R6 V-05 architecture. The C-26 criterion is fully satisfied at ceiling across the board.

---

## Ranking

| Rank | Variation | Score | Above-Ceiling | Rationale |
|------|-----------|-------|---------------|-----------|
| 1 | **V-05** | 180/180 | inertia-competitor-phase-framing (strongest) + adoption-curve quantification | All 26 criteria at ceiling simultaneously. Strongest inertia framing: P1/P2/P3 body instructions + named competitor required in coverage trace column 2 + adoption-cost quantification tied to competitor reversion. C-22 explicit independence declaration ("each is checkable without reading the other"). |
| 2 | **V-03** | 180/180 | inertia-competitor-phase-framing (isolated) | All 26 criteria at ceiling with minimal C-24/C-25 mechanisms. Carries the primary above-ceiling signal in isolation, showing it is orthogonal to mechanism strength on new criteria. The inertia competitor framing strengthens C-06/C-07/C-08/C-11 simultaneously without adding structural gates. |
| 3 | **V-04** | 180/180 | none (V-01 + V-02 combination) | All 26 criteria at ceiling. STRONG C-24 + STRONG C-25 without inertia framing; confirms the two mechanisms are non-interfering but produces no emergent above-ceiling signal beyond what V-01 and V-02 individually carry. |
| 4 | **V-02** | 180/180 | exhaustive-collocation catch-all | All 26 criteria at ceiling. STRONG C-25 (13+ enumeration + catch-all) demonstrates that the unlisted-collocation escape route is structurally closed by catch-all. Carries the exhaustive-collocation signal but disproves its necessity for C-25 passage. |
| 5 | **V-01** | 180/180 | none | All 26 criteria at ceiling. STRONG C-24 (AUDIT RESULT slot) is cleanest single-axis implementation; disproves the AUDIT RESULT slot as a C-24 pass condition requirement. No above-ceiling signals. |

---

## Excellence Signals (above 180-pt ceiling)

### Signal 1 — Inertia Competitor Phase Framing (V-03 isolated, V-05 full strength)

The named-competitor STATUS QUO mechanism produces three structural properties no generic baseline achieves:

**Property 1 — Unambiguous coverage trace anchor**: The inertia competitor name must appear in the coverage table column 2. "The old workflow" fails by name. The trace is grep-checkable against a string, not interpretable from a phrase. This is above C-17's current ceiling (which requires a STATUS QUO element in column 2 without requiring tool-name fidelity).

**Property 2 — Phase-differentiated body language templates**: P1 bodies must name dual-tool parallelism ("I still have [tool] open because I don't trust this for [task] yet."). P3 bodies must name a specific parity gap by capability comparison ("In [tool], I could do X. I cannot find the equivalent here."). These are testable sentence-level instructions; C-11 STATUS QUO grounding only requires that bodies trace to a scenario element -- not that the body language vary by phase in a describable way.

**Property 3 — Gap analysis framing through switching lens**: Doc gaps are framed as "gaps that cause users to open the inertia competitor for documentation of the equivalent task." Design gaps include "feature parity gaps vs. the inertia competitor's equivalent capability." This re-frames gap analysis from generic documentation deficiencies to switching-friction-specific deficiencies -- a different signal profile.

**Why C-27 candidate**: A criterion requiring a named inertia competitor (not a category), adoption-curve phase body instructions, and tool-name-fidelity in coverage traces would distinguish V-03/V-05's output from any variation satisfying C-11. The failure mode C-11 leaves open: "STATUS QUO: [generic description of current process]" satisfies C-11 but produces no phase-differentiated body language and no grep-checkable coverage trace. The inertia competitor mechanism closes that failure mode structurally.

### Signal 2 — Exhaustive-Collocation Catch-All (V-02/V-04/V-05)

The catch-all clause "Any construction where a role title (SRE, PM, engineer, Support, C-[NN], UX, designer) precedes any verb whatsoever" makes C-25 compliance grep-checkable by role title alone, not role-title + enumerated-verb pairing. A scorer can search for " the SRE " or " the PM " and any verb that follows constitutes a violation -- no enumeration lookup required. C-25's pass condition requires 2 enumerated collocations; the catch-all replaces enumeration with a structural rule. This is a C-25 PASS+ signal: fully compliant at the criterion level while closing a structural gap the minimum threshold leaves open.

---

## New Criterion Candidates for v8

| Candidate | Weight | Points | Tightens | Source |
|-----------|--------|--------|----------|--------|
| C-27 -- Named Inertia Competitor Grounding | aspirational | 5 | C-11 | V-03/V-05 Step 1 + phase framing |

**C-27 structural logic**: C-11 STATUS QUO grounding passes when a current-state section exists and at least two ticket body framings trace to it. C-27 would require: (1) the STATUS QUO names a specific tool or named process (not a category); (2) at least one P1 ticket body explicitly names dual-tool parallelism ("I still have [tool] open..."); (3) at least one P3 ticket body names a specific missing capability by comparison ("In [tool], I could do X."). Coverage table column 2 must contain the named tool string (grep-checkable). C-11 passes with generic scenario grounding; C-27 passes only when a named competitor + adoption-curve differentiated body language is present.

**v8 projection**: 19 aspirational criteria / 95 pts. Total ceiling: 60 + 30 + 95 = **185**.

---

## Round 7 Hypothesis Ledger

| Variation | Hypothesis | Result | Finding |
|-----------|-----------|--------|---------|
| V-01 | AUDIT RESULT output slot is the C-24 differentiator | DISPROVEN | Slot strengthens enforcement but is not required. V-02 passes C-24 without it. |
| V-02 | Exhaustive enumeration (13+) closes the unlisted-collocation escape route for C-25 | CONFIRMED (for closing the escape route) but DISPROVEN (as a pass condition requirement) | 2 collocations satisfy C-25; exhaustive enumeration + catch-all exceed the criterion without producing a new scored criterion |
| V-03 | Named inertia competitor produces stronger STATUS QUO traces and phase-differentiated bodies | CONFIRMED | Above-ceiling signal generated; C-27 candidate identified; orthogonal to new criteria mechanism strength |
| V-04 | C-24 and C-25 at full strength do not interfere | CONFIRMED | Non-interference verified; no emergent above-ceiling signal from combination |
| V-05 | Full synthesis satisfies all 26 criteria simultaneously | CONFIRMED | 180/180 ceiling achieved; inertia competitor phase framing is the primary above-ceiling signal |

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["inertia-competitor-phase-framing"]}
```
