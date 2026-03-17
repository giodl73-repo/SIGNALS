---
skill: quest-variate
skill_target: corps-build
round: 4
date: 2026-03-16
rubric_version: 4
---

# Variate R4 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v4 adds C-17 and C-18. R3 V-05 contained early forms of both; R4 targets them directly.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis: named BUILD-VERIFY phase as post-write IA lens gate (C-17) | V-01 |
| Output format: CONTRACT-SEAL + TRANSCRIPTION-RECEIPT for verbatim copy (C-18) | V-02 |
| Phrasing register: output-forward description of verbatim chain (C-17, C-18) | V-03 |
| Lifecycle + Output format: CONTRACT-TRANSCRIBE-VERIFY pipeline (C-17, C-18) | V-04 |
| Full integration: all ten aspirational criteria (C-09 through C-18) | V-05 |

---

## R3 Gap Analysis (rubric v4 lens)

| New Criterion | Best R3 Coverage | Gap |
|---------------|-----------------|-----|
| C-17 IA lens-phrase verification at build-complete | R3 V-05 CROSS-REF C4: "every IA lens opens with Phase 4 lens-phrase" -- embedded as one of four CROSS-REF checks | C4 is not a named post-write phase; when bundled with file-count and dir checks, the model may abbreviate it; C-17 requires a standalone named step that explicitly closes the C-16 loop as a structural invariant, not a check-in-passing |
| C-18 Contract verbatim transcription | R3 V-05 Phase 6: "transcribe verbatim" instruction for table/prose/level dist | Instruction is present but unverified; no CONTRACT-SEAL marks artifacts immutable; no TRANSCRIPTION-RECEIPT confirms the copy happened; C-18 requires the step log to show transcription as an auditable act, not merely that the result is numerically correct |

Both C-17 and C-18 were structurally anticipated by R3 V-05. The gap is verification depth: R3 had the mechanisms implied; R4 makes them named, gated, and auditable.

---

## V-01 -- Lifecycle Emphasis: Named BUILD-VERIFY Phase (C-17)

**Axis**: Lifecycle emphasis
**Hypothesis**: When IA lens-phrase verification is embedded as one of four CROSS-REF checks
(as in R3 V-05), the model may deprioritize or abbreviate it relative to the file-count
check. A dedicated BUILD-VERIFY phase that executes after all files are written -- with a
single purpose: confirm each IA lens field opens with the exact phrase from the resistance
profile -- makes C-17 pass by naming it as the primary post-write obligation. The phase gate
forces the check to run before CROSS-REF; the VERBATIM/DRIFT binary catches drift that
write-time YES/NO annotations missed. This is the minimum structural addition for C-17.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use
the provided path.

**Phase sequence**: PARSE -> VALIDATE -> WRITE -> BUILD-VERIFY -> CROSS-REF. Each gate
must appear in output before the next phase begins.

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

`VALIDATE-PASS: 4/4 checks pass. Proceeding to WRITE.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 -- WRITE

**Entry condition**: VALIDATE-PASS.

**3a -- Resistance profiles** (no files written yet)

For every team, extract:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening it]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [list, one per line].`

Collision check: any identical lens phrases -> `LENS-COLLISION: [teams]. Revise one before continuing.`

---

**3b -- Inertia Advocate files** (all teams, before any standard or specialized role)

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from 3a; expands in 2-3 sentences;
  no generic stability language
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart (role most likely to
  propose the change-pressure initiative)

No two IA files share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from 3a]"
  opens verbatim: YES / NO
```
Any NO -> rewrite the lens field before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams covered.`

---

**3c -- org-chart.md** (after all IA files)

Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.

2. Headcount by Group/Area:
   ```markdown
   | Group/Area | Headcount | Key Roles |
   |------------|-----------|-----------|
   | [name]     | [n]       | [names]   |
   | **Total**  | **[n]**   |           |
   ```

3. Level Distribution -- labels from org.yaml. Total matches headcount Total.
   If no levels declared, infer IC and Management from role names.

4. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from org.yaml]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current structure: [parent > child pairs from org.yaml]
   ```

`CHART-WRITTEN.`

---

**3d -- Standard and specialized role files**

Paths: `.craft/roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.craft/roles/{group-slug}/{role-slug}.md` (shared group),
`.craft/roles/exec-office/{role-slug}.md` (exec office)

All five fields, no placeholder text. Scope field explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`

`ROLES-COMPLETE: [n] files written.`

---

