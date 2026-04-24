# Quest Score -- Round 13 Variations
**Skill**: quest-score
**Rubric**: v13 (N_essential=4, N_recommended=3, N_aspirational=23)
**Date**: 2026-03-15
**Round**: 13

---

## Design logic

### Unachieved ceiling entering R13

R12 was scored against rubric v12 (N_aspirational=21). Rubric v13 adds C-29
(SYNTHESIS gate explicit single-token prohibition complement) and C-30
(Per-entry annotation enforcement at JUDGE production time via register field).

| Criterion | R12 status | Gap analysis |
|-----------|------------|--------------|
| C-29 | DERIVED from R12 | R12 V-01 SYNTHESIS gate states "holding either token alone does not satisfy this gate" -- the explicit prohibition complement is attached to the BOTH...AND conjunction in the gate instruction, closing the interpretive bypass path: a scorer who holds one token cannot argue that individually satisfying a per-token requirement constitutes gate compliance. R12 V-02 used parenthetical "(both required independently)" with no BOTH...AND connector and no prohibition. R12 V-03 through V-05 carried BOTH...AND without a prohibition clause. R12 V-01 satisfies C-29 under v13 scoring; R12 V-02 through V-05 fail or partially satisfy it. |
| C-30 | UNIVERSAL PARTIAL in R12 | All five R12 variations declared grounding intent in a JUDGE role preamble ("drawn from provided inputs, not invented") but none included an annotation-field column in the production-time PAIR COVERAGE REGISTER. C-30 requires the annotation obligation to be structurally enforced at write time -- a named register field per row that must be populated before the row can be marked complete. A preamble declares intent; it cannot prevent an annotation from being omitted during writing. A post-write audit detects omissions reactively. Only a production-time register field makes annotation omission a structural gap detectable by inspection before JUDGE STANDARD COMPLETE is issued. |

### Formula change

N_aspirational increases from 21 to 23. All variations must update the composite
formula from `aspirational_pass / 21 * 10` to `aspirational_pass / 23 * 10`. A
variation using the old divisor produces systematically incorrect scores -- a C-02
FAIL and a C-07 error for every output. The PAIR COVERAGE REGISTER also expands from
28 rows (C-01 through C-28) to 30 rows (C-01 through C-30). Both the formula update
and the register row expansion are required infrastructure for every R13 variation;
they are not themselves variation axes.

### New mechanism gaps

**For C-29 (SYNTHESIS single-token prohibition complement):**
The prohibition must appear in the SYNTHESIS gate instruction itself -- attached to
the BOTH...AND conjunction in the same gate condition or immediately following it.
"Holding either token alone does not satisfy this gate" is the reference prohibition
form from R12 V-01. A gate that has BOTH...AND but no prohibition satisfies C-27 and
fails C-29 -- the positive conjunction form (both tokens must appear simultaneously)
does not exclude the interpretive reading that holding one token individually satisfies
that token's requirement. The prohibition changes the gate from a positive requirement
to a double-closure: both tokens must appear AND holding any subset is explicitly
named as insufficient.

**For C-30 (annotation register field):**
The annotation-field column must be a structural slot in the PAIR COVERAGE REGISTER --
a column with YES/NO values, identical in enforcement mechanism to the existing "Pair
present" and "Separating property declared" columns. A behavioral instruction to
annotate examples (e.g., "annotate with 'from [Output-N]:'") does not qualify because
it relies on the writer's own compliance check. A post-write annotation audit detects
omissions but cannot prevent them. Only a production-time register field -- established
before ACCEPTABLE examples are written -- makes annotation omission a structural gap
detectable by inspection at any workflow stage. The column must be part of the same
register that C-25 pre-structures, so that a missing annotation value is as visible as
a missing pair entry.

### New axes for R13

