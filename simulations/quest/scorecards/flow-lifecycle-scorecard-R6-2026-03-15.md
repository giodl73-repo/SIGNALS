Now I have the full R5 V-01 through V-05 text. Let me score the R6 variations with precision.

Key facts from R5 source file:
- R5 V-01: 3 gates (role registry, phase table, artifact), no Handler column, no failure declaration
- R5 V-02: 1 gate, has Y/N column + Handler column + Terminal Verification Scan (per-path), no failure declaration
- R5 V-03: 1 gate, prose Owner field, Terminal Verification Scan Step 12, **gate has "is a structural fail -- and it must be discarded"** (passes C-22 AND C-24 incidentally)
- R5 V-05: 4 gates, Handler column, failure declaration ("structural fail -- must be discarded"), Y/N column

---

## flow-lifecycle — Round 6 Scoring

**Rubric version:** v6 (C-01 through C-24, 16 aspirational denominator)

---

### Baseline Assessment

All five R6 variations inherit the R5 schema infrastructure. Criteria that are structurally enforced and stable across all variations:

| Criterion | All V-01 through V-05 | Evidence |
|-----------|----------------------|---------|
| C-01 State Transition Coverage | PASS | State Table schema enforces ≥6 states with entry/exit triggers; "then X happens" blocked by column header inline rules (V-05 carries most explicit enforcement) |
| C-02 Exception Flow Traces | PASS | Exception Catalog enforces ≥3 exceptions with trigger/divergence/recovery path or terminal |
| C-03 Terminal State Completeness | PASS | Terminal Declaration table (inherited from R5 V-01/V-02/V-05); Exception Catalog Recovery/Terminal column references T-IDs; Scan Tables A and B verify closure |
| C-04 Bottleneck and Gap Identification | PASS | Bottleneck and Gap Table requires B-01, B-02 (bottleneck type, cause, impact) and G-01 (missing step + consequence) |
| C-05 Domain Role Assignment | PASS | Role Registry with inline anti-pattern ("Approver/Owner/Manager are fails"); every decision gate and exception must cite R-ID |
| C-06 Parallel Path Table | PASS | Parallel Path Table with Fork, Branch A/B, Join Condition, Join Owner, Downstream S-ID present in all variations |
| C-07 Decision Point Explicitness | PASS | Decision Table: condition, owner R-ID, Branch A, Branch B, Fallback — all columns present; 3-decision minimum enforced |
| C-08 Edge Case Enumeration | PASS | Edge Case Table enforces ≥2 EC-IDs with scenario, gap reason, consequence |
| C-09 Cross-Lifecycle Dependencies | PASS | Cross-Lifecycle Dependency table present |
| C-10 SLA and Timing Annotation | PASS | State Table has SLA Window and Risk columns; Phase Table has SLA Envelope and At-Risk Threshold |
| C-11 Role-First Anchoring | PASS | Role Registry section is always first; column header includes concrete domain-title examples anchoring vocabulary |
| C-12 Anti-Pattern Negation | PASS | Role Name column header names concrete failures ("Approver," "Owner," "Finance team") with explicit counter-examples; minimum one inline anti-pattern with no-inference evidence |
| C-13 Sequential Gate Locking | PASS | All variations have ≥1 "do not proceed until" gate; V-01/V-04/V-05 have Gate 1 with explicit section-locking syntax |
| C-14 Terminal Verification Pass | PASS | All variations carry per-path terminal scan from R5 (Scan Table A per-state + Scan Table B per-exception, or equivalent Step 12 terminal verification scan); each row is per-path structural confirmation, not a count |
| C-15 Decision Fallback Coverage | PASS | Decision Table Fallback column is mandatory; column header syntax in V-05 makes blank a structural fail |
| C-16 Phase-Layer Structural Framing | PASS | Phase Table above state trace; ≥4 phases, each aggregating ≥2 states; At-Risk Threshold column names causal bottleneck |
| C-17 Quantified Decision Boundaries | PASS | Decision Table condition column enforces measurable thresholds ("dollar amount, day count, retry limit; 'needs review' does not count"); minimum 3 decisions |
| C-18 Schema-Inline Anti-Pattern Placement | PASS | Role Name column header carries inline negation at point of use; Exception Handler / Handler column carries inline mandatory rule; ≥2 inline negation locations in all variations |
| C-19 Artifact-Level Production Gate | PASS | All variations include a production gate blocking artifact write until Scan Summary is CLOSED; gate names scan artifact and required status condition |
| C-21 Exception Flow Handling Role | PASS | Exception Catalog includes Handler (R-ID) column (V-01/V-03/V-04/V-05) or prose Owner field (V-02); no exception path leaves ownership unassigned; handler field is present and labeled |

