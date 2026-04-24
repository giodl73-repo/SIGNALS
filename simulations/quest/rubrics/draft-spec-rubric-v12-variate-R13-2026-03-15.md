---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v12
round: R13
date: 2026-03-15
axes_explored: lifecycle-emphasis-compressed, inertia-framing-status-quo-c36-c37, output-format-additive-columns, lifecycle-compressed+status-quo-c36-c37, status-quo-c36-c37+strategy-inertia-scoping
---

# Quest Variate — `draft-spec` — Round 13 (Rubric v12)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Lifecycle emphasis — all phase headers compressed to single-line gate dependency statements; REQUIRES/PRODUCES/EXIT CONDITION/BLOCKS boilerplate removed; gate token invalidity rules and token bodies unchanged | None | All 37 criteria pass; composite 175/175; tests whether verbose phase-header boilerplate is required for C-17/C-28 or whether gate token presence alone satisfies; C-17 passes because the token definition still names the dependency |
| V-02 | Inertia framing — [STATUS-QUO-SNAPSHOT] block added as first operation in Phase 2; each SQ-ID seeds one IG-ID; [INERTIA-ANALYZED] Condition 1 extended to name [STATUS-QUO-SNAPSHOT] (C-36); co-located structural fail rule for blank gap statement (C-37) | None | C-36 and C-37 both PASS; all 35 prior criteria pass; composite 175/175; targeted golden candidate for v12 rubric |
| V-03 | Output format — additive columns: [PM-COVERAGE-TABLE] gains a Coverage Evidence column (scout artifact citation); Phase 3 Requirements table gains a Confidence column (HIGH/MEDIUM/LOW); all structural columns (Waiver Status, Status) preserved | None | All 37 criteria pass; composite 175/175; C-13 passes (Status column still present per row); C-33 passes (Waiver Status column still named structural element); tests whether additive columns are criterion-neutral |
| V-04 | V-02 + V-01 combined — [STATUS-QUO-SNAPSHOT] full integration with C-36/C-37 AND compressed single-line phase headers | Lifecycle emphasis, status-quo inertia framing | All 37 criteria pass; composite 175/175; primary golden candidate combining inertia depth with structural compactness |
| V-05 | V-02 + role sequence — [STATUS-QUO-SNAPSHOT] full integration with C-36/C-37 AND Phase 1.5 STRATEGY INERTIA SCOPING sub-phase; Strategy reviews [STATUS-QUO-SNAPSHOT] and nominates IG-IDs before [IG-REGISTER] enumeration begins; [STRATEGY-SCOPE-SEAL] gates [IG-REGISTER] authoring | Status-quo inertia framing, strategy role insertion | All 37 criteria pass; C-28 still PASS (PM pre-assignment Phase 1 still precedes inertia Phase 2); composite 175/175; tests whether pre-[IG-REGISTER] strategy scoping produces new aspirational signal patterns |

---

## V-01 — Axis: Lifecycle Emphasis (Compressed Phase Headers)

**Primary axis**: Lifecycle emphasis — verbose phase headers (REQUIRES / PRODUCES / EXIT CONDITION / BLOCKS) replaced with single-line gate dependency statements inline at each phase boundary. Gate tokens, invalidity rules, and all structural blocks unchanged. The goal is to test whether structural gate enforcement depends on header verbosity or on token placement and invalidity rules alone.

**Hypothesis**: All 37 criteria pass. C-17 (named gate token with REQUIRES declaration) passes because the compressed inline gate statement (`→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above.`) names the dependency. C-28 (PM pre-assignment before inertia with gate enforcement) passes for the same reason. Composite 175/175.

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
skill_version: v12
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

Scan `simulations/scout/` for artifacts. Produce [SCOUT-STATUS-TABLE].

→ BLOCKS: all subsequent phases until [SCOUT-STATUS-TABLE] present.

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

## PHASE 1: PM PRE-ASSIGNMENT — PM

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

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. This propagation is a named structural obligation declared here in Phase 1 and verified in [INERTIA-ANALYZED] Condition 2.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

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
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, Waiver Status column is a named structural element, and all P0 rows are assigned or waived.
>
> → BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] appears here.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

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
> → BLOCKED: Phase 3 begins after [INERTIA-ANALYZED] appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

