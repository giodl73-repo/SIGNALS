---
skill: quest-variate
skill_target: corps-build
round: 8
date: 2026-03-17
rubric_version: 6
r7_scorecard: corps-build-scorecard-R7-2026-03-17.md
---

# Variate R8 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 8. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R7 scorecard: rubric v6 formalizes three criteria surfaced by R7 excellence signals --
C-22 (IA failure mode contrast pair), C-23 (typed STRUCTURAL-ERROR code taxonomy),
C-24 (premature-exit violation named as STRUCTURAL-ERROR). These are now baseline criteria.
All three were satisfied by R7 V-03 and V-05.

R8 baseline architecture (foundation for all five variations):
PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA -> WRITE-ROLES ->
WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
V-05 R7 is the baseline: all three R7 axes integrated (DERIVATION-LOOP-CLOSED +
non-transplantable per-file gate + typed BUILD-VERIFY EXCLUSION-MANIFEST with STRUCTURAL-ERROR
codes + WRITE-CHART-PREMATURE-EXIT as named STRUCTURAL-ERROR).

R8 explores three new axes that rubric v6 does not yet capture:

- Phase-entry guard tokens: rubric v6 enforces phase exits (PARSE-PASS, CONTRACT-SEAL-PASS,
  CHART-WRITTEN) but phase entries are implicit. A skill runner could output phase content
  without a preceding exit token being present. Explicit ENTRY-GATE checks at each phase
  start create a bidirectional boundary system where both entry and exit are observable and
  named.

- Upfront STRUCTURAL-ERROR-CATALOG: rubric v6 captures that error codes exist (C-23) and
  that the premature-exit violation is named (C-24). But the codes in R7 V-03/V-05 are
  defined inline per-phase -- a reader must scan the full prompt to enumerate them. An
  upfront catalog table before Phase 1 makes the taxonomy navigable from the start, lets a
  reviewer confirm catalog completeness without reading phase bodies, and makes it detectable
  when a new phase introduces codes absent from the catalog.

- PROFILE typed structural errors: C-23 and C-24 enforce typed codes for BUILD-VERIFY and
  WRITE-CHART violations. PROFILE -- the upstream source of IA quality -- still uses prose
  failure modes ("defended-artifact names a category -> rewrite before proceeding"). If
  PROFILE violations carry named STRUCTURAL-ERROR codes (PROFILE-CATEGORY,
  PROFILE-LENS-UNDERIVED, PROFILE-DUPLICATE-LENS), the constraint precision at the
  derivation source matches the constraint precision at the derivation consumers.

---

## Variation Axes

| Axis | Used In |
|------|---------|
| Phase-entry guard tokens: explicit ENTRY-GATE check at each phase start, naming required prior exit token | V-01, V-04, V-05 |
| Upfront STRUCTURAL-ERROR-CATALOG: all codes in a table before Phase 1; inline references point back to catalog | V-02, V-04, V-05 |
| PROFILE typed errors: STRUCTURAL-ERROR:PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED, PROFILE-DUPLICATE-LENS | V-03, V-05 |

---

## V-01 -- Phase-entry guard tokens (C-25 candidate)

**Axis**: Bidirectional phase boundary enforcement
**Hypothesis**: R7 variations enforce phase exits (named exit tokens: PARSE-PASS,
CONTRACT-SEAL-PASS, CHART-WRITTEN, etc.) but phase entries are implicit -- any phase could
begin without confirming the previous phase's exit token appeared. A skill runner working
through a long org could output VALIDATE content while PARSE-PASS has not been emitted, or
begin WRITE-CHART without ROLES-COMPLETE present, and the current prompt structure would not
catch this by name. Adding explicit ENTRY-GATE checks at each phase start -- naming the
required prior exit token and specifying what to halt with if missing -- creates a
bidirectional enforcement system. EXIT tokens confirm a phase completed correctly; ENTRY-GATE
checks confirm the transition was authorized. Together they should surface as a candidate
criterion (C-25) for phase-transition integrity: the boundary between any two adjacent phases
is observable at both ends rather than only at the exit point.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

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

