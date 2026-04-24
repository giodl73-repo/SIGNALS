The user is declining the Bash commands. Let me output the complete v9 rubric as Markdown as requested, and note the file wasn't written:

---

# corps-scan Rubric v9 -- 2026-03-17

## What is new in v9

**Four new criteria from R8 (V-05 excellence signals):**

**C-35 -- Incompleteness predicate expressed as blockquote enabling rendered-markdown scan surface**
(requires C-33)
Beyond C-33 (predicate as first structural element of each phase body). The "Phase N is not
complete until X" predicate uses rendered-markdown blockquote syntax (> prefix), making it
visually and syntactically distinct from surrounding prose, ENTRY blocks, and IVR triple text.
The blockquote format creates a fourth independent audit surface beyond the three required by
C-31: a reviewer scanning rendered markdown locates all incompleteness predicates by visual
inspection of blockquote elements alone, without reading ENTRY blocks, IVR triples, or the
phase-contract table. C-33 can pass with bold-caps or plain prose; C-35 requires blockquote
syntax. A prompt where predicates satisfy C-33 ordering but use bold-caps or plain prose does
not pass. Requires C-33.

**C-36 -- Constraint manifest carries VIOLATION column making it a mini-IVR anti-pattern reference**
(requires C-28 + C-34)
Beyond C-28 (manifest enumerates labels with count) and C-34 (manifest has terminal TOTAL row).
The constraint manifest includes a dedicated VIOLATION column alongside each IVR triple label,
naming the concrete anti-pattern for that constraint. This converts the manifest from a bare
label-and-count list into a mini-IVR reference table: a reviewer can confirm both what is
required and what the specific failure looks like from the manifest alone, without navigating to
the phase body containing that triple. Anti-patterns for all labeled constraints become scannable
from the manifest, creating an independent failure-detection surface that requires no phase-body
traversal. A manifest that lists labels, counts, and a TOTAL row but omits the VIOLATION column
does not pass. A VIOLATION column present in any other table does not satisfy this criterion.
Evidence: V-02 "VIOLATION column makes manifest a mini-IVR anti-pattern reference; anti-patterns
scannable from manifest without reading phase bodies." Requires C-28 and C-34 to both pass.

**C-37 -- Phase-contract table carries test-item-count column enabling mechanical cross-check**
(requires C-32)
Beyond C-32 (phase-contract table as front-matter covering all phases). The phase-contract
summary table includes a dedicated column stating the number of YES/NO checklist items that each
phase's completion test block contains. The count declared in each row must equal the actual
number of items present in the corresponding directed completion test block in the phase body.
This creates a mechanical cross-check: a reviewer can verify that no test block has been
truncated or extended by comparing the table count to the actual item count, without reading
full phase body prose. A phase-contract table that includes ENTRY preconditions, incompleteness
predicate, test directive, and conditional advance columns but omits the test-item-count column
does not pass even if all other phase contract elements are present. A count column in any table
other than the phase-contract front-matter table does not satisfy this criterion. Evidence: V-03
"count column in contract table creates cross-check: table count must equal YES/NO items in test
block; mechanical discrepancy detection." Requires C-32 to pass.

**C-38 -- Cross-manifest count invariant: CONSTRAINT MANIFEST TOTAL equals sum of phase test-item counts**
(requires C-34 + C-37)
Beyond C-34 (manifest TOTAL row) and C-37 (phase-contract test-item-count column). The
CONSTRAINT MANIFEST TOTAL row (declaring the count of labeled IVR triples) and the sum of the
per-phase test-item-count column values in the PHASE CONTRACT TABLE declare the same count from
two structurally independent front-matter perspectives. In a well-formed prompt the two values
must be equal: N labeled IVR triples equals N total completion test items across all phases.
A discrepancy between the manifest TOTAL and the sum of phase test-item counts is mechanically
detectable by arithmetic on the two front-matter tables without reading any phase body. Having
two independent front-matter tables anchoring the same count creates the strongest available
cross-manifest invariant: a single table corruption cannot satisfy both tables simultaneously.
A prompt where the manifest TOTAL and the phase-contract item-count sum agree but only because
the count column is absent in the phase-contract table does not pass -- both C-34 and C-37 must
be independently satisfied. A prompt where the two counts disagree does not pass even if each
table is internally consistent. Evidence: V-05 "Cross-manifest count invariant -- CONSTRAINT
MANIFEST TOTAL (14) equals sum of all phase test-item counts in PHASE CONTRACT TABLE (P1=2,
P2=5, P3=6, P4=1, total=14); discrepancy between the two front-matter values mechanically
detectable without reading any phase body." Requires C-34 and C-37 to both pass.

