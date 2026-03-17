---
skill: campaign-simulate
round: 3
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v3-2026-03-17.md
---

# campaign-simulate -- Round 3 Variations

Round 3 targets the five new aspirational criteria introduced in rubric v3 (C-14 through C-18).
V-05 from Round 2 already satisfies all five -- Round 3 explores whether the same compliance can be
achieved with cleaner mechanisms, and whether any alternative formulation produces new excellence patterns.

- **C-14**: System boundary vocabulary pre-assigned per sub-skill (verbatim copy, not model judgment)
- **C-15**: Universal sentinel rule -- no column ever blank, including optional columns
- **C-16**: No-findings sentinel rows for clean sub-skills (absent row = execution gap)
- **C-17**: Pre-output blank-cell verification gate as a named, explicit checklist item
- **C-18**: One unified 10-column table that satisfies C-03, C-07, C-10, and C-13 simultaneously

**Variation axes this round**:

Single-axis: V-01 (schema-declaration first), V-02 (sentinel manifest pre-generation), V-03 (verification-gate-as-section).
Combined: V-04 (schema-declaration + sentinel manifest), V-05 (schema-declaration + sentinel manifest + verification-gate-as-section).

---

## V-01 -- Schema-Declaration Axis

**Variation axis:** Output format -- the unified 10-column schema and the five pre-assigned boundary
vocabulary labels are declared at the very top of the prompt, before any sub-skill instruction.
The author reads the schema contract and the vocabulary map before encountering any execution directive.

**Hypothesis:** C-14 requires that boundary labels are pre-assigned vocabulary, not model inference.
When the schema contract and the boundary map appear first, compliance becomes a transcription from
the opening contract rather than a recall from buried sub-skill instructions. The author is locked into
the vocabulary map from the first line they read. This also closes C-18 by construction: the author
knows the unified schema before deciding how to structure findings, preventing multi-table drift.
The risk is that a long opening contract may be skimmed rather than read; the vocabulary map must be
visually distinct (a two-column lookup table) to be noticed.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign.

---

**SCHEMA CONTRACT** (read before writing any finding)

One unified table receives all findings from all sub-skills:

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

**Pre-assigned boundary vocabulary -- copy verbatim, do not infer:**

| Sub-Skill | System Boundary |
|-----------|----------------|
| trace-state | state machine |
| trace-contract | contract surface |
| trace-permissions | permission check |
| flow-lifecycle | lifecycle phase |
| flow-conversation | conversation state |

**Severity enumeration** (no other values):
- CRITICAL: data loss, security breach, or system unavailability if shipped
- HIGH: incorrect behavior, contract violation, or blocked user flow if shipped
- MEDIUM: degraded behavior, performance issue, or misleading output
- LOW: minor inconsistency, cosmetic, or documentation gap

**Blast Radius enumeration**: system-wide / cross-skill / component-wide / isolated

**No-blank-cell contract**: every cell in every row must be populated.
- Optional fields that do not apply: "N/A -- [reason]" -- not blank, not a dash
- Trace Link: the F-ID of a related trace finding, or "none" -- never blank
- Spec Location: a specific section or boundary name -- never "the spec is unclear"
- Remediation: a named target and specific change -- never "fix the spec"

A sub-skill with no findings must still appear in the table as a sentinel row:
Summary = "No findings detected", Remediation = "None required -- [reason]", all other cells populated.

---

**EXECUTION ORDER**

1. trace-state        (severity budget: >= 1 CRITICAL or HIGH | boundary: "state machine")
2. trace-contract     (severity budget: >= 1 CRITICAL or HIGH | boundary: "contract surface")
3. trace-permissions  (severity budget: >= 1 CRITICAL or HIGH | boundary: "permission check")
   -- PAUSE: verify severity budget gate, write Trace Findings Brief --
4. flow-lifecycle     (reads brief | boundary: "lifecycle phase" | populate Trace Link)
5. flow-conversation  (reads brief | boundary: "conversation state" | populate Trace Link)

---

