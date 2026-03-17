---
skill: quest-variate
skill_target: corps-build
round: 6
date: 2026-03-16
rubric_version: 6
---

# Variate R6 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v6 adds C-21: TRANSCRIPTION-CLEAR as named structural re-audit gate after any
REVISED-triggered rewrite. R5 V-01 (99.58 pts) got PARTIAL on C-19 because after
rewriting a REVISED artifact it asserted TRANSCRIPTION-PASS covering only that artifact.
R5 V-02 (100 pts) already satisfies C-21 by listing all three artifacts in
TRANSCRIPTION-CLEAR. R6 isolates C-21 as a single axis, explores the deferred
phrasing-register axis from R5 V-03, and produces a full integration.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis: TRANSCRIPTION-CLEAR re-audit covers all artifacts, not only the rewritten one | V-01 |
| Output format: two-path conditional structure (PATH-A all-VERBATIM / PATH-B has-REVISED) | V-02 |
| Phrasing register: declarative output-forward framing for all 13 aspirational criteria | V-03 |
| Lifecycle + Inertia framing: resistance profiles as structural anchor with C-21 integrated | V-04 |
| Full integration: all 13 aspirational criteria C-09 through C-21 | V-05 |

---

## R5 Gap Analysis (rubric v6 lens)

| New Criterion | Best R5 Coverage | Gap |
|---------------|-----------------|-----|
| C-21 TRANSCRIPTION-CLEAR structural re-audit | R5 V-02: TRANSCRIPTION-CLEAR block lists all three artifacts after any rewrite; 100 pts | R5 V-01 (99.58): rewrites the REVISED artifact then asserts TRANSCRIPTION-PASS -- but the assertion covers only that artifact. A model can comply with R5 V-01 by rewriting ARTIFACT-A, asserting it is now VERBATIM, and emitting CHART-WRITTEN without re-checking ARTIFACT-B and ARTIFACT-C. C-21 closes this: the named re-audit block must enumerate every contract artifact in a single pass, including those that were already VERBATIM before the rewrite. |
| V-03 phrasing-register axis | R5 V-03: declarative framing for C-19 and C-20 only; aspirational table empty | R5 V-03 named the axis but did not extend it past the two R5-era criteria. R6 V-03 applies declarative output-forward framing to all 13 aspirational criteria: PROFILE shapes (C-16), IA portrait shapes (C-15), TRANSCRIPTION-CLEAR conditional shapes (C-19/C-21), BUILD-VERIFY block shapes (C-17/C-20). Each criterion is expressed as a description of what correct output looks like, not a behavioral instruction. |

The gap for C-21 is coverage scope: the re-audit block must include unrevised artifacts,
not only the artifact that changed. The gap for V-03 is depth: the declarative framing
axis was introduced but not developed past the R5 mechanism pair.

---

## V-01 -- Lifecycle: TRANSCRIPTION-CLEAR re-audit covers all artifacts after any rewrite (C-21)

**Axis**: Lifecycle emphasis
**Hypothesis**: R5 V-01 got PARTIAL on C-19 because after a rewrite it only re-audited
the rewritten artifact. The minimal structural fix is explicit: after any REVISED-triggered
rewrite, the TRANSCRIPTION-CLEAR block must enumerate ARTIFACT-A, ARTIFACT-B, and
ARTIFACT-C -- including the ones that were already VERBATIM before the rewrite. The block
is the exit gate; it covers all three or it does not exist. The exemption is also made
explicit: if all three receipts are VERBATIM on first pass (no rewrites occurred),
CHART-WRITTEN follows immediately and no TRANSCRIPTION-CLEAR is required.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  nesting depth: [n]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry condition**: PARSE-PASS. **No files written during this phase.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared
        PASS / FAIL -- teams with no roles: [list]
  [V-2] no role name in both standard and specialized for the same team
        PASS / FAIL -- collisions: [team.role list]
  [V-3] no duplicate team names across groups
        PASS / FAIL -- duplicates: [list]
  [V-4] level vocabulary uses one consistent label convention
        PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. Proceeding to CONTRACT.`
or `VALIDATE-FAIL: [n] error(s). No files written. Halt.`

---

### PHASE 3 -- CONTRACT

**Entry condition**: VALIDATE-PASS. **No files written during this phase.**
**This phase produces three contract artifacts. They are sealed in Phase 4 and
transcribed verbatim into org-chart.md in Phase 6. They are not regenerated at write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

One row per area. Headcount = count of all role slots for that area.
Total = sum of all area rows.

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

Write exactly 2-3 sentences interpreting the numbers:
- Sentence 1: name the largest area by headcount and express as percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: a structural observation the table rows alone do not convey

Strong example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml, suggesting the org has not yet leveled its management layer. The three product
> teams each carry two specialized roles, a higher ratio than any infrastructure team."

Weak example (do not produce this):
> "The org has several teams with different headcount. Level distribution is shown below."

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence:**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One sentence on seniority profile referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels). Proceeding to seal.`

---

### PHASE 4 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A (headcount table):    [n] area rows, total headcount = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B (analytic prose):     [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C (level distribution): [n] levels, total = [n]

  RULE: These artifacts are FINAL. org-chart.md sections 2-4 are copies of these
        artifacts -- not regenerations. Do not recalculate headcount. Do not rewrite
        the analytic prose. Do not reformat the level table.
        Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 6.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry condition**: CONTRACT-GATE. **No files written during this phase.**

