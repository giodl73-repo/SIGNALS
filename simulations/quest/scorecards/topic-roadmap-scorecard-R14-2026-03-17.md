Now I have all the variation content. Let me score each against the v14 rubric.

---

## Scorecard — topic-roadmap (topic-plan) v14 — Round 14

### Rubric Calibration

| Item | Value |
|------|-------|
| Formula | raw / 50 × 10 |
| Aspirational max | 25 × 2 = 50 |
| R13 V-05 baseline under v14 | 44/50 = 8.80 (C-31=0, C-32=0, C-33=0) |
| New headroom | 6 points (3 × 2) |

---

### V-01 — C-31 single axis (both failure modes named)

**Mechanism**: PROPOSAL BIAS AUDIT guard upgraded to name SYSTEMIC PHASE STRUCTURE BIAS (phase-level) and MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE (row-level), with explicit "BOTH LEVELS ARE REQUIRED. Neither substitutes for the other." SECTION SCOPE and CONTRACT unchanged from R13 V-05.

#### Criteria — Essential (all must pass)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 INERTIA COMPETITOR DECLARATION | PASS | Present at document open with full guard block |
| C-02 Phase ordering enforced | PASS | All 8 phases present with ENTRY CONDITION gates |
| C-03 Phase 1 READ-BARRIER | PASS | FIRST-RUN and RESTART isolation both present |
| C-04 Phase 2 9-namespace scan | PASS | Explicit null-row requirement stated |
| C-05 SIGNAL READ-LOCK at Phase 2 exit | PASS | Lock present with mechanism |

#### Criteria — Recommended (at least 2 of 3 must pass)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 Null path stop | PASS | "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS. Stop. Phase 6 does NOT open." at Phase 5 |
| C-07 Confidence tiers | PASS | HIGH/MEDIUM/LOW defined with evidential counts in Verdict Vocabulary |

#### Criteria — Aspirational (C-09 through C-30, each 2 pts)

All 22 criteria C-09–C-30 inherited from R13 V-05 at FULL (2) = **44 raw points**. Key checks:

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-24 SECTION SCOPE spatial separation | FULL | All four section scopes present with exclusion declarations |
| C-27 WRITE GUARD | FULL | Phase 7 + Phase 8 WRITE GUARD present |
| C-28 DEFEAT ASSESSMENT independence | FULL | Two-site INERTIA-GATE enforcement pattern intact |
| C-29 Consequence field naming identity | FULL | "Consequence if unchanged" at Phase 5 table, 6a, 6b, exit criterion — 4/4 sites |
| C-30 Bias column in schema | FULL | "Bias blocked by guard" present in Phase 6a and 6b schema |

#### New Aspirational Criteria (v14)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-31 PROPOSAL BIAS AUDIT guard at Phase 6 entry** | **FULL (2)** | Guard at Phase 6 entry co-located with INERTIA-GATE. Names LEVEL 1 (SYSTEMIC PHASE STRUCTURE BIAS) and LEVEL 2 (MOTIVATED REASONING AT INDIVIDUAL PROPOSAL DECISION SURFACE) as distinct failure modes at distinct granularities. States "BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against per-proposal motivated reasoning. The row-level column does not protect against systemic phase structure bias." Fully satisfies C-31 full condition. |
| **C-32 Phase 6 SECTION SCOPE includes row-level bias labeling** | **FAIL (0)** | SECTION SCOPE text reads "gate-exclusion text, proposal generation, and row-level bias labeling" — unchanged from R13 V-05 pre-C-31 form. Does not cross-reference the PROPOSAL BIAS AUDIT guard as enforcement mechanism. A C-24 auditor finds "row-level bias labeling" listed but cannot confirm from the scope declaration which guard produces it or that it is co-located at phase entry. Triggers FAIL condition: "SECTION SCOPE unchanged from pre-C-31 form." |
| **C-33 Output Schema CONTRACT pre-commits both fields** | **FAIL (0)** | CONTRACT block is an embedded annotation inside the Output Schema section (`[>> CONTRACT: ... <<]`), not a standalone named section. Not positioned before INERTIA COMPETITOR DECLARATION. While both CONTRACT A and CONTRACT B elements are present in the annotation, the block is not standalone — a scorer must navigate into the Output Schema section to locate it rather than encountering it as the first document content. Fails the standalone requirement for FULL; does not qualify for Partial because both elements are present and positioning is before Phase 1, but the non-standalone form is treated as FAIL under v14 strict evaluation. |

