# quest-rubric Variate — Round 8 against rubric v8

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v8 (C-01 through C-31; essential C-01–C-05)
**Round:** R8 — 3 single-axis + 2 combination

**Round 8 design note:** Round 7 produced one excellence signal absorbed into v8 as
aspirational criterion C-31 (pre-phase output skeleton declared from MECHANISMS alone and
cross-referenced in Structural Verification, ES-R7-1). C-31 extends C-29 (mechanism overview
declares structural format requirements) into an executable artifact: the builder constructs
the heading skeleton before any phase begins, creating a second independent source of truth.
Structural Verification then checks both the instruction-derived patterns and the
skeleton-declared headings, making builder-commitment failures (declared but not produced)
distinguishable from heading-pattern misses (absent from output but never declared in the
skeleton either).

R7 V-05 is the anchor. Under the v8 rubric:

**R7 V-05 score under v8:**
- Essential (5/5): all pass → 60
- Recommended (3/3): all pass → 30
- Aspirational (22/23):
  - C-09–C-30: all pass (R7 V-05 satisfies each by construction)
  - C-31: FAIL — R7 V-05 has no `### OUTPUT SKELETON` step; Structural Verification
    checks only instruction-derived heading patterns (Scan A equivalent) with no
    cross-reference to a builder-declared skeleton (Scan B absent). R7 V-03 introduced
    the `### OUTPUT SKELETON` step and an SV skeleton cross-check; under v8, V-03 would
    score C-31 PASS while V-05 scores C-31 FAIL.
  → 22/23 × 10 = 9.57
- **Composite: 99.57 → Golden. C-31 is the sole gap.**

The gap is a two-part structural addition: (1) insert a named `### OUTPUT SKELETON` step
built from MECHANISMS alone before any phase begins, and (2) update Structural Verification
to cross-reference it with an explicit two-source check that distinguishes builder-commitment
failures from heading-pattern misses.

**Axis selection for R8:**

Three single axes:

1. **skeleton-declaration** (V-01) — minimal addition to R7 V-05: `### OUTPUT SKELETON`
   step + SV Scan A / Scan B split, everything else identical to R7 V-05
2. **lifecycle-emphasis** (V-02) — skeleton promoted to `### PHASE 0 — OUTPUT SKELETON`
   with its own completion gate and tier-structured skeleton format
3. **phrasing-register** (V-03) — conversational register throughout; CONSTRAINT /
   INVARIANT / PRECONDITION labels replaced with plain imperative prose; structural
   contract identical to V-01

Two combinations:

4. **skeleton-declaration × lifecycle-emphasis** (V-04) — Phase 0 framing (V-02) +
   Status-Quo Rubric competitive framing (V-01); tests whether Phase 0 framing
   interacts with Status-Quo inertia vocabulary
5. **Full accumulation** (V-05) — V-04 + explicit M-06 skeleton mechanism added to
   MECHANISMS overview; tests whether naming the skeleton step as a mechanism (making
   its structural output format visible at orientation time) produces a C-29-analogous
   excellence signal for non-criterion-level mechanisms

---

## V-01 — Skeleton Declaration (Single Axis)

**axis:** skeleton-declaration
**hypothesis:** The minimal delta from R7 V-05 is sufficient to score C-31 PASS under v8:
insert the `### OUTPUT SKELETON` step between INVARIANTS and `### AUTHOR PHASE`, and
split Structural Verification into Scan A (instruction-derived patterns, heading-pattern
miss detection) and Scan B (skeleton-declared headings, builder-commitment failure
detection). All other elements — Status-Quo framing, formal register, MECHANISMS heading
patterns for C-29, SV scope declaration for C-30, annotated formula denominator for C-28 —
are identical to R7 V-05. If C-31 fails in V-01, the two-source distinction in SV is not
explicit enough: investigate whether C-31's pass condition requires both sources to be
labeled with distinct names (not just "also verify against the skeleton") and whether the
CONSTRAINT must name both sources explicitly.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan

**Why five mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional — not the first failure
listed. The category gate prevents all criteria clustering in one dimension. The Auditor
table enables cross-criterion analysis under `### REDUNDANCY-CHECK-TABLE`. The Status-Quo
Rubric framing makes the discrimination requirement concrete: every criterion you write must
catch something the Status-Quo Rubric misses. If it does not, it belongs in the Status-Quo
Rubric, not yours.

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### OUTPUT SKELETON (produce before any phase begins)

Before entering the Author Phase, construct the complete heading skeleton for your output.
Use only the MECHANISMS section above — do not read the phase instructions yet.

