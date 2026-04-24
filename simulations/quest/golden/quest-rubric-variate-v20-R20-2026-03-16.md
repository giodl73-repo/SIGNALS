---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-16
version: 20
round: R20
rubric: quest-rubric-variate-v20-R19-2026-03-16.md
baseline_score: "42/44 x 10 = 9.55 (V satisfying C-49 + C-50 but lacking C-51 co-located STOP gate and C-52 SPAN DEFINITION pre-step)"
targets: C-51, C-52
---

# quest-rubric Variate — Round 20 (Against rubric v20, targeting C-51/C-52)

**Date:** 2026-03-16
**Rubric:** v20 (C-01–C-52; denominator /44; adds C-51: Phase 8.5 FORMAT TEMPLATE slot
gate-enforced by co-located STOP condition — the FORMAT TEMPLATE's mandatory [C-NN] slot
required by C-49 is co-located with a STOP condition that blocks Phase 8.5 note completion
until the slot is filled with a valid criterion ID, converting the structural slot from an
SV-detectable unfilled placeholder to a gate failure at note-completion time; adds C-52:
STATUS QUO foil items preceded by SPAN DEFINITION pre-step — each foil item is preceded by
a declared block naming (a) the previous failure criterion or START, (b) the current failure
criterion, and (c) the full pass-side enumeration, from which the foil item text is
transcribed, making span completeness structurally pre-declared rather than only observable
in the foil item text)
**Target criteria:** C-51, C-52

**Round 20 design note:** R19 confirmed C-51 (co-located STOP gate per note in Phase 8.5)
via V-01 and C-52 (SPAN DEFINITION pre-step before each foil item) via V-03, with V-02
serving as C-51 ablation control (full-span enumeration, no SPAN DEFINITION block) and V-01
serving as C-52 ablation control (FORMAT TEMPLATE + co-located STOP, no SPAN DEFINITION).
R19 V-04 combined C-49 + C-50 (per-span enumeration instruction), stopping short of C-51
and C-52. R19 V-05 added the SLOT-FILL STOP per note (C-51 PASS) and FULL-SPAN STOP
(C-50 PASS) but used direct per-span instruction without SPAN DEFINITION blocks (C-52 FAIL).
R20 explores:

- **C-51 probe (V-01, single-axis):** FORMAT TEMPLATE with co-located inline STOP per note
  (C-51 PASS). STATUS QUO uses per-span direct instruction without SPAN DEFINITION pre-steps
  (C-52 FAIL). Ablation control for C-52.
- **C-52 probe (V-02, single-axis):** SPAN DEFINITION pre-step before each foil item
  (C-52 PASS). Phase 8.5 uses FORMAT TEMPLATE with end-of-section STOP only — not
  co-located with the note template (C-51 FAIL). Ablation control for C-51.
- **C-51 via NOTE-COMPLETION GATE (V-03, single-axis):** Phase 8.5 uses FORMAT TEMPLATE
  plus a per-note NOTE-COMPLETION GATE named artifact block (rather than inline STOP text)
  that must show YES before advancing. SPAN DEFINITION pre-step present (C-52 PASS). Tests
  whether a named structural gate artifact satisfies C-51's "co-located blocking" requirement
  vs inline STOP text alone.
- **Combined (V-04):** FORMAT TEMPLATE + co-located inline STOP (C-51) + SPAN DEFINITION
  pre-step (C-52). Tests joint satisfiability.
- **Combined + phrasing register (V-05):** V-04 mechanisms plus each co-located STOP names
  the detection-failure consequence if the gate were bypassed; each SPAN DEFINITION pre-step
  names its function and includes a transcription STOP. Ceiling form.

---

## Prediction Table

| Variation | Axis | C-51 signal | C-52 signal | C-49/C-50 preserved | Notes |
|-----------|------|-------------|-------------|---------------------|-------|
| V-01 | Lifecycle emphasis | Co-located inline STOP per note — PASS C-51 | Per-span direct instruction, no SPAN DEFINITION block — PASS C-50, FAIL C-52 | Preserved | Single-axis C-51 probe; C-52 ablation control |
| V-02 | Inertia framing | End-of-section SLOT CHECK only, not co-located — FAIL C-51 | SPAN DEFINITION pre-step before each foil item — PASS C-52 | Preserved | Single-axis C-52 probe; C-51 ablation control |
| V-03 | Output format | NOTE-COMPLETION GATE named artifact block per note — PASS C-51 predicted; tests whether named-block gate vs inline STOP satisfies C-51 co-location requirement | SPAN DEFINITION pre-step — PASS C-52 | Preserved | Tests C-51 boundary: named artifact gate vs inline STOP |
| V-04 | Combined (Lifecycle + Inertia) | Co-located inline STOP per note — PASS C-51 | SPAN DEFINITION pre-step — PASS C-52 | Preserved | Joint satisfiability test; prediction: both PASS |
| V-05 | Combined + Phrasing register | Co-located STOP naming detection-failure consequence — PASS C-51 | SPAN DEFINITION with named function + transcription STOP — PASS C-52 | Preserved | Ceiling form; maximum structural specificity at both sites |

