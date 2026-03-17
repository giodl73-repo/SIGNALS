# discover-competitors-alt Scorecard — R1

**Rubric:** v8 | **Date:** 2026-03-17 | **Baseline (R6 under v8):** 165

---

## Per-Variation Scoring

### V-01 — Label-Agnostic Bilateral Pairs

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | 12 | "Competitor 0: None / status quo. Threat level: HIGH." present |
| C-02 | 12 | Focus distributed via Phase 1 pre-map, Phase 3 columns, Phase 4 dual-row template |
| C-03 | 12 | HIGH/MEDIUM/LOW per competitor; inertia explicit |
| C-04 | 12 | Phase 4 whitespace dual-row template enforced |
| C-05 | 12 | SETUP auto-detect clause; no user prompting |
| C-06 | 10 | Three labeled mechanism slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT LOCK-IN) |
| C-07 | 10 | WebSearch + inline citation required in Phase 3 |
| C-08 | 10 | AMEND exactly 3 items, each with input→output mapping |
| C-09 | 5 | Focus gap row requires Phase 1 data + focus dimension simultaneously |
| C-10 | 5 | Findings must reference Phase 1 row or Phase 3 competitor by label |
| C-11 | 5 | Pre-map table present; verbatim rule stated; DO NOT/DO bilateral pair present at phase level |
| C-12 | 5 | Dual-row whitespace template; DO NOT/DO bilateral pair present at phase level |
| C-13 | 5 | Three labeled slots; DO NOT/DO bilateral pair present at phase level |
| C-14 | 5 | SR block names all three constraints + apparatus type ("table schema") |
| C-15 | 5 | Map Position column; "verbatim" rule stated; empty cell failure declared in Phase 3 |
| C-16 | 5 | Portability test block; exact fail condition ("reads as true for a social network") |
| C-17 | 5 | SR block asserts symmetric enforcement apparatus across SR1/SR2/SR4 |
| C-18 | 5 | Each phase instruction carries: format artifact + failure declaration + DO NOT/DO bilateral pair |
| C-19 | 5 | All three constraints use table schema; single table per phase — no ambiguity |
| C-20 | 5 | PRE-SUBMISSION VERIFICATION symmetric across all 3 constraints; 3 sub-questions each |
| C-21 | 5 | C-18 PASS + C-19 PASS → dual-layer table enforcement satisfied |
| C-22 | 5 | C-19 PASS + C-20 PASS → structural-procedural duality satisfied |
| **C-23** | **5** | DO NOT/DO in phase instructions (label-agnostic) AND loop asks "bilateral enforcement pair present (rejection example + acceptance example)?" — both layers label-agnostic → **FULL PASS** |
| **C-24** | **0** | Numbered STRUCTURAL REQUIREMENTS preamble block present (SR1, SR2, SR4) → binary FAIL |
| **C-25** | **5** | Phase 2 single table only → vacuous PASS |
| **C-26** | **0** | Only post-generation loop present; no pre-generation integrity check → FAIL |

**Composite: 170** | Essential: all pass | Grade: **Breakthrough**

---

