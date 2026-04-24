Scorecard written. Here's the summary:

---

## prove-intelligence R3 — Results

| Rank | Variation | Composite |
|------|-----------|-----------|
| 1 | V-05 | **100** |
| 2 (tie) | V-02 | **98.75** |
| 2 (tie) | V-04 | **98.75** |
| 4 (tie) | V-01 | **97.5** |
| 4 (tie) | V-03 | **97.5** |

**Floor**: 97.5 (up from 96 in R2). All five pass all essential criteria.

**What failed:**
- **C-14**: Universally solved — all five variations include verbatim WARNING with halt semantics. R3 closed the R2 gap.
- **C-15**: V-01 and V-03 fail — source blocks co-locate Excerpt + Relevance + Strength in the same block (in-block ordering). V-02's schema column exclusion is the strongest fix.
- **C-16**: V-01, V-02, V-04 fail — single ledger state written at synthesis. V-03/V-05 pass with phase-tied DRAFT/IN-PROGRESS/FINAL states.

**Three new patterns for R4:**

1. `schema-column-exclusion-as-structural-enforcement` — declaring a table schema that physically excludes interpretation columns makes C-15 impossible to violate without a visible schema error
2. `in-progress-ledger-before-gate-enables-targeted-redirect` — surfacing FC coverage gaps at search completion (before the gate fires) gives the model a specific redirect agenda rather than a vague "search more" instruction
3. `halt-instruction-semantics-vs-advisory-semantics` — "STOP. Do not proceed." vs. "before proceeding, re-search" — only the halt form requires explicit resolution before the artifact continues

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["schema-column-exclusion-as-structural-enforcement", "in-progress-ledger-before-gate-enables-targeted-redirect", "halt-instruction-semantics-vs-advisory-semantics"]}
```
---

## Scoring Formula (v3)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

---

## Detailed Criterion Scores

### Essential Criteria (60 pts total)

All five variations: **5/5 PASS → 60 pts**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 path citation | PASS | PASS | PASS | PASS | PASS |
| C-02 verbatim excerpt | PASS | PASS | PASS | PASS | PASS |
| C-03 hypothesis-linked relevance | PASS | PASS | PASS | PASS | PASS |
| C-04 per-source strength label | PASS | PASS | PASS | PASS | PASS |
| C-05 closing verdict | PASS | PASS | PASS | PASS | PASS |

---

### Recommended Criteria (30 pts total)

All five variations: **3/3 PASS → 30 pts**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 two source types | PASS | PASS | PASS | PASS | PASS |
| C-07 FC mapping | PASS | PASS | PASS | PASS | PASS |
| C-08 insider flag | PASS | PASS | PASS | PASS | PASS |

---

### Aspirational Criteria (10 pts total)

#### C-09 — Output identifies at least one internal contradiction

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 7: named conflict format — "Source A ([path]) and Source B ([path]) disagree on [X]." Explicit negative required. |
| V-02 | **PASS** | B4: row-anchored format — "Row N ([path]) and Row M ([path]) disagree on [X]." Negative case explicit. |
| V-03 | **PASS** | Phase D Contradiction Check with source-path anchors. |
| V-04 | **PASS** | Step 6 Contradiction Check with row-path references. |
| V-05 | **PASS** | Phase 4b Contradiction Check, row-anchored, negative case explicit. |

#### C-10 — Output recommends follow-up queries for evidence gaps

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 9: three-part format (`Query | Where | Addresses`), FC-linked, minimum two. |
| V-02 | **PASS** | B5: same three-part format, tied to uncovered FCs. |
| V-03 | **PASS** | Phase D: queries tied to `open` FCs from IN-PROGRESS state — leverages ledger lifecycle for query generation. |
| V-04 | **PASS** | Step 7: three-part format, tied to uncovered FCs. |
| V-05 | **PASS** | Phase 4c: tied to `open` FCs from IN-PROGRESS ledger or weakly-evidenced FCs. IN-PROGRESS state directly informs query selection. |

#### C-11 — Insider advantage treated as a hard exit condition

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 5 `## Insider Gate`: count block + WARNING emission with `STOP. Do not proceed to Step 6.` Hard gate, unconditional. Named `Gate status: PASS | BLOCKED` field. |
| V-02 | **PASS** | B1 `## Insider Gate`: count block + WARNING block with "Do not proceed to source analysis or synthesis." R3 redesign fixed R2 failure (R2 V-02 had no gate section at all). |
| V-03 | **PASS** | Phase C `## Insider Gate`: count block + WARNING block with "Do not proceed to Phase D synthesis." R3 redesign fixed R2 failure. |
| V-04 | **PASS** | `## Role Transition Gate`: count block + WARNING with `STOP. The Analyst role cannot proceed.` Gate IS the role boundary — cannot skip it. |
| V-05 | **PASS** | Phase 3 `## Insider Gate`: count block + WARNING with `STOP. Phase 4 (Analyst) cannot proceed.` Phase gate enforced. |

