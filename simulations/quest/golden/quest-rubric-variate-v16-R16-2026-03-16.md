# quest-rubric Variate -- Round 16 (Against rubric v16, targeting C-43/C-44)

**Date:** 2026-03-16
**Rubric:** v16 (C-01--C-44; denominator /36; adds C-43: per-quotation path attribution
inside the pre-emit gate -- each Quotation requirement carries an in-gate note naming
which enforcement path it confirms, making the gate self-contextualizing; adds C-44:
non-redundancy declaration at two structural loci -- both a named pre-gate section
(DUAL-PATH ENFORCEMENT DECLARATION) and the EMIT manifest row, creating defense-in-depth
for the non-redundancy property itself)
**Target criteria:** C-43, C-44 (new -- first probe round); C-41, C-42 (stability)

**Round 16 design note:** Round 15 produced excellence signals ES-R15-1 and ES-R15-2 from
V-05. V-05 passed both C-43 and C-44 (the two new aspirational criteria added to rubric
v16). V-04 passed C-41 and C-42 but failed C-43 (Phase 8.5 blocking gate with Quotation
A and B present, but no in-gate notes naming which enforcement path each quotation
confirms) and failed C-44 (NON-REDUNDANCY DECLARATION present only in the EMIT manifest
row -- one structural locus -- rather than at two independent structural loci). Rubric v16
elevates both to aspirational criteria (denominator /34 -> /36). R16 targets:
(1) Isolate whether per-quotation path attribution notes in Phase 8.5 (without a
    DUAL-PATH ENFORCEMENT DECLARATION section) achieve C-43 independently of C-44;
(2) Isolate whether a DUAL-PATH ENFORCEMENT DECLARATION named section (without
    per-quotation path attribution in Phase 8.5) achieves C-44 independently of C-43;
(3) Test whether STATUS QUO COMPETITOR foil items naming absent path attribution and
    single-locus non-redundancy achieve PARTIAL on both via concept-awareness contrast;
(4) Combine per-quotation path attribution (axis 1) and DUAL-PATH ENFORCEMENT DECLARATION
    (axis 2) to probe whether both criteria pass simultaneously;
(5) Add phrasing register to the combined stack -- explicit structural-phase labeling per
    quotation, naming which mechanism the quotation verifies and why that phase is distinct.

**C-43 vs C-44 -- distinction summary:**

- **C-43** governs *per-quotation path attribution inside the pre-emit gate*: the Phase 8.5
  EVIDENCE QUOTATION GATE requires the builder to produce two quotations (Quotation A from
  the Phase 5 SCOPE GATE prohibition clause; Quotation B from the Phase 9 EMIT instruction).
  C-43 requires that each quotation requirement in the gate body carries an in-gate note
  immediately following the quotation header, naming which enforcement path that quotation
  confirms. Quotation A's note names path 1 (construction-phase SCOPE GATE). Quotation B's
  note names path 2 (emit-phase STOP CONDITION). The notes make the gate self-contextualizing:
  a reviewer can trace each quotation to its enforcement path from within the gate text,
  without reading the DUAL-PATH ENFORCEMENT DECLARATION or surrounding prompt structure.
  V-04 demonstrates PASS C-41 / PASS C-42 / FAIL C-43: blocking gate is present with
  Quotation A and B required, but no in-gate notes name the enforcement path each confirms.

- **C-44** governs *non-redundancy declaration at two structural loci*: the skill prompt
  must declare the non-redundancy of the two DFM enforcement paths (Phase 5 SCOPE GATE and
  Phase 9 STOP CONDITION) at both (a) a named pre-gate section (DUAL-PATH ENFORCEMENT
  DECLARATION, positioned before Phase 8.5) with structural-phase distinction and
  per-mechanism failure-mode arguments, and (b) the EMIT manifest row (NON-REDUNDANCY
  DECLARATION row in the Phase 9 emit manifest check). C-42 requires only one locus; C-44
  requires both. A prompt with only the EMIT manifest row (passing C-42) satisfies one locus
  and fails C-44. A prompt with only the DUAL-PATH ENFORCEMENT DECLARATION section (no
  EMIT manifest row) also fails C-44. Both loci must be present. V-05 of R15 is the
  demonstration case: DUAL-PATH ENFORCEMENT DECLARATION section + EMIT manifest row.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|-------------------|----|
