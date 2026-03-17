Written to `simulations/quest/variations/scout-positioning-variations-R2-2026-03-14.md`.

---

## scout-positioning R2 Variations

**R2 baseline floor** (all 5 variations lock in R1 learnings):
- STOP verb, not conditional language (C-12)
- Dedicated FINDINGS section for degradation, not buried in SETUP prose (C-13)
- Whitespace citation names specific matrix dimensions (C-14)
- Contrast form required, not preferred (C-04 fix)
- Explicit PRIMARY / SECONDARY labels (C-08 fix)

---

### Single-axis (3)

**V-01 — Rubric-literal**
Axis: Output format. Sections numbered C-01 through C-10 matching rubric criterion IDs. A missing section IS the signal a criterion was skipped — no checklist pass required. Each EXECUTE role owns specific FINDINGS sections.
Hypothesis: When the output format is the rubric, structural omission replaces content review as the detection mechanism.

**V-02 — Claim-trace**
Axis: Output format. Every positioning claim in FINDINGS carries `[Source: ...]` — matrix cell, artifact, spec section, or inline. A SOURCE AUDIT block scans for unsourced claims before the artifact is emitted.
Hypothesis: Citation obligation at the point of production forces grounding earlier than a post-hoc reality check. Directly operationalizes C-14.

**V-03 — Dialog-adversarial**
Axis: Role sequence. Each role runs CHALLENGE then PRODUCE. GTM challenges Strategy's category under audience pressure before writing statements. PM challenges GTM's claims before the reality-check table. Design challenges PM's coverage before anti-positioning. A CHALLENGE SUMMARY tracks what changed.
Hypothesis: Adversarial pressure surfaces unsupported claims before they calcify into the artifact.

---

### Combined-axis (2)

**V-04 — Matrix-dominant + rubric-literal**
Axes: Matrix as evidence layer (V-03 R1) + rubric-literal section numbering (V-01 R2). Matrix is built before any prose. Every FINDINGS section cites a matrix cell. FINDINGS C-01 through C-10 structure forces criterion-complete output.
Hypothesis: Maximum defensibility (every claim grounded) + maximum structural completeness (every criterion has a section). Combines the two strongest structural enforcement strategies.

**V-05 — V-05-baseline + claim-trace + self-verify**
Axes: Lifecycle phase boundaries (R1 winner) + source citations on every claim (V-02 R2) + a VERIFY pass that checks each FINDINGS section against its pass condition before emitting the artifact.
Hypothesis: Three-layer enforcement should approach maximum R2 score. Lifecycle prevents role bleed, claim annotations prevent unsourced assertions, VERIFY catches failures before the artifact ships.

---

**Key R2 design decisions:**
- V-01 is the only variation where the output template IS the rubric criterion list
- V-02 is the only variation with an explicit SOURCE AUDIT block post-FINDINGS
- V-03 is the only variation with bidirectional role accountability (CHALLENGE phases)
- V-04 requires 5+ matrix dimensions (vs 3 in V-01/V-02/V-03) — matrix-first mandates more depth
- V-05 adds VERIFY as a post-output self-check; `verify_status` is written to frontmatter
:
  - Name the product category Signal occupies. It must be ownable -- not "AI coding
    assistant," "testing framework," or any category a named competitor already claims.
    Name the specific category you are rejecting and why.
  - State the single core differentiator in one sentence. Contrast form is required,
    not preferred: "[X] does Y. Signal does Z." Write the inertia contrast first
    (why change at all?), then write the named-competitor contrast (why this?).

GTM -- owns FINDINGS C-02:
  For each audience named in the invocation, write one distinct positioning statement.
  Audience framing is required: developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads get
  process-repeatability language. Reusing a statement for two audiences is a fail.

PM -- owns FINDINGS C-06:
  Reality-check table. At least 3 claims from the positioning statements, VALID /
  PARTIAL / INVALID verdicts. For PARTIAL: what is missing and whether the gap is
  ahead-of-spec or unsupported. For INVALID: what in the spec contradicts the claim.

