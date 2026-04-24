# Quest Score -- Round 17 Variations
**Skill**: quest-score
**Rubric**: v16 (C-01--C-05 essential, C-06--C-07 recommended, C-08--C-44 aspirational; denominator /37)
**Scoring context**: quest-rubric outputs (N_essential=4, N_recommended=3, N_aspirational=25)
**Date**: 2026-03-15
**Round**: 17

---

## Design logic

### Unachieved ceiling entering R17

| Criterion | R16 V-01 status | Gap analysis |
|-----------|-----------------|--------------|
| C-43 | new criterion (v16 rubric; not in v15) | C-43 requires: (1) SPECIFICITY AUDIT MANIFEST table as named terminal artifact keyed by (Output, Criterion); (2) VERIFIER per-cell schema references manifest rows by key rather than re-reading SA body; (3) SYNTHESIS explicitly prohibited from re-reading SPECIFICITY AUDITOR blocks. R16 V-01 SPECIFICITY AUDITOR produces per-output blocks without a consolidated manifest; VERIFIER cites "per SPECIFICITY AUDITOR" generically; dispersed-SA-body-reread path remains open. |
| C-44 | new criterion (v16 rubric; not in v15) | C-44 requires symmetric conjunction gate: VERIFIER entry condition must exclude BOTH [ANALYST COMPLETE] alone AND [SPECIFICITY AUDIT COMPLETE] alone. R16 V-01 includes [ANALYST COMPLETE] alone exclusion (C-42 PASS) but not [SPECIFICITY AUDIT COMPLETE] alone exclusion -- reverse bypass path remains open: a design where [SPECIFICITY AUDIT COMPLETE] is produced without [ANALYST COMPLETE] having appeared is not excluded from the VERIFIER header. |

### R17 variation axes

| Axis | Label | Mechanism |
|------|-------|-----------|
| manifest | SPECIFICITY AUDIT MANIFEST table | SA produces a named (Output, Criterion)-keyed manifest as terminal artifact; VERIFIER references Q1/Q2 results by manifest key; SYNTHESIS prohibited from re-reading SA blocks. Closes C-43 via all three requirements. |
| symm-gate | Symmetric conjunction gate | VERIFIER entry condition: "Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate. Both tokens are required." Closes C-44 via symmetric exclusion. |
| single-excl | Forward exclusion only | VERIFIER entry condition cites both tokens and excludes [ANALYST COMPLETE] alone but not [SPECIFICITY AUDIT COMPLETE] alone. Isolates C-44 PARTIAL path. |
| manifest-no-synth | Manifest + key, no SYNTHESIS prohibition | SA produces manifest; VERIFIER references by key; SYNTHESIS prohibition on SA-block re-read absent. Isolates C-43 PARTIAL path via missing prohibition. |
| manifest-no-key | Manifest + prohibition, generic VERIFIER reference | SA produces manifest; SYNTHESIS prohibition present; VERIFIER per-cell entries use generic "per SPECIFICITY AUDITOR" reference without keying to manifest rows. Isolates C-43 PARTIAL path via missing key reference. |

### Single-axis selections

- **V-02 (manifest + single-excl)**: Full C-43 implementation + forward-only exclusion. Tests C-43 pass floor and C-44 partial ceiling as independent axes.
- **V-03 (symm-gate only)**: Full C-44 implementation. No manifest. Tests C-44 pass with C-43 fail.

### Combination selections

- **V-01 (manifest + symm-gate)**: Ceiling. V-02 manifest architecture + V-03 symmetric gate. All 35 prior aspirationals inherited. Predicts: C-43 PASS + C-44 PASS.
- **V-04 (manifest-no-synth + symm-gate)**: Manifest + key + symmetric gate, SYNTHESIS prohibition absent. Predicts: C-43 PARTIAL, C-44 PASS.
- **V-05 (manifest-no-key + symm-gate)**: Manifest + SYNTHESIS prohibition + symmetric gate, VERIFIER key reference absent. Predicts: C-43 PARTIAL, C-44 PASS.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Named SPECIFICITY AUDITOR role (separate from VERIFIER) | YES | YES | YES | YES | YES |
| [SPECIFICITY AUDIT COMPLETE] gate token | YES | YES | YES | YES | YES |
| VERIFIER entry condition quotes gate verbatim | YES | YES | YES | YES | YES |
| [ANALYST COMPLETE] alone exclusion clause (C-42) | YES | YES | YES | YES | YES |
| [SPECIFICITY AUDIT COMPLETE] alone exclusion clause (C-44) | YES | NO | YES | YES | YES |
| SPECIFICITY AUDIT MANIFEST table as named terminal artifact (C-43 req 1) | YES | YES | NO | YES | YES |
| VERIFIER references manifest rows by key (C-43 req 2) | YES | YES | NO | YES | NO |
| SYNTHESIS prohibition on SA block re-read (C-43 req 3) | YES | YES | NO | NO | YES |
| Predicted C-43 | PASS | PASS | FAIL | PARTIAL | PARTIAL |
| Predicted C-44 | PASS | PARTIAL | PASS | PASS | PASS |

---

## V-01 -- Axes manifest + symm-gate: SPECIFICITY AUDIT MANIFEST + symmetric conjunction gate (ceiling)

**Variation axis**: Role sequence + lifecycle emphasis -- ceiling combination. SPECIFICITY AUDITOR produces a SPECIFICITY AUDIT MANIFEST keyed by (Output, Criterion) as its terminal artifact. VERIFIER references manifest rows by key. SYNTHESIS prohibited from re-reading SA blocks. VERIFIER entry condition symmetrically excludes both single-token bypass paths: [ANALYST COMPLETE] alone and [SPECIFICITY AUDIT COMPLETE] alone.

**Hypothesis**: C-43 PASS + C-44 PASS. All three C-43 requirements met: manifest as named terminal artifact, VERIFIER key-reference, SYNTHESIS SA-block re-read prohibition. C-44 symmetric exclusion closes both bypass paths. All 35 prior aspirational PASSes from R16 V-01 preserved. Ceiling for v16 rubric denominator /37.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

Load prior-round verdicts before scoring begins.

| Variation | Open aspirationals entering this round                                         |
|-----------|--------------------------------------------------------------------------------|
| V-01 R16  | (none -- ceiling achieved, all 35 prior aspirationals PASS; C-43 and C-44 new)|
| V-02 R16  | C-42 PARTIAL; C-43 new; C-44 new                                               |
| V-03 R16  | C-42 FAIL; C-43 new; C-44 new                                                  |
| V-04 R16  | C-44 new (C-43 PASS via SPECIFICITY AUDIT MANIFEST already present)            |
| V-05 R16  | C-43 new (C-44 PASS via symmetric conjunction gate already present)            |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

