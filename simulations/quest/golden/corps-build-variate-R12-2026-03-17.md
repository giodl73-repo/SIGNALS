---
skill: quest-variate
skill_target: corps-build
round: 12
date: 2026-03-17
rubric_version: 10
r11_scorecard: (pending)
---

# Variate R12 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 12. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R11 excellence signals are now baseline criteria in rubric v10:
- C-34: SPECIALIZATION-GATE per-team comparison block in WRITE-ROLES phase
- C-35: ROLES-COMPLETE `all-specialization-gates-passed: YES|NO` field
- C-36: AMEND --area SPECIALIZATION-GATE re-run named in repair chain

R11 persistent PARTIALs targeted by R12:
- C-11: PARTIAL across all R11 variations -- STRUCTURAL-ERROR-CATALOG serves the invariant
  function but no dedicated `INVARIANTS:` labeled block with distinct named identifiers paired
  to enforcement codes. V-01 (R11) achieved full PASS via INVARIANTS block; that pattern must
  now be combined with the SPECIALIZATION-GATE baseline from V-03 (R11).
- C-15: PARTIAL across all R11 variations -- EXCLUSION-MANIFEST covers excluded-output
  content but no named `CHECK-OUTPUT PROTOCOL:` section; phases do not reference COP-NN
  identifiers. V-02 (R11) achieved full PASS via COP-NN; that pattern must be combined
  with the SPECIALIZATION-GATE baseline.
- C-36: PARTIAL in V-03 (R11) -- AMEND --area names SPECIALIZATION-GATE parenthetically
  ("includes SPECIALIZATION-GATE per team") but AMEND-CHAIN-COMPLETE has no per-team
  gate-rerun field, making the re-audit unauditable at output level.

R12 variation axes:

1. INVARIANTS-block (V-01): Dedicated `INVARIANTS:` block immediately after
   STRUCTURAL-ERROR-CATALOG with five named identifiers (INVARIANT-PATH-ISOLATION,
   INVARIANT-IA-PRESENCE, INVARIANT-FIELD-COMPLETENESS, INVARIANT-PROFILE-UNIQUENESS,
   INVARIANT-SPECIALIZATION-DISTINCTNESS) each paired to enforcement codes. INVARIANTS block
   and STRUCTURAL-ERROR-CATALOG declared co-extensive. Phase 7 SPECIALIZATION-GATE references
   INVARIANT-SPECIALIZATION-DISTINCTNESS by ID. Targets C-11 + C-34 together.

2. CHECK-OUTPUT-PROTOCOL (V-02): Dedicated `CHECK-OUTPUT PROTOCOL:` section after
   STRUCTURAL-ERROR-CATALOG enumerating COP-01 through COP-13. Each phase references its
   COP-NN items by identifier. SPECIALIZATION-GATE gate-verdict and ROLES-COMPLETE
   specialization-gates field are COP items (COP-07 and COP-09). Targets C-15 + C-34/C-35.

3. AMEND-chain precision (V-03): AMEND --area description names SPECIALIZATION-GATE re-run
   as a first-class step (prior gate verdicts discarded, earned fresh). AMEND-CHAIN-COMPLETE
   gains explicit `specialization-gate-rerun:` field with per-team audit results. No INVARIANTS
   block, no COP section added. Targets C-36 specifically.

4. INVARIANTS + CHECK-OUTPUT PROTOCOL (V-04): V-01 + V-02 combined. Full C-11 + C-15
   pass with SPECIALIZATION-GATE carried through both lenses.

5. Full synthesis (V-05): V-01 + V-02 + V-03 combined. CO-EXTENSIVE DECLARATION
   strengthened to include SPECIALIZATION-GATE as an invariant enforcement event.
   COP-07/COP-09 reference the INVARIANT-SPECIALIZATION-DISTINCTNESS identifier.
   AMEND-CHAIN-COMPLETE enumerates gate-rerun per team. Targets C-11, C-15, C-36 together.

---

## V-01 -- INVARIANTS-block axis

