---
skill: campaign-simulate
round: 4
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v4-2026-03-16.md
---

# campaign-simulate -- Round 4 Variations

**Context**: R3 V-05 scored highest by introducing a structural-axis preamble and an end-of-report checklist, which were codified as C-17 (Pre-Finding Structural Axis Declaration) and C-18 (End-of-Report Structural Compliance Checklist) in rubric v4. The v4 rubric adds these two criteria to close the gaps: V-05's preamble was prompt-level instruction text (not a section the model writes into the output artifact), and its end-checklist used template checkboxes without requiring evidence citations. R4 targets both gaps.

**Round 4 axes chosen:**
- Single-axis: V-01 (declaration section written into output / C-17), V-02 (evidence-citation compliance checklist / C-18), V-03 (audit register -- organic C-17 + C-18 via domain framing)
- Combined: V-04 (C-17 declaration + C-18 checklist on R3 V-05 base), V-05 (full integration: 4 structural axes + declaration + compliance checklist)

---

## V-01 -- Pre-Finding Structural Axis Declaration Axis

**Variation axis:** Output format -- the model is required to write a STRUCTURAL AXIS DECLARATION section as the first section of the output report (before any execution results or findings). The declaration table names each structural axis, the mechanism implementing it, and the report section where it fires. This section is part of the output artifact, not the prompt preamble -- its presence in the report makes structural commitments verifiable before reading any findings.

**Hypothesis:** C-17 passes by construction -- the declaration table appears before findings in the output, names at least three structural axes (filtering, empty-state, cross-skill comparison), and names the specific mechanism for each. C-16 also benefits because the declaration table makes structural symmetry directly inspectable. C-18 is not targeted here (no compliance checklist at the end), so the closing verification gap remains. All prior R3 V-05 mechanisms (filter log, empty-state templates, comparison protocol) carry forward unchanged.

---

Simulate the technical behavior of: {{topic}}

This report enforces three structural axes simultaneously. Before any findings, write the STRUCTURAL AXIS DECLARATION section in your output. Then run the execution sequence. Both axes -- filtering and empty-state -- are verifiable from the report structure alone without assuming model compliance.

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

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. This is part of your output artifact -- not the prompt text. Fill in the "Report Section" column using the actual section names from this report. Complete this table before writing any execution results.

| Axis | Criteria | Mechanism | Report Section Where It Fires |
|------|----------|-----------|-------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with named rejection rules (Rules 1-4); Filter Log Resolution block (Template A or B) | Candidate Observations and Filter Log; Filter Log Resolution |
| Empty-state axis | C-11 | Per-section empty-state templates applied to all structured sections | [list the sections where templates fire, or write "all structured sections"] |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1), pairwise verdicts (Step 2), pattern declaration (Step 3 requires Steps 1+2) | Cross-Skill Comparison Protocol |

An evaluator reading this table should be able to predict what structural sections appear in the report before reading any findings. If a declared mechanism does not fire, the declaration becomes a false commitment -- do not declare mechanisms you do not use.

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

For each compounding finding: "Promoted from [tier] to [tier] because [cross-skill root cause means ...]."

If no compounding pairs: apply the cross-skill-patterns empty-state template (must cite Step 2 pairs and verdicts).

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3).

The Structural Axis Declaration must be the first section of the output file. An evaluator must be able to read the declaration and predict what structural sections follow before reading any findings.

---

## V-02 -- End-of-Report Structural Compliance Checklist Axis

**Variation axis:** Output format -- the model is required to write a STRUCTURAL COMPLIANCE CHECKLIST as the final section of the output report. The checklist uses a four-column schema (Mechanism, Report Section, Evidence, Status) where the Evidence column requires citing actual counts and outcomes from the report body. The model cannot write "fired" without naming the section where the mechanism fired and quoting the evidence. Empty checkboxes are not acceptable -- every row requires a completed Evidence entry.

**Hypothesis:** C-18 passes by construction -- the schema forces the model to cite actual section names and evidence counts for each mechanism, not just confirm that mechanisms were intended to fire. The difference between "Filter Log applied" (partial pass) and "Filter Log: Candidate Observations section, 4 observations, 1 rejected at Rule 1" (full pass) is structural -- the Evidence column enforces it. C-17 is not directly targeted here; the preamble from R3 V-05 approximates C-17 at the prompt level but no formal declaration section is written into the output. Hardest remaining gap after this variation: C-17 (model-written declaration in output before findings).

