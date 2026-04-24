Written to `simulations/quest/variations/campaign-simulate-variations-R5-2026-03-16.md`.

---

## Round 5 Variations Summary

**Targets:** C-19 (domain vocabulary coherence), C-20 (observation-qualification threshold as named rule), C-21 (per-scope filter gate embedding)

---

### V-01 — Domain Vocabulary Genre Declaration Axis (single-axis, C-19)
Adds a **GENRE DECLARATION** table as the second output section (after the Structural Axis Declaration). Names one report genre (e.g., "technical inspection", "pre-implementation audit") and declares a vocabulary anchor set: finding label, scope label, source field label, impact field label, null-result phrase. All structural elements must use that vocabulary. The compliance checklist gains a 7th row requiring the model to cite one section header and one field label as evidence of genre coherence.

**Hypothesis:** C-19 passes by construction — genre is named, anchors are declared, and the checklist forces citation of actual structural examples. V-01 deliberately omits C-20 and C-21 to isolate the single axis.

---

### V-02 — Observation Qualification Threshold as Named Structural Rule Axis (single-axis, C-20)
Adds **THRESHOLD RULE T-1** as a named, standalone section before filtering. The rule states explicitly: an observation qualifies for elevation *if and only if* (a) spec location is named, (b) downstream impact is estimable, (c) no filter rule applies. The filter log gains a `T-1 Met?` column. Every elevation row must cite "T-1 met" or "T-1 not met: condition [a/b]." The compliance checklist gains a T-1 row requiring a concrete citation of one T-1 rejection.

**Hypothesis:** C-20 passes by construction — the rule is named, pre-declared, cited per-row, and verified in the checklist. The violation is detectable from the findings table alone (finding without spec location = T-1 violated), not inferred from output quality.

---

### V-03 — Per-Scope Filter Gate Embedding Axis (single-axis, C-21)
Replaces the centralized Candidate Observations and Filter Log table with **five per-scope embedded gates**, one inline within each sub-skill section: scope observation log → per-row elevation decisions → scope filter gate resolution (Template A or B). The compliance checklist must cite all five scope gates individually with counts. A centralized table with scope-attribution rows explicitly does not satisfy the criterion.

**Hypothesis:** C-21 passes by construction — each scope's filter gate is co-located with its evidence. Cross-scope filtering patterns become directly visible from the five gate resolution blocks in the execution log.

---

### V-04 — Combined: C-19 + C-20 + C-21 on R4 V-05 Base
Takes R4 V-05 (100/100) and adds all three new criteria. Genre declaration + T-1 + per-scope gates are co-located in a single **OBSERVATIONAL DISCIPLINE** section (second in the report). The structural axis declaration grows to 5 axes. Compliance checklist grows to 8 rows. The OBSERVATIONAL DISCIPLINE section is the single source of truth for genre vocabulary and T-1 before any sub-skill fires.

**Key architectural decision:** bundling genre + T-1 into one section keeps the report's structural preamble coherent — the model declares all observational constraints before executing any sub-skill.

---

### V-05 — Full Integration: Observational Discipline as Fifth Structural Axis (self-referential)
Extends V-04 by declaring C-19+C-20+C-21 as a single **observational discipline axis** in the 5-axis Structural Axis Declaration. The compliance checklist has 7 rows; **row 7** carries three-part evidence for the observational discipline axis: (1) genre named + structural examples cited, (2) T-1 cited with a rejection example, (3) all 5 per-scope gates present and not centralized.

**New pattern:** Row 7 accepts `fired / partial / not fired` where `partial` names which of the three mechanisms (genre, threshold, per-scope) produced insufficient evidence. This is the first variation in the series where a compliance checklist row has three independently-verifiable sub-claims — a partial row is more informative than a silent failure, and makes the weakest observational discipline mechanism immediately actionable.
iance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did not produce observable output. Reason: [why]. Impact on report validity: [whether omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked. Field labels must use vocabulary from the declared genre after the Genre Declaration section is written.

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

Write this section as the first section of your output report. An evaluator reading only this section must be able to predict which structural sections appear in the report and what observable output each mechanism produces. Complete this before writing any execution results.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Filter Log with four named rejection rules; Filter Log Resolution block declaring Template A (at least one rejection) or Template B (zero rejections, recalibration required) | Candidate Observations and Filter Log table; Filter Log Resolution block with named template |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types using genre vocabulary; silent sections not permitted | Any structured section with no results uses a named template |
| Cross-skill comparison axis | C-15 | Three-step protocol: candidate pairings (Step 1), pairwise verdicts (Step 2), pattern declaration (Step 3); Steps 1+2 required even when Step 3 finds no patterns | Cross-Skill Comparison Protocol: Step 1 table, Step 2 table, Step 3 declaration |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration (before findings) + Structural Compliance Checklist (after findings) with section citations and evidence counts | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |
| Vocabulary-coherence axis | C-19 | Genre Declaration table naming one report genre and its vocabulary anchors; all structural elements (section headers, field labels, empty-state phrasing, log entries) use vocabulary from that anchor set | Genre Declaration section (immediately after this section); every structural label in the report traces to the declared genre |

Mechanisms that do not fire receive "not fired" in the compliance checklist. Do not declare mechanisms you do not use.

---

**GENRE DECLARATION**

Write this section immediately after the Structural Axis Declaration, before any execution results. Name one report genre. List the vocabulary anchor set for that genre. Every section header, field label, empty-state template, and log entry in this report must use vocabulary from this anchor set.

| Element | Genre Vocabulary Anchor |
|---------|------------------------|
| Report genre | [one named genre: e.g., "technical inspection", "pre-implementation audit", "behavioral analysis", "failure-mode investigation"] |
| Finding label | [genre-consistent term for an elevated issue: e.g., "finding", "deficiency", "anomaly", "issue", "flag"] |
| Scope label | [genre-consistent term for a sub-skill execution unit: e.g., "sub-skill", "check", "module", "lens", "probe"] |
| Source field label | [genre-consistent label for the field naming which sub-skill discovered the issue: e.g., "Source sub-skill", "Originating check", "Discovery probe"] |
| Impact field label | [genre-consistent label for the standalone impact field: e.g., "Impact", "Consequence", "Downstream effect", "Failure mode"] |
| Null-result phrase | [genre-consistent phrasing for a section-level null result: e.g., "No [finding label] from [scope label]", "Check complete -- no [finding label] detected"] |

After declaring the genre, do not use vocabulary from any other genre in structural elements. Genre consistency applies to all structural elements -- section headers, field labels, empty-state templates, and log entries. Incidental prose transitions may use natural language; structural elements may not mix genres. An evaluator reading only section headers and field labels must be able to name this report's genre without reading any content.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, list candidate observations before filtering. Use genre vocabulary from the Genre Declaration for all structural labels.

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
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: A gate that rejects nothing provides no evidence of filtering judgment -- it demonstrates only that the schema ran. Required: revisit candidate list. Either (a) name at least one observation that should be rejected under the filter rules, or (b) justify that every candidate is genuinely anchored to a named spec location and scoped to at least one downstream component.

---

**FINDINGS TABLE**

Only observations that passed the filter. If none: apply the findings-table empty-state template. Use genre vocabulary declared in the Genre Declaration for field labels.

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

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills sharing surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**: If compounding pairs found, record with elevation rationale ("Promoted from [tier] to [tier] because [cross-skill root cause means that X expands downstream scope from Y to Z]"). If no compounding pairs: apply the cross-skill-patterns empty-state template -- must cite every Step 2 pair and verdict; a bare "no patterns" declaration without citing pairs fails C-15.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the Structural Axis Declaration, confirm whether it fired. Cite the actual report section by name and provide evidence drawn from the report you just produced. Do not write "fired" without a section name and evidence.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules) | [section name] | [e.g., "6 observations across 5 sub-skills; 2 rejected at Rule 1: no spec location; 1 rejected at Rule 3: style preference"] | fired / not fired |
| Filter Log Resolution block | [section name] | [Template A or B: cite template letter and counts] | fired / not fired |
| Empty-state templates | [list sections where a template fired] | [for each: template type and first clause used] | fired / not fired |
| Cross-skill comparison Steps 1+2 | [section name] | [N pairs in Step 1; N pairwise verdicts in Step 2] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [Five axes declared: filtering, empty-state, cross-skill comparison, declaration-compliance, vocabulary-coherence] | fired / not fired |
| Structural Compliance Checklist | Structural Compliance Checklist | [Present as final section; all mechanisms cited with section names and evidence] | fired / not fired |
| Genre Declaration and vocabulary coherence | Genre Declaration + all structural sections | [Genre named: "[genre name]"; structural elements verified: cite one section header and one field label as examples of genre vocabulary in use throughout the report] | fired / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Genre Declaration > Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Genre Declaration is the second section. Structural Compliance Checklist is the last section. All three are part of the output artifact -- not prompt text.

