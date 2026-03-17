---
skill: campaign-simulate
round: 2
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v2-2026-03-17.md
---

# campaign-simulate -- Round 2 Variations

Round 2 targets the three new aspirational criteria introduced in rubric v2:

- **C-11**: At least one CRITICAL or HIGH finding per trace sub-skill (structural severity budget)
- **C-12**: Findings in a structured table with no blank cells
- **C-13**: At least one flow finding explicitly references a trace finding by ID or content

Single-axis: V-01 (role sequence -- trace-first), V-02 (severity budgets), V-03 (no-blank-cell table contract).
Combined: V-04 (trace-first + severity budgets), V-05 (trace-first + severity budgets + no-blank-cell table).

---

## V-01 -- Role Sequence Axis (Trace-First Ordering)

**Variation axis:** Role sequence -- the three trace sub-skills execute before the two flow sub-skills, reversing the Round 1 default order. Flow sub-skills receive an explicit brief containing the trace findings before they run.

**Hypothesis:** Running trace-state, trace-contract, and trace-permissions first populates a findings corpus before flow simulation begins. The flow brief requirement then forces the author to read that corpus and name at least one trace finding in their flow analysis, closing C-13 by construction. The ordering also benefits C-11 indirectly: the trace sub-skills run in isolation without flow context, making them more likely to surface structural anomalies rather than behavioral summaries. C-01 still requires all five to execute; the ordering change makes the integration section (flow referencing trace) structurally inevitable rather than optional.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute the five sub-skills in the order below -- trace sub-skills first, then flow sub-skills. This ordering is intentional: trace findings become context for flow analysis.

---

**EXECUTION ORDER**

1. trace-state       -- hand-compile state transitions with preconditions, postconditions, and invariants
2. trace-contract    -- compare expected vs actual outputs at contract boundaries
3. trace-permissions -- trace RBAC paths with privilege escalation detection
4. flow-lifecycle    -- trace the business document lifecycle with phase contracts and exception flows
5. flow-conversation -- simulate multi-turn agent conversation paths

Do not reorder. flow-lifecycle and flow-conversation must receive the trace findings brief before they execute.

---

**TRACE BRIEF PROTOCOL**

After completing all three trace sub-skills, write a **Trace Findings Brief** before starting any flow sub-skill. The brief lists:

- Every finding produced by trace-state, trace-contract, and trace-permissions (F-ID, type, one-sentence summary)
- Any state, transition, contract boundary, or permission path flagged as anomalous

When executing flow-lifecycle and flow-conversation, read the Trace Findings Brief first. For each flow finding, ask: is this flow behavior explained or worsened by any trace finding? If yes, name the trace finding by ID in the flow finding record.

---

**SUB-SKILL 1: trace-state**

Hand-compile the state machine for {{topic}}. Write every state, every transition, every precondition and postcondition. Then find:

- Exit-less states (a caller that enters cannot proceed)
- Transitions that can fire before their precondition is met
- Invariants named in the spec that are not enforced
- Unreachable states (no path from the initial state)

For each finding: name the state or transition, name the spec section, assign a severity (CRITICAL / HIGH / MEDIUM / LOW), and state the blast radius.

| F-ID | Type | State or Transition | Spec Location | Summary | Severity | Blast Radius |
|------|------|---------------------|--------------|---------|----------|-------------|
|      |      |                     |              |         |          |             |

---

**SUB-SKILL 2: trace-contract**

Identify the three most important contract boundaries for {{topic}} -- the interfaces where caller and callee assumptions diverge. For each: state the caller's expectation, state what the callee returns per the spec, and flag any mismatch.

For each mismatch: name the interface, state the exact divergence, assign severity (CRITICAL / HIGH / MEDIUM / LOW), and list every caller affected.

| F-ID | Type | Interface | Spec Location | Expected | Actual | Severity | Callers Affected |
|------|------|-----------|--------------|----------|--------|----------|-----------------|
|      |      |           |              |          |        |          |                 |

---

**SUB-SKILL 3: trace-permissions**

Walk the RBAC model. For each role, trace the full permission path. Find:

- Privilege escalation routes
- Missing permission denials (an action is attempted by a role the spec does not address)
- Cross-role conflicts enabling race conditions or data leaks

For each finding: name the role, the path taken, the spec section, assign severity (CRITICAL / HIGH / MEDIUM / LOW), and name what else is affected.

