# Quest Score — Round 4 Variations
**Skill**: quest-score
**Rubric**: v4 (N_essential=4, N_recommended=3, N_aspirational=9)
**Date**: 2026-03-15
**Round**: 4

## Design logic

### Unachieved ceilings entering R4

| Criterion | R3 status | Why unachieved |
|-----------|-----------|----------------|
| C-15 | Achieved by V-01(G) only | Other R3 variations have no output-input coupling; G's `JUDGE STANDARD COMPLETE` token is the specific mechanism |
| C-16 | PARTIAL for all R3 variations | V-01(G) is closest — Judge pre-conditions evidence standard — but no entity verifies Analyst evidence *after* it is written; pre-conditioning does not catch drift during writing |

### New axes for R4

| Axis | Label | Mechanism |
|------|-------|-----------|
| M | Post-write Verifier role | A third named role runs after the Analyst writes evidence cells and audits them against the Judge's standard; produces `VERIFIER AUDIT COMPLETE` token. Targets C-16 directly. |
| N | Skeptic-proof accountability framing | Every evidence cell must pass a "skeptic test": could a reader who has NOT seen this output identify it from the evidence alone? Single-scorer; no role separation. Targets C-04 via rhetorical obligation rather than structural enforcement. |
| O | Lifecycle phase proportion | Explicit effort allocation across phases (10%/60%/10%/20%); evidence-quality phase receives dominant scaffolding with per-criterion annotation blocks. Targets C-09 (diagnostic depth) and C-08. No role separation. |

### Single-axis selection rationale

Three single-axis variations (V-01, V-02, V-03) to establish divergence baselines:
- V-01 (M): directly targets C-16; predicts C-13 PASS, C-15 PASS (token coupling present), C-16 PASS (post-write Verifier)
- V-02 (N): does not target C-16; predicts C-04 improved, C-13/C-15/C-16 FAIL (no external roles); provides low-scoring contrast variation to ensure spread
- V-03 (O): does not target C-16; predicts C-09 improved, C-08 PASS, C-13/C-15/C-16 FAIL; provides medium-scoring contrast

### Combination selection rationale

Two combination variations (V-04, V-05):
- V-04 (G+B+M): minimum sufficient combination — G enforces C-15 via `JUDGE STANDARD COMPLETE` coupling, B enforces sequential ordering, M adds post-write Verifier for C-16. Should achieve all R3 criteria + C-15 + C-16.
- V-05 (G+B+M+N): adds skeptic framing inside the Analyst phase on top of V-04. Creates a fourth enforcement axis (rhetorical self-accountability) orthogonal to role (G+M) and sequential gate (B). Tests whether the skeptic test inside the Analyst phase strengthens C-12 or C-04 beyond what V-04 achieves alone.

---

## V-01 — Axis M: Post-write Verifier role

**Variation axis**: Role sequence — adds a third role (Verifier) that audits Analyst evidence cells after they are written, against the Judge's pre-defined standard, before synthesis can proceed.

**Hypothesis**: The Verifier role is a structurally independent entity performing post-write evidence verification. This directly targets C-16. The JUDGE STANDARD COMPLETE token as Analyst input preserves C-15. C-11 should achieve PASS: role axis (Judge pre-conditioning) + sequential gate axis (VERIFIER AUDIT COMPLETE as Synthesis prerequisite) = two independent enforcement layers. C-14 should PASS: role-based enforcement (who) + sequential gate enforcement (when) are orthogonal families.

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
  ROLE 3: VERIFIER  — audits the Analyst's evidence cells after they are written

Do not begin Role 2 until JUDGE STANDARD COMPLETE appears below.
Do not begin Role 3 until ANALYST COMPLETE appears below.
Do not write synthesis sections until VERIFIER AUDIT COMPLETE appears below.

---

ROLE 1: JUDGE

Read all N outputs provided as inputs. For each criterion in the rubric, extract
one ACCEPTABLE and one UNACCEPTABLE evidence example from the actual output text:

  C-[NN]: [criterion name]
  ACCEPTABLE: "[text from an actual output that satisfies this criterion]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail — drawn from provided outputs, not invented]"
  Distinction: [one sentence: what separates the ACCEPTABLE example from the
               UNACCEPTABLE one for this criterion specifically]

Cover every criterion in the rubric. Do not generate examples from outside the
provided outputs.

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, check
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your
draft evidence resembles the UNACCEPTABLE pattern, rewrite it before entering the
final cell.

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence grounded in this output] |
  ...

  No row may be skipped. No evidence cell may be blank.

  After the table:
    essential_pass    = [count; PARTIAL counts as 0.5]
    recommended_pass  = [count; PARTIAL counts as 0.5]
    aspirational_pass = [count; PARTIAL counts as 0.5]

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

