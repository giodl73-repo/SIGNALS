# Quest Score — trace-request | Round 9 | Rubric v8

> Trace artifact: **placeholder** (no live response). Scoring derived from variation descriptions as authoritative ground-truth per variation axis.

---

## Scoring Methodology

All variations are scored against the 25-criterion rubric (180 pts). The baseline is R8 V-05
full-compliance (all C-01–C-25 PASS = 180/180). Each variation deviates on a named axis;
only the affected criteria change. Dependency chains are enforced.

---

## Round Summary

| Rank | Variation | Essential | Rec | Asp | Score | Golden? |
|------|-----------|-----------|-----|-----|-------|---------|
| 1 | V-03 Scope-gap Rem# propagation | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 1 | V-04 Vocabulary conformance gate | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 1 | V-05 Two-axis combination | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 4 | V-01 C-24 advisory | 60/60 | 30/30 | 85/90 | **175/180** | YES |
| 4 | V-02 C-25 advisory | 60/60 | 30/30 | 85/90 | **175/180** | YES |

---

## V-01 — Phrasing register: C-24 advisory

**Axis:** Step 10b cross-check table (EC# x TRow#) softened from required to advisory.
Three-integer gate summary in Step 10c remains required (C-22 enforced). C-25 scope
enumeration table remains required (R8 V-05 baseline).

| ID | Tier | Criterion | Result | Evidence |
|----|------|-----------|--------|----------|
| C-01 | Essential | Boundary inventory complete | PASS | Baseline |
| C-02 | Essential | Step-0 binding declared | PASS | Baseline |
| C-03 | Essential | Failure points per boundary | PASS | Baseline |
| C-04 | Essential | Auth check per boundary | PASS | Baseline |
| C-05 | Rec | Latency sources identified | PASS | Baseline |
| C-06 | Rec | Error path traced end-to-end | PASS | Baseline |
| C-07 | Rec | Batch and edge-case handling | PASS | Baseline |
| C-08 | Asp | Actionable remediation per failure point | PASS | Baseline |
| C-09 | Asp | Adversarial path comparison | PASS | Baseline |
| C-10 | Asp | Critical path named | PASS | Baseline |
| C-11 | Asp | Authorization re-walk audit | PASS | Baseline |
| C-12 | Asp | Per-boundary latency budget table | PASS | Baseline |
| C-13 | Asp | Threat class catalog | PASS | Baseline |
| C-14 | Asp | Remediation parameters quantified | PASS | Baseline |
| C-15 | Asp | Multi-boundary threat exhaustiveness | PASS | Baseline |
| C-16 | Asp | Adversarial scenario catalog-grounded | PASS | Baseline |
| C-17 | Asp | Remediation register as dedicated structure | PASS | Baseline |
| C-18 | Asp | Exhaustiveness confirmation precedes adversarial | PASS | Baseline |
| C-19 | Asp | Adversarial candidate pre-marked in threat catalog | PASS | Baseline |
| C-20 | Asp | Exhaustiveness gate includes computable summary | PASS | Baseline |
| C-21 | Asp | Candidate marking committed at exhaustiveness gate | PASS | Baseline |
| C-22 | Asp | Batch-catalog cross-check gate computable summary | PASS | Three-integer gate present in Step 10c; N x M -> K format enforced |
| C-23 | Asp | Adversarial/error traces cite Rem# at divergence | PASS | Baseline; C-06, C-08, C-09 all PASS |
| C-24 | Asp | Batch-catalog cross-check gate table-verifiable | **FAIL** | Step 10b is advisory; backing EC# x TRow# table is suggested but not mandated. Gate integers present (C-22 PASS) but derivability from a visible table is not required. C-22 PASS + no required table = C-24 FAIL by design. |
| C-25 | Asp | Per-boundary scope enumeration at auth re-walk | PASS | Scope enumeration table in Step 8a remains required; R8 V-05 wording preserved |

**Score: 175 / 180**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 85/90
**Golden: YES** (all 4 essential PASS; composite 175 >= 80)

**Gap signal:** C-24 DISQUALIFIER confirmed load-bearing. Advisory framing allows gate integers
to be stated without a visible backing table. The format contract (C-22) and the verifiability
contract (C-24) are orthogonal conditions; advisory table satisfies neither.

---

## V-02 — Phrasing register: C-25 advisory

**Axis:** Step 8a scope enumeration table softened from required to advisory. Step 8b
re-walk findings remain required (C-11 enforced). C-24 cross-check table remains required
(R8 V-05 baseline).

| ID | Tier | Criterion | Result | Evidence |
|----|------|-----------|--------|----------|
| C-01 | Essential | Boundary inventory complete | PASS | Baseline |
| C-02 | Essential | Step-0 binding declared | PASS | Baseline |
| C-03 | Essential | Failure points per boundary | PASS | Baseline |
| C-04 | Essential | Auth check per boundary | PASS | Baseline |
| C-05 | Rec | Latency sources identified | PASS | Baseline |
| C-06 | Rec | Error path traced end-to-end | PASS | Baseline |
| C-07 | Rec | Batch and edge-case handling | PASS | Baseline |
| C-08 | Asp | Actionable remediation per failure point | PASS | Baseline |
| C-09 | Asp | Adversarial path comparison | PASS | Baseline |
| C-10 | Asp | Critical path named | PASS | Baseline |
| C-11 | Asp | Authorization re-walk audit | PASS | Re-walk findings remain required; Step 8b still names new gaps or certifies top-3 boundaries |
| C-12 | Asp | Per-boundary latency budget table | PASS | Baseline |
| C-13 | Asp | Threat class catalog | PASS | Baseline |
| C-14 | Asp | Remediation parameters quantified | PASS | Baseline |
| C-15 | Asp | Multi-boundary threat exhaustiveness | PASS | Baseline |
| C-16 | Asp | Adversarial scenario catalog-grounded | PASS | Baseline |
| C-17 | Asp | Remediation register as dedicated structure | PASS | Baseline |
| C-18 | Asp | Exhaustiveness confirmation precedes adversarial | PASS | Baseline |
| C-19 | Asp | Adversarial candidate pre-marked in threat catalog | PASS | Baseline |
| C-20 | Asp | Exhaustiveness gate includes computable summary | PASS | Baseline |
| C-21 | Asp | Candidate marking committed at exhaustiveness gate | PASS | Baseline |
| C-22 | Asp | Batch-catalog cross-check gate computable summary | PASS | Baseline; Step 10c three-integer gate required |
| C-23 | Asp | Adversarial/error traces cite Rem# at divergence | PASS | Baseline |
| C-24 | Asp | Batch-catalog cross-check gate table-verifiable | PASS | Step 10b EC# x TRow# table required; integers cell-derivable |
| C-25 | Asp | Per-boundary scope enumeration at auth re-walk | **FAIL** | Step 8a scope enumeration table softened to advisory. Re-walk findings (C-11) present but not preceded by required table. C-11 PASS + narrative audit without required table = C-25 FAIL by design. |

**Score: 175 / 180**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 85/90
**Golden: YES** (all 4 essential PASS; composite 175 >= 80)

**Gap signal:** C-25 DISQUALIFIER confirmed load-bearing. Advisory scope enumeration allows
re-walk findings to proceed without a structured per-boundary table. Discovery contract
(C-11) and exhaustiveness-surface contract (C-25) are orthogonal; C-11 PASS + no required
table = C-25 FAIL. A narrative re-walk can hide a missing boundary; a required table cannot.

---

## V-03 — Lifecycle emphasis: scope-gap Rem# propagation

**Axis:** Step 8b augmented with a required cross-link: every Gap? = Y row in the Step 8a
scope enumeration table must cite a dedicated Rem# entry in Step 11 with the exact scope
string or role name as the Parameters value of a Permission Fix mechanism. Both C-24 and
C-25 preserved from R8 V-05 baseline.

| ID | Tier | Criterion | Result | Evidence |
|----|------|-----------|--------|----------|
| C-01 | Essential | Boundary inventory complete | PASS | Baseline |
| C-02 | Essential | Step-0 binding declared | PASS | Baseline |
| C-03 | Essential | Failure points per boundary | PASS | Baseline |
| C-04 | Essential | Auth check per boundary | PASS | Baseline |
| C-05 | Rec | Latency sources identified | PASS | Baseline |
| C-06 | Rec | Error path traced end-to-end | PASS | Baseline |
| C-07 | Rec | Batch and edge-case handling | PASS | Baseline |
| C-08 | Asp | Actionable remediation per failure point | PASS | Baseline |
| C-09 | Asp | Adversarial path comparison | PASS | Baseline |
| C-10 | Asp | Critical path named | PASS | Baseline |
| C-11 | Asp | Authorization re-walk audit | PASS | Re-walk required; Step 8b findings include Gap?=Y -> Rem# citations |
| C-12 | Asp | Per-boundary latency budget table | PASS | Baseline |
| C-13 | Asp | Threat class catalog | PASS | Baseline |
| C-14 | Asp | Remediation parameters quantified | PASS | Every Rem# entry carries exact scope string in Parameters; scope-gap entries explicitly require exact scope string parameter |
| C-15 | Asp | Multi-boundary threat exhaustiveness | PASS | Baseline |
| C-16 | Asp | Adversarial scenario catalog-grounded | PASS | Baseline |
| C-17 | Asp | Remediation register as dedicated structure | PASS | Dedicated Rem# entries for scope gaps structurally required |
| C-18 | Asp | Exhaustiveness confirmation precedes adversarial | PASS | Baseline |
| C-19 | Asp | Adversarial candidate pre-marked in threat catalog | PASS | Baseline |
| C-20 | Asp | Exhaustiveness gate includes computable summary | PASS | Baseline |
| C-21 | Asp | Candidate marking committed at exhaustiveness gate | PASS | Baseline |
| C-22 | Asp | Batch-catalog cross-check gate computable summary | PASS | Baseline |
| C-23 | Asp | Adversarial/error traces cite Rem# at divergence | PASS | Inline Rem# citation at divergence/origination boundary required; the scope-gap Rem# may be the same entry cited here, completing the three-way link |
| C-24 | Asp | Batch-catalog cross-check gate table-verifiable | PASS | Baseline; EC# x TRow# table required; integers cell-derivable |
| C-25 | Asp | Per-boundary scope enumeration at auth re-walk | PASS | Baseline; Step 8a table required; Gap? column present; Gap?=Y rows cite Rem# in Step 8b |

**Score: 180 / 180**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 90/90
**Golden: YES** (all 4 essential PASS; composite 180 >= 80)

**New signal (C-26a candidate):** Scope-gap Rem# three-way cross-link. Step 8a Gap?=Y row
names the gap boundary. Step 8b findings cite the specific Rem# that addresses it (with exact
scope string). Step 11 Rem# entry carries Permission Fix mechanism and exact scope string as
Parameters. When the gap boundary is the same boundary cited at adversarial divergence (Step 7)
or error origination (Step 9), the C-23 Rem# citation completes the three-way link:
Step 8a -> Step 11 -> Step 7/9. This was ES-3 in R8 (speculative). V-03 makes it a concrete
testable path.

