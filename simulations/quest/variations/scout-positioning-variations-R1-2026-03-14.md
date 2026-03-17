Written to `simulations/quest/variations/scout-positioning-variations-R1-2026-03-14.md`.

---

## Variations: scout-positioning R1

**Single-axis (3):**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Baseline | Spec order (Strategy, GTM, PM, Design) — control |
| V-02 | Role sequence | GTM leads; audience framing pulls category/differentiator out rather than asserting them top-down |
| V-03 | Output format | Matrix-dominant; all prose claims must trace to a matrix cell |

**Combined-axis (2):**

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-04 | Inertia framing + phrasing register | Lead with "why change at all?"; conversational second-person register |
| V-05 | Lifecycle emphasis + findings-first | Explicit phase boundaries; findings section is the deliverable, setup/execute are inputs |

**Key design decisions across all five:**
- C-01 (prior run handling) is in SETUP in every variation — never optional
- V-03 is the only variation that makes the matrix the structural anchor rather than a findings artifact
- V-04 is the only variation that names inertia before named competitors in every role pass
- V-05 is the only variation with labeled `--- SETUP --- / --- EXECUTE --- / --- FINDINGS ---` boundary markers, testing whether explicit phase walls improve role separation or just add verbosity
the single core
  differentiator in plain language, contrast form preferred (e.g., "Coding
  assistants prevent bad code. Signal prevents bad decisions.").
- GTM: For each audience named in the invocation, produce a distinct positioning
  statement. Use audience-appropriate framing: developers get technique language,
  PMs get workflow/evidence language, architects get formal-methods language,
  team leads get process-repeatability language. Reusing the same statement for
  two audiences is not permitted.
- PM: Reality-check table. Cover at least 3 claims from the positioning statements
  with VALID / PARTIAL / INVALID verdicts. For PARTIAL or INVALID, state the reason
  and what is missing (e.g., "claim ahead of spec -- composite score not in v1").
- Design: Messaging hierarchy. Identify a single primary message that works across
  all audiences. Then list per-audience secondary messages beneath it. The hierarchy
  must be explicit -- flat lists fail this step.

FINDINGS:
- Anti-positioning: 2+ explicit "Signal is NOT..." statements. Name categories a
  prospect might plausibly confuse Signal with (e.g., NOT a testing framework,
  NOT a code generator). Generic negations ("not a database") do not count.
- Competitive differentiation matrix: tabular, Signal plus 2+ named competitors,
  3+ dimensions relevant to the product.
- If scout:competitors was missing: quantify the degradation -- name the specific
  risk (e.g., "primary competitor is likely inertia, but without scout:competitors
  we cannot confirm whitespace or table stakes -- differentiation claims are
  provisional").
- Whitespace: one uncontested space no named competitor has claimed, grounded in
  competitor data.

AMEND: List 3 things the user can change. For each: what changes in the output.

Write artifact to simulations/scout/positioning/{topic}-positioning-{date}.md with
standard frontmatter.
```

---

## V-02: GTM-leads (role sequence axis)

Axis: Role sequence -- GTM runs first, audience frames everything downstream

Hypothesis: Audience-first ordering forces category definition and differentiator
to emerge from real framing pressure rather than being asserted top-down. GTM going
first may produce more grounded per-audience statements; risk is that Strategy's
category becomes reactive rather than intentional.

```
You are running /scout:positioning. Audience framing drives everything -- run
GTM first, let the per-audience statements pull the category and differentiator
into shape.

SETUP: Locate the most recent scout:competitors artifact in
simulations/scout/competitors/. If found, load it. If not found: emit a degradation
warning naming the specific risk ("without competitor context, differentiation claims
are provisional -- primary competitor is likely inertia, but whitespace and table
stakes cannot be confirmed"), then identify 3-5 competitors inline.

EXECUTE: Run 4 roles in this order:
- GTM: For each audience named in the invocation, produce a distinct positioning
  statement. Each statement must use audience-appropriate framing. Do not write a
  generic statement then vary the vocabulary -- each statement should emphasize a
  different dimension of the product's value.
- Strategy: Read the GTM statements. From them, extract: (1) the product category
  that unifies all audiences -- it must be ownable, not one a named competitor
  already claims; (2) the single core differentiator that threads through all
  audience statements in plain language. If no single differentiator threads through,
  flag the inconsistency rather than inventing one.
- PM: Reality-check table. At least 3 claims, VALID / PARTIAL / INVALID verdicts.
  For PARTIAL or INVALID: reason + what is missing. Flag claims that are ahead of
  the spec.
- Design: Messaging hierarchy. Promote Strategy's core differentiator to primary
  message. Arrange per-audience statements as secondary messages beneath it. Mark
  the hierarchy structure explicitly -- not just ordering.

FINDINGS:
- Anti-positioning: 2+ "Signal is NOT..." statements grounded in the category
  definition from Strategy. Name plausible confusion categories only.
- Competitive differentiation matrix: tabular, Signal plus 2+ named competitors,
  3+ dimensions.
- Whitespace: one uncontested space grounded in competitor data.

AMEND: 3 adjustments with impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md with frontmatter.
```

---

## V-03: Matrix-dominant (output format axis)

Axis: Output format -- competitive differentiation matrix is the primary structure,
prose is derivative

Hypothesis: Leading with the matrix forces explicit grounding for every positioning
claim. Risk is that the matrix structure crowds out narrative coherence and makes
the output harder to use as pitch material.

```
You are running /scout:positioning. Structure the output around the competitive
differentiation matrix -- all positioning claims must trace back to a matrix cell.

SETUP: Locate the most recent scout:competitors artifact in
simulations/scout/competitors/. If found, load it and extract the competitor list.
If not found: degradation warning (name specific risk -- cannot confirm whitespace,
table stakes unverified, differentiation claims provisional), then identify 3-5
competitors inline.

EXECUTE:

Step 1 -- Build the matrix first (Architect + Strategy):
Construct a competitive differentiation matrix with Signal plus all named competitors
as rows and at least 5 dimensions as columns. Dimensions must be product-relevant
(e.g., pre-build vs post-build, artifact-producing, zero accounts, CLI-native,
audience-specific, phase of development lifecycle). Use H/M/L or explicit labels --
no numeric scores.

Step 2 -- Derive positioning from the matrix (Strategy + GTM):
- Category: read the matrix. Which row pattern is unique to Signal? Name the
  category Signal occupies -- it must be supported by at least 2 matrix dimensions
  where Signal is H and no competitor is H.
- Core differentiator: the single dimension where Signal's position is most
  distinctive. State it in plain language contrasting with the nearest competitor.
- Per-audience statements: for each audience named in the invocation, write a
  distinct positioning statement. Each statement must cite 1-2 matrix dimensions
  as its grounding. Audience-appropriate framing required.

Step 3 -- Reality check (PM):
At least 3 claims, VALID / PARTIAL / INVALID. Trace each claim back to its
matrix cell. For PARTIAL or INVALID: reason + what is missing.

Step 4 -- Messaging hierarchy (Design):
Primary message at top, per-audience secondary messages beneath. Mark hierarchy
explicitly.

FINDINGS:
- Anti-positioning: 2+ "Signal is NOT..." statements. Each must correspond to a
  matrix row where a competitor is H and Signal is L or M.
- Whitespace: matrix cells where no competitor is H and Signal is H or could be H.
- If scout:competitors missing: state exactly which matrix columns cannot be reliably
  scored.

AMEND: 3 adjustments with impact.

Artifact: simulations/scout/positioning/{topic}-positioning-{date}.md with frontmatter.
```

---

## V-04: Inertia-primary + conversational register (combined axes)

Axes: Inertia framing (status quo is competitor #1, named throughout) +
phrasing register (conversational imperative, second-person, plain language)

Hypothesis: Naming inertia explicitly as the primary competitor forces every
positioning statement to answer "why change at all?" -- the real objection.
Conversational register may improve clarity for GTM use but may feel less rigorous
for PM or architect audiences.

```
You are running /scout:positioning. The hardest competitor is inertia -- teams
doing nothing, living with the cost of missed design bugs. Name it first. Make
every positioning statement answer: "why change?"

SETUP: Check simulations/scout/competitors/ for the most recent competitors artifact.
If you find one, load it and look specifically at the "none / status quo" row -- that
is your primary competitor. If you don't find one: say so explicitly and name the
specific gap ("can't confirm whitespace or table stakes without a competitors run --
running inline to fill the gap"), then sketch 3-5 competitors quickly before
continuing.

Now work through four lenses:

Strategy -- what is Signal, actually?
Name the category Signal owns. It can't be "AI coding assistant" or "testing
framework" -- those are taken. It has to be a space Signal can move into without
a direct fight. Then write the core differentiator: one sentence, plain language,
contrast form. Compare it against inertia first (why change at all?), then against
the nearest named competitor (why this instead of that?).

GTM -- who are we talking to, and what do they hear?
For each audience: write a positioning statement that speaks their language.
Developers hear about technique and workflow. PMs hear about evidence and decisions.
Architects hear about formal methods and traceability. Team leads hear about
repeatability and process. Don't write one statement and swap out a word -- each
audience needs a genuinely different emphasis.

PM -- does this hold up?
Take at least 3 claims from the positioning statements and check them against
the spec. Mark each VALID, PARTIAL, or INVALID. For anything less than VALID:
say what's missing and whether it's ahead of spec or just unsupported.

Design -- what's the message structure?
Pick the one message that works for any audience and put it at the top. The
per-audience statements go under it as secondary messages. Make the hierarchy
visible -- label the primary message, label the secondary messages. Don't just
order them and hope the reader infers it.

Wrap up with:
- Anti-positioning: at least 2 "Signal is NOT..." lines. Name categories people
  could genuinely confuse it with -- not obvious negations.
- Competitive differentiation matrix: table, Signal plus 2+ competitors, 3+ columns.
- Whitespace: one space no competitor has claimed, grounded in what you found above.
- If no competitors artifact was loaded: be specific about what you couldn't verify
  (whitespace claim, table stakes, differentiation vs. a specific competitor).

What can the user change? Give 3 options, each with a concrete impact statement.

Write the artifact to simulations/scout/positioning/{topic}-positioning-{date}.md.
```

---

## V-05: Lifecycle-explicit + findings-first (combined axes)

Axes: Lifecycle emphasis (each phase labeled and bounded, findings section
carries the weight) + output format (findings-first, setup/execute are abbreviated)

Hypothesis: Making lifecycle phase boundaries explicit reduces ambiguity about
what each role is responsible for. Findings-first ordering mirrors how practitioners
actually consume the output (skip to conclusions). Risk is that abbreviated setup
and execute sections may produce shallower role contributions.

```
You are running /scout:positioning. Each lifecycle phase is bounded -- complete
one before moving to the next. The findings section carries the weight; setup
and execute are inputs to it.

--- SETUP ---
Locate simulations/scout/competitors/ and load the most recent competitors artifact.
If found: confirm load ("Loaded competitors artifact, N competitors identified").
If not found: STOP and emit a degradation note before proceeding. The note must
name the specific positioning risk (not just "quality may vary") -- e.g., "no
scout:competitors run found. Primary competitor is likely inertia, but whitespace
cannot be confirmed and table stakes are unverified. Differentiation claims that
follow are provisional. Run /scout:competitors for richer positioning." Then run
inline competitor identification (3-5 competitors) and continue.
--- END SETUP ---

--- EXECUTE ---
Run each role. Do not merge roles or let one role comment on another during this phase.

STRATEGY: (a) Name the product category. It must be ownable. (b) State the core
differentiator in one sentence, plain language, contrast form. (c) Note the primary
competitive threat and the inertia threat separately.

GTM: For each audience in the invocation, write one positioning statement.
Different emphasis per audience -- not varied vocabulary on a shared statement.

PM: Reality-check table. 3+ claims, VALID / PARTIAL / INVALID, with reasons for
anything less than VALID.

DESIGN: Messaging hierarchy. One primary message. Per-audience secondary messages
beneath it. Mark the hierarchy structure explicitly with labels (PRIMARY / SECONDARY).
--- END EXECUTE ---

--- FINDINGS ---
This section is the deliverable. Structure it as follows:

1. CATEGORY AND DIFFERENTIATOR
   - Category: [ownable category name]
   - Core differentiator: [one sentence]
   - Primary threat: [named competitor or inertia]

2. PER-AUDIENCE POSITIONING
   [One subsection per audience, with the positioning statement and the 1-2
    audience framing signals that make it distinct from the other statements]

3. MESSAGING HIERARCHY
   PRIMARY: [one message]
   SECONDARY (per audience): [labeled list]

4. COMPETITIVE DIFFERENTIATION MATRIX
   [Tabular. Signal + 2+ named competitors. 3+ dimensions. H/M/L scale.]

5. ANTI-POSITIONING
   Signal is NOT [X] -- [why this confusion is plausible]
   Signal is NOT [Y] -- [why this confusion is plausible]
   [2 minimum; more if the category definition creates additional confusion candidates]

6. WHITESPACE
   [One uncontested space. Must be grounded in the matrix above -- cite the
    dimensions that support the claim.]

7. PM REALITY CHECK
   [Table: Claim | Verdict | Reason]

8. DEGRADATION NOTE (if applicable)
   [If scout:competitors was missing: the specific risks that could not be verified,
    named precisely]
--- END FINDINGS ---

AMEND: 3 specific things the user can change, each with a concrete output impact.

Write artifact to simulations/scout/positioning/{topic}-positioning-{date}.md
with standard frontmatter (skill, topic, date, source_competitors if loaded).
```
