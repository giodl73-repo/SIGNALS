## quest-rubric Rubric v8

**Date:** 2026-03-16
**Version:** 8 (C-01 through C-26; essential C-01–C-05, recommended C-06–C-08, aspirational C-09–C-26)
**Formula:** `composite = (E/5 × 60) + (R/3 × 30) + (A/18 × 10)`
**Denominator change:** /14 → /18

---

### What changed from v7 → v8

Four new aspirational criteria extracted from Round 7 excellence signals. All four target
partial-credit integrity — a structural property that C-10 tests at the formula level but not at
the criterion level, the reproduction level, or the inter-boundary semantic level. C-10 is
necessary but not sufficient: a rubric can pass C-10 while still collapsing partial credit at
reproduction, failing to define it per criterion, or disagreeing across structural positions.

**C-23 — Per-criterion PARTIAL-CONDITION block** (A-4, R7)

V-03 introduces per-criterion PARTIAL-CONDITION blocks as sub-step A2d, requiring the Author to
define what evidence earns 0.5 weight for each criterion before moving to the next. V-05 extends
this: SA-1 `criteria_fields` includes a `partial_condition` key so the template itself carries
the field. The gap C-23 closes: C-10 tests whether the formula distinguishes PARTIAL from PASS.
C-23 tests whether each criterion's partial-credit condition is explicitly defined so an evaluator
can apply it without interpretation. Without per-criterion definition, the evaluator must decide
subjectively what earns 0.5 — violating C-02 (testable) at the partial-credit boundary. V-01
fails C-23: SA-1 has `verdict_weights` but no per-criterion PARTIAL-CONDITION; an evaluator
reading V-01 output knows PARTIAL = 0.5 in the formula but has no criterion-level specification
of when PARTIAL applies. V-04 fails for the same reason. V-03 and V-05 pass.

Distinct from C-10: C-10 tests formula-level PARTIAL/PASS distinction. C-23 tests
criterion-level PARTIAL-CONDITION definition (what evidence earns 0.5 for this specific
criterion).

**C-24 — Formula consistency across all structural positions** (A-4, R7)

