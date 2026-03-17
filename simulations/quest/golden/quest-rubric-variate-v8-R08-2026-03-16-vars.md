# quest-rubric Variate — Round 8 against rubric v8

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v8 (C-01 through C-26; essential C-01–C-05; aspirational /18)
**Round:** R8 — 3 single-axis + 2 combination

---

## Round 8 Design Note

R7 V-05 = 100.00 / Golden under v8 (all 18 aspirational criteria satisfied). No entering gap.

Round 8 direction: explore structural properties not yet formalized as criteria. Three candidate territories:

1. **Generalization** — v8 criteria were built against quest-rubric specifically. A prompt that abstracts the target skill may reveal tacit specificity assumptions in any criterion.
2. **Criterion dependency declaration** — No criterion in C-01–C-26 tests whether criteria declare their logical prerequisites. DEPENDS_ON / INDEPENDENT metadata per criterion is a structural property not yet captured.
3. **Discriminability contract** — No criterion tests whether each criterion names the quality boundary it enforces. A DISCRIMINATES_BETWEEN block per criterion makes the discriminative purpose explicit and tests for a new structural property.

## Axis Selection

| Variation | Axis | What Changes | New territory |
|-----------|------|--------------|--------------|
| V-01 | generalization-probe | All quest-rubric-specific language → abstract "target skill" framing | Tacit specificity assumptions |
| V-02 | criterion-dependency-declaration | M-06 added; DEPENDS_ON / INDEPENDENT per criterion; dependency ordering check in Auditor | Criterion dependency graph |
| V-03 | discriminability-contract | `### DISCRIMINATES-BETWEEN [C-NN]` block per essential criterion; Boundary uniqueness scan in Auditor | Discriminability declaration |
| V-04 | generalization-probe × criterion-dependency | V-01 abstraction + V-02 dependency | Dependency structure across skill types |
| V-05 | generalization-probe × criterion-dependency × discriminability | Full accumulation; M-06 checks boundary-dependency consistency | Boundary × dependency coherence |

## Score Projections under v8

All variations projected Golden. Excellence signal watch:

- **ES-R8-1 (V-02/V-04/V-05):** `DEPENDS_ON` / `INDEPENDENT` field + dependency ordering check — new criterion metadata property not in C-01–C-26
- **ES-R8-2 (V-03/V-05):** `### DISCRIMINATES-BETWEEN [C-NN]` block + Boundary uniqueness scan — new named block not in C-01–C-26
- **ES-R8-3 (V-05):** Dependency × boundary consistency check — whether DISCRIMINATES-BETWEEN boundary relationships entail DEPENDS_ON declarations

---

## V-01 — Generalization Probe (Single Axis)

**axis:** generalization-probe
**hypothesis:** All five mechanisms and sub-step protocols use "target skill" throughout; actual skill identity supplied only via SkillSpec input. If a builder can apply this prompt to any Signal skill and produce a C-01–C-26-compliant rubric, the criteria are skill-agnostic. If the prompt fails for a non-quest-rubric skill, a criterion fails that would not fail for quest-rubric — revealing a tacit specificity assumption. This is a rubric universality test, not a criterion gap test.

---

You are executing a scoring-rubric construction protocol for a Signal skill.

You will receive a **SkillSpec** naming the target skill, its artifact, and its required output fields. Your rubric must be specific enough to evaluate only that skill — a condition the Status-Quo Rubric would also accept is too weak.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

Every criterion you write must catch something this baseline misses. Name the count, field, structural pattern, or enumeration from the target skill's output contract that makes your condition non-generic.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to lowest-stakes failure mode; C-01 targets the failure making the output non-functional regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence; a missing block produces a missing heading detectable by scan without reading content
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria (`correctness` / `depth` / `format` / `coverage` / `behavior`)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`

**INVARIANTS:**

- INVARIANT A: a criterion row may not appear unless `### INERTIA-RECORD [C-NN]` and `### CALIBRATION-PAIR [C-NN]` are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### VERDICT TIER DECLARATION

- **PASS (1.0):** pass condition met in full; observable without evaluator discussion
- **PARTIAL (0.5):** partial evidence present but incomplete — only valid for criteria that declare a PARTIAL-CONDITION below
- **FAIL (0.0):** condition not met; or PARTIAL claimed but no PARTIAL-CONDITION declared

---

### AUTHOR PHASE

Read the SkillSpec. Answer before writing any criterion:

1. What artifact does the target skill produce? What fields are required?
2. What lifecycle phases does the skill have?
3. What single failure would make the rubric non-functional as an objective function for this skill?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking, 2 degrading. DO NOT proceed until satisfied.

**SEVERITY RANKING:**

