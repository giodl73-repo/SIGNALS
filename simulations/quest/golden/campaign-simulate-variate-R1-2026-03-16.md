---
skill: campaign-simulate
round: 1
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v1-2026-03-16.md
---

# campaign-simulate -- Round 1 Variations

Single-axis: V-01 (output format), V-02 (lifecycle emphasis), V-03 (phrasing register).
Combined: V-04 (output format + lifecycle emphasis), V-05 (phrasing register + blast radius prominence).

---

## V-01 -- Output Format Axis

**Variation axis:** Output format -- a mandatory finding schema table is defined upfront. Every finding from every sub-skill must populate all columns. The table structure enforces C-06 compliance by construction and makes blast radius an explicit required column rather than a post-hoc sort.

**Hypothesis:** When the finding schema is defined before execution begins, the author cannot produce vague findings -- every column is a forcing function. C-06 (source + location + impact) passes because those are three of the required columns. C-04 (blast radius as explicit sort key) passes because blast radius is a required column with enumerated values. C-05 (spec anchoring) passes because "Spec Location" is a required field with an explicit rule that vague references fail. The hardest remaining criterion will be C-09 (cross-skill patterns) since the table structure alone doesn't surface compounding causes.

---

Simulate the technical behavior of: {{topic}}

You are running a pre-implementation simulation campaign. Execute all five sub-skills below in order against the spec and design artifacts for {{topic}}. Collect findings from each sub-skill and enter them into the unified findings table.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. Do not reorder.

1. flow-lifecycle    -- trace the complete business document lifecycle with phase contracts and exception flows
2. flow-conversation -- simulate multi-turn agent conversation paths with dead-end and loop detection
3. trace-state       -- hand-compile state transitions with preconditions, postconditions, and invariants
4. trace-contract    -- compare expected vs actual outputs at contract boundaries with mismatch severity
5. trace-permissions -- trace RBAC paths for each role with privilege escalation detection

After each sub-skill runs, extract its findings and add rows to the FINDINGS TABLE.

---

**FINDINGS TABLE**

Each finding gets one row. All fields are required. A finding with a blank required cell is incomplete and fails.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact (if ignored) | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|---------------------|-------------|-------------|
| F-01 | | | | | | | |
| F-02 | | | | | | | |

Field definitions:
- **Sub-Skill**: which of the five sub-skills discovered this finding (flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions)
- **Type**: one of -- spec-gap, contract-violation, state-anomaly, permission-gap, flow-gap
- **Spec Location**: the specific spec section, contract boundary, or interface name where the gap or violation exists -- "the spec is unclear" without a named location fails this field
- **Summary**: one sentence describing the problem
- **Impact**: what breaks or degrades if this finding is not resolved before implementation
- **Blast Radius**: downstream scope -- isolated (one state or boundary), component-wide (one subsystem), cross-skill (two or more sub-skills affected), system-wide (all callers or all flows affected)
- **Remediation**: the specific action the spec author or implementer should take -- name the target (spec section, contract boundary, or interface) and describe the action; "fix the spec" is not acceptable

---

**EXECUTION LOG**

After all five sub-skills complete, confirm execution status and list the finding IDs each produced:

| Sub-Skill | Status | Finding IDs |
|-----------|--------|-------------|
| flow-lifecycle | executed / no findings | |
| flow-conversation | executed / no findings | |
| trace-state | executed / no findings | |
| trace-contract | executed / no findings | |
| trace-permissions | executed / no findings | |

A sub-skill with "no findings" must state why: either the simulation found no issues in this area, or the sub-skill is not applicable to this topic (explain why).

---

**RANKED FINDINGS**

After populating the findings table, produce a ranked list sorted by blast radius (system-wide first, then cross-skill, then component-wide, then isolated). Within each tier, sort by impact severity.

For every finding ranked in the top three positions overall, include an explicit blast radius rationale: name the downstream flows, components, or contracts affected and explain why the scope reaches that far.

**Tier 1 -- System-Wide**
[findings with blast radius = system-wide, in severity order]
[for each: blast radius rationale -- which flows/components/contracts are affected and why]

**Tier 2 -- Cross-Skill**
[findings with blast radius = cross-skill, in severity order]
[for each: blast radius rationale -- which sub-skills are affected and what shared root cause links them]

**Tier 3 -- Component-Wide**
[findings with blast radius = component-wide, in severity order]

