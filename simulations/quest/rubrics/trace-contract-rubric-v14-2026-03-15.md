Reading the scorecard, two synthesis patterns emerge from R13:

- **V-R13-A**: Value-binding provenance at the gate-writing step — V-01 and V-05 pass C-35 by writing a structured `S6.5-CENSUS-GATE:` block with a named `census-distribution:` field holding the verbatim S5.5 Sub-task A value. The remaining re-derivation surface: the gate-writing step itself could re-derive the `census-distribution:` value from the findings rather than copying it from Sub-task A output — the field's presence is verifiable but its provenance is not. C-35 requires the gate token to encode the verbatim value; V-R13-A identifies the next escalation: an explicit provenance-binding sub-step within S6.5 that names S5.5 Sub-task A as the source, reproduces the Sub-task A `mechanism-distribution:` output line verbatim as the `census-distribution:` value, and emits a `gate-provenance: S5.5-Sub-task-A` field alongside `census-distribution:` — converting value-binding from a structural constraint into a provenance-traceable copy that closes the gate-writing re-derivation surface without requiring re-inspection of the findings section → **C-37**

- **V-R13-B**: Verdict-gate closure rule for unresolved FAIL rows — V-01 and V-05 pass C-36 by writing a post-population cross-field verification table whose verdict column makes `mechanism-type-shared:` mismatches visible rather than silent. The remaining surface: a FAIL row in the table has no defined consequence — the document can be closed with unresolved FAILs, making the audit surface a detection mechanism rather than a blocking gate. C-36 requires the consistency check; V-R13-B identifies the next escalation: a verdict-gate closure rule stating that the document cannot proceed to `## Summary` while any verdict-table row holds FAIL, and that the resolution path is explicit — a FAIL row requires the staging line at S5.5 Sub-task B to be amended (not the template fill site patched), making correction traceable to the census stage and preventing silent value substitution downstream → **C-38**

---

# Rubric: trace-contract v14

Reading the scorecard, two synthesis patterns emerge from R13:

- **V-R13-A**: Provenance-binding at the gate-writing step — V-01 and V-05 achieve C-35 via a
  structured `S6.5-CENSUS-GATE:` block with a named `census-distribution:` field holding the
  verbatim S5.5 Sub-task A value. The field's presence is structurally verifiable; its provenance
  at the gate-writing step is not — the block could be authored by re-deriving the count from
  findings rather than copying from Sub-task A output, leaving a re-derivation surface inside
  the gate step itself. C-35 requires the gate token to encode the verbatim value; V-R13-A
  identifies the next escalation: an explicit provenance-binding sub-step within S6.5 that
  names S5.5 Sub-task A as the authoritative source, reproduces its `mechanism-distribution:`
  output line verbatim as the `census-distribution:` value, and emits a
  `gate-provenance: S5.5-Sub-task-A` field alongside `census-distribution:` — converting
  value-binding from a structural constraint into a provenance-traceable copy whose source
  is auditable by field inspection without re-inspecting the findings section → **C-37**

- **V-R13-B**: Verdict-gate closure rule for unresolved FAIL rows — V-01 and V-05 achieve C-36
  via a post-population cross-field verification table whose verdict column makes
  `mechanism-type-shared:` mismatches visible rather than silent. The remaining surface: a FAIL
  row has no defined consequence — the document can be closed with unresolved FAIL verdicts,
  making the audit surface a detection mechanism rather than a structural blocking gate. C-36
  requires the consistency check; V-R13-B identifies the next escalation: a verdict-gate closure
  rule stating that the document cannot proceed to `## Summary` while any verdict-table row
  holds FAIL, and that the explicit resolution path requires amending the staging line at S5.5
  Sub-task B rather than patching the template fill site — making every correction traceable
  to the census stage, preventing silent value substitution downstream, and converting the
  post-population audit surface from a detection-only mechanism into a structural closure
  precondition that eliminates unresolved integrity failures from the final document → **C-38**

---

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
  where the grouping decision and its supporting evidence are fixed before template population
  begins — decoupling the grouping analysis from the template authoring step and making the
  decision visible to audit without re-tracing the findings section → **C-32**

---

## Rubric Table

| ID | Criterion | Points |
|----|-----------|--------|
| C-26 | Output format token `[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]` present | 10 |
| C-27 | Zero / Singleton / Multi-pattern branch templates with named structural slots | 10 |
| C-28 | `mechanism-type:` token on each finding entry, constrained vocabulary | 15 |
| C-29 | `mechanism-type-shared:` field present in both Singleton and Multi-pattern branch templates, unconditionally | 15 |
| C-30 | `mechanism-distribution:` aggregate present in Summary section | 10 |
| C-31 | Mandatory interstitial S5.5 step placed between S5 (findings) and closure; Sub-task A produces `mechanism-distribution:` via single ordered walk; Sub-task B stages per-group candidates; explicit "do not skip to S6 until both sub-tasks complete" enforcement | 20 |
| C-32 | `group-candidate-N: findings=[...] mechanism-type-shared=... rationale={...}` staging format with `rationale:` clause in S5.5 Sub-task B entries | 20 |
| C-33 | Explicit copy-forward directive in Summary spec designating S5.5 Sub-task A as authoritative source; `mechanism-distribution:` in Summary is a verbatim copy of Sub-task A output, not a recount | 15 |
| C-34 | `source: group-candidate-N` back-reference field in each `pattern-N:` Multi-pattern branch template entry naming the specific S5.5 Sub-task B staging line it was derived from | 15 |
| C-35 | Mandatory blocking gate step S6.5 that emits a structured gate token encoding the verbatim `mechanism-distribution:` value from S5.5 Sub-task A in a named field (`census-distribution:`); `## Summary` section header is structurally inaccessible until gate token is emitted; `gate-status: OPEN` as auditable exit condition | 15 |
| C-36 | Post-population cross-field verification table with columns `pattern-N \| source \| mechanism-type-shared (at fill site) \| mechanism-type-shared (from staging) \| verdict`; written after all pattern entries are complete; a mismatch row is a C-36 violation detectable without re-inspecting the findings section | 15 |
| C-37 | Provenance-binding sub-step within S6.5 naming S5.5 Sub-task A as the authoritative source; `census-distribution:` value is reproduced verbatim from Sub-task A output; `gate-provenance: S5.5-Sub-task-A` field emitted alongside `census-distribution:` — gate provenance is auditable by field inspection without re-inspecting findings | 15 |
| C-38 | Verdict-gate closure rule: document cannot proceed to `## Summary` while any C-36 verdict-table row holds FAIL; explicit resolution path requires amending the staging line at S5.5 Sub-task B (not patching the template fill site); every correction is traceable to the census stage | 15 |
| **Total** | | **190** |
