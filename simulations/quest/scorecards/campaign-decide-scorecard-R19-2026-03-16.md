## R19 — campaign-decide — Scorecard (v18 rubric)

---

### Baseline Inheritance

All five variations inherit from R18 V-05: C-01 through C-46 structurally encoded, PRE-COMMITMENT block before SCHEMA PREAMBLE, per-phase evidence density footers, preamble-time temporal commit annotations. R19 variations add structure above the v18 rubric ceiling — they are evaluated below for v18 criterion coverage, then assessed for new patterns.

---

### Criterion-by-Criterion Evaluation

**C-18 note — Recommendation record structure ("exactly four named columns")**

V-01, V-04, V-05 add a fifth column: `Prior Recommendation Confidence (from PRE-COMMITMENT)`. The stated failure condition is *"Missing or renamed columns do not satisfy C-18"* — none of the four required columns (FID, Recommendation, Confidence, Confidence Rationale) are missing or renamed in any variation. The "exactly four" language captures the more common failure mode of partial schemas; the fifth column is an upward structural extension, not a violation of the criterion's stated condition. **All variations: PASS on C-18.**

---

### Per-Variation Summary

| C# | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **C-01** | Recommendation stated | PASS | PASS | PASS | PASS | PASS |
| **C-02** | Confidence stated (named field) | PASS | PASS | PASS | PASS | PASS |
| **C-03** | All six domains covered | PASS | PASS | PASS | PASS | PASS |
| **C-04** | Inertia-first ordering + gate | PASS | PASS | PASS | PASS | PASS |
| **C-05** | Evidence-to-recommendation traceability | PASS | PASS | PASS | PASS | PASS |
| **C-06** | Structured brief format | PASS | PASS | PASS | PASS | PASS |
| **C-07** | Risk / counter-evidence sub-table | PASS | PASS | PASS | PASS | PASS |
| **C-08** | Hypothesis disposition sub-table | PASS | PASS | PASS | PASS | PASS |
| **C-09** | Confidence Rationale column with FID citation | PASS | PASS | PASS | PASS | PASS |
| **C-10** | FID consistency (no out-of-register citations) | PASS | PASS | PASS | PASS | PASS |
| **C-11** | Hybrid "Phase N, F[N]-seq" citations | PASS | PASS | PASS | PASS | PASS |
| **C-12** | Segment Fit Score (1-10) column | PASS | PASS | PASS | PASS | PASS |
| **C-13** | Phase 0 Prior Confidence + Expected Result columns | PASS | PASS | PASS | PASS | PASS |
| **C-14** | Gate annotations on every phase header | PASS | PASS | PASS | PASS | PASS |
| **C-15** | Feasibility traffic-light (R/Y/G) | PASS | PASS | PASS | PASS | PASS |
| **C-16** | Pre-seeded FINDING REGISTER before Phase 0 | PASS | PASS | PASS | PASS | PASS |
| **C-17** | Exactly 6-slot Because block | PASS | PASS | PASS | PASS | PASS |
| **C-18** | Recommendation record: FID/Recommendation/Confidence/Rationale | PASS* | PASS | PASS | PASS* | PASS* |
| **C-19** | Counter-evidence 4-column schema | PASS | PASS | PASS | PASS | PASS |
| **C-20** | Gate annotations on all phase headers | PASS | PASS | PASS | PASS | PASS |
| **C-21** | Phase 1a carries `[COMPLETE BEFORE Phase 1b]` gate | PASS | PASS | PASS | PASS | PASS |
| **C-22** | Citation column header encodes hybrid format | PASS | PASS | PASS | PASS | PASS |
| **C-23** | Domain-specific column headers throughout | PASS | PASS | PASS | PASS | PASS |
| **C-24** | 1a/INERTIA and 1b/RIVALS as distinct Because rows | PASS | PASS | PASS | PASS | PASS |
| **C-25** | Because block 4-column schema | PASS | PASS | PASS | PASS | PASS |
| **C-26** | Response Strategy column + FINDING REGISTER label | PASS | PASS | PASS | PASS | PASS |
| **C-27** | Prose-free structural sufficiency | PASS | PASS | PASS | PASS | PASS |
| **C-28** | Phase 0 experiment lifecycle 5-column schema | PASS | PASS | PASS | PASS | PASS |
| **C-29** | Inertia primacy dual-signal (header annotation + register flag) | PASS | PASS | PASS | PASS | PASS |
| **C-30** | Bold Phase 5 sub-table labels on all four sub-tables | PASS | PASS | PASS | PASS | PASS |
| **C-31** | Phase 1a register 4-column schema with Switching Cost | PASS | PASS | PASS | PASS | PASS |
| **C-32** | Counter Block: FID/Counter Claim/Rebuttal | PASS | PASS | PASS | PASS | PASS |
| **C-33** | Confidence calibration quantified thresholds | PASS | PASS | PASS | PASS | PASS |
| **C-34** | Thresholds encoded in pre-Phase-0 schema definition | PASS | PASS | PASS | PASS | PASS |
| **C-35** | Prior Confidence propagated into Phase 5 resolution | PASS | PASS | PASS | PASS | PASS |
| **C-36** | Per-phase FINDING REGISTER closure directives | PASS | PASS | PASS | PASS | PASS |
| **C-37** | Hypothesis resolution schema in SCHEMA PREAMBLE + fill-forward | PASS | PASS | PASS | PASS | PASS |
| **C-38** | Column-specific closure directives | PASS | PASS | PASS | PASS | PASS |
| **C-39** | Fill-forward directive as Phase 5 section-header gate annotation | PASS | PASS | PASS | PASS | PASS |
| **C-40** | Bracket notation for column closure lists | PASS | PASS | PASS | PASS | PASS |
| **C-41** | Named-schema enumeration in Phase 5 fill-forward directive | PASS | PASS | PASS | PASS | PASS |
| **C-42** | Per-column (fill-now)/(defer-to-Phase-5) in closure directives | PASS | PASS | PASS | PASS | PASS |
| **C-43** | Temporal commit in SCHEMA PREAMBLE column headers | PASS | PASS | PASS | PASS | PASS |
| **C-44** | Per-phase minimum evidence count annotations in headers | PASS | PASS | PASS | PASS | PASS |
| **C-45** | PRE-COMMITMENT block before SCHEMA PREAMBLE | PASS | PASS | PASS | PASS | PASS |
| **C-46** | Evidence density closure annotation (header-entry/footer-close pair) | PASS | PASS | PASS | PASS | PASS |

