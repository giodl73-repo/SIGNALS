# quest-rubric Variate -- Round 15 (Against rubric v16, targeting C-41/C-42)
**Date:** 2026-03-16
**Rubric:** v15 (C-01--C-42; denominator /34; adds C-41: pre-emit evidence-quotation gate
requiring quoted text from two structural loci, C-42: dual-path DFM enforcement declaration
stating per-phase and pre-emit gates as non-redundant independently necessary mechanisms)
**Target criteria:** C-41, C-42 (new -- first probe round); C-39, C-40 (stability under
pre-emit gate pressure)

**Round 15 design note:** Round 14 produced excellence signals ES-R14-1 (Phase 8.5 pre-emit
gate resolves previously-partial audit-trail criterion by requiring quoted structural labels
from two loci) and ES-R14-2 (layered dual-path enforcement -- per-phase SCOPE GATE +
independent pre-emit gate -- operate at structurally distinct phases). V-05 passed both
C-41 and C-42; V-04 demonstrated PASS C-39 / PASS C-40 / FAIL C-41. Rubric v15 elevates
both to aspirational criteria (denominator /32 -> /34).

R15 targets:
(1) Isolate whether a Phase 8.5 EVIDENCE QUOTATION GATE alone (with no non-redundancy
    declaration) achieves C-41 independently of C-42;
(2) Isolate whether a NON-REDUNDANCY DECLARATION in the EMIT manifest achieves C-42
    without a Phase 8.5 blocking gate (ablating C-41);
(3) Test whether STATUS QUO COMPETITOR foil items naming single-path failure and missing
    evidence-quotation achieve PARTIAL on both via concept-awareness contrast;
(4) Combine Phase 8.5 gate (axis 1) and NON-REDUNDANCY DECLARATION (axis 2) to probe
    whether both criteria pass simultaneously;
(5) Add DUAL-PATH ENFORCEMENT DECLARATION with per-mechanism failure-mode arguments to the
    combined stack, extending the non-redundancy property from emit-manifest row to
    independently-stated section.

**C-41 vs C-42 -- distinction summary:**

- **C-41** governs the *pre-emit evidence-quotation gate*: a Phase 8.5 gate positioned after
  the final construction role (BUILDER ASPIRATIONAL) and before the artifact emission step
  (PHASE 9 EMIT). The gate requires the builder to produce quoted text from two structural
  loci: (a) the Scope Gatekeeper prohibition clause, showing that the structural DFM label
  appears in the prohibition text; and (b) the output instruction clause, showing that the
  label-carry requirement appears in the emit directive. Both quotations must be present and
  attributed to their structural source. The gate blocks emission if either quotation is
  absent or the quoted text does not contain the required label. V-04 demonstrates PASS C-39
  / PASS C-40 / FAIL C-41: structural enforcement is present at construction time, but no
  pre-emit gate independently re-verifies compliance from artifact text.

