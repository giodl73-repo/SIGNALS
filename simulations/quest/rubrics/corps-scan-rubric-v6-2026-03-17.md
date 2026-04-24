Written to `simulations/quest/rubrics/corps-scan-rubric-v6-2026-03-17.md` (491 lines).

---

**Five new criteria extracted from R5:**

**C-23 -- Inline `detected-from:` traceability field embedded in YAML team entries** (V-01)
V-01 C-02 evidence: `` `detected-from:` field traces every team to ROLE 2 inventory ``. C-09 requires a pre-YAML inventory; C-16 requires a repair path when traceability fails; C-23 additionally requires the YAML output itself to carry inline traceability — each team entry includes a `detected-from:` annotation naming the specific inventory signal that justified it. The YAML becomes self-documenting. Requires C-02 and C-09.

**C-24 -- Pivot mode candidates enumerated before selection** (V-01)
V-01 C-06 evidence: `"ROLE 2: pivot mode candidates + selected pivot with Signal citation"`. C-06 requires rationale for the selected mode; C-24 additionally requires all rejected modes to be named with rejection reasons before the selection is declared. Requires C-06 and C-12.

**C-25 -- Each IVR triple carries a phase-scoped structural label** (V-01, V-02, V-03)
V-01: `"13 labeled IVR triples"` (IVR-1A/2B/3E). V-02: `"12 SPECs"` (SPEC-01/SPEC-12). V-03: `"11 REQ blocks"` (REQ-1.1/REQ-4.1). C-22 requires all constraints to use IVR; C-25 additionally requires each triple to carry a label that scopes it to its phase and enumerates it — enabling cross-reference, counting for completeness, and audit by label. Requires C-22.

**C-26 -- Formal constraint system contains explicit meta-rule declaring informal constraints non-binding** (V-02)
V-02 C-22 evidence: `"A constraint not expressed as a SPEC is not a constraint"`. Closes the constraint set: prevents prose advisory language from accumulating alongside formal constraints. Requires C-22 and C-25.

**C-27 -- Completion test includes explicit conditional advance instruction** (V-03)
V-03 C-15 evidence: `"Proceed to GATE 1: only if all YES"`. C-17 requires the completion test to be produced as visible output; C-27 additionally requires a conditional advance instruction — the model is told what to do with the result, converting the test from reporting artifact to phase-gate enforcement mechanism. Requires C-17.

---

**Score change:** 22 criteria → 27 criteria, 220 pts max → **270 pts max**. Golden threshold unchanged.
er constraints ("see IVR-2A"); (b) counting to verify
completeness ("13 labeled triples, none missing"); (c) audit by label without reading full
logic. IVR triples present but unnamed (i.e., not individually labeled) do not pass. Requires
C-22.

**C-26 -- Formal constraint system contains explicit meta-rule declaring informal constraints
non-binding** (V-02)
V-02 C-22 evidence: "A constraint not expressed as a SPEC is not a constraint". When a prompt
uses a formal constraint system (IVR/SPEC/REQ), it must include a meta-rule that explicitly
states any constraint outside that system is non-binding -- e.g., "Any requirement not expressed
as a SPEC object is advisory only." This closes the constraint set: it prevents prose advisory
language from accumulating alongside formal constraints and enables a reviewer to enumerate the
full constraint set by counting labeled triples. A prompt that uses IVR/SPEC/REQ without this
meta-rule leaves the constraint set open -- additional prose directives have ambiguous normative
status. Requires C-22 and C-25.

**C-27 -- Completion test includes explicit conditional advance instruction** (V-03)
V-03 C-15 evidence: "Proceed to GATE 1: only if all YES". C-17 requires the prompt to direct
the model to produce a named completion test block as visible output; C-27 additionally requires
that block to include a conditional advance instruction naming what to do with the test result --
e.g., "Proceed to GATE 1: only if all YES" or "Advance to Phase 3: only if Phase 2 Completion
Test is all YES. If any NO: return to Phase 2 and resolve before continuing." A completion test
block that lists YES/NO checklist items without a conditional advance instruction does not pass:
the model knows how to produce the test but not how to act on the result. The conditional
instruction converts the test from a reporting artifact into a phase-gate enforcement mechanism.
Requires C-17.

