---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-16
version: 19
round: R19
rubric: quest-rubric-variate-v19-R18-2026-03-16.md
baseline_score: "40/42 x 10 = 9.52 (V satisfying all R18 criteria, C-49 FAIL, C-50 FAIL)"
targets: C-49, C-50
---

# quest-rubric Variate — Round 19 (Against rubric v19, targeting C-49/C-50)

**Date:** 2026-03-16
**Rubric:** v19 (C-01–C-50; denominator /42; adds C-49: FORMAT TEMPLATE with mandatory [C-NN]
slot in Phase 8.5 failure-mode clauses — criterion-ID inclusion structurally enforced by
template slot, not only behaviorally instructed by prose, so omission is visible as an
unfilled placeholder; adds C-50: full criterion-span enumeration in STATUS QUO foil items —
every passing criterion in the span between consecutive failure points must be explicitly
named, converting the foil item from a partial bidirectional statement to a precision
criterion-lattice locator)
**Target criteria:** C-49, C-50

**Round 19 design note:** R18 confirmed C-47 (criterion-ID-named failure-mode clause) and
C-48 (pass/fail criterion-pair foil items) stable across all R18 variations. R18 V-03
produced Phase 8.5 notes from a FORMAT TEMPLATE with a mandatory [C-NN] slot — criterion ID
structurally embedded rather than prose-instructed, establishing ES-R18-1 as the C-49
excellence signal. R18 V-02 produced STATUS QUO foil items of the form "passes C-01 through
C-04 while failing C-05" using range notation and cumulative-from-start framing — V-04 used
the same cumulative framing. Neither satisfied C-50 because partial or range-notation spans
leave gaps on the pass side. R19 explores:

- **C-49 probe (V-01, single-axis):** FORMAT TEMPLATE with mandatory [C-NN] slot in Phase 8.5.
  STATUS QUO foil items use cumulative range notation (C-48 PASS, C-50 FAIL). Ablation
  control for C-50.
- **C-50 probe (V-02, single-axis):** Per-span explicit enumeration in STATUS QUO foil items.
  Phase 8.5 failure-mode clauses name criterion IDs in prose (C-47 PASS, C-49 FAIL). Ablation
  control for C-49.
- **C-50 via SPAN DEFINITION (V-03, single-axis):** SPAN DEFINITION pre-step co-located with
  STATUS QUO foil item instruction — builder computes span bounds before writing each foil
  item, then enumerates the full pass-side list. Different structural mechanism from V-02 for
  achieving C-50. Phase 8.5 remains prose criterion-ID (C-49 FAIL).
- **Combined (V-04):** FORMAT TEMPLATE (C-49) + per-span explicit enumeration (C-50). Tests
  joint satisfiability without interference.
- **Combined + phrasing register (V-05):** V-04 mechanisms plus explicit SLOT-FILL STOP in
  Phase 8.5 and FULL-SPAN STOP in STATUS QUO — structural defect is named as a visible
  placeholder rather than a silent omission. Ceiling form.

---

## Prediction Table

| Variation | Axis | C-49 signal | C-50 signal | C-47/C-48 preserved | C-45/C-46 preserved | Notes |
|-----------|------|-------------|-------------|---------------------|---------------------|-------|
| V-01 | Lifecycle emphasis | FORMAT TEMPLATE with [C-NN] slot — criterion ID is structural slot, not prose instruction | Absent — cumulative range notation (C-48 PASS, C-50 FAIL) | Preserved | Preserved | Single-axis; prediction: V-01 passes C-49, fails C-50 |
| V-02 | Inertia framing | Absent — criterion IDs in prose (C-47 PASS, C-49 FAIL) | Per-span explicit enumeration — "passes C-04 and C-05 while failing C-06" names all criteria in the span | Preserved | Preserved | Single-axis; prediction: V-02 fails C-49, passes C-50 |
| V-03 | Output format | Absent — criterion IDs in prose (C-47 PASS, C-49 FAIL) | SPAN DEFINITION pre-step forces builder to compute span bounds before writing each foil item, then enumerate explicitly | Preserved | Preserved | Single-axis alternative C-50 mechanism; tests whether span-computation scaffolding vs direct instruction changes C-50 pass rate; prediction: V-03 fails C-49, passes C-50 |
| V-04 | Combined (Lifecycle + Inertia) | FORMAT TEMPLATE with [C-NN] slot (V-01) | Per-span explicit enumeration (V-02) | Preserved | Preserved | Combined; tests joint satisfiability; prediction: V-04 passes both C-49 and C-50 |
| V-05 | Combined + Phrasing register | FORMAT TEMPLATE + SLOT-FILL STOP naming unfilled bracket as visible structural defect | Per-span explicit enumeration + FULL-SPAN STOP naming range notation as non-compliant form | Preserved | Preserved | V-04 + explicit STOP conditions at both sites; tests whether STOP framing at defect detection adds measurable ceiling lift vs V-04; prediction: V-05 passes both C-49 and C-50 with highest defect-detection specificity |

