# quest-score Variations -- Round 18
**Skill**: quest-score
**Rubric**: v18 (N_essential=4, N_recommended=3, N_aspirational=35)
**Date**: 2026-03-15
**Round**: 18

---

## Design logic

### Unachieved ceiling entering R18

R17 was scored against rubric v17 (N_aspirational=33). R17 V-05 (full stack) achieved all
33 aspirational criteria including C-39 (anchor-complete positional notes) and C-40
(inertia-FAIL structural-equivalence framing). Rubric v18 adds 2 new aspirational criteria
(C-41, C-42) derived from R17 scorecard patterns.

| Criterion | R17 status | Gap analysis |
|-----------|------------|--------------|
| C-41 | **ACHIEVED R17** | Positional classification label. R17 JUDGE STANDARD notes for C-10 and C-15 carry "Positional verification test (C-39 applies here):" tag. C-41 is already satisfied in R17 V-05. R18 must carry it and confirm it appears on all positional criteria (C-10, C-15, C-27). |
| C-42 | NOT IN RUBRIC | Structural-class-recognition classification label. Parallel to C-41: each structural-class-recognition application note must carry a classification label ("Structural-class-recognition criterion (C-38/C-40 applies here):" or equivalent) making the set of structural-class-recognition criteria enumerable by label-scan alone without reading note content. C-40 is achieved (inertia-FAIL declaration present) but the note is not labeled as a structural-class-recognition note. C-42 names whether the label is present. |

### Formula change

N_aspirational increases from 33 to 35. All variations update the composite formula
from `aspirational_pass / 33 * 10` to `aspirational_pass / 35 * 10`. The CONSOLIDATED
PRODUCTION-TIME REGISTER expands from 40 rows to 42 rows (C-01 through C-42). Both
updates are required infrastructure for every R18 variation.

### New mechanism gap: C-42

**For C-42 (structural-class-recognition classification label -- CLBL):**
C-40 requires the structural-class-recognition application note to include an explicit
inertia-pattern-equals-FAIL declaration with structural-equivalence basis. A note satisfying
C-40 is inertia-declaration-complete without necessarily being labeled as a structural-class-
recognition note. C-42 requires the classification label itself -- "Structural-class-recognition
criterion (C-38/C-40 applies here):" or equivalent -- attached to each application note entry.
This label makes the set of structural-class-recognition criteria enumerable by scanning the
JUDGE STANDARD for the label tag alone, without reading any note's inertia declaration.

The three structural-class-recognition criteria in the current rubric: C-13 (adversarial auditor
role), C-14 (orthogonal enforcement axes), C-33 (intra-role lifecycle sub-gate). Each criterion
requires the scorer to identify and name a structural class as a distinct category.

Test for C-42:
- PASS: Each structural-class-recognition application note entry carries an explicit
  classification label at the note entry itself (not in a preamble or section header).
  A reviewer can enumerate C-13, C-14, C-33 as structural-class-recognition criteria by
  scanning for the label tag without reading any note content.
- PARTIAL: Some structural-class-recognition notes carry the label but not all; or the
  label appears in a preamble but not attached to each per-criterion note entry.
- FAIL: No classification labels on structural-class-recognition notes; or classification
  label present only in a preamble, not per-criterion.

### C-41 carry-forward requirement

C-41 is achieved in R17 V-05. Every R18 variation must carry C-41 forward:
- Each positional application note entry carries "Positional verification test (C-39 applies here):"
  label tag at the note entry itself.
- Position-sensitive criteria: C-10, C-15, C-27.
- A reviewer can enumerate C-10, C-15, C-27 as position-sensitive criteria by scanning
  for the label tag without reading any note content.

### New axes for R18

| Axis | Label | Mechanism |
|------|-------|-----------|
| CLBL | Structural-class-recognition classification label | JUDGE STANDARD per-criterion structural-class-recognition notes carry explicit classification label ("Structural-class-recognition criterion (C-38/C-40 applies here):") making the set enumerable by label-scan. Closes C-42. |
| PRBL | Preamble classification families enumeration | A preamble section before per-criterion notes enumerates both classification families (position-sensitive and structural-class-recognition) by criterion ID. Tests whether preamble-level enumeration satisfies C-42 without per-criterion labels. |
| TAGINL | Tag-inline (phrasing register) | All classification content correct -- C-41 and C-42 labels present -- but expressed as inline prose sentences rather than formal tag format. Tests whether C-41/C-42 require formal "(C-NN applies here):" tag syntax or are satisfied by prose-embedded classification language. |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (CLBL)**: Structural-class-recognition classification labels. Per-criterion notes for
  C-13, C-14, C-33 each carry "Structural-class-recognition criterion (C-38/C-40 applies here):"
  label at the note entry. C-41 positional labels carried from R17. Full R17 V-05 base. 42-row
  register, YES-only gate, formula /35, E=4.
  Predicts: C-42 PASS, C-41 PASS (carried), C-40 PASS (carried), C-39 PASS (carried),
  C-02 PASS (/35).

- **V-02 (PRBL)**: Preamble-level classification families enumeration. A "Classification families
  summary" section is added before per-criterion notes, listing position-sensitive criteria
  (C-10, C-15, C-27) and structural-class-recognition criteria (C-13, C-14, C-33) by ID.
  Per-criterion structural-class notes are C-40 complete but NOT labeled (no per-criterion
  "Structural-class-recognition criterion" tag). C-41 positional labels carried. Full R17 V-05
  base. 42-row register, formula /35.
  Predicts: C-42 PARTIAL or FAIL (preamble enumeration vs per-criterion labels), C-41 PASS
  (carried per-criterion labels), C-40 PASS (carried), C-02 PASS (/35).

- **V-03 (TAGINL)**: Phrasing register (prose labels). All classification content correct:
  C-41 and C-42 labels present -- but expressed as inline prose rather than formal tag format.
  Positional notes say "This is a position-sensitive criterion to which C-39/C-41 applies."
  Class-recognition notes say "This is a structural-class-recognition criterion to which
  C-38/C-40/C-42 applies." Tests whether formal "(C-42 applies here):" tag format is required
  by C-41/C-42 or whether inline prose classification satisfies the label requirement. 42-row
  register, formula /35.
  Predicts: C-41 PARTIAL (inline prose vs formal tag), C-42 PARTIAL (same reason), C-39 PASS
  (anchor content present, carried), C-40 PASS (inertia declaration present, carried).

### Combination selections (V-04, V-05)

- **V-04 (CLBL + PRBL)**: Structural-class-recognition labels (C-42) combined with preamble
  classification families enumeration. Both per-criterion labels AND preamble enumeration present.
  Full R17 V-05 base. Tests whether adding preamble to per-criterion labels creates any
  interaction effect. 42-row register, formula /35.
  Predicts: C-42 PASS (per-criterion labels present), C-41 PASS (carried), all R17 carried
  criteria PASS, C-02 PASS (/35).

