---
skill: quest-variate
skill_target: corps-build
round: 13
date: 2026-03-17
rubric_version: 11
r12_scorecard: (pending)
---

# Variate R13 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 13. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R12 excellence signals are now baseline criteria in rubric v11:
- C-37: INVARIANTS entries carry `cop:` pointer fields; COP-NN items carry `invariant:` annotations
- C-38: CO-EXTENSIVE DECLARATION explicitly names all three layers and asserts the coverage rule

R12 persistent PARTIALs targeted by R13:
- C-37: PARTIAL across V-01, V-02, V-03 (lack one or both layers). V-04 achieved PASS by
  combining INVARIANTS block + COP section. However V-05 R12 left INVARIANT-PATH-ISOLATION
  with `cop: (implicit in ROLES-WRITTEN receipt paths)` -- not a COP-NN identifier. A reviewer
  cannot verify which COP item enforces path isolation without inferring it. V-01 targets this:
  add COP-14 (PATH-ISOLATION-CHECK per team) so INVARIANT-PATH-ISOLATION carries a concrete
  `cop: COP-14` pointer, completing the bidirectional map for all five invariants.
- C-38: PARTIAL across V-01 through V-04 (two-layer declaration or missing the explicit
  coverage rule). V-05 R12 named all three layers ("no invariant outside INVARIANTS block; no
  enforcement code outside catalog; no output check outside CHECK-OUTPUT PROTOCOL") but did
  NOT assert that adding a NEW structural property requires entries in all three layers. The
  rubric requires this positive assertion. V-02 targets this: CO-EXTENSIVE DECLARATION gains
  an explicit PROPERTY-COVERAGE-RULE statement.

R13 variation axes:

1. PATH-ISOLATION COP assignment (V-01): Add COP-14 as `PATH-ISOLATION-CHECK [team-slug]:`
   emitted per team in WRITE-ROLES after all role files for that team are written. INVARIANT-PATH-ISOLATION
   changes from `cop: (implicit)` to `cop: COP-14`. Targets C-37 full precision.

2. PROPERTY-COVERAGE-RULE (V-02): CO-EXTENSIVE DECLARATION gains explicit rule: "Any new
   structural property MUST register one entry in each of the three layers (CATALOG,
   INVARIANTS, CHECK-OUTPUT PROTOCOL). A property tracked by fewer than three layers is
   structurally incomplete." Targets C-38 full PASS by adding the rule-assertion.

3. Phase ENFORCES-INVARIANTS annotation (V-03): Each phase body opens with
   `ENFORCES-INVARIANTS:` naming which INVARIANT-NN identifiers it enforces; phases without
   invariant enforcement declare `ENFORCES-INVARIANTS: NONE`. New structural pattern not
   present in any prior variation. Targets per-phase invariant traceability.

4. PATH-ISOLATION COP + PROPERTY-COVERAGE-RULE (V-04): V-01 + V-02 combined. Adding COP-14
   live-demonstrates the PROPERTY-COVERAGE-RULE: new property tracked across all three layers
   simultaneously (error code + invariant + COP-14). C-37 and C-38 both reach full PASS.

5. Full synthesis + CROSS-REF invariant linkage (V-05): V-01 + V-02 + V-03 combined, plus
   CROSS-REF rows gain `enforces-invariant:` annotations pointing to INVARIANT-NN identifiers.
   CO-EXTENSIVE DECLARATION extended to name CROSS-REF as a fourth independent verification
   layer. Seeds potential C-39 (CROSS-REF invariant-linkage) and C-40.

---

## V-01 -- PATH-ISOLATION COP assignment axis

**Axis**: Add COP-14 as `PATH-ISOLATION-CHECK [team-slug]:` output block per team in
WRITE-ROLES; INVARIANT-PATH-ISOLATION `cop:` field changes from `(implicit)` to `COP-14`.
**Hypothesis**: INVARIANT-PATH-ISOLATION was the only invariant without a concrete COP-NN
pointer in V-05 R12 (`cop: (implicit in ROLES-WRITTEN receipt paths)`). Assigning COP-14
as a dedicated path-isolation check token emitted per team completes the bidirectional map:
every INVARIANTS entry now carries a concrete `cop:` pointer, and every COP-NN item with
invariant relevance carries an `invariant:` annotation. C-37 reaches full PASS. C-38 remains
PARTIAL (no PROPERTY-COVERAGE-RULE assertion).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. Phases reference codes by name; they do not redefine
violations.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth violation |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count mismatch |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | wrong category assigned |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not domain-derived |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | required field absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role duplicates standard role lens+expertise |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | file written outside path pattern |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE before all receipts pass |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | out-of-scope action in BUILD-VERIFY |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict OPEN |

---

### INVARIANTS

Declared immediately after STRUCTURAL-ERROR-CATALOG. Named identifiers referenced by phases
and by CHECK-OUTPUT PROTOCOL COP-NN annotations.

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
    cop: COP-14 (PATH-ISOLATION-CHECK per team confirms all paths match pattern)

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC
    cop: COP-06 (IA-PHASE-COMPLETE confirms all teams)

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
    cop: COP-08 (ROLES-WRITTEN standard-fields-complete: YES per team)

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS
    cop: COP-05 (PROFILE-GATE uniqueness confirmation)

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
    cop: COP-07 (SPECIALIZATION-GATE gate-verdict: PASS per team)
         COP-09 (ROLES-COMPLETE all-specialization-gates-passed: YES)
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG above and
> this INVARIANTS block are co-extensive. Every named invariant is enforced by one or more
> typed error codes. Every structural error code enforces at least one named invariant.
> The CHECK-OUTPUT PROTOCOL COP-NN items confirm invariant satisfaction at the output level
> (see `cop:` fields above). CATALOG-CLOSURE CLEAN = all INVARIANTS satisfied = all
> relevant COP-NN items emitted with passing values. No invariant exists outside the
> INVARIANTS block. No enforcement code exists outside the STRUCTURAL-ERROR-CATALOG.

---

### CHECK-OUTPUT PROTOCOL

Every check string below MUST appear verbatim in the output. Phases reference COP-NN items
by identifier. COP-NN `invariant:` annotations identify which invariant each item confirms.

| ID | Check String | Phase | Invariant |
|----|-------------|-------|-----------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (per team) |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS (per team) |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (all teams) |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS (co-extensive) |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |
| COP-14 | `PATH-ISOLATION-CHECK [team-slug]: ... verdict: PASS` | WRITE-ROLES | INVARIANT-PATH-ISOLATION (per team) |

COP-07, COP-08, and COP-14 are emitted once per team (N times total). COP-09 is emitted
exactly once. COP-14 is emitted per team immediately after all role files for that team are
written; STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if any path falls outside pattern.

---

### Phase 1: PARSE

ENTRY-GATE: First phase -- no predecessor token required.

Read `org.yaml`. Enumerate groups, teams, area slugs, role slots (IA excluded).

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Exit token: `PARSE-PASS` (COP-01)

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS` (COP-01). If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

Derive headcount table (standard, specialized, IA=1 per team, group totals) and level
distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS` (COP-04)

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS` (COP-04). If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS
required`. Halt.

INVARIANT-PROFILE-UNIQUENESS enforced. For each team, derive category, defended-artifact,
lens-phrase from team domain vocabulary. Apply STRUCTURAL-ERROR:PROFILE-* on violation;
rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS: satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

INVARIANT-IA-PRESENCE enforced. Lens and expertise from team PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC
if generic. Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE: satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) write standard roles, (2) write specialized roles, (3) PATH-ISOLATION-CHECK
(COP-14), (4) SPECIALIZATION-GATE (COP-07), (5) ROLES-WRITTEN receipt (COP-08), (6) IA reference.