For every team, extract a resistance profile:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift -- not a generic force]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [list, one per line: team: "phrase"]`

Collision check: any identical lens phrases -> `LENS-COLLISION: [teams]. Revise one before continuing.`

`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: PROFILE-GATE.
**Write all Inertia Advocate files before any standard or specialized role files.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:
- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; 2-3 sentences;
  no generic stability language; no boilerplate applicable to any team
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart (the role most likely
  to propose the change-pressure initiative)

No two IA files share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 5]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite that field before proceeding to next team.

`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized roles.`

---

### PHASE 7 -- WRITE-CHART

**Entry condition**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs from org.yaml]
   ```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1-lock: "[verbatim]"
    org-chart.md sentence 1:  "[verbatim]"
    verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
```

**Two exit paths from TRANSCRIPTION-RECEIPT:**

PATH-A (all three verdicts are VERBATIM on first receipt):
No rewrites occurred. No TRANSCRIPTION-CLEAR block is required.
`CHART-WRITTEN.`

PATH-B (one or more verdicts are REVISED):
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line to show corrected values and VERBATIM.
2. After all rewrites are complete, emit TRANSCRIPTION-CLEAR:
   This block re-audits every contract artifact in a single pass -- including those
   that were already VERBATIM before the rewrite. The block covers all three or it
   does not serve as an exit gate.

   ```
   TRANSCRIPTION-CLEAR:
     ARTIFACT-A: VERBATIM
     ARTIFACT-B: VERBATIM
     ARTIFACT-C: VERBATIM
     all three confirmed -- CHART-WRITTEN authorized
   ```

   If any artifact shows REVISED in this re-audit: return to step 1 for that artifact.
   The phase cannot close until TRANSCRIPTION-CLEAR lists all three as VERBATIM.
   `CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
Paths: `.craft/roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.craft/roles/{group-slug}/{role-slug}.md` (shared group),
`.craft/roles/exec-office/{role-slug}.md` (exec office)

All five fields, no placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

**SINGLE-PURPOSE GATE**
This phase has exactly one responsibility: confirm that every Inertia Advocate role
file's lens field opens with the exact lens-phrase derived in Phase 5.
This phase produces exactly one output per team: a VERBATIM or DRIFT verdict.
This phase contains NO file writes, NO structural file-count checks, NO directory
comparisons, NO headcount verifications, NO AMEND generation, and NO summary rows.
Any content beyond per-team VERBATIM/DRIFT verdicts inside this phase block is a build error.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 5]"
  IA lens field opening:  "[exact first phrase in written .craft/roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

After all teams:
`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 5 profiles.`
or `BUILD-VERIFY-FAIL: [n] mismatch(es): [team names]. Correct each before proceeding.`
`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  if MISMATCH: missing: [list]
  IA files:  teams [n], IA files [n] -- MATCH / MISMATCH
  dir check: areas in org.yaml [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`
Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4 checks)
  contract:      SEALED (headcount=[n], analytic prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA coverage:   [n of n] teams -- written before standard/specialized
  org-chart.md:  [PATH-A: all VERBATIM first pass -- no re-audit required |
                  PATH-B: post-rewrite TRANSCRIPTION-CLEAR -- all three artifacts confirmed]
  role files:    [n] written / [n] declared
  build-verify:  PASS (single-purpose: [n of n] IA lens verdicts only)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-02 -- Output format: two-path conditional structure (PATH-A / PATH-B)

**Axis**: Output format
**Hypothesis**: The C-21 requirement has an important exemption: if all three artifacts
are VERBATIM on first receipt, no TRANSCRIPTION-CLEAR block is required. V-01 states this
as a rule. V-02 makes the branching structure the primary design feature of the
WRITE-CHART phase -- framing it as two named, mutually exclusive paths with different
exit shapes. This makes the exemption structurally visible (PATH-A produces a shorter
output than PATH-B) and makes non-compliance with C-21 structurally visible (a model that
emits CHART-WRITTEN after a REVISED verdict without TRANSCRIPTION-CLEAR is not following
either path). The binary branching also clarifies that PATH-B's TRANSCRIPTION-CLEAR is
mandatory, not optional, when it applies.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Step sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next step begins.

---

**STEP 1 -- PARSE**

```
PARSE:
  org name: [name]
  groups: [list]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

---

**STEP 2 -- VALIDATE**

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

---

**STEP 3 -- CONTRACT**

**Entry**: VALIDATE-PASS. **No files written.**
**Three contract artifacts. Sealed in Step 4. Transcribed verbatim into org-chart.md
in Step 6. Not regenerated at write time.**

**ARTIFACT-A -- Headcount table:**
```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
Sentence 1: largest area by headcount as percentage of total.
Sentence 2: dominant level label, or note its absence.
Sentence 3: structural observation the table rows alone do not convey. No generic summaries.

**ARTIFACT-C -- Level distribution table + seniority sentence.**
```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

**STEP 4 -- CONTRACT-SEAL**

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite.
        Enforcement: TRANSCRIPTION-RECEIPT in Step 6.
        If any REVISED verdict: TRANSCRIPTION-CLEAR (all three artifacts) required before
        CHART-WRITTEN. If all VERBATIM on first receipt: CHART-WRITTEN directly.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

**STEP 5 -- PROFILE**

**Entry**: CONTRACT-GATE. **No files written.**

For each team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; opens IA lens field verbatim]
```

```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: profiles confirmed. Proceeding to WRITE-IA.`

---

**STEP 6 -- WRITE-IA**

**Entry**: PROFILE-GATE.
**All IA files before any standard or specialized role files.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern
- **lens**: opens verbatim with lens-phrase; 2-3 sentences; no generic stability language
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 5]"
  opens verbatim: YES / NO
  expertise concrete: YES / NO
```
Any NO -> rewrite that field before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams.`

---

**STEP 7 -- WRITE-CHART**

**Entry**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:
1. ASCII hierarchy
2. [TRANSCRIBE ARTIFACT-A verbatim]
3. [TRANSCRIBE ARTIFACT-B verbatim]
4. [TRANSCRIBE ARTIFACT-C verbatim + seniority sentence]
5. AMEND section (--area, --levels, --restructure with specific values from org.yaml)

Emit TRANSCRIPTION-RECEIPT immediately after writing org-chart.md:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1: "[phrase]" / org-chart.md sentence-1: "[phrase]"  -- verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
```