- **V-05 (Full stack R18)**: All R17 mechanisms + CLBL + PRBL + formula-anchor in manifest
  Domain column declares N_aspirational=35 + dual-family dual-site enumeration (preamble lists
  both families; per-criterion notes carry both label types). Ceiling variation. 42-row register,
  three-way SYNTHESIS gate, formula /35.
  Predicts: all C-08 through C-42 PASS, C-02 PASS (/35), composite 100.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| JUDGE body emits REGISTER COMPLETENESS CONFIRMED (C-33 lifecycle) | YES | YES | YES | YES | YES |
| Gate rules declare intra-role sub-gate | YES | YES | YES | YES | YES |
| SYNTHESIS three-way gate (BOTH...AND...AND strict conjunction) | YES | YES | YES | YES | YES |
| Single-token prohibition complement on SYNTHESIS gate | YES | YES | YES | YES | YES |
| Schema enforcement with inspection-without-reading self-attesting (C-36) | YES | YES | YES | YES | YES |
| Anchor-complete positional notes with named anchor + direction (C-39) | YES | YES | YES | YES | YES |
| Positional classification label per note entry -- "Positional verification test (C-39 applies here):" (C-41) | YES | YES | NO (prose) | YES | YES |
| Structural-class-recognition application note -- inertia-FAIL with structural-equivalence basis (C-40) | YES | YES | YES | YES | YES |
| Structural-class-recognition label per note entry -- "Structural-class-recognition criterion (C-38/C-40 applies here):" (C-42) | YES | NO | NO (prose) | YES | YES |
| Classification families preamble enumerating both families by criterion ID (PRBL) | NO | YES | NO | YES | YES |
| Formula anchor N_aspirational=35 declared in manifest Domain column | NO | NO | NO | NO | YES |
| YES-only gate rule | YES | YES | YES | YES | YES |
| Register rows | 42 | 42 | 42 | 42 | 42 |
| Formula divisor | /35 | /35 | /35 | /35 | /35 |
| Essential denominator | /4 | /4 | /4 | /4 | /4 |

---

## V-01 -- Axis CLBL: Structural-class-recognition classification labels (C-42 probe)

**Variation axis**: Classification label -- JUDGE STANDARD per-criterion application notes
for structural-class-recognition criteria (C-13, C-14, C-33) each carry an explicit
classification label at the note entry itself: "Structural-class-recognition criterion
(C-38/C-40 applies here):". This label makes the set of structural-class-recognition criteria
enumerable by scanning the JUDGE STANDARD for the label tag alone, without reading any note's
inertia declaration content. C-41 positional labels carried from R17. Full R17 V-05 base:
anchor-complete positional notes (C-39), inertia-FAIL structural-equivalence framing (C-40),
three-way SYNTHESIS gate, inspection-without-reading schema (C-36), intra-role lifecycle
sub-gate (C-33/C-35). 42-row register, YES-only gate, formula /35, E=4.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-42 PASS: structural-class-recognition notes for C-13, C-14, C-33 each carry "Structural-class-recognition criterion (C-38/C-40 applies here):" label at the note entry. A reviewer can enumerate these criteria by label-scan without reading inertia declaration content. C-40 PASS: carried (inertia-FAIL declaration + structural-equivalence basis present in each note). C-41 PASS: carried (positional labels present for C-10, C-15, C-27). | C-02 PASS (/35 denominator). All R17 V-05 carried criteria remain PASS. No preamble-level enumeration (PRBL absent): C-42 is satisfied by per-criterion labels alone without a preamble summary. | V-04 adds PRBL to confirm C-42 still passes and preamble creates no degradation. V-02 tests preamble without per-criterion labels to separate the contribution of each mechanism. |

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

| Role      | Requires                                                                                                                                    | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                                         | Cannot Check                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                                      | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete positional notes (C-41 labeled) + structural-class-recognition notes (C-42 labeled) + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01--C-42) with intra-role lifecycle sub-gate | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                                     | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                                                       | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                                            | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                                            | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                                     | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                 | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)                   | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                 | Re-scoring, re-auditing                                                                                   |

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
    the third does not satisfy this gate. Holding either token alone does not satisfy
    this gate.
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
C-42), produce a Judge standard entry with four required components:

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

  For each position-sensitive criterion, the application note entry must carry the
  classification label at the entry itself, then name the anchor and direction:

  Positional verification test (C-39 applies here): verify that [specific element]
  appears [BEFORE / AFTER / co-located with] [specific anchor element] in the scored
  output -- not that [element] exists anywhere in the output. A scored variation where
  [element] exists but appears on the wrong side of [anchor] fails this criterion.

  The classification label "Positional verification test (C-39 applies here):" must
  appear as the first line of each positional application note entry. This label makes
  the set of position-sensitive criteria in the JUDGE STANDARD enumerable by scanning
  for the label tag without reading each note's anchor and direction content.

  Per-criterion anchor-complete positional notes:

  C-10 (phase-completion-gates):
    Positional verification test (C-39 applies here): verify that the named gate marker
    (e.g., JUDGE STANDARD COMPLETE) appears BEFORE the opening line of the gated role's
    first output (e.g., the ANALYST scoring table header row). The anchor is the first
    output line of the role the gate claims to block. The direction is BEFORE. A gate
    token appearing anywhere after any ANALYST output fails C-10's positional requirement
    even if the token exists.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test (C-39 applies here): verify that the first role's named
    completion token (JUDGE STANDARD COMPLETE) appears BEFORE the first criterion row of
    the ANALYST scoring table (i.e., before the C-01 row). The anchor is the ANALYST C-01
    row. The direction is BEFORE. A completion token appearing after any ANALYST criterion
    row does not satisfy C-15's positional coupling requirement.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test (C-39 applies here): verify that the BOTH...AND conjunction
    gate instruction appears BEFORE the LEADERBOARD section heading in the scored output.
    The anchor is the LEADERBOARD heading. The direction is BEFORE. A conjunction gate
    instruction appearing after the LEADERBOARD section has begun does not block SYNTHESIS.

