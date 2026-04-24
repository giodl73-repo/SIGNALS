# quest-rubric Variate — Round 9 against rubric v9

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v9 (C-01 through C-34; essential C-01–C-05)
**Round:** R9 — 3 single-axis + 2 combination

**Round 9 design note:** R8 produced three excellence signals absorbed into v9 as aspirational
criteria C-32, C-33, C-34 — all originating from R8 V-05. C-32 requires the MECHANISMS
overview to name M-06 (the pre-phase skeleton step) with its heading pattern. C-33 requires
Structural Verification to open with a two-source preamble naming both sources and their
non-overlapping failure classes before the scans begin. C-34 requires the pre-phase step
to be labeled Phase 0 (not merely `### OUTPUT SKELETON`).

R8 V-05 scores 100.0 under v9. It is the anchor for R9.

**R8 V-05 score under v9:**
- Essential (5/5): all pass → 60
- Recommended (3/3): all pass → 30
- Aspirational (26/26): all pass (C-32, C-33, C-34 all pass — they originated in V-05)
  → 26/26 × 10 = 10.0
- **Composite: 100.0 → Golden. No gaps.**

R9 explores three axes not yet exhausted at the v9 discrimination frontier:

1. **inertia-framing** — whether naming three specific competitors that fail on exactly
   C-32, C-33, C-34 respectively produces a new excellence signal around competitor-to-
   mechanism mapping (potential C-35 candidate: per-mechanism competitor defeat annotation)
2. **output-format** — whether reformatting the Phase 0 skeleton as a flat annotated
   checklist (vs tier-structured code-block) produces a signal around operational skeleton
   use during output construction (potential C-36 candidate: skeleton used as live tick list)
3. **lifecycle-emphasis** — whether adding a Phase 0 M-06 Self-Test sub-step (builder maps
   each heading to its source mechanism) produces a signal around mechanism-attribution
   completeness (potential C-37 candidate: heading-to-mechanism attribution map in Phase 0)

**Axis selection for R9:**

Three single axes:
1. **inertia-framing** (V-01) — three-gap competitor framing naming Overview-Silent,
   Inline-Scan, and Pre-Phase competitors; everything else identical to R8 V-05
2. **output-format** (V-02) — flat annotated checklist skeleton replacing tier-structured
   code-block; everything else identical to R8 V-05
3. **lifecycle-emphasis** (V-03) — Phase 0 M-06 Self-Test sub-step added after skeleton
   construction; everything else identical to R8 V-05

Two combinations:
4. **inertia-framing × lifecycle-emphasis** (V-04) — three-gap competitors + Phase 0
   self-test; tests whether competitor-defeat annotation emerges when the self-test makes
   mechanism attribution explicit
5. **Full accumulation** (V-05) — all three axes; tests whether flat checklist skeleton +
   self-test + three-gap competitors produces compound structural signals beyond C-37

---

## V-01 — Inertia Framing: Three-Gap Competitors (Single Axis)

**axis:** inertia-framing
**hypothesis:** R8 named one Status-Quo competitor throughout. V-01 adds three specific
named competitors — Overview-Silent Protocol (fails C-32), Inline-Scan Protocol (fails C-33),
Pre-Phase Protocol (fails C-34) — each placed at the precise moment the relevant mechanism
is introduced. Naming them forces the builder to explicitly distinguish their rubric from
each gap. If a new excellence signal emerges — e.g., a per-competitor defeat record
annotating which mechanism closes each gap — it is the R9 C-35 candidate. If no new signal
appears, the three-competitor framing is equivalent to the single-competitor framing for
the C-32/C-33/C-34 layer. All other elements identical to R8 V-05 (M-06 in MECHANISMS,
Phase 0 label, SV two-source preamble).

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

Three more specific competitors also fail — each on a narrower gap:

- **Overview-Silent Protocol:** has five mechanisms (M-01 through M-05) and a pre-phase
  skeleton step, but the skeleton step is not named in the MECHANISMS overview. A builder
  reading only the orientation section cannot derive the full heading skeleton without
  reading phase instructions. The Status-Quo Rubric cannot detect this gap; the
  Overview-Silent Protocol satisfies it.

