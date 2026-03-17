# Quest Score -- Round 14 Variations
**Skill**: quest-score
**Rubric**: v14 (N_essential=4, N_recommended=3, N_aspirational=25)
**Date**: 2026-03-15
**Round**: 14

---

## Design logic

### Unachieved ceiling entering R14

R13 was scored against rubric v13 (N_aspirational=23). Rubric v14 adds C-31
(Register cell gate enforces YES-only completion: NO is a blocking value) and C-32
(Single consolidated register unifies all production-time obligations as columns in
one artifact).

| Criterion | R13 status | Gap analysis |
|-----------|------------|--------------|
| C-31 | DERIVED from R13 | C-25 ACCEPTABLE in the R13 JUDGE STANDARD names "A 'NO' in any cell blocks JUDGE STANDARD COMPLETE" as the distinguishing mechanism. R13 V-01 closes blank-path AND YES-only simultaneously ("all 30 rows show YES in both columns"). R13 V-04 closes YES-only in all three columns ("Every row must show YES in all three columns"). R13 V-03's lifecycle check verifies only blank non-emptiness ("All cells in every row contain YES or NO") -- it checks that a value was written but does not name NO as a blocking value; an inspector reading the lifecycle gate cannot determine from the gate instruction alone whether NO is acceptable. V-01 and V-04 satisfy C-31 under v14 scoring; V-02 satisfies C-31 ("Every row must show YES in all three columns"); V-03 is PARTIAL at best (blank blocking confirmed, NO-as-blocking not stated as a gate consequence). |
| C-32 | DERIVED from R13 | C-30 ACCEPTABLE in the R13 JUDGE STANDARD names "5-column PAIR COVERAGE REGISTER with 'ACCEPTABLE source annotated' YES/NO as 5th column" as the consolidated form. R13 V-02, V-04, V-05 all include a 5-column register with pair present, separating property, and ACCEPTABLE source annotated as columns in the same artifact -- one inspectable surface. R13 V-01 and V-03 use 4-column registers with behavioral annotation obligations; annotation is not a register column and can be independently tracked or omitted. V-02, V-04, V-05 satisfy C-32 under v14 scoring; V-01, V-03 fail. |

### Formula change

N_aspirational increases from 23 to 25. All variations must update the composite
formula from `aspirational_pass / 23 * 10` to `aspirational_pass / 25 * 10`. A
variation using /23 produces systematically incorrect scores -- a C-02 FAIL and a
C-07 error for every output. The PAIR COVERAGE REGISTER also expands from 30 rows
(C-01 through C-30) to 32 rows (C-01 through C-32). Both the formula update and the
register row expansion are required infrastructure for every R14 variation; they are
not themselves variation axes.

### New mechanism gaps