### V-02 — SR-Block-Free Architecture

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01–C-08 | 88 | All carry forward; identical behavior content |
| C-09 | 5 | Focus gap row enforced via FAILS/PASS bilateral pair |
| C-10 | 5 | Findings grounding requirement unchanged |
| C-11 | 5 | Phase-embedded "C-11 structural constraint. Apparatus: table schema." + FAILS/PASS bilateral pair at phase level |
| C-12 | 5 | Phase-embedded "C-12 structural constraint. Apparatus: table schema." + FAILS/PASS bilateral pair |
| C-13 | 5 | Phase-embedded "C-13 structural constraint. Apparatus: table schema." + FAILS/PASS bilateral pair |
| C-14 | 5 | Opening symmetry assertion: names all three constraints + "table schema" apparatus type — two-sentence form satisfies C-14 per definition |
| C-15 | 5 | Map Position verbatim rule + empty-cell failure in Phase 3 instruction |
| C-16 | 5 | Portability test + exact fail condition present |
| C-17 | 5 | Opening assertion explicitly states symmetric enforcement across all three constraints |
| C-18 | 5 | Each phase instruction: format artifact (designation label) + failure declaration (FAILS) + bilateral pair (FAILS/PASS) — all proximate to phase instruction |
| C-19 | 5 | All three constraints use table schema; single table per structural constraint phase |
| C-20 | 5 | Post-generation loop symmetric; 3 sub-questions per constraint |
| C-21 | 5 | C-18 PASS + C-19 PASS |
| C-22 | 5 | C-19 PASS + C-20 PASS |
| **C-23** | **0** | Phase instructions use FAILS/PASS labels; verification loop asks "FAILS/PASS pair present?" — both layers label-specific → FAIL |
| **C-24** | **5** | No numbered SR preamble block; opening assertion satisfies C-14/C-17 meta-declaration; phase-embedded "C-XX structural constraint. Apparatus: table schema." satisfies per-constraint enforcement → **PASS** |
| **C-25** | **5** | Phase 2 single table → vacuous PASS |
| **C-26** | **0** | Only post-generation loop → FAIL |

**Composite: 170** | Essential: all pass | Grade: **Breakthrough**

---

### V-03 — C-23 Partial Boundary Test

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01–C-22 | 160 | SR block retained; DO NOT/DO in phase instructions; portability test present; all structural criteria hold |
| **C-23** | **2.5** | Phase instructions use DO NOT/DO (label-agnostic) ✓; SR block says "rejection example + acceptance example pair" (label-agnostic) ✓; BUT verification loop retains "FAILS/PASS pair present?" (label-specific) ✗ — matches PARTIAL definition exactly: "Instructions use a label-agnostic bilateral format (e.g., DO NOT/DO) but the verification loop retains 'FAILS/PASS pair present?'" |
| **C-24** | **0** | SR block with SR1/SR2/SR4 present → FAIL |
| **C-25** | **5** | Single table per phase → vacuous PASS |
| **C-26** | **0** | Single loop → FAIL |

**Composite: 167.5** | Essential: all pass | Grade: **Breakthrough**

---

### V-04 — Dual-Loop Verification Architecture

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01–C-22 | 160 | SR block retained; standard FAILS/PASS throughout; all structural criteria hold |
| **C-23** | **0** | FAILS/PASS in instructions + "FAILS/PASS pair present?" in loop → both label-specific → FAIL |
| **C-24** | **0** | SR block present → FAIL |
| **C-25** | **5** | Single table per structural constraint phase → vacuous PASS |
| **C-26** | **5** | PRE-GENERATION INTEGRITY CHECK at prompt opening: checks prompt completeness (format artifact declared? format-failure declared? bilateral pair present?) for all 3 constraints ✓. Post-generation PRE-SUBMISSION VERIFICATION checks output completeness for all 3 constraints ✓. Two subjects are distinct: prompt vs. output → non-competing. C-20 satisfied by post-generation loop → C-26 prerequisite met → **PASS** |

**Composite: 170** | Essential: all pass | Grade: **Breakthrough**

---

