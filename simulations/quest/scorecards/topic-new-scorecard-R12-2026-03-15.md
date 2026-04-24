# topic-new Scorecard — Round 12 (v11 rubric)

**Date**: 2026-03-15
**Rubric version**: v11 (C-01–C-38, aspirational denominator = 30)
**Variations scored**: V-01 through V-05

---

## Variation Summary

| Variation | Axis | ES signals |
|-----------|------|-----------|
| V-01 | Full priority-level vocabulary anchoring | ES-1 |
| V-02 | Consumer-to-decision-table traceability | ES-2 |
| V-03 | Recovery cost column | ES-3 |
| V-04 | Full vocabulary anchoring × consumer traceability | ES-1 + ES-2 |
| V-05 | Full vocabulary anchoring × consumer traceability × recovery cost | ES-1 + ES-2 + ES-3 |

R12 invariants (present in all five): C-35 (essential anchor), C-36 (F-05 Producer→Consumer),
C-37 (Handoff Artifact column), C-38 (team inertia default column).

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | TOPICS.md entry exists | PASS | PASS | PASS | PASS | PASS |
| C-02 | Strategy file at correct path | PASS | PASS | PASS | PASS | PASS |
| C-03 | All five signal fields present | PASS | PASS | PASS | PASS | PASS |
| C-04 | Priority values are valid | PASS | PASS | PASS | PASS | PASS |
| C-05 | At least one essential signal planned | PASS | PASS | PASS | PASS | PASS |

Evidence: All five variations write TOPICS.md via Phase 4, strategy.md at `simulations/{topic}/strategy.md`,
FIELD SCHEMA defines F-01 through F-05, Phase 2 enforces essential/recommended/optional vocabulary, Phase 3
commit gate requires ≥ 1 essential row.

**Essential: 5/5 for all variations.**

---

### Recommended Criteria (C-06–C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Signal set spans multiple namespaces | PASS | PASS | PASS | PASS | PASS |
| C-07 | Strategy includes a narrative rationale | PASS | PASS | PASS | PASS | PASS |
| C-08 | Owner roles are differentiated | PASS | PASS | PASS | PASS | PASS |

Evidence: F-02 Namespace enumerates 9 canonical namespaces; strategy.md template has ## Rationale section;
Phase 3 commit gate requires ≥ 2 distinct Consumer roles, enforcing role differentiation structurally.

**Recommended: 3/3 for all variations.**

---

