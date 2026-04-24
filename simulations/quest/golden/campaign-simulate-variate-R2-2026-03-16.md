---
skill: campaign-simulate
round: 2
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v2-2026-03-16.md
---

# campaign-simulate -- Round 2 Variations

**Context**: Round 1 achieved 95/100 on V-01, V-03, V-04 and 90/100 on V-02, V-05. The universal weakness was C-07 (no structural guarantee of coverage breadth). Round 2 targets the three new v2 criteria: C-11 (empty-state discipline across all sections), C-12 (compounding elevation documentation), C-13 (discriminating rejection of weak observations) -- plus the tightened C-06 (standalone Impact field) and C-08 (finding-level remediation).

**Round 2 axes chosen:**
- Single-axis: V-01 (filtering evidence / C-13), V-02 (elevation narrative / C-12), V-03 (universal empty-state / C-11)
- Combined: V-04 (filtering evidence + universal empty-state / C-13 + C-11), V-05 (elevation narrative + tightened finding schema / C-12 + C-06 + C-08)

---

## V-01 -- Filtering Evidence Axis

**Variation axis:** Filtering evidence -- a mandatory "observations evaluated and rejected" filter log is required before the findings table. Every sub-skill execution must produce a filter decision for any candidate observation that was considered but did not meet the anchoring rules. The filter log is a first-class section, not a footnote.

**Hypothesis:** C-13 passes by construction -- the filter log structurally requires at least one explicit rejection before the author can write the findings table. Producing a filter log also strengthens C-05 because the act of evaluating candidates against anchoring rules makes the anchoring rules visible and enforced. The filter log also reduces the risk of inflated finding counts: weak observations are named and rejected rather than silently elevated or silently dropped. Hardest remaining: C-11 (empty-state discipline across all sections -- not only the filter log).

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills below in order. For each sub-skill, capture every candidate observation -- including ones you decide not to elevate to a finding. Then apply the filter protocol before writing the findings table. Only anchored observations become findings.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. Do not reorder.

1. flow-lifecycle    -- trace the complete business document lifecycle with phase contracts and exception flows
2. flow-conversation -- simulate multi-turn agent conversation paths with dead-end and loop detection
3. trace-state       -- hand-compile state transitions with preconditions, postconditions, and invariants
4. trace-contract    -- compare expected vs actual outputs at contract boundaries with mismatch severity
5. trace-permissions -- trace RBAC paths for each role with privilege escalation detection

After each sub-skill, list every candidate observation you noticed -- including weak ones. You will filter them in the next step.

---

**CANDIDATE OBSERVATIONS**

For each sub-skill, list candidate observations before deciding which ones become findings.

| Sub-Skill | Observation # | What was noticed | Spec Location (if known) | Elevate to Finding? | Reason if Rejected |
|-----------|--------------|-----------------|--------------------------|--------------------|--------------------|
| flow-lifecycle | O-01 | | | yes / no | |
| flow-conversation | O-02 | | | yes / no | |
| trace-state | O-03 | | | yes / no | |
| trace-contract | O-04 | | | yes / no | |
| trace-permissions | O-05 | | | yes / no | |

**Filter rules** -- an observation is rejected if any of these apply:
- No spec location can be named (the observation is not anchored to any specific section, boundary, or interface)
- No blast radius can be estimated (the observation cannot be scoped to even one downstream component)
- The problem is a style preference, not a correctness or coverage gap
- The observation duplicates a finding already captured at higher blast radius

At least one observation must be evaluated and explicitly rejected with a reason. If every observation passes the filter, the filter is not functioning -- revisit the candidate list and identify what was not elevated.

---

**FINDINGS TABLE**

Only observations that passed the filter above enter this table. All fields are required. A finding with a blank required cell is incomplete and fails.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

Field definitions:
- **Sub-Skill**: which sub-skill discovered this finding
- **Type**: spec-gap, contract-violation, state-anomaly, permission-gap, or flow-gap
- **Spec Location**: specific spec section, contract boundary, or interface name -- "the spec is unclear" without a named location fails this field
- **Summary**: one sentence describing the problem -- do not include impact here; impact has its own field
- **Impact**: standalone field -- what breaks or degrades if this finding is not resolved before implementation; do not merge with Summary
- **Blast Radius**: isolated / component-wide / cross-skill / system-wide
- **Remediation**: the specific action at a named target -- not "fix the spec" but the exact change at the named spec section, contract boundary, or interface; must be attached here, not only in a closing summary

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates Evaluated | Observations Rejected | Finding IDs |
|-----------|--------|---------------------|----------------------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

