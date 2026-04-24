# Quest Score — Round 5 Variations
**Skill**: quest-score
**Rubric**: v5 (N_essential=4, N_recommended=3, N_aspirational=11)
**Date**: 2026-03-15
**Round**: 5

---

## Design logic

### Unachieved ceilings entering R5

R4 was scored against rubric v4 (N_aspirational=9). Rubric v5 adds two new
aspirational criteria extracted from R4 excellence signals:

| Criterion | R4 status | Why unachieved in best R4 variation |
|-----------|-----------|-------------------------------------|
| C-17 | V-05 achieves via template sentence; V-04 FAIL | V-04's Analyst has no two-part PARTIAL diagnostic requirement. V-05 adds a named sentence template mandating both halves. Against v5 rubric, V-05 scores C-17 PASS; V-04 FAIL. |
| C-18 | R4 V-04/V-05 use inline role declarations — compliance depends on strictness of "standalone structural artifact" interpretation | V-04/V-05 declare `ROLE 1: JUDGE  Produces: JUDGE STANDARD COMPLETE` inline in the role structure header. The v5 rubric pass condition requires "a formal table with ROLE N \| Produces \| Requires columns (or equivalent named structure)... not inline behavioral instructions." This ambiguity makes C-18 the primary R5 diagnostic target. |

Key diagnostic question for R5: does the R4 inline declaration format satisfy C-18, or must the Produces/Requires manifest be a structurally distinct standalone table? R5 tests both interpretations.

### New axes for R5

| Axis | Label | Mechanism |
|------|-------|-----------|
| P | Formal manifest table | A standalone `ROLE DEPENDENCY MANIFEST` section with a markdown `\| Role \| Requires \| Produces \|` table declared before any role instructions — separable from role prose, inspectable without executing the protocol. A missing row or blank cell is a structural gap by visual inspection. |
| Q | Verifier-enforced diagnostic audit | The Verifier audit table adds a dedicated "Check C" column that verifies each PARTIAL verdict has a two-part diagnostic covering BOTH halves. Adversarial enforcement: the Verifier (distinct from the Analyst who wrote the diagnostic) rejects incomplete diagnostics. |
| R | Template-enforced PARTIAL rows | The scoring table template itself forces PARTIAL cells to expand into a mandatory two-field block (Present / Absent) before the row can advance. The template is the enforcement — a missing field is a visible structural gap in the output, not a missing sentence. No role required. |

### Single-axis selection rationale

Three single-axis variations (V-01, V-02, V-03):

- **V-01 (P)**: Formal manifest table only. Uses Judge + Analyst + Verifier with gate
  tokens but NO two-part PARTIAL diagnostic. Tests C-18 in isolation. Predicts: C-18
  PASS (standalone table), C-17 FAIL (no mandate for two-part structure).
- **V-02 (Q)**: Verifier-enforced diagnostic audit only. Uses Judge + Analyst + Verifier
  with gate tokens but NO formal standalone manifest table. Tests C-17 via adversarial
  enforcement. Predicts: C-17 PASS (Verifier rejects incomplete diagnostics), C-18
  PARTIAL (inline role declarations, not a formal standalone table).
- **V-03 (R)**: Template-enforced PARTIAL rows, no role separation. Single scorer.
  Tests C-17 via structural template without any external roles. Predicts: C-17 PASS
  (template creates visible gap), C-13/C-15/C-16/C-18 FAIL (no external roles). Low-
  scoring contrast variation — required to establish that structural template alone
  cannot achieve the multi-mechanism aspirational criteria.

### Combination selection rationale

Two combination variations (V-04, V-05):

- **V-04 (P+Q+G+B+M)**: Minimum sufficient combination targeting all 18 criteria.
  P provides the standalone manifest (C-18). Q provides adversarial Verifier enforcement
  of two-part diagnostics (C-17). G+B+M from R4 provides the Judge pre-conditioning
  (C-13, C-15), sequential gates (C-10), and post-write Verifier (C-16). The Verifier
  in this design performs two independent audits: evidence quality (A) and diagnostic
  completeness (B).
- **V-05 (P+R+G+B+M+N)**: Alternative path to all 18 criteria. Replaces Verifier
  diagnostic enforcement (Q) with template PARTIAL rows inside the Analyst (R), and
  adds skeptic framing (N) as a fourth enforcement axis. The Verifier checks diagnostic
  completeness (Check C) but the primary enforcement is structural template, not
  adversarial auditing. Tests whether template-axis C-17 enforcement is equivalent to
  adversarial-axis C-17 enforcement, and whether N adds measurable value on top of
  P+R. Predicts C-17 PASS via two independent mechanisms (R template + C Verifier check).

