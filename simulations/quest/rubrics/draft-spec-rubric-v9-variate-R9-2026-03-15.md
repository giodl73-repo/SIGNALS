---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v9
round: R9
date: 2026-03-15
axes_explored: C-28-pm-before-inertia-gate, C-29-elimination-path-inline-rids, C-29-separate-req-column, C-28+C-29-combined-full-base, full-combination-v9
---

# Quest Variate — `draft-spec` — Round 9 (Rubric v9)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-28: PM pre-assignment structurally ordered before inertia via named gate [PM-CONTRACT-SEAL] — minimal base (merged inertia table, no C-22/C-23/C-27) | — | C-28 passes on a minimal REQUIRES/PRODUCES/BLOCKS base without split registers or imperative phrasing; the gate dependency alone (INERTIA ANALYSIS REQUIRES [PM-CONTRACT-SEAL]) is the distinguishing mechanism; C-29 intentionally absent to isolate ordering signal |
| V-02 | C-29: Elimination Path inline R-ID slots in merged inertia table — on V-01 C-28 base | C-28 (from V-01) | C-29 passes when each Elimination Path cell has a structural sub-slot "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]"; the inline format enforces traceability without requiring split registers; AMPLIFIED rows carry a dual requirement (risk dimension + R-ID); C-29 depends on C-28 already passing |
| V-03 | C-29: Separate "Req Closed" column in inertia table — format variant on V-01 C-28 base | C-28 (from V-01) | C-29 satisfies via a dedicated column rather than inline embedding; column format makes R-ID omission structurally visible without reading prose; tests whether column-per-row traceability is a stronger or equivalent implementation vs V-02 inline approach |
| V-04 | C-28+C-29 combined on R8 V-04 base (split registers, C-26 Branch B sub-conditions, C-27 imperative phrasing; no CASCADE TO) | C-22, C-23, C-26, C-27 | C-28 and C-29 compose cleanly with split registers: [IG-REGISTER] gains Elimination Path R-ID column, [ID-REGISTER] keeps its defeat structure; PM-first ordering gates inertia via named [PM-CONTRACT-SEAL] dependency; C-26 and C-27 preserved from R8; no axes from R8 broken |
| V-05 | Full combination — all 29 v9 criteria; target 175/175 | C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29 + all C-09–C-21 | PM-first phase ordering gates inertia (C-28); [IG-REGISTER] Elimination Paths reference pre-assigned R-IDs with AMPLIFIED dual requirement (C-29); all R8 gate tokens with invalidity rules, split registers, CASCADE TO annotations, ordinal location markers, unified declarations, Branch B sub-conditions, and imperative phrasing preserved; 175/175 composite under v9 |

---

## V-01 — Axis: C-28 PM-Before-Inertia Gate (Minimal Base)

**Primary axis**: C-28 — PM pre-assignment phase runs before inertia analysis. The inertia analysis phase's header names [PM-CONTRACT-SEAL] as a gate prerequisite. Base: REQUIRES/PRODUCES/BLOCKS syntax, merged [INERTIA-TABLE] (no C-22/C-23), single Branch B (C-25 present, C-26 absent), no C-27 imperative phrasing.
**Secondary axes**: none.
**Hypothesis**: C-28 passes on the minimal base through gate dependency alone, without split registers or imperative phrasing. C-29 is intentionally absent — Elimination Paths remain generic — isolating C-28 as the single axis.

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
skill_version: v9
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

If `scout-requirements` NOT FOUND: C-03 WAIVER — no requirements artifact loaded. Proceed. P0 coverage criterion waived.

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
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies that [PM-COVERAGE-TABLE] is present and non-empty in this block.
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

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo the model might default to] | [why it fails to satisfy the spec need; if AMPLIFIED, explicitly address the risk dimension] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension. A generic functional elimination does not satisfy.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies [INERTIA-TABLE] is present and non-empty in this block.
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