### PHASE 4 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.
**Purpose**: Confirm that every Inertia Advocate role file's lens field opens with the exact
phrase extracted in the resistance profile. This phase closes the Phase 3a derivation loop
as a post-write structural invariant. Drift between profile extraction and final file is
caught here, not assumed absent.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3a]"
  IA lens field opening:  "[actual first phrase in written .craft/roles/ file]"
  match: VERBATIM / DRIFT
  if DRIFT: "[file opening]" does not match "[profile phrase]"
            action: rewrite IA lens field to open with profile phrase verbatim
```

After all teams:

`BUILD-VERIFY-PASS: [n of n] IA lens phrases verified verbatim against profiles. Derivation loop closed.`
or `BUILD-VERIFY-FAIL: [n] mismatch(es): [team names]. Rewrite each flagged IA lens before proceeding.`

If BUILD-VERIFY-FAIL: rewrite each flagged IA lens, then reemit the BUILD-VERIFY block
showing VERBATIM for all teams before proceeding.

`BUILD-VERIFY-COMPLETE: all IA lens phrases confirmed.`

---

### PHASE 5 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  if MISMATCH: missing: [list]

  IA files:  teams [n], IA files [n] -- MATCH / MISMATCH
  dir check: areas in org.yaml [list], dirs present [list] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`
Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4 checks) -- no files written before validation
  profiles:      [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA coverage:   [n of n] teams -- written before standard/specialized
  org-chart.md:  written
  role files:    [n] written / [n] declared
  build-verify:  PASS -- [n of n] IA lens phrases confirmed verbatim against profiles
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-02 -- Output Format: CONTRACT-SEAL and TRANSCRIPTION-RECEIPT (C-18)

**Axis**: Output format
**Hypothesis**: When the headcount table and analytic prose are written in a pre-role
contract phase (as in R3 V-05), the instruction "transcribe verbatim" in the org-chart.md
phase is present but unverified. The model can satisfy the surface instruction by producing
numerically identical output while having regenerated the text -- and C-18 fails because
the contract is not the source, the model is. A CONTRACT-SEAL step that marks artifacts
as immutable + a TRANSCRIPTION-RECEIPT log inside the org-chart.md write phase -- showing
exactly what was copied and from where -- makes C-18 pass by making transcription visible
as an act, not an outcome. "No regeneration" must be a named rule, not an implication.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE -> WRITE ->
CROSS-REF. Each gate must appear in output before the next phase begins.

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
**This phase produces the headcount table and analytic prose. These become the sealed
contract artifacts for org-chart.md. They are not regenerated at org-chart write time --
only transcribed.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules: one row per area; headcount = count of all role slots for that area; Total = sum
of all area rows.

`TABLE-CLOSED: [n] area rows, headcount total = [n]. File generation must produce
exactly [n] .craft/roles/ files.`

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

---

### PHASE 4 -- CONTRACT-SEAL

**Entry**: CONTRACT ARTIFACT-A, -B, and -C complete.

Emit this block:

```
CONTRACT-SEALED:
  ARTIFACT-A (headcount table):    [n] area rows, total headcount = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B (analytic prose):     [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C (level distribution): [n] levels, total = [n]

  RULE: These artifacts are FINAL. When writing org-chart.md in Phase 6,
        sections 2-4 are copies of these artifacts -- not regenerations.
        Do not recalculate headcount. Do not rewrite the analytic prose.
        Do not reformat the level table. The org-chart.md content IS these
        artifacts. Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 6.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PHASE 5.`

---

### PHASE 5 -- PROFILE

**Entry**: CONTRACT-GATE.
**No files written during this phase.**

For every team in the headcount table:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening it
                      -- not a generic force like "rapid change" or "new technology"]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field; cannot be produced
                      without knowing both other fields]
```

After all profiles:

```
PROFILE-COMPLETE: [n of n] teams.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: identical or near-identical phrases -> `LENS-COLLISION: [teams]. Revise one.`

`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE.`

---

### PHASE 6 -- WRITE

**Entry**: PROFILE-GATE.

**6a -- Inertia Advocate files (all teams)**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:
- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; expands in 2-3 sentences;
  no generic stability language
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart (role most likely to
  propose the change-pressure initiative)

After each file:
```
IA-WRITTEN: [team]
  lens-phrase from profile: "[phrase]"
  opens verbatim: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams.`

---

**6b -- org-chart.md**

**TRANSCRIPTION RULE: sections 2-4 of org-chart.md are copied from CONTRACT-SEALED
artifacts. Do not regenerate from org.yaml. Do not recalculate counts. Do not rewrite
the analytic prose. The source for sections 2-4 is CONTRACT-SEAL, not the model.**

Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.

