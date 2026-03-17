---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v6
round: R6
date: 2026-03-15
axes_explored: C-22-proper-IG-ID-register, C-18-scripted-verbatim-fallback, C-24-cascade-directive, C-23-IG-role-binding
---

# Quest Variate — `draft-spec` — Round 6 (Rubric v6)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-22: Proper IG-ID register (distinct IG-XX guards + ID-XX defeats as parallel namespaces) | — | Splitting the inertia namespace into parallel IG-XX guard rows and ID-XX defeat rows satisfies C-22's "distinct IDs" and "parallel namespace" requirements from a single structural redesign; the AMPLIFIED threshold and proof-of-work gate survive the split unchanged |
| V-02 | C-18: Scripted verbatim fallback copy (demarcated VERBATIM RESPONSE: blockquote, two variants) | — | Wrapping the no-scout fallback in a `VERBATIM RESPONSE:` blockquote with a second scripted variant for partial-context (some artifacts loaded but requirements missing) satisfies C-18 without restructuring any phase; C-09 passes by inclusion |
| V-03 | C-24: Cascade directive on every unified role-and-source declaration | — | Appending `CASCADE TO: [location A of N] → [location B of N]` to every unified declaration satisfies C-24 (declaration specifies its own propagation) and upgrades C-15 from design aspiration to structurally declared contract; C-19 ordinal markers become load-bearing via the cascade denominator |
| V-04 | C-22 + C-23: Proper IG-ID register with inline IG-role binding | — | Adding a `Responsible Role` column to the IG register and an inline role annotation binding each IG-XX to the role that confirms ID defeat satisfies C-23; combined with C-22's parallel namespace, the risk namespace achieves structural parity with the requirements namespace at both the tracking and accountability dimensions |
| V-05 | C-22 + C-23 + C-24 + C-18 | all three new criteria + scripted copy from V-02 | Full combination: proper IG/ID parallel namespace (C-22), per-IG role binding (C-23), cascade directives on all unified declarations (C-24), scripted verbatim fallback (C-18) — expected score 170/170 |

---

## V-01 — C-22: Proper IG-ID Register (Parallel Namespaces)

**Primary axis**: C-22 — distinct IG-XX (guard) entries and ID-XX (defeat) entries as separate, parallel tables.
**Secondary axes**: none (all other R5 V-05 structure preserved exactly).
**Hypothesis**: Splitting the inertia register into a named IG table and a named ID table with distinct IG-XX and ID-XX IDs satisfies C-22's "parallel namespace" and "verifiable by counting pairs" requirements. The AMPLIFIED threshold and [INERTIA-ANALYZED] gate token survive unchanged.

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
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 1 REQUIRES [INERTIA-ANALYZED]

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each inertia guard and defeat PRODUCES [IG-REGISTER] and [ID-REGISTER].**

> Unified declaration: role PM, sources named, action named, outputs named.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Guards

Enumerate guards against lazy model defaults. Minimum 2 IG entries required. Each guard declares what the spec must NOT allow the model to default to.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Mitigation Location |
|-------|------------------------|----------------------|-------------|---------------------|
| IG-01 | [describe the status-quo default or existing alternative the model might accept without scrutiny] | [name the scout artifact that would reveal this default is insufficient] | STANDARD / AMPLIFIED [cite trigger: "feasibility < 70" or "compliance = blocking"] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [location] |
| IG-03 | [add if applicable] | | | |

> When Risk Signal = AMPLIFIED, the guard's Named Artifact Trigger must address the risk dimension (technical feasibility or compliance exposure). A generic functional trigger does not satisfy.

### [ID-REGISTER] — Inertia Defeats

One ID entry per IG entry. Each defeat entry names the condition that confirms the corresponding guard has successfully blocked the default. IG-XX and ID-XX IDs pair one-to-one.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence |
|-------|--------|-----------------|----------------------|
| ID-01 | IG-01 | [condition under which the guard is confirmed to have defeated the default — name the specific spec decision, constraint, or design element that activates the defeat] | [named evidence: scan result reference, spec entry name, coverage count, or named constraint] |
| ID-02 | IG-02 | [condition] | [evidence] |
| ID-03 | IG-03 (if present) | | |

