Now I have all 5 variation bodies and the self-scoring. I'll score each variation independently against the rubric criteria.

---

## /quest:score — quest-golden Round 1

**Rubric:** v1 (C-01–C-10) | **Variations:** V-01 through V-05

---

### SCORECARD: V-01 — Role Sequence: Rubric-Curator-First

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "EACH ROUND: EXECUTE ALL FOUR PHASES" — PHASE 1 through PHASE 4 labeled; "Round 1: vary exactly one axis per variation. Round 2+: combine axes"; V-NN labeling required. Multi-round loop with named variations. |
| C-02 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as independent sections, each requiring a distinct state declaration. "DO NOT declare golden unless TRIAL CONVERGED AND QUEST PLATEAUED in the same round." Both conditions explicitly named. |
| C-03 | E | PASS | "Body: the full, verbatim prompt text. Not a summary. Not a description. The complete skill body must be usable as a skill without modification." |
| C-04 | E | PASS | "Write the accumulated rubric (all criteria across all rounds)... Include all criteria with all five fields. Note which round added each criterion." |
| C-05 | E | PASS | "Composite formula: (essential_pass/N_essential * 60) + (recommended_pass/N_recommended * 30) + (aspirational_pass/N_aspirational * 10)" — explicit formula in Phase 2. |
| C-06 | R | PASS | "Mechanism: the structural property present in passing variations and absent from failing ones / Principle: stated as reusable, transferable rule — not 'V-02 scored higher' but what design choice caused the difference" |
| C-07 | R | FAIL | Phase 4 instructs proposing criteria with 5 fields (QU3 proposal present) but no approval/rejection/deferral decision step (b) and no explicit QU4 application step (c). Criteria accumulate into the golden artifact without a traced approval gate. |
| C-08 | R | PASS | "cite both rounds by explicit name (e.g., 'Round 2 and Round 3: no new patterns found'). Do not write 'the last two rounds.'" |
| C-09 | A | FAIL | No explicit element→criterion mapping table or inline annotation in the prompt body. The round-progression rule is present but not annotated with the criterion it satisfies. |
| C-10 | A | FAIL | Convergence not yet achieved in Round 1; factual criterion requires confirming actual round count ≤5. |
| **COMPOSITE** | — | **80** | (5/5 × 60) + (2/3 × 30) + (0/2 × 10) = 60 + 20 + 0 |

---

### SCORECARD: V-02 — Output Format: Per-Variation Scorecard

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | STEP 1 through STEP 4 with V-NN labeling, "Round 1: vary exactly one axis / Round 2+: combine axes." Multi-round loop structure. |
| C-02 | E | PASS | "GATE 1 — TRIAL" and "GATE 2 — PLATEAU" as separate sections, each requiring an explicit state declaration. "Declare golden only if both gates are satisfied in the same round." |
| C-03 | E | PASS | "Body must be the complete, verbatim, runnable skill prompt — not a summary." |
| C-04 | E | PASS | "List all criteria from all rounds with all five fields per criterion." |
| C-05 | E | PASS | "Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)" — explicit formula with concrete denominators. |
| C-06 | R | PASS | "Structural property: [what design choice in passing variations is absent in failing ones] / Reusable principle: [transferable rule, not a variation comparison]" |
| C-07 | R | FAIL | Step 4 instructs 5-field proposals; no approval/rejection/deferral gate (b) between proposal and rubric accumulation. |
| C-08 | R | PASS | Gate 2: "Name both rounds explicitly (e.g., 'Round 3 and Round 4: no new patterns found')." |
| C-09 | A | FAIL | No explicit element→criterion mapping in the prompt body. |
| C-10 | A | FAIL | Convergence not yet achieved. |
| **COMPOSITE** | — | **80** | (5/5 × 60) + (2/3 × 30) + (0/2 × 10) = 60 + 20 + 0 |

---

