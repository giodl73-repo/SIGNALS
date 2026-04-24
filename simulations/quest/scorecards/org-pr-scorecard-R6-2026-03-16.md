---

## Scorecard — org-pr Round 6

**Rubric**: v6 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 15

### Essential (all variations, all PASS — 60 pts)

All 5 essential criteria pass across all 5 variations.

### Recommended

| Variation | C-09 gap | Total |
|-----------|----------|-------|
| V-01 | FAIL (no phase gate — single-axis isolation) | **24** |
| V-02–V-05 | all PASS | **30** |

### Aspirational — criterion grid

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | P | P | P | P | P |
| C-12 Named invalid forms | F | F | F | P | P |
| C-13 Inertia / if-stays | F | F | F | P | P |
| C-14 Escape closure | PT | PT | PT | P | P |
| C-15 Projection convergence | P | P | P | P | P |
| C-16 Pre-commit self-check | P | P | P | P | P |
| C-17 Authority sequence | P | P | P | P | P |
| C-18 Axis conflict rule | N/A | N/A | N/A | P | N/A |
| C-19 Verdict hardening pair | PT | PT | PT | P | P |
| C-20 Priority table | N/A | N/A | N/A | P | N/A |
| C-21 Auth-inertia reconciliation | N/A | N/A | N/A | P | P |
| C-22 Conflict resolution column | P | P | P | P | P |
| **C-23** Judgment-elimination | **P** | F | **P** | **P** | **P** |
| **C-24** Correction-paired catalog | N/A | N/A | N/A | **P** | **P** |
| **C-25** Coupling label | F | **P** | **P** | **P** | **P** |

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 24 | 7.33 | **91.33** |
| V-02 | 60 | 30 | 7.33 | **97.33** |
| V-03 | 60 | 30 | 8.00 | **98.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

### Excellence Signals

1. **C-23 is complexity-independent** — a single phrase ("derived mechanically from the authority chain — no judgment required") in any conflict resolution column achieves C-23 PASS with zero structural preconditions. Confirmed in V-01 (no phase gate, no inertia, no table).

2. **C-25 is a labeling criterion, not a completeness criterion** — "Verdict Hardening Pair" header achieves C-25 PASS with C-14 still PARTIAL. Tests declaration of co-occurrence dependency, not whether both halves are closed.

3. **Embedded conflict resolution is the minimal 100/100 path** — V-05 keeps N=2 axes by embedding conflict resolution inside the Authority Chain section (not declaring it as a third axis). C-18/C-20 fire N/A→PASS; all structural elements still present. This is the minimum complete form across all 6 rounds.