---

## V-01 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis — Phase 8.5 is restructured around a PER-NOTE FORMAT TEMPLATE
with three required slots, one of which is the criterion ID: `Absent this path, [C-NN] is
unenforced at [gate name] entry.` The `[C-NN]` slot is presented as a mandatory unfilled
placeholder that the builder must populate when writing each enforcement-path note — its
omission would leave a visible bracket rather than produce a silent prose omission. STATUS QUO
COMPETITOR foil items pair passing and failing criteria (C-48 PASS) but express the pass side
as a cumulative range from the start of the rubric (C-50 FAIL — partial span, range notation).
All other R18 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain Phase 8.5 enforcement-path notes that follow the three-slot FORMAT TEMPLATE verbatim, with the [C-NN] slot populated by a specific criterion ID — e.g., "Absent this path, C-43 is unenforced at Phase 9 entry" — rather than a prose gap description or a note with the [C-NN] bracket left unfilled; any output where the note form deviates from the template structure (ID absent, bracket visible, or prose-only) falsifies the FORMAT TEMPLATE hypothesis. | The FORMAT TEMPLATE converts criterion-ID naming from a behavioral instruction to a structural slot: a builder following the template cannot produce a compliant note without filling the [C-NN] slot; this is structurally distinct from V-02's prose instruction (which names the criterion but does not make the [C-NN] placeholder visible as an unfilled defect); V-01 outputs should show template-slot-populated notes while STATUS QUO foil items continue to use cumulative range notation on the pass side. | V-02 is the primary C-49 ablation control: V-02 has criterion-IDs in prose failure-mode clauses (C-47 PASS, C-49 FAIL) and per-span explicit enumeration in foil items (C-50 PASS); comparing Phase 8.5 note form across V-01 (FORMAT TEMPLATE, C-49 probe) and V-02 (prose criterion IDs, C-49 FAIL) isolates whether template scaffolding is load-bearing for C-49 beyond prose instruction; prediction: V-01 passes C-49, V-02 fails C-49. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write pass conditions on the fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03**: essential criteria not grounded in the skill's actual non-negotiable behaviors;
  criteria come from intuition about good output rather than from systematic analysis of
  broken output.
- Fails to produce causal direction templates — **passes C-01 through C-05 while failing
  C-06**: Text fields describe presence of good properties, not consequence of absence; the
  causal direction "Without Y, Z fails" is absent.
- Fails to enforce pass observability by template — **passes C-01 through C-08 while failing
  C-09**: pass conditions include bare qualitative language with no concrete anchor; two
  independent evaluators cannot reach the same verdict without discussion.
- Fails to name a reference anchor with Falls-short dimension — **passes C-01 through C-09
  while failing C-10**: aspirational gap not anchored against a named baseline; inertia test
  not applicable because no discrimination target exists.

**From the description above, derive what the required rubric-building procedure must supply
— before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 — FAILURE MODE ANALYSIS

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form — in
any phrasing — is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION — ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates.

---

### PHASE 3 — ESSENTIAL CRITERIA (3–5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 — RECOMMENDED CRITERIA (2–3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

---

### PHASE 4.5 — POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** — The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential criteria are predominantly
> "correctness" and aspirational criteria are also predominantly "correctness" passes the
> standard audit. The tier convergence is invisible to the standard check. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... — majority: [category]
Recommended tier:  [category] x[N] ... — majority: [category]
Aspirational tier: [category] x[N]     — majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 — REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied — at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL names ROLE: MECHANISM DEFINER as the
predecessor gate. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1–2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
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

### PHASE 6.75 — COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A — Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B — Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C — Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 — PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1–2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 — SCORING

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
include the map as a terminal section in the emitted artifact. Architecture A fails C-43:
the terminal evaluability section is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44: the Independence field is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 — NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

