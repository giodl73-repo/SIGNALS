---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v13
round: R14
date: 2026-03-15
axes_explored: lifecycle-emphasis-enter-exit-contract, phrasing-register-second-person-frame, role-sequence-explicit-shift-markup, enter-exit+phase-1.5+c38-c39-c40, second-person-frame+phase-1.5+c38-c39-c40
---

# Quest Variate — `draft-spec` — Round 14 (Rubric v13)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Lifecycle emphasis — each phase wrapped in explicit ENTER: (preconditions) and EXIT: (postconditions) contract blocks; gate tokens emitted from EXIT blocks; replaces single-line → BLOCKED: statements | None | All 37 prior criteria pass; C-17 satisfied because [PM-CONTRACT-SEAL] definition still names the Phase 2 dependency; C-28 satisfied because PM pre-assignment still gates inertia analysis; ENTER/EXIT ceremony is criterion-neutral; composite ~161.7/175 (C-36 through C-40 N/A — no STATUS-QUO-SNAPSHOT or Phase 1.5) |
| V-02 | Phrasing register — surrounding explanatory prose shifts to second-person "you" address ("You enter Phase 1 as PM. In this phase, you scan…"); formal actor→action directives retain the "PM: scan `scout-requirements` → assign…" form required by C-27; only the framing narrative changes register | None | Register shift in explanatory prose is criterion-neutral; C-27 passes because actor→action directives are unchanged; composite ~161.7/175 (no STATUS-QUO-SNAPSHOT or Phase 1.5) |
| V-03 | Role sequence — explicit → ROLE: [ROLE-NAME] inline shift marker at each phase entry; role assignments unchanged; transitions made visible as first-class structural elements before the first directive of each phase | None | Explicit role-shift markup is criterion-neutral; all role-phase directives still satisfy C-27; C-16/C-28 pass because PM phase still precedes inertia phase; composite ~161.7/175 (no STATUS-QUO-SNAPSHOT or Phase 1.5) |
| V-04 | Combined: V-01 ENTER/EXIT contract blocks + Phase 1.5 STRATEGY INERTIA SCOPING (C-39) + [STATUS-QUO-SNAPSHOT] with co-located structural fail rule (C-36/C-37) + [STRATEGY-SCOPE-SEAL] with INVALID IF naming structural fail rule by name (C-40) + dual-token Phase 2 gate (C-38) | Lifecycle emphasis (V-01), inertia framing, Phase 1.5 strategy scoping | ENTER/EXIT blocks are criterion-neutral even with full Phase 1.5 extension; all five new v13 extension criteria pass; composite 175/175 |
| V-05 | Combined: V-02 second-person frame prose + Phase 1.5 STRATEGY INERTIA SCOPING (C-39) + [STATUS-QUO-SNAPSHOT] with co-located structural fail rule (C-36/C-37) + [STRATEGY-SCOPE-SEAL] INVALID IF cross-reference (C-40) + dual-token Phase 2 gate (C-38) | Phrasing register (V-02), inertia framing, Phase 1.5 strategy scoping | Second-person frame prose is criterion-neutral across all governance criteria including C-38 through C-40; composite 175/175 |

---

## V-01 — Axis: Lifecycle Emphasis (Explicit ENTER/EXIT Phase Contract)

**Primary axis**: Lifecycle emphasis — each phase is wrapped with a structured ENTER: block (preconditions that must be true before the phase begins) and an EXIT: block (postconditions that must be true and gate tokens that must be emitted before the phase completes). Gate tokens appear inside EXIT: blocks. All `→ BLOCKED:` single-line statements are replaced by explicit ENTER:/EXIT: contract declarations. Gate token definitions and INVALID IF rules are unchanged.

**Hypothesis**: ENTER/EXIT contract blocks are a ceremony-level change only. The gate token identities, their INVALID IF rules, and their phase dependencies are all preserved. C-17 passes because [PM-CONTRACT-SEAL] is still named with Phase 2 as its dependent. C-28 passes because PM pre-assignment still computationally precedes inertia analysis. All 27 non-extension aspirational criteria pass. C-36 through C-40 are N/A (no STATUS-QUO-SNAPSHOT, no Phase 1.5). Expected composite: ~161.7/175.

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
skill_version: v13
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

ENTER:
- File system access to `simulations/scout/` available
- Topic defined; session initialized

