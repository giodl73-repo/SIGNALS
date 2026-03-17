The prompt asked to "output the complete updated rubric as Markdown" -- here it is:

---

# corps-rob rubric v6 -- 2026-03-17

## Change Log

| Version | Change |
|---------|--------|
| v1 | C-01 -- C-08: essential (x5) + recommended (x3) |
| v2 | C-09 -- C-10: inter-stage blocker detection, cross-cutting theme elevation |
| v3 | C-11 -- C-12: handoff packet, stage-boundary blocker field |
| v4 | C-13 -- C-18: inertia anchor, briefing envelope, anti-redundancy, lens-impact/risk-shift pair + guard, explicit lens fill field |
| v5 | C-19 -- C-23: Stage 1 lens coverage, pre-envelope Part 0 block, KEY CONCERNS back-ref, three-hop chain, chain health summary. N_aspirational 10 -> 15. |
| v6 | C-24 -- C-26: fill-slot structural completeness, displacement map with D-IDs, table-first findings format. N_aspirational 15 -> 18. |

---

## New in v6 -- What was extracted from the R6 scorecard

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-24 | Finding Slot Structural Completeness | V-01 R6, V-04 R6, V-05 R6 | All finding slots (severity, owner, resolution) declared as mandatory `[fill]` fields. Converts C-04's 50% ownership floor into a per-finding structural guarantee: absent slot = format failure, not prose quality gap. |
| C-25 | Displacement Map with Labeled D-IDs | V-02 R6, V-04 R6, V-05 R6 | INERTIA ANCHOR contains a numbered displacement register (D-01, D-02 ...). When a stage's Inertia Stance is RESISTANT and a finding is HIGH severity, the finding must cite a D-ID from the register. Escalates C-13 from prose anchor to machine-scannable register with finding-level citations. N/A when C-13 absent. |
| C-26 | Table-First Findings Format with Inline Rejection Guards | V-03 R6, V-05 R6 | All stage findings rendered in a structured table with mandatory typed columns (ID, severity, artifact/concern, owner, resolution). Each column carries an inline rejection guard in the template. Converts C-04's prose-level quality check into a format-level check. |

**Scoring change:** N_aspirational 15 -> 18. Max contributable to composite still 10 (ceiling = 100). Raw count (max 18) is the tie-break.

**Re-grades under v6:**
- V-02 R5 (prior leader): C-24 FAIL, C-25 FAIL, C-26 FAIL -> 15 raw / 10 contributable -> **100** (ceiling; tie-break 15, unchanged from v5)
- V-01 R6 (fill-slot only): C-24 PASS, C-25 FAIL, C-26 FAIL -> 16 raw -> **100**; tie-break 16
- V-02 R6 (D-ID map only): C-24 FAIL, C-25 PASS, C-26 FAIL -> 16 raw -> **100**; tie-break 16
- V-03 R6 (table-first only): C-24 FAIL, C-25 FAIL, C-26 PASS -> 16 raw -> **100**; tie-break 16
- V-04 R6 (V-01 + V-02): C-24 PASS, C-25 PASS, C-26 FAIL -> 17 raw -> **100**; tie-break 17
- V-05 R6 (all three axes): C-24 PASS, C-25 PASS, C-26 PASS -> 18 raw -> **100**; tie-break 18 -- new leader

**Design note:** The three R6 axes are independent of each other and of the Part 0 architecture. All R6 variations preserve the Part 0 architecture (C-20 through C-23 PASS at base), so the tie-break delta is entirely attributable to the three new axes. V-05 R6's 18-raw ceiling reflects the full stack: Part 0 chain traceability (C-20--C-23) + fill-slot discipline (C-24) + displacement map with D-ID citations (C-25) + table-first format with inline rejection guards (C-26). Each axis addresses a distinct failure mode: C-24 prevents incomplete findings from passing format inspection; C-25 prevents inertia acknowledgment from being abstract (RESISTANT stance forces finding-level D-ID citation); C-26 prevents prose quality from being the only line of defense against weak findings. The GO/NO-GO signal in C-05 is explicitly exempted from table-first scope -- unambiguous labeled signals are degraded, not improved, by tabular rendering.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-26 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 18 (tie-break when composite = 100).

**Any essential failure = not golden regardless of composite.**

---

## Essential Criteria

*All five must pass for golden. Each is worth 12 points. PARTIAL = 6 pts.*

---

