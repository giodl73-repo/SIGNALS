Scorecard written. Here are the results:

---

## prove-websearch Round 2 Scorecard

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1= | V-03 Null Hypothesis Attack | **110/110** | YES |
| 1= | V-04 Null Attack + Tables | **110/110** | YES |
| 1= | V-05 Full R2 Synthesis | **110/110** | YES |
| 4 | V-02 RFC Normative | **104/110** | YES |
| 5 | V-01 Evidence Tables | **94/110** | YES |

**Ceiling raised:** R1 best was 100/110 (106 retroactive). R2 hits 110/110 on three variations.

**What closed the gap from R1 V-05 (+4 pts):**
- C-11 (+2): "Do not proceed" gate blocks — R1 had numbered steps, R2 has hard stops
- C-15 (+2): Rules block before Topic/Hypothesis — R1 embedded rules contextually

**Key finding — MUST vs gate:**
V-02 (RFC MUST, 104) vs V-03 (phase gates, 110). Same constraint content, 6-point gap. Normative language describes requirements; gates enforce them. C-11, C-13, and C-07's PARTIAL→PASS are all attributable to the gate mechanism.

**Three new patterns for R3:**

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": [
  "null-attack-target-declaration: pre-committing to a specific falsifying result closes the semantic loophole where refuting-framed queries target qualifications rather than genuine falsifiers",
  "unconditional-refinement-mandate: complete-for-every-SEARCH-BLOCK removes conditional escape -- forces ran-as-planned documentation even when no adjustment occurs",
  "null-attack-verdict-propagation: requiring YES/NO null attack verdict in the conclusion prevents a failed adversarial test from disappearing after PHASE 3"
]}
```

**Open question for live runs:** V-03/V-04/V-05 are rubric-indistinguishable at 110. Whether unconditional refinement mandate (V-05) and evidence tables (V-04/V-05) produce measurably better execution quality than V-03's vertical fields + conditional trail is the R3 empirical question.
framings (one supporting, one refuting)." + "Repeat SEARCH blocks until you have at least 2 searches." | 10 |
| C-07 | PARTIAL | Balance check section present with ONE-SIDED escape slot and follow-up query field -- but ungated. No "do not proceed" checkpoint. Model can advance without completing balance check. | 5 |
| C-08 | PASS | Credibility column with enumerated label options listed inline | 10 |
| C-09 | PASS | SYNTHESIS has Convergence:, Conflict:, Conclusion: as pre-printed labeled fields with population instructions | 5 |
| C-10 | FAIL | No refinement trail field anywhere in the prompt | 0 |
| C-11 | FAIL | No "do not proceed" gate blocks -- design deliberately omitted to isolate table-format axis | 0 |
| C-12 | FAIL | No refinement trail, so live-phase placement is moot | 0 |
| C-13 | FAIL | Rule 3 requires "one supporting, one refuting" but names no adversarial target; no Q2 target declaration | 0 |
| C-14 | PASS | Convergence:/Conflict:/Conclusion: pre-printed in SYNTHESIS -- three distinct sub-fields required | 2 |
| C-15 | PASS | Rules block (1-4) appears before Topic: and Hypothesis: fields | 2 |

**Score: 94/110**
All essential: YES | Golden: YES

---

### V-02: RFC Normative Register (MUST/SHALL)

| C | Rating | Evidence | Pts |
|---|--------|---------|-----|
| C-01 | PASS | R-01: "Every factual claim in the output MUST be grounded in a URL retrieved during this session. Training-data knowledge MUST NOT be used as evidence." Strongest individual rule text of any variation. | 12 |
| C-02 | PASS | R-02: "Evidence MUST be a verbatim quotation in double quotation marks attributed to its source URL." + Quote: field in template | 12 |
| C-03 | PASS | R-03: output MUST contain >=2 search records each with (a) query string, (b) sources, (c) evidence extracted. Template has all three fields. | 12 |
| C-04 | PASS | R-04: output MUST state [supports / refutes / mixed] + one sentence per evidence item. Relevance: field present. | 12 |
| C-05 | PASS | R-05: output MUST include strength rating + one-sentence justification per item. Strength: field present. | 12 |
| C-06 | PASS | R-03 (>=2 searches) + R-06 ("At least one search MUST target evidence supporting... At least one MUST target evidence refuting") -- two-sided coverage explicitly mandated. | 10 |
| C-07 | PARTIAL | R-06 MUST with documented follow-up mandate is strong normative coverage. But no structural gate -- model under output pressure could nominally comply without genuine balance. No "do not proceed" checkpoint. | 8 |
| C-08 | PASS | R-07: "Each source MUST carry a credibility label." Credibility: field in template. | 10 |
| C-09 | PASS | R-08: synthesis MUST contain Convergence:, Conflict:, Conclusion: -- each MUST be populated. Template has all three. | 5 |
| C-10 | PASS | R-09: refinement MUST be documented inside the search record where it occurred. Query refinement block in template with Planned query / Gap observed / Adjusted to fields. | 5 |
| C-11 | FAIL | No explicit "GATE: do not proceed" blocks. RFC MUST language creates normative requirements but C-11 pass condition requires named GATE blocks with an explicit stop condition. MUST != gate. | 0 |
| C-12 | PASS | R-09 mandates refinement inside the search record (not post-synthesis). Template "Query refinement (per R-09)" appears inside each SEARCH [N] block -- live-phase placement. | 2 |
| C-13 | FAIL | R-06 says "target evidence refuting the hypothesis" -- names refutation as target but does not require a target declaration naming a specific falsifying result. No NULL HYPOTHESIS ATTACK framing; no pre-committed falsifier sentence. | 0 |
| C-14 | PASS | R-08 mandates three named sub-fields; template has Convergence:/Conflict:/Conclusion: pre-printed. | 2 |
| C-15 | PASS | "RULES (RFC 2119 normative)" block (R-01 through R-09) appears before Topic: and Hypothesis: fields. | 2 |

**Score: 104/110**
All essential: YES | Golden: YES

---

### V-03: Null Hypothesis Attack Framing

| C | Rating | Evidence | Pts |
|---|--------|---------|-----|
| C-01 | PASS | Rule 1: "Every factual claim must have a URL from this session. No training data as evidence." Rules-first positioning. | 12 |
| C-02 | PASS | Quote: field: "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" | 12 |
| C-03 | PASS | PHASE 2 block: Query string + Sources list + Evidence block (all required, pre-printed) | 12 |
| C-04 | PASS | Relevance: "[supports / refutes / mixed] -- [one sentence linking to hypothesis]" | 12 |
| C-05 | PASS | Strength: "[strong / weak / mixed] -- [one sentence justification]" | 12 |
| C-06 | PASS | GATE 1 enforces Q1 + Q2. Two queries with distinct framings required before PHASE 2 can begin. | 10 |
| C-07 | PASS | GATE 3: "Balance result is filled (BALANCED or ONE-SIDED with documented follow-up). Null hypothesis verdict is completed. Do not proceed to PHASE 4 until this gate is met." Hard stop enforces balance. | 10 |
| C-08 | PASS | Credibility: "[peer-reviewed / industry report / news outlet / blog / forum / other]" in every evidence block | 10 |
| C-09 | PASS | PHASE 4: Convergence:, Conflict:, Conclusion: pre-printed sub-fields with population requirements | 5 |
| C-10 | PASS | Query refinement block in each PHASE 2 query block: Planned query / Gap observed / Adjusted to. Captured immediately per query. | 5 |
| C-11 | PASS | GATE 1/2/3 with "Do not proceed to PHASE N until this gate is met." Binary verdict required before each phase transition. | 2 |
| C-12 | PASS | Refinement trail is inside the PHASE 2 query block -- captured at the moment each search returns results, before moving to the next query. Live-phase placement. | 2 |
| C-13 | PASS | GATE 1: "Q2 is present with a target declaration that names a falsifying result -- not a qualification or hedge." Q2 label is "NULL HYPOTHESIS ATTACK" + target declaration required. | 2 |
| C-14 | PASS | Convergence:/Conflict:/Conclusion: pre-printed labeled fields in PHASE 4 | 2 |
| C-15 | PASS | Rules block (1-4) before Topic/Hypothesis fields | 2 |

**Score: 110/110**
All essential: YES | Golden: YES

---

### V-04: Null Hypothesis Attack + Evidence Tables

| C | Rating | Evidence | Pts |
|---|--------|---------|-----|
| C-01 | PASS | Rule 1: "Every factual claim must have a URL from this session. No training data as evidence." | 12 |
| C-02 | PASS | Quote column in evidence table: "[Exact verbatim text in double quotation marks -- do not paraphrase]" -- table structure makes empty Quote cell visually disruptive | 12 |
| C-03 | PASS | SEARCH section: Query string + Sources table + Evidence table (all fields required) | 12 |
| C-04 | PASS | Relevance column: "[supports / refutes / mixed] -- [one sentence: link to hypothesis]" | 12 |
| C-05 | PASS | Strength column: "[strong / weak / mixed] -- [one sentence: justification]" | 12 |
| C-06 | PASS | PHASE 1 Query design table with Q1/Q2/Q3. GATE 1 enforces Q2 presence before PHASE 2. | 10 |
| C-07 | PASS | PHASE 3 balance table + GATE 3: "Do not proceed to PHASE 4 until met." Structural table + gate. | 10 |
| C-08 | PASS | Credibility column in evidence table with enumerated options | 10 |
| C-09 | PASS | PHASE 4: Convergence:/Conflict:/Conclusion: labeled sub-fields | 5 |
| C-10 | PASS | Query refinement block in each PHASE 2 SEARCH: Planned / Gap observed / Adjusted to. Live placement. | 5 |
| C-11 | PASS | GATE 1/2/3 with "Do not proceed to PHASE N until met." Hard stops enforced. | 2 |
| C-12 | PASS | Refinement trail inside PHASE 2 SEARCH block -- one phase earlier than R1-V-05's PHASE 3 placement. | 2 |
| C-13 | PASS | GATE 1: "Target declaration names a falsifying result (not a hedge or qualification)." Q2 labeled NULL HYPOTHESIS ATTACK. | 2 |
| C-14 | PASS | Convergence:/Conflict:/Conclusion: pre-printed in PHASE 4 | 2 |
| C-15 | PASS | Rules block (1-5) before Topic/Hypothesis -- Rule 5 adds explicit NULL HYPOTHESIS ATTACK constraint | 2 |

**Score: 110/110**
All essential: YES | Golden: YES

---

### V-05: Full R2 Synthesis (All Axes)

| C | Rating | Evidence | Pts |
|---|--------|---------|-----|
| C-01 | PASS | Rule 1: "Every factual claim MUST have a URL retrieved in this session. Training-data knowledge is NOT evidence. No URL = no claim." MUST capitalization + Source URL: field redundancy. | 12 |
| C-02 | PASS | Quote column in evidence table: "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" -- table structure + explicit Rule 2 cross-reference | 12 |
| C-03 | PASS | SEARCH BLOCK: Query string + Sources table + Evidence table -- all required, labeled "Apply Rules 1-3 to every row" | 12 |
| C-04 | PASS | Relevance column: "[supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?]" | 12 |
| C-05 | PASS | Strength column: "[strong / weak / mixed] -- [one sentence: why this rating?]" | 12 |
| C-06 | PASS | PHASE 1 Q1/Q2/Q3 required. GATE 1 enforces Q1 + Q2. | 10 |
| C-07 | PASS | PHASE 3 balance table + GATE 3: "Do not proceed to PHASE 4 until both fields are complete." Hard stop. | 10 |
| C-08 | PASS | Credibility column with enumerated options. | 10 |
| C-09 | PASS | PHASE 4: Convergence:/Conflict:/Conclusion: pre-printed with specific requirements -- Conclusion has 3 enumerated sub-items. | 5 |
| C-10 | PASS | "Query refinement trail (complete for every SEARCH BLOCK)" -- labeled mandatory, inside PHASE 2 SEARCH BLOCK. Unconditional: not "if any query was refined" but required for every block. | 5 |
| C-11 | PASS | GATE 1/2/3 with "Do not proceed to PHASE N until this gate is met." Three hard stops covering C-06, C-10, and C-07. | 2 |
| C-12 | PASS | Refinement trail is inside PHASE 2 SEARCH BLOCK -- one phase earlier than R1-V-05's PHASE 3. Captured at moment of observation. | 2 |
| C-13 | PASS | GATE 1: "Q2 is present AND its target declaration names a specific falsifying result (not a hedge or qualification). Rule 5 is met." Rule 5: "NULL HYPOTHESIS ATTACK... You MUST declare what falsifying evidence looks like before running Q2." | 2 |
| C-14 | PASS | Convergence:/Conflict:/Conclusion: pre-printed in PHASE 4 with 3-part Conclusion (aggregate verdict + null attack YES/NO + largest gap). | 2 |
| C-15 | PASS | "RULES (read before proceeding -- apply to all phases):" numbered block (1-5) before Topic: and Hypothesis: fields. | 2 |

**Score: 110/110**
All essential: YES | Golden: YES

---

## Composite Ranking

| Rank | Variation | Score | All Essential | Golden | C-11 | C-12 | C-13 | C-14 | C-15 |
|------|-----------|-------|---------------|--------|------|------|------|------|------|
| 1= | V-03 Null Hypothesis Attack | 110 | YES | YES | PASS | PASS | PASS | PASS | PASS |
| 1= | V-04 Null Attack + Tables | 110 | YES | YES | PASS | PASS | PASS | PASS | PASS |
| 1= | V-05 Full R2 Synthesis | 110 | YES | YES | PASS | PASS | PASS | PASS | PASS |
| 4 | V-02 RFC Normative | 104 | YES | YES | FAIL | PASS | FAIL | PASS | PASS |
| 5 | V-01 Evidence Tables | 94 | YES | YES | FAIL | FAIL | FAIL | PASS | PASS |

R1 V-05 retroactive score under v2: **106/110** (C-11 FAIL, C-12 PASS, C-13 PASS, C-14 PASS, C-15 FAIL).
R2 closed the 4-point gap: GATE enforcement (C-11, +2) + rule-first ordering (C-15, +2).

---

## Analysis

### Why V-01 and V-02 fall short

**V-01 (94):** Tables enforce C-02/C-04/C-05/C-08 structurally, but without phase gates, C-07 is
ungated (PARTIAL, -5 pts), and C-10/C-12/C-13 are absent (-9 pts, -2 pts, -2 pts). Tables are a
necessary mechanism for quote compliance but insufficient alone for adversarial coverage and balance
enforcement.

**V-02 (104):** RFC MUST language is the strongest individual rule phrasing of any variation. It
achieves C-10 and C-12 via R-09 (refinement inside search record), adding +9 pts over V-01. Two
structural gaps remain: (1) MUST is not a gate -- C-11 FAIL costs 2 pts; (2) R-06 names "refuting"
as target but doesn't require a target declaration -- C-13 FAIL costs 2 pts. The remaining
6-point gap from ceiling is entirely structural, not semantic.

### Why V-03/V-04/V-05 reach ceiling

Three mechanisms close all gaps over R1 V-05:

1. **Phase-gate enforcement (C-11, +2):** "Do not proceed to PHASE N until this gate is met" across
   GATE 1/2/3. R1 had numbered steps but no binary stop conditions. Gates convert soft expectations
   to hard preconditions.

2. **Named-target gate framing (C-13, +2):** GATE 1 requires Q2 to have "a target declaration that
   names a specific falsifying result -- not a hedge or qualification." R1's "Q2 explicitly targets
   the refutation side" named the category (refutation) but not the specific falsifier. R2's target
   declaration requires a pre-committed sentence before the search runs.

3. **Rule-first constraint ordering (C-15, +2):** Rules block before Topic/Hypothesis ensures
   constraints are parsed before content is seen. R1 V-05 embedded rules contextually; R2 promotes
   them to an explicit pre-content numbered block.

### Differentiation within V-03/V-04/V-05 (rubric-invisible, open for live runs)

All three score 110/110 -- the rubric cannot discriminate. Three mechanisms in V-05 that may
produce better live execution quality (open questions for R3):

1. **Unconditional refinement mandate:** "complete for every SEARCH BLOCK" vs. V-02's R-09 "if any
   query was refined." Removes the null-refinement escape -- forces "ran as planned" documentation
   even when no adjustment occurred. Prevents silent omission.

2. **Null attack verdict propagation:** Conclusion requires "(2) whether the null hypothesis attack
   found falsifying evidence (YES/NO + one sentence)." Forces the adversarial test result into the
   aggregate finding. Without this, a failed null attack can disappear after PHASE 3.

3. **MUST capitalization within phase gates:** V-05 uses "MUST" inside gate-structured prompts
   (not just normative rules as in V-02). Creates dual enforcement: normative language + structural
   gate. Neither mechanism alone reached 110/110. Whether the combination improves live execution
   quality over V-03's non-capitalized rules is untested.

---

## Excellence Signals

**1. Null hypothesis attack with target declaration outperforms "refutation side" framing.**
R1's "Q2 explicitly targets the refutation side" was the state of the art. R2's "target declaration
names a specific falsifying result -- not a qualification or hedge" closes the loophole: a model
searching for "limitations of X" can satisfy R1's framing while avoiding genuine falsifiers. The
target declaration forces pre-commitment to a specific falsifying result before querying.

**2. Phase gates are binary; MUST rules are not.**
V-02 uses MUST for every constraint and scores 104. V-03 uses identical constraint content but adds
"do not proceed" gates and scores 110. The 6-point gap is attributable to gating: C-11 (+2), C-13
gate framing (+2), and C-07 full PASS under gate enforcement (+2 vs PARTIAL). Normative language
describes requirements; gates enforce them.

**3. Live-phase refinement placement moved one phase earlier.**
R1 V-05 placed the refinement trail in PHASE 3 (post-collection, pre-synthesis). R2 V-03/V-04/V-05
place it inside each individual SEARCH BLOCK in PHASE 2. This captures gap observation at the
moment it occurs -- before the next query runs. Whether this produces higher-fidelity refinement
documentation than PHASE 3 placement is the key open question for live runs.

**4. Unconditional field mandate removes conditional escape.**
"Complete for every SEARCH BLOCK" (V-05) vs. "if any query was refined" (V-02 R-09 / V-03).
The conditional form allows a model to skip the refinement trail by deciding no refinement occurred.
The unconditional form requires at minimum "ran as planned" -- forcing explicit documentation of
null adjustments.

**5. Table format as structural enforcer for quote compliance.**
V-04 and V-05 use markdown tables for evidence. An empty Quote cell in a table row is more visually
salient than a missing labeled line in a vertical block. Whether this produces measurably higher
C-02 compliance than vertical fields in live execution is the R2 open question for the table axis.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["null-attack-target-declaration: requiring Q2 to pre-commit to a specific falsifying result (not category of doubt) before searching closes the semantic loophole where refuting-framed queries target qualifications rather than genuine falsifiers", "unconditional-refinement-mandate: labeling the refinement trail as complete-for-every-SEARCH-BLOCK removes the conditional escape -- prevents silent omission by requiring ran-as-planned documentation even when no adjustment occurs", "null-attack-verdict-propagation: explicitly requiring the conclusion to address whether the null hypothesis attack found falsifying evidence (YES/NO) prevents a failed adversarial test from disappearing after PHASE 3 and not affecting the aggregate synthesis"]}
```