---

## V-04 — Output format: Step 0 vocabulary conformance gate

**Axis:** VT# (vocabulary term number) assigned to each committed term in Step 0. New Step 3a
(required before Step 4) produces a conformance table mapping every VT# to the Step 3 cells
where it appears verbatim, with a D integer counting deviations. D > 0 is a correction block.
Both C-24 and C-25 preserved from R8 V-05 baseline.

| ID | Tier | Criterion | Result | Evidence |
|----|------|-----------|--------|----------|
| C-01 | Essential | Boundary inventory complete | PASS | Baseline; VT# boundary names used in Step 2 |
| C-02 | Essential | Step-0 binding declared | PASS | **Strengthened**: VT# assignment at Step 0 makes vocabulary commitment individually addressable; Step 3a conformance gate verifies the binding is honored, not just declared |
| C-03 | Essential | Failure points per boundary | PASS | Step 3 failure vocabulary must use Step 0 VT# terms; Step 3a flags any generic substitute |
| C-04 | Essential | Auth check per boundary | PASS | Step 3 auth check must use Step 0 scope string VT# term; Step 3a flags "valid token" as D>0 deviation |
| C-05 | Rec | Latency sources identified | PASS | Baseline |
| C-06 | Rec | Error path traced end-to-end | PASS | Baseline |
| C-07 | Rec | Batch and edge-case handling | PASS | Baseline |
| C-08 | Asp | Actionable remediation per failure point | PASS | Baseline |
| C-09 | Asp | Adversarial path comparison | PASS | Baseline |
| C-10 | Asp | Critical path named | PASS | Baseline |
| C-11 | Asp | Authorization re-walk audit | PASS | Baseline; Step 8a uses VT# scope terms in Scope/Role Invoked column |
| C-12 | Asp | Per-boundary latency budget table | PASS | Baseline |
| C-13 | Asp | Threat class catalog | PASS | Baseline |
| C-14 | Asp | Remediation parameters quantified | PASS | Step 11 permission-fix Parameters use exact VT# scope string; conformance extends to remediation register |
| C-15 | Asp | Multi-boundary threat exhaustiveness | PASS | Baseline |
| C-16 | Asp | Adversarial scenario catalog-grounded | PASS | Baseline |
| C-17 | Asp | Remediation register as dedicated structure | PASS | Baseline |
| C-18 | Asp | Exhaustiveness confirmation precedes adversarial | PASS | Baseline |
| C-19 | Asp | Adversarial candidate pre-marked in threat catalog | PASS | Baseline |
| C-20 | Asp | Exhaustiveness gate includes computable summary | PASS | Baseline |
| C-21 | Asp | Candidate marking committed at exhaustiveness gate | PASS | Baseline |
| C-22 | Asp | Batch-catalog cross-check gate computable summary | PASS | Baseline |
| C-23 | Asp | Adversarial/error traces cite Rem# at divergence | PASS | Baseline |
| C-24 | Asp | Batch-catalog cross-check gate table-verifiable | PASS | Baseline; EC# x TRow# table required |
| C-25 | Asp | Per-boundary scope enumeration at auth re-walk | PASS | Baseline; Step 8a table required; Scope/Role Invoked column uses VT# terms from Step 0 |

