# quest-rubric Variate — Round 13 (2026-03-16)
**Date:** 2026-03-16
**Rubric:** v13 (C-01--C-38; adds C-36: STOP-phrasing register uniformity; C-37: atomic
gate-item structure; C-38: pre-role dominant failure mode callout)
**Target criteria:** C-36, C-37, C-38
**Denominator:** /30

**Round 13 design note:** Round 12 extracted three new criteria from excellence and ablation
signals. C-36 (advisory STOP ablation, V-03 R12) found that advisory phrasing at gate
positions is structurally equivalent to gate removal, causing a 10+ criterion cascade. C-37
(prose format ablation, V-04 R12) found that prose checklist items bundling multiple
properties degrade C-05, C-08, C-16, C-17 simultaneously. C-38 (pre-role inertia framing,
V-02 R12) found that a named Dominant Failure Mode callout before the agent-role declaration
creates a calibration anchor independent of SA-1 output.

Round 13 probes whether these three criteria can be independently confirmed (single-axis
ablations and a single-axis addition) and whether their combined activation produces
interference or reinforcement.

**Axis selection:**

| Axis | Single-axis variation | C-36 probe | C-37 probe | C-38 probe |
|------|-----------------------|-----------|-----------|-----------|
| Phrasing register | V-01 | FAIL (advisory at all gates) | baseline | baseline |
| Output format | V-02 | baseline | FAIL (prose rows) | baseline |
| Inertia framing | V-03 | baseline | baseline | PASS (DFM callout added) |
| Output format + inertia framing | V-04 | baseline | FAIL | PASS |
| Phrasing register + format + inertia | V-05 | FAIL | FAIL | PASS |

Single-axis variations isolate each new criterion independently. V-04 tests C-37/C-38
independence (can C-38 pass when C-37 fails?). V-05 tests joint activation stability.

---

## V-01 — Phrasing Register (Advisory STOP Ablation)

**Axis:** Phrasing register — all enforcement-gate STOP tokens replaced with advisory
phrasing throughout the prompt. "STOP if" → "please ensure that", "⛔ STOP" → "consider
pausing", "rewrite before continuing" → "it may be worth revising before continuing",
"halt" → "you may wish to pause". Gate positions are preserved in structure but converted
from imperative to advisory register.

**Hypothesis:**

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-36 FAIL: every gate position is advisory; no imperative enforcement gate exists anywhere in the rubric output; the cascade documented in V-03 R12 re-occurs because the advisory register makes each gate structurally open. | C-31 FAIL (no independent STOP per absent enforcement position -- advisory variants cannot close individual positions); C-33 FAIL (Phase 1 gate does not name Phase 2 as destination in imperative form; advisory framing makes the destination naming ambiguous); C-04 PARTIAL (formula reproducibility weakened when gate enforcement is advisory; partial reproduction less likely to trigger a correction pass). | V-03 R12 is the primary comparison site. V-01 should reproduce the cascade pattern. V-02 baseline STOPs should show sharp contrast at each gate position. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form. Your sole
output is these two templates.

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

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any
phrasing -- locates causality in X's consequence: "X causes failure," "failure occurs
when X is present," "X leads to Z," and all semantic equivalents.

**DEFINER GUIDANCE:** It is recommended that the Definer produce only the two templates
and nothing else. Consider pausing if additional commentary has been added, as this may
affect the quality of downstream roles.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log (minimum 5 entries):**

Please document the following in the failure log:
- F-NN | failure behavior | structural gap the skill failed to require | severity

It is good practice to include at least 5 entries. If fewer than 5 are present, you may
wish to identify additional failure modes before proceeding.

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields per criterion: ID (C-NN, starting at C-01), Text, Weight (essential),
Category (correctness | depth | format | coverage | behavior), Pass (apply Pass template).

If introducing a competitor for any essential criterion: please place the competitor block
immediately before that criterion's definition. Consider grouping competitors only if it
is more natural for the reader.

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

If introducing a competitor for any recommended criterion: same guidance as above.

**Post-draft audit.** For each criterion, it is recommended that you verify:

1. Text contains a causal chain (Y → Z), a contrast (not X), and direction (Y absence)
2. Pass conditions name a location, an observable, and avoid qualitative language
3. The criterion is grounded in the failure log

Consider revising any criterion that does not satisfy all three checks before proceeding.

**TIER-DIVERGENCE CHECK:**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
Please ensure majorities are not identical -- if they are, consider revising
  category assignments.
