---
skill: quest-variate
skill_target: org-pr
round: 10
date: 2026-03-16
rubric: org-pr-rubric-v9-2026-03-16.md
---

# org-pr — Round 10 Variations

**Rubric version**: v9 | **N_aspirational**: 22 | **R9 peak**: V-01 through V-05 all projected 100.00

## Round 10 Objectives

R9 confirmed all three minimum-content hypotheses and the rubric codified them in v9:

| Confirmed minimum | Rubric criterion | Codified floor |
|-------------------|-----------------|----------------|
| Inline gate (no labeled section) passes C-09 | C-30 | 3 elements required: lifecycle condition + halt + alternative path reference |
| 2-form invalid catalog passes C-12/C-24 | C-31 | >=2 correction-paired forms; each must address a distinct decision-path governance failure mode |
| 3-item pre-commit self-check passes C-16 | C-32 | >=3 items; absent item types must be covered by named structural redundancy |

The v9 rubric also raised N_aspirational from 19 to 22. Under v9, a single aspirational FAIL
costs 21/22 * 10 = 9.545 pts aspirational → composite 99.545 (vs 99.47 under v8). The added
criteria change the cost curve but not the test questions.

R9 Round Summary directed R10 toward testing the **formulation margin** within each confirmed
floor — not below the floor (which would be known FAILs against v9), but at the minimum
satisfying form of each element. Three new investigation targets:

| Target | Criterion | R9 evidence level | R10 question |
|--------|-----------|-------------------|-------------|
| C-30 element (3) form | C-30 | Full explanatory clause: "halt — org-pr is a pre-merge skill; post-merge scope has changed; use /org-review instead" | Does a parenthetical named reference "(see /org-review)" satisfy element (3), or does the explanatory clause carry load? |
| C-31 failure mode language | C-31 | Parenthetical descriptions: "(no severity label)", "(changing an upstream role's severity)" | Does C-31 require explicit failure mode description language, or does the correction instruction imply the failure mode sufficiently? |
| C-32 structural redundancy form | C-32 | Structural redundancy implicit — the elements exist in the prompt but are not named in the self-check | Does C-32 require the structural element to be explicitly named at the point of redundancy claim, or is the element's existence sufficient? |

Additionally, R10 investigates whether two aspirational criteria that have been N/A in every
prior round can be activated from N/A to explicit PASS:

| Target | Criterion | Prior status | R10 question |
|--------|-----------|-------------|-------------|
| Axis conflict resolution rule | C-18 | N/A every round (no multi-axis conflict rule declared) | Does a 3-axis design with a formal pairwise axis priority declaration activate C-18 from N/A to explicit PASS? |
| Priority table | C-20 | N/A every round (no axis priority table present) | Does an explicit priority table over governance axes satisfy C-20? |

Note: Since N/A counts as PASS_equiv 1.0, activating C-18/C-20 does not improve the
composite score. The investigation value is confirmation that these criteria are achievable
and that activating them does not unintentionally FAIL other criteria.

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-30 minimum alternative path — gate compressed to parenthetical "(see /org-review)" | C-30 element (3) fires on the presence of any named alternative path reference; the explanatory clause is not load-bearing; "(see /org-review)" satisfies the reference requirement |
| V-02 | C-31 terse form definitions — remove parenthetical descriptions; retain form name + correction instruction only | C-31 "addressing a distinct decision-path governance failure mode" fires on the correction instruction's governance function, not on explicit failure mode language; the form name (Untagged, Revision) plus correction instruction implies the failure mode; terse forms satisfy the criterion |
| V-03 | C-32 explicit structural redundancy naming — extend 3-item self-check with named section references for each absent item type | C-32 "named structural redundancy" is more robustly satisfied when absent items are explicitly traced to named structural elements by section label; tests whether explicit naming is required for C-32 PASS or merely sufficient |
| V-04 | V-01 + V-02 + V-03 (compressed gate + terse forms + explicit redundancy naming) | Three modifications target independent criteria (C-30, C-31, C-32) with no cross-criterion dependency; if each passes individually, the compound design passes all three simultaneously |
| V-05 | C-18 + C-20 activation — 3-axis design (authority chain + inertia framing + lifecycle scope) with explicit axis priority table and cross-axis resolution rule | C-18 (Axis conflict resolution rule) and C-20 (Priority table) have been N/A in every round; a 3-axis design with a formal priority table and a cross-axis resolution rule activates both from N/A to PASS; activation must not FAIL any existing criterion |