**Score: 340 --> 380 pts max. 34 --> 38 criteria. Golden threshold unchanged.**

---

## What carried forward from v8

**C-31 -- Multi-surface verification: completion infrastructure anchored on three independent surfaces**
V-05 (R7). Three structurally independent audit surfaces simultaneously present: constraint
manifest (C-28), phase-contract front-matter table (C-32), and canonical predicate phrasing at
phase-body openings (C-33). Each surface independently sufficient; all three required. A prompt
satisfying C-28/C-29/C-30 via only one or two surfaces does not pass. Requires C-28, C-29,
and C-30.

**C-32 -- Phase-contract table placed as front-matter before any phase body**
V-01/V-04/V-05 (R7). Complete phase contract architecture (ENTRY + incompleteness predicate +
test directive + conditional advance) for all phases collected into a single summary table
appearing before any phase body. Partial tables covering only selected phases do not pass.
Contracts within individual phase body sections only, without the front-matter table, do not
pass even if C-29 and C-30 are otherwise satisfied. Requires C-29 and C-30.

**C-33 -- Incompleteness predicate is the first structural element of each phase body**
V-03/V-05 (R7). The "Phase N is not complete until X" predicate must be the FIRST line of each
phase body -- before the ENTRY block, before IVR triples, before any prose. This ordering makes
C-15/C-30 compliance checkable by scanning only the opening line of each phase section. A prompt
where the predicate appears after ENTRY declarations, after IVR triples, or only in a summary
table does not pass. Requires C-15 and C-30.

**C-34 -- Constraint manifest uses terminal count row matching the gate-row sentinel pattern**
V-02/V-04/V-05 (R7). The constraint manifest (C-28) applies the same structural device as the
inventory gate row (C-14): a terminal sentinel row whose stated value must match a mechanical
count -- e.g., "| TOTAL | 14 labeled triples -- count to verify completeness |". A manifest
that lists labels and states a count in prose but does not use a structured terminal row does
not pass. A TOTAL row in any table other than the constraint manifest does not satisfy this
criterion. Requires C-14 and C-28.

---

## What carried forward from v7

**C-28 -- META-RULE enumerates all IVR triples by label with a count instruction**
V-01/V-02 (R6). C-26 requires an explicit meta-rule declaring informal constraints non-binding;
C-28 additionally requires the meta-rule to function as an exhaustive labeled manifest: lists
every IVR triple by its structural label and states the total count. Discrepancy detection becomes
mechanical. Requires C-25 and C-26.

**C-29 -- Explicit ENTRY contracts at phase start pairing with EXIT contracts**
V-02 (R6). C-27 requires each phase's completion test to include a conditional advance instruction;
C-29 additionally requires each phase to open with a formal ENTRY contract block declaring the
preconditions that must already hold before that phase begins. Requires C-27.

**C-30 -- Completion infrastructure covers every phase without exception**
V-02 (R6). C-30 requires the full suite -- incompleteness predicate, directed visible test block,
and conditional advance instruction -- to be present for every phase. Requires C-15, C-17,
and C-27.

---

## What carried forward from v6

**C-23 -- Inline detected-from: traceability field embedded in YAML team entries**
V-01 (R5). Requires C-02 and C-09.

**C-24 -- Pivot mode candidates enumerated before selection**
V-01 (R5). Requires C-06 and C-12.

**C-25 -- Each IVR triple carries a phase-scoped structural label**
V-01/V-02/V-03 (R5). Requires C-22.