DESIGN -- owns FINDINGS C-05 and C-08:
  - Messaging hierarchy: one PRIMARY message (labeled PRIMARY) that works across all
    audiences. Per-audience SECONDARY messages (each labeled SECONDARY). Explicit
    labels required -- flat lists without labels fail.
  - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]"
    statements. Name categories a prospect could genuinely confuse Signal with.
    Generic negations ("not a database") do not count.

FINDINGS:
Emit one section per criterion below. When a criterion cannot be met, emit the
section with an explicit note -- never omit the section entirely.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note repeated here]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. State the 1-2 framing signals that distinguish this
   statement from the others -- what dimension this audience hears that others do not.]

FINDINGS C-03: CATEGORY DEFINITION
  Category: [ownable category name]
  Not: [name one category explicitly rejected and why Signal cannot own it]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence -- why change at all?]
  Named competitor contrast: [one sentence -- why this over [competitor]?]
  [Both sentences in contrast form. Feature lists fail this section.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT [X] -- [why this confusion is plausible]
  Signal is NOT [Y] -- [why this confusion is plausible]
  [2 minimum; add more if category definition creates additional confusion candidates]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Gap type |
  |-------|---------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  [Table: Signal + 2+ named competitors. 3+ product-relevant dimensions. H/M/L scale.]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- works for all audiences]
  SECONDARY:
    [Audience]: [message]
    [Audience]: [message]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: specific risks named -- "primary competitor likely inertia
   but unverified," "whitespace claim provisional," etc. Not "quality may vary."]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE
  Claim: [one uncontested space]
  Dimensions tested: [name the specific matrix columns where Signal is H and no
    named competitor is H -- this makes the whitespace claim falsifiable]

AMEND: 3 things the user can change. For each: what changes in the output.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter: skill, topic, date, source_competitors (filename or "none").
```

---

## V-02: Claim-trace (output format axis)

Axis: Output format -- every positioning claim carries a [Source: ...] annotation.
No unsourced claim is permitted anywhere in FINDINGS.

Hypothesis: The citation mandate forces grounding at the point of claim production,
not as a post-hoc check. Elevates C-10 (whitespace) and C-14 (whitespace citation)
compliance and makes C-03/C-04 category claims falsifiable. Risk: annotation overhead
may produce mechanical-sounding output; prose flow degrades.

```
You are running /scout:positioning. Every positioning claim in FINDINGS must carry
a [Source: ...] annotation. An unsourced claim is invalid and must be flagged.

Valid source types:
  [Source: matrix cell -- Signal H, [Competitor] L/M on [dimension]]
  [Source: competitors artifact -- [filename], [specific finding]]
  [Source: spec -- [section or feature name]]
  [Source: inline analysis -- [basis for the claim]]

SETUP:
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor unverified (likely inertia; cannot confirm without run)
  - Whitespace claim will cite only inline analysis, not a verified competitor set
  - Table stakes unverified; PARTIAL or INVALID verdicts may be missed
  All claims that follow are labeled [Source: inline]. Run /scout:competitors for
  source-grounded positioning.

  Then identify 3-5 competitors inline. Label all inline claims throughout.

EXECUTE:
Run four roles in spec order. Every claim produced must carry a source annotation.

STRATEGY:
  - Category: name the space Signal occupies. Must be ownable -- not a category
    a named competitor already claims. State the rejected category explicitly.
    Annotate: [Source: competitors artifact or inline -- [basis]].
  - Core differentiator: one sentence, contrast form required. "X does Y. Signal
    does Z." Write inertia contrast first, named-competitor contrast second.
    Annotate both contrasts with their source.

GTM: Per-audience positioning statements. One per audience named in the invocation.
  Audience framing required. Each statement must cite at least one source that
  grounds the claim -- a spec feature, matrix dimension, or competitor position.
  Reusing a statement for two audiences fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing and whether the gap is ahead-of-spec or unsupported.
  For each verdict, name the source (spec section, matrix cell) that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: one PRIMARY (labeled PRIMARY), per-audience SECONDARY (labeled
    SECONDARY). Explicit labels required -- flat lists without labels fail.
  - Anti-positioning: 2+ "Signal is NOT [X]" statements. Each must name why the
    confusion is plausible, and cite the source that grounds the negation.

