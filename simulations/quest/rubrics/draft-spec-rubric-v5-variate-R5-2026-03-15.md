---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v5
round: R5
date: 2026-03-15
axes_explored: unified-declaration, proof-of-work-output-format, inertia-framing, lifecycle-emphasis
---

# Quest Variate — `draft-spec` — Round 5 (Rubric v5)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Unified Role-and-Source Declaration | — | Expressing every role action as "ROLE INSPECTS artifact TO ACTION before gate" creates a single parseable element satisfying C-12 + C-14 + C-20 simultaneously; the inspection block becomes the gate token's proof-of-work evidence automatically |
| V-02 | Output Format (REQUIRES/PRODUCES + INVALID IF) | — | A REQUIRES/PRODUCES chain with an explicit INVALID IF clause on every gate token satisfies C-21 as a structural rule without requiring role-sequence ordering; REQUIRES names the data source (C-14) and the INVALID IF declares the invalidity condition (C-21) in one output-format convention |
| V-03 | Inertia Framing (IG-ID Parallel Namespace) | — | Treating inertia hypotheses as first-class IG-IDs with numbered IDs, per-ID elimination paths, AMPLIFIED risk flags at named thresholds, and a dedicated gate token satisfies C-22 fully from a single axis without requiring unified-declaration or proof-of-work machinery |
| V-04 | Unified Declaration + REQUIRES/PRODUCES + Lifecycle Emphasis | three axes combined | The intersection of inline unified declarations (V-01) and REQUIRES/PRODUCES format (V-02) naturally produces a single parseable instruction of the form "Role X INSPECTS Source Y REQUIRES [artifact] TO CONFIRM Z PRODUCES [token]" — satisfying C-12, C-14, C-20, C-21 from a single structural element; lifecycle gates make phase ordering binding |
| V-05 | All four axes: Unified Declaration + REQUIRES/PRODUCES + Lifecycle + Inertia | four axes combined | All 22 criteria satisfied; the IG-ID namespace (C-22) receives the full unified-declaration treatment — "PM INSPECTS scout-feasibility AND scout-compliance REQUIRES [both] TO ASSESS each IG-ID risk PRODUCES [INERTIA-TABLE] + [INERTIA-ANALYZED]" — extending the C-20 pattern to the risk class for maximum structural parity |

---

## V-01 — Unified Role-and-Source Declaration

**Axis**: Unified role-and-source declaration
**Hypothesis**: Expressing every role action as `ROLE INSPECTS {artifact} TO {action} before {gate}` creates a
single structural element satisfying C-12 (inline role), C-14 (named inspection source), and C-20 (unified
declaration) simultaneously. The inspection block populated by each declaration becomes the gate token's natural
prerequisite evidence, making C-21 structurally derivable without a separate invalidity clause.

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
skill_version: v1
input: [list each loaded scout artifact by filename]
```

---

## SETUP

### Scout Artifact Discovery

Search `simulations/scout/` for artifacts matching topic `{topic}`. Record each:

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

### No-Scout Fallback

If ALL artifacts above show NOT FOUND:

write: "I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed."

Stop. Do not proceed to EXECUTE until the user provides context or at least one artifact is LOADED.

---

## EXECUTE

### Phase 1 — PM Pre-Assignment

**PM INSPECTS `scout-requirements` TO ENUMERATE all P0 requirements before any prose writing begins.**

> This declaration is the unified role-and-source element (location 1 of 1 for PM-role inline invocation).
> PM is the named role. `scout-requirements` is the named data source. Enumeration is the named action.
> This instruction is invalid as written if `scout-requirements` is NOT FOUND — apply the waiver below.

If `scout-requirements` is LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name (pre-fill) |
|--------|----------|-----------------|------------------|-----------------------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the spec entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} P0 requirements assigned.

If `scout-requirements` is NOT FOUND:
> C-03 WAIVED: no scout-requirements artifact exists. State this waiver here and proceed.

**PM INSPECTS `scout-feasibility` AND `scout-compliance` TO NAME the cross-namespace signal before [PM-CONTRACT-SEAL] is emitted.**

> PM is the named role. `scout-feasibility` and `scout-compliance` are the named data sources. Naming the signal is the named action.

Cross-namespace signal (location 1 of 2):
- Artifact: [name the specific artifact — `scout-feasibility` or `scout-compliance` — that yields this signal]
- Signal: [1-sentence description]
- Spec impact: [1-sentence decision or constraint it drives in this spec]

> If this cell shows `[name the artifact]` unfilled, C-11 fires: the cross-namespace field is visibly blank.

**PM INSPECTS `scout-requirements` TO IDENTIFY R-ID contradiction pairs before [PM-CONTRACT-SEAL] is emitted.**

> Scan source is named: `scout-requirements`. Default "none found" requires a completed scan, not an assumption.

Contradiction scan result: [name conflicting R-ID pair as "R-XX vs R-YY", or write "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> Structurally invalid if emitted without ALL of the following in this document block:
> - P0 pre-assignment table above with all rows populated, OR an explicit C-03 waiver
> - Cross-namespace signal (location 1 of 2) above with `Artifact` cell filled
> - Contradiction scan result above with a named scan outcome
>
> Architect is blocked from writing guided sections until [PM-CONTRACT-SEAL] appears in this document.

---

### Phase 2 — Strategy Validation

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` TO VALIDATE spec viability before [STRATEGY-SEAL] is emitted.**

