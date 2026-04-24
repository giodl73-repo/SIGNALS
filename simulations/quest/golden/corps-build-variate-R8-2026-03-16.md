---
skill: quest-variate
skill_target: corps-build
round: 8
date: 2026-03-16
rubric_version: 7
---

# Variate R8 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
R7 produced two 100/100 variations (V-04 and V-05). R8 explores three new axes to
surface candidate criteria for a potential rubric v8.

---

## R7 Status and Candidate C-24 Territory

R7 achieved perfect score on two variations (V-04: C-22+C-23 combined; V-05: full
integration with PROFILE-before-CONTRACT). All 23 criteria are now reachable.

R7 excellence signals not yet extracted as rubric criteria:

| Signal | Source | Gap |
|--------|--------|-----|
| Exhaustive invalidity enumeration | V-05 R7 Signal 4: BUILD-VERIFY names every prohibited content type ("file writes, structural checks, directory comparisons, headcount verifications, summary rows, or any other output"); V-04 uses "nothing else" shorthand | Differentiator within the 100-point space -- but not yet scored |
| Causal chain trace in FINAL SUMMARY | V-05 R7 Signal 5: "profiles are causal source of CONTRACT artifacts" named explicitly in FINAL SUMMARY | V-04 does not trace the causal chain -- traces execution sequence only |
| Phase lifecycle visibility | Not present in R7 | PHASE-ENTERED / PHASE-EXITED tokens make entry/exit preconditions structural assertions; no variation has explored this axis |
| Resistance landscape as org artifact | Not present in R7 | PROFILE-derived resistance landscape in org-chart.md transcribed and verified like headcount table; no variation has explored this axis |

Three axes unexplored at 100-point baseline: **lifecycle emphasis**,
**inertia framing**, and **role sequence**. R8 makes each a primary axis.

---

## Variation Axes

| Axis | Variation |
|------|-----------|
| Lifecycle emphasis: PHASE-ENTERED / PHASE-EXITED at every boundary | V-01 |
| Inertia framing: RESISTANCE-LANDSCAPE as ARTIFACT-D transcribed to org-chart.md | V-02 |
| Role sequence: named write passes (PASS-EXEC, PASS-SHARED, PASS-TEAM) in WRITE-ROLES | V-03 |
| Lifecycle emphasis + inertia framing combined (PROFILE-before-CONTRACT base) | V-04 |
| Full integration: V-05 R7 base + all three axes | V-05 |

---

## Key Design Decisions

**V-01 (lifecycle axis):** Every phase opens with `PHASE-ENTERED: [name] -- precondition:
[token]` before any work begins and closes with `PHASE-EXITED: [name] -- gate: [token]`
after the gate is emitted. A PHASE-ENTERED declares the precondition satisfied;
PHASE-EXITED names the gate produced. A phase that emits PHASE-EXITED without a
preceding PHASE-ENTERED in the same output block is structurally invalid. FINAL SUMMARY
adds a `phase-trace:` row listing all 10 phase names in sequence confirming all
PHASE-ENTERED / PHASE-EXITED tokens were emitted. Base: V-04 R7. No other changes.
Candidate C-24: named phase-lifecycle tokens as structural precondition assertions.

**V-02 (inertia framing axis):** On V-05 R7's PROFILE-before-CONTRACT architecture,
CONTRACT adds ARTIFACT-D: a compact resistance landscape table derived from the PROFILE
entries (one row per team with defended-artifact, change-pressure, lens-phrase). SEAL
covers all four artifacts. org-chart.md gains a sixth section: RESISTANCE-LANDSCAPE
(after AMEND), transcribed verbatim from ARTIFACT-D. TRANSCRIPTION-RECEIPT audits all
four artifacts. TRANSCRIPTION-CLEAR re-audits all four. FINAL SUMMARY leads with
`resistance-landscape: [n of n] teams -- transcribed verbatim from PROFILE`. This makes
the Inertia Advocate's systemic role visible at the document level.
Candidate C-25: resistance landscape as a PROFILE-derived transcribed org-chart artifact.

**V-03 (role sequence axis):** WRITE-ROLES splits into three named write passes on V-04
R7's architecture: PASS-EXEC (exec office roles, if any), PASS-SHARED (shared group
roles, if any), PASS-TEAM (team-level standard and specialized roles). Each pass has its
own receipt token: EXEC-WRITTEN, SHARED-WRITTEN, TEAM-WRITTEN. ROLES-COMPLETE
aggregates all three. A correct WRITE-ROLES phase names all three passes in order; a
WRITE-ROLES that writes team roles before resolving exec and shared roles is structurally
out of order. Candidate C-26: named role-category write passes with per-category receipts.

**V-04 (lifecycle + inertia framing):** V-04 R7 step architecture adapted to
PROFILE-before-CONTRACT ordering (required for ARTIFACT-D derivation from profiles) plus
PHASE-ENTERED/PHASE-EXITED at every boundary. Phase sequence: PARSE -> VALIDATE ->
PROFILE -> CONTRACT -> CONTRACT-SEAL -> WRITE-IA -> WRITE-CHART -> WRITE-ROLES ->
BUILD-VERIFY -> CROSS-REF. ARTIFACT-D added to CONTRACT. Declarative correctness rules
from V-04 R7 preserved. CHART-PATH emission preserved.

**V-05 (full integration):** V-05 R7 base (PROFILE-before-CONTRACT, declarative rules,
CHART-PATH emission) plus all three R8 axes: PHASE-ENTERED/PHASE-EXITED lifecycle tokens,
ARTIFACT-D resistance landscape, named write passes in WRITE-ROLES. Deepest integration:
every phase has lifecycle tokens, resistance landscape in org-chart.md with four-artifact
TRANSCRIPTION-RECEIPT, role categories isolated in three named write passes.

---

## V-01 -- Lifecycle emphasis: PHASE-ENTERED / PHASE-EXITED at every phase boundary (C-24 candidate)