**STOP if any EVIDENCE QUOTATION GATE note omits the [C-NN] slot** — a note of the form
"Absent this path, the evaluability requirement would pass unchallenged" does not satisfy the
template because it describes the structural gap in prose without naming the criterion ID
left unenforced. The compliant form names the criterion: "Absent this path, C-43 is
unenforced at emit entry." These two forms are structurally distinct: the prose form is a
detection record; the criterion-ID form is a criterion-indexed compliance claim auditable by
ID lookup.

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP: if Architecture B label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows
populated, Verification Artifact named for every row, Scan Method named for every row, and
Independence field naming excluded content for every row.**

For each structural criterion, produce:

```
EVALUABILITY GATE — Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes — independently verifiable without reading [named excluded content] |
```

Independence column requirement: "Yes — independently verifiable without reading [named
excluded content]" where [named excluded content] names the specific construction records
that a verifier can skip. "Yes — independently verifiable" without the exclusion name fails.

STOP CONDITION: The EVALUABILITY GATE is not satisfied until every row has all three cells
populated. Any blank cell or generic Independence claim blocks the gate.

---

### PHASE 9 — EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** — all F-NN entries from Phase 1
2. **Design Rationale** — dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons
3. **Essential Criteria** — all five fields per criterion
4. **Recommended Criteria** — all five fields per criterion
5. **Independence Map** — the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** — all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** — COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE
8. **Scoring** — composite formula, golden threshold, three-state table
9. **Notes** — `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** — patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** — reproduce the EVALUABILITY GATE output verbatim as the
    final section; all four columns must be present for every structural criterion

---

## V-02 — Inertia Framing

**Axis:** Inertia framing — the STATUS QUO COMPETITOR block is elevated to use per-span
explicit enumeration for every foil item. Each foil item names every criterion in the span
between the previous failure point and the current failure point on the pass side, rather
than using a cumulative range from the start of the rubric. The instruction co-located with
the foil items states the span rule explicitly: "Span = criteria between [previous failure
criterion] and [current failure criterion]; enumerate every passing criterion in the span."
Phase 8.5 NON-REDUNDANCY DECLARATION names criterion IDs in prose (C-47 PASS) without a
FORMAT TEMPLATE structure (C-49 FAIL). All other R18 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain STATUS QUO COMPETITOR foil items where the pass side explicitly enumerates every criterion in the span between the previous failure criterion and the current failure criterion — e.g., "passes C-04 and C-05 while failing C-06" (span from C-03 to C-06 = {C-04, C-05}) rather than "passes C-01 through C-05 while failing C-06" (cumulative from start, ignores C-03 failure); any output where foil items use range notation or skip criteria in the span falsifies the full-span hypothesis. | Full-span enumeration converts the foil item from a partial bidirectional discrimination statement to a precision criterion-lattice locator: a reviewer reading "passes C-04 and C-05 while failing C-06" knows the exact lattice position of the STATUS QUO (passes through C-05, fails at C-06, previous failure was at C-03) without reading any other foil item; V-02 outputs will show per-span foil items while Phase 8.5 notes continue to name criterion IDs in prose without template scaffolding. | V-01 is the primary C-50 ablation control: V-01 has FORMAT TEMPLATE in Phase 8.5 (C-49 probe) and cumulative range notation in foil items (C-50 FAIL); comparing STATUS QUO foil item form across V-02 (per-span explicit, C-50 probe) and V-01 (cumulative range, C-50 FAIL) isolates whether per-span explicit enumeration is load-bearing for C-50; prediction: V-02 passes C-50, V-01 fails C-50. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write pass conditions on the fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

Each foil item below names every criterion in the span between the previous failure point
and the current failure point on the pass side. Span = {criteria between previous FAIL and
current FAIL that the STATUS QUO passes}.

- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03** (span from START to C-03: C-01, C-02): essential criteria not grounded in the
  skill's actual non-negotiable behaviors; criteria come from intuition about good output
  rather than from systematic analysis of broken output.
- Fails to produce causal direction templates — **passes C-04 and C-05 while failing C-06**
  (span from C-03 to C-06: C-04, C-05): Text fields describe presence of good properties,
  not consequence of absence; the causal direction "Without Y, Z fails" is absent.
- Fails to name a reference anchor with Falls-short dimension — **passes C-07, C-08, and
  C-09 while failing C-10** (span from C-06 to C-10: C-07, C-08, C-09): aspirational gap
  not anchored against a named baseline; inertia test not applicable because no
  discrimination target exists.
- Fails to verify mechanism independence — **passes C-11 and C-12 while failing C-13** (span
  from C-10 to C-13: C-11, C-12): independence map absent; aspirational criteria may share
  a mechanism, making redundancy between criteria undetectable without running isolation
  experiments.

**From the description above, derive what the required rubric-building procedure must supply
— before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 — FAILURE MODE ANALYSIS

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form — in
any phrasing — is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION — ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates.

---

### PHASE 3 — ESSENTIAL CRITERIA (3–5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 — RECOMMENDED CRITERIA (2–3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

---

### PHASE 4.5 — POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** — The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential criteria are predominantly
> "correctness" and aspirational criteria are also predominantly "correctness" passes the
> standard audit. The tier convergence is invisible to the standard check. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... — majority: [category]
Recommended tier:  [category] x[N] ... — majority: [category]
Aspirational tier: [category] x[N]     — majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 — REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied — at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL names ROLE: MECHANISM DEFINER as the
predecessor gate. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1–2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
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

### PHASE 6.75 — COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A — Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B — Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C — Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 — PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1–2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 — SCORING

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
include the map as a terminal section in the emitted artifact. Architecture A fails C-43:
the terminal evaluability section is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44: the Independence field is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 — NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): **C-43 is unenforced at emit entry** — the
  Criterion Evaluability Map remains in the construction record only; absent enforcement
  path 2 (terminal map requirement), **C-43 is unenforced at Phase 9 entry**; a criterion
  emitted without the terminal evaluability section would pass Phase 9 unchallenged.
  See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if Architecture A label does not resolve to a named entry in the EVALUABILITY
  ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.

- Architecture B (terminal-table-only, no gate): **C-44 is unenforced at the pre-emit
  stage** — the Independence field is populated by the emit phase without pre-Phase-9
  verification; absent enforcement path 1 (EVALUABILITY GATE), **C-44 is unenforced at
  Phase 8 entry**; a criterion with generic Independence declarations would pass the
  EVALUABILITY GATE unchallenged.
  See Architecture B in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if Architecture B label does not resolve to a named entry in the EVALUABILITY
  ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows
populated, Verification Artifact named for every row, Scan Method named for every row, and
Independence field naming excluded content for every row.**

For each structural criterion, produce:

```
EVALUABILITY GATE — Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes — independently verifiable without reading [named excluded content] |
```

Independence column requirement: "Yes — independently verifiable without reading [named
excluded content]" where [named excluded content] names the specific construction records
that a verifier can skip. "Yes — independently verifiable" without the exclusion name fails.

STOP CONDITION: The EVALUABILITY GATE is not satisfied until every row has all three cells
populated. Any blank cell or generic Independence claim blocks the gate.

---

### PHASE 9 — EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** — all F-NN entries from Phase 1
2. **Design Rationale** — dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons
3. **Essential Criteria** — all five fields per criterion
4. **Recommended Criteria** — all five fields per criterion
5. **Independence Map** — the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** — all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** — COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE
8. **Scoring** — composite formula, golden threshold, three-state table
9. **Notes** — `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** — patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** — reproduce the EVALUABILITY GATE output verbatim as the
    final section; all four columns must be present for every structural criterion