### Aspirational Criteria (C-09–C-38)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Strategy defines a commit gate | PASS | PASS | PASS | PASS | PASS | Phase 3 is dedicated Commit Gate |
| C-10 | Signal item names follow artifact naming convention | PASS | PASS | PASS | PASS | PASS | F-04 = `{topic}-{signal}-{date}.md` |
| C-11 | Checkbox-gate before phase transition | PASS | PASS | PASS | PASS | PASS | Every phase boundary has explicit checkbox gate |
| C-12 | Invalid vocabulary framed as operational consequence | PASS | PASS | PASS | PASS | PASS | F-01 violation: "strategy fails C-04 and cannot serve as a commit gate" |
| C-13 | Each aspirational criterion has a dedicated section | PASS | PASS | PASS | PASS | PASS | Phase 3 dedicated to Commit Gate; F-04 dedicated schema row |
| C-14 | Consequence framing applied pervasively | PASS | PASS | PASS | PASS | PASS | Every FIELD SCHEMA row carries "If I Violate This, I Will..." column |
| C-15 | Prompt opens with stakeholder-risk enumeration | PASS | PASS | PASS | PASS | PASS | Phase 1 produces decision + stakeholder tables as first output before Phase 2; C-17 PASS implies C-15 PASS |
| C-16 | Every criterion enforced by structural mechanism | PASS | PASS | PASS | PASS | PASS | Schema fields, checkboxes, table columns, phase gates throughout; no prose-only constraint |
| C-17 | Stakeholder-risk section is active fill-in output | PASS | PASS | PASS | PASS | PASS | Phase 1 = required fill-in tables (decision + stakeholder) produced before signal planning |
| C-18 | Constraints partitioned into named schemas with consequence columns | FAIL | FAIL | FAIL | FAIL | FAIL | Only FIELD SCHEMA present; no COVERAGE SCHEMA; coverage constraints inline in phase gates |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | PASS | PASS | PASS | PASS | PASS | F-05 = Producer→Consumer; Consumer = stakeholder traceability; PASS+ for V-02/V-04/V-05 (Consumer must trace to decision table) |
| C-20 | Consequence columns are temporally layered | FAIL | FAIL | FAIL | FAIL | FAIL | FIELD SCHEMA consequence column is single-tier; recovery cost column (V-03/V-05) is in pipeline overview, not FIELD SCHEMA |
| C-21 | Per-phase exit gates at every phase boundary | PASS | PASS | PASS | PASS | PASS | Gates at Phases 0, 1, 2, 3, 4 |
| C-22 | Stakeholder fill-in table has quantified minimum row count gate | PASS | PASS | PASS | PASS | PASS | Phase 1 gate: "Decision table has at least 3 rows" + "Stakeholder table has at least 3 rows" |
| C-23 | Schema constraints carry row-level identifiers for gate citation | PASS | PASS | PASS | PASS | PASS | F-01 through F-05; gates cite [F-01], [F-05] by ID |
| C-24 | Pipeline declares all exit gates in summary table before phase content | PASS | PASS | PASS | PASS | PASS | PIPELINE OVERVIEW table with Exit Gate column precedes all phase content |
| C-25 | Commit Gate occupies a dedicated phase | PASS | PASS | PASS | PASS | PASS | Phase 3 = Commit Gate; Phase 2 = signal production; structurally separate |
| C-26 | Pipeline overview carries read-before-executing meta-instruction | PASS | PASS | PASS | PASS | PASS | "I will not execute Phase 0 until I have processed every row including [all] consequence columns" |
| C-27 | Schema row IDs cited at multiple independent gate boundaries | PASS | PASS | PASS | PASS | PASS | F-01 + F-05 cited at Phase 2 exit gate AND Phase 3 gate; V-02/V-04/V-05: F-05 cited twice at Phase 2 |
| C-28 | Fill-in table exit gate enforces column completeness independently of row count | PASS | PASS | PASS | PASS | PASS | Phase 1 gate: row count (≥3) AND cell completeness as separate checkboxes |
| C-29 | Pipeline overview carries per-row consequence column | PASS | PASS | PASS | PASS | PASS | "If I Skip This Phase, I Will..." column present |
| C-30 | Gate independence stated as explicit semantic instruction | PASS | PASS | PASS | PASS | PASS | "Check these N items independently" + "Do not advance until all checked independently" |
| C-31 | Priority column placed first in signal table column order | PASS | PASS | PASS | PASS | PASS | "Priority (F-01) | Namespace | Skill | Item Name | Producer → Consumer" |
| C-32 | Consequence column uses first-person framing | PASS | PASS | PASS | PASS | PASS | "If I Skip This Phase, I Will..." throughout |
| C-33 | Independence gate names specific sequential-treatment failure mode | PASS | PASS | PASS | PASS | PASS | Each gate carries "If I check these sequentially..." + named failure output |
| C-34 | Schema row order defines table column order | PASS | PASS | PASS | PASS | PASS | "Schema row order = table column order. F-01=Priority is column 1" explicit |
| C-35 | Priority schema row carries consumer-decision-dependency anchor | PASS | PASS | PASS | PASS | PASS | All have "essential = consumer cannot decide without this"; V-01/V-04/V-05 PASS+ (all three levels anchored) |
| C-36 | FIELD SCHEMA carries explicit Producer→Consumer role-relationship field | PASS | PASS | PASS | PASS | PASS | F-05 = Producer → Consumer in all variations |
| C-37 | Pipeline overview carries Handoff Artifact column | PASS | PASS | PASS | PASS | PASS | "Handoff Artifact" column present in all pipeline overviews |
| C-38 | Pipeline overview carries second consequence column naming team inertia default | PASS | PASS | PASS | PASS | PASS | "Team Default When I Skip This" column present in all variations |