Read every evidence cell written by the Analyst. For each output, for each
criterion, compare the evidence cell against the Judge's ACCEPTABLE/UNACCEPTABLE
pair. Produce an audit table:

  Output: [output identifier] — Post-write Evidence Audit

  | ID | Evidence cell excerpt (first 15 words) | Status    | Rejection reason |
  |----|----------------------------------------|-----------|-----------------|
  | C-01 | [excerpt]                            | ACCEPTED  |                  |
  | C-02 | [excerpt]                            | REJECTED  | [reason]         |
  ...

Rejection criteria: evidence resembles the Judge's UNACCEPTABLE pattern, or could
apply to a different output with no modification.

For every REJECTED cell:
  FLAG: [output ID] / [criterion ID] — [specific reason evidence fails the standard]

Flagged cells must be rewritten by the Analyst. Rewritten cells are re-audited
before the Verifier signs off. Only flagged cells are reopened; accepted cells
are not re-examined.

When all evidence cells are ACCEPTED across all outputs:
VERIFIER AUDIT COMPLETE

---

SYNTHESIS

Do not begin until VERIFIER AUDIT COMPLETE appears above.

LEADERBOARD

All outputs ranked by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output scores higher than others:
  Signal: [output ID] — [criterion ID] — [specific structural property that caused
  the difference; name the mechanism, not just the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If a prior-round scorecard is provided, list any criterion that regressed (prior
PASS to current PARTIAL or FAIL) with output ID, criterion ID, and a note on
what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-02 — Axis N: Skeptic-proof accountability framing

**Variation axis**: Phrasing register — replaces structural role separation with an explicit "skeptic test" cognitive obligation. Single scorer. The scorer must prove each evidence cell would identify the specific output to a reader who has not seen it.

**Hypothesis**: Rhetorical accountability framing without role separation. Predicts: C-04 moderate improvement (framing creates quality pressure but no structural enforcement), C-09 PASS (accountability prose generates diagnostic depth), C-13/C-15/C-16 FAIL (no external roles), C-11/C-14 FAIL (single mechanism). Low-scoring contrast variation confirms that rhetorical framing alone cannot substitute for structural role separation on the aspirational criteria.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

EVIDENCE STANDARD: THE SKEPTIC TEST

Before writing any evidence field, apply this test:

  "If a reader had NOT read the output I am citing, could they — from my evidence
   alone — identify which specific output I am describing?"

If the answer is NO: the evidence is generic. Rewrite it before entering the cell.
If the answer is YES: the evidence is grounded. Write it.

Evidence that passes the skeptic test:
  - Quotes or closely paraphrases text that could only appear in this specific output
  - Describes a structural feature unique to this output's design
  - References a mechanism specific to this output's implementation

Evidence that fails the skeptic test:
  - Describes a pattern that would apply to any well-designed output
    (e.g., "includes a verdict table with evidence")
  - Uses criterion-language rather than output-language
    (e.g., "satisfies the completeness requirement")
  - Describes what the criterion requires rather than what the output does

---

SCORING PHASE

For each output, produce a scoring table. Apply the skeptic test to each evidence
cell before writing it.

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence (skeptic-test passed) |
  |----|-----------|--------|---------|-------------------------------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence] |
  ...

  No row may be skipped. No evidence cell may be blank.

  For each PARTIAL verdict, add a one-sentence self-check after the table row:
    Self-check C-[NN]: My evidence says "[brief excerpt]." A reader who has not
    seen this output would know: [what the evidence reveals specifically]. This
    evidence could not apply to another output because: [distinguishing reason].

  Compute composite:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / N_essential * 60)
              + (recommended_pass / N_recommended * 30)
              + (aspirational_pass / N_aspirational * 10)
              = [result]

    Golden: YES — all essentials PASS; composite >= 80
         |  NO  — [reason]

Score all N outputs.

---

LEADERBOARD

All outputs ranked by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

---

EXCELLENCE SIGNALS

For each criterion where at least one output scores higher than others:
  Signal: [output ID] — [criterion ID] — [structural property causing the difference]

If all outputs score identically: "No differentiating excellence signals."

---

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [reason]

If none: "No failure patterns in this round."

---

REGRESSION SIGNALS