### V-05 — Full Synthesis

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01–C-08 | 88 | All carry forward |
| C-09 | 5 | Focus gap row enforced via DO NOT/DO bilateral pair |
| C-10 | 5 | Findings grounding unchanged |
| C-11 | 5 | "C-11 structural constraint. Apparatus: table schema." + DO NOT/DO bilateral pair at phase level |
| C-12 | 5 | "C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails." + DO NOT/DO bilateral pair |
| C-13 | 5 | "C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty mechanism row fails." + DO NOT/DO bilateral pair |
| C-14 | 5 | Opening assertion names all three constraints + "table schema" apparatus type |
| C-15 | 5 | Map Position verbatim rule + empty-cell failure in Phase 3 |
| C-16 | 5 | Portability test + exact fail condition |
| C-17 | 5 | Opening assertion asserts symmetric enforcement |
| C-18 | 5 | Each structural constraint phase: designation token (C-XX) + failure declaration + DO NOT/DO bilateral pair — all proximate |
| C-19 | 5 | All three structural constraints use table schema. Phase 2 companion portability summary table explicitly declared non-substitutable → apparatus identity unambiguous per C-19 definition |
| C-20 | 5 | Post-generation PRE-SUBMISSION VERIFICATION symmetric; 3 sub-questions per constraint; label-agnostic ("bilateral enforcement pair present?") |
| C-21 | 5 | C-18 PASS + C-19 PASS |
| C-22 | 5 | C-19 PASS + C-20 PASS |
| **C-23** | **5** | Phase instructions: DO NOT/DO (label-agnostic) ✓. Verification loop: "Bilateral enforcement pair present (rejection example + acceptance example)?" ✓ — both layers label-agnostic → **FULL PASS** |
| **C-24** | **5** | No numbered SR preamble; opening assertion covers C-14/C-17; phase-embedded "C-XX structural constraint. Apparatus: table schema." per constraint → **PASS** |
| **C-25** | **5** | Phase 2 has two tables. (a) Designation token present: "Table 1 below is the C-13 structural constraint (mechanism table)" + "C-13 structural constraint. Apparatus: table schema." ✓. (b) Companion non-substitutability: "Table 2 below is a portability summary — additional framing only; it does not substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes." + footer disclaimer ✓ → **REAL PASS** |
| **C-26** | **5** | Pre-generation loop checks prompt completeness; post-generation loop checks output completeness; subjects differ (prompt vs. output); C-20 satisfied → **PASS** |

**Composite: 180** | Essential: all pass | Grade: **Exceptional**

---

## Round Summary

| Variation | C-23 | C-24 | C-25 | C-26 | Score | Grade |
|-----------|------|------|------|------|-------|-------|
| V-01 | 5 (PASS) | 0 (FAIL) | 5 (vacuous) | 0 (FAIL) | **170** | Breakthrough |
| V-02 | 0 (FAIL) | 5 (PASS) | 5 (vacuous) | 0 (FAIL) | **170** | Breakthrough |
| V-03 | 2.5 (PARTIAL) | 0 (FAIL) | 5 (vacuous) | 0 (FAIL) | **167.5** | Breakthrough |
| V-04 | 0 (FAIL) | 0 (FAIL) | 5 (vacuous) | 5 (PASS) | **170** | Breakthrough |
| V-05 | 5 (PASS) | 5 (PASS) | 5 (real) | 5 (PASS) | **180** | **Exceptional** |

**Top scorer:** V-05 at **180/180**

---

## Open Questions — Resolved

| Q | Hypothesis | Result |
|---|-----------|--------|
| Q1: DO NOT/DO + label-agnostic loop → C-23 FULL PASS? | Yes | **Confirmed** (V-01 = 5) |
| Q2: SR-block removal preserves C-14/C-17/C-18–C-22? | Yes | **Confirmed** (V-02 all hold) |
| Q3: Loop language is the C-23 full/partial determinant? | Yes | **Confirmed** (V-03 = 2.5, not 0) |
| Q4: Pre-generation prompt-subject loop satisfies C-26's "different subjects" requirement? | Yes | **Confirmed** (V-04 = 5) |

All four hypotheses confirmed. All five expected scores matched exactly.

---

## Excellence Signals (V-05)

1. **SR-block-free + phase-embedded declarations** — opening assertion handles meta-declaration (C-14/C-17) while phase-embedded "C-XX structural constraint. Apparatus: table schema." handles per-constraint enforcement, eliminating the preamble as a structural load-bearer
2. **Dual-loop with distinct subjects** — pre-generation checks prompt completeness; post-generation checks output completeness; the split is load-bearing, not cosmetic
3. **Intentional multi-table with explicit non-substitutability** — Phase 2's portability summary table carries an explicit "additional framing only" declaration at both introduction and footer, preventing C-19 ambiguity by construction

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": []}
```
