# quest-rubric Variate — Round 13 (Against rubric v13)
**Date:** 2026-03-15
**Rubric:** v13 (C-01--C-39; adds C-38: self-referential-coverage-demonstration; C-39: competitor-at-verification-step)
**Target criteria:** C-38, C-39, C-11

**Round 13 design note:** Round 12 produced mechanisms for C-35
(tier-divergence-scan-phase), C-36 (competitor-at-construction-step), and C-37
(competitor-criterion-coverage-complete). Rubric v13 adds two aspirational criteria
extracted from Round 12 excellence signals. V-05 of R12 PASSES C-38 (seven competitors
covering C-31--C-37 in bijection, Competitor 7 itself covering C-37 so the count is
self-demonstrating) and PASSES C-39 (Competitor 5: Tier-Blind Categorizer placed inline
at the divergence-check step before the divergence-check format is specified).
V-05 R12 is PARTIAL on C-11: competitors are in negative-space format (what the wrong
form does) but not in the structured Reference / Passes / Fails format that C-11 requires
-- the three-field prior-version anchor stating which criteria the reference satisfies
and the exact dimension where it falls short.

**C-11 vs C-36.** C-36 requires each competitor to be placed at the construction step
where the wrong implementation would most naturally be produced. A V-05 R12 competitor
satisfies C-36 (placed at the correct step) while failing C-11 (no three-field
Reference / Passes / Fails anchor). C-11 requires the aspirational competitor to name
(1) which earlier criteria it passes -- making it a valid contender up to the aspirational
bar -- and (2) the exact dimension where it falls short -- making the aspirational
criterion's target observable without reading the full criterion text. A competitor that
only describes failure behavior satisfies C-36 but not C-11.

**C-38 vs C-37.** C-37 requires one-to-one correspondence between competitors and
novel-requirement aspirational criteria: counts are equal, each criterion has one
competitor, no competitor governs two criteria. C-38 requires that when the criterion
governing this correspondence is itself a novel criterion in the rubric being built,
the bijection be self-demonstrating: an evaluator can count numbered competitor blocks
and confirm coverage without reading criterion or competitor text. A rubric that satisfies
C-37 (bijection exists, confirmed by cross-referencing lists) while failing C-38
(the coverage-completeness criterion's competitor is not distinguishable from the count
alone) is V-05 R12 in a round where C-37 is first introduced as a novel criterion.

**C-39 vs C-36.** C-36 requires competitors at CONSTRUCTION steps. C-39 requires
the same pattern at VERIFICATION steps: the wrong form of verification is named as a
competitor immediately before the correct verification format is specified. V-05 R12
satisfies C-39 at the DIVERGENCE CHECK verification step (Competitor 5: Tier-Blind
Categorizer placed before the divergence check format). C-39 is also satisfiable at
the Phase 4.5 ISOLATION AUDIT step by placing a competitor (the Holistic Audit Reader)
before the six-check structured format. Round 13 tests whether C-39 can be reinforced
at the isolation audit step in addition to the divergence check step.

**Axis selection:**

Three axes map to the three target criteria:
- Output format → C-11: Definer produces a third Anchor template (Reference / Passes /
  Fails at), constraining aspirational competitors to the structured prior-version format
- Inertia framing → C-38: Competitor 8 (Non-Self-Demonstrating Coverage Architect)
  placed inline at the Builder A coverage-completeness check, making the self-referential
  numbering requirement derivable from the competitor description
- Role sequence → C-39 at isolation audit: a new AUDIT-FORM SPECIFIER role between
  Builder E+R and Phase 4.5 introduces the Holistic-Audit-Reader competitor before
  the six-check isolation audit format is specified

Single-axis variations: V-01 (output format), V-02 (role sequence), V-03 (inertia
framing). Combined variations: V-04 (output format + inertia framing), V-05 (output
format + inertia framing + role sequence).

---

## Round 13 Variation Map

| Variation | Axis | C-11 probe | C-38 probe | C-39 probe | Notes |
|-----------|------|-----------|-----------|-----------|-------|
| V-01 | Output format (Anchor template as third Definer output) | Very strong -- Definer produces three templates: Text, Pass, Anchor (Reference / Passes / Fails at); each aspirational competitor must be in Anchor format; a competitor that only describes failure behavior without citing which criteria it passes and the exact dimension it fails is a format violation firing before Builder A completes | Strong (baseline) -- Competitor 7 from R12 V-05 at coverage completeness; V-05 R12 bijection is preserved | Strong (baseline) -- Competitor 5 from R12 V-05 at divergence check; C-39 preserved at divergence-check step | Single-axis; tests whether the Anchor template alone closes C-11 without role-header enforcement; C-38 and C-39 inherited at R12 V-05 strength |
| V-02 | Role sequence (AUDIT-FORM SPECIFIER role before isolation audit) | None -- Definer produces two templates; no Anchor template; aspirational competitors in negative-space format | Strong (baseline) -- Competitor 7 at coverage completeness | Very strong -- AUDIT-FORM SPECIFIER role inserted after Builder E+R, before Phase 4.5; Holistic-Audit-Reader competitor placed inline in this role before the six-check isolation audit format is specified; role cannot complete without the competitor description and the structured audit format | Single-axis; tests whether a dedicated role boundary at the isolation audit step with an inline competitor satisfies C-39 at the isolation-audit level distinct from the divergence-check level |
| V-03 | Inertia framing (Competitor 8: Non-Self-Demonstrating Coverage Architect at coverage-completeness step) | None -- two Definer templates; no Anchor template; C-11 unaddressed | Very strong -- Competitor 8 placed inline at the Builder A coverage completeness check; derivation instruction requires sequential competitor numbering when the coverage-completeness criterion is itself novel; the competitor count = novel-criterion count = verifiable by counting numbered blocks alone | Strong (baseline) -- Competitor 5 at divergence check | Single-axis; tests whether Competitor 8 with sequential numbering instruction produces C-38 PASS without the Anchor template or the isolation-audit role |
| V-04 | Output format + inertia framing (C-11 + C-38) | Very strong -- three Definer templates including Anchor; aspirational competitors in Reference / Passes / Fails at format | Very strong -- Competitor 8 at coverage-completeness step with self-referential numbering | Strong (baseline) -- Competitor 5 at divergence check | Combined; tests whether the Anchor template (C-11) and Competitor 8 (C-38) reinforce each other; C-39 at isolation-audit step ablated to isolate the C-11+C-38 joint effect |
| V-05 | Output format + inertia framing + role sequence (C-11 + C-38 + C-39) | Very strong -- three Definer templates; Anchor format required for aspirational competitors | Very strong -- Competitor 8 at coverage-completeness step; sequential numbering instruction | Very strong -- AUDIT-FORM SPECIFIER role with Holistic-Audit-Reader competitor at isolation-audit step PLUS Competitor 5 (Tier-Blind Categorizer) at divergence-check step; C-39 satisfied at both verification levels | Full combination; ceiling target: all three criteria PASS yields composite 100 if C-11 clears; tests whether all three axes together produce no interference |

---

## V-01 -- Output Format (Anchor Template as Third Definer Output)

**Axis:** Output format -- the Definer produces three slot-fillable templates instead
of two: the Text template (Y/Z/X causal chain), the Pass template (Location/Observable/
Standard), and the Anchor template (Reference / Passes / Fails at) required for all
aspirational competitor definitions. Each aspirational competitor must be in Anchor
format; a competitor that describes failure behavior without naming which criteria it
passes and the exact dimension it fails short is a Definer-gate violation.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric under V-01 will contain aspirational competitors in three-field Anchor format (Reference: / Passes: / Fails at:); a competitor block that has only a failure-behavior description without these three fields is a format violation detectable at the Definer-gate output; C-11 PASS is structural from the first aspirational draft. | The Anchor template changes the character of aspirational competitors from negative-space-only specifications to prior-version references; this constrains the builder to name a reference that passes essential+recommended, which means the reference's full-design validity is acknowledged before the aspirational gap is identified -- generators under V-01 will produce aspirational criteria whose required property is positioned as genuinely beyond the reference, not merely different. | V-04 is the primary comparison site: V-01 has the Anchor template only; V-04 has the Anchor template AND Competitor 8 (C-38); if V-04's aspirational competitors are structurally tighter in the Anchor format dimension, the self-referential count instruction amplifies format compliance; if equivalent, the Anchor template alone is sufficient for C-11. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DEFINER ROLE

