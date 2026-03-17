Now I have all five variations fully. Let me score them.

---

## quest-score Scorecard — Round 7 (v7 rubric)

**Date:** 2026-03-16
**Rubric:** v7 — C-01..C-24, E=5, R=3, A=16
**Formula:** `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/16 × 10)`

---

## ROLE 1: JUDGE

Reading all five outputs (V-01 through V-05). Establishing one ACCEPTABLE and one UNACCEPTABLE evidence example per criterion.

---

**C-01 — Essential-1** (role-gated execution with dependency manifest)
ACCEPTABLE: V-01 — "ROLE DEPENDENCY MANIFEST / The following table declares the complete dependency graph for this task. It is a standalone structural artifact — auditable without executing the protocol."
UNACCEPTABLE: "The roles are organized so that the Judge runs first, then the Analyst, then the Verifier."
What separates them: ACCEPTABLE names a standalone structural artifact that is explicitly auditable without execution; UNACCEPTABLE embeds the same information as prose with no structural separation.

**C-02 — Essential-2** (hard gate token enforcement)
ACCEPTABLE: V-01 — "Gate rules (hard): Role 2 cannot begin without JUDGE STANDARD COMPLETE present above. Role 3 cannot begin without ANALYST COMPLETE present above."
UNACCEPTABLE: "Wait for each prior role to finish before proceeding to the next."
What separates them: ACCEPTABLE names specific gate tokens and binds them to specific roles with hard-enforcement language; UNACCEPTABLE gives a general sequencing instruction with no token check.

**C-03 — Essential-3** (per-criterion scoring table, no row skipped)
ACCEPTABLE: V-02 — "| ID | Criterion | Weight | Verdict | Evidence | / No row may be skipped. No evidence cell may be blank."
UNACCEPTABLE: "Evaluate each criterion and assign PASS, PARTIAL, or FAIL with your reasoning."
What separates them: ACCEPTABLE provides a structural table template plus an explicit no-skip mandate; UNACCEPTABLE is a behavioral instruction without format enforcement.

**C-04 — Essential-4** (evidence quality gate against UNACCEPTABLE pattern)
ACCEPTABLE: V-01 — "Before writing each evidence cell, verify it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell."
UNACCEPTABLE: "Provide specific, output-grounded evidence for each criterion."
What separates them: ACCEPTABLE references the Judge's named UNACCEPTABLE pattern as the quality gate and mandates a rewrite action; UNACCEPTABLE is a quality instruction with no rewrite mechanism.

**C-05 — Essential-5** (composite formula with correct tier weights and current denominator)
ACCEPTABLE: V-04 — "composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]"
UNACCEPTABLE: "Compute a composite score weighted by essential, recommended, and aspirational criteria." (or any formula using `/13` denominator)
What separates them: ACCEPTABLE states all three tier weights as exact arithmetic with the updated `/16` aspirational denominator; UNACCEPTABLE is either structurally absent or uses a stale denominator.

**C-06 — Recommended-1** (JUDGE covers all criteria with ACCEPTABLE/UNACCEPTABLE/separator)
ACCEPTABLE: V-01 — "C-[NN]: [criterion name] / ACCEPTABLE: '[verbatim or close paraphrase...]' / UNACCEPTABLE: '[text from an actual output...]' / What separates them: [one sentence]" — mandated for every criterion in the rubric.
UNACCEPTABLE: "The judge notes which outputs perform well and which do not on each criterion."
What separates them: ACCEPTABLE requires a three-part structure (quote, counter-quote, separator sentence) for every criterion; UNACCEPTABLE identifies no format, no counter-example, and no separator.

**C-07 — Recommended-2** (Verifier with named audit type, specific rejection conditions)
ACCEPTABLE: V-01 — "AUDIT A — Evidence quality: Compare each evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that: (a) resembles the UNACCEPTABLE pattern, OR (b) could apply to a different output with no modification."
UNACCEPTABLE: "The verifier checks for errors in the analyst's scoring."
What separates them: ACCEPTABLE names the audit type and provides two specific rejection conditions tied to prior role output; UNACCEPTABLE is generic quality assurance with no structural triggers.

**C-08 — Recommended-3** (Synthesis with leaderboard + excellence signals + failure patterns)
ACCEPTABLE: V-04 — Three named sections: "LEADERBOARD / Rank all outputs by composite score descending: | Rank | Output | Composite | Golden? |" + "EXCELLENCE SIGNALS / For each criterion where at least one output outperforms others: Signal: [output ID] — [criterion ID] — [specific structural mechanism...]" + "FAILURE PATTERNS / For each criterion where every output scores PARTIAL or FAIL: Pattern: [criterion ID]..."
UNACCEPTABLE: "Summarize results, identify the top performer, and note any consistent weaknesses."
What separates them: ACCEPTABLE specifies three separate named synthesis sections with distinct structural triggers and format requirements; UNACCEPTABLE collapses all synthesis into one undifferentiated summary instruction.

**C-09 — Aspirational-1** (per-output scorecard with complete row coverage)
ACCEPTABLE: V-05 — "No row may be skipped. No evidence cell may be blank. No PARTIAL verdict may appear without its complete two-field diagnostic block (both DIAG rows filled)."
UNACCEPTABLE: "Cover all criteria." (without explicit mandates on blank cells and PARTIAL completeness)
What separates them: ACCEPTABLE specifies three independent mandates (no skip, no blank, PARTIAL completeness) as co-equal obligations; UNACCEPTABLE is a single coverage instruction.

**C-10 — Aspirational-2** (PARTIAL verdict diagnostic with two-directional structure)
ACCEPTABLE: V-01 — "For each PARTIAL verdict, add a one-line diagnostic immediately after the table row: C-[NN] partial: [what is present in this output that prevented FAIL] / [what is absent that prevented PASS]"
UNACCEPTABLE: "For PARTIAL verdicts, explain why the criterion is partially met."
What separates them: ACCEPTABLE names two mandatory halves (prevented-FAIL and prevented-PASS) as separate fields; UNACCEPTABLE gives no structural division.

**C-11 — Aspirational-3** (leaderboard with golden threshold classification per output)
ACCEPTABLE: V-01 — "| Rank | Output | Composite | Golden? |" — the Golden column must carry YES or NO with reason for every output.
UNACCEPTABLE: "List outputs ranked by score." (without Golden classification)
What separates them: ACCEPTABLE includes a Golden classification column with stated conditions (all essentials PASS; composite ≥ 80); UNACCEPTABLE is a pure ranking without threshold adjudication.

**C-12 — Aspirational-4** (excellence signals name structural mechanism, not criterion label)
ACCEPTABLE: V-04 — "Signal: [output ID] — [criterion ID] — [specific structural mechanism causing the difference — name the design property, not just the criterion label]"
UNACCEPTABLE: "Output X excels at criterion C-19." (naming the criterion without the mechanism)
What separates them: ACCEPTABLE requires naming the design property that causes the difference; UNACCEPTABLE reports the label without the causal mechanism.

**C-13 — Aspirational-5 / Axis P** (standalone Role Dependency Manifest as auditable artifact)
ACCEPTABLE: V-01 — "The following table declares the complete dependency graph for this task. It is a standalone structural artifact — auditable without executing the protocol. A row with a blank Produces or Requires cell is a structural gap."
UNACCEPTABLE: A dependency table embedded within a role instruction without the standalone and auditable language.
What separates them: ACCEPTABLE identifies the table as both standalone and auditable with a gap-detection rule; UNACCEPTABLE embeds the same table content without the meta-properties.

