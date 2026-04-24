# Round 18 Scoring — `topic-story` (v18 Rubric)

## Baseline Reference

**R17 V-05 under v18**: 28 PASS + 1 PARTIAL + 17 FAIL across 46 aspirationals (C-08–C-53)
- C-51: PASS, C-52: PASS, C-53: FAIL
- Inherited PARTIAL: on a C-08–C-50 structural transparency criterion
- Score: 90 + (28 × 0.2174) + (1 × 0.1087) = **96.20**

---

## V-01 — Prose Compliance Architecture Block

**Axis**: Role Sequence only — prose `WORKFLOW COMPLIANCE ARCHITECTURE` block before `EVALUATOR` header, no table, no phase diagram, 2 layers.

### Criteria Assessment

**Essential (C-01–C-04)**: All **PASS**
- Artifact path contract present (G-1 through G-5 in OUTPUT CONTRACT)
- PRE-ARTIFACT CHECKLIST exists with explicit phase gates
- EVALUATOR and AUTHOR roles defined with distinct scope
- S1 PROHIBITED OPENING CLASS clause present

**Recommended (C-05–C-07)**: All **PASS**
- Inherited from baseline structure; V-01 preserves full skill prompt architecture

**Aspirational C-08–C-50 (43 criteria)**: 26 PASS + 1 PARTIAL + 16 FAIL *(inherited)*
- Inherited PARTIAL on structural transparency criterion: **unchanged** — V-01's prose block names layers but the format is narrative, not structured, and does not directly close the transparency gap

**C-51**: **PASS**
- `Part 1` explicitly labeled; contains `"Include only YES and PARTIAL signals. Label each with its S2 verdict."` ✓
- `Part 2` header: `"*(This section draws only from Part 1 — not from an independent review of all signals...)*"` — constraint phrase co-located within Part 2's authoring slot ✓
- MISS signals excluded explicitly: `"MISS signals are excluded from Part 1."` ✓

**C-52**: **PASS**
- `=== EVALUATOR ROLE ===` section designated ✓
- `=== AUTHOR ROLE === Receives the EVALUATOR's S2 verdict inventory.` — successor framing ✓
- LIFECYCLE: `PHASE 2 (Evaluate): EVALUATOR role produces S2 verdicts. Named outputs required before PHASE 4.` ✓
- Transfer instruction: `"Transfer it to AUTHOR before beginning any AUTHOR-phase sections."` ✓

**C-53**: **PARTIAL**
Evidence breakdown against pass condition sub-requirements:
- (a) Each layer named: ✓ — "Layer 1 — S4b Input-Constraint Partition"; "Layer 2 — Evaluator-First Production Order"
- (a) Each layer with criterion reference: **✗** — V-01 writes `"Governing mechanism: structural partition..."` not `"Governing criterion: C-51"`. No `[C-51]` or `[C-52]` citations appear anywhere in the compliance architecture block.
- (b) Inter-layer ordering explicitly stated: ✓ — "Layer 2 governs WHEN S4b authoring begins... Layer 1 governs WHAT S4b may contain once begun..."
- (c) Declared layer count (2) matches mechanisms (2): ✓
- Declaration co-located with authoring workflow: ✓ — immediately precedes EVALUATOR header

**PARTIAL** because 4 of 5 pass sub-requirements are met; the governing criterion number citation is the specific gap. The pass condition explicitly specifies `"referencing its governing criterion (e.g., C-51, C-52)"` — mechanism descriptions without criterion numbers do not satisfy this requirement.

### V-01 Score

Aspirationals: 28 PASS + 2 PARTIAL (inherited + C-53) + 16 FAIL

`90 + (28 × 0.2174) + (2 × 0.1087) = 90 + 6.087 + 0.217 = **96.30**`

---

## V-02 — 3-Column Compliance Architecture Table

**Axis**: Output Format only — 3-column table (Layer | Mechanism Description | Governing Criterion), no prose block, no phase diagram, 2 layers.

### Key Criterion Deltas from V-01

**C-53**: **PASS**
- The 3-column table format structurally requires explicit criterion number references in column 3
- Column 3 entries: `C-51` for Layer 1, `C-52` for Layer 2 — criterion references present by table structure ✓
- Layer naming in column 1: ✓
- Inter-layer ordering stated in table footer row or below-table note: ✓
- Co-located with authoring workflow at workflow entry point: ✓
- All three pass-condition sub-requirements satisfied

