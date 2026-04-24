## Round 11 — Scoring Scorecard: topic-plan (v11 rubric, C-01–C-39)

---

### Essential Criteria (C-01 – C-05)

All five variations share the same essential structure. Evaluated once.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Read strategy.md | PASS | PASS | PASS | PASS | PASS |
| C-02 | Signal inventory (9 namespaces) | PASS | PASS | PASS | PASS | PASS |
| C-03 | Delta detection / NEW vs PRIOR | PASS | PASS | PASS | PASS | PASS |
| C-04 | Typed change proposals (ADD/REMOVE/REPRIORITIZE) | PASS | PASS | PASS | PASS | PASS |
| C-05 | Confirmation gate (YES/NO/REVISED) | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 for all variations → 60 pts each.**

---

### Recommended Criteria (C-06 – C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Evidence citation in proposal rows | PASS | PASS | PASS | PASS | PASS |
| C-07 | Before/After diff structure | PASS | PASS | PASS | PASS | PASS |
| C-08 | Inertia justification column | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 for all variations → 30 pts each.**

---

### Aspirational Criteria (C-09 – C-39)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Type-labeled null declarations | PASS | PASS | PASS | PASS | PASS |
| C-10 | Conflict detection with typed null | PASS | PASS | PASS | PASS | PASS |
| C-11 | Required-cell table schemas | PASS | PASS | PASS | PASS | PASS |
| C-12 | In-phase stop gates (EXIT slot) | PASS | PASS | PASS | PASS | PASS |
| C-13 | Mandatory column enforcement ([MANDATORY] label) | PASS | PASS | PASS | PASS | PASS |
| C-14 | Explicit placeholder tokens (??) | PASS | PASS | PASS | PASS | PASS |
| C-15 | Counted-total delta summary sentence | PASS | PASS | PASS | PASS | PASS |
| C-16 | Hedge-phrase disqualification | PASS | PASS | PASS | PASS | PASS |
| C-17 | Two-tier sentinel vocabulary (?? vs --) | PASS | PASS | PASS | PASS | PASS |
| C-18 | Pre-signal defense register | PASS | PASS | PASS | PASS | PASS |
| C-19 | Integer-enforcement gate language | PASS | PASS | PARTIAL | PARTIAL | PASS |
| C-20 | Sequential phase-linked stop gates | PASS | PASS | PASS | PASS | PASS |
| C-21 | Vocabulary contract violation enumeration | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-22 | Row-number anchor citation | PASS | PASS | PASS | PASS | PASS |
| C-23 | Verbatim-quoted banned forms | PASS | PASS | PASS | PASS | PASS |
| C-24 | Cell-level banned-forms check instruction | PASS | PASS | PASS | PASS | PASS |
| C-25 | Banned-forms scope propagation (null cells) | PASS | PASS | PASS | PASS | PASS |
| C-26 | Gate-0 pre-signal stop gate | PASS | PASS | PASS | PASS | PASS |
| C-27 | Write-surface enforcement completeness | PASS | PASS | PASS | PASS | PASS |
| C-28 | Write-surface blocks as first-class section headers | PASS | PASS | PASS | PASS | PASS |
| C-29 | Write-surface register (upfront table) | PASS | PASS | PASS | PASS | PASS |
| C-30 | Register-milestone linkage (WS-N fulfills Row N) | PASS | PASS | PASS | PASS | PASS |
| C-31 | Named phase lifecycle template (ENTRY/JOB/EXIT) | PASS | PASS | PASS | PASS | PASS |
| C-32 | Artifact-to-register calibration column | PASS | PASS | PASS | PASS | PASS |
| C-33 | Inverted artifact sequence with upfront calibration | PASS | PASS | PASS | PASS | PASS |
| C-34 | Compound audit structure (spine + lifecycle) | PASS | PASS | PASS | PASS | PASS |
| C-35 | Upfront table schema register | PASS | PASS | PASS | PASS | PASS |
| C-36 | Schema-phase lifecycle elevation (Phase -1 with ENTRY/JOB/EXIT) | PASS | PASS | PASS | PASS | PASS |
| C-37 | Per-schema breach conditions (inline per schema block) | PASS | PASS | PASS | PASS | PASS |
| C-38 | Schema-phase gate in sequential chain (Gate-S before Gate-0) | PASS | PASS | PASS | PASS | PASS |
| C-39 | Modal obligation language (SHALL/SHALL NOT at 4+ sites) | PARTIAL | PASS | FAIL | PASS | PASS |

---

### Evidence Notes on Contested Criteria

**C-19 (V-03, V-04 — PARTIAL):** BANNED FORMS list names `"a few artifacts"`, `"several artifacts"`, `"some signals"` individually, and violation taxonomy / vocabulary contract labels non-integer count a gate failure. However, C-19 requires the gate-failure rule itself to name the specific forms inline — both variations split the named forms and the gate-failure label into separate blocks rather than a unified rule statement. PARTIAL.

**C-21 (V-01, V-02, V-04 — PARTIAL):** Vocabulary contract blocks define ?? and -- correctly, list verbatim BANNED FORMS, and have integer-enforcement language — but do not enumerate named violation conditions (e.g., "blank cell where ?? is required = inadmissibility violation") as a typed taxonomy. V-03 adds a `Violation taxonomy` section within the contract; V-05 does the same with category labels (vocabulary violation, integer-enforcement gate failure, schema contract breach). V-01/V-02/V-04 have per-schema BREACH CONDITIONS but not an equivalent taxonomy inside the vocabulary contract block itself.

