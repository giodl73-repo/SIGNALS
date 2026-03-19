"""Write R16 V-01 through V-05 to the golden file."""

PATH = "C:/src/sim/simulations/quest/golden/quest-score-variate-R16-2026-03-15.md"

# Shared PRIOR ROUND LOAD block (same for all variations)
PRIOR = """
PRIOR ROUND LOAD

Load prior-round verdicts before scoring begins.

| Variation | Open aspirationals entering this round                                  |
|-----------|-------------------------------------------------------------------------|
| V-01 R15  | (none -- ceiling achieved, all 34 prior aspirationals PASS; C-42 new)  |
| V-02 R15  | C-35 PARTIAL; C-42 new in this round                                    |
| V-03 R15  | C-35 FAIL; C-42 new in this round                                       |
| V-04 R15  | C-23 PARTIAL; C-42 new in this round                                    |
| V-05 R15  | C-23 PARTIAL; C-42 new in this round                                    |

[PRIOR ROUND LOAD COMPLETE]
"""

# Shared JUDGE block (same for all variations)
JUDGE = """
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
"""

# Shared ANALYST block (same for all variations)
ANALYST = """
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
"""

# Shared CHANGE MANIFEST block
CHANGE_MANIFEST = """
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
"""

# Shared CONFIRMER block
CONFIRMER = """
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
"""

# Shared SYNTHESIS block
SYNTHESIS = """
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
blocks or the baseline table during synthesis. This prohibition is unconditional.

  Regression: [output ID] / [criterion ID] -- prior: [verdict] -- current: [verdict]
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- all outputs ranked; tie-break protocol applied per definition above
[ ] EXCELLENCE SIGNALS -- section complete or "no signals" stated explicitly
[ ] FAILURE PATTERNS -- all-fail criteria identified or "none" stated explicitly
[ ] REGRESSION SIGNALS -- drawn from manifest exclusively; re-read prohibition observed

[SYNTHESIS COMPLETE]
"""

# Anti-pattern anchor -- V-01/V-02/V-04/V-05 use this (Failure Mode F names header-silent audit)
ANTI_PATTERN_FULL = """
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
  Typical output: The same evidence sentence appears in two different outputs
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
  gate; the Q1/Q2 specificity audit is conducted inside the VERIFIER body with
  no dedicated role gate token -- a reader cannot detect from the VERIFIER header
  alone whether a dedicated independent audit completed.
  Closing mechanism: C-42 requires a named SPECIFICITY AUDITOR role with its own
  gate token ([SPECIFICITY AUDIT COMPLETE]); the VERIFIER entry condition must
  quote this gate verbatim with an explicit exclusion clause ([ANALYST COMPLETE]
  alone does not satisfy this gate); the named-gate citation makes the dedicated
  audit independently verifiable from the VERIFIER header without reading the body.
"""

# V-01 Anti-pattern (same as full)
ANTI_V01 = ANTI_PATTERN_FULL

# V-02 Anti-pattern: Failure Mode F is about missing exclusion clause
ANTI_V02 = """
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying
  pattern at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two outputs cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication named as second
  disqualifying pattern; cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression at the scoring site.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline at the
  calculation site; C-03 PASS does not require inline inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table with single merged "Specificity" column.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns; C-29 PASS does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: LEADERBOARD breaks ties in synthesis prose without inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol with named secondary and tertiary
  dimensions inscribed at the leaderboard definition site; C-04 PASS does not require it.

Failure Mode F -- Verbatim cite without exclusion clause
  Typical output: VERIFIER entry condition says "Do not begin until [SPECIFICITY AUDIT
  COMPLETE] appears above" -- the gate is cited verbatim but the exclusion clause
  stating [ANALYST COMPLETE] alone does not satisfy this gate is absent; a reader
  cannot determine from the header whether [ANALYST COMPLETE] would have been
  sufficient in a prior design version.
  Closing mechanism: C-42 requires the VERIFIER entry condition to include an
  explicit exclusion clause; verbatim cite alone satisfies C-42 requirements 1-3
  but not requirement 4; the exclusion clause closes the bypass-ambiguity path that
  a verbatim-cite-only header leaves open.
"""