**Evaluate the receipt. Follow exactly one path:**

---
PATH-A: All three verdicts are VERBATIM.
No rewrites occurred. No re-audit is required.
`CHART-WRITTEN.`
---

---
PATH-B: One or more verdicts are REVISED.
For each REVISED artifact:
  1. Rewrite that section in org-chart.md from the sealed CONTRACT artifact.
  2. Update that receipt line: corrected values, verdict changed to VERBATIM.

After all REVISED artifacts have been rewritten:
Emit TRANSCRIPTION-CLEAR. This block re-audits all three artifacts in one pass --
including those that were VERBATIM before the rewrites. CHART-WRITTEN cannot be
emitted until this block is present and all three lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm value matches CONTRACT-SEALED]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1-lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  all three confirmed -- PATH-B exit authorized
```

If TRANSCRIPTION-CLEAR shows any REVISED: return to step 1 of PATH-B for that artifact.

`CHART-WRITTEN.`
---

---

**STEP 8 -- WRITE-ROLES**

**Entry**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
All five fields. No placeholder text. Scope explicit.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

**STEP 9 -- BUILD-VERIFY**

**Entry**: ROLES-COMPLETE.

**SINGLE-PURPOSE GATE**
One responsibility: confirm each IA lens field opens with the exact lens-phrase from Step 5.
One output per team: a VERBATIM or DRIFT verdict.
NO file writes. NO structural checks. NO directory comparisons. NO headcount verifications.
NO summary rows. NO other outputs. Any content beyond per-team verdicts is a build error.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 5]"
  IA lens field opening:  "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens to open with profile phrase verbatim.
Reemit that team's BUILD-VERIFY block showing VERBATIM before proceeding.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Step 5 profiles.`
`BUILD-VERIFY-COMPLETE.`

---

**STEP 10 -- CROSS-REF**

**Entry**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:      areas [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4)
  contract:      SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams
  IA phase:      [n of n] teams written before standard/specialized
  transcription: [PATH-A: all VERBATIM, no re-audit | PATH-B: TRANSCRIPTION-CLEAR, all confirmed]
  role files:    [n] written / [n] declared
  build-verify:  PASS -- [n of n] verdicts (single-purpose block, no other outputs)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-03 -- Phrasing register: declarative output-forward framing (deferred R5 axis, all 13 criteria)

**Axis**: Phrasing register
**Hypothesis**: R5 V-03 applied declarative framing to C-19 and C-20 only, leaving the
aspirational table empty. A fully declarative prompt describes what correct output looks
like at every stage, covering all 13 aspirational criteria. Each criterion is expressed
as a shape constraint on the output -- not a behavioral instruction. The model sees what
a correct PROFILE looks like, what a correct IA portrait looks like, what a correct
TRANSCRIPTION-CLEAR block looks like (for both the all-VERBATIM and the post-rewrite case),
and what a correct BUILD-VERIFY block looks like. Shapes are harder to elide than
behavioral instructions because elision produces visibly wrong output rather than
instructions-not-followed output.

```
You are running `corps-build`. Read org.yaml in the working directory, or use the path provided.

`corps-build` produces two artifacts: **org-chart.md** and **.craft/roles/ files**.
What follows describes what correct output looks like at each stage. Every description
is a constraint on output shape, not an instruction about behavior. Output that does not
match the described shapes is a build failure.

---

### Stage 1 -- Parse

A correct parse block:
```
PARSE: [org name], [n] teams, [n] role slots, nesting depth [n].
```

If malformed: `PARSE-FAIL: [description]. Halt.`

---

### Stage 2 -- Validate

A correct validate block:
```
VALIDATE: no structural anomalies. [n] teams, [n] slots confirmed.
```

Or if problems exist -- one line per problem, then halt. No files are written by a
validate block. A validate block that does not halt on problems is structurally invalid.

---

### Stage 3 -- Build contract

A correct build has three contract artifacts produced before any file is written:

```
CONTRACT-DRAFT:
  ARTIFACT-A (headcount table, [n] area rows, total=[n])
  ARTIFACT-B (analytic prose, [n] sentences)
  ARTIFACT-C (level distribution, [n] rows, total=[n])
