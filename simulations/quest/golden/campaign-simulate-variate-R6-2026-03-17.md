---
skill: campaign-simulate
round: 6
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v5-2026-03-17.md
---

# campaign-simulate -- Round 6 Variations

Round 5 V-04 and V-05 achieve 100/100 on rubric v5. Round 6 explores three new axes that
could surface excellence patterns warranting a rubric v6 upgrade. The goal is to test whether
any of these axes produces output quality not captured by the current rubric -- and if so, to
characterize the pattern precisely enough to define a new criterion.

**New axes this round:**

- **Axis A: Remediation Quality Gate as named verification table** -- R5 V-05 includes
  "All Remediation entries match action form or research form" as a checklist bullet in the
  pre-output blank-cell verification gate. Axis A promotes this from a checkbox item to a
  named REMEDIATION QUALITY GATE with a per-remediation verification table: Verb, Target,
  Location, Conformance (PASS/FAIL). The gate catches "fix the spec" and other vague entries
  structurally rather than relying on the model to self-assess them as a checkbox.

- **Axis B: Entity Coverage Matrix** -- R5 V-05 creates the Topic Entity Manifest (five
  entity lists) and uses it to scope sub-skills, but never verifies post-execution that every
  listed entity was actually examined. Axis B adds an ENTITY COVERAGE MATRIX produced after
  all sub-skills run: rows are entities from all five lists, columns are the owning sub-skill
  and the finding F-IDs (or "CLEAN -- examined, no anomaly") attributed to each entity. An
  entity with a blank cell is indistinguishable from an entity that was skipped -- the matrix
  forces explicit coverage claims at the entity level, extending C-16's sub-skill sentinel
  rule down to the entity level.

- **Axis C: Post-Synthesis Blast Radius Re-Assessment** -- R5 V-05 assigns blast radius
  per finding at sub-skill execution time, then runs cross-skill synthesis as the final gate.
  But synthesis can reveal that two individually isolated findings from different sub-skills
  share a root cause in a P-ID pattern -- their combined blast radius may exceed either
  individual assignment. Axis C adds a BLAST RADIUS RE-ASSESSMENT GATE after synthesis:
  for each finding in a pattern, compare the individual blast radius to the combined blast
  radius from the synthesis gate; if the pattern elevates scope, update the finding's blast
  radius with notation "ELEVATED by P-ID" and produce a revised ranked table. This propagates
  synthesis results back into the ranked output rather than leaving them as orphan pattern
  observations.

**Variation assignments:**

Single-axis: V-01 (Remediation Quality Gate), V-02 (Entity Coverage Matrix),
V-03 (Post-Synthesis Blast Radius Re-Assessment).
Combined: V-04 (Axis A + Axis B), V-05 (Axis A + Axis B + Axis C, full R5 V-05
architecture forward).

---

## V-01 -- Remediation Quality Gate Axis

**Variation axis:** Output format -- the remediation quality check is promoted from a
checklist bullet inside the pre-output blank-cell verification gate into a named
REMEDIATION QUALITY GATE with a per-remediation structured verification table. Each
remediation in the findings table gets a row in the gate showing: F-ID, Verb extracted,
Target extracted, Location extracted, and Conformance (PASS / FAIL -- [violation type]).
The gate must show all rows PASS before the report is finalized.

**Hypothesis:** R5 V-05 includes a REMEDIATION TEMPLATE with a strict action form
(`[VERB] [TARGET] AT [LOCATION] TO [SPEC]` or the INVESTIGATE research form) and a
checklist item confirming conformance. The checklist approach relies on the model
self-certifying compliance -- the same structural weakness that C-17 addresses for blank
cells. A named gate table makes each remediation's verb and location extractable by
inspection: a reviewer can scan the Verb column to detect "fix" or "clarify" without
reading prose. The hypothesis is that the gate catches vague remediations that the
checkbox-only approach silently allows through.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. A named Remediation Quality Gate
produces a per-remediation verification table after the findings table, making remediation
conformance verifiable by column scan rather than checkbox assertion.

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
= template violation. These violations will be caught by the Remediation Quality Gate.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide** blast radius: required -- one sentence naming downstream flows, components,
  or contracts affected and explaining why scope reaches system-wide.
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
  trace findings -- name the exception path triggered at this anomaly site. "N/A --
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
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows)
5. flow-conversation   (walks Entity List 5; reads brief; add rows)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify all transitions, preconditions, and postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Trace Link = "N/A -- trace
sub-skill". Exception Path: name the exception path a caller triggers at this anomaly.
Remediation: action form or research form per template.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ...
-- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee behavior per spec,
and divergence. Find undocumented edge case behaviors at interfaces.