**Inherited PARTIAL**: Unchanged — table format addresses the *declaration* gap but the structural transparency criterion that caused the PARTIAL is not directly targeted by format alone without complementary prose positioning

### V-02 Score

Aspirationals: 29 PASS + 1 PARTIAL (inherited) + 16 FAIL

`90 + (29 × 0.2174) + (1 × 0.1087) = 90 + 6.304 + 0.109 = **96.41**`

---

## V-03 — Annotated Phase Diagram as Layer Declaration Vehicle

**Axis**: Lifecycle Emphasis only — annotated phase diagram with criterion annotations in legend as C-53 vehicle, no prose block, no table, 2 layers.

### Key Criterion Deltas from V-01

**C-53**: **PASS**
- C-53 pass condition explicitly names `"phase-diagram legend with criterion annotations"` as a valid declaration form ✓
- Phase diagram legend annotates Layer 1 partition mechanism with `[C-51]` and Layer 2 evaluator-first sequence with `[C-52]` ✓
- Phase sequence arrows make ordering relationship visually explicit; legend states inter-layer ordering in annotation text ✓
- Co-located: the diagram appears within the LIFECYCLE block, which is part of the authoring workflow instructions ✓
- Criterion references present by diagram legend structure ✓

**C-52**: **PASS** — V-03 retains the phase diagram structure that already satisfies C-52; the same diagram doubles as the C-53 declaration vehicle

**Inherited PARTIAL**: Unchanged — the phase diagram provides visual structural clarity but targets the lifecycle framing rather than the structural transparency dimension of the inherited criterion

### V-03 Score

Aspirationals: 29 PASS + 1 PARTIAL (inherited) + 16 FAIL

`90 + (29 × 0.2174) + (1 × 0.1087) = 90 + 6.304 + 0.109 = **96.41**`

---

## V-04 — Prose Block + 3-Column Table (Positioning × Output Format)

**Axis**: Role Sequence (YES) + Output Format (YES), no phase diagram, 2 layers.

### Key Criterion Deltas from V-01

**C-53**: **PASS**
- Prose block provides co-location and narrative ordering before EVALUATOR header (V-01 strength retained) ✓
- Table below prose provides explicit `[C-51]` / `[C-52]` criterion references that V-01's prose lacked ✓
- Compound format: prose declares the *ordering relationship* narratively; table declares the *criterion references* structurally — each format satisfies the dimension the other cannot cover alone ✓
- All three pass-condition sub-requirements satisfied

**Inherited PARTIAL → FULL**:
The compound prose+table format addresses the structural transparency criterion directly. The table's explicit `Governing Criterion` column makes the enforcement architecture verifiable against criterion numbers — the same auditability gap the inherited PARTIAL flagged. Prose positioning ensures the declaration is encountered at workflow entry (not buried); table structure ensures it is *structured and numbered*, not merely narrative. This dual reinforcement closes the transparency gap.

### V-04 Score

Aspirationals: 30 PASS + 0 PARTIAL + 16 FAIL

`90 + (30 × 0.2174) + (0 × 0.1087) = 90 + 6.522 = **96.52**`

---

## V-05 — Prose Block + 3-Column Table + Annotated Phase Diagram (All Axes) + 3 Layers

**Axis**: Role Sequence (YES) + Output Format (YES) + Lifecycle Emphasis (YES), 3 layers declared.

### Key Criterion Deltas from V-04

**C-53**: **PASS** (strongest implementation)
- Prose block: co-location + narrative ordering ✓
- 3-column table: explicit `[C-51]` / `[C-52]` / `[C-52 secondary]` criterion references ✓
- Phase diagram: visual three-layer architecture with criterion annotations in legend ✓
- **3 layers declared**: Layer 1 (S4b partition [C-51]) + Layer 2 (evaluator-first [C-52]) + Layer 3 (phase-sequence prerequisites [C-52 secondary path]) ✓
- **Declared layer count (3) matches implemented mechanisms (3)**: S4b structural partition + EVALUATOR/AUTHOR role boundary + LIFECYCLE phase prerequisites — all three mechanisms present in V-05's architecture ✓
- C-53 pass condition: `"(c) the total number of declared layers matches the number of enforcement mechanisms implemented"` — satisfied

**Inherited PARTIAL → FULL**:
V-05 makes the strongest case for PARTIAL resolution. The 3-layer count alignment is the discriminating factor: the structural transparency criterion that caused the inherited PARTIAL fires on whether the rubric's architecture is legible and verifiable as a system. When declared layer count equals implemented mechanism count — and each layer is criterion-referenced in both tabular and diagrammatic form — the declaration is fully auditable. The inherited PARTIAL was a partial satisfaction of structural transparency; V-05's three-layer declaration with matched count closes the gap the prior PARTIAL identified.

