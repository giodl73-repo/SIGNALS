---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v7
round: R7
date: 2026-03-15
axes_explored: C-25-two-branch-verbatim, C-25-expanded-branch-B, phrasing-register-concise, C-25-plus-C-22, full-combination-175
---

# Quest Variate — `draft-spec` — Round 7 (Rubric v7)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-25: Two-branch verbatim fallback on minimal base (no C-22/C-23/C-24) | — | Adding structurally named Branch A and Branch B each with their own VERBATIM RESPONSE: blockquote to the minimal-base Phase 0 satisfies C-25 in isolation; C-09 and C-18 pass by inclusion; the parallel IG/ID register from R6 V-01 is NOT included, allowing C-25 to be scored independently |
| V-02 | C-25 expanded Branch B: sub-conditional within Branch B based on which non-requirements artifacts are loaded | — | Adding artifact-specific copy within Branch B (distinct VERBATIM RESPONSE: text when feasibility-only vs compliance-only vs both loaded) without adding a full third branch explores the upper bound of C-25; hypothesis: this yields a C-25-plus signal where sub-conditional specificity strengthens the verbatim copy without requiring a third structural branch |
| V-03 | Phrasing register: concise imperative (all structural elements preserved, bureaucratic framing removed) | C-25 two-branch fallback carried forward | Rewriting all phase headers, gate token declarations, and unified role declarations in a concise imperative register ("PM: scan X, fill Y") while preserving every structural element (tables, gate tokens, role columns, ordinal labels) still satisfies all rubric criteria; tests whether the formal REQUIRES/PRODUCES/BLOCKS syntax is load-bearing or cosmetic |
| V-04 | C-25 + C-22: two-branch verbatim fallback + parallel IG/ID registers | (C-23, C-24 excluded to isolate the two-axis combination) | Combining the two-branch verbatim fallback (C-25) with the parallel IG/ID namespace (C-22) without adding role binding (C-23) or cascade directives (C-24) tests whether the C-25 and C-22 axes interact positively; hypothesis: Phase 0 context-branching and Phase 0B register-splitting reinforce each other without requiring the accountability and propagation axes |
| V-05 | C-22 + C-23 + C-24 + C-25 full combination | All four axes from V-01 through V-04 carried forward | R6 V-05 already contains all four axes implicitly; this variation confirms it scores 175/175 under v7 rubric criteria by making C-25's two-branch structure explicit with named branch headers and distinct VERBATIM RESPONSE: blocks per the v7 C-25 pass condition; target: 175/175 with no partial criteria |

---

## V-01 — C-25: Two-Branch Verbatim Fallback (Minimal Base)