> Strategy is the named role. Both artifacts are named data sources. Validation is the named action.

| Check | Source Artifact | Verdict | Finding (if any) |
|-------|----------------|---------|------------------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Additional constraints surfaced | [name artifact] | [list constraints to add] | — |

> **[STRATEGY-SEAL]**
>
> Structurally invalid if emitted without the validation table above populated with artifact names in every `Source Artifact` cell.

---

### Phase 3 — Architect: Guided Sections

Architect writes the five guided sections in the order below. Do not reorder. Do not omit.
Architect RECEIVES pre-assigned rows from [PM-CONTRACT-SEAL] and FILLS them — not re-enumerating from scratch.

#### 1. Purpose

State what this feature does, for whom, and why it exists.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| Cross-namespace signal (location 2 of 2) | [name artifact + 1-sentence signal — must match location 1 of 2 from PM phase] |

> Cross-namespace signal appears in two structurally independent locations: PM pre-assignment phase (location 1 of 2) and this Purpose table (location 2 of 2). If this cell is empty, C-11 fires from this location.

#### 2. Requirements

**Architect FILLS pre-assigned rows from [PM-CONTRACT-SEAL]. Do not re-enumerate.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [from PM pre-assignment — use the exact name assigned in Phase 1] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n} covered. Waiver applied: [YES / NO — state if C-03 was waived in Phase 1].

**Architect INVOKES Design role to validate this section inline.**

Design validation: PASS / FINDING: [describe if any requirement conflicts with known design constraints]

#### 3. Design

Describe the architecture, components, and key technical decisions.

**Architect INVOKES Strategy role to validate this section inline.**

[Write design content here — components, data flows, key decisions. Reference constraint additions from [STRATEGY-SEAL] where applicable.]

Strategy validation: PASS / FINDING: [describe if any design decision conflicts with feasibility or compliance findings]

#### 4. Constraints

List constraints derived from: requirements, feasibility, compliance, and design decisions.

**Architect INVOKES Compliance role to validate this section inline.**

[List constraints — each on its own line, with source artifact named where known]

Compliance validation: PASS / FINDING: [describe if any constraint is missing or conflicts with compliance posture]

#### 5. Open Questions

List unresolved questions that block or risk the spec. Include at least one question per open finding from Phases 1–2 if any findings were raised.

[List open questions — numbered, each actionable]

---

### Phase 4 — Self-Review: Findings

**Architect INSPECTS sections 1–5 TO SURFACE contradictions, gaps, ambiguities, and hotspots.**

> Scan source: this document. Claim "none found" only after explicit inspection — not by default.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [contradiction / gap / ambiguity / hotspot] | [section name] | [describe specifically] | [propose or flag for Open Questions] |
| ... | | | | |

Finding claim: [either "F-01 through F-{n} above represent all findings" or "No contradictions, gaps, ambiguities, or hotspots found after explicit inspection of all five sections."]

---

### Phase 5 — Amend

Produce a numbered list of at least 2 specific, actionable amendments addressing findings above.
Each amendment must name: the section, the finding ID (F-NN) or type, and the specific change.