**C-52**: **PASS** — V-05 retains EVALUATOR/AUTHOR role structure; Layer 3 (phase prerequisites) is a secondary C-52 implementation path, reinforcing rather than replacing C-52

### V-05 Score

Aspirationals: 30 PASS + 0 PARTIAL + 16 FAIL

`90 + (30 × 0.2174) + (0 × 0.1087) = 90 + 6.522 = **96.52**`

---

## Composite Scores and Ranking

| Rank | Variation | C-53 | Inherited PARTIAL | Aspirational Pass/Partial/Fail | Score |
|------|-----------|------|-------------------|-------------------------------|-------|
| 1 | **V-05** | PASS (3-layer, triple format) | → FULL | 30 / 0 / 16 | **96.52** |
| 1 | **V-04** | PASS (prose+table, criterion refs) | → FULL | 30 / 0 / 16 | **96.52** |
| 3 | V-02 | PASS (table criterion refs) | Stays PARTIAL | 29 / 1 / 16 | **96.41** |
| 3 | V-03 | PASS (phase diagram legend) | Stays PARTIAL | 29 / 1 / 16 | **96.41** |
| 5 | V-01 | PARTIAL (no criterion refs) | Stays PARTIAL | 28 / 2 / 16 | **96.30** |

**V-05 is the nominal top variation** despite tying V-04 numerically — it produces the most auditable architecture (declared 3-layer count matching 3 implemented mechanisms, triple-format reinforcement) and is the stronger candidate for inherited PARTIAL resolution if any disambiguation is needed.

**Prediction accuracy**:
- V-01 predicted 96.41 (PASS on C-53); actual 96.30 (PARTIAL — criterion number refs absent). Prediction overcounted by 0.11.
- V-02, V-03 predicted 96.41; actual 96.41. ✓
- V-04, V-05 predicted 96.41–96.63; actual 96.52. Within range. ✓

---

## Excellence Signals

**Signal 1 — Criterion reference format is the C-53 discriminating factor within prose declarations**
V-01 demonstrates that a well-structured prose compliance architecture block — with layer naming, mechanism description, inter-layer ordering, and co-location — still fails criterion (a) of C-53's pass condition if it uses `"Governing mechanism: [description]"` rather than `"Governing criterion: C-51"`. The prose form's failure mode is substituting mechanism descriptions for criterion numbers. This is not caught by the co-location or ordering requirements. The fix is not more prose — it is a structural format that forces explicit criterion numbers, which the 3-column table provides by design.

**Signal 2 — Compound prose+table is the minimal sufficient format for PARTIAL resolution**
V-02 and V-03 each independently satisfy C-53 but do not resolve the inherited PARTIAL. V-04 resolves it by combining formats: prose provides the narrative ordering declaration (addresses the *ordering relationship* transparency dimension), table provides the structured criterion reference (addresses the *auditability* transparency dimension). Neither format alone closes both dimensions. The inherited PARTIAL was split across two transparency requirements; V-04 is the first variant to address both simultaneously.

**Signal 3 — Declared layer count matching implemented mechanism count is the structural transparency closure condition**
V-05's addition of a declared Layer 3 (phase-sequence prerequisites as C-52 secondary path) makes the declared layer count exactly match the implemented mechanism count for the first time. The C-53 pass condition sub-requirement (c) explicitly governs this alignment. When the count is declared and correct, an evaluator can verify structural completeness numerically — not only qualitatively. This is the architectural difference between V-04 (2 declared, 2 implemented — correct but stated without an explicit count) and V-05 (3 declared, 3 implemented — correct with an explicit count that makes layer removal detectable).

---

```json
{"top_score": 96.52, "all_essential_pass": true, "new_patterns": ["Prose compliance architecture blocks fail C-53 criterion reference requirement when mechanism descriptions substitute for criterion numbers — the 3-column table format enforces criterion number citations structurally", "Compound prose+table is the minimal format to resolve the inherited structural transparency PARTIAL: prose closes the ordering-relationship dimension, table closes the auditability dimension; neither alone closes both", "Declared layer count matching implemented mechanism count is the structural transparency closure condition — explicit count declaration makes layer removal numerically detectable and upgrades PARTIAL to FULL"]}
```