---

## V-01 — Axis P: Formal dependency manifest as standalone markdown table

**Variation axis**: Output format — a standalone `ROLE DEPENDENCY MANIFEST` markdown
table declared before any role instructions, making the full dependency graph inspectable
as a structural artifact independent of role prose.

**Hypothesis**: A formal markdown table with explicit ROLE / Requires / Produces columns
creates a structurally distinct artifact that satisfies C-18 unambiguously. A missing row
or blank cell is detectable by inspection without executing the protocol — the table is
the gap detector, not the prose. This variation does NOT add a two-part PARTIAL diagnostic
requirement, testing whether C-18 can achieve PASS independently of C-17. Predicts: C-18
PASS (standalone table), C-17 FAIL (no mandate), C-15 PASS (JUDGE STANDARD COMPLETE token
coupling preserved), C-16 PASS (Verifier post-write), C-13 PASS (Verifier distinct from
Analyst), C-14 PASS (role + sequential gate axes).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table is the authoritative dependency graph for this task. It is a
standalone structural artifact — auditable without executing the protocol. No role
may begin unless its Requires entry is present in the output above. A row with a
blank Produces or Requires cell is a structural gap.

| Role      | Requires                  | Produces                  |
|-----------|---------------------------|---------------------------|
| JUDGE     | (none)                    | JUDGE STANDARD COMPLETE   |
| ANALYST   | JUDGE STANDARD COMPLETE   | ANALYST COMPLETE          |
| VERIFIER  | ANALYST COMPLETE          | VERIFIER AUDIT COMPLETE   |
| SYNTHESIS | VERIFIER AUDIT COMPLETE   | (terminal output)         |

---

ROLE 1: JUDGE

Read all N outputs provided as inputs. For each criterion in the rubric, extract
one ACCEPTABLE and one UNACCEPTABLE evidence example from the actual text of the
provided outputs:

  C-[NN]: [criterion name]
  ACCEPTABLE: "[verbatim or close paraphrase from an actual output satisfying this
               criterion]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail — drawn from provided outputs, not invented]"
  Distinction: [one sentence — what specific property makes ACCEPTABLE output-specific
               and UNACCEPTABLE generic or criterion-restating for this criterion]

