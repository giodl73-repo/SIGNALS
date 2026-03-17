---
skill: quest-variate
skill_target: corps-build
round: 9
date: 2026-03-16
rubric_version: 8
---

# Variate R9 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
R8 produced three new criteria (C-24/C-25/C-26) and two 100/100 variations (V-04 and V-05).
R9 uses V-05 R8 as the baseline for all five variations -- every R9 variation starts with
the full C-01 through C-26 architecture and adds one new structural axis.

---

## R8 Status and Candidate C-27 Territory

R8 achieved 100/100 on V-04 and V-05. All 26 criteria are now reachable via V-05 R8.
R9 uses V-05 R8 as the baseline for all five variations. Every variation inherits:

- PHASE-ENTERED / PHASE-EXITED at every boundary (C-24)
- ARTIFACT-D resistance landscape in CONTRACT, audited in TRANSCRIPTION-RECEIPT and
  TRANSCRIPTION-CLEAR (C-25)
- WRITE-ROLES decomposed into PASS-EXEC / PASS-SHARED / PASS-TEAM with per-pass receipts
  and ROLES-COMPLETE aggregation (C-26)
- Declarative block-shape correctness rules for VALIDATE, PROFILE, CONTRACT,
  TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, BUILD-VERIFY, CROSS-REF, AMEND (C-23)
- PATH-A / PATH-B named binary paths in WRITE-CHART (C-22)
- PROFILE-before-CONTRACT ordering (C-16)
- Four-artifact TRANSCRIPTION audit loop (C-25 requirement)

R8 excellence signals not yet extracted as rubric criteria:

| Signal | Source | Gap |
|--------|--------|-----|
| WRITE-CHART section-pass decomposition | All R8: WRITE-CHART writes all six sections in a single undifferentiated block with no named section passes and no per-section receipts | Analogous to C-26 (WRITE-ROLES named passes) but applied to org-chart.md section writing; section coverage cannot be independently verified from the output token stream |
| AMEND structural receipt | All R8: AMEND declares three concrete options (C-08 + C-23) but emits no confirmation token that all three type-tagged option slots are filled | AMEND-RECEIPT closes the C-08 verification loop as a named build output rather than a visual inspection |
| PROFILE expertise derivation seed | All R8: lens-phrase traced through BUILD-VERIFY (C-17); expertise required to be specific (C-15, C-16) but no pre-extracted EXPERTISE-SEED is verified at BUILD-VERIFY time | EXPERTISE-SEED extracted in PROFILE and verified in BUILD-VERIFY alongside LENS-FORMULA closes the expertise derivation loop symmetrically with the lens loop |

Three axes unexplored at the 100-point baseline: **WRITE-CHART section decomposition**,
**AMEND receipt**, and **PROFILE expertise seed + BUILD-VERIFY two-field trace**. R9 makes
each a primary axis.

---

## Variation Axes

| Axis | Variation |
|------|-----------|
| WRITE-CHART section decomposition: PASS-TREE / PASS-CONTRACT / PASS-AMEND / PASS-LANDSCAPE | V-01 |
| AMEND structured receipt: type-tagged options + AMEND-RECEIPT token | V-02 |
| PROFILE expertise seed: EXPERTISE-SEED field + BUILD-VERIFY two-field trace | V-03 |
| WRITE-CHART decomposition + AMEND receipt combined (V-01 + V-02) | V-04 |
| Full integration: all three axes (V-01 + V-02 + V-03) | V-05 |

---

## Key Design Decisions

**V-01 (WRITE-CHART section-pass axis):** WRITE-CHART is decomposed into four named
section passes: PASS-TREE (ASCII hierarchy section), PASS-CONTRACT (sections 2-4:
ARTIFACT-A, ARTIFACT-B, ARTIFACT-C verbatim), PASS-AMEND (AMEND section), and
PASS-LANDSCAPE (ARTIFACT-D resistance landscape verbatim). Each pass emits a dedicated
receipt token: TREE-WRITTEN, CONTRACT-SECTIONS-WRITTEN, AMEND-WRITTEN, LANDSCAPE-WRITTEN.
A gate token SECTIONS-COMPLETE aggregates all four receipts before TRANSCRIPTION-RECEIPT
begins. FINAL SUMMARY org-chart.md row references per-pass receipts plus CHART-PATH.
Orthogonal to C-26 (which applies to WRITE-ROLES): C-26 decomposes role-file writing;
this decomposes org-chart.md section writing. A WRITE-CHART that writes all sections in a
single undifferentiated block is structurally undifferentiated. Base: V-05 R8. No other
changes. Candidate C-27: WRITE-CHART section-pass decomposition with per-pass receipts
and SECTIONS-COMPLETE gate before the verbatim transcription audit.

**V-02 (AMEND receipt axis):** The AMEND section gains structured type tags per option:
[REGENERATE-AREA], [ADJUST-LEVEL], [CHANGE-STRUCTURE]. After writing the AMEND section,
the build emits an AMEND-RECEIPT block confirming that all three type tags are present and
each references specific org.yaml values. A structurally correct AMEND block contains
exactly three options with distinct type tags; a block with fewer than three, repeated type
tags, or options whose values are not drawn from org.yaml is structurally invalid.
AMEND-RECEIPT emits a COMPLETE / INCOMPLETE verdict; INCOMPLETE triggers option rewrite
before AMEND-WRITTEN is confirmed. FINAL SUMMARY adds an amend-receipt row. Orthogonal to
C-08 (which requires three concrete options) and C-23 (which requires a correctness rule
for the block): AMEND-RECEIPT produces a build-time verification token that the three
type-tagged slots are filled, making option coverage structurally auditable. Base: V-05 R8.
No other changes. Candidate C-28: AMEND-RECEIPT with type-tag coverage confirmation.

**V-03 (PROFILE expertise seed + BUILD-VERIFY two-field axis):** The PROFILE format
expands from three fields to four: DOMAIN-ANCHOR (same semantic as `defended-artifact` but
named as a structural key), THREAT-VECTOR (same semantic as `change-pressure`), LENS-FORMULA
(same 5-10-word phrase now explicitly labeled as a formula derived from DOMAIN-ANCHOR and
THREAT-VECTOR), and EXPERTISE-SEED (new: one concrete nameable thing -- a metric name,
file path, SLA value, alert name, procedure title -- that this person would cite by name).
IA role file construction requires expertise to name EXPERTISE-SEED verbatim. BUILD-VERIFY
extends to two-field trace: each team entry verifies both lens opening (against LENS-FORMULA)
and expertise mention (against EXPERTISE-SEED), producing a team verdict of VERBATIM-BOTH /
DRIFT-LENS / DRIFT-EXPERTISE / DRIFT-BOTH. BUILD-VERIFY-PASS requires all teams
VERBATIM-BOTH. Orthogonal to C-17 (which traces only the lens phrase): this closes the
expertise derivation loop with the same structural verification pattern applied to the lens.
Base: V-05 R8. No other changes. Candidate C-29: EXPERTISE-SEED field in PROFILE +
BUILD-VERIFY two-field trace with VERBATIM-BOTH per-team verdict.

**V-04 (WRITE-CHART decomposition + AMEND receipt):** V-05 R8 base with both V-01 and V-02
applied. WRITE-CHART is decomposed into four named section passes; PASS-AMEND gains
type-tagged options and emits AMEND-RECEIPT before confirming AMEND-WRITTEN. SECTIONS-COMPLETE
aggregates all four pass receipts. TRANSCRIPTION-RECEIPT and PATH-A/PATH-B operate on the
assembled org-chart.md as before. Both axes are orthogonal: section passes govern write
coverage tracking; AMEND-RECEIPT governs option type-tag completeness.

**V-05 (full integration):** V-05 R8 base with all three R9 axes. Every writing phase is
decomposed into named passes with receipts (WRITE-CHART: four section passes; WRITE-ROLES:
three role-category passes). Every named block has a structural receipt (TRANSCRIPTION-RECEIPT,
AMEND-RECEIPT). Every derivation is traced through BUILD-VERIFY (lens via LENS-FORMULA,
expertise via EXPERTISE-SEED). Maximum structural density for rubric-extraction signal.

