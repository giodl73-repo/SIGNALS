---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v11
round: R12
date: 2026-03-15
axes_explored: phrasing-register-descriptive, inertia-framing-status-quo-first, output-format-requirements-prose-list, role-sequence-strategy-first, inertia-framing+strategy-first-combined
---

# Quest Variate — `draft-spec` — Round 12 (Rubric v11)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Phrasing register — all role-phase instructions converted to descriptive/declarative form (REQUIRES/PRODUCES/BLOCKS keywords, no imperative actor→action→output directives) | None | C-27 (imperative phrasing) FAILS; all other 34 criteria pass; composite ≈ 172/175; isolates whether C-27 is the only criterion sensitive to phrasing register |
| V-02 | Inertia framing — [STATUS-QUO-SNAPSHOT] block added as first operation in Phase 2; each IG-ID explicitly references its seeding SQ-ID; status-quo competitor named before inertia hypotheses are declared | None | All 35 criteria pass; composite 175/175; status-quo-first framing may surface new patterns in [INERTIA-ANALYZED] certification scope |
| V-03 | Output format — Phase 3 Requirements section uses a numbered prose list instead of a table; C-13 (per-row P0 status COLUMN) requires a table; this isolates whether the requirements section format affects only C-13 or adjacent criteria | None | C-13 FAILS; all other 34 criteria pass; composite ≈ 172/175 |
| V-04 | Role sequence + lifecycle emphasis — Phase 0.5 STRATEGY SCOPING added between SETUP and PM PRE-ASSIGNMENT; Strategy produces [STRATEGY-SCOPE-SEAL] gating Phase 1; phase headers expanded with explicit role-owner labels | Role sequence, lifecycle emphasis | All 35 criteria pass; C-28 (PM structurally ordered before inertia) remains PASS since PM still precedes inertia; composite 175/175 |
| V-05 | V-02 + V-04 combined — [STATUS-QUO-SNAPSHOT] inertia framing AND Phase 0.5 Strategy pre-phase; all R11 V-05 structural elements preserved (C-33, C-34, C-35, ordinal markers, imperative phrasing) | Status-quo framing, strategy-first role sequence, all R11 criteria | Target 175/175; tests whether both structural additions compose without conflict; likely surfaces new patterns at gate-token certification scope |

---

## V-01 — Axis: Phrasing Register (Descriptive/Declarative)

**Primary axis**: Phrasing register — all `**PM: scan [source] → fill [target]**` imperative directives replaced with descriptive form (`**The PM should scan [source] and fill [target]**`). REQUIRES/PRODUCES/BLOCKS structural headers preserved. CASCADE TO annotations preserved. Gate tokens and table structures unchanged. No `→` arrows binding actor-action-output in role-phase instructions.
**Hypothesis**: C-27 (imperative phrasing register) FAILS because instructions use descriptive "should" form rather than concise imperative voice binding actor, action, and output in a single directive. C-20 (unified role-and-source declaration) passes via REQUIRES/PRODUCES keyword bindings per C-20's note: "the axis-complementarity pattern (combining role-sequence ordering with field-level REQUIRES bindings) is the canonical implementation." All other 34 criteria pass.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter:
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v11
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP — Architect =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present
BLOCKS: all subsequent phases

### [SCOUT-STATUS-TABLE]

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

---

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**B-1: Feasibility artifact loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend with B-2 or B-3 copy; emit the matching block verbatim.

**B-2: Compliance artifact loaded, feasibility NOT FOUND**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec using the compliance posture I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend with B-1 or B-3 copy; emit the matching block verbatim.

**B-3: Both feasibility and compliance loaded**

VERBATIM RESPONSE:
> I have feasibility and compliance signals for this topic but no requirements artifact. I can write a spec using both signals, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend with B-1 or B-2 copy; emit the matching block verbatim.

**B-catch: Any other combination**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**Anti-blend instruction**: Do not blend sub-condition copy; identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