A sub-skill with "no findings" must state why. A sub-skill with zero candidates evaluated is a signal that the simulation did not run.

---

**RANKED FINDINGS**

Rank all findings by blast radius (system-wide first, then cross-skill, then component-wide, then isolated). Within each tier, sort by impact severity.

**Tier 1 -- System-Wide**
[findings with blast radius = system-wide]
[for each: name the downstream flows, components, or contracts affected and explain why the scope reaches that far]

**Tier 2 -- Cross-Skill**
[findings with blast radius = cross-skill]
[for each: name which sub-skills are affected and what shared root cause links them]

**Tier 3 -- Component-Wide**
[findings with blast radius = component-wide]

**Tier 4 -- Isolated**
[findings with blast radius = isolated]

If a tier has no findings: "No findings at this tier."

---

**CROSS-SKILL PATTERNS**

After completing the ranked list, scan for compounding patterns -- a single root cause that manifests in two or more sub-skills.

| P-ID | Root Cause | F-IDs Linked | Original Blast Radius (per skill) | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------------|----------------------------------|-----------------------|---------------------|

If no compounding patterns exist: "No cross-skill patterns detected -- all findings describe distinct root causes. [Brief reason why findings are independent.]"

---

**OUTPUT**

Write the simulation findings report to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations (with filter decisions and rejections) > Execution Log > Findings Table > Ranked Findings (with tier labels and blast radius rationale for top findings) > Cross-Skill Patterns.

---

## V-02 -- Elevation Narrative Axis

**Variation axis:** Elevation narrative -- when findings compound across sub-skills, the report must document the elevation explicitly: what blast radius the finding carries in isolation, what blast radius it receives due to the cross-skill root cause, and why the compounding expands the scope. The elevation narrative is a required field on the compounding finding record, not an optional annotation.

**Hypothesis:** C-12 passes by construction -- any compounding finding must include before/after scope documentation as a required schema field. The "promoted from / promoted to" framing also strengthens C-10 (blast radius rationale) because the elevation narrative is the most precise form of blast radius explanation. C-09 benefits because authors must be precise about which finding IDs share a root cause in order to write the elevation narrative. Hardest remaining: C-13 (no structural filter log), C-11 (no universal empty-state protocol beyond sub-skill sections).

---

Simulate the technical behavior of: {{topic}}

You are running a pre-implementation simulation campaign. Execute all five sub-skills in order. After completing all five, synthesize findings and identify any compounding patterns where a single root cause manifests across multiple sub-skills. For each compounding pattern, document the elevation: what blast radius the finding would carry in isolation versus what it receives because of the cross-skill root cause.

---

**FINDING SCHEMA**

Every finding uses this schema. All fields are required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [required: name the specific spec section, contract boundary, or interface --
                 vague references such as "the spec does not address this" fail this field]
Summary:        [one sentence describing the problem -- do not include impact here]
Impact:         [standalone field: what breaks or degrades if unresolved -- must be separately
                 labeled; merging Impact into Summary fails this field]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [required for cross-skill or system-wide: name the downstream scope and why]
Remediation:    [specific action at a named target -- required here on the finding record,
                 not only in a closing summary; "fix the spec" fails this field]