**Axis**: Lifecycle emphasis
**Hypothesis**: V-04 and V-05 R7 use gate tokens (PARSE-PASS, VALIDATE-PASS, etc.) to
order phases but do not separate the entry-condition assertion from the exit-condition
assertion as distinct structural tokens. A model executing phases correctly may emit gate
tokens in sequence without ever naming the precondition it satisfied to enter a phase.
PHASE-ENTERED and PHASE-EXITED make entry preconditions and exit gates structurally
visible: PHASE-ENTERED declares what satisfied entry; PHASE-EXITED names the gate
produced. A phase that emits PHASE-EXITED without PHASE-ENTERED is structurally invalid
because the entry precondition is unasserted. A FINAL SUMMARY phase-trace confirms all
10 phases completed their lifecycle tokens in sequence. No other structural change from
V-04 R7 -- this is a pure lifecycle-emphasis axis.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Step sequence**: PARSE -> VALIDATE -> CONTRACT -> CONTRACT-SEAL -> PROFILE ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED in the same output
block is structurally invalid.

---

**STEP 1 -- PARSE**

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

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
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

**STEP 2 -- VALIDATE**

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written during this phase.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

**STEP 3 -- CONTRACT**

`PHASE-ENTERED: CONTRACT -- precondition: VALIDATE-PASS`
**No files written during this phase.**
**Three contract artifacts. Sealed in Step 4. Transcribed verbatim into org-chart.md
in Step 7. Not regenerated at write time.**

A correct CONTRACT phase produces three artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B, or that produces fewer than 2-3 analytic sentences in
ARTIFACT-B, is structurally incomplete.

**ARTIFACT-A -- Headcount table:**
```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```
One row per area. Total = sum of all area rows.
`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
A correct ARTIFACT-B names the largest area by headcount as a percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not readable from the table rows alone. An ARTIFACT-B with generic language
applicable to any org is structurally deficient.

Strong example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml, suggesting the org has not yet leveled its management layer. The three product
> teams each carry two specialized roles, a higher ratio than any infrastructure team."

Weak (do not produce):
> "The org has several teams with different headcount. Level distribution is shown below."

**ARTIFACT-C -- Level distribution table + seniority sentence.**
```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```
One sentence on seniority profile referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

**STEP 4 -- CONTRACT-SEAL**

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] area rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]

  RULE: org-chart.md sections 2-4 are verbatim copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite. Audited via TRANSCRIPTION-RECEIPT in Step 7.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: CONTRACT-GATE`

---

**STEP 5 -- PROFILE**

`PHASE-ENTERED: PROFILE -- precondition: CONTRACT-GATE`
**No files written during this phase.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (a specific
named system, schema, pipeline, SLA, or procedure -- not a category), `change-pressure`
(a specific named migration, initiative, or shift -- not a generic force), and
`lens-phrase` (5-10 words derived from both fields; verbatim opening of this team's IA
lens field). A PROFILE entry naming a category rather than a specific artifact is
structurally underspecified.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific artifact -- not a category]
  change-pressure:    [specific initiative -- not a generic force]
  lens-phrase:        [5-10 words; verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

`PHASE-EXITED: PROFILE -- gate: PROFILE-GATE`

---

**STEP 6 -- WRITE-IA**

`PHASE-ENTERED: WRITE-IA -- precondition: PROFILE-GATE`
**All Inertia Advocate files written before any standard or specialized role files.**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. An IA role file containing generic resistance
language ("ensures process stability", "advocates for continuity", "resists unnecessary
change") applicable to any team is structurally deficient.

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Step 5; 2-3 sentences;
  no generic stability language; phrase not applicable to any team without rewrite
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA;
  names a concrete artifact, system, or practice -- not a category
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt names the team, confirms the lens-phrase was applied, and
carries two binary checks. An IA-WRITTEN receipt missing any of these is structurally
incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 5]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite that field before proceeding to next team.

`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-PHASE-COMPLETE`

---

**STEP 7 -- WRITE-CHART**

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-PHASE-COMPLETE`

Write org-chart.md. Sections in order:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each naming specific mechanisms
drawn from org.yaml: (1) `--area "[name]"` with the list of available area names from
the headcount table; (2) `--levels "[old]:[new]"` with the level vocabulary currently
in use; (3) `--restructure "[team] > [new-parent]"` with the current parent > child
nesting pairs. An AMEND section with fewer than three options, or with options that give
no specific org.yaml values as placeholders, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area (resistance profile + IA + roles + chart row).
   Available areas: [list from headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

Emit TRANSCRIPTION-RECEIPT immediately after writing org-chart.md.

A correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C), each showing the CONTRACT-SEALED value, the org-chart.md value,
and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three artifact
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

**Evaluate the receipt. Emit the path you are entering as the next output line:**
- All three verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`
The `CHART-PATH:` line must appear as an output token before executing the path.

**PATH-A execution (emit after CHART-PATH: PATH-A):**
All three verdicts VERBATIM. No rewrites. No TRANSCRIPTION-CLEAR block required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line: corrected values, verdict VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts with a VERBATIM
verdict for each, in a single pass that includes artifacts already VERBATIM before
the rewrite. A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally
incomplete and does not serve as a PATH-B exit gate. CHART-WRITTEN may not follow
PATH-B until TRANSCRIPTION-CLEAR is present and all three lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  all three confirmed -- CHART-WRITTEN authorized
```

If any artifact shows REVISED in this re-audit: return to step 1 of PATH-B.
`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

**STEP 8 -- WRITE-ROLES**

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

Standard, specialized, shared group, and exec office role files.
Paths: `.roles/{area-slug}/{role-slug}.md` (standard and specialized),
`.roles/{group-slug}/{role-slug}.md` (shared group),
`.roles/exec-office/{role-slug}.md` (exec office)

All five fields, no placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

**STEP 9 -- BUILD-VERIFY**

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase, an IA lens field opening, and a single VERBATIM/DRIFT
verdict. A BUILD-VERIFY block containing any content other than per-team VERBATIM/DRIFT
verdict entries -- file writes, structural checks, directory comparisons, headcount
verifications, summary rows, or any other output -- is structurally invalid.

For each team:

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 5]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

If DRIFT: rewrite IA lens field to open with profile phrase verbatim. Reemit that
team's BUILD-VERIFY block showing VERBATIM before proceeding to next team.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Step 5 profiles.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

