Scorecard written to `simulations/quest/scorecards/scout-inertia-scorecard-R4-2026-03-17.md`.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-table inline column manifest: placing Required columns declaration immediately before each table converts column requirement into execution-site pre-commitment -- column omission detectable at declaration line not only at table header; column-level analog of C-17; C-18 candidate", "manifest redundancy creates reliability gradient orthogonal to score: all five score 100 but differ in adversarial robustness; score and structural enforcement strength are independent axes -- rubric captures pass/fail; reliability gradient captures how hard violation is to produce undetected"]}
```

---

## Summary

**All five variations: 100.00 / Gold.** R4 is fully closed.

The round differentiator is **reliability gradient, not score**. C-17 pass/fail is binary; structural enforcement strength is continuous. Ranked V-01 < V-02 < V-03 < V-04 < V-05 by how hard it is to violate the manifest without detection.

**Two new patterns extracted from V-05:**

1. **C-18 candidate — per-table inline column manifest**: V-05 adds `Required columns for this table:` immediately before Section C and D. This is the column-level analog of C-17: a pre-committed declaration at the execution site, making column omission detectable at the declaration line rather than only at the table header row. Neither C-16 (dedicated columns exist) nor C-17 (section-level manifest) captures this property. A v5 criterion would be: "Each tabular section opens with an explicit pre-committed column declaration."

2. **Manifest redundancy / reliability orthogonality**: Score and structural enforcement strength are independent axes. The rubric captures structural presence; reliability gradient captures how hard the structure is to violate without detection. A scoring system that treats all C-17 passes equally misses the V-01/V-05 difference. Design implication for future rubrics: reliability tiers may matter more than score tiers once a scaffold reaches 100.

**Convergence status**: V-05 is mature against rubric v4. If C-18 is added to v5, V-05 already satisfies it; V-01–V-03 would need one insertion. If C-18 is not added, the scaffold is fully converged.
-06 | Switching cost dimensions separate | PASS | Time / Training / Disruption as distinct table rows |
| C-07 | Threshold-based conditions | PASS | Observable Threshold column in Section D |
| C-08 | Long-term risk stated | PASS | Section E paragraph with explicit time horizon |
| C-09 | Severity ranked | PASS | Severity column in Section C; HIGH/MED/LOW defined |
| C-10 | Steelman rebutted | PASS | Two-pass structure (Advocate -> Analyst); Section F |
| C-11 | Verification method included | PASS | Verification Command column in Section D with format spec |
| C-12 | Rebuttal anchored to named claim | PASS | STRONGEST CLAIM -> NAMED CLAIM verbatim traceability chain |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard in STEP 1: named products, steps, tribal knowledge flagging |
| C-14 | Labeled analytical sections | PASS | Sections A-F with descriptive headings; reader can locate by scan |
| C-15 | Trigger/Impact decomposed | PASS | Separate Trigger and Impact content in Section C |
| C-16 | Dedicated Trigger/Impact columns | PASS | Trigger column and Impact column are distinct; blank Impact = automatic fail |

---

## Per-Variation C-17 Evaluation

### V-01 -- Bulleted Manifest Before Section A in STEP 2

**Mechanism**: Bulleted list block before `**A. Switching Cost Table**`:

```
Required sections manifest -- all must appear as headings in the final artifact,
in this order, with these exact labels...
- A. Switching Cost Table  - B. Threat Score  - C. Failure Mode Table
- D. Why Inertia Loses  - E. Long-Term Risk of Staying  - F. Anchored Rebuttal
```

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-17 | Synthesis heading manifest | PASS | Bulleted pre-committed list appears before Section A content; a reader can verify section coverage against the list without scanning the body |

**Reliability note**: Weakest form. No explicit fail condition named. Bullets could be
treated as decorative context; structural contract enforceability is lowest of five.

---

### V-02 -- Numbered Backtick Manifest Before Section A in STEP 2

**Mechanism**: Numbered list with backtick-formatted headings + explicit fail condition:

```
1. `## A. Switching Cost Table`  ...  6. `## F. Anchored Rebuttal`
Fail condition: role labels as section headings; prose summary replacing named sections;
any two adjacent components merged under one heading.
```

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-17 | Synthesis heading manifest | PASS | Numbered checklist with backtick heading text; explicit fail condition names violation patterns; structurally stronger than V-01 bullets |

**Reliability note**: Strongest step-local form. Fail conditions convert the manifest from
advisory to contractual. Numbered format enables tick-off verification.

---

### V-03 -- Global Preamble Manifest Before STEP 1

**Mechanism**: Standalone `### Structural Manifest` section before `## Inertia Analysis` and STEP 1.
STEP 2 back-references: "Use the section headings declared in the Structural Manifest above."

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-17 | Synthesis heading manifest | PASS | Manifest declared before any content generation step begins; back-referenced at STEP 2 execution site; "manifest violation is an analysis failure" explicit |

**Reliability note**: Most structurally non-skippable single-mechanism form. Global preamble
precedes STEP 1; a model must read past it before generating any output. STEP 2 back-reference
creates traceability between declaration site and execution site.

---

### V-04 -- Combined Section + Column Manifest Table at STEP 2 Header

**Mechanism**: Manifest table listing section name, required heading (exact backtick), and
required columns for tabular sections -- before Section A content. Plus explicit violation
conditions block.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-17 | Synthesis heading manifest | PASS | Manifest table is an explicit structural contract before Section A; each row is a compliance requirement; violation conditions named |