### C-01 -- Stage Attribution
- **Category**: format
- **Weight**: essential
- **Text**: Every stage in the output has an explicit, non-anonymous attribution to a canonical label (`leadership`, `teams`, `pm`, `tpm`, `arch-board`, `exec-office`). Each stage section is headed by both the stage name and the role conducting it. No stage is anonymous and no stage is silently merged with another.
- **Pass condition**: Every stage run has a section header containing the canonical stage name and the name or role title of the assigned persona. Labels must match the six canonical names exactly -- no substitutions or abbreviations.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the documented lens of the persona loaded from `.craft/roles/` via `org.yaml` -- not a generic review any role could have written. The role's orientation shapes which concerns are surfaced and how they are framed.
- **Pass condition**: At least one finding per stage is grounded in the loaded persona's specific lens (e.g., a TPM flags schedule risk and dependency gaps, a Principal Architect flags interface coupling, a PM flags adoption risk, a Chief of Staff flags mission alignment). Findings that are fully generic -- applicable by any reviewer to any topic -- do not satisfy this criterion for any stage in which they appear.

---

### C-03 -- ROB Document Format
- **Category**: format
- **Weight**: essential
- **Text**: Each stage document follows the ROB format: stage header, role identity, numbered findings with severity labels, and an explicit stage verdict. All four structural elements are required per stage.
- **Pass condition**: For each stage run, all four are present: (1) stage header with canonical name, (2) role identity statement, (3) at least one finding carrying a severity label (HIGH / MED / LOW or equivalent), (4) an explicit stage verdict using one of the four tokens: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED.

---

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least two concrete findings. Each finding names a specific concern -- not a category or domain name. Each finding carries an explicit or implied owner and a resolution path or next step.
- **Pass condition**: Total findings across all stages >= 2 * N_stages_run. Each finding references the specific artifact or topic under review, not just the problem domain. At least 50% of findings include an owner (role name) and a resolution action. "Needs attention" or "review required" alone does not constitute a resolution.

---

### C-05 -- TPM Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output contains an explicit go/no-go recommendation. The verdict is not implied, buried in prose, or deferred to a future stage -- it is a top-level labeled statement in the tpm section.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO / GO WITH CONDITIONS verdict as a labeled, top-level element (heading, bold label, or equivalent structural marker), accompanied by at least one sentence of rationale that cites a specific finding ID or risk ID.

---

## Recommended Criteria

*Output is better with these. Each adds material value. Each is worth 10 points. PARTIAL = 5 pts.*

---

### C-06 -- Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose narrative. Each entry carries a title, severity, likelihood, and mitigation. The register is machine-scannable and actionable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list with >= 3 entries. Each entry contains: title (specific risk name), severity (HIGH/MED/LOW), likelihood (HIGH/MED/LOW), and mitigation (concrete action). At least one risk is rated HIGH severity. Prose-only risk summaries do not satisfy this criterion.

---

### C-07 -- Exec-Office Mission Cascade
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the `exec-office` stage runs, output traces how at least one named S-office mission cascades down to the artifact under review. The mission must be named by title -- not paraphrased as "strategic priorities" or "company goals". Alignment or gap must be stated explicitly with a specific example.
- **Pass condition**: `exec-office` stage output names at least one S-office mission by its actual title and traces the path from that mission to the artifact with an explicit ALIGNED / PARTIAL / GAP verdict. Vague alignment claims ("supports our direction") do not pass. A Mission Cascade table with at least one populated row satisfies this.

---

### C-08 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings from earlier stages. The escalation chain (teams -> pm -> tpm) is visible in the output: a teams finding becomes a pm alignment issue, which becomes a tpm risk register entry.
- **Pass condition**: At least 2 cross-stage references appear in any multi-stage run. Each reference names the source stage, the source finding ID, and how the current stage confirms, escalates, or contradicts it (e.g., "teams F-02 escalated: pm confirms ownership still unresolved"). Forward-looking references ("future stages should watch X") do not count -- references must look backward.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