→ BLOCKED: Phase 3 begins after [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present above.

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

---

## PHASE 4: AMENDMENTS — Architect

→ BLOCKED: Phase 4 begins after [SPEC-DRAFT-COMPLETE] is present above.

Amendment list (produce after Phase 3 — minimum 2 specific, actionable items):
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

## V-02 — Axis: Inertia Framing (STATUS-QUO-SNAPSHOT + C-36 + C-37)

**Primary axis**: Inertia framing — [STATUS-QUO-SNAPSHOT] structural block added as the first operation in Phase 2, before [IG-REGISTER]. The snapshot names the top status-quo alternatives that make this feature avoidable; each SQ-ID seeds one IG-ID. [INERTIA-ANALYZED] Condition 1 is extended to name [STATUS-QUO-SNAPSHOT] as a required presence check (C-36). A co-located structural fail rule is added to the [STATUS-QUO-SNAPSHOT] block: "A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap" (C-37). All R12 structural elements preserved (C-33, C-34, C-35, ordinal markers, imperative phrasing, chain closure).

**Hypothesis**: C-36 and C-37 both PASS. All 35 prior criteria pass. Composite 175/175. Primary golden candidate for the v12 rubric.

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
skill_version: v12
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

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block or a row-level annotation strategy in another column does not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements. [INERTIA-ANALYZED] Condition 2 includes an explicit exemption: cells marked "R-ID WAIVED" are exempt from the per-cell R-ID population check.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. P0 coverage criterion waived. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` before confirming absence → name any conflicting R-ID pairs (e.g., "R-06 vs R-10") → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, Waiver Status column is a named structural element, and all P0 rows are assigned or waived.
>
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding to inertia analysis"
PRODUCES: [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

---

### [STATUS-QUO-SNAPSHOT] — Status-Quo Alternatives Register

Name the top alternatives that currently make this feature avoidable. Each SQ-ID seeds one IG-ID in [IG-REGISTER]. Minimum 2 SQ-IDs required.

**Structural fail rule (co-located)**: A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap. The gap statement is the load-bearing element for downstream inertia analysis — a row that names an alternative without stating the gap that prevents the alternative from satisfying the feature need is incomplete at the structural level, not merely underspecified.

| SQ-ID | Status-Quo Alternative | What users do today | Gap statement — why this alternative fails to satisfy the feature need | Seeds IG-ID |
|-------|----------------------|--------------------|--------------------------------------------------------------------|-------------|
| SQ-01 | [name the tool, workflow, or workaround] | [1 sentence: how teams use it today] | [specific capability the status-quo cannot provide — not "it is worse"; name the structural gap] | IG-01 |
| SQ-02 | [name] | [1 sentence] | [gap statement] | IG-02 |
| SQ-03 | [add if applicable] | | | IG-03 |

---

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID corresponds to one SQ-ID from [STATUS-QUO-SNAPSHOT]. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason this requirement closes the gap. When C-03 WAIVER applies, mark the cell `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.

| IG-ID | SQ-ID | Responsible Role | Inertia Hypothesis (from SQ gap statement) | Elimination Path | Risk Signal |
|-------|-------|------------------|--------------------------------------------|-----------------|-------------|
| IG-01 | SQ-01 | [PM / Architect / Strategy / Compliance] | [restate the gap from SQ-01 as a hypothesis] | R-ID: R-XX — [reason; if AMPLIFIED, use sub-slot format] | STANDARD / AMPLIFIED [cite trigger] |
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
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID, even when [IG-REGISTER] is present and all rows are populated. A cell containing only a functional description without a named "R-XX" reference fails Condition 2. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> Meeting Condition 1 without meeting Condition 2 renders this token invalid.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural waiver propagation rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [STATUS-QUO-SNAPSHOT] present with all SQ-IDs populated (Condition 1) AND [IG-REGISTER] and [ID-REGISTER] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2) AND all AMPLIFIED rows carry both sub-slots populated (partial-population structural fail rule verified).
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
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

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row → confirm P0 coverage count before Architect writes prose.**

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

===== END PHASE 3 =====

---

## ===== PHASE 4: AMENDMENTS — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

Amendment list (produce after Phase 3 — minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment — name the section and the change]
... (additional items if Phase 3 findings warrant)

===== END PHASE 4 =====

