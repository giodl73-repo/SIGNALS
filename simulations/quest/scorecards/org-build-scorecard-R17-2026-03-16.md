## Quest Score — org-build R17 (Rubric v12)

### Evaluation

---

#### V-01 — Binary Compliance Tokens

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 3 Step 1 produces org-chart.md with ASCII box/line diagram, min 2 levels |
| C-02 | PASS | Phase 2 Step 5 + Phase 3 Step 2 enumerate all five fields |
| C-03 | PASS | Phase 2 Step 3 + Phase 3 Step 2 require inertia-advocate |
| C-04 | PASS | Phase 2 Step 1 binds floor to T0-DEPTH-FLAG |
| C-05 | PASS | Phase 3 Step 1: Area, Headcount, Key Roles, Decides, Escalates |
| C-06 | PASS | Phase 2 Step 2 + Phase 3 Step 2: group by area subdir |
| C-07 | PASS | Phase 3 Step 1: 3+ row rhythm, charter with quorum N of M |
| C-08 | PASS | Phase 1 delivers FLAT-CASE-PRESSURE: <T1-PRESSURE>, VERDICT: <T1-VERDICT>, closed set |
| C-09 | PASS | Row 1 headcount threshold, Row 2 different trigger category |
| C-10 | PASS | Phase 2 Constraints: MUST use `[element name] (cat-N) --` format |
| C-11 | PASS | SCOPE-TEMPLATE[T1-PRESSURE] verbatim via gate variable |
| C-12 | PASS | CATEGORY-DERIVATION[T1-VERDICT] drives category selection |
| C-13 | PASS | "FORBIDDEN: writing both verdicts. Both is an error." |
| C-14 | PASS | T1-VERDICT/T1-PRESSURE emitted at Phase 1 gate, consumed by Phase 2 Input Contract |
| C-15 | PASS | "FORBIDDEN: writing neither verdict. Neither is an error." — bidirectional |
| C-16 | PASS | Phase 3 Constraints: FORBIDDEN Mitigation cells with format guidance |
| C-17 | PASS | FORBIDDEN: paraphrasing template; verbatim enforced in Constraints |
| C-18 | PASS | CATEGORY-DERIVATION table + per-verdict FORBIDDEN categories |
| C-19 | PASS | All constraint statements use MUST/FORBIDDEN; no advisory language |
| C-20 | PASS | All gates declare named typed outputs; all consuming phases declare Input Contracts |
| C-21 | PASS | Phase 3 Input Contract binds all named variables with MUST/FORBIDDEN |
| C-22 | **FAIL** | No artifact skeleton with `{{SLOT}}` notation |
| C-23 | PASS | Per-boundary FORBIDDEN at each phase transition |
| C-24 | PASS | `=== RECORD: PHASE-N ===` blocks present after each phase |
| C-25 | PASS | Outbound FORBIDDEN in Constraints + inbound FORBIDDEN in Input Contract at every boundary |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field unifies declaration, anchor, and materialization |
| C-27 | PASS | Phase 2 Task Step 1: per-flag conditional with MUST for each case |
| C-28 | PASS | PHASE-ORDERING-GUARD as named first entry in every record block |
| C-29 | PASS | All prohibitions use explicit `FORBIDDEN:` — no "do not X" or "avoid X" |
| C-30 | PASS | Task Steps / Constraints / Input Contract structurally segmented |
| C-31 | PASS | T2-COUNT-COMPLIANCE: [FLOOR-MET \| FLOOR-MISS]; T2-AREA-COMPLIANCE: [ADEQUATE \| INADEQUATE]; all fields closed-set |
| C-32 | PASS | Input Contract labeled section distinct from Constraints in all consuming phases |
| C-33 | PASS | All Input Contracts name every consumed variable with source + MUST/FORBIDDEN binding |
| C-34 | PASS | CATEGORY-DERIVATION table: Required Categories + FORBIDDEN Categories columns side-by-side |
| C-35 | PASS | Phase 1 = INERTIA-VERDICT before Phase 2 = ROLE-ENUM; T1-VERDICT is gate output consumed by Phase 2 |
| C-36 | PASS | PRE-PHASE CONSTANTS section before phases; FORBIDDEN embedding inside phase instructions |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 27/28**
`composite = (5/5 × 60) + (3/3 × 30) + (27/28 × 10) = 60 + 30 + 9.64 = **99.6**`

---

#### V-02 — Depth-Outcome Class

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-21 | PASS | Same structural wins as V-01; table-dominant Constraints format doesn't affect criterion coverage |
| C-22 | **FAIL** | No artifact skeleton with `{{SLOT}}` notation |
| C-23–C-36 | PASS | Same structural wins; T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS] and T2-AREA-OUTCOME: [COVERAGE-ADEQUATE \| COVERAGE-INADEQUATE] give richer C-31 semantics |

Notable: C-31 is stronger here — depth-outcome class encodes both mode and compliance in one token. But C-22 still absent.

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 27/28**
`composite = 60 + 30 + 9.64 = **99.6**`

---

#### V-03 — Count Fields Removed from Record Block

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-21 | PASS | Count compliance verified in Phase 2 Constraints pre-emission; Phase 3 Input Contract re-consumes T0-DEPTH-FLAG for count floor — all gate variable bindings named with MUST/FORBIDDEN |
| C-22 | **FAIL** | No artifact skeleton with `{{SLOT}}` notation |
| C-23–C-36 | PASS | Sub-step ordering guards (FORBIDDEN: beginning sub-step AREA before completing COUNT) extend phase-ordering discipline into task substeps; all record block fields carry closed-set annotations |

Notable: C-31 passes cleanly — by eliminating count fields entirely, the record block has no range-annotated fields at all.

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 27/28**
`composite = 60 + 30 + 9.64 = **99.6**`

