Here is the complete updated rubric:

---

# Scoring Rubric -- topic-roadmap (topic-plan) v14

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 13 -> 14 |
| Formula denominator | `/44 * 10` -> `/50 * 10` (25 aspirational x 2 = 50 max) |
| Aspirational range | C-09--C-30 -> C-09--C-33 |
| **C-31 added** | PROPOSAL BIAS AUDIT guard at Phase 6 entry |
| **C-32 added** | Phase 6 SECTION SCOPE includes row-level bias labeling |
| **C-33 added** | Output Schema CONTRACT pre-commits consequence field name and bias column |

---

## Three new aspirational criteria

### C-31 -- PROPOSAL BIAS AUDIT guard at Phase 6 entry
**Category:** safety

A named enforcement point at Phase 6 entry. The guard text distinguishes per-row bias labeling (prevents motivated reasoning at the individual proposal decision surface) from phase-level annotations (prevents systemic phase structure bias) and explains why both are required -- not merely asserts presence. C-30 tests whether the column is in the table schema; C-31 tests whether Phase 6 entry carries a named guard with the structural rationale.

- **Full (2):** Named guard at Phase 6 entry, co-located with INERTIA-GATE label; guard text distinguishes the two labeling levels and explains the distinct failure mode each addresses.
- **Partial (1):** Guard present but lacks the explanatory distinction; or guard is in a preamble section rather than at phase entry.
- **Fail (0):** No named guard at Phase 6 entry.

### C-32 -- Phase 6 SECTION SCOPE includes row-level bias labeling
**Category:** correctness

The Phase 6 SECTION SCOPE declaration explicitly adds "row-level bias labeling" to its scope text. Without this update, a C-24 auditor checking Phase 6's declared scope would find the C-31 guard operating on content not named in that scope -- a spatial separation violation introduced by adding C-31. C-24 tests the three pre-existing mechanisms; C-32 tests whether Phase 6's scope declaration is updated to preserve C-24 after C-31 is added.

- **Full (2):** SECTION SCOPE text reads (e.g.) "gate-exclusion text, proposal generation, and row-level bias labeling"; co-located with Phase 6 INERTIA-GATE.
- **Partial (1):** SECTION SCOPE present but not updated; or row-level bias labeling mentioned in Phase 6 preamble but not in the scope declaration.
- **Fail (0):** No SECTION SCOPE declaration, or SECTION SCOPE unchanged from pre-C-31 form.

### C-33 -- Output Schema CONTRACT pre-commits consequence field name and bias column
**Category:** correctness

An OUTPUT SCHEMA CONTRACT block before any file read pre-commits both (a) the exact consequence field name at all three C-29 sites and (b) "Bias blocked by guard" as a required Phase 6 column. Makes C-29 naming drift and C-30 column absence detectable from the schema block alone. V-05's CONTRACT A + CONTRACT B is the reference. C-29 tests naming identity at runtime; C-33 tests pre-execution commitment. C-30 tests column presence in the table; C-33 tests contractual declaration before any file is read.

- **Full (2):** CONTRACT block before any file read; pre-commits both consequence field name (naming all three sites) and "Bias blocked by guard" column; both failures detectable from the block alone.
- **Partial (1):** Contract block present but pre-commits only one of the two elements; or block is positioned after a file read instruction.
- **Fail (0):** No schema CONTRACT block; or CONTRACT appears after Phase 1 begins.

---

**Orthogonality:** All three are independent. C-31 fail / C-32 fail / C-33 fail = no guard, no scope update, no contract. C-31+C-32 pass / C-33 fail = guard + scope correct, no upfront pre-commitment. Full pass on all three = V-05 R13 target state.

**R13 score ceiling under v14:** V-04 and V-05 (44/44 under v13) score 44/50 = 8.80 without targeting C-31/C-32/C-33, giving R14 three independent targets with 6 points of headroom.
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

## Aspirational Criteria (scored 0 / 1 / 2 per criterion; max = 50)

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