- **C-42** governs the *dual-path enforcement declaration*: the skill prompt must declare
  that the per-phase SCOPE GATE (Phase 5, construction time) and the pre-emit Phase 8.5
  gate are non-redundant enforcement points, each independently necessary, operating at
  structurally distinct phases. The declaration must include per-mechanism failure-mode
  arguments: removing SCOPE GATE leaves the prohibition text free to use prose description
  rather than structural label citation; removing Phase 8.5 gate leaves DFM label propagation
  unverifiable from artifact text alone. A prompt containing both mechanisms with no explicit
  non-redundancy statement does not satisfy C-42. The non-redundancy must be stated positively
  ("each is independently necessary because removing either causes exactly one enforcement
  path to fail") rather than shown only by negative example.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|-------------------|----|
| Role sequence | C-41 | Phase 8.5 EVIDENCE QUOTATION GATE after BUILDER ASPIRATIONAL; requires quoted evidence from SCOPE GATE prohibition clause + Phase 9 emit instruction; C-42 ablated (no non-redundancy declaration) |
| Output format | C-42 | NON-REDUNDANCY DECLARATION row in EMIT manifest declares per-phase and pre-emit gates as independently necessary; Phase 9 EMIT opens with declaration; C-41 ablated (no blocking Phase 8.5 gate) |
| Inertia framing | C-41 partial / C-42 partial | STATUS QUO COMPETITOR extended with single-path enforcement foil items; concept-awareness without structural enforcement; both criteria addressed via contrast inference only |
| Role sequence + Output format | C-41 + C-42 | Phase 8.5 gate (role sequence axis) + NON-REDUNDANCY DECLARATION in EMIT (output format axis) simultaneously active |
| Role sequence + Output format + Phrasing register | C-41 + C-42 + independence-verifiability | V-04 mechanisms + DUAL-PATH ENFORCEMENT DECLARATION section between SCOPE GATEKEEPER and Phase 8.5; per-mechanism failure-mode arguments; C-41 independence note in gate |

Single-axis: V-01 (role sequence), V-02 (output format), V-03 (inertia framing).
Combined: V-04 (role sequence + output format), V-05 (role sequence + output format +
phrasing register).

---

## Round 15 Variation Map

| Variation | Axis | C-41 probe | C-42 probe | C-39 | C-40 | Notes |
|-----------|------|-----------|-----------|------|------|-------|
| V-01 | Role sequence | Very strong -- Phase 8.5 EVIDENCE QUOTATION GATE; requires quoted evidence from both structural loci; gate blocks emission if absent | Ablated -- no NON-REDUNDANCY DECLARATION; SCOPE GATE and Phase 8.5 gate both present but their non-redundancy not stated | Stable from R14 | Stable from R14 | Single-axis; isolation control for C-41 |
| V-02 | Output format | Ablated -- no Phase 8.5 blocking gate; Phase 8.5 check present but advisory | Very strong -- EMIT manifest NON-REDUNDANCY DECLARATION row; per-mechanism failure-mode arguments stated | Stable from R14 | Stable from R14 | Single-axis; isolation control for C-42 |
| V-03 | Inertia framing | Partial (predicted) -- STATUS QUO COMPETITOR foil item names single-path-enforcement failure; no structural gate | Partial (predicted) -- STATUS QUO COMPETITOR foil item names missing non-redundancy; no positive declaration | Stable from R14 | Stable from R14 | Single-axis; ablation control for both |
| V-04 | Role sequence + Output format | Strong -- Phase 8.5 EVIDENCE QUOTATION GATE (same as V-01) | Strong -- NON-REDUNDANCY DECLARATION in EMIT (same as V-02) | Stable | Stable | Combined; first simultaneous probe |
| V-05 | Full stack | Strong (same as V-04) + independence note in gate body | Strong (same as V-04) + DUAL-PATH ENFORCEMENT DECLARATION with per-mechanism arguments + STATUS QUO COMPETITOR foil items | Stable | Stable | Ceiling: all mechanisms; DUAL-PATH DECLARATION is named section not just emit row |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- Phase 8.5 EVIDENCE QUOTATION GATE inserted after ROLE: BUILDER
ASPIRATIONAL, before PHASE 9. The gate requires the builder to produce quoted evidence
from two structural loci: (a) the Phase 5 SCOPE CONSTRAINT prohibition clause showing the
structural DFM label, and (b) the Phase 9 output instruction clause showing the label-carry
requirement. The gate blocks emission if either quotation is absent or the quoted text does
not contain the required label. C-42 is ablated: no NON-REDUNDANCY DECLARATION; SCOPE GATE
and Phase 8.5 gate are both present but their non-redundancy is not stated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-01 will include a Phase 8.5 gate requiring quoted evidence from both structural loci before emission; the primary falsification signal is a rubric where the gate exists but accepts prose summaries of the prohibition clause rather than verbatim quotations -- confirming C-41 requires the blocking quotation requirement, not mere gate presence. | The Phase 8.5 gate, by requiring the builder to quote Phase 9's emit instruction, may cause the builder to revise Phase 9 to be more explicit about the label-carry requirement -- a proximity-induced vocabulary improvement for C-40. | C-41 primary test: Phase 8.5 section heading "EVIDENCE QUOTATION GATE" present; Quotation A and Quotation B both required and attributed; blocking gate condition explicit. C-42 test: absent -- no independence declaration between SCOPE GATE and Phase 8.5. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

- Fails to enumerate failure modes before drafting -- criteria come from intuition about
  good output rather than from systematic analysis of broken output.
- Fails to produce causal direction templates -- Text fields describe presence of good
  properties, not consequence of their absence.
- Fails to enforce Pass observability by template -- Pass conditions include qualitative
  language as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier -- category distribution is checked globally
  rather than per tier, making tier convergence invisible.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.**

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1. Do not write any criterion fields during this role.**

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass
template), no additional content.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION: Rewrite before proceeding if the output of this role contains anything
beyond the two required templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply Text template and Pass template from ROLE: CRITERION
DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

Count category assignments per tier. Majority per tier:

```
Essential tier:    [category] x[N] -- majority: [category]
Recommended tier:  [category] x[N] -- majority: [category]
```

If essential and recommended share the same majority, flag before proceeding to Phase 5.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Dominant Failure Mode: [label exactly as it will appear in the Design Rationale block]

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**SCOPE GATE:** Each criterion that references a failure mode in its prohibition text must
cite the structural "Dominant Failure Mode" label declared above -- not merely describe the
failure mode in prose. A prohibition text reading "avoids the dominant failure mode" does
NOT satisfy the gate. A prohibition text reading "avoids the Dominant Failure Mode: [label]"
DOES satisfy the gate. These two outputs are structurally distinct.

