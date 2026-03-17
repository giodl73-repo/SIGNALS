Now I have the context I need. Let me generate the R7 variations. The rubric v6 adds C-26/C-27/C-28 and R6 V-04/V-05 already satisfy all three. R7 should explore new axes that could surface excellence patterns beyond the current rubric ceiling.

**R7 new axes:**
- **Axis A**: Cross-Skill Dependency Map -- explicit entity-sharing map before execution; findings in one sub-skill trigger re-examination in linked sub-skills
- **Axis B**: Finding Confidence Scoring -- each finding rated HIGH/MEDIUM/LOW based on spec evidence strength; equal blast-radius = higher confidence ranks first
- **Axis C**: Spec Gap Classification -- findings typed at detection as GAP / CONTRADICTION / ASSUMPTION; type constrains remediation Verb (extends C-26)

---

# campaign-simulate -- Round 7 Variations

Round 6 V-04 and V-05 achieve 100/100 on rubric v6. Round 7 explores three new axes. The goal is to test whether any axis produces output quality not captured by the current rubric -- and if so, to characterize the pattern precisely enough to define a new criterion.

**New axes this round:**

- **Axis A: Cross-Skill Dependency Map** -- R6 gold runs five sub-skills as five independent passes against the same entity set. Axis A adds a DEPENDENCY MAP phase before execution: for each pair of sub-skills, list shared entities and declare propagation rules (finding in flow-lifecycle touching entity X triggers re-examination of X in trace-state). The map converts the execution model from 5 independent sweeps to a coordinated cascade, where findings in one sub-skill can open or close examination paths in subsequent ones.

- **Axis B: Finding Confidence Scoring** -- R6 gold ranks findings by blast radius but treats all findings of equal blast-radius as equivalent. Axis B adds a CONFIDENCE column to every finding row: HIGH (spec text explicitly describes the behavior and contradicts it), MEDIUM (spec is silent; behavior inferred from surrounding context), LOW (behavior assumed from general convention). Confidence is the tiebreaker for equal blast-radius rows. A LOW-confidence HIGH-blast finding is surfaced differently from a HIGH-confidence HIGH-blast finding.

- **Axis C: Spec Gap Classification** -- R6 gold produces findings with Verb/Target/Location remediation entries (C-26). Axis C types each finding at detection time: GAP (spec is silent on this behavior), CONTRADICTION (spec states X, simulation shows Y), ASSUMPTION (behavior inferred; not stated). The type constrains the remediation Verb: GAP -> add, CONTRADICTION -> resolve or remove, ASSUMPTION -> confirm. A checklist of "add permission check" is already non-falsifiable; an ASSUMPTION-typed finding that requires a "confirm" verb forces a spec consultation rather than a code change.

---

## V-01 -- Axis A (Cross-Skill Dependency Map)

**Hypothesis**: Adding a dependency map before execution will cause findings to propagate across sub-skill boundaries, producing cross-linked findings that single-pass execution misses. The map may also surface an additional rubric criterion: cross-link coverage (was every triggered re-examination actually completed?).

---

Simulate the technical behavior of: {{topic}}

You are running a coordinated simulation campaign. Five sub-skills execute in sequence. Before they run, you will build a dependency map that governs how findings propagate across sub-skills.

---

**PHASE 0 -- TOPIC ENTITY MANIFEST**

Read all spec and design artifacts for {{topic}}. Extract five entity lists:

- **State entities** (state machines, status fields, lifecycle phases)
- **Contract entities** (API surfaces, input/output schemas, event payloads)
- **Permission entities** (roles, claims, permission checks, access paths)
- **Lifecycle entities** (document types, workflow stages, phase transitions)
- **Conversation entities** (intents, dialog nodes, branching conditions)

Emit the manifest as five labeled bullet lists before proceeding.

---

**PHASE 1 -- CROSS-SKILL DEPENDENCY MAP**

For each pair of sub-skills that share entities from the manifest, declare:

1. Which entities are shared
2. Propagation rule: if a finding touches entity X in sub-skill A, re-examine X in sub-skill B before B closes

Format:

```
DEPENDENCY MAP
--------------
flow-lifecycle <-> trace-state
  Shared: [entity list]
  Rule: finding in flow-lifecycle touching entity X -> re-examine X in trace-state

flow-lifecycle <-> trace-contract
  Shared: [entity list]
  Rule: ...

[all pairs with shared entities]
```

Pairs with no shared entities are declared INDEPENDENT and require no propagation.

---

**PHASE 2 -- SUB-SKILL EXECUTION**

Execute each sub-skill in order. For each sub-skill:

1. Name the sub-skill and the entities it will examine (drawn from the manifest)
2. Run the simulation
3. Emit findings as rows in a table:

| F-ID | Entity | Boundary | Severity | Blast Radius | Finding Summary |
|------|--------|----------|----------|--------------|-----------------|

4. For every finding that touches an entity with a declared dependency, mark it with PROPAGATE and name the target sub-skill.

Execute in this order:
- **flow-lifecycle** -- business document lifecycle with phase contracts and exception flows
- **flow-conversation** -- multi-turn agent conversation with dead-end and loop detection
- **trace-state** -- state machine transitions with preconditions and invariants
- **trace-contract** -- expected vs actual output comparison with mismatch severity
- **trace-permissions** -- RBAC walk-through with privilege escalation detection

After each sub-skill, process any PROPAGATE markers: re-open the target sub-skill's examination for the flagged entity and record any additional findings with suffix -P (propagated).

---

**PHASE 3 -- PROPAGATION COVERAGE GATE**

After all five sub-skills complete, verify the dependency map was fully honored:

```
PROPAGATION COVERAGE GATE
-------------------------
| Propagation Rule | Triggered? | Re-examined? | Finding Added? |
|------------------|------------|--------------|----------------|
| [rule 1]         | YES/NO     | YES/NO/N/A   | YES/NO/N/A     |
...
```

A rule that was triggered but not re-examined = OPEN PROPAGATION GAP. List all open gaps after the table.

---

**PHASE 4 -- ENTITY COVERAGE MATRIX**

After all sub-skills (including propagated re-examinations) complete, produce:

```
ENTITY COVERAGE MATRIX
----------------------
| Entity | Owning Sub-Skill | Status | F-IDs |
|--------|-----------------|--------|-------|
| [entity from manifest] | [sub-skill] | COVERED / CLEAN / SKIPPED | [F-IDs or --] |
```

COVERED = entity examined, finding raised. CLEAN = entity examined, no anomaly. SKIPPED = entity in manifest, not examined by any sub-skill.

Any SKIPPED entity = execution gap. List SKIPPED entities in a gap block after the matrix.

---

**PHASE 5 -- REMEDIATION QUALITY GATE**

For every finding, produce a remediation entry decomposed into four columns:

```
REMEDIATION QUALITY GATE
------------------------
| F-ID | Verb | Target | Location | Conformance |
|------|------|--------|----------|-------------|
```

Verb: add / remove / resolve / confirm / restrict / relax (action-form only -- no vague entries)
Target: the specific artifact, field, or behavior to change
Location: file, section, or contract surface
Conformance: PASS (entry is specific) / FAIL (entry is vague or incomplete)

Any FAIL row = gate failure. Re-write the failing entry before proceeding.

---

**PHASE 6 -- CROSS-SKILL SYNTHESIS**

Scan all findings (including propagated) for patterns that appear across two or more sub-skills. Name each pattern P-01, P-02, etc. For each pattern:

- Pattern name (descriptive)
- Contributing F-IDs
- Common root cause
- Blast radius classification: SYSTEMIC (affects all sub-skills) / CROSS-CUTTING (affects 2+) / LOCAL (single sub-skill only)

---

**PHASE 7 -- BLAST RADIUS RE-ASSESSMENT**

Re-rank all findings incorporating synthesis results. For any finding whose blast radius increases due to a named pattern, add an ELEVATED annotation citing the P-ID.

Emit the final ranked findings table:

```
FINAL RANKED FINDINGS
---------------------
| Rank | F-ID | Entity | Boundary | Blast Radius | Severity | ELEVATED? | Finding Summary |
|------|------|--------|----------|--------------|----------|-----------|-----------------|
```

