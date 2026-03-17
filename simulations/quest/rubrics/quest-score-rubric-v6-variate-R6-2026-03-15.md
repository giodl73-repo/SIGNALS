# Quest Score — Round 6 Variations
**Skill**: quest-score
**Rubric**: v6 (N_essential=4, N_recommended=3, N_aspirational=12)
**Date**: 2026-03-15
**Round**: 6

---

## Design logic

### Unachieved ceiling entering R6

R5 was scored against rubric v5 (N_aspirational=11). Rubric v6 adds one new
aspirational criterion extracted from R5 excellence signals:

| Criterion | R5 status | Why unachieved in best R5 variation |
|-----------|-----------|-------------------------------------|
| C-19 | V-05 achieves via two independent paths (R template + N confirmation); V-04 FAIL | V-04's Verifier Audit B is a single adversarial enforcement path. No structural template mandate exists. C-19 requires: one format-family mechanism (template schema, structural expansion, or scoring table field) AND one independent confirmation mechanism from a different structural family. V-04 has only the adversarial family. V-05 satisfies C-19 implicitly via R (template expands PARTIAL row into Present/Absent fields) + N (Verifier Check C independently verifies content of both fields). |

Key diagnostic question for R6: can we isolate the two C-19 mechanism families in
single-axis tests, then combine them cleanly? V-05 R5 achieves C-19 implicitly — the
N axis (skeptic framing + Check C) was not designed as a C-19 mechanism; it emerged
as one. R6 makes C-19 mechanism design explicit.

### New axes for R6

| Axis | Label | Mechanism |
|------|-------|-----------|
| S | CONFIRMER role | A dedicated 4th role (after Verifier) whose sole function is to verify that every PARTIAL diagnostic's Present/Absent fields contain specific structural property names — not criterion labels, not generic phrases. Structurally separate from Verifier: separate manifest row, separate gate token (CONFIRMATION COMPLETE), separate audit question ("is this a structural property name?" rather than "is the two-part format present?"). |
| T | Content-constrained template | Extends the R-axis PARTIAL template (from R5) by embedding inline content-quality guardrails inside the field labels themselves. Each DIAG field names what counts as ACCEPTABLE (specific structural property or design gap name) and NOT ACCEPTABLE (criterion label or generic phrase). A filled-but-generic diagnostic field is treated as a format error, not a content quality issue. |

### Single-axis selection rationale

Three single-axis variations (V-01, V-02, V-03):

- **V-01 (S)**: CONFIRMER role only. Uses V-04 R5 (P+Q+G+B+M) as baseline —
  formal manifest, Judge, Analyst with one-line PARTIAL diagnostics, Verifier
  Audit A+B. Adds CONFIRMER as 4th role. Tests content-quality verification
  in isolation. Predicts: C-17 PASS (Verifier Audit B enforces format), C-19
  FAIL (two adversarial mechanisms, same structural family — no template
  format mandate as the required first path).

- **V-02 (T)**: Content-constrained template only. Uses V-03 R5 (template, no
  roles) as baseline — single scorer, no Judge/Verifier/Confirmer. Extends
  PARTIAL template fields with ACCEPTABLE/NOT ACCEPTABLE inline constraints.
  Tests whether a stronger template format mandate achieves C-17 more cleanly
  than basic field presence. Predicts: C-17 PASS (template + inline guardrails),
  C-19 FAIL (single mechanism — template family only, no independent confirmation).

- **V-03 (lifecycle-emphasis)**: Two-phase Verifier with equal lifecycle weight.
  Uses V-02 R5 (inline roles, Verifier Audit A+B) as baseline. Splits the
  Verifier into Phase 1 (Evidence Quality) and Phase 2 (Diagnostic Verification),
  each with its own named gate token and equal structural prominence. No new
  roles. Tests whether lifecycle separation (same role, two explicit phases)
  approaches the independent-mechanism requirement for C-19 — or whether same-
  entity separation doesn't satisfy "structurally independent." Predicts: C-17
  PASS (Phase 2 enforces format check + content check), C-19 FAIL (two phases
  within same role; no template format mandate in format-family sense).

### Combination selection rationale

Two combination variations (V-04, V-05):

- **V-04 (S+T)**: Minimum sufficient combination for C-19. T provides the format-
  family mechanism (content-constrained template mandates two-part structure with
  content quality inline). S provides the independent confirmation mechanism
  (CONFIRMER role, different structural family from template, operates post-write
  without inspecting template field labels). Together: template constrains content
  AT WRITE TIME; CONFIRMER challenges content quality POST-WRITE via a question
  the template cannot answer by inspection. Predicts C-19 PASS.