```

---

**EXECUTION: SUB-SKILL 1 -- flow-lifecycle**

Phase 1 -- Setup:
Spec artifacts: [name sections governing lifecycle phases, transitions, terminals]
Detection target: missing states, undefined phase contracts, exception flows without recovery paths, orphaned terminal paths

Phase 2 -- Execute:
[step-by-step lifecycle trace for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 2 -- flow-conversation**

Phase 1 -- Setup:
Spec artifacts: [name sections governing conversation states, intents, transitions]
Detection target: dead ends, loops, ambiguous transitions without defined next states

Phase 2 -- Execute:
[step-by-step conversation simulation for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 3 -- trace-state**

Phase 1 -- Setup:
Spec artifacts: [name sections governing the state machine, preconditions, postconditions, invariants]
Detection target: exit-less states, precondition violations, invariant breaks, unreachable states

Phase 2 -- Execute:
[state transition hand-compilation for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 4 -- trace-contract**

Phase 1 -- Setup:
Spec artifacts: [name the contract boundaries -- interfaces, API surfaces, caller/callee assumption docs]
Detection target: caller/callee expectation divergence, undocumented edge cases at interfaces

Phase 2 -- Execute:
[expected vs actual output comparison for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 5 -- trace-permissions**

Phase 1 -- Setup:
Spec artifacts: [name sections governing RBAC, role definitions, permission boundaries]
Detection target: privilege escalation paths, missing permission denials, cross-role conflicts

Phase 2 -- Execute:
[RBAC walk-through for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: [explanation]"]

---

**SYNTHESIS**

**Findings Table** (all findings from all sub-skills, in F-ID order):

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

**Ranked Findings** (blast-radius sort: system-wide first, then cross-skill, component-wide, isolated):

| Rank | F-ID | Sub-Skill | Summary | Blast Radius | BR Rationale |
|------|------|-----------|---------|-------------|-------------|

BR Rationale is required for all cross-skill and system-wide findings.

---

**COMPOUNDING PATTERNS**

Identify any single root cause that manifests as findings across two or more sub-skills. For each compounding pattern, complete this elevation record:

```
P-ID:                    [P-01, P-02, ...]
Root cause:              [the shared problem that produces findings in multiple sub-skills]
F-IDs linked:            [all finding IDs that share this root cause -- must be from 2+ sub-skills]
Blast radius per skill:  [what blast radius each linked finding carries in isolation]
Elevated blast radius:   [the blast radius tier after compounding is applied]
Elevation rationale:     [explain precisely why the cross-skill root cause expands the scope --
                          "promoted from [original tier] to [elevated tier] because [the
                          shared root cause means that fixing F-0X alone does not resolve F-0Y,
                          and both affect the following downstream scope: ...]"]