| Role sequence | C-43 | Per-quotation path attribution notes in Phase 8.5: Quotation A note names path 1 (construction-phase SCOPE GATE); Quotation B note names path 2 (emit-phase STOP CONDITION); C-44 ablated (NON-REDUNDANCY in EMIT manifest only -- one locus; no DUAL-PATH ENFORCEMENT DECLARATION section) |
| Output format | C-44 | DUAL-PATH ENFORCEMENT DECLARATION named section added before Phase 8.5; EMIT manifest retains NON-REDUNDANCY DECLARATION row; two structural loci achieved; C-43 ablated (no in-gate path attribution notes in Phase 8.5) |
| Inertia framing | C-43 partial / C-44 partial | STATUS QUO COMPETITOR extended with two foil items naming absent path attribution and single-locus non-redundancy; no structural implementation of either; both criteria addressed via contrast inference only |
| Role sequence + Output format | C-43 + C-44 | Per-quotation path attribution (axis 1) + DUAL-PATH ENFORCEMENT DECLARATION + EMIT manifest row (axis 2) simultaneously active |
| Role sequence + Output format + Phrasing register | C-43 + C-44 + structural-phase explicitness | V-04 mechanisms + each in-gate path attribution note names the structural phase and states what removing that path would cause; STATUS QUO COMPETITOR foil items from V-03 |

Single-axis: V-01 (role sequence), V-02 (output format), V-03 (inertia framing).
Combined: V-04 (role sequence + output format), V-05 (role sequence + output format +
phrasing register).

---

## Round 16 Variation Map

