Reading the v2 rubric to confirm what was shown, then I'll extract the new patterns and write v3.

The scorecard reveals three distinct excellence mechanisms not yet captured as criteria:

1. **V-02 C-11** — beyond formula lock: "there is no third choice" closes the rationalization escape; explicit reclassify-or-accept provides a resolution path after the verdict. This is structurally distinct from C-11 (which captures the property declaration).

2. **V-03 C-06** — consensus analysis explicitly checks whether *downstream/inertia projections* across roles agree, not just immediate findings. Static convergence ≠ projection convergence.

3. **V-01 C-08** — the self-correction instruction ("rewrite the location before adding it to the matrix") is what made C-08 PASS where V-02/V-04 were PARTIAL. Structural self-correction beats a column header.

These become C-14, C-15, C-16. Aspirational pool grows from N=5 to N=8.

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 3
supersedes: org-pr-rubric-v2-2026-03-16.md
---

# Scoring Rubric -- org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v2 -> v3)

Added three aspirational criteria extracted from R2 excellence signals:

- **C-14** (verdict escape closure): V-02 C-11 strongest-lock evidence — the excellence in
  V-02 was not just the property declaration ("this formula is not editable") but the
  companion closure: "There is no third choice" eliminates the rationalization escape;
  explicit reclassify-or-accept provides a defined resolution path. C-11 captures the lock;
  C-14 captures the closure. A variation can pass C-11 without C-14.

- **C-15** (projection-aware consensus): V-03 C-06 evidence — consensus analysis explicitly
  notes whether downstream/inertia projections from different roles agree or diverge, not only
  whether immediate findings converge. Static convergence and projection convergence are
  structurally different checks; only V-03 required the second.

- **C-16** (finding self-correction gate): V-01 C-08 mechanism — the LOCATOR RULES block
  included "rewrite the location before adding it to the matrix," a structural self-correction
  step that made C-08 PASS where V-02 and V-04 were only PARTIAL (column header only). Named
  invalid forms (C-12) tell the model what not to do; a self-correction gate forces it to
  verify before committing.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total) — unchanged

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Multi-role coverage | coverage | 2+ labeled sections from defined role set, each with a finding |
| C-02 | P1/P2/P3 on every finding | correctness | Zero untagged findings |
| C-03 | File-based role selection rationale | correctness | Each role's inclusion tied to specific changed files |
| C-04 | Explicit go/no-go recommendation | correctness | Labeled verdict block, derivable from findings |
| C-05 | Per-role structure | format | Each section opens with role-name heading; sections can't bleed |

## Recommended Criteria (weight: 30 pts total) — unchanged

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Consensus analysis | depth | Convergence + conflicts both addressed |
| C-07 | P1 blocks go | correctness | Any open P1 = No-Go, no exceptions |
| C-08 | Actionable findings | depth | 80%+ of findings include a specific locator |

## Aspirational Criteria (weight: 10 pts total) — N=5 -> N=8

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Author-blind perspective | depth | 1+ finding per section challenges an embedded assumption |
| C-10 | Non-obvious issue surfaced | coverage | 1+ cross-cutting / out-of-diff finding present |
| C-11 | Formula lock | correctness | Explicit "this formula is not editable" or equivalent; applying it without locking it satisfies C-07 not C-11 |
| C-12 | Locator anti-pattern named | depth | Names what does NOT count as a locator (e.g., "General concern is not a location") |
| C-13 | Inertia framing | depth | 1+ finding answers "what breaks if this stays in" with a downstream effect or failure mode |
| C-14 | **Verdict escape closure** | correctness | Formula section explicitly closes escape routes — at minimum names one impossible path (e.g., "there is no third choice") OR provides a reclassify-or-accept resolution path after verdict; C-11 lock + C-14 closure are distinct: a variation can pass one without the other |
| C-15 | **Projection-aware consensus** | depth | Consensus analysis explicitly addresses whether downstream/inertia projections from different roles agree or diverge, not only whether immediate findings converge |
| C-16 | **Finding self-correction gate** | depth | Finding template includes an explicit self-correction step before an entry is committed (e.g., "before adding: verify the location meets the locator rules; rewrite if not") |

---

## Scoring Worksheet