```
1. [most critical — C-01 MUST target this]
2. [second]
3. [third]
[all blocking modes]
```

**AUTHOR PHASE 2 ENTRY GATE:**

- [ ] ≥ 3 blocking failure modes listed
- [ ] ≥ 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] ≥ 3 distinct output-contract categories identifiable: ___, ___, ___

CONSTRAINT: DO NOT write any criterion until all four confirmed.

**AUTHOR PHASE 2: ESSENTIAL CRITERIA (3–5)**

For each essential criterion in severity-rank order, apply sub-steps 2a–2d.

**Sub-step 2a** — Draft the pass condition. Specific, observable, references a count, field, structural pattern, or enumeration from the target skill's output contract.

**Sub-step 2b** — `### INERTIA-RECORD [C-NN]`:

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Status-Quo test: Would "clear, complete, well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field, pattern, or enumeration from this skill's output contract]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR. Violates INVARIANT A otherwise.

**Sub-step 2c** — `### CALIBRATION-PAIR [C-NN]` (INVARIANT B — write immediately after 2b):

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [condition any artifact could pass]
GROUNDED: [condition naming the skill-specific element; Status-Quo Rubric cannot replicate]
```

**Sub-step 2d** — Per-criterion forward gate:

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written in 2c (INVARIANT B confirmed)
- [ ] Severity-rank alignment confirmed

After gate cleared, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition] | [evidence for 0.5 or "binary"] |
```

Repeat sub-steps 2a–2d for each essential criterion.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational. Six-field table. No sub-step protocol required.

**CATEGORY-COVERAGE GATE:**

- [ ] Categories present: ___
- [ ] Count: ___ (minimum 3)

CONSTRAINT: fewer than 3 categories — add or revise before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION

**Scope: Author Phase output only.** Out of scope: `### REDUNDANCY-CHECK-TABLE` (Auditor Phase heading, not yet produced). Deferred to: AUDITOR GATE.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]    present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN]  present (STATUS-QUO + GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]         present, Partial Condition field populated
```

Missing heading = Phase 2 gate bypassed. Write the missing block, re-check.

PRECONDITION for Auditor Phase: every required heading pattern present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks before writing any Auditor output. Write the full Audit Table after reading all criteria — not one row at a time.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:** Discriminating Element variety vs clustering. Confirm C-01 = rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

| Pair | Pass-One-Fail-Other? | Reason | Action |
|------|---------------------|--------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| [all essential pairs] | | | |

**REDUNDANCY GATE:** all pairs evaluated; all YES or NO-flagged pairs resolved.

**Auditor Calibration Pair — most critical essential criterion:**

```
STATUS-QUO: [Status-Quo Rubric form]
GROUNDED: [Auditor-verified grounded form]
```

**AUDITOR GATE:**

- [ ] Audit Table complete
- [ ] All essential: Status-Quo Test = NO
- [ ] Discriminating Element filled for all NO rows
- [ ] Cross-criterion note written
- [ ] C-01 = rank-1 confirmed
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

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

Replace [N_x] with actual counts. Replace [first]/[last] with actual criterion IDs. DO NOT collapse to binary counting. DO NOT use symbolic variable names as denominators.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70–79 | Minor gaps, usable with awareness |
| Marginal | all essential + < 70 | Iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

---

## V-02 — Criterion Dependency Declaration (Single Axis)

**axis:** criterion-dependency-declaration
**hypothesis:** Each criterion carries an explicit DEPENDS_ON / INDEPENDENT declaration: does this criterion's pass condition presuppose another criterion passing? M-06 is added as a sixth mechanism. A criterion declared DEPENDS_ON C-M but ordered before C-M indicates a severity-ranking error detectable by scanning the dependency graph. A criterion declared INDEPENDENT but whose pass condition logically presupposes another criterion is a hidden coupling. If all criteria declare INDEPENDENT, the dependency property is vacuous for this skill — a negative finding with informational value. If ES-R8-1 surfaces, it becomes C-27: "Each essential criterion carries a DEPENDS_ON field identifying prerequisite criteria or declares INDEPENDENT; Auditor Phase checks ordering consistency."

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric competes against the Status-Quo Rubric — a rubric that says nothing specific about the target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through six mechanisms with formal invariants. Violating any invariant invalidates the step it governs. Every pass condition must name a specific count, field, structural pattern, or enumeration from the target skill's output contract — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to lowest-stakes failure mode; C-01 targets the failure making the output non-functional regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence; a missing block produces a missing heading detectable by scan without reading content
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria (`correctness` / `depth` / `format` / `coverage` / `behavior`)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading detects the omitted check by scan
- **M-06 — dependency graph:** each essential criterion carries a DEPENDS_ON or INDEPENDENT declaration in its `### CRITERION [C-NN]` row; Auditor Phase checks dependency ordering consistency — a criterion that depends on C-M but is ordered before C-M indicates a severity-ranking error