- **V-05 (S+T+P+Q+G+B+M, formal C-19 manifest)**: Full stack with explicit C-19
  two-path declaration. Takes V-04 R5 (P+Q+G+B+M) and adds S (CONFIRMER) +
  T (content-constrained template). Critically: adds a C-19 ENFORCEMENT MAP
  section to the manifest, formally naming both C-19 mechanism paths as
  auditable structural entries. Tests whether explicit C-19 mechanism declaration
  in the manifest produces measurably different score signal from V-05 R5's
  implicit C-19 achievement. Predicts C-19 PASS with a formally auditable two-
  path record.

---

## V-01 — Axis S: CONFIRMER role (role-sequence)

**Variation axis**: Role sequence — a dedicated CONFIRMER role is added as the 4th
role in the dependency chain, after the Verifier. The CONFIRMER's sole function is
content-quality verification of PARTIAL diagnostic fields: it checks whether each
Present/Absent field names a specific structural property, not a criterion label or
generic phrase. This question is structurally independent of Verifier Audit B
(which checks format presence only) and operates without inspecting template field
labels.

**Hypothesis**: A CONFIRMER role whose function is structurally distinct from the
Verifier's achieves the second C-19 mechanism family (independent confirmation of
substantive content) when its input is gated on VERIFIER AUDIT COMPLETE and its
output (CONFIRMATION COMPLETE) is the Synthesis input. The CONFIRMER asks "is this
a structural property name?" rather than "is the two-part format present?" — two
non-overlapping verification questions. Failure condition: if C-19 scores FAIL
rather than PARTIAL, the CONFIRMER-alone design does not demonstrate partial
compliance with C-19's two-path requirement, meaning the confirmer mechanism
contributes nothing measurable to C-19 in isolation.

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

| Role       | Requires                   | Produces                  |
|------------|----------------------------|---------------------------|
| JUDGE      | (none)                     | JUDGE STANDARD COMPLETE   |
| ANALYST    | JUDGE STANDARD COMPLETE    | ANALYST COMPLETE          |
| VERIFIER   | ANALYST COMPLETE           | VERIFIER AUDIT COMPLETE   |
| CONFIRMER  | VERIFIER AUDIT COMPLETE    | CONFIRMATION COMPLETE     |
| SYNTHESIS  | CONFIRMATION COMPLETE      | (terminal output)         |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without CONFIRMATION COMPLETE present above.
  - No role may be skipped or merged with another.

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
  What separates them: [one sentence — the specific property making the ACCEPTABLE
                        example output-specific rather than generic or
                        criterion-restating]

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

AUDIT B — Diagnostic format: Applies to PARTIAL verdicts only. Verify that the
C-[NN] partial: line is present and contains BOTH required halves:
  (i)  what is present in the output that prevented FAIL — named
  (ii) what is absent that prevented PASS — named
A diagnostic that states only one direction, repeats the criterion label, or is
missing either half fails Audit B. Mark n/a for PASS and FAIL verdicts.

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |----|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                        | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                        | PASS    | FAIL    | REJECTED |
  ...

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] — Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer independently verifies that every PARTIAL diagnostic names specific
structural properties — not criterion labels, not generic quality phrases. The
Confirmer does NOT re-check format presence (Verifier Audit B already verified
that both halves are stated). The Confirmer asks one question per field: does this
text identify a real design element by name?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] — Diagnostic Content Audit

  | Criterion | Present field (verbatim excerpt)       | Specific? | Absent field (verbatim excerpt)        | Specific? | Status              |
  |-----------|----------------------------------------|-----------|----------------------------------------|-----------|---------------------|
  | C-[NN]    | [first 15 words of Present content]    | YES / NO  | [first 15 words of Absent content]     | YES / NO  | CONFIRMED/CHALLENGED|

