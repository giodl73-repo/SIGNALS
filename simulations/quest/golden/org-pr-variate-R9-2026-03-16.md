---
skill: quest-variate
skill_target: org-pr
round: 9
date: 2026-03-16
rubric: org-pr-rubric-v8-2026-03-16.md
---

# org-pr — Round 9 Variations

**Rubric version**: v8 | **N_aspirational**: 19 | **R8 peak**: V-04 = 100.00, V-05 = 100.00

## Round 9 Objectives

R8 confirmed four concurrent 100.00 paths and codified two new criteria (C-28, C-29). Under v8
retroactive scoring: V-04 (single-axis) and V-05 (2-axis + co-located opening) remain 100.00;
V-01/V-02/V-03 drop to 98.95–99.47 due to C-29 FAIL.

R8's Round Summary directed R9 toward minimum *content* testing. The question shifts from
"which governance structures achieve 100.00?" to "how minimal can each passing criterion's
evidence be while still passing?" Three reduction targets were identified:

| Target | Criterion(s) | R8 evidence level | R9 question |
|--------|-------------|-------------------|-------------|
| Invalid-form catalog depth | C-12, C-24 | 3 named forms with corrections | Does 2 named correction-paired forms still pass? |
| Pre-commit self-check depth | C-16 | 6 items | Does a 3-item focused self-check still pass? |
| Phase gate explicitness | C-09 | Dedicated labeled section | Does an inline gate sentence in the opening still pass? |

All R9 variations build on the V-04(R8) architecture (single-axis, standalone Conflict section,
full escape closure) that produced 100.00 in R8. V-05 adds the V-05(R8) co-location pattern
(2-axis, opening-preamble governance declarations, C-29 PASS) to test whether simplifications
compound with the multi-axis path.

## Variation Plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | 2-form invalid catalog (drop Aggregate; retain Untagged + Revision) | C-12/C-24 pass with 2 named correction-paired forms; criteria test pattern presence, not catalog completeness; Aggregate is a formatting concern, not a governance concern |
| V-02 | 3-item pre-commit self-check (verdict formula + conflict column + invalid-form scan) | C-16 passes with 3 focused items covering the highest-risk post-generation gaps; the 3 dropped items are enforced by other structural elements |
| V-03 | Implicit phase gate — halt condition in opening sentence, no labeled Phase Gate section | C-09 passes when gating content (pre-merge condition + halt + alt-path reference) appears in the opening; criterion tests gate content, not section structure |
| V-04 | All three reductions combined (2-form catalog + 3-item self-check + implicit gate) | Simplifications target independent criteria (C-12/C-24, C-16, C-09) with no cross-criterion dependency; if each passes individually, the compound prompt passes all three simultaneously |
| V-05 | V-05(R8) architecture (2-axis + co-located governance) + 2-form catalog + 3-item self-check | The co-location path (C-29 PASS) is compatible with catalog and self-check minimization; neither simplification interacts with C-21/C-23/C-26/C-29; 2-axis minimum-content 100.00 confirmed if individual simplifications pass |

---

## V-01 — 2-Form Invalid Catalog

**Axis**: Invalid-form catalog reduced from 3 named forms to 2; Aggregate dropped; Untagged and
Revision retained
**Hypothesis**: C-12 (Named invalid forms) and C-24 (Correction-paired invalid form catalog) fire
on the presence of named, correction-paired forms — not on an exhaustive enumeration. Untagged
and Revision are the two governance-critical forms: Untagged introduces ungoverned severity
assessments that corrupt the verdict formula; Revision introduces unauthorized upstream overrides
that corrupt the authority chain. Aggregate is a formatting constraint, not a governance failure
mode — its absence does not introduce a decision-path error. If C-12/C-24 require only that
named correction-paired forms be present (minimum 2), this variant scores 100.00. If the
criteria require all three canonical forms to be named, C-12 FAIL + C-24 FAIL → PASS_equiv
17.0/19 → aspirational 8.95 → composite 98.95. If one criterion's pass condition differs from
the other, a single FAIL gives 18.0/19 → aspirational 9.47 → composite 99.47.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

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
5. Named invalid forms (Untagged, Revision) do not appear in any finding row.
6. All role locators valid or self-corrected.

---

## V-02 — 3-Item Pre-Commit Self-Check

