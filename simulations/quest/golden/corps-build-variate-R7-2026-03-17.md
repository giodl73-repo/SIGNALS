---
skill: quest-variate
skill_target: corps-build
round: 7
date: 2026-03-17
rubric_version: 5
r6_scorecard: corps-build-scorecard-R6-2026-03-17.md
---

# Variate R7 -- corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 7. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R6 scorecard: all five variations achieved 100/100 (rubric v4 formula). Rubric v5 updates
scoring (max 155, golden >= 128) and formalizes C-19/C-20/C-21 as aspirational criteria.
R6 also extracted two candidate criteria not yet in the rubric:

- C-22 candidate: DERIVATION-LOOP-CLOSED attestation -- BUILD-VERIFY-PASS names the
  resistance-profile -> IA-lens derivation chain as a closed structural event, making
  derivation recoverable after the fact from output alone
- C-23 candidate: Non-transplantable IA per-file gate -- IA-WRITTEN adds
  "lens-team-specific (non-transplantable): YES / NO" as a write-time check; NO halts
  the build and requires rewrite before the next team begins

R7 baseline architecture (used as foundation for all five variations):
PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA -> WRITE-ROLES ->
WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
WRITE-ROLES precedes WRITE-CHART (org-chart.md is the final document written after all
role files exist). This is the V-05 R6 sequence.

---

## Variation Axes

| Axis | Used In |
|------|---------|
| DERIVATION-LOOP-CLOSED: BUILD-VERIFY-COMPLETE names PROFILE->IA chain as closed structural event | V-01, V-04, V-05 |
| Non-transplantable per-file gate: IA-WRITTEN adds YES/NO check; NO halts + requires rewrite | V-02, V-04, V-05 |
| BUILD-VERIFY exclusion manifest as typed structural error taxonomy (error codes) | V-03, V-05 |

---

## V-01 -- DERIVATION-LOOP-CLOSED: derivation chain as named structural event (C-22 candidate)

**Axis**: DERIVATION-LOOP-CLOSED
**Hypothesis**: In R6, BUILD-VERIFY confirms that each IA lens opens verbatim with the
PROFILE lens-phrase. This verification is present but the connection to the PROFILE
derivation chain is implicit -- BUILD-VERIFY and PROFILE are separate phases with no
named token bridging them. If BUILD-VERIFY-COMPLETE emits an explicit per-team derivation
trace (PROFILE lens-phrase -> IA file lens opening -> VERBATIM/DRIFT) followed by a named
DERIVATION-LOOP-CLOSED attestation, the derivation chain becomes a recoverable structural
record rather than a rule that happens to be satisfied. It is then possible to verify,
after the fact, that every IA lens was DERIVED from the resistance profile rather than
invented. Addresses C-17 (BUILD-VERIFY per-team verdicts), C-20 (exclusion manifest),
and surfaces as the primary signal for C-22. Does not add V-02's write-time gate -- the
only new mechanism is the BUILD-VERIFY-COMPLETE derivation trace and DERIVATION-LOOP-CLOSED
attestation.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

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

No files written in this phase.

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

No files written in this phase.

Produce three sealed artifacts. These artifacts are fixed at CONTRACT-SEAL and transcribed
verbatim in WRITE-CHART. They are not recalculated or reformatted later.

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

A defended-artifact naming a category (e.g., "the existing architecture") rather than a
specific thing (e.g., "the schema contract table that maps 34 external callers") fails
PROFILE quality and must be rewritten before proceeding to the next team.

After all team profiles:
`PROFILE-GATE: [n] profiles complete. All defended-artifacts name specific things.
All lens-phrases derived from team vocabulary.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

Write all Inertia Advocate files before any standard or specialized role files.

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

After writing each IA file, emit IA-WRITTEN:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES -- names this team's specific concern | NO -- rewrite required]
  expertise-concrete: [YES -- names actual systems or decisions | NO -- rewrite required]
  lens-phrase-verbatim: [YES -- lens opens with exact PROFILE phrase | NO -- rewrite required]
```