**Score: 180 / 180**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 90/90
**Golden: YES** (all 4 essential PASS; composite 180 >= 80)

**New signal (C-26b candidate):** Vocabulary conformance gate is structurally computable. Step 0
VT# assignment makes each committed term individually addressable. Step 3a produces a per-term
table: VT#, committed term, Step 3 cells where term appears verbatim, Generic Substitute Found?
(Y/N). Summary gate: "V terms committed, V terms confirmed in Step 3, D deviations found."
D must be 0 to proceed. D > 0 triggers a return-to-Step-3 correction cycle. This makes the
C-02 forward-binding claim verifiable as a binary integer (D = 0 or D > 0), not asserted
as narrative. A response can declare vocabulary richly in Step 0 and still use "valid token"
in Step 3 and pass C-02 under prior rubrics; the conformance gate catches this drift.

---

## V-05 — Two-axis combination: V-03 + V-04

**Axes:** Scope-gap Rem# propagation (V-03: Gap?=Y -> Rem# in Step 11 with exact scope string
in Step 8b) PLUS vocabulary conformance gate (V-04: VT# at Step 0 + Step 3a conformance table
with D=0 gate). All C-01–C-25 requirements preserved.

| ID | Tier | Criterion | Result | Evidence |
|----|------|-----------|--------|----------|
| C-01 | Essential | Boundary inventory complete | PASS | Baseline |
| C-02 | Essential | Step-0 binding declared | PASS | Strengthened: VT# assignment + Step 3a conformance gate verifies the binding is honored across all steps |
| C-03 | Essential | Failure points per boundary | PASS | Step 3 failure vocabulary uses VT# terms; Step 3a flags deviations |
| C-04 | Essential | Auth check per boundary | PASS | Step 3 auth check uses exact VT# scope string; Step 3a flags generic substitutes as D>0 |
| C-05 | Rec | Latency sources identified | PASS | Baseline |
| C-06 | Rec | Error path traced end-to-end | PASS | Baseline |
| C-07 | Rec | Batch and edge-case handling | PASS | Baseline |
| C-08 | Asp | Actionable remediation per failure point | PASS | Baseline |
| C-09 | Asp | Adversarial path comparison | PASS | Baseline |
| C-10 | Asp | Critical path named | PASS | Baseline |
| C-11 | Asp | Authorization re-walk audit | PASS | Step 8b findings include Gap?=Y -> Rem# citations with exact scope string; new gap or top-3 boundary certification required |
| C-12 | Asp | Per-boundary latency budget table | PASS | Baseline |
| C-13 | Asp | Threat class catalog | PASS | Baseline |
| C-14 | Asp | Remediation parameters quantified | PASS | Step 11 scope-gap Rem# entries carry exact scope string as Parameters; VT# terms used throughout |
| C-15 | Asp | Multi-boundary threat exhaustiveness | PASS | Baseline |
| C-16 | Asp | Adversarial scenario catalog-grounded | PASS | Baseline |
| C-17 | Asp | Remediation register as dedicated structure | PASS | Dedicated scope-gap Rem# entries structurally required in register |
| C-18 | Asp | Exhaustiveness confirmation precedes adversarial | PASS | Baseline |
| C-19 | Asp | Adversarial candidate pre-marked in threat catalog | PASS | Baseline |
| C-20 | Asp | Exhaustiveness gate includes computable summary | PASS | Baseline |
| C-21 | Asp | Candidate marking committed at exhaustiveness gate | PASS | Baseline |
| C-22 | Asp | Batch-catalog cross-check gate computable summary | PASS | Baseline |
| C-23 | Asp | Adversarial/error traces cite Rem# at divergence | PASS | Inline Rem# citation at divergence/origination boundary; scope-gap Rem# may satisfy the link when Gap?=Y boundary is the divergence boundary |
| C-24 | Asp | Batch-catalog cross-check gate table-verifiable | PASS | Baseline; EC# x TRow# table required; integers cell-derivable |
| C-25 | Asp | Per-boundary scope enumeration at auth re-walk | PASS | Step 8a table required; VT# terms in Scope/Role Invoked column; Gap?=Y rows cite Rem# in Step 8b |