**Tier 4 -- Isolated**
[findings with blast radius = isolated, in severity order]

---

**CROSS-SKILL PATTERNS**

After completing the ranked list, scan for compounding patterns -- a single root cause that manifests in two or more sub-skills. A compounding finding is not two independent findings that happen to come from two skills; it is one root cause with multiple downstream expressions.

For each compounding pattern found:

| P-ID | Root Cause | F-IDs Linked | Blast Radius After Elevation |
|------|------------|-------------|------------------------------|
| P-01 | | | |

If no compounding patterns exist, include this section with the note: "No cross-skill patterns detected -- all findings are independent."

---

**OUTPUT**

Write the simulation findings report to: simulations/{{topic}}/simulate-{{date}}.md

The report must contain: the Execution Log, the Findings Table (all findings with all columns populated), the Ranked Findings list (blast-radius sorted with tier labels and top-3 rationale), and the Cross-Skill Patterns section.

---

## V-02 -- Lifecycle Emphasis Axis

**Variation axis:** Lifecycle emphasis -- each sub-skill runs a mandatory 3-phase cycle (setup / execute / extract) before the campaign can advance. Phase boundaries are structural, not optional. The sequential execution log is a first-class section, not an afterthought.

**Hypothesis:** Requiring a named setup phase per sub-skill -- where the author states what spec artifacts they are examining and what class of problem they are looking for -- prevents silent skipping (C-01 passes by construction: a sub-skill with no setup phase did not run). The sequential gate structure enforces C-02 because later sub-skills can reference earlier findings but the setup phase must name them explicitly. The extract phase drives C-05 because it requires each finding to include a spec location as a non-optional field.

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign before implementation begins. Execute all five sub-skills in the order listed. For each sub-skill, complete all three phases of the protocol before advancing to the next. After all five complete, synthesize findings into a unified ranked report.

---

**3-PHASE PROTOCOL**

Every sub-skill follows this structure:

**Phase 1 -- Setup**: Name the spec artifacts being examined. State the class of problems this sub-skill is designed to detect.

**Phase 2 -- Execute**: Run the simulation step by step against the spec and design artifacts for {{topic}}. No boundary may be skipped; no transition may be assumed without verification.

**Phase 3 -- Extract**: For each problem found, produce a finding record with: sub-skill source, finding type, specific spec location (named section or boundary), summary, and impact. If no problems are found, state "no findings" and give the reason.

---

**SUB-SKILL 1: flow-lifecycle**

Phase 1 -- Setup:
- Spec artifacts: [name the spec sections governing lifecycle phases, transitions, and exception flows]
- Looking for: missing states, undefined phase contracts, exception flows without recovery paths, terminal states without declared prior paths

Phase 2 -- Execute:
[step-by-step lifecycle trace for {{topic}} -- walk each phase, each transition, each exception path]

Phase 3 -- Extract:
- FL-01: [type] | [spec location] | [summary] | [impact]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SUB-SKILL 2: flow-conversation**

Phase 1 -- Setup:
- Spec artifacts: [name the spec sections governing conversation states, intents, and transitions]
- Looking for: dead ends, infinite loops, ambiguous transitions where the agent has no next action

Phase 2 -- Execute:
[step-by-step conversation simulation for {{topic}} -- walk the major branches and edge paths]

Phase 3 -- Extract:
- FC-01: [type] | [spec location] | [summary] | [impact]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SUB-SKILL 3: trace-state**

Phase 1 -- Setup:
- Spec artifacts: [name the spec sections governing the state machine, preconditions, postconditions, invariants]
- Looking for: unreachable states, exit-less states, precondition violations, invariant breaks

Phase 2 -- Execute:
[state transition hand-compilation for {{topic}} -- write every state, every transition, every pre/post condition]

Phase 3 -- Extract:
- TS-01: [type] | [spec location] | [summary] | [impact]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SUB-SKILL 4: trace-contract**

Phase 1 -- Setup:
- Spec artifacts: [name the contract boundaries -- interfaces, API surfaces, or caller/callee assumptions documented in the spec]
- Looking for: caller expectations that diverge from callee behavior, undocumented edge cases at boundaries

Phase 2 -- Execute:
[expected vs actual output comparison for {{topic}} -- walk each contract boundary, state what is expected and what the spec says the callee returns]

