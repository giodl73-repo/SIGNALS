---

## discover-competitors-alt — Round 6 Results

**All five variations: 160/160**

| Rank | Variation | C-18 | C-19 | C-20 | C-21 | C-22 | Total |
|------|-----------|------|------|------|------|------|-------|
| 1 (tie) | V-01 Dual-table inertia | PASS | PASS | PASS | PASS | PASS | **160** |
| 1 (tie) | V-02 Dual loop | PASS | PASS | PASS | PASS | PASS | **160** |
| 1 (tie) | V-03 DO NOT/DO | PASS | PASS | PASS | PASS | PASS | **160** |
| 1 (tie) | V-04 SR-free | PASS | PASS | PASS | PASS | PASS | **160** |
| 1 (tie) | V-05 Conversational | PASS | PASS | PASS | PASS | PASS | **160** |

**The R5 V-05 triple synthesis is fully robust.** No variation breaks it.

### Two Open Questions Resolved

**V-03 (C-18 label boundary):** `DO NOT/DO` satisfies C-18. The invariant is **bilateral pair structure** (rejection + acceptance at phase instruction level), not the "FAILS/PASS" label specifically. Only unilateral declarative statements ("An empty row fails") fail C-18.

**V-04 (SR block necessity):** The SR preamble block is **sufficient but not necessary** for C-14 and C-17. A two-sentence opening declaration naming all three constraints and the apparatus type, combined with phase-embedded `C-XX structural constraint. Apparatus: table schema.` declarations, satisfies both. Expected was 155; actual was 160.

### Four New Patterns