**STEP 10 -- CROSS-REF**

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

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

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

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
  phase-trace:   PARSE(entered/exited) -> VALIDATE(entered/exited) ->
                 CONTRACT(entered/exited) -> CONTRACT-SEAL(entered/exited) ->
                 PROFILE(entered/exited) -> WRITE-IA(entered/exited) ->
                 WRITE-CHART(entered/exited) -> WRITE-ROLES(entered/exited) ->
                 BUILD-VERIFY(entered/exited) -> CROSS-REF(entered/exited)
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-02 -- Inertia framing: RESISTANCE-LANDSCAPE as ARTIFACT-D transcribed to org-chart.md (C-25 candidate)

**Axis**: Inertia framing
**Hypothesis**: In all R7 variations, the PROFILE phase data exists only in three places:
the PROFILE blocks in phase output, the IA-WRITTEN receipts, and the BUILD-VERIFY
verdicts. The resistance profiles never appear as a unified artifact in the final
deliverable -- org-chart.md contains only headcount, prose, levels, and AMEND, not the
Inertia Advocate landscape. V-02 adds ARTIFACT-D: a compact resistance landscape table
(one row per team with defended-artifact, change-pressure, and lens-phrase) produced in
the CONTRACT phase from the already-complete PROFILE entries. SEAL covers all four
artifacts. org-chart.md gains a sixth section (RESISTANCE-LANDSCAPE) transcribed verbatim
from ARTIFACT-D. TRANSCRIPTION-RECEIPT audits all four artifacts. TRANSCRIPTION-CLEAR
re-audits all four. FINAL SUMMARY leads with the resistance landscape row. This makes the
IA's systemic role visible at the org-chart level rather than distributed across individual
role files. Base: V-05 R7 (PROFILE-before-CONTRACT ordering, deepest C-16 integration).
No path-label or correctness-rule changes -- this is a pure inertia-framing axis.

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

---

### PHASE 3 -- PROFILE

**Entry condition**: VALIDATE-PASS. **No files written during this phase.**
**Resistance profiles are extracted before CONTRACT is built. CONTRACT ARTIFACT-D
(resistance landscape) is derived from these profiles.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (the specific
named system, pipeline, schema, SLA, or procedure this team's IA would defend -- not a
category), `change-pressure` (the specific named initiative, migration, or shift that
threatens it -- not a generic force), and `lens-phrase` (5-10 words derived from both,
which opens the IA lens field verbatim). A PROFILE entry naming a category rather than a
specific artifact is structurally underspecified. A PROFILE entry whose lens-phrase does
not trace to both `defended-artifact` and `change-pressure` is structurally ungrounded.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific named artifact -- not a category]
  change-pressure:    [specific named initiative -- not a generic force]
  lens-phrase:        [5-10 words derived from both; verbatim opening of IA lens field]
```

Correct example:
```
PROFILE: Platform Team
  defended-artifact:  the circuit-breaker configuration governing three downstream services
  change-pressure:    migration to async event bus eliminating synchronous fallback paths
  lens-phrase:        circuit-breaker thresholds erased by async event bus migration
```

Incorrect (do not produce):
```
PROFILE: Platform Team
  defended-artifact:  system stability
  change-pressure:    rapid change
  lens-phrase:        defending platform reliability against disruption
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. [n] teams. Proceeding to CONTRACT.`

---

### PHASE 4 -- CONTRACT

**Entry condition**: PROFILE-GATE. **No files written during this phase.**
**Four contract artifacts produced from profiles and org.yaml structure. Sealed in
Phase 5. ARTIFACT-A through ARTIFACT-C transcribed verbatim into org-chart.md sections
2-4. ARTIFACT-D transcribed verbatim into org-chart.md section 6. Not regenerated.**

**CONTRACT ARTIFACT-A -- Headcount table:**

One row per area. Headcount = all role slots for that area, including IA roles.

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
to any org is structurally deficient.

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

**CONTRACT ARTIFACT-C -- Level distribution table + seniority sentence.**

```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```

One seniority sentence referencing the dominant level.

**CONTRACT ARTIFACT-D -- Resistance landscape table:**

Derived from PROFILE-COMPLETE entries. One row per team. A correct ARTIFACT-D names
every team from PROFILE-COMPLETE with its defended-artifact and lens-phrase. An
ARTIFACT-D with fewer rows than teams in PROFILE-COMPLETE is structurally incomplete.

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact from PROFILE] | [change-pressure from PROFILE] | [lens-phrase from PROFILE] |
```

`LANDSCAPE-CLOSED: [n] team rows, one per team from PROFILE-COMPLETE.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

---

### PHASE 5 -- CONTRACT-SEAL

**Entry condition**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [defended-artifact first 5 words]"

  RULE: org-chart.md sections 2-4 are verbatim copies of ARTIFACT-A, -B, -C.
        org-chart.md section 6 is a verbatim copy of ARTIFACT-D.
        No recalculation. No rewrite. All four audited via TRANSCRIPTION-RECEIPT in Phase 7.
```

`CONTRACT-GATE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

---

### PHASE 6 -- WRITE-IA

**Entry condition**: CONTRACT-GATE.
**All Inertia Advocate files written before any standard or specialized role files.**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. An IA role file containing generic resistance
language ("ensures process stability", "advocates for continuity", "resists unnecessary
change") applicable to any team is structurally deficient.

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: grounded in `defended-artifact` from Phase 3 -- specific concern
- **lens**: opens verbatim with the Phase 3 `lens-phrase`; 2-3 sentences; no generic
  language; characterizes a specific viewpoint anchored to this team's domain
- **expertise**: names a concrete artifact, system, or practice this person would
  defend -- not a category; differs from every other team's IA
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Phase 3]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams. All IA files written before standard/specialized roles.`

---

### PHASE 7 -- WRITE-CHART

**Entry condition**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each citing specific values
drawn from org.yaml: option 1 names `--area` with the area list from ARTIFACT-A;
option 2 names `--levels` with the level vocabulary from org.yaml; option 3 names
`--restructure` with the current parent > child nesting pairs. An AMEND section with
fewer than three options, or with options that give no specific org.yaml values, is
structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

