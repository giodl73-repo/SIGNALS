# Quest Score -- Round 12 Variations
**Skill**: quest-score
**Rubric**: v8 (N_essential=5, N_recommended=3, N_aspirational=15)
**Date**: 2026-03-15
**Round**: 12

---

## Design logic

### Unachieved ceiling entering R12

R11 was scored against rubric v7 (N_aspirational=13). Rubric v8 adds C-22 and C-23,
bumping N_aspirational to 15. Denominator changes from 13 to 15.

Reconstructed gap map for R11 variations under v8 scoring:

| Variation | C-08 | C-11 | C-12 | C-20 | C-22 | C-23 | Composite (v8 ceiling) |
|-----------|------|------|------|------|------|------|------------------------|
| R11 V-01 | FAIL | PASS | PASS | PARTIAL | PARTIAL | FAIL | ~86 |
| R11 V-02 | PASS | PASS | PASS | PARTIAL | PARTIAL | FAIL | ~93 |
| R11 V-03 | PASS | PASS | PASS | PARTIAL | PARTIAL | FAIL | ~93 |
| R11 V-04 | FAIL | PASS | PASS | PASS | PASS | FAIL | ~89 |
| R11 V-05 | PASS | PASS | PASS | PASS | PARTIAL | PASS | ~97 |

No R11 variation achieves both C-22 PASS and C-23 PASS simultaneously under v8.

C-22 mechanism analysis: R11 V-04's IMPROVEMENT-ANALYST sub-step protocol declared
"a structural violation declared for non-traceable suggestions" as a gate. This
satisfies C-20 at PASS. C-22 asks whether this gate is an **explicit named declaration**
("a suggestion that cannot be traced to a pass condition is a structural violation")
vs. a behavioral gate embedded in the step sequence. V-04's wording was protocol-
embedded, not a standalone named violation class declaration. Scored PASS for C-20;
PARTIAL for C-22 (gate exists structurally but not declared as a named violation class).

C-23 mechanism analysis: R11 V-05 added a "How derived" column to the IMPROVEMENT
TABLE schema. This is the direct C-23 mechanism. No other R11 variation included this
column. V-04 achieved C-22 via gate without the column; V-05 achieved C-23 via column
without a standalone violation gate declaration. V-05 gets PARTIAL on C-22 because
the schema's "how derived" column enforces traceability via schema compliance, not via
a named violation class declaration -- the column audit catches a missing derivation
but no instruction declares that a non-traceable suggestion is a structural violation.

### R12 axes

| Axis | Label | Mechanism |
|------|-------|-----------|
| A | Improvement Auditor role | New IMPROVEMENT AUDITOR phase runs between ENFORCEMENT AUDITOR and SYNTHESIS. It declares the violation gate by name (C-22) and emits the IMPROVEMENT TABLE schema with "How derived" column (C-23). SYNTHESIS gate requires IMPROVEMENT REGISTER COMPLETE. |
| B | Schema-first with derivation enforcement | OUTPUT SCHEMA DECLARATION includes IMPROVEMENT TABLE with "How derived" as required column. Schema preamble contains the violation gate declaration inline: "Any suggestion whose How-derived cell cannot be traced to the verbatim pass condition text is a structural violation." |
| C | Lifecycle phase gate | Explicit Phase 6 (Improvement Generation) with a named checkpoint: VIOLATION GATE DECLARED must appear as an output before improvement notes are written. The checkpoint requires emitting the gate declaration as a distinct labeled artifact. |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (A)**: Improvement Auditor role. Inherits enforcement auditor from V-01 R11.
  Adds IMPROVEMENT AUDITOR between ENFORCEMENT AUDITOR and SYNTHESIS. The role
  declares the violation gate explicitly and emits IMPROVEMENT TABLE with "How derived".
  Predicts: C-22 PASS (named violation class declaration in role domain), C-23 PASS
  (schema column), C-08 FAIL (no CRITERION SUMMARY TABLE step), C-11 PASS (enforcement
  auditor), C-12 PASS (enforcement auditor), C-20 PASS (structural derivation in role).

- **V-02 (B)**: Schema-first declaration. Inherits V-02 R11 schema structure.
  Extends OUTPUT SCHEMA DECLARATION with v8 IMPROVEMENT TABLE (adds "How derived" +
  violation gate inline in schema preamble). CRITERION SUMMARY TABLE retained from
  V-02 R11. ENFORCEMENT ANALYSIS TABLE retained.
  Predicts: C-08 PASS, C-11 PASS, C-12 PASS, C-22 PASS (schema preamble gate), C-23
  PASS ("How derived" column required), C-20 PASS. Maximum composite attempt without
  role-sequence addition.

- **V-03 (C)**: Phase-gate lifecycle. Inherits V-03 R11 sub-role decomposition.
  Adds VIOLATION GATE DECLARED as a named Phase 5b checkpoint before IMPROVEMENT-ANALYST
  fires. The checkpoint must emit a standalone labeled artifact. IMPROVEMENT-ANALYST
  entry condition is VIOLATION GATE DECLARED.
  Predicts: C-22 PASS (standalone labeled artifact), C-23 PASS (schema in
  IMPROVEMENT-ANALYST domain), C-08 PASS (PATTERN-ANALYST domain), C-11 PASS,
  C-12 PASS, C-20 PASS.

### Combination selection rationale

- **V-04 (A + Inertia)**: Improvement Auditor role + inertia framing. Combines the
  IMPROVEMENT AUDITOR role (Axis A) with explicit named inertia framing: the NAIVE
  PATTERN (FORBIDDEN) is declared before IMPROVEMENT AUDITOR instructions fire. The
  violation gate (C-22) and derivation column (C-23) emerge as the structural answer
  to the named forbidden pattern.
  Predicts: C-22 PASS (named forbidden + gate together), C-23 PASS (schema column),
  C-08 FAIL (no CRITERION SUMMARY step), C-11 PASS, C-12 PASS, C-20 PASS.

- **V-05 (B + formal FORBIDDEN blocks)**: Schema-first with FORBIDDEN declarations
  embedded in each schema definition. The IMPROVEMENT TABLE schema declaration contains
  two FORBIDDEN lines making C-22/C-23 violations explicitly labeled and independently
  auditable. Inherits all V-02 mechanisms.
  Predicts: C-08 PASS, C-11 PASS, C-12 PASS, C-22 PASS (FORBIDDEN as named violation),
  C-23 PASS ("How derived" column), C-20 PASS. Maximum composite attempt.

---

## V-01 -- Axis A: Improvement Auditor role (new phase between ENFORCEMENT AUDITOR and SYNTHESIS)

**Variation axis**: Role sequence -- a named IMPROVEMENT AUDITOR phase runs after
ENFORCEMENT REGISTER COMPLETE and before SYNTHESIS. It declares the violation gate
by name (satisfying C-22) and emits the IMPROVEMENT TABLE with a "How derived"
column (satisfying C-23). The SYNTHESIS gate requires IMPROVEMENT REGISTER COMPLETE
in addition to the existing three tokens.