```

If no compounding patterns exist: "No cross-skill patterns detected. Findings from each sub-skill describe distinct root causes with no shared origin."

The elevation record is the most important section for high-blast findings. A compounding pattern entry without an explicit "promoted from X to Y because Z" statement fails this section.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs |
|-----------|--------|-------------|
| flow-lifecycle | executed / no findings | |
| flow-conversation | executed / no findings | |
| trace-state | executed / no findings | |
| trace-contract | executed / no findings | |
| trace-permissions | executed / no findings | |

A sub-skill with "no findings" must state why.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections: Execution logs (all 5 sub-skills with setup, execution, and extract phases) > Findings Table > Ranked Findings > Compounding Patterns (with elevation records) > Execution Log.

All finding schema fields are required. Impact must be a standalone labeled field. Remediation must be attached to each finding, not only in a summary. Compounding patterns require explicit "promoted from / promoted to" elevation narrative.

---

## V-03 -- Universal Empty-State Protocol Axis

**Variation axis:** Universal empty-state protocol -- every structured section in the report has a defined empty-state template that must be used when the section has no entries. The empty-state templates are defined upfront, before execution begins. Using the silence of omission to indicate "nothing here" is not permitted for any section.

**Hypothesis:** C-11 passes by construction -- empty-state templates are named for every section, and any section without content must use its defined template. The protocol also strengthens C-01 because sub-skill "no findings" is just one instance of a broader empty-state discipline that has been made structural. C-09 also benefits because the cross-skill patterns section now has a mandatory empty-state statement that is more precise than a simple blank. Hardest remaining: C-12 (elevation narrative) and C-13 (filter log) -- this variation does not add active filtering or elevation documentation.

---

Before you write a line of code for {{topic}}, prove the spec holds.

Run these five checks in order. Then write a findings report. Every section of the report follows the empty-state protocol: when a section has no content, use the defined empty-state template for that section. Silence is never acceptable.

---

**EMPTY-STATE TEMPLATES**

Use these exact templates when a section has no content. Do not omit the section; do not leave it blank.

- **Sub-skill with no findings**: "No findings from [sub-skill name]. Simulation ran against [spec artifacts examined]. No gaps, violations, or anomalies were identified in this area because [brief reason -- e.g., this sub-skill is not applicable to this topic / the spec fully addresses this domain]."
- **Findings table with no rows**: "No findings elevated from any sub-skill. All candidate observations failed the filter rules or the simulation found no problems."
- **Ranked findings tier with no entries**: "No findings at [tier name] blast radius."
- **Cross-skill patterns section with no patterns**: "No cross-skill patterns detected. Each finding describes a distinct root cause. Sub-skills whose findings appeared related were compared; the divergences are: [brief explanation of why the findings are independent rather than sharing a root cause]."
- **Execution log sub-skill with no candidates**: "Candidates evaluated: 0. [Explanation of why this simulation area produced no observable candidates.]"

---

**CHECK 1: flow-lifecycle**

Walk the business process lifecycle for {{topic}} step by step. At every phase boundary, ask: does the spec tell you exactly what happens here? For each place where the answer is no, that is a candidate observation.

Look for: missing exit states, exception flows with no recovery path, phase contracts the spec leaves undefined, terminal states reached without a declared prior path.

For each problem: name the spec section where the gap lives. Name what the spec says (or fails to say). Name what downstream flows break if this ships without a fix.

If no problems are found, apply the sub-skill empty-state template.

---

**CHECK 2: flow-conversation**

Simulate the multi-turn conversation paths for {{topic}}. Walk every major branch. Walk the edge paths. Look for dead ends (the agent has no valid next action), loops (agent returns to prior state without resolution), and ambiguous transitions (spec does not define what happens next).

For each problem: name the conversation state where it occurs. Name what the spec says about this state. Name what the caller experiences if the agent cannot resolve the transition.

If no problems are found, apply the sub-skill empty-state template.

---

**CHECK 3: trace-state**

Hand-compile the state machine. Write out every state, every transition, every precondition and postcondition. Then check:

- Can every state be exited? A state with no defined exit transition is a trap.
- Can every transition fire without meeting its precondition? A transition that can fire early is a race condition.
- Does the spec enforce every invariant? An invariant the spec names but does not enforce is a contract the implementation will violate.

For each violation: name the state or transition. Name the spec section. Name how many callers depend on this contract holding.

If no violations found, apply the sub-skill empty-state template.

---

**CHECK 4: trace-contract**

Pick the three most important contract boundaries for {{topic}} -- the interfaces where caller and callee make assumptions about each other. For each: state what the caller expects. State what the callee actually returns per the spec. If they diverge, that is a contract violation.

For each mismatch: name the interface and spec location. State the expected value and actual value. Name every caller that receives the wrong output.

If no mismatches found, apply the sub-skill empty-state template.

---

**CHECK 5: trace-permissions**

Walk the RBAC model for {{topic}}. For each role, trace the permission path. Look for privilege escalation, missing denials, and cross-role conflicts.

For each finding: name the role, the path taken, the spec section governing this boundary, and who else is affected if this boundary is wrong.

If no permission problems found, apply the sub-skill empty-state template.

---

**FINDINGS REPORT**

For each finding:

- **Sub-skill**: which check found it
- **Type**: spec-gap, contract-violation, state-anomaly, permission-gap, or flow-gap
- **Spec location**: name the specific section, interface, or boundary -- not "the spec is unclear about X"
- **Summary**: one sentence describing the problem -- do not include impact in this field
- **Impact**: standalone field -- what breaks if you ship this finding unresolved; must be separately labeled from Summary
- **Blast radius**: isolated / component-wide / cross-skill / system-wide
- **Remediation**: a specific action with a named target, attached to this finding -- not "fix the spec" but the exact change at the named location; remediation at finding level is required, not only in a closing summary

If no findings from any check: apply the findings-table empty-state template.

---

**RANKED BY BLAST RADIUS**

Rank all findings by blast radius (system-wide first, then cross-skill, component-wide, isolated). For each tier, list findings in severity order. For every system-wide or cross-skill finding, state the downstream rationale: name the flows, components, or contracts affected and explain why the scope is wide.

If a tier has no findings: apply the ranked-findings-tier empty-state template.

---

**CROSS-SKILL PATTERNS**

Scan for compounding patterns -- a single root cause that appears in two or more checks. A compounding finding shares a root cause; two independently similar findings do not qualify.

For each compounding pattern: name the root cause, the check IDs that surface it, the finding IDs linked, and the elevated blast radius they receive together.

If no patterns exist: apply the cross-skill-patterns empty-state template. The template requires more than "none found" -- name why the related-looking findings are actually independent.

---

**EXECUTION LOG**

| Check | Ran | Candidates Evaluated | Finding IDs |
|-------|-----|---------------------|-------------|
| flow-lifecycle | yes / no | | |
| flow-conversation | yes / no | | |
| trace-state | yes / no | | |
| trace-contract | yes / no | | |
| trace-permissions | yes / no | | |

If any check shows 0 candidates evaluated: apply the execution-log empty-state template for that row.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Structure: Findings Report > Ranked by Blast Radius > Cross-Skill Patterns > Execution Log.

Every section applies the empty-state protocol. No section may be blank or omitted without using the defined empty-state template.

---

## V-04 -- Combined (Filtering Evidence + Universal Empty-State)

**Variation axes combined:**
1. Filtering evidence (V-01) -- mandatory filter log with explicit rejection records before the findings table
2. Universal empty-state protocol (V-03) -- every structured section has a defined template for the empty case

**Hypothesis:** The two axes close the two most common silent-failure modes simultaneously. The filter log makes C-13 structural: at least one explicit rejection must appear before the findings table can be written. The universal empty-state protocol makes C-11 structural: no section can be blank or absent without using a defined template. Together they remove all silent paths from the report. C-01 and C-07 also benefit: the filter log shows candidates were actually evaluated (preventing silent skipping), and the empty-state templates for cross-skill patterns and execution logs enforce breadth accounting. The combination is more heavily scaffolded than either single-axis variation, but the scaffolding targets different failure modes than R1's most scaffolded variation (V-04 in R1 used phase protocol + schema). Hardest remaining: C-12 (no elevation narrative for compounding findings).

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills in order. Apply the filter protocol before writing any findings to the table. Every section of the report follows the empty-state protocol: when a section has no content, use the defined empty-state template. Silence is not acceptable anywhere in the report.

---

**FINDING SCHEMA**

Every finding uses this schema. All fields are required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [required: name the specific spec section, contract boundary, or interface --
                 vague references such as "the spec does not cover this" fail this field]
Summary:        [one sentence describing the problem -- do not include impact here]
Impact:         [standalone field: what breaks or degrades if unresolved --
                 do not merge with Summary; merging fails this field]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [required for cross-skill or system-wide: name downstream scope and why]
Remediation:    [specific action at a named target -- required on this finding record,
                 not only in a closing summary; "fix the spec" fails this field]
```

