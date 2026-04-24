# trace-state · Round 14 Scoring · Rubric v13

---

## Point Value Recap

| Bucket | Weight | Criteria | Pts Each |
|--------|--------|----------|----------|
| Essential | 60% | C-01 – C-05 (5) | 12.00 |
| Recommended | 30% | C-06 – C-08 (3) | 10.00 |
| Aspirational | 10% | C-09 – C-43 (35) | 0.286 |

**Baseline (R13 V-05 under v13)**: passes C-01–C-41, fails C-42 and C-43.
Score = 60 + 30 + (33 × 0.286) = **99.43**

---

## Variation Summary Table

| Variation | Axis | C-42 | C-43 | Aspirational Passed | Score |
|-----------|------|------|------|---------------------|-------|
| V-01 | Output Format | **PASS** | FAIL | 34/35 | **99.71** |
| V-02 | Lifecycle Emphasis | FAIL | **PASS** | 34/35 | **99.71** |
| V-03 | Phrasing Register | PARTIAL | FAIL | 33.5/35 | **99.57** |
| V-04 | Output Format + Lifecycle | **PASS** | **PASS** | 35/35 | **100.00** |
| V-05 | Lifecycle + Phrasing | PARTIAL | **PASS** | 34.5/35 | **99.86** |

---

## V-01 — Criterion-Level Detail (full template provided)

### Essential (all PASS — 60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Before/after state per operation | PASS | Trace step template has `From: ___ (S-ID)` / `To: ___ (S-ID)` on every step |
| C-02 Preconditions + postconditions per operation | PASS | `Precondition check` and `Postcondition verified` are named fields in the step template |
| C-03 Invariants named | PASS | INV-ID registry required at 1D with explicit threshold |
| C-04 At least one anomaly identified | PASS | All five phases require Findings List; sweep cannot be empty without Gap Record |
| C-05 Domain grounding | PASS | Header: `Domain: {domain} — Sales / Customer Service / Finance` |

### Recommended (all PASS — 30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-06 Negative path | PASS | Rejection step template requires explicit `After-state: Entity remains in [From-State S-ID]` |
| C-07 Numbered step-by-step | PASS | `Step N` template enforced for 8–15 steps |
| C-08 Race condition scenario | PASS | Phase 3D dedicated phase for RCS in lock chain |

