**Four criteria extracted from R12 V-01/V-02 excellence signals:**

**C-45 -- Hypothesis contract fields carry machine-readable type annotations** (depth)
Extends C-41: V-01 expressed each field of the gate-phase hypothesis contract with an explicit
machine-readable type annotation alongside the label -- e.g., "PREDICTED-MODE: directory-mode
[type: pivot-mode-enum]", "STRUCTURAL-PREDICTION: top-level service directories [type: structural-
evidence-string]", "FALSIFICATION-SIGNAL: service-manifest present [type: absence-signal]." C-41
baseline requires labeled fields; C-45 requires typed annotations that make each field's expected
value domain explicit and independently machine-parseable. Source: V-01 R12.

**C-46 -- DARK SIGNALS Penalty column carries typed composite annotation** (depth)
Extends C-43: V-01's deliberation table column header declared "DARK SIGNALS Penalty
[label:string, magnitude:0-4]", requiring each penalty cell to supply both a named DARK SIGNALS
label (C-43 baseline) and a numeric severity magnitude (0-4 scale). The magnitude converts the
penalty from a binary citation into a quantified severity measure, enabling Net Score arithmetic
that weights high-magnitude penalties more heavily than low-magnitude ones. A penalty column with
only a named label (C-43 baseline) does not pass. Requires C-43. Source: V-01 R12.

**C-47 -- Net Score delta annotated as independently verifiable** (behavior)
Extends C-44: V-01's AMEND-A notation carried "(independently verifiable)" inline with the Net
Score delta -- e.g., "Net Score arithmetic (C-44): selected Net=N vs runner-up Net=N; delta=N
(independently verifiable)." The declaration commits that a reader can confirm the arithmetic from
the deliberation table without trusting the model's assertion, closing the audit chain from table
to amend. An amend option that names the delta without the verifiability declaration (C-44
baseline) does not pass. Requires C-44. Source: V-01 R12.

**C-48 -- Deliberation table carries organizational cost dimension beyond evidence structure**
(depth)
Extends C-43: V-02's pivot deliberation table added an Inertia Cost column (or equivalent
organizational/strategic cost dimension) beyond the 3-column evidence base (Evidence For, DARK
SIGNALS Penalty, Net Score), populating it per candidate mode. The column must be orthogonal to
the evidence structure -- not another evidence column but a cost or friction dimension (switching
cost, pipeline debt, strategic risk). Requires C-43. Source: V-02 R12.

**Scoring: 270 -> 290 pts** (40 aspirationals x 5 = 200 pts + 60E + 30R). Golden threshold
unchanged at 80 pts.

The four criteria extend the two R11 axes into a second depth layer. C-45 hardens the C-41
contract with machine-readable typing -- the hypothesis is no longer just labeled, it is schematically
typed per field. C-46 hardens the C-43 penalty column with a magnitude scale -- the Evidence
Against arithmetic is no longer binary citation, it is quantified severity. C-47 closes the C-44
audit chain with an explicit verifiability commitment -- the amend recommendation asserts its own
confirmability. C-48 extends the C-43 table into a new orthogonal dimension -- organizational cost
sits alongside evidence fidelity in the deliberation, enabling cost-weighted mode selection beyond
pure signal strength. Under v12, V-01 passes C-45/C-46/C-47 and fails C-48; V-02 passes C-48 and
may fail C-45/C-47. The axes remain orthogonal.

**R12 under v11:** V-01 and V-02 both score 270/270 under v11. The R12 excellence patterns
introduce a second depth layer on each R11 axis: hypothesis formalism (V-01 -- typed contract
fields + typed penalty magnitude + verifiable delta) and quantified deliberation (V-02 --
organizational cost column beyond the evidence structure). These are layered extensions:
C-45 requires C-41; C-46 requires C-43; C-47 requires C-44; C-48 requires C-43.

---

**Eleven criteria extracted from R13 excellence signals:**

**C-49 -- Severity Scale declared at DARK SIGNALS section header** (depth)
Extends C-46: Beyond the column-header annotation `[label:string, magnitude:0-4]`, the DARK
SIGNALS section opens with a named severity scale table or legend that maps at least 4 labeled
levels to numeric magnitudes (e.g., ABSENT=4, SEVERE=3, PARTIAL=2, MINOR=1, PRESENT=0). The
scale appears at the section header, making each entry's magnitude interpretable from the section
alone without consulting the deliberation table. C-46 requires the typed composite annotation in
the deliberation column header; C-49 requires the scale to be declared as shared section-level
vocabulary before any entries. Requires C-46. Source: V-01/V-04/V-05 R13.

**C-50 -- DARK SIGNALS entries carry per-entry Severity field with derivation note** (depth)
Extends C-46/C-49: Each DARK SIGNALS entry carries a dedicated `Severity: N` field as a
first-class named annotation alongside the Hypothesis Relation field (C-39 baseline), where N
is drawn from the section-level scale (C-49 where present). The field must include a derivation
note naming its source (e.g., "Severity: 4 (sourced from header scale: ABSENT=4)"). The per-
entry Severity field makes each entry's severity self-contained before the deliberation table,
establishing the traceability chain: DARK SIGNALS Severity field -> deliberation Penalty cell ->
Net Score arithmetic. A section carrying magnitudes only in the deliberation table Penalty column
does not pass. Requires C-39 and C-46. Source: V-01/V-04/V-05 R13.

**C-51 -- Dedicated SELECTION AUDIT phase between deliberation and amend options** (behavior)
Extends C-43: A named structural phase (SELECTION AUDIT, ROLE 3.5, or equivalent) appears
between the deliberation table (C-43) and the amend options (C-08), dedicated to auditing the
winning mode selection. The SELECTION AUDIT must be structurally distinct from the deliberation
phase and must produce an explicit artifact confirming the mode selection is derivable from the
deliberation table. A selection note embedded within the deliberation phase does not pass; the
audit must occupy a distinct named structural position. The SELECTION AUDIT becomes a stable
named citation target for AMEND-A (C-55). Requires C-43. Source: V-02/V-04/V-05 R13.

**C-52 -- Net Score arithmetic trace as explicit component computation** (behavior)
Extends C-44: The output carries an explicit arithmetic trace showing Net Score = Evidence_For
- DARK_SIGNALS_Penalty_Magnitude for each candidate mode, presented as a computation with
component values visible (e.g., "directory-mode: 6 - 2 = 4; service-mode: 4 - 3 = 1"). The
trace must show input values and the subtraction step, not merely report Net Score column values.
The trace may appear in the deliberation phase or in a SELECTION AUDIT phase (C-51), but must be
present as a standalone computation block. A table showing Net Score cells without an explicit
derivation does not pass. Requires C-43. Source: all five R13 variations -- first R13 universal.