# V-03 Anti-pattern: Failure Mode F is about sub-phase without role gate
ANTI_V03 = """
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying
  pattern at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two outputs cells for the same criterion.
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

Failure Mode F -- Named sub-phase without dedicated role gate
  Typical output: VERIFIER body contains a labeled SPECIFICITY AUDITOR SUB-PHASE
  section that applies Q1/Q2 review; the sub-phase closes with a section delimiter,
  not a role gate token; VERIFIER entry condition lists only [ANALYST COMPLETE];
  the dedicated audit is invisible from the VERIFIER header.
  Closing mechanism: C-42 requires SPECIFICITY AUDITOR to be a named role with its
  own gate token, not a sub-phase inside another role; the named-role gate token is
  what makes the dedicated audit verifiable from the VERIFIER header; a sub-phase
  marker inside the VERIFIER body does not close the header-silent path.
"""

# V-05 Anti-pattern: Failure Mode F is about single-direction exclusion vs symmetric
ANTI_V05 = """
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying
  pattern at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two outputs cells for the same criterion.
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

Failure Mode F -- Single-direction exclusion clause (asymmetric gate)
  Typical output: VERIFIER entry condition states "[ANALYST COMPLETE] alone does not
  satisfy this gate" but does not state "[SPECIFICITY AUDIT COMPLETE] alone does not
  satisfy this gate"; a reader can confirm the dedicated audit was required but cannot
  confirm from the header that [ANALYST COMPLETE] alone is also insufficient.
  Closing mechanism: Symmetric exclusion adds the complementary clause closing the
  reverse bypass path; C-42 requires only the [ANALYST COMPLETE] alone exclusion;
  symmetric exclusion is a superset closing both single-token bypass paths from the
  VERIFIER header; the anti-pattern characterizes the asymmetric path that C-42 closes
  at its floor and symmetric exclusion closes at its ceiling.
"""

# Role dependency manifest strings
MANIFEST_V01 = """
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

A row with any blank cell is a structural gap. No role may begin unless its
Requires entry appears in the output above.

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
"""

# V-02 manifest: VERIFIER requires both tokens but gate rule has no exclusion clause
MANIFEST_V02 = """
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
  - VERIFIER cannot begin without [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]
    above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
    gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
"""

# V-03 manifest: No SPECIFICITY AUDITOR role; VERIFIER requires only [ANALYST COMPLETE]
MANIFEST_V03 = """
ROLE DEPENDENCY MANIFEST

| Role            | Requires                                                                                             | Produces                   | Domain (ONLY)                                                                    | Cannot Check                                           |
|-----------------|------------------------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------|
| JUDGE           | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]  | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                     | Scoring verdicts; format compliance; content quality   |
| ANALYST         | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]         | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                  | Evidence standards (Judge); format auditing (Verifier) |
| CHANGE MANIFEST | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE] | Sweep *Change*: CHANGE annotations into manifest table                           | Re-scoring; re-auditing                                |
| VERIFIER        | [ANALYST COMPLETE]                                                                                   | [VERIFIER COMPLETE]        | Specificity sub-phase (Q1/Q2); format presence (Q1/Q2 columns); Audit B         | Content quality (Confirmer); evidence standards (Judge)|
| CONFIRMER       | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]    | Content quality: do Present/Absent cells name structural properties?              | Format presence (Verifier); scoring (Analyst)          |
| SYNTHESIS       | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)          | Leaderboard; excellence signals; failure patterns; regression signals             | Re-scoring; re-auditing                                |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
"""

# V-04 manifest: adds SPECIFICITY AUDIT MANIFEST to SPECIFICITY AUDITOR domain;
# SYNTHESIS prohibition extended
MANIFEST_V04 = """
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                            | Produces                      | Domain (ONLY)                                                                                          | Cannot Check                                           |
|---------------------|-----------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                         | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                           | Scoring verdicts; format compliance; content quality   |
| ANALYST             | [JUDGE STANDARD COMPLETE]                           | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                        | Evidence standards (Judge); format auditing (Verifier) |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                  | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                 | Re-scoring; re-auditing                                |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                  | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging            | Format presence (Verifier); scoring (Analyst)          |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows          | Q1/Q2 content (SA); evidence standards (Judge)         |
| CONFIRMER           | [VERIFIER COMPLETE]                                 | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                   | Format presence (Verifier); scoring (Analyst)          |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output) | Leaderboard; excellence signals; failure patterns; regression signals | Re-reading SPECIFICITY AUDITOR blocks or baseline table|

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
  - SYNTHESIS may not re-read ANALYST blocks, SPECIFICITY AUDITOR blocks, or the
    baseline table during synthesis. This prohibition is unconditional.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
"""