---

**OUTPUT**

Write the complete simulation report to:
`simulations/{{topic}}/simulate-{{date}}.md`

The report must contain all seven phases. Each finding must include system boundary and severity. The final ranked table is the primary deliverable.

---

## V-02 -- Axis B (Finding Confidence Scoring)

**Hypothesis**: Adding confidence scoring will split findings that currently appear equivalent under blast-radius alone. HIGH-confidence HIGH-blast findings demand immediate action; LOW-confidence HIGH-blast findings demand spec clarification before any implementation. This distinction may surface a new criterion: confidence-stratified action list (what to fix vs what to confirm first).

---

Simulate the technical behavior of: {{topic}}

You are running a full simulation campaign. Each finding you produce will carry a confidence rating that reflects how strongly the spec supports the finding. Confidence is not a severity modifier -- it is an evidence-strength rating that governs remediation type.

---

**PHASE 1 -- TOPIC ENTITY MANIFEST**

Read all spec and design artifacts for {{topic}}. Extract five entity lists:

- **State entities** (state machines, status fields, lifecycle phases)
- **Contract entities** (API surfaces, input/output schemas, event payloads)
- **Permission entities** (roles, claims, permission checks, access paths)
- **Lifecycle entities** (document types, workflow stages, phase transitions)
- **Conversation entities** (intents, dialog nodes, branching conditions)

Emit as five labeled bullet lists.

---

**PHASE 2 -- CONFIDENCE RATING DEFINITION**

Before running sub-skills, declare the confidence scale:

```
CONFIDENCE SCALE
----------------
HIGH   -- Spec text explicitly describes this behavior. The finding contradicts or extends
          a stated requirement. Evidence: direct quote from spec.
MEDIUM -- Spec is silent. Behavior inferred from surrounding context, related sections,
          or analogous patterns. No direct quote available.
LOW    -- Behavior assumed from general convention, platform norms, or common practice.
          Not derivable from this spec at all.
```

Confidence affects ranking: equal blast radius = higher confidence ranks first.
Confidence affects remediation verb: HIGH -> fix/resolve, MEDIUM -> investigate/confirm, LOW -> consult/validate.

---

**PHASE 3 -- SUB-SKILL EXECUTION**

Execute each sub-skill. For each, emit findings as rows:

| F-ID | Entity | Boundary | Severity | Blast Radius | Confidence | Spec Evidence | Finding Summary |
|------|--------|----------|----------|--------------|------------|---------------|-----------------|

Spec Evidence column: direct quote or "NONE" (MEDIUM) or "CONVENTION" (LOW).

Execute in order:
- **flow-lifecycle** -- business document lifecycle with phase contracts and exception flows
- **flow-conversation** -- multi-turn agent conversation with dead-end and loop detection
- **trace-state** -- state machine transitions with preconditions and invariants
- **trace-contract** -- expected vs actual output comparison with mismatch severity
- **trace-permissions** -- RBAC walk-through with privilege escalation detection

---

**PHASE 4 -- ENTITY COVERAGE MATRIX**

```
ENTITY COVERAGE MATRIX
----------------------
| Entity | Owning Sub-Skill | Status | Confidence Distribution | F-IDs |
|--------|-----------------|--------|------------------------|-------|
```

Confidence Distribution: e.g., "2 HIGH, 1 MEDIUM" or "CLEAN" or "SKIPPED".

SKIPPED entities = execution gap. List after the matrix.

---

**PHASE 5 -- REMEDIATION QUALITY GATE**

```
REMEDIATION QUALITY GATE
------------------------
| F-ID | Confidence | Verb | Target | Location | Conformance |
|------|------------|------|--------|----------|-------------|
```

Verb is confidence-constrained:
- HIGH confidence: fix / add / remove / resolve / restrict / relax
- MEDIUM confidence: investigate / confirm / clarify
- LOW confidence: consult spec / validate assumption / defer

Any verb that does not match confidence level = FAIL. Re-write before proceeding.

---

**PHASE 6 -- CROSS-SKILL SYNTHESIS**