- **Inline-Scan Protocol:** has Phase 0, M-06 in MECHANISMS, and two independent scans in
  Structural Verification (Scan A: instruction-derived patterns; Scan B: skeleton-declared
  headings). But Structural Verification begins directly with Scan A — no preamble names
  both sources or declares the non-overlapping failure classes. A maintainer reading the
  SV section cannot determine whether collapsing to one scan destroys a distinct failure
  class without reading both scan definitions and inferring the design intent.

- **Pre-Phase Protocol:** has M-06 in MECHANISMS, and an SV two-source preamble, but the
  pre-phase skeleton step is labeled `### OUTPUT SKELETON` rather than
  `### PHASE 0 — OUTPUT SKELETON`. The complete phase sequence (Phase 0 → Author Phase →
  Structural Verification → Auditor Phase) is not readable from section headings alone:
  `### OUTPUT SKELETON` does not anchor the pre-phase boundary as a scannable lifecycle
  position. C-26 (phase transitions marked by named section headings) cannot be verified
  by heading scan at the Phase 0 boundary.

Your protocol must go further than all four competitors.

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
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton);
  this mechanism closes the gap left by the Overview-Silent Protocol

**Why six mechanisms plus the four-competitor framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion analysis. The output
skeleton serves as an executable test of mechanism-overview sufficiency: if the overview
is complete, the builder can construct the full heading structure before reading a single
phase instruction. The Status-Quo Rubric framing and the three specific competitors make
the discrimination requirement concrete at four levels.

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
the MECHANISMS section alone, the overview is incomplete — and your rubric falls into the
same gap as the Overview-Silent Protocol.

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
      (skeleton built from M-01 through M-06 alone — flag and remove any heading not
      derivable from MECHANISMS)

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

Write essential criteria in severity-rank order: C-01 targets rank-1, C-02 targets rank-2.
For each criterion, apply sub-steps 2a–2d in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something all four competitors would miss?

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
satisfies structural ordering while violating INVARIANT B. Do not defer. Batch production
is a protocol violation even if block order is preserved.

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
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared skeleton from Phase 0, which records which headings
the builder committed to producing. These sources cover non-overlapping failure classes:
source (1) detects headings required by instructions but absent from output
(**heading-pattern miss** — a Phase 2 forward gate was bypassed); source (2) detects
headings declared by the builder in Phase 0 but absent from output (**builder-commitment
failure** — a commitment was made and not kept). The Inline-Scan Protocol has both scans
but not this preamble: without naming both sources and their failure classes, a maintainer
cannot determine whether collapsing to one scan destroys a distinct failure class.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

Scan the Author Phase output for section headings matching the patterns below. Pattern
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

## V-02 — Output Format: Flat Annotated Checklist Skeleton (Single Axis)

**axis:** output-format
**hypothesis:** R8 V-05 uses a tier-structured code-block for the Phase 0 skeleton, organized
into labeled sections (ESSENTIAL CRITERIA BLOCKS / VERIFICATION PHASES / OUTPUT SECTION).
V-02 replaces this with a flat annotated checklist: every heading appears as a `- [ ]`
item in a single ordered list, with a source annotation `[M-NN]` after each entry marking
which MECHANISM named it. Hypothesis: the flat checklist makes the skeleton usable as a
live tick-off tool during output construction — the builder can check each item as it is
produced, making skeleton tracking operational rather than declarative. If a new excellence
signal emerges around ticking off the checklist during output production (not just at Phase 0
declaration), it is the R9 C-36 candidate. If no new signal: flat checklist format is
functionally equivalent to tier-structured code-block for C-32/C-33/C-34 compliance.
All other elements identical to R8 V-05.

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
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton)

**Why six mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion pattern analysis. The
output skeleton serves as an executable test of mechanism-overview sufficiency: if the
overview is complete, the builder can construct the full heading structure before reading
a single phase instruction. The Status-Quo Rubric framing makes the discrimination
requirement concrete throughout.

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

Produce the skeleton as a flat annotated checklist. For each heading, record the mechanism
that named it in `[M-NN]` notation. Use `[C-0N]` as a placeholder where the criterion count
is not yet known. Mark each item with `- [ ]` — you will tick each item as you produce
the corresponding block in your output.