---

## V-01 -- WRITE-CHART section decomposition: named passes with per-pass receipts (C-27 candidate)

**Axis**: WRITE-CHART section decomposition
**Hypothesis**: In all R8 variations, WRITE-CHART writes all six org-chart.md sections in a
single undifferentiated block. There are no named section passes and no per-section receipt
tokens. The section coverage of org-chart.md -- whether ARTIFACT-A was written before
ARTIFACT-B, whether the AMEND section was written before the resistance landscape -- is not
visible from the output token stream until TRANSCRIPTION-RECEIPT audits content after the
fact. V-01 decomposes WRITE-CHART into four named section passes, each with a scope
declaration and a receipt token, gated by SECTIONS-COMPLETE before the verbatim audit
begins. This makes section coverage structurally verifiable without reading section content:
a missing TREE-WRITTEN or LANDSCAPE-WRITTEN token means that section was skipped, not
quietly absent from an aggregate CHART-WRITTEN confirmation.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

### PHASE 1 -- PARSE

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

A correct PARSE block names the org, lists all groups and teams with parent assignments,
lists standard and specialized roles per team, states shared group and exec office roles,
declares levels or "not declared", gives nesting depth and total role slot count. A PARSE
block missing any of these fields is structurally incomplete.

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

### PHASE 2 -- VALIDATE

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

A correct VALIDATE block carries four named checks. A VALIDATE block with fewer than
four checks, or that writes files before all checks pass, is structurally invalid.

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

### PHASE 3 -- PROFILE

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written during this phase.**
**Resistance profiles extracted before CONTRACT is built. ARTIFACT-D (resistance
landscape) in Phase 4 is derived from these profiles -- profiles are the causal source
of both IA role files and the landscape artifact.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (the specific
named system, pipeline, schema, SLA, or procedure this team's IA would defend -- not a
category), `change-pressure` (the specific named initiative, migration, or architectural
shift threatening it -- not a generic force), and `lens-phrase` (5-10 words derived from
both, which opens the IA lens field verbatim). A PROFILE entry naming a category
("data integrity", "system stability") rather than a specific artifact is structurally
underspecified. A PROFILE entry whose lens-phrase cannot be traced to both
`defended-artifact` and `change-pressure` is structurally ungrounded.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
```

Correct example:
```
PROFILE: Data Platform Team
  defended-artifact:  the three-stage ETL validation sequence for nightly order reconciliation
  change-pressure:    migration to streaming ingestion pipeline bypassing batch validation stages
  lens-phrase:        ETL validation stages eliminated by streaming pipeline migration
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

### PHASE 4 -- CONTRACT

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written during this phase.**
**Four contract artifacts produced from profiles and org.yaml structure. Sealed in
Phase 5. ARTIFACT-A through ARTIFACT-C transcribed verbatim into org-chart.md sections
2-4. ARTIFACT-D transcribed verbatim into org-chart.md section 6. Not regenerated.**

A correct CONTRACT phase produces four artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B, produces fewer than 2-3 sentences in ARTIFACT-B, or omits
ARTIFACT-D is structurally incomplete.

**ARTIFACT-A -- Headcount table:**
One row per area. Headcount = all role slots for that area, including IA roles.

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**

A correct ARTIFACT-B names the largest area by headcount as a percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not derivable from table rows alone. An ARTIFACT-B with language applicable
to any org is structurally deficient.

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

**ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One seniority sentence referencing the dominant level.

**ARTIFACT-D -- Resistance landscape table (derived from PROFILE-GATE):**

A correct ARTIFACT-D contains exactly one row per team from PROFILE-COMPLETE, with
the team name, defended-artifact, change-pressure, and lens-phrase transcribed verbatim
from the PROFILE entries. An ARTIFACT-D with fewer rows than teams in PROFILE-COMPLETE
is structurally incomplete. An ARTIFACT-D whose rows do not trace verbatim to
PROFILE-COMPLETE entries is structurally ungrounded.

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact verbatim] | [change-pressure verbatim] | [lens-phrase verbatim] |
```

`LANDSCAPE-CLOSED: [n] team rows -- one per PROFILE-COMPLETE entry, values traced verbatim.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

### PHASE 5 -- CONTRACT-SEAL

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: org-chart.md sections 2-4 are the same content as ARTIFACT-A, -B, -C --
        not rewrites, not reformats. Section 6 is ARTIFACT-D verbatim.
        No recalculation. No rewrite. All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
        PATH-A: all four VERBATIM on first receipt, no re-audit block.
        PATH-B: any REVISED -- TRANSCRIPTION-CLEAR re-audits all four before CHART-WRITTEN.
```

`SEAL-COMPLETE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: SEAL-COMPLETE`

---

### PHASE 6 -- WRITE-IA

`PHASE-ENTERED: WRITE-IA -- precondition: SEAL-COMPLETE`
**All Inertia Advocate files written before any standard or specialized role files.**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. Lens and expertise read as characterizations
of a particular individual's worldview and domain knowledge, not as a filled-in template.
A correct IA role file could not be transplanted to a different team without substantive
rewrite. An IA role file containing generic resistance language ("ensures process
stability", "advocates for continuity", "resists unnecessary change") applicable to any
team is structurally deficient.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Phase 3 -- specific concern
- **lens**: opens verbatim with the Phase 3 `lens-phrase`; 2-3 sentences; no generic
  language; characterizes a specific viewpoint anchored to this team's domain
- **expertise**: names a concrete artifact, system, or practice this person would
  defend -- not a category; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt names the team, confirms the lens-phrase was applied
verbatim, and carries two binary checks. An IA-WRITTEN receipt missing any of these
three fields is structurally incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 3]"
  opens verbatim: YES / NO
  expertise names specific artifact: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-COMPLETE`

---

### PHASE 7 -- WRITE-CHART

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-COMPLETE`

Write org-chart.md in four named section passes. A correct WRITE-CHART phase names all
four passes in fixed order: PASS-TREE before PASS-CONTRACT before PASS-AMEND before
PASS-LANDSCAPE. A WRITE-CHART phase that writes all sections in a single undifferentiated
block -- with no named passes and no per-section receipt tokens -- is structurally
undifferentiated: section coverage cannot be verified from the output token stream
without reading content. A correct SECTIONS-COMPLETE block names all four pass receipt
tokens; a SECTIONS-COMPLETE block naming fewer than four is structurally incomplete.

**PASS-TREE -- ASCII hierarchy (section 1):**
Write section 1: ASCII tree using box-drawing characters. Minimum two nesting levels.
Group names match org.yaml exactly. Team leaf nodes show headcount in parentheses.
`TREE-WRITTEN.`

**PASS-CONTRACT -- Contract artifact sections (sections 2-4):**
Write sections 2, 3, 4 in order:
- Section 2: [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
- Section 3: [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
- Section 4: [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
`CONTRACT-SECTIONS-WRITTEN: ARTIFACT-A (total=[n]) + ARTIFACT-B ([n] sentences) + ARTIFACT-C (total=[n]) transcribed.`

**PASS-AMEND -- AMEND section (section 5):**
Write section 5: three options with specific org.yaml values.

A correct AMEND section contains exactly three options, each citing specific values
drawn from org.yaml: option 1 names `--area` with the area list from ARTIFACT-A;
option 2 names `--levels` with the level vocabulary from org.yaml; option 3 names
`--restructure` with the current parent > child nesting pairs. An AMEND section with
fewer than three options, or with options that give no specific org.yaml values, is
structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area (profiles + IA + roles + chart row).
   Available areas: [list from ARTIFACT-A headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

`AMEND-WRITTEN: 3 options, org.yaml values cited.`

**PASS-LANDSCAPE -- Resistance landscape section (section 6):**
Write section 6: [TRANSCRIBE CONTRACT ARTIFACT-D verbatim -- the resistance landscape].

```markdown
## Resistance Landscape