---

## V-02 -- Observation Qualification Threshold as Named Structural Rule Axis

**Variation axis:** Correctness -- the model is required to declare a named THRESHOLD RULE T-1 that states exactly what separates an observation from an elevated finding. The rule must be: (a) named (T-1) so it can be cited, (b) stated before filtering begins as a standalone section, (c) cited by name in the filter log for every elevation decision. This differs from the four rejection rules -- T-1 says what conditions must hold for elevation to proceed at all; the rejection rules say what rejects an otherwise eligible observation. The compliance checklist gains a T-1 row verifying the rule was cited in at least one elevation decision.

**Hypothesis:** C-20 passes by construction: T-1 is declared by name before filtering, cited in every elevation row, and verified in the compliance checklist -- making it falsifiable and verifiable independent of output quality. C-19 not targeted (no genre declaration). C-21 not targeted (centralized gate unchanged). All R4 V-05 mechanisms carry forward.

---

Simulate the technical behavior of: {{topic}}

This report enforces four structural axes simultaneously plus a named observation qualification threshold. The first section declares all axes and their mechanisms. The qualification threshold rule is declared before filtering begins and cited in every elevation decision. The last section verifies all mechanisms fired with evidence citations. All three sections are part of the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any section blank without its template.

- **Sub-skill no findings**: "No findings from [sub-skill]. Spec artifacts examined: [list]. No gaps or violations detected because [reason]."
- **Filter gate Template B (zero rejections)**: "Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: THRESHOLD RULE T-1 was applied to all [N] candidates; all passed. Required: verify that each passing candidate names a specific spec location and estimable impact, or identify at least one that should not have passed T-1."
- **Findings table empty**: "No findings elevated. All candidates failed THRESHOLD RULE T-1, failed filter rules, or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates evaluated. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did not produce observable output. Reason: [why]. Impact on report validity: [whether omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Fields with failure conditions marked.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference without named location violates THRESHOLD RULE T-1]
Summary:        [one sentence, problem only --
                 FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD: what breaks if unresolved --
                 FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14, C-20 | Filter Log with four named rejection rules plus THRESHOLD RULE T-1 (qualification threshold -- declared before filtering as a named rule); Filter Log Resolution declaring Template A or Template B | Threshold Rule T-1 section; Candidate Observations and Filter Log with T-1 citation column; Filter Log Resolution block |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections not permitted | Any structured section with no results uses a named template |
| Cross-skill comparison axis | C-15 | Three-step protocol: Steps 1+2 required even when Step 3 finds no patterns | Cross-Skill Comparison Protocol sections |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration (before findings) + Structural Compliance Checklist (after findings) with section citations and evidence counts | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |

---

**THRESHOLD RULE T-1**

Declare this rule before filtering begins. Every elevation decision in the filter log must cite this rule by name.

> **THRESHOLD RULE T-1 -- Observation Qualification Gate:**
> An observation qualifies for elevation to a finding if and only if ALL of the following are satisfied:
> (a) A specific spec location is named: a named section, boundary, or interface -- not "the spec" or "the design" generally
> (b) Downstream impact is estimable: at least one affected flow, component, or contract can be named
> (c) None of the four filter rejection rules apply
>
> An observation failing condition (a) or (b) is recorded in the filter log as "T-1 not met: condition [a/b]" with Elevate = no.
> An observation satisfying (a) and (b) but rejected by a filter rule is recorded as "T-1 met; rejected at Rule [N]: [reason]."
>
> This rule is falsifiable: a finding in the findings table without a named spec location is a T-1 violation detectable from the findings table alone, without evaluator judgment about output quality. Stating the rule here makes the violation detectable; implying the rule from clean output does not.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. After each, list candidate observations before filtering. THRESHOLD RULE T-1 is applied before the four filter rules.

1. flow-lifecycle    -- complete lifecycle trace with phase contracts and exception flows
2. flow-conversation -- multi-turn conversation simulation with dead-end and loop detection
3. trace-state       -- state transition hand-compilation with preconditions, postconditions, invariants
4. trace-contract    -- expected vs actual output comparison at contract boundaries
5. trace-permissions -- RBAC path trace with privilege escalation detection

---

**CANDIDATE OBSERVATIONS AND FILTER LOG**

For each sub-skill, list all observations (including weak ones). Apply THRESHOLD RULE T-1 first, then filter rules.

| Sub-Skill | Obs # | What was noticed | Spec Location | T-1 (a): loc named? | T-1 (b): impact estimable? | T-1 Met? | Filter Rule | Elevate? | Rejection Reason |
|-----------|-------|-----------------|---------------|--------------------|-----------------------------|----------|-------------|----------|-----------------|

**THRESHOLD RULE T-1** (declared above): conditions (a) and (b) must both be met before filter rules are applied.
- T-1 not met: record "T-1 not met: condition [a/b] -- [brief reason]." Elevate = no. Skip filter rules.
- T-1 met: apply filter rules. Record which rule applies if any.

**Filter rules** (apply only after T-1 is met):
1. No specific spec location can be named (T-1 primarily covers this; Rule 1 for marginal cases where T-1 passes but the reference is too vague to anchor a remediation)
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**FILTER LOG RESOLUTION**

After completing the filter log, declare the gate state.

**Template A (at least one rejection):**
> Filter gate applied. [N] observations evaluated. [M] rejected ([T-1 not met: N at condition a/b / Rule K: brief reason]). Gate operating normally -- filtering judgment demonstrated.

**Template B (zero rejections):**
> Filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: THRESHOLD RULE T-1 was applied to all [N] candidates; all passed conditions (a) and (b). All four filter rules were applied; none triggered. Required: either (a) identify at least one observation that should fail T-1 or a filter rule, or (b) confirm that the candidate set is genuinely minimal and justify why every observation is elevation-worthy.

---

**FINDINGS TABLE**

Only observations where T-1 was met and all filter rules passed. If none: apply the findings-table empty-state template.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Candidates | T-1 Rejected | Filter Rejected | Finding IDs |
|-----------|--------|------------|-------------|-----------------|-------------|
| flow-lifecycle | executed / no findings | | | | |
| flow-conversation | executed / no findings | | | | |
| trace-state | executed / no findings | | | | |
| trace-contract | executed / no findings | | | | |
| trace-permissions | executed / no findings | | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide** [or empty-state template]
**Tier 2 -- Cross-Skill** [or empty-state template]
**Tier 3 -- Component-Wide** [or empty-state template]
**Tier 4 -- Isolated** [or empty-state template]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Compounding findings with elevation rationale, or cross-skill-patterns empty-state template (must cite Step 2 pairs and verdicts -- a bare declaration fails C-15).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Filter Log (named rejection rules + T-1) | Candidate Observations and Filter Log | [N observations; M T-1 rejected at condition [a/b]; K filter rejected at Rule N; cite one example: "Obs [N] from [sub-skill]: T-1 not met -- no spec location"] | fired / not fired |
| Filter Log Resolution block | Filter Log Resolution | [Template A or B: cite template letter, total count, rejection count] | fired / not fired |
| THRESHOLD RULE T-1 (qualification threshold) | Threshold Rule T-1 + Filter Log | [T-1 declared before filtering; cited in filter log for [N] elevation decisions; [M] observations rejected at T-1; example: "Obs [N], [sub-skill], T-1 not met: [condition a/b]: [brief description]"] | fired / not fired |
| Empty-state templates | [list sections where a template fired] | [for each: template type and first clause used] | fired / not fired |
| Cross-skill comparison Steps 1+2 | Cross-Skill Comparison Protocol | [N pairs in Step 1; N pairwise verdicts in Step 2] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [Four axes declared: filtering+T-1, empty-state, cross-skill comparison, declaration-compliance] | fired / not fired |
| Structural Compliance Checklist | Structural Compliance Checklist | [Present as final section; all mechanisms cited with section names and evidence] | fired / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Threshold Rule T-1 > Candidate Observations and Filter Log > Filter Log Resolution > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

---

## V-03 -- Per-Scope Filter Gate Embedding Axis

**Variation axis:** Correctness -- each sub-skill section carries its own embedded filter gate (observation log + elevation decisions + gate resolution block) co-located with that sub-skill's evidence. No centralized filter table. The model applies filtering judgment locally at each scope boundary. Cross-scope filtering patterns become visible when the five per-scope gates can be compared directly. The compliance checklist verifies that all five per-scope filter gates fired.

**Hypothesis:** C-21 passes by construction: five per-scope gates are embedded, each co-located with its sub-skill's evidence. C-19 and C-20 not targeted. All R4 V-05 mechanisms carry forward; the centralized Candidate Observations and Filter Log table is replaced by five per-scope sections. The compliance checklist's filter-log row must cite all five scope gates. Risk: per-scope gates add length; the model may abbreviate later scopes. Partial credit on C-21 if at least 3 of 5 scopes have embedded gates; fail if only a centralized table exists with scope-attribution rows.

---

Simulate the technical behavior of: {{topic}}

This report enforces four structural axes simultaneously. The first section declares all axes and their mechanisms. Filtering is applied locally -- each sub-skill section carries its own embedded observation log and filter gate rather than deferring to a centralized table. The last section verifies all mechanisms fired. Both the declaration and the checklist are part of the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Do not omit any section; do not leave any section blank without its template.

- **Sub-skill no observations**: "No observations from [sub-skill]. Spec artifacts examined: [list]. Scope filter gate: no candidates to evaluate."
- **Per-scope filter gate Template B (zero rejections)**: "Scope filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: Zero rejections in this scope do not demonstrate filtering judgment. Required: either (a) name at least one observation that should be rejected, or (b) justify that all candidates name a specific spec location and estimable downstream impact."
- **Findings table empty**: "No findings elevated across all sub-skill scopes. All candidates failed their per-scope filter gates or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates in this scope. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did not produce observable output. Reason: [why]. Impact on report validity: [whether omission affects findings]."

---

**FINDING SCHEMA**

All fields required.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface]
Summary:        [one sentence, problem only -- FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD -- FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Remediation:    [REQUIRED HERE: specific action at named target]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis (per-scope) | C-13, C-14, C-21 | Per-scope embedded filter gate in each sub-skill section: observation log with elevation decisions + scope filter gate resolution block (Template A or B); filtering judgment is applied at each scope boundary, not deferred to a central table | Five per-scope filter gate sections, one embedded within each sub-skill execution section |
| Empty-state axis | C-11 | Per-section empty-state templates for all section types; silent sections not permitted | Any structured section with no results uses a named template |
| Cross-skill comparison axis | C-15 | Three-step protocol: Steps 1+2 required even when Step 3 finds no patterns | Cross-Skill Comparison Protocol sections |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration (before findings) + Structural Compliance Checklist (after findings) with section citations and evidence counts | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |

The per-scope filter gate replaces the centralized Candidate Observations and Filter Log table. Every sub-skill section must end with its own embedded filter gate before any findings from that scope are elevated. A centralized table with scope-attribution rows does not satisfy the per-scope embedding requirement.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. For each sub-skill: (1) execute the sub-skill, (2) list all observations in a per-scope observation log, (3) apply filter rules to each observation, (4) declare the scope gate state with Template A or B. Elevated findings carry forward to the Findings Table.

**Filter rules** (applied within each per-scope gate):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**SUB-SKILL 1: flow-lifecycle**

*Execute*: Complete lifecycle trace with phase contracts and exception flows.

*Scope Observation Log -- flow-lifecycle*:

| Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-lifecycle*:

[Template A: "Scope filter gate applied. [N] observations evaluated. [M] rejected (Rule [number]: [reason for each]). Gate operating normally." OR Template B: "Scope filter gate applied. [N] observations. Zero rejected. RECALIBRATION REQUIRED: ..."]

*Findings elevated from flow-lifecycle*: [Finding IDs, or "none -- no observations elevated from this scope"]

---

**SUB-SKILL 2: flow-conversation**

*Execute*: Multi-turn conversation simulation with dead-end and loop detection.

*Scope Observation Log -- flow-conversation*:

| Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-conversation*: [Template A or B with counts]

*Findings elevated from flow-conversation*: [IDs or "none"]

---

**SUB-SKILL 3: trace-state**

*Execute*: State transition hand-compilation with preconditions, postconditions, invariants.

*Scope Observation Log -- trace-state*:

| Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-state*: [Template A or B with counts]

*Findings elevated from trace-state*: [IDs or "none"]

---

**SUB-SKILL 4: trace-contract**

*Execute*: Expected vs actual output comparison at contract boundaries.

*Scope Observation Log -- trace-contract*:

| Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-contract*: [Template A or B with counts]

*Findings elevated from trace-contract*: [IDs or "none"]

---

**SUB-SKILL 5: trace-permissions**

*Execute*: RBAC path trace with privilege escalation detection.

*Scope Observation Log -- trace-permissions*:

| Obs # | What was noticed | Spec Location | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-permissions*: [Template A or B with counts]

*Findings elevated from trace-permissions*: [IDs or "none"]

---

**FINDINGS TABLE**

Only observations elevated through their per-scope filter gate. If none: apply the findings-table empty-state template.

| F-ID | Sub-Skill | Type | Spec Location | Summary | Impact | Blast Radius | Remediation |
|------|-----------|------|--------------|---------|--------|-------------|-------------|

---

**EXECUTION LOG**

| Sub-Skill | Status | Scope Gate State | Candidates | Rejected | Finding IDs |
|-----------|--------|-----------------|------------|---------|-------------|
| flow-lifecycle | executed | Template A / B | | | |
| flow-conversation | executed | Template A / B | | | |
| trace-state | executed | Template A / B | | | |
| trace-contract | executed | Template A / B | | | |
| trace-permissions | executed | Template A / B | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide** [or empty-state template]
**Tier 2 -- Cross-Skill** [or empty-state template]
**Tier 3 -- Component-Wide** [or empty-state template]
**Tier 4 -- Isolated** [or empty-state template]

For top three ranked findings: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Compounding findings with elevation rationale, or cross-skill-patterns empty-state template (must cite Step 2 pairs -- bare declaration fails C-15).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Per-scope filter gates (5 scopes) | Sub-Skill 1-5 scope filter gate sections | [Cite each scope individually: "flow-lifecycle: [N] obs, [M] rejected at Rule [K]"; repeat for all five scopes] | fired / not fired |
| Filter Gate Resolution (per scope) | Per sub-skill scope filter gate | [For each scope: "Template A" or "Template B -- recalibration invoked"; cite scope name and counts; example: "trace-state: Template A, 3 obs, 1 rejected at Rule 2"] | fired / not fired |
| Empty-state templates | [list sections where a template fired] | [template type and first clause for each] | fired / not fired |
| Cross-skill comparison Steps 1+2 | Cross-Skill Comparison Protocol | [N pairs in Step 1; N verdicts in Step 2] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [Four axes declared: filtering (per-scope), empty-state, cross-skill comparison, declaration-compliance] | fired / not fired |
| Structural Compliance Checklist | Structural Compliance Checklist | [Present as final section; all mechanisms cited] | fired / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > [Sub-Skill 1-5 each containing: scope observation log, scope filter gate with Template A or B, elevated findings list] > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

The per-scope filter gate is embedded within each sub-skill section -- not deferred to a centralized table. The Structural Compliance Checklist must cite all five scope gates individually with counts. A centralized table listing scopes as rows does not satisfy C-21 -- the gate evidence must be co-located with each scope's observation data.

---

## V-04 -- Combined: C-19 + C-20 + C-21 on R4 V-05 Base

**Variation axes combined:**
1. Domain Vocabulary Genre Declaration (R5 V-01) -- C-19: Genre Declaration section naming one genre with vocabulary anchors; all structural elements use that vocabulary; compliance checklist verifies with examples
2. Observation Qualification Threshold as Named Rule (R5 V-02) -- C-20: THRESHOLD RULE T-1 declared before filtering, cited in every per-scope gate, verified in compliance checklist
3. Per-Scope Filter Gate Embedding (R5 V-03) -- C-21: each sub-skill section carries its own embedded observation log and filter gate; no centralized table
4. Pre-Finding Structural Axis Declaration (R4 V-05) -- C-17: Structural Axis Declaration as first output section
5. End-of-Report Structural Compliance Checklist (R4 V-05) -- C-18: compliance checklist as final section with evidence citations

**Hypothesis:** C-19 passes via Genre Declaration and vocabulary-coherence axis. C-20 passes via THRESHOLD RULE T-1 (named, cited per elevation, verified in checklist). C-21 passes via per-scope filter gates replacing the centralized table. C-17 and C-18 carry from R4 V-05. Compliance checklist grows to 8 rows. Risk: genre coherence must be maintained across all five per-scope observation log sections using consistent vocabulary anchors; the model must cite T-1 in each scope gate. If vocabulary drifts after the first two scopes, C-19 receives partial credit.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all axes. The second section declares the report genre, vocabulary anchors, and the named qualification threshold rule. Filtering is applied per-scope with T-1 cited in each gate. The last section verifies all mechanisms fired. All three sections are part of the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Templates must use vocabulary from the declared genre.

- **Sub-skill no observations**: "No observations from [sub-skill]. Spec artifacts examined: [list]. Scope filter gate: no candidates to evaluate."
- **Per-scope filter gate Template B (zero rejections)**: "Scope filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: THRESHOLD RULE T-1 applied to all [N] candidates; all satisfied conditions (a) and (b). Verify each candidate names a specific spec location and estimable impact."
- **Findings table empty**: "No findings elevated. All candidates failed THRESHOLD RULE T-1, failed filter rules, or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates in this scope. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared but did not produce observable output. Reason: [why]. Impact: [whether omission affects findings]."

---

**FINDING SCHEMA**

All fields required. Field labels must use genre vocabulary after the Observational Discipline section is declared.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface -- FAILURE violates T-1]
Summary:        [one sentence, problem only -- FAILURE: merging Impact into Summary fails C-06]
Impact:         [STANDALONE FIELD -- FAILURE: blank or merged with Summary fails C-06]
Blast radius:   [isolated / component-wide / cross-skill / system-wide]
BR rationale:   [REQUIRED for cross-skill or system-wide]
Remediation:    [REQUIRED HERE: specific action -- FAILURE: "fix the spec" fails C-08]
```

---

**STRUCTURAL AXIS DECLARATION**

Write this section as the first section of your output report.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis (per-scope + threshold) | C-13, C-14, C-20, C-21 | THRESHOLD RULE T-1 (qualification threshold, declared in Observational Discipline section before filtering); per-scope embedded filter gate in each sub-skill section with T-1 citation, four rejection rules, and scope gate resolution (Template A or B) | Threshold Rule T-1 in Observational Discipline section; five per-scope observation logs and embedded filter gates in sub-skill sections; Execution Log scope gate summary |
| Empty-state axis | C-11 | Per-section empty-state templates using genre vocabulary; silent sections not permitted | Any structured section with no results uses a named template |
| Cross-skill comparison axis | C-15 | Three-step protocol: Steps 1+2 required even when Step 3 finds no patterns | Cross-Skill Comparison Protocol sections |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration (before findings) + Structural Compliance Checklist (after findings) with section citations and evidence | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |
| Vocabulary-coherence axis | C-19 | Genre Declaration in Observational Discipline section naming one report genre with vocabulary anchors; all structural elements (section headers, field labels, empty-state text, log entries) use genre vocabulary | Observational Discipline > Genre Declaration; all structural labels trace to declared genre; compliance checklist row cites header and field label examples |

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration, before any execution results. This section declares both the genre vocabulary and the qualification threshold rule.

**Genre Declaration**:

| Element | Genre Vocabulary Anchor |
|---------|------------------------|
| Report genre | [one named genre: e.g., "technical inspection", "pre-implementation audit", "behavioral analysis", "failure-mode investigation"] |
| Finding label | [genre-consistent term: e.g., "finding", "deficiency", "anomaly", "issue", "flag"] |
| Scope label | [genre-consistent term: e.g., "sub-skill", "check", "module", "lens", "probe"] |
| Source field label | [e.g., "Source sub-skill", "Originating check", "Discovery probe"] |
| Impact field label | [e.g., "Impact", "Consequence", "Downstream effect", "Failure mode"] |
| Null-result phrase | [e.g., "No [finding label] from [scope label]", "Check complete -- no [finding label] detected"] |

After declaring the genre: all section headers, field labels, empty-state templates, and log entries must use this vocabulary. Incidental prose may use natural language; structural elements may not mix genres.

**THRESHOLD RULE T-1 -- Observation Qualification Gate:**

> An observation qualifies for elevation to a finding if and only if ALL of the following are satisfied:
> (a) A specific spec location is named (named section, boundary, or interface -- not "the spec" generally)
> (b) Downstream impact is estimable (at least one affected flow, component, or contract named)
> (c) None of the four filter rejection rules apply
>
> An observation failing (a) or (b): record in the per-scope filter log as "T-1 not met: condition [a/b] -- [reason]." Elevate = no.
> The rule is falsifiable: a finding without a named spec location violates T-1 and is detectable from the findings table alone.
> T-1 must be cited by name in every per-scope filter gate elevation decision.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. For each: (1) list observations using genre vocabulary, (2) apply T-1 and filter rules, (3) declare scope gate state (Template A or B) as the final element of that sub-skill section.

**Filter rules** (applied after T-1 is met):
1. No specific spec location can be named
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**SUB-SKILL 1: flow-lifecycle**

*Execute*: Complete lifecycle trace with phase contracts and exception flows.

*Scope Observation Log -- flow-lifecycle* [use declared scope label]:

| Obs # | What was noticed | Spec Location | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-lifecycle* [cite T-1 results and filter rules]:

[Template A: "Scope filter gate applied. [N] observations. [M] rejected (T-1 not met: [N] at condition [a/b]; Rule [K]: [reason]). Gate operating normally." OR Template B with T-1 recalibration notice.]

*[Finding label] elevated from this scope*: [IDs using declared finding label, or declared null-result phrase]

---

**SUB-SKILL 2: flow-conversation**

*Execute*: Multi-turn conversation simulation with dead-end and loop detection.

*Scope Observation Log -- flow-conversation*:

| Obs # | What was noticed | Spec Location | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-conversation*: [Template A or B with T-1 citation]

*[Finding label] elevated from this scope*: [IDs or null-result phrase]

---

**SUB-SKILL 3: trace-state**

*Execute*: State transition hand-compilation with preconditions, postconditions, invariants.

*Scope Observation Log -- trace-state*:

| Obs # | What was noticed | Spec Location | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-state*: [Template A or B]

*[Finding label] elevated from this scope*: [IDs or null-result phrase]

---

**SUB-SKILL 4: trace-contract**

*Execute*: Expected vs actual output comparison at contract boundaries.

*Scope Observation Log -- trace-contract*:

| Obs # | What was noticed | Spec Location | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-contract*: [Template A or B]

*[Finding label] elevated from this scope*: [IDs or null-result phrase]

---

**SUB-SKILL 5: trace-permissions**

*Execute*: RBAC path trace with privilege escalation detection.

*Scope Observation Log -- trace-permissions*:

| Obs # | What was noticed | Spec Location | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-permissions*: [Template A or B]

*[Finding label] elevated from this scope*: [IDs or null-result phrase]

---

**FINDINGS TABLE**

Only observations elevated through their per-scope filter gate. Use genre vocabulary for field labels.

| F-ID | [Source field label] | Type | Spec Location | Summary | [Impact field label] | Blast Radius | Remediation |
|------|---------------------|------|--------------|---------|---------------------|-------------|-------------|

---

**EXECUTION LOG**

| [Scope label] | Status | Scope Gate | Candidates | T-1 Rejected | Filter Rejected | [Finding label] IDs |
|---------------|--------|-----------|------------|-------------|-----------------|---------------------|
| flow-lifecycle | executed | A/B | | | | |
| flow-conversation | executed | A/B | | | | |
| trace-state | executed | A/B | | | | |
| trace-contract | executed | A/B | | | | |
| trace-permissions | executed | A/B | | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide** [or empty-state template]
**Tier 2 -- Cross-Skill** [or empty-state template]
**Tier 3 -- Component-Wide** [or empty-state template]
**Tier 4 -- Isolated** [or empty-state template]

For top three: state blast radius rationale.

---

**CROSS-SKILL COMPARISON PROTOCOL**

**Step 1 -- Candidate pairings**:

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

**Step 3 -- Patterns declaration**: Compounding findings with elevation rationale, or cross-skill-patterns empty-state template (must cite Step 2 pairs -- bare declaration fails C-15).

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Per-scope filter gates (5 scopes) | Sub-Skill 1-5 scope filter gate sections | [Cite each scope: "[scope]: N obs, M T-1 rejected (condition [a/b]), K filter rejected (Rule [N])"; repeat for all 5] | fired / not fired |
| Filter Gate Resolution (per scope) | Per sub-skill scope | [Each scope: Template A or B; cite scope name, template letter, and counts] | fired / not fired |
| THRESHOLD RULE T-1 (qualification threshold) | Observational Discipline + per-scope gates | [T-1 declared in Observational Discipline; cited in gates for all 5 scopes; cite one T-1 rejection example: "[scope] Obs [N]: T-1 not met, condition [a/b]: [reason]"] | fired / not fired |
| Empty-state templates | [list sections] | [template type and first clause for each section] | fired / not fired |
| Cross-skill comparison Steps 1+2 | Cross-Skill Comparison Protocol | [N pairs in Step 1; N verdicts in Step 2] | fired / not fired |
| Genre Declaration and vocabulary coherence | Observational Discipline > Genre Declaration + all structural sections | [Genre named: "[genre]"; cite one section header and one field label as genre vocabulary examples from the report] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [Five axes declared: filtering+threshold+per-scope, empty-state, cross-skill comparison, declaration-compliance, vocabulary-coherence] | fired / not fired |
| Structural Compliance Checklist | Structural Compliance Checklist | [Present as final section; all 8 mechanisms cited with section names and evidence] | fired / not fired |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline (Genre Declaration + Threshold Rule T-1) > [Sub-Skill 1-5 each with scope observation log and embedded scope filter gate] > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

---

## V-05 -- Full Integration: Observational Discipline as a Fifth Structural Axis

**Variation axes combined:**
1. Filter Log Resolution (R3 V-01) -- C-14
2. Active Negative Comparison (R3 V-02) -- C-15
3. Universal Empty-State Protocol (R2 V-03) -- C-11
4. Pre-Finding Structural Axis Declaration (R4 V-01) -- C-17
5. End-of-Report Structural Compliance Checklist (R4 V-02) -- C-18
6. Observational Discipline Axis (R5, new) -- C-19 + C-20 + C-21 bundled as the fifth declared structural axis: (a) genre vocabulary coherence via Genre Declaration, (b) named qualification threshold rule via THRESHOLD RULE T-1, (c) per-scope filter gate embedding

**Hypothesis:** C-17 and C-18 pass by construction (carry from R4 V-05). C-19 passes by construction: genre is named and declared as the vocabulary-coherence mechanism of the fifth axis; compliance checklist attests with structural examples. C-20 passes by construction: T-1 is declared as the qualification-threshold mechanism of the fifth axis; compliance checklist verifies it was cited in elevation decisions. C-21 passes by construction: per-scope filter gates are declared as the per-scope-embedding mechanism of the fifth axis; compliance checklist requires citing all five scope gates. The compliance checklist has 7 rows; row 5 attests to all five declared axes (including the observational discipline axis); row 6 attests to the checklist's own presence; row 7 attests to the observational discipline axis with three-part evidence (genre, T-1, per-scope gates). The structural verification system verifies all three new criteria as a named unit. Risk: bundling C-19+C-20+C-21 requires row 7 in the compliance checklist to carry three distinct evidence claims; partial evidence on any one produces a partial row rather than a full-pass row.

---

Simulate the technical behavior of: {{topic}}

This report enforces five structural axes simultaneously. The first section declares all five axes and their mechanisms. The fifth axis -- observational discipline -- bundles three mechanisms: genre vocabulary coherence via a Genre Declaration, a named qualification threshold rule via THRESHOLD RULE T-1, and per-scope filter gate embedding (each sub-skill carries its own gate co-located with its evidence). The last section verifies all five axes fired with evidence for each. All three sections are part of the output artifact -- not the prompt text you are reading.

---

**EMPTY-STATE TEMPLATES**

Use these templates when a section has no content. Templates must use genre vocabulary declared in the Observational Discipline section. Do not omit any section; do not leave any section blank without its template.

- **Sub-skill no observations**: "No observations from [sub-skill]. Spec artifacts examined: [list]. Scope filter gate: no candidates to evaluate."
- **Per-scope filter gate Template B (zero rejections)**: "Scope filter gate applied. [N] observations evaluated. Zero rejected. RECALIBRATION REQUIRED: THRESHOLD RULE T-1 applied to all [N] candidates; all passed conditions (a) and (b). Verify each candidate names a specific spec location and estimable downstream impact -- or identify at least one that should not have passed T-1."
- **Findings table empty**: "No findings elevated. All candidates failed THRESHOLD RULE T-1, failed filter rules, or no problems were detected."
- **Ranked tier empty**: "No findings at [tier name] blast radius."
- **Comparison step with no pairs**: "No findings from multiple sub-skills available for pairwise comparison. Cross-skill comparison cannot proceed."
- **Cross-skill patterns empty**: "No compounding patterns detected. Candidate pairs compared in Step 2: [list pairs and verdicts from Step 2 table]. Each describes a distinct root cause."
- **Execution log zero candidates**: "Zero candidates in this scope. Reason: [explanation]."
- **Compliance checklist not fired**: "Mechanism declared in Structural Axis Declaration but did not produce observable output. Reason: [why]. Impact on report validity: [whether omission affects any findings]."

---

**FINDING SCHEMA**

All fields required. Field labels must use vocabulary from the declared genre. Failure conditions for schema violations are stated as structural rules that checklist row 7 can verify.

```
F-ID:           [sequential: F-01, F-02, ...]
Sub-skill:      [flow-lifecycle / flow-conversation / trace-state / trace-contract / trace-permissions]
Type:           [spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap]
Spec location:  [REQUIRED: named section, boundary, or interface --
                 FAILURE: vague reference violates THRESHOLD RULE T-1 condition (a)]
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