**SUB-SKILL 1: trace-state** (boundary: "state machine" | severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Write every state, every transition, every precondition
and postcondition. Find:
- Exit-less states (a caller that enters cannot proceed)
- Transitions that fire before their precondition is met
- Invariants named in the spec that are not enforced
- Unreachable states (no path from the initial state)

Add each finding as a row. System Boundary = "state machine" (from the schema contract above).

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (boundary: "contract surface" | severity budget: >= 1 CRITICAL or HIGH)

Identify the three most important contract boundaries for {{topic}}. For each: state the caller's
expectation, the callee's behavior per the spec, and any divergence. Find undocumented edge case
behaviors at interfaces.

Add findings to the table. System Boundary = "contract surface" (from the schema contract above).

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (boundary: "permission check" | severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Trace each role through the permission path. Find privilege escalation routes,
missing denials, and cross-role conflicts.

Add findings to the table. System Boundary = "permission check" (from the schema contract above).

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

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

[Compile all trace rows from the findings table. Flow sub-skills read this before executing.]

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (boundary: "lifecycle phase" | reads Trace Findings Brief)

Read the Trace Findings Brief. Then trace the business process lifecycle for {{topic}} phase by phase.
Find missing exit states, undefined phase contracts, exception paths without recovery, undeclared
terminal states.

Add findings to the table. System Boundary = "lifecycle phase" (from the schema contract above).

For each finding, scan the brief: if this flow finding is downstream of, caused by, or shares a root
cause with any trace finding, name the trace F-ID in the Trace Link column. If no link: "none."

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (boundary: "conversation state" | reads Trace Findings Brief)

Read the Trace Findings Brief. Simulate the multi-turn conversation graph for {{topic}}. Walk major
and edge paths. Find dead ends, loops, ambiguous transitions.

Add findings to the table. System Boundary = "conversation state" (from the schema contract above).

Same Trace Link requirement: populate from the brief. If no link: "none."

---

**FINDINGS TABLE (complete)**

[Insert the full findings table here. Confirm before inserting:
- All System Boundary values match the vocabulary map in the schema contract exactly
- Zero blank cells
- All severity and blast-radius values from the enumerated sets
- All spec locations name a specific section or boundary
- All Trace Link cells populated ("none" acceptable; blank is not)
- Every sub-skill has at least one row]

---

**RANKED FINDINGS**

Re-sort the findings table by blast radius (system-wide first) then severity within tier. Add Rank column.

For all system-wide and cross-skill findings: add blast radius rationale naming the downstream flows,
components, or contracts affected.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario:

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why scope is wider than any single finding |
|------|------------|-------|----------------------|------------------------------------------|
|      |            |       |                      |                                           |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. trace sub-skill executions (each with budget status)
2. Severity Budget Gate
3. Trace Findings Brief
4. flow sub-skill executions (each with trace link check)
5. Findings Table (complete, all cells populated)
6. Ranked Findings (blast-radius sorted, top-tier rationale)
7. Execution Log
8. Test Scenario Baseline
9. Cross-Skill Patterns

Before writing: run blank-cell check. Every row, every column. Any blank found -- fill it or mark
"N/A -- [reason]". Verify all System Boundary values match the schema contract vocabulary exactly.

---

## V-02 -- Sentinel-Manifest Axis

**Variation axis:** Output format -- before any sub-skill executes, a Sentinel Manifest is written.
The manifest pre-authors the clean-run sentinel row for every sub-skill: its assigned boundary label,
a standard summary, and a standard remediation. When a sub-skill has no findings, the author copies
the manifest row verbatim into the findings table.

**Hypothesis:** C-16 requires a sentinel row for every clean sub-skill. The failure mode is not
forgetting the rule -- it is forgetting to add the row when a sub-skill finishes cleanly, because
the author's attention is on findings, not on absence-of-findings. Pre-writing the sentinel rows
at the start eliminates this: the rows exist before execution begins. Copy-paste is less error-prone
than on-demand authoring. The manifest also implicitly enforces C-14 and C-15: the pre-assigned
boundary vocabulary appears in the manifest, and the manifest rows demonstrate fully-populated cells.
The risk is the manifest being treated as boilerplate -- authors may copy sentinel rows even when
findings exist, omitting real issues.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute trace sub-skills first (with severity
budgets), then flow sub-skills (with trace findings brief). Every finding and every clean-run
sentinel enters the unified findings table.

---

**SEVERITY SCALE**

- CRITICAL: data loss, security breach, or system unavailability if shipped
- HIGH: incorrect behavior, contract violation, or blocked user flow if shipped
- MEDIUM: degraded behavior, performance issue, or misleading output
- LOW: minor inconsistency, cosmetic, or documentation gap

---

**STEP 0: WRITE THE SENTINEL MANIFEST BEFORE EXECUTING ANY SUB-SKILL**

Before running any sub-skill, write the Sentinel Manifest. This is the template to use if a
sub-skill produces no findings. Copy the manifest row verbatim into the findings table for that
sub-skill when its execution is clean.

| Sub-Skill | System Boundary | Sentinel Summary | Sentinel Remediation |
|-----------|----------------|-----------------|---------------------|
| trace-state | state machine | No findings detected in state machine trace | None required -- full state machine traversal completed without anomalies |
| trace-contract | contract surface | No findings detected in contract surface trace | None required -- all contract boundaries matched expected behavior |
| trace-permissions | permission check | No findings detected in permission path trace | None required -- RBAC traversal completed without escalation routes or missing denials |
| flow-lifecycle | lifecycle phase | No findings detected in lifecycle phase trace | None required -- all phases have defined contracts and exception recovery paths |
| flow-conversation | conversation state | No findings detected in conversation state trace | None required -- no dead ends, loops, or ambiguous transitions found |

Rules:
- If a sub-skill produces >= 1 finding: add only the real findings. Do not add the sentinel row.
- If a sub-skill produces 0 findings: copy its manifest row verbatim into the findings table.
- A sub-skill absent from the findings table = execution gap, regardless of the execution log.

---

**FINDINGS TABLE SCHEMA**

One table. All real findings and all sentinel rows from all five sub-skills.

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No-blank-cell contract:
- Every row has all ten columns populated
- If a column does not apply: "N/A -- [reason]" -- not blank, not a dash
- System Boundary: copy from the Sentinel Manifest -- never infer or substitute
- Severity: CRITICAL / HIGH / MEDIUM / LOW only
- Blast Radius: system-wide / cross-skill / component-wide / isolated only
- Trace Link: F-ID of a related trace finding, or "none" -- never blank
- Spec Location: a specific section or boundary name -- never "the spec is unclear"
- Remediation: a named target and a specific change -- never "fix the spec"

---

**EXECUTION ORDER**

1. trace-state        (severity budget: >= 1 CRITICAL or HIGH | add rows or copy manifest sentinel)
2. trace-contract     (severity budget: >= 1 CRITICAL or HIGH | add rows or copy manifest sentinel)
3. trace-permissions  (severity budget: >= 1 CRITICAL or HIGH | add rows or copy manifest sentinel)
   -- PAUSE: verify budget gate, write Trace Findings Brief --
4. flow-lifecycle     (reads brief | add rows or copy manifest sentinel | populate Trace Link)
5. flow-conversation  (reads brief | add rows or copy manifest sentinel | populate Trace Link)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Every state, every transition, every precondition
and postcondition. Find: exit-less states, early-firing transitions, unenforced invariants,
unreachable states.

Add findings to the table. System Boundary = "state machine" (from manifest).
If no findings: copy the trace-state sentinel row from the manifest verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Three most important contract boundaries. Caller expectation, callee behavior per spec, divergence.
Find undocumented edge case behaviors at interfaces.

Add findings to the table. System Boundary = "contract surface" (from manifest).
If no findings: copy the trace-contract sentinel row from the manifest verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Each role's permission path. Privilege escalation routes, missing denials,
cross-role conflicts.

Add findings to the table. System Boundary = "permission check" (from manifest).
If no findings: copy the trace-permissions sentinel row from the manifest verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without rationale, the campaign halts.

---

**TRACE FINDINGS BRIEF**

[Compile all trace rows from the findings table.]

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief)

Read the Trace Findings Brief. Trace the lifecycle for {{topic}} phase by phase. Missing exit states,
undefined phase contracts, exception recovery gaps, undeclared terminal states.

Add findings to the table. System Boundary = "lifecycle phase" (from manifest).
If no findings: copy the flow-lifecycle sentinel row from the manifest verbatim.

For each real finding: scan the brief. If this finding is downstream of, caused by, or shares a root
cause with any trace finding, name the trace F-ID in Trace Link. If no link: "none."
At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief)

