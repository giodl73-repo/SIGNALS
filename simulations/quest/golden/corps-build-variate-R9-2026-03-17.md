---
skill: quest-variate
skill_target: corps-build
round: 9
date: 2026-03-17
rubric_version: 7
r8_scorecard: corps-build-scorecard-R8-2026-03-17.md
---

# Variate R9 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 9. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R8 scorecard: rubric v7 formalizes three criteria surfaced by R8 excellence signals --
C-25 (ENTRY-GATE bidirectional phase enforcement), C-26 (pre-execution STRUCTURAL-ERROR-CATALOG),
C-27 (PROFILE-phase typed violation taxonomy). These are now baseline criteria.
All three were satisfied by R8 V-01 through V-05 (with V-04 taking C-09 PARTIAL).

R9 baseline architecture (foundation for all five variations):
PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA -> WRITE-ROLES ->
WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
R8 V-05 is the baseline: all three R8 axes integrated (ENTRY-GATE tokens + upfront
STRUCTURAL-ERROR-CATALOG with 16 codes + PROFILE typed STRUCTURAL-ERROR codes +
PROFILE/IA named contrast pairs).

R9 explores three new axes that rubric v7 does not yet capture:

- WRITE-ROLES per-team verification receipt: rubric v7 enforces per-team output
  quality via IA-WRITTEN (four checks, including non-transplantable gate) in WRITE-IA.
  WRITE-ROLES emits only a phase-end ROLES-COMPLETE count -- no per-team receipt during
  the write loop. A ROLES-WRITTEN token after each team's standard and specialized roles
  are complete (confirming all five fields non-empty, specialized lens structurally
  distinct from all standard lenses on the same team) mirrors the IA-WRITTEN pattern
  and makes role quality auditable per-team rather than only as a phase-end aggregate.

- AMEND full-chain propagation: the current --area amend option runs IA-WRITTEN but
  not PROFILE. Since the lens-phrase is derived in PROFILE, regenerating an area's role
  files without re-deriving the resistance profile can introduce a PROFILE-IA consistency
  gap: a regenerated IA file could adopt a fresh lens-phrase not anchored in a sealed
  PROFILE for that area. Adding a PROFILE-REDERIVE step as the first action of --area
  amend propagates the regeneration from the correct upstream source, then flows through
  WRITE-IA -> IA-WRITTEN -> ROLES-WRITTEN -> BUILD-VERIFY for the amended area.

- CATALOG-CLOSURE attestation: the STRUCTURAL-ERROR-CATALOG is declared before Phase 1
  and referenced inline throughout execution. The catalog is a pre-execution promise, but
  there is no post-execution audit confirming each code was either triggered+resolved or
  confirmed-not-triggered. A CATALOG-CLOSURE block after CROSS-REF PASS enumerates every
  catalog code with its run-time disposition, turning the catalog into a closed-loop audit
  record. BUILD-COMPLETE is gated on CATALOG-CLOSURE: CLEAN.

---

## Variation Axes

| Axis | Used In |
|------|---------|
| ROLES-WRITTEN: per-team receipt in WRITE-ROLES with field-completeness and specialized-distinctness checks | V-01, V-04, V-05 |
| AMEND full-chain: --area amend begins with PROFILE-REDERIVE before WRITE-IA | V-02, V-04, V-05 |
| CATALOG-CLOSURE: post-execution audit block enumerating disposition of every catalog code | V-03, V-05 |

---

## V-01 -- ROLES-WRITTEN per-team verification receipt (C-28 candidate)

**Axis**: Per-team receipt in WRITE-ROLES
**Hypothesis**: IA-WRITTEN provides per-team feedback during WRITE-IA -- four checks after
each IA file, with a non-transplantable enforcement gate that halts the build if the lens is
generic. WRITE-ROLES emits no equivalent per-team signal; role quality is only observable at
phase-end via the ROLES-COMPLETE count. A skill runner could write 12 role files for four
teams and learn only after all writes that a specialized lens duplicated a standard lens on
team 3. Adding a ROLES-WRITTEN receipt after each team's standard and specialized files are
complete -- confirming all five fields are non-empty for every file, and that every
specialized lens is structurally distinct from all standard lenses on the same team --
mirrors the IA-WRITTEN per-team feedback loop. This should produce a candidate criterion
(C-28): the role-write phase must emit a per-team verification receipt confirming field
completeness and specialized distinctness before the next team's roles begin.
Does not include V-02's AMEND full-chain or V-03's CATALOG-CLOSURE.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Defined before Phase 1. Phase bodies reference
these codes by name; they do not re-define them.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT-A/B/C recalculated rather than transcribed from CONTRACT-SEAL |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | defended-artifact names a type or category rather than a specific named thing |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase uses vocabulary not present in defended-artifact or change-pressure |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two or more teams share an identical lens-phrase |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE emitted before all ROLES-WRITTEN receipts show passing verdicts |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from CONTRACT-SEAL |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit a parse manifest before writing any files:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list all Group/Division names]
  teams:
    [team name] (group: [parent]):
      standard: [role names or "none"]
      specialized: [role names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four structural checks:
1. Team name uniqueness within each group
2. Role slug uniqueness within each team
3. Area slug uniqueness across the org (no two teams produce the same `.roles/{slug}/`)
4. Nesting depth <= 3 (Division > Group > Team)

```
VALIDATE:
  [1] team name uniqueness within groups: [PASS | FAIL -- name duplicates]
  [2] role slug uniqueness within teams: [PASS | FAIL -- name duplicates]
  [3] area slug uniqueness across org: [PASS | FAIL -- name conflicts]
  [4] nesting depth <= 3: [PASS | FAIL -- [n] levels detected]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
Artifacts sealed here are source of truth for WRITE-CHART. Recalculation elsewhere:
STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3: structural observation not visible from rows alone. An ARTIFACT-B with no area
names is structurally invalid even if sentence count and format are correct.

**ARTIFACT-C -- Level Distribution**: breakdown by label if declared; else
`Level distribution: not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

ENTRY-GATE: TABLE-CLOSED required. If not present:
`ENTRY-GATE-FAIL: CONTRACT-SEAL requires TABLE-CLOSED from CONTRACT.`

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words of ARTIFACT-B...]
  ARTIFACT-C: SEALED -- [level summary or "not declared"]
  CONTRACT-SEAL-PASS
