---
skill: quest-variate
skill_target: corps-build
round: 10
date: 2026-03-17
rubric_version: 8
r9_scorecard: corps-build-scorecard-R9-2026-03-17.md
---

# Variate R10 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 10. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R9 scorecard: rubric v8 formalizes three criteria surfaced by R9 excellence signals --
C-28 (ROLES-WRITTEN per-team field-completeness receipt), C-29 (AMEND --area full-chain
re-derivation with PROFILE-REDERIVE gate), C-30 (CATALOG-CLOSURE terminal attestation).
These are now baseline criteria satisfied by all R10 variations.

R10 baseline architecture (foundation for all five variations):
PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA -> WRITE-ROLES ->
WRITE-CHART -> BUILD-VERIFY -> CROSS-REF (with CATALOG-CLOSURE before BUILD-COMPLETE).
R9 V-05 is the baseline: all three R9 axes integrated (ROLES-WRITTEN per-team receipts +
AMEND full-chain PROFILE-REDERIVE gating + CATALOG-CLOSURE terminal attestation).

R10 explores three new axes that rubric v8 does not yet capture:

- CROSS-REF ROLES-RECEIPT check: rubric v8 enforces ROLES-WRITTEN per-team receipts
  during WRITE-ROLES (C-28). But CROSS-REF does not confirm that every team emitted a
  passing ROLES-WRITTEN receipt -- it only checks file count, IA count, dir match, and
  table fidelity. A `roles-receipts` row in CROSS-REF that compares the count of teams
  with passing ROLES-WRITTEN verdicts against the org.yaml team count closes the audit
  gap between write-time enforcement (per-team gate) and build-time verification (CROSS-REF).
  A MISMATCH on this row blocks CROSS-REF PASS identically to the existing file-count check.

- CATALOG-CLOSURE triggered-trace: rubric v8 requires CATALOG-CLOSURE to enumerate every
  catalog code with its disposition (CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED). When
  a code shows TRIGGERED+RESOLVED, the current format records only the disposition -- not
  where in the build it triggered or what action resolved it. Adding a per-code
  `triggered-at: [phase] | resolved-by: [action taken]` annotation for any
  TRIGGERED+RESOLVED entry converts the closure attestation from a binary verdict log
  into an auditable trace. Any TRIGGERED+RESOLVED entry missing triggered-at or resolved-by
  is treated as OPEN and blocks BUILD-COMPLETE.

- AMEND-CHAIN-COMPLETE exit token: rubric v8 requires AMEND --area to run the full
  PROFILE-REDERIVE -> IA-WRITTEN -> BUILD-VERIFY chain with PROFILE-REDERIVE-COMPLETE
  as a named phase-exit gate (C-29). But after the full chain completes, there is no
  named terminal token confirming end-to-end propagation. Adding AMEND-CHAIN-COMPLETE
  after BUILD-VERIFY for the amended area -- with four required fields: area name,
  PROFILE-DELTA (what changed or confirmed unchanged), files-regenerated count,
  ROLES-WRITTEN-summary, and BUILD-VERIFY-summary -- converts AMEND from a gated repair
  sequence into a closed-loop amendment record. PROFILE-DELTA is the critical innovation:
  it exposes whether re-derivation produced materially different values (genuine amendment)
  or confirmed the originals (no-op re-derivation).

---

## Variation Axes

| Axis | Used In |
|------|---------|
| CROSS-REF ROLES-RECEIPT: `roles-receipts` row in CROSS-REF verifying all teams emitted passing ROLES-WRITTEN | V-01, V-04, V-05 |
| CATALOG-CLOSURE triggered-trace: `triggered-at` + `resolved-by` annotations for TRIGGERED+RESOLVED codes | V-02, V-04, V-05 |
| AMEND-CHAIN-COMPLETE: terminal token after AMEND --area full chain with PROFILE-DELTA and BUILD-VERIFY summary | V-03, V-05 |

---

