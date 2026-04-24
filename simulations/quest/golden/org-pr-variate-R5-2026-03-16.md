---
skill: quest-variate
skill_target: org-pr
round: 5
date: 2026-03-16
rubric: org-pr-rubric-v5-2026-03-16.md
---

# org-pr — Round 5 Variations

**Rubric version**: v5 | **N_aspirational**: 12 | **Target composite**: 95+

## Round 5 Objectives

| Objective | Criterion | Status entering R5 |
|-----------|-----------|-------------------|
| Seal conflict resolution path | C-07 / C-22 | PARTIAL all 4 rounds |
| Phase/lifecycle gating | C-09 | FAIL/PARTIAL all 4 rounds |
| Verdict hardening pair (C-11+C-14 co-occur) | C-19 | New in v5 |
| Priority table for N≥3 axes | C-20 | New in v5 |
| Authority-inertia reconciliation declaration | C-21 | New in v5 |
| Conflict resolution column | C-22 | New in v5 / R5 hypothesis |

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-22 isolation — Resolution column only | Minimal prompt + Resolution column closes C-07 without side effects |
| V-02 | C-09 isolation — Pre-merge phase gate only | Explicit phase gate instruction alone achieves C-09 PASS |
| V-03 | C-22 + C-09 two-axis | Conflict resolution + lifecycle gate compose without interference |
| V-04 | C-22 + C-21 + C-09 three-axis with priority table | Three new targets govern distinct elements; C-20 table required |
| V-05 | Full integration (R4 V-05 base + all v5 criteria) | Seal all gaps from R4; first attempt at 100/100 on aspirational pool |

---

## V-01 — C-22 Isolation (Resolution Column Only)

**Axis**: Conflict resolution column
**Hypothesis**: Adding only the Resolution column to the conflict output template — with the explicit authority-position rule — closes C-07 while leaving all other scores from a clean R4 baseline unchanged.

---

You are running /org-pr for: {{topic}}

### Role Loading

Read `.roles/`. For each file, the role locator is valid if the file exists and the `name:` field is non-empty.

**Locator self-correction gate**: before proceeding with any role, verify its locator. If YES (locator valid): include the role. If NO (locator invalid): rewrite to the most specific anchor that exists in `.roles/`, then include.

### Role Selection

Examine the PR diff. For each changed file, identify which roles hold expertise over that file type, layer, or domain. A role is selected if at least one changed file falls within its area.

For each selected role, state:
- Role name
- Authority position in the review sequence
- Changed files that triggered selection

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Roles at later positions document downstream effects of earlier-authority findings. They do not revise or override upstream findings.

### Per-Role Review

Run each selected role in authority-chain order.

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | Downstream Risk |
|---------|----------|-----------------|
| [description] | P1 / P2 / P3 | [cascading effect if not resolved] |

Severity definitions:
- P1: blocks merge; must resolve before Go verdict
- P2: must resolve or carry a documented exception before merge
- P3: advisory; may defer

### Verdict Formula

Any P1 finding = No-Go. This formula is not editable, no exceptions.

Composite:
- P1 present → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1, no P2) → Go

There is no third outcome. The only alternatives to Go are No-Go and Conditional-Go. Reclassify any P1 or accept No-Go.

### Consensus Analysis

After all per-role sections, produce:

**Projection call**: ALIGNED or DIVERGENT — state whether all roles project the same future-state trajectory for the feature area after merge. One sentence explaining the direction.

If DIVERGENT: list the roles, the surfaces they disagree on, and the direction of disagreement.

### Conflict Analysis

When two or more roles hold incompatible assessments of the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs; Role B records position as downstream risk entry on Role A's finding row] |

**Resolution column instruction**: the role with the lower position number (earlier in the authority chain) governs. The higher-position role does not record a counter-finding; it records a downstream risk entry on the governing role's finding row.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [list the P1 and P2 findings that determine the verdict; or "no P1/P2 findings — Go"]

Pre-commit self-check: before writing the verdict block, verify:
1. Every finding has a severity tag (P1/P2/P3).
2. The verdict follows the formula above with no modification.
3. The Conflict table Resolution column is populated for every row.
4. Every role locator resolves to an existing file in `.roles/`.

---