---

## V-01 — C-30 Minimum Alternative Path Reference

**Axis**: Phase gate compressed to the minimum form that satisfies all three C-30 elements;
alternative path expressed as a parenthetical reference only — no explanatory clause
**Hypothesis**: C-30 requires three content elements: (1) lifecycle condition, (2) halt
instruction, (3) alternative path reference. The R9 gate carried an explanatory clause —
"org-pr is a pre-merge skill; post-merge scope has changed" — that precedes the halt and
the alternative path. This clause explains *why* the halt applies but is not one of the three
required elements. If C-30 fires on element presence alone, the compressed form "Pre-merge
only — halt if already merged (see /org-review)" contains all three elements:
(1) "Pre-merge only" = lifecycle condition;
(2) "halt if already merged" = halt instruction;
(3) "(see /org-review)" = named alternative path reference.
If C-30 PASS → 100.00. If C-30 requires the explanatory clause as part of the halt
instruction or requires the alternative path reference to appear as an imperative clause
(not a parenthetical), FAIL → recommended tier 24 → composite 94.00 floor. This is the
highest-risk single variation in R10 because C-30 is derived from the recommended C-09,
and a FAIL costs 6 pts. The hypothesis is conservative: the parenthetical form names the
skill explicitly, satisfying "alternative path reference."

---

You are running /org-pr for: {{topic}}. Pre-merge only — halt if already merged (see /org-review).

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
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

---

## V-02 — C-31 Terse Form Definitions

**Axis**: Named invalid forms reduced to form name + correction instruction only; parenthetical
descriptions of the failure mode omitted
**Hypothesis**: C-31 (named-invalid-form 2-form floor) requires each named form to "address a
distinct decision-path governance failure mode." The current form definitions carry parenthetical
descriptions: "Untagged (no severity label)" and "Revision (changing an upstream role's
severity)." These parentheticals name the surface manifestation of each failure mode — how the
invalid form appears in the output. The correction instruction names the remediation —
what must be done to fix the failure. If the form name plus correction instruction together
imply the failure mode (Untagged → ungoverned severity → add tag; Revision → unauthorized
override → use if-stays), then the parenthetical description is explanatory but not
definitional. If C-31 fires on the governance function of the form (correction instruction +
distinct class of failure) rather than requiring explicit failure mode language, PASS → 100.00.
If C-31 requires the parenthetical description as evidence that a distinct failure mode was
identified, FAIL → aspirational 21/22 * 10 = 9.545 → composite 99.545. Note: C-31 and C-12
will co-resolve on this axis (both test the same catalog entry; a form without explicit failure
mode description either satisfies both or fails both).

---

You are running /org-pr for: {{topic}}. This skill runs before merge only — if the PR has
already merged, halt and use /org-review instead.

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
- **Untagged** — invalid; add P1/P2/P3 tag before including.
- **Revision** — invalid; record as if-stays projection instead.

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
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

---

## V-03 — C-32 Explicit Structural Redundancy Naming

**Axis**: 3-item self-check retained from R9 V-04; each item type absent from the check is
explicitly traced to the named structural element that covers it
**Hypothesis**: C-32 requires that "any output types absent from the gate are enforced by a
named structural element (template field, authority chain declaration, named gate) elsewhere
in the prompt" and that "implicit coverage does not satisfy the redundancy condition." In R9
V-04, the structural redundancy was present in the prompt (the per-role template, the Authority
Chain prohibition clause, the Locator Self-Correction Gate) but was not named at the
self-check. The rubric text says "named structural redundancy" and explicitly disqualifies
implicit coverage. If this means the structural element must be identified by name *at the
point of the redundancy claim*, then R9 V-04 satisfies C-32 only because the scorer infers
the named elements from the prompt body. V-03 removes that inference requirement by explicitly
naming each structural backstop in the self-check commentary. If C-32 requires explicit naming
at the point of redundancy claim → V-03 is the stronger form; R9 V-04 may have passed on a
generous reading. If C-32 merely requires that named elements exist in the prompt → both V-03
and R9 V-04 satisfy it equally. Either outcome refines the understanding of C-32's pass condition.

---

You are running /org-pr for: {{topic}}. This skill runs before merge only — if the PR has
already merged, halt and use /org-review instead.

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
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