Cover every criterion in the rubric. Do not fabricate examples outside the provided
outputs.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence specific to this output] |
  ...

  No row may be skipped. No evidence cell may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / N_essential * 60)
              + (recommended_pass / N_recommended * 30)
              + (aspirational_pass / N_aspirational * 10)
              = [result]

    Golden: YES — all essentials PASS; composite >= 80
         |  NO  — [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE — [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above.

Read every evidence cell written by the Analyst. For each output, for each criterion,
compare the evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE pair. Produce
a per-output audit table:

  Output: [output identifier] — Post-write Evidence Audit

  | ID | Evidence cell excerpt (first 15 words) | ACCEPTED / REJECTED | Reason if REJECTED |
  |----|----------------------------------------|--------------------|--------------------|
  | C-01 | [excerpt] | ACCEPTED | |
  ...

Rejection criteria: evidence resembles the Judge's UNACCEPTABLE pattern for this
criterion, OR could apply to a different output with no modification.

For every REJECTED cell:
  FLAG: [output ID] / [criterion ID] — [specific reason the evidence fails the
        Judge's standard for this criterion]

Flagged cells must be rewritten by the Analyst and re-audited. Only flagged cells
are reopened; accepted cells are closed.

When all evidence cells are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference:
          name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
   detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-02 — Axis Q: Verifier-enforced two-part diagnostic audit

**Variation axis**: Role sequence — the Verifier phase expands its audit to cover
diagnostic completeness for PARTIAL verdicts in addition to evidence quality. The
Analyst writes a brief one-line diagnostic for each PARTIAL, but the structural
enforcement comes from the Verifier's adversarial check: a diagnostic that states
only one direction is rejected before VERIFIER AUDIT COMPLETE can be issued.

**Hypothesis**: Adversarial enforcement of two-part diagnostic structure (by a role
distinct from the one that wrote the diagnostic) achieves C-17 via the same structural
family that achieves C-13 — an external entity that cannot exempt its own work from
challenge. This is a different enforcement path from V-05 R4 (which used a named template
sentence at write time) and V-03 R5 (which uses a template block structure). No formal
standalone manifest table is present — inline role declarations only — to isolate axis Q
from P and confirm C-18 requires the table. Predicts: C-17 PASS (Verifier rejects
single-direction diagnostics), C-18 PARTIAL (inline role declarations present but no
standalone table), C-15 PASS, C-16 PASS, C-13 PASS, C-14 PASS.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE STRUCTURE

Three roles complete this task in strict sequence:

  ROLE 1: JUDGE     — defines the evidence quality standard before scoring begins
  ROLE 2: ANALYST   — scores each output using the Judge's standard
  ROLE 3: VERIFIER  — audits the Analyst's evidence quality and diagnostic completeness

Do not begin Role 2 until JUDGE STANDARD COMPLETE appears below.
Do not begin Role 3 until ANALYST COMPLETE appears below.
Do not write synthesis sections until VERIFIER AUDIT COMPLETE appears below.

---

ROLE 1: JUDGE

Read all N outputs provided as inputs. For each criterion in the rubric, extract
one ACCEPTABLE and one UNACCEPTABLE evidence example from the actual text of the
provided outputs:

  C-[NN]: [criterion name]
  ACCEPTABLE: "[verbatim or close paraphrase from an actual output satisfying this
               criterion]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail — drawn from provided outputs, not invented]"
  Distinction: [one sentence — what specific property separates the ACCEPTABLE example
               from the UNACCEPTABLE one for this criterion]

Cover every criterion in the rubric. Do not fabricate examples.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence specific to this output] |
  ...

  No row may be skipped. No evidence cell may be blank.

  For each PARTIAL verdict, add a one-line diagnostic immediately after the table row:
    C-[NN] partial: [what is present in this output that prevented FAIL] /
                    [what is absent that prevented PASS]

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / N_essential * 60)
              + (recommended_pass / N_recommended * 30)
              + (aspirational_pass / N_aspirational * 10)
              = [result]

    Golden: YES — all essentials PASS; composite >= 80
         |  NO  — [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE — [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per row:

AUDIT A — Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B — Diagnostic completeness: Applies to PARTIAL verdicts only. Verify that
the one-line diagnostic present covers BOTH required halves:
  (i)  what is present in the output that prevented FAIL — named specifically
  (ii) what is absent that prevented PASS — named specifically
A diagnostic that states only one direction, repeats the criterion requirement, or
omits either half fails Audit B. Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |----|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS   | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL| [excerpt]                         | PASS    | FAIL    | REJECTED |
  | C-03 | FAIL   | [excerpt]                         | PASS    | n/a     | ACCEPTED |
  ...

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] — Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
   detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-03 — Axis R: Template-enforced PARTIAL two-field rows (no role separation)

**Variation axis**: Output format — the scoring table template itself forces PARTIAL
cells to expand into a mandatory two-field diagnostic block. A PARTIAL row cannot close
until both named fields (Present / Absent) are filled. The template creates a visible
structural gap (empty named field) rather than a missing sentence. No role separation.

**Hypothesis**: A template that structurally prevents advancing past a PARTIAL without
completing both diagnostic fields achieves C-17 via format enforcement rather than role
enforcement. The gap is architectural — the output structure is incomplete if either field
is absent, detectable by inspection. This is the purest single-axis isolation of R: no
roles, no role coupling, no phase gates, no external auditor. It will fail C-13, C-14,
C-15, C-16, C-18 (all role-dependent aspirational criteria) by design. The low score
confirms that template-axis enforcement alone, while sufficient for C-17, cannot achieve
the multi-mechanism aspirational tier — and generates the score spread needed to produce
excellence signals. Predicts: C-17 PASS, C-13/C-15/C-16/C-18 FAIL, C-10/C-11/C-14 FAIL.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

EVIDENCE STANDARD

Before writing any evidence cell, verify that the content is specific to the output
being scored — not generic criterion-language, not a description that applies equally
to any well-designed output. Evidence that could apply to a different output without
modification must be rewritten before it is entered.

---

SCORING PHASE

For each output, produce a scoring record. Every criterion requires a row. No row
may be skipped. No evidence cell may be blank.

For PASS and FAIL verdicts, use the standard row:

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS | [evidence specific to this output] |
  | C-03 | [name] | A | FAIL | [evidence specific to this output] |

For PARTIAL verdicts, the standard row is followed immediately by a mandatory
two-field diagnostic block. Both fields are required before advancing to the next
criterion. This block is not optional — a PARTIAL row without its complete diagnostic
block is a format error:

  | C-[NN] | [name] | [wt] | PARTIAL | [evidence specific to this output] |
  | C-[NN]-DIAG | Present (prevented FAIL): | | | [name the specific structural  |
  |             |                            | | | property present in this output |
  |             |                            | | | that kept the verdict above FAIL] |
  | C-[NN]-DIAG | Absent (prevented PASS):   | | | [name the specific structural  |
  |             |                            | | | property absent from this output |
  |             |                            | | | that kept the verdict below PASS] |

A PARTIAL verdict without a completed two-field block (both rows filled, neither
left blank) is incomplete. The template enforces completeness: a missing DIAG field
is visible as a blank named cell in the output structure.

After all criteria rows (with all PARTIAL diagnostic blocks):

  essential_pass    = [count; PARTIAL = 0.5]
  recommended_pass  = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]

  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
            = [result]

  Golden: YES — all essentials PASS; composite >= 80
       |  NO  — [which essential failed, or composite < 80]