```

A correct ARTIFACT-A: one row per area; headcount column is count of all role slots
for that area; Total row sums all area rows. A row with a wrong total is structurally
invalid.

A correct ARTIFACT-B interprets the numbers with specific names:
> "Data Engineering carries 11 of 28 total headcount -- the largest area at 39%. Six of
> eight Data Engineering teams declare IC levels; two carry no level vocabulary. The two
> real-time processing teams carry more specialized roles per headcount than any batch
> processing team -- three specialized versus one or two."

An incorrect ARTIFACT-B contains no area names, no specific counts, or no structural
observations -- only generic description. An incorrect ARTIFACT-B is invalid even if
correct in structure.

A correct ARTIFACT-C: one row per level label present in org.yaml; Count and % of Org
columns; Total row showing 100%. A missing level label is structurally invalid.

---

### Stage 4 -- CONTRACT-SEAL

A correct seal block:
```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total=[n]; first-row lock: "[area] | [n]"
  ARTIFACT-B: [n] sentences; sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] rows, total=[n]
  RULE: org-chart.md sections 2-4 are copies of these artifacts.
        Any drift from CONTRACT-SEALED values is a build failure.
        Detected and corrected at TRANSCRIPTION-RECEIPT.
        TRANSCRIPTION-CLEAR authorizes CHART-WRITTEN.
```

`CONTRACT-GATE: [n] files to produce.`

A seal block that does not include the RULE is structurally incomplete.

---

### Stage 5 -- Resistance profiles

A correct build has one resistance profile per team, produced before any IA file is written.

A correct profile:
```
PROFILE: [team name]
  defended-artifact:  [named thing this team owns -- not a category]
  change-pressure:    [named initiative threatening it -- not a generic force]
  lens-phrase:        "[5-10 words compressing the specific tension; verbatim
                      opening of this team's IA lens field; cannot be written
                      without knowing both defended-artifact and change-pressure]"
```

An incorrect profile has a `defended-artifact` that names a category ("data stability",
"system reliability") rather than a specific thing ("the nightly reconciliation job",
"the schema contract table"). An incorrect profile is invalid even if complete in
structure.

A correct profile summary:
```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

`PROFILE-GATE: profiles confirmed.`

---

### Stage 6 -- IA role files

A correct build writes all IA files before any standard or specialized role file.

A correct IA role file is a person-portrait:
- **orientation** names the specific thing this person watches for -- not generic caution.
  An orientation that could apply to any team's IA is incorrect.
- **lens** opens with the resistance profile lens-phrase verbatim. It expands in 2-3
  sentences describing a specific worldview anchored to this team's domain. It contains
  no generic stability language ("ensures process stability", "advocates for continuity",
  "resists unnecessary change"). An IA lens that could survive transplanting to a
  different team without rewrite is incorrect.
- **expertise** names the specific defended-artifact by name, not by category. It differs
  from every other team's IA expertise body text.
- **scope**: `standard -- present in all teams`
- **collaboration pattern** names forums, cadence, and primary counterpart by role name.

A correct per-file confirmation:
```
IA-WRITTEN: [team]
  lens opens with profile lens-phrase: YES / NO
  expertise concrete (not a category): YES / NO
```
A NO verdict requires a rewrite before the next team is started.

`IA-COMPLETE: [n of n] teams.`

---

### Stage 7 -- Standard and specialized role files

A correct role file contains all five fields (orientation, lens, expertise, scope,
collaboration pattern). No field is a placeholder. Scope names the role type explicitly.
A role file with any omitted or placeholder field is structurally invalid.

`ROLES-COMPLETE: [n] files written.`

---

### Stage 8 -- org-chart.md and transcription confirmation

**What correct org-chart.md write output looks like:**

org-chart.md has five sections: (1) ASCII hierarchy, (2) headcount table, (3) analytic
prose, (4) level distribution, (5) AMEND.

Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content. Not a rewrite.
A section that differs from the sealed CONTRACT artifact is structurally incorrect.

A correct TRANSCRIPTION-RECEIPT immediately follows org-chart.md write:
```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1: "[phrase]" / org-chart.md sentence-1: "[phrase]"  -- verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
```

**Two correct exit shapes:**

Shape A -- all three verdicts VERBATIM (no rewrites occurred):
```
TRANSCRIPTION-RECEIPT: [all three VERBATIM as above]
CHART-WRITTEN.
```
A TRANSCRIPTION-CLEAR block does not appear. CHART-WRITTEN follows directly.

Shape B -- one or more verdicts REVISED (rewrite occurred):
```
TRANSCRIPTION-RECEIPT: [at least one REVISED]
[rewrite of REVISED section(s)]
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
CHART-WRITTEN.
```
A correct TRANSCRIPTION-CLEAR names all three artifacts -- not only the one that was
rewritten. A TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally
incomplete. CHART-WRITTEN appears only after TRANSCRIPTION-CLEAR in Shape B.
A build that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR after any REVISED verdict
is structurally invalid.

---