Read the skill spec. Produce three binding templates in slot-fillable form. Your sole
output is these three templates.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**Anchor template (slot-fillable, for aspirational competitor definitions only):**

```
Reference: [name of the competitor or prior-version being anchored]
Passes: [C-NN through C-NN -- the essential and recommended criteria this reference satisfies]
Fails at: [the exact dimension where this reference falls short of the aspirational bar -- one sentence naming the observable gap]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any
phrasing -- locates causality in X's consequence: "X causes failure," "failure occurs
when X is present," "X leads to Z," and all semantic equivalents. The Auditor check
function tests causal structure, not pattern matching.

**DEFINER GATE: Three slot-fillable templates (Text, Pass, Anchor). Nothing else.**

STOP CONDITION: A Definer output that contains explanatory commentary, structural notes,
or any content beyond the three required templates is incomplete. Rewrite before Builder
E+R runs. The three templates are the complete output of this role.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log** (minimum 5 entries):

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim.

Five fields per criterion: ID (C-NN, starting at C-01), Text, Weight (essential),
Category (correctness | depth | format | coverage | behavior), Pass (apply Pass template).

**IF INTRODUCING A COMPETITOR FOR ANY ESSENTIAL CRITERION: PLACE THE COMPETITOR BLOCK
IMMEDIATELY BEFORE THAT CRITERION'S DEFINITION. DO NOT GROUP COMPETITORS IN A SHARED
BLOCK. A COMPETITOR NOT AT ITS CONSTRUCTION STEP IS NOT A GAP SPECIFICATION.**

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**IF INTRODUCING A COMPETITOR FOR ANY RECOMMENDED CRITERION: SAME RULE -- PLACE IT
IMMEDIATELY BEFORE THAT CRITERION'S DEFINITION.**

**Post-draft audit.** For each criterion:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

**--- COMPETITOR 5: THE TIER-BLIND CATEGORIZER ---**

The Tier-Blind Categorizer assigns each criterion a category from the menu (correctness |
depth | format | coverage | behavior) and produces a rubric whose criteria are
well-distributed across the menu by design. It grounds tiers in distinct failure
dimensions: essential criteria address broken artifacts, recommended criteria address
quality shortfalls, aspirational criteria address structural gaps. By design, this
produces organic category diversity. The Categorizer notes this expected divergence and
considers C-07 (>= 3 distinct categories) satisfied by construction. It never produces
a named step that counts category assignments per tier and outputs a per-tier distribution
as a verification artifact. An evaluator reading the output cannot confirm that the
expected divergence actually materialized without manually counting categories per tier.
If the expected divergence did not materialize, no STOP fires.

**This competitor IS the gap specification for C-35. From the description above, derive
what the correct implementation must add before reading the operative requirement below.**

After the post-draft audit, run the TIER-DIVERGENCE CHECK:

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise category assignments before proceeding.
  Note: the complete three-tier check (including aspirational) is run at Builder A.
Divergence status (essential + recommended): [PASS / STOP]
```

**BUILDER E+R GATE:** Failure log + essential + recommended + audit report + Divergence
Check output (status = PASS).

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria. Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- at any threshold
  -- is not aspirational. Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator satisfies C-27 and C-28. Before writing any mechanism
definition, it assembles a block of named competitors -- one per novel aspirational
criterion -- and places the block at the start of the aspirational section. Each
competitor correctly constitutes the gap specification. The builder reads all competitors
once at the start of the aspirational role. By the time the builder reaches the mechanism
definition for novel criterion C-NN, the corresponding competitor was encountered forty
lines above during role setup. The competitor is not the first content the builder reads
before committing to the design decision -- it is a recalled item from the opening block.

**This competitor IS the gap specification for C-36. From the description above, derive
what the correct implementation must require about competitor placement before reading
the operative requirement below.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT THE CONSTRUCTION STEP WHERE ITS GAP IS OPERATIONALLY
RELEVANT. DO NOT GROUP COMPETITORS IN A SHARED BLOCK. A COMPETITOR READ AT ROLE STARTUP
IS NOT AT ITS CONSTRUCTION STEP.**

A blank "Criterion affected" cell or generic "Yes, independent" without a C-NN citation
is a format violation. STOP if any such cell exists.

**MECHANISM DEFINER GATE:** Independence Map with non-blank, specific C-NN citation in
every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.

For each aspirational criterion, place a competitor block **immediately before** that
criterion's definition. The competitor block **must be in Anchor template format:**

```
Reference: [name of competitor or prior version being anchored]
Passes: [C-NN through C-NN -- essential and recommended criteria this reference satisfies]
Fails at: [the exact dimension where this reference falls short -- one sentence]
```

A competitor block that describes the wrong behavior without naming which criteria it
passes and the exact dimension it fails is a format violation: the Anchor template
requires all three fields, not a narrative description alone.

**--- COMPETITOR 1 (Anchor format): THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

```
Reference: The Unbounded-Aspirational Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; the protocol
  correctly requires tier count targets of "3-5 essential / 2-3 recommended" with
  STOP conditions for both]
Fails at: the aspirational tier -- the protocol notes that aspirational criteria
  "should be limited in number" but names no upper bound and includes no STOP
  condition; a builder using this protocol may draft three or four aspirational
  criteria without violating the protocol's stated requirements
```

**--- COMPETITOR 2 (Anchor format): THE CATEGORY-MENU PROTOCOL ---**

```
Reference: The Category-Menu Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; the protocol
  lists five category options and correctly constructs criteria with all five fields]
Fails at: category diversity verification -- the protocol advises "a good rubric
  should use diverse categories" but includes no step requiring confirmation that
  >= 3 distinct categories appear before Emit; a builder may produce nominal
  diversity while measuring the same content-quality property
```

**--- COMPETITOR 7 (Anchor format): THE PARTIAL-COVERAGE ARCHITECT ---**

```
Reference: The Partial-Coverage Architect
Passes: [C-01 through C-NN -- all essential and recommended criteria; correctly places
  competitors at their construction steps (C-36); names well-formed competitors for
  the majority of novel aspirational criteria]
Fails at: coverage completeness -- for the criterion introducing the most structurally
  complex construction requirement, the Architect relies on a positive specification
  alone; an evaluator counting competitors cannot determine the novel-criterion count
  from the competitors alone; the third requirement is navigated without a negative-
  space specification
```

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum. Do not draft a third.

Each criterion: five fields (ID continuing from Builder E+R) plus **Fills gap**: [cite
G-NN from Scope Gatekeeper -- required; blank = format error.] After each criterion:
"Is the cited gap in the gap register?" If not, revise.

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Competitors present (Anchor-format blocks, listed by Reference name and C-NN governed):
  [list each] | Count: [N]
Bijection: [counts equal? YES / NO] [each criterion has exactly one Anchor-format
  competitor? YES / NO]
⛔ STOP if any answer is NO.
Coverage status: [PASS / STOP]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential tier:    [cat: N, ...] -- majority: [category]
  Recommended tier:  [cat: N, ...] -- majority: [category]
  Aspirational tier: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
⛔ STOP if N < 2.
Final divergence status: [PASS / STOP]
```

**BUILDER A GATE:** 1-2 aspirational criteria with Anchor-format competitor blocks +
Coverage status = PASS + Final divergence status = PASS.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit.

**Text field checks (3):**
1. Direction: does Text locate causality in Y's absence?
2. Contrast: does Text name X alongside Y?
3. Causal chain: does Text name Z?

**Pass field checks (3):**
4. Location: names artifact location?
5. Observable: names specific count or token?
6. No qualitative-only: avoids unanchored qualitative language?

**--- COMPETITOR 3 (Anchor format): THE FORMULA-ONLY SCORER ---**

```
Reference: The Formula-Only Scorer
Passes: [C-01 through C-NN -- all essential and recommended criteria; states
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0 alongside the composite formula and
  golden threshold; the scoring structure is complete in form]
Fails at: PARTIAL earn conditions -- the specific circumstances under which a
  criterion earns 0.5 rather than 1.0 or 0.0 are never named; two evaluators
  reading the same criterion will assign 0.5 or 0.0 by independent judgment;
  the scoring is not reproducible
```

**--- COMPETITOR 4 (Anchor format): THE DECLARED-INDEPENDENT MAP ---**

```
Reference: The Declared-Independent Map
Passes: [C-01 through C-NN -- all essential and recommended criteria; produces
  a table with "Mechanism name," "What it does," and "Independent?" columns;
  the one-to-one assignment between mechanisms and criteria is asserted]
