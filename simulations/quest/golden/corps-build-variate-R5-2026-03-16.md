---
skill: quest-variate
skill_target: corps-build
round: 5
date: 2026-03-16
rubric_version: 5
---

# Variate R5 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v5 adds C-19 and C-20. R4 V-01 (97 pts) and R4 V-02 (99 pts) contained early forms of both; R5 targets the remaining gaps.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis: BUILD-VERIFY as truly single-purpose phase (C-20) | V-01 |
| Output format: TRANSCRIPTION-RECEIPT with phase-exit guard (C-19) | V-02 |
| Phrasing register: declarative output-forward framing for C-19 and C-20 | V-03 |
| Lifecycle + Output format: C-19 + C-20 together | V-04 |
| Full integration: all 12 aspirational criteria C-09 through C-20 | V-05 |

---

## R4 Gap Analysis (rubric v5 lens)

| New Criterion | Best R4 Coverage | Gap |
|---------------|-----------------|-----|
| C-20 BUILD-VERIFY single-purpose phase | R4 V-01: named BUILD-VERIFY phase with single stated purpose and VERBATIM/DRIFT binary per team; scored 97 | C-20 requires a SINGLE-PURPOSE DECLARATION at phase entry and a structural prohibition on all non-verdict content inside the phase block. R4 V-01 described the purpose correctly but did not assert it as a constraint -- the phase could accumulate adjacent checks. C-20 fails if the phase contains anything beyond one VERBATIM/DRIFT verdict per team. |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | R4 V-02: CONTRACT-SEAL + TRANSCRIPTION-RECEIPT with VERBATIM/REVISED per artifact and "Any REVISED -> rewrite"; scored 99 | C-19 requires a PHASE-EXIT GUARD that re-audits all verdicts after any rewrite and refuses to emit CHART-WRITTEN until all show VERBATIM. R4 V-02 instructed rewrite but did not close the loop with an explicit gate that confirms the phase cannot exit in REVISED state. A model can comply with the R4 instruction by noting the rewrite and then continuing; C-19 prevents that. |

Both C-19 and C-20 were structurally anticipated by R4. The gap is enforcement depth: R4 named the mechanisms; R5 adds explicit entry constraints (C-20) and exit guards (C-19) that make non-compliance structurally visible.

---

## V-01 -- Lifecycle: BUILD-VERIFY as single-purpose phase (C-20)

Hypothesis: R4 V-01 had BUILD-VERIFY with a stated purpose and binary verdicts. C-20 fails when the phase accumulates non-verdict content (structural file-count checks, CROSS-REF subitems, summary rows) alongside the IA lens verdicts. The fix is a SINGLE-PURPOSE GATE declaration at phase entry that names exactly what the phase contains (one VERBATIM/DRIFT verdict per team and nothing else) and an explicit structural rule that any other content inside the BUILD-VERIFY block is a build error.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use
the provided path.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA ->
WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF. Each gate must appear in output
before the next phase begins.

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
  [V-1] every team has >= 1 role declared        PASS / FAIL -- teams with no roles: [list]
  [V-2] no role name in both standard and specialized for the same team
        PASS / FAIL -- collisions: [team.role list]
  [V-3] no duplicate team names across groups    PASS / FAIL -- duplicates: [list]
  [V-4] level vocabulary uses one consistent label convention
        PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. Proceeding to CONTRACT.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 -- CONTRACT

**Entry condition**: VALIDATE-PASS.
**No files written during this phase.**
**This phase produces three contract artifacts. They are sealed in Phase 4 and transcribed
verbatim into org-chart.md in Phase 7. They are not regenerated at write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules: one row per area; headcount = count of all role slots for that area; Total = sum
of all area rows.

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

Write exactly 2-3 sentences interpreting the numbers:
- Sentence 1: name the largest area by headcount and express as percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: a structural observation the table rows alone do not convey

Strong (produce this):
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml, suggesting the org has not yet leveled its management layer. The three product
> teams each carry two specialized roles, a higher ratio than any infrastructure team."

