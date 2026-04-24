Reading the scorecard, two synthesis patterns emerge from R11:

- **V-R11-A**: V-05 reaches 105/110 with the only gap at C-30 (10/15). The tabular column in Sub-task A makes the `mechanism-distribution:` tally mechanical and error-free, but the Summary section's obligation to copy that output is implied by the data flow rather than structurally required by the spec. C-30 requires `mechanism-distribution:` in Summary; V-R11-A identifies the next escalation: an explicit copy-forward directive in the Summary section spec that designates S5.5 Sub-task A as the authoritative source and requires the `mechanism-distribution:` line to appear in Summary by verbatim copy from Sub-task A output — closing the gap between census production and summary consumption and making the data flow a structural obligation rather than an inferred one → **C-33**

- **V-R11-B**: V-05 closes C-32 (20/20) via the `rationale:` clause in each `group-candidate-N:` staging line, which makes format-compliant fill-in without genuine grouping analysis visibly distinguishable. C-32 requires the staging format with `rationale:` clause; V-R11-B identifies the next escalation: each `pattern-N:` entry in the Multi-pattern Patterns branch template carries a `source: group-candidate-N` back-reference to the specific staging line it was derived from — the census stage produces the grouping decision with rationale, the template stage names its source, creating a closed audit chain that enables verification that every populated branch template entry traces to a deliberate S5.5 staging decision rather than a template-site re-derivation → **C-34**

---

# Rubric: trace-contract v12

Reading the scorecard, two synthesis patterns emerge from R11:

- **V-R11-A**: Explicit copy-forward mandate from S5.5 to Summary — V-05's 105/110 result shows
  that when Sub-task A performs a mechanical column scan producing `mechanism-distribution:` data
  at S5.5, the Summary section's obligation to copy this output verbatim is implied by the data
  flow but not structurally required. C-30 requires `mechanism-distribution:` in Summary;
  V-R11-A identifies the next escalation: an explicit copy-forward directive in the Summary
  section spec that designates S5.5 Sub-task A as the authoritative source and requires the
  `mechanism-distribution:` line to appear in Summary by verbatim copy from Sub-task A output —
  eliminating the gap between census production and summary consumption, and making the data flow
  obligation structural rather than inferred → **C-33**

- **V-R11-B**: Staging-to-template reference chain — V-05's `rationale:` clause in
  `group-candidate-N:` staging lines closes C-32 by making format-compliant fill-in without
  genuine grouping analysis visibly distinguishable. C-32 requires the staging format with
  `rationale:` clause; V-R11-B identifies the next escalation: each `pattern-N:` entry in the
  Multi-pattern Patterns branch template carries a `source: group-candidate-N` back-reference to
  the specific staging line it was derived from, creating a closed audit chain — the census stage
  produces the grouping decision with rationale, the template stage copies from the staging line
  and names its source, enabling verification that every populated branch template entry traces to
  an S5.5 staging decision rather than a template-site re-derivation → **C-34**

---

Reading the scorecard, two synthesis patterns emerge from R10 (carried forward):

- **V-R10-A**: Dedicated Taxonomy Census step (S5.5) — V-03's 110/110 result shows that computing
  `mechanism-distribution:` inside Summary and `mechanism-type-shared:` inside Patterns branch
  templates as separate passes requires re-inspection of the findings section twice. C-29 requires
  `mechanism-type-shared:` unconditionally; C-30 requires `mechanism-distribution:` as a computed
  aggregate; V-R10-A identifies the next escalation: a mandatory interstitial lifecycle step S5.5
  placed between S5 (findings) and the closure that performs both computations in a single ordered
  walk — Sub-task A tallies mechanism-type tokens across all findings to produce the
  `mechanism-distribution:` line; Sub-task B stages per-group mechanism alignment candidates.
  Both downstream consumers (Summary and Patterns branch templates) copy from S5.5 outputs
  verbatim, eliminating re-derivation errors and ensuring distribution aggregate and per-group
  alignment share a single consistent census pass → **C-31**

- **V-R10-B**: Group-candidate staging format in S5.5 Sub-task B — V-03 emits structured
  `group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token or 'mixed']`
  entries for each candidate Patterns group before any branch template is populated. C-29 requires
  `mechanism-type-shared:` in the branch template; V-R10-B identifies the next escalation: the
  mechanism-alignment computation is externalized into a visible staging line at the census site,
  decoupling the determination step from the template-filling step — the branch template then
  copies from the staging line rather than re-deriving the alignment at write time, making the
  type-alignment decision inspectable and auditable before it propagates into the Patterns
  section → **C-32**

