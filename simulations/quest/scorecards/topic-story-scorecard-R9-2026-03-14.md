Now I have full context on all five variations. Let me score them.

---

# Scorecard — `topic-story` Round 9 (v9 Rubric, 33 Criteria)

**Skill**: `topic-story`
**Round**: 9
**Rubric**: `topic-story-rubric-v9-2026-03-14.md`
**New criteria**: C-31, C-32, C-33
**Date**: 2026-03-15

---

## Scoring Formula

- **Essential (C-01--C-07)**: 7 criteria. Gate. All must PASS. Collectively worth 90 pts.
- **Aspirational (C-08--C-33)**: 26 criteria sharing 10 pts. Each criterion = 10/26 ≈ 0.385 pts.
- **Total max**: 100.0
- **R8 baseline under v9 rubric**: 23/26 aspirational pass → 90 + (23 × 0.385) = 90 + 8.85 = 98.85

---

## C-01 through C-30: Inherited R8 Baseline

All five R9 variations inherit the full R8 baseline. Structural changes in R9 are confined to three locations: (a) the checklist design invariant block, (b) the field inventory table, and (c) the Section 4 header. No R9 variation alters sections 1--3, the checklist items, the failure mode table, or the essential four-section structure. All 30 criteria pass across all five variations.

| Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| C-01--C-07 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-08--C-30 (aspirational) | PASS (all 23) | PASS (all 23) | PASS (all 23) | PASS (all 23) | PASS (all 23) |

---

## New Criterion Evaluation: C-31, C-32, C-33

### C-31 — Checklist Design Invariant Is a Navigable Artifact Element with a Repair Operation

**Pass conditions**: (a) invariant expressed as a named heading block (scan anchor, not bold inline), AND (b) block names a prescribed repair operation formula -- quotable, not generic.

**V-01**: PASS.
The invariant appears as `### Checklist Design Invariant` with a `**Rule**:` line and an explicit `**Repair operation**:` block quoting `"Does [Section name] include the label \`**[field name]**:\`?"`. Both conditions satisfied: heading creates scan anchor; repair formula is quotable. C-31 fires cleanly.

**V-02**: FAIL.
Invariant is `**Checklist Design Invariant**` (bold text) followed by a blockquote. No heading-level element -- not a scan anchor. The blockquote contains repair intent ("must be rewritten as a structural presence check") but no prescribed formula. Same PARTIAL form as R8 V-01. C-31 does not fire.

**V-03**: FAIL.
The invariant is a single inline sentence: "**Checklist Invariant**: No item tests content quality; each item locates a label string or reports it missing." No heading. No repair formula. V-03 deliberately isolates C-32; C-31 is absent by design.

**V-04**: PASS.
Carries V-01's heading block verbatim: `### Checklist Design Invariant` with `**Rule**:` and `**Repair operation**:` formula. Identical to V-01 on this criterion. C-31 fires.

**V-05**: PASS.
Carries the same heading block as V-01 and V-04. `### Checklist Design Invariant` with `**Rule**:` and `**Repair operation**:` formula. C-31 fires.

---

### C-32 — Anti-Consolidation Constraint for Required Labeled Field Groups Is Stated at the Section Template Level

**Pass condition**: Section 4 contains an explicit anti-consolidation directive co-located with the three inertia fields -- visible at field-entry time, not only at checklist review time. Directive must name the violation form.

**V-01**: FAIL.
Section 4 opens with stance note and "Required labeled fields:" header -- no anti-consolidation directive before the field list. The constraint lives only in the checklist (items 10-12 verify separate fields). Author entering Section 4 sees no prohibition. C-32 does not fire.

**V-02**: FAIL.
Section 4 says "Required labeled fields (see inventory Structural Constraint column for consolidation rules):" -- a cross-reference to the inventory, not a co-located directive. The author must leave Section 4 to read the constraint. C-32 requires the directive to be co-located and visible at field-entry time; a pointer is not a directive. C-32 does not fire.

