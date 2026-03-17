---
skill: campaign-simulate
round: 3
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v3-2026-03-16.md
---

# campaign-simulate -- Round 3 Variations

**Context**: R1 achieved 95/100 on V-01, V-03, V-04. R2 targeted C-11, C-12, C-13. R3 targets the three new v3 criteria: C-14 (vacuous-filter acknowledgment), C-15 (active negative comparison in cross-skill sections), C-16 (structural coverage symmetry across filtering and empty-state axes).

**Round 3 axes chosen:**
- Single-axis: V-01 (filter log resolution / C-14), V-02 (active negative comparison phase / C-15), V-03 (inertia framing -- new axis not previously explored)
- Combined: V-04 (filter log resolution + active negative comparison / C-14 + C-15), V-05 (filter log resolution + active negative comparison + universal empty-state + symmetry declaration / C-14 + C-15 + C-16 + C-11)

---

## V-01 -- Filter Log Resolution Axis

**Variation axis:** Output format -- a mandatory "Filter Log Resolution" block is required after the filter table. The block uses one of two named templates depending on the gate outcome: Template A (normal: at least one rejection logged) or Template B (vacuous: zero rejections logged, recalibration required). This closes the vacuous-filter trap: zero rejections cannot be silently accepted as evidence of filtering quality.

**Hypothesis:** C-14 passes by construction -- the Filter Log Resolution block forces an explicit declaration of gate state in every report. When Template B fires, the prompt requires the author to revisit candidates or confirm the topic is unusually clean with a stated reason. C-13 remains structural from R2 (the filter log is required). C-11 and C-15 are not targeted here and remain the hardest remaining criteria for this variation.

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills below in order against the spec and design artifacts for {{topic}}. For each sub-skill, capture every candidate observation -- including weak ones. Apply the filter protocol. Then use the Filter Log Resolution block to declare the gate state before writing findings.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. Do not reorder.

1. flow-lifecycle    -- trace the complete business document lifecycle with phase contracts and exception flows
2. flow-conversation -- simulate multi-turn agent conversation paths with dead-end and loop detection
3. trace-state       -- hand-compile state transitions with preconditions, postconditions, and invariants
4. trace-contract    -- compare expected vs actual outputs at contract boundaries with mismatch severity
5. trace-permissions -- trace RBAC paths for each role with privilege escalation detection

After each sub-skill, list every candidate observation -- including weak ones. You will filter them in the next step.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

For each sub-skill, list observations and apply the filter rules before elevating to findings.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|
| flow-lifecycle | O-01 | | | | yes / no | |
| flow-conversation | O-02 | | | | yes / no | |
| trace-state | O-03 | | | | yes / no | |
| trace-contract | O-04 | | | | yes / no | |
| trace-permissions | O-05 | | | | yes / no | |

**Filter rules** -- reject if any apply:
1. No specific spec location can be named (not "the spec is vague" but a named section, boundary, or interface)
2. No blast radius can be estimated (cannot scope to even one downstream component)
3. Problem is a style preference, not correctness or coverage gap
4. Duplicates a finding already captured at higher blast radius

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state using one of the two templates below. This section is required in every report. Do not skip it.

**Template A -- Normal gate (at least one observation rejected):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B -- Vacuous gate (zero observations rejected):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: A gate that rejects nothing does not demonstrate filtering judgment -- it demonstrates schema compliance only. The gate ran but produced no behavioral evidence of discrimination. Required action: revisit the candidate list. Either (a) identify at least one weak observation to reject with a named filter rule, or (b) confirm this is an unusually clean topic and state explicitly why the filter rules were not triggered (e.g., every observation named a specific spec section and could be scoped to at least one downstream component).

Use Template A when at least one row in the filter log is marked "no." Use Template B when every row is marked "yes." Choosing Template B does not fail the report; silently accepting zero rejections without this block does.

---

**FINDINGS TABLE**