> ID-ID defeat entries must reference their paired IG-ID. An ID-REGISTER with fewer entries than [IG-REGISTER] is structurally incomplete. Defeat Condition blank means the guard has no verifiable exit condition — not allowed.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER] present in this phase block with:
> - All IG-XX rows fully populated (Guard, Named Artifact Trigger, Risk Signal, Mitigation Location filled)
> - All ID-XX rows present (one per IG-XX) with Defeat Condition and Confirmation Evidence filled
> - Every AMPLIFIED IG-XX row addressing the named threshold dimension in its Named Artifact Trigger
> - Every IG-XX with Mitigation Location = Constraints/Design producing a named entry in that section
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies that [IG-REGISTER] and [ID-REGISTER] are present and non-empty in this block.
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

**Architect RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows. Architect RECEIVES [IG-REGISTER] and [ID-REGISTER] and incorporates mitigations. Do not re-enumerate either.**

#### 1. Purpose

**PM INSPECTS this section REQUIRES [CNS-SLOT-1-OF-2] TO VERIFY cross-namespace signal placement at location 2 of 2 PRODUCES [CNS-SLOT-2-OF-2].**

> Unified declaration inline within Purpose content block.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence summary: dominant IG-ID guard and why the spec activates its paired ID defeat — reference IG-XX and ID-XX by number] |

> [CNS-SLOT-1-OF-2] (Phase 1) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires. Inertia context blank means [IG-REGISTER]/[ID-REGISTER] are structurally disconnected from spec body.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-XX with Mitigation Location = Design, name the design element that activates its paired ID-XX defeat.

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.

[Write design content here]

IG/ID mitigation coverage:
| IG-ID | ID-ID | Guard | Defeat Condition | Mitigation Element (Design) |
|-------|-------|-------|-----------------|------------------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints from requirements, feasibility, compliance, design, and IG-XX mitigations. Name source artifact for each.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.

[List constraints with source artifact names]

IG-XX constraints: [list any constraints derived from IG-XX rows with Mitigation Location = Constraints, referencing IG-ID and ID-ID]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2 and one per IG-XX with Mitigation Location = Open Questions not fully resolved in Design or Constraints.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE] (BLOCKS if absent)
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots, and IG/ID mitigation gaps PRODUCES [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> Scan must cover: IG/ID mitigation completeness — any IG-XX with Mitigation Location filled but lacking a named design element, constraint, or open question is a gap. Any ID-XX with Defeat Condition blank is a gap.

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

---

---

## V-02 — C-18: Scripted Verbatim Fallback Copy

**Primary axis**: C-18 — demarcated VERBATIM RESPONSE: blockquote in the NOT FOUND branch; two scripted variants (all missing / requirements missing).
**Secondary axes**: none (all other R5 V-05 structure preserved exactly; Phase 0B retains the R5 INERTIA-TABLE format since C-22 is not this axis's target).
**Hypothesis**: Wrapping the no-scout fallback response in a `VERBATIM RESPONSE:` blockquote demarcation, and adding a second scripted variant for the partial-context case (some artifacts loaded but scout-requirements missing), satisfies C-18 without restructuring any phase. C-09 passes by inclusion.

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

---

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND but at least one other artifact LOADED

VERBATIM RESPONSE:
> I have some scout signals for this topic (feasibility, compliance, or market), but I don't have a requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — at least `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 0B.

===== END PHASE 0 =====

---

## ===== PHASE 0B: INERTIA ANALYSIS =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [INERTIA-TABLE], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 1 REQUIRES [INERTIA-ANALYZED]

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each IG-ID risk signal PRODUCES [INERTIA-TABLE].**

> Unified declaration: role PM, sources named, action named, output named.

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

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension. A generic functional elimination does not satisfy.
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

---

---

## V-03 — C-24: Cascade Directive on Unified Declarations

**Primary axis**: C-24 — each unified role-and-source declaration carries an explicit `CASCADE TO:` annotation naming all structural locations where the role-source pair instantiates, with ordinal denominators.
**Secondary axes**: none (R5 V-05 INERTIA-TABLE format preserved; C-22/C-23 not targeted).
**Hypothesis**: Appending `CASCADE TO: [location A of N: ...] → [location B of N: ...]` to every unified declaration satisfies C-24 (declaration specifies its own propagation). The ordinal denominators make C-19 load-bearing rather than incidental. C-15 upgrades from design aspiration to structurally declared contract because each declaration names both its own location and its cascade destination.

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

> Unified declaration: role PM, sources named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase block, [INERTIA-TABLE]] — this declaration has one structural instantiation; no cascade required.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [INERTIA-TABLE]

Enumerate inertia hypotheses as first-class IG-IDs. Minimum 2 IG-IDs required.

| IG-ID | Inertia Hypothesis | Elimination Path | Risk Signal | Spec Mitigation Required | Verdict |
|-------|-------------------|-----------------|-------------|--------------------------|---------|
| IG-01 | [describe existing alternative or status-quo] | [why it fails to satisfy the spec need — name the specific gap] | STANDARD / AMPLIFIED [cite threshold trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension. A generic functional elimination does not satisfy.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated.
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
> CASCADE TO: [location 1 of 1: this phase, [PM-COVERAGE-TABLE]] — this declaration has one structural instantiation; the Architect receives [PM-COVERAGE-TABLE] as a pre-filled contract, not a cascade destination.

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
> CASCADE TO: [location 1 of 2: this phase, [CNS-SLOT-1-OF-2]] → [location 2 of 2: Phase 3 Purpose, [CNS-SLOT-2-OF-2]]
> The cross-namespace signal field instantiates in exactly 2 structural locations. Completeness is verifiable by counting labeled instances.

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or decision] |

> If `Source artifact` is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY R-ID contradiction pairs PRODUCES [CONTRADICTION-SCAN].**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [CONTRADICTION-SCAN]] — single instantiation.

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
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies all three outputs present and non-empty.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 3 REQUIRES [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.
> CASCADE TO: [location 1 of 2: this phase, [STRATEGY-VALIDATION-TABLE]] → [location 2 of 2: Phase 3 Design, inline Strategy verdict]
> Strategy validation appears in exactly 2 structural locations — this table and the inline Design verdict.

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
> CASCADE TO: [location 2 of 2: this section, [CNS-SLOT-2-OF-2]] — completing the cascade declared in Phase 1.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence summary: dominant IG-ID and why the spec wins — reference IG-ID by number] |