**For C-31 (YES-only cell gate):**
C-31 closes the remaining bypass that C-28 leaves open: a cell containing NO is
not blank (satisfies C-28's blank-blocking rule) but contains an unmet obligation.
A register design that only states "blank = structural violation" allows a scorer to
write NO (obligation acknowledged but not satisfied) and still issue JUDGE STANDARD
COMPLETE. C-31 closes this by requiring the register design to explicitly name NO as
a blocking value -- either in the register header, in the gate rules, or in an
equivalent structural declaration. The test for pass is: can a reader determine from
the gate instruction alone, without inference, that writing NO in any cell prevents
JUDGE STANDARD COMPLETE? A preamble comment that says "NO means the obligation is
unmet" without a gate consequence does not satisfy C-31 -- it names the interpretation
without establishing the enforcement. The gate-rule form ("A NO cell in any required
column blocks JUDGE STANDARD COMPLETE") is the structural enforcement.

**For C-32 (consolidated register):**
C-32 requires all production-time obligations (pair present, separating property
declared, ACCEPTABLE source annotated) to be columns in ONE register artifact. The
bypass path that C-32 closes: two separate registers can each reach COMPLETE
independently while the combined obligation lags. A 5-column consolidated register
makes all three obligations visible in a single inspection. A design that has a
4-column pair/sep register plus a behavioral annotation obligation fails C-32; a
design that has a 4-column register plus a separate annotation log also fails C-32
(split surface). Only a single artifact with all three columns satisfies C-32.

### New axes for R14

| Axis | Label | Mechanism |
|------|-------|-----------|
| YG | YES-only gate rule | Gate rules section explicitly names NO as a blocking value: "A NO cell in any required column blocks JUDGE STANDARD COMPLETE. Only YES is a passing cell value." Closes C-31 via the gate-rule enforcement form. |
| CR | Consolidated register | Register explicitly labeled as CONSOLIDATED PRODUCTION-TIME REGISTER; all three obligations (pair present, separating property declared, ACCEPTABLE source annotated) present as columns in the same 32-row artifact; explicit declaration that no production-time obligation may be tracked outside this register. Closes C-32. |
| YP | YES-only preamble only | YES-only constraint stated in a preamble comment above the register table ("Note: NO = obligation unmet = blocks. Only YES passes.") but NOT in gate rules. Tests whether preamble form satisfies C-31 -- hypothesis is PARTIAL, because gate rules specify structural consequences and a preamble declares intent without enforcing. |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (YG)**: YES-only gate rule, 4-column register (no annotation column). Annotation
  is behavioral (preamble instruction in JUDGE role text). SYNTHESIS gate has BOTH...AND
  + prohibition complement (from R12 best). Formula /25, 32 rows.
  Predicts: C-31 PASS (gate rules name NO as blocking), C-32 FAIL (annotation is not a
  register column; obligation tracked behaviorally, not structurally), C-02 PASS (/25).

- **V-02 (CR without YG)**: 5-column CONSOLIDATED PRODUCTION-TIME REGISTER. Blank-blocking
  stated in header; NO value NOT named as blocking in gate rules or register header
  (only "blank = structural violation"). SYNTHESIS gate uses BOTH...AND without
  prohibition. Formula /25, 32 rows.
  Predicts: C-32 PASS (all three obligations consolidated), C-31 PARTIAL (blank blocks
  per header; NO is a structurally valid non-blocking value -- a row with NO in any
  column satisfies the blank-blocking rule while leaving the obligation unmet), C-29
  PARTIAL (BOTH...AND without prohibition leaves interpretive bypass open).

- **V-03 (YP + CR)**: 5-column consolidated register. YES-only constraint named in
  preamble comment above the register table ("NO = obligation unmet = blocks JUDGE
  STANDARD COMPLETE") but gate rules state only "blank = structural violation" for
  enforcement. SYNTHESIS gate uses BOTH...AND without prohibition. Formula /25, 32 rows.
  Tests whether preamble naming of NO-as-blocking satisfies C-31 when the gate rule
  omits it.
  Predicts: C-31 PARTIAL (preamble names NO as an obligation-failure state but the
  structural gate consequence is only stated for blank; a design with no-blocking
  consequence in the gate rule cannot be satisfied/violated by inspection of the gate
  rule alone), C-32 PASS (consolidated), C-29 PARTIAL (no prohibition).

### Combination selection rationale

- **V-04 (YG + CR + prohibition)**: YES-only gate rule + consolidated 5-column register
  + SYNTHESIS prohibition complement. Closes C-31 (gate rule), C-32 (consolidated),
  C-29 (prohibition). No lifecycle gates; tests whether the three R14 mechanisms
  are sufficient for full pass on new criteria without the lifecycle enforcement layer.

- **V-05 (full stack R14)**: All mechanisms from R13 V-05 best performer, updated for
  R14: formula /25, 32-row register, YES-only in gate rules AND in lifecycle check
  (both blank AND NO block REGISTER COMPLETENESS CONFIRMED), 5-column consolidated,
  ANNOTATION COVERAGE CONFIRMED lifecycle gate, SYNTHESIS BOTH...AND + prohibition,
  formula anchor /25 in manifest, Verifier Audit D for formula anchor. Maximum
  structural footprint for R14.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| YES-only gate rule (YG) | YES | NO | NO (preamble only) | YES | YES |
| Consolidated 5-column register (CR) | NO (4-col) | YES | YES | YES | YES |
| SYNTHESIS prohibition complement | YES | NO | NO | YES | YES |
| Annotation register column | NO (behavioral) | YES | YES | YES | YES |
| ANNOTATION COVERAGE CONFIRMED lifecycle gate | NO | NO | NO | NO | YES |
| REGISTER COMPLETENESS CONFIRMED lifecycle gate | NO | NO | NO | NO | YES |
| Formula anchor /25 in manifest | NO | NO | NO | NO | YES |
| Verifier Audit D (formula anchor check) | NO | NO | NO | NO | YES |
| Register rows | 32 | 32 | 32 | 32 | 32 |
| Register columns | 4 | 5 | 5 | 5 | 5 |
| Formula divisor | /25 | /25 | /25 | /25 | /25 |

---

## V-01 -- Axis YG: YES-only gate rule, 4-column register

**Variation axis**: Register gate -- the gate rules section explicitly names NO as a
blocking value ("A NO cell in any required column blocks JUDGE STANDARD COMPLETE. Only
YES is a passing cell value."), closing the bypass that C-28's blank-only rule leaves
open. The register remains 4 columns (no annotation column); annotation is a behavioral
obligation (preamble instruction) rather than a structural column.

**Hypothesis**: C-31 is closed by the gate-rule form: a reader can determine from the
gate rules alone, without inference, that writing NO prevents JUDGE STANDARD COMPLETE.
C-32 is not satisfied: annotation obligation is tracked behaviorally, not as a register
column, so the pair/sep register and the annotation obligation are on separate
enforcement surfaces. The 4-column register cannot unify all three obligations in one
inspectable artifact. C-29 is satisfied (SYNTHESIS prohibition complement inherited).
The variation isolates whether C-31 pass requires gate-rule form specifically, or
whether any YES-only declaration suffices.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task, including
each role's domain boundary. It is a standalone structural artifact -- auditable
without executing the protocol. A row with a blank cell is a structural gap. No role
may begin unless its Requires entry is present in the output above.

| Role      | Requires                                                                    | Produces                | Domain (ONLY)                                                                                                                               | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-32)   | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                    | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                  | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                       | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                       | Re-scoring, re-auditing                                                                   |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE
    present above. Both tokens must appear simultaneously as a strict conjunction --
    holding either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone
    does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-32), produce a Judge standard entry with three required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. It must be expressed as a named label followed by the two mechanism poles
separated by "vs" -- not embedded in prose.

When writing each ACCEPTABLE entry, attach an explicit "from [Output-N]:" prefix
annotation naming the specific output the example was drawn from. All ACCEPTABLE
examples must carry this prefix; an example without it is not fully grounded. This
is a behavioral obligation -- verify your own compliance before issuing JUDGE STANDARD
COMPLETE.

Before issuing JUDGE STANDARD COMPLETE, produce the PAIR COVERAGE REGISTER confirming
all 32 criteria are covered. This register is a standalone structural artifact -- its
absence or any missing row blocks JUDGE STANDARD COMPLETE.

PAIR COVERAGE REGISTER

No-skip column rule: every cell in every row must contain YES or NO. A blank cell in
any required column (Pair present or Separating property declared) is a structural
violation equivalent to a missing row and blocks JUDGE STANDARD COMPLETE.

YES-only gate: A NO cell in any required column also blocks JUDGE STANDARD COMPLETE.
Only YES is a passing cell value. A row with YES in both columns is complete; a row
with NO in any column, or a blank in any column, is incomplete and blocks JUDGE
STANDARD COMPLETE until corrected.

  | Criterion | Criterion name | Pair present | Separating property declared |
  |-----------|----------------|--------------|------------------------------|
  | C-01      | [name]         | YES / NO     | YES / NO                     |
  | C-02      | [name]         | YES / NO     | YES / NO                     |
  | C-03      | [name]         | YES / NO     | YES / NO                     |
  | C-04      | [name]         | YES / NO     | YES / NO                     |
  | C-05      | [name]         | YES / NO     | YES / NO                     |
  | C-06      | [name]         | YES / NO     | YES / NO                     |
  | C-07      | [name]         | YES / NO     | YES / NO                     |
  | C-08      | [name]         | YES / NO     | YES / NO                     |
  | C-09      | [name]         | YES / NO     | YES / NO                     |
  | C-10      | [name]         | YES / NO     | YES / NO                     |
  | C-11      | [name]         | YES / NO     | YES / NO                     |
  | C-12      | [name]         | YES / NO     | YES / NO                     |
  | C-13      | [name]         | YES / NO     | YES / NO                     |
  | C-14      | [name]         | YES / NO     | YES / NO                     |
  | C-15      | [name]         | YES / NO     | YES / NO                     |
  | C-16      | [name]         | YES / NO     | YES / NO                     |
  | C-17      | [name]         | YES / NO     | YES / NO                     |
  | C-18      | [name]         | YES / NO     | YES / NO                     |
  | C-19      | [name]         | YES / NO     | YES / NO                     |
  | C-20      | [name]         | YES / NO     | YES / NO                     |
  | C-21      | [name]         | YES / NO     | YES / NO                     |
  | C-22      | [name]         | YES / NO     | YES / NO                     |
  | C-23      | [name]         | YES / NO     | YES / NO                     |
  | C-24      | [name]         | YES / NO     | YES / NO                     |
  | C-25      | [name]         | YES / NO     | YES / NO                     |
  | C-26      | [name]         | YES / NO     | YES / NO                     |
  | C-27      | [name]         | YES / NO     | YES / NO                     |
  | C-28      | [name]         | YES / NO     | YES / NO                     |
  | C-29      | [name]         | YES / NO     | YES / NO                     |
  | C-30      | [name]         | YES / NO     | YES / NO                     |
  | C-31      | [name]         | YES / NO     | YES / NO                     |
  | C-32      | [name]         | YES / NO     | YES / NO                     |

JUDGE STANDARD COMPLETE may not be issued until all 32 rows show YES in both
columns. A blank cell or a NO cell in any column blocks this gate.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table format:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict           | Evidence                           | Present_mechanism | Absent_mechanism |
  |------|-----------|--------|-------------------|------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [evidence grounded in this output] | --                | --               |

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present in this output
    and prevented FAIL. For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent in this output and
    prevented PASS. For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a
    structural violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or
  Absent_mechanism cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 25 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic and are Present_mechanism
and Absent_mechanism columns non-empty on PARTIAL rows? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per output:

AUDIT A -- Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B -- Diagnostic column presence: Applies to PARTIAL verdicts only. Verify that:
  (i)  Present_mechanism cell is non-empty (contains named content, not -- or blank)
  (ii) Absent_mechanism cell is non-empty (contains named content, not -- or blank)
This audit verifies column non-emptiness only. Whether the content names a specific
structural property is the CONFIRMER's domain.
Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge domain),
scoring verdicts (Analyst domain).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer asks one question per PARTIAL column cell: does this text identify a
real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |
  |-----------|---------------------------------------|-----------|---------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words of Present content]   | YES / NO  | [first 15 words of Absent content]    | YES / NO  | CONFIRMED/CHALLENGED |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap:
        e.g., "explicit gate token ANALYST COMPLETE coupling Analyst to Verifier",
              "no post-write verification step independent of the writer",
              "named Produces/Requires manifest table with DOMAIN and CANNOT CHECK entries"
  NO  -- uses a criterion label, a generic quality phrase, or restates the verdict:
        e.g., "some structure is present", "mechanism is partially addressed",
              "does not fully satisfy the criterion", "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens must appear simultaneously as a strict conjunction -- holding