Only observations that passed the filter above enter this table. All fields are required. A finding with a blank required cell is incomplete and fails.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

Field definitions:
- **Sub-Skill**: which of the five sub-skills discovered this finding
- **Type**: spec-gap, contract-violation, state-anomaly, permission-gap, or flow-gap
- **Spec Location**: specific spec section, contract boundary, or interface name -- "the spec is unclear" without a named location fails this field
- **Summary**: one sentence describing the problem -- do not include impact here
- **Impact**: standalone field -- what breaks or degrades if unresolved; do not merge with Summary
- **Blast Radius**: isolated / component-wide / cross-skill / system-wide
- **Remediation**: specific action at a named target -- not "fix the spec"; must be attached here, not only in a closing summary

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates Evaluated | Rejected | Finding IDs |
|-----------|--------|---------------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

A sub-skill with "no findings" must state why. A sub-skill with zero candidates evaluated is a signal the simulation did not run.

---

**RANKED FINDINGS**

Rank all findings by blast radius (system-wide first, then cross-skill, then component-wide, then isolated). Within each tier, sort by impact severity.

**Tier 1 -- System-Wide**
[findings or: "No findings at this tier."]
[for each: name downstream flows, components, or contracts affected and explain why scope reaches that far]

**Tier 2 -- Cross-Skill**
[findings or: "No findings at this tier."]
[for each: name which sub-skills are affected and what shared root cause links them]

**Tier 3 -- Component-Wide**
[findings or: "No findings at this tier."]

**Tier 4 -- Isolated**
[findings or: "No findings at this tier."]

---

**CROSS-SKILL PATTERNS**

After completing the ranked list, scan for compounding patterns -- a single root cause that manifests in two or more sub-skills.

| P-ID | Root Cause | F-IDs Linked | Original Blast Radius (per skill) | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------------|----------------------------------|-----------------------|---------------------|

If no compounding patterns exist: "No cross-skill patterns detected -- all findings describe distinct root causes. [Brief reason why findings are independent.]"

---

**OUTPUT**

Write the simulation findings report to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings (with tier labels and blast radius rationale for top findings) > Cross-Skill Patterns.

---

## V-02 -- Active Negative Comparison Phase Axis

**Variation axis:** Lifecycle emphasis -- the cross-skill analysis is restructured as a mandatory three-step comparison protocol: (1) identify candidate pairings, (2) compare each pair and declare verdict with reason, (3) declare patterns based on Step 2 results. The conclusion "no patterns" cannot be written without a completed comparison table. This forces active negative work: the author must show what was compared before claiming nothing compounded.

**Hypothesis:** C-15 passes by construction -- the comparison table (Step 1 + Step 2) must be present regardless of the Step 3 outcome. A "no patterns" conclusion that skips the table fails this section by schema. C-09 also benefits because the comparison protocol makes the difference between "two findings that look related" and "one root cause with two expressions" an explicit judgment call. C-14 is not targeted here -- no filter resolution block is present -- so the vacuous-filter trap remains the hardest remaining failure mode.

---

Before you write a line of code for {{topic}}, prove the spec holds.

Run these five checks in order. For each check, complete all three phases before advancing. After all five complete, run the cross-skill comparison protocol -- compare every related-looking finding pair before declaring whether any patterns compound.

---

**3-PHASE PROTOCOL**

Every check follows this structure:

**Phase 1 -- Setup**: Name the spec artifacts being examined. State the class of problems this check detects.

**Phase 2 -- Execute**: Run the simulation step by step. No boundary skipped; no transition assumed without verification.

**Phase 3 -- Extract**: For each problem found, produce a finding with: check source, type, specific spec location (named section or boundary), summary (problem only), impact (standalone field), blast radius, and remediation attached to this finding. If no problems, state "no findings -- [reason]".

---

**CHECK 1: flow-lifecycle**

Phase 1 -- Setup:
- Spec artifacts: [name sections governing lifecycle phases, transitions, terminals]
- Detection target: missing exit states, undefined phase contracts, exception flows without recovery paths, orphaned terminal paths