Score all N outputs.

---

LEADERBOARD

Build after all N output scoring records are complete. Rank all outputs by
composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

---

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference]

If all outputs score identically on all criteria:
  "No differentiating excellence signals."

---

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

---

REGRESSION SIGNALS

If prior-round scorecard data is provided, list any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-04 — Axes P+Q+G+B+M: Formal manifest + Verifier diagnostic audit + Judge + gates + Verifier

**Variation axis**: Combination — the minimum sufficient stack to achieve all 18 criteria
including both C-17 and C-18. P (formal manifest table) provides the standalone Produces/
Requires artifact for C-18. Q (Verifier audits diagnostic completeness) provides adversarial
enforcement of two-part PARTIAL diagnostics for C-17. G (Judge pre-conditions evidence
standard) establishes C-13 and C-15. B (sequential gate tokens) establishes C-10. M
(post-write Verifier, independent of Judge) establishes C-16.

**Hypothesis**: P+Q is the minimum addition to the R4 V-04 (G+B+M) stack to achieve
both new v5 criteria. P makes the role dependency graph a structural artifact — a table
with auditable rows where a missing entry is a visible gap (C-18). Q extends the Verifier's
existing audit to cover C-17 compliance — the same adversarial role that checks evidence
quality (Audit A) also checks that every PARTIAL verdict has a two-part diagnostic (Audit
B), before VERIFIER AUDIT COMPLETE can be issued. Two enforcement axes on C-17: the Analyst
instruction to write the diagnostic (write-time obligation) and the Verifier rejection
(post-write adversarial enforcement). Predicts: C-17 PASS (Q), C-18 PASS (P), all R4 V-04
criteria preserved. Should achieve 100/100 on v5 rubric.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task. It is a
standalone structural artifact — auditable without executing the protocol. A row with
a blank Produces or Requires cell is a structural gap. No role may begin unless its
Requires entry is present in the output above.

| Role      | Requires                  | Produces                  |
|-----------|---------------------------|---------------------------|
| JUDGE     | (none)                    | JUDGE STANDARD COMPLETE   |
| ANALYST   | JUDGE STANDARD COMPLETE   | ANALYST COMPLETE          |
| VERIFIER  | ANALYST COMPLETE          | VERIFIER AUDIT COMPLETE   |
| SYNTHESIS | VERIFIER AUDIT COMPLETE   | (terminal output)         |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - SYNTHESIS cannot begin without VERIFIER AUDIT COMPLETE present above.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Read all N outputs provided as inputs.

For each criterion in the rubric, extract one ACCEPTABLE and one UNACCEPTABLE evidence
example from the actual text of the provided outputs:

  C-[NN]: [criterion name]
  ACCEPTABLE: "[verbatim or close paraphrase from an actual output that satisfies
               this criterion]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail — drawn from provided outputs, not invented]"
  What separates them: [one sentence — the specific property that makes the ACCEPTABLE
                        example output-specific rather than generic or criterion-restating]