## V-01 -- CROSS-REF ROLES-RECEIPT check (C-31 candidate)

**Axis**: ROLES-WRITTEN receipt audit in CROSS-REF
**Hypothesis**: C-28 adds a per-team ROLES-WRITTEN receipt during WRITE-ROLES that gates
each team's write sequence on `standard-fields-complete: YES` and `specialized-distinctness:
YES` (or NOT-APPLICABLE). This enforcement fires at write time -- after each team's files
are written. But CROSS-REF, which is the build's terminal audit phase, does not verify that
all teams emitted passing receipts. The current CROSS-REF checks file count, IA count, dir
match, and table fidelity. A skill runner could skip ROLES-WRITTEN for one team, write the
files anyway, and reach CROSS-REF PASS if the file count matched. Adding a `roles-receipts:
[n teams with passing ROLES-WRITTEN] = [n teams in org.yaml] -- [MATCH | MISMATCH]` row to
CROSS-REF closes this gap. It makes receipt completeness a build-time verification criterion,
not only a write-time enforcement signal. A MISMATCH on this row blocks CROSS-REF PASS and
therefore BUILD-COMPLETE. Expected candidate criterion (C-31): CROSS-REF must include a
roles-receipts row verifying that every team emitted a passing ROLES-WRITTEN receipt;
MISMATCH blocks CROSS-REF PASS.
Does not include V-02's CATALOG triggered-trace or V-03's AMEND-CHAIN-COMPLETE token.

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
3. Area slug uniqueness across the org (no two teams produce the same `.craft/roles/{slug}/`)
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

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`:

Fields:
- **orientation**: grounds IA identity in this team's specific operational context; not
  generic change-resistance framing; names what this person is protecting and why it matters
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
Rewrite using this team's specific system names, process names, or known failure modes.
IA-WRITTEN must be re-emitted with YES on all four checks before the next team's IA file begins.

Named failure mode contrast for non-transplantable check:
- FAIL (transplantable): "Any change to the existing architecture risks disrupting the
  team's current workflow" -- applies verbatim to any team's IA.
- PASS (team-specific): "The claim routing table's 847 active rule entries were audited
  manually every quarter because no automated validation existed" -- cannot be transplanted.

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
   a specialized lens identical to any standard lens on the same team fails distinctness.

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

NO verdict on `standard-fields-complete` or `specialized-distinctness` halts the build.
Rewrite. Re-emit ROLES-WRITTEN with passing verdicts before next team begins.
ROLES-COMPLETE before all ROLES-WRITTEN passing:
STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (catalog).

Named failure mode (specialized distinctness): "As a senior specialist, I bring expertise
across the full breadth of systems in this team's domain, with deeper focus on optimization
and performance" -- scalar extension of generic standard lens; does not name specific systems.

Named pass (specialized distinctness): "The schema negotiation contract between the ingest
layer and the three downstream consumers was written and owned by this role; any migration
that touches the contract surface requires this role's sign-off."

After all teams, write shared-group roles to `.craft/roles/shared/` (role-type: shared-group)
and exec-office roles to `.craft/roles/exec-office/` (role-type: exec-office) if declared.
Shared-group and exec-office roles also require ROLES-WRITTEN before phase gate.

`ROLES-COMPLETE: [n] files written to .craft/roles/. All ROLES-WRITTEN checks passed for
every team, shared-group, and exec-office section.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.
Recalculating: STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

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
TRANSCRIPTION-CLEAR in PATH-A: STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

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

CHART-WRITTEN before TRANSCRIPTION-CLEAR: STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": re-derive resistance profile for area (PROFILE-REDERIVE):
   emit a new PROFILE block for each team in the named area; apply all three
   STRUCTURAL-ERROR:PROFILE-* enforcement checks; emit:
   PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
   Then: regenerate all role files for that area; re-run IA-WRITTEN (all four checks,
   including non-transplantable) for regenerated IA; re-run ROLES-WRITTEN for regenerated
   area; re-run BUILD-VERIFY for re-profiled teams with VERBATIM verdict; update ARTIFACT-A.
   PROFILE-REDERIVE must precede WRITE-IA for the amended area -- skipping re-derivation
   is a PROFILE-IA consistency gap.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN. Complete WRITE-CHART first.`

