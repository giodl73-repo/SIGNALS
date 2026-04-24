---
skill: quest-variate
skill_target: corps-build
round: 7
date: 2026-03-16
rubric_version: 7
---

# Variate R7 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v7 adds C-22 (named binary path structure) and C-23 (declarative block-shape
correctness rules). R6 had three variations at 100 under v6 (V-01, V-02, V-04). Under
v7, all three have gaps: PATH-A/PATH-B labels are defined as instruction structure but
not emitted as output tokens at execution point (C-22); structural blocks are described
procedurally rather than with explicit "a correct X is..." correctness rules and named
invalidity conditions (C-23). V-03 R6 (95 pts) comes closest to C-23 but had C-08
PARTIAL -- its AMEND section lacked a block-shape correctness rule with concrete option
placeholders.

---

## R6 Gap Analysis (rubric v7 lens)

| New Criterion | Best R6 Coverage | Gap |
|---------------|-----------------|-----|
| C-22 Named binary path structure | V-02 R6: PATH-A / PATH-B as named structural sections in WRITE-CHART; FINAL SUMMARY template includes `[PATH-A: ... \| PATH-B: ...]` | Pass condition: "each path label appears in the phase output at the point where that path executes." V-01/V-02/V-04 R6 define PATH-A and PATH-B as instruction-level section headers. The instruction does not require the model to emit `PATH-A` or `PATH-B` as an output token at the moment the path fires. A model executing PATH-B correctly (rewrite + TRANSCRIPTION-CLEAR + CHART-WRITTEN) may never print "PATH-B" in WRITE-CHART's output -- only in FINAL SUMMARY. C-22 requires the label to appear at execution point, not only in a trailing summary. |
| C-23 Declarative block-shape correctness rules | V-03 R6: "A BUILD-VERIFY block with non-verdict content is structurally invalid"; "A TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally incomplete" | V-03 R6 passes C-23 but scored PARTIAL on C-08 (AMEND section named as a section of org-chart.md but no block-shape correctness rule specifying the three `--area`/`--levels`/`--restructure` options with concrete value placeholders). The gap for all other R6 variations: they describe what phases do (procedural framing) rather than declaring what correct output looks like (declarative framing). None of V-01/V-02/V-04 have "a correct TRANSCRIPTION-RECEIPT contains..." or "a correct AMEND section contains..." phrasing. |

The gap for C-22 is emission location: label must appear as an output token at the
moment the path fires, not only in a post-build summary. The gap for C-23 is framing
depth: correctness rules must be stated as declarative output-forward shape
descriptions with named invalidity conditions -- not as behavioral phase instructions.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format: PATH-A/PATH-B label emitted as explicit output token at path execution point | V-01 |
| Phrasing register: declarative block-shape correctness rules for all named structural blocks | V-02 |
| Phrasing register (narrow fix): AMEND correctness rule added to R6 V-03 declarative architecture | V-03 |
| Output format + phrasing register: PATH label emission + declarative correctness rules (combined) | V-04 |
| Full integration: PROFILE-before-CONTRACT + PATH label emission + declarative correctness rules | V-05 |

---

## V-01 -- Output format: PATH-A/PATH-B label emitted as output token at execution point (C-22)

**Axis**: Output format (PATH label emission)
**Hypothesis**: R6 V-01 defines PATH-A and PATH-B as named instruction regions and
mentions them in the FINAL SUMMARY template. But neither the path-entry instruction nor
the phase-output template requires the model to emit "PATH-A" or "PATH-B" as a visible
token at the moment the path fires inside WRITE-CHART. The minimal fix is one explicit
instruction: after evaluating TRANSCRIPTION-RECEIPT, emit a `CHART-PATH:` line naming
the path selected before executing that path. This makes the path label an observable
output token -- not just a structural label in the prompt. FINAL SUMMARY then traces
which path fired by referencing the CHART-PATH emission, closing the loop. The
exemption is preserved: PATH-A fires when all three verdicts are VERBATIM; PATH-B fires
when any verdict is REVISED. The emission requirement applies only to WRITE-CHART; no
other phase has named binary paths in this variation.

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
transcribed verbatim into org-chart.md in Phase 7. They are not regenerated at write
time.**

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

  RULE: These artifacts are FINAL. org-chart.md sections 2-4 are copies --
        not regenerations. Compliance is audited via TRANSCRIPTION-RECEIPT in Phase 7.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry condition**: CONTRACT-GATE. **No files written during this phase.**