### Stage 9 -- BUILD-VERIFY

**What a correct BUILD-VERIFY block looks like:**

The BUILD-VERIFY block runs after all role files are written and before CROSS-REF.
It contains exactly N entries, where N is the number of teams.
Each entry is one VERBATIM or DRIFT verdict for one team.
The block contains nothing else: no file-count checks, no directory checks, no headcount
verifications, no summary rows.

A correct BUILD-VERIFY block for a 3-team org:
```
BUILD-VERIFY: [Team A] -- lens: "[phrase]" -- VERBATIM
BUILD-VERIFY: [Team B] -- lens: "[phrase]" -- VERBATIM
BUILD-VERIFY: [Team C] -- lens: "[phrase]" -- VERBATIM
```

Or expanded:
```
BUILD-VERIFY: [team name]
  profile lens-phrase:   "[phrase from profiles stage]"
  IA lens field opening: "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

A DRIFT verdict requires a rewrite and re-emission of that entry as VERBATIM before the
next team entry appears. A BUILD-VERIFY block with non-verdict content is structurally
invalid even if the verdicts themselves are correct.

`BUILD-VERIFY-PASS: [n of n] verdicts VERBATIM.`
`BUILD-VERIFY-COMPLETE.`

---

### Stage 10 -- Cross-reference

A correct cross-reference block:
```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       [n of n] teams -- MATCH / MISMATCH
  table fidelity: CONTRACT [n] == org-chart.md [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**CORPS-BUILD -- {date}**

A correct final summary names the actual values, not placeholders:
```
  parse:          [org name], [n] teams
  validate:       PASS -- no anomalies
  contract:       SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:       [n of n] teams (specific artifacts, not categories)
  IA files:       [n of n] -- portraits from profiles, written before standard/specialized
  standard roles: [n], specialized roles: [n]
  org-chart.md:   [Shape A: all VERBATIM | Shape B: TRANSCRIPTION-CLEAR, all three confirmed]
  build-verify:   [n of n] VERBATIM verdicts -- block contained nothing else
  cross-ref:      PASS / FAIL
  status:         COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-04 -- Lifecycle + Inertia framing: resistance profiles as structural anchor with C-21

**Axes**: Lifecycle emphasis + Inertia framing
**Hypothesis**: Variations V-01 through V-03 treat resistance profiles (PROFILE phase)
as one phase among many. This variation makes resistance profiles the structural anchor
of the entire build: the org is a resistance map before it is a headcount table, and
every generated artifact traces back to a profile. This framing elevation serves C-15
and C-16 (portrait quality and profile-derivation) by making them the defining
structural property of the output, not subordinate quality criteria. The TRANSCRIPTION-CLEAR
requirement (C-21) is integrated as a consequence of the contract-verbatim architecture,
not introduced as a separate rule. The inertia-forward framing also changes the IA file
write order: profiles are extracted immediately after VALIDATE (not after CONTRACT),
because profiles are the source from which the headcount contract is assembled.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

`corps-build` generates the org as a resistance map: every team declares a defended
artifact and a change pressure, and every artifact in the build traces back to those
declarations. The headcount table is a count of resistance positions, not just role slots.
The org-chart.md is a map of what the org is defending, not just who reports to whom.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  nesting depth: [n]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry condition**: PARSE-PASS. **No files written during this phase.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared
        PASS / FAIL -- teams with no roles: [list]
  [V-2] no role name in both standard and specialized for the same team
        PASS / FAIL -- collisions: [team.role list]
  [V-3] no duplicate team names across groups
        PASS / FAIL -- duplicates: [list]
  [V-4] level vocabulary uses one consistent label convention
        PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

---

### PHASE 3 -- PROFILE (before CONTRACT)

**Entry condition**: VALIDATE-PASS. **No files written during this phase.**
**Resistance profiles are extracted before the headcount contract is built.
The contract is assembled from profiles, not independent of them.**

For each team, name the thing it would defend and the initiative threatening it:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift -- not a generic force]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field;
                      a phrase that could not be written without knowing both above fields]
```

Quality bar: "defended-artifact: data stability" is a category and fails this phase.
"defended-artifact: the schema contract table used by all downstream consumers" is specific
and passes. "change-pressure: rapid change" is a generic force and fails. "change-pressure:
migration to a streaming pipeline that skips the schema contract layer" is specific and passes.

No two lens-phrases may be identical:
Collision check -> `LENS-COLLISION: [teams]. Revise one before continuing.`

```
PROFILE-COMPLETE: [n of n] teams.
  Resistance map:
    [team] -- defends: [defended-artifact] / against: [change-pressure] / lens: "[phrase]"
    ...
```

`PROFILE-GATE: resistance map confirmed. [n] profiles. Proceeding to CONTRACT.`

---

### PHASE 4 -- CONTRACT

**Entry condition**: PROFILE-GATE. **No files written during this phase.**
**Contract artifacts are assembled from the resistance map, not constructed independently.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n]. Contract target: [n] role files.`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

Write exactly 2-3 sentences. Sentence 1: largest area by headcount as percentage of total.
Sentence 2: dominant level label, or note its absence. Sentence 3: structural observation
the table rows alone do not convey. Reference specific area names, counts, and findings.
No generic summaries.

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

### PHASE 5 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite.
        TRANSCRIPTION-RECEIPT audits compliance at org-chart.md write time.
        After any REVISED-triggered rewrite, TRANSCRIPTION-CLEAR re-audits all three
        artifacts in one named pass. CHART-WRITTEN gates on TRANSCRIPTION-CLEAR.
        If all artifacts are VERBATIM on first receipt, CHART-WRITTEN follows directly.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: CONTRACT-GATE.
**All Inertia Advocate files are written from the resistance map -- before any standard
or specialized role files. Each IA file is a portrait of a specific kind of person, not
a filled-in template.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

For each team, write from Phase 3 profile:
- **orientation**: names the specific `defended-artifact` as a concrete concern.
  The orientation reads as what this particular person watches for, not what any
  IA watches for in general.
- **lens**: opens verbatim with the lens-phrase from Phase 3. Expands in 2-3 sentences
  describing the specific tension -- the specific artifact at risk and the specific
  pressure that threatens it. No generic resistance language. No phrases applicable to
  any team. Strong: "The nightly reconciliation job has prevented three data consistency
  incidents in the past year by catching upstream drift before it reaches downstream
  consumers. A streaming migration that routes around this job removes the only
  catch point." Weak: "Ensures stability during rapid change."
- **expertise**: names the `defended-artifact` specifically. Differs word-for-word
  from every other team's IA expertise body text.
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart by role name.

No two IA files share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  lens opens with profile lens-phrase verbatim: YES / NO
  lens is team-specific (non-transplantable): YES / NO
  expertise names specific defended-artifact: YES / NO
```
Any NO -> rewrite that field before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams. Resistance portraits written from profiles.`

---

### PHASE 7 -- WRITE-CHART

**Entry condition**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs from org.yaml]
   ```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1-lock: "[verbatim]"
    org-chart.md sentence 1:  "[verbatim]"
    verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