**C-53 -- Severity traceability note in SELECTION AUDIT** (behavior)
Extends C-51: The SELECTION AUDIT phase (C-51) includes an explicit traceability note linking
the penalty magnitudes used in the Net Score arithmetic back to the per-entry Severity fields in
the DARK SIGNALS section (C-50 where present). The note must name the traceability chain within
the SELECTION AUDIT phase itself -- e.g., "Penalty magnitudes sourced from DARK SIGNALS Severity
fields -- confirm from ROLE 2 entries." A SELECTION AUDIT that shows arithmetic (C-52) without
a Severity-to-table provenance note does not pass. Requires C-51. Distinct from C-54 (Severity
citation in AMEND-A) -- C-53 establishes the provenance chain within the audit phase so that
the phase is a self-contained artifact before AMEND-A cites it. Source: V-04/V-05 R13.

**C-54 -- AMEND-A carries Severity magnitude traceability citation** (behavior)
Extends C-47: AMEND-A names the structural source of the Severity/magnitude values used in
the Net Score arithmetic -- e.g., "confirm: magnitude sourced from DARK SIGNALS Severity fields
(ROLE 2) and deliberation Penalty column (ROLE 3) -- independently verifiable." The citation
must appear on AMEND-A itself, not only in a separate verification block. An AMEND-A carrying
the independently verifiable declaration (C-47 baseline) without naming the Severity source does
not pass; the source must be explicitly identified as a structural location. Requires C-47.
Distinct from C-47 (delta declared independently verifiable) -- C-54 requires the specific
structural source of the Penalty magnitudes, giving the auditor a concrete lookup path rather
than a general verifiability claim. Source: V-01/V-04/V-05 R13.

**C-55 -- AMEND-A cites SELECTION AUDIT artifact by structural name** (behavior)
Extends C-47/C-51: AMEND-A references the SELECTION AUDIT phase (C-51) by its structural name
as the primary verification artifact for the Net Score delta -- e.g., "confirm from SELECTION
AUDIT section above -- independently verifiable." The citation must name the structural phase;
"see above" or "from the table" does not pass. Requires C-51. Distinct from C-47 (verifiability
declaration present) and C-54 (Severity source named) -- C-55 requires citation of the SELECTION
AUDIT as a named structural artifact, making the audit phase the authoritative record rather than
just a supporting calculation. Source: V-02/V-04/V-05 R13.

