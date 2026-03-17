---
skill: quest-variate
skill_target: corps-build
round: 11
date: 2026-03-17
rubric_version: 9
r10_scorecard: corps-build-scorecard-R10-2026-03-17.md
---

# Variate R11 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 11. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R10 excellence signals are now baseline criteria in rubric v9:
- C-31: ROLES-WRITTEN NO-halt remediation cycle
- C-32: AMEND-CHAIN-COMPLETE terminal token with PROFILE-DELTA
- C-33: STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract

R10 persistent PARTIALs targeted by R11:
- C-11: PARTIAL across all R10 variations -- STRUCTURAL-ERROR-CATALOG serves the invariant
  function but no dedicated `INVARIANTS:` labeled block with distinct named identifiers.
- C-15: PARTIAL across all R10 variations -- EXCLUSION-MANIFEST covers excluded-output content
  but the specific named section "CHECK-OUTPUT PROTOCOL" is absent and phases do not reference
  it by name.

R11 variation axes:

1. INVARIANTS-block (V-01): Dedicated `INVARIANTS:` block immediately after
   STRUCTURAL-ERROR-CATALOG. Per-invariant named identifiers (INVARIANT-PATH-ISOLATION,
   INVARIANT-IA-PRESENCE, INVARIANT-FIELD-COMPLETENESS, INVARIANT-PROFILE-UNIQUENESS,
   INVARIANT-SPECIALIZATION-DISTINCTNESS) each paired to their enforcement STRUCTURAL-ERROR
   code(s). C-33 co-extensive declaration bridges INVARIANTS block and STRUCTURAL-ERROR-CATALOG.
   Targets C-11 resolution.

2. CHECK-OUTPUT-PROTOCOL (V-02): Dedicated `CHECK-OUTPUT PROTOCOL:` section after
   STRUCTURAL-ERROR-CATALOG. Enumerates every check string that must be emitted (COP-01 through
   COP-21) with format and emitting phase. Phase bodies reference protocol items by COP-NN id.
   Targets C-15 resolution.

3. SPECIALIZATION-GATE (V-03): Per-team SPECIALIZATION-GATE block in Phase 7, after specialized
   roles are written and before ROLES-WRITTEN receipt. Compares each specialized role's lens +
   expertise pair against all standard roles in the same team. STRUCTURAL-ERROR:SPECIALIZATION-
   COPY-VIOLATION if any identical pair found. New axis targeting C-07 depth and potential C-34.

4. INVARIANTS-block + CHECK-OUTPUT-PROTOCOL (V-04): V-01 axis and V-02 axis combined. Both
   persistent PARTIALs (C-11 and C-15) resolved simultaneously.

5. Full integration (V-05): All three R11 axes (V-01 + V-02 + V-03) plus full R10 baseline.
   Fully self-contained spec. Canonical R11 baseline.

---

## V-01 -- INVARIANTS-block axis

**Axis**: Dedicated INVARIANTS block with per-invariant named identifiers
**Hypothesis**: A dedicated `INVARIANTS:` labeled block placed immediately after the
STRUCTURAL-ERROR-CATALOG -- with named identifiers (INVARIANT-PATH-ISOLATION etc.) each paired
to their enforcement code(s) -- resolves C-11 PARTIAL by providing the distinct named block with
per-invariant identifiers the criterion requires. The C-33 co-extensive declaration bridges the
INVARIANTS block back to the STRUCTURAL-ERROR-CATALOG, confirming they describe the same
contract from complementary perspectives. C-15 remains PARTIAL (no CHECK-OUTPUT PROTOCOL).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. All structural violations are encoded as named codes here.
Phases reference codes by name; they do not redefine violations.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL | PARSE | org.yaml missing required node (groups, teams, or roles) |
| STRUCTURAL-ERROR:PARSE-EMPTY-TEAM | PARSE | team node has zero role slots |
| STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG | VALIDATE | two areas share the same slug |
| STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION | VALIDATE | nesting depth exceeds declared schema or skips level |
| STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH | CONTRACT | derived slot count does not match org.yaml declarations |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | team assigned to wrong category (product/platform/ops) |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase not drawn from team domain vocabulary |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two teams share identical lens-phrase |
| STRUCTURAL-ERROR:WRITE-IA-GENERIC | WRITE-IA | IA lens/expertise is generic resistance language, not team-specific |
| STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING | WRITE-ROLES | one or more of five required fields absent or empty |
| STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION | WRITE-ROLES | specialized role lens+expertise pair identical to a standard role in the same team |
| STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION | WRITE-ROLES | role file written outside `.craft/roles/{area-slug}/{role-slug}.md` |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE emitted before all teams have passing ROLES-WRITTEN receipt |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR |
| STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION | BUILD-VERIFY | BUILD-VERIFY performs an action listed in EXCLUSION-MANIFEST |
| STRUCTURAL-ERROR:CROSS-REF-MISMATCH | BUILD-VERIFY | any CROSS-REF row returns MISMATCH -- blocks CROSS-REF PASS |
| STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN | BUILD-VERIFY | CATALOG-CLOSURE verdict is OPEN -- blocks BUILD-COMPLETE |

---

### INVARIANTS

Each structural invariant governing this build is named below with a distinct identifier. The
STRUCTURAL-ERROR-CATALOG above is the complete enforcement mechanism for every invariant. Every
invariant is encoded as at least one named STRUCTURAL-ERROR code. No invariant exists outside
the catalog.

> **C-33 CO-EXTENSIVE DECLARATION**: The INVARIANTS block and the STRUCTURAL-ERROR-CATALOG are
> co-extensive. The INVARIANTS block names each constraint. The STRUCTURAL-ERROR-CATALOG names
> the enforcement code for each constraint. They describe the same contract from two
> complementary perspectives. A runtime structural error is either cataloged (covered by a named
> code) or a rubric violation (invariant not encoded).

| Invariant | Enforcement Code(s) |
|-----------|---------------------|
| **INVARIANT-PATH-ISOLATION** -- Role files are written only to paths matching `.craft/roles/{area-slug}/{role-slug}.md`. No role file is created outside this pattern. | STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION |
| **INVARIANT-IA-PRESENCE** -- Every team has exactly one Inertia Advocate. IA is never omitted and never duplicated per team. | STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (if IA absent at closure) |
| **INVARIANT-FIELD-COMPLETENESS** -- Every role file contains all five typed fields with substantive bodies: title, role-type, area, lens, expertise. | STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING |
| **INVARIANT-PROFILE-UNIQUENESS** -- No two teams share an identical lens-phrase. Each team's defended-artifact and lens-phrase are derived from that team's declared domain vocabulary only. | STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS, STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED |
| **INVARIANT-SPECIALIZATION-DISTINCTNESS** -- No specialized role is a copy of a standard role in the same team. Distinctness is enforced at lens + expertise pair level. | STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION |

---

### Phase 1: PARSE

ENTRY-GATE: First phase -- no predecessor token required.

