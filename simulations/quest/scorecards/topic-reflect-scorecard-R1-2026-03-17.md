# Quest Score — topic-echo (topic-reflect) Round 1

## Evaluation Matrix

Scoring: PASS = full points, PARTIAL = half points, FAIL = 0

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| **C-01** Surprise orientation | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-02** Symmetric Contract | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-03** Signal tracing | 12 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | **PASS** |
| **C-04** Design impact specificity | 12 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | **PASS** |
| **C-05** Adversarial gate executed | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-06** Epistemic dimension compliance | 10 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| **C-07** Minimum 2 surprises | 10 | PASS | PASS | PASS | PASS | PASS |
| **C-08** Cluster map actionability | 10 | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |
| **C-09** Token protocol integrity | 5 | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |
| **C-10** Foreknowledge signal evaluated | 5 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

---

## Evidence Notes

**C-03 / C-04 — why only V-05 passes:**
The root failure pattern is *table cell pressure* — Stage 4 as a table creates syntactic pressure to compress `Signal Source` and `Design Impact` into 3-word fragments. V-01, V-02, and V-04 do not change Stage 4's structure; the pressure remains. V-03's imperative register says "name the artifact" but still leaves a narrow table cell as the output target. V-05 eliminates the table entirely — numbered prose entries with a labeled template make a one-word cell structurally impossible. Full sentence required by format, not by instruction.

**C-08 — why V-03 and V-05 pass, others partial:**
Stage 5's cluster map remains weakly specified in V-01, V-02, and V-04. V-03's imperative collapse reduces Stage 5's intro to a direct command: the stripped form naturally becomes "Name the responsible skill or role — not just investigate." V-05 inherits this via the shared V-03 register. V-01/V-02/V-04 leave Stage 5 prose unchanged, leaving "investigate" entries likely.

**C-09 — why V-03 and V-05 pass:**
V-03 explicitly targets token omission failures. The 6-item rule list at the top includes token requirements as explicit named rules rather than embedded in stage intros. V-05 inherits this.

**C-04 note for V-04:** Combining V-01 (gate preview) and V-02 (worked examples) closes the priming gap and the calibration gap — this is the strongest treatment for **C-01** and **C-05**, both of which are already PASS in isolation. The combination yields no *score* improvement because the criteria are binary, but the robustness of those passes is higher. The weakness remains C-03/C-04: Stage 4 format is untouched.

---

## Composite Scores

| Variation | Essential (/60) | Recommended (/30) | Aspirational (/10) | **Total** | All Essential Pass? | Golden? |
|-----------|-----------------|-------------------|--------------------|-----------|---------------------|---------|
| V-01 | 48 | 20 | 5 | **73** | No (C-03/C-04 partial) | No |
| V-02 | 48 | 20 | 5 | **73** | No (C-03/C-04 partial) | No |
| V-03 | 48 | 25 | 7.5 | **81** | No (C-03/C-04 partial) | No |
| V-04 | 48 | 20 | 5 | **73** | No (C-03/C-04 partial) | No |
| **V-05** | **60** | **25** | **7.5** | **93** | **Yes** | **Yes** |

---

## Rankings

1. **V-05 — 93** — Only variation to reach essential pass on all 5. Structural prose template closes C-03 and C-04; V-03 register closes C-08 and C-09.
2. **V-03 — 81** — Imperative register improves recommended and aspirational tier. Misses golden due to C-03/C-04 still table-format.
3. **V-01, V-02, V-04 — 73 (tied)** — All close the priming/calibration gap for C-01/C-05 but leave Stage 4 intact. V-04's combination adds robustness to the passes it already has, not new passes.

---

## Excellence Signals from V-05

**Format enforces specificity; instruction cannot.** When the pass condition requires a named artifact or a named component, the table format is the enemy — narrow cells create abbreviation pressure that instruction-level reminders cannot overcome. Replacing the table with numbered prose entries carrying labeled fields (each requiring a full sentence) closes the gap structurally. No matter how clearly the instruction says "name the artifact," a 2-column cell invites a fragment. A prose template does not.

**Register + format stack multiplicatively.** V-03's imperative register alone reaches 81 by fixing C-08 and C-09. V-05 inherits that register *and* adds the Stage 4 format change, unlocking the two essential criteria that account for 24 pts. The combination is not additive (81 + 12) — it is the intersection of two independent failure modes both being closed.

**Stage 4 is the highest-leverage rewrite target in this skill.** Four of the five unresolved criteria in V-01 through V-04 trace back to Stage 4 output format. One structural change to that stage produces a 20-point score swing (73 → 93). Variations that leave Stage 4 untouched are bounded at ~81.

---

```json
{"top_score": 93, "all_essential_pass": true, "new_patterns": ["Format enforces specificity: replacing Stage 4 tables with templated prose entries structurally prevents fragment cells, more reliably than instruction-level reminders", "Stage 4 is the highest-leverage rewrite target: four essential/recommended failures trace to table cell pressure, one format change closes all four"]}
```