V-02 fails: SA-1 states `essential_pass / N_essential * 60` (binary count), while FINAL RUBRIC
states the weighted form `(E_pass + 0.5 * E_partial) / N_essential * 60`. When two structural
positions disagree on formula type, the governing formula is ambiguous — a scorer could apply
either. V-01, V-04, and V-05 pass cleanly: SA-1 carries `verdict_weights` and a weighted
formula; FINAL RUBRIC restates it; no binary instance appears anywhere. V-03 is awarded PARTIAL:
SA-1 formula is binary-structured but carries a note ("PARTIAL verdicts count as 0.5 in the
numerator") and FINAL RUBRIC is fully expanded; the two positions agree on the 0.5 coefficient
but differ in formula structure, creating ambiguity for a scorer who reads SA-1 without the note.

Distinct from C-04: C-04 tests whether a scoring formula is present and explicit. C-24 tests
whether all formula instances across structural positions agree on the same weighting model
(binary instance in any position when another is weighted fails).

**C-25 — FINAL RUBRIC anti-collapse formula guard** (A-4, R7)

V-04 introduces: "Reproduce the weighted formula from SA-1 verbatim — do not collapse to binary
counting." V-05 inherits this guard. V-01 and V-03 have no such instruction. The risk without
it: even when SA-1 carries a correct weighted formula, the FINAL RUBRIC reproduction step is a
natural compression point — the model may simplify `(E_pass + 0.5 * E_partial) / N * 60` to
`E_pass / N * 60` because the binary form is shorter and structurally familiar. An explicit
prohibition in the reproduction step is the same class of defense as C-22's citation-retention
guard but targets formula structure rather than identifiers. V-01's FINAL RUBRIC has no
anti-collapse instruction despite having `verdict_weights` in SA-1 — a latent collapse risk.

Distinct from C-22: C-22 guards citation retention (CM-NN identifiers must not be stripped
during reproduction). C-25 guards formula integrity (weighted structure must not be collapsed to
binary during reproduction). Both are reproduction-fidelity guards over different content types.

**C-26 — VERDICT TIER DECLARATION inter-boundary block** (A-4, R7)

V-02, V-04, and V-05 have a named VERDICT TIER DECLARATION block positioned between SPEC
ANALYST: CLOSED and AUTHOR: OPEN that explicitly defines PASS, PARTIAL, and FAIL with semantic
conditions for each tier. This block is evaluator-facing: it provides the human-readable
grounding for the machine formula before any criterion is written. V-01 and V-03 embed tier
semantics only within SA-1 fields or formula comments — positions a scorer may not locate
when evaluating a completed rubric. The VERDICT TIER DECLARATION at a named inter-boundary
position makes tier semantics findable by structure rather than by content search. V-02's PARTIAL
on C-10 coexists with PASS on C-26: the Declaration defines PARTIAL correctly; the SA-1 formula
fails to use it, which is C-10/C-24's territory.

Distinct from C-21: C-21 tests whether machine-readable status tokens appear at every role
boundary (SA close, Author open, Author close, Auditor open). C-26 tests whether a named
semantic block defining verdict tier criteria appears between those boundaries, providing
evaluator-facing grounding for the weighting model.

---

### New failure modes

**FM-09 — Conflicting formula type across structural positions**: SA-1 declares a binary counting
formula while FINAL RUBRIC states a weighted formula (or vice versa). A scorer cannot determine
which instance governs. Caught by C-24.

**FM-10 — Formula collapse at reproduction without guard**: Weighted formula present in SA-1
collapses to binary count during FINAL RUBRIC reproduction because no explicit guard instruction
prohibits it. Caught by C-25.

**FM-11 — Subjective partial-credit evaluation**: Formula claims PARTIAL credit exists but no
criterion specifies what evidence earns 0.5 weight. Evaluator must interpret partial credit
subjectively, violating the testability requirement (C-02) at the partial-credit boundary.
Caught by C-23.

**FM-12 — Floating tier semantics**: Verdict tier definitions embedded only in SA-1 fields or
formula comments with no dedicated named structural block at a known inter-boundary position.
Evaluator must search for semantics rather than find them at a declared location. Caught by C-26.

---

### Essential Criteria

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-01 | **Skill identity declared** | Rubric names the target skill in the header |
| C-02 | **Criteria are testable** | Every criterion evaluable pass/fail/partial without subjective interpretation |
| C-03 | **Pass condition enforced** | Each criterion uses pass language ("must", "required"); advisory language fails |
| C-04 | **Scoring formula explicit** | Formula states the exact computation including denominator |
| C-05 | **Tier structure present** | Essential / Recommended / Aspirational tiers present |

### Recommended Criteria

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-06 | **Failure modes cataloged** | Known failure modes of target skill listed |
| C-07 | **Specificity test included** | At least one criterion tests output is specific to input, with concrete definition of "specific" for this skill |
| C-08 | **Version and date stamped** | Version number and date present |

### Aspirational Criteria (C-09 through C-26)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-09 | **Coverage of all output sections** | At least one criterion per named output section |
| C-10 | **Partial credit in formula** | Formula distinguishes PARTIAL from PASS; no binary collapse |
| C-11 | **External enforcement gate** | Named review role, rejection step, or prohibition checklist — not advisory language |
| C-12 | **Failure modes before criteria** | Failure mode catalog appears before the criteria it informs |
| C-13 | **Foil pair present** | At least one criterion has concrete PASS example and concrete FAIL example |
| C-14 | **Closed category enumeration** | At least one dimension uses a closed named-category enumeration; "e.g." fails |
| C-15 | **Specificity prohibitions converted** | Every specificity element is a testable output property; mechanism present |
| C-16 | **Fields have structural home** | All required fields declared in an explicit output schema block |
| C-17 | **SCHEMA BLOCK positionally first** | Output schema declaration is the first section, before failure modes and criteria |
| C-18 | **CONVERSION-MAP boolean gate** | Specificity conversion uses boolean classification table with DO-NOT-PROCEED completion gate |
| C-19 | **Identifier citation in canonical row** | CM-NN identifier appears in the CRITERION table row's Pass Condition field for each specificity criterion |
| C-20 | **Author Entry Gate structural block** | Gate uses imperative blocking phrasing AND names specific artifact identifiers (not phase labels) |
| C-21 | **Phase-completion status token at every boundary** | Machine-readable status tokens present at all four role boundaries: SA close, Author open, Author close, Auditor open; checklists do not pass |
| C-22 | **FINAL RUBRIC citation-retention guard** | FINAL RUBRIC section contains explicit instruction to retain CM-NN identifiers verbatim during reproduction; A2d-only or STRUCTURAL VERIFICATION-only fails |
| **C-23** | **Per-criterion PARTIAL-CONDITION block** | Every criterion has an explicit PARTIAL-CONDITION field or equivalent block defining what evidence earns 0.5 weight; PARTIAL defined only at the formula level with no per-criterion condition fails |
| **C-24** | **Formula consistency across structural positions** | All structural positions where the scoring formula appears (SA-1, VERDICT TIER DECLARATION, FINAL RUBRIC) state the same weighting model; a binary formula instance in any position when another position is weighted fails; PARTIAL when a prose note aligns intent but formula structure differs |
| **C-25** | **FINAL RUBRIC anti-collapse formula guard** | FINAL RUBRIC section contains explicit instruction to reproduce the weighted formula verbatim and not collapse to binary counting; absence of this guard fails; a guard addressing only citation retention (C-22) but not formula structure fails |
| **C-26** | **VERDICT TIER DECLARATION inter-boundary block** | A named VERDICT TIER DECLARATION (or equivalent) structural block defining PASS, PARTIAL, and FAIL semantics appears between SPEC ANALYST: CLOSED and AUTHOR: OPEN; tier semantics embedded only within SA-1 fields or formula comments fails |

---

### Baseline: R7 V-05 under v8 → 100.00 / Golden

R7 V-05 satisfies all 26 criteria: per-criterion PARTIAL-CONDITION in both SA-1 `criteria_fields`
and per-criterion A2d blocks (C-23); SA-1 `verdict_weights` and FINAL RUBRIC both weighted with
no binary instance (C-24); explicit "do not collapse to binary counting" guard in FINAL RUBRIC
(C-25); VERDICT TIER DECLARATION block positioned between SPEC ANALYST: CLOSED and AUTHOR: OPEN
(C-26).

**No entering gap identified for Round 8.** All 18 aspirational criteria satisfied by R7 V-05.
Round 8 direction: identify structural properties not yet formalized as criteria, or test rubric
generalization to non-quest-rubric skills.

---

### R7 Variations under v8 — Composite Scores

Formula: `(E/5 × 60) + (R/3 × 30) + (A/18 × 10)`

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-22 (from v7) | 5E/3R/14A | 5E/3R/13.5A | 5E/3R/14A | 5E/3R/14A | 5E/3R/14A |
| **C-23** Per-criterion PARTIAL-CONDITION | FAIL | FAIL | PASS | FAIL | PASS |
| **C-24** Formula consistency across positions | PASS | FAIL | PARTIAL | PASS | PASS |
| **C-25** FINAL RUBRIC anti-collapse guard | FAIL | PASS | FAIL | PASS | PASS |
| **C-26** VERDICT TIER DECLARATION inter-boundary | FAIL | PASS | FAIL | PASS | PASS |

| Score component | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------|------|------|------|------|------|
| E (C-01–C-05) /5 × 60 | 60.00 | 60.00 | 60.00 | 60.00 | 60.00 |
| R (C-06–C-08) /3 × 30 | 30.00 | 30.00 | 30.00 | 30.00 | 30.00 |
| A (C-09–C-26) /18 × 10 | 8.333 | 8.611 | 8.611 | 9.444 | 10.000 |
| **Composite** | **98.33** | **98.61** | **98.61** | **99.44** | **100.00** |
| **Band** | Golden | Golden | Golden | Golden | **Golden** |
| All essential PASS? | Yes | Yes | Yes | Yes | Yes |

**A-score detail:**

- V-01: 14 (v7 carry) + 0 (C-23 fail) + 1 (C-24 pass) + 0 (C-25 fail) + 0 (C-26 fail) = **15/18**
- V-02: 13.5 (v7 carry, C-10 partial) + 0 (C-23 fail) + 0 (C-24 fail) + 1 (C-25 pass) + 1 (C-26 pass) = **15.5/18**
- V-03: 14 (v7 carry) + 1 (C-23 pass) + 0.5 (C-24 partial) + 0 (C-25 fail) + 0 (C-26 fail) = **15.5/18**
- V-04: 14 (v7 carry) + 0 (C-23 fail) + 1 (C-24 pass) + 1 (C-25 pass) + 1 (C-26 pass) = **17/18**
- V-05: 14 (v7 carry) + 1 (C-23 pass) + 1 (C-24 pass) + 1 (C-25 pass) + 1 (C-26 pass) = **18/18**