Read `org.yaml`. Enumerate all group nodes (Division, Team, Sub-group), all area slugs, all
role slots per team (standard and specialized), total role count (IA excluded -- IA derived
in WRITE-IA).

```
PARSE-SUMMARY:
  groups: [N]
  teams: [N]
  areas: [list of area-slugs]
  total-role-slots: [N]
```

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if any team has zero role slots. Halt.

Exit token: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: emit `ENTRY-GATE-FAIL: PARSE-PASS required` and halt.

Check: no duplicate area slugs (STRUCTURAL-ERROR:VALIDATE-DUPLICATE-SLUG), nesting matches
declared depth (STRUCTURAL-ERROR:VALIDATE-NESTING-VIOLATION), all parent group refs exist.

```
VALIDATE-SUMMARY:
  duplicate-slug-check: PASS | FAIL
  nesting-check: PASS | FAIL
  parent-ref-check: PASS | FAIL
```

All checks must be PASS before proceeding.

Exit token: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: emit `ENTRY-GATE-FAIL: VALIDATE-PASS required` and halt.

Derive headcount table from org.yaml. Per team: standard-count (from role declarations),
specialized-count (from role declarations), IA-count = 1. Total = standard + specialized + IA.
Sum per group. Derive level distribution (count by level per group).

```
TABLE-CLOSED:
  [table: Group | Team | Standard | Specialized | IA | Total | Levels]
  total-slots: [N]
```

STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if derived count does not match org.yaml. Halt.

Exit token: `TABLE-CLOSED`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: emit `ENTRY-GATE-FAIL: TABLE-CLOSED required` and halt.

Lock the headcount contract. No structural changes to the table are permitted after
CONTRACT-SEAL-PASS. Confirm level distribution is complete.

```
CONTRACT-SEAL: LOCKED
  sealed-slots: [N]
  level-distribution: [table: Level | Count | % of Total]
```

Exit token: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: emit `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`
and halt.

For each team, derive three profile fields from team's declared domain vocabulary:
- `category`: product | platform | ops. STRUCTURAL-ERROR:PROFILE-CATEGORY if wrong.
- `defended-artifact`: the specific system, document, or capability this team owns.
  Must name a specific thing, not a generic description.
- `lens-phrase`: unique 3-6 word phrase from the team's vocabulary.
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if generic.
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if identical to another team's phrase.

Per-team violation: rewrite deficient field before advancing to next team.

```
PROFILE [team-slug]:
  category: [product | platform | ops]
  defended-artifact: [specific named thing]
  lens-phrase: "[phrase]"
  status: PASS
```

When all teams have `status: PASS`:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: emit `ENTRY-GATE-FAIL: PROFILE-GATE required` and halt.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`. Lens and expertise MUST
come from this team's `defended-artifact` and `lens-phrase` from Phase 5 (INVARIANT-IA-PRESENCE
via INVARIANT-PROFILE-UNIQUENESS chain).

Non-transplantable check per team:
- FAIL (generic): "Any change to the existing architecture risks disrupting team workflows."
  No reference to team's specific defended-artifact.
- PASS (team-specific): Lens and expertise reference the team's specific defended-artifact and
  domain vocabulary.

STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic. Rewrite before advancing.

```
IA-WRITTEN [team-slug]:
  path: .craft/roles/{area-slug}/inertia-advocate.md
  lens-source: [lens-phrase from PROFILE]
  artifact-source: [defended-artifact from PROFILE]
  non-transplantable: PASS
```

When all teams:

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: emit `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`
and halt.

For each team, write role files in sequence: (1) standard roles, (2) specialized roles,
(3) IA -- already written, reference only, do not rewrite.

Path validation (per role file, before writing): confirm `.craft/roles/{area-slug}/{role-slug}.md`.
STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if mismatch. Halt.

Required fields per file (INVARIANT-FIELD-COMPLETENESS): title, role-type, area, lens, expertise.
All five must have substantive bodies. STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING if any absent.

Specialization-distinctness enforcement (after all specialized roles for this team are written):
For each specialized role: compare its lens + expertise pair against every standard role in
the same team. STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION if identical pair found.
Rewrite specialized role before continuing.

ROLES-WRITTEN receipt per team (after all roles written + distinctness confirmed):
```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`:
- Enter remediation loop: identify deficient fields -> rewrite -> re-emit ROLES-WRITTEN receipt
  for this team -> confirm YES.
- DO NOT advance to next team until receipt shows `standard-fields-complete: YES`.
- This is a within-phase recoverable state, not a build halt.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES`:

```
ROLES-COMPLETE:
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
```

STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE if any team lacks passing receipt. Resolve before
emitting ROLES-COMPLETE.

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: emit `ENTRY-GATE-FAIL: ROLES-COMPLETE required`
and halt.

Write `org-chart.md`:
- ASCII hierarchy using `+--` and `|` notation; all org.yaml names verbatim; nesting reflects
  group -> team depth (minimum two levels).
- Headcount table: columns Group | Standard | Specialized | IA | Total | Levels.
- Level distribution table.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

If any artifact is REVISED: describe revision reason. Confirm final content is faithful to
org.yaml.

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if TRANSCRIPTION-CLEAR absent. Halt.

Exit token: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: emit `ENTRY-GATE-FAIL: CHART-WRITTEN required` and halt.

**Single responsibility**: BUILD-VERIFY verifies the build artifact set against the sealed
contract. It does nothing else.

EXCLUSION-MANIFEST -- BUILD-VERIFY explicitly does NOT:

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

CROSS-REF (5 rows required; MISMATCH on any row triggers STRUCTURAL-ERROR:CROSS-REF-MISMATCH):

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

A CROSS-REF with fewer than 5 rows is a structural violation.

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

CATALOG-CLOSURE (after CROSS-REF PASS -- per all 17 codes):

```
CATALOG-CLOSURE:
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

TRIGGERED+RESOLVED entry missing `triggered-at` or `resolved-by` = verdict OPEN.
STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

> **CATALOG-CLOSURE INVARIANTS DECLARATION**: CATALOG-CLOSURE CLEAN means all structural
> invariants named in the INVARIANTS block above have been verified: no invariant was violated
> (CONFIRMED-NOT-TRIGGERED) or every violation was resolved within-phase (TRIGGERED+RESOLVED
> with full audit trace). The STRUCTURAL-ERROR-CATALOG and the INVARIANTS block are the same
> contract. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

Exit token: `BUILD-VERIFY-COMPLETE`

Emit `BUILD-COMPLETE` only if CATALOG-CLOSURE verdict is CLEAN and all 5 CROSS-REF rows MATCH.

---

### AMEND

**`--area {area-slug}`** -- Regenerate a specific area. Full repair chain required:

1. PROFILE-REDERIVE: re-run Phase 5 PROFILE for all teams in `{area-slug}`. Emit:
   ```
   PROFILE-REDERIVE-COMPLETE [area-slug]:
     teams-re-profiled: [N]
     violations-found: [N]
     violations-resolved: [N]
   ```
2. WRITE-IA: re-run Phase 6 for `{area-slug}` teams only. Requires PROFILE-REDERIVE-COMPLETE.
3. WRITE-ROLES: re-run Phase 7 for `{area-slug}` teams only.
4. BUILD-VERIFY: re-run Phase 9. STRUCTURAL-ERROR:PROFILE-* invariants re-checked for affected
   teams.

After all four stages:
```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value for each changed profile field)
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