6. [TRANSCRIBE CONTRACT ARTIFACT-D verbatim -- the resistance landscape table]

```markdown
## Resistance Landscape

[ARTIFACT-D table: Team | Defended Artifact | Change Pressure | Lens Phrase]
```

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT.

A correct TRANSCRIPTION-RECEIPT contains exactly four artifact rows (ARTIFACT-A through
ARTIFACT-D), each showing the CONTRACT-SEALED value, the org-chart.md value, and a
VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than four rows is
structurally incomplete.

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
  ARTIFACT-D (resistance landscape):
    CONTRACT first-row lock: "[team name] | [defended-artifact first 5 words]"
    org-chart.md first row:  "[team name] | [defended-artifact first 5 words]"
    verdict: VERBATIM / REVISED
```

**Immediately after TRANSCRIPTION-RECEIPT, emit the path you are entering:**
- All four verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`
The `CHART-PATH:` line must appear as an output token before executing the path.

**PATH-A execution (emit after CHART-PATH: PATH-A):**
All four verdicts VERBATIM. No rewrites. No TRANSCRIPTION-CLEAR block required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
1. For each REVISED verdict: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line: corrected values, verdict VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all four contract artifacts (ARTIFACT-A through
ARTIFACT-D) with a VERBATIM verdict for each, in a single pass that includes artifacts
already VERBATIM before the rewrite. A TRANSCRIPTION-CLEAR naming fewer than four
artifacts is structurally incomplete and does not serve as a PATH-B exit gate.
CHART-WRITTEN may not follow PATH-B until TRANSCRIPTION-CLEAR is present and all four
lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  ARTIFACT-D: VERBATIM
  all four confirmed -- CHART-WRITTEN authorized
```

If any artifact shows REVISED in this re-audit: return to step 1 of PATH-B.
`CHART-WRITTEN.`

---

### PHASE 8 -- WRITE-ROLES

**Entry condition**: CHART-WRITTEN.

Standard, specialized, shared group, and exec office role files. All five fields, no
placeholder text. Scope field explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

`TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

---

### PHASE 9 -- BUILD-VERIFY

**Entry condition**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase from Phase 3, the exact IA lens field opening from the
written file, and a VERBATIM/DRIFT verdict. A BUILD-VERIFY block containing any content
other than per-team VERBATIM/DRIFT verdict entries -- file writes, structural checks,
directory comparisons, headcount verifications, summary rows, or any other output --
is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Phase 3]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry
before proceeding.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Phase 3 profiles.`
`BUILD-VERIFY-COMPLETE.`

---

### PHASE 10 -- CROSS-REF

**Entry condition**: BUILD-VERIFY-COMPLETE.

A correct CROSS-REF contains four checks. A CROSS-REF with fewer than four checks is
structurally incomplete.

```
CROSS-REF:
  slots:          org.yaml [n] == files written [n] -- MATCH / MISMATCH
  IA coverage:    teams [n] == IA files [n] -- MATCH / MISMATCH
  directories:    org.yaml areas [list] == .roles/ dirs [list] -- MATCH / MISMATCH
  table fidelity: CONTRACT-SEALED total [n] == org-chart.md total [n] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS.` Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:             PASS (4/4 structural checks)
  profiles:             [n of n] teams (specific artifact + pressure + lens-phrase;
                        profiles are causal source of CONTRACT artifacts)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim from PROFILE
  IA coverage:          [n of n] teams -- all portraits written before standard/specialized
  org-chart.md:         [CHART-PATH: PATH-A -- all four VERBATIM, no re-audit required |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  role files:           [n] written / [n] declared
  build-verify:         PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-03 -- Role sequence: named write passes (PASS-EXEC, PASS-SHARED, PASS-TEAM) in WRITE-ROLES (C-26 candidate)

**Axis**: Role sequence
**Hypothesis**: In all R7 variations, WRITE-ROLES is a single undifferentiated phase.
Exec office roles, shared group roles, and team-level roles are written in an unspecified
order with only per-team TEAM-WRITTEN receipts. No variation names exec office and shared
group as distinct write passes with their own receipts. V-03 splits WRITE-ROLES into three
named passes: PASS-EXEC (exec office roles), PASS-SHARED (shared group roles), PASS-TEAM
(team-level standard and specialized roles). Each pass has a dedicated receipt token
(EXEC-WRITTEN, SHARED-WRITTEN, TEAM-WRITTEN-ALL). Passes run in fixed order:
PASS-EXEC before PASS-SHARED before PASS-TEAM. A WRITE-ROLES phase that writes team roles
before completing exec and shared passes is structurally out of order. ROLES-COMPLETE
aggregates all three. A correct WRITE-ROLES phase names all three passes and their receipt
tokens. A WRITE-ROLES phase that merges exec, shared, and team writes into a single pass
is structurally undifferentiated. Base: V-04 R7. No other changes.

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

A correct CONTRACT phase produces three artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B or produces fewer than 2-3 sentences in ARTIFACT-B is
structurally incomplete.

**ARTIFACT-A -- Headcount table:**
```markdown
| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```
One row per area. Total = sum of all area rows.
`TABLE-CLOSED: [n] area rows, headcount total = [n].`

**ARTIFACT-B -- Analytic prose (2-3 sentences):**
A correct ARTIFACT-B names the largest area by headcount as a percentage of total,
names the dominant level label or notes its absence, and states one structural
observation not readable from the table rows alone. An ARTIFACT-B with generic language
applicable to any org is structurally deficient.

Strong example:
> "Platform Engineering carries 9 of 22 total headcount -- the largest area at 41%. All
> five Platform teams declare IC levels, but no management level vocabulary appears in
> org.yaml. The three product teams each carry two specialized roles, a higher ratio than
> any infrastructure team."

**ARTIFACT-C -- Level distribution table + seniority sentence.**
```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```
One seniority sentence referencing the dominant level.

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels).`

---

**STEP 4 -- CONTRACT-SEAL**