APPLICATION NOTE for structural-class-recognition criteria (criteria where the pass
condition requires the scorer to identify and name a structural class as a distinct
category -- e.g., "adversarial auditor role," "orthogonal enforcement axes," "intra-role
lifecycle sub-gate"):

  For each structural-class-recognition criterion, the application note entry must carry
  the classification label at the entry itself:

  Structural-class-recognition criterion (C-38/C-40 applies here): [identification
  instruction directing the scorer to recognize and name the structural class] +
  [inertia-FAIL declaration with structural-equivalence basis]

  The classification label "Structural-class-recognition criterion (C-38/C-40 applies
  here):" must appear as the first line of each structural-class-recognition application
  note entry. This label makes the set of structural-class-recognition criteria in the
  JUDGE STANDARD enumerable by scanning for the label tag without reading each note's
  inertia declaration content.

  Per-criterion structural-class-recognition notes:

  C-13 (adversarial-auditor):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the adversarial auditor role as a structurally distinct entity whose function is to
    challenge evidence produced by another role. The adversarial relationship -- not the
    audit obligation alone -- is the structural class. A scored variation that has a
    named role performing auditing functions satisfies this criterion only if that role
    is structurally separated from the primary scorer AND produces an independent output.
    THE INERTIA PATTERN IS FAIL: a scored variation where adversarial auditing happens
    architecturally (two roles exist, audit occurs) but the adversarial class is not
    identified as a distinct structural category is FAIL -- not PARTIAL. This is
    structurally equivalent to a variation with no adversarial role, because the criterion
    requirement is the identification act: recognizing and naming the adversarial auditor
    as a structural class. Architecture-present-without-naming = structurally equivalent
    to architecture-absent. Do not assign PARTIAL to the inertia pattern.

  C-14 (orthogonal-enforcement-axes):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the orthogonality relationship between enforcement mechanisms as a distinct structural
    class. Two mechanisms are orthogonal when they operate on independent enforcement
    dimensions (role-based, sequential, structural, content-validation). Two sequential
    phases are not orthogonal -- they are the same axis repeated. The orthogonal class
    requires naming both mechanisms AND naming the specific enforcement dimensions they
    occupy. THE INERTIA PATTERN IS FAIL: a scored variation where two mechanisms are
    present (architecturally orthogonal) but the orthogonality class is not named is
    FAIL -- not PARTIAL. The criterion requirement is naming the class. Architecture-
    present-without-naming = structurally equivalent to a single-mechanism variation
    that has no orthogonal pair at all.

  C-33 (intra-role-lifecycle-sub-gate):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the intra-role lifecycle sub-gate as a distinct structural class -- an intermediate
    completion checkpoint within a single role's execution, not between roles. A role
    with two sequential steps is not an intra-role lifecycle sub-gate unless the
    intermediate step emits a named state that gates the role's terminal output. The
    class requires naming the sub-gate as "intra-role lifecycle sub-gate" or equivalent
    that identifies the within-role sequential enforcement mechanism. THE INERTIA PATTERN
    IS FAIL: a scored variation where REGISTER COMPLETENESS CONFIRMED functions as an
    intermediate checkpoint but is not identified as an intra-role lifecycle sub-gate
    class is FAIL -- not PARTIAL. The criterion requirement is the identification act.
    Architecture-present-without-naming = structurally equivalent to a variation with
    no sub-gate.

After writing all 42 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME
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
  | C-41      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-42      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 42 rows show YES in all three columns, produce the intra-role
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
              + (aspirational_pass / 35 * 10)
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
does not satisfy this gate. Holding either token alone does not satisfy this gate.
Holding any two without the third does not satisfy this gate.

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

## V-02 -- Axis PRBL: Preamble classification families enumeration (C-42 preamble probe)

**Variation axis**: Preamble-level classification enumeration -- a "Classification families
summary" preamble section is added before per-criterion notes, listing both families by
criterion ID. Position-sensitive criteria: C-10, C-15, C-27. Structural-class-recognition
criteria: C-13, C-14, C-33. The preamble makes both families enumerable by reading the
preamble section alone. Per-criterion structural-class-recognition notes are C-40 complete
(inertia-FAIL + structural-equivalence basis) but NOT labeled with per-criterion classification
tags -- testing whether a preamble-level enumeration satisfies C-42 without per-criterion labels.
C-41 positional labels carried (per-criterion). Full R17 V-05 base: anchor-complete positional
notes, inertia-FAIL framing, three-way SYNTHESIS gate. 42-row register, formula /35, E=4.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-42 PARTIAL or FAIL: preamble enumerates structural-class-recognition criteria by ID, but per-criterion notes lack the classification label at each entry. C-42 requires the label "at the note entry itself -- not in a preamble or section header." Preamble satisfies the enumeration function but not the per-entry requirement. C-41 PASS: positional notes carry per-criterion labels (not just preamble). | C-40 PASS: inertia-FAIL declaration present in each note. C-39 PASS: anchor-complete positional notes carried. C-02 PASS (/35). The preamble/per-criterion distinction for C-42 is the key signal. | V-04 combines preamble with per-criterion labels to confirm per-criterion labels alone satisfy C-42; preamble adds no ceiling but also creates no degradation. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role      | Requires                                                                                                                                    | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                          | Cannot Check                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                                      | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete positional notes (C-41 labeled) + structural-class-recognition notes with inertia-FAIL framing + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01--C-42) with intra-role lifecycle sub-gate | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                                     | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                                       | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                                            | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                            | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                                     | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                 | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)                   | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                 | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate.
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
C-42), produce a Judge standard entry with four required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase -- drawn from provided
               inputs, not invented]"
  UNACCEPTABLE: "[from provided inputs, or representative failure -- not invented]"
  Separating property: [mechanism A] vs [mechanism B]

For each ACCEPTABLE entry, attach "from [Output-N]:" prefix. The "ACCEPTABLE source
annotated" column records whether this annotation is present. YES = present; NO =
absent or general; blank = structural violation; NO = blocks; only YES passes.

CLASSIFICATION FAMILIES SUMMARY (for coverage audit -- scannable by section):

  This section enumerates both application-note families so a reviewer can identify
  which criteria require which type of application note without reading individual
  note content.

  Position-sensitive criteria (C-39/C-41 applies -- anchor-complete labeled notes required):
    C-10 (phase-completion-gates), C-15 (role-enforcement-output-input-coupling),
    C-27 (SYNTHESIS-gate-strict-conjunction)

  Structural-class-recognition criteria (C-38/C-40 applies -- inertia-FAIL framing required):
    C-13 (adversarial-auditor), C-14 (orthogonal-enforcement-axes),
    C-33 (intra-role-lifecycle-sub-gate)

APPLICATION NOTE for position-sensitive criteria:

  For each position-sensitive criterion, append after the Separating property line:

  Positional verification test (C-39 applies here): verify that [specific element]
  appears [BEFORE / AFTER] [specific anchor element] -- not that [element] exists.
  The anchor is [named structural anchor]. The direction is [BEFORE / AFTER].

  Per-criterion anchor-complete positional notes:

  C-10 (phase-completion-gates):
    Positional verification test (C-39 applies here): verify that the named gate marker
    (e.g., JUDGE STANDARD COMPLETE) appears BEFORE the opening line of the gated role's
    first output (the ANALYST scoring table header row). Anchor: first output line of the
    blocked role. Direction: BEFORE.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test (C-39 applies here): verify that JUDGE STANDARD COMPLETE
    appears BEFORE the ANALYST C-01 row. Anchor: ANALYST C-01 row. Direction: BEFORE.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test (C-39 applies here): verify that the BOTH...AND conjunction
    gate instruction appears BEFORE the LEADERBOARD section heading. Anchor: LEADERBOARD
    heading. Direction: BEFORE.