The following failure modes appear before scoring begins. Each failure mode is
paired with a dedicated closing mechanism that names the criterion ID enforcing
the close. This anchor enables bidirectional lookup: failure mode -> mechanism
-> criterion ID.

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required
  structure." [applies to any well-designed output of this type]
  Closing mechanism: C-40 requires the evidence field definition at the schema
  definition site to name cross-type genericity as a named disqualifying pattern;
  C-02 PASS alone does not close generic evidence.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: The same evidence sentence appears in two different output
  cells for the same criterion, with only the output identifier changed.
  Closing mechanism: C-40 requires the evidence field definition to name
  cross-output duplication within the run as a second disqualifying pattern;
  a cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score is given as "87.3" with no formula expression
  at the scoring site.
  Closing mechanism: C-39 requires the formula with all parameters (denominator,
  weights, counts) to be inscribed inline at the calculation site; C-03 PASS
  does not require inline formula inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table has a single "Audit A" or "Specificity"
  column in which both the type-level and intra-run questions are answered in
  one merged cell.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns in the per-cell schema; C-29 PASS does not require
  column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: LEADERBOARD section breaks ties in synthesis prose with no
  protocol inscribed at the definition site; ties may be broken differently
  across runs.
  Closing mechanism: C-41 requires the tie-break protocol with named secondary
  and tertiary dimensions to be inscribed at the leaderboard definition site;
  C-04 PASS does not require an inscribed protocol.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER entry condition lists only [ANALYST COMPLETE] as its
  gate; no dedicated SPECIFICITY AUDITOR role gate token exists; a reader cannot
  detect from the VERIFIER header alone whether a dedicated independent audit
  completed.
  Closing mechanism: C-42 requires a named SPECIFICITY AUDITOR role with its own
  gate token ([SPECIFICITY AUDIT COMPLETE]); the VERIFIER entry condition must
  quote this gate verbatim with an explicit exclusion clause ([ANALYST COMPLETE]
  alone does not satisfy this gate); the named-gate citation makes the dedicated
  audit independently verifiable from the VERIFIER header.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no
  consolidated manifest; VERIFIER per-cell entries reference "per SPECIFICITY
  AUDITOR" generically; SYNTHESIS re-reads SA blocks to retrieve Q1/Q2 results;
  any cell lookup requires traversing the full SA body.
  Closing mechanism: C-43 requires the SPECIFICITY AUDITOR to produce a named
  SPECIFICITY AUDIT MANIFEST table keyed by (Output, Criterion); the VERIFIER
  references Q1/Q2 results by manifest key rather than re-reading SA blocks;
  SYNTHESIS is explicitly prohibited from re-reading SPECIFICITY AUDITOR blocks;
  C-42 PASS leaves the dispersed-reread path open; C-43 closes it via the
  keyed-manifest terminal artifact.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone
  but not [SPECIFICITY AUDIT COMPLETE] alone; a design where [SPECIFICITY AUDIT
  COMPLETE] is produced without [ANALYST COMPLETE] having appeared is not
  excluded at the header; the reverse bypass path is unaddressed.
  Closing mechanism: C-44 requires the VERIFIER entry condition to additionally
  exclude [SPECIFICITY AUDIT COMPLETE] alone, making neither token independently
  sufficient; the symmetric clause closes the reverse bypass path that C-42 PASS
  leaves open; C-42 requires only the [ANALYST COMPLETE] alone exclusion;
  C-44 closes the complementary path.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                                                               | Cannot Check                                                      |
|---------------------|-----------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                | Scoring verdicts; format compliance; content quality              |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                             | Evidence standards (Judge); format auditing (Verifier)            |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                      | Re-scoring; re-auditing                                           |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                 | Format presence (Verifier); scoring (Analyst)                     |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows               | Q1/Q2 content (SA); evidence standards (Judge)                    |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                        | Format presence (Verifier); scoring (Analyst)                     |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-reading ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table |

A row with any blank cell is a structural gap. No role may begin unless its
Requires entry appears in the output above.

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT
    COMPLETE] appear above. [ANALYST COMPLETE] alone does not satisfy this gate.
    [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate.
    Both tokens are required.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
    gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32, produce a Judge standard entry:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase; the from [Output-N]:
               prefix annotation is required on every ACCEPTABLE entry]"
  UNACCEPTABLE: "[text that would fail -- drawn from provided inputs]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank or NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-02      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-03      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-04      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-05      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-06      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-07      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-08      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-09      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-10      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-11      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-12      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-13      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-14      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-15      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-16      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-17      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-18      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-19      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-20      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-21      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-22      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-23      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-24      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-25      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-26      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-27      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-28      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-29      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-30      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-31      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-32      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |

All 32 rows YES in all three columns before [JUDGE STANDARD COMPLETE] may be issued.

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cells; composite computation; *Why* field;
*Change* field; Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