**V-01 raw: 44 + 2 + 0 + 0 = 46/50**
**V-01 score: 46/50 × 10 = 9.20**

---

### V-02 — C-32 single axis (Phase 6 SECTION SCOPE explicit enumeration)

**Mechanism**: Phase 6 SECTION SCOPE upgraded to three numbered content types: (1) GATE-EXCLUSION TEXT naming INERTIA-GATE, (2) PROPOSAL GENERATION, (3) ROW-LEVEL BIAS LABELING naming PROPOSAL BIAS AUDIT guard as enforcement mechanism, stating co-location explicitly, and adding auditor note: "A C-24 auditor verifying that row-level bias labeling belongs to Phase 6's declared scope finds it enumerated here." PROPOSAL BIAS AUDIT guard and CONTRACT unchanged from R13 V-05.

#### Essential / Recommended

All pass (same reasoning as V-01; structure preserved from R13 V-05).

#### Aspirational

C-09–C-30: FULL (2) = **44 raw points**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-31 PROPOSAL BIAS AUDIT guard** | **FAIL (0)** | Guard text reads "Bias blocked: motivated reasoning at individual proposal decision surface / Mechanism: Per-phase bias annotations (above) label the bias prevented by the entire phase structure. The 'Bias blocked by guard' column labels the bias prevented at the individual proposal row's decision point -- a separate failure mode not captured by phase-level annotations." Names only the row-level failure mode. Does not name SYSTEMIC PHASE STRUCTURE BIAS as the phase-level failure mode, and does not state "BOTH LEVELS ARE REQUIRED." Unchanged from R13 V-05. FAIL: guard does not distinguish the two failure modes by name or explain why both are required. |
| **C-32 Phase 6 SECTION SCOPE includes row-level bias labeling** | **FULL (2)** | SECTION SCOPE enumerates three content types with structural roles. Item (3) reads: "ROW-LEVEL BIAS LABELING: The PROPOSAL BIAS AUDIT guard (immediately below, co-located with the INERTIA-GATE at this phase entry boundary) enforces the 'Bias blocked by guard' column requirement. Per-row bias labeling is produced within this section at the individual proposal row level." Names enforcement mechanism, states co-location, distinguishes row-level from phase-level annotations. Ends with C-24 auditor guidance. Satisfies FULL condition: scope updated from pre-C-31 form, guard cross-reference present, co-location explicit. |
| **C-33 Output Schema CONTRACT** | **FAIL (0)** | CONTRACT is embedded annotation in Output Schema section (`[>> CONTRACT: ... <<]`), unchanged from R13 V-05. Same reasoning as V-01 C-33 FAIL. |

**V-02 raw: 44 + 0 + 2 + 0 = 46/50**
**V-02 score: 46/50 × 10 = 9.20**

---

### V-03 — C-33 single axis (standalone OUTPUT SCHEMA CONTRACT, earliest position)

**Mechanism**: Standalone `## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment` section placed before INERTIA COMPETITOR DECLARATION — absolute document-first position. Explicitly states "No file read instruction appears before this CONTRACT." CONTRACT A names all four sites (Phase 5 column, Phase 6a column, Phase 6b column, Phase 5 exit criterion). CONTRACT B names "Bias blocked by guard" with violation detection language: "A scorer detects a CONTRACT B column-absence violation from this block alone by checking whether the column name appears in the table header -- no phase content required." Embedded `[>> CONTRACT <<]` annotation in Output Schema section removed. PROPOSAL BIAS AUDIT guard and Phase 6 SECTION SCOPE unchanged from R13 V-05.

#### Essential / Recommended

All pass.

#### Aspirational

C-09–C-30: FULL (2) = **44 raw points**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-31 PROPOSAL BIAS AUDIT guard** | **FAIL (0)** | Guard text unchanged from R13 V-05. Names only row-level failure mode. No SYSTEMIC PHASE STRUCTURE BIAS, no "BOTH LEVELS ARE REQUIRED." FAIL for same reason as V-02. |
| **C-32 Phase 6 SECTION SCOPE** | **FAIL (0)** | SECTION SCOPE text reads "gate-exclusion text, proposal generation, and row-level bias labeling" — unchanged from R13 V-05 pre-C-31 form. No guard cross-reference. FAIL: unchanged from pre-C-31 form. Note: V-03's SECTION SCOPE says "Output Schema CONTRACT" instead of "Output Schema block" showing the V-03 pass forward, but the Phase 6 scope declaration does not enumerate a guard cross-reference for row-level bias labeling. |
| **C-33 Output Schema CONTRACT** | **FULL (2)** | Standalone named section `## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment` at absolute document-first position, before INERTIA COMPETITOR DECLARATION. States "This section appears at the document-first position, before any other structural content including the INERTIA COMPETITOR DECLARATION. No file read instruction appears before this CONTRACT." CONTRACT A names all four sites explicitly (Site 1–3 + exit criterion). CONTRACT B names "Bias blocked by guard" for both Phase 6a and 6b. Violation detection language present for both: "A scorer detects a CONTRACT A violation by comparing the actual string at any site to 'Consequence if unchanged' -- this comparison does not require reading surrounding prose or other sections." Both failures detectable from block alone. Satisfies FULL condition on all dimensions. |

