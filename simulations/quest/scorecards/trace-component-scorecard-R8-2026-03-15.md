# trace-component — R8 Score (v7 Rubric)

## Scoring Key

- Essential: C-01–C-04 × 15 pts = 60 pts
- Recommended: C-05–C-07 × 10 pts = 30 pts
- Aspirational: C-08–C-21 × 5 pts = 70 pts
- **Total ceiling: 160 pts**

PASS = full weight | PARTIAL = half weight | FAIL = 0

---

## V-01 — Role Sequence: ECC First

**Structure**: 6-role pipeline. Role 1 (Evidence Architect) produces ECC as standalone artifact before any schemas exist. Schema fill rules embed OBL-IDs creating bidirectional binding. Role 4 emits TRACE ARCHITECTURE: SEALED after 4-artifact inventory check. Role 6 fills compliance table against Role 1 ECC.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | TABLE-01 SCHEMA: every causal hop, dispatch chains show source+target, UNKNOWN tokens at gaps |
| C-02 | Component tree traversal | PASS | §2 table with Hop/From/To/Direction/Carrier Name/Signal Type; every §1 component required |
| C-03 | State delta shown | PASS | §3 table with Before/After/Derived Selectors; UNKNOWN for undetermined |
| C-04 | Re-render list complete | PASS | TABLE-04 SCHEMA: YES/NO/UNKNOWN; NO rows for memoized; skip mechanism required |
| C-05 | Side effects identified | PASS | §5 table; both branches per async effect; MISSING-LOADING/MISSING-ERROR for unconfirmed |
| C-06 | Issue flags present | PASS | §6 all four categories required; named findings or "none detected" with row citations |
| C-07 | Final UI state described | PASS | §7 per-item format with OBL-03/OBL-04 citations; derivable from §3 |
| C-08 | Optimization opportunities | PASS | §9 table; explicit "None — §4 NO rows: [list]" fallback |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes as dedicated section; §1–§7 use PART A neutral equivalents |
| C-10 | Gap-visible format | PASS | TABLE-01 and TABLE-04 are named schema-driven tables; missing entry is structurally obvious |
| C-11 | Cross-section evidence chaining | PASS | OBL-01–OBL-06 require explicit cross-section citations; §7 cites §3 and §4 by key/row |
| C-12 | Incompleteness tokens | PASS | UNKNOWN/MISSING-LOADING/MISSING-ERROR defined and required; §10 stamp + correction protocol |
| C-13 | Framework-neutral core enforcement | PASS | §1–§7 bound to Neutral Equivalents; MAP terms confined to §8 only |
| C-14 | Vocabulary contract artifact | PASS | §0 with PART A MAP and PART B PASS-THROUGH produced before trace content (Role 3) |
| C-15 | Machine-readable completeness inventory | PASS | §10 stamp with counts by category; structured block |
| C-16 | PASS-THROUGH designation | PASS | PART B with named Type column; required entries explicitly listed; no aliasing |
| C-17 | Stamp with active correction | PASS | §10 active correction protocol: discrepancy correction with location OR "Cross-checked: no corrections required" — both paths required |
| C-18 | Role-level enforcement gate | PASS | Role 5 explicit pre-output gate: "Before generating §1, confirm no MAP term from §0 PART A will appear in §1–§7 cell values." Named blocking constraint |
| C-19 | Pre-declared named column schemas | PASS | TABLE-01 SCHEMA (Role 2) and TABLE-04 SCHEMA (Role 2) declared as named blocks before Role 5 trace content |
| C-20 | Pre-declared evidence chain contract | PASS | Role 1 produces ECC with 6 OBL-IDs before schemas exist; Role 6 §12 fills compliance against Role 1 ECC, not body inspection |
| C-21 | Unified pre-trace architecture seal | PASS | Role 4 emits TRACE ARCHITECTURE: SEALED after 4-artifact inventory; single completion token; Role 5 blocked by single condition; no intermediate blocking tokens between Roles 1–3 |

