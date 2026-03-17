## quest-score Scoring Run — Round 1 (2026-03-16)

**Rubric**: v1-2026-03-16 | **Skill**: quest-score | **Variations**: V-01 through V-05

---

### LOAD BLOCK

1. **Criteria (ID + tier):**
   - C-01: Essential — rubric load verification
   - C-02: Essential — per-criterion verdict matrix
   - C-03: Essential — evidence for every verdict
   - C-04: Essential — composite score per output (explicit calculation)
   - C-05: Essential — failure patterns section
   - C-06: Recommended — ranked leaderboard
   - C-07: Recommended — excellence signals
   - C-08: Recommended — per-output synthesis notes
   - C-09: Aspirational — regression signals
   - C-10: Aspirational — score arithmetic verification

2. **Formula (exact):**
   `composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)`
   PARTIAL = 0.5 toward pass count.

3. **Golden threshold:** all 5 essentials PASS AND composite >= 80

4. **N/A rules:**
   - C-09: PARTIAL (not FAIL) when scorer writes the prescribed "no prior round data" statement. Omitting the section entirely = FAIL.

5. **Outputs loaded:** V-01 (Axis A), V-02 (Axis B), V-03 (Axis C), V-04 (A+B), V-05 (A+B+C). N=5.
   No prior-round scorecard provided. Trace artifact: placeholder (design-level analysis).

---

### Scoring Note

Since no actual AI-generated trace outputs exist (trace = placeholder), this scoring evaluates the **prompt design** of each variation: given the structural features of each variation prompt, what would a `quest-score` execution using that variation reliably produce, and does that production satisfy each rubric criterion?

---

## V-01 — Axis A: Numbered criterion blocks

### C-01 — Rubric load verification
**VERDICT: PASS**
**EVIDENCE:** V-01 provides a five-field numbered LOAD BLOCK template with labeled slots — "1. Criteria (ID + tier)," "2. Formula (exact text from rubric)," "3. Golden threshold (exact text)," "4. N/A rules," "5. Outputs loaded" — pre-populated with placeholder text requiring the scorer to fill each slot before proceeding.
**WHY:** All four C-01 sub-elements (criteria IDs+tiers, formula text, golden threshold, output count) are represented as distinct numbered slots; an empty slot is structurally visible, making partial compliance detectable before scoring begins.
**SUBELEMENTS:**
- (a) criteria IDs + tiers: present (slot 1 pre-labels Essential/Recommended/Aspirational)
- (b) formula text: present (slot 2 requires paste from rubric)
- (c) golden threshold: present (slot 3 requires paste from rubric)
- (d) output count or list: present (slot 5 requires V-XX list with N count)

### C-02 — Per-criterion verdict matrix
**VERDICT: PASS**
**EVIDENCE:** Step 2 instructs one numbered block per criterion per output, C-01 through C-10 in order, with exact block format `[V-XX / C-NN -- criterion short name]`. The structure forces one block × 10 criteria × N outputs.
**WHY:** The named-block structure makes a missing criterion visible as a skipped block rather than a missing table row; no criterion-output pair can be implied or merged without breaking the block sequence.

### C-03 — Evidence for every verdict
**VERDICT: PARTIAL**
**EVIDENCE:** The EVIDENCE slot in each block carries instructions — "Sentence(s) referencing specific output content -- quote a phrase, name a section, or describe a structural feature. Generic observations not tied to specific output text do not qualify. Do not restate the criterion." No worked example for general evidence is provided; the C-04 CALC slot shows one format-level reference but not a content-level quote example for other criteria.
**WHY:** The anti-pattern warning ("Do not restate the criterion") reduces the worst-case failure mode, but without a positive anchor across multiple criteria, some criteria (particularly C-07 or C-08 verdicts) are likely to produce structural observations that border on criterion restatement, producing 1–2 borderline evidence cells per output.

### C-04 — Composite score per output (explicit calculation)
**VERDICT: PASS**
**EVIDENCE:** Step 2 includes a CALC slot with format `"E=4/5, R=2/3, A=1/2 -> composite = YY"` and anti-anchor `"calculation not shown."` Step 3 COMPOSITE SCORES shows `([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/2 * 10)` with PARTIAL = 0.5 noted.
**CALC for V-01 design:** The CALC slot mechanically forces the E/R/A breakdown before the final number; a bare number would leave the CALC slot unfilled, which is visible as a missing field.