The PM should inspect `scout-requirements` and assign each P0 requirement to a named spec section before any Architect prose is written. The PM should also name any conflicting requirement pairs found after scanning all P0 rows, rather than confirming absence by default without review.

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute for this dedicated typed column.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. A behavioral note about waivers does not satisfy — the propagation is a named structural obligation declared here in Phase 1 and verified in [INERTIA-ANALYZED] Condition 2.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

The cross-namespace signal should also appear at location 2 of 2 in the Purpose section pre-printed row.

---

Contradiction scan: the PM should inspect all P0 rows in `scout-requirements` before confirming absence. Name any conflicting R-ID pairs (e.g., "R-06 vs R-10") or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, and includes the Waiver Status column.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When Risk Signal = AMPLIFIED, use the pre-printed sub-slot format below. When C-03 WAIVER applies, mark the cell `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [describe existing alternative or status-quo] | R-ID: R-XX (from [PM-COVERAGE-TABLE]) — [why this requirement closes the gap; if AMPLIFIED, use sub-slot format above] | STANDARD / AMPLIFIED [cite trigger] |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | [add if applicable] | | | |

---

### [ID-REGISTER] — Inertia Decision Register

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named constraint or open question, if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [IG-REGISTER] is present and all rows are populated. A cell containing only a functional description without a named "R-XX" reference fails Condition 2. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural waiver propagation rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [IG-REGISTER] and [ID-REGISTER] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2) AND all AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified).
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

The Architect should receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. The Architect should not re-enumerate.

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [name source artifact and signal from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

The PM should scan [PM-COVERAGE-TABLE] and fill each pre-assigned row below before the Architect writes prose.

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it.

Architect: name at least one design element per P0 requirement assigned here. If a P0 requirement has no corresponding design element after writing, flag it as a gap in the findings section.

---

### 4. Constraints

List non-negotiable implementation constraints. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, include a named constraint or open question traceable to that IG-ID.

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

List unresolved issues that block or risk the spec. For each open question, name the deciding role and the information needed to resolve it.

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, both gate tokens previously emitted, cross-namespace signal present at both locations when applicable.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

Amendment list (produce after Phase 3):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]
... (minimum 2 items required)

===== END PHASE 4 =====

---

## ===== FINDINGS =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to their requirement priority.
Open question register: all OQ-IDs from Phase 3.

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Self-review scan list: the Architect should verify each of the following before emitting FINDINGS:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 and Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule)
- Waiver chain closed: Waiver Status → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order

===== END FINDINGS =====

---

---

## V-02 — Axis: Inertia Framing (Status-Quo-First)

**Primary axis**: Inertia framing — [STATUS-QUO-SNAPSHOT] structural block added as the first operation in Phase 2, before [IG-REGISTER]. The snapshot names the top alternatives that make this feature avoidable; each alternative seeds one IG-ID. Inertia hypotheses are derived from the snapshot rather than enumerated independently. All R11 V-05 structural elements preserved.
**Hypothesis**: All 35 criteria pass; composite 175/175. The [STATUS-QUO-SNAPSHOT] block does not add new gate tokens (it is a sub-block within Phase 2, not an independent phase), so C-17/C-21 are unaffected. The snapshot's SQ-ID references in [IG-REGISTER] may satisfy C-14's active inspection guard at a higher specificity level. Potential new pattern: snapshot-to-hypothesis traceability as a structural depth criterion.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter:
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v11
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP — Architect =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present
BLOCKS: all subsequent phases

### [SCOUT-STATUS-TABLE]

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

---

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**B-1: Feasibility artifact loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend sub-condition copy; emit the matching block verbatim.

**B-2: Compliance artifact loaded, feasibility NOT FOUND**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec using the compliance posture I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-3: Both feasibility and compliance loaded**

VERBATIM RESPONSE:
> I have feasibility and compliance signals for this topic but no requirements artifact. I can write a spec using both signals, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-catch: Any other combination**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**Anti-blend instruction**: Do not blend sub-condition copy; identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 requirement to a named spec section → fill [PM-COVERAGE-TABLE] below → emit [PM-CONTRACT-SEAL]**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths; SQ-ID references seed hypothesis statements) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` or `C-03 WAIVER`. Named structural element; prose note or row-level annotation in another column does not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells. A behavioral note does not satisfy — this is a named structural obligation verified in [INERTIA-ANALYZED] Condition 2.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row carries `C-03 WAIVER` in the Waiver Status column.