Weak (do not produce this):
> "The org has several teams with different headcount. Level distribution is shown below."

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence:**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One sentence on seniority profile after the table.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels). Proceeding to seal.`

---

### PHASE 4 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

Emit this block:

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
        Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 7.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry condition**: CONTRACT-GATE.
**No files written during this phase.**

For every team, extract:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening it]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [list, one per line, team: "phrase"]`

Collision check: any identical lens phrases -> `LENS-COLLISION: [teams]. Revise one before continuing.`

`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: PROFILE-GATE.

Write all Inertia Advocate files before any standard or specialized role files.
Path: `.roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:
- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; expands in 2-3 sentences;
  no generic stability language; no boilerplate applicable to any team
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart (role most likely to
  propose the change-pressure initiative)

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

Any REVISED -> rewrite that section from the sealed artifact. Reemit that receipt line showing VERBATIM before proceeding.
`TRANSCRIPTION-PASS: all artifacts VERBATIM. CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
Paths: `.roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.roles/{group-slug}/{role-slug}.md` (shared group),
`.roles/exec-office/{role-slug}.md` (exec office)

All five fields, no placeholder text. Scope field explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`

`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

**SINGLE-PURPOSE GATE**
This phase has exactly one responsibility: confirm that every Inertia Advocate role file's
lens field opens with the exact lens-phrase derived in Phase 5.
This phase produces exactly one output per team: a VERBATIM or DRIFT verdict.
This phase contains NO file writes, NO structural file-count checks, NO directory
comparisons, NO headcount verifications, NO AMEND generation, and NO summary rows.
Any content beyond per-team VERBATIM/DRIFT verdicts inside this phase block is a build error.

For each team, emit exactly:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 5]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: `[file opening] does not match [profile phrase]. Rewrite IA lens field to open
with profile phrase verbatim before continuing to next team.`

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
  org-chart.md:  written (transcription: all VERBATIM)
  role files:    [n] written / [n] declared
  build-verify:  PASS (single-purpose: [n of n] IA lens verdicts only)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-02 -- Output format: TRANSCRIPTION-RECEIPT with phase-exit guard (C-19)

Hypothesis: R4 V-02 had TRANSCRIPTION-RECEIPT with VERBATIM/REVISED per artifact and "Any REVISED -> rewrite that section." C-19 fails when a model can note the REVISED verdict and the rewrite instruction, and then continue to CHART-WRITTEN without actually re-auditing all verdicts. The gap is a PHASE-EXIT GUARD -- a named step between any rewrite and CHART-WRITTEN that re-emits every receipt line and confirms all show VERBATIM before the phase can close. Without the exit guard, the phase is self-reporting but not self-correcting. The exit guard is the structural element that makes CHART-WRITTEN contingent on the VERBATIM state of every receipt.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE ->
BUILD-VERIFY -> CROSS-REF. Each gate must appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

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

### PHASE 2 -- VALIDATE

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec collision per team          PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names                 PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary             PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. Proceeding to CONTRACT.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

---

### PHASE 3 -- CONTRACT

**Entry**: VALIDATE-PASS.
**No files written during this phase.**
**This phase produces the sealed contract. Three artifacts. They are the source for
org-chart.md sections 2-4. They are not rewritten at org-chart.md write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**
- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note its absence
- Sentence 3: structural observation the table rows alone do not convey

No generic summaries. Name specific areas, counts, and findings.

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One sentence on seniority profile.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

### PHASE 4 -- CONTRACT-SEAL

**Entry**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: headcount table, [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B: analytic prose, [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: level distribution, [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 ARE these artifacts.
        Any revision between CONTRACT-SEAL and CHART-WRITTEN is a build failure.
        Compliance is enforced via TRANSCRIPTION-RECEIPT in Phase 6b.
        TRANSCRIPTION-RECEIPT must confirm all artifacts VERBATIM before CHART-WRITTEN.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry**: CONTRACT-GATE. **No files written.**

For each team in the headcount table:

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

`PROFILE-GATE: profiles confirmed. Proceeding to WRITE.`

---

### PHASE 6 -- WRITE

**Entry**: PROFILE-GATE.

**6a -- Inertia Advocate files (all teams, before any other role files)**

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; 2-3 sentences; no generic stability language
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart

After each file:
```
IA-WRITTEN: [team]
  lens-phrase from profile: "[phrase]"
  opens verbatim: YES / NO
