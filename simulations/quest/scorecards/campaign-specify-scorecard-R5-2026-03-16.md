# Scorecard — campaign-specify / Round 5

**Rubric**: v5 (15 aspirational, 3 new: C-21 citation lock, C-22 full gate chain, C-23 existence-status index)
**Formula**: `(essential/5 * 60) + (rec/3 * 30) + (asp/15 * 10)`

---

## Scoring Matrix

### Essential (C-01–C-05) — all variations

All five variations inherit the same essential skeleton: three required artifacts with write instructions, six spec sections explicitly named, proposal with three options + Do Nothing + all fields, pitch with Exec/Dev/Maker versions + Anti-Positioning, and Step 0a inertia costs flowing consistently through all artifacts. **5/5 PASS across all variations.**

### Recommended (C-06–C-08) — all variations

All five include: Self-Review with "No gaps found fails" (C-06); Anti-Positioning as an explicit named section (C-07); Defeating [Other Option] with "specific trade-off traceable to a risk, effort, or cons field — not a preference statement" (C-08). **3/3 PASS across all variations.**

---

## V-01 — Citation Lock (C-21 target)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 0d scout glob + per-phase targeted namespace pulls (scout/, scout-feasibility/, scout-positioning/) |
| C-10 | PASS | Step 0c voice contracts define distinct audience registers; pitch versions each lead with audience-specific cost |
| C-11 | PASS | "If any artifact is missing: write it now before continuing. Do not emit the final index until all three files exist on disk." Active recovery, not advisory |
| C-12 | PASS | Step 0c voice contracts defined in Phase 0 before Phase 1 begins |
| C-13 | PASS | Phase 1 → scout/ broadly; Phase 2 → scout-feasibility/; Phase 3 → scout-positioning/ |
| C-14 | PASS | Step 0a: exec cost names consequence not category; dev cost names friction not feeling; maker cost names blocked step |
| C-15 | PASS | "Defeating Do Nothing: Do Nothing perpetuates [cite cost]... We choose to act because [rationale]" — explicit defeat by name with specific cost |
| C-16 | PASS | `**Defeating Do Nothing**` on its own line (standalone bold header, not bold+colon inline); content follows on next line |
| C-17 | PASS | STABILITY CITATION RECORD established in Step 0b (Form A/B), pasted verbatim in Phase 2 Defeating Do Nothing block — two-location requirement met |
| C-18 | PASS | Two intra-Phase 0 gates: "Do not advance to Step 0b until..." and "Do not advance to Step 0c until..." |
| C-19 | **FAIL** | No inline write gates at production points. Risk note confirms: "C-19 and C-20 are not targeted." |
| C-20 | **FAIL** | No voice differentiation save gate. Not targeted by design |
| C-21 | PASS | Three-point enforcement: (1) named STABILITY CITATION RECORD block in Step 0b with Form A/B, (2) "PASTE THE STEP 0b STABILITY CITATION RECORD VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the exact Form A or Form B sentence." (3) Completion Check requires "State one of: CITATION CONFIRMED / CITATION MISSING" — affirmative declaration, not checkbox |
| C-22 | PASS | Phase 0 has 4 steps; 0d (scout pull) is terminal (no subsequent Phase 0 step). Non-terminal chain is 0a→0b→0c with 2 explicit gates. Consistent with R4 analysis that found V-01 earning C-22 under this terminal-exclusion interpretation |
| C-23 | **FAIL** | Completion Check lists artifact paths and uses numbered existence checks, but no named "COMPLETION INDEX" block with three-column table and per-row "[exists / missing]" status field. Risk note confirms: "C-23 is not targeted." |

**Aspirational: 12/15** | **Composite: 60 + 30 + 8.0 = 98.0**

---