Scan `simulations/scout/` for existing artifacts. Populate [SCOUT-STATUS-TABLE].

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
- [SCOUT-STATUS-TABLE] complete with all seven artifact rows populated
- Fallback branch selected (A / B-1 / B-2 / B-3 / B-catch / Normal)
- Phases 1 through FINDINGS blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

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

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- If absent: halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"

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

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- If either absent: halt and name the missing token

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

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it.

Architect: name at least one design element per P0 requirement assigned here. If a P0 requirement has no corresponding design element after writing, flag it as a gap in FINDINGS.

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
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present in this document
- Cross-namespace signal at both locations when a non-requirements artifact was LOADED

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Amendment list (produce after Phase 3 — minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]
... (additional items if Phase 3 findings warrant)

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Self-review scan list — Architect: verify each item before emitting findings:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 (names [IG-REGISTER], [ID-REGISTER]) and Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-02 — Axis: Phrasing Register (Second-person Frame Prose)

**Primary axis**: Phrasing register — surrounding explanatory prose shifts from third-person/descriptive to second-person imperative, addressing the executing Architect directly as "you." The formal actor→action directives (e.g., "PM: scan `scout-requirements` → assign each P0 row → emit [PM-CONTRACT-SEAL]") are unchanged — these retain the actor-named form required by C-27. Only the framing and explanatory narrative surrounding the directives changes register.

**Hypothesis**: Second-person frame prose is criterion-neutral. C-27 passes because actor→action directives maintain the "PM: scan…" form. All structural elements (tables, gate tokens, INVALID IF rules, ordinal markers, chain closure) are unchanged. Composite ~161.7/175 (no STATUS-QUO-SNAPSHOT or Phase 1.5; C-36 through C-40 N/A).

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
skill_version: v13
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ BLOCKS: all subsequent phases until [SCOUT-STATUS-TABLE] is present.

You begin by scanning `simulations/scout/` for existing artifacts related to this topic. Populate the [SCOUT-STATUS-TABLE] with what you find.

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

You now evaluate the scout status and select the appropriate fallback branch.

### Fallback Branch A — ALL rows NOT FOUND

If every artifact row is NOT FOUND, you emit the following response verbatim and halt:

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

If requirements are missing but other signals exist, you select the specific B sub-branch and emit only that branch's response.

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

You have requirements available. Proceed to Phase 1.

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ BLOCKED: Phase 1 begins after [SCOUT-STATUS-TABLE] is present above.

You enter Phase 1 acting as PM. Your task is to assign every P0 requirement to a named spec section and certify that assignment by emitting [PM-CONTRACT-SEAL].

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

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

