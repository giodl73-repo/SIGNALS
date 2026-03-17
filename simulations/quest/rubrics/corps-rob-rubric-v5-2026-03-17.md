Written to `simulations/quest/rubrics/corps-rob-rubric-v5-2026-03-17.md`.

---

**What was extracted from the R5 scorecard:**

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-19 | Lens Field Complete Stage Coverage | V-01 R5 | Stage 1 has no briefing envelope; C-18 silently omits it. V-01 fills the gap with a standalone `Lens:` in Stage Identity. N/A when C-18 absent. |
| C-20 | Pre-Envelope Lens Activation Block | V-02 R5 | `LENS ACTIVATION` as Part 0, before the envelope opens -- declaration precedes all context loading. Distinct from C-18 (inside envelope = post-context). |
| C-21 | KEY CONCERNS Explicit Lens Back-Reference | V-02 R5 | KEY CONCERNS field explicitly names Part 0 as the governing filter ("selected through the Lens declared in Part 0"). Converts C-14's implicit orientation into a stated mechanical constraint. N/A when C-20 absent. |
| C-22 | Three-Hop Lens Chain Mechanical Traceability | V-02 R5 | Both hops of Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact carry explicit back-references in the output text. C-16 requires the pair; C-22 requires the chain citations. N/A when C-20 absent. |
| C-23 | ROB Summary Lens Activation Chain Health Field | V-02 R5 | ROB Summary carries a named `LENS ACTIVATION CHAIN HEALTH` field with per-stage chain status. Makes chain integrity a first-class artifact. N/A when C-20 absent. |

**Scoring change:** N_aspirational 10 -> 15. Max contributable to composite still 10 (ceiling = 100). Raw count (max 15) is the new tie-break.

**Key re-grade insight:** Both V-01 R5 (11 raw) and V-02 R5 (15 raw) composite at 100. The raw margin (15 vs 11) quantifies that V-02's Part 0 architecture is structurally richer -- C-20 through C-23 are only reachable via pre-envelope positioning.
e Lens declared in Part 0"). C-14 requires lens-directed selection but does not require a back-reference to the declaration artifact; C-21 requires the instruction text itself to cite the Part 0 block as governing, converting implicit lens influence into a mechanically stated constraint. Scored N/A (= FAIL) when C-20 is absent. |
| C-22 | Three-Hop Lens Chain Mechanical Traceability | `three-hop-lens-chain-traceability` | V-02 R5. The chain Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact is mechanically traceable in the output text at two hops: (1) KEY CONCERNS names Part 0 as its governing source (C-21), and (2) the `Prior-Stage Lens Impact` subsection explicitly references "the role's orientation declared in Part 0." C-16 requires the pair without requiring chain back-references; C-22 requires both forward hops to carry the explicit reference. PARTIAL = one of the two hops present but the other absent. Scored N/A (= FAIL) when C-20 is absent. |
| C-23 | ROB Summary Lens Activation Chain Health Field | `rob-summary-lens-activation-chain-health` | V-02 R5. The ROB Summary includes a named `LENS ACTIVATION CHAIN HEALTH` field assessing the Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact chain integrity across all stages, identifying per-stage chain status (COMPLETE / PARTIAL / BROKEN). Without this field, chain health is visible only to a scorer reading each stage individually. PARTIAL = field present but lacking per-stage breakdown. Scored N/A (= FAIL) when C-20 is absent. |

**Scoring change:** N_aspirational goes from 10 to 15. Max aspirational contribution to
composite is still 10 (ceiling = 100; essential 60 + recommended 30 = 90 baseline).
Raw aspirational count (max 15) serves as a tie-break between equal composites.

**Re-grades under v5:**
- V-01 R5: C-18 PASS, C-19 PASS, C-20 FAIL, C-21 N/A->FAIL, C-22 N/A->FAIL, C-23 N/A->FAIL
  -> 11 raw / 10 contributable -> **100** (ceiling; same as v4 score)