**V-01 Score: 160/160**

---

## V-02 — Output Format: ECC as Two-Column Compliance Table

**Structure**: 3-role pipeline. Role 1 (Trace Architect) produces entire TRACE ARCHITECTURE artifact with ECC as first sub-artifact. ECC uses two-pass compliance table — audit role fills COMPLIANCE column against pre-declared rows. Shorter prompt; tighter mechanical audit.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | TABLE-01 SCHEMA in TRACE ARCHITECTURE: every hop, dispatch chains, UNKNOWN tokens |
| C-02 | Component tree traversal | PASS | §2 table; every §1 component; Carrier Name required; direction explicit |
| C-03 | State delta shown | PASS | §3 table; Before/After/Derived Selectors; UNKNOWN for undetermined |
| C-04 | Re-render list complete | PASS | TABLE-04 SCHEMA; YES/NO/UNKNOWN; evaluated-and-skipped = NO row; skip mechanism |
| C-05 | Side effects identified | PASS | §5 table; both branches; MISSING-LOADING/MISSING-ERROR for unconfirmed |
| C-06 | Issue flags present | PASS | §6 all four categories; OBL-05/OBL-06 row citations for "none detected" |
| C-07 | Final UI state described | PASS | §7 format: §3 key [OBL-03] and §4 row [OBL-04] per item |
| C-08 | Optimization opportunities | PASS | §9 table with explicit "None — §4 NO rows: [list]" fallback |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes; PART A neutral equivalents in §1–§7 |
| C-10 | Gap-visible format | PASS | Named TABLE-01/TABLE-04 schemas; structured tables for §1 and §4 |
| C-11 | Cross-section evidence chaining | PASS | ECC OBL-01–OBL-06 mandate explicit cross-section citations throughout |
| C-12 | Incompleteness tokens | PASS | UNKNOWN/MISSING-LOADING/MISSING-ERROR; §10 stamp with correction protocol |
| C-13 | Framework-neutral core enforcement | PASS | §1–§7 bound to PART A neutral equivalents; MAP terms only in §8 |
| C-14 | Vocabulary contract artifact | PASS | §0 PART A + PART B within TRACE ARCHITECTURE, declared before trace content |
| C-15 | Machine-readable completeness inventory | PASS | §10 stamp with structured counts |
| C-16 | PASS-THROUGH designation | PASS | PART B with Type column; required entries explicitly enumerated; no aliasing |
| C-17 | Stamp with active correction | PASS | §10 active correction: discrepancy or "Cross-checked: no corrections required" |
| C-18 | Role-level enforcement gate | PASS | Role 2 pre-output gate: "Before §1, state: GATE CHECK: PASS — no MAP terms in §1–§7 planned column values." Named blocking constraint at role level |
| C-19 | Pre-declared named column schemas | PASS | TABLE-01 SCHEMA and TABLE-04 SCHEMA declared inside TRACE ARCHITECTURE before Role 2 begins |
| C-20 | Pre-declared evidence chain contract | PASS | ECC is first sub-artifact within TRACE ARCHITECTURE; includes OBL-ID + violation type columns; Role 3 fills COMPLIANCE column against pre-declared rows |
| C-21 | Unified pre-trace architecture seal | PASS | All sub-artifacts (ECC, TABLE-01, TABLE-04, §0 PART A/B, GATE-VOCAB) inside single TRACE ARCHITECTURE block; SEALED emitted after GATE-VOCAB: PASS; single blocking condition |

**V-02 Score: 160/160**

---

## V-03 — Phrasing Register: Imperative + Violation Types