Phase 2 -- Execute:
[step-by-step lifecycle trace for {{topic}}]

Phase 3 -- Extract:
- FL-01: [type] | Spec: [location] | Summary: [problem only] | Impact: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**CHECK 2: flow-conversation**

Phase 1 -- Setup:
- Spec artifacts: [name sections governing conversation states, intents, transitions]
- Detection target: dead ends, loops, ambiguous transitions without defined next states

Phase 2 -- Execute:
[step-by-step conversation simulation for {{topic}}]

Phase 3 -- Extract:
- FC-01: [type] | Spec: [location] | Summary: [problem only] | Impact: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**CHECK 3: trace-state**

Phase 1 -- Setup:
- Spec artifacts: [name sections governing state machine, preconditions, postconditions, invariants]
- Detection target: exit-less states, precondition violations, invariant breaks, unreachable states

Phase 2 -- Execute:
[state transition hand-compilation for {{topic}}]

Phase 3 -- Extract:
- TS-01: [type] | Spec: [location] | Summary: [problem only] | Impact: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**CHECK 4: trace-contract**

Phase 1 -- Setup:
- Spec artifacts: [name contract boundaries -- interfaces, API surfaces, caller/callee assumption docs]
- Detection target: caller/callee expectation divergence, undocumented edge cases at boundaries

Phase 2 -- Execute:
[expected vs actual output comparison for {{topic}}]

Phase 3 -- Extract:
- TC-01: [type] | Spec: [location] | Summary: [problem only] | Impact: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**CHECK 5: trace-permissions**

Phase 1 -- Setup:
- Spec artifacts: [name sections governing RBAC, role definitions, permission boundaries]
- Detection target: privilege escalation paths, missing permission denials, cross-role conflicts

Phase 2 -- Execute:
[RBAC walk-through for {{topic}}]

Phase 3 -- Extract:
- TP-01: [type] | Spec: [location] | Summary: [problem only] | Impact: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: "No findings -- reason: [explanation]"]

---

**SYNTHESIS: UNIFIED FINDINGS TABLE**

Assign sequential F-IDs across all checks (F-01, F-02, ...).

| F-ID | Source Check | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-------------|------|--------------|---------|--------|-------------|-------------|

---

**RANKED BY BLAST RADIUS**

Sort all findings by blast radius: system-wide > cross-skill > component-wide > isolated.

For the top three ranked findings, state downstream rationale: name flows, components, or contracts affected and explain why scope reaches that far.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Before declaring whether any compounding patterns exist, complete all three steps. Step 3 may not be written until Steps 1 and 2 are complete.

**Step 1 -- Candidate pairings**: List every pair of findings from different checks that share any surface similarity -- same spec area, similar problem type, related symptoms.

| Pair # | F-ID A | F-ID B | Surface similarity (why these were compared) |
|--------|--------|--------|---------------------------------------------|

If no findings exist from multiple checks: "No findings from multiple checks available for pairwise comparison. Cross-skill analysis cannot proceed."

**Step 2 -- Pairwise comparison**: For each pair from Step 1, determine: do these share a root cause (compounding) or describe distinct problems (independent)?

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|
| | | | compounding / independent | [one sentence: why they share or do not share a root cause] |

A pair is compounding only if fixing the root cause of one finding also resolves the other. Coincidental similarity (same spec area, different failure mode) is not compounding.

**Step 3 -- Patterns declaration**: Based on Step 2 results:

If at least one pair is compounding:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each pattern: state what blast radius each finding carries in isolation, what it receives after elevation, and why the compounding expands the scope ("promoted from [tier] to [tier] because [shared root cause means ...]").

If no pairs are compounding:
> No cross-skill patterns detected. Candidate pairs compared: [list Pair numbers from Step 2, their F-IDs, and their verdicts]. Each finding describes a distinct root cause.