List every named section heading your output will contain, in order, using the exact
heading patterns from the MECHANISMS section. For per-criterion headings, use placeholders
where the criterion count is not yet known.

```
### AUTHOR PHASE
### INERTIA-RECORD [C-01]
### CALIBRATION-PAIR [C-01]
### CRITERION [C-01]
[... repeat for each essential criterion C-02 through C-0N ...]
### STRUCTURAL VERIFICATION
### AUDITOR PHASE
### REDUNDANCY-CHECK-TABLE
### END AUDITOR PHASE
[Final Rubric section]
```

PRECONDITION for Author Phase entry: skeleton is complete.

A heading declared in this skeleton but absent from the output is a **builder-commitment
failure** — distinct from a **heading-pattern miss** (absent from output and also absent
from this skeleton because it was never declared). Structural Verification checks both
failure classes independently using two separate scans.

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2. For each criterion, apply sub-steps 2a–2d in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration that the
  Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR for the same criterion.
Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
are complete satisfies structural ordering while violating INVARIANT B. Do not defer.
Batch production is a protocol violation even if block order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the condition it would accept for
  any artifact; the competitor's best attempt at this criterion]
GROUNDED: [what your rubric says — the condition the Status-Quo Rubric rejects because
  it names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with STATUS-QUO and GROUNDED fields,
      written before this gate check and before this criterion's table row (INVARIANT B
      confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. If any precondition is false, do not record the
criterion row. Write the missing block or correct the alignment, then re-check.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories present, add or revise criteria in Phase 3 before
proceeding. A rubric clustering all criteria in one or two categories fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry (verified as part of the Auditor Gate checklist).

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

Scan the Author phase output for section headings matching the patterns below. Pattern
scan only — content not evaluated; a heading is present or absent.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss** — a Phase 2 forward gate was
bypassed.

**Scan B — skeleton-declared headings (builder-commitment failure detection):**

Refer to the OUTPUT SKELETON produced before the Author Phase. For each heading declared
in the skeleton, confirm it is present in the output:

```
- [ ] Every heading declared in the OUTPUT SKELETON has a corresponding block in the output
```

A skeleton heading absent from the output is a **builder-commitment failure** — the builder
declared it before the Author Phase but did not produce it. This failure class is distinct
from a heading-pattern miss: a builder-commitment failure can involve a heading that
instruction-scanning alone would not detect as required (because the builder committed to
it independently of the instructions).

For any missing block found in either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until (1) every required Author Phase heading
pattern from Scan A is confirmed present and correctly ordered, AND (2) every heading
declared in the OUTPUT SKELETON is present in the output (Scan B shows no
builder-commitment failures outstanding). Structural completeness is a precondition for
reasoning analysis — the Auditor role never encounters structurally incomplete criteria.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

- **YES** — independent: each adds unique signal. Keep both.
- **NO** — redundant: passing one always means passing the other. Revise, consolidate, or
  remove the redundant criterion.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification: this is the Auditor Phase heading, verified here)

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Record the criterion ID range for each tier, then write the formula with annotations.

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual criterion count. Replace [first]/[last] with actual
criterion IDs. DO NOT use symbolic variable names as denominators — the criterion ID range
annotation makes the denominator self-verifiable without counting the criteria table.

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-02 — Lifecycle Emphasis (Single Axis)

**axis:** lifecycle-emphasis
**hypothesis:** V-01 positions the skeleton as a pre-phase step with a simple PRECONDITION
label. V-02 promotes it to a full named lifecycle phase — `### PHASE 0 — OUTPUT SKELETON`
— with the same structural weight as `### AUTHOR PHASE` and `### AUDITOR PHASE`. The
skeleton format is tier-structured (ESSENTIAL CRITERIA BLOCKS / VERIFICATION PHASES) rather
than a flat heading list. Structural Verification explicitly labels its two scans. Hypothesis:
naming the skeleton as PHASE 0 makes the lifecycle sequence (Phase 0 → Author → Structural
Verification → Auditor) visible from section-heading scan alone, satisfying C-26 (phase
transitions marked by named section headings) at the Phase 0 boundary. If a new excellence
signal emerges around Phase 0 gate completeness or tier-structured skeleton format, it is
the R9 C-32 candidate. Failure condition: if C-31 fails in V-02 while passing in V-01,
the PHASE 0 framing conflicts with C-31's pass condition — investigate whether "a named
pre-phase step" requires a `### OUTPUT SKELETON` heading specifically, or accepts
`### PHASE 0 — OUTPUT SKELETON` as equivalent.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan

**Why five mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion pattern analysis. The
Status-Quo Rubric framing makes the discrimination requirement concrete.

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### PHASE 0 — OUTPUT SKELETON

**Lifecycle position:** Phase 0 precedes all other phases. No Author Phase criterion may
be written until Phase 0 is complete and the Phase 0 Completion Gate is cleared.

Construct the complete heading skeleton for your output using only the MECHANISMS section
above. Do not read ahead into the phase instructions.

The skeleton declares every named section heading your output will contain, organized by
lifecycle position. Use the exact heading patterns from the MECHANISMS section. For
per-criterion headings, use placeholders where the criterion count is not yet known.

Produce the skeleton in this structured format:

```
--- PHASE 0: OUTPUT SKELETON ---

ESSENTIAL CRITERIA BLOCKS (Author Phase 2, repeated for each criterion C-01 through C-0N):
  ### AUTHOR PHASE
  ### INERTIA-RECORD [C-01]
  ### CALIBRATION-PAIR [C-01]
  ### CRITERION [C-01]
  [... C-02, C-03, ... C-0N ...]

RECOMMENDED & ASPIRATIONAL CRITERIA (Author Phase 3 — criteria table only, no named blocks):
  (none — appears inline in Phase 3 criteria table)

VERIFICATION PHASES:
  ### STRUCTURAL VERIFICATION
  ### AUDITOR PHASE
  ### REDUNDANCY-CHECK-TABLE
  ### END AUDITOR PHASE

OUTPUT SECTION:
  [Final Rubric section]
```

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No heading in the skeleton was derived from reading phase instructions
      (skeleton must be built from MECHANISMS alone — flag and remove any heading not
      derivable from MECHANISMS)

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

The skeleton is a structural commitment. Every heading declared here must appear in the
output. A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure**. A heading absent from both the skeleton and the output is a **heading-pattern
miss**. These are distinct failure classes. Structural Verification checks them separately.

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order. For each criterion, apply sub-steps 2a–2d
in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. Does this
condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration that the
  Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
satisfies structural ordering while violating INVARIANT B. Do not defer. Batch production
is a protocol violation even if block order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the competitor's best attempt]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check and
      before this criterion's table row (INVARIANT B confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. Do not record the criterion row if any precondition
is false. Write the missing block or correct the alignment, then re-check.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories present, add or revise criteria before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss** — a Phase 2 forward gate was
bypassed.

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

Refer to the skeleton produced in `### PHASE 0 — OUTPUT SKELETON`. For each heading
declared in the Phase 0 skeleton, confirm it is present in the output:

```
- [ ] Every heading declared in the Phase 0 skeleton has a corresponding block in the output
```

A Phase 0 heading absent from the output is a **builder-commitment failure**. A heading
missing from both Scan A and Scan B (never declared in Phase 0 and absent from the output)
is a heading-pattern miss detectable only by Scan A. The two scans cover non-overlapping
failure classes.

For any missing block from either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until Scan A and Scan B both show all required
headings confirmed present. Structural completeness is a precondition for reasoning analysis.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (after completing the table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria: Is there a rubric output that passes one but fails
the other for a non-trivial reason?

- **YES** — independent. Keep both.
- **NO** — redundant. Revise, consolidate, or remove.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification: Auditor Phase heading, verified here)

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual count. DO NOT use symbolic variable names as
denominators. Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Phrasing Register: Conversational (Single Axis)

**axis:** phrasing-register
**hypothesis:** V-01 uses formal vocabulary throughout: CONSTRAINT, INVARIANT, PRECONDITION,
VIOLATION. V-03 replaces these labels with plain imperative prose delivering the same
structural contract at the same positions. Gates become "Stop here. Do not continue until
[condition]." Invariants become "Rule A: / Rule B:". Anti-deferral becomes "Write it now.
Do not save calibration pairs for after all pass conditions are done." Hypothesis: formal
label vocabulary creates parsing overhead or is skipped as boilerplate — especially in
multi-step phases where a constraint stated at the top of the phase has faded by the time
the operative sub-step is reached. Conversational equivalents at the same structural
positions produce fewer gate violations because they read as immediate instructions rather
than protocol headers. Failure condition: if C-22 or C-25 regress (both require explicit
anti-deferral prohibition language), investigate whether "Write it now" satisfies "explicit
blocking language" under those criteria's pass conditions.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol has five quality mechanisms. Every pass condition you write must name
something the Status-Quo Rubric cannot verify — a specific count, field name, structural
pattern, or enumeration from the target skill's output contract. If the Status-Quo Rubric
would accept your condition, the condition is not discriminating enough.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes; C-01 targets the failure making the output non-functional regardless of
  all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing heading detectable by scan without reading content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; preventing omission up front is not the same as detecting it afterward
