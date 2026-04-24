---
skill: quest-variate
skill_target: org-pr
round: 8
date: 2026-03-16
rubric: org-pr-rubric-v7-2026-03-16.md
---

# org-pr — Round 8 Variations

**Rubric version**: v7 | **N_aspirational**: 17 | **R7 peak**: V-05 = 100.00

## Round 8 Objectives

R7 established two structural findings that define R8's scope:

1. **The embedded-conflict path caps at 99.41** — C-22 FAIL costs 0.59 pts when conflict
   resolution is embedded as a *procedure*. The cost persists even with escape closure (R7
   V-04). The path to 100.00 has required a standalone Conflict Analysis section in every
   round.

2. **The 2-axis path has not been tested with escape closure** — R7 V-02 (2-axis + standalone
   Conflict section) reached 99.41 with C-14 PARTIAL. Adding escape closure to the 2-axis
   design has not been attempted; the maximum 2-axis score is unknown.

R8 investigates four open questions:

| Objective | Criterion | Status entering R8 |
|-----------|-----------|-------------------|
| Does a per-role conflict sub-table (inline, conditional table) satisfy C-22? | C-22 | Untested: prior C-22 FAIL was embedded *procedure*, not embedded *table*; criterion says "conflict table with resolution column" |
| Can the 2-axis design reach 100.00 by adding escape closure? | C-14, C-19 | R7 V-02 = 99.41 with C-14 PARTIAL; escape closure not yet added at 2-axis |
| Is single-axis + standalone Conflict section + escape closure a valid 100.00 path? | C-21, C-26, C-27 | Untested: all three are N/A→PASS at single-axis; no reconciliation rule needed; C-26 N/A when only one axis |
| Can C-23 fire from the opening reconciliation rule alone (not the resolution column)? | C-23 | Untested: C-23 phrase has always appeared in the resolution column instruction; location sensitivity unknown |

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Per-role conflict sub-table, 2-axis, no escape closure | A per-role conflict table (conditional, inline per role) satisfies C-22 PASS; C-14 PARTIAL → 99.41 if C-22 PASS, 98.82 if C-22 FAIL |
| V-02 | V-01 + escape closure | C-22 PASS from per-role table + C-14 PASS → 100.00 on the embedded-conflict path; first 100.00 without a standalone global Conflict Analysis section |
| V-03 | 2-axis + standalone Conflict section + escape closure (no priority table) | 2-axis design reaches 100.00; escape closure is the sole missing piece from R7 V-02; no priority table needed |
| V-04 | Single-axis + standalone Conflict section + escape closure | Single-axis achieves 100.00; C-21/C-26/C-27 all N/A→PASS; minimum governance complexity for 100.00 |
| V-05 | V-03 + C-23 phrase in opening only (not in resolution column) | C-23 fires from the opening reconciliation rule when it includes "no judgment required"; resolution column says only "pos M governs"; tests C-23 location sensitivity |

---

## V-01 — Per-Role Conflict Sub-Table (2-Axis, No Escape Closure)

**Axis**: Per-role inline conflict sub-table; 2-axis declaration; no escape closure
**Hypothesis**: Adding a conditional conflict sub-table within each per-role review block —
structured as a table with a resolution column, not a prose instruction — satisfies C-22 PASS
without requiring a global standalone Conflict Analysis section. The sub-table includes the
authority-position resolution logic and the judgment-elimination phrase. Expected score:
99.41 if C-22 PASS (PASS_equiv 16.0), 98.82 if C-22 FAIL (PASS_equiv 15.0). C-14 PARTIAL
(two escape paths named, no explicit exclusion statement) caps C-19 at PARTIAL for both
outcomes.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces
already covered by earlier-authority findings. Those projections describe the compounding cost
of the upstream finding going unresolved — not a reclassification. The upstream finding remains
at its declared severity; the if-stays projection is a compounding-cost entry, not a
counter-finding.

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

**Conflicts with upstream roles** (include only when this role's assessment is incompatible
with an earlier-authority finding on the same surface):

| Surface | This Role's Assessment | Upstream Role (pos M) Assessment | Resolution |
|---------|------------------------|----------------------------------|------------|
| [surface] | [this role's position] | [Role M's position] | [pos M governs — derived mechanically from the authority chain, no judgment required; this role's position recorded as compounding-cost entry under Role M's finding] |

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding = No-Go. This formula is not editable, no exceptions.

2. **Outcome set**: The complete verdict set is: Go, Conditional-Go, No-Go. There is no fourth
   outcome. Reclassify any P1 or accept No-Go.