APPLICATION NOTE for structural-class-recognition criteria (enumerated in Classification
families summary above -- C-13, C-14, C-33):

  These criteria require the scorer to identify and name a structural class as a distinct
  category. The identification act is the criterion requirement, not architectural confirmation.

  C-13 (adversarial-auditor): identify and name the adversarial auditor role as a
  structurally distinct entity whose function is to challenge evidence produced by another
  role. THE INERTIA PATTERN IS FAIL: architecture-present-without-naming is structurally
  equivalent to architecture-absent, because the criterion requirement is the identification
  act. A scored variation where adversarial auditing occurs but the adversarial class is not
  named is FAIL -- not PARTIAL. Do not assign PARTIAL to the inertia pattern.

  C-14 (orthogonal-enforcement-axes): identify and name the orthogonality relationship
  between enforcement mechanisms as a distinct structural class. Name both mechanisms AND
  their specific enforcement dimensions (role-based, sequential, structural, content-
  validation). THE INERTIA PATTERN IS FAIL: two mechanisms architecturally present but
  orthogonality not named = FAIL. Architecture-present-without-naming = structurally
  equivalent to a single-mechanism variation.

  C-33 (intra-role-lifecycle-sub-gate): identify and name the intra-role lifecycle sub-gate
  as a distinct structural class. An intra-role sub-gate is a named intermediate completion
  state within a single role's execution that gates the role's terminal output. THE INERTIA
  PATTERN IS FAIL: REGISTER COMPLETENESS CONFIRMED functioning as intermediate checkpoint
  but not identified as intra-role lifecycle sub-gate class = FAIL. The identification act
  IS the criterion requirement.

After writing all 42 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER.

CONSOLIDATED PRODUCTION-TIME REGISTER

No-skip column rule: every cell must contain YES or NO. Blank = structural violation.
YES-only gate: NO blocks. Only YES passes.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-42 (42 rows) -- all columns must show YES |

[42 rows: C-01 through C-42, each with Pair present / Separating property declared /
ACCEPTABLE source annotated columns requiring YES]

After confirming all 42 rows show YES in all three columns:

REGISTER COMPLETENESS CONFIRMED

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: Present_mechanism and Absent_mechanism are required schema columns.
A scoring table missing either column is a structural gap detectable by table inspection
without reading cell content. A scorer confirms both columns by reading the header row
alone. A sentence mandate without named schema columns does not satisfy this requirement.

Column rules:
  - Present_mechanism / Absent_mechanism: required on PARTIAL rows; -- on PASS/FAIL rows.
  - Blank cell on PARTIAL row = structural violation.
  No row may be skipped.

  Composite computation:
    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 35 * 10)
              = [result]

    Golden: YES -- all essentials PASS; composite >= 80
         |  NO  -- [reason]

Score all N outputs.
ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence (see manifest).
Cannot check: content quality (Confirmer domain), evidence standards (Judge domain).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A -- Evidence quality: compare each evidence cell against Judge ACCEPTABLE/
UNACCEPTABLE pair. Reject if resembles UNACCEPTABLE or is generic across outputs.

AUDIT B -- Diagnostic column presence (PARTIAL rows only): Present_mechanism non-empty
AND Absent_mechanism non-empty.

Per-output audit table:

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

Status = ACCEPTED only if all applicable audits pass.
FLAG rejected rows. Flagged items reopened; accepted items closed.

When all rows ACCEPTED:
VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality of Present_mechanism and Absent_mechanism cells (see manifest).
Cannot check: format presence (Verifier), evidence standards (Judge), verdicts (Analyst).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

Per PARTIAL verdict, produce content challenge row:

  | Criterion | Present_mechanism excerpt | Specific? | Absent_mechanism excerpt | Specific? | Status |

Specificity: YES = names specific structural element/role/gate/design gap; NO = generic.
CHALLENGE any NO entry. Challenged items reopened; confirmed items closed.

When all PARTIAL diagnostics CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens must appear simultaneously
as a strict three-way conjunction -- holding any two without the third does not satisfy
this gate. Holding either token alone does not satisfy this gate.

LEADERBOARD

  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS

  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference]

FAILURE PATTERNS

  Pattern: [criterion ID] -- [name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

REGRESSION SIGNALS

  Prior PASS -> current PARTIAL/FAIL with output ID, criterion ID, change note.
  If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-03 -- Axis TAGINL: Inline prose classification labels (phrasing register)

**Variation axis**: Phrasing register -- all classification content is correct (C-41 and
C-42 label content present) but expressed as inline prose sentences rather than formal
"(C-NN applies here):" tag format. Positional notes say "This is a position-sensitive
criterion to which C-39/C-41 applies." Structural-class-recognition notes say "This is
a structural-class-recognition criterion to which C-38/C-40/C-42 applies." Tests whether
C-41/C-42 require the specific formal tag syntax or whether prose-embedded classification
language satisfies the label requirement. Anchor content (C-39) and inertia-FAIL framing
(C-40) are present and correct. 42-row register, formula /35.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-41 PARTIAL: positional label content present (inline prose: "position-sensitive criterion, C-39/C-41 applies") but not in the formal tag format ("Positional verification test (C-39 applies here):"). C-41 requires a label that makes the set enumerable by label-scan; prose embedded in note body requires content-reading to identify classification. C-42 PARTIAL: same issue for structural-class-recognition labels. | C-39 PASS: anchor-complete content present regardless of label format. C-40 PASS: inertia-FAIL + structural-equivalence basis present regardless of label format. C-02 PASS (/35). | The prose/tag distinction is the isolating test: C-41 and C-42 distinguish whether classification-label enumeration requires a scan-detectable tag or tolerates any label form. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role      | Requires                                                                                                                                    | Produces                                                  | Domain (ONLY)                                                                                                                                                                                 | Cannot Check                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                                      | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + positional and class-recognition application notes + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01--C-42) | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                                     | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                               | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                                            | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                    | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                                     | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                         | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)                   | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                         | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. Holding any two without
    the third does not satisfy this gate. Holding either token alone does not satisfy
    this gate.
  - No role may be skipped or merged with another.
  - A blank cell in any register column blocks REGISTER COMPLETENESS CONFIRMED and
    JUDGE STANDARD COMPLETE. A NO cell also blocks. Only YES passes.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs. For each criterion C-01 through C-42, produce:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [from actual inputs, not invented]"
  UNACCEPTABLE: "[from actual inputs or representative failure]"
  Separating property: [mechanism A] vs [mechanism B]

Attach "from [Output-N]:" prefix to every ACCEPTABLE entry (ACCEPTABLE source annotated
column: YES = present; NO = absent; blank = violation; NO = blocks; only YES passes).

For criteria whose pass condition requires positional verification, append a note after
the Separating property line. Note that these criteria belong to the position-sensitive
family (C-39/C-41 applies to this criterion) and specify the anchor and direction:

  For C-10: Note -- this criterion belongs to the position-sensitive application-note
  family; C-39 and C-41 apply here. Positional check: the named gate marker must appear
  before the opening line of the gated role's first output. Verify the gate token appears
  BEFORE the ANALYST scoring table header. Anchor: first ANALYST output line. Direction:
  BEFORE. A gate token existing but appearing after ANALYST output fails C-10.

  For C-15: Note -- position-sensitive criterion; C-39 and C-41 apply here. Positional
  check: verify JUDGE STANDARD COMPLETE appears before the ANALYST C-01 criterion row.
  Anchor: ANALYST C-01 row. Direction: BEFORE. Token appearing after any ANALYST output
  fails the coupling requirement.

  For C-27: Note -- position-sensitive criterion; C-39 and C-41 apply here. Positional
  check: verify the BOTH...AND conjunction gate instruction appears before the LEADERBOARD
  section heading. Anchor: LEADERBOARD heading. Direction: BEFORE.

