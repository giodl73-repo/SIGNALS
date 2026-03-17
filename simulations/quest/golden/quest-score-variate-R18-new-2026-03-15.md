# quest-score Variations -- Round 18
**Skill**: quest-score
**Rubric**: v17 (C-01--C-05 essential, C-06--C-07 recommended, C-08--C-45 aspirational; denominator /38)
**Scoring context**: quest-rubric outputs (N_essential=4, N_recommended=3, N_aspirational=25)
**Date**: 2026-03-15
**Round**: 18

---

## Design logic

### Unachieved ceiling entering R18

R17 V-01 achieved ceiling with all 37 aspirationals PASS (rubric v16, denominator /37).
Rubric v17 adds C-45 (multi-component pass condition numbered-requirement enumeration,
denominator /38).

| Criterion | R17 status | Gap analysis |
|-----------|------------|--------------|
| C-45 | NOT IN RUBRIC (new in v17) | C-45 requires multi-component pass conditions (N>=2 requirements) to enumerate each requirement with an explicit label at the definition site, enabling PARTIAL verdicts to cite "req N not met" as a structural reference rather than a descriptive reconstruction. In V-01 R17: Failure Mode G's closing mechanism lists C-43's three requirements in prose ("requires the SPECIFICITY AUDITOR to produce a named manifest... the VERIFIER references by key... SYNTHESIS is prohibited...") without numbered labels. Failure Mode H's closing mechanism lists C-44's two requirements in prose without numbered labels. The SPECIFICITY AUDIT MANIFEST definition in ROLE 3 states three conditions in prose without numbered labels. When a PARTIAL verdict on C-43 cites "req 1 met / req 2 not met", those numbers are supplied by the scorer from context -- they are not inscribed at any definition site. C-45 closes this by requiring "Req 1: / Req 2: / Req 3:" labels at each multi-component definition site. |

### Formula change

Rubric v17 denominator: 37 -> 38. Aspirational formula: `(aspirational_pass/38 x 220)`, max 310
unchanged. All R18 variations carry this update in the JUDGE STANDARD domain declaration.
The ANALYST scoring-context formula remains unchanged (quest-rubric: `essential_pass/4 x 60 +
recommended_pass/3 x 30 + aspirational_pass/25 x 10`).

### New mechanism gap: C-45

**For C-45 (multi-component pass condition -- numbered-requirement enumeration at definition site):**

C-43's three requirements and C-44's two requirements are stated in prose at their definition
sites. A scorer reading a PARTIAL verdict on C-43 that cites "req 1 met / req 2 met / req 3 not
met" cannot verify whether those numbers correspond to the actual requirements without re-reading
the definition. C-45 requires each requirement in any multi-component pass condition (N >= 2)
to carry an explicit label ("Req 1:", "Req 2:", "Req 3:") at the definition site. After labeling,
a PARTIAL verdict can cite "req 3 not met" as a structural reference pointing to the labeled
entry, not as a descriptive reconstruction.

Multi-component pass conditions in the V-01 R17 skill body requiring enumeration:
1. Failure Mode G closing mechanism (C-43): three requirements in prose
2. Failure Mode H closing mechanism (C-44): two requirements in prose
3. ROLE 3 SPECIFICITY AUDIT MANIFEST conditions (parallel to C-43): three conditions in prose

Test for C-45:
- PASS: ALL multi-component pass conditions across ALL their definition sites carry explicit
  "Req N:" labels. A scorer giving a C-43 PARTIAL can cite "req 2 not met" by pointing to the
  labeled entry without paraphrasing the requirement from context.
- PARTIAL: SOME multi-component pass conditions have numbered labels but not all definition
  sites are enumerated. Some PARTIAL verdicts can cite by number; others cannot.
- FAIL: No multi-component pass conditions have numbered labels. All PARTIAL verdicts must
  describe by effect rather than cite by structural reference.

### New axes for R18

| Axis | Label | Mechanism |
|------|-------|-----------|
| ENUM-ALL | Full enumeration at all sites | "Req 1: / Req 2: / Req 3:" labels added to Failure Mode G closing mechanism (C-43, 3 reqs), Failure Mode H closing mechanism (C-44, 2 reqs), and ROLE 3 SPECIFICITY AUDIT MANIFEST conditions (3 reqs). New Failure Mode I names the C-45 pattern. All three definition sites enumerated. Closes C-45. |
| ENUM-C43 | C-43 sites only | Numbered labels added to Failure Mode G AND ROLE 3 manifest conditions (both C-43 definition sites). Failure Mode H (C-44) remains prose. Tests whether C-43 site-complete enumeration without C-44 enumeration satisfies C-45 or yields PARTIAL. |
| ENUM-C44 | C-44 site only | Numbered labels added to Failure Mode H (C-44, 2 reqs) only. Failure Mode G and ROLE 3 remain prose. Tests opposite partial-site path. |
| ENUM-FM | Failure Mode sites only | Numbered labels added to Failure Mode G AND Failure Mode H. ROLE 3 manifest conditions remain prose. Tests whether FM-layer enumeration alone (without ROLE 3 definition site) satisfies C-45. |
| INLINE-NUM | Inline numeric ordering | All definition sites use "(1) ... (2) ... (3) ..." inline numbering in prose rather than dedicated "Req N:" label lines. Tests whether inline numbering satisfies C-45 or only dedicated label format satisfies the "explicit label at definition site" requirement. |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (ENUM-ALL)**: All three definition sites enumerated. Req 1/2/3 labels in Failure Mode G
  (C-43, 3 reqs), Req 1/2 labels in Failure Mode H (C-44, 2 reqs), Req 1/2/3 labels in ROLE 3
  manifest. New Failure Mode I added. Full V-01 R17 base: SPECIFICITY AUDIT MANIFEST (C-43),
  symmetric conjunction gate (C-44), three-way SYNTHESIS gate, CHANGE MANIFEST, CONFIRMER,
  inspection-without-reading schema, 32-row register, YES-only gate, formula /25 (scoring
  context). Predicts: C-45 PASS; all 37 prior aspirationals carried.

- **V-02 (ENUM-C43)**: Both C-43 definition sites enumerated (FM G + ROLE 3), C-44 site (FM H)
  prose only. Full V-01 R17 base. Predicts: C-45 PARTIAL -- FM H closing mechanism describes
  C-44's two requirements in prose; PARTIAL C-44 verdicts cannot cite by number.