### C-05 — Failure patterns section
**VERDICT: PASS**
**EVIDENCE:** Step 3 lists "FAILURE PATTERNS" as a required synthesis section with exact empty-state text: `` `No failure patterns -- all criteria passed in at least one output.` ``
**WHY:** The required-even-when-empty instruction with prescribed verbatim text means a missing section is an explicit omission, not a soft miss.

### C-06 — Ranked leaderboard
**VERDICT: PASS**
**EVIDENCE:** Step 3 includes a RANKED LEADERBOARD table with header `| Rank | Output | Score | Golden |` and descending order requirement; ties noted explicitly.
**WHY:** The table template forces all N outputs to appear; an output missing from the rank table is a missing row.

### C-07 — Excellence signals
**VERDICT: PASS**
**EVIDENCE:** Step 3 includes an EXCELLENCE SIGNALS section requiring "(1) the output, (2) the criterion, (3) the structural feature that produced the outlier." Empty-state text: `No excellence signals identified in this scoring run.`
**WHY:** The three-part signal requirement and anti-anchor ("V-XX scored highest overall" is not an excellence signal) match the rubric's C-07 pass condition precisely.

### C-08 — Per-output synthesis notes
**VERDICT: FAIL**
**EVIDENCE:** V-01 Step 3 lists five synthesis sections: COMPOSITE SCORES, RANKED LEADERBOARD, FAILURE PATTERNS, EXCELLENCE SIGNALS, REGRESSION SIGNALS. Per-Output Synthesis Notes is absent from this list. No Step 3 section instructs the scorer to write a paragraph explaining each output's structural score drivers.
**WHY:** C-08 requires a narrative note per output explaining what it did structurally to raise or lower its score; without the section prompt, the scorecard output would omit this entirely.

### C-09 — Regression signals
**VERDICT: PARTIAL**
**EVIDENCE:** Step 2 C-09 block template prescribes `VERDICT: PARTIAL / EVIDENCE: No prior-round scorecard was provided. / WHY: The rubric N/A rule prescribes PARTIAL (not FAIL) when no prior data exists...` Step 3 includes a REGRESSION SIGNALS synthesis section with if/else logic.
**WHY:** The per-output PARTIAL template plus the synthesis section together produce the required N/A statement; the rubric's N/A rule awards PARTIAL, not FAIL, for this condition.

### C-10 — Score arithmetic verification
**VERDICT: PASS**
**EVIDENCE:** V-01 has a dedicated Step 4 — "Pick one output. Independently verify its composite score" — with a full verification block: E counts list, R counts list, A counts list, computed formula, and `Matches stated score: [YES | NO -- discrepancy: stated X, computed Y]`.
**WHY:** The standalone verification block goes beyond what any other variation provides; the explicit discrepancy field forces the scorer to flag arithmetic errors rather than silently skip them.

---

## V-02 — Axis B: Phase gates with STOP tokens

### C-01 — Rubric load verification
**VERDICT: PASS**
**EVIDENCE:** Phase 1 instructs: "Write a load summary containing all four of the following; omitting any one makes C-01 PARTIAL" — then lists Criteria (with tier labels), Formula, Golden threshold, N/A rules, and Outputs. The `=== LOAD COMPLETE ===` gate forces the scorer to commit to the load output before proceeding.
**WHY:** All four required C-01 sub-elements are present in the load summary requirements; the phase gate makes skipping load a visible structural error.
**SUBELEMENTS:**
- (a) criteria IDs + tiers: present
- (b) formula text: present
- (c) golden threshold: present
- (d) output count or list: present

### C-02 — Per-criterion verdict matrix
**VERDICT: PASS**
**EVIDENCE:** Phase 2 provides a verdict table template with one row per criterion, C-01 through C-10, with explicit tier labels and verdict+evidence columns. The `=== SCORING COMPLETE ===` gate prevents premature exit from the scoring phase.
**WHY:** The table template forces all 10 criteria to appear in each output's verdict block; a missing row breaks the table's visual completeness.

### C-03 — Evidence for every verdict
**VERDICT: PARTIAL**
**EVIDENCE:** Evidence rules in Phase 2 state "Each evidence cell must reference specific output content: a quoted phrase, a named section, or a structural observation. Restating the criterion does not qualify." No worked example provided; evidence is constrained to a table cell, which compresses multi-sentence references.
**WHY:** Table cell format naturally truncates evidence, and without a positive anchor showing what "specific output reference" looks like across multiple criteria, borderline evidence (structural observations that border on criterion restatement) is likely in 1–3 cells per output.