> [CNS-SLOT-1-OF-2] (Phase 1) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.
> CASCADE TO: [location 1 of 1: this section, per-row coverage table] — single instantiation.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with REQUIRES SPEC MITIGATION verdict, name the design element that addresses it.

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.
> CASCADE TO: [location 2 of 2: this section, inline Strategy verdict] — completing the Strategy cascade declared in Phase 2.

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
> CASCADE TO: [location 1 of 1: this section, inline Compliance verdict] — single instantiation.

[List constraints with source artifact names]

IG-ID constraints: [list any constraints derived from REQUIRES SPEC MITIGATION rows in [INERTIA-TABLE]]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2 and one per REQUIRES SPEC MITIGATION IG-ID not fully resolved.

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
> CASCADE TO: [location 1 of 1: this phase, [FINDINGS-TABLE]] — single instantiation.
> Cascade verification check: confirm both CNS-SLOT locations are filled (location 1 of 2 in Phase 1 and location 2 of 2 in Purpose). If either is blank, add a gap finding.

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
Cascade completeness: CNS-SLOT locations 1 of 2 and 2 of 2 both filled. Strategy validation locations 1 of 2 and 2 of 2 both filled.
All sections populated. Frontmatter complete.

---

---

## V-04 — C-22 + C-23: Proper IG-ID Register with IG-Role Binding

**Primary axis**: C-22 proper (distinct IG-XX guards + ID-XX defeats as parallel namespaces) + C-23 (each IG entry names its Responsible Role inline).
**Secondary axes**: none beyond V-01 base + C-23 addition.
**Hypothesis**: Adding a `Responsible Role` column to the IG register — naming which role confirms that each ID defeat has activated — satisfies C-23. The role binding is inline on the IG entry itself, not deferred to a behavioral phase. Combined with the C-22 IG/ID split from V-01, the risk namespace achieves structural parity with the requirements namespace at both the tracking dimension (parallel IDs) and the accountability dimension (named role per guard).

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
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 1 REQUIRES [INERTIA-ANALYZED]

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each inertia guard and defeat PRODUCES [IG-REGISTER] and [ID-REGISTER].**