**C-39 (V-01 — PARTIAL):** V-01 uses lowercase `must` / `must not` at 4+ critical sites (gate conditions, schema constraints, integer enforcement). C-39 accepts MUST/MUST NOT but requires lexically formal modal register distinguishable from advisory guidance. V-01's informal prose `must` is borderline — not SHALL/SHALL NOT, not capitalized MUST NOT. PARTIAL.

**C-39 (V-03 — FAIL):** V-03 uses predominantly imperative enforcement language (`Do not advance`, `Halt here`, `may not begin`) and `PROHIBITED` markers. `PROHIBITED` is a constraint adjective, not a modal verb. One `may not` at Gate-S. Fewer than four distinct constraint sites carry formal modal forms. FAIL.

**V-05 unique structure:** `CROSS-SCHEMA DEPENDENCY` declared as an explicit named Phase -1 contract term (lines 1402–1406), with Schema C in Phase 1 noting the constraint is "inherited from Phase -1 declaration, not invented here" (line 1553). Three-path audit (Schema Spine / Write-Surface Spine / Lifecycle Slots) vs. two-path in C-34.

---

### Score Computation

| | Essential | Recommended | Aspirational PASS | Aspirational PARTIAL | Score |
|--|-----------|-------------|-------------------|----------------------|-------|
| **V-01** | 5/5 → 60 | 3/3 → 30 | 29 | 2 | **99.4** |
| **V-02** | 5/5 → 60 | 3/3 → 30 | 30 | 1 | **99.7** |
| **V-03** | 5/5 → 60 | 3/3 → 30 | 29 | 1 + 1 FAIL | **99.4** |
| **V-04** | 5/5 → 60 | 3/3 → 30 | 29 | 2 | **99.4** |
| **V-05** | 5/5 → 60 | 3/3 → 30 | 31 | 0 | **100.0** |

*Aspirational formula: (PASS count / 31) × 10. PARTIAL = 0 for scoring.*

V-01: 90 + (29/31 × 10) = 90 + 9.35 = **99.4**
V-02: 90 + (30/31 × 10) = 90 + 9.68 = **99.7**
V-03: 90 + (29/31 × 10) = 90 + 9.35 = **99.4** *(note: 1 FAIL + 1 PARTIAL vs. 0 FAIL + 2 PARTIAL)*
V-04: 90 + (29/31 × 10) = 90 + 9.35 = **99.4**
V-05: 90 + (31/31 × 10) = 90 + 10.0 = **100.0**

---

### Ranking

| Rank | Variation | Score | Axis | Differentiator |
|------|-----------|-------|------|----------------|
| 1 | **V-05** | **100.0** | Modal + Table Schemas | All 31 aspirational PASS; violation taxonomy + explicit integer rule + full SHALL saturation |
| 2 | **V-02** | **99.7** | Phrasing register (modal) | C-21 PARTIAL only; 30/31 |
| 3 | **V-04** | **99.4** | Lifecycle + Inertia | C-19 and C-21 PARTIAL; two-dimensional BREACH CONDITIONS |
| 3 | **V-01** | **99.4** | Lifecycle emphasis | C-21 and C-39 PARTIAL; strongest ENTRY/JOB/EXIT explicitness |
| 3 | **V-03** | **99.4** | Inertia framing | C-19 PARTIAL, C-39 FAIL; strongest inertia chain-of-custody framing |

---

### Excellence Signals (from V-05)

**What made V-05 the top scorer:**

1. **Cross-schema dependency as a named Phase -1 contract term** — V-05 declares a `CROSS-SCHEMA DEPENDENCY` block in Phase -1 JOB (not in Phase 4), explicitly labeling it a "Phase -1 contract term." Phase 4 then cites "Phase -1 cross-schema dependency — inherited from Phase -1, not invented here." This creates a formal inheritance relationship: the ordering constraint has an upstream origin that downstream phases acknowledge rather than rediscover. No existing criterion captures this; C-33 covers the ordering constraint itself but not the upstream-contract-term framing.

2. **Violation taxonomy with typed error categories** — V-05 enumerates violations under three named categories: `vocabulary violation`, `integer-enforcement gate failure`, `schema contract breach`. This is more precise than V-03's `inadmissibility violation` taxonomy, which uses a single category for all constraint types. Typed categories make the error space partitioned and independently auditable per category.

3. **Three-path audit system (Schema Spine + Write-Surface Spine + Lifecycle Slots)** — V-05 adds a third audit path (PATH 1: count schema blocks in Phase -1; PATH 2: count WS headers; PATH 3: scan EXIT slots) vs. the two-path C-34 requirement. The schema spine path is new: a reviewer can verify schema completeness purely by counting named schema sections in Phase -1, without reading any phase content.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Cross-schema Cal ordering constraint declared as a named Phase -1 contract term with explicit downstream inheritance citation (Phase 4 notes the constraint is 'inherited from Phase -1, not invented here'), creating a formal upstream origin for inter-schema ordering obligations", "Three-path audit system that adds Schema Spine (count named schema blocks in Phase -1) as a third independent audit path beyond the two-path compound audit structure required by C-34, making schema completeness verifiable by block count alone without reading phase content"]}
```
