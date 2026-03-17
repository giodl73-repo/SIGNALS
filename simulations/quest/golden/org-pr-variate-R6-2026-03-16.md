---
skill: quest-variate
skill_target: org-pr
round: 6
date: 2026-03-16
rubric: org-pr-rubric-v6-2026-03-16.md
---

# org-pr — Round 6 Variations

**Rubric version**: v6 | **N_aspirational**: 15 | **R5 V-05 baseline**: 100.00

## Round 6 Objectives

R5 V-05 achieved 100/100 against the v6 rubric. R6 investigation question (from rubric):
"Whether a prompt can achieve C-23 + C-25 *without* requiring the full V-05 complexity —
can judgment-elimination and coupling labels appear in simpler single-axis designs, or do
they only emerge naturally in 3+ axis compositions?"

| Objective | Criterion | Status entering R6 |
|-----------|-----------|-------------------|
| C-23 in minimal design (no phase gate, no inertia) | C-23 | FAIL in V-01–V-04; PASS only in V-05 |
| C-25 in mid-complexity (no inertia, C-14 still PARTIAL) | C-25 | FAIL in V-01–V-04; PASS only in V-05 |
| C-23 + C-25 compose at mid-complexity | C-23, C-25 | Untested combination at V-03 level |
| 100/100 at 3-axis (not 8-axis) | All 15 | V-04 was 97.33 due to C-23/C-25/C-14 FAIL |
| 100/100 at 2-axis (no priority table) | All 15 | Untested; N/A path may cover C-18/C-20 |

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-23 isolation in minimal design | Adding "derived mechanically — no judgment required" to a minimal prompt achieves C-23 PASS without phase gate, inertia, or coupling label |
| V-02 | C-25 isolation at mid-complexity | Adding "Verdict Hardening Pair" label to a V-03-level design achieves C-25 PASS without requiring C-14 escape closure |
| V-03 | C-23 + C-25 two-axis | Both R6 declarations compose cleanly at V-03 complexity; C-14 remains PARTIAL; tests whether the two criteria are independent of each other |
| V-04 | All 3 R6 criteria + C-14 escape closure in 3-axis | First 100/100 at 3-axis complexity (not 8-axis); C-20 fires legitimately vs. N/A→PASS |
| V-05 | 2-axis complete (minimal 100/100) | Achieves 100/100 with 2 governance axes and no priority table; C-18/C-20 N/A→PASS path means full score is achievable below the priority-table threshold |

---

## V-01 — C-23 Isolation (Judgment-Elimination in Minimal Design)

**Axis**: C-23 judgment-elimination declaration only
**Hypothesis**: Adding "derived mechanically from the authority chain — no judgment required"
to the resolution column of a minimal design (no phase gate, no inertia, no coupling label)
achieves C-23 PASS. Expected delta over R5 V-01: +0.67 pts (C-23 PASS vs FAIL).

---

You are running /org-pr for: {{topic}}

### Role Loading

Read `.craft/roles/`. For each file, the role locator is valid if the file exists and the `name:` field is non-empty.

**Locator self-correction gate**: before proceeding with any role, verify its locator. If YES (locator valid): include the role. If NO (locator invalid): rewrite to the most specific anchor that exists in `.craft/roles/`, then include.

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
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; Role B records its position as a downstream risk entry on Role A's finding row] |

**Resolution column instruction**: The role with the lower position number (earlier in the authority chain) governs. This is derived mechanically from the authority chain — no judgment required. The higher-position role does not record a counter-finding; it records a downstream risk entry on the governing role's finding row.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [list the P1 and P2 findings that determine the verdict; or "no P1/P2 findings — Go"]

Pre-commit self-check: before writing the verdict block, verify:
1. Every finding has a severity tag (P1/P2/P3).
2. The verdict follows the formula above with no modification.
3. The Conflict table Resolution column is populated for every row.
4. Every role locator resolves to an existing file in `.craft/roles/`.

---

## V-02 — C-25 Isolation (Coupling Label at Mid-Complexity)

