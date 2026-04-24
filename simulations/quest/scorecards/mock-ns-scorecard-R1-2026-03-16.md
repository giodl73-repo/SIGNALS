## Round 1 Scorecard -- mock-ns

**Rubric v1** | 5 essential / 3 recommended / 2 aspirational

### Scoring grid

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Header 6-field | PASS | PASS | PASS | PASS | PASS |
| C-02 CATEGORY registry | PASS | PASS | PASS | PASS | PASS |
| **C-03 FLAG + tier-conditional** | **PARTIAL** | **PARTIAL** | PASS | PASS | PASS |
| C-04 Fidelity warning | PASS | PASS | PASS | PASS | PASS |
| C-05 Skill-specific body | PASS | PASS | PASS | PASS | PASS |
| **C-06 Both emit lines** | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-07 Path + write confirm | PASS | PASS | PASS | PASS | PASS |
| C-08 Next-step line | PASS | PASS | PASS | PASS | PASS |
| C-09 topic-plan exclusion | PASS | PASS | PASS | PASS | PASS |
| C-10 Compliance override | PASS* | PASS* | PASS* | PASS* | PASS* |

*default-pass (no compliance tags in test case)

### Composite scores

| Variation | Score | Golden |
|-----------|-------|--------|
| V-01 | **84** | NO (C-03 PARTIAL) |
| V-02 | **84** | NO (C-03 PARTIAL) |
| V-03 | **100** | YES |
| V-04 | **100** | YES |
| V-05 | **100** | YES |

### Key findings

**Why V-01/V-02 scored 84**: Both lack a TOPICS.md setup step. Without S-0, tier is never resolved, so the tier-conditional flag case (C-03) can't fire correctly (PARTIAL), and the TOPICS.md emit line is absent (C-06 FAIL). Adding S-0 would have brought both to 100.

**Why V-03/V-04/V-05 scored 100**: TOPICS.md as a dedicated first step with its own emit line solves both gaps simultaneously. Register (V-03 structured vs V-04 conversational) does not affect score.

