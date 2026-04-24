Now I have enough to score all five variations. Let me work through the evaluation.

---

# corps-rob R11 Scorecard (rubric v9, 2026-03-17)

## Baseline State

V-05 R10 passes all 27 aspirational criteria (C-09 -- C-35) and all essential + recommended criteria. It is the ceiling under v9: composite 100, raw 27.

All five R11 variations explicitly preserve the complete V-05 R10 architecture, including every element listed as non-negotiable at R11 (C-24 through C-35, all three R10 additions). The three R11 axes introduce structural additions -- Synthesis F-IDs, Risk Shift Source F-ID, and STAGE VERDICT AGGREGATE -- that do not appear in rubric v9. They therefore do not affect the v9 raw count in either direction.

---

## Per-Variation Evaluation

### Essential Criteria (C-01 -- C-05) -- all variants

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Stage Attribution | PASS | PASS | PASS | PASS | PASS |
| C-02 Role-Loaded Perspective | PASS | PASS | PASS | PASS | PASS |
| C-03 Blocker Propagation | PASS | PASS | PASS | PASS | PASS |
| C-04 Stage Verdict w/ Calibration | PASS | PASS | PASS | PASS | PASS |
| C-05 VERDICT CALIBRATION table at stage header | PASS | PASS | PASS | PASS | PASS |

Evidence: All five carry identical VERDICT CALIBRATION, BLOCKER PROPAGATION RULE, and PHASE GATE PROPAGATION RULE at the Stage Template level. Stage Identity section names canonical label + role in every variant. No stage is anonymous. At least one finding per stage is grounded in the Part 0 Dimension (constraint is explicit in all five prompts). No essential regression in any variant.

**Essential subtotal: 5 x 12 = 60 (all five variants)**

---

### Recommended Criteria (C-06 -- C-08) -- all variants

| Criterion | All Variants |
|-----------|-------------|
| C-06 INERTIA ANCHOR w/ Displacement Map | PASS -- present in all five; minimum 2 D-ID rows, D-ID Ref constraint in Findings |
| C-07 Phase Gate (PASS/FAIL/CONDITIONAL w/ counts) | PASS -- PHASE GATE section present in all five with three-band severity count requirement and F-ID citation rule |
| C-08 ROB Summary with cross-cutting tables | PASS -- all five carry Blocker Resolution Status, Inertia Resolution Status, Cross-Cutting Themes, RESISTANCE TRAJECTORY, and LENS ACTIVATION CHAIN HEALTH |

**Recommended subtotal: 3 x 10 = 30 (all five variants)**

---

### Aspirational Criteria (C-09 -- C-35) -- all variants

The R11 document explicitly states that all five variants preserve the complete V-05 R10 architecture. V-05 R10 passed all 27 aspirational criteria under v9. The additions in R11 (Synthesis F-IDs, Risk Shift Source F-ID, Stage Verdict Aggregate) are net-new structural elements not addressed by any of the 27 aspirational criteria.

**Spot-check of v9-relevant criteria in each variant:**

| Criterion | Evidence Location | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------------------|------|------|------|------|------|
| C-09 Inter-stage blocker detection | BLOCKER PROPAGATION RULE present | PASS | PASS | PASS | PASS | PASS |
| C-12 Stage-boundary blocker field | Blocker Field table present in Stage Template | PASS | PASS | PASS | PASS | PASS |
| C-20 Part 0 LENS ACTIVATION pre-envelope | Present in Stage Template before Part 1 | PASS | PASS | PASS | PASS | PASS |
| C-23 CHAIN HEALTH w/ Remediation Action (C-35) | LENS ACTIVATION CHAIN HEALTH table present with Remediation Action column and anti-pattern guards | PASS | PASS | PASS | PASS | PASS |
| C-25 Displacement Map w/ D-IDs | D-IDs D-01/D-02 in INERTIA ANCHOR | PASS | PASS | PASS | PASS | PASS |
| C-27 D-ID Ref column | Present in Findings table | PASS | PASS | PASS | PASS | PASS |
| C-28 Named anti-pattern rejection in D-ID Ref | V-01/V-02: full guard text. V-03: full guard. V-04: compressed guard ("Empty D-ID Ref when RESISTANT+HIGH: format failure") -- format failure named; anti-pattern implicit. V-05: full guard text restored | PASS | PASS | PASS | PASS | PASS |
| C-30 Resolution Evidence in Blocker Resolution Status | Column present with anti-pattern guards | PASS | PASS | PASS | PASS | PASS |
| C-31 Primary F-IDs in Cross-Cutting Themes | Column present with "at least one F-ID per named stage" guard | PASS | PASS | PASS | PASS | PASS |
| C-32 Addressing F-IDs in Inertia Resolution Status | Column present with F-ID obligation when RESOLVED | PASS | PASS | PASS | PASS | PASS |
| C-33 Source F-IDs in Risk Register | Column present with "Inferred from ROB does not satisfy" guard | PASS | PASS | PASS | PASS | PASS |
| C-34 Supporting F-IDs in Mission Cascade | Column present with PARTIAL/GAP citation obligation | PASS | PASS | PASS | PASS | PASS |
| C-35 Remediation Action in Chain Health | Column present with BROKEN/PARTIAL requirement and anti-patterns | PASS | PASS | PASS | PASS | PASS |