FINDINGS:

1. CATEGORY AND DIFFERENTIATOR
   Category: [ownable category name] [Source: ...]
   Not: [rejected category -- why it is taken] [Source: ...]
   Inertia contrast: [statement] [Source: ...]
   Named competitor contrast: [statement] [Source: ...]

2. PER-AUDIENCE POSITIONING STATEMENTS
   [One subsection per audience. Statement + source annotation. State the 1-2
    framing signals that make this statement distinct from the others.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message] [Source: ...]
   SECONDARY:
     [Audience]: [message] [Source: ...]
     [Audience]: [message] [Source: ...]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Table: Signal + 2+ named competitors. 3+ dimensions. H/M/L scale.]
   [Source note: loaded from [filename] / built from inline analysis]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why plausible] [Source: ...]
   Signal is NOT [Y] -- [why plausible] [Source: ...]
   [2 minimum]

6. WHITESPACE
   Claim: [one uncontested space]
   Dimensions tested: [name the specific columns in the matrix above where Signal
     is H and no named competitor is H]
   [Source: matrix section 4, dimensions [X] and [Y]]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Source | Gap type |
   |-------|---------|--------|--------|----------|
   [3+ rows]

8. DEGRADATION NOTE
   [If prior run missing: specific risks named with precision]
   [If prior run loaded: N/A -- source: [filename]]

SOURCE AUDIT: Before emitting the artifact, scan FINDINGS 1 through 7. List any
claims found without a [Source: ...] annotation. For each: either add the source
or flag the claim as UNSOURCED. Emit the audit result as a final block.

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter: skill, topic, date, source_competitors.
```

---

## V-03: Dialog-adversarial (role sequence axis)

Axis: Role sequence -- each role runs in two phases: CHALLENGE (critique the prior
role's output) then PRODUCE (new output). Strategy has no CHALLENGE phase -- it goes
first. Design challenges PM before wrapping.

Hypothesis: Built-in adversarial pressure sharpens differentiators and surfaces
unsupported claims earlier. GTM challenging Strategy's category forces audience-reality
testing before downstream work. PM challenging GTM's statements catches ahead-of-spec
claims before the reality-check table. Risk: CHALLENGE phases may produce redundant
content; role separation may blur.

```
You are running /scout:positioning. Each role runs in two phases: CHALLENGE then
PRODUCE. Adversarial pressure is the quality mechanism -- roles do not simply
accept the prior role's output.

SETUP:
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions
  - Table stakes are unverified; differentiation claims are provisional
  Run /scout:competitors for richer positioning.

  Then identify 3-5 competitors inline and continue.

EXECUTE:

STRATEGY -- PRODUCE (no CHALLENGE phase; goes first):
  - Category: name the product space Signal occupies. It must be ownable. State
    one category Signal cannot claim and why. Name the primary competitive threat
    and the inertia threat separately.
  - Core differentiator: one sentence, contrast form required. Not a feature list.
    Write the inertia contrast first ("Without Signal, teams X; with Signal, Y"),
    then the named-competitor contrast ("[Competitor] does X; Signal does Y").

GTM -- CHALLENGE, then PRODUCE:
  CHALLENGE: Evaluate Strategy's category and differentiator under audience pressure.
    Would a developer, a PM, an architect, or a team lead recognize this category?
    Does the differentiator answer "so what?" for any real audience? If the category
    is inside-out or the differentiator fails the "so what?" test for a named
    audience, say so. Propose a revision if needed before proceeding.
  PRODUCE: For each audience named in the invocation, one positioning statement.
    Different emphasis per audience -- not vocabulary variation on a shared statement.
    Audience framing required: developers get technique language, PMs get
    workflow/evidence language, architects get formal-methods language, team leads
    get process-repeatability language.