PROFILE-DELTA distinguishes genuine re-derivation (CHANGED with values) from no-op confirmation
(UNCHANGED). Missing PROFILE-DELTA makes the amendment block structurally incomplete.
No further `--area` amend for this area until `AMEND-CHAIN-COMPLETE: PASS`.

**`--level {area-slug} {old-term} {new-term}`** -- Adjust level vocabulary. Update all role
files in `{area-slug}` where the old term appears. Emit count of files updated. Re-run
BUILD-VERIFY for `{area-slug}`.

**`--group {add | rename | reparent} {args}`** -- Change group structure. Re-run CONTRACT,
CONTRACT-SEAL, PROFILE (INVARIANT-PROFILE-UNIQUENESS re-check for reparented teams), and
BUILD-VERIFY for affected teams.

---

## V-02 -- CHECK-OUTPUT-PROTOCOL axis

**Axis**: Dedicated CHECK-OUTPUT PROTOCOL section enumerating all check strings
**Hypothesis**: A dedicated `CHECK-OUTPUT PROTOCOL:` section placed after the
STRUCTURAL-ERROR-CATALOG -- listing every check string that must be emitted with its format
and emitting phase, referenced from phase bodies by COP-NN id -- resolves C-15 PARTIAL by
providing the named protocol section that phases reference by name. C-11 remains PARTIAL
(no dedicated INVARIANTS block; STRUCTURAL-ERROR-CATALOG serves the function under its own
label, and the C-33 declaration is still present at CATALOG-CLOSURE).

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. All structural violations are encoded as named codes here.
Phases reference codes by name; they do not redefine violations. This catalog constitutes
the complete invariants contract for this build -- all structural invariants are encoded as
typed error codes, no invariant exists outside the catalog.

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

Every check string that must be emitted during this build is enumerated below with its required
format and emitting phase. Phase bodies reference items by COP-NN id. A build that does not
emit a required check string has violated the CHECK-OUTPUT PROTOCOL for that phase.

| ID | Check String | Format | Emitting Phase |
|----|-------------|--------|----------------|
| COP-01 | PARSE-SUMMARY block | `PARSE-SUMMARY: groups: [N] teams: [N] areas: [...] total-role-slots: [N]` | PARSE |
| COP-02 | PARSE-PASS token | `PARSE-PASS` | PARSE |
| COP-03 | VALIDATE-SUMMARY block | `VALIDATE-SUMMARY: duplicate-slug-check: PASS\|FAIL nesting-check: PASS\|FAIL parent-ref-check: PASS\|FAIL` | VALIDATE |
| COP-04 | VALIDATE-PASS token | `VALIDATE-PASS` | VALIDATE |
| COP-05 | TABLE-CLOSED block | `TABLE-CLOSED: [headcount table] total-slots: [N]` | CONTRACT |
| COP-06 | CONTRACT-SEAL block | `CONTRACT-SEAL: LOCKED sealed-slots: [N] level-distribution: [table]` | CONTRACT-SEAL |
| COP-07 | CONTRACT-SEAL-PASS token | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL |
| COP-08 | PROFILE block per team | `PROFILE [team-slug]: category: [...] defended-artifact: [...] lens-phrase: "[...]" status: PASS` | PROFILE |
| COP-09 | PROFILE-GATE summary | `PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* outstanding. All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.` | PROFILE |
| COP-10 | IA-WRITTEN block per team | `IA-WRITTEN [team-slug]: path: [...] lens-source: [...] artifact-source: [...] non-transplantable: PASS` | WRITE-IA |
| COP-11 | IA-PHASE-COMPLETE summary | `IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.` | WRITE-IA |
| COP-12 | ROLES-WRITTEN receipt per team | `ROLES-WRITTEN [team-slug]: standard-count: [N] specialized-count: [N] ia-count: 1 standard-fields-complete: YES\|NO` | WRITE-ROLES |
| COP-13 | ROLES-COMPLETE block | `ROLES-COMPLETE: total-standard: [N] total-specialized: [N] total-ia: [N] total-files: [N] all-receipts-passed: YES` | WRITE-ROLES |
| COP-14 | TRANSCRIPTION-RECEIPT block | `TRANSCRIPTION-RECEIPT: ARTIFACT-A: VERBATIM\|REVISED ARTIFACT-B: VERBATIM\|REVISED ARTIFACT-C: VERBATIM\|REVISED` | WRITE-CHART |
| COP-15 | TRANSCRIPTION-CLEAR block | `TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.` | WRITE-CHART |
| COP-16 | CHART-WRITTEN token | `CHART-WRITTEN` | WRITE-CHART |
| COP-17 | CROSS-REF 5-row table | `CROSS-REF: file-count: [...] ia-count: [...] dir-match: [...] table-fidelity: [...] roles-receipts: [...]` | BUILD-VERIFY |
| COP-18 | DERIVATION-LOOP-CLOSED table | `DERIVATION-LOOP-CLOSED: [team-slug]: PROFILE lens-phrase "[...]" -> IA lens: CLOSED` (one row per team) | BUILD-VERIFY |
| COP-19 | CATALOG-CLOSURE block | Full 17-code enumeration with CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED (triggered-at + resolved-by) and verdict CLEAN\|OPEN | BUILD-VERIFY |
| COP-20 | BUILD-VERIFY-COMPLETE token | `BUILD-VERIFY-COMPLETE` | BUILD-VERIFY |
| COP-21 | BUILD-COMPLETE declaration | `BUILD-COMPLETE` (only if COP-19 verdict CLEAN and all COP-17 rows MATCH) | BUILD-VERIFY |

---

### Phase 1: PARSE

ENTRY-GATE: First phase -- no predecessor token required.

Read `org.yaml`. Enumerate groups, teams, area slugs, role slots per team (IA excluded).
Emit COP-01 (PARSE-SUMMARY) per CHECK-OUTPUT PROTOCOL.

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if any team has zero slots. Halt.

Emit COP-02: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.

Check duplicate slugs, nesting depth, parent refs. Emit COP-03 (VALIDATE-SUMMARY) per
CHECK-OUTPUT PROTOCOL. All checks PASS before proceeding.

Emit COP-04: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.

Derive headcount table. Per team: standard, specialized, IA=1, total. Sum per group.
Derive level distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.

Emit COP-05: `TABLE-CLOSED: [headcount table] total-slots: [N]`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.

Lock contract. No structural changes permitted after CONTRACT-SEAL-PASS.
Emit COP-06 (CONTRACT-SEAL block with level distribution) per CHECK-OUTPUT PROTOCOL.