either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone does not
satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference -- name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-02 -- Axis CR (without YG): Consolidated register, no YES-only gate rule

**Variation axis**: Output format -- the PAIR COVERAGE REGISTER is replaced by a
CONSOLIDATED PRODUCTION-TIME REGISTER with an explicit declaration that this is the
single artifact tracking all production-time obligations. The fifth column (ACCEPTABLE
source annotated) is present and mandatory. The annotation obligation is enforced as a
register column, not behaviorally. The register header states "blank = structural
violation" but does NOT name NO as a blocking value in the gate rules. SYNTHESIS uses
BOTH...AND without a prohibition clause.

**Hypothesis**: C-32 is closed by the consolidated label and column structure: all three
obligations (pair present, separating property, annotation) are visible in one
inspection, and no obligation can be satisfied through a separate artifact. C-31 is
PARTIAL: the header states blank-blocking (C-28 compliant) but does not name NO as a
blocking gate consequence -- a scorer who writes NO in the annotation column produces a
"valid non-blank" value that passes C-28 inspection while leaving the annotation
obligation unmet. The absence of an explicit YES-only gate rule is the bypass path C-31
closes; its absence here predicts PARTIAL. C-29 is PARTIAL (BOTH...AND without
prohibition).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task, including
each role's domain boundary. It is a standalone structural artifact -- auditable
without executing the protocol. A row with a blank cell is a structural gap. No role
may begin unless its Requires entry is present in the output above.