```
Phase 0 skeleton — tick each as produced:

- [ ] ### PHASE 0 — OUTPUT SKELETON  [M-06]
- [ ] ### AUTHOR PHASE               [M-02, M-03]
- [ ] ### INERTIA-RECORD [C-01]      [M-02]
- [ ] ### CALIBRATION-PAIR [C-01]    [M-02]
- [ ] ### CRITERION [C-01]           [M-02]
- [ ] [... repeat INERTIA-RECORD / CALIBRATION-PAIR / CRITERION for C-02 through C-0N ...]
- [ ] ### STRUCTURAL VERIFICATION    [M-06]
- [ ] ### AUDITOR PHASE              [M-05]
- [ ] ### REDUNDANCY-CHECK-TABLE     [M-05]
- [ ] ### END AUDITOR PHASE          [M-05]
- [ ] [Final Rubric section]
```

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Checklist is complete with source annotations for every entry
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No heading in the checklist was derived from reading phase instructions
      (checklist built from M-01 through M-06 alone — flag and remove any heading not
      attributable to a named MECHANISM)

CONSTRAINT: DO NOT begin the Author Phase until all three preconditions are confirmed.

As you produce each block in your output, tick the corresponding checklist item. A heading
declared in Phase 0 but absent from the output is a **builder-commitment failure**. A
heading absent from both the checklist and the output is a **heading-pattern miss**. These
are distinct failure classes checked by independent scans in Structural Verification.

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
proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared checklist from Phase 0, which records which headings
the builder committed to producing. These sources cover non-overlapping failure classes:
source (1) detects headings required by instructions but absent from output
(**heading-pattern miss**); source (2) detects headings declared in Phase 0 but absent
from output (**builder-commitment failure**). The two scans below correspond to these two
sources.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

Scan the Author Phase output for section headings matching the patterns below.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss**.

**Scan B — Phase 0 checklist-declared headings (builder-commitment failure detection):**

Refer to the flat checklist produced in `### PHASE 0 — OUTPUT SKELETON`. For each entry
in the checklist, confirm the corresponding block is present in the output:

```
- [ ] Every heading from the Phase 0 checklist has a corresponding block in the output
```

A checklist entry absent from the output is a **builder-commitment failure**. This failure
class is invisible to Scan A.

For any missing block found in either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until (1) every required Author Phase heading
pattern from Scan A is confirmed present and correctly ordered, AND (2) every heading in
the Phase 0 checklist is present in the output (Scan B shows no builder-commitment failures
outstanding).

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

Replace each [N_x] with the actual criterion count. DO NOT use symbolic variable names as
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

## V-03 — Lifecycle Emphasis: Phase 0 M-06 Self-Test (Single Axis)

**axis:** lifecycle-emphasis
**hypothesis:** R8 V-05 instructs the builder to derive the skeleton from MECHANISMS alone
but does not verify the derivation explicitly. V-03 adds a Phase 0 M-06 Self-Test sub-step:
after constructing the skeleton, the builder maps each heading to the MECHANISM that named
it. Any heading that cannot be attributed to a named MECHANISM is flagged — either the
MECHANISMS section is incomplete (gap in the overview) or the heading was imported from
phase instructions in violation of the Phase 0 constraint. Hypothesis: the self-test makes
M-06 sufficiency auditable from Phase 0 output alone. If a new excellence signal emerges
around the mechanism-attribution record — e.g., a heading-to-mechanism mapping table that
could be used to verify MECHANISMS completeness — it is the R9 C-37 candidate. The
self-test also operationalizes C-32 at the builder level: producing the attribution map
requires that M-06 be explicitly named in MECHANISMS, otherwise `### PHASE 0` itself has
no mechanism to attribute. All other elements identical to R8 V-05.

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
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton)

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

**PHASE 0 M-06 SELF-TEST**

After producing the skeleton, verify M-06's sufficiency claim. For each heading in the
skeleton, identify which MECHANISM named it. Produce the attribution table:

```
Heading-to-Mechanism Attribution:
  ### PHASE 0 — OUTPUT SKELETON      → [M-NN]
  ### AUTHOR PHASE                   → [M-NN]
  ### INERTIA-RECORD [C-NN]          → [M-NN]
  ### CALIBRATION-PAIR [C-NN]        → [M-NN]
  ### CRITERION [C-NN]               → [M-NN]
  ### STRUCTURAL VERIFICATION        → [M-NN]
  ### AUDITOR PHASE                  → [M-NN]
  ### REDUNDANCY-CHECK-TABLE         → [M-NN]
  ### END AUDITOR PHASE              → [M-NN]
```

