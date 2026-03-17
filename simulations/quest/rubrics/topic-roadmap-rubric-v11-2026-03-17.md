Done. Written to `simulations/quest/rubrics/topic-roadmap-rubric-v11-2026-03-17.md`.

---

**What changed v10 → v11:**

| Change | Detail |
|--------|--------|
| Version bump | 10 → 11 |
| Formula denominator | `/34 * 10` → `/36 * 10` (18 aspirational × 2 = 36 max) |
| Aspirational range | C-09--C-25 → C-09--C-26 |
| **C-26 added** | Consequence field enforcement stated in Phase 5 exit criterion |

**C-26 in brief:** Round 10 shows C-12 partial (1) universally — the consequence column is present in all defeat assessment tables, but no variation states the advancement block in the Phase 5 exit criterion text. C-12 tests column presence + a general blocking mechanism. C-26 tests specifically that the Phase 5 exit criterion names "Consequence if unchanged" as a named advancement condition, verifiable at the phase boundary without reading surrounding prose. Full pass requires the field name to appear in the exit criterion itself.

**Why one criterion, not two:** Round 10 produced a single structural gap. All criteria except C-12 score 2 across all five variations. Subdividing that one gap would generate correlated, not orthogonal, criteria. One criterion closes the gap cleanly.
ectness
- **Text:** Signal inventory and delta analysis are present in the output
  before any proposal table is shown. The inventory classifies each artifact
  as NEW (date > strategy date) or PRIOR.
- **Pass condition:** A signal inventory table appears (at minimum: artifact
  filename, date, NEW/PRIOR, namespace). At least one of the four delta
  categories -- CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED -- is present
  in the output, even if populated with a null declaration. Proposals that
  appear before any delta analysis fail.

---

### C-03 -- Proposals are concrete and action-typed
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

### C-04 -- User confirmation gate is present and blocking
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

### C-05 -- All-namespace coverage with null rows
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

### C-06 -- Null path stop enforced at defeat phase
- **Weight:** recommended
- **Category:** correctness
- **Text:** When all defeat assessment verdicts are HOLDS, the skill emits a
  NULL_DELTA declaration and halts. It does not open the proposal phase for
  zero proposals.
- **Pass condition:** Defeat assessment phase contains an explicit conditional:
  "If all verdicts are HOLDS: Emit NULL_DELTA. Stop. Do not open Phase 6."
  A run that generates an empty proposal table after all-HOLDS verdicts fails.

---

### C-07 -- Confidence tiers defined
- **Weight:** recommended
- **Category:** depth
- **Text:** Proposals carry a confidence level defined with specific evidential
  criteria. The tiers are HIGH, MEDIUM, and LOW; each is tied to the count
  or type of independent NEW artifacts supporting the defeat.
- **Pass condition:** At least three confidence tiers are defined with their
  evidential backing (e.g., HIGH = two+ independent NEW artifacts; MEDIUM =
  one; LOW = inference). Tiers without evidential criteria do not pass.

---

### C-08 -- Consequence-if-unchanged in proposals
- **Weight:** recommended
- **Category:** depth
- **Text:** Every proposal and every defeat assessment row requires a
  "Consequence if unchanged" field. Proposals without a stated consequence do
  not pass the defeat assessment gate and cannot advance to the proposal table.
- **Pass condition:** "Consequence if unchanged" column required in both the
  defeat assessment table and the proposal table. Absent in either location
  is a partial pass.

---

## Aspirational Criteria (scored 0 / 1 / 2 per criterion; max = 36)

### C-09 -- Pre-signal defense register written before reading any file
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

### C-10 -- SIGNAL READ-LOCK enforced after inventory is written
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

### C-11 -- INERTIA-GATE phase sequencing enforcement
- **Weight:** aspirational
- **Category:** correctness
- **Text:** A structural gate labeled INERTIA-GATE (or equivalent) explicitly
  blocks dimensions with HOLDS verdicts from entering the proposal phase. HOLDS
  rows receive a NO CHANGE entry with no path to Phase 6. The gate is not implied
  by phase ordering -- it is explicitly stated as a structural constraint.
- **Full pass (2):** "[INERTIA-GATE: This phase runs only for DEFEATED dimensions]"
  or equivalent explicit label; HOLDS rows explicitly prohibited from reaching the
  proposal phase.