[ARTIFACT-D table: Team | Defended Artifact | Change Pressure | Lens Phrase]
```

`LANDSCAPE-WRITTEN: ARTIFACT-D ([n] team rows) transcribed.`

`SECTIONS-COMPLETE: TREE-WRITTEN + CONTRACT-SECTIONS-WRITTEN + AMEND-WRITTEN + LANDSCAPE-WRITTEN. All four passes confirmed. Proceeding to TRANSCRIPTION-RECEIPT.`

After SECTIONS-COMPLETE, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly four artifact rows (one each for
ARTIFACT-A, ARTIFACT-B, ARTIFACT-C, ARTIFACT-D), each with the CONTRACT-SEALED value,
the org-chart.md value, and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with
fewer than four rows is structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-D (resistance landscape):
    CONTRACT first-row "[team] | [lens-phrase first 4 words]" |
    org-chart.md first row "[team] | [lens-phrase first 4 words]" | verdict: VERBATIM / REVISED
```

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**
- All four verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`
The `CHART-PATH:` line must appear as an output token before executing the path.

**PATH-A execution (emit after CHART-PATH: PATH-A):**
A correct PATH-A exit contains no TRANSCRIPTION-CLEAR block. All four artifacts are
VERBATIM. No rewrites occurred. No re-audit block is required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
For each REVISED artifact: rewrite that section in org-chart.md from the SEALED CONTRACT
value. Update that receipt row to VERBATIM.

After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all four contract artifacts (ARTIFACT-A through
ARTIFACT-D) -- not only the ones that were rewritten. It is a single-pass re-audit that
confirms every artifact is VERBATIM before CHART-WRITTEN is emitted. A TRANSCRIPTION-CLEAR
naming fewer than four artifacts is structurally incomplete and does not serve as a PATH-B
exit gate. A PATH-B exit that emits CHART-WRITTEN before TRANSCRIPTION-CLEAR is
structurally invalid.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm total matches CONTRACT-SEALED first-row lock]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1 lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  ARTIFACT-D: VERBATIM  [confirm first row matches ARTIFACT-D first-row lock]
  all four confirmed -- PATH-B exit authorized
```

If any artifact shows REVISED in TRANSCRIPTION-CLEAR: rewrite that artifact and
re-emit TRANSCRIPTION-CLEAR covering all four before CHART-WRITTEN.
`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

### PHASE 8 -- WRITE-ROLES

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

A correct WRITE-ROLES phase names three passes in fixed order: PASS-EXEC before
PASS-SHARED before PASS-TEAM. A WRITE-ROLES phase that writes team roles before
completing PASS-EXEC and PASS-SHARED is structurally out of order. A WRITE-ROLES
phase that merges exec, shared, and team role writes into a single undifferentiated
pass is structurally undifferentiated -- role categories cannot be verified independently.

**PASS-EXEC -- Exec office roles:**
Path: `.craft/roles/exec-office/{role-slug}.md`
All five fields. Scope: `exec office`.
For each role: `EXEC-ROLE-WRITTEN: [role-slug].`
If no exec office roles: `EXEC-ROLE-WRITTEN: none declared.`
`EXEC-WRITTEN: [n] exec office role files.`

**PASS-SHARED -- Shared group roles:**
Path: `.craft/roles/{group-slug}/{role-slug}.md`
All five fields. Scope: `shared -- [group name]`.
For each role: `SHARED-ROLE-WRITTEN: [group] / [role-slug].`
If no shared roles: `SHARED-ROLE-WRITTEN: none declared.`
`SHARED-WRITTEN: [n] shared group role files.`

**PASS-TEAM -- Team-level standard and specialized roles:**
Path: `.craft/roles/{area-slug}/{role-slug}.md`
All five fields. Scope: `standard -- present in all teams` or `specialized -- [team name]`.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] team role files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total files.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

### PHASE 9 -- BUILD-VERIFY

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team), each with a
profile lens-phrase from Phase 3, the exact IA lens field opening from the written file,
and a VERBATIM/DRIFT verdict. The block contains nothing else. A BUILD-VERIFY block
containing any content other than per-team VERBATIM/DRIFT verdict entries -- file writes,
structural checks, directory comparisons, headcount verifications, summary rows, or any
other output -- is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3]"
  IA lens field opening:  "[exact first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry
before proceeding.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

### PHASE 10 -- CROSS-REF

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .craft/roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:               PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted in sequence)
  validate:             PASS (4/4 structural checks, no files written)
  profiles:             [n of n] teams (specific artifact + specific pressure + lens-phrase;
                        profiles are causal source of ARTIFACT-D and IA role files)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim from PROFILE;
                        section 6 of org-chart.md
  IA coverage:          [n of n] teams -- all portraits written before standard/specialized
  org-chart.md:         SECTIONS-COMPLETE: TREE + CONTRACT-SECTIONS + AMEND + LANDSCAPE
                        [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared (all three passes named)
  build-verify:         PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-02 -- AMEND structured receipt: type-tagged options + AMEND-RECEIPT token (C-28 candidate)

**Axis**: AMEND structured receipt
**Hypothesis**: In all R8 variations, the AMEND section declares three concrete options
(satisfying C-08) and the section has a declarative correctness rule (C-23). However,
no variation emits a build-time verification token that all three option slots are filled
with distinct type tags referencing specific org.yaml values. A model can write an AMEND
section that looks structurally correct without the build ever asserting that all three
type-tagged slots are present. V-02 adds [REGENERATE-AREA], [ADJUST-LEVEL], and
[CHANGE-STRUCTURE] type tags to each AMEND option and emits AMEND-RECEIPT after writing
the section -- a named block that assigns a PRESENT/MISSING verdict to each type tag and
emits an overall COMPLETE/INCOMPLETE verdict. INCOMPLETE triggers option rewrite before
AMEND-WRITTEN is confirmed. This closes the C-08 verification loop as a structural output
token rather than a visual inspection. Base: V-05 R8. The only change is Phase 7's AMEND
section format and the addition of AMEND-RECEIPT before AMEND-WRITTEN.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

### PHASE 1 -- PARSE

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

A correct PARSE block names the org, lists all groups and teams with parent assignments,
lists standard and specialized roles per team, states shared group and exec office roles,
declares levels or "not declared", gives nesting depth and total role slot count. A PARSE
block missing any of these fields is structurally incomplete.

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

### PHASE 2 -- VALIDATE

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

A correct VALIDATE block carries four named checks. A VALIDATE block with fewer than
four checks, or that writes files before all checks pass, is structurally invalid.

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

### PHASE 3 -- PROFILE

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written during this phase.**
**Resistance profiles extracted before CONTRACT is built. ARTIFACT-D (resistance
landscape) in Phase 4 is derived from these profiles.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (specific
named artifact -- not a category), `change-pressure` (specific named initiative -- not
a generic force), and `lens-phrase` (5-10 words derived from both; verbatim opening of
this team's IA lens field). A PROFILE entry naming a category is structurally
underspecified. A PROFILE entry whose lens-phrase cannot be traced to both fields is
structurally ungrounded.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

### PHASE 4 -- CONTRACT

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written during this phase.**
**Four contract artifacts produced. Sealed in Phase 5. Transcribed verbatim in Phase 7.**

A correct CONTRACT phase produces four artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B or omits ARTIFACT-D is structurally incomplete.

**ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

**ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

**ARTIFACT-D -- Resistance landscape table (derived from PROFILE-GATE):**

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact verbatim] | [change-pressure verbatim] | [lens-phrase verbatim] |
```