Read the Trace Findings Brief. Simulate the conversation graph for {{topic}}. Major and edge paths.
Dead ends, loops, ambiguous transitions.

Add findings to the table. System Boundary = "conversation state" (from manifest).
If no findings: copy the flow-conversation sentinel row from the manifest verbatim.

---

**FINDINGS TABLE (complete)**

[Insert the full findings table. Every sub-skill must appear -- as real findings or as the manifest
sentinel row. Confirm: no blank cells, all boundary labels match the manifest vocabulary.]

---

**RANKED FINDINGS**

Re-sort by blast radius (system-wide first), then severity within tier. Add Rank column.
Top-tier findings: add blast radius rationale naming affected flows, components, or contracts.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario:

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why scope is wider than any single finding |
|------|------------|-------|----------------------|------------------------------------------|
|      |            |       |                      |                                           |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. Sentinel Manifest (Step 0 -- written before execution)
2. trace sub-skill executions (each with budget status)
3. Severity Budget Gate
4. Trace Findings Brief
5. flow sub-skill executions (each with trace link check)
6. Findings Table (complete -- every sub-skill present, no blank cells)
7. Ranked Findings
8. Execution Log
9. Test Scenario Baseline
10. Cross-Skill Patterns

Before writing: confirm every sub-skill has at least one row (real finding or manifest sentinel).
Confirm no blank cells.