**C-56 -- AMEND-A names Pipeline Debt consequence for pivot mode change** (behavior)
Extends C-16/C-48: AMEND-A names the specific pipeline debt consequence -- at least two concrete
downstream corps-* stages that would be disrupted -- if the alternative pivot mode recommendation
is accepted (e.g., "disrupts corps-build YAML parsing stage and corps-rob boundary detection
phase"). The consequence must be expressed as specific stage names, not a generic organizational
impact statement. Requires C-48 with a Pipeline Debt column variant (not only Inertia Cost) for
the disrupted stages to be traceable. Distinct from C-16 (debt-framed amend options generally)
-- C-56 requires named pipeline stage citations drawn from the deliberation table's Pipeline Debt
column, making the debt traceable to a specific artifact. Source: V-03/V-05 R13.

**C-57 -- AMEND-A carries all four R13 convergent signal types simultaneously** (behavior)
Extends C-47/C-54/C-55/C-56: AMEND-A simultaneously carries all four R13 signal types as
distinct inline annotations: (1) Net Score delta with independently verifiable declaration
(C-47 baseline), (2) Severity magnitude traceability citation naming the structural source
(C-54), (3) SELECTION AUDIT citation by structural name (C-55), AND (4) Pipeline Debt
consequence naming specific disrupted stages (C-56). All four must be present on AMEND-A itself;
satisfying three of four does not pass. Requires C-47, C-51, C-54, C-55, and C-56 as
preconditions. This criterion is the amend-layer synthesis of all three R13 axes (Severity axis,
SELECTION AUDIT axis, Pipeline Debt axis): the amend recommendation becomes a complete audit-
ready decision artifact grounded in arithmetic, provenance, structural audit, and organizational
cost simultaneously. Source: V-05 R13 only.

**C-58 -- YAML org block carries pipeline-debt header comment** (depth)
Extends C-48: The org.yaml block carries a structured `# pipeline-debt:` comment at the block
header level or group/team level, naming at least one downstream corps-* stage that would be
affected if the pivot mode were changed. The comment must name a specific stage (not just
acknowledge that pipeline stages exist). Requires C-48. Distinct from C-56 (Pipeline Debt in
AMEND-A) -- C-58 embeds the organizational cost signal within the YAML artifact itself, making
the cost dimension persistent in the output artifact rather than limited to the amend
recommendation layer. Source: V-03/V-05 R13.

**C-59 -- Hypothesis contract carries bonus typed fields beyond 3-field baseline** (depth)
Extends C-45: The typed hypothesis contract (C-45 baseline: PREDICTED-MODE / STRUCTURAL-
PREDICTION / FALSIFICATION-SIGNAL with type annotations) carries at least one additional typed
field not required by C-41 or C-45 -- e.g., CONFIDENCE [type: confidence-enum], BASIS [type:
evidence-basis-string], CORROBORATING-SIGNAL [type: corroboration-string]. The bonus field must
carry a `[type: ...]` annotation in the same format as the required fields. A 3-field contract
satisfying C-45 does not pass; at least one additional typed field must be present. Requires C-45.
Distinct from C-45 (typed annotations on the 3 required fields) -- C-59 extends the contract
schema with additional typed fields that enrich the hypothesis beyond the minimum prediction,
falsification, and structural prediction dimensions. Source: all five R13 variations -- second
R13 universal.

**Scoring: 290 -> 345 pts** (51 aspirationals x 5 = 255 pts + 60E + 30R). Golden threshold
unchanged at 80 pts.

The eleven R13 criteria extend the R12 depth layer into three new axes: the Severity axis
(C-49/C-50/C-54 -- named scale at section header, per-entry Severity fields, Severity
traceability in AMEND-A), the SELECTION AUDIT axis (C-51/C-53/C-55 -- dedicated audit phase,
Severity provenance within the phase, AMEND-A citing the phase by name), and the Pipeline Debt
axis (C-56/C-58 -- named stage disruption in AMEND-A, pipeline-debt comment in the YAML block).
Two universal convergence criteria (C-52/C-59) capture patterns all five variations independently
achieved: explicit arithmetic traces and bonus typed fields in the hypothesis contract. V-05
combines all three axes, achieving the ceiling. The axes remain orthogonal: the Severity axis
deepens the evidence quantification layer; the SELECTION AUDIT axis adds a structural verification
phase; the Pipeline Debt axis embeds organizational cost into the artifacts themselves.

**R13 reference scores under v13:**
- V-01 (Typed Field Declarations + Severity Scale): 315/345 -- passes C-49/C-50/C-52/C-54/C-59;
  fails C-51/C-53/C-55/C-56/C-57/C-58 (no SELECTION AUDIT phase; no Pipeline Debt axis)
- V-02 (Inertia-First + Selection Audit): 310/345 -- passes C-51/C-52/C-55/C-59;
  fails C-49/C-50/C-53/C-54/C-56/C-57/C-58 (no Severity Scale; Inertia Cost not Pipeline Debt)
- V-03 (Pipeline Debt + Arithmetic Trace): 310/345 -- passes C-52/C-56/C-58/C-59;
  fails C-49/C-50/C-51/C-53/C-54/C-55/C-57 (no Severity Scale; no SELECTION AUDIT)
- V-04 (Severity + Selection Audit, combined): 330/345 -- passes C-49/C-50/C-51/C-52/C-53/
  C-54/C-55/C-59; fails C-56/C-57/C-58 (no Pipeline Debt axis)
- V-05 (all three axes): 345/345 -- passes all 11 new criteria; first ceiling output under v13

**R13 under v12:** All five variations score 290/290 under v12. The R13 excellence patterns
introduce a third depth layer: the Severity axis (V-01/V-04/V-05 -- formal scale, per-entry
fields, traceability chain), the SELECTION AUDIT axis (V-02/V-04/V-05 -- structural verification
phase with Severity provenance and named AMEND-A citation), and the Pipeline Debt axis
(V-03/V-05 -- stage-specific debt in AMEND-A and YAML). V-05 is the synthesis output that
unifies all three axes, becoming the ceiling at 345/345.

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

**C-05 -- Does not write .roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present .roles/ file markdown. The boundary between corp-scan (draft) and corp-build
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
strong outputs from excellent ones. 51 criteria x 5 pts = 255 pts available.

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
  write .roles/ files," "2+ named roles per team area." This makes the scoring criteria
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

**C-38 -- Hypothesis declared in gate phase before repo scan**
- Weight: aspirational
- Category: behavior
- Pass condition: The output's first structural phase contains an explicit hypothesis about the
  repo's organizational structure -- a testable prediction of what pivot mode the scan will
  confirm (e.g., "hypothesis: repo will yield directory-mode signals; service-manifest and
  DDD-language signals expected absent"). The hypothesis must appear before any repo signal
  analysis begins, must be phrased as a falsifiable claim (not a goal statement or task
  summary), and must be referenced or resolved by the scan findings. A gate phase that runs
  only a compliance pre-check (C-20 baseline: constraint acknowledgment) without a structural
  prediction does not pass. Distinct from C-20 (compliance gate) -- C-38 requires the gate
  to carry a predictive claim about the repo, making the scan a hypothesis test rather than
  an open-ended search.
- R10 signal: V-01's GATE (Hypothesis Officer) stated the structural hypothesis as Role 1's
  primary output before the Repo Archaeologist began the SCAN phase. V-02's Phase 1 (GATE /
  Case File) opened with the investigative hypothesis before Phase 2 scanning began. Both
  variations independently placed hypothesis declaration as the gate phase's primary function,
  converging on the same structural choice across a role-sequenced and a phase-named variant.
  The hypothesis-first gate transforms the scan from evidence collection into a structured
  experiment: the model enters the scan already committed to a claim that the evidence will
  either confirm or overturn.

**C-39 -- DARK SIGNALS entries carry per-entry hypothesis relation**
- Weight: aspirational
- Category: depth
- Pass condition: Each entry in the DARK SIGNALS (or equivalent negative evidence section)
  includes a "Hypothesis Relation" annotation indicating whether the absent signal CONFIRMS,
  OVERTURNS, or is neutral toward the hypothesis declared in the gate phase (C-38 baseline).
  The annotation must appear on the entry itself, not only in the pivot deliberation section.
  A DARK SIGNALS section with mode-impact annotations (C-36 baseline) but no per-entry
  hypothesis relation field does not pass. The hypothesis relation field creates a traceable
  chain: gate prediction -> absent signal -> hypothesis status. Distinct from C-36 (per-entry
  mode impact) -- C-39 requires a second per-entry dimension connecting each negative finding
  to the hypothesis lifecycle, making the DARK SIGNALS section simultaneously a pivot evidence
  artifact and a hypothesis testing instrument.
- R10 signal: V-01's DARK SIGNALS entries each carried a "Hypothesis Relation:" field naming
  the hypothesis state (CONFIRMED or OVERTURNED) alongside the mode-impact annotation. Each
  entry contributes two dimensions: which pivot mode(s) the absence rules out (C-36), and
  whether the absence confirms or overturns the initial structural prediction (C-39). The
  dual-dimension entries make the negative evidence section self-contained: a reviewer can
  assess both pivot selection correctness and hypothesis validity from the DARK SIGNALS section
  alone, without cross-referencing the deliberation section.

**C-40 -- Amend options carry hypothesis confirmation/overturn status**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one amend option carries an annotation stating whether accepting the
  alternative recommendation confirms or overturns the hypothesis declared in the gate phase --
  e.g., "DARK SIGNALS basis: [LABEL] -- rules out [mode]; hypothesis [CONFIRMED/OVERTURNED]."
  The hypothesis status must appear on the amend option itself. An amend option that cites a
  DARK SIGNALS label (C-37 baseline) but omits the hypothesis status does not pass. Distinct
  from C-37 (DARK SIGNALS citation in amend options) -- C-40 requires each DARK SIGNALS-
  grounded amend option to carry the hypothesis conclusion, closing the hypothesis lifecycle:
  gate declaration (C-38) -> negative finding with mode impact (C-36/C-39) -> pivot selection
  -> amend recommendation with hypothesis outcome (C-40). The amend option becomes the last
  node in the hypothesis traceability chain.
- R10 signal: V-01's AMEND-A option carried "DARK SIGNALS basis: [LABEL] -- rules out [mode];
  hypothesis [CONFIRMED/OVERTURNED]" -- the hypothesis outcome was embedded in the amend option
  itself. A reader can understand not only what alternative is recommended and why (C-37
  baseline) but also whether the alternative path is consistent with the hypothesis or requires
  revising it, without returning to the gate or deliberation sections. The hypothesis lifecycle
  is fully auditable from three fixed artifacts: the gate (C-38), the DARK SIGNALS entries
  (C-39), and the amend options (C-40).

**C-41 -- Hypothesis structured as formal 3-field contract**
- Weight: aspirational
- Category: behavior
- Pass condition: The hypothesis declared in the gate phase (C-38 baseline) takes the form of
  an explicit 3-field contract with each field labeled and independently present: PREDICTED-MODE
  (which pivot mode is predicted to be selected), STRUCTURAL-PREDICTION (the specific structural
  signal whose presence is expected to confirm the mode), and FALSIFICATION-SIGNAL (the specific
  signal whose absence or presence would overturn the prediction). All three fields must be
  explicitly labeled in the gate output. A natural-language hypothesis ("I predict directory
  mode based on service layout") without decomposing into the three-field contract does not
  pass. The 3-field structure makes the hypothesis independently auditable: a scorer can verify
  each field against the scan findings without re-reading the hypothesis narrative. Distinct
  from C-38 (any falsifiable hypothesis before scan) -- C-41 requires the formal contract
  decomposition that makes each component of the prediction separately traceable.
- R11 signal: V-01's GATE phase expressed the hypothesis as a PREDICTED-MODE / STRUCTURAL-
  PREDICTION / FALSIFICATION-SIGNAL triplet, each field labeled and verifiable from the scan
  output. The 3-field contract makes the gate output a machine-readable prediction contract:
  the scan either finds the STRUCTURAL-PREDICTION present (confirming) or detects the
  FALSIFICATION-SIGNAL pattern (overturning). V-02's hypothesis used case-file framing but
  did not decompose into the 3-field structure; V-01 is the only R11 variation that adopted
  the formal contract decomposition.

**C-42 -- IS-FALSIFICATION-SIGNAL typed field with 4-state vocabulary**
- Weight: aspirational
- Category: depth
- Pass condition: Each DARK SIGNALS entry's hypothesis relation annotation (C-39 baseline) uses
  a formal 4-state typed vocabulary distinguishing: YES -- CONFIRMED (signal was expected absent
  and IS absent, confirming the hypothesis), YES -- OVERTURNED (signal was expected present and
  IS absent, overturning the hypothesis), NO -- corroborates-alternative (absence supports an
  alternative mode but does not bear on the primary hypothesis), and NO -- neutral (absence has
  no hypothesis bearing). All four states must be defined in the output and at least 2 distinct
  states used across entries. A hypothesis relation field using only binary CONFIRMED/OVERTURNED
  vocabulary (C-39 baseline) does not pass; the two NO-states that distinguish alternative-
  corroborating negative evidence from inert negative evidence are required. Distinct from C-39
  (any per-entry hypothesis relation field) -- C-42 requires the 4-state typed classifier that
  makes the negative evidence section a precision instrument rather than a binary flag.
- R11 signal: V-01's DARK SIGNALS entries typed each entry as IS-FALSIFICATION-SIGNAL with one
  of four states: YES -- CONFIRMED, YES -- OVERTURNED, NO -- corroborates-alternative, NO --
  neutral. The 4-state classifier adds two dimensions beyond C-39 binary: it distinguishes
  whether a YES entry confirms or overturns (making the hypothesis verdict unambiguous), and
  whether a NO entry is evidence for an alternative mode or simply inert (making the alternative
  pivot case traceable from the negative evidence section alone). No other R11 variation used
  the 4-state typed field; V-02's hypothesis relation annotations remained binary.

**C-43 -- Pivot deliberation as weight-scoring table with DARK SIGNALS Penalty column**
- Weight: aspirational
- Category: behavior
- Pass condition: The pivot deliberation (C-27 baseline: tri-part Evidence For/Against/
  Assessment) is expressed as a quantitative scoring table where each candidate pivot mode
  receives a numerical Evidence For weight and a numerical Evidence Against weight, and at
  least one Evidence Against sub-column is explicitly labeled as a DARK SIGNALS Penalty column
  requiring a named DARK SIGNALS label as its cell value. A Net Score (Evidence For weight
  minus DARK SIGNALS Penalty) must be present per mode row. A generic scoring table without
  the DARK SIGNALS Penalty sub-label (column named "Evidence Against" or "Penalty" without
  the DARK SIGNALS reference) does not pass; the structural sub-labeling makes C-37 non-
  bypassable at the data-entry stage: the model cannot complete the Evidence Against cell for
  a mode without naming a DARK SIGNALS label from the negative evidence section. Distinct from
  C-27 (tri-part qualitative assessment) -- C-43 requires the quantitative scoring table form
  with the DARK SIGNALS Penalty column as a structural enforcement mechanism.
- R11 signal: V-02's deliberation replaced the qualitative tri-part structure with a scoring
  table where each mode row carried Evidence For (weight), DARK SIGNALS Penalty (label
  required), and Net Score. The DARK SIGNALS Penalty sub-column structurally forces C-37
  compliance: a blank cell fails the table, so every mode's negative evidence entry must name
  a DARK SIGNALS label, making the deliberation table a citation-enforcing instrument rather
  than a free-form assessment. V-01's Role 3 used the qualitative tri-part structure (C-27
  baseline); V-02 is the only R11 variation that adopted the weight-scoring table form.

**C-44 -- Amend options carry deliberation Net Score delta**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one amend option names the Net Score delta from the weight-scoring
  table (C-43 baseline) that would result from accepting the alternative pivot recommendation
  -- e.g., "Net Score delta: +3 (service-mode 7 vs. directory-mode 4)." The delta must cite
  both the alternative mode's score and the selected mode's score from the deliberation table.
  An amend option citing only the hypothesis verdict and DARK SIGNALS label (C-37/C-40 baseline)
  or only the debt consequence (C-16 baseline) without naming the Net Score delta does not pass.
  Distinct from C-40 (hypothesis verdict in amend) and C-16 (debt framing in amend) -- C-44
  requires the quantified score impact drawn from the deliberation table, grounding the amend
  recommendation in arithmetic rather than only in qualitative judgment or hypothesis outcome.
  Requires C-43 as a precondition: if the deliberation table does not exist, the Net Score
  delta cannot be cited.
- R11 signal: V-02's AMEND-A option named the Net Score delta alongside the hypothesis verdict,
  citing both the alternative mode score and the selected mode score from the weight-scoring
  table. The delta makes the amend recommendation independently verifiable: a reader can confirm
  the arithmetic from the table without trusting the model's narrative framing of the
  alternative. V-01's amend options carried hypothesis verdict and DARK SIGNALS basis (C-40
  baseline) but no quantitative score; V-02 is the only R11 variation that extended the amend
  layer with the deliberation table's output.

