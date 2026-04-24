Looking at the scorecard, I need to identify what C-17 and C-18 represent from their score patterns before writing the new criteria.

**C-17 pattern**: PARTIAL in V-01 (phrasing register), FAIL in V-02/V-03, PARTIAL in V-04 (role sequence), PARTIAL in V-05 (integration). The three variations that partially achieve it share one thing: they impose structure on *which roles speak in what order and why* — but none formalize the authority chain with rationale.

**C-18 pattern**: FAIL in V-01–V-04, PARTIAL only in V-05. V-05's note is "structural overcrowding risk." The only variation that even attempts C-18 is the one combining multiple axes — suggesting C-18 is about resolving conflicts *between* axes when they're composed together.

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 4
supersedes: org-pr-rubric-v3-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v3 -> v4)

Added two aspirational criteria extracted from R3 inferred excellence signals. Both were
observed as PARTIAL in the R3 scorecard under labels "C-17 (pre-v3, inferred)" and
"C-18 (pre-v3, inferred)" and are now formally defined.

- **C-17** (role authority sequence declaration): The three variations that scored PARTIAL
  — V-01 (phrasing register), V-04 (role sequence + lifecycle), V-05 (full integration) —
  all impose structure on review order but none declare *why* that order carries authority.
  The excellence signal is an explicit ordering rationale: roles that own blocking concerns
  (security, schema) are sequenced before advisory roles (DX, docs), and the prompt states
  the ordering principle. V-02/V-03 fail entirely: V-02 uses per-role headings with no
  sequence logic; V-03's inertia framing is role-agnostic. A prompt that names the order
  without naming the authority principle scores PARTIAL; one that declares both scores PASS.

- **C-18** (axis conflict resolution rule): Only V-05 scores PARTIAL, and only because it
  combines multiple axes (phrasing register + inertia framing + role sequence + lifecycle).
  The gap identified is "structural overcrowding risk" — when axes are composed, their
  instructions can contradict each other (e.g., property declaration form vs. inertia
  framing produce different sentence structures for the same finding). An explicit axis
  priority rule — stating which instruction wins when two axes conflict — prevents the model
  from blending registers in unpredictable ways. Single-axis prompts (V-01 through V-04)
  cannot exhibit this pattern; V-05 reaches PARTIAL because it attempts composition but
  omits the conflict rule. PASS requires an explicit "if X axis conflicts with Y axis, apply
  X" statement or equivalent tiebreaker.

Aspirational pool grows from N=8 to N=10. No changes to essential or recommended tiers.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Multi-role coverage | coverage | 2+ labeled sections from defined role set, each with a finding |
| C-02 | P1/P2/P3 on every finding | correctness | Zero untagged findings |
| C-03 | File-based role selection rationale | correctness | Each role's inclusion tied to specific changed files |
| C-04 | Explicit go/no-go recommendation | correctness | Labeled verdict block, derivable from findings |
| C-05 | Per-role structure / no bleeding | format | Each section opens with role-name heading; sections cannot bleed |

---

## Recommended Criteria (weight: 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Projection-aware consensus | correctness | Consensus section explicitly checks whether downstream/inertia projections across roles agree or diverge — not only immediate findings |
| C-07 | Conflict analysis | correctness | At least one cross-role conflict identified and its resolution path stated |
| C-08 | Locator self-correction gate | format | LOCATOR RULES block (or equivalent) includes an explicit rewrite-before-commit instruction, not only a column header |
| C-09 | Phase / lifecycle gating | correctness | Phase context (e.g., pre-merge, post-deploy) governs finding severity; at least one finding references phase |
| C-10 | Downstream risk field | coverage | At least one finding includes a downstream impact field distinct from the finding body |

---

## Aspirational Criteria (weight: 10 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-11 | Formula lock declaration | correctness | Prompt or output declares the go/no-go rule as a fixed property, not a heuristic ("this formula is not editable") |
| C-12 | Named invalid forms | format | Prompt names at least two invalid output forms by example (not just by description) |
| C-13 | Inertia / if-stays-in framing | correctness | At least one role section frames the finding as "if this stays in" rather than only "this is wrong" |
| C-14 | Verdict escape closure | correctness | Verdict block includes an escape-hatch closer: states there is no third choice and provides a reclassify-or-accept resolution path |
| C-15 | Projection convergence/divergence call | correctness | Consensus section explicitly labels whether downstream projections converge or diverge across roles (not only immediate-finding convergence) |
| C-16 | Self-correction gate pre-commit | format | Structural gate forces model to verify location before committing to matrix — distinct from naming invalid forms (C-12) |
| C-17 | Role authority sequence declaration | format | Review order is stated with an explicit authority rationale: blocking roles (security, schema) before advisory roles (DX, docs), and the ordering principle is named; naming the order without the rationale scores PARTIAL |
| C-18 | Axis conflict resolution rule | correctness | When two or more instruction axes are composed in one prompt, an explicit tiebreaker rule states which axis wins on conflict (e.g., "if property declaration form conflicts with inertia framing, use property declaration form"); required only when N_axes >= 2 — single-axis prompts are exempt |

---

## Scoring Notes

- **PARTIAL** counts as 0.5 in pass totals for all tiers.
- **N/A** (e.g., C-18 on single-axis prompts) counts as PASS for composite calculation to avoid
  penalizing architecturally correct scope choices.
- Projected scores (†) carry a confidence discount of up to 6 pts on composite when 3+ criteria
  are projected without prompt text.
- Aspirational N is now 10. A variation that passes all 10 aspirational criteria adds the full
  10 pts to composite.
```

---

**What changed and why:**

| New criterion | Signal source | Why PARTIAL ≠ PASS |
|---|---|---|
| C-17 | V-01/V-04/V-05 all impose role ordering but omit the rationale | "Security before DBA" is observable; "because schema changes gate permission changes" is the authority signal |
| C-18 | V-05 only, flagged as "structural overcrowding risk" | Axis composition without a conflict rule produces register blending — the failure mode is silent and probabilistic, not structural |