ENTRY-GATE: PARSE-PASS required. If PARSE-PASS not present in prior output, halt:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS. Re-run PARSE before proceeding.`

STRUCTURAL-ERROR:PHASE-2-FILE-WRITE -- any file written during VALIDATE is a structural error.
This phase reads org.yaml state only.

Four structural checks:
1. Team name uniqueness within each group
2. Role slug uniqueness within each team
3. Area slug uniqueness across the org (no two teams produce the same `.craft/roles/{slug}/` path)
4. Nesting depth <= 3 (Division > Group > Team); deeper nesting halts

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

STRUCTURAL-ERROR:CONTRACT-FILE-WRITE -- any file written during CONTRACT is a structural error.
STRUCTURAL-ERROR:CONTRACT-RECALC -- any recalculation of these artifacts outside this phase
is a structural error. The sealed values are copied verbatim in WRITE-CHART.

Produce three sealed artifacts:

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**

Exactly 2-3 sentences. Sentence 1: name the org and total headcount with the largest area
by count and its percentage. Sentence 2: name the level distribution or state levels are
not declared. Sentence 3: a structural observation that the table rows alone do not convey.
A correct ARTIFACT-B names at least two specific area names. An ARTIFACT-B with no area
names is structurally invalid even if sentence count and format are correct.

**ARTIFACT-C -- Level Distribution**

If levels declared: breakdown by level label with counts.
If not declared: `Level distribution: not declared in org.yaml.`

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

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision the IA is invested in --
                      NOT a category; must name the actual thing]
  change-pressure: [the specific proposed change that threatens the defended-artifact;
                    must be concrete; NOT "change in general"]
  lens-phrase: [the exact phrase, drawn from defended-artifact + change-pressure vocabulary,
               that will open the IA file's lens field verbatim]
```

Failure modes:
- Defended-artifact names a category (e.g., "the existing pipeline architecture") rather
  than a specific thing (e.g., "the schema contract table that maps 34 external callers") --
  rewrite before proceeding to the next team.
- Lens-phrase uses vocabulary not present in defended-artifact or change-pressure -- rewrite.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. All defended-artifacts name specific things.
All lens-phrases derived from team vocabulary.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE. Complete PROFILE for all teams first.`

Write all Inertia Advocate files before any standard or specialized role files.

STRUCTURAL-ERROR:IA-OUT-OF-ORDER -- writing a standard or specialized role file before
all IA files for that team are complete is a structural error.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`:

```markdown
---
role-type: inertia-advocate
area: {area-slug}
---

## orientation
[Why a senior member of this specific team would rationally resist: grounded in the
team's declared responsibilities, not generic change resistance]

## lens
[Opens with the EXACT lens-phrase from PROFILE for this team -- verbatim, no paraphrase.
Continues with 1-2 sentences grounding the lens in this team's domain.]

## expertise
[Concrete systems, decisions, or failures survived in this team's specific domain.
Must name the actual systems. Generic expertise statements fail.]

## scope
[What this role can flag, block, or escalate -- tied to the defended-artifact from PROFILE]

## collaboration-pattern
[How this IA works with other roles on this team; surfaces concerns early, does not veto,
asks about rollback paths]
```

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

Named failure mode (transplantable): "Any change to the existing architecture risks
disrupting the team's current workflow" -- this phrase applies verbatim to any team's IA.