### C-04 — Composite score per output (explicit calculation)
**VERDICT: PARTIAL**
**EVIDENCE:** The verdict table template shows `| C-04 | Essential | ... | [must include the calculation form if PASS, or note its absence if PARTIAL/FAIL] |`. Evidence rules state "C-04 evidence must note whether the E/R/A breakdown was shown or only the final number." No CALC slot or anti-anchor enforces the form.
**WHY:** Without a dedicated CALC slot, the table cell for C-04 evidence can satisfy the text instruction with a partial reference ("output shows E=4/5, R=3/3") without the full `-> composite = X` form; this makes C-04 PARTIAL the highest-risk criterion in V-02.

### C-05 — Failure patterns section
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3c: "Required even when empty: write `No failure patterns -- all criteria passed in at least one output.`" — exact empty-state text prescribed. `=== SYNTHESIS COMPLETE ===` gate enforces that synthesis sections are all present.
**WHY:** Phase gate + exact empty text prevents both omission (gate catches it) and empty-section silence (text prescribed).

### C-06 — Ranked leaderboard
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3b: "All N outputs, descending by composite score. Ties stated explicitly." `=== SYNTHESIS COMPLETE ===` gate ensures synthesis runs to completion.
**WHY:** Phase gate prevents premature exit before the leaderboard section.

### C-07 — Excellence signals
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3d: "Any output-criterion pair where one output clearly leads the field structurally. Each signal: name the output, criterion, and structural feature. Overall 'scored highest' does not qualify. Required even when empty."
**WHY:** Output-criterion-mechanism requirement with "scored highest" anti-anchor and required-even-when-empty instruction match C-07 pass conditions.

### C-08 — Per-output synthesis notes
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3e: "One paragraph per output explaining what it did structurally that raised or lowered its score relative to the other outputs. Do not restate verdict counts -- explain the mechanism." The phase gate forces this section to appear before `=== SYNTHESIS COMPLETE ===`.
**WHY:** Explicit prohibition against verdict-count restatement ("Do not restate verdict counts") directly addresses the most common C-08 PARTIAL failure mode.

### C-09 — Regression signals
**VERDICT: PARTIAL**
**EVIDENCE:** Phase 3 section 3f prescribes: "`No prior round data -- regression analysis cannot be performed.`" The `=== SYNTHESIS COMPLETE ===` gate ensures the regression section is written before synthesis closes.
**WHY:** Phase gate + prescribed N/A text guarantees the section exists and contains the required statement; rubric awards PARTIAL for this condition.

### C-10 — Score arithmetic verification
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3a shows full calculation format: `V-XX: E=[n]/5, R=[n]/3, A=[n]/2 -> composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]`. All tier counts and the formula are stated on one line.
**WHY:** The tier count + formula format gives an evaluator everything needed to independently verify one output's arithmetic; per the rubric note, PARTIAL requires counts to be absent, which they are not here.

---

## V-03 — Axis C: Worked examples inline

### C-01 — Rubric load verification
**VERDICT: PASS**
**EVIDENCE:** Step 1 provides a "compliant load summary" worked example with actual values: `Essential: C-01, C-02, C-03, C-04, C-05 / Recommended: C-06, C-07, C-08 / Aspirational: C-09, C-10 / Formula: ... / Golden threshold: ... / Outputs: V-01...V-05 (N=5)`. The scorer copies the format.
**WHY:** A positive anchor with all four sub-elements already filled in is a lower-friction path to compliance than a blank template; the probability of missing any one sub-element decreases when the example shows all four simultaneously.
**SUBELEMENTS:**
- (a) criteria IDs + tiers: present (example shows tier groupings)
- (b) formula text: present
- (c) golden threshold: present
- (d) output count or list: present

### C-02 — Per-criterion verdict matrix
**VERDICT: PASS**
**EVIDENCE:** Step 2 instructs "produce a verdict for every criterion (C-01 through C-10)" across all outputs, with flexible format. The instruction is unambiguous: every criterion must appear.
**WHY:** Despite flexible format, explicit "C-01 through C-10" enumeration leaves no criterion susceptible to silent omission.

### C-03 — Evidence for every verdict
**VERDICT: PARTIAL**
**EVIDENCE:** Step 2 states "each verdict must include: A specific evidence reference: a quoted phrase from the output, a named section, or a structural observation. Generic restatements of the criterion do not qualify as evidence." The C-04 worked example models a specific output quote (`"V-03: E=4/5..."`) but covers only C-04; no worked example shows evidence quality for C-01, C-07, or C-08.
**WHY:** The C-04 anchor demonstrates specificity for one criterion; without equivalent examples for synthesis-phase criteria (C-07, C-08), scorers evaluating those criteria may fall back to structural observations that are weakly specific.