**Entry**: CONTRACT-DRAFT.

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] area rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]

  RULE: org-chart.md sections 2-4 are verbatim copies of ARTIFACT-A, -B, -C.
        No recalculation. No rewrite. Audited via TRANSCRIPTION-RECEIPT in Step 7.
```

`CONTRACT-GATE: artifacts sealed. [n] files to produce. Proceeding to PROFILE.`

---

**STEP 5 -- PROFILE**

**Entry**: CONTRACT-GATE. **No files written.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (a specific
named artifact -- not a category), `change-pressure` (a specific named initiative -- not
a generic force), and `lens-phrase` (5-10 words derived from both; verbatim opening of
this team's IA lens field). A PROFILE entry naming a category rather than a specific
artifact is structurally underspecified.

For every team:

```
PROFILE: [team name]
  defended-artifact:  [specific artifact -- not a category]
  change-pressure:    [specific initiative -- not a generic force]
  lens-phrase:        [5-10 words; verbatim opening of this team's IA lens field]
```

`PROFILE-COMPLETE: [n of n] teams. Lens phrases: [team: "phrase", one per line]`
Collision: `LENS-COLLISION: [teams]. Revise one.` (if applicable)
`PROFILE-GATE: distinct profiles confirmed. Proceeding to WRITE-IA.`

---

**STEP 6 -- WRITE-IA**

**Entry**: PROFILE-GATE.
**All IA files written before any standard or specialized role files.**

A correct IA role file is a person-portrait. An IA role file containing generic
resistance language applicable to any team is structurally deficient.

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Step 5; 2-3 sentences; no
  generic stability language; phrase not applicable to any team without rewrite
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA;
  names a concrete artifact -- not a category
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

A correct IA-WRITTEN receipt names the team, confirms the lens-phrase was applied, and
carries two binary checks. An IA-WRITTEN receipt missing any of these is structurally
incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 5]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized roles.`

---

**STEP 7 -- WRITE-CHART**

**Entry**: IA-PHASE-COMPLETE.

Write org-chart.md. Sections in order:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section

A correct AMEND section contains exactly three options, each naming specific mechanisms
drawn from org.yaml: (1) `--area "[name]"` with the area list; (2) `--levels "[old]:[new]"`
with the level vocabulary in use; (3) `--restructure "[team] > [new-parent]"` with the
current parent > child pairs. An AMEND section with fewer than three options, or with
options that give no specific org.yaml values, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area (resistance profile + IA + roles + chart row).
   Available areas: [list from headcount table]
2. --levels "[old]:[new]" -- replace level vocabulary throughout.
   Levels in use: [list from org.yaml]
3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
   Current nesting: [parent > child pairs from org.yaml]
```

Emit TRANSCRIPTION-RECEIPT after writing org-chart.md.

A correct TRANSCRIPTION-RECEIPT contains exactly three artifact rows (ARTIFACT-A,
ARTIFACT-B, ARTIFACT-C), each showing the CONTRACT-SEALED value, the org-chart.md value,
and a VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than three rows is
structurally incomplete.

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

**Evaluate the receipt. Emit the path you are entering as the next output line:**
- All three verdicts VERBATIM: emit `CHART-PATH: PATH-A`
- Any verdict REVISED: emit `CHART-PATH: PATH-B`
The `CHART-PATH:` line must appear as an output token before executing the path.

**PATH-A execution (emit after CHART-PATH: PATH-A):**
All three verdicts VERBATIM. No rewrites. No TRANSCRIPTION-CLEAR block required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
1. For each REVISED verdict: rewrite that section from the sealed CONTRACT artifact.
   Update that receipt line: corrected values, verdict VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all three contract artifacts with a VERBATIM
verdict for each, in a single pass including artifacts already VERBATIM before the
rewrite. A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally
incomplete and does not serve as a PATH-B exit gate.

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

**STEP 8 -- WRITE-ROLES**

**Entry**: CHART-WRITTEN.

A correct WRITE-ROLES phase names three passes in fixed order: PASS-EXEC before
PASS-SHARED before PASS-TEAM. A WRITE-ROLES phase that writes team roles before
completing PASS-EXEC and PASS-SHARED is structurally out of order. A WRITE-ROLES
phase that merges all role writes into a single undifferentiated pass is structurally
undifferentiated -- exec office and shared group roles cannot be verified independently.

**PASS-EXEC -- Exec office roles:**
Path: `.roles/exec-office/{role-slug}.md`
All five fields. Scope: `exec office`.
For each exec office role: `EXEC-ROLE-WRITTEN: [role-slug].`
If no exec office roles declared: `EXEC-ROLE-WRITTEN: none declared.`
`EXEC-WRITTEN: [n] exec office role files.`

**PASS-SHARED -- Shared group roles:**
Path: `.roles/{group-slug}/{role-slug}.md`
All five fields. Scope: `shared -- [group name]`.
For each shared role: `SHARED-ROLE-WRITTEN: [group] / [role-slug].`
If no shared group roles declared: `SHARED-ROLE-WRITTEN: none declared.`
`SHARED-WRITTEN: [n] shared group role files.`

**PASS-TEAM -- Team-level standard and specialized roles:**
Path: `.roles/{area-slug}/{role-slug}.md`
All five fields. Scope explicit: `standard -- present in all teams` or
`specialized -- [team name]`.
After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`TEAM-PASS-WRITTEN: [n] team role files.`

`ROLES-COMPLETE: EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total files.`

---

**STEP 9 -- BUILD-VERIFY**

**Entry**: ROLES-COMPLETE.

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase from Step 5, the exact IA lens field opening from the
written file, and a single VERBATIM/DRIFT verdict. A BUILD-VERIFY block containing any
content other than per-team VERBATIM/DRIFT verdict entries -- file writes, structural
checks, directory comparisons, headcount verifications, summary rows, or any other
output -- is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 5]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Step 5 profiles.`
`BUILD-VERIFY-COMPLETE.`

---

**STEP 10 -- CROSS-REF**

**Entry**: BUILD-VERIFY-COMPLETE.

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
  profiles:      [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA coverage:   [n of n] teams -- written before standard/specialized
  org-chart.md:  [CHART-PATH: PATH-A -- all VERBATIM, no re-audit required |
                  CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all three]
  role files:    EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n]) = [n] total
  build-verify:  PASS (single-purpose: [n of n] IA lens verdicts only)
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-04 -- Combined: lifecycle emphasis + inertia framing (C-24 + C-25 candidates)