# V-05 manifest: symmetric exclusion in gate rules
MANIFEST_V05 = """
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
  - VERIFIER cannot begin without BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]
    above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
    COMPLETE] alone does not satisfy this gate. Both tokens are required.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
    gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
"""

# SPECIFICITY AUDITOR role body (shared by V-01, V-02, V-04, V-05)
SA_ROLE = """
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1-TypeLevel and Q2-IntraRun specificity review of every evidence cell;
ANCHOR REVIEW BLOCK application; revision flagging (see manifest).
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

When all evidence cells PASS both Q1-TypeLevel and Q2-IntraRun across all N outputs:
[SPECIFICITY AUDIT COMPLETE]
"""

# V-04 adds a manifest to the SA role
SA_ROLE_V04 = SA_ROLE.replace(
    "When all evidence cells PASS both Q1-TypeLevel and Q2-IntraRun across all N outputs:\n[SPECIFICITY AUDIT COMPLETE]",
    """SPECIFICITY AUDIT MANIFEST

After all outputs are reviewed, sweep all Q1/Q2 results into a keyed manifest table.
VERIFIER uses this manifest as the authoritative Q1/Q2 source; per-cell VERIFIER
table entries reference this manifest by output+criterion key.

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action |
  |--------|-----------|--------------|-------------|--------------|

This manifest is the single inspectable artifact for all SPECIFICITY AUDITOR
production-time obligations. No Q1/Q2 result may be tracked outside this manifest.

When all cells ACCEPT and manifest is complete:
[SPECIFICITY AUDIT COMPLETE]"""
)

# VERIFIER role body -- V-01 version (requires SA gate + exclusion clause)
VERIFIER_V01 = """
ROLE 4: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun columns non-empty per cell;
Present_mechanism and Absent_mechanism non-emptiness on PARTIAL rows (see manifest).
Cannot check: Q1/Q2 specificity content (Specificity Auditor domain). Cannot check:
content quality of Present_mechanism or Absent_mechanism cells (Confirmer domain).
Cannot check: evidence quality standards (Judge domain).
Do not begin until [SPECIFICITY AUDIT COMPLETE] appears above.
[ANALYST COMPLETE] alone does not satisfy this gate.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)        | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel (required for every row):
    PRESENT: Q1-TypeLevel column contains a non-empty result from SPECIFICITY AUDITOR
    ABSENT:  the column is blank, --, or empty -- format violation

  Q2-IntraRun (required for every row):
    PRESENT: Q2-IntraRun column contains a non-empty result from SPECIFICITY AUDITOR
    ABSENT:  the column is blank, --, or empty -- format violation

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
"""

# VERIFIER V-02: same as V-01 but entry condition has no exclusion clause
VERIFIER_V02 = VERIFIER_V01.replace(
    "Do not begin until [SPECIFICITY AUDIT COMPLETE] appears above.\n[ANALYST COMPLETE] alone does not satisfy this gate.",
    "Do not begin until [SPECIFICITY AUDIT COMPLETE] appears above."
)

