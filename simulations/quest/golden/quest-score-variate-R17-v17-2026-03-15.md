# quest-score Variations -- Round 17
**Skill**: quest-score
**Rubric**: v17 (N_essential=4, N_recommended=3, N_aspirational=33)
**Date**: 2026-03-15
**Round**: 17

---

## Design logic

### Unachieved ceiling entering R17

R16 was scored against rubric v16 (N_aspirational=31). R16 V-05 (full stack) achieved all
31 aspirational criteria. Rubric v17 adds 2 new aspirational criteria (C-39, C-40) derived
from R16 scorecard patterns and PARTIAL/PASS discriminators.

| Criterion | R16 status | Gap analysis |
|-----------|------------|--------------|
| C-39 | NOT IN RUBRIC | Derived from R16 C-37 PASS discriminator. R16 V-03 (POS axis) achieved C-37 PASS by naming positional verification tests with "[element] appears BEFORE [anchor]" template syntax. The template uses generic placeholders ("[anchor]", "[element]") rather than naming the specific anchor element for each position-sensitive criterion. C-39 escalates: for each position-sensitive criterion, the application note must name the specific structural anchor element the positional check references AND the directional relationship -- not just a slot-fillable template. A note naming "[element] BEFORE [anchor]" with placeholders satisfies C-37 (names the positional test class) but not C-39 (the anchor element is a placeholder, not a named structural element). C-39 closes the remaining scorer discretion: after reading the per-criterion note, the scorer knows exactly which element to check, which anchor to check against, and which direction. |
| C-40 | NOT IN RUBRIC | Derived from R16 C-38 PASS discriminator. R16 V-04 (EMIT+CLASS axis) achieved C-38 PASS by including a dedicated application note directing class identification and naming the inertia pattern as FAIL. The three components of C-38 PASS: (1) naming the inertia pattern, (2) declaring it FAIL, (3) grounding the verdict in structural-equivalence reasoning. C-38 is satisfied by having these components present; C-40 names whether the structural-equivalence basis closes the PARTIAL bypass path in the application note itself, not just in the pass condition. Without the structural-equivalence reasoning, a scorer who encounters architecture-present-but-unnamed may still default to PARTIAL under a "something is present, something is absent" logic. C-40 requires the application note to make the PARTIAL bypass path explicitly unavailable by providing the equivalence argument. |

### Formula change

N_aspirational increases from 31 to 33. All variations update the composite formula
from `aspirational_pass / 31 * 10` to `aspirational_pass / 33 * 10`. The CONSOLIDATED
PRODUCTION-TIME REGISTER expands from 38 rows to 40 rows (C-01 through C-40). Both
updates are required infrastructure for every R17 variation.

### New mechanism gaps

**For C-39 (anchor-complete positional application note -- ANCH):**
C-37 requires a per-criterion application note naming the positional verification test.
C-39 closes the remaining gap: the note must name the specific anchor element the
positional check references AND the directional relationship (BEFORE, AFTER, co-located),
not just the class of test. Two components must both be present in each per-criterion note:
(a) anchor axis -- the specific structural element against which position is verified;
(b) direction axis -- the explicit directional relationship (BEFORE / AFTER / co-located).