**Hypothesis**: When the violation gate declaration (C-22) and the derivation field
schema (C-23) are embedded in SYNTHESIS as behavioral reminders, the model can produce
improvement notes without the gate being a named structural constraint. Promoting
improvement generation to a dedicated named phase makes the violation gate a
protocol-entry declaration that must appear before any improvement note is written --
not a tone-setter for a behavioral step. C-23 is satisfied by the role's domain
declaration that the "How derived" column is a required schema field, making its
absence a domain violation detectable at role-boundary inspection.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role                | Requires                                                                                                                              | Produces                       | Domain (ONLY)                                                                                                                                             | Cannot Check                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| SCANNER             | (none)                                                                                                                                | SCANNER COMPLETE               | Pre-scan divergence; SPREADER SPREAD TABLE; SCAN IMPORT DECLARATION                                                                                        | Scoring verdicts, evidence quality, content specificity                               |
| ANALYST             | SCANNER COMPLETE                                                                                                                      | ANALYST COMPLETE               | Per-criterion verdicts; evidence; composite; golden; Present_mechanism / Absent_mechanism                                                                  | Pre-scan (Scanner domain), format auditing (Verifier domain)                          |
| VERIFIER            | ANALYST COMPLETE                                                                                                                      | VERIFIER AUDIT COMPLETE        | Format presence: evidence non-genericity; PARTIAL column non-emptiness; per-cell portability ACCEPTED/REJECTED verdict                                     | Content quality of diagnostic cells (Confirmer domain)                                |
| CONFIRMER           | VERIFIER AUDIT COMPLETE                                                                                                               | CONFIRMATION COMPLETE          | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                       | Format presence (Verifier domain), scoring verdicts (Analyst domain)                  |
| ENFORCEMENT AUDITOR | CONFIRMATION COMPLETE                                                                                                                 | ENFORCEMENT REGISTER COMPLETE  | Two-layer enforcement detection; asymmetric enforcement detection across all scored variations                                                              | Scoring verdicts (Analyst), evidence quality (Verifier), content depth (Confirmer)    |
| IMPROVEMENT AUDITOR | ENFORCEMENT REGISTER COMPLETE                                                                                                         | IMPROVEMENT REGISTER COMPLETE  | Violation gate declaration; IMPROVEMENT TABLE production; derivation-field schema enforcement                                                               | Enforcement patterns (Enforcement Auditor domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS           | VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND ENFORCEMENT REGISTER COMPLETE AND IMPROVEMENT REGISTER COMPLETE (all four independently) | (terminal output)         | Leaderboard; excellence signals; failure patterns; regression signals                                                                                      | Re-scoring; re-auditing; enforcement re-inspection; improvement re-generation         |

Gate rules (hard):
  - ANALYST cannot begin without SCANNER COMPLETE present above.
  - VERIFIER cannot begin without ANALYST COMPLETE present above.
  - CONFIRMER cannot begin without VERIFIER AUDIT COMPLETE present above.
  - ENFORCEMENT AUDITOR cannot begin without CONFIRMATION COMPLETE present above.
  - IMPROVEMENT AUDITOR cannot begin without ENFORCEMENT REGISTER COMPLETE present above.
  - SYNTHESIS cannot begin without ALL FOUR tokens present above independently:
    VERIFIER AUDIT COMPLETE, CONFIRMATION COMPLETE, ENFORCEMENT REGISTER COMPLETE,
    IMPROVEMENT REGISTER COMPLETE.
    A missing IMPROVEMENT REGISTER COMPLETE blocks SYNTHESIS even if the other three
    tokens are present.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: SCANNER

Domain: Pre-scan divergence prediction; SPREADER SPREAD TABLE; SCAN IMPORT
DECLARATION (see manifest).

Read all N outputs and the rubric. Do not score any criterion yet.

Step 1 -- Produce the SPREADER SPREAD TABLE:

  SPREADER SPREAD TABLE

  | Criterion | Divergence? | Outputs predicted to split | Structural reason for divergence        |
  |-----------|-------------|----------------------------|-----------------------------------------|
  | C-01      | YES / NO    | [output IDs or all same]   | [specific structural mechanism or N/A]  |
  ...one row per rubric criterion (C-01 through C-23)...

  Rules:
  - Every rubric criterion must have a row. A blank row is a structural gap.
  - Divergence? = YES only if a specific structural mechanism in one or more
    outputs is expected to produce a different verdict relative to peers.
  - Structural reason must name the design property (gate token, table column,
    declaration label, schema entry, phase name), not describe the criterion.
  - If no divergence is predicted, enter NO and N/A -- do not leave cells blank.

Step 2 -- Immediately after the SPREADER SPREAD TABLE, produce the SCAN IMPORT
DECLARATION:

  SCAN IMPORT DECLARATION

  This declaration is a synthesis contract governing how SYNTHESIS may derive
  verdict-split excellence signal claims.

  (a) All verdict-split excellence signal claims in SYNTHESIS are structurally
      derived from the SPREADER SPREAD TABLE above. A claim is structurally
      derived if it cites a specific row (criterion + structural reason) from
      the table. A claim that cannot be traced to a specific table row is
      prohibited.

  (b) Retroactive inference from verdict tallies is prohibited. SYNTHESIS may
      not construct verdict-split excellence signals by comparing verdict counts
      after scoring completes. Verdict tallies may confirm a signal identified
      in the table, but may not originate one.

SCANNER COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cells; composite; Present_mechanism and
Absent_mechanism columns (see manifest).
Do not begin until SCANNER COMPLETE appears above.

DENOMINATOR GUARD -- read before scoring any output:

  N/A resolution rules:
    C-09: Prior-round data present? YES => score normally. NO => N/A = PASS.
    C-10: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-11: Symmetric enforcement on C-01/C-02? YES => N/A = PASS. NO => fires.
    C-12: Any variation uses two-layer enforcement? NO => N/A = PASS. YES => fires.
    C-13: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
    C-14: NO N/A CONDITION. C-14 fires unconditionally for every run.
    C-15: Any aspirational criteria resolve to N/A = PASS? YES => fires. NO => N/A = PASS.
    C-16: NO N/A CONDITION. C-16 fires unconditionally for every run.
    C-17: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-18: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
    C-19: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-20: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-21: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-22: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-23: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.

  Aspirational denominator: ALWAYS 15. N/A = PASS criteria count as 1 in the
  numerator. The denominator does NOT change.

  CORRECT form:    aspirational_pass / 15 * 10
  PROHIBITED form: aspirational_pass / N_resolved * 10   [denominator-shrinkage error]

  C-14 anti-exemption: C-14 has NO N/A = PASS condition. It fires unconditionally
  every run, regardless of how many other aspirational criteria resolve to N/A = PASS.
  There is no run configuration in which C-14 is exempt.

For each output, produce a scoring table:

  Output: [output identifier]

  | ID   | Criterion                                            | Wt | Verdict           | Evidence                                             | Present_mechanism | Absent_mechanism |
  |------|------------------------------------------------------|----|-------------------|------------------------------------------------------|-------------------|------------------|
  | C-01 | Per-criterion verdicts present                       | E  | PASS/PARTIAL/FAIL  | [grounded in this output -- not portable to others]  | --                | --               |
  | C-02 | Evidence quotes are grounded                         | E  | ...               | ...                                                  | ...               | ...              |
  | C-03 | Composite score computed correctly                   | E  | ...               | ...                                                  | ...               | ...              |
  | C-04 | Ranked leaderboard present                           | E  | ...               | ...                                                  | ...               | ...              |
  | C-05 | Golden threshold applied                             | E  | ...               | ...                                                  | ...               | ...              |
  | C-06 | Failure patterns identified                          | R  | ...               | ...                                                  | ...               | ...              |
  | C-07 | Excellence signals identified                        | R  | ...               | ...                                                  | ...               | ...              |
  | C-08 | Per-criterion verdict summary table                  | R  | ...               | ...                                                  | ...               | ...              |
  | C-09 | Regression signals identified                        | A  | ...               | ...                                                  | ...               | ...              |
  | C-10 | Actionable improvement note per failing output       | A  | ...               | ...                                                  | ...               | ...              |
  | C-11 | Asymmetric enforcement diagnosed                     | A  | ...               | ...                                                  | ...               | ...              |
  | C-12 | Two-layer enforcement recognized                     | A  | ...               | ...                                                  | ...               | ...              |
  | C-13 | Evidence portability verified                        | A  | ...               | ...                                                  | ...               | ...              |
  | C-14 | N/A denominator explicitly guarded                  | A  | ...               | ...                                                  | ...               | ...              |
  | C-15 | Denominator proof with anti-pattern shown            | A  | ...               | ...                                                  | ...               | ...              |
  | C-16 | C-14 no-N/A exemption declared                       | A  | ...               | ...                                                  | ...               | ...              |
  | C-17 | Excellence signals pre-scanned structurally          | A  | ...               | ...                                                  | ...               | ...              |
  | C-18 | Per-cell portability verdict column                  | A  | ...               | ...                                                  | ...               | ...              |
  | C-19 | Synthesis contract explicitly declared               | A  | ...               | ...                                                  | ...               | ...              |
  | C-20 | Structural improvement generation                    | A  | ...               | ...                                                  | ...               | ...              |
  | C-21 | Synthesis contract clauses individually labeled      | A  | ...               | ...                                                  | ...               | ...              |
  | C-22 | Improvement derivation violation gate declared       | A  | ...               | ...                                                  | ...               | ...              |
  | C-23 | Improvement table schema includes derivation field   | A  | ...               | ...                                                  | ...               | ...              |

  Column rules:
    - Evidence: must be grounded in this specific output. Before writing, ask:
      "Could this evidence apply to a different output with no modification?"
      If YES, rewrite until it uniquely identifies this output.
    - Present_mechanism: for PARTIAL only -- name the specific structural element
      present that prevented FAIL. Enter -- for PASS and FAIL.
    - Absent_mechanism: for PARTIAL only -- name the specific structural element
      absent that prevented PASS. Enter -- for PASS and FAIL.
    - A blank Present_mechanism or Absent_mechanism on a PARTIAL row is a
      structural violation equivalent to a blank evidence cell.
    - No row may be skipped.

  Composite computation:
    essential_pass    = [count of C-01..C-05 PASS; PARTIAL = 0.5]
    recommended_pass  = [count of C-06..C-08 PASS; PARTIAL = 0.5]
    aspirational_pass = [count of C-09..C-23 PASS or N/A=PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)
              = [result]

    Golden: YES -- all 5 essentials PASS AND composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- evidence cell non-genericity; PARTIAL column
non-emptiness; per-cell portability (see manifest).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A -- Evidence quality: For each evidence cell, compare against the criterion
pass condition. Reject any cell that:
  (a) could apply to a different output without modification, OR
  (b) restates the criterion name or verdict rather than citing evidence.

AUDIT B -- Diagnostic column presence: PARTIAL verdicts only.
  (i)  Present_mechanism: must be non-empty (not -- or blank)
  (ii) Absent_mechanism: must be non-empty (not -- or blank)
  Mark n/a for PASS and FAIL rows.

AUDIT C -- Per-cell portability: For every evidence cell, produce an explicit
ACCEPTED/REJECTED verdict:
  ACCEPTED -- evidence uniquely identifies this output; could not apply
              unchanged to a peer output.
  REJECTED -- evidence is portable; must be rewritten before row is accepted.

Produce combined audit output per output:

  Output: [output identifier] -- Verifier Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Audit C  | Row status |
  |------|---------|-----------------------------------|---------|---------|----------|------------|
  | C-01 | PASS    | [excerpt]                         | PASS    | n/a     | ACCEPTED | ACCEPTED   |

  Row status = ACCEPTED only when all applicable audits are PASS or ACCEPTED.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B/C]: [specific reason]

Flagged items must be corrected and re-audited. Only flagged items are reopened.

When all rows are ACCEPTED across all N outputs:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells
name specific structural properties? (see manifest).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

For each PARTIAL verdict, produce a content challenge row:

  Output: [output identifier] -- Confirmer Audit

  | Criterion | Present_mechanism (first 15 words) | Specific? | Absent_mechanism (first 15 words) | Specific? | Status               |
  |-----------|-------------------------------------|-----------|-----------------------------------|-----------|----------------------|
  | C-[NN]    | [verbatim excerpt]                  | YES / NO  | [verbatim excerpt]                | YES / NO  | CONFIRMED/CHALLENGED |

  Specific = YES: names a specific structural element, mechanism, role, gate
             token, or design gap by name.
  Specific = NO: uses a criterion label, a generic quality phrase, or restates
             the verdict.

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim]" -- [specific reason it fails the specificity test]
    Absent:  "[verbatim]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten and re-audited. Only challenged items reopened.

When all PARTIAL diagnostics are CONFIRMED:
CONFIRMATION COMPLETE

---

ROLE 5: ENFORCEMENT AUDITOR

Domain: Two-layer enforcement detection; asymmetric enforcement detection across
all scored variations (see manifest).
Do not begin until CONFIRMATION COMPLETE appears above.

Inspect each scored variation's prompt body for the following patterns:

Part A -- Two-layer enforcement detection:
  A variation uses two-layer enforcement on a criterion when it applies BOTH:
    Layer 1 (positive instruction): a directive to produce a specific output
      in a specific form.
    Layer 2 (structural gate): a constraint that makes Layer 1 non-compliance
      structurally visible (e.g., a schema declaration with "blank = structural
      violation", a FORBIDDEN prohibitive, a completion-token dependency that
      blocks the next phase).
  A single positive instruction without a gate is single-layer.

Part B -- Asymmetric enforcement detection:
  A variation has asymmetric enforcement when it enforces C-01 (completeness --
  every criterion has a verdict) and C-02 (evidence grounding -- each verdict
  has output-specific evidence) at different enforcement levels: one enforced by
  a structural mechanism (schema declaration, gate token, audit role), the other
  enforced only by a behavioral instruction or left unaddressed.

