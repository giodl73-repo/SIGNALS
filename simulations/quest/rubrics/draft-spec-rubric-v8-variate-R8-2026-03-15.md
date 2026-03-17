---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v8
round: R8
date: 2026-03-15
axes_explored: C-26-branch-B-sub-conditionals, C-27-imperative-phrasing, role-sequence-PM-first, C-26-plus-C-27, full-combination-v8
---

# Quest Variate — `draft-spec` — Round 8 (Rubric v8)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-26: per-artifact Branch B sub-conditionals (4 named blocks + anti-blend) on v7 V-01 minimal base (merged INERTIA-TABLE, no C-22/C-23/C-24) | — | C-26 can pass independently of C-22/C-23/C-24; the 4 per-artifact sub-conditions each with their own VERBATIM RESPONSE block and an explicit anti-blend instruction satisfy C-26 on any base that includes C-25 |
| V-02 | C-27: imperative phrasing register (actor-action-output directives throughout) on v7 V-03 minimal base (no C-22/C-23/C-24; Branch B single, not subdivided) | — | C-27 passes on a minimal base that has the split-register structure from v7 V-03 but does NOT include C-26; the actor-action-output directive form is independent of whether Branch B is subdivided; 2+ explicit directives are present throughout the template |
| V-03 | Role sequence: PM pre-assignment runs before inertia analysis (Phase 1 precedes Phase 0B) on v7 V-05 full-combination base (all C-22/C-23/C-24/C-25 present) | — | Moving PM pre-assignment ahead of inertia analysis allows IG-REGISTER guards to reference specific pre-assigned requirement IDs by name, strengthening the Elimination Path specificity requirement and the AMPLIFIED threshold links; no existing v7 criteria are broken by the reorder |
| V-04 | C-26 + C-27 combined on v7 V-05 full-combination base (all C-22/C-23/C-24/C-25 present) | — | C-26 and C-27 are non-interacting axes: Branch B sub-conditions add structural copy to Phase 0 while imperative directives change phrasing register throughout all phases; combining both on the v7 V-05 base should satisfy all 27 v8 criteria with no axis conflict |
| V-05 | C-26 + C-27 + role-sequence combined — target 175/175 under v8 | — | All three axes (Branch B sub-conditionals, imperative phrasing, PM-first phase ordering) compose without conflict; PM-first ordering enables inertia guards to reference pre-assigned requirement IDs in their Elimination Path, C-26 discriminates among fallback sub-scenarios, and C-27 phrasing applies uniformly to all actor-phase instructions; target: 175/175 composite |

---

## V-01 — Axis: C-26 Branch B Sub-Conditionals (Minimal Base)

**Primary axis**: C-26 — Branch B expanded into 4 per-artifact sub-conditions (B-1 through B-4), each with its own `VERBATIM RESPONSE:` block, plus an explicit anti-blend instruction. A catch-all sub-condition (B-4) handles unlisted combinations.
**Secondary axes**: none — uses v7 V-01 base (merged [INERTIA-TABLE], no C-22/C-23/C-24; REQUIRES/PRODUCES/BLOCKS phrasing preserved).
**Hypothesis**: C-26 can pass on a minimal base without requiring split inertia registers or imperative phrasing. The structural discriminator (which artifacts are LOADED) is independent of the inertia register architecture. C-25 passes by inclusion (Branch A and Branch B are both named with VERBATIM blocks). The four sub-conditions are scenario-appropriate — each VERBATIM block names the specific signal present.

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
skill_version: v8
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

Inspect [SCOUT-STATUS-TABLE] to identify which non-requirements artifacts are LOADED. Match exactly one sub-condition below. Do not blend sub-condition copy; emit the matching block verbatim. If multiple sub-conditions could apply simultaneously (e.g., both B-1 and B-2 conditions are met), apply B-3. If none of B-1 through B-3 apply, apply B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND, market / stakeholders / positioning / naming any combination:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — the Design section will be driven by feasibility constraints and I'll call out the specific scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND, market / stakeholders / positioning / naming any combination:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec that treats compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and I'll flag each compliance-driven decision explicitly. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on which decisions would shift if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements NOT FOUND, feasibility NOT FOUND, compliance NOT FOUND, but at least one of market / stakeholders / positioning / naming LOADED:**

VERBATIM RESPONSE:
> I have some positioning or market signals for this topic but no requirements artifact and no feasibility or compliance data. I can draft a spec from the available context, but coverage will be limited and constraint grounding will rely on the positioning signals. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

HALT after emitting the matching sub-condition block. Do not blend sub-condition copy; emit the matching block verbatim.

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
| IG-01 | [describe existing alternative or status-quo the model might default to] | [why it fails to satisfy the spec need — name the specific gap; if AMPLIFIED, address the risk dimension] | STANDARD / AMPLIFIED [cite trigger] | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-02 | [describe] | [why it fails] | STANDARD / AMPLIFIED | YES / NO | ELIMINATED / REQUIRES SPEC MITIGATION |
| IG-03 | [add if applicable] | | | | |

> When Risk Signal = AMPLIFIED, the Elimination Path must explicitly address the risk dimension. A generic functional elimination does not satisfy.
> When Verdict = REQUIRES SPEC MITIGATION, the IG-ID must produce a named constraint or open question in Phase 3.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated (IG-ID, Inertia Hypothesis, Elimination Path, Risk Signal, Verdict cells filled).
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
| Spec impact | [1-sentence constraint or design decision] |

> If `Source artifact` is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY R-ID contradiction pairs PRODUCES [CONTRADICTION-SCAN].**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" after scanning all rows, or "none found after scanning R-01 through R-{n}"]

> Do not confirm "none found" without reviewing the requirements artifact. State which rows were inspected.

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF emitted without ALL of the following present in this phase block:
> - [PM-COVERAGE-TABLE]: P0 rows populated (or C-03 waiver)
> - [CNS-SLOT-1-OF-2]: `Source artifact` cell filled
> - [CONTRADICTION-SCAN]: named scan outcome stating rows inspected
>
> Proof-of-work: presence of [PM-CONTRACT-SEAL] certifies all three outputs present and non-empty in this block.
> Phase 3 is blocked until [PM-CONTRACT-SEAL] appears here.

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
| Inertia context | [1-sentence: dominant IG-ID guard and why the spec wins — reference IG-ID by number] |

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

Describe architecture, components, and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION, name the design element that addresses it.

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

List constraints with source artifact names. For each IG-ID with Verdict = REQUIRES SPEC MITIGATION and Mitigation Location = Constraints, name the constraint.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.

