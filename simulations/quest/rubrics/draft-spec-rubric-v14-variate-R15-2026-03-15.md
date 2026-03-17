---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v14
round: R15
date: 2026-03-15
axes_explored: output-format-dd-register, inertia-framing-status-quo-snapshot-anchor, role-sequence-architect-coleads-phase1, dd-register+status-quo-snapshot+phase-1.5, full-synthesis-all-five-axes
---

# Quest Variate — `draft-spec` — Round 15 (Rubric v14)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Output format — Phase 3 Design section replaced by structured [DD-REGISTER] with DD-ID, Decision, R-ID Coverage, Trade-off, Architect Note columns; DD-register completeness rule (blank R-ID Coverage = structural fail) | C-41, C-42, C-43 universal baseline | DD-register is criterion-neutral for all governance criteria; C-05 passes because five guided sections remain in prescribed order with Design present in register form; C-27 passes because actor→action directives unchanged; C-41/C-42/C-43 all satisfied; C-36/C-37/C-38/C-39/C-40 N/A (no STATUS-QUO-SNAPSHOT, no Phase 1.5); expected composite: 30/35 aspirational |
| V-02 | Inertia framing — [STATUS-QUO-SNAPSHOT] as Phase 2 opening block before [IG-REGISTER]; each snapshot row names the competing alternative, gap, and why the alternative does not scale; [INERTIA-ANALYZED] Condition 1 extended to require [STATUS-QUO-SNAPSHOT] presence (C-36); structural fail rule co-located with snapshot row definition (C-37) | C-41, C-42, C-43 universal baseline | STATUS-QUO-SNAPSHOT activates C-36 and C-37; with C-41/C-42/C-43 also satisfied, expected composite: 32/35 aspirational; C-38/C-39/C-40 N/A (no Phase 1.5) |
| V-03 | Role sequence — Architect co-active from Phase 1 entry; → ROLE: PM + ARCHITECT at Phase 1 entry; Architect scans feasibility and compliance artifacts in Phase 1 while PM handles requirements assignment; Phase 1 emits [PM-CONTRACT-SEAL] after both complete | C-41, C-42 universal baseline | C-43 condition (1) requires Phase 1 single-actor marker (→ ROLE: PM); V-03 intentionally violates this by co-assigning Architect at Phase 1, producing C-43 = FAIL; this surfaces the rubric's embedded role-ordering assumption; all other criteria unaffected; expected composite: 29/35 aspirational (C-43 = fail, C-36/C-37/C-38/C-39/C-40 N/A) |
| V-04 | Combined: V-01 DD-register output format + V-02 STATUS-QUO-SNAPSHOT inertia framing + Phase 1.5 STRATEGY INERTIA SCOPING emitting [STRATEGY-SCOPE-SEAL] + dual-token Phase 2 gate + [STRATEGY-SCOPE-SEAL] cross-references STATUS-QUO-SNAPSHOT structural fail rule (C-40) | C-41, C-42, C-43 universal baseline | DD-register is criterion-neutral across C-36/C-37/C-38/C-39/C-40; all five extension criteria pass; with C-41/C-42/C-43 also satisfied: 35/35 aspirational; composite 175/175 |
| V-05 | Combined: V-01 DD-register + V-02 STATUS-QUO-SNAPSHOT + V-03 Architect co-leads Phase 1 + Phase 1.5 + dual-token gate + C-41/C-42 throughout | C-43 intentionally re-examined: Phase 1 multi-actor marker vs C-43 condition (1) boundary | V-03 role sequence is C-43-incompatible; full synthesis with V-03 achieves 34/35 aspirational (C-43 = fail) and 35/35 for all other extension criteria; tests whether maximum feature coverage at cost of C-43 is preferable to C-43-compliant V-04; expected composite: ~174.6/175 |

---

## V-01 — Axis: Output Format (Design Decisions Register)

**Primary axis**: Output format — Phase 3 Design section uses a structured [DD-REGISTER] (Design Decisions register) instead of prose narrative. Each design decision is a named, numbered row with columns: DD-ID, Decision, R-ID Coverage, Trade-off, Architect Note. A DD-register completeness rule names blank R-ID Coverage as a structural fail. This replaces the ad-hoc "name at least one design element per P0 requirement" prose instruction with a traceable register pattern consistent with [IG-REGISTER] and [PM-COVERAGE-TABLE].

**Hypothesis**: DD-register is criterion-neutral for all governance criteria. C-05 passes because the five guided sections remain in prescribed order with Design present in register form. C-27 passes because actor→action directives are unchanged. C-41/C-42/C-43 all satisfied via universal baseline. C-36/C-37/C-38/C-39/C-40 N/A (no STATUS-QUO-SNAPSHOT, no Phase 1.5). Expected composite: 30/35 aspirational.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter (hard fail if any field missing):
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v14
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ ROLE: ARCHITECT

