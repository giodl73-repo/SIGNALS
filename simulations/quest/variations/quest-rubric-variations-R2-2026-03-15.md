---

## quest-rubric Variate — Round 2 (revised against current rubric v2)

**Date:** 2026-03-15 | **Skill:** quest-rubric | **Rubric:** v2 (C-01–C-13) | **Round:** R2

**Note on existing R02 file:** The prior `quest-rubric-variate-v2-R02-2026-03-15.md` targeted
an intermediate rubric (C-11 = inertia test, C-12 = calibration example, C-13 = phase-gate).
The current rubric v2 defines them differently. These variations target the current definitions.

---

### Round 2 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | Phase 0 failure catalog is a hard-gated prerequisite; each essential criterion must cite a parent failure by F-NN; uncited criteria are rejected as generic | C-12 |
| V-02 | output-format | single-axis | Essential criteria table gains mandatory `Foil Pair` column requiring a GENERIC/SPECIFIC pair per row; empty cell is a table-completion failure | C-13 |
| V-03 | role-sequence | single-axis | Discriminator role runs before Author, producing a Discrimination Surface and Rejection Checklist (TRUE/FALSE checklist items, not advisory language); Author pass conditions vetoed on any TRUE item | C-11 |
| V-04 | lifecycle-emphasis × role-sequence | combination (Priority 1) | Phase 0 failure catalog + Discriminator Rejection Checklist extended with failure-trace requirement; two non-redundant gates target C-12 and C-11 independently | C-12, C-11 |
| V-05 | lifecycle-emphasis × output-format | combination (Priority 2) | Phase 0 failure catalog + mandatory Foil Pair column; F-NN trace anchors the SPECIFIC cell — builder knows which failure the SPECIFIC condition must detect | C-12, C-13 |

**Anchor: V-01.** Phase 0 gate makes C-12 a format check (empty Addresses column = structural failure), not a quality judgment.

---

### V-01 — Lifecycle Emphasis: Phase 0 Failure Catalog with Traceability Gate

**axis:** lifecycle-emphasis
**hypothesis:** Failure catalog as hard-gated Phase 0 + required `Addresses: F-NN` column per criterion. A criterion with no Addresses entry reveals itself as generic by structural absence. The derivation order is architecturally enforced, not stylistically requested.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden: it must enable two independent evaluators to reach the same pass/fail verdict for any skill output, without discussion.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence of quality.

**PHASE 0: FAILURE CATALOG**

Before writing any criterion, catalog the specific ways this skill's output can fail to function as intended. A failure mode is a specific, detectable condition — not a quality gradient.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

- **Blocking**: the output cannot function as intended if this failure is present.
- **Degrading**: the output functions but with reduced signal value.
- Each failure mode must be detectable from the output alone — not a quality gradient.

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 1 until the failure catalog has at least 3 blocking and 2 degrading entries.**

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

Write 3-5 essential criteria with six fields:

| ID | Criterion | Category | Weight | Pass Condition | Addresses |
|----|-----------|----------|--------|----------------|-----------|

- **Addresses**: the F-NN code(s) from Phase 0 this criterion detects or prevents. A criterion with no `Addresses` entry is generic — it is not derived from any named failure. Generic criteria are not permitted in the essential tier. Either trace the criterion to a Phase 0 failure or do not include it.

**PHASE 2: RECOMMENDED CRITERIA (2-3)**

Same six-field format. If a recommended criterion cannot trace to a Phase 0 failure, document why it is included despite having no blocking parent.

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)**

Five-field format (Addresses optional).

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

### V-02 — Output Format: Mandatory Foil Pair Column

**axis:** output-format
**hypothesis:** A required `Foil Pair` column in the essential criteria table makes C-13 (generic-vs-specific foil pair near C-07) a format requirement — an empty cell is a structural failure, not an omission-by-neglect. The author cannot complete a row without writing both the generic formulation and the specific replacement.

---

You are building a scoring rubric for a Signal skill.

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

Minimum: 3 blocking, 2 degrading. **DO NOT proceed until this minimum is met.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Extended table format. The `Foil Pair` column is required — empty cell = criterion completion failure.

| ID | Criterion | Category | Weight | Pass Condition | Foil Pair |
|----|-----------|----------|--------|----------------|-----------|

`Foil Pair` column must contain a **GENERIC/SPECIFIC pair**:

```
GENERIC: [pass condition applicable to any artifact regardless of which skill produced it]
SPECIFIC: [pass condition naming this skill's output contract — a count, field name, structural
           element, or enumeration that only this skill supplies]
```