**Structure**: Flat prompt. 5 BLOCKs in PRE-TRACE PHASE (no role transitions between blocks). Imperative SHALL/MUST language. Named violation types (CITATION-GAP, DERIVATION-BREAK, UNSUPPORTED-CONCLUSION, VOCABULARY-LEAK, SCHEMA-VIOLATION). Inline ARCHITECTURE CHECKLIST before seal. Flagged C-18 risk.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | BLOCK 2 TABLE-01 SCHEMA; every hop required; SCHEMA-VIOLATION named for implicit jumps |
| C-02 | Component tree traversal | PASS | §2 table; every §1 component; Carrier Name required |
| C-03 | State delta shown | PASS | §3 table; Before/After/Derived Selectors; UNKNOWN for undetermined |
| C-04 | Re-render list complete | PASS | BLOCK 3 TABLE-04 SCHEMA; MUST for every §2 component; NO rows for memoized |
| C-05 | Side effects identified | PASS | §5 table; both branches; MISSING-LOADING/MISSING-ERROR |
| C-06 | Issue flags present | PASS | §6 all four categories; OBL-05/OBL-06 with named violation types |
| C-07 | Final UI state described | PASS | §7 per item: §3 key [OBL-03] and §4 row [OBL-04] |
| C-08 | Optimization opportunities | PASS | §9 table; explicit "None — §4 NO rows: [list]" with SCHEMA-VIOLATION for omission |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes; PART A neutral equivalents in §1–§7; VOCABULARY-LEAK named for violations |
| C-10 | Gap-visible format | PASS | Named TABLE-01 SCHEMA and TABLE-04 SCHEMA declared as BLOCKs with completion tokens |
| C-11 | Cross-section evidence chaining | PASS | ECC OBL-01–OBL-06 with violation types; §7 cites §3 and §4 per item |
| C-12 | Incompleteness tokens | PASS | UNKNOWN/MISSING-LOADING/MISSING-ERROR; §10 stamp + correction protocol |
| C-13 | Framework-neutral core enforcement | PASS | §1–§7 bound to PART A neutral equivalents; MAP terms confined to §8 |
| C-14 | Vocabulary contract artifact | PASS | BLOCK 4 §0 VOCABULARY CONTRACT with PART A/B; declared before trace content |
| C-15 | Machine-readable completeness inventory | PASS | §10 structured stamp with counts by category |
| C-16 | PASS-THROUGH designation | PASS | PART B with Type column; SHALL/MUST language on aliasing = ALIAS-VIOLATION |
| C-17 | Stamp with active correction | PASS | §10 active correction with correction notation or "Cross-checked: no corrections required" |
| C-18 | Role-level enforcement gate | **PASS** | TRACE GENERATION PHASE has named blocking check: "**Pre-output verification**: `GATE CHECK: PASS — no MAP terms in §1–§7 planned column values.`" — criterion explicitly allows "equivalent blanket pre-output check for the core-section generating role"; this is a named, non-advisory constraint. *Risk: "role-level" is ambiguous for flat prompts; scoring as PASS on the "equivalent blanket pre-output check" basis.* |
| C-19 | Pre-declared named column schemas | PASS | TABLE-01 SCHEMA (BLOCK 2) and TABLE-04 SCHEMA (BLOCK 3) declared as named blocks with completion tokens (`TABLE-01 SCHEMA: DECLARED`) before trace generation |
| C-20 | Pre-declared evidence chain contract | PASS | BLOCK 1 is ECC with violation types; declared before all other blocks; AUDIT PHASE §12 fills compliance against pre-declared BLOCK 1 obligations |
| C-21 | Unified pre-trace architecture seal | PASS | ARCHITECTURE CHECKLIST ticks 5 conditions (ECC + TABLE-01 + TABLE-04 + VOCABULARY CONTRACT + GATE-VOCAB) before emitting `TRACE ARCHITECTURE: SEALED`; no intermediate blocking tokens; single blocking condition for TRACE GENERATION PHASE |

**V-03 Score: 160/160**

> Note: C-18 scored PASS on "equivalent blanket pre-output check" basis. If read strictly as requiring a role transition, V-03 scores PARTIAL on C-18 → 157.5/160.

---

## V-04 — Combined: Role Sequence + Output Format