#### C-12 — Extraction and interpretation are structurally separated

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 3 (Candidate Files table — "Do not summarize from memory") precedes Step 4 (Source N interpretation blocks). Two named sections with distinct mandates; extraction table is upstream of all interpretation in the artifact. |
| V-02 | **PASS** | Archivist Section (table — no interpretation columns by schema) precedes Analyst Section (row-reference blocks only). Named section boundary enforces order. |
| V-03 | **FAIL** | Phase B source blocks combine `**Excerpt**` + `**Relevance**` + `**Strength**` + `**FC addressed**` in the same block, written simultaneously per source. In-block ordering. FM-12 active. Extraction is not logged before interpretation begins. |
| V-04 | **PASS** | Archivist section (extraction table, no interpretation columns) precedes Analyst section (row-reference analysis blocks). Named role boundary enforces order. Archivist mandate: "if you find yourself writing what something means, stop." |
| V-05 | **PASS** | Phase 2 Archivist (extraction, schema-enforced column set) precedes Phase 4 Analyst (interpretation, row-reference only). Phase boundary enforces order at structural level. |

#### C-13 — Falsification ledger is a first-class named artifact

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 6 `## Falsification Ledger`: named table with FC/Criterion/Source(s)/Status. Every FC must appear; `uncovered` is valid terminal status. |
| V-02 | **PASS** | B3 `## Falsification Ledger`: named table, every FC with sources and status. |
| V-03 | **PASS** | Three named ledger artifacts: DRAFT (Phase A exit), IN-PROGRESS (Phase B exit), FINAL (Phase D exit). Best C-13 in round. |
| V-04 | **PASS** | Step 5 `## Falsification Ledger`: named table, every FC with sources and status. `uncovered` valid. |
| V-05 | **PASS** | Three named ledger states tied to phase exits: DRAFT (Phase 1), IN-PROGRESS (Phase 2), FINAL (Phase 5). |

#### C-14 — Insider gate enforced by blocking WARNING text, not by count field

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Verbatim `WARNING: INSIDER GATE NOT MET` block required. `STOP. Do not proceed to Step 6. Do not write a verdict. Do not write synthesis.` Three explicit prohibitions. Named `Gate status: PASS | BLOCKED` field. Strongest HALT semantics in round. |
| V-02 | **PASS** | Verbatim `WARNING: INSIDER GATE NOT MET` + "Do not proceed to source analysis or synthesis." WARNING is B1 gate structure. |
| V-03 | **PASS** | Verbatim `WARNING: INSIDER GATE NOT MET` + "Do not proceed to Phase D synthesis." WARNING in Phase C. |
| V-04 | **PASS** | Verbatim `WARNING: INSIDER GATE NOT MET` + `STOP. The Analyst role cannot proceed.` WARNING is the role boundary — physically required to traverse it. |
| V-05 | **PASS** | Verbatim `WARNING: INSIDER GATE NOT MET` + `STOP. Phase 4 (Analyst) cannot proceed.` WARNING with four-item re-search agenda + three-step reclassification protocol. |

