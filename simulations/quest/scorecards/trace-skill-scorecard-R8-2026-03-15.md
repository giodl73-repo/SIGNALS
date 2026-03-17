## trace-skill Variations R8 — Scorecard (Rubric v7)

### Scoring Basis

All five variations explicitly inherit the full R7 V-04 architecture, which achieved C-01 through C-26 PASS. The R8 rubric adds three new aspirational criteria (C-27, C-28, C-29), raising the aspirational denominator from 18 to 21. Scores below treat C-01–C-26 as inherited PASS and evaluate each variation only for the new axes.

---

### V-01 — Single axis: C-27 (RequiredVocabulary type declaration)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Stage 1 / Phase 1 Setup / Phase 2 Execute / Verdict in sequence |
| C-02 | PASS | Stage 1 enumerates SA/SG/EG gaps with source attribution |
| C-03 | PASS | Phase 1 Setup binds all carry-forward values by name |
| C-04 | PASS | Phase 2 Execute produces `{topic}-skill-trace-{date}.md` with required sections |
| C-05 | PASS | Verdict compliance ledger declares PASS/FAIL per VC row with site evidence |
| C-06 | PASS | Phase headers follow Coverage Matrix schema label convention |
| C-07 | PASS | Verdict ledger rows cite VC-1 through VC-5 by ID |
| C-08 | PASS | No elision markers — all relay and artifact fields fully specified |
| C-09–C-26 | PASS ×18 | Inherited from R7 V-04 (Coverage Matrix, BLOCKED declaration, relays, compliance ledger, C-14/C-15/C-16/C-17/C-18/C-19/C-20/C-21/C-22/C-23/C-24/C-25/C-26 all present) |
| **C-27** | **PASS** | `RequiredVocabulary` declared as closed type `{YES, VIOLATION}` before relay schema table; column header is `Required (RequiredVocabulary)`; semantics of each value expanded inline — row type self-identifiable without sub-table name |
| **C-28** | **FAIL** | Uniform `(TypeName)` annotation not applied — Coverage Matrix, Schema 1–5 tables all use untyped headers; only relay schema carries a typed column |
| **C-29** | **FAIL** | No Defect Classification Registry; structural mandates carry no defect codes; Verdict ledger has no Defect code column |

**Aspirational passing**: C-09–C-26 (18) + C-27 (1) = **19/21**

**Score**: (5/5 × 60) + (3/3 × 30) + (19/21 × 10) = 60 + 30 + 9.05 = **99.0**

---

### V-02 — Single axis: C-28 (uniform type annotation)

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-08 | PASS ×8 | Inherited + identical structure to V-01 |
| C-09–C-26 | PASS ×18 | Inherited from R7 V-04 |
| **C-27** | **PASS** | `RequiredVocabulary = {YES, VIOLATION}` declared (references V-01 semantics); `Required (RequiredVocabulary)` column header present in relay schema |
| **C-28** | **PASS** | Uniform `(TypeName)` applied to every typed column across all tables: Coverage Matrix (`ContentVocab`, `PhaseRef`, `RoleRef`, `VCIdentifier`), Schema 1 (`SeverityVocab`, `BlocksVocab`), Schema 2 (`GapTypeVocab`, `PromotionVocab`), Schema 3 (`ChannelVocab`, `ActivationPhaseRef`), Schema 4 (`GateIdentifier`, `BlockConditionVocab`), Schema 5 (`StepIdentifier` on all three step-ref columns), Role-Schema Binding Summary (`RoleName`, `SeverityVocab`, `GapTypeVocab`), Stage 1 table (`GapTypeVocab`, `SeverityVocab`, `PhaseRef`), Step 3b findings (`GapTypeVocab`, `SeverityVocab`); C-28 self-audit block in Verdict confirms all YES |
| **C-29** | **FAIL** | No Defect Classification Registry; no defect code column in Verdict |

**Aspirational passing**: 18 + C-27 + C-28 = **20/21**

**Score**: 60 + 30 + (20/21 × 10) = 60 + 30 + 9.52 = **99.5**

---