The SPECIFIC entry must name at least one term from this skill's output contract that does NOT appear in the GENERIC entry. A SPECIFIC entry movable unchanged to a different skill's rubric is not specific enough — revise until it names a skill-owned term.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Standard five-column format (no Foil Pair required).

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Standard five-column format.

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

`- [ ] C-NN: [one-line assertion]`

---

### V-03 — Role Sequence: Discriminator Role Produces Rejection Checklist Before Author Writes

**axis:** role-sequence
**hypothesis:** A Discriminator role producing a Rejection Checklist (TRUE/FALSE items, not advisory suggestions) before the Author writes anything satisfies C-11 (external enforcement gate) because the rejection step is: named (Discriminator), structural (runs before finalization), and non-advisory (checklist items have binary verdicts, not quality gradients). A pass condition hitting any TRUE item is rejected unconditionally.

---

You are building a scoring rubric for a Signal skill. Discriminator runs first. Author writes second.

--- ROLE: DISCRIMINATOR ---

Read the skill spec. Produce two artifacts before any criteria are written.

**Discrimination Surface**

Catalog every element of this skill's output contract that makes a pass condition skill-specific:

```
DISCRIMINATION SURFACE — {skill name}

Counts:
  - [element]: [minimum / exact / maximum per spec]

Named fields:
  - [field name]: [content type per spec]

Structural patterns:
  - [pattern]: [required shape — table with N columns, header with M fields, etc.]

Enumerations:
  - [name]: [closed value set]
```

**Rejection Checklist**

A pass condition is **rejected** if any item is TRUE:

```
REJECTION CHECKLIST

[ ] Names no element from the Discrimination Surface above.
[ ] Uses only quality-adjacent language with no counts or field names
    ("clear", "comprehensive", "well-formed", "high quality").
[ ] Could apply unchanged to a rubric for a different skill.
[ ] Names only structural elements present in all Markdown documents
    ("has headers", "has a table", "is formatted").
[ ] Requires evaluator discussion to reach pass/fail verdict.
```

--- END DISCRIMINATOR ---

--- ROLE: AUTHOR ---

Read the Discrimination Surface and Rejection Checklist before writing.

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. **DO NOT proceed until this minimum is met.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Write each essential criterion. After drafting the pass condition, apply the Rejection Checklist:

- Any item TRUE: condition is rejected. Revise to name a specific element from the Discrimination Surface. Re-apply until all FALSE.
- All items FALSE: condition approved.

Record inline before the table row:
`[Rejection Checklist: all FALSE — pass condition names {element from Discrimination Surface}]`

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Apply Rejection Checklist internally (no inline record required).

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)** — five-field format.

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

`- [ ] C-NN: [one-line assertion]`

---

### V-04 — Lifecycle Emphasis × Role Sequence: Failure Catalog Feeds Discriminator (Priority Combo)

**axis:** lifecycle-emphasis × role-sequence
**hypothesis:** C-12 and C-11 are non-redundant: the failure trace checks **criterion motivation** (did the author derive this from a named failure?), while the Rejection Checklist checks **pass condition vocabulary** (does the condition name a skill-owned element?). A criterion can pass the trace check while its pass condition fails the Rejection Checklist — both gates are needed. If V-04 does not show higher joint C-12+C-11 pass rates than either V-01 or V-03 alone, the gates are redundant and the combination adds nothing.

---

You are building a scoring rubric for a Signal skill.

**PHASE 0: FAILURE CATALOG**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. **DO NOT proceed until this minimum is met.**

--- ROLE: DISCRIMINATOR ---

Read the Phase 0 failure catalog and the skill spec.

**Step D-1: Discrimination Surface**

```
DISCRIMINATION SURFACE — {skill name}

Counts:     [one line per count element]
Named fields:  [one line per required field]
Structural patterns: [one line per required shape]
Enumerations:  [one line per closed value set]
```

**Step D-2: Rejection Checklist**

```
REJECTION CHECKLIST

[ ] Names no element from the Discrimination Surface.
[ ] Uses only quality-adjacent language with no counts or field names.
[ ] Could apply unchanged to a rubric for a different skill.
[ ] Names only structural elements present in all Markdown documents.
[ ] Requires evaluator discussion to reach pass/fail verdict.
[ ] Cites no parent failure from the Phase 0 catalog (Addresses: F-NN absent or
    the cited code does not exist in Phase 0).
```