**Axis**: Lifecycle emphasis + inertia framing combined
**Hypothesis**: C-24 (phase lifecycle tokens) and C-25 (resistance landscape artifact) are
orthogonal -- PHASE-ENTERED/PHASE-EXITED operate at the phase boundary level; ARTIFACT-D
operates at the contract artifact level. V-01 shows that lifecycle tokens can be added to
V-04 R7 without affecting any other criterion. V-02 shows that ARTIFACT-D can be added to
V-05 R7 without affecting any other criterion. V-04 R8 combines both on the
PROFILE-before-CONTRACT architecture (required for ARTIFACT-D derivation from profiles).
Phase sequence: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL -> WRITE-IA ->
WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF. All declarative correctness rules
from V-04 R7 preserved. CHART-PATH emission preserved. ARTIFACT-D added to CONTRACT and
SEAL. PHASE-ENTERED/PHASE-EXITED added to all 10 phases.

```
You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or
use the provided path.

**Step sequence**: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL ->
WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF.
Each gate must appear in output before the next step begins.
Each phase is bounded by PHASE-ENTERED and PHASE-EXITED tokens. PHASE-ENTERED names
the precondition satisfied to enter this phase. PHASE-EXITED names the gate emitted on
exit. A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally
invalid.

---

**STEP 1 -- PARSE**

`PHASE-ENTERED: PARSE -- precondition: initial phase (no prior gate required)`

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

`PHASE-EXITED: PARSE -- gate: PARSE-PASS`

---

**STEP 2 -- VALIDATE**

`PHASE-ENTERED: VALIDATE -- precondition: PARSE-PASS`
**No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared      PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec name collision per team    PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names               PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4. Proceeding.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

`PHASE-EXITED: VALIDATE -- gate: VALIDATE-PASS`

---

**STEP 3 -- PROFILE**

`PHASE-ENTERED: PROFILE -- precondition: VALIDATE-PASS`
**No files written. Resistance profiles extracted before CONTRACT is built. CONTRACT
ARTIFACT-D (resistance landscape) is derived from these profiles.**

A correct PROFILE entry contains exactly three fields: `defended-artifact` (a specific
named artifact -- not a category), `change-pressure` (a specific named initiative -- not
a generic force), and `lens-phrase` (5-10 words derived from both; verbatim opening of
this team's IA lens field). A PROFILE entry naming a category rather than a specific
artifact is structurally underspecified.

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

**STEP 4 -- CONTRACT**

`PHASE-ENTERED: CONTRACT -- precondition: PROFILE-GATE`
**No files written. Four contract artifacts. Sealed in Step 5. ARTIFACT-A through
ARTIFACT-C transcribed verbatim into org-chart.md sections 2-4. ARTIFACT-D transcribed
verbatim into org-chart.md section 6. Not regenerated.**

A correct CONTRACT phase produces four artifacts before any file is written. A CONTRACT
phase that skips ARTIFACT-B or ARTIFACT-D is structurally incomplete.

**ARTIFACT-A -- Headcount table:**
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
observation not readable from the table rows alone. An ARTIFACT-B with generic language
applicable to any org is structurally deficient.

**ARTIFACT-C -- Level distribution table + seniority sentence.**
```markdown
| Level     | Count | % of Org |
|-----------|-------|----------|
| [label]   | [n]   | [n]%     |
| **Total** | **[n]** | 100%   |
```
One seniority sentence referencing the dominant level.

**ARTIFACT-D -- Resistance landscape table (derived from PROFILE-GATE output):**
A correct ARTIFACT-D contains one row per team from PROFILE-COMPLETE, with the team
name, defended-artifact, change-pressure, and lens-phrase transcribed directly from
the PROFILE entries. An ARTIFACT-D with fewer rows than teams in PROFILE-COMPLETE is
structurally incomplete.

```markdown
| Team | Defended Artifact | Change Pressure | Lens Phrase |
|------|------------------|-----------------|-------------|
| [team name] | [defended-artifact verbatim] | [change-pressure verbatim] | [lens-phrase verbatim] |
```

`LANDSCAPE-CLOSED: [n] team rows -- one per PROFILE-COMPLETE entry.`

`CONTRACT-DRAFT: ARTIFACT-A (total=[n]), ARTIFACT-B ([n] sentences), ARTIFACT-C ([n] levels), ARTIFACT-D ([n] teams).`

`PHASE-EXITED: CONTRACT -- gate: CONTRACT-DRAFT`

---

**STEP 5 -- CONTRACT-SEAL**

`PHASE-ENTERED: CONTRACT-SEAL -- precondition: CONTRACT-DRAFT`

```
CONTRACT-SEALED:
  ARTIFACT-A: [n] rows, total = [n] | first-row lock: "[area name] | [n]"
  ARTIFACT-B: [n] sentences | sentence-1 lock: "[first sentence verbatim]"
  ARTIFACT-C: [n] levels, total = [n]
  ARTIFACT-D: [n] team rows | first-row lock: "[team name] | [lens-phrase first 4 words]"

  RULE: org-chart.md sections 2-4 are verbatim copies of ARTIFACT-A, -B, -C.
        org-chart.md section 6 is a verbatim copy of ARTIFACT-D.
        No recalculation. No rewrite. All four audited via TRANSCRIPTION-RECEIPT in Step 7.
        PATH-A: all four VERBATIM on first receipt. PATH-B: any REVISED -- TRANSCRIPTION-CLEAR required.