```

No modifications to sealed artifacts after this point.

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

Extract one resistance profile per team before writing any IA file.

**Typed violation codes for this phase (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY -- defended-artifact names a type/category
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED -- lens-phrase vocabulary absent from profile fields
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS -- two teams share identical lens-phrase

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision -- NOT a category;
                      must name the actual thing]
  change-pressure: [the specific proposed change threatening it; concrete;
                    NOT "change in general"]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact names a category
  rather than a specific thing -- rewrite before proceeding to next team.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses vocabulary absent from
  defended-artifact and change-pressure -- rewrite lens-phrase before next team.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two or more profiles share an identical
  lens-phrase -- rewrite at least one before PROFILE-GATE can be emitted.

Named failure mode contrast for defended-artifact quality:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture" --
  names a type; transplantable to any team; category label not a specific thing.
- PASS: "the event-resequencing buffer that preserves order during backpressure" --
  names the actual component; cannot be transplanted to a different team without rewriting.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write ALL Inertia Advocate files before ANY standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.roles/{area-slug}/inertia-advocate.md`:

Fields:
- **orientation**: grounds IA identity in this team's specific operational context; not
  generic change-resistance framing; names what this person is protecting and why it
  matters here
- **lens**: opens verbatim with the PROFILE lens-phrase for this team; extends it with
  1-2 sentences using this team's domain vocabulary
- **expertise**: names actual systems built, decisions owned, or failures survived in this
  domain -- not generic expertise labels; must name the actual things
- **scope**: tied to the specific defended-artifact from PROFILE; names the escalation
  path when change velocity exceeds tested capacity
