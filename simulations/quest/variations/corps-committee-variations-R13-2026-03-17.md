Written to `simulations/quest/golden/corps-committee-variate-R13-2026-03-17.md`.

---

## Summary

| ID | Axis | Key structural addition |
|----|------|------------------------|
| V-01 | C-37 dual-enforcement (single) | **ROLE VOICE GUARD** table (Mech 2 for C-02) before Phase 3; **OWNERSHIP TALLY** after Action Items table (Mech 2 for C-04). Both mechanisms operate independently — remove one, the violation still signals from the other. |
| V-02 | C-38 FAILS syntax template (single) | **FAILS SYNTAX TEMPLATE** block before STEP 1 declares `FAILS [C-NN]: <description>` as the canonical required form. Missing `[C-NN]` is malformed, not suboptimal. All fill-rule FAILS entries reformatted to positional canonical form. |
| V-03 | C-39 REQUIRES: annotations (single) | **CO-DEPENDENCY PREAMBLE** table at start of STEP 2; `REQUIRES: C-35` annotation in PHASE-2-ENTER skeleton and immediately before TOKEN TRACE CONFIRMATION fill rules; `REQUIRES: [TIER SORT complete]` before INERTIA CONTINUITY BRIDGE affirmation check. |
| V-04 | V-01 + V-02 | ROLE VOICE GUARD + OWNERSHIP TALLY + canonical FAILS template. Dual-enforcement addresses correctness at simulation sites; FAILS template addresses annotation completeness at fill-rule sites — orthogonal levels, no interaction. |
| V-05 | V-01 + V-02 + V-03 | Full integration on R12 V-05 baseline. Only variation where all four new detection paths are simultaneously load-bearing. |

**Key design decision for C-37:** I split the two mechanisms by *type* — one structural sequence gate (TIER-N-SEQUENCE-COMMIT, ordering-dimension), one domain-scope declaration (ROLE VOICE GUARD, content-dimension). A voice can be in the right tier order but the wrong domain; ROLE VOICE GUARD catches what the tier gate cannot, and vice versa.