**C-26 -- Formal constraint system contains explicit meta-rule declaring informal constraints non-binding**
V-02 (R5). Requires C-22 and C-25.

**C-27 -- Completion test includes explicit conditional advance instruction**
V-03 (R5). Requires C-17.

---

## What carried forward from v5

**C-20 -- Amend phase names an explicit anti-pattern for non-actionable offers**
V-01/V-02 (R4). Requires C-08.

**C-21 -- Each gate labeled with a category name identifying its enforcement type**
V-01/V-02 (R4). Requires C-19.

**C-22 -- Every structural constraint in every phase expressed as a separate IVR triple**
V-01/V-02 (R4). Requires C-18.

---

## Score table

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 -- C-05 | 50 pts |
| Recommended | C-06 -- C-08 | 30 pts |
| Aspirational | C-09 -- C-38 | 300 pts |
| **Total** | 38 criteria | **380 pts** |

Golden threshold unchanged at >= 80 pts composite with all 5 essentials passing.

---

## ESSENTIAL

Five criteria. Each worth 10 pts (50 pts total if all pass). Any essential failure disqualifies
the output from golden regardless of composite score.

---

**C-01 -- Valid org.yaml code fence produced**
- Weight: essential
- Category: format
- Pass condition: Output contains a single `yaml` code fence identified as `org.yaml` that
  includes at minimum the keys `groups:`, `teams:`, and `exec-office:`. Output in any other
  format -- prose description of an org chart, JSON, an informal bullet list of team names, or a
  partial YAML fragment -- does not pass. A code fence containing only partial key coverage (e.g.,
  teams but no groups) does not pass.

**C-02 -- Team areas derived from repo signals**
- Weight: essential
- Category: coverage
- Pass condition: Team names and group structure in the YAML are grounded in actual repo signals
  (directory names, service paths, module identifiers, domain terms) rather than invented or
  generic. At least half the team names must have a traceable basis in repo signals named
  somewhere in the output -- pre-YAML inventory, inline YAML comment, or prose explanation. A
  fully generic org chart (e.g., Frontend / Backend / Infrastructure with no repo grounding)
  fails even if syntactically valid.

**C-03 -- Group structure organizes teams**
- Weight: essential
- Category: correctness
- Pass condition: The YAML `groups:` section contains at least one named group container that
  organizes teams beneath it. An org.yaml that lists teams at the top level without grouping
  them fails -- group structure is required for corps-build and corps-rob compatibility. A single
  group containing all teams passes; a flat team list with no group hierarchy does not.

**C-04 -- Standard roles present per team**
- Weight: essential
- Category: coverage
- Pass condition: Each team entry in the YAML includes a `roles:` list with at least one named
  role. Role names must be substantive (e.g., "Product Manager", "Engineer", "Tech Lead") rather
  than placeholder tokens (e.g., "role_1", "TBD"). The Inertia Advocate must NOT appear in the
  draft output -- it is auto-added by corps-build and is outside corps-scan scope.

**C-05 -- Does not write .roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present `.roles/` file markdown. Any output that writes role files or presents role
  file markdown in any form fails. This boundary (scan = draft org.yaml only; build = role
  files) must be respected unconditionally.

---

## RECOMMENDED

Three criteria. Each worth 10 pts (30 pts total if all pass).

---

**C-06 -- Pivot mode declared with rationale**
- Weight: recommended
- Category: format
- Pass condition: Output names the pivot mode used (directory / concept / service / domain) and
  provides at least one sentence explaining why that mode was selected based on observed repo
  signals. Declaring a mode without rationale does not pass. Note: C-12 further requires the
  rationale to cite a specific named signal; C-06 passes with any explanatory sentence.

**C-07 -- Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: `org.yaml` contains an `exec-office:` section with at least a name field, even
  if no teams are listed under it.

**C-08 -- Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable. A generic "let me know if you want changes" does not pass.

---

## ASPIRATIONAL

Thirty criteria. Each worth 10 pts (300 pts total if all pass).