The Step 1 and Step 2 tables must appear even when Step 3 concludes "no patterns." A "no patterns" conclusion without a completed Step 1 comparison table fails C-15.

---

**EXECUTION LOG**

| Check | Ran | Finding IDs |
|-------|-----|-------------|
| flow-lifecycle | yes / no findings | |
| flow-conversation | yes / no findings | |
| trace-state | yes / no findings | |
| trace-contract | yes / no findings | |
| trace-permissions | yes / no findings | |

A check with "no findings" must state why.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Check executions (all 5, each with 3 phases) > Unified Findings Table > Ranked by Blast Radius > Cross-Skill Comparison Protocol (Steps 1, 2, and 3) > Execution Log.

Every finding must have a named spec location, a standalone Impact field, and a finding-level Remediation. Cross-Skill Comparison Protocol Steps 1 and 2 must be present before Step 3 is written.

---

## V-03 -- Inertia Framing Axis

**Variation axis:** Inertia framing -- each check section opens with a one-line "Without this check" statement naming what a spec-only review (no simulation) would miss. The simulation campaign is positioned as a correction to the status quo of passive spec reading. The findings report asks: "what would a team that only read the spec have shipped wrong?" Findings that cannot answer that question cannot be elevated.

**Hypothesis:** Inertia framing is a motivational axis that changes the author's mental model from "run a checklist" to "prove what static review misses." C-05 (spec anchoring) becomes natural because the "without this check" frame only works if a specific spec location is named. C-04 and C-10 (blast radius ranking and rationale) become the primary output question because "what breaks downstream" is the natural completion of "what you'd miss." C-08 (remediation) follows because the frame ends with "here is what to fix." C-14 and C-15 are not directly targeted here -- the three new R3 aspirationals remain the hardest remaining criteria for this variation.

---

The goal of this simulation is to surface what a team would miss if they only read the spec for {{topic}}.

A team that reads the spec without running simulation will miss: state-machine failures that only appear when transitions are hand-compiled; contract divergences that only appear when caller expectations are compared against callee behavior explicitly; permission boundaries that only appear when the RBAC model is walked role by role. This campaign finds those gaps before implementation.

Run all five checks below. For every finding, name what the spec fails to say, what breaks downstream if you ship it, and what to add to close the gap. A finding that cannot answer "what would a team have shipped wrong" is not a finding -- it is a vague observation.

---

**CHECK 1: flow-lifecycle**

> **Without this check**: Teams typically miss undefined phase contracts and exception flows that the spec implies but never states -- the implementation fills them in with assumptions that reviewers never intended.

Walk the business process lifecycle for {{topic}} step by step. At every phase boundary: does the spec state the exact transition condition and the exact next state? For every place where the answer is no, that is a finding.

Look for: missing exit states, exception flows with no recovery path, phase contracts implied but not defined, terminal states reachable through undocumented paths.

For each finding:
- **Spec location**: name the specific section or boundary -- not "the spec is unclear" but the section identifier or boundary name
- **What the spec fails to say**: one sentence
- **What a team would implement incorrectly** (Impact): one sentence -- this is the answer to "what would they have shipped wrong"
- **What to add** (Remediation): specific addition at a named spec section
- **Blast radius**: isolated / component-wide / cross-skill / system-wide

If no findings: "flow-lifecycle check complete. No gaps detected. The spec fully addresses all phase transitions, exception flows, and terminal states examined. [Explanation of what was checked and why no gaps were found.]"

---

**CHECK 2: flow-conversation**

> **Without this check**: Teams typically miss conversation dead ends and ambiguous transitions -- states where the agent has no valid next action and the spec never tells the implementer what to do there.

Simulate the multi-turn conversation paths for {{topic}}. Walk every major branch and edge path. Find dead ends (no valid next action), loops (return to prior state without resolution), and ambiguous transitions (spec does not define next state).