Divergence status (essential + recommended): [PASS / NEEDS REVIEW]
```

**BUILDER E+R GUIDANCE:** It is suggested that the Builder E+R output include the failure
log, essential criteria, recommended criteria, audit report, and divergence check with
status PASS before proceeding. Please review these elements before the next role begins.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria. Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation note:
  An aspirational criterion covering a property already listed above -- at any
  threshold -- is not aspirational. Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GUIDANCE:** Please ensure the SCOPE DECLARATION includes at least one
gap entry (G-01) before the next role begins. If no gap is found, consider whether the
essential and recommended tiers are truly complete.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator assembles all competitors in a block at the start of the
aspirational section. Each competitor correctly constitutes the gap specification. The
builder reads all competitors at role startup. By the time the builder reaches the
mechanism definition for C-NN, the corresponding competitor was encountered earlier
in the opening block -- it is a recalled item rather than the first content read before
the construction decision.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement from the description above before reading the operative requirement.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Please ensure that the "Criterion affected" column is not blank. A blank cell may
indicate the mechanism is not well-scoped. Consider revising before proceeding.

**MECHANISM DEFINER GUIDANCE:** It is recommended that the Independence Map contain
non-blank, specific C-NN citations in every row. Consider reviewing any row where the
citation is ambiguous or generic.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.
Count constraint: 1-2 maximum. Please do not draft a third aspirational criterion, as
this may inflate the denominator unintentionally.

For each aspirational criterion, it is recommended that you place a competitor block
immediately before that criterion's definition. The competitor should describe the wrong
form and explain the gap.

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

The Unbounded-Aspirational Protocol correctly requires "3-5 essential / 2-3 recommended"
tier targets with stop guidance for both. For the aspirational tier, it notes that
criteria "should be limited" but names no upper bound. A builder using this protocol may
draft three or four aspirational criteria without triggering any gate.

**This competitor IS the gap specification for C-31 (aspirational count bound). Derive
the correct implementation from the description above before reading the operative
requirement.**

Each criterion: five fields (ID continuing from Builder E+R) plus **Fills gap**:
[cite G-NN -- required; if blank, consider whether the criterion is truly aspirational].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Competitors present (listed by reference name and C-NN governed):
  [list each] | Count: [N]
Bijection check: counts equal? [YES / NO] | each criterion has one competitor? [YES / NO]
Please ensure counts are equal and bijection holds. If not, consider adding a competitor
  or revising the aspirational set.
Coverage status: [PASS / NEEDS REVIEW]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential tier:    [cat: N, ...] -- majority: [category]
  Recommended tier:  [cat: N, ...] -- majority: [category]
  Aspirational tier: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
Consider reviewing if N < 2.
Final divergence status: [PASS / NEEDS REVIEW]
```

**BUILDER A GUIDANCE:** It is recommended that the output include 1-2 aspirational
criteria with competitor blocks, coverage status, and divergence status before proceeding.

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

**--- COMPETITOR 3: THE FORMULA-ONLY SCORER ---**

The Formula-Only Scorer states PASS = 1.0, PARTIAL = 0.5, FAIL = 0 alongside the
composite formula and golden threshold. The scoring structure is complete in form. However,
the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0 are
never named. Two evaluators reading the same criterion will assign 0.5 or 0.0 by
independent judgment.

**This competitor IS the gap specification for C-23 (per-criterion PARTIAL conditions).
Derive the correct requirement from the description above.**

**--- COMPETITOR 4: THE DECLARED-INDEPENDENT MAP ---**

The Declared-Independent Map produces a table with "Mechanism name," "What it does," and
"Independent?" columns. The one-to-one assignment is asserted. But the "Independent?"
column reads "Yes, independent" for every row; an evaluator cannot confirm which criterion
each mechanism affects without reading descriptions manually.

**This competitor IS the gap specification for C-28 (DEPENDS_ON declarations). Derive
the correct requirement from the description above.**

**Audit report format -- required:**
`C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count:
  Count: [N] | Bound: 1-2 maximum.
  Consider reviewing if count > 2.
  Compliant? [YES / REVIEW]

Check B -- Category diversity:
  Distinct categories: [N] | Requirement: >= 3.
  Consider reviewing if N < 3.
  Compliant? [YES / REVIEW]
```

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State earn conditions: the specific circumstances under which a criterion earns 0.5. Name the conditions explicitly rather than leaving them to evaluator judgment.] |
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

Body: purpose statement (2-3 sentences), then SCOPE DECLARATION (retained), then Coverage
Completeness record (retained), then final Divergence Check (retained), then criteria
ordered essential -> recommended -> aspirational (competitors retained inline at their
construction steps; Dimension and Fills gap annotations retained; audit report omitted),
then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 — Output Format (Prose Checklist Rows)

**Axis:** Output format — the Phase 1 planning audit (post-draft audit in Builder E+R)
and the Phase 2 isolation audit (Dual Auditor) are specified as numbered prose items
instead of per-criterion structured format tables. Each prose item bundles multiple
structural properties: "1. Verify that the Text field contains a causal chain, names the
contrast form, and locates causality in Y's absence; also confirm the Pass condition names
a location and an observable without qualitative language." One sentence = one item = multiple
properties. The `C-NN: Text flags: [Y/N, Y/N, Y/N]` per-criterion record format is absent.