C-09 and C-10 carry forward from v1. C-11, C-12, C-13 added in v2. C-14, C-15, C-16 added in
v3. C-17, C-18, C-19 added in v4. C-20, C-21, C-22 added in v5. C-23, C-24, C-25, C-26, C-27
added in v6. C-28, C-29, C-30 added in v7. C-31, C-32, C-33, C-34 added in v8.
C-35, C-36, C-37, C-38 new in v9.

---

**C-09 -- Pre-YAML scan inventory listed**
- Weight: aspirational
- Category: depth
- Pass condition: Before the YAML block, the output lists the repo signals it detected as a
  readable inventory of directory names, service paths, module identifiers, or domain terms. The
  inventory must be structurally distinct from the YAML and must appear before the YAML block
  begins. Outputs with only inline YAML comments but no pre-YAML inventory do not pass.

**C-10 -- Draft boundary stated before first structural content**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only framing is stated explicitly before any YAML or structural
  content appears. Burying the boundary acknowledgment after the YAML, or only at the very end,
  does not pass. PARTIAL case: a scope constraint block present at the top of the prompt but
  with no explicit instruction directing the model to output the boundary statement as its first
  visible line earns PARTIAL -- the constraint must direct model output, not merely inform model
  context.

**C-11 -- Inventory formatted as typed table**
- Weight: aspirational
- Category: depth
- Pass condition: The pre-YAML inventory is presented as a typed table with at least two named
  columns -- minimally a signal identifier column and a relevance or category column. A bulleted
  list alone does not pass. Requires C-09 to pass -- a typed table appearing after the YAML does
  not satisfy this criterion.

**C-12 -- Pivot rationale cites specific named signal**
- Weight: aspirational
- Category: format
- Pass condition: The rationale for pivot mode selection names at least one specific signal from
  the inventory by path or identifier. A generic justification without naming a specific
  inventory signal does not pass.

**C-13 -- Hard ordering gate between inventory and YAML**
- Weight: aspirational
- Category: behavior
- Pass condition: A structural ordering mechanism prevents YAML generation before the inventory
  is complete. Advisory sequencing ("first do X, then do Y") without an explicit enforcement
  mechanism does not pass.

**C-14 -- Gate row embedded as terminal row of the inventory table**
- Weight: aspirational
- Category: behavior
- Pass condition: The hard ordering gate (C-13) is expressed as the terminal row of the typed
  inventory table (C-11), not as a separate sentinel line or prose block. The gate row must be
  structurally inside the table and must appear immediately before the YAML block. A gate row
  added to any table other than the inventory table does not satisfy this criterion. Requires
  C-11 and C-13 to both pass.

**C-15 -- Phase incompleteness predicate stated per phase**
- Weight: aspirational
- Category: behavior
- Pass condition: Each phase or step that produces a structural artifact includes an explicit
  incompleteness predicate -- "Phase N is not complete until X" or equivalent. A step
  description does not pass. At least the inventory phase and the YAML authoring phase must each
  have a stated predicate.

**C-16 -- Traceability failure triggers explicit repair instruction**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt specifies what to do when a team area cannot be traced to an
  inventory signal -- either a stop instruction or a repair instruction. An implicit constraint
  without a stated failure action does not pass.

**C-17 -- Phase completion tests produced as visible model output**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt directs the model to produce a named Completion Test block as
  visible output before advancing from one phase to the next. A predicate in the prompt with no
  corresponding output directive does not pass. At least the inventory phase and the YAML
  authoring phase must have directed completion test output.

**C-18 -- Constraints expressed as INVARIANT / VIOLATION / REPAIR triples**
- Weight: aspirational
- Category: behavior
- Pass condition: Each structural constraint in the prompt is specified in three named blocks:
  (1) INVARIANT -- the condition that must hold; (2) VIOLATION -- a concrete example of the
  wrong output, naming the anti-pattern by example; (3) REPAIR -- the specific steps to take
  when the violation is detected. An INVARIANT + REPAIR block without a VIOLATION block does not
  pass. At least the traceability constraint and the pivot rationale constraint must use all three
  blocks.