Test for C-39:
- PASS: JUDGE STANDARD application notes for position-sensitive criteria each name a
  specific anchor element (e.g., "first ANALYST criterion row," "LEADERBOARD section
  heading") AND a specific directional relationship (e.g., BEFORE). The anchor is not
  a placeholder like "[anchor]" but a named structural element.
- PARTIAL: Per-criterion notes present (C-37 PASS level) but anchor or direction is a
  generic placeholder; scorer still must determine what to check against.
- FAIL: No per-criterion application notes for position-sensitive criteria; or notes
  name only the class of positional test without anchor or direction.

**For C-40 (inertia-FAIL declaration with structural-equivalence basis -- INER):**
C-38 requires a dedicated application note directing class identification with the inertia
framing. C-40 closes the PARTIAL bypass path: the application note must provide the
structural-equivalence basis explaining WHY a variation with all components but no
class-naming is FAIL rather than PARTIAL. The structural-equivalence argument is:
"the identification act IS the criterion requirement; architecture-present-without-naming
is structurally equivalent to architecture-absent because neither satisfies the criterion."

Test for C-40:
- PASS: The class-recognition application note (required by C-38) includes an explicit
  structural-equivalence declaration: "architecture-present-without-naming = structurally
  equivalent to architecture-absent, because the identification act IS the criterion
  requirement." The note must (a) name the inertia pattern, (b) declare it FAIL not PARTIAL,
  (c) provide the structural-equivalence basis that closes the PARTIAL bypass.
- PARTIAL: Application note with inertia framing present (C-38 PASS level) but structural-
  equivalence reasoning absent; the FAIL verdict is asserted but not grounded.
- FAIL: No dedicated class-recognition application note; or note directs identification
  without addressing the inertia case.

### New axes for R17

| Axis | Label | Mechanism |
|------|-------|-----------|
| ANCH | Anchor-complete positional note | JUDGE STANDARD per-criterion application notes for position-sensitive criteria name specific anchor element (not a placeholder) AND explicit direction. Closes C-39. |
| INER | Inertia-FAIL framing with structural-equivalence basis | JUDGE STANDARD class-recognition application note includes structural-equivalence basis grounding the inertia=FAIL verdict, closing the PARTIAL bypass. Closes C-40. |
| PHREG | Phrasing register (conversational) | Application note content correct (anchor-complete + inertia-FAIL) but expressed in flowing conversational prose without formal APPLICATION NOTE block labels. Tests whether C-39/C-40 require formal block structure or are satisfied by content alone. |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (ANCH)**: Anchor-complete positional application notes. Per-criterion notes for
  C-10, C-15, C-27 each name the specific anchor element and directional relationship.
  Class-recognition application note present (C-38 PASS level) but WITHOUT inertia-FAIL
  structural-equivalence basis (C-40 FAIL). Full R16 V-05 base: three-way SYNTHESIS
  conjunction (C-35), inspection-without-reading schema (C-36), intra-role lifecycle
  sub-gate (C-33/C-35). 40-row register, YES-only gate, formula /33, E=4.
  Predicts: C-39 PASS, C-37 PASS (carried), C-38 PASS (carried), C-40 FAIL (no
  structural-equivalence basis in note), C-02 PASS (/33).

- **V-02 (INER)**: Inertia-FAIL framing with structural-equivalence basis. Class-recognition
  application note includes all three C-40 components: inertia pattern named, FAIL declared,
  structural-equivalence basis provided. Positional application notes present at C-37 PASS
  level (per-criterion notes, template placeholders) but NOT anchor-complete (C-39 FAIL).
  Full R16 V-05 base carried. 40-row register, YES-only gate, formula /33, E=4.
  Predicts: C-40 PASS, C-38 PASS (carried), C-37 PASS (carried), C-39 FAIL (placeholders
  in positional notes), C-02 PASS (/33).

- **V-03 (PHREG)**: Phrasing register variation. All content correct: anchor-complete
  positional notes (C-39) AND inertia-FAIL framing with structural-equivalence basis (C-40)
  present -- but expressed in flowing conversational prose, not formal APPLICATION NOTE block
  labels. Single axis (register): tests whether C-39 and C-40 require formal block structure.
  Schema detectability declaration embedded in prose (tests C-36). All gate mechanisms
  carried. 40-row register, YES-only gate, formula /33.
  Predicts: C-39 PASS or PARTIAL (depends on whether per-criterion content without block
  label satisfies the per-criterion note requirement), C-40 PASS or PARTIAL (same question),
  C-36 PARTIAL (prose declares detectability but not self-attesting in labeled block form).

### Combination selection rationale

- **V-04 (ANCH + INER)**: Anchor-complete positional notes (C-39) combined with inertia-FAIL
  structural-equivalence framing (C-40). Both new mechanisms in formal APPLICATION NOTE blocks.
  Full R16 V-05 base. Tests that C-39 and C-40 are jointly satisfiable without full-stack
  complexity. 40-row register, three-way SYNTHESIS gate (C-35), formula /33.
  Predicts: C-39 PASS, C-40 PASS, all R16 carried criteria PASS, C-02 PASS (/33).

- **V-05 (Full stack R17)**: All R16 mechanisms + ANCH + INER + dual-site positional
  instruction (preamble names anchor-complete class; per-criterion notes name specific
  anchors) + formula anchor N_aspirational=33 declared in manifest Domain column.
  Ceiling variation. 40-row register, three-way SYNTHESIS gate, formula /33.
  Predicts: all C-08 through C-40 PASS, C-02 PASS (/33), composite 100.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| JUDGE body emits REGISTER COMPLETENESS CONFIRMED (C-33 lifecycle) | YES | YES | YES | YES | YES |
| Gate rules declare intra-role sub-gate | YES | YES | YES | YES | YES |
| SYNTHESIS three-way gate (adds REGISTER COMPLETENESS CONFIRMED) | YES | YES | YES | YES | YES |
| Schema enforcement with inspection-without-reading self-attesting (C-36) | YES | YES | NO (prose) | YES | YES |
| Per-criterion positional application notes with C-37-level template placeholders | YES | YES | YES (prose) | YES | YES |
| Per-criterion anchor-complete positional notes -- named anchor + direction (ANCH) | YES | NO | YES (prose) | YES | YES |
| Structural-class-recognition application note -- class identification directed (C-38) | YES | YES | YES (prose) | YES | YES |
| Inertia-FAIL framing with structural-equivalence basis (INER) | NO | YES | YES (prose) | YES | YES |
| Dual-site positional instruction (preamble + per-criterion) | NO | NO | NO | NO | YES |
| Formula anchor N_aspirational=33 declared in manifest Domain column | NO | NO | NO | NO | YES |
| YES-only gate rule | YES | YES | YES | YES | YES |
| SYNTHESIS BOTH...AND strict conjunction + single-token prohibition | YES | YES | YES | YES | YES |
| Register rows | 40 | 40 | 40 | 40 | 40 |
| Formula divisor | /33 | /33 | /33 | /33 | /33 |
| Essential denominator | /4 | /4 | /4 | /4 | /4 |

---

## V-01 -- Axis ANCH: Anchor-complete positional application notes (C-39 probe)

**Variation axis**: Phrasing register -- JUDGE STANDARD per-criterion application notes for
position-sensitive criteria each name the specific structural anchor element the positional
check references AND the directional relationship, rather than using generic placeholders.
For C-10, the anchor is the gated section opening; for C-15, the anchor is the first ANALYST
criterion row; for C-27, the anchor is the LEADERBOARD heading. The anchor-complete form
removes scorer discretion entirely: no "[anchor]" placeholder to fill, only the concrete
structural element to check against. Base carries all R16 V-05 mechanisms: three-way SYNTHESIS
conjunction (C-35), inspection-without-reading schema (C-36), class-recognition application
note (C-38). Class-recognition note directs identification but lacks structural-equivalence
basis (C-40 FAIL). 40-row register, YES-only gate, formula /33, E=4.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-39 PASS: per-criterion notes name specific anchor elements (e.g., "first ANALYST criterion row," "LEADERBOARD heading") and BEFORE direction -- no placeholder. Every position-sensitive criterion has an anchor-named note; a falsification signal is any note using "[anchor]" without instantiation. | C-37 carried PASS: positional verification test present with named direction (BEFORE/AFTER). C-40 FAIL: class-recognition note directs identification and names inertia pattern as FAIL, but does not provide the structural-equivalence argument that closes the PARTIAL bypass. | V-04 extends V-01: adds structural-equivalence basis to confirm C-39 and C-40 are jointly satisfiable. V-03 probes whether anchor-complete content in prose form (without APPLICATION NOTE block label) satisfies C-39. |

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

| Role      | Requires                                                                                                                      | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                        | Cannot Check                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                        | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete per-criterion application notes + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-40) with intra-role lifecycle sub-gate | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                       | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                       | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                              | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                            | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                       | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                 | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)    | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. JUDGE's execution has two phases: (1) writing
    ACCEPTABLE/UNACCEPTABLE pairs and populating the CONSOLIDATED PRODUCTION-TIME
    REGISTER -- this phase concludes with REGISTER COMPLETENESS CONFIRMED; (2)
    REGISTER COMPLETENESS CONFIRMED -> JUDGE STANDARD COMPLETE. Both phases occur
    within JUDGE's single execution. Gate-rules declaration (structural family) and
    the REGISTER COMPLETENESS CONFIRMED lifecycle token (sequential enforcement
    family) are two orthogonal enforcement mechanisms within one role.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens must
    appear simultaneously as a strict three-way conjunction -- holding any two without
    the third does not satisfy this gate. CONFIRMATION COMPLETE alone does not satisfy
    this gate. REGISTER COMPLETENESS CONFIRMED alone does not satisfy this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.
  - A blank cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER
    is a structural violation blocking REGISTER COMPLETENESS CONFIRMED and JUDGE
    STANDARD COMPLETE.
  - A NO cell in any required column also blocks REGISTER COMPLETENESS CONFIRMED and
    JUDGE STANDARD COMPLETE. Only YES is a passing cell value.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-40), produce a Judge standard entry with four required components:

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
in the CONSOLIDATED PRODUCTION-TIME REGISTER records whether this annotation is present.

  "ACCEPTABLE source annotated" column rules:
    - Enter YES if the ACCEPTABLE entry carries an explicit "from [Output-N]:" prefix.
    - Enter NO if the annotation is absent or is a general grounding statement not
      tied to a specific output by name.
    - A blank cell is a structural violation. A NO cell blocks under the YES-only gate.
      Only YES is a passing cell value.