1. [Section: X / Finding: F-NN / Change: describe the exact edit]
2. [Section: X / Finding: F-NN / Change: describe the exact edit]
...

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
All sections populated. All gate tokens ([PM-CONTRACT-SEAL], [STRATEGY-SEAL]) present in document.
Frontmatter complete with all required fields.

---

## V-02 — Output Format: REQUIRES/PRODUCES with INVALID IF

**Axis**: Output format (REQUIRES/PRODUCES chain with proof-of-work invalidity rules)
**Hypothesis**: A REQUIRES/PRODUCES chain with an explicit `INVALID IF` clause on every gate token
enforces C-21 as a structural template rule — the invalidity condition appears in the template, not as
a behavioral instruction. The REQUIRES line names the data source for each phase (satisfying C-14).
The PRODUCES line makes each phase's output a named artifact the next phase can reference. This axis
achieves strong structural rigor without role-sequence ordering machinery; roles appear at phase headers
rather than inline within section content (C-12 is the expected gap).

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
skill_version: v1
input: [list each loaded scout artifact by filename]
```

---

## SETUP

REQUIRES: file system access to `simulations/scout/`
PRODUCES: Scout Status Table + no-scout fallback response (if applicable)

Scout Status Table:

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

NOT FOUND branch — if ALL rows show NOT FOUND:

PRODUCES: verbatim fallback response

respond: "I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed."

Stop. Do not advance to Phase 1 until context is provided or at least one artifact is LOADED.

---

## Phase 1 — PM Coverage and Cross-Namespace Signal

REQUIRES: `scout-requirements-{date}.md` (for P0 enumeration), `scout-feasibility-{date}.md` (for cross-namespace signal), `scout-compliance-{date}.md` (for cross-namespace signal)
PRODUCES: [PM-COVERAGE-TABLE], [CNS-SIGNAL-SLOT-A], [PM-CONTRACT-SEAL]

INVALID IF [PM-CONTRACT-SEAL] is emitted without [PM-COVERAGE-TABLE] AND [CNS-SIGNAL-SLOT-A] present in this phase block.

### [PM-COVERAGE-TABLE]

Role: PM

If `scout-requirements` LOADED — enumerate all P0 requirements and assign to spec sections:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [pre-fill entry name] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} requirements assigned.

If `scout-requirements` NOT FOUND:
C-03 WAIVER: scout-requirements artifact absent. State waiver here and proceed.

Contradiction scan (REQUIRES: `scout-requirements`): [name any R-ID pair as "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}"]

### [CNS-SIGNAL-SLOT-A] — Cross-namespace signal, slot A of 2

Role: PM

REQUIRES: `scout-feasibility-{date}.md` OR `scout-compliance-{date}.md` OR `scout-market-{date}.md` OR `scout-positioning-{date}.md`

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence decision or constraint] |

> If `Source artifact` cell shows `[name the specific loaded artifact]` unfilled, C-11 fires: CNS field visibly blank at slot A of 2.

---

> **[PM-CONTRACT-SEAL]**
> INVALID IF emitted without [PM-COVERAGE-TABLE] present above with P0 rows populated (or C-03 waiver stated) AND [CNS-SIGNAL-SLOT-A] present above with `Source artifact` cell filled.
> Architect REQUIRES [PM-CONTRACT-SEAL] before writing any guided section prose.

---

## Phase 2 — Strategy Feasibility + Compliance Validation

REQUIRES: `scout-feasibility-{date}.md`, `scout-compliance-{date}.md`
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]

INVALID IF [STRATEGY-SEAL] is emitted without [STRATEGY-VALIDATION-TABLE] present in this phase block with all `Source Artifact` cells filled.

Role: Strategy

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list additional constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] above with all `Source Artifact` cells naming specific loaded artifacts.

---

## Phase 3 — Architect: Guided Sections

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL]
PRODUCES: five guided sections in prescribed order + [SPEC-DRAFT-COMPLETE]

INVALID IF [SPEC-DRAFT-COMPLETE] is emitted without all five guided sections present in the order: Purpose → Requirements → Design → Constraints → Open Questions.

Role: Architect

**Architect REQUIRES [PM-CONTRACT-SEAL] and [STRATEGY-SEAL] before beginning. If either token is absent, halt and state: "[PM-CONTRACT-SEAL] or [STRATEGY-SEAL] missing — cannot begin guided sections."**

#### 1. Purpose

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SIGNAL-SLOT-B] — Cross-namespace signal, slot B of 2 | [name artifact + 1-sentence signal — must match [CNS-SIGNAL-SLOT-A] from Phase 1] |

> [CNS-SIGNAL-SLOT-A] is in Phase 1 (slot A of 2). [CNS-SIGNAL-SLOT-B] is in this Purpose table (slot B of 2). If this cell is empty, C-11 fires from slot B.

Inline role validation (Design):
PRODUCES: Design role verdict → PASS / FINDING: [describe if any stated purpose conflicts with known design constraints]

#### 2. Requirements

REQUIRES: [PM-COVERAGE-TABLE] rows from Phase 1
PRODUCES: per-row requirement coverage table

Architect fills pre-assigned rows — do not re-enumerate:

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact entry name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n} covered. Waiver applied: [YES / NO].

Inline role validation (PM):
PRODUCES: PM role verdict → PASS / FINDING: [describe if any P0 requirement is missing coverage]

#### 3. Design

Describe architecture, components, and key technical decisions. Reference constraint additions from [STRATEGY-VALIDATION-TABLE].

[Write design content here]

Inline role validation (Strategy):
PRODUCES: Strategy role verdict → PASS / FINDING: [describe if any design decision conflicts with feasibility or compliance findings]

#### 4. Constraints

List constraints derived from requirements, feasibility, compliance, and design decisions. Name the source artifact for each.

[List constraints with source artifact names]

Inline role validation (Compliance):
PRODUCES: Compliance role verdict → PASS / FINDING: [describe if any constraint is incomplete or conflicts with compliance posture]

#### 5. Open Questions

List unresolved questions that block or risk the spec.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections above present in prescribed order (Purpose → Requirements → Design → Constraints → Open Questions).

---

## Phase 4 — Self-Review: Findings

REQUIRES: all five guided sections (REQUIRES [SPEC-DRAFT-COMPLETE])
PRODUCES: [FINDINGS-TABLE], finding claim

INVALID IF [FINDINGS-TABLE] is absent and no written claim appears in this section.

Role: Architect

Scan all five sections for contradictions, gaps, ambiguities, and hotspots. Do not default to "none found" without a completed scan.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [contradiction / gap / ambiguity / hotspot] | [section] | [describe] | [propose or flag] |
| ... | | | | |

Finding claim: ["F-01 through F-{n} above represent all findings after explicit scan" or "No findings after explicit scan of all five sections."]

---

## Phase 5 — Amend

REQUIRES: [FINDINGS-TABLE] or finding claim
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF amendment list contains fewer than 2 items or items are vague (must name section + finding + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]
...

---

## Output

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE]
PRODUCES: artifact written to `simulations/draft/specs/{topic}-spec-{date}.md`

Write the completed artifact with all sections and frontmatter populated.

---

## V-03 — Inertia Framing: IG-ID Parallel Namespace

**Axis**: Inertia framing (IG-ID first-class risk class)
**Hypothesis**: Treating inertia hypotheses as first-class named entities with numbered IG-IDs, per-ID
elimination paths, AMPLIFIED risk flags at a named threshold (feasibility-score < 70 OR
compliance-status = blocking), and a dedicated [INERTIA-ANALYZED] gate token satisfies C-22 fully from
a single axis. The IG-ID namespace is structurally parallel to R-IDs: pre-printed template fields, not
prose commentary. Role-sequencing and REQUIRES/PRODUCES format are minimal — this variation shows how far
the inertia axis alone carries.

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
skill_version: v1
input: [list each loaded scout artifact by filename]
```