Scan findings for patterns across two or more sub-skills. For each named pattern P-NN:
- Contributing F-IDs
- Average confidence of contributing findings (HIGH/MEDIUM/LOW weighted)
- Pattern blast radius: SYSTEMIC / CROSS-CUTTING / LOCAL

---

**PHASE 7 -- CONFIDENCE-STRATIFIED ACTION LIST**

After synthesis, produce a two-section action list:

**IMMEDIATE ACTION (HIGH confidence findings):**
Ranked by blast radius. These are spec-grounded problems. Fix them.

**SPEC CONSULTATION REQUIRED (MEDIUM + LOW confidence findings):**
Ranked by blast radius. These require spec clarification before implementation. Do not code against unconfirmed assumptions.

---

**PHASE 8 -- BLAST RADIUS RE-ASSESSMENT**

Re-rank all findings incorporating synthesis results. ELEVATED annotations cite P-ID.

```
FINAL RANKED FINDINGS
---------------------
| Rank | F-ID | Entity | Boundary | Blast Radius | Severity | Confidence | ELEVATED? | Finding Summary |
|------|------|--------|----------|--------------|----------|------------|-----------|-----------------|
```

---

**OUTPUT**

Write the complete simulation report to:
`simulations/{{topic}}/simulate-{{date}}.md`

All eight phases required. Each finding must include system boundary, severity, and confidence. The final ranked table is the primary deliverable.

---

## V-03 -- Axis C (Spec Gap Classification)

**Hypothesis**: Typing findings as GAP / CONTRADICTION / ASSUMPTION at detection time will produce structurally distinct remediation plans. A GAP drives a "write new spec text" action; a CONTRADICTION drives a "resolve conflicting requirements" action; an ASSUMPTION drives a "schedule spec review" action. The type column may surface a new rubric criterion: finding type distribution (a spec with 80% GAP findings is structurally different from one with 80% CONTRADICTION findings).

---

Simulate the technical behavior of: {{topic}}

You are running a full simulation campaign. Every finding you detect will be classified by finding type at the moment of detection. Finding type reflects the relationship between the finding and the spec: is the spec silent, contradictory, or merely assumed?

---

**FINDING TYPE VOCABULARY**

Before running sub-skills, internalize this type vocabulary:

```
GAP          -- Spec is silent. The behavior is not described anywhere. No spec text covers
                this scenario. Remediation: add new spec section or requirement.

CONTRADICTION -- Spec describes behavior X. Simulation shows behavior Y is more likely
                (or the spec describes two incompatible behaviors). Remediation: resolve
                conflicting requirements before implementation.

ASSUMPTION   -- Behavior is not in the spec but is inferred from general convention,
                platform norms, or analogous patterns. Not provably wrong -- but not
                provably right either. Remediation: confirm with spec author or add
                explicit spec coverage.
```

Finding type constrains the remediation Verb (C-26):
- GAP -> add, define, specify
- CONTRADICTION -> resolve, remove, reconcile
- ASSUMPTION -> confirm, validate, verify

---

**PHASE 1 -- TOPIC ENTITY MANIFEST**

Read all spec and design artifacts for {{topic}}. Extract five entity lists:

- **State entities** (state machines, status fields, lifecycle phases)
- **Contract entities** (API surfaces, input/output schemas, event payloads)
- **Permission entities** (roles, claims, permission checks, access paths)
- **Lifecycle entities** (document types, workflow stages, phase transitions)
- **Conversation entities** (intents, dialog nodes, branching conditions)

Emit as five labeled bullet lists.

---

**PHASE 2 -- SUB-SKILL EXECUTION**

Execute each sub-skill. For each, emit findings as rows:

| F-ID | Entity | Boundary | Type | Severity | Blast Radius | Finding Summary |
|------|--------|----------|------|----------|--------------|-----------------|

Type column: GAP / CONTRADICTION / ASSUMPTION

Execute in order:
- **flow-lifecycle** -- business document lifecycle with phase contracts and exception flows
- **flow-conversation** -- multi-turn agent conversation with dead-end and loop detection
- **trace-state** -- state machine transitions with preconditions and invariants
- **trace-contract** -- expected vs actual output comparison with mismatch severity
- **trace-permissions** -- RBAC walk-through with privilege escalation detection