```

`CONTRACT-GATE: four artifacts sealed. [n] files to produce. Proceeding to WRITE-IA.`

`PHASE-EXITED: CONTRACT-SEAL -- gate: CONTRACT-GATE`

---

**STEP 6 -- WRITE-IA**

`PHASE-ENTERED: WRITE-IA -- precondition: CONTRACT-GATE`
**All IA files written before any standard or specialized role files.**

A correct IA role file is a person-portrait -- describing the specific kind of person
who would occupy this role on this team. An IA role file containing generic resistance
language ("ensures process stability", "advocates for continuity", "resists unnecessary
change") applicable to any team is structurally deficient.

Path: `.roles/{area-slug}/inertia-advocate.md`

- **orientation**: from `defended-artifact` -- specific concern, not generic caution
- **lens**: opens verbatim with the `lens-phrase` from Step 3; 2-3 sentences; no
  generic stability language; phrase not applicable to any team without rewrite
- **expertise**: anchored to `defended-artifact`; differs from every other team's IA;
  names a concrete artifact -- not a category
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: specific forums, cadence, primary counterpart

No two IA files share identical `lens` or `expertise` text.

A correct IA-WRITTEN receipt names the team, confirms the lens-phrase was applied, and
carries two binary checks. An IA-WRITTEN receipt missing any of these is structurally
incomplete.

```
IA-WRITTEN: [team]
  lens-phrase applied: "[phrase from Step 3]"
  opens verbatim: YES / NO
  expertise concrete (not a category): YES / NO
```
Any NO -> rewrite before proceeding.

`IA-PHASE-COMPLETE: [n of n] teams covered. All IA files written before standard/specialized roles.`

`PHASE-EXITED: WRITE-IA -- gate: IA-PHASE-COMPLETE`

---

**STEP 7 -- WRITE-CHART**

`PHASE-ENTERED: WRITE-CHART -- precondition: IA-PHASE-COMPLETE`

Write org-chart.md. Sections in order:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. [TRANSCRIBE CONTRACT ARTIFACT-A verbatim -- do not recalculate]
3. [TRANSCRIBE CONTRACT ARTIFACT-B verbatim -- same sentences, not a rewrite]
4. [TRANSCRIBE CONTRACT ARTIFACT-C verbatim + seniority sentence]
5. AMEND section
6. [TRANSCRIBE CONTRACT ARTIFACT-D verbatim -- resistance landscape table]

A correct AMEND section contains exactly three options, each naming specific mechanisms
drawn from org.yaml: (1) `--area "[name]"` with the area list; (2) `--levels "[old]:[new]"`
with the level vocabulary; (3) `--restructure "[team] > [new-parent]"` with the parent >
child nesting pairs. An AMEND section with fewer than three options, or with options that
give no specific org.yaml values, is structurally incomplete.

```markdown
## AMEND
1. --area "[area name]" -- regenerate that area.
   Available areas: [list from ARTIFACT-A]
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

A correct TRANSCRIPTION-RECEIPT contains exactly four artifact rows (ARTIFACT-A through
ARTIFACT-D), each showing the CONTRACT-SEALED value, the org-chart.md value, and a
VERBATIM/REVISED verdict. A TRANSCRIPTION-RECEIPT with fewer than four rows is
structurally incomplete.

```
TRANSCRIPTION-RECEIPT:
  ARTIFACT-A (headcount table):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
  ARTIFACT-B (analytic prose):
    CONTRACT sentence-1: "[phrase]" / org-chart.md sentence-1: "[phrase]"  -- verdict: VERBATIM / REVISED
  ARTIFACT-C (level distribution):
    CONTRACT total: [n] / org-chart.md total: [n]  -- verdict: VERBATIM / REVISED
  ARTIFACT-D (resistance landscape):
    CONTRACT first-row lock: "[team] | [lens-phrase first 4 words]" /
    org-chart.md first row:  "[team] | [lens-phrase first 4 words]"  -- verdict: VERBATIM / REVISED
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
All four verdicts VERBATIM. No rewrites. No TRANSCRIPTION-CLEAR required.
`CHART-WRITTEN.`

**PATH-B execution (emit after CHART-PATH: PATH-B):**
1. For each REVISED artifact: rewrite that section in org-chart.md from the sealed
   CONTRACT artifact. Update that receipt line: corrected values, verdict VERBATIM.
2. After all rewrites, emit TRANSCRIPTION-CLEAR.

A correct TRANSCRIPTION-CLEAR names all four contract artifacts (ARTIFACT-A through
ARTIFACT-D) with a VERBATIM verdict for each, in a single pass including artifacts
already VERBATIM before the rewrite. A TRANSCRIPTION-CLEAR naming fewer than four
artifacts is structurally incomplete and does not serve as a PATH-B exit gate. CHART-WRITTEN
may not follow PATH-B until TRANSCRIPTION-CLEAR is present and all four lines show VERBATIM.

```
TRANSCRIPTION-CLEAR:
  ARTIFACT-A: VERBATIM
  ARTIFACT-B: VERBATIM
  ARTIFACT-C: VERBATIM
  ARTIFACT-D: VERBATIM
  all four confirmed -- PATH-B exit authorized
```

If any artifact shows REVISED in this re-audit: return to step 1 of PATH-B.
`CHART-WRITTEN.`

`PHASE-EXITED: WRITE-CHART -- gate: CHART-WRITTEN`

---

**STEP 8 -- WRITE-ROLES**

`PHASE-ENTERED: WRITE-ROLES -- precondition: CHART-WRITTEN`

Standard, specialized, shared group, and exec office role files. All five fields, no
placeholder text. Scope explicit:
`standard -- present in all teams`, `specialized -- [team name]`,
`shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team] -- [n] std + [n] spec.`
`ROLES-COMPLETE: [n] files written.`

`PHASE-EXITED: WRITE-ROLES -- gate: ROLES-COMPLETE`

---

**STEP 9 -- BUILD-VERIFY**

`PHASE-ENTERED: BUILD-VERIFY -- precondition: ROLES-COMPLETE`

A correct BUILD-VERIFY phase contains exactly N entries (one per team in org.yaml),
each with a profile lens-phrase from Step 3, the exact IA lens field opening from the
written file, and a VERBATIM/DRIFT verdict. A BUILD-VERIFY block containing any content
other than per-team VERBATIM/DRIFT verdict entries -- file writes, structural checks,
directory comparisons, headcount verifications, summary rows, or any other output --
is structurally invalid.

```
BUILD-VERIFY: [team name]
  profile lens-phrase:    "[phrase from Step 3]"
  IA lens field opening:  "[exact first phrase in written .roles/ file]"
  verdict: VERBATIM / DRIFT
