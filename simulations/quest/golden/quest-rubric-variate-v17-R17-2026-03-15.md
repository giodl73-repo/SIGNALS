# quest-rubric Variate -- Round 17 (Against rubric v17, targeting C-49/C-50)

**Date:** 2026-03-15
**Rubric:** v17 (C-01--C-50; denominator /42; adds C-49: Phase 9 PREREQUISITE independence
boundary declaration includes a co-located positive audit-sufficiency claim explicitly stating
that reading the PREREQUISITE line alone is sufficient to confirm gate completion, converting
the independence boundary from a negative-exclusion claim to a combined exclusion-plus-sufficiency
declaration, extending C-48 by the same pattern C-43 is extended by C-44; C-50: each
Architecture-labeled STOP in the NON-REDUNDANCY DECLARATION explicitly names the target
resolution section in the STOP predicate, making the STOP condition independently checkable
from its text alone without reading declaration context)
**Target criteria:** C-49, C-50

**Round 17 design note:** Round 16 produced excellence signals ES-R16-1 (V-01) and ES-R16-2
(V-02). V-01 passed C-48 AND additionally produced a Phase 9 PREREQUISITE containing a
positive sufficiency claim ("a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR"). V-02
passed C-47 AND additionally produced Architecture-labeled STOP predicates that explicitly
named "the EVALUABILITY ARCHITECTURE COMPETITOR section" as the resolution target. Rubric v17
elevates both excellence signals as aspirational criteria C-49 and C-50, extending the
denominator from /40 to /42. R17 targets: (1) isolate whether Phase 9 PREREQUISITE with
positive sufficiency claim co-located alongside the independence boundary declaration (all
three: verbatim gate-ID, exclusion boundary, positive sufficiency) achieves C-49 without
Architecture-labeled STOP predicates naming the resolution section; (2) isolate whether
Architecture-labeled STOP predicates naming the EVALUABILITY ARCHITECTURE COMPETITOR section
explicitly achieve C-50 without the positive sufficiency claim in Phase 9; (3) test whether
Architecture labels in the NON-REDUNDANCY DECLARATION without STOP enforcement at all approach
C-47/C-50 (negative control); (4) combine both single-axis mechanisms for simultaneous C-49
and C-50; (5) add phrasing register to the combined stack with explicit auditability-purpose
clauses at both the Phase 9 PREREQUISITE and the NON-REDUNDANCY DECLARATION.

**C-49 vs C-50 -- distinction summary for variation design:**

- C-49 governs the *Phase 9 PREREQUISITE's bidirectionality*: the PREREQUISITE must not only
  include the verbatim gate-ID quote (C-45) and the independence boundary declaration naming
  the excluded role body (C-48) but must also include a positive audit-sufficiency claim
  explicitly stating that reading the PREREQUISITE line alone is sufficient to confirm gate
  completion -- e.g., "a reader can confirm that Phase 9 was properly gated by reading this
  PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR." A
  PREREQUISITE satisfying C-48 (verbatim gate-ID + independence boundary) without the
  positive sufficiency counterpart satisfies C-48 but fails C-49 -- the exclusion claim is
  necessary but not sufficient. V-02 (C-48 pass, no positive sufficiency) is the primary
  C-49 ablation control.

- C-50 governs the *STOP predicate's self-sufficiency at the NON-REDUNDANCY DECLARATION*:
  each Architecture-labeled STOP must not only enforce the label-structure requirement
  (C-47) but must additionally name the resolution target section explicitly in the STOP
  predicate text -- e.g., "STOP: if the Architecture A label above does not resolve to a
  named entry in the EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY
  DECLARATION is incomplete." A STOP predicate that enforces label presence without naming
  the resolution target section satisfies C-47 but fails C-50 -- the enforcement is present
  but the predicate is not self-contained. V-01 (C-47 ablated via prose-only NON-REDUNDANCY)
  cannot produce C-50 passes; a new C-50-ablation variant uses Architecture labels + STOP
  enforcement but STOP predicates that omit the section name.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|--------------------|-----------|