Fails at: criterion citation -- the "Independent?" column reads "Yes, independent"
  for every row; an evaluator examining the map cannot confirm which criterion each
  mechanism affects without reading the mechanism descriptions and performing the
  matching step manually; the citation is declared but not annotated
```

**Audit report format -- required:**
`C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count (C-31):
  Count: [N] | Bound: 1-2 maximum.
  ⛔ STOP if count > 2.
  Compliant? [YES / NO]

Check B -- Category diversity (C-32):
  Distinct categories: [N] | Requirement: >= 3.
  ⛔ STOP if N < 3.
  Compliant? [YES / NO]
```

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State earn conditions: the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. Competitor 3 above shows what this row looks like when earn conditions are absent. Name the conditions explicitly.] |
| FAIL    | 0.0   | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum of essential values) / N_essential x 60        max 60
Recommended:  (sum of recommended values) / N_recommended x 30    max 30
Aspirational: (sum of aspirational values) / N_aspirational x 10  max 10

Composite = Essential + Recommended + Aspirational                 max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational maximum.

**Golden threshold:** All essential criteria PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Body: purpose statement (2-3 sentences: state the Anchor template principle -- the
Definer produces three binding templates; the Anchor template constrains every
aspirational competitor to the three-field Reference / Passes / Fails at format,
making C-11 satisfaction structural from the first draft; a competitor block without
the Anchor fields is a gate violation detectable before Builder A completes),
then SCOPE DECLARATION (retained), then Coverage Completeness record (Builder A,
retained), then final Divergence Check (Builder A, retained), then criteria ordered
essential -> recommended -> aspirational (Anchor-format competitors retained inline
at their construction steps; Dimension and Fills gap annotations retained; audit
report omitted), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Role Sequence (Audit-Form Specifier Role Before Isolation Audit)

**Axis:** Role sequence -- a dedicated AUDIT-FORM SPECIFIER role runs between Builder
E+R and the Phase 4.5 isolation audit. This role introduces the Holistic-Audit-Reader
competitor inline before the six-check structured isolation audit format is specified.
The role cannot complete without both the competitor description and the structured
format. C-39 is satisfied at the isolation-audit verification step, not only at the
divergence-check step.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric under V-02 will contain a named AUDIT-FORM SPECIFIER role between E+R construction and Phase 4.5 isolation audit; the Holistic-Audit-Reader competitor is the first content in this role; the structured six-check format follows the competitor derivation instruction; C-39 is satisfied at the isolation-audit step (not only at the divergence-check step as in V-05 R12); an evaluator can confirm C-39 at two independent verification steps. | The AUDIT-FORM SPECIFIER role boundary makes the wrong audit form visible before the correct format is committed; this mirrors the pattern V-05 R12 established at the divergence-check step (Competitor 5) and extends it to the field-level audit; rubrics generated under V-02 will show the six-check format preceded by a named wrong-form competitor at the audit role, and the divergence check preceded by Competitor 5 as in the baseline. | V-05 is the primary comparison site: V-02 has the isolation-audit competitor only; V-05 has isolation-audit + Anchor template + Competitor 8; if V-05's C-39 compliance is tighter than V-02's despite identical isolation-audit structure, role-boundary framing or the Anchor template amplifies C-39 compliance. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form --
in any phrasing -- locates causality in X's consequence. Check function tests
causal structure, not pattern matching.

**DUAL DEFINER GATE:** Two templates in slot-fillable form. Nothing else.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log** (minimum 5 entries):
```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category,
Pass (apply Pass template). If introducing a competitor: place immediately before that
criterion's definition.

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].
If introducing a competitor: place immediately before that criterion's definition.

**BUILDER E+R GATE:** Failure log + essential + recommended.

---

### AUDIT-FORM SPECIFIER ROLE

Read the essential and recommended criteria from Builder E+R. Your sole deliverable is:
(1) the Holistic-Audit-Reader competitor description, and (2) the structured isolation
audit format. **Do not run the audit in this role. Specify the form only.**

**--- COMPETITOR [N]: THE HOLISTIC AUDIT READER ---**

*(placed at this step because the verification method for criterion fields is committed here)*

The Holistic Audit Reader evaluates the essential and recommended criteria by reading
each criterion as a complete unit. It notes whether the Text "seems to argue for the
right requirement" and whether the Pass conditions "appear to reference measurable
things." Its output is a written commentary per criterion: "C-NN looks good; the Text
clearly describes why the criterion matters and the Pass condition references a count"
or "C-NN needs strengthening; the causal chain could be clearer." The reader's
commentary is thoughtful and identifies real quality issues. However, it never records
which of the six structural checks (direction, contrast, causal chain, location,
observable, no-qualitative) produced each flag. A criterion with a valid Pass field
but wrong-direction Text may receive "the Text is a bit weak" without the direction
check firing. A criterion with qualitative-only Pass receives "Pass could be more
specific" without the no-qualitative check triggering. An evaluator reading the audit
output cannot verify that all six checks ran for all criteria.

**This competitor IS the gap specification for C-39 at the isolation audit step. From
the description above, derive what the correct audit output must record before reading
the operative requirement below.**

**Structured isolation audit format -- required for all criteria in Phase 4.5:**

For each criterion, read each field stripped of surrounding context. Report format --
required; do not substitute narrative commentary:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Text field checks:
1. Direction: does Text locate causality in Y's absence? (Check function: "does this
   locate causality in the wrong form's consequence, in any phrasing?")
2. Contrast: does Text name X alongside Y?
3. Causal chain: does Text name Z?

Pass field checks:
4. Location: names artifact location?
5. Observable: names specific count or token?
6. No qualitative-only: avoids unanchored "clearly" / "adequately"?

**AUDIT-FORM SPECIFIER GATE:** Holistic-Audit-Reader competitor description +
structured audit format specification. No audit output yet.

---

### ISOLATION AUDIT ROLE

Apply the Audit-Form Specifier's structured format to all criteria from Builder E+R.

Run the six-field check for each criterion. Record the structured output format from
Audit-Form Specifier for every criterion. Rewrite any criterion that has a flag.

After audit: run the TIER-DIVERGENCE CHECK:

**--- COMPETITOR 5: THE TIER-BLIND CATEGORIZER ---**

*(placed at this step because the category-distribution commitment is made here)*

The Tier-Blind Categorizer assigns each criterion a category from the menu and grounds
tiers in distinct failure dimensions by design, expecting organic category diversity.
It never produces a named step that counts category assignments per tier and outputs a
per-tier distribution as a verification artifact. If the expected divergence did not
materialize, no STOP fires.

**This competitor IS the gap specification for C-35. Derive the correct implementation
from the description above.**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise category assignments before proceeding.
Divergence status: [PASS / STOP]
```

**ISOLATION AUDIT GATE:** Audit report (structured format for all criteria) +
Divergence status = PASS. Rewritten criteria replace originals.

---

### SCOPE GATEKEEPER ROLE

Read all criteria (Builder E+R + any rewrites). Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property above -- at any threshold -- is not aspirational.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

*(placed at this step because competitor placement for aspirational criteria is committed here)*

The Preamble-Block Curator assembles all novel-aspirational competitors in a block at
the start of the aspirational section. Each competitor correctly constitutes the gap
specification. The builder reads all competitors once at role startup. By the time
the builder reaches the mechanism definition for novel criterion C-NN, the competitor
was encountered earlier in the opening block -- it is a recalled item, not the first
content read before the construction decision.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement from the description above.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT THE CONSTRUCTION STEP WHERE ITS GAP IS OPERATIONALLY
RELEVANT. DO NOT GROUP COMPETITORS IN A SHARED BLOCK.**

A blank "Criterion affected" cell is a format violation. STOP if any exists.

**MECHANISM DEFINER GATE:** Independence Map with specific C-NN in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** For each novel criterion: place a competitor block
immediately before the criterion's definition (at the construction step).

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**
*(placed at this step because the aspirational count is committed here)*

The Unbounded-Aspirational Protocol correctly states "3-5 essential / 2-3 recommended"
tier targets with STOP conditions. For the aspirational tier, it notes that criteria
"should be limited" but names no upper bound and includes no STOP condition.

**This competitor IS the gap specification for C-31. Derive the correct bound from above.**

**--- COMPETITOR 2: THE CATEGORY-MENU PROTOCOL ---**
*(placed at this step because category assignments are completed here)*

The Category-Menu Protocol lists five category options and advises diversity. It does
not include a verification step requiring confirmation of >= 3 distinct categories before
Emit.

**This competitor IS the gap specification for C-32. Derive the correct verification from above.**

**--- COMPETITOR 7: THE PARTIAL-COVERAGE ARCHITECT ---**
*(placed at this step because the novel-criterion count is committed here)*

The Partial-Coverage Architect correctly places competitors at construction steps (C-36)
and names competitors for most novel aspirational criteria. For one novel criterion --
the most structurally complex -- it relies on a positive specification alone. An evaluator
counting competitors cannot determine the novel-criterion count from competitors alone.

**This competitor IS the gap specification for C-37. Derive the coverage requirement from above.**

**Aspirational criteria (1-2).** Count: 1-2 maximum. STOP before drafting a third.

Each criterion: five fields plus **Fills gap**: [cite G-NN -- required].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Competitors: [list by name and C-NN governed] | Count: [N]
Bijection: [counts equal? YES / NO] [one-to-one? YES / NO]
⛔ STOP if any NO.
Coverage status: [PASS / STOP]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential:    [cat: N, ...] -- majority: [category]
  Recommended:  [cat: N, ...] -- majority: [category]
  Aspirational: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N] | ⛔ STOP if N < 2.
Final divergence status: [PASS / STOP]
```

