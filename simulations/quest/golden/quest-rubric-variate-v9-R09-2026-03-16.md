# quest-rubric Variate — Round 9 against rubric v9 (batch 2)

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v9 (C-01 through C-34; essential C-01–C-05)
**Round:** R9 — 3 single-axis + 2 combination (batch 2)

**Batch 2 design note:** Batch 1 (2026-03-15) explored inertia-framing (3-gap competitors),
output-format (flat annotated checklist), and lifecycle-emphasis (Phase 0 M-06 Self-Test).
Batch 2 covers the two axes Batch 1 left untouched — role-sequence and phrasing-register —
plus a fresh angle on inertia-framing (minimal vs. named competitor).

R8 V-05 is the v9 anchor (100.0). All five variations start from its structure.

**R8 V-05 score under v9 (baseline):**
- Essential (5/5): all pass → 60
- Recommended (3/3): all pass → 30
- Aspirational (26/26): all pass → 10.0
- **Composite: 100.0 → Golden.**

**Axis selection for R9 Batch 2:**

Three single axes:
1. **role-sequence** (V-01) — Auditor Pre-Declaration inserted before Author Phase;
   Auditor reads spec and declares per-criterion acceptance thresholds; Author Phase drafts
   against those thresholds; tests whether pre-declared acceptance tightens PARTIAL-CONDITION
   specification and surfaces C-35 candidate: Auditor pre-declaration block
2. **phrasing-register** (V-02) — conversational imperative throughout; all
   CONSTRAINT/INVARIANT/PRECONDITION labels replaced with plain directive prose; structural
   contract identical to R8 V-05; tests whether formal register labels are load-bearing for
   structural scan detectability (C-27, C-28 require named structural blocks)
3. **inertia-framing** (V-03) — unnamed/implicit Status-Quo competitor; no "THE STATUS-QUO
   RUBRIC:" block at the top; discrimination requirement stated as a quality constraint only;
   INERTIA-RECORD and CALIBRATION-PAIR blocks preserved but reference "a generic rubric" not
   a named competitor; tests whether named-competitor framing is load-bearing for CALIBRATION-
   PAIR calibration quality (C-02 regression probe)

Two combinations:
4. **role-sequence × phrasing-register** (V-04) — Auditor Pre-Declaration + conversational
   register; tests whether the structural clarity of Auditor pre-declaration compensates for
   the loss of formal CONSTRAINT/INVARIANT vocabulary
5. **Full accumulation** (V-05) — all three axes; Auditor Pre-Declaration + conversational
   register + unnamed Status-Quo; hardest case for structural detectability; tests whether
   compound variation surfaces signals beyond individual axes or exposes compounding regressions

---

## V-01 — Role Sequence: Auditor Pre-Declaration (Single Axis)

**axis:** role-sequence
**hypothesis:** R8 V-05 runs Author Phase first, then Auditor reviews post-hoc. V-01 inserts
an Auditor Pre-Declaration step before the Author Phase: the Auditor reads the skill spec and
declares acceptance thresholds — what evidence would earn PASS vs. PARTIAL for each essential
criterion position — before any criteria are drafted. The Author Phase then writes each
criterion with explicit reference to the Auditor's pre-declared threshold. Potential new
signal: does pre-declared acceptance produce tighter PARTIAL-CONDITION blocks (C-23) because
the Auditor named the partial-evidence boundary before the Author committed to a criterion?
Potential C-35 candidate: per-position Auditor pre-declaration block (`### AUDITOR-PRE [C-NN]`)
that pairs with the post-hoc Auditor review and makes the acceptance drift detectable by
structural scan. If no new signal: Auditor pre-declaration is functionally equivalent to
post-hoc review for C-23 compliance, and the current role sequence is sufficient. All other
elements identical to R8 V-05 (M-06 in MECHANISMS, Phase 0 label, SV two-source preamble).

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
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-06 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton);
  this mechanism closes the gap left by the Overview-Silent Protocol

**Why six mechanisms plus the Auditor Pre-Declaration and Status-Quo framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the most critical failure. The category gate prevents clustering. The
Auditor table enables cross-criterion analysis. The output skeleton tests mechanism-overview
sufficiency before any phase begins. The Auditor Pre-Declaration step (below) makes the
acceptance threshold for each criterion position explicit before the Author commits to it —
surfacing PARTIAL-credit boundaries before they are needed, not after a criterion is already
written and the partial interpretation is locked in.

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete
- INVARIANT C: `### AUDITOR-PRE [C-NN]` is written for each essential criterion position
  before the Author Phase writes any criterion; the Author reads the AUDITOR-PRE block for
  position N before drafting the criterion at that position

---

### PHASE 0 — OUTPUT SKELETON

**Lifecycle position:** Phase 0 precedes all other phases. No Auditor Pre-Declaration or
Author Phase criterion may be written until Phase 0 is complete.

Construct the complete heading skeleton for your output using only the MECHANISMS section
above (M-01 through M-06). Do not read ahead into the phase instructions. The skeleton is
an executable test of M-06's claim: if you cannot construct the full heading structure from
the MECHANISMS section alone, the overview is incomplete.

The skeleton declares every named section heading your output will contain, organized by
lifecycle position. Use the exact heading patterns from the MECHANISMS section.

```
--- PHASE 0: OUTPUT SKELETON ---

PRE-DECLARATION (Auditor Pre-Declaration Phase — before Author Phase):
  ### AUDITOR PRE-DECLARATION PHASE
  ### AUDITOR-PRE [C-01]
  ### AUDITOR-PRE [C-02]
  [... AUDITOR-PRE for each essential position C-03 through C-0N ...]

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

PRECONDITION for Auditor Pre-Declaration Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No heading in the skeleton was derived from reading phase instructions
      (skeleton built from M-01 through M-06 alone — flag and remove any heading not
      derivable from MECHANISMS)

CONSTRAINT: DO NOT begin the Auditor Pre-Declaration Phase until all three preconditions
are confirmed.

---

### AUDITOR PRE-DECLARATION PHASE

**Role:** Auditor (reading the skill spec before any criteria are drafted)

Read the skill spec. For each essential criterion position (C-01 through C-0N), produce a
pre-declaration block before the Author Phase begins.

CONSTRAINT: produce all AUDITOR-PRE blocks before writing any Author Phase content.
INVARIANT C (restated): `### AUDITOR-PRE [C-NN]` for position N must be present before the
Author drafts the criterion at position N.