Phase 3 -- Extract:
- TC-01: [type] | [spec location] | [summary] | [impact]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SUB-SKILL 5: trace-permissions**

Phase 1 -- Setup:
- Spec artifacts: [name the spec sections governing the RBAC model, role definitions, and permission boundaries]
- Looking for: privilege escalation paths, missing permission denials, cross-role conflicts

Phase 2 -- Execute:
[RBAC walk-through for {{topic}} -- trace each role through the permission model, state what they can and cannot do]

Phase 3 -- Extract:
- TP-01: [type] | [spec location] | [summary] | [impact]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SYNTHESIS: UNIFIED FINDINGS REPORT**

Collect all findings from all five sub-skills. Assign sequential F-IDs across the full set (F-01, F-02, ...). Rank by blast radius -- the downstream scope of impact if the finding is ignored.

Blast radius tiers: system-wide > cross-skill > component-wide > isolated.

| Rank | F-ID | Sub-Skill | Type | Spec Location | Summary | Blast Radius | Remediation |
|------|------|-----------|------|--------------|---------|-------------|-------------|
| 1 | | | | | | | |
| 2 | | | | | | | |

For the top three ranked findings, add an explicit blast radius rationale immediately below the row: name the downstream flows, components, or contracts affected and explain why the scope reaches that far.

---

**CROSS-SKILL PATTERNS**

After ranking, look for findings that share a root cause across two or more sub-skills. For each compounding pattern:

| P-ID | Root Cause | F-IDs | Elevated Tier |
|------|------------|-------|--------------|
| P-01 | | | |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Structure: Sub-skill execution logs (all five in order, each with three phases) > Unified Findings table > Ranked Findings (with top-3 blast radius rationale) > Cross-Skill Patterns.

Every sub-skill must have a Phase 3 extract entry. Every finding must have a named spec location. Every finding ranked in the top three must have a blast radius rationale.

---

## V-03 -- Phrasing Register Axis

**Variation axis:** Phrasing register -- direct imperative voice with "you" framing throughout. The task is cast as a pre-implementation gate: before writing code, prove the spec holds. The conversational register makes the spec verification purpose explicit in every instruction, which naturally drives the author toward C-05 (spec anchoring) because verifying a spec requires pointing to specific sections.

**Hypothesis:** "Before you write code, prove the spec holds" is a harder framing than "simulate the system." The imperative register forces the author to treat every finding as evidence of a spec problem, not a vague observation. C-05 (spec anchoring) becomes natural because pointing to a spec section is the only way to prove the spec failed. C-08 (remediation) becomes natural because "what to fix" is the direct goal of a gate check. The register also reduces the tendency to produce five parallel dumps rather than a unified report (C-03), because a gate check produces a verdict, not a log dump.

---

Before you write a line of code for {{topic}}, prove the spec holds.

Run these five checks in order. Each one looks for a different class of problem. Together they tell you what you need to fix in the spec before implementation begins. When you find a problem, point to the spec section where the gap lives -- a finding without a spec location is not a finding, it is a guess.

---

**CHECK 1: flow-lifecycle**

Walk the business process lifecycle for {{topic}} step by step. At every phase transition, ask: does the spec tell you exactly what happens here? For each place where the answer is no, that is a finding.

Look for: missing exit states, exception flows with no recovery path, phase contracts the spec leaves undefined, terminal states that can be reached but were not declared.

For each problem: name the spec section where the gap lives. Name what the spec says (or fails to say). Name what downstream flows break if this ships without a fix.

---

**CHECK 2: flow-conversation**

Simulate the multi-turn conversation paths for {{topic}}. Walk every major branch. Walk the edge paths. Look for dead ends (the agent has no valid next action), loops (the agent returns to a prior state without resolution), and ambiguous transitions (the spec does not define what the agent does next).

For each problem: name the conversation state where it occurs. Name what the spec says about this state. Name what the caller experiences if the agent cannot resolve the transition.

---

**CHECK 3: trace-state**

Hand-compile the state machine. Write out every state, every transition, every precondition and postcondition. Then check:

- Can every state be exited? A state with no defined exit transition is a trap.
- Can every transition fire without meeting its precondition? A transition that can fire early is a race condition.
- Does the spec enforce every invariant? An invariant the spec names but does not enforce is a contract the implementation will violate.

For each violation: name the state or transition. Name the spec section that defines (or fails to define) it. Name how many other states or callers depend on this contract holding -- that is the blast radius.