**Primary axis**: C-25 — structurally named Branch A (all NOT FOUND) and Branch B (requirements NOT FOUND, others LOADED), each with its own demarcated `VERBATIM RESPONSE:` block.
**Secondary axes**: none — Phase 0B uses merged [INERTIA-TABLE] (R6 V-02 base), no C-22/C-23/C-24.
**Hypothesis**: C-25 passes purely from the two-branch structure in Phase 0. C-09 and C-18 pass by inclusion. The merged [INERTIA-TABLE] from the V-02 base is unchanged, so any C-22/C-23/C-24 criteria remain at their R6 V-02 values (C-22 ✗, C-23 ✗, C-24 ✗). This isolates C-25's marginal contribution.

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
| IG-01 | [describe existing alternative or status-quo] | [why it fails to satisfy the spec need — name the specific gap] | STANDARD / AMPLIFIED [cite threshold trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension. A generic functional elimination does not satisfy.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated (IG-ID, Elimination Path, Risk Signal, Verdict cells filled).
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

> [CNS-SLOT-1-OF-2] (Phase 1) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2. If [CNS-SLOT-2-OF-2] is blank, C-11 fires.

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
Fallback branches: Branch A and Branch B verbatim response blocks present in Phase 0.
All sections populated. Frontmatter complete.

---

---

## V-02 — C-25 Expanded Branch B: Artifact-Specific Verbatim Copy

**Primary axis**: C-25 expanded — Branch B is sub-conditioned on which specific non-requirements artifacts are loaded, producing artifact-aware VERBATIM RESPONSE: copy within Branch B rather than generic "some signals" copy.
**Secondary axes**: none — merged [INERTIA-TABLE] from V-01/R6-V-02 base; no C-22/C-23/C-24.
**Hypothesis**: Within Branch B, differentiating response copy by which non-requirements artifacts are present (feasibility only / compliance only / both / market or others) creates a C-25-plus signal: verbatim copy that names specific available signals is more model-ready than generic copy. A single-verbatim-block Branch B with artifact-specific appended prose does not satisfy; each sub-condition has its own demarcated block.

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

Branch B sub-conditional: inspect which non-requirements artifacts are LOADED and emit the matching block verbatim.

**Branch B-1 — feasibility AND compliance both LOADED (requirements absent)**

VERBATIM RESPONSE:
> I have feasibility and compliance signals for this topic but no requirements artifact. I can write a spec grounded in technical constraints and compliance posture, but P0 requirement coverage will be waived — I'll state the waiver explicitly. Should I proceed, or run `scout:requirements` first?

**Branch B-2 — feasibility LOADED only (requirements and compliance absent)**

VERBATIM RESPONSE:
> I have a feasibility assessment for this topic but no requirements or compliance artifacts. I can write a spec informed by technical feasibility, but P0 coverage and compliance constraints will be waived — I'll state both waivers explicitly. Should I proceed, or run `scout:requirements` first?

**Branch B-3 — compliance LOADED only (requirements and feasibility absent)**

VERBATIM RESPONSE:
> I have a compliance scan for this topic but no requirements or feasibility artifacts. I can write a spec with compliance constraints, but P0 coverage will be waived and design decisions may be underspecified. Should I proceed, or run `scout:requirements` first?

**Branch B-4 — only market, stakeholders, positioning, or naming LOADED (requirements, feasibility, compliance all absent)**

VERBATIM RESPONSE:
> I have some context signals for this topic (market, stakeholders, positioning, or naming) but no requirements, feasibility, or compliance artifacts. These signals can inform the spec's purpose and constraints, but P0 coverage and risk assessment will be waived. Should I proceed with what I have, or run `scout:requirements` first?

HALT on any Branch B sub-condition until user confirms or provides requirements context. Do not blend sub-condition copy; emit the matching block verbatim.

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
| IG-01 | [describe existing alternative or status-quo] | [why it fails — name the specific gap] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present with all IG-ID rows fully populated.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact.
> Phase 1 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 0B =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [INERTIA-ANALYZED] (BLOCKS if absent)
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
> INVALID IF emitted without [PM-COVERAGE-TABLE] (P0 rows or waiver), [CNS-SLOT-1-OF-2] (Source artifact filled), and [CONTRADICTION-SCAN] (named outcome) all present.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list new constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] with specific artifact names in all `Source Artifact` cells.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL] (BLOCKS if either absent)
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
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
| Inertia context | [dominant IG-ID and why the spec wins — reference by number] |

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 rows TO CONFIRM P0 placement PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.

[Write design content here]

IG-ID mitigations: [for each REQUIRES SPEC MITIGATION row in [INERTIA-TABLE], name the design element]

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.

[List constraints with source artifact names]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

[List open questions — numbered, including one per REQUIRES SPEC MITIGATION IG-ID not resolved above]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF emitted without all five sections present in order.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

REQUIRES: [SPEC-DRAFT-COMPLETE]
PRODUCES: [FINDINGS-TABLE], [SELF-REVIEW-SEAL]

**Architect INSPECTS sections 1–5 REQUIRES [SPEC-DRAFT-COMPLETE] TO SURFACE contradictions, gaps, ambiguities, hotspots, and IG-ID mitigation gaps PRODUCES [FINDINGS-TABLE].**

> Scan must cover: IG-ID mitigation completeness. Note which Branch B sub-condition was triggered in Phase 0 and whether the relevant waivers appear in Requirements and Constraints.

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome]

> **[SELF-REVIEW-SEAL]**
> INVALID IF emitted without [FINDINGS-TABLE] or explicit finding claim referencing [SPEC-DRAFT-COMPLETE].

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
Gate tokens present: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Branch B sub-condition triggered: [B-1 / B-2 / B-3 / B-4 / N/A — Normal branch taken].
All sections populated. Frontmatter complete.

---

---

## V-03 — Phrasing Register: Concise Imperative

**Primary axis**: Phrasing register — all phase headers, gate token declarations, and unified role declarations rewritten in concise imperative voice ("PM: scan X, fill Y") while every structural element is preserved identically.
**Secondary axes**: C-25 two-branch verbatim fallback carried forward from V-01.
**Hypothesis**: The formal REQUIRES/PRODUCES/BLOCKS header syntax is cosmetic, not load-bearing. A concise imperative register ("Before writing sections: confirm [INERTIA-ANALYZED] is in the document. If not, stop.") satisfies every structural criterion equally well because the rubric checks for named tables, gate tokens, role-source declarations, and ordinal labels — not for any specific framing register. A successful score on V-03 at parity with V-01 supports deprioritizing REQUIRES/PRODUCES/BLOCKS boilerplate in future versions.

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