**INVARIANTS:**

- INVARIANT A: a criterion row may not appear unless `### INERTIA-RECORD [C-NN]` and `### CALIBRATION-PAIR [C-NN]` are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete
- INVARIANT C: DEPENDS_ON or INDEPENDENT is declared in sub-step 2d before the criterion row is recorded; undeclared dependency fails INVARIANT C

---

### VERDICT TIER DECLARATION

- **PASS (1.0):** pass condition met in full; observable without evaluator discussion
- **PARTIAL (0.5):** partial evidence present but incomplete — only valid for criteria declaring a PARTIAL-CONDITION below
- **FAIL (0.0):** condition not met; or PARTIAL claimed but no PARTIAL-CONDITION declared

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and required fields.
2. What lifecycle phases does the skill have?
3. What single failure would make the rubric non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking, 2 degrading. DO NOT proceed until satisfied.

**SEVERITY RANKING:**

```
1. [most critical — C-01 MUST target this]
2. [second]
3. [third]
[all blocking modes]
```

**AUTHOR PHASE 2 ENTRY GATE:**

- [ ] ≥ 3 blocking failure modes listed
- [ ] ≥ 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] ≥ 3 distinct output-contract categories identifiable: ___, ___, ___

CONSTRAINT: DO NOT write any criterion until all four confirmed.

**AUTHOR PHASE 2: ESSENTIAL CRITERIA (3–5)**

For each essential criterion in severity-rank order, apply sub-steps 2a–2e.

**Sub-step 2a** — Draft the pass condition. Specific, observable; references count, field, structural pattern, or enumeration from the target skill's output contract.

**Sub-step 2b** — `### INERTIA-RECORD [C-NN]`:

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Status-Quo test: Would "clear, complete, well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field, pattern, or enumeration]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD before CALIBRATION-PAIR (INVARIANT A).

**Sub-step 2c** — `### CALIBRATION-PAIR [C-NN]` (INVARIANT B — write immediately):

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [condition any artifact could pass]
GROUNDED: [condition naming the skill-specific element]
```

**Sub-step 2d** — Dependency declaration (INVARIANT C):

Does this criterion's pass condition presuppose any earlier criterion passing? If C-NN can pass while an earlier criterion fails, it is INDEPENDENT. If passing C-NN logically requires C-M to also pass, it DEPENDS_ON C-M.

```
Dependency: INDEPENDENT | DEPENDS_ON C-[M] — [reason]
```

**Sub-step 2e** — Per-criterion forward gate:

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written in 2c (INVARIANT B)
- [ ] Dependency declared in 2d (INVARIANT C)
- [ ] Severity-rank alignment confirmed

After gate cleared:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition] | [0.5 evidence or "binary"] | INDEPENDENT / DEPENDS_ON C-[M] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational. Seven-field table (include Dependency column). No sub-step protocol required for these tiers.

**CATEGORY-COVERAGE GATE:** Categories present: ___. Count: ___ (minimum 3).

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION

**Scope: Author Phase output only.** `### REDUNDANCY-CHECK-TABLE` deferred to AUDITOR GATE.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]    present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN]  present (STATUS-QUO + GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]         present, Partial Condition populated, Dependency field populated
```

PRECONDITION for Auditor Phase: every required heading pattern present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks before writing Auditor output.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Dependency ordering check (write after Audit Table):**

```
For each DEPENDS_ON C-M declaration:
  C-NN DEPENDS_ON C-M: ordered after C-M? [YES / NO] | dependency claim verified? [YES / NO]