- V-02 R5: C-18 PASS (Part 0 block satisfies labeled declaration before findings),
  C-19 PASS (Part 0 covers Stage 1), C-20 PASS, C-21 PASS, C-22 PASS, C-23 PASS
  -> 15 raw / 10 contributable -> **100** (ceiling; 15 raw vs V-01 R5's 11 raw)
- V-02 R4 (prior top score): C-19 FAIL, C-20 FAIL, C-21--C-23 N/A->FAIL
  -> 9 raw / 9 contributable -> **99** (unchanged from v4)

**Design note:** C-19 closes the Stage 1 gap C-18 leaves open: the briefing envelope only
opens from Stage 2 onward, so placing `Lens:` inside the envelope silently omits Stage 1.
V-01 R5 fills this gap via a standalone Lens: in the Stage Identity; the V-02 R5 Part 0
mechanism fills it automatically via the pre-envelope block at every stage. C-20 is the
structural escalation: instead of declaring the lens inside (C-18) or alongside (C-19) the
envelope, Part 0 precedes the envelope entirely. C-21 enforces that KEY CONCERNS names
Part 0 as its governing source; C-22 enforces that the three-hop chain is cited in both
output directions (not just claimed by the template); C-23 makes chain health a first-class
ROB Summary artifact rather than a property only visible to a stage-by-stage scorer.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-23 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 15 (tie-break when composite = 100).

**Any essential failure = not golden regardless of composite.**

---

## Essential Criteria

*All five must pass for golden. Each is worth 12 points. PARTIAL = 6 pts.*

---

### C-01 -- Stage Attribution
- **Category**: format
- **Weight**: essential
- **Text**: Every stage in the output has an explicit, non-anonymous attribution to a
  canonical label (`leadership`, `teams`, `pm`, `tpm`, `arch-board`, `exec-office`). Each
  stage section is headed by both the stage name and the role conducting it. No stage is
  anonymous and no stage is silently merged with another.
- **Pass condition**: Every stage run has a section header containing the canonical stage
  name and the name or role title of the assigned persona. Labels must match the six
  canonical names exactly -- no substitutions or abbreviations.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the documented lens of the persona loaded from
  `.craft/roles/` via `org.yaml` -- not a generic review any role could have written.
  The role's orientation shapes which concerns are surfaced and how they are framed.
- **Pass condition**: At least one finding per stage is grounded in the loaded persona's
  specific lens (e.g., a TPM flags schedule risk and dependency gaps, a Principal Architect
  flags interface coupling, a PM flags adoption risk, a Chief of Staff flags mission
  alignment). Findings that are fully generic -- applicable by any reviewer to any topic --
  do not satisfy this criterion for any stage in which they appear.

---

### C-03 -- ROB Document Format
- **Category**: format
- **Weight**: essential
- **Text**: Each stage document follows the ROB format: stage header, role identity,
  numbered findings with severity labels, and an explicit stage verdict. All four structural
  elements are required per stage.
- **Pass condition**: For each stage run, all four are present: (1) stage header with
  canonical name, (2) role identity statement, (3) at least one finding carrying a severity
  label (HIGH / MED / LOW or equivalent), (4) an explicit stage verdict using one of the
  four tokens: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED.

---

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least two concrete findings. Each finding names a
  specific concern -- not a category or domain name. Each finding carries an explicit or
  implied owner and a resolution path or next step.
- **Pass condition**: Total findings across all stages >= 2 * N_stages_run. Each finding
  references the specific artifact or topic under review, not just the problem domain.
  At least 50% of findings include an owner (role name) and a resolution action. "Needs
  attention" or "review required" alone does not constitute a resolution.

---

### C-05 -- TPM Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output contains an
  explicit go/no-go recommendation. The verdict is not implied, buried in prose, or
  deferred to a future stage -- it is a top-level labeled statement in the tpm section.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled, top-level element (heading, bold label, or
  equivalent structural marker), accompanied by at least one sentence of rationale that
  cites a specific finding ID or risk ID.

---

## Recommended Criteria

*Output is better with these. Each adds material value. Each is worth 10 points. PARTIAL = 5 pts.*

---

### C-06 -- Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose narrative.
  Each entry carries a title, severity, likelihood, and mitigation. The register is
  machine-scannable and actionable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list with
  >= 3 entries. Each entry contains: title (specific risk name), severity (HIGH/MED/LOW),
  likelihood (HIGH/MED/LOW), and mitigation (concrete action). At least one risk is rated
  HIGH severity. Prose-only risk summaries do not satisfy this criterion.

---

### C-07 -- Exec-Office Mission Cascade
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the `exec-office` stage runs, output traces how at least one named
  S-office mission cascades down to the artifact under review. The mission must be named
  by title -- not paraphrased as "strategic priorities" or "company goals". Alignment or
  gap must be stated explicitly with a specific example.
- **Pass condition**: `exec-office` stage output names at least one S-office mission by
  its actual title and traces the path from that mission to the artifact with an explicit
  ALIGNED / PARTIAL / GAP verdict. Vague alignment claims ("supports our direction")
  do not pass. A Mission Cascade table with at least one populated row satisfies this.

---

### C-08 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings from
  earlier stages. The escalation chain (teams -> pm -> tpm) is visible in the output:
  a teams finding becomes a pm alignment issue, which becomes a tpm risk register entry.
- **Pass condition**: At least 2 cross-stage references appear in any multi-stage run.
  Each reference names the source stage, the source finding ID, and how the current stage
  confirms, escalates, or contradicts it (e.g., "teams F-02 escalated: pm confirms
  ownership still unresolved"). Forward-looking references ("future stages should watch X")
  do not count -- references must look backward.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

Aspirational score = N_pass (each full PASS = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10 (ceiling = 100). Raw count max = 15.
Tie-break between equal composites uses raw aspirational count.

---

### C-09 -- Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly surfaces when a finding in one stage creates a hard blocker
  for a downstream stage. Blockers are identified at the stage boundary where they arise,
  not discovered retroactively at a later stage.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run,
  specifying: the upstream stage that raised it, the blocking finding ID, the downstream
  stage it blocks, and the reason the downstream stage cannot proceed (e.g., "teams F-03
  blocks tpm go/no-go: data ownership unresolved, risk register cannot be finalized").
  A BLOCKER CHECK section or equivalent structural marker at the stage close satisfies
  this if populated with a concrete finding reference.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages independently, output
  recognizes the pattern and elevates it as a cross-cutting theme above individual stage
  findings. The theme names why repetition across stages increases severity beyond any
  single-stage instance.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level (in a
  Cross-Cutting Themes section or equivalent, not embedded inside a single stage), citing
  the 2+ stages that surfaced it and explaining the elevated severity. Copying one finding
  verbatim from one stage and labeling it a theme does not satisfy this -- the theme must
  characterize the pattern of recurrence.

---

### C-11 -- Handoff Packet at Stage Close
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `handoff-packet-at-stage-close`
- **Text**: Each stage (from Stage 2 onward in a multi-stage run) closes with a formal
  HANDOFF PACKET section that catalogs cross-stage references to prior findings. The
  handoff packet makes C-08 (cross-stage coherence) a process output rather than a
  model-recall artifact -- every stage is structurally forced to scan what came before.
  In a 6-stage full run this produces a minimum of 5 structured cross-stage entries.
- **Pass condition**: Each stage after the first contains a dedicated HANDOFF PACKET (or
  equivalent labeled section) at the stage close. Each packet lists at least one
  cross-stage reference entry giving: source stage name, source finding ID, and
  relationship type (confirms / escalates / contradicts). A 6-stage run must contain a
  minimum of 5 cross-stage entries distributed across all packets.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `stage-boundary-blocker-detection`
- **Text**: Each stage close contains a BLOCKER field (as part of the handoff packet or
  as a standalone structural marker). The field is populated at the stage boundary where
  the blocker arises -- not deferred to a later stage or collected retroactively in a
  document-level ledger. A post-hoc escalation ledger at the document end does not satisfy
  this criterion because it cannot detect blockers before the downstream stage runs.
- **Pass condition**: Each stage close contains a BLOCKER: YES / NO field (or equivalent
  labeled element). For every YES entry, the field names: the blocking finding ID, the
  downstream stage that is blocked, and the specific reason the downstream stage cannot
  proceed without resolution. A BLOCKER: NO entry is acceptable and still satisfies the
  structural requirement for that stage.

---

### C-13 -- Inertia Anchor and Per-Stage Inertia Check
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `inertia-anchor-per-stage-check`
- **Text**: The run opens with an INERTIA ANCHOR section that names what the topic
  displaces and who bears the cost of change. Each stage then opens with an INERTIA CHECK
  that forces the reviewing role to articulate the status-quo pressure from their own
  perspective before writing findings. This mechanism grounds C-02 (role-loaded
  perspective) in concrete inertia context rather than relying on the model to infer it.
- **Pass condition**: Output contains an INERTIA ANCHOR (or equivalent labeled section)
  before Stage 1 that names at least one specific thing displaced by the topic and
  identifies the cost-bearer (team, system, or process). At least 3 stage sections contain
  an INERTIA CHECK (or equivalent labeled step) that frames the status-quo tension from
  the reviewing role's specific perspective -- not a generic "change is hard" statement.

---

### C-14 -- Stage-Open Briefing Envelope
- **Category**: structure
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-03 and V-04 pattern `stage-open-briefing-envelope`
- **Text**: Each stage (from Stage 2 onward) opens with a BRIEFING ENVELOPE section that
  distills what the current reviewing role should attend to from prior stages, filtered
  through their specific role lens. The envelope forces C-02 role-loading to operate on
  forwarded cross-stage context before any findings are written -- the role does not just
  receive prior findings verbatim, it selects which ones are relevant from its own
  perspective. In a 6-stage full run this produces 5 lens-filtered distillations. Without
  this mechanism, C-08 cross-stage coherence is structurally enforced only at the close
  (via handoff packet) but not at the open, leaving a gap where the reviewing role begins
  writing findings without first scanning what came before through its lens.
- **Pass condition**: Each stage after the first contains a BRIEFING ENVELOPE (or
  equivalent labeled section) at the stage open. Each envelope: (1) names the reviewing
  role's lens explicitly, (2) lists forwarded concerns selected as relevant from that
  role's perspective -- not a verbatim copy of prior findings but a role-filtered
  selection, (3) carries an instruction (explicit or demonstrated) that selection must be
  lens-directed. A "Must be lens-directed" instruction in the template satisfies the
  structural requirement if the output demonstrates genuine selection. A 6-stage full run
  requires at least 5 envelopes; a 3-stage run requires at least 2.

---

### C-15 -- Anti-Redundancy Synthesis Constraint
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-04 pattern `anti-redundancy-synthesis-constraint`
- **Text**: When both a Cross-Stage References section (in the findings body) and a
  CROSS-STAGE SYNTHESIS section (in the handoff packet) appear in the same stage, an
  explicit anti-redundancy constraint prevents the synthesis from being a copy of the
  references. The two coherence mechanisms serve different purposes: the references section
  surfaces backward citations as they become relevant to individual findings; the synthesis
  section at the close names the downstream significance of the collected cross-stage
  picture. Without a constraint, the synthesis collapses into a restatement of the
  references, eliminating the value added by the second mechanism.
- **Pass condition**: When C-08 and C-11 both pass in the same run, at least one stage
  contains an explicit anti-redundancy instruction or demonstrates non-redundant synthesis.
  "Must add substance not already stated in the Cross-Stage References section above" or
  equivalent satisfies the structural requirement. A handoff synthesis that mirrors the
  wording of the corresponding cross-stage references section does not satisfy this
  criterion even if both sections are present. Acceptable substance added by the synthesis
  includes: risk escalation beyond any single reference, naming of a pattern across
  multiple references, or a specific downstream action not stated in any individual
  reference.

---

### C-16 -- Prior-Stage Lens Impact and Downstream Risk Shift Pair
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-02 pattern `lens-impact-risk-shift-pair`
- **Text**: Cross-stage visibility operates through two paired role-lens mechanisms:
  (1) a `Prior-Stage Lens Impact` section in the findings body that asks "how does this
  role's orientation change the reading of a prior finding?" -- naming source stage, F-ID,
  and relationship type (confirms / escalates / reframes); and (2) a `Downstream Risk
  Shift` field in the handoff packet that asks "what failure mode or ownership gap becomes
  newly visible at this stage?" -- naming the stage and risk shift type. Together they
  separate two distinct contributions: role-specific re-reading of prior work (lens impact)
  vs. net-new visibility surfaced by this stage's vantage point (risk shift). This pair
  extends C-08 beyond backward citation into active role-lens transformation. A prompt
  that has this pair satisfies C-08 through a more rigorous mechanism; a prompt that has
  C-08 without this pair does not satisfy C-16.
- **Pass condition**: Stages 2--6 each contain a `Prior-Stage Lens Impact` section (or
  equivalently named section) in the findings body with at least 1 entry naming source
  stage, F-ID, and relationship type. Each handoff packet contains a `Downstream Risk
  Shift` field (or equivalently named field) with at least 1 entry naming a failure mode
  or ownership gap not previously named in prior stages' packets. **Both elements must be
  present for a PASS; either alone is a PARTIAL.**

---

### C-17 -- Lens-Impact / Risk-Shift Anti-Copy Guard
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-02 pattern `lens-impact-risk-shift-anti-copy-guard`
- **Text**: When both `Prior-Stage Lens Impact` (findings body) and `Downstream Risk
  Shift` (handoff packet) are present, an explicit negative constraint prevents the lens
  impact observation from being restated as the downstream risk shift entry. The risk shift
  names what becomes newly visible at this stage; the lens impact names how prior work
  reads differently through this role's lens. They are complementary questions, not
  paraphrases of each other. Without a constraint, the two fields collapse into
  paraphrase pairs, defeating the purpose of separating them. This criterion is the
  structural parallel to C-15 (which guards the original C-08 mechanism pair); it applies
  the same discipline to the C-16 mechanism pair.
- **Pass condition**: The handoff packet template or a preamble before the `Downstream
  Risk Shift` field contains an explicit negative constraint preventing Prior-Stage Lens
  Impact content from being copied into Downstream Risk Shift (e.g., "do not copy the
  lens impact into the risk shift -- the risk shift names what becomes visible at this
  stage, not what was reread from prior stages"). **Scored N/A (= FAIL for scoring) when
  C-16 is absent.**

---

### C-18 -- Explicit Lens Declaration Fill Field
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-04 R4 pattern `explicit-lens-declaration-fill-field`;
  gap identified via V-01 R4 C-14 PARTIAL
- **Text**: The stage-open output contains a dedicated, labeled fill field (e.g.,
  `Lens: TPM -- schedule risk + dependency gaps`) that declares the reviewing role's
  orientation dimension in practice-domain terms before findings begin. This is distinct
  from C-14's briefing envelope, which can satisfy its lens requirement through the role
  title in the header and a filter rule instruction. C-18 requires the lens to appear as
  a named output field with a substantive domain declaration in the generated artifact
  itself -- not just in the template instructions. A prompt that names only the role
  title (e.g., "Reviewing as: TPM") does not satisfy this criterion; the field must name
  the dimension being applied (e.g., "schedule risk + dependency management," "adoption
  risk + stakeholder readiness," "interface coupling + system boundary integrity"). The
  field may appear inside the briefing envelope, in a pre-envelope Part 0 block, or in
  the Stage Identity section -- position does not disqualify the field as long as it is
  labeled and appears before numbered findings.
- **Pass condition**: Every stage section contains an explicit `Lens:` (or equivalently
  labeled) fill field appearing at stage open, before any numbered findings, that names
  the orientation dimension in terms specific to the role's practice domain. The field
  must declare a dimension -- role name alone does not satisfy this criterion. A 6-stage
  run requires 6 populated Lens fields.

---

### C-19 -- Lens Field Complete Stage Coverage
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-01 R5 pattern `lens-field-complete-stage-coverage`
- **Text**: C-18 requires a labeled Lens declaration field at every stage, but Stage 1 has
  no prior-stage briefing envelope -- the envelope mechanism only opens from Stage 2
  onward. Without an explicit provision for Stage 1, a design placing `Lens:` inside the
  briefing envelope satisfies C-18 at stages 2-6 but silently omits Stage 1. C-19 closes
  this gap: Stage 1 must contain a dedicated labeled Lens field (in its Stage Identity
  section, a pre-envelope Part 0 block, or equivalent) regardless of whether a briefing
  envelope is present. The count of Lens declaration instances in the output must equal
  N_stages_run. A design using the C-20 pre-envelope Part 0 LENS ACTIVATION block at all
  stages also satisfies C-19 at Stage 1 via that block.
- **Pass condition**: Stage 1 section contains an explicit labeled Lens declaration
  (e.g., `Lens: [role] -- [dimension]` in Stage Identity, a LENS ACTIVATION Part 0 block,
  or equivalent) before Stage 1's first numbered finding. Combined with C-18's coverage of
  stages 2-6, the total Lens declaration count equals N_stages_run.
  **Scored N/A (= FAIL for scoring) when C-18 is absent.**

---

### C-20 -- Pre-Envelope Lens Activation Block
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `pre-envelope-lens-activation-block`
- **Text**: A dedicated labeled `LENS ACTIVATION` block appears as Part 0 at every stage,
  before the briefing envelope (Part 1) opens. The lens is declared before any prior-stage
  context is loaded, ensuring the role's orientation governs intake rather than being
  conditioned by the prior-stage picture. Structurally distinct from C-18 (Lens: field
  inside the envelope or Stage Identity, which is post-context-loading at stages 2+) and
  from C-19 (Stage 1 coverage within an envelope/identity approach): Part 0 precedes all
  context at every stage. The block names the orientation dimension in practice-domain
  terms (same standard as C-18). A design using Part 0 satisfies C-18 (the Part 0 block
  is a labeled Lens declaration field before findings), C-19 (Stage 1 covered via its own
  Part 0 block), and C-20 together. C-20 is earned only when the block is structurally
  prior to the envelope (Part 0 position), not concurrent with or after it.
- **Pass condition**: Every stage section contains a `LENS ACTIVATION` (or equivalently
  labeled) block at the stage open, before the BRIEFING ENVELOPE section (Part 1). The
  block names the role's orientation dimension in practice-domain terms. Required at all
  stages including Stage 1.
  **PARTIAL = block present and populated at 4 or more stages but absent at 1-2 stages.**

---

### C-21 -- KEY CONCERNS Explicit Lens Back-Reference
- **Category**: depth
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `key-concerns-lens-back-reference`
- **Text**: The KEY CONCERNS field in the briefing envelope explicitly names the governing
  Part 0 LENS ACTIVATION declaration as the selection constraint -- for example, "concerns
  selected through the Lens declared in Part 0" or "KEY CONCERNS filtered by the Part 0
  Lens declaration." C-14 requires lens-directed selection but does not require a
  back-reference to the declaration artifact; C-21 requires the instruction text itself
  to cite the Part 0 block as governing, converting implicit lens influence into a
  mechanically stated constraint. Without this back-reference, even when a Part 0 block
  exists, the chain between declaration and selection is asserted by proximity rather than
  by explicit instruction.
- **Pass condition**: The KEY CONCERNS field in each briefing envelope contains explicit
  text naming the Part 0 declaration as the governing selection source (e.g., "through the
  Lens declared in Part 0," "per the Part 0 Lens," or equivalent). Required in each
  envelope at stages 2-6. A 6-stage full run requires 5 KEY CONCERNS back-references.
  **Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

### C-22 -- Three-Hop Lens Chain Mechanical Traceability
- **Category**: depth
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `three-hop-lens-chain-traceability`
- **Text**: The chain Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact is mechanically
  traceable in the output text at two hops: (1) KEY CONCERNS names Part 0 as its governing
  source (C-21), and (2) the `Prior-Stage Lens Impact` subsection explicitly references
  "the role's orientation declared in Part 0" (or equivalent), naming the Part 0 block as
  the lens governing how prior findings are re-read. C-16 requires the Prior-Stage Lens
  Impact + Downstream Risk Shift pair without requiring either to reference Part 0 by
  name; C-22 requires both forward hops to carry the explicit back-reference, converting
  the three-part chain from a design claim into a verifiable output property: a scorer can
  confirm the chain without reading the prompt template.
- **Pass condition**: At every stage with a Prior-Stage Lens Impact section, that section
  contains explicit text naming the Part 0 declaration as the governing lens (e.g.,
  "orientation declared in Part 0," "the Part 0 Lens," or equivalent). Combined with
  C-21's requirement that KEY CONCERNS names Part 0, the full chain Part 0 -> KEY CONCERNS
  -> Prior-Stage Lens Impact is traceable via explicit text.
  **PARTIAL = one of the two hops (KEY CONCERNS reference or Lens Impact reference)
  present but the other absent.**
  **Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

### C-23 -- ROB Summary Lens Activation Chain Health Field
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `rob-summary-lens-activation-chain-health`
- **Text**: The ROB Summary section (or equivalent final synthesis section) includes a
  named `LENS ACTIVATION CHAIN HEALTH` field (or equivalently labeled field) that assesses
  the integrity of the Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact chain across all
  stages of the run. The field identifies per-stage chain status (COMPLETE / PARTIAL /
  BROKEN) and names any stage where the chain is broken or partial. Without this field,
  chain health is visible only to a scorer reading each stage individually; this field
  makes chain integrity a first-class output artifact in the summary.
- **Pass condition**: The ROB Summary contains a labeled `LENS ACTIVATION CHAIN HEALTH`
  entry (or equivalent). The field reports per-stage chain status across all N_stages_run
  stages.
  **PARTIAL = field present but lacking per-stage breakdown (overall health statement only).**
  **Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

## Criterion Summary

| ID   | Text (short)                                       | Weight        | Category    |
|------|----------------------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling                        | essential     | format      |
| C-02 | Role-loaded perspective                            | essential     | correctness |
| C-03 | ROB document format compliance                     | essential     | format      |
| C-04 | Actionable findings (2x per stage)                 | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage                     | essential     | correctness |
| C-06 | Risk register structure in tpm                     | recommended   | depth       |
| C-07 | Exec-office mission cascade                        | recommended   | coverage    |
| C-08 | Cross-stage coherence (2+ refs)                    | recommended   | depth       |
| C-09 | Inter-stage blocker detection                      | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation                      | aspirational  | depth       |
| C-11 | Handoff packet at stage close                      | aspirational  | structure   |
| C-12 | Stage-boundary blocker field                       | aspirational  | structure   |
| C-13 | Inertia anchor and per-stage check                 | aspirational  | depth       |
| C-14 | Stage-open briefing envelope                       | aspirational  | structure   |
| C-15 | Anti-redundancy synthesis constraint               | aspirational  | depth       |
| C-16 | Prior-stage lens impact + downstream risk shift    | aspirational  | depth       |
| C-17 | Lens-impact / risk-shift anti-copy guard           | aspirational  | depth       |
| C-18 | Explicit lens declaration fill field               | aspirational  | depth       |
| C-19 | Lens field complete stage coverage                 | aspirational  | structure   |
| C-20 | Pre-envelope lens activation block                 | aspirational  | structure   |
| C-21 | KEY CONCERNS explicit lens back-reference          | aspirational  | depth       |
| C-22 | Three-hop lens chain mechanical traceability       | aspirational  | depth       |
| C-23 | ROB Summary lens activation chain health field     | aspirational  | structure   |

---

## N/A Dependency Chain

| Criterion | Scored N/A (= FAIL) when |
|-----------|--------------------------|
| C-17 | C-16 absent |
| C-19 | C-18 absent |
| C-21 | C-20 absent |
| C-22 | C-20 absent |
| C-23 | C-20 absent |

---

## Example Score Calculations

**All essential pass, 2 of 3 recommended pass, 0 of 15 aspirational pass:**

```
composite = (5/5 x 60) + (2/3 x 30) + 0
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**All essential pass, 3/3 recommended pass, 3/15 aspirational pass:**

```
composite = (5/5 x 60) + (3/3 x 30) + 3
          = 60 + 30 + 3
          = 93
```

**All essential pass, 3/3 recommended pass, 10+ aspirational pass (ceiling):**

```
composite = (5/5 x 60) + (3/3 x 30) + 10
          = 60 + 30 + 10
          = 100
```

Any raw aspirational count >= 10 produces composite = 100.
Raw count (max 15) is the tie-break between equal composites.

**V-02 R4 re-graded under v5 (C-19 FAIL, C-20--C-23 FAIL/N/A):**

```
raw aspirational = 9   (C-09 through C-17 pass, C-18 fail)
composite        = 60 + 30 + 9 = 99    (unchanged from v4)
```

**V-01 R5 under v5 (C-09--C-18 all PASS, C-19 PASS, C-20--C-23 FAIL/N/A):**

```
raw aspirational = 11  (C-09 through C-19 pass)
contributable    = 10  (ceiling)
composite        = 60 + 30 + 10 = 100
```

**V-02 R5 under v5 (C-09--C-23 all PASS via Part 0 architecture):**

```
raw aspirational = 15  (all 15 pass)
contributable    = 10  (ceiling)
composite        = 60 + 30 + 10 = 100
tie-break margin: 15 raw vs V-01 R5's 11 raw
```

V-01 R5 and V-02 R5 both composite at 100. V-02 R5 leads on raw aspirational count (15
vs 11), reflecting that its pre-envelope Part 0 architecture unlocks four additional
criteria (C-20 through C-23) that the envelope-position architecture of V-01 R5 does not
reach.

**Any essential failure = not golden regardless of composite.**