For each heading, fill in the MECHANISM ID that names it. If a heading has no source
MECHANISM, flag it:

```
- Unattributed headings: [list or "none"]
- If any unattributed: either add a missing MECHANISM to the overview, or remove the heading
```

SELF-TEST PRECONDITION: all skeleton headings attributed to a named MECHANISM before
proceeding. An unattributed heading indicates the MECHANISMS section is structurally
incomplete — the builder has imported a heading from phase instructions in violation of
M-06's constraint.

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] M-06 Self-Test complete: every heading attributed to a named MECHANISM
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No unattributed headings flagged

CONSTRAINT: DO NOT begin the Author Phase until all four preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure** — distinct from a **heading-pattern miss** (absent from output and absent from
the skeleton because it was never declared). Structural Verification distinguishes them
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
is false.

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

CONSTRAINT: if fewer than 3 categories present, add or revise criteria before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared skeleton from Phase 0, which records which headings
the builder committed to producing. These sources cover non-overlapping failure classes:
source (1) detects **heading-pattern misses** (required by instructions, absent from
output); source (2) detects **builder-commitment failures** (declared in Phase 0, absent
from output). The Phase 0 M-06 Self-Test already verified that every skeleton heading is
attributable to a named MECHANISM; Scan B now verifies that every attributed heading was
actually produced.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A heading absent from Scan A is a **heading-pattern miss**.

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

Refer to the `### PHASE 0 — OUTPUT SKELETON` and its M-06 Self-Test attribution table.
For each heading declared in the skeleton:

```
- [ ] Every heading from the Phase 0 skeleton has a corresponding block in the output
```

A skeleton heading absent from the output is a **builder-commitment failure** — invisible
to Scan A.

For any missing block from either scan: write the block using the exact heading pattern
and re-check.

CONSTRAINT: the Auditor Phase cannot begin until Scan A and Scan B both show all required
headings confirmed present.

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

Replace each [N_x] with the actual criterion count. DO NOT use symbolic variable names as
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

## V-04 — Inertia Framing × Lifecycle Emphasis (Combination)

**axis:** inertia-framing × lifecycle-emphasis
**hypothesis:** V-01 names three specific competitors (Overview-Silent, Inline-Scan,
Pre-Phase) at the mechanism level. V-03 adds a Phase 0 M-06 Self-Test that maps every
skeleton heading to its source mechanism. V-04 combines both: the three-competitor framing
contextualizes the self-test as a mechanism-defeat audit — the builder not only maps
headings to mechanisms but can annotate which competitor each mechanism-attribution defeats.
Hypothesis: the combination produces a compound excellence signal where the self-test
attribution table is enriched with competitor-defeat annotations (e.g.,
`### PHASE 0 — OUTPUT SKELETON → M-06 [defeats Pre-Phase Protocol]`). If this annotation
emerges in V-04 output, it is the R9 C-35+C-37 compound candidate. Failure condition: if
the two axes interact negatively — three competitors crowding the orientation section while
the self-test adds Phase 0 weight — investigate whether the total Phase 0 overhead reduces
Author Phase quality (C-01 through C-05 pass rates).

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

Three more specific competitors also fail — each on a narrower gap:

- **Overview-Silent Protocol:** has five mechanisms (M-01 through M-05) and a pre-phase
  skeleton step, but the skeleton step is not named in the MECHANISMS overview. A builder
  reading only the orientation section cannot derive the full heading skeleton without
  reading phase instructions.

- **Inline-Scan Protocol:** has Phase 0, M-06 in MECHANISMS, and two independent scans in
  Structural Verification. But Structural Verification begins directly with Scan A — no
  preamble names both sources or declares the non-overlapping failure classes before the
  scans begin.

- **Pre-Phase Protocol:** has M-06 in MECHANISMS and an SV two-source preamble, but the
  pre-phase step is labeled `### OUTPUT SKELETON` rather than `### PHASE 0 — OUTPUT SKELETON`.
  The complete phase sequence is not readable from section headings alone.

Your protocol must exceed all four competitors.

This protocol enforces quality through six mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition any of the four competitors would also accept is too weak.

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
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton);
  this mechanism closes the gap left by the Overview-Silent Protocol; the Phase 0 label
  closes the gap left by the Pre-Phase Protocol