For every team, extract a resistance profile:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, or procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift -- not generic]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure;
                      verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`

Collision check: identical lens phrases -> `LENS-COLLISION: [teams]. Revise one before continuing.`

`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: PROFILE-GATE.
**Write all Inertia Advocate files before any standard or specialized role files.**

Path: `.roles/{area-slug}/inertia-advocate.md`

Five fields derived from the resistance profile:
- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; 2-3 sentences;
  no generic stability language; no boilerplate applicable to any team
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA
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
   1. --area "[area name]" -- regenerate that area.
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list from org.yaml]
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

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**

- All three verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`

The `CHART-PATH:` line must appear as an output token before executing the path.

**After emitting CHART-PATH: PATH-A:**
No rewrites occurred. No TRANSCRIPTION-CLEAR block is required.
`CHART-WRITTEN.`

**After emitting CHART-PATH: PATH-B:**
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line to show corrected values and VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR. This block re-audits every contract
   artifact in a single pass -- including those already VERBATIM before the rewrite.
   The block covers all three or it does not serve as an exit gate.

   ```
   TRANSCRIPTION-CLEAR:
     ARTIFACT-A: VERBATIM
     ARTIFACT-B: VERBATIM
     ARTIFACT-C: VERBATIM
     all three confirmed -- CHART-WRITTEN authorized
   ```

   If any artifact shows REVISED in this re-audit: return to step 1 for that artifact.
   `CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
Paths: `.roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.roles/{group-slug}/{role-slug}.md` (shared group),
`.roles/exec-office/{role-slug}.md` (exec office)

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
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 5 profiles.`
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
  org-chart.md:  [CHART-PATH: PATH-A -- all VERBATIM, no re-audit required |
                  CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all three]
  role files:    [n] written / [n] declared
  build-verify:  PASS (single-purpose: [n of n] IA lens verdicts only)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-02 -- Phrasing register: declarative block-shape correctness rules for all named structural blocks (C-23)

**Axis**: Phrasing register (declarative correctness rules)
**Hypothesis**: R6 variations describe what each phase does ("this phase confirms X",
"this phase emits Y") rather than declaring what a correct output block looks like ("a
correct X contains Y"; "an X with fewer than Z items is structurally incomplete"). C-23
requires each named structural block to have an explicit declarative correctness rule in
output-forward terms with a named structural invalidity condition. V-02 takes R6 V-01's
architecture (which passes all 13 v6 criteria) and adds declarative correctness rules
adjacent to every named block: PROFILE, IA-WRITTEN, TRANSCRIPTION-RECEIPT,
TRANSCRIPTION-CLEAR, BUILD-VERIFY, AMEND, CROSS-REF. Rules use "a correct X is..."
framing. Invalidity conditions use "an X with non-Y content is structurally invalid"
framing. The block is self-describing: correctness is declared at the block definition
site, not in a preamble or trailing note.

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
**Three contract artifacts produced here. Sealed in Phase 4. Transcribed verbatim into
org-chart.md in Phase 7. Not regenerated at write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

One row per area. Total = sum of all area rows.
`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note its absence
- Sentence 3: structural observation the table rows alone do not convey. No generic summaries.

Strong example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml. The three product teams each carry two specialized roles, a higher ratio than
> any infrastructure team."

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence.**

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
  ARTIFACT-A: [n] area rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]

  RULE: org-chart.md sections 2-4 are verbatim copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite. Audited via TRANSCRIPTION-RECEIPT in Phase 7.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

### PHASE 5 -- PROFILE