> Unified declaration: role PM, sources named, action named, outputs named.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Guards

Minimum 2 IG entries. Each guard names the default to block, the artifact that would reveal the gap, the risk threshold, the responsible role, and the mitigation location.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Responsible Role | Mitigation Location |
|-------|------------------------|----------------------|-------------|-----------------|---------------------|
| IG-01 | [describe the status-quo default or existing alternative the model might accept without scrutiny] | [name the scout artifact that reveals this default is insufficient] | STANDARD / AMPLIFIED [cite trigger] | [PM / Strategy / Compliance / Design / Architect] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if applicable] | | | | |

> Responsible Role: the role accountable for confirming that the paired ID defeat has activated. Must be one of the named roles in this spec. Blank = C-23 fail for this row.
> When Risk Signal = AMPLIFIED, the Named Artifact Trigger must address the risk dimension (feasibility or compliance). A generic trigger does not satisfy.

### [ID-REGISTER] — Inertia Defeats

One ID entry per IG entry. Each defeat entry names the condition confirming the guard succeeded, with named confirmation evidence and the responsible role (matching its paired IG entry).

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition under which the guard is confirmed to have defeated the default] | [named evidence: named scan result, specific spec entry, coverage count, or constraint ID] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> ID-REGISTER must have exactly as many rows as IG-REGISTER. Confirming Role in ID-XX must match Responsible Role in its paired IG-XX — role binding is verifiable by cross-referencing columns.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER] present in this phase block with:
> - All IG-XX rows fully populated including Responsible Role column (not blank)
> - All ID-XX rows present with Defeat Condition, Confirmation Evidence, and Confirming Role filled
> - ID-XX row count = IG-XX row count
> - Confirming Role in each ID-XX matches Responsible Role in paired IG-XX
> - Every AMPLIFIED IG-XX row addressing the named threshold dimension in its Named Artifact Trigger
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies that [IG-REGISTER] and [ID-REGISTER] are structurally complete and role-bound.
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
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies all three outputs present and non-empty.

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

**Architect RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows. Architect RECEIVES [IG-REGISTER] and [ID-REGISTER] and incorporates mitigations and confirmations. Do not re-enumerate either.**

#### 1. Purpose

**PM INSPECTS this section REQUIRES [CNS-SLOT-1-OF-2] TO VERIFY cross-namespace signal placement at location 2 of 2 PRODUCES [CNS-SLOT-2-OF-2].**

> Unified declaration inline within Purpose content block.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence summary: dominant IG-XX guard, its paired ID-XX defeat condition, and the Responsible Role confirming it — reference IG-XX/ID-XX by number] |

> [CNS-SLOT-1-OF-2] (Phase 1) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires.
> Inertia context blank means [IG-REGISTER]/[ID-REGISTER] and their role bindings are structurally disconnected from spec body.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-XX with Mitigation Location = Design, name the design element that activates its paired ID-XX defeat. Note the Responsible Role from [IG-REGISTER].

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.

[Write design content here]

IG/ID mitigation coverage:
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element (Design) |
|-------|-------|-------|-----------------|-----------------|------------------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints from requirements, feasibility, compliance, design, and IG-XX mitigations. Name source artifact for each.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.

[List constraints with source artifact names]

