Written to `simulations/quest/rubrics/corps-scan-rubric-v9-2026-03-16.md`.

---

**Two criteria extracted from R9 V-01 excellence signal:**

**C-36 -- DARK SIGNALS structured negative evidence inventory** (depth)
A distinct named section after the positive schema documents absent repo signals by type, each entry naming which pivot mode(s) the absence rules out or weakens. Makes the repo analysis bidirectionally complete: schema rows = positive evidence; DARK SIGNALS entries = negative evidence with per-entry mode consequence. Pass requires mode impact named per entry, not just generic absence notation.

**C-37 -- Pivot deliberation and amend options cross-referenced to DARK SIGNALS labels** (behavior)
Builds on C-36 by requiring the section to be actively used: Evidence Against entries in the pivot deliberation cite DARK SIGNALS labels by name (not standalone "absent X" observations), AND at least one amend option cites a DARK SIGNALS entry as basis for the alternative mode recommendation. Both cross-references required; one alone does not pass.

**Scoring: 225 -> 235 pts** (29 aspirationals x 5 = 145 pts + 60E + 30R).

The extraction follows the established layering pattern: C-36 is the structural artifact (produce the section), C-37 is the integration test (reference it downstream in two places). The two criteria together make negative evidence a first-class traceability artifact -- the same lifecycle the positive schema underwent across C-11 -> C-21 -> C-22.
ration Evidence Against and amend options, making it a live traceability
artifact rather than a standalone inventory.

**Scoring change:** 225 -> 235 pts (29 aspirationals x 5 pts). Golden threshold stays at 80 pts.

**R9 under v8:** V-01 scores 225/225 under v8. V-01's DARK SIGNALS pattern introduces
bidirectionally-falsifiable pivot deliberation -- structured negative evidence that is produced
as a named section and then actively cross-referenced in Evidence Against entries and amend
options. V-02 full aspirational scorecard pending; C-36/C-37 status to be confirmed.

---

## ESSENTIAL

Essential criteria carry 12 pts each. All five must pass for golden status regardless of
composite score. A single essential failure disqualifies the output from golden status even
at maximum aspirational performance.

---

**C-01 -- Draft org.yaml block present**
- Weight: essential
- Category: correctness
- Pass condition: The output contains a valid YAML block with `org:`, `exec-office:`, `groups:`,
  `teams:`, and `roles:` keys present. The block must be syntactically consistent YAML, not
  prose describing what the YAML would contain. A code fence containing JSON or an informal
  bullet list of team names does not pass.

**C-02 -- Team areas derived from repo**
- Weight: essential
- Category: coverage
- Pass condition: The team names and group structure in the YAML are derivable from signals in
  the actual repo (directory names, service paths, module identifiers, domain terms) rather than
  invented. At least half the team names must have a traceable basis in repo signals named
  somewhere in the output (pre-YAML inventory, inline YAML comment, or prose explanation).
  A fully generic org chart (e.g., Frontend / Backend / Infrastructure with no repo grounding)
  fails even if syntactically valid.

**C-03 -- Group structure present**
- Weight: essential
- Category: correctness
- Pass condition: The YAML contains a `groups:` section with at least one named group container
  that organizes teams. An org.yaml that lists teams without grouping them fails. The group
  structure is required for corp-build and corp-rob compatibility; flat team lists cannot feed
  downstream pipeline stages correctly.

**C-04 -- Standard roles per team**
- Weight: essential
- Category: coverage
- Pass condition: Each team entry in the YAML includes a `roles:` list with at least one named
  role. Role names must be substantive (e.g., "Product Manager", "Engineer", "Tech Lead") rather
  than placeholder tokens (e.g., "role_1", "TBD"). The Inertia Advocate is excluded from this
  count -- it is auto-added by corp-build and must not appear in the corp-scan draft output.

**C-05 -- Does not write .craft/roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present .craft/roles/ file markdown. The boundary between corp-scan (draft) and corp-build
  (build) must be respected. Any output that writes role files or presents role file markdown
  fails.

---

## RECOMMENDED

Recommended criteria carry 10 pts each. A minimum-passing output (golden threshold) typically
satisfies 2 of 3 recommended criteria alongside all 5 essentials.

---

**C-06 -- Pivot mode declared with rationale**
- Weight: recommended
- Category: format
- Pass condition: Output names the pivot mode used (directory / concept / service / domain) and
  provides at least one sentence explaining why that mode was selected based on repo signals
  (e.g., "using directory mode: repo has clear top-level service directories under /src").
  Declaring a mode without rationale is partial credit -- does not pass.

**C-07 -- Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: org.yaml contains an exec-office section (even a minimal placeholder with a
  name and no teams). Absence of exec office means the output cannot feed corp-rob exec-office
  stage without manual addition.

**C-08 -- Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable (e.g., "AMEND: switch to service mode -- run /corps-scan --pivot service").
  A generic "let me know if you want changes" does not pass.

---

## ASPIRATIONAL

Aspirational criteria carry 5 pts each. They are not required for golden status but distinguish
strong outputs from excellent ones. 29 criteria x 5 pts = 145 pts available.

