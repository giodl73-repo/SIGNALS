Written to `simulations/quest/golden/scout-positioning-golden-2026-03-14.md`.

---

**Golden file summary:**

- **Score**: 190/190 (v4 rubric) using the simplified body (1598 words, 35% reduction from V-05's 2468)
- **Simplification**: PASS -- all 17 essential criteria preserved; VERIFY condensed from ~970 words to ~235 words by dropping verbatim C-19 overhead

**5 patterns that distinguish it from baseline V-01:**

1. **Category proof by elimination** -- DEFENSIBILITY TEST table in C-03, ACCEPTED only if all rows NO, re-test loop on any YES
2. **C-09 always populated** -- PREAMBLE declares N/A invalid; loaded-run path records quality delta (positions confirmed, whitespace grounded, claims elevated), not silence
3. **Inertia as structural first-class** -- PREAMBLE global rule: row 1 in matrix, first beat in every contrast, required in anti-positioning
4. **Three-layer enforcement declared before SETUP** -- MECHANISM 1/2/3 in PREAMBLE, confirmed in FINDINGS C-16, checked in VERIFY
5. **Condensed VERIFY** -- all 17 criterion checks preserved, aspirational C-19 verbatim overhead dropped; structural redundancy from PREAMBLE + C-16 makes condensed form sufficient
ach section to its rubric pass condition and emits PASS or FLAG.
  All three confirmed in VERIFY.

Inertia framing: "current workflow without Signal" is row 1 in the matrix, first beat in
  every contrast, required element of anti-positioning.

Degradation-path rule: FINDINGS C-09 is always populated. When prior run is loaded, record
  the quality delta gained -- "N/A" is not a valid C-09 entry.

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
   separate from SETUP instructions.]
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
    mapping each section to its rubric pass condition.
  All three declared in PREAMBLE above SETUP: YES

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in FINDINGS C-07: [list them]
  Count: [N] -- PASS if N >= 5.
--- END FINDINGS ---

--- VERIFY ---
Check each section against its rubric pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [exact failure description]"

C-01: Prior run loaded and named, OR degradation note names specific risk before any output.
  Silent continuation = auto-fail regardless of output quality.
C-02: Every --audiences audience has its own statement with audience-appropriate framing.
  Reuse = fail.
C-03: Category stated, not owned by any named competitor or inertia. Defensibility table
  all rows NO. Any YES row without revised category = auto-FLAG.
C-04: One differentiator in contrast form. Inertia beat + named-competitor beat both present.
  Feature list = auto-FLAG. Missing either beat = FLAG.
C-05: 2+ anti-positioning statements. Inertia statement required. Generic negations = auto-FLAG.
C-06: 3+ claims with VALID/PARTIAL/INVALID. PARTIAL names gap type (ahead-of-spec vs unsupported).
  Fewer than 3 rows = auto-FLAG.
C-07: Inertia row first. 5+ dimensions. Tabular form. Prose description = auto-FLAG.
C-08: PRIMARY labeled (inertia buyer). SECONDARY labeled per audience. Flat list = auto-FLAG.
C-09: ALWAYS POPULATED. Missing run: names specific risks (not generic warning). Loaded run:
  records quality delta. Generic N/A = auto-FLAG. Generic "may be lower quality" = auto-FLAG.
C-10: Whitespace claim states specific matrix dimensions. Inertia row tested. Missing dimension
  citation = auto-FLAG.
C-11: Exactly 17 FINDINGS sections C-01 through C-17 present. Missing section = auto-FLAG.
C-12: STOP verb before degradation note in SETUP. Conditional or soft language = auto-FLAG.
C-13: Degradation note in named FINDINGS section, separate from SETUP. SETUP-only = auto-FLAG.
C-14: Dimensions cited in C-10 each appear as named column in C-07 matrix. Vague citation
  = auto-FLAG.
C-15: VERIFY phase present after FINDINGS, before emission. [PASS by position]
C-16: Three mechanisms declared in PREAMBLE, confirmed in FINDINGS C-16.
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
C-17: Matrix has 5+ distinct dimensions. Count: [N]. Fewer than 5 = auto-FLAG.

PREAMBLE CHECK (C-18): PREAMBLE before SETUP names MECHANISM 1, 2, 3 explicitly. [PASS / FLAG]

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
  inertia_framing: enabled
  enforcement_layers: lifecycle,structural-mandate,pre-artifact-verify