| Axis | Label | Mechanism |
|------|-------|-----------|
| AA | SYNTHESIS prohibition complement | SYNTHESIS gate adds explicit prohibition: "holding either token alone does not satisfy this gate" -- closes C-29 interpretive bypass alongside the C-27 BOTH...AND conjunction |
| AD | Annotation register field | PAIR COVERAGE REGISTER adds "ACCEPTABLE source annotated" column (YES/NO) -- enforces per-entry source annotation as a production-time structural obligation; blank or NO blocks JUDGE STANDARD COMPLETE, closing C-30 |
| LA | Lifecycle annotation gate | JUDGE emits ANNOTATION COVERAGE CONFIRMED before JUDGE STANDARD COMPLETE; annotation coverage enforced as a named lifecycle milestone that blocks JUDGE STANDARD COMPLETE unless every ACCEPTABLE entry carries its source annotation |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (AA)**: Prohibition complement only. 30-row register (4 columns); no
  annotation-field column (behavioral instruction: annotate with "from [Output-N]:"
  prefix). BOTH...AND gate + explicit prohibition clause. Formula /23.
  Predicts: C-29 PASS, C-30 PARTIAL (behavioral instruction declares grounding intent
  but no register field makes annotation omission a structural gap detectable at write
  time; intent vs enforcement distinction is identical to C-23/C-25 and C-26/C-30).

- **V-02 (AD)**: Annotation register field only. 30-row register (5 columns) with
  "ACCEPTABLE source annotated" YES/NO column. SYNTHESIS gate uses BOTH...AND without
  any prohibition clause. Formula /23.
  Predicts: C-30 PASS, C-29 PARTIAL (BOTH...AND satisfies C-27; the absence of a
  prohibition statement leaves the interpretive bypass open -- a scorer holding one
  token can still argue that the per-token requirement was individually met, because
  nothing in the gate instruction names subset satisfaction as explicitly insufficient).

- **V-03 (LA)**: Lifecycle annotation gate. JUDGE emits ANNOTATION COVERAGE CONFIRMED
  as a named intermediate gate before JUDGE STANDARD COMPLETE; the gate requires every
  ACCEPTABLE entry to carry a "from [Output-N]:" prefix annotation. BOTH...AND +
  prohibition complement inherited from R12 V-01 best performer. No annotation-field
  column in register header (4 columns). Formula /23.
  Predicts: C-29 PASS (inherited), C-30 PASS (lifecycle gate enforces annotation
  coverage as a named structural precondition before JUDGE STANDARD COMPLETE --
  equivalent structural role to R12 V-03's REGISTER COMPLETENESS CONFIRMED for C-28;
  annotation omission is a structural gap blocking ANNOTATION COVERAGE CONFIRMED, which
  blocks JUDGE STANDARD COMPLETE, making omission detectable by token inspection).

### Combination selection rationale

- **V-04 (AA+AD)**: Prohibition complement + annotation register field. C-29 closed by
  the prohibition statement in the gate instruction; C-30 closed by the annotation-field
  column in the register. No lifecycle annotation gate. Tests whether the orthogonal
  gate-level (AA) and register-level (AD) mechanisms are sufficient for full C-29+C-30
  PASS without the lifecycle enforcement layer.

- **V-05 (AA+AD+LA full stack)**: All three mechanisms plus formula anchor for
  N_aspirational=23. JUDGE emits ANNOTATION COVERAGE CONFIRMED before JUDGE STANDARD
  COMPLETE. Register includes annotation-field column. SYNTHESIS gate has BOTH...AND +
  prohibition. Formula anchor declared before composite computation. Verifier gains
  Audit D for formula anchor verification. Maximum structural footprint for R13.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| SYNTHESIS prohibition complement (AA) | YES | NO | YES (inherited) | YES | YES |
| Annotation register field (AD) | NO (behavioral) | YES | NO (behavioral) | YES | YES |
| ANNOTATION COVERAGE CONFIRMED lifecycle gate (LA) | NO | NO | YES | NO | YES |
| Formula anchor N_aspirational=23 | NO | NO | NO | NO | YES |
| Register rows | 30 | 30 | 30 | 30 | 30 |
| Register columns | 4 | 5 | 4 | 5 | 5 |
| Formula divisor | /23 | /23 | /23 | /23 | /23 |

---

## V-01 -- Axis AA: SYNTHESIS prohibition complement

**Variation axis**: SYNTHESIS gate -- explicit single-token prohibition complement
attached to the BOTH...AND conjunction, closing the interpretive bypass path for C-29.