Describe architecture, components, and key technical decisions. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element that addresses it.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element |
|-------|---------|-------------------|
| IG-01 | [from [INERTIA-TABLE]] | [name element, or "N/A — ELIMINATED"] |
| IG-02 | [from [INERTIA-TABLE]] | [name element, or "N/A — ELIMINATED"] |

Secondary role validation (Design): Strategy — PASS / FINDING: [describe, citing source artifact if FINDING]

#### 4. Constraints

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION and mitigation assigned to Constraints, name the constraint.

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

Scan sections 1–5 for: contradictions, gaps, ambiguities, hotspots, IG-ID mitigation gaps.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — state "none found" if scan reveals no issues, but never omit]

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

## V-02 — Axis: C-29 Elimination Path Inline R-ID Slots (on V-01 base)

**Primary axis**: C-29 — each Elimination Path cell in [INERTIA-TABLE] carries a mandatory "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" sub-slot. When Risk Signal = AMPLIFIED, the cell must name both the risk dimension and at least one R-ID.
**Secondary axes**: C-28 (from V-01 — PM pre-assignment gates inertia analysis).
**Hypothesis**: C-29 passes via inline embedding of R-IDs in the Elimination Path column. The sub-slot format makes omission visible: a cell that does not name an R-ID is structurally incomplete. AMPLIFIED rows carry a dual requirement. C-28 is a prerequisite — PM-first ordering is what makes R-IDs available when inertia rows are filled.

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
skill_version: v9
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

If `scout-requirements` NOT FOUND: C-03 WAIVER — no requirements artifact loaded. Proceed. P0 coverage criterion waived. Note: [INERTIA-TABLE] Elimination Path R-ID slots will be left blank with a stated waiver in each row.

---

Cross-namespace signal:

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

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When Risk Signal = AMPLIFIED, the cell must also name the specific risk dimension from `scout-feasibility` or `scout-compliance` before the R-ID reference. Example: "AMPLIFIED: feasibility constraint [score] — R-03 (assigned to Design: retry-backoff component) closes this gap." A generic functional description without a named R-ID does not satisfy. If C-03 WAIVER applies, state "R-ID WAIVED (no requirements artifact)" in the cell.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | R-ID: R-XX (from [PM-COVERAGE-TABLE]) — [why this requirement closes the gap; if AMPLIFIED, name risk dimension first] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | R-ID: R-XX — [reason] | | | |

> A blank or generic Elimination Path cell (no R-ID named) is a structural fail for that row.
> AMPLIFIED rows require: risk dimension named + at least one R-ID. Either element absent is a row-level fail.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated, including R-ID references in each Elimination Path cell (or stated C-03 WAIVER).
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies [INERTIA-TABLE] is present, non-empty, and R-ID references are populated.
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
> INVALID IF emitted without all five guided sections present in order.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

Scan must cover: IG-ID mitigation completeness; R-ID Elimination Path cells in [INERTIA-TABLE] (any blank cells); Phase 0 fallback branches present; cross-namespace signal named in Purpose.

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

## V-03 — Axis: C-29 Separate "Req Closed" Column Format (on V-01 base)

**Primary axis**: C-29 — [INERTIA-TABLE] carries a dedicated "Req Closed (from [PM-COVERAGE-TABLE])" column, separate from the Elimination Path prose column. Each row names the R-ID in that column; the Elimination Path column carries the functional reason without embedding R-IDs inline.
**Secondary axes**: C-28 (from V-01 — PM pre-assignment gates inertia analysis).
**Hypothesis**: C-29 satisfies via column separation rather than inline embedding. The dedicated column makes R-ID omission visually immediate — a blank cell in a named column is harder to overlook than a missing sub-slot in prose. Tests whether structural column placement is a stronger implementation axis than V-02's inline format.

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
skill_version: v9
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

HALT until context provided.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

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
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here.

---