Before writing any evidence cell, verify it against the Judge ACCEPTABLE/UNACCEPTABLE
pair. If your draft resembles the UNACCEPTABLE pattern, rewrite before entering.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E  | PASS/PARTIAL/FAIL | [specific evidence grounded in this output] | --                | --               |

  Evidence field violations (stated at this definition site):
    Disqualifying pattern 1: evidence could describe any well-designed output
      of this type (cross-type genericity) -- trigger a rewrite before filing
    Disqualifying pattern 2: the same description fits another output in this
      run without modification (cross-output duplication) -- trigger a rewrite
    Both disqualifying patterns are named here; either one is a cell violation.

  Per-row annotations (required for EVERY row; blank is a structural violation):
    *Why* (required): [structural mechanism or design property driving the verdict;
                       a criterion restatement or evidence paraphrase is a violation]
    *Change* (required): exactly one of three values:
      NO CHANGE
      CHANGE from [prior verdict]: [reason]
      NO PRIOR DATA

  PARTIAL row additions (required only on PARTIAL verdicts):
    Present_mechanism (required): [specific structural element preventing FAIL;
      a generic quality phrase is a structural violation]
    Absent_mechanism (required): [specific structural element preventing PASS;
      a criterion restatement is a structural violation]
    A blank Present_mechanism or Absent_mechanism on a PARTIAL row is a structural
    violation equivalent to a blank evidence cell.

  Composite computation (required -- formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [which essential failed, or composite < 80]

  Per-output narrative (required -- three labeled fields):
    Primary differentiator (required): [the structural feature explaining why
      this output scored differently from others in this run]
    Primary miss (required): [the criterion or structural mechanism most clearly
      absent from this output]
    Verdict spread (required): [where this output concentrated its points and why]

PROHIBITED CONTENT CATEGORIES (no cell, annotation, or narrative field may
contain any item in this list):

  A. Evaluative prose -- quality assessment without naming a structural element
     Route: rewrite as structural observation with named mechanism
  B. Criterion restatement -- text that rephrases the criterion label as evidence
     Route: rewrite using a structural feature observable in the output
  C. Cross-output generic text -- same sentence could appear in another output
     Route: flag for Specificity Auditor Q2-IntraRun review; rewrite with specific detail
  D. Narrative analysis in scoring cells -- mechanism interpretation or narrative prose
     Route: defer to per-output narrative section; keep scoring cells factual
  E. Novel field labels -- any label not in the permitted set above
     Route: prohibited; *Note*, *Comment*, *Observation*, or any unlisted label
     is a structural violation regardless of content

  No prohibited content category lacks a named destination.

Score all N outputs.
[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.

Sweep all *Change*: CHANGE annotations from every scoring block into a single
manifest table. SYNTHESIS must draw regression signals exclusively from this
manifest and is prohibited from re-reading ANALYST blocks or the baseline table
during synthesis. This prohibition is unconditional.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE annotations appear: "No changes from prior round detected."

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1-TypeLevel and Q2-IntraRun specificity review of every evidence cell;
ANCHOR REVIEW BLOCK application; SPECIFICITY AUDIT MANIFEST production;
revision flagging (see manifest).
Cannot check: scoring verdicts (Analyst domain); format column presence (Verifier
domain); content quality of diagnostic columns (Confirmer domain).
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK

The following two questions are the authority for all per-cell specificity entries.
Per-cell Q1-TypeLevel and Q2-IntraRun entries in the VERIFIER table must be
evaluated against these verbatim question forms. Per-cell entries that answer a
paraphrase rather than these anchored questions are a structural drift.

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type -- i.e., would this evidence be equally valid for a correct implementation
    that is not this specific output?"

  Q2 (Intra-run): "Does this evidence fit another output in this run -- i.e.,
    could the same description appear in a different output's cell for this same
    criterion without modification?"

For every evidence cell across all N outputs, apply both questions and record results:

  Output: [output identifier] -- SPECIFICITY AUDITOR pass

  | ID   | Evidence excerpt (first 15 words)  | Q1-TypeLevel | Q2-IntraRun | Action          |
  |------|------------------------------------|--------------|-------------|-----------------|
  | C-01 | [excerpt]                          | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

  Q1-TypeLevel:
    PASS: evidence would NOT describe any well-designed output of this type
    FAIL: evidence WOULD describe any well-designed output -- require Analyst revision

  Q2-IntraRun:
    PASS: evidence would NOT fit another output in this run unchanged
    FAIL: evidence WOULD fit another output unchanged -- require Analyst revision

For every cell where Q1-TypeLevel FAIL or Q2-IntraRun FAIL:
  REVISION FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PASS/FAIL -- reason if FAIL]
    Q2-IntraRun:  [PASS/FAIL -- reason if FAIL]
    Required action: Analyst must revise evidence before this cell may be accepted.

Flagged cells require Analyst revision and SPECIFICITY AUDITOR re-review of the
revised cell only. ACCEPTED cells are closed and not reopened by a revision.

SPECIFICITY AUDIT MANIFEST

After all evidence cells across all N outputs are reviewed, produce this manifest
as the terminal artifact of the SPECIFICITY AUDITOR role. This manifest is the
authoritative Q1/Q2 source for the VERIFIER. The VERIFIER must reference manifest
rows by (Output, Criterion) key; it must not re-read SPECIFICITY AUDITOR per-output
blocks. SYNTHESIS is prohibited from re-reading SPECIFICITY AUDITOR blocks; this
prohibition is structurally parallel to the prohibition on re-reading ANALYST
blocks during regression analysis and is equally unconditional.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun columns non-empty per cell
(verified against SPECIFICITY AUDIT MANIFEST by keyed lookup); Audit B on PARTIAL
rows (see manifest).
Cannot check: Q1/Q2 specificity content (Specificity Auditor domain). Cannot check:
content quality of Present_mechanism or Absent_mechanism cells (Confirmer domain).
Cannot check: evidence quality standards (Judge domain).
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)             | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|-----------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per manifest row [output/C-01]   | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per manifest row [output/C-02]   | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel (required for every row):
    PRESENT: SPECIFICITY AUDIT MANIFEST row for this (Output, Criterion) key shows
             a Q1-TypeLevel result entry
    ABSENT:  manifest row is blank, --, or missing for this key -- format violation

  Q2-IntraRun (required for every row):
    PRESENT: SPECIFICITY AUDIT MANIFEST row for this (Output, Criterion) key shows
             a Q2-IntraRun result entry
    ABSENT:  manifest row is blank, --, or missing for this key -- format violation

  Audit B (required for PARTIAL rows; n/a for PASS and FAIL):
    PRESENT: Present_mechanism and Absent_mechanism cells both contain named content
    MISSING: one or both cells are blank, --, or empty

  Status:
    ACCEPTED: all applicable fields PRESENT
    REJECTED: any applicable field ABSENT or MISSING

For every REJECTED row:
  FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PRESENT/ABSENT]
    Q2-IntraRun:  [PRESENT/ABSENT]
    Audit B:      [PRESENT/MISSING/n/a]

Flagged items require correction and VERIFIER re-audit. Only flagged items
are reopened; ACCEPTED items are closed.

When all rows ACCEPTED across all N outputs:
[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Specificity
Auditor domain), scoring verdicts (Analyst domain).
Do not begin until [VERIFIER COMPLETE] appears above.

For each PARTIAL verdict across all outputs:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status               |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words]                     | YES/NO    | [first 15 words]                    | YES/NO    | CONFIRMED/CHALLENGED |

  Specificity test:
    YES -- names a specific structural element, mechanism, role, gate token,
           design property, or observable structural gap
    NO  -- uses a criterion label, generic quality phrase, or verdict restatement

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items closed.