# VERIFIER V-03: sub-phase inside VERIFIER, entry condition only [ANALYST COMPLETE]
VERIFIER_V03 = """
ROLE 3: VERIFIER

Domain: Specificity sub-phase (Q1/Q2 review of every evidence cell); format presence
(Q1-TypeLevel and Q2-IntraRun columns non-empty); Audit B on PARTIAL rows (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells (Confirmer).
Cannot check: evidence quality standards (Judge domain).
Do not begin until [ANALYST COMPLETE] appears above.

--- SPECIFICITY AUDITOR SUB-PHASE ---

The following two questions govern specificity review for all evidence cells.
This sub-phase runs before the per-cell format table below.

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type -- i.e., would this evidence be equally valid for a correct implementation
    that is not this specific output?"

  Q2 (Intra-run): "Does this evidence fit another output in this run -- i.e.,
    could the same description appear in a different output's cell for this same
    criterion without modification?"

For every evidence cell across all N outputs:

  Output: [output identifier] -- Specificity Sub-Phase

  | ID   | Evidence excerpt (first 15 words)  | Q1-TypeLevel | Q2-IntraRun | Action          |
  |------|------------------------------------|--------------|-------------|-----------------|
  | C-01 | [excerpt]                          | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

For every FAIL in either column, require Analyst revision before proceeding to
the per-cell format table below.

--- SPECIFICITY PRE-PASS COMPLETE ---

Per-cell VERIFIER format table (runs after specificity sub-phase above):

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)    | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|--------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt]                            | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                            | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel: PRESENT if non-empty per sub-phase above; ABSENT is a format violation.
  Q2-IntraRun:  PRESENT if non-empty per sub-phase above; ABSENT is a format violation.
  Audit B (PARTIAL rows): PRESENT if both Present/Absent contain named content; MISSING otherwise.
  Status: ACCEPTED if all applicable PRESENT; REJECTED if any ABSENT or MISSING.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Q1: [result] / Q2: [result] / Audit B: [result]

When all rows ACCEPTED:
[VERIFIER COMPLETE]
"""

# VERIFIER V-04: references SPECIFICITY AUDIT MANIFEST by keyed lookup
VERIFIER_V04 = """
ROLE 4: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun columns non-empty per cell
(verified against SPECIFICITY AUDIT MANIFEST by keyed lookup); Audit B on PARTIAL rows.
Cannot check: Q1/Q2 specificity content (Specificity Auditor domain). Cannot check:
content quality of Present_mechanism or Absent_mechanism cells (Confirmer domain).
Do not begin until [SPECIFICITY AUDIT COMPLETE] appears above.
[ANALYST COMPLETE] alone does not satisfy this gate.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)                  | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|-----------------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per manifest row [output/C-01]         | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per manifest row [output/C-02]         | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel: PRESENT if SPECIFICITY AUDIT MANIFEST row for this output+criterion
    shows a Q1-TypeLevel result; ABSENT if manifest row is blank or missing.
  Q2-IntraRun: PRESENT if manifest row shows a Q2-IntraRun result; ABSENT otherwise.
  Audit B (PARTIAL rows): PRESENT if both Present/Absent contain named content; MISSING otherwise.
  Status: ACCEPTED if all applicable PRESENT; REJECTED if any ABSENT or MISSING.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PRESENT/ABSENT]
    Q2-IntraRun:  [PRESENT/ABSENT]
    Audit B:      [PRESENT/MISSING/n/a]

Flagged items require correction and VERIFIER re-audit. Only flagged items are
reopened; ACCEPTED items are closed.

When all rows ACCEPTED across all N outputs:
[VERIFIER COMPLETE]
"""

# VERIFIER V-05: symmetric exclusion in entry condition
VERIFIER_V05 = """
ROLE 4: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun columns non-empty per cell;
Present_mechanism and Absent_mechanism non-emptiness on PARTIAL rows (see manifest).
Cannot check: Q1/Q2 specificity content (Specificity Auditor domain). Cannot check:
content quality of Present_mechanism or Absent_mechanism cells (Confirmer domain).
Cannot check: evidence quality standards (Judge domain).
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)        | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- per SPECIFICITY AUDITOR     | PRESENT / ABSENT | PRESENT / ABSENT | PRESENT | ACCEPTED |

  Q1-TypeLevel (required for every row):
    PRESENT: Q1-TypeLevel column contains a non-empty result from SPECIFICITY AUDITOR
    ABSENT:  the column is blank, --, or empty -- format violation

  Q2-IntraRun (required for every row):
    PRESENT: Q2-IntraRun column contains a non-empty result from SPECIFICITY AUDITOR
    ABSENT:  the column is blank, --, or empty -- format violation

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
"""

# V-04 SYNTHESIS: adds re-read prohibition for SPECIFICITY AUDITOR blocks
SYNTHESIS_V04 = SYNTHESIS.replace(
    "Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND\n[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two of these\ntokens does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy\nthis gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.",
    "Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND\n[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two of these\ntokens does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy\nthis gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.\nDo not re-read ANALYST blocks, SPECIFICITY AUDITOR blocks, or the baseline table.\nThis prohibition is unconditional."
)