**C-16 bonus**: V-04 pre-declares required columns for Sections C and D in the manifest block.
A missing Impact column is detectable at the manifest declaration site AND at the table column
header. Two detection sites vs one.

**Reliability note**: Most information-dense single-declaration form. A reader can audit both
section coverage AND column coverage from the manifest table alone.

---

### V-05 -- Triple-Layer: Global Preamble + STEP 2 Numbered List + Inline Column Manifests

**Mechanism**: Three independent manifest declarations:
1. **Global Structural Manifest** (before STEP 1): All 7 sections + required columns for C and D
2. **STEP 2 numbered list** (at STEP 2 header): Repeats the 6 section headings 1-6
3. **Inline per-table declarations**: `Required columns for this table:` immediately before each table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-17 | Synthesis heading manifest | PASS | Triple-layer: global preamble + STEP 2 numbered list + per-table inline; manifest declared at three independent locations; C-17 violation structurally impossible |

**C-16 bonus**: Inline `Required columns for this table:` declarations before Section C and D
make column pre-commitment visible at the execution site. Column omission detectable at
declaration line, not only at table column header. Three detection sites for C-16 violations.

**Reliability note**: Maximum structural pre-commitment. C-17 cannot be violated without
the violation being visible at three independent locations simultaneously.

---

## Composite Scores

**Formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/9 * 10)`

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|-------------|-----------|------|
| V-01 | 5/5 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | Gold |
| V-02 | 5/5 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | Gold |
| V-03 | 5/5 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | Gold |
| V-04 | 5/5 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | Gold |
| V-05 | 5/5 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | Gold |

---

## Variation Rankings

All five clear gold. Ranked by reliability gradient (how hard it is to violate C-17
without detection):

| Rank | Variation | Score | Reliability tier |
|------|-----------|-------|-----------------|
| 1 | V-05 | 100.00 | Triple-layer; C-17 structurally non-skippable; 3 detection sites per violation |
| 2 | V-04 | 100.00 | Section + column manifest table; 2 detection sites per C-16 violation |
| 3 | V-03 | 100.00 | Global preamble + STEP 2 back-reference; precedes STEP 1 |
| 4 | V-02 | 100.00 | Numbered backtick + explicit fail conditions; strongest step-local form |
| 5 | V-01 | 100.00 | Bulleted list; minimum-form C-17 pass |

Reliability gradient: V-01 < V-02 < V-03 < V-04 < V-05

---

## Excellence Signals

### Signal 1 -- Per-table inline column manifest (C-18 candidate)

V-05 places `Required columns for this table: # | Failure Mode | Trigger | Impact | Severity`
immediately before each table section. This converts the column requirement from an implicit
template property (visible only at the table header row) into an explicit pre-commitment at
the execution site. If Section C's Trigger or Impact column is missing or merged, the violation
is detectable at the `Required columns:` declaration line, not only at the column header.

This is structurally distinct from:
- C-16 (requires dedicated columns in the table -- structural presence, not pre-committed declaration)
- C-17 (requires section-level manifest -- section pre-commitment, not per-table column pre-commitment)

**Pattern**: Pre-committing column requirements at the table's execution site is the column-level
analog of C-17. A v5 criterion could read: "Each tabular section opens with an explicit
pre-committed declaration of required column names immediately before the table."

### Signal 2 -- Manifest redundancy creates reliability gradient orthogonal to score

All five score 100/100, yet compliance robustness differs significantly. Score and structural
enforcement strength are independent axes: the rubric captures pass/fail; the reliability
gradient captures adversarial robustness. A future rubric could operationalize "manifest
reinforced at the execution site" as distinct from "manifest declared globally once."

### Signal 3 -- V-04's manifest table is the maximal single-declaration form

V-04 achieves section manifest (C-17) and column pre-commitment (C-16 reliability) from a
single manifest table. A reader can audit both section and column coverage from one block
without entering any section content. Alternative to V-05's inline-per-table approach: one
declaration vs three, same coverage. Valuable when prompt compactness matters.

---

## R4 Convergence Assessment

Round delta = 1 mechanism (C-17 manifest). Pattern:

| Round | Delta | Mechanism |
|-------|-------|-----------|
| R1 -> R2 | 3 | Replication Fidelity, Verification Command, STRONGEST/NAMED CLAIM |
| R2 -> R3 | 1 | Impact column (dedicated C-16 column) |
| R3 -> R4 | 1 | Section heading manifest (C-17) |

V-05 accumulates every signal from all prior rounds with no gaps against rubric v4.

**Convergence status**: V-05 is mature against v4. If C-18 (per-table column manifest) is added
to v5, V-05 already satisfies it via inline column manifests; V-01/V-02/V-03 would need one
insertion. If C-18 is not added, the scaffold is fully converged.

---

## Golden Variation

**V-05** -- triple-layer manifest makes both C-17 and C-16 violations detectable at three
independent structural locations. Designated Round 4 golden scaffold and v5 criteria extraction
candidate.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-table inline column manifest: placing Required columns declaration immediately before each table converts column requirement into execution-site pre-commitment -- column omission detectable at declaration line not only at table header; column-level analog of C-17; C-18 candidate", "manifest redundancy creates reliability gradient orthogonal to score: all five score 100 but differ in adversarial robustness; score and structural enforcement strength are independent axes -- rubric captures pass/fail; reliability gradient captures how hard violation is to produce undetected"]}
```