`LANDSCAPE-CLOSED: [n] team rows -- one per PROFILE-COMPLETE entry.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

### PHASE 5 -- CONTRACT-SEAL

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: org-chart.md sections 2-4 are the same content as ARTIFACT-A, -B, -C.
        Section 6 is ARTIFACT-D verbatim. No recalculation. No rewrite.
        All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
        PATH-A: all four VERBATIM on first receipt, no re-audit block.
        PATH-B: any REVISED -- TRANSCRIPTION-CLEAR re-audits all four before CHART-WRITTEN.
```

`SEAL-COMPLETE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: SEAL-COMPLETE`

---

### PHASE 6 -- WRITE-IA

`PHASE-ENTERED: WRITE-IA -- precondition: SEAL-COMPLETE`
**All Inertia Advocate files written before any standard or specialized role files.**

A correct IA role file is a person-portrait. An IA role file containing generic resistance
language applicable to any team is structurally deficient.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Phase 3 -- specific concern
- **lens**: opens verbatim with Phase 3 `lens-phrase`; 2-3 sentences; no generic language
- **expertise**: names a concrete artifact this person would defend -- not a category;
  differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 3]"
  opens verbatim: YES / NO
  expertise names specific artifact: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-COMPLETE`

---

### PHASE 7 -- WRITE-CHART

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-COMPLETE`

Write org-chart.md with six sections:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section (structured -- see below)
6. [TRANSCRIBE CONTRACT ARTIFACT-D verbatim -- resistance landscape table]

**AMEND section -- structured with type-tagged options:**

A correct AMEND block contains exactly three options with distinct type tags
([REGENERATE-AREA], [ADJUST-LEVEL], [CHANGE-STRUCTURE]), each referencing specific
org.yaml values. An AMEND block with fewer than three options, repeated type tags, or
options whose values are not drawn from org.yaml is structurally invalid.

```markdown
## AMEND
1. [REGENERATE-AREA] --area "[area name]" -- regenerate that area (profiles + IA + roles + chart row).
   Available areas: [list from ARTIFACT-A headcount table]
2. [ADJUST-LEVEL] --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. [CHANGE-STRUCTURE] --restructure "[team] > [new-parent]" -- move team, rename directory, redraw.
   Current nesting: [parent > child pairs from org.yaml]
```

After writing the AMEND section, emit AMEND-RECEIPT.

A correct AMEND-RECEIPT assigns a PRESENT/MISSING verdict to each of the three required
type tags and emits an overall COMPLETE/INCOMPLETE verdict. An AMEND-RECEIPT missing any
type-tag row is structurally incomplete. An AMEND-RECEIPT that emits COMPLETE when any
type tag shows MISSING is structurally inconsistent.

```
AMEND-RECEIPT:
  [REGENERATE-AREA]:   option 1 -- area=[area name from ARTIFACT-A] -- PRESENT / MISSING
  [ADJUST-LEVEL]:      option 2 -- levels=[list from org.yaml] -- PRESENT / MISSING
  [CHANGE-STRUCTURE]:  option 3 -- nesting=[parent > child from org.yaml] -- PRESENT / MISSING
  verdict: COMPLETE (3/3) / INCOMPLETE ([n]/3 -- missing: [list])
```

If INCOMPLETE: rewrite missing options and reemit AMEND-RECEIPT before proceeding.
`AMEND-WRITTEN: COMPLETE (3/3 type-tagged options, org.yaml values cited).`

After writing org-chart.md (all six sections, AMEND-RECEIPT COMPLETE), emit
TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly four artifact rows (ARTIFACT-A through
ARTIFACT-D), each with the CONTRACT-SEALED value, the org-chart.md value, and a
VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than four rows is
structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-D (resistance landscape):
    CONTRACT first-row "[team] | [lens-phrase first 4 words]" |
    org-chart.md first row "[team] | [lens-phrase first 4 words]" | verdict: VERBATIM / REVISED
```

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**
- All four verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`

**PATH-A execution (emit after CHART-PATH: PATH-A):**
All four verdicts VERBATIM. No rewrites. No TRANSCRIPTION-CLEAR required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
For each REVISED artifact: rewrite that section from the SEALED CONTRACT value.
Update that receipt row to VERBATIM. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all four contract artifacts with VERBATIM for each,
in a single pass including artifacts already VERBATIM. A TRANSCRIPTION-CLEAR with fewer
than four artifacts is structurally incomplete. CHART-WRITTEN may not follow PATH-B until
TRANSCRIPTION-CLEAR confirms all four.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  ARTIFACT-D: VERBATIM
  all four confirmed -- PATH-B exit authorized
```

`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

### PHASE 8 -- WRITE-ROLES

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

Three passes in fixed order: PASS-EXEC before PASS-SHARED before PASS-TEAM.

**PASS-EXEC:** `.craft/roles/exec-office/{role-slug}.md`. Scope: `exec office`.
`EXEC-ROLE-WRITTEN: [role-slug].` (or `none declared`)
`EXEC-WRITTEN: [n] exec office role files.`

**PASS-SHARED:** `.craft/roles/{group-slug}/{role-slug}.md`. Scope: `shared -- [group]`.
`SHARED-ROLE-WRITTEN: [group] / [role-slug].` (or `none declared`)
`SHARED-WRITTEN: [n] shared group role files.`

**PASS-TEAM:** `.craft/roles/{area-slug}/{role-slug}.md`. Scope: explicit per role.
`TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] team role files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total files.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

### PHASE 9 -- BUILD-VERIFY

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team), each with a
profile lens-phrase from Phase 3, the exact IA lens field opening from the written file,
and a VERBATIM/DRIFT verdict. The block contains nothing else. A BUILD-VERIFY block
containing any content other than per-team VERBATIM/DRIFT verdict entries is structurally
invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3]"
  IA lens field opening:  "[exact first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

### PHASE 10 -- CROSS-REF

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

A correct CROSS-REF contains four checks. Fewer than four is structurally incomplete.

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .craft/roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:               PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted in sequence)
  validate:             PASS (4/4 structural checks, no files written)
  profiles:             [n of n] teams (specific artifact + specific pressure + lens-phrase;
                        profiles are causal source of ARTIFACT-D and IA role files)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim; section 6
  IA coverage:          [n of n] teams -- all portraits written before standard/specialized
  org-chart.md:         [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  amend-receipt:        COMPLETE (3/3: [REGENERATE-AREA] | [ADJUST-LEVEL] | [CHANGE-STRUCTURE])
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared (all three passes named)
  build-verify:         PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-03 -- PROFILE expertise seed: EXPERTISE-SEED field + BUILD-VERIFY two-field trace (C-29 candidate)

**Axis**: PROFILE expertise seed + BUILD-VERIFY two-field trace
**Hypothesis**: All R8 variations trace the lens-phrase derivation through BUILD-VERIFY
(C-17): the profile lens-phrase is extracted in PROFILE, the IA lens field is written
from it in WRITE-IA, and BUILD-VERIFY confirms the lens field opens with the exact
profile phrase. The expertise field follows a parallel design -- it must name a concrete
artifact (C-15, C-16) -- but there is no pre-extracted expertise seed and no BUILD-VERIFY
check that the specific seed appears in the written expertise field. The lens loop is
closed; the expertise loop is not. V-03 adds EXPERTISE-SEED as a fourth field in PROFILE
(a single concrete nameable thing: a metric name, file path, SLA value, alert name, or
procedure title this person would cite by name), requires that expertise field includes
EXPERTISE-SEED verbatim, and extends BUILD-VERIFY to trace both lens (against the
lens-phrase) and expertise (against EXPERTISE-SEED), producing a team verdict of
VERBATIM-BOTH / DRIFT-LENS / DRIFT-EXPERTISE / DRIFT-BOTH. BUILD-VERIFY-PASS requires
all teams VERBATIM-BOTH.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

### PHASE 1 -- PARSE

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

### PHASE 2 -- VALIDATE

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

### PHASE 3 -- PROFILE

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written during this phase.**
**Four-field resistance profiles extracted before CONTRACT is built. ARTIFACT-D is
derived from the first three fields. EXPERTISE-SEED populates the expertise field of
each IA role file and is verified at BUILD-VERIFY time.**

A correct PROFILE entry contains exactly four fields. A PROFILE entry missing
EXPERTISE-SEED is structurally incomplete. A PROFILE entry where EXPERTISE-SEED names
a category ("data quality", "system health") rather than a specific nameable thing is
structurally underspecified -- a correct EXPERTISE-SEED names something a person could
point to: a specific file path, metric name, SLA value, alert rule, or procedure title.

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
  expertise-seed:     [one concrete nameable thing this person would cite by name:
                       a metric, SLA, file path, alert rule, or procedure title]
```