ENTER:
- File system access to `simulations/scout/` available
- Topic and date defined; session initialized

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate [SCOUT-STATUS-TABLE] with every row before proceeding.

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

HALT until user confirms. Do not blend with B-2 or B-3 copy; emit this block verbatim.

**B-2: Compliance artifact loaded, feasibility NOT FOUND**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec using the compliance posture I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend with B-1 or B-3 copy; emit this block verbatim.

**B-3: Both feasibility and compliance loaded**

VERBATIM RESPONSE:
> I have feasibility and compliance signals for this topic but no requirements artifact. I can write a spec using both signals, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms. Do not blend with B-1 or B-2 copy; emit this block verbatim.

**B-catch: Any other combination**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**Anti-blend instruction**: Identify the matching branch and emit its VERBATIM RESPONSE block without modification. Do not combine copy from multiple branches.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

EXIT:
- [SCOUT-STATUS-TABLE] complete; all seven artifact rows populated
- Fallback branch selected (A / B-1 / B-2 / B-3 / B-catch / Normal)
- Phases 1 through FINDINGS blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ ROLE: PM

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

You are now entering the pre-assignment phase. Your goal is to scan the requirements artifact and assign every P0 requirement to a named spec section before any inertia analysis begins.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). Named structural element — a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. [INERTIA-ANALYZED] Condition 2 explicitly exempts cells marked "R-ID WAIVED."

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` → name any conflicting R-ID pairs (e.g., "R-06 vs R-10") → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

EXIT:
- [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 WAIVER stated) and Waiver Status column as named structural element
- Contradiction scan complete; conflicts recorded or absence stated with named range
- Cross-namespace signal row populated (or "none loaded" stated)

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Phase 2 is blocked until this token is present.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

You are now entering inertia analysis. Your goal is to identify what teams, tools, and habits already exist that could substitute for this feature — and prove that each alternative is insufficient.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When C-03 WAIVER applies, mark the cell `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [describe existing alternative or status-quo] | R-ID: R-XX — [reason; if AMPLIFIED, use sub-slot format] | STANDARD / AMPLIFIED [cite trigger] |
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

EXIT:
- [IG-REGISTER] present; minimum 2 rows populated
- [ID-REGISTER] present; all IG-IDs have Verdict
- Every non-waived Elimination Path cell contains a named R-ID

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
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ ROLE: ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

You are now authoring the specification. Five sections must appear in prescribed order. Your goal is a document any engineer can implement without ambiguity.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

State what this feature does in 2–4 sentences. Name the primary user, the core workflow enabled, and the business value.

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [copy source artifact and signal from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row below → confirm P0 coverage count before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}). "All requirements covered" without a named scan range does not satisfy.

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

You will now produce the design as a structured [DD-REGISTER]. Each row names one design decision. Every P0 requirement assigned to this section must appear in at least one DD row's R-ID Coverage column. A P0 requirement assigned here with no corresponding DD row is a gap — flag it in FINDINGS.

### [DD-REGISTER] — Design Decisions

| DD-ID | Decision | R-ID Coverage | Trade-off | Architect Note |
|-------|----------|---------------|-----------|----------------|
| DD-01 | [name the design decision — e.g., "Use event-driven state machine for lifecycle transitions"] | R-XX, R-YY | [what is given up by this choice; name the alternative considered] | [additional constraint or implementation note] |
| DD-02 | [next decision] | R-XX | [trade-off] | [note] |
| DD-03 | [add as needed] | | | |

**DD-register completeness rule**: A DD row with a named decision but a blank R-ID Coverage column is a structural fail, not a content gap. Every DD row must name at least one R-ID.

---

### 4. Constraints

List non-negotiable implementation constraints. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, include a named constraint or open question traceable to that IG-ID.

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

List unresolved issues that block or risk the spec.

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |
| OQ-02 | | | |

---

EXIT:
- All five guided sections present in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)
- [DD-REGISTER] present with at least two rows; every Design-assigned P0 requirement has a named DD row with R-ID Coverage
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present in this document
- Cross-namespace signal at both locations when a non-requirements artifact was LOADED

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Your goal is to identify specific gaps and surface the amendments that would close them. Produce a minimum of two actionable items.

Amendment list (minimum 2 — name the target section and the change for each):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Your final task is a self-review scan. Verify each item below before writing any finding.

Self-review scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 (names [IG-REGISTER], [ID-REGISTER]) and Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)
- [DD-REGISTER] present; every DD row has named R-ID Coverage

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-02 — Axis: Inertia Framing (STATUS-QUO-SNAPSHOT as Phase 2 Anchor)

