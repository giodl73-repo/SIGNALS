Now I have all 5 variations. Let me score them against the v12 rubric (C-01–C-42).

---

# Scoring: `topic:plan` — Round 12 (v12 rubric, 42 criteria)

## Rubric Mapping Note

The file's variations were designed for an older internal rubric (§ID contract architecture). The v12 rubric in the prompt tests a different architectural axis (vocabulary contracts, sentinel tokens, ENTRY/JOB/EXIT lifecycle, write-surface blocks, defense registers). I'm scoring the file's V-01–V-05 against the prompt's v12 rubric. Where architectural elements overlap (strategy.md read, 9-namespace inventory, ADD/REMOVE/REPRIORITIZE proposals, confirmation gate), criteria map directly.

---

## Essential Criteria (C-01–C-05)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|-----------|------|------|------|------|------|-------|
| C-01 | Reads strategy.md, cites reference | PASS | PASS | PASS | PASS | PASS | Phase 1 opens strategy.md, extracts STRATEGY DATE, fills Schema A |
| C-02 | All 9 namespaces with artifact filenames + dates | FAIL | FAIL | FAIL | FAIL | FAIL | §4 template gives counts (`total artifacts \| new`) not individual artifact filenames + dates |
| C-03 | NEW vs PRIOR split, strategy date named | PASS | PASS | PASS | PASS | PASS | `new (date > STRATEGY DATE)` in §4; STRATEGY DATE explicitly named; only HIGH-PRESSURE namespaces drive proposals |
| C-04 | Typed change proposals ADD/REMOVE/REPRIORITIZE | PASS | PASS | PASS | PASS | PASS | §6 template; "missing null row != no proposals" annotation |
| C-05 | Confirmation gate YES/NO/REVISED | PASS | PASS | PASS | PASS | PASS | Phase 6: "Stop. Do not write to strategy.md. Halt here and wait for user reply." YES/NO/REVISED gate |

**Essential pass count: 4/5 for all variations (C-02 fails all).** No variation is golden.

Essential score: 4/5 × 60 = **48**

---

## Recommended Criteria (C-06–C-08)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|-----------|------|------|------|------|------|-------|
| C-06 | Evidence citation in non-null proposals | PASS | PASS | PASS | PASS | PASS | §6 "Evidence artifact [R-3]" column; Phase 5 enforces HIGH-PRESSURE artifact evidence |
| C-07 | Before/after diff structure | PASS | PASS | PASS | PASS | PASS | §6 `Before (from §1 Schema A) \| After` columns |
| C-08 | Inertia justification per row | PASS | PASS | PASS | PASS | PASS | §6 "Why this beats NO CHANGE [R-0]"; R-0 requires naming consequence of NOT changing. V-04/V-05 extend to null rows |

**Recommended: 3/3 for all.**

Recommended score: 3/3 × 30 = **30**

---

## Aspirational Criteria (C-09–C-42)

| C | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-09 | Type-labeled null declarations | PASS | PASS | PASS | PASS | PASS |
| C-10 | Conflict detection phase with typed null | PASS | PASS | PASS | PASS | PASS |
| C-11 | Required-cell table schemas | PASS | PASS | PASS | PASS | PASS |
| C-12 | In-phase stop gates | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-13 | Mandatory column enforcement | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-14 | Explicit placeholder tokens (??) | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-15 | Counted-total delta summary sentence | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-16 | Hedge-phrase disqualification | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-17 | Two-tier sentinel vocabulary | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-18 | Pre-signal defense register | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-19 | Integer-enforcement gate language | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-20 | Sequential phase-linked stop gates | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-21 | Vocabulary contract violation enumeration | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-22 | Row-number anchor citation | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-23 | Verbatim-quoted banned forms | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-24 | Cell-level banned-forms check instruction | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-25 | Banned-forms scope propagation | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-26 | Gate-0 pre-signal stop gate | PARTIAL | FAIL | FAIL | FAIL | PARTIAL |
| C-27 | Write-surface enforcement completeness | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-28 | Write-surface blocks as section headers | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-29 | Write-surface register | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-30 | Register-milestone linkage | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-31 | Named phase lifecycle template (ENTRY/JOB/EXIT) | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-32 | Artifact-to-register calibration column | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-33 | Inverted artifact sequence with upfront calibration | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-34 | Compound audit structure (spine + lifecycle) | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-35 | Upfront table schema register | PASS | PASS | PASS | PASS | PASS |
| C-36 | Schema-phase lifecycle elevation | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-37 | Per-schema breach conditions | PASS | PASS | PASS | PASS | PASS |
| C-38 | Schema-phase gate in sequential chain | PASS | FAIL | FAIL | FAIL | PASS |
| C-39 | Modal obligation language | PASS | PASS | PASS | PASS | PASS |
| C-40 | Typed violation taxonomy in vocabulary contract | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-41 | Cross-schema dependency declaration | FAIL | FAIL | PARTIAL | FAIL | PARTIAL |
| C-42 | Three-path audit declaration | FAIL | FAIL | FAIL | FAIL | FAIL |

