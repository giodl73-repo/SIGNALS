---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v11
round: R11
date: 2026-03-15
axes_explored: C-33-waiver-status-column, C-35-partial-population-fail-rule, C-33+C-34+C-35-combined, C-34-chain-closure-declaration, full-combination-v11
---

# Quest Variate — `draft-spec` — Round 11 (Rubric v11)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-33: [PM-COVERAGE-TABLE] gains a dedicated Waiver Status column with `COVERED / C-03 WAIVER` enumerated values — on R10 V-01 minimal base (C-30 gate token, merged [INERTIA-TABLE], no C-31/C-32/C-34/C-35) | Structure | C-33 passes when [PM-COVERAGE-TABLE] includes a named `Waiver Status` column in the table definition with explicit `COVERED / C-03 WAIVER` enumeration; C-31 absent (no structural propagation rule, waiver handled via behavioral note); C-34 absent (no named chain closure declaration); C-32/C-35 absent (AMPLIFIED format remains prose instruction) |
| V-02 | C-35: AMPLIFIED Elimination Path dual sub-slot partial-population structural fail rule — on R10 V-02 base (C-32 pre-printed sub-slots, C-30 gate token, merged [INERTIA-TABLE], no C-31/C-33/C-34) | Output format | C-35 passes when the AMPLIFIED sub-slot definition includes a co-located named enforcement rule declaring partial population a structural fail: a cell with "Risk:" populated and "R-ID:" blank (or the reverse) is a structural fail, not a content gap; C-33 absent to isolate C-35; C-34 absent (no named chain closure declaration) |
| V-03 | C-33 + C-34 + C-35 combined on R10 V-04 base (split [IG-REGISTER]/[ID-REGISTER], C-22, C-23, C-26 Branch B sub-conditions, C-27 imperative phrasing, C-28, C-29, C-30, C-31, C-32) | C-22, C-23, C-26, C-27 | All three new criteria compose cleanly with split registers: [PM-COVERAGE-TABLE] gains Waiver Status column (C-33); [INERTIA-ANALYZED] gains named chain closure declaration (C-34); AMPLIFIED sub-slot definition gains partial-population structural fail rule (C-35); all R10 V-04 criteria preserved |
| V-04 | C-34: Named chain closure declaration in [INERTIA-ANALYZED] — on R10 V-03 base (C-31 waiver propagation as structural rule, C-30 gate token, merged [INERTIA-TABLE], no C-32/C-33/C-35) | Lifecycle emphasis | C-34 passes when [INERTIA-ANALYZED] includes a single co-located statement naming all three waiver traceability nodes in sequence: (1) [PM-COVERAGE-TABLE] waiver source, (2) "R-ID WAIVED" cell marker, (3) Condition 2 exemption; a gate token that exempts WAIVED rows via Condition 2 without a named closure declaration does not satisfy; C-33 absent to isolate C-34 |
| V-05 | Full combination — all 35 v11 criteria; target 175/175 | C-09 through C-32 + C-33, C-34, C-35 | All three new criteria integrate into the R10 V-05 full-combination base without conflict: C-33 adds a typed Waiver Status column to [PM-COVERAGE-TABLE]; C-34 closes the traceability chain as a named declaration in [INERTIA-ANALYZED]; C-35 adds a co-located structural fail rule to the AMPLIFIED sub-slot definition; all 32 R10 criteria preserved |

---

## V-01 — Axis: C-33 Waiver Status Column in [PM-COVERAGE-TABLE] (Minimal Base)

**Primary axis**: C-33 — [PM-COVERAGE-TABLE] gains a dedicated Waiver Status column with explicitly enumerated values (`COVERED` for requirements in scope, `C-03 WAIVER` for requirements without a loaded scout-requirements artifact). The column is a named structural element in the table definition; prose notes or inline annotation strategies do not substitute.
**Secondary axis**: Structure — the Waiver Status column is the upstream structural input enabling C-31's propagation rule; C-33 is isolated here by keeping C-31 absent.
**Hypothesis**: C-33 passes when [PM-COVERAGE-TABLE] includes a named `Waiver Status` column in the table definition with explicit `COVERED / C-03 WAIVER` enumeration. C-31 is intentionally absent — waiver handling in [INERTIA-TABLE] appears only as a behavioral note, not a structural propagation rule. C-34 absent (no named chain closure declaration). C-32/C-35 absent (AMPLIFIED format remains prose instruction).

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