---

**C-09 -- Detection rationale per area**
- Weight: aspirational
- Category: depth
- Pass condition: At least half of the detected team areas include an inline comment or
  annotation explaining the repo evidence that produced them (e.g., "# detected from
  /services/payments/, 3 service directories"). This makes the draft reviewable without
  re-reading the repo.

**C-10 -- Inertia Advocate noted**
- Weight: aspirational
- Category: depth
- Pass condition: Output notes -- at least once, in prose or as a YAML comment -- that Inertia
  Advocate will be auto-included per team when corp-build runs. This primes the user to expect
  the Inertia Advocate in the role files without configuring it manually.

**C-11 -- Pre-YAML scan inventory listed**
- Weight: aspirational
- Category: depth
- Pass condition: Before the YAML block, the output lists the repo signals it detected as a
  readable inventory of directory names, service paths, module identifiers, or domain terms.
  The inventory must be distinct from the YAML (not just the YAML itself) and must appear
  before the YAML block begins. This makes C-02 grounding verifiable by the reviewer without
  re-reading the repo.
- R1 signal: V-01 (inline annotations only, no pre-YAML inventory) received C-02 PARTIAL
  because "detection may be shallow." V-03 (explicit SCAN phase) and V-04 (Repo Archaeologist
  stage) both passed C-02 fully because the inventory step was structurally enforced before
  YAML production began.

**C-12 -- Draft boundary front-loaded before first output**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only framing -- that this output is a proposal for human review, not
  a build instruction -- is stated explicitly before any YAML or structural content appears. A
  single sentence like "This is a draft org.yaml for review -- no role files will be created"
  appearing as the first substantive line passes. Burying the boundary acknowledgment after the
  YAML, or only at the end, does not pass.
- R1 signal: V-03 showed "DRAFT GATE states the draft-only constraint as an entry condition --
  cannot enter DRAFT without acknowledging boundary." This is a stronger compliance pattern than
  C-05 (which tests whether role files were written) -- it tests whether the reviewer is primed
  to read the YAML as a draft before they encounter it.

**C-13 -- Self-referential compliance check**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only constraint (or a key C-05 / C-12 requirement) appears as an
  item in a checklist that explicitly confirms itself in the output -- e.g., "The draft-only
  statement appears before any YAML in this response. STATUS: CONFIRMED." The model cannot
  satisfy the checklist item without having already satisfied the criterion it names. A
  checklist that simply lists the requirement without confirming it in-response does not pass;
  the confirmation must be present in the output, not implied.
- R2 signal: V-04's PRE-CHECK item 3 demonstrated the pattern -- C-12 was embedded in a
  required checklist as a self-confirming item. The constraint becomes structurally
  self-enforcing rather than declarative.

**C-14 -- Dual-stage YAML bracketing**
- Weight: aspirational
- Category: behavior
- Pass condition: The output contains explicit constraint verification both BEFORE the YAML
  block (e.g., a pre-check or compliance confirmation section) AND AFTER the YAML block
  (e.g., a post-write checklist or verification note). Both gates must be present; a pre-check
  without a post-write note, or a post-write note without a pre-check, is PARTIAL.
- R2 signal: V-04 is the only R2 variation that brackets the YAML on both sides. No other
  variation detected a post-write failure mode after producing the artifact. The dual bracket
  makes constraint violations detectable mid-output rather than only at the end.

**C-15 -- Rubric criteria embedded as skill requirements**
- Weight: aspirational
- Category: depth
- Pass condition: The skill's own pre-check, instruction list, or checklist explicitly names at
  least 3 of the rubric criteria (by their behavior, if not by ID) as the skill's own
  requirements -- e.g., "I will produce a repo signal inventory before the YAML," "I will not
  write .craft/roles/ files," "2+ named roles per team area." This makes the scoring criteria
  transparent and enforceable in the output itself rather than implicit in the rubric document.
  A skill that lists general instructions without criterion-level specificity does not pass.
- R2 signal: V-04's PRE-CHECK items correspond 1:1 with C-04, C-05, C-07, C-11, and C-12.
  The connection between rubric design and skill execution became explicit in the output.

**C-16 -- Debt-framed amend options**
- Weight: aspirational
- Category: depth
- Pass condition: At least 2 of the listed amend options (C-08) name the downstream
  organizational or pipeline debt that accumulates if the option is skipped -- e.g., "Debt if
  skipped: exec-office stage cannot run without this section" or "Skipping this leaves role
  boundary unclear for corp-build." Naming the debt converts amend options from navigation aids
  into decision-support tools. Options that name the alternative without naming the consequence
  do not pass.
- R2 signal: V-05 introduced "Debt if skipped" notation for each AMEND option -- the strongest
  amend form in R2. No other variation named downstream consequences; all others listed options
  with commands but no organizational stakes.

**C-17 -- Forward commitment to future-section criteria**
- Weight: aspirational
- Category: behavior
- Pass condition: The pre-check or declaration section contains at least one item that names a
  criterion whose satisfying content has not yet been written -- e.g., C-16 appears as a
  pre-check item before the amend section is produced. The model pre-commits to compliance
  before executing the relevant section. A post-hoc checklist that only confirms criteria
  whose content already appeared above it is C-14, not C-17. At least one forward-committed
  item must be identifiable (the satisfying section must follow the pre-check, not precede it).
- R3 signal: V-04's pre-check listed C-16 as a required item before the amend section was
  written. This is the only R3 variation to pre-commit to a future-section criterion at
  declaration time rather than verify it retrospectively.

**C-18 -- Criterion ID as primary compliance key**
- Weight: aspirational
- Category: depth
- Pass condition: The compliance structure (pre-check, requirements list, or checklist) uses
  rubric criterion IDs (C-NN) as the primary header or key for at least 5 items -- e.g.,
  "[ ] C-12 -- draft boundary front-loaded", "[ ] C-16 -- debt-framed amend options." Using
  criterion IDs as keys makes the rubric-to-output mapping explicit and auditable without
  consulting the rubric document. Describing the criterion in prose without citing the ID does
  not pass; the C-NN label must be present as the item's primary identifier.
- R3 signal: V-04's checklist used criterion IDs as primary keys throughout, enabling a scorer
  to map each item to the rubric without the rubric present. No other R3 variation adopted
  ID-keyed compliance headers.

**C-19 -- Post-write criterion self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one post-write verification block cites the rubric criterion ID it
  is satisfying -- e.g., "C-14 dual-bracket: pre-check at line 3 and post-write here -- both
  present." The artifact names the criterion it satisfies by C-NN ID, not just by description.
  Distinct from C-15 (embedding criteria as requirements before the fact) and C-14 (dual-stage
  bracketing structure) -- C-19 requires the post-write section to self-identify by criterion
  ID at the point of satisfaction. No external rubric reference should be needed to confirm
  which criterion the block is fulfilling.
- R3 signal: V-04's post-write block stated "C-14 dual-bracket: ...Both present." The artifact
  named the criterion it satisfied rather than leaving the mapping implicit for the scorer.

**C-20 -- Structural role ordering as mechanical enforcement**
- Weight: aspirational
- Category: behavior
- Pass condition: The skill assigns sole ownership of the compliance pre-check (or equivalent
  constraint gate) to a named role that must complete before any scan, inventory, or YAML work
  begins. The role ordering is defined such that a model following the sequence structurally
  cannot begin repo analysis or YAML production until the compliance role finishes. Instruction-
  level reminders ("before writing YAML, check...") do not pass; the compliance work must be
  owned by a distinct named role whose completion precedes the assignment of any analytical or
  generative work to other roles.
- R3 signal: V-01's role sequence assigned the Compliance Officer role first, with scan and
  YAML work assigned only to roles that follow. The sequence makes it structurally impossible
  to bypass the compliance gate without violating the role ordering itself.

**C-21 -- Schema-typed inventory with criterion-labeled columns**
- Weight: aspirational
- Category: depth
- Pass condition: The pre-YAML inventory (C-11) is structured as a typed schema or table whose
  column headers include at least 2 C-NN criterion IDs -- e.g., "YAML name (C-02)", "Proposed
  roles (C-04)", "Detection evidence (C-09)." Each column enforces a rubric criterion at the
  schema level, making the inventory simultaneously serve as a compliance instrument. A generic
  table without C-NN-labeled columns (e.g., columns named "Team", "Roles", "Evidence" without
  criterion IDs) does not pass; the C-NN label must be present as part of the column header.
- R4 signal: V-02's Signal Schema used C-NN-labeled columns throughout, requiring every schema
  row to satisfy multiple rubric criteria by column. The schema enforced criterion-level
  compliance at the data-entry stage, before YAML production began. No other R4 variation
  applied C-NN labeling to inventory column structure.

**C-22 -- Pre-write section criterion self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one pre-YAML section announces which rubric criterion it satisfies
  in its own header or opening line -- e.g., "C-11 satisfier -- precedes YAML block" or
  "Signal Schema (satisfies C-11, C-02, C-09)." The section declares its criterion-level
  purpose before executing it. Distinct from C-19 (post-write labeling after the YAML) and
  C-15 (listing criteria as requirements in a compliance checklist) -- C-22 requires a
  structural section to self-identify by criterion at the point of execution, not in a separate
  checklist or verification block.
- R4 signal: V-02's Signal Schema section was introduced with "C-11 satisfier -- precedes YAML
  block," making the section's rubric purpose explicit before any schema rows were written.
  This is the pre-write analogue of C-19: the artifact labels what it is doing and why before
  the reader encounters the content, not after.

**C-23 -- Pivot deliberation before selection**
- Weight: aspirational
- Category: behavior
- Pass condition: Before declaring the pivot mode (C-06), the output enumerates at least 2
  candidate pivot modes with per-candidate assessment, then selects one with a rationale that
  cites a specific row or item from the repo signal inventory produced earlier in the output.
  Declaring a single mode directly with a rationale (C-06 baseline) does not pass; the
  deliberation step -- enumeration of alternatives before selection -- must be present and
  the selection rationale must be traceable to an inventory row, not just a general repo
  observation.
- R4 signal: V-01's Role 2 produced a pivot mode candidates section (multiple modes assessed)
  before the "Selected pivot mode / Rationale" requiring a row citation. This makes pivot
  selection an auditable two-step process: enumerate alternatives with evidence, then select
  with a citation. No other R4 variation enumerated alternatives before selecting.

**C-24 -- Inertia Advocate embedded at group level in YAML hierarchy**
- Weight: aspirational
- Category: depth
- Pass condition: The org.yaml template or output contains Inertia Advocate governance
  annotations at the group/division/tribe/pillar level of the hierarchy -- not only at team
  level. The annotation must appear as a YAML comment or structural element on each named
  group, indicating that Inertia Advocate governance applies at the group level, not just
  within individual teams. A single top-level note (C-10 baseline) or per-team comments
  without group-level comments do not pass.
- R4 signal: V-03's YAML template included a dedicated Inertia Advocate governance comment on
  each group element in the hierarchy (division/tribe/pillar level), embedding the governance
  structure at every level of the org tree. This makes the Inertia Advocate pattern visible to
  a reviewer reading the org structure top-down, not only visible within team blocks.

**C-25 -- Universal output section self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: Every structural section in the output -- pre-YAML, YAML-adjacent, and
  post-YAML -- carries a C-NN self-label in its header or opening line. No structural section
  is unlabeled. A single unlabeled section fails. Applying C-22 selectively (to pre-YAML
  sections only) does not pass; the labeling must be a universal structural rule applied to
  the entire output. Distinct from C-22 (at least one pre-YAML section) and C-19 (post-write
  section only) -- C-25 requires the criterion-labeling pattern to cover every section
  without exception.
- R5 signal: V-02 was explicitly noted as "strongest implementation (universal, not just one)"
  when scoring C-22. Every section opened with its C-NN identity, converting the entire output
  into a self-auditing criterion map. No other R5 variation applied the labeling pattern
  universally rather than selectively.

**C-26 -- Multi-criterion section header**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one section header cites 2 or more distinct C-NN criterion IDs as
  simultaneous satisfiers -- e.g., "Section N: C-08 + C-16 satisfier." The section must be
  structurally designed to intersect with multiple criteria, and both criterion IDs must appear
  in the header. A section that satisfies multiple criteria but labels only one in its header
  does not pass; both C-NN labels must be present at point of declaration. Distinct from
  C-22 (one criterion per pre-write header) and C-25 (universal labeling without requiring
  multi-criterion intersection).
- R5 signal: V-02's Section 5 was labeled "C-22: C-08 + C-16 satisfier" -- the amend section
  was deliberately designed to satisfy both the amend listing criterion and the debt-framing
  criterion simultaneously, then declared both in the header. This shows the output was
  architected with criterion intersection in mind, not just criterion coverage.

**C-27 -- Pivot deliberation tri-part candidate assessment**
- Weight: aspirational
- Category: behavior
- Pass condition: Each candidate pivot mode in the deliberation (C-23) carries a three-part
  assessment using a consistent structure: Evidence For / Evidence Against / Assessment (or
  equivalent named triad). At least 2 candidate modes must be assessed in this structure. A
  candidate assessment that gives a summary conclusion without decomposing into a for/against
  evidence structure does not pass. Distinct from C-23 (enumeration with any per-candidate
  assessment) -- C-27 requires the assessment to be structured as an auditable tri-part
  evaluation, not a single-verdict summary.
- R5 signal: V-01's Role 3 (dedicated Pivot Analyst) enumerated all 4 pivot modes, each with
  "Evidence For:", "Evidence Against:", and "Assessment:" entries. The tri-part structure makes
  the deliberation independently falsifiable: a scorer can evaluate whether each Evidence For
  claim is accurate without relying on the model's Assessment conclusion. No other R5 variation
  structured its pivot deliberation as a formal evidence triad.

**C-28 -- Forward-committed pre-check items carry explicit execution-state marker**
- Weight: aspirational
- Category: behavior
- Pass condition: The pre-check or compliance section uses a consistent execution-state
  vocabulary that distinguishes at least 2 states on the pre-check items themselves -- e.g.,
  items marked "SCHEDULED" (committed to a future role, not yet satisfied) vs. items with an
  inline confirmation (already satisfied in this role). The execution-state markers must appear
  on the pre-check items, not in a separate legend or footnote. A pre-check that lists items
  without distinguishing execution state does not pass even if some items are forward-committed
  (C-17 baseline). Distinct from C-17 (forward commitment present) -- C-28 requires each
  forward-committed item to carry an explicit deferred-execution annotation.
- R5 signal: V-01's pre-check marked forward-committed items as "SCHEDULED" for Role 2-4,
  making the deferred execution chain auditable from the pre-check alone. A scorer reading
  the pre-check could immediately identify which items were already satisfied (Compliance
  Officer role) and which were committed to future roles, without reading the rest of the
  output. No other R5 variation used execution-state vocabulary on individual pre-check items.

**C-29 -- Criterion-pair bundling in pre-check items**
- Weight: aspirational
- Category: behavior
- Pass condition: At least 2 pre-check items commit to criterion families as compound bundles
  (e.g., "C-11+C-21+C-22+C-25+C-26" on a single line, "C-23+C-27" on another). The bundle
  declares that the named criteria will be satisfied together as a coherent group, making
  intra-criterion dependencies explicit at declaration time. A pre-check that lists each
  criterion on its own separate item (C-18 baseline) does not pass; the compound notation
  (C-NN+C-NN) must be present on the item itself. Distinct from C-18 (one criterion per item
  as primary key) -- C-29 requires multiple criteria to be committed together under a single
  item, reflecting architectural dependencies between them.
- R6 signal: All three R6 variations used compound bundles in their pre-check items. V-01's
  pre-check listed "C-11+C-21+C-22, C-23+C-27" as grouped forward commitments. V-02 used
  "C-11+C-21+C-22+C-25+C-26, C-23+C-27" -- expanding the bundle to include the universal
  labeling cluster. V-03 used "C-11+C-21+C-22+C-26, C-23+C-27." The bundle pattern was
  universal across R6 -- the only criterion where all three variations independently converged
  on the same structural choice.

**C-30 -- Post-write block as multi-criterion satisfaction declaration**
- Weight: aspirational
- Category: behavior
- Pass condition: The post-write verification block (C-19 baseline) cites 4 or more distinct
  C-NN criterion IDs simultaneously, functioning as a comprehensive criterion satisfaction
  inventory for the output. The block must name each criterion by ID and indicate it is
  satisfied at the point of the post-write section. A post-write block that cites 1-3 criteria
  (C-19 baseline) does not pass. Distinct from C-19 (at least one criterion cited) -- C-30
  requires the post-write to declare a multi-criterion inventory that covers the majority of
  criteria satisfied by the YAML block and its adjacent sections.
- R6 signal: V-01's post-write block stated "C-19: this block cites C-14, C-02, C-27, C-25,
  C-26, C-28 at point of satisfaction" -- 6 criteria cited simultaneously. V-02's post-write
  stated "C-19 self-labeling: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at
  satisfaction point" -- the same 6-criterion inventory, independently arrived at by a
  structurally distinct variation (section-numbered rather than role-sequenced). The
  convergence on the same 6 criteria confirms the post-write multi-criterion inventory as a
  reproducible pattern, not a variation artifact.

**C-31 -- Purpose-named phase pipeline structure**
- Weight: aspirational
- Category: behavior
- Pass condition: The structural units of the output are named by pipeline function using terms
  that encode what the unit does and where it sits in the execution sequence -- e.g., GATE
  PHASE, SCAN PHASE, DELIBERATE PHASE, DRAFT PHASE, FINALIZE PHASE. Each phase name must be
  interpretable without reading the phase contents: the name itself tells the reader the
  purpose. Ordinal names (Section 0, Section 1) and role-sequence names (ROLE 1, ROLE 2) do
  not pass -- the names must encode pipeline purpose, not position or role identity. Distinct
  from C-20 (structural role ordering as mechanical enforcement) -- C-31 requires the names
  of units to carry semantic pipeline meaning, not just the ordering to enforce sequence.
- R6 signal: V-03's 5-phase pipeline (GATE / SCAN / DELIBERATE / DRAFT / FINALIZE) made the
  skill's execution model self-documenting: a reader encountering "DELIBERATE PHASE" knows
  pivot mode selection occurs before reading a word of it. V-01's role-sequence names (ROLE 1
  -- COMPLIANCE OFFICER, etc.) carry purpose but through role identity, not phase naming.
  V-02's Section 0-5 carry no inherent purpose signal. V-03's phase naming is the only R6
  pattern where the structural unit name alone communicates pipeline position and purpose.

