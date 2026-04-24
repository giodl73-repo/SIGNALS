Written to `simulations/quest/variations/scout-positioning-variations-R3-2026-03-14.md`.

---

## scout-positioning R3 Variations

**R3 baseline floor** (all 5 variations lock in):
- All R2 floor items (STOP verb, dedicated degradation FINDINGS, whitespace citation, contrast form, explicit labels)
- **NEW**: 5+ matrix dimensions (C-17)
- **NEW**: VERIFY step after FINDINGS with verify_status in frontmatter (C-15)

---

### Single-axis (3)

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01 -- Rubric-mirror-17** | Output format | 17 FINDINGS sections C-01 through C-17; meta-criteria sections (C-11 to C-17) force the LLM to self-report structural compliance. Missing section = missed criterion, detectable by counting. |
| **V-02 -- Inertia-first** | Inertia framing | Status quo is matrix row 1, first beat in every contrast, required anti-positioning element. Two-beat mandate (inertia THEN named competitor) is structural, not stylistic. |
| **V-03 -- Pre-flight GATE + post-FINDINGS VERIFY** | Lifecycle emphasis | Two distinct quality gates: GATE before EXECUTE (catches input failures), VERIFY after FINDINGS (catches output failures). A blocked GATE stops execution before any positioning work begins. |