For criteria whose pass condition requires structural-class identification, append a note
directing class recognition. Note that these criteria belong to the structural-class-
recognition family (C-38/C-40/C-42 applies to this criterion):

  For C-13: Note -- this criterion belongs to the structural-class-recognition family;
  C-38, C-40, and C-42 apply here. Recognize and name the adversarial auditor role as a
  structurally distinct entity challenging evidence produced by another role. The inertia
  pattern -- architecture present (two roles exist, audit occurs) but class not named --
  is equivalent to no adversarial role at all. Architecture-present-without-naming is
  structurally equivalent to architecture-absent because the identification act IS the
  criterion requirement. FAIL, not PARTIAL, for the inertia pattern.

  For C-14: Note -- structural-class-recognition criterion; C-38, C-40, and C-42 apply
  here. Recognize and name the orthogonality relationship between enforcement mechanisms
  as a structural class. Name both mechanisms and their specific enforcement dimensions.
  The inertia pattern -- two orthogonal mechanisms present but orthogonality not named --
  is FAIL: architecture-present-without-naming = structurally equivalent to a single-
  mechanism design. Do not assign PARTIAL to the inertia pattern.

  For C-33: Note -- structural-class-recognition criterion; C-38, C-40, and C-42 apply
  here. Recognize and name the intra-role lifecycle sub-gate as a structural class: a
  named intermediate completion state within a single role's execution. The inertia
  pattern -- REGISTER COMPLETENESS CONFIRMED functioning as sub-gate but not identified
  as intra-role lifecycle sub-gate class -- is FAIL. The identification act is the
  criterion requirement.

After writing all 42 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER.

CONSOLIDATED PRODUCTION-TIME REGISTER

No-skip: every cell YES or NO. Blank = violation. YES-only gate: NO blocks.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  | C-01 through C-42 (42 rows) |

After all 42 rows show YES in all three columns:

REGISTER COMPLETENESS CONFIRMED

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: Present_mechanism and Absent_mechanism are required schema columns.
A scoring table missing either column is a structural gap detectable by table inspection
without reading cell content. Confirmation by header-row inspection alone.

Column rules: Present_mechanism / Absent_mechanism required on PARTIAL rows (-- on PASS/
FAIL). No blank cells on PARTIAL rows.

  Composite computation:
    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 35 * 10)
    Golden: YES (all essentials PASS; composite >= 80) | NO (reason)

ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence (see manifest). Cannot check content quality or evidence standards.
Do not begin until ANALYST COMPLETE appears above.

AUDIT A: Evidence vs ACCEPTABLE/UNACCEPTABLE pairs. Reject if UNACCEPTABLE pattern or generic.
AUDIT B: PARTIAL rows -- Present_mechanism and Absent_mechanism non-empty.

Per-output audit table:
  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

FLAG rejected rows. Only flagged items reopened.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality of Present_mechanism and Absent_mechanism (see manifest).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

Per PARTIAL verdict:
  | Criterion | Present_mechanism excerpt | Specific? | Absent_mechanism excerpt | Specific? | Status |

Specific = names structural element / role / gate / design gap. CHALLENGE any NO.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. Strict three-way conjunction. Holding
any two without the third does not satisfy this gate.

LEADERBOARD
  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
  Signal: [output ID] -- [criterion ID] -- [mechanism]

FAILURE PATTERNS
  Pattern: [criterion ID] -- [name]
  Diagnosis: [type] -- [sentence]

REGRESSION SIGNALS
  [regression notes or "No prior round data; regression analysis not possible."]