---

Simulate the technical behavior of: {{topic}}

This report enforces two structural axes simultaneously:

- **Filtering axis** (structural): A filter gate runs before the findings table. All rejection decisions are logged. The gate resolution is declared explicitly -- Template A (normal: at least one rejection) or Template B (vacuous: zero rejections, recalibration required). Observable from the filter log and resolution block. Not dependent on model judgment.
- **Empty-state axis** (structural): Every report section has a defined empty-state template. No section is blank or absent without using its template. Observable from section presence and template text. Not dependent on model judgment.

Both axes are verifiable from the report structure alone. At the end of the report, a STRUCTURAL COMPLIANCE CHECKLIST verifies each mechanism actually fired -- with section citations and evidence counts.

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

For each compounding finding: "Promoted from [tier] to [tier] because [cross-skill root cause means ...]."

If no compounding pairs: apply the cross-skill-patterns empty-state template (must cite Step 2 pairs and verdicts).

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. This is part of your output artifact. For each mechanism, name the report section where it fired and provide evidence (actual counts and outcomes). Do not write "fired" without citing the section and evidence. Do not copy hypothetical values -- cite what actually appears in the report you just wrote.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "4 observations evaluated, 1 rejected at Rule 1: no spec location"] | fired / not fired |
| Filter Log Resolution block | [section name] | [e.g., "Template A applied: 3 elevated, 1 rejected" OR "Template B applied: zero rejections, recalibration invoked"] | fired / not fired |
| Empty-state templates | [list sections where templates fired] | [e.g., "Ranked tier 1 template applied: 'No findings at system-wide blast radius'"] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [e.g., "3 candidate pairs compared in Step 2; 0 compounding"] | fired / not fired |

A mechanism marked "not fired" is a structural compliance failure that this checklist surfaces -- it does not fail the report silently. If a mechanism did not fire, state why.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

The Structural Compliance Checklist must be the final section of the output file. Every row in the checklist must name an actual section from this report and cite actual evidence from that section.

---

## V-03 -- Audit Register Axis

**Variation axis:** Phrasing register -- the skill is recast as a formal technical audit. The prompt uses audit vocabulary throughout: AUDIT SCOPE (declares what controls are active), AUDIT EXECUTION (5 checks run as audit tests), AUDIT COMPLIANCE SUMMARY (verifies what controls fired). The hypothesis is that an audit register organically produces a scope section (analog to C-17) and a compliance summary (analog to C-18) without requiring explicit structural templates. This tests whether domain framing alone can produce better structural discipline than explicit mechanism declarations.

**Hypothesis:** C-17 and C-18 may fire organically -- audit scope sections declare controls before findings, and compliance summaries verify them after. The register frames the entire simulation as "prove the spec is auditable" rather than "run a checklist," which changes the author's mental model. Risk: the organic audit format tends to produce prose scope sections and narrative compliance summaries rather than the table/citation structure that C-17/C-18 pass conditions require. Mechanism names must be explicit ("Filter Log with named rules") not implicit ("we applied filtering"). Section citations in the compliance summary must be specific ("Section 3, 1 rejection logged") not generic ("filtering was applied"). This variation tests whether a register change is sufficient or whether explicit schema enforcement is required.

---

Conduct a technical pre-implementation audit of: {{topic}}

This audit determines whether the spec for {{topic}} is implementation-ready. A spec is implementation-ready when its lifecycle transitions are fully defined, its state machine has no exit-less states, its contract boundaries have no assumption divergence, and its permission model has no escalation paths. The audit runs five checks. Each check is a formal audit test with a defined scope, a detection protocol, and a set of audit findings. The findings are ranked by blast radius -- how far an unresolved gap propagates if the team ships without fixing it.

---

**AUDIT SCOPE AND STRUCTURAL CONTROLS**

Write this section as the first section of the audit report. Declare the audit scope and name each structural control active in this report.

**Audit scope**: Technical specification audit for {{topic}} covering business lifecycle, conversation flows, state machine, contract boundaries, and permission model.