- **M-04 — category-coverage:** at least 3 of 5 categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`

**Two rules hold throughout:**

- **Rule A:** A criterion row appears in the output only after its `### INERTIA-RECORD [C-NN]`
  and `### CALIBRATION-PAIR [C-NN]` blocks are confirmed present above it.
- **Rule B:** The `### CALIBRATION-PAIR [C-NN]` block is written immediately after
  `### INERTIA-RECORD [C-NN]` for the same criterion — not after all INERTIA-RECORD blocks
  are done. Writing all calibration pairs in a batch at the end violates Rule B even if
  the structural order (CALIBRATION-PAIR before CRITERION) is preserved.

---

### OUTPUT SKELETON (produce before any phase begins)

Before you write any criteria, produce the heading skeleton for your output. Use only the
MECHANISMS section above — do not read ahead into the phase instructions.

List every named section heading your output will contain, in order, using the exact heading
patterns from the MECHANISMS section. Use placeholders where the criterion count is unknown.

```
### AUTHOR PHASE
### INERTIA-RECORD [C-01]
### CALIBRATION-PAIR [C-01]
### CRITERION [C-01]
[... repeat for each essential criterion ...]
### STRUCTURAL VERIFICATION
### AUDITOR PHASE
### REDUNDANCY-CHECK-TABLE
### END AUDITOR PHASE
[Final Rubric section]
```

Produce this skeleton now, before doing anything else.

Every heading you list here is a commitment — it must appear in the output. A heading you
declared but did not produce is a builder-commitment failure (you said you would produce
it, and you did not). That is a different failure from forgetting to include a required
heading entirely. Structural Verification checks for both kinds of gap.

Do not start the Author Phase until this skeleton is complete.

---

### AUTHOR PHASE

Read the skill spec. Before writing any criterion, answer these three questions:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

List at least 3 blocking failure modes and at least 2 degrading failure modes.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Stop here. Do not move to Severity Ranking until you have at least 3 blocking and at least
2 degrading failure modes listed.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank the blocking failure modes from most to least critical.

Most critical means: the failure making the output non-functional as an objective function
regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical — C-01 will target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

Before continuing: confirm every blocking failure mode from Phase 1 appears in the rank.

**AUTHOR PHASE 2 ENTRY CHECK**

Before writing any criterion, confirm all four of these:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete, all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

Do not write any criterion until all four are checked off.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1, C-02 targets rank-2.
For each criterion, work through steps 2a–2d in order. Do not skip or reorder a step.

**Step 2a — Draft the pass condition.**

Write a specific, observable condition two independent evaluators can verify without
discussion. Ask yourself: does this condition catch something the Status-Quo Rubric would
miss? If not, sharpen it until it does.

**Step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would "the output is clear, complete, and well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration from this
  skill's contract making this condition non-generic]
Severity-rank alignment: [this criterion targets rank-N failure mode — "[failure mode]"]
```

Produce this block before moving to step 2c. (Rule A requires the INERTIA-RECORD to come
before the CALIBRATION-PAIR for the same criterion.)

**Step 2c — Produce the CALIBRATION-PAIR block.**

Write it now — right after step 2b, while the pass condition is still fresh. Do not save
calibration pairs until after all pass conditions are written. Writing them all at the end
violates Rule B, even if they appear in the correct order in the final output.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the condition it would accept for
  any artifact of this type]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
```

**Step 2d — Per-criterion forward check.**

Before recording this criterion and starting the next one, confirm all three:

- [ ] `### INERTIA-RECORD [C-NN]` is present above, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` is present above, written before this check and before
      the criterion's table row (Rule B satisfied)
- [ ] Severity-rank alignment field matches rank-N

If anything is missing, write the missing block and re-check. Do not record the criterion
row until all three are confirmed.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition] |
```

Repeat steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**Category coverage check:**

Before moving to Structural Verification, confirm at least 3 distinct categories appear
across all criteria (essential + recommended + aspirational).

Categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present: ___________________________
- [ ] Count: ___ (need at least 3)

If fewer than 3, add or revise criteria before continuing.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

This step covers Author Phase output only. Auditor Phase output has not been produced yet.