**Hypothesis**: R12 V-01 carried the prohibition clause ("holding either token alone
does not satisfy this gate") and is expected to satisfy C-29 under v13 scoring. Other
R12 variations lacked it. V-01 isolates this mechanism: the SYNTHESIS gate adds the
explicit prohibition alongside the BOTH...AND conjunction. The annotation obligation
for ACCEPTABLE examples is expressed behaviorally ("from [Output-N]:" prefix
instruction in JUDGE role text) with no register column -- leaving C-30 at PARTIAL.
The distinction between a behavioral annotation mandate and a structural register field
is the same structural gap that C-23/C-25 and C-26/C-30 escalation chains name.

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
| JUDGE     | (none)                                                                      | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-30)   | Scoring verdicts, format compliance, diagnostic content quality                           |
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
C-30), produce a Judge standard entry with three required components:

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
all 30 criteria are covered. This register is a standalone structural artifact -- its
absence or any missing row blocks JUDGE STANDARD COMPLETE.

PAIR COVERAGE REGISTER

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

A "NO" in any cell blocks JUDGE STANDARD COMPLETE. No cell in any row may be left
blank -- write YES or NO for every cell. JUDGE STANDARD COMPLETE may not be issued
until all 30 rows show YES in both columns.

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
              + (aspirational_pass / 23 * 10)
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

## V-02 -- Axis AD: Annotation register field

**Variation axis**: Output format -- the PAIR COVERAGE REGISTER adds a fifth column,
"ACCEPTABLE source annotated" (YES/NO), making per-entry source annotation a
production-time structural obligation. A blank or NO value in this column blocks
JUDGE STANDARD COMPLETE identically to a missing pair or absent separating property.

**Hypothesis**: R12 registered grounding intent behaviorally (preamble instruction)
without a structural slot per row. C-30 names the gap: only a production-time register
field makes annotation omission detectable by inspection during writing, not after.
V-02 introduces this field -- a fifth YES/NO column that must be populated before any
row is considered complete. The SYNTHESIS gate uses BOTH...AND conjunction without a
prohibition clause, to isolate whether the register-level mechanism alone closes C-30
while C-29 remains PARTIAL. A scorer holding one token can still argue that the per-
token requirement was individually met; the absence of a prohibition statement leaves
this interpretive route open.

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

| Role      | Requires                                                  | Produces                | Domain (ONLY)                                                                                                                                                            | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                    | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-30) with annotation-field column  | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                   | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                 | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                          | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                               | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                   | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                    | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE    | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                    | Re-scoring, re-auditing                                                                   |
|           | (both required independently)                             |                         |                                                                                                                                                                          |                                                                                           |

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
C-30), produce a Judge standard entry with three required components:

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
in the PAIR COVERAGE REGISTER records whether this annotation is present for each
entry. Populate this column as you write:

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output the example was drawn from.
    - Enter NO if the ACCEPTABLE entry lacks this annotation or carries only a general
      grounding statement not tied to a specific output.
    - A blank cell in this column is a structural violation blocking JUDGE STANDARD
      COMPLETE under the no-skip column rule below.

Before issuing JUDGE STANDARD COMPLETE, produce the PAIR COVERAGE REGISTER confirming
all 30 criteria are covered.

PAIR COVERAGE REGISTER

No-skip column rule: every cell in every row must contain YES or NO. A blank cell --
one with no value, not even NO -- is a structural violation equivalent to a missing
row and blocks JUDGE STANDARD COMPLETE. Only YES and NO are accepted values. Any row
with a blank cell in any required column (Pair present, Separating property declared,
or ACCEPTABLE source annotated) is treated as an incomplete row and blocks JUDGE
STANDARD COMPLETE identically to a row with a NO cell.

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

A "NO" in any cell blocks JUDGE STANDARD COMPLETE. A blank cell also blocks JUDGE
STANDARD COMPLETE under the no-skip column rule. Every row must show YES in all three
columns before JUDGE STANDARD COMPLETE may be issued.

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
              + (aspirational_pass / 23 * 10)
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

## V-03 -- Axis LA: Lifecycle annotation gate (ANNOTATION COVERAGE CONFIRMED)

**Variation axis**: Lifecycle emphasis -- the JUDGE role emits two sequential named
intermediate gates before JUDGE STANDARD COMPLETE: REGISTER COMPLETENESS CONFIRMED
(row and cell coverage, inherited from R12 V-03) and ANNOTATION COVERAGE CONFIRMED
(every ACCEPTABLE entry carries a "from [Output-N]:" prefix annotation). Annotation
coverage is enforced as a named lifecycle milestone, not as a register-header column.
BOTH...AND + prohibition complement inherited from R12 V-01.