IG-XX constraints: [list any constraints from IG-XX rows with Mitigation Location = Constraints; include the Responsible Role from [IG-REGISTER] as the confirmation accountable party]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2 and one per IG-XX with Mitigation Location = Open Questions not fully resolved. Name the Responsible Role from [IG-REGISTER] as the party accountable for resolving each IG-derived question.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE] (BLOCKS if absent)
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, and role-binding completeness PRODUCES [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> Scan must cover: (a) any IG-XX in [IG-REGISTER] with Responsible Role blank; (b) any ID-XX in [ID-REGISTER] with Confirming Role not matching paired IG-XX Responsible Role; (c) any IG-XX with Mitigation Location filled but lacking a named design element, constraint, or open question.

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
IG/ID register: [IG-REGISTER] row count = [ID-REGISTER] row count. All Responsible Role columns filled.
All sections populated. Frontmatter complete.

---

---

## V-05 — All Axes: C-22 + C-23 + C-24 + C-18

**Axes**: All three new criteria (C-22 proper IG-ID register, C-23 IG-role binding, C-24 cascade directives) plus C-18 scripted verbatim fallback copy from V-02.
**Hypothesis**: Full combination of V-01 (proper IG/ID parallel namespace), V-04 additions (IG-role binding per row), V-03 (cascade directives on all unified declarations), and V-02 (scripted VERBATIM RESPONSE: blockquote). Expected score 170/170. The four-axis V-05 R5 base plus all three new criteria plus demarcated verbatim fallback: no criterion remains PARTIAL or FAIL.

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

---

### Fallback Branch A — ALL rows NOT FOUND

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

HALT until context provided. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND but at least one other artifact LOADED

VERBATIM RESPONSE:
> I have some scout signals for this topic (feasibility, compliance, or market), but I don't have a requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

HALT until user confirms or provides requirements context.

---

### Normal branch — at least `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 0B.

===== END PHASE 0 =====

---

## ===== PHASE 0B: INERTIA ANALYSIS =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 1 REQUIRES [INERTIA-ANALYZED]

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each inertia guard and defeat PRODUCES [IG-REGISTER] and [ID-REGISTER].**

> Unified declaration: role PM, sources named (`scout-feasibility` and `scout-compliance`), action named (assess guards and defeats), outputs named ([IG-REGISTER], [ID-REGISTER]).
> CASCADE TO: [location 1 of 1: this phase, [IG-REGISTER] and [ID-REGISTER]] — single instantiation; role-source pair does not cascade; the guard/defeat outputs carry their own structural propagation via Mitigation Location column.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Guards

Minimum 2 IG entries. Each guard names the default to block, the named artifact trigger, the risk threshold, the responsible role, and the mitigation location.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Responsible Role | Mitigation Location |
|-------|------------------------|----------------------|-------------|-----------------|---------------------|
| IG-01 | [describe the status-quo default or existing alternative the model might accept without scrutiny] | [name the scout artifact revealing this default is insufficient] | STANDARD / AMPLIFIED [cite trigger: "feasibility < 70" or "compliance = blocking"] | [PM / Strategy / Compliance / Design / Architect] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if applicable] | | | | |

> Responsible Role: the role accountable for confirming the paired ID defeat has activated. Must be one of the named roles. Blank = C-23 structural fail for this row.
> AMPLIFIED rows: Named Artifact Trigger must address the risk dimension. Generic triggers do not satisfy.

### [ID-REGISTER] — Inertia Defeats

One ID entry per IG entry. Each defeat names the condition confirming the guard succeeded, with named evidence and confirming role.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition under which the guard is confirmed to have defeated the default — name the specific spec decision, constraint, or design element that activates it] | [named evidence: named scan result, specific spec entry name, coverage count, or constraint ID] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> ID-REGISTER must have exactly as many rows as IG-REGISTER. Confirming Role must match Responsible Role in paired IG-XX. Cross-column verification is a valid structural check.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER] present in this phase block with:
> - All IG-XX rows fully populated including Responsible Role (not blank)
> - All ID-XX rows present with Defeat Condition, Confirmation Evidence, and Confirming Role filled
> - ID-XX row count = IG-XX row count
> - Confirming Role in each ID-XX matches Responsible Role in paired IG-XX
> - Every AMPLIFIED IG-XX addressing the named threshold dimension in its Named Artifact Trigger
> - Every IG-XX with Mitigation Location filled noting the planned spec location for its defeat activation evidence
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies [IG-REGISTER] and [ID-REGISTER] are structurally complete, role-bound, and pair-balanced in this block.
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
> CASCADE TO: [location 1 of 1: this phase, [PM-COVERAGE-TABLE]] — single instantiation; Architect receives [PM-COVERAGE-TABLE] as a pre-filled contract.

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
> CASCADE TO: [location 1 of 2: this phase, [CNS-SLOT-1-OF-2]] → [location 2 of 2: Phase 3 Purpose, [CNS-SLOT-2-OF-2]]
> The cross-namespace signal field instantiates in exactly 2 structurally independent locations. Completeness verifiable by counting labeled instances (1 of 2 + 2 of 2).

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or decision] |