**Why six mechanisms plus the four-competitor framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional. The category gate
prevents clustering. The Auditor table enables cross-criterion analysis. The output
skeleton is an executable test of M-06 sufficiency. Naming four competitors makes the
discrimination requirement concrete at four levels: generic quality (Status-Quo), mechanism
visibility (Overview-Silent), scan architecture (Inline-Scan), and lifecycle labeling
(Pre-Phase).

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
the MECHANISMS section alone, the overview is incomplete — and your rubric falls into the
same gap as the Overview-Silent Protocol.

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

**PHASE 0 M-06 SELF-TEST**

After producing the skeleton, verify M-06's sufficiency claim. For each heading in the
skeleton, identify which MECHANISM named it. Produce the attribution table:

```
Heading-to-Mechanism Attribution:
  ### PHASE 0 — OUTPUT SKELETON      → [M-NN]  [competitor defeated: ___]
  ### AUTHOR PHASE                   → [M-NN]  [competitor defeated: ___]
  ### INERTIA-RECORD [C-NN]          → [M-NN]  [competitor defeated: ___]
  ### CALIBRATION-PAIR [C-NN]        → [M-NN]  [competitor defeated: ___]
  ### CRITERION [C-NN]               → [M-NN]  [competitor defeated: ___]
  ### STRUCTURAL VERIFICATION        → [M-NN]  [competitor defeated: ___]
  ### AUDITOR PHASE                  → [M-NN]  [competitor defeated: ___]
  ### REDUNDANCY-CHECK-TABLE         → [M-NN]  [competitor defeated: ___]
  ### END AUDITOR PHASE              → [M-NN]  [competitor defeated: ___]
```

Fill in each [M-NN] with the mechanism that names the heading. Fill in each
[competitor defeated] with the named competitor whose gap this mechanism closes, or
"Status-Quo" if the heading exceeds only the baseline competitor.

If a heading has no source mechanism, flag it — the MECHANISMS section is incomplete.

SELF-TEST PRECONDITION: all skeleton headings attributed and competitor-defeat annotations
complete before proceeding.

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Skeleton is complete and covers all lifecycle sections above
- [ ] M-06 Self-Test complete: every heading attributed, competitor defeats annotated
- [ ] Every heading pattern matches exactly the pattern named in the MECHANISMS section
- [ ] No unattributed headings flagged

CONSTRAINT: DO NOT begin the Author Phase until all four preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure**. A heading absent from both the skeleton and the output is a **heading-pattern
miss**. Structural Verification distinguishes them using two independent scans.

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

DEFINITION (most critical): the failure that makes the output non-functional regardless of
all other criteria passing.

```
SEVERITY RANK:
1. [most critical — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode ordered.

**AUTHOR PHASE 2 ENTRY GATE**

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

For each criterion, apply sub-steps 2a–2d in severity-rank order.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. Does it
catch something all four competitors would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would "the output is clear, complete, and well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [count, field name, pattern, or enumeration]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated): produce this block now — do not batch calibration pairs after all
inertia records are complete.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [competitor's best attempt]
GROUNDED: [your condition naming the skill-specific element]
```

**Sub-step 2d — Per-criterion forward gate.**

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written before this gate (INVARIANT B satisfied)
- [ ] Severity-rank alignment confirmed

After confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

- [ ] Categories present: ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: fewer than 3 categories → add or revise before Structural Verification.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

**Out of scope:** `### REDUNDANCY-CHECK-TABLE` — deferred to AUDITOR GATE.

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared skeleton from Phase 0 (verified by the M-06 Self-Test
attribution table), which records which headings the builder committed to producing. These
sources cover non-overlapping failure classes: source (1) detects **heading-pattern misses**
(required by instructions, absent from output); source (2) detects **builder-commitment
failures** (declared in Phase 0, absent from output). The Inline-Scan Protocol has both
scans but not this preamble: without naming both sources and their failure classes, a
maintainer cannot determine whether collapsing to one scan destroys a distinct failure class.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

**Scan B — Phase 0 skeleton-declared headings (builder-commitment failure detection):**

```
- [ ] Every heading from the Phase 0 skeleton has a corresponding block in the output
```

For any missing block from either scan: write the block and re-check.