2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim]

3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]

4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]

5. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs]
   ```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    match: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT-SEALED sentence 1: "[verbatim]"
    org-chart.md sentence 1:    "[verbatim]"
    match: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total:  [n]
    org-chart.md total:     [n]
    match: VERBATIM / REVISED
```

Any REVISED -> rewrite that section from the sealed artifact. Reemit that receipt line.
All VERBATIM: `TRANSCRIPTION-PASS: contract fidelity confirmed.`

`CHART-WRITTEN.`

---

**6c -- Standard, specialized, shared group, and exec office role files**

Paths per scope type. All five fields, no placeholder text. Scope explicit.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`

---

### PHASE 7 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  if MISMATCH: missing: [list]

  IA files:         teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:        areas [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity:   CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4) -- no files written before validation
  contract:      SEALED (headcount=[n], analytic prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA phase:      [n of n] teams written from profiles
  transcription: PASS -- CONTRACT ARTIFACT-A/B/C copied verbatim to org-chart.md
  role files:    [n] written / [n] declared
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-03 -- Phrasing Register: Output-Forward Verbatim Chain (C-17, C-18)

**Axis**: Phrasing register
**Hypothesis**: Describing what a correctly executed build produces -- showing the full
chain from contract artifact to org-chart.md section and from resistance profile to final
IA lens field -- in output-forward language (what you see, not what you do) is more likely
to produce C-17 and C-18 compliance than imperative instructions. The model sees the target
output shape, including the verbatim transcription receipt and the post-write lens check,
and replicates it. Key mechanism: explicit before/after contrasts at the transcription and
lens-check stages that show what "verbatim" and "drift" look like in practice.

---

You are running `corps-build`. Read org.yaml in the working directory, or use the path provided.

`corps-build` produces two artifacts: **org-chart.md** and **.craft/roles/ files**.
What follows describes what correct output looks like at each stage, including what
verbatim transcription and lens-phrase verification look like when done correctly.

---

### Stage 1: Parse

Read org.yaml. Emit:
```
PARSE: [org name], [n] teams, [n] role slots, nesting depth [n].
```
If malformed: `PARSE-FAIL: [description]. Halt.`

---

### Stage 2: Validate

Before writing anything, check: every team has at least one declared role; no role name
appears in both standard and specialized for the same team; no two teams share a name;
level vocabulary is consistent. If any problem is found, list it and halt.
If none: `VALIDATE: no structural anomalies. [n] teams, [n] slots confirmed.`

---

### Stage 3: The build contract -- what it looks like and why it comes first

Before any file is written, the build contract is produced. The contract has three
components, and they are produced in this stage only -- not rewritten later.

**Component A -- Headcount table:**
One row per area, headcount column summed to Total. This table is not a preview -- it is
the exact table that will appear in org-chart.md. Once produced, it does not change.

**Component B -- Analytic prose (2-3 sentences):**
Sentences name specific findings from the table. A correct example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml. The org has a clear concentration in infrastructure roles relative to
> product-facing roles."

An incorrect example (do not produce this):
> "The org has several teams with varying headcount. The level distribution is provided below."

**Component C -- Level distribution table + seniority sentence:**
One row per level label from org.yaml. Total matches headcount Total from Component A.

Emit: `CONTRACT-READY: headcount total [n], analytic prose [n] sentences, levels [n] entries.`

---

### Stage 4: Resistance profiles -- what they look like and how they feed the IA files

Before writing any IA file, a resistance profile for each team is produced. A correct profile:

```
PROFILE: [team name]
  defended-artifact:  [specific named thing this team owns -- not a category]
  change-pressure:    [specific named initiative threatening it -- not a generic force]
  lens-phrase:        "[5-10 word compressed statement of the specific tension]"
```

A correct lens-phrase opens the IA lens field verbatim. It is a compression of the
specific tension between what is defended and what threatens it. It cannot be produced
without knowing both defended-artifact and change-pressure.

After all profiles: `PROFILE-COMPLETE: [n] profiles. Lens phrases: [list, team: "phrase"].`

---

### Stage 5: What .craft/roles/inertia-advocate.md files look like

A correctly produced IA file is a portrait of the specific person who would occupy this
role on this team. The `lens` field opens with the resistance profile's lens-phrase,
verbatim. The `expertise` field names the defended artifact and associated systems.
The file cannot be transplanted unchanged to a different team's IA slot.

Five fields: orientation, lens, expertise, scope (`standard -- present in all teams`),
collaboration pattern.

Write all IA files before any standard or specialized role files. After each:
```
IA-WRITTEN: [team]
  lens opens with profile lens-phrase: YES / NO
  expertise names a concrete artifact (not a category): YES / NO