**Entry condition**: CONTRACT-GATE. **No files written during this phase.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (a specific
named system, schema, pipeline, SLA, or procedure -- not a category), `change-pressure`
(a specific named migration, initiative, or shift -- not a generic force), and
`lens-phrase` (5-10 words derived from both fields; this phrase opens the IA lens field
verbatim). A PROFILE entry that names a category ("data stability") rather than a
specific artifact ("the nightly reconciliation job") is structurally underspecified.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific artifact -- not a category]
  change-pressure:    [specific initiative -- not a generic force]
  lens-phrase:        [5-10 words; verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`

Collision check: identical lens phrases -> `LENS-COLLISION: [teams]. Revise one before continuing.`

`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: PROFILE-GATE.
**All Inertia Advocate files written before any standard or specialized role files.**

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Phase 5; 2-3 sentences;
  no generic stability language; no phrase applicable to any team without rewrite
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt names the team, confirms the lens-phrase was applied, and
carries two binary checks. An IA-WRITTEN receipt missing any of these three fields is
structurally incomplete.

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
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- do not rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each naming specific mechanisms
drawn from org.yaml: (1) `--area "[name]"` with the list of available area names from
the headcount table; (2) `--levels "[old]:[new]"` with the level vocabulary currently
in use; (3) `--restructure "[team] > [new-parent]"` with the current parent > child
nesting pairs. An AMEND section with fewer than three options, or with options that
give no specific org.yaml values as placeholders, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area (resistance profile + IA + roles + chart row).
   Available areas: [list from headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C), each showing the CONTRACT-SEALED value, the org-chart.md
value, and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three
artifact rows is structurally incomplete.

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

PATH-A (all three verdicts VERBATIM on first receipt):
No rewrites occurred. No TRANSCRIPTION-CLEAR block is required.
`CHART-WRITTEN.`

PATH-B (one or more verdicts REVISED):
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line: corrected values, verdict VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts with a VERBATIM
verdict for each, in a single pass that includes artifacts already VERBATIM before
the rewrite. A TRANSCRIPTION-CLEAR that names fewer than three artifacts is
structurally incomplete and does not serve as an exit gate. CHART-WRITTEN may not
be emitted until TRANSCRIPTION-CLEAR is present and all three lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

If any artifact shows REVISED in this re-audit: return to step 1 of PATH-B.
`CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
All five fields, no placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase, an IA lens field opening, and a single VERBATIM/DRIFT
verdict. A BUILD-VERIFY block containing any content other than per-team
VERBATIM/DRIFT verdict entries -- file writes, structural checks, directory comparisons,
headcount verifications, summary rows -- is structurally invalid.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 5]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 5 profiles.`
`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

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
  profiles:      [n of n] teams (specific artifact + specific pressure + lens-phrase)
  IA coverage:   [n of n] teams -- written before standard/specialized
  org-chart.md:  [PATH-A: all VERBATIM first pass -- no re-audit required |
                  PATH-B: TRANSCRIPTION-CLEAR -- all three artifacts confirmed]
  role files:    [n] written / [n] declared
  build-verify:  PASS (single-purpose: [n of n] VERBATIM/DRIFT verdicts, no other content)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-03 -- Phrasing register narrow fix: AMEND correctness rule added to R6 V-03 declarative architecture (C-23 + C-08)

**Axis**: Phrasing register (narrow fix)
**Hypothesis**: R6 V-03 applied full declarative output-forward framing to all 13
aspirational criteria and received PARTIAL only on C-08: the AMEND section was named
as one of five org-chart.md sections but contained no block-shape correctness rule
specifying the three option shapes with concrete value placeholders. V-03 R6 scored 95.
The minimal fix is one addition: adjacent to the AMEND section definition, declare "a
correct AMEND section contains exactly three options..." with the option shapes. Under
v7, this variation must also pass C-22 (Shape A vs Shape B for TRANSCRIPTION-CLEAR
already satisfies "named binary paths" per the R6 V-03 shape-framing; the pass
condition accepts "equivalent named identifiers"). V-03 R7 is therefore V-03 R6 with
the AMEND shape rule inserted and no other changes.

```
You are running `corps-build`. Read org.yaml in the working directory, or use the path
provided.

**Stage sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL -> WRITE-IA ->
WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Every stage produces a named gate token before the next stage begins.

---

### STAGE 1 -- PARSE

A correct PARSE block names the org, lists all groups and teams with their parent
assignments, lists standard and specialized roles per team, lists any shared group or
exec office roles, states levels declared or "not declared", and gives a total role
slot count. A PARSE block missing any of these fields is structurally incomplete.

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
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

### STAGE 2 -- VALIDATE

**Entry**: PARSE-PASS. **No files written.**

A correct VALIDATE block carries four named checks. A VALIDATE block with fewer than
four checks, or that writes files before all checks pass, is structurally invalid.

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding.` or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

---

### STAGE 3 -- PROFILE

**Entry**: VALIDATE-PASS. **No files written.**

A correct PROFILE entry for a team contains exactly three fields: `defended-artifact`
(the specific named system, pipeline, schema, SLA, or process this team's IA would
defend -- not a category label), `change-pressure` (the specific named initiative,
migration, or architectural shift that threatens it -- not a generic force), and
`lens-phrase` (5-10 words derived from both, which opens the IA lens field verbatim).
A PROFILE entry naming a category ("data integrity") rather than a specific artifact
("the three-stage ETL validation sequence for order reconciliation") is structurally
underspecified. A PROFILE entry whose lens-phrase does not trace to both
`defended-artifact` and `change-pressure` is structurally ungrounded.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact]
  change-pressure:    [specific named initiative]
  lens-phrase:        [5-10 words derived from both]
```

Incorrect profile (do not produce):
```
PROFILE: Platform Team
  defended-artifact:  system stability
  change-pressure:    rapid change
  lens-phrase:        defending platform reliability against disruption
```

Correct profile:
```
PROFILE: Platform Team
  defended-artifact:  the circuit-breaker configuration governing three downstream services
  change-pressure:    migration to async event bus eliminating synchronous fallback paths
  lens-phrase:        circuit-breaker thresholds erased by async event bus migration
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: profiles confirmed. Proceeding to CONTRACT.`

---

### STAGE 4 -- CONTRACT

**Entry**: PROFILE-GATE. **No files written.**

A correct CONTRACT phase produces three artifacts before any file is written. A
CONTRACT phase that skips ARTIFACT-B or produces fewer than 2-3 analytic sentences
is structurally incomplete.

**ARTIFACT-A -- Headcount table:**
One row per area (not per team). Headcount = all role slots in that area, including
the IA role.

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] rows, total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**