Both must be satisfied simultaneously.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point
in the same direction? State direction. If DIVERGENT: list roles, surfaces, divergent directions.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no modification path used.
3. Per-role conflict sub-table populated for each role that has upstream conflicts; resolution
   column uses authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-02 — Per-Role Conflict Sub-Table + Escape Closure

**Axis**: V-01 + full escape closure ("No other escape path exists")
**Hypothesis**: If the per-role conflict sub-table satisfies C-22 PASS (V-01 hypothesis), adding
the explicit escape closure achieves C-14 PASS and C-19 PASS simultaneously. Combined with
C-22 PASS, all 17 aspirational criteria reach PASS or N/A→PASS: PASS_equiv 17.0 →
aspirational 10.00 → composite 100.00. This would be the first 100.00 achieved without a
global standalone Conflict Analysis section. If C-22 FAIL (per-role table insufficient),
escape closure alone cannot compensate: PASS_equiv 16.0 → 99.41.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces
already covered by earlier-authority findings. Those projections describe the compounding cost
of the upstream finding going unresolved — not a reclassification. The upstream finding remains
at its declared severity; the if-stays projection is a compounding-cost entry, not a
counter-finding.

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

**Conflicts with upstream roles** (include only when this role's assessment is incompatible
with an earlier-authority finding on the same surface):

| Surface | This Role's Assessment | Upstream Role (pos M) Assessment | Resolution |
|---------|------------------------|----------------------------------|------------|
| [surface] | [this role's position] | [Role M's position] | [pos M governs — derived mechanically from the authority chain, no judgment required; this role's position recorded as compounding-cost entry under Role M's finding] |

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no
   fourth outcome. All escape paths:
   - Reclassify the P1 to P2 with documented rationale; formula re-evaluates with new severity.
   - Accept No-Go and record.
   No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. A locked formula without escape closure allows novel
escape claims. An escape closure without a locked formula allows formula modification before
the check. The pair closes the decision space.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point
in the same direction? State the direction explicitly. If DIVERGENT: list roles, surfaces, and
divergent projection directions.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the
   declared set.
3. Per-role conflict sub-table populated for each role that has upstream conflicts; resolution
   column uses authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-03 — 2-Axis + Standalone Conflict Section + Escape Closure (No Priority Table)

**Axis**: R7 V-02 structure (2-axis, standalone Conflict section, C-26 PASS) + escape closure
**Hypothesis**: R7 V-02 reached 99.41 with C-14 PARTIAL. Adding full escape closure ("No other
escape path exists") achieves C-14 PASS and C-19 PASS. All other criteria carry forward from
R7 V-02 as PASS or N/A→PASS. Expected: PASS_equiv 17.0 → aspirational 10.00 → composite
100.00. This is the minimum-structure 100.00 path: 2-axis, no priority table, standalone
Conflict section, escape closure. C-18/C-20/C-27 all N/A→PASS because no priority table.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces
already covered by earlier-authority findings. Those projections describe the compounding cost
of the upstream finding going unresolved — not a reclassification. The upstream finding remains
at its declared severity; the if-stays projection is a compounding-cost entry, not a
counter-finding.

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no
   fourth outcome. All escape paths:
   - Reclassify the P1 to P2 with documented rationale; formula re-evaluates with new severity.
   - Accept No-Go and record.
   No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. A locked formula without escape closure allows novel
escape claims. An escape closure without a locked formula allows formula modification before
the check. The pair closes the decision space.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point
in the same direction? State the direction explicitly. If DIVERGENT: list roles, surfaces, and
divergent projection directions.

### Conflict Analysis

When two or more roles hold incompatible assessments of the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; Role B's position recorded as compounding-cost entry on Role A's finding row] |

**Resolution column instruction**: The role with the lower authority position number governs.
This is derived mechanically from the authority chain — no judgment required. The
higher-position role's assessment is recorded as a compounding-cost / if-stays entry, not
a counter-finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the
   declared set.
3. Conflict Resolution column populated for every conflict row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-04 — Single-Axis + Standalone Conflict Section + Escape Closure