**SCOPE GATE exit condition:** All criteria reviewed. Any criterion referencing failure mode
via prose description (without the structural label) is revised before ROLE: MECHANISM
DEFINER begins.

**Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

#### Step 1 -- Independence Map

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only."

#### Step 2 -- PHASE-LOCALITY RULE

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
fall in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition,
subject to the PHASE-LOCALITY RULE:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. Notes: "closes gap via [mechanism name] per independence
map | DEFINER OUTPUT GATE: Two slot-fillable templates | MECHANISM DEFINER GATE: Independence
Map | PHASE-LOCALITY RULE: applied | competitor: [first four words]."

STOP conditions:
- An aspirational criterion whose Notes field lacks all three gate/rule identifiers: rewrite.
- COMPETITOR block ending with failure description rather than derivation instruction: rewrite.
- Competitor placed in any PHASE-LOCALITY RULE prohibited zone: move before proceeding.

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [observable anchor]                         |
| PARTIAL | 0.5         | [observable anchor]                         |
| FAIL    | 0.0         | [observable anchor]                         |
```

Every criterion must have all three states named. A scoring section naming PASS and FAIL
without PARTIAL is incomplete.

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/[N] x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /[N] where N = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL is complete. All criteria drafted and sealed.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label. The quoted text must include the structural
> label name as it appears in the SCOPE CONSTRAINT block.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's purpose statement or Design Rationale.

**Gate condition:** STOP if either quotation is absent. STOP if the quoted text does not
contain the structural "Dominant Failure Mode" label or its designated equivalent. Both
quotations must be present and attributed to their source section before Phase 9 begins.

This gate is independent of the Phase 5 SCOPE GATE. Passing the SCOPE GATE (construction
phase) does not satisfy this gate. Both gates operate at structurally distinct phases and
must be satisfied independently.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label (not prose
description).**

**PREREQUISITE: Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A and Quotation B both present
and attributed.**

Output the complete rubric document in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- Dominant Failure Mode block (label must match Phase 5 SCOPE
   CONSTRAINT declaration), self-application, >= 3 rejected generic criteria with reasons;
   must appear before the first criteria table. **STOP if Design Rationale omits the
   Dominant Failure Mode block or if the block does not carry the structural label from
   Phase 5 SCOPE CONSTRAINT verbatim.**
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites all three gate/rule identifiers
8. **Scoring** -- composite formula, denominator, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

STOP CONDITION -- Phase 9: The emit is incomplete if Design Rationale does not contain the
Dominant Failure Mode block with the structural label from Phase 5 SCOPE CONSTRAINT.

---

## V-02 -- Output Format

**Axis:** Output format -- EMIT manifest restructured to include a NON-REDUNDANCY DECLARATION
row. The declaration states that Phase 5 SCOPE GATE (construction-phase enforcement) and
the Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each
independently necessary: removing SCOPE GATE allows prose description to pass without
structural label citation; removing the Phase 9 STOP CONDITION allows the Design Rationale
to omit the Dominant Failure Mode label. Phase 8.5 is present as an advisory check but is
NOT a blocking gate -- the builder records the two quotations but emission is not blocked
if they are absent. C-41 is ablated; C-42 is strongly targeted.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-02 will contain a Phase 9 EMIT manifest row declaring Phase 5 SCOPE GATE and Phase 9 STOP CONDITION as non-redundant enforcement points, each with a per-mechanism failure-mode argument; the primary falsification signal is a rubric where the manifest acknowledges both mechanisms but omits the failure-mode argument for each (confirming C-42 requires the per-mechanism argument, not just co-presence). | The NON-REDUNDANCY DECLARATION in the EMIT manifest may cause a proximity effect: a builder who writes the manifest row may revise Phase 9's STOP CONDITION to reference the declaration by name, strengthening C-40 specificity as a side effect. | C-42 primary test: EMIT manifest row "NON-REDUNDANCY DECLARATION" present with two failure-mode arguments. C-41 test: Phase 8.5 is advisory-only; no blocking gate; predicts FAIL C-41. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

- Fails to enumerate failure modes before drafting -- criteria come from intuition about
  good output rather than from systematic analysis of broken output.
- Fails to produce causal direction templates -- Text fields describe presence of good
  properties, not consequence of their absence.
- Fails to enforce Pass observability by template -- Pass conditions include qualitative
  language as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier -- category distribution is checked globally
  rather than per tier, making tier convergence invisible.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass
template), no additional content.**

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails." Prohibited: causality located in wrong form's
consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.

STOP CONDITION: Rewrite if output contains criterion fields, narrative, or anything beyond
the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from blocking failure modes. Apply Text template and Pass template. Competitor blocks
immediately before the criterion they govern.

Five fields per criterion: C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.
Competitor blocks immediately before the criterion.

Five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Text field checks: Direction, Contrast, Causal chain.
Pass field checks: Location, Observable, No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit does not separate
> assignments by tier and does not check whether different tiers have different majority
> categories. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

Count category assignments per tier. Majority per tier. Flag if essential and recommended
share the same majority before proceeding to Phase 5.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Dominant Failure Mode: [label exactly as it will appear in the Design Rationale block]

Essential coverage: [C-NN guards against: one-line description per criterion.]

Recommended coverage: [C-NN guards the [dimension] of [property] -- one line.]

Threshold escalation prohibition: An aspirational criterion at a higher threshold of an
  already-covered property is not aspirational.

Gap zone: Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
  Observable: what would an evaluator check?]
```