**Axis**: Dedicated INVARIANTS block with named identifiers paired to enforcement codes;
SPECIALIZATION-GATE references INVARIANT-SPECIALIZATION-DISTINCTNESS by ID.
**Hypothesis**: Adding a dedicated `INVARIANTS:` block co-extensive with the
STRUCTURAL-ERROR-CATALOG -- listing five named invariant identifiers each paired to
their enforcement code(s) -- resolves C-11 PARTIAL. Pairing INVARIANT-SPECIALIZATION-DISTINCTNESS
to STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION makes SPECIALIZATION-GATE (C-34) directly
traceable to a named invariant rather than to a catalog entry alone. C-15 remains PARTIAL
(no COP-NN section). C-36 remains PARTIAL (AMEND chain not extended).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
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

Declared immediately after STRUCTURAL-ERROR-CATALOG. Named invariant identifiers are
referenced by phases that enforce them. Each invariant is paired to its enforcement code(s).

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .craft/roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG above and
> this INVARIANTS block are co-extensive. Every named invariant is enforced by one or more
> typed error codes in the catalog. Every structural error code enforces at least one named
> invariant. No invariant exists outside the INVARIANTS block. No enforcement code exists
> outside the STRUCTURAL-ERROR-CATALOG.

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

Exit token: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

Check duplicate slugs, nesting depth, parent refs.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate found. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting depth exceeded. Halt.

Exit token: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

Derive headcount table (standard, specialized, IA=1 per team, group totals) and level
distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

```
TABLE-CLOSED:
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

Lock contract. No structural changes permitted after CONTRACT-SEAL-PASS.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`.
Halt.

For each team, derive category, defended-artifact, lens-phrase from the team's domain
vocabulary. Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite before next team.
INVARIANT-PROFILE-UNIQUENESS: all lens-phrases must be distinct across teams.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

When all teams PASS:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`. Lens and expertise from
team's PROFILE. INVARIANT-IA-PRESENCE enforced: STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic.
Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`.
Halt.

Sequence per team: (1) standard roles, (2) specialized roles, (3) IA reference.

INVARIANT-PATH-ISOLATION enforced before each write: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION
if path mismatch. INVARIANT-FIELD-COMPLETENESS enforced on every file: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING if any required field absent.

**SPECIALIZATION-GATE** (per team, after all specialized roles written, before ROLES-WRITTEN
receipt): Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS. For each specialized role, compare
its `lens` and `expertise` against every standard role in the same team. Record per-role result.

```
SPECIALIZATION-GATE [team-slug]:
  (enforces: INVARIANT-SPECIALIZATION-DISTINCTNESS)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. Emit STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
for the specific role slug. Rewrite that specialized role. Re-emit SPECIALIZATION-GATE. DO NOT
advance to ROLES-WRITTEN receipt until gate-verdict is PASS.

ROLES-WRITTEN receipt per team (after SPECIALIZATION-GATE PASS):

```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop (rewrite -> re-emit receipt -> confirm YES)
before next team. STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE if ROLES-COMPLETE emitted before
all receipts pass.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES`:

```
ROLES-COMPLETE:
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
```

If `all-specialization-gates-passed: NO`: halt. Re-audit each team whose SPECIALIZATION-GATE
verdict is not PASS. Re-emit SPECIALIZATION-GATE per failing team. Rewrite violating roles.
Re-emit ROLES-WRITTEN for affected teams. Only when all gates PASS: re-emit ROLES-COMPLETE
with `all-specialization-gates-passed: YES`.

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

Write `org-chart.md`: ASCII hierarchy (`+--`/`|`, verbatim names from org.yaml, min two
levels), headcount table (Group | Team | Standard | Specialized | IA | Total | Levels), level
distribution.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR.
Halt.

Exit token: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

Single responsibility: verify artifact set against sealed contract.

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
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
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
CATALOG-CLOSURE:
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: This catalog constitutes the complete
> invariants contract for this build. CATALOG-CLOSURE CLEAN = all named invariants in the
> INVARIANTS block satisfied. No invariant exists outside the INVARIANTS block; no enforcement
> code exists outside this catalog.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

Exit token: `BUILD-VERIFY-COMPLETE`

`BUILD-COMPLETE` only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`** -- PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES (includes
SPECIALIZATION-GATE per team) -> BUILD-VERIFY. PROFILE-REDERIVE-COMPLETE required before
WRITE-IA.

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-02 -- CHECK-OUTPUT PROTOCOL axis