```

**Cross-criterion note:** Discriminating Element variety. Dependency graph: connected vs fragmented. Confirm C-01 = rank-1.

### REDUNDANCY-CHECK-TABLE

| Pair | Pass-One-Fail-Other? | Reason | Action |
|------|---------------------|--------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| [all essential pairs] | | | |

**REDUNDANCY GATE:** all pairs evaluated; all YES or NO-flagged resolved.

**Auditor Calibration Pair:**

```
STATUS-QUO: [Status-Quo Rubric form]
GROUNDED: [Auditor-verified grounded form]
```

**AUDITOR GATE:**

- [ ] Audit Table complete; all essential: Status-Quo Test = NO
- [ ] Dependency ordering check complete; all DEPENDS_ON claims verified or corrected
- [ ] Cross-criterion note written
- [ ] C-01 = rank-1 confirmed
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|

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

DO NOT collapse to binary counting. DO NOT use symbolic variable names as denominators.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70–79 | Minor gaps, usable with awareness |
| Marginal | all essential + < 70 | Iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

---

## V-03 — Discriminability Contract (Single Axis)

**axis:** discriminability-contract
**hypothesis:** Each essential criterion carries a `### DISCRIMINATES-BETWEEN [C-NN]` block naming the quality boundary it enforces: the highest-quality output that fails vs the lowest-quality output that passes. This is a fourth named block in M-02's sequence (INERTIA-RECORD → DISCRIMINATES-BETWEEN → CALIBRATION-PAIR → CRITERION). The Auditor Phase gains a boundary uniqueness scan. If ES-R8-2 surfaces as distinct from REDUNDANCY-CHECK-TABLE (which tests outcome independence, not quality-boundary overlap), it becomes C-27: "Each essential criterion carries a DISCRIMINATES-BETWEEN block with Boundary statement; Auditor Phase scans for duplicate boundaries as consolidation candidates."

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric competes against the Status-Quo Rubric — a rubric that says nothing specific about the target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating any invariant invalidates the step it governs. Every pass condition must name a specific count, field, structural pattern, or enumeration from the target skill's output contract — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to lowest-stakes failure mode; C-01 targets the failure making the output non-functional regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`, `### DISCRIMINATES-BETWEEN [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence; a missing block produces a missing heading detectable by scan without reading content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is written; gates prevent omission
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria (`correctness` / `depth` / `format` / `coverage` / `behavior`)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated table, pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`, and boundary uniqueness scan

**Why the DISCRIMINATES-BETWEEN block?**

The Status-Quo Rubric discriminates only between "acceptable" and "unacceptable." Your rubric must discriminate between specific quality levels within the target skill's output. Naming the quality boundary each criterion enforces prevents two criteria from guarding the same boundary under different labels. This is distinct from CALIBRATION-PAIR (which names specific artifact content examples) and from REDUNDANCY-CHECK-TABLE (which tests outcome independence). DISCRIMINATES-BETWEEN operates at the quality-level meta-description layer.

**INVARIANTS:**

- INVARIANT A: a criterion row may not appear unless `### INERTIA-RECORD [C-NN]`, `### DISCRIMINATES-BETWEEN [C-NN]`, and `### CALIBRATION-PAIR [C-NN]` are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after `### DISCRIMINATES-BETWEEN [C-NN]` — not after all INERTIA-RECORD or DISCRIMINATES-BETWEEN blocks are complete

---

### VERDICT TIER DECLARATION

- **PASS (1.0):** pass condition met in full; observable without evaluator discussion
- **PARTIAL (0.5):** partial evidence present but incomplete — only valid for criteria declaring a PARTIAL-CONDITION below
- **FAIL (0.0):** condition not met; or PARTIAL claimed but no PARTIAL-CONDITION declared

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and required fields.
2. What lifecycle phases does the skill have?
3. What single failure would make the rubric non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking, 2 degrading. DO NOT proceed until satisfied.

**SEVERITY RANKING:**

```
1. [most critical — C-01 MUST target this]
2. [second]
3. [third]
[all blocking modes]
```

**AUTHOR PHASE 2 ENTRY GATE:**

- [ ] ≥ 3 blocking failure modes listed
- [ ] ≥ 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] ≥ 3 distinct output-contract categories identifiable: ___, ___, ___

CONSTRAINT: DO NOT write any criterion until all four confirmed.

**AUTHOR PHASE 2: ESSENTIAL CRITERIA (3–5)**

For each essential criterion in severity-rank order, apply sub-steps 2a–2d.

**Sub-step 2a** — Draft the pass condition. Specific, observable; references count, field, structural pattern, or enumeration from the target skill's output contract.

**Sub-step 2b** — `### INERTIA-RECORD [C-NN]`:

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Status-Quo test: Would "clear, complete, well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field, pattern, or enumeration]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

**Sub-step 2b.5** — `### DISCRIMINATES-BETWEEN [C-NN]` (write immediately after INERTIA-RECORD):

```
### DISCRIMINATES-BETWEEN [C-NN]
FAILS-AT:  [highest-quality output that still fails this criterion — what is present but insufficient]
PASSES-AT: [lowest-quality output that passes — minimum sufficient condition]
Boundary:  [one sentence naming the quality level transition this criterion guards]
```

CONSTRAINT 2b.5: Boundary statement must be unique across all criteria. Identical boundaries = consolidation candidate (flag it). Do not produce CALIBRATION-PAIR until DISCRIMINATES-BETWEEN is complete.