APPLICATION NOTE for position-sensitive criteria (criteria where the pass condition
requires a structural element to appear at a specific position relative to another
structural element, not merely to exist):

  For each position-sensitive criterion, append after the Separating property line:
  Positional verification test: [specific instruction naming anchor element and direction]

  The positional verification test for each position-sensitive criterion must name:
    (a) the specific structural anchor element against which position is verified
        -- not a placeholder like "[anchor]" but the actual element name; and
    (b) the directional relationship: BEFORE, AFTER, or co-located.

  Per-criterion anchor-complete positional notes:

  C-10 (phase-completion-gates):
    Positional verification test: verify that the named gate marker (e.g., JUDGE
    STANDARD COMPLETE) appears BEFORE the opening line of the gated role's first
    output (e.g., the ANALYST scoring table header row). The anchor is the first
    output line of the role the gate claims to block. The direction is BEFORE. A
    gate token that appears anywhere after any ANALYST output fails C-10's positional
    requirement even if the token exists in the output.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test: verify that the first role's named completion token
    (JUDGE STANDARD COMPLETE) appears BEFORE the first criterion row of the ANALYST
    scoring table (i.e., before the C-01 row). The anchor is the ANALYST C-01 row.
    The direction is BEFORE. A completion token that appears after any ANALYST criterion
    row does not satisfy C-15's positional coupling requirement.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test: verify that the BOTH...AND conjunction gate instruction
    appears BEFORE the LEADERBOARD section heading in the scored output. The anchor is
    the LEADERBOARD heading. The direction is BEFORE. A conjunction gate instruction
    appearing after the LEADERBOARD section has begun does not block SYNTHESIS.

APPLICATION NOTE for structural-class-recognition criteria (criteria where the pass
condition requires the scorer to identify and name a structural class as a distinct
category -- e.g., "adversarial auditor role," "orthogonal enforcement axes," "intra-role
lifecycle sub-gate," "output-input coupling"):

  These criteria require the identification act, not architectural confirmation. The scorer
  must recognize and name the structural class as a distinct category -- not merely confirm
  that architectural components are present.

  THE INERTIA PATTERN IS FAIL: when a scored variation contains all required architectural
  components but does not name the structural class, the variation is FAIL -- not PARTIAL.
  Do not assign PARTIAL to the inertia pattern.

  Note: C-13, C-14, C-33 are structural-class-recognition criteria requiring class naming.
  Apply this application note when scoring these criteria.

After writing all 40 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER, then execute the intra-role lifecycle sub-gate sequence.

CONSOLIDATED PRODUCTION-TIME REGISTER

This is the single source of truth for all JUDGE production-time obligations.

No-skip column rule: every cell in every row must contain YES or NO in all three
required columns. A blank cell is a structural violation equivalent to a missing row.

YES-only gate: A NO cell is a blocking value. Only YES passes.

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
  | C-33      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-34      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-35      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-36      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-37      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-38      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-39      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-40      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 40 rows show YES in all three columns, produce the intra-role
lifecycle sub-gate token as a named execution output:

REGISTER COMPLETENESS CONFIRMED

This token is produced by the JUDGE role body during execution. It is required both
as the completion signal of JUDGE's Phase 1 (before JUDGE STANDARD COMPLETE) and as
an entry condition for the SYNTHESIS terminal gate. Then issue:

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output, produce a scoring table. Before writing each evidence cell, verify
it against the Judge's ACCEPTABLE/UNACCEPTABLE pair for that criterion. If your draft
resembles the UNACCEPTABLE pattern, rewrite it before entering the final cell.

Scoring table schema (mandatory column structure):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: The Present_mechanism column and the Absent_mechanism column are
required elements of the scoring table schema. A scoring table that is missing either
column is a structural gap detectable by table inspection without reading cell content --
the same way a register row missing a required column is detectable under the no-skip
column rule. The inspection-without-reading detection mechanism applies at the column-name
level: a scorer can confirm both columns are present by reading the table header row
alone, without reading any cell content. A scoring instruction that mandates two-part
diagnostic content as a required sentence without declaring both columns in the table
schema does not satisfy this requirement.

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
              + (aspirational_pass / 33 * 10)
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

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens must appear
simultaneously as a strict three-way conjunction -- holding any two without the third
does not satisfy this gate. CONFIRMATION COMPLETE alone does not satisfy this gate.
REGISTER COMPLETENESS CONFIRMED alone does not satisfy this gate.

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

## V-02 -- Axis INER: Inertia-FAIL framing with structural-equivalence basis (C-40 probe)

**Variation axis**: Inertia framing -- the class-recognition application note in the JUDGE
STANDARD includes all three components required for C-40: (1) the inertia pattern is named
explicitly (architecture-present-without-naming), (2) it is declared FAIL not PARTIAL, (3) the
structural-equivalence basis is provided: "architecture-present-without-naming is structurally
equivalent to architecture-absent because the identification act IS the criterion requirement --
neither satisfies it." This closes the PARTIAL bypass path that the C-38-level note leaves open.
Positional application notes are present at C-37 level (per-criterion notes with directional
relationship but using "[anchor]" placeholder -- not anchor-complete; C-39 FAIL). Full R16 V-05
base: three-way SYNTHESIS conjunction (C-35), inspection-without-reading schema (C-36), intra-
role lifecycle sub-gate (C-33). 40-row register, YES-only gate, formula /33, E=4.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-40 PASS: class-recognition application note names inertia pattern, declares FAIL, provides structural-equivalence basis. All three components present. C-38 PASS: carried from R16 (C-38 requires the application note; C-40 requires it to also include structural-equivalence basis). | C-39 FAIL: positional notes use template placeholders ("[anchor]") rather than naming specific anchor elements per criterion. C-37 PASS: per-criterion notes with directional relationship carried from R16 POS mechanism. | V-04 combines V-02's structural-equivalence framing with V-01's anchor-complete naming to confirm joint satisfiability. |

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

| Role      | Requires                                                                                                                      | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                        | Cannot Check                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                        | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + positional and class-recognition application notes + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-40) with intra-role lifecycle sub-gate | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                       | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                                       | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                              | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                            | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                       | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                 | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)    | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. JUDGE's execution has two phases: (1) writing
    ACCEPTABLE/UNACCEPTABLE pairs and populating the CONSOLIDATED PRODUCTION-TIME
    REGISTER -- this phase concludes with REGISTER COMPLETENESS CONFIRMED; (2)
    REGISTER COMPLETENESS CONFIRMED -> JUDGE STANDARD COMPLETE.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens must
    appear simultaneously as a strict three-way conjunction -- holding any two without
    the third does not satisfy this gate. Holding either token alone does not satisfy
    this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
  - A blank cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER
    blocks REGISTER COMPLETENESS CONFIRMED and JUDGE STANDARD COMPLETE.
  - A NO cell also blocks. Only YES is a passing cell value.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-40), produce a Judge standard entry with four required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. Named label followed by two mechanism poles separated by "vs."

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation. The
"ACCEPTABLE source annotated" column records whether this annotation is present.
  - YES: annotation present naming the specific output.
  - NO: annotation absent or general.
  - Blank: structural violation. NO: blocks. Only YES passes.