You also capture the strongest non-requirements signal here to trace it through the spec.

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Before sealing the phase, you scan for requirement conflicts.

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` → name any conflicting R-ID pairs (e.g., "R-06 vs R-10") → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Phase 2 is blocked until this token appears here.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above. If absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding."

You enter Phase 2 as PM and Architect. The goal is to enumerate inertia hypotheses and decisions that will shape the spec's design and constraints.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

You enumerate inertia hypotheses below. Minimum 2 IG-IDs required.

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

→ BLOCKED: Phase 3 begins after [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present above.

You enter Phase 3 as Architect. You write the five guided spec sections in prescribed order.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

State what this feature does in 2–4 sentences.

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

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

You write the requirements narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

You detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned here, you name a design element that satisfies it. Flag gaps in FINDINGS.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ BLOCKED: Phase 4 begins after [SPEC-DRAFT-COMPLETE] is present above.

You review Phase 3 output and produce the amendment list.

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]
... (additional items if Phase 3 findings warrant)

---

## FINDINGS

→ REQUIRES: [SPEC-DRAFT-COMPLETE]

You perform a self-review before finalizing. Verify each item on the scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 and Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-03 — Axis: Role Sequence (Explicit Role-Shift Inline Markup)

**Primary axis**: Role sequence — each phase begins with an explicit → ROLE: [ROLE-NAME] inline shift marker immediately before the first directive of the phase. The shift marker names which of the three stock roles (PM, ARCHITECT, STRATEGY) is active at phase entry. Role assignments are unchanged from the baseline template; only the visibility of transitions is added. The directive form ("PM: scan…") still appears on directives; the → ROLE: marker announces the transition itself.

**Hypothesis**: Explicit role-shift markup is criterion-neutral. Role identities are unchanged; C-27 (actor→action directive form) still passes because the directives retain their "PM: scan…" form. C-16/C-28 pass because PM assignment still occurs in Phase 1 before any inertia analysis. Composite ~161.7/175 (no STATUS-QUO-SNAPSHOT or Phase 1.5; C-36 through C-40 N/A).

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
skill_version: v13
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP

→ ROLE: ARCHITECT

→ BLOCKS: all subsequent phases until [SCOUT-STATUS-TABLE] present.

Scan `simulations/scout/` for artifacts. Populate [SCOUT-STATUS-TABLE].

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

---

## PHASE 1: PM PRE-ASSIGNMENT

→ ROLE: PM
→ BLOCKED: Phase 1 begins after [SCOUT-STATUS-TABLE] is present above.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). Named structural element — prose notes or row-level annotations in another column do not substitute.

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

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Phase 2 is blocked until this token appears here.

---

## PHASE 2: INERTIA ANALYSIS

→ ROLE: PM + ARCHITECT
→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above. If absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding."

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

## PHASE 3: GUIDED SECTIONS

→ ROLE: ARCHITECT
→ BLOCKED: Phase 3 begins after [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present above.

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

→ ROLE: PM (secondary validation)

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row below → confirm P0 coverage count before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

→ ROLE: ARCHITECT

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it. Flag gaps in FINDINGS.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS

→ ROLE: ARCHITECT
→ BLOCKED: Phase 4 begins after [SPEC-DRAFT-COMPLETE] is present above.

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]
... (additional items if Phase 3 findings warrant)

---

## FINDINGS

→ REQUIRES: [SPEC-DRAFT-COMPLETE]

Self-review scan list — Architect: verify each item before emitting findings:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 and Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-04 — Combined: ENTER/EXIT Contract + Phase 1.5 + Full C-38/C-39/C-40

**Primary axis**: Combined — V-01's explicit ENTER:/EXIT: contract blocks on every phase PLUS Phase 1.5 STRATEGY INERTIA SCOPING inserted between Phase 1 and Phase 2. Phase 1.5 emits [STRATEGY-SCOPE-SEAL], which joins [PM-CONTRACT-SEAL] as a dual required token for Phase 2 entry. [STATUS-QUO-SNAPSHOT] is defined in Phase 1.5 with a co-located structural fail rule. [STRATEGY-SCOPE-SEAL]'s INVALID IF rule cross-references the [STATUS-QUO-SNAPSHOT] structural fail rule by name. [INERTIA-ANALYZED] Condition 1 is extended to name [STATUS-QUO-SNAPSHOT].

**Hypothesis**: ENTER/EXIT contract blocks are criterion-neutral even with the full Phase 1.5 extension pattern. C-39 passes (Phase 1.5 header names ordinal 1.5 and role scope STRATEGY INERTIA SCOPING; emits [STRATEGY-SCOPE-SEAL]). C-38 passes (Phase 2 declares REQUIRES [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]). C-36 passes ([INERTIA-ANALYZED] Condition 1 names [STATUS-QUO-SNAPSHOT]). C-37 passes (structural fail rule co-located with [STATUS-QUO-SNAPSHOT] row definition). C-40 passes ([STRATEGY-SCOPE-SEAL] INVALID IF names structural fail rule by reference). C-01 still passes — all five required numbered phases remain in prescribed order; Phase 1.5 does not replace or merge any required phase. Expected composite: 175/175.

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
skill_version: v13
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

ENTER:
- File system access to `simulations/scout/` available
- Topic defined; session initialized

Scan `simulations/scout/` for artifacts. Populate [SCOUT-STATUS-TABLE].

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
- [SCOUT-STATUS-TABLE] complete with all seven artifact rows populated
- Fallback branch selected (A / B-1 / B-2 / B-3 / B-catch / Normal)
- All subsequent phases blocked until this EXIT is satisfied

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

ENTER:
- [SCOUT-STATUS-TABLE] complete (Phase 0 EXIT satisfied)
- Fallback = Normal branch or user-confirmed B branch

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). Named structural element — prose notes or row-level annotations in another column do not substitute.

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

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> Phase 1.5 is blocked until [PM-CONTRACT-SEAL] appears here. Phase 2 is blocked until [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] are both present.

---

## PHASE 1.5 — STRATEGY INERTIA SCOPING — Strategy

ENTER:
- [PM-CONTRACT-SEAL] present (Phase 1 EXIT satisfied)
- Role transitions from PM to Strategy for inertia scoping

Strategy: review [PM-COVERAGE-TABLE] and, if any non-requirements scout artifacts are LOADED, enumerate the status-quo alternatives that currently make this feature avoidable. For each SQ-ID, nominate the IG-ID it should seed.

**IMPORTANT**: Phase 1 (PM PRE-ASSIGNMENT) is complete before this phase begins. Strategy inertia scoping is an additive pre-analysis step, not a replacement for PM assignment. All P0 rows are already assigned in [PM-COVERAGE-TABLE] before Strategy acts here.

### [STATUS-QUO-SNAPSHOT] — Status-Quo Alternatives Register

**Structural fail rule (co-located)**: A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap. The gap statement is the load-bearing element for downstream inertia analysis.

| SQ-ID | Status-Quo Alternative | What users do today | Gap statement — why this alternative fails to satisfy the feature need | Nominated IG-ID |
|-------|----------------------|--------------------|--------------------------------------------------------------------|-----------------|
| SQ-01 | [name the tool, workflow, or workaround] | [1 sentence] | [specific structural gap — name the capability the status-quo cannot provide] | IG-01 |
| SQ-02 | [name] | [1 sentence] | [gap statement] | IG-02 |
| SQ-03 | [add if applicable] | | | IG-03 |

---

EXIT:
- [STATUS-QUO-SNAPSHOT] present with all nominated IG-IDs populated and all gap statements non-blank (structural fail rule verified)
- Phase 2 [IG-REGISTER] authoring blocked until this EXIT is satisfied

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STATUS-QUO-SNAPSHOT] present with all nominated IG-IDs populated AND without the structural fail rule present co-located with the [STATUS-QUO-SNAPSHOT] row definition.
>
> [STRATEGY-SCOPE-SEAL] INVALID IF the [STATUS-QUO-SNAPSHOT] structural fail rule is absent from the [STATUS-QUO-SNAPSHOT] block definition — the seal's validity requires the co-located enforcement rule to be verifiably present, not merely the block it governs.
>
> [STRATEGY-SCOPE-SEAL] is a proof-of-work artifact. Phase 2 [IG-REGISTER] authoring is blocked until this token appears here.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

ENTER:
- [PM-CONTRACT-SEAL] from Phase 1 AND [STRATEGY-SCOPE-SEAL] from Phase 1.5 — both must be present
- If either absent: halt and name the missing token
- → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID corresponds to one nominated SQ-ID from [STATUS-QUO-SNAPSHOT] in Phase 1.5. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason. When C-03 WAIVER applies, mark `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap.