| Role      | Requires                                                  | Produces                | Domain (ONLY)                                                                                                                                                                           | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                    | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-32) with annotation-field column  | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                   | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                                | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                          | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                              | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                   | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                   | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE    | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                   | Re-scoring, re-auditing                                                                   |
|           | (both required independently)                             |                         |                                                                                                                                                                                         |                                                                                           |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE
    present above. Both tokens are required independently; CONFIRMATION COMPLETE alone
    does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-32), produce a Judge standard entry with three required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. It must be expressed as a named label followed by the two mechanism poles
separated by "vs" -- not embedded in prose.

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation naming the
specific output the example was drawn from. The "ACCEPTABLE source annotated" column
in the CONSOLIDATED PRODUCTION-TIME REGISTER records whether this annotation is present
for each entry. Populate this column as you write each entry:

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output the example was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement
      not tied to a specific output by name.
    - A blank cell in this column is a structural violation blocking JUDGE STANDARD
      COMPLETE under the no-skip column rule.

Before issuing JUDGE STANDARD COMPLETE, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER confirming all 32 criteria are covered. This register is the single
inspectable artifact for all JUDGE production-time obligations. No production-time
obligation in this design is tracked outside this register.

CONSOLIDATED PRODUCTION-TIME REGISTER

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns (Pair present, Separating property declared, ACCEPTABLE source
annotated). A blank cell in any column is a structural violation equivalent to a
missing row and blocks JUDGE STANDARD COMPLETE.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-02      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-03      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-04      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-05      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-06      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-07      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-08      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-09      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-10      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-11      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-12      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-13      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-14      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-15      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-16      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-17      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-18      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-19      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-20      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-21      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-22      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-23      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-24      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-25      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-26      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-27      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-28      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-29      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-30      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-31      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-32      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

A blank cell in any column blocks JUDGE STANDARD COMPLETE under the no-skip column
rule. Every row must have all three columns populated before JUDGE STANDARD COMPLETE
may be issued.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table format:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict           | Evidence                           | Present_mechanism | Absent_mechanism |
  |------|-----------|--------|-------------------|------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [evidence grounded in this output] | --                | --               |

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present in this output
    and prevented FAIL. For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent in this output and
    prevented PASS. For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a
    structural violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or
  Absent_mechanism cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 25 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic and are Present_mechanism
and Absent_mechanism columns non-empty on PARTIAL rows? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per output:

AUDIT A -- Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B -- Diagnostic column presence: Applies to PARTIAL verdicts only. Verify that:
  (i)  Present_mechanism cell is non-empty (contains named content, not -- or blank)
  (ii) Absent_mechanism cell is non-empty (contains named content, not -- or blank)