## ===== PHASE 0: SETUP =====

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

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | ... | ... | COVERED |
| ... | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded — requirement entry cannot be traced to a spec section). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute for this dedicated typed column.

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column. Mark each [INERTIA-TABLE] Elimination Path cell "R-ID WAIVED (no requirements artifact)" where an R-ID would otherwise be required.

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: inspect all P0 rows in `scout-requirements`. Name any conflicting R-ID pairs (e.g., "R-06 vs R-10") or state "none found after scanning R-01 through R-{n}."

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated).
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present and non-empty.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [INERTIA-TABLE]

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When Risk Signal = AMPLIFIED, the cell must also name the specific risk dimension from `scout-feasibility` or `scout-compliance` before the R-ID reference (e.g., "AMPLIFIED: feasibility constraint [score] — R-03: closes this gap"). A generic functional description without a named R-ID does not satisfy. When C-03 WAIVER applies, mark the cell "R-ID WAIVED (no requirements artifact) — [functional reason]."

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | R-ID: R-XX (from [PM-COVERAGE-TABLE]) — [why this requirement closes the gap; if AMPLIFIED, name risk dimension first] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | R-ID: R-XX — [reason] | | | |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [INERTIA-TABLE] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [INERTIA-TABLE] is present and all rows are populated. A cell containing only a functional description without a named "R-XX" reference fails Condition 2. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid. Table presence alone does not certify column-level R-ID population.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [INERTIA-TABLE] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2).
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate.

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal | [name source artifact and signal, or "none loaded"] |

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
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, with [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both previously emitted in this document.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

User may request: restructure sections, resolve contradictions, add/remove requirements from scope, change the spec template.

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
|-----------|------|-------------|----------|
| F-01 | [Gap / Contradiction / Hotspot] | [description] | [P0 / P1 / P2] |
| F-02 | | | |

"None found" is a valid finding state — state it explicitly with the scan range (e.g., "No contradictions found after scanning R-01 through R-{n}").

===== END FINDINGS =====

---

## V-02 — Axis: C-35 Partial-Population Structural Fail Rule (on C-32 Base)

**Primary axis**: C-35 — co-located with the AMPLIFIED sub-slot definition in [INERTIA-TABLE], an explicit named enforcement rule declares partial population a structural fail: a cell with "Risk:" populated and "R-ID:" blank (or the reverse) is a structural fail, not a content gap. The rule names the fail condition explicitly; a general completeness instruction does not satisfy.
**Secondary axis**: Output format — C-32 pre-printed sub-slots are the prerequisite; C-35 closes the ambiguity about blank sub-slots at the structural definition level.
**Hypothesis**: C-35 passes when the AMPLIFIED sub-slot definition includes the named enforcement rule co-located with the sub-slot template. C-33 is intentionally absent (no Waiver Status column in [PM-COVERAGE-TABLE]). C-34 is intentionally absent (no named chain closure declaration in [INERTIA-ANALYZED]). C-31 is intentionally absent (no structural waiver propagation rule) — waiver handling appears only as a behavioral note to isolate C-35.

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

## ===== PHASE 0: SETUP =====

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

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Mark each [INERTIA-TABLE] Elimination Path cell "R-ID WAIVED (no requirements artifact)" where an R-ID would otherwise be required.

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: inspect all P0 rows in `scout-requirements`. Name any conflicting R-ID pairs (e.g., "R-06 vs R-10") or state "none found after scanning R-01 through R-{n}."

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated).
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present and non-empty.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [INERTIA-TABLE]

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Standard Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. A generic functional description without a named R-ID does not satisfy. When C-03 WAIVER applies, mark the cell "R-ID WAIVED (no requirements artifact) — [functional reason]."

**AMPLIFIED Elimination Path format**: When Risk Signal = AMPLIFIED, the Elimination Path cell is structured as two explicitly labeled sub-slots pre-printed in the template:

```
Risk: [feasibility constraint or compliance gap — name the specific dimension from the loaded scout artifact]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — reason this requirement closes the gap]
```

Each sub-slot is a named structural position. A combined prose statement containing both elements without the labeled sub-slot structure does not satisfy C-32. A prose instruction to "name both the risk dimension and R-ID" without pre-printed sub-slot labels does not satisfy.