# ----- Assemble each variation -----

def wrap_prompt(body):
    return "```\n" + body.strip() + "\n```\n"

def make_prompt(prior, anti, manifest, judge, analyst, change_manifest, sa_role, verifier, confirmer, synthesis):
    parts = [
        "You are running quest-score.\n\nquest-score scores N skill outputs against a rubric. Each output receives a\nper-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,\nand a golden-threshold determination. The scorecard includes a ranked leaderboard,\nexcellence signals, failure patterns, and regression signals.\n\n---",
        prior,
        "---",
        anti,
        "---",
        manifest,
        "---",
        judge,
        "---",
        analyst,
        "---",
        change_manifest,
        "---",
        sa_role,
        "---",
        verifier,
        "---",
        confirmer,
        "---",
        synthesis,
    ]
    return "\n".join(p.strip() for p in parts)

def make_prompt_v03(prior, anti, manifest, judge, analyst, change_manifest, verifier_with_sub, confirmer, synthesis):
    """V-03 has no separate SA role."""
    parts = [
        "You are running quest-score.\n\nquest-score scores N skill outputs against a rubric. Each output receives a\nper-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,\nand a golden-threshold determination. The scorecard includes a ranked leaderboard,\nexcellence signals, failure patterns, and regression signals.\n\n---",
        prior,
        "---",
        anti,
        "---",
        manifest,
        "---",
        judge,
        "---",
        analyst,
        "---",
        change_manifest,
        "---",
        verifier_with_sub,
        "---",
        confirmer,
        "---",
        synthesis,
    ]
    return "\n".join(p.strip() for p in parts)

v01_prompt = make_prompt(PRIOR, ANTI_V01, MANIFEST_V01, JUDGE, ANALYST, CHANGE_MANIFEST, SA_ROLE, VERIFIER_V01, CONFIRMER, SYNTHESIS)
v02_prompt = make_prompt(PRIOR, ANTI_V02, MANIFEST_V02, JUDGE, ANALYST, CHANGE_MANIFEST, SA_ROLE, VERIFIER_V02, CONFIRMER, SYNTHESIS)
v03_prompt = make_prompt_v03(PRIOR, ANTI_V03, MANIFEST_V03, JUDGE, ANALYST, CHANGE_MANIFEST, VERIFIER_V03, CONFIRMER, SYNTHESIS)
v04_prompt = make_prompt(PRIOR, ANTI_PATTERN_FULL, MANIFEST_V04, JUDGE, ANALYST, CHANGE_MANIFEST, SA_ROLE_V04, VERIFIER_V04, CONFIRMER, SYNTHESIS_V04)
v05_prompt = make_prompt(PRIOR, ANTI_V05, MANIFEST_V05, JUDGE, ANALYST, CHANGE_MANIFEST, SA_ROLE, VERIFIER_V05, CONFIRMER, SYNTHESIS)