**SCOPE GATE:** Each criterion referencing a failure mode in its prohibition text must cite
the structural "Dominant Failure Mode" label declared above -- not merely describe the
failure mode in prose. Prose-only prohibition does NOT satisfy the gate. Label citation DOES.

**SCOPE GATE exit condition:** All criteria reviewed; any criterion using prose-only
prohibition revised before ROLE: MECHANISM DEFINER begins.

Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.

---

### ROLE: MECHANISM DEFINER

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations and all rows
"Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

Independence Map:

```
| Mechanism name | What it does (one sentence) | Criterion affected | Independent? |
|----------------|----------------------------|--------------------|--------------|
| [name]         | [one sentence]              | C-NN               | Yes -- affects C-NN only |
```

PHASE-LOCALITY RULE: Named competitors may not appear in (1) preamble zone, (2)
shared-operating-principles zone, or (3) multi-criterion zone.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE. PREREQUISITE: MECHANISM DEFINER GATE.**

Write 1-2 aspirational criteria from the gap zone. Competitor immediately before each
criterion (PHASE-LOCALITY RULE applies). Five fields + Notes citing all three gate/rule
identifiers.

STOP conditions:
- Notes field missing gate/rule identifiers: rewrite.
- Competitor block ends with failure description rather than derivation instruction: rewrite.
- Competitor in any prohibited zone: move before proceeding.

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [observable anchor]                         |
| PARTIAL | 0.5         | [observable anchor]                         |
| FAIL    | 0.0         | [observable anchor]                         |
```

Every criterion must have all three states named.

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/[N] x 10)`
**Golden threshold:** >= [NN]

---

### PHASE 8.5 -- EVIDENCE REVIEW (advisory)

Before Phase 9, produce quoted text from two structural loci (advisory -- emission not
blocked if absent):

- Quotation A: text from Phase 5 SCOPE GATE prohibition clause containing "Dominant
  Failure Mode."
- Quotation B: text from Phase 9 EMIT instruction requiring Dominant Failure Mode label
  in Design Rationale.

Record both quotations before proceeding. This step is a construction record, not a gate.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label.**

Output the complete rubric document:

1. Failure Mode Log
2. Design Rationale -- Dominant Failure Mode block (label from Phase 5 SCOPE CONSTRAINT),
   self-application, >= 3 rejected generic criteria. **STOP if Dominant Failure Mode block
   absent or label does not match Phase 5 declaration.**
3. Essential Criteria
4. Recommended Criteria
5. Independence Map + PHASE-LOCALITY RULE
6. Aspirational Criteria (COMPETITOR blocks inline)
7. Scoring (formula, denominator, threshold, three-state table)
8. Notes + vN Candidates

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no other content) | |
| MECHANISM DEFINER GATE satisfied (Independence Map, all C-NN cited) | |
| SCOPE GATE exit condition satisfied (all criteria cite DFM label) | |
| Phase 9 Design Rationale contains Dominant Failure Mode block | |
| COMPETITOR coverage: one competitor per aspirational criterion | |
| PHASE-LOCALITY RULE: no competitor in any prohibited zone | |
| Aspirational count: 1-2 criteria | |
| Three-state scoring table present (PASS / PARTIAL / FAIL) | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE and Phase 9 STOP CONDITION are non-redundant enforcement points. Each is independently necessary: removing SCOPE GATE allows prose-only prohibition to pass; removing Phase 9 STOP CONDITION allows Design Rationale to omit Dominant Failure Mode label. These two mechanisms are the load-bearing enforcement paths for DFM label propagation.** | |