**Hypothesis:**

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-37 FAIL: every audit row bundles multiple structural properties; no row is evaluable as a single binary gate; the pattern from V-04 R12 recurs -- C-05, C-16, C-17 each degrade to PARTIAL because the bundled items cannot support independent per-property verification. | C-08 PARTIAL (duplicate failure mode visibility degraded when checklist is prose narrative); C-31 PARTIAL (independent STOP per absent position weakened by prose bundling -- a bundled gate fires on the bundle, not on individual absent positions). V-01 baseline STOPs are preserved imperative; the advisory cascade from V-01 does not appear here. | V-04 R12 is the primary comparison site. V-02 should reproduce the prose-bundling degradation pattern while leaving gate register intact. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

### DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form. Your sole
output is these two templates.

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

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any
phrasing -- locates causality in X's consequence.

**DEFINER GATE: Two slot-fillable templates. Nothing else.**

⛔ STOP CONDITION: A Definer output containing commentary beyond the two templates is
incomplete. Rewrite before Builder E+R runs.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log (minimum 5 entries):**

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

⛔ STOP if fewer than 5 entries are present. Identify additional failure modes before
proceeding.

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category
(correctness | depth | format | coverage | behavior), Pass (apply Pass template).

If introducing a competitor: place immediately before that criterion's definition. Do not
group competitors in a shared block.

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test
degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft quality review.** After drafting criteria, review each one against the
following checklist:

1. Check that the Text field argues causally for the requirement: it should explain why
   the property matters, name what happens when it is absent (Z), and identify the
   contrast form (X) that looks similar but fails differently. The causal argument should
   be present, not just implied.
2. Confirm that the Pass condition is specific enough for two evaluators to reach the same
   verdict: it should name where in the artifact the evaluator looks, what specific token
   or count they check, and it should avoid saying things like "clearly" or "adequately"
   without a measurement standard attached.
3. Ensure that each criterion is traceable to a specific entry in the failure log. A
   criterion with no failure-log origin may be covering a property that was not actually
   observed to fail, which weakens the rubric's empirical grounding.

Revise any criterion that does not satisfy all three checklist items before proceeding to
the Scope Gatekeeper.