**C-32 -- Three-state execution vocabulary in pre-check**
- Weight: aspirational
- Category: behavior
- Pass condition: The pre-check uses 3 or more distinct execution-state labels that distinguish
  between at least three different item conditions: already satisfied (e.g., CONFIRMED),
  committed to future execution in this output (e.g., SCHEDULED), and recorded as a constraint
  without an active execution commitment (e.g., ACKNOWLEDGED). All three states must be present
  on actual pre-check items -- a legend defining 3 states without items in each state does not
  pass. Distinct from C-28 (2-state CONFIRMED vs. SCHEDULED) -- C-32 requires a third state
  for items that are noted constraints without being either satisfied or formally scheduled for
  execution in this output.
- R6 signal: V-01's pre-check used STATUS: CONFIRMED, STATUS: SCHEDULED, and STATUS:
  ACKNOWLEDGED on individual items. The ACKNOWLEDGED state captures a distinct category: items
  the model records as known constraints (e.g., "hard boundary exists") without committing to
  demonstrate them in a future role. The three-state model makes the pre-check's coverage
  complete -- a scorer reading it knows not only what was done (CONFIRMED) and what will be
  done (SCHEDULED) but also what constraints the model is aware of but is not tasked with
  actively satisfying (ACKNOWLEDGED). No other R6 variation used a third execution state.