A NO on any check requires a rewrite of the IA file before writing the next team's IA file.

After all IA files:
`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard and
specialized roles. All IA-WRITTEN checks passed.`

---

### PHASE 7 -- WRITE-ROLES

Write standard and specialized role files for all teams.

For each team in declaration order:
1. **Standard roles** -- `.craft/roles/{area-slug}/{role-slug}.md`
   Frontmatter: `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- same path pattern
   Frontmatter: `role-type: specialized`, `area: {area-slug}`
   F-2 (lens) and F-3 (expertise) must name domain-specific systems that distinguish this
   role from the standard roles on the same team.

After all teams: write shared-group roles to `.craft/roles/shared/` (role-type: shared-group)
and exec-office roles to `.craft/roles/exec-office/` (role-type: exec-office) if declared.

Every role file must contain all five fields with substantive, non-empty, non-"TBD" body:
- **orientation**: team-specific perspective
- **lens**: named domain, system, or practice -- not generic
- **expertise**: concrete systems or decisions owned -- not generic labels
- **scope**: what this role approves, blocks, or escalates
- **collaboration-pattern**: how this role interacts with others on the team

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. This phase transcribes the sealed CONTRACT artifacts verbatim.
It does not recalculate, reformat, or derive new values.

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

After transcription, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

If TRANSCRIPTION-RECEIPT shows all VERBATIM:
`PATH-A: all three artifacts VERBATIM -- CHART-WRITTEN.`

If TRANSCRIPTION-RECEIPT shows any REVISED:
- Rewrite the deviant artifact to match the sealed CONTRACT version
- Re-emit TRANSCRIPTION-RECEIPT with the corrected verdict
- A REVISED verdict may not remain outstanding when this phase closes
- Emit TRANSCRIPTION-CLEAR:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
```

`PATH-B: TRANSCRIPTION-CLEAR passed -- CHART-WRITTEN.`

CHART-WRITTEN cannot be emitted until either PATH-A or PATH-B conditions are satisfied.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate all role files for that area; re-check IA-WRITTEN,
   ROLES-COMPLETE, and PROFILE quality for that area; update ARTIFACT-A headcount row.
2. --levels "[old-term]:[new-term]": replace level vocabulary across all role files
   and update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

This phase has exactly one responsibility: confirm that each IA file's lens field opens
verbatim with the lens-phrase derived in PHASE 5 (PROFILE).

SINGLE-PURPOSE GATE -- The following are NOT outputs of this phase:
- File writes of any kind
- Structural file-count checks or directory comparisons
- Headcount verifications or table audits
- AMEND generation or summary rows
- Any content beyond per-team verdicts and the DERIVATION-LOOP-CLOSED attestation

Any content in this phase beyond what is specified below is a build error.

For each team, emit:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[exact phrase from PHASE 5 PROFILE for this team]"
  IA file lens opens: "[first 8-12 words of the lens field in the written IA file]"
  VERDICT: [VERBATIM -- lens-phrase survives into written file |
            DRIFT -- lens-phrase absent or paraphrased]
```

DRIFT verdict: rewrite the IA file so the lens opens with the exact PROFILE lens-phrase.
Re-emit BUILD-VERIFY for that team with updated lens opening and VERBATIM verdict.
Do not proceed to the next team until the current team is VERBATIM.

After all teams are VERBATIM:

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed. Resistance profiles fully derivable from built files.
```

A DERIVATION-LOOP-CLOSED block that names fewer than [n] teams is structurally incomplete.
BUILD-VERIFY-COMPLETE must be emitted before DERIVATION-LOOP-CLOSED.

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

## V-02 -- Non-transplantable IA per-file gate (C-23 candidate)

