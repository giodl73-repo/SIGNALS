---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v10
round: R10
date: 2026-03-15
axes_explored: C-30-gate-token-column-check, C-32-amplified-dual-subslots, C-31-waiver-propagation-structural-rule, C-30+C-31+C-32-combined-split-registers, full-combination-v10
---

# Quest Variate — `draft-spec` — Round 10 (Rubric v10)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-30: [INERTIA-ANALYZED] extends its invalidity rule to column-level R-ID population check — minimal base (merged [INERTIA-TABLE], no C-31/C-32) | Inertia framing | C-30 passes when the gate token invalidity rule explicitly names two conditions: Condition 1 (table presence) and Condition 2 (column-level R-ID population); WAIVED cells exempted from Condition 2 via behavioral note; C-31 absent (no structural propagation rule); C-32 absent (AMPLIFIED format remains prose instruction) |
| V-02 | C-32: AMPLIFIED Elimination Path dual sub-slot structural format — on V-01 C-30 base | Output format | C-32 passes when AMPLIFIED rows in [INERTIA-TABLE] carry two pre-printed labeled sub-slots ("Risk:" and "R-ID:") in the markdown table template itself; a prose instruction without pre-printed labels does not satisfy; C-31 absent to isolate C-32 |
| V-03 | C-31: Waiver propagation from [PM-COVERAGE-TABLE] to [INERTIA-TABLE] as a structural rule — on V-01 C-30 base | Lifecycle emphasis | C-31 passes when Phase 1 declares a named structural waiver-propagation rule and [INERTIA-ANALYZED] closes the chain (PM-COVERAGE-TABLE waiver → "R-ID WAIVED" cell marker → gate token exemption); C-32 absent to isolate C-31 |
| V-04 | C-30+C-31+C-32 combined on R9 V-04 base (split [IG-REGISTER]/[ID-REGISTER], C-22, C-23, C-26 Branch B sub-conditions, C-27 imperative phrasing, C-28, C-29) | C-22, C-23, C-26, C-27 | All three new criteria compose cleanly with split registers: [IG-REGISTER] gains AMPLIFIED dual sub-slots (C-32) and waiver propagation (C-31); [INERTIA-ANALYZED] extends to column-content R-ID check with WAIVED exemption (C-30+C-31); no axes from R9 broken |
| V-05 | Full combination — all 32 v10 criteria; target 175/175 | C-09 through C-29 + C-30, C-31, C-32 | All three new criteria integrate into the R9 V-05 full-combination base without conflict: C-31 closes the waiver chain from PM-COVERAGE-TABLE through IG-REGISTER Elimination Path cells to the gate-token exemption; C-30 adds column-content checking to [INERTIA-ANALYZED]; C-32 restructures AMPLIFIED rows into two labeled structural sub-slots; all R9 criteria preserved |

---

## V-01 — Axis: C-30 Gate Token Column-Content Check (Minimal Base)

**Primary axis**: C-30 — [INERTIA-ANALYZED] invalidity rule extended from table-presence checking to column-level R-ID population checking. Two explicit invalidity conditions: Condition 1 (table present, rows populated) and Condition 2 (each non-waived Elimination Path cell contains a named R-ID).
**Secondary axis**: Inertia framing — the gate token explanation foregrounds the distinction between table-presence validity and column-content validity.
**Hypothesis**: C-30 passes on the minimal base when the gate token names Condition 2 as a distinct structural check. C-31 is intentionally absent — waiver handling appears only as a behavioral note, not a structural propagation rule. C-32 is absent — AMPLIFIED rows carry a prose instruction for the dual requirement, not pre-printed sub-slots.

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
skill_version: v10
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

#### 1. Purpose

State what the feature does, who uses it, and what problem it solves. Name the strongest non-requirements signal influencing this purpose statement and its source artifact.

[Write purpose content]

#### 2. Requirements

For each P0 requirement from [PM-COVERAGE-TABLE], confirm placement. At least one secondary role (PM, Strategy, Compliance, or Design) validates this section and records PASS or finding.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

Secondary role validation (Requirements): [role name] — PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element and the R-ID it addresses.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element | R-ID Addressed |
|-------|---------|-------------------|----------------|
| IG-01 | [from [INERTIA-TABLE]] | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |
| IG-02 | [from [INERTIA-TABLE]] | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |

Secondary role validation (Design): Strategy — PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION and mitigation assigned to Constraints, name the constraint and the R-ID it closes.

[List constraints with source artifact names]

Secondary role validation (Constraints): Compliance — PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 2–3, and one per IG-ID with Verdict = REQUIRES SPEC MITIGATION not resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

Scan must cover: IG-ID mitigation completeness; [INERTIA-TABLE] Elimination Path R-ID cells (Condition 2 of [INERTIA-ANALYZED]: any blank or generic cells); Phase 0 fallback branches present; cross-namespace signal named in Purpose.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — state exactly what was scanned and result]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B / Normal — state which.
All five sections in order. Frontmatter complete.