Produce the ENFORCEMENT PATTERN REGISTER:

  ENFORCEMENT PATTERN REGISTER

  Two-layer sub-table:
  | Output | Two-layer detected? | Criterion | Layer 1 (instruction excerpt)                | Layer 2 (gate or constraint name)      | Stronger because                          |
  |--------|---------------------|-----------|----------------------------------------------|----------------------------------------|-------------------------------------------|
  | [ID]   | YES / NO            | [C-NN]    | [first 12 words of instruction or N/A]       | [gate mechanism name or N/A]           | [one sentence or N/A]                     |
  ...one row per scored output...

  Asymmetry sub-table:
  | Output | Asymmetric detected? | Strongly enforced criterion | Enforcement mechanism             | Weakly/un-enforced criterion | Missing enforcement mechanism          |
  |--------|---------------------|-----------------------------|------------------------------------|------------------------------|----------------------------------------|
  | [ID]   | YES / NO            | [C-NN or N/A]               | [mechanism type or N/A]            | [C-NN or N/A]                | [what would close the gap, or N/A]     |
  ...one row per scored output...

  Rules:
  - Every scored output must appear in each sub-table.
  - Two-layer detected? = YES only if BOTH a positive instruction AND a distinct
    structural gate are present for the same criterion.
  - Asymmetric detected? = YES only if enforcement mechanisms differ in kind
    (structural vs. behavioral, or addressed vs. unaddressed) between C-01 and C-02.
  - A blank row is a structural gap equivalent to a missing criterion row in ANALYST.

ENFORCEMENT REGISTER COMPLETE

---

ROLE 6: IMPROVEMENT AUDITOR

Domain: Violation gate declaration; IMPROVEMENT TABLE production with derivation
field schema (see manifest).
Do not begin until ENFORCEMENT REGISTER COMPLETE appears above.

This role has three responsibilities:

Step 6a -- VIOLATION GATE DECLARATION:

  Emit the following named gate before producing any improvement notes:

  VIOLATION GATE: Any improvement suggestion that cannot be traced to the verbatim
  text of its source criterion's pass condition is a structural violation. A
  suggestion composed by reading the criterion name or the output's failing area,
  without deriving content from the quoted pass condition, is not a behavioral
  shortfall -- it is a structural violation of the derivation requirement. Do not
  emit such a suggestion.

Step 6b -- Determine which outputs require improvement notes:

  If all outputs are golden: emit "All outputs golden; IMPROVEMENT TABLE not required."
  and proceed to IMPROVEMENT REGISTER COMPLETE.

  If any non-golden output exists: continue to Step 6c.

Step 6c -- Produce the IMPROVEMENT TABLE:

  Schema: The IMPROVEMENT TABLE must include the following columns exactly.
  A table that omits any column, or uses a different column name, is a structural
  schema violation.

  IMPROVEMENT TABLE

  | Output | Lowest essential | Verdict | Pass condition (quoted verbatim) | Suggestion | How derived |
  |--------|-----------------|---------|----------------------------------|------------|-------------|
  | [ID]   | C-[NN]          | FAIL/PARTIAL | "[verbatim pass condition from rubric]" | [suggestion text] | [specific step in pass condition that the suggestion satisfies] |

  Column definitions:
    Lowest essential: the C-01..C-05 criterion with the lowest verdict
      (FAIL < PARTIAL < PASS) for this non-golden output.
    Pass condition (quoted verbatim): the exact text of the pass condition
      from the rubric for the lowest-essential criterion. Must be a direct quote,
      not a paraphrase.
    Suggestion: the improvement the output would need to make. Must be derived
      from -- not merely consistent with -- the quoted pass condition text.
    How derived: the specific phrase or clause within the quoted pass condition
      that the suggestion addresses. Example: "derived from 'direct quote or a
      specific reference to the output being evaluated' in C-02 pass condition."
      A cell that reads "general derivation" or "from pass condition" without
      naming the specific phrase does not satisfy the derivation-field requirement.

  Violation check: After completing each row, verify:
    Is the suggestion traceable to a specific phrase in the "Pass condition
    (quoted verbatim)" cell? If NO, the suggestion is a structural violation
    under the VIOLATION GATE declared in Step 6a. Rewrite or remove it.

IMPROVEMENT REGISTER COMPLETE

---

SYNTHESIS

Do not begin until ALL FOUR tokens appear above independently:
  - VERIFIER AUDIT COMPLETE
  - CONFIRMATION COMPLETE
  - ENFORCEMENT REGISTER COMPLETE
  - IMPROVEMENT REGISTER COMPLETE

Missing any single token blocks SYNTHESIS.

LEADERBOARD

Rank all outputs by composite score descending. Ties broken by output ID ascending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

Two signal sources apply. Both must be checked.

Source 1 -- Verdict-split signals (governed by SCAN IMPORT DECLARATION clause (a)):
  For each criterion where SPREADER TABLE shows Divergence? = YES, confirm whether
  the split materialized in verdicts. For confirmed splits:
    Signal: [output ID] -- [criterion ID] -- [structural reason from SPREADER TABLE row]

Source 2 -- Enforcement-pattern signals (derived from ENFORCEMENT PATTERN REGISTER):
  Two-layer: for each output where Two-layer detected? = YES in the register:
    Two-layer: [output ID] -- [criterion ID] -- Layer 1: [instruction excerpt] --
    Layer 2: [gate name] -- Stronger because: [from register]
  Asymmetric: for each output where Asymmetric detected? = YES in the register:
    Asymmetry: [output ID] -- enforces [strongly enforced criterion] via
    [enforcement mechanism] -- [weakly/un-enforced criterion] has no equivalent
    structural enforcement -- missing mechanism: [from register]

If neither source yields any signal: "No excellence signals in this round."

FAILURE PATTERNS

For each criterion where every output scored PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round data is available: identify any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed.

If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-02 -- Axis B: Schema-first declaration with IMPROVEMENT TABLE derivation enforcement

**Variation axis**: Output format -- the OUTPUT SCHEMA DECLARATION is updated for v8
to include the IMPROVEMENT TABLE schema with "How derived" as a required named column.
The schema preamble declares the violation gate inline: absence of a traceable
"How derived" cell is a structural schema violation. Inherits CRITERION SUMMARY TABLE,
ENFORCEMENT ANALYSIS TABLE, and all other schema entries from V-02 R11.

**Hypothesis**: V-02 R11 showed that schema-declaring a deliverable before scoring
begins makes its absence a detectable structural gap checkable without content
interpretation. The same mechanism extended to C-22/C-23: if the IMPROVEMENT TABLE
schema declares "How derived" as a required column AND the preamble declares that any
untraceable suggestion is a structural violation, then C-22 and C-23 are both
independently column-auditable before synthesis executes. The schema preamble
declaration is the named violation class (C-22); the required column is the derivation
field (C-23). A scorer following the schema cannot write improvement notes without
both properties being structurally enforced.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

OUTPUT SCHEMA DECLARATION

The following schemas are declared before any scoring begins. Every section must
conform to its declared schema. A section using prose instead of its declared
table format, or omitting a required table, is a structural violation.

| Section                       | Table name                   | Required columns                                                                                                                                                            |
|-------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-scan divergence           | SPREADER SPREAD TABLE        | Criterion / Divergence? / Outputs predicted to split / Structural reason                                                                                                    |
| Synthesis contract            | SCAN IMPORT DECLARATION      | Clause ID / Property declared / Enforcement rule                                                                                                                            |
| Per-output scoring            | SCORING TABLE                | ID / Criterion / Wt / Verdict / Evidence / Present_mechanism / Absent_mechanism / PORTABILITY                                                                               |
| Per-criterion summary         | CRITERION SUMMARY TABLE      | Criterion / PASS count / PARTIAL count / FAIL count / N/A count                                                                                                             |
| Enforcement analysis          | ENFORCEMENT ANALYSIS TABLE   | Output / Two-layer? / Two-layer criterion / Layer 1 instruction / Layer 2 gate / Asymmetric? / Covered criterion / Coverage mechanism / Uncovered criterion / Missing mechanism |
| Improvement notes             | IMPROVEMENT TABLE            | Output / Lowest essential / Verdict / Pass condition (quoted verbatim) / Suggestion / How derived                                                                           |
| Failure patterns              | FAILURE PATTERN TABLE        | Criterion / Criterion name / All-output verdict / Diagnosis type / Diagnosis                                                                                                |
| Excellence signals            | EXCELLENCE SIGNAL TABLE      | Source / Output / Criterion / Structural reason / Confirmed?                                                                                                                |
| Regression signals            | REGRESSION TABLE             | Output / Criterion / Prior verdict / Current verdict / What changed                                                                                                         |
| Leaderboard                   | LEADERBOARD TABLE            | Rank / Output / Composite / Golden?                                                                                                                                         |

IMPROVEMENT TABLE enforcement rules (applies to all non-golden outputs):

  (1) VIOLATION GATE: Any improvement suggestion whose "How derived" cell cannot
      be traced to a specific phrase within the quoted verbatim pass condition of
      the same row is a structural violation. A suggestion that is merely
      consistent with the criterion, or is composed from knowledge of the criterion
      name, is not structurally derived and is a violation.

  (2) "How derived" column requirement: Every improvement row must name the specific
      phrase or clause within the quoted pass condition from which the suggestion
      is derived. A cell containing "general observation", "N/A", or a paraphrase
      of the pass condition does not satisfy this requirement.

  (3) A blank "How derived" cell is a structural schema violation equivalent to a
      blank evidence cell in the SCORING TABLE.

A blank cell in any required column of any declared table is a structural violation.

---

DENOMINATOR GUARD -- read before any scoring begins:

N/A resolution rules:
  C-09: Prior-round data present? YES => score. NO => N/A = PASS.
  C-10: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
  C-11: All variations symmetric on C-01/C-02 enforcement? YES => N/A = PASS. NO => fires.
  C-12: Any variation uses two-layer enforcement? NO => N/A = PASS. YES => fires.
  C-13: N > 1? YES => fires. N = 1 => N/A = PASS.
  C-14: NO N/A CONDITION. Fires unconditionally every run.
  C-15: Any aspirational criteria resolve to N/A = PASS? YES => fires. NO => N/A = PASS.
  C-16: NO N/A CONDITION. Fires unconditionally every run.
  C-17: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-18: N > 1? YES => fires. N = 1 => N/A = PASS.
  C-19: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-20: Any non-golden outputs? YES => fires. NO => N/A = PASS.
  C-21: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-22: Any non-golden outputs? YES => fires. NO => N/A = PASS.
  C-23: Any non-golden outputs? YES => fires. NO => N/A = PASS.

Aspirational denominator: ALWAYS 15. N/A = PASS criteria count as 1 in numerator.

  CORRECT form:    aspirational_pass / 15 * 10
  PROHIBITED form: aspirational_pass / N_resolved * 10   [denominator-shrinkage error]

C-14 anti-exemption: C-14 has NO N/A = PASS condition. It fires unconditionally
in every run, regardless of how many other aspirational criteria resolve to N/A = PASS.