- **collaboration-pattern**: surfaces concerns early; does not veto; asks: "what is the
  rollback plan, and has it been tested against production load?"

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES -- names this team's specific concern |
                         NO -- rewrite required before next team]
  expertise-concrete: [YES -- names actual systems or decisions in this domain |
                       NO -- rewrite required before next team]
  lens-phrase-verbatim: [YES -- lens opens with exact PROFILE phrase |
                         NO -- rewrite required before next team]
  lens-team-specific (non-transplantable): [YES -- uses vocabulary unique to this team's
    domain; a reader could not move this lens text verbatim to another team's IA |
    NO -- contains phrases applicable to any team's IA without modification;
    rewrite required before proceeding to next team's IA file]
```

Non-transplantable enforcement gate: a NO verdict on `lens-team-specific` halts the build.
The lens must be rewritten using this team's specific system names, process names, or known
failure modes. IA-WRITTEN must be re-emitted with YES on all four checks before the next
team's IA file begins.

Named failure mode contrast for non-transplantable check:
- FAIL (transplantable): "Any change to the existing architecture risks disrupting the
  team's current workflow" -- this phrase applies verbatim to any team's IA.
- PASS (team-specific): "The claim routing table's 847 active rule entries were audited
  manually every quarter because no automated validation existed" -- this cannot be
  transplanted to a different team without rewriting.

After all IA files:
`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team, including non-transplantable verification. All IA files written before standard and
specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE. All IA files must be written first.`

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- `role-type: specialized`; lens and expertise must
   name domain-specific systems distinguishing this role from standard roles on the same team;
   a specialized lens identical to any standard lens on the same team fails distinctness and
   requires rewrite.

After writing all standard and specialized files for each team, emit ROLES-WRITTEN:

```
ROLES-WRITTEN: [team name]
  standard-fields-complete: [YES -- all five fields non-empty for all [n] standard roles |
                              NO -- [role slug]: [field name] missing; rewrite required
                                   before proceeding to next team]
  specialized-count: [n files | "none declared"]
  specialized-distinctness: [YES -- each specialized lens names domain-specific systems
                              structurally distinct from all standard lenses on this team |
                              NOT-APPLICABLE -- no specialized roles declared |
                              NO -- [specialized role slug] lens duplicates [standard role slug]
                                   lens; rewrite required before proceeding to next team]
```

A NO verdict on `standard-fields-complete` or `specialized-distinctness` halts the build.
Rewrite the failing file(s). Re-emit ROLES-WRITTEN with passing verdicts before the next
team's roles begin. Emitting ROLES-COMPLETE before all ROLES-WRITTEN receipts show passing
verdicts triggers STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (catalog).

Named failure mode (specialized distinctness): "As a senior specialist, I bring expertise
across the full breadth of systems in this team's domain, with deeper focus on optimization
and performance" -- this lens is a scalar extension of a generic standard lens and does
not name the specific systems or contracts that distinguish the specialized role.

Named pass (specialized distinctness): "The schema negotiation contract between the ingest
layer and the three downstream consumers was written and owned by this role; any migration
that touches the contract surface requires this role's sign-off" -- names specific ownership
that no standard role on the team holds.

After all teams, write shared-group roles to `.roles/shared/` (role-type: shared-group)
and exec-office roles to `.roles/exec-office/` (role-type: exec-office) if declared.
Shared-group and exec-office roles also require ROLES-WRITTEN confirmation before phase gate.

Every role file: five non-empty fields (orientation, lens, expertise, scope,
collaboration-pattern) with substantive, non-"TBD" body text.

`ROLES-COMPLETE: [n] files written to .roles/. All ROLES-WRITTEN checks passed for
every team, shared-group, and exec-office section.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**Step 8a -- ASCII Hierarchy**

Use `+--` and `|`. All names verbatim from `org.yaml`. Every area from PARSE manifest
must appear. Minimum two nesting levels visible.

**Step 8b -- Transcription**

Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from CONTRACT-SEAL into org-chart.md.
Do not recalculate. Do not reformat. The sealed artifact is the source.

Emit TRANSCRIPTION-RECEIPT immediately after transcription:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

PATH-A shape (all VERBATIM after TRANSCRIPTION-RECEIPT):
```
PATH-A: all three artifacts VERBATIM.
CHART-WRITTEN.
```
A correct PATH-A output contains no TRANSCRIPTION-CLEAR block.
Emitting TRANSCRIPTION-CLEAR here triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

PATH-B shape (any REVISED in TRANSCRIPTION-RECEIPT):
```
[rewrite deviant artifact to match CONTRACT-SEAL version]
[re-emit TRANSCRIPTION-RECEIPT -- all verdicts should now be VERBATIM]
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```
CHART-WRITTEN before TRANSCRIPTION-CLEAR triggers STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT
(catalog). A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate all role files for that area; re-run IA-WRITTEN
   (all four checks, including non-transplantable) for regenerated IA; re-run ROLES-WRITTEN
   for regenerated area; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN. Complete WRITE-CHART first.`

This phase has exactly one responsibility: confirm each IA file's lens field opens verbatim
with the lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- these output types are out-of-scope for this phase (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks (total vs org.yaml slots) | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons or subdirectory audits | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount or ARTIFACT-A verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND section generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows or aggregate statistics | STRUCTURAL-ERROR:BV-SUMMARY |

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5 PROFILE for this team]"
  IA lens opens: "[first 8-12 words of the lens field in the written IA file]"
  VERDICT: [VERBATIM -- lens-phrase survives into written file |
            DRIFT -- lens-phrase absent or paraphrased in written file]
```

DRIFT verdict: rewrite the IA file so the lens field opens with the exact PROFILE
lens-phrase. Re-emit BUILD-VERIFY for that team with VERBATIM verdict. Do not proceed
to the next team until the current team shows VERBATIM.

After all teams VERBATIM:

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed.
  Each resistance profile is fully recoverable from the built IA file's lens opening.
```

A DERIVATION-LOOP-CLOSED block that names fewer than [n] teams is structurally incomplete.
A DERIVATION-LOOP-CLOSED block emitted before BUILD-VERIFY-COMPLETE is structurally invalid.

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE. Complete BUILD-VERIFY first.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [list all .roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-02 -- AMEND full-chain propagation (C-29 candidate)

**Axis**: AMEND --area triggers PROFILE-REDERIVE before WRITE-IA
**Hypothesis**: The --area amend option regenerates role files and re-runs IA-WRITTEN but
does not re-derive the resistance profile. PROFILE is the upstream source of IA quality:
it produces the lens-phrase that IA-WRITTEN checks at write time and BUILD-VERIFY confirms
at verification time. When a team's area is regenerated without re-deriving from PROFILE,
the regenerated IA could adopt a lens-phrase not anchored in the sealed profile vocabulary
for that team. This creates a PROFILE-IA consistency gap that the current --area amend
procedure cannot detect, because the existing profile is not re-validated against the
regeneration context. Adding PROFILE-REDERIVE as the first step of --area amend ensures
the resistance profile is freshly derived before any role files are written, carries all
three PROFILE typed codes (STRUCTURAL-ERROR:PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED,
PROFILE-DUPLICATE-LENS), and gates the re-write sequence on PROFILE-REDERIVE-COMPLETE
before proceeding to WRITE-IA, IA-WRITTEN, and BUILD-VERIFY for the amended area.
Expected candidate criterion (C-29): AMEND --area must re-derive the resistance profile
from source before regenerating role files; the full chain from PROFILE through BUILD-VERIFY
must be re-run for any amended area.
Does not include V-01's ROLES-WRITTEN or V-03's CATALOG-CLOSURE.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Defined before Phase 1. Phase bodies reference
these codes by name; they do not re-define them.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT-A/B/C recalculated rather than transcribed from CONTRACT-SEAL |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | defended-artifact names a type or category rather than a specific named thing |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase uses vocabulary not present in defended-artifact or change-pressure |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two or more teams share an identical lens-phrase |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from CONTRACT-SEAL |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit a parse manifest before writing any files:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list all Group/Division names]
  teams:
    [team name] (group: [parent]):
      standard: [role names or "none"]
      specialized: [role names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four structural checks:
1. Team name uniqueness within each group
2. Role slug uniqueness within each team
3. Area slug uniqueness across the org
4. Nesting depth <= 3 (Division > Group > Team)

```
VALIDATE:
  [1] team name uniqueness within groups: [PASS | FAIL -- name duplicates]
  [2] role slug uniqueness within teams: [PASS | FAIL -- name duplicates]
  [3] area slug uniqueness across org: [PASS | FAIL -- name conflicts]
  [4] nesting depth <= 3: [PASS | FAIL -- [n] levels detected]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
Artifacts sealed here are source of truth for WRITE-CHART. Recalculation elsewhere:
STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3: structural observation not visible from rows alone. An ARTIFACT-B with no area
names is structurally invalid even if sentence count and format are correct.

**ARTIFACT-C -- Level Distribution**: breakdown by label if declared; else
`Level distribution: not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

ENTRY-GATE: TABLE-CLOSED required. If not present:
`ENTRY-GATE-FAIL: CONTRACT-SEAL requires TABLE-CLOSED from CONTRACT.`

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words of ARTIFACT-B...]
  ARTIFACT-C: SEALED -- [level summary or "not declared"]
  CONTRACT-SEAL-PASS
```

No modifications to sealed artifacts after this point.

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

Extract one resistance profile per team before writing any IA file.

**Typed violation codes for this phase (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY -- defended-artifact names a type/category
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED -- lens-phrase vocabulary absent from profile fields
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS -- two teams share identical lens-phrase

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision -- NOT a category;
                      must name the actual thing]
  change-pressure: [the specific proposed change threatening it; concrete;
                    NOT "change in general"]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact names a category -- rewrite.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses absent vocabulary -- rewrite.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two profiles share a lens-phrase -- rewrite one.

Named failure mode contrast for defended-artifact quality:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture" --
  names a type; transplantable to any team; category label not a specific thing.
- PASS: "the event-resequencing buffer that preserves order during backpressure" --
  names the actual component; cannot be transplanted to a different team without rewriting.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write ALL Inertia Advocate files before ANY standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.roles/{area-slug}/inertia-advocate.md`:

Fields:
- **orientation**: grounds IA identity in this team's specific operational context
- **lens**: opens verbatim with the PROFILE lens-phrase; extends with team-domain vocabulary
- **expertise**: names actual systems built, decisions owned, or failures survived -- no
  generic labels; must name the actual things
- **scope**: tied to the specific defended-artifact from PROFILE
- **collaboration-pattern**: surfaces concerns early; does not veto; asks about rollback paths

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required before next team]
  expertise-concrete: [YES | NO -- rewrite required before next team]
  lens-phrase-verbatim: [YES | NO -- rewrite required before next team]
  lens-team-specific (non-transplantable): [YES -- vocabulary unique to this team's domain |
    NO -- transplantable phrases present; rewrite required before next team]
```

Non-transplantable enforcement gate: NO on `lens-team-specific` halts the build. Rewrite.
Re-emit IA-WRITTEN with YES on all four checks before next team's IA file.

Named failure mode contrast for non-transplantable check:
- FAIL (transplantable): "Any change to the existing architecture risks disrupting the
  team's current workflow" -- applies verbatim to any team's IA.
- PASS (team-specific): "The claim routing table's 847 active rule entries were audited
  manually every quarter because no automated validation existed."

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team, including non-transplantable verification. All IA files written before standard and
specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE. All IA files must be written first.`

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- `role-type: specialized`; lens and expertise must
   name domain-specific systems distinguishing this role from standard roles on the same team;
   a specialized lens identical to any standard lens on the same team fails distinctness and
   requires rewrite.

After all teams: shared-group roles to `.roles/shared/` (role-type: shared-group)
and exec-office roles to `.roles/exec-office/` (role-type: exec-office) if declared.

Every role file: five non-empty fields (orientation, lens, expertise, scope,
collaboration-pattern) with substantive, non-"TBD" body text.

`ROLES-COMPLETE: [n] files written to .roles/.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**Step 8a -- ASCII Hierarchy**

Use `+--` and `|`. All names verbatim from `org.yaml`. Every area from PARSE manifest
must appear. Minimum two nesting levels visible.

**Step 8b -- Transcription**

Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from CONTRACT-SEAL into org-chart.md.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
Emitting TRANSCRIPTION-CLEAR here triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

PATH-B (any REVISED): rewrite deviant artifact -> re-emit TRANSCRIPTION-RECEIPT -> confirm:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```

CHART-WRITTEN before TRANSCRIPTION-CLEAR triggers STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT
(catalog). A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": re-derive resistance profile for area (PROFILE-REDERIVE):
   emit a new PROFILE block for each team in the named area; apply all three
   STRUCTURAL-ERROR:PROFILE-* enforcement checks; emit:
   PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
   Then: regenerate all role files for that area; re-run IA-WRITTEN (all four checks,
   including non-transplantable) for regenerated IA; re-run BUILD-VERIFY for re-profiled
   teams with VERBATIM verdict; update ARTIFACT-A. PROFILE-REDERIVE must precede WRITE-IA
   for the amended area -- skipping re-derivation is a PROFILE-IA consistency gap.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN. Complete WRITE-CHART first.`

This phase has exactly one responsibility: confirm each IA file's lens field opens verbatim
with the lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- these output types are out-of-scope for this phase (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks (total vs org.yaml slots) | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons or subdirectory audits | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount or ARTIFACT-A verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND section generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows or aggregate statistics | STRUCTURAL-ERROR:BV-SUMMARY |

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5 PROFILE for this team]"
  IA lens opens: "[first 8-12 words of the lens field in the written IA file]"
  VERDICT: [VERBATIM | DRIFT]
```

DRIFT: rewrite IA file, re-emit BUILD-VERIFY with VERBATIM before next team.

After all teams VERBATIM:

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed.
  Each resistance profile is fully recoverable from the built IA file's lens opening.
```

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE. Complete BUILD-VERIFY first.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [list all .roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-03 -- CATALOG-CLOSURE attestation (C-30 candidate)

**Axis**: Post-execution catalog audit block
**Hypothesis**: The STRUCTURAL-ERROR-CATALOG (C-26) is declared before Phase 1 as a
pre-execution promise: every code that could trigger is named upfront. But there is no
post-execution audit confirming that each code was either triggered+resolved (a violation
occurred and was corrected before the build continued) or confirmed-not-triggered (the
phase completed without that code firing). Without CATALOG-CLOSURE, the catalog is a
reference document that goes unaudited. A catalog where some codes could theoretically
have fired without being detected produces a weaker structural guarantee than one where
every code is explicitly accounted for at build end. Adding a CATALOG-CLOSURE block after
CROSS-REF PASS -- enumerating each catalog code with its run-time disposition -- converts
the catalog from a reference into a closed-loop audit. BUILD-COMPLETE is gated on
CATALOG-CLOSURE: CLEAN; any code left OPEN blocks the build. Expected candidate criterion
(C-30): the structural error catalog must be audited at build completion with each code
either CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED; BUILD-COMPLETE requires
CATALOG-CLOSURE: CLEAN.
Does not include V-01's ROLES-WRITTEN or V-02's AMEND full-chain.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Defined before Phase 1. Phase bodies reference
these codes by name; they do not re-define them.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT-A/B/C recalculated rather than transcribed from CONTRACT-SEAL |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | defended-artifact names a type or category rather than a specific named thing |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase uses vocabulary not present in defended-artifact or change-pressure |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two or more teams share an identical lens-phrase |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from CONTRACT-SEAL |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit a parse manifest before writing any files:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list all Group/Division names]
  teams:
    [team name] (group: [parent]):
      standard: [role names or "none"]
      specialized: [role names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four structural checks:
1. Team name uniqueness within each group
2. Role slug uniqueness within each team
3. Area slug uniqueness across the org
4. Nesting depth <= 3 (Division > Group > Team)

```
VALIDATE:
  [1] team name uniqueness within groups: [PASS | FAIL -- name duplicates]
  [2] role slug uniqueness within teams: [PASS | FAIL -- name duplicates]
  [3] area slug uniqueness across org: [PASS | FAIL -- name conflicts]
  [4] nesting depth <= 3: [PASS | FAIL -- [n] levels detected]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
Recalculation elsewhere: STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3: structural observation not visible from rows alone.

**ARTIFACT-C -- Level Distribution**: by label if declared; else `not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

ENTRY-GATE: TABLE-CLOSED required. If not present:
`ENTRY-GATE-FAIL: CONTRACT-SEAL requires TABLE-CLOSED from CONTRACT.`

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words of ARTIFACT-B...]
  ARTIFACT-C: SEALED -- [level summary or "not declared"]
  CONTRACT-SEAL-PASS
```

No modifications to sealed artifacts after this point.

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

Extract one resistance profile per team before writing any IA file.

**Typed violation codes for this phase (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY -- defended-artifact names a type/category
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED -- lens-phrase vocabulary absent from profile fields
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS -- two teams share identical lens-phrase

For each team:

```
PROFILE: [team name]
  defended-artifact: [specific named thing -- NOT a category label]
  change-pressure: [specific proposed change; concrete]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact names a category -- rewrite.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses absent vocabulary -- rewrite.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two profiles share a lens-phrase -- rewrite one.

Named failure mode contrast for defended-artifact quality:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture"
- PASS: "the event-resequencing buffer that preserves order during backpressure"

After all team profiles:
`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write ALL Inertia Advocate files before ANY standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.roles/{area-slug}/inertia-advocate.md`.
Fields: orientation, lens (opens verbatim with PROFILE lens-phrase), expertise (names
actual systems), scope (tied to defended-artifact), collaboration-pattern.

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
  lens-team-specific (non-transplantable): [YES | NO -- rewrite required]
```

Non-transplantable enforcement gate: NO on `lens-team-specific` halts the build.
Re-emit IA-WRITTEN with YES before next team's IA file.

Named failure mode contrast:
- FAIL: "Any change to the existing architecture risks disrupting the team's current workflow"
- PASS: "The claim routing table's 847 active rule entries were audited manually every
  quarter because no automated validation existed"

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team. All IA files written before standard and specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE.`

Standard then specialized per team. Shared-group and exec-office after all teams if declared.
All five fields non-empty. Specialized lens must differ structurally from standard on same team.

`ROLES-COMPLETE: [n] files written to .roles/.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE.`

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**Step 8a**: ASCII Hierarchy -- `+--` / `|`; all names verbatim; minimum two nesting levels.

**Step 8b**: Transcription -- copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
TRANSCRIPTION-CLEAR in PATH-A triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

PATH-B (any REVISED): rewrite -> re-emit TRANSCRIPTION-RECEIPT -> confirm all VERBATIM:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```

CHART-WRITTEN before TRANSCRIPTION-CLEAR triggers STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT.

**Step 8d**: AMEND:
```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN (all four checks,
   including non-transplantable) for regenerated IA; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN.`

Single responsibility: confirm each IA lens opens verbatim with PROFILE lens-phrase.

EXCLUSION-MANIFEST (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows | STRUCTURAL-ERROR:BV-SUMMARY |

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
  VERDICT: [VERBATIM | DRIFT]
```

DRIFT: rewrite IA file, re-emit BUILD-VERIFY VERBATIM before next team.

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed. Resistance profiles fully recoverable from built files.
```

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [all .roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

After CROSS-REF PASS, before BUILD-COMPLETE, emit CATALOG-CLOSURE:

```
CATALOG-CLOSURE:
  STRUCTURAL-ERROR:PHASE-2-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:CONTRACT-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:CONTRACT-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-CATEGORY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:IA-OUT-OF-ORDER: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-COUNT-CHECK: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-DIR-AUDIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-HEADCOUNT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-AMEND: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-SUMMARY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  CATALOG-CLOSURE: [CLEAN -- all 16 codes accounted for |
                   OPEN: [list codes with unresolved violations] -- BUILD-COMPLETE blocked]
```

BUILD-COMPLETE is only emitted after CATALOG-CLOSURE: CLEAN. An OPEN code blocks the build.
Any code showing TRIGGERED but not explicitly resolved is treated as OPEN.

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## V-04 -- ROLES-WRITTEN + AMEND full-chain (V-01 + V-02)

**Axes**: Per-team WRITE-ROLES receipt + AMEND full-chain propagation from PROFILE source
**Hypothesis**: V-01 and V-02 address write-phase lifecycle integrity from complementary
angles. ROLES-WRITTEN (V-01) makes role quality auditable per-team during the forward
write pass -- surfacing field-completeness and distinctness failures after each team rather
than at phase end. AMEND full-chain (V-02) ensures that when a team is regenerated, the
derivation chain is re-run from the correct upstream source (PROFILE) before role files
are written. Together they close two separate audit gaps in the WRITE-ROLES lifecycle:
(1) per-team quality is invisible until ROLES-COMPLETE, and (2) amend re-writes start
mid-chain (IA-WRITTEN) rather than at chain origin (PROFILE). The risk is that combining
per-team receipts with expanded amend semantics increases WRITE-ROLES and AMEND section
length. The test is whether the added coverage holds all existing criteria without
compressing the phases that satisfy C-09 and C-22 quality bars.
Does not include V-03's CATALOG-CLOSURE.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Defined before Phase 1. Phase bodies reference
these codes by name; they do not re-define them.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT-A/B/C recalculated rather than transcribed from CONTRACT-SEAL |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | defended-artifact names a type or category rather than a specific named thing |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase uses vocabulary not present in defended-artifact or change-pressure |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two or more teams share an identical lens-phrase |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE emitted before all ROLES-WRITTEN receipts show passing verdicts |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from CONTRACT-SEAL |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list all Group/Division names]
  teams:
    [team name] (group: [parent]):
      standard: [role names or "none"]
      specialized: [role names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four checks: (1) team name uniqueness; (2) role slug uniqueness; (3) area slug uniqueness;
(4) nesting depth <= 3.

```
VALIDATE:
  [1] team name uniqueness within groups: [PASS | FAIL]
  [2] role slug uniqueness within teams: [PASS | FAIL]
  [3] area slug uniqueness across org: [PASS | FAIL]
  [4] nesting depth <= 3: [PASS | FAIL]
  VALIDATE-PASS
```

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
Recalculation elsewhere: STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B**: 2-3 sentences. Names at least two specific area names. Sentence 3:
structural observation not visible from rows alone.

**ARTIFACT-C**: level breakdown by label, or `not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

ENTRY-GATE: TABLE-CLOSED required. If not present:
`ENTRY-GATE-FAIL: CONTRACT-SEAL requires TABLE-CLOSED from CONTRACT.`

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words...]
  ARTIFACT-C: SEALED -- [level summary or "not declared"]
  CONTRACT-SEAL-PASS