Emit COP-07: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`.
Halt.

For each team, derive category, defended-artifact, lens-phrase from team's domain vocabulary.
Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite before advancing to next team.
Emit COP-08 (PROFILE block) per team per CHECK-OUTPUT PROTOCOL.

When all teams PASS, emit COP-09:
```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`. Lens and expertise from
team's PROFILE (defended-artifact, lens-phrase). Non-transplantable check: generic language
triggers STRUCTURAL-ERROR:WRITE-IA-GENERIC; rewrite before advancing.

Emit COP-10 (IA-WRITTEN block) per team per CHECK-OUTPUT PROTOCOL.

When all teams done, emit COP-11:
```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`.
Halt.

Sequence per team: (1) standard roles, (2) specialized roles, (3) IA reference.
Path validation before each write (STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if mismatch).
All five fields required per file (STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING if absent).
Specialization-distinctness: after specialized roles written, check lens+expertise pair against
standard roles in same team (STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION if identical).
Rewrite specialized role before continuing.

Emit COP-12 (ROLES-WRITTEN receipt) per team per CHECK-OUTPUT PROTOCOL:
```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: enter remediation loop (rewrite -> re-emit -> confirm YES)
before advancing to next team. Within-phase recoverable, not a halt.

When all teams have passing receipts, emit COP-13:
```
ROLES-COMPLETE:
  total-standard: [N]  total-specialized: [N]  total-ia: [N]
  total-files: [N]     all-receipts-passed: YES
```

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

Write `org-chart.md`: ASCII hierarchy (`+--`/`|`, verbatim names, min two levels), headcount
table, level distribution. Emit COP-14 (TRANSCRIPTION-RECEIPT) per CHECK-OUTPUT PROTOCOL.
If any REVISED: describe reason, confirm fidelity. Emit COP-15 (TRANSCRIPTION-CLEAR).
STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if COP-15 absent. Halt.

Emit COP-16: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

Single responsibility: verify artifact set against sealed contract. Nothing else.

EXCLUSION-MANIFEST (per CHECK-OUTPUT PROTOCOL item COP-17 format requirement -- phase scope):

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

Emit COP-17 (CROSS-REF 5-row table) per CHECK-OUTPUT PROTOCOL:
```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

Emit COP-18 (DERIVATION-LOOP-CLOSED, one row per team) per CHECK-OUTPUT PROTOCOL.

Emit COP-19 (CATALOG-CLOSURE) per CHECK-OUTPUT PROTOCOL. All 17 codes enumerated.
TRIGGERED+RESOLVED requires `triggered-at` and `resolved-by`; missing = OPEN.
STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

> **C-33 CATALOG-CLOSURE DECLARATION**: The STRUCTURAL-ERROR-CATALOG constitutes the complete
> invariants contract for this build. All structural invariants are encoded as typed error codes.
> No invariant exists outside the catalog. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

Emit COP-20: `BUILD-VERIFY-COMPLETE`

Emit COP-21: `BUILD-COMPLETE` (only if COP-19 verdict CLEAN and all COP-17 rows MATCH).

---

### AMEND

**`--area {area-slug}`** -- Full chain: PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES ->
BUILD-VERIFY. Emit PROFILE-REDERIVE-COMPLETE (PROFILE-REDERIVE-COMPLETE, teams-re-profiled,
violations-found, violations-resolved). PROFILE-REDERIVE-COMPLETE required before WRITE-IA.

After all stages:
```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed field)
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

PROFILE-DELTA distinguishes genuine re-derivation (CHANGED) from no-op confirmation (UNCHANGED).
Missing PROFILE-DELTA = amendment block structurally incomplete. No further `--area` amend for
this area until `AMEND-CHAIN-COMPLETE: PASS`.

**`--level {area-slug} {old-term} {new-term}`** -- Update level vocabulary. Emit files-updated
count. Re-run BUILD-VERIFY.

**`--group {add | rename | reparent} {args}`** -- Change group structure. Re-run CONTRACT,
CONTRACT-SEAL, PROFILE, and BUILD-VERIFY for affected teams.

---

## V-03 -- SPECIALIZATION-GATE axis

**Axis**: Per-team SPECIALIZATION-GATE block in Phase 7 after specialized roles are written
**Hypothesis**: A named SPECIALIZATION-GATE block (emitted after all specialized roles for a
team are written, before the ROLES-WRITTEN receipt) that explicitly records each specialized
role's lens+expertise pair and its comparison result against standard roles in the same team
strengthens C-07 specialization-distinctness enforcement -- converting an inline violation check
into an auditable named gate with its own token. If the gate emits a new excellence pattern
(named gate token + per-role comparison table), it becomes the basis for C-34. C-11 and C-15
remain PARTIAL (no INVARIANTS block, no CHECK-OUTPUT PROTOCOL).

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
team's PROFILE. Non-transplantable check: STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic. Rewrite.

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

For each specialized role, compare its `lens` value and `expertise` value against every standard
role in the same team. Record the comparison result per specialized role.