| Variation | Axis | C-43 probe | C-44 probe | C-41 | C-42 | Notes |
|-----------|------|-----------|-----------|------|------|-------|
| V-01 | Role sequence | Very strong -- in-gate notes naming enforcement path per quotation; Quotation A note names construction-phase SCOPE GATE; Quotation B note names emit-phase STOP CONDITION | Ablated -- NON-REDUNDANCY DECLARATION in EMIT manifest only (one locus); no DUAL-PATH ENFORCEMENT DECLARATION section | Stable from R15 | Stable from R15 | Single-axis; isolation control for C-43 |
| V-02 | Output format | Ablated -- Phase 8.5 blocking gate present (Quotation A + B required) with no in-gate path attribution notes | Very strong -- DUAL-PATH ENFORCEMENT DECLARATION section before Phase 8.5 + NON-REDUNDANCY DECLARATION in EMIT manifest; two structural loci | Stable from R15 | Stable from R15 | Single-axis; isolation control for C-44 |
| V-03 | Inertia framing | Partial (predicted) -- STATUS QUO foil item names absent path attribution; no structural in-gate notes | Partial (predicted) -- STATUS QUO foil item names single-locus non-redundancy; no DUAL-PATH section | Stable from R15 | Stable from R15 | Single-axis; ablation control for both |
| V-04 | Role sequence + Output format | Strong -- same as V-01 per-quotation path attribution | Strong -- same as V-02 DUAL-PATH section + EMIT manifest | Stable | Stable | Combined; first simultaneous probe |
| V-05 | Full stack | Strong (same as V-04) + each note names structural phase AND states failure mode if path were removed | Strong (same as V-04) + STATUS QUO foil items | Stable | Stable | Ceiling: all mechanisms; explicit structural-phase labeling per quotation |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- Phase 8.5 EVIDENCE QUOTATION GATE gains per-quotation path
attribution notes. Each quotation requirement header is followed by an in-gate note naming
which enforcement path that quotation confirms: Quotation A names the construction-phase
SCOPE GATE (path 1); Quotation B names the emit-phase STOP CONDITION (path 2). C-44 is
ablated: the NON-REDUNDANCY DECLARATION appears only in the EMIT manifest row (one
structural locus); no DUAL-PATH ENFORCEMENT DECLARATION section is present before Phase 8.5.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-01 will contain a Phase 8.5 gate with in-gate notes naming enforcement path 1 (construction-phase SCOPE GATE) after Quotation A and path 2 (emit-phase STOP CONDITION) after Quotation B; the primary falsification signal is a rubric where the in-gate notes are present but name the paths only generically ("confirms enforcement") rather than by structural-phase label, confirming C-43 requires path identification by name, not merely presence of a note. | The in-gate path attribution for Quotation B (naming the emit-phase STOP CONDITION) may cause a proximity effect on Phase 9: a builder who writes Quotation B's note explicitly may revise Phase 9's STOP CONDITION to be more specific, improving C-40 specificity as a side effect. | C-43 primary test: Phase 8.5 section with Quotation A header followed by a note naming "construction-phase SCOPE GATE" (or structural equivalent); Quotation B header followed by a note naming "emit-phase STOP CONDITION" (or structural equivalent). C-44 test: absent -- no DUAL-PATH ENFORCEMENT DECLARATION section; EMIT manifest NON-REDUNDANCY row present (C-42 satisfied) but second locus absent. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
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
>
> This quotation confirms enforcement path 1 (construction-phase SCOPE GATE): the quoted
> prohibition clause shows that the structural DFM label is required in criterion text at
> construction time, not merely described in prose. A reviewer reading only this quotation
> can confirm that path 1 enforcement names the structural label explicitly.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> This quotation confirms enforcement path 2 (emit-phase STOP CONDITION): the quoted
> instruction shows that label propagation to the emitted artifact is required by an
> explicit emit-phase constraint, independently verifiable from Phase 9 text alone. A
> reviewer reading only this quotation can confirm that path 2 enforcement exists as a
> blocking instruction, not merely a construction-phase assumption.

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
   CONSTRAINT declaration verbatim), self-application, >= 3 rejected generic criteria with
   reasons; must appear before the first criteria table. **STOP if Design Rationale omits
   the Dominant Failure Mode block or if the block does not carry the structural label from
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

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no other content) | |
| MECHANISM DEFINER GATE satisfied (Independence Map, all C-NN cited) | |
| SCOPE GATE exit condition satisfied (all criteria cite structural DFM label) | |
| Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A present and attributed | |
| Phase 8.5 EVIDENCE QUOTATION GATE: Quotation B present and attributed | |
| Design Rationale contains Dominant Failure Mode block with Phase 5 label | |
| COMPETITOR coverage: one competitor per aspirational criterion | |
| PHASE-LOCALITY RULE: no competitor in any prohibited zone | |
| Aspirational count: 1-2 criteria | |
| Three-state scoring table present (PASS / PARTIAL / FAIL with earn conditions) | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit the Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is missing.

---

## V-02 -- Output Format

**Axis:** Output format -- a DUAL-PATH ENFORCEMENT DECLARATION named section is added
between ROLE: BUILDER ASPIRATIONAL and Phase 8.5. This section declares the construction-
phase SCOPE GATE (path 1) and the pre-emit Phase 8.5 EVIDENCE QUOTATION GATE (path 2) as
non-redundant independently necessary mechanisms, with structural-phase distinction and
per-mechanism failure-mode arguments. The EMIT manifest retains its NON-REDUNDANCY
DECLARATION row. Two structural loci for the non-redundancy declaration are now present:
the DUAL-PATH ENFORCEMENT DECLARATION section (pre-gate) and the EMIT manifest row (emit).
C-43 is ablated: Phase 8.5 blocking gate is present with Quotation A and B required, but
no in-gate path attribution notes follow the quotation headers.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-02 will have the non-redundancy of the two enforcement paths declared in two structurally independent locations: the DUAL-PATH ENFORCEMENT DECLARATION section (positioned before Phase 8.5) and the NON-REDUNDANCY DECLARATION row in the EMIT manifest; the primary falsification signal is a rubric where only one locus is present -- confirming C-44 requires both loci, not merely two mentions of the property. | The DUAL-PATH ENFORCEMENT DECLARATION section's requirement to state per-mechanism failure-mode arguments may cause the builder to strengthen Phase 8.5's gate condition text, because the DECLARATION immediately precedes the gate and names its failure mode explicitly; outputs from V-02 may show a more specific Phase 8.5 gate condition than V-01 outputs (proximity-induced vocabulary refinement). | C-44 primary test: DUAL-PATH ENFORCEMENT DECLARATION section present before Phase 8.5 with structural-phase distinction and per-mechanism failure-mode arguments + NON-REDUNDANCY DECLARATION row in EMIT manifest; two distinct structural loci confirmed. C-43 test: Phase 8.5 present with two named quotation requirements and STOP condition -- but no in-gate notes following Quotation A or Quotation B headers; predicts FAIL C-43. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is the required form.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.