Named pass (team-specific): "The claim routing table's 847 active rule entries were
audited manually every quarter because no automated validation existed" -- this cannot be
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
1. **Standard roles** -- `.craft/roles/{area-slug}/{role-slug}.md`
   Frontmatter: `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- same path pattern
   Frontmatter: `role-type: specialized`; lens and expertise must name domain-specific systems
   that distinguish this role from the standard roles on the same team; a specialized lens
   identical to any standard lens on the same team fails distinctness and requires rewrite.

After all teams: write shared-group roles to `.craft/roles/shared/` (role-type: shared-group)
and exec-office roles to `.craft/roles/exec-office/` (role-type: exec-office) if declared.

Every role file must contain all five fields with substantive, non-empty, non-"TBD" body:
orientation, lens, expertise, scope, collaboration-pattern.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE. All role files must be written first.`

Write `org-chart.md`. This phase transcribes the sealed CONTRACT artifacts verbatim.

STRUCTURAL-ERROR:WRITE-CHART-RECALC -- recalculating ARTIFACT-A/B/C values in this phase
rather than transcribing from CONTRACT-SEAL is a structural error.

**Step 8a -- ASCII Hierarchy**

Use `+--` and `|` characters. All names verbatim from `org.yaml`. Every area from the
PARSE manifest must appear. Minimum two nesting levels visible.

**Step 8b -- Transcription**

Transcribe CONTRACT artifacts verbatim into org-chart.md sections 2, 3, and 4:

```
[TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate, do not reformat]
[TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- do not rewrite, do not paraphrase]
[TRANSCRIBE CONTRACT ARTIFACT-C verbatim -- do not rewrite]
```

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
STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR -- TRANSCRIPTION-CLEAR emitted before PATH-A
confirmation is a structural error.

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
STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT -- CHART-WRITTEN emitted before
TRANSCRIPTION-CLEAR in PATH-B is a structural error.
A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate all role files for that area; re-run IA-WRITTEN
   (all four checks, including non-transplantable) for regenerated IA; update ARTIFACT-A.
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

EXCLUSION-MANIFEST -- the following output types are STRUCTURAL-ERROR:BUILD-VERIFY-OOB
and their presence in this phase is a build error:

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks (total vs org.yaml slots) | STRUCTURAL-ERROR:BV-COUNT-CHECK |
| Directory comparisons or subdirectory audits | STRUCTURAL-ERROR:BV-DIR-AUDIT |
| Headcount or ARTIFACT-A verifications | STRUCTURAL-ERROR:BV-HEADCOUNT |
| AMEND section generation | STRUCTURAL-ERROR:BV-AMEND |
| Summary rows or aggregate statistics | STRUCTURAL-ERROR:BV-SUMMARY |