**Latent gap for R2**: No variation includes the explicit compliance override rule (`REAL-REQUIRED (compliance-sensitive)` for scout-compliance/trace-permissions with compliance tags). Passes by default in R1's Tier 1 no-tag scenario. A rubric v2 criterion that removes the default-pass would expose this in all five variations.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["TOPICS.md as dedicated S-0 step with emit line is the structural gate: it resolves tier before flag computation and satisfies C-06; V-01 and V-02 score 84 without it", "Register (conversational vs structured) does not affect score once the TOPICS.md step is anchored -- V-03 and V-04 tie at 100 despite different styles", "C-10 compliance override is a latent gap in all R1 variations -- passes by default in Tier 1 no-tag scenarios but absent from flag computation; rubric v2 should remove the default-pass to surface this"]}
```
Has only the skill selection emit (Phase 1) -- and that emit omits `tier: {tier}`. No TOPICS.md step exists. Two misses.

V-02: Has the skill selection emit WITH tier (S-1). No TOPICS.md step. First required line absent.

Both FAIL C-06. The root cause is the same: no S-0/setup step that reads TOPICS.md and emits the status line.

V-03/V-04/V-05 each open with a dedicated TOPICS.md step that emits the required status line before skill selection begins. Both lines present, both before the header. C-06 PASS.

**C-09 -- PASS for all**

All five variations explicitly exclude topic-status as the default for the topic namespace:
- V-01: "topic -> topic-plan (never topic-status -- that is meta-structural and excluded)"
- V-02: table note "topic-status excluded (meta-structural)"
- V-03: "topic -> topic-plan (NEVER topic-status -- excluded as meta-structural)"
- V-04: "topic -> topic-plan (never topic-status)"
- V-05: table note "NEVER topic-status (excluded: meta-structural)"

**C-10 -- default-pass for all**

No variation includes an explicit compliance override rule in flag computation. However, the rubric grants a default pass when no compliance tags are present. The test scenario for R1 carries no compliance tags. All PASS by default. The override instruction gap is noted for R2.

---

## Composite scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|-----------|---------------|------------------|-------------------|-------|
| V-01 | 54 (4.5/5) | 20 (2/3) | 10 (2/2) | **84** |
| V-02 | 54 (4.5/5) | 20 (2/3) | 10 (2/2) | **84** |
| V-03 | 60 (5/5) | 30 (3/3) | 10 (2/2) | **100** |
| V-04 | 60 (5/5) | 30 (3/3) | 10 (2/2) | **100** |
| V-05 | 60 (5/5) | 30 (3/3) | 10 (2/2) | **100** |

---

## Golden status

| Variation | All essential pass | Composite >= 80 | Golden |
|-----------|--------------------|-----------------|--------|
| V-01 | NO (C-03 PARTIAL) | yes (84) | NO |
| V-02 | NO (C-03 PARTIAL) | yes (84) | NO |
| V-03 | YES | yes (100) | **YES** |
| V-04 | YES | yes (100) | **YES** |
| V-05 | YES | yes (100) | **YES** |

---

## Ranking

1. **V-05** -- Convergent best: tier-conditional expressed as a 5-row explicit table, named critical skills list with wildcard notation (trace-*, listen-*), TOPICS.md step with tier carry-forward, exception handling for mock-review calls in C-08.
2. **V-03** -- Lifecycle emphasis: same structural coverage as V-05 for all criteria; tier-conditional in prose form. Slightly less mechanical than V-05's table.
3. **V-04** -- Two-axis (conversational + TOPICS.md anchor): achieves the same rubric score as V-03 despite lighter register. Demonstrates register is not load-bearing.
4. **V-01** -- Conversational register only: scores 84. Tier-conditional and TOPICS.md emit are the gaps. Would be golden with S-0 added.
5. **V-02** -- Table-centric format only: scores 84. Same structural gap as V-01 (no TOPICS.md step). Tables improve readability but do not compensate for the missing step.

---

## Excellence signals from V-05

1. **TOPICS.md as dedicated S-0** -- placing TOPICS.md read in its own labeled step with a required emit line, before any other computation, is the structural unlock for both C-06 and tier-conditional correctness (C-03). Without S-0, tier is never resolved and the flag computation cannot branch correctly.
2. **5-row tier table in S-3** -- expressing all flag cases (including the two HIGH-STRUCTURE critical rows for Tier 1 and Tier 2+) as a keyed table makes the tier-conditional unambiguous and machine-readable.
3. **Critical skills list with wildcard notation** -- naming trace-*, listen-* explicitly alongside the expansion list removes ambiguity about which skills trigger the tier-conditional refinement.
4. **Exception clause in Next-step instruction** -- V-05 names the exact condition under which the next-step line is omitted (mock-review regeneration), matching the rubric's exception case verbatim.

---

## New patterns from R1

1. **TOPICS.md as first step is the critical gate**: Adding S-0 (read TOPICS.md, emit status, carry tier) is what separates the 84 scorers from the 100 scorers. V-01 and V-02 have all the right logic *except* tier propagation -- fixing only S-0 would have brought both to 100.
2. **Register is not load-bearing once structure is anchored**: V-03 (step-labeled, structural) and V-04 (conversational, prose) both score 100. The conversational register in V-04 did not compromise correctness for any criterion.
3. **C-10 compliance override gap persists across all R1 variations**: No variation includes the explicit override rule (`REAL-REQUIRED (compliance-sensitive)` for scout-compliance/trace-permissions with compliance tags). This passes by default in R1's test scenario but is a latent correctness hole. A rubric v2 aspirational criterion that removes the default-pass interpretation would expose this.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["TOPICS.md as dedicated S-0 step with emit line is the structural gate: it resolves tier before flag computation and satisfies C-06; V-01 and V-02 score 84 without it", "Register (conversational vs structured) does not affect score once the TOPICS.md step is anchored -- V-03 and V-04 tie at 100 despite different styles", "C-10 compliance override is a latent gap in all R1 variations -- passes by default in Tier 1 no-tag scenarios but absent from flag computation; rubric v2 should remove the default-pass to surface this"]}
```