Out of scope here:
- `### REDUNDANCY-CHECK-TABLE` — belongs to the Auditor Phase. It will be checked at the
  Auditor Gate.

**Check 1 — instruction-derived heading patterns:**

For each essential criterion C-NN from Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, comes before ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO and GROUNDED), comes before ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading missing here means a forward check was skipped.

**Check 2 — skeleton-declared headings:**

Look at the OUTPUT SKELETON you produced before the Author Phase. For each heading in the
skeleton, confirm it appears in the output:

```
- [ ] Every heading from the OUTPUT SKELETON is present in the output
```

A skeleton heading missing from the output is a builder-commitment failure — different from
a heading-pattern miss caught by Check 1.

For any missing block from either check: write the block using the exact heading pattern,
then re-check.

Do not start the Auditor Phase until both checks are complete with no missing headings.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read every one of them before writing anything.

Write the full Audit Table after reading all criteria — do not write rows one at a time
as you work through criteria.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

Columns:
- *Discriminating Element*: what the Status-Quo Rubric cannot replicate. Fill for every NO.
  Leave blank for YES.
- *Revised Condition*: fill for every YES; leave blank otherwise.

After the table: write one sentence on whether discriminating elements vary in type or
cluster. Confirm C-01 targets the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria: can you construct a rubric output that passes one but
fails the other for a real, non-trivial reason?

- **YES** — they are independent. Keep both.
- **NO** — they always agree. Revise, consolidate, or remove the redundant one.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

Do not continue until all pairs show YES, or any NO-flagged pairs are resolved and
re-evaluated as YES.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Before producing the Final Rubric, confirm:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and redundancy table cleared

Do not produce the Final Rubric until all are confirmed.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual count. Do not use symbolic variable names as
denominators. Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-04 — Skeleton Declaration × Lifecycle Emphasis (Combination)

**axis:** skeleton-declaration × lifecycle-emphasis
**hypothesis:** V-01 adds the skeleton as a simple pre-phase step. V-02 promotes it to
`### PHASE 0 — OUTPUT SKELETON` with its own completion gate and tier-structured format.
V-04 combines both axes: Phase 0 lifecycle framing from V-02 plus full Status-Quo Rubric
competitive framing from V-01. The combination tests whether Phase 0 lifecycle framing
interacts with the Status-Quo vocabulary — specifically, whether the Structural Verification
Scan A / Scan B labeling (from V-02) creates ambiguity when CALIBRATION-PAIR fields are
labeled STATUS-QUO / GROUNDED (a term "Status-Quo" appearing in two different contexts:
the Phase 0 competitor rubric framing and the Scan B failure class name). No interaction
risk expected: the STATUS-QUO field label in CALIBRATION-PAIR refers to the competitor
rubric; the Scan B builder-commitment failure label refers to skeleton completeness.
These appear in separate sections. Expected score: 100.0 under v8. Failure condition for
C-31: if Phase 0 framing causes the OUTPUT SKELETON to be evaluated under C-31's pass
condition as a "full lifecycle phase" rather than a "pre-phase step" — investigate whether
C-31's language "before any Author Phase criterion is processed" is satisfied by Phase 0
framing or only by a step that precedes a named `### AUTHOR PHASE` heading.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan

**Why five mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional — not the first failure
listed. The category gate prevents all criteria clustering in one dimension. The Auditor
table enables cross-criterion analysis under `### REDUNDANCY-CHECK-TABLE`. The Status-Quo
Rubric framing makes the discrimination requirement concrete: every criterion you write must
catch something the Status-Quo Rubric misses.

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### PHASE 0 — OUTPUT SKELETON

**Lifecycle position:** Phase 0 precedes all other phases. No Author Phase criterion may
be written until Phase 0 is complete and the Phase 0 Completion Gate is cleared.

Construct the complete heading skeleton for your output using only the MECHANISMS section
above. Do not read ahead into the phase instructions.

The skeleton declares every named section heading your output will contain, organized by
lifecycle position. Use the exact heading patterns from the MECHANISMS section. For
per-criterion headings, use placeholders where criterion count is not yet known.

Produce the skeleton in this structured format:

```
--- PHASE 0: OUTPUT SKELETON ---

ESSENTIAL CRITERIA BLOCKS (Author Phase 2, repeated for each criterion C-01 through C-0N):
  ### AUTHOR PHASE
  ### INERTIA-RECORD [C-01]
  ### CALIBRATION-PAIR [C-01]
  ### CRITERION [C-01]
  [... C-02, C-03, ... C-0N ...]

RECOMMENDED & ASPIRATIONAL CRITERIA (Author Phase 3 — criteria table only, no named blocks):
  (none — appears inline in Phase 3 criteria table)

VERIFICATION PHASES:
  ### STRUCTURAL VERIFICATION
  ### AUDITOR PHASE
  ### REDUNDANCY-CHECK-TABLE
  ### END AUDITOR PHASE

OUTPUT SECTION:
  [Final Rubric section]
```

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No heading in the skeleton was derived from reading phase instructions
      (skeleton built from MECHANISMS alone)

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure**. A heading absent from both the skeleton and the output is a **heading-pattern
miss**. These are distinct failure classes. Structural Verification checks them separately
using two independent scans.

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order. For each criterion, apply sub-steps 2a–2d
in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration that the
  Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
satisfies structural ordering while violating INVARIANT B. Do not defer. Batch production
is a protocol violation even if block order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the competitor's best attempt]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check and
      before this criterion's table row (INVARIANT B confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. Do not record the criterion row if any precondition
is false. Write the missing block or correct the alignment, then re-check.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories present, add or revise criteria before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss** — a Phase 2 forward gate was
bypassed.

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

Refer to the `### PHASE 0 — OUTPUT SKELETON` produced above. For each heading declared
in the Phase 0 skeleton, confirm it is present in the output:

```
- [ ] Every heading declared in the Phase 0 skeleton has a corresponding block in the output
```

A Phase 0 heading absent from the output is a **builder-commitment failure**. The two
failure classes are non-overlapping: Scan A catches headings required by instructions but
absent from output; Scan B catches headings declared by the builder but absent from output.

For any missing block from either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until Scan A and Scan B both show all required
headings present. Structural completeness is a precondition for reasoning analysis.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (after completing the table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria: Is there a rubric output that passes one but fails
the other for a non-trivial reason?

- **YES** — independent. Keep both.
- **NO** — redundant. Revise, consolidate, or remove.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification: Auditor Phase heading, verified here)

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual count. DO NOT use symbolic variable names as
denominators. Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-05 — Full Accumulation (Five-Axis Combination)

**axis:** skeleton-declaration × lifecycle-emphasis × inertia-framing × phrasing-register ×
output-format
**hypothesis:** V-05 carries all five axes simultaneously. V-04 closes C-31 (skeleton-
declaration × lifecycle-emphasis × inertia-framing). V-05 adds the remaining two axes:
formal CONSTRAINT/INVARIANT register (phrasing-register, from R6/R7) and a sixth mechanism
M-06 added to the MECHANISMS overview that explicitly names the OUTPUT SKELETON step and
its heading pattern (output-format axis). M-06 tests a potential C-29 extension: does C-29's
pass condition require that even non-criterion-level mechanisms (like the skeleton step)
be named in the MECHANISMS overview with their structural output format? If M-06 in V-05
produces a new excellence signal around orientation-time completeness for all structural
steps — not only the per-criterion named blocks — it becomes the R9 C-32 candidate. All
five axes operate at non-competing layers: M-06 changes the MECHANISMS preamble; Phase 0
changes the pre-phase step heading; Status-Quo framing changes inertia vocabulary; formal
register changes constraint labels; annotated denominator changes the scoring formula
annotation. Combined, V-05 should score 100.0 under v8 (23/23 aspirational). Failure
condition: if C-29 fails in V-05 while passing in V-01 or V-04, investigate whether adding
M-06 to the MECHANISMS section changes how C-29's pass condition evaluates the overview —
specifically whether a builder reading M-01 through M-06 can now identify all mechanisms
requiring named `###` headings (M-02, M-05, M-06) without reading phase instructions.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through six mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan
- **M-06 — output skeleton:** before any phase begins, the builder constructs the complete
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-05 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it to
  detect builder-commitment failures (declared but not produced) distinct from
  heading-pattern misses (absent from output and absent from skeleton)

**Why six mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion pattern analysis. The
output skeleton serves as an executable test of mechanism-overview sufficiency: if the
overview is complete, the builder can construct the full heading structure before reading
a single phase instruction. If the skeleton cannot be completed from the overview alone,
the overview is missing a structural declaration. The Status-Quo Rubric framing makes the
discrimination requirement concrete throughout.

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### PHASE 0 — OUTPUT SKELETON

**Lifecycle position:** Phase 0 precedes all other phases. No Author Phase criterion may
be written until Phase 0 is complete and the Phase 0 Completion Gate is cleared.