#### C-15 — Structural separation implemented with named roles or phases, not in-block ordering

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Step 4 Source N blocks include `**Excerpt**` + `**Relevance**` + `**Strength**` + `**FC**` co-located in the same block. Steps are numbered (Step 3/Step 4) but interpretation blocks re-include excerpt alongside analysis fields — in-block ordering persists at the source block level. FM-12 active. |
| V-02 | **PASS** | Archivist Evidence Table schema: Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider? — no Relevance/Strength/FC Status columns by schema definition. Analyst B2 blocks: Relevance/Strength/FC assessment only, no excerpt field. Schema exclusion makes in-block ordering structurally impossible. Strongest C-15 design in round. |
| V-03 | **FAIL** | Phase B source blocks combine Excerpt + Relevance + Strength + FC addressed in the same block. Named phases (Phase A/B/C/D) exist but extraction-interpretation co-location persists within each source block. In-block ordering at source level is invisible under model compression. FM-12 active. Intentional per single-axis design. |
| V-04 | **PASS** | Named sections `## Archivist` / `## Role Transition Gate` / `## Analyst` as distinct top-level structure. Archivist table: Path, Verbatim Excerpt, Source Type, Insider? — no interpretation columns. Analyst blocks: row reference + Relevance + Strength + FC, excerpt referenced from table (not re-extracted). Named structural gap is visible if either section is skipped. |
| V-05 | **PASS** | Named phases `Phase 2: Archivist (Extraction)` / `Phase 4: Analyst (Interpretation)` as distinct top-level headers. Archivist table: six columns, no interpretation fields by schema. Analyst blocks reference rows by number; excerpt field references table row, does not re-extract. Schema + phase naming provide dual enforcement. |

#### C-16 — Falsification ledger exists in multiple lifecycle states tied to phase exits

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Single ledger state: Step 6 only, written at synthesis. No pre-search baseline. No intermediate state at search completion. Uncovered FCs visible only after verdict is already framed. FM-13 active. |
| V-02 | **FAIL** | Single ledger state: B3 only, written during Analyst Section. No DRAFT state. No IN-PROGRESS state at search completion. FM-13 active. |
| V-03 | **PASS** | Three lifecycle states, all phase-tied: DRAFT at Phase A exit (all FCs `open`, pre-search baseline), IN-PROGRESS at Phase B exit (coverage visible before synthesis), FINAL at Phase D exit. "Review the IN-PROGRESS state before proceeding" instruction explicitly enables redirect before synthesis. |
| V-04 | **FAIL** | Single ledger state: Analyst Step 5 only. Archivist produces no intermediate ledger snapshot. FM-13 active. |
| V-05 | **PASS** | Three lifecycle states: DRAFT (Phase 1 exit, all FCs open), IN-PROGRESS (Phase 2 exit, search complete — "any open FC is a search gap visible now, before synthesis"), FINAL (Phase 5 exit). IN-PROGRESS state precedes the insider gate — model sees coverage gaps before gate evaluation, enabling targeted re-search with a specific FC agenda. |

---

## Composite Scores

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Asp Pass | Asp Pts | Composite | All Essential? |
|-----------|------|------|------|------|------|------|------|------|----------|---------|-----------|---------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | 6/8 | 7.5 | **97.5** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 7/8 | 8.75 | **98.75** | YES |
| V-03 | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | PASS | 6/8 | 7.5 | **97.5** | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 7/8 | 8.75 | **98.75** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 8/8 | 10.0 | **100** | YES |

**Golden threshold** (all essential + composite >= 80): all five pass. Floor rose from 96 (R2) to 97.5 (R3).