```

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

**Typed violation codes (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS

For each team:

```
PROFILE: [team name]
  defended-artifact: [specific named thing -- NOT a category]
  change-pressure: [specific proposed change]
  lens-phrase: [exact phrase from defended-artifact + change-pressure vocabulary]
```

Enforcement: PROFILE-CATEGORY if category label; PROFILE-LENS-UNDERIVED if absent vocabulary;
PROFILE-DUPLICATE-LENS if two profiles share a phrase. Rewrite violating profiles before proceeding.

Named failure mode contrast:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture"
- PASS: "the event-resequencing buffer that preserves order during backpressure"

`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts specific. All lens-phrases derived from team vocabulary. All unique.`

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE.`

Write ALL IA files before ANY standard or specialized roles.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

Per team: `.roles/{area-slug}/inertia-advocate.md`.
Fields: orientation (team-specific), lens (opens verbatim with PROFILE lens-phrase; extends
with team domain), expertise (names actual systems), scope (tied to defended-artifact),
collaboration-pattern (early surfacing; no veto; rollback path questions).

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES -- names this team's specific concern |
                         NO -- rewrite required before next team]
  expertise-concrete: [YES -- names actual systems or decisions in this domain |
                       NO -- rewrite required before next team]
  lens-phrase-verbatim: [YES -- lens opens with exact PROFILE phrase |
                         NO -- rewrite required before next team]
  lens-team-specific (non-transplantable): [YES -- vocabulary unique to this team's domain |
    NO -- transplantable phrases present; rewrite required before next team]