If prior-round scorecard data is provided, list any regression (prior PASS to
current PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-03 — Axis O: Lifecycle emphasis — phased effort allocation with per-criterion annotation

**Variation axis**: Lifecycle emphasis — explicit effort proportion guidance across four phases; evidence-quality phase receives dominant scaffolding with mandatory per-criterion annotation blocks that expand each criterion entry from a table row to a full observation record.

**Hypothesis**: Allocating explicit effort to evidence quality and requiring per-criterion annotation blocks (not just table rows) elevates C-09 (diagnostic depth) by forcing the scorer to write "gap" observations even for PASS verdicts. Predicts C-08 PASS (phase completeness markers), C-09 PASS (annotation blocks contain causal explanation). C-13/C-15/C-16 FAIL (no roles); C-11/C-14 FAIL (single sequential mechanism). Medium-scoring contrast variation between V-02 and V-04.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PHASE STRUCTURE AND EFFORT ALLOCATION

This task has four phases. Allocate effort in proportion to the weight shown.
Complete each phase before advancing to the next.

  Phase 1 — EVIDENCE BARS         (10%)
    Extract the evidence quality standard for each criterion from the rubric.

  Phase 2 — EVIDENCE QUALITY      (60%)
    Core of this task. Write per-criterion annotation blocks for every output.
    Scoring errors originate here; this phase receives the most scaffolding.

  Phase 3 — COMPOSITE SCORING     (10%)
    Apply the formula mechanically from Phase 2 verdicts.

  Phase 4 — SYNTHESIS             (20%)
    Leaderboard, excellence signals, failure patterns, regression signals.

---

PHASE 1: EVIDENCE BARS

For each criterion in the rubric, state the evidence quality bar in one sentence:

  C-01: Bar — [what specific, traceable evidence looks like for this criterion]
  C-02: Bar — [...]
  ...

Cover every criterion. These bars are the scoring standard for Phase 2.

PHASE 1 COMPLETE

---

PHASE 2: EVIDENCE QUALITY

Do not begin until PHASE 1 COMPLETE appears above.

For each output, for each criterion, write a full annotation block. Do not compress
into table rows — each criterion gets its own block:

  Output: [output identifier]
  Criterion: C-[NN] — [criterion name]
  Evidence bar (from Phase 1): [restate the bar for this criterion]
  Observed text: [specific text or structural observation from this output]
  Gap (if any): [what would be required to elevate PARTIAL to PASS, or FAIL to PARTIAL]
  Verdict: PASS | PARTIAL | FAIL

Repeat for every criterion and every output. No criterion may be skipped for any output.

PHASE 2 COMPLETE — [N] outputs x [M] criteria = [N*M] annotation blocks written

---

PHASE 3: COMPOSITE SCORING

Do not begin until PHASE 2 COMPLETE appears above.

For each output, extract the verdicts from Phase 2 and compute:

  Output: [output identifier]
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / N_essential * 60)
              + (recommended_pass / N_recommended * 30)
              + (aspirational_pass / N_aspirational * 10)
              = [result]

    Golden: YES — all essentials PASS; composite >= 80
         |  NO  — [which essential failed, or composite < 80]

PHASE 3 COMPLETE

---

PHASE 4: SYNTHESIS

Do not begin until PHASE 3 COMPLETE appears above.

LEADERBOARD

All outputs ranked by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output scores higher than others:
  Signal: [output ID] — [criterion ID] — [structural property causing the difference]

If all outputs score identically: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] — [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] — [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round scorecard data is provided, list any criterion that regressed (prior
PASS to current PARTIAL or FAIL) with output ID, criterion ID, and note on what changed.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-04 — Axes G+B+M: Judge-first + phase gates + post-write Verifier

**Variation axis**: Combination — Judge-first standard-setting (G) establishes C-15 coupling via `JUDGE STANDARD COMPLETE` as Analyst required input; phase gates (B) enforce all three role transitions via named tokens; post-write Verifier (M) performs independent evidence audit after Analyst writes, targeting C-16.

**Hypothesis**: This is the minimum sufficient combination to achieve both C-15 and C-16 simultaneously. G establishes role output-input coupling (C-15). M provides the post-write independent verification mechanism (C-16). B creates sequential gates across all three role transitions (C-10). Role axis (Judge pre-write, Verifier post-write) + sequential gate axis (B) = two orthogonal enforcement families (C-14). Three enforcement mechanisms: who sets the standard (G), when scoring can begin (B gate 1), who verifies after writing (M), when synthesis can begin (B gate 2). Predicts 100/100 on v4.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE STRUCTURE AND PHASE GATES

Three roles complete this task in strict sequence. Each role produces a named
gate token that the next role requires as its input.

  ROLE 1: JUDGE     Produces: JUDGE STANDARD COMPLETE
  ROLE 2: ANALYST   Requires: JUDGE STANDARD COMPLETE | Produces: ANALYST COMPLETE
  ROLE 3: VERIFIER  Requires: ANALYST COMPLETE        | Produces: VERIFIER AUDIT COMPLETE

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present in the output above.
  - Role 3 cannot begin without ANALYST COMPLETE present in the output above.
  - Synthesis cannot begin without VERIFIER AUDIT COMPLETE present in the output above.
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
                 that would fail — drawn from the provided outputs, not invented]"
  What separates them: [one sentence — what specific property makes the ACCEPTABLE
                        example output-specific and the UNACCEPTABLE example generic]

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