```
Any NO -> rewrite lens before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams.`

---

**6b -- org-chart.md**

Write org-chart.md. Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels.

2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim]

3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim]

4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]

5. AMEND section:
   ```
   ## AMEND
   1. --area "[name]" -- regenerate area. Available: [list]
   2. --levels "[old]:[new]" -- replace levels. In use: [list]
   3. --restructure "[team] > [new-parent]" -- move team. Current: [parent > child pairs]
   ```

**TRANSCRIPTION-RECEIPT** -- emit this block immediately after writing org-chart.md,
before any further output:

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

**For each REVISED verdict:**
1. Rewrite that section of org-chart.md from the sealed CONTRACT artifact.
2. Update that receipt line to show the corrected values.
3. Change the verdict to VERBATIM.

**PHASE-EXIT GUARD** -- this step runs after any rewrites:
Before emitting CHART-WRITTEN, re-audit all three receipt verdicts.
If any verdict is not VERBATIM, return to step 1 above for that artifact.
The phase cannot close until all three receipt lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- phase exit authorized
```

`CHART-WRITTEN.`

---

**6c -- Standard, specialized, shared group, and exec office role files**

All five fields. No placeholder text. Scope explicit.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`

`ROLES-COMPLETE: [n] files written.`

---

### PHASE 7 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.
**Purpose**: Confirm each IA lens field opens with the exact lens-phrase from Phase 5.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 5]"
  IA lens field opening:  "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens to open with profile phrase verbatim. Reemit that BUILD-VERIFY
block showing VERBATIM before proceeding.

`BUILD-VERIFY-PASS: [n of n] IA lens phrases confirmed verbatim.`
or `BUILD-VERIFY-FAIL: [n] mismatch(es): [team names].`

`BUILD-VERIFY-COMPLETE.`

---

### PHASE 8 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:      areas [list], dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4)
  contract:      SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams
  IA phase:      [n of n] teams written before standard/specialized
  transcription: CLEAR -- all three artifacts VERBATIM at phase exit
  role files:    [n] written / [n] declared
  build-verify:  PASS -- [n of n] IA lens phrases confirmed
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-03 -- Phrasing register: declarative output-forward framing for C-19 and C-20

Hypothesis: Imperative instructions describe what to do; declarative framing describes what correct output looks like. For C-20, framing the single-purpose constraint as "The BUILD-VERIFY block contains exactly N lines: one VERBATIM/DRIFT verdict per team. It contains nothing else." makes it a shape constraint on the output rather than a behavioral instruction. For C-19, framing the phase-exit guard as "CHART-WRITTEN appears only after TRANSCRIPTION-CLEAR, which lists all three artifacts as VERBATIM" makes the gate a required output shape rather than a conditional instruction. These shapes are harder to elide because the model sees what correct output looks like.

```
You are running `corps-build`. Read org.yaml in the working directory, or use the path provided.

`corps-build` produces two artifacts: **org-chart.md** and **.roles/ files**.
What follows describes what correct output looks like at each stage. The descriptions
at Stage 8 (BUILD-VERIFY shape) and Stage 6b (TRANSCRIPTION-CLEAR gate) are the
defining structural properties of a correct build.

---

### Stage 1 -- Parse

Read org.yaml. A correct parse block looks like this:

```
PARSE: [org name], [n] teams, [n] role slots, nesting depth [n].
```

If malformed: `PARSE-FAIL: [description]. Halt.`

---

### Stage 2 -- Validate

Before writing anything, check four conditions: every team has at least one declared role;
no role name appears in both standard and specialized for the same team; no two teams share
a name; level vocabulary is consistent. If any problem is found, list it and halt.
If none: `VALIDATE: no structural anomalies. [n] teams, [n] slots confirmed.`

---

### Stage 3 -- Build contract

Before any file is written, three contract artifacts are produced. A correct contract block:

```
CONTRACT-DRAFT:
  ARTIFACT-A (headcount table, [n] area rows, total=[n])
  ARTIFACT-B (analytic prose, [n] sentences)
  ARTIFACT-C (level distribution, [n] rows, total=[n])