**V-03**: PASS.
Section 4 opens with an explicit `**Anti-consolidation directive**:` block before the field list: "The three inertia fields below are required as separate labeled entries. Do not consolidate `**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a single field. A consolidated `**Position delta**:` field or equivalent fails C-29 and fails this section directive." Names the violation form. Co-located with fields. C-32 fires.

**V-04**: PASS.
Section 4 opens with `**Anti-consolidation directive**:` block before the field list (same placement as V-03): "The three inertia fields below must appear as separate labeled entries. Do not consolidate... A consolidated `**Position delta**:` field or equivalent fails C-29 and fails this section template." Names the violation form. C-32 fires.

**V-05**: PASS.
Section 4 opens with `**Anti-consolidation directive**:` block before the field list, stating the prohibition and naming the violation form. Additionally, the Section 4 preamble instructs authors to cross-reference the inventory ("see inventory Structural Constraint column"). The directive is co-located and independently actionable. C-32 fires.

---

### C-33 — Anti-Consolidation Constraints for Required Labeled Field Groups Are Annotated in the Field Inventory

**Pass condition**: Field inventory table contains a Structural Constraint column (or equivalent) annotating that `**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` must not be consolidated. The inventory alone must be sufficient to audit consolidation violations without reading section templates or checklists.

**V-01**: FAIL.
Field inventory is a two-column table (Axis / Required labeled fields introduced). No structural constraint column. Anti-consolidation constraint is absent from the inventory. An audit procedure reading only the field table cannot determine which fields are subject to anti-consolidation rules. C-33 does not fire.

**V-02**: PASS.
Field inventory has a three-column table: Axis / Required labeled fields / Structural constraint. The inertia-framing axis row reads: "**Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). This constraint is auditable from this table alone without reading Section 4 or the checklist." The falsifiability axis row reads: "Independent -- each field separately verifiable; no anti-consolidation constraint applies." Both rows populated. The table alone is sufficient for consolidation audit. C-33 fires.

**V-03**: FAIL.
Field inventory is a two-column table (Axis / Fields). No structural constraint column. Same as V-01. C-33 does not fire.

**V-04**: FAIL.
Field inventory is a two-column table (Axis / Required labeled fields introduced). No structural constraint column. C-33 is deliberately absent from V-04. Does not fire.

**V-05**: PASS.
Field inventory has a three-column table identical to V-02's in structure. The inertia-framing axis row annotates: "**Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). Constraint is auditable from this table alone without reading Section 4 template or the checklist." Additionally, the checklist footer explicitly states that structural constraints for items 10-12 are registered in the inventory's Structural Constraint column. The inventory is the authoritative constraint source; Section 4 cross-references it rather than independently restate. C-33 fires.

---

## Per-Variation Criterion Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01--C-07 (essential, 7 criteria) | PASS | PASS | PASS | PASS | PASS |
| C-08--C-27 (aspirational, 20 criteria) | PASS | PASS | PASS | PASS | PASS |
| C-28 (checklist design invariant stated) | PASS | PASS | PASS | PASS | PASS |
| C-29 (required labeled fields for inertia) | PASS | PASS | PASS | PASS | PASS |
| C-30 (S4 disproof condition closure) | PASS | PASS | PASS | PASS | PASS |
| **C-31** (invariant as heading + repair formula) | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-32** (anti-consolidation in S4 template) | FAIL | FAIL | **PASS** | **PASS** | **PASS** |
| **C-33** (inventory constraint annotation) | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| **Aspirational criteria passing (of 26)** | 24 | 24 | 24 | 25 | 26 |

---

## Score Computation

| Variation | Essential (90 pts) | Aspirational (10 pts) | **Total** |
|-----------|-------------------|----------------------|-----------|
| V-01 | 90.00 | 24/26 × 10 = 9.23 | **99.23** |
| V-02 | 90.00 | 24/26 × 10 = 9.23 | **99.23** |
| V-03 | 90.00 | 24/26 × 10 = 9.23 | **99.23** |
| V-04 | 90.00 | 25/26 × 10 = 9.62 | **99.62** |
| V-05 | 90.00 | 26/26 × 10 = 10.00 | **100.00** |