### C-27 -- Schema column header and exit criterion field name are lexically identical
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The Phase 5 defeat assessment table column header and the field name
  cited in the Phase 5 exit criterion must use exactly the same string. The R11
  V-01 failure demonstrates the failure mode: the table column was renamed to
  "Consequence if unchanged" but the exit criterion was not updated, leaving the
  field name absent from the boundary check entirely. A variation that renames the
  column but leaves the exit criterion unchanged produces C-26=0 regardless of the
  column's presence. C-12 tests whether the column and a blocking mechanism exist;
  C-26 tests whether the exit criterion names the field; C-27 tests whether the
  two names match -- closing the gap where column and criterion are updated
  independently and drift apart. Mismatched naming creates a verifiability failure:
  a reviewer reading only the exit criterion cannot confirm which column the rule
  applies to.
- **Full pass (2):** The column header in the Phase 5 defeat assessment table and
  the field name in the Phase 5 exit criterion are lexically identical (both read
  "Consequence if unchanged" or a single consistent alternative); this match is
  verifiable without reading surrounding prose.
- **Partial (1):** Both the column header and the exit criterion reference the
  consequence concept, but use different terms (e.g., column says "Consequence if
  unchanged," exit criterion says "consequence field" or "impact if not addressed");
  intent matches but lexical identity fails.
- **Fail (0):** Exit criterion does not name a consequence field at all; or column
  header is absent; or the V-01 pattern -- column renamed, exit criterion
  unchanged -- yielding one site updated and the other not.

---

### C-28 -- Dual-site blocking enforcement: preamble before table + exit criterion at phase boundary
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The blocking rule for "Consequence if unchanged" must be stated at two
  structurally independent sites within Phase 5: (1) a preamble before the defeat
  assessment table that asserts the blocking rule before any row is evaluated, and
  (2) the Phase 5 exit criterion that names the consequence field as an advancement
  condition at the phase boundary. The R11 high-scoring variations (V-02 through
  V-05) achieve C-12 full and C-26 full simultaneously via this dual-placement
  pattern. The two sites are orthogonal: the preamble guards table entry (no row
  may be evaluated without the field); the exit criterion guards phase departure
  (no DEFEATED row may advance without the field populated). A skill with only one
  site is vulnerable to the gap the absent site closes. C-12 tests column presence
  and general blocking; C-26 tests exit criterion naming; C-28 tests that both
  enforcement sites exist independently, without either referencing the other.
- **Full pass (2):** A preamble before the Phase 5 defeat assessment table
  explicitly states that rows with an empty "Consequence if unchanged" field
  cannot be evaluated or advance; AND the Phase 5 exit criterion independently
  names "Consequence if unchanged" as a named advancement condition; each site
  is self-contained and states the rule without delegating to the other site.
- **Partial (1):** Blocking rule stated at one site (preamble only, or exit
  criterion only) but not both; or both sites present but one cross-references
  the other ("as stated in the preamble above") rather than stating the rule
  independently.
- **Fail (0):** Consequence blocking appears only in a rationale or note section,
  not at either structural site; or only one site is present and it references
  the absent site without carrying the rule itself.

---

### C-29 -- Three-way consequence field name identity across all naming sites
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The consequence field name must be lexically identical across all
  three sites where it appears: (1) the Phase 5 defeat assessment table column
  header, (2) the proposal table column header (Phase 6), and (3) the Phase 5
  exit criterion field name. C-27 closes the defeat-assessment↔exit-criterion
  pairing; C-29 extends the identity requirement to include the proposal table
  column, closing the gap isolated by R12 V-02. In V-02, the defeat assessment
  column was deliberately named "Consequence if HOLDS" while the proposal column
  and exit criterion used "Consequence if unchanged" -- producing C-27 partial
  and C-08 partial from the same root cause: naming drifted between the two
  tables independently of the exit criterion. Three sites, three independent
  edit operations, three opportunities for drift. All three must resolve to the
  same string. A reviewer checking any single site must be able to confirm which
  column the blocking rule applies to in all other sites without reading
  surrounding prose.
- **Full pass (2):** The Phase 5 defeat assessment column header, the Phase 6
  proposal table column header, and the Phase 5 exit criterion field name are
  all lexically identical (e.g., all three read "Consequence if unchanged");
  the identity is verifiable at each site independently.
- **Partial (1):** Two of the three sites use identical names but the third
  diverges (e.g., defeat assessment = "Consequence if HOLDS", proposal table =
  "Consequence if unchanged", exit criterion = "Consequence if unchanged" -- the
  V-02 R12 pattern); or all three reference the same concept but use different
  phrasing.
- **Fail (0):** None of the three sites use the same term; or the consequence
  column is absent at one or more sites; or naming was updated at one site
  without propagating to the others.

---

### C-30 -- Proposal table bias column present at row level
- **Weight:** aspirational
- **Category:** safety
- **Text:** The proposal table (Phase 6) includes a dedicated "Bias blocked by
  guard" column (or equivalent) that names, at the row level, the cognitive bias
  each structural guard prevents for that specific proposal. C-17 tests whether
  bias labels appear at both the proposal-table level and the phase-annotation
  level; C-30 isolates the proposal-table row-level column as a separately
  testable structural feature. The distinction matters because phase-level
  annotations (which label the bias prevented by an entire phase) and row-level
  columns (which label the bias prevented for a specific proposal row by its
  guard) address different failure modes: phase annotations prevent systemic
  bias in the phase structure; row-level columns prevent motivated reasoning
  at the individual proposal decision surface. The persistent C-17=1 pattern
  across R12 V-01 and V-02 traces to this specific absence -- per-phase
  annotations are present in both, the proposal table column is absent in both.
  C-17 full requires both; C-30 tests the row-level column alone, allowing
  independent verification of this specific structural feature.
- **Full pass (2):** A "Bias blocked by guard" column (or equivalent named column)
  is present in the proposal table; each proposal row carries a bias label naming
  the cognitive bias the gate prevents at that row's decision point; the column
  is present in the proposal table schema, not supplied only in a preamble or
  rationale section.
- **Partial (1):** Bias labeling appears in a proposal table preamble or rationale
  section but not as a per-row column; or the column is present but most rows
  carry only a null or generic label without naming the specific bias.
- **Fail (0):** No bias column or per-row bias label in the proposal table; bias
  information present only at the phase-annotation level.

---

### C-31 -- PROPOSAL BIAS AUDIT guard at Phase 6 entry
- **Weight:** aspirational
- **Category:** safety
- **Text:** A named enforcement point ("PROPOSAL BIAS AUDIT" or equivalent) appears
  at Phase 6 entry. The guard text explicitly distinguishes per-row bias labeling
  (the "Bias blocked by guard" column in the proposal table, which prevents
  motivated reasoning at the individual proposal decision surface) from phase-level
  annotations (which prevent systemic bias in the phase structure). The guard
  explains why both levels are required -- not merely asserts that both are present.
  C-17 tests whether both bias-labeling levels are present; C-30 tests whether
  the row-level column is present in the proposal table schema; C-31 tests whether
  Phase 6 has a named enforcement site that makes the requirement independently
  verifiable at the phase entry point and explains the structural rationale for
  requiring both levels. A variation that has the column (C-30 full) and phase
  annotations (contributing to C-17 full) but no named guard at Phase 6 entry
  passes C-30 and C-17 but fails C-31 -- the distinction is detectable at phase
  entry without reading the table schema or phase annotations.
- **Full pass (2):** A named guard appears at Phase 6 entry before the proposal
  table is opened; the guard text explicitly distinguishes per-row bias labeling
  from phase-level annotations; the guard explains why both levels are required
  (naming the distinct failure modes each level addresses); the guard is
  structurally co-located with the INERTIA-GATE label at Phase 6 entry or
  immediately follows it.
- **Partial (1):** A guard at Phase 6 entry is present but does not explain why
  both labeling levels are required; or the guard asserts that both are required
  without distinguishing the failure mode each level addresses; or the guard
  appears in a Phase 6 preamble section rather than at the phase entry point
  alongside the INERTIA-GATE.
- **Fail (0):** No named guard at Phase 6 entry for bias labeling; bias requirements
  appear only in the table schema or in a rationale section without a dedicated
  Phase 6 enforcement point.

---

### C-32 -- Phase 6 SECTION SCOPE declaration includes row-level bias labeling
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The Phase 6 SECTION SCOPE declaration explicitly names row-level bias
  labeling as within scope. C-24 tests that Phase 1 (read-barrier + restart clause),
  the verdict vocabulary block, and INERTIA-GATE labels occupy non-overlapping
  sections. When C-31 adds a PROPOSAL BIAS AUDIT guard to Phase 6, the Phase 6
  SECTION SCOPE must be updated to include row-level bias labeling -- a C-24
  auditor reading only the SECTION SCOPE declaration would otherwise see a guard
  whose subject is not declared within Phase 6's scope, producing a spatial
  separation failure even though the guard content is correctly limited to Phase 6.
  C-32 is a scope-declaration test, not a content test: C-30 tests whether the
  bias column is present in the table schema; C-31 tests whether a named guard
  explains the requirement; C-32 tests whether Phase 6's own scope declaration
  claims row-level bias labeling as a Phase 6 responsibility, making the full
  set of Phase 6 structural obligations auditable from the scope line alone.
- **Full pass (2):** Phase 6 SECTION SCOPE text explicitly names row-level bias
  labeling as within scope (e.g., "gate-exclusion text, proposal generation, and
  row-level bias labeling"); the SECTION SCOPE declaration is co-located with or
  immediately follows the Phase 6 INERTIA-GATE label; the scope text does not
  bleed into Phase 5 or Phase 7 content.
- **Partial (1):** Phase 6 SECTION SCOPE is present but does not name row-level
  bias labeling explicitly; or row-level bias labeling is referenced in Phase 6
  preamble text but not added to the formal SECTION SCOPE declaration; or SECTION
  SCOPE is absent entirely but the Phase 6 entry block otherwise covers gate-
  exclusion and proposal generation.
- **Fail (0):** No Phase 6 SECTION SCOPE declaration; or SECTION SCOPE present
  but its text is unchanged from a version predating C-31 (names gate-exclusion
  and proposal generation only, with no row-level bias mention), leaving the C-31
  guard unscoped.

---

### C-33 -- Output Schema CONTRACT pre-commits consequence field name and bias column
- **Weight:** aspirational
- **Category:** correctness
- **Text:** An OUTPUT SCHEMA CONTRACT block, positioned before any file read
  instruction, pre-commits both (a) the exact consequence field name used at all
  three sites (Phase 5 defeat assessment column, Phase 6 proposal table column,
  Phase 5 exit criterion) and (b) the "Bias blocked by guard" column as a required
  structural element of Phase 6 proposal tables. The contract makes a C-29 failure
  (naming drift across consequence sites) or a C-30 failure (missing bias column)
  detectable from the schema block alone -- a reviewer does not need to read Phase 5
  or Phase 6 to verify the commitment. C-29 tests three-way naming identity at the
  sites where the names appear; C-33 tests whether the schema pre-commits the names
  before execution begins, shifting the verification point upstream. C-30 tests
  whether the "Bias blocked by guard" column is present in the proposal table at
  runtime; C-33 tests whether the column is contractually declared in the output
  schema before any file is read, making absence a schema violation detectable
  without running the skill. V-05's dual CONTRACT A + CONTRACT B pattern is the
  reference implementation: CONTRACT A names "Consequence if unchanged" as the
  pre-committed field name at all three sites; CONTRACT B names "Bias blocked by
  guard" as the pre-committed column in Phase 6 proposal tables.
- **Full pass (2):** An OUTPUT SCHEMA CONTRACT block appears before any file read
  instruction; the block pre-commits both the consequence field name (naming all
  three sites explicitly) and the "Bias blocked by guard" column in Phase 6 tables;
  a reviewer can detect a C-29 failure (naming drift) or a C-30 failure (missing
  bias column) from this block without reading Phase 5 or Phase 6.
- **Partial (1):** A schema contract block is present before file reads but
  pre-commits only one of the two required elements (consequence field name OR
  bias column, not both); or the block is positioned after a file read instruction,
  making it a post-hoc statement rather than a pre-commitment; or the consequence
  field name is pre-committed but the three sites are not explicitly named.
- **Fail (0):** No output schema contract block; consequence field name and bias
  column stated only within phase instructions without an upfront pre-commitment;
  or a CONTRACT block is present but appears after Phase 1 begins.

---

## What changed from v13 -> v14

| Change | Detail |
|--------|--------|
| Version bump | 13 -> 14 |
| Formula denominator | `/44 * 10` -> `/50 * 10` (25 aspirational x 2 = 50 max) |
| Aspirational range | C-09--C-30 -> C-09--C-33 |
| **C-31 added** | PROPOSAL BIAS AUDIT guard at Phase 6 entry: named enforcement point explaining why per-row and per-phase bias labeling are structurally distinct requirements |
| **C-32 added** | Phase 6 SECTION SCOPE includes row-level bias labeling: scope declaration explicitly claims row-level bias labeling as a Phase 6 responsibility, keeping C-24 spatial separation intact |
| **C-33 added** | Output Schema CONTRACT pre-commits consequence field name and bias column: upstream pre-commitment makes C-29/C-30 failures detectable from the schema block before any file is read |

**C-31 source:** V-04 and V-05 add a PROPOSAL BIAS AUDIT guard at Phase 6 entry
that explains why both per-row labeling and phase-level annotations are required --
phase annotations address systemic phase structure bias; row-level column addresses
motivated reasoning at the individual proposal decision surface. This closes C-30
via a named enforcement site that makes the row-level requirement independently
verifiable at phase entry. C-30 tests whether the column is present in the schema;
C-31 tests whether Phase 6 entry carries a named guard that explains the structural
rationale, making the requirement detectable without reading the table definition.

**C-32 source:** V-04's Phase 6 SECTION SCOPE reads "gate-exclusion text, proposal
generation, and row-level bias labeling." The scope extension is necessary: without
it, a C-24 auditor checking Phase 6's declared scope would find the PROPOSAL BIAS
AUDIT guard operating on content (row-level bias) not named in Phase 6's SECTION
SCOPE, producing a spatial separation violation from the C-32 guard addition alone.
C-24 tests whether the three pre-existing mechanisms are spatially separated; C-32
tests whether Phase 6's scope declaration is updated to include the new enforcement
obligation so that C-24 spatial separation is preserved after C-31 is added.

**C-33 source:** V-05's dual CONTRACT A + CONTRACT B locks in both "Consequence if
unchanged" (Phase 5 defeat assessment, Phase 5 exit criterion, Phase 6 proposal
table -- all three C-29 sites) and "Bias blocked by guard" (Phase 6 tables) before
any file is read. A reviewer can detect a C-29 naming drift or a C-30 column
absence from the schema block alone, without reading Phase 5 or Phase 6. C-29 tests
naming identity at the three sites at runtime; C-33 tests whether the names are
pre-committed before execution begins. C-30 tests column presence in the table;
C-33 tests whether the column is contractually declared in the schema, shifting
verification upstream. V-04 has a single CONTRACT covering consequence field name;
V-05 extends it to CONTRACT A + CONTRACT B, adding the bias column. C-33 full
requires both commitments; C-33 partial covers one.

**Why three, not two:** C-31, C-32, and C-33 are mutually orthogonal. A variation
can pass C-31 (Phase 6 guard present with explanation) while failing C-32 (Phase 6
SECTION SCOPE not updated) or failing C-33 (no upfront schema CONTRACT). A variation
can pass C-32 (SECTION SCOPE updated) while failing C-31 (no named guard) or C-33.
A variation can pass C-33 (dual CONTRACT present) while failing C-31 (no Phase 6
guard) or C-32 (SECTION SCOPE not updated). All three address different verifiability
surfaces: C-31 = phase-entry enforcement, C-32 = scope declaration integrity,
C-33 = pre-execution schema commitment.

**Orthogonality matrix:**

- C-31 fail, C-32 fail, C-33 fail: no Phase 6 guard, no SECTION SCOPE update, no
  schema CONTRACT (R13 V-01 pattern for C-31/C-32; base pattern without schema block).
- C-31 pass, C-32 fail, C-33 fail: Phase 6 guard present with explanation; SECTION
  SCOPE not updated; no schema CONTRACT.
- C-31 pass, C-32 pass, C-33 fail: Phase 6 guard present; SECTION SCOPE updated;
  no schema CONTRACT pre-committing both names.
- C-31 pass, C-32 pass, C-33 partial: Phase 6 guard present; SECTION SCOPE updated;
  schema CONTRACT covers one element (consequence name OR bias column, not both).
- C-31 pass, C-32 pass, C-33 pass: Phase 6 guard with explanation; SECTION SCOPE
  includes row-level bias labeling; dual CONTRACT pre-commits both consequence
  field name and bias column (V-05 R13 target state).

**Score ceiling at R13 base:** V-04 and V-05 both scored 44/44 (10.00) under v13.
Under v14 they would score 44/50 = 8.80 without targeting C-31/C-32/C-33,
providing headroom for R14 to chase all three. V-01's C-31 gap (no Phase 6 guard),
V-01's C-32 gap (SECTION SCOPE not updated), and V-01's C-33 gap (single CONTRACT
only, not dual) isolate the three independent targets.