Write this section as the first section of your output report. An evaluator reading only this section must be able to predict which structural sections appear, what mechanism implements each axis, and where each mechanism fires.

| Axis | Criteria | Mechanism | Observable Output in This Report |
|------|----------|-----------|----------------------------------|
| Filtering axis | C-13, C-14 | Per-scope filter gate resolution (Template A or B) embedded in each sub-skill section; declared as part of Observational Discipline axis below -- listed here to note that C-14 (vacuous-filter acknowledgment) fires within each per-scope gate | Five per-scope scope filter gate resolution blocks (one per sub-skill section) |
| Empty-state axis | C-11 | Per-section empty-state templates using genre vocabulary for all section types; silent sections not permitted | Any structured section with no results uses a named genre-coherent template |
| Cross-skill comparison axis | C-15 | Three-step protocol: Step 1 candidate pairings, Step 2 pairwise verdicts, Step 3 patterns declaration; Step 3 requires Steps 1+2 to be present; bare "no patterns" without Step 2 citations fails C-15 | Cross-Skill Comparison Protocol: Step 1 table, Step 2 table, Step 3 declaration |
| Declaration-compliance axis | C-17, C-18 | This Structural Axis Declaration section (before findings, naming all five axes and their mechanisms); Structural Compliance Checklist section (final section) with 7 rows and evidence citations | Structural Axis Declaration (this section); Structural Compliance Checklist (final section) |
| Observational discipline axis | C-19, C-20, C-21 | Three bundled mechanisms -- (1) Genre Declaration: one named genre with vocabulary anchors; all structural elements use that vocabulary; (2) THRESHOLD RULE T-1: named, falsifiable qualification rule cited in every per-scope filter gate; (3) Per-scope filter gate embedding: each sub-skill section carries its own observation log and filter gate co-located with its evidence, not deferred to a centralized table | Observational Discipline section (Genre Declaration + Threshold Rule T-1); five per-scope observation logs and embedded filter gates in sub-skill execution sections |