```

A correct ARTIFACT-B analytic prose example:
> "Data Engineering carries 11 of 28 total headcount -- the largest area at 39%. Six of
> eight Data Engineering teams declare IC levels; two carry no level vocabulary. The two
> real-time processing teams carry more specialized roles per headcount than any batch
> processing team -- three specialized versus one or two."

A weak ARTIFACT-B (do not produce this):
> "The organization has several teams. Level distribution is shown below."

---

### Stage 4 -- CONTRACT-SEAL

Correct seal output:

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total=[n]; first-row lock: "[area] | [n]"
  ARTIFACT-B: [n] sentences; sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] rows, total=[n]
  RULE: org-chart.md sections 2-4 are copies of these artifacts.
        No recalculation. No rewrite. Any drift is caught by TRANSCRIPTION-RECEIPT
        and corrected before TRANSCRIPTION-CLEAR authorizes CHART-WRITTEN.
```

`CONTRACT-GATE: [n] files to produce.`

---

### Stage 5 -- Resistance profiles

Before any IA file is written, a resistance profile for each team. A correct profile:

```
PROFILE: [team name]
  defended-artifact:  [named thing this team owns -- not a category]
  change-pressure:    [named initiative threatening it -- not a generic force]
  lens-phrase:        "[5-10 words that compress the specific tension; verbatim
                      opening of this team's IA lens field]"
```

A correct lens-phrase cannot be produced without knowing both defended-artifact and
change-pressure. It is not a category description. It is the exact words that open
the IA file's lens field.

After all profiles:
```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

`PROFILE-GATE: profiles confirmed.`

---

### Stage 6 -- Write IA files

All IA files before any standard or specialized role files.
Path: `.roles/{area-slug}/inertia-advocate.md`

A correctly produced IA file: lens opens with the resistance profile lens-phrase verbatim.
Expertise names the specific defended-artifact. The file cannot be used for a different
team without substantive rewrite.

After each file:
```
IA-WRITTEN: [team]
  lens opens with profile lens-phrase: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite that field before continuing.

`IA-COMPLETE: [n of n] teams.`

---

### Stage 7 -- Write standard and specialized role files

All five fields. No placeholder text. Scope explicit.
After each team: `TEAM-COMPLETE: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### Stage 6b -- Write org-chart.md and confirm transcription

**What correct org-chart.md write output looks like:**

org-chart.md has five sections: ASCII hierarchy, headcount table, analytic prose,
level distribution, AMEND.

Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content, not a rewrite.

A correct TRANSCRIPTION-RECEIPT immediately follows org-chart.md write:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total: [n]
    org-chart.md total: [n]
    verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1-lock: "[phrase]"
    org-chart.md sentence 1:  "[phrase]"
    verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total: [n]
    org-chart.md total: [n]
    verdict: VERBATIM / REVISED
```

If any verdict is REVISED: rewrite that section from the sealed CONTRACT artifact.
Update that receipt line to VERBATIM. A correct build does not advance until all
three verdicts show VERBATIM.

**A correct TRANSCRIPTION-CLEAR block:**
This block appears after all receipts show VERBATIM. CHART-WRITTEN appears only after
TRANSCRIPTION-CLEAR. A build that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is
structurally invalid.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

`CHART-WRITTEN.`

---

### Stage 8 -- BUILD-VERIFY

**What a correct BUILD-VERIFY block looks like:**

The BUILD-VERIFY block runs after all role files are written and before CROSS-REF.
It contains exactly N lines, where N is the number of teams. Each line is one VERBATIM
or DRIFT verdict. The block contains nothing else: no file-count checks, no directory
checks, no headcount verifications, no summary rows, no other outputs.

A correct BUILD-VERIFY block for a 4-team org:

```
BUILD-VERIFY: [Team A] -- VERBATIM
BUILD-VERIFY: [Team B] -- VERBATIM
BUILD-VERIFY: [Team C] -- VERBATIM
BUILD-VERIFY: [Team D] -- VERBATIM
```