For each essential criterion position, identify from the skill spec:
1. What output-contract element does a criterion at this position most need to protect?
2. What would PASS look like for a criterion at this position?
3. What would PARTIAL (0.5 credit) look like — what evidence is present but incomplete?
4. What is the boundary between PARTIAL and FAIL at this position?

```
### AUDITOR-PRE [C-NN]
Position: C-NN (rank-N — [failure mode this position should target])
PASS evidence: [what a fully passing criterion at this position looks like]
PARTIAL evidence: [what earns 0.5 — present but incomplete; boundary: [distinguishing marker]]
FAIL evidence: [what earns 0 — absent or contradicted]
Pre-declared acceptance threshold: [the specific, observable marker that separates PASS from PARTIAL]
```

Produce AUDITOR-PRE blocks for C-01 through C-05 (or however many essential criteria
the Author Phase will write). Use the skill spec — not hypothesis — to ground each block.

**AUDITOR PRE-DECLARATION GATE**

PRECONDITION for Author Phase entry:

- [ ] AUDITOR-PRE blocks present for all anticipated essential criterion positions
- [ ] Each block names a specific PARTIAL evidence boundary (not "somewhat satisfied")
- [ ] Pre-declared acceptance thresholds do not duplicate across positions (each position
      protects a distinct output-contract element)

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

---

### AUTHOR PHASE

Read the skill spec. The Auditor Pre-Declaration blocks above are your acceptance targets.
Answer before writing any criterion:

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

Write essential criteria in severity-rank order: C-01 targets rank-1, C-02 targets rank-2.
Before drafting each criterion, read the corresponding `### AUDITOR-PRE [C-NN]` block.
For each criterion, apply sub-steps 2a–2e in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something all four competitors would miss? Does it satisfy the
PASS evidence declared in `### AUDITOR-PRE [C-NN]`?

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
Auditor-Pre alignment: [confirm: this condition satisfies AUDITOR-PRE [C-NN] PASS evidence —
  "[quoted PASS evidence from pre-declaration]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the condition it would accept for
  any artifact; the competitor's best attempt at this criterion]
GROUNDED: [what your rubric says — the condition the Status-Quo Rubric rejects because
  it names the skill-specific element from INERTIA-RECORD]
PARTIAL-CONDITION: [what earns 0.5 — the evidence boundary declared in AUDITOR-PRE [C-NN];
  must not be identical to the PASS condition or inferrable from it without independent judgment]
```

Note the PARTIAL-CONDITION field: it is grounded in `### AUDITOR-PRE [C-NN]` — the Auditor
declared the partial-evidence boundary before the Author wrote this criterion. Using the
pre-declared boundary closes the gap where partial credit is interpreted subjectively at
evaluation time.

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO and
      Auditor-Pre alignment field populated
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with STATUS-QUO, GROUNDED, and
      PARTIAL-CONDITION fields; written before this gate check (INVARIANT B confirmed satisfied)
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

CONSTRAINT: if fewer than 3 categories present, add or revise criteria in Phase 3.

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
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared skeleton from Phase 0, which records which headings
the builder committed to producing. These sources cover non-overlapping failure classes:
source (1) detects headings required by instructions but absent from output
(**heading-pattern miss** — a Phase 2 forward gate was bypassed); source (2) detects
headings declared by the builder in Phase 0 but absent from output (**builder-commitment
failure** — a commitment was made and not kept).

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

Scan the Author Phase output for section headings matching the patterns below. Pattern
scan only — content not evaluated; a heading is present or absent.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED, PARTIAL-CONDITION),
                                  precedes ### CRITERION [C-NN]
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
invisible to Scan A.

For any missing block found in either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until (1) every required Author Phase heading
pattern from Scan A is confirmed present and correctly ordered, AND (2) every heading
declared in the Phase 0 OUTPUT SKELETON is present in the output (Scan B shows no
builder-commitment failures outstanding).

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks and all `### AUDITOR-PRE [C-NN]` blocks.
Read all of them before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria and Auditor Pre-Declaration blocks.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Pre-Dec Alignment | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|-------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate.
- *Pre-Dec Alignment*: does the CALIBRATION-PAIR PARTIAL-CONDITION match the Auditor-Pre
  boundary declared before drafting? YES/DRIFT. DRIFT requires investigation in the note below.
- *Revised Condition*: required for every YES row in Status-Quo Test; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode. Note any DRIFT entries in Pre-Dec Alignment
and whether drift is substantive (Auditor-Pre threshold was incorrect) or cosmetic (phrasing
differs, intent matches).

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
- [ ] Pre-Dec Alignment column complete; all DRIFT entries resolved or annotated
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared

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
DO NOT collapse to binary counting — reproduce this formula verbatim at every structural
position where a formula appears.

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

## V-02 — Phrasing Register: Conversational Imperative (Single Axis)

**axis:** phrasing-register
**hypothesis:** R8 V-05 uses formal CONSTRAINT/INVARIANT/PRECONDITION/DEFINITION labels
throughout. V-02 replaces every such label with plain imperative prose: "CONSTRAINT: DO NOT
proceed" becomes "Stop here until this is done." INVARIANT A becomes "Never write a criterion
row without the named blocks confirmed above it." PRECONDITION becomes "Before starting:
[list]." The structural contract is identical — same mechanisms, same gates, same required
blocks. Only the label vocabulary changes. Hypothesis: formal labels are load-bearing for
structural scan detectability per C-27 (DISCRIMINATES-BETWEEN blocks) and C-28 (DEPENDS_ON
declarations), which require named structural blocks. If conversational prose causes those
blocks to be unnamed or merged, the scan detects the regression. If no regression: formal
vocabulary is cosmetic and conversational register achieves equivalent structural guarantees.
All other elements identical to R8 V-05 (M-06 in MECHANISMS, Phase 0 label, SV two-source
preamble).

---