**Structural controls active in this report:**

| Control | Purpose | Mechanism | Report Section |
|---------|---------|-----------|---------------|
| Observation filter | Reject weak observations before elevating to findings | Filter Log with four named rejection rules; Filter Log Resolution block (Template A: normal / Template B: vacuous gate) | Observation Filter Log; Filter Gate Resolution |
| Empty-state discipline | Prevent silent empty sections | Per-section audit templates applied when no content found | All sections -- any with no audit results |
| Cross-check comparison | Require active comparison before declaring no compounding | Three-step comparison: candidates (Step 1), pairwise verdicts (Step 2), declaration (Step 3) | Cross-Check Compounding Analysis |

Declaring a control does not satisfy it. Each control must produce observable output in its named report section.

---

**FILTER LOG TEMPLATES**

When no audit results exist for a section, use the appropriate template below. Do not leave sections blank.

- **Audit check no findings**: "Audit check [name] complete. Artifacts examined: [list]. No deficiencies found because [reason]. This check is closed."
- **Filter gate zero rejections**: "Observation filter applied. [N] observations evaluated. Zero rejected. NOTE: A filter gate with zero rejections provides no evidence of filtering judgment -- it confirms only that the schema was applied. Action required: either identify at least one observation that fails a named filter rule, or confirm the topic is unusually clean and explain which filter rules did not trigger and why."
- **Audit findings table empty**: "No audit findings elevated. All observations failed filter rules or no deficiencies were detected during audit execution."
- **Blast radius tier empty**: "No audit findings at [tier] blast radius."
- **Cross-check candidates empty**: "No findings from multiple audit checks available for cross-check comparison. Compounding analysis cannot proceed."
- **Cross-check summary no compounding**: "No compounding deficiencies identified. Cross-check comparisons conducted in Step 2: [list pairs and verdicts]. Each deficiency originates from a distinct root cause."

---

**AUDIT FINDING SCHEMA**

All fields required for every finding.

```
AF-ID:          [sequential: AF-01, AF-02, ...]
Audit check:    [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Deficiency type:[spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec reference: [REQUIRED: named section, boundary, or interface; a finding without a specific reference
                 is an observation -- it does not qualify as an audit finding]
Deficiency:     [one sentence, the problem only; do not include consequences here]
Consequence:    [STANDALONE FIELD: what the implementation team ships wrong if this is unresolved;
                 must be separable from the Deficiency field]
Blast radius:   [isolated / component-wide / cross-check / system-wide]
BR basis:       [REQUIRED for cross-check or system-wide: name affected flows, components, or contracts]
Remediation:    [specific addition or change at a named spec section; "update the spec" fails this field]
```

---

**AUDIT EXECUTION**

Run all five checks in the order below. After each check, complete the Observation Filter Log before advancing to the next check.

**AUDIT CHECK 1: flow-lifecycle**

Audit scope: Trace the complete business document lifecycle for {{topic}}, including all phase transitions, exception paths, and terminal states.

Detection targets: Undefined phase contracts (transition condition not stated), exception flows with no recovery path, terminal states reachable through undocumented paths, phases with no defined exit condition.

Observation log for this check:

| Obs # | What was observed | Spec Reference | Estimated Blast Radius | Elevate to finding? | If no: rejection rule applied |
|-------|------------------|---------------|----------------------|--------------------|-----------------------------|

Audit findings (observations that passed the filter):
- AF-[N]: [deficiency type] | Spec: [reference] | Deficiency: [one sentence] | Consequence: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: apply audit-check-no-findings template]

---

**AUDIT CHECK 2: flow-conversation**

Audit scope: Simulate the multi-turn conversation paths for {{topic}}, tracing every major branch and edge path.

Detection targets: Dead ends (no valid next action defined), loops (return to prior state without resolution), ambiguous transitions (spec does not define next state).

Observation log for this check:

| Obs # | What was observed | Spec Reference | Estimated Blast Radius | Elevate to finding? | If no: rejection rule applied |
|-------|------------------|---------------|----------------------|--------------------|-----------------------------|

Audit findings:
- AF-[N]: [deficiency type] | Spec: [reference] | Deficiency: [one sentence] | Consequence: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: apply audit-check-no-findings template]

---