```
Essential (N=5):    C-01[_] C-02[_] C-03[_] C-04[_] C-05[_]
  essential_pts  = essential_pass / 5 * 60 = __

Recommended (N=3):  C-06[_] C-07[_] C-08[_]
  recommended_pts = recommended_pass / 3 * 30 = __

Aspirational (N=8): C-09[_] C-10[_] C-11[_] C-12[_] C-13[_] C-14[_] C-15[_] C-16[_]
  aspirational_pts = aspirational_pass / 8 * 10 = __

Composite = essential_pts + recommended_pts + aspirational_pts = __
Golden = all essential pass? [Y/N] AND composite >= 80? [Y/N] → [GOLDEN / NOT GOLDEN]
```

---

## R2 Scorecard (rubric v2 applied)

### Scoring Key

| Symbol | Meaning | Formula value |
|--------|---------|---------------|
| PASS | Criterion clearly met | 1 |
| PARTIAL | Criterion partially met / ambiguous | 0 (treated as FAIL) |
| FAIL | Criterion not met | 0 |

**C-05 note — matrix formats**: V-01 and V-05 use a single findings matrix with a Role column
rather than per-role sections with `### Role` headings. The matrix satisfies "sections can't
bleed" but not "each section opens with a role-name heading." Scored PARTIAL (treated as FAIL)
consistently across both.

**C-08 note — locator confidence**: Scored PASS where the prompt provides an explicit locator
rules block or inline format that structurally forces a location (V-01 Step 3 block, V-03
inline `[file:location]` format, V-05 Phase 3 block). Scored PARTIAL (FAIL) where only a
column header like "[file:function or pattern]" guides the model without a self-correction
mechanism (V-02, V-04).

---

### V-01 — Locator Anti-Pattern Block (targeting C-12)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Step 4 matrix with Role column; "Minimum 2 ACTIVE roles must contribute at least one non-null finding row" |
| C-02 | P1/P2/P3 on every finding | PASS | "Every finding must have a severity of P1, P2, or P3. No other values permitted." |
| C-03 | File-based role rationale | PASS | Step 2 "Triggered By" column requires specific file(s) per role |
| C-04 | Explicit go/no-go | PASS | Step 6 "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PARTIAL | Matrix rows not per-role sections; Role column provides attribution but no `### heading` per role |
| C-06 | Consensus analysis | PASS | Step 5 has Convergence table + Conflicts table both required |
| C-07 | P1 blocks go | PASS | Step 6 formula present; verdict derivable |
| C-08 | Actionable locators (80%) | PASS | Step 3 LOCATOR RULES block names valid + invalid forms; self-correction instruction: "rewrite the location before adding it to the matrix" |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no instruction to challenge embedded assumptions |
| C-10 | Non-obvious issue surfaced | FAIL | No cross-cutting / out-of-diff mechanism |
| C-11 | Formula lock | PARTIAL | "apply without editorial override" — instructional but not a property declaration; rubric exemplar is "this formula is not editable" |
| C-12 | Locator anti-pattern named | PASS | Seven named disallowed forms: "The codebase — not a location", "Throughout — not a location", "General concern — not a location", etc. |
| C-13 | Inertia framing | FAIL | No downstream failure mode required on findings |
| C-14 | Verdict escape closure | FAIL | No "third choice" elimination; no reclassify-or-accept path |
| C-15 | Projection-aware consensus | FAIL | Convergence/conflicts tables present but no instruction to check projection agreement |
| C-16 | Finding self-correction gate | PASS | "rewrite the location before adding it to the matrix" is an explicit pre-commit gate |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[x]
  essential_pass = 4/5 → essential_pts = 4/5 * 60 = 48

Recommended (N=3):  C-06[P] C-07[P] C-08[P]
  recommended_pass = 3/3 → recommended_pts = 3/3 * 30 = 30

Aspirational (N=8): C-09[x] C-10[x] C-11[x] C-12[P] C-13[x] C-14[x] C-15[x] C-16[P]
  aspirational_pass = 2/8 → aspirational_pts = 2/8 * 10 = 2.5