The fifth axis -- observational discipline -- bundles three mechanisms whose evidence appears in three distinct locations: the Observational Discipline section (genre + T-1 declaration), the sub-skill execution sections (per-scope gates), and the structural compliance checklist row 7 (three-part attestation). A partial row 7 identifies which mechanism is the weakest link.

---

**OBSERVATIONAL DISCIPLINE**

Write this section immediately after the Structural Axis Declaration. Declare both the report genre and the qualification threshold rule. These are the first two mechanisms of the observational discipline axis.

**Genre Declaration**:

| Element | Declared Value |
|---------|----------------|
| Report genre | [one named genre] |
| Finding label | [genre-consistent term for an elevated issue] |
| Scope label | [genre-consistent term for a sub-skill execution unit] |
| Source field label | [genre-consistent label for the discovering sub-skill field] |
| Impact field label | [genre-consistent label for the standalone impact field] |
| Null-result phrase | [genre-consistent phrasing for a section-level no-result] |

After declaring the genre: all section headers, field labels, empty-state templates, and log entries must use this vocabulary. Incidental prose may use natural language; structural elements may not mix genres. An evaluator reading only headers and field labels must be able to name the genre without reading content.

**THRESHOLD RULE T-1 -- Observation Qualification Gate:**

> An observation qualifies for elevation to a finding if and only if ALL of the following are satisfied:
> (a) A specific spec location is named (named section, boundary, or interface -- not "the spec" generally)
> (b) Downstream impact is estimable (at least one affected flow, component, or contract named)
> (c) None of the four filter rejection rules apply
>
> An observation failing (a) or (b): recorded in the per-scope filter log as "T-1 not met: condition [a/b] -- [reason]." Elevate = no. Filter rules are not applied.
> An observation satisfying (a) and (b) but rejected by a filter rule: recorded as "T-1 met; rejected at Rule [N]: [reason]."
> A finding in the findings table without a named spec location is a T-1 violation -- detectable from the table alone, without evaluator judgment about output quality.
> T-1 must be cited by name ("T-1 met" or "T-1 not met: condition [a/b]") in every per-scope filter gate elevation row.