For each team, emit:

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
  dir check: [list all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-02 -- Upfront STRUCTURAL-ERROR-CATALOG (C-25 candidate)

**Axis**: Pre-execution structural error catalog
**Hypothesis**: R7 V-03 and V-05 define STRUCTURAL-ERROR codes inline per-phase. A reader
verifying constraint coverage must scan the full prompt to enumerate all defined codes, and
there is no mechanism to detect whether a new phase introduced codes that are absent from
prior definitions. If an upfront STRUCTURAL-ERROR-CATALOG table appears before Phase 1 --
listing every code, the phase where it applies, and the trigger condition -- the taxonomy
becomes navigable from the first line of the prompt. A reviewer can confirm catalog
completeness by checking the table alone; they do not need to read phase bodies to audit
which error codes exist. Inline phase references ("See STRUCTURAL-ERROR:BV-FILE-WRITE in
the catalog") tie each occurrence back to the catalog, making each code a named entry in
a shared vocabulary rather than a local declaration. Expected to surface as a candidate
criterion (C-25): structural error taxonomy must appear as a catalog entry before the
first phase that uses a code, with inline phase bodies referencing rather than
re-defining codes.
Does not include V-01's phase-entry guard tokens.

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
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard or specialized role written before all IA files for that team complete |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT values recalculated in WRITE-CHART rather than copied from seal |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A (all-VERBATIM path) |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison performed in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section generated in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows or aggregate statistics in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

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

No files written in this phase. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

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

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
No recalculation outside this phase. Violation: STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

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

Extract one resistance profile per team before writing any IA file.

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision the IA is invested in --
                      NOT a category; must name the actual thing]
  change-pressure: [the specific proposed change that threatens the defended-artifact;
                    must be concrete; NOT "change in general"]
  lens-phrase: [the exact phrase, drawn from defended-artifact + change-pressure vocabulary,
               that will open the IA file's lens field verbatim]
```

Failure modes:
- Defended-artifact names a category (e.g., "the existing pipeline architecture") rather
  than a specific thing (e.g., "the event-resequencing buffer that handles out-of-order
  arrivals") -- rewrite before proceeding to the next team.
- Lens-phrase uses vocabulary not present in defended-artifact or change-pressure -- rewrite.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. All defended-artifacts name specific things.
All lens-phrases derived from team vocabulary.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

Write all Inertia Advocate files before any standard or specialized role files.
Violation for out-of-order writes: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`:

Fields: orientation (grounds IA in this team's specific operational context), lens (opens
verbatim with PROFILE lens-phrase; extends with team-domain vocabulary), expertise (names
actual systems, decisions, or failures in this domain -- no generic labels), scope (tied to
the defended-artifact from PROFILE), collaboration-pattern (surfaces concerns early; does
not veto; asks about rollback paths).

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

Non-transplantable enforcement gate: a NO on `lens-team-specific` halts the build. Rewrite
using this team's specific system names or failure modes. Re-emit IA-WRITTEN with YES on
all four checks before beginning the next team's IA file.

Named failure mode (transplantable): "Any change to the existing architecture risks
disrupting the team's current workflow."

Named pass (team-specific): "The claim routing table's 847 active rule entries were
audited manually every quarter because no automated validation existed."

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team. All IA files written before standard and specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

For each team in declaration order: standard then specialized. After all teams:
shared-group and exec-office if declared. All files: five non-empty fields (orientation,
lens, expertise, scope, collaboration-pattern). Specialized lens must differ structurally
from standard lens on same team.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**ASCII Hierarchy**: `+--` / `|`; all names verbatim from `org.yaml`; minimum two nesting
levels; every area from PARSE manifest present.

**Transcription**: Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from CONTRACT-SEAL.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
Emitting TRANSCRIPTION-CLEAR in PATH-A triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR
(catalog).

PATH-B (any REVISED): rewrite deviant artifact -> re-emit TRANSCRIPTION-RECEIPT -> confirm
all VERBATIM -> emit:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```

Emitting CHART-WRITTEN before TRANSCRIPTION-CLEAR in PATH-B triggers
STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT (catalog).

```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

This phase has exactly one responsibility: confirm each IA lens opens verbatim with PROFILE
lens-phrase.

EXCLUSION-MANIFEST -- the following are out-of-scope for this phase (all codes in catalog):

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
  PROFILE lens-phrase: "[exact phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
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
  All [n] chains confirmed closed. Resistance profiles fully recoverable from built files.
```

---

### PHASE 10 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-03 -- PROFILE typed structural errors (C-25 candidate)

**Axis**: Typed STRUCTURAL-ERROR codes at the derivation source (PROFILE phase)
**Hypothesis**: C-23 captures typed structural error codes for BUILD-VERIFY violations
(BV-FILE-WRITE, BV-COUNT-CHECK, etc.) and C-24 captures STRUCTURAL-ERROR:WRITE-CHART-
PREMATURE-EXIT. These codes enforce constraints at verification and transcription points --
the downstream end of the derivation chain. PROFILE is the upstream source: it produces
the lens-phrase that IA-WRITTEN checks at write time and BUILD-VERIFY confirms at
verification time. Yet PROFILE violations ("defended-artifact names a category") currently
use only prose failure modes, with no STRUCTURAL-ERROR code. If PROFILE violations carry
typed codes -- STRUCTURAL-ERROR:PROFILE-CATEGORY for category-naming, STRUCTURAL-ERROR:
PROFILE-LENS-UNDERIVED for vocabulary not drawn from defended-artifact or change-pressure,
STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS for two profiles sharing an identical lens-phrase --
the constraint precision at the derivation source matches the precision at the derivation
consumers. The entire chain from PROFILE -> IA-WRITTEN -> BUILD-VERIFY is then uniformly
enforced by named codes rather than mixing typed enforcement downstream with prose enforcement
upstream. Expected to surface as a candidate criterion (C-25): upstream derivation phases
must use typed STRUCTURAL-ERROR codes matching the precision of downstream verification.
Does not include V-01's phase-entry guard tokens or V-02's upfront catalog.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

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

STRUCTURAL-ERROR:PHASE-2-FILE-WRITE -- any file written during VALIDATE is a structural error.

Four checks: (1) team name uniqueness within group; (2) role slug uniqueness within team;
(3) area slug uniqueness across org; (4) nesting depth <= 3.

```
VALIDATE:
  [1] team name uniqueness: [PASS | FAIL]
  [2] role slug uniqueness: [PASS | FAIL]
  [3] area slug uniqueness: [PASS | FAIL]
  [4] nesting depth <= 3: [PASS | FAIL]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

STRUCTURAL-ERROR:CONTRACT-FILE-WRITE -- any file written during CONTRACT is a structural error.
STRUCTURAL-ERROR:CONTRACT-RECALC -- recalculating these artifacts outside this phase is
a structural error.

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3 is a structural observation not visible from table rows alone.

**ARTIFACT-C -- Level Distribution**: by label if declared; else `not declared in org.yaml.`

`TABLE-CLOSED: [n] files required. No files written during this phase.`

---

### PHASE 4 -- CONTRACT-SEAL

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] area rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words...]
  ARTIFACT-C: SEALED
  CONTRACT-SEAL-PASS