---

### Differentiating Criteria

These four criteria split the variations:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-20** Per-Step Sequential Gate Coverage (≥3 boundaries) | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **C-22** Production Gate Failure Declaration | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-23** Exception Handler Authority Pre-Certification | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** |
| **C-24** Gate Violation Remediation Instruction | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |

**C-20 evidence per variation:**

- **V-01**: Gate 1 (role registry → phase table) + production gate = 2 gates. Hypothesis confirms: "one gate before the phase table, one gate before the artifact write." C-20 requires ≥3 at distinct section boundaries. FAIL.
- **V-02**: Inherits R5 V-03 step-numbered format. R5 V-03 had only the Step 12/13 production gate — 1 gate. C-20 FAIL.
- **V-03**: Inherits R5 V-02 structure — 1 gate (production only). C-20 FAIL.
- **V-04**: Combines V-01 (2 gates) + V-02 (1 gate). Combination preserves 2 gates (role registry + production); no third gate is added by either axis. C-20 FAIL.
- **V-05**: "Full C-18 through C-22 carry-through" explicitly addresses C-20. Inherits R5 V-05's 4 gates: Gate 1 (role registry → phase table), Gate 2 (phase table → state table), Gate 3 (exception catalog → terminals), Gate 4 (scan summary → artifact). Each names section locked and unlocked. C-20 PASS.

**C-22 / C-24 evidence per variation:**

- **V-01 (C-22 FAIL)**: Hypothesis explicit — "production gate states the CLOSED requirement without naming a remediation action." Gate text: condition only. No "is a structural fail."
- **V-01 (C-24 FAIL)**: Hypothesis explicit — "C-24 is absent." No remediation instruction.
- **V-02 (C-22 PASS)**: Inherits R5 V-03's gate declaration. R5 V-03: "Writing the artifact when Scan Summary is OPEN is a structural fail." Inline failure consequence present.
- **V-02 (C-24 PASS)**: R5 V-03 gate includes "and it must be discarded." R6 V-02 is the C-24 axis — this language is its defining feature. PASS.
- **V-03 (C-22/C-24 FAIL)**: Inherits R5 V-02 structure. R5 V-02 gate: "Artifact may not be written until Scan Summary shows status CLOSED." Condition only — no failure declaration, no remediation instruction.
- **V-04 (C-22 PASS, C-24 PASS)**: Combines V-01 (C-23) and V-02 (C-22 + C-24) axes. The V-02 gate phrasing carries into V-04.
- **V-05 (C-22 PASS, C-24 PASS)**: Gate 4 inherits R5 V-05: "Writing the artifact when Scan Summary is OPEN is a structural fail -- it produces an incomplete lifecycle trace where at least one path has no named terminal, and that artifact must be discarded." Full C-22 + C-24 pass.

**C-23 evidence per variation:**

- **V-01 (PASS)**: Role Registry carries Exception Handler Y/N column. Exception Catalog preamble states: "every Handler (R-ID) cell below must resolve to a role with Exception Handler = Y in the registry. A Handler R-ID that traces to a role marked N is a structural fail." Backward direction enforced explicitly.
- **V-02 (FAIL)**: Inherits R5 V-03's prose exception format. No Y/N column in Role Registry. Handler is a prose "Owner: [R-ID]" field pointing to registry, but no pre-certification column exists at the registry level. Backward verification not possible.
- **V-03 (PASS)**: Output format axis — the backward trace rule is embedded inline in the Handler column header itself (not in a preamble block). Column header: "Must trace to a role with Exception Handler = Y in the Role Registry." Inline enforcement at point of use. C-23 PASS via schema-header placement.
- **V-04 (PASS)**: Combines V-01's Y/N column and backward enforcement with V-02's gate phrasing.
- **V-05 (PASS)**: Inherits Y/N column from R5 V-05 Role Registry plus R6 V-01/V-03 backward trace enforcement.

---