**BUILDER A GATE:** Aspirational criteria + Coverage status = PASS + Final divergence = PASS.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R (as rewritten by Isolation Audit) and Builder A,
re-run the six-field isolation audit using the structured format from Audit-Form Specifier.

**--- COMPETITOR 3: THE FORMULA-ONLY SCORER ---**
*(placed at this step because the PARTIAL earn condition is committed here)*

States "PASS = 1.0, PARTIAL = 0.5, FAIL = 0" without naming earn conditions for 0.5.
Two evaluators assign 0.5 by independent judgment; scoring is not reproducible.

**This competitor IS the gap specification for C-33. Derive the earn-condition requirement.**

**--- COMPETITOR 4: THE DECLARED-INDEPENDENT MAP ---**
*(placed at this step because the Independence Map format is confirmed here)*

Produces a table with "Independent?" = "Yes, independent" for every row, without citing
the specific criterion each mechanism affects.

**This competitor IS the gap specification for C-34. Derive the citation requirement.**

**Audit report:** `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count: Count: [N] | Bound: 1-2. ⛔ STOP if > 2. Compliant? [YES / NO]
Check B -- Category diversity: Distinct categories: [N] | Requirement: >= 3. ⛔ STOP if < 3. Compliant? [YES / NO]
```

---

### SCORING SECTION

| State | Value | Earn conditions |
|-------|-------|-----------------|
| PASS | 1.0 | All Pass conditions met. |
| PARTIAL | 0.5 | [Name earn conditions. Competitor 3 shows what this looks like when absent.] |
| FAIL | 0.0 | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60        max 60
Recommended:  (sum) / N_recommended x 30      max 30
Aspirational: (sum) / N_aspirational x 10     max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational.

**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Body: purpose statement (2-3 sentences: the Audit-Form Specifier role makes the wrong
form of verification the first content read before the isolation audit format is
committed; C-39 is satisfied at the isolation-audit verification step by the
Holistic-Audit-Reader competitor, and at the divergence-check step by the Tier-Blind
Categorizer competitor; the role boundary ensures the competitor description precedes
the format specification structurally, not merely by ordering advice), then SCOPE
DECLARATION, then Coverage Completeness record, then final Divergence Check, then
criteria ordered essential -> recommended -> aspirational (competitors inline, Fills
gap and Dimension retained), then Scoring.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Inertia Framing (Competitor 8: Non-Self-Demonstrating Coverage Architect)

**Axis:** Inertia framing -- Competitor 8 (The Non-Self-Demonstrating Coverage Architect)
is placed inline at the Builder A coverage-completeness check step. The competitor
explicitly describes a rubric that satisfies C-37 (bijection exists) but where the
coverage-completeness criterion's competitor is not distinguishable by counting alone.
The derivation instruction that follows requires sequential competitor numbering when
C-37 (or its equivalent) is itself a novel criterion.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric under V-03 where a coverage-completeness criterion is novel will contain numbered competitors (Competitor 1 through Competitor N); the count of numbered competitors will equal the count of novel aspirational criteria; an evaluator who counts the numbered blocks without reading them confirms bijection including the coverage-completeness criterion's slot; C-38 PASS is structural from the first aspirational draft in any round where C-37 is itself novel. | The sequential numbering instruction changes how all competitors are introduced, not just Competitor 8; rubrics generated under V-03 will show consistently numbered competitor blocks across all construction steps, making the competitor set enumerable from block headers alone; if V-04 (which adds the Anchor template) shows even more consistent competitor enumeration, the Anchor format reinforces the numbering discipline. | V-03 vs V-05 is the primary comparison site for C-38 strength: V-03 has only Competitor 8; V-05 has Competitor 8 plus the Anchor template (which also names competitors by Reference field); if V-05 shows stronger self-referential properties, the Anchor format reinforces the count-verification property independently. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form --
in any phrasing -- locates causality in X's consequence.

**WRITE THE TEMPLATES IN SLOT-FILLABLE FORM. If you write "Pass conditions should
reference observables," you have written a principle, not a template. Start over.**

**DEFINER GATE:** Two templates. Nothing else.

---

### BUILDER E+R ROLE

Read skill spec, failure modes, and Definer templates.

**Failure log** (minimum 5 entries):

```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category,
Pass.

**IF INTRODUCING A COMPETITOR FOR ANY ESSENTIAL CRITERION: PLACE THE COMPETITOR BLOCK
IMMEDIATELY BEFORE THAT CRITERION'S DEFINITION. DO NOT GROUP COMPETITORS IN A SHARED
"OPERATING PRINCIPLES" BLOCK. A COMPETITOR NOT AT ITS CONSTRUCTION STEP IS NOT A GAP
SPECIFICATION -- IT IS A PREAMBLE NOTE.**

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**IF INTRODUCING A COMPETITOR FOR ANY RECOMMENDED CRITERION: SAME RULE.**

**Post-draft audit.** For each criterion:

**--- COMPETITOR 5: THE TIER-BLIND CATEGORIZER ---**

*(placed at this step because the category-distribution commitment is made here)*

The Tier-Blind Categorizer assigns each criterion a category and grounds tiers in
distinct failure dimensions by design, expecting organic category diversity. It considers
C-07 satisfied by construction. It never produces a named step that counts category
assignments per tier and outputs a per-tier distribution as a verification artifact.
If the expected divergence did not materialize, no STOP fires.

**This competitor IS the gap specification for C-35. From the description above, derive
what the correct implementation must add before reading the operative requirement below.**

After the post-draft audit, run the TIER-DIVERGENCE CHECK:

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical.
  Note: the complete three-tier check is run at Builder A.
Divergence status (essential + recommended): [PASS / STOP]
```

**BUILDER E+R GATE:** Failure log + essential + recommended + audit report + Divergence
Check (status = PASS).

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria. Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property above -- at any threshold -- is not aspirational.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

*(placed at this step because competitor placement for aspirational criteria is committed here)*

The Preamble-Block Curator assembles all novel-aspirational competitors in a block at
the start of the aspirational section. Each competitor correctly constitutes the gap
specification. The builder reads all competitors once at role startup -- the competitor
for novel criterion C-NN was encountered forty lines earlier during role setup, not
at the construction step where the design decision is committed.

**This competitor IS the gap specification for C-36. From the description above, derive
what the correct implementation must require before reading the operative requirement below.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT THE CONSTRUCTION STEP WHERE ITS GAP IS OPERATIONALLY
RELEVANT. DO NOT GROUP COMPETITORS IN A SHARED BLOCK AT THE START OF THIS ROLE OR ANY
ROLE. A COMPETITOR READ AT ROLE STARTUP IS NOT AT ITS CONSTRUCTION STEP.**

A blank "Criterion affected" cell is a format violation. STOP if any exists.

**MECHANISM DEFINER GATE:** Independence Map with specific C-NN in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.

**IF INTRODUCING A COMPETITOR FOR ANY ASPIRATIONAL CRITERION: PLACE THE COMPETITOR BLOCK
IMMEDIATELY BEFORE THAT CRITERION'S DEFINITION. THE BUILDER MUST ENCOUNTER THE COMPETITOR
BEFORE MAKING THE CONSTRUCTION DECISION THE COMPETITOR'S FAILURE TRACES TO.**

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

*(placed at this step because the aspirational count is committed here)*