---

## V-03 -- Verification-Gate-as-Section Axis

**Variation axis:** Output format -- the blank-cell verification gate (C-17) is elevated from an
embedded output instruction to a named, first-class section in the output structure. The section
produces a structured per-column audit table with explicit PASS/FAIL per column and an Overall status.
The output file is not written until Overall = PASS.

**Hypothesis:** C-17 requires that the verification gate "must be labeled or documented as a gate,
not implied by the absence of blank cells." When the gate is a named section with a per-column audit
table, it is inspectable by rubric evaluators independently of the findings table -- a blank cell
cannot be hidden. The audit table also serves as a self-correction mechanism: a FAIL on any column
forces the author to name exactly which cells failed before continuing. The risk is that the gate
becomes theater -- the author marks all columns PASS without actually auditing. The gate must list
actual blank-cell counts, not just a checkbox.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute trace sub-skills first (with severity
budgets), then flow sub-skills (with trace findings brief). All findings enter the unified table.
A named Blank-Cell Verification Gate section must appear in the output before the file is written.

---

**SEVERITY SCALE**

- CRITICAL: data loss, security breach, or system unavailability if shipped
- HIGH: incorrect behavior, contract violation, or blocked user flow if shipped
- MEDIUM: degraded behavior, performance issue, or misleading output
- LOW: minor inconsistency, cosmetic, or documentation gap

---

**FINDINGS TABLE SCHEMA**

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No-blank-cell contract:
- Every row has all ten columns populated
- Optional fields that do not apply: "N/A -- [reason]" -- not blank, not a dash
- System Boundary: state machine / contract surface / permission check / lifecycle phase / conversation state
- Severity: CRITICAL / HIGH / MEDIUM / LOW only
- Blast Radius: system-wide / cross-skill / component-wide / isolated only
- Trace Link: F-ID of a related trace finding, or "none" -- never blank
- Spec Location: specific section or boundary -- never "the spec is unclear"
- Remediation: named target and specific change -- never "fix the spec"

---

**EXECUTION ORDER**

1. trace-state        (severity budget: >= 1 CRITICAL or HIGH | System Boundary = "state machine")
2. trace-contract     (severity budget: >= 1 CRITICAL or HIGH | System Boundary = "contract surface")
3. trace-permissions  (severity budget: >= 1 CRITICAL or HIGH | System Boundary = "permission check")
   -- PAUSE: verify budget gate, write Trace Findings Brief --
4. flow-lifecycle     (reads brief | System Boundary = "lifecycle phase" | populate Trace Link)
5. flow-conversation  (reads brief | System Boundary = "conversation state" | populate Trace Link)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Every state, every transition, every precondition
and postcondition. Find: exit-less states, early-firing transitions, unenforced invariants,
unreachable states.

Add findings to the table. System Boundary = "state machine."

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Three most important contract boundaries. Caller expectation, callee behavior per spec, divergence.
Find undocumented edge case behaviors.

Add findings to the table. System Boundary = "contract surface."

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Each role's permission path. Privilege escalation, missing denials,
cross-role conflicts.

Add findings to the table. System Boundary = "permission check."

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without rationale, the campaign halts.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief)

Read the brief. Trace the lifecycle for {{topic}} phase by phase. Missing exit states, undefined
phase contracts, exception recovery gaps, undeclared terminal states.

Add findings to the table. System Boundary = "lifecycle phase."

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief)