---

STEP 1 -- PRE-SCAN

Read all N outputs and the rubric. Do not score any criterion yet.

Produce the SPREADER SPREAD TABLE (one row per criterion, C-01 through C-23):

  SPREADER SPREAD TABLE

  | Criterion | Divergence? | Outputs predicted to split | Structural reason                      |
  |-----------|-------------|----------------------------|----------------------------------------|
  | C-01      | YES / NO    | [IDs or all same]          | [named design property or N/A]         |
  ...

  No criterion may be omitted. Blank structural reason on a NO row: enter N/A.

Immediately after, produce the SCAN IMPORT DECLARATION:

  SCAN IMPORT DECLARATION

  | Clause ID | Property declared                                                                                                                    | Enforcement rule                                                                               |
  |-----------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
  | (a)       | All verdict-split excellence signal claims in the EXCELLENCE SIGNAL TABLE are structurally derived from a specific SPREADER TABLE row | A claim without a traceable SPREADER TABLE row (criterion + structural reason) is prohibited.  |
  | (b)       | Retroactive inference from verdict tallies is prohibited. SYNTHESIS may not construct verdict-split signals by comparing verdict counts | Verdict tallies may confirm a signal from the table but may not originate one.                 |

---

STEP 2 -- SCORING

For each output, produce a SCORING TABLE conforming to the declared schema:

  Output: [output identifier]

  SCORING TABLE

  | ID   | Criterion                                            | Wt | Verdict           | Evidence                          | Present_mechanism | Absent_mechanism | PORTABILITY |
  |------|------------------------------------------------------|----|-------------------|-----------------------------------|-------------------|------------------|-------------|
  | C-01 | Per-criterion verdicts present                       | E  | PASS/PARTIAL/FAIL  | [evidence unique to this output]  | --                | --               | ACCEPTED    |
  | C-02 | Evidence quotes are grounded                         | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-03 | Composite score computed correctly                   | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-04 | Ranked leaderboard present                           | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-05 | Golden threshold applied                             | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-06 | Failure patterns identified                          | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-07 | Excellence signals identified                        | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-08 | Per-criterion verdict summary table                  | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-09 | Regression signals identified                        | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-10 | Actionable improvement note per failing output       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-11 | Asymmetric enforcement diagnosed                     | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-12 | Two-layer enforcement recognized                     | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-13 | Evidence portability verified                        | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-14 | N/A denominator explicitly guarded                  | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-15 | Denominator proof with anti-pattern shown            | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-16 | C-14 no-N/A exemption declared                       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-17 | Excellence signals pre-scanned structurally          | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-18 | Per-cell portability verdict column                  | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-19 | Synthesis contract explicitly declared               | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-20 | Structural improvement generation                    | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-21 | Synthesis contract clauses individually labeled      | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-22 | Improvement derivation violation gate declared       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-23 | Improvement table schema includes derivation field   | A  | ...               | ...                               | ...               | ...              | ...         |

  PORTABILITY column: ACCEPTED = evidence uniquely identifies this output.
  REJECTED = portable; must be rewritten before entering ACCEPTED.
  Blank = structural violation.

  Present_mechanism / Absent_mechanism: PARTIAL rows only; PASS and FAIL: enter --.
  Blank cells on PARTIAL rows are structural violations.

  Composite computation:
    essential_pass    = [count C-01..C-05 PASS; PARTIAL = 0.5]
    recommended_pass  = [count C-06..C-08 PASS; PARTIAL = 0.5]
    aspirational_pass = [count C-09..C-23 PASS or N/A=PASS; PARTIAL = 0.5]
                        denominator = 15 always

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)
              = [result]

    Golden: YES -- all 5 essentials PASS AND composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

---

STEP 3 -- CRITERION SUMMARY

After scoring all N outputs, produce the CRITERION SUMMARY TABLE:

  CRITERION SUMMARY TABLE

  | Criterion | PASS count | PARTIAL count | FAIL count | N/A count |
  |-----------|------------|---------------|------------|-----------|
  | C-01      | [n]        | [n]           | [n]        | [n]       |
  ...one row per criterion C-01 through C-23...

---

STEP 4 -- ENFORCEMENT ANALYSIS

Inspect each scored variation's prompt body for enforcement patterns. Produce
the ENFORCEMENT ANALYSIS TABLE conforming to the declared schema:

  ENFORCEMENT ANALYSIS TABLE

  | Output | Two-layer? | Two-layer criterion | Layer 1 instruction (first 12 words)    | Layer 2 gate / constraint name           | Asymmetric? | Covered criterion | Coverage mechanism  | Uncovered criterion | Missing mechanism                    |
  |--------|------------|---------------------|----------------------------------------|------------------------------------------|-------------|-------------------|---------------------|---------------------|--------------------------------------|
  | [ID]   | YES / NO   | [C-NN or N/A]       | [excerpt or N/A]                       | [gate name or N/A]                       | YES / NO    | [C-NN or N/A]     | [type or N/A]       | [C-NN or N/A]       | [what closes the gap or N/A]         |
  ...one row per scored output...

  Two-layer? = YES when a positive instruction AND a distinct structural gate both
  apply to the same criterion. Single instruction without gate = single-layer.

  Asymmetric? = YES when C-01 and C-02 are enforced at different levels (structural
  vs. behavioral, or addressed vs. unaddressed).

  All cells required. Blank = structural violation.

---

STEP 5 -- IMPROVEMENT TABLE

Produce the IMPROVEMENT TABLE conforming to the declared schema and enforcement rules.

  If all outputs are golden: single row "All outputs golden; no improvement notes."

  Otherwise:

  IMPROVEMENT TABLE

  | Output | Lowest essential | Verdict | Pass condition (quoted verbatim)                  | Suggestion                               | How derived                                          |
  |--------|-----------------|---------|--------------------------------------------------|------------------------------------------|------------------------------------------------------|
  | [ID]   | C-[NN]          | FAIL/PARTIAL | "[verbatim pass condition from rubric]"     | [suggestion derived from quoted text]    | [specific phrase within quoted condition addressed]  |

  After completing each row, apply the VIOLATION GATE check:
    Is the "Suggestion" traceable to a specific phrase in "Pass condition
    (quoted verbatim)"? If NO, the suggestion is a structural violation. Rewrite.

---

STEP 6 -- SYNTHESIS TABLES

Produce each table in order.

FAILURE PATTERN TABLE

  | Criterion | Criterion name | All-output verdict | Diagnosis type             | Diagnosis       |
  |-----------|----------------|--------------------|----------------------------|-----------------|
  Include only criteria where every output scored PARTIAL or FAIL.
  If none: single row "No failure patterns in this round."

EXCELLENCE SIGNAL TABLE

  | Source                                             | Output | Criterion | Structural reason                  | Confirmed? |
  |----------------------------------------------------|--------|-----------|------------------------------------|------------|
  Verdict-split signals: derive from SPREADER TABLE rows only (clause (a) governs).
  Enforcement signals: derive from ENFORCEMENT ANALYSIS TABLE rows where
    Two-layer? = YES or Asymmetric? = YES.
  If no sources: single row "No excellence signals in this round."

REGRESSION TABLE

  | Output | Criterion | Prior verdict | Current verdict | What changed           |
  |--------|-----------|---------------|-----------------|------------------------|
  If no prior data: single row "No prior round data; regression analysis not possible."

LEADERBOARD TABLE

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|
  Rank descending by composite. Ties broken by output ID ascending.