- **V-03 (ENUM-C44)**: C-44 site (FM H) enumerated with Req 1/2 labels. Both C-43 sites (FM G,
  ROLE 3) remain prose. Full V-01 R17 base. Predicts: C-45 PARTIAL -- FM G and ROLE 3 describe
  C-43's three requirements without labels; PARTIAL C-43 verdicts cannot cite by number.

### Combination selections (V-04, V-05)

- **V-04 (ENUM-FM)**: Failure Mode G (C-43) and Failure Mode H (C-44) have numbered labels.
  ROLE 3 SPECIFICITY AUDIT MANIFEST conditions remain prose. Probes whether the Failure Mode
  layer (two sites) satisfies C-45 without the ROLE 3 definition site, or whether the ROLE 3
  site is independently required. Full V-01 R17 base. Predicts: C-45 PARTIAL -- ROLE 3 is a
  structural definition site for C-43's requirements; FM G enumeration without ROLE 3 enumeration
  leaves one C-43 definition site with prose-only requirements.

- **V-05 (INLINE-NUM)**: All definition sites use inline "(1) / (2) / (3)" numbering in prose
  rather than "Req 1: / Req 2: / Req 3:" dedicated label lines. Tests format requirement: does
  C-45 require the dedicated "Req N:" label form or is ordered inline numbering sufficient?
  Full V-01 R17 base. Predicts: C-45 PARTIAL -- inline numbering provides ordering but a scorer
  citing "req 1 not met" cannot point to a structurally labeled entry; "(1)" is an inline
  sequence marker, not a citable requirement label.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Failure Mode I (C-45 pattern named) | YES | YES | YES | YES | YES |
| Failure Mode G "Req 1/2/3:" labels for C-43 | YES | YES | NO | YES | NO (inline) |
| Failure Mode H "Req 1/2:" labels for C-44 | YES | NO | YES | YES | NO (inline) |
| ROLE 3 manifest "Req 1/2/3:" labels | YES | YES | NO | NO | NO (inline) |
| Inline "(1)/(2)/(3)" numbering in lieu of Req N | NO | NO | NO | NO | YES |
| SPECIFICITY AUDIT MANIFEST (C-43 PASS) | YES | YES | YES | YES | YES |
| Symmetric conjunction gate (C-44 PASS) | YES | YES | YES | YES | YES |
| CHANGE MANIFEST with re-read prohibition | YES | YES | YES | YES | YES |
| Three-way SYNTHESIS gate (BOTH...AND...AND) | YES | YES | YES | YES | YES |
| Inspection-without-reading schema (C-36) | YES | YES | YES | YES | YES |
| CONFIRMER role | YES | YES | YES | YES | YES |
| PRIOR ROUND LOAD with per-variation table | YES | YES | YES | YES | YES |
| ANTI-PATTERN ANCHOR failure modes A-I | YES | YES | YES | YES | YES |
| YES-only gate rule | YES | YES | YES | YES | YES |
| Register rows | 32 | 32 | 32 | 32 | 32 |
| Formula divisor (scoring context) | /25 | /25 | /25 | /25 | /25 |
| Essential denominator (scoring context) | /4 | /4 | /4 | /4 | /4 |

---

## V-01 -- Axis ENUM-ALL: Full numbered-requirement enumeration at all multi-component definition sites (C-45 ceiling)

**Variation axis**: Numbered-requirement enumeration -- all three multi-component pass condition
definition sites in the skill body carry explicit "Req N:" labels. Failure Mode G's C-43 closing
mechanism enumerates three requirements (Req 1: manifest terminal artifact; Req 2: VERIFIER key
reference; Req 3: SYNTHESIS re-read prohibition). Failure Mode H's C-44 closing mechanism
enumerates two requirements (Req 1: [ANALYST COMPLETE] alone excluded; Req 2: [SPECIFICITY
AUDIT COMPLETE] alone excluded). ROLE 3 SPECIFICITY AUDIT MANIFEST conditions enumerate
three requirements with matching Req labels. New Failure Mode I names the C-45 prose-only
failure mode. Full V-01 R17 base: SPECIFICITY AUDIT MANIFEST (C-43), symmetric conjunction
gate (C-44), CHANGE MANIFEST phase, CONFIRMER, three-way SYNTHESIS gate, inspection-without-
reading schema. 32-row register, YES-only gate, formula /25.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-45 PASS: all multi-component pass conditions have numbered labels at their definition sites. FM G cites "Req 1/2/3" for C-43; FM H cites "Req 1/2" for C-44; ROLE 3 cites "Req 1/2/3" for the manifest conditions. A scorer giving C-43 PARTIAL can write "req 2 not met" as a structural citation. C-43 PASS (carried): manifest artifact present. C-44 PASS (carried): symmetric exclusion present. | All 37 prior aspirationals carried PASS. Formula /38 in domain declaration (updated from /37). Failure Mode I (new) enables C-45 PASS via named failure mode for the prose-only pattern. | V-02 isolates C-43 site enumeration without C-44 to confirm PARTIAL path. V-03 isolates C-44 site only. V-04 tests FM-layer alone without ROLE 3 to detect whether ROLE 3 is an independent definition site. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

Load prior-round verdicts before scoring begins.

| Variation | Open aspirationals entering this round                                          |
|-----------|---------------------------------------------------------------------------------|
| V-01 R17  | (none -- ceiling achieved, all 37 prior aspirationals PASS; C-45 new)          |
| V-02 R17  | C-43 PASS; C-44 PARTIAL; C-45 new                                              |
| V-03 R17  | C-43 FAIL; C-44 PASS; C-45 new                                                 |
| V-04 R17  | C-43 PARTIAL (req 3 not met); C-44 PASS; C-45 new                              |
| V-05 R17  | C-43 PARTIAL (req 2 not met); C-44 PASS; C-45 new                              |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

