## review-design — Round 13 Scorecard

**Rubric**: v12 | **Denominator**: 33 aspirational | **Date**: 2026-03-14

---

### Scoring Approach

All 5 variations carry the R12 V-05 baseline: BLOCK 0 through BLOCK 5, F-01 through F-27, all structural table forms, Section-leftmost BLOCK 2 (C-36), Amendment Cost column (C-38), Priority Rank column (C-39), Preservation Principle (C-40). The differentiation pivot is **C-37** (inline corrective action specificity), which became a criterion only in v12 and is now live.

---

### C-37 Compliance Analysis (Key Differentiator)

C-37 pass condition: every named F-ID includes both trigger and **explicit corrective action naming the target field and content type**. A single bare "Populate. Halt." without naming the target cell fails if it is the weakest link.

| F-ID test | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| F-07 (Reason cell) | "Populate the Reason cell with the specific content signal" ✓ | "Populate before continuing" — no cell name ✗ | "Populate. Halt." ✗ | "Populate the Reason cell" ✓ | "Populate. Halt." ✗ |
| F-02 (Sev tag) | "Replace the non-standard tag with P1, P2, or P3" ✓ | "Replace before continuing" — no target ✗ | "Replace" ✗ | "replace the non-standard value with the correct tier" ✓ | "Replace. Halt." ✗ |
| F-27 (P1 Section cell) | "Populate the Section cell before continuing" ✓ | "Populate before continuing" ✗ | "Populate" ✗ | "Populate the Section cell" ✓ | "Populate. Halt." ✗ |
| F-11 (SPLIT Synthesis) | "Populate the Synthesis cell before continuing" ✓ | "Populate with disagreement basis" — partial ✓ | "Populate with disagreement basis" ✓ | "Populate. Halt." — weakest point | "Populate. Halt." ✗ |
| F-17 (Re-run Scope name) | "Correct the name to a roster member" ✓ | "Correct the name" — no target ✗ | "Correct. Halt." ✗ | "correct the name to a roster member" ✓ | "Correct. Halt." ✗ |

**C-37 verdict**: V-01 and V-04 maintain cell-level specificity throughout. V-02, V-03, V-05 have systematic shorthand ("Populate. Halt." / "Replace. Halt.") without naming target fields.

---

### Per-Variation Scorecards