**Sub-step 2c** — `### CALIBRATION-PAIR [C-NN]` (INVARIANT B — write immediately after 2b.5):

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [condition any artifact could pass]
GROUNDED: [condition naming the skill-specific element; references the boundary from DISCRIMINATES-BETWEEN]
```

**Sub-step 2d** — Per-criterion forward gate:

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### DISCRIMINATES-BETWEEN [C-NN]` present (FAILS-AT + PASSES-AT + Boundary), Boundary unique
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written in 2c (INVARIANT B)
- [ ] Severity-rank alignment confirmed

After gate cleared:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition] | [evidence for 0.5 or "binary"] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational. Six-field table. No sub-step protocol required.

**CATEGORY-COVERAGE GATE:** Categories present: ___. Count: ___ (minimum 3).

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION

**Scope: Author Phase output only.** `### REDUNDANCY-CHECK-TABLE` deferred to AUDITOR GATE.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]          present, precedes ### DISCRIMINATES-BETWEEN [C-NN]
- [ ] ### DISCRIMINATES-BETWEEN [C-NN]   present (FAILS-AT + PASSES-AT + Boundary), precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN]        present (STATUS-QUO + GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]               present, Partial Condition populated
```

PRECONDITION for Auditor Phase: every required heading pattern present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` and all `### DISCRIMINATES-BETWEEN [C-NN]` blocks before writing Auditor output.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Boundary uniqueness scan (write after Audit Table):**

```
C-01: [boundary statement]
C-02: [boundary statement]
...
Duplicate boundaries: [none / C-NN and C-MM share boundary — consolidation candidate]
```

**Cross-criterion note:** Discriminating Element variety. Boundaries: distinct vs overlapping. Confirm C-01 = rank-1.

### REDUNDANCY-CHECK-TABLE

| Pair | Pass-One-Fail-Other? | Reason | Action |
|------|---------------------|--------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| [all essential pairs] | | | |

**REDUNDANCY GATE:** all pairs evaluated; all YES or NO-flagged resolved.

**Auditor Calibration Pair:**

```
STATUS-QUO: [Status-Quo Rubric form]
GROUNDED: [Auditor-verified grounded form]
```

**AUDITOR GATE:**

- [ ] Audit Table complete; all essential: Status-Quo Test = NO
- [ ] Boundary uniqueness scan complete; duplicate boundaries flagged or resolved
- [ ] Cross-criterion note written
- [ ] C-01 = rank-1 confirmed
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

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

DO NOT collapse to binary counting. DO NOT use symbolic variable names as denominators.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70–79 | Minor gaps, usable with awareness |
| Marginal | all essential + < 70 | Iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

---

## V-04 — Generalization Probe × Criterion Dependency (Combination)

**axis:** generalization-probe × criterion-dependency-declaration
**hypothesis:** Abstract target-skill framing (V-01) combined with M-06 criterion dependency graph (V-02) tests whether dependency structure varies by skill type. For quest-rubric, criteria are expected largely INDEPENDENT. For a lifecycle-heavy skill (e.g., flow-trigger), criteria may have richer DEPENDS_ON structure. If V-04 surfaces a dependency finding not present in V-02, the interaction between generalization framing and dependency declaration is a combined excellence signal candidate. The skill identity is supplied via SkillSpec only — no skill-specific vocabulary in the instructions.

---

You are executing a scoring-rubric construction protocol for a Signal skill.

You will receive a **SkillSpec** naming the target skill, its artifact, and its required output fields. Your rubric must be specific enough to evaluate only that skill — a condition the Status-Quo Rubric would also accept is too weak.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through six mechanisms with formal invariants. Every pass condition must name a specific count, field, structural pattern, or enumeration from the target skill's output contract.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to lowest-stakes failure mode; C-01 targets the failure making the output non-functional regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence; a missing block produces a missing heading detectable by scan
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is written; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria (`correctness` / `depth` / `format` / `coverage` / `behavior`)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`
- **M-06 — dependency graph:** each essential criterion carries a DEPENDS_ON or INDEPENDENT declaration; Auditor Phase checks dependency ordering consistency — a criterion that depends on C-M but is ordered before C-M indicates a severity-ranking error

**INVARIANTS:**

- INVARIANT A: a criterion row may not appear unless `### INERTIA-RECORD [C-NN]` and `### CALIBRATION-PAIR [C-NN]` are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` written immediately after `### INERTIA-RECORD [C-NN]`
- INVARIANT C: DEPENDS_ON / INDEPENDENT declared in sub-step 2d before the criterion row is recorded

---

### VERDICT TIER DECLARATION

- **PASS (1.0):** pass condition met in full; observable without evaluator discussion
- **PARTIAL (0.5):** partial evidence present but incomplete — only valid for criteria declaring a PARTIAL-CONDITION
- **FAIL (0.0):** condition not met; or PARTIAL claimed but no PARTIAL-CONDITION declared