The last item enforces the failure trace requirement. A well-written, skill-specific pass condition that addresses no named failure is rejected — motivation and vocabulary are both required.

--- END DISCRIMINATOR ---

--- ROLE: AUTHOR ---

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

| ID | Criterion | Category | Weight | Pass Condition | Addresses |
|----|-----------|----------|--------|----------------|-----------|

After drafting each criterion, apply the full Rejection Checklist (all six items). Record inline:

`[Rejection Checklist: all FALSE — addresses F-NN; pass condition names {element}]`

**PHASE 2: RECOMMENDED CRITERIA (2-3)** — six-field format; apply Rejection Checklist internally.

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)** — five-field format.

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

`- [ ] C-NN: [one-line assertion]`

---

### V-05 — Lifecycle Emphasis × Output Format: Failure Catalog Anchors Foil Pair Column

**axis:** lifecycle-emphasis × output-format
**hypothesis:** Phase 0 failure catalog makes the `Foil Pair` SPECIFIC cell easier to write: the builder knows which failure the criterion addresses, so the SPECIFIC pass condition is answerable as "what would an evaluator look at to detect F-NN?" Without Phase 0, the SPECIFIC cell must be derived from the spec alone. With Phase 0, the specific failure mode provides a concrete anchor. If SPECIFIC cells in V-05 runs cite failure modes from Phase 0 more often than V-02 runs, the anchoring effect is confirmed and the combination is additive.

---

You are building a scoring rubric for a Signal skill.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 0: FAILURE CATALOG**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. **DO NOT proceed to Phase 1 until this minimum is met.**

**PHASE 1: ESSENTIAL CRITERIA (3-5)**

Extended table format. Both `Addresses` and `Foil Pair` columns are required.

| ID | Criterion | Category | Weight | Pass Condition | Addresses | Foil Pair |
|----|-----------|----------|--------|----------------|-----------|-----------|

`Foil Pair` column — GENERIC/SPECIFIC pair, guided by the failure trace:

```
GENERIC: [pass condition that would miss the F-NN failure — applies to any artifact,
          names no observable specific to this skill]
SPECIFIC: [pass condition that detects the F-NN failure — names the count, field name,
           structural element, or enumeration an evaluator would inspect to find it]
```

Write the SPECIFIC cell by answering: "What would an evaluator look at in this output to determine whether F-NN is present?" The answer is the SPECIFIC pass condition. The GENERIC version is the same criterion without that named observable.

**PHASE 2: RECOMMENDED CRITERIA (2-3)** — standard five-column format.

**PHASE 3: ASPIRATIONAL CRITERIA (1-2)** — standard five-column format.

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

`- [ ] C-NN: [one-line assertion]`

---

### Anchor Designation

**Anchor: V-01**

**Structural impact:** Phase 0 gate makes C-12 a format check, not a quality judgment. Empty `Addresses` column = structural incompleteness, auditable by column inspection alone. No prose evaluation needed to detect failure.

**Isolation quality:** Only lifecycle structure modified (Phase 0 added). Phase content unchanged. The `Addresses` column is the only new table field. Co-variation in combination runs traces to the Phase 0 gate or Addresses column only.

**Detectable failure condition:** Skipped Phase 0 → no Addresses column (or empty cells). Populated Phase 0 with non-existent codes → traceability link broken by cross-reference. Both failures are mechanical and auditable.

**Combination priority:**
1. **V-04 (V-01 × V-03)** — highest. Two non-redundant gates: failure trace checks criterion motivation, Rejection Checklist checks pass condition vocabulary. Additive if both fire on independent failures.
2. **V-05 (V-01 × V-02)** — second. Failure catalog anchors foil pair SPECIFIC cell. Additive if SPECIFIC cells improve in quality over V-02 alone.

---

Saved to `simulations/quest/golden/quest-rubric-variate-v2-R02-2026-03-15-new.md`.

**Key differences from the existing R02 file** (which targeted an intermediate rubric):

| | Existing R02 | This file |
|---|---|---|
| C-11 target | inertia test framing | external enforcement gate (Rejection Checklist role) |
| C-12 target | calibration example column | failure-first derivation (Phase 0 catalog) |
| C-13 target | phase-gate enforcement | generic-vs-specific foil pair (Foil Pair column) |
| Priority combo | role-sequence × inertia-framing | lifecycle-emphasis × role-sequence (V-04) |
| Anchor | V-03 (lifecycle sub-steps) | V-01 (Phase 0 failure catalog) |