| F-ID | Type | Role | Permission Path | Spec Location | Summary | Severity | Scope |
|------|------|------|----------------|--------------|---------|----------|-------|
|      |      |      |                |              |         |          |       |

---

**TRACE FINDINGS BRIEF**

[List all findings from trace-state, trace-contract, and trace-permissions here before executing flow sub-skills.]

| F-ID | Sub-Skill | Summary | Severity |
|------|-----------|---------|----------|
|      |           |         |          |

---

**SUB-SKILL 4: flow-lifecycle**

Read the Trace Findings Brief above. Then trace the business process lifecycle for {{topic}} -- every phase, every transition, every exception path.

Look for: missing exit states, undefined phase contracts, exception flows without recovery paths, terminal states that can be reached without being declared.

For each finding: name the spec section, assign severity (CRITICAL / HIGH / MEDIUM / LOW), state blast radius. If this finding connects to a trace finding, name the trace finding by F-ID in the "Trace Link" column.

| F-ID | Type | Phase or Transition | Spec Location | Summary | Severity | Blast Radius | Trace Link |
|------|------|---------------------|--------------|---------|----------|-------------|-----------|
|      |      |                     |              |         |          |             |           |

---

**SUB-SKILL 5: flow-conversation**

Read the Trace Findings Brief above. Simulate the multi-turn conversation graph for {{topic}} -- major paths and edge paths. Find dead ends, loops, and ambiguous transitions.

For each finding: name the conversation state, the spec section, assign severity (CRITICAL / HIGH / MEDIUM / LOW), state blast radius. If this finding connects to a trace finding, name it by F-ID in the "Trace Link" column.

| F-ID | Type | Conversation State | Spec Location | Summary | Severity | Blast Radius | Trace Link |
|------|------|-------------------|--------------|---------|----------|-------------|-----------|
|      |      |                   |              |         |          |             |           |

---

**UNIFIED FINDINGS REPORT**

Collect all findings from all five sub-skills. Assign sequential F-IDs if not already assigned. Rank by blast radius: system-wide first, then cross-skill, then component-wide, then isolated. Within each tier, sort by severity (CRITICAL before HIGH before MEDIUM before LOW).

| Rank | F-ID | Sub-Skill | Type | Spec Location | Summary | Severity | Blast Radius | Remediation |
|------|------|-----------|------|--------------|---------|----------|-------------|-------------|
|      |      |           |      |              |         |          |             |             |

For all system-wide and cross-skill findings, add a blast radius rationale: name the downstream flows, components, or contracts affected.

**Execution Log**

| Sub-Skill | Status | Finding IDs |
|-----------|--------|-------------|
| trace-state | executed / no findings | |
| trace-contract | executed / no findings | |
| trace-permissions | executed / no findings | |
| flow-lifecycle | executed / no findings | |
| flow-conversation | executed / no findings | |

**Test Scenario Baseline**

For each CRITICAL or HIGH finding, derive a named test scenario:

| Scenario | F-ID | What to Exercise |
|----------|------|-----------------|
|          |      |                 |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Trace Findings Brief > per-sub-skill execution tables > Unified Findings Report (ranked) > Execution Log > Test Scenario Baseline.

All table cells are required. "Trace Link" is required for flow findings; if no trace link exists, write "none" -- not blank.

---

## V-02 -- Severity Budgets Axis

**Variation axis:** Lifecycle emphasis -- each trace sub-skill runs under an explicit severity budget. The budget requires at least one CRITICAL or HIGH finding from each trace sub-skill before the campaign can advance to flow simulation. If a trace sub-skill budget is not met, the author must state why and re-examine the sub-skill scope.

**Hypothesis:** An explicit severity budget on trace sub-skills directly closes C-11 by construction -- the prompt makes a budget miss a named failure rather than a silent omission. When all three budgets are met, at least three HIGH/CRITICAL findings exist in the corpus before flow simulation begins, making C-09 (test scenario baseline >= 3 scenarios) close by construction without requiring an explicit floor. The budget mechanism also prevents a common failure mode: trace sub-skills that run but produce only LOW/MEDIUM findings by treating everything as minor. The risk is over-pressure: a forced CRITICAL finding may produce a low-quality finding rather than a real one -- the prompt must make clear the budget can be met with "budget not met" plus rationale if the sub-skill genuinely finds nothing severe.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute all five sub-skills in order. The three trace sub-skills each carry a severity budget: you must identify at least one CRITICAL or HIGH severity finding before advancing. If the budget is not met, state why explicitly -- do not leave the budget cell blank.

