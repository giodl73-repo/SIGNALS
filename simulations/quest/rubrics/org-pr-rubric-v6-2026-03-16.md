Reading the R5 scorecard evidence carefully before writing new criteria.

**R5 excellence signals — V-05 deltas over V-01 through V-04:**

1. **C-22 enhanced** — V-05 adds "derived mechanically from the authority chain — no judgment required." Earlier variations have the resolution *column* (C-22 PASS) but leave resolution as implicitly judgment-based. The signal: declaring judgment-free derivation forecloses the soft-override path. → **C-23**

2. **C-12 mechanism** — V-05 names three invalid forms *each paired with a correction instruction*. V-01–V-04 fail C-12 entirely (no forms named). The signal: naming a form without its repair path leaves reviewers acknowledging invalidity but unable to self-correct. The three-part structure (label + violation description + correction instruction) is what distinguishes a catalog from a list. → **C-24**

3. **C-19 pass mechanism** — V-05 is first to name the C-11+C-14 co-occurrence as a structural unit ("Verdict Hardening Pair" section header). V-01–V-04 have C-11 present but C-14 PARTIAL and no pairing label. The signal: explicit co-occurrence labeling prevents half-implementations where one half is satisfied and the reviewer considers the requirement met. → **C-25**

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 6
supersedes: org-pr-rubric-v5-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v5 -> v6)

Three new aspirational criteria extracted from R5 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=12 to N=15.

**C-23** (judgment-elimination declaration): The conflict resolution mechanism in V-01
through V-04 specifies *who* governs (authority position) but leaves *how* as implicit —
an implicit invitation to argue that judgment should override the declared sequence. V-05
closes this by stating "derived mechanically from the authority chain — no judgment
required." The signal: when resolution is declared mechanical and non-judgmental, the
soft-override path (a reviewer arguing their interpretation should govern) is explicitly
foreclosed, not merely discouraged. PASS requires an explicit mechanical/non-judgment
statement paired with the resolution mechanism. FAIL if a resolution mechanism is present
without the declaration. N/A if no conflict resolution mechanism is present (counts as PASS).

**C-24** (correction-paired invalid form catalog): C-12 requires that invalid finding forms
be named. C-24 requires that each named form include a correction instruction — completing
the "error + repair" unit. Without the repair path, a reviewer who produces an invalid form
has no self-correction path and must infer the fix or leave the finding as-is. The R5 signal:
V-05 presents three named forms (untagged / no severity, revision / changing upstream
severity, aggregate / combining two surfaces), each with an explicit correction instruction.
PASS requires every named invalid form to have a paired correction instruction. PARTIAL if
some forms have correction instructions but others do not. N/A if no invalid forms are named
(counts as PASS; C-12 gates whether forms are named at all).

**C-25** (co-occurrence coupling label): C-19 tests whether C-11 and C-14 co-occur. C-25
tests whether their mutual dependency is *declared as a named structural unit* in the prompt.
Without the coupling label, a reviewer producing C-11 PASS and C-14 PARTIAL has no signal
that the pair is incomplete — partial implementation reads as progress. V-05 is the first
variation to introduce a "Verdict Hardening Pair" section header, making the co-occurrence
requirement explicit and the partial state visibly incomplete. PASS requires any pair of
mutually-dependent criteria to be declared as a named coupled unit (section header,
explicit pairing label, or equivalent). N/A if no co-occurrence dependencies are present
in the prompt (counts as PASS).

---

## Scoring Formula

Scorecard with excellence signals:

## Scorecard — org-pr Round 5 (evaluated against v6 rubric)

**Rubric**: v6 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 15

---

### Criterion-by-Criterion Grid

#### Essential Criteria (60 pts / 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **60** | **60** | **60** | **60** | **60** |

All essential pass in every variation.

---

#### Recommended Criteria (30 pts / 6 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | **FAIL** | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | **FAIL** | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **24** | **24** | **30** | **30** | **30** |

Evidence notes:
- **C-07 V-02**: No conflict analysis section at all. V-02 is a single-axis isolation (phase
  gate only); no conflict table → FAIL, not PARTIAL.
- **C-09 V-01**: No phase gate in V-01. Confirmed FAIL — this was the primary remaining gap
  after R4.
- **C-08 all**: Branch instruction present in every variation — "if invalid → rewrite →
  include" explicit in V-01 through V-05. Tightened pass condition satisfied.

---

