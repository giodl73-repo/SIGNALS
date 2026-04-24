Looking at the R8 scorecard for new excellence signals:

- **Signal 1** (C-22 PASS confirmed for V-01/V-02 via embedded per-role sub-tables): First round to confirm the distributed-table path. Each per-role sub-table includes all four columns (Surface / This Role's Assessment / Upstream Role Assessment / Resolution). When conflict governance is distributed rather than centralized, the self-containment of each per-role table is load-bearing — a role specialist reading only their section must be able to determine the conflict and its resolution without cross-section traversal. → **C-28**.

- **Signal 2** (C-23 PASS for V-05 via opening governance rule): V-05 places both axis count (C-26) and judgment-elimination (C-23) in a single opening reconciliation rule. V-01–V-04 scatter these across the prompt: axis count in the opening, judgment-elimination in the resolution column. When both declarations are present but separated, a reviewer reading only the Conflict Analysis section may encounter the resolution mechanism without the judgment-elimination declaration and apply discretionary resolution believing the prompt permits it. Co-location forecloses that gap. → **C-29**.

Retroactive R8 scores under v8: V-04 and V-05 remain 100.00; V-03 drops to 99.47 (C-29 FAIL); V-02 drops to 99.47 (C-29 FAIL); V-01 drops to 98.95 (C-14 PARTIAL + C-19 PARTIAL + C-29 FAIL).

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 8
supersedes: org-pr-rubric-v7-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v7 -> v8)

Two new aspirational criteria extracted from R8 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=17 to N=19.