**Primary axis**: Inertia framing — [STATUS-QUO-SNAPSHOT] is the opening block of Phase 2, preceding [IG-REGISTER]. Each snapshot row names the competing alternative (what teams use today), its gap (why it does not scale), and the transition cost (what changes when this feature replaces it). The inertia analysis reads as "what we are replacing and why" rather than "risks and mitigations." [INERTIA-ANALYZED] Condition 1 is extended to require [STATUS-QUO-SNAPSHOT] presence. A structural fail rule is co-located with the [STATUS-QUO-SNAPSHOT] row definition.

**Hypothesis**: STATUS-QUO-SNAPSHOT activates C-36 ([INERTIA-ANALYZED] Condition 1 extended to snapshot presence) and C-37 (structural fail rule co-located with row definition). With C-41/C-42/C-43 also satisfied, expected composite: 32/35 aspirational. C-38/C-39/C-40 N/A (no Phase 1.5).

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter (hard fail if any field missing):
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v14
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ ROLE: ARCHITECT

ENTER:
- File system access to `simulations/scout/` available
- Topic and date defined; session initialized

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate [SCOUT-STATUS-TABLE] before proceeding.

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

**B-1: Feasibility artifact loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

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

**Anti-blend instruction**: Identify the matching branch and emit its VERBATIM RESPONSE block without modification. Do not combine copy from multiple branches.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

EXIT:
- [SCOUT-STATUS-TABLE] complete; all seven artifact rows populated
- Fallback branch selected (A / B-1 / B-2 / B-3 / B-catch / Normal)
- Phases 1 through FINDINGS blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ ROLE: PM

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

You are now entering the pre-assignment phase. Your goal is to scan the requirements artifact and assign every P0 requirement to a named spec section before any inertia analysis begins.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` or `C-03 WAIVER`. Named structural element.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells. [INERTIA-ANALYZED] Condition 2 explicitly exempts cells marked "R-ID WAIVED."

If `scout-requirements` NOT FOUND: C-03 WAIVER stated. Each [PM-COVERAGE-TABLE] row carries `C-03 WAIVER` in Waiver Status.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` → name any conflicting R-ID pairs → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

EXIT:
- [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 WAIVER stated) and Waiver Status column as named structural element
- Contradiction scan complete; conflicts recorded or absence stated with named range
- Cross-namespace signal row populated (or "none loaded" stated)

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> Phase 2 is blocked until this token is present.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

You are now entering inertia analysis. Your goal is to name what already exists that teams could use instead of this feature, explain exactly why each alternative fails at scale, and record those failures as the foundation for spec requirements.

---

### [STATUS-QUO-SNAPSHOT]

Name each competing alternative the team is currently using or could plausibly use. For each, state the gap — the specific capability it lacks that this feature provides — and the transition cost.

**Structural fail rule**: A row with a named alternative but a blank Gap statement is a structural fail, not a content gap. Do not leave Gap blank when Alternative is populated.

| Alt-ID | Alternative (what teams use today) | Gap (why it does not scale or satisfy) | Transition Cost |
|--------|-----------------------------------|----------------------------------------|-----------------|
| ALT-01 | [name the existing tool, workflow, or manual process] | [specific capability this alternative lacks] | [what changes when this feature replaces it] |
| ALT-02 | [another alternative] | [gap] | [cost] |

---

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Each IG-ID should correspond to or extend an ALT-ID row above. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap.

**AMPLIFIED Elimination Path sub-slot format**:
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: A cell with "Risk:" populated and "R-ID:" blank is a structural fail. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [describe existing alternative — reference ALT-ID where applicable] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | [add if applicable] | | | |

---

### [ID-REGISTER] — Inertia Decision Register

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named constraint or open question, if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

---

EXIT:
- [STATUS-QUO-SNAPSHOT] present; minimum 2 ALT-ID rows populated; structural fail rule co-located
- [IG-REGISTER] present; minimum 2 rows populated
- [ID-REGISTER] present; all IG-IDs have Verdict
- Every non-waived Elimination Path cell contains a named R-ID

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path → Condition 2 exemption declared above.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ ROLE: ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

You are now authoring the specification. Five sections must appear in prescribed order. Your goal is a document any engineer can implement without ambiguity.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [copy source artifact and signal from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row → confirm P0 coverage count before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name] | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

Architect: write requirements narrative from pre-assigned rows. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned here, include a named design element that satisfies it. If a P0 requirement has no corresponding design element after writing, flag it as a gap in FINDINGS.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed to close it] |

---

EXIT:
- All five guided sections present in prescribed order
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present in this document
- Cross-namespace signal at both locations when a non-requirements artifact was LOADED

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Your goal is to identify specific gaps surfaced in Phase 3 and produce actionable amendments.

1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Your final task is a self-review scan. Verify each item below before writing any finding.