The following failure modes appear before scoring begins. Each failure mode is
paired with a dedicated closing mechanism naming the criterion ID that enforces
the close. This enables bidirectional lookup: failure mode -> mechanism -> criterion ID.

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires the evidence field definition to name cross-type
  genericity as a named disqualifying pattern at the field definition site; C-02 PASS
  alone does not close generic evidence.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two output cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication named as second
  disqualifying pattern at the field definition site; cross-type anchor alone leaves
  intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression at the scoring site.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline at the
  calculation site; C-03 PASS does not require inline inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table with single merged "Specificity" column for
  both Q1-TypeLevel and Q2-IntraRun questions.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns; C-29 PASS does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: Ties broken differently across runs with no inscribed protocol.
  Closing mechanism: C-41 requires the tie-break protocol with named secondary and
  tertiary dimensions inscribed at the leaderboard definition site; C-04 PASS does
  not require an inscribed protocol.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER entry condition lists only [ANALYST COMPLETE] as its gate;
  no dedicated SPECIFICITY AUDITOR role gate token exists; a reader cannot detect from
  the VERIFIER header alone whether a dedicated independent audit completed.
  Closing mechanism: C-42 requires a named SPECIFICITY AUDITOR role with its own gate
  token ([SPECIFICITY AUDIT COMPLETE]); the VERIFIER entry condition must quote this
  gate verbatim with an explicit exclusion clause ([ANALYST COMPLETE] alone does not
  satisfy this gate); the named-gate citation makes the dedicated audit independently
  verifiable from the VERIFIER header.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no
  consolidated manifest; VERIFIER per-cell entries reference "per SPECIFICITY AUDITOR"
  generically; SYNTHESIS re-reads SA blocks to retrieve Q1/Q2 results.
  Closing mechanism: C-43 requires three conditions at the definition site --
    Req 1: SPECIFICITY AUDITOR produces a named SPECIFICITY AUDIT MANIFEST table
      keyed by (Output, Criterion) as its terminal artifact;
    Req 2: VERIFIER per-cell schema references Q1/Q2 results by manifest key rather
      than re-reading SPECIFICITY AUDITOR per-output blocks;
    Req 3: SYNTHESIS is explicitly prohibited from re-reading SPECIFICITY AUDITOR
      blocks (unconditional; structurally parallel to the ANALYST re-read prohibition
      in C-16);
  C-42 PASS leaves the dispersed-reread path open; C-43 closes it via Req 1 + Req 2 +
  Req 3 simultaneously; a SPECIFICITY AUDITOR satisfying Req 1 and Req 2 but not Req 3
  is C-43 PARTIAL ("req 3 not met").

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but not
  [SPECIFICITY AUDIT COMPLETE] alone; the reverse bypass path is unaddressed.
  Closing mechanism: C-44 requires two conditions at the definition site --
    Req 1: VERIFIER entry condition excludes [ANALYST COMPLETE] alone (closes the
      forward bypass path; already required by C-42);
    Req 2: VERIFIER entry condition also excludes [SPECIFICITY AUDIT COMPLETE] alone
      (closes the reverse bypass path that C-42 PASS leaves open);
  C-42 satisfies Req 1 only; C-44 requires Req 1 + Req 2 simultaneously; a VERIFIER
  entry condition satisfying only Req 1 is C-44 PARTIAL ("req 2 not met").

Failure Mode I -- Prose-only multi-component pass conditions
  Typical output: PARTIAL verdict on C-43 cites "manifest exists but VERIFIER does not
  reference by key" (description by effect); the scorer cannot write "req 2 not met" as
  a structural citation because requirement numbers were not inscribed at the definition
  site; the requirement must be described from context, not cited by label.
  Closing mechanism: C-45 requires multi-component pass conditions (N >= 2 requirements)
  to enumerate each requirement with an explicit "Req N:" label at the definition site;
  C-43 PASS and C-44 PASS do not require numbered labels; C-45 closes the description-
  only PARTIAL path that prose-only requirement lists leave open; a definition site using
  prose-only requirements satisfies C-43 PASS but not C-45; after C-45 enumeration, a
  C-43 PARTIAL verdict can cite "req 2 not met" as a structural reference to the labeled
  entry, not a paraphrase.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                                                    | Produces                      | Domain (ONLY)                                                                                                       | Cannot Check                                                     |
|---------------------|-----------------------------------------------------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                                                 | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                        | Scoring verdicts; format compliance; content quality             |
| ANALYST             | [JUDGE STANDARD COMPLETE]                                                   | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                                     | Evidence standards (Judge); format auditing (Verifier)           |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                                          | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                              | Re-scoring; re-auditing                                          |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                                          | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                         | Format presence (Verifier); scoring (Analyst)                    |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]                         | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows                       | Q1/Q2 content (SA); evidence standards (Judge)                   |
| CONFIRMER           | [VERIFIER COMPLETE]                                                         | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                                | Format presence (Verifier); scoring (Analyst)                    |
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
as the terminal artifact of the SPECIFICITY AUDITOR role. The three conditions
for the manifest to satisfy C-43 are:

  Req 1 (manifest as named terminal artifact): produce a SPECIFICITY AUDIT MANIFEST
    table keyed by (Output, Criterion) with columns for Q1-TypeLevel result,
    Q2-IntraRun result, and Final action; the manifest is the terminal artifact of
    this role, not embedded inline per-output block.

  Req 2 (VERIFIER key reference): the VERIFIER must reference manifest rows by
    (Output, Criterion) key rather than re-reading SPECIFICITY AUDITOR per-output
    blocks; per-cell VERIFIER entries carry "per manifest row [output/C-NN]" notation;
    re-reading SA body blocks is a format violation detectable at the VERIFIER header.

  Req 3 (SYNTHESIS re-read prohibition): SYNTHESIS is prohibited from re-reading
    SPECIFICITY AUDITOR blocks; this prohibition is structurally parallel to the
    prohibition on re-reading ANALYST blocks during regression analysis and is
    equally unconditional; a SYNTHESIS that re-reads SA blocks to resolve Q1/Q2
    is a structural violation even if all manifest rows are present.

A SPECIFICITY AUDITOR satisfying Req 1 and Req 2 but not Req 3 yields C-43 PARTIAL
("req 3 not met"). All three requirements must be simultaneously present for C-43 PASS.

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

## V-02 -- Axis ENUM-C43: C-43 definition sites enumerated, C-44 site prose (C-45 PARTIAL probe)