### Score Computation

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/16 * 10)
```

| | Essential (5) | Recommended (3) | Aspirational (16) | Score |
|-|---------------|-----------------|-------------------|-------|
| **V-01** | 5/5 = 60 | 3/3 = 30 | 13/16 = 8.1 | **98.1** |
| **V-02** | 5/5 = 60 | 3/3 = 30 | 14/16 = 8.75 | **98.75** |
| **V-03** | 5/5 = 60 | 3/3 = 30 | 13/16 = 8.1 | **98.1** |
| **V-04** | 5/5 = 60 | 3/3 = 30 | 15/16 = 9.375 | **99.4** |
| **V-05** | 5/5 = 60 | 3/3 = 30 | 16/16 = 10 | **100** |

Aspirational fail breakdown:
- V-01: FAIL C-20, C-22, C-24 (13/16)
- V-02: FAIL C-20, C-23 (14/16)
- V-03: FAIL C-20, C-22, C-24 (13/16)
- V-04: FAIL C-20 only (15/16)
- V-05: no fails (16/16)

All five variations: all essential PASS, composite ≥ 80. All are golden-threshold eligible.

---

### Ranking

| Rank | Variation | Score | Fails |
|------|-----------|-------|-------|
| 1 | **V-05** | 100 | none |
| 2 | **V-04** | 99.4 | C-20 |
| 3 | **V-02** | 98.75 | C-20, C-23 |
| 4 | **V-01** | 98.1 | C-20, C-22, C-24 |
| 4 | **V-03** | 98.1 | C-20, C-22, C-24 |

**Axis asymmetry note**: The C-24 axis (V-02) outscores the C-23 axis (V-01, V-03) by 0.625 points because the C-24 package includes C-22 as a prerequisite — two aspirational criteria pass when C-24 is present, versus one when only C-23 is present. The C-23 axis is a single criterion; the C-24 axis is a two-criterion unlock.

**V-01 vs V-03**: Tied at 98.1. Both fail C-20, C-22, C-24 and pass C-23. The distinction is _how_ C-23 is achieved: V-01 uses a preamble block before the exception catalog; V-03 embeds the backward trace rule inline in the Handler column header (point-of-use placement). Neither approach changes the criterion score under the current rubric, but V-03's placement produces a stronger C-18 compliance signal — the inline enforcement appears adjacent to the cell being constrained, not in a prior block that can be skimmed.

---

### Excellence Signals from V-05

**Signal 1 — Four-gate saturation enabling C-20 PASS**
V-05 inherits R5 V-05's four-gate structure: Gate 1 (role registry → phase table), Gate 2 (phase table → state table), Gate 3 (exception catalog → terminals), Gate 4 (scan summary → artifact). Each gate names the section it locks and the section it unlocks. V-01 through V-04 plateau at 2 gates; V-05 is the first R6 variation to satisfy C-20 because the gate distribution spans the full schema, not just the endpoints. The third gate (exception catalog → terminals) is structurally significant: it forces handler completeness before terminal states are declared, creating a mid-schema checkpoint that earlier variations skipped.

**Signal 2 — Gate dependency ladder fully satisfied**
V-05 is the first variation to satisfy all five gate-related criteria simultaneously: C-13 (≥1 gate with "do not proceed" syntax), C-19 (artifact-level production gate), C-20 (≥3 gates at distinct section boundaries), C-22 (inline failure consequence in production gate), and C-24 (inline remediation instruction in production gate). The chain C-13 → C-19 → C-20 → C-22 → C-24 is a dependency ladder where each criterion is unreachable without the prior. V-05 reaching the end of that ladder means every gate mechanism works: a gate exists, it's distributed, it declares its failure consequence, and it specifies what to do with the violating artifact.

**Signal 3 — Backward trace + inline column enforcement**
V-05 combines the V-01/V-03 backward trace enforcement approaches: the Role Registry Y/N column pre-certifies handler authority, and the Exception Catalog Handler column header carries an inline constraint ("must trace to Exception Handler = Y"). This creates two enforcement sites for the same constraint — registry pre-certification and catalog column header — ensuring both the registry-side declaration and the catalog-side constraint are visible without relying on the author to read a preamble.

**New pattern candidate for C-25**: _Certified-Handler Assignment Coverage_. C-23 constrains the exception catalog to cite only Y-marked roles (forward direction: catalog → registry). The inverse is not yet required: that every Y-marked role in the registry must appear in at least one exception flow. A registry can have 3 Y-marked roles with only 1 referenced in the catalog — the other 2 are pre-certified but never assigned. A C-25 criterion would close this gap by requiring the exception catalog to reference each Y-marked role at least once, making the authorization and the assignment bidirectionally complete.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Certified-Handler Assignment Coverage: every role marked Exception Handler = Y in the Role Registry must appear as Handler in at least one exception flow — C-23 constrains the catalog to cite only Y-marked roles (forward direction); the inverse constraint (all Y-marked roles must be assigned at least once) would close the orphaned-authorization gap where a role is pre-certified for exception handling but never used"]}
```