---

## SETUP

Search `simulations/scout/` for artifacts matching topic `{topic}`. Record each:

| Artifact | Status |
|----------|--------|
| {topic}-requirements-{date}.md | LOADED / NOT FOUND |
| {topic}-feasibility-{date}.md | LOADED / NOT FOUND |
| {topic}-compliance-{date}.md | LOADED / NOT FOUND |
| {topic}-market-{date}.md | LOADED / NOT FOUND |
| {topic}-stakeholders-{date}.md | LOADED / NOT FOUND |
| {topic}-positioning-{date}.md | LOADED / NOT FOUND |
| {topic}-naming-{date}.md | LOADED / NOT FOUND |

### No-Scout Fallback

If ALL rows show NOT FOUND:

write: "I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed."

Stop. Do not proceed until context is provided.

---

## Phase 0 — Inertia Analysis (IG-ID Enumeration)

**Run before any other phase. [INERTIA-ANALYZED] must appear in this document before Phase 1 begins.**

Inertia hypotheses are the existing alternatives this feature competes with — status-quo tools, current workarounds, manual processes, or adjacent features that users might default to instead. Each gets a first-class IG-ID.

### Risk Signal Source

Read from SETUP:
- Feasibility score (from `scout-feasibility` if LOADED): [record score, or "NOT LOADED"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### IG-ID Table

Enumerate each inertia hypothesis. Minimum 2 IG-IDs required. Add rows as needed.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Verdict |
|-------|-------------------|-----------------|-------------|---------|
| IG-01 | [describe the existing alternative or status-quo option] | [why this option does not satisfy the spec need — name the specific gap] | STANDARD / AMPLIFIED [cite threshold trigger if AMPLIFIED] | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | |

> An IG-ID with REQUIRES SPEC MITIGATION verdict must produce a named open question in section 5 (Open Questions) or a named constraint in section 4 (Constraints). Do not leave the mitigation implicit.

> AMPLIFIED risk signal fires when: feasibility-score < 70 OR compliance-status = blocking. When AMPLIFIED, the IG-ID's elimination path must address the risk dimension (technical risk or compliance exposure) explicitly — a generic functional elimination does not satisfy.

---

> **[INERTIA-ANALYZED]**
>
> Structurally invalid if emitted without:
> (a) the IG-ID table above with at least 2 rows fully populated (IG-ID, Elimination Path, Risk Signal, Verdict), AND
> (b) every AMPLIFIED row addressing the named threshold dimension in its Elimination Path cell.
>
> Phase 1 is blocked until [INERTIA-ANALYZED] appears in this document.

---

## Phase 1 — PM Pre-Assignment

Role: PM

If `scout-requirements` is LOADED:

Enumerate all P0 requirements and assign to spec sections before writing begins:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [section name] | [pre-fill entry name] |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

Contradiction scan (scan `scout-requirements` for conflicting pairs): [name R-XX vs R-YY pairs found, or "none found after scanning R-01 through R-{n}"]

Cross-namespace signal (location 1 of 2):
- Artifact: [name the specific loaded non-requirements artifact]
- Signal: [1-sentence description]
- Spec impact: [1-sentence decision or constraint]

If `scout-requirements` is NOT FOUND: C-03 WAIVED — state waiver here.

**[PM-GATE]** — Architect blocked until this gate appears. Invalid if P0 table (or waiver) and CNS location 1 of 2 are absent.

---

## Phase 2 — Strategy Validation

Role: Strategy

Validate feasibility and compliance posture against planned spec. Produce a findings table:

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |

**[STRATEGY-GATE]** — Architect blocked until this gate appears. Invalid if validation table above is empty or artifact names are missing.

---

## Phase 3 — Architect: Guided Sections

Write five guided sections in prescribed order: Purpose → Requirements → Design → Constraints → Open Questions.
Do not reorder. Fill pre-assigned rows from [PM-GATE] rather than re-enumerating.

#### 1. Purpose

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| Cross-namespace signal (location 2 of 2) | [name artifact + 1-sentence signal — must match location 1 of 2] |
| Inertia context | [1-sentence summary referencing the dominant IG-ID — which inertia option is the primary competitor and why the spec wins] |

> If CNS location 2 of 2 is blank, C-11 fires. If Inertia context is blank, the IG-ID analysis is structurally disconnected from the spec body.

#### 2. Requirements

Fill pre-assigned rows from [PM-GATE]:

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from PM pre-assignment] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