```

Non-transplantable enforcement gate: NO halts build. Rewrite. Re-emit IA-WRITTEN YES before
next team.

Named failure mode contrast:
- FAIL: "Any change to the existing architecture risks disrupting the team's current workflow"
- PASS: "The claim routing table's 847 active rule entries were audited manually every
  quarter because no automated validation existed"

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed. All IA
files written before standard and specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE.`

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`
2. **Specialized roles** (if declared) -- `role-type: specialized`; lens and expertise must
   name domain-specific systems distinguishing from standard on same team; identical specialized
   and standard lens fails distinctness.

After all standard and specialized files for each team, emit ROLES-WRITTEN:

```
ROLES-WRITTEN: [team name]
  standard-fields-complete: [YES -- all five fields non-empty for all [n] standard roles |
                              NO -- [role slug]: [field] missing; rewrite required]
  specialized-count: [n | "none declared"]
  specialized-distinctness: [YES -- each specialized lens names domain-specific systems
                              structurally distinct from all standard lenses on this team |
                              NOT-APPLICABLE -- no specialized roles |
                              NO -- [specialized role] lens duplicates [standard role];
                                   rewrite required before next team]
```

NO on either verdict halts the build. Rewrite failing files. Re-emit ROLES-WRITTEN with
passing verdicts before next team begins.
Emitting ROLES-COMPLETE before all ROLES-WRITTEN pass triggers
STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (catalog).

Named failure mode (specialized distinctness):
"As a senior specialist, I bring expertise across the full breadth of systems in this
team's domain, with deeper focus on optimization" -- generic scalar extension of a
standard lens; no specific system ownership named.

Named pass (specialized distinctness):
"The schema negotiation contract between the ingest layer and the three downstream
consumers was written and owned by this role; any migration touching the contract surface
requires this role's sign-off" -- names specific ownership distinct from any standard role.

After all teams: shared-group and exec-office if declared.
Shared-group and exec-office also emit ROLES-WRITTEN before phase gate.

`ROLES-COMPLETE: [n] files written to .roles/. All ROLES-WRITTEN checks passed.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE.`

Write `org-chart.md`. Transcribes sealed artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**Step 8a**: `+--` / `|` hierarchy; all names verbatim; two nesting levels minimum.

**Step 8b**: Transcribe ARTIFACT-A, B, C verbatim.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
TRANSCRIPTION-CLEAR in PATH-A: STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

PATH-B (any REVISED): rewrite -> re-emit TRANSCRIPTION-RECEIPT -> all VERBATIM:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```

