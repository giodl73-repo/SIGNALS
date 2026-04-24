Written to `simulations/quest/rubrics/scout-positioning-rubric-v4-2026-03-14.md`.

---

**What changed from v3 to v4:**

2 new aspirational criteria from the R3 JSON patterns:

| ID | Criterion | Tier | Key insight |
|----|-----------|------|-------------|
| C-18 | Preamble mechanism declaration | aspirational/behavior | MECHANISM 1/2/3 declared before any phase begins; implicit compound (R2 V-05) required inferring the layers; declarative compound (R3 V-05) announces the quality architecture in the first section |
| C-19 | Verbatim-VERIFY pass conditions | aspirational/behavior | VERIFY block quotes rubric pass condition text verbatim; paraphrased-VERIFY caps at 8/10; condensed language introduces threshold drift where borderline passes get rationalized |

**Scoring progression:**

| Version | Max | N_aspirational |
|---------|-----|---------------|
| v1 | 100 | 2 |
| v2 | 140 | 6 |
| v3 | 170 | 9 |
| v4 | **190** | **11** |

**Key structural note on C-18 vs C-16:** C-16 (compound stacking) is satisfied when three mechanisms are *identifiable*. C-18 is satisfied only when they are *declared in a preamble before SETUP*. V-01 (R3) had compound mechanisms inside FINDINGS meta sections -- that earns C-16 but not C-18. The distinction is auditability-before-reading.

**Key structural note on C-19 vs C-15:** C-15 is satisfied when a VERIFY block exists with a verify_status record. C-19 is satisfied only when the VERIFY text quotes rubric pass conditions verbatim. V-01 capped at 8/10 on C-15 precisely because of paraphrased VERIFY -- C-19 codifies that gap as its own criterion.

