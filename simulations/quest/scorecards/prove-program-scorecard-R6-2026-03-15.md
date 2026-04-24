## prove-program R6 — Scoring (v6 Rubric, 160 pts)

---

### V-01 — Role sequence: 4-role (FRAMER/PLANNER/RUNNER/EVALUATOR)

**Essential (60 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Hypothesis pre-commitment | PASS | FRAMER Phase 1 has named "Hypothesis Pre-Commitment" section with positive-form hypothesis before PLANNER names any experiment |
| C-02 Experiment plan >=2 types | PASS | PLANNER Phase 1B table requires distinct types with rationale; GATE-P enforces >=2 distinct types |
| C-03 Feed-forward | PASS | RUNNER E-02 INPUT section explicitly consumes E-01 output verbatim with local contract clause |
| C-04 Synthesis contrast | PASS | EVALUATOR Synthesis: "What we thought: [hypothesis verbatim]" + "What we actually learned: [must differ]" + FAIL condition |
| C-05 Qx.md at correct path | PASS | Artifact section writes `simulations/prove/research/{{topic}}-research-{{date}}.md`; >=4 labeled sections |

**Essential: 60/60**

**Recommended (30 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Principles >=2 | PASS | EVALUATOR Principles table with P-01/P-02, source finding required, FAIL for <2 or truisms |
| C-07 Confidence per finding | PASS | EVALUATOR Findings table has high/medium/low per row + Evidence basis column |
| C-08 Flexibility beyond prove-topic | PASS | FRAMER Phase 0 Inertia Gap Declaration + "Closes gap?" column in PLANNER plan |

**Recommended: 30/30**

**Aspirational (70 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 Falsification | PASS | GATE-1 Condition B tests falsification explicitly; FAIL if absent |
| C-10 Cross-namespace | PASS | EVALUATOR Synthesis cross-namespace note field present |
| C-11 Audit ledger | PASS | EVALUATOR Feed-Forward Audit Ledger table with FAIL condition |
| C-12 COMPLETE markers | PASS | FRAMER COMPLETE / PLANNER COMPLETE / RUNNER COMPLETE + EXPERIMENT N COMPLETE per block |
| C-13 Inertia bookending | PASS | Phase 0 gap → Closes gap? column → EVALUATOR inertia gap closure question |
| C-14 Plan output routing | PASS | Output label + Consumed by columns in PLANNER Phase 1B table |
| C-15 Delivery boolean | PASS | Contract delivery line per block with "delivered? Yes/No" + FAIL |
| C-16 Gap-to-plan column | PASS | Closes gap? column with >=1 Yes requirement enforced |
| C-17 Verbatim quotation | PASS | RUNNER E-02 INPUT has blockquote placeholder + anti-pointer prohibition |
| C-18 Phase-boundary gates | PASS | GATE-0, GATE-1, GATE-FRAMER, GATE-P, GATE-PLANNER, GATE-E1/E2, GATE-RUNNER, GATE-CAL — all named at role/phase transitions |
| C-19 Inline FAIL conditions | PASS | FAIL conditions throughout all four role sections (>=3) |
| C-20 Atomic gate | PASS | GATE-1: boolean table, PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE), conjunctive |
| C-21 Calibration gate | PASS | GATE-CAL: "FAIL: All findings carry the same confidence level" — uniform-label pattern named explicitly |
| C-22 Per-block citation contract | PASS | E-02 INPUT embeds "citation contract (local to this block)" clause + verbatim blockquote + anti-pointer prohibition locally |

**Aspirational: 70/70**

**V-01 Score: 160/160**

---

### V-02 — Output format: numbered procedure (Step 1–11)

**Essential (60 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Hypothesis pre-commitment | PASS | Step 2 "Commit to Hypothesis and Falsification" before Step 3 (plan) and Step 4+ (execution) |
| C-02 Experiment plan >=2 types | PASS | Step 3 table with distinct types + GATE-3 enforcement |
| C-03 Feed-forward | PASS | Step 5 INPUT section references Step 4 (E-01) output; feed-forward is structurally mandated |
| C-04 Synthesis contrast | PASS | Step 8: "What we thought: [verbatim]" + "What we actually learned: [must differ]" + GATE-8 FAIL |
| C-05 Qx.md at correct path | PASS | Step 10 Artifact writes correct path; >=4 labeled sections (Steps 1–11) |

**Essential: 60/60**

**Recommended (30 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Principles >=2 | PASS | Step 9 with P-01/P-02, source finding, FAIL condition |
| C-07 Confidence per finding | PASS | Step 7 findings table with Confidence + Evidence basis columns |
| C-08 Flexibility beyond prove-topic | PASS | Step 1 inertia gap declaration + Closes gap? column |

**Recommended: 30/30**

**Aspirational (70 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 | PASS | GATE-2A Condition B tests falsification; FAIL if absent |
| C-10 | PASS | Step 8 cross-namespace note field |
| C-11 | PASS | Step 6 Feed-Forward Audit Ledger + FAIL condition |
| C-12 | PASS | STEP 4 COMPLETE / STEP 5 COMPLETE + ALL EXPERIMENTS COMPLETE markers |
| C-13 | PASS | Step 1 gap → Closes gap? column → Step 8 inertia gap closure |
| C-14 | PASS | Output label + Consumed by columns in Step 3 table |
| C-15 | PASS | Contract delivery per step with delivered? boolean + FAIL |
| C-16 | PASS | Closes gap? column enforced by GATE-3 |
| C-17 | PASS | Step 5 INPUT: blockquote placeholder + pointer prohibition |
| C-18 | PASS | GATE-1 (Step 1), GATE-2A (Step 2→3), GATE-3, GATE-7A, GATE-8 — >=2 at step transitions |
| C-19 | PASS | FAIL conditions throughout all steps (>=3) |
| C-20 | PASS | GATE-2A: boolean table, PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE) |
| C-21 | PASS | GATE-7A: "FAIL condition: all findings rated HIGH (uniform high), or all MEDIUM, or all LOW" — uniform-label named |
| C-22 | PASS | Step 5 INPUT: "citation contract (local to this step)" with anti-pointer clause + blockquote — locally embedded; closing note confirms "not in a global rule" |

**Aspirational: 70/70**

**V-02 Score: 160/160**

---

### V-03 — Phrasing register: second-person imperative + Q&A frame

**Essential (60 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Hypothesis pre-commitment | PASS | "What do you believe is true?" section with hypothesis before "What experiments will you run?" |
| C-02 Experiment plan >=2 types | PASS | Experiment plan table with "Why this type, not another?" column; GATE-P enforces >=2 distinct |
| C-03 Feed-forward | PASS | E-02 INPUT section: "What you bring in -- citation contract" consumes E-01 output |
| C-04 Synthesis contrast | PASS | "What you thought going in: [verbatim]" + "What you actually learned: [must differ]" + FAIL |
| C-05 Qx.md at correct path | PASS | "Write the artifact" section with correct path; >=4 question-headed sections |

**Essential: 60/60**

**Recommended (30 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Principles >=2 | PASS | "What principles do you take away?" with P-01/P-02 + source finding + FAIL |
| C-07 Confidence per finding | PASS | "How confident are you" + "Why that confidence level" columns in findings table |
| C-08 Flexibility beyond prove-topic | PASS | Gap declaration naming prove-topic limitation + "Does it close the gap?" column |

**Recommended: 30/30**

**Aspirational (70 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 | PASS | GATE-H Condition B: "Is your falsification criterion explicit?" — FAIL if vague |
| C-10 | PASS | "Which Signal artifact downstream should receive these findings?" in synthesis |
| C-11 | PASS | "What did each experiment actually deliver?" ledger section + FAIL |
| C-12 | PASS | "E-01 complete" / "E-02 complete" + "All experiments complete." markers |
| C-13 | PASS | Gap declaration → "Does it close the gap?" column → "Did the gap-closing experiment deliver..." |
| C-14 | PASS | "What you will call the output" + "Who consumes it" columns |
| C-15 | PASS | "Record delivery" lines per experiment with delivered? boolean + FAIL |
| C-16 | PASS | "Does it close your gap?" column with >=1 Yes requirement |
| C-17 | PASS | E-02 INPUT: blockquote placeholder + "You may not write 'see above'..." prohibition |
| C-18 | PASS | GATE-0, GATE-H, GATE-P, GATE-CAL, GATE-S — >=2 named gates at section transitions |
| C-19 | PASS | FAIL conditions throughout Q&A sections (>=3) |
| C-20 | PASS | GATE-H: boolean table, PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE) |
| C-21 | PASS | GATE-CAL: "all HIGH, all MEDIUM, or all LOW" uniform-label FAIL named explicitly |
| C-22 | PASS | E-02 INPUT: "citation contract (local to this experiment)" with anti-pointer clause + blockquote — locally embedded; note confirms "not in a global rule above" |

**Aspirational: 70/70**

**V-03 Score: 160/160**

---

### V-04 — Combined: Lifecycle emphasis + Inertia framing

**Essential (60 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Hypothesis pre-commitment | PASS | Phase 1 "Hypothesis" section before Phase 1B "Experiment Plan" with lifecycle narration |
| C-02 Experiment plan >=2 types | PASS | Phase 1B table with capability-map-referenced rationale; GATE-P enforces >=2 distinct |
| C-03 Feed-forward | PASS | Phase 2 E-02 INPUT: citation contract + verbatim from E-01 |
| C-04 Synthesis contrast | PASS | Phase 3C: "What we thought: [verbatim]" + "What we actually learned: [must differ]" + GATE-S FAIL |
| C-05 Qx.md at correct path | PASS | Artifact section with correct path; >=4 labeled phase sections |

**Essential: 60/60**

**Recommended (30 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Principles >=2 | PASS | Phase 3D Principles with P-01/P-02, source finding, FAIL |
| C-07 Confidence per finding | PASS | Phase 3B Findings table with Confidence + Evidence basis |
| C-08 Flexibility beyond prove-topic | PASS | prove-topic capability map as structural spine + Closes gap? column; referenced at every boundary |

**Recommended: 30/30**

**Aspirational (70 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 | PASS | GATE-1 Condition B: falsification present; FAIL if absent |
| C-10 | PASS | Phase 3C "Cross-namespace note" field |
| C-11 | PASS | Phase 3A Feed-Forward Audit Ledger + FAIL |
| C-12 | PASS | EXPERIMENT N COMPLETE per block + PHASE 2 COMPLETE + "Phase N complete. You are crossing..." narration |
| C-13 | PASS | Phase 0 gap → Closes gap? column → capability map referenced at every boundary → Phase 3C closure with "prove-program capability" named |
| C-14 | PASS | Output label + Consumed by columns |
| C-15 | PASS | Contract delivery per block with delivered? boolean + FAIL |
| C-16 | PASS | Closes gap? column; GATE-P enforces >=1 Yes |
| C-17 | PASS | Phase 2 E-02 INPUT: blockquote + anti-pointer prohibition |
| C-18 | PASS | GATE-0, GATE-1, GATE-P, GATE-CAL, GATE-S — all at explicit phase transitions; >=2 |
| C-19 | PASS | FAIL conditions throughout phases (>=3) |
| C-20 | PASS | GATE-1: boolean table, PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE) with note "Consult the prove-topic capability map" |
| C-21 | PASS | GATE-CAL: "FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW -- any uniform label pattern fails)" — uniform-label explicitly named with capability map reference |
| C-22 | PASS | Phase 2 E-02 INPUT: "citation contract (local to this block)" clause + blockquote — locally embedded per-block; closing instruction confirms "per-block, not global" |

**Aspirational: 70/70**

**V-04 Score: 160/160**

---

### V-05 — Combined: Role sequence + Phrasing register + Inertia framing

**Essential (60 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Hypothesis pre-commitment | PASS | FRAMER section with "Write your hypothesis" before PLANNER may begin; GATE-1 is the hard boundary |
| C-02 Experiment plan >=2 types | PASS | PLANNER table with "Why this type -- name the prove-program capability if gap-closing"; GATE-P enforces >=2 |
| C-03 Feed-forward | PASS | RUNNER Experiment 2 INPUT: citation contract + verbatim from E-01 |
| C-04 Synthesis contrast | PASS | EVALUATOR: "What you thought going in: [verbatim]" + "What you actually learned: [must differ]" + FAIL |
| C-05 Qx.md at correct path | PASS | "Write the artifact" section with correct path; >=4 role-labeled sections |

**Essential: 60/60**

**Recommended (30 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Principles >=2 | PASS | EVALUATOR "What principles do you take away?" table with P-01/P-02, source finding, FAIL |
| C-07 Confidence per finding | PASS | EVALUATOR "What did you find?" table: "How confident" + "Why that confidence level" columns |
| C-08 Flexibility beyond prove-topic | PASS | Gap declaration + GATE-0 + "Does it close your gap?" column in PLANNER |

**Recommended: 30/30**

**Aspirational (70 pts)**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 | PASS | GATE-1 Condition B: "Is your falsification criterion explicit?" — FAIL if absent |
| C-10 | PASS | EVALUATOR synthesis: "Which downstream Signal artifact should receive these findings?" |
| C-11 | PASS | EVALUATOR "What did each experiment actually deliver?" ledger + FAIL |
| C-12 | PASS | FRAMER COMPLETE / PLANNER COMPLETE / RUNNER COMPLETE + EXPERIMENT 1 COMPLETE / EXPERIMENT 2 COMPLETE |
| C-13 | PASS | Gap declaration → "Does it close your gap?" column → RUNNER notes "this multi-experiment chain justifies prove-program over prove-topic" → EVALUATOR inertia gap closure question |
| C-14 | PASS | Output label + "Who consumes it" columns in PLANNER table |
| C-15 | PASS | "Record delivery" lines per experiment with delivered? boolean + FAIL |
| C-16 | PASS | "Does it close your gap?" column with >=1 Yes enforced |
| C-17 | PASS | RUNNER Experiment 2 INPUT: blockquote + "pointer references... are prohibited" |
| C-18 | PASS | GATE-0, GATE-1, GATE-P, GATE-E1-entry, GATE-E2-entry, GATE-CAL — >=2 named gates at role/phase transitions |
| C-19 | PASS | FAIL conditions throughout all role sections (>=3) |
| C-20 | PASS | GATE-1: boolean table, PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE) — conjunctive, second-person voice |
| C-21 | PASS | GATE-CAL: "FAIL condition: all findings rated HIGH (uniform high), or all MEDIUM, or all LOW -- any uniform pattern fails regardless of which label you chose" — most explicit uniform-label statement across all R6 variations |
| C-22 | PASS | RUNNER Experiment 2 INPUT: "citation contract (local to this experiment): I am consuming E-01 output. I reproduce its exact text below. Pointer references... are prohibited in this INPUT section." — locally embedded with first-person voice; closing note confirms "not satisfied by the global instruction above" |

**Aspirational: 70/70**

**V-05 Score: 160/160**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Rank |
|-----------|-----------|-------------|-------------|-------|------|
| V-01 | 60/60 | 30/30 | 70/70 | **160/160** | T-1 |
| V-02 | 60/60 | 30/30 | 70/70 | **160/160** | T-1 |
| V-03 | 60/60 | 30/30 | 70/70 | **160/160** | T-1 |
| V-04 | 60/60 | 30/30 | 70/70 | **160/160** | T-1 |
| V-05 | 60/60 | 30/30 | 70/70 | **160/160** | T-1 |

All five variations: 160/160. Ceiling confirmed stable across all R6 structural axes.

---

## Excellence Signals

All five variations tie at ceiling, so excellence signals are drawn from patterns that were most robustly implemented — not merely present:

**V-05 C-21 phrasing**: "any uniform pattern fails regardless of which label you chose" is the most explicit statement of the non-uniformity rule across all five variations. The parenthetical eliminates an edge-case interpretation (e.g., "I assigned all HIGH so I chose the best level — that's fine") that earlier rounds left implicit.

**V-04 capability map spine**: Consulting the prove-topic capability map at every phase boundary (GATE-0, GATE-1, GATE-P, GATE-CAL, GATE-S notes) converts C-08 from a one-time declaration into a structural recurrence. The C-13 bookend is the strongest in the batch: the capability map explicitly names the row that closes the gap in Phase 3C synthesis.

**V-01 role-authority table**: The "Role | Writes | May Not" declaration table makes write authority auditable. It creates a second enforcement surface for GATE-1 (FRAMER cannot produce the plan) and GATE-PLANNER (RUNNER cannot change the hypothesis) without adding criteria.

No new rubric criteria are indicated — all three patterns are already well-covered by existing C-08, C-13, C-20/21 criteria.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": []}
```