Correct example:
```
PROFILE: Observability Team
  defended-artifact:  the p99_latency_ms SLA of 200ms in the service-contracts/api.yaml
  change-pressure:    migration to async trace aggregation removing synchronous SLA checks
  lens-phrase:        p99 SLA boundary eliminated by async trace aggregation
  expertise-seed:     service-contracts/api.yaml (p99_latency_ms: 200ms)
```

Incorrect (do not produce):
```
PROFILE: Observability Team
  defended-artifact:  system reliability
  change-pressure:    rapid change
  lens-phrase:        defending observability standards
  expertise-seed:     monitoring practices
```

`PROFILE-COMPLETE: [n of n] teams.`
`  Lens phrases:    [team: "phrase", one per line]`
`  Expertise seeds: [team: "seed", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

### PHASE 4 -- CONTRACT

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written during this phase.**
**Four contract artifacts. ARTIFACT-D derived from first three PROFILE fields.
EXPERTISE-SEED is a PROFILE output used in WRITE-IA and BUILD-VERIFY -- not in ARTIFACT-D.**

A correct CONTRACT phase produces four artifacts before any file is written.

**ARTIFACT-A -- Headcount table:**

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

**ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

**ARTIFACT-D -- Resistance landscape table (derived from PROFILE first three fields):**

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact verbatim] | [change-pressure verbatim] | [lens-phrase verbatim] |
```

Note: EXPERTISE-SEED is not in ARTIFACT-D -- it is a derivation seed for IA role files,
verified independently at BUILD-VERIFY.

`LANDSCAPE-CLOSED: [n] team rows.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

### PHASE 5 -- CONTRACT-SEAL

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: org-chart.md sections 2-4 are the same content as ARTIFACT-A, -B, -C.
        Section 6 is ARTIFACT-D verbatim. No recalculation. No rewrite.
        All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
        PATH-A: all four VERBATIM. PATH-B: any REVISED -- TRANSCRIPTION-CLEAR required.
```

`SEAL-COMPLETE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: SEAL-COMPLETE`

---

### PHASE 6 -- WRITE-IA

`PHASE-ENTERED: WRITE-IA -- precondition: SEAL-COMPLETE`
**All Inertia Advocate files written before any standard or specialized role files.**
**lens opens verbatim with lens-phrase from Phase 3. expertise names expertise-seed
from Phase 3. Both are verified at BUILD-VERIFY (Phase 9).**

A correct IA role file is a person-portrait. An IA file containing generic resistance
language is structurally deficient.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Phase 3
- **lens**: opens verbatim with Phase 3 `lens-phrase`; no generic language
- **expertise**: names Phase 3 `expertise-seed` verbatim; not a category; team-specific
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

A correct IA-WRITTEN receipt confirms lens-phrase applied, checks lens verbatim,
and confirms expertise-seed named. An IA-WRITTEN receipt missing any of these three
fields is structurally incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied:   "[phrase from Phase 3]"
  opens verbatim:        YES / NO
  expertise-seed named:  "[seed from Phase 3]" -- present in expertise field: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-COMPLETE`

---

### PHASE 7 -- WRITE-CHART

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-COMPLETE`

Write org-chart.md with six sections:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section
6. [TRANSCRIBE CONTRACT ARTIFACT-D verbatim -- resistance landscape]

A correct AMEND section contains exactly three options citing specific org.yaml values.
An AMEND section with fewer than three options or generic values is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

```markdown
## Resistance Landscape

[ARTIFACT-D table: Team | Defended Artifact | Change Pressure | Lens Phrase]
```

Emit TRANSCRIPTION-RECEIPT after writing org-chart.md.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B: CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-D: CONTRACT first-row "[team] | [lens-phrase first 4 words]" |
              org-chart.md first row "[team] | [lens-phrase first 4 words]" | verdict: VERBATIM / REVISED
```

- All four VERBATIM: emit `CHART-PATH: PATH-A` then `CHART-WRITTEN.`
- Any REVISED: emit `CHART-PATH: PATH-B`, rewrite REVISED sections, emit TRANSCRIPTION-CLEAR.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  ARTIFACT-D: VERBATIM
  all four confirmed -- PATH-B exit authorized
```

`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

### PHASE 8 -- WRITE-ROLES

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

Three passes in fixed order: PASS-EXEC, PASS-SHARED, PASS-TEAM.

**PASS-EXEC:** exec office roles. `EXEC-WRITTEN: [n] files.`
**PASS-SHARED:** shared group roles. `SHARED-WRITTEN: [n] files.`
**PASS-TEAM:** team-level roles. After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

### PHASE 9 -- BUILD-VERIFY

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team). Each entry
carries four named verification fields (lens-phrase, IA lens opening, lens verdict,
expertise-seed, IA expertise mention, expertise verdict) and one team verdict. The block
contains nothing else. A BUILD-VERIFY block containing any content other than per-team
verdict entries -- file writes, structural checks, headcount checks, summary rows, or
any other output -- is structurally invalid. A BUILD-VERIFY entry missing the expertise
verification fields is structurally incomplete: the expertise loop is not closed.

BUILD-VERIFY-PASS requires all teams to show VERBATIM-BOTH. A team showing DRIFT-LENS,
DRIFT-EXPERTISE, or DRIFT-BOTH is not BUILD-VERIFY-PASS eligible until the drifted
field(s) are rewritten.

```
BUILD-VERIFY: [team name]
  lens-phrase:          "[from Phase 3 PROFILE]"
  IA lens opening:      "[exact first phrase in written .craft/roles/ file]"
  lens verdict:         VERBATIM / DRIFT
  expertise-seed:       "[from Phase 3 PROFILE]"
  IA expertise mention: "[excerpt from written .craft/roles/ file where seed appears]"
  expertise verdict:    VERBATIM / DRIFT
  team verdict:         VERBATIM-BOTH / DRIFT-LENS / DRIFT-EXPERTISE / DRIFT-BOTH
```

On DRIFT-LENS: rewrite IA lens field to open with lens-phrase verbatim.
On DRIFT-EXPERTISE: rewrite IA expertise field to name expertise-seed verbatim.
On DRIFT-BOTH: rewrite both fields.
After each rewrite: reemit that team's BUILD-VERIFY entry with corrected values and
VERBATIM-BOTH verdict before proceeding to the next team.

`BUILD-VERIFY-PASS: [n of n] teams VERBATIM-BOTH. Both lens-phrase and expertise-seed confirmed.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