For each finding:
- **Spec location**: the conversation state or transition where the gap lives
- **What the spec fails to define**: one sentence
- **What the caller experiences when this state is reached in production** (Impact): one sentence
- **What to add** (Remediation): specific state or transition definition at a named spec location
- **Blast radius**: tier

If no findings: "flow-conversation check complete. No dead ends, loops, or ambiguous transitions detected. [Explanation of paths examined and why they are fully specified.]"

---

**CHECK 3: trace-state**

> **Without this check**: Teams typically miss exit-less states and invariant violations -- problems invisible in the spec narrative but exposed immediately when every precondition and postcondition is written out.

Hand-compile the state machine for {{topic}}. Write every state, every transition, every precondition and postcondition. Then identify:
- States with no exit transition (traps -- a caller that enters cannot proceed)
- Transitions that can fire without meeting their precondition (race conditions)
- Invariants the spec names but does not structurally enforce

For each violation:
- **State or transition**: named exactly
- **Spec location**: the section that defines (or fails to define) it
- **What an implementation will get wrong** (Impact): one sentence
- **What to add** (Remediation): specific addition at a named spec section
- **Blast radius**: how many callers or downstream states depend on this contract -- tier

If no violations: "trace-state check complete. All states have defined exits. All transitions have enforceable preconditions. All named invariants are structurally enforced. [Explanation of what was compiled and why no violations were found.]"

---

**CHECK 4: trace-contract**

> **Without this check**: Teams typically miss caller/callee assumption divergence -- the spec describes behavior from the callee's perspective, and callers assume something different. This only appears when both sides are stated explicitly and compared.

Identify the three most important contract boundaries for {{topic}} -- interfaces where callers and callees make assumptions about each other. For each:
- State what the caller expects (what they send and what they expect back)
- State what the callee actually does per the spec
- If they diverge, that is a contract violation

For each mismatch:
- **Interface and spec location**: named exactly
- **The divergence**: caller expects X, callee returns Y
- **Every caller affected** (Blast radius contributors): named
- **What to add** (Remediation): specific addition to the contract spec at the named boundary
- **Blast radius**: tier based on affected callers

If no mismatches: "trace-contract check complete. Caller and callee assumptions are aligned at all three contract boundaries examined. [Name the three boundaries and explain why they are aligned.]"

---

**CHECK 5: trace-permissions**

> **Without this check**: Teams typically miss privilege escalation paths -- routes through the permission model that the spec never explicitly addresses, which only surface when every role's path is traced through the RBAC graph.

Walk the RBAC model for {{topic}}. For each role, trace the full permission path. Find:
- Privilege escalation: a role reaching a resource or action it should not
- Missing denials: an action attempted by a role the spec does not explicitly address
- Cross-role conflicts: overlapping permissions enabling race conditions or data leaks

For each finding:
- **Role and path**: named exactly
- **Spec location**: the permission boundary section that governs this
- **Who else is affected if this boundary is wrong** (Blast radius contributors): named
- **What to add** (Remediation): specific permission boundary to define at a named spec location
- **Blast radius**: tier

If no findings: "trace-permissions check complete. No privilege escalation routes, missing denials, or cross-role conflicts detected. [Roles examined and why the RBAC model is complete.]"

---

**FINDINGS REPORT**

Collect every finding from all five checks. Assign F-IDs (F-01, F-02, ...).

For each finding, the report must answer: what would a team that only read the spec have shipped wrong? That answer is the Impact field.

| F-ID | Check | Type | Spec Location | What the spec fails to say | What a team would ship wrong (Impact) | Blast Radius | What to add (Remediation) |
|------|-------|------|--------------|---------------------------|--------------------------------------|-------------|--------------------------|

Every check must appear in the report, even if it found nothing. A check that found nothing must state what was examined and why no gaps were found.

---

**RANKED BY BLAST RADIUS**

Sort all findings by blast radius: system-wide > cross-skill > component-wide > isolated.

For the top three findings, state: "A team that only read the spec would have shipped this and discovered [consequence] only when [failure mode in production]." Name the downstream scope.