Note on V-04 C-28 (compressed): The RESISTANT+HIGH format failure condition is preserved; what is condensed is the verbosity of inline guard text. The structural obligation remains explicit. PASS maintained.

**Aspirational raw: 27 / 27 for all five variants. Contributable: 10 (ceiling). All five variants.**

---

## Score Summary

| Variant | Essential (60) | Recommended (30) | Aspirational (max 10) | Composite | Raw (tie-break) |
|---------|---------------|------------------|-----------------------|-----------|-----------------|
| V-01 | 60 | 30 | 10 | **100** | 27 |
| V-02 | 60 | 30 | 10 | **100** | 27 |
| V-03 | 60 | 30 | 10 | **100** | 27 |
| V-04 | 60 | 30 | 10 | **100** | 27 |
| V-05 | 60 | 30 | 10 | **100** | 27 |

**All five variations score 100 composite / 27 raw under rubric v9.** The three R11 structural additions (Synthesis F-IDs, Risk Shift Source F-ID, Stage Verdict Aggregate) exceed the rubric v9 ceiling -- they would require new criteria (C-36, C-37, C-38) to differentiate the variations. Under v9, all variations are tied at the maximum.

---

## Ranking Under v9

No differentiation possible by score. Under a hypothetical v10 rubric where the three R11 axes become criteria:
- V-05: 3 new criteria pass (leader)
- V-04: 2 new criteria pass
- V-01, V-02, V-03: 1 new criterion each pass

**V-05 is the de facto leader** for v10 transition purposes, carrying all three closed structural positions.

---

## Excellence Signals from V-05

**1. Citation closure at the prose boundary using the same typed-field + anti-pattern mechanism as table columns**
V-05 applies the identical enforcement pattern established in v8/v9 (typed column + named invalid values) to prose slots, resolving the structural asymmetry where tables had citation obligations but prose slots did not. Synthesis F-IDs and Risk Shift Source F-ID each follow the exact pattern: typed field name, fill instruction, two or more named invalid values, explicit format failure condition. No new mechanism is invented -- the table-column citation architecture is extended to prose positions.

**2. Minimum-cardinality rules derived from slot semantics, not arbitrary thresholds**
Synthesis F-IDs requires at least two F-IDs because cross-stage synthesis is semantically defined as a characterization across multiple findings -- a one-finding "synthesis" is a contradiction in terms. Risk Shift Source F-ID requires exactly one because a risk shift identifies a single primary source of new visibility. The cardinality rules are not policy choices; they are derivable from the definition of each slot. V-05 makes this explicit in the hypothesis: "cross-stage synthesis by definition requires characterizing at least two findings in relation to each other."

**3. Verdict derivability chain completed end-to-end with pre-stated aggregation rule**
STAGE VERDICT AGGREGATE converts the ROB Summary Overall Verdict from an editorial synthesis into a derivable result: finding → [Risk Register Source F-IDs] → Stage Verdict → Aggregate (Governing F-ID, Propagation) → Overall Verdict. The worst-verdict-wins aggregation rule is stated before any stage runs, not applied retroactively. This makes the Overall Verdict independently auditable without reading all six Stage Verdict sections.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Citation closure at prose boundary: typed field + anti-pattern guard mechanism extended from table columns to prose slots (Synthesis F-IDs, Risk Shift Source F-ID), resolving the structural asymmetry where tables had citation obligations but prose did not", "Minimum cardinality derived from slot semantics: Synthesis F-IDs requires >=2 F-IDs because cross-stage synthesis is definitionally multi-finding; Risk Shift Source F-ID requires exactly 1 because a risk shift has a single primary source -- cardinality rules follow from semantic definitions, not policy", "Verdict derivability chain completed end-to-end: STAGE VERDICT AGGREGATE makes Overall Verdict mechanically derivable from six Stage Verdicts via pre-stated worst-verdict-wins rule with Governing F-ID per stage, eliminating editorial re-synthesis at the summary level"]}
```