**C-19 -- Dual gate architecture: inventory gate and traceability gate structurally independent**
- Weight: aspirational
- Category: behavior
- Pass condition: Two named, structurally independent gates are present: (1) a structural
  ordering gate preventing YAML authoring before the inventory table is complete; and (2) a
  semantic traceability gate preventing phase completion if any team area lacks a traceable
  inventory signal. A single block checking both conditions does not pass. Requires C-13 and
  C-16 to both pass.

**C-20 -- Amend phase names an explicit anti-pattern for non-actionable offers**
- Weight: aspirational
- Category: behavior
- Pass condition: The amend phase directive explicitly names what does NOT satisfy it -- e.g.,
  "A response that says 'Let me know if you want changes' does not satisfy this phase." The
  anti-pattern call-out must appear inside the amend phase directive, not in a separate glossary.
  Requires C-08 to pass.

**C-21 -- Each gate labeled with a category name identifying its enforcement type**
- Weight: aspirational
- Category: behavior
- Pass condition: Each of the two independent gates (C-19) carries a category label in
  parentheses -- e.g., "GATE 1 (Structural Ordering)" and "GATE 2 (Semantic Traceability)".
  Gates named by number only without parenthesized category labels do not pass. Requires C-19
  to pass.

**C-22 -- Every structural constraint in every phase expressed as a separate IVR triple**
- Weight: aspirational
- Category: behavior
- Pass condition: The INVARIANT/VIOLATION/REPAIR discipline (C-18) is applied to every structural
  constraint in every phase -- role population, group hierarchy, amend completeness, scope
  exclusion, and any format constraint that has a named failure mode. A prompt that applies IVR
  to only the two required constraints while leaving other structural constraints as prose
  directives does not pass. Requires C-18 to pass.

**C-23 -- Inline detected-from: traceability field embedded in YAML team entries**
- Weight: aspirational
- Category: depth
- Pass condition: Each team entry in the generated org.yaml carries a detected-from: annotation
  field (or semantically equivalent: source:, signal:, origin:) naming the specific inventory
  signal that justified that team. Team entries without a detected-from: field do not pass even
  if the pre-YAML inventory is complete. Requires C-02 and C-09 to both pass.

**C-24 -- Pivot mode candidates enumerated before selection**
- Weight: aspirational
- Category: format
- Pass condition: The pivot phase enumerates all candidate pivot modes considered before declaring
  the selected mode, naming each non-selected mode and stating why it was rejected. Declaring
  only the selected mode -- even with a strong signal-cited rationale -- does not pass. Requires
  C-06 and C-12 to both pass.

**C-25 -- Each IVR triple carries a phase-scoped structural label**
- Weight: aspirational
- Category: behavior
- Pass condition: Every IVR triple in the prompt carries a structured label that scopes it to
  its phase and enumerates it within that phase. Acceptable label conventions: hierarchical
  identifiers (IVR-1A, IVR-2B), SPEC-object numbering, numbered requirements, or equivalent.
  IVR triples present but unnamed do not pass. Requires C-22 to pass.

**C-26 -- Formal constraint system contains explicit meta-rule declaring informal constraints non-binding**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt includes an explicit meta-rule stating that any constraint outside
  the formal system is non-binding or advisory only. A prompt that uses a formal system without
  this meta-rule leaves the constraint set open. The meta-rule must appear in the prompt body,
  not only in a header comment. Requires C-22 and C-25 to both pass.

**C-27 -- Completion test includes explicit conditional advance instruction**
- Weight: aspirational
- Category: behavior
- Pass condition: Each phase completion test block (C-17) includes a conditional advance
  instruction that names what to do with the test result -- e.g., "Advance to Phase 3: only if
  Phase 2 Completion Test is all YES. If any item is NO: resolve the failing item before
  continuing." A completion test block without a conditional advance instruction does not pass.
  Requires C-17 to pass.

**C-28 -- META-RULE enumerates all IVR triples by label with a count instruction**
- Weight: aspirational
- Category: behavior
- Pass condition: The meta-rule block (C-26) functions as an exhaustive labeled manifest of the
  constraint set: it lists every IVR triple by its structural label and states the total count
  of triples. A meta-rule that declares informal constraints non-binding but does not enumerate
  the formal labels or state a count does not pass. Requires C-25 and C-26 to both pass.