```
SPECIALIZATION-GATE [team-slug]:
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If any `pair-identical: YES`: gate-verdict is FAIL. Emit
STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION for the specific role slug. Rewrite that
specialized role. Re-emit SPECIALIZATION-GATE for this team. DO NOT advance to ROLES-WRITTEN
receipt until gate-verdict is PASS.

SPECIALIZATION-GATE with `gate-verdict: PASS` required before ROLES-WRITTEN receipt for
each team.

ROLES-WRITTEN receipt per team (after SPECIALIZATION-GATE PASS):

```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop (rewrite -> re-emit -> confirm YES)
before next team.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES`:

```
ROLES-COMPLETE:
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES
```

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

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if TRANSCRIPTION-CLEAR absent. Halt.

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
> contract for this build. All structural invariants are encoded as typed error codes. No
> invariant exists outside the catalog. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

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

## V-04 -- INVARIANTS-block + CHECK-OUTPUT-PROTOCOL (combined)

**Axis**: C-11 resolution and C-15 resolution simultaneously
**Hypothesis**: Combining the dedicated INVARIANTS block (V-01 axis) and the dedicated
CHECK-OUTPUT PROTOCOL section (V-02 axis) in a single variation resolves both persistent
PARTIALs from R10. The INVARIANTS block satisfies C-11's requirement for a named block with
distinct per-invariant identifiers. The CHECK-OUTPUT PROTOCOL satisfies C-15's requirement for
a named protocol section referenced from phase bodies. The C-33 co-extensive declaration is
embedded in both blocks for reinforcement. SPECIALIZATION-GATE is absent (single-phase-scope
innovation reserved for V-05).

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

Each structural invariant governing this build is named with a distinct identifier. The
STRUCTURAL-ERROR-CATALOG is the complete enforcement mechanism for every invariant.

> **C-33 CO-EXTENSIVE DECLARATION**: The INVARIANTS block and the STRUCTURAL-ERROR-CATALOG are
> co-extensive. The INVARIANTS block names each constraint. The catalog names the enforcement
> code. They describe the same contract. No invariant exists outside the catalog.

| Invariant | Enforcement Code(s) |
|-----------|---------------------|
| **INVARIANT-PATH-ISOLATION** -- Role files written only to `.craft/roles/{area-slug}/{role-slug}.md`. | STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION |
| **INVARIANT-IA-PRESENCE** -- Every team has exactly one Inertia Advocate. | STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE |
| **INVARIANT-FIELD-COMPLETENESS** -- Every role file has all five typed fields with substantive bodies. | STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING |
| **INVARIANT-PROFILE-UNIQUENESS** -- No two teams share a lens-phrase; each team's profile derives from its domain vocabulary. | STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS, STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED |
| **INVARIANT-SPECIALIZATION-DISTINCTNESS** -- No specialized role duplicates a standard role at lens+expertise pair level. | STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION |

---

### CHECK-OUTPUT PROTOCOL

Every check string that must be emitted is listed below with format and emitting phase.
Phase bodies reference items by COP-NN id. A build that omits a required check string has
violated the CHECK-OUTPUT PROTOCOL for that phase.

| ID | Check String | Format (abbreviated) | Emitting Phase |
|----|-------------|----------------------|----------------|
| COP-01 | PARSE-SUMMARY | `PARSE-SUMMARY: groups: [N] teams: [N] areas: [...] total-role-slots: [N]` | PARSE |
| COP-02 | PARSE-PASS | `PARSE-PASS` | PARSE |
| COP-03 | VALIDATE-SUMMARY | `VALIDATE-SUMMARY: duplicate-slug-check: P\|F nesting-check: P\|F parent-ref-check: P\|F` | VALIDATE |
| COP-04 | VALIDATE-PASS | `VALIDATE-PASS` | VALIDATE |
| COP-05 | TABLE-CLOSED | `TABLE-CLOSED: [headcount table] total-slots: [N]` | CONTRACT |
| COP-06 | CONTRACT-SEAL | `CONTRACT-SEAL: LOCKED sealed-slots: [N] level-distribution: [table]` | CONTRACT-SEAL |
| COP-07 | CONTRACT-SEAL-PASS | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL |
| COP-08 | PROFILE per team | `PROFILE [team-slug]: category: [...] defended-artifact: [...] lens-phrase: "[...]" status: PASS` | PROFILE |
| COP-09 | PROFILE-GATE | Full summary string with no violations outstanding | PROFILE |
| COP-10 | IA-WRITTEN per team | `IA-WRITTEN [team-slug]: path: [...] lens-source: [...] artifact-source: [...] non-transplantable: PASS` | WRITE-IA |
| COP-11 | IA-PHASE-COMPLETE | `IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.` | WRITE-IA |
| COP-12 | ROLES-WRITTEN per team | `ROLES-WRITTEN [team-slug]: standard-count: [N] specialized-count: [N] ia-count: 1 standard-fields-complete: YES\|NO` | WRITE-ROLES |
| COP-13 | ROLES-COMPLETE | `ROLES-COMPLETE: total-standard: [N] ... all-receipts-passed: YES` | WRITE-ROLES |
| COP-14 | TRANSCRIPTION-RECEIPT | Three-artifact VERBATIM\|REVISED block | WRITE-CHART |
| COP-15 | TRANSCRIPTION-CLEAR | `TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.` | WRITE-CHART |
| COP-16 | CHART-WRITTEN | `CHART-WRITTEN` | WRITE-CHART |
| COP-17 | CROSS-REF | 5-row table: file-count, ia-count, dir-match, table-fidelity, roles-receipts | BUILD-VERIFY |
| COP-18 | DERIVATION-LOOP-CLOSED | Per-team: `[team-slug]: PROFILE lens-phrase "[...]" -> IA lens: CLOSED` | BUILD-VERIFY |
| COP-19 | CATALOG-CLOSURE | Full 17-code enumeration with verdict CLEAN\|OPEN | BUILD-VERIFY |
| COP-20 | BUILD-VERIFY-COMPLETE | `BUILD-VERIFY-COMPLETE` | BUILD-VERIFY |
| COP-21 | BUILD-COMPLETE | `BUILD-COMPLETE` (only if COP-19 CLEAN and all COP-17 MATCH) | BUILD-VERIFY |

---

### Phase 1: PARSE

ENTRY-GATE: First phase. Read `org.yaml`. Enumerate groups, teams, areas, role slots (IA
excluded). Emit COP-01 (PARSE-SUMMARY) per CHECK-OUTPUT PROTOCOL. STRUCTURAL-ERROR:PARSE-
SCHEMA-FAIL if required node absent (halt). STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if zero slots
(halt). Emit COP-02: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.
Check duplicate slugs, nesting, parent refs. Emit COP-03 per CHECK-OUTPUT PROTOCOL.
All PASS before proceeding. Emit COP-04: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.
Derive headcount table and level distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if
mismatch (halt). Emit COP-05: `TABLE-CLOSED: [headcount table] total-slots: [N]`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.
Lock contract. Emit COP-06 per CHECK-OUTPUT PROTOCOL. Emit COP-07: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`.
Halt. Per team: derive category, defended-artifact, lens-phrase from domain vocabulary (see
INVARIANT-PROFILE-UNIQUENESS). Apply STRUCTURAL-ERROR:PROFILE-* codes on violation; rewrite
before next team. Emit COP-08 per team per CHECK-OUTPUT PROTOCOL. When all PASS, emit COP-09:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.
Per team: write `.craft/roles/{area-slug}/inertia-advocate.md` using PROFILE lens/artifact
(INVARIANT-IA-PRESENCE). Non-transplantable check: STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic.
Emit COP-10 per team per CHECK-OUTPUT PROTOCOL. When all done, emit COP-11:

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`.
Halt. Sequence: standard -> specialized -> IA reference. Path validation per write
(INVARIANT-PATH-ISOLATION). All five fields required (INVARIANT-FIELD-COMPLETENESS).
Specialization-distinctness enforcement at lens+expertise pair level
(INVARIANT-SPECIALIZATION-DISTINCTNESS). Emit COP-12 per team per CHECK-OUTPUT PROTOCOL:

```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

`standard-fields-complete: NO` -> remediation loop (rewrite -> re-emit -> confirm YES) before
next team. Emit COP-13 when all receipts pass:

```
ROLES-COMPLETE:
  total-standard: [N]  total-specialized: [N]  total-ia: [N]
  total-files: [N]     all-receipts-passed: YES
```

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.
Write `org-chart.md` (ASCII hierarchy, headcount table, level distribution). Emit COP-14
(TRANSCRIPTION-RECEIPT) per CHECK-OUTPUT PROTOCOL. Emit COP-15 (TRANSCRIPTION-CLEAR) per
CHECK-OUTPUT PROTOCOL. STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if COP-15 absent. Halt.
Emit COP-16: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.
Single responsibility: verify artifact set against sealed contract.

EXCLUSION-MANIFEST (per CHECK-OUTPUT PROTOCOL scope constraint):

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

