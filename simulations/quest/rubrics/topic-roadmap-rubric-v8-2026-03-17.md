v8 written to `simulations/quest/rubrics/topic-roadmap-rubric-v8-2026-03-17.md`.

**What changed v7 → v8:**

| | |
|---|---|
| Version | 7 → 8 |
| Formula | `/ 20 * 10` → `/ 24 * 10` |
| Aspirational range | C-09–C-18 → C-09–C-20 |
| **C-19 added** | Phase entry/exit conditions — from V-05: explicit phase boundaries make skipping detectable at the boundary, not inferred from output structure |
| **C-20 added** | Bias labels at every structural guard point — from V-05: complete guard coverage (SIGNAL READ-LOCK, INERTIA-GATE, confirmation gate, write guard all labeled inline), not just proposal table columns |

The two criteria are orthogonal: C-19 tests whether phase sequencing is verifiably bounded; C-20 tests whether bias-label coverage is complete across all guard sites. A skill can pass one while failing the other. V-05 achieves both; that's why the scorecard singles it out with the lifecycle emphasis axis.
firms. strategy.md updated.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_raw / 24 * 10)
```

Where `aspirational_raw` = sum of per-criterion scores across C-09–C-20
(full pass = 2, partial = 1, fail = 0; max = 24).

**Golden threshold:** all essential pass + composite >= 80

---

## Essential Criteria (must all pass)

### C-01 — Inertia prior enforced
- **Weight:** essential
- **Category:** correctness
- **Text:** Zero-change is a valid, complete output. The skill treats strategy.md
  unchanged as the default outcome. Proposals require evidence from NEW signal
  artifacts; volume of signals alone does not trigger change.
- **Pass condition:** Output either (a) produces proposals each backed by a
  named NEW artifact, OR (b) explicitly declares that inertia holds with a
  type-labeled null declaration. A run that opens with "here are the changes
  I recommend" without naming new artifacts fails.

---

### C-02 — Signal delta established before proposals
- **Weight:** essential
- **Category:** correctness
- **Text:** Signal inventory and delta analysis are present in the output
  before any proposal table is shown. The inventory classifies each artifact
  as NEW (date > strategy date) or PRIOR.
- **Pass condition:** A signal inventory table appears (at minimum: artifact
  filename, date, NEW/PRIOR, namespace). At least one of the four delta
  categories — CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED — is present
  in the output, even if populated with a null declaration. Proposals that
  appear before any delta analysis fail.

---

### C-03 — Proposals are concrete and action-typed
- **Weight:** essential
- **Category:** depth
- **Text:** Every proposal names its action type (ADD, REMOVE, or REPRIORITIZE),
  the specific strategy dimension it targets, and the new signal evidence
  that defeats the keep-unchanged option. Vague proposals ("consider expanding
  coverage") do not pass.
- **Pass condition:** Each proposal row contains: (a) action type from the
  ADD / REMOVE / REPRIORITIZE set, (b) a named strategy dimension with
  Before/After state, and (c) a specific signal artifact cited as evidence.
  A proposal row missing any of the three elements fails.

---

### C-04 — User confirmation gate is present and blocking
- **Weight:** essential
- **Category:** safety
- **Text:** After presenting proposals, the skill emits an explicit stop
  instruction and an AWAITING CONFIRMATION block. strategy.md is not modified
  until the user responds. The block names the file explicitly and states it
  has not been changed.
- **Pass condition:** Output contains an explicit stop instruction (e.g.,
  "STOP. Do not modify strategy.md.") followed by an AWAITING CONFIRMATION
  block stating strategy.md has not been modified. A skill that advances to
  apply without a user reply fails unconditionally.

---

### C-05 — All-namespace coverage with null rows
- **Weight:** essential
- **Category:** completeness
- **Text:** All 9 namespaces (scout / draft / review / flow / trace / prove /
  listen / program / topic) are assessed in the signal inventory. A namespace
  with zero artifacts emits an explicit null row; silence is not a null
  declaration. The proposal section also requires a row per namespace.
- **Pass condition:** All 9 namespaces appear in the inventory table. Any
  namespace without artifacts has an explicit null row. Proposal phase mandates
  a row for each namespace, even if that row is a null declaration.

---

## Recommended Criteria (at least 2 of 3 must pass)

### C-06 — Null path stop enforced at defeat phase
- **Weight:** recommended
- **Category:** correctness
- **Text:** When all defeat assessment verdicts are HOLDS, the skill emits a
  NULL_DELTA declaration and halts. It does not open the proposal phase for
  zero proposals.
- **Pass condition:** Defeat assessment phase contains an explicit conditional:
  "If all verdicts are HOLDS: Emit NULL_DELTA. Stop. Do not open Phase 6."
  A run that generates an empty proposal table after all-HOLDS verdicts fails.

---

### C-07 — Confidence tiers defined
- **Weight:** recommended
- **Category:** depth
- **Text:** Proposals carry a confidence level defined with specific evidential
  criteria. The tiers are HIGH, MEDIUM, and LOW; each is tied to the count
  or type of independent NEW artifacts supporting the defeat.
- **Pass condition:** At least three confidence tiers are defined with their
  evidential backing (e.g., HIGH = two+ independent NEW artifacts; MEDIUM =
  one; LOW = inference). Tiers without evidential criteria do not pass.

---

### C-08 — Consequence-if-unchanged in proposals
- **Weight:** recommended
- **Category:** depth
- **Text:** Every proposal and every defeat assessment row requires a
  "Consequence if unchanged" field. Proposals without a stated consequence do
  not pass the defeat assessment gate and cannot advance to the proposal table.
- **Pass condition:** "Consequence if unchanged" column required in both the
  defeat assessment table and the proposal table. Absent in either location
  is a partial pass.

---

## Aspirational Criteria (scored 0 / 1 / 2 per criterion; max = 24)

### C-09 — Pre-signal defense register written before reading any file
- **Weight:** aspirational
- **Category:** depth
- **Text:** Before reading any signal artifact or strategy.md, the skill writes
  a defense register table with one row per active strategy dimension, stating
  the best reason to keep each dimension unchanged and what evidence would defeat
  that defense. Defenses written pre-read declare prior belief; defenses written
  post-read rationalize evidence. This is the only anchor-bias block that works.
- **Full pass (2):** Defense register table with schema (dimension, current state,
  best defense, what would defeat this) appears before any signal files are read;
  a hard constraint ("Do NOT read strategy.md or any signal file yet") enforces
  pre-read isolation.
- **Partial (1):** Defense register present but appears after signal read, or
  lacks table schema, or isolation constraint is absent.
- **Fail (0):** No pre-signal defense register.

---

### C-10 — SIGNAL READ-LOCK enforced after inventory is written
- **Weight:** aspirational
- **Category:** safety
- **Text:** Once the signal inventory table is written, signal files may not be
  re-read. The lock is named ("SIGNAL READ-LOCK" or equivalent), placed
  immediately after the inventory closes, and names the bias it prevents
  (confirmation bias / vocabulary contamination from strategy re-read).
- **Full pass (2):** Explicit named instruction placed immediately after the
  inventory table; states that signal files may not be re-read; names the
  bias blocked.
- **Partial (1):** Sequencing implies the lock but no explicit named instruction,
  or lock is present but not named or not bias-labeled.
- **Fail (0):** No read-lock present.

---

### C-11 — INERTIA-GATE phase sequencing enforcement
- **Weight:** aspirational
- **Category:** correctness
- **Text:** A structural gate labeled INERTIA-GATE (or equivalent) explicitly
  blocks dimensions with HOLDS verdicts from entering the proposal phase. HOLDS
  rows receive a NO CHANGE entry with no path to Phase 6. The gate is not implied
  by phase ordering — it is explicitly stated as a structural constraint.
- **Full pass (2):** "[INERTIA-GATE: This phase runs only for DEFEATED dimensions]"
  or equivalent explicit label; HOLDS rows explicitly prohibited from reaching the
  proposal phase.
- **Partial (1):** Gate concept present but not explicitly labeled, or HOLDS
  exclusion from proposal phase not stated.
- **Fail (0):** No inertia gate or HOLDS path unguarded.

---

### C-12 — Consequence column in defeat assessment
- **Weight:** aspirational
- **Category:** depth
- **Text:** The defeat assessment table requires a "Consequence if unchanged"
  column populated for every row, positioned before the proposal gate. Placing
  consequence only in the proposal table (where the user sees it) and not in
  the defeat assessment (where the qualification decision is made) leaves the
  evaluation post-hoc.
- **Full pass (2):** Consequence column required in the defeat assessment table,
  positioned before the proposal generation gate; failing to populate it blocks
  the row from advancing.
- **Partial (1):** Consequence present in proposal table only, not in defeat
  assessment; or present in defeat assessment but not enforced as a gate.
- **Fail (0):** No consequence column in defeat assessment.

---

### C-13 — DEFEATED/HOLDS verdict semantics
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The defeat assessment uses exactly two verdict tokens with explicit
  semantics: DEFEATED (signal overcomes the pre-registered defense; dimension
  advances to proposals) and HOLDS (defense survives; no proposal generated for
  this dimension). Semantics and consequences are stated explicitly — not inferred
  from phase ordering.
- **Full pass (2):** DEFEATED and HOLDS defined with semantics; HOLDS explicitly
  maps to "no proposal generated"; consequences of each verdict are stated.
- **Partial (1):** Two verdicts present but semantics not stated, or one verdict's
  consequences are implied rather than explicit.
- **Fail (0):** No explicit verdict vocabulary.

---

### C-14 — NEW/PRIOR split with explicit date anchor
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The signal inventory classifies artifacts as NEW or PRIOR using an
  explicit date rule tied to a recorded strategy date. The rule is stated as an
  inequality ("NEW = artifact date > strategy date / PRIOR = artifact date <=
  strategy date"). The strategy date is recorded as a named field before inventory
  classification begins.
- **Full pass (2):** Date rule stated with explicit inequality; strategy date
  recorded as a named field before classification; all inventory rows carry the
  NEW/PRIOR classification.
- **Partial (1):** NEW/PRIOR classification present but date rule not explicit, or
  strategy date not recorded before classification begins.
- **Fail (0):** No date-anchored NEW/PRIOR classification.

---

### C-15 — Confidence levels with evidential criteria
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each proposal carries a confidence level (HIGH / MEDIUM / LOW) with
  specific, countable evidential criteria tied to the number of independent NEW
  artifacts. Level assignment follows a stated rule — not qualitative judgment
  (e.g., HIGH = two or more independent NEW artifacts; MEDIUM = one; LOW =
  inference only).
- **Full pass (2):** HIGH, MEDIUM, and LOW each defined with specific evidential
  criteria; criteria involve countable artifact independence.
- **Partial (1):** Confidence levels defined but criteria are qualitative
  descriptions without specific counts or artifact-independence requirement.
- **Fail (0):** No confidence levels, or levels without evidential criteria.

---

### C-16 — Type-labeled nulls for all categories
- **Weight:** aspirational
- **Category:** completeness
- **Text:** Every structured output section emits a type-labeled null declaration
  when empty. Required: four delta-type nulls (CONFIRMED / EXPANDED / UNEXPECTED /
  CHALLENGED) and three proposal-type nulls (ADDITIONS / REMOVALS /
  REPRIORITIZATIONS). All null declarations carry their category label. Silent
  omission of any category is a structural failure.
- **Full pass (2):** All seven null declaration types required; each carries its
  category label; explicit prohibition on silent omission.
- **Partial (1):** Some null types covered but not all seven, or type label absent
  on some declarations.
- **Fail (0):** No type-labeled null structure.

---

### C-17 — Bias labels per proposal row and per phase
- **Weight:** aspirational
- **Category:** safety
- **Text:** Cognitive bias labels appear at two structural levels: (a) a "Bias
  blocked by guard" column in proposal tables names the bias each proposal guard
  prevents at the decision surface, and (b) per-phase "Bias blocked:" annotations
  in phase headings or preambles name the cognitive bias each phase structure
  prevents. Both levels are required.
- **Full pass (2):** "Bias blocked by guard" column present in proposal tables AND
  per-phase "Bias blocked:" annotations present for all major phases; all major
  guards labeled at their respective level.
- **Partial (1):** Bias labels present at one level only (proposal table OR
  phase-level annotations, not both), or some guards unlabeled.
- **Fail (0):** No bias labels on guards.

---

### C-18 — WITHDRAW operator defined with row-level semantics
- **Weight:** aspirational
- **Category:** safety
- **Text:** The confirmation gate defines WITHDRAW as a row-level removal operator
  with explicit syntax (e.g., WITHDRAW [#] or WITHDRAW [2, 4]). WITHDRAW removes
  only the named proposals; remaining proposals are applied. It is explicitly
  distinguished from NO (rejects all proposals) and REVISED (requires user to
  resubmit an edited table).
- **Full pass (2):** WITHDRAW defined with row-level syntax; distinguished from
  both NO and REVISED with explicit behavior statements; apply step handles a
  WITHDRAW reply by removing named rows and applying the remainder.
- **Partial (1):** WITHDRAW mentioned as a reply mode but syntax or distinction
  from REVISED not specified, or behavior after WITHDRAW not stated.
- **Fail (0):** WITHDRAW absent from the confirmation gate.

---

### C-19 — Phase entry/exit conditions making gate sequencing verifiable
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Each gated phase includes explicit entry and exit conditions. Entry
  conditions ("Do NOT open Phase N until Phase N-1 exit criterion is met") block
  phase skipping at the boundary — a violation is detectable before execution
  begins, not inferred from output structure. Exit conditions confirm phase
  completion before the next phase opens. This applies especially to Phase 1
  (defense register), the INERTIA-GATE, and the confirmation gate.
- **Full pass (2):** Entry and exit conditions defined for all gated phases; each
  entry condition references the preceding phase by number; INERTIA-GATE and
  confirmation gate each carry both entry and exit conditions.
- **Partial (1):** Entry or exit conditions present for some gated phases but not
  all, or conditions defined without referencing phase numbers.
- **Fail (0):** No phase entry/exit conditions.

---

### C-20 — Bias labels at every structural guard point
- **Weight:** aspirational
- **Category:** safety
- **Text:** Bias labels are present at every named structural guard in the skill:
  Phase 1 read-barrier, SIGNAL READ-LOCK, INERTIA-GATE, confirmation gate, and
  write guard. C-17 tests whether proposal tables and phases carry bias annotations;
  C-20 tests completeness — no guard is unlabeled or labeled only in a summary
  section. Having labels in proposal tables and some phases but not all guards
  fails this criterion.
- **Full pass (2):** Every named structural guard carries an inline bias label; no
  guard is unlabeled; labels appear at the guard site, not only in a summary or
  rationale section.
- **Partial (1):** Bias labels present at most guards but one or more major guards
  (SIGNAL READ-LOCK, confirmation gate, or write guard) are unlabeled or carry
  only a summary reference.
- **Fail (0):** Bias labels present only in proposal tables, or absent altogether.
```

---

**What changed from v7 → v8:**

| Change | Detail |
|--------|--------|
| Version bump | `version: 7` → `version: 8` |
| Formula denominator | `/ 20` → `/ 24` (12 aspirational criteria × 2 max each) |
| Aspirational range | `C-09–C-18` → `C-09–C-20` |
| C-19 added | Phase entry/exit conditions making gate sequencing verifiable — formalized from V-05 pattern where explicit entry/exit conditions make the INERTIA-GATE structurally bounded (skipping detectable at the boundary, not inferred from output) |
| C-20 added | Bias labels at every structural guard point — formalized from V-05 pattern where bias labels extend beyond proposal table columns and phase-level annotations to cover every named guard inline; C-17 tests the two-level architecture, C-20 tests completeness across all guard sites |

**Why two new criteria rather than one:** C-19 and C-20 test orthogonal properties. A skill can have per-gate entry/exit conditions (C-19) while leaving the write guard or SIGNAL READ-LOCK unlabeled (C-20 fail). A skill can label every guard (C-20) while using soft narrative phrasing that describes phases without explicit entry/exit conditions (C-19 fail). V-05 achieves both simultaneously; the two criteria distinguish that achievement from partial coverage.
