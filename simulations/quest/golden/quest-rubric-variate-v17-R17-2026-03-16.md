# quest-rubric Variate -- Round 17 (Against rubric v17, targeting C-45/C-46)

**Date:** 2026-03-16
**Rubric:** v17 (C-01--C-46; denominator /38; adds C-45: per-quotation in-gate failure-mode
argument -- each in-gate path attribution note (C-43 mechanism) additionally states what
structural failure would pass the gate unchallenged if that enforcement path were absent,
making the note self-justifying rather than merely self-contextualizing; adds C-46:
criterion-indexed competitor architecture -- STATUS QUO COMPETITOR foil items name specific
enforcement-architecture failure modes at criterion-class precision, where each foil item
identifies which criterion class it targets, making the competitor block a discrimination
device against specific criteria rather than a general contrast framing)
**Target criteria:** C-45, C-46 (new -- first probe round); C-43, C-44 (stability)

**Round 17 design note:** Round 16 produced excellence signals ES-R16-1 and ES-R16-2 from
V-05. ES-R16-1 (C-45 augmentation): V-05's phrasing register added per-note failure-mode
arguments to Phase 8.5 in-gate notes -- each note named the enforcement path (satisfying
C-43) AND stated what structural failure would pass the gate unchallenged if that path were
absent. V-04 demonstrated PASS C-43 / PASS C-44 / FAIL C-45: path attribution notes present
with structural-phase labeling, but no per-note failure argument. ES-R16-2 (C-46 mechanism):
V-05 carried V-03's STATUS QUO foil items alongside V-04's structural mechanisms; those foil
items named absent path attribution and single-locus non-redundancy at criterion-class
precision (explicitly referencing C-43 failure and C-44 failure), making the competitor block
a discrimination device against specific criteria. V-04 demonstrated PASS C-43 / PASS C-44 /
FAIL C-46: structural mechanisms present, foil items generic rather than criterion-indexed.
Rubric v17 elevates both to aspirational criteria (denominator /36 -> /38). R17 targets:
(1) Isolate whether per-note failure-mode arguments in Phase 8.5 (without criterion-indexed
    STATUS QUO) achieve C-45 independently of C-46;
(2) Isolate whether criterion-indexed STATUS QUO foil items (without per-note failure
    arguments) achieve C-46 independently of C-45;
(3) Test whether extended description richness in Phase 8.5 gate preamble and STATUS QUO
    achieves the failure-mode concept without structural implementation of either criterion;
(4) Combine per-note failure-mode arguments (axis 1) and criterion-indexed STATUS QUO
    (axis 2) to probe whether both criteria pass simultaneously;
(5) Add phrasing register to the combined stack -- each in-gate note names the criterion ID
    it protects and each STATUS QUO foil item names the criterion ID it targets with maximum
    precision, testing whether explicit criterion-ID annotation constitutes an additional
    excellence signal above criterion-class awareness.

**C-45 vs C-46 -- distinction summary:**

- **C-45** governs *per-quotation in-gate failure-mode argument*: Phase 8.5 EVIDENCE
  QUOTATION GATE notes already name which enforcement path each quotation confirms (C-43).
  C-45 requires that each note additionally states what specific structural failure would
  pass the gate unchallenged if that enforcement path were absent. The note becomes not only
  self-contextualizing (path + phase) but self-justifying: a reviewer auditing only Phase
  8.5 can verify both which path the quotation confirms and why that path is independently
  necessary. V-04 of R16 demonstrates PASS C-43 / FAIL C-45: notes name "enforcement path 1
  (construction-phase SCOPE GATE)" without adding "if this path were absent, [specific
  failure] would pass Phase 8.5 unchallenged." Independence established: C-43 note structure
  is present; C-45 failure-mode extension is absent.