Add rows. System Boundary = "contract surface". Type from map. Exception Path: name
the boundary-crossing exception path that is unhandled or mis-specified.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths through all spec-declared
actions. Find escalation routes, missing denials, and cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map. Exception Path: name the
access exception path (unguarded route or denied action with no response defined).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without a rationale that the entity list was
fully exhausted without finding a HIGH or CRITICAL defect, the campaign halts.

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

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan the brief --
if any trace finding shares a root cause or spec section, name its F-ID. If no link: "none."
Exception Path: name the exception path this finding exposes as absent or underspecified.

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path through the graph.
Find dead ends, loops, and ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements as flow-lifecycle.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column findings table. Sentinel rows for clean sub-skills: Summary =
"No findings detected", Exception Path = "N/A -- no findings to classify", Remediation =
"None required -- [reason]", all other cells populated.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] All System Boundary values copied from Type Vocabulary Map
- [ ] All Type values copied from Type Vocabulary Map for the attributed sub-skill
- [ ] All Exception Path cells populated (value or "N/A -- happy path finding -- [reason]")
- [ ] All Trace Links populated
- [ ] All Severity values from the four-value enumerated set
- [ ] All Spec Locations name a specific section, state, boundary, or phase
- [ ] All Remediation entries match action form or research form (will be verified in gate below)
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED OR FAILED (list failures; correct before proceeding).

---

**REMEDIATION QUALITY GATE**

For every finding row in the findings table, extract and verify the remediation:

| F-ID | Remediation (verbatim) | Verb Extracted | Target Extracted | Location Extracted | Conformance |
|------|------------------------|---------------|-----------------|-------------------|-------------|
|      |                        |               |                 |                   | PASS / FAIL -- [violation type] |

Violation types:
- **VAGUE-VERB**: verb is not in the approved set (e.g., "fix", "clarify", "update", "improve")
- **MISSING-TARGET**: no specific thing being acted on is named
- **MISSING-LOCATION**: no specific spec section, boundary, or state is named
- **TEMPLATE-MISMATCH**: does not match action form or research form

**Gate status**: PASSED (all rows show PASS) OR FAILED (list the failing F-IDs and their
violation types). Correct failing remediations in the findings table before proceeding.

---

**RANKED FINDINGS** (12 columns)

Sort by blast radius (system-wide first), then severity within tier. Add Rank column.

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

Minimum: at least 2 rows carry a named, non-N/A exception path.

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

All CRITICAL and HIGH findings produce a named test scenario.

| Scenario ID | F-ID | Type | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|---------------|-----------------|---------------------|
|             |      |      |          |               |                 |                     |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory)

Scan the full findings table for root causes appearing across two or more sub-skills.

If patterns found:

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider Than Any Individual Finding |
|------|------------|-------|--------------------|-----------------------|-----------------------------------------------|
|      |            |       |                    |                       |                                               |

Combined Blast Radius escalation rule: if any constituent is system-wide, the pattern is
system-wide. If no constituent is system-wide but two or more are cross-skill, promote to
system-wide. Otherwise, promote one level above the highest constituent finding.

If no patterns found -- write the sentinel:

**No cross-skill patterns detected.**

Justification (minimum two sentences):
- Which sub-skill pairs were examined for shared root causes.
- Why no shared root cause was identified.

**Gate status**: POPULATED (at least one P-ID row) OR SENTINEL (justification written).

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
13. Remediation Quality Gate (all rows PASS before proceeding to ranked findings)
14. Ranked Findings (12 columns including Blast Rationale)
15. Blast Rationale Verification
16. Exception Path Coverage Summary
17. Type Vocabulary Verification
18. Execution Log
19. Test Scenario Baseline
20. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)

---

## V-02 -- Entity Coverage Matrix Axis

**Variation axis:** Lifecycle emphasis -- after all five sub-skills execute, produce an
ENTITY COVERAGE MATRIX before the findings table is finalized. The matrix has one row per
entity from the Topic Entity Manifest and columns for the owning sub-skill and the finding
F-IDs attributed to that entity (or "CLEAN -- examined, no anomaly" if the sub-skill ran
over this entity and produced no finding). An entity row with a blank cell is structurally
indistinguishable from an entity that was never examined -- the matrix forces the model to
make an explicit coverage claim at the entity level.

**Hypothesis:** R5 V-05 creates the entity manifest at the start (Phase 0), uses it to
scope sub-skills ("walk Entity List N"), and then adds a sentinel row at the sub-skill level
when a sub-skill produces no findings (C-16). But C-16 operates at the sub-skill granularity:
it tells you that trace-state ran over Entity List 1 but says nothing about whether every
state in Entity List 1 was examined. An entity manifest with 6 states and only 2 F-IDs
attributed to trace-state findings is ambiguous -- did the other 4 states produce no anomaly,
or were they skipped? The entity coverage matrix forces an explicit answer per entity. The
hypothesis is that this surfaces skipped entities that the sub-skill-level sentinel does not
detect, producing a new structural criterion analogous to C-16 but at entity granularity.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. An Entity Coverage Matrix is produced
after all sub-skills execute, making entity-level examination completeness verifiable by
row rather than by sub-skill count alone.

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