## INTAKE

**Step 1. Load scout context.**

Check `simulations/scout/` for these seven artifacts and record each as LOADED or NOT FOUND:

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

**Step 2. Dispatch.**

*Branch A — all seven NOT FOUND:*

VERBATIM RESPONSE:
> I don't have any prior scout signals for this topic. To write a useful spec I need a short description — 3 to 5 sentences covering: what the feature does, who uses it, and what problem it solves. Please share that and I'll proceed.

Stop here until the user responds.

*Branch B — requirements NOT FOUND but at least one other artifact is LOADED:*

VERBATIM RESPONSE:
> I have some scout signals for this topic (feasibility, compliance, or market), but I don't have a requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

Stop here until the user confirms or provides requirements context.

*Normal — requirements LOADED:* continue to INERTIA CHECK.

---

## INERTIA CHECK

Before writing any section, assess risk signals and enumerate inertia guards.

**PM: scan `scout-feasibility` and `scout-compliance` (if loaded) → record risk level → fill [IG-REGISTER] and [ID-REGISTER].**

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

### [IG-REGISTER] — Guards

Minimum 2 rows. Each row names what the model might default to, which scout artifact reveals the gap, the risk level, the responsible role, and where the mitigation goes.

| IG-ID | Default to Block | Artifact Trigger | Risk | Responsible Role | Mitigation Location |
|-------|-----------------|------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or existing alternative] | [scout artifact that reveals the gap] | STANDARD / AMPLIFIED | [PM / Strategy / Compliance / Design / Architect] | Design / Constraints / Open Questions |
| IG-02 | [lazy default] | [artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | | | | |

> Responsible Role blank = structural fail for this row.
> AMPLIFIED rows: Artifact Trigger must address the risk dimension specifically.

### [ID-REGISTER] — Defeats

One row per IG row. Each row names the condition confirming the guard succeeded, evidence proving it, and the confirming role (must match the paired IG-XX Responsible Role).

| ID-ID | Paired IG | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|----------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition] | [named evidence] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> Row count: [ID-REGISTER] must equal [IG-REGISTER]. Mismatched counts = structural fail.

> **[INERTIA-ANALYZED]**
> INVALID if: either register is missing; any IG-XX Responsible Role cell is blank; any ID-XX Confirming Role does not match its paired IG-XX; row counts differ; any AMPLIFIED row's Artifact Trigger is generic rather than risk-specific.
> This gate must appear in this block before the PM PRE-ASSIGNMENT step begins.

---

## PM PRE-ASSIGNMENT

**Before writing the five sections, PM assigns each P0 requirement to a section and names the spec entry.**

Confirm [INERTIA-ANALYZED] is in the document above. If not, stop and state "[INERTIA-ANALYZED] missing."

**PM: scan `{topic}-requirements-{date}.md` → fill [PM-COVERAGE-TABLE].**

### [PM-COVERAGE-TABLE]

If requirements LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| ... | | | | |

P0 coverage: {n}/{n}. If requirements NOT FOUND: C-03 waiver stated here.

---

**PM: inspect `scout-feasibility` and `scout-compliance` → name the cross-namespace signal → fill [CNS-SLOT-1-OF-2].**

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or decision] |

> Source artifact blank = C-11 fires at location 1 of 2.

---

**PM: scan all rows in `{topic}-requirements-{date}.md` → name contradiction pairs → fill [CONTRADICTION-SCAN].**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
> INVALID if any of these are absent from this block: [PM-COVERAGE-TABLE] with P0 rows or waiver; [CNS-SLOT-1-OF-2] with Source artifact filled; [CONTRADICTION-SCAN] with named outcome.
> The five guided sections may not begin until [PM-CONTRACT-SEAL] appears here.

---

## STRATEGY VALIDATION

**Strategy: inspect `scout-feasibility` and `scout-compliance` → validate spec viability → fill [STRATEGY-VALIDATION-TABLE].**

Confirm [PM-CONTRACT-SEAL] is in the document. If not, stop.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list] | — |

> **[STRATEGY-SEAL]**
> INVALID if [STRATEGY-VALIDATION-TABLE] is absent or any Source Artifact cell is blank.
> Phase 3 (guided sections) may not begin until [STRATEGY-SEAL] appears here.