```

---

## V-04 -- Axis CLBL + PRBL: Classification labels with preamble enumeration (combination)

**Variation axis**: Combination -- per-criterion structural-class-recognition labels (C-42)
combined with the classification families preamble (PRBL). Both per-criterion labels AND
preamble enumeration present. C-41 positional labels carried. Full R17 V-05 base. Tests that
C-42 is satisfied when per-criterion labels are present (preamble adds redundancy, creates no
degradation). 42-row register, formula /35.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-42 PASS: per-criterion structural-class labels present on C-13, C-14, C-33 note entries. C-41 PASS: positional labels carried. Preamble enumeration adds a redundant path to classification enumeration without degrading per-criterion labels. All R17 V-05 criteria carry forward. | C-02 PASS (/35). Preamble adds no new ceiling (C-42 is the ceiling); V-05 distinguishes by adding formula-anchor in manifest Domain column. V-04 vs V-01: identical on C-42 satisfaction path; V-04 adds PRBL which is unscored but confirms additive compatibility. | V-05 adds formula-anchor N_aspirational=35 in Domain column to test whether manifest-level formula declaration adds any ceiling criterion. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite
score computed from the rubric formula, and a golden-threshold determination. The
final scorecard includes a ranked leaderboard, excellence signals, failure patterns,
and regression signals.

---

ROLE DEPENDENCY MANIFEST

| Role      | Requires                                                                                                                                    | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                                                            | Cannot Check                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                                      | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete positional notes (C-41 labeled) + structural-class-recognition notes (C-42 labeled) + classification families preamble + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01--C-42) | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                                     | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite; Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                                                                          | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                                            | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                                                               | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                                     | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                                    | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)                   | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                                    | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. Two orthogonal enforcement mechanisms within one role:
    gate-rules declaration (structural family) and REGISTER COMPLETENESS CONFIRMED token
    (sequential enforcement family).
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens required
    simultaneously as a strict three-way conjunction -- holding any two without the third
    does not satisfy this gate. Holding either token alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
  - Blank cell in any required register column blocks REGISTER COMPLETENESS CONFIRMED
    and JUDGE STANDARD COMPLETE. NO cell also blocks. Only YES passes.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).

Read all N outputs. For each criterion C-01 through C-42, produce:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [from actual inputs, not invented]"
  UNACCEPTABLE: "[from actual inputs or representative failure]"
  Separating property: [mechanism A] vs [mechanism B]

Attach "from [Output-N]:" prefix to every ACCEPTABLE entry. YES-only gate applies to
ACCEPTABLE source annotated column in the CONSOLIDATED PRODUCTION-TIME REGISTER.

CLASSIFICATION FAMILIES PREAMBLE (for coverage audit and dual-path enumeration):

  Both application-note families are enumerated here AND labeled at each per-criterion
  note entry. The preamble enables section-level enumeration; the per-criterion label
  enables entry-level enumeration. Both paths are independently valid.

  Position-sensitive criteria (C-39/C-41 applies -- labeled at each note entry):
    C-10 (phase-completion-gates), C-15 (role-enforcement-output-input-coupling),
    C-27 (SYNTHESIS-gate-strict-conjunction)

  Structural-class-recognition criteria (C-38/C-40/C-42 applies -- labeled at each note entry):
    C-13 (adversarial-auditor), C-14 (orthogonal-enforcement-axes),
    C-33 (intra-role-lifecycle-sub-gate)

APPLICATION NOTE for position-sensitive criteria:

  For each position-sensitive criterion, the note entry carries the classification label:

  Positional verification test (C-39 applies here): verify that [specific element]
  appears BEFORE [specific anchor element]. Anchor: [named element]. Direction: BEFORE.

  C-10 (phase-completion-gates):
    Positional verification test (C-39 applies here): verify that the named gate marker
    (e.g., JUDGE STANDARD COMPLETE) appears BEFORE the opening line of the gated role's
    first output (ANALYST scoring table header row). Anchor: first ANALYST output line.
    Direction: BEFORE. Gate token appearing after any ANALYST output fails C-10.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test (C-39 applies here): verify that JUDGE STANDARD COMPLETE
    appears BEFORE the ANALYST C-01 criterion row. Anchor: ANALYST C-01 row. Direction:
    BEFORE. Token appearing after any ANALYST criterion row fails C-15's coupling.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test (C-39 applies here): verify that the BOTH...AND conjunction
    gate instruction appears BEFORE the LEADERBOARD section heading. Anchor: LEADERBOARD
    heading. Direction: BEFORE.

APPLICATION NOTE for structural-class-recognition criteria:

  For each structural-class-recognition criterion, the note entry carries the classification
  label. The label enables label-scan enumeration; the inertia declaration closes the PARTIAL
  bypass path.

  C-13 (adversarial-auditor):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name the
    adversarial auditor role as a structurally distinct entity whose function is to challenge
    evidence produced by another role. Recognition of the adversarial class -- not just audit
    presence -- is the criterion requirement. THE INERTIA PATTERN IS FAIL: architecture-
    present-without-naming is structurally equivalent to architecture-absent, because the
    identification act IS the criterion. A scored variation where adversarial auditing occurs
    but the adversarial class is not named is FAIL -- not PARTIAL.

  C-14 (orthogonal-enforcement-axes):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name the
    orthogonality relationship between enforcement mechanisms as a distinct structural class.
    Name both mechanisms AND their specific enforcement dimensions (role-based, sequential,
    structural, content-validation). THE INERTIA PATTERN IS FAIL: two mechanisms present but
    orthogonality not named = FAIL. Architecture-present-without-naming = structurally
    equivalent to a single-mechanism design. The identification act is the requirement.

  C-33 (intra-role-lifecycle-sub-gate):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name the
    intra-role lifecycle sub-gate as a distinct structural class -- a named intermediate
    completion state within a single role's execution, separate from terminal completion.
    THE INERTIA PATTERN IS FAIL: REGISTER COMPLETENESS CONFIRMED functioning as sub-gate
    but not identified as intra-role lifecycle sub-gate class = FAIL. Architecture-present-
    without-naming = structurally equivalent to a variation with no intra-role sub-gate.

After writing all 42 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME REGISTER.

CONSOLIDATED PRODUCTION-TIME REGISTER

No-skip column rule: every cell must be YES or NO. Blank = structural violation.
YES-only gate: NO = blocking. Only YES passes.

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
  | C-41      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-42      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 42 rows show YES in all three columns:

REGISTER COMPLETENESS CONFIRMED

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until JUDGE STANDARD COMPLETE appears above.

Scoring table schema (mandatory):

  | ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |

Schema enforcement: Present_mechanism and Absent_mechanism are required schema columns.
A scoring table missing either column is a structural gap detectable by table inspection
without reading cell content. The inspection-without-reading detection mechanism applies
at the column-name level. A sentence-format mandate without schema columns does not satisfy.

Column rules: Present_mechanism / Absent_mechanism required on PARTIAL rows; -- on PASS/
FAIL. No blank cells on PARTIAL rows.

  Composite computation:
    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 35 * 10)
    Golden: YES (all essentials PASS; composite >= 80) | NO ([reason])

ANALYST COMPLETE -- [N] outputs scored

---

ROLE 3: VERIFIER

Domain: Format presence (see manifest).
Cannot check: content quality (Confirmer), evidence standards (Judge).
Do not begin until ANALYST COMPLETE appears above.

AUDIT A: Evidence vs ACCEPTABLE/UNACCEPTABLE pairs. Reject if UNACCEPTABLE or generic.
AUDIT B: PARTIAL rows -- Present_mechanism and Absent_mechanism non-empty.

  | ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |

FLAG rejected rows. Flagged items reopened; accepted items closed.

VERIFIER AUDIT COMPLETE

---

ROLE 4: CONFIRMER

Domain: Content quality of Present_mechanism and Absent_mechanism (see manifest).
Do not begin until VERIFIER AUDIT COMPLETE appears above.

  | Criterion | Present_mechanism excerpt | Specific? | Absent_mechanism excerpt | Specific? | Status |

Specific = names structural element / role / gate / gap. CHALLENGE any NO entry.
Challenged items reopened; confirmed items closed.

CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens required simultaneously
as a strict three-way conjunction. Holding any two without the third does not satisfy
this gate. Holding either token alone does not satisfy this gate.

LEADERBOARD
  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
  Signal: [output ID] -- [criterion ID] -- [structural mechanism]

FAILURE PATTERNS
  Pattern: [criterion ID] -- [name] | Diagnosis: [type] -- [sentence]

REGRESSION SIGNALS
  [regression notes or "No prior round data; regression analysis not possible."]
```

---

## V-05 -- Full stack R18: All axes + formula anchor in manifest (ceiling variation)

**Variation axis**: Full stack -- all R17 mechanisms + CLBL (C-42 per-criterion labels) +
PRBL (classification families preamble) + formula-anchor in manifest Domain column
(N_aspirational=35 explicitly declared as a domain property of the JUDGE role) + dual-family
dual-site enumeration (preamble lists both families; per-criterion notes carry both label types
with formal tag syntax). Ceiling variation. Predicts all C-08 through C-42 PASS, C-02 PASS
(/35), composite 100.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-42 PASS: per-criterion labels on C-13, C-14, C-33 in formal "Structural-class-recognition criterion (C-38/C-40 applies here):" tag. C-41 PASS: positional labels carried. C-02 PASS: /35 denominator correct. All R17 criteria carried. | Formula-anchor in manifest Domain column (N_aspirational=35) makes formula denominator self-documenting in the manifest artifact -- no additional rubric criterion names this, but it creates structural redundancy for C-02 conformance. | V-05 vs V-04: the formula-anchor in Domain column and dual-site enumeration are the distinguishing elements. Neither creates a new rubric criterion, but both close remaining redundancy gaps. |

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
each role's domain boundary and the formula parameter anchored in the JUDGE domain.
It is a standalone structural artifact -- auditable without executing the protocol.
A row with a blank cell is a structural gap. No role may begin unless its Requires
entry is present in the output above.