**C-29 -- Explicit ENTRY contracts at phase start pairing with EXIT contracts**
- Weight: aspirational
- Category: behavior
- Pass condition: Each phase opens with a formal ENTRY contract block that declares the
  preconditions that must already hold before that phase begins. The ENTRY block must be a named
  structural element appearing at the start of the phase, not a prose advisory. A prompt with
  EXIT conditions but no corresponding ENTRY declarations at phase start does not pass. Requires
  C-27 to pass.

**C-30 -- Completion infrastructure covers every phase without exception**
- Weight: aspirational
- Category: behavior
- Pass condition: The full completion suite -- incompleteness predicate (C-15), directed visible
  test block (C-17), and conditional advance instruction (C-27) -- is present for every phase in
  the prompt. A prompt that applies the full suite to two phases while leaving a third phase with
  only a prose description does not pass. Requires C-15, C-17, and C-27 to all pass.

**C-31 -- Multi-surface verification: completion infrastructure anchored on three independent surfaces**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt provides three structurally independent surfaces from which a
  reviewer can verify C-28/C-29/C-30 compliance: (1) the constraint manifest; (2) a front-matter
  phase-contract summary covering all phases; and (3) canonical predicate phrasing at the opening
  of each phase body. Each surface must be independently sufficient to confirm compliance. A
  prompt satisfying C-28/C-29/C-30 via only one or two surfaces does not pass. Requires C-28,
  C-29, and C-30 to all pass.

**C-32 -- Phase-contract table placed as front-matter before any phase body**
- Weight: aspirational
- Category: behavior
- Pass condition: The complete phase contract architecture for every phase -- ENTRY preconditions,
  incompleteness predicate, completion test directive, and conditional advance instruction -- is
  collected into a single summary table appearing in the prompt before any phase body begins.
  The table must have one row per phase and cover all phases without exception. A prompt that
  places ENTRY/exit contracts only within individual phase body sections, with no front-matter
  contract table, does not pass even if C-29 and C-30 are otherwise satisfied. Requires C-29
  and C-30 to both pass.

**C-33 -- Incompleteness predicate is the first structural element of each phase body**
- Weight: aspirational
- Category: behavior
- Pass condition: The "Phase N is not complete until X" predicate (C-15) appears as the FIRST
  line of each phase body -- before the ENTRY block, before any IVR triples, before any prose
  description of phase content. This ordering makes C-15/C-30 compliance checkable by scanning
  only the opening line of each phase section. A prompt where the incompleteness predicate
  appears after ENTRY declarations, after IVR triples, or only in a summary table does not pass.
  The criterion requires correct ordering, not merely predicate presence. Requires C-15 and C-30
  to both pass.

**C-34 -- Constraint manifest uses terminal count row matching the gate-row sentinel pattern**
- Weight: aspirational
- Category: behavior
- Pass condition: The constraint manifest (C-28) applies the same structural device as the
  inventory gate row (C-14): a terminal sentinel row whose stated value must match a mechanical
  count -- e.g., "| TOTAL | 14 labeled triples -- count to verify completeness |". A manifest
  that lists labels and states a count in prose (not a structured terminal row) does not pass.
  A TOTAL row in any table other than the constraint manifest does not satisfy this criterion.
  Requires C-14 and C-28 to both pass.

**C-35 -- Incompleteness predicate expressed as blockquote enabling rendered-markdown scan surface**
- Weight: aspirational
- Category: behavior
- Pass condition: The "Phase N is not complete until X" predicate (C-33) is expressed using
  rendered-markdown blockquote syntax (> prefix), making it visually and syntactically distinct
  from surrounding prose, ENTRY blocks, and IVR triple text. The blockquote format creates a
  fourth independent audit surface beyond the three required by C-31: a reviewer scanning
  rendered markdown locates all incompleteness predicates by visual inspection of blockquote
  elements alone, without reading ENTRY blocks, IVR triples, or the phase-contract table. C-33
  requires correct ordering and can pass with bold-caps or plain prose; C-35 requires blockquote
  syntax specifically. A prompt where predicates satisfy C-33 ordering but use bold-caps or plain
  prose does not pass this criterion. The blockquote scan surface is orthogonal to the three
  C-31 surfaces -- it enables a rendered-view scan not available from the manifest, phase-contract
  table, or phase-body text scan. Evidence: V-01 "blockquote predicates as rendered-markdown scan
  surface -- C-33 verifiable by scanning rendered blockquotes only." Requires C-33 to pass.