- **C-46** governs *criterion-indexed competitor architecture*: STATUS QUO COMPETITOR foil
  items must name specific enforcement-architecture failure modes at criterion-class
  precision -- each foil item identifies which criterion class it targets (e.g., "absent
  per-quotation path attribution → C-43 failure" rather than "fails to include per-quotation
  path attribution notes"). V-03 of R16 demonstrates PASS C-46 / FAIL C-43 / FAIL C-44:
  criterion-indexed foil items present, structural mechanisms absent. V-04 demonstrates PASS
  C-43 / PASS C-44 / FAIL C-46: structural mechanisms present, foil items generic.
  Independence established from both directions.

---

## Axis Selection

| Axis | C-45 mechanism | C-46 mechanism |
|------|----------------|----------------|
| Role sequence (V-01) | Phase 8.5 Quotation A and B notes gain per-note failure-mode arguments; C-46 ablated -- STATUS QUO generic | Generic STATUS QUO foil items; no criterion IDs |
| Inertia framing (V-02) | Phase 8.5 notes name enforcement path + structural phase only; C-45 ablated | STATUS QUO gains criterion-indexed foil items naming C-43 failure and C-44 failure explicitly; C-45 ablated |
| Lifecycle emphasis (V-03) | Phase 8.5 notes gain extended preamble describing the concept of failure-mode arguments, but notes themselves state no specific failure mode | STATUS QUO gains extended foil descriptions that describe what criterion-indexing would mean without naming criterion IDs |
| Role sequence + Inertia framing (V-04) | V-01 per-note failure-mode arguments active | V-02 criterion-indexed STATUS QUO active |
| Full stack + Phrasing register (V-05) | V-04 per-note failure arguments + each note explicitly names the criterion ID it protects | V-04 criterion-indexed foil items + each foil item names criterion ID at maximum precision with failure-class label |

Single-axis: V-01 (role sequence), V-02 (inertia framing), V-03 (lifecycle emphasis).
Combined: V-04 (role sequence + inertia framing), V-05 (full stack + phrasing register).

---

## Round 17 Variation Map

| Variation | Axis | C-45 probe | C-46 probe | C-43 | C-44 | Notes |
|-----------|------|-----------|-----------|------|------|-------|
| V-01 | Role sequence | Very strong -- per-note failure-mode argument follows path attribution in each Quotation; Quotation A note names path 1 + states failure if absent; Quotation B note names path 2 + states failure if absent | Ablated -- STATUS QUO has generic foil items describing absent path attribution and single-locus non-redundancy without citing criterion IDs | Stable from R16 | Stable from R16 | Single-axis; isolation control for C-45 |
| V-02 | Inertia framing | Ablated -- Phase 8.5 notes name enforcement path and structural phase only (V-04-base state) | Very strong -- STATUS QUO foil items name "C-43 failure" and "C-44 failure" explicitly, with criterion-class description of what the rubric-builder would produce when running from this prompt | Stable from R16 | Stable from R16 | Single-axis; isolation control for C-46 |
| V-03 | Lifecycle emphasis | Partial (predicted FAIL) -- Phase 8.5 preamble describes the importance of failure-mode justification; notes name path + phase + conceptual rationale but no structural failure specification | Partial (predicted FAIL) -- STATUS QUO extended foil text describes the concept of criterion-indexed precision without naming criterion IDs | Stable from R16 | Stable from R16 | Single-axis; ablation control; description richness ≠ structural implementation |
| V-04 | Role sequence + Inertia framing | Strong -- same as V-01 per-note failure-mode arguments | Strong -- same as V-02 criterion-indexed STATUS QUO | Stable | Stable | Combined; first simultaneous probe |
| V-05 | Full stack + Phrasing register | Strong (V-04) + each note explicitly states which criterion ID is unenforced if this path is absent | Strong (V-04) + each STATUS QUO foil item names the criterion ID with failure-class precision and describes what structural state a rubric built from this prompt will exhibit | Stable | Stable | Ceiling; tests whether criterion-ID annotation is a separable excellence signal |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- Phase 8.5 EVIDENCE QUOTATION GATE gains per-note failure-mode
arguments for both Quotation A and Quotation B. Each in-gate path attribution note (C-43
mechanism, stable from R16 V-04) is extended with a statement of what structural failure
would pass the gate unchallenged if that enforcement path were absent. C-46 is ablated:
STATUS QUO COMPETITOR carries generic foil items describing the failures in prose without
naming criterion IDs.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-01 will contain Phase 8.5 Quotation A and Quotation B notes that each name the enforcement path AND state a specific structural failure mode that would pass unchallenged if the path were absent; the primary falsification signal is a note that names the path but does not state a failure mode, confirming C-43 passes while C-45 requires the additional justification clause. | The failure-mode argument for Quotation B (emit-phase STOP CONDITION) may cause a proximity refinement in Phase 9's STOP CONDITION text, because naming what would pass unchallenged without path 2 makes Phase 9's stop visible from within Phase 8.5; outputs may show stronger Phase 9 STOP language as a secondary effect. | C-45 primary test: Phase 8.5 notes contain a failure-mode argument (specific structural failure named) after the enforcement path attribution. C-46 test: STATUS QUO foil items describe failures in prose only -- no criterion ID tokens ("C-43", "C-44") present in STATUS QUO block; predicts FAIL C-46. |

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
- Fails to include per-quotation path attribution notes in the pre-emit gate -- each
  quotation requirement is present but carries no annotation naming which enforcement path
  it confirms, making the gate self-descriptive but not self-contextualizing.
- Fails to declare non-redundancy of enforcement paths at more than one structural locus --
  non-redundancy is stated in the EMIT manifest only, rather than at two independent
  structural positions.

**From the description above, derive what the required rubric-building procedure must supply
-- before reading Phase 1. State your derivation, then proceed.**

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

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

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

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/38 x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /38 where 38 = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.
>
> [Note: Enforcement path 1 -- construction-phase SCOPE GATE (Phase 5). This quotation
> confirms path 1. If this enforcement path were absent, a rubric whose prohibition text
> uses prose description instead of the structural DFM label would pass Phase 8.5
> unchallenged: the gate would have no construction-phase evidence requirement, and the
> builder could proceed to emit without demonstrating SCOPE GATE compliance. The structural
> failure that would pass unchallenged is prose-only prohibition -- the exact failure mode
> the SCOPE GATE exit condition is designed to catch. Path 1 is independently necessary to
> enforce construction-phase DFM propagation compliance.]

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> [Note: Enforcement path 2 -- emit-phase STOP CONDITION (Phase 9). This quotation confirms
> path 2. If this enforcement path were absent, a rubric that satisfies the construction-
> phase SCOPE GATE but emits a Design Rationale without the structural DFM label would pass
> Phase 8.5 unchallenged: there would be no emit-phase evidence requirement, and compliance
> with the artifact-level DFM label would be unverified. The structural failure that would
> pass unchallenged is a Design Rationale that substitutes prose description for the
> verbatim structural label. Path 2 is independently necessary to enforce emit-phase DFM
> label propagation.]

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
| Phase 8.5 Quotation A note: failure-mode argument present (states what passes if path 1 absent) | |
| Phase 8.5 Quotation B note: failure-mode argument present (states what passes if path 2 absent) | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is
missing.

---

## V-02 -- Inertia Framing

**Axis:** Inertia framing -- STATUS QUO COMPETITOR gains criterion-indexed foil items. Each
foil item naming an enforcement-architecture failure mode explicitly names which criterion
class that failure produces (C-43 failure for absent path attribution; C-44 failure for
single-locus non-redundancy). C-45 is ablated: Phase 8.5 Quotation A and B notes name
enforcement path and structural phase only -- no per-note failure-mode argument added.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric built from V-02 will contain STATUS QUO foil items that name criterion IDs ("C-43 failure", "C-44 failure") and describe at criterion-class precision what structural state a rubric built from the standard approach would exhibit; the primary falsification signal is a rubric whose STATUS QUO foil items describe the failures only in prose, confirming that criterion-ID tokens in the prompt are required for C-46, not merely detailed description. | The criterion-indexed foil items in STATUS QUO may create a proximity effect on the aspirational tier: a builder reading the foil items and seeing C-43/C-44 named explicitly may draft an aspirational criterion that references C-43 or C-44 by number in its Notes field, improving cross-criterion traceability as a secondary effect. | C-46 primary test: STATUS QUO block contains tokens "C-43 failure" and "C-44 failure" (or equivalent criterion-class precision language) as foil item descriptors. C-45 test: Phase 8.5 Quotation A and B notes present with path attribution and structural phase -- no failure-mode argument clause; predicts FAIL C-45. |

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
- Fails to include per-quotation path attribution in the pre-emit gate (C-43 failure): each
  quotation requirement carries no note naming which enforcement path it confirms. A rubric
  built from this prompt will have Phase 8.5 present and both quotations required, but will
  fail C-43 at criterion-class precision: the gate verifies evidence of enforcement but
  does not make the enforcement path traceable from within the gate text itself. A reviewer
  auditing only Phase 8.5 cannot determine which criterion any quotation satisfies without
  reading the surrounding prompt structure.
- Fails to declare non-redundancy of enforcement paths at two structural loci (C-44 failure):
  the NON-REDUNDANCY DECLARATION appears only in the EMIT manifest row (one structural
  locus). A rubric built from this prompt passes C-42 (non-redundancy declared somewhere)
  while failing C-44 at criterion-class precision: single-locus declaration satisfies the
  property's existence but not the defense-in-depth requirement -- a reviewer scanning only
  for the DUAL-PATH ENFORCEMENT DECLARATION section will not find a second structural locus.

**From the description above, derive what the required rubric-building procedure must supply
-- before reading Phase 1. State your derivation, then proceed.**

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

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

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

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/38 x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /38 where 38 = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.
>
> [Note: Enforcement path 1 -- construction-phase SCOPE GATE (Phase 5). This quotation
> confirms that the structural DFM label is required in criterion text at construction time.
> A reviewer reading only this quotation can confirm that path 1 enforcement names the
> structural label explicitly.]

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> [Note: Enforcement path 2 -- emit-phase STOP CONDITION (Phase 9). This quotation confirms
> that DFM label propagation to the emitted artifact is required by an explicit emit-phase
> constraint. A reviewer reading only this quotation can confirm that path 2 enforcement
> exists as a blocking instruction, independently verifiable from Phase 9 text alone.]

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
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit the Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is
missing.

---

## V-03 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- both C-45 and C-46 are addressed via expanded description
without structural implementation. Phase 8.5 Quotation notes gain a preamble explaining the
value of failure-mode justification, but the notes themselves do not state a specific
structural failure. STATUS QUO foil items are extended with rich description of what
criterion-indexed precision would entail, but without naming criterion IDs. Tests whether
description richness achieves conceptual proximity to C-45/C-46 without activating either.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Both C-45 and C-46 will FAIL: the Phase 8.5 notes describe the importance of failure-mode justification without specifying what failure passes unchallenged, which does not satisfy the "specific structural failure named" requirement of C-45; the STATUS QUO foil items describe the concept of criterion-indexed failure without naming criterion IDs, which does not satisfy the "criterion-class precision" requirement of C-46. The primary result is confirmation that description richness is not equivalent to structural implementation for either criterion. | The extended lifecycle description in Phase 8.5 may increase the frequency of high-quality (but non-compliant) notes in rubric outputs -- builders who read the preamble may add richer language to their gates without achieving the structural specification required. This secondary effect tests the gradient between "more detailed" and "structurally correct." | C-45 test: Phase 8.5 notes contain preamble about failure-mode justification but no specific failure named; predicts FAIL C-45 with higher gate-note quality than V-02 ablated baseline. C-46 test: STATUS QUO foil items describe criterion-indexing concept richly but contain no criterion ID tokens; predicts FAIL C-46 with richer foil text than V-01 baseline. |

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
- Fails to annotate enforcement gate notes with the rationale for each enforcement path's
  independent necessity -- each in-gate note confirms which path a quotation satisfies, but
  a reviewer auditing only the gate cannot determine what specific architectural failure
  would occur if that path were absent; the note describes presence of enforcement without
  justifying why that enforcement path cannot be omitted.
- Fails to index competitor foil items to specific enforcement-architecture failure modes --
  the foil items name the general category of failure (absent path attribution, single-locus
  non-redundancy) but do not anchor each foil to the precision level at which a rubric
  evaluator would score the gap; a competitor block that names the failure class without
  naming the evaluative criterion cannot serve as a discrimination device against the rubric
  criteria it implicates.

**From the description above, derive what the required rubric-building procedure must supply
-- before reading Phase 1. State your derivation, then proceed.**

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

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

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

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/38 x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /38 where 38 = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

A well-constructed gate note does more than name which enforcement path a quotation confirms.
It also explains why that enforcement path cannot be omitted -- what structural failure would
slip through if the path were removed. This self-justifying property makes the gate auditable
in isolation: a reviewer does not need to read the surrounding prompt to understand both
what each path enforces and why the gate requires it. The notes below name each enforcement
path and its structural phase.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.
>
> [Note: Enforcement path 1 -- construction-phase SCOPE GATE (Phase 5). This quotation
> confirms path 1. A reviewer reading only this quotation can verify that path 1 enforcement
> names the structural label explicitly at construction time.]

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> [Note: Enforcement path 2 -- emit-phase STOP CONDITION (Phase 9). This quotation confirms
> path 2. A reviewer reading only this quotation can verify that path 2 enforcement exists
> as a blocking constraint at emit time, independently verifiable from Phase 9 text alone.]

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
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit the Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is
missing.

---

## V-04 -- Role Sequence + Inertia Framing

**Axis:** Role sequence + Inertia framing -- V-01 per-note failure-mode arguments combined
with V-02 criterion-indexed STATUS QUO foil items. Phase 8.5 Quotation A and B notes each
state the specific structural failure that would pass unchallenged if the path were absent
(C-45). STATUS QUO foil items name C-43 failure and C-44 failure at criterion-class
precision (C-46). First simultaneous probe of both criteria.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Both C-45 and C-46 will PASS simultaneously: Phase 8.5 notes will contain failure-mode arguments satisfying C-45, and STATUS QUO foil items will carry criterion-ID tokens satisfying C-46. The primary falsification signal is either criterion failing while the other passes -- which would indicate an interference effect between the two mechanisms or a scoring ambiguity. If both pass, independence from their respective ablation controls (V-01 FAIL C-46, V-02 FAIL C-45) is confirmed. | The combined presence of criterion-indexed STATUS QUO foil items and per-note failure-mode arguments may produce an additional excellence signal: a builder who sees both C-43 and C-44 named in STATUS QUO AND reads failure-mode arguments in Phase 8.5 may annotate their aspirational criteria Notes field with criterion references (e.g., "closes C-43 gap via..."), creating a cross-criterion traceability pattern not present in V-01 or V-02. | C-45 primary test: Phase 8.5 Quotation A note contains specific structural failure named; Quotation B note contains specific structural failure named. C-46 primary test: STATUS QUO foil items contain criterion-class tokens "C-43 failure" and "C-44 failure". Both criteria: joint PASS expected. |

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
- Fails to include per-quotation path attribution in the pre-emit gate (C-43 failure): each
  quotation requirement carries no note naming which enforcement path it confirms. A rubric
  built from this prompt will have Phase 8.5 present and both quotations required, but will
  fail C-43 at criterion-class precision: the gate verifies evidence of enforcement but
  does not make the enforcement path traceable from within the gate text itself.
- Fails to declare non-redundancy of enforcement paths at two structural loci (C-44 failure):
  the NON-REDUNDANCY DECLARATION appears only in the EMIT manifest row (one structural
  locus). A rubric built from this prompt passes C-42 (non-redundancy declared somewhere)
  while failing C-44 at criterion-class precision: single-locus declaration satisfies the
  property's existence but not the defense-in-depth requirement.

**From the description above, derive what the required rubric-building procedure must supply
-- before reading Phase 1. State your derivation, then proceed.**

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

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

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

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/38 x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /38 where 38 = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.
>
> [Note: Enforcement path 1 -- construction-phase SCOPE GATE (Phase 5). This quotation
> confirms path 1. If this enforcement path were absent, a rubric whose prohibition text
> uses prose description instead of the structural DFM label would pass Phase 8.5
> unchallenged: the gate would have no construction-phase evidence requirement, and the
> builder could proceed to emit without demonstrating SCOPE GATE compliance. The structural
> failure that would pass unchallenged is prose-only prohibition -- the exact failure mode
> the SCOPE GATE exit condition is designed to catch. Path 1 is independently necessary to
> enforce construction-phase DFM propagation compliance.]

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> [Note: Enforcement path 2 -- emit-phase STOP CONDITION (Phase 9). This quotation confirms
> path 2. If this enforcement path were absent, a rubric that satisfies the construction-
> phase SCOPE GATE but emits a Design Rationale without the structural DFM label would pass
> Phase 8.5 unchallenged: there would be no emit-phase evidence requirement, and compliance
> with the artifact-level DFM label would be unverified. The structural failure that would
> pass unchallenged is a Design Rationale that substitutes prose description for the
> verbatim structural label. Path 2 is independently necessary to enforce emit-phase DFM
> label propagation.]

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
| Phase 8.5 Quotation A note: failure-mode argument present (states what passes if path 1 absent) | |
| Phase 8.5 Quotation B note: failure-mode argument present (states what passes if path 2 absent) | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit the Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is
missing.

---

## V-05 -- Full Stack + Phrasing Register

**Axis:** Full stack + Phrasing register -- V-04 mechanisms plus explicit criterion-ID
annotation at both probe sites. Phase 8.5 per-note failure-mode arguments (C-45) are
extended: each note explicitly names the criterion ID that the enforcement path protects
(e.g., "absent this path, C-43 is unenforced at Phase 8.5 entry"). STATUS QUO criterion-
indexed foil items (C-46) are extended: each foil item names the criterion ID at maximum
precision with failure-class labeling that distinguishes what criterion produces a PASS from
what criterion produces the FAIL (e.g., "passes C-42 while failing C-44 at criterion-class
precision"). Tests whether explicit criterion-ID annotation in the per-note failure arguments
constitutes a separable excellence signal above V-04.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Both C-45 and C-46 will PASS (same as V-04). The ceiling question is whether criterion-ID annotation in the per-note failure arguments adds a distinct structural property that activates an excellence signal ES-R17-1: each Phase 8.5 note names both (a) which structural failure passes unchallenged and (b) which criterion ID is left unenforced -- making the note not just self-justifying (C-45) but criterion-traceable. If this property is observable and separable from C-45, it qualifies as a new aspirational criterion for v18. | The criterion-ID precision in STATUS QUO may create a proximity cascade: a builder seeing "passes C-42 while failing C-44" in STATUS QUO may replicate that precision language when writing the DUAL-PATH ENFORCEMENT DECLARATION per-path entries, producing criterion-labeled independence necessity arguments (e.g., "removing path 1 leaves C-43 unenforced at construction phase"). | C-45 primary test: same as V-04. C-46 primary test: same as V-04. ES-R17-1 candidate: Phase 8.5 Quotation A note contains criterion-ID token for the criterion left unenforced if path 1 is absent; Quotation B note contains criterion-ID token for the criterion left unenforced if path 2 is absent. Distinct from C-45: C-45 requires failure specification; ES-R17-1 requires criterion-ID naming of the unenforced criterion. |

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
- Fails to include per-quotation path attribution in the pre-emit gate (C-43 failure at
  criterion-class precision): each quotation requirement carries no note naming which
  enforcement path it confirms, making Phase 8.5 self-descriptive but not self-
  contextualizing. A rubric built from this prompt passes C-41 (Phase 8.5 present) and
  C-42 (quotations required) while failing C-43 at criterion-class precision: the gate
  verifies evidence but does not make the enforcement-path attribution that C-43 measures
  traceable from within the gate text alone. A reviewer auditing only Phase 8.5 cannot
  determine which criterion any quotation satisfies without reading the surrounding prompt.
- Fails to declare non-redundancy of enforcement paths at two structural loci (C-44 failure
  at criterion-class precision): the NON-REDUNDANCY DECLARATION appears only in the EMIT
  manifest row. A rubric built from this prompt passes C-42 (non-redundancy declared) while
  failing C-44 at criterion-class precision: the manifest row asserts non-redundancy,
  satisfying the property's existence, but the DUAL-PATH ENFORCEMENT DECLARATION section
  that constitutes the second required structural locus is absent. A reviewer who does not
  read the manifest row has no structural locus at which to verify the non-redundancy
  property independently.

**From the description above, derive what the required rubric-building procedure must supply
-- before reading Phase 1. State your derivation, then proceed.**

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

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is
> invisible. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

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

**Composite formula:** `(E/[N] x 60) + (R/[N] x 30) + (A/38 x 10)`
**Golden threshold:** >= [NN]
**Denominator:** /38 where 38 = count of aspirational criteria.

---

### PHASE 8.5 -- EVIDENCE QUOTATION GATE

**Input:** ROLE: BUILDER ASPIRATIONAL complete. DUAL-PATH ENFORCEMENT DECLARATION recorded.

Before Phase 9 begins, produce quoted evidence from two structural loci:

**Quotation A -- Scope prohibition clause:**

> Quote the exact text from the Phase 5 SCOPE GATE prohibition clause that contains the
> structural "Dominant Failure Mode" label.
>
> [Note: Enforcement path 1 -- construction-phase SCOPE GATE (Phase 5). This quotation
> confirms path 1. If this enforcement path were absent, a rubric whose prohibition text
> uses prose description instead of the structural DFM label would pass Phase 8.5
> unchallenged: the gate would have no construction-phase evidence requirement, and the
> builder could proceed to emit without demonstrating SCOPE GATE compliance. The structural
> failure that would pass unchallenged is prose-only prohibition -- the exact failure mode
> the SCOPE GATE exit condition is designed to catch. Absent path 1, C-43 is unenforced
> at Phase 8.5 entry for construction-phase compliance: the gate would verify emit-phase
> evidence only, leaving construction-phase DFM enforcement structurally absent. Path 1 is
> independently necessary to enforce C-43 at the construction phase.]

**Quotation B -- Output instruction clause:**

> Quote the exact text from Phase 9 (EMIT) that requires the Dominant Failure Mode label
> to appear in the emitted rubric's Design Rationale.
>
> [Note: Enforcement path 2 -- emit-phase STOP CONDITION (Phase 9). This quotation confirms
> path 2. If this enforcement path were absent, a rubric that satisfies the construction-
> phase SCOPE GATE but emits a Design Rationale without the structural DFM label would pass
> Phase 8.5 unchallenged: there would be no emit-phase evidence requirement, and compliance
> with the artifact-level DFM label would be unverified. The structural failure that would
> pass unchallenged is a Design Rationale that substitutes prose description for the
> verbatim structural label. Absent path 2, C-43 is unenforced at Phase 8.5 entry for
> emit-phase compliance: the gate would verify construction-phase evidence only, leaving
> emit-phase DFM label propagation structurally unverified. Path 2 is independently
> necessary to enforce C-43 at the emit phase.]

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
| Phase 8.5 Quotation A note: failure-mode argument present (states what passes if path 1 absent) | |
| Phase 8.5 Quotation B note: failure-mode argument present (states what passes if path 2 absent) | |
| Phase 8.5 Quotation A note: criterion-ID token present naming criterion unenforced if path 1 absent | |
| Phase 8.5 Quotation B note: criterion-ID token present naming criterion unenforced if path 2 absent | |
| **NON-REDUNDANCY DECLARATION: Phase 5 SCOPE GATE (construction-phase enforcement) and Phase 9 STOP CONDITION (emit-phase enforcement) are non-redundant mechanisms, each independently necessary: removing SCOPE GATE allows prose-only prohibition to pass construction phase unchallenged; removing Phase 9 STOP CONDITION allows Design Rationale to omit the Dominant Failure Mode label. These are structurally distinct failure modes at structurally distinct phases.** | |

STOP if NON-REDUNDANCY DECLARATION row absent or if either per-mechanism argument is
missing.