**Aspirational PASS: 28/30 for all variations (C-18 and C-20 fail for all).**

---

## Notes on C-18 and C-20 Failures

**C-18** (COVERAGE SCHEMA): All R12 variations have FIELD SCHEMA but no named COVERAGE SCHEMA. Coverage
constraints (essential count, minimum row counts, role count) are embedded inline in phase exit gates,
citing FIELD SCHEMA IDs (F-01, F-05). The two-named-schema architecture is not present. This has been
a persistent FAIL since R7 and remains unfixed in R12.

**C-20** (Temporal tiers): FIELD SCHEMA consequence column uses single-tier framing ("If I Violate
This, I Will..."). V-03/V-05 add a Recovery Cost column to the pipeline overview — this provides
temporal separation at the overview level (immediate failure vs. late-detection rework), but C-20
specifies FIELD SCHEMA and COVERAGE SCHEMA consequence columns. Recovery Cost is in the pipeline
overview, not in FIELD SCHEMA.

---

## Composite Scores

**Scoring formula:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 30 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 | 3/3 | 28/30 | 99.33 |
| V-02 | 5/5 | 3/3 | 28/30 | 99.33 |
| V-03 | 5/5 | 3/3 | 28/30 | 99.33 |
| V-04 | 5/5 | 3/3 | 28/30 | 99.33 |
| V-05 | 5/5 | 3/3 | 28/30 | 99.33 |

**All five variations score identically on the v11 rubric.** This is the expected outcome when
the variation axes operate above the current rubric ceiling — the ES signals are excellence
patterns that the rubric does not yet capture.

---

## Variation Ranking (by excellence signal coverage)

| Rank | Variation | ES signals | Rationale |
|------|-----------|-----------|-----------|
| 1 | **V-05** | ES-1 + ES-2 + ES-3 | Full combination — all three independent failure axes closed |
| 2 | V-04 | ES-1 + ES-2 | Vocabulary anchoring + consumer traceability; closes fill-time and schema-time axes |
| 3 | V-01 | ES-1 | Full vocabulary anchoring — closes recommended/optional collapse vector |
| 3 | V-02 | ES-2 | Consumer traceability — closes F-05 consumer improvisation at fill time |
| 3 | V-03 | ES-3 | Recovery cost framing — closes skip-cost underestimation axis |

---

## Excellence Signals from V-05

### ES-1 — Full Priority-Level Vocabulary Anchoring

**What V-05 does**: FIELD SCHEMA carries a dedicated Decision-State Anchor column covering all
three priority levels:
- essential = cannot decide — blocked
- recommended = decides with risk — exposure accepted
- optional = decides unaffected — supplementary

**Why this exceeds C-35**: C-35 requires "essential = consumer cannot decide without this" —
anchoring only the top tier. The recommended/optional collapse failure mode persists: models
mark borderline signals as "recommended" because it sounds appropriately cautious without
checking whether the consumer's decision would proceed unaffected (optional). Full anchoring
makes substitution fail at all three tiers simultaneously — "high/medium/low" has no mapping
anywhere in the anchor column.

**Gap closed**: C-35 closes vocabulary-meaning enforcement for "essential" only. ES-1 closes
it for all three levels, making the entire priority vocabulary operationally closed at
schema-definition time.

**Candidate**: C-39 — Full vocabulary anchoring covers all three priority levels with
decision-state anchors, not only "essential."

---

### ES-2 — Consumer-to-Decision-Table Traceability Enforcement

**What V-05 does**: F-05 Consumer values must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. Phase 2 exit gate adds a third checkbox: "[F-05] Every Consumer value
appears verbatim as a Decision-Maker Role in Phase 1 decision table." Phase 3 commit gate
verifies the same condition on the ≥ 2 distinct consumer requirement.

**Why this exceeds C-36**: C-36 requires F-05 = Producer→Consumer in FIELD SCHEMA, making role
differentiation auditable by schema inspection. But if Consumer can be any role string, the field
is structurally present without operational constraint — a consumer role invented at fill time
("PM") may have no corresponding decision in the decision table. ES-2 creates mechanical
traceability from signal to decision at fill time. Priority assignment becomes verifiable by
inspection of the decision table: if the consumer's decision is not blocked by this signal, the
essential label is falsified by structural comparison, not only by rubric evaluation.

**Gap closed**: C-36 makes the Producer→Consumer relationship a schema-level structural constraint.
ES-2 makes every fill-time Consumer value traceable to an actual decision-maker, closing the orphaned-
consumer failure mode where F-05 is formatted correctly but points nowhere.

**Candidate**: C-40 — F-05 Consumer must trace to Phase 1 decision table; Phase 2 exit gate
verifies this explicitly as a third independent checkpoint.

---

### ES-3 — Recovery Cost Column

**What V-05 does**: Pipeline overview carries a third consequence column: "Recovery Cost When
Caught Late" — naming the concrete rework chain for each phase skip (e.g., "Re-run Phase 2
with traceable consumers, re-run Phase 3, re-write both output files").

**Why this exceeds C-38**: C-38 requires a second consequence column naming the team's inertia
default. Together with the first-person failure column (C-32), the pipeline overview carries two
orthogonal axes: what the executing model will produce incorrectly, and what the team defaults to.
Neither column names the concrete rework cost when the skip is discovered downstream. Models
evaluate costs in concrete operational terms more readily than in abstract failure-state terms. "I
will produce a strategy that fails C-04" is abstract. "Re-run Phase 2, re-run Phase 3, re-write
TOPICS.md and strategy.md" is a concrete rework chain. Recovery cost closes the third failure
axis: skip-cost underestimation.

**Gap closed**: C-38 closes the orthogonal axis where the team's default behavior continues even
when the model predicts individual failure correctly. ES-3 closes the axis where the model treats
a skip as low-cost because recovery cost is unnamed. These are three independent consequence axes:
individual failure mode, systemic team default, and concrete recovery cost.

**Candidate**: C-41 — Pipeline overview carries a third consequence column naming the rework
chain required when a phase skip is caught late.

---

## Persistent Gaps

**C-18 (COVERAGE SCHEMA)**: No R12 variation adds a named COVERAGE SCHEMA. The coverage constraints
remain embedded inline in phase gates. This is the highest-value unfixed gap — adding a COVERAGE SCHEMA
with row-level identifiers (COV-01 = essential count, COV-02 = namespace count, COV-03 = role count)
and consequence columns would satisfy C-18 and enable C-20. Candidate for a future R13 axis.

**C-20 (Temporal tiers)**: The Recovery Cost column (ES-3/V-03/V-05) provides a partial approach —
immediate failure vs. late-detection rework in the pipeline overview. But C-20 requires temporal tiers
in FIELD SCHEMA consequence columns. Extending temporal tiers to FIELD SCHEMA (Immediate violation /
Downstream cascade) would satisfy C-20. Candidate for R13 or R14 axis.

---

## Rubric Version Recommendation

**v12 rubric**: Promote ES-1, ES-2, ES-3 as candidates for C-39, C-40, C-41.
Aspirational denominator: 30 → 33.

| Candidate | Name | Sharpens |
|-----------|------|---------|
| C-39 | Full priority-level vocabulary anchoring — all three levels carry decision-state anchors | C-35 |
| C-40 | F-05 Consumer must trace to Phase 1 decision table; Phase 2 gate verifies | C-36 |
| C-41 | Pipeline overview carries third consequence column naming recovery cost when caught late | C-38 |