```

If all three verdicts are VERBATIM: `CHART-WRITTEN.`

If any verdict is REVISED:
1. Rewrite that section from the sealed CONTRACT artifact.
2. Update the receipt line to corrected values and VERBATIM.
3. After all rewrites, emit TRANSCRIPTION-CLEAR -- one pass over all three artifacts,
   not only the ones that changed:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

If TRANSCRIPTION-CLEAR shows any REVISED: return to step 1 for that artifact.
`CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
Paths: `.craft/roles/{area-slug}/{role-slug}.md`, `.craft/roles/{group-slug}/{role-slug}.md`,
`.craft/roles/exec-office/{role-slug}.md`

All five fields (orientation, lens, expertise, scope, collaboration pattern).
No placeholder text. Scope explicit.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

**SINGLE-PURPOSE GATE**
This phase confirms that every IA lens field opens with the exact lens-phrase from Phase 3.
One output per team: VERBATIM or DRIFT. Nothing else inside this phase.

```
BUILD-VERIFY: [team name]
  Phase 3 lens-phrase:    "[phrase]"
  IA lens field opening:  "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM
before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. Resistance portrait lens-phrases confirmed verbatim.`
`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:  teams [n], IA files [n] -- MATCH / MISMATCH
  dir check: areas in org.yaml [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4)
  resistance map: [n of n] teams (specific artifact + specific pressure + lens-phrase)
  contract:      SEALED from resistance map (headcount=[n], prose=[n] sentences, levels=[n])
  IA portraits:  [n of n] teams -- team-specific, written from profiles, before std/spec
  org-chart.md:  [all VERBATIM / post-rewrite TRANSCRIPTION-CLEAR -- all three artifacts]
  role files:    [n] written / [n] declared
  build-verify:  PASS ([n of n] lens-phrase verdicts -- single-purpose, no other outputs)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-05 -- Full integration: all 13 aspirational criteria C-09 through C-21

**Axis**: Full integration
**Hypothesis**: V-01 through V-04 each advance one or two mechanisms in isolation.
The complete architecture integrates all 13 aspirational criteria such that each
criterion's mechanism is structurally enforced. C-21 slots into WRITE-CHART without
displacing C-19's exit-guard structure: TRANSCRIPTION-RECEIPT identifies REVISED verdicts,
rewrites execute, TRANSCRIPTION-CLEAR re-audits all three artifacts (satisfying C-21),
and CHART-WRITTEN gates on the named block. The all-VERBATIM exemption is explicit.
BUILD-VERIFY retains its single-purpose isolation (C-20). C-09 through C-16 are
satisfied by PROFILE and WRITE-IA phases. C-17 and C-20 are satisfied by BUILD-VERIFY's
structure. C-18 and C-19 are satisfied by TRANSCRIPTION-RECEIPT plus TRANSCRIPTION-CLEAR.
C-21 is satisfied by TRANSCRIPTION-CLEAR covering all three artifacts in one named pass.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**:
PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF

Each gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  nesting depth: [n]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry condition**: PARSE-PASS.
**No files written during this phase.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared
        PASS / FAIL -- teams with no roles: [list]
  [V-2] no role name in both standard and specialized for the same team
        PASS / FAIL -- collisions: [team.role list]
  [V-3] no duplicate team names across groups
        PASS / FAIL -- duplicates: [list]
  [V-4] level vocabulary uses one consistent label convention
        PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. No files written. Proceeding to CONTRACT.`