```

---

## V-03 -- Axis C: Phase-gate lifecycle with VIOLATION GATE DECLARED checkpoint

**Variation axis**: Lifecycle emphasis -- explicit numbered phases with named entry and
exit conditions. Phase 5b is a dedicated VIOLATION GATE DECLARATION checkpoint that
must be completed and emitted before IMPROVEMENT-ANALYST can fire. The checkpoint
requires the scorer to emit a standalone labeled artifact (VIOLATION GATE DECLARATION)
naming the violation class explicitly. IMPROVEMENT-ANALYST entry condition is
VIOLATION GATE DECLARATION COMPLETE. Inherits the sub-role synthesis decomposition
from V-03 R11 (PATTERN-ANALYST, SIGNAL-ANALYST, REGRESSION-ANALYST, IMPROVEMENT-
ANALYST, LEADERBOARD).

**Hypothesis**: When the violation gate is a behavioral reminder inside IMPROVEMENT-
ANALYST, the model can produce improvement notes without emitting the gate as a
named standalone artifact. Making the violation gate a phase-gate checkpoint with
its own completion token changes it from a behavioral instruction to a protocol
precondition: IMPROVEMENT-ANALYST cannot begin unless VIOLATION GATE DECLARATION
COMPLETE appears above. This makes C-22 satisfaction testable at phase-boundary
inspection. C-23 is satisfied by the IMPROVEMENT-ANALYST schema declaration, which
inherits the "How derived" column requirement as a phase deliverable.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

DENOMINATOR GUARD -- read before any scoring begins:

N/A resolution rules:
  C-09: Prior-round data present? YES => fires. NO => N/A = PASS.
  C-10: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
  C-11: All variations symmetric on C-01/C-02 enforcement? YES => N/A = PASS. NO => fires.
  C-12: Any variation uses two-layer enforcement? NO => N/A = PASS. YES => fires.
  C-13: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
  C-14: NO N/A CONDITION. Fires unconditionally, every run.
  C-15: Any aspirational criteria resolve to N/A = PASS? YES => fires. NO => N/A = PASS.
  C-16: NO N/A CONDITION. Fires unconditionally, every run.
  C-17: All outputs score identically on all criteria? YES => N/A = PASS. NO => fires.
  C-18: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
  C-19: All outputs score identically on all criteria? YES => N/A = PASS. NO => fires.
  C-20: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
  C-21: All outputs score identically on all criteria? YES => N/A = PASS. NO => fires.
  C-22: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
  C-23: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.

Aspirational denominator: ALWAYS 15. N/A = PASS count as 1 in numerator.

  CORRECT form:    aspirational_pass / 15 * 10
  PROHIBITED form: aspirational_pass / N_resolved * 10   [denominator-shrinkage error]

C-14 anti-exemption: C-14 has NO N/A = PASS condition. It fires unconditionally
regardless of how many other criteria resolve to N/A = PASS.

---

PHASE 1 -- PRE-SCAN

Read all N outputs and the rubric. Do not score any criterion yet.

Step 1a -- Produce the SPREADER SPREAD TABLE (one row per criterion, C-01 through C-23):

  SPREADER SPREAD TABLE

  | Criterion | Divergence? | Outputs predicted to split | Structural reason                       |
  |-----------|-------------|----------------------------|-----------------------------------------|
  | C-01      | YES / NO    | [IDs or all same]          | [design property causing split or N/A]  |
  ...

  Divergence? = YES only when a named structural mechanism is expected to produce
  a different verdict for at least one output. If NO, enter N/A for structural reason.
  Every criterion must have a row.

Step 1b -- Produce the SCAN IMPORT DECLARATION:

  SCAN IMPORT DECLARATION

  (a) All verdict-split excellence signal claims in SIGNAL-ANALYST are structurally
      derived from the SPREADER SPREAD TABLE above. An excellence signal claim is
      structurally derived only if it cites a specific row (criterion + structural
      reason) from the table. A claim that cannot be traced to a specific table
      row is a prohibited inference.

  (b) Retroactive inference from verdict tallies is prohibited. SIGNAL-ANALYST may
      not construct verdict-split excellence signals by comparing verdict counts
      after scoring completes. Verdict tallies may confirm a signal already in the
      table, but may not originate one.

PRE-SCAN COMPLETE

---

PHASE 2 -- SCORING

Do not begin until PRE-SCAN COMPLETE appears above.

For each output, produce a scoring table:

  Output: [output identifier]

  | ID   | Criterion                                            | Wt | Verdict           | Evidence                          | Present_mechanism | Absent_mechanism |
  |------|------------------------------------------------------|----|-------------------|-----------------------------------|-------------------|------------------|
  | C-01 | Per-criterion verdicts present                       | E  | PASS/PARTIAL/FAIL  | [grounded in this output]         | --                | --               |
  | C-02 | Evidence quotes are grounded                         | E  | ...               | ...                               | ...               | ...              |
  | C-03 | Composite score computed correctly                   | E  | ...               | ...                               | ...               | ...              |
  | C-04 | Ranked leaderboard present                           | E  | ...               | ...                               | ...               | ...              |
  | C-05 | Golden threshold applied                             | E  | ...               | ...                               | ...               | ...              |
  | C-06 | Failure patterns identified                          | R  | ...               | ...                               | ...               | ...              |
  | C-07 | Excellence signals identified                        | R  | ...               | ...                               | ...               | ...              |
  | C-08 | Per-criterion verdict summary table                  | R  | ...               | ...                               | ...               | ...              |
  | C-09 | Regression signals identified                        | A  | ...               | ...                               | ...               | ...              |
  | C-10 | Actionable improvement note per failing output       | A  | ...               | ...                               | ...               | ...              |
  | C-11 | Asymmetric enforcement diagnosed                     | A  | ...               | ...                               | ...               | ...              |
  | C-12 | Two-layer enforcement recognized                     | A  | ...               | ...                               | ...               | ...              |
  | C-13 | Evidence portability verified                        | A  | ...               | ...                               | ...               | ...              |
  | C-14 | N/A denominator explicitly guarded                  | A  | ...               | ...                               | ...               | ...              |
  | C-15 | Denominator proof with anti-pattern shown            | A  | ...               | ...                               | ...               | ...              |
  | C-16 | C-14 no-N/A exemption declared                       | A  | ...               | ...                               | ...               | ...              |
  | C-17 | Excellence signals pre-scanned structurally          | A  | ...               | ...                               | ...               | ...              |
  | C-18 | Per-cell portability verdict column                  | A  | ...               | ...                               | ...               | ...              |
  | C-19 | Synthesis contract explicitly declared               | A  | ...               | ...                               | ...               | ...              |
  | C-20 | Structural improvement generation                    | A  | ...               | ...                               | ...               | ...              |
  | C-21 | Synthesis contract clauses individually labeled      | A  | ...               | ...                               | ...               | ...              |
  | C-22 | Improvement derivation violation gate declared       | A  | ...               | ...                               | ...               | ...              |
  | C-23 | Improvement table schema includes derivation field   | A  | ...               | ...                               | ...               | ...              |

  Evidence: before writing each cell, ask "Could this evidence apply to a
  different output without modification?" If yes, rewrite.

  Present_mechanism / Absent_mechanism: PARTIAL rows only. PASS and FAIL: enter --.
  Blank cells on PARTIAL rows are structural violations.

  Composite computation:
    essential_pass    = [count C-01..C-05 PASS; PARTIAL = 0.5]
    recommended_pass  = [count C-06..C-08 PASS; PARTIAL = 0.5]
    aspirational_pass = [count C-09..C-23 PASS or N/A=PASS; PARTIAL = 0.5]
                        denominator = 15 always

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)
              = [result]

    Golden: YES -- all 5 essentials PASS AND composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
SCORING COMPLETE -- [N] outputs scored

---

PHASE 3 -- VERIFICATION

Do not begin until SCORING COMPLETE appears above.

Audit A: For each evidence cell, verify it is grounded in this specific output
and does not resemble a generic criterion description.

Audit B: For PARTIAL rows only, verify Present_mechanism and Absent_mechanism
are non-empty. Mark n/a for PASS and FAIL.

Audit C -- Per-cell portability: for every evidence cell:
  ACCEPTED -- evidence uniquely identifies this output
  REJECTED -- evidence is portable; must be rewritten

  Output: [output identifier] -- Verification Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Audit C  | Row status |
  |------|---------|-----------------------------------|---------|---------|----------|------------|

  Row status = ACCEPTED only when all applicable audits are PASS or ACCEPTED.

Flag all REJECTED rows. Flagged items must be corrected and re-audited.

VERIFICATION COMPLETE

---

PHASE 4 -- CONFIRMATION

Do not begin until VERIFICATION COMPLETE appears above.

For each PARTIAL verdict, confirm Present_mechanism and Absent_mechanism name
specific structural properties (not generic quality phrases):

  Output: [output identifier] -- Content Confirmation

  | Criterion | Present_mechanism (first 15 words) | Specific? | Absent_mechanism (first 15 words) | Specific? | Status               |
  |-----------|-------------------------------------|-----------|-----------------------------------|-----------|----------------------|

Challenge any row where Specific? = NO. Challenged items must be rewritten.

CONFIRMATION COMPLETE

---

PHASE 5 -- SYNTHESIS

Do not begin until BOTH VERIFICATION COMPLETE AND CONFIRMATION COMPLETE appear
above. Both tokens are independent preconditions.

Runs five sub-roles in sequence. A sub-role cannot begin until the prior
sub-role issues its completion token.

---

PATTERN-ANALYST

Entry condition: VERIFICATION COMPLETE and CONFIRMATION COMPLETE both present above.
Domain: failure pattern detection; CRITERION SUMMARY TABLE; enforcement pattern analysis.

Step P1 -- FAILURE PATTERNS:
  For each criterion where every output scored PARTIAL or FAIL:
    Pattern: [criterion ID] -- [criterion name]
    Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]
  If none: "No failure patterns in this round."

Step P2 -- CRITERION SUMMARY TABLE (one row per criterion, C-01 through C-23):
  | Criterion | PASS count | PARTIAL count | FAIL count | N/A count |
  |-----------|------------|---------------|------------|-----------|
  | C-01      | [n]        | [n]           | [n]        | [n]       |

Step P3 -- ENFORCEMENT PATTERN TABLE:
  Inspect each scored variation's prompt body for:
  (i)  Two-layer enforcement: a positive instruction AND a structural gate apply
       to the same criterion. Name the criterion, Layer 1, Layer 2, and why
       the combination is stronger than single-layer.
  (ii) Asymmetric enforcement: C-01 and C-02 are enforced at different levels.
       Name the covered criterion, its mechanism, the uncovered criterion, and
       what enforcement mechanism is missing.

  ENFORCEMENT PATTERN TABLE

  | Output | Two-layer? | Criterion | Layer 1 (instruction excerpt)          | Layer 2 (gate name)        | Stronger because                      |
  |--------|------------|-----------|----------------------------------------|----------------------------|---------------------------------------|

  | Output | Asymmetric? | Covered criterion | Mechanism                 | Uncovered criterion | Missing mechanism                |
  |--------|-------------|-------------------|---------------------------|---------------------|----------------------------------|

PATTERN-ANALYST COMPLETE

---

SIGNAL-ANALYST

Entry condition: PATTERN-ANALYST COMPLETE present above.
Domain: excellence signals derived from SPREADER TABLE (clause (a)) and
ENFORCEMENT PATTERN TABLE.

Verdict-split signals (SCAN IMPORT DECLARATION clause (a) governs):
  For each criterion where SPREADER TABLE shows Divergence? = YES, confirm
  whether the split materialized in verdicts:
    Signal: [output ID] -- [criterion ID] -- [structural reason from SPREADER TABLE]

Enforcement signals (derived from ENFORCEMENT PATTERN TABLE):
  Two-layer: for each output where Two-layer? = YES:
    Two-layer: [output ID] -- [criterion ID] -- Layer 1: [excerpt] -- Layer 2:
    [gate name] -- Stronger because: [from table]
  Asymmetric: for each output where Asymmetric? = YES:
    Asymmetry: [output ID] -- enforces [covered criterion] via [mechanism] --
    [uncovered criterion] has no equivalent structural enforcement --
    missing mechanism: [from table]

If neither source yields any signal: "No excellence signals in this round."

SIGNAL-ANALYST COMPLETE

---

REGRESSION-ANALYST

Entry condition: SIGNAL-ANALYST COMPLETE present above.

If prior-round data is available: identify output/criterion pairs where prior
verdict was PASS and current verdict is PARTIAL or FAIL.
  Regression: [output ID] / [criterion ID] -- prior [verdict] => current [verdict]
  Note: [what changed between rounds]

If no prior data: "No prior round data; regression analysis not possible."

REGRESSION-ANALYST COMPLETE

---

PHASE 5b -- VIOLATION GATE DECLARATION

Do not begin until REGRESSION-ANALYST COMPLETE appears above.

Determine whether any non-golden outputs exist (require improvement notes):

  If all outputs are golden: emit "All outputs golden; VIOLATION GATE DECLARATION
  not required." and emit VIOLATION GATE DECLARATION COMPLETE. Skip to IMPROVEMENT-
  ANALYST which will also find all outputs golden.

  If any non-golden output exists: emit the following named artifact verbatim:

  VIOLATION GATE DECLARATION

  Any improvement suggestion that cannot be traced to the verbatim text of its
  source criterion's pass condition is a structural violation. This is not a
  behavioral quality failure -- it is a structural violation of the derivation
  requirement. A suggestion composed by reading the criterion name, the output's
  failing area, or a paraphrase of the pass condition, without the suggestion
  content being derivable from a specific phrase within the quoted pass condition,
  must not be emitted. The IMPROVEMENT-ANALYST must check each suggestion against
  the "How derived" field before emitting it.

VIOLATION GATE DECLARATION COMPLETE

---

IMPROVEMENT-ANALYST

Entry condition: VIOLATION GATE DECLARATION COMPLETE present above.
Domain: improvement notes per non-golden output; IMPROVEMENT TABLE with derivation
field.

If all outputs are golden: "All outputs golden; no improvement notes required."
IMPROVEMENT-ANALYST COMPLETE

Otherwise:

For each non-golden output, apply the two-step derivation protocol:

  Step 1 -- Identify lowest-scoring essential criterion (C-01..C-05):
    Lowest essential: [output ID] -- C-[NN] -- [verdict] -- [rubric pass condition]

  Step 2 -- Derive suggestion from pass condition:
    Suggestion must quote a specific phrase from the pass condition and make that
    phrase the content source for the improvement. Do not compose from criterion
    knowledge alone.

    How derived: [specific phrase within the pass condition that the suggestion addresses]

  Violation check: if the "How derived" trace cannot be completed, the suggestion
  is a structural violation under the VIOLATION GATE DECLARATION above. Do not
  emit it. Revise until traceable.

Produce the IMPROVEMENT TABLE:

  IMPROVEMENT TABLE

  | Output | Lowest essential | Verdict | Pass condition (quoted verbatim)              | Suggestion                                    | How derived                                                 |
  |--------|-----------------|---------|----------------------------------------------|-----------------------------------------------|-------------------------------------------------------------|
  | [ID]   | C-[NN]          | FAIL/PARTIAL | "[verbatim pass condition from rubric]" | [suggestion derived from quoted text]         | [specific phrase within quoted condition addressed]         |

IMPROVEMENT-ANALYST COMPLETE

---

LEADERBOARD

Entry condition: IMPROVEMENT-ANALYST COMPLETE present above.

Rank all outputs by composite score descending. Ties broken by output ID ascending.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

LEADERBOARD COMPLETE
SYNTHESIS COMPLETE
```