## V-02 — Explicit Full Gate Chain (C-22 target)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-15 | PASS | Same foundations as V-01 |
| C-16 | PASS | `**Defeating Do Nothing**` as standalone bold header before content block |
| C-17 | PASS | Step 0b Form A/B; Phase 2 "Cite the Step 0b stability assessment verbatim: paste Form A or Form B here" |
| C-18 | PASS | Subsumed by C-22 full chain |
| C-19 | **FAIL** | No inline write gates. Write instructions are collocated but not blocking gates with "Do not begin Phase N+1 until..." phrasing |
| C-20 | **FAIL** | Not targeted |
| C-21 | **FAIL** | Final index says "Step 0b stability form used (Form A / Form B)" — records which form was used but does NOT include "CITATION CONFIRMED / CITATION MISSING" affirmative declaration. Risk note: "C-21's Completion Check confirmation is absent." The third leg of C-21 (citation confirmation) is missing |
| C-22 | PASS | Phase 0 header: `PHASE 0 GATE CHAIN: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Step 0d terminal`. Each gate labeled `--- GATE N: Do not advance... ---`. Step 0d explicitly labeled `TERMINAL — no subsequent Phase 0 step`. Unambiguous full coverage — all three non-terminal→next transitions gated |
| C-23 | **FAIL** | Completion Check uses numbered existence checks ("if missing: write now") but no named COMPLETION INDEX block with three-column table and per-artifact "[exists / missing]" status |

**Aspirational: 11/15** | **Composite: 60 + 30 + 7.3 = 97.3**

---

## V-03 — Existence-Status Completion Index (C-23 target)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-14 | PASS | Same foundations |
| C-15 | PASS | Defeating Do Nothing block cites specific audience cost + stability cite + "We choose to act because [rationale]" |
| C-16 | **FAIL** | `**Defeating Do Nothing**: Do Nothing perpetuates...` — bold+colon inline pattern. "**Defeating Do Nothing**" appears with a colon immediately followed by content on the same line. Rubric: "A bold label followed immediately by content on the same line (bold+colon inline pattern) does not pass; the label must stand alone as a dedicated header." |
| C-17 | PASS | Step 0b establishes Form A/B; Phase 2 Defeating Do Nothing says "cite the Form A or Form B text" — two-location requirement met |
| C-18 | PASS | One intra-Phase 0 gate: "Do not advance to Step 0b until all three costs are named." Satisfies C-18's "at least one" minimum |
| C-19 | PASS | Three `>> PHASE N WRITE GATE <<` blocks, each collocated with artifact production, each with "Confirm the file was written. If it does not exist: write it again now. Do not begin Phase N+1 until [file] exists on disk." |
| C-20 | **FAIL** | Not targeted — risk note confirms |
| C-21 | **FAIL** | Step 0b has Form A/Form B but no named STABILITY CITATION RECORD label. Phase 2 says "cite the Form A or Form B text" — references by concept, not by record name. COMPLETION INDEX has no "CITATION CONFIRMED / CITATION MISSING" row. All three legs of C-21 are weakened or absent |
| C-22 | **FAIL** | Only one intra-Phase 0 gate (0a→0b). Transitions 0b→0c and 0c→0d have no explicit "do not advance" gates. C-22 requires every adjacent non-terminal transition to be gated |
| C-23 | PASS | Named `## COMPLETION INDEX` block with explicit structural label: "Structurally distinct from the write gates (which fire at production time) and from the recovery steps (which are embedded in each write gate)." Three-column table `| Artifact | Path | Status |` with `[exists / missing]` fill-in per row. Recovery: "If status is 'missing': write the artifact now." |

**Aspirational: 11/15** | **Composite: 60 + 30 + 7.3 = 97.3**

*Note: Author predicted 93.3 (14/15 asp). Actual scoring reveals C-16 fail (bold+colon inline), C-20 fail (not targeted per risk note), reducing to 11/15. Author's prediction likely used a pre-v5 formula.*

---

## V-04 — C-21 + C-22 + C-23 Combined