---

**CHECK 4: trace-contract**

Pick the three most important contract boundaries for {{topic}} -- the interfaces where caller and callee make assumptions about each other. For each one: state what the caller expects. State what the callee actually returns (per the spec). If they diverge, that is a contract violation.

For each mismatch: name the interface. State the expected value and the actual value. Name every caller that will receive the wrong output. That caller list is the blast radius.

---

**CHECK 5: trace-permissions**

Walk the RBAC model for {{topic}}. For each role, trace the permission path. Look for:

- Privilege escalation: a role can reach a resource or action they should not be able to reach
- Missing denials: an action is attempted by a role the spec does not explicitly address
- Cross-role conflicts: two roles have overlapping permissions in ways that allow race conditions or data leaks

For each finding: name the role, the path they followed, the spec section that governs this permission boundary, and who else is affected if this boundary is wrong.

---

**FINDINGS REPORT**

Now write up every problem you found. For each finding:

- **Sub-skill**: which check found it
- **Type**: spec-gap, contract-violation, state-anomaly, permission-gap, or flow-gap
- **Spec location**: name the specific section, interface, or boundary -- not "the spec is unclear about X" but "spec section 3.2, the Cancel transition definition" or "the notify() contract in section 4, expected return type"
- **What is wrong**: one sentence
- **What breaks if you ship it**: one sentence
- **What to fix**: a specific action with a named target -- not "clarify the spec" but "add a recovery state to flow-lifecycle spec section 3.1 for the timeout case in the Approval phase"

Every check must appear in the report, even if it found nothing. A check that found nothing must say why.

---

**RANKED BY BLAST RADIUS**

Rank all findings by blast radius -- how many other parts of the system are affected if you ship this finding unresolved. System-wide first. For the top three findings, state your ranking rationale: name what downstream scope makes this finding wide.

---

**COMPOUNDING FINDINGS**

Before finalizing the ranking, look across all five checks for compounding patterns -- a single root cause that appears in two or more checks. A compounding finding is elevated in the ranking because its blast radius spans multiple simulation domains. Flag each one separately with the check IDs that surface it and the shared root cause.

---

**OUTPUT**

Write the report to: simulations/{{topic}}/simulate-{{date}}.md

Every check must appear. Every finding must have a named spec location. The top three findings by blast radius must have explicit rationale for why their scope is wide.

---

## V-04 -- Combined (Output Format + Lifecycle Emphasis)

**Variation axes combined:**
1. Output format -- mandatory finding schema with all fields required, blast radius enumerated
2. Lifecycle emphasis -- 3-phase protocol per sub-skill with explicit setup, execute, and extract phases

**Hypothesis:** The combination closes the two biggest failure modes simultaneously. The per-skill phase protocol prevents silent skipping and enforces sequential execution (C-01, C-02). The mandatory finding schema prevents vague findings and drives C-06 (source + location + impact) and C-05 (spec anchoring) by making those fields required with explicit failure rules. The synthesis section adds a cross-skill pattern table that makes C-09 structurally required rather than optional. This is the most heavily scaffolded variation -- the hypothesis is that high scaffolding produces more complete rubric coverage at the cost of flexibility, and the question is whether the coverage gain is worth the added prompt complexity.

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills in order. For each sub-skill, follow the 3-phase protocol exactly. After all five complete, enter all findings into the unified findings table and produce the ranked synthesis report.

---

**FINDING SCHEMA**

Every finding uses this schema. All fields are required.

```
F-ID:           [sequential across all sub-skills: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [required: name the specific spec section, contract boundary, or interface --
                 vague references such as "the spec does not cover this" fail this field]
Summary:        [one sentence describing the problem]
Impact:         [what breaks or degrades if this finding is not resolved before implementation]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [required for blast radius = cross-skill or system-wide:
                 name the downstream flows, components, or contracts affected and explain why]
Remediation:    [specific action + named target: not "fix the spec" but the specific change,
                 naming the spec section, contract boundary, or interface and what must change]
```

---

**3-PHASE PROTOCOL**

For each sub-skill, complete all three phases before advancing.

**Phase 1 -- Setup**: Name the spec artifacts being examined. State what class of problems this sub-skill is designed to detect.

**Phase 2 -- Execute**: Run the simulation step by step. No transition may be assumed; every boundary must be walked.