**Axis**: Non-transplantable IA per-file verification
**Hypothesis**: R6 V-03 and V-04 state the non-transplantable rule -- "a lens that could
survive transplanting to a different team without rewrite is incorrect" -- but verify it
only through BUILD-VERIFY lens-phrase comparison. This leaves a gap: a lens-phrase that
sounds specific but uses vocabulary applicable to any team can pass BUILD-VERIFY (it opens
verbatim with the PROFILE phrase) while still being transplantable if the PROFILE phrase
itself was insufficiently grounded. R6 V-04 and V-05 added "lens is team-specific
(non-transplantable): YES / NO" as a third IA-WRITTEN check field. Making this the PRIMARY
axis of V-02 -- with explicit rewrite-and-re-emit on NO before the next team begins --
converts C-15 (portrait quality as a stated rule) into a per-file structural gate. A NO
verdict is not advisory; it is a build halt. Expected to surface as the primary signal
for C-23. Does not include V-01's BUILD-VERIFY derivation trace.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  nesting: [depth]
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
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

No files written. Four structural checks: (1) team name uniqueness within each group;
(2) role slug uniqueness within each team; (3) area slug uniqueness across org;
(4) nesting depth <= 3.
Emit VALIDATE block with per-check PASS/FAIL. Halt with VALIDATE-FAIL if any check fails.

---

### PHASE 3 -- CONTRACT

No files written.

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. Names at least two specific area names.
Sentence 3 makes a structural observation not visible from table rows alone.

**ARTIFACT-C -- Level Distribution**: breakdown by label, or `Level distribution: not declared.`

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

Extract one resistance profile per team.

For each team:

```
PROFILE: [team name]
  defended-artifact: [specific system/process/decision -- NOT a category]
  change-pressure: [specific proposed change threatening the defended-artifact]
  lens-phrase: [exact phrase that will open the IA file's lens field verbatim]
```

Failure mode: defended-artifact names a category -> rewrite before proceeding to next team.

`PROFILE-GATE: [n] profiles complete. PROFILE quality confirmed.`
Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

Write all Inertia Advocate files before any standard or specialized role files.

For each team, write `.craft/roles/{area-slug}/inertia-advocate.md` with five fields:
- **orientation**: grounds IA identity in this team's specific operational context
- **lens**: opens verbatim with the PROFILE lens-phrase; extends with team-domain vocabulary
- **expertise**: names actual systems, decisions, or failures in this domain -- no generic labels
- **scope**: tied to the defended-artifact from PROFILE
- **collaboration-pattern**: surfaces concerns early; does not veto; asks about rollback paths

After writing each IA file, emit IA-WRITTEN:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
  lens-team-specific (non-transplantable): [YES -- lens uses vocabulary unique to this
    team's domain; could not be reused verbatim for any other team's IA without rewriting |
    NO -- lens contains phrases applicable to any team's IA without modification;
    rewrite required before proceeding to next team]
```

**Non-transplantable enforcement gate**: A NO verdict on `lens-team-specific` is a build
halt. The IA lens must be rewritten so its content is grounded in this team's declared
domain vocabulary -- using system names, process names, or failure modes specific to this
team -- and IA-WRITTEN must be re-emitted with YES before writing the next team's IA file.

Named failure mode: "Any change to the existing architecture risks disrupting the team's
current workflow" is transplantable -- this phrase applies verbatim to any team's IA.
Named pass: "The schema contract table cannot be rewritten by a migration tool that lacks
a dry-run mode" is team-specific -- it references a concrete artifact unique to this team.

After all IA files:
`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed including
non-transplantable verification. All IA files written before standard and specialized roles.`

---

### PHASE 7 -- WRITE-ROLES

For each team: standard then specialized. After all teams: shared-group and exec-office
if declared. All files: five non-empty fields with substantive text.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. Transcribes sealed CONTRACT artifacts verbatim.

**Step 8a -- ASCII Hierarchy**: `+--` / `|`; all names verbatim; minimum two nesting levels;
every area from PARSE manifest present.

**Step 8b -- Transcription**: Transcribe ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.
Emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

PATH-A (all VERBATIM): `CHART-WRITTEN.`

PATH-B (any REVISED): rewrite deviant artifact to match sealed CONTRACT -> re-emit
TRANSCRIPTION-RECEIPT -> confirm all VERBATIM -> emit:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
```