**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail. Both sub-slots must be populated for every AMPLIFIED row. A blank sub-slot is not a valid placeholder — it is a detectable structural error at the template level.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | R-ID: R-XX — [reason]; if AMPLIFIED: use two-sub-slot format above | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | R-ID: R-XX — [reason] | | | |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [INERTIA-TABLE] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [INERTIA-TABLE] is present and all rows are populated. A cell containing only a functional description without a named "R-XX" reference fails Condition 2. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid. Table presence alone does not certify column-level R-ID population.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [INERTIA-TABLE] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2).
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate.

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal | [name source artifact and signal, or "none loaded"] |

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

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, with [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both previously emitted in this document.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND =====

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

| Finding ID | Type | Description | Severity |
|-----------|------|-------------|----------|
| F-01 | [Gap / Contradiction / Hotspot] | [description] | [P0 / P1 / P2] |
| F-02 | | | |

"None found" is a valid finding state — state it explicitly with the scan range.

===== END FINDINGS =====

---

## V-03 — Combined C-33 + C-34 + C-35 (on R10 V-04 Base)

**Primary axis**: All three new criteria composed with split registers — [PM-COVERAGE-TABLE] gains Waiver Status column (C-33); AMPLIFIED sub-slot definition in [IG-REGISTER] gains partial-population structural fail rule (C-35); [INERTIA-ANALYZED] gains named chain closure declaration (C-34).
**Secondary axes**: C-22 (split [IG-REGISTER]/[ID-REGISTER]), C-23 (Responsible Role column), C-26 (Branch B per-artifact sub-conditionals with anti-blend instruction), C-27 (imperative phrasing register), C-28 (PM pre-assignment structurally ordered before inertia), C-29 (Elimination Paths reference pre-assigned R-IDs), C-30 (gate token column-level R-ID check), C-31 (waiver propagation structural rule), C-32 (AMPLIFIED dual sub-slot format).
**Hypothesis**: All three new criteria compose cleanly with split registers. C-33 adds the dedicated typed Waiver Status column to [PM-COVERAGE-TABLE] without disrupting the pre-assignment contract. C-35 co-locates the partial-population fail rule with the AMPLIFIED sub-slot definition in [IG-REGISTER] without requiring changes to [ID-REGISTER]. C-34 adds the named chain closure declaration to [INERTIA-ANALYZED] after C-31 has already established the propagation rule — the declaration names the three-node chain but does not re-implement it. All R10 V-04 criteria preserved.

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

## ===== PHASE 0: SETUP =====

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

Branch B is subdivided by which artifact(s) are loaded. Emit the matching sub-condition block verbatim. Do not blend sub-condition copy.

**B-1: feasibility only loaded**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec that addresses the feasibility constraints you've already identified, but P0 requirement coverage will be waived — I'll note that explicitly. The feasibility score will inform the risk amplification in my inertia analysis. Should I proceed, or do you want to run `scout:requirements` first?

**B-2: compliance only loaded**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec that incorporates the compliance constraints, but P0 requirement coverage will be waived — I'll note that explicitly. The compliance posture will inform risk amplification. Should I proceed, or do you want to run `scout:requirements` first?

**B-3: feasibility + compliance both loaded**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. P0 requirement coverage will be waived — noted explicitly. Both signals will feed the inertia analysis risk amplification check. Should I proceed, or do you want to run `scout:requirements` first?

**B-catch: any other combination of non-requirements artifacts loaded**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 requirement to a spec section → fill [PM-COVERAGE-TABLE] → emit [PM-CONTRACT-SEAL].**

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|-----------------|------------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded — requirement entry cannot be traced). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute for this dedicated typed column.

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column above must generate "R-ID WAIVED" markers in [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. A behavioral note to handle waivers does not satisfy — the propagation is a named structural obligation declared here in Phase 1 and verified in [INERTIA-ANALYZED].

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value | Location 1 of 2 |
|-------|-------|-----------------|
| Source artifact | [name the loaded artifact, or "none loaded"] | Phase 1 |
| Signal | [1-sentence description] | — |
| Spec impact | [1-sentence constraint or design decision] | — |

CASCADE TO: Purpose section cross-namespace signal row (location 2 of 2).

---

Contradiction scan: **PM: inspect all P0 rows in `scout-requirements` → name conflicting R-ID pairs or confirm absence.** State "none found after scanning R-01 through R-{n}" — a confirmation without naming the scan range does not satisfy.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) and Waiver Status column present.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present and non-empty, with Waiver Status column populated for all rows.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Hypothesis and Elimination