**Phase 3 -- Extract**: For each problem found, produce a finding using the schema above. If no problems are found, state "no findings -- [reason]".

---

**EXECUTION: SUB-SKILL 1 -- flow-lifecycle**

Phase 1 -- Setup:
Spec artifacts: [name sections governing lifecycle phases, transitions, terminals]
Detection target: missing states, undefined phase contracts, exception flows without recovery paths, orphaned terminal paths

Phase 2 -- Execute:
[step-by-step lifecycle trace for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, one per finding block, or: "No findings -- reason: ..."]

---

**EXECUTION: SUB-SKILL 2 -- flow-conversation**

Phase 1 -- Setup:
Spec artifacts: [name sections governing conversation states, intents, transitions]
Detection target: dead ends, loops, ambiguous transitions without defined next states

Phase 2 -- Execute:
[step-by-step conversation simulation for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: ..."]

---

**EXECUTION: SUB-SKILL 3 -- trace-state**

Phase 1 -- Setup:
Spec artifacts: [name sections governing the state machine, preconditions, postconditions, invariants]
Detection target: exit-less states, precondition violations, invariant breaks, unreachable states

Phase 2 -- Execute:
[state transition hand-compilation for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: ..."]

---

**EXECUTION: SUB-SKILL 4 -- trace-contract**

Phase 1 -- Setup:
Spec artifacts: [name the contract boundaries -- interfaces, API surfaces, caller/callee assumption docs]
Detection target: caller/callee expectation divergence, undocumented edge cases at interfaces

Phase 2 -- Execute:
[expected vs actual output comparison for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: ..."]

---

**EXECUTION: SUB-SKILL 5 -- trace-permissions**

Phase 1 -- Setup:
Spec artifacts: [name sections governing RBAC, role definitions, permission boundaries]
Detection target: privilege escalation paths, missing permission denials, cross-role conflicts

Phase 2 -- Execute:
[RBAC walk-through for {{topic}}]

Phase 3 -- Extract:
[findings using schema above, or: "No findings -- reason: ..."]

---

**SYNTHESIS**

**Findings Table** (all findings from all sub-skills, in F-ID order):

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

**Ranked Findings** (blast-radius sort: system-wide first, then cross-skill, component-wide, isolated; ties broken by impact severity):

| Rank | F-ID | Sub-Skill | Summary | Blast Radius | BR Rationale |
|------|------|-----------|---------|-------------|-------------|

For all system-wide and cross-skill findings, the BR Rationale column is required. For isolated and component-wide findings it is optional.

**Cross-Skill Patterns**:

Identify any single root cause that manifests as findings across two or more sub-skills. These are not just two findings from two skills -- they share a root cause that, if fixed once, resolves multiple findings.

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Elevated Rank |
|------|------------|-------|----------------------|--------------|

If none exist: "No compounding patterns detected. All findings are independent."

---

**OUTPUT**

Write the full report to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Execution logs (all 5 sub-skills, each with 3 phases) > Findings Table > Ranked Findings > Cross-Skill Patterns.

All finding schema fields are required. Spec Location must name a specific section or boundary. BR Rationale is required for cross-skill and system-wide findings.

---

## V-05 -- Combined (Phrasing Register + Blast Radius Prominence)

**Variation axes combined:**
1. Phrasing register -- direct imperative "you" framing with gate-check orientation
2. Blast radius prominence -- blast radius is the organizing principle from the first sentence; the entire report is structured as a ranked threat assessment rather than a sequential skill log

**Hypothesis:** Leading with blast radius as the organizing principle from the first line makes C-04 and C-10 structural rather than optional -- the author is told the job is to find downstream damage and rank it, not to run five skills and append a sort. The direct register reinforces this by making "what breaks downstream" the explicit question at every step. The combination should drive C-09 (cross-skill patterns) because compounding findings naturally receive elevated blast radius, and the report structure rewards surfacing them. The risk is that blast-radius framing may cause the author to skip sub-skills that don't produce high-blast findings, threatening C-01 and C-07.

---

The goal of this simulation is to find every place where a gap or violation in {{topic}} would cause downstream damage, then rank those places by how much damage they cause.

Run the five simulation checks below. Then rank everything you find by blast radius -- how many downstream flows, components, or contracts break if you ship the finding unresolved -- and write a specific remediation for each.

---

**CHECK 1: flow-lifecycle**

Trace the business process lifecycle for {{topic}}. At every phase boundary, ask: if this phase contract is wrong, which flows downstream of it break?

Find: missing exit states, undefined exception recovery, phase transitions the spec leaves ambiguous. For every problem: name the spec section where the gap lives, name what is missing, and name every downstream flow that depends on this being correct.

---

**CHECK 2: flow-conversation**

Simulate the multi-turn conversation graph. Walk the major paths. Walk the edge paths. Find dead ends, loops, and ambiguous transitions. For every problem: name the conversation state where it occurs, what the spec says (or fails to say), and what the caller receives when the agent cannot resolve the transition.

---

**CHECK 3: trace-state**

Hand-compile the state machine for {{topic}}. Write out every state, every transition, every precondition and postcondition. Then find the failures:

- States with no exit: a caller that enters this state cannot proceed
- Transitions that can fire early: a precondition violation that corrupts the state
- Invariants the spec names but does not enforce: a contract that will be violated under load or concurrent access

For each failure: name the state or transition, name the spec section, and count how many callers depend on this contract holding. That count is your blast radius indicator.

---

**CHECK 4: trace-contract**

Identify the three most critical contract boundaries for {{topic}} -- the interfaces where caller and callee make divergent assumptions. For each: state the caller's expectation, state the callee's actual behavior per the spec, and flag the mismatch.

For each mismatch: name the interface by its spec location, state the exact divergence, and name every caller affected. That caller list is the blast radius.

---

**CHECK 5: trace-permissions**

Walk the RBAC model. For each role, trace the full permission path. Find privilege escalation routes, missing permission denials, and cross-role conflicts. For each finding: name the role, the path taken, the spec section that governs this boundary, and every other role or resource affected if this boundary is wrong.

---

**RANKED FINDINGS REPORT**

Collect every finding from all five checks. Sort by blast radius:

1. **System-wide** -- the finding affects all callers, all flows, or the full permission model
2. **Cross-skill** -- the root cause appears in two or more simulation checks; compounding effect elevates the blast radius
3. **Component-wide** -- one subsystem or one flow is affected
4. **Isolated** -- local to one state, one transition, or one permission boundary

Every check must appear in the report. A check that produced no findings must say so and state why.

| Rank | F-ID | Check | Type | Spec Location | What is wrong | Blast Radius | Why this scope | Remediation |
|------|------|-------|------|--------------|--------------|-------------|---------------|-------------|

Column rules:
- **Spec Location**: required; must name a specific spec section, interface, or contract boundary -- not "the spec is unclear"
- **Blast Radius**: system-wide / cross-skill / component-wide / isolated
- **Why this scope**: required for all system-wide and cross-skill findings; name the downstream flows, components, or contracts affected and explain why the impact reaches that far
- **Remediation**: name the target and describe the specific change -- not "fix the spec" but the exact addition or correction needed at the named location

---

**COMPOUNDING FINDINGS**

Before finalizing the ranked order, scan all findings for compounding patterns -- a single root cause that manifests in two or more simulation checks. A compounding finding is not two coincidentally related findings; it is one root cause with multiple expressions. When you identify one, elevate it to a higher blast radius tier.

For each compounding finding:

```
Pattern:      [name of the shared root cause]
Checks:       [which simulation checks surfaced this -- must be two or more]
Finding IDs:  [the F-IDs that share this root cause]
Promoted to:  [the blast radius tier after elevation -- typically cross-skill or system-wide]
Rationale:    [why the compounding effect expands the scope beyond what any single check saw]
```

---

**SIMULATION COVERAGE LOG**

Confirm that all five checks ran and record the finding IDs each produced:

| Check | Ran | Finding IDs |
|-------|-----|-------------|
| flow-lifecycle | yes / no findings | |
| flow-conversation | yes / no findings | |
| trace-state | yes / no findings | |
| trace-contract | yes / no findings | |
| trace-permissions | yes / no findings | |

A check with "no findings" must state why -- either no issues were found in this area or the check is not applicable to this topic (explain).

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Structure: Ranked Findings Report (blast-radius sorted, with tier labels) > Compounding Findings > Simulation Coverage Log.

The Ranked Findings table is the primary artifact. Every finding requires a named spec location, a blast radius tier, and a remediation with a named target. System-wide and cross-skill findings require explicit "Why this scope" rationale.