Composite = 48 + 30 + 2.5 = 80.5
Golden = all essential pass? NO (C-05 partial) → NOT GOLDEN
```

---

### V-02 — Formula Lock (targeting C-11)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Per-role `### [ROLE NAME]` sections, each with findings template |
| C-02 | P1/P2/P3 on every finding | PASS | "Every finding requires a severity" rule |
| C-03 | File-based role rationale | PASS | Role Selection table with per-role "Rationale" column tied to File Manifest |
| C-04 | Explicit go/no-go | PASS | "**Verdict**: Go / No-Go" labeled block in GO/NO-GO section |
| C-05 | Per-role structure | PASS | `### [ROLE NAME]` headings; section template prevents role bleeding |
| C-06 | Consensus analysis | PASS | CONSENSUS ANALYSIS section with Convergence + Conflicts both required |
| C-07 | P1 blocks go | PASS | Formula derived from findings; no exception pathway |
| C-08 | Actionable locators (80%) | PARTIAL | "[file:function or pattern]" column header only; no named invalid forms, no self-correction step |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no author-blind posture instruction |
| C-10 | Non-obvious issue surfaced | FAIL | No mechanism targeting cross-cutting concerns |
| C-11 | Formula lock | PASS | "**This formula is not editable. It applies without exception.**" — property declaration, not instruction |
| C-12 | Locator anti-pattern named | FAIL | No named disallowed locator forms |
| C-13 | Inertia framing | FAIL | No downstream failure mode required |
| C-14 | Verdict escape closure | PASS | "There is no third choice. The formula cannot be rationalized away at this step." + explicit reclassify-or-accept closure — both escape elimination and resolution path present |
| C-15 | Projection-aware consensus | FAIL | Consensus checks finding convergence/conflicts; no projection agreement check |
| C-16 | Finding self-correction gate | FAIL | No pre-commit verification step in finding template |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[P]
  essential_pass = 5/5 → essential_pts = 5/5 * 60 = 60

Recommended (N=3):  C-06[P] C-07[P] C-08[x]
  recommended_pass = 2/3 → recommended_pts = 2/3 * 30 = 20

Aspirational (N=8): C-09[x] C-10[x] C-11[P] C-12[x] C-13[x] C-14[P] C-15[x] C-16[x]
  aspirational_pass = 2/8 → aspirational_pts = 2/8 * 10 = 2.5

Composite = 60 + 20 + 2.5 = 82.5
Golden = all essential pass? YES, composite >= 80? YES → GOLDEN
```

---

### V-03 — Inertia Framing (targeting C-13)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Per-role `### [ROLE NAME]` sections each producing findings |
| C-02 | P1/P2/P3 on every finding | PASS | `[P1 / P2 / P3]` is part of the finding template; severity required structurally |
| C-03 | File-based role rationale | PASS | Role Selection with "Rationale (which changed file activates this role)" column |
| C-04 | Explicit go/no-go | PASS | "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PASS | `### [ROLE NAME]` headings; section template prevents bleeding |
| C-06 | Consensus analysis | PASS | CONSENSUS ANALYSIS addresses convergence + conflicts; notes whether downstream projections agree |
| C-07 | P1 blocks go | PASS | "Any open P1 = No-Go" with formula |
| C-08 | Actionable locators (80%) | PASS | Inline finding format `[P1/P2/P3] | [file:location] | [issue]` — location is structurally part of every finding, not a separate column that can be skipped |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no explicit instruction to challenge embedded assumptions |
| C-10 | Non-obvious issue surfaced | PASS | "If this stays in" downstream projection requires reasoning beyond the diff boundary; examples include PII in audit trails (compliance cross-cutting); failure mode projection naturally reaches surfaces the author wouldn't flag |
| C-11 | Formula lock | PARTIAL | Not shown in provided excerpt |
| C-12 | Locator anti-pattern named | PARTIAL | Not shown in provided excerpt |
| C-13 | Inertia framing | PASS | "If this stays in" framing is the structural mechanism; finding template requires a downstream effect or failure mode |
| C-14 | Verdict escape closure | PARTIAL | Not shown in provided excerpt |
| C-15 | Projection-aware consensus | PASS | C-06 evidence: "notes whether downstream projections agree" — cross-role projection convergence explicitly required |
| C-16 | Finding self-correction gate | PARTIAL | Not shown in provided excerpt |

*Note: V-03 scorecard truncated after C-10 in source; C-11/C-12/C-14/C-16 marked PARTIAL
pending full excerpt.*
```

---

Three new patterns extracted and locked:

| New ID | Signal source | What it captures |
|--------|---------------|-----------------|
| C-14 | V-02 C-11 strongest-lock | Escape closure: "no third choice" + reclassify-or-accept. C-11 locks the formula; C-14 closes the exits. |
| C-15 | V-03 C-06 | Projection-aware consensus: cross-role inertia projections checked for agreement, not just immediate findings. |
| C-16 | V-01 C-08 mechanism | Self-correction gate: pre-commit verification step in the finding template itself. The difference between C-08 PASS and PARTIAL. |

V-02 re-scores under v3: composite 82.5, still GOLDEN (C-14 PASS adds 0.5 pts to aspirational, net same category pass count as before since N grew from 5 to 8).