**Variation axis**: Numbered-requirement enumeration at C-43 definition sites only. Failure Mode G's
C-43 closing mechanism enumerates three requirements with Req 1/2/3 labels. ROLE 3 SPECIFICITY AUDIT
MANIFEST conditions enumerate three requirements with Req 1/2/3 labels. Failure Mode H's C-44 closing
mechanism remains prose-only (two requirements described without numbered labels). Tests whether
C-43 complete enumeration without C-44 enumeration satisfies C-45 or yields PARTIAL. Full V-01 R17
base: SPECIFICITY AUDIT MANIFEST, symmetric conjunction gate, CHANGE MANIFEST, CONFIRMER, three-way
SYNTHESIS gate. 32-row register, YES-only gate, formula /25.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-45 PARTIAL: C-43 definition sites (FM G + ROLE 3) have numbered labels; C-44 definition site (FM H) remains prose. A scorer giving C-43 PARTIAL can cite "req 2 not met" by label. A scorer giving C-44 PARTIAL must describe by effect ("only the forward exclusion clause is present"). Not all multi-component pass conditions have enumeration -- C-45 PARTIAL. C-43 PASS: carried. C-44 PASS: carried (symmetric gate present). | C-37/C-38 (baseline PRIOR ROUND LOAD) PASS: carried. All 37 prior aspirationals carried. | V-04 combines FM G + FM H without ROLE 3 to separate the FM-layer contribution from the ROLE 3-layer contribution. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                          |
|-----------|---------------------------------------------------------------------------------|
| V-01 R17  | (none -- ceiling achieved, all 37 prior aspirationals PASS; C-45 new)          |
| V-02 R17  | C-43 PASS; C-44 PARTIAL; C-45 new                                              |
| V-03 R17  | C-43 FAIL; C-44 PASS; C-45 new                                                 |
| V-04 R17  | C-43 PARTIAL (req 3 not met); C-44 PASS; C-45 new                              |
| V-05 R17  | C-43 PARTIAL (req 2 not met); C-44 PASS; C-45 new                              |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying pattern
  at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two output cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication named as second disqualifying
  pattern at field definition site; cross-type anchor alone leaves intra-run duplication
  undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression at the scoring site.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline; C-03 PASS
  does not require inline inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table with single merged "Specificity" column.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally separated
  labeled columns; C-29 PASS does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: Ties broken differently across runs with no inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol with named secondary and tertiary
  dimensions inscribed at leaderboard definition site; C-04 PASS does not require this.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER lists only [ANALYST COMPLETE] as its gate.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR role with its own gate token
  ([SPECIFICITY AUDIT COMPLETE]) quoted verbatim in VERIFIER entry condition.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no manifest;
  VERIFIER references "per SPECIFICITY AUDITOR" generically.
  Closing mechanism: C-43 requires three conditions at the definition site --
    Req 1: SPECIFICITY AUDITOR produces a named SPECIFICITY AUDIT MANIFEST table
      keyed by (Output, Criterion) as its terminal artifact;
    Req 2: VERIFIER per-cell schema references Q1/Q2 results by manifest key rather
      than re-reading SPECIFICITY AUDITOR per-output blocks;
    Req 3: SYNTHESIS is explicitly prohibited from re-reading SPECIFICITY AUDITOR
      blocks (unconditional);
  C-42 PASS leaves dispersed-reread path open; C-43 closes it via Req 1 + Req 2 +
  Req 3 simultaneously; a design satisfying Req 1 and Req 2 but not Req 3 is C-43
  PARTIAL ("req 3 not met").

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but not
  [SPECIFICITY AUDIT COMPLETE] alone; the reverse bypass path is unaddressed.
  Closing mechanism: C-44 requires the VERIFIER entry condition to additionally exclude
  [SPECIFICITY AUDIT COMPLETE] alone, making neither token independently sufficient;
  C-42 closes only the forward bypass path; C-44 closes the reverse bypass path that
  C-42 PASS leaves open.

Failure Mode I -- Prose-only multi-component pass conditions
  Typical output: PARTIAL verdict on C-43 cites "manifest exists but VERIFIER does not
  reference by key" (description by effect); scorer cannot cite "req 2 not met."
  Closing mechanism: C-45 requires multi-component pass conditions (N >= 2 requirements)
  to enumerate each requirement with an explicit "Req N:" label at the definition site;
  C-43 PASS and C-44 PASS do not require numbered labels; C-45 closes the description-
  only PARTIAL path; a definition site using prose-only requirements satisfies C-43 PASS
  but not C-45.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                                                    | Produces                      | Domain (ONLY)                                                                                                       | Cannot Check                                                     |
|---------------------|-----------------------------------------------------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                                                 | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                                                        | Scoring verdicts; format compliance; content quality             |
| ANALYST             | [JUDGE STANDARD COMPLETE]                                                   | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols                                                     | Evidence standards (Judge); format auditing (Verifier)           |
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                                          | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest table                                                              | Re-scoring; re-auditing                                          |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                                          | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST production; revision flagging                         | Format presence (Verifier); scoring (Analyst)                    |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]                         | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (via manifest keyed lookup); Audit B on PARTIAL rows                       | Q1/Q2 content (SA); evidence standards (Judge)                   |
| CONFIRMER           | [VERIFIER COMPLETE]                                                         | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?                                                | Format presence (Verifier); scoring (Analyst)                    |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] | (terminal output)          | Leaderboard; excellence signals; failure patterns; regression signals                                               | Re-reading ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table |

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
    does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.
---
ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32, produce a Judge standard entry:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase; from [Output-N]:
               prefix annotation required on every ACCEPTABLE entry]"
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
    Primary differentiator (required): [structural feature explaining score difference]
    Primary miss (required): [criterion or mechanism most clearly absent]
    Verdict spread (required): [where output concentrated its points and why]

PROHIBITED CONTENT CATEGORIES (no cell, annotation, or narrative field may
contain any item in this list):

  A. Evaluative prose -- quality assessment without naming a structural element
     Route: rewrite as structural observation with named mechanism
  B. Criterion restatement -- rephrases criterion label as evidence
     Route: rewrite using a structural feature observable in the output
  C. Cross-output generic text -- same sentence could appear in another output
     Route: flag for Specificity Auditor Q2-IntraRun review; rewrite with specific detail
  D. Narrative analysis in scoring cells -- mechanism interpretation or narrative prose
     Route: defer to per-output narrative section; keep scoring cells factual
  E. Novel field labels -- any label not in the permitted set above
     Route: prohibited; *Note*, *Comment*, *Observation*, or any unlisted label is a
     structural violation regardless of content

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