---

## ===== FINDINGS =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Self-review scan list — Architect: verify each item before emitting findings:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 (names [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]) and Condition 2 certified
- [STATUS-QUO-SNAPSHOT] present with all SQ-IDs having populated gap statements (structural fail rule verified)
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

===== END FINDINGS =====

---

---

## V-03 — Axis: Output Format (Additive Coverage Columns)

**Primary axis**: Output format — additive columns added to two structural tables without removing any required columns. [PM-COVERAGE-TABLE] gains a Coverage Evidence column (citation to the specific scout artifact section or line supporting the coverage claim). Phase 3 Requirements table gains a Confidence column (HIGH / MEDIUM / LOW) applied per row alongside the existing Status column. All required structural columns (Waiver Status, per-row Status) preserved. Gate tokens unchanged.

**Hypothesis**: All 37 criteria pass. C-13 passes because the per-row Status column is still present as a structural element in the Phase 3 Requirements table — the Confidence column is additive, not a replacement. C-33 passes because the Waiver Status column is still present as a named structural element in [PM-COVERAGE-TABLE] — Coverage Evidence is additive. C-03 passes because [PM-COVERAGE-TABLE] still has P0 rows and C-03 waiver protocol. Composite 175/175. Tests whether additive output format changes are criterion-neutral.

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
skill_version: v12
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

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 2 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status | Coverage Evidence |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|-------------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name] | COVERED | [scout artifact filename + section/line] |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED | [citation] |
| ... | | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note about waivers in a surrounding block does not substitute.

**Coverage Evidence column**: cites the specific scout artifact filename and section or line that supports the coverage claim. When Waiver Status = `C-03 WAIVER`, set Coverage Evidence to "waived — no requirements artifact."

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` in the Waiver Status column must generate corresponding `"R-ID WAIVED"` markers in the [IG-REGISTER] Elimination Path cells. [INERTIA-ANALYZED] Condition 2 includes an explicit exemption: cells marked "R-ID WAIVED" are exempt from the per-cell R-ID population check.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row in [PM-COVERAGE-TABLE] carries `C-03 WAIVER` in the Waiver Status column and "waived — no requirements artifact" in Coverage Evidence.

---

Cross-namespace signal (location 1 of 2 — if any non-requirements artifact LOADED):

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact (location 1 of 2), or "none loaded"] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

---

**Contradiction scan**: PM: scan all P0 rows in `scout-requirements` before confirming absence → name any conflicting R-ID pairs → or state "none found after scanning R-01 through R-{n}." Do not confirm "none found" without naming the scan range.

Contradictions: [pairs or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present in this phase block with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Its presence certifies [PM-COVERAGE-TABLE] is present, non-empty, Waiver Status column is a named structural element, and all P0 rows are assigned or waived.
>
> Phase 2 is blocked until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 before proceeding"
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Gate Register

Enumerate inertia hypotheses. Minimum 2 IG-IDs required.

**Elimination Path format**: Each cell must begin with "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — " followed by the reason. When C-03 WAIVER applies, mark `"R-ID WAIVED (no requirements artifact) — [functional reason]"`.

**AMPLIFIED Elimination Path sub-slot format** (pre-printed — use when Risk Signal = AMPLIFIED):
```
Risk: [feasibility constraint or compliance gap — name the specific dimension]
R-ID: [R-XX from [PM-COVERAGE-TABLE] — name the requirement that closes this risk]
```
**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap.

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

---

> **[INERTIA-ANALYZED]**
>
> **Condition 1 (table presence):** INVALID IF [IG-REGISTER] or [ID-REGISTER] is absent from this phase block or any IG-ID row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural waiver propagation rule) → Condition 2 exemption declared above.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
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

| Req ID | Priority | Spec Entry | Status | Confidence |
|--------|----------|-----------|--------|------------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED | HIGH / MEDIUM / LOW |
| R-02 | P0 | ... | ASSIGNED | HIGH / MEDIUM / LOW |
| ... | | | | |

**Confidence column**: Architect assigns HIGH (design element clearly satisfies requirement), MEDIUM (design element partially addresses requirement — open question flagged), or LOW (design element does not yet exist — gap flagged). This column is additive; the Status column remains the structural P0 coverage signal per C-13.

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it.

Architect: name at least one design element per P0 requirement assigned here. Flag gaps in FINDINGS.

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
> INVALID IF emitted before all five guided sections are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMENDMENTS — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

===== END PHASE 4 =====

---

## ===== FINDINGS =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Self-review scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present with Condition 1 and Condition 2 certified
- Cross-namespace signal at both locations
- All AMPLIFIED rows carry both sub-slots populated
- Waiver chain closed: Waiver Status → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

===== END FINDINGS =====

---

---

## V-04 — Combined: V-02 (STATUS-QUO-SNAPSHOT + C-36/C-37) + V-01 (Compressed Phase Headers)

**Primary axis**: Combined — [STATUS-QUO-SNAPSHOT] full integration with C-36/C-37 (V-02) AND all phase headers compressed to single-line gate dependency statements (V-01). Gate tokens, invalidity rules, structural blocks, chain closure declaration, and imperative phrasing unchanged. All structural columns (Waiver Status, per-row Status, Responsible Role) preserved.

**Hypothesis**: All 37 criteria pass. C-36 passes (Condition 1 names [STATUS-QUO-SNAPSHOT]). C-37 passes (co-located structural fail rule in [STATUS-QUO-SNAPSHOT]). C-17/C-28 pass (gate dependency inline statements satisfy the REQUIRES declaration criterion). Composite 175/175. Primary golden candidate for R13.

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
skill_version: v12
input: [list each loaded scout artifact by filename]
```