**Axis**: C-25 co-occurrence coupling label only
**Hypothesis**: Adding a "Verdict Hardening Pair" section header to a V-03-level design
(phase gate + resolution column) achieves C-25 PASS without requiring C-14 escape closure.
C-14 remains PARTIAL because "no fourth outcome" does not add "No other escape path exists."
Expected delta over R5 V-03: +0.67 pts (C-25 PASS vs FAIL).

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.craft/roles/`, then include.

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

### Verdict Hardening Pair

The verdict has two properties that must co-occur:

1. **Formula lock**: Any P1 finding = No-Go. This formula is not editable, no exceptions.

2. **Outcome set**: The complete verdict set is: Go, Conditional-Go, No-Go. There is no fourth outcome. Reclassify any P1 or accept No-Go.

Both must be satisfied simultaneously.

Composite derivation:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection call**: ALIGNED or DIVERGENT — all roles projecting the same post-merge trajectory? State direction in one sentence.

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs per authority chain; pos M assessment recorded as downstream risk on pos N's finding] |

**Resolution column rule**: role with lower position number governs. Higher-position role's assessment is not a counter-finding — it is a downstream risk entry under the governing finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding has a severity tag.
2. Verdict follows the Verdict Hardening Pair formula; no modification path used.
3. Conflict Resolution column populated for every row.
4. All locators valid or self-corrected.

---

## V-03 — C-23 + C-25 Two-Axis (Mid-Complexity)

**Axis**: C-23 judgment-elimination + C-25 coupling label, both at V-03 complexity
**Hypothesis**: The two R6 declarations are independent of each other — C-23 operates on
the conflict table's Resolution column; C-25 operates on the verdict formula section header.
They should compose without interference in a mid-complexity design. C-13 and C-14 remain
FAIL/PARTIAL (no inertia, no escape closure). Expected composite: 98.00 (+1.33 over R5 V-03).

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.craft/roles/`, then include.

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

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding = No-Go. This formula is not editable, no exceptions.

2. **Outcome set**: The complete verdict set is: Go, Conditional-Go, No-Go. There is no fourth outcome. Reclassify any P1 or accept No-Go.

Both must be satisfied simultaneously.

Composite derivation:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection call**: ALIGNED or DIVERGENT — all roles projecting the same post-merge trajectory? One sentence.

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; pos M assessment recorded as downstream risk on pos N's finding] |

**Resolution column rule**: The role with the lower position number governs. This is derived mechanically from the authority chain — no judgment required. The higher-position role's assessment is not a counter-finding; it is a downstream risk entry under the governing finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding has a severity tag.
2. Verdict follows the Verdict Hardening Pair formula; no modification path used.
3. Conflict Resolution column populated for every row with authority-position logic.
4. All locators valid or self-corrected.

---

## V-04 — All Three R6 Criteria + C-14 Escape Closure in 3-Axis Design

**Axis**: C-23 + C-24 + C-25 + C-14 escape closure, at 3-axis complexity (priority table fires)
**Hypothesis**: All three R6 new criteria (C-23, C-24, C-25) plus C-14 escape closure can be
achieved with a 3-axis priority table — not the 8-axis table of R5 V-05. The 3-axis table
(authority chain + inertia + conflict resolution) triggers C-20 PASS legitimately (not N/A).
This should be the first 100/100 design that is not R5 V-05. Target composite: 100.00.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already been merged: halt — "org-pr is a pre-merge skill. Post-merge scope has changed; use /org-review instead."

### Axis Composition Table

This prompt uses three composition axes. When axes produce conflicting instructions, this table governs:

| Axis | Governs | Yields To |
|------|---------|-----------|
| Authority chain | Review order; conflict resolution; constraint propagation | Nothing (highest priority) |
| Inertia framing | Finding content (if-stays projections) | Authority chain |
| Conflict resolution column | Conflict table output (Resolution field logic) | Authority chain |

**Tiebreaker default**: authority chain governs when any two axes conflict.

### Authority-Inertia Reconciliation Rule