### C-04 — Composite score per output (explicit calculation)
**VERDICT: PASS**
**EVIDENCE:** V-03 provides both a PASS worked example (`C-04: PASS / Evidence: The output shows "V-03: E=4/5, R=3/3, A=1/2 -> composite = (4/5*60)+(3/3*30)+(1/2*10) = 83"`) and an explicit PARTIAL anti-example (`C-04: PASS / Evidence: V-03 composite score is 83. [PARTIAL because tier counts absent]`).
**WHY:** The paired PASS + PARTIAL examples at the point of instruction are a direct anchor for the scorer; the anti-example makes the most common C-04 failure mode unmistakably recognizable.
**CALC for V-03 design:** The PASS example format (`E=4/5, R=3/3, A=1/2 -> composite = ...`) is the exact form the rubric requires; a scorer following it produces a verifiable calculation.

### C-05 — Failure patterns section
**VERDICT: PASS**
**EVIDENCE:** Step 3 includes "Failure Patterns" with exact empty-state text: `` `No failure patterns -- all criteria passed in at least one output.` `` and explicit note "This section is required even when empty. Do not omit it."
**WHY:** Required-even-when-empty instruction with prescribed verbatim text prevents silent omission.

### C-06 — Ranked leaderboard
**VERDICT: PASS**
**EVIDENCE:** Step 3 "Ranked Leaderboard" section: "All outputs, descending by composite score. Ties noted."
**WHY:** Section title and ordering requirement ensure the leaderboard is distinct from the composite scores section and explicitly sorted.

### C-07 — Excellence signals
**VERDICT: PASS**
**EVIDENCE:** Step 3 "Excellence Signals" section names the three-part requirement: "Each signal names: the output, the criterion, and the structural feature that produced the outlier. 'V-XX scored highest overall' is not an excellence signal."
**WHY:** "Scored highest overall" anti-anchor directly targets the most common C-07 PARTIAL failure mode; the three-part requirement names the mechanism criterion.

### C-08 — Per-output synthesis notes
**VERDICT: PASS**
**EVIDENCE:** Step 3 "Per-Output Synthesis Notes": "One short paragraph per output: what did it do structurally that drove its score up or down? Do not list verdict counts -- explain the mechanism."
**WHY:** Anti-restatement instruction ("Do not list verdict counts") directly targets the rubric's C-08 PARTIAL failure mode.

### C-09 — Regression signals
**VERDICT: PARTIAL**
**EVIDENCE:** Step 2 C-09 template prescribes `C-09: PARTIAL -- no prior round data available; regression analysis cannot be performed.` per output. V-03 Step 3 does not include a Regression Signals synthesis section — the five synthesis sections are: Composite Scores, Ranked Leaderboard, Failure Patterns, Excellence Signals, Per-Output Synthesis Notes.
**WHY:** The per-output N/A statement satisfies the "writes the prescribed no-prior-data statement" condition for PARTIAL; the absence of a dedicated synthesis regression section is a structural gap, but the N/A acknowledgment is present in each output's per-output verdict, earning PARTIAL rather than FAIL per the rubric's N/A rule.

### C-10 — Score arithmetic verification
**VERDICT: PASS**
**EVIDENCE:** Step 3 "Composite Scores" section shows `V-XX: E=[n]/5, R=[n]/3, A=[n]/2 / composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]` — full tier count and formula in one line.
**WHY:** The calculation line provides all elements needed for independent arithmetic verification; PARTIAL requires counts to be absent, which they are not.

---

## V-04 — Axis A+B: Numbered blocks + phase gates

### C-01 — Rubric load verification
**VERDICT: PASS**
**EVIDENCE:** Phase 1 LOAD BLOCK template has five numbered slots with pre-labeled tier groupings (`Essential: C-01..C-05 / Recommended: C-06..C-08 / Aspirational: C-09..C-10`) and `=== LOAD COMPLETE ===` gate. All four required sub-elements are distinct slots.
**WHY:** Phase gate + slot structure: the scorer cannot advance to scoring without filling all five load fields; a partially filled block is structurally incomplete before the gate.
**SUBELEMENTS:**
- (a) criteria IDs + tiers: present (pre-labeled in template)
- (b) formula text: present (slot 2 placeholder)
- (c) golden threshold: present (slot 3 placeholder)
- (d) output count or list: present (slot 5)