---

## V-01 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis — Phase 8.5 is restructured so each EVIDENCE QUOTATION GATE
note application has a co-located NOTE-COMPLETION STOP immediately following the note
template, blocking Phase 8.5 note completion until the [C-NN] slot is filled with a
specific criterion ID. This is the co-located STOP architecture that satisfies C-51: the
STOP is in the same instruction block as the note template, making [C-NN] slot completion
a gate condition at note-writing time rather than a post-hoc SV finding. STATUS QUO
COMPETITOR uses per-span explicit enumeration via a direct instruction header (C-50 PASS,
C-52 FAIL — per-span instruction present, no SPAN DEFINITION pre-step format block). All
other R19 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain Phase 8.5 notes that follow the FORMAT TEMPLATE verbatim with the [C-NN] slot populated by a specific criterion ID, because the co-located NOTE-COMPLETION STOP blocks note completion until the slot is filled — a builder cannot produce a compliant note without the co-located STOP triggering if the bracket remains; any output where a note retains an unfilled [C-NN] bracket demonstrates the co-located STOP gate is non-functional and falsifies C-51. | The co-located NOTE-COMPLETION STOP is structurally distinct from the section-level SLOT CHECK in V-02: the per-note STOP fires at note-completion time, preventing the builder from advancing to the next note; the section-level SLOT CHECK fires after both notes are written, allowing a builder to write both notes with unfilled brackets before hitting the gate; V-01 outputs should show higher [C-NN] slot completion rates than V-02 if co-location is load-bearing for C-51. | V-02 is the C-51 ablation control: V-02 has FORMAT TEMPLATE (C-49 PASS) with section-level SLOT CHECK (C-51 FAIL) and SPAN DEFINITION pre-step (C-52 PASS); comparing Phase 8.5 slot-population rates across V-01 (co-located STOP, C-51 probe) and V-02 (section-level STOP, C-51 FAIL) isolates whether co-location is load-bearing; prediction: V-01 passes C-51, V-02 fails C-51. |

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

**STOP — NOTE-COMPLETION GATE:** Do not write the next path note or proceed past this point
until the [C-NN] slot in the note above names a specific criterion ID. An unfilled bracket
`[C-NN]` is a visible structural defect detectable by string scan without reading surrounding
prose. A note of the form "Absent this path, the evaluability requirement would pass
unchallenged" is also non-compliant — it omits the criterion ID, making the claim
unverifiable by ID lookup. Both forms block note completion. The compliant form: "Absent
this path, C-43 is unenforced at Phase 9 entry."

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
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

**Axis:** Inertia framing — the STATUS QUO COMPETITOR block is restructured with a SPAN
DEFINITION pre-step immediately before each foil item. The SPAN DEFINITION declares the
span bounds explicitly, and the foil item is written from the SPAN DEFINITION's pass-side
list. This is the C-52 probe: span completeness is structurally pre-declared in the SPAN
DEFINITION block, making completeness verifiable from the pre-step alone without reading the
foil item. Phase 8.5 uses the FORMAT TEMPLATE with [C-NN] slot (C-49 PASS) but the STOP
condition for the [C-NN] slot is placed at the end of Phase 8.5 as a section-level SLOT
CHECK — not co-located per note (C-51 FAIL). All other R19 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain STATUS QUO foil items preceded by a SPAN DEFINITION block with all three required fields (Previous failure, Current failure, Pass side), from which the foil item text is transcribed verbatim — e.g., SPAN DEFINITION names Pass side as "C-04, C-05" and the foil item reads "passes C-04 and C-05 while failing C-06"; any output where foil items lack a preceding SPAN DEFINITION or where the foil item's pass side diverges from the SPAN DEFINITION falsifies the C-52 hypothesis. | The SPAN DEFINITION converts span-completeness from a quality property of the foil item text to a structural property of the pre-step output: a reviewer checking C-52 can read the SPAN DEFINITION alone to verify pass-side completeness, without reading surrounding foil items; this is structurally distinct from C-50 (which only requires completeness in the foil item) and from V-01 (which uses a direct span-enumeration instruction without the pre-step format). | V-01 is the primary C-52 ablation control: V-01 has co-located STOP (C-51 PASS) with per-span direct instruction and no SPAN DEFINITION blocks (C-52 FAIL); comparing STATUS QUO foil item structure across V-02 (SPAN DEFINITION pre-step) and V-01 (direct instruction) isolates whether the SPAN DEFINITION block is load-bearing for C-52; prediction: V-02 passes C-52, V-01 fails C-52. |

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
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