---

## V-03 — Output Format

**Axis:** Output format — the STATUS QUO COMPETITOR block is restructured with a SPAN
DEFINITION pre-step co-located with the foil item writing instruction. Before writing each
foil item, the builder must define the span in a named slot:

```
SPAN DEFINITION:
  Previous failure: [C-NN or START]
  Current failure:  [C-NN]
  Pass side (enumerate every criterion in span): [C-NN, C-NN, ...]
```

The foil item is then written from the SPAN DEFINITION's pass-side list, guaranteeing
explicit per-criterion enumeration rather than range notation or cumulative framing. This
is a structural mechanism distinct from V-02's direct instruction ("enumerate every passing
criterion in the span"): V-03 makes span computation a named intermediate step with a
visible output format that the foil item must reference. Phase 8.5 names criterion IDs in
prose (C-47 PASS, C-49 FAIL). All other R18 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-03 will contain STATUS QUO COMPETITOR foil items written from a completed SPAN DEFINITION — the pass-side list in the SPAN DEFINITION slot enumerates every criterion between the previous failure and the current failure, and the foil item reproduces that list verbatim; any output where foil items use range notation, cumulative framing, or skip criteria in the span falsifies the SPAN DEFINITION hypothesis; compare V-03 (SPAN DEFINITION intermediate step) against V-02 (direct instruction) to test whether the intermediate computation step yields higher C-50 pass rates. | The SPAN DEFINITION converts full-span enumeration from a quality instruction to a production process: a builder following the SPAN DEFINITION step cannot write a foil item without first computing the pass side, then transcribing the list; V-02's direct instruction relies on the builder remembering to enumerate all criteria in the span; V-03's intermediate step makes omission visible as a gap in the SPAN DEFINITION output, not only as a gap in the foil item itself. | V-02 is the direct comparison for V-03: both target C-50, both ablate C-49; V-02 uses a direct instruction ("enumerate every passing criterion in the span"); V-03 uses an intermediate SPAN DEFINITION step; if V-03 produces higher C-50 pass rates than V-02, the intermediate-step mechanism is load-bearing; if rates are equivalent, direct instruction is sufficient and the intermediate step adds no measurable value for C-50. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write pass conditions on the fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