[List constraints with source artifact names]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. Include at least one per open FINDING from Phases 0B–2, and one per IG-ID with Verdict = REQUIRES SPEC MITIGATION not resolved in Design or Constraints.

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
> Scan must cover: IG-ID mitigation completeness; [CNS-SLOT-2-OF-2] filled; Branch A and Branch B sub-conditions present in Phase 0.

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

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Fallback: Branch A (ALL NOT FOUND) with VERBATIM block; Branch B (requirements absent, others loaded) with sub-conditions B-1 through B-4 each with own VERBATIM block; Normal branch. State which applied.
All five sections in order. Frontmatter complete. [CNS-SLOT-1-OF-2] and [CNS-SLOT-2-OF-2] both filled (location 1 of 2 and location 2 of 2).

---

---

## V-02 — Axis: C-27 Imperative Phrasing Register (Minimal Base)

**Primary axis**: C-27 — every role-phase instruction written as a concise actor-action-output directive ("**PM: scan X → fill Y**", "Confirm [token] is present before proceeding"). REQUIRES/PRODUCES/BLOCKS header syntax absent throughout. At least two explicit directives in actor-action-output form are verifiable in the template.
**Secondary axes**: none — uses v7 V-03 INTAKE-based structure with split [IG-REGISTER]/[ID-REGISTER] (C-22 present); Branch B is a single condition (C-25 present, C-26 absent). No cascade TO annotations (C-24 absent).
**Hypothesis**: C-27 passes on a base that does not include C-26 sub-conditions. The imperative form is syntactically independent — the VERBATIM RESPONSE blocks in Branch B do not need to be subdivided for the actor-action-output directives throughout the phases to be scoreable. The test: C-27 is satisfied when C-26 is absent.

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
skill_version: v8
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

Stop here until the user responds. Do not compose an alternative response; emit the text above verbatim.

*Branch B — requirements NOT FOUND but at least one other artifact is LOADED:*

VERBATIM RESPONSE:
> I have some scout signals for this topic (feasibility, compliance, or market), but I don't have a requirements artifact. I can still write a spec using the signals I have, but I won't be able to do P0 requirement coverage — I'll note the waiver explicitly. Should I proceed, or do you want to run `scout:requirements` first?

Stop here until the user confirms or provides requirements context.

*Normal — requirements LOADED:* continue to INERTIA CHECK.

---

## INERTIA CHECK

**PM: scan `scout-feasibility` and `scout-compliance` (if loaded) → record risk level → fill [IG-REGISTER] and [ID-REGISTER].**

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

### [IG-REGISTER] — Guards

Minimum 2 rows. Each row names the lazy default to block, the scout artifact that reveals the gap, the risk level, the responsible role, and the mitigation location.

| IG-ID | Default to Block | Artifact Trigger | Risk | Responsible Role | Mitigation Location |
|-------|-----------------|------------------|------|-----------------|---------------------|
| IG-01 | [lazy default or existing alternative] | [scout artifact that reveals the gap] | STANDARD / AMPLIFIED | [PM / Strategy / Compliance / Design / Architect] | Design / Constraints / Open Questions |
| IG-02 | [lazy default] | [artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if needed] | | | | |

> Responsible Role blank = structural fail for this row.
> AMPLIFIED rows: Artifact Trigger must address the risk dimension specifically.

### [ID-REGISTER] — Defeats

One row per IG row. Each row names the defeat condition, the confirmation evidence, and the confirming role (must match paired IG-XX Responsible Role).

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition] | [named evidence] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Mismatched counts = structural fail.

> **[INERTIA-ANALYZED]**
> INVALID if: either register is missing; any IG-XX Responsible Role cell is blank; any ID-XX Confirming Role does not match its paired IG-XX; row counts differ; any AMPLIFIED row's Artifact Trigger is generic rather than risk-specific.
> Confirm this gate is written to the document before beginning PM PRE-ASSIGNMENT.

---

## PM PRE-ASSIGNMENT

**Before writing any section, PM assigns each P0 requirement to a section and names the spec entry.**

Confirm [INERTIA-ANALYZED] is in the document above. If not, stop and state "[INERTIA-ANALYZED] missing."

**PM: scan `{topic}-requirements-{date}.md` → enumerate P0 requirements → fill [PM-COVERAGE-TABLE].**

### [PM-COVERAGE-TABLE]

If requirements LOADED:

| Req ID | Priority | Requirement Text | Assigned Section | Spec Entry Name |
|--------|----------|-----------------|------------------|-----------------|
| R-01 | P0 | [from artifact] | [Purpose / Requirements / Design / Constraints] | [name the entry] |
| ... | | | | |

P0 coverage: {n}/{n}. If requirements NOT FOUND: C-03 waiver stated here.

---

**PM: scan `scout-feasibility` and `scout-compliance` → identify strongest non-requirements signal → fill [CNS-SLOT-1-OF-2].**

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> Source artifact blank = C-11 fires at location 1 of 2.

---

**PM: scan all rows in `{topic}-requirements-{date}.md` → name contradiction pairs as "R-XX vs R-YY" → fill [CONTRADICTION-SCAN].**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" after scanning, or "none found after scanning R-01 through R-{n}"]

> Do not state "none found" without completing the scan. Name the row range inspected.

---

> **[PM-CONTRACT-SEAL]**
> INVALID if any of these are absent from this block: [PM-COVERAGE-TABLE] with P0 rows or waiver; [CNS-SLOT-1-OF-2] with Source artifact filled; [CONTRADICTION-SCAN] with named outcome.
> The five guided sections may not begin until [PM-CONTRACT-SEAL] appears here.

---

## STRATEGY VALIDATION

**Strategy: scan `scout-feasibility` and `scout-compliance` → validate spec viability → fill [STRATEGY-VALIDATION-TABLE].**

Confirm [PM-CONTRACT-SEAL] is in the document. If not, stop.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list] | — |

> **[STRATEGY-SEAL]**
> INVALID if [STRATEGY-VALIDATION-TABLE] is absent or any Source Artifact cell is blank.
> Guided sections may not begin until [STRATEGY-SEAL] appears here.

---

## GUIDED SECTIONS

Confirm [PM-CONTRACT-SEAL] and [STRATEGY-SEAL] are both present in the document. If either is missing, stop.

**Architect: use [PM-COVERAGE-TABLE] pre-assigned rows as the contract → fill each Spec Entry cell. Do not re-enumerate. Use [IG-REGISTER]/[ID-REGISTER] for mitigation placement — do not re-enumerate.**

#### 1. Purpose

**PM: verify [CNS-SLOT-1-OF-2] → place cross-namespace signal at location 2 of 2 → write [CNS-SLOT-2-OF-2] in the table below.**

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-XX guard, Responsible Role from [IG-REGISTER], paired ID-XX defeat condition — reference by number] |

> [CNS-SLOT-2-OF-2] blank = C-11 fires. [CNS-SLOT-1-OF-2] (INTAKE) and [CNS-SLOT-2-OF-2] (here) are location 1 of 2 and location 2 of 2.

#### 2. Requirements