The [C-NN] slot must be populated with a specific criterion ID in each note. A note
describing the gap in prose without naming a criterion ID — e.g., "Absent this path, the
evaluability requirement would pass unchallenged" — does not satisfy the template because
the criterion-indexed claim is absent and cannot be verified by ID lookup.

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP: if Architecture B label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

NON-REDUNDANCY DECLARATION: Architecture A leaves C-43 unenforced at emit entry;
Architecture B leaves C-44 unenforced at pre-emit entry. Both enforcement points are
independently necessary. Neither can substitute for the other.

**PHASE 8.5 SLOT CHECK:** After writing both path notes above, scan each note for an
unfilled `[C-NN]` bracket. STOP if any bracket remains unfilled — return to the note and
fill the slot with the criterion ID before proceeding to ROLE: EVALUABILITY AUDITOR.

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

**Axis:** Output format — Phase 8.5 is restructured so each path note is followed
immediately by a NOTE-COMPLETION GATE named artifact block (rather than an inline prose
STOP). The NOTE-COMPLETION GATE is a two-field structured block that must show YES in both
fields before the builder may advance to the next path note or to NON-REDUNDANCY
DECLARATION. This converts the co-located gate from a prose STOP instruction to a named
structural artifact: a reviewer can detect gate violations by looking for NOTE-COMPLETION
GATE blocks with NO fields, independently of reading the note prose. SPAN DEFINITION
pre-step present in STATUS QUO (C-52 PASS). Tests whether a named-artifact gate structure
satisfies C-51's "co-located STOP blocking note completion" requirement, or whether C-51
requires a literal inline prose STOP statement.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-03 will contain Phase 8.5 notes followed by NOTE-COMPLETION GATE artifacts with YES in both fields — [C-NN] slot populated and Architecture label resolved — before any subsequent path note or NON-REDUNDANCY DECLARATION is written; a rubric output where a NOTE-COMPLETION GATE shows NO in either field and subsequent content is present anyway demonstrates gate non-compliance and falsifies the V-03 C-51 hypothesis. | The NOTE-COMPLETION GATE named artifact is structurally distinct from V-01's inline STOP: it produces an independent section heading and two-field table that can be scanned without reading the note prose; V-01's inline STOP is detectable only by reading the instruction text; both purport to satisfy C-51's co-located blocking requirement, but the named artifact produces an independently-scannable gate state; if V-03 passes C-51, co-location is architecture-neutral; if V-03 fails C-51, the requirement is specifically for inline prose STOP co-located with the FORMAT TEMPLATE declaration. | V-01 is the primary comparison for V-03: V-01 uses inline prose STOP per note, V-03 uses NOTE-COMPLETION GATE artifact; prediction: V-03 passes C-51 because the NOTE-COMPLETION GATE blocks note completion regardless of form; the named-artifact format may additionally surface as a C-53 candidate if it yields higher defect-detection specificity than prose STOP. |

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
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

Immediately after writing each note, produce the following **NOTE-COMPLETION GATE** artifact
for that path. Do not write the next path note or advance to NON-REDUNDANCY DECLARATION
until the NOTE-COMPLETION GATE for the current path shows YES in both fields.

```
NOTE-COMPLETION GATE — Path [N]:
  [C-NN] slot populated with specific criterion ID: [YES / NO — STOP if NO, fill slot above]
  Architecture label resolved in EVALUABILITY ARCHITECTURE COMPETITOR: [YES / NO — STOP if NO]
```

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`

  NOTE-COMPLETION GATE — Path 2:
  ```
  [C-NN] slot populated with specific criterion ID: [YES / NO — STOP if NO]
  Architecture label resolved in EVALUABILITY ARCHITECTURE COMPETITOR: [YES / NO — STOP if NO]
  ```

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`

  NOTE-COMPLETION GATE — Path 1:
  ```
  [C-NN] slot populated with specific criterion ID: [YES / NO — STOP if NO]
  Architecture label resolved in EVALUABILITY ARCHITECTURE COMPETITOR: [YES / NO — STOP if NO]
  ```

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