### Aspirational — Selected Highlights

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-09 All four anomaly types | PASS | Phases 3A–3D cover IST / MPC / IVC / RCS |
| C-10 Structured notation | PASS | State Registry, Operation Registry, Invariant Registry all tabular |
| C-11 Sweep table with row-level verdicts | PASS | Pass 1 and Pass 2 tables per phase with Strength column |
| C-12 OP-ID cross-referencing | PASS | Trace step template requires `OP-ID` field referencing Operation Registry |
| C-13 Entry Condition column | PASS | `Entry Condition` column explicit in State Registry template at 1B |
| C-14 Min-found threshold | PASS | Evidence Strength Gate: "at least one finding at strength ≥ 2" |
| C-15 Full ID ecosystem | PASS | S-IDs (1B), OP-IDs (1C), INV-IDs (1D) all declared |
| C-16 URF as fifth anomaly class | PASS | Phase 3E with its own sweep structure |
| C-17 Anomaly register with entity-type columns | PASS | Separate Declaration-Only and Trace-Diff columns per sweep table |
| C-18 Pre-sweep hypothesis | PASS | PART 3 prediction table before Phase 3A opens |
| C-19 Evidence strength 1/2/3 quality gate | PASS | Strength column in every sweep table |
| C-20 Numeric/temporal invariant gate | PASS | "Declare at least one INV-ID with explicit falsifiable threshold" at 1C |
| C-21 Surprise column in reconciliation | PASS | Inherited from baseline (PART 5, not shown; v12 baseline passes) |
| C-22 Score-at-point-of-discovery | PASS | Inline note: "assign strength at moment of discovery, not end-of-pass" |
| C-23 Score-aloud verbal protocol | PASS | "Incomplete sentence = not recordable" explicitly names the discipline |
| C-24 Phase exit gate checkboxes | PASS | Exit Certification checklist with ☐ items per phase |
| C-25 Three-value surprise taxonomy | PASS | Inherited from baseline |
| C-26 Anomaly-type-as-top-level-phase | PASS | 3A → 3B → 3C → 3D → 3E as numbered lock-chained phases |
| C-27 Prejudice-dismissal naming | PASS | Gap Record field "What Was Not Found" requires specific trace steps or state conditions |
| C-28 Dual-mode detection | PASS | Pass 1 Declaration-Only + Pass 2 Trace-Diff in every phase |
| C-29 Acquittal-advocate sub-role | PASS | `Role B pre-detection commitment` and Gap Record mandatory regardless of finding count |
| C-30 Parallel verdict columns | PASS | `Declaration-Only Finding` and `Trace-Diff Finding` as separate named columns |
| C-31 Phase LOCKED/OPEN with COMPLETE | PASS | `[LOCKED until PHASE N-1: COMPLETE]` and unlock signal declared per phase |
| C-32 Unconditional gap documentation | PASS | "mandatory regardless of finding count" stated explicitly in Phase 3A |
| C-33 Symmetric phase output contract | PASS | Every phase emits `Findings List + Gap Record` pair |
| C-34 Gap Record as mechanical unlock signal | PASS | "The Gap Record is the unlock signal for the Phase 3A exit gate." |
| C-35 Pre-detection Role B commitment | PASS | SCORING PROTOCOL table placed before either detection pass; commitment recorded before findings |
| C-36 URF as fifth peer phase | PASS | Phase 3E has sweep table, LOCKED/OPEN label, COMPLETE signal, Role B elements |
| C-37 Evidence strength as hard exit gate | PASS | Evidence Strength Gate is checkbox item in Exit Certification |
| C-38 Global standards registry with pre-game seal | PASS | 0B Standards Registry sealed before PART 1 opens; SEALED declaration explicit |
| C-39 Rejection immutability as mandatory trace constraint | PASS | `[If REJECTED] After-state` is named structural element in step template |
| C-40 | PASS | Inherited from baseline |
| C-41 Phase 3E Pass 1 entity-class stratification | PASS | P1-S / P1-O / P1-I sub-tables in Phase 3E Pass 1 |
| **C-42** Application Sentence as active binding | **PASS** | SCORING PROTOCOL table has `Application Sentence` as mandatory named row; explicit failure condition: "A sentence that reproduces the Verbatim Restate is a structural failure of this table" |
| **C-43** Phase 3E Pass 2 stratified P2-S/P2-O/P2-I | **FAIL** | Template explicitly notes "(single unified pass — see V-02 for stratified Pass 2)" — stratification absent |

**V-01 Score**: 60 + 30 + (34/35 × 10) = **99.71**

---

## V-02 — Delta Analysis (Lifecycle Emphasis — C-43)

V-02 adds P2-S/P2-O/P2-I sub-scan tables to Phase 3E Pass 2, mirroring Pass 1's stratification. The "single unified pass" note is replaced with three independent Trace-Diff sub-tables. No SCORING PROTOCOL Application Sentence table is introduced.