**PM: confirm all P0 rows from [PM-COVERAGE-TABLE] are placed → fill per-row coverage table below.**

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture and key technical decisions. For each IG-XX with Mitigation Location = Design, name the design element activating its paired ID-XX defeat. Include the Responsible Role from [IG-REGISTER] as the confirmation accountable party.

**Strategy: validate design against [STRATEGY-VALIDATION-TABLE] → record verdict inline.**

[Write design content here]

IG/ID mitigation coverage (Design):
| IG-ID | ID-ID | Responsible Role | Defeat Condition | Mitigation Element |
|-------|-------|-----------------|-----------------|---------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |

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

**Architect: scan sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, and role-binding gaps → fill [FINDINGS-TABLE].**

Confirm [SPEC-DRAFT-COMPLETE] is present. Scan checklist:
- Every IG-XX with a Mitigation Location has a named element in the correct section
- Every ID-XX Confirming Role matches its paired IG-XX Responsible Role
- [CNS-SLOT-2-OF-2] is filled (location 2 of 2)
- Branch A and Branch B VERBATIM blocks are present in INTAKE

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — must reference sections scanned and [SPEC-DRAFT-COMPLETE] as source]

> **[SELF-REVIEW-SEAL]**
> INVALID if [FINDINGS-TABLE] is absent or finding claim does not reference [SPEC-DRAFT-COMPLETE] as the scan source.

---

## AMEND

Confirm [SELF-REVIEW-SEAL] is present.

**Architect: produce at least 2 specific, actionable amendments → each must name a section, a finding ID, and the exact change.**

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
Registers: [IG-REGISTER] row count = [ID-REGISTER] row count. All Responsible Role and Confirming Role columns filled and cross-matched.
CNS-SLOT: location 1 of 2 (INTAKE) and location 2 of 2 (Purpose) both filled.
Fallback: Branch A (ALL NOT FOUND) and Branch B (requirements absent, others loaded) — each with its own VERBATIM RESPONSE block. Branch B is a single condition (not subdivided).
All sections populated. Frontmatter complete.

---

---

## V-03 — Axis: Role Sequence: PM Pre-Assignment Before Inertia Analysis

**Primary axis**: Role sequence — Phase 1 (PM pre-assignment) runs immediately after Phase 0 (setup), before Phase 0B (inertia analysis). PM assigns every P0 requirement to a named spec section first; inertia analysis can then reference specific pre-assigned requirement IDs in Elimination Path entries, making IG guards more precise.
**Secondary axes**: v7 V-05 full-combination base (C-22/C-23/C-24/C-25 all present; REQUIRES/PRODUCES/BLOCKS phrasing preserved; Branch A and Branch B each with VERBATIM block; C-26 absent, C-27 absent).
**Hypothesis**: Reordering Phase 1 before Phase 0B strengthens the Elimination Path column in [IG-REGISTER]: guards can name specific pre-assigned requirement IDs that the inertia hypothesis would violate. This also allows the [PM-CONTRACT-SEAL] gate to serve as the REQUIRES prerequisite for [INERTIA-ANALYZED] rather than the other way around. No v7 criteria break; PM-first ordering is a structural reinforcement, not a disruption.

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
skill_version: v8
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

Proceed to Phase 1 (PM pre-assignment). **Note: Phase 1 runs before Phase 0B in this variation. Inertia guards are authored after requirement IDs are known.**

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

REQUIRES: [SCOUT-STATUS-TABLE]
PRODUCES: [PM-COVERAGE-TABLE], [CNS-SLOT-1-OF-2], [CONTRADICTION-SCAN], [PM-CONTRACT-SEAL]
EXIT CONDITION: [PM-CONTRACT-SEAL] present
BLOCKS: Phase 0B REQUIRES [PM-CONTRACT-SEAL]

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO ENUMERATE all P0 requirements PRODUCES [PM-COVERAGE-TABLE].**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [PM-COVERAGE-TABLE]] — Architect receives [PM-COVERAGE-TABLE] as a pre-filled contract. Phase 0B receives [PM-COVERAGE-TABLE] to anchor inertia guard Elimination Path entries to named requirement IDs.

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
> The cross-namespace signal field instantiates in exactly 2 structurally independent locations.

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> If `Source artifact` is unfilled, C-11 fires at location 1 of 2.

---

**PM INSPECTS `scout-requirements` REQUIRES `{topic}-requirements-{date}.md` TO IDENTIFY R-ID contradiction pairs PRODUCES [CONTRADICTION-SCAN].**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [CONTRADICTION-SCAN]]

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

## ===== PHASE 0B: INERTIA ANALYSIS =====

REQUIRES: [PM-CONTRACT-SEAL] (BLOCKS if absent — halt and state "[PM-CONTRACT-SEAL] missing")
PRODUCES: [IG-REGISTER], [ID-REGISTER], [INERTIA-ANALYZED]
EXIT CONDITION: [INERTIA-ANALYZED] present
BLOCKS: Phase 2 REQUIRES [INERTIA-ANALYZED]

> **Note**: Phase 0B runs after Phase 1 in this variation. [PM-COVERAGE-TABLE] is available. Inertia guard Elimination Path entries should reference specific pre-assigned requirement IDs by name (e.g., "violates R-03 as pre-assigned to Design:retry-backoff") when applicable.

**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each inertia guard and defeat PRODUCES [IG-REGISTER] and [ID-REGISTER].**

> Unified declaration: role PM, sources named, action named, outputs named.
> CASCADE TO: guard/defeat outputs carry structural propagation via Mitigation Location column.

### Risk Signal Source

- Feasibility score (from `scout-feasibility` if LOADED): [record numeric score, or "NOT LOADED — threshold check skipped"]
- Compliance status (from `scout-compliance` if LOADED): ["blocking" / "non-blocking" / "NOT LOADED — threshold check skipped"]

Risk amplification threshold: **AMPLIFIED** if feasibility-score < 70 OR compliance-status = blocking.

### [IG-REGISTER] — Inertia Guards

Minimum 2 IG entries. Where [PM-COVERAGE-TABLE] is populated, Elimination Path should reference the specific pre-assigned requirement ID the guard would violate.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Responsible Role | Mitigation Location |
|-------|------------------------|----------------------|-------------|-----------------|---------------------|
| IG-01 | [describe the status-quo default or existing alternative] | [name the scout artifact revealing this default is insufficient] | STANDARD / AMPLIFIED [cite trigger] | [PM / Strategy / Compliance / Design / Architect] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if applicable] | | | | |

> Responsible Role blank = C-23 structural fail for this row.
> AMPLIFIED rows: Named Artifact Trigger must address the risk dimension. Generic triggers do not satisfy.
> Where [PM-COVERAGE-TABLE] is populated: Elimination Path should reference pre-assigned requirement IDs by name when the guard would contradict a specific pre-assigned entry.