Read the brief. Simulate the conversation graph for {{topic}}. Dead ends, loops, ambiguous transitions.

Add findings to the table. System Boundary = "conversation state."

A sub-skill with no findings gets a sentinel row: Summary = "No findings detected",
Remediation = "None required -- [reason]", all other cells populated.

---

**FINDINGS TABLE (complete)**

[Insert full findings table. All sub-skills present. All cells populated.]

---

**RANKED FINDINGS**

Re-sort by blast radius (system-wide first), then severity within tier. Add Rank column.
Top-tier findings: add blast radius rationale naming affected flows, components, or contracts.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

---

## BLANK-CELL VERIFICATION GATE

Before writing the output file, audit the findings table. For each column: count blank cells found,
record the action taken, and mark PASS (0 blank cells after action) or FAIL.

| Column | Blank Cells Found | Action Taken | Status |
|--------|------------------|-------------|--------|
| F-ID | 0 / N | [none / filled] | PASS / FAIL |
| Sub-Skill | 0 / N | [none / filled] | PASS / FAIL |
| System Boundary | 0 / N | [none / vocabulary-corrected] | PASS / FAIL |
| Type | 0 / N | [none / filled] | PASS / FAIL |
| Spec Location | 0 / N | [none / specified] | PASS / FAIL |
| Summary | 0 / N | [none / filled] | PASS / FAIL |
| Severity | 0 / N | [none / enumerated] | PASS / FAIL |
| Blast Radius | 0 / N | [none / enumerated] | PASS / FAIL |
| Trace Link | 0 / N | [none / "none" written] | PASS / FAIL |
| Remediation | 0 / N | [none / targeted] | PASS / FAIL |
| **Overall** | | **All columns must PASS** | **PASS / FAIL** |

Do not write the output file until Overall = PASS. If any column shows FAIL after action: revisit
those rows and fill or mark "N/A -- [reason]" before proceeding.

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario:

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why scope is wider than any single finding |
|------|------------|-------|----------------------|------------------------------------------|
|      |            |       |                      |                                           |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. trace sub-skill executions (each with budget status)
2. Severity Budget Gate
3. Trace Findings Brief
4. flow sub-skill executions (each with trace link check)
5. Findings Table (complete)
6. Ranked Findings
7. Execution Log
8. **BLANK-CELL VERIFICATION GATE** (per-column audit table, Overall = PASS)
9. Test Scenario Baseline
10. Cross-Skill Patterns

The output file must contain the Blank-Cell Verification Gate section. A file without this section
has an incomplete verification record.

---

## V-04 -- Combined (Schema-Declaration + Sentinel-Manifest)

**Variation axes combined:**
1. Output format -- schema and boundary vocabulary declared first (V-01 axis)
2. Output format -- sentinel manifest pre-written before any sub-skill executes (V-02 axis)

**Hypothesis:** V-01 locks the author into the schema contract and boundary vocabulary from the first
line. V-02 pre-authors the sentinel rows before execution begins. Together, they close C-14 (boundary
labels are a transcription from the schema contract header) and C-16 (sentinel rows are a copy from
the manifest, not authored from memory after the fact). C-15 and C-18 follow from the schema contract
declaration. The combination means every structural compliance requirement is satisfied by setup
artifacts (schema contract, manifest) that exist before any sub-skill runs, rather than by per-skill
instructions scattered through the prompt. The risk is prompt length and the perception that two setup
sections are redundant -- the vocabulary map (V-01) and the manifest (V-02) both carry the boundary
labels. They serve different purposes: the vocabulary map is the lookup table for writing findings;
the manifest is the pre-written content for clean runs.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign.

---

**SCHEMA CONTRACT** (read before writing any finding)

All findings from all sub-skills enter one unified table:

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

**Boundary vocabulary -- copy verbatim:**

| Sub-Skill | System Boundary |
|-----------|----------------|
| trace-state | state machine |
| trace-contract | contract surface |
| trace-permissions | permission check |
| flow-lifecycle | lifecycle phase |
| flow-conversation | conversation state |

**Severity** (enumerated): CRITICAL / HIGH / MEDIUM / LOW
**Blast Radius** (enumerated): system-wide / cross-skill / component-wide / isolated

**No-blank-cell contract**: every cell populated; optional fields: "N/A -- [reason]";
Trace Link: F-ID or "none" -- never blank.

---

**SENTINEL MANIFEST** (written before any sub-skill executes)