Built on R4 V-04 base (holding C-16, C-17, C-18, C-19) + three new mechanisms.

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-15 | PASS | Same foundations; Step 0a quantification prompts added |
| C-16 | PASS | `#### Defeating Do Nothing` as level-4 header, structurally separate from `#### Defeating [Other Option Name]`. Explicit disqualification in Note |
| C-17 | PASS | STABILITY CITATION RECORD in Step 0b; "PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize. Do not paraphrase." |
| C-18 | PASS | Three gates (Gate 1: 0a→0b, Gate 2: 0b→0c, Gate 3: 0c→0d) for four-step Phase 0 |
| C-19 | PASS | `>> SPEC WRITE GATE <<`, `>> PROPOSAL WRITE GATE <<`, `>> PITCH WRITE GATE <<` — each collocated, each with "Do not begin Phase N+1 until this file exists on disk" |
| C-20 | **FAIL** | Not included per design. Risk note: "C-20 (voice differentiation save gate) is not included. Predicted score: 14/15." |
| C-21 | PASS | Three-point: (1) named STABILITY CITATION RECORD block in Step 0b, (2) "PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B sentence character for character," (3) COMPLETION INDEX: "STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block: CITATION CONFIRMED / CITATION MISSING (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)" |
| C-22 | PASS | "Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Step 0d terminal" in Phase 0 header. Each gate labeled. Step 0d `[TERMINAL]`. COMPLETION INDEX confirms "3 gates passed" |
| C-23 | PASS | Named `## COMPLETION INDEX` block, labeled as distinct from write gates and recovery steps. Three-column table with `[exists / missing]` per row. Recovery embedded. Additional CITATION CONFIRMED/MISSING check in self-scoring index |

**Aspirational: 14/15** | **Composite: 60 + 30 + 9.3 = 99.3**

---

## V-05 — Full Synthesis (C-19 + C-20 + C-21 + C-22 + C-23)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 0d glob with per-artifact routing; per-phase targeted re-queries |
| C-10 | PASS | Step 0c voice contracts (exec: outcomes/risk, dev: capability/friction, maker: workflow plain) anchor pitch openings. VOICE DIFFERENTIATION GATE enforces distinct opening frames with conditional rewrite trigger |
| C-11 | PASS | Each write gate: "If the file does not exist: write it now before continuing." COMPLETION INDEX adds second recovery path: "If any status is 'missing': write that artifact now, then update the row." |
| C-12 | PASS | Five-step Phase 0 (0a inertia, 0b stability, 0c voice contracts, 0d scout, 0e baseline compile) all precede Phase 1 |
| C-13 | PASS | Step 0d broad `scout/**/*.md`; Phase 2 `scout-feasibility/`; Phase 3 `scout-positioning/` |
| C-14 | PASS | Step 0a: per-audience costs with quantification prompts ("$X quarterly", "3-5 hours per sprint") |
| C-15 | PASS | `#### Defeating Do Nothing` block: names Do Nothing explicitly, cites Step 0e decisive cost, pastes STABILITY CITATION RECORD verbatim, "We choose to act because [rationale]" |
| C-16 | PASS | `#### Defeating Do Nothing` as standalone level-4 header, structurally separate from `#### Defeating [Other Option Name]`. Note explicitly disqualifies combined paragraph form |
| C-17 | PASS | STABILITY CITATION RECORD: established in Step 0b, compiled verbatim into Step 0e baseline, pasted verbatim in Phase 2. Three-anchor chain makes citation loss nearly impossible |
| C-18 | PASS | Four gates (subsumed by C-22 full chain coverage) |
| C-19 | PASS | `>> SPEC WRITE GATE <<`, `>> PROPOSAL WRITE GATE <<`, `>> PITCH WRITE GATE <<` — each at production point, each blocking next phase until file is on disk. Structurally distinct from COMPLETION INDEX (emitted later) |
| C-20 | PASS | `>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<` extracts first sentence of each version, specifies expected frames (exec: business cost/risk; dev: tool friction/capability gap; maker: blocked step), conditional: "IF any two openings are the same or use the same frame: Rewrite the duplicated version(s)... Do not save the pitch until all three opening frames are distinct." Save gate collocated AFTER voice gate passes |
| C-21 | PASS | Three-point: (1) named STABILITY CITATION RECORD block in Step 0b; (2) Phase 2 "PASTE THE STEP 0e STABILITY LINE VERBATIM HERE — the Form A or Form B sentence from Step 0b as recorded in Step 0e. Do not summarize. Do not paraphrase. Character for character."; (3) Self-scoring index row: "STABILITY CITATION RECORD — pasted verbatim in Defeating Do Nothing block | CITATION CONFIRMED / CITATION MISSING" — affirmative declaration with recovery |
| C-22 | PASS | Phase 0 header: "Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Gate 4 (0d→0e) | Step 0e terminal." Four labeled `--- GATE N: Do not advance... ---` blocks. Step 0e explicitly `[TERMINAL]`. Self-scoring index: "Phase 0 gate chain — 4 gates passed | Gate 1: yes/no | Gate 2: yes/no | Gate 3: yes/no | Gate 4: yes/no" |
| C-23 | PASS | Named `## COMPLETION INDEX` labeled as "structurally distinct from: (1) write gates... (2) the voice differentiation gate... (3) the recovery instructions embedded in each write gate." Three-column table with `[exists / missing]` required fill-in per row. Recovery: "If any status is 'missing': write that artifact now, then update the row to 'exists' before emitting the rest of this index." |