When all PARTIAL diagnostics are CONFIRMED:
[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two of these
tokens does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy
this gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending. Tie-break protocol (inscribed
here; applied unconditionally when composite scores are equal):
  Primary:   composite score descending
  Secondary: essential_pass count descending (first tie-break dimension)
  Tertiary:  recommended_pass count descending (second tie-break dimension)
  If tied after tertiary: note the tie explicitly; no further inference applied

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output clearly outperforms others, name
the output, the criterion, and the structural mechanism causing the difference.
If no outlier exists: "No excellence signals in this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]
If none: "No failure patterns in this round."

REGRESSION SIGNALS

Draw exclusively from [CHANGE MANIFEST COMPLETE] above. Do not re-read ANALYST
blocks, SPECIFICITY AUDITOR blocks, or the baseline table during synthesis.
These prohibitions are unconditional.

  Regression: [output ID] / [criterion ID] -- prior: [verdict] -- current: [verdict]
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- all outputs ranked; tie-break protocol applied per definition above
[ ] EXCELLENCE SIGNALS -- section complete or "no signals" stated explicitly
[ ] FAILURE PATTERNS -- all-fail criteria identified or "none" stated explicitly
[ ] REGRESSION SIGNALS -- drawn from manifest exclusively; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-02 -- Axes manifest + single-excl: SPECIFICITY AUDIT MANIFEST + forward exclusion only

**Variation axis**: Lifecycle emphasis + phrasing register -- identical to V-01 except the VERIFIER entry condition uses only the forward exclusion clause ([ANALYST COMPLETE] alone does not satisfy this gate) without the reverse exclusion ([SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate). The SPECIFICITY AUDIT MANIFEST and all three C-43 requirements are present.

**Hypothesis**: C-43 PASS -- all three C-43 requirements met: manifest terminal artifact, VERIFIER key reference, SYNTHESIS prohibition on SA blocks. C-44 PARTIAL -- one of the two required symmetric exclusion clauses is present ([ANALYST COMPLETE] alone), the reverse clause ([SPECIFICITY AUDIT COMPLETE] alone) is absent; a reader scanning the VERIFIER header can verify that scoring completed before the audit, but cannot verify from the header alone that a SA-without-ANALYST path is excluded.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

Load prior-round verdicts before scoring begins.

| Variation | Open aspirationals entering this round                                         |
|-----------|--------------------------------------------------------------------------------|
| V-01 R16  | (none -- ceiling achieved, all 35 prior aspirationals PASS; C-43 and C-44 new)|
| V-02 R16  | C-42 PARTIAL; C-43 new; C-44 new                                               |
| V-03 R16  | C-42 FAIL; C-43 new; C-44 new                                                  |
| V-04 R16  | C-44 new (C-43 PASS via SPECIFICITY AUDIT MANIFEST already present)            |
| V-05 R16  | C-43 new (C-44 PASS via symmetric conjunction gate already present)            |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying
  pattern at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two output cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication named as second
  disqualifying pattern; cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression at the scoring site.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline;
  C-03 PASS does not require inline inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table with single merged "Specificity" column.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns; C-29 PASS does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: LEADERBOARD breaks ties in synthesis prose without inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol inscribed at the leaderboard
  definition site; C-04 PASS does not require it.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER entry condition lists only [ANALYST COMPLETE] as gate;
  no dedicated SPECIFICITY AUDITOR role gate token cited in the VERIFIER header.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR role with gate token
  quoted verbatim in VERIFIER entry condition plus explicit [ANALYST COMPLETE] alone
  exclusion clause; the named-gate citation closes the header-silent path.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks without a
  consolidated manifest; VERIFIER cites "per SPECIFICITY AUDITOR" generically;
  Q1/Q2 lookup requires traversing the full SA body.
  Closing mechanism: C-43 requires SPECIFICITY AUDIT MANIFEST table keyed by
  (Output, Criterion) as SA terminal artifact; VERIFIER references by manifest key;
  SYNTHESIS prohibited from re-reading SA blocks; C-42 PASS leaves the dispersed-
  reread path open; C-43 closes it via the keyed-manifest artifact.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                                                               | Cannot Check                                                      |
|---------------------|-----------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                | Scoring verdicts; format compliance; content quality              |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                             | Evidence standards (Judge); format auditing (Verifier)            |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                      | Re-scoring; re-auditing                                           |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                 | Format presence (Verifier); scoring (Analyst)                     |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows               | Q1/Q2 content (SA); evidence standards (Judge)                    |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                        | Format presence (Verifier); scoring (Analyst)                     |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-reading ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]
    above. [ANALYST COMPLETE] alone does not satisfy this gate.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
    gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32, produce a Judge standard entry:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase; the from [Output-N]:
               prefix annotation is required on every ACCEPTABLE entry]"
  UNACCEPTABLE: "[text that would fail -- drawn from provided inputs]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank or NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-02      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-03      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-04      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-05      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-06      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-07      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-08      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-09      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-10      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-11      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-12      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-13      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-14      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-15      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-16      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-17      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-18      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-19      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-20      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-21      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-22      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-23      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-24      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-25      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-26      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-27      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-28      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-29      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-30      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-31      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-32      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |

All 32 rows YES in all three columns before [JUDGE STANDARD COMPLETE] may be issued.

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cells; composite computation; *Why* field;
*Change* field; Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