When a sub-skill produces no findings, copy its row from this manifest verbatim into the findings table.

| Sub-Skill | System Boundary | Sentinel Summary | Sentinel Remediation |
|-----------|----------------|-----------------|---------------------|
| trace-state | state machine | No findings detected in state machine trace | None required -- full traversal completed without anomalies |
| trace-contract | contract surface | No findings detected in contract surface trace | None required -- all contract boundaries matched expected behavior |
| trace-permissions | permission check | No findings detected in permission path trace | None required -- RBAC traversal completed without escalation routes |
| flow-lifecycle | lifecycle phase | No findings detected in lifecycle phase trace | None required -- all phases have defined contracts and recovery paths |
| flow-conversation | conversation state | No findings detected in conversation state trace | None required -- no dead ends, loops, or ambiguous transitions found |

Rule: real findings replace the sentinel row. Zero findings = copy sentinel verbatim.
A sub-skill absent from the findings table = execution gap, not clean run.

---

**SEVERITY SCALE**

- CRITICAL: data loss, security breach, or system unavailability if shipped
- HIGH: incorrect behavior, contract violation, or blocked user flow if shipped
- MEDIUM: degraded behavior, performance issue, or misleading output
- LOW: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION ORDER**

1. trace-state        (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
2. trace-contract     (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
3. trace-permissions  (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
   -- PAUSE: verify budget gate, write Trace Findings Brief --
4. flow-lifecycle     (reads brief | add rows or sentinel | populate Trace Link)
5. flow-conversation  (reads brief | add rows or sentinel | populate Trace Link)

---

**SUB-SKILL 1: trace-state** (boundary: "state machine" | severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Every state, every transition, every precondition and
postcondition. Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add findings to the table using System Boundary = "state machine" (from schema contract).
If no findings: copy the trace-state row from the Sentinel Manifest verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (boundary: "contract surface" | severity budget: >= 1 CRITICAL or HIGH)

Three most important contract boundaries. Caller expectation, callee behavior per spec, divergence.
Find undocumented edge case behaviors.

System Boundary = "contract surface." If no findings: copy the trace-contract manifest row verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (boundary: "permission check" | severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Each role's permission path. Privilege escalation, missing denials, cross-role conflicts.

System Boundary = "permission check." If no findings: copy the trace-permissions manifest row verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without rationale, the campaign halts.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (boundary: "lifecycle phase" | reads Trace Findings Brief)

Read the brief. Trace the lifecycle for {{topic}} phase by phase. Missing exit states, undefined
phase contracts, exception recovery gaps, undeclared terminal states.

System Boundary = "lifecycle phase." If no findings: copy the flow-lifecycle manifest row verbatim.

For each real finding: scan the brief. Name the trace F-ID in Trace Link, or "none."
At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (boundary: "conversation state" | reads Trace Findings Brief)

Read the brief. Simulate the conversation graph for {{topic}}. Dead ends, loops, ambiguous transitions.

System Boundary = "conversation state." If no findings: copy the flow-conversation manifest row verbatim.

---

**FINDINGS TABLE (complete)**

[Insert the full findings table. Every sub-skill present -- real findings or manifest sentinel.
All boundary values match the schema contract vocabulary. No blank cells.]

---

**RANKED FINDINGS**

Re-sort by blast radius, then severity within tier. Add Rank column.
Top-tier findings: add blast radius rationale.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

---

**TEST SCENARIO BASELINE**

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why scope is wider |
|------|------------|-------|----------------------|--------------------|
|      |            |       |                      |                    |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. Schema Contract (at top -- included in the artifact for reference)
2. Sentinel Manifest
3. trace sub-skill executions (each with budget status)
4. Severity Budget Gate
5. Trace Findings Brief
6. flow sub-skill executions (each with trace link check)
7. Findings Table (complete)
8. Ranked Findings
9. Execution Log
10. Test Scenario Baseline
11. Cross-Skill Patterns

Before writing: confirm every sub-skill has at least one row. Verify all boundary labels match the
schema contract vocabulary map. No blank cells.

---

## V-05 -- Combined (Schema-Declaration + Sentinel-Manifest + Verification-Gate-as-Section)

**Variation axes combined:**
1. Output format -- schema and boundary vocabulary declared first (V-01 axis)
2. Output format -- sentinel manifest pre-written before execution (V-02 axis)
3. Output format -- blank-cell verification gate as an explicit named output section (V-03 axis)

**Hypothesis:** This is the maximum-clarity variant for Round 3. It closes all five new aspirational
criteria by construction from the prompt structure alone:
- C-14: schema contract header contains the boundary vocabulary map -- transcription, not judgment
- C-15: no-blank-cell contract stated in the schema header + gate enforces it at output time
- C-16: sentinel manifest pre-writes clean-run rows -- copy operation, not on-demand authoring
- C-17: BLANK-CELL VERIFICATION GATE is a named section producing a per-column audit table
- C-18: one 10-column table is declared in the schema contract before any sub-skill runs

All five criteria are enforced by setup artifacts that exist before any finding is written.
The risk is maximum prompt length: schema contract + sentinel manifest + gate section adds significant
structure. Authors may skim the setup sections, defeating their purpose. The vocabulary map must
remain visually distinct (two-column table) and each setup section must have a bold heading.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. All setup artifacts (schema contract, sentinel
manifest) are written before any sub-skill executes. A named Blank-Cell Verification Gate section
must appear in the output before the file is written.

---

**SCHEMA CONTRACT** (read before writing any finding)

One unified table receives all findings from all sub-skills:

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

**Boundary vocabulary -- copy verbatim, never infer:**

| Sub-Skill | System Boundary |
|-----------|----------------|
| trace-state | state machine |
| trace-contract | contract surface |
| trace-permissions | permission check |
| flow-lifecycle | lifecycle phase |
| flow-conversation | conversation state |

**Severity** (enumerated): CRITICAL / HIGH / MEDIUM / LOW
**Blast Radius** (enumerated): system-wide / cross-skill / component-wide / isolated

**No-blank-cell contract**:
- Every cell in every row populated; optional fields: "N/A -- [reason]"
- Trace Link: F-ID of a related trace finding, or "none" -- never blank
- Spec Location: specific section or boundary -- never "the spec is unclear"
- Remediation: named target + specific change -- never "fix the spec"

---

**SENTINEL MANIFEST** (written before any sub-skill executes)

Pre-authored clean-run rows. If a sub-skill produces no findings, copy its row verbatim into the
findings table. Real findings replace the sentinel row -- do not add both.

| Sub-Skill | System Boundary | Sentinel Summary | Sentinel Remediation |
|-----------|----------------|-----------------|---------------------|
| trace-state | state machine | No findings detected in state machine trace | None required -- full traversal completed without anomalies |
| trace-contract | contract surface | No findings detected in contract surface trace | None required -- all contract boundaries matched expected behavior |
| trace-permissions | permission check | No findings detected in permission path trace | None required -- RBAC traversal completed without escalation routes |
| flow-lifecycle | lifecycle phase | No findings detected in lifecycle phase trace | None required -- all phases have defined contracts and recovery paths |
| flow-conversation | conversation state | No findings detected in conversation state trace | None required -- no dead ends, loops, or ambiguous transitions found |

A sub-skill absent from the findings table = execution gap. Absence is never evidence of a clean run.

---

**SEVERITY SCALE**

- CRITICAL: data loss, security breach, or system unavailability if shipped
- HIGH: incorrect behavior, contract violation, or blocked user flow if shipped
- MEDIUM: degraded behavior, performance issue, or misleading output
- LOW: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION ORDER**

1. trace-state        (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
2. trace-contract     (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
3. trace-permissions  (severity budget: >= 1 CRITICAL or HIGH | add rows or sentinel)
   -- PAUSE: verify budget gate, write Trace Findings Brief --
4. flow-lifecycle     (reads brief | add rows or sentinel | populate Trace Link)
5. flow-conversation  (reads brief | add rows or sentinel | populate Trace Link)

---

**SUB-SKILL 1: trace-state** (boundary: "state machine" | severity budget: >= 1 CRITICAL or HIGH)

Hand-compile the state machine for {{topic}}. Every state, every transition, every precondition and
postcondition. Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add findings to the table using System Boundary = "state machine" (from schema contract).
If no findings: copy the trace-state sentinel row from the Sentinel Manifest verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (boundary: "contract surface" | severity budget: >= 1 CRITICAL or HIGH)

Three most important contract boundaries. Caller expectation, callee behavior per spec, divergence.
Find undocumented edge case behaviors at interfaces.

System Boundary = "contract surface." If no findings: copy the trace-contract manifest row verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (boundary: "permission check" | severity budget: >= 1 CRITICAL or HIGH)

Walk the RBAC model. Each role's permission path. Privilege escalation, missing denials, cross-role conflicts.

System Boundary = "permission check." If no findings: copy the trace-permissions manifest row verbatim.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET. If any is NOT MET without rationale, the campaign halts.

---

**TRACE FINDINGS BRIEF**

[Compile all trace rows from the findings table.]

| F-ID | Sub-Skill | Summary | Severity | Blast Radius |
|------|-----------|---------|----------|-------------|
|      |           |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (boundary: "lifecycle phase" | reads Trace Findings Brief)

Read the brief. Trace the lifecycle for {{topic}} phase by phase. Missing exit states, undefined
phase contracts, exception recovery gaps, undeclared terminal states.

System Boundary = "lifecycle phase." If no findings: copy the flow-lifecycle manifest row verbatim.

For each real finding: scan the brief. Name the trace F-ID in Trace Link, or "none."
At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (boundary: "conversation state" | reads Trace Findings Brief)

Read the brief. Simulate the conversation graph for {{topic}}. Dead ends, loops, ambiguous transitions.

System Boundary = "conversation state." If no findings: copy the flow-conversation manifest row verbatim.

---

**FINDINGS TABLE (complete)**

[Insert the full findings table. Every sub-skill present. All boundary values from the schema contract
vocabulary. No blank cells. Trace Link populated for every row.]

---

**RANKED FINDINGS**

Re-sort by blast radius (system-wide first), then severity within tier. Add Rank column.
For system-wide and cross-skill findings: add blast radius rationale naming affected flows,
components, or contracts.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status |
|-----------|--------|-------------|--------------|
| trace-state | executed / no findings | | MET / NOT MET |
| trace-contract | executed / no findings | | MET / NOT MET |
| trace-permissions | executed / no findings | | MET / NOT MET |
| flow-lifecycle | executed / no findings | | N/A |
| flow-conversation | executed / no findings | | N/A |

---

## BLANK-CELL VERIFICATION GATE

Audit the findings table before writing the output file. Count blank cells per column. Mark PASS
(0 blank after action) or FAIL. Record the action taken for any blank found.

| Column | Blank Cells Found | Action Taken | Status |
|--------|------------------|-------------|--------|
| F-ID | 0 / N | none / filled sequentially | PASS / FAIL |
| Sub-Skill | 0 / N | none / filled from execution log | PASS / FAIL |
| System Boundary | 0 / N | none / corrected to vocabulary | PASS / FAIL |
| Type | 0 / N | none / filled | PASS / FAIL |
| Spec Location | 0 / N | none / specified section named | PASS / FAIL |
| Summary | 0 / N | none / filled | PASS / FAIL |
| Severity | 0 / N | none / enumerated value assigned | PASS / FAIL |
| Blast Radius | 0 / N | none / enumerated value assigned | PASS / FAIL |
| Trace Link | 0 / N | none / "none" written where no link | PASS / FAIL |
| Remediation | 0 / N | none / target + change specified | PASS / FAIL |
| **Overall** | | **All columns must PASS** | **PASS / FAIL** |

Do not write the output file until Overall = PASS. Any column that still FAILs after action:
return to those rows and fill or mark "N/A -- [reason]" before proceeding.

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario. The baseline must contain at least as
many scenarios as there are CRITICAL/HIGH findings in the table.

| Scenario ID | F-ID | Severity | What to Exercise | Acceptance Condition |
|-------------|------|----------|-----------------|---------------------|
|             |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

Scan for single root causes appearing across two or more sub-skills:

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why scope is wider than any single finding |
|------|------------|-------|----------------------|------------------------------------------|
|      |            |       |                      |                                           |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. Schema Contract (artifact header -- includes boundary vocabulary map)
2. Sentinel Manifest
3. trace sub-skill executions (each with budget status)
4. Severity Budget Gate
5. Trace Findings Brief
6. flow sub-skill executions (each with trace link check)
7. Findings Table (complete)
8. Ranked Findings
9. Execution Log
10. **BLANK-CELL VERIFICATION GATE** (per-column audit table, Overall = PASS)
11. Test Scenario Baseline
12. Cross-Skill Patterns

The output file must contain the Schema Contract header, the Sentinel Manifest, and the Blank-Cell
Verification Gate section. A file missing any of these three setup/verification artifacts has an
incomplete structural record.