Construct the complete heading skeleton for your output using only the MECHANISMS section
above (M-01 through M-06). Do not read ahead into the phase instructions. The skeleton is
an executable test of M-06's claim: if you cannot construct the full heading structure from
the MECHANISMS section alone, the overview is incomplete.

The skeleton declares every named section heading your output will contain, organized by
lifecycle position. Use the exact heading patterns from the MECHANISMS section.

Produce the skeleton in this structured format:

```
--- PHASE 0: OUTPUT SKELETON ---

ESSENTIAL CRITERIA BLOCKS (Author Phase 2, repeated for each criterion C-01 through C-0N):
  ### AUTHOR PHASE
  ### INERTIA-RECORD [C-01]
  ### CALIBRATION-PAIR [C-01]
  ### CRITERION [C-01]
  [... C-02, C-03, ... C-0N ...]

RECOMMENDED & ASPIRATIONAL CRITERIA (Author Phase 3 — criteria table only, no named blocks):
  (none — appears inline in Phase 3 criteria table)

VERIFICATION PHASES:
  ### STRUCTURAL VERIFICATION
  ### AUDITOR PHASE
  ### REDUNDANCY-CHECK-TABLE
  ### END AUDITOR PHASE

OUTPUT SECTION:
  [Final Rubric section]
```

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No heading in the skeleton was derived from reading phase instructions
      (skeleton built from M-01 through M-06 alone — if a heading is present that the
      MECHANISMS section does not name, flag it and remove it)

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure** — distinct from a **heading-pattern miss** (absent from output and absent from
the skeleton because it was never declared). The Status-Quo Rubric cannot detect either
failure class because it produces no structural commitments. Structural Verification
distinguishes them using two independent scans.

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2. For each criterion, apply sub-steps 2a–2d in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration that the
  Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR for the same criterion.
Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
are complete satisfies structural ordering while violating INVARIANT B. Do not defer.
Batch production is a protocol violation even if block order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the condition it would accept for
  any artifact; the competitor's best attempt at this criterion]
GROUNDED: [what your rubric says — the condition the Status-Quo Rubric rejects because
  it names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with STATUS-QUO and GROUNDED fields,
      written before this gate check and before this criterion's table row (INVARIANT B
      confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. If any precondition is false, do not record the
criterion row. Write the missing block or correct the alignment, then re-check.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories present, add or revise criteria in Phase 3 before
proceeding. A rubric clustering all criteria in one or two categories fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry (verified as part of the Auditor Gate checklist).

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required; and (2)
the builder-declared skeleton from Phase 0, which records which headings the builder
committed to producing. A heading absent from both sources is undetectable by this scan.
A heading absent from source (1) but not declared in source (2) is a heading-pattern miss.
A heading declared in source (2) but absent from the output is a builder-commitment failure.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

Scan the Author phase output for section headings matching the patterns below. Pattern
scan only — content not evaluated; a heading is present or absent.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss** — a Phase 2 forward gate was
bypassed.

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

Refer to the `### PHASE 0 — OUTPUT SKELETON` produced above. For each heading declared
in the Phase 0 skeleton, confirm it is present in the output:

```
- [ ] Every heading declared in the Phase 0 skeleton has a corresponding block in the output
```

A Phase 0 heading absent from the output is a **builder-commitment failure** — the builder
declared it as a structural commitment but did not produce it. This failure class is
invisible to Scan A: instruction scanning confirms format compliance but cannot detect
violations of builder-declared commitments.

For any missing block found in either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until (1) every required Author Phase heading
pattern from Scan A is confirmed present and correctly ordered, AND (2) every heading
declared in the Phase 0 OUTPUT SKELETON is present in the output (Scan B shows no
builder-commitment failures outstanding). Structural completeness is a precondition for
reasoning analysis — the Auditor role never encounters structurally incomplete criteria.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

- **YES** — independent: each adds unique signal. Keep both.
- **NO** — redundant: passing one always means passing the other. Revise, consolidate, or
  remove the redundant criterion.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification: this is the Auditor Phase heading, verified here)

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Record the criterion ID range for each tier, then write the formula with annotations.

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual criterion count. Replace [first]/[last] with actual
criterion IDs. DO NOT use symbolic variable names (N_essential, N_aspirational) as
denominators — the criterion ID range annotation makes the denominator self-verifiable
without counting the criteria table.

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## Anchor Designation

**Anchor: V-05**

V-05 is designated the combination anchor for Round 8.