CONSTRAINT: Auditor Phase cannot begin until both scans complete with no missing headings.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks before writing any output.

CONSTRAINT: write the full Audit Table after reading all criteria — no row-at-a-time.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:** one sentence on discriminating element variety. Confirm
C-01 targets rank-1.

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

**REDUNDANCY GATE:**
- [ ] All pairs evaluated; all YES or NO-flagged pairs resolved

**Auditor Calibration Pair:**

```
STATUS-QUO: [C-01 in Status-Quo form]
GROUNDED: [C-01 Auditor-verified]
```

**AUDITOR GATE:**

- [ ] Audit Table complete
- [ ] Every essential criterion Status-Quo Test = NO
- [ ] Discriminating Element filled for every NO row
- [ ] Cross-criterion pattern note written
- [ ] C-01 confirmed = rank-1
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

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

DO NOT use symbolic variable names as denominators. Golden threshold: all essential +
composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-05 — Full Accumulation: All Three Axes (Combination)

**axis:** inertia-framing × output-format × lifecycle-emphasis
**hypothesis:** V-05 carries all three axes simultaneously. V-01 provides three-competitor
framing. V-02 provides flat annotated checklist skeleton. V-03 provides Phase 0 M-06
Self-Test. The combination tests whether the flat checklist and the attribution self-test
reinforce each other: the checklist items can be annotated with mechanism IDs (from V-03)
while the competitor-defeat column (from V-01) contextualizes which gap each mechanism
closes. Hypothesis: the compound structure produces a single Phase 0 artifact that is
simultaneously a structural commitment (V-02 checklist), a mechanism-sufficiency test
(V-03 attribution), and a competitor-defeat record (V-01 framing). If this three-layer Phase
0 artifact emerges as a distinct excellence pattern — beyond what any single axis produces
— it is the compound C-35+C-36+C-37 candidate. Risk: three-axis combination may produce
overcrowded Phase 0 output, reducing Author Phase quality. Monitor C-01–C-05 pass rates.
All other elements identical to R8 V-05 (formal CONSTRAINT/INVARIANT register preserved).

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

Three more specific competitors also fail — each on a narrower gap:

- **Overview-Silent Protocol:** M-01 through M-05, with a pre-phase skeleton step not
  named in the MECHANISMS overview. A builder reading only the orientation section cannot
  derive the full heading skeleton without reading phase instructions.

- **Inline-Scan Protocol:** Phase 0, M-06, two independent SV scans — but SV begins
  directly with Scan A. No preamble names both sources or declares non-overlapping failure
  classes before the scans.

- **Pre-Phase Protocol:** M-06 in MECHANISMS, SV two-source preamble — but the pre-phase
  step is labeled `### OUTPUT SKELETON`, not `### PHASE 0 — OUTPUT SKELETON`. The complete
  phase sequence (Phase 0 → Author → SV → Auditor) is not readable from headings alone.

Your protocol must exceed all four competitors.

This protocol enforces quality through six mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition any competitor would also accept is too weak.

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
  the skeleton is a builder commitment; Structural Verification cross-references it using
  two independent scans to detect builder-commitment failures (declared but not produced)
  distinct from heading-pattern misses (absent from output and absent from skeleton);
  this mechanism closes the gap left by the Overview-Silent Protocol; the Phase 0 label
  closes the gap left by the Pre-Phase Protocol

**Why six mechanisms plus the four-competitor framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the non-functional failure. Category gate prevents clustering. Auditor
table enables cross-criterion analysis. The output skeleton is an executable M-06 test.
Four competitors make discrimination concrete at four levels: generic quality, mechanism
visibility, scan architecture, and lifecycle labeling. The Status-Quo Rubric framing and
three specific competitors make the discrimination requirement concrete throughout.

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
an executable test of M-06's claim.

Produce the skeleton as a flat annotated checklist. For each heading, record the source
mechanism `[M-NN]` and the competitor whose gap this mechanism closes `[competitor]`.
Mark each item with `- [ ]` — tick as you produce each block.