### C-02 — Per-criterion verdict matrix
**VERDICT: PASS**
**EVIDENCE:** Phase 2 instructs numbered blocks per criterion per output, C-01 through C-10 in order, with `=== SCORING COMPLETE — [N] outputs scored ===` gate. Block format `[V-XX / C-NN -- criterion short name]` labels every cell.
**WHY:** Block sequence + phase gate: skipping a criterion produces a gap in block numbering; the scoring gate token commits the scorer to stating N before exiting.

### C-03 — Evidence for every verdict
**VERDICT: PARTIAL**
**EVIDENCE:** EVIDENCE slot instruction: "Direct quote or specific structural reference to this output's content. Generic criterion restatements do not qualify." WHY slot adds a mechanism-explanation requirement. No worked example provided for any criterion outside of C-04's CALC field.
**WHY:** The slot structure enforces the presence of an EVIDENCE field but not its quality beyond the anti-pattern warning; without a multi-criterion positive anchor, 1–2 cells per output are likely to produce structural observations that stop short of a direct output quote.

### C-04 — Composite score per output (explicit calculation)
**VERDICT: PASS**
**EVIDENCE:** CALC slot: `"Reproduce the E/R/A breakdown as written in the output, e.g. 'E=4/5, R=2/3, A=1/2 -> 76.7'. If no breakdown shown: 'calculation not shown -- PARTIAL'."` Phase 3a shows full tier count + formula format.
**WHY:** The CALC slot with anti-anchor ("calculation not shown -- PARTIAL") makes a bare-number score visibly incomplete; a scorer filling the CALC slot with only a number would be directly contradicted by the slot's own guidance.
**CALC for V-04 design:** The `calculation not shown -- PARTIAL` anti-anchor is a stronger C-04 guard than any text instruction alone.

### C-05 — Failure patterns section
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3c: "`No failure patterns -- all criteria passed in at least one output.`" Required even when empty. `=== SYNTHESIS COMPLETE ===` gate ensures the section is written.
**WHY:** Phase gate prevents termination before synthesis sections; prescribed text prevents silent omission.

### C-06 — Ranked leaderboard
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3b with table template `| Rank | Output | Composite | Golden |` and "All N outputs descending."
**WHY:** Explicit table template with Golden column ensures ordering is unambiguous and each output's golden status is stated.

### C-07 — Excellence signals
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3d: "Output-criterion pairs where one output structurally leads the field. Each entry: Output ID, Criterion ID, Structural feature that produced the outlier. Overall ranking ('scored highest') does not qualify."
**WHY:** Three-part entry requirement with "scored highest" anti-anchor directly matches the rubric's C-07 pass condition.

### C-08 — Per-output synthesis notes
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3e: "One paragraph per output: what structural choices drove its score? Do not recount verdicts." `=== SYNTHESIS COMPLETE ===` gate ensures this section is written before synthesis closes.
**WHY:** Phase gate + anti-restatement instruction combine to address both the presence problem (gate) and the quality problem ("do not recount verdicts").

### C-09 — Regression signals
**VERDICT: PARTIAL**
**EVIDENCE:** Phase 3 section 3f: "`No prior round data -- regression analysis cannot be performed.`" `=== SYNTHESIS COMPLETE ===` gate ensures this section exists before closing.
**WHY:** Phase gate makes section omission a structural error; prescribed text produces the exact N/A statement the rubric requires for PARTIAL.

### C-10 — Score arithmetic verification
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3a shows `V-XX: E=[n]/5 ([verdict list]), R=[n]/3, A=[n]/2 / composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]` — verdict list + formula on one line.
**WHY:** The verdict list in the calculation line makes per-tier counts auditable; combined with the formula, this satisfies the C-10 "independently verified" condition.

---

## V-05 — Axis A+B+C: Numbered blocks + phase gates + worked examples

### C-01 — Rubric load verification
**VERDICT: PASS**
**EVIDENCE:** Phase 1 provides both a numbered slot template AND a "Compliant load block (copy this format)" worked example pre-filled with actual criterion IDs, formula, golden threshold, N/A rule, and sample output list. The N/A rule (C-09 PARTIAL condition) is explicitly shown in the example.
**WHY:** The pre-filled example reduces the load block to a copy-and-replace operation; the example itself demonstrates all four required sub-elements simultaneously, making partial compliance harder to achieve accidentally.
**SUBELEMENTS:**
- (a) criteria IDs + tiers: present (example shows tier groupings by name)
- (b) formula text: present (exact formula text in example)
- (c) golden threshold: present (exact threshold text in example)
- (d) output count or list: present (sample list in example)