You are building a scoring rubric for a Signal skill. The rubric you produce is an objective
function — it tells evaluators exactly what PASS, PARTIAL, and FAIL mean for each quality
dimension of the skill's output. A rubric that could apply to any skill ("the output is
clear and complete") is too weak. Every criterion you write must name something specific to
this skill's output contract that a generic rubric could not replicate.

Think of the weak generic rubric as your competition: "The output is clear, complete, and
well-formatted." Every criterion you write must catch a failure that generic rubric would miss.

This protocol runs through six quality mechanisms. Skipping any mechanism invalidates the
step it governs. Work through them in order.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the generic rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan
- **M-06 — output skeleton:** before any phase begins, the builder constructs the complete
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-06 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton)

Why does this work? Named blocks catch skipped checks. Gates prevent skips. Severity ranking
makes C-01 target the most critical failure. The category gate prevents clustering. The
Auditor table surfaces cross-criterion patterns. The output skeleton tests that the mechanism
overview is self-sufficient: if you can derive the full heading structure from the MECHANISMS
section alone before reading any instructions, the overview is complete.

**Two structural rules — never break these:**

- Rule A: never write a criterion row unless `### INERTIA-RECORD [C-NN]` and
  `### CALIBRATION-PAIR [C-NN]` for that criterion are already present above it
- Rule B: produce the `### CALIBRATION-PAIR [C-NN]` block immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are done

---

### PHASE 0 — OUTPUT SKELETON

Do this first, before anything else. Construct the complete heading skeleton for your output
using only the MECHANISMS section above. Don't read ahead into the phase instructions yet.

This is a test: if the MECHANISMS section is complete, you should be able to list every
section heading your output will contain without reading further. If you can't, the overview
has a gap — same failure mode as a rubric with a missing structural section.

List every named section heading your output will contain, organized by lifecycle position.
Use the exact heading patterns from the MECHANISMS section.

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

Before moving to the Author Phase, confirm:
- The skeleton covers all lifecycle sections above
- Every heading pattern matches what MECHANISMS named
- No heading came from reading the phase instructions (skeleton built from M-01–M-06 only)

Don't start the Author Phase until all three are confirmed. A heading you declare here but
don't produce is a builder-commitment failure. A heading missing from both here and your
output is a heading-pattern miss. These are different problems — Structural Verification
checks them with separate scans.

---

### AUTHOR PHASE

Read the skill spec. Before writing any criterion, answer:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**Failure modes**

List at least three blocking failures and two degrading failures.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Don't move to the severity ranking until you have at least three blocking and two degrading.

**Severity ranking**

Order the blocking failures from most to least critical. Most critical means: this failure
makes the output useless as an objective function even if every other criterion passes.

```
SEVERITY RANK:
1. [most critical — C-01 must target this]
2. [second most critical]
3. [third most critical]
[... all blocking failures ranked]
```

Don't write any criterion until the severity rank is complete.

**Before writing criteria — check four things:**

- At least 3 blocking failures listed? ___
- At least 2 degrading failures listed? ___
- Severity rank covers all blocking failures? ___
- At least 3 distinct categories identifiable (list: ___, ___, ___)? ___

If any is no, fix it before continuing.

**Essential criteria (3–5 criteria)**

Write in severity-rank order. C-01 targets rank-1, C-02 targets rank-2. For each criterion,
work through steps 2a–2d before moving to the next.

**Step 2a — Draft the pass condition.**

Make it specific, observable, verifiable by two independent evaluators. Ask yourself: does
this catch something the generic rubric misses? If a generic rubric could satisfy this
condition, it's too weak — revise.

**Step 2b — Write the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Generic rubric test: Would "the output is clear, complete, and well-formatted" accept
  this condition? [YES / NO]
If YES — revised condition: [revision; loop until NO]
Final condition: [condition the generic rubric rejects]
Skill-specific element: [the count, field name, pattern, or enumeration that makes
  this condition impossible for a generic rubric to replicate]
Severity-rank alignment: [this criterion targets rank-N — "[failure mode]"]
```

The INERTIA-RECORD must come before the CALIBRATION-PAIR. If you write the criterion row
first, you've broken Rule A.

**Step 2c — Write the CALIBRATION-PAIR block. Write it now.**

Write it immediately — not after finishing all INERTIA-RECORD blocks. The reason:
CALIBRATION-PAIR quality depends on having the pass condition active in working memory.
Deferring it even until the next criterion is written is a Rule B violation.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [what the generic rubric would say — its best attempt at this criterion]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
```

**Step 2d — Gate check before recording this criterion.**

Confirm before writing the criterion row:
- `### INERTIA-RECORD [C-NN]` is present above and shows generic rubric test = NO
- `### CALIBRATION-PAIR [C-NN]` is present above and was written before this gate
- Severity-rank alignment field names rank-N

If any is missing or wrong, fix it now. Then record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat steps 2a–2d for each essential criterion, working down the severity rank.

**Recommended and aspirational criteria**

Write 2–3 recommended and 1–2 aspirational criteria.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**Category coverage check**

Before moving to Structural Verification, confirm at least 3 distinct categories are present
across all criteria.

Categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- Categories present: ___________________________
- Count: ___ (need at least 3)

If fewer than 3, add or revise criteria in the aspirational tier before continuing.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

This scan covers Author Phase output only — not Auditor Phase output, which hasn't been
produced yet.

Not in scope here: `### REDUNDANCY-CHECK-TABLE` — that's an Auditor Phase heading.
It gets verified as part of the Auditor Gate later.

**Two independent sources — why two?**

The protocol uses two independent sources of truth for structural checking: (1) the
instruction-derived heading patterns from M-02 and M-05, which tell you what headings the
protocol requires; and (2) the builder-declared skeleton from Phase 0, which records what
headings you committed to producing. These sources catch different problems. Source (1)
catches headings the instructions require that you didn't produce (heading-pattern miss —
you bypassed a Phase 2 gate). Source (2) catches headings you committed to producing but
didn't (builder-commitment failure — you broke your own declaration). The Inline-Scan
Protocol has both scans but lacks this preamble: without naming both sources and declaring
their non-overlapping failure classes, a maintainer can't determine whether collapsing to
one scan destroys a distinct failure class.