System Boundary and Type: copy from this table. `spec-gap` is the cross-cutting escape type.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document
   - TARGET: specific thing being acted on
   - AT: specific location (spec section, interface, state name, code boundary)
   - TO: what it should be after the action

2. **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", or any entry without named target and location = template
violation.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide**: required sentence naming downstream flows, components, or contracts
  affected and why scope reaches system-wide.
- **cross-skill**: required sentence naming the boundaries involved and propagation mechanism.
- **component-wide**: "N/A -- component-wide: [component name]"
- **isolated**: "N/A -- isolated: [caller or boundary name]"

Blank Blast Rationale = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

No blank cells. System Boundary and Type from Type Vocabulary Map. Trace Link = "N/A --
trace sub-skill" for trace; F-ID or "none" for flow.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Sub-skills walk these lists exclusively.

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

**Manifest completeness gate**: All five lists non-empty before any sub-skill runs. Empty
list = sentinel F-00 in findings table.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows)
5. flow-conversation   (walks Entity List 5; reads brief; add rows)
   -- PAUSE: produce Entity Coverage Matrix --

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions. Find
exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Exception Path: name the
exception path a caller triggers at this anomaly.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee spec behavior, and
divergence. Find undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map. Exception Path: name the
boundary-crossing exception path that is unhandled.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map. Exception Path: name the
access exception path (unguarded route or denied action with no response defined).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, exception path.
Find lifecycle gaps, missing exit states, undefined phase contracts, recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: name linked F-ID
or "none." At least one non-"none" Trace Link required. Exception Path: name the exception
path this finding exposes.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate conversation paths. Find dead ends,
loops, ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements.

---

**ENTITY COVERAGE MATRIX**

After all five sub-skills have run, produce the coverage matrix. One row per entity from
the Topic Entity Manifest. Column definitions:

- **Entity**: name from the entity list
- **Owning Sub-Skill**: the sub-skill responsible for examining this entity
- **Coverage**: the F-IDs of findings attributed to this entity, OR "CLEAN -- examined, no anomaly detected"
- **Coverage Status**: COVERED (finding produced) / CLEAN (examined, no anomaly) / SKIPPED (not examined -- requires explanation)

| Entity | Entity List | Owning Sub-Skill | Coverage | Coverage Status |
|--------|-------------|-----------------|----------|----------------|
|        |             |                 |          |                |

**Coverage gate rules:**
- COVERED: entity appears in at least one finding row via a matching Spec Location
- CLEAN: sub-skill explicitly traversed this entity and found no anomaly; record as "CLEAN -- examined, no anomaly"
- SKIPPED: entity was in the manifest but not examined; add "SKIPPED -- [reason]" and flag as a coverage gap
- No entity row may be blank in the Coverage column

**Entity coverage gate**: Count SKIPPED rows. Zero SKIPPED = gate PASSED. Any SKIPPED =
gate FAILED -- document why the entity was not examined and either re-run or record the
skip as a coverage gap finding in the findings table.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column findings table. Sentinel rows for clean sub-skills.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] All System Boundary values copied from Type Vocabulary Map
- [ ] All Type values copied from Type Vocabulary Map for the attributed sub-skill
- [ ] All Exception Path cells populated
- [ ] All Trace Links populated
- [ ] All Severity values from the four-value enumerated set
- [ ] All Spec Locations name specific sections or boundaries
- [ ] All Remediation entries match action form or research form
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED OR FAILED (list failures; correct before proceeding).

---

**RANKED FINDINGS** (12 columns)

Sort by blast radius (system-wide first), then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

Blast Rationale: required sentence for system-wide and cross-skill; "N/A -- component-wide/
isolated: [name]" for lower tiers. No blank cells.

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

| Scenario ID | F-ID | Type | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|---------------|-----------------|---------------------|
|             |      |      |          |               |                 |                     |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory)

Scan the full findings table for root causes appearing across two or more sub-skills.

If patterns found:

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider |
|------|------------|-------|--------------------|-----------------------|-------------------|
|      |            |       |                    |                       |                   |

If no patterns found -- sentinel entry required (two-sentence minimum justification).

**Gate status**: POPULATED OR SENTINEL.

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
12. Entity Coverage Matrix (entity coverage gate PASSED or FAILED with gaps documented)
13. Findings Table (complete, verification gate PASSED)
14. Ranked Findings (12 columns including Blast Rationale)
15. Blast Rationale Verification
16. Exception Path Coverage Summary
17. Type Vocabulary Verification
18. Execution Log
19. Test Scenario Baseline
20. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)

---

## V-03 -- Post-Synthesis Blast Radius Re-Assessment Axis