Emit COP-17 (CROSS-REF 5 rows: file-count, ia-count, dir-match, table-fidelity,
roles-receipts) per CHECK-OUTPUT PROTOCOL. STRUCTURAL-ERROR:CROSS-REF-MISMATCH on any
MISMATCH row. Emit COP-18 (DERIVATION-LOOP-CLOSED per team) per CHECK-OUTPUT PROTOCOL.

Emit COP-19 (CATALOG-CLOSURE) per CHECK-OUTPUT PROTOCOL. All 17 codes enumerated.
TRIGGERED+RESOLVED requires `triggered-at` and `resolved-by`. Missing = OPEN.
STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

> **CATALOG-CLOSURE INVARIANTS DECLARATION**: This catalog constitutes the complete invariants
> contract for this build (see INVARIANTS block above). CATALOG-CLOSURE CLEAN = all five named
> invariants satisfied. The INVARIANTS block and this catalog are co-extensive declarations of
> the same contract.

Emit COP-20: `BUILD-VERIFY-COMPLETE`
Emit COP-21: `BUILD-COMPLETE` (only if COP-19 CLEAN and all COP-17 MATCH).

---

### AMEND

**`--area {area-slug}`** -- PROFILE-REDERIVE -> WRITE-IA -> WRITE-ROLES -> BUILD-VERIFY.
PROFILE-REDERIVE-COMPLETE required before WRITE-IA. After all stages:

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
BUILD-VERIFY for affected teams. INVARIANT-PROFILE-UNIQUENESS re-check for reparented teams.

---

## V-05 -- Full integration (all R11 axes)

**Axis**: INVARIANTS-block + CHECK-OUTPUT-PROTOCOL + SPECIALIZATION-GATE
**Hypothesis**: All three R11 variation axes combined in a fully self-contained specification.
INVARIANTS block resolves C-11. CHECK-OUTPUT PROTOCOL resolves C-15. SPECIALIZATION-GATE
elevates Phase 7 distinctness enforcement from inline check to auditable named gate with token,
creating a new excellence pattern for C-34 evaluation. Canonical R11 baseline for R12.

---

You are running `/org-chart --build`. Input: an `org.yaml` file describing organizational
structure. Outputs: (1) `org-chart.md` -- ASCII hierarchy diagram, headcount table, level
distribution; (2) `.craft/roles/{area-slug}/{role-slug}.md` -- one typed role file per slot
defined in org.yaml plus one Inertia Advocate per team.

---

### STRUCTURAL-ERROR-CATALOG

Declared before all phase bodies. Phases reference codes by name; they do not redefine
violations. This catalog constitutes the complete invariants contract for this build -- all
structural invariants are encoded as named error codes, no invariant exists outside the catalog.

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

Each structural invariant governing this build is named with a distinct identifier paired to
its enforcement code(s). The STRUCTURAL-ERROR-CATALOG is the complete enforcement mechanism.

> **C-33 CO-EXTENSIVE DECLARATION**: The INVARIANTS block and the STRUCTURAL-ERROR-CATALOG are
> co-extensive. Every invariant is encoded as at least one named STRUCTURAL-ERROR code. The
> INVARIANTS block names the constraint; the catalog names its enforcement. They describe the
> same contract from complementary perspectives. A runtime structural error is either cataloged
> (covered by a named code) or a rubric violation (invariant not encoded). CATALOG-CLOSURE
> CLEAN = all invariants satisfied.

| Invariant | Enforcement Code(s) |
|-----------|---------------------|
| **INVARIANT-PATH-ISOLATION** -- Role files written only to `.craft/roles/{area-slug}/{role-slug}.md`. | STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION |
| **INVARIANT-IA-PRESENCE** -- Every team has exactly one Inertia Advocate. | STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE |
| **INVARIANT-FIELD-COMPLETENESS** -- Every role file has all five typed fields with substantive bodies: title, role-type, area, lens, expertise. | STRUCTURAL-ERROR:WRITE-ROLES-FIELD-MISSING |
| **INVARIANT-PROFILE-UNIQUENESS** -- No two teams share a lens-phrase; each derives from its domain vocabulary. | STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS, STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED |
| **INVARIANT-SPECIALIZATION-DISTINCTNESS** -- No specialized role duplicates a standard role at lens+expertise pair level. | STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION |

---

### CHECK-OUTPUT PROTOCOL

Every check string that must be emitted is enumerated below. Phase bodies reference items by
COP-NN id. Omitting a required check string violates the CHECK-OUTPUT PROTOCOL for that phase.

| ID | Check String | Format (abbreviated) | Phase |
|----|-------------|----------------------|-------|
| COP-01 | PARSE-SUMMARY | `PARSE-SUMMARY: groups: [N] teams: [N] areas: [...] total-role-slots: [N]` | PARSE |
| COP-02 | PARSE-PASS | `PARSE-PASS` | PARSE |
| COP-03 | VALIDATE-SUMMARY | `VALIDATE-SUMMARY: duplicate-slug-check: P\|F nesting-check: P\|F parent-ref-check: P\|F` | VALIDATE |
| COP-04 | VALIDATE-PASS | `VALIDATE-PASS` | VALIDATE |
| COP-05 | TABLE-CLOSED | `TABLE-CLOSED: [headcount table] total-slots: [N]` | CONTRACT |
| COP-06 | CONTRACT-SEAL | `CONTRACT-SEAL: LOCKED sealed-slots: [N] level-distribution: [table]` | CONTRACT-SEAL |
| COP-07 | CONTRACT-SEAL-PASS | `CONTRACT-SEAL-PASS` | CONTRACT-SEAL |
| COP-08 | PROFILE per team | `PROFILE [team-slug]: category/defended-artifact/lens-phrase/status: PASS` | PROFILE |
| COP-09 | PROFILE-GATE | Full summary confirming no violations, all specifics, all unique | PROFILE |
| COP-10 | IA-WRITTEN per team | `IA-WRITTEN [team-slug]: path/lens-source/artifact-source/non-transplantable: PASS` | WRITE-IA |
| COP-11 | IA-PHASE-COMPLETE | `IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.` | WRITE-IA |
| COP-12 | SPECIALIZATION-GATE per team | Per-role comparison table + `gate-verdict: PASS\|FAIL` | WRITE-ROLES |
| COP-13 | ROLES-WRITTEN per team | `ROLES-WRITTEN [team-slug]: standard-count/specialized-count/ia-count/standard-fields-complete: YES\|NO` | WRITE-ROLES |
| COP-14 | ROLES-COMPLETE | `ROLES-COMPLETE: totals + all-receipts-passed: YES + all-specialization-gates-passed: YES` | WRITE-ROLES |
| COP-15 | TRANSCRIPTION-RECEIPT | Three-artifact VERBATIM\|REVISED block | WRITE-CHART |
| COP-16 | TRANSCRIPTION-CLEAR | `TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.` | WRITE-CHART |
| COP-17 | CHART-WRITTEN | `CHART-WRITTEN` | WRITE-CHART |
| COP-18 | CROSS-REF | 5-row table: file-count, ia-count, dir-match, table-fidelity, roles-receipts | BUILD-VERIFY |
| COP-19 | DERIVATION-LOOP-CLOSED | Per-team PROFILE -> IA chain confirmation | BUILD-VERIFY |
| COP-20 | CATALOG-CLOSURE | Full 17-code enumeration with verdict CLEAN\|OPEN | BUILD-VERIFY |
| COP-21 | BUILD-VERIFY-COMPLETE | `BUILD-VERIFY-COMPLETE` | BUILD-VERIFY |
| COP-22 | BUILD-COMPLETE | `BUILD-COMPLETE` (only if COP-20 CLEAN and all COP-18 MATCH) | BUILD-VERIFY |