**Behavioral criterion density:** 6 of 11 aspirational criteria now enforce *how the skill reasons*, not what it outputs. The v4 frontier (22 points above R3's best score) is entirely behavioral.
 the
ceiling is structural, not behavioral.

**Scoring progression:**

| Version | Max | N_aspirational | Key addition |
|---------|-----|---------------|-------------|
| v1 | 100 | 2 | baseline |
| v2 | 140 | 6 | R1: structural enforcement (C-11 to C-14) |
| v3 | 170 | 9 | R2: VERIFY gate (C-15), compound stacking (C-16), 5+ matrix floor (C-17) |
| v4 | 190 | 11 | R3: preamble declaration (C-18), verbatim-VERIFY (C-19) |

The aspirational tier now has 6 behavioral criteria (C-12, C-13, C-15, C-16, C-18, C-19) -- more
than half of aspirational. The R3 signal: the gap between 168 and 190 is entirely behavioral, not
content. V-05 reached the content ceiling; the remaining 22 points require declaring and quoting
the quality architecture, not improving the positioning output.

---

## Essential Criteria (50 pts total)

### C-01 | Prior Run Handling | essential | behavior

**Text**: When a prior `scout:competitors` run exists, it is loaded. When it does not, the skill
falls back explicitly rather than continuing silently.

**Pass condition**: The skill either (a) loads the prior run and names the file, or (b) emits an
explicit degradation note that names the specific positioning risk before producing any output.
Silent continuation -- producing positioning output without acknowledging missing competitor data --
is an auto-fail regardless of output quality.

---

### C-02 | Per-Audience Positioning Statements | essential | coverage

**Text**: A distinct positioning statement is produced for each audience named in the invocation.

**Pass condition**: Every audience listed in `--audiences` receives its own statement. Each statement
uses audience-appropriate framing -- developers get technique language, PMs get workflow/evidence
language, architects get formal-methods language, team leads get process-repeatability language.
Reusing the same statement for two audiences is a fail.

---

### C-03 | Category Definition | essential | correctness

**Text**: Output names the product category Signal occupies, and that category is one Signal can own.

**Pass condition**: A category is stated explicitly (e.g. "pre-commit investigation tool"). The
category must NOT be a category a named competitor already owns (e.g. "AI coding assistant" or
"testing framework"). The category framing must be consistent with the anti-positioning section.

---

### C-04 | Core Differentiator | essential | correctness

**Text**: Output states a single, memorable competitive differentiator that survives the "so what?" test.

**Pass condition**: One differentiator is elevated above the others and stated in plain language, not
feature-list form. It must draw a contrast with the primary competitor or inertia (e.g. "Coding
assistants prevent bad code. Signal prevents bad decisions."). A list of five equal bullet points
with no hierarchy is a fail. Contrast form is required, not preferred.

---

### C-05 | Anti-Positioning | essential | correctness

**Text**: Output explicitly names things Signal is NOT.

**Pass condition**: At least two anti-positioning statements present (e.g. NOT a testing framework,
NOT a code generator, NOT an autonomous agent). Anti-positioning must be grounded in the category
definition -- items named should be categories a prospect might plausibly confuse Signal with.
Generic negations ("not a database") do not count.

---

## Recommended Criteria (30 pts total)

### C-06 | PM Reality Check | recommended | depth

**Text**: Claims made in positioning are spot-checked against what the spec actually supports.

**Pass condition**: A reality-check table (or equivalent) covers at least 3 claims with VALID /
PARTIAL / INVALID verdicts and a brief reason for each PARTIAL or INVALID. Claims marked PARTIAL
must note what is missing (e.g. "claim ahead of spec -- composite score not in v1") and whether
the gap is ahead-of-spec or simply unsupported. Absence of any reality check is a fail for this
criterion.

---

### C-07 | Competitive Differentiation Matrix | recommended | depth

**Text**: A structured comparison maps Signal against competitors across multiple dimensions.

**Pass condition**: Matrix covers Signal plus at least one named competitor across at least 3
dimensions relevant to the product (e.g. "pre-build vs post-build", "CLI-native", "zero accounts",
"artifact-producing"). Matrix must be in tabular form. A prose paragraph describing differences
does not satisfy this criterion.

---

### C-08 | Messaging Hierarchy | recommended | format

**Text**: Messages are ordered -- a primary message, then per-audience secondary messages, not a
flat list.

**Pass condition**: Output distinguishes a single primary message (works for any audience, top of
the hierarchy) from audience-specific secondary messages. The hierarchy must be labeled explicitly
(e.g. PRIMARY / SECONDARY), not inferred from ordering. Flat lists of positioning statements
without hierarchy labels fail this criterion.

---

## Aspirational Criteria (110 pts total)

### C-09 | Degradation Quantification | aspirational | behavior

**Text**: When no prior `scout:competitors` run exists, the output quantifies what positioning
quality was lost.

**Pass condition**: The degradation note (required by C-01) goes further than "competitors run
missing." It names the specific risk: e.g. "primary competitor is likely inertia, but without
scout:competitors we cannot confirm whitespace or table stakes -- differentiation claims are
provisional." Generic "output may be lower quality" warnings do not satisfy this criterion.

---

### C-10 | Whitespace Identification | aspirational | depth

**Text**: Output identifies at least one uncontested positioning space competitors have not claimed.

**Pass condition**: A whitespace claim is stated explicitly -- an area where no named competitor has
a strong position and Signal can move without direct confrontation. The claim must be grounded in
competitor data (loaded prior run or inline analysis), not asserted without evidence.

---

### C-11 | Output Structure Mirrors Rubric Criteria | aspirational | structure

*Added v2 from R1 excellence signal: "findings-section structure mirrors rubric criteria --
numbered FINDINGS sections map one-to-one to rubric criteria, making omission visible by
inspection."*

**Text**: The output's FINDINGS sections are organized so that each rubric criterion has a
corresponding named section, making criterion omission detectable by structure inspection rather
than content review.

**Pass condition**: Output contains named or numbered FINDINGS sections that correspond to each
rubric criterion (e.g. FINDINGS C-01 through FINDINGS C-17, labeled with criterion IDs). When a
criterion is not applicable or cannot be met, the section is still present with an explicit note.
A flat prose output with no named sections, or a single undifferentiated FINDINGS block, fails this
criterion. The maximum-scoring form labels sections C-01 through C-NN matching rubric IDs exactly,
so that a reviewer can confirm coverage by counting sections. The value: a missing section IS the
signal that a criterion was skipped -- no checklist pass required.

---

### C-12 | STOP Enforcement Verb for Prior-Run Failure | aspirational | behavior

*Added v2 from R1 excellence signal: "STOP enforcement verb for prior-run handling -- stronger than
conditional emit; prevents silent continuation with degraded output."*

**Text**: When the prior scout run is missing, the prompt instruction uses a hard-stop verb before
the degradation note, not conditional or soft language.

**Pass condition**: The instruction for prior-run failure uses a hard-stop verb (STOP, HALT, DO NOT
CONTINUE) before emitting the degradation note. Conditional language ("if not found, emit then
continue") or soft language ("you may note this and proceed") does not satisfy this criterion. The
enforcement verb must prevent any positioning output from appearing before the degradation note is
emitted. The distinction matters because conditional language allows the LLM to assess the gap as
minor and continue silently with degraded output.

---

### C-13 | Dedicated FINDINGS Section for Degradation Note | aspirational | behavior

*Added v2 from R1 excellence signal: "dedicated degradation-note section in FINDINGS -- separates
diagnostic from positioning output, ensures the note survives LLM compression of setup prose."*

**Text**: When a prior run is missing, the degradation note appears in a named FINDINGS section,
not embedded in SETUP instructions.

**Pass condition**: The degradation note occupies a dedicated, numbered FINDINGS section (e.g.
FINDINGS C-13: DEGRADATION NOTE) that is separate from both SETUP instructions and positioning
output. A degradation note buried in SETUP prose fails this criterion even if the note text itself
is accurate -- setup prose is subject to LLM compression when producing the deliverable, and the
degradation note must appear in the output, not the instructions.

---

### C-14 | Whitespace Citation Obligation | aspirational | depth

*Added v2 from R1 excellence signal: "citation obligation for whitespace -- require citing specific
matrix dimensions, making the whitespace claim falsifiable."*

**Text**: The whitespace claim (C-10) cites the specific matrix dimensions or competitor positions
that support it, making the claim falsifiable by a reviewer.

**Pass condition**: The whitespace claim names the specific dimensions tested (e.g. "no competitor
is H on pre-build investigation and artifact traceability -- this space is uncontested"). A claim
that says "no named competitor occupies this space" without naming the dimensions used to test that
claim fails. A claim that says "grounded in competitor data" without citing which dimensions were
examined fails. The citation obligation distinguishes a researched whitespace claim from an asserted
one.

---

### C-15 | Pre-Artifact VERIFY Pass | aspirational | behavior

*Added v3 from R2 excellence signal: "VERIFY pass as pre-artifact quality gate -- explicit
self-check maps each FINDINGS section to its rubric pass condition before emitting; catches
criterion failures at production rather than review time."*

**Text**: Before emitting any output, the skill performs an explicit self-check that maps each
FINDINGS section to its rubric pass condition and records the result.

**Pass condition**: A VERIFY step is present in the skill's phase structure (after FINDINGS, before
emission) that tests each FINDINGS section against its criterion's stated pass condition. The result
is recorded as `verify_status: pass` or `verify_status: flagged-N` in output frontmatter or a VERIFY
header. Skills that emit output without a pre-emission quality gate do not satisfy this criterion.
The key distinction: VERIFY catches criterion failures at production time -- when the LLM can still
revise -- not at review time, when revision requires a full re-run. See C-19 for the scoring
difference between verbatim and paraphrased VERIFY.

---

### C-16 | Compound Enforcement Stacking | aspirational | behavior

*Added v3 from R2 excellence signal: "compound enforcement stacking (lifecycle + claim-trace +
self-verify) approaches rubric ceiling -- three-layer redundancy beats single-axis optimization for
high-complexity skills."*

**Text**: The skill combines at least three independent enforcement mechanisms rather than
optimizing one axis deeply.

**Pass condition**: Three distinct enforcement mechanisms are identifiable in the skill structure.
Canonical examples: (1) lifecycle ordering -- SETUP enforces prior-run load before FINDINGS begin;
(2) claim-traceability -- each claim annotated with `[Source: ...]` making unsupported claims
detectable; (3) pre-artifact VERIFY -- explicit pass/fail check against rubric conditions before
emission. A skill with one very deep mechanism (e.g. exhaustive 5-dimension matrix) but no
redundancy does not satisfy this criterion. Three-layer redundancy matters because each layer
catches a different failure mode: ordering prevents contamination, tracing prevents unsupported
claims, verify prevents criterion omission. No single mechanism defends against all three. See C-18
for the additional scoring distinction between declared and implicit compound stacking.

---

### C-17 | Matrix Dimension Floor of 5+ | aspirational | depth

*Added v3 from R2 excellence signal: "matrix dimension floor of 5+ yields more defensible
whitespace claims -- mandating more dimensions forces ground-truthing on more axes, making C-10
citation falsifiable by a wider reviewer."*

**Text**: The competitive differentiation matrix mandates at least 5 dimensions, not the recommended
minimum of 3.

**Pass condition**: The matrix includes Signal plus at least one named competitor evaluated across
at least 5 dimensions relevant to the product. Dimensions must be distinct and independently
testable (e.g. "pre-build vs post-build", "CLI-native", "zero accounts", "artifact-producing",
"multi-contributor"). A 3-dimension matrix satisfies C-07 (recommended criterion) but does not
satisfy C-17. The higher floor matters for C-14: with 5+ dimensions, a whitespace claim that cites
specific dimensions is testable on more axes, making it harder to assert whitespace that a reviewer
could refute by checking one overlooked dimension.

---

### C-18 | Preamble Mechanism Declaration | aspirational | behavior

*Added v4 from R3 excellence signal: "preamble mechanism declaration makes compound enforcement
auditable before reading output -- naming MECHANISM 1/2/3 upfront announces the quality
architecture; implicit compound (R2 V-05) required inferring the layers, declarative compound (R3
V-05) confirms them before any phase begins."*

**Text**: Before any phase (SETUP, FINDINGS, VERIFY, emission) begins, the skill declares a named
preamble section listing each enforcement mechanism by name and number.

**Pass condition**: A PREAMBLE or MECHANISMS section appears at the top of the skill structure
(before SETUP) that names each enforcement mechanism explicitly (e.g. "MECHANISM 1: lifecycle
ordering -- prior-run load before FINDINGS; MECHANISM 2: claim-traceability -- [Source:] annotation
on every claim; MECHANISM 3: pre-artifact VERIFY -- pass/fail check before emission"). Mechanisms
declared only within FINDINGS meta sections (not in a preamble) satisfy C-16 but do not satisfy
C-18. Mechanisms that are identifiable from reading the full skill but never named explicitly do not
satisfy C-18. The distinction: a preamble declaration announces the quality architecture before the
reader encounters any output -- a reviewer can confirm compound enforcement in the first section
without scanning the full output.

---

### C-19 | Verbatim-VERIFY Pass Conditions | aspirational | behavior

*Added v4 from R3 excellence signal: "verbatim-VERIFY closes the rubric-skill interpretation gap
-- paraphrased-VERIFY scores 8/10 on C-15; verbatim-VERIFY scores 10/10; quoting rubric pass
conditions exactly prevents threshold drift where condensed language rationalizes borderline
passes."*

**Text**: The VERIFY block quotes each rubric pass condition verbatim (or near-verbatim), not in
paraphrased or condensed form.

**Pass condition**: For each criterion tested in the VERIFY step, the pass condition text matches
the rubric's exact wording closely enough that a reviewer can confirm the threshold without
cross-referencing the rubric. A VERIFY that says "PASS if prior run loaded OR degradation note
emitted" (condensed) does not satisfy this criterion -- the rubric pass condition for C-01 specifies
"names the specific positioning risk" and "is an auto-fail regardless of output quality," both of
which disappear in condensed form. A VERIFY that reproduces the rubric's full pass condition
language satisfies this criterion. The mechanism: paraphrased language introduces an interpretation
gap -- condensed pass conditions can rationalize borderline cases as passes by omitting a specific
disqualifier. Verbatim quotation prevents the VERIFY step from becoming a weaker version of the
criterion it is checking.

---

## Scoring Summary

| ID | Criterion | Tier | Category | Max |
|----|-----------|------|----------|-----|
| C-01 | Prior run handling | essential | behavior | 10 |
| C-02 | Per-audience positioning statements | essential | coverage | 10 |
| C-03 | Category definition | essential | correctness | 10 |
| C-04 | Core differentiator | essential | correctness | 10 |
| C-05 | Anti-positioning | essential | correctness | 10 |
| C-06 | PM reality check | recommended | depth | 10 |
| C-07 | Competitive differentiation matrix | recommended | depth | 10 |
| C-08 | Messaging hierarchy | recommended | format | 10 |
| C-09 | Degradation quantification | aspirational | behavior | 10 |
| C-10 | Whitespace identification | aspirational | depth | 10 |
| C-11 | Output structure mirrors rubric | aspirational | structure | 10 |
| C-12 | STOP enforcement verb | aspirational | behavior | 10 |
| C-13 | Dedicated FINDINGS section for degradation | aspirational | behavior | 10 |
| C-14 | Whitespace citation obligation | aspirational | depth | 10 |
| C-15 | Pre-artifact VERIFY pass | aspirational | behavior | 10 |
| C-16 | Compound enforcement stacking | aspirational | behavior | 10 |
| C-17 | Matrix dimension floor of 5+ | aspirational | depth | 10 |
| C-18 | Preamble mechanism declaration | aspirational | behavior | 10 |
| C-19 | Verbatim-VERIFY pass conditions | aspirational | behavior | 10 |

**N_essential** = 5 (50 pts) | **N_recommended** = 3 (30 pts) | **N_aspirational** = 11 (110 pts)
**Max score v4** = 190 | **Max score v3** = 170 | **Max score v2** = 140 | **Max score v1** = 100

**all_essential_pass**: requires C-01 through C-05 all PASS (no PARTIAL, no FAIL).
Auto-fail: C-01 silent skip regardless of all other scores.

---

## Behavioral Criterion Density

6 of 11 aspirational criteria (C-12, C-13, C-15, C-16, C-18, C-19) enforce *how the skill reasons*,
not what it outputs. This is the dominant signal across all three rounds: structural quality and
behavioral quality are the same thing. A skill can produce correct positioning output and still fail
C-12 through C-19 entirely if it lacks declared mechanisms, verbatim VERIFY, and hard-stop
enforcement. The content ceiling (C-03, C-09) is reachable; the behavioral ceiling (C-18, C-19) is
the v4 frontier.

---

## Version History

| Version | Max Score | N_aspirational | Key addition |
|---------|-----------|---------------|-------------|
| v1 | 100 | 2 | baseline 10-criterion rubric |
| v2 | 140 | 6 | R1: structural enforcement (C-11 to C-14); C-04/C-08 tightened |
| v3 | 170 | 9 | R2: VERIFY gate (C-15), compound stacking (C-16), 5+ matrix floor (C-17) |
| v4 | 190 | 11 | R3: preamble declaration (C-18), verbatim-VERIFY (C-19) |