PM -- CHALLENGE, then PRODUCE:
  CHALLENGE: Select the 3 strongest claims from GTM's per-audience statements.
    Test each: is it ahead-of-spec, unsupported, or valid? Name any claim that
    would embarrass the team in a real GTM conversation before proceeding.
  PRODUCE: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
    For PARTIAL: what is missing and whether ahead-of-spec or unsupported.
    For INVALID: what in the spec contradicts the claim.

DESIGN -- CHALLENGE, then PRODUCE:
  CHALLENGE: Did PM's reality check miss any claim likely to be challenged?
    Name one claim PM did not assess and state your verdict on it.
  PRODUCE:
    - Messaging hierarchy: one PRIMARY message (labeled PRIMARY), per-audience
      SECONDARY messages (each labeled SECONDARY). Explicit labels required.
      Flat lists without labels fail.
    - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]"
      statements. Name categories a prospect could genuinely confuse Signal with.
      Generic negations do not count.

FINDINGS:

1. CATEGORY AND DIFFERENTIATOR
   [Final version after GTM challenge -- note if GTM revised Strategy's output]
   Category: [ownable category name]
   Inertia contrast: [one sentence]
   Named competitor contrast: [one sentence]

2. PER-AUDIENCE POSITIONING STATEMENTS
   [From GTM, post-challenge. One subsection per audience. Note the 1-2 framing
    signals that make each statement distinct.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message]
   SECONDARY:
     [Audience]: [message]
     [Audience]: [message]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Table: Signal + 2+ named competitors. 3+ dimensions. H/M/L scale.]
   [Source: loaded competitor artifact [filename] / inline analysis]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why this confusion is plausible]
   Signal is NOT [Y] -- [why this confusion is plausible]
   [2 minimum]

6. WHITESPACE
   Claim: [one uncontested space]
   Dimensions tested: [name the specific matrix columns where Signal is H and no
     named competitor is H -- makes the claim falsifiable]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Gap type |
   |-------|---------|--------|----------|
   [3+ rows; include the Design-added claim if flagged; Gap type required]

8. DEGRADATION NOTE
   [If prior run missing: specific risks named precisely]
   [If prior run loaded: N/A -- source: [filename]]

CHALLENGE SUMMARY: Briefly list what changed in each CHALLENGE phase:
  - GTM challenge result: [revised / no change -- reason]
  - PM challenge result: [claims flagged / no change]
  - Design challenge result: [claim added to PM table / no change]

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter: skill, topic, date, source_competitors.
```

---

## V-04: Matrix-dominant + rubric-literal (combined axes)

Axes: Output format (matrix as structural evidence layer, all prose derives from it)
+ Output format (rubric-literal section numbering, C-01 through C-10)

Hypothesis: Combining matrix-dominant evidence grounding with rubric-literal output
structure gives maximum claim defensibility AND maximum structural completeness. Every
claim cites a matrix cell; every criterion has a named output section. Risk: two
structural mandates may feel over-engineered; narrative flow may suffer relative to
prose-first approaches.

```
You are running /scout:positioning. Two structural mandates:
1. Build the competitive differentiation matrix first. All positioning claims must
   derive from it -- cite the matrix cell.
2. Output sections are numbered C-01 through C-10, matching rubric criteria. A
   missing section signals a missed criterion, detectable without a checklist pass.

SETUP:
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before building the matrix, emit:

  FINDINGS C-01 / C-09: PRIOR RUN MISSING
  No scout:competitors artifact found.
  Specific risks:
  - Matrix will be built from inline analysis only -- positions are unverified
  - Whitespace claim (C-10) cannot be grounded in a verified competitor set;
    cite which matrix dimensions you cannot reliably score without a prior run
  - Table stakes are unverified; PARTIAL or INVALID verdicts may be missed
  Run /scout:competitors to ground the matrix in a verified competitor set.

  Then identify 3-5 competitors inline and build the matrix with these as the source.

EXECUTE:

STEP 1 -- BUILD THE MATRIX FIRST (Strategy + GTM):
Construct the competitive differentiation matrix before writing any prose positioning.
Rows: Signal + all named competitors.
Columns: at least 5 product-relevant dimensions. Examples: pre-build vs post-build,
artifact-producing, zero accounts required, CLI-native, investigation-focused,
team-workflow integration, decision-support vs code-generation.
Ratings: H / M / L. Do not rate Signal higher than the spec supports.

This matrix is the evidence layer. All downstream claims must cite a cell.

STEP 2 -- DERIVE POSITIONING (Strategy):
  - Category: which row pattern is unique to Signal? Name the space. It must be
    supported by at least 2 matrix columns where Signal is H and no competitor is H.
    Cite the columns.
  - Core differentiator: the single column where Signal's position is most distinctive.
    One sentence, contrast form required. "[Competitor] is [position] on [dimension].
    Signal is [position] on [dimension]." Write inertia contrast first, then named
    competitor. Cite the matrix column.

STEP 3 -- PER-AUDIENCE STATEMENTS (GTM):
  For each audience named in the invocation, one positioning statement. Each must
  cite 1-2 matrix columns as its grounding. Audience framing required. Reusing a
  statement for two audiences fails.

STEP 4 -- REALITY CHECK (PM):
  3+ claims, VALID / PARTIAL / INVALID. Trace each claim to its matrix cell.
  For PARTIAL: what is missing; ahead-of-spec or unsupported distinction required.

STEP 5 -- HIERARCHY AND ANTI-POSITIONING (Design):
  - Messaging hierarchy: one PRIMARY (labeled PRIMARY), per-audience SECONDARY
    (labeled SECONDARY). Explicit labels required.
  - Anti-positioning: 2+ "Signal is NOT [X]" statements. Each must correspond to
    a matrix row where a competitor is H and Signal is L or M. The matrix grounds
    every negation.

FINDINGS:
(One section per criterion. A missing section is a missed criterion.)

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename] / MISSING: degradation note repeated here]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Matrix dimensions cited per statement.]

FINDINGS C-03: CATEGORY DEFINITION
  Category: [ownable category name]
  Supporting dimensions: [cite 2+ matrix columns where Signal is H, competitors are not]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence] [Matrix: [column]]
  Named competitor contrast: [one sentence] [Matrix: [column], Signal [H/M/L] vs [competitor] [H/M/L]]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT [X] -- [why plausible] [Matrix: [competitor] H on [dimension], Signal L/M]
  Signal is NOT [Y] -- [why plausible] [Matrix: ...]
  [2 minimum]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Matrix cell | Gap type |
  |-------|---------|--------|-------------|----------|
  [3+ rows]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  [Table from Step 1. Signal + 2+ named competitors. 5+ dimensions. H/M/L.]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message]
  SECONDARY:
    [Audience]: [message]
    [Audience]: [message]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: name the specific matrix columns that cannot be reliably
   scored without a verified competitor set]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE
  Claim: [one uncontested space]
  Matrix support: [cite the specific columns where Signal is H and no competitor
    is H -- these columns are the evidence; this makes the claim falsifiable]

AMEND: 3 adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter: skill, topic, date, source_competitors, matrix_dimensions: [list].
```

---

## V-05: V-05-baseline + claim-trace + self-verify (combined axes)

Axes: Lifecycle emphasis (explicit phase boundaries, V-05 R1 baseline) + claim-trace
(every claim annotated with source, V-02 R2) + self-verify (VERIFY pass checks each
FINDINGS section against its pass condition before emitting the artifact)

Hypothesis: Three-layer enforcement -- lifecycle structure prevents role bleed,
claim annotation prevents unsourced assertions, self-verify catches criterion failures
before the artifact is emitted. Should approach maximum score on R2 rubric. Risk:
high structural overhead; longer prompt may cause LLM to abbreviate content.

```
You are running /scout:positioning. Three layers of enforcement:
1. Lifecycle phase boundaries are explicit -- complete one before moving to the next.
2. Every positioning claim in FINDINGS carries a [Source: ...] annotation.
   Valid types: [Source: matrix -- Signal H/M/L on [dim] vs [competitor] H/M/L],
   [Source: artifact -- [filename]], [Source: spec -- [section]], [Source: inline -- [basis]].