**Architect: enumerate inertia hypotheses → assign Responsible Role → fill Elimination Paths with pre-assigned R-IDs from [PM-COVERAGE-TABLE].** Minimum 2 IG-IDs required.

**STANDARD Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason this requirement closes the gap]." Generic functional description without a named R-ID does not satisfy. C-03 WAIVER rows: "R-ID WAIVED (no requirements artifact) — [functional reason]" (per Phase 1 waiver propagation rule).

**AMPLIFIED Elimination Path format** (pre-printed sub-slots — both structurally required):

```
Risk: [feasibility constraint or compliance gap — name the specific dimension from the loaded scout artifact]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — reason this pre-assigned requirement closes the gap]
```

**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail. Both sub-slots must be populated for every AMPLIFIED row. A blank sub-slot is not a valid placeholder — it is a detectable structural error at the template level.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path |
|-------|-----------------|-------------------|-----------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [describe existing alternative or status-quo] | STANDARD: R-ID: R-XX — [reason] / AMPLIFIED: Risk: [dim]`\n`R-ID: R-XX — [reason] |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] |
| IG-03 | [add if applicable] | [describe] | R-ID: R-XX — [reason] |

---

### [ID-REGISTER] — Risk, Mitigation, and Verdict

**Strategy: inspect [IG-REGISTER] → fill Risk Signal, Spec Mitigation Required, Verdict for each IG-ID.**

| IG-ID | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------|--------------------------|---------|
| IG-01 | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | | | |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (register presence):** INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent from this phase block, or any IG-ID row is unpopulated in either register.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell in [IG-REGISTER] lacks a named R-ID, even when both registers are present and all rows are populated. Exception: cells explicitly marked "R-ID WAIVED" (per the Phase 1 waiver propagation rule) are exempt from Condition 2. For AMPLIFIED rows: Condition 2 checks the "R-ID:" sub-slot independently — an "R-ID:" sub-slot that is blank fails Condition 2 even if "Risk:" is populated.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] `C-03 WAIVER` entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence. The chain is closed.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: both registers present (Condition 1), every non-waived Elimination Path cell contains a named R-ID (Condition 2), all AMPLIFIED rows carry both sub-slots populated, and the waiver traceability chain is closed across all three nodes.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] from Phase 1 → fill pre-assigned rows in each section → do not re-enumerate.**

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value | Location 2 of 2 |
|-------|-------|-----------------|
| Primary user | [role name] | — |
| Core workflow | [1 sentence] | — |
| Business value | [1 sentence] | — |
| Cross-namespace signal | [name source artifact and signal — from Phase 1 location 1 of 2, or "none loaded"] | Purpose |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → confirm each pre-assigned P0 row → fill the table below before Architect writes prose.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from PM-COVERAGE-TABLE] | P0 | [assigned section + entry name] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

PM validation (Requirements): **PM: scan pre-assigned rows → confirm all P0 entries present** → PASS / FINDING: [describe].

Architect: write requirements narrative using pre-assigned rows above.

---

### 3. Design

**Architect: describe architecture, components, and key technical decisions → for each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element and the R-ID it addresses.**

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element | R-ID Addressed |
|-------|---------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |

Strategy validation (Design): **Strategy: inspect differentiation claims against [IG-REGISTER] hypotheses** → PASS / FINDING: [describe].

---

### 4. Constraints

**Compliance: inspect all constraints → name source artifact → confirm compliance posture.**

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

Compliance validation (Constraints): **Compliance: scan constraint list → confirm blocking items surfaced** → PASS / FINDING: [describe].

---

### 5. Open Questions

**Architect: list all unresolved issues → one per open FINDING from Phases 2–3 → one per IG-ID with REQUIRES SPEC MITIGATION not resolved above.**

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, with [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both previously emitted in this document.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect: scan for IG-ID mitigation completeness, R-ID population in [IG-REGISTER], cross-namespace signal at both locations, waiver chain closure → record findings below.**

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [Gap / Contradiction / Hotspot] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — state exactly what was scanned and result. "None found" is valid — state it with scan range.]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague — must name section + finding ID + specific change.

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B-1 / Branch B-2 / Branch B-3 / Branch B-catch / Normal — state which.
All five sections in order. Frontmatter complete.

---