STOP if NON-REDUNDANCY DECLARATION row is not present in the emit manifest or if it omits
either per-mechanism failure-mode argument.

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- STATUS QUO COMPETITOR extended with two new foil items naming
the C-41 and C-42 failure patterns: single-path DFM enforcement (only per-phase, no
pre-emit gate) and missing non-redundancy declaration (both mechanisms present but
non-redundancy not stated). Both C-41 and C-42 are addressed via contrast inference only;
no structural Phase 8.5 gate, no positive NON-REDUNDANCY DECLARATION. Predicts PARTIAL on
C-42 (concept-awareness) and FAIL on C-41 (no blocking gate present).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| The STATUS QUO COMPETITOR foil items establish concept-awareness of single-path failure and missing non-redundancy, but without a positive declaration or blocking gate, neither C-41 nor C-42 will fully pass; predicted: C-41 FAIL (no Phase 8.5 gate), C-42 PARTIAL (foil items name the gap but no positive statement); this mirrors the inertia-framing pattern from R14 V-03. | A rubric builder who reads the foil items may spontaneously add a non-redundancy note to the Design Rationale or Notes section, partially satisfying C-42 as a proximity artifact. This would test whether the PARTIAL condition for C-42 can be met by foil-induced spontaneous addition rather than a positive instruction. | C-41 test: no Phase 8.5 section present; FAIL. C-42 test: foil items mention non-redundancy concept; PARTIAL if rubric mentions the concept in Design Rationale or Notes without a dedicated declaration block. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

- Fails to enumerate failure modes before drafting -- criteria come from intuition about
  good output rather than from systematic analysis of broken output.
- Fails to produce causal direction templates -- Text fields describe presence of good
  properties, not consequence of their absence.
- Fails to enforce Pass observability by template -- Pass conditions include qualitative
  language as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier.
- **Fails to include a pre-emit evidence-verification gate** -- DFM label propagation is
  enforced only at construction time via the per-phase SCOPE GATE; no independent gate
  verifies compliance from artifact text before emission. A builder who satisfies the SCOPE
  GATE during construction but modifies the prohibition text afterward will not be caught.
- **Fails to declare enforcement mechanisms as non-redundant** -- when a per-phase gate and
  an emit-phase STOP CONDITION both reference DFM propagation, their independence is assumed
  but not stated; removing either mechanism's failure-mode is invisible without a positive
  non-redundancy statement.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass
template), no additional content.**

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

STOP CONDITION: Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from blocking failure modes. Apply templates. Competitor blocks immediately before
their criterion.

Five fields: C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from suboptimal failure modes. Five fields. **Dimension:** annotation.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

Text: Direction, Contrast, Causal chain. Pass: Location, Observable, No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

> **TIER-BLIND CATEGORIZER** -- [standard inertia block: does not check tier majority].
> From the description above, derive the required divergence check before reading below.

Category majority per tier. Flag convergence before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Dominant Failure Mode: [label]
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property]...]
Threshold escalation prohibition: [...]
Gap zone: Gap G-01: [property / observable]
```

**SCOPE GATE:** Criteria referencing failure mode in prohibition text must cite the structural
"Dominant Failure Mode" label -- not prose description.

SCOPE GATE exit condition: All criteria reviewed; prose-only prohibitions revised.

---

### ROLE: MECHANISM DEFINER

Independence Map + PHASE-LOCALITY RULE.

MECHANISM DEFINER GATE: All rows "Yes -- affects C-NN only," PHASE-LOCALITY RULE stated.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE. PREREQUISITE: MECHANISM DEFINER GATE.**

1-2 aspirational criteria from gap zone. Competitor immediately before each. Notes cite
all three gate/rule identifiers.

---

### PHASE 8 -- SCORING

Three-state scoring table. Composite formula. Denominator. Golden threshold.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition.**

Output:
1. Failure Mode Log
2. Design Rationale -- Dominant Failure Mode block, self-application, >= 3 rejected generic.
   STOP if DFM block absent or label differs from Phase 5 declaration.
3. Essential Criteria
4. Recommended Criteria
5. Independence Map + PHASE-LOCALITY RULE
6. Aspirational Criteria (COMPETITOR blocks inline)
7. Scoring
8. Notes + vN Candidates

Emit manifest: standard checks (DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, SCOPE GATE,
DFM block, competitor coverage, PHASE-LOCALITY RULE, aspirational count, three-state table).

---

## V-04 -- Combined (Role Sequence + Output Format)

**Axis:** Role sequence + output format combined. V-01 Phase 8.5 EVIDENCE QUOTATION GATE
(blocking, requires Quotation A and Quotation B) is present and active. V-02 NON-REDUNDANCY
DECLARATION row is present in the EMIT manifest. Both C-41 and C-42 are structurally
enforced simultaneously. First combined probe: tests whether C-41 and C-42 can both pass
on top of the C-39/C-40 baseline without disrupting each other.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-04 will include Phase 8.5 EVIDENCE QUOTATION GATE (Quotation A + Quotation B required) and a NON-REDUNDANCY DECLARATION row in the EMIT manifest; both C-41 and C-42 are predicted to pass; primary falsification signal: Phase 8.5 present but EMIT manifest NON-REDUNDANCY row absent (suggesting the two mechanisms are competing for the builder's attention, with Phase 8.5 displacing the manifest requirement). | The combined activation of Phase 8.5 (which requires quoting Phase 9 EMIT instruction text) and the EMIT manifest NON-REDUNDANCY row (which requires naming both mechanisms in the manifest) may cause the builder to cross-reference them, producing a rubric where the NON-REDUNDANCY DECLARATION cites the Phase 8.5 gate by name -- making the declaration more specific and potentially satisfying C-42 at a higher level than V-02 alone. | C-41 primary test: Phase 8.5 section present with two named quotation requirements and a blocking STOP. C-42 primary test: EMIT manifest NON-REDUNDANCY DECLARATION row present with two failure-mode arguments. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

**What it does not do:**

- Fails to enumerate failure modes before drafting.
- Fails to produce causal direction templates.
- Fails to enforce Pass observability by template.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. Do not begin ROLE: CRITERION DEFINER until complete.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
```

