---

## Scorecard: quest-rubric — Round 1

**Trace artifact**: placeholder (scored as prompt-quality projections — evaluating whether each variation reliably produces rubric outputs satisfying each criterion)

### Scoring Grid

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 All 5 fields present | essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Weight distribution in spec | essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula + threshold stated | essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Criteria are skill-specific | essential | PARTIAL | PARTIAL | PASS | PASS | PASS |
| C-05 Pass conditions binary/testable | essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Ordered by tier | recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Categories from allowed set | recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Distinct failure modes | recommended | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-09 Rubric is calibrated | aspirational | FAIL | PARTIAL | PARTIAL | FAIL | PARTIAL |
| C-10 Evolution hook present | aspirational | PASS | PASS | PASS | PASS | PASS |

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | Golden |
|-----------|---------------|-----------------|-------------------|-------|--------|
| V-01 | 54 | 25 | 5 | **84** | NO |
| V-02 | 54 | 25 | 7.5 | **86.5** | NO |
| V-03 | 60 | 25 | 7.5 | **92.5** | YES |
| V-04 | 60 | 25 | 5 | **90** | YES |
| V-05 | 60 | 30 | 7.5 | **97.5** | YES |

**Ranking**: V-05 > V-03 > V-04 > V-02 > V-01

---

### Key Findings

**C-04 (skill-specificity)** is the decisive discriminator between V-01/V-02 and the rest. V-01 and V-02 both fail to pass it because neither explicitly names generic criteria as the enemy. V-03 passes by mid-prompt instruction; V-04 passes with an inline rewrite rule; V-05 passes hardest by opening with the named failure before any construction begins.

**C-08 (distinct failure modes)** is where V-05 separates from V-03 and V-04. All others get PARTIAL because they don't require proof that the filter ran. V-05's rejection log in the Design Rationale ("which generic criteria were considered and rejected") turns intent into evidence.

**V-04 vs V-03 trade-off**: V-04 has the clearest pass-condition construction logic (acceptable/unacceptable anchors list is best in class) but drops C-09 to FAIL by removing all reflection steps. V-03's conversational framing recovers C-09 to PARTIAL at the cost of less rigorous anchor guidance. Net: V-03 scores higher (92.5 vs 90) because calibration partial > calibration fail.

**Key bets verdicts:**
- V-02 vs V-01: Prose format helps marginally (+2.5) but doesn't escape the generic-criteria trap
- V-04 vs V-01: Front-loading construction logic works (+6) but costs calibration (C-09 FAIL)
- V-05 vs V-04: Inertia framing is additive, not redundant (+7.5 over V-04)

### Excellence Signals