The Unbounded-Aspirational Protocol correctly states tier count targets of "3-5
essential / 2-3 recommended" with STOP conditions. For the aspirational tier, it
notes "aspirational criteria should be limited" but names no upper bound and includes
no STOP condition. A builder using this protocol may draft three or four aspirational
criteria without violating the protocol's stated requirements.

**This competitor IS the gap specification for C-31. From the description above, derive
what the correct implementation must add before reading the operative requirement below.**

**--- COMPETITOR 2: THE CATEGORY-MENU PROTOCOL ---**

*(placed at this step because category assignments are completed here)*

The Category-Menu Protocol lists five category options and advises that "a good rubric
should use diverse categories." It does not include a verification step or STOP requiring
the builder to confirm >= 3 distinct categories appear before Emit.

**This competitor IS the gap specification for C-32. From the description above, derive
what the correct implementation must add.**

**--- COMPETITOR 7: THE PARTIAL-COVERAGE ARCHITECT ---**

*(placed at this step because the novel-criterion count is committed here)*

The Partial-Coverage Architect correctly places competitors at construction steps
(satisfying C-36) and names well-formed competitors for most novel aspirational criteria.
For the criterion introducing the most structurally complex construction requirement,
the Architect relies on a positive specification alone. An evaluator counting competitors
cannot determine the novel-criterion count from the competitor set alone.

**This competitor IS the gap specification for C-37. From the description above, derive
what the correct implementation must require about coverage before reading the operative
requirement below.**

**--- COMPETITOR 8: THE NON-SELF-DEMONSTRATING COVERAGE ARCHITECT ---**

*(placed at this step because the self-referential bijection commitment is made here)*

The Non-Self-Demonstrating Coverage Architect satisfies C-37: every novel aspirational
criterion has exactly one competitor, the competitor count equals the novel-criterion
count, and the Coverage Completeness Check confirms the bijection. When the criterion
governing competitor-criterion coverage completeness (C-37 or an equivalent criterion
in the rubric being built) is itself one of the novel aspirational criteria, the Architect
places the competitor for C-37 alongside the others and confirms the bijection in the
coverage check by listing novel criteria and competitors in parallel. An evaluator who
reads the coverage check and counts both lists confirms the numbers match. But to
confirm that the coverage-completeness criterion specifically has a competitor -- rather
than two of the other novel criteria sharing a competitor -- the evaluator must read
the criterion descriptions and competitor descriptions and match them manually. The
bijection is confirmed by inspection, not by counting alone: the competitor for C-37
is not distinguishable as the C-37 competitor from the competitor count.

**This competitor IS the gap specification for C-38. From the description above, derive
what the correct implementation must guarantee when the coverage-completeness criterion
is itself one of the novel criteria.**

When the criterion governing competitor-criterion correspondence (C-37 or an equivalent
novel criterion in this rubric) is itself listed in the gap register: **NUMBER your
competitors sequentially starting at 1 (Competitor 1, Competitor 2, ... Competitor N)
at their respective construction steps.** The total count of numbered competitors must
equal the total count of novel aspirational criteria. The competitor for C-37 (or
equivalent) is Competitor N -- the same integer as the count of novel criteria. An
evaluator who counts numbered competitor blocks without reading them confirms the
bijection is complete for all novel criteria including the coverage-completeness
criterion itself.

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum. STOP before drafting a third.

Each criterion: five fields (ID continuing from Builder E+R) plus **Fills gap**: [cite
G-NN -- required; blank = format error.] After each criterion: "Is the cited gap named
in the gap register?" If not, revise.

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria (from gap register): [list by C-NN and G-NN]
  Count: [N]

Numbered competitors in this rubric draft:
  [Competitor 1 through Competitor N: name and C-NN governed]
  Count: [N]

Bijection: [counts equal? YES / NO] [each novel criterion has exactly one numbered
  competitor? YES / NO] [each competitor governs exactly one novel criterion? YES / NO]
Self-demonstrating (when C-37 or equivalent is novel): [competitor count = novel-criterion
  count without reading criteria text? YES / NO]
⛔ STOP if any answer is NO.
Coverage status: [PASS / STOP]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential:    [cat: N, ...] -- majority: [category]
  Recommended:  [cat: N, ...] -- majority: [category]
  Aspirational: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
⛔ STOP if N < 2.
Final divergence status: [PASS / STOP]
```

**BUILDER A GATE:** 1-2 aspirational criteria + Coverage status = PASS + Final
divergence status = PASS.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit. Strip preamble;
read each field alone.

**Text field checks (3):**
1. Direction: does Text locate causality in Y's absence?
2. Contrast: does Text name X alongside Y?
3. Causal chain: does Text name Z?

**Pass field checks (3):**
4. Location: names artifact location?
5. Observable: names specific count or token?
6. No qualitative-only: avoids unanchored qualitative language?

**--- COMPETITOR 3: THE FORMULA-ONLY SCORER ---**

*(placed at the scoring-section step because the PARTIAL earn condition is committed here)*

The Formula-Only Scorer states "PASS = 1.0, PARTIAL = 0.5, FAIL = 0" alongside the
composite formula and golden threshold. The scoring structure is complete in form. The
earn conditions for PARTIAL -- the specific circumstances under which a criterion earns
0.5 -- are never named. Two evaluators reading the same criterion assign 0.5 or 0.0
by independent judgment; the scoring is not reproducible.

**This competitor IS the gap specification for C-33. Derive what the correct scoring
section must name before reading the Scoring Section below.**

**--- COMPETITOR 4: THE DECLARED-INDEPENDENT MAP ---**

*(placed at the scoring-section step because the Independence Map format is confirmed here)*

The Declared-Independent Map produces a table where the "Independent?" column reads
"Yes, independent" for every row. The one-to-one assignment is asserted but not cited:
an evaluator cannot confirm which criterion each mechanism affects without reading and
matching manually.

**This competitor IS the gap specification for C-34. Derive the citation format from above.**

**Audit report format -- required:**
`C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**SEVEN-COMPETITOR COVERAGE CONFIRMATION (C-37 and C-38 final):**

```
Novel aspirational criteria in this rubric (for the skill being scored, not the
quest-rubric protocol's own criteria -- list the actual novel G-NN criteria):
  [List by C-NN / G-NN]
  Count: [N]

Numbered competitors in this rubric draft:
  [Competitor 1 through Competitor N: name and C-NN governed]
  Count: [N]

Bijection confirmed? [YES / NO]
Self-demonstrating bijection (C-38, when coverage-completeness criterion is novel)?
  [competitor count = novel-criterion count by counting alone, without reading criteria? YES / NO / N/A]
⛔ STOP if any applicable answer is NO.
```

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count: Count: [N] | Bound: 1-2. ⛔ STOP if > 2. Compliant? [YES / NO]
Check B -- Category diversity: Distinct categories: [N] | Requirement: >= 3. ⛔ STOP if < 3. Compliant? [YES / NO]
```

---

### SCORING SECTION

| State | Value | Earn conditions |
|-------|-------|-----------------|
| PASS | 1.0 | All Pass conditions met. |
| PARTIAL | 0.5 | [Name earn conditions. Competitor 3 above shows what this looks like when earn conditions are absent. Name when 0.5 applies.] |
| FAIL | 0.0 | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60     max 60
Recommended:  (sum) / N_recommended x 30   max 30
Aspirational: (sum) / N_aspirational x 10  max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier bounds (Competitor 1 above shows what happens without the aspirational bound):**
3-5 essential | 2-3 recommended | 1-2 aspirational maximum.

**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Body: purpose statement (2-3 sentences: eight competitors cover eight construction
requirements in sequential numbered bijection; Competitors 5, 6, 7, and 8 extend the
R12 V-05 negative-space specification layer with a self-referential coverage requirement
-- when the criterion governing competitor-criterion correspondence is itself novel,
numbering competitors sequentially makes the bijection verifiable by counting alone;
each competitor is placed at the construction step where its gap is first operationally
relevant, making the negative-space specification temporally co-located with the
commitment it governs), then SCOPE DECLARATION (retained), then Coverage Completeness
record and final Divergence Check (Builder A outputs, retained), then criteria ordered
essential -> recommended -> aspirational (numbered competitors retained inline at
construction steps; Fills gap and Dimension retained; audit report omitted), then
Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Output Format + Inertia Framing (C-11 + C-38)

**Axes:** Output format (Anchor template for C-11) + Inertia framing (Competitor 8
for C-38). C-39 inherited at divergence-check level from R12 V-05 baseline. No
isolation-audit competitor role.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-04 combines the Anchor template (C-11) with Competitor 8 (C-38); every generated rubric will have aspirational competitors in three-field Anchor format AND sequential numbering when the coverage-completeness criterion is itself novel; C-11 and C-38 are both structural from the first aspirational draft; an evaluator can confirm both by inspecting the Anchor fields and counting the numbered competitor blocks. | The Anchor template (Reference / Passes / Fails at) and the sequential numbering instruction are complementary: the Anchor format names competitors by Reference field (making them identifiable by name), while sequential numbering makes them identifiable by count; together they provide two independent verification paths for the same bijection. If V-04's coverage check is tighter than V-01 (Anchor only) or V-03 (numbering only), the two mechanisms reinforce each other. | V-01 (Anchor only) vs V-03 (numbering only) vs V-04 (both) -- if V-04's C-38 compliance is stronger than V-03's despite identical Competitor 8 placement, the Anchor Reference field provides a parallel naming axis that reinforces the count-verification; if equivalent, sequential numbering alone is sufficient for C-38. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DEFINER ROLE

Read the skill spec. Produce three binding templates in slot-fillable form.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**Anchor template (for aspirational competitor definitions only):**

```
Reference: [name of the competitor or prior version being anchored]
Passes: [C-NN through C-NN -- the essential and recommended criteria this reference satisfies]
Fails at: [the exact dimension where this reference falls short -- one sentence naming the observable gap]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form --
in any phrasing -- locates causality in X's consequence.

