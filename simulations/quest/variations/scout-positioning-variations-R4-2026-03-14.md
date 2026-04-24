Written to `simulations/quest/variations/scout-positioning-variations-R4-2026-03-14.md`.

---

## R4 Variations — Summary

**R4 baseline floor locked in all 5 variations:**
- C-18: PREAMBLE section before SETUP declares MECHANISM 1/2/3 explicitly
- C-19: VERIFY quotes rubric pass conditions verbatim, not paraphrased
- Plus all R3 floor items (17 sections, STOP verb, 5+ dims, dedicated degradation FINDINGS)

**Gap analysis:** R3 V-05 projects to 188/190 on v4 rubric (C-18 and C-19 already satisfied). Remaining 2 points are both content:

| Gap | Root cause | R4 fix |
|-----|-----------|--------|
| C-03 (9/10) | Category derived not proven | Defensibility test table in FINDINGS C-03 -- proposed category tested against each named competitor; ACCEPTED only if all rows NO |
| C-09 (9/10) | Prior run loaded -> N/A | Degradation-path-first rule -- C-09 always populated; when loaded, records quality delta gained (competitor positions confirmed, whitespace grounded, table stakes sourced) |

**Variation axes:**

| V | Axis | Single/Combined | Key mechanism |
|---|------|-----------------|---------------|
| V-01 | Category-proof | Single | Defensibility test table in C-03 |
| V-02 | Degradation-path-first | Single | C-09 always-populated, quality delta when loaded |
| V-03 | Verbatim-preamble | Single | PREAMBLE quotes C-18/C-19 rubric text before declaring mechanisms |
| V-04 | R3-V05 + category-proof + verbatim-preamble | Combined | Closes C-03 gap, isolates C-09 |
| V-05 | Full-stack | Combined | All axes; R4 ceiling attempt |

**Projected scoring:** V-05 targets 190/190. V-04 tests whether C-03 fix alone is sufficient (190 if C-09 N/A path is acceptable; 189 if scorer requires quality delta). V-01 and V-02 are single-axis isolation tests to confirm each content fix independently.
erbatim before declaring mechanisms. The declaration IS the rubric text, not a summary of it. |
| **V-04 -- R3-V05 + category-proof + verbatim-preamble** | Format + preamble register | Incremental upgrade of R3 V-05: adds category defensibility test (C-03 gap) and verbatim-preamble (C-18/C-19 reinforced). Should reach 190. |
| **V-05 -- Full-stack R4** | All axes | Category-proof + degradation-path-first + verbatim-preamble stacked on R3 V-05 foundation. The R4 ceiling attempt. |

---

## V-01: Category-proof (output format axis)

Axis: Output format -- FINDINGS C-03 includes a mandatory per-competitor defensibility test.
The proposed category passes only after explicit confirmation that no named competitor already
owns it. Category claim is proven by elimination, not asserted from intent.

Hypothesis: R3 V-05 scored 9/10 on C-03 because the category was "derived not proven." A
defensibility test -- iterating through each named competitor and confirming they don't own the
proposed category -- produces a provable, falsifiable claim. The rubric requires the category
to be "one Signal can own"; the test operationalizes that requirement.