> If `Source artifact` is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY R-ID contradiction pairs PRODUCES [CONTRADICTION-SCAN].**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [CONTRADICTION-SCAN]] — single instantiation.

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
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies all three outputs present and non-empty in this block.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 3 REQUIRES [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.
> CASCADE TO: [location 1 of 2: this phase, [STRATEGY-VALIDATION-TABLE]] → [location 2 of 2: Phase 3 Design, inline Strategy verdict]
> Strategy validation appears in exactly 2 structural locations. Location 2 of 2 is a cascade destination — the inline Design verdict must reference [STRATEGY-VALIDATION-TABLE] by name.

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

**Architect RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows. Architect RECEIVES [IG-REGISTER] and [ID-REGISTER] and incorporates mitigations, confirmations, and role bindings. Do not re-enumerate either.**

#### 1. Purpose

**PM INSPECTS this section REQUIRES [CNS-SLOT-1-OF-2] TO VERIFY cross-namespace signal placement at location 2 of 2 PRODUCES [CNS-SLOT-2-OF-2].**

> Unified declaration inline within Purpose content block.
> CASCADE TO: [location 2 of 2: this section, [CNS-SLOT-2-OF-2]] — completing the cascade declared in Phase 1. Two-location coverage is now structurally declared and verifiable by counting labeled instances.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence summary: dominant IG-XX guard, its Responsible Role from [IG-REGISTER], its paired ID-XX defeat condition — reference IG-XX/ID-XX by number] |

> If [CNS-SLOT-2-OF-2] is blank, C-11 fires from this location. Inertia context blank means [IG-REGISTER]/[ID-REGISTER] role bindings are disconnected from spec body.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.
> CASCADE TO: [location 1 of 1: this section, per-row coverage table] — single instantiation.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions (location 2 of 2 of Strategy cascade). For each IG-XX with Mitigation Location = Design, name the design element that activates its paired ID-XX defeat. Include the Responsible Role from [IG-REGISTER] as the confirmation accountable party.

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions against feasibility and compliance findings PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.
> CASCADE TO: [location 2 of 2: this section, inline Strategy verdict] — completing the Strategy cascade declared in Phase 2.

[Write design content here]

IG/ID mitigation coverage:
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element (Design) |
|-------|-------|-------|-----------------|-----------------|------------------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [name the design element, or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe] [references [STRATEGY-VALIDATION-TABLE] from Phase 2]

#### 4. Constraints

List constraints from requirements, feasibility, compliance, design, and IG-XX mitigations. Name source artifact for each.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.
> CASCADE TO: [location 1 of 1: this section, inline Compliance verdict] — single instantiation.

[List constraints with source artifact names]

IG-XX constraints: [list any constraints from IG-XX rows with Mitigation Location = Constraints; name the Responsible Role from [IG-REGISTER] as confirmation accountable party for each]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2 and one per IG-XX with Mitigation Location = Open Questions not fully resolved. Name the Responsible Role from [IG-REGISTER] as the party accountable for resolving each IG-derived question.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five guided sections present in order (Purpose → Requirements → Design → Constraints → Open Questions).

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE] (BLOCKS if absent)
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, role-binding completeness, and cascade completeness PRODUCES [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [FINDINGS-TABLE]] — single instantiation.
> Scan checklist:
> - IG/ID pair balance: [IG-REGISTER] row count = [ID-REGISTER] row count
> - Role binding: every IG-XX Responsible Role filled; every ID-XX Confirming Role matches its paired IG-XX
> - Cascade completeness: CNS-SLOT location 1 of 2 (Phase 1) and location 2 of 2 (Purpose) both filled; Strategy location 1 of 2 (Phase 2) and location 2 of 2 (Design inline) both filled
> - Mitigation coverage: every IG-XX with Mitigation Location filled has a named design element, constraint, or open question in the correct section

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
IG/ID register: [IG-REGISTER] row count = [ID-REGISTER] row count. All Responsible Role and Confirming Role columns filled and cross-matched.
Cascade completeness: CNS-SLOT 1 of 2 and 2 of 2 filled. Strategy 1 of 2 and 2 of 2 filled. All cascade denominators verified.
Fallback branches: Branch A and Branch B verbatim response blocks present in Phase 0.
All sections populated. Frontmatter complete.