For each failure below, a SPAN DEFINITION precedes the foil item. The foil item is written
from the SPAN DEFINITION's pass-side list.

```
SPAN DEFINITION:
  Previous failure: START
  Current failure:  C-03
  Pass side (every criterion in span): C-01, C-02
```
- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03**: essential criteria not grounded in the skill's actual non-negotiable behaviors;
  criteria come from intuition about good output rather than from systematic analysis of
  broken output.

```
SPAN DEFINITION:
  Previous failure: C-03
  Current failure:  C-06
  Pass side (every criterion in span): C-04, C-05
```
- Fails to produce causal direction templates — **passes C-04 and C-05 while failing C-06**:
  Text fields describe presence of good properties, not consequence of absence; the causal
  direction "Without Y, Z fails" is absent.

```
SPAN DEFINITION:
  Previous failure: C-06
  Current failure:  C-10
  Pass side (every criterion in span): C-07, C-08, C-09
```
- Fails to name a reference anchor with Falls-short dimension — **passes C-07, C-08, and
  C-09 while failing C-10**: aspirational gap not anchored against a named baseline;
  inertia test not applicable because no discrimination target exists.

```
SPAN DEFINITION:
  Previous failure: C-10
  Current failure:  C-13
  Pass side (every criterion in span): C-11, C-12
```
- Fails to verify mechanism independence — **passes C-11 and C-12 while failing C-13**:
  independence map absent; aspirational criteria may share a mechanism, making redundancy
  between criteria undetectable without running isolation experiments.

**From the description above, derive what the required rubric-building procedure must supply
— before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 — FAILURE MODE ANALYSIS

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form — in
any phrasing — is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION — ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates.

---

### PHASE 3 — ESSENTIAL CRITERIA (3–5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 — RECOMMENDED CRITERIA (2–3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

---

### PHASE 4.5 — POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** — The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential criteria are predominantly
> "correctness" and aspirational criteria are also predominantly "correctness" passes the
> standard audit. The tier convergence is invisible to the standard check. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... — majority: [category]
Recommended tier:  [category] x[N] ... — majority: [category]
Aspirational tier: [category] x[N]     — majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 — REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied — at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL names ROLE: MECHANISM DEFINER as the
predecessor gate. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1–2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
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

### PHASE 6.75 — COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A — Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B — Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C — Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 — PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1–2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 — SCORING

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
include the map as a terminal section in the emitted artifact. Architecture A fails C-43:
the terminal evaluability section is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44: the Independence field is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 — NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): **C-43 is unenforced at emit entry** — the
  Criterion Evaluability Map remains in the construction record only; absent enforcement
  path 2 (terminal map requirement), **C-43 is unenforced at Phase 9 entry**; a criterion
  emitted without the terminal evaluability section would pass Phase 9 unchallenged.
  See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if Architecture A label does not resolve to a named entry in the EVALUABILITY
  ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.

- Architecture B (terminal-table-only, no gate): **C-44 is unenforced at the pre-emit
  stage** — the Independence field is populated by the emit phase without pre-Phase-9
  verification; absent enforcement path 1 (EVALUABILITY GATE), **C-44 is unenforced at
  Phase 8 entry**; a criterion with generic Independence declarations would pass the
  EVALUABILITY GATE unchallenged.
  See Architecture B in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if Architecture B label does not resolve to a named entry in the EVALUABILITY
  ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows
populated, Verification Artifact named for every row, Scan Method named for every row, and
Independence field naming excluded content for every row.**

For each structural criterion, produce:

```
EVALUABILITY GATE — Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes — independently verifiable without reading [named excluded content] |
```

Independence column requirement: "Yes — independently verifiable without reading [named
excluded content]" where [named excluded content] names the specific construction records
that a verifier can skip. "Yes — independently verifiable" without the exclusion name fails.

STOP CONDITION: The EVALUABILITY GATE is not satisfied until every row has all three cells
populated. Any blank cell or generic Independence claim blocks the gate.

---