**TIER-DIVERGENCE CHECK:**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise category assignments before proceeding.
Divergence status (essential + recommended): [PASS / STOP]
```

**BUILDER E+R GATE:** Failure log + essential + recommended + quality review notes +
Divergence Check output (status = PASS).

⛔ STOP if divergence status is not PASS. Do not proceed to Scope Gatekeeper.

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
  An aspirational criterion covering a property already listed above -- at any
  threshold -- is not aspirational. Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

⛔ STOP if no gap is registered. The aspirational tier cannot be built without a gap.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator assembles all competitors in a block at the start of the
aspirational section. Each competitor correctly constitutes the gap specification. The
builder reads all competitors at role startup. By the time the builder reaches criterion
C-NN, the competitor was encountered earlier in the opening block.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement from the description above before reading the operative requirement below.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT THE CONSTRUCTION STEP WHERE ITS GAP IS OPERATIONALLY
RELEVANT. DO NOT GROUP COMPETITORS IN A SHARED BLOCK. A COMPETITOR READ AT ROLE STARTUP
IS NOT AT ITS CONSTRUCTION STEP.**

A blank "Criterion affected" cell is a format violation.
⛔ STOP if any blank cell exists. Rewrite before Builder A runs.

**MECHANISM DEFINER GATE:** Independence Map with specific C-NN in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum.

For each aspirational criterion, place a competitor block immediately before that
criterion's definition.

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

The Unbounded-Aspirational Protocol correctly requires "3-5 essential / 2-3 recommended"
tier targets with STOP conditions. For the aspirational tier, it notes that criteria
"should be limited" but names no upper bound. A builder may draft three or four
aspirational criteria without triggering any gate.

**This competitor IS the gap specification for C-31. Derive the correct implementation
from the description above.**

Each criterion: five fields (ID continuing from Builder E+R) plus **Fills gap**:
[cite G-NN -- required; blank = format error].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Competitors present (listed by reference name and C-NN governed):
  [list each] | Count: [N]
Bijection: counts equal? [YES / NO] | each criterion has one competitor? [YES / NO]
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

**BUILDER A GATE:** 1-2 aspirational criteria + Coverage status = PASS + Divergence
status = PASS.

⛔ STOP if either status is not PASS.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit.

Review each criterion against the following quality checklist. For each criterion, write
a short evaluation paragraph covering: (a) whether the Text field makes a clear causal
argument for the requirement, names what fails when the property is absent, and identifies
a contrast form; (b) whether the Pass condition is specific enough for independent
evaluation, names a location in the artifact, and uses measurement-based rather than
purely qualitative language; (c) whether any criterion should be revised based on this
review. If a criterion requires revision, note it explicitly and provide the revised form
before proceeding to the Scoring Section.

1. Text quality: does the Text field contain a clear Y/Z causal chain plus an X contrast?
   Does it locate causality in Y's absence rather than X's presence? Is the argument
   specific to this skill's failure mode, or is it generic enough to apply to any rubric?
2. Pass condition quality: does the Pass condition give an evaluator a location, a
   specific observable, and a standard? Does it avoid saying "clearly" or "adequately"
   without anchoring those words to a count, token, or structural property?
3. Cross-criterion check: do any two criteria measure the same property? If so, which
   one is more precisely scoped, and should the other be merged or dropped?

After the review, run the pre-emit checks:

The aspirational count should be 1-2. Count the aspirational criteria and confirm this
is within bounds. If the count exceeds 2, identify which criterion is least essential
and revise the aspirational tier before emitting.

The category diversity requirement is >= 3 distinct categories across all criteria.
Count distinct categories and confirm. If fewer than 3 are present, identify which
criteria could be reassigned to a different category without distorting their meaning,
and revise before emitting.

**DUAL AUDITOR GATE:** Quality review notes for all criteria + pre-emit checks
(aspirational count <= 2, category diversity >= 3).

⛔ STOP if either pre-emit check fails. Revise before emitting.

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State earn conditions: the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. Name the conditions explicitly.] |
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

Body: purpose statement (2-3 sentences), then SCOPE DECLARATION (retained), then Coverage
Completeness record (retained), then final Divergence Check (retained), then criteria
ordered essential -> recommended -> aspirational (competitors retained inline; Dimension
and Fills gap annotations retained; audit notes omitted), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 — Inertia Framing (Pre-Role Dominant Failure Mode Callout)

**Axis:** Inertia framing — a named "DOMINANT FAILURE MODE" block is added before the
first role declaration (before the DEFINER ROLE). The block is a discrete labeled
structural unit (not a parenthetical or inline comment). It names the dominant failure
mode the rubric is architected to detect and explains why that mode is primary. It is
self-contained: an evaluator reading only the pre-role block can identify the failure mode
without reading any criterion.

**Hypothesis:**

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-38 PASS: a named, self-contained failure mode callout block appears before the first role declaration; the block names the failure mode and explains why it is primary; satisfies all three C-38 conditions (named block, pre-role placement, self-contained explanation). | C-04 depth strengthened: the pre-role anchor establishes the calibration target before any structural scope is declared; rubrics generated under V-03 will show tighter alignment between the failure mode and the essential criteria. C-11 depth signal: the pre-role framing surfaces the dominant failure mode as a grounding anchor for the entire construction; the failure mode named in the block should be traceable to at least one essential criterion. | V-05 is the primary comparison site: V-03 adds the DFM callout with clean gate enforcement; V-05 combines DFM with advisory gates; if V-05 degrades the C-38 anchor quality despite having the DFM callout, the advisory register contaminates the pre-role grounding. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

## DOMINANT FAILURE MODE

**Name:** Threshold Tightening Without New Territory

**Why this is the dominant failure mode for rubrics built by this skill:**

A rubric that adds an aspirational criterion covering a property already guarded by an
essential criterion -- but at a higher threshold -- appears to offer depth while
measuring nothing new. The essential criterion fires when the property is absent. The
aspirational criterion fires when the property is present but weak. Both criteria measure
the same dimension. The aspirational criterion does not widen the rubric's coverage; it
narrows the acceptable band. This failure mode is dominant because it is produced
naturally by the construction process: the same spec language that motivates an essential
criterion also motivates a more demanding form of that criterion, and the builder has no
gate that checks whether the new bar is on the same dimension as an existing bar. The
Scope Gatekeeper's threshold escalation prohibition is the primary defense; without it,
the aspirational tier becomes a threshold-tightening appendix rather than a genuine
coverage extension.

**Observable indicator:** Two criteria in the rubric share a property name (e.g.,
"completeness," "specificity," "accuracy") and differ only in the threshold value
(e.g., "at least one" vs "all"). The higher-threshold criterion is aspirational. An
evaluator who can satisfy the aspirational criterion has already satisfied the essential
one by construction; the aspirational criterion adds no independent observable.

---

### DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form. Your sole
output is these two templates.

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

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any
phrasing -- locates causality in X's consequence.

**DEFINER GATE: Two slot-fillable templates. Nothing else.**

⛔ STOP CONDITION: A Definer output containing commentary beyond the two templates is
incomplete. Rewrite before Builder E+R runs.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log (minimum 5 entries):**

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

⛔ STOP if fewer than 5 entries. Identify additional failure modes.

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots
verbatim. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category
(correctness | depth | format | coverage | behavior), Pass (apply Pass template).

**IF INTRODUCING A COMPETITOR FOR ANY ESSENTIAL CRITERION: PLACE THE COMPETITOR BLOCK
IMMEDIATELY BEFORE THAT CRITERION'S DEFINITION. DO NOT GROUP COMPETITORS IN A SHARED
BLOCK.**

**Recommended criteria (2-3).** From suboptimal failure modes. Annotate: **Dimension:**
[degree | precision | specificity].

**Post-draft audit.** For each criterion:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

**TIER-DIVERGENCE CHECK:**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise before proceeding.
Divergence status (essential + recommended): [PASS / STOP]
```