---

**EXECUTION SEQUENCE**

Run each sub-skill in order. For each: (1) execute the sub-skill, (2) list all observations in the per-scope observation log using genre vocabulary, (3) apply T-1 then filter rules, (4) declare the scope gate state with Template A or B. Elevated findings carry forward to the Findings Table.

**Filter rules** (applied after T-1 is met):
1. No specific spec location can be named (T-1 covers the primary case; Rule 1 for marginal cases where T-1 passes but the reference is too vague to anchor a remediation)
2. No blast radius can be estimated
3. Style preference, not correctness or coverage gap
4. Duplicates a higher-blast finding already captured

---

**SUB-SKILL 1: flow-lifecycle**

*Execute*: Complete lifecycle trace with phase contracts and exception flows.

*Scope Observation Log -- flow-lifecycle* [use declared scope label]:

| Obs # | What was noticed | Spec Location | T-1 (a) | T-1 (b) | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|---------|---------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-lifecycle*:
[Template A: "Scope filter gate applied. [N] observations. [M] rejected: [T-1 not met: [N] at condition [a/b] -- [brief reason]; Rule [K]: [reason]]. Gate operating normally -- filtering judgment demonstrated."
OR Template B: "Scope filter gate applied. [N] observations. Zero rejected. RECALIBRATION REQUIRED: T-1 applied to all [N] candidates; all passed (a) and (b). All filter rules applied; none triggered. Required: identify at least one observation that should fail T-1 or a filter rule, or justify the minimal candidate set."]