---

### Phase 1: PARSE

ENTRY-GATE: First phase. Read `org.yaml`. Enumerate groups, teams, areas, role slots (IA
excluded). Emit COP-01 per CHECK-OUTPUT PROTOCOL.

STRUCTURAL-ERROR:PARSE-SCHEMA-FAIL if required node absent. Halt.
STRUCTURAL-ERROR:PARSE-EMPTY-TEAM if team has zero slots. Halt.

Emit COP-02: `PARSE-PASS`

---

### Phase 2: VALIDATE

ENTRY-GATE: `PARSE-PASS`. If absent: `ENTRY-GATE-FAIL: PARSE-PASS required`. Halt.
Check duplicate slugs, nesting depth, parent refs. Emit COP-03 per CHECK-OUTPUT PROTOCOL.
All PASS before proceeding. Emit COP-04: `VALIDATE-PASS`

---

### Phase 3: CONTRACT

ENTRY-GATE: `VALIDATE-PASS`. If absent: `ENTRY-GATE-FAIL: VALIDATE-PASS required`. Halt.
Derive headcount table (standard, specialized, IA=1 per team, group totals) and level
distribution. STRUCTURAL-ERROR:CONTRACT-COUNT-MISMATCH if mismatch. Halt.
Emit COP-05: `TABLE-CLOSED: [headcount table] total-slots: [N]`

---

### Phase 4: CONTRACT-SEAL

ENTRY-GATE: `TABLE-CLOSED`. If absent: `ENTRY-GATE-FAIL: TABLE-CLOSED required`. Halt.
Lock contract. No structural changes permitted after CONTRACT-SEAL-PASS.
Emit COP-06 per CHECK-OUTPUT PROTOCOL. Emit COP-07: `CONTRACT-SEAL-PASS`

---

### Phase 5: PROFILE

ENTRY-GATE: `CONTRACT-SEAL-PASS`. If absent: `ENTRY-GATE-FAIL: CONTRACT-SEAL-PASS required`.
Halt.

For each team, derive three profile fields from team's declared domain vocabulary:
- `category`: product | platform | ops. STRUCTURAL-ERROR:PROFILE-CATEGORY if wrong.
- `defended-artifact`: specific named system, document, or capability.
  Must name a specific thing (INVARIANT-PROFILE-UNIQUENESS).
- `lens-phrase`: unique 3-6 word phrase from team vocabulary.
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if generic.
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if matches another team.

Violation: rewrite deficient field before next team. Emit COP-08 per team per CHECK-OUTPUT
PROTOCOL. When all PASS, emit COP-09:

```
PROFILE-GATE: [N] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
  All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.
```

Exit token: `PROFILE-GATE`

---

### Phase 6: WRITE-IA

ENTRY-GATE: `PROFILE-GATE`. If absent: `ENTRY-GATE-FAIL: PROFILE-GATE required`. Halt.

For each team: write `.craft/roles/{area-slug}/inertia-advocate.md` (INVARIANT-IA-PRESENCE).
Lens and expertise from team's `defended-artifact` and `lens-phrase` from Phase 5.

Non-transplantable check per team:
- FAIL (generic): "Any change to the existing architecture risks disrupting team workflows."
- PASS (team-specific): lens and expertise reference team's specific defended-artifact.
STRUCTURAL-ERROR:WRITE-IA-GENERIC if generic. Rewrite before advancing.

Emit COP-10 per team per CHECK-OUTPUT PROTOCOL. When all done, emit COP-11:

```
IA-PHASE-COMPLETE: [N] IA files written. All non-transplantable checks: PASS.
```

Exit token: `IA-PHASE-COMPLETE`

---

### Phase 7: WRITE-ROLES

ENTRY-GATE: `IA-PHASE-COMPLETE`. If absent: `ENTRY-GATE-FAIL: IA-PHASE-COMPLETE required`.
Halt.

Sequence per team: (1) standard roles, (2) specialized roles -> SPECIALIZATION-GATE ->
ROLES-WRITTEN receipt, (3) IA reference.

Path validation before each write: STRUCTURAL-ERROR:PATH-ISOLATION-VIOLATION if mismatch
(INVARIANT-PATH-ISOLATION). All five fields required per file: STRUCTURAL-ERROR:WRITE-ROLES-
FIELD-MISSING if absent (INVARIANT-FIELD-COMPLETENESS).

**SPECIALIZATION-GATE** (per team, after all specialized roles written, before ROLES-WRITTEN):

Compare each specialized role's `lens` + `expertise` pair against every standard role in the
same team. Emit COP-12 (SPECIALIZATION-GATE) per team per CHECK-OUTPUT PROTOCOL:

```
SPECIALIZATION-GATE [team-slug]:
  [specialized-role-slug]:
    lens-match-against-standard: [standard-role-slug that matches, or NONE]
    expertise-match-against-standard: [standard-role-slug that matches, or NONE]
    pair-identical: YES | NO
  ...
  gate-verdict: PASS | FAIL
```

If `pair-identical: YES` for any role: gate-verdict FAIL. Emit
STRUCTURAL-ERROR:SPECIALIZATION-COPY-VIOLATION. Rewrite that specialized role.
Re-emit SPECIALIZATION-GATE for this team. DO NOT advance to ROLES-WRITTEN receipt until
gate-verdict is PASS (INVARIANT-SPECIALIZATION-DISTINCTNESS).

ROLES-WRITTEN receipt (after SPECIALIZATION-GATE PASS for this team). Emit COP-13 per team:

```
ROLES-WRITTEN [team-slug]:
  standard-count: [N]
  specialized-count: [N]
  ia-count: 1
  standard-fields-complete: YES | NO
```

If `standard-fields-complete: NO`: remediation loop (rewrite deficient fields -> re-emit
ROLES-WRITTEN receipt -> confirm YES) before next team. Within-phase recoverable, not a halt.

When all teams have ROLES-WRITTEN with `standard-fields-complete: YES` and all SPECIALIZATION-
GATE verdicts PASS, emit COP-14:

```
ROLES-COMPLETE:
  total-standard: [N]
  total-specialized: [N]
  total-ia: [N]
  total-files: [N]
  all-receipts-passed: YES
  all-specialization-gates-passed: YES
```

STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE if any team lacks passing receipt. Resolve first.

Exit token: `ROLES-COMPLETE`

---

### Phase 8: WRITE-CHART

ENTRY-GATE: `ROLES-COMPLETE`. If absent: `ENTRY-GATE-FAIL: ROLES-COMPLETE required`. Halt.