### [ID-REGISTER] — Inertia Defeats

One ID entry per IG entry.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition confirming the guard succeeded] | [named evidence: spec entry, constraint ID, coverage count] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Confirming Role must match Responsible Role in paired IG-XX.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER] present in this phase block with:
> - All IG-XX rows fully populated including Responsible Role (not blank)
> - All ID-XX rows present with Defeat Condition, Confirmation Evidence, and Confirming Role filled
> - ID-XX row count = IG-XX row count
> - Confirming Role in each ID-XX matches Responsible Role in paired IG-XX
> - Every AMPLIFIED IG-XX addressing the named threshold dimension in its Named Artifact Trigger
>
> [INERTIA-ANALYZED] is a proof-of-work artifact.
> Phase 2 is blocked until [INERTIA-ANALYZED] appears in this document.

===== END PHASE 0B =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

REQUIRES: [INERTIA-ANALYZED] (BLOCKS if absent)
PRODUCES: [STRATEGY-VALIDATION-TABLE], [STRATEGY-SEAL]
EXIT CONDITION: [STRATEGY-SEAL] present
BLOCKS: Phase 3 REQUIRES [STRATEGY-SEAL]

**Strategy INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts TO VALIDATE spec viability PRODUCES [STRATEGY-VALIDATION-TABLE].**

> Unified declaration: role Strategy, sources named, action named, output named.
> CASCADE TO: [location 1 of 2: this phase, [STRATEGY-VALIDATION-TABLE]] → [location 2 of 2: Phase 3 Design, inline Strategy verdict]

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

REQUIRES: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [STRATEGY-SEAL] (BLOCKS if any absent)
PRODUCES: five guided sections + [SPEC-DRAFT-COMPLETE]
EXIT CONDITION: all five sections in order + [SPEC-DRAFT-COMPLETE] emitted
SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

**Architect RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows. Architect RECEIVES [IG-REGISTER] and [ID-REGISTER] and incorporates mitigations, confirmations, and role bindings. Do not re-enumerate either.**

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
| Inertia context | [1-sentence: dominant IG-XX guard, Responsible Role from [IG-REGISTER], paired ID-XX defeat condition — reference by number] |

> If [CNS-SLOT-2-OF-2] is blank, C-11 fires from this location. Inertia context blank means [IG-REGISTER]/[ID-REGISTER] role bindings are disconnected from spec body.

#### 2. Requirements

**PM INSPECTS [PM-COVERAGE-TABLE] REQUIRES Phase 1 pre-assignment rows TO CONFIRM all P0 entries are placed PRODUCES per-row coverage table below.**

> Unified declaration inline within Requirements content block.
> CASCADE TO: [location 1 of 1: this section, per-row coverage table]

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions (location 2 of 2 of Strategy cascade). For each IG-XX with Mitigation Location = Design, name the design element activating its paired ID-XX defeat. Include Responsible Role as confirmation accountable party.

**Strategy INSPECTS this section REQUIRES [STRATEGY-VALIDATION-TABLE] TO VALIDATE design decisions PRODUCES inline verdict below.**

> Unified declaration inline within Design content block.
> CASCADE TO: [location 2 of 2: this section, inline Strategy verdict] — completing Strategy cascade from Phase 2.

[Write design content here]

IG/ID mitigation coverage (Design):
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element |
|-------|-------|-------|-----------------|-----------------|---------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-XX with Mitigation Location = Constraints, name the constraint and the Responsible Role confirming it.

**Compliance INSPECTS this section REQUIRES scout-compliance-{date}.md TO VALIDATE constraint completeness PRODUCES inline verdict below.**

> Unified declaration inline within Constraints content block.
> CASCADE TO: [location 1 of 1: this section, inline Compliance verdict]

[List constraints with source artifact names]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. At least one per open FINDING from Phases 0B–2. At least one per IG-XX with Mitigation Location = Open Questions not resolved. Name Responsible Role for each IG-derived question.

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
> CASCADE TO: [location 1 of 1: this phase, [FINDINGS-TABLE]]
> Scan checklist:
> - IG/ID pair balance: [IG-REGISTER] row count = [ID-REGISTER] row count
> - Role binding: every IG-XX Responsible Role filled; every ID-XX Confirming Role matches its paired IG-XX
> - Cascade completeness: CNS-SLOT 1 of 2 (Phase 1) and 2 of 2 (Purpose) both filled; Strategy 1 of 2 (Phase 2) and 2 of 2 (Design inline) both filled
> - Mitigation coverage: every IG-XX with Mitigation Location has a named element in the correct section
> - Fallback branches: Branch A and Branch B VERBATIM blocks present in Phase 0

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

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens: [PM-CONTRACT-SEAL] (Phase 1, runs before Phase 0B), [INERTIA-ANALYZED] (Phase 0B), [STRATEGY-SEAL] (Phase 2), [SPEC-DRAFT-COMPLETE] (Phase 3), [SELF-REVIEW-SEAL] (Phase 4).
Phase execution order: Phase 0 → Phase 1 → Phase 0B → Phase 2 → Phase 3 → Phase 4 → Phase 5.
[IG-REGISTER]/[ID-REGISTER]: row counts match; Responsible Role and Confirming Role filled and cross-matched; where [PM-COVERAGE-TABLE] is populated, Elimination Path entries reference pre-assigned requirement IDs.
Cascade completeness: CNS-SLOT 1 of 2 and 2 of 2; Strategy 1 of 2 and 2 of 2.
Fallback branches: Branch A and Branch B VERBATIM blocks in Phase 0.
All five sections in order. Frontmatter complete.

---

---

## V-04 — Combined: C-26 + C-27

**Primary axes**: C-26 (Branch B per-artifact sub-conditionals with anti-blend) + C-27 (imperative phrasing register throughout all role-phase instructions). Combines the two new v8 signal axes on the v7 V-05 full-combination base (C-22/C-23/C-24/C-25 all present; standard Phase 0 → 0B → 1 → 2 → 3 ordering).
**Secondary axes**: C-22/C-23/C-24/C-25 from v7 V-05 base, preserved without modification.
**Hypothesis**: C-26 and C-27 are non-interacting. C-26 adds structural copy in Phase 0 (the Branch B sub-conditionals); C-27 changes the phrasing register in all other phases. Combining both on the v7 V-05 base should satisfy all 27 v8 criteria: the 25 from v7 V-05 plus C-26 and C-27.

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
skill_version: v8
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP =====

Check `simulations/scout/` for these seven artifacts. Record each as LOADED or NOT FOUND.

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

Halt here. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**Inspect [SCOUT-STATUS-TABLE] → identify which non-requirements artifacts are LOADED → match exactly one sub-condition → emit the matching VERBATIM RESPONSE block.**