#### V-01 | Cost Continuity Formula

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 All 6 disciplines | essential | PASS | Security/Performance/Scalability/Maintainability/UX/Data-API all present |
| C-02 Severity on every finding | essential | PASS | F-02 fires on non-standard tag; "Replace the non-standard tag with P1, P2, or P3" |
| C-03 Domain expert auto-selection justified | essential | PASS | Signal-detected → Expert-added → Reason table in BLOCK 1 |
| C-04 Consensus block present | essential | PASS | BLOCK 3 with F-04 halt |
| C-05 Unique catches surfaced | recommended | PASS | BLOCK 4 with sentinel |
| C-06 Amend pathway described | recommended | PASS | BLOCK 5 targeted Re-run Scope + F-05 halt |
| C-07 Finding traceability to section | recommended | PASS | Section leftmost column + F-27 halt on P1 rows |
| C-08 Severity pyramid sanity | aspirational | PASS | BLOCK 2.5 with Status + F-06 |
| C-09 Expert disagreement synthesis | aspirational | PASS | SPLIT row Synthesis column + F-11 |
| C-10 Structural column enforcement | aspirational | PASS | `\| Section \| Sev \| Finding \|` table form |
| C-11 Three-field expert trace | aspirational | PASS | Signal detected / Expert added / Reason as labeled fields in table |
| C-12 Pyramid gate as dedicated block | aspirational | PASS | BLOCK 2.5 between BLOCK 2 and BLOCK 3 |
| C-13 Expert trace in table column form | aspirational | PASS | Table row per expert with three columns |
| C-14 Named halt conditions | aspirational | PASS | F-01 through F-27 across all mandatory blocks |
| C-15 Roster commitment table | aspirational | PASS | BLOCK 1.5 table before BLOCK 2 |
| C-16 Source column in roster | aspirational | PASS | `\| Reviewer \| Role \| Source \|` with Stock/Domain values |
| C-17 Orphan detection halt | aspirational | PASS | F-10 names exact-match requirement |
| C-18 SPLIT synthesis content halt | aspirational | PASS | F-11 fires on empty Synthesis |
| C-19 P1 count parity | aspirational | PASS | BLOCK 2.5 ANCHOR + F-12 fires on mismatch |
| C-20 BLOCK 5 4-column table | aspirational | PASS | 5-column table (Priority Rank additive; base schema intact) |
| C-21 BLOCK 0 signal catalogue | aspirational | PASS | BLOCK 0 with SHALL constraint + F-13/F-18 gates |
| C-22 BLOCK 3 4-column table | aspirational | PASS | `\| Issue \| Type \| Reviewers \| Synthesis \|` |
| C-23 Register isolation | aspirational | PASS | Formal modal throughout; no "aim for" / "try to" in headers or F-IDs |
| C-24 BLOCK 4 reviewer identity | aspirational | PASS | F-16 halt on absent-from-BLOCK-1.5 names |
| C-25 BLOCK 5 re-run scope identity | aspirational | PASS | F-17 halt naming roster-member requirement |
| C-26 BLOCK 0 disposition completeness | aspirational | PASS | F-18 bidirectional gate |
| C-27 Pyramid inversion rationale | aspirational | PASS | F-19 content gate |
| C-28 BLOCK 4 structural table | aspirational | PASS | 3-column table with F-20 halt |
| C-29 No-expert disposition reason | aspirational | PASS | F-21 fires on empty Reason; "N/A without explanation is non-conformant" |
| C-30 Domain expert finding coverage | aspirational | PASS | F-22 mirrors F-01 for domain tier |
| C-31 BLOCK 3 Issue cell completeness | aspirational | PASS | F-23 fires on empty Issue (sentinel exempt) |
| C-32 BLOCK 5 Action cell completeness | aspirational | PASS | F-24 fires on empty/placeholder Action |
| C-33 BLOCK 4 Finding cell completeness | aspirational | PASS | F-25 fires on empty Finding |
| C-34 BLOCK 5 Section cell completeness | aspirational | PASS | F-26 fires on empty/placeholder Section |
| C-35 BLOCK 2 P1 Section halt | aspirational | PASS | F-27 fires on empty P1 Section cell |
| C-36 Section column leftmost BLOCK 2 | aspirational | PASS | `\| Section \| Sev \| Finding \|` — Section first |
| C-37 Inline corrective actions | aspirational | PASS | Cell-level specificity throughout: "Reason cell with the specific content signal", "Replace the non-standard tag with P1, P2, or P3", "Populate the Section cell before continuing" |
| C-38 BLOCK 0 Amendment Cost column | aspirational | PASS | `\| Signal Phrase \| Location \| Amendment Cost \| Disposition \|` |
| C-39 BLOCK 5 Priority Rank column | aspirational | PASS | Priority Rank as first column in 5-column BLOCK 5 table |
| C-40 BLOCK 5 Inertia framing | aspirational | PASS | PRESERVATION PRINCIPLE declared before amend table; bars full re-review |

**Essential**: 4/4 → 60.00 | **Recommended**: 3/3 → 30.00 | **Aspirational**: 33/33 → 10.00
**V-01 Composite: 100.00**

---

#### V-02 | Section-Anchored BLOCK 5

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 – C-04 | essential | PASS × 4 | All blocks present, all 6 disciplines, F-02/F-03/F-04 gates |
| C-05 – C-07 | recommended | PASS × 3 | Unique catches, targeted amend, F-27 on P1 Section |
| C-08 – C-36 | aspirational | PASS × 29 | Full F-01 through F-27 enforcement; Section-leftmost BLOCK 2; Section-first BLOCK 5 new axis |
| **C-37** | aspirational | **FAIL** | F-07 "Populate before continuing" (no cell name); F-02 "Replace before continuing" (no P1/P2/P3 target); F-27 "Populate before continuing" (no cell name); F-17 "Correct the name" (no roster-member content); systematic shorthand throughout |
| C-38 | aspirational | PASS | Amendment Cost in BLOCK 0 |
| C-39 | aspirational | PASS | Priority Rank column in BLOCK 5 |
| C-40 | aspirational | PASS | Preservation Principle declared |

**New feature carried**: Section-first in BLOCK 5 (`Section | Priority Rank | P1 Finding | Action | Re-run Scope`) + section-traceability cross-block rule (Section in BLOCK 5 absent from BLOCK 2 = structural mismatch). Not a v12 criterion but surfaces as R13 new-pattern candidate.

**Essential**: 4/4 → 60.00 | **Recommended**: 3/3 → 30.00 | **Aspirational**: 32/33 → 9.697
**V-02 Composite: 99.70**

---