1. **Inertia framing** — name the dominant failure mode before any construction instructions; it anchors every subsequent decision as a persistent filter
2. **Amend-as-validation-gate** — amend step lists explicit per-criterion quality checks (specificity, binary pass condition, real failure mode), not just "revise on feedback"
3. **Rejection log** — design rationale requires naming generic criteria considered and rejected, proving the specificity filter ran

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["inertia-framing: name the dominant failure mode before any construction instructions to anchor all subsequent decisions", "amend-as-validation-gate: amend step lists explicit per-criterion quality checks (specificity, binary pass condition, real failure mode) not just 'revise on feedback'", "rejection-log: design rationale requires naming generic criteria considered and rejected, proving the specificity filter ran"]}
```
out anchors" list (good, sufficient, appropriate, thorough, complete).

**C-08 PARTIAL**: Phase-by-phase construction protocol (one criterion per lifecycle phase) reduces accidental overlap but does not require a formal distinctness check across the essential set.

**C-09 FAIL**: No design rationale step, no calibration mechanism. The most technically rigorous prompt for criterion construction but the least reflective — no step asks the author to verify the rubric would classify outputs correctly.

### V-05 — Inertia framing + imperative + table

**C-04 PASS**: Inertia framing names the exact failure mode before construction begins ("'output is well-structured,' 'covers all required phases,' 'is clear and complete'"). Then the skill-specificity test is embedded in the Execute step: "Does this criterion name something specific to this skill — a field name, a count range, a formula, a structural property — or is it generic?" Both a pre-construction filter AND an inline per-criterion test.

**C-08 PASS**: The Execute step requires "Only genuinely unusable failures are essential" (filters duplicates by requiring the unusability test to be distinct per criterion). The Amend step asks "Does it catch a real failure mode?" which forces a reviewer to verify coverage. The Design Rationale requires "which generic criteria were considered and rejected" — proving the specificity filter ran, not just that the author intended to run it.

**C-09 PARTIAL**: Design Rationale includes "which generic criteria were considered and rejected, which criterion is hardest to satisfy" — demonstrates calibration reasoning. Does not require a concrete thought experiment with a specific poor output. Partial credit.

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | All Essential Pass | Golden |
|-----------|---------------|-----------------|-------------------|-------|-------------------|--------|
| V-01 | 54 (4.5/5 * 60) | 25 (2.5/3 * 30) | 5 (1/2 * 10) | **84** | NO | NO |
| V-02 | 54 (4.5/5 * 60) | 25 (2.5/3 * 30) | 7.5 (1.5/2 * 10) | **86.5** | NO | NO |
| V-03 | 60 (5/5 * 60) | 25 (2.5/3 * 30) | 7.5 (1.5/2 * 10) | **92.5** | YES | YES |
| V-04 | 60 (5/5 * 60) | 25 (2.5/3 * 30) | 5 (1/2 * 10) | **90** | YES | YES |
| V-05 | 60 (5/5 * 60) | 30 (3/3 * 30) | 7.5 (1.5/2 * 10) | **97.5** | YES | YES |

**Ranking**: V-05 (97.5) > V-03 (92.5) > V-04 (90) > V-02 (86.5) > V-01 (84)

---

## Excellence Signals

Patterns from V-05 that explain its lead over V-03 and V-04:

**1. Inertia framing as persistent filter**
Opening with the named failure mode ("generic quality criteria") before any construction instructions anchors every subsequent decision. The author cannot "forget" to run the specificity test because they were told what they are preventing before they started. V-03 names the same failure mid-prompt ("not 'is it well-structured' but 'does it contain X, Y, Z'") but the framing arrives after the author has already started thinking, not before.

**2. Closed-world constraint on categories**
"correctness / depth / format / coverage / behavior -- no other values" is stronger than listing the allowed values without closure. The phrase "no other values" prevents invented categories without requiring the author to remember that invented categories are disallowed.

**3. Amend-as-validation-gate**
V-05's Amend step lists explicit per-criterion quality checks: "is it specific enough? Is the pass condition binary? Does it catch a real failure mode?" This turns revision into a structured quality gate rather than a freeform editorial pass. V-01, V-03, and V-04 treat Amend as "revise on feedback" without specifying what the reviewer should check.

**4. Rejection log in Design Rationale**
Requiring "which generic criteria were considered and rejected" in the design rationale creates proof that the specificity filter ran. An author who cannot name any rejected generic criteria probably did not run the filter seriously. This is the key reason V-05 passes C-08 while all others are PARTIAL: the Amend + Design Rationale combination forces retroactive verification of the distinctness constraint.

---

## Key Bets — Verdicts

**V-02 vs V-01 (Does prose format produce richer pass conditions?)**
Marginal advantage to V-02 (+2.5 points). Prose blocks produce a slightly better calibration story (design rationale paragraph) and the Failure signal field provides implicit specificity pressure. But neither variation passes C-04, so prose format alone is insufficient to escape the generic-criteria trap.

**V-04 vs V-01 (Does front-loading construction logic reduce generic criteria?)**
V-04 +6 points over V-01, with all essential passing. The skill-specificity test and acceptable/unacceptable anchor lists are the decisive additions. However V-04 pays a cost: no design rationale, no calibration step (C-09 FAIL vs V-01's FAIL for the same reason). Front-loading construction logic works — but trading away reflection costs points.

**V-05 vs V-04 (Does naming the failure mode outperform construction protocol alone?)**
V-05 +7.5 over V-04. The inertia framing is not redundant once the construction protocol is present — it adds to it by (a) front-loading the failure mode as motivation before the protocol, and (b) adding the rejection log which produces C-08 PASS that V-04 cannot achieve. The combination is strictly better.

---

## Notes

This is Round 1. No golden output exists yet. Scores are projected from prompt quality — how reliably each variation's instructions would produce rubric outputs satisfying each criterion. When `/quest:golden` produces actual rubric artifacts, re-run this scorecard against the real outputs.

C-09 (calibration) remains aspirational for all variations — the criterion requires concrete good/poor output examples that don't exist at R1. Expect C-09 to resolve to PASS or FAIL more clearly in R2+ when golden outputs exist.