| IG-ID | SQ-ID | Responsible Role | Inertia Hypothesis (from SQ gap statement) | Elimination Path | Risk Signal |
|-------|-------|------------------|--------------------------------------------|-----------------|-------------|
| IG-01 | SQ-01 | [PM / Architect / Strategy / Compliance] | [restate gap from SQ-01 as hypothesis] | R-ID: R-XX — [reason; if AMPLIFIED, sub-slot format] | STANDARD / AMPLIFIED |
| IG-02 | SQ-02 | [role] | [gap from SQ-02 as hypothesis] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | SQ-03 | [add if applicable] | | | |

---

### [ID-REGISTER] — Inertia Decision Register

| IG-ID | Mitigation Required | Spec Mitigation | Verdict |
|-------|--------------------|--------------------|---------|
| IG-01 | YES / NO | [named constraint or open question, if YES] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | YES / NO | | ELIMINATED / REQUIRES SPEC MITIGATION |

> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

EXIT:
- [IG-REGISTER] and [ID-REGISTER] present; minimum 2 IG-ID rows populated
- [STATUS-QUO-SNAPSHOT] verified present (Condition 1 check)
- Every non-waived Elimination Path cell contains a named R-ID (Condition 2 check)

> **[INERTIA-ANALYZED]**
>
> This token has two distinct invalidity conditions — both must pass:
>
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 waiver propagation rule) → Condition 2 exemption declared above. All three nodes named in sequence.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

ENTER:
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present (Phase 2 EXIT satisfied)
- If either absent: halt and name the missing token

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
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

Architect: write the requirements section narrative using the pre-assigned rows above.

---

### 3. Design