INVARIANT-FIELD-COMPLETENESS enforced on every file: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
if any required field absent.

**PATH-ISOLATION-CHECK** (per team, after all role files for team written, before SPECIALIZATION-GATE):
Enforces INVARIANT-PATH-ISOLATION. Confirm every file written for this team is at the expected path.

```
PATH-ISOLATION-CHECK [team-slug]:                   (COP-14 -- INVARIANT-PATH-ISOLATION per team)
  expected-prefix: .roles/{area-slug}/
  files-checked: [N]
  any-path-violation: YES | NO
  verdict: PASS | FAIL
```

If `any-path-violation: YES`: verdict FAIL. Emit STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
for the specific file path(s). Correct path before proceeding.

**SPECIALIZATION-GATE** (per team, after PATH-ISOLATION-CHECK PASS):
Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS. Compare each specialized role's lens and
expertise against every standard role in same team.

```
SPECIALIZATION-GATE [team-slug]:    (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION.
Rewrite. Re-emit SPECIALIZATION-GATE. DO NOT advance to ROLES-WRITTEN (COP-08) until PASS.

```
ROLES-WRITTEN [team-slug]:          (COP-08 -- INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop before next team.

```
ROLES-COMPLETE:                     (COP-09 -- INVARIANT-SPECIALIZATION-DISTINCTNESS all teams)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
  all-path-isolation-checks-passed: YES
```

If `all-specialization-gates-passed: NO`: halt. Per-team re-audit. Re-emit ROLES-COMPLETE
with YES when all gates pass.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

Write `org-chart.md`: ASCII hierarchy (`+--`/`|`, verbatim names, min two levels), headcount
table, level distribution.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.   (COP-10)
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN before TRANSCRIPTION-CLEAR.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

EXCLUSION-MANIFEST:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

CATALOG-CLOSURE (all 17 codes):

```
CATALOG-CLOSURE:                   (COP-12 -- confirms all INVARIANTS satisfied)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN = all named
> INVARIANTS satisfied = all relevant COP-NN items emitted with passing values (COP-05
> through COP-09, COP-12, COP-14). No invariant exists outside the INVARIANTS block; no
> enforcement code exists outside this catalog; no output completeness check exists outside
> the CHECK-OUTPUT PROTOCOL.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

```
BUILD-COMPLETE                                                       (COP-13)
```

`BUILD-COMPLETE` (COP-13) only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`**

Repair chain: PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES -> BUILD-VERIFY.
PROFILE-REDERIVE-COMPLETE required before WRITE-IA begins.

SPECIALIZATION-GATE and PATH-ISOLATION-CHECK re-runs are named, first-class steps in the
WRITE-ROLES re-execution for this area. Prior gate verdicts for all teams in the amended area
are DISCARDED. Both COP-14 and COP-07 MUST be earned fresh per team.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  specialization-gate-rerun:
    teams-reaudited: [N]
    per-team:
      [team-slug]: gate-verdict: PASS | (FAIL -> rewrite -> PASS, rewrites: [N])
      ...
    all-gates-passed: YES
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-02 -- PROPERTY-COVERAGE-RULE axis

**Axis**: CO-EXTENSIVE DECLARATION gains explicit `PROPERTY-COVERAGE-RULE` assertion stating
that adding any new structural property requires entries in all three layers.
**Hypothesis**: V-05 R12's CO-EXTENSIVE DECLARATION named all three layers but did not assert
the positive rule: "Any new structural property MUST be registered in all three layers." The
rubric requires this assertion for C-38 full PASS. Adding the PROPERTY-COVERAGE-RULE to the
declaration closes the gap. C-37 remains PARTIAL (INVARIANT-PATH-ISOLATION still has
`cop: (implicit)` -- no COP-14 added). C-38 reaches full PASS.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. Phases reference codes by name; they do not redefine
violations.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth violation |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count mismatch |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | wrong category assigned |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not domain-derived |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | required field absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role duplicates standard role lens+expertise |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | file written outside path pattern |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE before all receipts pass |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | out-of-scope action in BUILD-VERIFY |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict OPEN |

---

### INVARIANTS

Declared immediately after STRUCTURAL-ERROR-CATALOG. Named identifiers referenced by phases
and by CHECK-OUTPUT PROTOCOL COP-NN annotations.

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
    cop: (implicit in ROLES-WRITTEN receipt paths)

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC
    cop: COP-06 (IA-PHASE-COMPLETE confirms all teams)

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
    cop: COP-08 (ROLES-WRITTEN standard-fields-complete: YES per team)

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS
    cop: COP-05 (PROFILE-GATE uniqueness confirmation)

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
    cop: COP-07 (SPECIALIZATION-GATE gate-verdict: PASS per team)
         COP-09 (ROLES-COMPLETE all-specialization-gates-passed: YES)
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG above and
> this INVARIANTS block are co-extensive. Every named invariant is enforced by one or more
> typed error codes. Every structural error code enforces at least one named invariant.
> The CHECK-OUTPUT PROTOCOL COP-NN items confirm invariant satisfaction at the output level
> (see `cop:` fields above). CATALOG-CLOSURE CLEAN = all INVARIANTS satisfied = all
> relevant COP-NN items emitted with passing values. No invariant exists outside the
> INVARIANTS block. No enforcement code exists outside the STRUCTURAL-ERROR-CATALOG.
> No output completeness check exists outside the CHECK-OUTPUT PROTOCOL.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all three layers: (1) one typed error code in STRUCTURAL-ERROR-CATALOG,
> (2) one named identifier in INVARIANTS with `enforcement:` and `cop:` fields, (3) one
> check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation. A structural property
> tracked by fewer than three layers is incompletely specified and constitutes a gap in the
> co-extensive contract.

---

### CHECK-OUTPUT PROTOCOL

Every check string below MUST appear verbatim in the output. Phases reference COP-NN items
by identifier. COP-NN `invariant:` annotations identify which invariant each item confirms.

| ID | Check String | Phase | Invariant |
|----|-------------|-------|-----------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (per team) |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS (per team) |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (all teams) |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS (co-extensive) |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |

---

### Phase 1: PARSE

ENTRY-GATE: First phase -- no predecessor token required.

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Exit token: `PARSE-PASS` (COP-01)

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS` (COP-01). If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS` (COP-04)

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS` (COP-04). If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS
required`. Halt.

INVARIANT-PROFILE-UNIQUENESS enforced. For each team, derive category, defended-artifact,
lens-phrase. Apply STRUCTURAL-ERROR:PROFILE-* on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS: satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

INVARIANT-IA-PRESENCE enforced. Lens and expertise from team PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC
if generic. Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE: satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles, (3) SPECIALIZATION-GATE (COP-07)
after (2) before ROLES-WRITTEN receipt (COP-08), (4) IA reference.

INVARIANT-PATH-ISOLATION: path validation before each write.
INVARIANT-FIELD-COMPLETENESS: all five fields required on every file.

**SPECIALIZATION-GATE** (per team, after all specialized roles written):
Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS.

```
SPECIALIZATION-GATE [team-slug]:   (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION. Rewrite.
Re-emit. DO NOT advance to COP-08 until PASS.

```
ROLES-WRITTEN [team-slug]:         (COP-08 -- INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If NO: remediation loop before next team.

```
ROLES-COMPLETE:                    (COP-09 -- INVARIANT-SPECIALIZATION-DISTINCTNESS all teams)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
```

If NO: halt. Per-team re-audit. Re-emit ROLES-COMPLETE with YES when all gates pass.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.   (COP-10)
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN before TRANSCRIPTION-CLEAR.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

EXCLUSION-MANIFEST:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

```
CATALOG-CLOSURE:                   (COP-12 -- confirms all INVARIANTS satisfied)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]
    resolved-by:  [action taken]
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN = all named
> INVARIANTS satisfied = all relevant COP-NN items emitted with passing values. No invariant
> exists outside the INVARIANTS block. No enforcement code exists outside this catalog.
> No output completeness check exists outside the CHECK-OUTPUT PROTOCOL.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all three layers: (1) one typed error code in STRUCTURAL-ERROR-CATALOG,
> (2) one named identifier in INVARIANTS with `enforcement:` and `cop:` fields, (3) one
> check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation. A structural property
> tracked by fewer than three layers is incompletely specified.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

```
BUILD-COMPLETE                                                       (COP-13)
```

`BUILD-COMPLETE` (COP-13) only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`** -- PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES (includes
SPECIALIZATION-GATE per team) -> BUILD-VERIFY. PROFILE-REDERIVE-COMPLETE required before
WRITE-IA.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  specialization-gate-rerun:
    teams-reaudited: [N]
    per-team:
      [team-slug]: gate-verdict: PASS | (FAIL -> rewrite -> PASS, rewrites: [N])
      ...
    all-gates-passed: YES
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-03 -- Phase ENFORCES-INVARIANTS annotation axis

**Axis**: Each phase body opens with `ENFORCES-INVARIANTS:` naming which INVARIANT-NN
identifiers it enforces; phases without invariant enforcement declare `ENFORCES-INVARIANTS: NONE`.
**Hypothesis**: Currently, the INVARIANTS block declares which phases enforce each invariant
indirectly through `cop:` pointers, but no phase body declares which invariants it is
responsible for. A reviewer can't determine per-phase invariant responsibility without reading
all phase bodies and the INVARIANTS block together. Adding `ENFORCES-INVARIANTS:` per phase
makes invariant residency auditable at a glance: scan the phase list and see which invariants
each phase owns. New structural pattern -- not present in any prior variation. C-37 remains
PARTIAL (INVARIANT-PATH-ISOLATION `cop:` still implicit). C-38 remains PARTIAL (no
PROPERTY-COVERAGE-RULE). Seeds potential C-39.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth violation |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count mismatch |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | wrong category assigned |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not domain-derived |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | required field absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role duplicates standard role lens+expertise |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | file written outside path pattern |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE before all receipts pass |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | out-of-scope action in BUILD-VERIFY |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict OPEN |

---

### INVARIANTS

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
    cop: (implicit in ROLES-WRITTEN receipt paths)

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC
    cop: COP-06 (IA-PHASE-COMPLETE confirms all teams)

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
    cop: COP-08 (ROLES-WRITTEN standard-fields-complete: YES per team)

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS
    cop: COP-05 (PROFILE-GATE uniqueness confirmation)

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
    cop: COP-07 (SPECIALIZATION-GATE gate-verdict: PASS per team)
         COP-09 (ROLES-COMPLETE all-specialization-gates-passed: YES)
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG and this
> INVARIANTS block are co-extensive. Every named invariant is enforced by one or more typed
> error codes. Every structural error code enforces at least one named invariant. The
> CHECK-OUTPUT PROTOCOL COP-NN items confirm invariant satisfaction. CATALOG-CLOSURE CLEAN
> = all INVARIANTS satisfied. No invariant exists outside the INVARIANTS block. No enforcement
> code exists outside the STRUCTURAL-ERROR-CATALOG.

---

### CHECK-OUTPUT PROTOCOL

| ID | Check String | Phase | Invariant |
|----|-------------|-------|-----------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (per team) |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS (per team) |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (all teams) |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS (co-extensive) |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |

---

### Phase 1: PARSE

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: First phase -- no predecessor token required.

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Exit token: `PARSE-PASS` (COP-01)

---

### Phase 2: VALIDATE

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `PARSE-PASS` (COP-01). If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS` (COP-04)

---

### Phase 5: PROFILE

ENFORCES-INVARIANTS: INVARIANT-PROFILE-UNIQUENESS

ENTRY-GATE: `CONTRACT-SEAL-PASS` (COP-04). If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS
required`. Halt.

For each team, derive category, defended-artifact, lens-phrase from team domain vocabulary.
Apply STRUCTURAL-ERROR:PROFILE-* on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS: satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENFORCES-INVARIANTS: INVARIANT-IA-PRESENCE

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

Lens and expertise from team PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic.
Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE: satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENFORCES-INVARIANTS: INVARIANT-PATH-ISOLATION, INVARIANT-FIELD-COMPLETENESS,
                     INVARIANT-SPECIALIZATION-DISTINCTNESS

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles -- SPECIALIZATION-GATE (COP-07)
after (2) before ROLES-WRITTEN receipt (COP-08), (3) IA reference.

INVARIANT-PATH-ISOLATION: path validation before each write.
INVARIANT-FIELD-COMPLETENESS: all five fields required on every file.

**SPECIALIZATION-GATE** (per team, after all specialized roles written):

```
SPECIALIZATION-GATE [team-slug]:   (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION. Rewrite.
Re-emit. DO NOT advance to COP-08 until PASS.

```
ROLES-WRITTEN [team-slug]:         (COP-08 -- INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If NO: remediation loop before next team.

```
ROLES-COMPLETE:                    (COP-09 -- INVARIANT-SPECIALIZATION-DISTINCTNESS all teams)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
```

If NO: halt. Per-team re-audit. Re-emit with YES when all pass.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.   (COP-10)
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN before TRANSCRIPTION-CLEAR.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENFORCES-INVARIANTS: NONE (verifies all; enforces none)

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

EXCLUSION-MANIFEST:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

```
CATALOG-CLOSURE:                   (COP-12 -- confirms all INVARIANTS satisfied)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]
    resolved-by:  [action taken]
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN = all named
> INVARIANTS satisfied = all relevant COP-NN items emitted with passing values. No invariant
> exists outside the INVARIANTS block; no enforcement code exists outside this catalog; no
> output completeness check exists outside the CHECK-OUTPUT PROTOCOL.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

```
BUILD-COMPLETE                                                       (COP-13)
```

`BUILD-COMPLETE` (COP-13) only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`** -- PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES (includes
SPECIALIZATION-GATE per team) -> BUILD-VERIFY. PROFILE-REDERIVE-COMPLETE required before
WRITE-IA.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  specialization-gate-rerun:
    teams-reaudited: [N]
    per-team:
      [team-slug]: gate-verdict: PASS | (FAIL -> rewrite -> PASS, rewrites: [N])
      ...
    all-gates-passed: YES
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-04 -- PATH-ISOLATION COP + PROPERTY-COVERAGE-RULE (combination)

**Axes**: V-01 PATH-ISOLATION COP assignment + V-02 PROPERTY-COVERAGE-RULE combined.
**Hypothesis**: Adding COP-14 (PATH-ISOLATION-CHECK per team) gives INVARIANT-PATH-ISOLATION a
concrete `cop:` pointer, completing the bidirectional map for all five invariants (C-37 full
PASS). Adding the PROPERTY-COVERAGE-RULE to the CO-EXTENSIVE DECLARATION provides the explicit
rule-assertion required by C-38. More importantly: COP-14 is the first NEW structural property
added in R13, and its addition live-demonstrates the PROPERTY-COVERAGE-RULE -- it receives an
error code (already present: PATH-ISOLATION-VIOLATION), a named invariant (INVARIANT-PATH-ISOLATION),
and a COP item (COP-14) simultaneously, showing the rule in action. This makes the declaration
self-referentially complete. C-37 PASS + C-38 PASS. ENFORCES-INVARIANTS (V-03 axis) absent.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth violation |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count mismatch |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | wrong category assigned |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not domain-derived |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | required field absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role duplicates standard role lens+expertise |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | file written outside path pattern |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE before all receipts pass |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | out-of-scope action in BUILD-VERIFY |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict OPEN |

---

### INVARIANTS

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
    cop: COP-14 (PATH-ISOLATION-CHECK per team confirms all paths match pattern)

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC
    cop: COP-06 (IA-PHASE-COMPLETE confirms all teams)

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
    cop: COP-08 (ROLES-WRITTEN standard-fields-complete: YES per team)

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS
    cop: COP-05 (PROFILE-GATE uniqueness confirmation)

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
    cop: COP-07 (SPECIALIZATION-GATE gate-verdict: PASS per team)
         COP-09 (ROLES-COMPLETE all-specialization-gates-passed: YES)
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG above and
> this INVARIANTS block are co-extensive. Every named invariant is enforced by one or more
> typed error codes. Every structural error code enforces at least one named invariant.
> The CHECK-OUTPUT PROTOCOL COP-NN items confirm invariant satisfaction at the output level
> (see `cop:` fields above). CATALOG-CLOSURE CLEAN = all INVARIANTS satisfied = all
> relevant COP-NN items emitted with passing values. No invariant exists outside the
> INVARIANTS block. No enforcement code exists outside the STRUCTURAL-ERROR-CATALOG.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all three layers: (1) one typed error code in STRUCTURAL-ERROR-CATALOG,
> (2) one named identifier in INVARIANTS with `enforcement:` and `cop:` fields, (3) one
> check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation. A structural property
> tracked by fewer than three layers is incompletely specified and constitutes a gap in the
> co-extensive contract. COP-14 (PATH-ISOLATION-CHECK) was added in accordance with this rule:
> CATALOG entry (PATH-ISOLATION-VIOLATION), INVARIANTS entry (INVARIANT-PATH-ISOLATION with
> `cop: COP-14`), and COP entry (COP-14 with `invariant: INVARIANT-PATH-ISOLATION`) all present.

---

### CHECK-OUTPUT PROTOCOL

| ID | Check String | Phase | Invariant |
|----|-------------|-------|-----------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (per team) |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS (per team) |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (all teams) |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS (co-extensive) |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |
| COP-14 | `PATH-ISOLATION-CHECK [team-slug]: ... verdict: PASS` | WRITE-ROLES | INVARIANT-PATH-ISOLATION (per team) |

COP-07, COP-08, and COP-14 emitted once per team. COP-09 emitted once. COP-14 emitted after
all role files for a team are written; before SPECIALIZATION-GATE.

---

### Phase 1: PARSE

ENTRY-GATE: First phase -- no predecessor token required.

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Exit token: `PARSE-PASS` (COP-01)

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS` (COP-01). If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS` (COP-04)

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS` (COP-04). If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS
required`. Halt.

INVARIANT-PROFILE-UNIQUENESS enforced. For each team, derive category, defended-artifact,
lens-phrase. Apply STRUCTURAL-ERROR:PROFILE-* on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS: satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

INVARIANT-IA-PRESENCE enforced. Lens and expertise from team PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC
if generic. Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE: satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles, (3) PATH-ISOLATION-CHECK (COP-14),
(4) SPECIALIZATION-GATE (COP-07), (5) ROLES-WRITTEN receipt (COP-08), (6) IA reference.

INVARIANT-FIELD-COMPLETENESS: all five fields required on every file.

**PATH-ISOLATION-CHECK** (per team, after all role files written for team):
Enforces INVARIANT-PATH-ISOLATION.

```
PATH-ISOLATION-CHECK [team-slug]:   (COP-14 -- INVARIANT-PATH-ISOLATION per team)
  expected-prefix: .roles/{area-slug}/
  files-checked: [N]
  any-path-violation: YES | NO
  verdict: PASS | FAIL
```

If `any-path-violation: YES`: Emit STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION. Correct.
DO NOT advance to SPECIALIZATION-GATE until verdict PASS.

**SPECIALIZATION-GATE** (per team, after PATH-ISOLATION-CHECK PASS):
Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS.

```
SPECIALIZATION-GATE [team-slug]:    (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION. Rewrite.
Re-emit. DO NOT advance to COP-08 until PASS.

```
ROLES-WRITTEN [team-slug]:          (COP-08 -- INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If NO: remediation loop before next team.

```
ROLES-COMPLETE:                     (COP-09 -- INVARIANT-SPECIALIZATION-DISTINCTNESS all teams)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
  all-path-isolation-checks-passed: YES
```

If `all-specialization-gates-passed: NO`: halt. Per-team re-audit. Re-emit with YES when all pass.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.   (COP-10)
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN before TRANSCRIPTION-CLEAR.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

EXCLUSION-MANIFEST:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

```
CATALOG-CLOSURE:                   (COP-12 -- confirms all INVARIANTS satisfied)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]
    resolved-by:  [action taken]
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN = all named
> INVARIANTS satisfied = all relevant COP-NN items emitted with passing values (COP-05
> through COP-09, COP-12, COP-14). No invariant exists outside the INVARIANTS block; no
> enforcement code exists outside this catalog; no output completeness check exists outside
> the CHECK-OUTPUT PROTOCOL.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all three layers: (1) one typed error code in STRUCTURAL-ERROR-CATALOG,
> (2) one named identifier in INVARIANTS with `enforcement:` and `cop:` fields, (3) one
> check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation. COP-14 demonstrates this
> rule: PATH-ISOLATION-VIOLATION (catalog) + INVARIANT-PATH-ISOLATION (invariants) + COP-14
> (protocol) all registered simultaneously.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

```
BUILD-COMPLETE                                                       (COP-13)
```

`BUILD-COMPLETE` (COP-13) only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`**

Repair chain: PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES -> BUILD-VERIFY.
PROFILE-REDERIVE-COMPLETE required before WRITE-IA begins.

PATH-ISOLATION-CHECK (COP-14) and SPECIALIZATION-GATE (COP-07) re-runs are named, first-class
steps in the WRITE-ROLES re-execution. Prior verdicts DISCARDED for amended area; both MUST
be earned fresh per team.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  specialization-gate-rerun:
    teams-reaudited: [N]
    per-team:
      [team-slug]: gate-verdict: PASS | (FAIL -> rewrite -> PASS, rewrites: [N])
      ...
    all-gates-passed: YES
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-05 -- Full synthesis + CROSS-REF invariant linkage

**Axes**: V-01 + V-02 + V-03 combined, plus CROSS-REF rows gain `enforces-invariant:` annotations;
CO-EXTENSIVE DECLARATION extended to name CROSS-REF as a fourth independent verification layer.
**Hypothesis**: With all three single-axis improvements in place (COP-14 completing C-37,
PROPERTY-COVERAGE-RULE completing C-38, ENFORCES-INVARIANTS per phase), a fourth verification
layer becomes visible: BUILD-VERIFY CROSS-REF rows verify correctness properties that correspond
directly to named invariants. Annotating each CROSS-REF row with `enforces-invariant:` creates
a structural link from the terminal verification step back to the INVARIANTS block. This link
is currently absent -- CROSS-REF rows verify count/path/table properties but do not explicitly
claim invariant coverage. Adding this annotation and extending the CO-EXTENSIVE DECLARATION to
name CROSS-REF as a fourth layer seeds C-39. V-05 is the only variation predicted to achieve
full PASS on C-37, C-38, and the new ENFORCES-INVARIANTS pattern simultaneously.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth violation |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count mismatch |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | wrong category assigned |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not domain-derived |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | required field absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role duplicates standard role lens+expertise |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | file written outside path pattern |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE before all receipts pass |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | out-of-scope action in BUILD-VERIFY |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict OPEN |

---

### INVARIANTS

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
    cop: COP-14 (PATH-ISOLATION-CHECK per team confirms all paths match pattern)

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC
    cop: COP-06 (IA-PHASE-COMPLETE confirms all teams)

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING
    cop: COP-08 (ROLES-WRITTEN standard-fields-complete: YES per team)

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS
    cop: COP-05 (PROFILE-GATE uniqueness confirmation)

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
    cop: COP-07 (SPECIALIZATION-GATE gate-verdict: PASS per team)
         COP-09 (ROLES-COMPLETE all-specialization-gates-passed: YES)
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG, this
> INVARIANTS block, and the CHECK-OUTPUT PROTOCOL are co-extensive: every named invariant is
> enforced by one or more typed error codes, confirmed by one or more COP-NN items, and
> independently verified by one or more CROSS-REF rows in BUILD-VERIFY. CATALOG-CLOSURE CLEAN
> = all INVARIANTS satisfied = all relevant COP-NN items emitted with passing values = all
> relevant CROSS-REF rows MATCH. No invariant exists outside the INVARIANTS block; no
> enforcement code outside the STRUCTURAL-ERROR-CATALOG; no output completeness check outside
> the CHECK-OUTPUT PROTOCOL; no terminal verification outside CROSS-REF.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all four layers: (1) one typed error code in STRUCTURAL-ERROR-CATALOG,
> (2) one named identifier in INVARIANTS with `enforcement:` and `cop:` fields, (3) one
> check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation, (4) one row in BUILD-VERIFY
> CROSS-REF with `enforces-invariant:` annotation. A structural property tracked by fewer
> than four layers is incompletely specified.

---

### CHECK-OUTPUT PROTOCOL

| ID | Check String | Phase | Invariant |
|----|-------------|-------|-----------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (per team) |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS (per team) |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS (all teams) |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS (co-extensive) |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |
| COP-14 | `PATH-ISOLATION-CHECK [team-slug]: ... verdict: PASS` | WRITE-ROLES | INVARIANT-PATH-ISOLATION (per team) |

---

### Phase 1: PARSE

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: First phase -- no predecessor token required.

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Exit token: `PARSE-PASS` (COP-01)

---

### Phase 2: VALIDATE

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `PARSE-PASS` (COP-01). If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS` (COP-04)

---

### Phase 5: PROFILE

ENFORCES-INVARIANTS: INVARIANT-PROFILE-UNIQUENESS

ENTRY-GATE: `CONTRACT-SEAL-PASS` (COP-04). If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS
required`. Halt.

For each team, derive category, defended-artifact, lens-phrase. Apply STRUCTURAL-ERROR:PROFILE-*
on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS: satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENFORCES-INVARIANTS: INVARIANT-IA-PRESENCE

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

Lens and expertise from team PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic.
Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE: satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENFORCES-INVARIANTS: INVARIANT-PATH-ISOLATION, INVARIANT-FIELD-COMPLETENESS,
                     INVARIANT-SPECIALIZATION-DISTINCTNESS

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles, (3) PATH-ISOLATION-CHECK (COP-14),
(4) SPECIALIZATION-GATE (COP-07), (5) ROLES-WRITTEN receipt (COP-08), (6) IA reference.

INVARIANT-FIELD-COMPLETENESS: all five fields required on every file.

**PATH-ISOLATION-CHECK** (per team, after all role files written):
Enforces INVARIANT-PATH-ISOLATION.

```
PATH-ISOLATION-CHECK [team-slug]:   (COP-14 -- INVARIANT-PATH-ISOLATION per team)
  expected-prefix: .roles/{area-slug}/
  files-checked: [N]
  any-path-violation: YES | NO
  verdict: PASS | FAIL
```

If `any-path-violation: YES`: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION. Correct.
DO NOT advance to SPECIALIZATION-GATE until verdict PASS.

**SPECIALIZATION-GATE** (per team, after PATH-ISOLATION-CHECK PASS):
Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS.

```
SPECIALIZATION-GATE [team-slug]:    (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION. Rewrite.
Re-emit. DO NOT advance to COP-08 until PASS.

```
ROLES-WRITTEN [team-slug]:          (COP-08 -- INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If NO: remediation loop before next team.

```
ROLES-COMPLETE:                     (COP-09 -- INVARIANT-SPECIALIZATION-DISTINCTNESS all teams)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
  all-path-isolation-checks-passed: YES
```

If `all-specialization-gates-passed: NO`: halt. Per-team re-audit. Re-emit with YES when all pass.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENFORCES-INVARIANTS: NONE

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.   (COP-10)
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN before TRANSCRIPTION-CLEAR.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENFORCES-INVARIANTS: NONE (terminal verification layer -- verifies all INVARIANTS via CROSS-REF)

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

EXCLUSION-MANIFEST:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
    enforces-invariant: INVARIANT-FIELD-COMPLETENESS (file per slot)
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
    enforces-invariant: INVARIANT-IA-PRESENCE (one IA per team)
  dir-match:      all files in .roles/{area-slug}/ -- MATCH | MISMATCH
    enforces-invariant: INVARIANT-PATH-ISOLATION (all files in correct directory)
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
    enforces-invariant: (contract fidelity -- no INVARIANT-NN, structural only)
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
    enforces-invariant: INVARIANT-FIELD-COMPLETENESS (all teams receipted)
```

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

```
CATALOG-CLOSURE:                   (COP-12 -- confirms all INVARIANTS satisfied)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]
    resolved-by:  [action taken]
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG, this
> INVARIANTS block, the CHECK-OUTPUT PROTOCOL, and CROSS-REF constitute four independent
> verification layers. Every named invariant is (1) enforced by one or more typed error codes
> in the catalog, (2) confirmed by one or more COP-NN items in the protocol, and (3)
> independently verified by one or more annotated CROSS-REF rows in BUILD-VERIFY. CATALOG-CLOSURE
> CLEAN = all INVARIANTS satisfied = all relevant COP-NN items emitted with passing values =
> all relevant CROSS-REF rows MATCH. No invariant exists outside the INVARIANTS block; no
> enforcement code outside the STRUCTURAL-ERROR-CATALOG; no output completeness check outside
> the CHECK-OUTPUT PROTOCOL; no terminal verification row outside CROSS-REF.
>
> **PROPERTY-COVERAGE-RULE**: Any new structural property introduced to this build protocol
> MUST be registered in all four layers simultaneously: (1) one typed error code in
> STRUCTURAL-ERROR-CATALOG, (2) one named identifier in INVARIANTS with `enforcement:` and
> `cop:` fields, (3) one check item in CHECK-OUTPUT PROTOCOL with `invariant:` annotation,
> (4) one CROSS-REF row in BUILD-VERIFY with `enforces-invariant:` annotation. A structural
> property tracked by fewer than four layers is incompletely specified and constitutes a gap
> in the co-extensive contract.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

```
BUILD-COMPLETE                                                       (COP-13)
```

`BUILD-COMPLETE` (COP-13) only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`**

Repair chain: PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES -> BUILD-VERIFY.
PROFILE-REDERIVE-COMPLETE required before WRITE-IA begins.

PATH-ISOLATION-CHECK (COP-14) and SPECIALIZATION-GATE (COP-07) re-runs are named, first-class
steps in the WRITE-ROLES re-execution for the amended area. Prior verdicts DISCARDED; both
MUST be earned fresh per team. CROSS-REF `enforces-invariant:` annotations are re-evaluated
in BUILD-VERIFY for the amended area.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  specialization-gate-rerun:
    teams-reaudited: [N]
    per-team:
      [team-slug]: gate-verdict: PASS | (FAIL -> rewrite -> PASS, rewrites: [N])
      ...
    all-gates-passed: YES
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

The `specialization-gate-rerun:` block is REQUIRED in every `--area` AMEND-CHAIN-COMPLETE.

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## R13 Variation Summary

| Variation | Axis | C-37 | C-38 | ENFORCES-INVARIANTS | Notes |
|-----------|------|------|------|---------------------|-------|
| V-01 | PATH-ISOLATION COP assignment | PASS | PARTIAL | absent | COP-14 completes bidirectional map; no PROPERTY-COVERAGE-RULE |
| V-02 | PROPERTY-COVERAGE-RULE | PARTIAL | PASS | absent | Explicit rule added; INVARIANT-PATH-ISOLATION `cop:` still implicit |
| V-03 | Phase ENFORCES-INVARIANTS | PARTIAL | PARTIAL | PASS | New per-phase annotation; others unchanged |
| V-04 | PATH-ISOLATION COP + COVERAGE-RULE | PASS | PASS | absent | COP-14 live-demonstrates PROPERTY-COVERAGE-RULE |
| V-05 | Full synthesis + CROSS-REF linkage | PASS | PASS | PASS | CROSS-REF gains `enforces-invariant:` annotations; four-layer CO-EXTENSIVE DECLARATION seeds C-39 |

**Predicted discriminator**: C-37 separates V-01/V-04/V-05 (PASS) from V-02/V-03 (PARTIAL).
C-38 separates V-02/V-04/V-05 (PASS) from V-01/V-03 (PARTIAL).
ENFORCES-INVARIANTS criterion (potential C-39) separates V-03/V-05 from all others.
V-05 is the only variation predicted to demonstrate all three patterns simultaneously.

**New pattern candidates for rubric v12**:
- C-39 (Phase ENFORCES-INVARIANTS annotation): Each phase declares which INVARIANT-NN
  identifiers it enforces; phases without enforcement declare NONE. Converts per-phase
  invariant responsibility from implicit (derivable from INVARIANTS `cop:` + phase body)
  to explicit (readable from phase header). V-03 and V-05 demonstrate.
- C-40 (CROSS-REF invariant-linkage): BUILD-VERIFY CROSS-REF rows carry `enforces-invariant:`
  annotations pointing to INVARIANT-NN identifiers. Extends bidirectional traceability to the
  terminal verification step, making CROSS-REF a fourth independent verification layer.
  V-05 demonstrates. Four-layer CO-EXTENSIVE DECLARATION is the necessary companion declaration.