---

## Ranking

1. **V-05** — 100.00 (C-31 + C-32 + C-33: full structural saturation)
2. **V-04** — 99.62 (C-31 + C-32: two-moment enforcement, no inventory annotation)
3. **V-01** — 99.23 (C-31 only: heading block + repair formula)
3. **V-02** — 99.23 (C-33 only: inventory as constraint registry)
3. **V-03** — 99.23 (C-32 only: section directive, lean register)

---

## Excellence Signals — V-05

V-05 is the first variation across all rounds to satisfy all 26 aspirational criteria simultaneously. Three structural properties distinguish it from V-04 (the next best):

**Signal 1 (C-33 PASS): Inventory promoted to authoritative constraint source**
V-05's field inventory carries the full anti-consolidation rule in the Structural Constraint column and explicitly states that the constraint is "auditable from this table alone without reading Section 4 template or the checklist." V-04 has the identical Section 4 directive (C-32 PASS) but its inventory is a two-column table with no constraint annotation -- C-33 fails because an audit procedure reading only the inventory cannot determine which fields are subject to anti-consolidation rules. V-05 converts the inventory from a field directory into a constraint registry: the inventory becomes the single authoritative source, and section template + checklist are downstream consumers of that authority.

**Signal 2 (C-32 + C-33 non-redundancy confirmed): Section directive and inventory annotation serve distinct audit procedures**
V-05 encodes the anti-consolidation rule in two locations -- the Section 4 directive (C-32) and the inventory Structural Constraint column (C-33) -- but they are not redundant. The Section 4 directive fires at write-time: it is the first block an author reads before entering inertia fields. The inventory annotation fires at audit-time: any reviewer with only the field table can identify a consolidation violation without opening section templates. V-05's architecture makes these two enforcement moments structurally independent. V-02 proves C-33 alone satisfies the inventory criterion; V-04 proves C-31 + C-32 satisfies the write-time enforcement. V-05 combines both without conflict -- confirming the non-redundancy claim stated in the variation hypothesis.

**Signal 3 (hub-and-spoke constraint architecture): Section 4 directive cross-references the inventory rather than independently restating**
V-05's Section 4 preamble says "Required labeled fields (see inventory Structural Constraint column for consolidation rules):" -- the section directive points to the inventory as authority rather than restating the rule. This creates a hub-and-spoke architecture: one authoritative statement (inventory Structural Constraint column) with one downstream reference (Section 4 cross-reference). Contrast V-03 and V-04, which state the anti-consolidation rule in Section 4 without any inventory annotation -- the inventory and section template are structurally disconnected and could silently diverge. V-05's design eliminates the divergence risk by making the section directive derive from the inventory rather than duplicate it.

---

## Patterns for R10 Criterion Candidates

From V-05 Signal 2 (non-redundancy) and Signal 3 (hub-and-spoke):

The inventory-as-authoritative-source pattern (C-33) combines with the section-directive-as-reference pattern (Signal 3) to suggest a fourth structural property not yet tested: does the Section 4 directive name the inventory as the authoritative source (cross-reference form) rather than independently restating the constraint (independent-restatement form)? V-05 uses cross-reference; V-03 and V-04 use independent restatement. V-02 has no section directive. A criterion firing on whether the section directive derives from the inventory (cross-reference) rather than duplicates it (restatement) would be the logical next layer -- making the hub-and-spoke architecture a required property, not just an observed excellence signal.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inventory promoted to authoritative constraint source: annotating anti-consolidation rules in the field inventory converts the inventory from a field directory into a constraint registry, enabling consolidation audits from the inventory alone without reading section templates or checklists", "Hub-and-spoke constraint architecture: section directive cross-references the inventory as the authoritative source rather than independently restating the rule, eliminating the risk of the two locations diverging"]}
```