Then: `CHART-WRITTEN.`

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate all role files; re-run IA-WRITTEN (all four checks
   including non-transplantable) for regenerated IA; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

Single responsibility: confirm each IA's lens opens verbatim with PROFILE lens-phrase.

EXCLUSION MANIFEST -- NOT outputs of this phase (presence is a build error):
- File writes, file-count checks, directory comparisons, headcount verifications
- AMEND generation, summary rows
- Content beyond per-team VERBATIM/DRIFT verdicts

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
  VERDICT: [VERBATIM | DRIFT]
```

DRIFT: rewrite IA file, re-emit BUILD-VERIFY with VERBATIM before next team.

`BUILD-VERIFY-COMPLETE: [n] teams VERBATIM.`

---

### PHASE 10 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [slugs vs parse manifest -- MATCH | extra/missing]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-03 -- BUILD-VERIFY exclusion manifest as typed structural error taxonomy

**Axis**: BUILD-VERIFY exclusion manifest as a named structural error taxonomy with typed
error codes
**Hypothesis**: R6 C-20 requires the BUILD-VERIFY phase to enumerate what it must NOT do.
R6 V-01 satisfied this with a prose prohibition list; V-02 framed it as "structurally
invalid" outputs. Neither gives the excluded outputs typed identifiers that make a violation
matchable against a named taxonomy. If excluded output types carry explicit error codes
(STRUCTURAL-ERROR:BV-FILE-WRITE, STRUCTURAL-ERROR:BV-COUNT-CHECK, etc.), violations become
enumerable and auditable -- a reviewer can check whether any output matches the exclusion
taxonomy by name, not just by judgment. The same structural-error taxonomy pattern also
applies to WRITE-CHART (STRUCTURAL-ERROR:WRITE-CHART-RECALC) and VALIDATE
(STRUCTURAL-ERROR:PHASE-2-FILE-WRITE), creating consistent exclusion enforcement across all
phases where out-of-scope behavior is most likely. Expected to satisfy C-20 at the highest
fidelity and push toward a new criterion for typed phase-boundary error taxonomy.
Does not include V-01's DERIVATION-LOOP-CLOSED or V-02's non-transplantable gate.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  nesting: [depth]
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
Halt with `PARSE-FAIL: [reason]` if `org.yaml` is missing or unreadable.

---

### PHASE 2 -- VALIDATE

STRUCTURAL-ERROR:PHASE-2-FILE-WRITE -- any file written during VALIDATE is a structural
error. This phase reads org.yaml state only.

Four checks: (1) team name uniqueness within group; (2) role slug uniqueness within team;
(3) area slug uniqueness across org; (4) nesting depth <= 3.
Emit VALIDATE block with per-check PASS/FAIL. Halt with VALIDATE-FAIL if any check fails.

---

### PHASE 3 -- CONTRACT

STRUCTURAL-ERROR:CONTRACT-FILE-WRITE -- any file written during CONTRACT is a structural
error. Artifacts are sealed here; files are written only in WRITE-IA and WRITE-ROLES.
STRUCTURAL-ERROR:CONTRACT-RECALC -- any recalculation of these artifacts outside this phase
is a structural error. The sealed values are copied verbatim in WRITE-CHART.

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B -- Narrative Summary**: 2-3 sentences. At least two specific area names.
Sentence 3: structural observation not visible from table rows alone.

**ARTIFACT-C -- Level Distribution**: breakdown by label if declared; else "not declared."

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

Extract one resistance profile per team.

```
PROFILE: [team name]
  defended-artifact: [specific named thing -- NOT a category label]
  change-pressure: [specific proposed change]
  lens-phrase: [phrase to open the IA lens field verbatim]