---

Reading the scorecard, two synthesis patterns emerge from R9 (carried forward):

- **V-R9-A**: Taxonomy-aligned Patterns synthesis — V-05's C-28 `mechanism-type:` token tags
  each finding with a vocabulary-constrained class. C-28 requires the per-finding type token;
  V-R9-A identifies the next escalation: a `mechanism-type-shared:` field in the Singleton and
  Multi-pattern branch templates propagates the taxonomy into the synthesis layer — same-class
  groupings (`mechanism-type-shared: field-mapping`) signal a systemic root cause requiring one
  fix, while mixed-class groupings (`mechanism-type-shared: mixed`) signal coincident symptoms
  requiring independent fixes, enabling automated fix-strategy detection from the Patterns
  section alone without re-inspecting individual finding blocks → **C-29**

- **V-R9-B**: Taxonomy distribution aggregate in Summary — V-05's per-finding `mechanism-type:`
  tokens accumulate document-locally but are not analyzed at document close. C-28 requires the
  per-finding type token; V-R9-B identifies the next escalation: a taxonomy distribution line in
  the Summary section converts individual type tokens into a document-level class distribution
  aggregate (e.g., `mechanism-distribution: field-mapping:2 serialization-path:1
  conditional-branch:1`), enabling cross-session comparison of failure-class prevalence by
  mechanism type and trending of systemic failure patterns across contract versions → **C-30**

---

Reading the scorecard, three synthesis patterns emerged from R8 (carried forward):

- **V-R8-A**: Gate-closure confirmation token — V-01's C-23 PASS evidence shows a matched
  two-phase gate: opening token `[EXPECTED-SEALED | clauses:N | date:... | author:... |
  phase:1-complete]` plus a closure token that echoes `gate-clauses`. C-23 requires only the
  opening token with metadata; V-R8-A identifies the next escalation: a matched closure token
  placed immediately after the findings section that echoes the committed clause count and adds
  a resolved count (`clauses-resolved:M`), enabling automated diff-verification that every
  committed expected clause was accounted for → **C-26**

- **V-R8-B**: Branch-conditional Patterns template slots — V-02's C-24 PASS evidence shows
  three named branches (zero / singleton / multi) with explicit handling instructions. C-24
  requires per-branch instructions; V-R8-B identifies the next escalation: each branch carries
  pre-printed structural slots (`no-pattern-confirmation:` for zero, `single-finding-ref:` +
  `root-cause:` for singleton, `pattern-N: root-cause: findings:[]` for multi), converting
  procedural branch instructions into structural branch templates that enforce field completion
  within each branch at write time → **C-27**

- **V-R8-C**: Mechanism taxonomy constraint — V-03's C-25 self-test rule distinguishes causal
  mechanisms from symptom restatements via a necessary-information condition. C-25 requires the
  self-test procedure; V-R8-C identifies the next escalation: a vocabulary-constrained mechanism
  taxonomy — a named enumeration of mechanism types appropriate to the contract domain (e.g.,
  `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`,
  `null-handling`) — applied as a per-finding `mechanism-type:` token that constrains root-cause
  prose to a verifiable class, making taxonomy drift visible at write time rather than at review
  time → **C-28**

---

## Rubric Criteria (v12)

| ID | Description | Points |
|----|-------------|--------|
| C-26 | Gate-closure confirmation token (`clauses-resolved` echo matched to opening gate) | 10 |
| C-27 | Branch-conditional Patterns template slots (pre-printed structural fields per branch) | 10 |
| C-28 | Mechanism taxonomy constraint (vocabulary-constrained per-finding `mechanism-type:` token) | 15 |
| C-29 | `mechanism-type-shared:` in Singleton + Multi-pattern branch templates | 15 |
| C-30 | `mechanism-distribution:` aggregate in Summary | 10 |
| C-31 | S5.5 mandatory interstitial Taxonomy Census step (single ordered walk, both aggregates) | 20 |
| C-32 | `group-candidate-N:` staging format with `rationale:` clause in Sub-task B (before any branch template fill) | 20 |
| C-33 | Explicit copy-forward directive: Summary names S5.5 Sub-task A as authoritative source for `mechanism-distribution:` (verbatim copy, not re-derivation) | 15 |
| C-34 | Staging-to-template reference chain: each `pattern-N:` entry in Multi-pattern branch carries `source: group-candidate-N` back-reference to S5.5 staging line | 15 |
| **Total** | | **130** |