| Role      | Requires                                                                                                                                    | Produces                                                  | Domain (ONLY)                                                                                                                                                                                                                                                                                                                                                                        | Cannot Check                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| JUDGE     | (none)                                                                                                                                      | REGISTER COMPLETENESS CONFIRMED, JUDGE STANDARD COMPLETE  | Evidence quality standards: ACCEPTABLE/UNACCEPTABLE pairs + separating property declarations + anchor-complete positional notes (C-41 labeled) + structural-class-recognition notes (C-42 labeled) + dual-family classification preamble + CONSOLIDATED PRODUCTION-TIME REGISTER (C-01--C-42, 42 rows) with intra-role lifecycle sub-gate. Formula parameter: N_aspirational=35 (v18 rubric). | Scoring verdicts, format compliance, diagnostic content quality                                           |
| ANALYST   | JUDGE STANDARD COMPLETE                                                                                                                     | ANALYST COMPLETE                                          | Per-criterion scoring; evidence cells; composite using N_aspirational=35 (as declared in JUDGE domain); Present_mechanism and Absent_mechanism columns (schema-bound)                                                                                                                                                                                                                | Evidence quality standards (Judge domain), format auditing (Verifier domain)                              |
| VERIFIER  | ANALYST COMPLETE                                                                                                                            | VERIFIER AUDIT COMPLETE                                   | Format presence: evidence cell non-genericity; Present_mechanism and Absent_mechanism column non-emptiness on PARTIAL rows                                                                                                                                                                                                                                                           | Diagnostic content quality (Confirmer domain), evidence standards (Judge domain)                          |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                                                                                                     | CONFIRMATION COMPLETE                                     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?                                                                                                                                                                                                                                                                                | Format presence (Verifier domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain)  |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED (strict three-way conjunction)                   | (terminal output)                                         | Leaderboard, excellence signals, failure patterns, regression signals                                                                                                                                                                                                                                                                                                                | Re-scoring, re-auditing                                                                                   |

Gate rules (hard):
  - JUDGE STANDARD COMPLETE requires REGISTER COMPLETENESS CONFIRMED as a prior
    intra-role lifecycle sub-gate. JUDGE's execution has two phases: (1) writing
    ACCEPTABLE/UNACCEPTABLE pairs and populating the CONSOLIDATED PRODUCTION-TIME
    REGISTER (42 rows, C-01 through C-42) -- concludes with REGISTER COMPLETENESS
    CONFIRMED; (2) REGISTER COMPLETENESS CONFIRMED -> JUDGE STANDARD COMPLETE. Gate-rules
    declaration (structural family) and REGISTER COMPLETENESS CONFIRMED token (sequential
    enforcement family) are two orthogonal enforcement mechanisms within one role.
  - Role 2 cannot begin without JUDGE STANDARD COMPLETE present above.
  - Role 3 cannot begin without ANALYST COMPLETE present above.
  - Role 4 cannot begin without VERIFIER AUDIT COMPLETE present above.
  - SYNTHESIS cannot begin without BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION
    COMPLETE AND REGISTER COMPLETENESS CONFIRMED present above. All three tokens must
    appear simultaneously as a strict three-way conjunction -- holding any two without
    the third does not satisfy this gate. Holding either token alone does not satisfy
    this gate. Holding any two without the third does not satisfy this gate.
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

Domain: Evidence quality standards (see manifest). Formula parameter: N_aspirational=35.

Read all N outputs provided as inputs. For each criterion in the rubric (C-01 through
C-42), produce a Judge standard entry with four required components:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase from an actual output
               satisfying this criterion -- drawn from provided inputs, not invented]"
  UNACCEPTABLE: "[text from an actual output, or a representative generic statement
                 that would fail -- drawn from provided inputs, not invented]"
  Separating property: [mechanism A] vs [mechanism B]

The "Separating property:" line names, in a single labeled declaration, the specific
structural mechanism present in the ACCEPTABLE form and absent in the UNACCEPTABLE
form. Named label + two mechanism poles separated by "vs" -- not embedded in prose.

For each ACCEPTABLE entry, attach a "from [Output-N]:" prefix annotation. The
"ACCEPTABLE source annotated" column records whether this annotation is present.
  - YES: annotation present naming the specific output.
  - NO: annotation absent or general statement not tied to a specific output.
  - Blank: structural violation. NO: blocks. Only YES passes.

DUAL-FAMILY CLASSIFICATION PREAMBLE

  Both application-note families are enumerated here (preamble-level enumeration path)
  AND labeled at each per-criterion note entry (entry-level enumeration path). Both paths
  are independently valid for coverage verification.

  Position-sensitive criteria (C-39/C-41 applies -- labeled at each note entry below):
    C-10 (phase-completion-gates), C-15 (role-enforcement-output-input-coupling),
    C-27 (SYNTHESIS-gate-strict-conjunction)
    Verification: position-sensitive membership is enumerable by scanning for the
    "Positional verification test (C-39 applies here):" label tag at each note entry,
    without reading anchor or direction content.

  Structural-class-recognition criteria (C-38/C-40/C-42 applies -- labeled at each note entry below):
    C-13 (adversarial-auditor), C-14 (orthogonal-enforcement-axes),
    C-33 (intra-role-lifecycle-sub-gate)
    Verification: structural-class-recognition membership is enumerable by scanning for
    the "Structural-class-recognition criterion (C-38/C-40 applies here):" label tag at
    each note entry, without reading inertia declaration content.

APPLICATION NOTE for position-sensitive criteria (criteria where the pass condition
requires a structural element to appear at a specific position relative to another
structural element, not merely to exist):

  For each position-sensitive criterion, the application note entry carries the
  classification label as its first line, then names the anchor and direction:

  Positional verification test (C-39 applies here): verify that [specific element]
  appears [BEFORE / AFTER] [specific anchor element] -- not that [element] exists.
  Anchor: [named structural element]. Direction: [BEFORE / AFTER]. A scored variation
  where [element] exists but appears on the wrong side of [anchor] fails this criterion.

  The label "Positional verification test (C-39 applies here):" appears as the first
  line of each positional application note entry. A reviewer can enumerate all
  position-sensitive criteria by scanning for this label tag without reading each
  note's anchor and direction content.

  C-10 (phase-completion-gates):
    Positional verification test (C-39 applies here): verify that the named gate marker
    (e.g., JUDGE STANDARD COMPLETE) appears BEFORE the opening line of the gated role's
    first output (e.g., the ANALYST scoring table header row). Anchor: first output line
    of the role the gate claims to block. Direction: BEFORE. A gate token appearing
    anywhere after any ANALYST output fails C-10's positional requirement even if the
    token exists in the output.

  C-15 (role-enforcement-output-input-coupling):
    Positional verification test (C-39 applies here): verify that the first role's named
    completion token (JUDGE STANDARD COMPLETE) appears BEFORE the first criterion row of
    the ANALYST scoring table (before the C-01 row). Anchor: ANALYST C-01 criterion row.
    Direction: BEFORE. A completion token appearing after any ANALYST criterion row does
    not satisfy C-15's positional coupling requirement.

  C-27 (SYNTHESIS-gate-strict-conjunction):
    Positional verification test (C-39 applies here): verify that the BOTH...AND conjunction
    gate instruction appears BEFORE the LEADERBOARD section heading in the scored output.
    Anchor: LEADERBOARD heading. Direction: BEFORE. A conjunction gate instruction appearing
    after the LEADERBOARD section has begun does not block SYNTHESIS.