```
Any NO -> rewrite that field before continuing.

After all IA files: `IA-COMPLETE: [n of n] teams.`

---

### Stage 6: Standard, specialized, shared group, and exec office role files

All five fields. No placeholder text. Scope explicit in every file.
After each team: `TEAM-COMPLETE: [team] -- [n] std + [n] spec.`

---

### Stage 7: What org-chart.md looks like -- and what verbatim transcription means

org-chart.md has five sections:

1. ASCII hierarchy
2. Headcount table -- this is CONTRACT Component A, copied verbatim.
   No recalculation. No reformatting. Not written again from org.yaml.
3. Analytic prose -- this is CONTRACT Component B, copied verbatim.
   The same sentences. Not a rewrite. Not a summary of the same content.
4. Level distribution -- this is CONTRACT Component C, copied verbatim.
5. AMEND section (three options: --area, --levels, --restructure, each with specific values)

**What verbatim transcription means:**
The headcount total in org-chart.md is the same number produced in Stage 3.
The first sentence of the analytic prose in org-chart.md is the same sentence written
in Stage 3. Not a similar sentence. The same sentence, word for word.

**What verbatim transcription does not mean:**
Writing the table again from org.yaml and arriving at the same counts. That is regeneration.
Even if the counts match, regeneration fails C-18 because the contract is not the source.

After writing org-chart.md, a transcription receipt confirms what was copied:

```
TRANSCRIPTION-RECEIPT:
  headcount table:    CONTRACT total [n] -> org-chart.md total [n]
                      match: VERBATIM / REVISED
  analytic prose:     CONTRACT sentence 1: "[phrase]"
                      org-chart.md sentence 1: "[phrase]"
                      match: VERBATIM / REVISED
  level distribution: CONTRACT total [n] -> org-chart.md total [n]
                      match: VERBATIM / REVISED
```

Any REVISED -> rewrite that section from the CONTRACT artifact before proceeding.
`CHART-WRITTEN.`

---

### Stage 8: What the build-complete verification looks like

After all files are written, the build-complete verification confirms that every IA lens
field in every .craft/roles/ file opens with the exact lens-phrase from Stage 4. This is
the final confirmation that the derivation chain from resistance profile to written file
is intact.

A correct build-complete verification looks like this:

```
BUILD-VERIFY: [team name]
  Stage 4 lens-phrase:      "[phrase]"
  IA file lens opening:     "[first phrase of lens field as written]"
  match: VERBATIM / DRIFT
```

**What VERBATIM means:** The first words of the lens field in the written file are exactly
the words in the lens-phrase entry from Stage 4.

**What DRIFT means:** The IA file's lens field opened with a paraphrase, a synonym, or a
summary of the lens-phrase rather than the phrase itself. Drift is a write failure --
the profile derivation was not honored in the final artifact. Even a close paraphrase
is drift: "Schema contract table stability" drifts from "Schema contract table integrity
under federation migration" and must be corrected.

After all teams:
`BUILD-VERIFY-PASS: [n of n] IA lenses verified verbatim.`
or `BUILD-VERIFY-FAIL: [n] drift(s). Correct each failing IA lens to open with profile phrase.`

---

### Stage 9: Cross-reference

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       [n of n] teams -- MATCH / MISMATCH
  table fidelity: CONTRACT headcount [n] == org-chart.md headcount [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`

---

**CORPS-BUILD -- {date}**

```
  parse:          [org name], [n] teams
  validate:       PASS -- no anomalies
  contract:       headcount=[n], prose=[n] sentences, levels=[n]
  profiles:       [n of n] teams
  IA files:       [n of n] -- portraits written from profiles
  standard roles: [n], specialized roles: [n]
  org-chart.md:   written (transcription: VERBATIM / REVISED)
  build-verify:   [n of n] IA lenses confirmed verbatim against profiles
  cross-ref:      PASS / FAIL
  status:         COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-04 -- Lifecycle + Output Format: CONTRACT-TRANSCRIBE-VERIFY Pipeline (C-17, C-18)

**Axes**: Lifecycle emphasis + Output format
**Hypothesis**: C-17 and C-18 form a structural pair: C-18 requires the contract to be
the source (not regenerated at write time); C-17 requires the derivation chain to be
confirmed at build-complete (not merely claimed at write time). A prompt that composes
these as a named pipeline -- CONTRACT-SEAL marks artifacts immutable before any file
is written; TRANSCRIBE copies them into org-chart.md with a receipt; BUILD-VERIFY confirms
IA lens phrases post-write -- makes both criteria pass by construction through
complementary mechanisms. CONTRACT-SEAL prevents drift at write time; BUILD-VERIFY catches
drift that slipped through. The combination is stronger than either alone and requires
no redundant steps.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

Execute steps in order. Each gate must appear in output before the next step begins.

**Step sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-ROLES -> TRANSCRIBE -> BUILD-VERIFY -> CROSS-REF

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

**Entry**: VALIDATE-PASS.
**No files written during this step.**

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
        Any revision between CONTRACT-SEAL and org-chart.md write is a build failure.
        Compliance is audited via TRANSCRIPTION-RECEIPT in STEP 8.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce (contract total = [n]).`