A correct ARTIFACT-B names the largest area by headcount as a percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not readable from the table rows alone. An ARTIFACT-B with generic
language applicable to any org ("the org has several teams") is structurally deficient.

Strong:
> "Data Platform carries 11 of 28 total headcount -- the largest area at 39%. Only
> Data Platform and Infrastructure declare IC levels; the four product teams have no
> level vocabulary in org.yaml. Data Platform's three specialized roles outnumber any
> other area's, reflecting the depth of domain expertise concentration."

Weak (do not produce):
> "The org has multiple teams with varying headcount. Level distribution varies."

**ARTIFACT-C -- Level distribution table + seniority sentence:**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One seniority sentence referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

### STAGE 5 -- SEAL

**Entry**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]

  RULE: org-chart.md sections 2-4 are the same content -- not rewrites, not
        reformats. Sections 2-4 are ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim.
        Compliance verified via TRANSCRIPTION-RECEIPT in Stage 7.
```

`SEAL-COMPLETE: [n] files to produce. Proceeding to WRITE-IA.`

---

### STAGE 6 -- WRITE-IA

**Entry**: SEAL-COMPLETE. **All IA files before any standard or specialized role files.**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. Lens and expertise read as characterizations
of a particular individual's worldview and domain knowledge, not as a filled-in
template. A correct IA role file could not be transplanted to a different team without
substantive rewrite. An IA role file containing generic resistance language ("ensures
process stability", "advocates for continuity", "resists unnecessary change")
applicable to any team is structurally deficient.

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Stage 3 -- specific concern
- **lens**: opens verbatim with the Stage 3 `lens-phrase`; 2-3 sentences; no generic
  language; characterizes a specific viewpoint anchored to this team's domain
- **expertise**: names a concrete artifact, system, or practice this person would
  defend -- not a category
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Stage 3]"
  opens verbatim: YES / NO
  expertise names specific artifact: YES / NO
```

Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

---

### STAGE 7 -- WRITE-CHART

**Entry**: IA-COMPLETE.

Write org-chart.md with five sections:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels, group names
   match org.yaml exactly, team leaf nodes show headcount in parentheses
2. Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content. Not a rewrite.
3. (see above)
4. (see above)
5. AMEND section

A correct AMEND section contains exactly three options, each citing specific values
drawn from org.yaml: option 1 names `--area` with the area list from ARTIFACT-A;
option 2 names `--levels` with the level vocabulary from org.yaml; option 3 names
`--restructure` with the current parent > child nesting pairs. An AMEND section with
fewer than three options, or with options that give no specific org.yaml values as
placeholders, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains one row per contract artifact (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C), each with the CONTRACT-SEALED value, the org-chart.md value,
and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three artifact
rows is structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B: CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
```

**Shape A (all three verdicts VERBATIM on first receipt):**
A correct Shape-A exit contains no TRANSCRIPTION-CLEAR block. No rewrites occurred.
`CHART-WRITTEN.`

**Shape B (one or more verdicts REVISED):**
For each REVISED artifact: rewrite from the SEALED CONTRACT value. Update that
receipt row to VERBATIM.

After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts -- not only the ones
that were rewritten. It is a single-pass re-audit that confirms every artifact is
VERBATIM before CHART-WRITTEN is emitted. A TRANSCRIPTION-CLEAR that names fewer than
three artifacts is structurally incomplete and does not serve as an exit gate. A Shape-B
exit that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is structurally invalid.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm total matches CONTRACT-SEALED first-row lock]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1 lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  all three confirmed -- CHART-WRITTEN authorized
```

If any artifact shows REVISED in TRANSCRIPTION-CLEAR: rewrite that artifact and
re-emit TRANSCRIPTION-CLEAR covering all three before CHART-WRITTEN.
`CHART-WRITTEN.`

---

### STAGE 8 -- WRITE-ROLES

**Entry**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files. All five fields. No
placeholder text. Scope field names the role type explicitly:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

`TEAM-WRITTEN: [team] -- [n] std + [n] spec.` (after each team)
`ROLES-COMPLETE: [n] files written.`

---

### STAGE 9 -- BUILD-VERIFY

**Entry**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team), each with a
profile lens-phrase from Stage 3, the exact IA lens field opening from the written
file, and a VERBATIM/DRIFT verdict. The block contains nothing else. A BUILD-VERIFY
block with any content other than per-team lens-phrase comparison entries and their
VERBATIM/DRIFT verdicts is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Stage 3]"
  IA lens field opening:  "[exact first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry
before proceeding.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim.`
`BUILD-VERIFY-COMPLETE.`

---

### STAGE 10 -- CROSS-REF

**Entry**: BUILD-VERIFY-COMPLETE.

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

```
CROSS-REF:
  slots:         org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:   teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:   org.yaml areas [list] == .roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:        PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                 WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
  validate:      PASS (4/4 structural checks, no files written)
  profiles:      [n of n] teams (specific artifact + specific pressure + lens-phrase)
  contract:      SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  IA coverage:   [n of n] teams -- all portraits written before standard/specialized
  org-chart.md:  [Shape A: all VERBATIM, no TRANSCRIPTION-CLEAR required |
                  Shape B: TRANSCRIPTION-CLEAR -- all three artifacts confirmed VERBATIM]
  role files:    [n] written / [n] declared
  build-verify:  PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-04 -- Combined: PATH label emission as output token + declarative block-shape correctness rules (C-22 + C-23)

**Axis**: Output format + phrasing register (combined)
**Hypothesis**: C-22 and C-23 address orthogonal dimensions: C-22 requires the path
label to appear as an output token at execution point; C-23 requires each named block
to have a declarative correctness rule. V-01 handles C-22 alone; V-02 handles C-23
alone. V-04 combines both on R6 V-02's architecture (STEP labels, PATH-A/PATH-B as
primary structural feature). The combination is non-redundant: PATH label emission
satisfies C-22 by making the branch choice observable; declarative correctness rules
satisfy C-23 by making block validity self-describing. Neither change affects the other.
V-04 also fixes C-08 by adding a declarative AMEND correctness rule.

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
in Step 7. Not regenerated at write time.**

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
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] rows, total = [n]

  RULE: org-chart.md sections 2-4 are copies of ARTIFACT-A, -B, -C. No recalculation.
        No rewrite. Compliance verified via TRANSCRIPTION-RECEIPT in Step 7.
        If any REVISED verdict fires: CHART-PATH: PATH-B applies -- TRANSCRIPTION-CLEAR
        required before CHART-WRITTEN.
        If all VERBATIM on first receipt: CHART-PATH: PATH-A applies -- CHART-WRITTEN
        directly.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