**Variation axis:** Role sequence -- after the Cross-Skill Synthesis Gate runs and produces
pattern P-IDs (or a sentinel), run a mandatory BLAST RADIUS RE-ASSESSMENT GATE. For each
finding that participates in a cross-skill pattern, compare the finding's individual blast
radius to the combined blast radius from the P-ID entry. If the combined blast radius is
higher than the individual assignment, update the finding's blast radius with an elevation
annotation ("ELEVATED by P-01") and produce a revised ranked table that reflects the
updated assignments. The re-assessment gate closes the loop between synthesis output and
ranked output.

**Hypothesis:** R5 V-05 assigns blast radius to each finding at sub-skill execution time,
then runs cross-skill synthesis as a final gate. But the synthesis gate's P-ID table
includes "Combined Blast Radius" and "Why Scope Is Wider" columns -- data that may contradict
the individual blast radius assignments already written into the ranked findings table. A
finding ranked 15th as "isolated" during trace-state execution may actually be part of a
system-wide pattern after synthesis. The ranked table is never updated to reflect this: the
synthesis result is orphaned as an observation rather than propagated back into the primary
output. The re-assessment gate forces propagation: every finding's final blast radius
assignment is the higher of (a) the individual sub-skill assignment and (b) the combined
blast radius of any pattern it participates in.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. After the Cross-Skill Synthesis Gate
runs, a mandatory Blast Radius Re-Assessment Gate propagates any pattern-elevated blast
radius assignments back into the findings table and produces a revised ranked table.

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

System Boundary and Type: copy from this table. `spec-gap` is the cross-cutting escape type.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document

2. **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", or any entry without named target and location = template violation.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide**: required sentence naming downstream flows, components, or contracts and why.
- **cross-skill**: required sentence naming boundaries involved and propagation mechanism.
- **component-wide**: "N/A -- component-wide: [component name]"
- **isolated**: "N/A -- isolated: [caller or boundary name]"

Blank Blast Rationale = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

No blank cells. System Boundary and Type from Type Vocabulary Map.

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

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows)
5. flow-conversation   (walks Entity List 5; reads brief; add rows)
   -- PAUSE: findings table verification gate --
   -- PAUSE: cross-skill synthesis gate --
   -- PAUSE: blast radius re-assessment gate --

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions. Find
exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Exception Path: name the
exception path a caller triggers at this anomaly.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee spec behavior,
divergence. Find undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map. Exception Path: name
unhandled boundary-crossing exception path.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map. Exception Path: name the
unguarded access exception path.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. Verify entry condition, exit condition, exception path per phase. Find
lifecycle gaps, missing exit states, undefined phase contracts, recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan brief --
name F-ID or "none." At least one non-"none" Trace Link required.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. Simulate conversation paths. Find dead ends, loops, ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link requirements.

---

**FINDINGS TABLE (complete)**

[Insert full 11-column findings table. Sentinel rows for clean sub-skills.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] System Boundary and Type from Type Vocabulary Map
- [ ] Exception Path cells populated
- [ ] Trace Links populated
- [ ] Severity from four-value set
- [ ] Spec Locations specific
- [ ] Remediation entries match template
- [ ] Sentinel rows for clean sub-skills

**Verification gate**: PASSED OR FAILED.

---

**RANKED FINDINGS (initial)** (12 columns)

Sort by blast radius (system-wide first), then severity within tier. This ranking uses the
blast radius as assigned during sub-skill execution. It will be revised after re-assessment.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory)

Scan the full findings table for root causes appearing across two or more sub-skills.

If patterns found:

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider |
|------|------------|-------|--------------------|-----------------------|-------------------|
|      |            |       |                    |                       |                   |

If no patterns found -- sentinel entry required (two-sentence minimum justification).

**Gate status**: POPULATED OR SENTINEL.

---

**BLAST RADIUS RE-ASSESSMENT GATE**

For each finding that participates in a cross-skill pattern (appears in the F-IDs column of
the P-ID table), compare its individual blast radius to the combined blast radius of the
pattern. If the combined is higher, elevate and annotate.

| F-ID | Individual Blast Radius | Participating Pattern(s) | Combined Blast Radius | Elevation Required? | Updated Blast Radius |
|------|------------------------|------------------------|-----------------------|--------------------|--------------------|
|      |                        |                        |                       | YES / NO | [original] or [ELEVATED by P-ID] |

Blast radius ordering (lowest to highest): isolated < component-wide < cross-skill < system-wide.

**Elevation rule**: if Combined Blast Radius > Individual Blast Radius for any row, update
the Blast Radius cell in the findings table for that F-ID with the elevated value and add
"ELEVATED by P-ID" annotation.

**Gate status**: NO ELEVATIONS REQUIRED or ELEVATED (list affected F-IDs and their new
blast radius values). If elevated, produce the revised ranked findings below.

---

**RANKED FINDINGS (revised -- post-re-assessment)**

If the Re-Assessment Gate shows ELEVATED, re-sort the findings table with updated blast
radius values and produce the revised ranked table. Mark elevated rows with "(ELEVATED by
P-ID)" in the Blast Rationale column.

If NO ELEVATIONS REQUIRED, write: "Revised ranked findings not required -- no blast radius
elevations from synthesis."

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