4. **3-axis priority table is sufficient** — V-04 confirms the 8-axis design was over-engineered. Authority chain + inertia + conflict resolution in a 3-row table closes all 15 criteria.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-23 judgment-elimination is complexity-independent: a single phrase in any conflict resolution column achieves PASS with no structural preconditions — confirmed in a minimal design with no phase gate, inertia, or priority table", "C-25 is a labeling criterion independent of C-14 completeness: Verdict Hardening Pair header achieves PASS whether or not escape closure is present", "Embedded conflict resolution (inside the Authority Chain section, not as a third axis) is the minimal 100/100 path: N=2 keeps C-18/C-20 as N/A→PASS while all structural elements coexist", "3-axis priority table (authority chain + inertia + conflict resolution) is sufficient for 100/100 — the 8-axis design from R5 V-05 was over-engineered"]}
```
a minimal design with no
phase gate, no inertia, no coupling label. C-23 is purely a phrasing element.

**C-23 V-02 FAIL**: Resolution column reads "pos N governs per authority chain; pos M
assessment recorded as downstream risk on pos N's finding" — declares authority-position
governance but omits the mechanical/no-judgment statement. FAIL.

**C-23 V-03 PASS**: "pos N governs — derived mechanically from the authority chain, no
judgment required" in the resolution column. C-23 and C-25 compose independently: C-23
in the conflict table, C-25 in the verdict section header. No interference.

**C-25 V-01 FAIL**: Verdict formula is inline prose. No "Verdict Hardening Pair" section
header or equivalent coupling label. C-11 and C-14 are present but their co-occurrence
dependency is undeclared. FAIL.

**C-25 V-02 PASS**: "### Verdict Hardening Pair" section header explicitly declares C-11
and C-14 as a named structural unit. C-14 remains PARTIAL (no "No other escape path
exists") — C-25 tests labeling, not C-14 completeness. PASS confirmed independent of C-14.

**C-14 V-01/V-02/V-03 PARTIAL**: Each states "There is no third outcome / no fourth
outcome. Reclassify any P1 or accept No-Go." Names escape paths but does not add the
exclusion statement "No other escape path exists." Novel escape claims not explicitly
foreclosed. PARTIAL.

**C-14 V-04/V-05 PASS**: "No other escape path exists. A P1 + Go claim is invalid under
this formula." Explicit exclusion present. PASS.

**C-19 V-01/V-02/V-03 PARTIAL**: C-11 PASS but C-14 PARTIAL in all three. Co-occurrence
requirement not fully met. PARTIAL.

**C-18/C-20 V-05 N/A→PASS**: "This prompt operates under two governance axes." Conflict
resolution embedded inside the Authority Chain section — not declared as a third axis.
N=2 < 3 threshold. C-18 and C-20 are N/A→PASS. V-05 achieves 100/100 without triggering
these criteria as active requirements.

**C-21 V-05 PASS**: "Reconciliation rule: A later-authority role may add if-stays
projections... Those projections describe the compounding cost... not a reclassification."
Explicit reconciliation declaration present even though inertia is not a separate priority-
table axis. PASS.

**C-24 V-01/V-02/V-03 N/A→PASS**: C-12 FAIL in all three (no named invalid forms). C-24
tests whether named forms have correction instructions; if no forms are named, C-12 gates
the question and C-24 is N/A→PASS.

**C-24 V-04/V-05 PASS**: Three named forms each with correction instruction:
Untagged: "add P1/P2/P3 tag before including" | Revision: "record as if-stays projection
instead" | Aggregate: "split into separate rows". All three forms have repair paths. PASS.

---

### Aspirational Score Computation

| Variation | PASS | PARTIAL | FAIL | Effective count | Aspirational pts |
|-----------|------|---------|------|-----------------|-----------------|
| V-01 | 10.0 | 2 (×0.5) | 3 | **11.0 / 15** | **7.33** |
| V-02 | 10.0 | 2 (×0.5) | 3 | **11.0 / 15** | **7.33** |
| V-03 | 11.0 | 2 (×0.5) | 2 | **12.0 / 15** | **8.00** |
| V-04 | 15.0 | 0 | 0 | **15.0 / 15** | **10.00** |
| V-05 | 15.0 | 0 | 0 | **15.0 / 15** | **10.00** |

Pass detail:

**V-01**: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22, C-23,
C-24(N/A) = 10; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13, C-25 = 3×0

**V-02**: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22,
C-24(N/A), C-25 = 10; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13, C-23 = 3×0

**V-03**: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22, C-23,
C-24(N/A), C-25 = 11; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13 = 2×0

**V-04**: All 15 PASS (C-18 fires actively via 3-axis table; C-12/C-13/C-14/C-19/C-23/
C-24/C-25 all PASS). 15.0 / 15.

**V-05**: All 15 PASS (C-18/C-20 N/A→PASS via 2-axis design; C-21 PASS via embedded
reconciliation rule). 15.0 / 15.

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 24 | 7.33 | **91.33** |
| V-02 | 60 | 30 | 7.33 | **97.33** |
| V-03 | 60 | 30 | 8.00 | **98.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

**Top score**: 100.00 (V-04 and V-05 tied)
**All essential pass**: Yes (all variations)

---

## Excellence Signals — R6

R5 V-05 was already 100/100 against the v6 rubric. R6 investigates the minimal
complexity conditions under which C-23 and C-25 appear.

**Signal 1 — C-23 is complexity-independent.** V-01 achieves C-23 PASS in the
simplest design in the set: no phase gate, no inertia, no coupling label, no priority
table. The phrasing "derived mechanically from the authority chain — no judgment
required" is the entire mechanism. Any prompt with a conflict resolution column can
achieve C-23 PASS by adding this phrase. No structural preconditions.

**Signal 2 — C-25 is a labeling criterion, not a completeness criterion.** V-02
achieves C-25 PASS with C-14 PARTIAL. The "Verdict Hardening Pair" section header
declares the co-occurrence dependency; it does not require both halves to be fully
closed. C-25 tests whether the pair is named; C-19 tests whether both halves PASS.
The criteria are independent. A partial pair can be correctly labeled.

**Signal 3 — The two R6 phrasing additions compose without interference.** V-03
applies C-23 (in the conflict table) and C-25 (in the verdict section) at the same
complexity level without either requiring the other. They target different structural
sections and have no shared preconditions.

**Signal 4 — 3-axis priority table is the minimal 100/100 design with a table.** V-04
confirms that the 8-axis table from R5 V-05 is not required. Authority chain + inertia
+ conflict resolution in a 3-axis priority table, combined with the R6 phrasing additions
and C-14 escape closure, achieves 100/100. The 8-axis design was over-engineered.

**Signal 5 — Embedded conflict resolution is the minimal 100/100 design without a
table.** V-05 embeds conflict resolution in the Authority Chain section as a constraint
property of that axis, not as a third axis. N=2 keeps C-18 and C-20 N/A→PASS. All
structural elements (hardening pair, correction catalog, escape closure, reconciliation
rule, judgment-elimination) coexist in a 2-axis design. This is the minimum complete
form identified across all 6 rounds.

---

## R7 Direction

V-04 and V-05 both achieve 100/100 through different structural paths:
- V-04: 3-axis priority table (table present, C-18/C-20 fire as active criteria)
- V-05: 2-axis embedded (table absent, C-18/C-20 fire as N/A→PASS)

**R7 question**: Can C-12 and C-13 (named invalid forms + if-stays column) be added to
a V-03-level design (mid-complexity, no inertia axis, no priority table) without
triggering axis proliferation? If yes, the mid-complexity design would reach:
C-12 PASS, C-13 PASS, C-14 PARTIAL, C-23 PASS, C-25 PASS — only C-14/C-19 remaining
as PARTIAL. Closing those at V-03 complexity would establish whether V-05's 2-axis form
can be simplified further (e.g., removing the explicit Conflict Analysis section).