CHART-WRITTEN before TRANSCRIPTION-CLEAR: STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": re-derive resistance profile for area (PROFILE-REDERIVE):
   emit new PROFILE block for each team in the named area; enforce all three
   STRUCTURAL-ERROR:PROFILE-* checks; emit:
   PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
   Then: regenerate all role files for that area; re-run IA-WRITTEN (all four checks,
   including non-transplantable); re-run ROLES-WRITTEN for regenerated teams; re-run
   BUILD-VERIFY for re-profiled teams; update ARTIFACT-A.
   PROFILE-REDERIVE must precede WRITE-IA for the amended area.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, slugs, table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN.`

Single responsibility: confirm each IA lens opens verbatim with PROFILE lens-phrase.

EXCLUSION-MANIFEST (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows | STRUCTURAL-ERROR:BV-SUMMARY |

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
  VERDICT: [VERBATIM | DRIFT]
```

DRIFT: rewrite IA file, re-emit BUILD-VERIFY VERBATIM before next team.

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed.
```

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [slugs vs parse manifest -- MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-05 -- Full integration (V-01 + V-02 + V-03 + complete architecture)

**Axes**: ROLES-WRITTEN per-team receipt + AMEND full-chain propagation + CATALOG-CLOSURE
attestation
**Hypothesis**: All three R9 axes address audit gaps in the R8 V-05 baseline that v7
criteria do not yet capture. V-01 (ROLES-WRITTEN) makes role quality auditable per-team
during WRITE-ROLES rather than only at phase-end count. V-02 (AMEND full-chain) ensures
area regeneration re-derives from PROFILE before writing any role file, closing the
PROFILE-IA consistency gap in the amend path. V-03 (CATALOG-CLOSURE) converts the
STRUCTURAL-ERROR-CATALOG from a pre-execution promise into a post-execution closed-loop
audit, where every code is either confirmed-not-triggered or triggered+resolved before
BUILD-COMPLETE is emitted. Together they close three structural audit gaps operating at
different lifecycle points: per-write-team quality (V-01), amend chain origin (V-02),
and build-end catalog accountability (V-03). The expected excellence signal is that all
three gaps closing simultaneously produces a skill where no audit window -- forward write,
amend regeneration, or build completion -- is left without an observable, named closure
token.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Defined before Phase 1. Phase bodies reference
these codes by name; they do not re-define them.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT-A/B/C recalculated rather than transcribed from CONTRACT-SEAL |
| STRUCTURAL-ERROR:PROFILE-CATEGORY | PROFILE | defended-artifact names a type or category rather than a specific named thing |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | PROFILE | lens-phrase uses vocabulary not present in defended-artifact or change-pressure |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | PROFILE | two or more teams share an identical lens-phrase |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE | WRITE-ROLES | ROLES-COMPLETE emitted before all ROLES-WRITTEN receipts show passing verdicts |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from CONTRACT-SEAL |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit a parse manifest before writing any files:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list all Group/Division names]
  teams:
    [team name] (group: [parent]):
      standard: [role names or "none"]
      specialized: [role names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four structural checks:
1. Team name uniqueness within each group
2. Role slug uniqueness within each team
3. Area slug uniqueness across the org (no two teams produce the same `.roles/{slug}/`)
4. Nesting depth <= 3 (Division > Group > Team)

```
VALIDATE:
  [1] team name uniqueness within groups: [PASS | FAIL -- name duplicates]
  [2] role slug uniqueness within teams: [PASS | FAIL -- name duplicates]
  [3] area slug uniqueness across org: [PASS | FAIL -- name conflicts]
  [4] nesting depth <= 3: [PASS | FAIL -- [n] levels detected]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
Artifacts sealed here are source of truth for WRITE-CHART. Recalculation elsewhere:
STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3: structural observation not visible from rows alone. An ARTIFACT-B with no area
names is structurally invalid even if sentence count and format are correct.