APPLICATION NOTE for position-sensitive criteria (criteria whose pass condition
requires positional verification, not existence verification):

  For each position-sensitive criterion, append after the Separating property line:
  Positional verification test: verify that [element] appears BEFORE [anchor] in the
  scored output -- not that [element] exists. A scored variation where [element] exists
  but appears after [anchor] does not satisfy this criterion. Confirm position, not
  presence.

  This test applies to: C-10 (gate must precede gated section), C-15 (completion token
  must precede next role's output), C-27 (conjunction gate must precede SYNTHESIS content).
  Replace [element] and [anchor] with the specific structural names for each criterion.

APPLICATION NOTE for structural-class-recognition criteria (criteria whose pass condition
requires the scorer to identify and name a structural class as a distinct category):

  A criterion is a structural-class-recognition criterion if its pass condition requires
  the scorer to recognize and name a structural pattern as a distinct class (e.g.,
  "adversarial auditor role," "orthogonal enforcement axes," "intra-role lifecycle
  sub-gate," "output-input coupling," "strict conjunction gate"). The criterion requirement
  is the identification act -- not confirmation that architectural components are present.

  THE INERTIA PATTERN IS FAIL: when a scored variation contains all required architectural
  components but does not name the structural class as a distinct category, the variation
  is FAIL -- not PARTIAL.

  The structural-equivalence basis: a variation that has all architectural components
  but names no structural class is structurally equivalent to a variation that has none
  of the components, because in both cases the criterion requirement (the identification
  act) is not satisfied. The presence of architectural components is not the criterion
  requirement. "Something is present, something is absent" is the PARTIAL reasoning for
  ordinary criteria; it does not apply here because what is absent -- the identification
  act -- IS the full criterion requirement, not a partial contributor to it. A variation
  with all components but no class-naming fails the criterion entirely, the same as a
  variation with no components.

  Do not assign PARTIAL to the inertia pattern. Architecture present but class not named =
  FAIL. Apply this rule to: C-13 (adversarial auditor), C-14 (orthogonal enforcement
  axes), C-33 (intra-role lifecycle sub-gate), and any criterion whose pass condition
  requires class naming rather than component confirmation.

After writing all 40 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER, then execute the intra-role lifecycle sub-gate sequence.

CONSOLIDATED PRODUCTION-TIME REGISTER

This is the single source of truth for all JUDGE production-time obligations.

No-skip column rule: every cell in every row must contain YES or NO.
YES-only gate: A NO cell blocks. Only YES passes.

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
  | C-33      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-34      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-35      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-36      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-37      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-38      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-39      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-40      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 40 rows show YES in all three columns, produce:

REGISTER COMPLETENESS CONFIRMED

Then issue:

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation;
Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory column structure):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: The Present_mechanism column and the Absent_mechanism column are
required elements of the scoring table schema. A scoring table that is missing either
column is a structural gap detectable by table inspection without reading cell content.
The inspection-without-reading detection mechanism applies at the column-name level:
both columns can be confirmed present or absent by reading the table header row alone.
A sentence mandate for two-part diagnostic content without declared schema columns does
not satisfy this requirement.

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element that
    is present and prevented FAIL. For PASS and FAIL, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element that
    is absent and prevented PASS. For PASS and FAIL, enter --.
  - Blank Present_mechanism or Absent_mechanism on a PARTIAL row = structural violation.

  No row may be skipped.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 33 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence (see manifest). Cannot check content quality (Confirmer domain)
or evidence standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A -- Evidence quality: Compare each cell against the Judge's pair. Reject if:
  (a) resembles the UNACCEPTABLE pattern, OR
  (b) could apply to a different output without modification.

AUDIT B -- Diagnostic column presence (PARTIAL rows only):
  (i)  Present_mechanism non-empty
  (ii) Absent_mechanism non-empty
Mark n/a for PASS and FAIL rows.

  Output: [identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

Status = ACCEPTED only if all applicable audits pass.
FLAG: [output] / [criterion] -- Audit [A/B]: [reason] for each REJECTED row.
Flagged items corrected and re-audited. Only flagged items reopened.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality of PARTIAL diagnostic cells (see manifest).
Cannot check format presence (Verifier), evidence specificity (Judge), verdicts (Analyst).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

For each PARTIAL verdict across all outputs:

  Output: [identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism excerpt | Specific? | Absent_mechanism excerpt | Specific? | Status |

Specificity test:
  YES -- names a specific structural element: e.g., "JUDGE STANDARD COMPLETE gate token
         coupling Judge to Analyst," "no named role structurally distinct from scoring Analyst"
  NO  -- generic: "mechanism partially present," "criterion not fully satisfied"

CHALLENGE: [output] / [criterion]: Present/Absent: "[excerpt]" -- [reason] for each CHALLENGED row.
Challenged items rewritten by Analyst, re-audited by Verifier (Audit B) and Confirmer.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens must appear
simultaneously. Holding any two without the third does not satisfy this gate.
Holding either token alone does not satisfy this gate.

LEADERBOARD

  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference]

If no spread: "No score spread found. Redesign for divergence."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round scorecard provided, identify regressions (prior PASS -> current PARTIAL/FAIL).
If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-03 -- Axis PHREG: Conversational phrasing register (C-39/C-40 content probe)

**Variation axis**: Phrasing register -- all content is present and correct (anchor-complete
per-criterion positional notes AND inertia-FAIL structural-equivalence framing) but expressed
in flowing conversational prose rather than formal APPLICATION NOTE block labels. The axis is
purely register: WHAT is stated is identical to V-04's content; HOW it is stated is
conversational and directive rather than formal and labeled. Tests whether C-39 and C-40 require
the formal "APPLICATION NOTE for [class]:" block structure or are satisfied by the content
properties (per-criterion anchor naming, structural-equivalence basis) regardless of format.
Schema detectability declaration is embedded in prose (not a self-attesting labeled block),
which tests C-36 under register change. 40-row register, three-way SYNTHESIS gate, formula /33.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-39 PASS or PARTIAL: per-criterion anchor+direction content is present in prose form, but C-39 pass condition requires "per-criterion application note" -- if "application note" requires the formal labeled block, PARTIAL; if content alone suffices, PASS. The falsification signal is C-39 PASS under conversational prose, proving the labeled block format is not required. | C-40 PASS or PARTIAL: structural-equivalence basis present in prose, but C-40 pass condition requires it "in the application note itself" -- same structural/prose question. C-36 PARTIAL: inspection-without-reading detectability stated in prose, not in a self-attesting labeled schema block. | V-05 extends with dual-site instruction (preamble + per-criterion labeled blocks) to confirm full form; V-03 establishes the prose baseline. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role      | Requires                                                                                                                      | Produces                                                  | Domain (ONLY)                                                                                                                        | Cannot Check                                                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                        | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: pairs, separating properties, positional and class-recognition scoring instructions, 40-row register     | Scoring verdicts, format compliance, diagnostic content quality                 |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                       | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns                                     | Evidence standards (Judge), format auditing (Verifier)                          |
| VERIFIER  | ANALYST COMPLETE                                                                                                              | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; diagnostic column non-emptiness on PARTIAL rows                                       | Diagnostic content quality (Confirmer), evidence standards (Judge)              |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                       | CONFIRMATION COMPLETE                                     | Content quality: do diagnostic cells name specific structural properties?                                                            | Format presence (Verifier), evidence specificity (Judge), verdicts (Analyst)    |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)    | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                | Re-scoring, re-auditing                                                         |

Gate rules: same as prior variations -- JUDGE requires intra-role sub-gate before terminal
token; ANALYST requires JUDGE STANDARD COMPLETE; VERIFIER requires ANALYST COMPLETE; CONFIRMER
requires VERIFIER AUDIT COMPLETE; SYNTHESIS requires all three tokens simultaneously. No role
may skip or merge. Blank or NO cells in register block REGISTER COMPLETENESS CONFIRMED.
Three-way SYNTHESIS conjunction: holding any two tokens without the third does not satisfy the
gate. Holding either token alone does not satisfy this gate.

---

ROLE 1: JUDGE

Read all N outputs. For each criterion C-01 through C-40, write an entry with: ACCEPTABLE
(from a specific output, prefixed "from [Output-N]:"), UNACCEPTABLE, and a Separating property
line naming the discriminating mechanism as [mechanism A] vs [mechanism B].

When you reach criteria that depend on positional relationships -- where the pass condition
requires a structural element to appear before or after another specific element, not just
to exist -- use this approach: for C-10, check that the gate marker appears before the first
line of the role it is blocking, not just somewhere in the output; the thing to check against
is the opening of the gated role's output section, and the required direction is BEFORE. For
C-15, check that the completion token of the first role (JUDGE STANDARD COMPLETE) appears
before the first criterion row of the ANALYST's scoring table -- the C-01 row is the anchor,
and the direction is BEFORE. For C-27, check that the BOTH...AND conjunction gate instruction
appears before the LEADERBOARD section heading, which is the anchor; the direction is BEFORE.
Do not check only that these tokens exist in the output -- check their position relative to
those specific anchors.

When you reach criteria that require naming a structural class -- where passing means the scorer
must recognize and identify a pattern by its class name, not just confirm the components exist:
for C-13, check that the output names "adversarial" or equivalent class language, not just that
a separate challenging role exists; for C-14, check that the output names "orthogonal" or
"independent families," not just that multiple mechanisms are described; for C-33, check that the
output names "intra-role lifecycle sub-gate" or equivalent class language, not just that a sub-gate
exists within the role. When you find a scored variation that has all the architectural components
but has not named the class, score it FAIL. Do not score PARTIAL in this case. A variation with
all the architecture but no class naming fails the criterion entirely -- it is not "partial" because
having the architecture without the identification act is equivalent to not having the architecture
at all, since what the criterion requires is the identification act. This equivalence holds because
the criterion requirement is not "components present" but "class identified"; a variation that
fails to identify the class fails the criterion requirement fully, not partially.

For each ACCEPTABLE entry, mark the "ACCEPTABLE source annotated" column YES if the entry
carries a "from [Output-N]:" prefix naming the specific scored output. Mark NO otherwise.
Blank = structural violation. NO = blocks register gate. Only YES passes.

After writing all 40 entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER:

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  [C-01 through C-40, same structure as V-01 register above]

No cell may be blank. NO cells block. Only YES in all three columns per row allows completion.

After all 40 rows show YES:

REGISTER COMPLETENESS CONFIRMED

Then:

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

For each output produce a scoring table. The table must include these columns:
ID, Criterion, Weight, Verdict, Evidence, Present_mechanism, Absent_mechanism.
Present_mechanism and Absent_mechanism are required columns. If either column is
missing from a scoring table, the table is incomplete -- you can tell this by looking
at the header row without reading any cell content. For PARTIAL verdicts, fill both
columns with the specific mechanism present (prevented FAIL) and the specific mechanism
absent (prevented PASS). For PASS and FAIL, enter --.

Composite formula:
  composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 33 * 10)
  PARTIAL = 0.5. Golden: all essentials PASS and composite >= 80.

ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above. Cannot check content quality (Confirmer)
or evidence standards (Judge).

