# quest-rubric Variate — Round 2 against rubric v2 (revised)

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05)
**Round:** R2 — 3 single-axis passes + 2 combination passes

**Round 2 design note:** The existing R02 file targeted an intermediate rubric (C-11 =
inertia test, C-12 = calibration example, C-13 = phase-gate). The current rubric v2 defines
them as: C-11 = external enforcement gate (named role / rejection step / prohibition checklist),
C-12 = failure-first derivation (failure catalog before criteria; criteria traced to named
failures), C-13 = generic-vs-specific foil pair (concrete before/after near C-07). These
variations target the current definitions. The prior R02 file remains valid signal for the
prior rubric state; these variations provide signal against the current objective function.

Axes selected for single-axis: lifecycle-emphasis (→ C-12), output-format (→ C-13),
role-sequence (→ C-11). Combination V-04: lifecycle × role-sequence (→ C-12 + C-11).
Combination V-05: lifecycle × output-format (→ C-12 + C-13). Priority combo: V-04, because
C-12 and C-11 were the two criteria that most consistently failed in prior rounds.

---

## Round 2 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | Phase 0 failure catalog is a hard-gated prerequisite; each criterion must cite a parent failure by F-NN code; uncited criteria are rejected as generic | C-12 |
| V-02 | output-format | single-axis | Essential criteria table gains mandatory `Foil Pair` column requiring a GENERIC/SPECIFIC pair per row; empty cell is a table-completion failure | C-13 |
| V-03 | role-sequence | single-axis | Discriminator role runs before Author, producing a Discrimination Surface and a Rejection Checklist; Author's pass conditions are vetoed if they fail any checklist item | C-11 |
| V-04 | lifecycle-emphasis × role-sequence | combination (Priority 1) | Phase 0 failure catalog feeds the Discriminator's Rejection Checklist; Discriminator cannot approve a criterion whose pass condition is generic AND that cites no parent failure | C-12, C-11 |
| V-05 | lifecycle-emphasis × output-format | combination (Priority 2) | Phase 0 failure catalog + mandatory Foil Pair column; the F-NN trace in each row makes the SPECIFIC cell easier to write by making the failure mode visible | C-12, C-13 |

**Anchor designation (C-12 of the quest-variate rubric):** V-01. See anchor section at end.

---

## V-01 — Lifecycle Emphasis: Phase 0 Failure Catalog with Traceability Gate

**axis:** lifecycle-emphasis
**hypothesis:** Making the failure catalog a hard-gated Phase 0 — before any criterion is
written — and requiring each essential criterion to cite a parent failure by F-NN code
increases C-12 pass rates because traceability forces the builder to ground criteria in
specific, named failures rather than abstract quality properties. A criterion that cannot cite
a parent failure reveals itself as generic by the absence of a link: there is no failure mode
in the catalog it is addressing. The gate at Phase 0 prevents criteria from being written
until failures are enumerated, so the derivation order is architecturally enforced, not
stylistically requested. Failure condition: if C-12 pass rates do not improve relative to
variations without Phase 0 gating, the traceability requirement adds no protective value over
a prose instruction to "derive criteria from failure modes."

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable two independent evaluators to reach the same pass/fail verdict
for any skill output, without discussion.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence
   of quality.

**PHASE 0: FAILURE CATALOG**

Before writing any criterion, catalog the specific ways this skill's output can fail to
function as intended. A failure mode is a specific, detectable condition — not a quality
gradient.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Rules for failure modes:

- Blocking: the output cannot function as intended if this failure is present. Evaluators
  would flag the output as invalid, not merely weak.
- Degrading: the output functions but with reduced signal value. Evaluators would flag for
  improvement, not invalidity.
- Each failure mode must name a specific, detectable condition — not "quality is low" or
  "output is incomplete." A failure mode is specific when an evaluator can determine from
  the output alone whether the condition is present.

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 1 until the failure catalog has at least 3 blocking entries and
2 degrading entries.**

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

Write 3-5 essential criteria. Each criterion requires six fields:

| ID | Criterion | Category | Weight | Pass Condition | Addresses |
|----|-----------|----------|--------|----------------|-----------|

Field rules:

- **ID**: C-NN (sequential)
- **Criterion**: Bold label + one-sentence description of the property being evaluated
- **Category**: one of: correctness / depth / format / coverage / behavior
- **Weight**: essential
- **Pass Condition**: a specific, observable outcome — what an evaluator would look for and
  what constitutes a pass
- **Addresses**: the F-NN code(s) from Phase 0 that this criterion detects or prevents

A criterion with no `Addresses` entry is a generic criterion: it is not derived from any
named failure in this skill's catalog. Generic criteria are not permitted in the essential
tier. Either trace the criterion to a Phase 0 failure or do not include it.

A criterion that addresses multiple failures may list all of them: `F-01, F-03`.

