---
skill: campaign-simulate
round: 5
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v4-2026-03-17.md
---

# campaign-simulate -- Round 5 Variations

Round 4 V-04 and V-05 achieve 100/100 on rubric v4. Round 5 explores three new axes that
could surface excellence patterns warranting a rubric v5 upgrade. The goal is to test whether
any of these axes produces output quality not captured by the current rubric -- and if so, to
characterize the pattern precisely enough to define a new criterion.

**New axes this round:**

- **Axis A: Exception Path column in unified findings table** -- C-21 requires an Exception
  Path column in the findings table OR entity manifest. R4 V-05 satisfies C-21 through Entity
  List 4 ("Exception Path Defined?" column). Axis A moves the exception path column into the
  unified findings table itself, making per-row exception path coverage verifiable by a single
  column scan rather than by cross-referencing the entity manifest with the findings table.
- **Axis B: Blast radius rationale as a named column** -- C-20 requires a rationale sentence
  for CRITICAL/system-wide findings. R4 V-05 satisfies this with inline prose below the ranked
  table. Axis B promotes the rationale to a named `Blast Rationale` column in the ranked
  findings table so C-20 compliance is verifiable by column inspection, not by locating the
  correct prose paragraph after a long table.
- **Axis C: Mandatory cross-skill synthesis gate** -- R4 V-05 includes CROSS-SKILL PATTERNS
  as an output section. Axis C promotes it to a mandatory gate with a sentinel requirement:
  either one P-ID row exists, or a sentinel entry documents why no patterns were found. This
  converts the cross-skill synthesis from a bonus deliverable into a required structural output
  whose absence is a verifiable gap.

**Variation assignments:**

Single-axis: V-01 (exception path column), V-02 (blast rationale column),
V-03 (mandatory cross-skill gate).
Combined: V-04 (Axis A + Axis B), V-05 (Axis A + Axis B + Axis C, full R4 V-05
architecture forward).

---

## V-01 -- Exception Path Column Axis

**Variation axis:** Output format -- the unified findings table is extended from 10 columns
to 11 by adding an `Exception Path` column. The column is populated per finding row: for
flow findings, it names the exception path exercised or revealed as missing; for trace
findings, it names the exception path that must be guarded at the anomaly site. The column
makes exception path coverage verifiable by a single structural scan of the findings table,
independent of the entity manifest.

**Hypothesis:** C-21 passes when a named Exception Path column exists in the findings table
OR entity manifest. R4 satisfies C-21 through Entity List 4, which tracks per-phase exception
path definition. But Entity List 4 only covers the flow-lifecycle sub-skill. Trace sub-skills
(trace-state, trace-contract, trace-permissions) also produce findings with exception path
implications -- an exit-less state, a missing denial, or an unguarded boundary each represent
exception paths that callers will eventually trigger. Placing the Exception Path column in the
unified findings table forces every sub-skill to characterize its finding's exception path
dimension, not just flow-lifecycle. This produces a richer exception path picture and may
surface a new excellence pattern: exception path density across trace sub-skills as a
pre-implementation coverage signal.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. The unified findings table carries an
Exception Path column so exception path coverage is verifiable per finding row across all
five sub-skills.

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type must be copied from this table. `spec-gap` is available to all
sub-skills. Both fields are copy operations, not model judgments.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

**Column rules:**

- **F-ID**: sequential F-01, F-02, ... (F-00 reserved for manifest spec gaps)
- **Sub-Skill**: one of the five named sub-skills
- **System Boundary**: copy from Type Vocabulary Map
- **Type**: copy from Type Vocabulary Map for the attributed sub-skill
- **Spec Location**: name a specific section, state, boundary, or phase -- never "the spec"
- **Summary**: one sentence naming the specific defect
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **Blast Radius**: system-wide / cross-skill / component-wide / isolated
- **Trace Link**: "N/A -- trace sub-skill" for trace findings; F-ID of related trace finding
  or "none" for flow findings