**Hypothesis**: R12 showed that REGISTER COMPLETENESS CONFIRMED closes C-28 (cell-
completeness) by making an incomplete register a detectable structural gap at the
lifecycle gate. The same mechanism applied to annotation coverage closes C-30: an
ACCEPTABLE entry without its "from [Output-N]:" prefix is an annotation gap that
blocks ANNOTATION COVERAGE CONFIRMED, which blocks JUDGE STANDARD COMPLETE. Annotation
omission becomes a structural gap detectable by token inspection -- not a behavioral
lapse caught only by post-write audit. The register has 4 columns (no AD annotation-
field column) to isolate whether the lifecycle gate alone satisfies C-30 without the
register-field mechanism, and whether C-30 distinguishes the two enforcement paths.

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

| Role      | Requires                                                                    | Produces                                                              | Domain (ONLY)                                                                                                                                                           | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | REGISTER COMPLETENESS CONFIRMED, ANNOTATION COVERAGE CONFIRMED, JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-30) + two lifecycle sub-gates | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | ANALYST COMPLETE                                                      | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE                                               | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                              | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE                                                 | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                   | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)                                                     | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                   | Re-scoring, re-auditing                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE cannot be issued without REGISTER COMPLETENESS CONFIRMED
    and ANNOTATION COVERAGE CONFIRMED both present above it. Both are required
    intermediate sub-gates within the JUDGE phase; their order is fixed (REGISTER
    COMPLETENESS CONFIRMED must appear before ANNOTATION COVERAGE CONFIRMED).
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
C-30), produce a Judge standard entry with three required components:

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

After writing all 30 criterion entries, produce the PAIR COVERAGE REGISTER, then
execute the LIFECYCLE COMPLETENESS SEQUENCE before issuing JUDGE STANDARD COMPLETE.

PAIR COVERAGE REGISTER

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

LIFECYCLE COMPLETENESS SEQUENCE (execute in order; each gate blocks the next):

Step 1 -- REGISTER COMPLETENESS CHECK:
  (i)  All 30 rows present (no criterion row missing): YES / NO
  (ii) All cells in every row contain YES or NO (no blank cells): YES / NO
  If both pass: issue REGISTER COMPLETENESS CONFIRMED and proceed to Step 2.
  If either fails: correct the gap, re-run Step 1. Do not proceed until confirmed.

REGISTER COMPLETENESS CONFIRMED

Step 2 -- ANNOTATION COVERAGE CHECK (may begin only after REGISTER COMPLETENESS CONFIRMED):
  For every ACCEPTABLE entry written in the JUDGE STANDARD above, verify that it
  carries an explicit "from [Output-N]:" prefix annotation naming the specific scored
  output the example was drawn from. An ACCEPTABLE entry without this prefix is an
  annotation gap that blocks this gate.
  (i)  Every ACCEPTABLE entry carries a "from [Output-N]:" prefix: YES / NO
  If YES: issue ANNOTATION COVERAGE CONFIRMED and proceed to JUDGE STANDARD COMPLETE.
  If NO: list each missing annotation by criterion ID, add the annotation, re-run
         Step 2. Do not issue ANNOTATION COVERAGE CONFIRMED until all are present.

ANNOTATION COVERAGE CONFIRMED

JUDGE STANDARD COMPLETE may not be issued until REGISTER COMPLETENESS CONFIRMED
and ANNOTATION COVERAGE CONFIRMED both appear above.

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
              + (aspirational_pass / 23 * 10)
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

## V-04 -- Axes AA+AD: Prohibition complement + Annotation register field

**Variation axis**: AA (SYNTHESIS prohibition complement) + AD (annotation register
field). Both C-29 and C-30 addressed by orthogonal mechanisms: the gate-level
prohibition closes the interpretive bypass (C-29); the register-level annotation
column closes the production-time annotation gap (C-30). No lifecycle annotation gate.