---

**EMPTY-STATE TEMPLATES**

Use these exact templates when a section has no content:

- **Sub-skill with no findings**: "No findings from [sub-skill name]. Spec artifacts examined: [list]. No gaps or violations detected because [reason]."
- **Filter log with only passes**: "Filter applied. All [N] candidate observations met the anchoring rules and were elevated to findings. No observations were rejected."
  Note: if you reach this template, revisit your candidates -- a filter that rejects nothing may not be functioning.
- **Findings table empty**: "No findings. All candidate observations failed the filter rules or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Cross-skill patterns empty**: "No cross-skill patterns detected. Candidate compounds reviewed: [list the related-looking findings that were compared]. Each was determined to describe a distinct root cause because [brief explanation]."
- **Execution log row with zero candidates**: "Zero candidates evaluated. Reason: [explanation]."

---

**EXECUTION SEQUENCE**

Run each sub-skill in order:

1. flow-lifecycle    -- trace the complete lifecycle with phase contracts and exception flows
2. flow-conversation -- simulate multi-turn conversation paths with dead-end and loop detection
3. trace-state       -- hand-compile state transitions with preconditions, postconditions, invariants
4. trace-contract    -- compare expected vs actual outputs at contract boundaries
5. trace-permissions -- trace RBAC paths with privilege escalation detection

After each sub-skill runs, list every candidate observation -- including weak ones. You will filter them in the next step.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

For each sub-skill, list observations and apply the filter rules before elevating to findings.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** -- reject if any apply:
1. No specific spec location can be named (not "the spec is vague" but a named section, boundary, or interface)
2. No blast radius can be estimated (cannot name even one downstream component)
3. Problem is a style preference, not correctness or coverage gap
4. Duplicates a finding already captured at higher blast radius

At least one observation must be evaluated and explicitly rejected with a filter rule number. If every observation passes, the filter is not functioning -- identify and reject at least one weak candidate.

If a sub-skill produces zero candidates: apply the execution-log empty-state template for that sub-skill.

---

**FINDINGS TABLE**

Only observations that passed the filter enter this table.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

If no observations passed the filter: apply the findings-table empty-state template.

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

---

**RANKED FINDINGS**

Rank by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings or: apply ranked-tier empty-state template]
[for each: downstream scope rationale]