---

**COMPOUNDING FINDINGS**

Before finalizing the ranking, look across all five checks for a single root cause that manifests in two or more checks. When a root cause is compounding, the blast radius is wider than any single check shows -- the same underlying gap produces multiple failure modes.

For each compounding finding:
```
Pattern:        [the shared root cause -- not the symptoms, the cause]
Checks:         [which checks surfaced this -- must be two or more]
Finding IDs:    [the F-IDs that share this root cause]
Without simulation: [what a team that only read the spec would have shipped here]
Promoted to:    [the blast radius tier after elevation]
Rationale:      [why the compounding effect expands scope beyond what any single check saw]
```

If no compounding patterns: "No compounding patterns detected. Each finding describes a gap unique to its check area. [Name any findings that appeared related and explain why they describe different root causes rather than a shared one.]"

---

**EXECUTION LOG**

| Check | Ran | Finding IDs |
|-------|-----|-------------|
| flow-lifecycle | yes / no findings | |
| flow-conversation | yes / no findings | |
| trace-state | yes / no findings | |
| trace-contract | yes / no findings | |
| trace-permissions | yes / no findings | |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Structure: Check executions (all 5) > Findings Report (table) > Ranked by Blast Radius > Compounding Findings > Execution Log.

Every finding must name a spec location and answer "what would a team that only read the spec have shipped wrong." The Compounding Findings section must name related-looking findings before declaring they are independent.

---

## V-04 -- Combined (Filter Log Resolution + Active Negative Comparison)

**Variation axes combined:**
1. Filter Log Resolution (V-01) -- mandatory Filter Log Resolution block using Template A or Template B based on rejection count; zero rejections trigger recalibration notice (C-14)
2. Active Negative Comparison Phase (V-02) -- cross-skill analysis runs as a three-step comparison protocol; "no patterns" requires a completed comparison table (C-15)

**Hypothesis:** C-14 passes by construction via the Filter Log Resolution block -- zero rejections cannot be silently accepted. C-15 passes by construction via the comparison protocol -- "no patterns" cannot be declared without a completed Step 1 + Step 2 table. Both are structurally enforced independently. C-13 (filter gate) is structural from R2. C-16 gets partial credit: the filtering axis has structural enforcement (filter log + resolution block) and the comparison protocol provides structural enforcement for the cross-skill section, but no universal empty-state protocol covers all section types. Hardest remaining: C-11 (empty-state for all section types), C-12 (compounding elevation with before/after scope).

---

Simulate the technical behavior of: {{topic}}

Run the full technical simulation campaign. Execute all five sub-skills in the order listed. After each sub-skill, capture candidate observations and apply the filter protocol. After completing all five, run the cross-skill comparison protocol before declaring any patterns.

---

**FINDING SCHEMA**

Every finding uses this schema. All fields are required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: name the specific spec section, contract boundary, or interface --
                 "the spec does not address this" without a named location fails this field]
Summary:        [one sentence -- the problem only, no impact language]
Impact:         [STANDALONE FIELD: what breaks or degrades if unresolved --
                 merging Impact into Summary fails this field]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [required for cross-skill or system-wide: name downstream scope and explain why]
Remediation:    [specific action at named target -- "fix the spec" fails this field;
                 must be attached here, not only in a closing summary]