**BUILDER E+R GATE:** Failure log + essential + recommended + audit report + Divergence
Check (status = PASS).

⛔ STOP if divergence status is not PASS.

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
  -- is not aspirational. Tighter is not new territory. (This prohibition is the primary
  defense against the Dominant Failure Mode named in the pre-role block above.)

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

⛔ STOP if no gap registered.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator assembles all competitors in a block at the start of the
aspirational section. Each competitor correctly constitutes the gap specification. By the
time the builder reaches C-NN, the competitor was encountered earlier in the opening
block -- it is a recalled item, not the first content read before the construction
decision.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement from the description above.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT THE CONSTRUCTION STEP WHERE ITS GAP IS OPERATIONALLY
RELEVANT. DO NOT GROUP COMPETITORS IN A SHARED BLOCK.**

⛔ STOP if any "Criterion affected" cell is blank.

**MECHANISM DEFINER GATE:** Independence Map with specific C-NN in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum. Do not draft a third.

For each aspirational criterion, place a competitor block immediately before that
criterion's definition.

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

*(placed at this step because the aspirational count is committed here)*

The Unbounded-Aspirational Protocol correctly requires "3-5 essential / 2-3 recommended"
with STOP conditions. For the aspirational tier, it notes criteria "should be limited"
but names no upper bound.

**This competitor IS the gap specification for C-31. Derive the correct implementation.**

Each criterion: five fields (ID continuing from Builder E+R) plus **Fills gap**: [G-NN].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list] | Count: [N]
Competitors present: [list] | Count: [N]
Bijection: [YES/NO] | One-to-one: [YES/NO]
⛔ STOP if any NO.
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

**BUILDER A GATE:** 1-2 criteria + Coverage PASS + Divergence PASS.

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

**--- COMPETITOR 3: THE FORMULA-ONLY SCORER ---**

The Formula-Only Scorer states PASS = 1.0, PARTIAL = 0.5, FAIL = 0 alongside the
formula and threshold. The scoring structure is complete in form. However, the specific
circumstances under which a criterion earns 0.5 are never named.

**This competitor IS the gap specification for C-23. Derive the correct requirement.**

**--- COMPETITOR 4: THE DECLARED-INDEPENDENT MAP ---**

The Declared-Independent Map produces a table with "Mechanism," "What it does," and
"Independent?" columns. But "Independent?" reads "Yes, independent" for every row; an
evaluator cannot confirm which criterion each mechanism affects.

**This competitor IS the gap specification for C-28. Derive the correct requirement.**

**Audit report format -- required:**
`C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**PRE-EMIT VERIFICATION:**

```
Check A -- Aspirational count:
  Count: [N] | Bound: 1-2 maximum.
  ⛔ STOP if count > 2.
  Compliant? [YES / NO]

Check B -- Category diversity:
  Distinct categories: [N] | Requirement: >= 3.
  ⛔ STOP if N < 3.
  Compliant? [YES / NO]
```

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Name the specific circumstances under which a criterion earns 0.5.] |
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

Body: purpose statement (2-3 sentences, including reference to the Dominant Failure Mode
named in the pre-role block), then SCOPE DECLARATION (retained), then Coverage Completeness
(retained), then final Divergence Check (retained), then criteria ordered essential ->
recommended -> aspirational (competitors retained inline; Dimension and Fills gap retained;
audit report omitted), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 — Output Format + Inertia Framing (Prose Checklist + DFM Callout)

**Axis:** Output format (prose checklist rows, from V-02) combined with inertia framing
(pre-role dominant failure mode callout, from V-03). C-36 baseline: gate register is
imperative throughout. C-37 target: FAIL (prose audit). C-38 target: PASS (DFM callout).
Independence probe: can C-38 pass when C-37 fails?

**Hypothesis:**

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-37 FAIL + C-38 PASS: the prose checklist causes the same degradation cascade as V-02 (C-05, C-16, C-17 all PARTIAL); the DFM callout satisfies C-38 independently; the two criteria do not interact -- prose audit format does not contaminate the pre-role block's structural independence. | C-31 PARTIAL (prose-bundled items weaken per-position STOP; but gates are imperative so C-36 holds clean); the DFM block's "Observable indicator" section strengthens C-04 alignment between the stated failure mode and the essential criteria the rubric builds. | V-02 is the control for C-37 (prose without DFM); V-03 is the control for C-38 (DFM without prose). V-04 confirms independence: C-38 should score identically to V-03 on the rubric; C-37 should score identically to V-02. Any interference between the two axes is diagnostic. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

## DOMINANT FAILURE MODE

**Name:** Threshold Tightening Without New Territory

**Why this is the dominant failure mode for rubrics built by this skill:**

A rubric that adds an aspirational criterion covering a property already guarded by an
essential criterion -- but at a higher threshold -- appears to offer depth while
measuring nothing new. The essential criterion fires when the property is absent. The
aspirational criterion fires when the property is present but weak. Both criteria measure
the same dimension. This failure mode is dominant because the same spec language that
motivates an essential criterion also motivates a more demanding form of that criterion,
and the builder has no gate that checks whether the new bar is on the same dimension as
an existing bar. The Scope Gatekeeper's threshold escalation prohibition is the primary
defense.

**Observable indicator:** Two criteria share a property name and differ only in threshold
(e.g., "at least one" vs "all"). The higher-threshold criterion is aspirational. An
evaluator satisfying the aspirational criterion has already satisfied the essential one.

---

### DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form. Your sole
output is these two templates.

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

Causal direction rule: required form is "without Y, Z fails."

**DEFINER GATE: Two slot-fillable templates. Nothing else.**

⛔ STOP CONDITION: A Definer output with commentary beyond the templates is incomplete.
Rewrite before Builder E+R runs.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log (minimum 5 entries):**

```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