- **Exception Path**: For flow findings: name the exception path exercised or revealed as
  missing (e.g., "timeout on Submit -- no retry path defined"). For trace findings: name the
  exception path that callers will trigger at this anomaly (e.g., "concurrent write with stale
  lock bypasses guard"). If truly no exception path applies: "N/A -- happy path finding -- [reason]"
- **Remediation**: specific action at a named location (not "fix the spec" or "clarify")

No blank cells. Optional fields use "N/A -- [reason]".

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Each list is the traversal scope for its
owning sub-skill.

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty before sub-skills run. Any empty
list = pre-simulation spec gap, recorded as sentinel finding F-00 in the findings table
with System Boundary and Type drawn from the relevant sub-skill's vocabulary.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH)
   -- PAUSE: verify severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads Trace Findings Brief)
5. flow-conversation   (walks Entity List 5; reads Trace Findings Brief)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify all transitions, preconditions, and postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row. System Boundary = "state machine". Type from map. Trace Link =
"N/A -- trace sub-skill". Exception Path: identify the exception path a caller will trigger
at this anomaly site (e.g., re-entry into an exit-less state, a transition that fires without
its guard being met).

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state the caller's expectation, the callee's behavior
per spec, and the divergence. Find undocumented edge case behaviors at interfaces.

Add findings. System Boundary = "contract surface". Type from map. Trace Link = "N/A --
trace sub-skill". Exception Path: name the cross-boundary exception path that is unhandled
or mis-specified (e.g., "callee returns error code not in caller's handling set").

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace the full permission path through all permitted and
denied actions. Find privilege escalation routes, missing denials, cross-role conflicts.

Add findings. System Boundary = "permission check". Type from map. Trace Link = "N/A --
trace sub-skill". Exception Path: name the access exception path (the unguarded route, the
role that can reach a resource it should not).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run. If any is NOT MET, widen scope and
re-run before proceeding.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, and exception
path are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts,
recovery gaps.

Add findings. System Boundary = "lifecycle phase". Type from map. Trace Link: scan the
brief -- if any trace finding shares a root cause or spec section, name its F-ID. If none:
"none." Exception Path: name the specific exception path this finding reveals as absent or
under-specified.

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path through all defined
transitions. Find dead ends, loops, ambiguous transitions.

Add findings. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements as flow-lifecycle.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column table with all rows from all five sub-skills. Sub-skills with no
findings contribute a sentinel row: Summary = "No findings detected", Exception Path =
"N/A -- no findings to classify", Remediation = "None required -- [reason]", all other
cells populated per schema rules.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any column including Exception Path
- [ ] All System Boundary values copied from Type Vocabulary Map
- [ ] All Type values copied from Type Vocabulary Map for the attributed sub-skill
- [ ] All Exception Path cells populated (value or "N/A -- happy path finding -- [reason]")
- [ ] All Trace Links populated (not blank)
- [ ] All Severity values from the four-value enumerated set
- [ ] All Spec Locations name a specific section or boundary
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED (all checks clear) OR FAILED (list the failing checks and
correct before proceeding).

---

**RANKED FINDINGS**

Re-sort the complete findings table by blast radius (system-wide first), then severity
within tier. Add Rank column at left.

For all system-wide and cross-skill findings: add a blast radius rationale sentence below
the row naming the downstream flows, components, or contracts affected and explaining why
the finding's scope reaches that blast radius tier.

---

**EXCEPTION PATH COVERAGE SUMMARY**

| Sub-Skill | Findings with Named Exception Path | Findings "N/A -- happy path" |
|-----------|-----------------------------------|------------------------------|
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| flow-lifecycle | | |
| flow-conversation | | |

Minimum acceptable coverage: at least 2 findings across the full report carry a named,
non-N/A exception path. If coverage is below this floor, identify which entity list entries
were not fully exercised for exception paths and flag them as coverage gaps.

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

---

**TEST SCENARIO BASELINE**

For each CRITICAL or HIGH finding, derive a named test scenario.

| Scenario ID | F-ID | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|----------|---------------|-----------------|---------------------|
|             |      |          |               |                 |                     |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Type Vocabulary Map > Severity Scale > Findings Table Schema
(11 columns) > Topic Entity Manifest > Manifest Completeness Gate > trace sub-skill
executions (each with budget status) > Severity Budget Gate > Trace Findings Brief >
flow sub-skill executions (each with trace link + exception path check) > Findings Table
(complete, gate PASSED) > Ranked Findings (with blast rationale for top-tier) > Exception
Path Coverage Summary > Type Vocabulary Verification > Execution Log > Test Scenario
Baseline.