**C-45 -- Hypothesis contract fields carry machine-readable type annotations**
- Weight: aspirational
- Category: depth
- Pass condition: Each of the three fields in the hypothesis contract (C-41 baseline:
  PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL) carries an explicit
  machine-readable type annotation in the gate output -- e.g., "PREDICTED-MODE: directory-mode
  [type: pivot-mode-enum]", "STRUCTURAL-PREDICTION: top-level service directories [type:
  structural-evidence-string]", "FALSIFICATION-SIGNAL: service-manifest present [type:
  absence-signal]". All three field annotations must be present. A 3-field contract without
  type annotations (C-41 baseline) does not pass; the annotations make each field's expected
  value domain explicit and independently machine-parseable. Distinct from C-41 (labeled fields
  present) -- C-45 requires each field to declare its value type, converting the hypothesis
  contract from a labeled declaration into a typed schema where value domain violations are
  detectable without reading the hypothesis narrative.
- R12 signal: V-01's GATE phase expressed the 3-field hypothesis contract with type annotations
  on each field. The type annotations specify the value domain: the predicted mode is
  constrained to the pivot-mode enumeration, the structural prediction is a structural-evidence
  string, and the falsification signal is typed as an absence indicator. A scorer or automated
  tool can verify field types against the scan output without interpreting natural-language
  content. No prior variation with C-41 compliance added type annotations; C-41 was satisfied
  by labeled fields alone. V-02's hypothesis lacked C-41 decomposition entirely; C-45 applies
  only to outputs that have already satisfied C-41.