Do not blend sub-condition copy; emit the matching block verbatim. Priority for overlapping matches: B-3 > B-2 > B-1 > B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND, all others any combination:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — Design will be driven by feasibility constraints and I'll call out the scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND, all others any combination:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec treating compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and each compliance-driven decision will be flagged. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on decisions that would change if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements NOT FOUND, feasibility NOT FOUND, compliance NOT FOUND, at least one of market / stakeholders / positioning / naming LOADED:**

VERBATIM RESPONSE:
> I have positioning or market signals for this topic but no requirements and no feasibility or compliance data. I can draft a spec from the available context — P0 coverage will be waived and constraint grounding will draw on the positioning signals. Should I proceed, or would you prefer to run `scout:requirements` first?

Halt after emitting matching sub-condition block. Do not blend sub-condition copy.

---

### Normal branch — at least `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 0B.

===== END PHASE 0 =====

---

## ===== PHASE 0B: INERTIA ANALYSIS =====

Confirm [SCOUT-STATUS-TABLE] is present. If not, halt.

**PM: scan `scout-feasibility` and `scout-compliance` (if loaded) → record risk level → fill [IG-REGISTER] and [ID-REGISTER].**

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

### [IG-REGISTER] — Inertia Guards

Minimum 2 rows.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Responsible Role | Mitigation Location |
|-------|------------------------|----------------------|-------------|-----------------|---------------------|
| IG-01 | [describe status-quo default] | [name the scout artifact that reveals it is insufficient] | STANDARD / AMPLIFIED [cite trigger] | [PM / Strategy / Compliance / Design / Architect] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if applicable] | | | | |

> Responsible Role blank = C-23 structural fail for this row.
> AMPLIFIED rows: Named Artifact Trigger must address the risk dimension specifically.

### [ID-REGISTER] — Inertia Defeats

One row per IG row.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition] | [named evidence] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Confirming Role must match paired IG-XX Responsible Role.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF: either register is missing; any IG-XX Responsible Role blank; any ID-XX Confirming Role does not match paired IG-XX; row counts differ; any AMPLIFIED IG-XX Artifact Trigger is generic.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Confirm this gate is written here before proceeding to Phase 1.

===== END PHASE 0B =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

Confirm [INERTIA-ANALYZED] is present. If not, halt and state "[INERTIA-ANALYZED] missing."

**PM: scan `{topic}-requirements-{date}.md` → enumerate P0 requirements → fill [PM-COVERAGE-TABLE].**

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

**PM: scan `scout-feasibility` and `scout-compliance` → identify strongest non-requirements signal → fill [CNS-SLOT-1-OF-2].**

> CASCADE TO: [location 1 of 2: this phase, [CNS-SLOT-1-OF-2]] → [location 2 of 2: Phase 3 Purpose, [CNS-SLOT-2-OF-2]]
> The cross-namespace signal field appears in exactly 2 structurally independent locations. Completeness verifiable by counting labeled instances.

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> Source artifact blank = C-11 fires at location 1 of 2.

---

**PM: scan all rows in `{topic}-requirements-{date}.md` → name contradiction pairs as "R-XX vs R-YY" → fill [CONTRADICTION-SCAN]. Do not confirm "none found" without completing the scan; state the row range inspected.**

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF any of the following are absent from this block: [PM-COVERAGE-TABLE] with P0 rows or waiver; [CNS-SLOT-1-OF-2] with Source artifact filled; [CONTRADICTION-SCAN] with named scan outcome.
>
> Proof-of-work: [PM-CONTRACT-SEAL] presence certifies all three outputs are non-empty in this block.
> Guided sections may not begin until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

Confirm [PM-CONTRACT-SEAL] is present. If not, halt.

**Strategy: scan `scout-feasibility` and `scout-compliance` → validate spec viability → fill [STRATEGY-VALIDATION-TABLE].**

> CASCADE TO: [location 1 of 2: this phase, [STRATEGY-VALIDATION-TABLE]] → [location 2 of 2: Phase 3 Design, inline Strategy verdict]

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list new constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF [STRATEGY-VALIDATION-TABLE] absent or any Source Artifact cell is blank.
> Guided sections may not begin until [STRATEGY-SEAL] appears here.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

Confirm [PM-CONTRACT-SEAL] and [STRATEGY-SEAL] are both present. If either is missing, halt.

**Architect: use [PM-COVERAGE-TABLE] pre-assigned rows as the writing contract → fill each Spec Entry. Use [IG-REGISTER] and [ID-REGISTER] for mitigation placement. Do not re-enumerate either register.**

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

#### 1. Purpose

**PM: verify [CNS-SLOT-1-OF-2] → place cross-namespace signal at location 2 of 2 → write [CNS-SLOT-2-OF-2] in the table below.**

> Unified declaration inline within Purpose content block.
> CASCADE TO: [location 2 of 2: this section, [CNS-SLOT-2-OF-2]] — completing cascade declared in Phase 1.

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-XX guard, Responsible Role from [IG-REGISTER], paired ID-XX defeat condition — reference by number] |

> [CNS-SLOT-2-OF-2] blank = C-11 fires. Inertia context blank = IG/ID role bindings disconnected from spec body.

#### 2. Requirements

**PM: confirm all P0 rows from [PM-COVERAGE-TABLE] are placed → fill per-row coverage table below.**

> Unified declaration inline within Requirements content block.
> CASCADE TO: [location 1 of 1: this section, per-row coverage table]

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions (location 2 of 2 of Strategy cascade). For each IG-XX with Mitigation Location = Design, name the design element activating its paired ID-XX defeat. Include Responsible Role from [IG-REGISTER] as confirmation accountable party.

**Strategy: validate design against [STRATEGY-VALIDATION-TABLE] → record verdict inline.**

> Unified declaration inline within Design content block.
> CASCADE TO: [location 2 of 2: this section, inline Strategy verdict] — completing Strategy cascade from Phase 2.

[Write design content here]

IG/ID mitigation coverage (Design):
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element |
|-------|-------|-------|-----------------|-----------------|---------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe]

#### 4. Constraints

List constraints with source artifact names. For each IG-XX with Mitigation Location = Constraints, name the constraint and the Responsible Role confirming it.

**Compliance: validate constraint completeness against scout-compliance-{date}.md → record verdict inline.**

> Unified declaration inline within Constraints content block.
> CASCADE TO: [location 1 of 1: this section, inline Compliance verdict]

[List constraints with source artifact names]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. At least one per FINDING from Phases 0B–2. At least one per IG-XX with Mitigation Location = Open Questions not resolved. Name Responsible Role for each IG-derived question.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF all five sections are not present in this order: Purpose → Requirements → Design → Constraints → Open Questions.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

Confirm [SPEC-DRAFT-COMPLETE] is present. If not, halt.