**Axis:** Combined — Phase 8.5 uses FORMAT TEMPLATE with co-located inline STOP per note
(V-01 C-51 mechanism) AND STATUS QUO COMPETITOR uses SPAN DEFINITION pre-step before each
foil item (V-02 C-52 mechanism). Tests whether C-51 and C-52 are jointly satisfiable without
interference. The two mechanisms govern structurally and positionally distinct sections:
the co-located STOP operates in Phase 8.5 at each note-completion boundary; the SPAN
DEFINITION pre-step operates in the STATUS QUO COMPETITOR at each foil-item construction
boundary. All other R19 V-04 mechanisms preserved.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-04 will contain both (a) Phase 8.5 notes with co-located STOP per note — [C-NN] slot populated, NOTE-COMPLETION GATE per note satisfied — and (b) STATUS QUO foil items preceded by SPAN DEFINITION blocks with all three fields (Previous failure, Current failure, Pass side) — foil items transcribed from SPAN DEFINITION; any output missing either mechanism falsifies the joint-satisfiability hypothesis. | The two mechanisms are orthogonal: co-located STOP operates on Phase 8.5 note production; SPAN DEFINITION pre-step operates on STATUS QUO foil-item production; since the sections are structurally and positionally independent, interference is not expected; V-04 outputs should show both C-51 and C-52 passing at rates comparable to the single-axis variations. | V-01 (co-located STOP, no SPAN DEFINITION) and V-02 (SPAN DEFINITION, no co-located STOP) are the independent single-axis controls; if V-04 passes both C-51 and C-52, joint satisfiability is confirmed; prediction: V-04 passes both, establishing the joint ceiling baseline for R20. |

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
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

**STOP — NOTE-COMPLETION GATE:** Do not write the next path note or proceed past this point
until the [C-NN] slot in the note above names a specific criterion ID. An unfilled bracket
`[C-NN]` is a visible structural defect detectable by string scan without reading surrounding
prose. A note of the form "Absent this path, the evaluability requirement would pass
unchallenged" is also non-compliant — it omits the criterion ID, making the claim
unverifiable by ID lookup. Both forms block note completion. The compliant form: "Absent
this path, C-43 is unenforced at Phase 9 entry."

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
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