**STEP 5 -- PROFILE**

**Entry**: CONTRACT-GATE. **No files written.**

A correct PROFILE entry contains three fields: `defended-artifact` (a specific named
artifact -- not a category), `change-pressure` (a specific named initiative -- not a
generic force), and `lens-phrase` (5-10 words derived from both; verbatim opening of
this team's IA lens field). A PROFILE entry naming a category rather than a specific
artifact is structurally underspecified.

For each team:

```
PROFILE: [team name]
  defended-artifact:  [specific artifact -- not a category]
  change-pressure:    [specific initiative -- not a generic force]
  lens-phrase:        [5-10 words; verbatim opening of IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

**STEP 6 -- WRITE-IA**

**Entry**: PROFILE-GATE.
**All IA files before any standard or specialized role files.**

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Step 5; 2-3 sentences; no
  generic stability language; phrase not applicable to any team without rewrite
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt contains the team name, the applied lens-phrase, and two
binary checks (opens verbatim, expertise concrete). An IA-WRITTEN receipt missing any
of these is structurally incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 5]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```

Any NO -> rewrite that field before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams.`

---

**STEP 7 -- WRITE-CHART**

**Entry**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels
2. [TRANSCRIBE ARTIFACT-A verbatim]
3. [TRANSCRIBE ARTIFACT-B verbatim]
4. [TRANSCRIBE ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each naming specific mechanisms
drawn from org.yaml: `--area "[name]"` with the area list from ARTIFACT-A; `--levels
"[old]:[new]"` with the level vocabulary in use; `--restructure "[team] > [new-parent]"`
with the current parent > child nesting pairs. An AMEND section with fewer than three
options, or with options that do not cite specific org.yaml values, is structurally
incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

Emit TRANSCRIPTION-RECEIPT immediately after writing org-chart.md.

A correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows (one each for
ARTIFACT-A, ARTIFACT-B, ARTIFACT-C), each showing CONTRACT value, org-chart.md value,
and VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three rows is
structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1: "[phrase]" / org-chart.md sentence-1: "[phrase]"  -- verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
```

**Evaluate the receipt. Emit the path you are entering as the next output line:**

```
CHART-PATH: PATH-A
```
or
```
CHART-PATH: PATH-B
```

**PATH-A execution (emit after CHART-PATH: PATH-A):**
All three verdicts are VERBATIM. No rewrites. No re-audit block required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
For each REVISED artifact:
  1. Rewrite that section in org-chart.md from the sealed CONTRACT artifact.
  2. Update that receipt line: corrected values, verdict changed to VERBATIM.

After all REVISED artifacts have been rewritten, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C) with a VERBATIM verdict for each, in a single pass that
includes artifacts already VERBATIM before any rewrites. A TRANSCRIPTION-CLEAR naming
fewer than three artifacts is structurally incomplete and does not serve as a PATH-B
exit gate. CHART-WRITTEN may not follow PATH-B until TRANSCRIPTION-CLEAR is present
and all three lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm value matches CONTRACT-SEALED]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1-lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  all three confirmed -- PATH-B exit authorized
```

If any artifact shows REVISED in TRANSCRIPTION-CLEAR: return to step 1 of PATH-B.
`CHART-WRITTEN.`

---

**STEP 8 -- WRITE-ROLES**

**Entry**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files. All five fields, no
placeholder text. Scope explicit.

`TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

**STEP 9 -- BUILD-VERIFY**

**Entry**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase from Step 5, the exact IA lens field opening from the
written file, and a VERBATIM/DRIFT verdict. A BUILD-VERIFY block with any content
other than per-team VERBATIM/DRIFT verdict entries is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 5]"
  IA lens field opening:  "[actual first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry.

`BUILD-VERIFY-PASS: [n of n] teams.`
`BUILD-VERIFY-COMPLETE.`