This audit verifies column non-emptiness only. Whether the content names a specific
structural property is the CONFIRMER's domain.
Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge domain),
scoring verdicts (Analyst domain).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer asks one question per PARTIAL column cell: does this text identify a
real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |
  |-----------|---------------------------------------|-----------|---------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words of Present content]   | YES / NO  | [first 15 words of Absent content]    | YES / NO  | CONFIRMED/CHALLENGED |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap
  NO  -- uses a criterion label, generic quality phrase, or restates the verdict

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens are required independently; CONFIRMATION COMPLETE alone does not
satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference]

If no variation outperforms any other: "No score spread found."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression with output ID,
criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-03 -- Axes YP+CR: Preamble YES-only declaration + consolidated register

**Variation axis**: Phrasing register -- the CONSOLIDATED PRODUCTION-TIME REGISTER
includes a preamble comment above the table that names NO as an obligation-failure state
("Note: a NO in any column means the obligation for that row is unmet and blocks JUDGE
STANDARD COMPLETE. Only YES is a passing value."). However, the gate rules section only
names blank-blocking ("A blank cell in any column is a structural violation blocking
JUDGE STANDARD COMPLETE") -- the preamble is an intent-declaration, not a gate-rule
enforcement. The 5-column consolidated register is present. SYNTHESIS uses BOTH...AND
without prohibition.

**Hypothesis**: C-32 is closed by the 5-column consolidated register (all three
obligations as columns in one artifact). C-31 is PARTIAL: the preamble names NO as an
obligation-failure state (more than no mention), but the gate rule only lists blank as
the enforcement consequence -- a scorer reading the gate rules alone cannot determine
that writing NO blocks JUDGE STANDARD COMPLETE. C-31 pass condition requires the gate-
rule (or equivalent structural gate declaration) to name NO as blocking; a preamble
comment is intent without enforcement. C-29 is PARTIAL (no prohibition).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task, including
each role's domain boundary. It is a standalone structural artifact -- auditable
without executing the protocol. A row with a blank cell is a structural gap. No role
may begin unless its Requires entry is present in the output above.

| Role      | Requires                                                  | Produces                | Domain (ONLY)                                                                                                                                                                           | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                    | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-32) with annotation-field column  | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                   | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                                | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                          | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                              | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                   | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                   | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE    | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                   | Re-scoring, re-auditing                                                                   |
|           | (both required independently)                             |                         |                                                                                                                                                                                         |                                                                                           |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE
    present above. Both tokens are required independently; CONFIRMATION COMPLETE alone
    does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-32), produce a Judge standard entry with three required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. It must be expressed as a named label followed by the two mechanism poles
separated by "vs" -- not embedded in prose.

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation naming the
specific output the example was drawn from. The "ACCEPTABLE source annotated" column
in the CONSOLIDATED PRODUCTION-TIME REGISTER records whether this annotation is present
for each entry. Populate this column as you write each entry:

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output the example was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement
      not tied to a specific output by name.
    - A blank cell in this column is a structural violation blocking JUDGE STANDARD
      COMPLETE under the no-skip column rule.

Before issuing JUDGE STANDARD COMPLETE, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER confirming all 32 criteria are covered. This register is the single
inspectable artifact for all JUDGE production-time obligations. No production-time
obligation is tracked outside this register.

CONSOLIDATED PRODUCTION-TIME REGISTER

Note: a NO in any column means the obligation for that row is unmet and should be
treated as blocking JUDGE STANDARD COMPLETE. Only YES values indicate a satisfied
obligation. Resolve any NO cells before issuing JUDGE STANDARD COMPLETE.

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns (Pair present, Separating property declared, ACCEPTABLE source
annotated). A blank cell in any column is a structural violation equivalent to a
missing row and blocks JUDGE STANDARD COMPLETE.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-02      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-03      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-04      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-05      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-06      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-07      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-08      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-09      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-10      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-11      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-12      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-13      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-14      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-15      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-16      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-17      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-18      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-19      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-20      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-21      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-22      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-23      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-24      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-25      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-26      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-27      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-28      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-29      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-30      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-31      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-32      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

A blank cell in any column blocks JUDGE STANDARD COMPLETE under the no-skip column
rule. Every row must have all three columns populated before JUDGE STANDARD COMPLETE
may be issued.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table format:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict           | Evidence                           | Present_mechanism | Absent_mechanism |
  |------|-----------|--------|-------------------|------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [evidence grounded in this output] | --                | --               |

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present in this output
    and prevented FAIL. For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent in this output and
    prevented PASS. For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a
    structural violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or
  Absent_mechanism cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 25 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic and are Present_mechanism
and Absent_mechanism columns non-empty on PARTIAL rows? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per output:

AUDIT A -- Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B -- Diagnostic column presence: Applies to PARTIAL verdicts only. Verify that:
  (i)  Present_mechanism cell is non-empty (contains named content, not -- or blank)
  (ii) Absent_mechanism cell is non-empty (contains named content, not -- or blank)