---

**Score change:** 22 criteria --> 27 criteria, 220 pts max --> **270 pts max**. Golden threshold
(>= 80 pts, all 5 essentials) unchanged.

---

## What carried forward from v5

**C-20 -- Amend phase names an explicit anti-pattern for non-actionable offers**
V-01/V-02 (R4). The amend phase directive explicitly names what does NOT satisfy it --
"Let me know if you want changes" does not satisfy this phase. C-08 requires actionable amend
options; C-20 additionally requires the anti-pattern named by example inside the amend
directive. Requires C-08.

**C-21 -- Each gate labeled with a category name identifying its enforcement type**
V-01/V-02 (R4). Each of the two independent gates carries a parenthesized category label --
GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability). The label makes the gate
failure mode self-describing. Requires C-19.

**C-22 -- Every structural constraint in every phase expressed as a separate IVR triple**
V-01/V-02 (R4). The INVARIANT/VIOLATION/REPAIR discipline is applied to every structural
constraint in every phase -- role population, group hierarchy, amend completeness, scope
exclusion, and any format constraint with a named failure mode. C-18 required at minimum two
constraints to use IVR; C-22 requires the same discipline for all. Requires C-18.

---

## What carried forward from v4

**C-17 -- Phase completion tests produced as visible model output**
V-02 (R3). The prompt directs the model to produce a YES/NO Completion Test block as visible
output before advancing phases. Distinct from C-15: C-15 makes the boundary auditable to a
reader of the prompt; C-17 makes it auditable to a reader of the model response.

**C-18 -- Constraints expressed as INVARIANT / VIOLATION / REPAIR triples**
V-03 (R3). Every structural constraint has three named blocks: what must hold, a concrete
anti-pattern example, and the repair steps. C-16 required a repair instruction; C-18
additionally requires the VIOLATION block naming the anti-pattern by example.

**C-19 -- Dual gate architecture: inventory gate and traceability gate structurally independent**
V-04 (R3). Two named, structurally independent gates: a structural ordering gate (C-13/C-14
family) and a semantic traceability gate (C-16 family). A single block checking both conditions
does not pass. Requires C-13 and C-16.

---