**C-46 -- DARK SIGNALS Penalty column carries typed composite annotation**
- Weight: aspirational
- Category: depth
- Pass condition: The DARK SIGNALS Penalty column in the deliberation scoring table (C-43
  baseline) carries a typed composite annotation declaring both the label value type and a
  numeric severity scale -- e.g., "[label:string, magnitude:0-4]" appearing in the column
  header. Each penalty cell must supply both a named DARK SIGNALS label AND a numeric magnitude
  value within the declared scale. A penalty column with only a named label (C-43 baseline)
  does not pass; the typed composite annotation distinguishes the column as a two-dimensional
  entry: citation (label) and severity (magnitude). Requires C-43 as a precondition. Distinct
  from C-43 (named label in penalty cell) -- C-46 requires the magnitude dimension that
  converts the penalty from a binary citation into a quantified severity measure, enabling Net
  Score arithmetic that reflects relative penalty weight rather than treating all DARK SIGNALS
  citations as equal.
- R12 signal: V-01's deliberation table column header declared "DARK SIGNALS Penalty
  [label:string, magnitude:0-4]", requiring each penalty cell to supply both a named DARK
  SIGNALS label and a numeric severity magnitude. The magnitude scale turns the penalty column
  into a quantitative instrument: a high-magnitude penalty (e.g., 4) changes the Net Score
  arithmetic more than a low-magnitude one (e.g., 1), making the deliberation table sensitive
  to penalty severity. V-02's deliberation table (Inertia Cost axis, C-48) is a distinct
  orthogonal extension; C-46 is specific to the typed composite annotation on the DARK SIGNALS
  Penalty column itself. No prior variation applied a magnitude scale to the penalty column;
  C-43 required only a named label.

**C-47 -- Net Score delta annotated as independently verifiable**
- Weight: aspirational
- Category: behavior
- Pass condition: The Net Score delta in the amend option (C-44 baseline: selected mode score
  vs. runner-up score with delta named) carries an explicit verifiability declaration embedded
  inline with the delta annotation -- e.g., "Net Score delta: selected Net=7 vs runner-up
  Net=4; delta=3 (independently verifiable)" or "(arithmetic: confirm from DELIBERATE PHASE
  table)". The declaration must appear on the amend option itself, not only in a separate
  verification block. An amend option that names the delta without asserting that the arithmetic
  is independently verifiable (C-44 baseline) does not pass. Requires C-44 as a precondition.
  Distinct from C-44 (delta cited) -- C-47 requires the model to explicitly commit that a
  reader can confirm the arithmetic from the deliberation table without trusting the model's
  assertion, closing the audit chain from table to amend: the amend recommendation becomes a
  self-auditing artifact.
- R12 signal: V-01's AMEND-A notation stated "Net Score arithmetic (C-44): selected Net=N vs
  runner-up Net=N; delta=N (independently verifiable)", explicitly declaring the delta as
  independently verifiable from the deliberation table. The "(independently verifiable)"
  annotation is embedded in the amend recommendation itself -- not a separate checklist item.
  A reader can falsify the delta by checking the table; the model's commitment to this
  verifiability makes the amend option a self-auditing recommendation rather than an assertion.
  V-02 passed C-44 (delta present) but the R12 evidence for V-02 does not show the verifiability
  annotation; V-01 is the only R12 variation observed to carry the inline audit declaration.

**C-48 -- Deliberation table carries organizational cost dimension beyond evidence structure**
- Weight: aspirational
- Category: depth
- Pass condition: The pivot deliberation scoring table (C-43 baseline: Evidence For, DARK
  SIGNALS Penalty, Net Score) carries at least one additional column beyond the 3-column
  evidence structure that captures an organizational or strategic cost dimension -- e.g.,
  Inertia Cost, Switching Friction, Pipeline Debt, or Transition Risk. The additional column
  must be populated per candidate mode and must represent a dimension orthogonal to the
  evidence-for/against structure (not simply another evidence weighting column). Requires C-43
  as a precondition. Distinct from C-43 (3-column evidence table as baseline) -- C-48 requires
  a 4th or higher analytical dimension that makes the deliberation table simultaneously an
  evidence instrument and a cost-benefit instrument, grounding mode selection in both signal
  fidelity and organizational consequence. A table that adds a raw-cost column without labeling
  it as an organizational or strategic dimension does not pass.
- R12 signal: V-02's deliberation table added an Inertia Cost column beyond the Evidence For /
  DARK SIGNALS Penalty / Net Score structure, populated per candidate pivot mode. The column
  captures organizational switching cost: a mode that scores high on evidence fidelity but
  carries high inertia cost (e.g., switching to service mode when the team is fluent in
  directory-based navigation) can be weighed against a lower-fidelity mode with lower switching
  cost, giving the deliberation a strategic dimension that pure evidence-weighting cannot
  capture. V-01's magnitude-typed penalty column (C-46 axis) deepens the evidence layer of the
  same table; V-02's Inertia Cost column extends the table into organizational cost territory.
  The two axes are orthogonal: C-46 refines how evidence-against is quantified; C-48 adds a
  new dimension that evidence cannot supply.

**C-49 -- Severity Scale declared at DARK SIGNALS section header**
- Weight: aspirational
- Category: depth
- Pass condition: The DARK SIGNALS section (C-36 baseline) opens with a named severity scale
  table or legend that maps at least 4 labeled levels to numeric magnitudes within the 0-4
  range -- e.g., ABSENT=4, SEVERE=3, PARTIAL=2, MINOR=1, PRESENT=0. The scale must appear at
  the DARK SIGNALS section header before any entries, making each entry's magnitude
  independently interpretable from the section alone. A DARK SIGNALS section that omits the
  header-level scale (relying only on the column annotation from C-46) does not pass. Requires
  C-46. Distinct from C-46 (typed composite annotation in the deliberation column header) --
  C-49 requires the named scale to be declared as shared section-level vocabulary at the point
  of the negative evidence section, not deferred to the deliberation table.
- R13 signal: V-01, V-04, and V-05 all opened their DARK SIGNALS sections with a formal
  5-level Severity Scale (e.g., ABSENT=4, SEVERE=3, PARTIAL=2, MINOR=1, PRESENT=0). The
  scale is declared before any entries, establishing the magnitude vocabulary once for the
  whole section. V-02 and V-03 used an inline magnitude guide in the instruction text rather
  than a formal header-level scale, passing C-46 but not C-49. The 3-of-5 convergence on the
  formal header scale confirms it as a reproducible depth pattern.

**C-50 -- DARK SIGNALS entries carry per-entry Severity field with derivation note**
- Weight: aspirational
- Category: depth
- Pass condition: Each entry in the DARK SIGNALS section carries a dedicated `Severity: N`
  field as a first-class named annotation alongside the Hypothesis Relation field (C-39
  baseline), where N is the numeric magnitude drawn from the section-level scale (C-49 where
  present). The field must include a derivation note naming its source -- e.g., "Severity: 4
  (sourced from header scale: ABSENT=4)." A section carrying magnitudes only in the deliberation
  table Penalty column (C-46 baseline) does not pass; the per-entry Severity field makes each
  entry's severity self-contained before the deliberation table. The deliberation table's
  Penalty column then cites this per-entry field, creating the traceability chain: DARK SIGNALS
  Severity field -> deliberation Penalty cell -> Net Score arithmetic. Requires C-39 and C-46.