Self-review scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 extended to [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]
- [STATUS-QUO-SNAPSHOT] present; structural fail rule co-located
- Cross-namespace signal at both locations
- All AMPLIFIED rows carry both sub-slots (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-03 — Axis: Role Sequence (Architect Co-leads Phase 1)

**Primary axis**: Role sequence — Architect is co-active from Phase 1 entry alongside PM. → ROLE: PM + ARCHITECT at Phase 1 entry. PM handles requirements assignment to spec sections; Architect simultaneously scans feasibility and compliance artifacts to surface design constraints that should inform the PM-COVERAGE-TABLE assignments. Both actors must complete before [PM-CONTRACT-SEAL] is emitted.

**Hypothesis**: C-43 condition (1) requires a single-actor marker at Phase 1 (→ ROLE: PM). V-03 intentionally violates this by placing both roles at Phase 1 entry. This surfaces the rubric's embedded role-ordering assumption: Phase 1 is structurally reserved for PM-only governance. All other criteria unaffected. Expected composite: 29/35 aspirational (C-43 = FAIL; C-36/C-37/C-38/C-39/C-40 N/A).

**Discovery target**: Confirm C-43 condition (1) is a strict ordering rule, not just a labeling rule. Determine whether a "PM leads, Architect consults" co-assignment pattern in Phase 1 could satisfy condition (1) if the ROLE marker names PM as primary.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter (hard fail if any field missing):
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v14
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ ROLE: ARCHITECT

ENTER:
- File system access to `simulations/scout/` available
- Topic and date defined; session initialized

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate [SCOUT-STATUS-TABLE] before proceeding.

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

**B-1: Feasibility artifact loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

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

**Anti-blend instruction**: Identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

EXIT:
- [SCOUT-STATUS-TABLE] complete; all seven artifact rows populated
- Fallback branch selected
- Phases 1 through FINDINGS blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

You are now entering a joint pre-assignment phase. PM and Architect both contribute: PM assigns requirements to spec sections; Architect extracts design constraints from any loaded feasibility and compliance signals that should inform those assignments.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section.**

**Architect: scan `scout-feasibility` and `scout-compliance` (if LOADED) → record design constraints that affect section assignments → flag any P0 requirement whose assigned section may be under-specified given feasibility or compliance signals.**

Design constraint intake (Architect):

| Constraint Source | Artifact | Constraint | Affected R-IDs |
|-------------------|----------|-----------|----------------|
| [feasibility / compliance / none] | [artifact name or "NOT LOADED"] | [1-sentence constraint] | [R-XX, R-YY or "—"] |

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE]

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |

**Waiver Status column**: enumerated values are `COVERED` or `C-03 WAIVER`. Named structural element.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Paths. [INERTIA-ANALYZED] Condition 2 exempts cells marked "R-ID WAIVED."

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows → name any conflicting R-ID pairs → or state "none found after scanning R-01 through R-{n}."

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

EXIT:
- [PM-COVERAGE-TABLE] present; P0 rows assigned; Waiver Status column named
- Design constraint intake complete (Architect)
- Contradiction scan complete
- Cross-namespace signal row populated (or "none loaded")

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> Phase 2 is blocked until this token is present.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

You are now entering inertia analysis. Your goal is to identify alternatives the team could use instead of this feature and prove each is insufficient.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Minimum 2 IG-IDs required.

**Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]". When C-03 WAIVER: `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format**:
```
Risk: [feasibility constraint or compliance gap]
R-ID: [R-XX — requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot required. Blank sub-slot = structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [existing alternative or status-quo] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |

---

### [ID-REGISTER]

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [constraint or OQ if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

---

EXIT:
- [IG-REGISTER] present; minimum 2 rows; [ID-REGISTER] present; all Verdicts set
- Every non-waived Elimination Path cell contains named R-ID

> **[INERTIA-ANALYZED]**
>
> **Condition 1:** INVALID IF [IG-REGISTER] or [ID-REGISTER] absent or any IG-ID row unpopulated.
>
> **Condition 2:** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: "R-ID WAIVED" cells are exempt.
>
> Meeting Condition 1 without Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] → Condition 2 exemption above.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ ROLE: ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

You are now authoring the specification. Five sections in prescribed order. Your goal is a document any engineer can implement without ambiguity.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [copy from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row → confirm P0 coverage count.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name] | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming scan range (R-01 through R-{n}).

Architect: write requirements narrative from pre-assigned rows. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. Incorporate design constraints from Phase 1 Architect intake. For each P0 requirement assigned here, name a design element that satisfies it.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [source] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |

---

EXIT:
- All five guided sections in prescribed order
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- Cross-namespace signal at both locations when applicable

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF five guided sections not present in order, or [PM-CONTRACT-SEAL] / [INERTIA-ANALYZED] absent.
>
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Your goal is to identify gaps from Phase 3 and produce actionable amendments.

1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Your final task is a self-review scan. Verify each item before writing findings.

Self-review scan list:
- [PM-CONTRACT-SEAL] present; Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] Condition 1 and Condition 2 certified
- Design constraint intake from Phase 1 Architect scan reflected in Design section
- Cross-namespace signal at both locations
- AMPLIFIED rows: both sub-slots populated
- Waiver chain closed
- Five sections in prescribed order

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: sections disproportionate to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-04 — Compound: Output Format + Inertia Framing + Phase 1.5

**Primary axes**: V-01 [DD-REGISTER] in Phase 3 Design + V-02 [STATUS-QUO-SNAPSHOT] as Phase 2 anchor + Phase 1.5 STRATEGY INERTIA SCOPING emitting [STRATEGY-SCOPE-SEAL] + dual-token Phase 2 gate ([PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]) + C-40 cross-reference ([STRATEGY-SCOPE-SEAL] INVALID IF names [STATUS-QUO-SNAPSHOT] structural fail rule as required presence). ENTER/EXIT, second-person, ROLE markers throughout all five numbered phases.

**Hypothesis**: DD-register is criterion-neutral for C-36/C-37/C-38/C-39/C-40. All five extension criteria pass. C-41/C-42/C-43 all satisfied. Expected composite: 35/35 aspirational. Composite 175/175.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter (hard fail if any field missing):
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v14
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ ROLE: ARCHITECT

ENTER:
- File system access to `simulations/scout/` available
- Topic and date defined; session initialized

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate [SCOUT-STATUS-TABLE] before proceeding.

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

**B-1: Feasibility loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-2: Compliance loaded, feasibility NOT FOUND**

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

**Anti-blend instruction**: Identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

EXIT:
- [SCOUT-STATUS-TABLE] complete; all seven artifact rows populated
- Fallback branch selected
- All subsequent phases blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ ROLE: PM

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

You are now entering the pre-assignment phase. Your goal is to scan the requirements artifact and assign every P0 requirement to a named spec section before strategy scoping or inertia analysis begins.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE]

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |

**Waiver Status column**: enumerated values are `COVERED` or `C-03 WAIVER`. Named structural element.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` in [IG-REGISTER] Elimination Paths. [INERTIA-ANALYZED] Condition 2 exempts "R-ID WAIVED" cells.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the loaded artifact, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows → name conflicting R-ID pairs → or state "none found after scanning R-01 through R-{n}."

---

EXIT:
- [PM-COVERAGE-TABLE] present; P0 rows assigned; Waiver Status column named
- Contradiction scan complete
- Cross-namespace signal populated (or "none loaded")

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column as a named structural element.
>
> Phase 1.5 is blocked until this token is present.

---

## PHASE 1.5: STRATEGY INERTIA SCOPING — Strategy

→ ROLE: STRATEGY

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

You are now entering strategy scoping. Your goal is to name the status-quo alternatives the organization is currently using, document why each fails at scale, and emit [STRATEGY-SCOPE-SEAL] before inertia analysis begins.

### [STATUS-QUO-SNAPSHOT]

Name each competing alternative. For each, state the gap and transition cost.

**Structural fail rule**: A row with a named alternative but a blank Gap statement is a structural fail, not a content gap.

| Alt-ID | Alternative (what teams use today) | Gap (why it does not scale) | Transition Cost |
|--------|-----------------------------------|-----------------------------|-----------------|
| ALT-01 | [existing tool, workflow, or manual process] | [specific capability gap] | [what changes] |
| ALT-02 | [another alternative] | [gap] | [cost] |

---

EXIT:
- [STATUS-QUO-SNAPSHOT] present; minimum 2 ALT-ID rows; structural fail rule co-located
- Strategy scope confirmed

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STATUS-QUO-SNAPSHOT] present in this sub-phase AND without the [STATUS-QUO-SNAPSHOT] structural fail rule ("a row with a named alternative but a blank Gap statement is a structural fail") co-located within the [STATUS-QUO-SNAPSHOT] block definition.
>
> Phase 2 is blocked until [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] are both present.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] both present (Phase 1 AND Phase 1.5 EXIT satisfied)
- → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]. If either is absent, halt and name the missing token.

You are now entering inertia analysis. Your goal is to enumerate and eliminate each status-quo alternative identified in Phase 1.5 as an insufficient substitute.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [numeric or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID should correspond to an ALT-ID from [STATUS-QUO-SNAPSHOT]. Minimum 2 IG-IDs.

**Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]". Waiver: `"R-ID WAIVED (no requirements artifact) — [reason]"`.

**AMPLIFIED sub-slot format**:
```
Risk: [feasibility constraint or compliance gap]
R-ID: [R-XX — requirement that closes this risk]
```
**Partial-population structural fail rule**: Blank sub-slot = structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [ALT-ID reference + why insufficient] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |

---