---

**EXCEPTION PATH COVERAGE SUMMARY**

| Sub-Skill | Findings with Named Exception Path | Findings "N/A -- happy path" |
|-----------|-----------------------------------|------------------------------|
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| flow-lifecycle | | |
| flow-conversation | | |

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

| Scenario ID | F-ID | Type | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|---------------|-----------------|---------------------|
|             |      |      |          |               |                 |                     |

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
12. Findings Table (complete, verification gate PASSED)
13. Ranked Findings initial (12 columns, blast radius as assigned during execution)
14. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)
15. Blast Radius Re-Assessment Gate
16. Ranked Findings revised (post-re-assessment; or "not required" if no elevations)
17. Exception Path Coverage Summary
18. Type Vocabulary Verification
19. Execution Log
20. Test Scenario Baseline

---

## V-04 -- Combined (Remediation Quality Gate + Entity Coverage Matrix)

**Variation axes combined:**
1. Output format -- Remediation Quality Gate as named per-remediation verification table,
   making template conformance verifiable by Verb/Target/Location column scan (Axis A)
2. Lifecycle emphasis -- Entity Coverage Matrix after all sub-skills execute, making
   entity-level examination completeness verifiable row by row (Axis B)

**Hypothesis:** The two axes address complementary silent-failure modes. Axis A catches
output quality failures: a remediation that passes the no-blank-cell gate (it is not empty)
but fails the template (it is vague) cannot be detected without parsing the cell content.
The Remediation Quality Gate table extracts the verb and location from each remediation and
checks them mechanically -- the same structural shift that C-14 made for System Boundary
(from prose inference to vocabulary copy). Axis B catches input coverage failures: an entity
in the manifest that was silently skipped during sub-skill execution cannot be detected
without cross-referencing Spec Locations across all findings rows. The Entity Coverage Matrix
makes this cross-reference explicit and mechanical. Together the two axes extend the
mechanical verification principle -- already applied to type vocabulary (C-14/C-19), severity
(C-25), exception paths (C-21), blast rationale (C-23), and blank cells (C-17) -- to two
fields that R5 V-05 left as prose or checkbox obligations: remediation quality and entity
examination completeness.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. A Remediation Quality Gate verifies
each remediation by extracted Verb/Target/Location (Axis A). An Entity Coverage Matrix
verifies examination completeness at entity granularity (Axis B).

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

System Boundary and Type: copy from this table. `spec-gap` is the cross-cutting escape type.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document
   - TARGET: specific thing being acted on
   - AT: specific location (spec section, interface, state name, code boundary)
   - TO: what it should be after the action

2. **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", or vague entries = template violation, caught by the Remediation
Quality Gate below.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide**: required sentence naming downstream flows, components, or contracts and why.
- **cross-skill**: required sentence naming boundaries involved and propagation mechanism.
- **component-wide**: "N/A -- component-wide: [component name]"
- **isolated**: "N/A -- isolated: [caller or boundary name]"

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

No blank cells. System Boundary and Type from Type Vocabulary Map. Trace Link = "N/A --
trace sub-skill" for trace; F-ID or "none" for flow.

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

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: severity budget gate; compile Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows)
5. flow-conversation   (walks Entity List 5; reads brief; add rows)
   -- PAUSE: produce Entity Coverage Matrix (Axis B) --
   -- PAUSE: assemble findings table --
   -- PAUSE: Remediation Quality Gate (Axis A) --

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions. Find
exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add rows. System Boundary = "state machine". Type from map. Trace Link = "N/A -- trace
sub-skill". Exception Path: name the exception path a caller triggers at this anomaly.
Remediation: action form or research form.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee spec behavior,
divergence. Find undocumented edge case behaviors.

Add rows. System Boundary = "contract surface". Type from map. Exception Path: name the
boundary-crossing exception path that is unhandled.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, cross-role conflicts.

Add rows. System Boundary = "permission check". Type from map. Exception Path: name the
unguarded access path.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius | Exception Path |
|------|-----------|------|---------|----------|-------------|---------------|
|      |           |      |         |          |             |               |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. Verify entry condition, exit condition, exception path per phase. Find
lifecycle gaps, missing exit states, undefined phase contracts, recovery gaps.

Add rows. System Boundary = "lifecycle phase". Type from map. Trace Link: scan brief --
name F-ID or "none." At least one non-"none" Trace Link required. Exception Path: name
the exception path this finding exposes.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. Simulate conversation paths. Find dead ends, loops, ambiguous transitions.

Add rows. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements.

---

**ENTITY COVERAGE MATRIX** (Axis B)

After all five sub-skills have run, produce the coverage matrix before assembling the
findings table.

| Entity | Entity List | Owning Sub-Skill | Coverage | Coverage Status |
|--------|-------------|-----------------|----------|----------------|
|        |             |                 |          | COVERED / CLEAN / SKIPPED |