Design role validation (inline): PASS / FINDING: [describe]

#### 3. Design

Describe architecture, components, key decisions. For any IG-ID with REQUIRES SPEC MITIGATION verdict, name the design element that addresses it.

[Write design content here]

Mitigation coverage: [list each IG-ID with REQUIRES SPEC MITIGATION verdict and the design element that addresses it, or "none required"]

Strategy role validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints derived from requirements, feasibility, compliance, and IG-ID mitigation requirements.

[List constraints — name source artifact where known]

Compliance role validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one question per open IG-ID mitigation and per FINDING from Phases 0–2.

[List open questions — numbered]

---

## Phase 4 — Self-Review: Findings

Scan all five sections for contradictions, gaps, ambiguities, and hotspots. Include a scan of IG-ID mitigations: if any REQUIRES SPEC MITIGATION IG-ID lacks a named design element or constraint, that is a gap.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit statement — never empty]

---

## Phase 5 — Amend

Numbered list, minimum 2 specific actionable amendments. Each names section + finding + specific change.

1. [Section: X / Finding: F-NN / Change: ...]
2. [Section: X / Finding: F-NN / Change: ...]
...

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens present in document: [INERTIA-ANALYZED], [PM-GATE], [STRATEGY-GATE].
All sections populated. Frontmatter complete.