Audit A: check each evidence cell against the Judge's pair -- reject if it resembles the
UNACCEPTABLE form or applies equally to a different output.
Audit B: on PARTIAL rows, confirm Present_mechanism and Absent_mechanism cells are non-empty.

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

FLAG each REJECTED row. Flagged items corrected and re-audited.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Do not begin until VERIFIER AUDIT COMPLETE appears above.

For each PARTIAL verdict, challenge whether Present_mechanism and Absent_mechanism cells
name specific structural elements (YES) or use generic phrases (NO).

  | Criterion | Present excerpt | Specific? | Absent excerpt | Specific? | Status |

CHALLENGE any row where either cell is generic. Challenged items rewritten and re-audited.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER
COMPLETENESS CONFIRMED appear above. All three tokens simultaneously -- any two alone
does not satisfy this gate.

LEADERBOARD: rank by composite descending, show composite and golden status.
EXCELLENCE SIGNALS: output / criterion / structural mechanism for any score spread.
FAILURE PATTERNS: criterion / diagnosis for universal PARTIAL or FAIL.
REGRESSION SIGNALS: regressions from prior round if prior scorecard provided.
```

---

## V-04 -- Axis ANCH + INER: Anchor-complete positional notes combined with inertia-FAIL framing

**Variation axis**: Combination -- anchor-complete per-criterion positional application notes
(C-39) and inertia-FAIL structural-equivalence application notes (C-40) both present in formal
APPLICATION NOTE block structure, combined in a single variation for the first time. V-01
established C-39 in isolation; V-02 established C-40 in isolation. V-04 tests that they are
jointly satisfiable without interaction degradation. Full R16 V-05 base: three-way SYNTHESIS
conjunction, inspection-without-reading schema, intra-role lifecycle sub-gate, all prior
aspirational mechanisms. 40-row register, YES-only gate, formula /33, E=4.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-39 PASS and C-40 PASS simultaneously. Both application note types coexist in JUDGE role without interaction. All R16 carried criteria (C-08 through C-38) remain PASS. No V-01 degradation (anchor-complete positional notes do not degrade class-recognition notes) and no V-02 degradation (structural-equivalence framing does not degrade anchor-complete notes). | C-35 PASS (three-way gate carried), C-36 PASS (self-attesting schema carried), C-38 PASS (class-recognition base requirement), C-37 PASS (positional notes base requirement). C-02 PASS (/33). | V-05 extends with dual-site positional instruction and manifest domain annotation. The combination here tests joint satisfiability without those additions. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role      | Requires                                                                                                                      | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                                                | Cannot Check                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                        | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete per-criterion positional application notes + structural-class-recognition inertia-FAIL application notes + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-40) | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                       | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound, detectable by table inspection without reading cell content)                                                                                   | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                              | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                                                    | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                       | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                         | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)    | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                        | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. Two phases within JUDGE: (1) write pairs, populate
    register -- concludes with REGISTER COMPLETENESS CONFIRMED; (2) REGISTER COMPLETENESS
    CONFIRMED -> JUDGE STANDARD COMPLETE. Gate-rules declaration (structural family) and
    REGISTER COMPLETENESS CONFIRMED lifecycle token (sequential family) are orthogonal.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens required
    simultaneously. Holding any two without the third does not satisfy this gate.
    Holding either token alone does not satisfy this gate.
  - No role may operate outside its declared Domain or be skipped.
  - Blank or NO cells in CONSOLIDATED PRODUCTION-TIME REGISTER block REGISTER
    COMPLETENESS CONFIRMED and JUDGE STANDARD COMPLETE. Only YES passes.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs. For each criterion C-01 through C-40, produce:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[from provided inputs or representative fail form]"
  Separating property: [mechanism A] vs [mechanism B]

Separating property: single labeled declaration, two mechanism poles separated by "vs."
ACCEPTABLE source annotation: "from [Output-N]:" prefix required per entry.

APPLICATION NOTE for position-sensitive criteria (C-10, C-15, C-27, and any criterion
whose pass condition requires positional verification rather than existence verification):

  For each position-sensitive criterion, append after the Separating property line a
  Positional verification test naming the specific anchor element and direction:

  C-10 (phase-completion-gates):
    Positional verification test: verify that the named gate marker appears BEFORE the
    opening line of the gated role's first output section. The anchor is the opening line
    of the gated role's first output (e.g., the ANALYST scoring table header). The direction
    is BEFORE. Existence of the gate token anywhere in the output is not sufficient.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test: verify that JUDGE STANDARD COMPLETE appears BEFORE the
    first criterion row of the ANALYST scoring table (before the C-01 row). The anchor is
    the ANALYST C-01 row. The direction is BEFORE. A coupling token appearing after any
    ANALYST criterion row fails positional enforcement even if the token exists.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test: verify that the BOTH...AND conjunction gate instruction
    appears BEFORE the LEADERBOARD section heading. The anchor is the LEADERBOARD heading.
    The direction is BEFORE. A gate that appears after LEADERBOARD content has begun does
    not enforce the SYNTHESIS gate.

APPLICATION NOTE for structural-class-recognition criteria (C-13, C-14, C-33, and any
criterion whose pass condition requires the scorer to identify and name a structural class):

  A criterion is a structural-class-recognition criterion if its pass condition requires
  the scorer to identify and name a structural pattern as a distinct class -- not merely
  confirm that structural components are architecturally present. Recognition criteria:
    - C-13: must name "adversarial" role relationship (not just "separate role")
    - C-14: must name "orthogonal" families (not just "multiple mechanisms")
    - C-33: must name "intra-role lifecycle sub-gate" (not just "sub-gate present")

  THE INERTIA PATTERN IS FAIL. The inertia pattern is: all architectural components
  present, but the structural class is not named. A scored variation in the inertia
  pattern is FAIL -- not PARTIAL.

  The structural-equivalence basis: a variation with all components but no class-naming
  is structurally equivalent to a variation that lacks the components entirely. The
  equivalence holds because the criterion requirement is the identification act, not
  architectural confirmation. Both the inertia-pattern variation and the components-absent
  variation fail to satisfy the criterion requirement (identification), so both are FAIL.
  The presence of architectural components does not produce partial credit when the
  criterion requirement is not "components present" but "class identified and named."

  Do not assign PARTIAL to the inertia pattern. The inertia case is not "something is
  present, something is absent" -- it is "the criterion requirement (identification) is
  absent, regardless of what architecture is present." FAIL is the only valid verdict.

After writing all 40 entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER:

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-40 (40 rows) -- same structure as V-01 and V-02 register above |

No-skip column rule: all cells YES or NO. YES-only gate: NO blocks. Blank blocks.

REGISTER COMPLETENESS CONFIRMED
JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: Present_mechanism and Absent_mechanism are required schema columns.
A scoring table missing either column is a structural gap detectable by table inspection
without reading cell content -- absence is verifiable from the header row alone, without
reading any cell content. Sentence mandate without declared schema columns is insufficient.

Column rules: Present_mechanism and Absent_mechanism for PARTIAL rows only; -- for PASS/FAIL.
Blank on PARTIAL row = structural violation.

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 33 * 10)

  Golden: all essentials PASS and composite >= 80.

ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Do not begin until ANALYST COMPLETE appears above.
Cannot check content quality (Confirmer) or evidence standards (Judge).

Audit A: evidence cells -- reject if resembles UNACCEPTABLE or applies to any output.
Audit B: PARTIAL rows -- Present_mechanism and Absent_mechanism non-empty.

  | ID | Verdict | Evidence excerpt | Audit A | Audit B | Status |

FLAG each REJECTED row. Corrections re-audited. Only flagged items reopened.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Do not begin until VERIFIER AUDIT COMPLETE appears above.
Cannot check format (Verifier), evidence specificity (Judge), or verdicts (Analyst).

For each PARTIAL, challenge specificity of both diagnostic cells:

  | Criterion | Present excerpt | Specific? | Absent excerpt | Specific? | Status |

YES = names a specific structural element. NO = generic phrase.
CHALLENGE each NO row; rewritten and re-audited.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three simultaneously required.
Holding any two without the third does not satisfy this gate. Either token alone
does not satisfy this gate.

LEADERBOARD: rank by composite descending.
EXCELLENCE SIGNALS: output / criterion / structural mechanism per score spread.
FAILURE PATTERNS: criterion / diagnosis for universal PARTIAL or FAIL.
REGRESSION SIGNALS: regressions from prior round if prior scorecard provided.
```