**Architect: scan sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, role-binding completeness, and cascade completeness → fill [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [FINDINGS-TABLE]]
> Scan checklist:
> - IG/ID pair balance: [IG-REGISTER] row count = [ID-REGISTER] row count
> - Role binding: every IG-XX Responsible Role filled; every ID-XX Confirming Role matches paired IG-XX
> - Cascade completeness: CNS-SLOT 1 of 2 and 2 of 2; Strategy 1 of 2 and 2 of 2
> - Mitigation coverage: every IG-XX Mitigation Location has a named element in the correct section
> - Branch B sub-conditions: B-1 through B-4 VERBATIM blocks present in Phase 0 with anti-blend instruction

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — never absent or empty]

> **[SELF-REVIEW-SEAL]**
> INVALID IF [FINDINGS-TABLE] is absent or finding claim does not reference [SPEC-DRAFT-COMPLETE] as the scan source.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

Confirm [SELF-REVIEW-SEAL] is present.

**Produce at least 2 specific, actionable amendments → each names a section, a finding ID, and the exact change.**

INVALID IF fewer than 2 items or any item is vague.

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL].
[IG-REGISTER]/[ID-REGISTER]: row counts match; Responsible Role and Confirming Role filled and cross-matched.
CASCADE TO denominators verified: CNS-SLOT 1 of 2 + 2 of 2; Strategy 1 of 2 + 2 of 2.
Fallback Branch A with VERBATIM block; Branch B with sub-conditions B-1 through B-4 each with own VERBATIM block; anti-blend instruction present. State which branch or sub-condition applied.
All five sections in order. Frontmatter complete.

---

---

## V-05 — Full Combination: C-26 + C-27 + Role Sequence (Target 175/175 under v8)