---

**STEP 5 -- PROFILE**

**Entry**: CONTRACT-GATE.
**No files written during this step.**

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

Collision check: identical or near-identical phrases -> `LENS-COLLISION: [teams]. Revise one.`

`PROFILE-GATE: all profiles distinct. Proceeding.`

---

**STEP 6 -- WRITE-IA**

**Entry**: PROFILE-GATE.
Write all Inertia Advocate files before any standard or specialized role.
Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:

- **orientation**: from `defended-artifact`; specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Step 5; expands to name the domain
  slice monitored; no generic stability language
- **expertise**: anchored to `defended-artifact`; names specific system and operational
  knowledge; differs across all teams
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums (design review, architecture board), cadence,
  primary counterpart (role most likely to propose the change-pressure initiative)

After each file:
```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 5]"
  opens verbatim: YES / NO
  expertise concrete (names artifact, not category): YES / NO
```
Any NO -> rewrite that field before proceeding.

Portrait self-check after all IA files:
- [ ] No two IA files share identical lens or expertise text
- [ ] Every lens field contains no generic phrases ("stability," "institutional knowledge,"
      "status quo," "existing processes" unqualified)
- [ ] Every expertise entry names a concrete artifact, not a domain category
- [ ] File could not be transplanted to a different team unchanged

```
PORTRAIT-CHECK: [n of n] files pass all four checks.
  Failures (if any): [team] -- [failed check] -- [rewrite applied]
```

`IA-PHASE-COMPLETE: [n of n] teams. All portrait checks pass.`

---

**STEP 7 -- WRITE-ROLES**

**Entry**: IA-PHASE-COMPLETE.

Standard role files, then specialized, then shared group (if declared), then exec office
(if declared). Paths per scope type. All five fields, no placeholder text. Scope explicit.

After each team: `TEAM-WRITTEN: [team] -- 1 IA + [n] std + [n] spec.`

`ROLES-GATE: [n] role files written.`

---

**STEP 8 -- TRANSCRIBE**

**Entry**: ROLES-GATE.

Write org-chart.md. Sections in order:

1. **ASCII hierarchy** -- box-drawing characters, minimum two nesting levels. Group names
   from org.yaml exactly. Team leaf nodes show headcount.

2-4. **TRANSCRIBE from CONTRACT-SEALED:**
   - Section 2: ARTIFACT-A verbatim. Do not regenerate from org.yaml. Do not recalculate.
   - Section 3: ARTIFACT-B verbatim. Same sentences -- not a rewrite, not a summary.
   - Section 4: ARTIFACT-C verbatim + seniority sentence.

5. **AMEND section:**
   ```markdown
   ## AMEND
   1. --area "[name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs]
   ```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total: [n]
    org-chart.md total:    [n]
    match: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT-SEALED sentence 1: "[verbatim]"
    org-chart.md sentence 1:    "[verbatim]"
    match: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total: [n]
    org-chart.md total:    [n]
    match: VERBATIM / REVISED
```

Any REVISED -> rewrite that section from the sealed artifact. Reemit that receipt line.
All VERBATIM: `TRANSCRIPTION-PASS: contract fidelity confirmed.`

`CHART-GATE: org-chart.md written.`

---

**STEP 9 -- BUILD-VERIFY**

**Entry**: CHART-GATE.
**Purpose**: Close the derivation loop. Confirm every IA lens field opens with the exact
phrase from Step 5. This runs after all files are written -- not at write time. Any drift
between profile extraction and file writing is caught here.

For each team:

```
BUILD-VERIFY: [team]
  Step 5 lens-phrase:       "[phrase]"
  IA file lens opens with:  "[actual opening phrase in written file]"
  match: VERBATIM / DRIFT
  if DRIFT: "[file opening]" does not match "[profile phrase]"
            rewrite IA lens to open with profile phrase verbatim