**C-28** (distributed conflict table completeness): V-01 and V-02 satisfy C-22 via
per-role sub-tables — each role block contains its own 4-column conflict table (Surface /
This Role's Assessment / Upstream Role Assessment / Resolution). This is the first round
to confirm the distributed-table path as a valid C-22 form. The per-role architecture
means a role specialist reading only their section sees the complete conflict picture: the
surface in dispute, both positions, and the resolution outcome. A table missing any of
these four fields forces cross-section traversal — the reviewer cannot determine the
resolution without leaving their role block, which increases the chance that the wrong
resolution rule is applied. V-03/V-04/V-05 use centralized Conflict Analysis sections and
do not raise this criterion. PASS if every per-role conflict sub-table includes all four
fields: (1) conflict surface or criterion identifier, (2) this role's position, (3) the
conflicting role's position or role identifier, (4) resolution outcome or resolution rule
reference. FAIL if any per-role table is missing one or more of these fields. N/A if
conflict governance is centralized rather than per-role (counts as PASS).

**C-29** (governance declaration co-location): V-05 places both the axis count declaration
(C-26: "two governance axes") and the judgment-elimination declaration (C-23: "no judgment
required") in a single opening reconciliation rule. V-01/V-02 declare axis count in the
opening but place judgment-elimination inside per-role sub-table resolution entries.
V-03 declares axis count in the opening but places judgment-elimination in the standalone
Conflict Analysis section's resolution column instruction. In both cases the declarations
are present but separated. Separation creates a reading-path vulnerability: a reviewer who
enters the Conflict Analysis section directly — or reads only the resolution column
template — encounters the mechanism without its characterization and may apply judgment
under the belief that the prompt does not prohibit it. Co-location eliminates this
vulnerability by making the complete governance model visible at the prompt's entry point,
before any operational content begins. PASS if the prompt includes a single preamble or
opening block that contains both the governance scope declaration (axis count or
equivalent) and the resolution mechanism's characterization (mechanical/non-judgment or
equivalent). FAIL if both declarations are present in the prompt but separated across
different structural locations without a cross-reference. N/A if only one of the two
declarations is present — no co-location requirement applies to a single-declaration prompt
(counts as PASS).

---

## Scoring Formula

Composite = Essential (max 60) + Recommended (max 30) + Aspirational (max 10).

Aspirational = (PASS_equiv / N_aspirational) × 10, rounded to 2 decimal places.

PASS_equiv weights: N/A → 1.0, PASS → 1.0, PARTIAL → 0.5, FAIL → 0.

---

## Scorecard — org-pr Round 5 (evaluated against v6 rubric)

**Rubric**: v6 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 15

See org-pr-rubric-v6-2026-03-16.md for the full R5 criterion grid and composite scores.
Preserved without re-evaluation; R5 scores are not retroactively updated under v8.

---

## Scorecard — org-pr Round 8 (evaluated against v8 rubric)

**Rubric**: v8 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 19

---

### Essential Criteria (60 pts / 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **60** | **60** | **60** | **60** | **60** |

All essential criteria pass in all five variations without exception.

---

### Recommended Criteria (30 pts / 6 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | PASS | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | PASS | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30** | **30** | **30** | **30** | **30** |

Evidence notes:

**C-07 all**: V-01/V-02 resolve conflicts through per-role inline sub-tables (conditional,
inline). V-03/V-04/V-05 use standalone Conflict Analysis sections. C-07 tests *presence*
of a resolution mechanism, not its form. PASS for all five.

**C-09 all**: All five include an explicit PRE-MERGE phase gate with halt instruction.
PASS for all five.

---

### Aspirational Criteria (10 pts, N=19)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PARTIAL | PASS | PASS | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A | N/A | N/A | N/A | N/A |
| C-19 Verdict hardening pair | PARTIAL | PASS | PASS | PASS | PASS |
| C-20 Priority table | N/A | N/A | N/A | N/A | N/A |
| C-21 Authority-inertia reconciliation rule | PASS | PASS | PASS | N/A | PASS |
| C-22 Conflict resolution column | PASS | PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | PASS | PASS | PASS | PASS | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | PASS | PASS | PASS | N/A | PASS |
| C-27 Priority axis non-redundancy | N/A | N/A | N/A | N/A | N/A |
| C-28 Distributed conflict table completeness | **PASS** | **PASS** | N/A | N/A | N/A |
| C-29 Governance declaration co-location | **FAIL** | **FAIL** | **FAIL** | N/A | **PASS** |

**All N/A entries count as PASS_equiv = 1.0.**

---

#### Composite Scores

| Variation | Essential | Recommended | PASS_equiv | Aspirational | **Total** |
|-----------|-----------|-------------|------------|--------------|-----------|
| V-01 | 60 | 30 | 17.0 / 19 | 8.95 | **98.95** |
| V-02 | 60 | 30 | 18.0 / 19 | 9.47 | **99.47** |
| V-03 | 60 | 30 | 18.0 / 19 | 9.47 | **99.47** |
| V-04 | 60 | 30 | 19.0 / 19 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 19.0 / 19 | 10.00 | **100.00** |

---

#### Evidence Notes — Contested and Notable Criteria

**C-14 V-01**: "There is no fourth outcome. Reclassify any P1 or accept No-Go." Names two
escape paths; does not include the exclusion statement "No other escape path exists."
PARTIAL (0.5). Caps C-19 at PARTIAL.

**C-14 V-02 through V-05**: "No other escape path exists. A P1 + Go claim is invalid under
this formula." Explicit exclusion statement present. PASS.

**C-18 all**: No priority table in any variation. N/A→PASS.

**C-20 all**: No priority table in any variation. N/A→PASS.

**C-21 V-01/V-02/V-03**: Opening declares "two governance axes: authority chain and inertia
framing" plus reconciliation rule. Inertia is a declared governance axis. PASS.

**C-21 V-04**: No axis declaration. Inertia is not a declared governance axis — the
If-Stays Projection column is a format feature only. No reconciliation rule present or
needed. N/A→PASS.

**C-21 V-05**: Opening declares two axes and includes "the conflict resolves mechanically
from the authority chain — no judgment required" as part of the reconciliation rule.
Inertia is a declared governance axis. PASS.

**C-22 V-01/V-02**: Per-role sub-tables with 4 columns (Surface / This Role's Assessment /
Upstream Role Assessment / Resolution) embedded within each role block. First round to
confirm the embedded-table path satisfies C-22. PASS.

**C-22 V-03/V-04/V-05**: Standalone Conflict Analysis section with 4-column table including
Resolution column. Consistent with all prior confirmed PASS forms.

**C-23 V-01/V-02**: Phrase "derived mechanically from the authority chain, no judgment
required" in the per-role sub-table resolution entry. PASS.

**C-23 V-03/V-04**: Phrase in standalone Conflict Analysis section resolution column
instruction. PASS.

**C-23 V-05**: Phrase "no judgment required" in the opening reconciliation rule alongside
the axis count declaration. PASS. Prompts may concentrate all governance declarations in
the opening rule without distributing them across resolution column instructions.

**C-25 all**: "Both must be satisfied simultaneously" present in V-01 through V-05.
V-02 through V-05 additionally include the mutual-dependency explanation. PASS for all.

**C-26 V-04**: No axis declaration. Single-axis prompt or no declaration present. N/A→PASS.

**C-27 all**: No priority table in any variation. N/A→PASS.

**C-28 V-01/V-02**: Per-role sub-tables confirmed to include all four fields: conflict
surface identifier, this role's position, upstream role's position, resolution rule.
Self-containment criterion satisfied. PASS.

**C-28 V-03/V-04/V-05**: Conflict governance is centralized (standalone Conflict Analysis
section). C-28 does not fire for centralized architectures. N/A→PASS.

**C-29 V-01/V-02**: Axis count declaration in the prompt opening; judgment-elimination
phrase in per-role sub-table resolution entries. Both declarations present but separated
across structural locations. No cross-reference between opening and per-role tables.
FAIL.

**C-29 V-03**: Axis count declaration in the prompt opening; judgment-elimination phrase in
the standalone Conflict Analysis section's resolution column instruction. Both declarations
present but separated. FAIL.

**C-29 V-04**: C-26 is N/A — no axis count declaration present. Only one governance
declaration (judgment-elimination) exists; no co-location requirement applies to a
single-declaration prompt. N/A→PASS.

**C-29 V-05**: Opening reconciliation rule contains both "two governance axes" (axis count)
and "no judgment required" (judgment-elimination) in the same block before any operational
content. Both declarations co-located at prompt entry point. PASS. First round to confirm
the opening-preamble path satisfies C-29.
```