Cross-namespace signal:

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Contradiction scan: inspect all P0 rows. Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated).
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score: [record or "NOT LOADED"]
- Compliance status: [record or "NOT LOADED"]
- Risk level: STANDARD / AMPLIFIED

### [INERTIA-TABLE]

**Column instructions**:
- *Elimination Path*: functional reason the hypothesis is eliminated by this spec's design — prose, no R-IDs here
- *Req Closed (from [PM-COVERAGE-TABLE])*: name at least one R-ID (e.g., "R-03") from [PM-COVERAGE-TABLE] that this spec satisfies where the inertia hypothesis would not; leave blank only if C-03 WAIVER applies (state "WAIVED")
- *Risk Signal*: STANDARD or AMPLIFIED; if AMPLIFIED, also note the risk dimension in Elimination Path

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Req Closed (from [PM-COVERAGE-TABLE]) | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|---------------------------------------|--------------------------|---------|
| IG-01 | [existing alternative or status-quo] | [why spec satisfies what hypothesis cannot — name risk dimension if AMPLIFIED] | STANDARD / AMPLIFIED | R-XX [1-phrase label] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [reason] | STANDARD / AMPLIFIED | R-XX | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | | |

> Req Closed column blank (without WAIVER) = structural fail for that row.
> AMPLIFIED rows: Elimination Path must name risk dimension; Req Closed still required.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] with all Req Closed cells populated (or WAIVER stated) and all IG-ID rows complete.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

#### 1. Purpose

[Write purpose content — name strongest non-requirements signal and source artifact]

#### 2. Requirements

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.
Secondary role validation: [role name] — PASS / FINDING: [describe]

#### 3. Design

[Write design content — reference IG-ID mitigations and Req Closed IDs from [INERTIA-TABLE]]

Secondary role validation (Design): Strategy — PASS / FINDING: [describe]

#### 4. Constraints

[List constraints with source artifact names]

Secondary role validation (Constraints): Compliance — PASS / FINDING: [describe]

#### 5. Open Questions

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five sections in order.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Scan must cover: Req Closed column completeness in [INERTIA-TABLE]; IG-ID mitigation coverage in Design; P0 coverage count accuracy; fallback branches present in Phase 0.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |

Finding claim: [explicit scan outcome]

> **[SELF-REVIEW-SEAL]** — INVALID IF emitted without [FINDINGS-TABLE] or explicit finding claim.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write to `simulations/draft/specs/{topic}-spec-{date}.md`. Frontmatter complete. All five sections in order. Gate tokens: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].

---

---

## V-04 — C-28+C-29 Combined (R8 V-04 base: split registers, C-26, C-27)

**Primary axis**: C-28 + C-29 combined on R8 V-04 full base (split [IG-REGISTER]/[ID-REGISTER] preserving C-22; Responsible Role column C-23; Branch B sub-conditions C-26; imperative phrasing C-27; no CASCADE TO C-24).
**Secondary axes**: C-22, C-23, C-26, C-27 (all from R8 V-04 base).
**Hypothesis**: C-28 and C-29 compose with split registers without axis conflict. [IG-REGISTER] carries hypothesis + Elimination Path columns (with R-IDs), [ID-REGISTER] carries defeat + risk + mitigation + verdict. PM-first ordering gates inertia via [PM-CONTRACT-SEAL] in INERTIA ANALYSIS REQUIRES header. C-26 Branch B sub-conditions and C-27 imperative directives are preserved throughout. No C-24 CASCADE TO — this tests whether C-28+C-29 compose without requiring the cascade annotation.

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
skill_version: v9
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

HALT. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

Inspect [SCOUT-STATUS-TABLE] to identify which non-requirements artifacts are LOADED. Match exactly one sub-condition below. Do not blend sub-condition copy; emit the matching block verbatim. If multiple sub-conditions apply simultaneously (e.g., both B-1 and B-2), apply B-3. If none of B-1 through B-3 apply, apply B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — the Design section will be driven by feasibility constraints and I'll call out the specific scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec that treats compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and I'll flag each compliance-driven decision explicitly. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on which decisions would shift if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements, feasibility, and compliance all NOT FOUND, but at least one of market / stakeholders / positioning / naming LOADED:**