### PHASE 9 — EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** — all F-NN entries from Phase 1
2. **Design Rationale** — dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons
3. **Essential Criteria** — all five fields per criterion
4. **Recommended Criteria** — all five fields per criterion
5. **Independence Map** — the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** — all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** — COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE
8. **Scoring** — composite formula, golden threshold, three-state table
9. **Notes** — `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** — patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** — reproduce the EVALUABILITY GATE output verbatim as the
    final section; all four columns must be present for every structural criterion

---

## V-04 — Combined (Lifecycle Emphasis + Inertia Framing)

**Axis:** Combined — Phase 8.5 is restructured with a FORMAT TEMPLATE containing a mandatory
[C-NN] slot (V-01 mechanism, C-49 probe) AND STATUS QUO COMPETITOR foil items use per-span
explicit enumeration (V-02 mechanism, C-50 probe). Tests whether C-49 and C-50 are jointly
satisfiable without interference. The two mechanisms govern structurally distinct sections:
FORMAT TEMPLATE operates at Phase 8.5; per-span enumeration operates at STATUS QUO COMPETITOR.
All other R18 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-04 will contain both (a) Phase 8.5 notes structured by the PER-NOTE FORMAT TEMPLATE with the [C-NN] slot populated — e.g., "Absent this path, C-43 is unenforced at Phase 9 entry" produced from the template slot — and (b) STATUS QUO foil items with per-span explicit enumeration — e.g., "passes C-04 and C-05 while failing C-06" where C-04 and C-05 are every criterion in the span from C-03 to C-06; any output missing either mechanism falsifies the joint-satisfiability hypothesis. | Joint activation tests whether the FORMAT TEMPLATE and per-span enumeration mechanisms interfere: FORMAT TEMPLATE operates in Phase 8.5 on enforcement-path note structure; per-span enumeration operates in STATUS QUO COMPETITOR on foil-item pass-side construction; since the two mechanisms govern structurally and positionally distinct sections of the skill prompt, interference is not expected; V-04 outputs should show both patterns simultaneously at rates comparable to the single-axis variations (V-01 for FORMAT TEMPLATE, V-02 for per-span). | V-01 (FORMAT TEMPLATE only, per-span ablated) and V-02 (per-span only, FORMAT TEMPLATE ablated) are the independent single-axis controls; if V-04 passes both C-49 and C-50, joint satisfiability is confirmed and the two mechanisms are orthogonal; if V-04 passes one but fails the other at rates similar to the corresponding single-axis variation, one mechanism suppresses the other; prediction: V-04 passes both C-49 and C-50, establishing the joint ceiling for R19. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write pass conditions on the fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

Each foil item below names every criterion in the span between the previous failure point
and the current failure point on the pass side. Span = {criteria between previous FAIL and
current FAIL that the STATUS QUO passes}.

- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03** (span from START to C-03: C-01, C-02): essential criteria not grounded in the
  skill's actual non-negotiable behaviors; criteria come from intuition about good output
  rather than from systematic analysis of broken output.
- Fails to produce causal direction templates — **passes C-04 and C-05 while failing C-06**
  (span from C-03 to C-06: C-04, C-05): Text fields describe presence of good properties,
  not consequence of absence; the causal direction "Without Y, Z fails" is absent.
- Fails to name a reference anchor with Falls-short dimension — **passes C-07, C-08, and
  C-09 while failing C-10** (span from C-06 to C-10: C-07, C-08, C-09): aspirational gap
  not anchored against a named baseline; inertia test not applicable because no
  discrimination target exists.
- Fails to verify mechanism independence — **passes C-11 and C-12 while failing C-13** (span
  from C-10 to C-13: C-11, C-12): independence map absent; aspirational criteria may share
  a mechanism, making redundancy between criteria undetectable without running isolation
  experiments.

**From the description above, derive what the required rubric-building procedure must supply
— before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 — FAILURE MODE ANALYSIS

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form — in
any phrasing — is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION — ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates.

---

### PHASE 3 — ESSENTIAL CRITERIA (3–5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 — RECOMMENDED CRITERIA (2–3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

---

### PHASE 4.5 — POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** — The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential criteria are predominantly
> "correctness" and aspirational criteria are also predominantly "correctness" passes the
> standard audit. The tier convergence is invisible to the standard check. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... — majority: [category]
Recommended tier:  [category] x[N] ... — majority: [category]
Aspirational tier: [category] x[N]     — majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 — REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied — at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL names ROLE: MECHANISM DEFINER as the
predecessor gate. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1–2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
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

### PHASE 6.75 — COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A — Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B — Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C — Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 — PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1–2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 — SCORING

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
include the map as a terminal section in the emitted artifact. Architecture A fails C-43:
the terminal evaluability section is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44: the Independence field is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 — NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

**STOP if any EVIDENCE QUOTATION GATE note omits the [C-NN] slot** — a note of the form
"Absent this path, the evaluability requirement would pass unchallenged" does not satisfy the
template because it describes the structural gap in prose without naming the criterion ID
left unenforced. The compliant form names the criterion: "Absent this path, C-43 is
unenforced at emit entry." These two forms are structurally distinct: the prose form is a
detection record; the criterion-ID form is a criterion-indexed compliance claim auditable by
ID lookup.

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP: if Architecture B label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows
populated, Verification Artifact named for every row, Scan Method named for every row, and
Independence field naming excluded content for every row.**

For each structural criterion, produce:

```
EVALUABILITY GATE — Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes — independently verifiable without reading [named excluded content] |
```

Independence column requirement: "Yes — independently verifiable without reading [named
excluded content]" where [named excluded content] names the specific construction records
that a verifier can skip. "Yes — independently verifiable" without the exclusion name fails.

STOP CONDITION: The EVALUABILITY GATE is not satisfied until every row has all three cells
populated. Any blank cell or generic Independence claim blocks the gate.

---

### PHASE 9 — EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** — all F-NN entries from Phase 1
2. **Design Rationale** — dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons
3. **Essential Criteria** — all five fields per criterion
4. **Recommended Criteria** — all five fields per criterion
5. **Independence Map** — the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** — all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** — COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE
8. **Scoring** — composite formula, golden threshold, three-state table
9. **Notes** — `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** — patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** — reproduce the EVALUABILITY GATE output verbatim as the
    final section; all four columns must be present for every structural criterion

