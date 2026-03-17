Written to `simulations/quest/rubrics/corps-scan-rubric-v4-2026-03-17.md`.

---

**Three new criteria extracted from R3:**

**C-17 -- Phase completion tests produced as visible model output** (from V-02)
The prompt directs the model to output a YES/NO Completion Test block before advancing phases. Distinct from C-15: C-15 makes the boundary auditable to a reader of the prompt; C-17 makes it auditable to a reader of the model's response. A predicate in the prompt with no output directive fails.

**C-18 -- Constraints expressed as INVARIANT / VIOLATION / REPAIR triples** (from V-03)
Every structural constraint has three named blocks: what must hold, a concrete anti-pattern example, and the repair steps. C-16 required a repair instruction; C-18 additionally requires the VIOLATION block naming the anti-pattern by example. An INVARIANT + REPAIR without VIOLATION fails -- the VIOLATION is what makes the constraint unambiguous.

**C-19 -- Dual gate architecture: inventory gate and traceability gate structurally independent** (from V-04)
Two independent gates: (1) structural ordering gate (C-13/C-14 inventory → YAML); (2) semantic traceability gate (no team area may lack a signal anchor, with its own repair path). A single block checking both conditions fails. Requires C-13 + C-16 to both pass.

**Score change:** 16 criteria → 19 criteria, 160 pts max → **190 pts max**. Golden threshold (≥ 80 pts, all 5 essentials) unchanged.
repo shape'
without naming a Signal ID" -- this makes the constraint unambiguous without re-reading the pass
condition. An INVARIANT + REPAIR block without a VIOLATION block does not pass. The VIOLATION is
what converts an abstract constraint into an unambiguous specification.

**C-19 -- Dual gate architecture: inventory gate and traceability gate structurally independent**
V-04 ("Output Format + Lifecycle: Dual Gate Architecture") added a second gate independent of the
C-13/C-14 inventory gate. The first gate is structural: YAML authoring cannot begin until the
inventory GATE row is present. The second gate is semantic: YAML completion cannot proceed if any
team area lacks a traceable inventory signal -- a separate enforcement point requiring repair
before the phase closes. C-13 requires one gate; C-19 requires two named, structurally
independent gates. V-04 satisfied this with two separate Completion Test blocks, each with its
own failure action. Requires C-13 and C-16 to both pass. A single gate that checks both
conditions in one block does not pass -- the two gates must be independent enforcement points.

---

## What carried forward from v3

**C-14 -- Gate row embedded as terminal row of the inventory table**
V-04 earned C-11 and C-13 simultaneously because the ordering gate was the last row of the typed
inventory table itself. C-13 requires a hard gate; C-14 requires the gate to be inside the
table. The two constraints become structurally inseparable -- the prompt cannot satisfy one
without the other.

**C-15 -- Phase incompleteness predicate stated per phase**
V-03 POSTCONDITION checklist pattern converted step descriptions into verifiable completion
conditions. "Phase 1 is not complete until the typed table exists" is a predicate, not an
instruction. C-15 gates each phase boundary with an explicit incompleteness condition.

**C-16 -- Traceability failure triggers explicit repair instruction**
V-04: "return to Part 1 and add the missing signal before continuing." C-02 passes or fails
silently; C-16 requires the failure action to be named. V-01 used a stop instruction; V-04 used
a repair instruction. Both forms pass -- the criterion is that a failure action exists.

**C-10 refinement (v3):** Scope constraint present at top of prompt but no instruction to output
the boundary statement earns PARTIAL.

---

**Score table:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 -- C-05 | 50 pts |
| Recommended | C-06 -- C-08 | 30 pts |
| Aspirational | C-09 -- C-19 | 110 pts |
| **Total** | 19 criteria | **190 pts** |

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

**C-05 -- Does not write .craft/roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present `.craft/roles/` file markdown. Any output that writes role files or presents role
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

Eleven criteria. Each worth 10 pts (110 pts total if all pass).

C-09 and C-10 carry forward from v1. C-11, C-12, C-13 added in v2. C-14, C-15, C-16 added in
v3. C-17, C-18, C-19 new in v4.

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
  output, not merely inform model context. Evidence: V-02 earned PARTIAL on this criterion for
  exactly this reason.

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
  structurally inside the table -- e.g., `| GATE | INVENTORY COMPLETE | [n] signals | YAML
  authoring authorized |` as the last table row -- and must appear immediately before the YAML
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
  the inventory rather than halting -- but both satisfy the criterion. Evidence: V-04 used repair
  ("return to Part 1"); V-01 used stop ("you are inventing names -- stop").

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
  reading the prompt; C-17 makes the boundary auditable to a human reading the model's response.
  At least the inventory phase and the YAML authoring phase must have directed completion test
  output.

**C-18 -- Constraints expressed as INVARIANT / VIOLATION / REPAIR triples**
- Weight: aspirational
- Category: behavior
- Pass condition: Each structural constraint in the prompt is specified in three named blocks:
  (1) INVARIANT -- the condition that must hold; (2) VIOLATION -- a concrete example of the
  wrong output, naming the anti-pattern by example (e.g., "Pivot mode references 'repo shape'
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
  own named failure condition and repair action. Requires C-13 and C-16 to both pass. Evidence:
  V-04's two separate Completion Test blocks, each with its own traceability failure action,
  satisfied this criterion; V-01 through V-03's single-gate designs did not.

---

## Score Reference

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (5 criteria) | 50 pts |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts |
| Aspirational | C-09 through C-19 (11 criteria) | 110 pts |
| **Total** | | **190 pts** |

**Scoring per criterion**: PASS = 10 pts, PARTIAL = 5 pts, FAIL = 0 pts.

**Golden**: all 5 essentials pass AND composite >= 80 pts.

| Score | Breakdown | Result |
|-------|-----------|--------|
| 190 / 190 | 5E + 3R + 11A all PASS | Perfect |
| 130 / 190 | 5E + 3R + 5A PASS | Golden |
| 80 / 190 | 5E + 3R + 0A PASS | Golden (threshold) |
| 70 / 190 | 5E + 2R + 0A PASS | Below threshold -- not golden |
| any | 4E or fewer PASS | Disqualified (essential failure) |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-17 | Added C-11 (typed inventory table), C-12 (rationale cites specific named signal), C-13 (hard ordering gate) from R1 excellence signals. Corrected score table: aspirationals are 10 pts each, not 5 pts. Max score now 130 pts. |
| v3 | 2026-03-17 | Added C-14 (gate row embedded in inventory table, V-04), C-15 (phase incompleteness predicate, V-03), C-16 (traceability failure repair instruction, V-04/V-01) from R2 excellence signals. Updated C-10 pass condition with explicit PARTIAL case. Max score now 160 pts. |
| v4 | 2026-03-17 | Added C-17 (completion tests as visible model output, V-02), C-18 (INVARIANT/VIOLATION/REPAIR triples, V-03), C-19 (dual gate architecture, V-04) from R3 excellence signals. Max score now 190 pts. |