**Axis**: Dedicated `CHECK-OUTPUT PROTOCOL:` section after STRUCTURAL-ERROR-CATALOG enumerating
COP-01 through COP-13; each phase references its COP-NN items by identifier; SPECIALIZATION-GATE
gate-verdict and ROLES-COMPLETE specialization-gates field are named COP items.
**Hypothesis**: A named CHECK-OUTPUT PROTOCOL with numbered COP-NN items resolves C-15 PARTIAL
by giving every phase a verifiable check string that must appear in output. COP-07
(SPECIALIZATION-GATE gate-verdict) and COP-09 (ROLES-COMPLETE all-specialization-gates-passed)
make C-34 and C-35 auditable at the protocol level. C-11 remains PARTIAL (no INVARIANTS block).
C-36 remains PARTIAL (AMEND chain not extended).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. Phases reference codes by name; they do not redefine
violations. This catalog constitutes the complete invariants contract for this build.

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

### CHECK-OUTPUT PROTOCOL

Every check string below MUST appear verbatim in the output. Phases reference COP-NN items
by identifier. An output that omits any COP-NN string fails that phase's completeness check.

| ID | Check String (verbatim token or prefix) | Phase | Notes |
|----|------------------------------------------|-------|-------|
| COP-01 | `PARSE-PASS` | PARSE | Exit token |
| COP-02 | `VALIDATE-PASS` | VALIDATE | Exit token |
| COP-03 | `TABLE-CLOSED` | CONTRACT | Exit token |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | Exit token |
| COP-05 | `PROFILE-GATE` | PROFILE | Exit token |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | Exit token |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | One per team; gate-verdict PASS required before ROLES-WRITTEN |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | One per team |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | Terminal; NO blocks exit |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | Required before CHART-WRITTEN |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | Exit token |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | OPEN blocks BUILD-COMPLETE |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | Terminal build token |

Phases emit their COP-NN items as part of normal output. COP-07 and COP-08 are emitted once
per team (N times total where N = team count). COP-09 is emitted exactly once. If COP-09
would emit `all-specialization-gates-passed: NO`, the phase halts and re-audits before
re-emitting COP-09 with YES.

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

Check duplicate slugs, nesting depth, parent refs.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate found. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting depth exceeded. Halt.