**Tier 2 -- Cross-Skill**
[findings or: apply ranked-tier empty-state template]
[for each: sub-skills affected and shared root cause]

**Tier 3 -- Component-Wide**
[findings or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings or: apply ranked-tier empty-state template]

---

**CROSS-SKILL PATTERNS**

Scan findings for a single root cause that manifests in two or more sub-skills.

| P-ID | Root Cause | F-IDs | Original Blast Radius (per skill) | Elevated Blast Radius |
|------|------------|-------|----------------------------------|-----------------------|

If none exist: apply the cross-skill-patterns empty-state template. The template requires naming the related-looking findings that were compared and explaining why they are independent.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations and Filter Log > Findings Table > Execution Log > Ranked Findings > Cross-Skill Patterns.

Every section applies the empty-state protocol. The filter log must contain at least one explicit rejection. No section may be blank or absent without using its defined template.

---

## V-05 -- Combined (Elevation Narrative + Tightened Finding Schema)

**Variation axes combined:**
1. Elevation narrative (V-02) -- compounding findings require explicit before/after scope documentation
2. Tightened finding schema -- standalone Impact field (C-06), finding-level Remediation (C-08), and discriminating filter step (C-13) built directly into the schema

**Hypothesis:** The combination targets C-12, C-06, and C-08 simultaneously through schema design rather than protocol additions. When the finding schema itself encodes the C-06 Impact-isolation requirement and the C-08 finding-level Remediation requirement as separate fields with explicit failure conditions, compliance becomes structural. Adding the elevation narrative requirement to the compounding patterns section makes C-12 structural. A brief filter gate before each sub-skill's extract phase targets C-13 by requiring authors to name at least one observation that did not reach finding status per sub-skill. This is the tightest schema variation: every field is either required or has an explicit failure condition, and the compounding section is the most precise of all five variations. Risk: the elevation narrative adds length to the compounding section; authors may produce thin compounding entries to avoid the work, which would fail C-12.

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills in the order listed. For each sub-skill, apply the three-phase protocol. After all five complete, synthesize into a unified findings table and identify compounding patterns. For any compounding finding, document the elevation: what scope it carries in isolation and what scope it receives from the shared root cause.

---

**FINDING SCHEMA**

Every finding uses this schema. All fields are required. Fields with failure conditions are marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: name the specific spec section, contract boundary, or interface --
                 FAILURE: "the spec does not address this" without a named location fails this field]
Summary:        [one sentence -- the problem only, no impact language --
                 FAILURE: merging impact into this field fails C-06]
Impact:         [STANDALONE FIELD: what breaks or degrades if unresolved --
                 FAILURE: leaving this field blank or merging it into Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide: name the downstream scope and why --
                 FAILURE: cross-skill or system-wide findings without rationale fail C-10]
Remediation:    [REQUIRED HERE on this finding record: specific action at named target --
                 FAILURE: "fix the spec" fails this field; remediation only in a closing
                 summary section fails C-08]