If no CHANGE annotations: "No changes from prior round detected."

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

Domain: Q1-TypeLevel and Q2-IntraRun specificity review of every evidence cell;
ANCHOR REVIEW BLOCK application; SPECIFICITY AUDIT MANIFEST production;
revision flagging (see manifest).
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type -- i.e., would this evidence be equally valid for a correct implementation
    that is not this specific output?"

  Q2 (Intra-run): "Does this evidence fit another output in this run -- i.e.,
    could the same description appear in a different output's cell for this same
    criterion without modification?"

For every evidence cell across all N outputs:

  Output: [output identifier] -- SPECIFICITY AUDITOR pass

  | ID   | Evidence excerpt (first 15 words)  | Q1-TypeLevel | Q2-IntraRun | Action          |
  |------|------------------------------------|--------------|-------------|-----------------|
  | C-01 | [excerpt]                          | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

SPECIFICITY AUDIT MANIFEST

After all evidence cells are reviewed, produce this manifest as the terminal artifact.
The three conditions for the manifest to satisfy C-43 are:

  Req 1 (manifest as named terminal artifact): produce a SPECIFICITY AUDIT MANIFEST
    table keyed by (Output, Criterion) with Q1-TypeLevel, Q2-IntraRun, and Final
    action columns; the manifest is the terminal artifact of this role.

  Req 2 (VERIFIER key reference): the VERIFIER must reference manifest rows by
    (Output, Criterion) key; per-cell VERIFIER entries carry "per manifest row
    [output/C-NN]" notation; re-reading SA body blocks is a format violation.

  Req 3 (SYNTHESIS re-read prohibition): SYNTHESIS is prohibited from re-reading
    SPECIFICITY AUDITOR blocks; this prohibition is unconditional; a SYNTHESIS that
    re-reads SA blocks to resolve Q1/Q2 is a structural violation even if manifest
    rows are present.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

Domain: Format presence -- Q1/Q2 columns non-empty per cell (via manifest keyed
lookup); Audit B on PARTIAL rows (see manifest).
Do not begin until BOTH [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear
above. [ANALYST COMPLETE] alone does not satisfy this gate. [SPECIFICITY AUDIT
COMPLETE] alone does not satisfy this gate. Both tokens are required.

  Output: [output identifier] -- VERIFIER Column Format Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)             | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|-----------------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per manifest row [output/C-01]   | PRESENT / ABSENT | PRESENT / ABSENT | n/a     | ACCEPTED |

For every REJECTED row:
  FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PRESENT/ABSENT]
    Q2-IntraRun:  [PRESENT/ABSENT]
    Audit B:      [PRESENT/MISSING/n/a]