```
You are running /scout:positioning.

PREAMBLE -- enforcement mechanisms declared before any phase begins:
  MECHANISM 1 (lifecycle ordering): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Each phase
    completes before the next begins. Prevents role contamination and premature output.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17 force
    criterion-complete output. A missing section is the signal a criterion was skipped --
    detectable by counting, no checklist required.
  MECHANISM 3 (pre-artifact VERIFY): explicit PASS/FLAG check against verbatim rubric pass
    conditions after FINDINGS, before artifact emission. Catches failures at production time.

These three mechanisms are independent. Each defends a different failure mode.
Confirm all three in VERIFY.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS C-10 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS C-06 may be missed
  - Category defensibility test (FINDINGS C-03) will run against inline competitors only;
    results are provisional until /scout:competitors is run
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: propose a candidate ownable space. Do not accept it yet -- it will be
      tested in FINDINGS C-03. Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Both required. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation. Framing:
  developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer. SECONDARY (each
    labeled SECONDARY) addresses tool-switching per audience. Explicit labels required.
  - Anti-positioning: 2+ statements. At least one must address inertia:
    "Signal is NOT staying with the current workflow -- [what it costs]."
    All statements name categories a prospect could genuinely confuse Signal with.
    Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Produce exactly 17 sections labeled C-01 through C-17. A missing section signals a
missed criterion -- detectable by counting, no checklist required. Every claim carries
a [Source: ...] annotation.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note emitted in SETUP]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Each includes: (a) positioning statement [Source: ...],
   (b) the 1-2 framing signals distinguishing this statement from the others.]

FINDINGS C-03: CATEGORY DEFINITION
  Proposed category: [candidate ownable space] [Source: ...]

  DEFENSIBILITY TEST -- run for each named competitor:
  | Competitor | Owns this category? | Evidence |
  |------------|---------------------|----------|
  | Inertia    | YES / NO            | [basis]  |
  | [C1]       | YES / NO            | [basis]  |
  | [C2]       | YES / NO            | [basis]  |
  | [C3]       | YES / NO            | [basis]  |

  Verdict: ACCEPTED if all rows NO. REJECTED if any row YES -- propose alternate and re-test.
  Accepted category: [name] [Source: ...]
  Rejected categories tested: [list any that failed, with which competitor owned them, or "none"]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Source: ...]
  Named competitor contrast: [one sentence] [Source: ...]
  [Both in contrast form. Feature lists fail. Both beats required.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT staying with the current workflow -- [what it costs] [Source: ...]
  Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
  [2 minimum; inertia statement required as one]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Source | Gap type |
  |-------|---------|--------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  Rows: Inertia (current workflow, no tool) [FIRST], Signal, [named competitors]
  Columns: [5+ dimensions. Choose from: pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
  Scale: H / M / L
  [Source: loaded artifact [filename] / inline analysis]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- targets inertia buyer] [Source: ...]
  SECONDARY:
    [Audience]: [message -- tool-switching case] [Source: ...]
    [Audience]: [message -- tool-switching case] [Source: ...]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: name specific risks -- which competitor positions and table
   stakes are unverified. "Quality may vary" does not satisfy this criterion.
   Note that the category defensibility test in C-03 ran against inline competitors only;
   name which positions could not be confirmed.]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space -- neither inertia nor any named tool owns it]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and
    no other row -- including inertia -- is H. Falsifiable by column inspection.]
  [Source: matrix FINDINGS C-07, dimensions [X] and [Y]]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections present]
  Sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [before degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. SETUP prose is subject to LLM compression; this
   repetition ensures the note appears in output.]
  [If prior run loaded: N/A -- source: [filename]]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Phase order enforced.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    Missing section detectable by counting.
  MECHANISM 3 (pre-artifact VERIFY): VERIFY block runs after FINDINGS, before emission,
    mapping each section to its verbatim rubric pass condition.
  All three present: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: PASS if "the skill either (a) loads the prior run and names the file, or (b) emits
  an explicit degradation note that names the specific positioning risk before producing
  any output. Silent continuation -- producing positioning output without acknowledging
  missing competitor data -- is an auto-fail regardless of output quality."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND "each
  statement uses audience-appropriate framing -- developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing the same statement for two audiences is a fail."
C-03: PASS if "a category is stated explicitly" AND "the category must NOT be a category
  a named competitor already owns" AND "category framing must be consistent with the
  anti-positioning section." Defensibility test present; all rows NO. Any YES row without
  revised category = auto-FLAG.
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "must draw a contrast with the primary competitor or inertia."
  "A list of five equal bullet points with no hierarchy is a fail. Contrast form is
  required, not preferred." Feature list = auto-FLAG. Missing inertia beat = FLAG.
C-05: PASS if "at least two anti-positioning statements present" AND "grounded in the
  category definition -- items named should be categories a prospect might plausibly
  confuse Signal with. Generic negations ('not a database') do not count."
  Missing inertia statement = FLAG. Generic negations = auto-FLAG.
C-06: PASS if "a reality-check table (or equivalent) covers at least 3 claims with VALID /
  PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked
  PARTIAL must note what is missing and whether the gap is ahead-of-spec or simply
  unsupported." Fewer than 3 rows = auto-FLAG.
C-07: PASS if "matrix covers Signal plus at least one named competitor across at least 3
  dimensions relevant to the product" AND "must be in tabular form." Inertia row present.
C-08: PASS if "output distinguishes a single primary message (works for any audience, top
  of the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled
  explicitly (e.g. PRIMARY / SECONDARY), not inferred from ordering." Flat list = auto-FLAG.
C-09: PASS if prior run missing AND "names the specific risk: e.g. 'primary competitor is
  likely inertia, but without scout:competitors we cannot confirm whitespace or table stakes
  -- differentiation claims are provisional.' Generic 'output may be lower quality' warnings
  do not satisfy this criterion." OR prior run loaded AND N/A stated.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data"
  AND "cites the specific matrix dimensions or competitor positions that support it."
  Missing dimension citation = auto-FLAG. Inertia row tested.
C-11: PASS if "output contains named or numbered FINDINGS sections that correspond to each
  rubric criterion." Count sections C-01 through C-17. Missing section = auto-FLAG.
C-12: PASS if "instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
  CONTINUE) before emitting the degradation note." Conditional language = auto-FLAG.
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from
  both SETUP instructions and positioning output. SETUP-only = auto-FLAG."
C-14: PASS if "whitespace claim names the specific dimensions tested" AND "each cited
  dimension appears as a column in the matrix." Vague citation = auto-FLAG.
C-15: PASS because "a VERIFY step is present in the skill's phase structure (after FINDINGS,
  before emission) that tests each FINDINGS section against its criterion's stated pass
  condition." This VERIFY block is structurally present after FINDINGS.
C-16: PASS if "three distinct enforcement mechanisms are identifiable in the skill structure."
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: PASS if "matrix includes Signal plus at least one named competitor evaluated across at
  least 5 dimensions relevant to the product." Count: [N]. Fewer than 5 = auto-FLAG.

PREAMBLE DECLARATION CHECK (C-18): PASS if "a PREAMBLE or MECHANISMS section appears at
  the top of the skill structure (before SETUP) that names each enforcement mechanism
  explicitly (e.g. 'MECHANISM 1: lifecycle ordering -- prior-run load before FINDINGS;
  MECHANISM 2: claim-traceability -- [Source:] annotation on every claim; MECHANISM 3:
  pre-artifact VERIFY -- pass/fail check before emission'). Mechanisms declared only within
  FINDINGS meta sections (not in a preamble) satisfy C-16 but do not satisfy C-18."
  Confirm PREAMBLE before SETUP names MECHANISM 1, 2, 3. [PASS / FLAG]

VERBATIM-VERIFY CHECK (C-19): PASS if "the VERIFY block quotes each rubric pass condition
  verbatim (or near-verbatim), not in paraphrased or condensed form. A VERIFY that says
  'PASS if prior run loaded OR degradation note emitted' (condensed) does not satisfy this
  criterion -- the rubric pass condition for C-01 specifies 'names the specific positioning
  risk' and 'is an auto-fail regardless of output quality,' both of which disappear in
  condensed form."
  Spot-check C-01: "auto-fail regardless of output quality" present above. [PASS / FLAG]
  [PASS / FLAG]

SOURCE AUDIT: Scan FINDINGS C-01 through C-10. List any claim without [Source: ...].
  For each: add source inline or flag as UNSOURCED.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  category_defensibility: tested
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

## V-02: Degradation-path-first (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- FINDINGS C-09 is always populated. When the prior run is
loaded, it records what specific positioning quality was gained from it (not "N/A"). When
missing, it records specific risks. The N/A path that caps C-09 at 9/10 is eliminated.

Hypothesis: C-09 scored 9/10 in R3 V-05 because "prior run loaded -> N/A" -- the criterion
couldn't demonstrate itself when the prior run existed. If C-09 always records substantive
content (gains confirmed when loaded; risks quantified when missing), the criterion is fully
exercised on every run, not just on the degraded path.

```
You are running /scout:positioning.

PREAMBLE -- enforcement mechanisms declared before any phase begins:
  MECHANISM 1 (lifecycle ordering): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Each phase
    completes before the next begins. Prevents role contamination and premature output.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17 force
    criterion-complete output. A missing section is the signal a criterion was skipped --
    detectable by counting, no checklist required.
  MECHANISM 3 (pre-artifact VERIFY): explicit PASS/FLAG check against verbatim rubric pass
    conditions after FINDINGS, before artifact emission. Catches failures at production time.

These three mechanisms are independent. Each defends a different failure mode.
Confirm all three in VERIFY.

Degradation-path rule: FINDINGS C-09 is always populated. When prior run is loaded,
  record what the run confirmed (competitor positions, table stakes, whitespace dimensions
  that would have been provisional without it). "N/A" is not a valid C-09 entry.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
  Note: FINDINGS C-09 will record what this run confirmed, not N/A.
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS C-10 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS C-06 may be missed
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the ownable space. State the specific rejected category and why
      Signal cannot own it. Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Both required. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation. Framing:
  developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer. SECONDARY (each
    labeled SECONDARY) addresses tool-switching per audience. Explicit labels required.
  - Anti-positioning: 2+ statements. At least one must address inertia:
    "Signal is NOT staying with the current workflow -- [what it costs]."
    All statements name categories a prospect could genuinely confuse Signal with.
    Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Produce exactly 17 sections labeled C-01 through C-17. A missing section signals a
missed criterion -- detectable by counting, no checklist required. Every claim carries
a [Source: ...] annotation.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note emitted in SETUP]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Each includes: (a) positioning statement [Source: ...],
   (b) the 1-2 framing signals distinguishing this statement from the others.]