**Pass template:**
```
LOCATION: [field or section]
OBSERVABLE: [token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

STOP CONDITION: Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Blocking failure modes. Templates applied. Competitors immediately before their criterion.
Five fields: C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Suboptimal failure modes. Five fields. **Dimension:** annotation.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

Text: Direction, Contrast, Causal chain. Pass: Location, Observable, No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

> **TIER-BLIND CATEGORIZER** -- does not check tier majority. From the description above,
> derive the required divergence check before reading below.

Category majority per tier. Flag convergence.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Dominant Failure Mode: [label]
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [...]
Threshold escalation prohibition: [...]
Gap zone: Gap G-01: [property / observable]
```

**SCOPE GATE:** Each criterion referencing a failure mode must cite the structural
"Dominant Failure Mode" label -- not prose description. These two outputs are structurally
distinct. Prose-only does NOT satisfy the gate; label citation DOES.

SCOPE GATE exit condition: All criteria reviewed; prose-only prohibitions revised.

---

### ROLE: MECHANISM DEFINER

Independence Map + PHASE-LOCALITY RULE. MECHANISM DEFINER GATE: all rows "Yes -- affects
C-NN only," PHASE-LOCALITY RULE stated.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE. PREREQUISITE: MECHANISM DEFINER GATE.**

1-2 aspirational criteria from gap zone. Competitor immediately before each (PHASE-LOCALITY
RULE). Notes cite all three gate/rule identifiers.

---

### PHASE 8 -- SCORING

Three-state table. Composite formula. Denominator. Golden threshold.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. All criteria drafted and sealed.

Produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from Phase 5 SCOPE GATE that contains the structural "Dominant
> Failure Mode" label.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 EMIT that requires the Dominant Failure Mode label in
> the Design Rationale.

**Gate condition:** STOP if either quotation is absent. STOP if the quoted text does not
contain "Dominant Failure Mode" or its structural equivalent. Both quotations must be
present and attributed before Phase 9 begins.

This gate operates independently of the Phase 5 SCOPE GATE. Satisfying the SCOPE GATE does
not satisfy this gate.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label.**
**PREREQUISITE: Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A and Quotation B present
and attributed.**

Output in order:
1. Failure Mode Log
2. Design Rationale -- Dominant Failure Mode block (label from Phase 5 verbatim), self-
   application, >= 3 rejected generic criteria. **STOP if DFM block absent or label differs.**
3. Essential Criteria
4. Recommended Criteria
5. Independence Map + PHASE-LOCALITY RULE
6. Aspirational Criteria (COMPETITOR blocks inline)
7. Scoring (formula, denominator, threshold, three-state table)
8. Notes + vN Candidates

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied | |
| MECHANISM DEFINER GATE satisfied | |
| SCOPE GATE exit condition satisfied | |
| Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A + Quotation B present | |
| Design Rationale contains Dominant Failure Mode block | |
| COMPETITOR coverage: one per aspirational criterion | |
| PHASE-LOCALITY RULE: no competitor in any prohibited zone | |
| Aspirational count: 1-2 criteria | |
| Three-state scoring table present | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass; removing Phase 9 STOP CONDITION allows Design Rationale to omit Dominant Failure Mode label.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or missing either per-mechanism argument.

---

## V-05 -- Full Stack

