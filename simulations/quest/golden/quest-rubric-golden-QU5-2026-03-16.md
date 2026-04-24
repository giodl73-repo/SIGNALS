---
skill: quest-golden
skill_target: quest-rubric
date: 2026-03-15
rounds: 20
rubric_final: quest-rubric-rubric-v21-2026-03-15.md
score: 100
status: GOLDEN
---

# quest-rubric — Golden Prompt (QU5 / SPAN DEFINITION Track)

**Winning variation:** V-05 (Combined + Phrasing Register), simplified 20.1% (QU5)
**Score:** 100/100 on C-01–C-52 (v20 rubric, denominator /44)
**Tied at 100:** V-03 (named-artifact gate), V-04 (combined)
**V-05 preferred:** ceiling form — adds detection-failure consequence naming; simplified form
drops non-load-bearing rationale prose while keeping all gates intact
**Source file:** `simulations/quest/golden/quest-rubric-QU5-simplified-2026-03-16.md`

---

## Prompt Body

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

## What Made It Golden

Four patterns distinguish V-05 (simplified) from the R20 baseline (V-01) and close the
single failing criterion gap (C-52) that held V-01 at 99.77.

### 1. SPAN DEFINITION pre-step blocks (closes C-52)

V-01 used a per-span direct instruction header declaring span completeness as narrative:
*"Each foil item below names every criterion in the span..."* — a prose claim, not a
structured output. V-05 introduces a named `SPAN DEFINITION` block immediately before
each foil item with three required fields:

```
SPAN DEFINITION:
  Previous failure: [C-NN or START]
  Current failure:  [C-NN]
  Pass side (every criterion in span): [C-NN, C-NN, ...]
```

The pre-step converts span completeness from a narrative claim into a verifiable artifact.
A reviewer can scan for `SPAN DEFINITION` blocks, count them against foil items, and check
Pass-side enumeration by ID — without reading surrounding prose.

### 2. TRANSCRIPTION STOP with anti-range-notation rule

V-05 adds a general `TRANSCRIPTION STOP` above all SPAN DEFINITION blocks that bans range
notation ("C-04 through C-09") and partial enumeration. This is independently load-bearing:
range notation is precisely what a builder would use when attempting span completeness from
memory. The STOP closes that bypass route without relying on the builder to apply the SPAN
DEFINITION Pass-side list.

### 3. Foil item content constrained to SPAN DEFINITION Pass-side output

In V-01, foil items stated their pass-side spans inline (e.g., "passes C-01 and C-02").
In V-05, each foil item is explicitly required to *transcribe* the Pass-side list from the
preceding SPAN DEFINITION verbatim. This creates a two-artifact consistency check: SPAN
DEFINITION declares the span; the foil item transcribes it. A discrepancy is string-scannable
without reading surrounding prose.

### 4. Co-located per-note STOP gate (C-51) — inherited from V-01, preserved through simplification

V-01 solved C-51 with inline `STOP — NOTE-COMPLETION GATE` immediately after the PER-NOTE
FORMAT TEMPLATE in Phase 8.5. V-05 preserves this mechanism verbatim. The QU5 simplification
removes the extended SV-bypass rationale (5 sentences, ~92 words) as non-load-bearing while
keeping the operative gate intact: the `STOP if not` form is co-located at note-completion
time, blocking before the next note is written.

---

## Final Rubric Criteria Summary (v21)

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/46 × 10)`
**Denominator:** /46 (C-09 through C-54)
**Golden threshold:** composite >= 99.5

**R20 scoring (v20 rubric, /44):**

| Variation | C-51 | C-52 | Score |
|-----------|------|------|-------|
| V-01 Lifecycle | PASS | FAIL | 99.77 |
| V-02 Inertia | FAIL | PASS | 99.77 |
| V-03 Output format | PASS | PASS | 100.00 |
| V-04 Combined | PASS | PASS | 100.00 |
| V-05 Combined + Phrasing (GOLDEN) | PASS | PASS | 100.00 |

**Key criteria added in R19–R20 (C-49 through C-54):**

| Criterion | Round | What it requires |
|-----------|-------|-----------------|
| C-49 | R19 | Phase 8.5 PER-NOTE FORMAT TEMPLATE contains a `[C-NN]` slot |
| C-50 | R19 | STATUS QUO foil items enumerate full pass-side criteria per span |
| C-51 | R19/R20 | `[C-NN]` slot co-located with a STOP condition blocking Phase 8.5 note completion until slot is filled with a specific criterion ID |
| C-52 | R20 | Each STATUS QUO foil item preceded by a SPAN DEFINITION pre-step with (a) previous failure, (b) current failure, (c) full pass-side enumeration |
| C-53 | v21 (R21 target) | Phase 8.5 STOP gate implemented as a named, independently scannable artifact block — enables heading-search gate-state verification |
| C-54 | v21 (R21 target) | NOTE-COMPLETION GATE block contains separate YES/NO STOP fields for every per-note compliance requirement |

**V-05 on v21 rubric (C-01–C-54, /46):** ~95.65 — C-53/C-54 are R21 ceiling targets.
The V-03 named-artifact gate form (`NOTE-COMPLETION GATE` block with YES/NO fields) is the
R21 probe for C-53/C-54 satisfiability.