Or expanded if verification is needed:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:   "[phrase]"
  IA lens field opening: "[actual first phrase]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens to open with profile phrase verbatim. Reemit that line as
VERBATIM before proceeding to next team.

After all teams: `BUILD-VERIFY-PASS: [n of n] verdicts VERBATIM.`
`BUILD-VERIFY-COMPLETE.`

---

### Stage 9 -- Cross-reference

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       [n of n] teams -- MATCH / MISMATCH
  table fidelity: CONTRACT [n] == org-chart.md [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**CORPS-BUILD -- {date}**

```
  parse:          [org name], [n] teams
  validate:       PASS -- no anomalies
  contract:       SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:       [n of n] teams
  IA files:       [n of n] -- portraits written from profiles
  standard roles: [n], specialized roles: [n]
  org-chart.md:   TRANSCRIPTION-CLEAR (all VERBATIM at exit)
  build-verify:   [n of n] VERBATIM verdicts (block contained nothing else)
  cross-ref:      PASS / FAIL
  status:         COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-04 -- Combination: C-19 + C-20 together

Axis: Lifecycle + Output format combination
Hypothesis: C-19 and C-20 are mechanically independent -- one governs the transcription
phase exit condition, the other governs the post-write verification phase structure.
A prompt that integrates both into a named pipeline -- TRANSCRIPTION-CLEAR closes C-19
before CHART-WRITTEN; BUILD-VERIFY is isolated from CROSS-REF by a single-purpose
declaration -- produces both without redundancy. The key is that the two mechanisms
address different phases: C-19 governs Phase 6b (chart write); C-20 governs Phase 9
(post-write IA lens verification). They do not interact; they compose.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

Execute steps in order. Each gate must appear in output before the next step begins.

**Step sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-ROLES -> WRITE-CHART -> BUILD-VERIFY -> CROSS-REF

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

`PARSE-PASS.` or `PARSE-ERROR: [description]. Halt.`

---

**STEP 2 -- VALIDATE**

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL
  [V-2] no std/spec name collision per team    PASS / FAIL
  [V-3] no duplicate team names               PASS / FAIL
  [V-4] consistent level vocabulary            PASS / FAIL
```

`VALIDATE-PASS: 4/4. Proceeding.`
or `VALIDATE-FAIL: [errors]. No files written. Halt.`

---

**STEP 3 -- CONTRACT**

**Entry**: VALIDATE-PASS. **No files written during this step.**

Produce three contract artifacts:

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

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

**STEP 4 -- CONTRACT-SEAL**

Seal the three artifacts. After this step, the contract cannot be revised.

```
CONTRACT-SEALED:
  ARTIFACT-A: headcount table, [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B: analytic prose, [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: level distribution, [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C.
        Any revision is a build failure.
        Enforcement: TRANSCRIPTION-RECEIPT + TRANSCRIPTION-CLEAR in STEP 7.
        CHART-WRITTEN cannot be emitted before TRANSCRIPTION-CLEAR.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce.`

---

**STEP 5 -- PROFILE**

**Entry**: CONTRACT-GATE. **No files written.**

For each team in the headcount table:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; cannot be written without knowing
                      both fields; opens IA lens field verbatim]
```

```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: `LENS-COLLISION: [teams]. Revise.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed.`

---

**STEP 6 -- WRITE-IA**

**Entry**: PROFILE-GATE.