When all rows ACCEPTED across all N outputs:
[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

Domain: Content quality -- do Present/Absent cells name specific structural properties?
Do not begin until [VERIFIER COMPLETE] appears above.

For each PARTIAL verdict across all outputs:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status               |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|----------------------|

  Specificity test: YES -- names specific structural element, mechanism, role, gate
  token, or design gap. NO -- criterion label, generic phrase, or verdict restatement.

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[excerpt]" -- [reason]
    Absent:  "[excerpt]" -- [reason]

When all PARTIAL diagnostics CONFIRMED:
[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two tokens
does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite score descending
  Secondary: essential_pass count descending
  Tertiary: recommended_pass count descending
  If tied after tertiary: note explicitly; no further inference applied

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
If no outlier: "No excellence signals in this round."

FAILURE PATTERNS
If none: "No failure patterns in this round."

REGRESSION SIGNALS
Draw exclusively from [CHANGE MANIFEST COMPLETE]. Do not re-read ANALYST blocks,
SPECIFICITY AUDITOR blocks, or baseline table. These prohibitions are unconditional.
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- all outputs ranked; tie-break protocol applied per definition above
[ ] EXCELLENCE SIGNALS -- section complete or "no signals" stated explicitly
[ ] FAILURE PATTERNS -- all-fail criteria identified or "none" stated explicitly
[ ] REGRESSION SIGNALS -- drawn from manifest exclusively; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axis ENUM-C44: C-44 definition site enumerated, C-43 sites prose (C-45 PARTIAL probe)

**Variation axis**: Numbered-requirement enumeration at C-44 definition site only. Failure Mode H's
C-44 closing mechanism enumerates two requirements with Req 1/2 labels. Failure Mode G (C-43)
and ROLE 3 SPECIFICITY AUDIT MANIFEST conditions remain prose-only. Tests the opposite partial-site
path from V-02: C-43 is the more complex criterion (3 requirements); if its sites remain prose while
C-44 is enumerated, the PARTIAL is more severe (C-43 PARTIAL verdicts cannot cite by number).
Full V-01 R17 base: SPECIFICITY AUDIT MANIFEST, symmetric conjunction gate, CHANGE MANIFEST,
CONFIRMER, three-way SYNTHESIS gate. 32-row register, YES-only gate, formula /25.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-45 PARTIAL: C-44 site (FM H) has Req 1/2 labels; C-43 sites (FM G + ROLE 3) remain prose. C-44 PARTIAL verdicts can cite by number. C-43 PARTIAL verdicts must describe by effect. Not all multi-component pass conditions enumerated -- C-45 PARTIAL. C-43 PASS: carried. C-44 PASS: carried. | Probe for asymmetry: V-02 enumerates the 3-requirement criterion; V-03 enumerates the 2-requirement criterion. If C-45 PARTIAL verdict costs differ, the larger criterion's unenumerated status is the larger gap. | V-04 combines FM G + FM H without ROLE 3 to isolate the ROLE 3-layer contribution. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                          |
|-----------|---------------------------------------------------------------------------------|
| V-01 R17  | (none -- ceiling achieved, all 37 prior aspirationals PASS; C-45 new)          |
| V-02 R17  | C-43 PASS; C-44 PARTIAL; C-45 new                                              |
| V-03 R17  | C-43 FAIL; C-44 PASS; C-45 new                                                 |
| V-04 R17  | C-43 PARTIAL (req 3 not met); C-44 PASS; C-45 new                              |
| V-05 R17  | C-43 PARTIAL (req 2 not met); C-44 PASS; C-45 new                              |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying pattern
  at evidence field definition site; C-02 PASS alone does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two output cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication named as second disqualifying
  pattern; cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline.

Failure Mode D -- Combined specificity field
  Typical output: Single merged "Specificity" column for Q1 and Q2.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as separated labeled columns.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: Ties broken differently across runs with no inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol inscribed at leaderboard definition site.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER lists only [ANALYST COMPLETE] as its gate.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR role with gate token quoted
  verbatim in VERIFIER entry condition with explicit exclusion clause.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no manifest;
  VERIFIER references "per SPECIFICITY AUDITOR" generically.
  Closing mechanism: C-43 requires the SPECIFICITY AUDITOR to produce a named SPECIFICITY
  AUDIT MANIFEST table keyed by (Output, Criterion); the VERIFIER references Q1/Q2 results
  by manifest key rather than re-reading SA blocks; SYNTHESIS is explicitly prohibited from
  re-reading SPECIFICITY AUDITOR blocks; C-42 PASS leaves the dispersed-reread path open;
  C-43 closes it via the keyed-manifest terminal artifact.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but not
  [SPECIFICITY AUDIT COMPLETE] alone.
  Closing mechanism: C-44 requires two conditions at the definition site --
    Req 1: VERIFIER entry condition excludes [ANALYST COMPLETE] alone (closes forward
      bypass path; already required by C-42);
    Req 2: VERIFIER entry condition also excludes [SPECIFICITY AUDIT COMPLETE] alone
      (closes reverse bypass path that C-42 PASS leaves open);
  C-44 requires Req 1 + Req 2 simultaneously; satisfying only Req 1 is C-44 PARTIAL
  ("req 2 not met").

Failure Mode I -- Prose-only multi-component pass conditions
  Typical output: PARTIAL verdict cites requirement by effect rather than by label number.
  Closing mechanism: C-45 requires multi-component pass conditions (N >= 2) to enumerate
  each requirement with an explicit "Req N:" label at the definition site; C-43 PASS and
  C-44 PASS do not require numbered labels; C-45 closes the description-only PARTIAL path.
---
ROLE DEPENDENCY MANIFEST

| Role                | Requires                                                                    | Produces                      | Domain (ONLY)                                                                | Cannot Check                                          |
|---------------------|-----------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------|
| JUDGE               | [PRIOR ROUND LOAD COMPLETE]                                                 | [JUDGE STANDARD COMPLETE]     | ACCEPTABLE/UNACCEPTABLE pairs; separating property; REGISTER                 | Scoring verdicts; format compliance; content quality  |
| ANALYST             | [JUDGE STANDARD COMPLETE]                                                   | [ANALYST COMPLETE]            | Scoring; evidence; composite; golden; *Why*; *Change*; P/A cols              | Evidence standards (Judge); format auditing (Verifier)|
| CHANGE MANIFEST     | [ANALYST COMPLETE]                                                          | [CHANGE MANIFEST COMPLETE]    | Sweep *Change*: CHANGE annotations into manifest                             | Re-scoring; re-auditing                               |
| SPECIFICITY AUDITOR | [ANALYST COMPLETE]                                                          | [SPECIFICITY AUDIT COMPLETE]  | Q1/Q2 review; ANCHOR REVIEW BLOCK; SPECIFICITY AUDIT MANIFEST; revision flag | Format presence (Verifier); scoring (Analyst)         |
| VERIFIER            | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]                         | [VERIFIER COMPLETE]           | Format presence: Q1/Q2 columns non-empty (manifest keyed lookup); Audit B    | Q1/Q2 content (SA); evidence standards (Judge)        |
| CONFIRMER           | [VERIFIER COMPLETE]                                                         | [CONFIRMATION COMPLETE]       | Content quality: do Present/Absent cells name structural properties?          | Format presence (Verifier); scoring (Analyst)         |
| SYNTHESIS           | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] | (terminal output)          | Leaderboard; excellence signals; failure patterns; regression signals         | Re-reading ANALYST/SA blocks or baseline table        |

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
    does not satisfy this gate.
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
  | C-01 through C-32 rows (same structure as V-01) |

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

[Identical to V-02 ANALYST section -- same schema, same formula /25, same PROHIBITED CONTENT
CATEGORIES with "No prohibited content category lacks a named destination" terminal assertion]