FINDINGS C-03: CATEGORY DEFINITION
  Category: [ownable category name] [Source: ...]
  Not: [name one rejected category and why Signal cannot own it] [Source: ...]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Source: ...]
  Named competitor contrast: [one sentence] [Source: ...]
  [Both in contrast form. Feature lists fail. Both beats required.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT staying with the current workflow -- [what it costs] [Source: ...]
  Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
  [2 minimum; inertia statement required as one]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Source | Gap type |
  |-------|---------|--------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  Rows: Inertia (current workflow, no tool) [FIRST], Signal, [named competitors]
  Columns: [5+ dimensions. Choose from: pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
  Scale: H / M / L
  [Source: loaded artifact [filename] / inline analysis]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- targets inertia buyer] [Source: ...]
  SECONDARY:
    [Audience]: [message -- tool-switching case] [Source: ...]
    [Audience]: [message -- tool-switching case] [Source: ...]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [ALWAYS POPULATE -- do not write N/A]
  [If prior run missing:]
    Specific risks:
    - Primary competitor unconfirmed; likely inertia but cannot rule out a dominant tool
    - Whitespace provisional: a named tool may occupy the claimed space undetected
    - Table stakes unverified: PARTIAL verdicts in C-06 may undercount spec gaps
    - Differentiation claims labeled [Source: inline] -- treat as provisional until
      /scout:competitors confirms or refutes
  [If prior run loaded:]
    Prior run confirmed -- quality delta from loading:
    - Competitor positions: [which competitors' matrix positions are now source-grounded]
    - Whitespace: [which dimensions were confirmed clear vs would be provisional without run]
    - Table stakes: [which C-06 verdicts changed because of the run, or "none changed"]
    - Claims elevated from [Source: inline] to [Source: artifact]: [list or "none"]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space -- neither inertia nor any named tool owns it]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and
    no other row -- including inertia -- is H. Falsifiable by column inspection.]
  [Source: matrix FINDINGS C-07, dimensions [X] and [Y]]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections present]
  Sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [before degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. SETUP prose is subject to LLM compression; this
   repetition ensures the note appears in output.]
  [If prior run loaded: source-confirmed path -- see FINDINGS C-09 for quality delta]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Phase order enforced.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    Missing section detectable by counting.
  MECHANISM 3 (pre-artifact VERIFY): VERIFY block runs after FINDINGS, before emission,
    mapping each section to its verbatim rubric pass condition.
  All three present: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: PASS if "the skill either (a) loads the prior run and names the file, or (b) emits
  an explicit degradation note that names the specific positioning risk before producing
  any output. Silent continuation -- producing positioning output without acknowledging
  missing competitor data -- is an auto-fail regardless of output quality."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND "each
  statement uses audience-appropriate framing -- developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing the same statement for two audiences is a fail."
C-03: PASS if "a category is stated explicitly" AND "the category must NOT be a category a
  named competitor already owns (e.g. 'AI coding assistant' or 'testing framework')" AND
  "category framing must be consistent with the anti-positioning section."
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "must draw a contrast with the primary competitor or inertia."
  "A list of five equal bullet points with no hierarchy is a fail. Contrast form is
  required, not preferred." Feature list = auto-FLAG.
C-05: PASS if "at least two anti-positioning statements present" AND "grounded in the
  category definition -- items named should be categories a prospect might plausibly
  confuse Signal with. Generic negations ('not a database') do not count."
  Missing inertia statement = FLAG.
C-06: PASS if "a reality-check table (or equivalent) covers at least 3 claims with VALID /
  PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked
  PARTIAL must note what is missing and whether the gap is ahead-of-spec or simply
  unsupported." Fewer than 3 rows = auto-FLAG.
C-07: PASS if "matrix covers Signal plus at least one named competitor across at least 3
  dimensions relevant to the product" AND "must be in tabular form." Inertia row present.
C-08: PASS if "output distinguishes a single primary message (works for any audience, top
  of the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled
  explicitly (e.g. PRIMARY / SECONDARY), not inferred from ordering." Flat list = auto-FLAG.
C-09: PASS if prior run missing AND "names the specific risk: e.g. 'primary competitor is
  likely inertia, but without scout:competitors we cannot confirm whitespace or table stakes
  -- differentiation claims are provisional.' Generic 'output may be lower quality' warnings
  do not satisfy this criterion." OR if prior run loaded AND records "what specific
  positioning quality was gained from it" -- competitor positions confirmed, whitespace
  dimensions grounded, table stakes sourced. Generic N/A = auto-FLAG.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data"
  AND "cites the specific matrix dimensions or competitor positions that support it."
  Missing dimension citation = auto-FLAG. Inertia row tested.
C-11: PASS if "output contains named or numbered FINDINGS sections that correspond to each
  rubric criterion." Count. Missing section = auto-FLAG.
C-12: PASS if "instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
  CONTINUE) before emitting the degradation note." Conditional language = auto-FLAG.
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from
  both SETUP instructions and positioning output. SETUP-only = auto-FLAG."
C-14: PASS if "whitespace claim names the specific dimensions tested" AND "each cited
  dimension appears as a column in the matrix." Vague citation = auto-FLAG.
C-15: PASS because "a VERIFY step is present in the skill's phase structure (after FINDINGS,
  before emission) that tests each FINDINGS section against its criterion's stated pass
  condition." This VERIFY block is structurally present after FINDINGS.
C-16: PASS if "three distinct enforcement mechanisms are identifiable in the skill structure."
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: PASS if "matrix includes Signal plus at least one named competitor evaluated across at
  least 5 dimensions relevant to the product. Dimensions must be distinct and independently
  testable." Count: [N]. Fewer than 5 = auto-FLAG.

PREAMBLE DECLARATION CHECK (C-18): PASS if "a PREAMBLE or MECHANISMS section appears at
  the top of the skill structure (before SETUP) that names each enforcement mechanism
  explicitly." Confirm MECHANISM 1/2/3 named before SETUP. [PASS / FLAG]

VERBATIM-VERIFY CHECK (C-19): PASS if "the VERIFY block quotes each rubric pass condition
  verbatim (or near-verbatim), not in paraphrased or condensed form. A VERIFY that says
  'PASS if prior run loaded OR degradation note emitted' (condensed) does not satisfy this
  criterion -- the rubric pass condition for C-01 specifies 'names the specific positioning
  risk' and 'is an auto-fail regardless of output quality,' both of which disappear in
  condensed form."
  Spot-check C-01: "auto-fail regardless of output quality" present. [PASS / FLAG]
  Spot-check C-09: "Generic 'output may be lower quality' warnings do not satisfy" present.
  [PASS / FLAG]

SOURCE AUDIT: Scan FINDINGS C-01 through C-10. List any claim without [Source: ...].
  For each: add source inline or flag as UNSOURCED.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  degradation_path: always-populated
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

## V-03: Verbatim-preamble (preamble register axis)

Axis: Preamble register -- the PREAMBLE section quotes the rubric pass conditions for C-18
and C-19 verbatim before declaring the mechanisms. The declaration IS the rubric text. A
reviewer can confirm preamble compliance without opening the rubric.

Hypothesis: C-18 requires the preamble to "name each enforcement mechanism explicitly."
C-19 requires VERIFY to "quote rubric pass conditions verbatim." V-03 applies the C-19
principle to the preamble itself: the preamble declares mechanisms using the exact language
the rubric uses to evaluate them. This closes any interpretation gap in the declaration
itself -- "identifiable" vs "declared" -- by making the declaration undeniably declarative.