**Scan A — instruction-derived patterns (heading-pattern miss detection):**

For each essential criterion C-NN from Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (GENERIC, GROUNDED fields), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Anything missing here is a heading-pattern miss — a Phase 2 gate was bypassed.

**Scan B — Phase 0 skeleton headings (builder-commitment failure detection):**

Check the `### PHASE 0 — OUTPUT SKELETON` produced earlier. Every heading declared there
must appear in the output:

```
- [ ] Every heading declared in Phase 0 skeleton has a corresponding block in the output
```

Anything declared in Phase 0 but absent from output is a builder-commitment failure.
This failure class is invisible to Scan A.

For any missing block: write it now using the exact heading pattern, then re-check.

Don't start the Auditor Phase until: (1) every required Author Phase heading from Scan A
is present and correctly ordered, and (2) every Phase 0 skeleton heading is present in the
output (no builder-commitment failures outstanding).

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read all of them before writing anything.

Write the full Audit Table as a single block after reading all criteria — don't write rows
one at a time.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Generic Rubric Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|---------------------|----------------------|--------------------|-------------------|

For each row:
- *Discriminating Element*: what makes this condition impossible for a generic rubric
  to replicate. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

After the table, write one sentence: scan the Discriminating Element column and note
variety vs. clustering. Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria: is there an output that passes one but fails the other
for a non-trivial reason?

- YES — independent, each adds signal. Keep both.
- NO — redundant. Revise, consolidate, or remove.

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

[Add rows if more than 5 essential criteria.]

Don't continue until all pairs show YES, or NO-flagged pairs are resolved.

**Auditor calibration pair** — for the most critical essential criterion:

```
GENERIC: [condition in generic rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Before producing the Final Rubric, confirm:**

- Audit Table complete with all essential criteria as rows
- Every essential criterion shows generic rubric test = NO (original or revised)
- Discriminating Element filled for every NO-flagged row
- Cross-criterion pattern note written
- C-01 confirmed at rank-1 failure mode
- `### REDUNDANCY-CHECK-TABLE` heading present and all pairs resolved

If any is missing, produce it now.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

DO NOT collapse to binary counting — reproduce this formula verbatim at every structural
position where a formula appears.

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
criterion IDs. Don't use symbolic names as denominators.

Golden: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**Quick checklist**

One line per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Inertia Framing: Implicit Competitor / Unnamed Status-Quo (Single Axis)

**axis:** inertia-framing
**hypothesis:** R8 V-05 prominently names the Status-Quo Rubric at the top, giving it a
dedicated block and referencing it throughout. V-03 removes the named competitor block
entirely. The discrimination requirement is stated as a quality constraint ("every pass
condition must be specific to this skill's output contract") without naming a
competing protocol. INERTIA-RECORD and CALIBRATION-PAIR blocks are preserved, but their
reference is "a generic rubric" (implicit) rather than a named Status-Quo Rubric. Hypothesis:
named-competitor framing is load-bearing for CALIBRATION-PAIR calibration quality (C-02)
because the named competitor anchors the STATUS-QUO field to a concrete formulation — "clear
and complete" is a specific phrase, not just an abstraction. Without a named competitor,
CALIBRATION-PAIR STATUS-QUO fields may drift toward vague generic descriptions that lose
their discrimination signal. Potential regression at C-02 (calibration pair quality). If no
regression: named-competitor framing is a navigational convenience, not a quality requirement.
All other elements identical to R8 V-05 (M-06, Phase 0 label, two-source preamble in SV).

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through six mechanisms with formal invariants. Violating any invariant
invalidates the step it governs. Every pass condition must name a specific count, field,
structural pattern, or enumeration that only the target skill's output contract can supply.
A pass condition that any skill's rubric could satisfy is too weak and must be revised.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan
- **M-06 — output skeleton:** before any phase begins, the builder constructs the complete
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-06 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures distinct from heading-pattern
  misses

**Why six mechanisms?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion analysis. The output skeleton
tests mechanism-overview sufficiency before any phase begins.

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

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment failure**.
A heading absent from both is a **heading-pattern miss**. Structural Verification checks both
failure classes independently.

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

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order. For each criterion, apply sub-steps 2a–2d.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. Ask: could
this condition appear in any rubric for any skill, or does it name something specific to
this skill's output contract? If any rubric could satisfy it, the condition is too generic —
revise until it names a specific count, field, pattern, or enumeration.

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Generic-rubric test: Would a generic rubric ("the output is complete and well-structured")
  accept this condition without modification? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition a generic rubric cannot replicate unchanged]