**V-03 raw: 44 + 0 + 0 + 2 = 46/50**
**V-03 score: 46/50 × 10 = 9.20**

---

### V-04 — Combined C-31 + C-32 + C-33 (CONTRACT inside Output Schema, standard position)

**Mechanism**: V-01 guard upgrade (C-31) + V-02 SECTION SCOPE upgrade (C-32) + standalone `### OUTPUT SCHEMA CONTRACT` subsection inside the Output Schema block, before Phase 1 opens (C-33). CONTRACT positioned after phase schemas are shown but before Phase 1 instruction. States "Pre-execution commitment. This CONTRACT appears before Phase 1 opens and before any file read instruction."

#### Essential / Recommended

All pass.

#### Aspirational

C-09–C-30: FULL (2) = **44 raw points**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-31 PROPOSAL BIAS AUDIT guard** | **FULL (2)** | Guard at Phase 6 entry names LEVEL 1 (SYSTEMIC PHASE STRUCTURE BIAS) and LEVEL 2 (MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE) as distinct failure modes. States "BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against per-proposal motivated reasoning. The row-level column does not protect against systemic phase structure bias. These are distinct failure modes at distinct granularities." Ends with "This column is pre-committed in the OUTPUT SCHEMA CONTRACT above." Full C-31 pass. |
| **C-32 Phase 6 SECTION SCOPE** | **FULL (2)** | SECTION SCOPE enumeration mirrors V-02 with three numbered content types. Item (3) names PROPOSAL BIAS AUDIT guard as enforcement mechanism, states co-location, ends with "A C-24 auditor verifying that row-level bias labeling belongs to Phase 6's declared scope finds it enumerated here alongside gate-exclusion text and proposal generation." Full C-32 pass. |
| **C-33 Output Schema CONTRACT** | **FULL (2)** | Standalone `### OUTPUT SCHEMA CONTRACT` subsection inside Output Schema, after phase schemas, before Phase 1. States "Pre-execution commitment. This CONTRACT appears before Phase 1 opens and before any file read instruction. Both contract violations are detectable from this block alone without reading any phase." CONTRACT A names three C-29 sites + exit criterion. CONTRACT B names "Bias blocked by guard" for Phase 6a and 6b. Violation detection language present for both. Positioned before any file read. Satisfies FULL condition. Minor gap: CONTRACT is a subsection of Output Schema rather than a top-level standalone section — this is the "standard position" vs V-05's "pre-earliest position." Does not affect FULL pass under rubric. |

**V-04 raw: 44 + 2 + 2 + 2 = 50/50**
**V-04 score: 50/50 × 10 = 10.00**

---

### V-05 — Combined C-31 + C-32 + C-33 (CONTRACT pre-earliest; guard cross-references scope)

**Mechanism**: V-04 as base with two structural additions. (1) CONTRACT moved to absolute document-first position — before INERTIA COMPETITOR DECLARATION — as a top-level section (`## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment`). States "This block is the first content in the document. No file read instruction precedes this CONTRACT." (2) PROPOSAL BIAS AUDIT guard at Phase 6 entry explicitly cross-references the SECTION SCOPE: "See SECTION SCOPE above for co-location context. The SECTION SCOPE declares row-level bias labeling as a named content type of this section; this guard is the enforcement mechanism for that declared content type." Creates bidirectional chain: SECTION SCOPE → names row-level bias labeling → PROPOSAL BIAS AUDIT guard is enforcement → guard cites SECTION SCOPE.

#### Essential / Recommended

All pass.

#### Aspirational