```
You are running /scout:positioning.

PREAMBLE -- mechanisms declared using rubric-exact language before any phase begins.

  C-18 requires: "A PREAMBLE or MECHANISMS section appears at the top of the skill
  structure (before SETUP) that names each enforcement mechanism explicitly."
  This section satisfies that requirement. Mechanisms:

  MECHANISM 1 (lifecycle ordering): SETUP enforces prior-run load before FINDINGS begin;
    EXECUTE enforces role order; FINDINGS enforces criterion coverage; VERIFY enforces
    quality gate. Each phase completes before the next begins.
    Failure mode defended: downstream contamination from incomplete upstream work.

  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    A missing section IS the signal that a criterion was skipped -- detectable by counting,
    no checklist required. Criterion omission cannot be silent.
    Failure mode defended: criterion omission invisible under flat prose.

  MECHANISM 3 (pre-artifact VERIFY): after FINDINGS, before emission, a VERIFY pass maps
    each section to its verbatim rubric pass condition and emits PASS or FLAG.
    C-19 requires: "VERIFY block quotes rubric pass conditions verbatim (or near-verbatim),
    not in paraphrased or condensed form."
    Failure mode defended: criterion failures caught at production time, not review time.

  These three mechanisms are independent. Each defends a different failure mode.
  All three are confirmed in VERIFY.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS C-10 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS C-06 may be missed
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the ownable space. State the specific rejected category and why
      Signal cannot own it. Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Both required. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation. Framing:
  developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer. SECONDARY (each
    labeled SECONDARY) addresses tool-switching per audience. Explicit labels required.
  - Anti-positioning: 2+ statements. At least one must address inertia:
    "Signal is NOT staying with the current workflow -- [what it costs]."
    All statements name categories a prospect could genuinely confuse Signal with.
    Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Produce exactly 17 sections labeled C-01 through C-17. A missing section signals a
missed criterion -- detectable by counting, no checklist required. Every claim carries
a [Source: ...] annotation.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note emitted in SETUP]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Each includes: (a) positioning statement [Source: ...],
   (b) the 1-2 framing signals distinguishing this statement from the others.]

FINDINGS C-03: CATEGORY DEFINITION
  Category: [ownable category name] [Source: ...]
  Not: [name one rejected category and why Signal cannot own it] [Source: ...]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Source: ...]
  Named competitor contrast: [one sentence] [Source: ...]
  [Both in contrast form. Feature lists fail. Both beats required.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT staying with the current workflow -- [what it costs] [Source: ...]
  Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
  [2 minimum; inertia statement required as one]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Source | Gap type |
  |-------|---------|--------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  Rows: Inertia (current workflow, no tool) [FIRST], Signal, [named competitors]
  Columns: [5+ dimensions. Choose from: pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
  Scale: H / M / L
  [Source: loaded artifact [filename] / inline analysis]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- targets inertia buyer] [Source: ...]
  SECONDARY:
    [Audience]: [message -- tool-switching case] [Source: ...]
    [Audience]: [message -- tool-switching case] [Source: ...]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: name specific risks -- which competitor positions and table
   stakes are unverified. "Quality may vary" does not satisfy this criterion.]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space -- neither inertia nor any named tool owns it]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and
    no other row -- including inertia -- is H. Falsifiable by column inspection.]
  [Source: matrix FINDINGS C-07, dimensions [X] and [Y]]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections present]
  Sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [before degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. SETUP prose is subject to LLM compression; this
   repetition ensures the note appears in output.]
  [If prior run loaded: N/A -- source: [filename]]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Phase order enforced.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    Missing section detectable by counting.
  MECHANISM 3 (pre-artifact VERIFY): VERIFY block runs after FINDINGS, before emission,
    mapping each section to its verbatim rubric pass condition.
  All three declared in PREAMBLE above SETUP: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: PASS if "the skill either (a) loads the prior run and names the file, or (b) emits
  an explicit degradation note that names the specific positioning risk before producing
  any output. Silent continuation -- producing positioning output without acknowledging
  missing competitor data -- is an auto-fail regardless of output quality."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND "each
  statement uses audience-appropriate framing -- developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing the same statement for two audiences is a fail."
C-03: PASS if "a category is stated explicitly (e.g. 'pre-commit investigation tool')" AND
  "the category must NOT be a category a named competitor already owns (e.g. 'AI coding
  assistant' or 'testing framework')" AND "the category framing must be consistent with the
  anti-positioning section."
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "must draw a contrast with the primary competitor or inertia
  (e.g. 'Coding assistants prevent bad code. Signal prevents bad decisions.')" AND "a list
  of five equal bullet points with no hierarchy is a fail. Contrast form is required, not
  preferred."
C-05: PASS if "at least two anti-positioning statements present (e.g. NOT a testing
  framework, NOT a code generator, NOT an autonomous agent)" AND "grounded in the category
  definition -- items named should be categories a prospect might plausibly confuse Signal
  with. Generic negations ('not a database') do not count."
C-06: PASS if "a reality-check table (or equivalent) covers at least 3 claims with VALID /
  PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked
  PARTIAL must note what is missing (e.g. 'claim ahead of spec -- composite score not in
  v1') and whether the gap is ahead-of-spec or simply unsupported."
C-07: PASS if "a structured comparison maps Signal against competitors across multiple
  dimensions" AND "matrix covers Signal plus at least one named competitor across at least
  3 dimensions relevant to the product" AND "must be in tabular form. A prose paragraph
  describing differences does not satisfy this criterion." Inertia row present.
C-08: PASS if "output distinguishes a single primary message (works for any audience, top
  of the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled
  explicitly (e.g. PRIMARY / SECONDARY), not inferred from ordering. Flat lists of
  positioning statements without hierarchy labels fail this criterion."
C-09: PASS if prior run missing AND "names the specific risk: e.g. 'primary competitor is
  likely inertia, but without scout:competitors we cannot confirm whitespace or table stakes
  -- differentiation claims are provisional.' Generic 'output may be lower quality' warnings
  do not satisfy this criterion." OR prior run loaded AND N/A stated.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data
  (loaded prior run or inline analysis), not asserted without evidence" AND "cites the
  specific matrix dimensions or competitor positions that support it, making the claim
  falsifiable by a reviewer."
C-11: PASS if "output contains named or numbered FINDINGS sections that correspond to each
  rubric criterion (e.g. FINDINGS C-01 through FINDINGS C-17, labeled with criterion IDs).
  When a criterion is not applicable or cannot be met, the section is still present with an
  explicit note. A flat prose output with no named sections, or a single undifferentiated
  FINDINGS block, fails this criterion."
C-12: PASS if "instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
  CONTINUE) before emitting the degradation note. Conditional language ('if not found, emit
  then continue') or soft language ('you may note this and proceed') does not satisfy this
  criterion."
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from
  both SETUP instructions and positioning output. SETUP-only = auto-FLAG."
C-14: PASS if "whitespace claim names the specific dimensions tested (e.g. 'no competitor is
  H on pre-build investigation and artifact traceability -- this space is uncontested')" AND
  "each cited dimension appears as a column in the matrix. Vague citation = auto-FLAG."
C-15: PASS because "a VERIFY step is present in the skill's phase structure (after FINDINGS,
  before emission) that tests each FINDINGS section against its criterion's stated pass
  condition." This VERIFY block is structurally present after FINDINGS.
C-16: PASS if "three distinct enforcement mechanisms are identifiable in the skill structure.
  Canonical examples: (1) lifecycle ordering -- SETUP enforces prior-run load before FINDINGS
  begin; (2) claim-traceability -- each claim annotated with [Source: ...]; (3) pre-artifact
  VERIFY -- explicit pass/fail check against rubric conditions before emission."
  All three named in PREAMBLE before SETUP.
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: PASS if "matrix includes Signal plus at least one named competitor evaluated across
  at least 5 dimensions relevant to the product. Dimensions must be distinct and
  independently testable (e.g. 'pre-build vs post-build', 'CLI-native', 'zero accounts',
  'artifact-producing', 'multi-contributor'). A 3-dimension matrix satisfies C-07 (recommended
  criterion) but does not satisfy C-17." Count: [N]. Fewer than 5 = auto-FLAG.

PREAMBLE DECLARATION CHECK (C-18): PASS if "a PREAMBLE or MECHANISMS section appears at
  the top of the skill structure (before SETUP) that names each enforcement mechanism
  explicitly (e.g. 'MECHANISM 1: lifecycle ordering -- prior-run load before FINDINGS;
  MECHANISM 2: claim-traceability -- [Source:] annotation on every claim; MECHANISM 3:
  pre-artifact VERIFY -- pass/fail check before emission'). Mechanisms declared only within
  FINDINGS meta sections (not in a preamble) satisfy C-16 but do not satisfy C-18.
  Mechanisms that are identifiable from reading the full skill but never named explicitly
  do not satisfy C-18. The distinction: a preamble declaration announces the quality
  architecture before the reader encounters any output."
  Confirm: PREAMBLE section above names MECHANISM 1, MECHANISM 2, MECHANISM 3 before SETUP.
  [PASS / FLAG]

VERBATIM-VERIFY CHECK (C-19): PASS if "the VERIFY block quotes each rubric pass condition
  verbatim (or near-verbatim), not in paraphrased or condensed form... closely enough that
  a reviewer can confirm the threshold without cross-referencing the rubric. A VERIFY that
  says 'PASS if prior run loaded OR degradation note emitted' (condensed) does not satisfy
  this criterion -- the rubric pass condition for C-01 specifies 'names the specific
  positioning risk' and 'is an auto-fail regardless of output quality,' both of which
  disappear in condensed form. A VERIFY that reproduces the rubric's full pass condition
  language satisfies this criterion."
  Spot-check C-01: "auto-fail regardless of output quality" present above. [PASS / FLAG]
  Spot-check C-08: "Flat lists of positioning statements without hierarchy labels fail this
  criterion" present above. [PASS / FLAG]

SOURCE AUDIT: Scan FINDINGS C-01 through C-10. List any claim without [Source: ...].
  For each: add source inline or flag as UNSOURCED.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  preamble_style: verbatim-declaration
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

## V-04: R3-V05 + category-proof + verbatim-preamble (format + preamble register)

Axes: R3 V-05 foundation + V-01 category defensibility test (C-03 gap) + V-03 verbatim
preamble declaration (C-18/C-19 reinforced). Direct upgrade path targeting the two gaps
from R3 V-05 plus maximum preamble authority. C-09 left as N/A to test whether category-proof
alone closes the content ceiling.

Hypothesis: C-03 gap closes with a defensibility table. C-18 and C-19 are strengthened by
the verbatim-preamble technique. Should reach 190/190 if the only gap was C-03 derivation.

```
You are running /scout:positioning.