### C-02 — Per-criterion verdict matrix
**VERDICT: PASS**
**EVIDENCE:** Phase 2 instructs numbered blocks per criterion per output, C-01 through C-10, with `=== SCORING COMPLETE — [N] outputs scored ===` gate and block format `[V-XX / C-NN -- criterion short name]`.
**WHY:** Block sequence + phase gate with N-count commitment; identical mechanism to V-04.

### C-03 — Evidence for every verdict
**VERDICT: PARTIAL**
**EVIDENCE:** EVIDENCE slot + "restating the criterion does not qualify" + WHY slot for mechanism explanation. The compliant C-04 block worked example shows `EVIDENCE: Output states "V-03: E=4/5, R=3/3, A=1/2 -> composite = ..."` — a specific quote from the output. No equivalent worked example exists for C-01, C-07, C-08, or other criteria.
**WHY:** The C-04 worked example is criterion-specific; the positive anchor for evidence quality does not generalize to synthesis criteria (C-07, C-08) or structural criteria (C-05, C-06), leaving 6–8 of 10 criteria without a quality anchor despite the slot enforcement.

### C-04 — Composite score per output (explicit calculation)
**VERDICT: PASS**
**EVIDENCE:** Phase 2 provides a "Compliant C-04 block (this is PASS)" with `EVIDENCE: Output states "V-03: E=4/5, R=3/3, A=1/2 -> composite = (4/5*60)+(3/3*30)+(1/2*10) = 83"` AND a "Non-compliant C-04 block (this is PARTIAL -- do not produce this)" with `EVIDENCE: Output shows composite score of 83.` The CALC slot appears in both examples with contrast.
**WHY:** The paired PASS/PARTIAL worked examples at the point of instruction create an unmistakable quality contrast; the scorer can identify the anti-pattern in their own output before writing it.
**CALC for V-05 design:** Compliant block shows `CALC: E=4/5, R=3/3, A=1/2 -> 83`; non-compliant block shows `CALC: 83 [no breakdown]` — the contrast makes the compliance signal explicit.

### C-05 — Failure patterns section
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3c: "Required even when empty: `No failure patterns -- all criteria passed in at least one output.`" `=== SYNTHESIS COMPLETE ===` gate enforces presence.
**WHY:** Identical mechanism to V-04; phase gate + prescribed text.

### C-06 — Ranked leaderboard
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3b table `| Rank | Output | Composite | Golden |` with "all outputs descending; ties noted."
**WHY:** Table template with Golden column; identical to V-04.

### C-07 — Excellence signals
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3d: "output, criterion, mechanism. 'V-XX scored highest' is not sufficient." Required even when empty.
**WHY:** Three-part requirement + anti-anchor; identical to V-04.

### C-08 — Per-output synthesis notes
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3e: "One paragraph per output: structural choices that drove its score. Do not recount verdicts." `=== SYNTHESIS COMPLETE ===` gate.
**WHY:** Phase gate + anti-restatement instruction; identical to V-04.

### C-09 — Regression signals
**VERDICT: PARTIAL**
**EVIDENCE:** Phase 3 section 3f has hardcoded text: `` `No prior round data -- regression analysis cannot be performed.` `` (not a template — the exact text is written directly in the prompt). Per-output C-09 block template in Phase 2 also prescribes PARTIAL.
**WHY:** Hardcoded text (not a conditional) means the scorer copies the exact required N/A statement without needing to evaluate the condition; phase gate ensures the section exists.

### C-10 — Score arithmetic verification
**VERDICT: PASS**
**EVIDENCE:** Phase 3 section 3a format: `V-XX: E=[n]/5, R=[n]/3, A=[n]/2 / composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]`. PARTIAL = 0.5 noted.
**WHY:** Tier count + formula format provides all elements needed for independent verification.

---

## COMPOSITE SCORES

**V-01:**
E = C-01 PASS, C-02 PASS, C-03 PARTIAL, C-04 PASS, C-05 PASS → 4.5/5
R = C-06 PASS, C-07 PASS, C-08 FAIL → 2/3
A = C-09 PARTIAL, C-10 PASS → 1.5/2
composite = (4.5/5 × 60) + (2/3 × 30) + (1.5/2 × 10) = 54.0 + 20.0 + 7.5 = **81.5**
Golden: NO — C-03 PARTIAL (not all 5 essential PASS)