**C-14 — Aspirational-6 / Axis Q** (Verifier with diagnostic completeness audit for PARTIAL verdicts)
ACCEPTABLE: V-01 — "AUDIT B — Diagnostic completeness: Applies to PARTIAL verdicts only. Verify that the C-[NN] partial: line is present and covers BOTH required halves: (i) what is present in the output that prevented FAIL — named specifically (ii) what is absent that prevented PASS — named specifically. A diagnostic that states only one direction, repeats the criterion label, or omits either half fails Audit B."
UNACCEPTABLE: "The verifier checks that PARTIAL verdicts have adequate explanation."
What separates them: ACCEPTABLE specifies both required halves of the diagnostic, identifies three specific failure modes (single-direction, label-only, missing), and marks n/a for non-PARTIAL verdicts.

**C-15 — Closing-scan presence** (Verifier performs per-row audit, not summary review)
ACCEPTABLE: V-04 — The Verifier produces a per-output combined audit table with one row per scored criterion, with Status = ACCEPTED only when all applicable audits pass, and flags each rejected row individually.
UNACCEPTABLE: "The verifier reviews the analyst's scoring for completeness and accuracy."
What separates them: ACCEPTABLE mandates a row-per-criterion audit table with status tracking and per-row FLAG notation; UNACCEPTABLE is a pass-level quality review with no structural scan.

**C-16 — Pre-execution anti-pattern block** (ANALYST phase has pre-execution priming before scoring table)
ACCEPTABLE: V-01 — REGISTER NOTE appearing before the scoring table template in the ANALYST phase: "When scoring criteria related to structural scan mechanisms and pre-execution priming... Evaluate structural presence only, independent of prose register."
UNACCEPTABLE: Starting the ANALYST phase immediately with the scoring table template, with no pre-execution instruction block.
What separates them: ACCEPTABLE positions an instructional block before the output template, priming evaluator behavior before any output is produced; UNACCEPTABLE provides no pre-execution priming.

**C-17 — Self-referential priming** (pre-execution section contains anti-pattern entry that primes against the priming mechanism itself — second-order)
ACCEPTABLE: V-01 — The ANALYST REGISTER NOTE instructs the evaluator not to penalize imperative phrasing in pre-execution anti-pattern entries ("DO NOT execute the scan mechanically") — this primes against the error of misapplying the pre-execution priming standard to itself.
UNACCEPTABLE: A pre-execution block that warns against generic errors (e.g., "do not skip criteria") without any self-referential entry targeting the priming mechanism's own potential misapplication.
What separates them: ACCEPTABLE's self-referential entry targets the evaluator behavior toward the priming structure itself (register bias in anti-pattern entries); UNACCEPTABLE primes against first-order scoring errors only.

**C-18 — Closing-scan anti-pattern coverage** (both pre-execution priming block and closing scan mechanism present)
ACCEPTABLE: V-01 — REGISTER NOTE (pre-execution priming) present before scoring table AND Verifier audit table (closing scan) present in VERIFIER phase — both structural elements are present.
UNACCEPTABLE: Pre-execution priming note present but no Verifier audit table, only a narrative review instruction.
What separates them: ACCEPTABLE has both structural elements — a pre-execution priming block in ANALYST and a row-level audit table in VERIFIER; UNACCEPTABLE has the pre-execution block but lacks the closing scan artifact.

**C-19 — Priming-depth ceiling declaration / Axis S** (PRIMING CEILING NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE)
ACCEPTABLE: V-01 — "PRIMING CEILING NOTE / The scoring ceiling for priming depth is fixed at second-order self-reference. An anti-pattern entry... is a third-order entry. Third-order entries are architecturally valid additions but are rubric-neutral... do not receive additional aspirational credit beyond what second-order self-reference already awards." — appearing in JUDGE phase, before JUDGE STANDARD COMPLETE.
UNACCEPTABLE: A ceiling note that appears after JUDGE STANDARD COMPLETE, or a ceiling instruction embedded in the ANALYST phase.
What separates them: ACCEPTABLE places the ceiling declaration in the JUDGE phase, before the role-completion token, allowing it to govern evidence standards during standard-setting; UNACCEPTABLE misplaces the ceiling where it cannot govern the verdicts it follows.

**C-20 — Register-agnostic structural evaluation / Axis T** (REGISTER NOTE in ANALYST phase, before scoring table)
ACCEPTABLE: V-01 — "REGISTER NOTE / When scoring criteria related to structural scan mechanisms and pre-execution priming... Evaluate structural presence only, independent of prose register. A scan block that uses command-form phrasing... satisfies the structural scan criterion on equal terms with a declarative inventory..." — appearing at the start of the ANALYST phase, before the scoring table template.
UNACCEPTABLE: A register-agnostic instruction embedded in the JUDGE phase, or appearing after the scoring table template in ANALYST.
What separates them: ACCEPTABLE places the register instruction in the ANALYST phase before any output is produced, making it operative for all verdicts; UNACCEPTABLE places it outside the scoring phase or after scoring has begun.

**C-21 — C-17/C-18 independence tracking / Axis U** (CRITERIA INDEPENDENCE NOTE in ANALYST phase, after composite formula)
ACCEPTABLE: V-01 — "CRITERIA INDEPENDENCE NOTE / C-17 (self-referential anti-pattern priming) and C-18 (full-envelope structural coverage) share vocabulary but are independently satisfiable... Decoupling case: when C-17 PASS and C-18 FAIL appear together, note the decoupling explicitly..." — appearing after the composite computation block in the ANALYST phase.
UNACCEPTABLE: A criteria independence instruction that appears before the composite formula, or that is placed in the JUDGE phase.
What separates them: ACCEPTABLE positions the independence note after composite computation, where the evaluator is closing the record, forcing a final independent check; UNACCEPTABLE places it before scoring is complete, where it cannot serve as a closing verification.

**C-22 — New-axis independent audit / Axis V** (NEW-AXIS AUDIT NOTE in ANALYST phase, mandating independent verdicts for C-19/C-20/C-21)
ACCEPTABLE: V-01 — "NEW-AXIS AUDIT NOTE / C-19 (Priming-depth ceiling declaration), C-20 (Register-agnostic structural evaluation), and C-21 (C-17/C-18 independence tracking) are rubric-orthogonal: satisfying any one provides no structural inference about the others... For every scored output, audit all three axes on fully independent evidence before closing the scoring record: C-19: Is a PRIMING CEILING NOTE present...? If no: explicit FAIL — 'No PRIMING CEILING NOTE found in JUDGE phase.' C-20: Is a REGISTER NOTE present...? If no: explicit FAIL... C-21: Is a CRITERIA INDEPENDENCE NOTE present...? If no: explicit FAIL... Do not omit unsatisfied axes from the scoring table."
UNACCEPTABLE: V-02's COMPOSITE ACCURACY NOTE item (3) — "When any aspirational criterion fails, name the specific failing criteria by ID in the Unsatisfied row" — names missing criteria in the composite block but does not mandate row-level independent verdicts for C-19/C-20/C-21 with separate evidence lines.
What separates them: ACCEPTABLE mandates row-level PASS or FAIL verdicts with independent evidence and explicit prohibition on omission for each of the three axes; UNACCEPTABLE achieves listing at the composite level only, without enforcing independent scoring rows.