---

## V-05 — Combined + Phrasing Register

**Axis:** Combined + Phrasing register — V-04 mechanisms (FORMAT TEMPLATE for C-49,
per-span explicit enumeration for C-50) plus explicit STOP conditions at both modification
sites that name the non-compliant form and identify it as a visible structural defect rather
than a silent omission. In Phase 8.5: a SLOT-FILL STOP names an unfilled `[C-NN]` bracket
as a visible placeholder defect distinct from a prose omission. In STATUS QUO: a FULL-SPAN
STOP names range notation as a non-compliant form and identifies the compliance consequence.
The phrasing register shifts from "instruction + STOP" to "defect-class declaration +
compliant-form example + non-compliant-form example" at both sites. Tests whether explicit
defect-class framing at the STOP condition adds measurable ceiling lift beyond V-04's
mechanism presence alone.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-05 will contain both C-49-passing Phase 8.5 notes and C-50-passing STATUS QUO foil items, plus the STOP condition evidence: (a) Phase 8.5 notes will follow the FORMAT TEMPLATE with the [C-NN] slot populated, and any rubric produced under this prompt where a note omits the C-NN will have the unfilled bracket visible as a structural defect rather than absorbed into prose; (b) STATUS QUO foil items will have full per-span enumeration, and any foil item using range notation will fail the FULL-SPAN STOP which names range notation as a non-compliant form. | The SLOT-FILL STOP and FULL-SPAN STOP convert structural requirements from behavioral instructions to defect-class declarations: a reviewer checking a V-05 output does not need to infer that "[C-NN]" is required — the STOP names the non-compliant form explicitly and identifies the compliance consequence; V-05 outputs should show both C-49 and C-50 passing at rates at least as high as V-04, with higher defect-detection specificity (the STOP framing enables a reviewer to distinguish "FORMAT TEMPLATE absent" from "slot unfilled" as distinct failure modes). | V-04 is the primary comparison for V-05: V-04 has both FORMAT TEMPLATE and per-span enumeration without explicit STOP defect-class framing; V-05 adds SLOT-FILL STOP and FULL-SPAN STOP at both sites; if V-05 scores higher than V-04 on C-49 and C-50 by rubric evaluation, explicit defect-class framing adds measurable value beyond mechanism presence; if scores are equivalent, mechanism presence is the minimal sufficient structure and STOP framing is cosmetic at the ceiling. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write pass conditions on the fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

Each foil item below names every criterion in the span between the previous failure point
and the current failure point on the pass side. Span = {criteria between previous FAIL and
current FAIL that the STATUS QUO passes}.