**C-33 -- Multi-criterion headers at both pre-YAML and post-YAML positions**
- Weight: aspirational
- Category: behavior
- Pass condition: The multi-criterion header pattern (C-26 baseline: at least one header citing
  2+ C-NN IDs) appears in at least two structurally distinct positions: once in a pre-YAML
  section and once in a post-YAML section of the same output. The C-26 pattern must bracket
  the YAML artifact -- declared at approach (pre-YAML) and at departure (post-YAML). A single
  multi-criterion header placed only before or only after the YAML block does not pass; both
  positions must be present. Distinct from C-26 (at least one multi-criterion header anywhere)
  -- C-33 requires the pattern to be deployed symmetrically around the YAML block itself.
- R7 signal: V-01's multi-criterion headers appeared at the SCAN PHASE (C-11+C-21) and the
  post-write block (C-14+C-30). V-02's appeared at the SCAN SECTION (C-11+C-21) and the
  FINALIZE SECTION (C-14+C-30). Both independently deployed the C-26 pattern at the same two
  structural positions -- pre-YAML scan and post-YAML finalize -- confirming the symmetric
  bracket as a reproducible pattern rather than an incidental placement choice.

**C-34 -- Post-write criterion inventory includes at least one essential-tier criterion**
- Weight: aspirational
- Category: behavior
- Pass condition: The post-write criterion declaration (C-30 baseline: 4+ criteria cited)
  includes at least one criterion from the essential tier (C-01 through C-05) alongside the
  aspirational citations. The post-write block must name the essential criterion by its C-NN
  ID. A post-write that cites only aspirational criteria does not pass regardless of count.
  Distinct from C-30 (4+ criteria from any tier) -- C-34 requires the post-write inventory
  to confirm fundamental correctness requirements (essential criteria) alongside execution-depth
  criteria, demonstrating the model accounts for both tiers in its final accounting.