```

---

**3-PHASE PROTOCOL**

For each sub-skill, complete all three phases before advancing.

**Phase 1 -- Setup**: Name the spec artifacts being examined. State the class of problems this sub-skill detects.

**Phase 2 -- Execute**: Run the simulation step by step. No boundary assumed; every transition walked.

**Phase 3 -- Extract and Filter**: Before writing findings, list candidate observations (including weak ones). Name at least one observation that was evaluated and rejected (name the filter rule that caused rejection: no spec location / no blast radius / style preference / duplicate). Then write findings for the observations that pass.

---

**EXECUTION: SUB-SKILL 1 -- flow-lifecycle**

Phase 1 -- Setup:
Spec artifacts: [name sections governing lifecycle phases, transitions, terminals]
Detection target: missing states, undefined phase contracts, exception flows without recovery paths, orphaned terminal paths

Phase 2 -- Execute:
[step-by-step lifecycle trace for {{topic}}]

Phase 3 -- Extract and Filter:
Candidates considered: [list observations including weak ones]
Rejected: [at least one observation with rejection reason -- "Rejected: [observation] -- Rule: [no spec location / no blast radius / style preference / duplicate]"]
Findings elevated:
[findings using schema above, or: "No findings elevated. All candidates failed the filter: [reasons]"]

---

**EXECUTION: SUB-SKILL 2 -- flow-conversation**

Phase 1 -- Setup:
Spec artifacts: [name sections governing conversation states, intents, transitions]
Detection target: dead ends, loops, ambiguous transitions without defined next states

Phase 2 -- Execute:
[step-by-step conversation simulation for {{topic}}]

Phase 3 -- Extract and Filter:
Candidates considered: [list observations including weak ones]
Rejected: [at least one observation with rejection reason]
Findings elevated:
[findings using schema above, or: "No findings elevated. Reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 3 -- trace-state**

Phase 1 -- Setup:
Spec artifacts: [name sections governing state machine, preconditions, postconditions, invariants]
Detection target: exit-less states, precondition violations, invariant breaks, unreachable states

Phase 2 -- Execute:
[state transition hand-compilation for {{topic}}]

Phase 3 -- Extract and Filter:
Candidates considered: [list observations including weak ones]
Rejected: [at least one observation with rejection reason]
Findings elevated:
[findings using schema above, or: "No findings elevated. Reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 4 -- trace-contract**

Phase 1 -- Setup:
Spec artifacts: [name the contract boundaries -- interfaces, API surfaces, caller/callee docs]
Detection target: caller/callee expectation divergence, undocumented edge cases at interfaces

Phase 2 -- Execute:
[expected vs actual output comparison for {{topic}}]

Phase 3 -- Extract and Filter:
Candidates considered: [list observations including weak ones]
Rejected: [at least one observation with rejection reason]
Findings elevated:
[findings using schema above, or: "No findings elevated. Reason: [explanation]"]

---

**EXECUTION: SUB-SKILL 5 -- trace-permissions**

Phase 1 -- Setup:
Spec artifacts: [name sections governing RBAC, role definitions, permission boundaries]
Detection target: privilege escalation paths, missing permission denials, cross-role conflicts

Phase 2 -- Execute:
[RBAC walk-through for {{topic}}]

Phase 3 -- Extract and Filter:
Candidates considered: [list observations including weak ones]
Rejected: [at least one observation with rejection reason]
Findings elevated:
[findings using schema above, or: "No findings elevated. Reason: [explanation]"]

---

**SYNTHESIS**

**Findings Table** (all elevated findings from all sub-skills, in F-ID order):

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

**Ranked Findings** (blast-radius sort: system-wide > cross-skill > component-wide > isolated):

| Rank | F-ID | Sub-Skill | Summary | Blast Radius | BR Rationale |
|------|------|-----------|---------|-------------|-------------|

BR Rationale is required for all cross-skill and system-wide findings.

---

**COMPOUNDING PATTERNS AND ELEVATION RECORDS**

Identify any single root cause that manifests across two or more sub-skills. For each compounding finding, complete the full elevation record:

```
P-ID:
Root cause:          [the shared problem that produces findings in 2+ sub-skills]
F-IDs linked:        [must be from at least 2 different sub-skills]
Isolated scope:      [the blast radius each linked finding carries when considered in isolation]
Elevated scope:      [the blast radius tier assigned after compounding is recognized]
Elevation rationale: [required: "Promoted from [isolated tier] to [elevated tier] because
                      [the cross-skill root cause means that X, which expands the downstream
                      scope from [what it covers alone] to [what it covers combined]]"]
```

If no compounding patterns: "No cross-skill patterns detected. Findings from each sub-skill describe distinct root causes. [Name any findings that appeared related and explain why they are independent rather than compounding.]"

The elevation record is required in full for every compounding finding. A compounding entry that says only "this finding appears in multiple sub-skills" without a before/after scope statement fails C-12.

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Elevated | Finding IDs |
|-----------|--------|------------|---------|---------|-------------|
| flow-lifecycle | executed / no findings | | | | |
| flow-conversation | executed / no findings | | | | |
| trace-state | executed / no findings | | | | |
| trace-contract | executed / no findings | | | | |
| trace-permissions | executed / no findings | | | | |

A sub-skill with "no findings" must state why. A sub-skill with zero candidates evaluated did not run.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Execution logs (all 5 sub-skills, each with 3 phases including extract-and-filter) > Findings Table > Ranked Findings > Compounding Patterns and Elevation Records > Execution Log.

Schema field rules are enforcement rules, not suggestions. Impact must be a standalone field. Remediation must be attached to each finding. Elevation records require explicit "promoted from / to" statements with rationale. Compounding patterns with only a shallow summary statement fail.