```

---

## What Made It Golden

**Pattern 1: Category proof by elimination, not derivation**
FINDINGS C-03 includes a mandatory DEFENSIBILITY TEST table -- one row per named competitor
plus inertia, each tested for category ownership with evidence. ACCEPTED only if all rows
return NO. Any YES row triggers a revised proposal and re-test. This converts category
selection from assertion ("we occupy X space") to proof ("no competitor owns X; verified
per-row"). Scored 10/10 on C-03 vs 9/10 in variations without the table.

**Pattern 2: Degradation-path-first -- C-09 always populated**
The PREAMBLE declares: "FINDINGS C-09 is always populated. When prior run is loaded, record
the quality delta gained -- 'N/A' is not a valid C-09 entry." When a prior run exists, C-09
records what loading confirmed (competitor positions grounded, whitespace dimensions validated,
table stakes sourced, claims elevated from inline to artifact). This treats C-09 as an
intelligence record on every execution, not a fallback for the missing-run case only.

**Pattern 3: Inertia as a structural first-class entity**
Inertia framing is declared in the PREAMBLE as a global rule applied everywhere: row 1 in the
matrix, first beat in every contrast, required element of anti-positioning. This prevents
inertia from being treated as an optional competitor entry and ensures it anchors the entire
positioning output -- matrix, differentiator, messaging hierarchy, and anti-positioning all
reference it by structural mandate.

**Pattern 4: Three-layer compound enforcement declared before any phase**
PREAMBLE declares MECHANISM 1 (lifecycle ordering), MECHANISM 2 (structural mandate: 17
labeled sections), and MECHANISM 3 (pre-artifact VERIFY) before SETUP begins. FINDINGS C-16
confirms all three are active. VERIFY checks all three again. A reviewer can audit enforcement
architecture in the first section without scanning the full output.

**Pattern 5: Condensed VERIFY maintains all 17 criterion checks**
The simplified VERIFY drops verbatim rubric quotes (aspirational C-19) but preserves a
per-criterion check for all 17 essential criteria plus C-18. Each check names the auto-FLAG
condition explicitly. The PREAMBLE + FINDINGS C-16 provide structural redundancy that makes
the condensed VERIFY sufficient -- three mechanisms catch failures before VERIFY runs.

---

## Final Rubric Criteria Summary (v5, 21 criteria / 210 pts max)

### Essential (50 pts)

| ID | Criterion | Type |
|----|-----------|------|
| C-01 | Prior run handling | behavior |
| C-02 | Per-audience positioning statements | coverage |
| C-03 | Category definition | correctness |
| C-04 | Core differentiator | correctness |
| C-05 | Anti-positioning | coverage |

### Recommended (60 pts)

| ID | Criterion | Type |
|----|-----------|------|
| C-06 | PM reality check | correctness |
| C-07 | Competitive differentiation matrix | structure |
| C-08 | Messaging hierarchy | structure |
| C-09 | Degradation quantification | behavior |
| C-10 | Whitespace identification | correctness |
| C-11 | Output structure mirrors rubric | structure |

### Aspirational (100 pts)

| ID | Criterion | Type |
|----|-----------|------|
| C-12 | STOP enforcement verb | behavior |
| C-13 | Dedicated FINDINGS for degradation | structure |
| C-14 | Whitespace citation obligation | correctness |
| C-15 | Pre-artifact VERIFY pass | behavior |
| C-16 | Compound enforcement stacking | behavior |
| C-17 | Matrix dimension floor of 5+ | structure |
| C-18 | Preamble mechanism declaration | behavior |
| C-19 | Verbatim-VERIFY pass conditions | behavior |
| C-20 | Category defensibility test by elimination | depth |
| C-21 | Loaded-path quality delta | behavior |

**v4 score (17 criteria)**: 190/190
**v5 max (21 criteria)**: 210

### Round progression

| Round | Best score | Key advance |
|-------|-----------|-------------|
| R1 | ~130/170 | Baseline |
| R2 | ~155/170 | Inertia-first, claim-trace |
| R3 | 168/170 | 17-section mandate, STOP verb, 5+ dims, dedicated C-13 |
| R4 | 190/190 | Category defensibility test (C-03), always-populated degradation (C-09), verbatim preamble |

```json
{
  "skill": "scout-positioning",
  "date": "2026-03-14",
  "rounds": 4,
  "score": 190,
  "max_score_v4": 190,
  "simplified": true,
  "simplified_word_count": 1598,
  "original_word_count": 2468,
  "all_essential_pass": true,
  "golden_patterns": [
    "category-proof-by-elimination",
    "degradation-path-always-populated",
    "inertia-structural-first-class",
    "three-layer-compound-enforcement-preamble",
    "condensed-verify-essential-only"
  ]
}
```