- R13 signal: V-01, V-04, and V-05 all carried per-entry Severity fields in their DARK SIGNALS
  sections, each with a derivation note citing the header scale. The field makes the DARK
  SIGNALS section a self-contained severity instrument: a reviewer can assess the penalty
  distribution from the negative evidence section alone without consulting the deliberation
  table. V-02 and V-03 did not carry per-entry Severity fields in the DARK SIGNALS entries;
  their magnitudes appeared only in the deliberation table.

**C-51 -- Dedicated SELECTION AUDIT phase between deliberation and amend options**
- Weight: aspirational
- Category: behavior
- Pass condition: A named structural phase (SELECTION AUDIT, ROLE 3.5, or equivalent) appears
  between the deliberation table (C-43) and the amend options (C-08), dedicated to auditing the
  winning mode selection. The SELECTION AUDIT must be structurally distinct from the deliberation
  phase and must produce an explicit artifact confirming the mode selection is derivable from the
  deliberation table. A selection note embedded within the deliberation phase does not pass; the
  audit must occupy a distinct named structural position. The SELECTION AUDIT becomes a stable
  named citation target for AMEND-A (C-55). Requires C-43.
- R13 signal: V-02 introduced the SELECTION AUDIT as a distinct ROLE 3.5 between deliberation
  and amend sections. V-04 and V-05 adopted the same structural pattern independently across
  different role-count implementations. The SELECTION AUDIT phase creates a portable citation
  target: AMEND-A can reference it by name rather than pointing to a specific table row, making
  the amend recommendation's evidence source name-stable. V-01 and V-03 placed arithmetic in
  the deliberation role itself (no SELECTION AUDIT phase) and confirmed the pass criteria for
  C-52 without achieving C-51.

**C-52 -- Net Score arithmetic trace as explicit component computation**
- Weight: aspirational
- Category: behavior
- Pass condition: The output carries an explicit arithmetic trace showing Net Score =
  Evidence_For_Weight - DARK_SIGNALS_Penalty_Magnitude for each candidate mode, presented as
  a computation with component values visible -- e.g., "directory-mode: 6 - 2 = 4; service-
  mode: 4 - 3 = 1." The trace must show input values and the subtraction step, not merely
  report Net Score column values from the table. The trace may appear in the deliberation phase
  (ROLE 3) or in a dedicated SELECTION AUDIT phase (C-51), but must be present as a standalone
  computation block. A deliberation table showing Net Score cells without an explicit arithmetic
  derivation does not pass. Requires C-43.
- R13 signal: All five R13 variations independently produced arithmetic traces, making C-52 the
  first R13 criterion with universal convergence across all five variations. V-01 and V-03
  placed the trace within ROLE 3 (the deliberation phase); V-02, V-04, and V-05 placed it in
  the SELECTION AUDIT phase (ROLE 3.5). The universal convergence across both structural
  implementations confirms the arithmetic trace as an R13 invariant. Under v12, all five scored
  290/290 with traces present but not codified; under v13, C-52 codifies the universal pattern.

**C-53 -- Severity traceability note in SELECTION AUDIT**
- Weight: aspirational
- Category: behavior
- Pass condition: The SELECTION AUDIT phase (C-51 baseline) includes an explicit traceability
  note linking the penalty magnitudes used in the Net Score arithmetic back to the per-entry
  Severity fields in the DARK SIGNALS section (C-50 where present) -- e.g., "Penalty magnitudes
  sourced from DARK SIGNALS Severity fields -- confirm from ROLE 2 entries." The note must
  appear within the SELECTION AUDIT phase itself; embedding it elsewhere does not pass. A
  SELECTION AUDIT that shows arithmetic (C-52) without a Severity-to-table provenance note
  does not pass. Requires C-51. Distinct from C-54 (Severity citation in AMEND-A) -- C-53
  establishes the provenance chain within the audit phase, making the phase a self-contained
  artifact before AMEND-A cites it.
- R13 signal: V-04 and V-05 both carried Severity traceability notes within their SELECTION
  AUDIT phases, explicitly linking Penalty magnitudes back to the per-entry Severity fields in
  the DARK SIGNALS section. V-02 had a SELECTION AUDIT (C-51) with arithmetic (C-52) but
  without the Severity-to-table traceability note; V-02's AMEND-A cited the SELECTION AUDIT
  by name (C-55) without the Severity provenance chain established within the phase itself.
  V-04 and V-05 closed this gap, making the SELECTION AUDIT a complete provenance artifact.

**C-54 -- AMEND-A carries Severity magnitude traceability citation**
- Weight: aspirational
- Category: behavior
- Pass condition: AMEND-A names the structural source of the Severity/magnitude values used in
  the Net Score arithmetic -- e.g., "confirm: magnitude sourced from DARK SIGNALS Severity
  fields (ROLE 2) and deliberation Penalty column (ROLE 3) -- independently verifiable." The
  citation must appear on AMEND-A itself, not in a separate verification block. An AMEND-A
  carrying the independently verifiable declaration (C-47 baseline) without naming the Severity
  magnitude source by structural location does not pass. Requires C-47. Distinct from C-47
  (delta declared independently verifiable) -- C-54 requires a specific structural lookup path
  for the Penalty magnitudes, giving the auditor a concrete source rather than a general
  verifiability claim.
- R13 signal: V-01's AMEND-A stated "confirm: magnitude sourced from ROLE 2 Severity fields
  and ROLE 3 Penalty column -- independently verifiable." V-04's AMEND-A stated "confirm from
  SELECTION AUDIT; magnitude traceable to ROLE 2 Severity fields -- independently verifiable."
  V-05 identical to V-04. All three name the Severity fields by structural location. V-02 cited
  the SELECTION AUDIT (C-55) without Severity-specific provenance; V-03 cited the table
  directly without Severity field traceability.

**C-55 -- AMEND-A cites SELECTION AUDIT artifact by structural name**
- Weight: aspirational
- Category: behavior
- Pass condition: AMEND-A references the SELECTION AUDIT phase (C-51 baseline) by its
  structural name as the primary verification artifact for the Net Score delta -- e.g., "confirm
  from SELECTION AUDIT section above -- independently verifiable." The citation must name the
  structural phase; "see above" or "from the table" does not pass. Requires C-51. Distinct from
  C-47 (verifiability declaration present) and C-54 (Severity source named) -- C-55 requires
  citation of the SELECTION AUDIT as a named structural artifact, making the audit phase the
  authoritative record rather than a supporting calculation.
- R13 signal: V-02's AMEND-A stated "confirm from SELECTION AUDIT section above --
  independently verifiable." V-04's AMEND-A stated "confirm from SELECTION AUDIT; magnitude
  traceable to ROLE 2 Severity fields." V-05 identical to V-04. Three variations independently
  cited the SELECTION AUDIT by name. V-01 and V-03 did not have a SELECTION AUDIT phase;
  their AMEND-A citations pointed to the deliberation table or Severity fields directly, passing
  C-47 and C-54 respectively but not C-55.