---

---

## V-02 — Axis: C-32 AMPLIFIED Dual Sub-Slot Structural Format (on V-01 base)

**Primary axis**: C-32 — when a row's Risk Signal is AMPLIFIED, the Elimination Path cell is pre-printed in the template as two explicitly labeled sub-slots: "Risk: [feasibility constraint or compliance gap]" and "R-ID: [R-XX from [PM-COVERAGE-TABLE]]". The sub-slots appear in the markdown table template itself, structurally requiring independent population.
**Secondary axis**: Output format — the table template changes shape for AMPLIFIED rows; the dual sub-slot format is the structural differentiator that makes omission visible.
**Hypothesis**: C-32 passes when the AMPLIFIED row template in [INERTIA-TABLE] pre-prints two labeled sub-slots as distinct structural fields. A prose instruction ("name both the risk dimension and R-ID") without pre-printed labels does not satisfy C-32, even if the content would be equivalent. C-29 still passes from V-01. C-31 absent — waiver handling remains a behavioral note.

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
skill_version: v10
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

**STANDARD row — Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason this requirement closes the gap]." A generic description without a named R-ID does not satisfy. C-03 WAIVER rows: "R-ID WAIVED (no requirements artifact) — [functional reason]."

**AMPLIFIED row — Elimination Path format (two pre-printed sub-slots — both must be populated independently):**

```
Risk: [feasibility constraint or compliance gap — name the specific dimension from scout-feasibility or scout-compliance]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the specific entry that closes this risk dimension]
```

A combined prose statement containing both elements without labeled sub-slots does not satisfy C-32. A prose instruction to "name both the risk dimension and R-ID" without pre-printed sub-slot labels does not satisfy C-32. Each sub-slot is structurally required — a cell with only "Risk:" populated and "R-ID:" blank is a structural fail at the R-ID sub-slot level.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | STANDARD: R-ID: R-XX — [reason] / AMPLIFIED: Risk: [dim] / R-ID: R-XX | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | STANDARD: R-ID: R-XX — [reason] / AMPLIFIED: Risk: [dim] / R-ID: R-XX | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> For AMPLIFIED rows: populate both "Risk:" and "R-ID:" sub-slots independently. Either sub-slot absent is a row-level structural fail.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [INERTIA-TABLE] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [INERTIA-TABLE] is present and all rows are populated. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> For AMPLIFIED rows: Condition 2 checks both sub-slots independently — an "R-ID:" sub-slot that is blank or unpopulated fails Condition 2 regardless of whether "Risk:" is populated.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [INERTIA-TABLE] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2) AND all AMPLIFIED rows carry both pre-printed sub-slots populated.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

Architect: receive [PM-COVERAGE-TABLE] from Phase 1 and fill pre-assigned rows. Do not re-enumerate.

#### 1. Purpose

State what the feature does, who uses it, and what problem it solves. Name the strongest non-requirements signal influencing this purpose statement and its source artifact.

[Write purpose content]

#### 2. Requirements

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

Secondary role validation (Requirements): [role name] — PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element and the R-ID it addresses. For AMPLIFIED rows with REQUIRES SPEC MITIGATION, name the design element that addresses both the risk dimension and the requirement.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | Verdict | Risk Signal | Mitigation Element | R-ID Addressed |
|-------|---------|-------------|-------------------|----------------|
| IG-01 | [from [INERTIA-TABLE]] | STANDARD / AMPLIFIED | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |
| IG-02 | [from [INERTIA-TABLE]] | STANDARD / AMPLIFIED | [name element or "N/A — ELIMINATED"] | [R-XX or "N/A"] |

Secondary role validation (Design): Strategy — PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION and mitigation assigned to Constraints, name the constraint and the R-ID it closes.

[List constraints with source artifact names]

Secondary role validation (Constraints): Compliance — PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 2–3, and one per IG-ID with Verdict = REQUIRES SPEC MITIGATION not resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

Scan must cover: IG-ID mitigation completeness; [INERTIA-TABLE] AMPLIFIED rows (both "Risk:" and "R-ID:" sub-slots populated); non-waived Elimination Path R-ID cells (Condition 2 of [INERTIA-ANALYZED]); Phase 0 fallback branches present; cross-namespace signal named in Purpose.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B / Normal — state which.
All five sections in order. Frontmatter complete.

---

---

## V-03 — Axis: C-31 Waiver Propagation Structural Rule (on V-01 base)

