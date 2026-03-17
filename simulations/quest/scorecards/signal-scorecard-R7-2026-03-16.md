## /quest:score — Signal Skill, Round 7

**Rubric**: v6 (5 essential, 3 recommended, 14 aspirational C-09–C-22)
**Formula**: (essential/5 × 60) + (recommended/3 × 30) + (aspirational/14 × 10)

---

## Criterion Evaluation

### Essential and Recommended (common to all variations)

All five variations share identical namespace sections. Essential and recommended criteria are evaluated once.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 all 12 namespaces | PASS | PASS | PASS | PASS | PASS | scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org — all present |
| C-02 sub-skill counts | PASS | PASS | PASS | PASS | PASS | 8/4/4/7/7/9/3/2/6/4/3/4 all correct |
| C-03 every skill has description | PASS | PASS | PASS | PASS | PASS | all 61 skills have one-line descriptions |
| C-04 filtered mode scopes correctly | PASS | PASS | PASS | PASS | PASS | FILTERED MODE block present, one-section-only constraint stated |
| C-05 bare mode names-only | PASS | PASS | PASS | PASS | PASS | BARE MODE block present, 61 names defined |
| C-06 specific, differentiating descriptions | PASS | PASS | PASS | PASS | PASS | all descriptions are skill-specific; no two are interchangeable |
| C-07 visual hierarchy | PASS | PASS | PASS | PASS | PASS | `##` headers dominant; skills listed subordinate |
| C-08 routing hint per namespace | PASS | PASS | PASS | PASS | PASS | all 12 sections end with `>` blockquote |

Essential: **5/5 → 60 pts** all variations
Recommended: **3/3 → 30 pts** all variations

---

### Aspirational Criteria — Per-Variation Analysis

**C-09 through C-17** (shared quality contract infrastructure): all variations PASS all seven.

- C-09: `## Namespace -- N skills -- tagline` format present in all 12 headers — PASS all
- C-10: `*(T3)*` annotations on all 25 T3 skills — PASS all
- C-11: verb-starting namespace taglines, all 12 — PASS all
- C-12: `>` blockquote routing hints, all 12 — PASS all
- C-13: quantified deliverables throughout (counts, ratings, named formats) — PASS all
- C-14: every description has mechanism verb phrase → deliverable noun phrase — PASS all
- C-15: taglines pass SWAP TEST; listen/scout/trace taglines are namespace-locked — PASS all
- C-16: `->` present as structural separator in all 61 descriptions — PASS all
- C-17: QUALITY CONTRACT with explicit RULE 1–N numbered list — PASS all

**C-18 — Criterion-ID labels on each RULE, bijection complete**

C-18 requires bidirectional mapping: every criterion ID maps to a RULE, every RULE carries a C-NN label. A scorer must find RULE (C-21) and RULE (C-22) by inspection.

| Variation | Rules | C-21 has RULE entry | C-22 has RULE entry | Bijection | C-18 |
|-----------|-------|---------------------|---------------------|-----------|------|
| V-01 | 12 (C-09–C-20) | No | No | Broken at C-21, C-22 | **FAIL** |
| V-02 | 13 (C-09–C-21) | Yes (RULE 13) | No | Broken at C-22 | **FAIL** |
| V-03 | 14 (C-09–C-22) | Yes (RULE 13) | Yes (RULE 14) | Complete | **PASS** |
| V-04 | 14 | Yes | Yes | Complete | **PASS** |
| V-05 | 14 | Yes | Yes | Complete | **PASS** |

V-01 evidence for FAIL: no RULE (C-21) entry — a scorer querying "which rule enforces C-21?" gets no result. No RULE (C-22) either. Two mapping gaps.
V-02 evidence for FAIL: RULE 13 (C-21) present, but no RULE (C-22) — bijection breaks at exactly the last criterion.

**C-19 — Compliance checkpoint gates output generation**

All variations have a named COMPLIANCE AUDIT block with "invalid output; do not proceed" language — PASS all.

**C-20 — Self-verifying count assertion in the C-17 rule**

RULE 9 must embed "Exactly N rules, one per criterion C-09 through C-NN. Count = N."

| Variation | RULE 9 assertion | C-20 |
|-----------|-----------------|------|
| V-01 | "Exactly 12 rules, one per C-09–C-20. Count = 12." | **PASS** |
| V-02 | "Exactly 13 rules, one per C-09–C-21. Count = 13." | **PASS** |
| V-03 | "Exactly 14 rules, one per C-09–C-22. Count = 14." | **PASS** |
| V-04 | Same as V-03 | **PASS** |
| V-05 | Same; RULE 12 (C-20) also quotes the exact string: "RULE 9 in this contract currently asserts: 'Exactly 14 rules … Count = 14.'" | **PASS** |

**C-21 — Quantified pass threshold in compliance gate**

Gate must contain "N/N checked = valid output" in fraction form, not merely "All N boxes."