**C-36 -- Constraint manifest carries VIOLATION column making it a mini-IVR anti-pattern reference**
- Weight: aspirational
- Category: behavior
- Pass condition: The constraint manifest (C-28) includes a dedicated VIOLATION column alongside
  each IVR triple label, naming the concrete anti-pattern for that constraint. This converts the
  manifest from a bare label-and-count list into a mini-IVR reference table: a reviewer can
  confirm both what is required and what the specific failure looks like from the manifest alone,
  without navigating to the phase body containing that triple. Anti-patterns for all labeled
  constraints become scannable from the manifest, creating an independent failure-detection
  surface that requires no phase-body traversal. A manifest that lists labels, counts, and a
  TOTAL row but omits the VIOLATION column does not pass. A VIOLATION column present in any
  other table does not satisfy this criterion -- the column must be in the constraint manifest
  itself. Evidence: V-02 "VIOLATION column makes manifest a mini-IVR anti-pattern reference;
  anti-patterns scannable from manifest without reading phase bodies." Requires C-28 and C-34
  to both pass.

**C-37 -- Phase-contract table carries test-item-count column enabling mechanical cross-check**
- Weight: aspirational
- Category: behavior
- Pass condition: The phase-contract front-matter table (C-32) includes a dedicated column
  stating the number of YES/NO checklist items that each phase's completion test block contains.
  The count declared in each row must equal the actual number of items present in the
  corresponding directed completion test block in the phase body. This creates a mechanical
  cross-check: a reviewer can verify that no test block has been truncated or extended by
  comparing the table count to the actual item count, without reading full phase body prose. A
  phase-contract table that includes ENTRY preconditions, incompleteness predicate, test
  directive, and conditional advance columns but omits the test-item-count column does not pass
  even if all other phase contract elements are present. A count column in any table other than
  the phase-contract front-matter table does not satisfy this criterion. Evidence: V-03 "count
  column in contract table creates cross-check: table count must equal YES/NO items in test
  block; mechanical discrepancy detection." Requires C-32 to pass.

**C-38 -- Cross-manifest count invariant: CONSTRAINT MANIFEST TOTAL equals sum of phase test-item counts**
- Weight: aspirational
- Category: behavior
- Pass condition: The CONSTRAINT MANIFEST TOTAL row (C-34, declaring the count of labeled IVR
  triples) and the sum of the per-phase test-item-count column values in the PHASE CONTRACT TABLE
  (C-37) declare the same count from two structurally independent front-matter perspectives. In
  a well-formed prompt the two values must be equal: N labeled IVR triples equals N total
  completion test items across all phases. A discrepancy between the manifest TOTAL and the sum
  of phase test-item counts is mechanically detectable by arithmetic on the two front-matter
  tables without reading any phase body. Having two independent front-matter tables anchoring the
  same count creates the strongest available cross-manifest invariant: a single table corruption
  cannot satisfy both tables simultaneously. A prompt where the manifest TOTAL and the
  phase-contract item-count sum agree but only because the count column is absent in the
  phase-contract table does not pass -- both C-34 and C-37 must be independently satisfied. A
  prompt where the two counts disagree does not pass even if each table is internally consistent.
  Evidence: V-05 "Cross-manifest count invariant -- CONSTRAINT MANIFEST TOTAL (14) equals sum
  of all phase test-item counts in PHASE CONTRACT TABLE (P1=2, P2=5, P3=6, P4=1, total=14);
  discrepancy between the two front-matter values mechanically detectable without reading any
  phase body." Requires C-34 and C-37 to both pass.