sections = [
    ("V-01 -- Axis SA-full: Named SPECIFICITY AUDITOR role, gate, verbatim cite, exclusion clause",
     "Role sequence -- a named SPECIFICITY AUDITOR role is inserted between ANALYST and "
     "VERIFIER. It owns the ANCHOR REVIEW BLOCK and applies Q1/Q2 to every evidence cell. "
     "Its gate [SPECIFICITY AUDIT COMPLETE] is quoted verbatim in the VERIFIER entry "
     "condition with explicit exclusion: [ANALYST COMPLETE] alone does not satisfy this "
     "gate. A reader scanning the VERIFIER header can confirm the dedicated audit completed "
     "without reading the body.",
     "C-42 PASS -- all four C-42 requirements met: named role, own gate, verbatim cite in "
     "VERIFIER entry condition, exclusion clause. All 34 prior aspirational PASSes from R15 "
     "V-01 preserved. C-23 full PASS via *Note*, *Comment*, *Observation* prohibition.",
     v01_prompt),

    ("V-02 -- Axis SA-gate-no-excl: Named SPECIFICITY AUDITOR role, gate, verbatim cite, no exclusion clause",
     "Role sequence -- identical to V-01 with one change: the VERIFIER entry condition quotes "
     "[SPECIFICITY AUDIT COMPLETE] verbatim but omits the exclusion clause. The gate rule in "
     "the manifest requires both tokens but does not add the sentence [ANALYST COMPLETE] alone "
     "does not satisfy this gate.",
     "C-42 PARTIAL -- named role exists (req 1), gate token exists (req 2), VERIFIER entry "
     "condition cites gate verbatim (req 3), but exclusion clause is absent (req 4 missing). "
     "A reader scanning the VERIFIER header sees [SPECIFICITY AUDIT COMPLETE] required but "
     "cannot rule out that [ANALYST COMPLETE] alone would have been sufficient under a prior "
     "design -- the exclusion clause that closes this ambiguity is absent.",
     v02_prompt),

    ("V-03 -- Axis SA-sub: SPECIFICITY AUDITOR as named sub-phase inside VERIFIER, no dedicated role gate",
     "Role sequence -- no separate SPECIFICITY AUDITOR role exists in the manifest. The "
     "VERIFIER body opens with a labeled SPECIFICITY AUDITOR SUB-PHASE section that applies "
     "Q1/Q2 review before the per-cell format table. This sub-phase closes with a section "
     "marker (a prose delimiter, not a role gate token). The VERIFIER entry condition requires "
     "[ANALYST COMPLETE] only. From the VERIFIER header, Q1/Q2 work is invisible.",
     "C-42 FAIL -- no dedicated SPECIFICITY AUDITOR role gate token exists; the VERIFIER "
     "entry condition does not cite a dedicated audit gate; the header-silent path is not "
     "closed. All three of C-42 requirements 1, 2, and 3 are absent or not met as separate "
     "role constructs.",
     v03_prompt),

    ("V-04 -- Axes SA-full + manifest: V-01 + SPECIFICITY AUDITOR produces audit manifest referenced by VERIFIER",
     "Role sequence + lifecycle emphasis -- V-01 architecture extended so the SPECIFICITY "
     "AUDITOR produces a SPECIFICITY AUDIT MANIFEST table (parallel to CHANGE MANIFEST) that "
     "records Q1/Q2 results keyed by output+criterion. The VERIFIER per-cell entries reference "
     "this manifest by key. SYNTHESIS is additionally prohibited from re-reading SPECIFICITY "
     "AUDITOR blocks.",
     "C-42 PASS -- all four C-42 requirements met identically to V-01. The manifest extension "
     "is orthogonal to C-42: it strengthens traceability but does not add or remove any C-42 "
     "requirement. Expected to generate an excellence signal pointing toward a C-43 candidate: "
     "SPECIFICITY AUDIT MANIFEST as a keyed-lookup artifact making Q1/Q2 results independently "
     "retrievable by output+criterion key without reading the full SA pass.",
     v04_prompt),

    ("V-05 -- Axes SA-full + symm-excl: V-01 + symmetric dual-exclusion in VERIFIER entry condition",
     "Role sequence + lifecycle emphasis -- identical to V-01 except the VERIFIER entry "
     "condition uses symmetric exclusion: both [ANALYST COMPLETE] alone does not satisfy "
     "this gate AND [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate. Both "
     "single-token bypass paths are explicitly closed in the header.",
     "C-42 PASS -- all four C-42 requirements met. The symmetric exclusion is a superset of "
     "C-42 requirement 4: C-42 only requires the [ANALYST COMPLETE] alone exclusion; V-05 "
     "adds the symmetric [SPECIFICITY AUDIT COMPLETE] alone exclusion as well. Expected to "
     "generate an excellence signal pointing toward a C-43 candidate: symmetric conjunction "
     "gate closing BOTH single-token bypass paths at the VERIFIER entry condition header.",
     v05_prompt),
]

with open(PATH, 'a') as f:
    for title, axis_desc, hypothesis, prompt in sections:
        f.write(f"\n## {title}\n\n")
        f.write(f"**Variation axis**: {axis_desc}\n\n")
        f.write(f"**Hypothesis**: {hypothesis}\n\n")
        f.write(wrap_prompt(prompt))
        f.write("\n---\n")

print("All 5 variations written OK")