**Structure**: 5-role pipeline. Role 1 (Evidence Architect) produces ECC standalone (V-01 axis). ECC uses compliance table with MUST Carry column (V-02 axis). OBL-IDs annotated in TABLE-04 column header. Role 4 emits SEALED with explicit ECC obligation count. Role 6 fills compliance table directly from Role 1 ECC.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | TABLE-01 SCHEMA with OBL-02/OBL-01 in fill rules; every hop; UNKNOWN tokens |
| C-02 | Component tree traversal | PASS | §2 table; every §1 component; Carrier Name required |
| C-03 | State delta shown | PASS | §3 table; Before/After/Derived Selectors |
| C-04 | Re-render list complete | PASS | TABLE-04 SCHEMA with `Upstream Ref [OBL-01]` as explicit column header; NO rows for memoized |
| C-05 | Side effects identified | PASS | §5 table; both branches; MISSING-LOADING/MISSING-ERROR |
| C-06 | Issue flags present | PASS | §6 all four categories; OBL-05/OBL-06 brackets in section heading |
| C-07 | Final UI state described | PASS | §7 with `[OBL-03]` and `[OBL-04]` per item |
| C-08 | Optimization opportunities | PASS | §9 table; explicit "None — §4 NO rows: [list]" with SCHEMA-VIOLATION for omission |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes; PART A neutral equivalents in §1–§7 |
| C-10 | Gap-visible format | PASS | Named TABLE-01/TABLE-04 schemas; OBL-01 visible in column header |
| C-11 | Cross-section evidence chaining | PASS | ECC OBL-01–OBL-06; compliance table in §12 checks derivation chain |
| C-12 | Incompleteness tokens | PASS | UNKNOWN/MISSING-LOADING/MISSING-ERROR; §10 stamp + correction protocol |
| C-13 | Framework-neutral core enforcement | PASS | §1–§7 bound to PART A neutral equivalents; MAP terms only in §8 |
| C-14 | Vocabulary contract artifact | PASS | §0 PART A/B produced by Role 3; declared before trace content |
| C-15 | Machine-readable completeness inventory | PASS | §10 structured stamp with counts |
| C-16 | PASS-THROUGH designation | PASS | PART B with Type column; "No neutralization. No aliasing." |
| C-17 | Stamp with active correction | PASS | §10 active correction protocol with "Cross-checked: no corrections required" path |
| C-18 | Role-level enforcement gate | PASS | Role 5 pre-output gate: "GATE CHECK: PASS — no MAP terms in §1–§7 planned column values." Named blocking constraint at role level |
| C-19 | Pre-declared named column schemas | PASS | TABLE-01 SCHEMA (Role 2) and TABLE-04 SCHEMA (Role 2) declared before Role 5; column names, token values, fill rules all named |
| C-20 | Pre-declared evidence chain contract | PASS | Role 1 produces ECC standalone with MUST Carry and Violation Type columns; Role 6 §12 explicitly fills against "EVIDENCE CHAIN CONTRACT from Role 1" |
| C-21 | Unified pre-trace architecture seal | PASS | Role 4 emits `TRACE ARCHITECTURE: SEALED — ECC (6 obligations), TABLE-01 SCHEMA, TABLE-04 SCHEMA, §0 PART A/B, GATE-VOCAB: PASS`; single blocking condition; no intermediate blocks |

**V-04 Score: 160/160**

---

## V-05 — Combined: All Three Axes