---

#### V-04 — Binary Compliance Tokens + Terse Imperative Register

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-21 | PASS | Same as V-01; terse register does not introduce advisory language |
| C-22 | **FAIL** | No artifact skeleton with `{{SLOT}}` notation |
| C-23–C-36 | PASS | CATEGORY-DERIVATION table uses abbreviated labels (cat-2, cat-3 only) but still has both Required and FORBIDDEN columns — C-34 holds |

Notable: C-29 is especially clean here — the terse format leaves no surface area for "do not" creep.

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 27/28**
`composite = 60 + 30 + 9.64 = **99.6**`

---

#### V-05 — Depth-Outcome Class + Complete Artifact Skeleton

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-21 | PASS | All structural wins from V-02 carry forward |
| C-22 | **PASS** | ORG-CHART.MD SKELETON present with {{T1-PRESSURE}}, {{T1-VERDICT}}, {{T2-CATEGORY-A}}, {{T2-CATEGORY-B}}, {{T2-ROLE-OUTCOME}}, {{T2-AREA-OUTCOME}}, {{T0-DEPTH-FLAG}}, {{T2-IA-SCOPE-SOURCE}} — every gate variable has a corresponding slot; Phase 3 Input Contract maps each variable to its slot explicitly |
| C-23 | PASS | Per-boundary FORBIDDEN at each transition |
| C-24 | PASS | Named record blocks emitted after each phase |
| C-25 | PASS | Double-guard at all three phase boundaries |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field unifies declaration + anchor + materialization |
| C-27 | PASS | Phase 2 Task Step 1 flag-conditional count floor with T2-ROLE-OUTCOME derivation |
| C-28 | PASS | PHASE-ORDERING-GUARD named first field in all record blocks |
| C-29 | PASS | All prohibitions use `FORBIDDEN:` including PRE-PHASE CONSTANTS ("FORBIDDEN: restating or duplicating any row…") |
| C-30 | PASS | Task Steps / Input Contract / Constraints structurally segmented throughout |
| C-31 | PASS | T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS]; T2-AREA-OUTCOME: [COVERAGE-ADEQUATE \| COVERAGE-INADEQUATE]; all 9 record fields across 3 blocks carry closed-set annotations |
| C-32 | PASS | Input Contract and Constraints are labeled distinct sections in Phases 1–3 |
| C-33 | PASS | Phase 3 Input Contract is fully self-contained — every consumed variable named, source identified, MUST/FORBIDDEN binding present; no variable consumption implicit in Task Steps |
| C-34 | PASS | CATEGORY-DERIVATION table: Required Categories + FORBIDDEN Categories columns, both populated for both verdict rows |
| C-35 | PASS | INERTIA-VERDICT (Phase 1) produces T1-VERDICT as gate output; ROLE-ENUM (Phase 2) Input Contract names T1-VERDICT as required with FORBIDDEN guard |
| C-36 | PASS | PRE-PHASE CONSTANTS section before Phase 0; "FORBIDDEN: embedding these table definitions inside phase instructions" + "FORBIDDEN: restating or duplicating any row" — strongest enforcement of the three variations that declare pre-phase constants |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 28/28**
`composite = (5/5 × 60) + (3/3 × 30) + (28/28 × 10) = 60 + 30 + 10 = **100.0**`

---

### Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | **V-05** | 5/5 | 3/3 | **28/28** | **100.0** |
| 2 | V-01 | 5/5 | 3/3 | 27/28 | 99.6 |
| 2 | V-02 | 5/5 | 3/3 | 27/28 | 99.6 |
| 2 | V-03 | 5/5 | 3/3 | 27/28 | 99.6 |
| 2 | V-04 | 5/5 | 3/3 | 27/28 | 99.6 |

All five variations pass all essential and recommended criteria. The universal blocker in V-01 through V-04 is C-22 (no artifact skeleton with `{{SLOT}}` notation). V-05 resolves this by adding the ORG-CHART.MD SKELETON with Generation Metadata section.

### Excellence Signals from V-05

**Pattern 1 — Generation Metadata section as artifact home for non-content gate variables**
Phase 2 gate variables for count compliance (T2-ROLE-OUTCOME, T2-AREA-OUTCOME) and IA scope provenance (T2-IA-SCOPE-SOURCE) don't belong in any content section of org-chart.md. V-05 adds a `## Generation Metadata` section at the end of the skeleton that houses all these variables with named slots. This satisfies C-22 (every gate variable has an artifact slot) and C-31 (closed-set annotations on all fields) simultaneously for the entire variable set. The pattern: *any gate variable that is machine-useful but not human-readable content should be housed in a Generation Metadata section of the artifact skeleton.*

**Pattern 2 — Depth-outcome class encodes mode + compliance in a single closed token**
T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS] is semantically richer than a binary [FLOOR-MET | FLOOR-MISS]. The depth mode becomes observable at the gate — Phase 3 can verify role count compliance from T2-ROLE-OUTCOME alone without re-consulting T0-DEPTH-FLAG. This eliminates a cross-phase dependency in Phase 3's Input Contract and makes the count compliance audit fully self-contained at the Phase 2 boundary. The pattern: *when a compliance token's meaning depends on a prior gate variable's value, encode both the condition and the verdict in the token itself.*

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["generation metadata section in artifact skeleton houses all non-content gate variables (count/area compliance, IA scope source) with named slots — satisfies C-22 and C-31 simultaneously without cluttering content sections", "depth-outcome class encodes depth mode and compliance verdict in a single closed token (STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS), making count compliance self-contained at the Phase 2 gate and eliminating Phase 3 re-consultation of T0-DEPTH-FLAG"]}
```