---

## V-02 -- Blast Radius Rationale Column Axis

**Variation axis:** Output format -- the blast radius rationale required by C-20 is moved
from inline prose appended below the ranked findings table into a named `Blast Rationale`
column in the ranked findings table itself. For system-wide and cross-skill findings, the
column contains the rationale sentence. For component-wide and isolated findings, the column
contains "N/A -- scope limited to [component/boundary name]". The column makes C-20 compliance
verifiable by a single column scan rather than by locating the correct prose paragraph.

**Hypothesis:** R4 V-05 satisfies C-20 by appending rationale sentences below the ranked
table row. This works for a human reader but creates a fragile structural dependency: the
rationale is "near" the finding but not "in" it. A reader scanning the findings table cannot
determine C-20 compliance without also reading the paragraphs that follow. A named column
eliminates the location dependency: C-20 passes if and only if all rows in the Blast Rationale
column are populated with a non-N/A value for system-wide and cross-skill blast radius tiers.
The risk is that forcing a long rationale into a table cell degrades readability. The mitigation
is to require a single sentence (not a paragraph) in the column and allow an extended rationale
section after the table for findings that need more detail.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. The ranked findings table includes a
Blast Rationale column so blast radius tier assignments are verifiable by column inspection.

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type: copy from this table. `spec-gap` is the cross-cutting escape type.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a Blast Rationale column with these rules:

- **system-wide** findings: required -- one sentence naming the specific downstream flows,
  components, or contracts affected and why the scope reaches all of them. Example:
  "Affects all callers because the missing permission check is on a shared gateway that every
  role traverses regardless of action."
- **cross-skill** findings: required -- one sentence naming the two or more system boundaries
  where the impact is felt and the mechanism of propagation.
- **component-wide** findings: "N/A -- component-wide: [component name]"
- **isolated** findings: "N/A -- isolated: [single caller or boundary name]"

A Blast Rationale cell that is blank, or that contains only a severity label without a
rationale sentence, = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 10 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No blank cells. "N/A -- [reason]" for fields that do not apply. System Boundary and Type
copied from the Type Vocabulary Map. Trace Link = "N/A -- trace sub-skill" for trace findings;
F-ID or "none" for flow findings.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists.

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty. Empty list = sentinel F-00.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH)
   -- PAUSE: severity budget gate; Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief)
5. flow-conversation   (walks Entity List 5; reads brief)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions. Find
exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Trace Link = "N/A -- trace sub-skill".

