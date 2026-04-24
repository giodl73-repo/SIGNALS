Written to `simulations/quest/golden/scout-risk-variate-R1-2026-03-16.md`.

---

## scout-risk — Prompt Variations R1

**5 variations across 4 axes. Single-axis first, then combinations.**

---

### V-01 — Output Format (table-first)
**Axis**: table schema as the primary structural device
**Hypothesis**: Forcing a table with columns `# | Dimension | Risk | Severity | Likelihood | Mitigation` enforces anatomy completeness (C-03) and dimension labeling (C-06) structurally — the model cannot omit a column. Inertia is row 0 by convention.
**Vulnerability**: visual flattening of inertia into a row may dilute its primacy; no explicit anti-generic mitigation rule.

---

### V-02 — Inertia Framing (named section)
**Axis**: inertia gets its own titled section before the dimensional register
**Hypothesis**: `## 0. Inertia Risk — The Status Quo Competitor` as a section header makes C-01 structurally unavoidable and invites richer prose analysis. Includes an optional interdependency section.
**Vulnerability**: rich prose on inertia may drift toward generic "status quo is comfortable" writing rather than topic-specific analysis.

---

### V-03 — Phrasing Register (imperative/conversational)
**Axis**: direct command sequence ("Do X. Then do Y. Never do Z.")
**Hypothesis**: imperative phrasing produces more literal compliance with hard rules (C-01 position, C-04 severity scale). Includes an explicit **self-check step** that re-reads all mitigations and mandates replacement of generic hedges — directly targeting C-05.
**Vulnerability**: mechanical compliance may produce adequate but shallow mitigations.

---

### V-04 — Role Sequence + Lifecycle (explicit multi-role protocol)
**Axis**: three analyst roles (Skeptic / Realist / Scheduler) run in explicit sequence, each owning specific dimensions; four explicit lifecycle phases
**Hypothesis**: role ownership of dimensions drives C-02 coverage; role-specific failure-mode vocabulary produces richer mitigations; Scheduler / Realist cross-check surfaces C-09 interdependencies naturally.
**Vulnerability**: role protocol may produce redundant risks or dilute the inertia-first rule across a longer prompt.

---

### V-05 — Full Integration (all axes)
**Axis**: table format + named inertia section + imperative rules + role sequence + explicit interdependency step + self-check gate
**Hypothesis**: each single-axis win addresses a distinct rubric criterion — combining them produces the highest composite score. The self-check gate at Step 4 catches violations before artifact write.
**Vulnerability**: prompt length may diffuse the imperative force; model may satisfice on the checklist rather than actually verify.

---

### Variation Map against Rubric

| | C-01 inertia first | C-02 coverage | C-03 anatomy | C-04 severity scale | C-05 specific mitigation | C-06 dimension label | C-09 interdependency |
|---|---|---|---|---|---|---|---|
| V-01 | Medium (row 0) | Medium | **High** (columns) | Medium | Medium | **High** (column) | Low |
| V-02 | **High** (own section) | Medium | Medium | Medium | Medium | Medium | Medium |
| V-03 | **High** ("first, always") | Medium | **High** (step-by-step) | **High** (only 3 values) | **High** (explicit re-check) | Medium | Low |
| V-04 | **High** (Role A owns it) | **High** (roles drive it) | **High** (per-role) | Medium | **High** (roles name actions) | Medium | **High** (cross-check) |
| V-05 | **High** (Step 1) | **High** (roles) | **High** (table+gate) | **High** (absolute rule) | **High** (replace rule) | **High** (column) | **High** (Step 3) |

Next step: run `/quest-score` against a sample invocation to see which variation actually achieves golden.