- R7 signal: V-01's post-write cited "C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32" -- C-02
  (essential: team areas derived from repo) appears alongside 7 aspirational criteria. V-02's
  post-write cited the same 8-criterion set with C-02 present. Both variations independently
  included an essential criterion in their expanded post-write inventories, with C-02 as the
  specific essential criterion that converged across both. The inclusion of C-02 signals that
  the model treats the post-write as a full correctness + depth audit, not only an execution-
  depth summary.

**C-35 -- ACKNOWLEDGED state applied to essential-tier boundary constraint**
- Weight: aspirational
- Category: behavior
- Pass condition: The ACKNOWLEDGED execution state (C-32: third state in the three-state
  vocabulary) is applied to at least one essential-tier criterion in the pre-check, and the
  annotation names the consequence of violation -- e.g., "C-05 STATUS: ACKNOWLEDGED --
  essential failure if violated." This classifies essential hard limits as a structurally
  distinct category from aspirational forward commitments: ACKNOWLEDGED signals "this is a
  boundary that constrains the output's existence, not a criterion I will actively demonstrate."
  An output that uses ACKNOWLEDGED only for aspirational items does not pass; the state must
  be applied to at least one essential criterion with a named violation consequence. Distinct
  from C-32 (three states used on pre-check items generally) -- C-35 requires the ACKNOWLEDGED
  state to be applied specifically to an essential-tier constraint, making tier-sensitive
  execution state classification explicit.