- **COVERED**: entity appears in at least one finding row's Spec Location
- **CLEAN**: sub-skill traversed this entity; no anomaly found; record "CLEAN -- examined, no anomaly"
- **SKIPPED**: entity in manifest but not examined -- "SKIPPED -- [reason]"; add coverage gap to findings table

**Entity coverage gate**: Zero SKIPPED = PASSED. Any SKIPPED = FAILED (document and remediate).

---

**FINDINGS TABLE (complete)**

[Insert full 11-column findings table. Sentinel rows for clean sub-skills.]

**Pre-output blank-cell verification gate:**

- [ ] Zero blank cells in any of the 11 columns
- [ ] All System Boundary values from Type Vocabulary Map
- [ ] All Type values from Type Vocabulary Map for the attributed sub-skill
- [ ] All Exception Path cells populated
- [ ] All Trace Links populated
- [ ] All Severity values from four-value set
- [ ] All Spec Locations name specific sections
- [ ] All Remediation entries conform to template (verified below in Remediation Quality Gate)
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED OR FAILED (list failures; correct before proceeding).

---

**REMEDIATION QUALITY GATE** (Axis A)

For every finding row, extract and verify the remediation:

| F-ID | Remediation (verbatim) | Verb Extracted | Target Extracted | Location Extracted | Conformance |
|------|------------------------|---------------|-----------------|-------------------|-------------|
|      |                        |               |                 |                   | PASS / FAIL -- [violation type] |

Violation types:
- **VAGUE-VERB**: verb not in approved set (e.g., "fix", "clarify", "update")
- **MISSING-TARGET**: no specific thing named
- **MISSING-LOCATION**: no specific spec section, state, or boundary named
- **TEMPLATE-MISMATCH**: does not match action form or research form

**Gate status**: PASSED (all rows PASS) OR FAILED (list failing F-IDs). Correct failing
remediations in the findings table; confirm correction before proceeding to ranked findings.

---

**RANKED FINDINGS** (12 columns)

Sort by blast radius (system-wide first), then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

Blast Rationale: required sentence for system-wide and cross-skill; "N/A" for lower tiers.

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

| Scenario ID | F-ID | Type | Severity | Exception Path | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|---------------|-----------------|---------------------|
|             |      |      |          |               |                 |                     |

---

**CROSS-SKILL SYNTHESIS GATE** (mandatory)

Scan for root causes appearing across two or more sub-skills.

If patterns found:

| P-ID | Root Cause | F-IDs | Sub-Skills Involved | Combined Blast Radius | Why Scope Is Wider |
|------|------------|-------|--------------------|-----------------------|-------------------|
|      |            |       |                    |                       |                   |

If no patterns found -- sentinel entry required (two-sentence minimum justification).

**Gate status**: POPULATED OR SENTINEL.

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
12. Entity Coverage Matrix (Axis B -- coverage gate PASSED or FAILED)
13. Findings Table (complete, verification gate PASSED)
14. Remediation Quality Gate (Axis A -- all rows PASS before ranked findings)
15. Ranked Findings (12 columns including Blast Rationale)
16. Blast Rationale Verification
17. Exception Path Coverage Summary
18. Type Vocabulary Verification
19. Execution Log
20. Test Scenario Baseline
21. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)

---

## V-05 -- Full Combination (Remediation Quality Gate + Entity Coverage Matrix + Post-Synthesis Blast Radius Re-Assessment)

**Variation axes combined:**
1. Output format -- Remediation Quality Gate as named per-remediation verification table (Axis A)
2. Lifecycle emphasis -- Entity Coverage Matrix after all sub-skills execute (Axis B)
3. Role sequence -- Post-Synthesis Blast Radius Re-Assessment propagates pattern elevations
   back into the ranked findings table (Axis C)

This variation carries the full R5 V-05 architecture forward intact: trace-first execution
order, severity budget gates, Topic Entity Manifest with typed entity lists, no-blank-cell
contract with N/A sentinels, Type Vocabulary Map (C-14/C-19), pre-assigned System Boundary
vocabulary, sentinel rows for clean sub-skills (C-16), pre-output verification gate (C-17),
Remediation Template, unified 11-column schema (C-18), Test Scenario Baseline (C-09),
Trace Findings Brief, mandatory Cross-Skill Synthesis Gate (C-24), Blast Rationale column
(C-23), Exception Path column (C-21), four-value severity enforcement (C-25).

**Hypothesis:** The three new axes each address a structural gap in R5 V-05:

- Axis A (Remediation Quality Gate): R5 V-05 verifies blank cells but not content quality.
  The gate promotes remediation conformance from a checkbox to a per-row extraction table,
  completing the mechanical verification principle for the Remediation column.

- Axis B (Entity Coverage Matrix): R5 V-05 verifies sub-skill execution coverage (C-16)
  but not entity-level examination completeness. The matrix promotes entity coverage from
  implicit (entity list created, sub-skill ran) to explicit (each entity row shows COVERED,
  CLEAN, or SKIPPED), extending C-16's sentinel logic to entity granularity.