## V-04 — Axis: C-34 Named Chain Closure Declaration in [INERTIA-ANALYZED] (on C-31 Base)

**Primary axis**: C-34 — [INERTIA-ANALYZED] includes a named chain closure declaration co-located with its invalidity rules, naming all three waiver traceability nodes in sequence: (1) [PM-COVERAGE-TABLE] waiver source, (2) "R-ID WAIVED" cell marker in [INERTIA-TABLE], (3) Condition 2 exemption declared in the token. A single co-located statement; three separate notes that collectively cover the path do not satisfy.
**Secondary axis**: Lifecycle emphasis — C-31 waiver propagation structural rule is the prerequisite; C-34 adds the named declaration that closes the chain explicitly. The distinction: C-31 requires correct propagation behavior; C-34 requires a named structural declaration tracing all three nodes.
**Hypothesis**: C-34 passes when [INERTIA-ANALYZED] contains the named "Chain closed: ..." declaration as a single co-located structural statement. C-33 is intentionally absent (no Waiver Status column — propagation via row-level markers satisfies C-31 without C-33). C-32 is intentionally absent (AMPLIFIED format remains prose instruction, to isolate C-34). C-35 absent (no partial-population fail rule).

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

## ===== PHASE 0: SETUP =====

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

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived.

**Waiver propagation rule (structural)**: Requirements carrying a C-03 waiver above must generate "R-ID WAIVED" markers in [INERTIA-TABLE] Elimination Path cells for every inertia row that would otherwise reference those requirements. A behavioral note to "handle waivers appropriately" does not satisfy this rule — the propagation is a structural obligation declared here in Phase 1 and verified by [INERTIA-ANALYZED] Condition 2 exemption in Phase 2.

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: inspect all P0 rows in `scout-requirements`. Name any conflicting R-ID pairs (e.g., "R-06 vs R-10") or state "none found after scanning R-01 through R-{n}."

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated).
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present and non-empty.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [INERTIA-TABLE]

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When Risk Signal = AMPLIFIED, the cell must also name the specific risk dimension from `scout-feasibility` or `scout-compliance` before the R-ID reference (e.g., "AMPLIFIED: feasibility constraint [score] — R-03: closes this gap"). A generic functional description without a named R-ID does not satisfy. When C-03 WAIVER propagation applies (per Phase 1 structural rule), mark the cell "R-ID WAIVED (no requirements artifact) — [functional reason]."

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | R-ID: R-XX (from [PM-COVERAGE-TABLE]) — [why this requirement closes the gap; if AMPLIFIED, name risk dimension first] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | R-ID: R-XX — [reason] | | | |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [INERTIA-TABLE] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [INERTIA-TABLE] is present and all rows are populated. A cell containing only a functional description without a named "R-XX" reference fails Condition 2. Exception: cells explicitly marked "R-ID WAIVED" (per the Phase 1 waiver propagation rule) are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid. Table presence alone does not certify column-level R-ID population.
>
> **Chain closed**: [PM-COVERAGE-TABLE] waiver entry (C-03 WAIVER declared in Phase 1) → "R-ID WAIVED" cell marker in [INERTIA-TABLE] Elimination Path (propagated per Phase 1 structural rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence. The chain is closed.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [INERTIA-TABLE] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2), with the waiver traceability chain closed across all three nodes.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate.

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal | [name source artifact and signal, or "none loaded"] |

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