VERBATIM RESPONSE:
> I have some positioning or market signals for this topic but no requirements, feasibility, or compliance data. I can draft a spec from the available context, but coverage will be limited and constraint grounding will rely on the positioning signals. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

HALT after emitting the matching sub-condition block. Do not blend sub-condition copy.

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

**PM: scan `{topic}-requirements-{date}.md` → enumerate P0 requirements → fill [PM-COVERAGE-TABLE].**

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Proceed. Note: [IG-REGISTER] Elimination Path R-ID cells will carry "R-ID WAIVED" in all rows.

---

**PM: scan `scout-feasibility` and `scout-compliance` → identify strongest non-requirements signal → fill [CNS-SLOT-1-OF-2].**

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> If Source artifact is unfilled, C-11 fires at location 1 of 2.

---

**PM: scan `{topic}-requirements-{date}.md` → identify R-ID contradiction pairs → fill [CONTRADICTION-SCAN].**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}"]

> Do not confirm "none found" without reviewing the requirements artifact. State which rows were inspected.

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated (or C-03 waiver)
> - [CNS-SLOT-1-OF-2]: Source artifact cell filled
> - [CONTRADICTION-SCAN]: named scan outcome stating rows inspected
>
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies all three outputs present and non-empty.
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

**PM: scan `scout-feasibility` and `scout-compliance` → record risk level → fill [IG-REGISTER] and [ID-REGISTER].**

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

---

### [IG-REGISTER] — Guards

Minimum 2 rows. Elimination Path must reference at least one R-ID from [PM-COVERAGE-TABLE] per row.

**Elimination Path format**: "R-XX (from [PM-COVERAGE-TABLE]): [reason this requirement closes the gap this inertia hypothesis cannot satisfy]." When Risk Signal = AMPLIFIED: prepend "AMPLIFIED: [risk dimension] — " before the R-ID reference. A generic elimination without a named R-ID is a structural fail for that row. C-03 WAIVER rows: state "R-ID WAIVED — [functional reason]."

| IG-ID | Inertia Hypothesis | Elimination Path (must include R-ID) | Risk | Responsible Role | Mitigation Location |
|-------|-------------------|--------------------------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or status-quo alternative] | R-XX: [reason; if AMPLIFIED prepend risk dim] | STANDARD / AMPLIFIED | [PM / Strategy / Compliance / Design / Architect] | Design / Constraints / Open Questions |
| IG-02 | [lazy default] | R-XX: [reason] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | R-XX: [reason] | | | |

> Responsible Role blank = structural fail for this row.
> AMPLIFIED rows: risk dimension + R-ID both required in Elimination Path.

---

### [ID-REGISTER] — Defeats

One row per IG row. Confirming Role must match paired IG-XX Responsible Role.

| ID-ID | Guards | Defeat Condition | Risk Dimension | Confirmation Evidence | Verdict |
|-------|--------|-----------------|----------------|----------------------|---------|
| ID-01 | IG-01 | [condition under which the inertia hypothesis is defeated] | [from Risk Signal; "N/A" if STANDARD] | [named evidence from spec] | DEFEATED / REQUIRES MITIGATION |
| ID-02 | IG-02 | [condition] | [risk dim or N/A] | [evidence] | DEFEATED / REQUIRES MITIGATION |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Mismatched counts = structural fail.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF: either register is missing; any IG-XX Elimination Path has no R-ID (without WAIVER); any IG-XX Responsible Role is blank; row counts differ; any AMPLIFIED row's Elimination Path lacks risk dimension.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies both registers are present, non-empty, R-ID references populated, and row counts matched.
> Phase 3 is blocked until [INERTIA-ANALYZED] appears.

===== END PHASE 2 =====

---