---

## PHASE 0: SETUP — Architect

Scan `simulations/scout/` for artifacts. Produce [SCOUT-STATUS-TABLE].

→ BLOCKS: all subsequent phases until [SCOUT-STATUS-TABLE] present.

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

## PHASE 1: PM PRE-ASSIGNMENT — PM

→ BLOCKED: Phase 1 begins after [SCOUT-STATUS-TABLE] is present above. Phase 2 begins after [PM-CONTRACT-SEAL] appears at the end of this phase.

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (requirement in scope, assigned to a spec section) or `C-03 WAIVER` (scout-requirements artifact not loaded). This column is a named structural element of [PM-COVERAGE-TABLE].

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells. [INERTIA-ANALYZED] Condition 2 explicitly exempts cells marked "R-ID WAIVED."

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row carries `C-03 WAIVER` in the Waiver Status column.

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

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> [PM-CONTRACT-SEAL] is a proof-of-work artifact. Phase 2 is blocked until this token appears here.

---

## PHASE 2: INERTIA ANALYSIS — PM + Architect

→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above. If absent, halt and state "[PM-CONTRACT-SEAL] missing — complete Phase 1 first." Phase 3 begins after [INERTIA-ANALYZED] appears at the end of this phase.

Risk signal sources:
- Feasibility score (from `scout-feasibility` if LOADED): [numeric score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

---

### [STATUS-QUO-SNAPSHOT] — Status-Quo Alternatives Register

Name the top alternatives that currently make this feature avoidable. Each SQ-ID seeds one IG-ID. Minimum 2 SQ-IDs required.

**Structural fail rule (co-located)**: A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap. The gap statement is the load-bearing element for downstream inertia analysis — a row that names an alternative without stating the gap that prevents it from satisfying the feature need is incomplete at the structural level.

| SQ-ID | Status-Quo Alternative | What users do today | Gap statement — why this alternative fails to satisfy the feature need | Seeds IG-ID |
|-------|----------------------|--------------------|--------------------------------------------------------------------|-------------|
| SQ-01 | [name the tool, workflow, or workaround] | [1 sentence: how teams use it today] | [specific structural gap — not "it is worse"; name the capability the status-quo cannot provide] | IG-01 |
| SQ-02 | [name] | [1 sentence] | [gap statement] | IG-02 |
| SQ-03 | [add if applicable] | | | IG-03 |

---

### [IG-REGISTER] — Inertia Gate Register

Each IG-ID corresponds to one SQ-ID from [STATUS-QUO-SNAPSHOT]. Minimum 2 IG-IDs required.

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

---

> **[INERTIA-ANALYZED]**
>
> **Condition 1 (table presence):** INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated.
>
> **Condition 2 (column-level R-ID population):** INVALID IF any Elimination Path cell lacks a named R-ID. Exception: cells explicitly marked "R-ID WAIVED" are exempt from Condition 2.
>
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 waiver propagation rule) → Condition 2 exemption declared above. All three nodes named in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Phase 3 is blocked until this token appears here.