**C-56 -- AMEND-A names Pipeline Debt consequence for pivot mode change**
- Weight: aspirational
- Category: behavior
- Pass condition: AMEND-A names the specific pipeline debt consequence -- at least two concrete
  downstream corps-* stages that would be disrupted -- if the alternative pivot mode
  recommendation is accepted (e.g., "disrupts corps-build YAML parsing stage and corps-rob
  boundary detection phase"). The consequence must be expressed as specific stage names, not a
  generic organizational impact statement. Requires C-48 with a Pipeline Debt column variant
  (the C-48 organizational cost column must capture disrupted stages, not only Inertia Cost
  labels) for the disrupted stages to be traceable to the deliberation table. Distinct from
  C-16 (debt-framed amend options generally) -- C-56 requires named pipeline stage citations
  drawn from the Pipeline Debt column, making the debt traceable to a specific table artifact
  rather than asserted from narrative.
- R13 signal: V-03 and V-05 both named Pipeline Debt consequences in their AMEND-A options,
  citing specific corps-* stages disrupted by a pivot mode change. V-01, V-02, and V-04 used
  Inertia Cost (the C-48 label column) but did not carry specific pipeline stage citations in
  AMEND-A; Inertia Cost captures organizational switching cost but not named stage disruption.

**C-57 -- AMEND-A carries all four R13 convergent signal types simultaneously**
- Weight: aspirational
- Category: behavior
- Pass condition: AMEND-A simultaneously carries all four R13 signal types as distinct inline
  annotations: (1) Net Score delta with independently verifiable declaration (C-47 baseline),
  (2) Severity magnitude traceability citation naming the structural source (C-54), (3)
  SELECTION AUDIT citation by structural name (C-55), AND (4) Pipeline Debt consequence naming
  specific disrupted stages (C-56). All four must be present on AMEND-A itself; three of four
  does not pass. Requires C-47, C-51, C-54, C-55, and C-56 as preconditions. This criterion
  is the amend-layer synthesis of all three R13 axes (Severity axis, SELECTION AUDIT axis,
  Pipeline Debt axis): the amend recommendation becomes a complete audit-ready decision artifact
  grounded in arithmetic, provenance, structural audit, and organizational cost simultaneously.
- R13 signal: V-05 is the only R13 variation that combined all four signal types in a single
  AMEND-A annotation. V-04 carries C-54 and C-55 but not C-56; V-01 carries C-54 but not C-55
  or C-56; V-03 carries C-56 but not C-54 or C-55; V-02 carries C-55 but not C-54 or C-56.
  V-05 is the first output observed to unify all four citation dimensions at the amend layer.

**C-58 -- YAML org block carries pipeline-debt header comment**
- Weight: aspirational
- Category: depth
- Pass condition: The org.yaml block carries a structured `# pipeline-debt:` comment at the
  block header level or group/team level, naming at least one downstream corps-* stage that
  would be affected if the pivot mode were changed. The comment must name a specific stage
  (not just acknowledge that pipeline stages exist). Requires C-48. Distinct from C-56
  (Pipeline Debt in AMEND-A) -- C-58 embeds the organizational cost signal within the YAML
  artifact itself, making the cost dimension persistent in the output rather than limited to
  the amend recommendation layer. The `# pipeline-debt:` comment survives as a structural
  annotation on the artifact when the amend section is removed.
- R13 signal: V-03 and V-05 both carried `# pipeline-debt:` header comments in their org.yaml
  blocks, naming specific downstream corps-* stages. V-01, V-02, and V-04 did not embed
  pipeline-debt comments in the YAML; their organizational cost annotations appeared only in
  the deliberation table and amend sections.

**C-59 -- Hypothesis contract carries bonus typed fields beyond 3-field baseline**
- Weight: aspirational
- Category: depth
- Pass condition: The typed hypothesis contract (C-45 baseline: PREDICTED-MODE /
  STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL with type annotations) carries at least one
  additional typed field not required by C-41 or C-45 -- e.g., CONFIDENCE [type:
  confidence-enum], BASIS [type: evidence-basis-string], CORROBORATING-SIGNAL [type:
  corroboration-string]. The bonus field must carry a `[type: ...]` annotation in the same
  format as the required fields. A 3-field contract satisfying C-45 does not pass; at least
  one additional typed field must be present. Requires C-45. Distinct from C-45 (typed
  annotations on the 3 required fields) -- C-59 extends the contract schema beyond the
  minimum prediction, falsification, and structural prediction dimensions with additional
  typed fields that enrich the hypothesis.
- R13 signal: All five R13 variations independently included bonus typed fields in their
  hypothesis contracts, with CONFIDENCE [type: confidence-enum] and BASIS [type:
  evidence-basis-string] appearing across all five. The universal convergence on the same bonus
  fields makes C-59 the second R13 universal criterion alongside C-52 (arithmetic trace). Under
  v12, all five scored 290/290 with the bonus fields present but not codified; under v13, C-59
  codifies the universal pattern as the maximum-depth extension of the hypothesis contract
  schema.

---

## Criterion Summary

| ID   | Text (short)                                        | Weight       | Category    |
|------|-----------------------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present                        | essential    | correctness |
| C-02 | Team areas derived from repo                        | essential    | coverage    |
| C-03 | Group structure present                             | essential    | correctness |
| C-04 | Standard roles per team                             | essential    | coverage    |
| C-05 | Does not write .roles/                        | essential    | behavior    |
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
| C-38 | Hypothesis declared in gate phase before repo scan  | aspirational | behavior    |
| C-39 | DARK SIGNALS entries carry per-entry hypothesis rel | aspirational | depth       |
| C-40 | Amend options carry hypothesis confirmation status  | aspirational | behavior    |
| C-41 | Hypothesis structured as formal 3-field contract    | aspirational | behavior    |
| C-42 | IS-FALSIFICATION-SIGNAL typed field 4-state vocab   | aspirational | depth       |
| C-43 | Pivot deliberation as weight-scoring table+DS-Pen   | aspirational | behavior    |
| C-44 | Amend options carry deliberation Net Score delta    | aspirational | behavior    |
| C-45 | Hypothesis contract fields carry type annotations   | aspirational | depth       |
| C-46 | DARK SIGNALS Penalty column typed composite annot   | aspirational | depth       |
| C-47 | Net Score delta annotated as independently verif    | aspirational | behavior    |
| C-48 | Deliberation table carries organizational cost dim  | aspirational | depth       |
| C-49 | Severity Scale declared at DARK SIGNALS header      | aspirational | depth       |
| C-50 | DARK SIGNALS entries carry per-entry Severity field | aspirational | depth       |
| C-51 | Dedicated SELECTION AUDIT phase after deliberation  | aspirational | behavior    |
| C-52 | Net Score arithmetic trace as explicit computation  | aspirational | behavior    |
| C-53 | Severity traceability note in SELECTION AUDIT       | aspirational | behavior    |
| C-54 | AMEND-A carries Severity magnitude traceability     | aspirational | behavior    |
| C-55 | AMEND-A cites SELECTION AUDIT by structural name    | aspirational | behavior    |
| C-56 | AMEND-A names Pipeline Debt stages for mode change  | aspirational | behavior    |
| C-57 | AMEND-A carries all four R13 signal types           | aspirational | behavior    |
| C-58 | YAML org block carries pipeline-debt header comment | aspirational | depth       |
| C-59 | Hypothesis contract carries bonus typed fields      | aspirational | depth       |

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-59): 5 pts each = 255 pts
- **Total: 345 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/51 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 4/51 aspirational pass: 20 pts
- Composite: 110