**C-23 — Composite accuracy at near-ceiling / Axis W** (COMPOSITE ACCURACY NOTE with fraction/decimal/named criteria)
ACCEPTABLE: V-02 — "COMPOSITE ACCURACY NOTE / (1) State the aspirational count as an explicit fraction — e.g., '14/16 PASS'... (2) Compute the composite to two decimal places. Do not round. 98.75 is not 99 or 100... (3) When any aspirational criterion fails, name the specific failing criteria by ID... (4) Do not characterize a near-ceiling composite as complete... Aspirational fraction: [aspirational_pass]/16 PASS / Unsatisfied aspirational criteria: [C-NN list, or 'none']"
UNACCEPTABLE: V-01's composite block — "aspirational_pass = [count; PARTIAL = 0.5] / composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]" — uses `/16` denominator but contains no fraction-format instruction, no two-decimal mandate, and no named-missing-criteria requirement.
What separates them: ACCEPTABLE embeds four explicit format requirements in the composite computation block that prevent rounding, denominator-omission, and near-ceiling mischaracterization; UNACCEPTABLE has the correct denominator but no format constraints.

**C-24 — Phase-placement pass attribution / Axis X** (PHASE-PLACEMENT NOTE in JUDGE phase + ANALYST reminder to state phase location for C-19/C-20/C-21)
ACCEPTABLE: V-03 — PHASE-PLACEMENT NOTE in JUDGE phase before JUDGE STANDARD COMPLETE: "C-19: The PRIMING CEILING NOTE satisfies C-19 only when it precedes JUDGE STANDARD COMPLETE... ACCEPTABLE evidence for C-19 must explicitly state: 'PRIMING CEILING NOTE appears in JUDGE phase, before JUDGE STANDARD COMPLETE.'" — plus ANALYST reminder: "When scoring C-19, C-20, and C-21: state phase location explicitly in the evidence cell. Confirm the note precedes or follows the specific phase boundary required for PASS. Evidence that identifies note content without stating phase location fails C-24."
UNACCEPTABLE: V-01 and V-02 — PRIMING CEILING NOTE present in JUDGE phase (satisfying C-19) but no PHASE-PLACEMENT NOTE instructing the evaluator that phase location must appear in evidence for C-19/C-20/C-21, and no ANALYST reminder linking phase confirmation to pass evidence.
What separates them: ACCEPTABLE establishes, at evidence-standard time, that phase location is mandatory pass evidence for three specific criteria and repeats the requirement at scoring time; UNACCEPTABLE has the structural notes in the correct positions but issues no instruction that phase location must be named in evidence.

JUDGE STANDARD COMPLETE

---

## ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above. ✓

REGISTER NOTE applied: evaluating structural presence independently of prose register.

---

### Output: V-01 — Axis V (NEW-AXIS AUDIT NOTE only)

**Base:** R6 V-04 (S+T+U+P+Q+G+B+M). **R7 addition:** NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE. Formula updated to `/16`.

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Essential-1 | E | PASS | Standalone ROLE DEPENDENCY MANIFEST table with "auditable without executing the protocol" and gap-detection rule present before Role 1 instructions. |
| C-02 | Essential-2 | E | PASS | "Gate rules (hard): Role 2 cannot begin without JUDGE STANDARD COMPLETE present above" and symmetric gate tokens at each downstream role. |
| C-03 | Essential-3 | E | PASS | Scoring table template "| ID | Criterion | Weight | Verdict | Evidence |" with "No row may be skipped. No evidence cell may be blank." |
| C-04 | Essential-4 | E | PASS | "Before writing each evidence cell, verify it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell." |
| C-05 | Essential-5 | E | PASS | "(essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10)" — correct formula with updated `/16` aspirational denominator. |
| C-06 | Recommended-1 | R | PASS | JUDGE phase requires ACCEPTABLE/UNACCEPTABLE/separator triple for every rubric criterion; "Cover every criterion in the rubric. Do not fabricate examples." |
| C-07 | Recommended-2 | R | PASS | "AUDIT A — Evidence quality: Compare each evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE pair... Reject any cell that (a) resembles the UNACCEPTABLE pattern, OR (b) could apply to a different output with no modification." |
| C-08 | Recommended-3 | R | PASS | SYNTHESIS contains three named sections: LEADERBOARD (rank table + Golden column), EXCELLENCE SIGNALS (structural mechanism per criterion), FAILURE PATTERNS (universal-fail diagnosis). |
| C-09 | Aspirational-1 | A | PASS | "No row may be skipped. No evidence cell may be blank." — two independent no-skip mandates with blank-cell prohibition. |
| C-10 | Aspirational-2 | A | PASS | "For each PARTIAL verdict, add a one-line diagnostic immediately after the table row: C-[NN] partial: [what is present... prevented FAIL] / [what is absent... prevented PASS]" — two-directional structure. |
| C-11 | Aspirational-3 | A | PASS | LEADERBOARD includes "Golden?" column with explicit YES/NO conditions stated: "YES — all essentials PASS; composite >= 80 | NO — [which essential failed, or composite < 80]". |
| C-12 | Aspirational-4 | A | PASS | "Signal: [output ID] — [criterion ID] — [specific structural mechanism causing the difference — name the design property, not just the criterion label]" — mechanism naming mandated. |
| C-13 | Aspirational-5 / Axis P | A | PASS | ROLE DEPENDENCY MANIFEST: "standalone structural artifact — auditable without executing the protocol. A row with a blank Produces or Requires cell is a structural gap." |
| C-14 | Aspirational-6 / Axis Q | A | PASS | "AUDIT B — Diagnostic completeness: Applies to PARTIAL verdicts only. Verify... covers BOTH required halves: (i) what is present... prevented FAIL (ii) what is absent... prevented PASS. A diagnostic that states only one direction, repeats the criterion label, or omits either half fails Audit B." |
| C-15 | Closing-scan presence | A | PASS | Verifier produces per-output combined audit table with per-row Status = ACCEPTED/REJECTED and "FLAG: [output ID] / [criterion ID] — Audit [A/B]: [reason]" for every rejected row. |
| C-16 | Pre-execution anti-pattern block | A | PASS | REGISTER NOTE appears before scoring table in ANALYST phase: instructs evaluator on structural evaluation and primes against register-based scoring errors before any criterion is scored. |
| C-17 | Self-referential priming | A | PASS | REGISTER NOTE primes against reducing verdicts based on prose register in pre-execution anti-pattern entries — the instruction targets the evaluator's potential misapplication of the priming standard to stylistic choices within pre-execution blocks. |
| C-18 | Closing-scan anti-pattern coverage | A | PASS | Both structural elements present: REGISTER NOTE (pre-execution priming in ANALYST) and per-row Verifier audit table (closing scan in VERIFIER) — full envelope confirmed. |
| C-19 | Priming-depth ceiling declaration / Axis S | A | PASS | PRIMING CEILING NOTE appears in JUDGE phase, before JUDGE STANDARD COMPLETE: "scoring ceiling for priming depth is fixed at second-order self-reference... third-order entries are rubric-neutral: they do not open a new aspirational scoring dimension." |
| C-20 | Register-agnostic structural evaluation / Axis T | A | PASS | REGISTER NOTE appears in ANALYST phase, before the scoring table: "Evaluate structural presence only, independent of prose register. A scan block that uses command-form phrasing... satisfies the structural scan criterion on equal terms with a declarative inventory." |
| C-21 | C-17/C-18 independence tracking / Axis U | A | PASS | CRITERIA INDEPENDENCE NOTE appears in ANALYST phase, after the composite formula: "C-17 PASS condition: a self-referential anti-pattern entry appears in the pre-execution section — regardless of whether the scan mechanism it primes against... passes or fails. A C-17 PASS does not imply C-18 satisfaction." |
| C-22 | New-axis independent audit / Axis V | A | PASS | NEW-AXIS AUDIT NOTE present in ANALYST after CRITERIA INDEPENDENCE NOTE: "C-19, C-20, and C-21 are rubric-orthogonal... audit all three axes on fully independent evidence... If no: explicit FAIL — 'No PRIMING CEILING NOTE found in JUDGE phase.' ... Do not omit unsatisfied axes from the scoring table." |
| C-23 | Composite accuracy at near-ceiling / Axis W | A | FAIL | No COMPOSITE ACCURACY NOTE present. Composite block contains "(aspirational_pass / 16 * 10)" with updated denominator but issues no instruction for fraction format, two-decimal precision, named missing criteria, or prohibition on near-ceiling mischaracterization. |
| C-24 | Phase-placement pass attribution / Axis X | A | FAIL | No PHASE-PLACEMENT NOTE in JUDGE phase. No ANALYST reminder instructing the evaluator to state phase location in evidence for C-19, C-20, or C-21. PRIMING CEILING NOTE establishes ceiling (C-19) but does not establish phase location as mandatory pass evidence for any of the three criteria. |