```

Failure mode: defended-artifact names a category -> rewrite before proceeding.
`PROFILE-GATE: [n] profiles complete.`

---

### PHASE 6 -- WRITE-IA

Write all Inertia Advocate files before any standard or specialized role files.

Per team: `.craft/roles/{area-slug}/inertia-advocate.md`
Fields: orientation, lens (opens verbatim with PROFILE lens-phrase), expertise (names
actual systems), scope (tied to defended-artifact), collaboration-pattern.

IA-WRITTEN per file:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
```

`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard roles.`

---

### PHASE 7 -- WRITE-ROLES

For each team: standard then specialized. After all teams: shared-group and exec-office
if declared. All files: five non-empty fields.

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.

STRUCTURAL-ERROR:WRITE-CHART-RECALC -- recalculating ARTIFACT-A/B/C values in this phase
rather than copying from CONTRACT-SEAL is a structural error. The seal is the source.

**Step 8a -- ASCII Hierarchy**: `+--` / `|`; all names verbatim; minimum two nesting levels;
every area from PARSE manifest present.

**Step 8b -- Transcription**: Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.
Emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-B: [VERBATIM | REVISED -- describe deviation]
  ARTIFACT-C: [VERBATIM | REVISED -- describe deviation]
```

**Step 8c -- PATH-A / PATH-B**

PATH-A shape (all VERBATIM):
```
PATH-A: all three artifacts VERBATIM.
CHART-WRITTEN.
```
A correct PATH-A output contains no TRANSCRIPTION-CLEAR block.
STRUCTURAL-ERROR:WRITE-CHART-SPURIOUS-CLEAR -- a TRANSCRIPTION-CLEAR emitted in PATH-A
before PATH-A confirmation is a structural error.

PATH-B shape (any REVISED):
```
[rewrite deviant artifact to match CONTRACT-SEAL]
[re-emit TRANSCRIPTION-RECEIPT -- all should now be VERBATIM]
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
PATH-B: TRANSCRIPTION-CLEAR passed.
CHART-WRITTEN.
```
STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT -- CHART-WRITTEN emitted before TRANSCRIPTION-CLEAR
in PATH-B is a structural error.
A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

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

This phase has exactly one output: per-team VERBATIM/DRIFT verdicts. All other outputs
match the exclusion manifest and are structural errors.

For each team:

```
BUILD-VERIFY: [team name]
  PROFILE lens-phrase: "[phrase from PHASE 5]"
  IA lens opens: "[first 8-12 words of written lens field]"
  VERDICT: [VERBATIM | DRIFT]
```

DRIFT: rewrite IA file, re-emit BUILD-VERIFY with VERBATIM before next team.

`BUILD-VERIFY-COMPLETE: [n] teams VERBATIM.`

---

### PHASE 10 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [slugs vs parse manifest -- MATCH | extra/missing]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-04 -- DERIVATION-LOOP-CLOSED + Non-transplantable gate (V-01 + V-02)

**Axes**: DERIVATION-LOOP-CLOSED + Non-transplantable IA per-file gate
**Hypothesis**: V-01 closes the derivation chain at BUILD-VERIFY time (was the lens
actually derived?); V-02 gates it at write time (is the result non-transplantable?). The
two axes address the same quality objective from opposite ends of the lifecycle. V-02
prevents a generic lens from being written; V-01 confirms that what was written traces
back to the resistance profile. A lens that passes non-transplantable verification at
write time AND survives BUILD-VERIFY as a closed derivation chain is verified at both
production and confirmation points. Together these should surface C-22 and C-23
simultaneously and show whether the two gates reinforce each other or are redundant.
Risk: increased write-time friction (non-transplantable gate) may produce more rewrite
loops without improving coverage of the other 19 criteria.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  nesting: [depth]
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

No files written. Four checks: (1) team name uniqueness within group; (2) role slug
uniqueness within team; (3) area slug uniqueness across org; (4) nesting depth <= 3.
Emit VALIDATE block. Halt with VALIDATE-FAIL if any check fails.

---

### PHASE 3 -- CONTRACT

No files written.

**ARTIFACT-A -- Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | -- | -- | -- | [n or 0] | -- |
| shared | -- | -- | -- | [n or 0] | -- |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

**ARTIFACT-B**: 2-3 sentences naming at least two specific areas. Sentence 3: structural
observation not visible from rows alone.

**ARTIFACT-C**: level breakdown by label, or "not declared."

`TABLE-CLOSED: [n] files required.`

---

### PHASE 4 -- CONTRACT-SEAL

```
CONTRACT-SEAL:
  ARTIFACT-A: SEALED -- [n] rows, Total = [n]
  ARTIFACT-B: SEALED -- [first 8 words...]
  ARTIFACT-C: SEALED
  CONTRACT-SEAL-PASS