---

**SEVERITY SCALE**

- **CRITICAL**: causes data loss, security breach, or system unavailability if shipped
- **HIGH**: causes incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: causes degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION SEQUENCE**

1. flow-lifecycle
2. flow-conversation
3. trace-state         (severity budget: >= 1 CRITICAL or HIGH required)
4. trace-contract      (severity budget: >= 1 CRITICAL or HIGH required)
5. trace-permissions   (severity budget: >= 1 CRITICAL or HIGH required)

---

**SUB-SKILL 1: flow-lifecycle**

Trace the business process lifecycle for {{topic}}. Walk every phase, every transition, every exception path. Find: missing exit states, undefined phase contracts, exception recovery gaps, undeclared terminal states.

For each finding record:

```
F-ID:          [F-01, F-02, ...]
Sub-skill:     flow-lifecycle
Type:          [spec-gap / flow-gap / contract-violation]
Spec location: [specific section or boundary -- "the spec is unclear" fails]
Summary:       [one sentence]
Severity:      [CRITICAL / HIGH / MEDIUM / LOW]
Blast radius:  [system-wide / cross-skill / component-wide / isolated]
Remediation:   [specific action at a named target -- not "fix the spec"]
```

---

**SUB-SKILL 2: flow-conversation**

Simulate the multi-turn conversation graph for {{topic}}. Walk major and edge paths. Find dead ends, loops, and ambiguous transitions.

For each finding record: [same schema as above, sub-skill = flow-conversation]

---

**SUB-SKILL 3: trace-state**

**SEVERITY BUDGET: This sub-skill must produce at least one CRITICAL or HIGH finding.**

Hand-compile the state machine. Write every state, every transition, every precondition and postcondition. Find:

- Exit-less states
- Transitions that can fire before their precondition is met
- Invariants named in the spec that are not enforced
- Unreachable states

For each finding record: [same schema, sub-skill = trace-state, severity column required]

**Budget Status**: [MET -- F-IDs of CRITICAL/HIGH findings] OR [NOT MET -- reason: ...]

If budget is not met, do not proceed to trace-contract. Instead, widen the scope: consider concurrent access, error paths, or edge state transitions the initial pass did not examine. Document the widened scope and re-run.

---

**SUB-SKILL 4: trace-contract**

**SEVERITY BUDGET: This sub-skill must produce at least one CRITICAL or HIGH finding.**

Identify the three most critical contract boundaries for {{topic}}. For each: state the caller's expectation, the callee's actual behavior per the spec, and any divergence. Look especially for undocumented edge case behavior at boundaries.

For each finding record: [same schema, sub-skill = trace-contract]

**Budget Status**: [MET -- F-IDs of CRITICAL/HIGH findings] OR [NOT MET -- reason: ...]

---

**SUB-SKILL 5: trace-permissions**

**SEVERITY BUDGET: This sub-skill must produce at least one CRITICAL or HIGH finding.**

Walk the RBAC model. Trace each role through the permission path. Find privilege escalation routes, missing permission denials, and cross-role conflicts.

For each finding record: [same schema, sub-skill = trace-permissions]

**Budget Status**: [MET -- F-IDs of CRITICAL/HIGH findings] OR [NOT MET -- reason: ...]

---

**SEVERITY BUDGET SUMMARY**

| Sub-Skill | Budget Status | CRITICAL/HIGH Finding IDs |
|-----------|--------------|--------------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

If any trace sub-skill budget is NOT MET, the campaign cannot advance to synthesis. Re-examine that sub-skill with wider scope.

---

**SYNTHESIS: UNIFIED FINDINGS REPORT**

Collect all findings. Rank by blast radius, then severity within tier.

| Rank | F-ID | Sub-Skill | Type | Spec Location | Summary | Severity | Blast Radius | Remediation |
|------|------|-----------|------|--------------|---------|----------|-------------|-------------|
|      |      |           |      |              |         |          |             |             |

**Execution Log**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |

**Test Scenario Baseline**

All CRITICAL and HIGH findings produce a named test scenario. The baseline must contain at least as many scenarios as CRITICAL/HIGH findings in the corpus.

| Scenario | F-ID | Severity | What to Exercise |
|----------|------|----------|-----------------|
|          |      |          |                 |