Detail the solution design. For each P0 requirement assigned here, include a named design element. Flag gaps in FINDINGS.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |
| OQ-02 | | | |

---

EXIT:
- All five guided sections in prescribed order
- [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] both present
- Cross-namespace signal at both locations when a non-requirements artifact was LOADED

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

ENTER:
- [SPEC-DRAFT-COMPLETE] present (Phase 3 EXIT satisfied)

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

EXIT:
- Amendment list present; minimum 2 items named with section reference

---

## FINDINGS

ENTER:
- [SPEC-DRAFT-COMPLETE] present

Self-review scan list — Architect: verify each item before emitting findings:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [STRATEGY-SCOPE-SEAL] present — [STATUS-QUO-SNAPSHOT] all gap statements populated; structural fail rule verified co-located
- [INERTIA-ANALYZED] present — Condition 1 names [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]; Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.

---

---

## V-05 — Combined: Second-person Frame Prose + Phase 1.5 + Full C-38/C-39/C-40

**Primary axis**: Combined — V-02's second-person frame prose throughout PLUS Phase 1.5 STRATEGY INERTIA SCOPING inserted between Phase 1 and Phase 2. The second-person "you" register applies to all explanatory and transitional prose. Actor→action directives retain the "PM: scan…" form to preserve C-27. Phase 1.5 follows the full R13 V-05 pattern: [STATUS-QUO-SNAPSHOT] with co-located structural fail rule, [STRATEGY-SCOPE-SEAL] with INVALID IF cross-referencing the structural fail rule by name, and dual-token Phase 2 gate.

**Hypothesis**: Second-person frame prose is criterion-neutral across all 40 v13 criteria including the three new extension criteria C-38/C-39/C-40. C-27 passes because actor→action directives still name the acting role ("PM: scan…"). C-39 passes (Phase 1.5 header names ordinal and role scope, emits [STRATEGY-SCOPE-SEAL]). C-38 passes (Phase 2 REQUIRES [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]). C-36/C-37/C-40 pass per V-04. Expected composite: 175/175.

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
skill_version: v13
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

→ BLOCKS: all subsequent phases until [SCOUT-STATUS-TABLE] is present.

You begin by scanning `simulations/scout/` for existing artifacts. Your first task is to build a complete picture of what signal exists for this topic before any drafting work begins.

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

Once you have your table, you evaluate which branch applies and respond accordingly.

### Fallback Branch A — ALL rows NOT FOUND

When every artifact is NOT FOUND, you emit the following verbatim and halt:

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

When requirements are absent but other signals exist, you identify the specific sub-branch and emit only that branch's VERBATIM RESPONSE.

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

You have a requirements artifact. Proceed to Phase 1.

---

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ BLOCKED: Phase 1 begins after [SCOUT-STATUS-TABLE] is present above.

You enter Phase 1 acting as PM. Your goal in this phase is to assign every P0 requirement to a named spec section, document the cross-namespace signal, scan for contradictions, and emit [PM-CONTRACT-SEAL] to certify the work.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). Named structural element — prose notes or row-level annotations in another column do not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. [INERTIA-ANALYZED] Condition 2 explicitly exempts cells marked "R-ID WAIVED."

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

---

You capture the most relevant non-requirements signal here for traceability across the spec.

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