**Axis**: Authority chain as sole governance axis; no inertia axis; no axis declaration; full
escape closure; standalone Conflict Analysis section
**Hypothesis**: A single-axis design does not need an axis count declaration (C-26 N/A→PASS),
a reconciliation rule (C-21 N/A→PASS), or a priority table (C-18/C-20/C-27 all N/A→PASS).
The if-stays column is a structural feature of the per-role review template, not a declared
governance axis. With escape closure and a standalone Conflict Analysis section, all 17
criteria reach PASS or N/A→PASS: PASS_equiv 17.0 → 100.00. This is the minimum governance
complexity path to 100.00 — one axis, no priority table, no reconciliation rule required.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no
   fourth outcome. All escape paths:
   - Reclassify the P1 to P2 with documented rationale; formula re-evaluates with new severity.
   - Accept No-Go and record.
   No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. A locked formula without escape closure allows novel
escape claims. An escape closure without a locked formula allows formula modification before
the check. The pair closes the decision space.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point
in the same direction? State the direction explicitly. If DIVERGENT: list roles, surfaces, and
divergent projection directions.

### Conflict Analysis

When two or more roles hold incompatible assessments of the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; Role B's position recorded as compounding-cost entry on Role A's finding row] |

**Resolution column instruction**: The role with the lower authority position number governs.
This is derived mechanically from the authority chain — no judgment required. The
higher-position role's assessment is recorded as a compounding-cost / if-stays entry, not
a counter-finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the
   declared set.
3. Conflict Resolution column populated for every conflict row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-05 — V-03 with C-23 in Opening Reconciliation Rule Only

**Axis**: V-03 structure (2-axis, standalone Conflict section, escape closure) + judgment-
elimination phrase relocated to opening reconciliation rule only; resolution column omits
the phrase
**Hypothesis**: C-23 fires when the phrase "no judgment required" appears in the opening
reconciliation rule in the context of conflict resolution, even if the conflict table's
Resolution column instruction omits it. If C-23 is location-independent (fires at any
occurrence in the conflict-resolution context), this variant scores 100.00. If C-23
specifically requires the phrase in the Resolution column instruction, this variant scores
99.41 (C-23 FAIL costs 0.59 pts). The distinction resolves whether C-23 is a structural
criterion (phrase must appear in the resolution output mechanism) or a content criterion
(phrase must appear anywhere the conflict resolution process is described).

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces
already covered by earlier-authority findings. When a later-authority role's assessment
conflicts with an earlier-authority finding on the same surface, the conflict resolves
mechanically from the authority chain — no judgment required. The lower-position role governs.
The higher-position role's position is recorded as a compounding-cost entry in the governing
finding's If-Stays Projection column, not as a counter-finding.

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

### Role Loading