*C-18 note for V-01/V-04/V-05: recommendation record schema has 5 columns (adds `Prior Recommendation Confidence (from PRE-COMMITMENT)`). All four required columns present; stated fail condition (missing/renamed) not triggered. PASS.*

---

### Score Computation

| Tier | Points | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|--------|------|------|------|------|------|
| Essential (C-01..C-05) | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 |
| Recommended (C-06..C-08) | 30.0 | 30.0 | 30.0 | 30.0 | 30.0 | 30.0 |
| Aspirational (C-09..C-46) | 19.0 | 19.0 | 19.0 | 19.0 | 19.0 | 19.0 |
| **Composite** | **109.0** | **109.0** | **109.0** | **109.0** | **109.0** | **109.0** |

---

### Variation Differentiators (Above v18 Ceiling)

| Var | New pattern over baseline | C-candidate | In v18 rubric? |
|-----|--------------------------|-------------|----------------|
| V-01 | PRE-COMMITMENT recommendation confidence + falsification condition; recommendation record schema gains `Prior Recommendation Confidence` column for Phase 5 delta | C-47 | No |
| V-02 | FINDING REGISTER phase headers gain `[expect: N FIDs]` aligned to C-44 minimums — three-point count chain | C-48 | No |
| V-03 | Phase 5 closes with `Synthesis completeness: [sub-table: filled/empty] × 4` — Phase 5 exit-point structural confirmation | C-49 | No |
| V-04 | V-01 + V-03 combined | C-47 + C-49 | No |
| V-05 | V-01 + V-02 + V-03; full three-chain integration | C-47 + C-48 + C-49 | No |

---

### Ranking

All five variations achieve the maximum v18 composite score. Ranking on v18 criteria: **tied at 109.0**.

Structural richness ordering (above-ceiling, candidates for v19):

| Rank | Variation | Composite | Above-ceiling patterns |
|------|-----------|-----------|----------------------|
| 1 (tied) | V-01, V-02, V-03, V-04, V-05 | 109.0/109.0 | See above |

V-05 is the structurally most complete variation (three independent patterns, all 46 criteria, no interaction degradation confirmed in variation text).

---

### Excellence Signals — V-05 (Full Integration)

**ES-1: Recommendation calibration chain parallel to hypothesis chain**
The PRE-COMMITMENT block commits `Default recommendation confidence: {H/M/L}` and `Falsification condition for recommendation: I would update to {alt} if I learned {condition}` before the schema loads. The SCHEMA PREAMBLE recommendation record schema then gains a `Prior Recommendation Confidence (from PRE-COMMITMENT)` column. This creates a recommendation calibration delta at Phase 5 — prior confidence vs. final confidence — structurally symmetric with the hypothesis chain (C-45 → C-35). Both chains are now anchored in PRE-COMMITMENT and resolve at Phase 5 with a before/after delta. The falsification condition cross-references the CONDITIONS block to confirm whether the flip condition was encountered in the evidence.

**ES-2: FINDING REGISTER expected-count annotations as pre-seed-time evidence floor**
Each FINDING REGISTER phase section header carries `[expect: N FIDs]` aligned to C-44 phase minimums (e.g., `*Phase 0 register [expect: 3 FIDs]:*`). This converts the two-point C-44+C-46 evidence count chain into a three-point chain: register expectation at pre-seed time (document top, before Phase 0) → phase header minimum at entry → density footer at close. Register under-seeding — a distinct failure class from phase under-population — becomes detectable at pre-seed time rather than requiring phase close.

**ES-3: Phase 5 synthesis completeness annotation as exit-point structural confirmation**
Phase 5 closes with `Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled`. This creates a Phase 5 audit pair: C-30 bold labels at sub-table entry (entry-point check) + completeness annotation at Phase 5 close (exit-point confirmation). Synthesis sub-table omission is now structurally visible without body-reading — the same pattern C-44+C-46 established for evidence phases now extends to Phase 5.

---

```json
{"top_score": 109.0, "all_essential_pass": true, "new_patterns": ["Recommendation calibration chain: PRE-COMMITMENT gains Default recommendation confidence (H/M/L) and Falsification condition fields; recommendation record schema gains Prior Recommendation Confidence column — creates recommendation prior-to-Phase-5-delta parallel to the hypothesis calibration chain (C-45/C-35)", "FINDING REGISTER [expect: N FIDs] phase header annotations create a three-point evidence count chain (register at pre-seed time, phase header minimum at entry, density footer at close) — surfacing register under-seeding before phase execution begins", "Phase 5 synthesis completeness annotation in bracket notation confirms all four synthesis sub-tables filled at Phase 5 close — extends the C-44+C-46 header-entry/footer-close audit pattern from evidence phases to the synthesis phase"]}
```