**DEFINER GATE: Three slot-fillable templates (Text, Pass, Anchor). Nothing else.**

STOP CONDITION: Any output beyond the three templates -- commentary, structural notes,
rationale -- is incomplete. Rewrite before Builder E+R runs.

---

### BUILDER E+R ROLE

Read skill spec and Definer templates.

**Failure log** (minimum 5 entries):
```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots.
Five fields: ID (C-NN), Text, Weight (essential), Category, Pass.
If introducing a competitor: place immediately before the criterion's definition.

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate **Dimension:** [degree | precision | specificity].
If introducing a competitor: place immediately before the criterion's definition.

**Post-draft audit.**

**--- COMPETITOR 5: THE TIER-BLIND CATEGORIZER ---**

*(placed at this step because the category-distribution commitment is made here)*

The Tier-Blind Categorizer grounds tiers in distinct failure dimensions by design and
expects organic category diversity. It never produces a named step that counts category
assignments per tier and outputs a distribution as a verification artifact. If the
expected divergence did not materialize, no STOP fires.

**This competitor IS the gap specification for C-35. Derive the correct implementation.**

After post-draft audit:

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]  -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical.
Divergence status: [PASS / STOP]
```

**Audit report:** `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**BUILDER E+R GATE:** Failure log + essential + recommended + audit + Divergence (PASS).

---

### SCOPE GATEKEEPER ROLE

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property above -- at any threshold -- is not aspirational.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

*(placed at this step because competitor placement for aspirational criteria is committed here)*

The Preamble-Block Curator assembles all novel-aspirational competitors in a block at
the start of the aspirational section. The builder reads all competitors once at role
startup. By the time the builder reaches the mechanism definition for novel criterion
C-NN, the competitor was encountered in the opening block -- not at the construction step.

**This competitor IS the gap specification for C-36. Derive the placement requirement.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT ITS CONSTRUCTION STEP. DO NOT GROUP IN A SHARED BLOCK.**

A blank "Criterion affected" cell is a format violation. STOP if any exists.

**MECHANISM DEFINER GATE:** Independence Map with specific C-NN in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Each aspirational competitor must be in Anchor template format:**

```
Reference: [name]
Passes: [C-NN through C-NN]
Fails at: [exact dimension, one sentence]
```

A competitor block that describes failure behavior without all three Anchor fields is
a format violation.

**--- COMPETITOR 1 (Anchor): THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

```
Reference: The Unbounded-Aspirational Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; tier targets
  "3-5 essential / 2-3 recommended" with STOP conditions are correct]
Fails at: aspirational tier -- no upper bound and no STOP condition named; a builder
  may draft three or four aspirational criteria without violating the protocol
```

**--- COMPETITOR 2 (Anchor): THE CATEGORY-MENU PROTOCOL ---**

```
Reference: The Category-Menu Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; five category
  options listed; criteria constructed with all five fields]
Fails at: category diversity verification -- "use diverse categories" is advice, not
  a STOP condition; no step requires confirmation of >= 3 distinct categories before Emit
```

**--- COMPETITOR 7 (Anchor): THE PARTIAL-COVERAGE ARCHITECT ---**

```
Reference: The Partial-Coverage Architect
Passes: [C-01 through C-NN -- all essential and recommended criteria; competitors
  placed at construction steps (C-36); most novel aspirational criteria have competitors]
Fails at: coverage completeness -- one novel criterion (the most structurally complex)
  has no competitor; an evaluator counting competitors cannot determine the novel-
  criterion count from the competitor set alone
```

**--- COMPETITOR 8 (Anchor): THE NON-SELF-DEMONSTRATING COVERAGE ARCHITECT ---**

```
Reference: The Non-Self-Demonstrating Coverage Architect
Passes: [C-01 through C-NN -- all essential and recommended criteria; C-37 (bijection
  exists, coverage check confirms equal counts, one-to-one)]
Fails at: self-demonstrating bijection -- when the coverage-completeness criterion is
  itself novel, the competitor assigned to it is not distinguishable from the competitor
  count alone; an evaluator must read criterion and competitor descriptions and match
  them manually to confirm the coverage-completeness slot is filled
```

When the criterion governing competitor-criterion correspondence is itself listed in the
gap register: **NUMBER your competitors sequentially (Competitor 1 through Competitor N)
at their respective construction steps.** Competitor N (where N = count of novel criteria)
covers the coverage-completeness criterion. An evaluator who counts numbered competitor
blocks without reading them confirms bijection.

**Aspirational criteria (1-2).** Count: 1-2 maximum. STOP before drafting a third.

Each criterion: five fields plus **Fills gap**: [cite G-NN -- required].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Anchor-format competitors (Reference / Passes / Fails at):
  [Competitor 1 through Competitor N: Reference name and C-NN governed]
  Count: [N]
Bijection: [equal counts? YES / NO] [one-to-one? YES / NO]
Self-demonstrating (when C-37 equivalent is novel): [counting numbered Anchor
  blocks confirms bijection without reading text? YES / NO]
Anchor format compliance: [all competitors have three-field Anchor format? YES / NO]
⛔ STOP if any answer is NO.
Coverage status: [PASS / STOP]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential:    [cat: N, ...] -- majority: [category]
  Recommended:  [cat: N, ...] -- majority: [category]
  Aspirational: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
⛔ STOP if N < 2.
Final divergence status: [PASS / STOP]
```

**BUILDER A GATE:** Aspirational criteria with Anchor-format competitors + Coverage
status = PASS + Final divergence = PASS.

---

### DUAL AUDITOR ROLE

For each criterion: six-field isolation audit.

**--- COMPETITOR 3 (Anchor): THE FORMULA-ONLY SCORER ---**

```
Reference: The Formula-Only Scorer
Passes: [C-01 through C-NN -- all essential and recommended criteria; PASS/PARTIAL/
  FAIL values stated; composite formula and golden threshold correct]
Fails at: PARTIAL earn conditions -- earn conditions for 0.5 are never named; two
  evaluators assign 0.5 by independent judgment; scoring is not reproducible
```

**--- COMPETITOR 4 (Anchor): THE DECLARED-INDEPENDENT MAP ---**

```
Reference: The Declared-Independent Map
Passes: [C-01 through C-NN -- all essential and recommended criteria; Independence
  Map table present; one-to-one assignment between mechanisms and criteria asserted]
Fails at: criterion citation -- "Independent?" = "Yes, independent" for every row;
  no specific C-NN cited; an evaluator cannot confirm which criterion each mechanism
  affects without reading and matching manually
```

**Audit report:** `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count: Count: [N] | Bound: 1-2. ⛔ STOP if > 2. Compliant? [YES / NO]
Check B -- Category diversity: Distinct categories: [N] | Requirement: >= 3. ⛔ STOP if < 3. Compliant? [YES / NO]
```

---

### SCORING SECTION