**Axis**: Pre-commit self-check reduced from 6 items to 3; retains verdict formula, conflict
resolution column, and invalid-form scan; drops if-stays fill check, upstream-override check,
and locator check
**Hypothesis**: C-16 (Self-correction gate pre-commit) fires on the presence of a post-generation
self-check that covers the highest-risk failure modes. The current 6-item check includes three
redundant items: if-stays projection fill is enforced by the per-role template structure; the
upstream-override prohibition is enforced by the authority chain declaration; role locator
validity is enforced by the locator self-correction gate. The 3-item check targets the three
failures most likely to survive generation without a dedicated check: verdict derivation errors
(wrong formula applied), conflict resolution column gaps (resolution cell left blank), and
invalid-form contamination (Untagged/Revision/Aggregate rows present). If C-16 fires on
focused post-generation coverage, PASS → 100.00. If C-16 requires a minimum of more than 3
items, FAIL → PASS_equiv 18.0/19 → aspirational 9.47 → composite 99.47.

---

You are running /org-pr for: {{topic}}

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

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
3. Named invalid forms (Untagged, Revision, Aggregate) do not appear in any finding row.

---

## V-03 — Implicit Phase Gate

**Axis**: Phase gate embedded in the opening topic line; no dedicated labeled Phase Gate section
**Hypothesis**: C-09 (Phase/lifecycle gating) fires on the presence of a gating condition that
prevents out-of-lifecycle execution — not on a labeled section heading. An inline halt instruction
at the prompt opening that declares the pre-merge requirement and names the alternative skill
(/org-review) satisfies the same governance function as a dedicated phase gate section. The three
gate elements (pre-merge condition, halt instruction, alternative path) are all present; they are
structurally consolidated rather than sectioned. If C-09 fires on gate content, PASS → 100.00.
If C-09 requires a labeled section structure, FAIL → recommended 24 → composite 94.00 at best.
This is the highest-risk variation in R9: C-09 is a recommended criterion (6 pt cost on FAIL vs
0.53 pt aspirational cost). The hypothesis is that C-09 tests gating content, not section form.

---

You are running /org-pr for: {{topic}}. This skill runs before merge only — if the PR has
already merged, halt and use /org-review instead.

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

## V-04 — All Three Reductions Combined

**Axis**: 2-form catalog + 3-item self-check + implicit gate; single-axis minimum-content design
**Hypothesis**: The three content reductions target independent criteria (C-12/C-24, C-16, C-09)
with no cross-criterion dependency. C-09 is a recommended criterion; C-12, C-16, C-24 are
aspirational. A FAIL on C-09 costs 6 pts from recommended; a FAIL on a single aspirational
criterion costs 0.53 pts. If V-01 establishes 2-form catalog passes C-12/C-24, V-02 establishes
3-item self-check passes C-16, and V-03 establishes implicit gate passes C-09, then V-04 passes
all three simultaneously and reaches 100.00. This is the minimum-content 100.00 candidate for
single-axis: fewest named invalid forms, fewest self-check items, most implicit phase gate
framing, with all essential and recommended criteria satisfied. Compound failure scenarios:
C-09 FAIL = 94.00 floor; C-12+C-24 FAIL only = 98.95; C-16 FAIL only = 99.47.

---

You are running /org-pr for: {{topic}}. This skill runs before merge only — if the PR has
already merged, halt and use /org-review instead.

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

## V-05 — 2-Axis + Co-Location + 2-Form Catalog + 3-Item Self-Check