Write all Inertia Advocate files before any standard or specialized role files.
Path: `.roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:
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
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim]
5. AMEND section (--area, --levels, --restructure with specific values from org.yaml)

After writing, emit TRANSCRIPTION-RECEIPT:

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

For each REVISED verdict:
1. Rewrite that section from the sealed CONTRACT artifact.
2. Update that receipt line to show corrected values and change verdict to VERBATIM.

PHASE-EXIT GUARD: After all rewrites, re-audit all three receipt verdicts.
The phase cannot close until all show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

`CHART-WRITTEN.`

---

**STEP 8 -- WRITE-ROLES**

**Entry**: CHART-WRITTEN.

Standard, specialized, shared group, exec office role files. All five fields. Scope explicit.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

**STEP 9 -- BUILD-VERIFY**

**Entry**: ROLES-COMPLETE.

**SINGLE-PURPOSE GATE**
This step has exactly one responsibility: confirm each IA lens field opens with the
exact lens-phrase from Step 5. This step produces exactly one output per team: a
VERBATIM or DRIFT verdict. This step contains NO file writes, NO structural checks,
NO directory comparisons, NO headcount verifications, and NO summary rows.
Any content beyond per-team VERBATIM/DRIFT verdicts is a build error.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 5]"
  IA lens field opening:  "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens to open with profile phrase verbatim. Reemit that team's
BUILD-VERIFY block showing VERBATIM before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Step 5 profiles.
Phase contained [n] VERBATIM/DRIFT verdicts and no other outputs.`

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
  transcription: CLEAR (all three artifacts VERBATIM at phase exit -- C-19 satisfied)
  role files:    [n] written / [n] declared
  build-verify:  PASS ([n of n] verdicts; single-purpose phase, no other outputs -- C-20 satisfied)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-05 -- Full integration: all 12 aspirational criteria C-09 through C-20

Axis: Full integration
Hypothesis: V-01 through V-04 each advance one or two mechanisms in isolation. The complete architecture integrates all 12 aspirational criteria such that each criterion's mechanism is structurally enforced rather than merely requested. The v5 additions (C-19 phase-exit guard, C-20 single-purpose gate) slot into the pipeline without displacing C-17's BUILD-VERIFY derivation loop or C-18's CONTRACT-SEAL verbatim chain. The full architecture is: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE-IA -> WRITE-ROLES -> WRITE-CHART (with TRANSCRIPTION-RECEIPT + TRANSCRIPTION-CLEAR) -> BUILD-VERIFY (single-purpose) -> CROSS-REF. Criteria C-09 through C-16 are satisfied by the intermediate phases; C-17 and C-20 are satisfied by BUILD-VERIFY's structure; C-18 and C-19 are satisfied by TRANSCRIPTION-RECEIPT + TRANSCRIPTION-CLEAR's exit gate.

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