Cover every criterion in the rubric. Do not fabricate examples.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence grounded in this output] |
  ...

  No row may be skipped. No evidence cell may be blank.

  For each PARTIAL verdict, add a one-line diagnostic immediately after the table row:
    C-[NN] partial: [what is present in this output that prevented FAIL] /
                    [what is absent that prevented PASS]

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / N_essential * 60)
              + (recommended_pass / N_recommended * 30)
              + (aspirational_pass / N_aspirational * 10)
              = [result]

    Golden: YES — all essentials PASS; composite >= 80
         |  NO  — [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE — [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above.

The Verifier performs two independent audits per row:

AUDIT A — Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B — Diagnostic completeness: Applies to PARTIAL verdicts only. Verify that
the C-[NN] partial: line is present and covers BOTH required halves:
  (i)  what is present in the output that prevented FAIL — named specifically
  (ii) what is absent that prevented PASS — named specifically
A diagnostic that states only one direction, repeats the criterion label, or omits
either half fails Audit B. Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |----|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                        | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                        | PASS    | FAIL    | REJECTED |
  | C-03 | FAIL    | [excerpt]                        | PASS    | n/a     | ACCEPTED |
  ...

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] — Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [specific structural mechanism causing the
          difference — name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
   detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-05 — Axes P+R+G+B+M+N: Formal manifest + template PARTIAL rows + Judge + gates + Verifier + skeptic framing

**Variation axis**: Combination — replaces the adversarial Verifier diagnostic enforcement
(Q, used in V-04) with structural template PARTIAL rows (R) inside the Analyst phase, and
adds skeptic framing (N) as a fourth enforcement axis. The Verifier adds Check C (diagnostic
completeness) but the primary C-17 enforcement is now the template structure, not the
adversarial audit.

**Hypothesis**: R (template-enforced PARTIAL two-field block) achieves C-17 by making the
structural gap visible at write time, before the Verifier ever inspects it. The Verifier's
Check C then performs a post-write confirmation of the same property (C-17) via a different
enforcement family: the template creates the gap (structural/format axis); the Verifier
confirms completeness (adversarial/role axis). This is two orthogonal enforcement families
on C-17 — matching the C-11 pass condition of "two mechanisms from different enforcement
families." N adds a skeptic test (rhetorical self-accountability axis) as the fourth axis,
orthogonal to role (G+M), sequential gate (B), and structural template (R). Tests whether
two independent C-17 mechanisms from different families (template + adversarial) produce a
measurably different result from V-04's single-family adversarial approach (Q only).
Predicts: C-17 PASS via two mechanisms (R + C), C-18 PASS (P), all R4 V-05 criteria
preserved, C-11 PASS (role axis + sequential gate axis + structural template axis = three
orthogonal enforcement families, satisfying the "two independent" requirement with margin).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task. It is a
standalone structural artifact — auditable without executing the protocol. A row with
a blank Produces or Requires cell is a structural gap. No role may begin unless its
Requires entry is present in the output above.

| Role      | Requires                  | Produces                  |
|-----------|---------------------------|---------------------------|
| JUDGE     | (none)                    | JUDGE STANDARD COMPLETE   |
| ANALYST   | JUDGE STANDARD COMPLETE   | ANALYST COMPLETE          |
| VERIFIER  | ANALYST COMPLETE          | VERIFIER AUDIT COMPLETE   |
| SYNTHESIS | VERIFIER AUDIT COMPLETE   | (terminal output)         |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - SYNTHESIS cannot begin without VERIFIER AUDIT COMPLETE present above.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Read all N outputs provided as inputs.

For each criterion in the rubric, extract one ACCEPTABLE and one UNACCEPTABLE evidence
example from the actual text of the provided outputs:

  C-[NN]: [criterion name]
  ACCEPTABLE: "[text from an actual output that satisfies this criterion]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail — drawn from provided outputs, not invented]"
  What separates them: [one sentence — the specific property making the ACCEPTABLE
                        example output-specific rather than generic]

Cover every criterion in the rubric. Do not fabricate examples.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

Evidence standard — two checks apply to every evidence cell:

  CHECK A — Judge standard: Does the evidence resemble the Judge's UNACCEPTABLE
             pattern for this criterion? If yes: rewrite.

  CHECK B — Skeptic test: "If a reader had NOT seen this output, could they identify
             which specific output I am describing from my evidence alone?"
             If no: rewrite.

Both checks must clear before writing the final evidence cell.

For each output, produce a scoring record. For PASS and FAIL verdicts, use the
standard row:

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS | [evidence: Check A cleared, Check B cleared] |
  | C-03 | [name] | A | FAIL | [evidence: Check A cleared, Check B cleared] |

For PARTIAL verdicts, the standard row is followed immediately by a mandatory
two-field diagnostic block. Both fields are required before advancing to the next
criterion. This block is not optional — a PARTIAL row without a completed diagnostic
block is a format error:

  | C-[NN] | [name] | [wt] | PARTIAL | [evidence: Check A cleared, Check B cleared] |
  | C-[NN]-DIAG | Present (prevented FAIL): | | | [specific structural property     |
  |             |                            | | | present in this output that kept  |
  |             |                            | | | the verdict above FAIL]           |
  | C-[NN]-DIAG | Absent (prevented PASS):   | | | [specific structural property     |
  |             |                            | | | absent from this output that kept |
  |             |                            | | | the verdict below PASS]           |

No row may be skipped. No evidence cell may be blank. No PARTIAL verdict may appear
without its complete two-field diagnostic block (both DIAG rows filled).

Composite computation:
  essential_pass    = [count; PARTIAL = 0.5]
  recommended_pass  = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]

  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
            = [result]

  Golden: YES — all essentials PASS; composite >= 80
       |  NO  — [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE — [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above.

Apply three independent checks to each row written by the Analyst:

  CHECK A — Judge standard: Does this evidence cell resemble the UNACCEPTABLE pattern
             the Judge defined for this criterion?

  CHECK B — Skeptic test: Could a reader who has NOT read this specific output identify
             it from this evidence alone, without modification?

  CHECK C — Diagnostic completeness: Applies to PARTIAL verdicts only. Is the two-field
             PARTIAL diagnostic block present and complete? Verify BOTH:
             (i)  Present (prevented FAIL): names a specific structural property —
                  not a criterion label, not a generic quality attribute
             (ii) Absent (prevented PASS): names a specific structural property —
                  not a criterion label, not a generic quality attribute
             A single-direction diagnostic, a label-only diagnostic, or a missing
             block fails Check C. Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Check A | Check B | Check C | Status   |
  |----|---------|-----------------------------------|---------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                        | PASS    | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                        | PASS    | PASS    | FAIL    | REJECTED |
  | C-03 | FAIL    | [excerpt]                        | PASS    | PASS    | n/a     | ACCEPTED |
  ...

  Status = ACCEPTED only if all applicable checks pass.

For any row where a check fails:
  FLAG: [output ID] / [criterion ID] — Check [A/B/C]: [specific reason for failure]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference:
          name the design property, not just the criterion label]

If all outputs score identically:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
   detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, list any criterion that regressed (prior PASS
to current PARTIAL or FAIL) with output ID, criterion ID, and note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## Variation summary

| Variation | Axes | Key mechanism | C-17 pred | C-18 pred | C-11 pred |
|-----------|------|---------------|-----------|-----------|-----------|
| V-01 | P | Formal manifest table (standalone) | FAIL — no mandate for two-part structure | PASS — markdown table is standalone structural artifact | PARTIAL — role+sequential axes present, no diagnostic depth enforcement |
| V-02 | Q | Verifier audits diagnostic completeness (adversarial) | PASS — Verifier rejects single-direction diagnostics | PARTIAL — inline role declarations, no standalone table | PASS — role axis (Judge+Verifier) + sequential gate + adversarial C-17 enforcement |
| V-03 | R | Template PARTIAL rows, no roles | PASS — template block creates visible gap | FAIL — no roles, no manifest | FAIL — single mechanism (template), no role or gate axes |
| V-04 | P+Q+G+B+M | Formal manifest + Verifier C-17 audit + full role stack | PASS (Q: adversarial post-write enforcement) | PASS (P: standalone table) | PASS |
| V-05 | P+R+G+B+M+N | Formal manifest + template PARTIAL + Verifier Check C + skeptic | PASS (R: template at write time + C: Verifier post-write) | PASS (P: standalone table) | PASS |

Spread design: V-03 is the low-scoring contrast (no roles, no manifest — fails all
role-dependent aspirational criteria). V-01 tests C-18 with a formal table but no C-17
mechanism, confirming the criteria are independently required. V-02 tests C-17 via
adversarial Verifier enforcement without a formal table, targeting the C-18 ambiguity
from R4 inline declarations directly. V-04 is the minimum sufficient combination to
achieve 100/100 on v5. V-05 tests whether R (template-axis) + C (Verifier-axis) produces
a two-family enforcement combination for C-17 that is measurably distinguishable from
V-04's single-family adversarial approach (Q) — and whether N adds any remaining value
on top of the full P+R+G+B+M stack.