Structural redundancy (absent item types covered by named structural elements):
- Finding-row completeness (if-stays fill): enforced by the per-role table template — "If-Stays
  Projection" is a required column in every role's finding table.
- Upstream-override prohibition: enforced by the Authority Chain section's explicit clause —
  "May not revise, reclassify, or override upstream findings."
- Role locator validity: enforced by the Locator Self-Correction Gate — the named gate in the
  Role Loading section rewrites invalid locators before any role is included.

---

## V-04 — All Three Combined

**Axis**: V-01 + V-02 + V-03 (compressed gate + terse forms + explicit structural redundancy
naming); single-axis minimum-gate + minimum-form-description design with maximal C-32 support
**Hypothesis**: The three modifications target independent criteria (C-30, C-31/C-12, C-32/C-16)
with no cross-criterion dependency. C-30 fires on gate element presence (V-01 tests the minimum
form of element 3). C-31 fires on form governance function (V-02 tests the minimum description
that implies a distinct failure mode). C-32 fires on named structural redundancy (V-03 makes
redundancy naming explicit). If each passes individually in V-01/V-02/V-03, the compound
design passes all three simultaneously. Compound failure: C-30 FAIL = 94.00 floor
(recommended); C-31+C-12 FAIL only = 20/22 * 10 = 9.09 → 99.09; C-32+C-16 FAIL only =
21/22 * 10 = 9.545 → 99.545. The safest element of V-04 is the explicit structural redundancy
(V-03 axis) — if anything, it over-satisfies C-32. The gate compression (V-01 axis) carries
the highest risk.

---

You are running /org-pr for: {{topic}}. Pre-merge only — halt if already merged (see /org-review).

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
- **Untagged** — invalid; add P1/P2/P3 tag before including.
- **Revision** — invalid; record as if-stays projection instead.

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
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

Structural redundancy (absent item types covered by named structural elements):
- Finding-row completeness (if-stays fill): enforced by the per-role table template — "If-Stays
  Projection" is a required column in every role's finding table.
- Upstream-override prohibition: enforced by the Authority Chain section's explicit clause —
  "May not revise, reclassify, or override upstream findings."
- Role locator validity: enforced by the Locator Self-Correction Gate in the Role Loading section.

---

## V-05 — C-18 + C-20 Activation (3-Axis with Priority Table)

**Axis**: 3-axis design (authority chain + inertia framing + lifecycle scope); explicit axis
priority table; cross-axis conflict resolution rule; 2-axis co-location preamble extended to
3-axis; tests C-18 (Axis conflict resolution rule) and C-20 (Priority table) activation from
N/A to PASS
**Hypothesis**: C-18 and C-20 have been N/A in every prior round. C-18 requires an explicit
rule for resolving conflicts between governance axes (not a specific axis pair like
authority-inertia, which satisfies C-21, but a general cross-axis resolution mechanism).
C-20 requires a priority table that orders the governance axes. A 3-axis design with a
formal priority table (Axis 1 governs Axis 2; Axis 2 governs Axis 3 in absence of Axis 1
override) and a named axis conflict resolution rule satisfies both: the table is C-20's
evidence; the rule is C-18's evidence. The hypothesis is that activating C-18/C-20 does not
FAIL any criterion currently passing — the added structure is additive, not conflicting.
V-05 retains all R9 V-05 passing elements (2-axis co-location preamble satisfying C-29,
authority-inertia reconciliation satisfying C-21, governance scope declaration satisfying
C-26) and extends them. Since N/A = PASS_equiv 1.0, activating C-18/C-20 does not change
the composite score; it confirms that these criteria are achievable in the prompt architecture.
Note: V-05 retains the explicit Phase Gate section (not compressed) to isolate gate form
from axis structure — gate compression is already tested in V-01/V-04.

---

You are running /org-pr for: {{topic}}

This prompt operates under three governance axes: authority chain (governs review order and
conflict resolution between roles), inertia framing (governs if-stays projection content in
findings), and lifecycle scope (governs which prompt execution is valid; pre-merge only). When
axes appear to conflict, resolution follows the axis priority table — no judgment required.

**Axis priority table**:

| Priority | Axis | Governs |
|----------|------|---------|
| 1 | Lifecycle scope | Whether this execution is valid; voids output if post-merge |
| 2 | Authority chain | Review order; conflict resolution between roles |
| 3 | Inertia framing | If-stays projection content; compounding-cost entries on upstream surfaces |