```

---

**EXECUTION SEQUENCE**

Run each sub-skill in order:

1. flow-lifecycle    -- trace the complete lifecycle with phase contracts and exception flows
2. flow-conversation -- simulate multi-turn conversation paths with dead-end and loop detection
3. trace-state       -- hand-compile state transitions with preconditions, postconditions, invariants
4. trace-contract    -- compare expected vs actual outputs at contract boundaries
5. trace-permissions -- trace RBAC paths with privilege escalation detection

After each sub-skill, list every candidate observation before filtering.

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

For each sub-skill, list observations and apply filter rules before elevating to findings.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** -- reject if any apply:
1. No specific spec location can be named
2. No blast radius can be estimated (cannot scope to even one downstream component)
3. Problem is a style preference, not correctness or coverage gap
4. Duplicates a finding already captured at higher blast radius

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state. This section is required in every report.

**Template A -- Normal gate (at least one observation rejected):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason for each]). Gate operating normally -- filtering judgment demonstrated.

**Template B -- Vacuous gate (zero observations rejected):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment -- only that the schema ran. Required action: revisit the candidate list. Either (a) identify at least one weak observation to reject with a named filter rule, or (b) confirm this is an unusually clean topic and state explicitly why the filter rules were not triggered (e.g., every observation named a specific spec section and could be scoped to at least one downstream component).

Use Template A when any observation is marked "no" in the filter log. Use Template B when all observations are marked "yes." Choosing Template B is not a failure; silently accepting zero rejections without this block is.

---

**FINDINGS TABLE**

Only observations that passed the filter enter this table.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

If no observations passed: "No findings elevated. All candidate observations failed the filter rules or no problems were detected."

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | Rejected | Finding IDs |
|-----------|--------|------------|---------|-------------|
| flow-lifecycle | executed / no findings | | | |
| flow-conversation | executed / no findings | | | |
| trace-state | executed / no findings | | | |
| trace-contract | executed / no findings | | | |
| trace-permissions | executed / no findings | | | |

A sub-skill with zero candidates evaluated did not run.

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings, or: "No findings at this tier."]
[for each: name downstream scope]

**Tier 2 -- Cross-Skill**
[findings, or: "No findings at this tier."]
[for each: name which sub-skills and shared root cause]

**Tier 3 -- Component-Wide**
[findings, or: "No findings at this tier."]

**Tier 4 -- Isolated**
[findings, or: "No findings at this tier."]

For all top three ranked findings: state the blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Before declaring whether any compounding patterns exist, complete all three steps. Step 3 cannot be written until Steps 1 and 2 are complete.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills that share any surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills exist, state this explicitly.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|
| | | | compounding / independent | [one sentence on root cause relationship or lack thereof] |

A pair is compounding only if fixing the root cause of one resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each: state blast radius per finding in isolation, elevated tier after compounding, and why the shared root cause expands scope ("promoted from [tier] to [tier] because [...]").

If no compounding pairs:
> No cross-skill patterns detected. Candidate pairs compared: [list Pair numbers from Step 2 with their verdicts and F-IDs]. Each pair describes findings with distinct root causes.

Steps 1 and 2 must be completed regardless of Step 3 outcome. A "no patterns" conclusion without a Step 1 table fails C-15.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, and 3).

Filter Log Resolution is required in every report. Cross-Skill Comparison Protocol Steps 1 and 2 must be present before Step 3 is written.

---

## V-05 -- Combined: Full Structural Symmetry

**Variation axes combined:**
1. Filter Log Resolution (V-01) -- C-14: vacuous-filter trap closed by mandatory Template A / Template B declaration
2. Active Negative Comparison Phase (V-02) -- C-15: passive omission closed by mandatory comparison table before pattern declaration
3. Universal Empty-State Protocol (from R2 V-03) -- C-11: all sections have defined templates; silence is not acceptable anywhere
4. Structural symmetry declaration -- C-16: the preamble names both structural axes and their mechanisms explicitly, making coverage symmetry verifiable from structure alone

**Hypothesis:** C-14 passes by construction (Filter Log Resolution block). C-15 passes by construction (comparison protocol). C-11 passes by construction (universal templates defined for all section types). C-16 passes because both the filtering axis and the empty-state axis are named as structural in the preamble -- verifiable from the report structure without assuming model compliance. C-13 and C-12 both benefit from the combined scaffolding. Risk: this is the longest variation; authors may abbreviate structural sections under length pressure. If a structural section is abbreviated below its required content, the criterion it enforces fails -- but the structure itself prevents silent failure.

---

Simulate the technical behavior of: {{topic}}

This report enforces two structural axes simultaneously:

- **Filtering axis** (structural): A filter gate runs before the findings table. All rejection decisions are logged. The gate resolution is declared explicitly -- Template A (normal: at least one rejection) or Template B (vacuous: zero rejections, recalibration required). Observable from the filter log and resolution block. Not dependent on model judgment.
- **Empty-state axis** (structural): Every report section has a defined empty-state template. No section is blank or absent without using its template. Observable from section presence and template text. Not dependent on model judgment.

Both axes are verifiable from the report structure alone.

Execute all five sub-skills in the order listed. Apply the filter protocol after each sub-skill. After all five, run the cross-skill comparison protocol. Declare patterns and apply empty-state templates across all sections.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment. Revisit candidates -- either identify a weak observation to reject under a named rule, or confirm this topic is unusually clean and explain why the filter rules were not triggered."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts from the Step 2 table]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation of why this area produced no observable candidates]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference without named location fails this field]
Summary:        [one sentence, problem only --
                 FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide --
                 FAILURE: wide-scope finding without rationale fails C-10]
Remediation:    [REQUIRED HERE: specific action at named target --
                 FAILURE: "fix the spec" or remediation only in closing summary fails C-08]
```

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, list candidate observations before filtering.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions, invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

