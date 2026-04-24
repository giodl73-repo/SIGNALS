```markdown
Reading the scorecard, three synthesis patterns emerge from R14:

- **V-R14-A**: Schema co-requirement as structural field constraint — V-02 and V-04 pass C-37 by
  emitting `gate-provenance: S5.5-Sub-task-A` as an explicit named field alongside
  `census-distribution:`. V-03's PARTIAL shows that naming Sub-task A in authoring prose
  while omitting the field from the token output is insufficient — the field must be present
  in the emitted structure independently of how it is described in the instruction. C-37
  requires the provenance field; V-R14-A identifies the next escalation: declaring
  `census-distribution:` and `gate-provenance:` as co-required sibling fields in a named gate
  token schema, so that omitting either field is a schema violation detectable by field
  inspection without reading authoring prose — converting their joint presence from a prose
  convention into a structural property enforced by the output form itself → **C-39**

- **V-R14-B**: Formal imperative as execution-method specification — V-04 passes C-37 and C-38
  via `Bind: X := Y` and `Prohibit:` constructions that constrain the computation method, not
  only the expected result. A `Bind:` command distinguishes verbatim copy from re-derivation
  that coincidentally produces the same value; a `Prohibit:` construction eliminates the
  behavioral hedge that allows partial compliance ("do not patch" is weaker than
  "Prohibit: overwriting X at fill site without amending staging line"). C-37 and C-38 require
  the constraint to hold; V-R14-B identifies the next escalation: stating all copy-forward and
  amendment-path obligations in formal imperative form — `Bind: census-distribution :=
  Sub-task A mechanism-distribution verbatim`, `Assert: gate-provenance: S5.5-Sub-task-A is
  present`, `Prohibit: fill-site patch without staging-line amendment` — so that each
  obligation is a named executable command whose presence is auditable by structural inspection
  of the instruction, not inferred from its behavioral framing → **C-40**

- **V-R14-C**: Role ownership of attestation and witness falsifiability — V-05 passes C-37 and
  C-38 by assigning the provenance-binding sub-step to the census owner by role name, making
  re-derivation a role-boundary violation (only the Expert can attest their own census output),
  and adding an Automate witness step that performs character-for-character comparison of
  `census-distribution:` against the Sub-task A `mechanism-distribution:` output line.
  This two-party structure separates the Expert's attestation claim from a falsifiable
  verification test: the provenance guarantee is auditable at the gate boundary without
  re-inspecting the findings section, and no single role can silently satisfy both the
  attestation and the verification. C-37 requires the provenance field and named source; V-R14-C
  identifies the next escalation: a gate execution protocol that assigns attestation to the
  census owner by role name and assigns independent character-for-character verification to a
  distinct witness role, so that the gate token is auditable as a two-party claim-plus-proof
  structure rather than a single-role self-certification → **C-41**

---

# Rubric: trace-contract v15

Reading the scorecard, three synthesis patterns emerge from R14:

- **V-R14-A**: Schema co-requirement as structural field constraint — V-02 and V-04 pass C-37
  by emitting `gate-provenance: S5.5-Sub-task-A` as an explicit named field alongside
  `census-distribution:`. V-03's PARTIAL confirms that naming Sub-task A in authoring prose
  while omitting the field from the token output is insufficient — the field must be present
  in the emitted structure independently of how it is described in the instruction. C-37
  requires the provenance field; V-R14-A identifies the next escalation: declaring
  `census-distribution:` and `gate-provenance:` as co-required sibling fields in a named gate
  token schema, so that omitting either field is a schema violation detectable by field
  inspection without reading authoring prose — converting their joint presence from a prose
  convention into a structural property enforced by the output form itself → **C-39**

- **V-R14-B**: Formal imperative as execution-method specification — V-04 passes C-37 and C-38
  via `Bind: X := Y` and `Prohibit:` constructions that constrain the computation method, not
  only the expected result. A `Bind:` command distinguishes verbatim copy from re-derivation
  that coincidentally produces the same value; a `Prohibit:` construction eliminates the
  behavioral hedge that allows partial compliance. C-37 and C-38 require the constraint to hold;
  V-R14-B identifies the next escalation: stating all copy-forward and amendment-path
  obligations in formal imperative form — `Bind: census-distribution := Sub-task A
  mechanism-distribution verbatim`, `Assert: gate-provenance: S5.5-Sub-task-A is present`,
  `Prohibit: fill-site patch without staging-line amendment` — so that each obligation is a
  named executable command whose presence is auditable by structural inspection of the
  instruction, not inferred from its behavioral framing → **C-40**

- **V-R14-C**: Role ownership of attestation and witness falsifiability — V-05 passes C-37 and
  C-38 by assigning the provenance-binding sub-step to the census owner by role name, making
  re-derivation a role-boundary violation (only the Expert can attest their own census output),
  and adding an Automate witness step that performs character-for-character comparison of
  `census-distribution:` against the Sub-task A `mechanism-distribution:` output line. This
  two-party structure separates the Expert's attestation claim from a falsifiable verification
  test: the provenance guarantee is auditable at the gate boundary without re-inspecting the
  findings section, and no single role can satisfy both attestation and verification silently.
  C-37 requires the provenance field and named source; V-R14-C identifies the next escalation:
  a gate execution protocol that assigns attestation to the census owner by role name and
  assigns independent character-for-character verification to a distinct witness role, so that
  the gate token is auditable as a two-party claim-plus-proof structure rather than a
  single-role self-certification → **C-41**

---

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
  `pattern-N:` entries provides a narrative connection between the staging line and the template
  fill site but does not create a verifiable back-reference. C-31 requires the
  `mechanism-type-shared:` field in each pattern entry; V-R11-B identifies the next escalation:
  a named `source: group-candidate-N` back-reference field in each `pattern-N:` entry that
  identifies the specific staging line from which `mechanism-type-shared:` was copied — creating
  a field-level traceability chain from template fill site to census staging line that is
  auditable by field inspection without re-reading the findings section → **C-34**

---

## Criteria

### C-01 through C-25
*(carried forward from v10 baseline — omitted for brevity)*

### C-26 — `mechanism-distribution:` field present in S5.5 Sub-task A output (10 pts)
The Sub-task A output block must contain a `mechanism-distribution:` field that records the
column-scan result as a structured key-value entry. Presence is required; the value must reflect
the actual column scan performed.

### C-27 — Column scan executed mechanically (10 pts)
Sub-task A must document a row-by-row column scan of the `mechanism-type` column. The scan
must name each unique value encountered and count its occurrences. Assertion without evidence
of scan execution does not satisfy this criterion.

### C-28 — `mechanism-distribution:` value format correct (10 pts)
The `mechanism-distribution:` field value must enumerate all mechanism types present with
their counts in a consistent structured format (e.g., `pull: N, push: M`). A bare count
without type enumeration does not satisfy this criterion.

### C-29 — Sub-task B staging line present with `mechanism-type-shared:` field (10 pts)
The Sub-task B output must include a staging line for each group candidate that contains a
`mechanism-type-shared:` field. The staging line is the authoritative census record for that
group candidate's shared mechanism type.

### C-30 — `mechanism-distribution:` appears in `## Summary` (10 pts)
The Summary section must include a `mechanism-distribution:` line. Its presence is required;
it must not be omitted from the summary even when mechanism diversity is low.