| Role sequence | C-49 | Phase 9 PREREQUISITE: verbatim gate-ID (C-45) + independence boundary naming ROLE: EVALUABILITY AUDITOR (C-48) + **positive audit-sufficiency claim** co-located at section-header level (C-49); C-50 ablated: Phase 8.5 NON-REDUNDANCY uses prose-only arguments without Architecture labels (C-47 ablated, C-50 naturally absent) |
| Lifecycle emphasis | C-50 | EVALUABILITY ARCHITECTURE COMPETITOR section before Phase 8.5; Phase 8.5 NON-REDUNDANCY uses Architecture A/B labels with co-located STOP predicates **naming "the EVALUABILITY ARCHITECTURE COMPETITOR section" explicitly** in each predicate (C-47 pass, C-50 pass); C-49 ablated: Phase 9 PREREQUISITE has verbatim gate-ID + independence boundary (C-45 + C-48) but NO positive sufficiency claim |
| Inertia framing | ablation | EVALUABILITY ARCHITECTURE COMPETITOR section uses Architecture A/B labels; Phase 8.5 NON-REDUNDANCY references Architecture A/B labels WITHOUT STOP enforcement; Phase 9 PREREQUISITE: verbatim gate-ID only (C-45 satisfied, C-48 ablated, C-49 ablated); tests whether labels without STOP conditions approach C-47 |
| (combined) | C-49 + C-50 | Role sequence (C-49) + Lifecycle emphasis (C-50): Phase 9 PREREQUISITE has verbatim gate-ID + independence boundary + positive sufficiency; Phase 8.5 STOP predicates name "the EVALUABILITY ARCHITECTURE COMPETITOR section" |
| Role sequence + Phrasing register | C-49 + C-50 + explicit auditability purpose | V-04 mechanisms + Phase 9 PREREQUISITE adds explicit bidirectionality purpose clause + NON-REDUNDANCY STOP predicates add explicit self-sufficiency purpose clause ("making the STOP condition independently verifiable from its text alone without reading adjacent declaration prose") |

Single-axis: V-01 (role sequence), V-02 (lifecycle emphasis), V-03 (inertia framing).
Combined: V-04 (three single axes), V-05 (three single axes + phrasing register).

---

## Round 17 Variation Map

