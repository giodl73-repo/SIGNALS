---
skill: quest-variate
skill_target: org-pr
round: 7
date: 2026-03-16
rubric: org-pr-rubric-v7-2026-03-16.md
---

# org-pr — Round 7 Variations

**Rubric version**: v7 | **N_aspirational**: 17 | **R6 V-04 retroactive**: 99.41 | **R6 V-05 retroactive**: 100.00

## Round 7 Objectives

R6 confirmed: (a) 100/100 is achievable at 3-axis with a priority table (V-04), and (b) 100/100
is achievable at 2-axis without a priority table (V-05). v7 adds C-26 (explicit axis count) and
C-27 (priority axis non-redundancy). R6 V-04 drops to 99.41 under v7 due to C-26 FAIL. R6 V-05
holds at 100.00 (C-26 PASS from opening declaration + C-27 N/A from no priority table).

R7 investigates two structural questions and one new-criterion question:

| Objective | Criterion | Status entering R7 |
|-----------|-----------|-------------------|
| C-12 + C-13 at V-03-level complexity (no priority table) | C-12, C-13 | FAIL in V-01–V-03 R6; PASS only in V-04/V-05 |
| Embedded conflict (no standalone section) preserves C-22/C-23 | C-22, C-23 | Untested: C-22 requires conflict table; C-23 requires phrase in resolution column |
| C-26 composes cleanly at 2-axis mid-complexity | C-26 | FAIL in all R6 except V-05 (2-axis declaration) |
| C-26 at 3-axis (V-04 R6 + explicit count) restores 100/100 | C-26, C-27 | V-04 R6 was C-26 FAIL; adding declaration + confirming C-27 PASS targets 100.00 |
| C-21 fires vs. N/A depending on inertia axis declaration | C-21 | N/A in V-01–V-03 R6 (no inertia axis); PASS in V-04/V-05 (inertia declared) |

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-12 + C-13 at V-03 complexity, no C-26 | Adding invalid-form catalog + if-stays column to a V-03-level design (phase gate + authority chain, no priority table) achieves C-12/C-13 PASS without axis proliferation; C-26 FAIL (no declaration); C-14/C-19 PARTIAL (no escape closure) |
| V-02 | V-01 + C-26 + C-21 reconciliation | Adding "two governance axes" declaration + reconciliation rule to V-01 achieves C-26 PASS + C-21 PASS; cost: inertia now declared as axis (not N/A) so C-21 must fire via explicit rule |
| V-03 | Conflict embedded in per-role template, C-26 PASS | Remove standalone Conflict Analysis section; embed conflict resolution logic in Authority Chain section and per-role instructions; hypothesis: C-22 FAIL (no table) breaks this path; C-23 PASS (phrase survives in embedded form) |
| V-04 | V-03 + escape closure | V-03 + full C-14 escape closure; tests whether the embedded-conflict path can reach 99.41 — same as V-02 but via structural embedding rather than standalone section |
| V-05 | R6 V-04 + C-26 explicit count | R6 V-04 (3-axis priority table, 100.00 under v6) + "This prompt operates under three governance axes." declaration; C-26 PASS + C-27 PASS (axes non-redundant) restores 100.00 under v7 |

---

## V-01 — C-12 + C-13 at V-03 Complexity (No Axis Count Declaration)

**Axis**: C-12 (named invalid forms) + C-13 (if-stays framing) added to V-03-level design
**Hypothesis**: Adding an invalid-form catalog (with correction instructions) and an If-Stays
Projection column to a V-03-level prompt (phase gate + authority chain + standalone conflict
section) achieves C-12/C-13 PASS without needing a priority table or explicit axis count
declaration. Expected delta over R6 V-03 retroactive under v7 (97.65): +1.18 pts (C-12/C-13
PASS). C-14/C-19 remain PARTIAL (no escape closure). C-26 FAIL (no axis count).

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.craft/roles/`, then include.

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

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; pos M assessment recorded as compounding-cost entry on pos N's finding] |

**Resolution column rule**: The role with the lower position number governs. This is derived
mechanically from the authority chain — no judgment required. The higher-position role's
assessment is not a counter-finding; it is a compounding-cost entry under the governing finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no modification path used.
3. Conflict Resolution column populated for every row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-02 — V-01 + C-26 Explicit Axis Count + C-21 Reconciliation Rule

**Axis**: V-01 + "two governance axes" declaration + authority-inertia reconciliation rule
**Hypothesis**: Adding an explicit axis count declaration and a reconciliation rule to V-01
achieves C-26 PASS + C-21 PASS. The cost: inertia framing is now a declared governance axis
(not just an if-stays column feature), which means C-21 must fire as PASS via an explicit
reconciliation rule rather than N/A. Expected composite: 99.41 (+0.59 over V-01). The
reconciliation rule does not require a priority table — it can live in the opening section as
in R6 V-05.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces already
covered by earlier-authority findings. Those projections describe the compounding cost of the
upstream finding going unresolved — not a reclassification. The upstream finding remains at
its declared severity; the if-stays projection is a compounding-cost entry, not a counter-finding.

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.craft/roles/`, then include.

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