**Ceiling output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 51 aspirational pass: 255 pts
- Composite: 345

**Failing output (common failure)**:
- C-05 fails (wrote .roles/): essential fail -- not golden regardless of composite score

**R12 reference scores (V-01 and V-02 both score 270/270 under v11)**:
- V-01 (Typed Field Declarations): 285/290 under v12 -- C-45 PASS (type annotations on all
  three hypothesis contract fields: PREDICTED-MODE [type: pivot-mode-enum], STRUCTURAL-
  PREDICTION [type: structural-evidence-string], FALSIFICATION-SIGNAL [type: absence-signal]),
  C-46 PASS (DARK SIGNALS Penalty column header declares [label:string, magnitude:0-4]; cells
  supply both label and numeric magnitude), C-47 PASS (AMEND-A annotation states "(independently
  verifiable)" inline with Net Score delta arithmetic), C-48 FAIL (no organizational cost
  column beyond Evidence For / DARK SIGNALS Penalty / Net Score base structure)
- V-02 (Inertia-First Framing): 275/290 under v12 -- C-45 FAIL (hypothesis uses case-file
  framing; C-41 not satisfied, so C-45 precondition not met), C-46 FAIL (penalty column
  not observed with typed composite annotation; C-43 satisfied at baseline label-only level),
  C-47 FAIL (Net Score delta present per C-44; no independently verifiable declaration
  observed), C-48 PASS (deliberation table carries Inertia Cost column as 5th dimension,
  populated per candidate mode, orthogonal to evidence-for/against structure)

**R13 reference scores (all five variations score 290/290 under v12)**:
- V-01 (Severity Scale + Typed Fields): 315/345 -- passes C-49/C-50/C-52/C-54/C-59;
  fails C-51/C-53/C-55/C-56/C-57/C-58 (no SELECTION AUDIT phase; no Pipeline Debt axis)
- V-02 (Inertia-First + Selection Audit): 310/345 -- passes C-51/C-52/C-55/C-59;
  fails C-49/C-50/C-53/C-54/C-56/C-57/C-58 (no Severity Scale; Inertia Cost not Pipeline Debt)
- V-03 (Pipeline Debt + Arithmetic Trace): 310/345 -- passes C-52/C-56/C-58/C-59;
  fails C-49/C-50/C-51/C-53/C-54/C-55/C-57 (no Severity Scale; no SELECTION AUDIT)
- V-04 (Severity + Selection Audit combined): 330/345 -- passes C-49/C-50/C-51/C-52/C-53/
  C-54/C-55/C-59; fails C-56/C-57/C-58 (no Pipeline Debt axis)
- V-05 (all three axes unified): 345/345 -- passes all 11 new criteria; first ceiling output
  under v13; AMEND-A carries all four R13 signal types simultaneously (C-57)

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
| v10     | 2026-03-16 | Add C-38 through C-40 from R10 excellence signals: hypothesis declared in gate phase before repo scan (V-01+V-02 -- independently converged across role-sequenced and phase-named variants), DARK SIGNALS entries carry per-entry hypothesis relation (V-01 -- Hypothesis Relation: CONFIRMED/OVERTURNED/neutral), amend options carry hypothesis confirmation/overturn status (V-01 -- full lifecycle auditable from gate to amend); both V-01 and V-02 score 250/250 under v10; 40 criteria (5E/3R/32A), 250 pts |
| v11     | 2026-03-17 | Add C-41 through C-44 from R11 excellence signals: hypothesis structured as formal 3-field contract (V-01 -- PREDICTED-MODE/STRUCTURAL-PREDICTION/FALSIFICATION-SIGNAL triplet), IS-FALSIFICATION-SIGNAL typed field with 4-state vocabulary (V-01 -- YES-CONFIRMED/YES-OVERTURNED/NO-corroborates-alternative/NO-neutral), pivot deliberation as weight-scoring table with DARK SIGNALS Penalty column (V-02 -- structural citation enforcement; Net Score per mode), amend options carry deliberation Net Score delta (V-02 -- quantified score impact from table in amend recommendation); both V-01 and V-02 score 270/270 under v11; 44 criteria (5E/3R/36A), 270 pts |
| v12     | 2026-03-17 | Add C-45 through C-48 from R12 excellence signals: hypothesis contract fields carry machine-readable type annotations (V-01 -- typed annotations on all 3 contract fields make value domains explicit and machine-parseable), DARK SIGNALS Penalty column typed as composite [label:string, magnitude:0-4] (V-01 -- magnitude scale quantifies penalty severity, enabling weighted Net Score arithmetic), Net Score delta annotated as independently verifiable (V-01 -- inline "(independently verifiable)" closes the audit chain from deliberation table to amend option), deliberation table carries organizational cost dimension as 5th column (V-02 -- Inertia Cost column extends evidence table into strategic cost territory); V-01 scores 285/290; V-02 scores 275/290; both axes still orthogonal; 48 criteria (5E/3R/40A), 290 pts |
| v13     | 2026-03-17 | Add C-49 through C-59 from R13 excellence signals: Severity Scale declared at DARK SIGNALS header (V-01/V-04/V-05 -- named scale before entries makes entry magnitudes section-interpretable), per-entry Severity field with derivation note (V-01/V-04/V-05 -- first-class Severity annotation on each entry creates DARK SIGNALS -> Penalty -> Net Score traceability chain), dedicated SELECTION AUDIT phase after deliberation (V-02/V-04/V-05 -- named structural phase as stable citation target for AMEND-A), Net Score arithmetic trace as explicit computation (all five -- first R13 universal convergence; trace in ROLE 3 for V-01/V-03 or ROLE 3.5 for V-02/V-04/V-05), Severity traceability note in SELECTION AUDIT (V-04/V-05 -- provenance from DARK SIGNALS entries to Penalty magnitudes established within the audit phase), AMEND-A carries Severity magnitude traceability citation (V-01/V-04/V-05 -- names structural source of Penalty magnitudes), AMEND-A cites SELECTION AUDIT by structural name (V-02/V-04/V-05 -- audit phase becomes authoritative record), AMEND-A names Pipeline Debt stages for mode change (V-03/V-05 -- specific corps-* stage disruption in amend recommendation), AMEND-A carries all four R13 signal types simultaneously (V-05 only -- Severity + SELECTION AUDIT + Pipeline Debt + verifiable delta unified; first ceiling output under v13), YAML carries pipeline-debt header comment (V-03/V-05 -- cost signal embedded in the YAML artifact itself), bonus typed hypothesis contract fields beyond 3-field baseline (all five -- second R13 universal; CONFIDENCE + BASIS typed fields across all variations); R13 first round where all five score 290/290 under v12; V-05 achieves ceiling 345/345 under v13; 59 criteria (5E/3R/51A), 345 pts |
