Reading the scorecard, two synthesis patterns emerge from R12:

- **V-R12-A**: V-03 reaches 115/130 (failing only C-34) by satisfying C-33 via blocking gate S6.5 — "Do not write the `## Summary` section header until this gate token is emitted" — a structural enforcement mode that exceeds the named-directive form required by C-33. V-04 reaches 130/130 using a labeled procedural step plus an authoritativeness declaration: "If a fresh count would produce a different value, the S5.5 value is authoritative." V-R12-A identifies the next escalation: a mandatory blocking gate step S6.5 placed between S6 (census close) and the Summary section that emits a gate token encoding the verbatim `mechanism-distribution:` value from S5.5 Sub-task A — the Summary section header cannot be written until this gate token is emitted, converting the copy-forward directive from a procedural instruction into a structural lifecycle precondition that enforces census primacy at the architectural level rather than the behavioral level → **C-35**

- **V-R12-B**: V-04's audit rule for C-34 — "(a) `source:` names a `group-candidate-N` from S5.5 Sub-task B, and (b) `mechanism-type-shared:` matches that staging line's value exactly. A mismatch is a C-34 violation." — extends the back-reference field from a traceability annotation into a cross-field integrity constraint. C-34 requires `source: group-candidate-N` in each `pattern-N:` entry; V-R12-B identifies the next escalation: a cross-field consistency rule stating that `mechanism-type-shared:` at the template fill site must equal the `mechanism-type-shared` value on the named `group-candidate-N` staging line — a mismatch is detectable evidence that the template field was re-derived at write time rather than copied from the staging decision, elevating the audit chain from a presence check to a consistency verification that closes the remaining re-derivation surface → **C-36**

---

# Rubric: trace-contract v13

Reading the scorecard, two synthesis patterns emerge from R12:

- **V-R12-A**: Blocking gate S6.5 as lifecycle precondition for Summary — V-03's 115/130 result
  (failing only C-34) shows that the copy-forward obligation can be enforced architecturally via
  a gate step that makes the Summary section header structurally inaccessible until the gate token
  is emitted. V-04's authoritativeness declaration ("If a fresh count would produce a different
  value, the S5.5 value is authoritative") adds semantic weight but remains behavioral. C-33
  requires the named copy-forward directive designating S5.5 Sub-task A as authoritative source;
  V-R12-A identifies the next escalation: a mandatory blocking gate step S6.5 emitting a token
  that encodes the verbatim `mechanism-distribution:` value from S5.5 Sub-task A, where the gate
  token's emission is the structural precondition for writing the `## Summary` section header —
  converting census primacy from a behavioral instruction into a lifecycle invariant that cannot
  be bypassed → **C-35**

- **V-R12-B**: Cross-field consistency rule for staging-to-template integrity — V-04's audit
  rule for C-34 requires that `mechanism-type-shared:` in each `pattern-N:` entry match the
  value from the named `source: group-candidate-N` staging line exactly, and declares a mismatch
  a C-34 violation. C-34 requires the `source: group-candidate-N` back-reference field in each
  pattern entry; V-R12-B identifies the next escalation: an explicit cross-field consistency
  rule embedded in the spec stating that `mechanism-type-shared:` at the template fill site must
  equal the `mechanism-type-shared` field on the named staging line — a field-level integrity
  constraint that is checkable without re-inspecting the findings section, converting the
  source reference from a traceability annotation into an enforceable consistency predicate
  that detects re-derivation at the template site → **C-36**

---

Reading the scorecard, two synthesis patterns emerge from R11 (carried forward):

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

## Rubric Table

| ID | Description | Points |
|----|-------------|--------|
| C-26 | Gate-closure confirmation token (`clauses-resolved` echo) | 10 |
| C-27 | Branch-conditional Patterns template slots (pre-printed structural fields per branch) | 10 |
| C-28 | Vocabulary-constrained `mechanism-type:` token per finding | 15 |
| C-29 | `mechanism-type-shared:` in Singleton + Multi-pattern branch templates | 15 |
| C-30 | `mechanism-distribution:` aggregate in Summary | 10 |
| C-31 | S5.5 mandatory interstitial Taxonomy Census (single ordered walk, both sub-tasks) | 20 |
| C-32 | `group-candidate-N:` staging format with `rationale:` clause in Sub-task B | 20 |
| C-33 | Explicit copy-forward directive: Summary names S5.5 Sub-task A as authoritative source for `mechanism-distribution:` | 15 |
| C-34 | Staging-to-template reference chain: `source: group-candidate-N` in each `pattern-N:` Multi-pattern entry | 15 |
| C-35 | Blocking gate S6.5: mandatory lifecycle gate token before Summary section header may be written; gate token encodes verbatim `mechanism-distribution:` from S5.5 Sub-task A | 15 |
| C-36 | Cross-field consistency rule: `mechanism-type-shared:` in each `pattern-N:` entry must match the value from the named `source: group-candidate-N` staging line; mismatch is a structural violation | 15 |
| **Total** | | **160** |