**FULL-SPAN STOP:** A foil item of the form "passes C-04 through C-09 while failing C-10"
uses range notation and FAILS the full-span requirement — the range implicitly covers the
span but does not explicitly enumerate each criterion ID, so a reviewer cannot verify
completeness without counting criteria. A foil item of the form "passes C-04 and C-07 while
failing C-10" is also non-compliant — it names only a subset of the passing criteria in the
span. The compliant form explicitly lists every criterion: "passes C-04, C-05, C-06, C-07,
C-08, and C-09 while failing C-10."

- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03** (span from START to C-03: C-01, C-02): essential criteria not grounded in the
  skill's actual non-negotiable behaviors; criteria come from intuition about good output
  rather than from systematic analysis of broken output.
- Fails to produce causal direction templates — **passes C-04 and C-05 while failing C-06**
  (span from C-03 to C-06: C-04, C-05): Text fields describe presence of good properties,
  not consequence of absence; the causal direction "Without Y, Z fails" is absent.
- Fails to name a reference anchor with Falls-short dimension — **passes C-07, C-08, and
  C-09 while failing C-10** (span from C-06 to C-10: C-07, C-08, C-09): aspirational gap
  not anchored against a named baseline; inertia test not applicable because no
  discrimination target exists.
- Fails to verify mechanism independence — **passes C-11 and C-12 while failing C-13** (span
  from C-10 to C-13: C-11, C-12): independence map absent; aspirational criteria may share
  a mechanism, making redundancy between criteria undetectable without running isolation
  experiments.

**From the description above, derive what the required rubric-building procedure must supply
— before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 — FAILURE MODE ANALYSIS

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form — in
any phrasing — is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION — ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates.

---

### PHASE 3 — ESSENTIAL CRITERIA (3–5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 — RECOMMENDED CRITERIA (2–3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

---

### PHASE 4.5 — POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** — The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential criteria are predominantly
> "correctness" and aspirational criteria are also predominantly "correctness" passes the
> standard audit. The tier convergence is invisible to the standard check. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... — majority: [category]
Recommended tier:  [category] x[N] ... — majority: [category]
Aspirational tier: [category] x[N]     — majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 — REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied — at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL names ROLE: MECHANISM DEFINER as the
predecessor gate. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1–2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
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

### PHASE 6.75 — COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A — Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B — Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C — Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 — PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1–2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 — SCORING

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
include the map as a terminal section in the emitted artifact. Architecture A fails C-43:
the terminal evaluability section is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. Architecture B fails C-44: the Independence field is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 — NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

**SLOT-FILL STOP:** A note that contains the bracket `[C-NN]` left unfilled is a
NON-COMPLIANT note with a visible structural defect — the unfilled bracket is detectable by
string scan without reading surrounding prose. A note of the form "Absent this path, the
evaluability requirement would pass unchallenged" is also non-compliant — it describes the
structural gap in prose without naming the criterion ID, making the criterion-indexed claim
unverifiable by ID lookup. These two failure modes are structurally distinct: the unfilled
bracket is a template-production failure; the prose-only form is a criterion-ID omission
failure. Both produce a non-compliant note. The compliant form: "Absent this path, C-43 is
unenforced at Phase 9 entry" — criterion ID present, bracket filled, criterion-indexed claim
verifiable by ID lookup without reading surrounding prose.

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.
  SLOT-FILL STOP: if the [C-NN] slot above is not populated with a specific criterion ID.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP: if Architecture B label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.
  SLOT-FILL STOP: if the [C-NN] slot above is not populated with a specific criterion ID.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows
populated, Verification Artifact named for every row, Scan Method named for every row, and
Independence field naming excluded content for every row.**

For each structural criterion, produce:

```
EVALUABILITY GATE — Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes — independently verifiable without reading [named excluded content] |
```

Independence column requirement: "Yes — independently verifiable without reading [named
excluded content]" where [named excluded content] names the specific construction records
that a verifier can skip. "Yes — independently verifiable" without the exclusion name fails.

STOP CONDITION: The EVALUABILITY GATE is not satisfied until every row has all three cells
populated. Any blank cell or generic Independence claim blocks the gate.

---

### PHASE 9 — EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification.**

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** — all F-NN entries from Phase 1
2. **Design Rationale** — dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons
3. **Essential Criteria** — all five fields per criterion
4. **Recommended Criteria** — all five fields per criterion
5. **Independence Map** — the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** — all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** — COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE
8. **Scoring** — composite formula, golden threshold, three-state table
9. **Notes** — `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** — patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** — reproduce the EVALUABILITY GATE output verbatim as the
    final section; all four columns must be present for every structural criterion