### PHASE 10 -- CROSS-REF

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .craft/roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:               PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted in sequence)
  validate:             PASS (4/4 structural checks, no files written)
  profiles:             [n of n] teams (defended-artifact + change-pressure + lens-phrase
                        + expertise-seed; profiles are causal source of ARTIFACT-D,
                        IA lens fields, and IA expertise fields)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim; section 6
  IA coverage:          [n of n] teams -- portraits written before standard/specialized
  org-chart.md:         [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared
  build-verify:         PASS ([n of n] teams VERBATIM-BOTH -- two-field: lens-phrase + expertise-seed)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-04 -- Combined: WRITE-CHART section decomposition + AMEND receipt (V-01 + V-02)

**Axis**: WRITE-CHART section decomposition + AMEND structured receipt combined
**Hypothesis**: V-01 (section passes) and V-02 (AMEND-RECEIPT) are orthogonal: section
passes govern WRITE-CHART coverage tracking; AMEND-RECEIPT governs AMEND option type-tag
completeness. V-04 combines both on V-05 R8 base. PASS-AMEND within WRITE-CHART's
section-pass structure gains type-tagged options and emits AMEND-RECEIPT before confirming
AMEND-WRITTEN. SECTIONS-COMPLETE aggregates all four pass receipts (including the now-richer
AMEND-WRITTEN). TRANSCRIPTION-RECEIPT and PATH-A/PATH-B operate on the assembled file.
Neither axis affects the other structural invariants.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

### PHASE 1 -- PARSE

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

### PHASE 2 -- VALIDATE

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

A correct VALIDATE block carries four named checks. Fewer than four is structurally invalid.

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

### PHASE 3 -- PROFILE

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written. Resistance profiles extracted before CONTRACT. ARTIFACT-D derived
from these profiles.**

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

### PHASE 4 -- CONTRACT

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written. Four artifacts. Sealed in Phase 5. Transcribed verbatim in Phase 7.**

**ARTIFACT-A -- Headcount table:**
```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```
`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label or note its absence
- Sentence 3: structural observation not derivable from table rows alone

**ARTIFACT-C -- Level distribution table + seniority sentence.**
```markdown
| Level | Count | % of Org |
|-------|-------|----------|
| [label] | [n] | [n]%   |
| **Total** | **[n]** | 100% |
```

**ARTIFACT-D -- Resistance landscape (derived from PROFILE-GATE):**
```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [verbatim] | [verbatim] | [verbatim] |
```
`LANDSCAPE-CLOSED: [n] team rows.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

### PHASE 5 -- CONTRACT-SEAL

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: sections 2-4 of org-chart.md are ARTIFACT-A, -B, -C verbatim. Section 6 is
        ARTIFACT-D verbatim. All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
        PATH-A: all four VERBATIM. PATH-B: any REVISED -- TRANSCRIPTION-CLEAR required.
```

`SEAL-COMPLETE: four artifacts sealed. [n] files to produce.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: SEAL-COMPLETE`

---

### PHASE 6 -- WRITE-IA

`PHASE-ENTERED: WRITE-IA -- precondition: SEAL-COMPLETE`
**All IA files before any standard/specialized role files.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`
- **lens**: opens verbatim with Phase 3 lens-phrase; no generic language
- **expertise**: concrete, team-specific, not a category
- **scope**: `standard -- present in all teams`

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 3]"
  opens verbatim: YES / NO
  expertise names specific artifact: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams.`

`PHASE-EXITED: WRITE-IA -- gate: IA-COMPLETE`

---

### PHASE 7 -- WRITE-CHART

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-COMPLETE`

Write org-chart.md in four named section passes. A correct WRITE-CHART phase names all
four passes in fixed order. A WRITE-CHART phase that writes sections without named passes
and per-section receipts is structurally undifferentiated. A correct SECTIONS-COMPLETE
block names all four pass receipt tokens; fewer than four is structurally incomplete.

**PASS-TREE -- ASCII hierarchy (section 1):**
Box-drawing characters. Minimum two nesting levels. Group names match org.yaml exactly.
Team leaf nodes show headcount in parentheses.
`TREE-WRITTEN.`

**PASS-CONTRACT -- Contract artifact sections (sections 2-4):**
- Section 2: [TRANSCRIBE ARTIFACT-A verbatim]
- Section 3: [TRANSCRIBE ARTIFACT-B verbatim]
- Section 4: [TRANSCRIBE ARTIFACT-C verbatim + seniority sentence]
`CONTRACT-SECTIONS-WRITTEN: ARTIFACT-A (total=[n]) + ARTIFACT-B ([n] sentences) + ARTIFACT-C (total=[n]) transcribed.`

**PASS-AMEND -- AMEND section (section 5) with type-tagged options and AMEND-RECEIPT:**

A correct AMEND block names exactly three options with distinct type tags
([REGENERATE-AREA], [ADJUST-LEVEL], [CHANGE-STRUCTURE]) referencing specific org.yaml
values. An AMEND block with repeated type tags or generic values is structurally invalid.

```markdown
## AMEND
1. [REGENERATE-AREA] --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A]
2. [ADJUST-LEVEL] --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. [CHANGE-STRUCTURE] --restructure "[team] > [new-parent]" -- move team, redraw.
   Current nesting: [parent > child pairs from org.yaml]
```

```
AMEND-RECEIPT:
  [REGENERATE-AREA]:   option 1 -- area=[name from ARTIFACT-A] -- PRESENT / MISSING
  [ADJUST-LEVEL]:      option 2 -- levels=[list from org.yaml] -- PRESENT / MISSING
  [CHANGE-STRUCTURE]:  option 3 -- nesting=[parent > child] -- PRESENT / MISSING
  verdict: COMPLETE (3/3) / INCOMPLETE ([n]/3 -- missing: [list])
```

If INCOMPLETE: rewrite missing options and reemit AMEND-RECEIPT before proceeding.
`AMEND-WRITTEN: COMPLETE (3/3 type-tagged, org.yaml values cited).`

**PASS-LANDSCAPE -- Resistance landscape section (section 6):**
[TRANSCRIBE ARTIFACT-D verbatim]

```markdown
## Resistance Landscape

[ARTIFACT-D table: Team | Defended Artifact | Change Pressure | Lens Phrase]
```

`LANDSCAPE-WRITTEN: ARTIFACT-D ([n] team rows) transcribed.`

`SECTIONS-COMPLETE: TREE-WRITTEN + CONTRACT-SECTIONS-WRITTEN + AMEND-WRITTEN + LANDSCAPE-WRITTEN. All four passes confirmed. Proceeding to TRANSCRIPTION-RECEIPT.`

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B: CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C: CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-D: CONTRACT first-row "[team] | [4 words]" | org-chart.md first row "[team] | [4 words]" | verdict: VERBATIM / REVISED
```

- All four VERBATIM: `CHART-PATH: PATH-A` then `CHART-WRITTEN.`
- Any REVISED: `CHART-PATH: PATH-B`, rewrite, then TRANSCRIPTION-CLEAR.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  ARTIFACT-D: VERBATIM
  all four confirmed -- PATH-B exit authorized
```

`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

### PHASE 8 -- WRITE-ROLES

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

**PASS-EXEC:** exec office roles. `EXEC-WRITTEN: [n] files.`
**PASS-SHARED:** shared group roles. `SHARED-WRITTEN: [n] files.`
**PASS-TEAM:** team-level roles. `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

### PHASE 9 -- BUILD-VERIFY

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

Single-purpose phase. Contains only per-team VERBATIM/DRIFT verdict entries.
Any other content is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3]"
  IA lens field opening:  "[exact first phrase in written file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens verbatim from profile phrase. Reemit VERBATIM entry.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