#### V-03 | Consensus as Elevation Gate

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 – C-04 | essential | PASS × 4 | All structures present including BLOCK 3 with Elevation Record |
| C-05 – C-07 | recommended | PASS × 3 | All met |
| C-08 – C-36 | aspirational | PASS × 29 | Full enforcement chain; Section-leftmost BLOCK 2; Elevation Record in BLOCK 3 is additive |
| **C-37** | aspirational | **FAIL** | F-07 "Populate. Halt." (bare); F-02 "Replace. Halt." (no target content); F-06 "Populate. Halt." (no cell name); F-15 "Correct. Halt." (generic); systematic minimal corrective language |
| C-38 | aspirational | PASS | Amendment Cost in BLOCK 0 |
| C-39 | aspirational | PASS | Priority Rank column in BLOCK 5 |
| C-40 | aspirational | PASS | Preservation Principle + Consensus Elevation Rule |

**New feature carried**: BLOCK 3 Elevation Record sub-table (`P1 Finding | Consensus Status`); BLOCK 5 CONSENSUS ELEVATION RULE (ELEVATED SHALL rank lower integer than BASELINE). Not a v12 criterion but a significant new enforcement class candidate.

**Essential**: 4/4 → 60.00 | **Recommended**: 3/3 → 30.00 | **Aspirational**: 32/33 → 9.697
**V-03 Composite: 99.70**

---

#### V-04 | Declarative Register + Cost Continuity Formula

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 – C-04 | essential | PASS × 4 | All blocks present with CONSTRAINT VIOLATED gates |
| C-05 – C-07 | recommended | PASS × 3 | All met |
| C-08 – C-36 | aspirational | PASS × 29 | Full F-01 through F-27 as CONSTRAINT VIOLATED entries; Section-leftmost BLOCK 2 |
| **C-37** | aspirational | **PASS** | Declarative framing embeds corrective context: "Populate the Reason cell" ✓; "replace the non-standard value with the correct tier" ✓; "Populate the Section cell" ✓; "correct the name to a roster member" ✓; "populate with a specific finding description" ✓. F-11 and F-19 are the weakest ("Populate. Halt.") but all others are well above threshold |
| C-38 | aspirational | PASS | Amendment Cost column in BLOCK 0 |
| C-39 | aspirational | PASS | Priority Rank column in BLOCK 5 |
| C-40 | aspirational | PASS | Preservation Principle declared before amend table |
| C-23 | aspirational | PASS | Declarative block headers ("This block produces…") and CONSTRAINT VIOLATED marker contain no informal calibration language; SHA/MUST register intact |

**New feature carried**: Declarative output-framing register (block headers describe artifacts, not procedures); "CONSTRAINT VIOLATED:" as halt marker — alternative formal register distinct from "fires when." V-01 formula also carried.

**Essential**: 4/4 → 60.00 | **Recommended**: 3/3 → 30.00 | **Aspirational**: 33/33 → 10.00
**V-04 Composite: 100.00**

---

#### V-05 | Three-Axis Convergence (Section BLOCK 5 + Consensus Gate + Derivation Formula)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 – C-04 | essential | PASS × 4 | All present |
| C-05 – C-07 | recommended | PASS × 3 | All met |
| C-08 – C-36 | aspirational | PASS × 29 | Section-leftmost BLOCK 2; all F-01 through F-27; BLOCK 3 Elevation Record; SECTION TRACEABILITY rule in BLOCK 5 |
| **C-37** | aspirational | **FAIL** | Systematic bare forms: F-07 "Populate. Halt.", F-02 "Replace. Halt.", F-06 "Populate. Halt.", F-10 "Correct the mismatch. Halt.", F-11 "Populate. Halt.", F-14 "Replace. Halt.", F-15 "Correct. Halt.", F-17 "Correct. Halt." — majority of F-IDs use one-word actions without naming target field or content type |
| C-38 | aspirational | PASS | Amendment Cost in BLOCK 0 |
| C-39 | aspirational | PASS | Priority Rank column in Section-first BLOCK 5 |
| C-40 | aspirational | PASS | Preservation Principle + Consensus Elevation Rule + Section Traceability — strongest C-40 formulation across all variations |

**New feature carried**: All three axes simultaneously: Section-first in both BLOCK 2 and BLOCK 5 (structural spine through the entire lifecycle); BLOCK 3 Elevation Record feeding BLOCK 5 tier ordering; derivation formula within each tier; SECTION TRACEABILITY named constraint (BLOCK 5 Section absent from BLOCK 2 = conformance signal). The C-37 degradation is the direct cost of maximizing new-axis density.

**Essential**: 4/4 → 60.00 | **Recommended**: 3/3 → 30.00 | **Aspirational**: 32/33 → 9.697
**V-05 Composite: 99.70**