STOP CONDITION: Rewrite before proceeding if output contains anything beyond the two
required templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from blocking failure modes. Apply Text template and Pass template. Competitor blocks
immediately before the criterion they govern. Five fields: C-NN, Text, Weight: essential,
Category, Pass. No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Draft from suboptimal failure modes. Five fields. Annotation: **Dimension:** [degree |
precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

> **TIER-BLIND CATEGORIZER** -- does not separate assignments by tier, does not compute a
> majority category per tier. From the description above, derive what the category-
> distribution divergence check must verify before reading the check below.

Count category assignments per tier. Majority per tier. Flag if essential and recommended
share the same majority before proceeding to Phase 5.

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
  An aspirational criterion at a higher threshold of an already-covered property is not
  aspirational.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**SCOPE GATE:** Each criterion referencing a failure mode in its prohibition text must cite
the structural "Dominant Failure Mode" label declared above -- not merely describe the
failure mode in prose. Prose-only prohibition does NOT satisfy the gate. Label citation DOES.

**SCOPE GATE exit condition:** All criteria reviewed; any criterion using prose-only
prohibition revised before ROLE: MECHANISM DEFINER begins.

**Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.**

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

STOP CONDITION: Do not satisfy the gate until every row shows "Yes -- affects C-NN only."

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

**MECHANISM DEFINER GATE satisfied when:** Independence Map complete, all rows C-NN cited
and "Yes -- affects C-NN only," PHASE-LOCALITY RULE stated.

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

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's purpose statement or Design Rationale.

**Gate condition:** STOP if either quotation is absent. STOP if the quoted text does not
contain the structural "Dominant Failure Mode" label or its designated equivalent. Both
quotations must be present and attributed to their source section before Phase 9 begins.

This gate is independent of the Phase 5 SCOPE GATE. Passing the SCOPE GATE does not satisfy
this gate. Both gates operate at structurally distinct phases and must be satisfied
independently.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label (not prose
description).**

**PREREQUISITE: Phase 8.5 EVIDENCE QUOTATION GATE: Quotation A and Quotation B both present
and attributed.**

Output the complete rubric document in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- Dominant Failure Mode block (label from Phase 5 SCOPE CONSTRAINT
   verbatim), self-application, >= 3 rejected generic criteria with reasons. **STOP if DFM
   block absent or label differs from Phase 5 SCOPE CONSTRAINT declaration.**
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites all gate/rule
   identifiers
8. **Scoring** -- composite formula, denominator, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no other content) | |
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
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is missing.
STOP if DUAL-PATH ENFORCEMENT DECLARATION was not recorded before Phase 8.5.

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- STATUS QUO COMPETITOR extended with two new foil items naming
the C-43 and C-44 failure patterns: absent per-quotation path attribution (Phase 8.5 gate
has Quotation A and B but no in-gate notes naming which enforcement path each confirms) and
single-locus non-redundancy (NON-REDUNDANCY DECLARATION present in EMIT manifest only, no
DUAL-PATH ENFORCEMENT DECLARATION section). Both C-43 and C-44 are addressed via contrast
inference only; no structural Phase 8.5 path attribution notes, no DUAL-PATH section.
Predicts FAIL on C-43 (no in-gate notes) and FAIL on C-44 (no DUAL-PATH section).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| The STATUS QUO COMPETITOR foil items establish concept-awareness of absent path attribution and single-locus non-redundancy, but without positive structural enforcement, neither C-43 nor C-44 will fully pass; predicted: C-43 FAIL (no in-gate path attribution notes in Phase 8.5), C-44 FAIL (NON-REDUNDANCY in EMIT manifest only, no pre-gate section); this mirrors the inertia-framing ablation pattern from prior rounds where concept-awareness via foil items does not substitute for structural implementation. | A rubric builder who reads the foil items may spontaneously add an in-gate comment to Phase 8.5 or a non-redundancy note to the Design Rationale, partially satisfying C-43 or C-44 as proximity artifacts; if so, this would test whether foil-induced spontaneous addition qualifies as "partial" under the criteria's PARTIAL conditions. | C-43 test: Phase 8.5 section with two named quotation requirements and a STOP condition -- but no notes following each quotation header naming the enforcement path; FAIL predicted. C-44 test: NON-REDUNDANCY in EMIT manifest present (C-42 satisfied, one locus) but no DUAL-PATH ENFORCEMENT DECLARATION section before Phase 8.5; FAIL predicted. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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
- **Fails to add per-quotation path attribution in the pre-emit gate** -- when the pre-emit
  gate requires Quotation A and Quotation B, each quotation requirement names the artifact
  to quote but does not identify which enforcement path that quotation confirms; a reviewer
  seeing Quotation A and Quotation B in the gate cannot determine from the gate text alone
  which mechanism each confirms without reading the surrounding prompt structure.