```

---

### PHASE 5 -- PROFILE

Per team:

```
PROFILE: [team name]
  defended-artifact: [specific named system/process/decision]
  change-pressure: [specific proposed change threatening it]
  lens-phrase: [exact phrase to open IA lens verbatim]
```

Failure mode: defended-artifact names a category -> rewrite before next team.
`PROFILE-GATE: [n] profiles complete. All lens-phrases derived.`

---

### PHASE 6 -- WRITE-IA

Write all IA files before any standard or specialized roles.

Per team: `.craft/roles/{area-slug}/inertia-advocate.md`
Fields: orientation (grounds IA in this team's specific context), lens (opens verbatim
with PROFILE lens-phrase), expertise (names actual systems or decisions), scope (tied to
defended-artifact), collaboration-pattern (early concern surfacing, asks about rollback paths).

IA-WRITTEN per file:

```
IA-WRITTEN: [team name]
  orientation-concrete: [YES | NO -- rewrite required]
  expertise-concrete: [YES | NO -- rewrite required]
  lens-phrase-verbatim: [YES | NO -- rewrite required]
  lens-team-specific (non-transplantable): [YES -- vocabulary unique to this team's
    domain; cannot be reused verbatim for any other team's IA |
    NO -- contains phrases applicable to any team without modification;
    rewrite required before proceeding to next team]
```

Non-transplantable enforcement: NO on `lens-team-specific` halts the build. Rewrite IA
lens using this team's specific system names, process names, or failure modes. Re-emit
IA-WRITTEN with YES before proceeding to the next team's IA file.

`IA-PHASE-COMPLETE: [n of n] teams covered. All four IA-WRITTEN checks passed including
non-transplantable verification.`

---

### PHASE 7 -- WRITE-ROLES

For each team: standard then specialized. After all teams: shared-group and exec-office
if declared. All files: five non-empty fields with substantive text.

`ROLES-COMPLETE: [n] files written.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. Transcribes sealed artifacts verbatim.

**ASCII Hierarchy**: `+--` / `|`; all names verbatim; minimum two nesting levels; every area present.

**Transcription**: transcribe ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: [VERBATIM | REVISED]
  ARTIFACT-B: [VERBATIM | REVISED]
  ARTIFACT-C: [VERBATIM | REVISED]
```

PATH-A (all VERBATIM): `CHART-WRITTEN.`

PATH-B (any REVISED): rewrite deviant artifact -> re-emit TRANSCRIPTION-RECEIPT -> confirm
all VERBATIM -> emit:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  All three confirmed -- PATH-B exit authorized.
```

Then: `CHART-WRITTEN.`

**AMEND**:

```
AMEND:
1. --area "[area name]": regenerate role files; re-run IA-WRITTEN (all four checks
   including non-transplantable) for regenerated IA; update ARTIFACT-A.
2. --levels "[old]:[new]": replace level vocabulary; update ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update hierarchy, paths, table.
```

---