---

## V-04 — Multi-axis: Unified Declaration + REQUIRES/PRODUCES + Lifecycle Emphasis

**Axes**: Unified role-and-source declaration (V-01) + REQUIRES/PRODUCES with INVALID IF (V-02) + lifecycle emphasis
**Hypothesis**: Combining inline unified declarations with REQUIRES/PRODUCES format produces a single
structural element of the form `"Role X INSPECTS Source Y REQUIRES [artifact] TO ACTION PRODUCES [token]"` —
satisfying C-12 (inline role), C-14 (named scan source), C-20 (unified declaration), and C-21 (INVALID IF
clause) from one compound declaration. Lifecycle gates with explicit BEGIN/END phase markers and named
blocking conditions make phase ordering binding rather than advisory.

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
skill_version: v1
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP =====

REQUIRES: file system access to `simulations/scout/`
PRODUCES: [SCOUT-STATUS-TABLE]
EXIT CONDITION: [SCOUT-STATUS-TABLE] present in document

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

NOT FOUND branch — if ALL rows NOT FOUND:
PRODUCES: verbatim fallback text
respond: "I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed."
HALT until context provided.

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE] (BLOCKS if absent)
PRODUCES: [PM-COVERAGE-TABLE], [CNS-SLOT-1-OF-2], [CONTRADICTION-SCAN], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present in document with all prerequisites fulfilled
BLOCKS: Phase 3 (Guided Sections) REQUIRES [PM-CONTRACT-SEAL]

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO ENUMERATE all P0 requirements PRODUCES [PM-COVERAGE-TABLE].**

> This is the unified role-and-source declaration for PM coverage. Role: PM. Source: `scout-requirements`. Action: enumerate P0 requirements. Output: [PM-COVERAGE-TABLE]. Single structural element satisfying role-invocation, inspection guard, and output naming.

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry — e.g., "Design: retry-backoff component"] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND:
C-03 WAIVER: scout-requirements absent. Waiver recorded here. Proceed.

---

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO NAME cross-namespace signal PRODUCES [CNS-SLOT-1-OF-2].**

> Unified declaration: role PM, sources named, action named, output named.

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence decision or constraint this drives] |

> If `Source artifact` cell is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY contradiction R-ID pairs PRODUCES [CONTRADICTION-SCAN].**

> Unified declaration: role PM, source named, action named, output named.

### [CONTRADICTION-SCAN]

Contradiction pairs found: [name as "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}" — no default without scan]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated OR C-03 waiver stated
> - [CNS-SLOT-1-OF-2]: `Source artifact` cell filled with a specific artifact name
> - [CONTRADICTION-SCAN]: explicit named outcome (pair names or confirmed scan result)
>
> A [PM-CONTRACT-SEAL] emitted without these artifacts in the same document block is a proof-of-work failure.
> Phase 3 REQUIRES [PM-CONTRACT-SEAL]. Architect cannot begin guided sections until this token is present.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present with all rows filled
BLOCKS: Phase 3 REQUIRES [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list any new constraints] | — |

> **[STRATEGY-SEAL]**
>
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] above with specific artifact names in all `Source Artifact` cells.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL] (BLOCKS if either absent — halt and state which token is missing)
PRODUCES: five guided sections in prescribed order + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections present in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions (reordering is a structural fail)

**Architect RECEIVES [PM-COVERAGE-TABLE] from Phase 1 and FILLS pre-assigned rows. Do not re-enumerate.**