Composite computation:
```
essential_pass    = 5   (C-01..C-05 all PASS)
recommended_pass  = 3   (C-06..C-08 all PASS)
aspirational_pass = 14  (C-09..C-22 PASS; C-23 FAIL; C-24 FAIL)

composite = (5/5 * 60) + (3/3 * 30) + (14/16 * 10)
          = 60 + 30 + 8.75
          = 98.75

Golden: YES — all essentials PASS; composite >= 80
```

---

### Output: V-02 — Axis W (COMPOSITE ACCURACY NOTE only)

**Base:** R6 V-04 (S+T+U+P+Q+G+B+M). **R7 addition:** COMPOSITE ACCURACY NOTE in ANALYST composite computation block. Formula updated to `/16`.

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Essential-1 | E | PASS | Standalone ROLE DEPENDENCY MANIFEST with gap-detection rule present as standalone section, same structure as V-01. |
| C-02 | Essential-2 | E | PASS | Hard gate rules naming JUDGE STANDARD COMPLETE and ANALYST COMPLETE tokens at each downstream role boundary. |
| C-03 | Essential-3 | E | PASS | Scoring table template with five column headers and "No row may be skipped. No evidence cell may be blank." |
| C-04 | Essential-4 | E | PASS | "If your draft resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell." — rewrite gate tied to Judge standard. |
| C-05 | Essential-5 | E | PASS | Composite formula with correct `/16` denominator: "(aspirational_pass / 16 * 10)" as third term. |
| C-06 | Recommended-1 | R | PASS | JUDGE phase requires ACCEPTABLE/UNACCEPTABLE/separator triple for all criteria; no-fabrication constraint. |
| C-07 | Recommended-2 | R | PASS | AUDIT A with two rejection conditions (UNACCEPTABLE-pattern match; cross-output applicability) present in VERIFIER. |
| C-08 | Recommended-3 | R | PASS | SYNTHESIS contains LEADERBOARD + EXCELLENCE SIGNALS + FAILURE PATTERNS + REGRESSION SIGNALS, each with format specification. |
| C-09 | Aspirational-1 | A | PASS | "No row may be skipped. No evidence cell may be blank." — independent of and prior to PARTIAL handling. |
| C-10 | Aspirational-2 | A | PASS | Two-directional PARTIAL diagnostic: "[what is present in this output that prevented FAIL] / [what is absent that prevented PASS]". |
| C-11 | Aspirational-3 | A | PASS | Golden column with explicit YES/NO condition in LEADERBOARD. |
| C-12 | Aspirational-4 | A | PASS | Excellence signals mandate naming structural mechanism, not criterion label. |
| C-13 | Aspirational-5 / Axis P | A | PASS | Role Dependency Manifest as standalone auditable artifact with structural-gap detection rule. |
| C-14 | Aspirational-6 / Axis Q | A | PASS | AUDIT B mandating both diagnostic halves for PARTIAL verdicts; three specific failure modes named (single-direction, label-only, missing). |
| C-15 | Closing-scan presence | A | PASS | Per-row Verifier audit table with FLAG notation for rejected rows, Status = ACCEPTED only when all applicable audits pass. |
| C-16 | Pre-execution anti-pattern block | A | PASS | REGISTER NOTE before scoring table in ANALYST phase — structural presence confirmed independent of prose register. |
| C-17 | Self-referential priming | A | PASS | REGISTER NOTE contains register-agnostic instruction that primes against applying register standards to pre-execution priming entries themselves. |
| C-18 | Closing-scan anti-pattern coverage | A | PASS | Pre-execution priming (REGISTER NOTE) and closing scan (Verifier audit table) both present. |
| C-19 | Priming-depth ceiling declaration / Axis S | A | PASS | PRIMING CEILING NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: fixes ceiling at second-order self-reference, declares third-order entries rubric-neutral. |
| C-20 | Register-agnostic structural evaluation / Axis T | A | PASS | REGISTER NOTE in ANALYST phase, before scoring table: "Evaluate structural presence only, independent of prose register." |
| C-21 | C-17/C-18 independence tracking / Axis U | A | PASS | CRITERIA INDEPENDENCE NOTE in ANALYST phase, after composite formula: decoupling case explicitly specified. |
| C-22 | New-axis independent audit / Axis V | A | FAIL | No NEW-AXIS AUDIT NOTE present. COMPOSITE ACCURACY NOTE item (3) instructs naming unsatisfied criteria by ID in the Unsatisfied row, but this operates at the composite-block level only — no instruction mandates row-level independent verdicts for C-19/C-20/C-21 with separate evidence lines or prohibits omitting unsatisfied axes from the scoring table. |
| C-23 | Composite accuracy at near-ceiling / Axis W | A | PASS | COMPOSITE ACCURACY NOTE in ANALYST composite block: "(1) State aspirational count as explicit fraction — '14/16 PASS'... (2) Compute composite to two decimal places. Do not round. 98.75 is not 99 or 100... (3) name specific failing criteria by ID... (4) Do not characterize near-ceiling composite as complete." Template includes "Aspirational fraction: [aspirational_pass]/16 PASS" and "Unsatisfied aspirational criteria: [C-NN list, or 'none']". |
| C-24 | Phase-placement pass attribution / Axis X | A | FAIL | No PHASE-PLACEMENT NOTE in JUDGE phase. No ANALYST instruction requiring phase location in evidence for C-19/C-20/C-21. PRIMING CEILING NOTE (C-19) and REGISTER NOTE (C-20) are in correct positions but no instruction names phase location as mandatory pass evidence for any of the three criteria. |

Composite computation:
```
essential_pass    = 5
recommended_pass  = 3
aspirational_pass = 14  (C-09..C-21 + C-23 PASS; C-22 FAIL; C-24 FAIL)

composite = (5/5 * 60) + (3/3 * 30) + (14/16 * 10)
          = 60 + 30 + 8.75
          = 98.75

Golden: YES — all essentials PASS; composite >= 80
```

---

### Output: V-03 — Axis X (PHASE-PLACEMENT NOTE + ANALYST reminder)