### Combined-axis (2)

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| **V-04 -- R2-V05 upgraded** | Lifecycle + claim-trace + verbatim-VERIFY + 5+ dim | Direct incremental upgrade of the R2 winner. Verbatim-VERIFY (pass conditions quoted from rubric text) maximizes C-15. 5+ dim floor captures C-17. Compound enforcement explicitly confirmed in VERIFY block (C-16). |
| **V-05 -- Full-stack** | Rubric-mirror-17 + compound declaration + verbatim-VERIFY + inertia-first + 5+ dim | Three mechanisms declared explicitly in preamble as MECHANISM 1/2/3, then confirmed in VERIFY. 17-criteria structure resolves the C-11 gap from R2 (sections 1-8 weren't 1:1 to criteria). Inertia as first-class row. The R3 ceiling attempt. |

**What makes R3 different from R2:** R2 V-05 had compound enforcement *structurally* but *unlabeled* -- the mechanisms existed but weren't declared. R3 V-05 names them explicitly in the preamble, making C-16 unambiguous. R3 also moves 5+ dimensions from R2 V-04's matrix-dominant specialty to a universal floor across all variations.
 VERIFY catches output-level failures before emission. Two-phase enforcement is more robust than single-phase.

---

### Combined-axis (2)

**V-04 -- R2-V05 upgraded (lifecycle + claim-trace + verbatim-VERIFY + 5+ dim)**
Axes: Lifecycle phase boundaries (R2 V-05 baseline winner) + source citations on every claim (V-02 R2) + VERIFY pass conditions expressed in verbatim rubric language + 5+ matrix dimensions (C-17).
Hypothesis: Incremental upgrade of the R2 winner to directly target the three new R3 criteria. The verbatim-VERIFY upgrade (pass conditions quoted exactly from the rubric text) should yield full C-15 credit. Adding the 5+ matrix floor captures C-17. The compound enforcement declaration (C-16) is now explicit in the VERIFY block. Should approach the R3 ceiling.

**V-05 -- Full-stack: rubric-mirror-17 + compound declaration + verbatim-VERIFY + inertia-first + 5+ dim**
Axes: 17-criteria FINDINGS structure (V-01 R3) + three enforcement mechanisms explicitly named and declared as MECHANISM 1/2/3 in the preamble (C-16) + VERIFY pass conditions quoted verbatim from rubric (C-15) + inertia as first-class matrix row (V-02 R3) + 5+ matrix dimensions (C-17).
Hypothesis: Maximum compound stacking and maximum structural completeness combined. Unlike R2 V-05 where compound enforcement was structural but unlabeled, V-05 R3 names all three mechanisms explicitly in the preamble and confirms them in the VERIFY block. This should resolve the remaining C-11 gap (R2 V-05 got 8/10 on C-11 because sections 1-8 didn't map 1:1 to criteria) while preserving all other R2 V-05 strengths.

---

## V-01: Rubric-mirror-17 (output format axis)

Axis: Output format -- 17 FINDINGS sections labeled C-01 through C-17, matching every rubric
criterion ID. Meta-criteria get their own named sections.

Hypothesis: When the output template IS the 17-criterion rubric list, structural omission is
detectable by counting. The meta-criteria sections (C-11 to C-17) force the LLM to reason about
its own compliance at production time, not at review time.

```
You are running /scout:positioning.
Output format mandate: produce exactly 17 FINDINGS sections labeled C-01 through C-17,
matching the rubric criterion IDs. A missing section IS the signal that a criterion was
skipped -- detectable by structure inspection without a checklist pass.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit:

  FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; cite which
    matrix dimensions are unreliable without a prior run
  - Table stakes are unverified; PARTIAL verdicts in C-06 may be missed
  All downstream claims are labeled [Source: inline].
  Run /scout:competitors for source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Four roles. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the ownable space. Not a category a named competitor already claims.
      Name the specific rejected category and why Signal cannot own it.
  (b) Core differentiator: one sentence, contrast form required. Not a feature list.
      Write inertia contrast first ("Without Signal, teams X; with Signal, Y"),
      then named-competitor contrast ("[Competitor] does X; Signal does Y").

GTM: For each audience named in the invocation, one positioning statement.
  Audience framing required: developers get technique language, PMs get
  workflow/evidence language, architects get formal-methods language, team leads
  get process-repeatability language. Reusing a statement for two audiences fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID verdicts.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For INVALID: what in the spec contradicts the claim.

DESIGN:
  - Messaging hierarchy: one PRIMARY message (labeled PRIMARY), per-audience SECONDARY
    messages (each labeled SECONDARY). Explicit labels required. Flat lists fail.
  - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]."
    Name categories a prospect could genuinely confuse Signal with.
    Generic negations ("not a database") do not count.
--- END EXECUTE ---

--- FINDINGS ---
Produce one section per criterion. When a criterion cannot be met, emit the section with
an explicit note -- never omit it. Each section's content satisfies the pass condition.

FINDINGS C-01: PRIOR RUN HANDLING
  [Loaded: [filename], [N] competitors / MISSING: degradation note repeated here]

FINDINGS C-02: PER-AUDIENCE POSITIONING STATEMENTS
  [One subsection per audience. Include the 1-2 framing signals that distinguish each
   statement from the others. Audience framing required.]

FINDINGS C-03: CATEGORY DEFINITION
  Category: [ownable category name]
  Not: [name one rejected category and why Signal cannot own it]

FINDINGS C-04: CORE DIFFERENTIATOR
  Inertia contrast: [one sentence -- why change at all?]
  Named competitor contrast: [one sentence -- why this over [competitor]?]
  [Both in contrast form. Feature lists fail this section.]

FINDINGS C-05: ANTI-POSITIONING
  Signal is NOT [X] -- [why this confusion is plausible]
  Signal is NOT [Y] -- [why this confusion is plausible]
  [2 minimum; add more if category definition creates confusion candidates]

FINDINGS C-06: PM REALITY CHECK
  | Claim | Verdict | Reason | Gap type |
  |-------|---------|--------|----------|
  [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

FINDINGS C-07: COMPETITIVE DIFFERENTIATION MATRIX
  [Table: Signal + 2+ named competitors. 5+ product-relevant dimensions. H/M/L scale.]
  [Dimensions must be distinct and independently testable. Examples: pre-build vs
   post-build, artifact-producing, zero accounts required, CLI-native,
   investigation-focused, team-workflow integration, decision-support vs code-generation,
   multi-contributor, async evidence trail.]

FINDINGS C-08: MESSAGING HIERARCHY
  PRIMARY: [one message -- works for all audiences]
  SECONDARY:
    [Audience]: [message]
    [Audience]: [message]

FINDINGS C-09: DEGRADATION QUANTIFICATION
  [If prior run missing: name the specific risks -- which competitor positions and table
   stakes are unverified. "Quality may vary" does not satisfy this criterion.]
  [If prior run loaded: N/A]

FINDINGS C-10: WHITESPACE IDENTIFICATION
  Claim: [one uncontested space]
  Dimensions tested: [name the specific matrix columns in C-07 where Signal is H and no
    named competitor is H -- makes the claim falsifiable by column inspection]

FINDINGS C-11: OUTPUT STRUCTURE (META)
  Section count: [confirm 17 FINDINGS sections are present in this output]
  Any sections where pass condition could not be satisfied: [list, or "none"]

FINDINGS C-12: STOP ENFORCEMENT (META)
  Exact verb used in SETUP: [STOP / HALT / DO NOT CONTINUE]
  Position: [confirm the verb appeared before the degradation note, not after]

FINDINGS C-13: DEGRADATION NOTE (DEDICATED)
  [If prior run missing: repeat the specific risk list here as a named FINDINGS section,
   separate from SETUP instructions. Ensures note survives LLM compression of setup prose.]
  [If prior run loaded: N/A -- source: [filename]]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the list from FINDINGS C-10]
  Falsifiability check: [confirm each cited dimension is a column in the C-07 matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status will be set in frontmatter based on VERIFY result below.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  Mechanism 1 (lifecycle ordering): SETUP runs before EXECUTE; EXECUTE runs before
    FINDINGS; FINDINGS runs before VERIFY. Phase order prevents role contamination.
  Mechanism 2 (structural mandate): 17 FINDINGS sections force criterion-complete
    output. A missing section is detectable by inspection without a checklist pass.
  Mechanism 3 (pre-artifact VERIFY): explicit PASS/FLAG check against rubric pass
    conditions before emission. Catches criterion failures at production time.
  All three mechanisms are structurally present in this variation.

FINDINGS C-17: MATRIX DIMENSION FLOOR (META)
  Dimensions in C-07 matrix: [list them]
  Count: [N] -- PASS if N >= 5. FLAG if N < 5.
--- END FINDINGS ---

--- VERIFY ---
Map each FINDINGS section to its pass condition. Emit PASS or FLAG.
FLAG format: "C-XX: [criterion name] -- [what fails the pass condition]"

C-01: PASS if prior run loaded OR degradation note emitted with specific risks before positioning.
C-02: PASS if every named audience has a distinct statement with audience-appropriate framing.
C-03: PASS if ownable category stated; one rejected category named with reason.
C-04: PASS if two contrast sentences (inertia + named competitor) in contrast form. List = FAIL.
C-05: PASS if 2+ statements name plausible confusion categories. Generic negations = FAIL.
C-06: PASS if 3+ rows; PARTIAL/INVALID rows include gap type.
C-07: PASS if tabular, Signal + 2+ competitors, 5+ dimensions, H/M/L. Count dimensions.
C-08: PASS if PRIMARY label present; at least one SECONDARY label per audience.
C-09: PASS if specific risks named (not "quality may vary") OR prior run loaded.
C-10: PASS if uncontested space stated; specific matrix columns cited by name.
C-11: PASS if all 17 FINDINGS sections present.
C-12: PASS if STOP/HALT/DO NOT CONTINUE used in SETUP before degradation note.
C-13: PASS if degradation note is a named FINDINGS section separate from SETUP.
C-14: PASS if whitespace claim cites specific dimension names that appear in C-07 matrix.
C-15: PASS because this VERIFY block is present after FINDINGS, before artifact emission.
C-16: PASS if three distinct mechanisms are named and structurally identifiable.
C-17: PASS if matrix dimension count >= 5. State count.

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
```

---

## V-02: Inertia-first (inertia framing axis)

Axis: Inertia framing -- "current workflow without Signal" is a first-class named competitor
throughout. Row 1 in the matrix. First beat in every contrast. Required element of
anti-positioning.

Hypothesis: Making inertia structurally present in every output element prevents silent
treatment of named tools as the only competition. The 2-beat contrast mandate (inertia
THEN named competitor) is enforced structurally, not stylistically.

```
You are running /scout:positioning.
Inertia framing mandate: the primary competitor is always the "current workflow without
Signal" (inertia). Name it explicitly throughout as a first-class competitor.

Required throughout:
- Every contrast has two beats: (1) inertia contrast -- why change at all?, then
  (2) named-competitor contrast -- why Signal instead of an existing tool.
- Inertia is row 1 in the competitive differentiation matrix.
- Anti-positioning must include at least one "Signal is NOT staying with the current
  workflow" statement.
- Messaging hierarchy PRIMARY must address the inertia buyer (not the tool-switcher).

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified, inertia named
as primary threat").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Inertia is the default primary competitor; named tool alternatives are unverified
  - Whitespace claim cannot confirm which named tools occupy which matrix positions;
    inertia framing will be accurate but tool-level differentiation is provisional
  - Table stakes are unverified; PARTIAL verdicts in PM reality check may be missed
  All claims follow. Run /scout:competitors for named-competitor grounding.

  Then identify 3-5 named competitors inline and continue. Inertia ("current workflow,
  no tool") is always matrix row 1, regardless of source.
--- END SETUP ---

--- EXECUTE ---
Four roles. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the ownable space. Name one category Signal cannot own and why.
  (b) Inertia contrast (required, first): "Without Signal, teams [X]; with Signal, [Y]."
      Addresses why anyone should change their workflow at all.
  (c) Named-competitor contrast (required, second): "[Competitor] does [X]; Signal does [Y]."
      Addresses why Signal over an existing tool.
  Both in contrast form. Feature lists fail. Inertia contrast ALWAYS precedes
  named-competitor contrast. Both required -- not one or the other.

GTM: For each audience in the invocation, one positioning statement.
  Each statement has two sub-beats:
  (1) Inertia sub-beat -- what this audience currently does without Signal and what changes.
  (2) Tool sub-beat -- how Signal differs from a tool they might already use.
  Audience framing required. Reusing a statement for two audiences fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  The table must include at least one claim drawn from the inertia contrast.

DESIGN:
  - Messaging hierarchy: PRIMARY (labeled PRIMARY) targets the inertia buyer -- someone
    not using any investigation tool today. SECONDARY messages (each labeled SECONDARY)
    address the tool-switching case per audience. Explicit labels required. Flat lists fail.
  - Anti-positioning: 2+ statements. The first must be:
    "Signal is NOT staying with the current workflow -- [why inertia is a plausible
    non-choice and what it costs]."
    Additional statements name tool categories a prospect could genuinely confuse Signal with.
--- END EXECUTE ---

--- FINDINGS ---

1. CATEGORY AND DIFFERENTIATOR
   Category: [ownable category name]
   Rejected category: [name] -- [why Signal cannot own it]
   Inertia contrast: [one sentence -- beat 1: why change at all?]
   Named-competitor contrast: [one sentence -- beat 2: why Signal over [competitor]?]
   Primary threat: Inertia / [Named competitor] -- state which is primary and why

2. PER-AUDIENCE POSITIONING STATEMENTS
   [One subsection per audience.
    Each subsection: (a) inertia sub-beat, (b) tool sub-beat, (c) framing signal --
    1-2 words naming what makes this statement distinct from the others.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message -- targets inertia buyer; works without any tool context]
   SECONDARY:
     [Audience]: [message -- tool-switching case]
     [Audience]: [message -- tool-switching case]

4. COMPETITIVE DIFFERENTIATION MATRIX
   Rows: Inertia (current workflow, no tool) [ALWAYS FIRST], Signal, [named competitors]
   Columns: [5+ product-relevant dimensions. Choose from: pre-build vs post-build,
     artifact-producing, zero accounts required, CLI-native, investigation-focused,
     team-workflow integration, decision-support vs code-generation, multi-contributor,
     async evidence trail.]
   Scale: H / M / L
   [Source: loaded artifact [filename] / inline analysis]

5. ANTI-POSITIONING
   Signal is NOT staying with the current workflow -- [why inertia is a plausible
     non-choice and what it costs the team]
   Signal is NOT [X] -- [why this tool confusion is plausible]
   [2 minimum; inertia statement is required as one of them]

6. WHITESPACE
   Claim: [one uncontested space -- neither inertia nor any named tool owns it]
   Dimensions tested: [name the specific matrix columns where Signal is H and no
     other row -- including inertia -- is H. Falsifiable by column inspection.]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Gap type |
   |-------|---------|--------|----------|
   [3+ rows; at least one claim from the inertia contrast; Gap type required]

8. DEGRADATION NOTE
   [If prior run missing: specific risks named, including which inertia positions
    could not be verified against named competitor data]
   [If prior run loaded: N/A -- source: [filename]]
--- END FINDINGS ---

--- VERIFY ---
PASS or FLAG each section.

1. Category/differentiator: PASS if two contrast sentences present (inertia beat first,
   named competitor beat second), both in contrast form. Feature list = FLAG.
2. Per-audience: PASS if every named audience has inertia sub-beat + tool sub-beat +
   distinct framing signal.
3. Messaging hierarchy: PASS if PRIMARY targets inertia buyer; SECONDARY addresses
   tool-switching; explicit labels present.
4. Matrix: PASS if tabular, inertia is row 1, Signal + 2+ named competitors,
   5+ dimensions, H/M/L. Count dimensions.
5. Anti-positioning: PASS if inertia statement present as one of 2+ statements.
6. Whitespace: PASS if specific matrix columns cited; inertia row tested; falsifiable.
7. PM reality check: PASS if 3+ rows; at least one inertia-contrast claim; gap type present.
8. Degradation note: PASS if specific risks named (not "quality may vary") OR prior run loaded.

MATRIX DIMENSION COUNT: [list dimensions] -- Count: [N]. PASS if N >= 5.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific adjustments with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  inertia_framing: enabled
  verify_status: [pass / flagged-N]
```

---

## V-03: Pre-flight GATE + post-FINDINGS VERIFY (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- two explicit quality gates. GATE before EXECUTE validates
setup completeness. VERIFY after FINDINGS validates output quality. A blocked GATE stops
execution before any positioning work begins.

Hypothesis: Separating quality enforcement into two distinct phases catches different failure
modes at different points. GATE catches input-level failures (no audiences named, no topic,
fewer than 2 competitors) before the LLM invests in positioning. VERIFY catches output-level
failures before emission. Two-phase enforcement is more robust than single-phase because the
failure modes are structurally different.

```
You are running /scout:positioning. Two explicit quality gates:

GATE (before EXECUTE): validates that inputs are complete enough to run.
  gate_status: pass / blocked-N goes into frontmatter.
  A blocked GATE stops execution. Do not proceed to EXECUTE until resolved.

VERIFY (after FINDINGS): validates that output meets rubric pass conditions.
  verify_status: pass / flagged-N goes into frontmatter.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace claim will cite only inline analysis -- positions are provisional
  - Table stakes are unverified; PARTIAL verdicts may be missed
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- GATE ---
Before EXECUTE, check setup completeness. Emit each gate item on a labeled line.

G-01: Prior run: [Loaded: [filename] / Missing: degradation note emitted above]
G-02: Audiences: [list audiences named in the invocation / FLAG if none named]
G-03: Topic: [topic from invocation / FLAG if absent]
G-04: Competitor count: [N competitors available for matrix -- from artifact or inline.
      FLAG if fewer than 2.]

gate_status: pass -- if G-01 through G-04 are all present and non-flagged.
gate_status: blocked-N -- if N items are flagged. State what is needed before EXECUTE.

If gate_status: blocked-N -- STOP. Do not proceed to EXECUTE.
If gate_status: pass -- proceed.
--- END GATE ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the ownable space. Name one category Signal cannot own and why.
  (b) Core differentiator: one sentence, contrast form required.
      Inertia contrast first: "Without Signal, teams [X]; with Signal, [Y]."
      Named-competitor contrast second: "[Competitor] does [X]; Signal does [Y]."
      Feature list = FAIL. Both contrasts required.

GTM: For each audience confirmed in GATE G-02, one positioning statement.
  Audience framing required. Different emphasis per audience -- not vocabulary variation.
  Developers: technique language. PMs: workflow/evidence language.
  Architects: formal-methods language. Team leads: process-repeatability language.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For INVALID: what in the spec contradicts the claim.

DESIGN:
  - Messaging hierarchy: one PRIMARY (labeled PRIMARY), per-audience SECONDARY (each
    labeled SECONDARY). Explicit labels required. Flat lists fail.
  - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]."
    Name categories a prospect could genuinely confuse Signal with.
    Generic negations ("not a database") do not count.
--- END EXECUTE ---

--- FINDINGS ---
One section per content criterion. A missing section signals a missed criterion.

1. CATEGORY AND DIFFERENTIATOR
   Category: [ownable category name]
   Rejected: [name] -- [why Signal cannot own it]
   Inertia contrast: [one sentence]
   Named-competitor contrast: [one sentence]

2. PER-AUDIENCE POSITIONING STATEMENTS
   [One subsection per audience confirmed in GATE G-02.
    Include the 1-2 framing signals that distinguish each statement from the others.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message]
   SECONDARY:
     [Audience]: [message]
     [Audience]: [message]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Table: Signal + 2+ named competitors. 5+ product-relevant dimensions. H/M/L.]
   [Dimensions: choose 5+ from pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow
    integration, decision-support vs code-generation, multi-contributor,
    async evidence trail.]
   [Source: loaded artifact [filename] / inline analysis]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why this confusion is plausible]
   Signal is NOT [Y] -- [why this confusion is plausible]
   [2 minimum]

6. WHITESPACE
   Claim: [one uncontested space]
   Dimensions tested: [name the specific matrix columns where Signal is H and no
     named competitor is H -- falsifiable by column inspection]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Gap type |
   |-------|---------|--------|----------|
   [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

8. DEGRADATION NOTE
   [If prior run missing: specific risks named precisely, as emitted in SETUP]
   [If prior run loaded: N/A -- source: [filename]]
--- END FINDINGS ---

--- VERIFY ---
Map each FINDINGS section to its pass condition. Emit PASS or FLAG.
FLAG format: "FINDINGS [N]: [criterion name] -- [what fails the pass condition]"

1. Category/differentiator: PASS if ownable category stated; rejected category named;
   two contrast sentences (inertia first, named competitor second) in contrast form.
2. Per-audience: PASS if every audience from GATE G-02 has a distinct statement with
   audience-appropriate framing and different emphasis.
3. Messaging hierarchy: PASS if PRIMARY label present; at least one SECONDARY per audience.
4. Matrix: PASS if tabular; Signal + 2+ competitors; 5+ dimensions; H/M/L.
   Count the dimensions -- state count. FLAG if fewer than 5.
5. Anti-positioning: PASS if 2+ statements name plausible confusion categories.
   Generic negations = FLAG.
6. Whitespace: PASS if specific matrix columns cited by name (not "no competitor occupies
   this space" without naming the columns).
7. PM reality check: PASS if 3+ rows; PARTIAL/INVALID rows include gap type.
8. Degradation note: PASS if specific risks named (not "quality may vary") OR prior run loaded.

GATE REVIEW: Confirm gate_status from GATE phase. If gate was blocked-N, note which
  inputs were resolved inline vs left unresolved.

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
  gate_status: [pass / blocked-N]
  verify_status: [pass / flagged-N]
```

---

## V-04: R2-V05 upgraded (lifecycle + claim-trace + verbatim-VERIFY + 5+ dim)

Axes: Lifecycle phase boundaries (R2 V-05 baseline winner) + source citations on every
claim (R2 V-02) + VERIFY pass conditions expressed in verbatim rubric language + 5+
matrix dimensions (C-17).

Hypothesis: Incremental upgrade of the R2 winner to directly target all three new R3
criteria. Verbatim-VERIFY (pass conditions quoted from the rubric text) should earn full
C-15 credit. 5+ dimension floor captures C-17. Explicit compound enforcement declaration
in VERIFY captures C-16. Should approach the R3 ceiling.

```
You are running /scout:positioning. Three layers of enforcement:
1. Lifecycle phase boundaries are explicit -- complete one phase before moving to the next.
2. Every positioning claim in FINDINGS carries a [Source: ...] annotation.
   Valid types: [Source: matrix -- Signal H/M/L on [dim] vs [competitor] H/M/L],
   [Source: artifact -- [filename]], [Source: spec -- [section]], [Source: inline -- [basis]].
3. After FINDINGS, a VERIFY pass checks each section against verbatim rubric pass conditions
   and emits verify_status in frontmatter.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded: [filename], N competitors identified").
If not found: STOP. Before any other output, emit this as a named FINDINGS section:

  FINDINGS 8: DEGRADATION NOTE
  No scout:competitors artifact found.
  Specific risks:
  - Primary competitor cannot be confirmed (likely inertia, but unverified)
  - Whitespace cannot be grounded in verified competitor positions; citation in
    FINDINGS 6 will be [Source: inline] only -- treat as provisional
  - Table stakes are unverified; PARTIAL verdicts in FINDINGS 7 may be missed
  All source annotations that follow are labeled [Source: inline].
  Run /scout:competitors for richer, source-grounded positioning.

  Then identify 3-5 competitors inline and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles. Do not let one role revise another mid-phase.

STRATEGY:
  (a) Category: name the product space. Must be ownable -- not a category a named
      competitor already claims. State the specific rejected category and why.
      Annotate: [Source: ...].
  (b) Core differentiator: one sentence, contrast form required.
      Write the inertia contrast first ("Without Signal, teams X; with Signal, Y"),
      then the named-competitor contrast ("[Competitor] does X; Signal does Y").
      Not a feature list. Annotate both: [Source: ...].

GTM: For each audience in the invocation, one positioning statement.
  Different emphasis per audience -- not vocabulary variation on a shared statement.
  Framing: developers get technique language, PMs get workflow/evidence language,
  architects get formal-methods language, team leads get process-repeatability language.
  Each statement cites at least one source. Reusing a statement fails.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID.
  For PARTIAL: what is missing; ahead-of-spec vs unsupported distinction required.
  For each verdict, name the source that determines it.

DESIGN: Messaging hierarchy + anti-positioning.
  - Hierarchy: one PRIMARY (labeled PRIMARY), per-audience SECONDARY (each labeled
    SECONDARY). Explicit labels required. Flat lists fail.
  - Anti-positioning: 2+ "Signal is NOT [X] -- [why this confusion is plausible]."
    Categories a prospect could genuinely confuse Signal with.
    Generic negations fail. Annotate each: [Source: ...].
--- END EXECUTE ---

--- FINDINGS ---
Sections cover all content criteria. Every claim carries a [Source: ...] annotation.
A missing section signals a missed criterion.

1. CATEGORY AND DIFFERENTIATOR
   Category: [ownable category name] [Source: ...]
   Rejected category: [name] -- [why Signal cannot own it] [Source: ...]
   Inertia contrast: [one sentence] [Source: ...]
   Named competitor contrast: [one sentence] [Source: ...]
   Primary threat: [named competitor or inertia]

2. PER-AUDIENCE POSITIONING STATEMENTS
   [One subsection per audience.
    (a) Positioning statement [Source: ...]
    (b) The 1-2 framing signals that distinguish this statement from the others.]

3. MESSAGING HIERARCHY
   PRIMARY: [one message] [Source: ...]
   SECONDARY:
     [Audience]: [message] [Source: ...]
     [Audience]: [message] [Source: ...]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Table: Signal + 2+ named competitors. 5+ product-relevant dimensions. H/M/L scale.]
   [Required dimension pool (choose 5+): pre-build vs post-build, artifact-producing,
    zero accounts required, CLI-native, investigation-focused, team-workflow integration,
    decision-support vs code-generation, multi-contributor, async evidence trail.]
   [Source: loaded artifact [filename] / inline analysis]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why this confusion is plausible] [Source: ...]
   Signal is NOT [Y] -- [why this confusion is plausible] [Source: ...]
   [2 minimum]

6. WHITESPACE
   Claim: [one uncontested space]
   Dimensions tested: [name the specific matrix columns where Signal is H and no
     competitor is H -- cite these columns explicitly to make the claim falsifiable]
   [Source: matrix section 4, dimensions [X] and [Y]]

7. PM REALITY CHECK
   | Claim | Verdict | Reason | Source | Gap type |
   |-------|---------|--------|--------|----------|
   [3+ rows; Gap type: ahead-of-spec / unsupported / N/A]

8. DEGRADATION NOTE
   [If prior run missing: specific risks as emitted in SETUP]
   [If prior run loaded: N/A -- source: [filename]]
--- END FINDINGS ---

--- VERIFY ---
Check each section against its verbatim rubric pass condition. Emit PASS or FLAG.
FLAG format: "FINDINGS [N]: [criterion name] -- [what fails the pass condition]"

1. Category/differentiator: PASS if "a category is stated explicitly" AND "the category
   must NOT be a category a named competitor already owns" AND core differentiator "draws
   a contrast with the primary competitor or inertia." Feature list = auto-FLAG.
2. Per-audience: PASS if "every audience listed in --audiences receives its own statement"
   AND "each statement uses audience-appropriate framing." Reused statement = auto-FLAG.
3. Messaging hierarchy: PASS if "output distinguishes a single primary message" AND
   "hierarchy must be labeled explicitly (PRIMARY / SECONDARY), not inferred from ordering."
4. Competitive matrix: PASS if "matrix covers Signal plus at least one named competitor
   across at least 5 dimensions relevant to the product" AND "tabular form."
   Count dimensions -- state count. Fewer than 5 = auto-FLAG.
5. Anti-positioning: PASS if "at least two anti-positioning statements present" AND
   "grounded in the category definition." Generic negations = auto-FLAG.
6. Whitespace: PASS if "a whitespace claim is stated explicitly" AND "grounded in
   competitor data" AND "cites the specific matrix dimensions or competitor positions."
   Missing dimension citation = auto-FLAG.
7. PM reality check: PASS if "covers at least 3 claims with VALID / PARTIAL / INVALID
   verdicts" AND "PARTIAL rows note gap type." Fewer than 3 rows = auto-FLAG.
8. Degradation note: PASS if prior run missing AND "names the specific risk" (not generic
   warning) OR prior run loaded AND N/A stated. Generic warning = auto-FLAG.

COMPOUND ENFORCEMENT CHECK (C-16):
  Mechanism 1 -- lifecycle ordering: SETUP -> EXECUTE -> FINDINGS -> VERIFY order held.
    [PASS / FLAG]
  Mechanism 2 -- claim-traceability: every FINDINGS claim carries [Source: ...].
    Scan FINDINGS 1-8 for unsourced claims. [PASS / list unsourced claims]
  Mechanism 3 -- pre-artifact VERIFY: this VERIFY block runs before artifact emission.
    [PASS by structural position]
  All three present: [PASS / FLAG -- state which mechanism is missing]

MATRIX DIMENSION COUNT (C-17):
  Dimensions listed: [name them]
  Count: [N] -- PASS if N >= 5 / FLAG if N < 5.

If all PASS: "VERIFY: all criteria pass. Artifact ready."
If any FLAG: list all flags, then "VERIFY: artifact has [N] flags. Recommend revision."
--- END VERIFY ---

AMEND: 3 specific things the user can change, each with concrete output impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md
Frontmatter:
  skill: scout:positioning
  topic: [topic from invocation]
  date: [date]
  source_competitors: [filename or "none"]
  verify_status: [pass / flagged-N]
  matrix_dimensions: [list of dimension names]
  enforcement_layers: lifecycle,claim-trace,verbatim-verify
```

---

## V-05: Full-stack (rubric-mirror-17 + compound declaration + verbatim-VERIFY + inertia-first + 5+ dim)

Axes: 17-criteria FINDINGS structure (V-01 R3) + three enforcement mechanisms explicitly
declared in preamble (C-16) + VERIFY pass conditions verbatim from rubric (C-15) + inertia
as first-class matrix row (V-02 R3) + 5+ matrix dimensions (C-17).

Hypothesis: Maximum compound stacking and maximum structural completeness combined. Unlike
R2 V-05 where compound enforcement was structural but unlabeled, R3 V-05 names all three
mechanisms explicitly in the preamble AND confirms them in VERIFY. 17-criteria sections
resolve the C-11 gap from R2 (sections 1-8 weren't 1:1 to criteria). Inertia-first framing
sharpens C-04/C-05/C-10 without adding structural overhead. Should be the R3 ceiling.

```
You are running /scout:positioning.

Three enforcement mechanisms are declared upfront:
  MECHANISM 1 (lifecycle ordering): SETUP -> EXECUTE -> FINDINGS -> VERIFY.
    Each phase completes before the next begins. Phase order prevents role contamination.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17 force
    criterion-complete output. A missing section IS the signal a criterion was skipped.
  MECHANISM 3 (pre-artifact VERIFY): explicit PASS/FLAG check against verbatim rubric pass
    conditions after FINDINGS, before artifact emission. Catches failures at production time.

These three mechanisms are independent. Each defends a different failure mode.
Confirm all three in VERIFY.

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
   separate from SETUP instructions. This repetition is required -- SETUP prose is
   subject to LLM compression; the note must appear in FINDINGS to survive to output.]
  [If prior run loaded: N/A -- source: [filename]]

FINDINGS C-14: WHITESPACE CITATION OBLIGATION
  Dimensions cited in C-10: [repeat the dimension list from FINDINGS C-10]
  Each dimension appears as a named column in FINDINGS C-07: [PASS / FLAG -- list any
  that do not appear in the matrix]

FINDINGS C-15: PRE-ARTIFACT VERIFY PASS (META)
  VERIFY phase: present after FINDINGS, before artifact emission.
  verify_status: will be set in frontmatter based on VERIFY result.

FINDINGS C-16: COMPOUND ENFORCEMENT STACKING (META)
  MECHANISM 1 (lifecycle): SETUP enforces prior-run load; EXECUTE enforces role order;
    FINDINGS enforces criterion coverage; VERIFY enforces quality gate. Phase order
    prevents downstream contamination from incomplete upstream work.
  MECHANISM 2 (structural mandate): 17 FINDINGS sections labeled C-01 through C-17.
    A missing section is detectable by counting. Criterion omission cannot be silent.
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

C-01: PASS if "prior run is loaded and confirmed" OR "degradation note emitted before
  any positioning output, with specific risks named."
C-02: PASS if "every audience listed in --audiences receives its own statement" AND
  "each statement uses audience-appropriate framing." Reused statement = auto-FLAG.
C-03: PASS if "a category is stated explicitly" AND "the category must NOT be a category
  a named competitor already owns." Incoherence with C-05 = FLAG.
C-04: PASS if "one differentiator is elevated above the others and stated in plain language,
  not feature-list form" AND "draws a contrast with the primary competitor or inertia."
  Feature list = auto-FLAG. Missing inertia beat = FLAG.
C-05: PASS if "at least two anti-positioning statements present" AND "grounded in the
  category definition." Generic negations = auto-FLAG. Missing inertia statement = FLAG.
C-06: PASS if "covers at least 3 claims with VALID / PARTIAL / INVALID verdicts" AND
  "claims marked PARTIAL must note what is missing and whether the gap is ahead-of-spec
  or simply unsupported." Fewer than 3 rows = auto-FLAG.
C-07: PASS if "matrix covers Signal plus at least one named competitor" AND "5+
  dimensions relevant to the product" AND "tabular form." Inertia row present.
  Count dimensions -- state count. Fewer than 5 = auto-FLAG.
C-08: PASS if "output distinguishes a single primary message" AND "hierarchy must be
  labeled explicitly (PRIMARY / SECONDARY), not inferred from ordering."
  PRIMARY targets inertia buyer. Flat list = auto-FLAG.
C-09: PASS if prior run missing AND "names the specific risk" (not "output may be lower
  quality") OR prior run loaded AND N/A stated. Generic warning = auto-FLAG.
C-10: PASS if "a whitespace claim is stated explicitly" AND "grounded in competitor data"
  AND "cites the specific matrix dimensions or competitor positions that support it."
  Missing dimension citation = auto-FLAG. Inertia row tested.
C-11: PASS if all 17 FINDINGS sections C-01 through C-17 are present. Count.
C-12: PASS if STOP/HALT/DO NOT CONTINUE was the verb in SETUP before degradation note.
C-13: PASS if "degradation note appears in a named FINDINGS section" AND "separate from
  both SETUP instructions and positioning output." SETUP-only = auto-FLAG.
C-14: PASS if "whitespace claim names the specific dimensions tested" AND "each cited
  dimension appears as a column in the matrix." Vague citation = auto-FLAG.
C-15: PASS because this VERIFY block is structurally present after FINDINGS.
C-16: All three mechanisms present and named.
  Mechanism 1 (lifecycle): [PASS / FLAG]
  Mechanism 2 (structural mandate): [PASS / FLAG]
  Mechanism 3 (pre-artifact VERIFY): [PASS by position]
  [PASS / FLAG -- state count of mechanisms present]
C-17: Dimension count from FINDINGS C-07: [N]. PASS if N >= 5 / FLAG if N < 5.

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
  inertia_framing: enabled
  enforcement_layers: lifecycle,structural-mandate,verbatim-verify
```

---

**Key R3 design decisions:**
- V-01 extends the rubric-literal axis to all 17 criteria -- meta-criteria sections force structural self-reporting
- V-02 makes inertia a structural requirement, not a stylistic preference -- matrix row 1, 2-beat contrast, required anti-positioning element
- V-03 introduces a GATE phase (pre-EXECUTE input validation) distinct from VERIFY (post-FINDINGS output validation) -- tests whether two-phase enforcement beats single-phase
- V-04 is the direct incremental upgrade of R2 V-05 -- verbatim-VERIFY + 5+ dimensions added to the proven R2 winner
- V-05 combines maximum structural completeness (17 sections) + maximum behavioral density (all 3 mechanisms declared + verbatim-VERIFY + inertia-first) -- the R3 ceiling attempt
- Only V-05 names all three enforcement mechanisms explicitly in the preamble AND confirms them in VERIFY -- testing whether declarative compound stacking beats implicit compound stacking (R2 V-05)