For each sub-skill, list all observations (including weak ones) and apply filter rules.

| Sub-Skill | Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|-------------|----------|-----------------|

**Filter rules** (reject if any apply):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

Sub-skill with zero candidates: apply the execution-log empty-state template.

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state. This block is required in every report.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [brief reason for each rejection]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: A gate that rejects nothing provides no evidence of filtering judgment -- it demonstrates only that the schema ran. Required: revisit candidate list. Either (a) name at least one observation that should be rejected under the filter rules, or (b) provide explicit justification that every candidate is genuinely anchored to a named spec location and scoped to at least one downstream component.

Template A applies when at least one filter log row is "no." Template B applies when all rows are "yes." Template B is not a failure; silence about zero rejections is.

---

**FINDINGS TABLE**

Only observations that passed the filter. If none: apply the findings-table empty-state template.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

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

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream rationale, or: apply ranked-tier empty-state template]

**Tier 2 -- Cross-Skill**
[findings with shared root cause rationale, or: apply ranked-tier empty-state template]

**Tier 3 -- Component-Wide**
[findings, or: apply ranked-tier empty-state template]

**Tier 4 -- Isolated**
[findings, or: apply ranked-tier empty-state template]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2 to be present.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills that share surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

If no findings from multiple sub-skills: apply the comparison-step empty-state template.

**Step 2 -- Pairwise comparison**: For each pair, determine compounding or independent.

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each compounding finding: "Promoted from [isolated tier] to [elevated tier] because [cross-skill root cause means that X, which expands downstream scope from [what it covers alone] to [what it covers combined]]."

If no compounding pairs: apply the cross-skill-patterns empty-state template (requires citing Step 2 pairs and verdicts).

Steps 1 and 2 are required even when Step 3 concludes no patterns. The empty-state template for Step 3 must cite the Step 2 comparison table.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3).

Structural enforcement checklist (verifiable from report structure alone -- no content inference required):
- [ ] Filter log contains observation rows with Elevate? column filled (or execution-log empty-state template applied per sub-skill)
- [ ] Filter Log Resolution block is present with Template A or Template B text
- [ ] Every ranked tier label appears (empty tiers use ranked-tier empty-state template)
- [ ] Cross-Skill Comparison Protocol Steps 1 and 2 tables are present (even when Step 3 finds no patterns)
- [ ] Every section with no content uses its defined empty-state template

Both the filtering axis (filter log + Filter Log Resolution block) and the empty-state axis (templates defined and applied across all section types) must be observable from the checklist above without reading finding content.