or `VALIDATE-FAIL: [n] error(s). No files written. Halt.`

---

### PHASE 3 -- CONTRACT

**Entry condition**: VALIDATE-PASS.
**No files written during this phase.**
**This phase produces the sealed build contract. Three artifacts. They are the exclusive
source for org-chart.md sections 2-4. They are not regenerated at write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

One row per area. Headcount = count of all role slots. Total = sum of all area rows.

`TABLE-CLOSED: [n] area rows, headcount total = [n]. File generation must produce
exactly [n] .craft/roles/ files.`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

Write exactly 2-3 sentences:
- Sentence 1: name the largest area by headcount and express as percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: a structural observation the table rows alone do not convey

Strong example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml, suggesting the org has not yet leveled its management layer. The three product
> teams each carry two specialized roles, a higher ratio than any infrastructure team."

Weak example (do not produce this):
> "The org has several teams with different headcount. Level distribution is shown below."

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence:**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One sentence on seniority profile referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

### PHASE 4 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: headcount table, [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B: analytic prose, [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: level distribution, [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite. No reformatting.
        Enforcement: TRANSCRIPTION-RECEIPT at org-chart.md write time.
        After any REVISED-triggered rewrite, TRANSCRIPTION-CLEAR re-audits all three
        artifacts in one named pass before CHART-WRITTEN.
        If all artifacts are VERBATIM on first receipt, CHART-WRITTEN follows directly
        and no TRANSCRIPTION-CLEAR block is required.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry condition**: CONTRACT-GATE.
**No files written during this phase.**

For each team in the headcount table, extract a resistance profile. A resistance profile
names the specific thing this team's IA would defend, the specific initiative threatening
it, and derives a lens phrase from those two. Generic profiles fail this phase.

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure owned
                      by this team -- a named thing, not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening
                      the defended-artifact -- a named initiative, not a generic force]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      the exact verbatim opening of this team's IA lens field;
                      cannot be produced without knowing both other fields]
```

After all teams:

```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: any two identical or near-identical lens phrases ->
`LENS-COLLISION: [teams]. Revise one before continuing.`

`PROFILE-GATE: [n] distinct profiles confirmed. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: PROFILE-GATE.
**All Inertia Advocate files are written in this phase -- before any standard or
specialized role files. IA omission is structurally impossible: an unstarted IA file
means the team's entire role set has not begun.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

For each team, write from the resistance profile. The IA file is a person-portrait --
not a filled-in template. It describes the specific kind of person who would occupy
this role on this team:

- **orientation**: names the specific concern derived from `defended-artifact`. Not
  a generic caution. Reads as the specific thing this person watches for.
- **lens**: opens verbatim with the `lens-phrase` from Phase 5. Expands in 2-3 sentences.
  No phrase applicable to any team. Describes a specific viewpoint anchored to this
  team's domain -- the specific tension between the defended artifact and the change
  pressure. Strong: "The schema contract table cannot be rewritten by a migration tool
  that lacks a dry-run mode. Three prior migrations that skipped dry-run introduced
  schema drift that cost a full sprint to reconcile." Weak: "Ensures data stability
  during change."
- **expertise**: anchored to the specific `defended-artifact` by name. Not a category.
  Differs from every other team's IA expertise body text.
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: names forums and cadence. Names the primary counterpart --
  the role most likely to propose the initiative described in `change-pressure`.

No two IA files share identical `lens` or `expertise` body text.

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 5]"
  opens verbatim: YES / NO
  lens is team-specific (non-transplantable): YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite that field before proceeding to next team.

`IA-PHASE-COMPLETE: [n of n] teams covered. IA files written before standard/specialized.`

---

### PHASE 7 -- WRITE-ROLES

**Entry condition**: IA-PHASE-COMPLETE.

Standard, specialized, shared group, and exec office role files.
Paths: `.craft/roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.craft/roles/{group-slug}/{role-slug}.md` (shared group),
`.craft/roles/exec-office/{role-slug}.md` (exec office)

All five fields required for every file (orientation, lens, expertise, scope,
collaboration pattern). No placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`

`ROLES-COMPLETE: [n] files written.`

---

### PHASE 8 -- WRITE-CHART

**Entry condition**: ROLES-COMPLETE.

Write org-chart.md. Sections in order:

1. **ASCII hierarchy** -- box-drawing characters, minimum two nesting levels.
   Group names match org.yaml exactly. Team leaf nodes show headcount in parentheses.

2. **[TRANSCRIBE CONTRACT ARTIFACT-A verbatim]**
   Do not recalculate. Do not reformat. Copy the sealed artifact from Phase 3.

3. **[TRANSCRIBE CONTRACT ARTIFACT-B verbatim]**
   The same sentences. Not a rewrite or paraphrase. Copy the sealed artifact from Phase 3.

4. **[TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]**
   Copy the sealed artifact from Phase 3.

5. **AMEND section:**
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list from org.yaml]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs from org.yaml]
   ```

**After writing org-chart.md, emit TRANSCRIPTION-RECEIPT immediately:**

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1-lock: "[phrase]"
    org-chart.md sentence 1:  "[phrase]"
    verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    verdict: VERBATIM / REVISED
```

**Exit logic:**