Single responsibility: confirm each IA file's lens field opens verbatim with the
lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- out-of-scope for this phase (all codes in catalog):

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

DRIFT: rewrite IA file, re-emit BUILD-VERIFY VERBATIM before next team.

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
  dir check: [list all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  roles-receipts: [n teams with passing ROLES-WRITTEN verdicts] of [n teams in org.yaml]
                  -- [MATCH -- all teams emitted passing receipts |
                     MISMATCH -- [team names] missing or failing ROLES-WRITTEN]
  CROSS-REF: [PASS -- all five rows MATCH | FAIL -- list any MISMATCH]
```

MISMATCH on `roles-receipts` blocks CROSS-REF PASS identically to a file-count mismatch.
A CROSS-REF PASS that omits the `roles-receipts` row is structurally incomplete.

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

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## V-02 -- CATALOG-CLOSURE triggered-trace (C-32 candidate)

**Axis**: Per-code triggered-at + resolved-by annotations in CATALOG-CLOSURE
**Hypothesis**: C-30 requires CATALOG-CLOSURE to enumerate every catalog code with a
binary disposition: CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED. This attestation confirms
no code ended the build unresolved -- but it does not record where in the build each triggered
code fired or what action resolved it. A TRIGGERED+RESOLVED disposition on
STRUCTURAL-ERROR:PROFILE-CATEGORY tells a reviewer "this error fired and was fixed" but not
"this fired in Phase 5 during team Ingest at the defended-artifact quality check, and was
resolved by rewriting from 'the pipeline architecture' to 'the event-resequencing buffer'."
Without triggered-at and resolved-by, CATALOG-CLOSURE is an outcome attestation; with them
it is an audit trace. Adding per-code annotation for any TRIGGERED+RESOLVED entry --
`triggered-at: [phase name, which team or step] | resolved-by: [the action that cleared it]`
-- makes the closure block a recoverable record of every violation and its resolution. Any
TRIGGERED+RESOLVED entry that omits triggered-at or resolved-by is treated as OPEN, blocking
CATALOG-CLOSURE: CLEAN and therefore BUILD-COMPLETE.
Expected candidate criterion (C-32): CATALOG-CLOSURE must annotate each TRIGGERED+RESOLVED
code with triggered-at and resolved-by; missing annotations on triggered codes are OPEN.
Does not include V-01's CROSS-REF ROLES-RECEIPT or V-03's AMEND-CHAIN-COMPLETE token.

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

Phases 1-7 (PARSE through WRITE-ROLES): identical to V-01, including all ENTRY-GATE tokens,
full STRUCTURAL-ERROR-CATALOG references, ROLES-WRITTEN per-team receipts with
standard-fields-complete and specialized-distinctness checks, and STRUCTURAL-ERROR:
ROLES-COMPLETE-PREMATURE enforcement.

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE.`

Write `org-chart.md`. Transcribes sealed artifacts verbatim.
Recalculating: STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

Step 8a: ASCII Hierarchy -- `+--` / `|`; all names verbatim; two+ nesting levels.

Step 8b/8c: Transcription, TRANSCRIPTION-RECEIPT, PATH-A / PATH-B as in V-01.

Step 8d: AMEND:
```
AMEND:
1. --area "[area name]": PROFILE-REDERIVE chain:
   emit full PROFILE block for each team in area; apply all PROFILE-* checks;
   PROFILE-REDERIVE-COMPLETE: [area], [n] teams re-profiled. No violations.
   Regenerate role files; re-run IA-WRITTEN; re-run ROLES-WRITTEN; re-run BUILD-VERIFY;
   update ARTIFACT-A. PROFILE-REDERIVE must precede WRITE-IA for the amended area.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN.`

Single responsibility: confirm each IA lens verbatim with PROFILE lens-phrase.
EXCLUSION-MANIFEST, per-team BUILD-VERIFY block, DERIVATION-LOOP-CLOSED as in V-01.

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: CROSS-REF requires BUILD-VERIFY-COMPLETE.`

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

After CROSS-REF PASS, emit CATALOG-CLOSURE with triggered-trace annotations.
For each TRIGGERED+RESOLVED entry, `triggered-at` and `resolved-by` are required.
A TRIGGERED+RESOLVED entry without both fields is treated as OPEN and blocks BUILD-COMPLETE.

```
CATALOG-CLOSURE:
  STRUCTURAL-ERROR:PHASE-2-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase name, step or team name]
      resolved-by: [action that cleared this violation]]
  STRUCTURAL-ERROR:CONTRACT-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase name, step or team name]
      resolved-by: [action that cleared this violation]]
  STRUCTURAL-ERROR:CONTRACT-RECALC: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-CATEGORY: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:IA-OUT-OF-ORDER: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-RECALC: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-COUNT-CHECK: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-DIR-AUDIT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-HEADCOUNT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-AMEND: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-SUMMARY: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  CATALOG-CLOSURE: [CLEAN -- all 17 codes accounted for; all TRIGGERED+RESOLVED entries
                   carry triggered-at and resolved-by |
                   OPEN: [list codes missing annotations or unresolved] -- BUILD-COMPLETE blocked]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## V-03 -- AMEND-CHAIN-COMPLETE exit token (C-33 candidate)