- **Partial (1):** Gate concept present but not explicitly labeled, or HOLDS
  exclusion from proposal phase not stated.
- **Fail (0):** No inertia gate or HOLDS path unguarded.

---

### C-12 -- Consequence column in defeat assessment
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

### C-13 -- DEFEATED/HOLDS verdict semantics
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The defeat assessment uses exactly two verdict tokens with explicit
  semantics: DEFEATED (signal overcomes the pre-registered defense; dimension
  advances to proposals) and HOLDS (defense survives; no proposal generated for
  this dimension). Semantics and consequences are stated explicitly -- not inferred
  from phase ordering.
- **Full pass (2):** DEFEATED and HOLDS defined with semantics; HOLDS explicitly
  maps to "no proposal generated"; consequences of each verdict are stated.
- **Partial (1):** Two verdicts present but semantics not stated, or one verdict's
  consequences are implied rather than explicit.
- **Fail (0):** No explicit verdict vocabulary.

---

### C-14 -- NEW/PRIOR split with explicit date anchor
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

### C-15 -- Confidence levels with evidential criteria
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each proposal carries a confidence level (HIGH / MEDIUM / LOW) with
  specific, countable evidential criteria tied to the number of independent NEW
  artifacts. Level assignment follows a stated rule -- not qualitative judgment
  (e.g., HIGH = two or more independent NEW artifacts; MEDIUM = one; LOW =
  inference only).
- **Full pass (2):** HIGH, MEDIUM, and LOW each defined with specific evidential
  criteria; criteria involve countable artifact independence.
- **Partial (1):** Confidence levels defined but criteria are qualitative
  descriptions without specific counts or artifact-independence requirement.
- **Fail (0):** No confidence levels, or levels without evidential criteria.

---

### C-16 -- Type-labeled nulls for all categories
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

### C-17 -- Bias labels per proposal row and per phase
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

### C-18 -- WITHDRAW operator defined with row-level semantics
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

### C-19 -- Phase entry/exit conditions making gate sequencing verifiable
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Each gated phase includes explicit entry and exit conditions. Entry
  conditions ("Do NOT open Phase N until Phase N-1 exit criterion is met") block
  phase skipping at the boundary -- a violation is detectable before execution
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

### C-20 -- Bias labels at every structural guard point
- **Weight:** aspirational
- **Category:** safety
- **Text:** Bias labels are present at every named structural guard in the skill:
  Phase 1 read-barrier, SIGNAL READ-LOCK, INERTIA-GATE, confirmation gate, and
  write guard. C-17 tests whether proposal tables and phases carry bias annotations;
  C-20 tests completeness -- no guard is unlabeled or labeled only in a summary
  section. Having labels in proposal tables and some phases but not all guards
  fails this criterion.
- **Full pass (2):** Every named structural guard carries an inline bias label; no
  guard is unlabeled; labels appear at the guard site, not only in a summary or
  rationale section.
- **Partial (1):** Bias labels present at most guards but one or more major guards
  (SIGNAL READ-LOCK, confirmation gate, or write guard) are unlabeled or carry
  only a summary reference.
- **Fail (0):** Bias labels present only in proposal tables, or absent altogether.

---

### C-21 -- Dual-site INERTIA-GATE enforcement
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The INERTIA-GATE label appears at two distinct structural sites: the
  entry to the defeat assessment phase (Phase 5) AND the entry to the proposal
  phase (Phase 6). A gate labeled only at Phase 5 permits Phase 6 to be entered
  by a path that bypasses Phase 5 entirely; a gate labeled only at Phase 6 permits
  Phase 5 to run without the inertia framing. The Phase 6 label must restate
  the HOLDS exclusion independently -- referencing Phase 5 by name is not
  sufficient if the exclusion is not self-contained at Phase 6 entry.
