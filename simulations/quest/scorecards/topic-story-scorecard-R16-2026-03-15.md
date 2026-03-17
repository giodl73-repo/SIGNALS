# Quest Score — `topic-story` v15 — Round 16

---

## Essential Criteria

All four essentials are gates. Any FAIL = output unusable.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 BLUF | PASS | PASS | PASS | — | — |
| C-02 Five beats | PASS | PASS | PASS | — | — |
| C-03 Cross-signal | PASS | PASS | PASS | — | — |
| C-04 Pattern, not summary | PASS | PASS | PASS | — | — |

**V-04:** Prompt truncated after opening line — cannot score.
**V-05:** Prompt not provided — cannot score.

All three complete variations clear all essential gates.

---

## Full Criterion Scoring — V-01 through V-03

| ID | Criterion | V-01 | V-02 | V-03 |
|----|-----------|------|------|------|
| C-01 | BLUF | PASS | PASS | PASS |
| C-02 | Five beats | PASS | PASS | PASS |
| C-03 | Cross-signal synthesis | PASS | PASS | PASS |
| C-04 | Pattern not summary | PASS | PASS | PASS |
| C-05 | Signal coverage ≥3 | PASS | PASS | PASS |
| C-06 | Uncertainty specific | PASS | PASS | **PASS+** |
| C-07 | Recommendation proportionality | PASS | PASS | PASS |
| **C-40** | Verdict as literal first line | **FAIL** | **PARTIAL** | **PASS** |
| C-41 | Pattern necessity test | PASS | PASS | PASS |

---

## C-40 — Key Differentiator Analysis

This is the axis that separates all three variations.

**V-01 — FAIL**

The role-sequence structure produces: ROLE 1 extraction table → `### ROLE 2: AUTHOR — Story Synthesis` heading → verdict line. The "ABSOLUTE RULE" in V-01 applies inside ROLE 2, but the combined output has the table and the structural heading above the verdict. Rubric explicit: "appears after even a structural heading...fails." ROLE 1 table is not a heading but it still precedes the verdict in the output stream. FAIL.

**V-02 — PARTIAL**

Output opens with `### PART 1: DECISION CARD` heading on line 1; `VERDICT:` field appears on line 2 (or after a blank). The verdict is the first *content field* within the card, but not the topmost line. The section label `PART 1: DECISION CARD` is a structural heading in the rubric's sense. C-01 PASS, C-40 PARTIAL — the format creates the right intent (card leads, verdict leads card) but inserts a label above the verdict.

**V-03 — PASS**

"Before you write a single word of the brief: write your verdict sentence on the very first line." No structure is instructed before the verdict. The editorial frame does not impose a PART 1/PART 2 or ROLE 1/ROLE 2 architecture. Output starts: `[PROCEED/PAUSE/PIVOT/ABANDON]: [reason].` — then the brief. C-40 PASS.

---

## C-06 — Secondary Differentiator

**V-01:** Prohibition form — `"More research may be needed" fails. Name what research...`
Defines what to avoid.

**V-02:** Standard form — "how a different answer would change the verdict."
Names the test to meet.

**V-03:** Conditional form — "if it resolves one way, you stay with the verdict; if it resolves the other, you change it."
Gives the model a binary test to execute per open question. Strongest instruction for eliciting specific, decision-linked uncertainty.

---

## Composite Scores

Working from 9 visible criteria (4 essential + 3 recommended + 2 aspirational from v15). Full rubric has 34 aspirational; C-40 and C-41 are the two visible ones from that pool. Composite extrapolated from observed coverage pattern.

| Variation | Essential | Recommended | C-40 | C-41 | Approx. Composite |
|-----------|-----------|-------------|------|------|-------------------|
| V-01 | 4/4 | 3/3 | FAIL | PASS | ~82 |
| V-02 | 4/4 | 3/3 | PARTIAL | PASS | ~85 |
| V-03 | 4/4 | 3/3 | PASS | PASS | ~88 |
| V-04 | — | — | — | — | — |
| V-05 | — | — | — | — | — |

---

## Ranking

1. **V-03** — 88 — All essentials pass; only variation with C-40 PASS; strongest C-06 formulation
2. **V-02** — 85 — All essentials pass; Decision Card format is right instinct for C-40 but section heading creates borderline failure
3. **V-01** — 82 — All essentials pass; role-sequence architecture undermines C-40 because ROLE 1 output precedes verdict in combined output stream
4. **V-04** — unscored (truncated)
5. **V-05** — unscored (not provided)

---

## Excellence Signals from V-03

**ES-01 — Genre framing as natural BLUF enforcer**
Framing the task as an "editorial brief" removes the structural conflict that defeats V-01 and V-02. Editorials do not announce themselves with section labels before the thesis. V-01 and V-02 both try to instruct the verdict-first rule explicitly, then construct multi-part output architectures (ROLE 1/2, PART 1/2) that physically precede the verdict. V-03's genre contract makes the "write verdict first" instruction redundant as a safety rule — the genre itself carries it. This is the structural insight: explicit structural scaffolding and literal-first-line verdict placement are in tension; genre framing resolves the tension without a fight.

**ES-02 — Decision-flip conditional for uncertainty**
V-03 tests uncertainty with: "if it resolves one way, you stay with the verdict; if it resolves the other, you change it." This is executable — the model can apply it as a filter per candidate open question. V-01 uses prohibition form (names what fails), V-02 names the standard (what the answer must connect to). The conditional form is higher-leverage because it gives the model a binary pass/fail check it can apply before writing, not just after.

**ES-03 — Embedded necessity logic vs. labeled necessity rule**
V-03 teaches the C-41 necessity test through framing: "a reader who only had one signal could not have seen this." V-01 and V-02 name the test explicitly ("necessity test," "remove either signal"). The embedded form is harder to satisfy mechanically — a model cannot cite two signals and call it done; it has to verify the counterfactual. Labeled rules invite checkbox compliance; embedded logic invites genuine application.

---

```json
{"top_score": 88, "all_essential_pass": true, "new_patterns": ["genre framing as BLUF enforcer: editorial assignment removes structural-header interference with C-40 by eliminating the multi-part scaffolding that places output labels above the verdict", "decision-flip conditional for uncertainty: if-then formulation gives the model an executable pass/fail test per open question, stronger than prohibition-form or standard-form uncertainty instructions"]}
```