Read `.roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved before merge] | [cascading effect] |

### Verdict Hardening Pair

Two properties that must co-occur:

1. **Formula lock**: Any P1 finding from any role = No-Go. Not editable. No exceptions.

2. **Escape closure**: The complete verdict set is {Go, Conditional-Go, No-Go}. There is no
   fourth outcome. All escape paths:
   - Reclassify the P1 to P2 with documented rationale; formula re-evaluates with new severity.
   - Accept No-Go and record.
   No other escape path exists. A P1 + Go claim is invalid under this formula.

Both must be satisfied simultaneously. A locked formula without escape closure allows novel
escape claims. An escape closure without a locked formula allows formula modification before
the check. The pair closes the decision space.

Composite:
- P1 → No-Go
- All P2 (no P1) → Conditional-Go
- All P3 (no P1/P2) → Go

### Consensus Analysis

**Projection convergence call**: ALIGNED or DIVERGENT — do all roles' if-stays projections point
in the same direction? State the direction explicitly. If DIVERGENT: list roles, surfaces, and
divergent projection directions.

### Conflict Analysis

When two or more roles hold incompatible assessments of the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs; Role B's position recorded as compounding-cost entry on Role A's finding row] |

**Resolution column instruction**: The role with the lower authority position number governs.
The higher-position role's assessment is recorded as a compounding-cost / if-stays entry, not
a counter-finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the
   declared set.
3. Conflict Resolution column populated for every conflict row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## Projected Scorecard — R8 Against v7 Rubric

**Rubric**: v7 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 17

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
| C-09 Phase/lifecycle gating | PASS | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30** | **30** | **30** | **30** | **30** |

Evidence notes:
- C-07 all variations: conflict resolution mechanism is present in all five. V-01/V-02 use
  per-role conflict sub-tables (conditional, inline). V-03/V-04/V-05 use standalone Conflict
  Analysis sections. C-07 tests presence of resolution mechanism, not its structural form →
  PASS for all.

### Aspirational Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PARTIAL | **PASS** | **PASS** | **PASS** | **PASS** |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS |
| C-19 Verdict hardening pair | PARTIAL | **PASS** | **PASS** | **PASS** | **PASS** |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS |
| C-21 Authority-inertia reconciliation rule | PASS | PASS | PASS | N/A→PASS | PASS |
| C-22 Conflict resolution column | **PASS or FAIL** | **PASS or FAIL** | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | **PASS or FAIL** |
| C-24 Correction-paired invalid form catalog | PASS | PASS | PASS | PASS | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | PASS | PASS | PASS | N/A→PASS | PASS |
| C-27 Priority axis non-redundancy | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS |

Evidence notes:

**C-14 V-01**: "There is no fourth outcome. Reclassify any P1 or accept No-Go." Names both
escape paths but omits the exclusion statement "No other escape path exists" → PARTIAL. C-14
PARTIAL caps C-19 at PARTIAL.

**C-14 V-02 through V-05**: "No other escape path exists. A P1 + Go claim is invalid under
this formula." → PASS. Explicit exclusion statement forecloses novel escape claims.

**C-18 all variations**: No priority table present in any variation → N/A→PASS for all.

**C-20 all variations**: No priority table present → N/A→PASS for all.

**C-21 V-01/V-02/V-03**: Opening section declares "two governance axes: authority chain and
inertia framing" and includes reconciliation rule. C-21 fires as PASS. Inertia is a declared
governance axis.

**C-21 V-04**: No axis declaration; inertia is not a declared governance axis (if-stays is a
column feature only). No reconciliation rule present or needed → N/A→PASS.

**C-21 V-05**: Opening section declares two axes and includes "the conflict resolves
mechanically from the authority chain — no judgment required" as part of the reconciliation
rule. Inertia is a declared governance axis → C-21 PASS.

**C-22 V-01/V-02**: The per-role conflict sub-table includes a Resolution column with the
authority-position logic. The rubric defines C-22 as requiring "a resolution column in a
conflict table." A per-role sub-table is structurally a table with a resolution column —
not an embedded procedure (the R7 V-03/V-04 failure mode). **Investigation target**: does
C-22 require a global standalone section, or does any conflict table with a resolution column
qualify? If the criterion fires on structural presence (table + resolution column), C-22 PASS.
If it requires a dedicated standalone section, C-22 FAIL. Recorded as PASS or FAIL pending
scoring determination.

**C-22 V-03/V-04/V-05**: Standalone Conflict Analysis section with populated 4-column table
including Resolution column → PASS. Consistent with all prior rounds where standalone section
= C-22 PASS.

**C-23 V-01 through V-04**: The phrase "derived mechanically from the authority chain, no
judgment required" appears in the conflict table's resolution instruction. V-01/V-02: in the
per-role conflict sub-table resolution column ("pos M governs — derived mechanically from the
authority chain, no judgment required"). V-03/V-04: in the standalone Conflict Analysis
resolution column instruction. → PASS for all.

**C-23 V-05**: The phrase "no judgment required" appears in the opening reconciliation rule
only: "the conflict resolves mechanically from the authority chain — no judgment required."
The standalone Conflict Analysis Resolution column says only "pos N governs; Role B's position
recorded as compounding-cost entry" — no judgment-elimination phrase. **Investigation target**:
does C-23 fire when the phrase appears in the opening reconciliation rule but not in the
resolution column? If location-independent, PASS. If the criterion specifically fires from
the resolution column context, FAIL (costs 0.59 pts → composite 99.41).

**C-25 all variations**: "Both must be satisfied simultaneously" phrase present in V-01
through V-05. PASS for all. V-02 through V-05 additionally include the co-occurrence
explanation ("A locked formula without escape closure allows novel escape claims..."), which
reinforces C-25 PASS but is not required.

**C-26 V-01/V-02/V-03/V-05**: Opening sentence declares "two governance axes" explicitly →
PASS. Single sentence sufficient per R7 confirmation.

**C-26 V-04**: No axis declaration — single-axis design. C-26 states "N/A if only one axis is
present — no declaration is needed for single-axis prompts (counts as PASS)" → N/A→PASS. V-04
has no opening axis declaration by design; authority chain is the sole governance mechanism.

**C-27 all variations**: No priority table present in any variation → N/A→PASS for all.

### Aspirational Score Summary

| Variation | Scenario | PASS_equiv | Aspirational pts |
|-----------|----------|------------|-----------------|
| V-01 | C-22 PASS | 16.0 | **9.41** |
| V-01 | C-22 FAIL | 15.0 | **8.82** |
| V-02 | C-22 PASS | 17.0 | **10.00** |
| V-02 | C-22 FAIL | 16.0 | **9.41** |
| V-03 | — | 17.0 | **10.00** |
| V-04 | — | 17.0 | **10.00** |
| V-05 | C-23 PASS | 17.0 | **10.00** |
| V-05 | C-23 FAIL | 16.0 | **9.41** |

PASS_equiv detail:

V-01 (C-22 PASS): PASS/N/A=15 (C-11,12,13,15,16,17,C-18,C-20,C-21,C-22,C-23,C-24,C-25,C-26,C-27 all N/A); PARTIAL: C-14,C-19=1.0 → 16.0
V-01 (C-22 FAIL): PASS/N/A=14 (C-22 excluded); PARTIAL: C-14,C-19=1.0 → 15.0
V-02 (C-22 PASS): all 17 PASS/N/A → 17.0
V-02 (C-22 FAIL): 16 PASS/N/A (C-22 excluded) → 16.0
V-03: all 17 PASS/N/A → 17.0
V-04: all 17 PASS/N/A (C-21 N/A, C-26 N/A) → 17.0
V-05 (C-23 PASS): all 17 PASS/N/A → 17.0
V-05 (C-23 FAIL): 16 PASS/N/A (C-23 excluded) → 16.0

### Composite Score Summary

| Variation | Scenario | Essential | Recommended | Aspirational | **Composite** |
|-----------|----------|-----------|-------------|--------------|---------------|
| V-01 | C-22 PASS | 60 | 30 | 9.41 | **99.41** |
| V-01 | C-22 FAIL | 60 | 30 | 8.82 | **98.82** |
| V-02 | C-22 PASS | 60 | 30 | 10.00 | **100.00** |
| V-02 | C-22 FAIL | 60 | 30 | 9.41 | **99.41** |
| V-03 | — | 60 | 30 | 10.00 | **100.00** |
| V-04 | — | 60 | 30 | 10.00 | **100.00** |
| V-05 | C-23 PASS | 60 | 30 | 10.00 | **100.00** |
| V-05 | C-23 FAIL | 60 | 30 | 9.41 | **99.41** |

---

## Round Summary

**Key findings from R8** (projected; outcomes for V-01, V-02, V-05 depend on scoring
determinations for C-22 and C-23 location sensitivity):

1. **C-22 location sensitivity is the central R8 question** — V-01 and V-02 test whether a
   per-role conflict sub-table (conditional, inline within each role's review block) satisfies
   C-22. The criterion text requires "a resolution column in a conflict table." The R7 failure
   mode was an embedded *procedure* — a prose instruction without table structure. The per-role
   sub-table is structurally a table. If C-22 fires on structural presence alone, V-01 = 99.41
   and V-02 = 100.00. If C-22 requires a global standalone section, both drop 0.59 pts.

2. **The 2-axis path to 100.00 is confirmed if C-22 is location-independent** — V-03 adds the
   single missing piece from R7 V-02 (escape closure) and reaches 100.00 without requiring a
   priority table or explicit axis composition table. The full R7 V-05 structure (3-axis +
   Axis Composition Table) is not the minimum path; it is one of at least three valid paths
   (V-03, V-04, and V-05 from R7).

3. **Single-axis is a valid 100.00 path** — V-04 confirms that a prompt with no axis
   declaration, no reconciliation rule, and no priority table achieves 100.00 via the N/A→PASS
   mechanism for C-21, C-26, and C-27. The if-stays column satisfies C-13 as a format feature
   independent of governance axis declaration. Single-axis is the minimum-complexity 100.00
   design if all other structural elements (standalone Conflict section, escape closure,
   invalid-form catalog) are present.

4. **C-23 location sensitivity resolves the phrase's authority** — V-05 isolates whether the
   judgment-elimination phrase must appear in the Resolution column of the conflict table, or
   whether its presence in the opening reconciliation rule is sufficient. If C-23 fires from
   any conflict-resolution context, V-05 = 100.00. If C-23 requires the phrase specifically
   in the resolution output mechanism (the column), V-05 = 99.41. The result would constrain
   future prompt designs: opening-only placement of the phrase cannot guarantee C-23 PASS.

5. **R9 direction**: If V-04 (single-axis) reaches 100.00, R9 should investigate whether
   single-axis designs can be further simplified — can the invalid-form catalog (C-12, C-24)
   be reduced from 3 named forms to 2 without affecting PASS? Can the pre-commit self-check
   (C-16) be reduced to fewer items while keeping the criterion? Can the phase gate (C-09)
   survive a more implicit framing? These would test the minimum *content* within each
   criterion, not the minimum *count* of criteria.