---

**PHASE 3 -- FINDING TYPE DISTRIBUTION**

After all sub-skills complete, produce a type distribution table:

```
FINDING TYPE DISTRIBUTION
-------------------------
| Sub-Skill        | GAP | CONTRADICTION | ASSUMPTION | Total |
|-----------------|-----|---------------|------------|-------|
| flow-lifecycle  |     |               |            |       |
| flow-conversation |   |               |            |       |
| trace-state     |     |               |            |       |
| trace-contract  |     |               |            |       |
| trace-permissions |   |               |            |       |
| TOTAL           |     |               |            |       |
```

Write a one-paragraph interpretation: what does this distribution say about the spec's maturity? A GAP-dominant distribution signals an under-specified area. A CONTRADICTION-dominant distribution signals a spec that has accumulated conflicting revisions. An ASSUMPTION-dominant distribution signals an area where convention is substituting for explicit design.

---

**PHASE 4 -- ENTITY COVERAGE MATRIX**

```
ENTITY COVERAGE MATRIX
----------------------
| Entity | Owning Sub-Skill | Status | Finding Types | F-IDs |
|--------|-----------------|--------|---------------|-------|
```

Finding Types column: list types present (e.g., "GAP, ASSUMPTION") or CLEAN or SKIPPED.

SKIPPED = execution gap. List after matrix.

---

**PHASE 5 -- REMEDIATION QUALITY GATE**

```
REMEDIATION QUALITY GATE
------------------------
| F-ID | Type | Verb | Target | Location | Conformance |
|------|------|------|--------|----------|-------------|
```

Verb must match the type-constrained vocabulary:
- GAP: add / define / specify
- CONTRADICTION: resolve / remove / reconcile
- ASSUMPTION: confirm / validate / verify

Any verb that violates type constraints = FAIL. Re-write before proceeding.

---

**PHASE 6 -- CROSS-SKILL SYNTHESIS**

Scan findings for patterns across two or more sub-skills. For each named pattern P-NN:
- Contributing F-IDs and their types
- Dominant type in the pattern (what does this pattern reveal about the spec?)
- Blast radius: SYSTEMIC / CROSS-CUTTING / LOCAL

---

**PHASE 7 -- BLAST RADIUS RE-ASSESSMENT**

Re-rank all findings. ELEVATED annotations cite P-ID. Type column preserved.

```
FINAL RANKED FINDINGS
---------------------
| Rank | F-ID | Entity | Boundary | Type | Blast Radius | Severity | ELEVATED? | Finding Summary |
|------|------|--------|----------|------|--------------|----------|-----------|-----------------|
```

---

**OUTPUT**

Write the complete simulation report to:
`simulations/{{topic}}/simulate-{{date}}.md`

All seven phases required. Each finding must include system boundary, severity, and type. The final ranked table is the primary deliverable.

---

## V-04 -- Axes A + C (Dependency Map + Spec Gap Classification)

**Hypothesis**: Combining the cross-skill dependency map with spec gap classification will show that propagated findings tend to cluster around ASSUMPTION-typed gaps -- the missing spec coverage in one area propagates into adjacent sub-skills as untested assumptions. This combination may surface a new criterion: propagation type analysis (what types of findings trigger re-examination, and what types do re-examinations tend to produce).

---

Simulate the technical behavior of: {{topic}}

You are running a coordinated simulation campaign with two structural additions beyond the R6 baseline: (1) a dependency map that governs cross-skill propagation, and (2) spec gap classification that types every finding at detection. Together they answer: *which spec gaps cascade across system boundaries, and why?*

---

**PHASE 1 -- TOPIC ENTITY MANIFEST**

Read all spec and design artifacts for {{topic}}. Extract five entity lists:

- **State entities** (state machines, status fields, lifecycle phases)
- **Contract entities** (API surfaces, input/output schemas, event payloads)
- **Permission entities** (roles, claims, permission checks, access paths)
- **Lifecycle entities** (document types, workflow stages, phase transitions)
- **Conversation entities** (intents, dialog nodes, branching conditions)