**Axis conflict resolution rule**: Higher-priority axis governs unconditionally. Axis 1
(lifecycle scope) voids the entire execution before Axis 2 (authority chain) evaluates.
Axis 2 (authority chain) resolves role-surface conflicts before Axis 3 (inertia framing)
adds if-stays projections. A later-axis claim may not override an earlier-axis determination.

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
| [surface description] | [Role A assessment] | [Role B assessment] | [pos N governs; axis conflict resolution rule applies: authority chain (Axis 2) governs; Role B's position recorded as compounding-cost entry] |

**Resolution column instruction**: The role with the lower authority position number governs,
per the Axis 2 (authority chain) priority. The higher-position role's assessment is recorded
as a compounding-cost / if-stays entry, not a counter-finding.

### Verdict

**Verdict**: [Go | No-Go | Conditional-Go]
**Derivation**: [P1/P2 findings, or "no P1/P2 — Go"]
**Gate**: PRE-MERGE

Pre-commit self-check:
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

---

## Projected Scorecard — R10 Against v9 Rubric

**Rubric**: v9 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 22

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
| C-09 / C-30 Phase/lifecycle gating | **PASS or FAIL** | PASS | PASS | **PASS or FAIL** | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30 or 24** | **30** | **30** | **30 or 24** | **30** |

Evidence notes:

**C-09/C-30 V-01/V-04 — investigation target**: Gate appears in the opening line as:
"Pre-merge only — halt if already merged (see /org-review)." C-30 requires three elements:
(1) lifecycle condition — "Pre-merge only" PASS; (2) halt instruction — "halt if already
merged" PASS; (3) alternative path reference — "(see /org-review)" is a named skill reference
in parenthetical form. The investigation question is whether a parenthetical reference satisfies
element (3) or whether element (3) requires an imperative clause form ("use /org-review
instead"). C-30's wording says "alternative path reference" — a reference, not an imperative.
If the form of the reference (parenthetical vs imperative) is not load-bearing, PASS. If a
parenthetical is not a sufficiently explicit reference for a lifecycle gate, FAIL → 24 pts.

**C-09/C-30 V-02/V-03/V-05**: Full PRE-MERGE gate section or full halt clause with
imperative "use /org-review instead." All three elements clearly present. PASS.

### Aspirational Criteria (10 pts, N=22)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | **PASS or FAIL** | PASS | **PASS or FAIL** | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PASS | PASS | PASS | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A | N/A | N/A | N/A | **PASS or N/A** |
| C-19 Verdict hardening pair | PASS | PASS | PASS | PASS | PASS |
| C-20 Priority table | N/A | N/A | N/A | N/A | **PASS or N/A** |
| C-21 Authority-inertia reconciliation rule | N/A | N/A | N/A | N/A | PASS |
| C-22 Conflict resolution column | PASS | PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | PASS | **PASS or FAIL** | PASS | **PASS or FAIL** | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | N/A | N/A | N/A | N/A | PASS |
| C-27 Priority axis non-redundancy | N/A | N/A | N/A | N/A | **PASS or N/A** |
| C-28 Distributed conflict table completeness | N/A | N/A | N/A | N/A | N/A |
| C-29 Governance declaration co-location | N/A | N/A | N/A | N/A | PASS |
| C-30 Gate content sufficiency | PASS | PASS | PASS | PASS | PASS |
| C-31 Named-invalid-form 2-form floor | PASS | **PASS or FAIL** | PASS | **PASS or FAIL** | PASS |
| C-32 Self-correction gate 3-item floor | PASS | PASS | PASS | PASS | PASS |

**All N/A entries count as PASS_equiv = 1.0.**

### Evidence Notes — Investigation Targets

**C-12/C-24/C-31 V-02/V-04 — investigation target**: The named invalid form entries are
"Untagged — invalid; add P1/P2/P3 tag before including" and "Revision — invalid; record as
if-stays projection instead." Parenthetical descriptions are absent. C-31 requires each
retained form to "address a distinct decision-path governance failure mode." The form names
carry semantics (Untagged = without a tag; Revision = an unauthorized change), and the
correction instructions imply the governance concern (add tag = the tag was missing and the
severity ungoverned; use if-stays = the upstream finding must not be reclassified). If C-31
fires on the form's *function* — the correction instruction's governance implication — PASS.
If C-31 requires explicit failure mode language in the form definition itself, FAIL.
C-12 (Named invalid forms) and C-24 (Correction-paired catalog) will co-resolve with C-31:
all three test the same catalog evidence. Either all PASS or all FAIL together.

**C-18 V-05 — investigation target**: The opening preamble declares an explicit axis conflict
resolution rule: "When axes appear to conflict, resolution follows the axis priority table —
no judgment required" and "Higher-priority axis governs unconditionally." This is a named,
general cross-axis resolution rule, not a specific axis-pair reconciliation (C-21 covers
authority-inertia specifically). C-18 is labeled "Axis conflict resolution rule" — if it
fires on the presence of a named rule governing axis conflict resolution (as opposed to a
specific axis pair), PASS. If C-18 requires a specific form (e.g., a resolution ordering
that covers all declared axis pairs in a table), the priority table satisfies this — PASS.
If C-18 is satisfied only by single-axis designs that include a rule (not N/A), the criterion
definition would need to specify what qualifies. The hypothesis is that C-18 PASS.

**C-20 V-05 — investigation target**: An explicit priority table is present:

> | Priority | Axis | Governs |
> |----------|------|---------|
> | 1 | Lifecycle scope | ... |
> | 2 | Authority chain | ... |
> | 3 | Inertia framing | ... |

This is a formatted priority table over the three declared governance axes. C-20 is labeled
"Priority table" — if it fires on the presence of a priority table over governance axes,
PASS. If C-20 requires a specific form (e.g., a severity weight table for findings rather
than a governance axis priority table), then the criterion may fire on a different evidence
type. The hypothesis is that C-20 PASS given the table's form and purpose.

**C-27 V-05 — note**: C-27 is "Priority axis non-redundancy." If C-18 and C-20 activate from
N/A to PASS in V-05, C-27 may also become testable. A 3-axis priority table with distinct
axes (lifecycle, authority, inertia) that each cover non-overlapping surfaces satisfies
non-redundancy. N/A if C-27 applies only when C-20 is present — in that case V-05's C-20
PASS would activate C-27 as well. Conservative estimate: N/A→PASS (distinct axes, no
overlapping coverage).

**C-16/C-32 V-03/V-04**: The 3-item self-check is retained. The explicit structural redundancy
block names each absent item type and identifies the structural element covering it by section
label. This is stronger evidence for C-32's "named structural redundancy" condition than the
implicit form in R9 V-04. PASS in both cases; V-03/V-04 establish the explicit naming form as
the canonical C-32 evidence pattern.

**C-23 V-01/V-02/V-03/V-04**: Phrase "derived mechanically from the authority chain, no judgment
required" in the Conflict Analysis resolution column instruction. PASS.

**C-23 V-05**: "No judgment required" appears in the opening preamble's axis conflict
resolution rule. PASS — confirmed co-location pattern from R9 V-05.

**C-29 V-05**: Opening preamble contains axis count ("three governance axes"), axis conflict
resolution rule, and axis priority table before any operational content. All governance
declarations co-located at prompt entry point. PASS.

### PASS_equiv Calculation

**Single-axis base (V-01/V-02/V-03/V-04) — N_aspirational = 22**:
- Definite PASS/N/A: C-11, C-13, C-14, C-15, C-16, C-17, C-18(N/A), C-19, C-20(N/A), C-21(N/A),
  C-22, C-23, C-25, C-26(N/A), C-27(N/A), C-28(N/A), C-29(N/A), C-30, C-32 = 19 criteria
- C-09 recommended (V-01/V-04): investigation target
- C-12, C-24, C-31 (V-02/V-04): investigation target

| Variation | Investigation criteria | Best (all pass) PASS_equiv | Aspirational pts | Composite |
|-----------|----------------------|---------------------------|-----------------|-----------|
| V-01 | C-09 (recommended) | 22.0 | 10.00 | **100.00** |
| V-01 | C-09 FAIL | 22.0 | 10.00 | **94.00** |
| V-02 | C-12, C-24, C-31 | 22.0 | 10.00 | **100.00** |
| V-02 | C-12+C-24+C-31 FAIL (co-resolve) | 19.0 | 8.636 | **98.636** |
| V-02 | C-31 FAIL (C-12/C-24 PASS) | 21.0 | 9.545 | **99.545** |
| V-03 | (no investigation target) | 22.0 | 10.00 | **100.00** |
| V-04 | C-09 (recommended), C-12, C-24, C-31 | 22.0 | 10.00 | **100.00** |
| V-04 | C-09 FAIL + C-12+C-24+C-31 FAIL | 19.0 | 8.636 | **88.636** |
| V-05 | C-18, C-20, C-27 | 22.0 | 10.00 | **100.00** |
| V-05 | C-18 FAIL | 21.0 | 9.545 | **99.545** |
| V-05 | C-20 FAIL | 21.0 | 9.545 | **99.545** |

### Composite Score Summary

Expected scores (best-case):

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 30 | 10.00 | **100.00** |
| V-02 | 60 | 30 | 10.00 | **100.00** |
| V-03 | 60 | 30 | 10.00 | **100.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

Risk-adjusted composite floor per variation:

| Variation | Risk scenario | Composite floor |
|-----------|--------------|-----------------|
| V-01 | C-09 FAIL (recommended) | **94.00** — highest risk |
| V-02 | C-12+C-24+C-31 all FAIL (co-resolve) | 98.636 |
| V-03 | (no investigation target) | **100.00** — no risk |
| V-04 | C-09 FAIL + C-12+C-24+C-31 FAIL | 88.636 — compound floor |
| V-05 | C-18+C-20 FAIL (both) | 98.182 |

---

## Round Summary

**Key investigation structure for R10**:

1. **C-30 parenthetical alternative path (V-01, V-04)**: The most compressed gate form
   tested to date — all three elements present in one clause, element (3) as a parenthetical
   named reference. If PASS, the minimum C-30-satisfying alternative path form is a named
   parenthetical. If FAIL, an imperative clause form is required. This is the highest-risk
   axis because C-09/C-30 is recommended (6 pt cost on FAIL).

2. **C-31/C-12/C-24 terse form definitions (V-02, V-04)**: Parenthetical failure mode
   descriptions dropped from named invalid forms. If PASS, C-31 fires on correction
   instruction governance function alone; the form name + correction is sufficient to address
   a distinct failure mode. If FAIL, explicit failure mode language in the form body is
   load-bearing. All three criteria (C-12, C-24, C-31) will co-resolve — they test the same
   catalog evidence from different angles.

3. **C-32 explicit structural redundancy naming (V-03)**: The structural redundancy block
   explicitly names each structural element that covers absent self-check items. V-03 has no
   investigation target — it is projected 100.00 under all scenarios. It establishes whether
   explicit naming improves C-32 robustness or is merely equivalent to implicit presence.
   If the rubric scorer treats V-03 and R9 V-04 identically for C-32, the naming is sufficient
   but not required. If V-03 scores higher, explicit naming is required by C-32's "named
   structural redundancy" condition.

4. **C-18/C-20 activation (V-05)**: First test of whether previously unreachable criteria
   can be activated in the org-pr architecture. The 3-axis design with priority table does not
   improve the composite score (N/A = PASS_equiv 1.0) but confirms whether C-18 and C-20 are
   achievable. If PASS, these criteria are archivable as optional architecture signals for
   complex multi-axis designs. If FAIL, the criteria require a form not yet explored.

**R11 direction** (conditional on R10 outcomes):

- If C-30 PASS for parenthetical reference (V-01): investigate the absolute minimum
  alternative path form — e.g., just the skill name with no verb: "Pre-merge — halt if merged
  (/org-review)" — to confirm that a bare named reference satisfies element (3).
- If C-30 FAIL for parenthetical (V-01): establish that an imperative clause is required;
  test the shortest imperative form that satisfies element (3).
- If C-31/C-12/C-24 PASS for terse forms (V-02): codify the minimum passing form — form name
  + correction instruction, no failure mode description. Investigate whether even the form name
  can be dropped (correction instruction only) or whether the named anchor is load-bearing.
- If C-31/C-12/C-24 FAIL for terse forms (V-02): establish that the parenthetical description
  is load-bearing; test whether the description can be shortened to a single word per form.
- If C-18/C-20 PASS (V-05): codify that 3-axis designs unlock these criteria; document the
  minimum axis count and priority table form required. Test whether a 2-axis design with a
  priority table (instead of authority-inertia reconciliation rule alone) activates C-20.
- If C-18/C-20 FAIL (V-05): re-examine criterion definitions to identify what evidence type
  each criterion was originally designed to capture.