**Cross-Skill Patterns**

| P-ID | Root Cause | F-IDs | Elevated Blast Radius |
|------|------------|-------|----------------------|
|      |            |       |                       |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: per-sub-skill execution (each with severity budget status) > Severity Budget Summary > Unified Findings Report > Execution Log > Test Scenario Baseline > Cross-Skill Patterns.

Campaign does not complete if any trace sub-skill budget is not met without rationale.

---

## V-03 -- No-Blank-Cell Table Contract Axis

**Variation axis:** Output format -- a unified findings table is the primary artifact. The table schema is defined before any sub-skill executes, and a strict no-blank-cell contract governs every row. Every column is populated for every finding; missing values must use explicit sentinels (N/A with rationale) rather than blank cells.

**Hypothesis:** A no-blank-cell table contract directly closes C-12 by construction: blank cells are a named failure mode, not a formatting omission. The contract also makes C-03 and C-07 failures structurally visible -- a finding without a system boundary or sub-skill citation cannot hide in prose. The sentinel rule ("N/A with rationale" rather than blank) forces the author to acknowledge missing data explicitly, which is more useful than silent omission. The risk is that the table structure may cause shallow per-row entries as the author fills cells minimally to satisfy the contract -- the schema description must make clear that "summary" and "remediation" require actionable content, not placeholder text.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute all five sub-skills in order. Every finding goes into the unified findings table. No cell in any finding row may be blank -- use "N/A -- [reason]" if a field genuinely does not apply. A blank cell is a failed finding.

---

**FINDINGS TABLE SCHEMA**

Define this table before running any sub-skill. Add rows as findings are discovered.

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-------------|

Column definitions (all required; no blanks):

- **F-ID**: F-01, F-02, ... sequential across all sub-skills
- **Sub-Skill**: flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions
- **System Boundary**: the specific boundary where the finding was detected -- state machine / contract surface / permission check / lifecycle phase / conversation state
- **Type**: spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap
- **Spec Location**: the specific spec section, interface name, or contract boundary -- "the spec is unclear" fails; must name a location
- **Summary**: one sentence describing the problem -- not a category label; describe the specific problem
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **Blast Radius**: system-wide / cross-skill / component-wide / isolated
- **Remediation**: specific action at a named target -- "fix the spec" fails; name the section and the required change

**No-blank-cell enforcement rules:**

1. Every row must have all nine columns populated.
2. If a column does not apply, write "N/A -- [reason]" -- not blank, not a dash.
3. "Unknown" is not acceptable for Spec Location or Remediation -- investigate until a location or action can be named, or flag the finding as a research item with "Spec Location: TBD -- [what to investigate]" and a remediation of "Investigate [specific question]".
4. Severity and Blast Radius use only the enumerated values above. No free-text severity labels.

---

**EXECUTION SEQUENCE**

1. flow-lifecycle
2. flow-conversation
3. trace-state
4. trace-contract
5. trace-permissions

After each sub-skill, add its findings to the table before advancing. Do not batch all sub-skills first and add rows at the end -- the table grows incrementally.

---

**SUB-SKILL 1: flow-lifecycle**

Trace the business process lifecycle for {{topic}} phase by phase. At every transition: does the spec define exactly what happens? At every exception path: does the spec provide a recovery path? Find missing states, undefined contracts, and orphaned terminal paths.

Add findings to the table as discovered. Every finding needs all nine columns.

---

**SUB-SKILL 2: flow-conversation**

Simulate the multi-turn conversation graph for {{topic}}. Walk major paths and edge paths. Find dead ends (no valid next action), loops (returns to prior state without resolution), ambiguous transitions (spec does not define the next state).

Add findings to the table. Every finding needs all nine columns.

---

**SUB-SKILL 3: trace-state**

Hand-compile the state machine. Write every state, every transition, every precondition and postcondition. Find exit-less states, early-firing transitions, unenforced invariants, and unreachable states.

Add findings to the table. Severity must be one of the four enumerated values -- do not write "moderate" or "severe."

---

**SUB-SKILL 4: trace-contract**

Identify the most critical contract boundaries for {{topic}}. For each boundary: state caller expectation, callee behavior per spec, and any mismatch. Find undocumented edge case behavior.

Add findings to the table. Spec Location must name the interface or section -- not "the API contract."

---

**SUB-SKILL 5: trace-permissions**