### [ID-REGISTER]

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [constraint or OQ if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

---

EXIT:
- [IG-REGISTER] present; minimum 2 rows; [ID-REGISTER] all Verdicts set
- Every non-waived Elimination Path cell has named R-ID

> **[INERTIA-ANALYZED]**
>
> **Condition 1:** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated.
>
> **Condition 2:** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: "R-ID WAIVED" cells are exempt.
>
> Meeting Condition 1 without Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER (Phase 1) → "R-ID WAIVED" in [IG-REGISTER] Elimination Path → Condition 2 exemption above.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ ROLE: ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

You are now authoring the specification. Five sections in prescribed order. Your goal is a document any engineer can implement without ambiguity.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [copy from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill pre-assigned rows → confirm P0 coverage count.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name] | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming scan range (R-01 through R-{n}).

Architect: write requirements narrative. Do not reorder.

---

### 3. Design

You will now produce the design as a structured [DD-REGISTER]. Each row names one design decision. Every P0 requirement assigned to this section must appear in at least one DD row. A P0 requirement with no DD row is a gap — flag it in FINDINGS.

### [DD-REGISTER] — Design Decisions

| DD-ID | Decision | R-ID Coverage | Trade-off | Architect Note |
|-------|----------|---------------|-----------|----------------|
| DD-01 | [design decision name] | R-XX, R-YY | [alternative considered and why rejected] | [implementation constraint] |
| DD-02 | [decision] | R-XX | [trade-off] | [note] |
| DD-03 | [add as needed] | | | |

**DD-register completeness rule**: A DD row with a named decision but blank R-ID Coverage is a structural fail.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [source] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |

---

EXIT:
- All five guided sections in prescribed order
- [DD-REGISTER] present; every Design-assigned P0 has named R-ID Coverage
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] present
- Cross-namespace signal at both locations when applicable

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF five guided sections not present in order, or [PM-CONTRACT-SEAL] / [INERTIA-ANALYZED] absent.
>
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Your goal is to surface specific gaps and produce actionable amendments.

1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Your final task is a self-review scan. Verify each item before writing findings.

Self-review scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [STRATEGY-SCOPE-SEAL] present; [STATUS-QUO-SNAPSHOT] structural fail rule co-located
- [INERTIA-ANALYZED] Condition 1 extended to [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]
- [STRATEGY-SCOPE-SEAL] INVALID IF names [STATUS-QUO-SNAPSHOT] structural fail rule (C-40 check)
- Phase 2 BLOCKED statement names [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]
- [DD-REGISTER] present; all DD rows have named R-ID Coverage
- Cross-namespace signal at both locations
- All AMPLIFIED rows: both sub-slots populated
- Waiver chain closed
- Five sections in prescribed order

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: sections disproportionate to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-05 — Compound: Full Synthesis (All Five Axes)

**Primary axes**: V-01 [DD-REGISTER] output format + V-02 [STATUS-QUO-SNAPSHOT] inertia framing + V-03 Architect co-leads Phase 1 + Phase 1.5 STRATEGY INERTIA SCOPING + dual-token Phase 2 gate + C-41/C-42 throughout.

**Hypothesis**: V-03 role sequence (ROLE: PM + ARCHITECT at Phase 1 entry) is incompatible with C-43 condition (1), which requires a single-actor Phase 1 marker. Full synthesis therefore achieves 34/35 aspirational (C-43 = FAIL) with all other extension criteria active — C-36, C-37, C-38, C-39, C-40, C-41, C-42 all pass. Tests whether maximum feature coverage at the cost of C-43 produces a more useful spec than C-43-compliant V-04. Expected composite: ~174.6/175.

**Discovery target**: Determine if a "PM leads, Architect consults" Phase 1 co-assignment — where the ROLE marker reads → ROLE: PM (lead) + ARCHITECT (consult) — satisfies C-43 condition (1). If yes, V-05 achieves 35/35 and the rubric needs a clarification in C-43 to address the lead/consult distinction.

---

You are running the `draft-spec` skill as **Architect**.

## Artifact

Name this artifact: `{topic}-spec-{date}.md`