Skill-specific element: [the count, field name, pattern, or enumeration that anchors
  this condition to this skill's output contract specifically]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [what a generic rubric would say for this criterion — the condition it would
  accept for any well-structured output; name the generic rubric's best formulation]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD;
  a generic rubric cannot replicate this condition without knowing the skill's contract]
```

Note on the GENERIC field: even without a named Status-Quo Rubric, you must still formulate
the weakest acceptable condition for this criterion — the condition that feels adequate but
lacks the skill-specific anchor. The discrimination is between "adequate but generic" and
"precise and skill-specific."

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with generic-rubric test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with GENERIC and GROUNDED fields,
      written before this gate check (INVARIANT B confirmed satisfied)
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

CONSTRAINT: if fewer than 3 categories present, add or revise criteria in Phase 3.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared skeleton from Phase 0, which records which headings
the builder committed to producing. These sources cover non-overlapping failure classes:
source (1) detects headings required by instructions but absent from output
(**heading-pattern miss**); source (2) detects headings declared by the builder in Phase 0
but absent from output (**builder-commitment failure**). Without naming both sources and
declaring their non-overlapping failure classes here, a maintainer cannot determine whether
collapsing to one scan destroys a distinct failure class.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (GENERIC, GROUNDED fields), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss**.

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

Refer to the `### PHASE 0 — OUTPUT SKELETON` produced above. For each heading declared
in the Phase 0 skeleton, confirm it is present in the output:

```
- [ ] Every heading declared in the Phase 0 skeleton has a corresponding block in the output
```

A Phase 0 heading absent from the output is a **builder-commitment failure**.

For any missing block found in either scan: write the block and re-check.

CONSTRAINT: the Auditor Phase cannot begin until both scans clear.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Generic-Rubric Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|---------------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element a generic rubric cannot replicate. Required for
  every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note:**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria: Is there a rubric output that passes one but fails the
other for a non-trivial reason?

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

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in generic rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows generic-rubric test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

DO NOT collapse to binary counting — reproduce this formula verbatim at every structural
position where a formula appears.

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
criterion IDs. DO NOT use symbolic variable names as denominators.

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

## V-04 — Role Sequence × Phrasing Register (Combination)

**axes:** role-sequence × phrasing-register
**hypothesis:** V-01 (Auditor Pre-Declaration) uses formal CONSTRAINT/INVARIANT vocabulary.
V-04 combines V-01's structural addition with V-02's conversational register. The key test:
does the Auditor Pre-Declaration step's value depend on formal label vocabulary, or does
conversational framing preserve its discrimination function? In V-01, the Auditor Pre-
Declaration block is labeled `### AUDITOR-PRE [C-NN]` with PRECONDITION language enforcing
entry. In V-04, the same step uses plain directive prose: "Before drafting any criterion,
declare your acceptance thresholds for each position." Structural commitment survives if
the `### AUDITOR-PRE [C-NN]` heading pattern is preserved even when its surrounding prose
is conversational. Potential compound signal: if the Auditor Pre-Declaration works well with
conversational register and the pre-declared thresholds still tighten PARTIAL-CONDITION
quality, the formal vocabulary in V-01 was navigational, not structural. All other elements
from R8 V-05 preserved (M-06, Phase 0 label, two-source preamble).

---

You are building a scoring rubric for a Signal skill. A rubric that could apply to any
skill is too weak. Every criterion you write must catch a failure that a generic quality
check would miss — something specific to this skill's output contract.

This protocol runs through six quality mechanisms. Work through them in order — skipping
any mechanism invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading content;
  the generic quality check produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan
- **M-06 — output skeleton:** before any phase begins, the builder constructs the complete
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-06 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures distinct from heading-pattern
  misses; this mechanism closes the gap left by the Overview-Silent Protocol

Named blocks catch skipped checks. Gates prevent skips. Severity ranking makes C-01 target
the most critical failure. The category gate prevents clustering. The Auditor table surfaces
cross-criterion patterns. The output skeleton tests that the mechanism overview is complete
before any phase begins. The Auditor Pre-Declaration step (below) declares the acceptance
thresholds for each criterion position before any criteria are drafted, making PARTIAL-credit
boundaries explicit rather than deferred to evaluation time.

**Two structural rules:**

- Rule A: never write a criterion row unless `### INERTIA-RECORD [C-NN]` and
  `### CALIBRATION-PAIR [C-NN]` for that criterion are already present above it
- Rule B: produce `### CALIBRATION-PAIR [C-NN]` immediately after `### INERTIA-RECORD [C-NN]`
  — not after all INERTIA-RECORD blocks are done; Rule B is violated by deferral even if
  block order is preserved

---

### PHASE 0 — OUTPUT SKELETON

Start here. Before anything else, build the complete heading skeleton using only the
MECHANISMS section above. Don't read the phase instructions yet.

If the MECHANISMS section is complete, you can list every section heading your output will
contain without reading further. If you can't, the overview has a gap — this is an
executable test of M-06.

The Phase 0 skeleton includes the Auditor Pre-Declaration headings (declared before any
Author Phase content) plus all Author Phase and verification headings.

```
--- PHASE 0: OUTPUT SKELETON ---

AUDITOR PRE-DECLARATION (before Author Phase):
  ### AUDITOR PRE-DECLARATION PHASE
  ### AUDITOR-PRE [C-01]
  ### AUDITOR-PRE [C-02]
  [... AUDITOR-PRE for each essential position ...]

ESSENTIAL CRITERIA BLOCKS (Author Phase 2):
  ### AUTHOR PHASE
  ### INERTIA-RECORD [C-01]
  ### CALIBRATION-PAIR [C-01]
  ### CRITERION [C-01]
  [... C-02, C-03, ... C-0N ...]

RECOMMENDED & ASPIRATIONAL CRITERIA (Author Phase 3 — table only):
  (none — inline in Phase 3 table)

VERIFICATION PHASES:
  ### STRUCTURAL VERIFICATION
  ### AUDITOR PHASE
  ### REDUNDANCY-CHECK-TABLE
  ### END AUDITOR PHASE

OUTPUT:
  [Final Rubric section]
```

Before moving on, confirm:
- Skeleton covers all lifecycle sections including AUDITOR-PRE headings
- Every heading pattern matches what MECHANISMS named
- No heading came from reading the phase instructions

Don't start the Auditor Pre-Declaration Phase until all three are confirmed.

---

### AUDITOR PRE-DECLARATION PHASE

Do this before the Author Phase. Read the skill spec. For each essential criterion
position (C-01 through C-0N), declare the acceptance thresholds before the Author
drafts that criterion.

Write all AUDITOR-PRE blocks before any Author Phase content. For each position:

```
### AUDITOR-PRE [C-NN]
Position: C-NN (rank-N — [failure mode this position should target])
PASS evidence: [what a fully passing criterion at this position looks like]
PARTIAL evidence: [what earns 0.5 — present but incomplete; boundary: [distinguishing marker]]
FAIL evidence: [what earns 0 — absent or contradicted]
Acceptance threshold: [the specific observable marker separating PASS from PARTIAL]
```

Write AUDITOR-PRE blocks for C-01 through C-05 (or however many essential criteria the
Author will write). Ground each block in the skill spec, not hypothesis.

After writing all AUDITOR-PRE blocks, check:
- AUDITOR-PRE present for all anticipated essential positions
- Each block names a specific PARTIAL evidence boundary
- No two positions share the same acceptance threshold (each protects a distinct element)

Don't start the Author Phase until all three are confirmed.

---

### AUTHOR PHASE

Read the skill spec. The AUDITOR-PRE blocks above are your acceptance targets. Before
writing any criterion, answer:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**Failure modes**

List at least three blocking and two degrading.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Don't move to severity ranking until you have at least three blocking and two degrading.

**Severity ranking**

Order the blocking failures from most to least critical.

```
SEVERITY RANK:
1. [most critical — C-01 must target this]
2. [second most critical]
3. [third most critical]
[... all blocking failures ranked]
```

Before writing criteria, confirm:
- 3+ blocking failures listed
- 2+ degrading failures listed
- Severity rank covers all blocking failures
- 3+ distinct output-contract categories identifiable (list: ___, ___, ___)

If anything is missing, fix it before continuing.

**Essential criteria (3–5)**

Write in severity-rank order. Before drafting each criterion, read `### AUDITOR-PRE [C-NN]`
for that position. Apply steps 2a–2d for each criterion.

**Step 2a — Draft the pass condition.**

Make it specific, observable, verifiable by two independent evaluators. Does it satisfy the
PASS evidence from `### AUDITOR-PRE [C-NN]`? If a generic rubric could satisfy it, revise.

**Step 2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would "the output is clear, complete, and well-formatted" accept this
  condition? [YES / NO]
If YES — revised condition: [revision; loop until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field name, pattern, or enumeration specific to this skill]
Severity-rank alignment: [this criterion targets rank-N — "[failure mode]"]
Auditor-Pre alignment: [this condition satisfies AUDITOR-PRE [C-NN] PASS evidence —
  "[quoted from pre-declaration]"]
```

This block must come before CALIBRATION-PAIR (Rule A).

**Step 2c — CALIBRATION-PAIR block. Write it now.**

Write immediately after step 2b. Don't defer (Rule B).

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — its best attempt at this criterion]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
PARTIAL-CONDITION: [what earns 0.5 — the evidence boundary from AUDITOR-PRE [C-NN];
  must not be identical to the PASS condition or derivable from it without judgment]
```

**Step 2d — Gate check.**

Confirm before writing the criterion row:
- INERTIA-RECORD present above with Status-Quo test = NO and Auditor-Pre alignment filled
- CALIBRATION-PAIR present above with STATUS-QUO, GROUNDED, and PARTIAL-CONDITION fields
- CALIBRATION-PAIR was written before this check (not deferred)
- Severity-rank alignment confirmed

If anything is missing or wrong, fix it now. Then:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat steps 2a–2d for each essential criterion, working down the severity rank.

**Recommended and aspirational criteria**

Write 2–3 recommended and 1–2 aspirational.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**Category coverage check**

At least 3 distinct categories across all criteria.

- Categories present: ___________________________
- Count: ___

If fewer than 3, add or revise before continuing.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Covers Author Phase output only. Auditor Phase output hasn't been produced yet.

Out of scope: `### REDUNDANCY-CHECK-TABLE` — verified at Auditor Gate.

**Two independent sources — why two?**

This scan uses two independent sources of truth: (1) the instruction-derived heading
patterns from M-02 and M-05 — what headings the protocol requires; and (2) the
builder-declared skeleton from Phase 0 — what headings you committed to producing. These
sources catch non-overlapping problems. Source (1) catches headings the instructions require
that you didn't produce (heading-pattern miss). Source (2) catches headings you declared in
Phase 0 but didn't produce (builder-commitment failure). Without naming both sources and
their distinct failure classes, a maintainer can't tell whether collapsing to one scan would
destroy a failure-class distinction.

**Scan A — instruction-derived patterns (heading-pattern miss detection):**

For each essential criterion C-NN from Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED, PARTIAL-CONDITION),
                                  precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Also confirm AUDITOR-PRE blocks are present for all essential positions:

```
- [ ] ### AUDITOR-PRE [C-NN]      present for each essential criterion position
```

Missing Scan A heading = heading-pattern miss.

**Scan B — Phase 0 skeleton headings (builder-commitment failure detection):**

Check `### PHASE 0 — OUTPUT SKELETON`. Every heading declared there must be present:

```
- [ ] Every heading from the Phase 0 skeleton has a corresponding block in the output
```

Missing Scan B heading = builder-commitment failure. Invisible to Scan A.

For any missing block: write it, then re-check.

Don't start the Auditor Phase until both scans clear.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks and all `### AUDITOR-PRE [C-NN]` blocks.
Read all of them before writing anything.

Write the full Audit Table as one block after reading everything — no row-by-row writing.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Pre-Dec Alignment | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|-------------------|--------------------|-------------------|

Columns:
- *Discriminating Element*: what makes this condition unreplicable by the Status-Quo Rubric.
- *Pre-Dec Alignment*: does CALIBRATION-PAIR PARTIAL-CONDITION match the Auditor-Pre boundary?
  YES / DRIFT. Note DRIFT entries in the cross-criterion note.
- *Revised Condition*: for every YES Status-Quo Test row.

After the table: one sentence on Discriminating Element variety. Confirm C-01 = rank-1.
Note any DRIFT entries and whether drift is substantive or cosmetic.

### REDUNDANCY-CHECK-TABLE

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

Don't continue until all pairs show YES, or NO-flagged pairs are resolved.

**Auditor calibration pair:**

```
STATUS-QUO: [condition in Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Before producing the Final Rubric:**

- Audit Table complete with all essential criteria
- Every criterion: Status-Quo test = NO
- Discriminating Element filled for all NO rows
- Pre-Dec Alignment complete; DRIFT entries resolved
- Cross-criterion pattern note written
- C-01 confirmed at rank-1
- `### REDUNDANCY-CHECK-TABLE` present and all pairs resolved

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where needed.
Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA**

DO NOT collapse to binary counting — reproduce this formula verbatim at every structural
position where a formula appears.

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace [N_x] with actual counts. Replace [first]/[last] with actual IDs.
Don't use symbolic names as denominators.

Golden: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**Quick checklist:** `- [ ] C-NN: [one-line assertion]` per criterion.

---

## V-05 — Full Accumulation: Role Sequence × Phrasing Register × Inertia Framing