---

### Rankings

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | **V-01** | **100.00** | Formula-verifiable Priority Rank; tightest F-ID corrective action language across all 27 F-codes |
| 1 | **V-04** | **100.00** | Declarative output-framing register; CONSTRAINT VIOLATED marker; formula continuity carried |
| 3 | V-02 | 99.70 | Section-first BLOCK 5 + cross-block traceability rule; C-37 shorthand across majority of F-IDs |
| 3 | V-03 | 99.70 | Consensus elevation hard gate + BLOCK 3 Elevation Record; C-37 shorthand |
| 3 | V-05 | 99.70 | Richest feature set (three axes + SECTION TRACEABILITY); most C-37 degradation |

**Note on V-01 vs V-04 tie**: Both score 100 against the v12 rubric. V-04's declarative register represents a more fundamental structural paradigm shift (output-framing vs process-instruction); V-01's arithmetic formula introduces a new cross-block verifiability class. Excellence signals exist in both.

---

### Excellence Signals

**From V-01 (top score):**
- **Formula-anchored rank**: Priority Rank derived from `BLOCK 0 Amendment Cost (H=3/M=2/L=1) + BLOCK 3 Consensus (+2 if AGREE) + reviewer count (+1 each)`. Rank assignment is now arithmetic-verifiable, not qualitative — a rank inconsistent with formula inputs is a structural violation detectable without rubric inspection.
- **Corrective action precision floor**: F-02 "Replace the non-standard tag with P1, P2, or P3" and F-07 "Populate the Reason cell with the specific content signal that warrants this expert" — naming both the target cell and the content type in every F-ID except structural-reconciliation halts.

**From V-04 (top score):**
- **Declarative output-framing**: Block headers describe the artifact each block produces ("This block produces a committed reviewer roster") rather than giving procedural instructions. The generator must produce the named artifact; skipping means the artifact is absent, not that an instruction was missed.
- **CONSTRAINT VIOLATED as salient halt marker**: Placing the violation declaration first before the trigger condition (vs "fires when X, halt" where the trigger comes first) makes the constraint class visible at line-start — consistent with the leftmost-column salience principle applied to column order in C-36.

**From V-05 (99.70 — richest feature set despite C-37 cost):**
- **SECTION TRACEABILITY as named cross-block constraint**: "Every Section value in this table SHALL appear in at least one BLOCK 2 finding table" — extends section primacy from a column-order rule (C-36) to a cross-block identity gate. A BLOCK 5 amend acting on a location never reviewed is a new structural violation class orthogonal to all existing F-codes.

**From V-03 (99.70):**
- **Consensus-as-ordering-gate with Elevation Record**: The BLOCK 3 Elevation Record (`P1 Finding | Consensus Status`) makes the ELEVATED/BASELINE split a first-class artifact, not a prose annotation. BLOCK 5 must honor this record's tier ordering or fire a conformance signal. This is the first cross-block ordering constraint in the rubric architecture.

---

### Candidate v13 Criteria

| ID | Pattern | Source | Enforcement Class |
|----|---------|--------|------------------|
| C-41 | BLOCK 5 Priority Rank derivation formula arithmetic consistency | V-01, V-04, V-05 | Cross-block: rank inconsistent with formula inputs is a structural violation |
| C-42 | BLOCK 5 Section traceability cross-block gate | V-02, V-05 | Cross-block identity: Section in BLOCK 5 absent from BLOCK 2 = unreviewed location |
| C-43 | BLOCK 3 Elevation Record as explicit artifact | V-03, V-05 | Structural: ELEVATED/BASELINE partition must be a named first-class table, not an ordering annotation |
| C-44 | Declarative output-framing register for block headers | V-04 | Format: block header describes output artifact, not procedural instruction |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["arithmetic-verifiable Priority Rank derivation formula creates cross-block formula-consistency enforcement class (rank inconsistent with BLOCK 0 cost + BLOCK 3 consensus + reviewer count inputs is a structural violation)", "BLOCK 5 section traceability cross-block gate: Section value in amend plan absent from BLOCK 2 finding tables indicates amend acting on unreviewed design location — new identity-class violation orthogonal to all existing F-codes", "BLOCK 3 Elevation Record as named first-class artifact promoting consensus status from ordering annotation to structurally enforceable partition table", "declarative output-framing register: block headers describe output artifacts rather than procedural instructions; CONSTRAINT VIOLATED as salient halt marker extending leftmost-column salience principle from column order to violation declaration order"]}
```