#### Aspirational Criteria (10 pts / 0.667 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-13 Inertia / if-stays framing | FAIL | FAIL | FAIL | **PASS** | PASS |
| C-14 Verdict escape closure | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | **FAIL** | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | **FAIL** | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-19 Verdict hardening pair | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-21 Authority-inertia reconciliation rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-22 Conflict resolution column | PASS | N/A→PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | **FAIL** | N/A→PASS | **FAIL** | **FAIL** | **PASS** |
| C-24 Correction-paired invalid form catalog | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | **PASS** |
| C-25 Co-occurrence coupling label | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |

Evidence notes:

**C-12**: V-01 through V-04 have no named invalid forms. V-05 names three: untagged (no
severity), revision (changing upstream severity), and aggregate (combining two surfaces) —
each with correction instruction. First round to achieve PASS.

**C-13**: V-01 through V-03 have no if-stays column or instruction. V-04 and V-05 add the
"If-Stays Projection" column with "compounding cost" framing. PASS for V-04 and V-05.

**C-14**: V-01 through V-04 name the escape paths ("Reclassify any P1 or accept No-Go") and
state "No third outcome" — but none explicitly close by exclusion. The critical missing phrase
is "No other escape path exists." Without it, a novel escape claim is not explicitly
foreclosed. PARTIAL all four. V-05 adds: "No other escape path exists. A P1 + Go claim is
invalid under this formula." PASS.

**C-16**: V-02 has no pre-commit self-check section. All others include explicit numbered
pre-commit verification items.

**C-17**: V-02 has no Authority Chain section and no declared review order. V-01, V-03, V-04,
V-05 all declare Security (1) → UX (6) with authority rationale.

**C-18**: V-01, V-02, V-03 each have fewer than 3 competing governance axes (authority chain
is the primary axis, with supplemental structures that explicitly defer to it). N/A → PASS.
V-04 introduces an explicit 3-axis Axis Composition Table (authority chain / inertia framing
/ conflict resolution) with tiebreaker — PASS. V-05 extends to 8 axes with the same
structure — PASS.

**C-19**: Follows C-14. C-19 requires both C-11 and C-14 PASS simultaneously. C-11 PASS in
all variations. C-14 PARTIAL in V-01 through V-04 → C-19 PARTIAL. V-05 is the first to
explicitly name the pair as a unit ("Verdict Hardening Pair" section header) and achieve C-14
PASS → C-19 PASS.

**C-20**: V-01, V-02, V-03 all have fewer than 3 composition axes (phase gate excluded as a
pre-run guard, not a review-time governance axis). N/A → PASS. V-04 and V-05 both have 3+
explicit axes with priority tables — PASS.

**C-21**: V-01, V-02, V-03 have no inertia/if-stays axis — N/A → PASS. V-04 and V-05 both
include the explicit reconciliation declaration: "describes the compounding cost of the
upstream finding going unresolved — not a reclassification." PASS.

**C-22**: V-01, V-03, V-04, V-05 all have the Resolution column wired to authority-position
logic. V-02 has no conflict section → N/A → PASS.

**C-07 closure via C-22**: V-01, V-03, V-04, V-05 — all four seal C-07 PASS by providing a
Resolution column with explicit authority-position rule. V-05 adds the mechanical derivation
statement: "derived mechanically from the authority chain — no judgment required."

**C-23**: V-01, V-03, V-04 all have a resolution column (C-22 PASS) but include no statement
that derivation is mechanical or that judgment is not required → FAIL. V-02 has no conflict
resolution mechanism → N/A → PASS. V-05 adds "derived mechanically from the authority chain
— no judgment required" → PASS.

**C-24**: V-01 through V-04 name no invalid forms (C-12 FAIL for all four) → no named forms
to pair with correction instructions → N/A → PASS. V-05 names three forms, each with a
correction instruction (untagged: add P-level tag; revision: remove severity change, keep
surface finding; aggregate: split into two separate findings by surface) → PASS.

**C-25**: V-05 is the first variation to introduce "Verdict Hardening Pair" as an explicit
section header declaring the C-11 + C-14 co-occurrence as a named structural unit → PASS.
V-01, V-03, V-04 have C-11 present and C-14 relevant but no coupling label → FAIL. V-02
has neither a formula lock context nor an escape closure context in its single-axis design
→ FAIL (the co-occurrence dependency is absent in V-02's scope but C-25 tests labeling when
dependencies exist; V-02 has C-14 PARTIAL without a coupling label → FAIL).

---

#### Aspirational Score Summary