### C-31 — `mechanism-type-shared:` field present in each `pattern-N:` entry (10 pts)
Each `pattern-N:` entry in the Patterns section must include a `mechanism-type-shared:` field.
The field must be populated; an empty or absent field does not satisfy this criterion.

### C-32 — `mechanism-type-shared:` value consistent with Sub-task B staging (10 pts)
The `mechanism-type-shared:` value in each `pattern-N:` entry must match the value recorded
on the corresponding Sub-task B staging line. A value that differs from the staging line
constitutes a C-32 violation regardless of whether it matches the findings section.

### C-33 — Explicit copy-forward directive designating S5.5 Sub-task A as authoritative source (15 pts)
The Summary section spec must contain an explicit directive stating that the
`mechanism-distribution:` line is to be copied verbatim from S5.5 Sub-task A output, and that
S5.5 Sub-task A is the authoritative source for this value. An implied data flow or a
matching value without a named source directive does not satisfy this criterion.

### C-34 — `source: group-candidate-N` back-reference field in each `pattern-N:` entry (15 pts)
Each `pattern-N:` entry must include a `source:` field that names the specific Sub-task B
staging line from which `mechanism-type-shared:` was copied (e.g., `source: group-candidate-1`).
A narrative rationale clause does not substitute for the named back-reference field.