**Primary axis**: C-31 — Phase 1 declares a named structural waiver-propagation rule: P0 requirements marked C-03 WAIVER in [PM-COVERAGE-TABLE] generate "R-ID WAIVED" markers in [INERTIA-TABLE] Elimination Path cells for every inertia row that would otherwise reference those requirements. [INERTIA-ANALYZED] closes the chain by explicitly exempting WAIVED-marked rows from its Condition 2 R-ID population check.
**Secondary axis**: Lifecycle emphasis — Phase 1 expands to declare the waiver lifecycle (PM-COVERAGE-TABLE waiver → cell marker → gate token exemption) as a named structural rule, not a behavioral note.
**Hypothesis**: C-31 passes when: (a) Phase 1 contains a named structural waiver-propagation rule, (b) [INERTIA-TABLE] shows "R-ID WAIVED" in the cell format, and (c) [INERTIA-ANALYZED] closes the chain by naming the exemption as the outcome of the propagation rule. A behavioral note ("mark 'R-ID WAIVED' if waived") satisfies none of these. C-32 is absent — AMPLIFIED format remains a prose instruction.

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
skill_version: v10
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
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED / C-03 WAIVER |
| R-02 | P0 | [from artifact] | ... | ... | COVERED / C-03 WAIVER |
| ... | | | | | |

P0 coverage count: {n}/{n} assigned. Waived: {w} (C-03 WAIVER rows will generate "R-ID WAIVED" markers per the propagation rule below).

If `scout-requirements` NOT FOUND: C-03 WAIVER for all requirements — entire [PM-COVERAGE-TABLE] waived. All [INERTIA-TABLE] Elimination Path cells will carry "R-ID WAIVED (requirements artifact absent)."

---

**Waiver propagation rule (structural):** Any requirement row carrying "C-03 WAIVER" in the Waiver Status column of [PM-COVERAGE-TABLE] automatically generates an "R-ID WAIVED" marker in the [INERTIA-TABLE] Elimination Path cell for every inertia row (IG-ID) that would otherwise reference that requirement. This propagation is declared as a structural rule: it applies to every IG-ID row without requiring per-row judgment. The [INERTIA-ANALYZED] gate token exempts rows carrying the "R-ID WAIVED" marker from its Condition 2 R-ID population check — closing the traceability chain: [PM-COVERAGE-TABLE] waiver → [INERTIA-TABLE] cell marker → gate token exemption.

---

Cross-namespace signal (if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: inspect all P0 rows in `scout-requirements`. Name any conflicting R-ID pairs or state "none found after scanning R-01 through R-{n}."

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or full C-03 WAIVER stated) AND the waiver propagation rule declared above.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, and the waiver propagation rule has been declared.
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

**Elimination Path format**:
- STANDARD rows: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason this requirement closes the gap]."
- AMPLIFIED rows: "AMPLIFIED: [risk dimension from scout-feasibility or scout-compliance] — R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]."
- WAIVED rows (per waiver propagation rule from Phase 1): "R-ID WAIVED — [functional reason]." This marker is required; absence of the marker means the row is not exempt from Condition 2 of [INERTIA-ANALYZED].
- A generic functional description without a named R-ID (and without a WAIVED marker) fails Condition 2.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | R-ID: R-XX — [reason] / AMPLIFIED: [risk dim] — R-ID: R-XX — [reason] / R-ID WAIVED — [reason] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [as above] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> Waiver marker "R-ID WAIVED" must appear explicitly — absence of the marker is not an implicit exemption from Condition 2.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [INERTIA-TABLE] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID AND does not carry an explicit "R-ID WAIVED" marker. A cell with a functional description but no R-ID and no WAIVED marker fails Condition 2. The WAIVED marker is the only valid exemption — it is the downstream artifact of the waiver propagation rule declared in Phase 1. Rows not covered by that rule carry no implicit exemption.
>
> Chain closed: [PM-COVERAGE-TABLE] waiver → "R-ID WAIVED" cell marker in [INERTIA-TABLE] → explicit Condition 2 exemption here. A template that carries "R-ID WAIVED" in cells but omits the Condition 2 exemption fails chain closure.
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

#### 1. Purpose

State what the feature does, who uses it, and what problem it solves. Name the strongest non-requirements signal influencing this purpose statement and its source artifact.

[Write purpose content]

#### 2. Requirements

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED / WAIVED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO. Waived rows: {w}.

Secondary role validation (Requirements): [role name] — PASS / FINDING: [describe]

#### 3. Design

[Write design content]

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element | R-ID Addressed |
|-------|---------|-------------------|----------------|
| IG-01 | [from [INERTIA-TABLE]] | [name element or "N/A — ELIMINATED"] | [R-XX or "WAIVED" or "N/A"] |
| IG-02 | [from [INERTIA-TABLE]] | [name element or "N/A — ELIMINATED"] | [R-XX or "WAIVED" or "N/A"] |

Secondary role validation (Design): Strategy — PASS / FINDING: [describe]

#### 4. Constraints

[List constraints with source artifact names]

Secondary role validation (Constraints): Compliance — PASS / FINDING: [describe]

#### 5. Open Questions

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