| Variation | Axis | C-49 probe | C-50 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence | Very strong -- Phase 9 PREREQUISITE: verbatim gate-ID (C-45) + independence boundary naming ROLE: EVALUABILITY AUDITOR (C-48) + **positive sufficiency claim co-located at section-header level** (C-49 mechanism) | Absent -- Phase 8.5 NON-REDUNDANCY uses prose-only arguments; no Architecture labels; no STOP enforcement; C-47 ablated, C-50 naturally absent | Single-axis; isolates whether positive sufficiency claim co-located in Phase 9 PREREQUISITE achieves C-49 without Architecture-labeled STOP predicates naming resolution section; prediction: V-01 passes C-49, fails C-50 |
| V-02 | Lifecycle emphasis | Ablated -- Phase 9 PREREQUISITE has verbatim gate-ID + independence boundary (C-45 + C-48) but no positive sufficiency claim | Very strong -- Architecture A/B labels in EVALUABILITY ARCHITECTURE COMPETITOR section; Phase 8.5 STOP predicates **explicitly name "the EVALUABILITY ARCHITECTURE COMPETITOR section"** in each predicate (C-47 pass, C-50 mechanism) | Single-axis; isolates whether Architecture-labeled STOP predicates naming the resolution section achieve C-50 without positive sufficiency claim in Phase 9; prediction: V-02 passes C-50, fails C-49 |
| V-03 | Inertia framing | Ablated -- Phase 9 PREREQUISITE: verbatim gate-ID only (C-45 satisfied, C-48 absent, C-49 absent) | Ablated (partial) -- EVALUABILITY ARCHITECTURE COMPETITOR section uses Architecture A/B labels; Phase 8.5 references labels but NO STOP enforcement; hypothesis: labels without STOP do not satisfy C-47, and the STOP-predicate naming question (C-50) cannot be evaluated | Ablation control; tests whether Architecture labels without STOP enforcement approach C-47; C-47 and C-50 expected to fail; C-49 expected to fail |
| V-04 | Role sequence + Lifecycle emphasis + Inertia framing | Very strong -- same as V-01: verbatim gate-ID + independence boundary + positive sufficiency claim co-located in Phase 9 PREREQUISITE | Very strong -- same as V-02: Architecture A/B EVALUABILITY ARCHITECTURE COMPETITOR section + Phase 8.5 STOP predicates naming "the EVALUABILITY ARCHITECTURE COMPETITOR section" | Combined; tests whether C-49 and C-50 simultaneously pass on top of C-45/C-46/C-47/C-48 baseline; prediction: V-04 passes both |
| V-05 | Role sequence + Lifecycle emphasis + Inertia framing + Phrasing register | Very strong (same as V-04) + Phase 9 PREREQUISITE adds explicit bidirectionality purpose clause: "making this PREREQUISITE a bidirectional independence declaration -- a reader can confirm both what is excluded and what can be confirmed from this line alone" | Very strong (same as V-04) + each STOP predicate adds explicit self-sufficiency purpose clause: "making this STOP condition independently verifiable from its text alone without reading adjacent NON-REDUNDANCY DECLARATION prose" | V-04 mechanisms + phrasing register; tests whether explicit purpose declarations add measurable C-49/C-50 scoring value vs V-04's implicit mechanisms; prediction: V-05 passes C-49 and C-50 with higher criterion expression density than V-04 |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- Phase 9 opens with a PREREQUISITE that (1) quotes the EVALUABILITY
GATE identifier verbatim (satisfying C-45), (2) includes a co-located independence boundary
declaration naming ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification (satisfying C-48), AND (3) adds a co-located positive audit-sufficiency
claim explicitly stating that reading the PREREQUISITE line alone is sufficient to confirm gate
completion (C-49 mechanism). C-50 is naturally absent because Phase 8.5 is ablated: the
NON-REDUNDANCY DECLARATION uses prose-only arguments without Architecture labels and without
STOP-condition enforcement.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain a Phase 9 that opens with a three-part PREREQUISITE: (a) verbatim gate-ID quote, (b) independence boundary sentence naming ROLE: EVALUABILITY AUDITOR as the excluded role body, and (c) a positive sufficiency sentence explicitly stating that reading the PREREQUISITE line alone is sufficient to confirm gate completion -- any output where part (c) is absent, or where the positive sufficiency claim is buried in the Phase 9 body rather than co-located in the PREREQUISITE header, falsifies the C-49 hypothesis. | The positive sufficiency claim converts the PREREQUISITE from a negative-exclusion declaration ("you do not need to read ROLE: EVALUABILITY AUDITOR") to a bidirectional independence declaration ("you do not need to read ROLE: EVALUABILITY AUDITOR AND reading this line alone is sufficient") -- outputs from V-01 will show a three-sentence PREREQUISITE structure vs V-02 outputs which show a two-sentence PREREQUISITE (verbatim gate-ID + independence boundary, no positive sufficiency). | V-02 is the primary C-49 ablation control: V-02 has a two-sentence Phase 9 PREREQUISITE satisfying C-48 (verbatim gate-ID + independence boundary) but no positive sufficiency claim (C-49 fails); comparing PREREQUISITE structure across V-01 (three-part: gate-ID + boundary + sufficiency) and V-02 (two-part: gate-ID + boundary only) isolates whether the positive sufficiency claim -- not just the independence boundary -- is load-bearing for C-49; prediction: V-01 passes C-49, V-02 fails C-49. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

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

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

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

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

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

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Removing the EVALUABILITY GATE causes the Independence column to be unverified before
  emit: the Phase 9 terminal table may have generic or absent Independence fields, failing
  C-44.
- Removing the Phase 9 terminal Criterion Evaluability Map causes the verified map to remain
  in the construction record only: the emitted artifact has no terminal evaluability section,
  failing C-43.