⛔ STOP if fewer than 5 entries.

**Essential criteria (3-5).** From blocking failure modes. Apply Text template verbatim.
Five fields: ID (C-NN), Text, Weight (essential), Category, Pass (apply Pass template).

If introducing a competitor: place immediately before that criterion's definition.

**Recommended criteria (2-3).** Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft quality review.** After drafting criteria, review each one against the
following checklist:

1. Does the Text field make a causal argument? It should explain why the property
   matters, name what fails when the property is absent (Z), and identify a contrast
   form (X). The argument should be specific to this skill's failure mode, not generic.
2. Is the Pass condition specific enough for two independent evaluators to reach the same
   verdict? It should name a location, a specific observable (count, token, or structural
   property), and avoid purely qualitative language without a measurement anchor.
3. Is each criterion traceable to a specific failure log entry? A criterion with no
   failure-log origin may be covering a property that was not observed to fail.

Revise any criterion that does not satisfy all three checklist items before proceeding.

**TIER-DIVERGENCE CHECK:**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
⛔ STOP if majorities are identical -- revise before proceeding.
Divergence status (essential + recommended): [PASS / STOP]
```

**BUILDER E+R GATE:** Failure log + essential + recommended + quality review notes +
Divergence Check (status = PASS).

⛔ STOP if divergence status not PASS.

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
  -- is not aspirational. (This is the primary defense against the Dominant Failure Mode.)

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

⛔ STOP if no gap registered.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator assembles all competitors in a block at the start of the
aspirational section. Each competitor correctly constitutes the gap specification. The
builder reads all competitors at role startup. By the time the builder reaches C-NN,
the competitor was encountered earlier in the opening block.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**PLACE EACH COMPETITOR INLINE AT ITS CONSTRUCTION STEP. DO NOT GROUP IN A SHARED BLOCK.**

⛔ STOP if any "Criterion affected" cell is blank.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum.

For each aspirational criterion, place a competitor block immediately before its definition.

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

The Unbounded-Aspirational Protocol correctly requires "3-5 essential / 2-3 recommended"
with STOP conditions. For the aspirational tier, criteria "should be limited" but no
upper bound is named.

**This competitor IS the gap specification for C-31.**

Each criterion: five fields plus **Fills gap**: [G-NN].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list] | Count: [N]
Competitors present: [list] | Count: [N]
Bijection: [YES/NO] | One-to-one: [YES/NO]
⛔ STOP if any NO.
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

**BUILDER A GATE:** 1-2 criteria + Coverage PASS + Divergence PASS.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit.

Review each criterion against the following quality checklist. Write a short evaluation
paragraph per criterion covering:

1. Text quality: does the Text contain a Y/Z causal chain and an X contrast? Does it
   locate causality in Y's absence? Is it specific to this skill's failure mode?
2. Pass condition quality: does the Pass condition give a location, a specific observable,
   and a measurement-based standard? Does it avoid purely qualitative language?
3. Cross-criterion check: do any two criteria measure the same property at different
   thresholds? If so, identify which is aspirational and whether it adds independent
   coverage.

After the review, run the pre-emit checks:

Aspirational count should be 1-2. Count and confirm. If > 2, identify the least
essential aspirational criterion and revise before emitting.

Category diversity requirement is >= 3 distinct categories. Count and confirm. If
fewer than 3, identify which criteria could be reassigned and revise before emitting.

**DUAL AUDITOR GATE:** Quality review paragraphs for all criteria + pre-emit checks.

⛔ STOP if either pre-emit check fails.

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Name the specific circumstances under which a criterion earns 0.5.] |
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

Body: purpose statement (2-3 sentences, referencing the Dominant Failure Mode), then
SCOPE DECLARATION (retained), then Coverage Completeness (retained), then Divergence
Check (retained), then criteria ordered essential -> recommended -> aspirational
(competitors retained inline; Dimension and Fills gap retained; audit notes omitted),
then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 — Phrasing Register + Output Format + Inertia Framing (Full Combination)

**Axis:** All three axes activated simultaneously: advisory STOP register (V-01), prose
checklist audit rows (V-02), and pre-role dominant failure mode callout (V-03). Full
combination ceiling target: C-36 FAIL, C-37 FAIL, C-38 PASS. Tests whether all three
axes together produce interference or independence.

**Hypothesis:**

| Primary effect | Secondary effect | Predicted manifestation sites |
|---|---|---|
| C-36 FAIL + C-37 FAIL + C-38 PASS: advisory gates cause the C-36 cascade (C-31, C-33 degraded); prose audit rows cause the C-37 cascade (C-05, C-16, C-17 PARTIAL); DFM callout independently passes C-38; no axis interferes with another. | The DFM callout's pre-role position is immune to both ablation axes: advisory gates occur inside roles; prose audit occurs inside the Builder roles; neither contaminates the pre-role structural slot. C-38 PASS is therefore predicted with full confidence. The cascades from V-01 and V-02 are predicted to be additive: the combined degradation set is the union of V-01 and V-02 degradation sets. | V-01 vs V-05: V-05 adds prose audit and DFM; if V-05 C-36 score matches V-01 exactly, the other two axes are confirmed non-interfering with C-36. V-02 vs V-05: V-05 adds advisory gates and DFM; if C-37 score matches V-02 exactly, the other axes are confirmed non-interfering with C-37. V-03 vs V-05: if C-38 score matches V-03 exactly, the two ablation axes are confirmed non-interfering with C-38. |

---

You are a multi-role rubric construction system. Roles run in strict sequence.
**Do not begin a role until the previous role's output is complete.**

---

## DOMINANT FAILURE MODE

**Name:** Threshold Tightening Without New Territory

**Why this is the dominant failure mode for rubrics built by this skill:**

A rubric that adds an aspirational criterion covering a property already guarded by an
essential criterion -- but at a higher threshold -- appears to offer depth while
measuring nothing new. The essential criterion fires when the property is absent. The
aspirational criterion fires when the property is present but weak. Both criteria measure
the same dimension. This failure mode is dominant because the construction process
naturally produces it: the same spec language motivates an essential criterion and a more
demanding form of the same criterion. The builder has no gate checking whether the new
bar is on the same dimension as an existing bar. The Scope Gatekeeper's threshold
escalation prohibition is the primary defense; without it, the aspirational tier becomes
a threshold-tightening appendix rather than genuine coverage extension.

**Observable indicator:** Two criteria share a property name and differ only in threshold.
The higher-threshold criterion is aspirational. An evaluator satisfying the aspirational
criterion has already satisfied the essential one by construction.

---

### DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form. Your sole
output is these two templates.

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

Causal direction rule: required form is "without Y, Z fails."

**DEFINER GUIDANCE:** It is recommended that the Definer produce only the two templates.
Consider pausing if additional commentary has been included, as this may affect downstream
role quality.

---

### BUILDER E+R ROLE

Read the skill spec and Definer templates.

**Failure log (minimum 5 entries):**

```
F-NN | failure behavior | structural gap | severity: blocking / suboptimal / cosmetic
```

It is good practice to include at least 5 entries. If fewer than 5 are present, you may
want to identify additional failure modes before proceeding.

**Essential criteria (3-5).** From blocking failure modes. Apply Text template verbatim.
Five fields: ID (C-NN), Text, Weight (essential), Category, Pass (apply Pass template).

If introducing a competitor: please place immediately before that criterion's definition.
Consider not grouping competitors in a shared block, as inline placement is preferred.

**Recommended criteria (2-3).** Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft quality review.** After drafting criteria, review each one against the
following checklist:

1. Does the Text field make a causal argument? It should explain why the property
   matters, name what fails when the property is absent (Z), and identify a contrast
   form (X) that looks correct but fails differently. The argument should be specific to
   this skill, not generic.
2. Is the Pass condition specific enough for two independent evaluators to agree? It
   should name a location, a specific observable, and avoid purely qualitative language
   without a measurement anchor attached.
3. Is each criterion traceable to a specific failure log entry? A criterion with no
   failure-log origin may cover a property that was not observed to fail.

Please revise any criterion that does not satisfy all three items. Consider completing
the revision before proceeding to the Scope Gatekeeper.

**TIER-DIVERGENCE CHECK:**

```
TIER-DIVERGENCE CHECK:
  Essential tier:    [cat: N, cat: N, ...] -- majority: [category or "tied"]
  Recommended tier:  [cat: N, ...]         -- majority: [category or "tied"]