---

Cross-namespace signal (location 1 of 2):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: **PM: inspect all P0 rows in `scout-requirements` → name conflicting R-ID pairs before confirming absence.** Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"
PRODUCES: [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

---

### [STATUS-QUO-SNAPSHOT]

**PM: name the top alternatives that could make this feature unnecessary — minimum 2. Each alternative seeds one IG-ID in [IG-REGISTER] below.**

| SQ-ID | Status-Quo Alternative | Why It Falls Short | Seeds IG-ID |
|-------|----------------------|-------------------|-------------|
| SQ-01 | [name the existing tool, workflow, or approach this feature displaces] | [one-sentence gap that the alternative cannot close] | IG-01 |
| SQ-02 | [name the second alternative] | [one-sentence gap] | IG-02 |
| SQ-03 | [add if applicable] | | IG-03 |

**Snapshot validity rule**: [STATUS-QUO-SNAPSHOT] is structurally required before [IG-REGISTER]. Each SQ-ID must have a named alternative, a gap statement, and a seeding IG-ID. A row with a named alternative but a blank gap statement is a structural fail. [IG-REGISTER] IG-IDs that do not reference a SQ-ID remain valid — the snapshot seeds hypotheses but does not constrain the full IG-REGISTER set.

---

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Each IG-ID seeded from [STATUS-QUO-SNAPSHOT] must reference its SQ-ID. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When Risk Signal = AMPLIFIED, use the pre-printed sub-slot format below. When C-03 WAIVER applies, mark the cell `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | SQ-ID (if seeded) | Elimination Path | Risk Signal |
|-------|------------------|--------------------|------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [from SQ-01: why the status-quo alternative falls short] | SQ-01 | R-ID: R-XX — [reason; if AMPLIFIED, use sub-slot format] | STANDARD / AMPLIFIED [cite trigger] |
| IG-02 | [role] | [from SQ-02] | SQ-02 | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | [add if applicable] | [seeded or independent] | [SQ-XX or —] | | |

---

### [ID-REGISTER] — Inertia Decision Register

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named constraint or open question, if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

---

> **[INERTIA-ANALYZED]**
>
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [STATUS-QUO-SNAPSHOT] present with minimum 2 SQ-IDs (Condition 1 extension), [IG-REGISTER] and [ID-REGISTER] present (Condition 1), every non-waived Elimination Path cell contains a named R-ID (Condition 2), all AMPLIFIED rows carry both sub-slots populated.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate.**

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [name source artifact and signal from Phase 1 location 1 of 2, or "none loaded"] |

State what this feature does in 2–4 sentences. Name the primary user, core workflow, and business value.

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row below before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

Architect: write the requirements narrative using the pre-assigned rows above.

---

### 3. Design

Detail the solution design. For each P0 requirement assigned to this section, include a named design element that satisfies it.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five sections present in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present.
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

1. [Specific actionable amendment]
2. [Second specific actionable amendment]
... (minimum 2 items)

===== END PHASE 4 =====

---

## ===== FINDINGS =====

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Self-review scan list: Architect verifies: [PM-CONTRACT-SEAL] with Waiver Status column, [STATUS-QUO-SNAPSHOT] with minimum 2 SQ-IDs, [INERTIA-ANALYZED] Conditions 1 + 2, cross-namespace signal at both locations, all AMPLIFIED sub-slots populated, waiver chain closed, all five sections in order.

===== END FINDINGS =====

---

---

## V-03 — Axis: Output Format (Phase 3 Requirements Section — Prose List)

**Primary axis**: Output format — the Phase 3 Requirements section replaces its pre-assigned table with a numbered prose list. Each P0 requirement appears as a numbered item with inline status annotation. All other V-05 structural elements preserved (tables in all other phases, gate tokens, VERBATIM blocks, ordinal markers).
**Hypothesis**: C-13 (per-row P0 status COLUMN in requirements table) FAILS because C-13 requires "a table with a per-row Status or Spec Entry column"; a numbered prose list does not provide a table with a column. All other 34 criteria pass. Composite ≈ 172/175. Isolates whether C-13 is the only criterion sensitive to requirements section format.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter:
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v11
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP — Architect =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present
BLOCKS: all subsequent phases

### [SCOUT-STATUS-TABLE]

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided.

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**B-1: Feasibility only**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-2: Compliance only**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-3: Both feasibility and compliance**

VERBATIM RESPONSE:
> I have feasibility and compliance signals but no requirements artifact. P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-catch**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **Anti-blend instruction**: Do not blend sub-condition copy; emit the matching block verbatim.

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 requirement to a named spec section → fill [PM-COVERAGE-TABLE] → emit [PM-CONTRACT-SEAL]**

CASCADE TO: [IG-REGISTER] Phase 2 AND Purpose cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [section] | [name] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |

**Waiver Status column**: enumerated `COVERED` / `C-03 WAIVER`. Named structural element.

**Waiver propagation rule (structural)**: `C-03 WAIVER` entries generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells.

Cross-namespace signal (location 1 of 2):

| Field | Value |
|-------|-------|
| Source artifact | [name or "none loaded"] |
| Signal | [1 sentence] |
| Spec impact | [1 sentence] |

Contradiction scan: **PM: inspect all P0 rows before confirming absence.** Name conflicting R-ID pairs (e.g., "R-06 vs R-10") or state "none found after scanning R-01 through R-{n}."

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without Waiver Status column as a named structural element.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL]
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER]

**AMPLIFIED Elimination Path sub-slot format**:
```
Risk: [feasibility constraint or compliance gap]
R-ID: [R-XX from [PM-COVERAGE-TABLE]]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. "Risk:" populated with "R-ID:" blank is a structural fail, not a content gap. Reverse is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [role] | [hypothesis] | R-ID: R-XX — [reason; AMPLIFIED → sub-slot format] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [hypothesis] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |

### [ID-REGISTER]

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named item if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

> **[INERTIA-ANALYZED]**
>
> **Condition 1:** INVALID IF [IG-REGISTER] or [ID-REGISTER] absent or any IG-ID row unpopulated.
> **Condition 2:** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: "R-ID WAIVED" cells exempt.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path → Condition 2 exemption above. All three nodes named in sequence.
>
> [INERTIA-ANALYZED] certifies: Condition 1 AND Condition 2 AND all AMPLIFIED rows carry both sub-slots populated.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] and fill pre-assigned entries. Do not re-enumerate.**

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → confirm pre-assigned entries match below before Architect writes prose.**

