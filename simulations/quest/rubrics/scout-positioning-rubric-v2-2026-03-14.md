Written to `simulations/quest/rubrics/scout-positioning-rubric-v2-2026-03-14.md`.

---

**What changed from v1 to v2:**

4 new aspirational criteria extracted from the R1 scorecard JSON:

| ID | Criterion | Source pattern |
|----|-----------|---------------|
| C-11 | Output structure mirrors rubric | V-05: numbered FINDINGS sections = rubric checklist; omission visible by inspection |
| C-12 | STOP enforcement verb | V-05 vs V-01-04: "STOP and emit" vs "if not found, emit" -- hard stop prevents silent continuation |
| C-13 | Dedicated FINDINGS section for degradation | V-05: degradation note in named FINDINGS section, not SETUP prose (LLM compression risk) |
| C-14 | Whitespace citation obligation | V-05: cite specific matrix dimensions; makes whitespace claim falsifiable |

**Two fixes to existing criteria:**
- C-04: "contrast form is required, not preferred" -- closes the V-01 failure where "preferred" allowed a PARTIAL
- C-08: pass condition now requires explicit labels (PRIMARY / SECONDARY), not just ordering

**Scoring:** Max bumps from 100 to 140. Essential/recommended weights unchanged. Aspirational tier grows from 2 to 6 criteria (20 pts → 60 pts), reflecting that structural enforcement is now a first-class quality dimension.
 one-to-one to criteria *(new, R1)*
- C-12: STOP enforcement verb -- hard-stop verb for prior-run failure, not conditional language *(new, R1)*
- C-13: Dedicated FINDINGS section for degradation note -- separates diagnostic from positioning output *(new, R1)*
- C-14: Whitespace citation obligation -- cites specific matrix dimensions, not just "competitor data" *(new, R1)*

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

## Aspirational Criteria (60 pts total)

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
rubric criterion (e.g. FINDINGS 1: Category/Differentiator, FINDINGS 2: Per-Audience Statements,
etc.). When a criterion is not applicable or cannot be met, the section is still present with an
explicit note. A flat prose output with no named sections, or a single undifferentiated FINDINGS
block, fails this criterion. The value: a missing section IS the signal that a criterion was
skipped -- no checklist pass required.

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
FINDINGS 8: DEGRADATION NOTE) that is separate from both SETUP instructions and positioning output.
A degradation note buried in SETUP prose fails this criterion even if the note text itself is
accurate -- setup prose is subject to LLM compression when producing the deliverable, and the
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

**N_essential** = 5 (50 pts) | **N_recommended** = 3 (30 pts) | **N_aspirational** = 6 (60 pts)
**Max score v2** = 140 | **Max score v1** = 100

**all_essential_pass**: requires C-01 through C-05 all PASS (no PARTIAL, no FAIL).
Auto-fail: C-01 silent skip regardless of all other scores.