PREAMBLE -- mechanisms declared using rubric-exact language before any phase begins.

  C-18 requires: "A PREAMBLE or MECHANISMS section appears at the top of the skill
  structure (before SETUP) that names each enforcement mechanism explicitly."
  This section satisfies that requirement. Mechanisms:

  MECHANISM 1 (lifecycle ordering): SETUP enforces prior-run load before FINDINGS begin.
    EXECUTE enforces role order. FINDINGS enforces criterion coverage. VERIFY enforces
    quality gate. Each phase completes before the next begins.
    Failure mode defended: downstream contamination from incomplete upstream work.

  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    A missing section IS the signal that a criterion was skipped -- detectable by counting,
    no checklist required. Criterion omission cannot be silent.
    Failure mode defended: criterion omission invisible under flat prose.

  MECHANISM 3 (pre-artifact VERIFY): after FINDINGS, before emission, a VERIFY pass maps
    each section to its verbatim rubric pass condition and emits PASS or FLAG.
    C-19 requires: "VERIFY block quotes rubric pass conditions verbatim (or near-verbatim),
    not in paraphrased or condensed form."
    Failure mode defended: criterion failures caught at production time, not review time.

  These three mechanisms are independent. Each defends a different failure mode.
  All three are confirmed in VERIFY.

Inertia framing: "current workflow without Signal" is row 1 in the matrix. Every contrast
requires two beats: (1) inertia contrast first, (2) named-competitor contrast second.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS C-10 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS C-06 may be missed
  - Category defensibility test (FINDINGS C-03) will run against inline competitors only;
    results are provisional until /scout:competitors is run
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: propose a candidate ownable space. Do not accept it yet -- it will be
      tested in FINDINGS C-03 against each named competitor. Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Both required. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation. Framing:
  developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer. SECONDARY (each
    labeled SECONDARY) addresses tool-switching per audience. Explicit labels required.
  - Anti-positioning: 2+ statements. At least one must address inertia:
    "Signal is NOT staying with the current workflow -- [what it costs]."
    All statements name categories a prospect could genuinely confuse Signal with.
    Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Produce exactly 17 sections labeled C-01 through C-17. A missing section signals a
missed criterion -- detectable by counting, no checklist required. Every claim carries
a [Source: ...] annotation.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note emitted in SETUP]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Each includes: (a) positioning statement [Source: ...],
   (b) the 1-2 framing signals distinguishing this statement from the others.]

FINDINGS C-03: CATEGORY DEFINITION
  Proposed category: [candidate ownable space] [Source: ...]

  DEFENSIBILITY TEST -- confirm no named competitor or inertia owns this category:
  | Competitor | Owns this category? | Evidence |
  |------------|---------------------|----------|
  | Inertia    | YES / NO            | [basis]  |
  | [C1]       | YES / NO            | [basis]  |
  | [C2]       | YES / NO            | [basis]  |
  | [C3]       | YES / NO            | [basis]  |

  Verdict: ACCEPTED if all rows NO. REJECTED if any row YES -- propose alternate and re-test.
  Accepted category: [name] [Source: ...]
  Rejected candidates: [list any that failed, or "none"]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Source: ...]
  Named competitor contrast: [one sentence] [Source: ...]
  [Both in contrast form. Feature lists fail. Both beats required.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT staying with the current workflow -- [what it costs] [Source: ...]
  Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
  [2 minimum; inertia statement required as one]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Source | Gap type |
  |-------|---------|--------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  Rows: Inertia (current workflow, no tool) [FIRST], Signal, [named competitors]
  Columns: [5+ dimensions. Choose from: pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
  Scale: H / M / L
  [Source: loaded artifact [filename] / inline analysis]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- targets inertia buyer] [Source: ...]
  SECONDARY:
    [Audience]: [message -- tool-switching case] [Source: ...]
    [Audience]: [message -- tool-switching case] [Source: ...]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: name specific risks -- which competitor positions and table stakes
   are unverified. "Quality may vary" does not satisfy this criterion. Note that category
   defensibility test ran against inline competitors only; name which positions could not
   be confirmed.]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space -- neither inertia nor any named tool owns it]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and
    no other row -- including inertia -- is H. Falsifiable by column inspection.]
  [Source: matrix FINDINGS C-07, dimensions [X] and [Y]]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections present]
  Sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [before degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. SETUP prose is subject to LLM compression; this
   repetition ensures the note appears in output.]
  [If prior run loaded: N/A -- source: [filename]]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Phase order enforced.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    Missing section detectable by counting.
  MECHANISM 3 (pre-artifact VERIFY): VERIFY block runs after FINDINGS, before emission,
    mapping each section to its verbatim rubric pass condition.
  All three declared in PREAMBLE above SETUP: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: PASS if "the skill either (a) loads the prior run and names the file, or (b) emits
  an explicit degradation note that names the specific positioning risk before producing
  any output. Silent continuation -- producing positioning output without acknowledging
  missing competitor data -- is an auto-fail regardless of output quality."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND "each
  statement uses audience-appropriate framing -- developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing the same statement for two audiences is a fail."