Aspirational score = N_pass (each full PASS = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10 (ceiling = 100). Raw count max = 18.
Tie-break between equal composites uses raw aspirational count.

---

### C-09 -- Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly surfaces when a finding in one stage creates a hard blocker for a downstream stage. Blockers are identified at the stage boundary where they arise, not discovered retroactively at a later stage.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run, specifying: the upstream stage that raised it, the blocking finding ID, the downstream stage it blocks, and the reason the downstream stage cannot proceed. A BLOCKER CHECK section or equivalent structural marker at the stage close satisfies this if populated with a concrete finding reference.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages independently, output recognizes the pattern and elevates it as a cross-cutting theme above individual stage findings. The theme names why repetition across stages increases severity beyond any single-stage instance.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level (in a Cross-Cutting Themes section or equivalent, not embedded inside a single stage), citing the 2+ stages that surfaced it and explaining the elevated severity. Copying one finding verbatim does not satisfy this -- the theme must characterize the pattern of recurrence.

---

### C-11 -- Handoff Packet at Stage Close
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `handoff-packet-at-stage-close`
- **Text**: Each stage (from Stage 2 onward in a multi-stage run) closes with a formal HANDOFF PACKET section that catalogs cross-stage references to prior findings. The handoff packet makes C-08 a process output rather than a model-recall artifact -- every stage is structurally forced to scan what came before.
- **Pass condition**: Each stage after the first contains a dedicated HANDOFF PACKET (or equivalent labeled section) at the stage close. Each packet lists at least one cross-stage reference entry giving: source stage name, source finding ID, and relationship type (confirms / escalates / contradicts). A 6-stage run must contain a minimum of 5 cross-stage entries distributed across all packets.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `stage-boundary-blocker-detection`
- **Text**: Each stage close contains a BLOCKER field (as part of the handoff packet or as a standalone structural marker). The field is populated at the stage boundary where the blocker arises -- not deferred to a later stage or collected retroactively in a document-level ledger.
- **Pass condition**: Each stage close contains a BLOCKER: YES / NO field (or equivalent labeled element). For every YES entry, the field names: the blocking finding ID, the downstream stage that is blocked, and the specific reason the downstream stage cannot proceed without resolution.

---

### C-13 -- Inertia Anchor and Per-Stage Inertia Check
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `inertia-anchor-per-stage-check`
- **Text**: The run opens with an INERTIA ANCHOR section that names what the topic displaces and who bears the cost of change. Each stage then opens with an INERTIA CHECK that forces the reviewing role to articulate the status-quo pressure from their own perspective before writing findings.
- **Pass condition**: Output contains an INERTIA ANCHOR (or equivalent labeled section) before Stage 1 that names at least one specific thing displaced by the topic and identifies the cost-bearer. At least 3 stage sections contain an INERTIA CHECK that frames the status-quo tension from the reviewing role's specific perspective -- not a generic "change is hard" statement.

---

### C-14 -- Stage-Open Briefing Envelope
- **Category**: structure
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-03 and V-04 pattern `stage-open-briefing-envelope`
- **Text**: Each stage (from Stage 2 onward) opens with a BRIEFING ENVELOPE section that distills what the current reviewing role should attend to from prior stages, filtered through their specific role lens. The envelope forces C-02 role-loading to operate on forwarded cross-stage context before any findings are written.
- **Pass condition**: Each stage after the first contains a BRIEFING ENVELOPE (or equivalent labeled section) at the stage open. Each envelope: (1) names the reviewing role's lens explicitly, (2) lists forwarded concerns selected as relevant from that role's perspective -- not a verbatim copy of prior findings, (3) carries an instruction that selection must be lens-directed. A 6-stage full run requires at least 5 envelopes.

---

### C-15 -- Anti-Redundancy Synthesis Constraint
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-04 pattern `anti-redundancy-synthesis-constraint`
- **Text**: When both a Cross-Stage References section (in the findings body) and a CROSS-STAGE SYNTHESIS section (in the handoff packet) appear in the same stage, an explicit anti-redundancy constraint prevents the synthesis from being a copy of the references.
- **Pass condition**: When C-08 and C-11 both pass in the same run, at least one stage contains an explicit anti-redundancy instruction or demonstrates non-redundant synthesis. Acceptable substance added by the synthesis includes: risk escalation beyond any single reference, naming of a pattern across multiple references, or a specific downstream action not stated in any individual reference.

---

### C-16 -- Prior-Stage Lens Impact and Downstream Risk Shift Pair
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-02 pattern `lens-impact-risk-shift-pair`
- **Text**: Cross-stage visibility operates through two paired role-lens mechanisms: (1) a `Prior-Stage Lens Impact` section in the findings body; and (2) a `Downstream Risk Shift` field in the handoff packet. Together they separate role-specific re-reading of prior work from net-new visibility surfaced by this stage's vantage point.
- **Pass condition**: Stages 2--6 each contain a `Prior-Stage Lens Impact` section with at least 1 entry naming source stage, F-ID, and relationship type. Each handoff packet contains a `Downstream Risk Shift` field with at least 1 entry naming a failure mode or ownership gap not previously named. **Both elements must be present for a PASS; either alone is a PARTIAL.**

---

### C-17 -- Lens-Impact / Risk-Shift Anti-Copy Guard
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-02 pattern `lens-impact-risk-shift-anti-copy-guard`
- **Text**: When both `Prior-Stage Lens Impact` and `Downstream Risk Shift` are present, an explicit negative constraint prevents the lens impact observation from being restated as the downstream risk shift entry.
- **Pass condition**: The handoff packet template or preamble before `Downstream Risk Shift` contains an explicit negative constraint preventing Prior-Stage Lens Impact content from being copied into Downstream Risk Shift. **Scored N/A (= FAIL for scoring) when C-16 is absent.**

---

### C-18 -- Explicit Lens Declaration Fill Field
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 excellence signal -- V-04 R4 pattern `explicit-lens-declaration-fill-field`
- **Text**: The stage-open output contains a dedicated, labeled fill field (e.g., `Lens: TPM -- schedule risk + dependency gaps`) that declares the reviewing role's orientation dimension in practice-domain terms before findings begin. Role name alone does not satisfy this criterion; the field must name the dimension being applied.
- **Pass condition**: Every stage section contains an explicit `Lens:` (or equivalently labeled) fill field appearing at stage open, before any numbered findings, that names the orientation dimension in terms specific to the role's practice domain. A 6-stage run requires 6 populated Lens fields.

---

### C-19 -- Lens Field Complete Stage Coverage
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-01 R5 pattern `lens-field-complete-stage-coverage`
- **Text**: C-18 requires a labeled Lens declaration field at every stage, but Stage 1 has no prior-stage briefing envelope -- the envelope mechanism only opens from Stage 2 onward. Without an explicit provision for Stage 1, a design placing `Lens:` inside the briefing envelope satisfies C-18 at stages 2-6 but silently omits Stage 1. C-19 closes this gap.
- **Pass condition**: Stage 1 section contains an explicit labeled Lens declaration (e.g., `Lens: [role] -- [dimension]` in Stage Identity, a LENS ACTIVATION Part 0 block, or equivalent) before Stage 1's first numbered finding. Combined with C-18's coverage of stages 2-6, the total Lens declaration count equals N_stages_run. **Scored N/A (= FAIL for scoring) when C-18 is absent.**

---

### C-20 -- Pre-Envelope Lens Activation Block
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `pre-envelope-lens-activation-block`
- **Text**: A dedicated labeled `LENS ACTIVATION` block appears as Part 0 at every stage, before the briefing envelope (Part 1) opens. The lens is declared before any prior-stage context is loaded, ensuring the role's orientation governs intake rather than being conditioned by the prior-stage picture. A design using Part 0 satisfies C-18, C-19, and C-20 together. C-20 is earned only when the block is structurally prior to the envelope (Part 0 position), not concurrent with or after it.
- **Pass condition**: Every stage section contains a `LENS ACTIVATION` (or equivalently labeled) block at the stage open, before the BRIEFING ENVELOPE section (Part 1). The block names the role's orientation dimension in practice-domain terms. Required at all stages including Stage 1. **PARTIAL = block present and populated at 4 or more stages but absent at 1-2 stages.**

---

### C-21 -- KEY CONCERNS Explicit Lens Back-Reference
- **Category**: depth
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `key-concerns-lens-back-reference`
- **Text**: The KEY CONCERNS field in the briefing envelope explicitly names the governing Part 0 LENS ACTIVATION declaration as the selection constraint. C-14 requires lens-directed selection but does not require a back-reference to the declaration artifact; C-21 requires the instruction text itself to cite the Part 0 block as governing.
- **Pass condition**: The KEY CONCERNS field in each briefing envelope contains explicit text naming the Part 0 declaration as the governing selection source. Required in each envelope at stages 2-6. A 6-stage full run requires 5 KEY CONCERNS back-references. **Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

### C-22 -- Three-Hop Lens Chain Mechanical Traceability
- **Category**: depth
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `three-hop-lens-chain-traceability`
- **Text**: The chain Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact is mechanically traceable in the output text at two hops: (1) KEY CONCERNS names Part 0 as its governing source (C-21), and (2) the `Prior-Stage Lens Impact` subsection explicitly references "the role's orientation declared in Part 0." C-22 requires both forward hops to carry the explicit back-reference, converting the three-part chain from a design claim into a verifiable output property.
- **Pass condition**: At every stage with a Prior-Stage Lens Impact section, that section contains explicit text naming the Part 0 declaration as the governing lens. Combined with C-21's requirement, the full chain Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact is traceable via explicit text. **PARTIAL = one of the two hops present but the other absent. Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

### C-23 -- ROB Summary Lens Activation Chain Health Field
- **Category**: structure
- **Weight**: aspirational
- **Source**: R5 excellence signal -- V-02 R5 pattern `rob-summary-lens-activation-chain-health`
- **Text**: The ROB Summary section includes a named `LENS ACTIVATION CHAIN HEALTH` field that assesses the integrity of the Part 0 -> KEY CONCERNS -> Prior-Stage Lens Impact chain across all stages. The field identifies per-stage chain status (COMPLETE / PARTIAL / BROKEN), making chain integrity a first-class output artifact.
- **Pass condition**: The ROB Summary contains a labeled `LENS ACTIVATION CHAIN HEALTH` entry (or equivalent). The field reports per-stage chain status across all N_stages_run stages. **PARTIAL = field present but lacking per-stage breakdown (overall health statement only). Scored N/A (= FAIL for scoring) when C-20 is absent.**

---

### C-24 -- Finding Slot Structural Completeness
- **Category**: structure
- **Weight**: aspirational
- **Source**: R6 excellence signal -- V-01 R6, V-04 R6, V-05 R6 pattern `finding-slot-structural-completeness`
- **Text**: All three mandatory finding slots (severity label, owner role, resolution action) are declared as explicit `[fill]` fields in the template, making their absence a format failure rather than a prose quality gap. C-04 requires >= 50% of findings to carry owner and resolution action; C-24 escalates that floor to a per-finding structural guarantee: every finding in every stage has all three slots, and the template makes omission detectable by inspection. The template need not use literal `[fill]` notation -- any slot mechanism that makes absence detectable satisfies this (e.g., a required table column, a labeled dash-prefixed line). The owner slot must name a role, not a team or "TBD"; the resolution slot must name an action, not "needs attention."
- **Pass condition**: Every finding entry in the output contains explicit slots for severity, owner (role name), and resolution (concrete action). The template or table structure makes all three slots mandatory. At least the resolution slot carries an explicit inline rejection instruction (e.g., `[fill. "Needs attention" does not satisfy this slot]` or equivalent column guard). A 6-stage run with 2 findings per stage requires 12 fully populated finding triples. **PARTIAL = all three slots present in template but at least one stage has a finding with an omitted or visibly unfilled slot.**

---

### C-25 -- Displacement Map with Labeled D-IDs
- **Category**: depth
- **Weight**: aspirational
- **Source**: R6 excellence signal -- V-02 R6, V-04 R6, V-05 R6 pattern `displacement-map-labeled-d-ids`
- **Text**: The INERTIA ANCHOR section (C-13) is elevated from a prose statement of displacement to a numbered displacement register: each displaced entity receives a D-ID label (D-01, D-02, ...), names what is displaced, and identifies the cost-bearer. The register makes displacement machine-scannable and creates a citation target for findings. The activation rule: when a stage's Inertia Stance is RESISTANT and a finding is rated HIGH severity, the finding must reference at least one D-ID from the register as an inertia-contributing factor. Stages with Inertia Stance NEUTRAL or ADAPTIVE do not trigger the citation requirement.
- **Pass condition**: The INERTIA ANCHOR contains a displacement register with at least 2 D-ID-labeled entries, each naming a displaced entity and a cost-bearer. In any stage whose Inertia Stance is RESISTANT and that contains at least one HIGH-severity finding, the HIGH finding includes a D-ID reference. **PARTIAL = displacement register present with D-IDs but no RESISTANT+HIGH stage occurs in the run (citation requirement not triggered), OR register present but a RESISTANT+HIGH finding omits the D-ID citation. Scored N/A (= FAIL for scoring) when C-13 is absent.**

---

### C-26 -- Table-First Findings Format with Inline Rejection Guards
- **Category**: structure
- **Weight**: aspirational
- **Source**: R6 excellence signal -- V-03 R6, V-05 R6 pattern `table-first-findings-format-inline-rejection-guards`
- **Text**: All stage findings are rendered in a structured table rather than a numbered prose list. The table contains mandatory typed columns: finding ID, severity (HIGH/MED/LOW), specific artifact or concern, owner (role), and resolution (concrete action). Each quality-bearing column carries an inline rejection guard that specifies what does NOT satisfy the column (e.g., `Resolution (concrete action -- "Needs attention" does not satisfy this column)`). The table format converts C-04 from a prose quality check into a format check, enabling a scorer to verify compliance structurally. The go/no-go verdict in C-05 is explicitly exempted from table-first scope: unambiguous labeled signals are degraded, not improved, by tabular rendering, and the GO/NO-GO signal must remain a top-level bold labeled element.
- **Pass condition**: Every stage produces findings as a table (not a prose list) with at minimum five columns: ID, severity, artifact/concern, owner, resolution. At least the resolution column contains an inline rejection guard naming what does not satisfy the column. Minimum 2 populated rows per stage. The TPM GO/NO-GO signal remains a top-level bold labeled element and is not subsumed into the findings table. **PARTIAL = table present and populated but missing one mandatory column type, or rejection guard absent from all columns.**

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
| C-24 | Finding slot structural completeness               | aspirational  | structure   |
| C-25 | Displacement map with labeled D-IDs                | aspirational  | depth       |
| C-26 | Table-first findings format with inline guards     | aspirational  | structure   |

---

## N/A Dependency Chain

| Criterion | Scored N/A (= FAIL) when |
|-----------|--------------------------|
| C-17 | C-16 absent |
| C-19 | C-18 absent |
| C-21 | C-20 absent |
| C-22 | C-20 absent |
| C-23 | C-20 absent |
| C-25 | C-13 absent |

---

## Example Score Calculations

**All essential pass, 2 of 3 recommended pass, 0 of 18 aspirational pass:**
```
composite = (5/5 x 60) + (2/3 x 30) + 0 = 80
```
Golden threshold met (all essential pass, composite = 80).

**All essential pass, 3/3 recommended pass, 3/18 aspirational pass:**
```
composite = 60 + 30 + 3 = 93
```

**All essential pass, 3/3 recommended pass, 10+ aspirational pass (ceiling):**
```
composite = 60 + 30 + 10 = 100
```
Any raw aspirational count >= 10 produces composite = 100. Raw count (max 18) is the tie-break.

**V-02 R4 re-graded under v6 (C-19 FAIL, C-20--C-26 FAIL/N/A):**
```
raw aspirational = 9   (C-09 through C-17 pass, C-18 fail)
composite        = 99  (unchanged from v4/v5)
```

**V-01 R5 under v6 (C-09--C-19 PASS, C-20--C-26 FAIL/N/A):**
```
raw aspirational = 11; contributable = 10 (ceiling)
composite        = 100
```

**V-02 R5 under v6 (C-09--C-23 all PASS, C-24--C-26 FAIL):**
```
raw aspirational = 15; contributable = 10 (ceiling)
composite        = 100; tie-break 15  (unchanged from v5 leader)
```

**V-01 R6 / V-02 R6 / V-03 R6 (each one new axis):**
```
raw aspirational = 16; composite = 100; tie-break 16
```

**V-04 R6 (two axes):**
```
raw aspirational = 17; composite = 100; tie-break 17
```

**V-05 R6 (all three axes):**
```
raw aspirational = 18 (all 18 pass); composite = 100; tie-break 18 -- new leader
```

The three R6 axes are independent and additive: each adds exactly 1 raw point. V-05 R6 leads with 18/18 raw, reflecting the full stack.

**Any essential failure = not golden regardless of composite.**

---

**Summary of what's new in v6:**

- **C-24** converts C-04's percentage floor into a per-finding structural guarantee via `[fill]` slots -- absent owner or resolution becomes a detectable format failure.
- **C-25** converts C-13's prose inertia anchor into a machine-scannable D-ID register with an activation rule: RESISTANT+HIGH findings must cite a D-ID, forcing role-loading (C-02) and inertia awareness (C-13) to jointly satisfy the highest-risk findings.
- **C-26** converts C-04's prose quality check into a format check via mandatory table columns with inline rejection guards -- and explicitly carves out the GO/NO-GO signal from table-first scope, preserving C-05's labeled signal integrity.