---

## V-04 -- Axes A + Inertia: Improvement Auditor role + inertia framing

**Variation axes**: Role sequence (Axis A) + inertia framing. Combines the IMPROVEMENT
AUDITOR role from V-01 with an explicit NAIVE PATTERN / STRUCTURAL PATTERN contrast
embedded at the start of the IMPROVEMENT AUDITOR instructions. The violation gate
(C-22) and "How derived" derivation field (C-23) emerge structurally as the answer
to a named and forbidden naive pattern, not as abstract rule declarations.

**Hypothesis**: V-04 R11 showed that the inertia-framing axis is effective for C-11
and C-12 because naming the naive pattern creates a structural foil: the model must
consciously reject the naive path and take the structural one. The same mechanism
applied to C-22/C-23: if the IMPROVEMENT AUDITOR names "compose a suggestion by
reading the criterion name" as FORBIDDEN, then both the violation gate (C-22 -- the
named prohibition is the gate class) and the derivation field requirement (C-23 --
the "How derived" column exists to prove the FORBIDDEN path was not taken) become
natural structural consequences of the inertia contrast. C-22 is satisfied by the
FORBIDDEN declaration as a named violation class; C-23 is satisfied by the "How
derived" column as the compliance verification mechanism. C-08 remains the outstanding
gap (no CRITERION SUMMARY TABLE in this role-sequence family).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role                | Requires                                                                                                                              | Produces                       | Domain (ONLY)                                                                                                                                             | Cannot Check                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| SCANNER             | (none)                                                                                                                                | SCANNER COMPLETE               | Pre-scan divergence; SPREADER SPREAD TABLE; SCAN IMPORT DECLARATION                                                                                        | Scoring verdicts, evidence quality, content specificity                               |
| ANALYST             | SCANNER COMPLETE                                                                                                                      | ANALYST COMPLETE               | Per-criterion verdicts; evidence; composite; golden; Present_mechanism / Absent_mechanism                                                                  | Pre-scan (Scanner domain), format auditing (Verifier domain)                          |
| VERIFIER            | ANALYST COMPLETE                                                                                                                      | VERIFIER AUDIT COMPLETE        | Format presence: evidence non-genericity; PARTIAL column non-emptiness; per-cell portability ACCEPTED/REJECTED verdict                                     | Content quality of diagnostic cells (Confirmer domain)                                |
| CONFIRMER           | VERIFIER AUDIT COMPLETE                                                                                                               | CONFIRMATION COMPLETE          | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                       | Format presence (Verifier domain), scoring verdicts (Analyst domain)                  |
| ENFORCEMENT AUDITOR | CONFIRMATION COMPLETE                                                                                                                 | ENFORCEMENT REGISTER COMPLETE  | Two-layer enforcement detection; asymmetric enforcement detection across all scored variations                                                              | Scoring verdicts (Analyst), evidence quality (Verifier), content depth (Confirmer)    |
| IMPROVEMENT AUDITOR | ENFORCEMENT REGISTER COMPLETE                                                                                                         | IMPROVEMENT REGISTER COMPLETE  | Violation gate declaration via named inertia contrast; IMPROVEMENT TABLE with derivation field                                                             | Enforcement patterns (Enforcement Auditor domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS           | VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND ENFORCEMENT REGISTER COMPLETE AND IMPROVEMENT REGISTER COMPLETE (all four independently) | (terminal output)         | Leaderboard; excellence signals; failure patterns; regression signals                                                                                      | Re-scoring; re-auditing; enforcement re-inspection; improvement re-generation         |

Gate rules (hard):
  - ANALYST cannot begin without SCANNER COMPLETE present above.
  - VERIFIER cannot begin without ANALYST COMPLETE present above.
  - CONFIRMER cannot begin without VERIFIER AUDIT COMPLETE present above.
  - ENFORCEMENT AUDITOR cannot begin without CONFIRMATION COMPLETE present above.
  - IMPROVEMENT AUDITOR cannot begin without ENFORCEMENT REGISTER COMPLETE present above.
  - SYNTHESIS cannot begin without ALL FOUR tokens present above independently.
    Missing IMPROVEMENT REGISTER COMPLETE blocks SYNTHESIS even if the other three
    tokens are present.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: SCANNER

Domain: Pre-scan divergence prediction; SPREADER SPREAD TABLE; SCAN IMPORT
DECLARATION (see manifest).

Read all N outputs and the rubric. Do not score any criterion yet.

Step 1 -- Produce the SPREADER SPREAD TABLE (one row per criterion, C-01 through C-23):

  SPREADER SPREAD TABLE

  | Criterion | Divergence? | Outputs predicted to split | Structural reason for divergence        |
  |-----------|-------------|----------------------------|-----------------------------------------|
  | C-01      | YES / NO    | [output IDs or all same]   | [specific structural mechanism or N/A]  |
  ...

  Rules:
  - Every rubric criterion must have a row. A blank row is a structural gap.
  - Divergence? = YES only if a specific structural mechanism is expected to
    produce a different verdict relative to peers.
  - Structural reason must name the design property, not describe the criterion.
  - If no divergence is predicted, enter NO and N/A.

Step 2 -- Produce the SCAN IMPORT DECLARATION:

  SCAN IMPORT DECLARATION

  (a) All verdict-split excellence signal claims in SYNTHESIS are structurally
      derived from the SPREADER SPREAD TABLE above. A claim is structurally
      derived if it cites a specific row (criterion + structural reason). A claim
      that cannot be traced to a specific table row is prohibited.

  (b) Retroactive inference from verdict tallies is prohibited. SYNTHESIS may
      not construct verdict-split excellence signals by comparing verdict counts
      after scoring completes. Verdict tallies may confirm a signal identified
      in the table, but may not originate one.

SCANNER COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cells; composite; Present_mechanism and
Absent_mechanism columns (see manifest).
Do not begin until SCANNER COMPLETE appears above.

DENOMINATOR GUARD:

  N/A resolution rules:
    C-09: Prior-round data present? YES => score normally. NO => N/A = PASS.
    C-10: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-11: Symmetric enforcement on C-01/C-02? YES => N/A = PASS. NO => fires.
    C-12: Any variation uses two-layer enforcement? NO => N/A = PASS. YES => fires.
    C-13: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
    C-14: NO N/A CONDITION. C-14 fires unconditionally for every run.
    C-15: Any aspirational criteria resolve to N/A = PASS? YES => fires. NO => N/A = PASS.
    C-16: NO N/A CONDITION. C-16 fires unconditionally for every run.
    C-17: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-18: N > 1 outputs scored? YES => fires. N = 1 => N/A = PASS.
    C-19: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-20: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-21: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
    C-22: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
    C-23: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.

  Aspirational denominator: ALWAYS 15. N/A = PASS criteria count as 1 in numerator.

  CORRECT form:    aspirational_pass / 15 * 10
  PROHIBITED form: aspirational_pass / N_resolved * 10   [denominator-shrinkage error]

  C-14 anti-exemption: C-14 has NO N/A = PASS condition. It fires unconditionally
  every run, regardless of how many other aspirational criteria resolve to N/A = PASS.

For each output, produce a scoring table:

  Output: [output identifier]

  | ID   | Criterion                                            | Wt | Verdict           | Evidence                                             | Present_mechanism | Absent_mechanism |
  |------|------------------------------------------------------|----|-------------------|------------------------------------------------------|-------------------|------------------|
  | C-01 | Per-criterion verdicts present                       | E  | PASS/PARTIAL/FAIL  | [grounded in this output -- not portable to others]  | --                | --               |
  ...rows C-02 through C-23...

  Column rules:
    - Evidence: before writing, ask "Could this evidence apply to a different
      output with no modification?" If YES, rewrite until uniquely identifying.
    - Present_mechanism: PARTIAL only -- name the specific structural element
      present that prevented FAIL. Enter -- for PASS and FAIL.
    - Absent_mechanism: PARTIAL only -- name the specific structural element
      absent that prevented PASS. Enter -- for PASS and FAIL.
    - Blank Present_mechanism or Absent_mechanism on a PARTIAL row: structural
      violation equivalent to a blank evidence cell.
    - No row may be skipped.

  Composite computation:
    essential_pass    = [count C-01..C-05 PASS; PARTIAL = 0.5]
    recommended_pass  = [count C-06..C-08 PASS; PARTIAL = 0.5]
    aspirational_pass = [count C-09..C-23 PASS or N/A=PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)
              = [result]

    Golden: YES -- all 5 essentials PASS AND composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence -- evidence cell non-genericity; PARTIAL column
non-emptiness; per-cell portability (see manifest).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A -- Evidence quality: Reject any cell that:
  (a) could apply to a different output without modification, OR
  (b) restates the criterion name or verdict rather than citing evidence.

AUDIT B -- Diagnostic column presence: PARTIAL verdicts only.
  Present_mechanism and Absent_mechanism must be non-empty. Mark n/a for others.

AUDIT C -- Per-cell portability: For every evidence cell:
  ACCEPTED -- evidence uniquely identifies this output.
  REJECTED -- evidence is portable; must be rewritten.

  Output: [output identifier] -- Verifier Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Audit C  | Row status |
  |------|---------|-----------------------------------|---------|---------|----------|------------|

  Row status = ACCEPTED only when all applicable audits are PASS or ACCEPTED.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Audit [A/B/C]: [specific reason]

Flagged items must be corrected and re-audited.
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells
name specific structural properties? (see manifest).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

  Output: [output identifier] -- Confirmer Audit

  | Criterion | Present_mechanism (first 15 words) | Specific? | Absent_mechanism (first 15 words) | Specific? | Status               |
  |-----------|-------------------------------------|-----------|-----------------------------------|-----------|----------------------|

Challenge any row where Specific? = NO. Challenged items must be rewritten.
CONFIRMATION COMPLETE

---

ROLE 5: ENFORCEMENT AUDITOR

Domain: Two-layer enforcement detection; asymmetric enforcement detection (see manifest).
Do not begin until CONFIRMATION COMPLETE appears above.

Part A -- Two-layer enforcement detection:
  YES when a positive instruction AND a structural gate both apply to the same
  criterion. Single instruction without gate = single-layer.

Part B -- Asymmetric enforcement detection:
  YES when C-01 and C-02 are enforced at different levels.

  ENFORCEMENT PATTERN REGISTER

  Two-layer sub-table:
  | Output | Two-layer detected? | Criterion | Layer 1 (instruction excerpt)       | Layer 2 (gate or constraint name)  | Stronger because               |
  |--------|---------------------|-----------|-------------------------------------|------------------------------------|--------------------------------|

  Asymmetry sub-table:
  | Output | Asymmetric detected? | Strongly enforced criterion | Enforcement mechanism | Weakly/un-enforced criterion | Missing enforcement mechanism  |
  |--------|---------------------|-----------------------------|-----------------------|------------------------------|-------------------------------|

  Every scored output must appear in each sub-table. Blank row = structural gap.

ENFORCEMENT REGISTER COMPLETE

---

ROLE 6: IMPROVEMENT AUDITOR

Domain: Violation gate declaration via named inertia contrast; IMPROVEMENT TABLE
with derivation field (see manifest).
Do not begin until ENFORCEMENT REGISTER COMPLETE appears above.

INERTIA CONTRAST -- read before producing any improvement note:

  NAIVE PATTERN (FORBIDDEN):
    Read the failing criterion name. Think about what a good output would look like.
    Write a suggestion based on that knowledge.
    Why FORBIDDEN: this path composes suggestions from criterion knowledge, not from
    the pass condition text. The resulting suggestion may be valid in direction but
    cannot be verified as structurally derived. It satisfies neither C-20 (which
    requires structural derivation from the pass condition) nor C-22 (which requires
    any non-traceable suggestion to be a named violation). A suggestion produced by
    the naive path is a structural violation, not a behavioral quality shortfall.

  STRUCTURAL PATTERN (REQUIRED):
    Step 1: Identify the lowest-scoring essential criterion (C-01..C-05) for this
      non-golden output. If tied, select the lower criterion ID.
    Step 2: Quote the pass condition verbatim from the rubric for that criterion.
    Step 3: Identify a specific phrase within the quoted pass condition that the
      output fails to satisfy.
    Step 4: Derive the suggestion content from that specific phrase. The suggestion
      must be traceable to the phrase -- not merely consistent with it.
    GATE: If you cannot complete Step 3 (no specific phrase to target) or Step 4
      (suggestion cannot be traced to a phrase), do not emit the suggestion. The
      non-traceable suggestion is a structural violation under C-22. Revise the
      analysis of the failing criterion before proceeding.

If all outputs are golden: emit "All outputs golden; improvement notes not required."
and emit IMPROVEMENT REGISTER COMPLETE.

Otherwise, produce the IMPROVEMENT TABLE using the STRUCTURAL PATTERN for each
non-golden output:

  IMPROVEMENT TABLE

  | Output | Lowest essential | Verdict | Pass condition (quoted verbatim)              | Suggestion                                    | How derived                                                        |
  |--------|-----------------|---------|----------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------|
  | [ID]   | C-[NN]          | FAIL/PARTIAL | "[verbatim pass condition from rubric]" | [suggestion derived from quoted text]         | [specific phrase in quoted condition that the suggestion addresses] |

  After each row: confirm the "How derived" cell names a specific phrase from the
  quoted pass condition. If it reads "general derivation" or "from pass condition"
  without naming the phrase, the row is a structural schema violation. Rewrite.

IMPROVEMENT REGISTER COMPLETE

---

SYNTHESIS

Do not begin until ALL FOUR tokens appear above independently:
  - VERIFIER AUDIT COMPLETE
  - CONFIRMATION COMPLETE
  - ENFORCEMENT REGISTER COMPLETE
  - IMPROVEMENT REGISTER COMPLETE

LEADERBOARD

Rank all outputs by composite score descending. Ties broken by output ID ascending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

Source 1 -- Verdict-split signals (governed by SCAN IMPORT DECLARATION clause (a)):
  For each SPREADER TABLE criterion where Divergence? = YES and the split materialized:
    Signal: [output ID] -- [criterion ID] -- [structural reason from SPREADER TABLE row]

Source 2 -- Enforcement-pattern signals (from ENFORCEMENT PATTERN REGISTER):
  Two-layer: for each output where Two-layer detected? = YES:
    Two-layer: [output ID] -- [criterion ID] -- Layer 1: [excerpt] --
    Layer 2: [gate name] -- Stronger because: [from register]
  Asymmetric: for each output where Asymmetric detected? = YES:
    Asymmetry: [output ID] -- enforces [criterion] via [mechanism] --
    [uncovered criterion] lacks equivalent structural enforcement --
    missing mechanism: [from register]

If neither source yields any signal: "No excellence signals in this round."

FAILURE PATTERNS

For each criterion where every output scored PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round data available: flag any output/criterion pair regressing from
PASS to PARTIAL or FAIL. Include output ID, criterion ID, and note on what changed.

If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-05 -- Axes B + formal register: Schema-first with FORBIDDEN violation blocks

**Variation axes**: Output format (Axis B) + phrasing register (formal/technical with
FORBIDDEN block declarations). Extends V-02 by embedding FORBIDDEN violation
declarations directly inside the IMPROVEMENT TABLE schema definition in the OUTPUT
SCHEMA DECLARATION block. C-22 is satisfied by FORBIDDEN(1) -- a named prohibition
that makes non-traceable suggestions a violation class. C-23 is satisfied by the
"How derived" column declared in the schema. Both are independently auditable: C-22
by checking for the FORBIDDEN declaration in the schema block; C-23 by checking for
the column name in the IMPROVEMENT TABLE schema row.

**Hypothesis**: V-02 showed that schema-declared deliverables are auditable by column
reference. The gap is that schema compliance (column present) does not by itself
declare that an untraceable suggestion is a structural violation -- it only makes the
derivation path verifiable. FORBIDDEN blocks embedded in the schema definition close
this gap: FORBIDDEN(1) is the named violation class (C-22 requires a "named gate or
constraint"); FORBIDDEN(2) makes the column a compliance test rather than a data
capture field (C-23 requires the derivation to be "independently field-auditable").
The formal register makes FORBIDDEN declarations the baseline, not edge-case warnings.
A scorer following the schema encounters the FORBIDDEN blocks as structural constraints
before writing any improvement note.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

OUTPUT SCHEMA DECLARATION

The following schemas are declared before any scoring begins. Every section must
conform to its declared schema. A section using prose instead of its declared
table format, or omitting a required table entirely, is a structural violation.

SCORING TABLE schema:
  Required columns: ID / Criterion / Wt / Verdict / Evidence / Present_mechanism /
                    Absent_mechanism / PORTABILITY
  FORBIDDEN: A blank PORTABILITY cell is a structural violation.
  FORBIDDEN: A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row
             is a structural violation equivalent to a blank evidence cell.

SPREADER SPREAD TABLE schema:
  Required columns: Criterion / Divergence? / Outputs predicted to split / Structural reason
  FORBIDDEN: A criterion row with a blank Structural reason is a structural violation
             regardless of the Divergence? value (enter N/A if Divergence? = NO).

SCAN IMPORT DECLARATION schema:
  Required elements: Clause (a) with labeled clause marker; Clause (b) with labeled
                     clause marker. Both clauses must be independently labeled so
                     compliance with each can be verified by label reference.
  FORBIDDEN: A SCAN IMPORT DECLARATION without individually labeled clauses satisfies
             C-19 at PARTIAL level only and does not satisfy C-21.

CRITERION SUMMARY TABLE schema:
  Required columns: Criterion / PASS count / PARTIAL count / FAIL count / N/A count
  One row per rubric criterion (C-01 through C-23).
  FORBIDDEN: Omitting this table is a structural violation of C-08.

ENFORCEMENT ANALYSIS TABLE schema:
  Required columns: Output / Two-layer? / Two-layer criterion / Layer 1 instruction /
                    Layer 2 gate / Asymmetric? / Covered criterion / Coverage mechanism /
                    Uncovered criterion / Missing mechanism
  FORBIDDEN: A blank cell in any required column is a structural violation.

IMPROVEMENT TABLE schema:
  Required columns: Output / Lowest essential / Verdict / Pass condition (quoted verbatim) /
                    Suggestion / How derived
  FORBIDDEN(1): Any improvement suggestion that cannot be traced to the verbatim text
                of its source criterion's pass condition is a structural violation. This
                is not a behavioral quality shortfall -- it is a named violation class.
                Do not emit a non-traceable suggestion. If traceability cannot be
                established, revise the analysis before emitting the row.
  FORBIDDEN(2): A "How derived" cell that contains "general derivation", "from pass
                condition", or any formulation that does not name a specific phrase
                within the quoted pass condition is a structural violation. The cell
                must name the specific phrase or clause from the quoted condition that
                the suggestion addresses.
  FORBIDDEN(3): Omitting the "How derived" column is a structural violation of the
                IMPROVEMENT TABLE schema regardless of whether improvement notes are
                otherwise correct.
  N/A condition: If all outputs are golden, emit "All outputs golden; IMPROVEMENT
                 TABLE not required."

FAILURE PATTERN TABLE schema:
  Required columns: Criterion / Criterion name / All-output verdict / Diagnosis type / Diagnosis

EXCELLENCE SIGNAL TABLE schema:
  Required columns: Source / Output / Criterion / Structural reason / Confirmed?

REGRESSION TABLE schema:
  Required columns: Output / Criterion / Prior verdict / Current verdict / What changed

LEADERBOARD TABLE schema:
  Required columns: Rank / Output / Composite / Golden?

---

DENOMINATOR GUARD -- read before any scoring begins:

N/A resolution rules:
  C-09: Prior-round data present? YES => score. NO => N/A = PASS.
  C-10: Any non-golden outputs? YES => fires. NO (all golden) => N/A = PASS.
  C-11: All variations symmetric on C-01/C-02 enforcement? YES => N/A = PASS. NO => fires.
  C-12: Any variation uses two-layer enforcement? NO => N/A = PASS. YES => fires.
  C-13: N > 1? YES => fires. N = 1 => N/A = PASS.
  C-14: NO N/A CONDITION. Fires unconditionally every run.
  C-15: Any aspirational criteria resolve to N/A = PASS? YES => fires. NO => N/A = PASS.
  C-16: NO N/A CONDITION. Fires unconditionally every run.
  C-17: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-18: N > 1? YES => fires. N = 1 => N/A = PASS.
  C-19: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-20: Any non-golden outputs? YES => fires. NO => N/A = PASS.
  C-21: All outputs identical on all criteria? YES => N/A = PASS. NO => fires.
  C-22: Any non-golden outputs? YES => fires. NO => N/A = PASS.
  C-23: Any non-golden outputs? YES => fires. NO => N/A = PASS.

Aspirational denominator: ALWAYS 15. N/A = PASS criteria count as 1 in numerator.
The denominator does NOT change regardless of how many criteria resolve to N/A = PASS.

  CORRECT form:    aspirational_pass / 15 * 10
  PROHIBITED form: aspirational_pass / N_resolved * 10   [denominator-shrinkage error]

C-14 anti-exemption: C-14 has NO N/A = PASS condition. C-14 fires unconditionally
in every run. There is no run configuration -- including runs where every other
aspirational criterion resolves to N/A = PASS -- in which C-14 is exempt.

---

STEP 1 -- PRE-SCAN

Read all N outputs and the rubric. Do not score any criterion yet.

Produce the SPREADER SPREAD TABLE conforming to the declared schema:

  SPREADER SPREAD TABLE

  | Criterion | Divergence? | Outputs predicted to split | Structural reason                      |
  |-----------|-------------|----------------------------|----------------------------------------|
  | C-01      | YES / NO    | [IDs or all same]          | [named design property or N/A]         |
  ...one row per criterion C-01 through C-23...

Immediately after, produce the SCAN IMPORT DECLARATION conforming to the declared schema:

  SCAN IMPORT DECLARATION

  (a) All verdict-split excellence signal claims in the EXCELLENCE SIGNAL TABLE are
      structurally derived from a specific SPREADER SPREAD TABLE row (criterion +
      structural reason cited). A claim without a traceable SPREADER TABLE row is
      a prohibited inference.

  (b) Retroactive inference from verdict tallies is prohibited. SYNTHESIS may not
      construct verdict-split excellence signals by comparing verdict counts after
      scoring completes. Verdict tallies may confirm a pre-scan signal but may not
      originate one.

---

STEP 2 -- SCORING

For each output, produce a SCORING TABLE conforming to the declared schema:

  Output: [output identifier]

  SCORING TABLE

  | ID   | Criterion                                            | Wt | Verdict           | Evidence                          | Present_mechanism | Absent_mechanism | PORTABILITY |
  |------|------------------------------------------------------|----|-------------------|-----------------------------------|-------------------|------------------|-------------|
  | C-01 | Per-criterion verdicts present                       | E  | PASS/PARTIAL/FAIL  | [evidence unique to this output]  | --                | --               | ACCEPTED    |
  | C-02 | Evidence quotes are grounded                         | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-03 | Composite score computed correctly                   | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-04 | Ranked leaderboard present                           | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-05 | Golden threshold applied                             | E  | ...               | ...                               | ...               | ...              | ...         |
  | C-06 | Failure patterns identified                          | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-07 | Excellence signals identified                        | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-08 | Per-criterion verdict summary table                  | R  | ...               | ...                               | ...               | ...              | ...         |
  | C-09 | Regression signals identified                        | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-10 | Actionable improvement note per failing output       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-11 | Asymmetric enforcement diagnosed                     | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-12 | Two-layer enforcement recognized                     | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-13 | Evidence portability verified                        | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-14 | N/A denominator explicitly guarded                  | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-15 | Denominator proof with anti-pattern shown            | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-16 | C-14 no-N/A exemption declared                       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-17 | Excellence signals pre-scanned structurally          | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-18 | Per-cell portability verdict column                  | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-19 | Synthesis contract explicitly declared               | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-20 | Structural improvement generation                    | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-21 | Synthesis contract clauses individually labeled      | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-22 | Improvement derivation violation gate declared       | A  | ...               | ...                               | ...               | ...              | ...         |
  | C-23 | Improvement table schema includes derivation field   | A  | ...               | ...                               | ...               | ...              | ...         |

  PORTABILITY: ACCEPTED = uniquely identifies this output. REJECTED = portable; rewrite.
  Present_mechanism / Absent_mechanism: PARTIAL rows only; PASS and FAIL: enter --.

  Composite computation:
    essential_pass    = [count C-01..C-05 PASS; PARTIAL = 0.5]
    recommended_pass  = [count C-06..C-08 PASS; PARTIAL = 0.5]
    aspirational_pass = [count C-09..C-23 PASS or N/A=PASS; PARTIAL = 0.5]
                        denominator = 15 always

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)
              = [result]

    Golden: YES -- all 5 essentials PASS AND composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

---

STEP 3 -- CRITERION SUMMARY

Produce the CRITERION SUMMARY TABLE conforming to the declared schema:

  CRITERION SUMMARY TABLE

  | Criterion | PASS count | PARTIAL count | FAIL count | N/A count |
  |-----------|------------|---------------|------------|-----------|
  | C-01      | [n]        | [n]           | [n]        | [n]       |
  ...one row per criterion C-01 through C-23...

---

STEP 4 -- ENFORCEMENT ANALYSIS

Inspect each scored variation's prompt body for enforcement patterns. Produce the
ENFORCEMENT ANALYSIS TABLE conforming to the declared schema:

  ENFORCEMENT ANALYSIS TABLE

  | Output | Two-layer? | Two-layer criterion | Layer 1 instruction (first 12 words)    | Layer 2 gate / constraint name           | Asymmetric? | Covered criterion | Coverage mechanism  | Uncovered criterion | Missing mechanism                    |
  |--------|------------|---------------------|----------------------------------------|------------------------------------------|-------------|-------------------|---------------------|---------------------|--------------------------------------|
  | [ID]   | YES / NO   | [C-NN or N/A]       | [excerpt or N/A]                       | [gate name or N/A]                       | YES / NO    | [C-NN or N/A]     | [type or N/A]       | [C-NN or N/A]       | [what closes the gap or N/A]         |
  ...one row per scored output...

  Two-layer? = YES: positive instruction AND structural gate both apply to same criterion.
  Asymmetric? = YES: C-01 and C-02 enforced at different levels.
  FORBIDDEN: Blank cell in any column is a structural violation.

---

STEP 5 -- IMPROVEMENT TABLE

Produce the IMPROVEMENT TABLE conforming to the declared schema and FORBIDDEN constraints.

If all outputs are golden: emit "All outputs golden; IMPROVEMENT TABLE not required."

Otherwise:

  IMPROVEMENT TABLE

  | Output | Lowest essential | Verdict    | Pass condition (quoted verbatim)              | Suggestion                              | How derived                                                        |
  |--------|-----------------|------------|----------------------------------------------|-----------------------------------------|--------------------------------------------------------------------|
  | [ID]   | C-[NN]          | FAIL/PARTIAL | "[verbatim pass condition from rubric]"    | [suggestion derived from quoted text]   | [specific phrase within quoted condition that suggestion addresses] |

  After completing each row:
    (1) Verify "Suggestion" is traceable to a specific phrase in "Pass condition
        (quoted verbatim)". If not: FORBIDDEN(1) applies -- structural violation.
        Rewrite or revise criterion analysis before proceeding.
    (2) Verify "How derived" names a specific phrase from the quoted condition.
        If it uses a generic formulation: FORBIDDEN(2) applies -- structural violation.
        Rewrite the cell to name the specific phrase.

---

STEP 6 -- SYNTHESIS TABLES

Produce each table in order conforming to declared schemas.

FAILURE PATTERN TABLE

  | Criterion | Criterion name | All-output verdict | Diagnosis type             | Diagnosis       |
  Include only criteria where every output scored PARTIAL or FAIL.
  If none: single row "No failure patterns in this round."

EXCELLENCE SIGNAL TABLE

  | Source                                              | Output | Criterion | Structural reason                  | Confirmed? |
  Verdict-split signals: derive from SPREADER TABLE rows only (clause (a) governs).
  Enforcement signals: derive from ENFORCEMENT ANALYSIS TABLE rows where
    Two-layer? = YES or Asymmetric? = YES.
  If no sources: single row "No excellence signals in this round."

REGRESSION TABLE

  | Output | Criterion | Prior verdict | Current verdict | What changed           |
  If no prior data: single row "No prior round data; regression analysis not possible."

LEADERBOARD TABLE

  | Rank | Output | Composite | Golden? |
  Rank descending by composite. Ties broken by output ID ascending.
```

---

## Divergence predictions (R12 v8)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Structural reason |
|-----------|------|------|------|------|------|-------------------|
| C-08 | FAIL | PASS | PASS | FAIL | PASS | V-02/03/05 declare CRITERION SUMMARY TABLE as required schema deliverable; V-01/04 use role-sequence family without schema declaration |
| C-22 | PASS | PASS | PASS | PASS | PASS | All five variations declare violation gate by name (role domain, schema FORBIDDEN, phase checkpoint, inertia FORBIDDEN, schema FORBIDDEN(1) respectively) |
| C-23 | PASS | PASS | PASS | PASS | PASS | All five variations include "How derived" column in IMPROVEMENT TABLE schema |

Notable: C-22 and C-23 are expected to converge to PASS across all five variations. The
discriminating criterion for R12 is C-08 (CRITERION SUMMARY TABLE), which splits V-01/V-04
(FAIL) from V-02/V-03/V-05 (PASS). No new R12 gap is predicted for the covered criteria.

The theoretical maximum composite under v8 (all 23 criteria PASS):
  (5/5 * 60) + (3/3 * 30) + (15/15 * 10) = 100.0

V-02, V-03, V-05 are positioned to approach this ceiling. V-01, V-04 are limited by C-08 FAIL.