This audit verifies column non-emptiness only. Whether the content names a specific
structural property is the CONFIRMER's domain.
Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge domain),
scoring verdicts (Analyst domain).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer asks one question per PARTIAL column cell: does this text identify a
real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |
  |-----------|---------------------------------------|-----------|---------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words of Present content]   | YES / NO  | [first 15 words of Absent content]    | YES / NO  | CONFIRMED/CHALLENGED |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap
  NO  -- uses a criterion label, generic quality phrase, or restates the verdict

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens are required independently; CONFIRMATION COMPLETE alone does not
satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference]

If no variation outperforms any other: "No score spread found."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression with output ID,
criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-04 -- Axes YG+CR+prohibition: YES-only gate rule + consolidated register + SYNTHESIS prohibition

**Variation axis**: YG (YES-only gate rule) + CR (consolidated 5-column register) +
prohibition complement in SYNTHESIS gate. No lifecycle gates. Tests whether the three
R14 mechanisms (C-31, C-32, and C-29 maintenance) are sufficient for full pass without
the lifecycle enforcement layer.

**Hypothesis**: C-31 is closed by the explicit gate-rule naming of NO as a blocking
value ("A NO cell in any required column blocks JUDGE STANDARD COMPLETE. Only YES is
a passing cell value."). C-32 is closed by the consolidated 5-column register with
explicit declaration that no production-time obligation is tracked outside it. C-29 is
maintained by the SYNTHESIS prohibition complement. C-02 is PASS (/25). No lifecycle
gates means C-30 of the annotation enforcement is handled at the register level only --
this tests whether the register column alone (without a lifecycle gate) satisfies C-30,
which was already established in R13 V-04.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task, including
each role's domain boundary. It is a standalone structural artifact -- auditable
without executing the protocol. A row with a blank cell is a structural gap. No role
may begin unless its Requires entry is present in the output above.

| Role      | Requires                                                                    | Produces                | Domain (ONLY)                                                                                                                                                                                              | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-32) with annotation-field column and YES-only gate    | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                                                   | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                 | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                      | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                      | Re-scoring, re-auditing                                                                   |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE
    present above. Both tokens must appear simultaneously as a strict conjunction --
    holding either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone
    does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.
  - A blank cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER
    is a structural violation blocking JUDGE STANDARD COMPLETE.
  - A NO cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER also
    blocks JUDGE STANDARD COMPLETE. Only YES is a passing cell value.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-32), produce a Judge standard entry with three required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. It must be expressed as a named label followed by the two mechanism poles
separated by "vs" -- not embedded in prose.

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation naming the
specific output the example was drawn from. The "ACCEPTABLE source annotated" column
in the CONSOLIDATED PRODUCTION-TIME REGISTER records whether this annotation is present
for each entry. Populate this column as you write each entry:

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output it was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement
      not tied to a specific output by name.
    - A blank cell is a structural violation. A NO cell also blocks JUDGE STANDARD
      COMPLETE under the YES-only gate rule. Only YES is a passing cell value.

Before issuing JUDGE STANDARD COMPLETE, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER confirming all 32 criteria are covered. This register is the single
inspectable artifact for all JUDGE production-time obligations. No production-time
obligation in this design is tracked outside this register.

CONSOLIDATED PRODUCTION-TIME REGISTER

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns (Pair present, Separating property declared, ACCEPTABLE source
annotated). A blank cell in any column is a structural violation equivalent to a
missing row and blocks JUDGE STANDARD COMPLETE.

YES-only gate: A NO cell in any required column also blocks JUDGE STANDARD COMPLETE.
Blank = structural incompleteness. NO = obligation acknowledged but not satisfied.
Both block. Only YES = obligation met = passing cell value.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-02      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-03      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-04      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-05      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-06      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-07      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-08      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-09      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-10      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-11      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-12      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-13      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-14      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-15      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-16      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-17      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-18      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-19      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-20      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-21      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-22      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-23      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-24      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-25      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-26      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-27      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-28      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-29      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-30      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-31      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-32      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

A blank cell or a NO cell in any column blocks JUDGE STANDARD COMPLETE. Every row must
show YES in all three columns before JUDGE STANDARD COMPLETE may be issued.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table format:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict           | Evidence                           | Present_mechanism | Absent_mechanism |
  |------|-----------|--------|-------------------|------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [evidence grounded in this output] | --                | --               |

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present in this output
    and prevented FAIL. For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent in this output and
    prevented PASS. For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a
    structural violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or
  Absent_mechanism cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 25 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic and are Present_mechanism
and Absent_mechanism columns non-empty on PARTIAL rows? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per output:

AUDIT A -- Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B -- Diagnostic column presence: Applies to PARTIAL verdicts only. Verify that:
  (i)  Present_mechanism cell is non-empty (contains named content, not -- or blank)
  (ii) Absent_mechanism cell is non-empty (contains named content, not -- or blank)