---

## Ranking

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 | V-05 | 100 | All 8 aspirationals. Five-phase architecture composes all three R3 mechanisms: schema-enforced extraction (C-15), phase-boundary gate (C-14), DRAFT/IN-PROGRESS/FINAL ledger lifecycle (C-16). |
| 2 (tie) | V-02 | 98.75 | Schema column exclusion is the strongest C-15 mechanism — makes in-block ordering structurally impossible. Single ledger state is the only miss. |
| 2 (tie) | V-04 | 98.75 | Named roles (Archivist/Role Transition Gate/Analyst) with gate as the physical role boundary. Single ledger state is the only miss. |
| 4 (tie) | V-01 | 97.5 | Strongest C-14 (three explicit STOP prohibitions + named Gate status field). Fails C-15 (in-block ordering in Step 4 source blocks) and C-16. |
| 4 (tie) | V-03 | 97.5 | Only variation to pass C-16 without C-15. IN-PROGRESS ledger enables redirect-before-gate. Fails C-12 and C-15 (in-block ordering). Confirms C-15 and C-12 co-fail when source blocks combine extraction+interpretation. |

---

## Excellence Signals

### 1. Schema column exclusion makes in-block ordering structurally impossible
V-02's Archivist Evidence Table declares a fixed schema (Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?) that physically omits Relevance, Strength, and FC Status. The model cannot add interpretation fields without visibly violating the declared schema. V-05 inherits this mechanism. Contrast with V-04, which relies on role mandate instructions ("if you find yourself writing what something means, stop") — instruction-based enforcement is weaker because instructions can be abbreviated under compression; schema violations are structurally visible.

### 2. IN-PROGRESS ledger at search completion converts coverage gaps into a redirect agenda
V-03 and V-05 emit the IN-PROGRESS ledger at search completion, before the insider gate fires. The model can see which FCs have no evidence at the moment it could still redirect search. V-01/V-02/V-04's single ledger at synthesis means uncovered FCs are only visible after the verdict is framed. V-05's instruction "any open FC is a search gap visible now, before synthesis" converts the IN-PROGRESS state from a passive record into an active instrument — it gives the model a specific FC agenda for targeted re-search rather than a vague "search more" instruction.

### 3. HALT instruction semantics versus advisory semantics
V-01 sharpens the WARNING block with three explicit prohibitions: "Do not proceed to Step 6. Do not write a verdict. Do not write synthesis." V-04/V-05 use "STOP. Phase N cannot proceed." Both are categorically different from a conditional advisory ("before proceeding, re-search"). A halt instruction requires the model to stop and explicitly resolve the condition or reclassify before the artifact can continue; an advisory can be acknowledged with a sentence and bypassed. The distinction matters under model compression, where an advisory instruction is the first thing that gets elided.

---

## Failure Mode Analysis (R3 additions)

| FM | Criterion | Affected Variations | Notes |
|----|-----------|---------------------|-------|
| FM-11 (count field, not WARNING text) | C-14 | None | All five R3 variations use verbatim WARNING block with halt semantics. C-14 was universally addressed — R3 closed the gap that affected V-02 and V-03 in R2. |
| FM-12 (in-block ordering claims separation) | C-15 | V-01, V-03 | V-01: Step 4 blocks co-locate Excerpt + Relevance + Strength + FC. V-03: Phase B source blocks co-locate extraction and interpretation. Named steps/phases exist but source-level in-block ordering persists. |
| FM-13 (single-state ledger written at synthesis) | C-16 | V-01, V-02, V-04 | All three produce a complete and accurate final ledger — C-13 passes — but in a single pass at the end. Uncovered FCs are only visible after the verdict is already written. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["schema-column-exclusion-as-structural-enforcement", "in-progress-ledger-before-gate-enables-targeted-redirect", "halt-instruction-semantics-vs-advisory-semantics"]}
```