Before writing any evidence cell, verify it against the Judge ACCEPTABLE/UNACCEPTABLE
pair. If your draft resembles the UNACCEPTABLE pattern, rewrite before entering.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E  | PASS/PARTIAL/FAIL | [specific evidence grounded in this output] | --                | --               |

  Evidence field violations (stated at this definition site):
    Disqualifying pattern 1: evidence could describe any well-designed output
      of this type (cross-type genericity) -- trigger a rewrite before filing
    Disqualifying pattern 2: the same description fits another output in this
      run without modification (cross-output duplication) -- trigger a rewrite
    Both disqualifying patterns are named here; either one is a cell violation.

  Per-row annotations (required for EVERY row; blank is a structural violation):
    *Why* (required): [structural mechanism or design property driving the verdict;
                       a criterion restatement or evidence paraphrase is a violation]
    *Change* (required): exactly one of three values:
      NO CHANGE
      CHANGE from [prior verdict]: [reason]
      NO PRIOR DATA

  PARTIAL row additions (required only on PARTIAL verdicts):
    Present_mechanism (required): [specific structural element preventing FAIL]
    Absent_mechanism (required): [specific structural element preventing PASS]
    A blank Present_mechanism or Absent_mechanism on a PARTIAL row is a structural
    violation equivalent to a blank evidence cell.

  Composite computation (required -- formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [which essential failed, or composite < 80]

  Per-output narrative (required -- three labeled fields):
    Primary differentiator (required): [structural feature explaining this output's
      score differential]
    Primary miss (required): [criterion or structural mechanism most clearly absent]
    Verdict spread (required): [where this output concentrated its points and why]

PROHIBITED CONTENT CATEGORIES (no cell, annotation, or narrative field may
contain any item in this list):

  A. Evaluative prose -- quality assessment without naming a structural element
     Route: rewrite as structural observation with named mechanism
  B. Criterion restatement -- text that rephrases the criterion label as evidence
     Route: rewrite using a structural feature observable in the output
  C. Cross-output generic text -- same sentence could appear in another output
     Route: flag for Specificity Auditor Q2-IntraRun review; rewrite with specific detail
  D. Narrative analysis in scoring cells -- mechanism interpretation or narrative prose
     Route: defer to per-output narrative section; keep scoring cells factual
  E. Novel field labels -- any label not in the permitted set above
     Route: prohibited; *Note*, *Comment*, *Observation*, or any unlisted label
     is a structural violation regardless of content

  No prohibited content category lacks a named destination.

Score all N outputs.
[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.

Sweep all *Change*: CHANGE annotations from every scoring block into a single
manifest table. SYNTHESIS must draw regression signals exclusively from this
manifest and is prohibited from re-reading ANALYST blocks or the baseline table
during synthesis. This prohibition is unconditional.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE annotations appear: "No changes from prior round detected."

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1-TypeLevel and Q2-IntraRun specificity review of every evidence cell;
ANCHOR REVIEW BLOCK application; SPECIFICITY AUDIT MANIFEST production;
revision flagging (see manifest).
Cannot check: scoring verdicts (Analyst domain); format column presence (Verifier
domain); content quality of diagnostic columns (Confirmer domain).
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type -- i.e., would this evidence be equally valid for a correct implementation
    that is not this specific output?"

  Q2 (Intra-run): "Does this evidence fit another output in this run -- i.e.,
    could the same description appear in a different output's cell for this same
    criterion without modification?"

For every evidence cell across all N outputs, apply both questions and record results:

  Output: [output identifier] -- SPECIFICITY AUDITOR pass

  | ID   | Evidence excerpt (first 15 words)  | Q1-TypeLevel | Q2-IntraRun | Action          |
  |------|------------------------------------|--------------|-------------|-----------------|
  | C-01 | [excerpt]                          | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

For every cell where Q1-TypeLevel FAIL or Q2-IntraRun FAIL:
  REVISION FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PASS/FAIL -- reason if FAIL]
    Q2-IntraRun:  [PASS/FAIL -- reason if FAIL]
    Required action: Analyst must revise evidence before this cell may be accepted.

Flagged cells require Analyst revision and SPECIFICITY AUDITOR re-review of the
revised cell only. ACCEPTED cells are closed and not reopened by a revision.

SPECIFICITY AUDIT MANIFEST

After all evidence cells across all N outputs are reviewed, produce this manifest
as the terminal artifact of the SPECIFICITY AUDITOR role. This manifest is the
authoritative Q1/Q2 source for the VERIFIER. The VERIFIER must reference manifest
rows by (Output, Criterion) key; it must not re-read SPECIFICITY AUDITOR per-output
blocks. SYNTHESIS is prohibited from re-reading SPECIFICITY AUDITOR blocks; this
prohibition is unconditional and parallel to the ANALYST-block re-read prohibition.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun columns non-empty per cell
(verified against SPECIFICITY AUDIT MANIFEST by keyed lookup); Audit B on PARTIAL rows.
Cannot check: Q1/Q2 specificity content (Specificity Auditor domain). Cannot check:
content quality of Present_mechanism or Absent_mechanism cells (Confirmer domain).
Cannot check: evidence quality standards (Judge domain).
Do not begin until [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear above.
[ANALYST COMPLETE] alone does not satisfy this gate.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)             | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|-----------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per manifest row [output/C-01]   | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per manifest row [output/C-02]   | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel: PRESENT if SPECIFICITY AUDIT MANIFEST row for (Output, Criterion) key
    shows a Q1-TypeLevel entry; ABSENT if manifest row is blank, --, or missing.
  Q2-IntraRun: PRESENT if manifest row shows a Q2-IntraRun entry; ABSENT otherwise.
  Audit B (PARTIAL rows): PRESENT if both Present/Absent contain named content; MISSING otherwise.
  Status: ACCEPTED if all applicable PRESENT; REJECTED if any ABSENT or MISSING.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Q1-TypeLevel: [P/A] | Q2-IntraRun: [P/A] | Audit B: [P/M/n/a]

When all rows ACCEPTED across all N outputs:
[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Do not begin until [VERIFIER COMPLETE] appears above.

For each PARTIAL verdict across all outputs:

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status               |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words]                     | YES/NO    | [first 15 words]                    | YES/NO    | CONFIRMED/CHALLENGED |

  YES -- names a specific structural element, mechanism, role, gate token, or gap
  NO  -- uses a criterion label, generic quality phrase, or verdict restatement

Challenged items must be rewritten by the Analyst and re-audited by Verifier + Confirmer.

[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite descending | Secondary: essential_pass count descending |
  Tertiary: recommended_pass count descending | Beyond: note tie explicitly

  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
FAILURE PATTERNS
REGRESSION SIGNALS -- draw exclusively from [CHANGE MANIFEST COMPLETE]; do not
re-read ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table.

Pre-close checklist:
[ ] LEADERBOARD
[ ] EXCELLENCE SIGNALS
[ ] FAILURE PATTERNS
[ ] REGRESSION SIGNALS

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axis symm-gate: Symmetric conjunction gate, no SPECIFICITY AUDIT MANIFEST

**Variation axis**: Role sequence -- identical to R16 V-05 (symmetric exclusion architecture). VERIFIER entry condition symmetrically excludes both single-token bypass paths. SPECIFICITY AUDITOR produces standard per-output blocks (no manifest artifact). VERIFIER references "per SPECIFICITY AUDITOR" generically.

**Hypothesis**: C-44 PASS -- symmetric conjunction gate closes both bypass paths; both [ANALYST COMPLETE] alone and [SPECIFICITY AUDIT COMPLETE] alone are explicitly excluded. C-43 FAIL -- no SPECIFICITY AUDIT MANIFEST exists; VERIFIER does not reference manifest rows by key; SYNTHESIS prohibition on SA blocks is absent; the dispersed-SA-body-reread path remains open.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                         |
|-----------|--------------------------------------------------------------------------------|
| V-01 R16  | (none -- ceiling achieved, all 35 prior aspirationals PASS; C-43 and C-44 new)|
| V-02 R16  | C-42 PARTIAL; C-43 new; C-44 new                                               |
| V-03 R16  | C-42 FAIL; C-43 new; C-44 new                                                  |
| V-04 R16  | C-44 new (C-43 PASS via SPECIFICITY AUDIT MANIFEST already present)            |
| V-05 R16  | C-43 new (C-44 PASS via symmetric conjunction gate already present)            |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 requires both disqualifying patterns named at evidence
  field definition site; C-02 PASS alone does not close cross-type genericity.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 requires cross-output duplication as second named pattern;
  a cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline at
  calculation site; C-03 PASS does not require inline inscription.

Failure Mode D -- Combined specificity field
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns; C-29 PASS does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol inscribed at leaderboard
  definition site; C-04 PASS does not require it.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER entry condition lists only [ANALYST COMPLETE]; no
  dedicated SA gate cited in header.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR role, gate token, verbatim
  cite in VERIFIER entry condition, [ANALYST COMPLETE] alone exclusion clause.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but
  not [SPECIFICITY AUDIT COMPLETE] alone; a design where [SPECIFICITY AUDIT COMPLETE]
  is produced without [ANALYST COMPLETE] having appeared is not excluded at the header;
  the reverse bypass path is structurally unaddressed.
  Closing mechanism: C-44 requires the VERIFIER entry condition to additionally
  exclude [SPECIFICITY AUDIT COMPLETE] alone, making neither token independently
  sufficient; C-42 requires only the forward exclusion; C-44 closes the reverse.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                    | Cannot Check                                           |
|---------------------|-----------------------------------------------------|-------------------------------|------------------------------------------------------------------|--------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER     | Scoring verdicts; format compliance; content quality   |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols  | Evidence standards (Judge); format auditing (Verifier) |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table           | Re-scoring; re-auditing                                |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; revision flagging             | Format presence (Verifier); scoring (Analyst)          |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty; Audit B on PARTIAL rows| Q1/Q2 content (SA); evidence standards (Judge)         |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural props?  | Format presence (Verifier); scoring (Analyst)          |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-scoring; re-auditing |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT
    COMPLETE] appear above. [ANALYST COMPLETE] alone does not satisfy this gate.
    [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate.
    Both tokens are required.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32, produce a Judge standard entry:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase; from [Output-N]: prefix required]"
  UNACCEPTABLE: "[text that would fail]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank or NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (one row each) | [name] | YES/NO | YES/NO | YES/NO |

All 32 rows YES in all three columns before [JUDGE STANDARD COMPLETE] may be issued.

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence; composite; *Why*; *Change*; P/A cols.
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|

  Evidence field violations (stated at this definition site):
    Disqualifying pattern 1: cross-type genericity -- trigger a rewrite before filing
    Disqualifying pattern 2: cross-output duplication -- trigger a rewrite
    Both patterns named here; either one is a cell violation.

  *Why* (required): structural mechanism or design property; restatement is a violation
  *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  PARTIAL row additions:
    Present_mechanism (required) | Absent_mechanism (required)

  Composite computation (required -- formula inscribed inline):
    composite = (essential_pass / 4 x 60) + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10) = [result]
    Golden (required): YES -- all essentials PASS; composite >= 80 | NO -- [reason]

  Per-output narrative:
    Primary differentiator (required) | Primary miss (required) | Verdict spread (required)

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -- Route: rewrite as structural observation
  B. Criterion restatement -- Route: rewrite using observable structural feature
  C. Cross-output generic text -- Route: flag for SA Q2-IntraRun; rewrite
  D. Narrative analysis in scoring cells -- Route: defer to narrative section
  E. Novel field labels -- Route: prohibited; *Note*, *Comment*, *Observation* are violations

  No prohibited content category lacks a named destination.