---

## Score Reference

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (5 criteria) | 50 pts |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts |
| Aspirational | C-09 through C-38 (30 criteria) | 300 pts |
| **Total** | | **380 pts** |

**Scoring per criterion**: PASS = 10 pts, PARTIAL = 5 pts, FAIL = 0 pts.

**Golden**: all 5 essentials pass AND composite >= 80 pts.

| Score | Breakdown | Result |
|-------|-----------|--------|
| 380 / 380 | 5E + 3R + 30A all PASS | Perfect |
| 130 / 380 | 5E + 3R + 5A PASS | Golden |
| 80 / 380 | 5E + 3R + 0A PASS | Golden (threshold) |
| 70 / 380 | 5E + 2R + 0A PASS | Below threshold -- not golden |
| any | 4E or fewer PASS | Disqualified (essential failure) |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-17 | Added C-11 (typed inventory table), C-12 (rationale cites specific named signal), C-13 (hard ordering gate) from R1 excellence signals. Max score now 130 pts. |
| v3 | 2026-03-17 | Added C-14 (gate row embedded in inventory table, V-04), C-15 (phase incompleteness predicate, V-03), C-16 (traceability failure repair instruction, V-04/V-01) from R2 excellence signals. Updated C-10 PARTIAL case. Max score now 160 pts. |
| v4 | 2026-03-17 | Added C-17 (completion tests as visible model output, V-02), C-18 (INVARIANT/VIOLATION/REPAIR triples, V-03), C-19 (dual gate architecture, V-04) from R3 excellence signals. Max score now 190 pts. |
| v5 | 2026-03-17 | Added C-20 (amend phase names explicit anti-pattern, V-01/V-02), C-21 (gates labeled with category names, V-01/V-02), C-22 (all structural constraints in all phases covered by separate IVR triples, V-01/V-02) from R4 excellence signals. Max score now 220 pts. |
| v6 | 2026-03-17 | Added C-23 (inline detected-from: traceability field in YAML, V-01), C-24 (pivot candidates enumerated before selection, V-01), C-25 (phase-scoped labels on each IVR triple, V-01/V-02/V-03), C-26 (meta-rule declaring informal constraints non-binding, V-02), C-27 (completion test conditional advance instruction, V-03) from R5 excellence signals. Max score now 270 pts. |
| v7 | 2026-03-17 | Added C-28 (META-RULE enumerates all IVR triples by label with count instruction, V-01/V-02), C-29 (explicit ENTRY contracts pairing with EXIT contracts, V-02), C-30 (completion infrastructure covers every phase without exception, V-02) from R6 excellence signals. Max score now 300 pts. |
| v8 | 2026-03-17 | Added C-31 (multi-surface verification -- three independent audit surfaces for C-28/C-29/C-30, V-05), C-32 (phase-contract table as front-matter before phase bodies, V-01/V-04/V-05), C-33 (incompleteness predicate as first structural element of each phase body, V-03/V-05), C-34 (constraint manifest terminal count row mirrors gate-row sentinel pattern, V-02/V-04/V-05) from R7 excellence signals. Max score now 340 pts. |
| v9 | 2026-03-17 | Added C-35 (blockquote predicate as rendered-markdown scan surface, V-01), C-36 (VIOLATION column in manifest as mini-IVR anti-pattern reference, V-02), C-37 (test-item-count column in phase-contract table for mechanical cross-check, V-03), C-38 (cross-manifest count invariant -- manifest TOTAL equals sum of phase test-item counts, V-05) from R8 excellence signals. Max score now 380 pts. |

---

The four new criteria and their dependency chains:

```
C-35 requires C-33
C-36 requires C-28 + C-34
C-37 requires C-32
C-38 requires C-34 + C-37  (and transitively C-28 + C-32)
```

Note: `corps-scan-rubric-v9-2026-03-17.md` was not written to disk -- Bash was declined. To write the file, run: `python -c "open('simulations/quest/rubrics/corps-scan-rubric-v9-2026-03-17.md','w').write(content)"` with the content above, or approve a Bash/Write tool call.
