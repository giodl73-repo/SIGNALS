Now I have everything needed. Let me score all 5 variations against the v8 rubric (C-01–C-33, 215 pts).

---

# Round 9 — topic-plan — Scorecard (v8 rubric)

## Scoring Reference

**Formula**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/25 × 125)`
**Partial** = 0.5 pass. **Golden threshold**: all essential pass + composite ≥ 125.

---

## Essential Criteria (C-01–C-05)

All five variations pass all essential criteria — strategy read, signals read, delta identified, proposals typed, confirmation gate present.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Read strategy | PASS | PASS | PASS | PASS | PASS |
| C-02 Read signals | PASS | PASS | PASS | PASS | PASS |
| C-03 Delta not inventory | PASS | PASS | PASS | PASS | PASS |
| C-04 Typed proposals | PASS | PASS | PASS | PASS | PASS |
| C-05 Confirm gate | PASS | PASS | PASS | PASS | PASS |

**Essential score: 5/5 → 60 pts for all variations.**

---

## Recommended Criteria (C-06–C-08)

All five variations pass all recommended criteria — evidence cited per change, before/after diff present, all three change types addressed with null rows.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Evidence per change | PASS | PASS | PASS | PASS | PASS |
| C-07 Before/after diff | PASS | PASS | PASS | PASS | PASS |
| C-08 All three change types | PASS | PASS | PASS | PASS | PASS |

**Recommended score: 3/3 → 30 pts for all variations.**

---

## Aspirational Criteria (C-09–C-33)

All evidence drawn from the Criterion Coverage Matrix in the variations document plus prompt text inspection.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Namespace coverage gaps | PASS | PASS | PASS | PASS | PASS |
| C-10 | Conflicting signals | PASS | PASS | PASS | PASS | PASS |
| C-11 | Typed confirmation verb | PASS | PASS | PASS | PASS | PASS |
| C-12 | Explicit no-change rows | PASS | PASS | PASS | PASS | PASS |
| C-13 | Inline evidence in diff | PASS | PASS | PASS | PASS | PASS |
| C-14 | Anti-inventory warning | PASS | PASS | PASS | PASS | PASS |
| C-15 | All 9 namespaces named | PASS | PASS | PASS | PASS | PASS |
| C-16 | Two-level traceability | PASS | PASS | PASS | PASS | PASS |
| C-17 | Explicit no-conflicts | PASS | PASS | PASS | PASS | PASS |
| C-18 | Structured delta format | PASS | PASS | PASS | PASS | PASS |
| C-19 | Diff Proposal ID column | PASS | PASS | PASS | PASS | PASS |
| C-20 | Delta Finding column | PASS | PASS | PASS | PASS | PASS |
| C-21 | Column-completeness declaration | PASS | PASS | PASS | PASS | PASS |
| C-22 | Active anti-pattern checkpoint | PASS | PASS | PASS | PASS | PASS |
| C-23 | Pre-reproduced null templates | PASS | PASS | PASS | PASS | PASS |
| C-24 | Unstated-assumption extraction | PASS | PASS | PASS | PASS | PASS |
| C-25 | Inertia cost "If unchanged" column | PASS | PASS | PASS | PASS | PASS |
| C-26 | Schema-first priming | PASS | PASS | **PARTIAL** | PASS | PASS |
| C-27 | Cascade checkpoints (3+) | **PARTIAL** | PASS | **PARTIAL** | **PARTIAL** | PASS |
| C-28 | Named role + scan dimensions | **PARTIAL** | **PARTIAL** | PASS | PASS | PASS |
| C-29 | Back-fill column | PASS | PASS | PASS | PASS | PASS |
| C-30 | Forward-reasoning columns | PASS | PASS | **FAIL** | PASS | PASS |
| C-31 | Decision-gate framing | **FAIL** | PASS | **FAIL** | PASS | PASS |
| C-32 | Reversibility taxonomy | PASS | **FAIL** | PASS | PASS | PASS |
| C-33 | Assumption table in upfront schema | **FAIL** | PASS | **FAIL** | PASS | PASS |

### Evidence notes

**C-26 V-03 PARTIAL**: V-03 omits the upfront schema block (intentionally, to isolate phrasing register); mandatory-column declarations appear per-table only. C-26 requires pre-reading consolidation.

**C-27**: V-01 has Steps 3+7 only (no Step 6 proposals commitment). V-02 has full Steps 3+6+7 — the Step 6 verbatim "Proposals schema committed..." statement is present. V-03 has Steps 3+7 only. V-04 explicitly designed to omit cascade checkpoints; Step 3 stop+name counts as one checkpoint. V-05 has full Steps 3+6+7 with the Step 6 verbatim block naming all three reversibility values.

**C-28**: V-01 has five scan dimensions (a–e) but no "Assumption Archaeologist" named role — PARTIAL. V-02 has no named role and no scan dimensions enumerated — PARTIAL. V-03, V-04, V-05 all use "Assumption Archaeologist" + scan dimensions (a-e or a-f).

**C-30 V-03 FAIL**: V-03 uses a 4-column assumption table (no "Why this matters" delta-relevance column, no "Delta candidate?" designation). The matrix confirms: "FAIL: no delta-relevance col, no delta-candidate col."

**C-31**: V-01 and V-03 have the "If unchanged" column but no adjacent disqualification sentence ("a preference, not a decision"). V-02, V-04, V-05 all carry the disqualification rule.

**C-32**: V-02 has a Reversibility column in the upfront schema but no closed enum and no prose prohibition — three-value enumeration absent. V-01 embeds the enum in the upfront schema Proposals row header with "select one; prose is not a valid value." V-03 uses decision-question [A/B/C] framing with "do not write prose." V-04 and V-05 use in-header enum.

**C-33**: V-01 has the upfront Assumption Table schema but with only four content columns (no "Implicit evidence" column — row key replaces it). V-03 has no upfront schema at all. V-02, V-04, V-05 declare the full five-column schema including "Implicit evidence" in the upfront block before Step 1.

---

## Aspirational Point Tallies

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 1 | 1 | 1 | 1 | 1 |
| C-10 | 1 | 1 | 1 | 1 | 1 |
| C-11 | 1 | 1 | 1 | 1 | 1 |
| C-12 | 1 | 1 | 1 | 1 | 1 |
| C-13 | 1 | 1 | 1 | 1 | 1 |
| C-14 | 1 | 1 | 1 | 1 | 1 |
| C-15 | 1 | 1 | 1 | 1 | 1 |
| C-16 | 1 | 1 | 1 | 1 | 1 |
| C-17 | 1 | 1 | 1 | 1 | 1 |
| C-18 | 1 | 1 | 1 | 1 | 1 |
| C-19 | 1 | 1 | 1 | 1 | 1 |
| C-20 | 1 | 1 | 1 | 1 | 1 |
| C-21 | 1 | 1 | 1 | 1 | 1 |
| C-22 | 1 | 1 | 1 | 1 | 1 |
| C-23 | 1 | 1 | 1 | 1 | 1 |
| C-24 | 1 | 1 | 1 | 1 | 1 |
| C-25 | 1 | 1 | 1 | 1 | 1 |
| C-26 | 1 | 1 | 0.5 | 1 | 1 |
| C-27 | 0.5 | 1 | 0.5 | 0.5 | 1 |
| C-28 | 0.5 | 0.5 | 1 | 1 | 1 |
| C-29 | 1 | 1 | 1 | 1 | 1 |
| C-30 | 1 | 1 | 0 | 1 | 1 |
| C-31 | 0 | 1 | 0 | 1 | 1 |
| C-32 | 1 | 0 | 1 | 1 | 1 |
| C-33 | 0 | 1 | 0 | 1 | 1 |
| **Subtotal** | **22** | **22.5** | **21** | **24.5** | **25** |
| **× 5 pts** | **110** | **112.5** | **105** | **122.5** | **125** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 60 | 30 | 110 | **200** | YES |
| V-02 | 60 | 30 | 112.5 | **202.5** | YES |
| V-03 | 60 | 30 | 105 | **195** | YES |
| V-04 | 60 | 30 | 122.5 | **212.5** | YES |
| V-05 | 60 | 30 | 125 | **215** | YES |

**All variations exceed the golden threshold (125).** Every variation passes all essential criteria.

---

## Ranking

1. **V-05 — 215 pts** (perfect score, all 25 aspirational pass)
2. **V-04 — 212.5 pts** (24.5/25 asp; gap: C-27 PARTIAL — no cascade checkpoints)
3. **V-02 — 202.5 pts** (22.5/25 asp; gaps: C-28 PARTIAL, C-32 FAIL)
4. **V-01 — 200 pts** (22/25 asp; gaps: C-27 PARTIAL, C-28 PARTIAL, C-31 FAIL, C-33 FAIL)
5. **V-03 — 195 pts** (21/25 asp; gaps: C-26 PARTIAL, C-27 PARTIAL, C-30 FAIL, C-31 FAIL, C-33 FAIL)

---

## Excellence Signals from V-05

### Pattern 1 — Implicit evidence as archaeology obligation, not column addition

V-05's Step 1b reframes extraction as a textual audit: *"An assumption with no strategy text implying it is an inference you imposed — leave 'Implicit evidence' blank only if no strategy text, however indirect, implies the assumption."* This is stronger than V-04's equivalent instruction ("leave blank only if no strategy text implies the assumption"). The "inference you imposed" framing eliminates brainstormed assumptions that the document never made — a quality filter, not just a provenance column.

### Pattern 2 — Named pre-reading commitments block as structural intent declaration

Before the Output Schema block, V-05 explicitly lists: *"Two pre-reading commitments are made here: 1. Assumption table schema... 2. Reversibility taxonomy..."* This makes the structural intent of the upfront block transparent. V-04 uses an identical schema but without naming why it must be read first. The naming converts the schema from a format block into a declared contract, which reduces the likelihood of a model treating the schema as reference rather than commitment.

### Pattern 3 — Revision gate framing for closed-enum classification

V-05's Step 6 commitment checkpoint says: *"a row that cannot select one of these three values has not reasoned about the deferral window and must be revised before this step is complete."* This is qualitatively different from V-01's "prose is not a valid value" (a formatting prohibition). V-05 names the failure mode (insufficient reasoning, not formatting error) and makes it a blocking condition (must be revised). The same adjacency principle that made C-31's "a preference, not a decision" framing effective is applied here to reversibility classification.

### Pattern 4 — Open scan dimension (f) extending the Archaeologist

V-05 adds "(f) Any additional dimension this specific strategy reveals" to the five fixed scan dimensions. V-01, V-02, and V-04 are bounded at five fixed dimensions. The open dimension allows the model to surface topic-specific assumptions that fall outside the fixed taxonomy — without sacrificing the structured coverage guarantee that fixed dimensions provide. This is an enumeration with an escape valve.

---

## Criterion Independence Confirmed

The single-axis isolations in R9 confirm the independence of C-32 and C-33:
- **V-01 (C-32 PASS, C-33 FAIL)**: Closed-enum enforcement works without the implicit evidence column — the reversibility column is structurally constrained even when assumption extraction lacks citation.
- **V-02 (C-32 FAIL, C-33 PASS)**: Implicit evidence column surfaces auditable assumptions without needing enum enforcement — the two criteria address non-overlapping gaps.
- **V-03 (C-32 PASS, C-33 FAIL, C-30 FAIL, C-31 FAIL)**: Decision-question framing passes C-32 but at the cost of losing the full assumption table lifecycle (C-30) and decision-gate framing (C-31) — the role-sequence base (V-03 uses R8 V-03) doesn't carry those mechanisms. C-32 is achievable via multiple framing registers; the mechanism choice has second-order effects on other criteria.

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["implicit evidence as archaeology obligation reframes extraction as textual audit not brainstorming — imposed inferences filtered by requiring strategy-text citation", "named pre-reading commitments block declares structural intent before schema reducing model risk of treating schema as reference rather than contract", "revision gate framing for closed-enum classification names insufficient reasoning as blocking condition not formatting error"]}
```