**axes:** role-sequence × phrasing-register × inertia-framing (unnamed Status-Quo)
**hypothesis:** Full combination of V-01 + V-02 + V-03. Auditor Pre-Declaration + conversational
register + unnamed/implicit Status-Quo competitor. This is the hardest case for structural
detectability: no formal CONSTRAINT/INVARIANT labels, no named Status-Quo Rubric, and the
Auditor role is reordered to precede Author. Three compound hypotheses: (1) does Auditor
Pre-Declaration compensate for the loss of named-competitor framing — i.e., does pre-declared
acceptance threshold serve the same anchoring function as "the Status-Quo Rubric would say
X"? (2) does conversational register cause structural block names to weaken (e.g., `### AUDITOR-
PRE [C-NN]` heading drifts to prose description without a scannable heading)? (3) does the
compound of all three changes surface a new signal beyond any single-axis variation — e.g.,
a combined Auditor-Pre / Calibration-Pair convergence check that only appears when the
acceptance threshold must do double duty as both the PARTIAL boundary and the generic-rubric
discrimination anchor? If compound signals emerge that are absent in V-01, V-02, and V-03
independently, they are C-35 batch-2 candidates. If no compound signals: the axes are
independent and v9 Batch 2 confirms the independence structure.

---

You are building a scoring rubric for a Signal skill. The rubric you produce is an objective
function — it tells evaluators exactly what PASS, PARTIAL, and FAIL mean for each quality
dimension of the skill's output. A rubric that could apply to any skill is too weak. Every
criterion must name something specific to this skill's output contract.

This protocol runs through six quality mechanisms. Work through them in order.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading content
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan
- **M-06 — output skeleton:** before any phase begins, the builder constructs the complete
  heading skeleton under `### PHASE 0 — OUTPUT SKELETON` using M-01 through M-06 alone;
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures distinct from heading-pattern
  misses; this mechanism closes the gap left by the Overview-Silent Protocol

Named blocks catch skipped checks. Gates prevent skips. Severity ranking makes C-01 target
the most critical failure. The category gate prevents clustering. The Auditor table surfaces
cross-criterion patterns. The output skeleton tests that the mechanism overview is complete.
The Auditor Pre-Declaration step (below) makes acceptance thresholds explicit before any
criterion is drafted.

**Two structural rules:**

- Rule A: never write a criterion row unless `### INERTIA-RECORD [C-NN]` and
  `### CALIBRATION-PAIR [C-NN]` for that criterion are already present above it
- Rule B: produce `### CALIBRATION-PAIR [C-NN]` immediately after `### INERTIA-RECORD [C-NN]`
  — not deferred; deferral violates Rule B even if block order is preserved

---

### PHASE 0 — OUTPUT SKELETON

Start here. Build the complete heading skeleton using only the MECHANISMS section. Don't
read the phase instructions yet. If the MECHANISMS section is complete, you can list every
heading your output will contain without reading further — this is the M-06 test.

The skeleton includes the Auditor Pre-Declaration phase (before Author Phase), all Author
Phase criterion blocks, verification phases, and the final output section.

```
--- PHASE 0: OUTPUT SKELETON ---

AUDITOR PRE-DECLARATION (runs before Author Phase):
  ### AUDITOR PRE-DECLARATION PHASE
  ### AUDITOR-PRE [C-01]
  ### AUDITOR-PRE [C-02]
  [... AUDITOR-PRE for each essential criterion position ...]

AUTHOR PHASE CONTENT:
  ### AUTHOR PHASE
  ### INERTIA-RECORD [C-01]
  ### CALIBRATION-PAIR [C-01]
  ### CRITERION [C-01]
  [... C-02, C-03, ... C-0N ...]

RECOMMENDED & ASPIRATIONAL (table only, no named blocks):
  (none — inline in Phase 3 table)

VERIFICATION:
  ### STRUCTURAL VERIFICATION
  ### AUDITOR PHASE
  ### REDUNDANCY-CHECK-TABLE
  ### END AUDITOR PHASE

OUTPUT:
  [Final Rubric section]
```

Before continuing, confirm:
- Skeleton covers all sections including AUDITOR-PRE headings
- Every heading matches what MECHANISMS named
- No heading came from reading the phase instructions

Don't start the Auditor Pre-Declaration Phase until all three are confirmed. A heading you
declare here but don't produce is a builder-commitment failure. A heading missing from both
here and your output is a heading-pattern miss. Structural Verification checks these with
separate scans.

---

### AUDITOR PRE-DECLARATION PHASE

Do this before the Author Phase. Read the skill spec. For each essential criterion position,
declare the acceptance thresholds before the Author drafts anything.

Write all `### AUDITOR-PRE [C-NN]` blocks here, before any Author Phase content.

```
### AUDITOR-PRE [C-NN]
Position: C-NN (rank-N — [failure mode this position should target])
PASS evidence: [what fully passing criterion output looks like at this position]
PARTIAL evidence: [what earns 0.5 — present but incomplete; boundary: [distinguishing marker]]
FAIL evidence: [what earns 0 — absent or contradicted at this position]
Acceptance threshold: [specific observable marker separating PASS from PARTIAL]
```

Write AUDITOR-PRE blocks for C-01 through C-05 (or however many essential criteria). Ground
each in the skill spec.

After writing all AUDITOR-PRE blocks, check:
- AUDITOR-PRE present for all anticipated essential criterion positions
- Each block names a specific PARTIAL evidence boundary (not "somewhat satisfied")
- No two positions share the same acceptance threshold

Don't start the Author Phase until all three are confirmed.

---

### AUTHOR PHASE

Read the skill spec. The AUDITOR-PRE blocks above are your targets. Before writing any
criterion, answer:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**Failure modes**

At least three blocking, two degrading.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Don't move to severity ranking until you have at least three blocking and two degrading.

**Severity ranking**

Order the blocking failures from most to least critical.

```
SEVERITY RANK:
1. [most critical — C-01 must target this]
2. [second most critical]
3. [third most critical]
[... all blocking failures]
```

Before writing criteria, check four things:
- 3+ blocking failures listed
- 2+ degrading failures listed
- Severity rank covers all blocking failures
- 3+ distinct output-contract categories identifiable (list: ___, ___, ___)

Fix anything missing before continuing.

**Essential criteria (3–5)**

Write in severity-rank order. Before drafting each criterion, read `### AUDITOR-PRE [C-NN]`.
Apply steps 2a–2d for each criterion.