Emit as five labeled bullet lists.

---

**PHASE 2 -- CROSS-SKILL DEPENDENCY MAP**

For each pair of sub-skills sharing entities, declare:

1. Shared entities
2. Propagation rule: finding in sub-skill A touching entity X -> re-examine X in sub-skill B

```
DEPENDENCY MAP
--------------
[sub-skill A] <-> [sub-skill B]
  Shared: [entity list]
  Rule: [propagation rule]
```

Pairs with no shared entities: INDEPENDENT (no propagation required).

---

**PHASE 3 -- SUB-SKILL EXECUTION**

Execute each sub-skill. For each, emit findings:

| F-ID | Entity | Boundary | Type | Severity | Blast Radius | PROPAGATE? | Finding Summary |
|------|--------|----------|------|----------|--------------|------------|-----------------|

Type: GAP / CONTRADICTION / ASSUMPTION
PROPAGATE: YES (cite target sub-skill) / NO

After each sub-skill, process any PROPAGATE markers. Propagated findings get suffix -P.

Execute in order:
- **flow-lifecycle** -- business document lifecycle with phase contracts and exception flows
- **flow-conversation** -- multi-turn agent conversation with dead-end and loop detection
- **trace-state** -- state machine transitions with preconditions and invariants
- **trace-contract** -- expected vs actual output comparison with mismatch severity
- **trace-permissions** -- RBAC walk-through with privilege escalation detection

---

**PHASE 4 -- PROPAGATION TYPE ANALYSIS**

After all sub-skills complete, analyze what happened at propagation boundaries:

```
PROPAGATION TYPE ANALYSIS
-------------------------
| Source F-ID | Source Type | Target Sub-Skill | Propagated F-ID | Propagated Type | Type Changed? |
|-------------|-------------|-----------------|-----------------|-----------------|---------------|
```

Type Changed? YES = the propagation uncovered a different kind of spec problem than the trigger. Note whether GAP triggers tend to produce GAP or ASSUMPTION in the target, etc.

Write a two-sentence interpretation: what does the type shift (or lack of shift) at propagation boundaries say about the spec's internal consistency?

---

**PHASE 5 -- ENTITY COVERAGE MATRIX**

```
ENTITY COVERAGE MATRIX
----------------------
| Entity | Owning Sub-Skill | Status | Finding Types | F-IDs (incl. -P) |
|--------|-----------------|--------|---------------|-----------------|
```

COVERED / CLEAN / SKIPPED. SKIPPED = execution gap.

---

**PHASE 6 -- REMEDIATION QUALITY GATE**

```
REMEDIATION QUALITY GATE
------------------------
| F-ID | Type | Verb | Target | Location | Conformance |
|------|------|------|--------|----------|-------------|
```

Verb constrained by type:
- GAP: add / define / specify
- CONTRADICTION: resolve / remove / reconcile
- ASSUMPTION: confirm / validate / verify

FAIL = verb violates constraint. Re-write before proceeding.

---

**PHASE 7 -- CROSS-SKILL SYNTHESIS**

Named patterns P-NN across 2+ sub-skills. For each:
- Contributing F-IDs (including -P propagated)
- Dominant finding type
- Whether the pattern originated in a trigger finding or emerged from propagation
- Blast radius: SYSTEMIC / CROSS-CUTTING / LOCAL

---

**PHASE 8 -- BLAST RADIUS RE-ASSESSMENT**

Re-rank all findings with ELEVATED annotations citing P-ID.

```
FINAL RANKED FINDINGS
---------------------
| Rank | F-ID | Entity | Boundary | Type | Blast Radius | Severity | ELEVATED? | Finding Summary |
|------|------|--------|----------|------|--------------|----------|-----------|-----------------|
```

---

**OUTPUT**

Write the complete simulation report to:
`simulations/{{topic}}/simulate-{{date}}.md`

All eight phases required. Each finding must include system boundary, severity, and type. The final ranked table is the primary deliverable.

---

## V-05 -- Axes A + B + C (Full R7 Combined)