Scan must cover: IG-ID mitigation completeness; [INERTIA-TABLE] Elimination Path cells (Condition 2 check — any cell lacking R-ID and lacking explicit "R-ID WAIVED" marker); waiver propagation chain integrity (waived rows in [PM-COVERAGE-TABLE] matched to "R-ID WAIVED" markers in [INERTIA-TABLE]); Phase 0 fallback branches present; cross-namespace signal named in Purpose.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B / Normal — state which.
All five sections in order. Frontmatter complete.

---

---

## V-04 — C-30+C-31+C-32 Combined (R9 V-04 base: split registers, C-22, C-23, C-26, C-27)

**Primary axis**: C-30 + C-31 + C-32 combined on R9 V-04 full base (split [IG-REGISTER]/[ID-REGISTER] preserving C-22; Responsible Role column C-23; Branch B sub-conditions C-26; imperative actor-action-output phrasing C-27; PM-before-inertia gate C-28; Elimination Path R-IDs C-29; no CASCADE TO / no C-24).
**Secondary axes**: C-22, C-23, C-26, C-27 (all from R9 V-04 base).
**Hypothesis**: All three new criteria compose cleanly with split registers and imperative phrasing. [IG-REGISTER] gains: (a) AMPLIFIED dual sub-slots (C-32) with "Risk:" and "R-ID:" as pre-printed columns or row-level sub-slots; (b) waiver propagation markers (C-31) — C-03 WAIVER rows carry "R-ID WAIVED" in Elimination Path; (c) [INERTIA-ANALYZED] extends to column-content R-ID check with WAIVED exemption (C-30). No axes from R9 V-04 are broken.

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
skill_version: v10
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

Inspect [SCOUT-STATUS-TABLE] to identify which non-requirements artifacts are LOADED. Match exactly one sub-condition below. Do not blend sub-condition copy; emit the matching block verbatim. If multiple sub-conditions apply simultaneously, apply the higher-numbered condition (B-3 over B-1 or B-2). If none of B-1 through B-3 apply, apply B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND, market/stakeholders/positioning/naming any combination:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — the Design section will be driven by feasibility constraints and I'll call out the specific scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND, market/stakeholders/positioning/naming any combination:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec that treats compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and I'll flag each compliance-driven decision explicitly. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on which decisions would shift if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements, feasibility, and compliance all NOT FOUND, at least one of market/stakeholders/positioning/naming LOADED:**

VERBATIM RESPONSE:
> I have some positioning or market signals for this topic but no requirements, feasibility, or compliance data. I can draft a spec from the available context, but coverage will be limited and constraint grounding will rely on the positioning signals. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

HALT after emitting the matching sub-condition block. Do not blend sub-condition copy; emit the matching block verbatim.

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

**PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE] with section assignments and spec entry names.**

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED / C-03 WAIVER |
| R-02 | P0 | [from artifact] | ... | ... | COVERED / C-03 WAIVER |
| ... | | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER for all requirements. All [IG-REGISTER] Elimination Path cells will carry "R-ID WAIVED."

---

**Waiver propagation rule (structural):** Any requirement row in [PM-COVERAGE-TABLE] carrying "C-03 WAIVER" in the Waiver Status column automatically generates an "R-ID WAIVED" marker in the [IG-REGISTER] Elimination Path cell for every IG-ID row that would otherwise reference that requirement. The propagation applies to all affected IG-IDs without per-row judgment. The [INERTIA-ANALYZED] gate token explicitly exempts "R-ID WAIVED" cells from its Condition 2 R-ID population check. Chain: [PM-COVERAGE-TABLE] waiver → [IG-REGISTER] "R-ID WAIVED" marker → gate token exemption.

---

**PM: scan `scout-feasibility` AND `scout-compliance` (if LOADED) → identify strongest non-requirements signal → fill cross-namespace signal row.**

Cross-namespace signal:

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**PM: scan all P0 rows in `scout-requirements` → identify R-ID contradiction pairs → state scan outcome.**

Contradiction scan: [pairs or "none found after scanning R-01 through R-{n}"]

> Do not confirm "none found" without reviewing the requirements artifact. State which rows were inspected.

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated with Waiver Status column (or full C-03 WAIVER stated)
> - Waiver propagation rule declared in this phase
> - Cross-namespace signal row filled
> - Contradiction scan: named scan outcome stating rows inspected
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies all three outputs are present and non-empty in this block.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

**PM: scan `scout-feasibility` AND `scout-compliance` (if LOADED) → record risk level → populate [IG-REGISTER] and [ID-REGISTER].**

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

---

### [IG-REGISTER] — Guards

Minimum 2 rows. Each row names the inertia hypothesis, the elimination path with at least one R-ID from [PM-COVERAGE-TABLE], the risk level, and the responsible role.