**Axis:** Combined + Phrasing register — V-04 mechanisms (co-located inline STOP for C-51,
SPAN DEFINITION pre-step for C-52) plus explicit detection-failure consequence naming at
each gate site. In Phase 8.5: the co-located NOTE-COMPLETION STOP additionally names what
detection failure would occur if the gate were bypassed — specifically, that an unfilled
bracket would pass SV scan undetected because SV checks heading patterns, not bracket
population. In STATUS QUO: each SPAN DEFINITION pre-step names its function explicitly
("SPAN DEFINITION — computes pass-side enumeration for the foil item below; the foil item
must transcribe the Pass side list verbatim") and includes a TRANSCRIPTION STOP naming
range notation as a non-compliant form and identifying the span audit mechanism it defeats.
Tests whether naming detection-failure consequences at gate sites adds measurable ceiling
lift beyond V-04's mechanism presence.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-05 will contain both C-51-passing Phase 8.5 notes and C-52-passing STATUS QUO foil items, plus at each gate site the detection-failure consequence named: (a) Phase 8.5 NOTE-COMPLETION STOPs name the specific SV bypass that the gate prevents; (b) SPAN DEFINITION pre-steps name their function and include TRANSCRIPTION STOPs identifying range notation as non-compliant; any output missing either mechanism falsifies the ceiling-form hypothesis. | The detection-failure naming converts gate enforcement from a process requirement to a self-justifying audit claim, making each gate independently interpretable by a reviewer who has not read the surrounding construction protocol; V-05 outputs should score at least as high as V-04 on C-51 and C-52, with higher defect-detection specificity; if V-05 scores above V-04, detection-failure naming adds measurable value; if equivalent, V-04's mechanism presence is the minimal sufficient structure. | V-04 is the primary comparison for V-05: V-04 has co-located STOP and SPAN DEFINITION without detection-failure naming; V-05 adds detection-failure consequence at both sites; the SPAN DEFINITION function label may surface as a C-53 candidate if it yields independently higher C-52 compliance rates; prediction: V-05 passes both C-51 and C-52 at ceiling. |

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

For each failure below, a SPAN DEFINITION precedes the foil item. The SPAN DEFINITION
names its function and the foil item must transcribe the Pass side list verbatim.

**TRANSCRIPTION STOP:** A foil item that uses range notation ("C-04 through C-09") or names
only a subset of the passing criteria in the span is non-compliant — range notation leaves
span completeness unverifiable without counting criteria, and partial enumeration defeats the
precision criterion-lattice locator function of the foil item. The compliant form lists every
criterion from the SPAN DEFINITION's Pass side verbatim. STOP if any foil item deviates from
verbatim transcription of the SPAN DEFINITION's Pass side.

```
SPAN DEFINITION — computes pass-side enumeration for the foil item below:
  Function: enumerate every criterion between Previous failure and Current failure on the
            pass side; foil item must transcribe Pass side verbatim.
  Previous failure: START
  Current failure:  C-03
  Pass side (every criterion in span): C-01, C-02
  TRANSCRIPTION STOP: foil item must list C-01, C-02 — no range notation, no omissions.
```
- Fails to enumerate failure modes before drafting — **passes C-01 and C-02 while failing
  C-03**: essential criteria not grounded in the skill's actual non-negotiable behaviors;
  criteria come from intuition about good output rather than from systematic analysis of
  broken output.

```
SPAN DEFINITION — computes pass-side enumeration for the foil item below:
  Function: enumerate every criterion between Previous failure and Current failure on the
            pass side; foil item must transcribe Pass side verbatim.
  Previous failure: C-03
  Current failure:  C-06
  Pass side (every criterion in span): C-04, C-05
  TRANSCRIPTION STOP: foil item must list C-04, C-05 — no range notation, no omissions.
```
- Fails to produce causal direction templates — **passes C-04 and C-05 while failing C-06**:
  Text fields describe presence of good properties, not consequence of absence; the causal
  direction "Without Y, Z fails" is absent.

```
SPAN DEFINITION — computes pass-side enumeration for the foil item below:
  Function: enumerate every criterion between Previous failure and Current failure on the
            pass side; foil item must transcribe Pass side verbatim.
  Previous failure: C-06
  Current failure:  C-10
  Pass side (every criterion in span): C-07, C-08, C-09
  TRANSCRIPTION STOP: foil item must list C-07, C-08, C-09 — no range notation, no omissions.
```
- Fails to name a reference anchor with Falls-short dimension — **passes C-07, C-08, and
  C-09 while failing C-10**: aspirational gap not anchored against a named baseline;
  inertia test not applicable because no discrimination target exists.

```
SPAN DEFINITION — computes pass-side enumeration for the foil item below:
  Function: enumerate every criterion between Previous failure and Current failure on the
            pass side; foil item must transcribe Pass side verbatim.
  Previous failure: C-10
  Current failure:  C-13
  Pass side (every criterion in span): C-11, C-12
  TRANSCRIPTION STOP: foil item must list C-11, C-12 — no range notation, no omissions.
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
non-redundant enforcement points. Each is independently necessary.

Each enforcement path requires a co-located EVIDENCE QUOTATION GATE note. Apply the
following **PER-NOTE FORMAT TEMPLATE** when writing each note:

```
PER-NOTE FORMAT TEMPLATE:
  [path label] — [structural phase name].
  Absent this path, [C-NN] is unenforced at [gate name] entry.
  Evidence: [quotation from EVALUABILITY ARCHITECTURE COMPETITOR confirming path independence]
```

**STOP — NOTE-COMPLETION GATE:** Do not write the next path note or proceed past this point
until the [C-NN] slot in the note above names a specific criterion ID. An unfilled bracket
`[C-NN]` is a visible structural defect — detectable by string scan without reading
surrounding prose — and would pass Structural Verification unchallenged because SV scans
heading patterns and slot presence, not slot population; the unfilled bracket would reach
the emitted artifact without triggering any SV catch, making criterion-ID omission invisible
at the only automated verification stage. A note describing the gap in prose without a
criterion ID is also non-compliant — the claim is unverifiable by ID lookup and would pass
SV because prose descriptions have no checkable format. Both forms would reach Phase 9
undetected without this gate. The compliant form: "Absent this path, C-43 is unenforced at
Phase 9 entry."

- Architecture A path note (apply template):
  `enforcement path 2 — emit gate. Absent this path, C-43 is unenforced at Phase 9 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
  Detection-failure consequence if bypassed: unfilled [C-NN] bracket passes SV scan and
  reaches Phase 9 emitted artifact; criterion-ID omission undetected at all verification
  stages.
  STOP: if Architecture A label does not resolve in EVALUABILITY ARCHITECTURE COMPETITOR.

- Architecture B path note (apply template):
  `enforcement path 1 — pre-emit gate. Absent this path, C-44 is unenforced at Phase 8 entry.`
  STOP — NOTE-COMPLETION GATE: [C-NN] slot populated with specific criterion ID? STOP if not.
  Detection-failure consequence if bypassed: unfilled [C-NN] bracket passes SV scan and
  reaches Phase 9 emitted artifact; criterion-ID omission undetected at all verification
  stages.
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