**ARTIFACT-C -- Level Distribution**: breakdown by label if declared; else
`Level distribution: not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

ENTRY-GATE: TABLE-CLOSED required. If not present:
`ENTRY-GATE-FAIL: CONTRACT-SEAL requires TABLE-CLOSED from CONTRACT.`

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words of ARTIFACT-B...]
  ARTIFACT-C: SEALED -- [level summary or "not declared"]
  CONTRACT-SEAL-PASS
```

No modifications to sealed artifacts after this point.

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

Extract one resistance profile per team before writing any IA file.

**Typed violation codes for this phase (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY -- defended-artifact names a type/category
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED -- lens-phrase vocabulary absent from profile fields
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS -- two teams share identical lens-phrase

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision -- NOT a category;
                      must name the actual thing]
  change-pressure: [the specific proposed change threatening it; concrete;
                    NOT "change in general"]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact names a category
  rather than a specific thing -- rewrite before proceeding to next team.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses vocabulary absent from
  defended-artifact and change-pressure -- rewrite lens-phrase before next team.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two or more profiles share an identical
  lens-phrase -- rewrite at least one before PROFILE-GATE can be emitted.

Named failure mode contrast for defended-artifact quality:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture" --
  names a type; transplantable to any team; category label not a specific thing.
- PASS: "the event-resequencing buffer that preserves order during backpressure" --
  names the actual component; cannot be transplanted to a different team without rewriting.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write ALL Inertia Advocate files before ANY standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.roles/{area-slug}/inertia-advocate.md`:

Fields:
- **orientation**: grounds IA identity in this team's specific operational context; not
  generic change-resistance framing; names what this person is protecting and why it
  matters here
- **lens**: opens verbatim with the PROFILE lens-phrase for this team; extends it with
  1-2 sentences using this team's domain vocabulary
- **expertise**: names actual systems built, decisions owned, or failures survived in this
  domain -- not generic expertise labels; must name the actual things
- **scope**: tied to the specific defended-artifact from PROFILE; names the escalation
  path when change velocity exceeds tested capacity
- **collaboration-pattern**: surfaces concerns early; does not veto; asks: "what is the
  rollback plan, and has it been tested against production load?"

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES -- names this team's specific concern |
                         NO -- rewrite required before next team]
  expertise-concrete: [YES -- names actual systems or decisions in this domain |
                       NO -- rewrite required before next team]
  lens-phrase-verbatim: [YES -- lens opens with exact PROFILE phrase |
                         NO -- rewrite required before next team]
  lens-team-specific (non-transplantable): [YES -- uses vocabulary unique to this team's
    domain; a reader could not move this lens text verbatim to another team's IA |
    NO -- contains phrases applicable to any team's IA without modification;
    rewrite required before proceeding to next team's IA file]
```

Non-transplantable enforcement gate: a NO verdict on `lens-team-specific` halts the build.
The lens must be rewritten using this team's specific system names, process names, or known
failure modes. IA-WRITTEN must be re-emitted with YES on all four checks before the next
team's IA file begins.

Named failure mode contrast for non-transplantable check:
- FAIL (transplantable): "Any change to the existing architecture risks disrupting the
  team's current workflow" -- this phrase applies verbatim to any team's IA.
- PASS (team-specific): "The claim routing table's 847 active rule entries were audited
  manually every quarter because no automated validation existed" -- this cannot be
  transplanted to a different team without rewriting.

After all IA files:
`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team, including non-transplantable verification. All IA files written before standard and
specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE. All IA files must be written first.`

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- `role-type: specialized`; lens and expertise must
   name domain-specific systems distinguishing this role from standard roles on the same team;
   a specialized lens identical to any standard lens on the same team fails distinctness and
   requires rewrite.

After writing all standard and specialized files for each team, emit ROLES-WRITTEN:

```
ROLES-WRITTEN: [team name]
  standard-fields-complete: [YES -- all five fields non-empty for all [n] standard roles |
                              NO -- [role slug]: [field name] missing; rewrite required
                                   before proceeding to next team]
  specialized-count: [n files | "none declared"]
  specialized-distinctness: [YES -- each specialized lens names domain-specific systems
                              structurally distinct from all standard lenses on this team |
                              NOT-APPLICABLE -- no specialized roles declared |
                              NO -- [specialized role slug] lens duplicates [standard role slug]
                                   lens; rewrite required before proceeding to next team]
```

A NO verdict on `standard-fields-complete` or `specialized-distinctness` halts the build.
Rewrite the failing file(s). Re-emit ROLES-WRITTEN with passing verdicts before the next
team's roles begin. Emitting ROLES-COMPLETE before all ROLES-WRITTEN receipts show passing
verdicts triggers STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (catalog).

Named failure mode (specialized distinctness):
"As a senior specialist, I bring expertise across the full breadth of systems in this
team's domain, with deeper focus on optimization and performance" -- generic scalar
extension of a standard lens; no specific system ownership named.

Named pass (specialized distinctness):
"The schema negotiation contract between the ingest layer and the three downstream
consumers was written and owned by this role; any migration touching the contract surface
requires this role's sign-off" -- names specific ownership no standard role holds.

After all teams: shared-group and exec-office if declared, also with ROLES-WRITTEN receipts.

Every role file: five non-empty fields (orientation, lens, expertise, scope,
collaboration-pattern) with substantive, non-"TBD" body text.

`ROLES-COMPLETE: [n] files written to .roles/. All ROLES-WRITTEN checks passed for
every team, shared-group, and exec-office section.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**Step 8a -- ASCII Hierarchy**

Use `+--` and `|`. All names verbatim from `org.yaml`. Every area from PARSE manifest
must appear. Minimum two nesting levels visible.

**Step 8b -- Transcription**

Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from CONTRACT-SEAL into org-chart.md.
Do not recalculate. Do not reformat. The sealed artifact is the source.

Emit TRANSCRIPTION-RECEIPT immediately after transcription:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

PATH-A shape (all VERBATIM after TRANSCRIPTION-RECEIPT):
```
PATH-A: all three artifacts VERBATIM.
CHART-WRITTEN.
```
A correct PATH-A output contains no TRANSCRIPTION-CLEAR block.
Emitting TRANSCRIPTION-CLEAR here triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

PATH-B shape (any REVISED in TRANSCRIPTION-RECEIPT):
```
[rewrite deviant artifact to match CONTRACT-SEAL version]
[re-emit TRANSCRIPTION-RECEIPT -- all verdicts should now be VERBATIM]
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```
CHART-WRITTEN before TRANSCRIPTION-CLEAR triggers STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT
(catalog). A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": re-derive resistance profile for area (PROFILE-REDERIVE):
   emit new PROFILE block for each team in the named area; enforce all three
   STRUCTURAL-ERROR:PROFILE-* checks (PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED,
   PROFILE-DUPLICATE-LENS); emit:
   PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
   Then: regenerate all role files for that area; re-run IA-WRITTEN (all four checks,
   including non-transplantable) for regenerated IA; re-run ROLES-WRITTEN for regenerated
   teams; re-run BUILD-VERIFY for re-profiled teams with VERBATIM verdict before
   re-emitting DERIVATION-LOOP-CLOSED for those teams; update ARTIFACT-A.
   PROFILE-REDERIVE must precede WRITE-IA for the amended area -- skipping re-derivation
   is a PROFILE-IA consistency gap that blocks build closure.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN. Complete WRITE-CHART first.`