| Changed criterion | Verdict | Note |
|-------------------|---------|------|
| C-42 | **FAIL** | No named Application Sentence column or failure-condition enforcement; falls back to prose-level commitment (C-35 satisfied but C-42's structural-table requirement absent) |
| C-43 | **PASS** | P2-S / P2-O / P2-I present as independent sub-scans; a passing P2-S cannot mask absent P2-O or P2-I |

**V-02 Score**: 60 + 30 + (34/35 × 10) = **99.71**

---

## V-03 — Delta Analysis (Phrasing Register — C-42)

V-03 enforces the Application Sentence through bolded behavioral instruction ("**You MUST produce an active, evidence-shape binding sentence distinct from the registry restate**") rather than a named table column with a structural failure condition. This partially addresses C-42's intent but does not provide a blank-cell-is-detectable constraint.

| Changed criterion | Verdict | Note |
|-------------------|---------|------|
| C-42 | **PARTIAL** | Prose instruction closes the behavioral gap but not the structural gap; a model can satisfy the phrasing register without the Application Sentence being independently auditable from the verbatim restate |
| C-43 | **FAIL** | Not targeted |

**V-03 Score**: 60 + 30 + ((33 + 0.5) / 35 × 10) = **99.57**

---

## V-04 — Delta Analysis (Output Format + Lifecycle Emphasis — C-42 + C-43)

V-04 combines V-01's SCORING PROTOCOL table (Application Sentence as named, required column with explicit failure condition) with V-02's Phase 3E Pass 2 stratification (P2-S / P2-O / P2-I). Both targeted criteria are structurally enforced.

| Changed criterion | Verdict | Note |
|-------------------|---------|------|
| C-42 | **PASS** | SCORING PROTOCOL table with Application Sentence column + structural failure declaration |
| C-43 | **PASS** | P2-S / P2-O / P2-I as independent Pass 2 sub-scans in Phase 3E |

**V-04 Score**: 60 + 30 + (35/35 × 10) = **100.00**

---

## V-05 — Delta Analysis (Lifecycle Emphasis + Phrasing Register — C-42 + C-43)

V-05 combines V-02's stratification with V-03's phrasing approach for the Application Sentence. C-43 is structurally satisfied; C-42 is behaviorally addressed but not structurally enforced.

| Changed criterion | Verdict | Note |
|-------------------|---------|------|
| C-42 | **PARTIAL** | Behavioral enforcement via instruction phrasing; no table column; not independently auditable |
| C-43 | **PASS** | Stratified Pass 2 present |

**V-05 Score**: 60 + 30 + ((34 + 0.5) / 35 × 10) = **99.86**

---

## Ranking

| Rank | Variation | Score | C-42 | C-43 |
|------|-----------|-------|------|------|
| 1 | V-04 | **100.00** | PASS | PASS |
| 2 | V-05 | 99.86 | PARTIAL | PASS |
| 3 | V-01 | 99.71 | PASS | FAIL |
| 3 | V-02 | 99.71 | FAIL | PASS |
| 5 | V-03 | 99.57 | PARTIAL | FAIL |

---

## Excellence Signals from V-04

**Signal 1 — Application Sentence as named table column with dual constraint (positive + failure condition)**
The SCORING PROTOCOL table places the Application Sentence in a separate row from Verbatim Restate. Critically, it declares *both* what the field must be ("active binding naming the specific evidence shape") *and* what it must not be ("reproduces the Verbatim Restate is a structural failure"). The failure condition converts C-42 from a positive requirement into a two-sided mechanical gate: a passing Application Sentence must satisfy the positive definition *and* not trigger the failure condition. This is structurally stronger than a named column alone.

**Signal 2 — Phase 3E Application Sentence must enumerate entity-class-aware evidence shapes**
When Pass 2 is stratified (C-43) and the Application Sentence is required (C-42), the Application Sentence for Phase 3E must implicitly cover all three entity classes to remain non-vacuous. A generic Application Sentence for URF cannot be class-aware if the sub-scans have been collapsed into a single pass. V-04's combination forces the Application Sentence to reference which entity-class evidence shapes distinguish strength ≥ 2 in P2-S vs P2-O vs P2-I — a more specific binding than C-42 alone captures.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Application Sentence enforced via two-sided constraint: positive evidence-shape definition plus explicit named failure condition for restate echo — converts C-42 from a positive requirement to a mechanical two-sided gate", "Phase 3E Application Sentence must be entity-class-aware when Pass 2 is stratified: C-42 + C-43 combination forces the Application Sentence to enumerate evidence shapes per P2-S/P2-O/P2-I sub-scan rather than a generic URF threshold statement"]}
```