### SCORECARD: V-03 — Lifecycle Emphasis: Convergence-Gate-Heavy

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | STEP 1 through STEP 4 plus convergence check labeled; "Round 1: vary exactly one axis; Round 2+: combine axes." Loop structure present. |
| C-02 | E | PASS | "GATE 1: TRIAL CONVERGENCE" (procedure steps a–d) and "GATE 2: PLATEAU DETECTION" (procedure steps a–e) as fully independent sections. "Do not conflate TRIAL CONVERGED with QUEST PLATEAUED. They are independent gates asking different questions." Strongest gate-separation of any variation. |
| C-03 | E | PASS | "Body: complete, runnable, verbatim. Not a summary. Not a description." |
| C-04 | E | PASS | "All criteria from all rounds, all five fields per criterion, round-of-addition noted." |
| C-05 | E | **FAIL** | Step 2 shows matrix template with COMPOSITE row and instructs "Show per-criterion pass/fail before computing composite" but no composite formula is stated anywhere in the prompt body. An operator running V-03 must know the formula externally. |
| C-06 | R | PASS | "name the pattern as a reusable principle (mechanism, not comparison). State scope (skill-specific | transferable)." |
| C-07 | R | FAIL | No approval/rejection step between Step 4 proposals and rubric accumulation. |
| C-08 | R | PASS | Gate 2 procedure: "Name both rounds explicitly by label — e.g., 'Round 3' and 'Round 4.' Do not write 'the last two rounds' or 'the previous two rounds.'" |
| C-09 | A | FAIL | No element→criterion mapping. |
| C-10 | A | FAIL | Not yet achieved. |
| **COMPOSITE** | — | **68** | (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 |

---

### SCORECARD: V-04 — Phrasing Register (DO-NOT) + Lifecycle Emphasis

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | STEP 1 through STEP 4 with DO NOT gates; "Round 1: change exactly one axis per variation. Round 2+: combine axes that produced signal in prior rounds." V-NN labeling required. |
| C-02 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as fully separate sections. "Execute both gates separately. A single paragraph covering both is not acceptable." |
| C-03 | E | PASS | "Body: the complete, verbatim, runnable prompt text. Not a summary. Not a description. The body must be copyable and usable as a skill without any modification." |
| C-04 | E | PASS | "Include every criterion active at convergence, from every round, with all five fields. Note which round added each criterion." |
| C-05 | E | **FAIL** | Matrix template shown with COMPOSITE row; "Per-criterion results come before composite — no exceptions" but no composite formula stated in prompt body. The formula must be carried from rubric context; the prompt doesn't instruct its use. |
| C-06 | R | PASS | "Mechanism: [structural property present in passing variations, absent in failing ones] / Principle: [reusable rule — not 'V-02 scored higher' but what design choice caused it]" |
| C-07 | R | FAIL | Step 4 instructs 5-field proposals; "DO NOT proceed to the convergence check until every proposed criterion has all five fields" is a completeness gate, not an approval gate. No (b) decision step. |
| C-08 | R | PASS | Gate 2: "Name the current round by label. Name the immediately preceding round by label. State what Step 3 found in each — by round name, not 'the last two rounds.'" |
| C-09 | A | FAIL | No element→criterion mapping. |
| C-10 | A | FAIL | Not yet achieved. |
| **COMPOSITE** | — | **68** | (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 |

---

### SCORECARD: V-05 — Inertia Framing (Champion-Challenger) + Output Format

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | STEP 1 through STEP 4; "A challenger... changes exactly one axis from the champion (Round 1) or combines axes that produced improvement in earlier rounds (Round 2+)." V-NN labeling, multi-round structure. |
| C-02 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as separate sections. "Declare golden only if TRIAL CONVERGED AND QUEST PLATEAUED simultaneously in the same round." |
| C-03 | E | PASS | "Body: complete, verbatim, runnable. Not a summary." |
| C-04 | E | PASS | "All criteria from all rounds, all five fields, with round-of-addition noted." |
| C-05 | E | **FAIL** | "Per-criterion results required before composite" and matrix shown with COMPOSITE row and champion column, but no composite formula stated in prompt body. |
| C-06 | R | PASS | "Mechanism: [structural property present in better-scoring versions, absent from worse-scoring ones] / Principle: [reusable rule, not a comparison]" |
| C-07 | R | FAIL | Step 4 proposes criteria; no approval/rejection/deferral decision step. |
| C-08 | R | PASS | Gate 2: "Name both rounds explicitly by label." |
| C-09 | A | FAIL | No element→criterion mapping. |
| C-10 | A | FAIL | Not yet achieved. |
| **COMPOSITE** | — | **68** | (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 |

---

### Round 1 Summary Matrix

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS |
| C-02 | E | PASS | PASS | PASS | PASS | PASS |
| C-03 | E | PASS | PASS | PASS | PASS | PASS |
| C-04 | E | PASS | PASS | PASS | PASS | PASS |
| C-05 | E | PASS | PASS | FAIL | FAIL | FAIL |
| C-06 | R | PASS | PASS | PASS | PASS | PASS |
| C-07 | R | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-08 | R | PASS | PASS | PASS | PASS | PASS |
| C-09 | A | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-10 | A | FAIL | FAIL | FAIL | FAIL | FAIL |
| **COMPOSITE** | — | **80** | **80** | **68** | **68** | **68** |
| **RANK** | — | **T-1** | **T-1** | **T-3** | **T-3** | **T-3** |

---

### EXCELLENCE SIGNALS

**Score spread exists:** V-01/V-02 score 80; V-03/V-04/V-05 score 68. Discriminating criterion: C-05.

---

**Pattern: Explicit-Composite-Formula**
- Mechanism: V-01 and V-02 state the composite formula verbatim in the scoring step instructions (`(essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)`). V-03, V-04, V-05 show a matrix template with a COMPOSITE row but rely on the operator knowing the formula from the rubric context. When the formula is absent from the prompt body, operators may compute incorrectly or omit the numeric composite entirely.
- Principle: A scoring step that names the formula explicitly makes C-05 self-enforcing. A scoring step that says "compute composite" without the formula delegates computation correctness to operator memory.
- Scope: transferable

---

**Shared failures — no pattern (no score spread):**

| Criterion | All-fail diagnosis |
|-----------|--------------------|
| C-07 | skill-gap — no variation includes an approval/rejection/deferral gate between the criterion proposal step and rubric accumulation. All 5 propose criteria with 5 fields but none have a (b) decision step. |
| C-09 | skill-gap — no variation includes an explicit element→criterion mapping table or inline annotation for the golden prompt body. |
| C-10 | not applicable in Round 1 — factual criterion about actual convergence round count; not evaluable until convergence occurs. |

---

```json
{"top_score": 80, "all_essential_pass": false, "new_patterns": ["explicit-composite-formula"]}
```