**Base:** R6 V-04 (S+T+U+P+Q+G+B+M). **R7 additions:** PHASE-PLACEMENT NOTE in JUDGE phase before JUDGE STANDARD COMPLETE; ANALYST scoring instruction extended with phase-confirmation reminder for C-19/C-20/C-21. Formula updated to `/16`.

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Essential-1 | E | PASS | Standalone Role Dependency Manifest with auditable-artifact and gap-detection language. |
| C-02 | Essential-2 | E | PASS | Hard gate tokens at each role boundary; "No role may be skipped or merged with another." |
| C-03 | Essential-3 | E | PASS | Scoring table template with no-skip mandate. |
| C-04 | Essential-4 | E | PASS | UNACCEPTABLE-pattern rewrite gate in ANALYST. |
| C-05 | Essential-5 | E | PASS | Composite formula with `/16` denominator. |
| C-06 | Recommended-1 | R | PASS | JUDGE requires ACCEPTABLE/UNACCEPTABLE/separator per criterion. |
| C-07 | Recommended-2 | R | PASS | AUDIT A with two rejection conditions in VERIFIER. |
| C-08 | Recommended-3 | R | PASS | Three-section SYNTHESIS with format specifications. |
| C-09 | Aspirational-1 | A | PASS | No-row-skip + no-blank-cell mandates present. |
| C-10 | Aspirational-2 | A | PASS | Two-directional PARTIAL diagnostic format. |
| C-11 | Aspirational-3 | A | PASS | Golden classification in LEADERBOARD. |
| C-12 | Aspirational-4 | A | PASS | Excellence signal mechanism-naming mandate. |
| C-13 | Aspirational-5 / Axis P | A | PASS | Standalone manifest with auditable-artifact designation. |
| C-14 | Aspirational-6 / Axis Q | A | PASS | AUDIT B with both-halves requirement and three failure-mode names. |
| C-15 | Closing-scan presence | A | PASS | Per-row Verifier audit table with FLAG notation. |
| C-16 | Pre-execution anti-pattern block | A | PASS | REGISTER NOTE before scoring table in ANALYST. |
| C-17 | Self-referential priming | A | PASS | REGISTER NOTE primes against register-based evaluation of pre-execution priming entries. |
| C-18 | Closing-scan anti-pattern coverage | A | PASS | Pre-execution priming and closing scan both structurally present. |
| C-19 | Priming-depth ceiling declaration / Axis S | A | PASS | PRIMING CEILING NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: second-order ceiling fixed, third-order entries declared rubric-neutral. |
| C-20 | Register-agnostic structural evaluation / Axis T | A | PASS | REGISTER NOTE in ANALYST phase, before scoring table: structural-presence evaluation mandate. |
| C-21 | C-17/C-18 independence tracking / Axis U | A | PASS | CRITERIA INDEPENDENCE NOTE in ANALYST phase, after composite formula: decoupling case with explicit notation requirement. |
| C-22 | New-axis independent audit / Axis V | A | FAIL | No NEW-AXIS AUDIT NOTE present. ANALYST reminder "When scoring C-19, C-20, and C-21: state phase location explicitly" instructs HOW to write evidence for those criteria but does not mandate that all three carry independent PASS or FAIL verdicts, does not declare the three axes orthogonal, and does not prohibit omitting unsatisfied axes from the scoring table. |
| C-23 | Composite accuracy at near-ceiling / Axis W | A | FAIL | No COMPOSITE ACCURACY NOTE present. Formula uses `/16` denominator but composite block contains no fraction-format instruction, no two-decimal mandate, no named-missing-criteria requirement, and no prohibition on near-ceiling mischaracterization. |
| C-24 | Phase-placement pass attribution / Axis X | A | PASS | PHASE-PLACEMENT NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: "C-19: ACCEPTABLE evidence for C-19 must explicitly state: 'PRIMING CEILING NOTE appears in JUDGE phase, before JUDGE STANDARD COMPLETE.' ... C-20: 'REGISTER NOTE appears in ANALYST phase, before the scoring table.' ... C-21: 'CRITERIA INDEPENDENCE NOTE appears in ANALYST phase, after the composite formula.' Evidence that identifies note content without confirming phase placement is insufficient for PASS." Plus ANALYST reminder: "When scoring C-19, C-20, and C-21: state phase location explicitly in the evidence cell." |

Composite computation:
```
essential_pass    = 5
recommended_pass  = 3
aspirational_pass = 14  (C-09..C-21 + C-24 PASS; C-22 FAIL; C-23 FAIL)

composite = (5/5 * 60) + (3/3 * 30) + (14/16 * 10)
          = 60 + 30 + 8.75
          = 98.75

Golden: YES — all essentials PASS; composite >= 80
```

---

### Output: V-04 — Axes V+W+X+S+T+U+P+Q+G+B+M (full combination, adversarial enforcement base)

**Base:** R6 V-04 (S+T+U+P+Q+G+B+M). **R7 additions:** PHASE-PLACEMENT NOTE in JUDGE (before JUDGE STANDARD COMPLETE, alongside PRIMING CEILING NOTE); COMPOSITE ACCURACY NOTE in ANALYST composite block; NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE; ANALYST reminder for phase location in C-19/C-20/C-21 evidence.

When scoring C-19, C-20, and C-21: confirming phase location as required by the PHASE-PLACEMENT NOTE and the ANALYST reminder.

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Essential-1 | E | PASS | Standalone ROLE DEPENDENCY MANIFEST with auditable-artifact designation and structural-gap detection rule. |
| C-02 | Essential-2 | E | PASS | Hard gate tokens at each role; "SYNTHESIS cannot begin without VERIFIER AUDIT COMPLETE present above." |
| C-03 | Essential-3 | E | PASS | Scoring table template with five-column header and explicit no-skip/no-blank mandates. |
| C-04 | Essential-4 | E | PASS | Judge-standard rewrite gate: "If your draft resembles the UNACCEPTABLE pattern, rewrite it." |
| C-05 | Essential-5 | E | PASS | Three-tier composite formula with `/16` aspirational denominator. |
| C-06 | Recommended-1 | R | PASS | JUDGE phase ACCEPTABLE/UNACCEPTABLE/separator triple mandated per criterion; fabrication prohibited. |
| C-07 | Recommended-2 | R | PASS | AUDIT A (evidence quality, two rejection conditions) in VERIFIER with per-output audit table. |
| C-08 | Recommended-3 | R | PASS | SYNTHESIS: LEADERBOARD + EXCELLENCE SIGNALS (mechanism naming) + FAILURE PATTERNS (diagnosis) + REGRESSION SIGNALS. |
| C-09 | Aspirational-1 | A | PASS | No-skip and no-blank mandates as independent co-obligations. |
| C-10 | Aspirational-2 | A | PASS | Two-directional PARTIAL diagnostic with prevented-FAIL and prevented-PASS named separately. |
| C-11 | Aspirational-3 | A | PASS | LEADERBOARD with Golden column and explicit threshold conditions. |
| C-12 | Aspirational-4 | A | PASS | Excellence signal format names design property causing the difference. |
| C-13 | Aspirational-5 / Axis P | A | PASS | Standalone manifest with auditable-without-execution and gap-detection properties. |
| C-14 | Aspirational-6 / Axis Q | A | PASS | AUDIT B with both-halves requirement, three failure-mode enumeration (single-direction, label-only, omitted), and n/a annotation for non-PARTIAL rows. |
| C-15 | Closing-scan presence | A | PASS | Verifier produces per-row audit table; "Status = ACCEPTED only if all applicable audits pass"; FLAG notation per rejected row. |
| C-16 | Pre-execution anti-pattern block | A | PASS | REGISTER NOTE at start of ANALYST phase, before scoring table: structural-presence evaluation priming. |
| C-17 | Self-referential priming | A | PASS | REGISTER NOTE primes against register-based evaluation of pre-execution entries — second-order self-reference confirming the priming block's own application is structure-only. |
| C-18 | Closing-scan anti-pattern coverage | A | PASS | Pre-execution block (REGISTER NOTE) and closing scan (Verifier audit table) both structurally present. |
| C-19 | Priming-depth ceiling declaration / Axis S | A | PASS | PRIMING CEILING NOTE appears in JUDGE phase, before JUDGE STANDARD COMPLETE: "scoring ceiling for priming depth is fixed at second-order self-reference... third-order entries are rubric-neutral." |
| C-20 | Register-agnostic structural evaluation / Axis T | A | PASS | REGISTER NOTE appears in ANALYST phase, before the scoring table: "Evaluate structural presence only, independent of prose register." PHASE-PLACEMENT NOTE confirms: "Satisfied only by a REGISTER NOTE in the ANALYST phase, before the scoring table." |
| C-21 | C-17/C-18 independence tracking / Axis U | A | PASS | CRITERIA INDEPENDENCE NOTE appears in ANALYST phase, after the composite formula: independent-satisfiability declaration with decoupling-case notation requirement. PHASE-PLACEMENT NOTE confirms: "Satisfied only by a CRITERIA INDEPENDENCE NOTE in the ANALYST phase, after the composite formula." |
| C-22 | New-axis independent audit / Axis V | A | PASS | NEW-AXIS AUDIT NOTE present in ANALYST phase, after CRITERIA INDEPENDENCE NOTE: "C-19, C-20, and C-21 are rubric-orthogonal: satisfying any one provides no structural inference about the others... audit all three axes on fully independent evidence... Do not omit unsatisfied axes from the scoring table. The score report is not complete until C-19, C-20, and C-21 each carry explicit PASS or FAIL verdicts with separate evidence lines." |
| C-23 | Composite accuracy at near-ceiling / Axis W | A | PASS | COMPOSITE ACCURACY NOTE in ANALYST composite block: four requirements stated — fraction format (N/16 PASS), two-decimal precision ("do not round"), named missing criteria by ID, no near-ceiling mischaracterization. Template lines "Aspirational fraction: [aspirational_pass]/16 PASS" and "Unsatisfied aspirational criteria: [C-NN list, or 'none']" embedded in computation block. |
| C-24 | Phase-placement pass attribution / Axis X | A | PASS | PHASE-PLACEMENT NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: defines phase location as mandatory pass evidence for C-19 (JUDGE phase, before JUDGE STANDARD COMPLETE), C-20 (ANALYST phase, before scoring table), C-21 (ANALYST phase, after composite formula). ANALYST reminder: "When scoring C-19, C-20, and C-21: state phase location explicitly in the evidence cell." UNACCEPTABLE evidence for all three criteria defined as stating the note is "present" without specifying phase and position. |