**Axis:** Role sequence + output format + phrasing register. All V-04 mechanisms present:
Phase 8.5 EVIDENCE QUOTATION GATE (blocking, Quotation A + Quotation B required) and
NON-REDUNDANCY DECLARATION row in EMIT manifest. Additionally: a DUAL-PATH ENFORCEMENT
DECLARATION section is added between SCOPE GATEKEEPER and Phase 8.5. This section explicitly
states (a) the two enforcement paths are independent -- each fails separately when the
other is removed; (b) the construction-time path (SCOPE GATE) and the pre-emit path (Phase
8.5) operate at structurally distinct phases; and (c) a rubric satisfying only one path
achieves single-path enforcement rather than dual-path enforcement. STATUS QUO COMPETITOR
extended with the two foil items from V-03.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric from V-05 includes Phase 8.5 blocking gate (C-41), NON-REDUNDANCY DECLARATION in manifest (C-42), and DUAL-PATH ENFORCEMENT DECLARATION named section (C-42 stronger than V-04); primary comparison: V-04 passes C-42 via emit-manifest row, V-05 passes C-42 via a named section with per-mechanism failure-mode arguments that also confirm each mechanism fails independently -- the named section makes the non-redundancy property independently auditable from the DUAL-PATH DECLARATION section alone without reading the manifest row. | The DUAL-PATH ENFORCEMENT DECLARATION's requirement that each path "fails independently when the other is removed" may cause the builder to add failure-mode arguments to Phase 8.5 EVIDENCE QUOTATION GATE as well, making the gate more self-describing and increasing C-41 Pass condition specificity beyond V-04 levels. | C-41 test: Phase 8.5 section with two named quotation requirements, blocking STOP, independence note in gate body. C-42 test: both EMIT manifest NON-REDUNDANCY row and DUAL-PATH ENFORCEMENT DECLARATION named section present; named section includes per-mechanism failure-mode arguments and structural-phase distinction. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

**What it does not do:**

- Fails to enumerate failure modes before drafting.
- Fails to produce causal direction templates.
- Fails to enforce Pass observability by template.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier.
- **Fails to include a pre-emit evidence-verification gate** -- DFM label propagation is
  enforced only at construction time; no independent gate verifies compliance from artifact
  text before emission. A builder who satisfies the SCOPE GATE but modifies prohibition text
  afterward is not caught.
- **Fails to declare enforcement mechanisms as non-redundant** -- per-phase gate and
  emit-phase STOP CONDITION both reference DFM propagation but their independence is never
  stated; removing either mechanism's failure scope is invisible without a positive
  non-redundancy statement.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. Do not begin ROLE: CRITERION DEFINER until complete.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```

**Pass template:**
```
LOCATION: [field or section]
OBSERVABLE: [token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

STOP CONDITION: Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Blocking failure modes. Templates applied. Competitors immediately before their criterion.
C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Suboptimal failure modes. Five fields. **Dimension:** annotation.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

Text: Direction, Contrast, Causal chain. Pass: Location, Observable, No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

> **TIER-BLIND CATEGORIZER** -- does not check tier majority. From the description above,
> derive the required divergence check before reading below.

Category majority per tier. Flag convergence.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Dominant Failure Mode: [label -- will be cited structurally in all downstream prohibition text]
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property]...]
Threshold escalation prohibition: [...]
Gap zone: Gap G-01: [property / observable]
```

**SCOPE GATE:** Each criterion referencing a failure mode in its prohibition text must cite
the structural "Dominant Failure Mode" label as declared above -- not merely describe the
failure mode in prose. These two outputs are structurally distinct:
- Non-compliant: "avoids the dominant failure mode" (prose description)
- Compliant: "avoids the Dominant Failure Mode: [label]" (structural citation)

**SCOPE GATE exit condition:** All criteria reviewed; prose-only prohibitions revised before
ROLE: MECHANISM DEFINER begins. SCOPE GATE exit condition is the construction-phase
enforcement path for DFM label propagation.

---

### ROLE: MECHANISM DEFINER

Independence Map + PHASE-LOCALITY RULE. MECHANISM DEFINER GATE: all rows "Yes -- affects
C-NN only," PHASE-LOCALITY RULE stated.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE. PREREQUISITE: MECHANISM DEFINER GATE.**

1-2 aspirational criteria from gap zone. Competitor immediately before each (PHASE-LOCALITY
RULE). Notes cite all three gate/rule identifiers.

---

### DUAL-PATH ENFORCEMENT DECLARATION

This section is a structural declaration and does not produce criteria. It is placed after
ROLE: BUILDER ASPIRATIONAL and before Phase 8.5.

```
DUAL-PATH ENFORCEMENT DECLARATION:

Enforcement path 1 (construction-phase):
  Mechanism: SCOPE GATE (Phase 5 SCOPE CONSTRAINT exit condition)
  Phase: construction -- runs while criteria are being drafted
  Failure mode covered: prohibition text uses prose description instead of structural
    label citation; SCOPE GATE exit condition requires revision before construction ends
  Independent necessity: removing this mechanism leaves the pre-emit gate as the sole
    enforcement path; a builder may draft non-compliant prohibition text and only be
    caught at the pre-emit phase -- DFM propagation compliance is not enforced during
    construction

Enforcement path 2 (pre-emit):
  Mechanism: Phase 8.5 EVIDENCE QUOTATION GATE
  Phase: pre-emit -- runs after construction is complete, before artifact emission
  Failure mode covered: DFM label propagation compliance cannot be verified from artifact
    text alone without re-running construction; Phase 8.5 gate requires quoted evidence
    from structural loci, making compliance independently verifiable
  Independent necessity: removing this mechanism leaves Phase 5 SCOPE GATE as the sole
    enforcement path; a builder who satisfies the SCOPE GATE but later modifies prohibition
    text will not be caught; compliance is not independently verifiable from artifact text

Non-redundancy: these two mechanisms are non-redundant. Removing either enforcement path
  causes exactly one coverage gap. A rubric with only path 1 fails independently at the
  pre-emit phase. A rubric with only path 2 fails independently at the construction phase.
  Together they constitute dual-path enforcement: construction-time compliance + pre-emit
  independent verification.
```

**STOP if this declaration is absent before Phase 8.5 begins.**

---

### PHASE 8 -- SCORING

Three-state table. Composite formula. Denominator. Golden threshold.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from Phase 5 SCOPE GATE that contains the structural "Dominant
> Failure Mode" label. The quoted text must include the label as it appears in the SCOPE
> CONSTRAINT block -- not a paraphrase.
>
> This quotation confirms that the construction-phase enforcement path (SCOPE GATE, path 1
> per DUAL-PATH ENFORCEMENT DECLARATION) names the structural label in its exit condition.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 EMIT that requires the Dominant Failure Mode label in
> the Design Rationale. The quoted text must include the STOP CONDITION referencing the
> label.
>
> This quotation confirms that the emit-phase enforcement exists as an explicit instruction
> (not just a design intent), independently verifiable from the Phase 9 EMIT instruction
> alone.

**Gate condition:** STOP if either quotation is absent. STOP if the quoted text does not
contain the structural label or its designated equivalent. STOP if either quotation does not
name its source section. Both quotations must be present and attributed before Phase 9 begins.

This gate is the pre-emit enforcement path (path 2 per DUAL-PATH ENFORCEMENT DECLARATION).
It operates at a structurally distinct phase from the SCOPE GATE (path 1, construction
phase). Satisfying the SCOPE GATE does not satisfy this gate.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label.**
**PREREQUISITE: Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A and Quotation B present,
attributed to their source sections.**

Output in order:
1. Failure Mode Log
2. Design Rationale -- Dominant Failure Mode block (label from Phase 5 SCOPE CONSTRAINT
   verbatim), self-application, >= 3 rejected generic criteria. **STOP if DFM block absent
   or label differs from Phase 5 SCOPE CONSTRAINT declaration.**
3. Essential Criteria
4. Recommended Criteria
5. Independence Map + PHASE-LOCALITY RULE
6. Aspirational Criteria (COMPETITOR blocks inline; Notes cite all gate/rule identifiers)
7. Scoring (formula, denominator, threshold, three-state table)
8. Notes + vN Candidates

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| MECHANISM DEFINER GATE satisfied (Independence Map, all C-NN cited) | |
| SCOPE GATE exit condition satisfied (all criteria cite DFM label, not prose) | |
| Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A present and attributed | |
| Phase 8.5 EVIDENCE QUOTATION GATE: Quotation B present and attributed | |
| DUAL-PATH ENFORCEMENT DECLARATION recorded (two paths, non-redundancy stated) | |
| Design Rationale contains Dominant Failure Mode block with Phase 5 label | |
| COMPETITOR coverage: one competitor per aspirational criterion | |
| PHASE-LOCALITY RULE: no competitor in any prohibited zone | |
| Aspirational count: 1-2 criteria | |
| Three-state scoring table present (PASS / PARTIAL / FAIL with earn conditions) | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE and Phase 9 STOP CONDITION are non-redundant enforcement points. Removing SCOPE GATE: prose-only prohibition passes construction phase unchallenged. Removing Phase 9 STOP CONDITION: DFM label propagation unverifiable from emitted artifact. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is missing.
STOP if DUAL-PATH ENFORCEMENT DECLARATION was not recorded before Phase 8.5.