## ===== PHASE 3: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 4 REQUIRES [STRATEGY-SEAL]

**Strategy: inspect `scout-feasibility` and `scout-compliance` → validate spec viability → fill [STRATEGY-VALIDATION-TABLE].**

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | {topic}-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | {topic}-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list new constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] above with specific artifact names in all Source Artifact cells.

===== END PHASE 3 =====

---

## ===== PHASE 4: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect: receive [PM-COVERAGE-TABLE] and fill pre-assigned rows. Receive [IG-REGISTER] and incorporate mitigations. Do not re-enumerate either.**

#### 1. Purpose

**PM: inspect [CNS-SLOT-1-OF-2] → verify cross-namespace signal placement at location 2 of 2 → fill [CNS-SLOT-2-OF-2].**

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-ID and why spec wins — reference IG-ID by number and R-ID] |

> If [CNS-SLOT-2-OF-2] is blank, C-11 fires at location 2 of 2.

#### 2. Requirements

**PM: confirm [PM-COVERAGE-TABLE] pre-assigned rows are placed below.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

Secondary role validation (Requirements): [role name] — PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with Verdict = REQUIRES MITIGATION, name the design element and the R-ID it addresses.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element | R-ID Addressed |
|-------|---------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | [name or "N/A"] | [R-XX or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | [name or "N/A"] | [R-XX or "N/A"] |

**Strategy: inspect this section against [STRATEGY-VALIDATION-TABLE] → validate design decisions → record verdict inline.**

Strategy inline verdict: PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names.

[List constraints]

**Compliance: inspect this section against `scout-compliance` → validate constraint completeness → record verdict inline.**

Compliance inline verdict: PASS / FINDING: [describe]

#### 5. Open Questions

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five sections in order.

===== END PHASE 4 =====

---

## ===== PHASE 5: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect: inspect sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG-ID mitigation gaps, R-ID Elimination Path gaps → fill [FINDINGS-TABLE].**

Scan must cover: IG-ID mitigation completeness; [CNS-SLOT-2-OF-2] filled; Branch B sub-conditions present; R-ID references in all [IG-REGISTER] Elimination Path cells.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] OR explicit finding claim referencing [SPEC-DRAFT-COMPLETE] as scan source.

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
Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback: Branch A with VERBATIM block; Branch B with sub-conditions B-1 through B-4 each with own VERBATIM block; Normal branch. State which applied.
All five sections in order. [CNS-SLOT-1-OF-2] and [CNS-SLOT-2-OF-2] both filled. Frontmatter complete.

---

---

## V-05 — Full Combination — Target 175/175 under v9

**Primary axis**: C-28 + C-29 on R8 V-05 full-combination base; all 29 v9 criteria targeted.
**Secondary axes**: C-22, C-23, C-24, C-25, C-26, C-27 (from R8 V-05) + C-28, C-29 (new in v9).
**Hypothesis**: All three axes compose without conflict. PM-first ordering gates inertia via [PM-CONTRACT-SEAL] (C-28); [IG-REGISTER] Elimination Paths reference pre-assigned R-IDs with AMPLIFIED dual requirement (C-29); split [IG-REGISTER]/[ID-REGISTER] preserves C-22/C-23; CASCADE TO annotations on unified declarations preserved (C-24); Branch B sub-conditions with anti-blend preserved (C-26); imperative actor-action-output directives throughout (C-27); ordinal location markers "location 1 of 2 / 2 of 2" on [CNS-SLOT] fields (C-19); gate token invalidity rules on all gate artifacts (C-21); unified role-and-source declarations with CASCADE TO (C-20/C-24). Target: 175/175 composite under v9.

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
skill_version: v9
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

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. [IG-REGISTER] Elimination Path R-ID cells will carry "R-ID WAIVED" in all rows.

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
> - [PM-COVERAGE-TABLE]: P0 rows populated (or C-03 waiver)
> - [CNS-SLOT-1-OF-2]: Source artifact cell filled (location 1 of 2)
> - [CONTRADICTION-SCAN]: named scan outcome stating rows inspected
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