---

**STEP 10 -- CROSS-REF**

**Entry**: BUILD-VERIFY-COMPLETE.

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  IA files:       teams [n], IA files [n] -- MATCH / MISMATCH
  dir check:      areas [list], dirs present [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4)
  contract:      SEALED (headcount=[n], prose=[n] sentences, levels=[n])
  profiles:      [n of n] teams (specific artifact + specific pressure + lens-phrase)
  IA phase:      [n of n] teams written before standard/specialized
  chart-path:    [CHART-PATH: PATH-A -- all VERBATIM, no re-audit |
                  CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR, all three confirmed]
  role files:    [n] written / [n] declared
  build-verify:  PASS -- [n of n] VERBATIM/DRIFT verdicts (no other content in phase)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-05 -- Full integration: PROFILE-before-CONTRACT + PATH label emission + declarative correctness rules (all 15 criteria)

**Axis**: Full integration
**Hypothesis**: R6 V-04 (PROFILE before CONTRACT) produced the deepest C-16 integration
observed across all rounds -- making resistance profiles the causal source of contract
artifacts rather than a parallel preparation step. V-05 takes that architecture and adds
both R7 axes: (1) CHART-PATH: PATH-A / PATH-B emitted as output tokens at execution
point (C-22), and (2) declarative block-shape correctness rules for all named blocks
(C-23), including AMEND (fixing the V-03 R6 C-08 gap). The phase sequence is PARSE ->
VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL -> WRITE-IA -> WRITE-CHART ->
WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF. WRITE-CHART before WRITE-ROLES preserves C-13.
PROFILE before CONTRACT preserves the deepest C-16 coverage while allowing CONTRACT
artifacts to be described as derived from profiles.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

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

`VALIDATE-PASS: 4/4 checks pass. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] error(s). No files written. Halt.`

---

### PHASE 3 -- PROFILE

**Entry condition**: VALIDATE-PASS. **No files written during this phase.**
**Resistance profiles are extracted before the headcount contract is built. The
CONTRACT artifacts in Phase 4 are assembled from these profiles -- not constructed
independently.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (the
specific named system, pipeline, schema, SLA, or procedure this team's Inertia Advocate
would defend -- not a category), `change-pressure` (the specific named initiative,
migration, or architectural shift threatening it -- not a generic force), and
`lens-phrase` (5-10 words derived from both fields, which opens the IA lens field
verbatim). A PROFILE entry whose `defended-artifact` names a category ("data integrity",
"system stability") rather than a specific artifact is structurally underspecified. A
PROFILE entry whose `lens-phrase` cannot be traced back to both `defended-artifact` and
`change-pressure` is structurally ungrounded.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`

Collision check: identical lens phrases -> `LENS-COLLISION: [teams]. Revise one.`

`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

---

### PHASE 4 -- CONTRACT

**Entry condition**: PROFILE-GATE. **No files written during this phase.**
**Three contract artifacts produced from the resistance profiles. Sealed in Phase 5.
Transcribed verbatim into org-chart.md in Phase 7. Not regenerated at write time.**

**CONTRACT ARTIFACT-A -- Headcount table:**

One row per area. Headcount = count of all role slots for that area, including IA roles.
Derived from PROFILE-COMPLETE team and area assignments.

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**CONTRACT ARTIFACT-B -- Analytic prose (2-3 sentences):**

A correct ARTIFACT-B names the largest area by headcount as a percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not derivable from table rows alone. An ARTIFACT-B with language applicable
to any org ("the org has several teams") is structurally deficient.

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