**Structural impact:** V-05 carries all five axes. The R8 addition (skeleton-declaration
for C-31) closes the sole gap in R7 V-05's 99.57 score under v8, moving the aspirational
denominator coverage from 22/23 to 23/23 (expected). The four inherited axes from R6/R7
(Status-Quo inertia framing, formal register, MECHANISMS heading patterns, SV scope
declaration + annotated formula denominator) continue to satisfy C-11, C-12, C-22, C-25,
C-28, C-29, and C-30. The new M-06 addition in V-05 tests whether a C-29-style excellence
signal is available for skeleton-step orientation.

**Isolation quality:**
- V-01 isolates skeleton-declaration (C-31 only, minimal change from R7 V-05)
- V-02 isolates lifecycle-emphasis (Phase 0 framing, tier-structured skeleton)
- V-03 isolates phrasing-register (conversational, no CONSTRAINT/INVARIANT labels)
- V-04 tests V-01 × V-02 (skeleton-declaration × lifecycle-emphasis + Status-Quo framing)
- V-05 extends V-04 with M-06 skeleton mechanism in MECHANISMS overview (full accumulation)

**Detectable failure conditions:**

| Failure | Investigation |
|---------|--------------|
| C-31 fails in V-01 but V-03 from R7 passed | V-01's Scan A/Scan B labeling is not explicit enough — compare against V-03's "Also verify the OUTPUT SKELETON" language; identify the minimum explicit language C-31 requires |
| C-31 fails in V-02 but passes in V-01 | "PHASE 0" heading does not satisfy C-31's "named pre-phase step" requirement — investigate whether C-31's pass condition requires the heading to be `### OUTPUT SKELETON` specifically or accepts any named pre-phase step heading |
| C-29 passes in V-05 but not V-01/V-04 | M-06 in the MECHANISMS section is the change that satisfies C-29 for the skeleton mechanism — indicates C-29's pass condition applies to all mechanisms producing named headings, not only M-02 and M-05 |
| C-22 or C-25 regress in V-03 | Conversational "Write it now" does not qualify as "explicit blocking language" under those criteria — investigate exact language thresholds |
| V-04 fails C-29 or C-30 while V-01 and V-02 pass separately | Phase 0 framing in V-04 changes the MECHANISMS heading scan in a way that conflicts with C-29 or C-30 scope declaration — investigate whether "Phase 0" changes how the overview's structural contract is evaluated |

**Combination priority for Round 9:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-05 (this round) | all five | C-31 + R6/R7 axes preserved | 1 | Maximum coverage; test for new excellence signals around M-06 |
| V-05 × C-29 extension | V-05 + M-06 expanded for all mechanisms | Potential C-32 | 2 | If M-06 in V-05 produces an excellence signal around mechanism-overview completeness for structural steps, candidate for v9 |
| V-03 × V-04 | conversational × Phase 0 | C-31, C-22, C-25 | 3 | Test whether conversational register interacts with Phase 0 framing — if "Rule B" satisfies C-22/C-25 as well as INVARIANT B, register change is safe |

---

## Combination Roadmap (for Round 9)

**R8 outcome scenarios:**

| Scenario | Expected Outcome | Round 9 Action |
|----------|----------------|----------------|
| V-01 reaches 100.0, V-05 also reaches 100.0 | C-31 closed by skeleton-declaration; Phase 0 and M-06 add no interference | Extract excellence signals from V-05 M-06 addition; if M-06 produces a new orientation-completeness signal for non-criterion mechanisms, absorb into v9 as C-32 |
| V-01 reaches 100.0, V-02 fails C-31 | Phase 0 heading does not satisfy C-31's "pre-phase step" language | R9 variations should test `### OUTPUT SKELETON` (V-01 heading) within Phase 0 lifecycle framing — i.e., use `### PHASE 0 — OUTPUT SKELETON` but verify the inner heading name `### OUTPUT SKELETON` satisfies C-31's pass condition |
| V-01 fails C-31 but R7 V-03 passed | V-01's two-source Scan A/Scan B split is not the right implementation | Re-read C-31 pass condition exactly; identify the minimum language required in both the pre-phase step and in Structural Verification; V-01 may need the "two independent sources of truth" phrasing from V-05 to satisfy condition (b) |
| V-05 passes C-29 where V-01/V-04 fail | M-06 is the C-29 discriminator for skeleton mechanisms | R9: make M-06 a required element; design single-axis variation isolating M-06 addition against the R7 V-05 baseline |
| None of V-01/V-02/V-03 closes C-31 | Skeleton additions are insufficient for C-31 as written | Re-read C-31 pass condition conditions (a) and (b) precisely; diagnose which condition each variation fails and what element is still missing |