NON-REDUNDANCY DECLARATION: Each enforcement point governs a distinct failure mode. Neither
can substitute for the other. Both are required.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- the EVALUABILITY ARCHITECTURE COMPETITOR section appears
before Phase 8.5 and names Architecture A and Architecture B as distinct labeled entries.
Phase 8.5 NON-REDUNDANCY DECLARATION uses Architecture A/B labels as experiment anchors with
co-located STOP conditions; each STOP predicate **explicitly names "the EVALUABILITY
ARCHITECTURE COMPETITOR section"** as the resolution target, making the STOP condition
independently checkable from its text alone without reading the surrounding declaration prose
(C-50 mechanism). C-47 also passes (Architecture labels + STOP enforcement present). C-49 is
ablated: Phase 9 PREREQUISITE quotes the EVALUABILITY GATE identifier verbatim and includes
an independence boundary declaration (satisfying C-45 and C-48) but has no positive
audit-sufficiency claim.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain Architecture-labeled STOP predicates at Phase 8.5 that each name "the EVALUABILITY ARCHITECTURE COMPETITOR section" as the resolution target -- any output where the STOP predicates enforce label presence without naming the section (e.g., "STOP: if Architecture A label is absent"), or where the STOP conditions are absent entirely, falsifies the C-50 hypothesis. | The section-naming in each STOP predicate makes the STOP self-contained: a maintainer reading only the STOP text can identify (a) which Architecture label is being enforced, (b) the named section the label must resolve to, and (c) the consequence of resolution failure -- no adjacent prose read required; outputs from V-02 will show section-named STOP predicates at Phase 8.5 vs V-01 outputs which show prose-only Phase 8.5 without Architecture labels or STOP enforcement. | V-01 is the primary C-50 absence control (no Architecture labels, no STOP); the second control is any V-02 variant that has STOP enforcement but STOP predicates that omit the section name -- comparing STOP predicate text across V-02 (names "EVALUABILITY ARCHITECTURE COMPETITOR section") and a minimal C-47-pass variant (enforces label presence without naming section) isolates whether section-naming in the predicate -- not just STOP enforcement -- is load-bearing for C-50; prediction: V-02 passes C-50, V-01 cannot produce C-50, a STOP-without-section-name variant fails C-50. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

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

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

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

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

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

---

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map entirely, or includes it as an optional annotation rather than a required
terminal section. Architecture A fails C-43: the terminal evaluability section is absent from
the emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing (ablation control) -- the EVALUABILITY ARCHITECTURE COMPETITOR
section uses Architecture A/B labels; Phase 8.5 NON-REDUNDANCY DECLARATION references the
Architecture A/B labels but has NO STOP-condition enforcement at all. Phase 9 PREREQUISITE:
verbatim gate-ID only (C-45 satisfied; C-48 ablated -- no independence boundary declaration;
C-49 ablated). Hypothesis: Architecture labels without STOP enforcement do not satisfy C-47,
and without C-47 the C-50 question (STOP predicate names resolution section) cannot be
evaluated. Primary purpose: isolate whether the Architecture label structure alone -- without
STOP conditions -- provides any path to C-47 or C-50 passes.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-03 will contain Architecture A/B labels in the NON-REDUNDANCY DECLARATION but no STOP conditions enforcing label resolution against the EVALUABILITY ARCHITECTURE COMPETITOR section -- any output that adds STOP conditions falsifies the ablation hypothesis; any output that omits the Architecture labels confirms the inertia-framing baseline. | The absence of STOP enforcement means a maintainer reading the NON-REDUNDANCY DECLARATION encounters Architecture labels but has no enforcement instruction -- the labels are advisory rather than structural; V-03 outputs will show Architecture label references without co-located STOP conditions, vs V-02 outputs which show Architecture labels + STOP conditions naming the resolution section; the comparison isolates whether STOP enforcement -- not labeling -- is the load-bearing C-47/C-50 mechanism. | V-02 is the primary positive control for C-47/C-50: V-02 has Architecture labels + STOP predicates naming the EVALUABILITY ARCHITECTURE COMPETITOR section (C-47 pass, C-50 pass); V-03 has Architecture labels but no STOP conditions (predicted: C-47 fail, C-50 cannot be evaluated); comparison isolates whether STOP enforcement -- not Architecture labeling -- is necessary for C-47; prediction: V-03 fails C-47 (STOP is load-bearing) and cannot produce a C-50 score. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

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

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

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

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

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

---

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Architecture A fails C-43.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

---

## V-04 -- Combined (Role Sequence + Lifecycle Emphasis + Inertia Framing)