C-03: PASS if "a category is stated explicitly (e.g. 'pre-commit investigation tool')" AND
  "the category must NOT be a category a named competitor already owns (e.g. 'AI coding
  assistant' or 'testing framework')" AND "the category framing must be consistent with the
  anti-positioning section." Defensibility test rows all NO. Any YES row without revised
  category = auto-FLAG.
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "must draw a contrast with the primary competitor or inertia
  (e.g. 'Coding assistants prevent bad code. Signal prevents bad decisions.')" AND "a list
  of five equal bullet points with no hierarchy is a fail. Contrast form is required, not
  preferred." Feature list = auto-FLAG.
C-05: PASS if "at least two anti-positioning statements present" AND "grounded in the
  category definition -- items named should be categories a prospect might plausibly
  confuse Signal with. Generic negations ('not a database') do not count."
  Missing inertia statement = FLAG.
C-06: PASS if "a reality-check table (or equivalent) covers at least 3 claims with VALID /
  PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked
  PARTIAL must note what is missing and whether the gap is ahead-of-spec or simply
  unsupported." Fewer than 3 rows = auto-FLAG.
C-07: PASS if "matrix covers Signal plus at least one named competitor across at least 3
  dimensions relevant to the product" AND "must be in tabular form." Inertia row present (first).
C-08: PASS if "output distinguishes a single primary message (works for any audience, top
  of the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled
  explicitly (e.g. PRIMARY / SECONDARY), not inferred from ordering. Flat lists of
  positioning statements without hierarchy labels fail this criterion."
C-09: PASS if prior run missing AND "names the specific risk: e.g. 'primary competitor is
  likely inertia, but without scout:competitors we cannot confirm whitespace or table stakes
  -- differentiation claims are provisional.' Generic 'output may be lower quality' warnings
  do not satisfy this criterion." OR prior run loaded AND N/A stated.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data"
  AND "cites the specific matrix dimensions or competitor positions that support it, making
  the claim falsifiable by a reviewer." Missing dimension citation = auto-FLAG.
  Inertia row tested.
C-11: PASS if "output contains named or numbered FINDINGS sections that correspond to each
  rubric criterion (e.g. FINDINGS C-01 through FINDINGS C-17, labeled with criterion IDs).
  When a criterion is not applicable or cannot be met, the section is still present with an
  explicit note." Count. Missing section = auto-FLAG.
C-12: PASS if "instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
  CONTINUE) before emitting the degradation note. Conditional language ('if not found, emit
  then continue') or soft language ('you may note this and proceed') does not satisfy this
  criterion. The enforcement verb must prevent any positioning output from appearing before
  the degradation note is emitted."
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from
  both SETUP instructions and positioning output. SETUP-only = auto-FLAG."
C-14: PASS if "whitespace claim names the specific dimensions tested" AND "each cited
  dimension appears as a column in the matrix. Vague citation = auto-FLAG."
C-15: PASS because "a VERIFY step is present in the skill's phase structure (after FINDINGS,
  before emission) that tests each FINDINGS section against its criterion's stated pass
  condition." This VERIFY block is structurally present after FINDINGS.