**PHASE 2: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Same six-field format including `Addresses` column.

If a recommended criterion cannot trace to a Phase 0 failure, document why it is included
despite having no blocking parent (e.g., it represents an excellence pattern beyond failure
prevention, not a basic validity requirement).

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field format (Addresses column optional).

**PHASE 4: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 5: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-02 — Output Format: Mandatory Foil Pair Column in Essential Criteria Table

**axis:** output-format
**hypothesis:** Adding a required `Foil Pair` column to the essential criteria table forces
a GENERIC/SPECIFIC contrast pair at authoring time for every essential criterion, because an
empty cell is a visible structural failure rather than an omission-by-neglect. The foil pair
satisfies C-13 (generic-vs-specific foil pair near C-07) by making the contrast embedded in
the rubric artifact itself — not as a prose annotation separate from the criteria table. When
the table schema demands the pair, the author cannot complete a row without writing both the
generic formulation and the specific replacement. Failure condition: if C-13 pass rates do
not improve relative to variations using standard five-column tables, the schema-embedded
column adds no compliance benefit over a prose instruction to "include a contrast example."

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden: it must enable systematic scoring across all variations of the target skill.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 2 until this minimum is met.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Use the extended table format for essential criteria. The `Foil Pair` column is required — an
empty cell is a criterion completion failure and blocks the rubric from being finalized.

| ID | Criterion | Category | Weight | Pass Condition | Foil Pair |
|----|-----------|----------|--------|----------------|-----------|

The `Foil Pair` column must contain a **GENERIC/SPECIFIC pair** for each row:

```
GENERIC: [a pass condition formulation applicable to any skill output regardless of which
          skill produced it — could appear in a rubric for any artifact]
SPECIFIC: [a pass condition formulation naming this skill's output contract — a count,
           field name, structural element, or enumeration that only this skill supplies]
```

Requirements for the SPECIFIC entry:

- Must name at least one term from this skill's output contract that does NOT appear in the
  GENERIC entry
- Must not be movable unchanged to a rubric for a different skill — if it can, it is not
  specific enough; revise until it names a skill-owned term