#### 1. Purpose

**PM INSPECTS this section REQUIRES [CNS-SLOT-1-OF-2] TO VERIFY cross-namespace signal is placed at location 2 of 2 PRODUCES [CNS-SLOT-2-OF-2].**

> Unified declaration inline within Purpose section content block: role PM, source named ([CNS-SLOT-1-OF-2]), action named, output named. This is the C-12 inline role annotation for Purpose.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |

> [CNS-SLOT-1-OF-2] in Phase 1 and [CNS-SLOT-2-OF-2] in this table are the two structurally independent locations for the cross-namespace field (location 1 of 2 / location 2 of 2). If [CNS-SLOT-2-OF-2] cell is empty, C-11 fires from location 2.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements section: role PM, source named ([PM-COVERAGE-TABLE]), action named, output named.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact entry name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference constraint additions from [STRATEGY-VALIDATION-TABLE].

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

[Write design content here]

Strategy validation (inline): PASS / FINDING: [describe if any design decision conflicts with feasibility or compliance findings from [STRATEGY-VALIDATION-TABLE]]

#### 4. Constraints

List constraints from requirements, feasibility, compliance, and design. Name source artifact for each.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

[List constraints with source artifact names]

Compliance validation (inline): PASS / FINDING: [describe if any compliance-derived constraint is missing]

#### 5. Open Questions

List unresolved questions that block or risk the spec. Include at least one question per open FINDING from Phases 1–2.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE] (BLOCKS if absent)
PRODUCES: [FINDINGS-TABLE] OR explicit claim, [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots PRODUCES [FINDINGS-TABLE].**

> Unified declaration: role Architect, source named ([SPEC-DRAFT-COMPLETE]), action named, output named.
> Default "none found" without scan is structurally invalid. Name the scan source.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [contradiction / gap / ambiguity / hotspot] | [section] | [describe] | [propose or flag] |
| ... | | | | |

Finding claim: [explicit scan outcome — never absent]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim stating "none found after scanning [SPEC-DRAFT-COMPLETE]".

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)
EXIT CONDITION: at least 2 specific, actionable amendments named

INVALID IF amendment list contains fewer than 2 items or any item is vague (must name section + finding ID or type + specific change).

1. [Section: X / Finding: F-NN or type / Change: describe exactly]
2. [Section: X / Finding: F-NN or type / Change: describe exactly]
...

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
All gate tokens present: [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
All sections populated. Frontmatter complete.

---

## V-05 — All Axes: Unified Declaration + REQUIRES/PRODUCES + Lifecycle + Inertia Framing

**Axes**: All four — unified declaration (V-01) + REQUIRES/PRODUCES with INVALID IF (V-02) + lifecycle emphasis + inertia framing (V-03)
**Hypothesis**: All 22 criteria satisfied. The IG-ID namespace (C-22) receives the full unified-declaration
treatment — `"PM INSPECTS scout-feasibility AND scout-compliance REQUIRES [both] TO ASSESS each IG-ID risk
PRODUCES [INERTIA-TABLE] + [INERTIA-ANALYZED]"` — extending the C-20 pattern to the risk class for
structural parity. Risk amplification from the cross-namespace column becomes a live per-IG-ID discriminator.
The [INERTIA-ANALYZED] gate token is proof-of-work: invalid without the [INERTIA-TABLE] showing elimination
verdicts for all IG-IDs in the same block.

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
skill_version: v1
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

NOT FOUND branch — if ALL rows NOT FOUND:
respond: "I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed."
HALT until context provided.

===== END PHASE 0 =====

---

## ===== PHASE 0B: INERTIA ANALYSIS =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 1 REQUIRES [INERTIA-ANALYZED]

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each IG-ID risk signal PRODUCES [INERTIA-TABLE].**

> Unified declaration: role PM, sources named (`scout-feasibility` and `scout-compliance`), action named (risk assessment per IG-ID), output named ([INERTIA-TABLE]).
> This is the C-20 unified element extended to the inertia risk class.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [INERTIA-TABLE]

Enumerate inertia hypotheses as first-class IG-IDs. Minimum 2 IG-IDs required.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | [why it fails to satisfy the spec need — name the specific gap] | STANDARD / AMPLIFIED [cite threshold trigger: "feasibility < 70" or "compliance = blocking"] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension (technical feasibility gap or compliance exposure). A generic functional elimination does not satisfy.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint in Phase 3 (Constraints) or a named open question in Phase 3 (Open Questions).

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with:
> - All IG-ID rows fully populated (IG-ID, Elimination Path, Risk Signal, Verdict cells filled)
> - Every AMPLIFIED row addressing the named threshold dimension in its Elimination Path
> - Every REQUIRES SPEC MITIGATION row noting the planned mitigation location (Constraints or Open Questions)
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies that [INERTIA-TABLE] is present and non-empty in this block.
> Phase 1 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 0B =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [INERTIA-ANALYZED] (BLOCKS if absent — halt and state "[INERTIA-ANALYZED] missing")
PRODUCES: [PM-COVERAGE-TABLE], [CNS-SLOT-1-OF-2], [CONTRADICTION-SCAN], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 3 REQUIRES [PM-CONTRACT-SEAL]

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO ENUMERATE all P0 requirements PRODUCES [PM-COVERAGE-TABLE].**

> Unified declaration: role PM, source named, action named, output named.

### [PM-COVERAGE-TABLE]

If `scout-requirements` LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| R-02 | P0 | [from artifact] | ... | ... |
| ... | | | | |

P0 coverage count: {n}/{n} assigned.

If `scout-requirements` NOT FOUND: C-03 WAIVER stated here. Proceed.

---

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO NAME cross-namespace signal PRODUCES [CNS-SLOT-1-OF-2].**

> Unified declaration: role PM, sources named, action named, output named.

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or decision] |