| Variation | Pass count (PARTIAL=0.5) | Aspirational pts |
|-----------|--------------------------|-----------------|
| V-01 | 10×1.0 + 2×0.5 + 3×0 = **11.0** | **7.33** |
| V-02 | 10×1.0 + 2×0.5 + 3×0 = **11.0** | **7.33** |
| V-03 | 10×1.0 + 2×0.5 + 3×0 = **11.0** | **7.33** |
| V-04 | 12×1.0 + 2×0.5 + 1×0 = **13.0** | **8.67** |
| V-05 | 15×1.0 + 0×0.5 + 0×0 = **15.0** | **10.00** |

Pass count detail:

- **V-01**: C-11, C-15, C-16, C-17, C-18, C-20, C-21, C-22, C-24 = 9 PASS +
  C-14 PARTIAL, C-19 PARTIAL = 2×0.5 + C-12, C-13, C-23, C-25 = 4 FAIL — wait,
  recounting: PASS: C-11, C-15, C-16, C-17, N/A→PASS C-18, N/A→PASS C-20,
  N/A→PASS C-21, C-22, N/A→PASS C-24 = 9×1.0; PARTIAL: C-14, C-19 = 2×0.5;
  FAIL: C-12, C-13, C-23, C-25 = 4×0 → **9.0 + 1.0 = 10.0** → 10.0 × (10/15) = **6.67**

- **V-02**: PASS: C-11, C-15, N/A→PASS C-18, N/A→PASS C-20, N/A→PASS C-21,
  N/A→PASS C-22, N/A→PASS C-23, N/A→PASS C-24 = 8×1.0; PARTIAL: C-14, C-19 = 2×0.5;
  FAIL: C-12, C-13, C-16, C-17, C-25 = 5×0 → **8.0 + 1.0 = 9.0** →
  9.0 × (10/15) = **6.00**

- **V-03**: PASS: C-11, C-15, C-16, C-17, N/A→PASS C-18, N/A→PASS C-20,
  N/A→PASS C-21, C-22, N/A→PASS C-24 = 9×1.0; PARTIAL: C-14, C-19 = 2×0.5;
  FAIL: C-12, C-13, C-23, C-25 = 4×0 → **9.0 + 1.0 = 10.0** →
  10.0 × (10/15) = **6.67**

- **V-04**: PASS: C-11, C-13, C-15, C-16, C-17, C-18, C-20, C-21, C-22,
  N/A→PASS C-24 = 10×1.0; PARTIAL: C-14, C-19 = 2×0.5;
  FAIL: C-12, C-23, C-25 = 3×0 → **10.0 + 1.0 = 11.0** →
  11.0 × (10/15) = **7.33**

- **V-05**: All 15 PASS (12 original + C-23 + C-24 + C-25) = 15×1.0 →
  15.0 × (10/15) = **10.00**

| Variation | Pass count (PARTIAL=0.5) | Aspirational pts |
|-----------|--------------------------|-----------------|
| V-01 | 10.0 / 15 | **6.67** |
| V-02 | 9.0 / 15 | **6.00** |
| V-03 | 10.0 / 15 | **6.67** |
| V-04 | 11.0 / 15 | **7.33** |
| V-05 | 15.0 / 15 | **10.00** |

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 24 | 6.67 | **90.67** |
| V-02 | 60 | 24 | 6.00 | **90.00** |
| V-03 | 60 | 30 | 6.67 | **96.67** |
| V-04 | 60 | 30 | 7.33 | **97.33** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

V-05 is the first variation to achieve a perfect composite score. V-04 holds second at
97.33, with the gap entirely attributable to C-23 (FAIL), C-25 (FAIL), and C-14/C-19
(PARTIAL → 1.0 vs 2.0 pts effective). V-02 scores lowest (90.00) due to the C-07 FAIL
from missing conflict analysis and the additional C-16, C-17 FAIL from missing authority
and pre-commit sections — all consequent on V-02's single-axis isolation design.

---

### Round Summary

All five variations satisfy the essential floor. The recommended spread (24 vs 30) is
now attributable entirely to V-01 (missing phase gate, C-09 FAIL) and V-02 (missing
conflict analysis, C-07 FAIL). The aspirational spread (6.00–10.00) shows a clear
complexity gradient: V-02 (single axis, no conflict section) → V-01/V-03 (multi-axis
without inertia) → V-04 (inertia + tables, no hardening pair declared) → V-05 (full
closure, named pairs, correction catalog, judgment-free resolution).

The three R6 hypotheses entered as C-23, C-24, C-25 are confirmed PASS in V-05. The
primary R6 investigation question: whether a prompt can achieve C-23 + C-25 *without*
requiring the full V-05 complexity (i.e., can judgment-elimination and coupling labels
appear in simpler single-axis designs, or do they only emerge naturally in 3+ axis
compositions).
```