---

## PHASE 3: GUIDED SECTIONS — Architect

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

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. Name at least one design element per P0 requirement assigned here. Flag gaps in FINDINGS.

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
> INVALID IF emitted before all five guided sections are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present.
>
> INVALID IF cross-namespace signal is absent from both locations when a non-requirements scout artifact was LOADED.

---

## PHASE 4: AMENDMENTS — Architect

→ BLOCKED: Phase 4 begins after [SPEC-DRAFT-COMPLETE] is present above.

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

---

## FINDINGS

→ REQUIRES: [SPEC-DRAFT-COMPLETE]

Self-review scan list:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [INERTIA-ANALYZED] present — Condition 1 names [STATUS-QUO-SNAPSHOT], [IG-REGISTER], [ID-REGISTER]; Condition 2 certified
- [STATUS-QUO-SNAPSHOT] present with all gap statements populated (structural fail rule verified)
- Cross-namespace signal at both locations (Phase 1 AND Purpose row)
- All AMPLIFIED rows carry both sub-slots populated
- Waiver chain closed: Waiver Status → R-ID WAIVED cell → Condition 2 exemption
- All five sections in prescribed order

| Finding ID | Type | Description | Severity |
|------------|------|-------------|----------|
| F-01 | [gap / contradiction / hotspot / open-question] | [description] | [low / medium / high] |

Coverage gaps, contradictions, complexity hotspots, open question register.

---

---

## V-05 — Combined: V-02 (STATUS-QUO-SNAPSHOT + C-36/C-37) + Strategy Inertia Scoping Sub-Phase

**Primary axis**: Combined — [STATUS-QUO-SNAPSHOT] full integration with C-36/C-37 (V-02) AND a Phase 1.5 STRATEGY INERTIA SCOPING sub-phase inserted between Phase 1 (PM PRE-ASSIGNMENT) and Phase 2 (INERTIA ANALYSIS). Strategy reviews [STATUS-QUO-SNAPSHOT] rows and nominates which IG-IDs to prioritize for deep inertia analysis. Strategy emits [STRATEGY-SCOPE-SEAL] gating [IG-REGISTER] enumeration. This is a sub-phase, not a full phase — Phase 1 (PM) still precedes inertia analysis, satisfying C-16/C-28.

**Hypothesis**: All 37 criteria pass. C-36 passes (Condition 1 names [STATUS-QUO-SNAPSHOT]). C-37 passes (co-located structural fail rule). C-16/C-28 pass — PM pre-assignment still occurs in Phase 1, before any inertia analysis; the Strategy sub-phase is between PM assignment and [IG-REGISTER] authoring but does not precede PM. C-17 still passes because [PM-CONTRACT-SEAL] is the named gate token with Phase 2 REQUIRES dependency. Composite 175/175. Tests whether a Strategy inertia nomination sub-step produces new aspirational patterns.

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
skill_version: v12
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

**Anti-blend instruction**: Identify the matching branch and emit its VERBATIM RESPONSE block without modification.

---

### Normal branch — `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT — PM =====

REQUIRES: [SCOUT-STATUS-TABLE] from Phase 0
PRODUCES: [PM-COVERAGE-TABLE], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 1.5 REQUIRES [PM-CONTRACT-SEAL]

**PM: scan `scout-requirements` → assign each P0 row to a named spec section → emit [PM-CONTRACT-SEAL].**

CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs populate Elimination Paths) AND Purpose section cross-namespace signal row (location 2 of 2)

### [PM-COVERAGE-TABLE] — location 1 of 1

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |
|--------|----------|-----------------|------------------|-----------------|-----------------|---------------|
| R-01 | P0 | [from artifact] | PM | [Purpose / Requirements / Design / Constraints] | [name the entry] | COVERED |
| R-02 | P0 | [from artifact] | PM | ... | ... | COVERED |
| ... | | | | | | |

**Waiver Status column**: enumerated values are `COVERED` (in scope) or `C-03 WAIVER` (scout-requirements not loaded). Named structural element — prose notes or row-level annotations do not substitute.

P0 coverage count: {n}/{n} assigned.