---

## GUIDED SECTIONS

Confirm [PM-CONTRACT-SEAL] and [STRATEGY-SEAL] are both in the document. If either is missing, stop.

Fill in the five sections in this order. Architect uses [PM-COVERAGE-TABLE] pre-assigned rows — do not re-enumerate. Architect uses [IG-REGISTER] and [ID-REGISTER] for mitigations — do not re-enumerate.

#### 1. Purpose

**PM: verify [CNS-SLOT-1-OF-2] → place cross-namespace signal at location 2 of 2 → produce [CNS-SLOT-2-OF-2].**

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-XX guard, paired ID-XX defeat condition, Responsible Role — reference by number] |

> [CNS-SLOT-2-OF-2] blank = C-11 fires. Inertia context blank = IG/ID registers disconnected from spec body.

#### 2. Requirements

**PM: confirm all P0 rows from [PM-COVERAGE-TABLE] are placed → produce per-row coverage table below.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture, components, and key decisions. For each IG-XX with Mitigation Location = Design, name the design element activating its paired ID-XX defeat and the Responsible Role confirming it.

**Strategy: validate design against [STRATEGY-VALIDATION-TABLE] → record verdict inline.**

[Write design content here]

IG/ID mitigation coverage (Design section):
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element |
|-------|-------|-------|-----------------|-----------------|---------------------|
| IG-01 | ID-01 | [guard] | [role] | [defeat condition] | [design element or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [guard] | [role] | [defeat condition] | [design element or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-XX with Mitigation Location = Constraints, name the constraint and the Responsible Role confirming it.

**Compliance: validate constraint completeness against scout-compliance-{date}.md → record verdict inline.**

[List constraints]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. At least one per FINDING from inertia/strategy/compliance phases. At least one per IG-XX with Mitigation Location = Open Questions not resolved above. Name the Responsible Role for each IG-derived question.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID if all five sections are not present in this order: Purpose → Requirements → Design → Constraints → Open Questions.

---

## SELF-REVIEW

Confirm [SPEC-DRAFT-COMPLETE] is in the document.

**Architect: scan sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, and role-binding gaps → fill [FINDINGS-TABLE].**

Scan checklist:
- Every IG-XX with a Mitigation Location has a named element in the correct section
- Every ID-XX Confirming Role matches its paired IG-XX Responsible Role
- [CNS-SLOT-2-OF-2] is filled (location 2 of 2)

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — must reference sections scanned]

> **[SELF-REVIEW-SEAL]**
> INVALID if [FINDINGS-TABLE] is absent or finding claim does not reference [SPEC-DRAFT-COMPLETE] as the scan source.

---

## AMEND

Confirm [SELF-REVIEW-SEAL] is in the document.

Produce at least 2 specific, actionable amendments. Each must name a section, a finding ID, and the exact change.

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback: Branch A or Branch B verbatim block present (or Normal branch — state which).
IG/ID registers: row counts match, all Responsible Role and Confirming Role columns filled.
All sections populated. Frontmatter complete.

---

---

## V-04 — C-25 + C-22: Two-Branch Fallback + Parallel IG/ID Registers

**Primary axis**: C-25 (two-branch verbatim fallback) + C-22 (parallel IG-XX and ID-XX registers as distinct tables).
**Secondary axes**: C-23 excluded (no Responsible Role column), C-24 excluded (no CASCADE TO: annotations).
**Hypothesis**: Combining the Phase 0 two-branch structure (C-25) with the Phase 0B parallel namespace (C-22) tests whether these two axes interact cleanly. The context-branching at intake and the register-splitting in inertia analysis address different structural layers — intake dispatch vs. risk tracking — and should not interfere. Expected: C-22 + C-25 both pass; C-23 ✗ (no role column); C-24 ✗ (no cascade annotations).

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

> Unified declaration: role PM, sources named, action named, outputs named.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Guards

Enumerate guards against lazy model defaults. Minimum 2 IG entries. Each guard declares what the spec must NOT allow the model to default to.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Mitigation Location |
|-------|------------------------|----------------------|-------------|---------------------|
| IG-01 | [describe the status-quo default or existing alternative the model might accept without scrutiny] | [name the scout artifact that would reveal this default is insufficient] | STANDARD / AMPLIFIED [cite trigger: "feasibility < 70" or "compliance = blocking"] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [location] |
| IG-03 | [add if applicable] | | | |

> When Risk Signal = AMPLIFIED, the Named Artifact Trigger must address the risk dimension. A generic functional trigger does not satisfy.

### [ID-REGISTER] — Inertia Defeats

One ID entry per IG entry. Each defeat entry names the condition confirming the corresponding guard has successfully blocked the default. IG-XX and ID-XX IDs pair one-to-one.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence |
|-------|--------|-----------------|----------------------|
| ID-01 | IG-01 | [condition under which the guard is confirmed to have defeated the default — name the specific spec decision, constraint, or design element that activates the defeat] | [named evidence: scan result reference, spec entry name, coverage count, or named constraint] |
| ID-02 | IG-02 | [condition] | [evidence] |
| ID-03 | IG-03 (if present) | | |

> ID-REGISTER must have exactly as many rows as [IG-REGISTER]. Defeat Condition blank = guard has no verifiable exit condition — not allowed.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER] present in this phase block with:
> - All IG-XX rows fully populated (Guard, Named Artifact Trigger, Risk Signal, Mitigation Location)
> - All ID-XX rows present with Defeat Condition and Confirmation Evidence filled
> - ID-XX row count = IG-XX row count
> - Every AMPLIFIED IG-XX row addressing the named threshold dimension in its Named Artifact Trigger
> - Every IG-XX with Mitigation Location = Design/Constraints/Open Questions producing a named entry in that section
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies [IG-REGISTER] and [ID-REGISTER] are present, pair-balanced, and non-empty in this block.
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
> INVALID IF emitted without [STRATEGY-VALIDATION-TABLE] with specific artifact names in all `Source Artifact` cells.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