**Hypothesis**: V-01 predicts C-29 PASS and C-30 PARTIAL. V-02 predicts C-30 PASS and
C-29 PARTIAL. V-04 combines both: the prohibition clause makes SYNTHESIS double-closure-
complete for the token-conjunction requirement, and the annotation-field register column
makes per-entry annotation omission a structural gap detectable by inspection at write
time. Together they should produce C-29 PASS + C-30 PASS without the lifecycle
annotation gate. This tests whether the orthogonal gate-level and register-level
mechanisms close both new criteria without requiring the ANNOTATION COVERAGE CONFIRMED
lifecycle layer.

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

| Role      | Requires                                                                    | Produces                | Domain (ONLY)                                                                                                                                                                              | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-30) with annotation-field column and no-skip rule   | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | ANALYST COMPLETE        | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns                                                                                   | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                 | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE   | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                      | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)       | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                      | Re-scoring, re-auditing                                                                   |

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
C-30), produce a Judge standard entry with three required components:

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
in the PAIR COVERAGE REGISTER records whether this annotation is present for each
entry. Populate this column as you write each entry:

  "ACCEPTABLE source annotated" column:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output it was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement
      not tied to a specific output by name.
    - A blank cell in this column is a structural violation blocking JUDGE STANDARD
      COMPLETE under the no-skip column rule.

Before issuing JUDGE STANDARD COMPLETE, produce the PAIR COVERAGE REGISTER confirming
all 30 criteria are covered.

PAIR COVERAGE REGISTER

No-skip column rule: every cell in every row must contain YES or NO. A blank cell
in any required column (Pair present, Separating property declared, or ACCEPTABLE
source annotated) is a structural violation equivalent to a missing row and blocks
JUDGE STANDARD COMPLETE. Only YES and NO are accepted values.

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

A "NO" in any cell blocks JUDGE STANDARD COMPLETE. A blank cell also blocks JUDGE
STANDARD COMPLETE under the no-skip column rule. Every row must show YES in all three
columns before JUDGE STANDARD COMPLETE may be issued.

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
              + (aspirational_pass / 23 * 10)
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

## V-05 -- Axes AA+AD+LA: Full stack + formula anchor

**Variation axis**: AA (SYNTHESIS prohibition complement) + AD (annotation register
field) + LA (ANNOTATION COVERAGE CONFIRMED lifecycle gate) + formula anchor for
N_aspirational=23. Maximum structural footprint for R13.

**Hypothesis**: V-04 achieves C-29 PASS and C-30 PASS through the orthogonal gate-
level and register-level mechanisms. V-05 adds a third enforcement layer for C-30:
the ANNOTATION COVERAGE CONFIRMED sub-gate makes annotation coverage a named lifecycle
milestone independently of the register column. The AD register column enforces
annotation at write time (per-row structural slot); the LA lifecycle gate confirms
completeness before JUDGE STANDARD COMPLETE (batch-level structural checkpoint). Two
structurally independent C-30 mechanisms cover different bypass paths: the register
column prevents individual row omissions at write time; the lifecycle gate catches any
annotation gap that slipped past the register. The formula anchor declares
N_aspirational=23 as a named structural artifact before composite computation, making
a wrong-divisor error detectable by register inspection. Verifier Audit D checks the
anchor declaration against the actual formula divisor.

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

| Role      | Requires                                                                    | Produces                                                                         | Domain (ONLY)                                                                                                                                                                                                 | Cannot Check                                                                              |
|-----------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                      | REGISTER COMPLETENESS CONFIRMED, ANNOTATION COVERAGE CONFIRMED, JUDGE STANDARD COMPLETE | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + PAIR COVERAGE REGISTER (C-01 through C-30) with annotation-field column, no-skip rule, and two lifecycle sub-gates | Scoring verdicts, format compliance, diagnostic content quality                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                     | ANALYST COMPLETE                                                                 | Per-criterion scoring; evidence cells; composite; golden; Present_mechanism and Absent_mechanism columns; FORMULA ANCHOR N_aspirational=23 declaration                                                        | Evidence quality standards (Judge domain), format auditing (Verifier domain)              |
| VERIFIER  | ANALYST COMPLETE                                                            | VERIFIER AUDIT COMPLETE                                                          | Format presence: evidence cell non-genericity; PARTIAL column non-emptiness; FORMULA ANCHOR presence and divisor match                                                                                        | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                     | CONFIRMATION COMPLETE                                                            | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                         | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain) |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE (strict conjunction) | (terminal output)                                                                | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                         | Re-scoring, re-auditing                                                                   |

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

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-30), produce a Judge standard entry with three required components:

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
you write:

  "ACCEPTABLE source annotated" column:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix
      annotation naming the specific scored output it was drawn from.
    - Enter NO if the annotation is absent or is only a general grounding statement.
    - A blank cell is a structural violation blocking JUDGE STANDARD COMPLETE under
      the no-skip column rule.