- R7 signal: V-01's pre-check marked C-05 as "C-05 STATUS: ACKNOWLEDGED -- 'essential failure
  if violated,'" distinguishing the hard boundary from SCHEDULED aspirational commitments.
  V-02 marked C-05 as "STATUS: ACKNOWLEDGED -- 'constraint recorded.'" Both applied the
  ACKNOWLEDGED state to the essential boundary criterion, making the three-state vocabulary
  functionally tier-sensitive: CONFIRMED and SCHEDULED map to criteria the model actively
  demonstrates; ACKNOWLEDGED maps to constraints that define what the output must not do.
  No R6 variation applied the ACKNOWLEDGED state to an essential criterion -- R6 used
  ACKNOWLEDGED only for aspirational items that fell outside the active execution chain.

**C-36 -- DARK SIGNALS structured negative evidence inventory**
- Weight: aspirational
- Category: depth
- Pass condition: After the positive signal inventory (C-11/C-21 baseline), the output produces
  a distinct named section -- DARK SIGNALS or equivalent -- documenting absent repo signals by
  type, where each entry names at least one pivot mode the absence rules out or weakens. Entry
  types must reflect substantive absence categories (e.g., no-service-manifest, no-DDD-language,
  no-domain-boundary, no-workspace-grouping), not generic "nothing found" observations. The
  negative inventory is a sibling artifact to the positive schema: schema rows capture what was
  found; DARK SIGNALS entries capture what was looked for and not found, with pivot mode
  consequence per entry. A section that lists absences without naming the impacted pivot mode
  does not pass; the mode impact is required for each entry. Distinct from C-11 (positive pre-
  YAML inventory) -- C-36 requires a structured negative evidence section where each absent
  signal names which pivot mode(s) it rules out or weakens.