**AUDIT CHECK 3: trace-state**

Audit scope: Hand-compile the state machine for {{topic}}, enumerating every state, transition, precondition, and postcondition.

Detection targets: Exit-less states (callers that enter cannot proceed), transitions that can fire without meeting preconditions, invariants named but not structurally enforced.

Observation log for this check:

| Obs # | What was observed | Spec Reference | Estimated Blast Radius | Elevate to finding? | If no: rejection rule applied |
|-------|------------------|---------------|----------------------|--------------------|-----------------------------|

Audit findings:
- AF-[N]: [deficiency type] | Spec: [reference] | Deficiency: [one sentence] | Consequence: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: apply audit-check-no-findings template]

---

**AUDIT CHECK 4: trace-contract**

Audit scope: Identify the three most critical contract boundaries for {{topic}} and compare caller and callee assumptions at each.

Detection targets: Divergence between what the caller sends and expects versus what the callee does per the spec; undocumented edge cases at boundary interfaces.

Observation log for this check:

| Obs # | What was observed | Spec Reference | Estimated Blast Radius | Elevate to finding? | If no: rejection rule applied |
|-------|------------------|---------------|----------------------|--------------------|-----------------------------|

Audit findings:
- AF-[N]: [deficiency type] | Spec: [reference] | Deficiency: [one sentence] | Consequence: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: apply audit-check-no-findings template]

---

**AUDIT CHECK 5: trace-permissions**

Audit scope: Walk the RBAC model for {{topic}}, tracing each role's permission path through the full authorization graph.

Detection targets: Privilege escalation (a role reaching a resource or action it should not), missing denials (actions attempted by roles the spec does not address), cross-role conflicts enabling race conditions or data leaks.

Observation log for this check:

| Obs # | What was observed | Spec Reference | Estimated Blast Radius | Elevate to finding? | If no: rejection rule applied |
|-------|------------------|---------------|----------------------|--------------------|-----------------------------|

Audit findings:
- AF-[N]: [deficiency type] | Spec: [reference] | Deficiency: [one sentence] | Consequence: [standalone] | Blast radius: [tier] | Remediation: [specific action at named target]
- [additional findings, or: apply audit-check-no-findings template]

---

**OBSERVATION FILTER GATE RESOLUTION**

After completing all five observation logs, declare the gate state. This section is required.

**Template A (at least one observation rejected across any check):**
> Observation filter applied. [N total] observations evaluated across all checks. [M] rejected. Rejected observations: [list check, observation, and rule number for each]. Gate operating normally -- filtering judgment demonstrated.

**Template B (zero observations rejected across all checks):**
> Observation filter applied. [N total] observations evaluated across all checks. Zero rejected. GATE RECALIBRATION REQUIRED: Zero rejections provide no evidence of filtering judgment -- only that the schema was applied. Action: revisit each check's observation log. Either (a) identify at least one observation that should be rejected under the named filter rules, or (b) confirm this is an unusually clean spec and state which filter rules each check did not trigger and why.

---

**UNIFIED AUDIT FINDINGS TABLE**

Collect all elevated findings. Assign sequential AF-IDs if not already assigned.

| AF-ID | Audit Check | Deficiency Type | Spec Reference | Deficiency | Consequence | Blast Radius | Remediation |
|-------|------------|-----------------|---------------|------------|-------------|-------------|-------------|

If no findings: apply the audit-findings-table-empty template.

---

**AUDIT EXECUTION LOG**

| Check | Status | Observations | Rejected | Finding IDs |
|-------|--------|-------------|---------|-------------|
| flow-lifecycle | complete / no findings | | | |
| flow-conversation | complete / no findings | | | |
| trace-state | complete / no findings | | | |
| trace-contract | complete / no findings | | | |
| trace-permissions | complete / no findings | | | |

---

**BLAST RADIUS RANKING**

Sort all audit findings by blast radius: system-wide > cross-check > component-wide > isolated.

**Tier 1 -- System-Wide**
[findings with downstream scope rationale, or: apply blast-radius-tier-empty template]

**Tier 2 -- Cross-Check**
[findings naming which audit checks are affected and shared root cause, or: apply blast-radius-tier-empty template]

**Tier 3 -- Component-Wide**
[findings, or: apply blast-radius-tier-empty template]