---

### AUTHOR PHASE

Read the SkillSpec. Answer before writing any criterion:

1. What artifact does the target skill produce? What fields are required?
2. What lifecycle phases does the skill have?
3. What single failure would make the rubric non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking, 2 degrading. DO NOT proceed until satisfied.

**SEVERITY RANKING:**

```
1. [most critical — C-01 MUST target this]
2. [second]
3. [third]
[all blocking modes]
```

**AUTHOR PHASE 2 ENTRY GATE:**

- [ ] ≥ 3 blocking failure modes listed
- [ ] ≥ 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] ≥ 3 distinct output-contract categories identifiable: ___, ___, ___

**AUTHOR PHASE 2: ESSENTIAL CRITERIA (3–5)**

For each essential criterion in severity-rank order, apply sub-steps 2a–2e.

**Sub-step 2a** — Draft the pass condition. References count, field, structural pattern, or enumeration from the target skill's output contract.

**Sub-step 2b** — `### INERTIA-RECORD [C-NN]`:

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Status-Quo test: Would "clear, complete, well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field, pattern, or enumeration from target skill's contract]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

**Sub-step 2c** — `### CALIBRATION-PAIR [C-NN]` (INVARIANT B — write now):

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [condition any artifact could pass]
GROUNDED: [condition naming the skill-specific element]
```

**Sub-step 2d** — Dependency declaration (INVARIANT C):

```
Dependency: INDEPENDENT | DEPENDS_ON C-[M] — [reason]
```

**Sub-step 2e** — Per-criterion forward gate:

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written in 2c (INVARIANT B)
- [ ] Dependency declared in 2d (INVARIANT C)
- [ ] Severity-rank alignment confirmed

After gate cleared:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition] | [0.5 evidence or "binary"] | INDEPENDENT / DEPENDS_ON C-[M] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational. Seven-field table. No sub-step protocol.

**CATEGORY-COVERAGE GATE:** Categories present: ___. Count: ___ (minimum 3).

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION

**Scope: Author Phase output only.** `### REDUNDANCY-CHECK-TABLE` deferred to AUDITOR GATE.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]    present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN]  present (STATUS-QUO + GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]         present, Partial Condition populated, Dependency field populated
```

PRECONDITION for Auditor Phase: every required heading pattern present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks before writing Auditor output.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Dependency ordering check:**

```
For each DEPENDS_ON C-M declaration:
  C-NN DEPENDS_ON C-M: ordered after C-M? [YES / NO] | dependency claim verified? [YES / NO]
```

**Cross-criterion note:** Discriminating Element variety. Dependency graph: connected vs fragmented. Confirm C-01 = rank-1.

### REDUNDANCY-CHECK-TABLE

| Pair | Pass-One-Fail-Other? | Reason | Action |
|------|---------------------|--------|--------|
| [all essential pairs] | | | |

**REDUNDANCY GATE:** all pairs evaluated; all YES or NO-flagged resolved.

**Auditor Calibration Pair:**

```
STATUS-QUO: [Status-Quo form]
GROUNDED: [Auditor-verified grounded form]
```

**AUDITOR GATE:**

- [ ] Audit Table complete; all essential: Status-Quo Test = NO
- [ ] Dependency ordering check complete; all DEPENDS_ON claims verified
- [ ] Cross-criterion note written
- [ ] C-01 = rank-1 confirmed
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|

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

DO NOT collapse to binary. DO NOT use symbolic denominators.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready |
| Acceptable | all essential + 70–79 | Minor gaps |
| Marginal | all essential + < 70 | Iterate |
| Fail | any essential fails | Not a valid objective function |

---

## V-05 — Full Accumulation (Generalization × Dependency × Discriminability)

**axis:** generalization-probe × criterion-dependency-declaration × discriminability-contract
**hypothesis:** All three new structural properties combined in skill-agnostic framing. V-05 tests whether DISCRIMINATES-BETWEEN boundary relationships entail DEPENDS_ON declarations (i.e., whether discriminability and dependency are the same structural property viewed from different angles). If C-NN guards a higher quality boundary than C-M and DEPENDS_ON C-M, then the dependency follows from the boundary relationship — and the two properties may not be independent. If they co-vary completely, they collapse into one C-27. If they diverge (a dependency without a boundary ordering, or a boundary ordering without a dependency), they become separate aspirational criteria in rubric v9.

---

You are executing a scoring-rubric construction protocol for a Signal skill.

You will receive a **SkillSpec** naming the target skill, its artifact, and its required output fields. Your rubric must be specific enough to evaluate only that skill — a condition the Status-Quo Rubric would also accept is too weak.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through six mechanisms with formal invariants. Violating any invariant invalidates the step it governs. Every pass condition must name a specific count, field, structural pattern, or enumeration from the target skill's output contract.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to lowest-stakes failure mode; C-01 targets the failure making the output non-functional regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`, `### DISCRIMINATES-BETWEEN [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence; a missing block produces a missing heading detectable by scan; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is written; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria (`correctness` / `depth` / `format` / `coverage` / `behavior`)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated table, pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`, and boundary uniqueness scan
- **M-06 — dependency graph with boundary consistency:** each essential criterion carries a DEPENDS_ON or INDEPENDENT declaration; Auditor Phase checks (a) dependency ordering consistency and (b) whether declared DEPENDS_ON relationships are entailed by the DISCRIMINATES-BETWEEN boundary orderings — a consistency test between the quality-boundary view and the logical-dependency view of the criterion graph