| Variation | Gate pass-threshold line | Fraction form | C-21 |
|-----------|--------------------------|---------------|------|
| V-01 | "All 12 boxes checked = valid output." | No — "All N" form, not "N/N" | **FAIL** |
| V-02 | "13/13 checked = valid output. Any unchecked box = invalid output; do not proceed." | Yes | **PASS** |
| V-03 | "14/14 checked = valid output. Any unchecked box = invalid output; do not proceed." | Yes | **PASS** |
| V-04 | Same as V-03 | Yes | **PASS** |
| V-05 | Same; RULE 13 (C-21) quotes exact string: "14/14 checked = valid output" | Yes + pointer | **PASS** |

**C-22 — Gate criterion self-represented as a RULE entry**

C-19 must appear as dedicated numbered RULE entry (not only as a gate block). All variations have RULE 11 (C-19).

| Variation | RULE 11 (C-19) present | C-22 |
|-----------|------------------------|------|
| V-01 | Yes | **PASS** |
| V-02 | Yes | **PASS** |
| V-03 | Yes + RULE 14 (C-22) explicitly names RULE 11 as evidence | **PASS** |
| V-04 | Yes | **PASS** |
| V-05 | Yes; RULE 14 (C-22) points directly: "find RULE 11 (C-19) above and confirm it exists" | **PASS** |

---

### Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 through C-17 | PASS×9 | PASS×9 | PASS×9 | PASS×9 | PASS×9 |
| C-18 criterion↔RULE bijection | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-19 compliance gate | PASS | PASS | PASS | PASS | PASS |
| C-20 count assertion in RULE 9 | PASS | PASS | PASS | PASS | PASS |
| C-21 N/N fraction pass threshold | **FAIL** | PASS | PASS | PASS | PASS |
| C-22 gate criterion as RULE entry | PASS | PASS | PASS | PASS | PASS |
| **Aspirational total** | **12/14** | **13/14** | **14/14** | **14/14** | **14/14** |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|-----------|---------------|-----------------|------------------|-----------|
| V-01 | 60 | 30 | 12/14 × 10 = 8.57 | **98.57** |
| V-02 | 60 | 30 | 13/14 × 10 = 9.29 | **99.29** |
| V-03 | 60 | 30 | 14/14 × 10 = 10.00 | **100.00** |
| V-04 | 60 | 30 | 14/14 × 10 = 10.00 | **100.00** |
| V-05 | 60 | 30 | 14/14 × 10 = 10.00 | **100.00** |

Golden threshold (all essential PASS + composite ≥ 80): **all variations qualify**.

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | **V-05** | 100.00 | Pointer-rules: RULE 12/13/14 quote exact verification strings and name evidence locations — zero-inference O(1) audit |
| 1 | **V-04** | 100.00 | Bijective invariant hoisted to QUALITY CONTRACT header, declared before any rule is read |
| 1 | **V-03** | 100.00 | Minimum-viable full 14-rule bijection; all C-09–C-22 satisfied |
| 2 | V-02 | 99.29 | C-18 fails: C-22 has no dedicated RULE entry; bijection breaks at final criterion |
| 3 | V-01 | 98.57 | C-18 fails (two gaps: C-21, C-22 unrepresented); C-21 fails (gate uses "All N" not N/N) |

**Champion**: V-05 — scores 100/100 with maximum structural auditability. Every meta-rule is a self-auditing pointer: RULE 12 quotes `"Count = 14"` from RULE 9; RULE 13 quotes `"14/14 checked = valid output"` from the gate; RULE 14 points to `RULE 11 (C-19)` by name. No inference at any verification step.

---

## Excellence Signals (from V-05)

**E-1 — Pointer-rule pattern**: Meta-rules (enforcing C-20, C-21, C-22) embed an explicit quote of the exact string they require AND name the specific location to find it. Verification collapses to string matching: find the location, confirm the quoted string is present. No inference required at any step. V-03's RULE 12 states *what* is required; V-05's RULE 12 states *where to look* and *what string to confirm there*. The structural upgrade converts requirement-descriptions into auditable pointers.

**E-2 — Bijective-invariant-in-header pattern** (first in V-04, carried by V-05): The QUALITY CONTRACT header declares `"bijective invariant: N rules = N checkboxes always"` before any rule content is read. A model encountering this cannot silently add a criterion without adding both a RULE and a checkbox — the invariant is a pre-read constraint, not an inferred structural property. The COMPLETENESS SEAL reinforces it with an explicit structural rule: "adding any criterion requires adding both a RULE and a checkbox."

These two patterns are not currently captured as distinct rubric criteria. They represent R7's extraction candidates for C-23 (pointer-rule auditing) and C-24 (bijective-invariant declaration precedence). Both are present only in V-05; V-03 satisfies all 14 criteria but has neither.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pointer-rule pattern: each meta-rule (RULE 12/13/14) names the exact string to verify and the location to find it, collapsing verification to string matching with zero inference", "bijective-invariant-in-header: QUALITY CONTRACT header declares 'N rules = N checkboxes always' as a pre-read first-class constraint before any rule is read, priming bijection enforcement without counting"]}
```