- The term that makes it specific may be: a count (e.g., "at least 3 blocking entries"),
  a named field (e.g., "Pass Condition field"), a structural pattern (e.g., "six-column
  table"), or a closed enumeration (e.g., "essential / recommended / aspirational")

The GENERIC entry serves as the contrast case: it shows what the SPECIFIC entry replaced.
Both entries must reference the target skill by name or by a term from its output contract.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Standard five-column table (no Foil Pair required):

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Standard five-column table.

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Role Sequence: Discriminator Role Produces Rejection Checklist Before Author Writes

**axis:** role-sequence
**hypothesis:** Running a Discriminator role before the Author — where the Discriminator's
sole output is a Discrimination Surface (the counts, field names, structural patterns, and
enumerations that only this skill's contract defines) plus a Rejection Checklist (explicit
prohibition conditions, not advisory suggestions) — addresses C-11 (external enforcement
gate) because the rejection step is structural, named, and runs before finalization rather
than as a post-hoc quality review. The key distinction from advisory language: the Rejection
Checklist contains items that are checked TRUE/FALSE; an Author pass condition that hits any
checklist item is rejected regardless of how well-written it otherwise appears. Failure
condition: if C-11 pass rates do not improve relative to variations using only prose
instructions ("write discriminating pass conditions"), the role-based rejection step provides
no structural enforcement advantage over advisory instruction alone.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence.
Discriminator runs first and defines the rejection surface. Author writes criteria and
submits each pass condition to the Rejection Checklist before finalizing.

--- ROLE: DISCRIMINATOR ---

Read the skill spec. Your output is two artifacts: the Discrimination Surface and the
Rejection Checklist. These artifacts are produced before any criteria are written.

**Discrimination Surface**

Catalog every element of this skill's output contract that a pass condition may reference
to become skill-specific rather than generic:

```
DISCRIMINATION SURFACE — {skill name}

Counts:
  - [element name]: [minimum / exact / maximum as stated in spec]
  [one line per count]

Named fields:
  - [field name]: [what it contains, per spec]
  [one line per named field]

Structural patterns:
  - [pattern name]: [required shape — e.g., "table with N columns", "header with M fields"]
  [one line per pattern]

Enumerations:
  - [enumeration name]: [closed set of values — e.g., "essential / recommended / aspirational"]
  [one line per enumeration]
```

A pass condition is skill-specific when it names at least one element from this Discrimination
Surface. A pass condition is generic when it names no element from this Surface — even if it
is well-written, grammatically clear, and appears to describe quality.

**Rejection Checklist**

A pass condition is rejected if any of the following items are TRUE:

```
REJECTION CHECKLIST

[ ] The condition names no element from the Discrimination Surface above.
[ ] The condition uses only quality-adjacent language with no counts or field names:
    ("clear", "comprehensive", "well-formed", "high quality", "appropriate").
[ ] The condition could be moved unchanged into a rubric for a different skill
    without modification.
[ ] The condition names a structural element present in all Markdown documents
    (e.g., "has headers", "has a table", "is formatted").
[ ] The condition requires subjective judgment to evaluate — two evaluators would
    need discussion to reach the same pass/fail verdict.
```

--- END DISCRIMINATOR ---

--- ROLE: AUTHOR ---

Read the Discrimination Surface and Rejection Checklist above before writing.

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 2 until this minimum is met.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Write each essential criterion. After drafting the pass condition, apply the Rejection
Checklist:

- For each checklist item: mark TRUE or FALSE.
- If any item is TRUE: the pass condition is rejected. Revise to name a specific element
  from the Discrimination Surface. Re-apply the checklist until all items are FALSE.
- If all items are FALSE: the pass condition is approved. Proceed.

Record the Rejection Checklist result inline before recording the criterion in the table:

`[Rejection Checklist: all FALSE — pass condition names {element from Discrimination Surface}]`

After the inline record, add the criterion to the table:

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Apply the Rejection Checklist to each pass condition
(internally — do not document the checklist result inline).

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field table format.

--- END AUTHOR ---

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-04 — Lifecycle Emphasis × Role Sequence: Failure Catalog Feeds Discriminator (Priority Combo)

**axis:** lifecycle-emphasis × role-sequence
**hypothesis:** Combining Phase 0 failure catalog (V-01 mechanism) with Discriminator role
enforcement (V-03 mechanism) addresses C-12 and C-11 simultaneously through non-redundant
paths: the failure catalog prevents generic criteria by requiring traceability (C-12), and the
Discriminator's Rejection Checklist prevents generic pass conditions by applying a named
rejection step (C-11). The interaction hypothesis is additive, not redundant: a criterion can
pass the failure trace check (citing F-01) while its pass condition still fails the Rejection
Checklist (the condition is generic even though the criterion addresses a real failure). Both
gates are needed because they check different things — the failure trace checks the criterion's
motivation, the Rejection Checklist checks the pass condition's specificity. If the combination
does not produce higher C-12 + C-11 joint pass rates than either V-01 or V-03 alone, the gates
are redundant (one subsumes the other) and the combination adds no coverage beyond the
stronger single-axis variation.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence, with a
required failure catalog preceding both. Phase 0 produces the failure catalog. Discriminator
extends Phase 0 into the Rejection Checklist. Author writes criteria grounded in both.

**PHASE 0: FAILURE CATALOG**

Read the skill spec. Before any roles engage, catalog failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed until this minimum is met.**

--- ROLE: DISCRIMINATOR ---

Read the failure catalog above and the skill spec.

**Step D-1: Produce the Discrimination Surface**

Catalog every element of this skill's output contract that makes a pass condition
skill-specific:

```
DISCRIMINATION SURFACE — {skill name}

Counts:
  [one line per count — minimum, exact, or maximum values from spec]

Named fields:
  [one line per required field — field name and its content type]

Structural patterns:
  [one line per required structural shape]

Enumerations:
  [one line per closed-set value list]
```

**Step D-2: Produce the Rejection Checklist**

A pass condition is rejected if any of the following items are TRUE:

```
REJECTION CHECKLIST

[ ] The condition names no element from the Discrimination Surface.
[ ] The condition uses only quality-adjacent language with no counts or field names.
[ ] The condition could apply unchanged to a rubric for a different skill.
[ ] The condition names only structural elements present in all Markdown documents.
[ ] The condition requires discussion between evaluators to reach pass/fail verdict.
```

**Step D-3: Extend the Rejection Checklist with failure-trace requirement**

Add one item to the Rejection Checklist:

```
[ ] The criterion cites no parent failure from the Phase 0 catalog (Addresses: F-NN
    is absent or the cited failure is not in the catalog).
```

This item ensures the Rejection Checklist enforces both pass condition specificity (Steps D-1
and D-2) and criterion derivation from named failures (Step D-3). A criterion that fails
either check is rejected.

--- END DISCRIMINATOR ---

--- ROLE: AUTHOR ---

Read the Phase 0 failure catalog, the Discrimination Surface, and the Rejection Checklist
(including the Step D-3 extension) before writing.

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

Write each essential criterion. Each requires six fields:

| ID | Criterion | Category | Weight | Pass Condition | Addresses |
|----|-----------|----------|--------|----------------|-----------|

After drafting each criterion, apply the full Rejection Checklist (including Step D-3):

- If any item is TRUE: the criterion is rejected. Revise the pass condition and/or add the
  missing failure trace. Re-apply the checklist until all items are FALSE.
- If all items are FALSE: the criterion is approved.

Record the checklist result inline:
`[Rejection Checklist: all FALSE — addresses F-NN; pass condition names {element}]`

**PHASE 2: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Six-field format. Apply Rejection Checklist internally.

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field format.

--- END AUTHOR ---

**PHASE 4: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 5: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-05 — Lifecycle Emphasis × Output Format: Failure Catalog + Foil Pair Column

**axis:** lifecycle-emphasis × output-format
**hypothesis:** Combining Phase 0 failure catalog (V-01 mechanism) with the mandatory Foil
Pair column (V-02 mechanism) addresses C-12 and C-13 through a positive interaction: the
failure catalog makes the SPECIFIC cell of the foil pair easier to write because the builder
already knows what failure the criterion addresses, and what a failure-specific pass condition
looks like for that failure. Without the failure catalog, the builder must derive the SPECIFIC
example from the spec alone. With the failure catalog, the builder has a named failure mode as
a concrete anchor — the SPECIFIC cell describes what an evaluator would look for to detect
that named failure, while the GENERIC cell shows the non-specific version that would miss it.
Failure condition: if SPECIFIC cell quality (assessed by whether the entry names a Discrimination
Surface element) does not improve over V-02 alone, the failure catalog provides no anchoring
benefit for the foil pair and the combination is not additive.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 0: FAILURE CATALOG**

Before writing any criterion:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Each failure mode must be a specific, detectable condition — not a quality gradient.
A failure mode is specific when an evaluator can determine from the output alone whether
the condition is present.

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 1 until this minimum is met.**

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

Use the extended table format. The `Foil Pair` column is required. An empty cell in
`Foil Pair` is a table-completion failure.

| ID | Criterion | Category | Weight | Pass Condition | Addresses | Foil Pair |
|----|-----------|----------|--------|----------------|-----------|-----------|

Column rules:

- **Addresses**: the F-NN code(s) from Phase 0 that this criterion detects. A criterion
  with no Addresses entry is generic — trace it to a failure or remove it.

- **Foil Pair**: a GENERIC/SPECIFIC pair using this format:
  ```
  GENERIC: [pass condition that could apply to any artifact — the non-specific version
            that would pass the criterion even for an output that fails this failure mode]
  SPECIFIC: [pass condition naming this skill's output contract element — count, field name,
             structural pattern, or enumeration — that directly detects the failure in F-NN]
  ```

  The SPECIFIC entry should be writable by answering: "What would an evaluator look at to
  determine whether the F-NN failure is present in this output?" The answer to that question
  is the SPECIFIC pass condition. The GENERIC version is the same criterion without the
  named observable.

**PHASE 2: RECOMMENDED CRITERIA (2-3)**

Standard five-column table (no Foil Pair or Addresses required):

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)**