*[Finding label] elevated from flow-lifecycle*: [IDs using declared finding label, or declared null-result phrase]

---

**SUB-SKILL 2: flow-conversation**

*Execute*: Multi-turn conversation simulation with dead-end and loop detection.

*Scope Observation Log -- flow-conversation*:

| Obs # | What was noticed | Spec Location | T-1 (a) | T-1 (b) | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|---------|---------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- flow-conversation*: [Template A or B with T-1 citation and counts]

*[Finding label] elevated from flow-conversation*: [IDs or null-result phrase]

---

**SUB-SKILL 3: trace-state**

*Execute*: State transition hand-compilation with preconditions, postconditions, invariants.

*Scope Observation Log -- trace-state*:

| Obs # | What was noticed | Spec Location | T-1 (a) | T-1 (b) | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|---------|---------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-state*: [Template A or B]

*[Finding label] elevated from trace-state*: [IDs or null-result phrase]

---

**SUB-SKILL 4: trace-contract**

*Execute*: Expected vs actual output comparison at contract boundaries.

*Scope Observation Log -- trace-contract*:

| Obs # | What was noticed | Spec Location | T-1 (a) | T-1 (b) | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|---------|---------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-contract*: [Template A or B]

*[Finding label] elevated from trace-contract*: [IDs or null-result phrase]