Frontmatter (hard fail if any field missing):
```
skill: draft-spec
topic: {topic}
item: specification
date: {date}
skill_version: v14
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ ROLE: ARCHITECT

ENTER:
- File system access to `simulations/scout/` available
- Topic and date defined; session initialized

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate [SCOUT-STATUS-TABLE] before proceeding.

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

**B-1: Feasibility loaded, compliance NOT FOUND**

VERBATIM RESPONSE:
> I have a feasibility signal for this topic but no requirements artifact. I can write a spec using the feasibility constraints I have, but I won't be able to do P0 requirement coverage — I'll note the C-03 waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-2: Compliance loaded, feasibility NOT FOUND**

VERBATIM RESPONSE:
> I have a compliance signal for this topic but no requirements artifact. I can write a spec using the compliance posture I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-3: Both loaded**

VERBATIM RESPONSE:
> I have feasibility and compliance signals for this topic but no requirements artifact. I can write a spec using both signals, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**B-catch: Any other combination**

VERBATIM RESPONSE:
> I have some scout signals for this topic but no requirements artifact. I can still write a spec using the signals I have, but P0 requirement coverage will be waived — I'll note this explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms.

**Anti-blend instruction**: Emit matching branch VERBATIM RESPONSE without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

EXIT:
- [SCOUT-STATUS-TABLE] complete; all seven rows populated
- Fallback branch selected
- All subsequent phases blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM + Architect

→ ROLE: PM (lead) + ARCHITECT (consult)

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

You are now entering a joint pre-assignment phase. PM leads requirement-to-section assignment. Architect consults: scan feasibility and compliance artifacts to surface design constraints that affect section assignments.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section.**

**Architect: scan `scout-feasibility` and `scout-compliance` (if LOADED) → record design constraints → flag P0 requirements whose assigned section may be under-specified.**

Design constraint intake (Architect — complete before [PM-CONTRACT-SEAL] emitted):

| Constraint Source | Artifact | Constraint | Affected R-IDs |
|-------------------|----------|-----------|----------------|
| [feasibility / compliance / none] | [artifact name or "NOT LOADED"] | [1-sentence constraint] | [R-XX, R-YY or "—"] |

CASCADE TO: [IG-REGISTER] Phase 2 AND Purpose cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE]

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |

**Waiver Status column**: `COVERED` or `C-03 WAIVER`. Named structural element.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule**: C-03 WAIVER rows generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Paths. [INERTIA-ANALYZED] Condition 2 exempts "R-ID WAIVED" cells.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [loaded artifact name, or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan P0 rows → name conflicting pairs → or state "none found after scanning R-01 through R-{n}."

---

EXIT:
- [PM-COVERAGE-TABLE] present; P0 rows assigned; Waiver Status column named
- Architect design constraint intake complete
- Contradiction scan complete
- Cross-namespace signal populated (or "none loaded")

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column as a named structural element.
>
> Phase 1.5 is blocked until this token is present.

---

## PHASE 1.5: STRATEGY INERTIA SCOPING — Strategy

→ ROLE: STRATEGY

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

You are now entering strategy scoping. Your goal is to name each status-quo alternative the organization could plausibly use instead of this feature, document why each fails at scale, and emit [STRATEGY-SCOPE-SEAL].

### [STATUS-QUO-SNAPSHOT]

**Structural fail rule**: A row with a named alternative but a blank Gap statement is a structural fail, not a content gap.

| Alt-ID | Alternative (what teams use today) | Gap (why it does not scale) | Transition Cost |
|--------|-----------------------------------|-----------------------------|-----------------|
| ALT-01 | [existing tool, workflow, or manual process] | [capability gap] | [what changes] |
| ALT-02 | [another alternative] | [gap] | [cost] |

---

EXIT:
- [STATUS-QUO-SNAPSHOT] present; minimum 2 ALT-ID rows; structural fail rule co-located

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STATUS-QUO-SNAPSHOT] present in this sub-phase AND without the [STATUS-QUO-SNAPSHOT] structural fail rule ("a row with a named alternative but a blank Gap statement is a structural fail") co-located within the [STATUS-QUO-SNAPSHOT] block definition.
>
> Phase 2 is blocked until [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] are both present.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ ROLE: PM + ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] both present (Phase 1 AND Phase 1.5 EXIT satisfied)
- → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]. If either absent, halt and name the missing token.

You are now entering inertia analysis. Your goal is to enumerate and eliminate each status-quo alternative from Phase 1.5 as an insufficient substitute.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [numeric or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID should correspond to or extend an ALT-ID from [STATUS-QUO-SNAPSHOT]. Minimum 2 IG-IDs.

**Elimination Path format**: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]". Waiver: `"R-ID WAIVED (no requirements artifact) — [reason]"`.

**AMPLIFIED sub-slot format**:
```
Risk: [feasibility constraint or compliance gap]
R-ID: [R-XX — requirement that closes this risk]
```
**Partial-population structural fail rule**: Blank sub-slot = structural fail.

| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path | Risk Signal |
|-------|------------------|--------------------|-----------------|-------------|
| IG-01 | [PM / Architect / Strategy / Compliance] | [ALT-ID reference + why insufficient] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-02 | [role] | [describe] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |

---

### [ID-REGISTER]

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [constraint or OQ if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

---

EXIT:
- [IG-REGISTER] and [ID-REGISTER] present; minimum 2 rows; all Verdicts set
- Every non-waived Elimination Path cell has named R-ID

> **[INERTIA-ANALYZED]**
>
> **Condition 1:** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated.
>
> **Condition 2:** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: "R-ID WAIVED" cells are exempt.
>
> Meeting Condition 1 without Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER (Phase 1) → "R-ID WAIVED" in [IG-REGISTER] Elimination Path → Condition 2 exemption above.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ ROLE: ARCHITECT

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

You are now authoring the specification. Incorporate design constraints from Phase 1 Architect intake and status-quo gap analysis from Phase 1.5 into each relevant section. Five sections in prescribed order.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

| Field | Value |
|-------|-------|
| Primary user | [role name] |
| Core workflow | [1 sentence] |
| Business value | [1 sentence] |
| Cross-namespace signal (location 2 of 2) | [copy from Phase 1 location 1 of 2, or "none loaded"] |

---

### 2. Requirements

**PM: scan [PM-COVERAGE-TABLE] → fill pre-assigned rows → confirm P0 coverage count.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name] | ASSIGNED |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming scan range (R-01 through R-{n}).

Architect: write requirements narrative. Do not reorder.

---

### 3. Design

You will now produce the design as a structured [DD-REGISTER]. Each row names one design decision. Incorporate design constraints from Phase 1 Architect intake. Every P0 requirement assigned to this section must appear in at least one DD row. Missing = gap → flag in FINDINGS.

### [DD-REGISTER] — Design Decisions

| DD-ID | Decision | R-ID Coverage | Trade-off | Architect Note |
|-------|----------|---------------|-----------|----------------|
| DD-01 | [design decision] | R-XX, R-YY | [alternative considered; why rejected] | [implementation constraint; cross-ref Phase 1 constraint if applicable] |
| DD-02 | [decision] | R-XX | [trade-off] | [note] |
| DD-03 | [add as needed] | | | |

**DD-register completeness rule**: DD row with named decision but blank R-ID Coverage = structural fail.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [source] | [IG-XX or —] |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |

---

EXIT:
- All five guided sections in prescribed order
- [DD-REGISTER] present; every Design-assigned P0 has DD row with R-ID Coverage
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] present
- Cross-namespace signal at both locations when applicable

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF five guided sections not present in order, or [PM-CONTRACT-SEAL] / [INERTIA-ANALYZED] absent.
>
> INVALID IF cross-namespace signal absent at both locations when a non-requirements artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Your goal is to identify gaps surfaced in Phase 3 and produce actionable amendments.

1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

→ ROLE: ARCHITECT

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Your final task is a self-review scan. Verify each item before writing findings.

Self-review scan list:
- [PM-CONTRACT-SEAL] present; Waiver Status column in [PM-COVERAGE-TABLE]
- [STRATEGY-SCOPE-SEAL] present; [STATUS-QUO-SNAPSHOT] structural fail rule co-located
- [STRATEGY-SCOPE-SEAL] INVALID IF names [STATUS-QUO-SNAPSHOT] structural fail rule by reference (C-40 check)
- [INERTIA-ANALYZED] Condition 1 extended to [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]
- Phase 2 BLOCKED statement names [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]
- [DD-REGISTER] present; all DD rows have named R-ID Coverage
- Design constraint intake from Phase 1 Architect scan reflected in Design section or Constraints
- Cross-namespace signal at both locations
- All AMPLIFIED rows: both sub-slots populated
- Waiver chain closed
- Five sections in prescribed order
- C-43 boundary check: Phase 1 → ROLE: PM (lead) + ARCHITECT (consult) — record whether this satisfies C-43 condition (1) or produces a fail

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: sections disproportionate to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

## Expected Score Summary

| Variation | C-41 | C-42 | C-43 | C-36 | C-37 | C-38 | C-39 | C-40 | Aspirational | Notes |
|-----------|------|------|------|------|------|------|------|------|--------------|-------|
| V-01 | PASS | PASS | PASS | N/A | N/A | N/A | N/A | N/A | 30/35 | DD-register neutral; no extension patterns |
| V-02 | PASS | PASS | PASS | PASS | PASS | N/A | N/A | N/A | 32/35 | STATUS-QUO-SNAPSHOT activates C-36/C-37 |
| V-03 | PASS | PASS | FAIL | N/A | N/A | N/A | N/A | N/A | 29/35 | C-43 cond.(1) violated by Phase 1 multi-actor marker |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 35/35 | All extension criteria; DD-register neutral |
| V-05 | PASS | PASS | TBD | PASS | PASS | PASS | PASS | PASS | 34-35/35 | C-43 TBD: depends on lead/consult marker reading |

**R15 discovery questions**:
1. Does the [DD-REGISTER] in Phase 3 Design trigger any unexpected criterion interactions? (V-01, V-04, V-05)
2. Does [STATUS-QUO-SNAPSHOT] as Phase 2 opening block — before [IG-REGISTER] — affect any Condition 1 evaluation order? (V-02, V-04, V-05)
3. Does → ROLE: PM (lead) + ARCHITECT (consult) at Phase 1 entry satisfy C-43 condition (1)? Answer determines V-05 final score. (V-03, V-05)
