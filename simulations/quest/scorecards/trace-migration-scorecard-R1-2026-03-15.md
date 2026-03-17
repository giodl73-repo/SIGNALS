## trace-migration — Round 1 Scoring

**Rubric:** v1 (C-01 through C-10) | **Date:** 2026-03-15
**Artifact:** placeholder (structural-guarantee analysis only)

---

### Scoring Key

| Tier | Criteria | Points Each |
|------|----------|------------|
| Essential | C-01–C-05 | 12 pts each |
| Recommended | C-06–C-08 | 10 pts each |
| Aspirational | C-09–C-10 | 5 pts each |

PARTIAL = half points. All-essential-pass requires C-01 through C-05 all PASS. Golden = all essential pass + composite >= 80.

---

### Per-Variation Criterion Scores

#### V-01 — Role Sequence (Operations-first)

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 Entity enumeration | **PASS (12)** | Operations produces locked ENTITY REGISTRY before domain roles run; domain roles must flag gaps, cannot silently skip |
| C-02 Before/after state | **PASS (12)** | FIELD 1 (before) and FIELD 3 (after) are discrete named fields per entity; merge structurally prevented |
| C-03 Migration action tracing | **PASS (12)** | FIELD 2 accepts only approved-verb DDL/DML list; "column changes" fails admission |
| C-04 Data loss path identification | **PASS (12)** | FIELD 4 is mandatory per entity; silence on data loss is an explicit failure condition |
| C-05 Constraint violation identification | **PASS (12)** | FIELD 5 is mandatory per entity |
| C-06 Default value gap analysis | **PASS (10)** | DEFAULT VALUE ANALYSIS field per entity |
| C-07 Performance cliff identification | **PASS (10)** | PERFORMANCE CLIFF field per entity |
| C-08 Reversibility assessment | **PASS (10)** | REVERSIBILITY VERDICT field per entity |
| C-09 Cross-entity dependency cascade | **PARTIAL (2)** | Dedicated cascade section exists but no minimum-trace count enforcement; one shallow entry passes |
| C-10 Quantified risk scoring | **PASS (5)** | RISK REGISTER with severity + likelihood + remediation fields |

**V-01 Total: 97** | All essential: YES | Golden: YES

---

#### V-02 — Output Format (Table-first)

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 Entity enumeration | **PASS (12)** | TABLE 1 ENTITY REGISTRY — empty row is visually obvious in a table; missing prose section is not |
| C-02 Before/after state | **PASS (12)** | TABLE 2 (BEFORE STATE) and TABLE 4 (AFTER STATE) as structurally separate tables |
| C-03 Migration action tracing | **PASS (12)** | TABLE 3 OPERATION column accepts only named DDL/DML verbs |
| C-04 Data loss path identification | **PASS (12)** | Dedicated TABLE 5 with per-entity rows; empty table is visible |
| C-05 Constraint violation identification | **PARTIAL (6)** | Coverage map assigns both after-state (C-02) and constraint violations (C-05) to "TABLE 4" — numbering collision creates ambiguity; likely TABLE 6 for constraints but not explicit in design notes |
| C-06 Default value gap analysis | **PASS (10)** | TABLE 5 (or downstream table) |
| C-07 Performance cliff identification | **PASS (10)** | TABLE 6 |
| C-08 Reversibility assessment | **PASS (10)** | TABLE 7 |
| C-09 Cross-entity dependency cascade | **PARTIAL (2)** | TABLE 8 exists; no minimum-trace enforcement |
| C-10 Quantified risk scoring | **PASS (5)** | TABLE 9 with structured risk entries |

**V-02 Total: 91** | All essential: NO (C-05 PARTIAL) | Golden: YES (composite >= 80, but not all-essential-pass)

---

#### V-03 — Lifecycle Emphasis (Phase gates)

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 Entity enumeration | **PASS (12)** | INVENTORY PHASE 1 gate with coverage floor; phase cannot close until entity list is verified complete |
| C-02 Before/after state | **PASS (12)** | PHASE 2 (BEFORE STATE) and PHASE 3 (AFTER STATE) are sequentially separate; temporal blur between phases is architecturally blocked |
| C-03 Migration action tracing | **PASS (12)** | TABLE 3 appears in PHASE 2 with named-operation requirement |
| C-04 Data loss path identification | **PASS (12)** | TABLE 5 in PHASE 4; phase gate cannot open without data-loss analysis present |
| C-05 Constraint violation identification | **PASS (12)** | TABLE 6 in PHASE 4 with same gate enforcement |
| C-06 Default value gap analysis | **PASS (10)** | TABLE 7 in PHASE 4 |
| C-07 Performance cliff identification | **PASS (10)** | TABLE 8 in PHASE 4 |
| C-08 Reversibility assessment | **PASS (10)** | TABLE 9 in PHASE 4 |
| C-09 Cross-entity dependency cascade | **PARTIAL (2)** | TABLE 10 in PHASE 5; PHASE 5 gate exists but no minimum two-trace enforcement |
| C-10 Quantified risk scoring | **PASS (5)** | TABLE 11 in PHASE 5 |

**V-03 Total: 97** | All essential: YES | Golden: YES

---