**Axes**: All three — per-artifact Branch B sub-conditionals with anti-blend (C-26), imperative phrasing register throughout (C-27), and PM-first role sequence (Phase 1 PM pre-assignment before Phase 0B inertia analysis). Built on v7 V-05 full-combination base (C-22/C-23/C-24/C-25 all present).
**Hypothesis**: The three axes compose without conflict. PM-first ordering allows IG guards to reference pre-assigned requirement IDs in their Elimination Path. C-26 discriminates among fallback sub-scenarios with scenario-appropriate copy. C-27 phrasing applies uniformly to all actor-phase directives. The result satisfies all 27 v8 criteria: C-01 through C-25 from v7 V-05, plus C-26 and C-27 from v8. Target: 175/175 composite.

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
skill_version: v8
input: [list each loaded scout artifact by filename]
```

---

## ===== PHASE 0: SETUP =====

Check `simulations/scout/` for the seven artifacts below. Record each as LOADED or NOT FOUND.

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

Halt here. Do not compose an alternative response; emit the text above verbatim.

---

### Fallback Branch B — `{topic}-requirements-{date}.md` NOT FOUND, at least one other artifact LOADED

**Inspect [SCOUT-STATUS-TABLE] → identify which non-requirements artifacts are LOADED → match exactly one sub-condition → emit the matching VERBATIM RESPONSE block verbatim.**

Do not blend sub-condition copy; emit the matching block verbatim. Priority for overlapping matches: B-3 > B-2 > B-1 > B-4.

**B-1 — feasibility LOADED, compliance NOT FOUND, all others any combination:**

VERBATIM RESPONSE:
> I have your feasibility signal for this topic but no requirements artifact. I can author a spec grounded in the feasibility data — Design will be driven by feasibility constraints and I'll call out the scope gaps that requirements would normally fill. P0 coverage will be waived explicitly. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-2 — compliance LOADED, feasibility NOT FOUND, all others any combination:**

VERBATIM RESPONSE:
> I have your compliance findings for this topic but no requirements artifact. I can author a spec treating compliance posture as the primary constraint driver — the Constraints section will be compliance-anchored and each compliance-driven decision flagged. P0 coverage will be waived. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-3 — feasibility LOADED AND compliance LOADED, requirements NOT FOUND:**

VERBATIM RESPONSE:
> I have both feasibility and compliance signals for this topic but no requirements artifact. I can author a spec using both as primary inputs — feasibility shapes Design, compliance drives Constraints, and I'll waive P0 coverage explicitly with a note on decisions that would change if requirements were added. Should I proceed, or would you prefer to run `scout:requirements` first?

**B-4 — requirements NOT FOUND, feasibility NOT FOUND, compliance NOT FOUND, at least one of market / stakeholders / positioning / naming LOADED:**

VERBATIM RESPONSE:
> I have positioning or market signals for this topic but no requirements and no feasibility or compliance data. I can draft a spec from the available context — P0 coverage will be waived and constraint grounding will draw on the positioning signals. Should I proceed, or would you prefer to run `scout:requirements` first?

Halt after emitting matching sub-condition block. Do not blend sub-condition copy.

---

### Normal branch — at least `{topic}-requirements-{date}.md` LOADED

Proceed to Phase 1 (PM pre-assignment). **Note: Phase 1 runs before Phase 0B. PM assigns requirements first; inertia guards authored after requirement IDs are known.**

===== END PHASE 0 =====

---

## ===== PHASE 1: PM PRE-ASSIGNMENT =====

Confirm [SCOUT-STATUS-TABLE] is present. If not, halt.

**PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE]. Confirm [PM-COVERAGE-TABLE] is complete before writing [CNS-SLOT-1-OF-2].**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [PM-COVERAGE-TABLE]] — Architect receives [PM-COVERAGE-TABLE] as a pre-filled contract. Phase 0B receives [PM-COVERAGE-TABLE] to anchor inertia guards to named requirement IDs.

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

**PM: scan `scout-feasibility` and `scout-compliance` → identify strongest non-requirements signal → fill [CNS-SLOT-1-OF-2]. Name the specific artifact; do not leave Source artifact blank.**

> Unified declaration: role PM, sources named, action named, output named.
> CASCADE TO: [location 1 of 2: this phase, [CNS-SLOT-1-OF-2]] → [location 2 of 2: Phase 3 Purpose, [CNS-SLOT-2-OF-2]]
> The cross-namespace signal field appears in exactly 2 structurally independent locations. Completeness verifiable by counting labeled instances (1 of 2 + 2 of 2).

### [CNS-SLOT-1-OF-2] — Cross-namespace signal, location 1 of 2

| Field | Value |
|-------|-------|
| Source artifact | [name the specific loaded artifact] |
| Signal | [1-sentence description] |
| Spec impact | [1-sentence constraint or design decision] |

> Source artifact blank = C-11 fires at location 1 of 2.

---

**PM: scan all rows in `{topic}-requirements-{date}.md` → name contradiction pairs as "R-XX vs R-YY" → fill [CONTRADICTION-SCAN]. Do not state "none found" without completing the scan; name the row range inspected.**

> Unified declaration: role PM, source named, action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [CONTRADICTION-SCAN]]

### [CONTRADICTION-SCAN]

Contradiction pairs: [name "R-XX vs R-YY" or "none found after scanning R-01 through R-{n}"]

---

> **[PM-CONTRACT-SEAL]**
>
> INVALID IF any of the following are absent from this block: [PM-COVERAGE-TABLE] with P0 rows or waiver; [CNS-SLOT-1-OF-2] with Source artifact filled; [CONTRADICTION-SCAN] with named scan outcome.
>
> Proof-of-work: [PM-CONTRACT-SEAL] presence certifies all three outputs are non-empty in this block.
> Phase 0B may not begin until [PM-CONTRACT-SEAL] appears here.

===== END PHASE 1 =====

---

## ===== PHASE 0B: INERTIA ANALYSIS =====

Confirm [PM-CONTRACT-SEAL] is present. If not, halt and state "[PM-CONTRACT-SEAL] missing."

**PM: scan `scout-feasibility` and `scout-compliance` (if loaded) → record risk level → fill [IG-REGISTER] and [ID-REGISTER]. Where [PM-COVERAGE-TABLE] is populated, anchor Elimination Path entries to specific pre-assigned requirement IDs.**

> Unified declaration: role PM, sources named, action named, outputs named.
> CASCADE TO: guard/defeat outputs carry structural propagation via Mitigation Location column.

Risk level: AMPLIFIED if feasibility score < 70 or compliance = blocking. Otherwise STANDARD.

Feasibility score: [record or "NOT LOADED"]
Compliance status: [record or "NOT LOADED"]
Risk level this topic: STANDARD / AMPLIFIED

### [IG-REGISTER] — Inertia Guards

Minimum 2 rows. Where [PM-COVERAGE-TABLE] is populated, Elimination Path should reference the specific pre-assigned requirement ID the guard would violate.

| IG-ID | Guard: Default to Block | Named Artifact Trigger | Risk Signal | Responsible Role | Mitigation Location |
|-------|------------------------|----------------------|-------------|-----------------|---------------------|
| IG-01 | [describe status-quo default or existing alternative] | [name the scout artifact that reveals this default is insufficient] | STANDARD / AMPLIFIED [cite trigger] | [PM / Strategy / Compliance / Design / Architect] | Constraints / Open Questions / Design |
| IG-02 | [describe] | [name artifact] | STANDARD / AMPLIFIED | [role] | [location] |
| IG-03 | [add if applicable] | | | | |

> Responsible Role blank = C-23 structural fail for this row.
> AMPLIFIED rows: Named Artifact Trigger must address the risk dimension specifically.
> Where [PM-COVERAGE-TABLE] is populated: Elimination Path should name the pre-assigned requirement ID that the guard would contradict, when applicable.

### [ID-REGISTER] — Inertia Defeats

One ID row per IG row.

| ID-ID | Guards | Defeat Condition | Confirmation Evidence | Confirming Role |
|-------|--------|-----------------|----------------------|-----------------|
| ID-01 | IG-01 | [condition confirming guard succeeded — name specific spec decision, constraint, or design element] | [named evidence: spec entry, constraint ID, coverage count] | [must match IG-01 Responsible Role] |
| ID-02 | IG-02 | [condition] | [evidence] | [role] |
| ID-03 | IG-03 (if present) | | | |

> [ID-REGISTER] row count must equal [IG-REGISTER] row count. Confirming Role must match Responsible Role in paired IG-XX.

---

> **[INERTIA-ANALYZED]**
>
> INVALID IF: either register is missing; any IG-XX Responsible Role is blank; any ID-XX Confirming Role does not match its paired IG-XX; row counts differ; any AMPLIFIED IG-XX Artifact Trigger is generic rather than risk-specific.
>
> [INERTIA-ANALYZED] is a proof-of-work artifact. Its presence certifies [IG-REGISTER] and [ID-REGISTER] are structurally complete, role-bound, and pair-balanced in this block.
> Phase 2 is blocked until [INERTIA-ANALYZED] appears here.

===== END PHASE 0B =====

---

## ===== PHASE 2: STRATEGY VALIDATION =====

Confirm [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] are both present. If either is missing, halt.

**Strategy: scan `scout-feasibility` and `scout-compliance` → validate spec viability → fill [STRATEGY-VALIDATION-TABLE]. Name the specific source artifact for each check; do not leave Source Artifact cells blank.**

> Unified declaration: role Strategy, sources named, action named, output named.
> CASCADE TO: [location 1 of 2: this phase, [STRATEGY-VALIDATION-TABLE]] → [location 2 of 2: Phase 3 Design, inline Strategy verdict]
> Strategy validation appears in exactly 2 structural locations. Location 2 of 2 is a cascade destination — inline Design verdict must reference [STRATEGY-VALIDATION-TABLE] by name.

### [STRATEGY-VALIDATION-TABLE]

| Check | Source Artifact | Verdict | Finding |
|-------|----------------|---------|---------|
| Technical feasibility | scout-feasibility-{date}.md | PASS / FINDING | [describe] |
| Compliance posture | scout-compliance-{date}.md | PASS / FINDING | [describe] |
| Constraint additions | [name artifact] | [list new constraints] | — |

> **[STRATEGY-SEAL]**
> INVALID IF [STRATEGY-VALIDATION-TABLE] absent or any Source Artifact cell is blank.
> Guided sections may not begin until [STRATEGY-SEAL] appears here.

===== END PHASE 2 =====

---

## ===== PHASE 3: GUIDED SECTIONS =====

Confirm [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], and [STRATEGY-SEAL] are all present. If any is missing, halt.

**Architect: use [PM-COVERAGE-TABLE] pre-assigned rows as the writing contract → fill each Spec Entry. Use [IG-REGISTER] and [ID-REGISTER] for mitigation placement. Do not re-enumerate either register.**

SECTION ORDER: Purpose → Requirements → Design → Constraints → Open Questions

#### 1. Purpose

**PM: verify [CNS-SLOT-1-OF-2] → place cross-namespace signal at location 2 of 2 → write [CNS-SLOT-2-OF-2] in the table below. Leave the cell visibly blank if no signal was identified in Phase 1.**

> Unified declaration inline within Purpose content block.
> CASCADE TO: [location 2 of 2: this section, [CNS-SLOT-2-OF-2]] — completing cascade declared in Phase 1. Two-location coverage verifiable by counting labeled instances (1 of 2 in Phase 1, 2 of 2 here).

| Field | Value |
|-------|-------|
| Core function | [what it does] |
| Primary user | [who uses it] |
| Problem solved | [what problem] |
| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal — must match [CNS-SLOT-1-OF-2]] |
| Inertia context | [1-sentence: dominant IG-XX guard, Responsible Role from [IG-REGISTER], paired ID-XX defeat condition — reference by number] |

> [CNS-SLOT-2-OF-2] blank = C-11 fires. Inertia context blank = IG/ID role bindings disconnected from spec body.

#### 2. Requirements

**PM: confirm all P0 rows from [PM-COVERAGE-TABLE] are placed → fill per-row coverage table below. Do not add new rows; use the pre-assigned rows as the contract.**

> Unified declaration inline within Requirements content block.
> CASCADE TO: [location 1 of 1: this section, per-row coverage table] — single instantiation.

| Req ID | Requirement Text | Priority | Spec Entry | Status |
|--------|-----------------|----------|------------|--------|
| R-01 | [from scout-requirements] | P0 | [exact name from [PM-COVERAGE-TABLE]] | COVERED |
| ... | | | | |

P0 coverage: {n}/{n}. Waiver: [YES / NO].

#### 3. Design

Describe architecture and key technical decisions. Reference [STRATEGY-VALIDATION-TABLE] constraint additions (location 2 of 2 of Strategy cascade). For each IG-XX with Mitigation Location = Design, name the design element activating its paired ID-XX defeat. Include Responsible Role from [IG-REGISTER] as the confirmation accountable party.

**Strategy: validate design against [STRATEGY-VALIDATION-TABLE] → record verdict inline. This verdict is location 2 of 2 of the Strategy cascade.**

> Unified declaration inline within Design content block.
> CASCADE TO: [location 2 of 2: this section, inline Strategy verdict] — completing Strategy cascade from Phase 2.

[Write design content here]

IG/ID mitigation coverage (Design):
| IG-ID | ID-ID | Guard | Responsible Role | Defeat Condition | Mitigation Element |
|-------|-------|-------|-----------------|-----------------|---------------------|
| IG-01 | ID-01 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |
| IG-02 | ID-02 | [from [IG-REGISTER]] | [from [IG-REGISTER]] | [from [ID-REGISTER]] | [design element or "N/A — ELIMINATED"] |

Strategy validation (inline): PASS / FINDING: [describe] [references [STRATEGY-VALIDATION-TABLE] from Phase 2]

#### 4. Constraints

List constraints with source artifact names. For each IG-XX with Mitigation Location = Constraints, name the constraint and the Responsible Role confirming it.

**Compliance: validate constraint completeness against scout-compliance-{date}.md → record verdict inline.**

> Unified declaration inline within Constraints content block.
> CASCADE TO: [location 1 of 1: this section, inline Compliance verdict] — single instantiation.

[List constraints with source artifact names]

IG-XX constraints: [list constraints from REQUIRES SPEC MITIGATION rows in [IG-REGISTER] where Mitigation Location = Constraints; name Responsible Role as confirmation accountable party for each]

Compliance validation (inline): PASS / FINDING: [describe]

#### 5. Open Questions

List unresolved questions. At least one per open FINDING from Phases 0B–2. At least one per IG-XX with Mitigation Location = Open Questions not fully resolved in Design or Constraints. Name Responsible Role from [IG-REGISTER] for each IG-derived question.

[List open questions — numbered]

---

> **[SPEC-DRAFT-COMPLETE]**
> INVALID IF all five guided sections are not present in this order: Purpose → Requirements → Design → Constraints → Open Questions.

===== END PHASE 3 =====

---

## ===== PHASE 4: SELF-REVIEW =====

Confirm [SPEC-DRAFT-COMPLETE] is present. If not, halt.

**Architect: scan sections 1–5 → surface contradictions, gaps, ambiguities, hotspots, IG/ID mitigation gaps, role-binding completeness, and cascade completeness → fill [FINDINGS-TABLE].**

> Unified declaration: role Architect, source [SPEC-DRAFT-COMPLETE], action named, output named.
> CASCADE TO: [location 1 of 1: this phase, [FINDINGS-TABLE]] — single instantiation.
> Scan checklist:
> - IG/ID pair balance: [IG-REGISTER] row count = [ID-REGISTER] row count
> - Role binding: every IG-XX Responsible Role filled; every ID-XX Confirming Role matches paired IG-XX
> - Cascade completeness: CNS-SLOT 1 of 2 (Phase 1) + 2 of 2 (Purpose) both filled; Strategy 1 of 2 (Phase 2) + 2 of 2 (Design inline) both filled
> - Mitigation coverage: every IG-XX Mitigation Location has a named element in the correct section
> - Branch B sub-conditions: B-1 through B-4 VERBATIM blocks present in Phase 0; anti-blend instruction present; priority rule stated
> - Phase order: Phase 1 ran before Phase 0B; [PM-CONTRACT-SEAL] precedes [INERTIA-ANALYZED] in document

| # | Type | Location | Description | Proposed Amendment |
|---|------|----------|-------------|-------------------|
| F-01 | [type] | [section] | [describe] | [propose] |
| ... | | | | |

Finding claim: [explicit scan outcome — never absent or empty; must reference [SPEC-DRAFT-COMPLETE] as the scan source]

> **[SELF-REVIEW-SEAL]**
> INVALID IF [FINDINGS-TABLE] is absent or finding claim does not reference [SPEC-DRAFT-COMPLETE] as the scan source.

===== END PHASE 4 =====

---

## ===== PHASE 5: AMEND =====

Confirm [SELF-REVIEW-SEAL] is present.

**Produce at least 2 specific, actionable amendments → each names a section, a finding ID, and the exact change.**

INVALID IF fewer than 2 items or any item is vague.

1. [Section: X / Finding: F-NN / Change: describe exactly]
2. [Section: X / Finding: F-NN / Change: describe exactly]

===== END PHASE 5 =====

---

## Output

Write the completed artifact to `simulations/draft/specs/{topic}-spec-{date}.md`.
Gate tokens in document: [PM-CONTRACT-SEAL] (Phase 1), [INERTIA-ANALYZED] (Phase 0B), [STRATEGY-SEAL] (Phase 2), [SPEC-DRAFT-COMPLETE] (Phase 3), [SELF-REVIEW-SEAL] (Phase 4).
Phase execution order: Phase 0 → Phase 1 → Phase 0B → Phase 2 → Phase 3 → Phase 4 → Phase 5. [PM-CONTRACT-SEAL] precedes [INERTIA-ANALYZED].
[IG-REGISTER]/[ID-REGISTER]: row counts match; Responsible Role and Confirming Role filled and cross-matched; AMPLIFIED rows address named threshold dimension; where [PM-COVERAGE-TABLE] populated, Elimination Path references pre-assigned requirement IDs.
CASCADE TO denominators verified: CNS-SLOT 1 of 2 + 2 of 2; Strategy 1 of 2 + 2 of 2.
Fallback Branch A (ALL NOT FOUND) with VERBATIM block; Fallback Branch B with sub-conditions B-1 through B-4 each with own VERBATIM block; anti-blend instruction and priority rule present. State which branch or sub-condition applied.
All five sections in order. Frontmatter complete.