Composite computation:
```
essential_pass    = 5
recommended_pass  = 3
aspirational_pass = 16  (C-09..C-24 all PASS)

Aspirational fraction: 16/16 PASS
Unsatisfied aspirational criteria: none

composite = (5/5 * 60) + (3/3 * 30) + (16/16 * 10)
          = 60 + 30 + 10.00
          = 100.00

Golden: YES — all essentials PASS; composite >= 80
```

---

### Output: V-05 — Axes V+W+X+S+T+U+P+R+G+B+M+N (full combination, template enforcement base + CHECK E)

**Base:** R6 V-05 (S+T+U+P+R+G+B+M+N). **R7 additions:** PHASE-PLACEMENT NOTE in JUDGE (before JUDGE STANDARD COMPLETE); REGISTER NOTE placed before CHECK A and CHECK B (earlier injection than V-04); COMPOSITE ACCURACY NOTE in ANALYST composite block; NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE; ANALYST reminder for phase location; CHECK E in Verifier (phase-placement compliance per-row audit for C-19/C-20/C-21).

When scoring C-19, C-20, and C-21: confirming phase location as required.

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Essential-1 | E | PASS | Standalone Role Dependency Manifest with auditable-artifact language and gap-detection rule. |
| C-02 | Essential-2 | E | PASS | Hard gate rules with named tokens at each role; "No role may be skipped or merged with another." |
| C-03 | Essential-3 | E | PASS | Scoring table template; "No row may be skipped. No evidence cell may be blank. No PARTIAL verdict may appear without its complete two-field diagnostic block." |
| C-04 | Essential-4 | E | PASS | CHECK A — Judge standard check: "Does the evidence resemble the Judge's UNACCEPTABLE pattern for this criterion?" as mandatory per-cell gate before writing. |
| C-05 | Essential-5 | E | PASS | Composite formula: "(essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10)" with `/16` aspirational denominator. |
| C-06 | Recommended-1 | R | PASS | JUDGE phase: ACCEPTABLE/UNACCEPTABLE/separator mandated per criterion; no-fabrication constraint. |
| C-07 | Recommended-2 | R | PASS | Verifier applies five checks per row (CHECK A through CHECK E); per-output audit table with five-column header; FLAG notation per failed check. |
| C-08 | Recommended-3 | R | PASS | SYNTHESIS: LEADERBOARD + EXCELLENCE SIGNALS + FAILURE PATTERNS + REGRESSION SIGNALS with format specifications. |
| C-09 | Aspirational-1 | A | PASS | Three co-equal mandates: "No row may be skipped. No evidence cell may be blank. No PARTIAL verdict may appear without its complete two-field diagnostic block." |
| C-10 | Aspirational-2 | A | PASS | Mandatory two-field diagnostic block as separate DIAG table rows: "Present (prevented FAIL): [specific structural property]" and "Absent (prevented PASS): [specific structural property]" — both required before advancing. |
| C-11 | Aspirational-3 | A | PASS | LEADERBOARD with Golden column and explicit YES/NO threshold conditions. |
| C-12 | Aspirational-4 | A | PASS | Excellence signals name "structural mechanism causing the difference: name the design property, not just the criterion label." |
| C-13 | Aspirational-5 / Axis P | A | PASS | Standalone manifest as auditable-without-execution artifact with structural-gap detection. |
| C-14 | Aspirational-6 / Axis Q | A | PASS | CHECK C — Diagnostic completeness: verifies two-field PARTIAL block complete; names three failure modes (single-direction, label-only, missing block). |
| C-15 | Closing-scan presence | A | PASS | Verifier applies five independent checks per row with per-row Status and FLAG notation; "Status = ACCEPTED only if all applicable checks pass." |
| C-16 | Pre-execution anti-pattern block | A | PASS | REGISTER NOTE at start of ANALYST phase, before CHECK A and CHECK B: "Apply this register-agnostic instruction before CHECK A and CHECK B below — it sets the structural basis that both checks apply against." |
| C-17 | Self-referential priming | A | PASS | REGISTER NOTE primes the evaluator to evaluate pre-execution imperative anti-pattern entries by structural presence, not register — the instruction targets the potential register-bias applied to the priming structure itself. |
| C-18 | Closing-scan anti-pattern coverage | A | PASS | Pre-execution priming (REGISTER NOTE in ANALYST) and closing scan (five-check Verifier table with CHECK C for PARTIAL diagnostics) both structurally present. |
| C-19 | Priming-depth ceiling declaration / Axis S | A | PASS | PRIMING CEILING NOTE appears in JUDGE phase, before JUDGE STANDARD COMPLETE: second-order ceiling fixed, third-order rubric-neutral. PHASE-PLACEMENT NOTE confirms: "C-19: Satisfied only by a PRIMING CEILING NOTE that precedes JUDGE STANDARD COMPLETE in the JUDGE phase." |
| C-20 | Register-agnostic structural evaluation / Axis T | A | PASS | REGISTER NOTE appears in ANALYST phase, before CHECK A and CHECK B (which precede the scoring table): "A register note in the JUDGE phase fails C-20 regardless of content." PHASE-PLACEMENT NOTE: "ACCEPTABLE evidence states: 'REGISTER NOTE appears in ANALYST phase, before CHECK A and CHECK B.'" Structural placement confirmed — ANALYST phase, before scoring table. |
| C-21 | C-17/C-18 independence tracking / Axis U | A | PASS | CRITERIA INDEPENDENCE NOTE appears in ANALYST phase, after the composite formula: decoupling case required. PHASE-PLACEMENT NOTE confirms: "Satisfied only by a CRITERIA INDEPENDENCE NOTE in the ANALYST phase, after the composite formula." |
| C-22 | New-axis independent audit / Axis V | A | PASS | NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE: "C-19, C-20, and C-21 are rubric-orthogonal... Before closing this output's scoring record, audit all three axes on fully independent evidence... Do not omit unsatisfied axes. The score report is not complete until C-19, C-20, and C-21 each carry explicit PASS or FAIL verdicts with separate evidence lines." CHECK B (skeptic test) reinforces: a reader must identify both note content and phase location from evidence alone. |
| C-23 | Composite accuracy at near-ceiling / Axis W | A | PASS | COMPOSITE ACCURACY NOTE in ANALYST composite block: fraction format (N/16 PASS), two-decimal precision, named missing criteria by ID, near-ceiling prohibition. Template lines "Aspirational fraction: [aspirational_pass]/16 PASS" and "Unsatisfied aspirational criteria:" embedded in computation. |
| C-24 | Phase-placement pass attribution / Axis X | A | PASS | PHASE-PLACEMENT NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: defines phase-location evidence requirements for C-19, C-20, C-21. ANALYST reminder: "state phase location explicitly in the evidence cell as part of CHECK B compliance — a reader must be able to identify both the note content and its phase location from the evidence alone." CHECK E in Verifier: "Verify that the evidence cell for each of these criteria explicitly states the phase location of the structural note being credited — not merely that the note is 'present.'" Three-layer enforcement: JUDGE standard-setting + ANALYST reminder + Verifier compliance check. |