Walk the RBAC model. Trace each role's permission path. Find privilege escalation routes, missing denials, and cross-role conflicts.

Add findings to the table. System Boundary = "permission check." Role and path must appear in the Summary column.

---

**FINDINGS TABLE (complete)**

[Insert the completed table here with all findings from all five sub-skills. Verify: no blank cells, all F-IDs assigned, all severity values from the enumerated set.]

---

**RANKED FINDINGS**

Re-sort the findings table by blast radius (system-wide first) then severity within each tier. Assign a Rank column.

For all system-wide and cross-skill findings, add a blast radius rationale section below the table: name the downstream flows, components, or contracts affected.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs Added |
|-----------|--------|------------------|
| flow-lifecycle | executed / no findings | |
| flow-conversation | executed / no findings | |
| trace-state | executed / no findings | |
| trace-contract | executed / no findings | |
| trace-permissions | executed / no findings | |

A sub-skill with "no findings" must add a row with all nine columns populated, Summary = "No findings", Remediation = "None required -- [reason]". No blank cells even for clean sub-skills.

---

**TEST SCENARIO BASELINE**

From all HIGH and CRITICAL findings, derive named test scenarios:

| Scenario | F-ID | What to Exercise | Acceptance Condition |
|----------|------|-----------------|---------------------|
|          |      |                 |                     |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections: Findings Table (incremental adds per sub-skill, all cells populated) > Ranked Findings (blast-radius sort with top-tier rationale) > Execution Log > Test Scenario Baseline.

Before writing the output file, verify: zero blank cells, all severity values from the enumerated set, all spec locations name a specific section or boundary.

---

## V-04 -- Combined (Trace-First Ordering + Severity Budgets)

**Variation axes combined:**
1. Role sequence -- trace sub-skills execute before flow sub-skills (V-01 axis)
2. Lifecycle emphasis -- each trace sub-skill has an explicit severity budget requiring >= 1 CRITICAL or HIGH finding (V-02 axis)

**Hypothesis:** The combination closes C-11 (severity budgets per trace sub-skill) and C-13 (flow findings reference trace context) simultaneously. The trace-first ordering ensures a populated trace findings corpus before flow runs; the severity budget ensures that corpus contains at least three HIGH/CRITICAL findings for flow sub-skills to reference. Flow findings that cannot reference any trace finding despite the non-empty corpus represent a genuine synthesis gap, making C-13 failures easier to detect. The combined prompt also closes C-09 by construction: if three trace budgets are met, three CRITICAL/HIGH findings exist as test scenario seeds without requiring an explicit floor count. The risk is prompt length -- the combined variation is longer, and the author may follow the structure mechanically rather than analytically.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute trace sub-skills first, then flow sub-skills. Each trace sub-skill carries a severity budget. Flow sub-skills receive a trace findings brief before executing.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION ORDER**

1. trace-state         (severity budget: >= 1 CRITICAL or HIGH)
2. trace-contract      (severity budget: >= 1 CRITICAL or HIGH)
3. trace-permissions   (severity budget: >= 1 CRITICAL or HIGH)
   -- PAUSE: write Trace Findings Brief --
4. flow-lifecycle      (reads Trace Findings Brief before executing)
5. flow-conversation   (reads Trace Findings Brief before executing)

---

**SUB-SKILL 1: trace-state**

**SEVERITY BUDGET: >= 1 CRITICAL or HIGH required**

Hand-compile the state machine for {{topic}}. Write every state, transition, precondition, and postcondition. Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

For each finding:

```
F-ID:          [F-01, F-02, ...]
Sub-skill:     trace-state
Type:          state-anomaly
Spec location: [specific section or state machine definition]
Summary:       [one sentence -- name the specific state or transition]
Severity:      [CRITICAL / HIGH / MEDIUM / LOW]
Blast radius:  [system-wide / cross-skill / component-wide / isolated]
Remediation:   [specific change at a named location]
```

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- re-examine: widened scope: ...]

---

**SUB-SKILL 2: trace-contract**

**SEVERITY BUDGET: >= 1 CRITICAL or HIGH required**

Identify the three most critical contract boundaries for {{topic}}. State caller expectation, callee behavior per spec, and any divergence. Find undocumented edge case behaviors.

For each finding: [same schema, sub-skill = trace-contract, type = contract-violation or spec-gap]

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- re-examine: ...]

---

**SUB-SKILL 3: trace-permissions**