3. After FINDINGS, a VERIFY pass checks each section against its pass condition.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS 6 will cite inline analysis only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS 7 may be missed
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Name the product category. Must be ownable. Reject one named category and
      state why Signal cannot own it.
  (b) State the core differentiator. One sentence. Contrast form required -- not
      a feature list. Write the inertia contrast first ("Without Signal, teams X;
      with Signal, Y"), then the named-competitor contrast ("[Competitor] does X;
      Signal does Y"). State the primary competitive threat and inertia threat
      separately.

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation on a shared statement.
  Framing: developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For INVALID: what in the spec contradicts the claim.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: one PRIMARY (labeled PRIMARY), per-audience SECONDARY (each labeled
    SECONDARY). Explicit labels required. Flat lists without labels fail.
  - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]"
    statements. Categories a prospect could genuinely confuse Signal with.
    Generic negations ("not a database") do not count.
--- END EXECUTE ---

--- FINDINGS ---
This section is the deliverable. Sections are numbered to mirror rubric criteria.
A missing section signals a missed criterion -- detectable by structure inspection.
Every claim carries a [Source: ...] annotation.

1. CATEGORY AND DIFFERENTIATOR
   Category: [ownable category name] [Source: ...]
   Rejected category: [name] -- [why Signal cannot own it] [Source: ...]
   Inertia contrast: [one sentence] [Source: ...]
   Named competitor contrast: [one sentence] [Source: ...]
   Primary threat: [named competitor or inertia]

2. PER-AUDIENCE POSITIONING STATEMENTS
   [One subsection per audience.
    Include: (a) positioning statement [Source: ...], (b) the 1-2 framing signals
    that make this statement distinct from the others.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message] [Source: ...]
   SECONDARY:
     [Audience]: [message] [Source: ...]
     [Audience]: [message] [Source: ...]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Table: Signal + 2+ named competitors. 3+ dimensions. H/M/L scale.]
   [Source: loaded artifact [filename] / inline analysis]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
   Signal is NOT [Y] -- [why this confusion is plausible] [Source: ...]
   [2 minimum]

6. WHITESPACE
   Claim: [one uncontested space]
   Dimensions tested: [name the specific matrix columns where Signal is H and no
     named competitor is H -- cite these columns explicitly to make the claim
     falsifiable by a reviewer]
   [Source: matrix section 4, dimensions [X] and [Y]]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Source | Gap type |
   |-------|---------|--------|--------|----------|
   [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

8. DEGRADATION NOTE
   [If prior run missing: specific risks named precisely, as emitted in SETUP]
   [If prior run loaded: N/A -- source: [filename]]
--- END FINDINGS ---

--- VERIFY ---
For each FINDINGS section, emit PASS or FLAG on a single line.
FLAG format: "FINDINGS [N]: [criterion name] -- [what is missing or fails the pass condition]"

1. Category and differentiator: PASS if category is stated, ownable, consistent with C-05.
   Core differentiator is one sentence, contrast form, not a feature list.
2. Per-audience: PASS if every named audience has a distinct statement with different emphasis.
3. Messaging hierarchy: PASS if PRIMARY label present and at least one SECONDARY label present.
4. Competitive matrix: PASS if tabular, Signal + 2+ competitors, 3+ dimensions, H/M/L scale.
5. Anti-positioning: PASS if 2+ statements, each names plausible confusion category, no generic negations.
6. Whitespace: PASS if specific matrix columns cited, not just "no competitor occupies this space."
7. PM reality check: PASS if 3+ rows, PARTIAL/INVALID rows include gap type.
8. Degradation note: PASS if prior run missing AND specific risks named; or prior run loaded AND "N/A."

If all sections PASS: emit "VERIFY: all criteria pass. Artifact ready."
If any section is FLAGged: emit all flags, then emit "VERIFY: artifact has [N] flags.
  Recommend revision before use."
--- END VERIFY ---

AMEND: 3 specific things the user can change, each with a concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
```