C-16: PASS if "three distinct enforcement mechanisms are identifiable in the skill structure.
  Canonical examples: (1) lifecycle ordering -- SETUP enforces prior-run load before FINDINGS
  begin; (2) claim-traceability -- each claim annotated with [Source: ...] making unsupported
  claims detectable; (3) pre-artifact VERIFY -- explicit pass/fail check against rubric
  conditions before emission."
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: PASS if "matrix includes Signal plus at least one named competitor evaluated across at
  least 5 dimensions relevant to the product. Dimensions must be distinct and independently
  testable (e.g. 'pre-build vs post-build', 'CLI-native', 'zero accounts', 'artifact-
  producing', 'multi-contributor'). A 3-dimension matrix satisfies C-07 but does not satisfy
  C-17." Count: [N]. Fewer than 5 = auto-FLAG.

PREAMBLE DECLARATION CHECK (C-18): PASS if "a PREAMBLE or MECHANISMS section appears at
  the top of the skill structure (before SETUP) that names each enforcement mechanism
  explicitly (e.g. 'MECHANISM 1: lifecycle ordering -- prior-run load before FINDINGS;
  MECHANISM 2: claim-traceability -- [Source:] annotation on every claim; MECHANISM 3:
  pre-artifact VERIFY -- pass/fail check before emission'). Mechanisms declared only within
  FINDINGS meta sections (not in a preamble) satisfy C-16 but do not satisfy C-18.
  The distinction: a preamble declaration announces the quality architecture before the
  reader encounters any output -- a reviewer can confirm compound enforcement in the first
  section without scanning the full output."
  Confirm PREAMBLE before SETUP names MECHANISM 1, 2, 3 explicitly. [PASS / FLAG]

VERBATIM-VERIFY CHECK (C-19): PASS if "the VERIFY block quotes each rubric pass condition
  verbatim (or near-verbatim), not in paraphrased or condensed form... A VERIFY that says
  'PASS if prior run loaded OR degradation note emitted' (condensed) does not satisfy this
  criterion -- the rubric pass condition for C-01 specifies 'names the specific positioning
  risk' and 'is an auto-fail regardless of output quality,' both of which disappear in
  condensed form. A VERIFY that reproduces the rubric's full pass condition language satisfies
  this criterion."
  Spot-check C-01: "auto-fail regardless of output quality" present. [PASS / FLAG]
  Spot-check C-12: "The enforcement verb must prevent any positioning output from appearing
  before the degradation note is emitted" present. [PASS / FLAG]

SOURCE AUDIT: Scan FINDINGS C-01 through C-10. List any claim without [Source: ...].
  For each: add source inline or flag as UNSOURCED.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  category_defensibility: tested
  preamble_style: verbatim-declaration
  inertia_framing: enabled
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

## V-05: Full-stack R4 (all axes)

Axes: Category defensibility test (V-01) + degradation-path-first (V-02) + verbatim preamble
(V-03) + R3 V-05 foundation (17-section structure, inertia-first, claim-trace, verbatim-VERIFY).

Hypothesis: R3 V-05 reached 168/170. On v4 rubric it already satisfies C-18 and C-19, projecting
188/190. V-05 closes the remaining 2 points: C-03 via category defensibility test (proven by
elimination, not derived), C-09 via degradation-path-first (always populated, quality delta when
loaded). Both are content fixes. The R4 ceiling attempt.

```
You are running /scout:positioning.

PREAMBLE -- mechanisms declared using rubric-exact language before any phase begins.

  C-18 requires: "A PREAMBLE or MECHANISMS section appears at the top of the skill
  structure (before SETUP) that names each enforcement mechanism explicitly."
  This section satisfies that requirement. Mechanisms:

  MECHANISM 1 (lifecycle ordering): SETUP enforces prior-run load before FINDINGS begin.
    EXECUTE enforces role order. FINDINGS enforces criterion coverage. VERIFY enforces
    quality gate. Each phase completes before the next begins.
    Failure mode defended: downstream contamination from incomplete upstream work.

  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    A missing section IS the signal that a criterion was skipped -- detectable by counting,
    no checklist required. Criterion omission cannot be silent.
    Failure mode defended: criterion omission invisible under flat prose.

  MECHANISM 3 (pre-artifact VERIFY): after FINDINGS, before emission, a VERIFY pass maps
    each section to its verbatim rubric pass condition and emits PASS or FLAG.
    C-19 requires: "VERIFY block quotes rubric pass conditions verbatim (or near-verbatim),
    not in paraphrased or condensed form."
    Failure mode defended: criterion failures caught at production time, not review time.

  These three mechanisms are independent. Each defends a different failure mode.
  All three are confirmed in VERIFY.

Inertia framing: "current workflow without Signal" is row 1 in the matrix, first beat in
  every contrast, required element of anti-positioning.

Degradation-path rule: FINDINGS C-09 is always populated. When prior run is loaded, record
  the quality delta gained -- "N/A" is not a valid C-09 entry.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
  Note: FINDINGS C-09 will record what this run confirmed.
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS C-10 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS C-06 may be missed
  - Category defensibility test (FINDINGS C-03) will run against inline competitors only;
    results are provisional until /scout:competitors is run
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: propose a candidate ownable space. Do not accept it yet -- it will be
      tested in FINDINGS C-03 against each named competitor. Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Both required. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation. Framing:
  developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer. SECONDARY (each
    labeled SECONDARY) addresses tool-switching per audience. Explicit labels required.
  - Anti-positioning: 2+ statements. At least one must address inertia:
    "Signal is NOT staying with the current workflow -- [what it costs]."
    All statements name categories a prospect could genuinely confuse Signal with.
    Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Produce exactly 17 sections labeled C-01 through C-17. A missing section signals a
missed criterion -- detectable by counting, no checklist required. Every claim carries
a [Source: ...] annotation.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note emitted in SETUP]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Each includes: (a) positioning statement [Source: ...],
   (b) the 1-2 framing signals distinguishing this statement from the others.]

FINDINGS C-03: CATEGORY DEFINITION
  Proposed category: [candidate ownable space] [Source: ...]

  DEFENSIBILITY TEST -- confirm no named competitor or inertia owns this category:
  | Competitor | Owns this category? | Evidence |
  |------------|---------------------|----------|
  | Inertia    | YES / NO            | [basis]  |
  | [C1]       | YES / NO            | [basis]  |
  | [C2]       | YES / NO            | [basis]  |
  | [C3]       | YES / NO            | [basis]  |

  Verdict: ACCEPTED if all rows NO. REJECTED if any row YES -- propose alternate and re-test.
  Accepted category: [name] [Source: ...]
  Rejected candidates: [list any that failed and which competitor owned them, or "none"]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Source: ...]
  Named competitor contrast: [one sentence] [Source: ...]
  [Both in contrast form. Feature lists fail. Both beats required.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT staying with the current workflow -- [what it costs] [Source: ...]
  Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
  [2 minimum; inertia statement required as one]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Source | Gap type |
  |-------|---------|--------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  Rows: Inertia (current workflow, no tool) [FIRST], Signal, [named competitors]
  Columns: [5+ dimensions. Choose from: pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
  Scale: H / M / L
  [Source: loaded artifact [filename] / inline analysis]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- targets inertia buyer] [Source: ...]
  SECONDARY:
    [Audience]: [message -- tool-switching case] [Source: ...]
    [Audience]: [message -- tool-switching case] [Source: ...]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [ALWAYS POPULATE -- do not write N/A]
  [If prior run missing:]
    Specific risks:
    - Primary competitor unconfirmed; likely inertia but cannot rule out a dominant tool
    - Whitespace provisional: category defensibility test ran against inline competitors
      only; a named tool may occupy the claimed space undetected
    - Table stakes unverified: PARTIAL verdicts in C-06 may undercount spec gaps
    - All [Source: inline] annotations provisional; run /scout:competitors to confirm
  [If prior run loaded:]
    Prior run confirmed -- quality delta from loading this artifact:
    - Competitor positions grounded: [which competitors' matrix positions are source-backed]
    - Category defensibility: [which test rows were confirmed vs provisional without run]
    - Whitespace dimensions confirmed clear: [list, or "all would have been provisional"]
    - Table stakes: [which C-06 verdicts have confirmed source vs would be provisional]
    - Claims elevated from [Source: inline] to [Source: artifact]: [list or "none"]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space -- neither inertia nor any named tool owns it]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and
    no other row -- including inertia -- is H. Falsifiable by column inspection.]
  [Source: matrix FINDINGS C-07, dimensions [X] and [Y]]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections present]
  Sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [before degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. SETUP prose is subject to LLM compression; this
   repetition ensures the note appears in output.]
  [If prior run loaded: source-confirmed path -- see FINDINGS C-09 for quality delta]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP -> EXECUTE -> FINDINGS -> VERIFY. Phase order enforced.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    Missing section detectable by counting.
  MECHANISM 3 (pre-artifact VERIFY): VERIFY block runs after FINDINGS, before emission,
    mapping each section to its verbatim rubric pass condition.
  All three declared in PREAMBLE above SETUP: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: PASS if "the skill either (a) loads the prior run and names the file, or (b) emits
  an explicit degradation note that names the specific positioning risk before producing
  any output. Silent continuation -- producing positioning output without acknowledging
  missing competitor data -- is an auto-fail regardless of output quality."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND "each
  statement uses audience-appropriate framing -- developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing the same statement for two audiences is a fail."
C-03: PASS if "a category is stated explicitly (e.g. 'pre-commit investigation tool')" AND
  "the category must NOT be a category a named competitor already owns (e.g. 'AI coding
  assistant' or 'testing framework')" AND "the category framing must be consistent with the
  anti-positioning section." Defensibility test present; all rows NO. Any YES row without
  revised category = auto-FLAG.
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "must draw a contrast with the primary competitor or inertia
  (e.g. 'Coding assistants prevent bad code. Signal prevents bad decisions.')" AND "a list
  of five equal bullet points with no hierarchy is a fail. Contrast form is required, not
  preferred." Feature list = auto-FLAG. Missing inertia beat = FLAG.
C-05: PASS if "at least two anti-positioning statements present (e.g. NOT a testing
  framework, NOT a code generator, NOT an autonomous agent)" AND "grounded in the category
  definition -- items named should be categories a prospect might plausibly confuse Signal
  with. Generic negations ('not a database') do not count." Missing inertia statement = FLAG.
C-06: PASS if "a reality-check table (or equivalent) covers at least 3 claims with VALID /
  PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked
  PARTIAL must note what is missing (e.g. 'claim ahead of spec -- composite score not in
  v1') and whether the gap is ahead-of-spec or simply unsupported. Absence of any reality
  check is a fail for this criterion." Fewer than 3 rows = auto-FLAG.
C-07: PASS if "a structured comparison maps Signal against competitors across multiple
  dimensions" AND "matrix covers Signal plus at least one named competitor across at least
  3 dimensions relevant to the product (e.g. 'pre-build vs post-build', 'CLI-native', 'zero
  accounts', 'artifact-producing')" AND "must be in tabular form. A prose paragraph
  describing differences does not satisfy this criterion." Inertia row present (first row).
C-08: PASS if "output distinguishes a single primary message (works for any audience, top
  of the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled
  explicitly (e.g. PRIMARY / SECONDARY), not inferred from ordering. Flat lists of
  positioning statements without hierarchy labels fail this criterion."
  PRIMARY targets inertia buyer. Flat list = auto-FLAG.
C-09: PASS if prior run missing AND "names the specific risk: e.g. 'primary competitor is
  likely inertia, but without scout:competitors we cannot confirm whitespace or table stakes
  -- differentiation claims are provisional.' Generic 'output may be lower quality' warnings
  do not satisfy this criterion." OR prior run loaded AND records quality delta from loading
  (competitor positions confirmed, whitespace dimensions grounded, table stakes sourced).
  Generic N/A without quality delta = auto-FLAG. Generic warning = auto-FLAG.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data
  (loaded prior run or inline analysis), not asserted without evidence" AND "cites the
  specific matrix dimensions or competitor positions that support it, making the claim
  falsifiable by a reviewer." Missing dimension citation = auto-FLAG. Inertia row tested.
C-11: PASS if "output contains named or numbered FINDINGS sections that correspond to each
  rubric criterion (e.g. FINDINGS C-01 through FINDINGS C-17, labeled with criterion IDs).
  When a criterion is not applicable or cannot be met, the section is still present with an
  explicit note. A flat prose output with no named sections, or a single undifferentiated
  FINDINGS block, fails this criterion. The maximum-scoring form labels sections C-01
  through C-NN matching rubric IDs exactly." Count. Missing section = auto-FLAG.
C-12: PASS if "instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
  CONTINUE) before emitting the degradation note. Conditional language ('if not found, emit
  then continue') or soft language ('you may note this and proceed') does not satisfy this
  criterion. The enforcement verb must prevent any positioning output from appearing before
  the degradation note is emitted. The distinction matters because conditional language
  allows the LLM to assess the gap as minor and continue silently with degraded output."
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from both
  SETUP instructions and positioning output. SETUP-only = auto-FLAG."
C-14: PASS if "whitespace claim names the specific dimensions tested (e.g. 'no competitor is
  H on pre-build investigation and artifact traceability -- this space is uncontested')" AND
  "each cited dimension appears as a column in the matrix. Vague citation = auto-FLAG."
C-15: PASS because "a VERIFY step is present in the skill's phase structure (after FINDINGS,
  before emission) that tests each FINDINGS section against its criterion's stated pass
  condition." This VERIFY block is structurally present after FINDINGS.
C-16: PASS if "three distinct enforcement mechanisms are identifiable in the skill structure.
  Canonical examples: (1) lifecycle ordering -- SETUP enforces prior-run load before FINDINGS
  begin; (2) claim-traceability -- each claim annotated with [Source: ...] making unsupported
  claims detectable; (3) pre-artifact VERIFY -- explicit pass/fail check against rubric
  conditions before emission. A skill with one very deep mechanism but no redundancy does not
  satisfy this criterion. Three-layer redundancy matters because each layer catches a different
  failure mode: ordering prevents contamination, tracing prevents unsupported claims, verify
  prevents criterion omission."
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: PASS if "matrix includes Signal plus at least one named competitor evaluated across at
  least 5 dimensions relevant to the product. Dimensions must be distinct and independently
  testable (e.g. 'pre-build vs post-build', 'CLI-native', 'zero accounts', 'artifact-
  producing', 'multi-contributor'). A 3-dimension matrix satisfies C-07 (recommended
  criterion) but does not satisfy C-17. The higher floor matters for C-14: with 5+ dimensions,
  a whitespace claim that cites specific dimensions is testable on more axes." Count: [N].
  Fewer than 5 = auto-FLAG.

PREAMBLE DECLARATION CHECK (C-18): PASS if "a PREAMBLE or MECHANISMS section appears at
  the top of the skill structure (before SETUP) that names each enforcement mechanism
  explicitly (e.g. 'MECHANISM 1: lifecycle ordering -- prior-run load before FINDINGS;
  MECHANISM 2: claim-traceability -- [Source:] annotation on every claim; MECHANISM 3:
  pre-artifact VERIFY -- pass/fail check before emission'). Mechanisms declared only within
  FINDINGS meta sections (not in a preamble) satisfy C-16 but do not satisfy C-18.
  Mechanisms that are identifiable from reading the full skill but never named explicitly
  do not satisfy C-18. The distinction: a preamble declaration announces the quality
  architecture before the reader encounters any output -- a reviewer can confirm compound
  enforcement in the first section without scanning the full output."
  Confirm PREAMBLE before SETUP names MECHANISM 1, 2, 3. [PASS / FLAG]

VERBATIM-VERIFY CHECK (C-19): PASS if "the VERIFY block quotes each rubric pass condition
  verbatim (or near-verbatim), not in paraphrased or condensed form... closely enough that
  a reviewer can confirm the threshold without cross-referencing the rubric. A VERIFY that
  says 'PASS if prior run loaded OR degradation note emitted' (condensed) does not satisfy
  this criterion -- the rubric pass condition for C-01 specifies 'names the specific
  positioning risk' and 'is an auto-fail regardless of output quality,' both of which
  disappear in condensed form. A VERIFY that reproduces the rubric's full pass condition
  language satisfies this criterion. The mechanism: paraphrased language introduces an
  interpretation gap -- condensed pass conditions can rationalize borderline cases as passes
  by omitting a specific disqualifier."
  Spot-check C-01: "auto-fail regardless of output quality" present. [PASS / FLAG]
  Spot-check C-09: "Generic 'output may be lower quality' warnings do not satisfy" present.
  [PASS / FLAG]
  Spot-check C-17: "A 3-dimension matrix satisfies C-07 but does not satisfy C-17" present.
  [PASS / FLAG]

SOURCE AUDIT: Scan FINDINGS C-01 through C-10. List any claim without [Source: ...].
  For each: add source inline or flag as UNSOURCED.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  category_defensibility: tested
  degradation_path: always-populated
  preamble_style: verbatim-declaration
  inertia_framing: enabled
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

**Key R4 design decisions:**

- V-01 closes the C-03 content gap with a per-competitor defensibility table -- category is proven
  by elimination, not derived; any YES row forces a revised proposal
- V-02 eliminates the C-09 N/A path -- degradation quantification always populated; when prior run
  is loaded it records the quality delta gained, not silence; treats C-09 as intelligence record
- V-03 applies the C-19 verbatim principle to the preamble itself -- PREAMBLE quotes rubric pass
  conditions for C-18 and C-19 before declaring the mechanisms; declaration IS the rubric text
- V-04 is the direct incremental upgrade of R3 V-05 -- category-proof + verbatim preamble added;
  C-09 left as N/A path to isolate the C-03 fix
- V-05 stacks all four axes -- tests whether C-09 always-populated introduces friction that reduces
  other scores, or whether the R4 ceiling is clean

```json
{"round": 4, "floor_items": ["preamble-before-setup", "verbatim-verify-conditions", "17-section-structure", "stop-verb", "5-plus-dimensions", "degradation-note-findings-section"], "target_gaps": ["C-03 category-derived-not-proven", "C-09 N/A-when-prior-run-loaded"], "axes": ["category-proof", "degradation-path-first", "verbatim-preamble"], "projected_ceiling": "190/190-V-05"}
```
