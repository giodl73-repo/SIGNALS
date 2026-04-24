Rubric written to `simulations/quest/rubrics/scout-positioning-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (5) — correctness + coverage:**
- C-01: Prior run handling — load it or fall back explicitly; silent skip = auto-fail (from SF-01 MAJOR)
- C-02: Per-audience statements — every named audience, audience-appropriate framing
- C-03: Category definition — ownable category, not one a competitor already claims
- C-04: Core differentiator — one elevated, plain-language contrast (not a feature list)
- C-05: Anti-positioning — 2+ explicit "not this" with plausible confusion candidates

**Recommended (3) — depth + structure:**
- C-06: PM reality check — 3+ claims with VALID/PARTIAL/INVALID verdicts
- C-07: Competitive differentiation matrix — tabular, 3+ dimensions
- C-08: Messaging hierarchy — primary message explicit, not inferred from ordering

**Aspirational (2) — raising the bar:**
- C-09: Degradation quantification — names the specific positioning risk, not just "quality may vary"
- C-10: Whitespace identification — one uncontested space, grounded in competitor data
2 | Per-Audience Positioning Statements | essential | coverage

**Text**: A distinct positioning statement is produced for each audience named in the invocation.

**Pass condition**: Every audience listed in `--audiences` receives its own statement. Each statement
uses audience-appropriate framing -- developers get technique language, PMs get workflow/evidence
language, architects get formal-methods language, team leads get process-repeatability language.
Reusing the same statement for two audiences is a fail.

---

### C-03 | Category Definition | essential | correctness

**Text**: Output names the product category Signal occupies, and that category is one Signal can own.

**Pass condition**: A category is stated explicitly (e.g. "pre-commit investigation tool"). The category
must NOT be a category a named competitor already owns (e.g. "AI coding assistant" or "testing
framework"). The category framing must be consistent with the anti-positioning section.

---

### C-04 | Core Differentiator | essential | correctness

**Text**: Output states a single, memorable competitive differentiator that survives the "so what?" test.

**Pass condition**: One differentiator is elevated above the others and stated in plain language, not
feature-list form. It must draw a contrast with the primary competitor or inertia (e.g. "Coding
assistants prevent bad code. Signal prevents bad decisions."). A list of five equal bullet points with
no hierarchy is a fail.

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
must note what is missing (e.g. "claim ahead of spec -- composite score not in v1"). Absence of
any reality check is a fail for this criterion.

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
the hierarchy) from audience-specific secondary messages. The hierarchy must be explicit, not
inferred from ordering. Flat lists of positioning statements without hierarchy fail this criterion.

---

## Aspirational Criteria (10 pts total)

### C-09 | Degradation Quantification | aspirational | behavior

**Text**: When no prior scout-competitors run exists, the output quantifies what positioning quality
was lost.

**Pass condition**: The degradation note (required by C-01) goes further than "competitors run
missing." It names the specific risk: e.g. "primary competitor is likely inertia, but without
scout-competitors we cannot confirm whitespace or table stakes -- differentiation claims are
provisional." Generic "output may be lower quality" warnings do not satisfy this criterion.

---

### C-10 | Whitespace Identification | aspirational | depth

**Text**: Output identifies at least one uncontested positioning space competitors have not claimed.

**Pass condition**: A whitespace claim is stated explicitly -- an area where no named competitor has
a strong position and Signal can move without direct confrontation. The claim must be grounded in
competitor data (loaded prior run or inline analysis), not asserted without evidence.

---

## Scoring Summary

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Prior run handling | essential | behavior |
| C-02 | Per-audience positioning statements | essential | coverage |
| C-03 | Category definition | essential | correctness |
| C-04 | Core differentiator | essential | correctness |
| C-05 | Anti-positioning | essential | correctness |
| C-06 | PM reality check | recommended | depth |
| C-07 | Competitive differentiation matrix | recommended | depth |
| C-08 | Messaging hierarchy | recommended | format |
| C-09 | Degradation quantification | aspirational | behavior |
| C-10 | Whitespace identification | aspirational | depth |

**N_essential** = 5 | **N_recommended** = 3 | **N_aspirational** = 2