REQUIRES: [PM-CONTRACT-SEAL], [STRATEGY-SEAL] (BLOCKS if either absent)
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
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
| Inertia context | [1-sentence summary: dominant IG-XX guard and its paired ID-XX defeat condition — reference IG-XX and ID-XX by number] |

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

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions PRODUCES inline verdict below.**

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
> Scan must cover: IG/ID pair balance ([IG-REGISTER] row count = [ID-REGISTER] row count); any IG-XX with Mitigation Location filled but lacking a named design element, constraint, or open question; [CNS-SLOT-2-OF-2] filled at location 2 of 2.

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

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]
...

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens present: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
IG/ID registers: [IG-REGISTER] row count = [ID-REGISTER] row count. Parallel namespaces confirmed.
Fallback branches: Branch A and Branch B verbatim response blocks present in Phase 0.
All sections populated. Frontmatter complete.

---

---

## V-05 — Full Combination: C-22 + C-23 + C-24 + C-25 (Target 175/175)

**Axes**: All four — parallel IG/ID namespace (C-22), per-IG responsible role binding (C-23), cascade directives on unified declarations (C-24), two-branch demarcated verbatim fallback (C-25).
**Hypothesis**: R6 V-05 already contained all four axes because it combined C-22+C-23+C-24 from V-01/V-04/V-03 with C-18's two-branch verbatim fallback (which implicitly satisfied C-25 before C-25 was in the rubric). This V-05 makes C-25 explicit — named branch headers, distinct VERBATIM RESPONSE: blocks per branch, branch conditions structurally distinct — and confirms 175/175 under v7 criteria. No new structural elements beyond R6 V-05; the C-25 satisfaction is structural, not incidental.

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
> CASCADE TO: [location 1 of 1: this phase, [IG-REGISTER] and [ID-REGISTER]] — single instantiation; guard/defeat outputs carry their own structural propagation via Mitigation Location column.

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
> CASCADE TO: [location 2 of 2: this section, [CNS-SLOT-2-OF-2]] — completing the cascade declared in Phase 1. Two-location coverage is structurally declared and verifiable by counting labeled instances.

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
> - Fallback branch coverage: Branch A and Branch B verbatim blocks present in Phase 0 with named branch conditions

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

INVALID IF fewer than 2 items or any item is vague (must name section + finding ID + specific change).

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]
...

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens present: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
IG/ID registers: [IG-REGISTER] row count = [ID-REGISTER] row count. All Responsible Role and Confirming Role columns filled and cross-matched.
Cascade completeness: CNS-SLOT 1 of 2 and 2 of 2 filled. Strategy 1 of 2 and 2 of 2 filled. All CASCADE TO: denominators verified.
Fallback branches: Branch A (ALL NOT FOUND) and Branch B (requirements absent, others loaded) — each with its own named VERBATIM RESPONSE: block. Branch conditions structurally distinct.
All sections populated. Frontmatter complete.