Distinct majority categories (essential + recommended): [N]
Please ensure majorities are not identical. If they are, consider revising category
  assignments before proceeding.
Divergence status (essential + recommended): [PASS / NEEDS REVIEW]
```

**BUILDER E+R GUIDANCE:** Please review that the output includes the failure log,
essential criteria, recommended criteria, quality review notes, and divergence check
before the next role begins.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria. Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation note:
  An aspirational criterion covering a property already listed above -- at any threshold
  -- is not aspirational. (This is the primary defense against the Dominant Failure Mode
  named in the pre-role block above.)

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GUIDANCE:** Please ensure the SCOPE DECLARATION includes at least
G-01 before the next role begins.

---

### MECHANISM DEFINER ROLE

Read all criteria. Produce the Independence Map.

**--- COMPETITOR 6: THE PREAMBLE-BLOCK CURATOR ---**

The Preamble-Block Curator assembles all competitors in a block at the start of the
aspirational section. Each competitor correctly constitutes the gap specification. The
builder reads all competitors at role startup. By the time the builder reaches C-NN,
the competitor was encountered earlier in the opening block -- it is a recalled item,
not the first content read before the construction decision.

**This competitor IS the gap specification for C-36. Derive the correct placement
requirement from the description above before reading the operative requirement below.**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Please ensure that the "Criterion affected" column is not blank. If a cell is blank,
consider whether the mechanism is well-scoped and revise before proceeding.

**MECHANISM DEFINER GUIDANCE:** It is recommended that the Independence Map contain
specific C-NN citations in every row before Builder A begins.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Count constraint: 1-2 maximum. Please do not draft a
third aspirational criterion.

For each aspirational criterion, it is recommended that you place a competitor block
immediately before that criterion's definition.

**--- COMPETITOR 1: THE UNBOUNDED-ASPIRATIONAL PROTOCOL ---**

The Unbounded-Aspirational Protocol correctly requires "3-5 essential / 2-3 recommended"
tier targets with stop guidance for both. For the aspirational tier, criteria "should be
limited" but no upper bound is named. A builder may draft three or four aspirational
criteria without triggering any gate.

**This competitor IS the gap specification for C-31.**

Each criterion: five fields plus **Fills gap**: [cite G-NN].

**COVERAGE COMPLETENESS CHECK:**

```
Novel aspirational criteria: [list by C-NN and G-NN] | Count: [N]
Competitors present (by reference name and C-NN governed): [list] | Count: [N]
Bijection check: counts equal? [YES / NO] | One-to-one? [YES / NO]
Please ensure counts are equal and bijection holds. If not, consider adding a competitor
  or revising the aspirational set before proceeding.