1. Bilateral pair structure is C-18's invariant — any label format works
2. Opening symmetry assertion satisfies C-14/C-17 without a numbered SR block
3. Explicit constraint designation token `(C-13)` prevents C-19 ambiguity when a phase has multiple tables
4. Pre-generation loops are non-competing with C-20 — closing loop label + placement is determinative

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["DO NOT/DO bilateral pair satisfies C-18 FAILS/PASS rejection example pair requirement -- bilateral pair structure (rejection + acceptance at phase instruction level) is the invariant; FAILS/PASS label format is surface", "Phase-embedded constraint declarations with opening symmetry assertion satisfy C-14 and C-17 without numbered SR preamble block -- SR block is sufficient but not necessary; opening declaration branch of C-14 covers two-sentence meta-statement naming all three constraints and apparatus type", "Explicit constraint designation token (e.g., C-13 label or (C-13) in FAILS pair) is sufficient to prevent C-19 apparatus ambiguity when a phase produces multiple tables -- only the designated constraint table counts for apparatus uniformity", "Pre-generation integrity check loop does not confuse C-20 -- closing PRE-SUBMISSION VERIFICATION satisfies C-20 by label and placement regardless of additional loops elsewhere in the prompt"]}
```
; single-row table; either row not grounded... PASS: Both rows present and grounded..." at Phase 4 instruction level. |
| C-13 | Inertia (table) | PASS | "INERTIA MECHANISMS (C-13 structural constraint; mechanism table required)." FAILS/PASS pair at phase instruction level references mechanism table specifically. SR block item 2 labels the constraint "(C-13)." Summary table is explicitly non-substitutable. |
| C-14 | Hard-stacked | PASS | SR preamble: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema. An absent table or empty table row/cell is an observable format failure." Apparatus named. |
| C-15 | Map Position column | PASS | Explicit Map Position column; verbatim-only rule stated; "Empty or paraphrased cell is a format failure." |
| C-16 | Domain-exclusive | PASS | Standalone portability test block with exact fail condition. Applied per mechanism row. |
| C-17 | Symmetric enforcement | PASS | All-table apparatus across C-11/C-13/C-12; SR enforcement symmetry item (item 5) asserts identical three-component structure for all three. |
| C-18 | Phase-level fingerprint | **PASS** | All three structural constraints carry three-component fingerprint at phase instruction level. C-11: FAILS/PASS in Phase 1 instruction (market + positioning variants). C-13: "FAILS: Mechanism table absent; any mechanism row empty... PASS: All three mechanism rows present..." immediately after mechanism table schema. C-12: "FAILS: Whitespace table absent; single-row table... PASS: Both rows present..." at Phase 4 instruction. No constraint relies on SR block alone. |
| C-19 | Apparatus uniformity | **PASS** | C-11 = pre-map table; C-13 = mechanism table (explicitly declared as C-13 constraint; summary table explicitly declared as not the constraint); C-12 = whitespace table. All three structural constraints use table schema. Summary table is additional content, not a structural constraint competing for apparatus type. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks identical three sub-questions per SR (SR1, SR2, SR4): format artifact present? format-failure declared? FAILS/PASS pair present? Symmetric by construction. |
| C-21 | Dual-layer table enforcement | **PASS** | C-18 PASS + C-19 PASS simultaneously. Mechanism table is both the format artifact named in the fingerprint and the observable failure surface in the table structure. Summary table does not dilute C-21 because it is not designated as the C-13 structural constraint. |
| C-22 | Structural-procedural duality | **PASS** | C-19 PASS + C-20 PASS simultaneously. Table schema provides structural enforcement; symmetric loop provides procedural enforcement. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09--C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 + C-21: 5 + C-22: 5 = **160/160**

**Finding:** Dual-table inertia does not break C-19 apparatus uniformity when the mechanism table is explicitly designated as the C-13 structural constraint and the summary table is labeled as additional framing with no substitution authority. The "(C-13)" label in the FAILS/PASS pair and the "does not substitute for the mechanism table" declaration are load-bearing for C-19 disambiguation.

---

### V-02 -- Dual Loop: Pre-generation + Post-generation

**Axis:** Adds a PRE-GENERATION INTEGRITY CHECK at the opening that asks identical sub-questions about prompt completeness (format artifact declared in prompt? format-failure declared in prompt? FAILS/PASS pair present in prompt?) for SR1, SR2, SR4 before any phase runs. Closing PRE-SUBMISSION VERIFICATION loop unchanged from R5 V-05. All C-18/C-19 apparatus unchanged.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | Standard "Competitor 0: None / status quo. Threat level: HIGH. State explicitly." |
| C-02 | Focus woven | PASS | Pre-map -> mechanism table -> Map Position -> whitespace table -> combined paragraph. |
| C-03 | Threat levels | PASS | Threat column; inertia row HIGH. |
| C-04 | Whitespace | PASS | Whitespace table (2 rows) + combined paragraph required. |
| C-05 | Auto-detect | PASS | SETUP block. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows with portability test + FAILS/PASS at phase instruction level. |
| C-07 | Web-verified | PASS | WebSearch + cite inline for Phase 2 and Phase 3. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position column + whitespace table grounded in Phase 1 rows. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | Phase instruction FAILS/PASS (market + positioning) + SR block item 1. |
| C-12 | Whitespace (table) | PASS | "FAILS: Whitespace table absent... PASS: Both rows present..." at Phase 4 instruction + SR block item 4. |
| C-13 | Inertia (table) | PASS | "FAILS: Mechanism table absent; any row empty... PASS: All three rows present..." at Phase 2 instruction + SR block item 2. |
| C-14 | Hard-stacked | PASS | SR preamble: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema." |
| C-15 | Map Position column | PASS | Explicit, verbatim-only, empty-cell failure declared. |
| C-16 | Domain-exclusive | PASS | Portability test per row; standalone block. |
| C-17 | Symmetric enforcement | PASS | All-table + phase-instruction FAILS/PASS + enforcement symmetry item in SR block. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints carry three-component fingerprint at phase instruction level. Phase 1 (market/positioning variants), Phase 2 mechanism table, Phase 4 whitespace table -- all carry named format artifact + format-failure declaration + labeled FAILS/PASS pair. SR block duplicates coverage. |
| C-19 | Apparatus uniformity | **PASS** | All-table: pre-map table, mechanism table, whitespace table. |
| C-20 | Symmetric loop | **PASS** | Closing PRE-SUBMISSION VERIFICATION satisfies C-20 cleanly: identical three sub-questions per SR constraint (format artifact present? format-failure declared? FAILS/PASS pair present?). Opening PRE-GENERATION INTEGRITY CHECK is labeled differently, checks prompt completeness rather than output completeness, and is placed before the phases. The closing loop's label ("PRE-SUBMISSION VERIFICATION") and placement (after all phases) are the determinative signals for C-20. Having two loops does not confuse C-20 -- the pre-generation loop is additive, not competing. |
| C-21 | Dual-layer table enforcement | **PASS** | C-18 PASS + C-19 PASS. |
| C-22 | Structural-procedural duality | **PASS** | C-19 PASS + C-20 PASS. The closing loop is the procedural layer; the table schema is the structural layer. Pre-generation loop adds a third layer (prompt-completeness check) but does not substitute for the closing loop. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09--C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 + C-21: 5 + C-22: 5 = **160/160**

**Finding:** The closing PRE-SUBMISSION VERIFICATION loop satisfies C-20 regardless of whether an additional opening loop is present. C-20's "closing pre-submission" criterion is satisfied by loop label + placement (post-phase), not by uniqueness. A pre-generation integrity check is additive and non-competing.

---

### V-03 -- Active Imperative Register

**Axis:** All instructions converted to active imperative (DO NOT / DO pairs instead of FAILS / PASS pairs). Structural apparatus identical to R5 V-05: all-table, phase-instruction pairs at all three constraints, symmetric closing verification loop. The pre-submission loop asks "rejection example pair present (DO NOT/DO)?" instead of "FAILS/PASS pair present?"

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | "Name Competitor 0 as 'None / status quo.' State threat level HIGH explicitly." |
| C-02 | Focus woven | PASS | Pre-map table -> mechanism table -> Map Position column -> whitespace table -> combined paragraph. |
| C-03 | Threat levels | PASS | Threat column; inertia row HIGH. |
| C-04 | Whitespace | PASS | Whitespace table (2 rows) required; combined paragraph required. |
| C-05 | Auto-detect | PASS | "SETUP: Detect the product domain. Read README, CLAUDE.md, package.json, Glob-discoverable files. Do not ask the user. Infer everything." |
| C-06 | Inertia stickiness | PASS | Three labeled mechanism slots with portability test. DO NOT/DO pairs at phase instruction level requiring domain specificity. |
| C-07 | Web-verified | PASS | "Run the portability test on every row. Use WebSearch if needed. Cite inline." + Phase 3 verify via WebSearch. |
| C-08 | AMEND 3 items | PASS | "AMEND: Exactly 3 items. Input change + output change. Specific." |
| C-09 | Cross-dimensional | PASS | Map Position column + whitespace table grounded in Phase 1. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | DO NOT/DO pair at Phase 1 instruction level (market + positioning variants). Named format artifact (table schema). SR block item 1 carries DO NOT/DO pair. |
| C-12 | Whitespace (table) | PASS | "DO NOT: Build only one row. Leave either row without Phase 1 or Map Position grounding. Omit the combined paragraph. DO: Fill both rows with grounded findings..." at Phase 4 instruction. |
| C-13 | Inertia (table) | PASS | "DO NOT: Omit the mechanism table. Leave any row empty. Write row content that passes the portability test. DO: Fill all three rows with content so domain-specific it would be obviously wrong..." immediately after mechanism table schema at Phase 2 instruction. |
| C-14 | Hard-stacked | PASS | SR preamble: "STRUCTURAL REQUIREMENTS: Use table schema for every structural constraint. Do not use prose blocks, labeled-slot text, or dual-line templates for SR1, SR2, or SR4." Names apparatus (table schema) and covers all three constraints. |
| C-15 | Map Position column | PASS | Explicit; "Do not paraphrase. Do not generalize. An empty cell or paraphrased label fails." |
| C-16 | Domain-exclusive | PASS | Standalone portability test block with exact fail condition. |
| C-17 | Symmetric enforcement | PASS | All-table apparatus declared; SR block item 5 asserts enforcement symmetry: "Confirm SR1 (C-11), SR2 (C-13), and SR4 (C-12) each carry a named format artifact, a failure statement, and a rejection example pair." Symmetry asserted, not listed separately. |
| C-18 | Phase-level fingerprint | **PASS** | All three structural constraints carry three-component fingerprint at phase instruction level: (1) named format artifact (pre-map table / mechanism table / whitespace table), (2) format-failure declaration embedded in DO NOT clause ("DO NOT: Omit the mechanism table"), (3) rejection example pair (DO NOT/DO). The R5 precedent excluding unilateral declarative statements ("An empty row fails") does not apply -- DO NOT/DO is a bilateral pair, not a unilateral declaration. PRE-SUBMISSION VERIFICATION asks "rejection example pair present (DO NOT/DO)?" -- self-identifying the pair type, confirming all three constraints carry it. |
| C-19 | Apparatus uniformity | **PASS** | SR preamble mandates table schema for SR1, SR2, SR4 exclusively; DO NOT explicitly prohibits prose blocks, labeled-slot text, dual-line templates. Phase 1 pre-map table, Phase 2 mechanism table, Phase 4 whitespace table -- all table schema by construction. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks identical three sub-questions per constraint (format artifact present? format-failure declared? rejection example pair present (DO NOT/DO)?). Structure is symmetric; sub-question 3 uses "rejection example pair (DO NOT/DO)" rather than "FAILS/PASS pair" -- C-20 requires symmetry of structure, not exact wording of sub-question 3 (confirmed by R5 precedent). |
| C-21 | Dual-layer table enforcement | **PASS** | C-18 PASS + C-19 PASS. |
| C-22 | Structural-procedural duality | **PASS** | C-19 PASS + C-20 PASS. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09--C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 + C-21: 5 + C-22: 5 = **160/160**

**Finding (V-03 boundary resolved):** DO NOT/DO satisfies C-18's "FAILS/PASS rejection example pair" requirement. The distinguishing property is bilateral pair structure (rejection example + acceptance example at phase instruction level), not the specific label format "FAILS:" / "PASS:". The R5 precedent only excluded unilateral declarative statements ("An empty row fails" -- single sentence, no acceptance counterpart). A full bilateral pair in any label format satisfies C-18.

---

### V-04 -- SR-Free Phase-Embedded Declarations

**Axis:** Opening SR block (numbered checklist) eliminated entirely. Each phase carries full apparatus inline: "C-11 structural constraint. Apparatus: table schema." / "C-13 structural constraint. Apparatus: table schema. An absent table or empty row fails." / "C-12 structural constraint. Apparatus: table schema." Opening two-sentence statement declares all three enforce via table schema. FAILS/PASS pairs present at all three phase instruction levels. Symmetric verification loop present.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | "Competitor 0: None / status quo. Threat level: HIGH. State explicitly." |
| C-02 | Focus woven | PASS | Pre-map -> mechanism table -> Map Position -> whitespace table -> combined paragraph. |
| C-03 | Threat levels | PASS | Threat column; inertia HIGH. |
| C-04 | Whitespace | PASS | Whitespace table with both rows + combined paragraph required. |
| C-05 | Auto-detect | PASS | SETUP block. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows with portability test; FAILS/PASS at phase instruction level. |
| C-07 | Web-verified | PASS | WebSearch + cite inline. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position column + whitespace table grounded in Phase 1. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | Phase 1 instruction: "C-11 structural constraint. Apparatus: table schema. Required when focus is provided." FAILS/PASS at phase instruction for both market/positioning variants. Named format artifact. |
| C-12 | Whitespace (table) | PASS | Phase 4 instruction: "C-12 structural constraint. Apparatus: table schema." FAILS/PASS pair at instruction level. |
| C-13 | Inertia (table) | PASS | Phase 2 instruction: "C-13 structural constraint. Apparatus: table schema. An absent table or empty row fails." FAILS/PASS pair at instruction level. |
| C-14 | Hard-stacked | **PASS** | Opening statement: "All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace) enforce via table schema. An absent table or empty row/cell is an observable format failure." Explicit opening declaration naming all three constraints and the apparatus type. C-14 pass condition says "SR block or opening declaration" -- satisfied via the opening declaration branch without requiring a numbered SR checklist block. |
| C-15 | Map Position column | PASS | Explicit; "Verbatim -- do not paraphrase. Empty or paraphrased cell is a format failure." |
| C-16 | Domain-exclusive | PASS | Portability test with standalone block. |
| C-17 | Symmetric enforcement | **PASS** | Opening statement asserts symmetry across all three constraints ("All three structural constraints... enforce via table schema") -- symmetry assertion, not separate listing. Phase-embedded declarations ("C-11/C-13/C-12 structural constraint. Apparatus: table schema.") produce identical enforcement apparatus at each phase. Verification loop confirms symmetry by applying identical sub-questions to all three. C-17 requires assertion of symmetry ("not by listing each separately but by asserting symmetry") -- the opening statement satisfies this; the SR block is one path to C-17, not the only path. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints carry three-component fingerprint at phase instruction level. C-11: FAILS/PASS in Phase 1 instruction. C-13: "FAILS: Mechanism table absent; any row empty... PASS: All three rows present..." at Phase 2 instruction. C-12: "FAILS: Whitespace table absent; single-row table... PASS: Both rows present and grounded..." at Phase 4 instruction. |
| C-19 | Apparatus uniformity | **PASS** | Phase 1 pre-map table, Phase 2 mechanism table, Phase 4 whitespace table -- all table schema. Opening statement mandates table schema for all three. Uniformity by construction. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION asks identical three sub-questions per C-11, C-13, C-12: format artifact present? format-failure declared? FAILS/PASS pair present? Loop uses constraint IDs rather than SR-block IDs -- maps to same three structural constraints. Symmetric by construction. |
| C-21 | Dual-layer table enforcement | **PASS** | C-18 PASS + C-19 PASS. |
| C-22 | Structural-procedural duality | **PASS** | C-19 PASS + C-20 PASS. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09--C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 + C-21: 5 + C-22: 5 = **160/160**

**Finding (V-04 boundary resolved):** C-14 and C-17 do not require a numbered SR preamble block. An opening meta-declaration naming all three constraints and the apparatus type satisfies C-14. Identical phase-embedded apparatus declarations + a symmetry-asserting opening statement satisfy C-17. The SR block is a sufficient mechanism for both, not a necessary one. Expected score was 155; actual is 160 -- the SR block was not load-bearing for C-14 or C-17.

---

### V-05 -- Conversational Inertia Framing + Technical Apparatus

**Axis:** Phase 2 opens with a plain-language lead paragraph ("The most dangerous competitor in almost every product market is not a named vendor -- it is the team's existing way of doing things...") before the mechanism table. SR block, portability test, Phase 1, Phase 3, Phase 4, and verification loop are identical to R5 V-05.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Inertia-first | PASS | Conversational framing explicitly names status quo as the primary threat before named competitors. "Competitor 0: None / status quo. Threat level: HIGH. State explicitly." Inertia-first is reinforced by narrative framing. |
| C-02 | Focus woven | PASS | Pre-map -> mechanism table -> Map Position -> whitespace table -> combined paragraph. |
| C-03 | Threat levels | PASS | Threat column; inertia HIGH. |
| C-04 | Whitespace | PASS | Whitespace table (2 rows) + combined paragraph required. |
| C-05 | Auto-detect | PASS | SETUP block unchanged. |
| C-06 | Inertia stickiness | PASS | Mechanism table rows with portability test + FAILS/PASS at phase instruction level. Narrative paragraph reinforces mechanism specificity intent. |
| C-07 | Web-verified | PASS | WebSearch + cite inline. |
| C-08 | AMEND 3 items | PASS | Explicit. |
| C-09 | Cross-dimensional | PASS | Map Position column + whitespace table grounded in Phase 1. |
| C-10 | Table stakes | PASS | "Reference at least one Phase 1 data point per item." |
| C-11 | Pre-map table | PASS | Phase instruction FAILS/PASS for both variants + SR block item. |
| C-12 | Whitespace (table) | PASS | Phase instruction FAILS/PASS + SR block item. |
| C-13 | Inertia (table) | PASS | SR block item 2 declares mechanism table as structural constraint. Phase 2 instruction places mechanism table after the narrative paragraph and immediately presents FAILS/PASS pair. Narrative paragraph is framing, not a C-13 compliance artifact; it does not substitute for the labeled mechanism table. Narrative framing before the mechanism table does not weaken C-13. |
| C-14 | Hard-stacked | PASS | SR preamble: "All three primary structural requirements (SR1, SR2, SR4) enforce via table schema." Unchanged from R5 V-05. |
| C-15 | Map Position column | PASS | Explicit, verbatim-only. |
| C-16 | Domain-exclusive | PASS | Portability test per row; standalone block. |
| C-17 | Symmetric enforcement | PASS | All-table + phase-instruction FAILS/PASS + SR block enforcement symmetry item. Unchanged from R5 V-05. |
| C-18 | Phase-level fingerprint | **PASS** | All three constraints carry three-component fingerprint at phase instruction level. Phase 2: conversational paragraph is before the mechanism table; FAILS/PASS pair is at the mechanism table instruction, proximate to the structural constraint. The pair is not displaced by the framing paragraph. |
| C-19 | Apparatus uniformity | **PASS** | All-table: pre-map table, mechanism table, whitespace table. Unchanged. |
| C-20 | Symmetric loop | **PASS** | PRE-SUBMISSION VERIFICATION unchanged from R5 V-05. |
| C-21 | Dual-layer table enforcement | **PASS** | C-18 PASS + C-19 PASS. |
| C-22 | Structural-procedural duality | **PASS** | C-19 PASS + C-20 PASS. |

**Score:** Essential 60/60 + Recommended 30/30 + C-09--C-17: 45/45 + C-18: 5 + C-19: 5 + C-20: 5 + C-21: 5 + C-22: 5 = **160/160**

**Finding:** Conversational framing in Phase 2 is neutral for all structural criteria. A narrative paragraph before the mechanism table does not weaken C-13 (mechanism table unchanged), C-14 (SR block unchanged), or C-18 (FAILS/PASS pair proximate to the mechanism table, not the narrative). Register mixing does not affect apparatus uniformity or procedural verification.

---

### Composite Scores

| Rank | Variation | Essential | Rec | Asp C-09-17 | C-18 | C-19 | C-20 | C-21 | C-22 | Total |
|------|-----------|-----------|-----|-------------|------|------|------|------|------|-------|
| 1 (tie) | V-01 | 60 | 30 | 45 | 5 | 5 | 5 | 5 | 5 | **160** |
| 1 (tie) | V-02 | 60 | 30 | 45 | 5 | 5 | 5 | 5 | 5 | **160** |
| 1 (tie) | V-03 | 60 | 30 | 45 | 5 | 5 | 5 | 5 | 5 | **160** |
| 1 (tie) | V-04 | 60 | 30 | 45 | 5 | 5 | 5 | 5 | 5 | **160** |
| 1 (tie) | V-05 | 60 | 30 | 45 | 5 | 5 | 5 | 5 | 5 | **160** |

All five variations score 160/160. All essential criteria pass across all five variations. The R5 V-05 triple synthesis is **fully robust** across all R6 structural variation axes.

---

### R6 Open Questions Resolved

**V-03 (C-18 label boundary):** DO NOT/DO is functionally equivalent to FAILS/PASS for C-18. The distinguishing property of a "FAILS/PASS rejection example pair" is **bilateral pair structure** -- rejection example + acceptance example at phase instruction level -- not the specific label format. The R5 precedent excluded unilateral declarative statements ("An empty row fails") because they are single-sentence failure declarations without an acceptance counterpart. A full bilateral pair in any label format satisfies C-18.

**V-04 (C-17 preamble requirement):** Phase-embedded declarations with an opening symmetry assertion satisfy C-14 and C-17 without a numbered SR preamble block. The SR block is a **sufficient but not necessary** mechanism. C-14's "opening declaration" branch and C-17's "explicitly confirms that the same apparatus type is present across all three" requirement are both satisfied by an opening statement naming all three constraints and the apparatus type.

---

### R6 Findings vs. Hypotheses

| Variation | Expected | Actual | Hypothesis confirmed? |
|-----------|----------|--------|----------------------|
| V-01 | 160 | 160 | Yes -- dual-table inertia neutral for C-19 when mechanism table labeled as C-13 constraint |
| V-02 | 160 | 160 | Yes -- pre-generation loop does not confuse C-20; closing loop satisfies by label + placement |
| V-03 | 160 | 160 | Yes -- DO NOT/DO satisfies C-18; label format is surface |
| V-04 | **155** | **160** | **No** -- C-14 and C-17 both survived SR block removal; phase-embedded declarations sufficient |
| V-05 | 160 | 160 | Yes -- conversational framing neutral for all structural criteria |

V-04 is the only variation where actual exceeded expected. The SR block was hypothesized to be load-bearing for C-14/C-17; it is not.

---

### Excellence Signals

1. **Explicit constraint designation token prevents C-19 apparatus ambiguity (V-01):** When a phase produces multiple tables, declaring one as "the C-13 structural constraint" and the other as "additional framing" is sufficient to preserve apparatus uniformity scoring. The "(C-13)" label in the FAILS/PASS pair is a minimal disambiguation token.

2. **Opening symmetry assertion is a portable C-14/C-17 mechanism (V-04):** Two sentences naming all three constraints and the apparatus type carry the full weight of C-14 + C-17 without a numbered SR checklist. This is the minimum viable meta-declaration form.

3. **Bilateral pair structure is C-18's invariant, not label format (V-03):** Any format that produces rejection-example + acceptance-example at phase instruction level satisfies C-18. DO NOT/DO, IF/THEN, WRONG/RIGHT -- any bilateral pair works. The R5 failure mode (declarative single-sentence) is the thing C-18 excludes, not the FAILS/PASS label specifically.

4. **Pre-generation loops are non-competing with C-20 (V-02):** A prompt can carry multiple verification loops at different lifecycle stages without C-20 ambiguity, because C-20's "closing pre-submission" is determined by label and placement, not by uniqueness.

---

### Rubric Writing Artifact

`simulations/quest/rubrics/discover-competitors-alt-rubric-v6-2026-03-17.md` -- v6 rubric as provided.
`simulations/quest/scorecards/discover-competitors-alt-scorecard-R6-2026-03-17.md` -- this document.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["DO NOT/DO bilateral pair satisfies C-18 FAILS/PASS rejection example pair requirement -- bilateral pair structure (rejection + acceptance at phase instruction level) is the invariant; FAILS/PASS label format is surface", "Phase-embedded constraint declarations with opening symmetry assertion satisfy C-14 and C-17 without numbered SR preamble block -- SR block is sufficient but not necessary; opening declaration branch of C-14 covers two-sentence meta-statement naming all three constraints and apparatus type", "Explicit constraint designation token (e.g., C-13 label or (C-13) in FAILS pair) is sufficient to prevent C-19 apparatus ambiguity when a phase produces multiple tables -- only the designated constraint table counts for apparatus uniformity", "Pre-generation integrity check loop does not confuse C-20 -- closing PRE-SUBMISSION VERIFICATION satisfies C-20 by label and placement regardless of additional loops elsewhere in the prompt"]}
```