If all three verdicts are VERBATIM on first receipt:
`CHART-WRITTEN.`
(No TRANSCRIPTION-CLEAR required -- no rewrites occurred.)

If one or more verdicts are REVISED:
1. For each REVISED artifact: rewrite that section of org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line to corrected values and VERBATIM.
2. After all rewrites are complete, emit TRANSCRIPTION-CLEAR:
   This named block re-audits every contract artifact in a single pass -- including
   those that were already VERBATIM before any rewrite. The block must list all three.
   A block that names fewer than three artifacts does not satisfy the exit gate.

   ```
   TRANSCRIPTION-CLEAR:
     ARTIFACT-A: VERBATIM
     ARTIFACT-B: VERBATIM
     ARTIFACT-C: VERBATIM
     all three confirmed -- CHART-WRITTEN authorized
   ```

   If any artifact in TRANSCRIPTION-CLEAR shows REVISED: return to step 1 for that
   artifact. The phase cannot close until TRANSCRIPTION-CLEAR lists all three as VERBATIM.
   `CHART-WRITTEN.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: CHART-WRITTEN.

**SINGLE-PURPOSE GATE -- read before emitting any output for this phase:**
This phase has exactly one responsibility: confirm that every Inertia Advocate role
file's lens field opens with the exact lens-phrase derived in Phase 5.
This phase produces exactly one output per team: a VERBATIM or DRIFT verdict.
This phase contains NO file writes, NO structural file-count checks, NO directory
comparisons, NO headcount verifications, NO AMEND generation, NO summary rows,
and NO other outputs of any kind.
Any content in this phase beyond per-team VERBATIM/DRIFT verdicts is a build error.

For each team -- emit exactly:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 5]"
  IA lens field opening:  "[exact first phrase in written .craft/roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

After all teams:

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 5 profiles.
Phase produced [n] VERBATIM/DRIFT verdicts and no other outputs. Derivation loop closed.`

`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots:   [n], files written: [n] -- MATCH / MISMATCH
  if MISMATCH: missing: [list]

  IA files:         teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:        areas in org.yaml [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity:   CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`
Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4 checks) -- no files written before validation
  contract:      SEALED (headcount=[n], analytic prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams (specific artifact + specific pressure + lens-phrase)
  IA coverage:   [n of n] teams -- portraits written before standard/specialized (C-12)
  IA quality:    portraits (specific lens + concrete expertise -- C-15); from profiles (C-16)
  org-chart.md:  [all VERBATIM first pass -- CHART-WRITTEN directly |
                  post-rewrite TRANSCRIPTION-CLEAR -- all 3 artifacts confirmed (C-21)]
  role files:    [n] written / [n] declared (C-01, C-04, C-05, C-07)
  build-verify:  PASS ([n of n] verdicts; single-purpose phase, no other outputs -- C-17/C-20)
  cross-ref:     PASS / FAIL (C-10)
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## Variation Summary

| Var | Axis | New Criterion Targeted | Key Mechanism |
|-----|------|------------------------|---------------|
| V-01 | Lifecycle emphasis | C-21 | Two exit paths from TRANSCRIPTION-RECEIPT; PATH-B requires TRANSCRIPTION-CLEAR enumerating all three artifacts; exemption explicit for PATH-A |
| V-02 | Output format | C-21 | PATH-A / PATH-B labeled as named mutually exclusive paths; PATH-B's TRANSCRIPTION-CLEAR is mandatory and visibly distinct from PATH-A's direct CHART-WRITTEN |
| V-03 | Phrasing register | C-19, C-20, C-21 (deferred R5 axis) | Declarative output shapes for all 13 aspirational criteria; Shape A vs Shape B for TRANSCRIPTION; BUILD-VERIFY block described as containing exactly N lines |
| V-04 | Lifecycle + Inertia framing | C-21, C-15, C-16 | Resistance profiles extracted before CONTRACT; profiles as structural anchor; TRANSCRIPTION-CLEAR integrated as architectural consequence |
| V-05 | Full integration | C-09 through C-21 | Complete architecture; C-21 satisfies via TRANSCRIPTION-CLEAR listing all three after any rewrite; all-VERBATIM exemption explicit; BUILD-VERIFY retains single-purpose isolation |

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 IA contextualized | + | + | ++ | + | ++ |
| C-10 Cross-ref integrity | + | + | + | + | + |
| C-11 Pre-write validation | + | + | + | + | + |
| C-12 IA-first ordering | + | + | + | + | ++ |
| C-13 Headcount as contract | + | + | + | + | ++ |
| C-14 Analytic narrative prose | + | + | ++ | + | ++ |
| C-15 IA as person-portrait | + | + | ++ | ++ | ++ |
| C-16 Resistance profile pre-IA | + | + | ++ | ++ | ++ |
| C-17 CROSS-REF lens-phrase verification | + | + | ++ | + | ++ |
| C-18 Contract verbatim transcription | + | ++ | ++ | ++ | ++ |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | ++ | ++ | ++ | ++ | ++ |
| C-20 BUILD-VERIFY single-purpose phase | ++ | ++ | ++ | ++ | ++ |
| C-21 TRANSCRIPTION-CLEAR re-audit gate | ++ | ++ | ++ | ++ | ++ |