### PHASE 10 -- CROSS-REF

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .craft/roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:               PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted in sequence)
  validate:             PASS (4/4 structural checks, no files written)
  profiles:             [n of n] teams (specific artifact + specific pressure + lens-phrase;
                        profiles are causal source of ARTIFACT-D and IA role files)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim; section 6
  IA coverage:          [n of n] teams -- portraits written before standard/specialized
  org-chart.md:         SECTIONS-COMPLETE: TREE + CONTRACT-SECTIONS + AMEND + LANDSCAPE
                        [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  amend-receipt:        COMPLETE (3/3: [REGENERATE-AREA] | [ADJUST-LEVEL] | [CHANGE-STRUCTURE])
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared
  build-verify:         PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-05 -- Full integration: all three R9 axes (V-01 + V-02 + V-03)

**Axis**: Full integration
**Hypothesis**: V-01 (WRITE-CHART section passes), V-02 (AMEND-RECEIPT), and V-03
(EXPERTISE-SEED + BUILD-VERIFY two-field) are mutually orthogonal. V-05 R8 was the
highest-signal architecture for rubric extraction; V-05 R9 extends that baseline with
all three new structural patterns. Every writing phase decomposes into named passes with
receipts (WRITE-CHART: four section passes; WRITE-ROLES: three role-category passes).
Every named block has a structural receipt (TRANSCRIPTION-RECEIPT four-artifact, AMEND-RECEIPT
three-tag, BUILD-VERIFY per-team two-field). Every derivation is closed at BUILD-VERIFY
(lens via lens-phrase, expertise via EXPERTISE-SEED). Maximum structural density for
candidate criterion extraction in R10.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next phase begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

### PHASE 1 -- PARSE

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

A correct PARSE block names the org, lists all groups and teams with parent assignments,
standard and specialized roles per team, shared group and exec office roles, declared
levels, nesting depth, and total role slot count. A PARSE block missing any of these
fields is structurally incomplete.

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

### PHASE 2 -- VALIDATE

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

A correct VALIDATE block carries four named checks. A VALIDATE block with fewer than
four checks, or that writes files before all checks pass, is structurally invalid.

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- offenders: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

### PHASE 3 -- PROFILE

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written during this phase.**
**Four-field resistance profiles extracted before CONTRACT is built. ARTIFACT-D is
derived from the first three fields. EXPERTISE-SEED populates the expertise field of
each IA role file and is verified at BUILD-VERIFY time. Profiles are the causal source
of ARTIFACT-D, IA lens fields, and IA expertise fields.**

A correct PROFILE entry contains exactly four named fields. A PROFILE entry missing
EXPERTISE-SEED is structurally incomplete. A PROFILE entry where EXPERTISE-SEED names
a category rather than a specific nameable thing is structurally underspecified. A
correct EXPERTISE-SEED names something a person could point to: a specific file path,
metric name, SLA value, alert rule, or procedure title.

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
  expertise-seed:     [one concrete nameable thing: metric, SLA, file path, alert, or
                       procedure title -- this person would cite this by name]
```

Correct example:
```
PROFILE: Reliability Team
  defended-artifact:  the error-budget policy document governing 99.95% monthly uptime SLA
  change-pressure:    adoption of feature-flag-driven deploys removing release freeze windows
  lens-phrase:        error-budget policy eroded by feature-flag deploy cadence
  expertise-seed:     reliability/error-budget-policy.md (section 4: burn-rate thresholds)
```

`PROFILE-COMPLETE: [n of n] teams.`
`  Lens phrases:    [team: "phrase", one per line]`
`  Expertise seeds: [team: "seed", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

### PHASE 4 -- CONTRACT

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written during this phase.**
**Four contract artifacts produced from profiles and org.yaml structure. Sealed in
Phase 5. ARTIFACT-A through ARTIFACT-C transcribed verbatim into org-chart.md sections
2-4. ARTIFACT-D transcribed verbatim into org-chart.md section 6. Not regenerated.
EXPERTISE-SEED is not in ARTIFACT-D -- it is a derivation seed for IA role files,
verified independently at BUILD-VERIFY.**

A correct CONTRACT phase produces four artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B, produces fewer than 2-3 sentences in ARTIFACT-B, or omits
ARTIFACT-D is structurally incomplete.

**ARTIFACT-A -- Headcount table:**
One row per area. Headcount = all role slots including IA roles.

```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**

A correct ARTIFACT-B names the largest area by headcount as percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not derivable from table rows alone. An ARTIFACT-B with generic language
applicable to any org is structurally deficient.

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

**ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One seniority sentence referencing the dominant level.

**ARTIFACT-D -- Resistance landscape table (derived from PROFILE first three fields):**

A correct ARTIFACT-D contains exactly one row per team from PROFILE-COMPLETE, with
defended-artifact, change-pressure, and lens-phrase transcribed verbatim. An ARTIFACT-D
with fewer rows than PROFILE-COMPLETE teams is structurally incomplete.

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact verbatim] | [change-pressure verbatim] | [lens-phrase verbatim] |
```

`LANDSCAPE-CLOSED: [n] team rows -- one per PROFILE-COMPLETE entry, values traced verbatim.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

### PHASE 5 -- CONTRACT-SEAL

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: org-chart.md sections 2-4 are the same content as ARTIFACT-A, -B, -C --
        not rewrites, not reformats. Section 6 is ARTIFACT-D verbatim.
        No recalculation. No rewrite. All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
        PATH-A: all four VERBATIM on first receipt, no re-audit block.
        PATH-B: any REVISED -- TRANSCRIPTION-CLEAR re-audits all four before CHART-WRITTEN.
```

`SEAL-COMPLETE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: SEAL-COMPLETE`

---

### PHASE 6 -- WRITE-IA

`PHASE-ENTERED: WRITE-IA -- precondition: SEAL-COMPLETE`
**All Inertia Advocate files written before any standard or specialized role files.**
**lens opens verbatim with lens-phrase from Phase 3. expertise names expertise-seed
from Phase 3. Both verified at BUILD-VERIFY (Phase 9).**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. An IA role file containing generic resistance
language applicable to any team is structurally deficient. An IA role file could not
be transplanted to a different team without substantive rewrite.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Phase 3 -- specific concern
- **lens**: opens verbatim with Phase 3 `lens-phrase`; 2-3 sentences; no generic
  language; viewpoint anchored to this team's domain
- **expertise**: names Phase 3 `expertise-seed` verbatim; concrete -- not a category;
  differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt confirms lens-phrase applied, checks lens verbatim,
and confirms expertise-seed named. An IA-WRITTEN receipt missing any of these three
verification fields is structurally incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied:   "[phrase from Phase 3]"
  opens verbatim:        YES / NO
  expertise-seed named:  "[seed from Phase 3]" -- present in expertise field: YES / NO
```
Any NO -> rewrite before proceeding.

`IA-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-COMPLETE`

---

### PHASE 7 -- WRITE-CHART

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-COMPLETE`

Write org-chart.md in four named section passes. A correct WRITE-CHART phase names all
four passes in fixed order: PASS-TREE before PASS-CONTRACT before PASS-AMEND before
PASS-LANDSCAPE. A WRITE-CHART phase that writes all sections in a single undifferentiated
block is structurally undifferentiated -- section coverage cannot be verified from the
output token stream. A correct SECTIONS-COMPLETE block names all four pass receipt tokens;
a SECTIONS-COMPLETE block naming fewer than four is structurally incomplete.

**PASS-TREE -- ASCII hierarchy (section 1):**
Box-drawing characters, minimum two nesting levels. Group names match org.yaml exactly.
Team leaf nodes show headcount in parentheses.
`TREE-WRITTEN.`

**PASS-CONTRACT -- Contract artifact sections (sections 2-4):**
- Section 2: [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
- Section 3: [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
- Section 4: [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
`CONTRACT-SECTIONS-WRITTEN: ARTIFACT-A (total=[n]) + ARTIFACT-B ([n] sentences) + ARTIFACT-C (total=[n]) transcribed.`

**PASS-AMEND -- AMEND section (section 5) with type-tagged options and AMEND-RECEIPT:**

A correct AMEND block names exactly three options with distinct type tags
([REGENERATE-AREA], [ADJUST-LEVEL], [CHANGE-STRUCTURE]), each referencing specific
org.yaml values. An AMEND block with fewer than three options, repeated type tags, or
options not drawn from org.yaml is structurally invalid.

```markdown
## AMEND
1. [REGENERATE-AREA] --area "[area name]" -- regenerate that area (profiles + IA + roles + chart row).
   Available areas: [list from ARTIFACT-A headcount table]
2. [ADJUST-LEVEL] --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. [CHANGE-STRUCTURE] --restructure "[team] > [new-parent]" -- move team, rename directory, redraw.
   Current nesting: [parent > child pairs from org.yaml]
```

After writing AMEND section, emit AMEND-RECEIPT.

A correct AMEND-RECEIPT assigns a PRESENT/MISSING verdict to each of the three required
type tags and emits an overall COMPLETE/INCOMPLETE verdict. An AMEND-RECEIPT with fewer
than three type-tag rows is structurally incomplete. An AMEND-RECEIPT emitting COMPLETE
when any tag shows MISSING is structurally inconsistent.

```
AMEND-RECEIPT:
  [REGENERATE-AREA]:   option 1 -- area=[area name from ARTIFACT-A] -- PRESENT / MISSING
  [ADJUST-LEVEL]:      option 2 -- levels=[list from org.yaml] -- PRESENT / MISSING
  [CHANGE-STRUCTURE]:  option 3 -- nesting=[parent > child from org.yaml] -- PRESENT / MISSING
  verdict: COMPLETE (3/3) / INCOMPLETE ([n]/3 -- missing: [list])
```

If INCOMPLETE: rewrite missing options and reemit AMEND-RECEIPT before proceeding.
`AMEND-WRITTEN: COMPLETE (3/3 type-tagged options, org.yaml values cited).`

**PASS-LANDSCAPE -- Resistance landscape section (section 6):**
[TRANSCRIBE CONTRACT ARTIFACT-D verbatim]

```markdown
## Resistance Landscape

[ARTIFACT-D table: Team | Defended Artifact | Change Pressure | Lens Phrase]
```

`LANDSCAPE-WRITTEN: ARTIFACT-D ([n] team rows) transcribed.`

`SECTIONS-COMPLETE: TREE-WRITTEN + CONTRACT-SECTIONS-WRITTEN + AMEND-WRITTEN + LANDSCAPE-WRITTEN. All four passes confirmed. Proceeding to TRANSCRIPTION-RECEIPT.`

After SECTIONS-COMPLETE, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly four artifact rows (one each for
ARTIFACT-A, ARTIFACT-B, ARTIFACT-C, ARTIFACT-D), each with the CONTRACT-SEALED value,
the org-chart.md value, and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with
fewer than four rows is structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1 "[phrase]" | org-chart.md sentence-1 "[phrase]" | verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total [n] | org-chart.md total [n] | verdict: VERBATIM / REVISED
  ARTIFACT-D (resistance landscape):
    CONTRACT first-row "[team] | [lens-phrase first 4 words]" |
    org-chart.md first row "[team] | [lens-phrase first 4 words]" | verdict: VERBATIM / REVISED
```

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**
- All four verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`
The `CHART-PATH:` line must appear as an output token before executing the path.

**PATH-A execution (emit after CHART-PATH: PATH-A):**
A correct PATH-A exit contains no TRANSCRIPTION-CLEAR block. All four artifacts are
VERBATIM. No rewrites occurred. No re-audit block is required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
For each REVISED artifact: rewrite that section in org-chart.md from the SEALED CONTRACT
value. Update that receipt row to VERBATIM. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all four contract artifacts -- not only the ones
that were rewritten. Single-pass re-audit confirming every artifact VERBATIM before
CHART-WRITTEN. A TRANSCRIPTION-CLEAR naming fewer than four artifacts is structurally
incomplete and does not serve as a PATH-B exit gate.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM  [confirm total matches CONTRACT-SEALED first-row lock]
  ARTIFACT-B: VERBATIM  [confirm sentence-1 matches sentence-1 lock]
  ARTIFACT-C: VERBATIM  [confirm total matches CONTRACT-SEALED]
  ARTIFACT-D: VERBATIM  [confirm first row matches ARTIFACT-D first-row lock]
  all four confirmed -- PATH-B exit authorized
```

If any artifact shows REVISED in TRANSCRIPTION-CLEAR: rewrite and re-emit covering all
four before CHART-WRITTEN.
`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

### PHASE 8 -- WRITE-ROLES

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

A correct WRITE-ROLES phase names three passes in fixed order: PASS-EXEC before
PASS-SHARED before PASS-TEAM. A WRITE-ROLES phase that writes team roles before
completing PASS-EXEC and PASS-SHARED is structurally out of order. A WRITE-ROLES
phase merging all role writes into a single undifferentiated pass is structurally
undifferentiated.

**PASS-EXEC -- Exec office roles:**
Path: `.craft/roles/exec-office/{role-slug}.md`
All five fields. Scope: `exec office`.
For each role: `EXEC-ROLE-WRITTEN: [role-slug].`
If no exec office roles: `EXEC-ROLE-WRITTEN: none declared.`
`EXEC-WRITTEN: [n] exec office role files.`

**PASS-SHARED -- Shared group roles:**
Path: `.craft/roles/{group-slug}/{role-slug}.md`
All five fields. Scope: `shared -- [group name]`.
For each role: `SHARED-ROLE-WRITTEN: [group] / [role-slug].`
If no shared roles: `SHARED-ROLE-WRITTEN: none declared.`
`SHARED-WRITTEN: [n] shared group role files.`

**PASS-TEAM -- Team-level standard and specialized roles:**
Path: `.craft/roles/{area-slug}/{role-slug}.md`
All five fields. Scope: `standard -- present in all teams` or `specialized -- [team name]`.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] team role files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total files.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

### PHASE 9 -- BUILD-VERIFY

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team). Each entry carries
four named verification fields (lens-phrase, IA lens opening, lens verdict, expertise-seed,
IA expertise mention, expertise verdict) and one team verdict. The block contains nothing
else. A BUILD-VERIFY block containing any content other than per-team verdict entries --
file writes, structural checks, directory comparisons, headcount verifications, summary
rows, or any other output -- is structurally invalid. A BUILD-VERIFY entry missing the
expertise verification fields (expertise-seed, IA expertise mention, expertise verdict) is
structurally incomplete: the expertise derivation loop is not closed.

BUILD-VERIFY-PASS requires all teams VERBATIM-BOTH. A team showing DRIFT-LENS,
DRIFT-EXPERTISE, or DRIFT-BOTH is not BUILD-VERIFY-PASS eligible until the drifted
field(s) are rewritten.

```
BUILD-VERIFY: [team name]
  lens-phrase:          "[from Phase 3 PROFILE]"
  IA lens opening:      "[exact first phrase in written .craft/roles/ file]"
  lens verdict:         VERBATIM / DRIFT
  expertise-seed:       "[from Phase 3 PROFILE]"
  IA expertise mention: "[excerpt from written .craft/roles/ file where seed appears]"
  expertise verdict:    VERBATIM / DRIFT
  team verdict:         VERBATIM-BOTH / DRIFT-LENS / DRIFT-EXPERTISE / DRIFT-BOTH
```

On DRIFT-LENS: rewrite IA lens field to open with lens-phrase verbatim.
On DRIFT-EXPERTISE: rewrite IA expertise field to name expertise-seed verbatim.
On DRIFT-BOTH: rewrite both fields.
After rewrite: reemit that team's BUILD-VERIFY entry with corrected values and
VERBATIM-BOTH before proceeding.

`BUILD-VERIFY-PASS: [n of n] teams VERBATIM-BOTH. Two-field: lens-phrase + expertise-seed both confirmed.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

### PHASE 10 -- CROSS-REF

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .craft/roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  stages:               PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted in sequence)
  validate:             PASS (4/4 structural checks, no files written)
  profiles:             [n of n] teams (defended-artifact + change-pressure + lens-phrase
                        + expertise-seed; profiles are causal source of ARTIFACT-D,
                        IA lens fields, and IA expertise fields)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim from PROFILE;
                        section 6 of org-chart.md
  IA coverage:          [n of n] teams -- all portraits written before standard/specialized
  org-chart.md:         SECTIONS-COMPLETE: TREE + CONTRACT-SECTIONS + AMEND + LANDSCAPE
                        [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  amend-receipt:        COMPLETE (3/3: [REGENERATE-AREA] | [ADJUST-LEVEL] | [CHANGE-STRUCTURE])
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared (all three passes named)
  build-verify:         PASS ([n of n] teams VERBATIM-BOTH -- two-field: lens-phrase + expertise-seed)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```