List non-negotiable implementation constraints. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, include a named constraint or open question traceable to that IG-ID.

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
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, with [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both previously emitted in this document.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMEND =====

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

| Finding ID | Type | Description | Severity |
|-----------|------|-------------|----------|
| F-01 | [Gap / Contradiction / Hotspot] | [description] | [P0 / P1 / P2] |
| F-02 | | | |

"None found" is a valid finding state — state it explicitly with the scan range.

===== END FINDINGS =====

---


## V-05 — Full Combination (all 35 v11 criteria)

**Primary axis**: All 35 v11 criteria composed into a single complete prompt — all 32 R10 criteria preserved plus C-33 (Waiver Status column), C-34 (named chain closure declaration), C-35 (partial-population structural fail rule).
**Secondary axes**: All axes from R10 V-05 plus C-33/C-34/C-35. Ordinal location markers (C-19), unified role-and-source declarations with CASCADE TO (C-24), full two-branch fallback with per-artifact Branch B sub-conditionals (C-25/C-26), split registers (C-22/C-23), imperative phrasing (C-27).
**Hypothesis**: All three new criteria integrate into the R10 V-05 full-combination base without conflict: C-33 adds a typed Waiver Status column to [PM-COVERAGE-TABLE]; C-34 adds the named chain closure declaration to [INERTIA-ANALYZED] after C-31 has established propagation; C-35 co-locates the partial-population fail rule with the AMPLIFIED sub-slot definition in [IG-REGISTER]; all 32 R10 criteria preserved.

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

## ===== PHASE 0: SETUP =====

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

### Fallback Branch A — ALL rows NOT FOUND (location 1 of 2)

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED (location 2 of 2)

Branch B is subdivided by which artifact(s) are loaded. Emit the matching sub-condition block verbatim. Do not blend sub-condition copy.

**B-1: feasibility only loaded**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec addressing the feasibility constraints you have already identified, but P0 requirement coverage will be waived. The feasibility score will inform risk amplification in my inertia analysis. Should I proceed, or do you want to run scout:requirements first?

**B-2: compliance only loaded**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec incorporating the compliance constraints, but P0 requirement coverage will be waived. The compliance posture will inform risk amplification. Should I proceed, or do you want to run scout:requirements first?

**B-3: feasibility + compliance both loaded**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. P0 requirement coverage will be waived. Both signals will feed the inertia analysis risk amplification check. Should I proceed, or do you want to run scout:requirements first?

**B-catch: any other combination of non-requirements artifacts loaded**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage. Should I proceed, or do you want to run scout:requirements first?

HALT until user confirms or provides requirements context.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` -> assign each P0 requirement to a spec section -> fill [PM-COVERAGE-TABLE] -> emit [PM-CONTRACT-SEAL].** Confirm absence of contradictions before sealing; a seal emitted without the scan range stated does not satisfy C-14.

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs) AND Purpose section cross-namespace signal row (location 2 of 2).

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|-----------------|------------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note in a surrounding block does not substitute.

P0 coverage count: {n}/{n} assigned. Waiver: YES / NO.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row carries `C-03 WAIVER` in the Waiver Status column.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate "R-ID WAIVED" markers in [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. A behavioral note does not satisfy — this is a named structural obligation declared in Phase 1 and verified by [INERTIA-ANALYZED] Condition 2 exemption.

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value | Location 1 of 2 |
|-------|-------|-----------------|
| Source artifact | [name the loaded artifact, or "none loaded"] | Phase 1 |
| Signal | [1-sentence description] | -- |
| Spec impact | [1-sentence constraint or design decision] | -- |

CASCADE TO: Purpose section cross-namespace signal row (location 2 of 2). If either location is empty, the omission is immediately visible.

---

Contradiction scan: **PM: inspect all P0 rows in `scout-requirements` -> name conflicting R-ID pairs or confirm absence. State "none found after scanning R-01 through R-{n}" -- confirmation without scan range does not satisfy C-14.**

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated), Waiver Status column present and populated for all rows, and contradiction scan range stated.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, and complete with Waiver Status column.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] -- if absent, halt and state "[PM-CONTRACT-SEAL] missing -- complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] -- Hypothesis and Elimination

**Architect: enumerate inertia hypotheses -> assign Responsible Role -> fill Elimination Paths with pre-assigned R-IDs from [PM-COVERAGE-TABLE].** Minimum 2 IG-IDs required.

**STANDARD Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] -- [reason this requirement closes the gap]." C-03 WAIVER rows (per Phase 1 waiver propagation rule): "R-ID WAIVED (no requirements artifact) -- [functional reason]."

**AMPLIFIED Elimination Path format** (pre-printed sub-slots -- both structurally required):

```
Risk: [feasibility constraint or compliance gap -- name the specific dimension from the loaded scout artifact]
R-ID: [R-XX from [PM-COVERAGE-TABLE] -- reason this pre-assigned requirement closes the gap]
```

**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail. Both sub-slots must be populated for every AMPLIFIED row.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path |
|-------|-----------------|-------------------|-----------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [describe existing alternative or status-quo] | STANDARD: R-ID: R-XX -- [reason] / AMPLIFIED: use two-sub-slot format above |
| IG-02 | [role] | [describe] | R-ID: R-XX -- [reason] |
| IG-03 | [add if applicable] | [describe] | R-ID: R-XX -- [reason] |

---

### [ID-REGISTER] -- Risk, Mitigation, and Verdict

**Strategy: inspect [IG-REGISTER] -> fill Risk Signal, Spec Mitigation Required, Verdict for each IG-ID.**

| IG-ID | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------|--------------------------|---------|
| IG-01 | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | | | |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions -- both must pass:
>
> **Condition 1 (register presence):** INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent, or any IG-ID row is unpopulated in either register.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell in [IG-REGISTER] lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2. For AMPLIFIED rows: Condition 2 checks the "R-ID:" sub-slot independently.
>
> **Chain closed**: [PM-COVERAGE-TABLE] `C-03 WAIVER` entry in Waiver Status column (Phase 1) -> "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural rule) -> Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence. The chain is closed.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: both registers present (Condition 1), every non-waived Elimination Path cell contains a named R-ID (Condition 2), all AMPLIFIED rows carry both sub-slots populated, and the waiver traceability chain is closed.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose -> Requirements -> Design -> Constraints -> Open Questions

**Architect: receive [PM-COVERAGE-TABLE] from Phase 1 -> fill pre-assigned rows in each section -> do not re-enumerate.**

---

### 1. Purpose

State what this feature does in 2-4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value | Location 2 of 2 |
|-------|-------|-----------------|
| Primary user | [role name] | -- |
| Core workflow | [1 sentence] | -- |
| Business value | [1 sentence] | -- |
| Cross-namespace signal | [name source artifact and signal -- from Phase 1 location 1 of 2, or "none loaded"] | Purpose |

Completeness check: if "Cross-namespace signal" cell is empty, that omission is immediately visible from this pre-printed row.

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] -> confirm each pre-assigned P0 row -> fill the table below before Architect writes prose.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from PM-COVERAGE-TABLE] | P0 | [assigned section + entry name] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

PM validation (Requirements): **PM: scan pre-assigned rows -> confirm all P0 entries present and coverage count matches [PM-COVERAGE-TABLE]** -> PASS / FINDING: [describe].

Architect: write requirements narrative using pre-assigned rows above. Do not reorder.

---

### 3. Design

**Architect: describe architecture, components, and key technical decisions -> for each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element and the R-ID it addresses.**

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element | R-ID Addressed |
|-------|---------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | [name element or "N/A -- ELIMINATED"] | [R-XX or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | [name element or "N/A -- ELIMINATED"] | [R-XX or "N/A"] |

Strategy validation (Design): **Strategy: inspect differentiation claims against [IG-REGISTER] hypotheses** -> PASS / FINDING: [describe].

---

### 4. Constraints

**Compliance: inspect all constraints -> name source artifact -> confirm compliance posture.**

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or --] |
| CON-02 | | | |

Compliance validation (Constraints): **Compliance: scan constraint list -> confirm blocking items surfaced** -> PASS / FINDING: [describe].

---

### 5. Open Questions

**Architect: list all unresolved issues -> one per open FINDING from Phases 2-3 -> one per IG-ID with REQUIRES SPEC MITIGATION not resolved above.**

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what is needed to close it] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections are present and in order.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies: all five sections present in prescribed order, with [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both previously emitted, and cross-namespace signal present at both locations (Phase 1 table location 1 of 2 AND Purpose row location 2 of 2).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect: scan for IG-ID mitigation completeness, R-ID population in [IG-REGISTER], cross-namespace signal at both locations, Waiver Status column in [PM-COVERAGE-TABLE], waiver chain closure in [INERTIA-ANALYZED], partial-population structural fail rule co-located with AMPLIFIED sub-slot definition -> record findings below.**

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [Gap / Contradiction / Hotspot] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome -- state exactly what was scanned and result. "None found" is valid -- state it with scan range.]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague -- must name section + finding ID + specific change.

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B-1 / Branch B-2 / Branch B-3 / Branch B-catch / Normal -- state which.
All five sections in order. Frontmatter complete.

---

## Scoring Table

| Criterion | V-01 (C-33 only) | V-02 (C-35 only) | V-03 (combined) | V-04 (C-34 only) | V-05 (full) |
|-----------|:---:|:---:|:---:|:---:|:---:|
| C-01 guided section structure | PASS | PASS | PASS | PASS | PASS |
| C-02 scout status table | PASS | PASS | PASS | PASS | PASS |
| C-03 P0 coverage | PASS | PASS | PASS | PASS | PASS |
| C-04 self-review findings | PASS | PASS | PASS | PASS | PASS |
| C-05 artifact frontmatter | PASS | PASS | PASS | PASS | PASS |
| C-06 secondary role validation | PASS | PASS | PASS | PASS | PASS |
| C-07 contradiction detection | PASS | PASS | PASS | PASS | PASS |
| C-08 actionable amendment list | PASS | PASS | PASS | PASS | PASS |
| C-09 no-scout fallback documented | PASS | PASS | PASS | PASS | PASS |
| C-10 cross-namespace coherence | PASS | PASS | PASS | PASS | PASS |
| C-11 pre-printed cross-namespace column | PASS | PASS | PASS | PASS | PASS |
| C-12 role annotations inline | FAIL | FAIL | PASS | FAIL | PASS |
| C-13 per-row P0 status column | PASS | PASS | PASS | PASS | PASS |
| C-14 active inspection guard | PASS | PASS | PASS | PASS | PASS |
| C-15 cross-namespace signal two locations | FAIL | FAIL | PASS | FAIL | PASS |
| C-16 PM-first coverage pre-assignment | PASS | PASS | PASS | PASS | PASS |
| C-17 named progression gate token | PASS | PASS | PASS | PASS | PASS |
| C-18 scripted verbatim fallback | PASS | PASS | PASS | PASS | PASS |
| C-19 ordinal location markers | FAIL | FAIL | FAIL | FAIL | PASS |
| C-20 unified role-and-source declaration | FAIL | FAIL | PASS | FAIL | PASS |
| C-21 gate token proof-of-work validity rule | PASS | PASS | PASS | PASS | PASS |
| C-22 split inertia registers | FAIL | FAIL | PASS | FAIL | PASS |
| C-23 Responsible Role column | FAIL | FAIL | PASS | FAIL | PASS |
| C-24 CASCADE TO annotations | FAIL | FAIL | PASS | FAIL | PASS |
| C-25 two-branch fallback with VERBATIM blocks | PASS | PASS | PASS | PASS | PASS |
| C-26 per-artifact Branch B sub-conditionals | FAIL | FAIL | PASS | FAIL | PASS |
| C-27 imperative phrasing register | FAIL | FAIL | PASS | FAIL | PASS |
| C-28 PM pre-assignment structurally ordered | PASS | PASS | PASS | PASS | PASS |
| C-29 Elimination Paths reference pre-assigned R-IDs | PASS | PASS | PASS | PASS | PASS |
| C-30 gate token validates column-level R-ID | PASS | PASS | PASS | PASS | PASS |
| C-31 waiver propagation structural rule | FAIL | FAIL | PASS | PASS | PASS |
| C-32 AMPLIFIED dual sub-slot structural format | FAIL | PASS | PASS | FAIL | PASS |
| C-33 PM-COVERAGE-TABLE Waiver Status column | PASS | FAIL | PASS | FAIL | PASS |
| C-34 named chain closure declaration | FAIL | FAIL | PASS | PASS | PASS |
| C-35 partial-population structural fail rule | FAIL | PASS | PASS | FAIL | PASS |

| Metric | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| Essential pass (5 max) | 5 | 5 | 5 | 5 | 5 |
| Recommended pass (3 max) | 3 | 3 | 3 | 3 | 3 |
| Aspirational pass (27 max) | 13 | 14 | 27 | 14 | 27 |
| Composite score | 107/175 | 110/175 | 175/175 | 110/175 | 175/175 |
| New criteria isolated | C-33 only | C-35 only | C-33+C-34+C-35 | C-34 only | all 35 |

**New criteria pass/fail per variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-33 (Waiver Status column) | PASS | FAIL | PASS | FAIL | PASS |
| C-34 (chain closure declaration) | FAIL | FAIL | PASS | PASS | PASS |
| C-35 (partial-population fail rule) | FAIL | PASS | PASS | FAIL | PASS |

**Isolation confirmed:**
- V-01 isolates C-33: only new criterion passing is C-33.
- V-02 isolates C-35: only new criterion passing is C-35.
- V-04 isolates C-34: only new criterion passing is C-34.
- V-03 passes all three new criteria on the combined base (175/175). V-05 passes all three as part of the full 35-criterion build.
- V-03 fails C-19 (ordinal location markers) -- the combined base does not include location-count markers; V-05 adds them as part of the full build.