- **Fails to declare non-redundancy at two structural loci** -- non-redundancy of the two
  enforcement paths is either absent or declared at only one structural location (typically
  the EMIT manifest row); a single-locus non-redundancy declaration can be removed or missed
  at exactly one location without creating a redundant safety signal at a second independent
  location.

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
their criterion. Five fields: C-NN, Text, Weight: essential, Category, Pass.

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

**SCOPE GATE:** Criteria referencing failure mode in prohibition text must cite the
structural "Dominant Failure Mode" label -- not prose description.

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

Three-state scoring table. Composite formula. Denominator. Golden threshold.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. All criteria drafted and sealed.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from Phase 5 SCOPE GATE that contains the structural "Dominant
> Failure Mode" label. The quoted text must include the structural label name as it appears
> in the SCOPE CONSTRAINT block.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's purpose statement or Design Rationale.

**Gate condition:** STOP if either quotation is absent. STOP if the quoted text does not
contain the structural "Dominant Failure Mode" label or its designated equivalent. Both
quotations must be present and attributed to their source section before Phase 9 begins.

This gate is independent of the Phase 5 SCOPE GATE. Passing the SCOPE GATE (construction
phase) does not satisfy this gate.

---

### PHASE 9 -- EMIT

**PREREQUISITE: SCOPE GATE exit condition: all criteria cite structural DFM label.**

Output the complete rubric document:
1. Failure Mode Log
2. Design Rationale -- Dominant Failure Mode block (label from Phase 5 verbatim),
   self-application, >= 3 rejected generic criteria. **STOP if DFM block absent or label
   differs from Phase 5 declaration.**
3. Essential Criteria
4. Recommended Criteria
5. Independence Map + PHASE-LOCALITY RULE
6. Aspirational Criteria (COMPETITOR blocks inline)
7. Scoring (formula, denominator, threshold, three-state table)
8. Notes + vN Candidates

Emit manifest check:

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

## V-04 -- Combined (Role Sequence + Output Format)