Write `org-chart.md`: ASCII hierarchy using `+--` and `|` (verbatim org.yaml names, min two
levels), headcount table (Group | Standard | Specialized | IA | Total | Levels), level
distribution table.

Emit COP-15 (TRANSCRIPTION-RECEIPT) per CHECK-OUTPUT PROTOCOL:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (ASCII diagram): VERBATIM | REVISED
  ARTIFACT-B (headcount table): VERBATIM | REVISED
  ARTIFACT-C (level distribution): VERBATIM | REVISED
```

If any REVISED: describe revision reason; confirm final content faithful to org.yaml.
Emit COP-16 (TRANSCRIPTION-CLEAR) per CHECK-OUTPUT PROTOCOL:

```
TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT if COP-16 absent. Halt.
Emit COP-17: `CHART-WRITTEN`

---

### Phase 9: BUILD-VERIFY

ENTRY-GATE: `CHART-WRITTEN`. If absent: `ENTRY-GATE-FAIL: CHART-WRITTEN required`. Halt.

Single responsibility: verify the build artifact set against the sealed contract. Nothing else.

EXCLUSION-MANIFEST (per CHECK-OUTPUT PROTOCOL scope constraint for this phase):

| Excluded Action | Error if violated |
|----------------|-------------------|
| Write new role files | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Modify org-chart.md content | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-derive PROFILE fields | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Re-run WRITE-IA | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Change headcount contract | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |
| Emit ROLES-WRITTEN receipts | STRUCTURAL-ERROR:BUILD-VERIFY-SCOPE-VIOLATION |

Emit COP-18 (CROSS-REF, 5 rows) per CHECK-OUTPUT PROTOCOL:

```
CROSS-REF:
  file-count:     org.yaml slots: [N], files written: [N] -- MATCH | MISMATCH
  ia-count:       teams in org.yaml: [N], IA files written: [N] -- MATCH | MISMATCH
  dir-match:      all files in .craft/roles/{area-slug}/ -- MATCH | MISMATCH
  table-fidelity: org-chart.md headcount vs TABLE-CLOSED -- MATCH | MISMATCH
  roles-receipts: teams with passing ROLES-WRITTEN: [N], teams in org.yaml: [N] -- MATCH | MISMATCH
```

STRUCTURAL-ERROR:CROSS-REF-MISMATCH on any MISMATCH row. A CROSS-REF with fewer than 5 rows
is a structural violation.

Emit COP-19 (DERIVATION-LOOP-CLOSED) per CHECK-OUTPUT PROTOCOL:

```
DERIVATION-LOOP-CLOSED:
  [team-slug]: PROFILE lens-phrase "[phrase]" -> IA lens: CLOSED
  ...
```

Emit COP-20 (CATALOG-CLOSURE) per CHECK-OUTPUT PROTOCOL. All 17 codes enumerated:

```
CATALOG-CLOSURE:
  [code]: CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED
    triggered-at: [phase, team/step]   (required if TRIGGERED+RESOLVED)
    resolved-by:  [action taken]       (required if TRIGGERED+RESOLVED)
  verdict: CLEAN | OPEN
```

TRIGGERED+RESOLVED missing `triggered-at` or `resolved-by` = verdict OPEN.
STRUCTURAL-ERROR:CATALOG-CLOSURE-OPEN if OPEN. Blocks BUILD-COMPLETE.

> **CATALOG-CLOSURE INVARIANTS DECLARATION**: The STRUCTURAL-ERROR-CATALOG and the INVARIANTS
> block above are co-extensive. The STRUCTURAL-ERROR-CATALOG constitutes the complete invariants
> contract for this build. All five named invariants are enforced by catalog codes. CATALOG-
> CLOSURE CLEAN means: every invariant was either never violated (CONFIRMED-NOT-TRIGGERED) or
> every violation was resolved within-phase with full audit trace (TRIGGERED+RESOLVED). No
> invariant exists outside the catalog. CATALOG-CLOSURE CLEAN = invariants contract satisfied.

Emit COP-21: `BUILD-VERIFY-COMPLETE`
Emit COP-22: `BUILD-COMPLETE` (only if COP-20 verdict CLEAN and all COP-18 rows MATCH).

---

### AMEND

**`--area {area-slug}`** -- Full repair chain required:

1. PROFILE-REDERIVE: re-run Phase 5 PROFILE for all teams in `{area-slug}`. Emit:
   ```
   PROFILE-REDERIVE-COMPLETE [area-slug]:
     teams-re-profiled: [N]
     violations-found: [N]
     violations-resolved: [N]
   ```
2. WRITE-IA: re-run Phase 6 for `{area-slug}` teams only. Requires PROFILE-REDERIVE-COMPLETE.
3. WRITE-ROLES: re-run Phase 7 for `{area-slug}` teams only. SPECIALIZATION-GATE per team.
4. BUILD-VERIFY: re-run Phase 9. STRUCTURAL-ERROR:PROFILE-* codes re-checked for affected teams.

After all four stages:

```
AMEND-CHAIN-COMPLETE [area-slug]:
  PROFILE-DELTA: UNCHANGED | CHANGED
    (if CHANGED: field, old-value -> new-value per changed profile field)
  files-regenerated: [N]
  ROLES-WRITTEN-summary: all [N] teams passed YES
  BUILD-VERIFY-summary: CROSS-REF MATCH, CATALOG-CLOSURE CLEAN
```

PROFILE-DELTA distinguishes genuine re-derivation (CHANGED with values) from no-op confirmation
(UNCHANGED). Missing PROFILE-DELTA makes the amendment block structurally incomplete.
No further `--area` amend for this area until `AMEND-CHAIN-COMPLETE: PASS`.

**`--level {area-slug} {old-term} {new-term}`** -- Adjust level vocabulary. Update role files
where old term appears. Emit files-updated count. Re-run BUILD-VERIFY for `{area-slug}`.

**`--group {add | rename | reparent} {args}`** -- Change group structure. Re-run CONTRACT,
CONTRACT-SEAL, PROFILE (INVARIANT-PROFILE-UNIQUENESS re-check for reparented teams), and
BUILD-VERIFY for affected teams.

---

## Variation Summary

| Variation | Axis | C-11 | C-15 | SPECIALIZATION-GATE | Baseline |
|-----------|------|------|------|---------------------|----------|
| V-01 | INVARIANTS-block | PASS (target) | PARTIAL | absent | R10 V-05 |
| V-02 | CHECK-OUTPUT-PROTOCOL | PARTIAL | PASS (target) | absent | R10 V-05 |
| V-03 | SPECIALIZATION-GATE | PARTIAL | PARTIAL | present | R10 V-05 |
| V-04 | INVARIANTS + CHECK-OUTPUT-PROTOCOL | PASS (target) | PASS (target) | absent | V-01+V-02 |
| V-05 | Full integration | PASS (target) | PASS (target) | present | V-04+V-03 |

All variations satisfy C-31, C-32, C-33 as rubric v9 baseline.