### Evidence notes for key judgments

**C-09 PASS:** §6 typed null rows: `ADD: none -- inertia holds [R-0].` / `REMOVE: none -- inertia holds [R-0].` / `REPRIORITIZE: none -- inertia holds [R-0].` — separate labeled declaration per absent type.

**C-11 PASS:** §4, §6, §8 all produce named-column tables; "missing row != absent namespace" and "missing block != null" annotations make absent cells detectable violations.

**C-12 PARTIAL:** `[PHASE N GATE: PASS/STOP -- condition: all 9 namespace rows present; no namespace omitted]` is a do-not-proceed gate. But gates check structural presence of rows/blocks, not cell-level fill for every individual cell. Not the "do not proceed until every cell is filled" instruction C-12 requires.

**C-20 FAIL:** PHASE SEQUENCE declares the chain, but gate blocks themselves never say "Do not advance to Phase N+1 without passing this gate."

**C-26 PARTIAL (V-01, V-05):** CONTRACT COMPLETENESS GATE with four labeled checks ([A][B][C][D]) fires before Phase 1 and blocks phase entry until passing. Satisfies the structural intent of Gate-0. Does not use "Gate-0" naming or "Gate-0 → Gate-1 explicit link" language.

**C-35 PASS:** SKILL EXECUTION CONTRACT §1–§8 is a dedicated pre-phase schema register. `§1 SCHEMA A TEMPLATE`, `§4 NAMESPACE INVENTORY TABLE TEMPLATE`, `§6 PROPOSALS TABLE TEMPLATE`, `§8 CONFLICT AUDIT BLOCK TEMPLATE` — column structure, null behavior, phase authorization, and breach annotations declared for each schema before Phase 1.

**C-36 FAIL:** SKILL EXECUTION CONTRACT lacks ENTRY/JOB/EXIT lifecycle slots. C-36 explicitly: "without lifecycle slots does not satisfy this criterion even if C-35 passes."

**C-37 PASS:** Each §ID has inline breach conditions: §2 "SEAL violation and fails this block"; §3 "SEAL violation"; §4 "missing row != absent namespace"; §5 "SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation" + "missing block != null"; §6 "missing null row != no proposals"; §8 "missing block != null."

**C-38 PASS (V-01, V-05):** CONTRACT COMPLETENESS GATE is positioned before Phase 1, checks all §ID sections, both indexes, and null annotations — functioning as a schema-phase gate. `[CONTRACT GATE: PASS/STOP -- condition: [A]...[B]...[C]...[D]...]` with "Phase 1 does not begin until this gate passes." Satisfies C-38's "equivalent" allowance for Gate-S/Gate-(-1).

**C-39 PASS:** 5+ modal constraint sites: (1) R-2 "Before values in §6 must trace to §1 Schema A"; (2) R-2 "must be dropped"; (3) §4 "no row may be omitted"; (4) R-1 "May not be re-read"; (5) authorization check "No other §ID templates may be instantiated in this phase."

**C-40 FAIL:** No vocabulary contract block exists. The §ID breach conditions satisfy C-37 (per-schema) but not C-40 (categorized vocabulary contract taxonomy).

**C-41 PARTIAL (V-03, V-05):** R-N enforcement result declarations cite source §ID at use sites: `[R-2 APPLIED: Before values must trace to §1 Schema A sealed in Phase 1...]` and `[R-4 APPLIED: §5 reproduced from Skill Execution Contract §5 -- contract name and §ID cited.]`. Cross-schema dependency (§6 Before values governed by §1 Schema A) is traced at application points. Missing: "inherited from Phase -1 declaration, not invented here" language at use sites and explicit dependency declaration at definition site.

**C-42 FAIL:** No named three-path audit declaration (Schema Spine, Write-Surface Spine, Lifecycle Slots) in any preamble.

---

## Aspirational Totals

| Variation | Passing aspirational (of 34) | Details |
|-----------|------------------------------|---------|
| V-01 | 8.0 (C-09,C-10,C-11,C-12½,C-26½,C-35,C-37,C-38,C-39) | +C-38, +C-26½ vs base |
| V-02 | 6.5 (C-09,C-10,C-11,C-12½,C-35,C-37,C-39) | base only |
| V-03 | 7.0 (C-09,C-10,C-11,C-12½,C-35,C-37,C-39,C-41½) | +C-41½ vs base |
| V-04 | 6.5 (C-09,C-10,C-11,C-12½,C-35,C-37,C-39) | base only |
| V-05 | 8.5 (all V-01 + C-41½) | +C-38, +C-26½, +C-41½ |