Exit token: `VALIDATE-PASS` (COP-02)

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`.
Halt.

Derive headcount table (standard, specialized, IA=1 per team, group totals) and level
distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

```
TABLE-CLOSED:                                   (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`.
Halt.

Lock contract. No structural changes permitted after CONTRACT-SEAL-PASS.

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

For each team, derive category, defended-artifact, lens-phrase from team's domain vocabulary.
Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

When all teams PASS:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.   (COP-05)
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`.
Halt.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`. Lens and expertise from
team's PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic. Rewrite until non-transplantable
check passes.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles -- SPECIALIZATION-GATE (COP-07)
after (2) before ROLES-WRITTEN receipt (COP-08), (3) IA reference.

Path validation before each write (STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if mismatch).
All five fields required (STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING if absent).

**SPECIALIZATION-GATE** (per team, after all specialized roles written for this team):

For each specialized role, compare its `lens` and `expertise` against every standard role in
the same team. Record the comparison result per specialized role.

```
SPECIALIZATION-GATE [team-slug]:                                     (COP-07)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. Emit STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
for the specific role slug. Rewrite that specialized role. Re-emit SPECIALIZATION-GATE. DO NOT
advance to ROLES-WRITTEN receipt (COP-08) until gate-verdict is PASS.

ROLES-WRITTEN receipt per team (after SPECIALIZATION-GATE PASS):

```
ROLES-WRITTEN [team-slug]:                                           (COP-08)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop (rewrite -> re-emit -> confirm YES) before
next team.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES`:

```
ROLES-COMPLETE:                                                      (COP-09)
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
```

If `all-specialization-gates-passed: NO`: halt. Per-team re-audit of all failing SPECIALIZATION-GATEs
before re-emitting ROLES-COMPLETE (COP-09) with YES.

Exit token: `ROLES-COMPLETE` (COP-09)

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`.
Halt.

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

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR.
Halt.

```
CHART-WRITTEN                                                        (COP-11)
```

Exit token: `CHART-WRITTEN` (COP-11)

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`.
Halt.

Single responsibility: verify artifact set against sealed contract.

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
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
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
CATALOG-CLOSURE:                                                     (COP-12)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

> **C-33 CATALOG-CLOSURE DECLARATION**: This catalog constitutes the complete invariants
> contract for this build. All structural invariants are encoded as typed error codes.
> No invariant exists outside the catalog. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

Exit token: `BUILD-VERIFY-COMPLETE`

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
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-03 -- AMEND-chain precision axis

**Axis**: AMEND --area names SPECIALIZATION-GATE re-run as a first-class step; prior gate
verdicts discarded for the amended area; AMEND-CHAIN-COMPLETE gains per-team gate-rerun field.
**Hypothesis**: Upgrading the AMEND --area description to explicitly discard prior
SPECIALIZATION-GATE verdicts (earned fresh, not inherited) and adding a
`specialization-gate-rerun:` field to AMEND-CHAIN-COMPLETE closes the C-36 PARTIAL gap:
the re-audit is now auditable at the output level rather than implied by the parenthetical
"includes SPECIALIZATION-GATE per team." C-11 remains PARTIAL (no INVARIANTS block). C-15
remains PARTIAL (no COP-NN section).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. Phases reference codes by name; they do not redefine
violations. This catalog constitutes the complete invariants contract for this build.

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

Exit token: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

Check duplicate slugs, nesting depth, parent refs.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG if duplicate found. Halt.
STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION if nesting depth exceeded. Halt.

Exit token: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

Derive headcount table (standard, specialized, IA=1 per team, group totals) and level
distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

```
TABLE-CLOSED:
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

Lock contract. No structural changes permitted after CONTRACT-SEAL-PASS.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`.
Halt.

For each team, derive category, defended-artifact, lens-phrase from team's domain vocabulary.
Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

When all teams PASS:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`. Lens and expertise from
team's PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic. Rewrite until non-transplantable
check passes.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`.
Halt.

Sequence per team: (1) standard roles, (2) specialized roles -- SPECIALIZATION-GATE after (2)
before ROLES-WRITTEN receipt, (3) IA reference.

Path validation before each write (STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if mismatch).
All five fields required (STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING if absent).

**SPECIALIZATION-GATE** (per team, after all specialized roles written for this team):

For each specialized role, compare its `lens` and `expertise` against every standard role in
the same team. Record the comparison result per specialized role.

```
SPECIALIZATION-GATE [team-slug]:
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. Emit STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
for the specific role slug. Rewrite that specialized role. Re-emit SPECIALIZATION-GATE. DO NOT
advance to ROLES-WRITTEN receipt until gate-verdict is PASS.

ROLES-WRITTEN receipt per team (after SPECIALIZATION-GATE PASS):

```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop (rewrite -> re-emit -> confirm YES) before
next team.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES`:

```
ROLES-COMPLETE:
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES | NO
```

If `all-specialization-gates-passed: NO`: halt. Re-audit each team whose gate-verdict is not
PASS. Re-emit SPECIALIZATION-GATE per failing team. Rewrite violating roles. Re-emit
ROLES-WRITTEN for affected teams. Re-emit ROLES-COMPLETE only when all gates PASS.

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

Write `org-chart.md`: ASCII hierarchy (`+--`/`|`, verbatim names, min two levels), headcount
table, level distribution.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR.
Halt.

Exit token: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

Single responsibility: verify artifact set against sealed contract.

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
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
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
CATALOG-CLOSURE:
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

> **C-33 CATALOG-CLOSURE DECLARATION**: This catalog constitutes the complete invariants
> contract for this build. All structural invariants are encoded as typed error codes.
> No invariant exists outside the catalog. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

Exit token: `BUILD-VERIFY-COMPLETE`

`BUILD-COMPLETE` only if CATALOG-CLOSURE CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`**

Repair chain: PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES -> BUILD-VERIFY.
PROFILE-REDERIVE-COMPLETE required before WRITE-IA begins.

SPECIALIZATION-GATE re-run is a named step in the WRITE-ROLES re-execution for this area.
Prior SPECIALIZATION-GATE verdicts for all teams in the amended area are DISCARDED. Gate
verdicts for the amended area MUST be earned fresh -- they cannot be inherited from the
original build. DO NOT advance to ROLES-WRITTEN receipt per team until the fresh
SPECIALIZATION-GATE emits gate-verdict: PASS for that team.

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

The `specialization-gate-rerun:` block is REQUIRED in every AMEND-CHAIN-COMPLETE for
`--area`. An AMEND-CHAIN-COMPLETE that omits `specialization-gate-rerun:` is incomplete.

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-04 -- INVARIANTS + CHECK-OUTPUT PROTOCOL (combination)

**Axes**: V-01 INVARIANTS block + V-02 CHECK-OUTPUT PROTOCOL combined.
**Hypothesis**: Combining the INVARIANTS block (C-11 resolution) with the CHECK-OUTPUT
PROTOCOL (C-15 resolution) creates a dual-layer contract: invariants name the properties
that must hold, COP-NN items name the verifiable strings that must appear. COP-07 references
INVARIANT-SPECIALIZATION-DISTINCTNESS by name, making C-34 auditable through both the
invariant contract and the output protocol simultaneously. C-36 remains PARTIAL (AMEND chain
not extended).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
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

Declared immediately after STRUCTURAL-ERROR-CATALOG. Each named invariant is paired to its
enforcement code(s). Phases reference invariant identifiers by name.

```
INVARIANTS:
  INVARIANT-PATH-ISOLATION:
    rule: All role files MUST be written to .craft/roles/{area-slug}/ only.
    enforcement: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION

  INVARIANT-IA-PRESENCE:
    rule: Every team MUST have exactly one Inertia Advocate file; IA lens and expertise
          MUST be derived from the team's PROFILE, not generic.
    enforcement: STRUCTURAL-ERROR:WRITE-IA-GENERIC

  INVARIANT-FIELD-COMPLETENESS:
    rule: Every role file MUST contain all five required fields (title, role-type, area,
          lens, expertise) with substantive content.
    enforcement: STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING

  INVARIANT-PROFILE-UNIQUENESS:
    rule: No two teams may share the same lens-phrase.
    enforcement: STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS

  INVARIANT-SPECIALIZATION-DISTINCTNESS:
    rule: Every specialized role MUST differ from all standard roles in the same team
          on BOTH lens AND expertise. Copying either field from a standard role is a violation.
    enforcement: STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: The STRUCTURAL-ERROR-CATALOG above and
> this INVARIANTS block are co-extensive. Every named invariant is enforced by one or more
> typed error codes. Every structural error code enforces at least one named invariant.
> No invariant exists outside the INVARIANTS block. No enforcement code exists outside
> the STRUCTURAL-ERROR-CATALOG. CATALOG-CLOSURE CLEAN = all INVARIANTS satisfied.

---

### CHECK-OUTPUT PROTOCOL

Every check string below MUST appear verbatim in the output. Phases reference COP-NN items
by identifier. Omission of any COP-NN string is a completeness failure for that phase.

| ID | Check String (verbatim token or prefix) | Phase | Invariant (if applicable) |
|----|------------------------------------------|-------|--------------------------|
| COP-01 | `PARSE-PASS` | PARSE | -- |
| COP-02 | `VALIDATE-PASS` | VALIDATE | -- |
| COP-03 | `TABLE-CLOSED` | CONTRACT | -- |
| COP-04 | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL | -- |
| COP-05 | `PROFILE-GATE` | PROFILE | INVARIANT-PROFILE-UNIQUENESS confirmed |
| COP-06 | `IA-PHASE-COMPLETE` | WRITE-IA | INVARIANT-IA-PRESENCE confirmed |
| COP-07 | `SPECIALIZATION-GATE [team-slug]: ... gate-verdict: PASS` | WRITE-ROLES | INVARIANT-SPECIALIZATION-DISTINCTNESS confirmed per team |
| COP-08 | `ROLES-WRITTEN [team-slug]: ... standard-fields-complete: YES` | WRITE-ROLES | INVARIANT-FIELD-COMPLETENESS confirmed per team |
| COP-09 | `ROLES-COMPLETE: ... all-specialization-gates-passed: YES` | WRITE-ROLES | All INVARIANT-SPECIALIZATION-DISTINCTNESS gates closed |
| COP-10 | `TRANSCRIPTION-CLEAR` | WRITE-CHART | -- |
| COP-11 | `CHART-WRITTEN` | WRITE-CHART | -- |
| COP-12 | `CATALOG-CLOSURE: ... verdict: CLEAN` | BUILD-VERIFY | All INVARIANTS satisfied |
| COP-13 | `BUILD-COMPLETE` | BUILD-VERIFY | -- |

COP-07 is emitted once per team (N total). COP-08 is emitted once per team (N total). COP-09
is emitted exactly once. COP-12 confirms all INVARIANTS are satisfied (co-extensive with
CATALOG-CLOSURE CLEAN).

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

Check duplicate slugs, nesting depth, parent refs.

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

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`.
Halt.

Derive headcount table and level distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if
mismatch. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`.
Halt.

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

For each team, derive category, defended-artifact, lens-phrase from team's domain vocabulary.
INVARIANT-PROFILE-UNIQUENESS enforced: all lens-phrases unique.
Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite before next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

```
PROFILE-GATE: [N] profiles complete. INVARIANT-PROFILE-UNIQUENESS satisfied.   (COP-05)
  All defended-artifacts specific. All lens-phrases domain-derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE` (COP-05)

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`.
Halt.

INVARIANT-IA-PRESENCE enforced: lens and expertise from team's PROFILE; STRUCTURAL-ERROR:WRITE-IA-GENERIC
if generic. Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

```
IA-PHASE-COMPLETE: [N] IA files written. INVARIANT-IA-PRESENCE satisfied for all teams.   (COP-06)
```

Exit token: `IA-PHASE-COMPLETE` (COP-06)

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE` (COP-06). If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE
required`. Halt.

Sequence per team: (1) standard roles, (2) specialized roles -- SPECIALIZATION-GATE (COP-07,
enforces INVARIANT-SPECIALIZATION-DISTINCTNESS) after (2) before ROLES-WRITTEN receipt (COP-08),
(3) IA reference.

INVARIANT-PATH-ISOLATION enforced before each write.
INVARIANT-FIELD-COMPLETENESS enforced on every file.

**SPECIALIZATION-GATE** (per team, after all specialized roles written):

```
SPECIALIZATION-GATE [team-slug]:   (COP-07 -- enforces INVARIANT-SPECIALIZATION-DISTINCTNESS)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION.
Rewrite. Re-emit. DO NOT advance to COP-08 until PASS.

```
ROLES-WRITTEN [team-slug]:         (COP-08 -- confirms INVARIANT-FIELD-COMPLETENESS per team)
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop before next team.

```
ROLES-COMPLETE:                    (COP-09 -- confirms all INVARIANT-SPECIALIZATION-DISTINCTNESS gates)
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

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`.
Halt.

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

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`.
Halt.

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
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
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

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN means all named
> invariants in the INVARIANTS block are satisfied. COP-12 is the output confirmation of this.

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
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## V-05 -- Full synthesis (INVARIANTS + CHECK-OUTPUT PROTOCOL + AMEND-chain precision)

**Axes**: V-01 INVARIANTS block + V-02 CHECK-OUTPUT PROTOCOL + V-03 AMEND-chain precision.
**Hypothesis**: Full integration of all three R12 single-axis improvements: (1) INVARIANTS
block names INVARIANT-SPECIALIZATION-DISTINCTNESS explicitly, (2) COP-07 and COP-09 reference
it by name, (3) AMEND-CHAIN-COMPLETE enumerates per-team gate-rerun results as a required
field, (4) CO-EXTENSIVE DECLARATION is extended to state that CATALOG-CLOSURE CLEAN confirms
all named INVARIANTS and all COP-NN items have been emitted. This is the strongest structural
guarantee available: C-11, C-15, and C-36 all achieve full PASS through distinct enforcement
mechanisms that cross-reference each other.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
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
    rule: All role files MUST be written to .craft/roles/{area-slug}/ only.
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
> CHECK-OUTPUT PROTOCOL COP-NN items confirm invariant satisfaction at the output level
> (see `cop:` fields above). CATALOG-CLOSURE CLEAN = all INVARIANTS satisfied = all
> relevant COP-NN items emitted with passing values. No invariant exists outside the
> INVARIANTS block. No enforcement code exists outside the STRUCTURAL-ERROR-CATALOG.

---

### CHECK-OUTPUT PROTOCOL

Every check string below MUST appear verbatim in the output. Phases reference COP-NN items
by identifier. COP-NN `cop:` annotations in the INVARIANTS block identify which invariants
each item confirms.

| ID | Check String | Phase | Confirms |
|----|-------------|-------|---------|
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

ENTRY-GATE: `VALIDATE-PASS` (COP-02). If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`.
Halt.

Derive headcount table and level distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if
mismatch. Halt.

```
TABLE-CLOSED:                      (COP-03)
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

Exit token: `TABLE-CLOSED` (COP-03)

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED` (COP-03). If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`.
Halt.

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

ENTRY-GATE: `PROFILE-GATE` (COP-05). If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`.
Halt.

INVARIANT-IA-PRESENCE enforced. Lens and expertise from team's PROFILE. STRUCTURAL-ERROR:WRITE-IA-GENERIC
if generic. Rewrite until non-transplantable check passes.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
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

Sequence per team: (1) standard roles, (2) specialized roles -- SPECIALIZATION-GATE (COP-07)
after (2) before ROLES-WRITTEN receipt (COP-08), (3) IA reference.

INVARIANT-PATH-ISOLATION: path validation before each write.
INVARIANT-FIELD-COMPLETENESS: all five fields required on every file.

**SPECIALIZATION-GATE** (per team, after all specialized roles written):
Enforces INVARIANT-SPECIALIZATION-DISTINCTNESS. Compare each specialized role's lens and
expertise against every standard role in the same team.

```
SPECIALIZATION-GATE [team-slug]:   (COP-07 -- INVARIANT-SPECIALIZATION-DISTINCTNESS per team)
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict FAIL. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION.
Rewrite. Re-emit SPECIALIZATION-GATE. DO NOT advance to COP-08 until PASS.

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

ENTRY-GATE: `ROLES-COMPLETE` (COP-09). If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`.
Halt.

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

ENTRY-GATE: `CHART-WRITTEN` (COP-11). If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`.
Halt.

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
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
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
CATALOG-CLOSURE:                   (COP-12 -- co-extensive confirmation of all INVARIANTS)
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

> **INVARIANTS-CATALOG CO-EXTENSIVE DECLARATION**: CATALOG-CLOSURE CLEAN = all named
> INVARIANTS satisfied = all relevant COP-NN items emitted with passing values (COP-05
> through COP-09, COP-12). No invariant exists outside the INVARIANTS block; no enforcement
> code exists outside this catalog; no output completeness check exists outside the
> CHECK-OUTPUT PROTOCOL.

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

SPECIALIZATION-GATE re-run is a named, first-class step in the WRITE-ROLES re-execution
for this area. Prior SPECIALIZATION-GATE verdicts for all teams in the amended area are
DISCARDED. Gate verdicts MUST be earned fresh (COP-07 re-emitted per team in the amended
area). DO NOT advance to ROLES-WRITTEN receipt (COP-08) per team until fresh
SPECIALIZATION-GATE emits gate-verdict: PASS.

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
An AMEND-CHAIN-COMPLETE that omits `specialization-gate-rerun:` is structurally incomplete
and fails C-36.

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Re-run CONTRACT, CONTRACT-SEAL, PROFILE, and
BUILD-VERIFY for affected teams.

---

## R12 Variation Summary

| Variation | Axis | C-11 | C-15 | C-34 | C-35 | C-36 | Notes |
|-----------|------|------|------|------|------|------|-------|
| V-01 | INVARIANTS block | PASS | PARTIAL | PASS | PASS | PARTIAL | Named INVARIANT-SPECIALIZATION-DISTINCTNESS; COP absent |
| V-02 | CHECK-OUTPUT PROTOCOL | PARTIAL | PASS | PASS | PASS | PARTIAL | COP-07/COP-09 audit gate; INVARIANTS block absent |
| V-03 | AMEND-chain precision | PARTIAL | PARTIAL | PASS | PASS | PASS | gate-rerun field in AMEND-CHAIN-COMPLETE; others unchanged |
| V-04 | INVARIANTS + COP | PASS | PASS | PASS | PASS | PARTIAL | Dual-layer contract; COP-NN references invariant IDs |
| V-05 | Full synthesis | PASS | PASS | PASS | PASS | PASS | Triply enforced: INVARIANTS, COP, AMEND-CHAIN-COMPLETE |

**Predicted discriminator**: C-36 separates V-03/V-05 (PASS) from V-01/V-02/V-04 (PARTIAL).
C-11 separates V-01/V-04/V-05 (PASS) from V-02/V-03 (PARTIAL).
C-15 separates V-02/V-04/V-05 (PASS) from V-01/V-03 (PARTIAL).
V-05 is the only variation predicted to achieve full PASS on all five target criteria.