```

After all teams:

`BUILD-VERIFY-PASS: [n of n] IA lenses verbatim against profiles. Derivation loop closed.`
or `BUILD-VERIFY-FAIL: [n] drift(s). Rewrite flagged IA lens fields. Reemit BUILD-VERIFY block.`

---

**STEP 10 -- CROSS-REF**

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:      areas [list], dirs [list] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4) -- no files written before validation
  contract:      SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams (defended-artifact + change-pressure -> lens-phrase)
  IA phase:      [n of n] teams -- written from profiles; portrait check [n/n] pass
  role files:    [n] written / [n] declared
  transcription: PASS -- ARTIFACT-A/B/C copied verbatim to org-chart.md
  build-verify:  PASS -- [n of n] IA lenses confirmed verbatim against profiles
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-05 -- Full Integration: All Ten Aspirational Criteria (C-09 through C-18)

**Axes**: Inertia framing + Lifecycle emphasis + Output format + Role sequence
**Hypothesis**: R3 V-05 scored 10/10 aspirational (8/8 at the time) by composing
C-09 through C-16 in a linear phase sequence where each criterion maps to a minimal
named mechanism. R4 extends this with C-17 and C-18:
- C-17 was implicit in R3 V-05's CROSS-REF C4 check. R4 makes it a named BUILD-VERIFY
  phase that explicitly closes the derivation loop after all files are written.
- C-18 was present as an instruction ("transcribe verbatim") in R3 V-05's Phase 6.
  R4 adds CONTRACT-SEAL (immutable artifact) and TRANSCRIPTION-RECEIPT (auditable copy).

Criterion-to-mechanism map (all ten):
- C-09: IA lens/expertise derived from per-team profile (PHASE 4)
- C-10: CROSS-REF checks chart total vs file count (PHASE 8)
- C-11: VALIDATE gates all writes (PHASE 2)
- C-12: IA-PHASE-COMPLETE before standard/specialized roles (PHASE 5)
- C-13: headcount table written in BUILD CONTRACT before any file (PHASE 3)
- C-14: mandatory analytic prose in BUILD CONTRACT (PHASE 3)
- C-15: portrait self-check gate in IA phase (PHASE 5)
- C-16: PROFILE phase with three gated fields before IA write (PHASE 4)
- C-17: BUILD-VERIFY phase after all files, IA lens verbatim confirmation (PHASE 7)
- C-18: CONTRACT-SEAL marks artifacts immutable + TRANSCRIPTION-RECEIPT confirms copy (PHASE 3)

The ten mechanisms remain compatible in linear order. No conflicts introduced.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

Ten phases. Each gate must appear in output before the next phase begins.
No file is written before Phase 5.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- std: [names], spec: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels: [list or "not declared"]
  depth: [n]
  total slots: [n]
```

`PARSE-PASS: [n] teams, [n] slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared     PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec collision per team         PASS / FAIL -- [team.role collisions]
  [V-3] no duplicate team names                PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. No structural anomalies. Proceeding to PHASE 3.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 -- BUILD CONTRACT

**Entry**: VALIDATE-PASS.
**This phase produces the headcount table and analytic prose before any .craft/roles/ file.
These artifacts will be transcribed verbatim into org-chart.md in Phase 6. They are sealed
after this phase and not regenerated at write time.**

**3a -- Headcount table:**

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules: one row per area; headcount = sum of all role slots; Total = sum of all area rows.

`TABLE-CLOSED: [n] area rows, headcount total = [n]. File generation must produce
exactly [n] .craft/roles/ files.`

**3b -- Analytic prose (mandatory, 2-3 sentences):**
- Sentence 1: name the largest area and its headcount as a percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: a structural observation the table rows alone do not convey -- not generic

**3c -- Level distribution table:**

```markdown
## Level Distribution

| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One sentence on seniority profile after the table.

**3d -- CONTRACT-SEAL:**

```
CONTRACT-SEALED:
  ARTIFACT-A (headcount table):    [n] area rows, total = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B (analytic prose):     [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C (level distribution): [n] rows, total = [n]

  RULE: These artifacts are FINAL. In Phase 6, org-chart.md sections 2-4 are
        copies of these artifacts unchanged. No regeneration. No reformatting.
        Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 6.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PHASE 4.`

---

### PHASE 4 -- RESISTANCE PROFILES

**Entry**: CONTRACT-GATE.
**No files written during this phase.**
**No IA file may be written before PROFILE-COMPLETE.**