---

**SUB-SKILL 5: trace-permissions**

*Execute*: RBAC path trace with privilege escalation detection.

*Scope Observation Log -- trace-permissions*:

| Obs # | What was noticed | Spec Location | T-1 (a) | T-1 (b) | T-1 Met? | Blast Radius | Elevate? | Rejection Reason |
|-------|-----------------|---------------|---------|---------|----------|-------------|----------|-----------------|

*Scope Filter Gate -- trace-permissions*: [Template A or B]

*[Finding label] elevated from trace-permissions*: [IDs or null-result phrase]

---

**FINDINGS TABLE**

Only observations elevated through their per-scope filter gate. If none: apply the findings-table empty-state template. Field labels must use genre vocabulary from the Genre Declaration.

| F-ID | [Source field label] | Type | Spec Location | Summary | [Impact field label] | Blast Radius | Remediation |
|------|---------------------|------|--------------|---------|---------------------|-------------|-------------|

---

**EXECUTION LOG**

| [Scope label] | Status | Scope Gate | Candidates | T-1 Rejected | Filter Rejected | [Finding label] IDs |
|---------------|--------|-----------|------------|-------------|-----------------|---------------------|
| flow-lifecycle | executed | Template A/B | | | | |
| flow-conversation | executed | Template A/B | | | | |
| trace-state | executed | Template A/B | | | | |
| trace-contract | executed | Template A/B | | | | |
| trace-permissions | executed | Template A/B | | | | |