### PHASE 9 -- BUILD-VERIFY

Single responsibility: confirm each IA lens opens verbatim with PROFILE lens-phrase.

EXCLUSION MANIFEST -- NOT outputs of this phase (presence is a build error):
- File writes, file-count checks, directory audits, headcount verifications
- AMEND generation, summary rows
- Content beyond per-team VERBATIM/DRIFT verdicts and DERIVATION-LOOP-CLOSED

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
  All [n] chains confirmed closed. Resistance profiles fully derivable from built files.
```

---

### PHASE 10 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- [MATCH | MISMATCH]
  IA count: [n teams], IA files: [n] -- [MATCH | MISMATCH]
  dir check: [slugs vs parse manifest -- MATCH | extra/missing]
  table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n] -- [MATCH | MISMATCH]
  CROSS-REF: [PASS | FAIL]
```

`BUILD-COMPLETE: org-chart.md written. [n] role files written. CROSS-REF PASS.`

---

## V-05 -- Full integration (V-01 + V-02 + V-03 + complete architecture)

**Axes**: DERIVATION-LOOP-CLOSED + non-transplantable per-file gate + BUILD-VERIFY exclusion
manifest as typed structural error taxonomy
**Hypothesis**: All three R7 axes address different aspects of the IA quality derivation
problem. V-01 closes the derivation chain at verification time (was it actually derived?).
V-02 gates specificity at write time (is the result non-transplantable?). V-03 defines
out-of-scope behavior as typed structural errors (does the verifier stay in its lane?).
Together, with WRITE-ROLES before WRITE-CHART and the full phase sequence from the R6
baseline, this variation delivers the maximum structural density for rubric-extraction
signal. The DERIVATION-LOOP-CLOSED token combined with BUILD-VERIFY per-team traces creates
a new auditable record format: each IA's full derivation chain
(PROFILE -> IA-WRITTEN non-transplantable YES -> BUILD-VERIFY VERBATIM -> DERIVATION-LOOP-CLOSED)
is recoverable as a named trace. This may surface as a candidate for C-24: full per-team IA
derivation audit trail recoverable from phase output alone.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF.
Each phase gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  nesting: [depth]
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

STRUCTURAL-ERROR:PHASE-2-FILE-WRITE -- any file written during VALIDATE is a structural error.

Four checks: (1) team name uniqueness within group; (2) role slug uniqueness within team;
(3) area slug uniqueness across org; (4) nesting depth <= 3.
Emit VALIDATE block with per-check PASS/FAIL. Halt with VALIDATE-FAIL if any check fails.

---

### PHASE 3 -- CONTRACT

STRUCTURAL-ERROR:CONTRACT-FILE-WRITE -- any file written during CONTRACT is a structural error.
STRUCTURAL-ERROR:CONTRACT-RECALC -- any recalculation of these artifacts outside this phase
is a structural error. CONTRACT-SEAL values are copied verbatim in WRITE-CHART only.

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
  ARTIFACT-B: SEALED -- [first 8 words...]
  ARTIFACT-C: SEALED
  CONTRACT-SEAL-PASS