**Axis**: Named terminal block after AMEND --area full chain with PROFILE-DELTA
**Hypothesis**: C-29 requires AMEND --area to run PROFILE-REDERIVE -> IA-WRITTEN ->
BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE as a named gate. This gate fires at the
midpoint of the chain -- after re-profiling, before role file regeneration. The amendment
is not complete until BUILD-VERIFY confirms regenerated IA files carry the rederived
lens-phrase verbatim. There is no named terminal signal confirming the entire amendment
propagated end-to-end. Adding AMEND-CHAIN-COMPLETE after BUILD-VERIFY for the amended
area -- with PROFILE-DELTA showing what field values changed or confirming them unchanged,
files-regenerated count, ROLES-WRITTEN-summary, and BUILD-VERIFY-summary -- converts
AMEND from a gated repair sequence into a closed-loop amendment record. PROFILE-DELTA is
the critical innovation: it exposes whether re-derivation produced materially different
profile values (genuine amendment) or confirmed the originals unchanged (no-op), making
two qualitatively different amendment outcomes distinguishable in the output.
Expected candidate criterion (C-33): AMEND --area must emit AMEND-CHAIN-COMPLETE after
BUILD-VERIFY for the amended area, with PROFILE-DELTA, files-regenerated, ROLES-WRITTEN-
summary, and BUILD-VERIFY-summary required; missing fields make the amendment incomplete.
Does not include V-01's CROSS-REF ROLES-RECEIPT or V-02's CATALOG triggered-trace.

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