**Entry condition**: PARSE-PASS. **No files written.**

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
exactly [n] .roles/ files.`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

Write exactly 2-3 sentences:
- Sentence 1: name the largest area by headcount and express as percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: a structural observation the table rows alone do not convey

Strong example (produce this):
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

**Entry**: CONTRACT-DRAFT.

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
        TRANSCRIPTION-CLEAR (all three artifacts VERBATIM) required before CHART-WRITTEN.
        CHART-WRITTEN cannot be emitted before TRANSCRIPTION-CLEAR.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry**: CONTRACT-GATE. **No files written during this phase.**

For each team in the headcount table, extract a resistance profile. A resistance profile
names the specific thing this team's IA would defend, the specific initiative threatening
it, and derives a lens phrase from those two. Generic profiles (e.g., "defends stability
against change") fail this phase.

For each team:

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
specialized role files.**
**IA omission is structurally impossible: an unstarted IA file means the team's
entire role set has not begun.**

Path: `.roles/{area-slug}/inertia-advocate.md`

For each team, write from the resistance profile:

- **orientation**: names the specific concern derived from `defended-artifact`. Not
  a generic caution applicable to any team. Reads as the specific thing this person
  watches for.
- **lens**: opens verbatim with the `lens-phrase` from Phase 5. Expands in 2-3 sentences.
  No phrase that reads as generic stability language. The lens describes a specific
  viewpoint anchored to this team's domain -- the specific tension, not the general concept.
  Strong: "The schema contract table cannot be rewritten by a migration tool that lacks
  a dry-run mode. Three prior migrations that skipped dry-run introduced schema drift
  that cost a full sprint to reconcile." Weak: "Ensures data stability during change."
- **expertise**: anchored to the specific `defended-artifact`. Names a concrete artifact,
  system, or practice this person would defend. Not a category. Differs from every other
  team's IA expertise body text.
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: names forums and cadence. Names the primary counterpart --
  the role most likely to propose the initiative described in `change-pressure`.

No two IA files share identical `lens` or `expertise` body text.

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 5]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite that field before proceeding to next team.

`IA-PHASE-COMPLETE: [n of n] teams covered. IA files written before standard/specialized.`

---

### PHASE 7 -- WRITE-ROLES

**Entry condition**: IA-PHASE-COMPLETE.

Standard, specialized, shared group, and exec office role files.
Paths: `.roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.roles/{group-slug}/{role-slug}.md` (shared group),
`.roles/exec-office/{role-slug}.md` (exec office)

All five fields required for every file (orientation, lens, expertise, scope,
collaboration pattern). No placeholder text. Scope field explicit:
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
   Do not recalculate. Do not reformat. Copy from Phase 3.

3. **[TRANSCRIBE CONTRACT ARTIFACT-B verbatim]**
   The same sentences. Not a rewrite or paraphrase. Copy from Phase 3.

4. **[TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]**
   Copy from Phase 3.

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

**For each REVISED verdict:**
1. Rewrite that section of org-chart.md from the sealed CONTRACT artifact.
2. Update the receipt line to show corrected values.
3. Change the verdict to VERBATIM.

**PHASE-EXIT GUARD** -- executes after all rewrites:
Re-audit all three receipt verdicts. If any verdict is not VERBATIM, return to step 1
for that artifact. The phase cannot close until all three show VERBATIM.
Emit TRANSCRIPTION-CLEAR only when all three are confirmed:

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

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
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
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
  profiles:      [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA coverage:   [n of n] teams -- written before standard/specialized (C-12)
  IA quality:    portraits (specific lens + concrete expertise -- C-15); from profiles (C-16)
  org-chart.md:  TRANSCRIPTION-CLEAR (all 3 artifacts VERBATIM at phase exit -- C-18/C-19)
  role files:    [n] written / [n] declared (C-01, C-04, C-05, C-07)
  build-verify:  PASS ([n of n] verdicts; single-purpose phase, no other outputs -- C-17/C-20)
  cross-ref:     PASS / FAIL (C-10)
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## Variation Summary

| Var | Axis | New Criteria Targeted | Mechanism |
|-----|------|-----------------------|-----------|
| V-01 | Lifecycle: single-purpose BUILD-VERIFY | C-20 | SINGLE-PURPOSE GATE declaration at phase entry; structural prohibition on non-verdict content |
| V-02 | Output format: TRANSCRIPTION-RECEIPT with exit guard | C-19 | PHASE-EXIT GUARD + TRANSCRIPTION-CLEAR required before CHART-WRITTEN |
| V-03 | Phrasing register: declarative output-forward | C-19, C-20 | Constraints expressed as output shapes; CHART-WRITTEN appears only after TRANSCRIPTION-CLEAR; BUILD-VERIFY block contains exactly N verdict lines |
| V-04 | Lifecycle + Output format combination | C-19, C-20 | Both mechanisms integrated; TRANSCRIPTION-CLEAR in WRITE-CHART; single-purpose gate in BUILD-VERIFY |
| V-05 | Full integration: all 12 aspirational criteria | C-09 through C-20 | Complete architecture; C-19/C-20 slot in without displacing prior mechanisms |

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 IA contextualized | + | + | + | + | ++ |
| C-10 Cross-ref integrity | + | + | + | + | + |
| C-11 Pre-write validation | + | + | + | + | + |
| C-12 IA-first ordering | + | + | + | + | ++ |
| C-13 Headcount as contract | + | ++ | + | ++ | ++ |
| C-14 Analytic narrative prose | + | ++ | ++ | ++ | ++ |
| C-15 IA as person-portrait | + | + | + | + | ++ |
| C-16 Resistance profile pre-IA | + | + | + | + | ++ |
| C-17 CROSS-REF lens-phrase verification | + | + | + | ++ | ++ |
| C-18 Contract verbatim transcription | + | ++ | ++ | ++ | ++ |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | - | ++ | ++ | ++ | ++ |
| C-20 BUILD-VERIFY single-purpose phase | ++ | - | ++ | ++ | ++ |

Legend: ++ primary target, + covered, - not primary target