**INVARIANTS:**

- INVARIANT A: a criterion row may not appear unless `### INERTIA-RECORD [C-NN]`, `### DISCRIMINATES-BETWEEN [C-NN]`, and `### CALIBRATION-PAIR [C-NN]` are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` written immediately after `### DISCRIMINATES-BETWEEN [C-NN]`
- INVARIANT C: DEPENDS_ON / INDEPENDENT declared and consistent with DISCRIMINATES-BETWEEN boundary before the criterion row is recorded

---

### VERDICT TIER DECLARATION

- **PASS (1.0):** pass condition met in full; observable without evaluator discussion
- **PARTIAL (0.5):** partial evidence present but incomplete — only valid for criteria declaring a PARTIAL-CONDITION
- **FAIL (0.0):** condition not met; or PARTIAL claimed but no PARTIAL-CONDITION declared

---

### AUTHOR PHASE

Read the SkillSpec. Answer before writing any criterion:

1. What artifact does the target skill produce? What fields are required?
2. What lifecycle phases does the skill have?
3. What single failure would make the rubric non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking, 2 degrading. DO NOT proceed until satisfied.

**SEVERITY RANKING:**

```
1. [most critical — C-01 MUST target this]
2. [second]
3. [third]
[all blocking modes]
```

**AUTHOR PHASE 2 ENTRY GATE:**

- [ ] ≥ 3 blocking failure modes listed
- [ ] ≥ 2 degrading failure modes listed
- [ ] Severity rank complete
- [ ] ≥ 3 distinct output-contract categories identifiable: ___, ___, ___

**AUTHOR PHASE 2: ESSENTIAL CRITERIA (3–5)**

For each essential criterion in severity-rank order, apply sub-steps 2a–2f.

**Sub-step 2a** — Draft the pass condition. References count, field, structural pattern, or enumeration from the target skill's output contract.

**Sub-step 2b** — `### INERTIA-RECORD [C-NN]`:

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Status-Quo test: Would "clear, complete, well-formatted" accept this? [YES / NO]
If YES — revised condition: [revision until NO]
Final condition: [condition the Status-Quo Rubric rejects]
Skill-specific element: [count, field, pattern, or enumeration from target skill's contract]
Severity-rank alignment: [targets rank-N — "[failure mode]"]
```

**Sub-step 2b.5** — `### DISCRIMINATES-BETWEEN [C-NN]` (write immediately after INERTIA-RECORD):

```
### DISCRIMINATES-BETWEEN [C-NN]
FAILS-AT:  [highest-quality output that still fails this criterion]
PASSES-AT: [lowest-quality output that passes]
Boundary:  [one sentence naming the quality level transition guarded]
```

CONSTRAINT 2b.5: Boundary must be unique. Identical boundaries = consolidation candidate (flag).

**Sub-step 2c** — `### CALIBRATION-PAIR [C-NN]` (INVARIANT B — write immediately after 2b.5):

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [condition any artifact could pass]
GROUNDED: [condition naming the skill-specific element; references boundary from DISCRIMINATES-BETWEEN]
```

**Sub-step 2d** — Dependency declaration (INVARIANT C):

Does the DISCRIMINATES-BETWEEN Boundary for C-NN presuppose the Boundary for any earlier C-M (i.e., the higher quality level guarded by C-NN is only reachable after the quality level guarded by C-M)? If yes, C-NN DEPENDS_ON C-M.

```
Dependency: INDEPENDENT | DEPENDS_ON C-[M] — [reason; consistent with DISCRIMINATES-BETWEEN boundary relationship]
```

CONSTRAINT 2d: If DEPENDS_ON C-M is declared but boundaries do not show an ordering relationship, state the dependency reason explicitly. Inconsistency between declared dependency and boundary relationship must be resolved.

**Sub-step 2f** — Per-criterion forward gate:

- [ ] `### INERTIA-RECORD [C-NN]` present, Status-Quo test = NO
- [ ] `### DISCRIMINATES-BETWEEN [C-NN]` present (FAILS-AT + PASSES-AT + Boundary), Boundary unique
- [ ] `### CALIBRATION-PAIR [C-NN]` present, written in 2c (INVARIANT B)
- [ ] Dependency declared in 2d, consistent with DISCRIMINATES-BETWEEN boundary (INVARIANT C)
- [ ] Severity-rank alignment confirmed

After gate cleared:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition] | [0.5 evidence or "binary"] | INDEPENDENT / DEPENDS_ON C-[M] |
```

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational. Seven-field table. No sub-step protocol required.

**CATEGORY-COVERAGE GATE:** Categories present: ___. Count: ___ (minimum 3).

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION

**Scope: Author Phase output only.** `### REDUNDANCY-CHECK-TABLE` deferred to AUDITOR GATE.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]          present, precedes ### DISCRIMINATES-BETWEEN [C-NN]
- [ ] ### DISCRIMINATES-BETWEEN [C-NN]   present (FAILS-AT + PASSES-AT + Boundary), precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN]        present (STATUS-QUO + GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]               present, Partial Condition populated, Dependency field populated
```

PRECONDITION for Auditor Phase: every required heading pattern present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]`, `### DISCRIMINATES-BETWEEN [C-NN]`, and `### CALIBRATION-PAIR [C-NN]` blocks before writing Auditor output.

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Boundary uniqueness scan:**