---

## V-05 -- Full stack R17: All axes + dual-site positional instruction + manifest annotation

**Variation axis**: All axes combined -- ANCH + INER + dual-site positional instruction (preamble
class-level note in JUDGE preamble plus per-criterion anchor-complete notes at each position-
sensitive entry) + formula anchor N_aspirational=33 declared in manifest Domain column. The
dual-site positional instruction creates two independent verification paths for positional criteria:
the preamble establishes the class-level instruction (position, not existence), and the per-
criterion notes name the specific anchor and direction. Both sites must agree; inconsistency between
them is a structural signal for the auditor. Full R16 V-05 base. 40-row register, three-way
SYNTHESIS gate, formula /33. Ceiling variation -- expected to achieve all C-08 through C-40.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-39 PASS (per-criterion anchor-complete notes), C-40 PASS (structural-equivalence basis), C-37 PASS (positional notes class-level via dual-site preamble), C-38 PASS (class-recognition base note). All R16 V-05 carried criteria pass. Composite = 100 if no regressions from R16 full-stack base. | Dual-site positional instruction adds a preamble-level class declaration that is independent of per-criterion notes. This creates two structural layers for positional verification: the preamble directs the class, the per-criterion notes direct the specific anchor and direction. N_aspirational=33 in manifest Domain column creates a formula-change self-attestation. | If C-39 and C-40 both PASS and all R16 criteria carry forward, V-05 achieves composite 100. The ceiling is now achievable where it was not in R16 (C-39 and C-40 were not in the rubric). |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