**Tier 4 -- Isolated**
[findings, or: apply blast-radius-tier-empty template]

For the top three ranked findings, state the blast radius basis: which downstream flows, components, or contracts are affected and why the scope reaches that far.

---

**CROSS-CHECK COMPOUNDING ANALYSIS**

Before declaring whether compounding deficiencies exist, complete all three steps. Step 3 requires Steps 1 and 2.

**Step 1 -- Candidate pairs**: List every pair of findings from different audit checks that share any surface similarity.

| Pair # | AF-ID A | AF-ID B | Why these were compared |
|--------|---------|---------|------------------------|

If no findings from multiple checks: apply the cross-check-candidates-empty template.

**Step 2 -- Pairwise verdict**: For each pair, determine whether fixing one also fixes the other.

| Pair # | AF-ID A | AF-ID B | Verdict | Reason |
|--------|---------|---------|---------|--------|
| | | | compounding / independent | [one sentence on whether the root cause is shared or distinct] |

**Step 3 -- Compounding declaration**:

If compounding pairs identified:

| P-ID | Root Cause | AF-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|-----------|--------|-------------------------|-----------------------|---------------------|

For each compounding finding: "Promoted from [tier] to [tier] because [shared root cause means ...]."

If no compounding pairs: apply the cross-check-summary-no-compounding template (must cite Step 2 pairs and verdicts by pair number).

Steps 1 and 2 must appear in the report even when Step 3 concludes no compounding.

---

**AUDIT COMPLIANCE SUMMARY**

Write this section as the final section of the audit report. For each structural control declared in the AUDIT SCOPE AND STRUCTURAL CONTROLS section, confirm whether it fired and provide specific evidence. Do not write "applied" without citing the section and actual counts. This is the audit's self-assessment of its own structural integrity.

| Control | Declared Section | Execution Evidence | Result |
|---------|-----------------|-------------------|--------|
| Observation filter | Observation Filter Gate Resolution | [cite: "N observations, M rejected at Rule K" or "Template B applied, zero rejections"] | compliant / non-compliant |
| Empty-state discipline | [list sections where templates fired] | [cite: "Template applied in [section]: '[first few words of template text]'"] | compliant / non-compliant |
| Cross-check comparison | Cross-Check Compounding Analysis | [cite: "N pairs compared in Step 2, verdicts: [list]"] | compliant / non-compliant |

A "non-compliant" result means the control was declared but did not fire. State why and whether the audit findings are still valid without it.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Audit Scope and Structural Controls > Filter Log Templates (embedded) > Audit Execution (5 checks) > Observation Filter Gate Resolution > Unified Audit Findings Table > Audit Execution Log > Blast Radius Ranking > Cross-Check Compounding Analysis (Steps 1, 2, 3) > Audit Compliance Summary.

---

## V-04 -- Combined: C-17 Declaration + C-18 Checklist

**Variation axes combined:**
1. Pre-Finding Structural Axis Declaration (V-01) -- a STRUCTURAL AXIS DECLARATION section is written by the model into the output artifact before any findings; names axes, mechanisms, and report sections
2. End-of-Report Structural Compliance Checklist (V-02) -- a STRUCTURAL COMPLIANCE CHECKLIST section is written by the model at the end of the output; requires mechanism, section, evidence, and status for each structural mechanism declared in the declaration

**Hypothesis:** C-17 passes by construction via the declaration table (written into the output, before findings). C-18 passes by construction via the compliance checklist (written at the end, with evidence citations). All prior R3 V-05 mechanisms carry forward: C-13 (filter log), C-14 (filter log resolution), C-15 (comparison protocol steps), C-11 (empty-state templates), C-16 (structural symmetry -- now verifiable from the declaration table alone). C-12 (compounding elevation) benefits from the compliance checklist verifying whether the cross-skill comparison fired. Risk: two new required sections add length pressure; authors may abbreviate the evidence column in the compliance checklist. Abbreviated evidence (writing "fired" without actual counts) produces a partial pass on C-18, not a fail.

---

Simulate the technical behavior of: {{topic}}