```
C-01: [boundary]
C-02: [boundary]
...
Duplicate boundaries: [none / C-NN and C-MM — consolidation candidate]
```

**Dependency × boundary consistency check:**

```
For each DEPENDS_ON C-M:
  C-M Boundary: [statement]
  C-NN Boundary: [statement]
  C-NN boundary presupposes C-M boundary? [YES / NO / EXPLAIN]
  Consistency: CONSISTENT | INCONSISTENT — [reason]
```

**Cross-criterion note:** Discriminating Element variety. Boundaries: distinct vs overlapping. Dependency graph coherence.

### REDUNDANCY-CHECK-TABLE

| Pair | Pass-One-Fail-Other? | Reason | Action |
|------|---------------------|--------|--------|
| [all essential pairs] | | | |

**REDUNDANCY GATE:** all pairs evaluated; all YES or NO-flagged resolved.

**Auditor Calibration Pair:**

```
STATUS-QUO: [Status-Quo form]
GROUNDED: [Auditor-verified grounded form]
```

**AUDITOR GATE:**

- [ ] Audit Table complete; all essential: Status-Quo Test = NO
- [ ] Boundary uniqueness scan: no duplicates, or consolidation candidates flagged
- [ ] Dependency × boundary consistency check complete; all inconsistencies resolved
- [ ] Cross-criterion note written
- [ ] C-01 = rank-1 confirmed
- [ ] `### REDUNDANCY-CHECK-TABLE` present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition | Dependency |
|----|-----------|----------|--------|----------------|-------------------|------------|

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

DO NOT collapse to binary counting. DO NOT use symbolic variable names as denominators.
Reproduce this formula verbatim at every structural position where a formula appears.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70–79 | Minor gaps, usable with awareness |
| Marginal | all essential + < 70 | Iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

---

## Anchor Designation (Preliminary)

**Anchor: V-05**

V-05 is the maximal accumulation. All C-01–C-26 properties carry forward (no existing criteria threatened). Excellence signal watch:

- **ES-R8-1:** `### DISCRIMINATES-BETWEEN [C-NN]` per essential criterion + Boundary uniqueness scan in Auditor Phase. New named block in M-02 sequence not in C-01–C-26. Present in V-03, V-05.
- **ES-R8-2:** DEPENDS_ON / INDEPENDENT per criterion + Dependency ordering check in Auditor Phase. New criterion metadata field and Auditor check not in C-01–C-26. Present in V-02, V-04, V-05.
- **ES-R8-3 (V-05 only):** Dependency × boundary consistency check — whether boundary relationship ordering entails dependency declarations. Tests ES-R8-1 and ES-R8-2 independence.

**Independence test:** If ES-R8-1 and ES-R8-2 co-vary completely (every boundary ordering produces a dependency, and every dependency has a boundary ordering), they collapse into C-27. If they diverge in at least one case, they become C-27 (discriminability contract) and C-28 (dependency graph). V-05 is designed to make this independence testable.

**Round 9 direction:** Score all five R8 variations. Identify which excellence signals appear in V-02+ vs V-03+ vs V-05 only. Absorb surviving signals as new aspirational criteria in rubric v9.