```
Phase 0 skeleton — annotated tick list:

- [ ] ### PHASE 0 — OUTPUT SKELETON  [M-06] [defeats: Pre-Phase Protocol]
- [ ] ### AUTHOR PHASE               [M-02, M-03]
- [ ] ### INERTIA-RECORD [C-01]      [M-02] [defeats: Status-Quo]
- [ ] ### CALIBRATION-PAIR [C-01]    [M-02] [defeats: Status-Quo]
- [ ] ### CRITERION [C-01]           [M-02] [defeats: Status-Quo]
- [ ] [... repeat for C-02 through C-0N ...]
- [ ] ### STRUCTURAL VERIFICATION    [M-06] [defeats: Overview-Silent]
- [ ] ### AUDITOR PHASE              [M-05] [defeats: Status-Quo]
- [ ] ### REDUNDANCY-CHECK-TABLE     [M-05] [defeats: Status-Quo]
- [ ] ### END AUDITOR PHASE          [M-05]
- [ ] [Final Rubric section]
```

**PHASE 0 M-06 SELF-TEST**

After producing the annotated tick list, confirm M-06 sufficiency:

```
Unattributed headings: [list or "none"]
Headings without competitor annotation: [list or "none"]
```

If any unattributed headings: either add a missing MECHANISM or remove the heading.
If any heading cannot be attributed to a named MECHANISM, the MECHANISMS section is
incomplete — the builder has imported a heading from phase instructions in violation of M-06.

SELF-TEST PRECONDITION: all headings attributed and competitor defeats annotated.

**PHASE 0 COMPLETION GATE**

PRECONDITION for Author Phase entry:

- [ ] Annotated tick list is complete
- [ ] M-06 Self-Test complete: all headings attributed, all competitor defeats annotated
- [ ] Every heading pattern matches exactly the MECHANISMS-named pattern
- [ ] No unattributed headings

CONSTRAINT: DO NOT begin the Author Phase until all four preconditions are confirmed.

A heading declared in Phase 0 but absent from the output is a **builder-commitment
failure** — distinct from a **heading-pattern miss**. Structural Verification distinguishes
them using two independent scans.

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

DEFINITION (most critical): the failure that makes the output non-functional regardless of
all other criteria passing.

```
SEVERITY RANK:
1. [most critical — C-01 MUST target this]
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

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. Does it
catch something all four competitors would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would "the output is clear, complete, and well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [count, field name, pattern, or enumeration]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated): produce this block now — immediately after 2b. Batch production
violates INVARIANT B even if structural order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [competitor's best attempt]
GROUNDED: [your condition naming the skill-specific element]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION:
- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present, before this gate (INVARIANT B satisfied)
- [ ] Severity-rank alignment confirmed

CONSTRAINT 2d: forward-blocking gate. Do not record criterion row until all preconditions
confirmed.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

- [ ] Categories present: ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: fewer than 3 → add or revise before Structural Verification.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

**Out of scope:** `### REDUNDANCY-CHECK-TABLE` — deferred to AUDITOR GATE.

**Two independent sources of truth:**

Structural Verification uses two independent sources of truth: (1) the instruction-derived
heading patterns from M-02 and M-05, which identify which headings are required by the
protocol; and (2) the builder-declared annotated tick list from Phase 0 (verified by the
M-06 Self-Test), which records which headings the builder committed to producing. These
sources cover non-overlapping failure classes: source (1) detects **heading-pattern misses**
(required by instructions, absent from output); source (2) detects **builder-commitment
failures** (declared in Phase 0, absent from output). The Inline-Scan Protocol has both
scans but not this preamble: without the preamble, a maintainer cannot determine whether
collapsing to one scan destroys a distinct failure class.

**Scan A — instruction-derived heading patterns (heading-pattern miss detection):**

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

**Scan B — Phase 0 tick-list-declared headings (builder-commitment failure detection):**

Refer to the annotated tick list produced in `### PHASE 0 — OUTPUT SKELETON`. For each
entry in the list:

```
- [ ] Every heading from the Phase 0 tick list has a corresponding block in the output
```

A tick-list entry absent from the output is a **builder-commitment failure** — invisible
to Scan A.

For any missing block from either scan: write the block and re-check.

CONSTRAINT: the Auditor Phase cannot begin until (1) every required Author Phase heading
from Scan A confirmed present, AND (2) every heading in the Phase 0 tick list confirmed
produced (Scan B shows no builder-commitment failures outstanding).

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: element the Status-Quo Rubric cannot replicate. Required for
  every NO row. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. One sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

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

Replace each [N_x] with the actual criterion count. DO NOT use symbolic variable names as
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