For every team in the headcount table, extract three fields:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening
                      the defended artifact -- not a generic force]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure; opens
                      the IA lens field verbatim; cannot be generic; cannot be written
                      without knowing both other fields]
```

Derivation requirement: `lens-phrase` is a compressed statement of the specific tension
between what is defended and what threatens it. A phrase producible without knowing both
`defended-artifact` and `change-pressure` is not derived.

After all profiles:

```
PROFILE-COMPLETE: [n of n] teams profiled.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: `LENS-COLLISION: [teams] -- "[phrase]". Revise one.` -- halt until resolved.

`PROFILE-GATE: all profiles complete with distinct lens phrases. Proceeding to PHASE 5.`

---

### PHASE 5 -- WRITE ROLE FILES

**Entry**: PROFILE-GATE.

**5a -- PASS 1: All Inertia Advocate files (all teams before any other role)**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields from the resistance profile:

- **orientation**: from `defended-artifact` -- the rational perspective of the person who
  built or maintains it; names the specific concern; no generic stance toward stability
- **lens**: opens verbatim with the `lens-phrase` from Phase 4; expands in 2-3 sentences
  naming the specific domain slice monitored; no "stability," "institutional knowledge,"
  or phrases applicable to any team
- **expertise**: anchored to `defended-artifact`; names the specific system, schema, or
  procedure and related operational knowledge; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums (design review, sprint planning, architecture board),
  cadence, primary counterpart (the role most likely to propose the change-pressure
  initiative on this team)

No two IA files share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  profile lens-phrase used: "[phrase]"
  lens-phrase appears verbatim: YES / NO
  expertise anchored to defended-artifact: YES / NO
```
Any NO -> rewrite the failing field before proceeding.

After all IA files, portrait self-check:

For each IA file, confirm:
- [ ] lens opens with the Phase 4 lens-phrase verbatim
- [ ] expertise names a concrete artifact (not a domain category)
- [ ] no generic resistance phrases present ("stability," "institutional knowledge,"
      "status quo," "existing processes" as unqualified terms)
- [ ] file could not be transplanted to a different team unchanged

```
PORTRAIT-CHECK: [n of n] IA files pass all four checks.
  Failures (if any): [team] -- [failed check] -- [rewrite applied]
```

`IA-PHASE-COMPLETE: [n of n] teams. All portraits verified. Standard and specialized
roles may now be written.`

---

**5b -- PASS 2: Standard role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: standard -- present in all teams`.

**5c -- PASS 3: Specialized role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: specialized -- [team name]`.

**5d -- Shared group roles** (if declared)

Path: `.craft/roles/{group-slug}/{role-slug}.md`, `scope: shared -- group: [name]`

**5e -- Exec office roles** (if declared)

Path: `.craft/roles/exec-office/{role-slug}.md`, `scope: exec office`

Standard vs. specialized must be explicit in `scope` -- not derivable from directory alone.
No placeholder text in any field.

After each team: `TEAM-WRITTEN: [team] -- 1 IA + [n] std + [n] spec.`

`ROLES-GATE: [n] written / [n] declared (TABLE-CLOSED). MATCH / MISMATCH.`
If MISMATCH: `ROLES-GATE-FAIL: missing: [list]. Halt.`

---

### PHASE 6 -- WRITE ORG-CHART.MD

**Entry**: ROLES-GATE MATCH.

org-chart.md sections in this order:

1. **ASCII hierarchy** -- box-drawing characters, minimum two nesting levels. Group names
   exactly as in org.yaml. Team leaf nodes show headcount.

2. **Headcount table** -- TRANSCRIBE CONTRACT-SEALED ARTIFACT-A verbatim.
   Do not regenerate from org.yaml. Do not recalculate.

3. **Analytic prose** -- TRANSCRIBE CONTRACT-SEALED ARTIFACT-B verbatim.
   Same sentences as written in Phase 3. Not rewritten.

4. **Level distribution + seniority sentence** -- TRANSCRIBE CONTRACT-SEALED ARTIFACT-C verbatim.

5. **AMEND section:**
   ```markdown
   ## AMEND
   1. --area "[name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs, e.g. "Platform > Infrastructure, Platform > Reliability"]
   ```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT:

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT-SEALED total: [n]
    org-chart.md total:    [n]
    match: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT-SEALED sentence 1: "[phrase]"
    org-chart.md sentence 1:    "[phrase]"
    match: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT-SEALED total: [n]
    org-chart.md total:    [n]
    match: VERBATIM / REVISED
```

Any REVISED -> rewrite that section from the sealed artifact. Reemit that receipt line showing VERBATIM.
All VERBATIM: `TRANSCRIPTION-PASS: contract fidelity confirmed.`