**SEVERITY BUDGET: >= 1 CRITICAL or HIGH required**

Walk the RBAC model. Trace each role's permission path. Find privilege escalation routes, missing denials, cross-role conflicts.

For each finding: [same schema, sub-skill = trace-permissions, type = permission-gap or spec-gap]

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- re-examine: ...]

---

**SEVERITY BUDGET GATE**

Before continuing to flow sub-skills, verify all three budgets are met:

| Sub-Skill | Budget | CRITICAL/HIGH F-IDs |
|-----------|--------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

If any budget is NOT MET: do not continue. Widen scope and re-run that sub-skill.

---

**TRACE FINDINGS BRIEF**

[Compile all trace findings here. Flow sub-skills read this before executing.]

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius |
|------|-----------|------|---------|----------|-------------|
|      |           |      |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle**

Read the Trace Findings Brief. Then trace the business process lifecycle for {{topic}} -- every phase, transition, and exception path. Find missing exit states, undefined phase contracts, exception recovery gaps.

For each finding: [same schema, sub-skill = flow-lifecycle]

**Trace link check**: For each flow finding, scan the Trace Findings Brief. If any trace finding is related -- same root cause, same spec section, or the flow anomaly is downstream of the trace anomaly -- add a "Trace Link" field naming the trace F-ID. At least one flow finding must carry a Trace Link.

---

**SUB-SKILL 5: flow-conversation**

Read the Trace Findings Brief. Simulate the multi-turn conversation graph for {{topic}} -- major and edge paths. Find dead ends, loops, ambiguous transitions.

For each finding: [same schema, sub-skill = flow-conversation]

**Trace link check**: Apply the same cross-reference scan. Name any trace F-ID that is linked to a flow finding.

---

**SYNTHESIS: UNIFIED FINDINGS REPORT**

Collect all findings. Rank by blast radius (system-wide > cross-skill > component-wide > isolated), then severity within tier.

| Rank | F-ID | Sub-Skill | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|------|-----------|------|--------------|---------|----------|-------------|-----------|-------------|
|      |      |           |      |              |         |          |             |           |             |

For all system-wide and cross-skill findings: add blast radius rationale naming affected flows, components, or contracts.

**Execution Log**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | | | MET / NOT MET |
| trace-contract | | | MET / NOT MET |
| trace-permissions | | | MET / NOT MET |
| flow-lifecycle | | | N/A |
| flow-conversation | | | N/A |

**Test Scenario Baseline**

All CRITICAL and HIGH findings become named test scenarios:

| Scenario | F-ID | Severity | What to Exercise |
|----------|------|----------|-----------------|
|          |      |          |                 |

**Cross-Skill Patterns**

| P-ID | Root Cause | F-IDs | Elevated Blast Radius |
|------|------------|-------|----------------------|
|      |            |       |                      |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections: trace sub-skill executions (each with budget status) > Severity Budget Gate > Trace Findings Brief > flow sub-skill executions (each with trace link check) > Unified Findings Report > Execution Log > Test Scenario Baseline > Cross-Skill Patterns.

Campaign does not complete without a passing Severity Budget Gate and at least one flow finding carrying a Trace Link.

---

## V-05 -- Combined (Trace-First + Severity Budgets + No-Blank-Cell Table)

**Variation axes combined:**
1. Role sequence -- trace-first ordering (V-01 axis)
2. Lifecycle emphasis -- severity budgets per trace sub-skill (V-02 axis)
3. Output format -- no-blank-cell table contract (V-03 axis)

**Hypothesis:** This is the maximum-structure variant. It closes all three v2 aspirational criteria by construction: C-11 via severity budgets, C-13 via the trace-first brief protocol and mandatory Trace Link column, C-12 via the no-blank-cell table contract with sentinel enforcement. With all three trace budgets met and a populated trace corpus before flow simulation, the test scenario baseline (C-09) and finding ID assignment (C-10) follow without additional prompting -- the structure forces them. The risk is that maximum scaffolding produces mechanical rather than analytical outputs: the author fills every cell with minimal content to pass the structural checks without genuinely simulating. The severity scale definitions and the sentinel enforcement rules must be specific enough to prevent this failure mode.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute trace sub-skills first (with severity budgets), then flow sub-skills (with trace findings brief). Enter every finding into the unified table. No cell in any finding row may be blank.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**FINDINGS TABLE SCHEMA**