This phase has exactly one responsibility: confirm each IA file's lens field opens verbatim
with the lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- these output types are out-of-scope for this phase (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks (total vs org.yaml slots) | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons or subdirectory audits | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount or ARTIFACT-A verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND section generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows or aggregate statistics | STRUCTURAL-ERROR:BV-SUMMARY |

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5 PROFILE for this team]"
  IA lens opens: "[first 8-12 words of the lens field in the written IA file]"
  VERDICT: [VERBATIM -- lens-phrase survives into written file |
            DRIFT -- lens-phrase absent or paraphrased in written file]
```

DRIFT verdict: rewrite the IA file so the lens field opens with the exact PROFILE
lens-phrase. Re-emit BUILD-VERIFY for that team with VERBATIM verdict. Do not proceed
to the next team until the current team shows VERBATIM.

After all teams VERBATIM:

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed.
  Each resistance profile is fully recoverable from the built IA file's lens opening.
```

A DERIVATION-LOOP-CLOSED block that names fewer than [n] teams is structurally incomplete.
A DERIVATION-LOOP-CLOSED block emitted before BUILD-VERIFY-COMPLETE is structurally invalid.

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE. Complete BUILD-VERIFY first.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [list all .roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

After CROSS-REF PASS, before BUILD-COMPLETE, emit CATALOG-CLOSURE:

```
CATALOG-CLOSURE:
  STRUCTURAL-ERROR:PHASE-2-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:CONTRACT-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:CONTRACT-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-CATEGORY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:IA-OUT-OF-ORDER: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-COUNT-CHECK: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-DIR-AUDIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-HEADCOUNT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-AMEND: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  STRUCTURAL-ERROR:BV-SUMMARY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  CATALOG-CLOSURE: [CLEAN -- all 17 codes accounted for |
                   OPEN: [list codes with unresolved violations] -- BUILD-COMPLETE blocked]
```

BUILD-COMPLETE is only emitted after CATALOG-CLOSURE: CLEAN.
Any code showing TRIGGERED but not explicitly resolved is treated as OPEN and blocks the build.

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## Candidate Criteria for Rubric v8

### Signal 1 -- WRITE-ROLES per-team verification receipt (V-01, V-04, V-05)

IA-WRITTEN provides per-team feedback at WRITE-IA with a non-transplantable enforcement
gate. WRITE-ROLES has no equivalent. V-01 adds ROLES-WRITTEN after each team's standard
and specialized files, confirming all five fields are non-empty and that each specialized
lens is structurally distinct from standard lenses on the same team. A named failure mode
contrast (generic scalar extension vs. specific contract ownership) mirrors the IA-WRITTEN
contrast structure. The gate enforces per-team quality before the next team's roles begin
rather than surfacing problems only at ROLES-COMPLETE count.

**Candidate C-28**: WRITE-ROLES must emit a per-team ROLES-WRITTEN receipt after each
team's role files confirming field completeness and specialized-lens distinctness; a NO
verdict must halt the build before the next team begins; emitting ROLES-COMPLETE before
all ROLES-WRITTEN receipts pass triggers STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE.

### Signal 2 -- AMEND full-chain propagation from PROFILE source (V-02, V-04, V-05)

The current --area amend sequence re-runs IA-WRITTEN but not PROFILE. Since PROFILE is the
upstream source of the lens-phrase that BUILD-VERIFY confirms, a regenerated IA file could
adopt a lens-phrase not anchored in a re-derived profile. V-02 adds PROFILE-REDERIVE as the
first step of --area amend, followed by WRITE-IA -> IA-WRITTEN -> ROLES-WRITTEN ->
BUILD-VERIFY for the amended area. The PROFILE-REDERIVE-COMPLETE gate (emitted after re-
deriving all teams in the area with no PROFILE-* violations) makes amend-path PROFILE
compliance as observable as forward-path PROFILE compliance.

**Candidate C-29**: AMEND --area must include a PROFILE-REDERIVE step as the first action,
emitting PROFILE-REDERIVE-COMPLETE before WRITE-IA begins for the amended area; re-running
IA-WRITTEN without PROFILE-REDERIVE is a PROFILE-IA consistency gap.

### Signal 3 -- CATALOG-CLOSURE post-execution audit (V-03, V-05)

The STRUCTURAL-ERROR-CATALOG (C-26) is a pre-execution promise. Without a post-execution
audit, the catalog is an unvalidated claim. V-03 adds a CATALOG-CLOSURE block after
CROSS-REF PASS that enumerates every catalog code with its run-time disposition:
CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED. BUILD-COMPLETE is gated on
CATALOG-CLOSURE: CLEAN; any OPEN code blocks the build. This converts the catalog from
a reference document into a closed-loop audit record where catalog completeness is
verifiable both at build start (pre-execution catalog table) and at build end (closure
attestation).

**Candidate C-30**: the structural error catalog must be audited at build completion with
each code either CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED; BUILD-COMPLETE requires
CATALOG-CLOSURE: CLEAN; any catalog code without an explicit disposition is treated as OPEN.

---

```json
{"round": 9, "rubric_version": 7, "baseline": "R8 V-05", "new_axes": ["ROLES-WRITTEN per-team receipt in WRITE-ROLES with field-completeness and specialized-distinctness checks", "AMEND full-chain propagation beginning with PROFILE-REDERIVE before WRITE-IA for any amended area", "CATALOG-CLOSURE post-execution audit block enumerating disposition of every catalog code before BUILD-COMPLETE"], "candidate_criteria": ["C-28: ROLES-WRITTEN per-team receipt with halt on NO verdict", "C-29: AMEND --area requires PROFILE-REDERIVE before WRITE-IA", "C-30: CATALOG-CLOSURE attestation gates BUILD-COMPLETE on all codes accounted for"]}
```