After writing all 30 criterion entries, produce the PAIR COVERAGE REGISTER, then
execute the LIFECYCLE COMPLETENESS SEQUENCE.

PAIR COVERAGE REGISTER

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns (Pair present, Separating property declared, ACCEPTABLE source
annotated). A blank cell in any column is a structural violation equivalent to a
missing row and blocks REGISTER COMPLETENESS CONFIRMED and JUDGE STANDARD COMPLETE.

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

LIFECYCLE COMPLETENESS SEQUENCE (execute in order; each gate blocks the next):

Step 1 -- REGISTER COMPLETENESS CHECK:
  (i)  All 30 rows present (no criterion row missing): YES / NO
  (ii) All three YES/NO columns fully populated in every row (no blank cells): YES / NO
  The no-skip column rule applies to all three columns -- a blank cell in any column
  is a structural violation equivalent to a missing row.
  If both checks pass: issue REGISTER COMPLETENESS CONFIRMED, proceed to Step 2.
  If either fails: correct the gap, re-run Step 1.

REGISTER COMPLETENESS CONFIRMED

Step 2 -- ANNOTATION COVERAGE CHECK (may begin only after REGISTER COMPLETENESS CONFIRMED):
  Cross-check the register against the JUDGE STANDARD entries:
  For every row where "ACCEPTABLE source annotated" is YES: verify the corresponding
  ACCEPTABLE entry in the JUDGE STANDARD carries the "from [Output-N]:" prefix.
  For every row where "ACCEPTABLE source annotated" is NO: this row blocks this gate.
  All 30 rows must show YES in the "ACCEPTABLE source annotated" column for this gate
  to pass.
  If all 30 annotation fields verify: issue ANNOTATION COVERAGE CONFIRMED.
  If any fail: add the missing annotation, update the register, re-run Step 2.

ANNOTATION COVERAGE CONFIRMED

JUDGE STANDARD COMPLETE may not be issued until REGISTER COMPLETENESS CONFIRMED
and ANNOTATION COVERAGE CONFIRMED both appear above.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns; FORMULA ANCHOR declaration (see manifest).
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

  N_aspirational = 23  -- FORMULA ANCHOR: v13 rubric denominator. Declare before
                          composite computation. A computation using any other value
                          fails C-02. This anchor makes a wrong-divisor error
                          detectable by Verifier Audit D without re-computing.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 23 * 10)  -- divisor must match FORMULA ANCHOR
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- are evidence cells non-generic, are Present_mechanism and
Absent_mechanism columns non-empty on PARTIAL rows, and does the FORMULA ANCHOR match
the actual formula divisor? (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

The Verifier performs three independent audits per output:

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

AUDIT D -- Formula anchor verification: Confirm that:
  (i)  N_aspirational = 23 was declared as a named FORMULA ANCHOR before any
       composite computation in the Analyst output.
  (ii) The divisor used in each output's composite formula is exactly 23.
  If the anchor is absent or any formula uses a different divisor: FLAG as REJECTED.
  This audit applies once across all outputs, not per-output.

Produce a per-output combined audit table:

  Output: [output identifier] -- Post-write Evidence, Diagnostic Column, and Formula Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |------|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | PASS    | FAIL    | REJECTED |

  Status = ACCEPTED only if all applicable audits pass.

Formula anchor result (applies across all outputs):
  AUDIT D -- FORMULA ANCHOR N_aspirational=23: [PASS if anchor declared and divisor
             matches; FAIL with specific reason if not]

For every REJECTED row or AUDIT D FAIL:
  FLAG: [output ID or "all"] / [criterion ID or "formula"] -- Audit [A/B/D]: [reason]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED and AUDIT D passes:
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