`CHART-GATE: org-chart.md written. Proceeding to PHASE 7.`

---

### PHASE 7 -- BUILD-VERIFY

**Entry**: CHART-GATE.
**Purpose**: Close the C-16 derivation loop as a post-write structural invariant. Verify
that every Inertia Advocate role file's lens field opens with the exact lens-phrase derived
in Phase 4. This check runs after all files are written -- not at write time. Drift between
profile extraction and the final written file is caught here, not assumed absent.

For each team:

```
BUILD-VERIFY: [team]
  Phase 4 lens-phrase:     "[phrase from Phase 4]"
  IA lens field opening:   "[actual first phrase in written .craft/roles/ file]"
  match: VERBATIM / DRIFT
  if DRIFT: "[file opening]" != "[profile phrase]" -- rewrite IA lens to open verbatim
```

After all teams:

`BUILD-VERIFY-PASS: [n of n] IA lens phrases verified verbatim against Phase 4 profiles.
Derivation loop closed.`
or `BUILD-VERIFY-FAIL: [n] drift(s): [team names]. Rewrite each failing IA lens field,
then reemit BUILD-VERIFY block.`

`BUILD-VERIFY-GATE: all IA lenses confirmed. Proceeding to PHASE 8.`

---

### PHASE 8 -- CROSS-REFERENCE

**Entry**: BUILD-VERIFY-GATE.

```
CROSS-REF:
  C1 -- TABLE-CLOSED contract vs .craft/roles/ file count
        contract: [n], files written: [n]
        result: MATCH / MISMATCH
        if MISMATCH: in contract not in files: [list]
                     in files not in contract: [list]

  C2 -- every team has an IA file
        teams: [n], IA files: [n] -- MATCH / MISMATCH
        if MISMATCH: teams missing IA: [list]

  C3 -- every area in headcount table has a .craft/roles/{area}/ directory
        table areas: [list], directories present: [list] -- MATCH / MISMATCH
        if MISMATCH: missing dirs: [list] / extra dirs: [list]
```

All MATCH: `CROSS-REF-PASS: build consistent.`
Any MISMATCH: `CROSS-REF-FAIL: [details]. Build is not consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:            PASS (4/4) -- no files written before validation
  headcount table:     written pre-roles (contract: [n] files, analytic prose: included)
  contract-seal:       ARTIFACT-A/B/C locked before PROFILE phase
  resistance profiles: [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA phase:            [n of n] teams -- written from profiles; portrait self-check [n/n] pass
  standard roles:      [n]
  specialized roles:   [n]
  shared group roles:  [n]
  exec office roles:   [n]
  total files:         [n] written / [n] declared -- MATCH / MISMATCH
  transcription:       PASS -- ARTIFACT-A/B/C verbatim in org-chart.md
  build-verify:        PASS -- [n of n] IA lenses confirmed verbatim against Phase 4 profiles
  cross-ref:           PASS / FAIL
  status:              COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## Variation Summary

| Var | Axis | Key Hypothesis | Criteria Targeted | R3 Predecessor |
|-----|------|----------------|-------------------|----------------|
| **V-01** | Lifecycle emphasis | Named BUILD-VERIFY phase (post-write, single purpose: IA lens verbatim) makes C-17 visible and ungroupable from CROSS-REF file-count check | C-17 | Extracts R3 V-05 CROSS-REF C4 into dedicated phase |
| **V-02** | Output format | CONTRACT-SEAL marks headcount/prose immutable + TRANSCRIPTION-RECEIPT audits copy; "no regeneration" as named rule, not implication | C-18 | Extends R3 V-05 Phase 3 + Phase 6 transcribe instruction |
| **V-03** | Phrasing register | Output-forward description of verbatim chain with VERBATIM/DRIFT and VERBATIM/REVISED contrast produces compliance by showing target output shape | C-17, C-18 | New register applied to R3 V-03 approach |
| **V-04** | Lifecycle + Output format | CONTRACT-SEAL (immutable artifact) + TRANSCRIBE (receipt) + BUILD-VERIFY (post-write lens check) form a paired construction-verification pipeline | C-17, C-18 | Combines V-01 + V-02 mechanisms as sequential steps |
| **V-05** | All axes | R3 V-05 architecture extended with CONTRACT-SEAL (3d) and BUILD-VERIFY (PHASE 7); ten criteria in linear sequence, each mapped to minimal mechanism | C-09 through C-18 | Directly extends R3 V-05; adds phases without restructuring |