## Score table

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 -- C-05 | 50 pts |
| Recommended | C-06 -- C-08 | 30 pts |
| Aspirational | C-09 -- C-27 | 190 pts |
| **Total** | 27 criteria | **270 pts** |

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
  organizes teams beneath it (e.g., divisions, tribes, pillars). An org.yaml that lists teams
  at the top level without grouping them fails -- group structure is required for corps-build and
  corps-rob compatibility. A single group containing all teams passes; a flat team list with no
  group hierarchy does not.

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
  signals (e.g., "using directory mode: repo has clear top-level service directories under
  /src"). Declaring a mode without rationale does not pass -- the rationale is what makes the
  draft reviewable and the mode choice reversible. Note: C-12 further requires the rationale to
  cite a specific named signal; C-06 passes with any explanatory sentence.

**C-07 -- Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: `org.yaml` contains an `exec-office:` section with at least a name field, even
  if no teams are listed under it. Absence of exec office means the output cannot feed the
  corps-rob exec-office stage without manual addition, breaking the downstream pipeline contract.

**C-08 -- Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable -- e.g., "AMEND: switch to service mode -- run /corps-scan --pivot service".
  A generic "let me know if you want changes" does not pass; each option must name the change and
  the action to take.

---

## ASPIRATIONAL

Nineteen criteria. Each worth 10 pts (190 pts total if all pass).

C-09 and C-10 carry forward from v1. C-11, C-12, C-13 added in v2. C-14, C-15, C-16 added in
v3. C-17, C-18, C-19 added in v4. C-20, C-21, C-22 added in v5. C-23, C-24, C-25, C-26, C-27
new in v6.

---

**C-09 -- Pre-YAML scan inventory listed**
- Weight: aspirational
- Category: depth
- Pass condition: Before the YAML block, the output lists the repo signals it detected as a
  readable inventory of directory names, service paths, module identifiers, or domain terms. The
  inventory must be structurally distinct from the YAML (not the YAML itself) and must appear
  before the YAML block begins. This makes C-02 grounding independently verifiable without
  re-reading the repo. Outputs with only inline YAML comments but no pre-YAML inventory do not
  pass.

**C-10 -- Draft boundary stated before first structural content**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only framing -- that this output is a proposal for human review, not
  a build instruction -- is stated explicitly before any YAML or structural content appears. A
  single sentence such as "This is a draft org.yaml for review -- no role files will be created"
  appearing as the first substantive line passes. Burying the boundary acknowledgment after the
  YAML, or only at the very end, does not pass. PARTIAL case: a scope constraint block present
  at the top of the prompt but with no explicit instruction directing the model to output the
  boundary statement as its first visible line earns PARTIAL -- the constraint must direct model
  output, not merely inform model context.

**C-11 -- Inventory formatted as typed table**
- Weight: aspirational
- Category: depth
- Pass condition: The pre-YAML inventory is presented as a typed table with at least two named
  columns -- minimally a signal identifier column (path, name, or module) and a relevance or
  category column (e.g., Pivot Relevance, Signal Type, Domain). A bulleted list alone does not
  pass. Typed columns make each signal basis independently verifiable without re-reading the
  repo and enable the pivot rationale (C-06, C-12) to cite a specific table row rather than a
  free-form claim. Requires C-09 to pass -- a typed table that appears after the YAML does not
  satisfy this criterion.

**C-12 -- Pivot rationale cites specific named signal**
- Weight: aspirational
- Category: format
- Pass condition: The rationale for pivot mode selection names at least one specific signal from
  the inventory by path or identifier (e.g., "/src/api/, /src/auth/, /src/billing/ -- three
  parallel service directories -> directory mode"). A generic justification ("this repo appears
  service-oriented" or "the repo structure suggests services") without naming a specific
  inventory signal does not pass. A named anchor makes the pivot choice independently auditable:
  a reviewer can verify the cited signal without re-reading the full scan. This criterion
  strengthens C-06 -- C-06 can pass with any explanatory sentence; C-12 requires that sentence
  to contain a named signal from the inventory.

**C-13 -- Hard ordering gate between inventory and YAML**
- Weight: aspirational
- Category: behavior
- Pass condition: A structural ordering mechanism prevents YAML generation before the inventory
  is complete -- e.g., a sentinel line (--- [SCAN COMPLETE] ---), an explicit "DO NOT begin
  YAML until inventory is written" instruction, or an equivalent phase gate that must be
  satisfied before YAML authoring begins. Advisory sequencing ("first do X, then do Y") without
  an explicit enforcement mechanism does not pass. The gate is what converts the pre-YAML
  inventory from advisory to unconditional, protecting C-09 across conversational phrasing
  registers.

**C-14 -- Gate row embedded as terminal row of the inventory table**
- Weight: aspirational
- Category: behavior
- Pass condition: The hard ordering gate (C-13) is expressed as the terminal row of the typed
  inventory table (C-11), not as a separate sentinel line or prose block. The gate row must be
  structurally inside the table -- e.g., "| GATE | INVENTORY COMPLETE | [n] signals | YAML
  authoring authorized |" as the last table row -- and must appear immediately before the YAML
  block. When the gate is a table row, the inventory cannot be considered complete without the
  gate row, and the gate row cannot appear without the inventory rows above it. A gate row added
  to any table other than the inventory table does not satisfy this criterion -- the gate must be
  the terminal row of the typed signal inventory. Requires C-11 and C-13 to both pass.

**C-15 -- Phase incompleteness predicate stated per phase**
- Weight: aspirational
- Category: behavior
- Pass condition: Each phase or step that produces a structural artifact includes an explicit
  incompleteness predicate -- a condition that must be true before the phase is considered
  complete, stated as "Phase N is not complete until X" or equivalent. A step description
  ("collect signals and list them") does not pass. A completion predicate ("Phase 1 is not
  complete until the typed table contains at least one row") passes. The predicate makes the
  phase boundary auditable without re-reading prose instructions. A single incompleteness
  predicate covering only the final phase does not pass -- at least the inventory phase and the
  YAML authoring phase must each have a stated predicate.

**C-16 -- Traceability failure triggers explicit repair instruction**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt specifies what to do when a team area cannot be traced to an
  inventory signal -- either a stop instruction ("you are inventing names -- stop") or a repair
  instruction ("return to Phase 1 and add the missing signal before continuing"). C-02 requires
  grounded team areas; C-16 requires that the failure action is named. An implicit constraint
  ("team areas must trace to signals") without a stated failure action does not pass. Either form
  passes: stop instructions and repair loops both make the failure action explicit. The repair
  instruction is the stronger form -- it prevents silent failures by routing the model back to
  the inventory rather than halting -- but both satisfy the criterion.

**C-17 -- Phase completion tests produced as visible model output**
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt directs the model to produce a named Completion Test block as
  visible output before advancing from one phase to the next. The Completion Test is a formatted
  block with YES/NO checklist items -- e.g., "Phase 1 Completion Test: Typed inventory table
  exists: YES / NO. Gate row present as final table row: YES / NO." -- that the model generates
  as part of its response, not a predicate stated only in the prompt. C-15 requires the
  incompleteness predicate to appear in the prompt; C-17 requires the model to produce the
  completion test as a visible output artifact. A predicate in the prompt with no corresponding
  output directive does not pass. The distinction: C-15 makes the boundary auditable to a human
  reading the prompt; C-17 makes the boundary auditable to a human reading the model response.
  At least the inventory phase and the YAML authoring phase must have directed completion test
  output.

**C-18 -- Constraints expressed as INVARIANT / VIOLATION / REPAIR triples**
- Weight: aspirational
- Category: behavior
- Pass condition: Each structural constraint in the prompt is specified in three named blocks:
  (1) INVARIANT -- the condition that must hold; (2) VIOLATION -- a concrete example of the
  wrong output, naming the anti-pattern by example (e.g., "Pivot mode references repo shape
  without naming a Signal ID"); (3) REPAIR -- the specific steps to take when the violation is
  detected. C-16 requires a repair instruction; C-18 additionally requires the VIOLATION
  anti-pattern to be named as a concrete example. An INVARIANT + REPAIR block without a
  VIOLATION block does not pass. The VIOLATION example is what converts an abstract constraint
  into an unambiguous specification -- a reviewer can confirm a failure without interpreting the
  pass condition. At least the traceability constraint and the pivot rationale constraint must
  use all three blocks.

**C-19 -- Dual gate architecture: inventory gate and traceability gate structurally independent**
- Weight: aspirational
- Category: behavior
- Pass condition: Two named, structurally independent gates are present: (1) a structural
  ordering gate preventing YAML authoring before the inventory table is complete and the gate row
  is present (the C-13/C-14 gate); and (2) a semantic traceability gate preventing phase
  completion if any team area lacks a traceable inventory signal, with a named repair path back
  to the inventory (extending C-16). The two gates must be independent enforcement points -- a
  single block that checks both conditions in one step does not pass. Each gate must have its
  own named failure condition and repair action. Requires C-13 and C-16 to both pass.

**C-20 -- Amend phase names an explicit anti-pattern for non-actionable offers**
- Weight: aspirational
- Category: behavior
- Pass condition: The amend phase directive explicitly names what does NOT satisfy it -- e.g.,
  "A response that says 'Let me know if you want changes' does not satisfy this phase." C-08
  requires actionable amend options; C-20 additionally requires the anti-pattern to be named by
  example, applying the VIOLATION discipline (C-18) to the amend phase boundary. The anti-pattern
  call-out must appear inside the amend phase directive, not in a separate glossary. A prompt
  that lists actionable options but leaves the non-actionable form unnamed does not pass.
  Requires C-08 to pass.

**C-21 -- Each gate labeled with a category name identifying its enforcement type**
- Weight: aspirational
- Category: behavior
- Pass condition: Each of the two independent gates (C-19) carries a category label in
  parentheses that names the class of error the gate enforces -- e.g., "GATE 1 (Structural
  Ordering)" and "GATE 2 (Semantic Traceability)". The category label makes the gate failure
  mode self-describing: a reader of the prompt knows what the gate enforces without reading its
  logic. Gates named by number only ("GATE 1", "GATE 2") without parenthesized category labels
  do not pass. The label must appear adjacent to the gate header, not only in a separate
  description block. Requires C-19 to pass.

**C-22 -- Every structural constraint in every phase expressed as a separate IVR triple**
- Weight: aspirational
- Category: behavior
- Pass condition: The INVARIANT/VIOLATION/REPAIR discipline (C-18) is applied systematically:
  every structural constraint in every phase has its own dedicated, separately-labeled IVR
  triple. C-18 requires at minimum the traceability constraint and the pivot rationale constraint
  to use full IVR; C-22 requires the same discipline for all structural constraints across all
  phases -- role population, group hierarchy, amend completeness, scope exclusion, and any
  format constraint that has a named failure mode. A prompt that applies IVR to only the two
  required constraints while leaving other structural constraints as prose directives does not
  pass. Evidence: V-01 "four separate IVR triples in Phase 3"; V-02 "All SPECs use full IVR
  across all phases." Requires C-18 to pass.

**C-23 -- Inline detected-from: traceability field embedded in YAML team entries**
- Weight: aspirational
- Category: depth
- Pass condition: Each team entry in the generated org.yaml carries a detected-from: annotation
  field (or semantically equivalent: source:, signal:, origin:) naming the specific inventory
  signal that justified that team -- e.g., "detected-from: /src/billing/" or
  "detected-from: Signal: billing-service (directory)". The annotation makes the YAML
  self-documenting: a reviewer can verify C-02 grounding by reading the YAML alone, without
  consulting the pre-YAML inventory. C-09 requires a separate pre-YAML inventory; C-23 requires
  the traceability to also appear inline within the YAML artifact itself. Team entries without a
  detected-from: (or equivalent) field do not pass even if the pre-YAML inventory is complete.
  Requires C-02 and C-09 to both pass.

**C-24 -- Pivot mode candidates enumerated before selection**
- Weight: aspirational
- Category: format
- Pass condition: The pivot phase enumerates all candidate pivot modes considered before declaring
  the selected mode, not only the selected mode with its rationale. The candidate list must name
  each non-selected mode and state why it was rejected -- e.g., "directory (selected: 3 parallel
  top-level service dirs); concept (rejected: no abstraction layer present); service (rejected:
  dirs already named by service)". C-06 requires a rationale for the selected mode and C-12
  requires it to cite a specific signal; C-24 additionally requires the rejected alternatives to
  be named. Declaring only the selected mode -- even with a strong signal-cited rationale -- does
  not pass. The candidate enumeration makes the selection auditable against alternatives without
  re-reading the repo. Requires C-06 and C-12 to both pass.

**C-25 -- Each IVR triple carries a phase-scoped structural label**
- Weight: aspirational
- Category: behavior
- Pass condition: Every IVR triple in the prompt carries a structured label that scopes it to
  its phase and enumerates it within that phase. Acceptable label conventions: hierarchical
  identifiers (IVR-1A, IVR-2B, IVR-3E), SPEC-object numbering (SPEC-01, SPEC-07, SPEC-12),
  numbered requirements (REQ-1.1, REQ-3.4), or equivalent. The label must appear adjacent to the
  triple header. The label enables: (a) cross-reference from other constraints ("see IVR-2A");
  (b) counting to verify completeness ("13 labeled triples -- none missing"); (c) audit by label
  without reading full logic. IVR triples present but unnamed (i.e., carrying no individual
  label beyond their phase section header) do not pass. Requires C-22 to pass.

**C-26 -- Formal constraint system contains explicit meta-rule declaring informal constraints
non-binding**
- Weight: aspirational
- Category: behavior
- Pass condition: When a prompt uses a formal constraint system (IVR/SPEC/REQ or equivalent),
  the prompt must include an explicit meta-rule stating that any constraint outside that system
  is non-binding or advisory only -- e.g., "A constraint not expressed as a SPEC is not a
  constraint" or "Any directive not assigned an IVR label is advisory and does not constitute a
  pass/fail requirement." This meta-rule closes the constraint set: it prevents prose advisory
  language from accumulating alongside formal constraints and enables a reviewer to enumerate the
  full constraint set by counting labeled triples. A prompt that uses a formal system without
  this meta-rule leaves the constraint set open -- additional prose directives have ambiguous
  normative status. The meta-rule must appear in the prompt body, not only in a header comment.
  Requires C-22 and C-25 to both pass.

**C-27 -- Completion test includes explicit conditional advance instruction**
- Weight: aspirational
- Category: behavior
- Pass condition: Each phase completion test block (C-17) includes a conditional advance
  instruction that names what to do with the test result -- e.g., "Proceed to GATE 1: only if
  all YES" or "Advance to Phase 3: only if Phase 2 Completion Test is all YES. If any item is
  NO: resolve the failing item before continuing." A completion test block that lists YES/NO
  checklist items without a conditional advance instruction does not pass: the model knows how
  to produce the test but not how to act on the result. The conditional instruction converts the
  completion test from a reporting artifact into a phase-gate enforcement mechanism: a YES result
  unlocks the next phase; a NO result triggers a named resolution path. Requires C-17 to pass.

---

## Score Reference

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (5 criteria) | 50 pts |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts |
| Aspirational | C-09 through C-27 (19 criteria) | 190 pts |
| **Total** | | **270 pts** |

**Scoring per criterion**: PASS = 10 pts, PARTIAL = 5 pts, FAIL = 0 pts.

**Golden**: all 5 essentials pass AND composite >= 80 pts.

| Score | Breakdown | Result |
|-------|-----------|--------|
| 270 / 270 | 5E + 3R + 19A all PASS | Perfect |
| 130 / 270 | 5E + 3R + 5A PASS | Golden |
| 80 / 270 | 5E + 3R + 0A PASS | Golden (threshold) |
| 70 / 270 | 5E + 2R + 0A PASS | Below threshold -- not golden |
| any | 4E or fewer PASS | Disqualified (essential failure) |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-17 | Added C-11 (typed inventory table), C-12 (rationale cites specific named signal), C-13 (hard ordering gate) from R1 excellence signals. Corrected score table: aspirationals are 10 pts each, not 5 pts. Max score now 130 pts. |
| v3 | 2026-03-17 | Added C-14 (gate row embedded in inventory table, V-04), C-15 (phase incompleteness predicate, V-03), C-16 (traceability failure repair instruction, V-04/V-01) from R2 excellence signals. Updated C-10 pass condition with explicit PARTIAL case. Max score now 160 pts. |
| v4 | 2026-03-17 | Added C-17 (completion tests as visible model output, V-02), C-18 (INVARIANT/VIOLATION/REPAIR triples, V-03), C-19 (dual gate architecture, V-04) from R3 excellence signals. Max score now 190 pts. |
| v5 | 2026-03-17 | Added C-20 (amend phase names explicit anti-pattern, V-01/V-02), C-21 (gates labeled with category names, V-01/V-02), C-22 (all structural constraints in all phases covered by separate IVR triples, V-01/V-02) from R4 excellence signals. Max score now 220 pts. |
| v6 | 2026-03-17 | Added C-23 (inline detected-from: traceability field in YAML, V-01), C-24 (pivot candidates enumerated before selection, V-01), C-25 (phase-scoped labels on each IVR triple, V-01/V-02/V-03), C-26 (meta-rule declaring informal constraints non-binding, V-02), C-27 (completion test conditional advance instruction, V-03) from R5 excellence signals. Max score now 270 pts. |