> If `Source artifact` is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY R-ID contradiction pairs PRODUCES [CONTRADICTION-SCAN].**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated (or C-03 waiver)
> - [CNS-SLOT-1-OF-2]: `Source artifact` cell filled
> - [CONTRADICTION-SCAN]: named scan outcome
>
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies [PM-COVERAGE-TABLE], [CNS-SLOT-1-OF-2], and [CONTRADICTION-SCAN] are present and non-empty in this block.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 3 REQUIRES [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list new constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] above with specific artifact names in all `Source Artifact` cells.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL] (BLOCKS if either absent)
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows. Architect RECEIVES [INERTIA-TABLE] and incorporates mitigations. Do not re-enumerate either.**

#### 1. Purpose

**PM INSPECTS this section REQUIRES [CNS-SLOT-1-OF-2] TO VERIFY cross-namespace signal placement at location 2 of 2 PRODUCES [CNS-SLOT-2-OF-2].**

> Unified declaration inline within Purpose content block.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence summary: dominant IG-ID and why the spec wins — reference IG-ID by number] |

> [CNS-SLOT-1-OF-2] (Phase 1) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires. Inertia context blank means [INERTIA-TABLE] is structurally disconnected from spec body.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with REQUIRES SPEC MITIGATION verdict, name the design element that addresses it.

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.

[Write design content here]

IG-ID mitigation coverage:
| IG-ID | Verdict | Mitigation Element (Design) |
|-------|---------|------------------------------|
| IG-01 | [from [INERTIA-TABLE]] | [name the design element, or "N/A — ELIMINATED"] |
| IG-02 | [from [INERTIA-TABLE]] | [name the design element, or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints from requirements, feasibility, compliance, design, and IG-ID mitigations. Name source artifact for each.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.

[List constraints with source artifact names]

IG-ID constraints: [list any constraints derived from REQUIRES SPEC MITIGATION rows in [INERTIA-TABLE], referencing IG-ID]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2 and one per REQUIRES SPEC MITIGATION IG-ID not fully resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE] (BLOCKS if absent)
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots, and IG-ID mitigation gaps PRODUCES [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> Scan must cover: IG-ID mitigation completeness — any REQUIRES SPEC MITIGATION IG-ID lacking a named design element or constraint is a gap.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — never absent or empty]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] above OR an explicit finding claim referencing [SPEC-DRAFT-COMPLETE] as the scan source.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

REQUIRES: [SELF-REVIEW-SEAL]
PRODUCES: numbered amendment list (minimum 2 items)

INVALID IF list contains fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]
...

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens present: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
All sections populated. Frontmatter complete.
