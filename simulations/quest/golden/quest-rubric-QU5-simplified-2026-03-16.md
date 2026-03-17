# quest-rubric QU5 Simplified Prompt
**Date:** 2026-03-16
**Source:** V-05 from quest-rubric-variate-v20-R20-2026-03-16.md
**Original word count (V-05 prompt body):** 2900
**Simplified word count:** 2316
**Reduction:** 20.1%
**All essential criteria preserved:** YES

---

## Simplified Prompt Body

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach: read the spec, draft criteria by editorial judgment,
write pass conditions on the fly, state a composite formula, add aspirational criteria as
afterthought.

**What it does not do:**

For each failure below, a SPAN DEFINITION precedes the foil item. The foil item must
transcribe the Pass side list verbatim.

**TRANSCRIPTION STOP:** A foil item using range notation ("C-04 through C-09") or naming
only a subset of passing criteria is non-compliant — range notation leaves span completeness
unverifiable, and partial enumeration defeats the criterion-lattice locator function. STOP
if any foil item deviates from verbatim transcription of the SPAN DEFINITION's Pass side.

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

Causal direction rule: "Without Y, Z fails" is the required form.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

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
> have different majority categories. From the description above, derive what the
> category-distribution divergence check must verify before reading the check below.

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
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### ROLE: MECHANISM DEFINER

**PREREQUISITE: REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE:
MECHANISM DEFINER as blocked consumer).**

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes — affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes — affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### PHASE 5.5 — BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes — affects C-NN only," and PHASE-LOCALITY RULE stated.**

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

Architecture A (gate-only): A skill prompt with ROLE: EVALUABILITY AUDITOR but without a
Phase 9 terminal Criterion Evaluability Map. Fails C-43: terminal evaluability section
absent from emitted artifact.

Architecture B (terminal-table-only): A skill prompt with a Phase 9 terminal Criterion
Evaluability Map but without ROLE: EVALUABILITY AUDITOR as a pre-Phase-9 gate. Fails C-44:
Independence declarations never independently verified pre-emit; generic claims pass through
undetected.

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
until the [C-NN] slot in the note above names a specific criterion ID. An unfilled `[C-NN]`
bracket is a visible structural defect detectable by string scan without reading surrounding
prose. A note describing the gap without a criterion ID is also non-compliant — the claim
is unverifiable by ID lookup. The compliant form: "Absent this path, C-43 is unenforced at
Phase 9 entry."

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

## Simplification Report

### What was removed and why