```

No modifications to sealed artifacts after this point.

---

### PHASE 5 -- PROFILE

Extract one resistance profile per team before writing any IA file.

Per team:

```
PROFILE: [team name]
  defended-artifact: [specific named system/process/decision -- NOT a category label]
  change-pressure: [specific proposed change threatening the defended-artifact]
  lens-phrase: [exact phrase drawn from defended-artifact + change-pressure vocabulary;
               will open the IA file's lens field verbatim]
```

Failure modes:
- Defended-artifact names a category (e.g., "the existing pipeline architecture") rather
  than a specific thing (e.g., "the event-resequencing buffer that handles out-of-order
  arrivals from Kafka partition 7") -- rewrite before next team
- Lens-phrase uses vocabulary not present in defended-artifact or change-pressure -- rewrite

`PROFILE-GATE: [n] profiles complete. All defended-artifacts specific. All lens-phrases
derived from team vocabulary. No two profiles share identical lens-phrases.`

Do not proceed to WRITE-IA until PROFILE-GATE is emitted.

---

### PHASE 6 -- WRITE-IA

Write ALL Inertia Advocate files before ANY standard or specialized role files.

STRUCTURAL-ERROR:IA-OUT-OF-ORDER -- writing a standard or specialized role file before
all IA files for that team are complete is a structural error.

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

For each team in declaration order:
1. **Standard roles** -- `role-type: standard`, `area: {area-slug}`
2. **Specialized roles** (if declared) -- `role-type: specialized`; F-2 and F-3 must
   name domain-specific systems that distinguish this role from standard roles on the
   same team; a specialized lens identical to any standard lens on the same team fails
   distinctness and requires rewrite

After all teams: write shared-group roles to `.craft/roles/shared/` (role-type: shared-group)
and exec-office roles to `.craft/roles/exec-office/` (role-type: exec-office) if declared.

Every role file: five non-empty fields with substantive, non-"TBD" body text
(orientation, lens, expertise, scope, collaboration-pattern).

`ROLES-COMPLETE: [n] files written to .craft/roles/.`

---

### PHASE 8 -- WRITE-CHART

Write `org-chart.md`. This phase transcribes sealed CONTRACT artifacts verbatim.

STRUCTURAL-ERROR:WRITE-CHART-RECALC -- recalculating ARTIFACT-A/B/C values in this phase
rather than transcribing from CONTRACT-SEAL is a structural error.

**Step 8a -- ASCII Hierarchy**: Use `+--` and `|`. All names verbatim from `org.yaml`.
Minimum two nesting levels. Every area from PARSE manifest must appear.

**Step 8b -- Transcription**: Copy ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim from
CONTRACT-SEAL into org-chart.md. Do not recalculate. Do not reformat. The sealed
artifact is the source.

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
A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete --
it must name A, B, and C individually, including those VERBATIM before any rewrite.

**Step 8d -- AMEND**

```
AMEND:
1. --area "[area name]": regenerate all role files for that area; re-run IA-WRITTEN
   (all four checks, including non-transplantable) for regenerated IA; update ARTIFACT-A
   headcount row.
2. --levels "[old]:[new]": replace level vocabulary across all role files and ARTIFACT-C.
3. --restructure "[team] > [new-parent]": update ASCII hierarchy, role file paths,
   area slug map, and ARTIFACT-A table.
```

---

### PHASE 9 -- BUILD-VERIFY

This phase has exactly one responsibility: confirm each IA file's lens field opens verbatim
with the lens-phrase derived in PHASE 5 (PROFILE).

EXCLUSION-MANIFEST -- the following output types are STRUCTURAL-ERROR:BUILD-VERIFY-OOB
and their presence in this phase is a build error:

| Excluded output type | Error code |
|----------------------|------------|
| File writes of any kind | STRUCTURAL-ERROR:BV-FILE-WRITE |
| File-count checks (total vs org.yaml) | STRUCTURAL-ERROR:BV-COUNT-CHECK |
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
lens-phrase. Re-emit BUILD-VERIFY for that team showing the updated lens opening and
VERBATIM verdict. The next team cannot be verified until the current team shows VERBATIM.

After all teams are VERBATIM:

```
BUILD-VERIFY-COMPLETE:
  [n] teams verified VERBATIM.

DERIVATION-LOOP-CLOSED:
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED
  [repeat one line per team]
  All [n] chains confirmed closed.
  Each resistance profile is fully recoverable from the built IA file's lens opening.
```

A DERIVATION-LOOP-CLOSED block that names fewer than [n] teams is structurally incomplete.
A DERIVATION-LOOP-CLOSED block emitted before BUILD-VERIFY-COMPLETE is structurally invalid.

---

### PHASE 10 -- CROSS-REF

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
