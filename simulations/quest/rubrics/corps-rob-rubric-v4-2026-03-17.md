Here is the complete updated rubric as written.

---

**What changed in v4:**

Three new aspirational criteria extracted from R4 excellence signals:

| ID | Name | Pattern | Source |
|----|------|---------|--------|
| C-16 | Prior-Stage Lens Impact and Downstream Risk Shift Pair | `lens-impact-risk-shift-pair` | V-02 R4. Paired role-lens mechanisms: `Prior-Stage Lens Impact` in findings body asks "how does this role's orientation change the reading of a prior finding?" (source stage + F-ID + relationship type); `Downstream Risk Shift` in handoff packet asks "what failure mode or ownership gap becomes newly visible at this stage?" Both required for PASS; either alone is PARTIAL. |
| C-17 | Lens-Impact / Risk-Shift Anti-Copy Guard | `lens-impact-risk-shift-anti-copy-guard` | V-02 R4. Explicit negative constraint ("do not copy the lens impact into the risk shift") preventing the lens impact observation from being restated as the risk shift entry. Structural parallel to C-15. Scored N/A (= FAIL) when C-16 is absent. |
| C-18 | Explicit Lens Declaration Fill Field | `explicit-lens-declaration-fill-field` | V-04 R4, gap surfaced by V-01 R4 C-14 PARTIAL. V-01 has a "Lens filter rule" instruction but no dedicated output field; V-04 R4 has an explicit `Lens:` fill field naming the orientation dimension by practice domain (e.g., "TPM -- schedule risk + dependency gaps"). Distinct from C-14, which can satisfy its lens requirement through role title + filter instruction. |

**Scoring change:** N_aspirational goes from 7 to 10. Formula is unchanged in form: `(N_pass/10) * 10`. Each aspirational pass is now exactly 1 point (cleaner than 10/7 ≈ 1.4 pts).

**Re-grades:**
- V-02 R4: C-16 PASS, C-17 PASS, C-18 FAIL → 9/10 → **99**
- V-01 R4: C-16 FAIL, C-17 N/A→FAIL, C-18 FAIL → 6.5/10 → **96.5** (was 99.3 under v3)
- V-04 R3: C-16 FAIL, C-17 N/A→FAIL, C-18 FAIL → 7/10 → **97** (was 100 under v3; ceiling resets)

**Design note:** C-16 separates two distinct contributions that C-08 conflates: re-reading prior work through a role lens (lens impact) vs. surfacing net-new visibility at this stage's vantage point (risk shift). C-17 enforces the same discipline C-15 enforces for the original pair. C-18 gives V-01 R4's C-14 PARTIAL a precise diagnosis: the filter rule exists in the template but the declaration field is absent from the output.
 "TPM -- schedule risk + dependency gaps"). Distinct from C-14's briefing envelope, which can satisfy its lens requirement through the role title and filter rule. C-18 requires a labeled declaration field in the output itself. |

**Scoring change:** N_aspirational goes from 7 to 10. Formula is unchanged in form:
`(N_pass / 10) * 10`. Each full aspirational pass is now worth exactly 1 point (10/10),
up from 10/7 ≈ 1.4 pts.

**Re-grades:**
- V-02 R4: C-16 PASS, C-17 PASS, C-18 FAIL (no explicit Lens field) → 9/10 → **99**
- V-01 R4: C-16 FAIL, C-17 N/A→FAIL, C-18 FAIL → 6.5/10 → **96.5** (was 99.3 under v3)
- V-04 R3: C-16 FAIL, C-17 N/A→FAIL, C-18 FAIL → 7/10 → **97** (was 100 under v3; ceiling resets)

**Design note:** C-16 names the structural contribution V-02 adds beyond C-08 -- not just
"what did prior stages find?" but "how does this role's lens change how I read that?", and
"what does my stage make visible that was not visible before?" C-17 enforces the same
discipline C-15 enforces for the original mechanism pair. C-18 explains why V-01's
compressed Stage-Open Context earns only a PARTIAL on C-14 -- the filter rule exists but
the declaration output field does not.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-18 | (N_pass / 10) x 10 |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts, max = 10).

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

Aspirational score = (N_pass / 10) x 10 = N_pass.
Each full PASS = 1 point. PARTIAL = 0.5. Ceiling = 10.

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
  risk + stakeholder readiness," "interface coupling + system boundary integrity").
- **Pass condition**: Every stage section contains an explicit `Lens:` (or equivalently
  labeled) fill field appearing at stage open, before any numbered findings, that names
  the orientation dimension in terms specific to the role's practice domain. The field
  must declare a dimension -- role name alone does not satisfy this criterion. A 6-stage
  run requires 6 populated Lens fields.

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

---

## Example Score Calculations

**All essential pass, 2 of 3 recommended pass, 0 of 10 aspirational pass:**

```
composite = (5/5 * 60) + (2/3 * 30) + (0/10 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**All essential pass, 3/3 recommended pass, 3/10 aspirational pass:**

```
composite = (5/5 * 60) + (3/3 * 30) + (3/10 * 10)
          = 60 + 30 + 3
          = 93
```

**All essential pass, 3/3 recommended pass, 10/10 aspirational pass (ceiling):**

```
composite = (5/5 * 60) + (3/3 * 30) + (10/10 * 10)
          = 60 + 30 + 10
          = 100
```

**R4 top score under v4 (V-02: all C-16 + C-17 PASS, C-18 FAIL, C-15 status TBD):**

```
composite = (5/5 * 60) + (3/3 * 30) + (9/10 * 10)
          = 60 + 30 + 9
          = 99
```

**R4 V-01 re-graded under v4 (C-14 PARTIAL, C-16 FAIL, C-17 N/A->FAIL, C-18 FAIL):**

```
composite = (5/5 * 60) + (3/3 * 30) + (6.5/10 * 10)
          = 60 + 30 + 6.5
          = 96.5
```

V-01 drops from 99.3 (v3) because the three new criteria expose gaps that already existed
in V-01's compressed Stage-Open Context design. The drop is diagnostic, not punitive:
C-18 names exactly why V-01 earns only PARTIAL on C-14 (no Lens field in output).

**R3 V-04 re-graded under v4 (C-16 FAIL, C-17 N/A->FAIL, C-18 FAIL -- R3 predates both):**

```
composite = (5/5 * 60) + (3/3 * 30) + (7/10 * 10)
          = 60 + 30 + 7
          = 97
```

V-04 R3's ceiling resets from 100 to 97 -- the new criteria identify mechanisms V-04 R3
does not have. The ceiling is recoverable: a future variate that achieves all 10
aspirational criteria scores 100.

**Any essential failure = not golden regardless of composite.**