Inertia framing (if-stays projections) is required for all findings. When a later-authority role adds an if-stays projection to a surface already covered by an earlier-authority finding, that projection describes the **compounding cost** of the upstream finding going unresolved — not a reclassification. The upstream finding remains at its declared severity; the if-stays projection is recorded as a downstream risk entry, not a counter-finding.

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.craft/roles/`, then include.

### Role Selection

From the PR diff, select roles by changed file surface area. State each selected role, its authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no fourth outcome. All escape paths:
   - Reclassify the P1 to P2 with documented rationale; formula re-evaluates with new severity.
   - Accept No-Go and record.
   No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. Formula lock without escape closure allows novel escape claims. Escape closure without formula lock allows formula modification before the escape check. The pair closes the decision space completely.

Composite derivation:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point in the same direction? State the direction explicitly. If DIVERGENT: list roles, surfaces, and divergent projection directions.

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; Role B's position recorded as compounding-cost entry on Role A's finding] |

**Resolution column instruction**: The role with the lower authority position number governs. This is derived mechanically from the authority chain — no judgment required. The higher-position role's assessment is recorded as a compounding-cost / if-stays entry, not a counter-finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
3. Conflict Resolution column populated for every row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are compounding-cost entries.
5. Named invalid forms (untagged, revision, aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-05 — 2-Axis Complete (Minimal 100/100)

**Axis**: 2 governance axes only (authority chain + inertia); conflict resolution embedded in
authority chain section; no priority table needed (N<3 triggers C-18/C-20 N/A→PASS)
**Hypothesis**: 100/100 is achievable without a priority table. With only 2 declared
governance axes, C-18 and C-20 resolve as N/A→PASS. Conflict resolution embedded in
the authority chain section (not declared as a third axis) achieves C-22/C-23 PASS.
All structural elements (Verdict Hardening Pair, correction catalog, escape closure)
can be present without axis proliferation. Demonstrates that N/A paths are not structural
debt — they represent legitimate design choices that still close all criteria.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a pre-merge skill; post-merge scope has changed; use /org-review instead."

### Authority-Inertia Governance

This prompt operates under two governance axes. Authority chain governs review order and constraint propagation direction. Inertia framing governs finding content (if-stays projections). When they appear to conflict: authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces already covered by earlier-authority findings. Those projections describe the **compounding cost** of the upstream finding going unresolved — not a reclassification of the upstream finding. The upstream finding remains at its declared severity.

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific anchor in `.craft/roles/`, then include.

### Role Selection

From the PR diff, select roles by changed file surface area. State each selected role, its authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

**Conflict resolution (embedded)**: When roles hold incompatible assessments on the same surface, the role with the lower authority position number governs. This is derived mechanically from the authority chain — no judgment required. The higher-position role's assessment is recorded as a compounding-cost / if-stays entry under the governing finding, not as a counter-finding.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved] | [cascading effect] |

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no fourth outcome. All escape paths: reclassify the P1 to P2 with documented rationale, or accept No-Go. No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. A locked formula without escape closure allows novel escape claims. An escape closure without a locked formula allows formula modification before the check. The pair closes the decision space.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; pos M assessment recorded as compounding-cost entry on pos N's finding] |

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point in the same direction? State the direction. If DIVERGENT: list roles, surfaces, and divergent directions.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
3. Conflict Resolution column populated for every row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are compounding-cost entries.
5. Named invalid forms (untagged, revision, aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## Projected Scorecard — R6 Against v6 Rubric

**Rubric**: v6 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 15

### Essential Criteria (all variations: all PASS, 60 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **60** | **60** | **60** | **60** | **60** |

### Recommended Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | PASS | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | **FAIL** | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **24** | **30** | **30** | **30** | **30** |

Evidence notes:
- C-09 V-01: No phase gate; single-axis isolation design.
- C-07 all: Every variation has a Conflict Analysis section. V-01 has resolution column + authority-position logic. V-02/V-03 have resolution column without judgment-elimination. V-04/V-05 have full conflict section.

### Aspirational Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | FAIL | FAIL | FAIL | **PASS** | **PASS** |
| C-13 Inertia / if-stays framing | FAIL | FAIL | FAIL | **PASS** | **PASS** |
| C-14 Verdict escape closure | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | N/A→PASS |
| C-19 Verdict hardening pair | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | PASS | N/A→PASS |
| C-21 Authority-inertia reconciliation rule | N/A→PASS | N/A→PASS | N/A→PASS | PASS | PASS |
| C-22 Conflict resolution column | PASS | PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | **PASS** | FAIL | **PASS** | **PASS** | **PASS** |
| C-24 Correction-paired invalid form catalog | N/A→PASS | N/A→PASS | N/A→PASS | **PASS** | **PASS** |
| C-25 Co-occurrence coupling label | FAIL | **PASS** | **PASS** | **PASS** | **PASS** |

Evidence notes:

**C-23 V-01**: Resolution column instruction reads "This is derived mechanically from the
authority chain — no judgment required." PASS. The minimal design is sufficient; no priority
table or inertia axis required for C-23 to fire.

**C-23 V-02**: Resolution column reads "pos N governs per authority chain" — no mechanical/
no-judgment statement → FAIL. Single-axis isolation confirms C-23 is independent of C-25.

**C-23 V-03**: Both declarations present; each operates on a distinct section (resolution
column for C-23, Verdict Hardening Pair header for C-25). Confirmed independent composition.

**C-25 V-01**: No "Verdict Hardening Pair" section header; verdict formula is inline → FAIL.
C-25 requires the coupling label when the co-occurrence dependency is present. V-01 has C-11
and C-14 both relevant, no label → FAIL.

**C-25 V-02**: "Verdict Hardening Pair" section header declares C-11 + C-14 as a named
structural unit → PASS. C-14 remains PARTIAL (no "No other escape path exists") — C-25
tests labeling only, not completeness of C-14 itself. Confirmed independent of C-14 PASS.

**C-14 V-02/V-03**: "There is no fourth outcome. Reclassify any P1 or accept No-Go." Names
the escape paths but does not add the exclusion statement "No other escape path exists" →
PARTIAL. The exclusion statement is what forecloses novel escape claims.

**C-14 V-04/V-05**: "No other escape path exists. A P1 + Go claim is invalid under this
formula." → PASS. The explicit exclusion statement is present.

**C-18/C-20 V-05**: The Authority-Inertia Governance section declares 2 axes. Conflict
resolution is embedded in the Authority Chain section — it is an output mechanism of the
authority chain axis, not a separate governance axis. N = 2 < 3. C-18 and C-20 are N/A→PASS.
V-05 achieves 100/100 without triggering C-18 or C-20 as active criteria.

**C-21 V-05**: The Authority-Inertia Governance section contains "Reconciliation rule:
[later-authority role] if-stays projections describe the compounding cost — not a
reclassification." Explicit reconciliation declaration → PASS, even though inertia is not
declared as a separate axis in a priority table.

**C-24 V-01/V-02/V-03**: No named invalid forms → C-12 FAIL → C-24 N/A→PASS (C-12 gates
whether forms are named at all).

**C-24 V-04/V-05**: Three named forms (Untagged, Revision, Aggregate), each with correction
instruction (add tag / record as if-stays / split into rows) → PASS.

### Aspirational Score Summary

| Variation | PASS (PARTIAL=0.5) | Aspirational pts |
|-----------|---------------------|-----------------|
| V-01 | 10.0 + 1.0 = **11.0** | **7.33** |
| V-02 | 10.0 + 1.0 = **11.0** | **7.33** |
| V-03 | 11.0 + 1.0 = **12.0** | **8.00** |
| V-04 | 15.0 + 0 = **15.0** | **10.00** |
| V-05 | 15.0 + 0 = **15.0** | **10.00** |

V-01 pass detail: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22,
C-23, C-24(N/A) = 10; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13, C-25 = 3×0 → 11.0

V-02 pass detail: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22,
C-24(N/A), C-25 = 10; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13, C-23 = 3×0 → 11.0

V-03 pass detail: PASS: C-11, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21(N/A), C-22,
C-23, C-24(N/A), C-25 = 11; PARTIAL: C-14, C-19 = 2×0.5; FAIL: C-12, C-13 = 2×0 → 12.0

V-04 pass detail: All 15 PASS — C-18 fires (3-axis table) → PASS. → 15.0
V-05 pass detail: All 15 PASS — C-18 N/A→PASS (2-axis), C-20 N/A→PASS. → 15.0

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 24 | 7.33 | **91.33** |
| V-02 | 60 | 30 | 7.33 | **97.33** |
| V-03 | 60 | 30 | 8.00 | **98.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

---

## Round Summary

**Key findings from R6:**

1. **C-23 is independent of complexity** — V-01 confirms that "derived mechanically from the
   authority chain — no judgment required" achieves C-23 PASS in a minimal single-axis design
   with no phase gate, inertia, or coupling label. C-23 is purely a phrasing element in the
   Resolution column instruction. It can be backported to any design that has a conflict
   section.

2. **C-25 is independent of C-14 completeness** — V-02 confirms that "Verdict Hardening Pair"
   as a section header achieves C-25 PASS even when C-14 is PARTIAL. C-25 tests labeling;
   C-19 tests co-occurrence completeness. Labeling the pair without closing C-14 yields
   C-25 PASS but C-19 PARTIAL — they are not equivalent.

3. **100/100 is achievable at 3-axis** — V-04 confirms that the 3-axis priority table
   (authority chain / inertia / conflict resolution) is sufficient to achieve 100/100. The
   8-axis design of R5 V-05 was not required.

4. **100/100 is achievable at 2-axis without a priority table** — V-05 confirms that
   embedding conflict resolution in the authority chain section (not declaring it as a
   separate axis) keeps N=2, triggering N/A→PASS for C-18 and C-20. All structural
   elements (hardening pair, correction catalog, escape closure, reconciliation rule) can
   coexist without axis proliferation. This is the minimal 100/100 design.

5. **The two remaining failure modes at mid-complexity** — V-03 still FAILS C-12 and C-13
   (no named invalid forms, no if-stays column). Closing these at mid-complexity would
   require adding the invalid-form catalog and if-stays column, which are present in V-04
   and V-05. The cost of adding them is minimal; the only reason V-03 omits them is to
   isolate the C-23/C-25 hypothesis cleanly.

**R7 direction**: V-04 and V-05 both hit 100/100 via different structural paths (3-axis
with table vs. 2-axis with embedded conflict resolution). R7 would investigate whether
C-13/C-12 can be added to V-03-level designs without introducing axis proliferation — i.e.,
an invalid-form catalog and if-stays column in a 2-axis design without a priority table.
This would determine whether V-05's 2-axis approach is the stable minimal form or whether
it can be simplified further (e.g., removing the explicit Conflict Analysis section and
embedding its logic in the per-role review template).