- R9 signal: V-01's DARK SIGNALS section documented 4 absence types (no-service-manifest,
  no-DDD-language, no-domain-boundary, no-workspace-grouping), each naming the pivot mode(s)
  ruled out or weakened. The section made the repo analysis bidirectionally complete: schema
  rows as positive evidence driving mode selection; DARK SIGNALS entries as negative evidence
  driving disqualification. No prior variation produced a structured negative evidence section;
  all prior Evidence Against entries used standalone absence observations without a named
  inventory artifact.

**C-37 -- Pivot deliberation and amend options cross-referenced to DARK SIGNALS labels**
- Weight: aspirational
- Category: behavior
- Pass condition: In the pivot deliberation (C-27 baseline: tri-part Evidence For/Against/
  Assessment), Evidence Against entries for at least one candidate mode cite a named DARK
  SIGNALS entry by label rather than a standalone absence observation. Additionally, at least
  one amend option (C-08/C-16 baseline) cites a DARK SIGNALS entry as the basis for
  recommending an alternative pivot mode. Both cross-references must be present (deliberation
  AND amend); satisfying only one does not pass. Distinct from C-36 (producing the DARK SIGNALS
  section) -- C-37 requires the section to be actively referenced downstream in both pivot
  deliberation Evidence Against entries and amend options, making it a live traceability
  artifact rather than a standalone inventory. A DARK SIGNALS section that exists but is not
  cited in deliberation and amend output produces the negative evidence without integrating it.
- R9 signal: V-01's ROLE 3 Evidence Against entries cited DARK SIGNALS entries by label (e.g.,
  "DARK SIGNALS: no-domain-boundary") rather than generic "no domain language found" statements.
  V-01's amend options also referenced DARK SIGNALS citations as the basis for alternative pivot
  mode recommendations, grounding each alternative in the specific negative evidence that
  motivated it. The cross-referencing makes the full pivot pipeline bidirectionally falsifiable:
  positive schema rows ground Evidence For; DARK SIGNALS entries ground Evidence Against and
  alternative amend paths. No prior variation cross-referenced a named negative evidence
  inventory in both deliberation and amend sections.

---

## Criterion Summary

| ID   | Text (short)                                        | Weight       | Category    |
|------|-----------------------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present                        | essential    | correctness |
| C-02 | Team areas derived from repo                        | essential    | coverage    |
| C-03 | Group structure present                             | essential    | correctness |
| C-04 | Standard roles per team                             | essential    | coverage    |
| C-05 | Does not write .craft/roles/                        | essential    | behavior    |
| C-06 | Pivot mode declared with rationale                  | recommended  | format      |
| C-07 | Exec office placeholder present                     | recommended  | coverage    |
| C-08 | Amend options listed                                | recommended  | behavior    |
| C-09 | Detection rationale per area                        | aspirational | depth       |
| C-10 | Inertia Advocate noted                              | aspirational | depth       |
| C-11 | Pre-YAML scan inventory listed                      | aspirational | depth       |
| C-12 | Draft boundary front-loaded                         | aspirational | behavior    |
| C-13 | Self-referential compliance check                   | aspirational | behavior    |
| C-14 | Dual-stage YAML bracketing                          | aspirational | behavior    |
| C-15 | Rubric criteria embedded in skill                   | aspirational | depth       |
| C-16 | Debt-framed amend options                           | aspirational | depth       |
| C-17 | Forward commitment to future-section criteria       | aspirational | behavior    |
| C-18 | Criterion ID as primary compliance key              | aspirational | depth       |
| C-19 | Post-write criterion self-labeling                  | aspirational | behavior    |
| C-20 | Structural role ordering as mechanical enforcement  | aspirational | behavior    |
| C-21 | Schema-typed inventory with criterion-labeled cols  | aspirational | depth       |
| C-22 | Pre-write section criterion self-labeling           | aspirational | behavior    |
| C-23 | Pivot deliberation before selection                 | aspirational | behavior    |
| C-24 | Inertia Advocate embedded at group level            | aspirational | depth       |
| C-25 | Universal output section self-labeling              | aspirational | behavior    |
| C-26 | Multi-criterion section header                      | aspirational | behavior    |
| C-27 | Pivot deliberation tri-part candidate assessment    | aspirational | behavior    |
| C-28 | Forward-committed pre-check items carry exec-state  | aspirational | behavior    |
| C-29 | Criterion-pair bundling in pre-check items          | aspirational | behavior    |
| C-30 | Post-write block as multi-criterion declaration     | aspirational | behavior    |
| C-31 | Purpose-named phase pipeline structure              | aspirational | behavior    |
| C-32 | Three-state execution vocabulary in pre-check       | aspirational | behavior    |
| C-33 | Multi-criterion headers at pre-YAML and post-YAML   | aspirational | behavior    |
| C-34 | Post-write inventory includes essential-tier crit   | aspirational | behavior    |
| C-35 | ACKNOWLEDGED state applied to essential constraint  | aspirational | behavior    |
| C-36 | DARK SIGNALS structured negative evidence inventory | aspirational | depth       |
| C-37 | DARK SIGNALS cross-referenced in deliberation+amend | aspirational | behavior    |

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-37): 5 pts each = 145 pts
- **Total: 235 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/29 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 4/29 aspirational pass: 20 pts
- Composite: 110