- **Full pass (2):** INERTIA-GATE label present at both Phase 5 entry and Phase 6
  entry; the Phase 6 label independently restates the HOLDS exclusion ("HOLDS
  dimensions have no path to this phase") without relying on Phase 5 label
  to carry the constraint.
- **Partial (1):** Gate labeled at one site only; or Phase 6 entry label references
  Phase 5 HOLDS outcome without an independent exclusion statement at the Phase 6
  site.
- **Fail (0):** INERTIA-GATE at one site only with no independent restatement,
  or absent.

---

### C-22 -- Restart isolation clause in Phase 1 read-barrier
- **Weight:** aspirational
- **Category:** safety
- **Text:** The Phase 1 read-barrier includes an explicit clause covering the
  mid-run restart scenario: if execution resumes without prior context, the model
  must not re-read files to reconstruct state. A barrier that only addresses
  the first-run case leaves a restart path unguarded -- any re-read after restart
  contaminates the defense register with post-read evidence as effectively as
  skipping Phase 1 entirely.
- **Full pass (2):** Phase 1 barrier includes an explicit restart clause; the
  clause prohibits re-reading signal files or strategy.md to reconstruct context
  after a restart; the prohibition is stated alongside the first-run constraint,
  not in a separate rationale section.
- **Partial (1):** Restart scenario addressed but prohibition on file re-read
  is not stated; or restart clause present in a rationale section rather than
  integrated into the Phase 1 barrier instruction.
- **Fail (0):** No restart isolation clause; Phase 1 barrier addresses first-run
  case only.

---

### C-23 -- Dedicated verdict vocabulary block before Phase 5
- **Weight:** aspirational
- **Category:** correctness
- **Text:** A standalone verdict vocabulary block defining DEFEATED and HOLDS
  appears before Phase 5 begins. The block contains forward-path statements for
  both verdicts ("DEFEATED: dimension advances to Phase 6" / "HOLDS: dimension
  receives NO CHANGE; no path to Phase 6") as self-contained definitions, not
  embedded within phase instructions. C-13 tests whether verdict semantics are
  defined anywhere in the skill; C-23 tests whether they are encapsulated in a
  block that is independently verifiable -- a reviewer can confirm the semantics
  without reading all phase instructions. Distributing verdict semantics across
  phase framing passes C-13 but fails C-23.
- **Full pass (2):** Dedicated verdict vocabulary block present before Phase 5;
  block defines both DEFEATED (-> Phase 6) and HOLDS (-> NO CHANGE, no path to
  Phase 6) as standalone definitions; block is structurally separate from phase
  instructions (not embedded mid-phase).
- **Partial (1):** Verdict semantics fully defined (C-13 passes) but embedded
  within phase instructions rather than a standalone block; or standalone block
  present but missing one verdict's forward-path.
- **Fail (0):** No dedicated verdict vocabulary block; semantics distributed across
  phases only, or absent.

---

### C-24 -- Structural mechanism spatial separation
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The three structural mechanisms introduced in C-21/C-22/C-23 -- the
  INERTIA-GATE dual-site labels, the restart isolation clause, and the verdict
  vocabulary block -- occupy distinct, non-overlapping sections of the skill.
  Each mechanism must be verifiable in isolation: a reviewer checking the
  INERTIA-GATE labels does not encounter restart-clause text; a reviewer
  checking the verdict block does not encounter gate-exclusion text; Phase 1
  contains only the read-barrier and restart clause, not verdict definitions.
  Spatial co-location defeats independent verifiability even when all three
  mechanisms are textually present. C-21/C-22/C-23 each test whether a mechanism
  exists; C-24 tests whether the three occupy independent sections that do not
  bleed into each other.
- **Full pass (2):** Phase 1 section contains the read-barrier and restart clause
  only (no verdict vocabulary, no INERTIA-GATE exclusion text); the verdict
  vocabulary block is positioned between Phase 4 and Phase 5, contains only
  verdict definitions (no gate labels, no restart text); INERTIA-GATE labels at
  Phase 5 and Phase 6 contain only gate-exclusion text (no verdict redefinitions,
  no restart language); sections do not reference each other's content inline.
- **Partial (1):** All three mechanisms present and in broadly correct positions,
  but one or two sections contain inline text belonging to a different mechanism
  (e.g., Phase 1 barrier embeds a verdict definition alongside the restart clause;
  or the verdict block restates the HOLDS gate exclusion from C-21).
- **Fail (0):** Two or more mechanisms co-located in the same section, or one
  mechanism's text is dispersed across sections.

---

### C-25 -- Phase 5 verdict deferral with anti-duplication clause
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Phase 5 instructions forward-reference the standalone verdict
  vocabulary block (C-23) rather than re-embedding verdict semantics inline.
  The deferral is explicit: Phase 5 names the block by title or location and
  includes a prohibition on redefinition ("Do not redefine here" or equivalent).
  Without the anti-duplication clause, Phase 5 can drift to add inline semantics
  that silently conflict with the standalone block, undermining the single-source
  guarantee that C-23 establishes. C-23 tests whether the standalone block exists
  and is structurally separate; C-25 tests whether Phase 5 actively enforces
  single-source by prohibiting inline redefinition.
- **Full pass (2):** Phase 5 contains an explicit forward-reference to the verdict
  vocabulary block (e.g., "Apply the Verdict Vocabulary block defined above");
  an anti-duplication clause is co-located in Phase 5 ("Do not redefine verdict
  semantics here" or equivalent); Phase 5 contains no inline DEFEATED/HOLDS
  semantic definitions.
- **Partial (1):** Phase 5 forward-references the block but omits the anti-
  duplication clause; or anti-duplication clause present but Phase 5 still
  contains a partial inline semantic definition alongside the reference.
- **Fail (0):** Phase 5 defines verdict semantics inline without referencing the
  standalone block; or no forward-reference and no anti-duplication clause.

---

### C-26 -- Consequence field enforcement stated in Phase 5 exit criterion
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The Phase 5 exit criterion text names the "Consequence if unchanged"
  field as an explicit advancement condition: a row cannot exit Phase 5 and enter
  Phase 6 if its consequence field is unpopulated. C-12 tests whether the
  consequence column exists in the defeat assessment table and whether a blocking
  mechanism exists; C-26 tests specifically whether that blocking rule is stated
  in the Phase 5 exit criterion text as a named condition. A skill where the column
  is present and a preamble note implies enforcement satisfies C-12 partial but
  fails C-26 -- the exit criterion text must carry the rule explicitly, making
  the gate verifiable at the phase boundary without reading the surrounding prose.
  This is the pattern universally absent in Round 10: all variations have the
  consequence column in the defeat assessment, but none state the advancement
  block in the exit criterion text itself.
- **Full pass (2):** Phase 5 exit criterion contains an explicit named condition
  referencing the "Consequence if unchanged" field (e.g., "Exit blocked if any
  DEFEATED row has an empty Consequence field"); the condition names the field by
  its column header; the rule appears in the exit criterion, not only in a preamble,
  rationale, or table note.
- **Partial (1):** Phase 5 exit criterion references completeness of the defeat
  assessment table without naming the consequence field explicitly; or the
  consequence advancement block is stated in a preamble or rationale section
  adjacent to the exit criterion rather than within the exit criterion text itself.
- **Fail (0):** Phase 5 exit criterion governs advancement by verdict alone
  (DEFEATED advances, HOLDS does not) with no mention of consequence field
  population; or Phase 5 has no exit criterion.

---

## What changed from v10 -> v11

| Change | Detail |
|--------|--------|
| Version bump | version: 10 -> version: 11 |
| Formula denominator | / 34 -> / 36 (18 aspirational criteria x 2 max each) |
| Aspirational range | C-09--C-25 -> C-09--C-26 |
| C-26 added | Consequence field enforcement stated in Phase 5 exit criterion -- from Round 10 C-12 universal partial pattern: all five variations have the consequence column in the defeat assessment table, but none state the advancement block in the Phase 5 exit criterion text itself; C-12 tests column presence + a general blocking mechanism; C-26 tests specifically that the blocking rule is a named condition in the exit criterion text, verifiable at the phase boundary without reading surrounding prose |

**Why one new criterion rather than two:** Round 10 produced a single structural
gap. C-12 is partial (1) across all five variations because enforcement is
structural/implied rather than explicit in the exit criterion text. That gap is
precisely scoped: the exit criterion text must name the consequence field as an
advancement condition. Adding a second criterion from the same gap would
subdivide a single rule, not capture an orthogonal pattern. The Round 10 session
achieves full pass on C-09--C-11, C-13--C-25 (all 2); the only unachieved
full pass is C-12, and C-26 captures the exact mechanism needed to close it.

**Orthogonality with C-12:**
- C-12 partial, C-26 fail: consequence column present in defeat assessment,
  exit criterion names no field condition (Round 10 state for all variations).
- C-12 partial, C-26 partial: consequence column present, exit criterion
  references table completeness but not the field by name.
- C-12 full, C-26 pass: consequence column present + exit criterion explicitly
  names the field as an advancement condition (the Round 11 target state).
- C-12 fail, C-26 fail: no consequence column anywhere (both fail together).