| # | Location | Removed | ~Words | Why |
|---|----------|---------|--------|-----|
| 1 | STATUS QUO opening | 5-step numbered list replaced with 1-sentence summary | 42 | The derivation instruction needs a description to derive from, but the foil items carry the load; the 5-step list is framing only |
| 2 | STATUS QUO | "This approach produces a rubric. It may be directionally correct. It may pass a basic completeness check." | 28 | Pure padding; no failure content |
| 3 | SPAN DEFINITION blocks (4x) | `Function:` label line in each block | 48 | Stated in preamble ("The SPAN DEFINITION names its function and the foil item must transcribe..."); 4 repetitions add zero information |
| 4 | SPAN DEFINITION blocks (4x) | `TRANSCRIPTION STOP: foil item must list C-XX, C-YY...` line in each block | 48 | Covered by the general TRANSCRIPTION STOP paragraph above all blocks; per-block repetition is redundant |
| 5 | SPAN DEFINITION block headers (4x) | `— computes pass-side enumeration for the foil item below:` subtitle | 32 | The Function label already expressed this; stripping the subtitle is consistent with removing it |
| 6 | ROLE: CRITERION DEFINER | "This role runs after Phase 1. Do not write any criterion fields during this role." | 18 | Sequencing implied by phase structure; the gate header enforces the output constraint |
| 7 | ROLE: CRITERION DEFINER | "DEFINER OUTPUT GATE is satisfied when: Both templates above are produced in slot-fillable form. Nothing else. A CRITERION DEFINER output containing any content other than the two slot-fillable templates is incomplete." | 38 | Gate header already states this; STOP CONDITION is the operative enforcement; three sentences restating the gate condition are redundant |
| 8 | PHASE 4 | `PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.` header | 15 | Phase 3 carries this prerequisite; builders applying Phase 4 have already read Phase 3's prerequisite; a reminder adds words without changing compliance |
| 9 | PHASE 5 | "The Falls-short dimension defines the aspirational gap that the Mechanism Definer's independence map must cover." | 20 | Restates what the Consumer field already says within the REFERENCE ANCHOR block |
| 10 | ROLE: MECHANISM DEFINER | `**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER as the blocked consumer).` | 25 | Restates Phase 5's Consumer field; the PREREQUISITE header I replaced it with is shorter and sufficient |
| 11 | ROLE: MECHANISM DEFINER | "Produces independence map for anticipated aspirational gaps." | 8 | Obvious from role name and format block below |
| 12 | ROLE: BUILDER ASPIRATIONAL | "This role's entry is gated on both ROLE identifiers above. If either gate has not been satisfied, this role cannot begin." | 26 | Redundant with the two PREREQUISITE headers immediately above it |
| 13 | TIER-BLIND CATEGORIZER | Last 2 illustrative sentences: "A rubric where essential criteria are predominantly 'correctness' and aspirational criteria are also predominantly 'correctness' passes the standard audit. The tier convergence is invisible to the standard check." | 44 | Examples illustrating the derivation target; the derivation instruction ("From the description above, derive...") covers the gap without needing illustration |
| 14 | EVALUABILITY ARCHITECTURE COMPETITOR | Architecture A and B verbose explanations condensed | 55 | Reasoning prose removed; load-bearing elements kept: architecture name, failure mode type (gate-only / terminal-only), criterion ID that fails (C-43/C-44), one-sentence failure reason |
| 15 | PHASE 8.5 STOP block | Extended SV-bypass explanation (5 sentences beginning "An unfilled bracket [C-NN] is a visible structural defect — detectable by string scan...and would pass Structural Verification unchallenged because SV scans heading patterns...") | 92 | V-05's ceiling-form addition explaining the detection-failure mechanism; C-51 requires co-located STOP blocking note completion, not the SV-bypass rationale; the gate itself is what satisfies C-51 |
| 16 | PHASE 8.5 Architecture A note | "Detection-failure consequence if bypassed: unfilled [C-NN] bracket passes SV scan and reaches Phase 9 emitted artifact; criterion-ID omission undetected at all verification stages." | 28 | V-05 ceiling form; the co-located STOP NOTE-COMPLETION GATE is the operative C-51 mechanism; the consequence description is rationale |
| 17 | PHASE 8.5 Architecture B note | Same detection-failure consequence paragraph | 28 | Same reason as #16 |

**Total removed: ~584 words**

### Criteria verification

| Criterion | Mechanism in simplified prompt | PASS? |
|-----------|-------------------------------|-------|
| C-51 — co-located STOP gate per note | `STOP — NOTE-COMPLETION GATE:` present immediately after PER-NOTE FORMAT TEMPLATE instruction, co-located with per-note instruction, blocks note completion until [C-NN] filled | YES |
| C-52 — SPAN DEFINITION pre-step | 4× SPAN DEFINITION blocks with Previous failure / Current failure / Pass side fields, each immediately before a foil item | YES |
| C-49 — FORMAT TEMPLATE [C-NN] slot | PER-NOTE FORMAT TEMPLATE with `[C-NN]` slot present in Phase 8.5 | YES |
| C-50 — per-span full enumeration | SPAN DEFINITION Pass side lists all criteria verbatim; TRANSCRIPTION STOP enforces verbatim transcription | YES |
| C-43/C-44 — dual evaluability paths | EVALUABILITY ARCHITECTURE COMPETITOR preserved (condensed but both criteria cited); Phase 8.5 NON-REDUNDANCY DECLARATION preserved | YES |
| C-48 — TIER-BLIND CATEGORIZER competitor | TIER-BLIND CATEGORIZER foil with derivation instruction preserved (2 illustrative trailing sentences removed, not the competitor itself) | YES |
| All earlier criteria C-01–C-42 | All phases (1, 3, 4, 4.5, 5, ROLES, 6.75, 7, 8, 8.5, 9) intact; no structural sections removed | YES |