**Budget status**: [MET -- F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: verify caller expectation against callee spec behavior.
Find mismatches and undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three MET before flow sub-skills run.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius |
|------|-----------|------|---------|----------|-------------|
|      |           |      |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, exception path
are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts,
recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan brief --
name linked F-ID or "none." At least one finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path. Find dead ends,
loops, ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link requirement.

---

**FINDINGS TABLE (complete)**

[Insert full 10-column findings table. Sub-skills with no findings contribute a sentinel row.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells
- [ ] System Boundary and Type values from Type Vocabulary Map
- [ ] Spec Locations name specific sections or boundaries
- [ ] Trace Links populated
- [ ] Severity from four-value set
- [ ] Sentinel rows for clean sub-skills

**Verification gate**: PASSED OR FAILED.

---

**RANKED FINDINGS** (11 columns: Rank + the 10 findings table columns + Blast Rationale)

Re-sort by blast radius (system-wide first), then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |             |                |

**Blast Rationale column rules:**
- system-wide or cross-skill Blast Radius: required sentence (see BLAST RADIUS RATIONALE RULE)
- component-wide: "N/A -- component-wide: [name]"
- isolated: "N/A -- isolated: [name]"
- A blank Blast Rationale cell = verification failure

**Blast Rationale verification:**

| F-ID | Blast Radius | Rationale Present? | Conformant? |
|------|-------------|-------------------|-------------|
|      |             | YES / NO | YES / NO |

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

---

**TEST SCENARIO BASELINE**

| Scenario ID | F-ID | Severity | Blast Radius | What to Exercise | Acceptance Condition |
|-------------|------|----------|-------------|-----------------|---------------------|
|             |      |          |             |                 |                     |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Type Vocabulary Map > Severity Scale > Blast Radius Rationale
Rule > Findings Table Schema > Topic Entity Manifest > Manifest Completeness Gate > trace
sub-skill executions (each with budget status) > Severity Budget Gate > Trace Findings Brief
> flow sub-skill executions > Findings Table (complete, gate PASSED) > Ranked Findings (with
Blast Rationale column) > Blast Rationale Verification > Type Vocabulary Verification >
Execution Log > Test Scenario Baseline.

---

## V-03 -- Mandatory Cross-Skill Synthesis Gate Axis

**Variation axis:** Lifecycle emphasis -- the CROSS-SKILL PATTERNS section is promoted from
an optional output deliverable to a mandatory gate with a sentinel requirement. The gate
requires: at least one P-ID row documenting a compounding pattern across two or more
sub-skills, OR a "No cross-skill patterns detected" sentinel entry with a minimum two-sentence
justification explaining why no patterns were found. The gate position is after the test
scenario baseline, and the report is not complete until the gate is satisfied.

**Hypothesis:** R4 V-05 includes CROSS-SKILL PATTERNS as an output section but does not
specify a minimum output requirement. When the model finds no cross-skill patterns, it can
omit the section or write an empty table without penalty. This silence is structurally
indistinguishable from skipping the synthesis step. A mandatory gate with a sentinel forces
the model to make an explicit claim: either "I found a pattern, here is P-01" or "I looked
and found none, here is my justification." The justification must name at minimum which
sub-skill pairs were examined and why no shared root cause was identified. This converts
the cross-skill synthesis from a passive output into an active reasoning step whose result
is always visible. The hypothesis is that mandatory sentinel logic surfaces cross-skill
patterns that the R4 V-05 optional section would silently skip.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. The cross-skill synthesis step is a
mandatory gate -- not an optional section. The report is incomplete until the gate entry
is written.

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type: copy from this table. `spec-gap` is the escape type.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**CROSS-SKILL SYNTHESIS GATE**

After the test scenario baseline, run the mandatory cross-skill synthesis step:

1. Scan the full findings table for root causes that appear across two or more sub-skills.
   A root cause "appears across" two sub-skills when a single underspecified behavior,
   missing guard, or contract ambiguity produces findings in more than one sub-skill's
   execution.

2. For each cross-skill pattern found:

   | P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Wider Than Individual |
   |------|------------|-------|--------------------|-----------------------|--------------------------|
   |      |            |       |                    |                       |                          |

   Combined Blast Radius rule: if any individual finding in the pattern is system-wide,
   the combined blast radius is system-wide. If no individual finding is system-wide but
   two or more are cross-skill, the combined is system-wide. Otherwise, promote one level
   above the highest individual finding.

3. If no cross-skill patterns are found, write this sentinel entry:

   **No cross-skill patterns detected.**

   Justification (required, minimum two sentences):
   - Sentence 1: which sub-skill pairs were examined for shared root causes.
   - Sentence 2: why no shared root cause was identified (e.g., "each sub-skill produced
     findings from distinct spec sections with no overlapping entity").

4. **Gate status**: POPULATED (at least one P-ID entry) OR SENTINEL (no patterns, justification
   written). Neither blank nor skipped is acceptable.

---

**FINDINGS TABLE SCHEMA** (unified, 10 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No blank cells. System Boundary and Type from the Type Vocabulary Map. Trace Link =
"N/A -- trace sub-skill" for trace findings; F-ID or "none" for flow findings.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty. Empty list = sentinel F-00.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH)
   -- PAUSE: severity budget gate; Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief)
5. flow-conversation   (walks Entity List 5; reads brief)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions.
Find exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map.

**Budget status**: [MET -- F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: verify caller expectation against callee spec behavior.
Find mismatches and undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius |
|------|-----------|------|---------|----------|-------------|
|      |           |      |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. Verify entry condition, exit condition, exception path per phase.
Find lifecycle gaps, missing exit states, undefined phase contracts, recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan brief --
name F-ID or "none." At least one non-"none" Trace Link required.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. Simulate conversation paths. Find dead ends, loops, ambiguous
transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link requirement.

---

**FINDINGS TABLE (complete)**

[Insert full 10-column table.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells
- [ ] System Boundary and Type from vocabulary
- [ ] Spec Locations specific
- [ ] Trace Links populated
- [ ] Severity from four-value set
- [ ] Sentinel rows for clean sub-skills

**Verification gate**: PASSED OR FAILED.

---

**RANKED FINDINGS**

Sort by blast radius (system-wide first), then severity. Add Rank column.

For system-wide and cross-skill findings: add blast radius rationale sentence below the
row naming downstream affected components.

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

---

**TEST SCENARIO BASELINE**

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory -- see specification above)

[Run the cross-skill synthesis step here. Produce either: a P-ID table with at least one
row, OR the "No cross-skill patterns detected" sentinel with two-sentence justification.]

**Gate status**: POPULATED OR SENTINEL.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Type Vocabulary Map > Severity Scale > Findings Table Schema >
Topic Entity Manifest > Manifest Completeness Gate > trace sub-skill executions (each with
budget status) > Severity Budget Gate > Trace Findings Brief > flow sub-skill executions >
Findings Table (complete, gate PASSED) > Ranked Findings > Type Vocabulary Verification >
Execution Log > Test Scenario Baseline > Cross-Skill Synthesis Gate (POPULATED or SENTINEL).

The report is incomplete until the Cross-Skill Synthesis Gate shows a status of POPULATED
or SENTINEL.

---

## V-04 -- Combined (Exception Path Column + Blast Rationale Column)

**Variation axes combined:**
1. Output format -- Exception Path as a named 11th column in the unified findings table,
   making C-21 compliance verifiable per-row across all sub-skills (Axis A)
2. Output format -- Blast Rationale as a named column in the ranked findings table,
   making C-20 compliance verifiable by column scan rather than prose search (Axis B)

**Hypothesis:** The two axes share a common structural pattern: both replace a prose
requirement with a named column. C-21 currently has structural compliance through Entity
List 4 (per-phase exception path tracking). C-20 currently has structural compliance
through inline prose below the ranked table. Moving both into named columns means the
full set of rubric-required information is locatable by column name rather than by reading
paragraphs. Together they extend the "closed vocabulary pair" principle (C-14/C-19) to
the coverage dimension: just as boundary and type labels cannot be invented, the exception
path and blast rationale are now column-scoped rather than prose-scoped, making them
independently verifiable. The combined prompt also tests whether the two columns interact
productively -- a finding with a named exception path and a blast rationale for system-wide
scope is a more complete finding than either column alone produces.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. The findings table carries an Exception
Path column (Axis A). The ranked findings table carries a Blast Rationale column (Axis B).
Both columns make their respective rubric criteria verifiable by inspection.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type: copy from this table. Both fields are copy operations. `spec-gap`
is available to all sub-skills.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide** blast radius: required sentence -- name the downstream flows, components, or
  contracts affected and explain the mechanism of propagation.
- **cross-skill** blast radius: required sentence -- name the two or more system boundaries
  where impact is felt and the propagation mechanism.
- **component-wide** blast radius: "N/A -- component-wide: [component name]"
- **isolated** blast radius: "N/A -- isolated: [caller or boundary name]"

Blank Blast Rationale cell or rationale without a named target = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

**Column rules (11-column schema):**

- **Exception Path**: For flow findings -- name the exception path exercised or absent.
  For trace findings -- name the exception path a caller triggers at this anomaly site.
  Required: never blank. "N/A -- happy path finding -- [reason]" is acceptable.
- All other columns: no blank cells; "N/A -- [reason]" if field does not apply.
- System Boundary and Type: copy from Type Vocabulary Map.
- Trace Link: "N/A -- trace sub-skill" for trace; F-ID or "none" for flow.
- Remediation: specific action at a named location.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists.

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty. Empty list = sentinel F-00 in
findings table.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows; populate Trace Link +
   Exception Path)
5. flow-conversation   (walks Entity List 5; reads brief; add rows; populate Trace Link +
   Exception Path)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions. Find:
exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Trace Link = "N/A -- trace
sub-skill". Exception Path: name the exception path a caller triggers at this anomaly.

**Budget status**: [MET -- F-IDs: ...] OR [NOT MET -- widened scope to: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: verify caller expectation against callee spec behavior.
Find mismatches and undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map. Exception Path: name the
boundary-crossing exception path that is unhandled or mis-specified.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map. Exception Path: name the
access exception path (the unguarded route or the denied action with no response defined).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. Flow sub-skills do not run until the gate clears.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, and exception
path are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts,
recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan brief --
name linked F-ID or "none." Exception Path: name the exception path this finding exposes as
missing or underspecified.

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path. Find dead ends,
loops, ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link and Exception
Path requirements.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column table. Sentinel rows for clean sub-skills.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] System Boundary values from Type Vocabulary Map
- [ ] Type values from Type Vocabulary Map per sub-skill
- [ ] Exception Path populated for every row (value or "N/A -- happy path finding -- [reason]")
- [ ] Trace Links populated
- [ ] Severity from four-value set
- [ ] Spec Locations name specific sections or boundaries
- [ ] Sentinel rows for sub-skills with no findings

**Verification gate**: PASSED OR FAILED (list failures; correct before proceeding).

---

**RANKED FINDINGS** (12 columns: Rank + 11 findings columns + Blast Rationale)

Sort by blast radius (system-wide first), then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

Blast Rationale rules: required sentence for system-wide and cross-skill findings; "N/A --
component-wide/isolated: [name]" for lower-tier findings. No blank cells.

**Blast Rationale verification:**

| F-ID | Blast Radius | Rationale Present and Conformant? |
|------|-------------|----------------------------------|
|      |             | YES / NO |

---

**EXCEPTION PATH COVERAGE SUMMARY**

| Sub-Skill | Findings with Named Exception Path | Findings "N/A -- happy path" |
|-----------|-----------------------------------|------------------------------|
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| flow-lifecycle | | |
| flow-conversation | | |

Minimum: at least 2 rows across the report carry a named, non-N/A exception path.

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

---

**TEST SCENARIO BASELINE**

| Scenario ID | F-ID | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|----------|---------------|-----------------|---------------------|
|             |      |          |               |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider |
|------|------------|-------|--------------------|-----------------------|-------------------|
|      |            |       |                    |                       |                   |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Severity Scale > Type Vocabulary Map > Blast Radius Rationale
Rule > Findings Table Schema (11 columns) > Topic Entity Manifest > Manifest Completeness
Gate > trace sub-skill executions (each with budget status) > Severity Budget Gate > Trace
Findings Brief > flow sub-skill executions (each with trace link + exception path check) >
Findings Table (complete, gate PASSED) > Ranked Findings (with Blast Rationale column) >
Blast Rationale Verification > Exception Path Coverage Summary > Type Vocabulary
Verification > Execution Log > Test Scenario Baseline > Cross-Skill Patterns.

---

## V-05 -- Full Combination (Exception Path Column + Blast Rationale Column + Mandatory Cross-Skill Gate)

**Variation axes combined:**
1. Output format -- Exception Path as 11th column in unified findings table (Axis A)
2. Output format -- Blast Rationale as named column in ranked findings (Axis B)
3. Lifecycle emphasis -- Cross-Skill Synthesis as mandatory gate with sentinel (Axis C)

This variation carries the full R4 V-05 architecture forward intact: trace-first execution
order, severity budget gates, Topic Entity Manifest with typed entity lists, no-blank-cell
contract with N/A sentinels, Type Vocabulary Map (C-14/C-19), pre-assigned System Boundary
vocabulary, sentinel rows for clean sub-skills, pre-output verification gate, remediation
template, unified schema, Test Scenario Baseline, Trace Findings Brief.

**Hypothesis:** The three new axes each replace a prose compliance mechanism with a named
structural column or gate. Axis A moves exception path tracking from entity manifest to
findings table column. Axis B moves blast rationale from inline prose to a named column.
Axis C moves cross-skill synthesis from optional section to mandatory gate with sentinel.
Together they extend the core principle of the R4 architecture -- that every required field
has a mechanical compliance path verifiable by inspection -- to three additional fields that
R4 left as prose obligations. The resulting prompt has no compliance requirement satisfied
by prose alone: every criterion from C-01 through C-21 maps to a named column, table, or
gate whose presence or absence is structurally visible. The risk is column proliferation
making the findings table unwieldy. The mitigation is that Exception Path and Blast Rationale
are added as separate tables at specific points in the output rather than as columns embedded
in a 12+ column main table. The cross-skill gate is a mandatory section with a one-row
minimum or a sentinel entry.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Phase 0 produces the Topic Entity
Manifest, Type Vocabulary Map, and Remediation Template -- all three are in effect for every
sub-skill. The findings table carries an Exception Path column (Axis A). The ranked findings
table carries a Blast Rationale column (Axis B). The Cross-Skill Synthesis Gate is mandatory
(Axis C). Every compliance requirement maps to a named structural element.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type: copy from this table. Both are copy operations. `spec-gap` is the
cross-cutting escape type.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document
   - TARGET: specific thing being acted on
   - AT: specific location (spec section, interface, state name, code boundary)
   - TO: what it should be after the action

2. **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", "add validation", or any entry without named target and location
= template violation.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide** blast radius: required -- one sentence naming downstream flows, components,
  or contracts affected and explaining why the scope reaches system-wide.
- **cross-skill** blast radius: required -- one sentence naming the boundaries involved and
  the propagation mechanism.
- **component-wide** blast radius: "N/A -- component-wide: [component name]"
- **isolated** blast radius: "N/A -- isolated: [caller or boundary name]"

Blank Blast Rationale = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

**All columns required; no blank cells. Rules:**

- **Exception Path**: For flow findings -- name the exception path exercised or absent. For
  trace findings -- name the exception path triggered at this anomaly site. Required: "N/A --
  happy path finding -- [reason]" acceptable; blank is not.
- System Boundary and Type: copy from Type Vocabulary Map.
- Spec Location: name a specific section, state, boundary, or phase.
- Severity: one of four enumerated values.
- Blast Radius: system-wide / cross-skill / component-wide / isolated.
- Trace Link: "N/A -- trace sub-skill" for trace; F-ID or "none" for flow.
- Remediation: action form or research form per template.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Sub-skills walk these lists -- they do
not re-derive scope from the raw spec.

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty before any sub-skill runs. Any
empty list = pre-simulation spec gap recorded as sentinel F-00 in the findings table.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: verify severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows; populate Trace Link +
   Exception Path)
5. flow-conversation   (walks Entity List 5; reads brief; add rows; populate Trace Link +
   Exception Path)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify all transitions, preconditions, and postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row. System Boundary = "state machine" (from map). Type from map.
Trace Link = "N/A -- trace sub-skill". Exception Path: name the exception path a caller
triggers at this anomaly (e.g., "re-entry when in exit-less PENDING state blocks all
subsequent operations"). Remediation: action or research form.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ...
-- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee behavior per spec,
and divergence. Find undocumented edge case behaviors at interfaces.

Add findings. System Boundary = "contract surface". Type from map. Exception Path: name
the boundary-crossing exception path that is unhandled or mis-specified.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths through all spec-declared
actions. Find escalation routes, missing denials, and cross-role conflicts.

Add findings. System Boundary = "permission check". Type from map. Exception Path: name the
access exception path (the unguarded route or the denied action with no response defined).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without a rationale that the sub-skill's entity
list was fully exhausted without finding a HIGH or CRITICAL defect, the campaign halts.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, and exception
path are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts,
recovery gaps.

Add findings. System Boundary = "lifecycle phase". Type from map. Trace Link: scan the
brief -- if any trace finding shares a root cause, same spec section, or this flow anomaly
is downstream of a trace anomaly, name the trace F-ID. If no link: "none." Exception Path:
name the specific exception path this finding exposes as absent or underspecified.

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path through the graph.
Find dead ends, loops, and ambiguous transitions.

Add findings. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements as flow-lifecycle.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column findings table here. Sub-skills with no findings contribute a
sentinel row: Summary = "No findings detected", Exception Path = "N/A -- no findings to
classify", Remediation = "None required -- [reason]", all other cells populated.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] All System Boundary values copied from Type Vocabulary Map
- [ ] All Type values copied from Type Vocabulary Map for the attributed sub-skill
- [ ] All Exception Path cells populated (value or "N/A -- happy path finding -- [reason]")
- [ ] All Trace Links populated ("none" or "N/A -- trace sub-skill" is acceptable; blank is not)
- [ ] All Severity values from the four-value enumerated set
- [ ] All Spec Locations name a specific section, state, boundary, or phase
- [ ] All Remediation entries match action form or research form
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED (all checks clear) OR FAILED (list failing checks; correct
before proceeding).

Do not write the ranked findings until this gate shows PASSED.

---

**RANKED FINDINGS** (12 columns)

Sort the complete findings table by blast radius (system-wide first), then severity within
tier. Add Rank column at left.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

Blast Rationale rules: required sentence for system-wide and cross-skill findings; "N/A --
component-wide: [name]" or "N/A -- isolated: [name]" for lower-tier findings. No blank cells.

**Blast Rationale verification:**

| F-ID | Blast Radius | Rationale Present? | Conformant? |
|------|-------------|-------------------|-------------|
|      |             | YES / NO | YES / NO |

---

**EXCEPTION PATH COVERAGE SUMMARY**

| Sub-Skill | Findings with Named Exception Path | Findings "N/A -- happy path" |
|-----------|-----------------------------------|------------------------------|
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| flow-lifecycle | | |
| flow-conversation | | |

Minimum: at least 2 rows carry a named, non-N/A exception path. Below the floor: flag
which entity list entries produced no exception path findings and record as coverage gaps.

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

A sub-skill with "no findings" still gets a sentinel row in the findings table. Summary =
"No findings detected", Remediation = "None required -- [reason]", all other cells per the
no-blank-cell contract.

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario.

| Scenario ID | F-ID | Type | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|---------------|-----------------|---------------------|
|             |      |      |          |               |                 |                     |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory)

Scan the full findings table for root causes that appear across two or more sub-skills.

**Rule**: A root cause "appears across" sub-skills when a single underspecified behavior,
missing guard, or contract ambiguity produces findings attributed to more than one sub-skill.
The Trace Link column is the primary evidence: flow findings that link to trace findings via
Trace Link are by construction candidates for cross-skill patterns.

If patterns found:

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider Than Any Individual Finding |
|------|------------|-------|--------------------|-----------------------|-----------------------------------------------|
|      |            |       |                    |                       |                                               |

Combined Blast Radius escalation rule: if any constituent finding is system-wide, the pattern
is system-wide. If no constituent is system-wide but two or more are cross-skill, promote to
system-wide. Otherwise, promote one level above the highest constituent finding.

If no patterns found -- write the sentinel:

**No cross-skill patterns detected.**

Justification (minimum two sentences required):
- Which sub-skill pairs were examined for shared root causes.
- Why no shared root cause was identified.

**Gate status**: POPULATED (at least one P-ID row) OR SENTINEL (justification written).
Report is incomplete until gate status is shown.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. Severity Scale
2. Type Vocabulary Map
3. Remediation Template
4. Blast Radius Rationale Rule
5. Findings Table Schema (11 columns)
6. Topic Entity Manifest
7. Manifest Completeness Gate
8. trace sub-skill executions (each with budget status)
9. Severity Budget Gate
10. Trace Findings Brief
11. flow sub-skill executions (each with trace link + exception path check)
12. Findings Table (complete, all 11 cells per row, verification gate PASSED)
13. Ranked Findings (12 columns including Blast Rationale)
14. Blast Rationale Verification
15. Exception Path Coverage Summary
16. Type Vocabulary Verification
17. Execution Log
18. Test Scenario Baseline
19. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)

Before writing the file: run the pre-output blank-cell verification gate. All nine checks
must clear. Report the gate result inline before the ranked findings section.