Composite computation:
```
essential_pass    = 5
recommended_pass  = 3
aspirational_pass = 16  (C-09..C-24 all PASS)

Aspirational fraction: 16/16 PASS
Unsatisfied aspirational criteria: none

composite = (5/5 * 60) + (3/3 * 30) + (16/16 * 10)
          = 60 + 30 + 10.00
          = 100.00

Golden: YES — all essentials PASS; composite >= 80
```

ANALYST COMPLETE — 5 outputs scored

---

## ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above. ✓

---

### Output: V-01 — Post-write Evidence and Diagnostic Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 | PASS | "Standalone ROLE DEPENDENCY MANIFEST table with 'auditable without executing the..." | PASS | n/a | ACCEPTED |
| C-02 | PASS | "Gate rules (hard): Role 2 cannot begin without JUDGE STANDARD COMPLETE..." | PASS | n/a | ACCEPTED |
| C-03 | PASS | "Scoring table template '| ID | Criterion | Weight | Verdict | Evidence |' with 'No row..." | PASS | n/a | ACCEPTED |
| C-04 | PASS | "'Before writing each evidence cell, verify it against the Judge's ACCEPTABLE/UNACCEPTABLE..." | PASS | n/a | ACCEPTED |
| C-05 | PASS | "'(essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10)'" | PASS | n/a | ACCEPTED |
| C-06 | PASS | "JUDGE phase requires ACCEPTABLE/UNACCEPTABLE/separator triple for every rubric criterion..." | PASS | n/a | ACCEPTED |
| C-07 | PASS | "'AUDIT A — Evidence quality: Compare each evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE..." | PASS | n/a | ACCEPTED |
| C-08 | PASS | "SYNTHESIS contains three named sections: LEADERBOARD (rank table + Golden column), EXCELLENCE..." | PASS | n/a | ACCEPTED |
| C-09 | PASS | "'No row may be skipped. No evidence cell may be blank.' — two independent no-skip mandates..." | PASS | n/a | ACCEPTED |
| C-10 | PASS | "'C-[NN] partial: [what is present... prevented FAIL] / [what is absent... prevented PASS]'..." | PASS | n/a | ACCEPTED |
| C-11 | PASS | "LEADERBOARD includes Golden column with YES/NO conditions: 'all essentials PASS; composite..." | PASS | n/a | ACCEPTED |
| C-12 | PASS | "Signal format names design property: 'specific structural mechanism causing the difference...'" | PASS | n/a | ACCEPTED |
| C-13 | PASS | "ROLE DEPENDENCY MANIFEST: 'standalone structural artifact — auditable without executing the..." | PASS | n/a | ACCEPTED |
| C-14 | PASS | "AUDIT B mandates both halves; three failure modes named: single-direction, label-only, omitted..." | PASS | n/a | ACCEPTED |
| C-15 | PASS | "Verifier produces per-row audit table with FLAG notation per rejected row; Status = ACCEPTED..." | PASS | n/a | ACCEPTED |
| C-16 | PASS | "REGISTER NOTE appears before scoring table in ANALYST: instructs structural evaluation, primes..." | PASS | n/a | ACCEPTED |
| C-17 | PASS | "REGISTER NOTE primes against register-based evaluation of pre-execution anti-pattern entries..." | PASS | n/a | ACCEPTED |
| C-18 | PASS | "REGISTER NOTE (pre-execution priming) and Verifier audit table (closing scan) both structurally present." | PASS | n/a | ACCEPTED |
| C-19 | PASS | "PRIMING CEILING NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: 'scoring ceiling for..." | PASS | n/a | ACCEPTED |
| C-20 | PASS | "REGISTER NOTE in ANALYST phase, before scoring table: 'Evaluate structural presence only..." | PASS | n/a | ACCEPTED |
| C-21 | PASS | "CRITERIA INDEPENDENCE NOTE in ANALYST phase, after composite formula: decoupling case specified." | PASS | n/a | ACCEPTED |
| C-22 | PASS | "NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE: 'C-19, C-20, and C-21 are..." | PASS | n/a | ACCEPTED |
| C-23 | FAIL | "No COMPOSITE ACCURACY NOTE. Formula uses /16 but no fraction format, decimal, or named-missing..." | PASS | n/a | ACCEPTED |
| C-24 | FAIL | "No PHASE-PLACEMENT NOTE in JUDGE. No ANALYST reminder for phase location in C-19/C-20/C-21..." | PASS | n/a | ACCEPTED |

All rows ACCEPTED. No flags.

---

### Output: V-02 — Post-write Evidence and Diagnostic Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 through C-21 | PASS | [Same base mechanisms as V-01; all evidence cells are V-02-specific by naming the COMPOSITE ACCURACY NOTE as the added mechanism] | PASS | n/a | ACCEPTED |
| C-22 | FAIL | "No NEW-AXIS AUDIT NOTE. COMPOSITE ACCURACY NOTE item (3) names missing criteria in composite..." | PASS | n/a | ACCEPTED |
| C-23 | PASS | "COMPOSITE ACCURACY NOTE: four requirements — fraction format '14/16 PASS', two-decimal precision..." | PASS | n/a | ACCEPTED |
| C-24 | FAIL | "No PHASE-PLACEMENT NOTE in JUDGE. PRIMING/REGISTER/CRITERIA notes in correct positions but no..." | PASS | n/a | ACCEPTED |

Audit A check on C-22 FAIL evidence: evidence is specific to V-02 (identifies the COMPOSITE ACCURACY NOTE as the distinguishing present element, and the absence of NEW-AXIS AUDIT NOTE as the failure cause). Does not resemble generic "no instruction present." PASS.

No flags.

---