---

## Composite Scores

`(essential/5 × 60) + (recommended/3 × 30) + (aspirational/34 × 10)`

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 48 | 30 | 8.0/34 × 10 = 2.35 | **80.35** |
| V-02 | 48 | 30 | 6.5/34 × 10 = 1.91 | **79.91** |
| V-03 | 48 | 30 | 7.0/34 × 10 = 2.06 | **80.06** |
| V-04 | 48 | 30 | 6.5/34 × 10 = 1.91 | **79.91** |
| V-05 | 48 | 30 | 8.5/34 × 10 = 2.50 | **80.50** |

**Rank:** V-05 (80.5) > V-01 (80.4) > V-03 (80.1) > V-02 = V-04 (79.9)

**Golden status:** None — C-02 fails all variations (§4 template produces namespace counts, not artifact filenames + dates). Composite threshold ≥ 80 is met by V-05 and V-01, but all-essential-pass requirement blocks golden.

---

## Excellence Signals — V-05

**V-05 outperforms V-02/V-03/V-04** by combining three single-axis innovations:

**Signal 1 — Contract completeness gate as schema-phase gate (V-01 axis → C-38 PASS):**
The `CONTRACT COMPLETENESS GATE` with four labeled checks ([A] §IDs, [B] PHASE AUTHORIZATION INDEX, [C] CONSTRAINT SCOPE INDEX, [D] null annotations) before Phase 1 satisfies C-38's schema-phase gate requirement. This is a compact alternative to Phase -1 lifecycle restructuring: a named compound `[CONTRACT GATE: PASS/STOP]` block achieves the same audit anchor without requiring ENTRY/JOB/EXIT slots on the contract section. Architecture: a pre-execution contract verification gate can carry the same structural weight as a full Phase -1 when it has labeled sub-conditions and a hard PASS/STOP result.

**Signal 2 — R-N enforcement event declarations closing the constraint chain (V-03 axis → C-41 PARTIAL):**
`[R-N APPLIED: ... Per §CONSTRAINT SCOPE INDEX, R-N is active in Phase N.]` at application points cites the source §ID and the contract section that governs the constraint. This begins the cross-schema dependency tracing required by C-41 — the constraint at §6 Before values is traced to §1 Schema A at use sites. The gap to full C-41 PASS: explicit "inherited from Phase -1 declaration, not invented here" language at use sites, and dependency declaration at the §6 definition site (not first introduced at use sites).

**Signal 3 — [1a]/[1b] compound authorization gate at each phase entry (V-02 axis):**
Restructuring the authorization check as `[AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified ... + [1b] R-N rules verified ...]` makes the dual-axis check (§IDs per PHASE AUTHORIZATION INDEX + R-N rules per CONSTRAINT SCOPE INDEX) a named gate with independently labeled sub-conditions. This doesn't yield new criterion passes in v12 but reveals a structural pattern: authorization headers can be named gates rather than prose lists, making dual-axis conformance auditable without re-reading indexes.

---

## C-02 Gap Analysis

C-02 is the blocking essential across all variations. The §4 NAMESPACE INVENTORY TABLE template captures namespace-level counts (`total artifacts | new (date > STRATEGY DATE)`) but not individual artifact filenames or dates. To fix:
- Add an artifact listing phase or sub-table that names individual artifacts with their dates
- Or expand §4 to include per-artifact rows: `namespace | artifact filename | artifact date | new?`

---

```json
{"top_score": 80, "all_essential_pass": false, "new_patterns": ["Contract completeness gate pattern: named compound pre-execution gate ([A][B][C][D] labeled checks) before Phase 1 satisfies C-38 schema-phase gate requirement without Phase -1 lifecycle restructuring — a PASS/STOP gate over the schema register achieves structural audit anchoring with less overhead", "R-N enforcement event declarations: [R-N APPLIED: ... Per §CONSTRAINT SCOPE INDEX] blocks at application points with source §ID citation begin C-41 cross-schema dependency tracing — gap to full C-41 is 'inherited from Phase -1 declaration, not invented here' language at use sites plus dependency declaration at definition site", "Compound authorization gate with [1a]/[1b] sub-conditions: restructuring phase authorization check as a named PASS/STOP gate with independently labeled axes (§IDs via PHASE AUTHORIZATION INDEX + R-N rules via CONSTRAINT SCOPE INDEX) makes dual-axis conformance auditable without reading full index text"]}
```