This report enforces three structural axes. Before any findings, write the STRUCTURAL AXIS DECLARATION. After all findings, write the STRUCTURAL COMPLIANCE CHECKLIST. Both sections are part of the output artifact -- they are not the prompt text you are reading.

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
- **Compliance checklist not fired**: "Mechanism declared but not fired. Reason: [why the mechanism did not produce output]."

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

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report, before any execution results. This is part of the output artifact -- not the prompt text. An evaluator reading this section must be able to predict what structural mechanisms appear in the report before reading any findings.

| Axis | Criteria | Mechanism | Report Section Where It Fires |
|------|----------|-----------|-------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with named rejection rules (Rules 1-4); Filter Log Resolution block (Template A: normal gate / Template B: vacuous gate, recalibration required) | Candidate Observations and Filter Log; Filter Log Resolution |
| Empty-state axis | C-11 | Per-section empty-state templates for all structured sections -- blank sections use the named template for their type | [fill in: list all sections where templates may fire] |
| Cross-skill comparison axis | C-15 | Three-step protocol: candidate pairings (Step 1) + pairwise verdicts (Step 2) + pattern declaration (Step 3, requires Steps 1+2) | Cross-Skill Comparison Protocol |

If you add structural mechanisms beyond those declared here, add rows. Declared mechanisms that do not fire appear as "not fired" in the STRUCTURAL COMPLIANCE CHECKLIST at the end of this report.

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

If no compounding pairs: apply the cross-skill-patterns empty-state template (must cite Step 2 pairs and verdicts).

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the STRUCTURAL AXIS DECLARATION, confirm whether it fired. Cite the actual report section and provide evidence (counts, template names, pair counts). Do not write "fired" without a section name and evidence.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "5 observations, 1 rejected at Rule 2: no blast radius estimable"] | fired / not fired |
| Filter Log Resolution block | [section name] | [e.g., "Template A: 4 elevated, 1 rejected" -- OR -- "Template B: zero rejections, recalibration invoked"] | fired / not fired |
| Empty-state templates | [list sections] | [e.g., "Tier 1 template: 'No findings at system-wide blast radius'; Tier 2 template: 'No findings at cross-skill blast radius'"] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [e.g., "2 candidate pairs listed in Step 1; 2 pairwise verdicts in Step 2: both independent"] | fired / not fired |

If a mechanism is marked "not fired," apply the compliance-checklist-not-fired template. A not-fired result is a disclosed compliance gap -- it does not fail the report silently.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration must be the first section. Structural Compliance Checklist must be the last section. Both are part of the output artifact -- they are not prompt text.

---

## V-05 -- Combined: Full Integration (Four Structural Axes)

**Variation axes combined:**
1. Filter Log Resolution (from R3 V-01) -- C-14: zero rejections trigger Template B recalibration notice
2. Active Negative Comparison Phase (from R3 V-02) -- C-15: comparison table required before pattern declaration
3. Universal Empty-State Protocol (from R2 V-03) -- C-11: all sections have named templates; silence is not acceptable
4. Pre-Finding Structural Axis Declaration (R4 V-01) -- C-17: the model writes a STRUCTURAL AXIS DECLARATION into the output before any findings; names four axes and their mechanisms
5. End-of-Report Structural Compliance Checklist (R4 V-02) -- C-18: the model writes a STRUCTURAL COMPLIANCE CHECKLIST at the end of the output; cites section names and evidence counts for each mechanism

**Hypothesis:** C-17 and C-18 both pass by construction. C-17: the declaration section names four structural axes and their mechanisms before findings, converting structural intent into a verifiable commitment. C-18: the compliance checklist requires citing actual sections and evidence, separating structural intent from structural execution. All prior R3 criteria carry forward: C-13 (filter log), C-14 (filter log resolution), C-15 (comparison protocol), C-11 (empty-state templates), C-16 (structural symmetry -- now visible from the four-axis declaration table). The compliance checklist also benefits C-12 (compounding elevation) and C-10 (blast radius rationale) by surfacing whether those mechanisms fired. Risk: this is the longest variation; the declaration and compliance sections add structural overhead. If the model abbreviates the evidence column in the compliance checklist, C-18 receives partial credit rather than full credit -- but the structure prevents silent failure.

---

Simulate the technical behavior of: {{topic}}