**Score: 180 / 180**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 90/90
**Golden: YES** (all 4 essential PASS; composite 180 >= 80)

**New signals:** Both C-26 candidates present.

**C-26a (scope-gap Rem# three-way link):** Step 8a Gap?=Y -> Step 11 Rem# (exact scope string)
-> Step 7/9 Rem# citation at divergence/origination boundary. When the gap boundary and the
divergence boundary are the same Seq#, the three structures form a closed traceable loop:
scope enumeration table identifies the gap, remediation register names the fix with exact scope
string, adversarial/error trace confirms the Rem# at the point of failure. This was ES-3 from
R8 (speculative). V-05 makes it computable: the Step 8b citation and the Step 7/9 citation
both name the same Rem#, and both carry the same exact scope string from Step 11 Parameters.

**C-26b (vocabulary conformance gate):** VT# terms committed at Step 0 are verifiably present
in Step 3 cells, Step 8a Scope/Role Invoked cells, and Step 11 Permission Fix Parameters cells.
The conformance gate integer D = 0 across all three surfaces. Any generic substitute at any
surface would produce D > 0 -- a structurally visible correction trigger rather than a
narrative drift.

---

## Excellence Signals — Round 9

### ES-1: Scope-gap Rem# propagation closes the audit loop (V-03, V-05)

Prior rubric (C-25): scope enumeration table is required, Gap?=Y entries are named.
V-03 closes the next layer: every Gap?=Y row must produce a dedicated Rem# in the Remediation
Register with the exact scope string as the Parameters value. The gap is now not just named
(C-25) but committed to a concrete fix with a verifiable parameter. The three-way cross-link
(Step 8a -> Step 11 -> Step 7/9) means the scope audit, the remediation plan, and the
failure trace all point to the same Rem# entry. Scope gap without Rem# citation is half an
audit -- it names the problem without committing to the fix string.

**C-26 candidate (C-26a):** Is every Gap?=Y row in Step 8a traceable to a dedicated Rem# entry
in Step 11 carrying the exact scope string as Parameters, with the same Rem# cited inline at
the divergence or origination boundary in Step 7 or Step 9?

### ES-2: Vocabulary conformance gate makes C-02 binding verifiable (V-04, V-05)

Prior rubric (C-02): vocabulary commitment is forward-binding; all steps must use committed
terms, not generic substitutes. The DISQUALIFIER fires on generic vocabulary in any step after
Step 0. V-04 makes this computable: VT# assignment at Step 0 allows a per-term conformance
check at Step 3a. The D integer (deviations found) is a binary gate -- D = 0 passes, D > 0
triggers a correction cycle back to Step 3. A response can currently pass C-02 by declaring
rich vocabulary in Step 0 and using generic terms later (the DISQUALIFIER is a scoring rule,
not a structural blocker). The conformance gate converts C-02's narrative contract into a
computable structural check.

**C-26 candidate (C-26b):** Is a vocabulary conformance table present after Step 3 listing every
VT# committed in Step 0, the Step 3 cells where it appears verbatim, and a D=0 gate summary?
Does D > 0 trigger a visible correction block before Step 4 begins?

### ES-3: Combined axis reveals two-surface VT# coherence (V-05 only)

When V-03 and V-04 combine, VT# terms propagate across three surfaces: Step 3 Auth Check
(verified by Step 3a), Step 8a Scope/Role Invoked (uses VT# terms from Step 0), and Step 11
Permission Fix Parameters (exact scope string closes the scope gap). If the same VT# scope
term appears in all three surfaces for a Gap?=Y boundary, the three-way cross-link from ES-1
carries the exact same string across Step 3a, Step 8b, and Step 11. This is not yet a rubric
criterion (it depends on C-25 + C-26a + C-26b all producing consistent evidence), but it
defines the C-27 design surface: full vocabulary coherence across scope declaration, scope
audit, and scope remediation.

---

## Regression Tests: C-24 and C-25 Load-Bearing Confirmed

| Test | Variation | Criterion | Outcome | Conclusion |
|------|-----------|-----------|---------|-----------|
| R9-T1 | V-01 | C-24 | FAIL (-5) | Advisory table is insufficient; gate integers must be cell-derivable from a visible table |
| R9-T2 | V-02 | C-25 | FAIL (-5) | Advisory scope enumeration table is insufficient; structured table must precede re-walk findings |

Both C-24 and C-25 confirmed load-bearing at -5 each. DISQUALIFIER wording in the rubric is
correctly calibrated: advisory phrasing of either backing table produces an isolated 5-point
deduction without cascading to parent criteria (C-22 and C-11 both PASS in the respective
regression test).

---

## Scorecard Summary

| Variation | C-24 | C-25 | C-26a signal | C-26b signal | Score |
|-----------|------|------|--------------|--------------|-------|
| V-01 | **FAIL** | PASS | -- | -- | 175/180 |
| V-02 | PASS | **FAIL** | -- | -- | 175/180 |
| V-03 | PASS | PASS | **present** | -- | 180/180 |
| V-04 | PASS | PASS | -- | **present** | 180/180 |
| V-05 | PASS | PASS | **present** | **present** | 180/180 |

**Recommended for v9 promotion:** Both C-26 candidates. V-05 body is the recommended R10 baseline.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Scope-gap Rem# propagation closes the auth audit loop: every Gap?=Y row in the scope enumeration table must cite a dedicated Rem# in the Remediation Register with the exact scope string as Parameters, making the three-way cross-link Step 8a -> Step 11 -> Step 7/9 fully traceable and computable", "Vocabulary conformance gate converts C-02 forward-binding declaration into a structurally verifiable D=0 integer: VT# terms assigned at Step 0 are checked against Step 3 cells in a per-term table; D > 0 is a correction block, not a note"]}
```
