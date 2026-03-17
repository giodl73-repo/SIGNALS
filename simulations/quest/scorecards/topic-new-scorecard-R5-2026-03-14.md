# Scorecard: topic-new — Round 5

**Rubric version**: v5
**Variations evaluated**: V-01, V-02, V-03 (V-04 and V-05 not provided in prompt)
**Date**: 2026-03-14

---

## V-01 — Stakeholder-Column as Primary Structural Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Phase 2 appends a structured row with topic, status, strategy path, and date |
| C-02 | Strategy at correct path | PASS | Phase 3 explicitly targets `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields present | PASS | Signal Plan table includes namespace, skill, item name, owner role, priority — plus Stakeholder Ref |
| C-04 | Priority values valid | PASS | FIELD SCHEMA row locks values to `essential` / `recommended` / `optional`; consequence columns state what breaks if violated |
| C-05 | At least one essential signal | PASS | Pre-write gate checklist item 2: "At least 1 planned signal will be marked `essential`" |
| C-06 | Multi-namespace coverage | PASS | COVERAGE SCHEMA threshold: ≥ 2 namespaces; checkbox gate verifies before write |
| C-07 | Narrative rationale | PASS | Section 3.1 Rationale required, ≥ 2 sentences |
| C-08 | Differentiated owner roles | PASS | COVERAGE SCHEMA requires ≥ 2 distinct S-N refs — role differentiation is auditable by column inspection, not aggregate counting |
| C-09 | Commit gate defined | PASS | Section 3.5 Commit Gate is a dedicated named section with explicit instruction to list item names |
| C-10 | Artifact naming convention | PASS | FIELD SCHEMA row enforces `{topic}-{signal}-{date}.md`; gate checklist item 6 re-verifies |
| C-11 | Checkbox gate before transition | PASS | 6-item pre-write checklist before Signal Plan table |
| C-12 | Invalid vocab framed as operational consequence | PASS | Priority row: "Strategy unparseable as a commit gate" + "Team proceeds to commit with no defined stopping condition" |
| C-13 | Each aspirational criterion has dedicated section | FAIL | Section 3.5 covers C-09 ✓; C-10 (item naming) lives as a FIELD SCHEMA row, not a dedicated section heading |
| C-14 | Consequence framing applied pervasively | PASS | Every field in FIELD SCHEMA carries Immediate Failure + Downstream Effect; COVERAGE SCHEMA identical |
| C-15 | Stakeholder-risk opener | PASS | Phase 1 "Stakeholders Table (First Output Required)" explicitly precedes signal planning |
| C-16 | Every criterion enforced structurally | PASS | Table columns, section headers, checkboxes, and named schemas enforce every criterion |
| C-17 | Stakeholder-risk section is active fill-in | PASS | Phase 1 is a required fill-in table, first output; signal rows must cite S-N from that table |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD SCHEMA + COVERAGE SCHEMA are named, each with Immediate Failure / Downstream Effect columns; gate checkboxes cite by schema row |
| C-19 | FIELD SCHEMA stakeholder traceability column | PASS | Dedicated Stakeholder Ref column; broken reference (citing absent S-N) and unauditable row (no citation) both named as FIELD SCHEMA violations |
| C-20 | Temporally layered consequence columns | PASS | Both schemas split every consequence into Immediate failure + Downstream effect |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 11/12 → 9.17
**Composite**: **99.17**
**Golden threshold met**: YES (all essential pass, composite ≥ 80)

---

## V-02 — Schema-First, Prose Minimized

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Output 1 appends structured row |
| C-02 | Strategy at correct path | PASS | Path `simulations/{topic}/strategy.md` explicit |
| C-03 | All five signal fields present | PASS | FIELD SCHEMA contains all five required fields plus Stakeholder Ref |
| C-04 | Priority values valid | PASS | FIELD SCHEMA row: `essential` / `recommended` / `optional`; consequence columns active |
| C-05 | At least one essential signal | PASS | COVERAGE SCHEMA threshold ≥ 1 essential; gate checklist item 2 enforces pre-write |
| C-06 | Multi-namespace coverage | PASS | COVERAGE SCHEMA threshold ≥ 2; gate checklist item 3 |
| C-07 | Narrative rationale | PASS | RATIONALE section required, 2+ sentences |
| C-08 | Differentiated owner roles | PASS | COVERAGE SCHEMA: ≥ 2 distinct S-N refs — structural inspection rather than counting |
| C-09 | Commit gate defined | PASS | COMMIT GATE named section with explicit instruction |
| C-10 | Artifact naming convention | PASS | FIELD SCHEMA row enforces pattern; gate checklist item 6 |
| C-11 | Checkbox gate before transition | PASS | 7-item GATE CHECKLIST before SIGNAL PLAN |
| C-12 | Invalid vocab framed as operational consequence | PASS | Priority row: "Strategy unparseable" + "No commit gate; investigation never closes" |
| C-13 | Each aspirational criterion has dedicated section | FAIL | COMMIT GATE is a named section (C-09 ✓); item naming (C-10) is a FIELD SCHEMA row only |
| C-14 | Consequence framing applied pervasively | PASS | Every row in both schemas carries Immediate Failure + Downstream Effect |
| C-15 | Stakeholder-risk opener | PASS | STAKEHOLDERS table is first section, marked "(fill as first step)" |
| C-16 | Every criterion enforced structurally | PASS | Pure schema enforcement — no criterion relies on prose alone |
| C-17 | Stakeholder-risk section is active fill-in | PASS | STAKEHOLDERS is a fill-in table as first step; Stakeholder Ref column enforces row-level traceability |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD SCHEMA and COVERAGE SCHEMA named, each with two-column consequences; gate checklist cites by reference |
| C-19 | FIELD SCHEMA stakeholder traceability column | PASS | Stakeholder Ref column citing S-N; both failure modes (broken ref, missing citation) named |
| C-20 | Temporally layered consequence columns | PASS | Immediate Failure + Downstream Effect across both schemas |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 11/12 → 9.17
**Composite**: **99.17**
**Golden threshold met**: YES

**V-02 note**: The prose-minimized format proves C-16's corollary — when structural mechanisms are complete, explanatory prose between schema sections is fully eliminable. V-02 removes the paragraph in V-01 that explains *why* column inspection is superior to aggregate counting, and compliance holds. This is a compression confirmation, not a new criterion.

---

## V-03 — Conversational Imperative Register (Incomplete)

V-03 contains only a title, variation description, and "Trace artifact (ground truth): placeholder." No prompt content is present.

| ID | Result | Note |
|----|--------|------|
| C-01–C-20 | FAIL | No evaluable content |

**Essential**: 0/5 → 0
**Recommended**: 0/3 → 0
**Aspirational**: 0/12 → 0
**Composite**: **0**
**Golden threshold met**: NO

---

## V-04, V-05

Not provided in this round's prompt input. Cannot be evaluated.

---

## Rankings

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 (tie) | V-01 | 99.17 | YES |
| 1 (tie) | V-02 | 99.17 | YES |
| 3 | V-03 | 0 | NO |

---

## Excellence Signals from R5

**V-01 and V-02 are structurally equivalent at the compliance level.** Both satisfy C-01–C-20 except C-13. The single persistent gap: item naming (C-10) has no dedicated section heading — it lives as a FIELD SCHEMA row, which is structurally sound but fails C-13's explicit requirement for a named section per aspirational criterion.

**V-02 confirms**: prose compression is safe. Explanatory paragraphs between schema rows (e.g., the V-01 paragraph explaining why S-N column inspection outperforms aggregate counting) can be removed without any compliance loss. Structure alone carries the requirement.

**No new patterns discovered in R5** that are not already captured in C-01–C-20. The two R4 excellence signals (C-19, C-20) are robustly satisfied by both top variations. The only remaining criterion gap (C-13 for item naming) is a known structural omission, not a new pattern type.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": []}
```