**Structure**: 5-role pipeline. Role 1 (Evidence Architect) produces ECC first with violation types (all three axes). Schemas embed OBL-ID coverage annotations. Role 5 section headers carry OBL-ID brackets (§4 [OBL-01], §5 [OBL-02]). PART B adds "Binds To" column (TABLE-01.Handler, TABLE-04.Component). SEALED token carries falsifiable count inventory. Role 6 §12 explicitly prohibits reconstructing obligations from body.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Event chain complete | PASS | TABLE-01 SCHEMA with OBL-01/OBL-02 coverage annotations in fill rules; every causal hop; SCHEMA-VIOLATION named |
| C-02 | Component tree traversal | PASS | §2 table; every §1 component; Carrier Name required; Signal Type column |
| C-03 | State delta shown | PASS | §3 table; Before/After/Derived Selectors; UNKNOWN for undetermined |
| C-04 | Re-render list complete | PASS | TABLE-04 SCHEMA: `Upstream Ref — §2 hop OR §3 key. MUST appear for every row including NO rows. [OBL-01]`; CITATION-GAP named for absent Upstream Ref |
| C-05 | Side effects identified | PASS | §5 [OBL-02] section header; both branches; MISSING-LOADING/MISSING-ERROR; CITATION-GAP named for absent Upstream Ref |
| C-06 | Issue flags present | PASS | §6 [OBL-05, OBL-06] section header; all four categories; UNSUPPORTED-CONCLUSION named for unsupported "none detected" |
| C-07 | Final UI state described | PASS | §7 [OBL-03, OBL-04]: "Missing = DERIVATION-BREAK" per item |
| C-08 | Optimization opportunities | PASS | §9 table; explicit "No optimization opportunities — §4 NO rows: [list all NO rows]" with SCHEMA-VIOLATION named |
| C-09 | Framework-portable annotations | PASS | §8 Framework Notes; PART A neutral equivalents in §1–§7; VOCABULARY-LEAK named |
| C-10 | Gap-visible format | PASS | TABLE-01/TABLE-04 named schemas; OBL-01 in column definition AND section header |
| C-11 | Cross-section evidence chaining | PASS | ECC OBL-01–OBL-06; §7 cites both §3 key [OBL-03] and §4 row [OBL-04]; DERIVATION-BREAK named for gaps |
| C-12 | Incompleteness tokens | PASS | UNKNOWN/MISSING-LOADING/MISSING-ERROR; §10 stamp with active correction; "A stamp without it is a completeness failure" |
| C-13 | Framework-neutral core enforcement | PASS | §1–§7 bound to PART A; "Any MAP term in §1–§7 cell values is a VOCABULARY-LEAK" |
| C-14 | Vocabulary contract artifact | PASS | §0 PART A/B produced by Role 3; declarations include "VOCABULARY-LEAKs" for violations |
| C-15 | Machine-readable completeness inventory | PASS | §10 structured stamp; "A stamp without [cross-check record] is a completeness failure" |
| C-16 | PASS-THROUGH designation | PASS | PART B with Type AND **Binds To** columns; Binds To: TABLE-01.Handler / TABLE-01.Owner / TABLE-04.Component; "Aliasing = ALIAS-VIOLATION" |
| C-17 | Stamp with active correction | PASS | §10: correction with category/before-after/location OR "Cross-checked: counts match body; no corrections required" — cross-check record required regardless |
| C-18 | Role-level enforcement gate | PASS | Role 5 pre-output gate: "GATE CHECK: PASS — no MAP terms in §1–§7 planned column values." Named blocking constraint at role level; precedes §1 |
| C-19 | Pre-declared named column schemas | PASS | TABLE-01 SCHEMA and TABLE-04 SCHEMA from Role 2; completion tokens `TABLE-01 SCHEMA: DECLARED — columns carry OBL-01, OBL-02 coverage annotations` and `TABLE-04 SCHEMA: DECLARED — Upstream Ref column annotated with OBL-01` |
| C-20 | Pre-declared evidence chain contract | PASS | Role 1 produces ECC first with SHALL/violation type columns; "This contract is the foundational artifact: all subsequent pre-trace roles reference its OBL-IDs; the trace-generating role fills against its obligations; the audit role checks compliance against its rows." Role 6 §12 explicitly states "do not reconstruct obligations from the body" |
| C-21 | Unified pre-trace architecture seal | PASS | Role 4 emits: `TRACE ARCHITECTURE: SEALED — constituent artifacts: ECC (6 obligations: OBL-01–OBL-06), TABLE-01 SCHEMA (5 cols), TABLE-04 SCHEMA (5 cols), §0 PART A ([N] MAP terms), §0 PART B ([M] PASS-THROUGH names), GATE-VOCAB: PASS. All trace-generating roles unlocked.` Single blocking condition; explicit falsifiable count inventory |