This audit verifies column non-emptiness only. Whether the content names a specific
structural property is the CONFIRMER's domain.
Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge domain),
scoring verdicts (Analyst domain).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer asks one question per PARTIAL column cell: does this text identify a
real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |
  |-----------|---------------------------------------|-----------|---------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words of Present content]   | YES / NO  | [first 15 words of Absent content]    | YES / NO  | CONFIRMED/CHALLENGED |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap
  NO  -- uses a criterion label, generic quality phrase, or restates the verdict

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens must appear simultaneously as a strict conjunction -- holding
either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone does not
satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference -- name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-05 -- Full stack R14: All mechanisms, /25 formula, 32-row register

**Variation axis**: AA (SYNTHESIS prohibition complement) + YG (YES-only gate rule in
gate rules AND in lifecycle check) + CR (consolidated 5-column register) + LA
(ANNOTATION COVERAGE CONFIRMED lifecycle gate) + REGISTER COMPLETENESS CONFIRMED
lifecycle gate (now checks both blank AND NO as blocking) + FA25 (FORMULA ANCHOR
N_aspirational=25 declared in manifest and Analyst output, verified by Verifier Audit D)
+ formula /25 + 32-row register. Maximum structural footprint for R14.

**Hypothesis**: Full stack closes all R14 criteria simultaneously. C-31 is closed at
two points: the gate rules name NO as blocking ("A NO cell also blocks"), and the
REGISTER COMPLETENESS CHECK lifecycle step checks that "all cells contain YES (not NO
or blank)" before issuing REGISTER COMPLETENESS CONFIRMED. Two orthogonal enforcement
points for C-31: gate-rule axis (static declaration) and lifecycle-gate axis (dynamic
check). C-32 is closed by the consolidated 5-column register labeled as the single
source of truth. Formula anchor /25 is declared in the manifest (making a wrong-divisor
error a manifest gap) and verified by Verifier Audit D (making it a post-write
structural check). V-05 achieves maximum redundancy across all criteria escalation
chains.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task, including
each role's domain boundary. It is a standalone structural artifact -- auditable
without executing the protocol. A row with a blank cell is a structural gap. No role
may begin unless its Requires entry is present in the output above.

Formula parameter declared here as a manifest-level structural artifact:
  N_aspirational = 25   (current rubric v14 value; Analyst must use /25 denominator)
  A formula using any other N_aspirational denominator is a manifest violation.

| Role      | Requires                                                                    | Produces                                                                                         | Domain (ONLY)                                                                                                                                                                                                                                                            | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | REGISTER COMPLETENESS CONFIRMED, ANNOTATION COVERAGE CONFIRMED, JUDGE STANDARD COMPLETE         | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-32) with annotation-field column, YES-only gate, no-skip rule, and two lifecycle sub-gates                          | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | FORMULA ANCHOR N_aspirational=25 DECLARED, ANALYST COMPLETE                                     | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns; FORMULA ANCHOR declaration (N_aspirational=25, /25 denominator)                                                                                                | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE                                                                          | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows; FORMULA ANCHOR presence and /25 denominator match (Audit D)                                                                                  | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE                                                                            | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                                    | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)                                                                                | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                                    | Re-scoring, re-auditing                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE cannot be issued without REGISTER COMPLETENESS CONFIRMED
    and ANNOTATION COVERAGE CONFIRMED both present above it. Both are required
    intermediate sub-gates within the JUDGE phase; REGISTER COMPLETENESS CONFIRMED
    must appear before ANNOTATION COVERAGE CONFIRMED.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE
    present above. Both tokens must appear simultaneously as a strict conjunction --
    holding either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone
    does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.
  - A blank cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER
    is a structural violation blocking REGISTER COMPLETENESS CONFIRMED and JUDGE
    STANDARD COMPLETE.
  - A NO cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER also
    blocks REGISTER COMPLETENESS CONFIRMED and JUDGE STANDARD COMPLETE. Only YES is a
    passing cell value.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-32), produce a Judge standard entry with three required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. It must be expressed as a named label followed by the two mechanism poles
separated by "vs" -- not embedded in prose.

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation naming the
specific output the example was drawn from. The "ACCEPTABLE source annotated" column
records whether this annotation is present for each entry. Populate this column as
you write each entry:

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output it was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement.
    - A blank cell is a structural violation. A NO cell also blocks under the YES-only
      gate rule. Only YES is a passing value.

After writing all 32 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER, then execute the LIFECYCLE COMPLETENESS SEQUENCE.

CONSOLIDATED PRODUCTION-TIME REGISTER

This is the single source of truth for all JUDGE production-time obligations. No
production-time obligation in this design is tracked outside this register. All three
obligations -- pair coverage (C-25/C-23), separating property (C-22), and source
annotation (C-26/C-30) -- are columns in this one artifact. A single incomplete row
reveals all unmet obligations simultaneously.

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns. A blank cell is a structural violation equivalent to a missing row.