```

---

### PHASE 5 -- PROFILE

Extract one resistance profile per team. No files written in this phase.

**Typed violation codes for this phase:**

| Code | Trigger |
|------|---------|
| STRUCTURAL-ERROR:PROFILE-CATEGORY | defended-artifact names a type or category rather than a specific named system, process, or decision |
| STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED | lens-phrase uses vocabulary not present in defended-artifact or change-pressure fields |
| STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS | two or more teams have identical lens-phrases |

For each team:

```
PROFILE: [team name]
  defended-artifact: [the specific system, process, or decision the IA is invested in --
                      NOT a category; must name the actual thing]
  change-pressure: [the specific proposed change threatening the defended-artifact;
                    concrete; NOT "change in general"]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Enforcement:
- STRUCTURAL-ERROR:PROFILE-CATEGORY if defended-artifact is a category label
  (e.g., "the existing pipeline architecture") rather than a specific thing
  (e.g., "the event-resequencing buffer that preserves order during backpressure") --
  rewrite before proceeding to the next team.
- STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED if lens-phrase uses vocabulary absent from
  defended-artifact and change-pressure -- rewrite lens-phrase before next team.
- STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS if two profiles share an identical lens-phrase --
  at least one must be rewritten to use vocabulary specific to that team's domain.

Named failure mode contrast for defended-artifact quality:
- FAIL (category): "the existing pipeline architecture" -- transplantable, names a type
- PASS (specific): "the event-resequencing buffer that preserves order during backpressure" --
  names the actual thing; transplanting this to a different team requires rewriting

After all team profiles:
`PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding.
All defended-artifacts name specific things. All lens-phrases derived from team vocabulary.
All lens-phrases unique across teams.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

Write all Inertia Advocate files before any standard or specialized role files.

STRUCTURAL-ERROR:IA-OUT-OF-ORDER -- writing a standard or specialized role file before
all IA files for that team are complete is a structural error.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md`:

Fields: orientation (team-specific; grounds IA in this team's declared responsibilities),
lens (opens verbatim with PROFILE lens-phrase; extends with team-domain vocabulary),
expertise (names actual systems, decisions, or failures -- no generic labels), scope
(tied to defended-artifact from PROFILE), collaboration-pattern (early surfacing, no veto,
asks about rollback paths).

After writing each IA file, emit IA-WRITTEN with four checks:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
  lens-team-specific (non-transplantable): [YES -- vocabulary unique to this team's domain |
    NO -- transplantable phrases present; rewrite required before next team]
```

Named failure mode contrast for non-transplantable check:
- FAIL: "Any change to the existing architecture risks disrupting the team's current
  workflow" -- applies verbatim to any team's IA; no domain vocabulary present.
- PASS: "The claim routing table's 847 active rule entries were audited manually every
  quarter because no automated validation existed" -- names the specific artifact and
  circumstance; cannot be reused verbatim for a different team.

Non-transplantable enforcement gate: NO on `lens-team-specific` halts the build. Rewrite.
Re-emit IA-WRITTEN with YES on all four checks before next team's IA file.

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed for every
team. All IA files written before standard and specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

For each team: standard then specialized. After all teams: shared-group and exec-office
if declared. All five fields non-empty. Specialized lens must differ structurally from
standard on same team.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.

STRUCTURAL-ERROR:WRITE-CHART-RECALC -- recalculating ARTIFACT-A/B/C in this phase is
a structural error.

**ASCII Hierarchy**: `+--` / `|`; all names verbatim; minimum two nesting levels; every
area from PARSE manifest present.

**Transcription**: Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR -- TRANSCRIPTION-CLEAR emitted in PATH-A
is a structural error.

PATH-B (any REVISED): rewrite deviant artifact -> re-emit TRANSCRIPTION-RECEIPT -> confirm
all VERBATIM:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```

STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT -- CHART-WRITTEN before TRANSCRIPTION-CLEAR
in PATH-B is a structural error.

```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

Single responsibility: confirm each IA lens opens verbatim with PROFILE lens-phrase.

EXCLUSION-MANIFEST -- presence of these output types in this phase is a build error:

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
  PROFILE lens-phrase: "[exact phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
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
  All [n] chains confirmed closed. Resistance profiles fully recoverable from built files.
```

---

### PHASE 10 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-04 -- Phase-entry guards + Upfront STRUCTURAL-ERROR-CATALOG (V-01 + V-02)

**Axes**: Bidirectional phase boundary enforcement + pre-execution structural error catalog
**Hypothesis**: V-01 makes phase entry observable by requiring the prior exit token before
each phase begins; V-02 makes all error codes navigable from the start by defining them in
a catalog before Phase 1. These two axes address the same structural legibility objective
from different angles. Entry guards tell you whether a transition was authorized; the
catalog tells you what every violation means before you encounter it. Together they create
a fully navigable phase-enforcement system: any point in the output is auditable against
(a) whether the correct entry token was present, and (b) whether any produced output
matches a catalog violation code. The risk is that the catalog + entry gates add significant
preamble, potentially displacing content that satisfies coverage criteria (C-01 through
C-10). The test is whether the structural framing overhead stays contained while the
criteria density improves.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

## STRUCTURAL-ERROR-CATALOG

All structural error codes for this skill. Phase bodies reference these codes by name.

| Code | Phase | Trigger |
|------|-------|---------|
| STRUCTURAL-ERROR:PHASE-2-FILE-WRITE | VALIDATE | Any file written during VALIDATE |
| STRUCTURAL-ERROR:CONTRACT-FILE-WRITE | CONTRACT | Any file written during CONTRACT |
| STRUCTURAL-ERROR:CONTRACT-RECALC | WRITE-CHART | ARTIFACT recalculated rather than transcribed |
| STRUCTURAL-ERROR:IA-OUT-OF-ORDER | WRITE-IA | Standard/specialized role written before all IA files for that team |
| STRUCTURAL-ERROR:WRITE-CHART-RECALC | WRITE-CHART | ARTIFACT-A/B/C values recalculated in WRITE-CHART |
| STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT | WRITE-CHART | CHART-WRITTEN before TRANSCRIPTION-CLEAR in PATH-B |
| STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR | WRITE-CHART | TRANSCRIPTION-CLEAR emitted during PATH-A |
| STRUCTURAL-ERROR:BV-FILE-WRITE | BUILD-VERIFY | Any file written during BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-COUNT-CHECK | BUILD-VERIFY | File-count check in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-DIR-AUDIT | BUILD-VERIFY | Directory comparison in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-HEADCOUNT | BUILD-VERIFY | Headcount or ARTIFACT-A verification in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-AMEND | BUILD-VERIFY | AMEND section in BUILD-VERIFY |
| STRUCTURAL-ERROR:BV-SUMMARY | BUILD-VERIFY | Summary rows in BUILD-VERIFY |

---

### PHASE 1 -- PARSE

No entry gate. This is the first phase.

Read `org.yaml`. Emit:

```
PARSE:
  org name: [name]
  nesting: [e.g., Division > Group > Team]
  groups: [list]
  teams:
    [team name] (group: [parent]):
      standard: [names or "none"]
      specialized: [names or "none"]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] total role slots.`
Halt with `PARSE-FAIL: [reason]` if org.yaml is missing or unreadable.

---

### PHASE 2 -- VALIDATE

ENTRY-GATE: PARSE-PASS required. If not present:
`ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:PHASE-2-FILE-WRITE (catalog).

Four checks: (1) team name uniqueness within group; (2) role slug uniqueness within team;
(3) area slug uniqueness across org; (4) nesting depth <= 3.

```
VALIDATE:
  [1] team name uniqueness: [PASS | FAIL]
  [2] role slug uniqueness: [PASS | FAIL]
  [3] area slug uniqueness: [PASS | FAIL]
  [4] nesting depth <= 3: [PASS | FAIL]
  VALIDATE-PASS
```

Halt with `VALIDATE-FAIL: [violations]` if any check fails.

---

### PHASE 3 -- CONTRACT

ENTRY-GATE: VALIDATE-PASS required. If not present:
`ENTRY-GATE-FAIL: CONTRACT requires VALIDATE-PASS.`

No files written. Violation: STRUCTURAL-ERROR:CONTRACT-FILE-WRITE (catalog).
No recalculation outside this phase. Violation: STRUCTURAL-ERROR:CONTRACT-RECALC (catalog).

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B**: 2-3 sentences. Names at least two specific areas. Sentence 3: structural
observation not visible from rows alone.

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
  ARTIFACT-C: SEALED
  CONTRACT-SEAL-PASS
```

---

### PHASE 5 -- PROFILE

ENTRY-GATE: CONTRACT-SEAL-PASS required. If not present:
`ENTRY-GATE-FAIL: PROFILE requires CONTRACT-SEAL-PASS.`

For each team:

```
PROFILE: [team name]
  defended-artifact: [specific named thing -- NOT a category label]
  change-pressure: [specific proposed change]
  lens-phrase: [exact phrase to open IA lens verbatim]
```

Failure modes:
- Defended-artifact names a category -> rewrite before next team.
- Lens-phrase uses vocabulary absent from defended-artifact or change-pressure -> rewrite.

`PROFILE-GATE: [n] profiles complete. All defended-artifacts specific. All lens-phrases
derived from team vocabulary.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

ENTRY-GATE: PROFILE-GATE required. If not present:
`ENTRY-GATE-FAIL: WRITE-IA requires PROFILE-GATE.`

Write all IA files before any standard or specialized role files.
Violation: STRUCTURAL-ERROR:IA-OUT-OF-ORDER (catalog).

Per team: `.craft/roles/{area-slug}/inertia-advocate.md`. Fields: orientation, lens
(opens verbatim with PROFILE lens-phrase), expertise (names actual systems), scope,
collaboration-pattern.

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
  lens-team-specific (non-transplantable): [YES | NO -- rewrite required]
```

Non-transplantable enforcement: NO on `lens-team-specific` halts build. Rewrite.
Re-emit IA-WRITTEN with YES before next team.

Named failure mode contrast:
- FAIL: "Any change to the existing architecture risks disrupting the team's current workflow"
- PASS: "The claim routing table's 847 active rule entries were audited manually every
  quarter because no automated validation existed"

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed.`

---

### PHASE 7 -- WRITE-ROLES

ENTRY-GATE: IA-PHASE-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-ROLES requires IA-PHASE-COMPLETE.`

Standard then specialized per team. Shared-group and exec-office after all teams if declared.
All five fields non-empty. Specialized lens must differ structurally from standard on same team.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

ENTRY-GATE: ROLES-COMPLETE required. If not present:
`ENTRY-GATE-FAIL: WRITE-CHART requires ROLES-COMPLETE.`

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.
Recalculating triggers STRUCTURAL-ERROR:WRITE-CHART-RECALC (catalog).

**ASCII Hierarchy**: `+--` / `|`; all names verbatim; minimum two nesting levels; every
area from PARSE manifest present.

**Transcription**: Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from CONTRACT-SEAL.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

PATH-A (all VERBATIM): `PATH-A: all three artifacts VERBATIM. CHART-WRITTEN.`
Emitting TRANSCRIPTION-CLEAR here triggers STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR (catalog).

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

CHART-WRITTEN before TRANSCRIPTION-CLEAR triggers STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT
(catalog).

```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN (all four checks); update
   ARTIFACT-A.
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
  dir check: [slugs vs parse manifest -- MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-05 -- Full integration (V-01 + V-02 + V-03 + complete architecture)

**Axes**: Phase-entry guard tokens + upfront STRUCTURAL-ERROR-CATALOG + PROFILE typed
structural errors
**Hypothesis**: All three R8 axes address the same underlying goal -- making constraint
enforcement uniformly structured throughout the skill lifecycle rather than mixing prose
and typed enforcement at different phases. V-01 makes phase boundaries bidirectional
(entry + exit both named). V-02 makes all error codes enumerable before Phase 1 begins.
V-03 makes the upstream derivation source (PROFILE) as precisely constrained as the
downstream verification (IA-WRITTEN, BUILD-VERIFY). Together they close three remaining
structural asymmetries in the R7 V-05 baseline: (1) exits are named but entries are not,
(2) error codes exist but are not cataloged before use, (3) PROFILE violations use prose
while IA and BUILD-VERIFY violations use typed codes. The expected excellence signal is
that all three asymmetries closing simultaneously produces a skill where any phase in
the output is auditable against a known catalog, any transition is authorized by a named
entry token, and the full derivation chain from PROFILE through BUILD-VERIFY carries typed
structural codes at every checkpoint. This may surface candidate criteria around: full
catalog navigability before execution (C-25), upstream derivation phase enforcement parity
with downstream verification phases (C-26).

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

After all teams: shared-group roles to `.craft/roles/shared/` (role-type: shared-group)
and exec-office roles to `.craft/roles/exec-office/` (role-type: exec-office) if declared.

Every role file: five non-empty fields (orientation, lens, expertise, scope,
collaboration-pattern) with substantive, non-"TBD" body text.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

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
   (all four checks, including non-transplantable) for regenerated IA; update ARTIFACT-A.
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
  dir check: [list all .craft/roles/ subdirs vs parse manifest area slugs --
              MATCH | extra: [...] | missing: [...]]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL -- list any MISMATCH]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`