**Step 2a — Draft the pass condition.**

Specific, observable, verifiable by two independent evaluators. Does it satisfy the PASS
evidence from `### AUDITOR-PRE [C-NN]`? Would any generic rubric satisfy this condition
without naming something specific to this skill? If yes, it's too weak — revise.

**Step 2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Generic test: Would a generic rubric ("complete and well-structured") accept this
  condition without modification? [YES / NO]
If YES — revised condition: [revision; loop until NO]
Final condition: [condition a generic rubric cannot replicate unchanged]
Skill-specific element: [count, field name, pattern, or enumeration specific to this skill]
Severity-rank alignment: [this criterion targets rank-N — "[failure mode]"]
Auditor-Pre alignment: [satisfies AUDITOR-PRE [C-NN] PASS evidence — "[quoted threshold]"]
```

This block must come before CALIBRATION-PAIR (Rule A).

**Step 2c — CALIBRATION-PAIR block. Write it now.**

Immediately after step 2b. Don't defer (Rule B violation even if order preserved later).

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [what a generic rubric would say for this criterion — its best attempt without
  knowing the skill's contract; the condition it would accept for any artifact]
GROUNDED: [what your rubric says — names the skill-specific element from INERTIA-RECORD]
PARTIAL-CONDITION: [what earns 0.5 — the evidence boundary from AUDITOR-PRE [C-NN];
  must not be identical to the PASS condition or derivable from it without judgment;
  the acceptance threshold declared before this criterion was drafted]
```

On the GENERIC field: without a named Status-Quo Rubric, you must still formulate the
weakest adequate condition for this criterion — the condition that feels sufficient but lacks
the skill-specific anchor. The Auditor Pre-Declaration's acceptance threshold (in
`### AUDITOR-PRE [C-NN]`) grounds the PARTIAL-CONDITION field independently of a named
generic competitor.

**Step 2d — Gate check before recording the criterion.**

Confirm:
- INERTIA-RECORD present with generic test = NO and Auditor-Pre alignment filled
- CALIBRATION-PAIR present with GENERIC, GROUNDED, and PARTIAL-CONDITION fields
- CALIBRATION-PAIR was written before this check (not deferred)
- Severity-rank alignment confirmed

Fix anything missing, then:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat steps 2a–2d for each essential criterion, working down the severity rank.

**Recommended and aspirational criteria**

2–3 recommended, 1–2 aspirational.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**Category coverage check**

At least 3 distinct categories across all criteria.

- Categories present: ___________________________
- Count: ___

If fewer than 3, add or revise before continuing.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Covers Author Phase output only. Auditor Phase output hasn't been produced yet.
`### REDUNDANCY-CHECK-TABLE` is not in scope here — verified at the Auditor Phase gate.

**Two independent sources — why two?**

This scan uses two independent sources of truth: (1) the instruction-derived heading
patterns from M-02 and M-05 — what headings the protocol requires; and (2) the
builder-declared skeleton from Phase 0 — what headings you committed to producing. These
catch non-overlapping problems. Source (1): headings the protocol requires that you didn't
produce (heading-pattern miss). Source (2): headings you declared in Phase 0 that you
didn't produce (builder-commitment failure). Without naming both sources and their distinct
failure classes, a maintainer can't tell whether collapsing to one scan destroys a distinct
failure class.

**Scan A — instruction-derived patterns (heading-pattern miss detection):**

For each essential criterion C-NN from Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (GENERIC, GROUNDED, PARTIAL-CONDITION fields),
                                  precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Also confirm:
```
- [ ] ### AUDITOR-PRE [C-NN]      present for each essential criterion position
```

Missing Scan A heading = heading-pattern miss.

**Scan B — Phase 0 skeleton headings (builder-commitment failure detection):**

Every heading declared in `### PHASE 0 — OUTPUT SKELETON` must appear in the output:

```
- [ ] Every Phase 0 skeleton heading has a corresponding block in the output
```

Missing Scan B heading = builder-commitment failure. Invisible to Scan A.

For any missing block: write it now, then re-check.

Don't start the Auditor Phase until both scans clear.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` and all `### AUDITOR-PRE [C-NN]` blocks. Read everything
before writing anything.

Write the full Audit Table as one block — not row by row.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Generic Test | Discriminating Element | Pre-Dec Alignment | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|-------------------|--------------------|-------------------|

Columns:
- *Discriminating Element*: what makes this condition specific to this skill's contract.
- *Pre-Dec Alignment*: does the CALIBRATION-PAIR PARTIAL-CONDITION match the acceptance
  threshold from `### AUDITOR-PRE [C-NN]`? YES / DRIFT.
- *Revised Condition*: for any YES generic test row.

After the table: one sentence on Discriminating Element variety. Confirm C-01 = rank-1.
Note any DRIFT entries and whether the drift is substantive or cosmetic.

Check also: does the Auditor Pre-Declaration threshold (PARTIAL evidence boundary) appear
in the CALIBRATION-PAIR PARTIAL-CONDITION field without being simply copied from the
AUDITOR-PRE block? This compound test — pre-declared boundary still grounded in criterion-
specific evidence — is the V-05 convergence signal to watch.

### REDUNDANCY-CHECK-TABLE

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

Don't continue until all pairs show YES or NO-flagged pairs are resolved.

**Auditor calibration pair — for the most critical essential criterion:**

```
GENERIC: [condition in generic rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Before producing the Final Rubric:**

- Audit Table complete with all essential criteria
- Every criterion: generic test = NO
- Discriminating Element filled for all NO rows
- Pre-Dec Alignment complete; DRIFT entries noted or resolved
- Convergence check complete (see above)
- Cross-criterion pattern note written
- C-01 confirmed at rank-1
- `### REDUNDANCY-CHECK-TABLE` present and all pairs resolved

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where needed.
Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA**

DO NOT collapse to binary counting — reproduce this formula verbatim at every structural
position where a formula appears.

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace [N_x] with actual counts. Replace [first]/[last] with actual IDs. Don't use symbolic
names as denominators.

Golden: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**Quick checklist:** `- [ ] C-NN: [one-line assertion]` per criterion.