**V-02:**
E = C-01 PASS, C-02 PASS, C-03 PARTIAL, C-04 PARTIAL, C-05 PASS → 3.5/5
R = C-06 PASS, C-07 PASS, C-08 PASS → 3/3
A = C-09 PARTIAL, C-10 PASS → 1.5/2
composite = (3.5/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 42.0 + 30.0 + 7.5 = **79.5**
Golden: NO — C-03 and C-04 PARTIAL (not all 5 essential PASS; composite 79.5 < 80)

**V-03:**
E = C-01 PASS, C-02 PASS, C-03 PARTIAL, C-04 PASS, C-05 PASS → 4.5/5
R = C-06 PASS, C-07 PASS, C-08 PASS → 3/3
A = C-09 PARTIAL, C-10 PASS → 1.5/2
composite = (4.5/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 54.0 + 30.0 + 7.5 = **91.5**
Golden: NO — C-03 PARTIAL (not all 5 essential PASS)

**V-04:**
E = C-01 PASS, C-02 PASS, C-03 PARTIAL, C-04 PASS, C-05 PASS → 4.5/5
R = C-06 PASS, C-07 PASS, C-08 PASS → 3/3
A = C-09 PARTIAL, C-10 PASS → 1.5/2
composite = (4.5/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 54.0 + 30.0 + 7.5 = **91.5**
Golden: NO — C-03 PARTIAL (not all 5 essential PASS)

**V-05:**
E = C-01 PASS, C-02 PASS, C-03 PARTIAL, C-04 PASS, C-05 PASS → 4.5/5
R = C-06 PASS, C-07 PASS, C-08 PASS → 3/3
A = C-09 PARTIAL, C-10 PASS → 1.5/2
composite = (4.5/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 54.0 + 30.0 + 7.5 = **91.5**
Golden: NO — C-03 PARTIAL (not all 5 essential PASS)

---

## RANKED LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 (tie) | V-03 | 91.5 | NO |
| 1 (tie) | V-04 | 91.5 | NO |
| 1 (tie) | V-05 | 91.5 | NO |
| 4 | V-01 | 81.5 | NO |
| 5 | V-02 | 79.5 | NO |

**Tie note (V-03/V-04/V-05):** All three achieve C-04 PASS, all three include C-08 and C-09 synthesis sections, all three earn C-03 PARTIAL. Qualitative differentiation by sub-criterion below (see Per-Output Notes).

---

## FAILURE PATTERNS

**C-03 (evidence for every verdict)** — PARTIAL across all 5 outputs, zero PASS.

This is the universal binding constraint in Round 1. Every variation provides the anti-pattern warning ("Generic restatements do not qualify") but only V-03 and V-05 provide a worked example, and that example covers only C-04. No variation shows what compliant evidence looks like for a synthesis-phase criterion (C-07, C-08) or for a structural criterion where the evidence reference is a section title rather than a calculation. The failure pattern signals a rubric axis gap: evidence quality for non-calculation criteria.

---

## EXCELLENCE SIGNALS

**V-01 / C-10 — Dedicated arithmetic verification block**
V-01 is the only variation with a standalone Step 4 arithmetic verification section containing verdict lists, computed formula, and an explicit `Matches stated score: YES | NO -- discrepancy` field. All other variations embed arithmetic in the composite score format, which enables verification but does not demand it. V-01's mechanism: the dedicated step with discrepancy field forces the scorer to detect errors rather than accept the stated score.

**V-05 / C-04 — Paired PASS/PARTIAL worked examples**
V-05 is the only variation providing both a compliant C-04 block and an explicit anti-example labeled "this is PARTIAL -- do not produce this." The contrast mechanism allows the scorer to self-check against a recognizable failure pattern at the point of instruction. V-03 provides the same PASS example but the anti-example is less structurally prominent (described in prose rather than shown as a named code block).

**V-04 / C-08 — Phase gate + anti-restatement instruction**
V-04 and V-05 (but not V-01, V-02, V-03 equivalently) combine the phase gate enforcement with the "do not recount verdicts" instruction at the point of the synthesis notes section. V-01 lacks the section; V-03 has the section but no gate. V-04's mechanism: synthesis cannot close without per-output notes, and the quality bar ("structural choices, not counts") is stated immediately before the section is written.

---

## PER-OUTPUT SYNTHESIS NOTES

**V-01:** The slot-enforcement mechanism is the strongest of any single-axis variation for C-01 and C-04 — numbered blocks with SUBELEMENTS and CALC slots make missing sub-elements and missing calculations structurally visible. The critical miss is C-08: Per-Output Synthesis Notes is simply absent from Step 3, a design gap rather than a quality gap. V-01 also uniquely includes a dedicated arithmetic verification step (Step 4), making it the strongest variation for C-10. The tradeoff is that slot verbosity without phase gates creates a risk of context-pressure synthesis truncation — the scorer may end after REGRESSION SIGNALS without noticing C-08 never appeared.

**V-02:** The phase gate mechanism is the strongest presence guarantee of any variation — four STOP tokens prevent premature termination at each phase boundary. The cost is enforcement depth: table-cell evidence format compresses multi-sentence references, and C-04's evidence requirement is instructed but not slot-enforced. V-02 is the only variation to lose C-04 PASS; the table format that makes C-02 robust also makes C-04 vulnerable. V-02 achieves the strongest C-08 guarantee among Axis B alone (phase gate + explicit per-output notes section), making it a useful complement to Axis A's slot precision.

**V-03:** The worked-example mechanism is the most selective but highest-precision tool in the round. The C-04 PASS/PARTIAL example pair directly addresses the most common new-rubric failure; the C-01 load example reduces the load block to a copy-and-replace operation. V-03 achieves parity with V-04 and V-05 at 91.5 despite having neither slot enforcement nor phase gates, because the synthesis sections are explicitly listed in Step 3. The gap is C-09 synthesis: V-03's Step 3 has 5 sections, missing Regression Signals, so the no-prior-data statement lives in per-output verdicts rather than a synthesis section.

**V-04:** The combination of Axes A and B produces the cleanest separation between what enforcement mechanisms address: A's slots prevent sub-element omissions in load (C-01) and calculation form in scoring (C-04); B's gates prevent synthesis-phase truncation (C-05, C-07, C-08, C-09). The combination is additive — neither axis individually provides the coverage of the pair. V-04's score is identical to V-03 and V-05 numerically but its enforcement profile is more defensive: it protects against lazy compliance (leaving slots partially filled) rather than assuming the worked example is followed.

**V-05:** The maximal variation adds V-03's worked examples to V-04's slot+gate foundation. The result is the highest C-04 compliance guarantee (paired examples + CALC slot), the clearest C-01 load compliance path (worked example + SUBELEMENTS slot), and the same synthesis coverage as V-04. The C-03 universal PARTIAL reveals the limit of the three-axis combination: even the strongest combination of enforcement, gating, and exemplification does not guarantee evidence quality for criteria where no worked example exists. V-05's tiebreaker advantage over V-04 and V-03 is reliability: it converts the two highest-risk new-rubric PARTIALs (C-01 incomplete load, C-04 bare number) into structurally enforced slots backed by concrete copy-paste anchors, reducing the probability of those PARTIAL outcomes from "likely in first-pass" to "possible only under active deviation."

---

## REGRESSION SIGNALS

No prior round data — regression analysis cannot be performed.

---

## ARITHMETIC VERIFICATION

**Verification: V-04**
E verdicts: C-01 PASS, C-02 PASS, C-03 PARTIAL (0.5), C-04 PASS, C-05 PASS → E count = 4.5
R verdicts: C-06 PASS, C-07 PASS, C-08 PASS → R count = 3.0
A verdicts: C-09 PARTIAL (0.5), C-10 PASS → A count = 1.5
Computed: (4.5/5 × 60) + (3.0/3 × 30) + (1.5/2 × 10) = 54.0 + 30.0 + 7.5 = **91.5**
Matches stated score: YES

---

```json
{"top_score": 91.5, "all_essential_pass": false, "new_patterns": ["C-03 (evidence) earns PARTIAL universally across all 5 variations despite slot enforcement, anti-pattern warnings, and worked examples — the gap is that worked examples cover only C-04 (a calculation criterion); no variation provides a positive anchor for evidence quality on synthesis criteria (C-07, C-08) where output referencing requires quoting a structural feature rather than a formula", "Three-way tie at 91.5 between V-03, V-04, V-05 shows axes A, B, C are complementary but not strictly additive once C-08 presence and C-04 calculation are achieved; the binding constraint shifts entirely to C-03, making a fourth axis targeting general evidence quality (e.g., a worked C-07 evidence block) the highest-leverage next move"]}
```