```

DRIFT -> rewrite IA lens to open with profile phrase verbatim. Reemit VERBATIM entry.

`BUILD-VERIFY-PASS: [n of n] teams. All IA lens phrases verbatim against Step 3 profiles.`
`BUILD-VERIFY-COMPLETE.`

`PHASE-EXITED: BUILD-VERIFY -- gate: BUILD-VERIFY-COMPLETE`

---

**STEP 10 -- CROSS-REF**

`PHASE-ENTERED: CROSS-REF -- precondition: BUILD-VERIFY-COMPLETE`

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

`PHASE-EXITED: CROSS-REF -- gate: CROSS-REF-PASS`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:             PASS (4/4 checks)
  profiles:             [n of n] teams (specific artifact + pressure + lens-phrase;
                        profiles are causal source of ARTIFACT-D)
  contract:             SEALED (headcount=[n], prose=[n] sentences, levels=[n],
                        resistance-landscape=[n] teams)
  resistance-landscape: [n of n] teams -- ARTIFACT-D transcribed verbatim to section 6
  IA coverage:          [n of n] teams -- written before standard/specialized
  org-chart.md:         [CHART-PATH: PATH-A -- all four VERBATIM, no re-audit required |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  role files:           [n] written / [n] declared
  build-verify:         PASS (single-purpose: [n of n] VERBATIM/DRIFT verdicts only)
  cross-ref:            PASS / FAIL
  phase-trace:          PARSE -> VALIDATE -> PROFILE -> CONTRACT -> SEAL ->
                        WRITE-IA -> WRITE-CHART -> WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF
                        (all PHASE-ENTERED / PHASE-EXITED tokens emitted)
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```

---

## V-05 -- Full integration: V-05 R7 base + all three R8 axes

**Axis**: Full integration
**Hypothesis**: V-04 R7 was the strongest combined architecture at 100/100; V-05 R7 was
the deepest integration with PROFILE-before-CONTRACT. R8 V-05 takes V-05 R7's architecture
and adds all three new axes: PHASE-ENTERED/PHASE-EXITED lifecycle tokens at every boundary
(C-24 candidate), ARTIFACT-D resistance landscape in org-chart.md (C-25 candidate), and
named write passes in WRITE-ROLES (C-26 candidate). Phase sequence is unchanged from V-05
R7: PARSE -> VALIDATE -> PROFILE -> CONTRACT -> CONTRACT-SEAL -> WRITE-IA -> WRITE-CHART ->
WRITE-ROLES -> BUILD-VERIFY -> CROSS-REF. Declarative correctness rules from V-05 R7
preserved and extended to cover ARTIFACT-D and named write passes. CHART-PATH emission
preserved. This variation maximizes the number of new structural patterns emitted per
build run, making it the highest-signal variation for rubric extraction.

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
lists standard and specialized roles per team, lists any shared group or exec office
roles, states levels declared or "not declared", and gives nesting depth and total role
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
Derived from PROFILE-GATE team and area assignments.

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
to any org ("the org has several teams") is structurally deficient.

- Sentence 1: largest area by headcount as percentage of total
- Sentence 2: dominant level label, or note that no levels are declared
- Sentence 3: structural observation the table rows alone do not convey

Strong example:
> "Infrastructure carries 12 of 30 total headcount -- the largest area at 40%. Six of
> nine teams declare IC1/IC2 levels; the three product-facing teams have no declared
> level vocabulary. Every team with declared levels maps to Infrastructure, concentrating
> leveling data in one half of the org."

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
| [team name] | [defended-artifact verbatim from PROFILE] | [change-pressure verbatim from PROFILE] | [lens-phrase verbatim from PROFILE] |
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

Path: `.roles/{area-slug}/inertia-advocate.md`

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

Write org-chart.md with six sections:
1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount in parentheses.
2. Sections 2-4 are CONTRACT ARTIFACT-A, -B, and -C. The same content. Not a rewrite.
3. (see above)
4. (see above)
5. AMEND section
6. RESISTANCE-LANDSCAPE section -- CONTRACT ARTIFACT-D. The same content. Not a rewrite.

A correct AMEND section contains exactly three options, each citing specific values
drawn from org.yaml: option 1 names `--area` with the area list from ARTIFACT-A;
option 2 names `--levels` with the level vocabulary from org.yaml; option 3 names
`--restructure` with the current parent > child nesting pairs. An AMEND section with
fewer than three options, or with options that give no specific org.yaml values, is
structurally incomplete.

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

After writing org-chart.md, emit TRANSCRIPTION-RECEIPT.

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
Path: `.roles/exec-office/{role-slug}.md`
All five fields. Scope: `exec office`.
For each role: `EXEC-ROLE-WRITTEN: [role-slug].`
If no exec office roles: `EXEC-ROLE-WRITTEN: none declared.`
`EXEC-WRITTEN: [n] exec office role files.`

**PASS-SHARED -- Shared group roles:**
Path: `.roles/{group-slug}/{role-slug}.md`
All five fields. Scope: `shared -- [group name]`.
For each role: `SHARED-ROLE-WRITTEN: [group] / [role-slug].`
If no shared roles: `SHARED-ROLE-WRITTEN: none declared.`
`SHARED-WRITTEN: [n] shared group role files.`

**PASS-TEAM -- Team-level standard and specialized roles:**
Path: `.roles/{area-slug}/{role-slug}.md`
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
  directories:    org.yaml areas [list] == .roles/ dirs [list] -- MATCH / MISMATCH
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
  org-chart.md:         [CHART-PATH: PATH-A -- all four VERBATIM, no TRANSCRIPTION-CLEAR |
                          CHART-PATH: PATH-B -- TRANSCRIPTION-CLEAR confirmed all four]
  role files:           EXEC-WRITTEN([n]) + SHARED-WRITTEN([n]) + TEAM-PASS-WRITTEN([n])
                        = [n] total / [n] declared (all three passes named)
  build-verify:         PASS ([n of n] lens-phrase verdicts -- block contains nothing else)
  cross-ref:            PASS / FAIL
  status:               COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}
```