**Axis**: V-05(R8) co-location architecture (2-axis, opening-preamble governance) + catalog
reduction (3 forms → 2: drop Aggregate) + self-check reduction (6 items → 3)
**Hypothesis**: The 2-axis co-location path from R8 V-05 (100.00 under v8) is compatible with
catalog and self-check simplifications. R8 V-05 established that placing both the axis count
declaration ("two governance axes") and the judgment-elimination declaration ("no judgment
required") in a single opening block satisfies C-29 PASS. Neither the catalog nor the self-check
interacts with C-21, C-23, C-26, or C-29. If the catalog reduction passes C-12/C-24 and the
self-check reduction passes C-16, V-05 reaches 100.00 via the 2-axis path. This confirms that
teams choosing multi-axis governance do not face a content premium: the same simplifications
available to single-axis designs are available at 2-axis scale. Note: the explicit phase gate
section is retained in V-05 to isolate the axis-co-location test from the gate-structure test
(V-03/V-04). V-05 tests catalog + self-check simplifications at 2-axis scale only.

---

You are running /org-pr for: {{topic}}

This prompt operates under two governance axes: authority chain (governs review order and
conflict resolution) and inertia framing (governs if-stays projection content in findings).
When they appear to conflict, the conflict resolves mechanically from the authority chain —
no judgment required. The lower-position role governs. A later-authority role may add
if-stays projections on upstream-covered surfaces as compounding-cost entries only; the
upstream finding remains at its declared severity and is not reclassified.

### Phase Gate

**PRE-MERGE gate — this skill runs before merge only.**

If PR is open and not yet merged: continue. If PR has already merged: halt — "org-pr is a
pre-merge skill; post-merge scope has changed; use /org-review instead."

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
1. Verdict follows the Verdict Hardening Pair formula; no escape path used outside the declared set.
2. Conflict Resolution column populated for every conflict row; resolution uses authority-position logic.
3. Named invalid forms (Untagged, Revision) do not appear in any finding row.

---

## Projected Scorecard — R9 Against v8 Rubric

**Rubric**: v8 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 19

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
| C-09 Phase/lifecycle gating | PASS | PASS | **PASS or FAIL** | **PASS or FAIL** | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30** | **30** | **30 or 24** | **30 or 24** | **30** |

Evidence notes:

**C-09 V-01/V-02/V-05**: Dedicated "### Phase Gate" section with explicit PRE-MERGE label,
halt instruction, and /org-review alternative. PASS — consistent with all prior rounds.

**C-09 V-03/V-04 — investigation target**: Gate condition appears in the opening topic line:
"This skill runs before merge only — if the PR has already merged, halt and use /org-review
instead." All three gate elements are present: (1) lifecycle condition (before merge only),
(2) halt instruction ("halt"), (3) alternative path reference (/org-review). The hypothesis
is that C-09 fires on gate content, not section structure. PASS or FAIL depending on whether
the criterion requires a labeled section. **Note**: C-09 is recommended (6 pt cost on FAIL
vs 0.53 pt aspirational cost); a FAIL drops the composite floor to 94.00.

**C-07 all**: All five variations include a standalone Conflict Analysis section with a
populated resolution column. PASS.

### Aspirational Criteria (10 pts, N=19)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | **PASS or FAIL** | PASS | PASS | **PASS or FAIL** | **PASS or FAIL** |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PASS | PASS | PASS | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | **PASS or FAIL** | PASS | **PASS or FAIL** | **PASS or FAIL** |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A | N/A | N/A | N/A | N/A |
| C-19 Verdict hardening pair | PASS | PASS | PASS | PASS | PASS |
| C-20 Priority table | N/A | N/A | N/A | N/A | N/A |
| C-21 Authority-inertia reconciliation rule | N/A | N/A | N/A | N/A | PASS |
| C-22 Conflict resolution column | PASS | PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | **PASS or FAIL** | PASS | PASS | **PASS or FAIL** | **PASS or FAIL** |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | N/A | N/A | N/A | N/A | PASS |
| C-27 Priority axis non-redundancy | N/A | N/A | N/A | N/A | N/A |
| C-28 Distributed conflict table completeness | N/A | N/A | N/A | N/A | N/A |
| C-29 Governance declaration co-location | N/A | N/A | N/A | N/A | PASS |

**All N/A entries count as PASS_equiv = 1.0.**

### Evidence Notes — Investigation Targets

**C-12 V-01/V-04/V-05 — investigation target**: The invalid-form catalog contains 2 named
forms (Untagged, Revision) instead of 3. The rubric criterion name "Named invalid forms"
does not specify a minimum count. The two retained forms are governance-critical: Untagged
corrupts the verdict formula (ungoverned severity); Revision corrupts the authority chain
(unauthorized upstream override). Aggregate prevents formatting confusion but does not
introduce a decision-path error in the absence of the named prohibition. If C-12 requires
named forms to be present (count unspecified) → PASS. If C-12 requires the canonical
three-form catalog established over multiple rounds → FAIL.

**C-16 V-02/V-04/V-05 — investigation target**: The self-check contains 3 items (verdict
formula, conflict resolution column, invalid-form scan) instead of 6. The removed items are:
(1) finding row completeness (if-stays fill) — covered by per-role template; (2) upstream
override prohibition — covered by authority chain declaration; (3) role locator validity —
covered by locator self-correction gate. The 3 retained items address the three failure modes
most likely to survive generation: wrong verdict formula applied, conflict resolution cell
omitted, named-form row present. If C-16 fires on post-generation coverage quality →
PASS. If C-16 requires a minimum item count above 3 → FAIL.

**C-24 V-01/V-04/V-05 — investigation target**: Same catalog scope as C-12 test (2 forms
with corrections). C-24 tests that each named form includes a correction instruction. V-01/
V-04/V-05 retain correction pairing for both forms (Untagged → "add P1/P2/P3 tag before
including"; Revision → "record as if-stays projection instead"). Pairing quality is unchanged;
count is reduced. If C-24 fires on pairing quality for named forms (count unspecified) →
PASS. If C-24 requires an exhaustive catalog of all canonical forms → FAIL. C-12 and C-24
are likely to co-resolve: both PASS or both FAIL.

**C-14 all**: "No other escape path exists. A P1 + Go claim is invalid under this formula."
Explicit exclusion statement present in all five variations. PASS.

**C-19 all**: Both formula lock and escape closure present and labeled "must co-occur" / "Both
must be satisfied simultaneously." PASS.

**C-21 V-01/V-02/V-03/V-04**: Single-axis designs; no axis declaration; no reconciliation
rule needed. If-stays column is a format feature, not a declared governance axis. N/A→PASS.

**C-21 V-05**: Opening block declares "two governance axes: authority chain [...] and inertia
framing [...]" plus a reconciliation rule. Inertia is a declared governance axis. PASS.

**C-23 V-01/V-02/V-03/V-04**: Phrase "derived mechanically from the authority chain, no
judgment required" appears in the standalone Conflict Analysis section's resolution column
instruction. PASS — consistent with confirmed V-03/V-04 pattern from R8.

**C-23 V-05**: Phrase "no judgment required" appears in the opening governance block only
("the conflict resolves mechanically from the authority chain — no judgment required"). The
resolution column instruction says only "The role with the lower authority position number
governs. The higher-position role's assessment is recorded as a compounding-cost / if-stays
entry, not a counter-finding." — no judgment-elimination phrase in the resolution column.
PASS — C-23 confirmed as a content criterion (phrase in conflict-resolution governance
context) by R8 V-05. Opening-only placement is sufficient.

**C-26 V-01/V-02/V-03/V-04**: Single-axis designs. No axis count declaration present.
N/A→PASS.

**C-26 V-05**: "This prompt operates under two governance axes" — explicit integer count
declared. PASS.

**C-27 all**: No priority table in any variation. N/A→PASS.

**C-28 all**: All five variations use a centralized standalone Conflict Analysis section.
No per-role conflict sub-tables. C-28 N/A→PASS for all.

**C-29 V-01/V-02/V-03/V-04**: C-26 is N/A (single-axis). Only one governance declaration
present (judgment-elimination in the resolution column). No co-location requirement applies
to a single-declaration prompt. N/A→PASS.

**C-29 V-05**: Opening block contains both "two governance axes" (axis count declaration,
C-26 PASS) and "no judgment required" (judgment-elimination declaration, C-23 PASS) in the
same preamble paragraph before any operational content. Both declarations co-located at prompt
entry point. PASS — consistent with R8 V-05 confirmed pattern.

### PASS_equiv Calculation

**Single-axis base (V-01, V-02, V-03, V-04) — baseline without investigation criteria**:
- Definitely PASS/N/A: C-11, C-13, C-14, C-15, C-17, C-18(N/A), C-19, C-20(N/A), C-21(N/A),
  C-22, C-23, C-25, C-26(N/A), C-27(N/A), C-28(N/A), C-29(N/A) = 16 criteria full-weight
- Investigation criteria per variation: C-09 (recommended), C-12, C-16, C-24 (aspirational)

**V-05 base — baseline without investigation criteria**:
- Definitely PASS/N/A: same 16 + C-21(PASS) + C-26(PASS) + C-29(PASS) = 19 criteria, minus
  investigation criteria C-12, C-16, C-24 = 16 definite full-weight

| Variation | Investigation criteria | Best (all pass) PASS_equiv | Aspirational pts | Composite |
|-----------|----------------------|---------------------------|-----------------|-----------|
| V-01 | C-12, C-24 | 19.0 | 10.00 | **100.00** |
| V-01 | C-12 or C-24 FAIL | 18.0 | 9.47 | **99.47** |
| V-01 | C-12 + C-24 FAIL | 17.0 | 8.95 | **98.95** |
| V-02 | C-16 | 19.0 | 10.00 | **100.00** |
| V-02 | C-16 FAIL | 18.0 | 9.47 | **99.47** |
| V-03 | C-09 (recommended) | 19.0 | 10.00 | **100.00** |
| V-03 | C-09 FAIL | 19.0 | 10.00 | **94.00** |
| V-04 | C-09, C-12, C-16, C-24 | 19.0 | 10.00 | **100.00** |
| V-04 | C-09 FAIL only | 19.0 | 10.00 | **94.00** |
| V-04 | C-12+C-24 FAIL only | 17.0 | 8.95 | **98.95** |
| V-04 | C-16 FAIL only | 18.0 | 9.47 | **99.47** |
| V-05 | C-12, C-16, C-24 | 19.0 | 10.00 | **100.00** |
| V-05 | C-12 or C-24 FAIL | 18.0 | 9.47 | **99.47** |
| V-05 | C-12 + C-24 FAIL | 17.0 | 8.95 | **98.95** |
| V-05 | C-16 FAIL | 18.0 | 9.47 | **99.47** |

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
| V-01 | C-12 + C-24 FAIL | 98.95 |
| V-02 | C-16 FAIL | 99.47 |
| V-03 | C-09 FAIL (recommended) | **94.00** — highest risk variation |
| V-04 | C-09 FAIL + C-12 + C-24 FAIL | 88.42 — compound floor |
| V-05 | C-12 + C-24 FAIL | 98.95 |

---

## Round Summary

**Key investigation structure for R9**:

1. **C-12/C-24 minimum catalog size** — V-01, V-04, V-05 each test whether 2 named
   correction-paired forms (Untagged + Revision) satisfy the named-invalid-form criteria.
   Aggregate omitted on the grounds that it is a formatting concern, not a decision-path
   governance failure. If PASS, the minimum catalog is 2 forms. If FAIL, the canonical 3 are
   required. C-12 and C-24 will likely co-resolve (the catalog and the pairing test the same
   evidence; a catalog of 2 satisfies both, or violates both).

2. **C-16 minimum self-check depth** — V-02, V-04, V-05 test whether 3 self-check items
   covering verdict, conflict resolution, and invalid forms satisfy C-16. The removed items
   are enforced by other structural elements (template, authority chain, locator gate). If PASS,
   the minimum depth is 3 focused items. If FAIL, coverage breadth above 3 is required.

3. **C-09 gate structure independence** — V-03 and V-04 are the highest-risk variations: they
   test whether C-09 fires on gate content alone, without a labeled section. A FAIL costs 6 pts
   from recommended (vs 0.53 pts for a single aspirational FAIL). If PASS, phase gate
   placement is structure-agnostic. If FAIL, a labeled section is load-bearing for C-09.

4. **2-axis compatibility with simplifications** — V-05 establishes whether catalog and
   self-check reductions compound cleanly with the 2-axis co-location path (V-05 from R8).
   Since C-29 fires on opening-preamble co-location independently of catalog or self-check
   content, the hypothesis is that V-05 inherits whatever C-12/C-16/C-24 outcomes V-01/V-02
   establish. No premium for choosing the 2-axis path.

**R10 direction** (conditional on R9 outcomes):
- If C-09 PASS for implicit gate: investigate whether the halt instruction can be reduced
  further (e.g., no /org-review reference, just "halt") — minimum gate content test.
- If C-12/C-24 PASS for 2-form catalog: investigate whether 1 named form (Untagged only,
  the highest-governance form) satisfies the criteria — absolute minimum catalog test.
- If C-16 PASS for 3-item self-check: test whether 2 items (verdict + conflict column,
  dropping invalid-form scan) retain PASS — absolute minimum check depth test.
- If any simplification FAILS: R10 should re-examine the failure criterion's definition for
  the minimum passing evidence that is just above the FAIL threshold.