### C-35 — Blocking gate S6.5 emitting verbatim `mechanism-distribution:` token before `## Summary` (15 pts)
A mandatory gate step S6.5 must exist between the census stage and the Summary section. The
gate step must emit a token that encodes the verbatim `mechanism-distribution:` value from
S5.5 Sub-task A. The gate token's emission is the structural precondition for writing the
`## Summary` section header — the Summary section must not be reachable until the gate token
is emitted.

### C-36 — Cross-field consistency rule: `mechanism-type-shared:` at fill site equals named staging line (15 pts)
The spec must contain an explicit cross-field consistency rule stating that
`mechanism-type-shared:` at each `pattern-N:` fill site must equal the `mechanism-type-shared:`
field on the staging line named by `source:`. A mismatch between the fill site and the named
staging line is a C-36 violation. A post-population verification table whose verdict column
makes mismatches visible satisfies this criterion; the verdict column must be present and
populated.

### C-37 — Provenance-binding sub-step within S6.5 emitting `gate-provenance: S5.5-Sub-task-A` field (15 pts)
The gate step S6.5 must contain an explicit provenance-binding sub-step that: (a) names
S5.5 Sub-task A as the authoritative source; (b) reproduces its `mechanism-distribution:`
output line verbatim as the `census-distribution:` value in the gate token; and (c) emits a
`gate-provenance: S5.5-Sub-task-A` field as a named field in the gate token alongside
`census-distribution:`. Naming Sub-task A in authoring prose while omitting the
`gate-provenance:` field from the emitted token does not satisfy this criterion — the field
must be present in the output structure independently of how it is described in the instruction.

### C-38 — Verdict-gate closure rule blocking `## Summary` on unresolved FAIL rows, with fill-site patch prohibition (15 pts)
The spec must contain a verdict-gate closure rule stating that the document cannot proceed
to `## Summary` while any verdict-table row holds FAIL. The resolution path must: (a) name
the S5.5 Sub-task B staging line as the only valid amendment target; and (b) explicitly
prohibit overwriting `mechanism-type-shared:` at the Patterns fill site without first amending
the staging line. Naming Sub-task B as the amendment target without an explicit fill-site
patch prohibition does not fully satisfy this criterion — the prohibition is a distinct
requirement from the gate-blocking rule.

### C-39 — Gate token schema declares `census-distribution:` and `gate-provenance:` as co-required sibling fields (15 pts)
The gate token specification must declare `census-distribution:` and `gate-provenance:` as
co-required sibling fields in a named schema, such that omitting either field is a schema
violation detectable by field inspection without reading authoring prose. A prose convention
stating that both fields should be present does not satisfy this criterion — the co-requirement
must be expressed as a structural schema property of the token output form itself, so that
field-level inspection of any emitted token can confirm or refute compliance without consulting
the instruction.

### C-40 — All copy-forward and amendment-path obligations stated as formal imperatives (`Bind:`, `Assert:`, `Prohibit:`) (15 pts)
Each copy-forward obligation and each amendment-path constraint must be stated in formal
imperative form: `Bind: X := Y` for verbatim-copy operations (constraining the computation
method, not only the result), `Assert: field is present` for presence requirements, and
`Prohibit: action` for excluded actions. Behavioral prose ("copy X from Y", "do not patch")
does not satisfy this criterion when a formal imperative form is achievable. Each formal
imperative must be a named, auditable command whose presence can be confirmed by structural
inspection of the instruction — not inferred from its framing.

### C-41 — Two-party gate execution protocol: census-owner attestation + independent witness falsifiability (15 pts)
The gate execution protocol must assign the provenance-binding attestation step to the census
owner by role name, making re-derivation a role-boundary violation. A separate, distinct
witness role must be assigned to perform character-for-character comparison of
`census-distribution:` against the Sub-task A `mechanism-distribution:` output line, providing
an independent falsifiability test for the attestation claim. The gate token must be auditable
as a two-party claim-plus-proof structure: the census owner's attestation is the claim; the
witness's character-for-character comparison is the falsifiability test. A single-role
self-certification — where the same role that writes the attestation also verifies it —
does not satisfy this criterion.

---

## Total Points

| Criteria | Points |
|----------|--------|
| C-01–C-25 | (baseline) |
| C-26–C-32 | 70 pts (10 pts each) |
| C-33–C-34 | 30 pts (15 pts each) |
| C-35–C-36 | 30 pts (15 pts each) |
| C-37–C-38 | 30 pts (15 pts each) |
| C-39–C-41 | 45 pts (15 pts each) |
| **R14 differentiators** | **C-39, C-40, C-41** |
```