Phases 1-7 (PARSE through WRITE-ROLES): identical to V-01, including all ENTRY-GATE tokens,
full ROLES-WRITTEN per-team receipts, and STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE enforcement.

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE.`

Write `org-chart.md`. Transcribes sealed artifacts verbatim.

Step 8a: ASCII Hierarchy -- `+--` / `|`; verbatim names; two+ nesting levels.
Step 8b/8c: Transcription, TRANSCRIPTION-RECEIPT, PATH-A / PATH-B as in V-01.

Step 8d: AMEND:
```
AMEND:
1. --area "[area name]": PROFILE-REDERIVE chain:
   a. Emit full PROFILE block for each team in the named area (same structure as PHASE 5).
      Apply all three STRUCTURAL-ERROR:PROFILE-* enforcement checks.
      PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
      AMEND --area cannot proceed to role file regeneration without PROFILE-REDERIVE-COMPLETE.
   b. Regenerate all role files for the area. Re-run IA-WRITTEN (all four checks including
      non-transplantable). Re-run ROLES-WRITTEN for the regenerated area.
      Re-run BUILD-VERIFY for all re-profiled teams (VERBATIM required per team).
   c. After BUILD-VERIFY completes for all teams in the amended area, emit AMEND-CHAIN-COMPLETE:
      AMEND-CHAIN-COMPLETE: [area name]
        PROFILE-DELTA:
          defended-artifact: [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
          change-pressure:   [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
          lens-phrase:       [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
        files-regenerated: [n role files written for this area, including IA]
        ROLES-WRITTEN-summary: [n teams with passing ROLES-WRITTEN receipts] of [n teams in area]
        BUILD-VERIFY-summary: [n teams VERBATIM] of [n teams in area] -- [CLEAN | DRIFT-DETECTED]
        AMEND-CHAIN-COMPLETE: [PASS -- full chain propagated cleanly, all fields populated |
                               FAIL -- [list gaps, outstanding DRIFT verdicts, or missing fields]]
   An AMEND-CHAIN-COMPLETE block missing PROFILE-DELTA, files-regenerated, ROLES-WRITTEN-summary,
   or BUILD-VERIFY-summary is structurally incomplete. No further --area amend for this area
   until AMEND-CHAIN-COMPLETE: PASS is present. Update ARTIFACT-A after PASS.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required.
Single responsibility, EXCLUSION-MANIFEST, per-team BUILD-VERIFY, DERIVATION-LOOP-CLOSED
as defined in V-01.

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL]
```

After CROSS-REF PASS, emit CATALOG-CLOSURE with all 17 codes (binary disposition):

```
CATALOG-CLOSURE:
  [each of the 17 catalog codes]:
    [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] times]
  CATALOG-CLOSURE: [CLEAN -- all 17 codes accounted for |
                   OPEN: [list unresolved] -- BUILD-COMPLETE blocked]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## V-04 -- CROSS-REF ROLES-RECEIPT + CATALOG triggered-trace (V-01 + V-02)

**Axes**: CROSS-REF roles-receipts row + CATALOG-CLOSURE triggered-at/resolved-by trace
**Hypothesis**: V-01 and V-02 address orthogonal audit gaps in the build's terminal phases.
CROSS-REF ROLES-RECEIPT (V-01) moves write-time per-team enforcement into build-time audit:
the `roles-receipts` row in CROSS-REF makes receipt completeness a structural prerequisite
for CROSS-REF PASS. CATALOG triggered-trace (V-02) moves disposition attestation into
recoverable audit trace: TRIGGERED+RESOLVED without triggered-at and resolved-by is OPEN.
Together they reinforce Phase 10 with the same rigor IA-WRITTEN applies to IA files:
every verification must be traceable to a specific step and outcome. The combination risk
is length in Phase 10: five-row CROSS-REF plus 17-code CATALOG-CLOSURE with per-code trace
annotations produces a dense terminal block. The test is whether models emit both correctly
at full fidelity without compressing either into shorthand.
Does not include V-03's AMEND-CHAIN-COMPLETE token.

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

Phases 1-7 (PARSE through WRITE-ROLES): identical to V-01, with all ENTRY-GATE tokens,
full ROLES-WRITTEN per-team receipts (standard-fields-complete + specialized-distinctness),
and STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE enforcement.

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required.

Write `org-chart.md`. Transcribes sealed artifacts verbatim.

Step 8a: ASCII Hierarchy as in V-01.
Step 8b/8c: Transcription, TRANSCRIPTION-RECEIPT, PATH-A / PATH-B as in V-01.

Step 8d: AMEND:
```
AMEND:
1. --area "[area name]": PROFILE-REDERIVE chain:
   emit full PROFILE block for each team in area; apply all PROFILE-* checks;
   PROFILE-REDERIVE-COMPLETE: [area], [n] re-profiled. No violations.
   Regenerate role files; re-run IA-WRITTEN; re-run ROLES-WRITTEN; re-run BUILD-VERIFY;
   update ARTIFACT-A. PROFILE-REDERIVE must precede WRITE-IA for the amended area.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required.
Single responsibility, EXCLUSION-MANIFEST, per-team BUILD-VERIFY, DERIVATION-LOOP-CLOSED
as in V-01.

---

### PHASE 10 -- CROSS-REF

ENTRY-GATE: BUILD-VERIFY-COMPLETE required.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  roles-receipts: [n teams with passing ROLES-WRITTEN verdicts] of [n teams in org.yaml]
                  -- [MATCH | MISMATCH -- [team names] missing or failing ROLES-WRITTEN]
  CROSS-REF: [PASS -- all five rows MATCH | FAIL -- list any MISMATCH]
```

MISMATCH on `roles-receipts` blocks CROSS-REF PASS. Omitting `roles-receipts` row is
structurally incomplete.

After CROSS-REF PASS, emit CATALOG-CLOSURE with triggered-trace annotations.
TRIGGERED+RESOLVED entries without triggered-at and resolved-by are treated as OPEN.

```
CATALOG-CLOSURE:
  STRUCTURAL-ERROR:PHASE-2-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase, step or team]
      resolved-by: [action]]
  STRUCTURAL-ERROR:CONTRACT-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase, step or team]
      resolved-by: [action]]
  STRUCTURAL-ERROR:CONTRACT-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-CATEGORY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:IA-OUT-OF-ORDER: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-RECALC: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-COUNT-CHECK: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-DIR-AUDIT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-HEADCOUNT: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-AMEND: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-SUMMARY: [CONFIRMED-NOT-TRIGGERED | TRIGGERED+RESOLVED: [n] /
    triggered-at: [...] / resolved-by: [...]]
  CATALOG-CLOSURE: [CLEAN -- all 17 codes accounted for; all TRIGGERED+RESOLVED carry
                   triggered-at and resolved-by |
                   OPEN: [list missing annotations or unresolved] -- BUILD-COMPLETE blocked]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`

---

## V-05 -- Full integration (V-01 + V-02 + V-03)

**Axes**: CROSS-REF ROLES-RECEIPT + CATALOG triggered-trace + AMEND-CHAIN-COMPLETE
**Hypothesis**: V-01 (CROSS-REF roles-receipts row) and V-02 (CATALOG triggered-trace)
both strengthen Phase 10, from complementary directions: V-01 audits write-phase receipt
completeness at build time; V-02 makes every violation resolution traceable in the closure
block. V-03 (AMEND-CHAIN-COMPLETE) operates in Phase 8's AMEND procedure, adding a named
terminal token that confirms end-to-end amendment propagation and surfaces PROFILE-DELTA.
Together they close audit gaps at three structural levels: (1) CROSS-REF now verifies
receipt completeness in addition to file-count fidelity; (2) CATALOG-CLOSURE is a trace,
not only an outcome list; (3) AMEND is a closed-loop record with a named terminal gate.
The integration risk: Phase 8 AMEND and Phase 10 both grow substantially. The critical
test is whether a model can correctly emit AMEND-CHAIN-COMPLETE with all four required
fields in AMEND, then emit the five-row CROSS-REF and the 17-code CATALOG-CLOSURE with
triggered-at/resolved-by annotations in Phase 10 -- without compressing any of the three
terminal constructs into shorthand. A run satisfying all three at full fidelity establishes
that the combined length is feasible and that no axis degrades the others when co-present.

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

Read `org.yaml`. Emit parse manifest:

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

Extract one resistance profile per team before any IA file.

**Typed violation codes for this phase (see catalog):**
- STRUCTURAL-ERROR:PROFILE-CATEGORY
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS

For each team:

```
PROFILE: [team name]
  defended-artifact: [specific named thing -- NOT a category label]
  change-pressure: [specific proposed change; concrete]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact names a category -- rewrite.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses absent vocabulary -- rewrite.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two profiles share a lens-phrase -- rewrite one.

Named failure mode contrast:
- FAIL (STRUCTURAL-ERROR:PROFILE-CATEGORY): "the existing pipeline architecture"
- PASS: "the event-resequencing buffer that preserves order during backpressure"

`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write ALL Inertia Advocate files before ANY standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`:

Fields:
- **orientation**: names what this team is protecting and why it matters here
- **lens**: opens verbatim with PROFILE lens-phrase; extends with team domain vocabulary
- **expertise**: names actual systems, decisions, failures -- not generic labels
- **scope**: tied to defended-artifact from PROFILE; names escalation path
- **collaboration-pattern**: surfaces concerns early; does not veto; asks about rollback plans

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required before next team]
  expertise-concrete: [YES | NO -- rewrite required before next team]
  lens-phrase-verbatim: [YES | NO -- rewrite required before next team]
  lens-team-specific (non-transplantable): [YES -- vocabulary unique to this team's domain |
    NO -- transplantable; rewrite required before next team]
```

Non-transplantable enforcement gate: NO halts. Rewrite; re-emit IA-WRITTEN YES before next team.

Named failure mode contrast:
- FAIL: "Any change to the existing architecture risks disrupting the team's current workflow"
- PASS: "The claim routing table's 847 active rule entries were audited manually every quarter
  because no automated validation existed"

`IA-PHASE-COMPLETE: [n of n] teams. All four checks passed. All IA files before roles.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE. All IA files must be written first.`

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- `role-type: specialized`; lens and expertise must
   name domain-specific systems structurally distinct from standard roles on the same team.

After writing all standard and specialized files for each team, emit ROLES-WRITTEN:

```
ROLES-WRITTEN: [team name]
  standard-fields-complete: [YES -- all five fields non-empty for all [n] standard roles |
                              NO -- [role slug]: [field name] missing; rewrite required
                                   before proceeding to next team]
  specialized-count: [n files | "none declared"]
  specialized-distinctness: [YES -- each specialized lens structurally distinct from all
                              standard lenses on this team |
                              NOT-APPLICABLE -- no specialized roles declared |
                              NO -- [specialized slug] duplicates [standard slug];
                                   rewrite required before next team]
```

NO verdict halts. Rewrite; re-emit ROLES-WRITTEN with passing verdicts before next team.
ROLES-COMPLETE before all passing: STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE (catalog).

Named failure mode (specialized distinctness): "As a senior specialist, I bring expertise
across the full breadth of systems in this team's domain, with deeper focus on optimization
and performance" -- scalar extension; does not name specific systems.

Named pass: "The schema negotiation contract between the ingest layer and the three
downstream consumers was written and owned by this role; any migration touching the
contract surface requires this role's sign-off."

After all teams, write shared-group and exec-office roles if declared; require ROLES-WRITTEN.

`ROLES-COMPLETE: [n] files written to .craft/roles/. All ROLES-WRITTEN checks passed.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.
Recalculating: STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

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
TRANSCRIPTION-CLEAR in PATH-A: STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR.

PATH-B (any REVISED): rewrite -> re-emit TRANSCRIPTION-RECEIPT -> confirm:
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
1. --area "[area name]": PROFILE-REDERIVE chain:
   a. Emit full PROFILE block for each team in the named area (same structure as PHASE 5).
      Apply all three STRUCTURAL-ERROR:PROFILE-* enforcement checks.
      PROFILE-REDERIVE-COMPLETE: [area name], [n] teams re-profiled. No PROFILE-* violations.
      AMEND --area cannot proceed to role file regeneration without PROFILE-REDERIVE-COMPLETE.
   b. Regenerate all role files for the area. Re-run IA-WRITTEN (all four checks including
      non-transplantable). Re-run ROLES-WRITTEN for the regenerated area (all fields checked).
      Re-run BUILD-VERIFY for all re-profiled teams (VERBATIM required for each team).
   c. After BUILD-VERIFY completes for all teams in the amended area, emit AMEND-CHAIN-COMPLETE:
      AMEND-CHAIN-COMPLETE: [area name]
        PROFILE-DELTA:
          defended-artifact: [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
          change-pressure:   [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
          lens-phrase:       [UNCHANGED | CHANGED: "[old value]" -> "[new value]"]
        files-regenerated: [n role files written for this area, including IA]
        ROLES-WRITTEN-summary: [n teams with passing ROLES-WRITTEN receipts] of [n teams in area]
        BUILD-VERIFY-summary: [n teams VERBATIM] of [n teams in area] -- [CLEAN | DRIFT-DETECTED]
        AMEND-CHAIN-COMPLETE: [PASS -- full chain propagated cleanly, all fields populated |
                               FAIL -- [list gaps, outstanding DRIFT, or missing fields]]
   An AMEND-CHAIN-COMPLETE block missing PROFILE-DELTA, files-regenerated, ROLES-WRITTEN-summary,
   or BUILD-VERIFY-summary is structurally incomplete. No further --area amend for this area
   until AMEND-CHAIN-COMPLETE: PASS is present. Update ARTIFACT-A after PASS.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

ENTRY-GATE: CHART-WRITTEN required. If not present:
`ENTRY-GATE-FAIL: BUILD-VERIFY requires CHART-WRITTEN. Complete WRITE-CHART first.`

Single responsibility: confirm each IA file's lens field opens verbatim with the
lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- out-of-scope for this phase (all codes in catalog):

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons | STRUCTURAL-ERROR:BV-DIR-AUDIT |
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

DRIFT: rewrite IA file, re-emit BUILD-VERIFY VERBATIM before next team.

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
  dir check: [list all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  roles-receipts: [n teams with passing ROLES-WRITTEN verdicts] of [n teams in org.yaml]
                  -- [MATCH -- all teams emitted passing receipts |
                     MISMATCH -- [team names] missing or failing ROLES-WRITTEN]
  CROSS-REF: [PASS -- all five rows MATCH | FAIL -- list any MISMATCH]
```

MISMATCH on `roles-receipts` blocks CROSS-REF PASS. Omitting `roles-receipts` is
structurally incomplete.

After CROSS-REF PASS, emit CATALOG-CLOSURE with triggered-trace annotations.
TRIGGERED+RESOLVED entries without triggered-at and resolved-by are treated as OPEN
and block CATALOG-CLOSURE: CLEAN and BUILD-COMPLETE.

```
CATALOG-CLOSURE:
  STRUCTURAL-ERROR:PHASE-2-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase name, step or team name]
      resolved-by: [action that cleared this violation]]
  STRUCTURAL-ERROR:CONTRACT-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times
      triggered-at: [phase name, step or team name]
      resolved-by: [action that cleared this violation]]
  STRUCTURAL-ERROR:CONTRACT-RECALC: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-CATEGORY: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:IA-OUT-OF-ORDER: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-RECALC: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-FILE-WRITE: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-COUNT-CHECK: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-DIR-AUDIT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-HEADCOUNT: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-AMEND: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  STRUCTURAL-ERROR:BV-SUMMARY: [CONFIRMED-NOT-TRIGGERED |
    TRIGGERED+RESOLVED: [n] times / triggered-at: [...] / resolved-by: [...]]
  CATALOG-CLOSURE: [CLEAN -- all 17 codes accounted for; all TRIGGERED+RESOLVED entries
                   carry triggered-at and resolved-by annotations |
                   OPEN: [list codes missing annotations or unresolved violations]
                   -- BUILD-COMPLETE blocked]
```

BUILD-COMPLETE is only emitted after CATALOG-CLOSURE: CLEAN and CROSS-REF PASS (all five rows).

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS. CATALOG-CLOSURE CLEAN.`