### V-03 — Single axis: C-29 (defect classification codes)

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-08 | PASS ×8 | Inherited |
| C-09–C-26 | PASS ×18 | Inherited; C-26 structurally confirmed by explicit `STRUCTURAL MANDATE -- CLOSED WORLD:` label in Coverage Matrix preamble with defect code `DEFECT: OPEN-WORLD-ASSERTION` inline |
| **C-27** | **PASS** | `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema; `Required (RequiredVocabulary)` column header present |
| **C-28** | **FAIL** | Type annotations not applied uniformly — Schema 1 uses `| Label | Definition | Blocks? |` (no typed headers); most tables untyped; only relay schema carries `Required (RequiredVocabulary)` |
| **C-29** | **PASS** | Defect Classification Registry declared before Stage 1 (5 codes: `OPEN-WORLD-ASSERTION`, `RELAY-SCHEMA-VIOLATION`, `LABEL-LOCK-VIOLATION`, `OUT-OF-ORDER-EXECUTION`, `PREMATURE-PHASE-ADVANCE`); every structural mandate cites its code inline (e.g., Coverage Matrix mandate cites `DEFECT: OPEN-WORLD-ASSERTION`, relay schema mandate cites `DEFECT: RELAY-SCHEMA-VIOLATION`); Verdict compliance ledger gains `Defect code (if FAIL)` column with codes pre-filled per row — FAIL rows cite by code, not prose |

**Aspirational passing**: 18 + C-27 + C-29 = **20/21**

**Score**: 60 + 30 + (20/21 × 10) = **99.5**

---

### V-04 — Combined: C-27 + C-28

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-08 | PASS ×8 | Inherited |
| C-09–C-26 | PASS ×18 | Inherited |
| **C-27** | **PASS** | Full `RequiredVocabulary` declaration with YES/VIOLATION semantics expanded; `Required (RequiredVocabulary)` column header; both values citable without parsing Field cell |
| **C-28** | **PASS** | Identical uniform annotation coverage as V-02: all Coverage Matrix columns typed, all Schema 1–5 definition tables typed, Role-Schema Binding Summary typed, Stage 1 findings table typed (`Source (GapTypeVocab)`, `Severity (SeverityVocab)`, `Affects phase (PhaseRef)`), Step 3b findings typed, relay schema typed; C-28 audit block confirms 10 annotation sites |
| **C-29** | **FAIL** | No Defect Classification Registry; no defect code column in Verdict; structural mandates carry no formal defect codes |

**Aspirational passing**: 18 + C-27 + C-28 = **20/21**

**Score**: 60 + 30 + (20/21 × 10) = **99.5**

---

### V-05 — Combined: C-27 + C-28 + C-29 (complete R8 target)

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-08 | PASS ×8 | Inherited |
| C-09–C-26 | PASS ×18 | Inherited; C-26 confirmed by labeled mandates throughout |
| **C-27** | **PASS** | `RequiredVocabulary is a closed two-value type: {YES, VIOLATION}` with full semantic expansion of both values; `Required (RequiredVocabulary)` column header; anti-pattern row carries `VIOLATION` in Required — row type self-validating without sub-table name |
| **C-28** | **PASS** | All V-04 annotations present PLUS Defect Classification Registry gains `Defect code (DefectCodeVocab)` typed column header; Verdict compliance ledger gains `Defect code (DefectCodeVocab)` typed column — registry and ledger are self-describing; `DefectCodeVocab` type propagates from declaration site to usage site via uniform annotation convention; 11 annotation sites confirmed in C-28 audit block |
| **C-29** | **PASS** | Defect Classification Registry with `DefectCodeVocab` closed type declared before Stage 1; every structural mandate carries inline defect code (`DEFECT: OPEN-WORLD-ASSERTION` on Coverage Matrix closure, `DEFECT: LABEL-LOCK-VIOLATION` on Schema 2 label lock, `DEFECT: PREMATURE-PHASE-ADVANCE` on Schema 4 gate hard-stop, `DEFECT: OUT-OF-ORDER-EXECUTION` on Schema 5 sub-step sequence, `DEFECT: RELAY-SCHEMA-VIOLATION` on relay schema mandate); Verdict compliance ledger column `Defect code (DefectCodeVocab)` pre-populated per row — FAIL rows cite by code, PASS rows carry `--`; C-29 audit block at Verdict top confirms registry present and all FAIL citations are from `DefectCodeVocab` |

**Aspirational passing**: 18 + C-27 + C-28 + C-29 = **21/21**

**Score**: 60 + 30 + (21/21 × 10) = **100**

---

### Ranking

| Rank | Variation | Score | New criteria passing |
|------|-----------|-------|---------------------|
| 1 | **V-05** | **100** | C-27, C-28, C-29 |
| 2 (tied) | V-02 | 99.5 | C-27, C-28 |
| 2 (tied) | V-03 | 99.5 | C-27, C-29 |
| 2 (tied) | V-04 | 99.5 | C-27, C-28 |
| 5 | V-01 | 99.0 | C-27 |

---

### Excellence Signals from V-05

**1. The defect registry is both a C-29 source and a C-28 participant.** The `Defect code (DefectCodeVocab)` column header in the registry itself carries the same uniform type annotation convention as every other typed column in the schema. The registry is simultaneously the source of truth for defect codes (satisfying C-29) and an instance of the uniform-annotation pattern (satisfying C-28). No special-case handling needed: the C-28 rule extends naturally to the defect registry.

**2. Typed column annotation propagates from declaration to usage.** The `DefectCodeVocab` type declared in the Defect Classification Registry appears in the Verdict compliance ledger column header as `Defect code (DefectCodeVocab)`. A reviewer inspecting any FAIL row can trace the type name from the Verdict column header directly to the registry table without counting rows or scanning prose. Vocabulary is self-locating.

**3. Structural mandates are co-located with their defect code inline.** Every `STRUCTURAL MANDATE --` label is immediately followed by its defect code on the next line. Readers see both the behavioral rule and its formal code at the same location. Verdict audit becomes a lookup, not a paraphrase exercise: "FAIL at Phase 4 pre-check → `DEFECT: PREMATURE-PHASE-ADVANCE`" with no further interpretation required.

**4. Three axes are additive at non-overlapping structural layers.** C-27 operates at vocabulary-closure level (column declares its two legal values), C-28 operates at column-header level (column names its type), C-29 operates at mandate-to-code level (mandate names its defect class). Adding all three to the same schema produces no collision: the relay schema `Required (RequiredVocabulary)` column satisfies both C-27 (closed vocabulary) and C-28 (typed header) through the same cell, while C-29 operates on a distinct structural element (the mandate/defect code pairing before the table).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Defect registry carries typed column header (DefectCodeVocab) making it simultaneously a C-29 source-of-truth and a C-28 self-describing schema participant — one structural element satisfies two criteria", "DefectCodeVocab type propagates from registry column header to Verdict compliance ledger column header — typed vocabulary is self-locating across declaration site and usage site without cross-reference prose", "Structural mandates carry inline defect code immediately after the mandate label — co-location makes Verdict audit a lookup, not a paraphrase exercise"]}
```