Flagged cells must be rewritten by the Analyst and re-audited by the Verifier before
sign-off. Only flagged cells are reopened; accepted cells are closed.

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
  Signal: [output ID] — [criterion ID] — [specific structural mechanism that caused
          the difference — name the property, not just the criterion label]

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
PARTIAL or FAIL) with output ID, criterion ID, and a note explaining the change.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-05 — Axes G+B+M+N: Judge-first + phase gates + post-write Verifier + skeptic-proof framing

**Variation axis**: Combination — adds skeptic-proof accountability framing (N) as a fourth enforcement axis inside the Analyst phase on top of the full G+B+M stack from V-04.

**Hypothesis**: G defines what acceptable evidence looks like (external standard, before writing). N obliges the Analyst to self-verify each cell at write time via the skeptic test (internal obligation, during writing). M's Verifier checks cells after writing via two independent checks (Judge-standard check + skeptic-test check). B enforces phase ordering via named tokens. Four enforcement forces on evidence quality across three orthogonal axes: role-based (G+M), sequential gate (B), and rhetorical self-accountability (N). The Verifier in this design applies both the Judge standard and the skeptic test, making C-16's post-write check dual-mechanism. Tests whether N adds measurable value on top of G+B+M or is redundant.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The final scorecard includes a ranked leaderboard, excellence
signals, failure patterns, and regression signals.

---

ROLE STRUCTURE AND PHASE GATES

Three roles complete this task in strict sequence. Each role produces a named
gate token that the next role requires as its input.

  ROLE 1: JUDGE     Produces: JUDGE STANDARD COMPLETE
  ROLE 2: ANALYST   Requires: JUDGE STANDARD COMPLETE | Produces: ANALYST COMPLETE
  ROLE 3: VERIFIER  Requires: ANALYST COMPLETE        | Produces: VERIFIER AUDIT COMPLETE

Gate rules (hard):
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Synthesis cannot begin without VERIFIER AUDIT COMPLETE present above.
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
  What separates them: [one sentence — the specific property that makes the ACCEPTABLE
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

For each output, produce a scoring table:

  Output: [output identifier]

  | ID | Criterion | Weight | Verdict | Evidence |
  |----|-----------|--------|---------|----------|
  | C-01 | [name] | E | PASS/PARTIAL/FAIL | [evidence: Check A cleared,
  |      |         |   |                   | Check B cleared] |
  ...

  No row may be skipped. No evidence cell may be blank.

  For any PARTIAL verdict, add a one-sentence diagnostic below the table row:
    C-[NN] diagnostic: [specific design property in this output that produced PARTIAL —
    what is present that prevented FAIL, and what is absent that prevented PASS]

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

Apply two independent checks to each evidence cell written by the Analyst:

  CHECK A — Judge standard: Does this evidence cell resemble the UNACCEPTABLE pattern
             the Judge defined for this criterion?
  CHECK B — Skeptic test: Could a reader who has NOT read this specific output identify
             it from this evidence alone, without modification?

Produce a per-output dual-check audit table:

  Output: [output identifier] — Post-write Evidence Audit

  | ID | Evidence excerpt (first 15 words) | Check A | Check B | Status   |
  |----|----------------------------------|---------|---------|----------|
  | C-01 | [excerpt] | PASS | PASS | ACCEPTED |
  | C-02 | [excerpt] | PASS | FAIL | REJECTED |
  ...

For any cell where Check A or Check B fails:
  FLAG: [output ID] / [criterion ID] — CHECK [A/B] FAILED: [specific reason]

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

| Variation | Axes | Key mechanism | C-15 pred | C-16 pred | C-11 pred |
|-----------|------|---------------|-----------|-----------|-----------|
| V-01 | M | Post-write Verifier (single-role-sequence axis) | PASS | PASS | PARTIAL — role pre-condition present; gate between Analyst and Verifier is single transition, not full gate system |
| V-02 | N | Skeptic-proof framing (phrasing register only) | FAIL | FAIL | FAIL |
| V-03 | O | Phase proportion + annotation blocks (lifecycle) | FAIL | FAIL | FAIL |
| V-04 | G+B+M | Judge-first + gates + post-write Verifier | PASS | PASS | PASS |
| V-05 | G+B+M+N | V-04 + skeptic framing inside Analyst | PASS | PASS | PASS |

Spread design: V-02 and V-03 are structurally single-mechanism designs that cannot
satisfy the multi-mechanism aspirational criteria. They provide the low-scoring
contrast required to generate excellence signals and confirm the rubric's diagnostic
accuracy. V-01 tests whether the Verifier role alone (without G's pre-conditioning)
is sufficient for C-15 -- it is not, because without JUDGE STANDARD COMPLETE as an
input requirement, the Analyst has no external standard to check against. V-04 is
the minimum sufficient combination. V-05 tests whether N adds value on top.