[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

[Identical to V-01 CHANGE MANIFEST -- sweep CHANGE annotations, SYNTHESIS re-read prohibition]

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

[Identical to V-01 R17 SPECIFICITY AUDITOR -- ANCHOR REVIEW BLOCK, per-output Q1/Q2 review]

SPECIFICITY AUDIT MANIFEST

After all evidence cells are reviewed, produce this manifest as the terminal artifact of
the SPECIFICITY AUDITOR role. This manifest is the authoritative Q1/Q2 source for the
VERIFIER. The VERIFIER must reference manifest rows by (Output, Criterion) key; it must
not re-read SPECIFICITY AUDITOR per-output blocks. SYNTHESIS is prohibited from re-reading
SPECIFICITY AUDITOR blocks; this prohibition is structurally parallel to the prohibition
on re-reading ANALYST blocks during regression analysis and is equally unconditional.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

[Identical to V-01 VERIFIER -- keyed manifest lookup, Audit B, BOTH gate with two exclusion clauses]

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

[Identical to V-01 CONFIRMER]

[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two tokens
does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite score descending
  Secondary: essential_pass count descending
  Tertiary: recommended_pass count descending
  If tied after tertiary: note explicitly

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
FAILURE PATTERNS
REGRESSION SIGNALS -- draw exclusively from [CHANGE MANIFEST COMPLETE]; do not re-read
ANALYST blocks, SPECIFICITY AUDITOR blocks, or baseline table.

Pre-close checklist:
[ ] LEADERBOARD
[ ] EXCELLENCE SIGNALS
[ ] FAILURE PATTERNS
[ ] REGRESSION SIGNALS

[SYNTHESIS COMPLETE]
```

---

## V-04 -- Axes ENUM-FM: Failure Mode G + H enumerated, ROLE 3 prose (C-45 PARTIAL probe)

**Variation axis**: Numbered-requirement enumeration at Failure Mode layer only. FM G enumerates
C-43's three requirements with Req 1/2/3 labels. FM H enumerates C-44's two requirements with
Req 1/2 labels. ROLE 3 SPECIFICITY AUDIT MANIFEST conditions remain prose-only (three requirements
stated without numbered labels). Tests whether the Failure Mode layer (both FM G and FM H enumerated)
is sufficient for C-45 PASS, or whether ROLE 3 is an independent required definition site. Full V-01
R17 base. 32-row register, YES-only gate, formula /25.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-45 PARTIAL: FM G and FM H both have numbered labels; ROLE 3 manifest conditions remain prose. The Failure Mode layer provides one enumerated definition site for each multi-component pass condition; ROLE 3 is a second definition site for C-43. If C-45 requires ALL definition sites to be enumerated, ROLE 3's prose form makes this PARTIAL. If C-45 requires at least one enumerated site per multi-component pass condition, this could be PASS. | The ROLE 3 site is a structural definition site because it prescribes the artifact the role must produce -- not merely describes what the artifact avoids. FM G describes the failure mode; ROLE 3 prescribes the requirement. The two sites are complementary, not redundant. | V-01 combines FM + ROLE 3 enumeration to confirm the ceiling requires both layers. The PARTIAL gap between V-04 and V-01 isolates the ROLE 3 site contribution. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                          |
|-----------|---------------------------------------------------------------------------------|
| V-01 R17  | (none -- ceiling achieved, all 37 prior aspirationals PASS; C-45 new)          |
| V-02 R17  | C-43 PASS; C-44 PARTIAL; C-45 new                                              |
| V-03 R17  | C-43 FAIL; C-44 PASS; C-45 new                                                 |
| V-04 R17  | C-43 PARTIAL (req 3 not met); C-44 PASS; C-45 new                              |
| V-05 R17  | C-43 PARTIAL (req 2 not met); C-44 PASS; C-45 new                              |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A through E: [identical to V-01 Failure Modes A-E]

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER lists only [ANALYST COMPLETE] as its gate.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR role with gate token quoted
  verbatim in VERIFIER entry condition with explicit exclusion clause.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no manifest.
  Closing mechanism: C-43 requires three conditions at the definition site --
    Req 1: SPECIFICITY AUDITOR produces a named SPECIFICITY AUDIT MANIFEST table
      keyed by (Output, Criterion) as its terminal artifact;
    Req 2: VERIFIER per-cell schema references Q1/Q2 results by manifest key rather
      than re-reading SPECIFICITY AUDITOR per-output blocks;
    Req 3: SYNTHESIS is explicitly prohibited from re-reading SPECIFICITY AUDITOR
      blocks (unconditional);
  A design satisfying Req 1 and Req 2 but not Req 3 is C-43 PARTIAL ("req 3 not met").

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but not
  [SPECIFICITY AUDIT COMPLETE] alone.
  Closing mechanism: C-44 requires two conditions at the definition site --
    Req 1: VERIFIER entry condition excludes [ANALYST COMPLETE] alone;
    Req 2: VERIFIER entry condition also excludes [SPECIFICITY AUDIT COMPLETE] alone;
  Satisfying only Req 1 is C-44 PARTIAL ("req 2 not met").

Failure Mode I -- Prose-only multi-component pass conditions
  Typical output: PARTIAL verdict cites requirement by effect rather than by label number.
  Closing mechanism: C-45 requires multi-component pass conditions (N >= 2) to enumerate
  each requirement with an explicit "Req N:" label at the definition site; C-43 PASS and
  C-44 PASS do not require numbered labels; C-45 closes the description-only PARTIAL path.
---
ROLE DEPENDENCY MANIFEST

[Identical to V-01 ROLE DEPENDENCY MANIFEST]

Gate rules: [Identical to V-01 gate rules]
---
ROLE 1: JUDGE

[Identical to V-01 ROLE 1 -- C-01 through C-32 register, 32 rows, YES-only gate]

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

[Identical to V-01 ANALYST -- same schema, formula /25, PROHIBITED CONTENT CATEGORIES]

[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

[Identical to V-01 CHANGE MANIFEST]

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

[ANCHOR REVIEW BLOCK identical to V-01]

SPECIFICITY AUDIT MANIFEST

After all evidence cells are reviewed, produce this manifest as the terminal artifact of
the SPECIFICITY AUDITOR role. This manifest is the authoritative Q1/Q2 source for the
VERIFIER. The VERIFIER must reference manifest rows by (Output, Criterion) key; it must
not re-read SPECIFICITY AUDITOR per-output blocks. SYNTHESIS is prohibited from re-reading
SPECIFICITY AUDITOR blocks; this prohibition is unconditional and structurally parallel to
the ANALYST re-read prohibition.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

[Identical to V-01 VERIFIER -- keyed manifest lookup, BOTH gate with two explicit exclusion clauses]

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

[Identical to V-01 CONFIRMER]

[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two tokens
does not satisfy this gate.

[Standard LEADERBOARD / EXCELLENCE SIGNALS / FAILURE PATTERNS / REGRESSION SIGNALS
sections with tie-break protocol inscribed and pre-close checklist as in V-01]

[SYNTHESIS COMPLETE]
```

---

## V-05 -- Axis INLINE-NUM: Inline numeric ordering without "Req N:" labels (C-45 PARTIAL probe)

**Variation axis**: Phrasing register -- all multi-component pass condition definition sites use
inline "(1) / (2) / (3)" numeric ordering within continuous prose sentences rather than dedicated
"Req N:" label lines. FM G describes C-43's three conditions as "(1) ... (2) ... (3) ...". FM H
describes C-44's two conditions as "(1) ... (2) ...". ROLE 3 manifest uses matching "(1)/(2)/(3)"
inline. Tests whether inline numbering satisfies C-45's "explicit label at definition site"
requirement, or whether C-45 requires dedicated "Req N:" label lines that are structurally
separable from prose. Full V-01 R17 base. 32-row register, YES-only gate, formula /25.

**Hypothesis**:

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-45 PARTIAL: inline "(1)/(2)/(3)" provides ordering information but a PARTIAL verdict citing "req 2 not met" cannot point to a structurally distinct labeled entry -- "(2)" is an inline sequence marker within a prose sentence, not a citable structural label. The distinction between C-45 PASS (dedicated "Req N:" labels) and C-45 PARTIAL (inline numbering) mirrors the C-35 PASS (structurally separated Q1/Q2 columns) vs C-29 PASS (both questions stated in prose) separation. | C-43 PASS: carried. C-44 PASS: carried. All 37 prior aspirationals carried. Inline numbering is a phrasing register test: the content is correct but the structural form is degraded. | V-01 contrasts V-05: both have all required content; V-01 uses "Req N:" dedicated labels; V-05 uses inline "(N)" markers. The C-45 PASS/PARTIAL boundary is the structural-separation axis. |

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---
PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round                                          |
|-----------|---------------------------------------------------------------------------------|
| V-01 R17  | (none -- ceiling achieved, all 37 prior aspirationals PASS; C-45 new)          |
| V-02 R17  | C-43 PASS; C-44 PARTIAL; C-45 new                                              |
| V-03 R17  | C-43 FAIL; C-44 PASS; C-45 new                                                 |
| V-04 R17  | C-43 PARTIAL (req 3 not met); C-44 PASS; C-45 new                              |
| V-05 R17  | C-43 PARTIAL (req 2 not met); C-44 PASS; C-45 new                              |

[PRIOR ROUND LOAD COMPLETE]
---
ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required structure."
  Closing mechanism: C-40 requires cross-type genericity as named disqualifying pattern
  at evidence field definition site.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence sentence in two output cells for the same criterion.
  Closing mechanism: C-40 requires cross-output duplication as second named disqualifying
  pattern at field definition site.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score "87.3" with no formula expression.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline.

Failure Mode D -- Combined specificity field
  Typical output: Single merged "Specificity" column for Q1 and Q2.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as separated labeled columns.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: Ties broken ad hoc with no inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol inscribed at leaderboard definition site.

Failure Mode F -- Header-silent Q1/Q2 audit
  Typical output: VERIFIER lists only [ANALYST COMPLETE] as its gate.
  Closing mechanism: C-42 requires named SPECIFICITY AUDITOR gate quoted verbatim in
  VERIFIER entry condition with explicit exclusion clause.

Failure Mode G -- Dispersed SA body reread
  Typical output: SPECIFICITY AUDITOR produces per-output Q1/Q2 blocks but no manifest.
  Closing mechanism: C-43 requires three conditions at the definition site: (1) SPECIFICITY
  AUDITOR produces a named SPECIFICITY AUDIT MANIFEST table keyed by (Output, Criterion) as
  its terminal artifact; (2) VERIFIER per-cell schema references Q1/Q2 results by manifest
  key rather than re-reading SPECIFICITY AUDITOR per-output blocks; (3) SYNTHESIS is
  explicitly prohibited from re-reading SPECIFICITY AUDITOR blocks (unconditional); a design
  satisfying (1) and (2) but not (3) is C-43 PARTIAL.

Failure Mode H -- Reverse bypass path (asymmetric gate)
  Typical output: VERIFIER entry condition excludes [ANALYST COMPLETE] alone but not
  [SPECIFICITY AUDIT COMPLETE] alone.
  Closing mechanism: C-44 requires two conditions at the definition site: (1) VERIFIER
  entry condition excludes [ANALYST COMPLETE] alone (closes forward bypass path); (2)
  VERIFIER entry condition also excludes [SPECIFICITY AUDIT COMPLETE] alone (closes
  reverse bypass path); satisfying only (1) is C-44 PARTIAL.

Failure Mode I -- Prose-only multi-component pass conditions
  Typical output: PARTIAL verdict cites requirement by effect rather than by label number.
  Closing mechanism: C-45 requires multi-component pass conditions (N >= 2) to enumerate
  each requirement with an explicit "Req N:" label at the definition site; C-43 PASS and
  C-44 PASS do not require numbered labels; C-45 closes the description-only PARTIAL path;
  inline "(1)/(2)/(3)" ordering within prose satisfies enumeration in content but not as a
  structurally citable label form -- a scorer citing "req 2 not met" cannot point to a
  structurally distinct labeled entry when the number is embedded in a prose sentence.
---
ROLE DEPENDENCY MANIFEST

[Identical to V-01 ROLE DEPENDENCY MANIFEST]

Gate rules: [Identical to V-01 gate rules]
---
ROLE 1: JUDGE

[Identical to V-01 ROLE 1 -- C-01 through C-32 register, 32 rows, YES-only gate]

[JUDGE STANDARD COMPLETE]
---
ROLE 2: ANALYST

[Identical to V-01 ANALYST -- same schema, formula /25, PROHIBITED CONTENT CATEGORIES]

[ANALYST COMPLETE] -- [N] outputs scored
---
CHANGE MANIFEST

[Identical to V-01 CHANGE MANIFEST]

[CHANGE MANIFEST COMPLETE]
---
ROLE 3: SPECIFICITY AUDITOR

[ANCHOR REVIEW BLOCK identical to V-01]

SPECIFICITY AUDIT MANIFEST

After all evidence cells are reviewed, produce this manifest as the terminal artifact.
The three conditions for the manifest to satisfy C-43 are: (1) SPECIFICITY AUDIT MANIFEST
table keyed by (Output, Criterion) as terminal artifact with Q1-TypeLevel, Q2-IntraRun, and
Final action columns; (2) VERIFIER must reference manifest rows by key, carrying "per manifest
row [output/C-NN]" notation in per-cell entries; (3) SYNTHESIS prohibited from re-reading
SPECIFICITY AUDITOR blocks, unconditionally. A design satisfying (1) and (2) but not (3)
yields C-43 PARTIAL.

  SPECIFICITY AUDIT MANIFEST

  | Output | Criterion | Q1-TypeLevel | Q2-IntraRun | Final action    |
  |--------|-----------|--------------|-------------|-----------------|
  | [ID]   | C-[NN]    | PASS / FAIL  | PASS / FAIL | ACCEPT / REVISE |

[SPECIFICITY AUDIT COMPLETE]
---
ROLE 4: VERIFIER

[Identical to V-01 VERIFIER -- keyed manifest lookup, BOTH gate with two explicit exclusion clauses]

[VERIFIER COMPLETE]
---
ROLE 5: CONFIRMER

[Identical to V-01 CONFIRMER]

[CONFIRMATION COMPLETE]
---
[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two tokens
does not satisfy this gate.

[Standard LEADERBOARD / EXCELLENCE SIGNALS / FAILURE PATTERNS / REGRESSION SIGNALS
sections with tie-break protocol inscribed and pre-close checklist as in V-01]

[SYNTHESIS COMPLETE]
```