## V-02 — C-09 Isolation (Pre-Merge Phase Gate)

**Axis**: Lifecycle emphasis — explicit pre-merge phase gate
**Hypothesis**: Embedding the review inside a named lifecycle phase with explicit do-not-run-after-merge boundary achieves C-09 PASS cleanly as a single-axis isolation.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**This skill runs at the PRE-MERGE gate only.**

- Execute this review before the PR is merged to the target branch.
- Do not run this skill on a PR that has already been merged. Post-merge surface area expands and per-role scope changes; post-merge review requires `/org-review`.
- If the PR has already been merged: halt and report — "org-pr must run pre-merge; post-merge review requires org-review."

Confirm: PR is at pre-merge gate before continuing.

### Role Loading

Read `.roles/`. Role locator is valid if the file exists and `name:` is non-empty.

**Locator self-correction gate**: If locator valid → include. If locator invalid → rewrite to the most specific anchor that exists in `.roles/`, then include.

### Role Selection

From the PR diff, select roles whose expertise covers the changed files. For each selected role, list the changed file(s) that triggered its selection.

### Per-Role Review

For each selected role:

**[Role Name]** | Selected because: [files]

| Finding | Severity | Downstream Risk |
|---------|----------|-----------------|
| [description] | P1 / P2 / P3 | [effect if not resolved before merge] |

Severity:
- P1: blocks merge at this gate
- P2: requires resolution or documented exception before merge
- P3: advisory; may carry forward

### Verdict Formula

Any P1 = No-Go. This formula is not editable and has no exceptions.

- P1 present → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1, no P2) → Go

No third outcome exists. Reclassify the P1 or accept No-Go.

### Consensus Analysis

**Phase projection**: given the current pre-merge diff state, state ALIGNED or DIVERGENT — do all roles project the same trajectory for the feature area after merge? One sentence.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE — this verdict applies to the current diff state only.

---

## V-03 — C-22 + C-09 Two-Axis (Conflict Resolution Column + Phase Gate)

**Axis**: Conflict resolution column + lifecycle phase gate
**Hypothesis**: C-22 governs the conflict table template (output structure); C-09 governs when the skill runs (lifecycle phase). They operate on distinct elements and should compose without interference. Both should PASS without a priority table (only 2 axes).

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles document downstream effects of earlier findings; they do not override them.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | Downstream Risk |
|---------|----------|-----------------|
| [text] | P1 / P2 / P3 | [cascading effect] |

### Verdict Formula

Any P1 = No-Go. Formula is closed: not editable, no exceptions.

- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

No third outcome. Reclassify the P1 or accept No-Go.

### Consensus Analysis

**Projection call**: ALIGNED or DIVERGENT — all roles projecting the same post-merge trajectory? State direction in one sentence.

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs; pos M assessment recorded as downstream risk on pos N's finding] |

**Resolution column rule**: role with lower position number governs. Higher-position role's assessment is not a counter-finding — it is a downstream risk entry under the governing finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding has a severity tag.
2. Verdict follows the formula; no modification path used.
3. Conflict Resolution column populated for every row.
4. All locators valid or self-corrected.

---

## V-04 — Three-Axis with Priority Table (C-22 + C-21 + C-09)

**Axis**: Conflict resolution column + authority-inertia reconciliation declaration + lifecycle gate
**Hypothesis**: Three new/unsealed criteria govern distinct output elements (conflict table output, inertia framing semantics, lifecycle phase). Priority table required per C-20 (3+ axes). Explicit C-21 declaration should produce C-21 PASS without destabilizing C-13 or C-17.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE only.** Halt if PR has already merged: "org-pr is a pre-merge skill; use org-review for post-merge."

### Axis Composition Table

This prompt uses three composition axes. When axes produce conflicting instructions, this table governs:

| Axis | Governs | Yields To |
|------|---------|-----------|
| Authority chain | Review order; constraint propagation direction | Nothing (highest priority) |
| Inertia framing | Finding content (if-stays projections) | Authority chain |
| Conflict resolution | Conflict table output (Resolution column logic) | Authority chain |

**Tiebreaker default**: authority chain governs when any axis conflicts with it. Inertia framing and conflict resolution govern orthogonal elements and do not conflict with each other.

### Authority-Inertia Reconciliation Rule