Score all N outputs.
[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.
Sweep all *Change*: CHANGE annotations into a manifest table.
SYNTHESIS draws regression signals exclusively from this manifest; re-reading
ANALYST blocks or the baseline table during synthesis is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1-TypeLevel and Q2-IntraRun review; ANCHOR REVIEW BLOCK; revision flagging.
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK
  Q1: "Could this evidence apply to any well-designed output of this type?"
  Q2: "Does this evidence fit another output in this run without modification?"

For every evidence cell across all N outputs:

  | ID   | Evidence excerpt (first 15 words)  | Q1-TypeLevel | Q2-IntraRun | Action          |
  |------|------------------------------------|--------------|-------------|-----------------|

For every Q1-TypeLevel FAIL or Q2-IntraRun FAIL:
  REVISION FLAG: [output/criterion] -- Analyst must revise; SA re-reviews flagged cell only.

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence -- Q1/Q2 columns non-empty per cell; Audit B on PARTIAL rows.
Cannot check: Q1/Q2 content (SA domain); content quality of P/A cells (Confirmer domain).
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

Per-cell VERIFIER table schema:

  | ID   | Verdict | Evidence excerpt (first 15 words)        | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |

  Q1-TypeLevel: PRESENT if Q1 column non-empty from SPECIFICITY AUDITOR; ABSENT if blank.
  Q2-IntraRun: PRESENT if Q2 column non-empty; ABSENT if blank.
  Audit B (PARTIAL): PRESENT if Present/Absent both named; MISSING if either blank.
  Status: ACCEPTED if applicable PRESENT; REJECTED if any ABSENT/MISSING.

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality of Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.

  | Criterion | Present_mechanism excerpt | Specific? | Absent_mechanism excerpt | Specific? | Status |
  YES -- names structural element, mechanism, gate, or gap
  NO -- criterion label or generic phrase

[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above.

LEADERBOARD
  Tie-break: Primary composite desc | Secondary essential_pass desc | Tertiary recommended_pass desc
  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
FAILURE PATTERNS
REGRESSION SIGNALS -- draw from [CHANGE MANIFEST COMPLETE] only; do not re-read
ANALYST blocks or baseline table.

Pre-close checklist:
[ ] LEADERBOARD
[ ] EXCELLENCE SIGNALS
[ ] FAILURE PATTERNS
[ ] REGRESSION SIGNALS

[SYNTHESIS COMPLETE]
```

---

## V-04 -- Axes manifest-no-synth + symm-gate: Manifest + key + symmetric gate, SYNTHESIS prohibition absent

**Variation axis**: Lifecycle emphasis -- SPECIFICITY AUDIT MANIFEST present as named terminal artifact; VERIFIER references manifest rows by key; VERIFIER entry condition uses symmetric exclusion; SYNTHESIS re-read prohibition for SA blocks is absent (only ANALYST-block and baseline prohibition retained).

**Hypothesis**: C-43 PARTIAL -- two of three C-43 requirements met (manifest exists, VERIFIER references by key); SYNTHESIS SA-block re-read prohibition absent; PARTIAL per C-43 pass condition ("PARTIAL if the manifest exists but... the SYNTHESIS SA-block re-read prohibition is absent"). C-44 PASS -- symmetric exclusion closes both bypass paths.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                         |
|-----------|--------------------------------------------------------------------------------|
| V-01 R16  | (none -- ceiling achieved, all 35 prior aspirationals PASS; C-43 and C-44 new)|
| V-02 R16  | C-42 PARTIAL; C-43 new; C-44 new                                               |
| V-03 R16  | C-42 FAIL; C-43 new; C-44 new                                                  |
| V-04 R16  | C-44 new (C-43 PASS via SPECIFICITY AUDIT MANIFEST already present)            |
| V-05 R16  | C-43 new (C-44 PASS via symmetric conjunction gate already present)            |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 requires both disqualifying patterns at evidence field
  definition site; C-02 PASS does not close cross-type genericity.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 requires cross-output duplication as second named pattern.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline.

Failure Mode D -- Combined specificity field
  Closing mechanism: C-35 requires structurally separated Q1-TypeLevel / Q2-IntraRun
  labeled columns; C-29 PASS does not require separation.

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol inscribed at leaderboard definition.

Failure Mode F -- Header-silent Q1/Q2 audit
  Closing mechanism: C-42 requires named SA role, gate, verbatim cite, exclusion clause.

Failure Mode G -- Dispersed SA body reread
  Typical output: SA produces per-output blocks without consolidated manifest;
  SYNTHESIS traverses full SA body to extract Q1/Q2 results.
  Closing mechanism: C-43 requires SPECIFICITY AUDIT MANIFEST keyed by (Output,
  Criterion); VERIFIER references by key; SYNTHESIS prohibited from re-reading SA blocks.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Closing mechanism: C-44 requires symmetric exclusion: both [ANALYST COMPLETE] alone
  and [SPECIFICITY AUDIT COMPLETE] alone excluded from VERIFIER entry condition.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                                                               | Cannot Check                                           |
|---------------------|-----------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                | Scoring verdicts; format compliance; content quality   |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                             | Evidence standards (Judge); format auditing (Verifier) |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                      | Re-scoring; re-auditing                                |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                 | Format presence (Verifier); scoring (Analyst)          |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows               | Q1/Q2 content (SA); evidence standards (Judge)         |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                        | Format presence (Verifier); scoring (Analyst)          |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-reading ANALYST blocks or baseline table            |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT
    COMPLETE] appear above. [ANALYST COMPLETE] alone does not satisfy this gate.
    [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate.
    Both tokens are required.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards.
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:
  C-[NN]: [name] | ACCEPTABLE: "from [N]: [...]" | UNACCEPTABLE: "[...]"
  Separating property: [A] vs [B]

CONSOLIDATED PRODUCTION-TIME REGISTER (32 rows; all YES before [JUDGE STANDARD COMPLETE])

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (one row each) | | YES/NO | YES/NO | YES/NO |

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID | Criterion | Wt | Verdict | Evidence (required) | Present_mechanism | Absent_mechanism |

  Evidence field violations:
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication
    Both named here; either is a cell violation.

  *Why* (required): structural mechanism; restatement is a violation
  *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  Composite (formula inscribed inline):
    composite = (essential_pass / 4 x 60) + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10) = [result]
    Golden (required): YES / NO -- [reason]

  Narrative: Primary differentiator (req) | Primary miss (req) | Verdict spread (req)

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -> rewrite as structural observation
  B. Criterion restatement -> rewrite using observable structural feature
  C. Cross-output generic -> flag for SA; rewrite
  D. Narrative in scoring cells -> defer to narrative section
  E. Novel field labels -> prohibited; *Note*, *Comment*, *Observation* are violations
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

Sweep all *Change*: CHANGE annotations into manifest table.
SYNTHESIS draws regressions from this manifest exclusively; re-reading ANALYST
blocks or the baseline table is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production.
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK
  Q1: "Could this evidence apply to any well-designed output of this type?"
  Q2: "Does this evidence fit another output in this run without modification?"

Per-output review table:
  | ID | Evidence excerpt | Q1-TypeLevel | Q2-IntraRun | Action |

SPECIFICITY AUDIT MANIFEST

After reviewing all outputs, produce this manifest as the terminal artifact.
VERIFIER references manifest rows by (Output, Criterion) key.

  SPECIFICITY AUDIT MANIFEST
  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence via manifest keyed lookup; Audit B on PARTIAL rows.
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

  | ID | Verdict | Evidence excerpt                               | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status |
  |    | PASS    | [excerpt] -- per manifest row [output/C-NN]   | PRESENT / ABSENT | PRESENT / ABSENT | n/a     |        |

  Q1/Q2: PRESENT if manifest row for (Output, Criterion) key is non-empty; ABSENT otherwise.
  Audit B (PARTIAL): PRESENT if both P/A cells named; MISSING otherwise.

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality of Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.
  YES -- names structural element, mechanism, gate, or gap
  NO -- criterion label or generic phrase
[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above.

LEADERBOARD
  Tie-break: composite desc | essential_pass desc | recommended_pass desc | note tie
  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
FAILURE PATTERNS
REGRESSION SIGNALS -- draw from [CHANGE MANIFEST COMPLETE] only; do not re-read
ANALYST blocks or baseline table. This prohibition is unconditional.

Pre-close checklist:
[ ] LEADERBOARD
[ ] EXCELLENCE SIGNALS
[ ] FAILURE PATTERNS
[ ] REGRESSION SIGNALS

[SYNTHESIS COMPLETE]
```

---

## V-05 -- Axes manifest-no-key + symm-gate: Manifest + SYNTHESIS prohibition + symmetric gate, no VERIFIER key reference

**Variation axis**: Output format -- SPECIFICITY AUDIT MANIFEST produced as named terminal artifact; SYNTHESIS SA-block re-read prohibition present; VERIFIER entry condition uses symmetric exclusion; VERIFIER per-cell entries reference "per SPECIFICITY AUDITOR" generically without keying to manifest rows.

**Hypothesis**: C-43 PARTIAL -- two of three C-43 requirements met (manifest exists, SYNTHESIS prohibition present); VERIFIER does not reference manifest rows by key; PARTIAL per C-43 pass condition ("PARTIAL if the manifest exists but the VERIFIER does not reference it by key"). C-44 PASS -- symmetric exclusion present.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                         |
|-----------|--------------------------------------------------------------------------------|
| V-01 R16  | (none -- ceiling achieved, all 35 prior aspirationals PASS; C-43 and C-44 new)|
| V-02 R16  | C-42 PARTIAL; C-43 new; C-44 new                                               |
| V-03 R16  | C-42 FAIL; C-43 new; C-44 new                                                  |
| V-04 R16  | C-44 new (C-43 PASS via SPECIFICITY AUDIT MANIFEST already present)            |
| V-05 R16  | C-43 new (C-44 PASS via symmetric conjunction gate already present)            |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 requires both disqualifying patterns at definition site.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 requires cross-output duplication as second named pattern.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline.

Failure Mode D -- Combined specificity field
  Closing mechanism: C-35 requires structurally separated Q1/Q2 labeled columns.

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol inscribed at leaderboard definition.

Failure Mode F -- Header-silent Q1/Q2 audit
  Closing mechanism: C-42 requires named SA role, gate, verbatim cite, exclusion clause.

Failure Mode G -- Manifest present but VERIFIER bypasses key lookup
  Typical output: SPECIFICITY AUDIT MANIFEST exists as SA terminal artifact; VERIFIER
  per-cell entries reference "per SPECIFICITY AUDITOR" generically rather than keying
  to manifest rows by (Output, Criterion); the manifest serves as a record artifact
  but is not used as the authoritative retrieval mechanism by the VERIFIER.
  Closing mechanism: C-43 requires VERIFIER per-cell schema to reference manifest rows
  by key (e.g., "per manifest row [output/C-NN]"); generic reference to SPECIFICITY
  AUDITOR body satisfies C-42 but leaves the keyed-lookup path open; C-43 requires
  the manifest to be the authoritative access point, not a parallel record.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Closing mechanism: C-44 requires symmetric exclusion: both [ANALYST COMPLETE] alone
  and [SPECIFICITY AUDIT COMPLETE] alone excluded from VERIFIER entry condition.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                                                               | Cannot Check                                                      |
|---------------------|-----------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                | Scoring verdicts; format compliance; content quality              |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                             | Evidence standards (Judge); format auditing (Verifier)            |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                      | Re-scoring; re-auditing                                           |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                 | Format presence (Verifier); scoring (Analyst)                     |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty per cell; Audit B on PARTIAL rows                                  | Q1/Q2 content (SA); evidence standards (Judge)                    |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                        | Format presence (Verifier); scoring (Analyst)                     |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-reading ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT
    COMPLETE] appear above. [ANALYST COMPLETE] alone does not satisfy this gate.
    [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate.
    Both tokens are required.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards.
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:
  C-[NN]: [name] | ACCEPTABLE: "from [N]: [...]" | UNACCEPTABLE: "[...]"
  Separating property: [A] vs [B]

CONSOLIDATED PRODUCTION-TIME REGISTER (32 rows; all YES before [JUDGE STANDARD COMPLETE])

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (one row each) | | YES/NO | YES/NO | YES/NO |

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID | Criterion | Wt | Verdict | Evidence (required) | Present_mechanism | Absent_mechanism |

  Evidence field violations:
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication
    Both named here; either is a cell violation.

  *Why* (required): structural mechanism; restatement is a violation
  *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  Composite (formula inscribed inline):
    composite = (essential_pass / 4 x 60) + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10) = [result]
    Golden (required): YES / NO -- [reason]

  Narrative: Primary differentiator (req) | Primary miss (req) | Verdict spread (req)

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -> rewrite as structural observation
  B. Criterion restatement -> rewrite using observable structural feature
  C. Cross-output generic -> flag for SA; rewrite
  D. Narrative in scoring cells -> defer to narrative section
  E. Novel field labels -> prohibited; *Note*, *Comment*, *Observation* are violations
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

Sweep all *Change*: CHANGE annotations into manifest table.
SYNTHESIS draws regressions from this manifest exclusively; re-reading ANALYST
blocks or the baseline table is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production.
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK
  Q1: "Could this evidence apply to any well-designed output of this type?"
  Q2: "Does this evidence fit another output in this run without modification?"

Per-output review table:
  | ID | Evidence excerpt (first 15 words) | Q1-TypeLevel | Q2-IntraRun | Action |

For every Q1 FAIL or Q2 FAIL:
  REVISION FLAG: [output/criterion] -- Analyst revises; SA re-reviews that cell only.

SPECIFICITY AUDIT MANIFEST

After reviewing all outputs, produce this manifest as the terminal artifact.
SYNTHESIS is prohibited from re-reading SPECIFICITY AUDITOR blocks; regression
analysis draws from [CHANGE MANIFEST COMPLETE] only. This prohibition is
unconditional and parallel to the ANALYST-block re-read prohibition.

  SPECIFICITY AUDIT MANIFEST
  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence -- Q1/Q2 columns non-empty per cell; Audit B on PARTIAL rows.
Cannot check: Q1/Q2 content (SA domain); content quality of P/A cells (Confirmer domain).
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)        | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel: PRESENT if Q1-TypeLevel column non-empty from SPECIFICITY AUDITOR; ABSENT if blank.
  Q2-IntraRun: PRESENT if Q2-IntraRun column non-empty; ABSENT if blank.
  Audit B (PARTIAL): PRESENT if Present/Absent both named; MISSING otherwise.
  Status: ACCEPTED if all applicable PRESENT; REJECTED if any ABSENT or MISSING.

For every REJECTED row:
  FLAG: [output/criterion] -- Q1: [P/A] | Q2: [P/A] | Audit B: [P/M/n/a]

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality of Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.
  YES -- names structural element, mechanism, gate, or gap
  NO -- criterion label or generic phrase
[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above.

LEADERBOARD
  Tie-break: composite desc | essential_pass desc | recommended_pass desc | note tie
  | Rank | Output | Composite | Golden? |

EXCELLENCE SIGNALS
FAILURE PATTERNS
REGRESSION SIGNALS -- draw from [CHANGE MANIFEST COMPLETE] only; do not re-read
ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table. These prohibitions
are unconditional.

Pre-close checklist:
[ ] LEADERBOARD
[ ] EXCELLENCE SIGNALS
[ ] FAILURE PATTERNS
[ ] REGRESSION SIGNALS

[SYNTHESIS COMPLETE]
```