**Aspirational: 15/15** | **Composite: 60 + 30 + 10.0 = 100.0**

---

## Rankings

| Rank | Variation | Essential | Rec | Asp | Composite | Notes |
|------|-----------|-----------|-----|-----|-----------|-------|
| 1 | **V-05** | 5/5 | 3/3 | 15/15 | **100.0** | All 15 aspirational earned |
| 2 | **V-04** | 5/5 | 3/3 | 14/15 | **99.3** | Misses only C-20 (voice gate) |
| 3 | **V-01** | 5/5 | 3/3 | 12/15 | **98.0** | Misses C-19, C-20, C-23 |
| 4 | **V-02** | 5/5 | 3/3 | 11/15 | **97.3** | Misses C-19, C-20, C-21, C-23 |
| 4 | **V-03** | 5/5 | 3/3 | 11/15 | **97.3** | Misses C-16, C-20, C-21, C-22 |

*V-02 and V-03 tie at 97.3 but fail on different criteria.*

---

## Excellence Signals from V-05

**Signal 1: Step 0e as compilation bridge**
The terminal Phase 0 step (Step 0e "Do Nothing Baseline") copies all Phase 0 outputs verbatim — inertia costs and STABILITY CITATION RECORD — into a single pre-wired block that Phase 2 references directly. This means cross-phase citation is structurally automatic: the model copies from Step 0e, not from Phase 0 Step 0b from memory. This pattern — a terminal compilation step that pre-assembles the next phase's reference inputs — is not captured by any existing criterion. It goes beyond C-17 and C-21 to eliminate citation loss at the architectural level.

**Signal 2: Per-gate self-scoring in COMPLETION INDEX**
The self-scoring index extends C-23's existence-status pattern to criterion-level compliance tracking: each Phase 0 gate has its own "Gate N: yes/no" row, citation confirmation has its own "CITATION CONFIRMED / CITATION MISSING" row, and voice differentiation result has "distinct / rewritten-to-distinct." This transforms the COMPLETION INDEX from an artifact existence log into a per-criterion audit trail. A model that fills it honestly will self-expose missed gates or missing citations before stopping.

**Observation on V-03's C-16 failure**
V-03 is the only variation that uses the bold+colon inline pattern (`**Defeating Do Nothing**: content on same line`) while V-04 and V-05 use `#### Defeating Do Nothing` as a level-4 header. This is a recurrent fork: authors writing from prose templates default to inline bold labels; authors using heading notation get C-16 automatically. The distinction is structurally subtle but determinative.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Step 0e compilation bridge — a terminal Phase 0 step that copies all Phase 0 outputs verbatim into a pre-assembled baseline block, making cross-phase citation structurally automatic rather than memory-dependent", "Per-gate self-scoring index — the COMPLETION INDEX extends the existence-status pattern to criterion-level compliance tracking, with individual gate yes/no rows and CITATION CONFIRMED/MISSING affirmative declarations that make model compliance self-auditing before the skill stops"]}
```