Standard five-column table.

**PHASE 4: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 5: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## Anchor Designation

**Anchor: V-01**

V-01 is designated the combination anchor for all Round 3 combination runs involving C-12.

**Structural impact**: V-01's Phase 0 gate produces a named failure catalog that subsequent
phases must reference. The `Addresses: F-NN` column in the essential criteria table creates
a machine-checkable traceability link: if the column is empty, the criterion is structurally
incomplete regardless of how well-written its pass condition appears. This makes the C-12
test (failure-first derivation) a format check, not a quality judgment — an auditor can
verify compliance by inspecting the Addresses column without evaluating the criterion's prose.

**Isolation quality**: Only lifecycle structure is modified. The phase sequence changes from
Phase 1→2→3 to Phase 0→1→2→3. The content of each phase is identical to baseline variants.
The Addresses column is the only new table field. Any co-variation in combination runs can
be attributed to the Phase 0 gate or the Addresses column, not to other changes.

**Detectable failure condition**: If a builder skips Phase 0, the essential criteria table
will have no Addresses column (or will have empty Addresses cells). This is visible as a
structural gap, not as degraded quality — making the failure mode mechanical and auditable.
If a builder writes Phase 0 but populates the Addresses column with non-existent failure
codes (e.g., "F-01" when Phase 0 lists only 2 entries), the traceability link is broken
and detectable by cross-reference.

**Combination priority**:

1. **V-04 (V-01 × V-03)** — highest priority. V-01 gates criteria derivation; V-03 gates
   pass condition specificity. The two checks are non-redundant (one checks criterion
   motivation, the other checks pass condition vocabulary). If V-04 shows additive improvement
   over both V-01 and V-03, the combination is the Round 3 candidate.
2. **V-05 (V-01 × V-02)** — second priority. V-01 failure catalog provides anchor for V-02
   foil pairs; the SPECIFIC cell quality hypothesis is testable. If SPECIFIC cells in V-05
   runs cite failure modes from Phase 0, the anchoring effect is confirmed.