**PM: scan `scout-feasibility` AND `scout-compliance` (if LOADED) → record risk level → fill [IG-REGISTER] and [ID-REGISTER].** CASCADE TO: Design section IG-ID mitigation table in Phase 4.

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

---

### [IG-REGISTER] — Guards

Minimum 2 rows. Each row names the inertia hypothesis, the elimination path with at least one R-ID from [PM-COVERAGE-TABLE], the risk level, and the responsible role.

**Elimination Path format**: "R-XX (from [PM-COVERAGE-TABLE]): [reason this requirement closes the gap the hypothesis cannot satisfy]." When Risk Signal = AMPLIFIED: "AMPLIFIED: [risk dimension] — R-XX: [reason]." Generic elimination without a named R-ID is a structural fail. C-03 WAIVER rows: "R-ID WAIVED — [functional reason]."

| IG-ID | Inertia Hypothesis | Elimination Path (R-ID required) | Risk | Responsible Role | Mitigation Location |
|-------|-------------------|----------------------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or status-quo] | R-XX: [reason; AMPLIFIED prepends risk dim] | STANDARD / AMPLIFIED | [role] | Design / Constraints / OQ |
| IG-02 | [describe] | R-XX: [reason] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | R-XX: [reason] | | | |

> Responsible Role blank = structural fail.
> AMPLIFIED rows: Elimination Path must name both risk dimension and R-ID.
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
> INVALID IF: either register is missing; any IG-XX Elimination Path has no R-ID (without WAIVER); any IG-XX Responsible Role is blank; any ID-XX Confirming Role does not match paired IG-XX; row counts differ; any AMPLIFIED row's Elimination Path lacks risk dimension; [PM-CONTRACT-SEAL] was not present in Phase 1 at time of inertia analysis.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies both registers are present, non-empty, R-ID references populated, row counts matched, and Phase 1 [PM-CONTRACT-SEAL] was the gate that authorized this phase.
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
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: YES / NO.

**Strategy: inspect this section → validate P0 coverage completeness → record inline verdict.**

Strategy inline verdict (Requirements): PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with Verdict = REQUIRES MITIGATION, name the design element and the R-ID from [PM-COVERAGE-TABLE] it addresses.

[Write design content]

IG-ID mitigation coverage:
| IG-ID | ID-Verdict | Mitigation Element | R-ID Addressed |
|-------|-----------|-------------------|----------------|
| IG-01 | [from [ID-REGISTER]] | [name element or "N/A — DEFEATED"] | [R-XX from [PM-COVERAGE-TABLE] or "N/A"] |
| IG-02 | [from [ID-REGISTER]] | [name element or "N/A — DEFEATED"] | [R-XX or "N/A"] |

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

**Architect: inspect sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG-ID mitigation gaps, R-ID Elimination Path gaps, and CNS slot completeness → fill [FINDINGS-TABLE].**

Scan must cover: IG-ID mitigation completeness; [CNS-SLOT-2-OF-2] filled; all [IG-REGISTER] Elimination Path R-ID cells non-blank (or WAIVER); Branch B sub-conditions present in Phase 0; [PM-CONTRACT-SEAL] listed as gate in Phase 2 REQUIRES header.

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

Gate tokens in document: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].

Fallback: Branch A (ALL NOT FOUND) with VERBATIM block; Branch B (requirements absent, others loaded) with sub-conditions B-1 through B-4 each with own VERBATIM block and anti-blend instruction; Normal branch. State which applied.

All five sections in order. [CNS-SLOT-1-OF-2] (location 1 of 2, Phase 1) and [CNS-SLOT-2-OF-2] (location 2 of 2, Purpose section) both filled. Frontmatter complete. [PM-CONTRACT-SEAL] named in Phase 2 REQUIRES header as the PM-first gate.