P0 coverage confirmed: {n}/{n}.

Numbered list of assigned requirements (one item per P0 row from [PM-COVERAGE-TABLE]):

1. **R-01** — [Requirement text] — Assigned to: [section name] — Spec Entry: [entry name] — Status: ASSIGNED
2. **R-02** — [Requirement text] — Assigned to: [section name] — Spec Entry: [entry name] — Status: ASSIGNED
3. ... (one item per P0 row)

Architect: write the requirements narrative referencing the numbered list above.

---

### 3. Design

Detail the solution design. For each P0 requirement assigned to this section, include a named design element.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID |
|---------------|-------------|--------|-------|
| CON-01 | [constraint] | [source] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [role] | [what's needed] |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five sections present in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present.
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

1. [Specific actionable amendment]
2. [Second specific actionable amendment]

===== END PHASE 4 =====

---

## ===== FINDINGS =====

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | | | |

===== END FINDINGS =====

---

---

## V-04 — Axis: Role Sequence + Lifecycle Emphasis (Strategy-First Phase 0.5)

**Primary axis**: Role sequence — Phase 0.5 STRATEGY SCOPING added between Phase 0 (SETUP) and Phase 1 (PM PRE-ASSIGNMENT). Strategy reviews [SCOUT-STATUS-TABLE], identifies the primary risk dimension, and produces [STRATEGY-SCOPE-SEAL] gating Phase 1. Lifecycle emphasis: each phase header carries an explicit role-owner label.
**Hypothesis**: All 35 criteria pass; composite 175/175. C-28 (PM pre-assignment structurally ordered before inertia) remains PASS — PM pre-assignment (Phase 1) still precedes inertia analysis (Phase 2). The Strategy pre-phase produces an additional gate token before PM, but does not break the PM-first-ordering-relative-to-inertia requirement. C-12 (role annotations inline) gains an additional Strategy role annotation in Phase 0.5 and Phase 3 cross-check. Potential new pattern: multi-gate phase ordering with distinct role handoffs as a structural depth criterion.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter:
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v11
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP — Architect =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present
BLOCKS: Phase 0.5 REQUIRES [SCOUT-STATUS-TABLE]

### [SCOUT-STATUS-TABLE]

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided.

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**B-1: Feasibility only**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints, but P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-2: Compliance only**

VERBATIM RESPONSE:
> I have a compliance signal but no requirements artifact. P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-3: Both**

VERBATIM RESPONSE:
> I have feasibility and compliance signals but no requirements artifact. P0 coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **B-catch**

VERBATIM RESPONSE:
> I have some scout signals but no requirements artifact. P0 coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. **Anti-blend instruction**: Identify the matching branch and emit its block verbatim.

### Normal branch — proceed to Phase 0.5.

===== END PHASE 0 =====

---

## ===== PHASE 0.5: STRATEGY SCOPING — Strategy =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [STRATEGY-SCOPE-TABLE], [STRATEGY-SCOPE-SEAL]
EXIT CONDITION: [STRATEGY-SCOPE-SEAL] present
BLOCKS: Phase 1 REQUIRES [STRATEGY-SCOPE-SEAL]

**Strategy: scan [SCOUT-STATUS-TABLE] → identify primary risk dimension → record scope decision → emit [STRATEGY-SCOPE-SEAL]**

### [STRATEGY-SCOPE-TABLE]

| Field | Value |
|-------|-------|
| Primary risk dimension | [feasibility / compliance / market / stakeholder / "none identified"] |
| Risk signal source | [artifact name, or "NOT LOADED"] |
| Scope decision | IN SCOPE / OUT OF SCOPE |
| Scope rationale | [1 sentence — if OUT OF SCOPE, state the reason and halt] |
| Risk amplification forecast | AMPLIFIED LIKELY / STANDARD EXPECTED [based on available signals] |

If Scope decision = OUT OF SCOPE: halt and state reason. Do not proceed to Phase 1.

---

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STRATEGY-SCOPE-TABLE] present with Scope decision and Risk amplification forecast populated.
>
> [STRATEGY-SCOPE-SEAL] is a proof-of-work artifact. Its presence certifies [STRATEGY-SCOPE-TABLE] is present and non-empty with Scope decision = IN SCOPE.
> Phase 1 is blocked until [STRATEGY-SCOPE-SEAL] appears here.