**Hypothesis**: Combining all three R7 axes with the R6 baseline (Entity Manifest, Entity Coverage Matrix, Remediation Quality Gate, Blast Radius Re-Assessment) produces the maximum structural density. The combined prompt should reveal whether the three axes are additive (each independently surfaces new findings) or overlapping (they capture the same patterns via different structures). If additive, all three may warrant separate rubric criteria. If overlapping, the highest-signal axis absorbs the others.

---

Simulate the technical behavior of: {{topic}}

You are running the full coordinated simulation campaign. This prompt incorporates all R6 structural advances (Entity Manifest, Entity Coverage Matrix, Remediation Quality Gate per C-26, Blast Radius Re-Assessment per C-28) plus three R7 extensions: cross-skill dependency map (Axis A), finding confidence scoring (Axis B), and spec gap classification (Axis C).

The output is a simulation report where every finding is simultaneously characterized by: which entities it touches, which sub-skills it propagated through, how strongly the spec grounds it, and what type of spec problem it represents.

---

**PHASE 1 -- TOPIC ENTITY MANIFEST**

Read all spec and design artifacts for {{topic}}. Extract five entity lists:

- **State entities** (state machines, status fields, lifecycle phases)
- **Contract entities** (API surfaces, input/output schemas, event payloads)
- **Permission entities** (roles, claims, permission checks, access paths)
- **Lifecycle entities** (document types, workflow stages, phase transitions)
- **Conversation entities** (intents, dialog nodes, branching conditions)

Emit as five labeled bullet lists.

---

**PHASE 2 -- CROSS-SKILL DEPENDENCY MAP**

For each sub-skill pair sharing entities:

```
DEPENDENCY MAP
--------------
[sub-skill A] <-> [sub-skill B]
  Shared: [entity list]
  Rule: finding in A touching entity X -> re-examine X in B

[continue for all pairs with shared entities]

INDEPENDENT PAIRS: [list pairs with no shared entities]
```

---

**PHASE 3 -- EXECUTION VOCABULARY**

Before running sub-skills, declare the two embedded scales:

```
FINDING TYPE
GAP          -- spec is silent; remediation verb: add / define / specify
CONTRADICTION -- spec is explicit but inconsistent; remediation verb: resolve / remove / reconcile
ASSUMPTION   -- inferred from convention; remediation verb: confirm / validate / verify

CONFIDENCE
HIGH   -- direct spec quote available; contradicts or extends an explicit requirement
MEDIUM -- spec is silent; inferred from surrounding context; no direct quote
LOW    -- assumed from convention; not derivable from this spec
```

Ranking tiebreaker: equal blast radius -> higher confidence ranks first.

---

**PHASE 4 -- SUB-SKILL EXECUTION**

Execute each sub-skill. For each, emit findings:

| F-ID | Entity | Boundary | Type | Severity | Blast Radius | Confidence | Spec Evidence | PROPAGATE? | Finding Summary |
|------|--------|----------|------|----------|--------------|------------|---------------|------------|-----------------|

After each sub-skill, process PROPAGATE markers. Propagated findings get suffix -P. Propagated findings inherit source confidence unless the re-examination reveals new spec evidence.

Execute in order:
- **flow-lifecycle** -- business document lifecycle with phase contracts and exception flows
- **flow-conversation** -- multi-turn agent conversation with dead-end and loop detection
- **trace-state** -- state machine transitions with preconditions and invariants
- **trace-contract** -- expected vs actual output comparison with mismatch severity
- **trace-permissions** -- RBAC walk-through with privilege escalation detection

---

**PHASE 5 -- PROPAGATION COVERAGE GATE**

```
PROPAGATION COVERAGE GATE
-------------------------
| Rule | Triggered? | Re-examined? | Finding Added? | Type Change? |
|------|------------|--------------|----------------|-------------|
```

Open propagation gaps (triggered but not re-examined) = execution failure. List after table.

---

**PHASE 6 -- ENTITY COVERAGE MATRIX**

```
ENTITY COVERAGE MATRIX
----------------------
| Entity | Owning Sub-Skill | Status | Finding Types | Confidence Dist | F-IDs |
|--------|-----------------|--------|---------------|-----------------|-------|
```