Inertia framing (if-stays projections) is permitted and required for all findings. When a later-authority role projects an if-stays outcome on a surface already covered by an earlier-authority finding, that projection describes the **compounding cost** of the upstream finding going unresolved — not a reclassification of the finding. The upstream finding remains at its declared severity. The if-stays projection is recorded as a downstream risk entry under the governing finding, not as a counter-finding.

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.roles/`, then include.

### Role Selection

From the PR diff, select roles by changed file surface area. State each role and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Roles at later positions may add if-stays projections on upstream findings as compounding cost descriptions. They do not revise upstream severity or override upstream decisions.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect on other surfaces] |

### Verdict Formula

Any P1 = No-Go. This formula is closed: not editable, no exceptions.

- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

No third outcome. Reclassify the P1 or accept No-Go.

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point in the same direction? State the direction explicitly.

If DIVERGENT: list the roles, surfaces, and divergent projection directions.

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs per authority chain; Role B if-stays recorded as compounding cost under Role A's finding] |

**Resolution column rule** (per authority chain axis): role with lower position number governs. Higher-position role's assessment is recorded as a compounding cost / if-stays projection entry, not a counter-finding or override.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding has severity + if-stays projection filled.
2. Verdict follows the formula; no modification path used.
3. Conflict Resolution column populated for every row.
4. No later-authority finding overrides an earlier-authority finding; if-stays on upstream findings recorded as compounding cost.
5. All locators valid or self-corrected.

---

## V-05 — Full Integration (R4 V-05 Base + All v5 Criteria)

**Axis**: Full integration — R4 V-05 base extended with C-22 (resolution column), C-09 (phase gate), explicit C-19 (hardening pair co-occurrence), and eight-axis priority table
**Hypothesis**: Building directly on R4 V-05 (92 composite), adding the Resolution column to the conflict template and the pre-merge phase gate closes the two remaining PARTIAL gaps (C-07/C-09) while retaining all 8 existing aspirational PASSes. All four new v5 aspirational criteria should PASS. Target: first round to achieve 95+ composite.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

Check the PR state before proceeding:
- If PR is open and not yet merged: continue.
- If PR has already been merged: halt — "org-pr is a pre-merge skill. Post-merge scope has changed; use /org-review instead."

This verdict applies to the pre-merge diff state only.

### Axis Composition Table

This prompt uses eight composition axes. When instructions across axes conflict, this table governs:

| Axis | Governs | Yields To |
|------|---------|-----------|
| Authority chain | Review order; constraint propagation; conflict resolution | Nothing (highest priority) |
| Inertia framing | Finding content (if-stays projections) | Authority chain |
| Conflict resolution column | Conflict table output structure (Resolution field) | Authority chain |
| Finding format | Row structure (severity + if-stays + downstream risk columns) | Authority chain |
| Verdict formula | Go/No-Go/Conditional-Go derivation | Authority chain |
| Locator self-correction | Role inclusion gate (valid/rewrite/include) | Nothing (runs before review phases) |
| Phrasing register | Field label validity; heading names | Finding format |
| Phase gate | Skill execution guard (pre-merge only) | Nothing (runs before all other axes) |

**Tiebreaker default**: when any two axes conflict and neither is listed as yielding to the other, authority chain governs.

### Authority-Inertia Reconciliation Rule

Inertia framing is required for every finding. When a role at a later authority position adds an if-stays projection to a surface already covered by an earlier-authority finding, that projection describes the **compounding cost** of the upstream finding going unresolved. It is not a reclassification of the upstream finding and does not change its severity. The upstream finding remains at its declared severity; the if-stays projection is recorded as a downstream risk entry under that finding, not as a counter-finding.

### Verdict Hardening Pair

The verdict formula has two properties that must both be present:

1. **Formula lock**: Any P1 finding = No-Go. This formula is not editable, no exceptions, no modifiers. No role, no authority level, and no contextual argument may modify it.

2. **Escape closure**: The complete set of possible verdicts is: Go, Conditional-Go, No-Go. There is no fourth outcome. If a P1 exists and Go is claimed, the claim is invalid — reclassify the P1 or accept No-Go. The only escape from No-Go is P1 reclassification; no other escape path exists.

Both properties must be satisfied simultaneously. A locked formula with an unspecified escape still allows a P1 + Go claim. An escape closure without a locked formula allows formula modification before the escape check. The pair closes the decision space completely.

### Role Loading

Read `.roles/`. A locator is valid if the file exists and `name:` is non-empty.

**Locator self-correction gate**: For each role needed in this review:
- If locator valid → include.
- If locator invalid → rewrite to the most specific anchor that exists in `.roles/`, then include.

Do not exclude a role because its locator is invalid. Rewrite first, then include.

### Role Selection

Examine the PR diff. For each changed file, map to roles whose expertise area covers that file's type, layer, or domain. A role is selected if at least one changed file falls within its area.

State for each selected role:
- Role name and slug
- Authority position in the review sequence
- Changed files that triggered its selection

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Authority position 1 (Security) holds the highest authority. Roles at later positions:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on surfaces covered by earlier roles — as compounding cost descriptions only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

Run each selected role in order of authority position.

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [finding description] | P1 / P2 / P3 | [compounding cost if this finding is not resolved before merge] | [cascading effect on other surfaces, teams, or systems] |

Named invalid finding forms (do not use):
- Untagged findings (no severity label) — invalid; rewrite with P1/P2/P3 before including.
- Findings that revise an earlier role's severity — invalid; record as if-stays projection instead.
- Aggregate findings that combine two distinct surfaces — invalid; split into separate rows.

### Verdict Formula (locked + escape closed)

**Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions. No role authority overrides this.

**Composite derivation**:
- Any P1 present → No-Go
- All P2, no P1 → Conditional-Go
- All P3, no P1/P2 → Go

**Escape closure**: The verdict set is {Go, Conditional-Go, No-Go}. There is no fourth outcome. All escape paths are:
- "P1 is actually P2" → reclassify; carry documented rationale; formula re-evaluates with new severity.
- "Accept No-Go" → record and halt.
No other escape path exists. A P1 + Go claim is invalid under this formula.

### Consensus Analysis

After all per-role sections:

**Projection convergence call**: ALIGNED or DIVERGENT.

State whether all roles' if-stays projections point in the same direction (feature area stable vs. degrading). Provide one sentence naming the projection direction.

If DIVERGENT: list the roles, the surfaces they diverge on, and the divergent projection directions.

### Conflict Analysis

When two roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface description] | [Role A's assessment of this surface] | [Role B's assessment] | [pos N governs; Role B's position recorded as compounding-cost entry on Role A's finding; Role B does not hold a counter-finding on this surface] |

**Resolution column instruction**: The role with the lower authority position number governs. This is derived mechanically from the authority chain — no judgment required. The higher-position role's incompatible assessment is not discarded; it is re-recorded as an if-stays projection (compounding cost entry) under the governing role's finding row. It does not appear in the Conflict table as an unresolved finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [list each P1 and P2 finding that determines the verdict, or "no P1/P2 findings — Go"]
**Gate**: PRE-MERGE — verdict applies to current diff state only.

Pre-commit self-check: before writing the verdict block, verify all of the following:

1. Every finding row has severity (P1/P2/P3) filled.
2. Every finding row has if-stays projection filled.
3. The verdict follows the formula with no modification, no escape path used outside the declared set.
4. The Conflict table Resolution column is populated for every row with the authority-position logic.
5. No later-authority finding overrides or revises an earlier-authority finding; if-stays on upstream surfaces are compounding-cost entries.
6. All role locators either resolved to valid `.roles/` files or were self-corrected before inclusion.
7. Named invalid forms (untagged, revision, aggregate) do not appear in any finding row.

---

## Variation Summary

| Variation | Primary Axis | New Criteria Targeted | R4 Baseline |
|-----------|-------------|----------------------|-------------|
| V-01 | C-22 isolation | C-07/C-22 | R4 V-03 structure |
| V-02 | C-09 isolation | C-09 | Minimal clean baseline |
| V-03 | C-22 + C-09 | C-07/C-22, C-09 | R4 V-03 + phase gate |
| V-04 | C-22 + C-21 + C-09 + table | C-07/C-22, C-09, C-21, C-20 | Three-axis + priority table |
| V-05 | Full integration | All v5 criteria | R4 V-05 + resolution column + phase gate |