- Axis C (Post-Synthesis Blast Radius Re-Assessment): R5 V-05 computes blast radius during
  sub-skill execution and runs synthesis as a final observation. The re-assessment gate
  propagates synthesis back into the ranked table: findings in cross-skill patterns get
  their blast radius elevated if the combined pattern scope exceeds their individual
  assignment. This closes the feedback loop between synthesis and ranking.

Combined, the three axes extend the mechanical verification principle to three of the four
remaining prose obligations in R5 V-05: remediation quality (Axis A), entity coverage (Axis
B), and blast radius propagation from synthesis (Axis C). The fourth remaining prose
obligation -- the two-sentence synthesis sentinel justification -- is already gated by C-24.
The resulting prompt has no compliance requirement whose failure mode is "model self-assessed
correctly in prose."

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Phase 0 produces the Topic Entity
Manifest, Type Vocabulary Map, and Remediation Template -- all three are in effect for every
sub-skill. The findings table carries an Exception Path column (C-21). The ranked findings
table carries a Blast Rationale column (C-23). The Remediation Quality Gate verifies each
remediation by extracted Verb/Target/Location (Axis A). The Entity Coverage Matrix verifies
entity-level examination completeness (Axis B). The Blast Radius Re-Assessment Gate
propagates synthesis pattern elevations back into the ranked table (Axis C). The Cross-Skill
Synthesis Gate is mandatory (C-24). Every compliance requirement maps to a named structural
element verifiable by column or table inspection.

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
cross-cutting escape type available to all sub-skills.

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
= template violation. Violations are caught by the Remediation Quality Gate (Axis A) which
runs after the findings table is assembled.

---

**BLAST RADIUS RATIONALE RULE**

The ranked findings table carries a `Blast Rationale` column:

- **system-wide**: required -- one sentence naming downstream flows, components, or contracts
  and explaining why scope reaches system-wide.
- **cross-skill**: required -- one sentence naming the boundaries involved and propagation
  mechanism.
- **component-wide**: "N/A -- component-wide: [component name]"
- **isolated**: "N/A -- isolated: [caller or boundary name]"

Blank Blast Rationale = verification failure.

---

**FINDINGS TABLE SCHEMA** (unified, 11 columns)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|

**All columns required; no blank cells. Rules:**

- **Exception Path**: For flow findings -- name the exception path exercised or absent. For
  trace findings -- name the exception path triggered at this anomaly site. "N/A --
  happy path finding -- [reason]" acceptable; blank is not.