Strong example:
> "Infrastructure carries 12 of 30 total headcount -- the largest area at 40%. Six of
> nine teams declare IC1/IC2 levels; the three product-facing teams have no declared
> level vocabulary. Every team with declared levels maps to Infrastructure, concentrating
> leveling data in one half of the org."

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One seniority sentence referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels). Proceeding to seal.`

---

### PHASE 5 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A (headcount table):    [n] area rows, total headcount = [n]
    first-row lock: "[area name] | [n]"
  ARTIFACT-B (analytic prose):     [n] sentences
    sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C (level distribution): [n] levels, total = [n]

  RULE: These artifacts are FINAL. org-chart.md sections 2-4 are verbatim copies.
        No recalculation. No rewrite. Compliance audited via TRANSCRIPTION-RECEIPT
        in Phase 7. PATH selection at TRANSCRIPTION-RECEIPT determines exit shape:
        all VERBATIM -> CHART-PATH: PATH-A; any REVISED -> CHART-PATH: PATH-B.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: CONTRACT-GATE.
**All Inertia Advocate files written before any standard or specialized role files.**

Path: `.roles/{area-slug}/inertia-advocate.md`

A correct IA role file is a person-portrait: lens and expertise characterize the specific
kind of person who occupies this role on this team, grounded in the Phase 3 resistance
profile. A correct IA role file could not be transplanted to a different team without
substantive rewrite. An IA role file containing generic resistance language ("ensures
process stability", "advocates for continuity") applicable to any team is structurally
deficient.

- **orientation**: from Phase 3 `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the Phase 3 `lens-phrase`; 2-3 sentences; no generic
  stability language; characterizes a specific viewpoint anchored to this team's domain
- **expertise**: names a concrete artifact, system, or practice from `defended-artifact`
  this person would defend -- differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart (the role most likely
  to propose the Phase 3 change-pressure initiative)

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt contains the team name, the applied lens-phrase, and two
binary quality checks. An IA-WRITTEN receipt missing any of these fields is incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 3]"
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
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- do not rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each citing specific values
drawn from org.yaml: option 1 names `--area "[name]"` with the list of available area
names from ARTIFACT-A; option 2 names `--levels "[old]:[new]"` with the level
vocabulary currently in use from org.yaml; option 3 names `--restructure "[team] >
[new-parent]"` with the current parent > child nesting pairs. An AMEND section with
fewer than three options, or with options that do not name specific org.yaml values as
placeholders, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area (resistance profile + IA + all roles + chart row).
   Available areas: [list from ARTIFACT-A headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C), each showing the CONTRACT-SEALED value, the org-chart.md
value, and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three
rows is structurally incomplete.

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

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**

- All three verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`

The `CHART-PATH:` line must appear as an output token before executing the path.

**After emitting CHART-PATH: PATH-A:**
No rewrites occurred. No TRANSCRIPTION-CLEAR block is required.
`CHART-WRITTEN.`

**After emitting CHART-PATH: PATH-B:**
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line to VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts with a VERBATIM
verdict for each, in a single pass that includes artifacts already VERBATIM before any
rewrite. A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally
incomplete and does not serve as a PATH-B exit gate. CHART-WRITTEN may not be emitted
in PATH-B until TRANSCRIPTION-CLEAR is present with all three lines VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm total matches CONTRACT-SEALED first-row lock]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1 lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  all three confirmed -- PATH-B exit authorized
```

If any artifact shows REVISED in TRANSCRIPTION-CLEAR: return to step 1 of PATH-B.
`CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files.
Paths: `.roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.roles/{group-slug}/{role-slug}.md` (shared group),
`.roles/exec-office/{role-slug}.md` (exec office)

All five fields, no placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a Phase 3 profile lens-phrase, the exact IA lens field opening from the
written file, and a single VERBATIM/DRIFT verdict. A BUILD-VERIFY block containing any
content other than per-team VERBATIM/DRIFT verdict entries -- file writes, structural
checks, directory comparisons, headcount verifications, summary rows, or any other
output -- is structurally invalid.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 3 profiles.`
`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

A correct CROSS-REF contains exactly four checks. A CROSS-REF with fewer than four
checks is structurally incomplete.

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
  validate:      PASS (4/4 checks, no files written)
  profiles:      [n of n] teams -- specific artifact + specific pressure + lens-phrase
                 (profiles are causal source of CONTRACT artifacts)
  contract:      SEALED (headcount=[n], analytic prose=[n] sentences, levels=[n])
  IA coverage:   [n of n] teams -- portraits written before standard/specialized
  org-chart.md:  [CHART-PATH: PATH-A -- all VERBATIM, no re-audit required |
                  CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR, all three artifacts confirmed]
  role files:    [n] written / [n] declared
  build-verify:  PASS (single-purpose: [n of n] VERBATIM/DRIFT verdicts, no other content)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```