| State | Value | Earn conditions |
|-------|-------|-----------------|
| PASS | 1.0 | All Pass conditions met. |
| PARTIAL | 0.5 | [Name earn conditions. Competitor 3 Anchor block above shows what this looks like when the Fails at dimension is "earn conditions never named." Name specifically when 0.5 applies for this rubric's criteria.] |
| FAIL | 0.0 | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60     max 60
Recommended:  (sum) / N_recommended x 30   max 30
Aspirational: (sum) / N_aspirational x 10  max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational maximum.
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Body: purpose statement (2-3 sentences: the Definer produces a third Anchor template
constraining every aspirational competitor to the three-field Reference / Passes /
Fails at format; eight competitors in Anchor format, numbered sequentially, cover eight
novel construction requirements in bijection; when the coverage-completeness criterion
is itself novel, Competitor 8 (the Non-Self-Demonstrating Coverage Architect) is the
eighth slot, and counting numbered Anchor blocks confirms coverage for all eight novel
criteria without reading criterion text), then SCOPE DECLARATION, then Coverage
Completeness record, then final Divergence Check, then criteria ordered essential ->
recommended -> aspirational (Anchor-format competitors inline, Fills gap and Dimension
retained), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Output Format + Inertia Framing + Role Sequence (C-11 + C-38 + C-39)

**Axes:** Output format (Anchor template for C-11) + Inertia framing (Competitor 8 for
C-38) + Role sequence (AUDIT-FORM SPECIFIER role with Holistic-Audit-Reader competitor
for C-39 at isolation audit step).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-05 is the ceiling-target variation: three Anchor-format Definer templates close C-11 by structure; Competitor 8 with sequential numbering closes C-38 by making the coverage-completeness bijection self-demonstrating; the AUDIT-FORM SPECIFIER role with Holistic-Audit-Reader competitor closes C-39 at the isolation-audit step (in addition to the divergence-check step inherited from V-05 R12); a rubric generated under V-05 with C-11 PASS achieves composite 100 under v13. | C-39 is satisfied at two independent verification levels: isolation audit (Holistic-Audit-Reader competitor at AUDIT-FORM SPECIFIER role) and divergence check (Tier-Blind Categorizer competitor at Builder E+R); this double-verification architecture makes C-39 structurally overdetermined -- an evaluator can confirm C-39 by finding the wrong-form competitor at either verification step; if V-02 (isolation-audit only) and V-05 (both verification levels) differ on C-39 score, the double-level enforcement adds measurable compliance above a single level. | V-04 (Anchor + Competitor 8, no isolation-audit competitor) vs V-05 (Anchor + Competitor 8 + isolation-audit competitor): if V-05 achieves composite 100 and V-04 does not, the AUDIT-FORM SPECIFIER role carries the C-39 isolation-audit step; if both achieve composite 100, the AUDIT-FORM SPECIFIER role adds no score increment but may add structural robustness. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

The seven roles are:
1. Definer
2. Builder E+R
3. Audit-Form Specifier
4. Isolation Auditor
5. Scope Gatekeeper
6. Mechanism Definer
7. Builder A
8. Dual Auditor

---

### ROLE 1: DEFINER

Read the skill spec. Produce three binding templates in slot-fillable form.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**Anchor template (for aspirational competitor definitions only):**

```
Reference: [name of the competitor or prior version being anchored]
Passes: [C-NN through C-NN -- the essential and recommended criteria this reference satisfies]
Fails at: [the exact dimension where this reference falls short -- one sentence naming the observable gap]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form --
in any phrasing -- locates causality in X's consequence.

**ROLE 1 GATE: Three slot-fillable templates (Text, Pass, Anchor). Nothing else.**

STOP CONDITION: Any content beyond the three templates is incomplete. Rewrite before
Role 2 runs. The three templates are the complete and exclusive output of Role 1.

---

### ROLE 2: BUILDER E+R

Read the skill spec and Role 1 templates.

**Failure log** (minimum 5 entries):
```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category
(correctness | depth | format | coverage | behavior), Pass (apply Pass template).

**IF INTRODUCING A COMPETITOR FOR ANY ESSENTIAL CRITERION: PLACE IT IMMEDIATELY BEFORE
THAT CRITERION'S DEFINITION. DO NOT GROUP COMPETITORS IN A SHARED BLOCK.**

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**IF INTRODUCING A COMPETITOR FOR ANY RECOMMENDED CRITERION: SAME RULE.**

**ROLE 2 GATE:** Failure log + essential + recommended.

---

### ROLE 3: AUDIT-FORM SPECIFIER

Read the criteria from Role 2. Your sole deliverable is: (1) the Holistic-Audit-Reader
competitor, and (2) the structured six-field isolation audit format. **Do not run the
audit. Specify the form only.**

**--- COMPETITOR [N]: THE HOLISTIC AUDIT READER ---**

*(placed at this step because the verification method for criterion fields is committed here)*

The Holistic Audit Reader evaluates the essential and recommended criteria by reading
each criterion as a complete unit. It produces written commentary per criterion:
"C-NN looks good; the Text clearly describes why the criterion matters and the Pass
condition references a count" or "C-NN needs strengthening; the causal chain could be
clearer." Its commentary is thoughtful and identifies real quality issues. However, it
never records which of the six structural checks (direction, contrast, causal chain,
location, observable, no-qualitative) produced each flag. A criterion with a valid
Pass field but wrong-direction Text may receive "the Text is a bit weak" without the
direction check firing. A criterion with qualitative-only Pass receives "Pass could be
more specific" without the no-qualitative check triggering. An evaluator reading the
audit output cannot verify that all six checks ran for all criteria. The wrong criterion
may be rewritten in response to a holistic comment; the right criterion may escape
rewriting when it failed a check that was not named.

**This competitor IS the gap specification for C-39 at the isolation audit step. From
the description above, derive what the correct audit output must record before reading
the operative requirement below.**

**Structured isolation audit format -- required for Role 4:**

For each criterion, read each field stripped of surrounding context. Report format --
required; do not substitute narrative commentary or holistic notes:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Text field checks (check function for each):
1. **Direction**: "does this Text locate causality in Y's absence?" Flag if the prohibited
   form (causality in X's consequence, in any phrasing) is present.
2. **Contrast**: does Text name X alongside Y?
3. **Causal chain**: does Text name Z (the downstream consequence)?

Pass field checks:
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid "clearly," "adequately," "well-structured"
   without an observable anchor?

**ROLE 3 GATE:** Holistic-Audit-Reader competitor description + structured audit format
specification. No audit output -- that is Role 4's deliverable.

---

### ROLE 4: ISOLATION AUDITOR

Apply the Role 3 structured format to all criteria from Role 2. Run the six-field check
for every criterion. Record the structured output format for every criterion. Rewrite
any criterion with a flag; the rewritten version replaces the original.

After audit: run the TIER-DIVERGENCE CHECK:

**--- COMPETITOR 5: THE TIER-BLIND CATEGORIZER ---**

*(placed at this step because the category-distribution verification is committed here)*

The Tier-Blind Categorizer grounds tiers in distinct failure dimensions by design and
expects organic category diversity. It considers C-07 satisfied by construction and
never produces a named step that counts category assignments per tier and outputs a
per-tier distribution as a verification artifact. If the expected divergence did not
materialize, no STOP fires.

**This competitor IS the gap specification for C-35. Derive the correct verification step.**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise category assignments before proceeding.
  Note: three-tier check (including aspirational) is run at Role 7.
Divergence status: [PASS / STOP]
```

**ROLE 4 GATE:** Structured audit report for all criteria (six-field format for each)
+ Divergence status = PASS. Rewritten criteria replace originals.

---

### ROLE 5: SCOPE GATEKEEPER

Read all criteria (Role 2 originals as rewritten by Role 4).

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property above -- at any threshold -- is not aspirational.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**ROLE 5 GATE:** SCOPE DECLARATION with at least G-01.

---

### ROLE 6: MECHANISM DEFINER

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

*(placed at this step because competitor placement for aspirational criteria is committed here)*

The Preamble-Block Curator assembles all novel-aspirational competitors in a block at
the start of the aspirational section. The builder reads all competitors once at role
startup. By the time the builder reaches the mechanism for novel criterion C-NN, the
competitor was encountered in the opening block -- not at the construction step where
the decision is committed.

**This competitor IS the gap specification for C-36. Derive the placement requirement.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT ITS CONSTRUCTION STEP. DO NOT GROUP IN A SHARED BLOCK
AT THE START OF THIS ROLE OR ANY ROLE.**

A blank "Criterion affected" cell is a format violation. STOP if any exists.

**ROLE 6 GATE:** Independence Map with specific C-NN in every row.

---

### ROLE 7: BUILDER A

Read SCOPE DECLARATION (Role 5) and Independence Map (Role 6).

**Each aspirational competitor must be in Role 1 Anchor template format. A competitor
block missing any of the three Anchor fields (Reference / Passes / Fails at) is a
format violation.**

**--- COMPETITOR 1 (Anchor): THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

*(placed at this step because the aspirational count is committed here)*

```
Reference: The Unbounded-Aspirational Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; "3-5 essential /
  2-3 recommended" tier targets with STOP conditions are correctly stated]
Fails at: aspirational tier bound -- no upper bound and no STOP condition named for
  aspirational criteria; a builder may draft three or four without violating the protocol
```

**--- COMPETITOR 2 (Anchor): THE CATEGORY-MENU PROTOCOL ---**

*(placed at this step because category assignments are completed here)*

```
Reference: The Category-Menu Protocol
Passes: [C-01 through C-NN -- all essential and recommended criteria; five category
  options listed; criteria constructed with all five fields correctly]
Fails at: category diversity verification -- "use diverse categories" is advice, not
  a verification step; no STOP condition requires confirmation of >= 3 distinct categories
```

**--- COMPETITOR 7 (Anchor): THE PARTIAL-COVERAGE ARCHITECT ---**

*(placed at this step because the novel-criterion count is committed here)*

```
Reference: The Partial-Coverage Architect
Passes: [C-01 through C-NN -- all essential and recommended criteria; competitors placed
  at construction steps (C-36); most novel aspirational criteria have competitors]
Fails at: coverage completeness -- one novel criterion has no competitor; an evaluator
  counting competitors cannot determine the novel-criterion count from competitors alone
```

**--- COMPETITOR 8 (Anchor): THE NON-SELF-DEMONSTRATING COVERAGE ARCHITECT ---**

*(placed at this step because the self-referential bijection commitment is made here)*

```
Reference: The Non-Self-Demonstrating Coverage Architect
Passes: [C-01 through C-NN -- all essential and recommended criteria; C-37 (bijection
  confirmed by listing novel criteria and competitors in parallel; counts equal;
  one-to-one assignment verified in coverage check)]
Fails at: self-demonstrating bijection -- when the coverage-completeness criterion is
  itself novel, the competitor for that criterion is not distinguishable by counting
  alone; an evaluator must read criterion and competitor text to confirm the coverage-
  completeness slot is occupied
```

When the criterion governing competitor-criterion correspondence is itself listed in the
gap register: **NUMBER your competitors sequentially starting at 1 (Competitor 1 through
Competitor N) at their respective construction steps.** The total count of numbered
Anchor-format competitors must equal the total count of novel aspirational criteria.
The competitor for the coverage-completeness criterion is Competitor N. An evaluator
who counts numbered Anchor blocks without reading them confirms bijection.

**Aspirational criteria (1-2).** Count: 1-2 maximum. STOP before drafting a third.

Each criterion: five fields (ID continuing from Role 2) plus **Fills gap**: [cite G-NN
from Role 5 -- required; blank = format error.] After each criterion: "Is the cited
gap in Role 5's gap register?" If not, revise.

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria (from Role 5 gap register): [list by C-NN and G-NN]
  Count: [N]

Numbered Anchor-format competitors (Reference / Passes / Fails at):
  [Competitor 1 through Competitor N: Reference name and C-NN governed]
  Count: [N]

Bijection: [counts equal? YES / NO] [each novel criterion has exactly one competitor? YES / NO]
Anchor format: [all competitors have three-field Anchor format? YES / NO]
Self-demonstrating (when coverage-completeness criterion is novel): [counting numbered
  Anchor blocks = confirming bijection without reading criterion text? YES / NO]
⛔ STOP if any answer is NO.
Coverage status: [PASS / STOP]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential:    [cat: N, ...] -- majority: [category]
  Recommended:  [cat: N, ...] -- majority: [category]
  Aspirational: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
⛔ STOP if N < 2.
Final divergence status: [PASS / STOP]
```

**ROLE 7 GATE:** Aspirational criteria with Anchor-format numbered competitors +
Coverage status = PASS + Final divergence = PASS.

---

### ROLE 8: DUAL AUDITOR

For each criterion from Roles 2 and 7, re-run the six-field isolation audit using the
Role 3 structured format.

**--- COMPETITOR 3 (Anchor): THE FORMULA-ONLY SCORER ---**

*(placed at this step because the PARTIAL earn condition is committed here)*

```
Reference: The Formula-Only Scorer
Passes: [C-01 through C-NN -- all essential and recommended criteria; PASS = 1.0,
  PARTIAL = 0.5, FAIL = 0; composite formula and golden threshold stated correctly]
Fails at: PARTIAL earn conditions -- earn conditions for 0.5 never named; two evaluators
  assign 0.5 by independent judgment; scoring is not reproducible across sessions
```

**--- COMPETITOR 4 (Anchor): THE DECLARED-INDEPENDENT MAP ---**

*(placed at this step because the Independence Map format is confirmed here)*

```
Reference: The Declared-Independent Map
Passes: [C-01 through C-NN -- all essential and recommended criteria; Independence Map
  table present; one-to-one assignment between mechanisms and criteria asserted]
Fails at: criterion citation -- "Independent?" = "Yes, independent" for every row;
  no specific C-NN cited; evaluator cannot match mechanisms to criteria without reading
```

**Audit report:** `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**COVERAGE CONFIRMATION (C-37 + C-38 final):**

```
Novel aspirational criteria in this rubric (actual skill's G-NN criteria):
  [List by C-NN / G-NN]
  Count: [N]

Numbered Anchor-format competitors:
  [Competitor 1 through Competitor N: Reference name and C-NN governed]
  Count: [N]

Bijection confirmed? [YES / NO]
Self-demonstrating bijection (when coverage-completeness criterion is novel):
  [counting numbered Anchor blocks confirms all slots filled without reading text? YES / NO / N/A]
Anchor format complete (all competitors have Reference / Passes / Fails at)?  [YES / NO]
⛔ STOP if any applicable answer is NO.
```

**C-39 VERIFICATION (both levels):**

```
Isolation audit (Role 3 mechanism):
  Holistic-Audit-Reader competitor placed in Role 3 before audit format specified? [YES / NO]
  Role 4 audit uses six-field structured format derived from Role 3? [YES / NO]

Divergence check (Role 4 mechanism):
  Tier-Blind Categorizer competitor placed in Role 4 before divergence check format? [YES / NO]
  Role 4 divergence check fires as STOP before aspirational drafting? [YES / NO]

C-39 status: [COMPLIANT -- both levels / COMPLIANT -- isolation audit only /
  COMPLIANT -- divergence check only / BLOCKED]
```

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count: Count: [N] | Bound: 1-2. ⛔ STOP if > 2. Compliant? [YES / NO]
Check B -- Category diversity: Distinct categories: [N] | Requirement: >= 3. ⛔ STOP if < 3. Compliant? [YES / NO]
```

---

### SCORING SECTION

| State | Value | Earn conditions |
|-------|-------|-----------------|
| PASS | 1.0 | All Pass conditions met. |
| PARTIAL | 0.5 | [Name earn conditions. Competitor 3 Anchor block above shows the Fails at dimension: "earn conditions for 0.5 never named." State specifically when 0.5 applies -- what partial satisfaction looks like for each criterion tier in this rubric.] |
| FAIL | 0.0 | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60     max 60
Recommended:  (sum) / N_recommended x 30   max 30
Aspirational: (sum) / N_aspirational x 10  max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational maximum.
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Body: purpose statement (3 sentences: the Definer produces three binding templates
-- Text, Pass, and Anchor -- constraining every aspirational competitor to the three-
field Reference / Passes / Fails at format that makes C-11 satisfaction structural;
the Audit-Form Specifier role places the Holistic-Audit-Reader competitor at the
isolation-audit verification step before the six-field structured format is specified,
satisfying C-39 at the field-level audit in addition to the divergence-check level
where the Tier-Blind Categorizer already operates; eight numbered Anchor-format
competitors cover eight novel construction requirements in bijection, and when the
coverage-completeness criterion is itself novel, counting the numbered Anchor blocks
confirms the bijection without reading criterion text, satisfying C-38), then SCOPE
DECLARATION, then Coverage Completeness record, then C-39 Verification record, then
final Divergence Check, then criteria ordered essential -> recommended -> aspirational
(numbered Anchor-format competitors inline at construction steps; Fills gap and
Dimension retained; audit report omitted), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