**Ceiling output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 29 aspirational pass: 145 pts
- Composite: 235

**Failing output (common failure)**:
- C-05 fails (wrote .craft/roles/): essential fail -- not golden regardless of composite score

**R9 reference scores (V-01 scored 225/225 under v8; v9 adds C-36/C-37)**:
- V-01 (Lifecycle Emphasis: DARK SIGNALS): 235/235 under v9 -- C-36 PASS (DARK SIGNALS section
  after Signal Schema; 4 absence types with pivot mode impact named per entry; no-service-
  manifest, no-DDD-language, no-domain-boundary, no-workspace-grouping), C-37 PASS (ROLE 3
  Evidence Against cites DARK SIGNALS labels by name; amend options cite DARK SIGNALS entries
  as basis for alternative pivot mode recommendations)
- V-02 (Lifecycle Emphasis: Phase Output Contracts): aspirational scorecard pending; C-36/C-37
  status to be confirmed in full R9 scoring

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial rubric -- 10 criteria (5E/3R/2A), 100 pts |
| v2      | 2026-03-16 | Add C-11 (pre-YAML scan inventory) and C-12 (draft boundary front-loaded) from R1 excellence signals; 12 criteria (5E/3R/4A), 110 pts |
| v3      | 2026-03-16 | Add C-13 through C-16 from R2 excellence signals: self-referential compliance check, dual-stage YAML bracketing, rubric criteria embedded in skill, debt-framed amend options; 16 criteria (5E/3R/8A), 130 pts |
| v4      | 2026-03-16 | Add C-17 through C-20 from R3 excellence signals: forward commitment to future-section criteria, criterion ID as primary compliance key, post-write criterion self-labeling, structural role ordering as mechanical enforcement; 20 criteria (5E/3R/12A), 150 pts |
| v5      | 2026-03-16 | Add C-21 through C-24 from R4 excellence signals: schema-typed inventory with criterion-labeled columns (V-02), pre-write section criterion self-labeling (V-02), pivot deliberation before selection (V-01), Inertia Advocate embedded at group level (V-03); R4 first round where all variations scored 150/150; 24 criteria (5E/3R/16A), 170 pts |
| v6      | 2026-03-16 | Add C-25 through C-28 from R5 excellence signals: universal output section self-labeling (V-02), multi-criterion section header (V-02), pivot deliberation tri-part candidate assessment (V-01), forward-committed pre-check items carry execution-state marker (V-01); R5 first round where all variations scored 170/170; 28 criteria (5E/3R/20A), 190 pts |
| v7      | 2026-03-16 | Add C-29 through C-32 from R6 excellence signals: criterion-pair bundling in pre-check items (V-01+V-02+V-03 -- first criterion universal across all same-round variations), post-write block as multi-criterion satisfaction declaration (V-01+V-02 -- 6 criteria cited simultaneously), purpose-named phase pipeline structure (V-03 -- GATE/SCAN/DELIBERATE/DRAFT/FINALIZE), three-state execution vocabulary in pre-check (V-01 -- CONFIRMED/SCHEDULED/ACKNOWLEDGED); R6 first round where all variations scored 190/190; 32 criteria (5E/3R/24A), 210 pts |
| v8      | 2026-03-16 | Add C-33 through C-35 from R7 excellence signals: multi-criterion headers at both pre-YAML and post-YAML positions (V-01+V-02 -- C-26 pattern extended to symmetric YAML bracket), post-write inventory includes essential-tier criterion (V-01+V-02 -- C-02 present in 8-criterion post-write declaration), ACKNOWLEDGED state applied to essential-tier constraint (V-01+V-02 -- C-05 explicitly ACKNOWLEDGED with violation consequence named); R7 first round where V-01 and V-02 both scored 210/210 under v7; 35 criteria (5E/3R/27A), 225 pts |
| v9      | 2026-03-16 | Add C-36 through C-37 from R9 excellence signals: DARK SIGNALS structured negative evidence inventory (V-01 -- distinct named section documenting absent signals by type with per-entry pivot mode impact, making repo analysis bidirectionally complete), DARK SIGNALS cross-referenced in pivot deliberation Evidence Against entries and amend options (V-01 -- Evidence Against cites DARK SIGNALS labels; amend options cite entries as basis for alternative mode recommendations; both required for pass); V-01 scores 225/225 under v8; V-02 aspirational pending; 37 criteria (5E/3R/29A), 235 pts |