---

**RANKED FINDINGS**

Sort by blast radius: system-wide > cross-skill > component-wide > isolated.

**Tier 1 -- System-Wide** [or empty-state template]
**Tier 2 -- Cross-Skill** [or empty-state template]
**Tier 3 -- Component-Wide** [or empty-state template]
**Tier 4 -- Isolated** [or empty-state template]

For top three ranked findings: state blast radius rationale (name downstream flows, components, or contracts affected and explain why scope reaches that far).

---

**CROSS-SKILL COMPARISON PROTOCOL**

Complete all three steps. Step 3 requires Steps 1 and 2 to be present.

**Step 1 -- Candidate pairings**: List every pair of findings from different sub-skills sharing surface similarity.

| Pair # | F-ID A | F-ID B | Surface similarity |
|--------|--------|--------|-------------------|

**Step 2 -- Pairwise comparison**:

| Pair # | F-ID A | F-ID B | Verdict | Reason |
|--------|--------|--------|---------|--------|

A pair is compounding only if fixing the root cause of one also resolves the other.

**Step 3 -- Patterns declaration**: If compounding pairs found, record each ("Promoted from [tier] to [tier] because [cross-skill root cause means that X expands downstream scope from Y to Z]"). If no compounding pairs: apply the cross-skill-patterns empty-state template -- must cite every Step 2 pair and verdict; a bare "no compounding patterns detected" without Step 2 citations fails C-15.

---

**STRUCTURAL COMPLIANCE CHECKLIST**

Write this section as the final section of your output report. For each mechanism declared in the Structural Axis Declaration, confirm whether it fired. Cite the actual report section by name and provide evidence drawn from the report you just produced. Do not write "fired" without a section name and evidence.

| Mechanism | Report Section | Evidence | Status |
|-----------|---------------|---------|--------|
| Per-scope filter gates (5 scopes) | Sub-Skill 1-5 scope filter gate sections | [Cite each scope individually: "flow-lifecycle: [N] obs, [M] T-1 rejected (condition [a/b]), [K] filter rejected (Rule [N])"; repeat for all five scopes] | fired / not fired |
| Filter Gate Resolution per scope | Per sub-skill scope | [Each scope: "Template A" or "Template B -- recalibration invoked"; cite scope name, template letter, and counts; example: "trace-state: Template A, 3 obs, 1 rejected at Rule 2: no blast radius estimable"] | fired / not fired |
| Empty-state templates | [list each section where a template fired] | [For each: template type and first clause of template text used; example: "Ranked Findings Tier 3: null-result phrase applied -- '[first clause]'"] | fired / not fired |
| Cross-skill comparison Steps 1+2 | Cross-Skill Comparison Protocol | [N pairs in Step 1; N pairwise verdicts in Step 2; cite one example pair verdict: "Pair [N]: F-[A] and F-[B] -- [compounding / independent]: [brief reason]"] | fired / not fired |
| Structural Axis Declaration | Structural Axis Declaration | [Five axes declared: filtering, empty-state, cross-skill comparison, declaration-compliance, observational discipline (C-19+C-20+C-21)] | fired / not fired |
| Structural Compliance Checklist | Structural Compliance Checklist | [Present as final section; all seven mechanisms cited with section names and evidence] | fired / not fired |
| Observational discipline axis (C-19 + C-20 + C-21) | Observational Discipline + Sub-Skill 1-5 scope gates | [Three-part evidence -- C-19: genre named "[genre]"; cite one section header and one field label as genre vocabulary examples; C-20: T-1 declared in Observational Discipline; cited in all 5 scope gates; cite one T-1 rejection example: "[scope] Obs [N]: T-1 not met condition [a/b]: [reason]"; C-21: 5 per-scope filter gates embedded in Sub-Skill 1-5 sections, not in a centralized table] | fired / partial / not fired |

Row 5 attests to the Declaration's five axes including the observational discipline axis. Row 7 is the three-part attestation for C-19, C-20, and C-21. A "partial" in row 7 identifies which mechanism (genre coherence, threshold rule, or per-scope gates) produced insufficient evidence -- making the weakest link in the observational discipline axis visible without requiring the evaluator to re-read all findings.

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Structural Axis Declaration > Observational Discipline (Genre Declaration + Threshold Rule T-1) > [Sub-Skill 1-5 each containing: scope observation log with T-1 column, scope filter gate with Template A or B, elevated findings list] > Findings Table > Execution Log > Ranked Findings > Cross-Skill Comparison Protocol (Steps 1, 2, 3) > Structural Compliance Checklist.

Structural Axis Declaration is the first section. Observational Discipline is the second section. Structural Compliance Checklist is the last section. All three are written by the model into the output artifact -- they are not prompt text.

The five declared axes must each produce observable output in the sections named in the declaration table. The compliance checklist's row 7 is the report's self-attestation that the observational discipline axis fired across all three mechanisms. A partial row 7 is always preferable to a silent omission -- it makes the weakest observational discipline mechanism visible and actionable.