- System Boundary and Type: copy from Type Vocabulary Map.
- Spec Location: name a specific section, state, boundary, or phase.
- Severity: one of four enumerated values only.
- Blast Radius: system-wide / cross-skill / component-wide / isolated.
- Trace Link: "N/A -- trace sub-skill" for trace; F-ID or "none" for flow.
- Remediation: action form or research form per template.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Sub-skills walk these lists -- they do not
re-derive scope from the raw spec.

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
   -- PAUSE: Entity Coverage Matrix (Axis B) --
   -- PAUSE: assemble findings table; pre-output blank-cell gate --
   -- PAUSE: Remediation Quality Gate (Axis A) --
   -- PAUSE: ranked findings (initial) --
   -- PAUSE: Cross-Skill Synthesis Gate (mandatory) --
   -- PAUSE: Blast Radius Re-Assessment Gate (Axis C) --

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify all transitions, preconditions, and postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row. System Boundary = "state machine" (from map). Type from map.
Trace Link = "N/A -- trace sub-skill". Exception Path: name the exception path a caller
triggers at this anomaly (e.g., "re-entry into exit-less PENDING state blocks all
subsequent operations"). Remediation: action form or research form per template.

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
access exception path (unguarded route or denied action with no response defined).

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without a rationale that the entity list was fully
exhausted without finding a HIGH or CRITICAL defect, the campaign halts.

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

Add findings. System Boundary = "lifecycle phase". Type from map. Trace Link: scan the brief
-- if any trace finding shares a root cause, same spec section, or this flow anomaly is
downstream of a trace anomaly, name the trace F-ID. If no link: "none." Exception Path: name
the exception path this finding exposes as absent or underspecified.

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path through the graph.
Find dead ends, loops, and ambiguous transitions.

Add findings. System Boundary = "conversation state". Type from map. Same Trace Link and
Exception Path requirements as flow-lifecycle.

---

**ENTITY COVERAGE MATRIX** (Axis B)

After all five sub-skills have run, produce the coverage matrix. One row per entity from the
Topic Entity Manifest.

| Entity | Entity List | Owning Sub-Skill | Coverage | Coverage Status |
|--------|-------------|-----------------|----------|----------------|
|        |             |                 |          |                |

- **COVERED**: entity name appears as a Spec Location in at least one finding row
- **CLEAN**: sub-skill explicitly traversed this entity; no anomaly found; record "CLEAN -- examined, no anomaly detected at [entity name]"
- **SKIPPED**: entity is in the manifest but not examined; record "SKIPPED -- [reason]"; add a coverage gap finding to the findings table with Summary = "Entity [name] in manifest not examined by [sub-skill]"

**Entity coverage gate**: Zero SKIPPED rows = PASSED. Any SKIPPED = FAILED -- add coverage
gap findings to the findings table before assembling the final table.

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
- [ ] All Remediation entries will be verified in the Remediation Quality Gate below
- [ ] Sub-skills with no findings have sentinel rows

**Verification gate**: PASSED (all checks clear) OR FAILED (list failing checks; correct
before proceeding).

Do not write the Remediation Quality Gate until this gate shows PASSED.

---

**REMEDIATION QUALITY GATE** (Axis A)

For every finding row in the findings table, extract and verify the remediation:

| F-ID | Remediation (verbatim) | Verb Extracted | Target Extracted | Location Extracted | Conformance |
|------|------------------------|---------------|-----------------|-------------------|-------------|
|      |                        |               |                 |                   | PASS / FAIL -- [violation type] |

Violation types:
- **VAGUE-VERB**: verb is not in the approved set (Add / Remove / Change / Enforce /
  Specify / Split / Merge / Guard / Document) -- e.g., "fix", "clarify", "update", "improve"
- **MISSING-TARGET**: no specific thing being acted on is named
- **MISSING-LOCATION**: no specific spec section, state, or boundary is named
- **TEMPLATE-MISMATCH**: does not match action form or INVESTIGATE research form

**Gate status**: PASSED (all rows show PASS) OR FAILED (list failing F-IDs and violation
types). Correct failing remediations before proceeding to ranked findings.

Do not write the ranked findings until both the pre-output blank-cell gate and the Remediation
Quality Gate show PASSED.

---

**RANKED FINDINGS (initial)** (12 columns)

Sort the complete findings table by blast radius (system-wide first), then severity within
tier. Add Rank column at left. This is the initial ranking using blast radius as assigned
during sub-skill execution.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

Blast Rationale rules: required sentence for system-wide and cross-skill; "N/A --
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

A sub-skill with "no findings" still gets a sentinel row in the findings table.

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

**BLAST RADIUS RE-ASSESSMENT GATE** (Axis C)

For each finding in a cross-skill pattern (appears in any P-ID row's F-IDs column):

| F-ID | Individual Blast Radius | Participating Pattern(s) | Combined Blast Radius | Elevation Required? | Updated Blast Radius |
|------|------------------------|------------------------|-----------------------|--------------------|--------------------|
|      |                        |                        |                       | YES / NO | [original] or [new value + "ELEVATED by P-ID"] |

Blast radius ordering: isolated < component-wide < cross-skill < system-wide.

**Elevation rule**: if Combined Blast Radius > Individual Blast Radius, elevate the finding's
Blast Radius cell in the findings table to the combined value and annotate the Blast Rationale
column with "(ELEVATED by P-ID -- [reason the pattern widens scope])" in the revised ranked
table.

**Gate status**: NO ELEVATIONS REQUIRED or ELEVATED (list F-IDs and updated blast radius
values).

If the Cross-Skill Synthesis Gate shows SENTINEL (no patterns), write: "Re-Assessment Gate
not applicable -- no cross-skill patterns detected."

---

**RANKED FINDINGS (revised -- post-re-assessment)**

If Blast Radius Re-Assessment Gate shows ELEVATED:

Re-sort the findings table using the updated blast radius values. Produce the revised ranked
table. In the Blast Rationale column, findings with updated blast radius carry "(ELEVATED by
P-ID)" appended to the rationale sentence. Findings not elevated are unchanged from the
initial ranked table.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Exception Path | Remediation | Blast Rationale |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|---------------|-------------|----------------|
|      |      |           |                |      |              |         |          |             |           |               |             |                |

If NO ELEVATIONS REQUIRED: write "Revised ranked findings not required -- no blast radius
elevations from synthesis."

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
12. Entity Coverage Matrix (Axis B -- coverage gate PASSED or FAILED)
13. Findings Table (complete, all 11 cells per row, pre-output blank-cell gate PASSED)
14. Remediation Quality Gate (Axis A -- all rows PASS before proceeding)
15. Ranked Findings initial (12 columns, blast radius as assigned during execution)
16. Blast Rationale Verification
17. Exception Path Coverage Summary
18. Type Vocabulary Verification
19. Execution Log
20. Test Scenario Baseline
21. Cross-Skill Synthesis Gate (POPULATED or SENTINEL)
22. Blast Radius Re-Assessment Gate (Axis C)
23. Ranked Findings revised (post-re-assessment, or "not required" if no elevations)

Before writing the file: run the pre-output blank-cell verification gate and the Remediation
Quality Gate. Both must show PASSED before the ranked findings section is written.
