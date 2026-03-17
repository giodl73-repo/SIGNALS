---
name: signal-quest-score
description: "Score a set of skill outputs against a rubric. Given outputs from N skill runs and a rubric file, evaluate each output against every criterion. Produce: per-criterion pass/fail per output, composite score per output, ranked leaderboard, excellence signals (outputs scoring unusually high on specific criteria), and failure patterns (criteria that fail consistently across all outputs -- rubric gap or skill gap?).
"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
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