**Axis:** Role sequence + output format combined. V-01 per-quotation path attribution notes
in Phase 8.5 (role sequence axis, C-43 mechanism) are present and active. V-02 DUAL-PATH
ENFORCEMENT DECLARATION section is added before Phase 8.5 (output format axis, C-44 first
locus). EMIT manifest retains NON-REDUNDANCY DECLARATION row (C-44 second locus). Both
C-43 and C-44 are structurally enforced simultaneously. First combined probe: tests whether
C-43 and C-44 can both pass on top of the C-41/C-42 baseline without disrupting each other.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric from V-04 will contain Phase 8.5 with in-gate path attribution notes after each quotation header (C-43) AND a DUAL-PATH ENFORCEMENT DECLARATION section before Phase 8.5 plus a NON-REDUNDANCY DECLARATION in the EMIT manifest (C-44 two loci); primary falsification: Phase 8.5 per-quotation notes present but DUAL-PATH section absent (suggesting the per-quotation notes displace the need for a separate declaration section in the builder's attention). | The combination of DUAL-PATH ENFORCEMENT DECLARATION (which names the two paths before Phase 8.5) and per-quotation path attribution in Phase 8.5 (which identifies each path at the quotation site) may cause the per-quotation notes to reference the DUAL-PATH DECLARATION by name ("path 1 per DUAL-PATH ENFORCEMENT DECLARATION"), making the in-gate notes cross-reference the pre-gate declaration and improving C-43 expression density. | C-43 primary test: Phase 8.5 section with Quotation A note naming construction-phase SCOPE GATE (path 1) and Quotation B note naming emit-phase STOP CONDITION (path 2). C-44 primary test: DUAL-PATH ENFORCEMENT DECLARATION section present before Phase 8.5 (locus 1) + NON-REDUNDANCY DECLARATION row in EMIT manifest (locus 2). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### DUAL-PATH ENFORCEMENT DECLARATION

This section is a structural declaration and does not produce criteria. Placed after
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
> This quotation confirms enforcement path 1 (construction-phase SCOPE GATE, per DUAL-PATH
> ENFORCEMENT DECLARATION): the quoted clause shows that the structural DFM label is
> required in construction-phase criterion text, independently verifiable from the SCOPE
> GATE exit condition alone.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 EMIT that requires the Dominant Failure Mode label in
> the Design Rationale. The quoted text must include the STOP CONDITION referencing the
> label.
>
> This quotation confirms enforcement path 2 (emit-phase STOP CONDITION, per DUAL-PATH
> ENFORCEMENT DECLARATION): the quoted instruction shows that DFM label propagation to the
> emitted artifact is enforced by an explicit blocking constraint, independently verifiable
> from the Phase 9 EMIT instruction alone.

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
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged. Removing Phase 9 STOP CONDITION allows Design Rationale to omit Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is missing.
STOP if DUAL-PATH ENFORCEMENT DECLARATION was not recorded before Phase 8.5.

---

## V-05 -- Full Stack

**Axis:** Role sequence + output format + phrasing register. All V-04 mechanisms present:
per-quotation path attribution notes in Phase 8.5 (C-43) and DUAL-PATH ENFORCEMENT
DECLARATION section + EMIT manifest NON-REDUNDANCY row (C-44 two loci). Additionally:
(a) each in-gate path attribution note explicitly names the structural phase of the
enforcement path AND states what removing that path would cause (phrasing register upgrade
for C-43 expression density); (b) STATUS QUO COMPETITOR extended with the two foil items
from V-03. This is the ceiling variation: all mechanisms present with maximum explicit
structural-phase identification per quotation.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric from V-05 includes Phase 8.5 per-quotation path attribution notes (C-43), DUAL-PATH section (C-44 locus 1), and EMIT manifest NON-REDUNDANCY row (C-44 locus 2); primary comparison: V-04 passes C-43 and C-44 at the structural minimum, V-05 passes both with higher path attribution specificity (each note names structural phase + failure mode if path removed); if scoring is binary PASS/FAIL, V-04 and V-05 score identically; if criteria have PARTIAL for naming path without failure mode, V-05 scores higher. | The explicit "what removing this path would cause" language in V-05's in-gate notes may cause a proximity effect on Phase 8.5 gate condition: a builder who writes the failure-mode-if-removed language per quotation may revise the gate condition STOP text to be more specific, naming both path failures as the blocking reason rather than just "quotation absent." | C-43 test: Phase 8.5 with Quotation A note naming "construction-phase SCOPE GATE" AND stating the failure mode if removed ("without this path, prose-only prohibition text can pass construction unchallenged"); Quotation B note naming "emit-phase STOP CONDITION" AND stating the failure mode if removed ("without this path, DFM label propagation compliance is not independently verifiable from artifact text"). C-44 test: same as V-04 (DUAL-PATH section + EMIT manifest row). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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
- **Fails to add per-quotation path attribution in the pre-emit gate** -- when the pre-emit
  gate requires Quotation A and Quotation B, each quotation requirement names the artifact
  to quote but does not identify which enforcement path that quotation confirms; a reviewer
  seeing Quotation A and Quotation B in the gate cannot determine from the gate text alone
  which mechanism each confirms without reading the surrounding prompt structure.
- **Fails to declare non-redundancy at two structural loci** -- non-redundancy of the two
  enforcement paths is either absent or declared at only one structural location (typically
  the EMIT manifest row); a single-locus non-redundancy declaration can be removed or missed
  at exactly one location without creating a redundant safety signal at a second independent
  location.

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass
template), no additional content.**