**Axis:** Combined -- Role sequence (C-49) + Lifecycle emphasis (C-50). Phase 9 PREREQUISITE:
verbatim gate-ID (C-45) + independence boundary naming ROLE: EVALUABILITY AUDITOR (C-48) +
positive audit-sufficiency claim (C-49 mechanism). Phase 8.5: EVALUABILITY ARCHITECTURE
COMPETITOR section with Architecture A/B entries + NON-REDUNDANCY DECLARATION with
Architecture A/B labeled anchors + co-located STOP predicates explicitly naming "the
EVALUABILITY ARCHITECTURE COMPETITOR section" (C-47 pass, C-50 mechanism). Tests whether
C-49 and C-50 simultaneously pass on top of the full C-45/C-46/C-47/C-48 baseline.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-04 will contain both the three-part Phase 9 PREREQUISITE (gate-ID + independence boundary + positive sufficiency) and Architecture-labeled STOP predicates naming "the EVALUABILITY ARCHITECTURE COMPETITOR section" at Phase 8.5 -- any output failing either mechanism falsifies the combined hypothesis. | The two mechanisms are independent: the Phase 9 PREREQUISITE three-part structure governs C-49 at the Phase 9 entry level; the STOP predicate section-naming governs C-50 at the Phase 8.5 NON-REDUNDANCY DECLARATION level; a model can produce one without the other, and V-01 and V-02 demonstrate this independence via single-axis ablation. | V-01 (C-49 pass, C-50 absent) and V-02 (C-49 absent, C-50 pass) are the ablation controls; V-04 combines both; prediction: V-04 passes C-49 and C-50 jointly, composite >= 42/42 x 10 + 10 = 100 if all other criteria also pass. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

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

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

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

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

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

---

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map entirely, or includes it as an optional annotation rather than a required
terminal section. Architecture A fails C-43: the terminal evaluability section is absent from
the emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

---

## V-05 -- Combined + Phrasing Register (Full Integration)

**Axis:** Combined (V-04 mechanisms) + Phrasing register. Phase 9 PREREQUISITE: verbatim
gate-ID (C-45) + independence boundary naming ROLE: EVALUABILITY AUDITOR (C-48) + positive
audit-sufficiency claim (C-49) + **explicit bidirectionality purpose clause** ("making this
PREREQUISITE a bidirectional independence declaration: a reader can confirm both what is
excluded from sequencing verification and what can be confirmed from this line alone").
Phase 8.5: EVALUABILITY ARCHITECTURE COMPETITOR section + Architecture A/B labeled anchors
+ STOP predicates naming the EVALUABILITY ARCHITECTURE COMPETITOR section (C-47, C-50) +
**explicit self-sufficiency purpose clause** ("making this STOP condition independently
verifiable from its text alone, without reading adjacent NON-REDUNDANCY DECLARATION prose").
Tests whether explicit purpose declarations add measurable criterion-expression density vs
V-04's implicit mechanisms.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-05 will contain both the three-part Phase 9 PREREQUISITE (gate-ID + independence boundary + positive sufficiency) and Architecture-labeled STOP predicates naming the EVALUABILITY ARCHITECTURE COMPETITOR section, AND will additionally contain explicit purpose clauses at both locations explaining the auditability property being established -- any output that omits the purpose clauses while retaining the mechanisms predicts that purpose clauses are stylistically optional but not mechanistically required. | The explicit purpose clauses convert implicit structural properties (bidirectionality at Phase 9, self-sufficiency at Phase 8.5) into named and declared properties: a reader encountering the Phase 9 PREREQUISITE is told not just that the PREREQUISITE is bidirectional but why it is bidirectional; a reader encountering the Phase 8.5 STOP is told not just that the predicate names the section but that naming the section makes the STOP self-sufficient; purpose-clause outputs may yield a distinct excellence signal pattern in R17. | V-04 is the direct comparison: V-04 has the same mechanisms without explicit purpose clauses; comparing V-04 and V-05 outputs isolates whether purpose-clause density -- not mechanism presence -- drives any observed criterion expression differences; prediction: V-05 passes C-49 and C-50 with higher expression density than V-04; any new R17 excellence signal is predicted to emerge from V-05. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

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

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

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

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

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

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

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

---

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map entirely, or includes it as an optional annotation rather than a required
terminal section. Architecture A fails C-43: the terminal evaluability section is absent from
the emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete
  -- making this STOP condition independently verifiable from its text alone, without reading
  adjacent NON-REDUNDANCY DECLARATION prose to learn which section Architecture A must
  resolve to.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete
  -- making this STOP condition independently verifiable from its text alone, without reading
  adjacent NON-REDUNDANCY DECLARATION prose to learn which section Architecture B must
  resolve to.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR --
making this PREREQUISITE a bidirectional independence declaration: a reader can confirm both
what is excluded from sequencing verification and what can be confirmed from this line alone.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

---