**STANDARD Elimination Path format**: "R-XX (from [PM-COVERAGE-TABLE]): [reason this requirement closes the gap]."
**AMPLIFIED Elimination Path format (two pre-printed sub-slots — both required independently):**
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the specific entry]
```
A prose instruction without pre-printed sub-slot labels does not satisfy C-32. A combined single-line statement does not satisfy C-32. Each sub-slot must be independently populated.
**WAIVED Elimination Path format (per waiver propagation rule from Phase 1):** "R-ID WAIVED — [functional reason]." Must carry explicit marker; absence of marker means row is not exempt from Condition 2.

| IG-ID | Inertia Hypothesis | Elimination Path (per format above) | Risk | Responsible Role | Mitigation Location |
|-------|-------------------|--------------------------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or status-quo] | [STANDARD / AMPLIFIED sub-slots / WAIVED] | STANDARD / AMPLIFIED | [role] | Design / Constraints / OQ |
| IG-02 | [describe] | [STANDARD / AMPLIFIED sub-slots / WAIVED] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | | | | |

> Responsible Role blank = structural fail.
> AMPLIFIED rows: populate both "Risk:" and "R-ID:" sub-slots independently.
> Row count must equal [ID-REGISTER] row count.

---

### [ID-REGISTER] — Defeats

One row per IG row. Confirming Role must match paired IG-XX Responsible Role.

| ID-ID | Guards | Defeat Condition | Risk Dimension | Confirmation Evidence | Verdict |
|-------|--------|-----------------|----------------|----------------------|---------|
| ID-01 | IG-01 | [condition under which hypothesis is defeated] | [from Risk Signal; "N/A" if STANDARD] | [named spec element — ties to R-ID from [PM-COVERAGE-TABLE]] | DEFEATED / REQUIRES MITIGATION |
| ID-02 | IG-02 | [condition] | [dim or N/A] | [evidence] | DEFEATED / REQUIRES MITIGATION |
| ID-03 | IG-03 (if present) | | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Mismatched counts = structural fail.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF either register is missing; any IG-XX Responsible Role is blank; any ID-XX Confirming Role does not match paired IG-XX; row counts differ; or any AMPLIFIED row's Elimination Path is missing either sub-slot; or [PM-CONTRACT-SEAL] was absent from Phase 1 at time of inertia analysis.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell in [IG-REGISTER] lacks a named R-ID AND does not carry an explicit "R-ID WAIVED" marker. The WAIVED marker is the only valid exemption — it must be present in the cell, propagated from [PM-COVERAGE-TABLE] per the structural waiver propagation rule declared in Phase 1. A cell that is blank, generic, or lacks the explicit WAIVED marker fails Condition 2 regardless of table or register completeness. For AMPLIFIED rows, Condition 2 checks the "R-ID:" sub-slot specifically.
>
> Chain closed: [PM-COVERAGE-TABLE] waiver → [IG-REGISTER] "R-ID WAIVED" marker → Condition 2 exemption here.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: both registers present and row-counts matched (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2).
> Phase 3 is blocked until [INERTIA-ANALYZED] appears.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] → fill pre-assigned rows. Receive [IG-REGISTER] → incorporate mitigations and R-ID traceback. Do not re-enumerate either.**

#### 1. Purpose

State what the feature does, who uses it, and what problem it solves. Name the strongest non-requirements signal influencing this purpose statement and its source artifact.

[Write purpose content]

#### 2. Requirements

**PM: confirm [PM-COVERAGE-TABLE] pre-assigned rows are present below → record per-row coverage.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED / WAIVED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO. Waived rows: {w}.

**Strategy: inspect this section → validate P0 coverage completeness → record inline verdict.**

Strategy inline verdict (Requirements): PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. For each IG-ID with Verdict = REQUIRES MITIGATION, name the design element and the R-ID from [PM-COVERAGE-TABLE] it addresses. For AMPLIFIED rows, name the design element addressing both the risk dimension and the requirement.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | ID-Verdict | Risk | Mitigation Element | R-ID Addressed |
|-------|-----------|------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | STANDARD / AMPLIFIED | [name element or "N/A — DEFEATED"] | [R-XX or "WAIVED" or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | STANDARD / AMPLIFIED | [name element or "N/A — DEFEATED"] | [R-XX or "WAIVED" or "N/A"] |

**Strategy: inspect this section against risk signals → validate design decisions → record inline verdict.**

Strategy inline verdict (Design): PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES MITIGATION and mitigation in Constraints, name the constraint and R-ID it closes.

[List constraints]

**Compliance: inspect this section against `scout-compliance` → validate constraint completeness → record inline verdict.**

Compliance inline verdict: PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 2–3, one per contradiction pair from Phase 1 not resolved, and one per IG-ID with Verdict = REQUIRES MITIGATION not resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions) AND all [PM-COVERAGE-TABLE] P0 rows confirmed in Requirements.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect: inspect sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG-ID mitigation gaps, R-ID Elimination Path gaps (Condition 2), AMPLIFIED sub-slot completeness, waiver chain integrity → fill [FINDINGS-TABLE].**

Scan must cover: IG-ID mitigation completeness; [IG-REGISTER] Elimination Path R-ID cells and AMPLIFIED dual sub-slots; waiver propagation chain (waived [PM-COVERAGE-TABLE] rows → "R-ID WAIVED" in [IG-REGISTER]); Branch B sub-conditions present in Phase 0; [PM-CONTRACT-SEAL] named in Phase 2 REQUIRES header.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — state exactly what was scanned and result; never omit]

> **[SELF-REVIEW-SEAL]**
>
> INVALID IF emitted without [FINDINGS-TABLE] above AND an explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B (sub-condition: B-1/B-2/B-3/B-4) / Normal — state which.
All five sections in order. Frontmatter complete.

---

---

## V-05 — Full Combination — Target 175/175 under v10

**Primary axis**: C-30 + C-31 + C-32 on R9 V-05 full-combination base; all 32 v10 criteria targeted.
**Secondary axes**: C-09 through C-29 (all from R9 V-05) + C-30, C-31, C-32 (new in v10).
**Hypothesis**: All three new criteria compose without conflict into the R9 V-05 full-combination base. C-31 closes the waiver chain (PM-COVERAGE-TABLE waiver → IG-REGISTER "R-ID WAIVED" cell marker → INERTIA-ANALYZED Condition 2 exemption); C-30 adds column-content R-ID checking as a named Condition 2 in [INERTIA-ANALYZED] (upgrading C-21 in the inertia domain); C-32 restructures AMPLIFIED rows into two pre-printed labeled sub-slots ("Risk:" and "R-ID:") that are independently required. All R9 V-05 gate tokens, split registers, CASCADE TO annotations, ordinal location markers, unified declarations, Branch B sub-conditions, and imperative phrasing are preserved intact. Target: 175/175 composite under v10.

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
skill_version: v10
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

Inspect [SCOUT-STATUS-TABLE] to identify which non-requirements artifacts are LOADED. Match exactly one sub-condition below. Do not blend sub-condition copy; emit the matching block verbatim. If multiple sub-conditions apply simultaneously, apply the higher-numbered condition (B-3 over B-1 or B-2). If none of B-1 through B-3 apply, apply B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND, market/stakeholders/positioning/naming any combination:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — the Design section will be driven by feasibility constraints and I'll call out the specific scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND, market/stakeholders/positioning/naming any combination:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec that treats compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and I'll flag each compliance-driven decision explicitly. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on which decisions would shift if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements, feasibility, and compliance all NOT FOUND, at least one of market/stakeholders/positioning/naming LOADED:**

VERBATIM RESPONSE:
> I have some positioning or market signals for this topic but no requirements, feasibility, or compliance data. I can draft a spec from the available context, but coverage will be limited and constraint grounding will rely on the positioning signals. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

HALT after emitting the matching sub-condition block. Do not blend sub-condition copy; emit the matching block verbatim.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [CNS-SLOT-1-OF-2], [CONTRADICTION-SCAN], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE].** CASCADE TO: [IG-REGISTER] Elimination Paths in Phase 2 (R-IDs must be drawn from this table).

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED / C-03 WAIVER |
| R-02 | P0 | [from artifact] | ... | ... | COVERED / C-03 WAIVER |
| ... | | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER for all requirements stated here. All [IG-REGISTER] Elimination Path cells will carry "R-ID WAIVED."

---

**Waiver propagation rule (structural):** Any requirement row carrying "C-03 WAIVER" in the Waiver Status column of [PM-COVERAGE-TABLE] automatically generates an "R-ID WAIVED" marker in the [IG-REGISTER] Elimination Path cell for every IG-ID row that would otherwise reference that requirement. The propagation applies to all affected IG-IDs without per-row judgment. The [INERTIA-ANALYZED] gate token explicitly exempts "R-ID WAIVED" cells from its Condition 2 R-ID population check. Chain: [PM-COVERAGE-TABLE] "C-03 WAIVER" → [IG-REGISTER] Elimination Path "R-ID WAIVED" → [INERTIA-ANALYZED] Condition 2 exemption.

---

**PM: scan `scout-feasibility` AND `scout-compliance` (if LOADED) → identify strongest non-requirements signal → fill [CNS-SLOT-1-OF-2].** CASCADE TO: Purpose section [CNS-SLOT-2-OF-2] in Phase 4 (must match content).

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> If Source artifact is unfilled, C-11 fires at location 1 of 2. This field at location 2 of 2 ([CNS-SLOT-2-OF-2]) must match.

---

**PM: scan `{topic}-requirements-{date}.md` → identify R-ID contradiction pairs → fill [CONTRADICTION-SCAN].** CASCADE TO: Open Questions in Phase 4 if unresolved pairs found.

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}"]

> Do not confirm "none found" without reviewing the requirements artifact. State which rows were inspected.

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated with Waiver Status column (or full C-03 WAIVER stated)
> - Waiver propagation rule declared in this phase block
> - [CNS-SLOT-1-OF-2]: Source artifact cell filled (location 1 of 2)
> - [CONTRADICTION-SCAN]: named scan outcome stating rows inspected
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies all four outputs are present and non-empty in this block.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

**PM: scan `scout-feasibility` AND `scout-compliance` (if LOADED) → record risk level → fill [IG-REGISTER] and [ID-REGISTER].** CASCADE TO: Design section IG-ID mitigation table in Phase 4.

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

---

### [IG-REGISTER] — Guards

Minimum 2 rows. Each row names the inertia hypothesis, the elimination path with at least one R-ID from [PM-COVERAGE-TABLE], the risk level, and the responsible role.

**STANDARD Elimination Path format**: "R-XX (from [PM-COVERAGE-TABLE]): [reason this requirement closes the gap]."

**AMPLIFIED Elimination Path format (two pre-printed sub-slots — both must be independently populated):**

```
Risk: [feasibility constraint or compliance gap — name the specific dimension from scout-feasibility or scout-compliance]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the specific entry]
```

A prose instruction to "name both the risk dimension and R-ID" without pre-printed sub-slot labels does not satisfy C-32. A single combined prose statement naming both elements without labeled sub-slots does not satisfy C-32. Each sub-slot is structurally required — a cell with only "Risk:" populated and "R-ID:" blank is a structural fail at the R-ID sub-slot level. C-29 requires both elements in the AMPLIFIED path — C-32 requires them as independently labeled sub-slots.

**WAIVED Elimination Path format (per waiver propagation rule from Phase 1):** "R-ID WAIVED — [functional reason]." Must carry explicit marker.

| IG-ID | Inertia Hypothesis | Elimination Path (per format) | Risk | Responsible Role | Mitigation Location |
|-------|-------------------|-------------------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or status-quo] | STANDARD: R-XX: [reason] / AMPLIFIED: Risk: [dim] + R-ID: R-XX / WAIVED: R-ID WAIVED — [reason] | STANDARD / AMPLIFIED | [role] | Design / Constraints / OQ |
| IG-02 | [describe] | [per format] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | | | | |

> Responsible Role blank = structural fail.
> AMPLIFIED rows: populate both "Risk:" and "R-ID:" sub-slots independently.
> WAIVED marker must be explicit — absence is not an implicit exemption.
> Row count must equal [ID-REGISTER] row count.

---

### [ID-REGISTER] — Defeats

One row per IG row. Confirming Role must match paired IG-XX Responsible Role.

| ID-ID | Guards | Defeat Condition | Risk Dimension | Confirmation Evidence | Verdict |
|-------|--------|-----------------|----------------|----------------------|---------|
| ID-01 | IG-01 | [condition under which hypothesis is defeated] | [from Risk Signal; "N/A" if STANDARD] | [named spec element — ties to R-ID from [PM-COVERAGE-TABLE]] | DEFEATED / REQUIRES MITIGATION |
| ID-02 | IG-02 | [condition] | [dim or N/A] | [evidence] | DEFEATED / REQUIRES MITIGATION |
| ID-03 | IG-03 (if present) | | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Mismatched counts = structural fail.

---

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (register integrity):** INVALID IF: either register is missing; any IG-XX Responsible Role is blank; any ID-XX Confirming Role does not match paired IG-XX; row counts differ; any AMPLIFIED row's Elimination Path is missing either "Risk:" or "R-ID:" sub-slot; [PM-CONTRACT-SEAL] was not present in Phase 1 at time of inertia analysis.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell in [IG-REGISTER] lacks a named R-ID AND does not carry an explicit "R-ID WAIVED" marker. For STANDARD rows: a generic functional description without a named R-XX reference fails Condition 2. For AMPLIFIED rows: Condition 2 checks the "R-ID:" sub-slot specifically — an empty or absent "R-ID:" sub-slot fails Condition 2 regardless of whether "Risk:" is populated. For WAIVED rows: cells carrying "R-ID WAIVED" (propagated per the structural rule in Phase 1) are explicitly exempted from Condition 2. Absence of the marker is not an implicit exemption.
>
> Chain closed: [PM-COVERAGE-TABLE] "C-03 WAIVER" → [IG-REGISTER] "R-ID WAIVED" marker → Condition 2 exemption here. A template that carries "R-ID WAIVED" in cells but omits the Condition 2 exemption rule fails chain closure — C-30 requires both the column check and the exemption to be declared.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: both registers present, row-counts matched, role columns populated (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID with AMPLIFIED rows carrying both pre-printed sub-slots independently populated (Condition 2).
> Phase 3 is blocked until [INERTIA-ANALYZED] appears.

===== END PHASE 2 =====

---

## ===== PHASE 3: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 4 REQUIRES [STRATEGY-SEAL]

**Strategy: inspect `scout-feasibility` AND `scout-compliance` → validate spec viability against Phase 2 risk levels → fill [STRATEGY-VALIDATION-TABLE].** CASCADE TO: Design and Constraints sections in Phase 4.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | {topic}-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | {topic}-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions from findings | [name artifact] | [list constraints] | — |

> **[STRATEGY-SEAL]**
>
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] above with specific artifact names in all Source Artifact cells.
> [STRATEGY-SEAL] is a proof-of-work artifact. Its presence certifies [STRATEGY-VALIDATION-TABLE] is present and non-empty.

===== END PHASE 3 =====

---

## ===== PHASE 4: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] → fill pre-assigned rows. Receive [IG-REGISTER] → incorporate mitigations and R-ID traceback. Do not re-enumerate either.**

#### 1. Purpose

**PM: inspect [CNS-SLOT-1-OF-2] → verify cross-namespace signal placement at location 2 of 2 → fill [CNS-SLOT-2-OF-2].** CASCADE TO: this section (inline requirement).

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-ID, why spec wins, and which R-ID is the deciding factor] |

> [CNS-SLOT-1-OF-2] is location 1 of 2; [CNS-SLOT-2-OF-2] is location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires. If [CNS-SLOT-1-OF-2] is filled and [CNS-SLOT-2-OF-2] matches, C-10 and C-15 pass.

#### 2. Requirements

**PM: confirm [PM-COVERAGE-TABLE] pre-assigned rows are present below → record per-row coverage.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED / WAIVED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO. Waived rows: {w}.

**Strategy: inspect this section → validate P0 coverage completeness → record inline verdict.**

Strategy inline verdict (Requirements): PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with Verdict = REQUIRES MITIGATION, name the design element and the R-ID from [PM-COVERAGE-TABLE] it addresses. For AMPLIFIED rows, name the design element addressing both the risk dimension (from the "Risk:" sub-slot) and the requirement (from the "R-ID:" sub-slot).

[Write design content]

IG-ID mitigation coverage:
| IG-ID | ID-Verdict | Risk | Mitigation Element | R-ID Addressed |
|-------|-----------|------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | STANDARD / AMPLIFIED | [name element or "N/A — DEFEATED"] | [R-XX or "WAIVED" or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | STANDARD / AMPLIFIED | [name element or "N/A — DEFEATED"] | [R-XX or "WAIVED" or "N/A"] |

**Strategy: inspect this section against [STRATEGY-VALIDATION-TABLE] → validate design decisions → record inline verdict.**

Strategy inline verdict (Design): PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES MITIGATION and mitigation in Constraints, name the constraint and R-ID it closes.

[List constraints]

**Compliance: inspect this section against `scout-compliance` → validate constraint completeness → record inline verdict.**

Compliance inline verdict: PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 2–3, one per contradiction pair from [CONTRADICTION-SCAN] not resolved, and one per IG-ID with Verdict = REQUIRES MITIGATION not resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions) AND [CNS-SLOT-2-OF-2] filled in Purpose AND all [PM-COVERAGE-TABLE] P0 rows confirmed in Requirements.
>
> [SPEC-DRAFT-COMPLETE] is a proof-of-work artifact. Its presence certifies five sections are present in order with required fields populated.

===== END PHASE 4 =====

---

## ===== PHASE 5: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect: inspect sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG-ID mitigation gaps, R-ID Elimination Path gaps, AMPLIFIED sub-slot completeness, waiver chain integrity, CNS slot completeness → fill [FINDINGS-TABLE].**

Scan must cover:
- IG-ID mitigation completeness
- [IG-REGISTER] Elimination Path cells: all non-waived cells contain R-ID (Condition 2 of [INERTIA-ANALYZED])
- [IG-REGISTER] AMPLIFIED rows: both "Risk:" and "R-ID:" sub-slots populated
- Waiver propagation chain: every [PM-COVERAGE-TABLE] C-03 WAIVER row has a corresponding "R-ID WAIVED" marker in [IG-REGISTER]
- [CNS-SLOT-2-OF-2] filled and matches [CNS-SLOT-1-OF-2]
- Branch B sub-conditions present in Phase 0
- [PM-CONTRACT-SEAL] named as gate in Phase 2 REQUIRES header

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — state exactly what was scanned and result; never omit]

> **[SELF-REVIEW-SEAL]**
>
> INVALID IF emitted without [FINDINGS-TABLE] above AND an explicit finding claim referencing [SPEC-DRAFT-COMPLETE] as scan source.

===== END PHASE 5 =====

---

## ===== PHASE 6: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 6 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback applied: Branch A / Branch B (sub-condition: B-1/B-2/B-3/B-4) / Normal — state which.
All five sections in order. Frontmatter complete.