One table. All findings from all sub-skills. Populated incrementally as sub-skills execute.

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No-blank-cell rules:
- Every row has all ten columns populated
- If a column does not apply: "N/A -- [reason]" -- not blank, not a dash
- Spec Location must name a specific section or boundary -- never "the spec is unclear"
- Remediation must name a target and a change -- never "fix the spec"
- Severity uses only the four enumerated values above
- Blast Radius uses only: system-wide / cross-skill / component-wide / isolated
- Trace Link: F-ID of related trace finding, or "none" -- never blank

---

**EXECUTION ORDER**

1. trace-state         (severity budget: >= 1 CRITICAL or HIGH; add rows to table)
2. trace-contract      (severity budget: >= 1 CRITICAL or HIGH; add rows to table)
3. trace-permissions   (severity budget: >= 1 CRITICAL or HIGH; add rows to table)
   -- PAUSE: verify budget gate, write Trace Findings Brief --
4. flow-lifecycle      (read brief; add rows to table; populate Trace Link column)
5. flow-conversation   (read brief; add rows to table; populate Trace Link column)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Write every state, transition, precondition, and postcondition. Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row in the findings table. All ten columns required.

System Boundary for trace-state findings: "state machine"

**Budget status after this sub-skill**: [MET -- F-IDs with CRITICAL or HIGH: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Identify the three most important contract boundaries for {{topic}}. For each: state caller expectation, callee behavior per spec, and the divergence. Find undocumented edge case behaviors at interfaces.

Add findings to the table. System Boundary = "contract surface."

**Budget status after this sub-skill**: [MET -- F-IDs with CRITICAL or HIGH: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Trace each role through the permission path. Find privilege escalation routes, missing denials, and cross-role conflicts.

Add findings to the table. System Boundary = "permission check."

**Budget status after this sub-skill**: [MET -- F-IDs with CRITICAL or HIGH: ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run. If any is NOT MET without rationale, the campaign halts.

---

**TRACE FINDINGS BRIEF**

[Compile all trace rows from the findings table.]

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief)

Read the Trace Findings Brief. Then trace the business process lifecycle for {{topic}} phase by phase. Find missing exit states, undefined phase contracts, exception paths without recovery, undeclared terminal states.

Add findings to the table. System Boundary = "lifecycle phase."

For each finding, populate Trace Link by scanning the brief: if this flow finding is downstream of, caused by, or shares a root cause with any trace finding, name the trace F-ID. If no link: "none."

At least one flow-lifecycle finding must have a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief)

Read the Trace Findings Brief. Simulate the multi-turn conversation graph for {{topic}}. Walk major and edge paths. Find dead ends, loops, ambiguous transitions.

Add findings to the table. System Boundary = "conversation state."

Same Trace Link requirement: populate from the brief. If no link: "none."

---

**FINDINGS TABLE (complete)**

[Insert the full findings table here with all rows from all five sub-skills. Verify before writing:
- Zero blank cells
- All severity values from the enumerated set
- All spec locations name a specific section or boundary
- All trace links populated ("none" is acceptable; blank is not)
- All remediation entries name a target and a specific change]

---

**RANKED FINDINGS**

Re-sort the complete findings table by blast radius (system-wide first) then severity within tier. Add a Rank column at left.

For all system-wide and cross-skill findings, add blast radius rationale immediately below the sorted table: name the downstream flows, components, or contracts affected and explain why the scope reaches that far.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

A sub-skill with "no findings" still gets a row in the findings table: Summary = "No findings detected", Remediation = "None required -- [reason]", all other cells populated. No blank cells.

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario. The baseline must have at least as many scenarios as there are CRITICAL/HIGH findings in the table.

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

Scan for single root causes that appear across two or more sub-skills. For each compounding pattern:

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why the scope is wider than any single finding |
|------|------------|-------|----------------------|------------------------------------------------|
|      |            |       |                      |                                                |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. trace sub-skill executions (each with budget status)
2. Severity Budget Gate table
3. Trace Findings Brief
4. flow sub-skill executions (each with trace link check)
5. Findings Table (complete, all cells populated)
6. Ranked Findings (blast-radius sorted, with top-tier rationale)
7. Execution Log
8. Test Scenario Baseline
9. Cross-Skill Patterns

Before writing the file, run a blank-cell check: every row, every column. Any blank found -- fill it or mark N/A with a reason.