Coverage status: [PASS / NEEDS REVIEW]
```

**COMPLETE THREE-TIER DIVERGENCE CHECK:**

```
  Essential tier:    [cat: N, ...] -- majority: [category]
  Recommended tier:  [cat: N, ...] -- majority: [category]
  Aspirational tier: [cat: N, ...] -- majority: [category]
Distinct majority categories: [N]
Consider reviewing if N < 2.
Final divergence status: [PASS / NEEDS REVIEW]
```

**BUILDER A GUIDANCE:** Please ensure the output includes 1-2 aspirational criteria with
competitor blocks, coverage status, and divergence status before proceeding.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit.

Review each criterion against the following quality checklist. For each criterion, write
a short evaluation paragraph covering:

1. Text quality: does the Text contain a Y/Z causal chain and an X contrast? Does it
   locate causality in Y's absence? Is the argument specific to this skill or generic?
2. Pass condition quality: does the Pass condition give a location, a specific observable,
   and a measurement standard? Does it avoid purely qualitative language?
3. Cross-criterion check: do any two criteria measure the same property at different
   thresholds? If so, which is aspirational and does it add independent coverage?

After the review, run the pre-emit checks:

Aspirational count should be 1-2. Count and confirm. If > 2, consider identifying the
least essential aspirational criterion and revising before emitting.

Category diversity requirement is >= 3 distinct categories. Count and confirm. If
fewer than 3, consider which criteria could be reassigned and revise before emitting.

**DUAL AUDITOR GUIDANCE:** It is recommended to complete the quality review and pre-emit
checks before emitting. If pre-emit checks show issues, consider revising before output.

---

### SCORING SECTION

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Name the specific circumstances under which a criterion earns 0.5.] |
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

Body: purpose statement (2-3 sentences, referencing the Dominant Failure Mode named
in the pre-role block), then SCOPE DECLARATION (retained), then Coverage Completeness
(retained), then Divergence Check (retained), then criteria ordered essential ->
recommended -> aspirational (competitors retained inline; Dimension and Fills gap
retained; audit notes omitted), then Scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