### Conflict Analysis

When roles hold incompatible assessments on the same surface:

| Surface | Role A (pos N) | Role B (pos M) | Resolution |
|---------|---------------|---------------|------------|
| [surface] | [assessment] | [assessment] | [pos N governs — derived mechanically from the authority chain, no judgment required; pos M assessment recorded as compounding-cost entry on pos N's finding] |

**Resolution column rule**: The role with the lower position number governs. This is derived
mechanically from the authority chain — no judgment required. The higher-position role's
assessment is not a counter-finding; it is a compounding-cost entry under the governing finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Every finding row has severity + if-stays projection filled.
2. Verdict follows the Verdict Hardening Pair formula; no modification path used.
3. Conflict Resolution column populated for every row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces are
   compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-03 — Conflict Embedded in Per-Role Template (No Standalone Conflict Section)

**Axis**: Remove standalone Conflict Analysis section; embed conflict resolution in Authority
Chain section and per-role review instructions; C-26 PASS via opening declaration
**Hypothesis**: Embedding conflict resolution logic directly into per-role review instructions
(rather than a standalone Conflict Analysis section with a table) preserves C-23 PASS (phrase
survives in embedded form) but loses C-22 PASS (no conflict table → C-22 FAIL). The C-26 PASS
exactly offsets the C-22 FAIL, leaving the composite equal to V-01 (98.82). The investigation
question: is C-22 tied to table format or to resolution logic presence?

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces already
covered by earlier-authority findings. Those projections describe the compounding cost of the
upstream finding going unresolved — not a reclassification. The upstream finding remains at
its declared severity; the if-stays projection is a compounding-cost entry, not a counter-finding.

### Phase Gate

**PRE-MERGE only.** Execute before the PR is merged to the target branch.

If the PR has already merged: halt — "org-pr is a pre-merge skill; use org-review for post-merge."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.craft/roles/`, then include.

### Role Selection

From the PR diff, identify roles by changed file surface area. List each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

**Conflict resolution (embedded)**: When your assessment as a later-authority role conflicts
with an earlier-authority finding on the same surface, do not issue a counter-finding. Derive
resolution mechanically from the authority chain — no judgment required. The lower-position
role governs. Record your position as a compounding-cost entry in the If-Stays Projection column
of the governing finding's row.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved; conflicts from later-authority roles recorded here] | [cascading effect] |

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
3. No counter-findings from later-authority roles; conflicts recorded as compounding-cost entries
   in the governing finding's If-Stays Projection column.
4. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
5. All role locators valid or self-corrected.

---

## V-04 — V-03 + Escape Closure (Embedded Conflict + Full C-14)

**Axis**: V-03 structure (embedded conflict, C-26 PASS, C-21 PASS) + full escape closure
**Hypothesis**: Adding full C-14 escape closure ("No other escape path exists") to the
embedded-conflict design achieves C-14/C-19 PASS. Expected composite: 99.41 — same ceiling
as V-02, reached via a structurally different path (no standalone Conflict section vs.
standalone section present). This tests whether C-22 FAIL is a permanent cap on the
embedded-conflict path or whether it can be offset by other criteria gains. Since C-22 FAIL
costs 0.59 pts and the cap without it is 100.00 (V-05), the embedded path caps at 99.41.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, authority chain governs.

**Reconciliation rule**: A later-authority role may add if-stays projections to surfaces already
covered by earlier-authority findings. Those projections describe the compounding cost of the
upstream finding going unresolved — not a reclassification. The upstream finding remains at
its declared severity; the if-stays projection is a compounding-cost entry, not a counter-finding.

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.craft/roles/`, then include.

### Role Selection

From the PR diff, select roles by changed file surface area. State each selected role, its
authority position, and the files that triggered selection.

### Authority Chain

Review order: Security (1) → Compliance (2) → Architect (3) → Performance (4) → Testing (5) → UX (6).

Earlier positions hold higher authority. Later roles:
- May issue new findings on surfaces not covered by earlier roles.
- May add if-stays projections on upstream-covered surfaces — as compounding cost entries only.
- May not revise, reclassify, or override upstream findings.

**Conflict resolution (embedded)**: When your assessment as a later-authority role conflicts
with an earlier-authority finding on the same surface, derive resolution mechanically from the
authority chain — no judgment required. The lower-position role governs. Record your position
as a compounding-cost entry in the If-Stays Projection column of the governing finding's row,
not as a counter-finding.

### Per-Role Review (authority-chain order)

**[Role Name]** | Authority position: [N] | Selected because: [files]

Named invalid finding forms (do not use):
- **Untagged** (no severity label) — invalid; add P1/P2/P3 tag before including.
- **Revision** (changing an upstream role's severity) — invalid; record as if-stays projection instead.
- **Aggregate** (combining two distinct surfaces in one row) — invalid; split into separate rows.

| Finding | Severity | If-Stays Projection | Downstream Risk |
|---------|----------|---------------------|-----------------|
| [text] | P1/P2/P3 | [compounding cost if not resolved; conflicts from later-authority roles recorded here] | [cascading effect] |

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
2. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
3. No counter-findings from later-authority roles; conflicts recorded as compounding-cost entries
   in the governing finding's If-Stays Projection column.
4. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
5. All role locators valid or self-corrected.

---

## V-05 — R6 V-04 + C-26 Explicit Count (3-Axis, Restores 100.00 Under v7)

**Axis**: R6 V-04 design (3-axis priority table, all 15 criteria PASS) + "three governance axes"
declaration in the Axis Composition Table opening
**Hypothesis**: Adding an explicit axis count declaration ("This prompt operates under three
governance axes") to R6 V-04 achieves C-26 PASS. The 3-axis table (authority chain / inertia
framing / conflict resolution column) satisfies C-27 PASS because all three axes are
structurally distinct: authority chain governs propagation direction, inertia governs finding
content, and conflict resolution column governs the output logic of the conflict table. None is
derivable from the other. Expected composite: 100.00, restoring R6 V-04's score under v7 by
closing the C-26 gap with a single phrase addition.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill. Post-merge scope has changed; use /org-review instead."

### Axis Composition Table

This prompt operates under three governance axes. When axes produce conflicting instructions,
this table governs:

| Axis | Governs | Yields To |
|------|---------|-----------|
| Authority chain | Review order; conflict resolution; constraint propagation | Nothing (highest priority) |
| Inertia framing | Finding content (if-stays projections) | Authority chain |
| Conflict resolution column | Conflict table output (Resolution field logic) | Authority chain |

**Tiebreaker default**: authority chain governs when any two axes conflict.

### Authority-Inertia Reconciliation Rule

Inertia framing (if-stays projections) is required for all findings. When a later-authority
role adds an if-stays projection to a surface already covered by an earlier-authority finding,
that projection describes the **compounding cost** of the upstream finding going unresolved —
not a reclassification. The upstream finding remains at its declared severity; the if-stays
projection is recorded as a downstream risk entry, not a counter-finding.

### Role Loading

Read `.craft/roles/`. Valid locator: file exists + `name:` non-empty.

**Locator self-correction gate**: If valid → include. If invalid → rewrite to the most specific
anchor in `.craft/roles/`, then include.

### Role Selection

From the PR diff, select roles by changed file surface area. State each selected role, its
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

Both must be satisfied simultaneously. Formula lock without escape closure allows novel escape
claims. Escape closure without formula lock allows formula modification before the escape check.
The pair closes the decision space completely.

Composite derivation:
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
3. Conflict Resolution column populated for every row with authority-position logic.
4. No later-authority finding overrides an upstream finding; if-stays on upstream surfaces
   are compounding-cost entries.
5. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## Projected Scorecard — R7 Against v7 Rubric

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
- C-07 all variations: V-01/V-02 have standalone Conflict Analysis section + resolution column.
  V-03/V-04 embed conflict resolution in Authority Chain section — conflict resolution logic is
  present and explicit; C-07 tests presence of resolution mechanism, not table format. PASS for
  all. (C-22 tests table format specifically — see aspirational.)

### Aspirational Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | PASS |
| C-19 Verdict hardening pair | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | PASS |
| C-21 Authority-inertia reconciliation rule | N/A→PASS | **PASS** | **PASS** | **PASS** | PASS |
| C-22 Conflict resolution column | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | PASS | PASS | PASS | PASS | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** |
| C-27 Priority axis non-redundancy | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | **PASS** |

Evidence notes:

**C-12 all variations**: V-01 through V-05 all include the three-form catalog (Untagged /
Revision / Aggregate) with correction instructions in the per-role section. PASS for all.
R7 confirms C-12 fires at V-03 complexity (V-01) — no priority table required.

**C-13 all variations**: V-01 through V-05 all include an If-Stays Projection column in the
per-role finding table. PASS for all. R7 confirms C-13 fires at V-03 complexity (V-01) —
no priority table required. The column need not be paired with an explicit inertia governance
axis for C-13 to fire; the feature fires independently of how the framing is declared.

**C-14 V-01/V-02/V-03**: "There is no fourth outcome. Reclassify any P1 or accept No-Go."
Names both escape paths but does not add the exclusion statement "No other escape path exists" →
PARTIAL. C-14 PARTIAL caps C-19 at PARTIAL for the same variations.

**C-14 V-04/V-05**: "No other escape path exists. A P1 + Go claim is invalid under this
formula." → PASS. The explicit exclusion statement forecloses novel escape claims.

**C-18/C-20 V-01 through V-04**: No priority table present; N/A→PASS for both. V-01 has no
axis declaration. V-02/V-03/V-04 declare 2 axes — below the threshold requiring a table.

**C-18/C-20 V-05**: The 3-axis Axis Composition Table is present → C-18 PASS (axis conflict
resolution rule: "Tiebreaker default: authority chain governs when any two axes conflict") and
C-20 PASS (priority table is the composition mechanism).

**C-21 V-01**: No inertia axis declared; if-stays column is present in the per-role table but
inertia is not a governance axis. No reconciliation rule exists, none needed → N/A→PASS.
The if-stays column alone does not trigger C-21; the governance axis declaration does.

**C-21 V-02/V-03/V-04**: Opening section declares "two governance axes: authority chain and
inertia framing" and includes the reconciliation rule ("compounding cost — not a reclassification").
C-21 fires as PASS rather than N/A because inertia is a declared governance axis. The
reconciliation rule satisfies the explicit requirement.

**C-22 V-01/V-02**: Standalone Conflict Analysis section with a populated resolution column →
PASS. The Resolution column instruction uses the authority-position logic explicitly.

**C-22 V-03/V-04**: No standalone Conflict Analysis section; conflict resolution is embedded in
the Authority Chain section as a procedural instruction. C-22 requires a resolution column in
a conflict table — an embedded procedure does not satisfy this criterion → FAIL. This is the
structural cost of the embedded-conflict path: one criterion permanently capped.

**C-23 V-03/V-04**: The phrase "derived mechanically from the authority chain — no judgment
required" appears in the embedded conflict instruction within the Authority Chain section.
C-23 tests the presence of this phrase, not its location in a column header → PASS. The phrase
survives embedding.

**C-24 all variations**: Three named forms (Untagged, Revision, Aggregate), each with a
correction instruction paired inline. PASS for all.

**C-26 V-01**: No axis count declaration — axis structure must be inferred from sections.
FAIL. Cost: 0.59 pts under v7.

**C-26 V-02/V-03/V-04**: Opening sentence declares "two governance axes" explicitly → PASS.

**C-26 V-05**: Axis Composition Table opens: "This prompt operates under three governance
axes." Explicit count + table + named axes → PASS.

**C-27 V-01 through V-04**: No priority table → N/A→PASS.

**C-27 V-05**: 3-axis table: authority chain (propagation direction) / inertia framing (finding
content) / conflict resolution column (conflict table output logic). Each axis governs a
distinct domain unreachable by the others. Authority chain governs *which* role's finding
survives conflict; conflict resolution column governs *how* the surviving finding is formatted
in the table output; inertia governs *what content* appears in the surviving finding's if-stays
field. None is a subdivision or logical consequence of another → PASS.

### Aspirational Score Summary

| Variation | PASS_equiv (PARTIAL=0.5) | Aspirational pts |
|-----------|--------------------------|-----------------|
| V-01 | 15.0 | **8.82** |
| V-02 | 16.0 | **9.41** |
| V-03 | 15.0 | **8.82** |
| V-04 | 16.0 | **9.41** |
| V-05 | 17.0 | **10.00** |

V-01: PASS: C-11,C-12,C-13,C-15,C-16,C-17,C-18(N/A),C-20(N/A),C-21(N/A),C-22,C-23,C-24,C-25,C-27(N/A)=14;
       PARTIAL: C-14,C-19=2×0.5; FAIL: C-26=0 → 14+1+0=15.0

V-02: PASS: C-11,C-12,C-13,C-15,C-16,C-17,C-18(N/A),C-20(N/A),C-21,C-22,C-23,C-24,C-25,C-26,C-27(N/A)=15;
       PARTIAL: C-14,C-19=2×0.5 → 15+1=16.0

V-03: PASS: C-11,C-12,C-13,C-15,C-16,C-17,C-18(N/A),C-20(N/A),C-21,C-23,C-24,C-25,C-26,C-27(N/A)=14;
       PARTIAL: C-14,C-19=2×0.5; FAIL: C-22=0 → 14+1+0=15.0

V-04: PASS: C-11,C-12,C-13,C-14,C-15,C-16,C-17,C-18(N/A),C-19,C-20(N/A),C-21,C-23,C-24,C-25,C-26,C-27(N/A)=16;
       FAIL: C-22=0 → 16+0=16.0

V-05: All 17 PASS → 17.0

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 30 | 8.82 | **98.82** |
| V-02 | 60 | 30 | 9.41 | **99.41** |
| V-03 | 60 | 30 | 8.82 | **98.82** |
| V-04 | 60 | 30 | 9.41 | **99.41** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

---

## Round Summary

**Key findings from R7:**

1. **C-12 and C-13 fire independently of complexity** — V-01 confirms that the invalid-form
   catalog and if-stays column achieve C-12/C-13 PASS in a V-03-level design with no priority
   table, no inertia governance axis, and no explicit axis count. Both criteria are purely
   content/format features of the per-role review section. They can be backported to any design
   that has a per-role review table.

2. **C-26 is the cheapest remaining gap at mid-complexity** — V-01 → V-02 delta is +0.59 pts
   from a single opening declaration. C-26 is the minimum viable path from 98.82 to 99.41 at
   the V-02/V-04 complexity level. No structural changes required.

3. **Embedded conflict preserves C-23 but breaks C-22** — V-03 confirms that moving conflict
   resolution from a standalone table into per-role instructions keeps C-23 PASS (phrase
   survives) but causes C-22 FAIL (no conflict table). The net effect on PASS_equiv is zero
   when C-26 PASS is present (V-01 vs. V-03 both 15.0; V-02 vs. V-04 both 16.0). The
   embedded path is structurally simpler but not higher-scoring.

4. **The embedded-conflict path caps at 99.41** — V-04 reaches 99.41 with all elements except
   a standalone Conflict Analysis section. C-22 FAIL costs exactly 0.59 pts; there is no other
   criterion that can offset it while keeping the section removed. To reach 100.00, the
   standalone Conflict Analysis section is required.

5. **C-26 backports cleanly to 3-axis designs** — V-05 confirms that adding the explicit axis
   count declaration to R6 V-04 restores 100.00 under v7 with no other changes. C-27 PASS is
   satisfied by the existing 3-axis table (authority chain / inertia / conflict resolution
   column) — all three axes are structurally non-redundant. The C-26 fix is a single-phrase
   addition.

**R8 direction**: Two paths reach 99.41 (V-02: standalone conflict + 2-axis; V-04: embedded
conflict + 2-axis). The 100/100 requirement is a standalone Conflict Analysis section. R8
could investigate: (a) whether C-22 can be satisfied with an inline conflict table embedded
within the per-role review section (a per-role conflict row rather than a global section), and
(b) whether the 2-axis designs (V-02/V-04) can reach 100/100 by adding a standalone Conflict
Analysis table without reintroducing the 3-axis complexity of V-05.