Status: COVERED / CLEAN / SKIPPED. SKIPPED = execution gap.
Confidence Dist: e.g., "1 HIGH, 2 MEDIUM" or "--" for CLEAN/SKIPPED.

---

**PHASE 7 -- REMEDIATION QUALITY GATE**

```
REMEDIATION QUALITY GATE
------------------------
| F-ID | Type | Confidence | Verb | Target | Location | Conformance |
|------|------|------------|------|--------|----------|-------------|
```

Dual constraint on Verb: must satisfy type-vocabulary AND confidence-vocabulary.
- GAP + HIGH: impossible by definition (if spec is silent, confidence cannot be HIGH) -> flag as classification error
- CONTRADICTION + LOW: unlikely; if LOW, reclassify as ASSUMPTION
- All other combinations: apply constrained verb vocabulary

FAIL = verb violates constraint or classification is internally inconsistent. Re-write before proceeding.

---

**PHASE 8 -- CROSS-SKILL SYNTHESIS**

Named patterns P-NN across 2+ sub-skills. For each:
- Contributing F-IDs (including -P)
- Dominant type and average confidence
- Whether pattern originated in trigger finding or emerged from propagation
- Blast radius: SYSTEMIC / CROSS-CUTTING / LOCAL

---

**PHASE 9 -- CONFIDENCE-STRATIFIED ACTION LIST**

Two-section action list from synthesis:

**IMMEDIATE ACTION (HIGH confidence):**
Fix these. Spec grounds them. Ranked by blast radius.

**SPEC CONSULTATION REQUIRED (MEDIUM + LOW confidence):**
Do not code against these. Confirm spec intent first. Ranked by blast radius.

---

**PHASE 10 -- BLAST RADIUS RE-ASSESSMENT**

Re-rank all findings with ELEVATED annotations citing P-ID. Type and Confidence columns preserved.

```
FINAL RANKED FINDINGS
---------------------
| Rank | F-ID | Entity | Boundary | Type | Blast Radius | Severity | Confidence | ELEVATED? | Finding Summary |
|------|------|--------|----------|------|--------------|----------|------------|-----------|-----------------|
```

---

**OUTPUT**

Write the complete simulation report to:
`simulations/{{topic}}/simulate-{{date}}.md`

All ten phases required. Each finding must include system boundary, severity, type, and confidence. The final ranked table is the primary deliverable.

---

## Variation Summary

| Variation | Axis | Hypothesis | New Structure |
|-----------|------|------------|---------------|
| V-01 | A only | Dependency map surfaces cross-linked findings missed by independent passes | DEPENDENCY MAP + PROPAGATION COVERAGE GATE |
| V-02 | B only | Confidence scoring splits equal-blast findings; surfaces spec-grounded vs assumption-grounded problems | CONFIDENCE column + CONFIDENCE-STRATIFIED ACTION LIST |
| V-03 | C only | Finding type distribution diagnoses spec maturity and constrains remediation verbs | TYPE column + FINDING TYPE DISTRIBUTION + type-constrained REMEDIATION QUALITY GATE |
| V-04 | A + C | Propagation type analysis reveals whether cascading gaps change type at sub-skill boundaries | DEPENDENCY MAP + TYPE column + PROPAGATION TYPE ANALYSIS |
| V-05 | A + B + C | Full kitchen-sink tests whether axes are additive or overlapping; maximizes structural density | All R6 + DEPENDENCY MAP + CONFIDENCE + TYPE + PROPAGATION TYPE ANALYSIS + CONFIDENCE-STRATIFIED ACTION LIST (10 phases) |

**Predicted rubric candidates from R7:**

- **C-29**: Propagation Coverage Gate -- all triggered dependency-map rules produce a documented re-examination result (extends C-27 from entity silence to propagation silence)
- **C-30**: Finding Type Distribution -- findings table includes a type column (GAP/CONTRADICTION/ASSUMPTION) and a post-execution distribution summary with spec maturity interpretation
- **C-31**: Confidence-Stratified Action List -- findings split into IMMEDIATE ACTION vs SPEC CONSULTATION REQUIRED sections based on confidence level before the final ranked table