YES-only gate: A NO cell in any required column is a blocking value equivalent to a
blank cell. Blank = structural incompleteness. NO = obligation acknowledged but unmet.
Both block REGISTER COMPLETENESS CONFIRMED and JUDGE STANDARD COMPLETE. Only YES
passes.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-02      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-03      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-04      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-05      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-06      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-07      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-08      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-09      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-10      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-11      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-12      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-13      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-14      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-15      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-16      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-17      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-18      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-19      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-20      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-21      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-22      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-23      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-24      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-25      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-26      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-27      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-28      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-29      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-30      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-31      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-32      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

LIFECYCLE COMPLETENESS SEQUENCE (execute in order; each gate blocks the next):

Step 1 -- REGISTER COMPLETENESS CHECK:
  (i)  All 32 rows present (no criterion row missing): YES / NO
  (ii) All three columns fully populated in every row (no blank cells): YES / NO
  (iii) All populated cells contain YES (no NO cells in any row): YES / NO
  All three checks must pass. A blank cell fails check (ii). A NO cell fails check (iii).
  Both blank and NO are blocking. Only YES is a passing cell value.
  If all three checks pass: issue REGISTER COMPLETENESS CONFIRMED and proceed to Step 2.
  If any check fails: identify and correct each gap, re-run Step 1.

REGISTER COMPLETENESS CONFIRMED

Step 2 -- ANNOTATION COVERAGE CHECK (may begin only after REGISTER COMPLETENESS CONFIRMED):
  Cross-check the register against the JUDGE STANDARD entries:
  For every row where "ACCEPTABLE source annotated" shows YES: verify the corresponding
  ACCEPTABLE entry in the JUDGE STANDARD above carries the "from [Output-N]:" prefix.
  For every row where the column shows NO: this row failed check (iii) and blocked Step 1.
  All 32 "ACCEPTABLE source annotated" values must be YES for this gate to pass.
  If all 32 annotation fields verify: issue ANNOTATION COVERAGE CONFIRMED.
  If any mismatch found: add missing annotation, update register, re-run Step 1.

ANNOTATION COVERAGE CONFIRMED

JUDGE STANDARD COMPLETE may not be issued until REGISTER COMPLETENESS CONFIRMED
and ANNOTATION COVERAGE CONFIRMED both appear above.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns; FORMULA ANCHOR declaration (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

Before scoring, declare the formula anchor as a named structural artifact:

  FORMULA ANCHOR
  N_essential = 4
  N_recommended = 3
  N_aspirational = 25   (rubric v14 value, per manifest declaration)
  Formula: composite = (E/4*60) + (R/3*30) + (A/25*10)
  Any deviation from /25 in the aspirational denominator is a formula error.

FORMULA ANCHOR N_aspirational=25 DECLARED

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table format:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict           | Evidence                           | Present_mechanism | Absent_mechanism |
  |------|-----------|--------|-------------------|------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [evidence grounded in this output] | --                | --               |

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present in this output
    and prevented FAIL. For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent in this output and
    prevented PASS. For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a
    structural violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or
  Absent_mechanism cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 25 * 10)    <- must match FORMULA ANCHOR above
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic, are Present_mechanism and
Absent_mechanism columns non-empty on PARTIAL rows, and does the FORMULA ANCHOR
declaration match /25? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs three independent audits per output (Audit A and B) plus one
global audit (Audit D):

AUDIT A -- Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B -- Diagnostic column presence: Applies to PARTIAL verdicts only. Verify that:
  (i)  Present_mechanism cell is non-empty (contains named content, not -- or blank)
  (ii) Absent_mechanism cell is non-empty (contains named content, not -- or blank)
This audit verifies column non-emptiness only. Whether the content names a specific
structural property is the CONFIRMER's domain.
Mark n/a for PASS and FAIL verdicts.

AUDIT D -- Formula anchor verification (global, runs once after all outputs scored):
  (i)  FORMULA ANCHOR N_aspirational=25 DECLARED token is present in the Analyst output.
  (ii) The formula used in every composite computation shows /25 in the aspirational
       denominator. A formula showing /23, /21, or any other value is a formula error.
  Report: FORMULA ANCHOR VERIFIED if both checks pass, or FLAG: Formula error if not.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

After all per-output audits complete, run Audit D and report result.

When all rows are ACCEPTED across all N outputs AND FORMULA ANCHOR VERIFIED:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge domain),
scoring verdicts (Analyst domain).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer asks one question per PARTIAL column cell: does this text identify a
real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |
  |-----------|---------------------------------------|-----------|---------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words of Present content]   | YES / NO  | [first 15 words of Absent content]    | YES / NO  | CONFIRMED/CHALLENGED |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap:
        e.g., "explicit gate token ANALYST COMPLETE coupling Analyst to Verifier",
              "no post-write verification step independent of the writer",
              "named Produces/Requires manifest table with DOMAIN and CANNOT CHECK entries"
  NO  -- uses a criterion label, a generic quality phrase, or restates the verdict:
        e.g., "some structure is present", "mechanism is partially addressed",
              "does not fully satisfy the criterion", "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens must appear simultaneously as a strict conjunction -- holding
either token alone does not satisfy this gate. CONFIRMATION COMPLETE alone does not
satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference -- name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```