Before you emit the seal, you run the contradiction scan.

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` → name any conflicting R-ID pairs (e.g., "R-06 vs R-10") → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> Phase 1.5 is blocked until [PM-CONTRACT-SEAL] appears here. Phase 2 is blocked until [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] are both present.

---

## PHASE 1.5 — STRATEGY INERTIA SCOPING — Strategy

→ BLOCKED: Phase 1.5 begins after [PM-CONTRACT-SEAL] is present above.

You transition to acting as Strategy. Your role in Phase 1.5 is to enumerate the status-quo alternatives that currently make this feature avoidable, so that downstream inertia analysis is grounded in real competitive context rather than abstract hypotheses.

**IMPORTANT**: Phase 1 (PM PRE-ASSIGNMENT) is complete before you begin this phase. You are adding inertia scoping context on top of completed PM assignment — not replacing or reordering it. All P0 rows are already assigned in [PM-COVERAGE-TABLE].

### [STATUS-QUO-SNAPSHOT] — Status-Quo Alternatives Register

**Structural fail rule (co-located)**: A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap. The gap statement is the load-bearing element for downstream inertia analysis.

| SQ-ID | Status-Quo Alternative | What users do today | Gap statement — why this alternative fails to satisfy the feature need | Nominated IG-ID |
|-------|----------------------|--------------------|--------------------------------------------------------------------|-----------------|
| SQ-01 | [name the tool, workflow, or workaround] | [1 sentence] | [specific structural gap — name the capability the status-quo cannot provide] | IG-01 |
| SQ-02 | [name] | [1 sentence] | [gap statement] | IG-02 |
| SQ-03 | [add if applicable] | | | IG-03 |

---

Once you have documented the snapshot and nominated each IG-ID, you emit the seal.

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STATUS-QUO-SNAPSHOT] present with all nominated IG-IDs populated AND without the structural fail rule present co-located with the [STATUS-QUO-SNAPSHOT] row definition.
>
> [STRATEGY-SCOPE-SEAL] INVALID IF the [STATUS-QUO-SNAPSHOT] structural fail rule is absent from the [STATUS-QUO-SNAPSHOT] block definition — the seal's validity requires the co-located enforcement rule to be verifiably present, not merely the block it governs.
>
> [STRATEGY-SCOPE-SEAL] is a proof-of-work artifact. Phase 2 [IG-REGISTER] authoring is blocked until this token appears here.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] from Phase 1 AND [STRATEGY-SCOPE-SEAL] from Phase 1.5. If either is absent, halt and name the missing token.

You enter Phase 2 as PM and Architect. The IG-IDs you enumerate here correspond to the SQ-IDs nominated in Phase 1.5 — your inertia analysis is grounded in the status-quo competitive context Strategy documented.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID corresponds to one nominated SQ-ID from [STATUS-QUO-SNAPSHOT] in Phase 1.5. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason. When C-03 WAIVER applies, mark `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap.

| IG-ID | SQ-ID | Responsible Role | Inertia Hypothesis (from SQ gap statement) | Elimination Path | Risk Signal |
|-------|-------|------------------|--------------------------------------------|-----------------|-------------|
| IG-01 | SQ-01 | [PM / Architect / Strategy / Compliance] | [restate gap from SQ-01 as hypothesis] | R-ID: R-XX — [reason; if AMPLIFIED, sub-slot format] | STANDARD / AMPLIFIED |
| IG-02 | SQ-02 | [role] | [gap from SQ-02 as hypothesis] | R-ID: R-XX — [reason] | STANDARD / AMPLIFIED |
| IG-03 | SQ-03 | [add if applicable] | | | |

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
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 waiver propagation rule) → Condition 2 exemption declared above. All three nodes named in sequence.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ BLOCKED: Phase 3 begins after [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present above.

You enter Phase 3 as Architect. You write the five spec sections that give the feature its definitive shape. The sections follow a prescribed order — do not reorder.

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

---

### 1. Purpose

State what this feature does in 2–4 sentences.

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
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

You write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

You detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned here, you name a design element that satisfies it. You flag any gap in FINDINGS.

---

### 4. Constraints

| Constraint ID | Description | Source | IG-ID (if applicable) |
|---------------|-------------|--------|-----------------------|
| CON-01 | [constraint] | [scout artifact or inline] | [IG-XX or —] |
| CON-02 | | | |

---

### 5. Open Questions

| OQ-ID | Question | Deciding Role | Resolution Needed |
|-------|---------|---------------|-------------------|
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ BLOCKED: Phase 4 begins after [SPEC-DRAFT-COMPLETE] is present above.

You review Phase 3 output and produce the amendment list.

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

---

## FINDINGS

→ REQUIRES: [SPEC-DRAFT-COMPLETE]

You perform the final self-review before the spec is complete. Work through the scan list in order:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [STRATEGY-SCOPE-SEAL] present — [STATUS-QUO-SNAPSHOT] all gap statements populated; structural fail rule verified co-located with row definition
- [INERTIA-ANALYZED] present — Condition 1 names [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]; Condition 2 certified
- Cross-namespace signal at both locations (Phase 1 table AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified)
- Waiver chain closed: Waiver Status column → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order (Purpose, Requirements, Design, Constraints, Open Questions)

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps: requirements with no spec section.
Contradictions: requirement pairs in conflict.
Complexity hotspots: spec sections disproportionately complex relative to requirement priority.
Open question register: all OQ-IDs from Phase 3.