===== END PHASE 0.5 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [STRATEGY-SCOPE-SEAL] from Phase 0.5 — if absent, halt and state "[STRATEGY-SCOPE-SEAL] missing — complete Phase 0.5 before proceeding"
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 requirement to a named spec section → fill [PM-COVERAGE-TABLE] → emit [PM-CONTRACT-SEAL]**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs) AND Purpose cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [section] | [name] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |

**Waiver Status column**: enumerated `COVERED` / `C-03 WAIVER`. Named structural element.

**Waiver propagation rule (structural)**: `C-03 WAIVER` entries generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells.

Cross-namespace signal (location 1 of 2):

| Field | Value |
|-------|-------|
| Source artifact | [name or "none loaded"] |
| Signal | [1 sentence] |
| Spec impact | [1 sentence] |

Contradiction scan: **PM: inspect all P0 rows before confirming absence.** Name conflicting R-ID pairs or state "none found after scanning R-01 through R-{n}."

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without Waiver Status column as named structural element.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking. Cross-reference [STRATEGY-SCOPE-TABLE] Risk amplification forecast.

### [IG-REGISTER]

**AMPLIFIED sub-slot format**:
```
Risk: [feasibility constraint or compliance gap]
R-ID: [R-XX from [PM-COVERAGE-TABLE]]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. "Risk:" populated with "R-ID:" blank is a structural fail. Reverse is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [role] | [hypothesis] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [hypothesis] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |

### [ID-REGISTER]

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [item if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

> **[INERTIA-ANALYZED]**
>
> **Condition 1:** INVALID IF [IG-REGISTER] or [ID-REGISTER] absent or any row unpopulated.
> **Condition 2:** INVALID IF any Elimination Path cell lacks a named R-ID. "R-ID WAIVED" cells exempt.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER in Waiver Status column → "R-ID WAIVED" cell marker in [IG-REGISTER] → Condition 2 exemption above. All three nodes named in sequence.
>
> [INERTIA-ANALYZED] certifies: Condition 1 AND Condition 2 AND all AMPLIFIED rows carry both sub-slots populated.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Strategy cross-check: flag any spec decision that conflicts with [STRATEGY-SCOPE-TABLE] risk dimension. Do not re-enumerate requirements.**

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [from Phase 1 location 1 of 2, or "none loaded"] |
| Strategy risk alignment | [cite [STRATEGY-SCOPE-TABLE] risk dimension or "no conflict"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row below before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

---

### 3. Design

Detail the solution design. For each P0 requirement assigned to this section, include a named design element.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID |
|---------------|-------------|--------|-------|
| CON-01 | [constraint] | [source] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five sections present in order, or before [STRATEGY-SCOPE-SEAL], [PM-CONTRACT-SEAL], and [INERTIA-ANALYZED] all present.
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

1. [Specific actionable amendment]
2. [Second specific actionable amendment]

===== END PHASE 4 =====

---

## ===== FINDINGS =====

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | | | |

Self-review: [STRATEGY-SCOPE-SEAL] present, [PM-CONTRACT-SEAL] with Waiver Status column, [INERTIA-ANALYZED] Conditions 1 + 2, cross-namespace signal at both locations, AMPLIFIED sub-slots populated, waiver chain closed, all five sections in order.

===== END FINDINGS =====

---

---

## V-05 — Full Combination: V-02 (Status-Quo Inertia Framing) + V-04 (Strategy-First Role Sequence)

**Primary axis**: V-02 [STATUS-QUO-SNAPSHOT] inertia framing combined with V-04 Phase 0.5 STRATEGY SCOPING. All R11 V-05 structural elements preserved. Imperative phrasing maintained throughout (C-27). Ordinal location markers on all multi-occurrence elements (C-19). Split [IG-REGISTER]/[ID-REGISTER] with Responsible Role column (C-22, C-23). Full Branch B sub-conditionals with anti-blend (C-26).
**Hypothesis**: All 35 criteria pass; composite 175/175. [STATUS-QUO-SNAPSHOT] and [STRATEGY-SCOPE-SEAL] compose without conflict — Strategy identifies the risk dimension that the snapshot makes concrete, and IG-IDs reference both SQ-IDs and pre-assigned R-IDs. [INERTIA-ANALYZED] certification scope expanded to cover both new blocks. Likely surfaces new pattern: multi-source traceability in [IG-REGISTER] (SQ-ID + R-ID + Strategy risk dimension as three independent mandatory references per amplified row).

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter:
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v11
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP — Architect =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present
BLOCKS: Phase 0.5 REQUIRES [SCOUT-STATUS-TABLE]

### [SCOUT-STATUS-TABLE]

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

---

### Fallback Branch A (location 1 of 2) — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B (location 1 of 2) — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**B-1: Feasibility only**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints, but P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT. Do not blend sub-condition copy; emit matching block verbatim.

**B-2: Compliance only**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. P0 requirement coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT.

**B-3: Both feasibility and compliance**

VERBATIM RESPONSE:
> I have feasibility and compliance signals but no requirements artifact. P0 coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT.

**B-catch: Any other combination**

VERBATIM RESPONSE:
> I have some scout signals but no requirements artifact. P0 coverage will be waived. Should I proceed, or run `scout:requirements` first?

HALT.

**Anti-blend instruction**: Do not blend sub-condition copy; identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — proceed to Phase 0.5.

===== END PHASE 0 =====

---

## ===== PHASE 0.5: STRATEGY SCOPING — Strategy =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [STRATEGY-SCOPE-TABLE], [STRATEGY-SCOPE-SEAL]
EXIT CONDITION: [STRATEGY-SCOPE-SEAL] present
BLOCKS: Phase 1 REQUIRES [STRATEGY-SCOPE-SEAL]

**Strategy: scan [SCOUT-STATUS-TABLE] → identify primary risk dimension → record scope decision and risk amplification forecast → emit [STRATEGY-SCOPE-SEAL]**

CASCADE TO: [STATUS-QUO-SNAPSHOT] Phase 2 (risk dimension seeds snapshot framing) AND Phase 3 Purpose row (strategy risk alignment field)

### [STRATEGY-SCOPE-TABLE]

| Field | Value |
|-------|-------|
| Primary risk dimension | [feasibility / compliance / market / stakeholder / "none identified"] |
| Risk signal source | [artifact name, or "NOT LOADED"] |
| Scope decision | IN SCOPE / OUT OF SCOPE |
| Scope rationale | [1 sentence] |
| Risk amplification forecast | AMPLIFIED LIKELY / STANDARD EXPECTED |

If Scope decision = OUT OF SCOPE: halt and state reason. Do not proceed to Phase 1.

---

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STRATEGY-SCOPE-TABLE] present with Scope decision, Risk signal source, and Risk amplification forecast populated.
>
> [STRATEGY-SCOPE-SEAL] is a proof-of-work artifact. Its presence certifies [STRATEGY-SCOPE-TABLE] is present, non-empty, and records Scope decision = IN SCOPE.
> Phase 1 is blocked until [STRATEGY-SCOPE-SEAL] appears here.

===== END PHASE 0.5 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [STRATEGY-SCOPE-SEAL] from Phase 0.5 — if absent, halt and state "[STRATEGY-SCOPE-SEAL] missing — complete Phase 0.5 before proceeding"
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 requirement to a named spec section → fill [PM-COVERAGE-TABLE] → emit [PM-CONTRACT-SEAL]**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated `COVERED` / `C-03 WAIVER`. This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note or row-level annotation in another column does not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. A behavioral note does not satisfy — this is a named structural obligation declared here in Phase 1 and verified in [INERTIA-ANALYZED] Condition 2.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row carries `C-03 WAIVER`.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: **PM: inspect all P0 rows in `scout-requirements` → name conflicting R-ID pairs before confirming absence.** Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without Waiver Status column as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, and includes the Waiver Status column.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt
PRODUCES: [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]
- Strategy risk forecast (from [STRATEGY-SCOPE-TABLE]): [AMPLIFIED LIKELY / STANDARD EXPECTED]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking OR Strategy forecast = AMPLIFIED LIKELY.

---

### [STATUS-QUO-SNAPSHOT]

**PM: name the top alternatives that could make this feature unnecessary — minimum 2. Each alternative seeds one IG-ID. Cross-reference [STRATEGY-SCOPE-TABLE] primary risk dimension when naming the gap.**

| SQ-ID | Status-Quo Alternative | Why It Falls Short | Risk Dimension (from [STRATEGY-SCOPE-TABLE]) | Seeds IG-ID |
|-------|----------------------|-------------------|--------------------------------------------|-------------|
| SQ-01 | [name the existing tool, workflow, or approach] | [gap — name the dimension from Strategy scope] | [feasibility / compliance / market / stakeholder / n/a] | IG-01 |
| SQ-02 | [second alternative] | [gap] | [dimension] | IG-02 |
| SQ-03 | [add if applicable] | | | IG-03 |

**Snapshot validity rule**: Each SQ-ID requires a named alternative, a gap statement, a risk dimension, and a seeding IG-ID. A row with a named alternative but a blank gap statement is a structural fail.

---

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Each IG-ID seeded from [STATUS-QUO-SNAPSHOT] must reference its SQ-ID. Minimum 2 IG-IDs required.

**Elimination Path format**: Begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason. When AMPLIFIED, use pre-printed sub-slot format. When C-03 WAIVER applies, mark `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format**:
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. "Risk:" populated with "R-ID:" blank is a structural fail, not a content gap. "R-ID:" populated with "Risk:" blank is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | SQ-ID (if seeded) | Elimination Path | Risk Signal |
|-------|------------------|--------------------|------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [from SQ-01] | SQ-01 | R-ID: R-XX — [reason; AMPLIFIED → sub-slot format] | STANDARD / AMPLIFIED [cite trigger] |
| IG-02 | [role] | [from SQ-02] | SQ-02 | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | [add if applicable] | | [SQ-XX or —] | | |