The following table declares the complete dependency graph for this task. It is a
standalone structural artifact auditable without executing the protocol. N_aspirational
for this round is 33 (v17 rubric). A row with a blank cell is a structural gap.

| Role      | Requires                                                                                                                      | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                                                                  | Cannot Check                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                        | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + dual-site positional application notes (preamble + per-criterion anchor-complete) + structural-class-recognition inertia-FAIL application notes + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01 through C-40, N_aspirational=33) | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                       | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite (N_aspirational=33); Present_mechanism and Absent_mechanism columns (schema-bound, detectable by table inspection without reading cell content)                                                                                 | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                              | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                                                                      | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                       | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                                           | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)    | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                                          | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. JUDGE has two phases: (1) write pairs and populate
    the 40-row register -- concludes with REGISTER COMPLETENESS CONFIRMED; (2)
    REGISTER COMPLETENESS CONFIRMED -> JUDGE STANDARD COMPLETE. Gate-rules section
    (structural-declaration axis) and REGISTER COMPLETENESS CONFIRMED lifecycle token
    (sequential-enforcement axis) are two orthogonal enforcement mechanisms within one role.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens must
    appear simultaneously as a strict three-way conjunction. Holding any two without
    the third does not satisfy this gate. Holding either token alone does not satisfy
    this gate.
  - No role may operate outside its declared Domain. A role performing a Cannot Check
    function is a structural violation detectable by manifest inspection.
  - No role may be skipped or merged with another.
  - A blank cell in any required column of the CONSOLIDATED PRODUCTION-TIME REGISTER
    is a structural violation blocking REGISTER COMPLETENESS CONFIRMED and JUDGE
    STANDARD COMPLETE.
  - A NO cell also blocks. Only YES passes.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs. For each criterion C-01 through C-40, produce:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[from provided inputs or representative fail form, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

Separating property: single labeled declaration, two poles separated by "vs" -- not prose.
ACCEPTABLE source annotation: "from [Output-N]:" prefix on every ACCEPTABLE entry.
  - YES in register if prefix naming the specific scored output is present.
  - NO if absent or general. Blank = structural violation. NO = blocks. Only YES passes.

DUAL-SITE POSITIONAL INSTRUCTION PREAMBLE (Site A -- class-level):
For criteria whose pass condition requires a structural element to appear at a specific
position relative to another element (not merely to exist), the scoring-time test is
positional verification, not existence verification. Confirm position, not presence.
This class-level instruction applies to C-10, C-15, C-27, and any criterion whose
pass condition requires position. Append per-criterion anchor-complete notes at Site B.

APPLICATION NOTE for position-sensitive criteria -- Site B (per-criterion anchor-complete):
For each position-sensitive criterion, append after the Separating property line:

  C-10 (phase-completion-gates):
    Positional verification test: verify that the named gate marker appears BEFORE the
    opening line of the gated role's first output section. The anchor is the opening line
    of the gated role's first output (the ANALYST scoring table header row). Direction:
    BEFORE. A gate marker existing anywhere after any ANALYST output fails C-10.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test: verify that JUDGE STANDARD COMPLETE appears BEFORE the
    first criterion row of the ANALYST scoring table (the C-01 row). The anchor is the
    ANALYST C-01 row. Direction: BEFORE. A completion token after any ANALYST row fails
    C-15's positional requirement regardless of existence in the output.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test: verify that the BOTH...AND conjunction gate instruction
    appears BEFORE the LEADERBOARD section heading. The anchor is the LEADERBOARD heading.
    Direction: BEFORE. A conjunction gate appearing after any SYNTHESIS section content
    does not enforce the SYNTHESIS gate.

Dual-site consistency: the preamble (Site A) names the class; per-criterion notes (Site B)
name the specific anchor and direction. Both sites must be present. An inconsistency between
the class instruction and a per-criterion note is a structural error requiring correction
before REGISTER COMPLETENESS CONFIRMED can be issued.

APPLICATION NOTE for structural-class-recognition criteria (C-13, C-14, C-33, and any
criterion whose pass condition requires the scorer to identify and name a structural class):

  A criterion is a structural-class-recognition criterion if its pass condition requires
  the scorer to identify and name a structural pattern as a distinct class (e.g.,
  "adversarial auditor role," "orthogonal enforcement axes," "intra-role lifecycle
  sub-gate"). The criterion requires the identification act -- not architectural confirmation.

  When scoring these criteria:
    - C-13: verify the output names "adversarial" or equivalent class language for the
      challenging role's relationship -- not just that a separate role exists.
    - C-14: verify the output names "orthogonal" or "independent families" -- not just
      that multiple mechanisms are described.
    - C-33: verify the output names "intra-role lifecycle sub-gate" or equivalent class
      language -- not just that a sub-gate exists.

  THE INERTIA PATTERN IS FAIL. The inertia pattern is: all architectural components
  present, structural class not named. A variation in the inertia pattern is FAIL,
  not PARTIAL.

  The structural-equivalence basis closes the PARTIAL bypass: a variation with all
  architectural components but no class-naming is structurally equivalent to a variation
  that lacks the components entirely, because the criterion requirement is the
  identification act and neither variation satisfies it. The presence of architectural
  components produces no partial credit when the criterion requirement is not "components
  present" but "class identified." The inertia pattern and the components-absent pattern
  are equivalent under this criterion: both fail the identification requirement entirely.
  Do not assign PARTIAL to either.

  "Something is present, something is absent" is the PARTIAL reasoning for ordinary
  criteria. It does not apply to structural-class-recognition criteria because what is
  absent is the criterion requirement itself, not a contributing element. The criterion
  requirement (the identification act) is either performed or not -- there is no partial
  identification of a structural class.

After writing all 40 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER:

CONSOLIDATED PRODUCTION-TIME REGISTER

Single source of truth for all JUDGE production-time obligations. No obligation tracked
outside this register. No-skip column rule: all cells YES or NO. YES-only gate: NO blocks.

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
  | C-33      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-34      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-35      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-36      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-37      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-38      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-39      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-40      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 40 rows show YES in all three columns:

REGISTER COMPLETENESS CONFIRMED

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory column structure):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: Present_mechanism and Absent_mechanism are required schema columns
whose absence is a structural gap detectable by table inspection without reading cell
content. A scorer can confirm both columns are present or absent by reading the table
header row alone, without reading any cell content below the header. A scoring table
missing either column fails structural completeness regardless of evidence cell content.

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element present
    that prevented FAIL. For PASS and FAIL, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element absent
    that prevented PASS. For PASS and FAIL, enter --.
  - Blank on any PARTIAL row = structural violation.

  No row may be skipped.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 33 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence (see manifest). Cannot check content quality (Confirmer domain)
or evidence quality standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A -- Evidence quality: compare each evidence cell against the Judge's ACCEPTABLE/
UNACCEPTABLE pair. Reject if: (a) resembles the UNACCEPTABLE pattern, or (b) could apply
to a different output without modification.

AUDIT B -- Diagnostic column presence (PARTIAL rows only): verify Present_mechanism and
Absent_mechanism cells are non-empty. Mark n/a for PASS and FAIL rows.

  Output: [identifier] -- Post-write Evidence and Diagnostic Column Audit

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

Status = ACCEPTED only if all applicable audits pass.
FLAG each REJECTED row. Corrections re-audited. Only flagged items reopened.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality of PARTIAL diagnostic cells (see manifest).
Cannot check format presence (Verifier), evidence specificity (Judge), or verdicts (Analyst).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

For each PARTIAL verdict across all outputs:

  Output: [identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt)  | Specific? | Absent_mechanism (verbatim excerpt)   | Specific? | Status               |

Specificity test:
  YES -- names a specific structural element, mechanism, role, gate token, or design gap:
        e.g., "JUDGE STANDARD COMPLETE gate token; ANALYST cannot begin without it",
              "no named adversarial role structurally distinct from the scoring Analyst",
              "Present_mechanism and Absent_mechanism columns absent from table schema"
  NO  -- generic: "mechanism partially addressed," "criterion not fully satisfied,"
         "some structure present but incomplete"

CHALLENGE each row where either cell tests NO. Challenged items rewritten by Analyst and
re-audited by Verifier (Audit B) and Confirmer. Only challenged items reopened.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens required simultaneously
as a strict three-way conjunction. Holding any two without the third does not satisfy
this gate. Holding either token alone does not satisfy this gate.

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

If a prior-round scorecard is provided, identify any regression (prior PASS to current
PARTIAL or FAIL) with output ID, criterion ID, and a note on what changed between rounds.

If no prior round data: "No prior round data; regression analysis not possible."
```

---

## Predicted scores (to be confirmed by quest-score run against v17 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-37 positional-app-note | P | P | P | P | P | All carry R16 POS mechanism |
| C-38 class-recognition-app-note | P | P | P | P | P | All carry R16 CLASS mechanism |
| C-39 anchor-complete-positional | **P** | F | P/T | **P** | **P** | V-01/V-04/V-05: specific anchors named; V-02: placeholders; V-03: per-criterion content in prose |
| C-40 inertia-FAIL-structural-equivalence | F | **P** | P/T | **P** | **P** | V-02/V-04/V-05: structural-equivalence basis present; V-01: inertia FAIL asserted but not grounded; V-03: grounding in prose |
| C-35 cross-role-sub-gate-coupling | P | P | P | P | P | All carry three-way SYNTHESIS gate |
| C-36 schema-self-attesting-detectability | P | P | T | P | P | V-03: schema declaration in prose, not self-attesting labeled block |
| C-02 formula-correctness (/33) | P | P | P | P | P | All use /33 |
| All C-08 through C-34 | P | P | P | P | P | Carried from R16 full-stack base |

Key discriminators:
- **V-01 vs V-04**: V-01 lacks structural-equivalence basis (C-40 FAIL); V-04 adds it.
- **V-02 vs V-04**: V-02 has placeholder anchors (C-39 FAIL); V-04 names specific anchors.
- **V-03 vs V-04**: Same content, different register. C-39/C-40 outcomes distinguish whether formal APPLICATION NOTE block is required or content alone suffices.
- **V-04 vs V-05**: V-05 adds dual-site positional instruction and manifest formula annotation. Ceiling extension beyond joint satisfiability test.