APPLICATION NOTE for structural-class-recognition criteria (criteria where the pass
condition requires the scorer to identify and name a structural class as a distinct
category -- architecture present is necessary but not sufficient; the identification act
is the criterion requirement):

  For each structural-class-recognition criterion, the application note entry carries the
  classification label as its first line, then directs identification and declares the
  inertia-FAIL verdict with structural-equivalence basis:

  Structural-class-recognition criterion (C-38/C-40 applies here): [identification
  instruction] + THE INERTIA PATTERN IS FAIL: [structural-equivalence declaration].

  The label "Structural-class-recognition criterion (C-38/C-40 applies here):" appears
  as the first line of each structural-class-recognition application note entry. A
  reviewer can enumerate all structural-class-recognition criteria by scanning for this
  label tag without reading each note's inertia declaration content.

  C-13 (adversarial-auditor):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the adversarial auditor role as a structurally distinct entity whose function is to
    challenge evidence produced by another role. The adversarial relationship -- not the
    audit obligation alone -- is the structural class. Recognition of the class as distinct
    is the criterion requirement. THE INERTIA PATTERN IS FAIL: a scored variation where
    adversarial auditing occurs architecturally (two roles exist, audit function executes)
    but the adversarial class is not identified as a distinct structural category is FAIL --
    not PARTIAL. This is structurally equivalent to a variation with no adversarial role,
    because the criterion requirement is the identification act: naming "adversarial auditor"
    as a named structural class. Architecture-present-without-naming = structurally
    equivalent to architecture-absent. Do not assign PARTIAL to the inertia pattern.

  C-14 (orthogonal-enforcement-axes):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the orthogonality relationship between enforcement mechanisms as a distinct structural
    class. Two mechanisms are orthogonal when they occupy independent enforcement
    dimensions: role-based (who is responsible), sequential (what must precede what),
    structural (what format is required), content-validation (what must be verified). Name
    both mechanisms AND name their specific enforcement dimensions. THE INERTIA PATTERN
    IS FAIL: a scored variation where two mechanisms are present and are architecturally
    orthogonal but where the orthogonality class is not named is FAIL -- not PARTIAL.
    Two mechanisms present without naming the orthogonal class = structurally equivalent
    to a single-mechanism design that has no orthogonal pair. The identification act is
    the criterion requirement. Do not assign PARTIAL to the inertia pattern.

  C-33 (intra-role-lifecycle-sub-gate):
    Structural-class-recognition criterion (C-38/C-40 applies here): identify and name
    the intra-role lifecycle sub-gate as a distinct structural class -- a named intermediate
    completion state produced within a single role's execution, distinct from the role's
    terminal completion token, and required as a precondition by the terminal gate. THE
    INERTIA PATTERN IS FAIL: a scored variation where REGISTER COMPLETENESS CONFIRMED
    functions as an intermediate checkpoint and is required before JUDGE STANDARD COMPLETE,
    but where it is not identified and named as an intra-role lifecycle sub-gate structural
    class, is FAIL -- not PARTIAL. Architecture-present-without-naming = structurally
    equivalent to a variation with no intra-role sub-gate, because the identification act
    IS the criterion requirement. Do not assign PARTIAL to the inertia pattern.

After writing all 42 criterion entries, produce the CONSOLIDATED PRODUCTION-TIME
REGISTER, then execute the intra-role lifecycle sub-gate sequence.

CONSOLIDATED PRODUCTION-TIME REGISTER

This is the single source of truth for all JUDGE production-time obligations. The
register covers C-01 through C-42 (42 rows, updated for v18 rubric).

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
  | C-41      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |
  | C-42      | [name]         | YES / NO     | YES / NO                     | YES / NO                    |

After confirming all 42 rows show YES in all three columns, produce the intra-role
lifecycle sub-gate token as a named execution output:

REGISTER COMPLETENESS CONFIRMED

This token is produced by the JUDGE role body during execution. It is required both
as the completion signal of JUDGE's Phase 1 (before JUDGE STANDARD COMPLETE) and as
an entry condition for the SYNTHESIS terminal gate. Then issue:

JUDGE STANDARD COMPLETE

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cell writing; composite computation using
N_aspirational=35 as declared in JUDGE domain (see manifest); Present_mechanism and
Absent_mechanism columns (schema-bound).
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
level: a scorer confirms both columns are present by reading the table header row alone,
without reading any cell content. A scoring instruction that mandates two-part diagnostic
content as a required sentence without declaring both columns in the table schema does
not satisfy this requirement.

Column rules:
  - Present_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design property that is present and prevented FAIL.
    For PASS and FAIL verdicts, enter --.
  - Absent_mechanism: for PARTIAL verdicts, name the specific structural element,
    mechanism, role, gate token, or design gap that is absent and prevented PASS.
    For PASS and FAIL verdicts, enter --.
  - A blank Present_mechanism or Absent_mechanism cell on a PARTIAL row is a structural
    violation equivalent to a blank evidence cell.

  No row may be skipped. No evidence cell, Present_mechanism cell, or Absent_mechanism
  cell on a PARTIAL row may be blank.

  Composite computation:
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 35 * 10)
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
              "named Produces/Requires manifest with DOMAIN and CANNOT CHECK entries"
  NO  -- uses a criterion label, generic quality phrase, or restates the verdict:
        e.g., "some structure is present", "mechanism is partially addressed",
              "does not fully satisfy the criterion", "coverage is incomplete"

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[verbatim excerpt]" -- [reason it fails the specificity test]
    Absent:  "[verbatim excerpt]" -- [reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items are closed.

When all PARTIAL diagnostics across all N outputs are CONFIRMED:
CONFIRMATION COMPLETE

---

SYNTHESIS

Do not begin until BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND
REGISTER COMPLETENESS CONFIRMED appear above. All three tokens must appear
simultaneously as a strict three-way conjunction -- holding any two without the third
does not satisfy this gate. Holding either token alone does not satisfy this gate.
Holding any two without the third does not satisfy this gate.

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

```json
{"round": 18, "rubric": "v18", "n_aspirational": 35, "new_criteria": ["C-41", "C-42"], "c41_status": "carried-from-R17", "c42_ceiling": true, "variations": ["V-01:CLBL", "V-02:PRBL", "V-03:TAGINL", "V-04:CLBL+PRBL", "V-05:full-stack-R18"], "predicted_ceiling": "V-05"}
```