---

### [ID-REGISTER] — Inertia Decision Register

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named constraint or open question, if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated. [STATUS-QUO-SNAPSHOT] must carry minimum 2 SQ-IDs with gap statements and seeding IG-IDs.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural waiver propagation rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [STATUS-QUO-SNAPSHOT] present with minimum 2 SQ-IDs (Condition 1 extension), [IG-REGISTER] and [ID-REGISTER] present (Condition 1), every non-waived Elimination Path cell contains a named R-ID (Condition 2), all AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified).
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate. Flag any spec decision that conflicts with [STRATEGY-SCOPE-TABLE] risk dimension in the Open Questions or Constraints section.**

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, core workflow, and business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [name source artifact and signal from Phase 1 location 1 of 2, or "none loaded"] |
| Strategy risk alignment | [cite [STRATEGY-SCOPE-TABLE] primary risk dimension or "no conflict identified"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row below before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it.

---

### 4. Constraints

List non-negotiable implementation constraints. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, include a named constraint traceable to that IG-ID.

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections present in order, or before [STRATEGY-SCOPE-SEAL], [PM-CONTRACT-SEAL], and [INERTIA-ANALYZED] all present in this document.
>
> INVALID IF cross-namespace signal absent at both locations (Phase 1 table location 1 of 2 AND Purpose row location 2 of 2) when a non-requirements scout artifact was LOADED.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, all three gate tokens previously emitted ([STRATEGY-SCOPE-SEAL] + [PM-CONTRACT-SEAL] + [INERTIA-ANALYZED]), cross-namespace signal at both locations when applicable, [STATUS-QUO-SNAPSHOT] minimum 2 SQ-IDs with seeding IG-IDs verified.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

Amendment list:
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]
... (minimum 2 items required)

===== END PHASE 4 =====

---

## ===== FINDINGS =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Self-review scan list — Architect verifies each before emitting FINDINGS:
- [STRATEGY-SCOPE-SEAL] present with Scope decision = IN SCOPE and Risk amplification forecast
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [STATUS-QUO-SNAPSHOT] present with minimum 2 SQ-IDs, gap statements, and seeding IG-IDs
- [INERTIA-ANALYZED] present with Condition 1 (all tables) and Condition 2 (R-ID per cell) certified
- Cross-namespace signal at both locations (Phase 1 table location 1 of 2 AND Purpose row location 2 of 2)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order

===== END FINDINGS =====
