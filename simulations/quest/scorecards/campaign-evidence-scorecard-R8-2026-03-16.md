## Quest Score — campaign-evidence, Round 8

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (60 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Multi-stage campaign (5 stages) | PASS | PASS | PASS | PASS | PASS |
| C-02 | Evidence before hypothesis | PASS | PASS | PASS | PASS | PASS |
| C-03 | Hypotheses with falsification conditions | PASS | PASS | PASS | PASS | PASS |
| C-04 | Self-contained coherent output | PASS | PASS | PASS | PASS | PASS |

All five variates: **4/4 essential**. Every variate structures five named stages (S1:Web, S2:Intel, S3:Hypothesis, S4:Analysis, S5:Synthesis); all enforce SEQUENCING RULE before hypothesis declaration; all require falsification conditions per hypothesis; all define an OUTPUT BRIEF with title, sections, and synthesized narrative.

---

### Recommended Criteria (30 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-05 | Source attribution per claim | PASS | PASS | PASS | PASS | PASS |
| C-06 | Synthesis distinguishes consensus from conflict | PASS | PASS | PASS | PASS | PASS |
| C-07 | Confidence calibrated, non-uniform | PASS | PASS | PASS | PASS | PASS |

All five variates: **3/3 recommended**. All mandate `[web search]` / `[intelligence: path]` / `[analysis]` labels at every evidence stage. All require explicit Consensus (findings where S1+S2 agree, cited by label) and Conflict (named divergence, not just both sides listed). All include CALIBRATION RULE with anti-uniformity guard and require ≥2 distinct confidence levels at S4.

V-05 note: ATTRIBUTION is structural via the Evidence Matrix Stage column — a null Stage cell fails the rule without needing a prose label check. Still satisfies C-05.

---

### Aspirational Criteria (10 pts, denominator = 19)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-08 | Gaps and open questions | PASS | PASS | PASS | PASS | PASS | All require explicit "Gaps and Open Questions" section in S5 and output brief |
| C-09 | Decision readiness signal | PASS | PASS | PASS | PASS | PASS | All include Decision Readiness as required S5 output |
| C-10 | Hypotheses declared post-evidence | PASS | PASS | PASS | PASS | PASS | SEQUENCING RULE enforces S1+S2 complete before S3 in all variates |
| C-11 | Calibration anti-pattern guard | PASS | PASS | PASS | PASS | PASS | All: CALIBRATION RULE includes anti-uniformity guard and S4 recalibrate instruction |
| C-12 | Decision readiness = one sentence | PASS | PASS | PASS | PASS | PASS | All specify "exactly one sentence" with posture + specific gap |
| C-13 | Named rules with inline invocations | PASS | PASS | PASS | PASS | PASS | All four rules named in preamble, invoked by identifier at applicable stages |
| C-14 | Hypothesis reordering rationale stated | PASS | PASS | **FAIL** | PASS | **FAIL** | V-01/V-02/V-04: "A hypothesis anchored before evidence is a bias, not a hypothesis." V-03 preamble says "evidence before hypothesis; named, cite by ID" — rule statement only, no rationale. V-05 SEQUENCING RULE is structural/mechanical only — focuses on sort-verification, not the underlying principle |
| C-15 | Evidence-first formalized as named rule | PASS | PASS | PASS | PASS | PASS | All: SEQUENCING RULE is a named, citable rule in preamble |
| C-16 | Zero-gap rule invocation | PASS | PASS | PASS | PASS | PASS | All coverage map `*` cells have corresponding invocation in stage body |
| C-17 | Coverage map declared prospectively | PASS | PASS | PASS | PASS | PASS | All: coverage map in GOVERNANCE PREAMBLE before Stage 1 |
| C-18 | All rules at peer tier in preamble | PASS | PASS | PASS | PASS | PASS | V-04 adds explicit "All five rules are peers. No rule is primary." V-03: code-block format treats all four rules identically. Others: all bold headers at same level |
| C-19 | Coverage map immutability declared | PASS | PASS | PASS | PASS | PASS | V-01/V-02/V-04/V-05: explicit "Immutable -- cannot be modified after any stage executes." V-03: preamble header "immutable, declared before Stage 1" + coverage map labeled "(immutable)" — functionally satisfies the intent |
| C-20 | Rule scope embedded inline in declaration | PASS | PASS | PASS | PASS | PASS | All rules include `[invoked at: Stage X, ...]` within rule body. V-03 uses `invoked: S1 S2 S3 S4 S5` inline in code block |
| C-21 | Interrogative invocation at critical rules | PASS | PASS | PASS | PASS | PASS | All: CALIBRATION at S4 uses "at least two distinct confidence levels assigned/present? [ Yes / No ]" — binary question, not passive tag |
| C-22 | Universal binary invocation format | PASS | PASS | PASS | PASS | PASS | Every invocation in every variate uses `[ Yes / No ]` or `[ Y/N ]` binary form — SEQUENCING, ATTRIBUTION, CALIBRATION, FALSIFICATION all covered |
| C-23 | Stage-indexed invocation trail | PASS | PASS | PASS | PASS | PASS | All: `[Stage N of 5]` or `[SN/5]` suffix on every invocation tag |
| C-24 | Per-stage entry and exit conditions | PASS | PASS | PASS | PASS | PASS | All: each stage has explicit named Entry condition and Exit condition with verifiable criteria |
| C-25 | Gate record as required output artifact | PASS | PASS | PASS | PASS | PASS | V-01/V-04: pre-templated in preamble + transferred to output section 2. V-02/V-03/V-05: gate record table appears as named section in OUTPUT BRIEF. All satisfy "not only embedded in stage narrative" |
| C-26 | Consolidated invocation audit table (derived count) | PASS | PASS | PASS | PASS | PASS | V-01/V-03: 12-row table with "derived from coverage map sum above" label + verify binary check. V-02/V-05: derivation protocol — executor sums Count column, writes "Derived row count = ___", never sees a pre-declared integer. V-04: 14-row table (5+3+2+2+2=14), INERTIA addition shifts count automatically |

**Aspirational pass counts**: V-01: 19/19, V-02: 19/19, V-03: 18/19 (miss C-14), V-04: 19/19, V-05: 18/19 (miss C-14)

---

## Composite Scores

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/19 * 10)
```

| Variate | Essential | Recommended | Aspirational | Composite | Golden? |
|---------|-----------|-------------|--------------|-----------|---------|
| **V-01** | 4/4 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100** | YES |
| **V-02** | 4/4 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100** | YES |
| V-03 | 4/4 → 60 | 3/3 → 30 | 18/19 → 9.47 | **99.47** | YES |
| **V-04** | 4/4 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100** | YES |
| V-05 | 4/4 → 60 | 3/3 → 30 | 18/19 → 9.47 | **99.47** | YES |

All five variates exceed the golden threshold (all essential pass AND composite ≥ 80). Three tie at 100.

---

## Ranking

1. **V-01, V-02, V-04** — tied at 100. Each 19/19 aspirational.
2. **V-03, V-05** — tied at 99.47. Both miss only C-14 (hypothesis reordering rationale stated).

---

## Excellence Signals (from top-scoring variates)

**Pre-templated gate record (V-01, V-04)** — Embedding the Gate Record table in the preamble with blank cells before Stage 1 executes changes compliance from a creative act (remembering to create a section) to a mechanical act (filling a cell that already exists). A blank cell is visible before the brief is finalized — it cannot be concealed by post-hoc addition. V-04 inherits this from V-01 and extends it to a 5-rule campaign without modification.

**Derivation protocol (V-02)** — Never embedding a hardcoded row count eliminates the drift risk entirely. The executor sums the Count column themselves, writes "Derived row count = ___", and any mismatch is their own arithmetic error — not a reviewer-detected discrepancy between prompt and output. The prompt cannot be inconsistent with itself because the count is a fresh computation at execution time, not a prior declaration that can go stale.

**INERTIA RULE map growth (V-04)** — Adding a 5th peer rule as an explicit governance rule (not a convention) demonstrates that the coverage map and derivation protocol scale without prompt edits. The derived row count shifts 12→14 automatically. The explicit peer declaration "All five rules are peers. No rule is primary." preempts any ambiguity about whether INERTIA is a real rule or a structural annotation.

**Structural sequencing proof via column sort (V-05)** — Encoding SEQUENCING compliance as a column value rather than a prose assertion makes violations mechanically detectable: sort the Stage column, any S3/S4/S5 row before S1/S2 rows is a sequencing violation. The Grounded In column constraint (S1/S2 row references only) enforces the same property at the hypothesis level. V-05 scores 99.47 only because it omits the rationale sentence — the structural mechanism is sound.

**C-14 gap pattern (V-03, V-05)** — Both fail by omitting the rationale for evidence-first ordering. The SEQUENCING rule is stated and enforced mechanically but the underlying principle ("a hypothesis anchored before evidence gathering is a bias, not a hypothesis") is absent. This matters: a reader who encounters a sequencing violation needs to understand why the constraint exists, not just that it exists. The explicit rationale sentence in V-01/V-02/V-04 is doing real work.

---

## New Patterns (C-27+ candidates)

**Derivation-protocol gate** — The audit table row count is never pre-declared; it is always re-derived from the coverage map Count column at execution. The protocol makes the executor perform the derivation, so any mismatch is their own arithmetic failure — not a discrepancy they could have missed because someone else wrote the number. Detection is internal, not reviewer-imposed.

**Pre-templated gate record** — Gate record table structure (with blank cells) appears in the preamble before Stage 1. Executor fills cells, does not create a section. A blank cell is structurally visible before the brief is finalized; there is no "I forgot to add the gate section" failure mode.

**INERTIA RULE map growth** — A fifth peer rule (or any future rule addition) shifts the derived row count automatically. Hardcoded counts would silently undercount new rule invocations across all applicable stages. The derivation protocol absorbs rule additions by design.

**Structural sequence proof** — SEQUENCING compliance encoded as a column sort value makes violations mechanically detectable without reading prose. The Grounded In column (S1/S2 row references only) extends this: hypothesis grounding becomes a structural constraint, not a self-assessment.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["derivation-protocol-gate: audit table row count always re-derived from coverage map Count column at execution time; executor performs derivation, cannot claim ignorance of a mismatch they introduced", "pre-templated-gate-record: gate record table with blank cells appears in preamble before Stage 1; compliance is filling cells not creating a section; blank cell is structurally visible before brief finalized", "inertia-rule-map-growth: adding a peer governance rule shifts derived row count automatically; hardcoded count would silently miss new rule invocations; derivation protocol absorbs rule additions without prompt edits", "structural-sequence-proof: sequencing compliance encoded as a column sort value in the Evidence Matrix; sort detects violations without reading prose; Grounded-In column disallows S4 row references making hypothesis grounding a structural constraint"]}
```