**Waiver propagation rule (structural)**: Requirements carrying `C-03 WAIVER` must generate `"R-ID WAIVED"` markers in [IG-REGISTER] Elimination Path cells. [INERTIA-ANALYZED] Condition 2 explicitly exempts cells marked "R-ID WAIVED."

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Each row carries `C-03 WAIVER` in the Waiver Status column.

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

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without [PM-COVERAGE-TABLE] present with P0 rows populated (or C-03 waiver stated) AND without the Waiver Status column present as a named structural element.
>
> Phase 1.5 is blocked until [PM-CONTRACT-SEAL] appears here. Phase 2 is blocked until [PM-CONTRACT-SEAL] and [STRATEGY-SCOPE-SEAL] are both present.

===== END PHASE 1 =====

---

## ===== PHASE 1.5: STRATEGY INERTIA SCOPING — Strategy =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1
PRODUCES: [STATUS-QUO-SNAPSHOT], [STRATEGY-SCOPE-SEAL]
EXIT CONDITION: [STRATEGY-SCOPE-SEAL] present
BLOCKS: Phase 2 [IG-REGISTER] authoring

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

> **[STRATEGY-SCOPE-SEAL]**
>
> INVALID IF emitted without [STATUS-QUO-SNAPSHOT] present with all nominated IG-IDs populated AND without the structural fail rule present co-located with the [STATUS-QUO-SNAPSHOT] row definition.
>
> [STRATEGY-SCOPE-SEAL] is a proof-of-work artifact. Phase 2 [IG-REGISTER] authoring is blocked until this token appears here.

===== END PHASE 1.5 =====

---

## ===== PHASE 2: INERTIA ANALYSIS — PM + Architect =====

REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 AND [STRATEGY-SCOPE-SEAL] from Phase 1.5 — if either absent, halt and name the missing token
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 3 REQUIRES [INERTIA-ANALYZED]

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
> **Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 waiver propagation rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies: [STATUS-QUO-SNAPSHOT] present with all SQ-IDs and gap statements populated (Condition 1) AND [IG-REGISTER] and [ID-REGISTER] present (Condition 1) AND every non-waived Elimination Path cell contains a named R-ID (Condition 2) AND all AMPLIFIED rows carry both sub-slots populated.
>
> Phase 3 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS — Architect =====

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED]
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
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

**PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row → confirm P0 coverage count before Architect writes prose.**

| Req ID | Priority | Spec Entry | Status |
|--------|----------|-----------|--------|
| R-01 | P0 | [entry name from PM-COVERAGE-TABLE] | ASSIGNED |
| R-02 | P0 | ... | ASSIGNED |
| ... | | | |

P0 coverage confirmed: {n}/{n}.

**Active inspection guard**: Do not confirm P0 coverage without naming the scan range (R-01 through R-{n}).

Architect: write the requirements section narrative using the pre-assigned rows above. Do not reorder.

---

### 3. Design

Detail the solution design: data model, operations/API surface, interaction patterns, extensibility points. For each P0 requirement assigned to this section, include a named design element that satisfies it. Flag gaps in FINDINGS.

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
| OQ-01 | [question] | [PM / Architect / Strategy] | [what's needed] |
| OQ-02 | | | |

---

> **[SPEC-DRAFT-COMPLETE]**
>
> INVALID IF emitted before all five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and in order, or before [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present in this document.
>
> INVALID IF cross-namespace signal is absent from both Phase 1 table (location 1 of 2) AND Purpose row (location 2 of 2) when a non-requirements scout artifact was LOADED.

===== END PHASE 3 =====

---

## ===== PHASE 4: AMENDMENTS — Architect =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: amendment list

Amendment list (minimum 2 specific, actionable items):
1. [Specific actionable amendment — name the section and the change]
2. [Second specific actionable amendment]

===== END PHASE 4 =====

---

## ===== FINDINGS =====

REQUIRES: [SPEC-DRAFT-COMPLETE]

Self-review scan list — Architect: verify each item before emitting findings:
- [PM-CONTRACT-SEAL] present with Waiver Status column in [PM-COVERAGE-TABLE]
- [STRATEGY-SCOPE-SEAL] present with [STATUS-QUO-SNAPSHOT] all gap statements populated (structural fail rule verified)
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

===== END FINDINGS =====