This report enforces four structural axes simultaneously. The first section of the output declares all four axes and their mechanisms. The last section verifies all four mechanisms fired with evidence citations. Both sections are part of the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections do not demonstrate filtering judgment -- only that the schema ran. Required: revisit candidate list. Either (a) name at least one observation that should be rejected under the filter rules, or (b) provide explicit justification that every candidate is genuinely anchored to a named spec location and scoped to at least one downstream component."
- **Findings table empty**: "No findings elevated. All candidates failed filter rules or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts from the Step 2 table]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation of why this area produced no observable candidates]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did not produce observable output in this report. Reason: [why the mechanism did not fire]. Impact on report validity: [whether the omission affects any findings]."

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

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report. This section is part of your output artifact -- not the prompt text. An evaluator reading only this section must be able to predict which structural sections appear in the report and what observable output each mechanism produces. Complete this before writing any execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block declaring Template A (normal: at least one rejection) or Template B (vacuous: zero rejections, recalibration required) | Candidate Observations and Filter Log table; Filter Log Resolution block with named template |
| Empty-state axis | C-11 | Per-section empty-state templates defined for all section types; silent empty sections are not permitted | Any structured section with no results: sub-skill sections, ranked tiers, comparison steps, execution log entries |
| Cross-skill comparison axis | C-15 | Three-step comparison protocol: candidate pairings (Step 1 table), pairwise verdicts (Step 2 table), pattern declaration (Step 3 -- requires Steps 1+2 to be present) | Cross-Skill Comparison Protocol: Step 1 table, Step 2 table, Step 3 declaration |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration section (before findings) + Structural Compliance Checklist section (after findings) with evidence citations | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |

Mechanisms declared in this table that do not produce observable output receive "not fired" in the compliance checklist. Do not declare mechanisms you do not use.

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

For top three ranked findings: state blast radius rationale (name downstream flows, components, or contracts affected and explain why scope reaches that far).

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

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**:

If compounding pairs found:

| P-ID | Root Cause | F-IDs | Blast Radius in Isolation | Elevated Blast Radius | Elevation Rationale |
|------|------------|-------|-------------------------|-----------------------|---------------------|

For each compounding finding: "Promoted from [tier] to [tier] because [cross-skill root cause means that X expands downstream scope from Y to Z]."

If no compounding pairs: apply the cross-skill-patterns empty-state template. The template requires citing every pair from Step 2 and their verdicts -- a bare declaration ("no compounding patterns detected") without citing Step 2 pairs fails C-15.

Steps 1 and 2 are required even when Step 3 concludes no patterns.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the STRUCTURAL AXIS DECLARATION, confirm whether it fired. Cite the actual report section by name and provide evidence (actual counts, template names, pair counts). Do not write "fired" without a section name and evidence drawn from the report you just produced.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "6 observations across 5 sub-skills; 2 rejected at Rule 1: no spec location; 1 rejected at Rule 3: style preference"] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template A: "N elevated, M rejected" -- cite the Template letter and rejection count] OR [Template B: "zero rejections, recalibration invoked -- cite the justification provided"] | fired / not fired |
| Empty-state templates | [list each section where a template fired] | [for each: cite the template type and first clause of the template text used] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [e.g., "3 candidate pairs in Step 1; 3 pairwise verdicts in Step 2: Pair 1 independent (distinct failure modes), Pair 2 compounding (shared root cause), Pair 3 independent (different spec areas)"] | fired / not fired |
| Structural Axis Declaration (this report's preamble) | Structural Axis Declaration | ["Four axes declared: filtering, empty-state, cross-skill comparison, declaration-compliance"] | fired / not fired |
| Structural Compliance Checklist (this section) | Structural Compliance Checklist | ["Present as final section; all mechanisms cited with section names and evidence"] | fired / not fired |

If a mechanism is marked "not fired," apply the compliance-checklist-not-fired template. A not-fired result is visible evidence of a structural gap -- it is always preferable to a mechanism that silently did not fire.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Structural Compliance Checklist is the last section. Both are written by the model into the output artifact -- they are not prompt text.

The four declared axes -- filtering, empty-state, cross-skill comparison, declaration-compliance -- must each produce observable output in the sections named in the declaration table. The compliance checklist is the report's self-attestation that they did.