**Text template (slot-fillable):**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```

**Pass template (slot-fillable):**
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

This section is a structural declaration and does not produce criteria. Placed after
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
> This quotation confirms enforcement path 1 (construction-phase SCOPE GATE, per DUAL-PATH
> ENFORCEMENT DECLARATION): the quoted prohibition clause shows that the structural DFM
> label is required in criterion text at construction time. Without this path, prose-only
> prohibition text would pass the construction phase unchallenged -- the prohibition clause
> would describe the failure mode without structurally citing the label. A reader examining
> this quotation alone can confirm that path 1 enforcement names the structural label in its
> exit condition.

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 EMIT that requires the Dominant Failure Mode label in
> the Design Rationale. The quoted text must include the STOP CONDITION referencing the
> label.
>
> This quotation confirms enforcement path 2 (emit-phase STOP CONDITION, per DUAL-PATH
> ENFORCEMENT DECLARATION): the quoted emit instruction shows that DFM label propagation to
> the artifact is enforced by an explicit blocking constraint at the emit phase. Without
> this path, a builder who satisfies the SCOPE GATE during construction but fails to carry
> the DFM label into the emitted Design Rationale would not be caught -- compliance would
> not be independently verifiable from artifact text. A reader examining this quotation
> alone can confirm that path 2 enforcement exists as a blocking instruction at the emit
> phase, not merely a construction-phase assumption.

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
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged. Removing Phase 9 STOP CONDITION allows Design Rationale to omit Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is missing.
STOP if DUAL-PATH ENFORCEMENT DECLARATION was not recorded before Phase 8.5.

---

## Predicted Scores (Rubric v16, denominator /36)

Assuming all essential and recommended criteria pass (E=1.0, R=1.0):

| Variation | C-43 prediction | C-44 prediction | Aspirational (/36) | Composite |
|-----------|----------------|----------------|-------------------|-----------|
| V-01 | PASS -- in-gate path attribution notes per quotation; Quotation A names path 1, Quotation B names path 2 | FAIL -- NON-REDUNDANCY in EMIT manifest only (one locus); no DUAL-PATH ENFORCEMENT DECLARATION section | 35/36 | 99.722 |
| V-02 | FAIL -- Phase 8.5 blocking gate present; no in-gate path attribution notes | PASS -- DUAL-PATH ENFORCEMENT DECLARATION section (locus 1) + EMIT manifest NON-REDUNDANCY row (locus 2) | 35/36 | 99.722 |
| V-03 | FAIL -- concept-awareness via foil items; no in-gate path attribution notes | FAIL -- no DUAL-PATH ENFORCEMENT DECLARATION section; EMIT manifest NON-REDUNDANCY present (C-42 satisfied, one locus only) | 34/36 | 99.444 |
| V-04 | PASS -- same as V-01 per-quotation path attribution | PASS -- same as V-02 DUAL-PATH section + EMIT manifest | 36/36 | 100.000 |
| V-05 | PASS (same as V-04) + explicit failure-mode-if-removed language per quotation note | PASS (same as V-04) | 36/36 | 100.000 |

**R16 spread hypothesis:** V-01 and V-02 score 99.722 (single criterion isolation each),
V-03 scores 99.444 (double ablation control), V-04 and V-05 score 100.000 (full
combination). V-04 vs V-05 discrimination requires graded C-43 scoring (PARTIAL for
path-name-present vs PASS for path-name-plus-failure-mode). If binary, V-04 = V-05.
R16 excellence signal target: V-05 explicit failure-mode-if-removed language per quotation
elevates C-43 expression to the pattern that may trigger C-45/C-46 candidate extraction
for v17.