Specificity test:
  YES — the field names a specific structural element, mechanism, role, gate token,
        or design gap: e.g., "explicit gate token ANALYST COMPLETE", "no post-write
        verification step independent of the writer", "named Produces/Requires
        manifest table"
  NO  — the field uses a criterion label, a generic quality phrase, or restates the
        verdict without naming a design element: e.g., "some structure is present",
        "mechanism is partially addressed", "does not fully satisfy the criterion",
        "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" — [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" — [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are
closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until CONFIRMATION COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the
          difference — name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-02 — Axis T: Content-constrained PARTIAL template (output-format)

**Variation axis**: Output format — the PARTIAL diagnostic template embeds inline
content-quality guardrails inside the field labels, naming ACCEPTABLE and NOT
ACCEPTABLE examples of valid content. A filled-but-generic diagnostic field is a
format error, not a scorer quality issue: the template's ACCEPTABLE/NOT ACCEPTABLE
examples make the violation visible as mismatched field content.

**Hypothesis**: A template that names what counts as specific content (structural
property names) and what counts as generic (criterion labels, quality phrases)
achieves C-17 more robustly than a template that merely names the two required
fields — because the guardrails make formulaic fill detectable without executing
any verification role. Failure condition: if C-17 and C-09 scores do not improve
over V-03 R5 (basic two-field template), the inline ACCEPTABLE/NOT ACCEPTABLE
annotation adds no structural benefit and the axis should not be promoted to
combination runs. C-19 will FAIL by design (template-family only; no independent
confirmation mechanism from a different structural family).

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
two-field diagnostic block. Both fields must name specific structural properties —
the inline examples define the content quality standard:

  | C-[NN] | [name]  | [wt] | PARTIAL | [evidence specific to this output]    |
  | C-[NN]-DIAG | Present (prevented FAIL)                           | | | [Name the specific mechanism or       |
  |             | ACCEPTABLE: "named gate token JUDGE STANDARD         | | | structural element present — a         |
  |             |   COMPLETE coupling Judge to Analyst"                | | | design feature with a name, not a      |
  |             | NOT ACCEPTABLE: "some structure is present" or       | | | quality description]                   |
  |             |   "criterion is partially addressed"                 | | |                                        |
  | C-[NN]-DIAG | Absent (prevented PASS)                            | | | [Name the specific design gap —        |
  |             | ACCEPTABLE: "no post-write verification step         | | | an element that could be added,        |
  |             |   independent of the Analyst"                        | | | named specifically, not described      |
  |             | NOT ACCEPTABLE: "mechanism is missing" or            | | | generically]                           |
  |             |   "does not fully implement this criterion"           | | |                                        |

A PARTIAL verdict without a completed two-field block is a format error.
A filled field that matches a NOT ACCEPTABLE pattern is also a format error —
the template violation is visible from the content against the inline examples.
Do not advance to the next criterion until both DIAG fields are filled with
content matching the ACCEPTABLE pattern for that field.

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

## V-03 — Axis U: Two-phase Verifier with equal lifecycle weight (lifecycle-emphasis)

**Variation axis**: Lifecycle emphasis — the Verifier's work is split into two
structurally equal lifecycle phases, each with its own named section header, its
own gate token, and proportional structural space. Phase 1 = evidence quality
(Audit A). Phase 2 = diagnostic verification (format check + content check).
SYNTHESIS is gated on BOTH phase markers. No new roles are added; the split is
a lifecycle reorganization of the Verifier's existing function.

**Hypothesis**: Elevating diagnostic verification to a lifecycle phase with equal
structural prominence as evidence quality auditing improves C-09 (diagnostic depth)
and C-10 (phase completion gates) by making the diagnostic verification phase
impossible to omit without producing a detectable structural gap (missing gate
token). The two-phase structure tests whether lifecycle separation within a single
role approaches C-19 compliance — the prediction is that it does NOT, because both
phases belong to the same role entity and neither constitutes a "format mandate"
in the template/structural-field sense. C-19 FAIL expected. Failure condition:
if C-09 and C-10 do not improve over V-02 R5 (single-phase Verifier with Audit A+B),
the lifecycle split adds structural cost without scoring benefit.

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

  ROLE 1: JUDGE      — defines evidence quality standard before scoring begins
  ROLE 2: ANALYST    — scores each output using the Judge's standard
  ROLE 3: VERIFIER   — two equal-weight phases: evidence quality, then diagnostic
                       verification

Phase boundary:
  EVIDENCE QUALITY AUDIT COMPLETE marks the end of Verifier Phase 1.
  DIAGNOSTIC VERIFICATION COMPLETE marks the end of Verifier Phase 2.
  SYNTHESIS does not begin until BOTH phase markers appear above.

Do not begin Role 2 until JUDGE STANDARD COMPLETE appears below.
Do not begin Role 3 until ANALYST COMPLETE appears below.
Do not begin Verifier Phase 2 until EVIDENCE QUALITY AUDIT COMPLETE appears below.
Do not write synthesis sections until DIAGNOSTIC VERIFICATION COMPLETE appears below.

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
  Distinction: [one sentence — the specific property separating the two examples
               for this criterion]

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

ROLE 3: VERIFIER — PHASE 1: Evidence Quality Audit

Do not begin until ANALYST COMPLETE appears above.

Read every evidence cell written by the Analyst. For each output, for each criterion,
compare the evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE pair. Produce
a per-output evidence audit table:

  Output: [output identifier] — Evidence Quality Audit

  | ID | Evidence cell excerpt (first 15 words) | ACCEPTED / REJECTED | Reason if REJECTED |
  |----|----------------------------------------|--------------------|---------------------|
  | C-01 | [excerpt]                             | ACCEPTED           |                     |
  ...

Rejection criteria: evidence resembles the UNACCEPTABLE pattern for this criterion,
OR could apply to a different output with no modification.

For every REJECTED cell:
  FLAG: [output ID] / [criterion ID] — Evidence: [specific reason the evidence
        fails the Judge's standard]

Flagged cells must be rewritten by the Analyst and re-audited here. Only flagged
cells are reopened; accepted cells are closed.

When all evidence cells are ACCEPTED across all N outputs:
EVIDENCE QUALITY AUDIT COMPLETE

---

ROLE 3: VERIFIER — PHASE 2: Diagnostic Verification Audit

Do not begin until EVIDENCE QUALITY AUDIT COMPLETE appears above.

This phase is structurally equal in weight to Phase 1. Read every PARTIAL verdict
across all N outputs. For each PARTIAL verdict, the C-[NN] partial: diagnostic is
subject to two independent checks:

CHECK 1 — Format completeness: Both halves present?
  (i)  what is present that prevented FAIL — stated?
  (ii) what is absent that prevented PASS — stated?
  Fails if either direction is missing, or if either direction restates the criterion
  label rather than naming content from the output.

CHECK 2 — Content specificity: Does each stated half identify a specific structural
  element or design gap?
  Present half: "a gate token named JUDGE STANDARD COMPLETE" is specific. "some
    structural element is present" is not.
  Absent half: "no standalone Produces/Requires manifest table" is specific.
    "mechanism is not fully present" is not.

Produce a per-PARTIAL diagnostic verification table:

  Output: [output identifier] — Diagnostic Verification Audit

  | Criterion | Diagnostic excerpt (first 15 words) | Check 1 | Check 2 | Status               |
  |-----------|-------------------------------------|---------|---------|----------------------|
  | C-[NN]    | [excerpt]                           | PASS/FAIL | PASS/FAIL | CONFIRMED/CHALLENGED |

For every CHALLENGED diagnostic:
  CHALLENGE: [output ID] / [criterion ID] — Check [1/2]: [specific reason]

Challenged diagnostics must be rewritten by the Analyst and re-audited in both
Phase 1 (evidence) and Phase 2 (diagnostic). Only challenged items are reopened.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
DIAGNOSTIC VERIFICATION COMPLETE

---

SYNTHESIS

Do not begin until DIAGNOSTIC VERIFICATION COMPLETE appears above.
(EVIDENCE QUALITY AUDIT COMPLETE must also be present — both phase markers required.)

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference:
          name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-04 — Axes S+T: CONFIRMER role + content-constrained template

**Variation axes**: Role sequence (S: CONFIRMER as 4th role) × Output format
(T: content-constrained PARTIAL template with inline ACCEPTABLE/NOT ACCEPTABLE
guardrails). Minimum sufficient combination for C-19: T provides the format-family
mechanism (template schema with embedded content constraints mandates two-part
structure with specificity requirements at write time); S provides the independent
confirmation mechanism (CONFIRMER role operates post-write, from a structurally
distinct position, on a question the template cannot answer by inspection).

**Hypothesis**: T (content-constrained template) + S (CONFIRMER) achieve C-19 via
two structurally independent enforcement families: template/format-family (T) and
role/adversarial-family (S). The template enforces format AND content quality at
write time — a filled-but-generic DIAG field is a visible format error. The
CONFIRMER verifies the same content quality post-write from an independent position
— it cannot be satisfied by inspecting whether the template fields exist. Two paths,
different failure modes: the template catches formulaic fill before writing is
complete; the CONFIRMER catches it after, without the template as its instrument.
C-19 PASS expected. Failure condition: if C-19 is PARTIAL rather than PASS, the
template + CONFIRMER combination does not constitute "structurally independent"
mechanisms in the rubric's sense, and the combination provides no improvement over
V-01 or V-02 alone on C-19.

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

| Role       | Requires                   | Produces                  |
|------------|----------------------------|---------------------------|
| JUDGE      | (none)                     | JUDGE STANDARD COMPLETE   |
| ANALYST    | JUDGE STANDARD COMPLETE    | ANALYST COMPLETE          |
| VERIFIER   | ANALYST COMPLETE           | VERIFIER AUDIT COMPLETE   |
| CONFIRMER  | VERIFIER AUDIT COMPLETE    | CONFIRMATION COMPLETE     |
| SYNTHESIS  | CONFIRMATION COMPLETE      | (terminal output)         |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without CONFIRMATION COMPLETE present above.
  - No role may be skipped or merged with another.

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
  What separates them: [one sentence — the specific property making the ACCEPTABLE
                        example output-specific rather than generic or
                        criterion-restating]

Cover every criterion in the rubric. Do not fabricate examples.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

Evidence standard: Before writing any evidence cell, verify it against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft resembles the
UNACCEPTABLE pattern, rewrite it before entering the final cell.

For each output, produce a scoring record.

For PASS and FAIL verdicts, use the standard row:

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS | [evidence: Judge standard cleared] |
  | C-03 | [name] | A | FAIL | [evidence: Judge standard cleared] |

For PARTIAL verdicts, the standard row is followed immediately by a mandatory
two-field diagnostic block. Both fields must name specific structural properties —
the inline examples define the content quality standard enforced by this template:

  | C-[NN] | [name]  | [wt] | PARTIAL | [evidence: Judge standard cleared]    |
  | C-[NN]-DIAG | Present (prevented FAIL)                           | | | [Name the specific mechanism or       |
  |             | ACCEPTABLE: "named gate token JUDGE STANDARD         | | | structural element present — a design  |
  |             |   COMPLETE coupling Judge to Analyst"                | | | feature with a real name, not a        |
  |             | NOT ACCEPTABLE: "some structure is present" or       | | | quality description]                   |
  |             |   "criterion is partially addressed"                 | | |                                        |
  | C-[NN]-DIAG | Absent (prevented PASS)                            | | | [Name the specific design gap —        |
  |             | ACCEPTABLE: "no post-write verification step         | | | an element that could be added,        |
  |             |   independent of the Analyst"                        | | | named specifically]                    |
  |             | NOT ACCEPTABLE: "mechanism is missing" or            | | |                                        |
  |             |   "does not fully implement this criterion"           | | |                                        |

A PARTIAL verdict without a completed two-field block is a format error.
A filled field that matches a NOT ACCEPTABLE pattern is also a format error.
Do not advance to the next criterion until both DIAG fields satisfy the ACCEPTABLE
pattern for that field.

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

The Verifier performs two independent audits per row:

AUDIT A — Evidence quality: Compare each evidence cell against the Judge's
ACCEPTABLE/UNACCEPTABLE pair for that criterion. Reject any cell that:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output with no modification.

AUDIT B — Diagnostic format: Applies to PARTIAL verdicts only. Verify that
both DIAG fields are present (neither blank). A diagnostic that states only one
direction, or that contains a NOT ACCEPTABLE pattern in either field, fails Audit B.
Mark n/a for PASS and FAIL verdicts.

Note: Audit B checks format presence and obvious template violations. Deeper content
specificity is verified by the Confirmer (Role 4), not here.

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status   |
  |----|---------|-----------------------------------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                        | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                        | PASS    | FAIL    | REJECTED |
  ...

  Status = ACCEPTED only if all applicable audits pass.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] — Audit [A/B]: [specific reason for rejection]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer independently verifies that every PARTIAL diagnostic names specific
structural properties — not criterion labels, not generic quality phrases. The
Confirmer operates independently of the template: it does not inspect whether the
template fields are structurally present (Audit B already verified that). It asks
only: does this text identify a real design element?

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] — Diagnostic Content Audit

  | Criterion | Present field (verbatim excerpt)    | Specific? | Absent field (verbatim excerpt)    | Specific? | Status              |
  |-----------|-------------------------------------|-----------|-------------------------------------|-----------|---------------------|
  | C-[NN]    | [first 15 words]                    | YES / NO  | [first 15 words]                    | YES / NO  | CONFIRMED/CHALLENGED|

Specificity test:
  YES — names a specific structural element, mechanism, role, gate token, or design
        gap: e.g., "explicit gate token ANALYST COMPLETE", "no post-write verification
        step independent of the writer", "named Produces/Requires manifest table"
  NO  — uses a criterion label, generic quality phrase, or restates the verdict:
        e.g., "some structure is present", "mechanism is partially addressed",
        "does not fully satisfy the criterion", "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" — [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" — [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
and Confirmer. Only challenged items are reopened.

When all PARTIAL diagnostics are CONFIRMED across all N outputs:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until CONFIRMATION COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference:
          name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-05 — Axes S+T+P+Q+G+B+M with formal C-19 enforcement map

**Variation axes**: Full best-of stack (P+Q+G+B+M from R5 V-04, T from V-02 R6,
S from V-01 R6) with a formal C-19 ENFORCEMENT MAP section added to the manifest.
The enforcement map explicitly declares which structural mechanisms satisfy C-17's
format-mandate requirement and which satisfy C-19's independent-confirmation
requirement — making the two-path design auditable as a standalone artifact, not
derived by reading the role instructions.

**Hypothesis**: Making the C-19 mechanism paths formally declared in a structural
artifact (the enforcement map table) satisfies C-19 more auditably than V-05 R5's
implicit achievement — where the N-axis confirmation function had to be inferred
from the Check B/C relationship. A reader who inspects only the manifest can
determine both C-17 mechanisms and both C-19 mechanism families without executing
the protocol. Predicts: C-19 PASS (explicit two-path declaration), all prior R5
V-04 criteria preserved, C-11 PASS (role + sequential gate + template = three
orthogonal enforcement families). Failure condition: if C-19 scores identically to
V-04 R6, the formal declaration adds no measurable scoring signal — the mechanism
existence (not its declaration) is what C-19 assesses, and R7 should test
declaration-level criteria if warranted.

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

| Role       | Requires                   | Produces                  |
|------------|----------------------------|---------------------------|
| JUDGE      | (none)                     | JUDGE STANDARD COMPLETE   |
| ANALYST    | JUDGE STANDARD COMPLETE    | ANALYST COMPLETE          |
| VERIFIER   | ANALYST COMPLETE           | VERIFIER AUDIT COMPLETE   |
| CONFIRMER  | VERIFIER AUDIT COMPLETE    | CONFIRMATION COMPLETE     |
| SYNTHESIS  | CONFIRMATION COMPLETE      | (terminal output)         |

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without CONFIRMATION COMPLETE present above.
  - No role may be skipped or merged with another.

C-19 ENFORCEMENT MAP

The following table declares the two structurally independent mechanisms that
enforce C-17 compliance (two-part PARTIAL diagnostics). This table is a standalone
auditable artifact. Both rows must be present; a blank row is a structural gap.

| Mechanism path | Family          | What it enforces                                           | Where it operates        |
|-----------------|-----------------|-------------------------------------------------------------|--------------------------|
| T: Content-constrained PARTIAL template | Format-family | Two-part structure is structurally mandated; generic fill is a template violation detectable by inspection | At Analyst write time |
| S: CONFIRMER role (Role 4) | Role/adversarial-family | Both diagnostic directions were substantively addressed with specific structural property names; verification question is independent of template inspection | Post-write, after VERIFIER AUDIT COMPLETE |

A design that satisfies C-17 through one path only (either T or S alone) achieves
C-17 compliance but not C-19 independence. Both rows of this table must be
structurally active.

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
  What separates them: [one sentence — the specific property making the ACCEPTABLE
                        example output-specific rather than generic or
                        criterion-restating]

Cover every criterion in the rubric. Do not fabricate examples.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

Evidence standard — two checks apply to every evidence cell before writing:

  CHECK A — Judge standard: Does the evidence resemble the Judge's UNACCEPTABLE
             pattern for this criterion? If yes: rewrite.

  CHECK B — Skeptic test: "If a reader had NOT seen this output, could they identify
             which specific output I am describing from my evidence alone?"
             If no: rewrite.

Both checks must clear before writing the final evidence cell.

For each output, produce a scoring record.

For PASS and FAIL verdicts, use the standard row:

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS | [evidence: Check A cleared, Check B cleared] |
  | C-03 | [name] | A | FAIL | [evidence: Check A cleared, Check B cleared] |

For PARTIAL verdicts, the standard row is followed immediately by a mandatory
two-field diagnostic block. Both fields must name specific structural properties —
the inline examples define the content quality standard (C-19 Mechanism T):

  | C-[NN] | [name]  | [wt] | PARTIAL | [evidence: Check A cleared, Check B cleared] |
  | C-[NN]-DIAG | Present (prevented FAIL)                           | | | [Name the specific mechanism or       |
  |             | ACCEPTABLE: "named gate token JUDGE STANDARD         | | | structural element present — a design  |
  |             |   COMPLETE coupling Judge to Analyst"                | | | feature with a real name]              |
  |             | NOT ACCEPTABLE: "some structure is present" or       | | |                                        |
  |             |   "criterion is partially addressed"                 | | |                                        |
  | C-[NN]-DIAG | Absent (prevented PASS)                            | | | [Name the specific design gap —        |
  |             | ACCEPTABLE: "no post-write verification step         | | | an element that could be added,        |
  |             |   independent of the Analyst"                        | | | named specifically]                    |
  |             | NOT ACCEPTABLE: "mechanism is missing" or            | | |                                        |
  |             |   "does not fully implement this criterion"           | | |                                        |

A PARTIAL verdict without a completed two-field block is a format error.
A filled field matching a NOT ACCEPTABLE pattern is also a format error.
Do not advance to the next criterion until both DIAG fields satisfy their
ACCEPTABLE pattern.

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

The Verifier performs three independent checks per row:

CHECK A — Judge standard: Does this evidence cell resemble the UNACCEPTABLE pattern
           the Judge defined for this criterion?

CHECK B — Skeptic test: Could a reader who has NOT read this specific output
           identify it from this evidence alone, without modification?

CHECK C — Diagnostic format: Applies to PARTIAL verdicts only. Are the two DIAG
           fields present and non-empty, with content that does not match the
           NOT ACCEPTABLE pattern in either field? Mark n/a for PASS and FAIL.
           Note: Check C verifies template compliance; content specificity is
           independently verified by the Confirmer (Role 4).

Produce a per-output combined audit table:

  Output: [output identifier] — Post-write Evidence and Diagnostic Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Check A | Check B | Check C | Status   |
  |----|---------|-----------------------------------|---------|---------|---------|----------|
  | C-01 | PASS    | [excerpt]                        | PASS    | PASS    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                        | PASS    | PASS    | FAIL    | REJECTED |
  ...

  Status = ACCEPTED only if all applicable checks pass.

For any row where a check fails:
  FLAG: [output ID] / [criterion ID] — Check [A/B/C]: [specific reason for failure]

Flagged items must be corrected by the Analyst and re-audited. Only flagged items
are reopened; accepted items are closed.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER  (C-19 Mechanism S)

Do not begin until VERIFIER AUDIT COMPLETE appears above.

The Confirmer independently verifies that every PARTIAL diagnostic names specific
structural properties — operating independently of the template (C-19 Mechanism T).
The Confirmer's verification question cannot be answered by inspecting whether the
template fields are present; it requires reading content and judging whether it
identifies a real design element.

For each PARTIAL verdict across all outputs, produce a content challenge row:

  Output: [output identifier] — Diagnostic Content Audit (C-19 Mechanism S)

  | Criterion | Present field (verbatim excerpt)    | Specific? | Absent field (verbatim excerpt)    | Specific? | Status              |
  |-----------|-------------------------------------|-----------|-------------------------------------|-----------|---------------------|
  | C-[NN]    | [first 15 words]                    | YES / NO  | [first 15 words]                    | YES / NO  | CONFIRMED/CHALLENGED|

Specificity test:
  YES — names a specific structural element, mechanism, role, gate token, or design
        gap: e.g., "explicit gate token ANALYST COMPLETE", "no post-write verification
        step independent of the writer", "named Produces/Requires manifest table"
  NO  — uses a criterion label, generic quality phrase, or restates the verdict:
        e.g., "some structure is present", "mechanism is partially addressed",
        "does not fully satisfy the criterion", "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" — [specific reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" — [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by Verifier (Check C)
and Confirmer. Only challenged items are reopened.

When all PARTIAL diagnostics are CONFIRMED across all N outputs:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until CONFIRMATION COMPLETE appears above.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] — [criterion ID] — [structural mechanism causing the difference:
          name the design property, not just the criterion label]

If no variation outperforms any other on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, identify any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## Variation summary

| Variation | Axes     | Key mechanism                                  | C-17 pred | C-18 pred | C-19 pred | C-11 pred |
|-----------|----------|------------------------------------------------|-----------|-----------|-----------|-----------|
| V-01 | S | CONFIRMER role checks content specificity post-write | PASS (Verifier Audit B enforces format) | PASS (manifest from V-04 R5 base) | FAIL — CONFIRMER alone is single adversarial-family mechanism; no template format mandate | PASS |
| V-02 | T | Content-constrained template with inline ACCEPTABLE/NOT ACCEPTABLE guardrails | PASS (template mandates format + names content quality standard) | FAIL (no roles; no manifest) | FAIL — template alone is single format-family mechanism; no independent confirmation | FAIL |
| V-03 | U (lifecycle) | Two-phase Verifier with equal lifecycle weight; Phase 1 = evidence; Phase 2 = diagnostic check | PASS (Phase 2 Check 1+2 enforces format and content) | FAIL (inline roles only; no standalone table) | FAIL — both phases in same role entity; no template format mandate; same-role phases are not structurally independent families | PARTIAL (Phase 2 gate adds structure) |
| V-04 | S+T | Content-constrained template + CONFIRMER role (minimum sufficient for C-19) | PASS (T template + Verifier Audit B) | PASS (manifest) | PASS — T is format-family mandate; S is role/adversarial-family independent confirmation; structurally independent by design | PASS |
| V-05 | S+T+P+Q+G+B+M + C-19 map | Full best-of stack + formal C-19 ENFORCEMENT MAP in manifest | PASS (T template + Verifier Check C) | PASS (P manifest) | PASS — both mechanism paths formally declared in C-19 ENFORCEMENT MAP; two-path design is auditable from the manifest alone | PASS |

Spread design: V-02 is the low-scoring contrast (no roles, no manifest — fails
all role-dependent aspirational criteria). V-01 tests the CONFIRMER mechanism
without a template, confirming it alone cannot satisfy C-19. V-03 tests lifecycle
separation within one role — designed to fail C-19 and establish that same-entity
phase separation is not structurally independent. V-04 is the minimum C-19 path
(S+T only). V-05 is the full stack with explicit C-19 mechanism declaration.

---

## Combination candidates for Round 7

| Priority | Axis Pair | V-NN Basis | Mechanism | Criteria Targeted |
|----------|-----------|------------|-----------|-------------------|
| 1 | S+T+formal-C19-declaration × inertia-framing (champion inventory) | V-05 R6 (formal C-19 manifest) × V-03 R3 (champion-challenger framing) | V-05 R6 makes C-19 mechanisms formally auditable; champion framing applied to the C-19 map would require each scored output's diagnostic choices to be evaluated against a named champion's mechanism choices, exposing whether C-19 compliance is substantive or nominal. Combined: criterion-keyed competitive scoring that forces the evaluator to name why a scored output's C-19 mechanism is weaker than the champion's — criterion C-09 and future C-20 candidates. | C-09 diagnostic depth, potential C-20 |
| 2 | lifecycle-emphasis (V-03 R6 two-phase Verifier) × role-sequence (S CONFIRMER) | V-03 R6 (Phase 2 gate token adds lifecycle structure) × V-01 R6 (CONFIRMER separate role) | V-03 R6 achieves PARTIAL lifecycle separation; V-01 achieves full role separation. Combined: the CONFIRMER role is explicitly mapped to Phase 2's diagnostic verification function — a role+phase coupling that tests whether assigning a dedicated role to an existing lifecycle phase strengthens or replicates the V-01 role-only mechanism. Tests whether role identity and lifecycle identity need to be separately declared or whether one covers both. | C-10, C-14, C-19 boundary case |

---

## Evaluation order

| Priority | Variation | Axis | Evaluation cost | Independence | Dependency note |
|----------|-----------|------|-----------------|--------------|-----------------|
| 1 | V-02 | T (output-format) | Low — no roles, no manifest; single-scorer template variant | Independent | No dependency on other R6 variations. Establishes the T-axis content-constrained template baseline that V-04 must exceed on C-19. |
| 2 | V-03 | U (lifecycle-emphasis) | Low — same role structure as V-02 R5; only phase split changes | Independent | Evaluate before V-01: confirms whether same-entity phase separation achieves C-19 PARTIAL (informing whether role-separation is necessary for C-19 at all). |
| 3 | V-01 | S (role-sequence) | Medium — adds CONFIRMER role with manifest update | Independent of V-02/V-03 | Evaluate after V-03: confirms CONFIRMER alone fails C-19, establishing the S-axis contribution without T as the second mechanism. C-19 scoring of V-01 is interpretable only once V-03 establishes that lifecycle-separation alone also fails. |
| 4 | V-04 | S+T (combination) | Medium — two axes active; CONFIRMER + content-constrained template | Dependent on V-01 and V-02 baselines | V-04's C-19 PASS claim is verifiable only once V-01 (S alone) and V-02 (T alone) both establish FAIL baselines. Interpret as: does combining two single-FAIL mechanisms achieve PASS? |
| 5 | V-05 | S+T+P+Q+G+B+M + C-19 map | High — full six-mechanism stack; most structurally complex variation in R6 | Dependent on V-04 baseline | Evaluate last. V-05's compound claim (formal declaration adds measurable signal beyond V-04) requires V-04 C-19 PASS to be confirmed first. If V-04 achieves C-19 PASS without formal declaration, V-05 tests the declaration-value hypothesis in isolation. |