#### V-04 — Role Sequence + Phrasing Register

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 Entity enumeration | **PASS (12)** | DIRECTIVE A-1 prohibits domain roles from omitting entities without domain owners; REGISTRY GAP — halt protocol forces Operations acknowledgment |
| C-02 Before/after state | **PASS (12)** | FIELD 1 / FIELD 3 with DIRECTIVE-capitalized imperatives; compliance is spot-checkable by a reader |
| C-03 Migration action tracing | **PASS (12)** | FIELD 2 DIRECTIVE names disallowed phrases explicitly: "MODIFIED is not an approved verb"; approved-verb list is enumerated |
| C-04 Data loss path identification | **PASS (12)** | FIELD 4 DIRECTIVE includes explicit silence clause: no data-loss analysis = automatic failure, stated in the prompt |
| C-05 Constraint violation identification | **PASS (12)** | FIELD 5 DIRECTIVE names violation types: nullable, unique, check — coverage is enumerated, not assumed |
| C-06 Default value gap analysis | **PASS (10)** | DIRECTIVE per field with semantic-correctness requirement |
| C-07 Performance cliff identification | **PASS (10)** | PERFORMANCE SUMMARY required per role; annotated with risk level |
| C-08 Reversibility assessment | **PASS (10)** | REVERSIBILITY field in per-role summary |
| C-09 Cross-entity dependency cascade | **PASS (5)** | DIRECTIVE D-1/D-2 enforces minimum **two** end-to-end cascade traces; single-entry outputs fail admission |
| C-10 Quantified risk scoring | **PASS (5)** | DIRECTIVE E-1/E-2 with CRITICAL severity enforcement; structured three-field requirement stated |

**V-04 Total: 100** | All essential: YES | Golden: YES

---

#### V-05 — Role Sequence + Output Format + Lifecycle Emphasis

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 Entity enumeration | **PASS (12)** | Triple enforcement: TABLE 1 visual anchor + PHASE 1 gate + Operations-first substrate; entity surviving one omission mechanism caught by another two |
| C-02 Before/after state | **PASS (12)** | TABLE 2 / TABLE 4 as separate tables + PHASE 2/3 gate separation |
| C-03 Migration action tracing | **PASS (12)** | TABLE 3 + PHASE 2 gate; named-verb enforcement |
| C-04 Data loss path identification | **PASS (12)** | TABLE 5 + PHASE 4 gate |
| C-05 Constraint violation identification | **PASS (12)** | TABLE 6 + PHASE 4 gate; V-03 table numbering resolves V-02's TABLE 4 collision |
| C-06 Default value gap analysis | **PASS (10)** | TABLE 7 + PHASE 4 gate |
| C-07 Performance cliff identification | **PASS (10)** | TABLE 8 + PHASE 4 gate |
| C-08 Reversibility assessment | **PASS (10)** | TABLE 9 + PHASE 4 gate |
| C-09 Cross-entity dependency cascade | **PARTIAL (2)** | TABLE 10 + PHASE 5 gate but no minimum-two-traces enforcement (V-04's DIRECTIVE language is not part of this combination — V-05 uses V-01+V-02+V-03 axes only) |
| C-10 Quantified risk scoring | **PASS (5)** | TABLE 11 + inertia frame close; inertia frame adds migration recommendation per dimension |

**V-05 Total: 97** | All essential: YES | Golden: YES

---

### Rankings

| Rank | Variation | Score | All Essential | Golden | Key Differentiator |
|------|-----------|-------|--------------|--------|-------------------|
| 1 | **V-04** | **100** | YES | YES | DIRECTIVE enforcement with minimum-count for C-09; disallowed-phrase naming |
| 2 | **V-01** | **97** | YES | YES | Locked registry contract; domain roles cannot filter silently |
| 2 | **V-03** | **97** | YES | YES | Phase gates with coverage floors prevent temporal blur |
| 2 | **V-05** | **97** | YES | YES | Triple-layer redundancy resolves V-02 table numbering flaw |
| 5 | **V-02** | **91** | NO | YES | Table-first is visually obvious but TABLE 4 numbering collision breaks C-05 |

---

### Excellence Signals — V-04

**What made V-04 the only 100-point variation:**

1. **Minimum-count enforcement closes aspirational gap.** C-09 is the only criterion where every other variation scores PARTIAL. DIRECTIVE D-1/D-2 resolves this by requiring at least two named end-to-end cascade traces — not "a cascade section exists" but a countable floor. This is the structural insight: aspirational criteria fail not because the topic is absent but because no floor prevents shallow compliance.

2. **Named disallowed phrases make failures checkable without execution.** "MODIFIED is not an approved verb" is a stronger constraint than "use DDL verbs" — a reviewer can verify compliance by grep. Abstract approval lists allow edge-case hedging; explicit rejection lists do not.

3. **Explicit silence clauses convert omission into detectable failure.** "No data-loss analysis = automatic failure, stated in the prompt" means a model cannot satisfy the rubric by simply not mentioning data loss. Every other variation flags this as required but does not name the failure mode explicitly. The silence clause converts absence from a neutral state into a scored error.

4. **REGISTRY GAP — halt protocol removes the domain-filter omission path.** Finance and Commerce have natural incentives to stay in their domain. An instruction to "flag gaps" is weaker than a halt instruction: halt forces the entity back to Operations for registration before any domain analysis proceeds.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["minimum-count floor for aspirational criteria (DIRECTIVE D-1/D-2 enforces >= 2 traces, not just presence of section)", "named disallowed phrases outperform abstract approval lists — rejection lists are grep-checkable", "explicit silence clauses convert omission from neutral state to scored failure", "halt protocol stronger than flag protocol for domain-filter omission paths"]}
```