**V-05 Score: 160/160**

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (70) | Total |
|-----------|----------------|-----------------|-------------------|-------|
| V-01 | 60 | 30 | 70 | **160** |
| V-02 | 60 | 30 | 70 | **160** |
| V-03 | 60 | 30 | 70 | **160** *(157.5 if C-18 strict)* |
| V-04 | 60 | 30 | 70 | **160** |
| V-05 | 60 | 30 | 70 | **160** |

---

## Rankings

All variations clear both bands (all essential PASS, all ≥ 128 → Golden).

**Qualitative ranking** (same numeric score, differentiated by binding density and structural completeness):

1. **V-05** — Maximum binding density: ECC-first + compliance table + imperative violation naming + section-header OBL-ID brackets + PART B "Binds To" column + falsifiable seal inventory. The pre-declared ECC explicitly prohibits audit reconstruction from body. Strongest implementation of both C-20 and C-21.
2. **V-04** — Cleanest C-20 mechanism: ECC standalone first + audit fills compliance table. OBL-ID visible in column headers. Explicit obligation count in seal.
3. **V-01** — ECC-first with bidirectional schema fill rule embedding. OBL-IDs in fill rules but not in section headers or column headers.
4. **V-02** — Compliance table as C-20 mechanism; tighter prompt (3 roles) but ECC not strictly first-standalone (embedded as first sub-artifact within TRACE ARCHITECTURE).
5. **V-03** — Flat prompt achieves same coverage via imperative language. C-18 borderline (phase-level vs role-level gate). Weakest structural enforcement guarantee despite equivalent criteria score.

---

## Excellence Signals from V-05

1. **"Do not reconstruct obligations from the body" prohibition** — Role 6 §12 explicitly forbids the audit role from inferring obligations from what was written. This hardcodes the C-20 guarantee (audit checks against pre-declared contract, not body pattern-matching) into the audit role instructions rather than trusting role framing alone.

2. **Falsifiable seal inventory** — TRACE ARCHITECTURE: SEALED carries verifiable constituent counts (6 obligations: OBL-01–OBL-06, TABLE-01 SCHEMA 5 cols, TABLE-04 SCHEMA 5 cols, N MAP terms, M PASS-THROUGH names). The seal is a checkable claim, not a declarative marker. Any discrepancy between token and artifacts is detectable.

3. **PART B "Binds To" column** — Each PASS-THROUGH entry explicitly names the schema column it feeds into (TABLE-01.Handler, TABLE-04.Component). Creates machine-checkable cross-artifact binding between vocabulary contract and schema structure. No existing criterion requires this; it goes beyond C-16 (which only requires the PASS-THROUGH set be declared).

4. **Section-header OBL-ID brackets** — OBL-IDs appear in section headings (§4 Re-render List [OBL-01], §5 Side Effects [OBL-02]) making obligation reference visible at the structural navigation level, not just embedded in fill rules.

5. **Complete violation-type vocabulary** — CITATION-GAP, DERIVATION-BREAK, UNSUPPORTED-CONCLUSION, VOCABULARY-LEAK, ALIAS-VIOLATION, SCHEMA-VIOLATION all appear as named violation types throughout pre-trace and trace phases. Each structural rule has a named failure mode, not just a remediation instruction.

---

## New Pattern Assessment

R8 variations explore implementation strategies for C-20 and C-21 (the R7 criteria). No pattern emerges that is structurally distinct from existing criteria at the level C-20/C-21 were distinct from C-11/C-18/C-19. The PART B "Binds To" column (cross-artifact vocabulary-to-schema binding) is the strongest candidate for a new criterion but is an enhancement of C-16 rather than a new structural property. The falsifiable seal inventory is an enhancement of C-21 rather than a distinct property.

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": []}
```