C-09–C-30: FULL (2) = **44 raw points**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **C-31 PROPOSAL BIAS AUDIT guard** | **FULL (2)** | Guard opens with "See SECTION SCOPE above for co-location context" cross-reference. Then names LEVEL 1 (SYSTEMIC PHASE STRUCTURE BIAS) and LEVEL 2 (MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE) with same "BOTH LEVELS ARE REQUIRED" language as V-04. Closes with "This column is pre-committed in the OUTPUT SCHEMA CONTRACT (document-first position) and declared as a scope item in the SECTION SCOPE above." Bidirectional references: guard → scope and guard → CONTRACT. Exceeds C-31 Full requirement. |
| **C-32 Phase 6 SECTION SCOPE** | **FULL (2)** | SECTION SCOPE in V-05 adds a sentence V-04's SECTION SCOPE lacked: "The 'Bias blocked by guard' column -- pre-committed in the OUTPUT SCHEMA CONTRACT (document-first position) -- is the per-row output of this content type." This creates a three-way anchor: SECTION SCOPE names the content type → names its enforcement guard → names its output column → references the CONTRACT. A C-24 auditor checking Phase 6 scope finds row-level bias labeling declared and can trace it to guard → column → contract without leaving the Phase 6 block. FULL pass plus additional auditability. |
| **C-33 Output Schema CONTRACT** | **FULL (2)** | Standalone `## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment` as first section in document. States "This block is the first content in the document. No file read instruction precedes this CONTRACT." Closes with "This CONTRACT block is the authoritative pre-read commitment for both C-29 naming identity and C-30 bias column presence. Compliance verification requires only this block and the target site -- no phase traversal needed." CONTRACT A names all four sites. CONTRACT B names "Bias blocked by guard" with column-absence violation detection. Positioned at earliest possible point — before INERTIA COMPETITOR DECLARATION, before Output Schema, before Phase 1. Strongest possible C-33 pass. |

**V-05 raw: 44 + 2 + 2 + 2 = 50/50**
**V-05 score: 50/50 × 10 = 10.00**

---

### Score Summary

| Variation | C-31 | C-32 | C-33 | Base | Raw | Score |
|-----------|------|------|------|------|-----|-------|
| V-01 | 2 | 0 | 0 | 44 | 46/50 | 9.20 |
| V-02 | 0 | 2 | 0 | 44 | 46/50 | 9.20 |
| V-03 | 0 | 0 | 2 | 44 | 46/50 | 9.20 |
| V-04 | 2 | 2 | 2 | 44 | **50/50** | **10.00** |
| V-05 | 2 | 2 | 2 | 44 | **50/50** | **10.00** |

**Ranking**: V-04 = V-05 (tied at 10.00) > V-01 = V-02 = V-03 (tied at 9.20)

---

### Excellence Signals — V-05 (top variation, strongest audit chain)

V-05 achieves the same raw score as V-04 but introduces two structural patterns not present in any prior variation:

**1. Bidirectional guard–scope cross-reference**
The PROPOSAL BIAS AUDIT guard opens with "See SECTION SCOPE above for co-location context" and the SECTION SCOPE names the guard's output column with a reference to the CONTRACT. The audit chain runs in both directions: a scorer starting at the SECTION SCOPE can follow to the guard and then to the CONTRACT; a scorer starting at the guard can follow to the SECTION SCOPE for co-location confirmation. Each node anchors the other. This eliminates the possibility that either element exists without the other being traceable.

**2. Document-first CONTRACT positioning**
V-03 established standalone CONTRACT at document-first position. V-05 combines this with the full C-31/C-32 structure. The CONTRACT now appears before INERTIA COMPETITOR DECLARATION — the absolute first content the model encounters. This means CONTRACT violations are detectable before any structural framing has been read, maximizing the pre-commitment effect the criterion was designed to achieve.

**3. Three-way scope-guard-contract anchor** (new in V-05, not present in V-04)
SECTION SCOPE item (3) names: (a) the content type ("row-level bias labeling"), (b) its enforcement mechanism (PROPOSAL BIAS AUDIT guard), (c) its output column ("Bias blocked by guard"), and (d) its upfront commitment ("pre-committed in the OUTPUT SCHEMA CONTRACT"). A single SECTION SCOPE item now closes the entire audit loop for this content type.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["bidirectional guard-scope cross-reference: guard cites scope for co-location context, scope names guard output column and references CONTRACT, creating a closed three-way audit chain", "document-first CONTRACT positioning combined with full C-31/C-32 structure: CONTRACT appears before INERTIA COMPETITOR DECLARATION, before any structural framing, maximizing pre-commitment detectability"]}
```