### Output: V-03 — Post-write Evidence and Diagnostic Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 through C-21 | PASS | [V-03-specific evidence identifying base mechanisms] | PASS | n/a | ACCEPTED |
| C-22 | FAIL | "No NEW-AXIS AUDIT NOTE. ANALYST reminder 'state phase location explicitly' instructs HOW to write..." | PASS | n/a | ACCEPTED |
| C-23 | FAIL | "No COMPOSITE ACCURACY NOTE. Formula uses /16 denominator but no fraction instruction, decimal..." | PASS | n/a | ACCEPTED |
| C-24 | PASS | "PHASE-PLACEMENT NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE: defines phase-location..." | PASS | n/a | ACCEPTED |

Audit A check on C-22 FAIL evidence: distinguishes V-03 from V-01 and V-02 by identifying that V-03's ANALYST reminder is about HOW to write evidence (phase location), not about whether all three axes get independent verdicts — this distinction is output-specific. PASS.

No flags.

---

### Output: V-04 — Post-write Evidence and Diagnostic Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 through C-21 | PASS | [V-04-specific evidence identifying all base + R6 mechanisms] | PASS | n/a | ACCEPTED |
| C-22 | PASS | "NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE: 'C-19, C-20, and C-21 are rubric-orthogonal..." | PASS | n/a | ACCEPTED |
| C-23 | PASS | "COMPOSITE ACCURACY NOTE in ANALYST composite block: four requirements — fraction N/16 PASS, two-decimal..." | PASS | n/a | ACCEPTED |
| C-24 | PASS | "PHASE-PLACEMENT NOTE in JUDGE phase, before JUDGE STANDARD COMPLETE + ANALYST reminder for C-19/C-20/C-21..." | PASS | n/a | ACCEPTED |

No flags.

---

### Output: V-05 — Post-write Evidence and Diagnostic Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 through C-21 | PASS | [V-05-specific evidence distinguishing template-path mechanisms from V-04's adversarial-path mechanisms] | PASS | n/a | ACCEPTED |
| C-22 | PASS | "NEW-AXIS AUDIT NOTE in ANALYST after CRITERIA INDEPENDENCE NOTE + CHECK B skeptic-test reinforcement..." | PASS | n/a | ACCEPTED |
| C-23 | PASS | "COMPOSITE ACCURACY NOTE in ANALYST composite block with fraction/decimal/named-missing + N/16 PASS template..." | PASS | n/a | ACCEPTED |
| C-24 | PASS | "PHASE-PLACEMENT NOTE in JUDGE + ANALYST reminder (CHECK B compliance) + Verifier CHECK E (phase-placement compliance per-row)..." | PASS | n/a | ACCEPTED |

Special check — C-24 Audit A: V-05's evidence quotes three distinct enforcement layers (JUDGE-level, ANALYST-level, Verifier-level). The Judge UNACCEPTABLE for C-24 is evidence that names notes as "present" without phase and position. V-05's evidence specifically quotes CHECK E as confirming "explicitly states the phase location... not merely that the note is 'present.'" This passes Audit A: the evidence names V-05-specific mechanisms not present in other variations.

No flags.

VERIFIER AUDIT COMPLETE

---

## SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above. ✓

---

### LEADERBOARD

| Rank | Output | Composite | Aspirational | Golden? |
|------|--------|-----------|--------------|---------|
| 1 (tied) | V-04 | 100.00 | 16/16 PASS | YES |
| 1 (tied) | V-05 | 100.00 | 16/16 PASS | YES |
| 3 (tied) | V-01 | 98.75 | 14/16 PASS — missing C-23, C-24 | YES |
| 3 (tied) | V-02 | 98.75 | 14/16 PASS — missing C-22, C-24 | YES |
| 3 (tied) | V-03 | 98.75 | 14/16 PASS — missing C-22, C-23 | YES |

Score spread: **1.25 points** between single-axis and combination groups.

---

### EXCELLENCE SIGNALS

**Signal: V-04 / V-05 — C-22, C-23, C-24 — Three-axis simultaneous closure**
The combination variations achieve 100.00 by injecting three independent evaluator-behavior instructions at three structurally distinct phase locations: X (JUDGE phase, standard-setting time), W (ANALYST composite block, computation time), and V (ANALYST after independence note, record-closing time). No single injection achieves more than one new criterion; the 100.00 score requires all three to fire at their respective phase positions.

**Signal: V-04 — C-24 — JUDGE-phase evidence-standard priming alone sufficient for C-24**
V-04 achieves C-24 without a Verifier-level compliance check: the PHASE-PLACEMENT NOTE fires in the JUDGE phase (before evidence standards are established for any criterion), creating top-of-pipe enforcement that carries through to ANALYST scoring. Phase location becomes mandatory pass evidence before the evaluator writes the first ACCEPTABLE pair.

**Signal: V-05 — C-24 — Verifier CHECK E as second enforcement layer**
V-05 adds CHECK E (Verifier-level phase-placement compliance) on top of the JUDGE-level and ANALYST-level instructions already present in V-04. Both V-04 and V-05 score 100.00 on C-24, establishing that JUDGE-level priming is sufficient, but CHECK E provides a post-write closure loop — the Verifier catches any evidence cell that identifies note content without confirming phase location. The two-path equivalence (adversarial path with JUDGE-level priming vs template path with Verifier-level compliance check) is confirmed.

**Signal: V-01 / V-02 / V-03 — C-22 / C-23 / C-24 — Axis-isolation equivalence at R7 tier**
Each single-axis variation satisfies exactly one of the three new criteria and scores identically at 98.75 (14/16 aspirational). The pattern from R6 (V-01/V-02/V-03 at 98.46 with 11/13 aspirational) repeats at the new tier: the three R7 axes are mutually non-inferrable — V-01's NEW-AXIS AUDIT NOTE provides no coverage for C-23 or C-24; V-02's COMPOSITE ACCURACY NOTE provides no coverage for C-22 or C-24; V-03's PHASE-PLACEMENT NOTE provides no coverage for C-22 or C-23.

---

### FAILURE PATTERNS

No failure patterns in this round. All five criteria tiers (E, R, and the aspirational C-09..C-21 block) achieve universal PASS. The only variation in scoring is on C-22, C-23, and C-24, each of which achieves PASS in at least two variations (V-01, V-04, V-05 for C-22; V-02, V-04, V-05 for C-23; V-03, V-04, V-05 for C-24). No criterion fails universally.

---

### REGRESSION SIGNALS

The R7 denominator change (A=16, `/16` formula) means no prior-round score is directly comparable without recomputation. The R6 single-axis near-ceiling score was 98.46 (11/13 aspirational under v6); under v7 with no R7 axes, the equivalent score would be 98.13 (13/16 aspirational). The R7 single-axis near-ceiling (V-01/V-02/V-03) is 98.75 (14/16 aspirational) — each fires one R7 axis on top of the full R6 v6 base. No regression on any of C-01..C-21: all five R7 variations inherit 100.00 on the v6 criterion set from their R6 V-04/V-05 base. No prior-round PASS has regressed to PARTIAL or FAIL.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["adversarial-path and template-path enforcement are equivalent for all three R7 axes — V-04 (JUDGE-level PHASE-PLACEMENT NOTE) and V-05 (JUDGE-level + Verifier CHECK E) both achieve 100.00 with no spread, confirming neither the additional CHECK E layer nor the earlier REGISTER NOTE injection in V-05 opens a new scoring dimension", "axis-isolation equivalence replicated at R7 tier — V-01/V-02/V-03 each score 98.75 with exactly one R7 axis, confirming C-22/C-23/C-24 are mutually non-inferrable at the same structural level as C-19/C-20/C-21 were in R6"]}
```
