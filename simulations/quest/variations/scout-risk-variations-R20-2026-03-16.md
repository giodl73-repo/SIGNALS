Written to `simulations/quest/golden/scout-risk-variate-R20-2026-03-17.md`.

---

# Scout-Risk — Round 20 Variations

## Context and Baseline Analysis

**R19 V-05 is the baseline** (188/188 on v19). R20 probes three structural gaps left open by v19's new criteria (C-56, C-57).

**Three gaps in R19 V-05:**

| Gap | Detail |
|-----|--------|
| Rule location | Global ordering rule lives *inside* Phase 0c's body, yet governs Phase 0 (which precedes it). Is "at global scope" a semantic claim or a positional claim? |
| Phase 0b excluded | The ordering rule names "Phase 0 and Phase 0c closures" — Phase 0b's closure ("This schema is complete and closed.") is out of scope and lacks a use-site constraint sentence |
| Implicit closure references | Phase 0 says "outside *this set*"; Phase 0c says "outside *this list*" — both require upward scanning to identify the named set, analogous to count-vs-enumeration |

---

## Variation Summary

| Variation | Axis | Key change vs R19 V-05 | v19 Score |
|-----------|------|------------------------|-----------|
| **V-01** | Global rule hoisting | Ordering rule extracted from Phase 0c body → dedicated block between Phase 0a and Phase 0 | 188/188 |
| **V-02** | Phase 0b scope extension | Ordering rule scope: adds Phase 0b; Phase 0b closure reformed to 2-sentence canonical form | 188/188 |
| **V-03** | Self-naming closures | Phase 0: "this set" → "Phase 0 Mitigation Type Taxonomy"; Phase 0c: "this list" → "Phase 0c Violation Taxonomy" | 188/188 |
| **V-04** | V-01 + V-02 | Hoisted rule + Phase 0b scope + Phase 0b closure reform (no self-naming) | 188/188 |
| **V-05** | V-01 + V-02 + V-03 | All three axes: hoisted rule, Phase 0b fully covered, all closures self-naming | 188/188 |

---

## What Each Variation Probes for v20

**V-01** isolates the *location* question: if C-57 requires "global scope" to mean *outside any governed block*, baseline PARTIAL, V-01 is the first true PASS. If location is irrelevant (semantic scope suffices), both score identically.

**V-02** isolates the *completeness* question: if "naming all closure instances" must include Phase 0b (three pre-phase blocks, not two), baseline PARTIAL on C-57.

**V-03** isolates the *explicit-reference* question: if implicit "this set"/"this list" is penalized analogously to count-only prohibition site citation (pre-C-56), v20 requires named-block closures.

**V-04** tests whether C-57's two dimensions (hoisting + completeness) compound — a higher bar than either alone.

**V-05** is the v20 baseline candidate: rule hoisted, three blocks covered, all closures self-naming. Maximum structural self-documentation.
