# Quest Variate — org-build Round 20 (V-01 through V-05)

---

## V-01 — Lifecycle Emphasis

**Axis:** Maximum phase-boundary explicitness — every boundary carries outbound + inbound double-guards, every sub-step has a named FORBIDDEN, Input Contracts are maximally verbose.

**Hypothesis:** Redundant guards at every structural seam eliminate cross-phase contamination, making the prompt independently auditable phase-by-phase.

---

```markdown
org-build

Generate a complete org from scan results or directly from a repo.

Produces:
- org-chart.md — ASCII hierarchy, headcount-by-area table, operating rhythm,
  committee charters, inertia assessment, evolution roadmap, anti-pattern watch
- .roles/{area}/{role}.md — one file per role with all five fields:
  orientation, lens, expertise, scope, collaborates_with

Depth modes: standard (20–30 roles, default) | deep (50+ roles, via --depth deep)

---

## GLOBAL CONSTANTS

Declared once. Phase instructions reference these tables by name only.
No phase embeds table contents inline.

### TABLE-A — Verbatim IA Scope Templates

Keyed to T2-PRESSURE. The inertia-advocate scope field MUST contain the exact
matching text. Paraphrase, adaptation, or deviation from this text fails C-17.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Monitor the status-quo bias in decisions that appear purely technical. The org is flat and healthy; your role is early-warning, not structural intervention. Flag when a team resists decomposition without articulating a complexity justification. |
| LOW | Identify the one load-bearing assumption keeping the current structure in place and surface it at the next planning cycle. The org can operate flat but carries a known structural debt; your role is to name it explicitly so the team can decide consciously. |
| MODERATE | Audit two to three decision points per quarter where flat structure introduces coordination overhead above the threshold for a three-person team. Produce a pressure memo after each audit. The org is approaching the zone where structure becomes load-bearing. |
| HIGH | Run a full structural case at the next program boundary. The inertia load is above the operational threshold. Your role shifts from monitor to advocate: build the affirmative case for the structural change and present it with evidence to the decision committee. |
| CRITICAL | Initiate the structural transition immediately. Flat operation is no longer viable at this scale and coupling density. Your role is transition architect: own the migration path, the committee charter, and the first-90-days operating model for the new structure. |

### TABLE-B — Anti-Pattern Category Derivation

Keyed to T2-VERDICT. Both columns MUST be populated per verdict row.
Category selection independent of this table fails C-12 and C-18.

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## PHASE 1 — Input Gate

### Input Contract

_(No upstream phase. No prior gate variables required.)_

### Task Steps

1. Read the provided repo path or scan results file.
2. Determine the depth mode from the invocation flag (--depth deep present or absent).
3. Classify the input source type as repo or scan.

### Constraints

MUST set T1-DEPTH-FLAG to exactly one value from [standard | deep].
MUST set T1-SOURCE to exactly one value from [repo | scan].
FORBIDDEN: beginning Phase 2 before the PHASE-1 record block is emitted.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-SOURCE: [repo | scan]
===

**Boundary Guard — Phase 2 Inbound:**
FORBIDDEN: Phase 2 executes before the PHASE-1 record block above is emitted.

---

## PHASE 2 — Inertia Assessment

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid set: [standard | deep].
MUST consume T1-SOURCE from PHASE-1 record block. Valid set: [repo | scan].
FORBIDDEN: executing Phase 2 before the PHASE-1 record block is emitted.

### Task Steps

**Sub-step SCAN:**
1. Examine the repo or scan for structural signals: team size, coupling density,
   decision latency indicators, escalation path length, communication topology.

**Sub-step PRESSURE:**
2. Assign a FLAT-CASE-PRESSURE rating from the closed set in TABLE-A column headers.
   Consider each pressure tier against the signals observed in sub-step SCAN.

**Sub-step VERDICT:**
3. Derive T2-VERDICT from the FLAT-CASE-PRESSURE rating. Apply exactly one verdict
   from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
   Only one verdict. Both is an error. Neither is an error.

### Constraints

MUST assign T2-PRESSURE to exactly one value from [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST assign T2-VERDICT to exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: beginning sub-step PRESSURE before completing sub-step SCAN.
FORBIDDEN: beginning sub-step VERDICT before completing sub-step PRESSURE.
FORBIDDEN: selecting anti-pattern categories before the PHASE-2 record block is emitted.
FORBIDDEN: enumerating roles before the PHASE-2 record block is emitted.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED as T2-VERDICT. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED as T2-VERDICT. Neither is an error.
FORBIDDEN: beginning Phase 3 before the PHASE-2 record block is emitted.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-GATE: FLAT-CASE-PRESSURE: {{T2-PRESSURE}}. VERDICT: {{T2-VERDICT}}.
             Only one verdict. Both is an error. Neither is an error.
===

**Boundary Guard — Phase 3 Inbound:**
FORBIDDEN: Phase 3 executes before the PHASE-2 record block above is emitted.

---

## PHASE 3 — Role Enumeration

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid set: [standard | deep].
MUST consume T2-PRESSURE from PHASE-2 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2 record block. Valid set: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: executing Phase 3 before the PHASE-2 record block is emitted.

### Task Steps

**Sub-step COUNT:**
1. Determine role count floor from T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = standard → enumerate 20–30 roles.
   - T1-DEPTH-FLAG = deep → enumerate 50+ roles.
   Record each role name and assigned area.

**Sub-step AREA-GROUPING:**
2. Group all enumerated roles into area subdirectories.
   Each area becomes a subdirectory under .roles/{area}/.
   Assign every role to exactly one area.

**Sub-step IA-ANCHOR:**
3. Define the inertia-advocate role. Look up T2-PRESSURE in TABLE-A.
   Copy the matching verbatim scope text. Write it as the scope field value.

**Sub-step CATEGORY-READ:**
4. Look up T2-VERDICT in TABLE-B. Record the required categories and
   FORBIDDEN categories for Phase 4's Anti-Pattern Watch section.

### Constraints

MUST set T3-ROLE-OUTCOME to exactly one value from [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST include inertia-advocate as a named role file under .roles/.
MUST create minimum 2 area subdirectories under .roles/.
MUST copy TABLE-A scope text verbatim. Paraphrase fails C-17.
FORBIDDEN: beginning sub-step AREA-GROUPING before completing sub-step COUNT.
FORBIDDEN: beginning sub-step IA-ANCHOR before completing sub-step AREA-GROUPING.
FORBIDDEN: beginning sub-step CATEGORY-READ before completing sub-step IA-ANCHOR.
FORBIDDEN: beginning Phase 4 before the PHASE-3 record block is emitted.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-IA-PRESSURE-KEY: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-AP-REQUIRED: [cat-2,cat-3 | cat-1,cat-4]
T3-AP-FORBIDDEN: [cat-1,cat-4 | cat-2,cat-3]
===

**Boundary Guard — Phase 4 Inbound:**
FORBIDDEN: Phase 4 executes before the PHASE-3 record block above is emitted.

---

## PHASE 4 — Artifact Production

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid set: [standard | deep].
MUST consume T2-PRESSURE from PHASE-2 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2 record block. Valid set: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T3-ROLE-OUTCOME from PHASE-3 record block. Valid set: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST consume T3-IA-PRESSURE-KEY from PHASE-3 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T3-AP-REQUIRED from PHASE-3 record block. Valid set: [cat-2,cat-3 | cat-1,cat-4].
MUST consume T3-AP-FORBIDDEN from PHASE-3 record block. Valid set: [cat-1,cat-4 | cat-2,cat-3].
FORBIDDEN: executing Phase 4 before the PHASE-3 record block is emitted.

### Task Steps

**Sub-step ORG-CHART:**
1. Write org-chart.md using the skeleton below. Fill every {{SLOT}} from
   the corresponding gate variable or enumerated content.

```
# Org Chart — {{REPO-NAME}}

## Hierarchy

{{ASCII-BOX-DIAGRAM}}
(minimum 2 org levels, box-and-line format)

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| {{T3-AREA-1}} | {{N}} | {{ROLES}} | {{DECIDES}} | {{ESCALATES}} |

## Operating Rhythm

| Meeting | Cadence | Owner | Quorum |
|---------|---------|-------|--------|
| ROB | {{CADENCE}} | {{OWNER}} | {{N of M}} |
| Shiproom | {{CADENCE}} | {{OWNER}} | {{N of M}} |
| {{GOVERNANCE-MEETING}} | {{CADENCE}} | {{OWNER}} | {{N of M}} |

### Committee Charters

#### {{GOVERNANCE-MEETING}}
- Name: {{NAME}}
- Cadence: {{CADENCE}}
- Owner: {{OWNER}}
- Attendees: {{LIST}}
- Quorum: {{N of M}}
- Purpose: {{PURPOSE}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Only one verdict. Both is an error. Neither is an error.
CAN-OPERATE-FLAT: permitted iff T2-VERDICT = CAN-OPERATE-FLAT. FORBIDDEN otherwise.
STRUCTURE-WARRANTED: permitted iff T2-VERDICT = STRUCTURE-WARRANTED. FORBIDDEN otherwise.

## Org Evolution Roadmap

| Trigger | Trigger Type | Structural Change |
|---------|-------------|-------------------|
| {{HEADCOUNT-THRESHOLD}} | headcount | {{CHANGE}} |
| {{NON-HEADCOUNT-TRIGGER}} | {{OTHER-CATEGORY}} | {{CHANGE}} |

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|--------------|----------|---------------------|------------|
| {{ELEMENT-NAME}} | {{T3-AP-REQUIRED-1}} | [{{ELEMENT-NAME}}] ({{CAT-N}}) — {{REASON}} | {{REMEDIATION-ACTION}} |
```

**Sub-step ROLE-FILES:**
2. Write one .roles/{area}/{role}.md file per enumerated role.
   Every file includes all five fields: orientation, lens, expertise, scope,
   collaborates_with. For inertia-advocate, copy scope verbatim from TABLE-A
   using T3-IA-PRESSURE-KEY.

### Constraints

MUST include ASCII box diagram with minimum 2 org levels in org-chart.md.
MUST include headcount-by-area table with columns: Area, Headcount, Key Roles, Decides, Escalates.
MUST include operating rhythm table with minimum 3 rows: ROB, shiproom, and one governance meeting.
MUST express quorum as N of M fraction in every governance meeting charter.
MUST include all five charter fields per governance meeting: name, cadence, owner, attendees, quorum.
MUST write FLAT-CASE-PRESSURE: {{T2-PRESSURE}} in the inertia assessment section.
MUST write exactly one verdict from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] in inertia assessment.
MUST include inertia-advocate role file under .roles/.
MUST include all five fields in every role file.
MUST write inertia-advocate scope verbatim from TABLE-A. Paraphrase fails C-17.
MUST include Org Evolution Roadmap with minimum 2 rows; Row 1 MUST be headcount-trigger; Row 2 MUST be a different trigger type.
MUST format anti-pattern citations as: [element name] (cat-N) — {reason}.
MUST write remediation actions in all Mitigation cells.
MUST select anti-pattern categories only from T3-AP-REQUIRED.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in the inertia assessment. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED in the inertia assessment. Neither is an error.
FORBIDDEN: using anti-pattern categories listed in T3-AP-FORBIDDEN.
FORBIDDEN: writing Mitigation cells as format guidance or column descriptions rather than remediation actions.
FORBIDDEN: using advisory language (should, prefer, consider, typically) in any constraint statement.
FORBIDDEN: beginning sub-step ROLE-FILES before completing sub-step ORG-CHART.
FORBIDDEN: any output after this phase before the PHASE-4 record block is emitted.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no subsequent output begins before this block is emitted.
T4-ORG-CHART: [WRITTEN | MISSING]
T4-ROLES-WRITTEN: [COMPLETE | INCOMPLETE]
T4-VERDICT-EMITTED: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-ANTI-PATTERN-COMPLIANCE: [COMPLIANT | NON-COMPLIANT]
===
```

---

## V-02 — Role Sequence Reorder

**Axis:** Role sequence — inertia assessment is elevated to Phase 1 (it subsumes the depth-gate as sub-step 1a). No standalone Input Gate phase. Phase count collapses from 4 to 3, changing T-variable prefixes throughout.

**Hypothesis:** Making inertia the entry point forces every downstream choice to derive from a locked verdict rather than treating inertia as a secondary concern. Earlier structural lock = fewer downstream coherence failures.

---

```markdown
org-build

Generate a complete org from scan results or directly from a repo.

Produces:
- org-chart.md — ASCII hierarchy, headcount-by-area table, operating rhythm,
  committee charters, inertia assessment, evolution roadmap, anti-pattern watch
- .roles/{area}/{role}.md — one file per role with all five fields:
  orientation, lens, expertise, scope, collaborates_with

Depth modes: standard (20–30 roles) | deep (50+ roles via --depth deep)

---

## GLOBAL CONSTANTS

Declared once. Phase instructions reference these tables by name only.

### TABLE-A — Verbatim IA Scope Templates

Keyed to T1-PRESSURE. Inertia-advocate scope field MUST contain verbatim text.
Paraphrase is FORBIDDEN.

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Monitor the status-quo bias in decisions that appear purely technical. The org is flat and healthy; your role is early-warning, not structural intervention. Flag when a team resists decomposition without articulating a complexity justification. |
| LOW | Identify the one load-bearing assumption keeping the current structure in place and surface it at the next planning cycle. The org can operate flat but carries a known structural debt; your role is to name it explicitly so the team can decide consciously. |
| MODERATE | Audit two to three decision points per quarter where flat structure introduces coordination overhead above the threshold for a three-person team. Produce a pressure memo after each audit. The org is approaching the zone where structure becomes load-bearing. |
| HIGH | Run a full structural case at the next program boundary. The inertia load is above the operational threshold. Your role shifts from monitor to advocate: build the affirmative case for the structural change and present it with evidence to the decision committee. |
| CRITICAL | Initiate the structural transition immediately. Flat operation is no longer viable at this scale and coupling density. Your role is transition architect: own the migration path, the committee charter, and the first-90-days operating model for the new structure. |

### TABLE-B — Anti-Pattern Category Derivation

Keyed to T1-VERDICT.

| T1-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## PHASE 1 — Inertia Assessment + Depth Gate

Phase 1 locks the structural verdict before any role enumeration occurs.
Depth mode is resolved as a sub-step here to eliminate a separate gate phase.

### Input Contract

_(No upstream phase. No prior gate variables required.)_

### Task Steps

**Sub-step DEPTH:**
1. Read the invocation flag. Set T1-DEPTH-FLAG from [standard | deep].

**Sub-step SCAN:**
2. Read the provided repo or scan results. Identify structural signals:
   team size, coupling density, decision latency, escalation path length.

**Sub-step PRESSURE:**
3. Assign a FLAT-CASE-PRESSURE rating keyed to TABLE-A.
   Apply the closest matching tier to the observed signals.

**Sub-step VERDICT:**
4. Derive T1-VERDICT from the FLAT-CASE-PRESSURE rating.
   Apply exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
   Only one verdict. Both is an error. Neither is an error.

**Sub-step CATEGORY-READ:**
5. Look up T1-VERDICT in TABLE-B. Record required and FORBIDDEN categories.

### Constraints

MUST set T1-DEPTH-FLAG to exactly one value from [standard | deep].
MUST set T1-PRESSURE to exactly one value from [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST set T1-VERDICT to exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: beginning sub-step SCAN before completing sub-step DEPTH.
FORBIDDEN: beginning sub-step PRESSURE before completing sub-step SCAN.
FORBIDDEN: beginning sub-step VERDICT before completing sub-step PRESSURE.
FORBIDDEN: beginning sub-step CATEGORY-READ before completing sub-step VERDICT.
FORBIDDEN: enumerating roles before the PHASE-1 record block is emitted.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED as T1-VERDICT. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED as T1-VERDICT. Neither is an error.
FORBIDDEN: beginning Phase 2 before the PHASE-1 record block is emitted.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-AP-REQUIRED: [cat-2,cat-3 | cat-1,cat-4]
T1-AP-FORBIDDEN: [cat-1,cat-4 | cat-2,cat-3]
T1-IA-GATE: FLAT-CASE-PRESSURE: {{T1-PRESSURE}}. VERDICT: {{T1-VERDICT}}.
            Only one verdict. Both is an error. Neither is an error.
===

**Boundary Guard — Phase 2 Inbound:**
FORBIDDEN: Phase 2 executes before the PHASE-1 record block above is emitted.

---

## PHASE 2 — Role Enumeration

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid set: [standard | deep].
MUST consume T1-PRESSURE from PHASE-1 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T1-VERDICT from PHASE-1 record block. Valid set: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T1-AP-REQUIRED from PHASE-1 record block. Valid set: [cat-2,cat-3 | cat-1,cat-4].
FORBIDDEN: executing Phase 2 before the PHASE-1 record block is emitted.

### Task Steps

**Sub-step COUNT:**
1. Set the role count floor from T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = standard → enumerate 20–30 roles.
   - T1-DEPTH-FLAG = deep → enumerate 50+ roles.

**Sub-step AREA-GROUPING:**
2. Group all enumerated roles into area subdirectories under .roles/{area}/.
   Assign every role to exactly one area. Create minimum 2 area subdirectories.

**Sub-step IA-ANCHOR:**
3. Define the inertia-advocate role. Look up T1-PRESSURE in TABLE-A.
   Copy verbatim scope text as the scope field value.

### Constraints

MUST set T2-ROLE-OUTCOME to exactly one value from [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST include inertia-advocate role under .roles/.
MUST create minimum 2 area subdirectories under .roles/.
MUST copy TABLE-A scope text verbatim for inertia-advocate. Paraphrase fails C-17.
FORBIDDEN: beginning sub-step AREA-GROUPING before completing sub-step COUNT.
FORBIDDEN: beginning sub-step IA-ANCHOR before completing sub-step AREA-GROUPING.
FORBIDDEN: beginning Phase 3 before the PHASE-2 record block is emitted.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T2-IA-PRESSURE-KEY: [NONE | LOW | MODERATE | HIGH | CRITICAL]
===

**Boundary Guard — Phase 3 Inbound:**
FORBIDDEN: Phase 3 executes before the PHASE-2 record block above is emitted.

---

## PHASE 3 — Artifact Production

### Input Contract

MUST consume T1-PRESSURE from PHASE-1 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T1-VERDICT from PHASE-1 record block. Valid set: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T1-AP-REQUIRED from PHASE-1 record block. Valid set: [cat-2,cat-3 | cat-1,cat-4].
MUST consume T1-AP-FORBIDDEN from PHASE-1 record block. Valid set: [cat-1,cat-4 | cat-2,cat-3].
MUST consume T2-ROLE-OUTCOME from PHASE-2 record block. Valid set: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST consume T2-IA-PRESSURE-KEY from PHASE-2 record block. Valid set: [NONE | LOW | MODERATE | HIGH | CRITICAL].
FORBIDDEN: executing Phase 3 before the PHASE-2 record block is emitted.

### Task Steps

**Sub-step ORG-CHART:**
1. Write org-chart.md:
   - ASCII box/line hierarchy with minimum 2 org levels.
   - Headcount-by-area table: Area | Headcount | Key Roles | Decides | Escalates.
   - Operating rhythm table: minimum 3 rows (ROB, shiproom, one governance meeting).
     Each governance row gets a full charter: name, cadence, owner, attendees,
     quorum (as N of M), purpose.
   - Inertia assessment: FLAT-CASE-PRESSURE: {{T1-PRESSURE}}.
     VERDICT: {{T1-VERDICT}}. Exactly one verdict.
     Only one verdict. Both is an error. Neither is an error.
   - Org Evolution Roadmap: 2+ rows; Row 1 = headcount trigger; Row 2 = different category.
   - Anti-Pattern Watch: use categories from T1-AP-REQUIRED.
     Format: [element name] (cat-N) — {reason}. Mitigation = remediation action.

**Sub-step ROLE-FILES:**
2. Write one .roles/{area}/{role}.md per role.
   Every file includes: orientation, lens, expertise, scope, collaborates_with.
   For inertia-advocate, copy scope verbatim from TABLE-A keyed to T2-IA-PRESSURE-KEY.

### Constraints

MUST include ASCII hierarchy with minimum 2 levels.
MUST include Decides and Escalates columns in headcount table.
MUST include minimum 3 rows in operating rhythm table.
MUST include quorum as N of M in every governance charter.
MUST write FLAT-CASE-PRESSURE: {{T1-PRESSURE}} in inertia assessment.
MUST write exactly one verdict from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST include Evolution Roadmap Row 1 as headcount trigger, Row 2 as different category.
MUST cite anti-patterns as [element name] (cat-N) — {reason}.
MUST write Mitigation cells as remediation actions, not format descriptions.
MUST include all five role file fields in every .roles/ file.
MUST write inertia-advocate scope verbatim from TABLE-A.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in inertia assessment. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED in inertia assessment. Neither is an error.
FORBIDDEN: using categories from T1-AP-FORBIDDEN in Anti-Pattern Watch.
FORBIDDEN: beginning sub-step ROLE-FILES before completing sub-step ORG-CHART.
FORBIDDEN: using advisory language (should, prefer, consider, typically) in any constraint context.
FORBIDDEN: any further output before the PHASE-3 record block is emitted.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no subsequent output begins before this block is emitted.
T3-ORG-CHART: [WRITTEN | MISSING]
T3-ROLES-WRITTEN: [COMPLETE | INCOMPLETE]
T3-VERDICT-EMITTED: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-AP-COMPLIANCE: [COMPLIANT | NON-COMPLIANT]
===
```

---

## V-03 — Output Format Variation

**Axis:** Output format — artifact skeleton uses maximally explicit named placeholder slots for every gate variable; tables use an Escalates-before-Decides column ordering; record block fields use expanded closed-set annotations with explicit type labels; the pre-print skeleton is front-loaded before Phase 1 as a "target shape" reference.

**Hypothesis:** Showing the filled skeleton as a global constant lets the model resolve all artifact structure questions before phase execution begins, reducing mid-phase format improvisation.

---

```markdown
org-build

Generate a complete org from scan results or directly from a repo.

Produces:
- org-chart.md — ASCII hierarchy, headcount-by-area table, operating rhythm,
  committee charters, inertia assessment, evolution roadmap, anti-pattern watch
- .roles/{area}/{role}.md — one file per role with all five fields

Depth modes: standard (20–30 roles) | deep (50+ roles via --depth deep)

---

## GLOBAL CONSTANTS

Declared once. Phase instructions reference these constants by name.

### TABLE-A — Verbatim IA Scope Templates

Keyed to gate variable T2-PRESSURE.
Inertia-advocate scope MUST contain the matching text verbatim.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Monitor the status-quo bias in decisions that appear purely technical. The org is flat and healthy; your role is early-warning, not structural intervention. Flag when a team resists decomposition without articulating a complexity justification. |
| LOW | Identify the one load-bearing assumption keeping the current structure in place and surface it at the next planning cycle. The org can operate flat but carries a known structural debt; your role is to name it explicitly so the team can decide consciously. |
| MODERATE | Audit two to three decision points per quarter where flat structure introduces coordination overhead above the threshold for a three-person team. Produce a pressure memo after each audit. The org is approaching the zone where structure becomes load-bearing. |
| HIGH | Run a full structural case at the next program boundary. The inertia load is above the operational threshold. Your role shifts from monitor to advocate: build the affirmative case for the structural change and present it with evidence to the decision committee. |
| CRITICAL | Initiate the structural transition immediately. Flat operation is no longer viable at this scale and coupling density. Your role is transition architect: own the migration path, the committee charter, and the first-90-days operating model for the new structure. |

### TABLE-B — Anti-Pattern Category Derivation

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

### TABLE-C — Artifact Skeleton (Target Shape)

Fill every [[ ]] slot with the corresponding gate variable or enumerated value.
This skeleton is the required output shape for org-chart.md. Deviation from this
structure fails. A reader who knows only the gate variable names MUST be able to
fill every slot without ambiguity.

```
# Org Chart — [[REPO-NAME: string]]

## Hierarchy

[[ASCII-BOX-DIAGRAM: box-and-line, minimum 2 levels]]

## Headcount by Area

| Area | Headcount | Key Roles | Escalates | Decides |
|------|-----------|-----------|-----------|---------|
| [[AREA-1: string]] | [[N: integer]] | [[ROLES: list]] | [[ESCALATES: string]] | [[DECIDES: string]] |

## Operating Rhythm

| Meeting | Cadence | Owner | Quorum |
|---------|---------|-------|--------|
| ROB | [[CADENCE: string]] | [[OWNER: string]] | [[N of M: fraction]] |
| Shiproom | [[CADENCE: string]] | [[OWNER: string]] | [[N of M: fraction]] |
| [[GOV-MEETING: string]] | [[CADENCE: string]] | [[OWNER: string]] | [[N of M: fraction]] |

### [[GOV-MEETING]] Charter
- Name: [[GOV-MEETING-NAME: string]]
- Cadence: [[GOV-CADENCE: string]]
- Owner: [[GOV-OWNER: string]]
- Attendees: [[GOV-ATTENDEES: list]]
- Quorum: [[GOV-QUORUM: N of M]]
- Purpose: [[GOV-PURPOSE: string]]

## Inertia Assessment

FLAT-CASE-PRESSURE: [[T2-PRESSURE: NONE|LOW|MODERATE|HIGH|CRITICAL]]
VERDICT: [[T2-VERDICT: CAN-OPERATE-FLAT|STRUCTURE-WARRANTED]]
Only one verdict. Both is an error. Neither is an error.

## Org Evolution Roadmap

| Trigger | Trigger Type | Structural Change |
|---------|-------------|-------------------|
| [[TRIGGER-1: headcount-threshold]] | headcount | [[CHANGE-1: string]] |
| [[TRIGGER-2: non-headcount]] | [[TYPE-2: string]] | [[CHANGE-2: string]] |

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|--------------|----------|---------------------|------------|
| [[AP-NAME]] | [[T3-AP-REQUIRED: cat-N]] | [[AP-NAME]] ([[CAT-N]]) — [[REASON: string]] | [[MITIGATION: remediation-action]] |
```

---

## PHASE 1 — Input Gate

### Input Contract

_(No upstream phase.)_

### Task Steps

1. Read the provided repo or scan results.
2. Determine depth mode from the invocation flag.
3. Classify input source as repo or scan.

### Constraints

MUST set T1-DEPTH-FLAG to exactly one value from [standard | deep].
MUST set T1-SOURCE to exactly one value from [repo | scan].
FORBIDDEN: beginning Phase 2 before the PHASE-1 record block is emitted.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: enum[standard | deep]
T1-SOURCE: enum[repo | scan]
===

**Boundary Guard — Phase 2 Inbound:**
FORBIDDEN: Phase 2 executes before the PHASE-1 record block above is emitted.

---

## PHASE 2 — Inertia Assessment

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1. Valid: enum[standard | deep].
MUST consume T1-SOURCE from PHASE-1. Valid: enum[repo | scan].
FORBIDDEN: executing Phase 2 before the PHASE-1 record block is emitted.

### Task Steps

**Sub-step SCAN:**
1. Examine repo or scan for structural signals: team size, coupling density,
   decision latency, escalation path length, communication topology.

**Sub-step PRESSURE:**
2. Assign FLAT-CASE-PRESSURE from the closed set in TABLE-A's T2-PRESSURE column.

**Sub-step VERDICT:**
3. Derive T2-VERDICT from the pressure rating using TABLE-B.
   Apply exactly one value: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
   Only one verdict. Both is an error. Neither is an error.

**Sub-step CATEGORY-READ:**
4. Read TABLE-B using T2-VERDICT. Record required and FORBIDDEN anti-pattern categories.

### Constraints

MUST set T2-PRESSURE to exactly one value from [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST set T2-VERDICT to exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: beginning sub-step PRESSURE before completing sub-step SCAN.
FORBIDDEN: beginning sub-step VERDICT before completing sub-step PRESSURE.
FORBIDDEN: beginning sub-step CATEGORY-READ before completing sub-step VERDICT.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED as T2-VERDICT. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED as T2-VERDICT. Neither is an error.
FORBIDDEN: enumerating roles before the PHASE-2 record block is emitted.
FORBIDDEN: beginning Phase 3 before the PHASE-2 record block is emitted.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: enum[NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-AP-REQUIRED: enum[cat-2,cat-3 | cat-1,cat-4]
T2-AP-FORBIDDEN: enum[cat-1,cat-4 | cat-2,cat-3]
T2-IA-GATE: FLAT-CASE-PRESSURE: [[T2-PRESSURE]]. VERDICT: [[T2-VERDICT]].
            Only one verdict. Both is an error. Neither is an error.
===

**Boundary Guard — Phase 3 Inbound:**
FORBIDDEN: Phase 3 executes before the PHASE-2 record block above is emitted.

---

## PHASE 3 — Role Enumeration

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1. Valid: enum[standard | deep].
MUST consume T2-PRESSURE from PHASE-2. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2. Valid: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: executing Phase 3 before the PHASE-2 record block is emitted.

### Task Steps

**Sub-step COUNT:**
1. Set role count floor from T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = standard → enumerate 20–30 roles.
   - T1-DEPTH-FLAG = deep → enumerate 50+ roles.

**Sub-step AREA-GROUPING:**
2. Group roles into area subdirectories under .roles/{area}/.
   Create minimum 2 area subdirectories.

**Sub-step IA-ANCHOR:**
3. Define inertia-advocate. Look up T2-PRESSURE in TABLE-A.
   Copy verbatim scope text as the scope field.

### Constraints

MUST set T3-ROLE-OUTCOME to exactly one composite value from [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST include inertia-advocate under .roles/.
MUST create minimum 2 area subdirectories.
MUST copy TABLE-A scope text verbatim for inertia-advocate.
FORBIDDEN: beginning sub-step AREA-GROUPING before completing sub-step COUNT.
FORBIDDEN: beginning sub-step IA-ANCHOR before completing sub-step AREA-GROUPING.
FORBIDDEN: beginning Phase 4 before the PHASE-3 record block is emitted.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: enum[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-IA-PRESSURE-KEY: enum[NONE | LOW | MODERATE | HIGH | CRITICAL]
===

**Boundary Guard — Phase 4 Inbound:**
FORBIDDEN: Phase 4 executes before the PHASE-3 record block above is emitted.

---

## PHASE 4 — Artifact Production

### Input Contract

MUST consume T2-PRESSURE from PHASE-2. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2. Valid: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T2-AP-REQUIRED from PHASE-2. Valid: enum[cat-2,cat-3 | cat-1,cat-4].
MUST consume T2-AP-FORBIDDEN from PHASE-2. Valid: enum[cat-1,cat-4 | cat-2,cat-3].
MUST consume T3-ROLE-OUTCOME from PHASE-3. Valid: enum[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST consume T3-IA-PRESSURE-KEY from PHASE-3. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
FORBIDDEN: executing Phase 4 before the PHASE-3 record block is emitted.

### Task Steps

**Sub-step ORG-CHART:**
1. Write org-chart.md using TABLE-C skeleton. Fill every [[ ]] slot.
   - [[T2-PRESSURE]] slot → value from PHASE-2 record block.
   - [[T2-VERDICT]] slot → value from PHASE-2 record block.
   - [[T3-AP-REQUIRED]] slots → categories from T2-AP-REQUIRED only.
   - Headcount table column order: Area | Headcount | Key Roles | Escalates | Decides.
   - Operating rhythm: minimum 3 rows. Quorum as N of M in all governance rows.
   - Committee charters: all 6 fields including quorum as N of M fraction.
   - Evolution Roadmap: Row 1 = headcount trigger; Row 2 = different category trigger.
   - Anti-Pattern citations: [[AP-NAME]] ([[CAT-N]]) — [[REASON]].
     Mitigation cells = remediation actions.

**Sub-step ROLE-FILES:**
2. Write one .roles/{area}/{role}.md per enumerated role.
   Every file includes: orientation, lens, expertise, scope, collaborates_with.
   Inertia-advocate scope = verbatim TABLE-A text keyed to T3-IA-PRESSURE-KEY.

### Constraints

MUST populate every [[ ]] slot in TABLE-C skeleton.
MUST include ASCII hierarchy minimum 2 levels.
MUST use Escalates-before-Decides column order in headcount table.
MUST include quorum as N of M in every governance charter.
MUST write FLAT-CASE-PRESSURE: [[T2-PRESSURE]] in inertia assessment.
MUST write exactly one verdict from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST include all five fields in every role file.
MUST write inertia-advocate scope verbatim from TABLE-A.
MUST select anti-pattern categories from T2-AP-REQUIRED only.
MUST write Mitigation cells as remediation actions.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in inertia assessment. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED in inertia assessment. Neither is an error.
FORBIDDEN: using categories from T2-AP-FORBIDDEN.
FORBIDDEN: writing Mitigation cells as format or column descriptions.
FORBIDDEN: using advisory language (should, prefer, consider, typically) in any constraint.
FORBIDDEN: beginning sub-step ROLE-FILES before completing sub-step ORG-CHART.
FORBIDDEN: any output after this phase before the PHASE-4 record block is emitted.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no subsequent output begins before this block is emitted.
T4-ORG-CHART: enum[WRITTEN | MISSING]
T4-ROLES-WRITTEN: enum[COMPLETE | INCOMPLETE]
T4-VERDICT-EMITTED: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-AP-COMPLIANCE: enum[COMPLIANT | NON-COMPLIANT]
===
```

---

## V-04 — Inertia Framing

**Axis:** Inertia framing — the inertia-advocate is declared as the anchor role before any other enumeration. All remaining roles are defined as "additional roles beyond the anchor." The preamble foregrounds inertia as the primary design concern of the entire skill. Phase 2 starts with IA-ANCHOR as sub-step 1 before COUNT.

**Hypothesis:** Foregrounding inertia forces the model to compute the IA scope before building the org, rather than treating inertia as an afterthought appended to an already-formed structure.

---

```markdown
org-build

The inertia-advocate is the first role defined in every org this skill produces.
All structural decisions — role count, area grouping, anti-pattern selection — derive
from the structural verdict, which is locked before enumeration begins.

Generate a complete org from scan results or directly from a repo.

Produces:
- org-chart.md — ASCII hierarchy, headcount-by-area table, operating rhythm,
  committee charters, inertia assessment, evolution roadmap, anti-pattern watch
- .roles/{area}/{role}.md — one file per role: orientation, lens,
  expertise, scope, collaborates_with. Inertia-advocate is always file zero.

Depth modes: standard (20–30 roles total including anchor) | deep (50+ roles)

---

## GLOBAL CONSTANTS

Declared once. Phase instructions reference by table name only.

### TABLE-A — Verbatim IA Scope Templates

The inertia-advocate scope field MUST contain the verbatim text matching T2-PRESSURE.
This is the anchor text from which the role's mandate is read. Paraphrase is FORBIDDEN.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Monitor the status-quo bias in decisions that appear purely technical. The org is flat and healthy; your role is early-warning, not structural intervention. Flag when a team resists decomposition without articulating a complexity justification. |
| LOW | Identify the one load-bearing assumption keeping the current structure in place and surface it at the next planning cycle. The org can operate flat but carries a known structural debt; your role is to name it explicitly so the team can decide consciously. |
| MODERATE | Audit two to three decision points per quarter where flat structure introduces coordination overhead above the threshold for a three-person team. Produce a pressure memo after each audit. The org is approaching the zone where structure becomes load-bearing. |
| HIGH | Run a full structural case at the next program boundary. The inertia load is above the operational threshold. Your role shifts from monitor to advocate: build the affirmative case for the structural change and present it with evidence to the decision committee. |
| CRITICAL | Initiate the structural transition immediately. Flat operation is no longer viable at this scale and coupling density. Your role is transition architect: own the migration path, the committee charter, and the first-90-days operating model for the new structure. |

### TABLE-B — Anti-Pattern Category Derivation

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## PHASE 1 — Input Gate

### Input Contract

_(No upstream phase.)_

### Task Steps

1. Read the provided repo or scan results.
2. Determine depth mode from the invocation flag.
3. Classify input source as repo or scan.

### Constraints

MUST set T1-DEPTH-FLAG to exactly one value from [standard | deep].
MUST set T1-SOURCE to exactly one value from [repo | scan].
FORBIDDEN: beginning Phase 2 before the PHASE-1 record block is emitted.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-SOURCE: [repo | scan]
===

**Boundary Guard — Phase 2 Inbound:**
FORBIDDEN: Phase 2 executes before the PHASE-1 record block above is emitted.

---

## PHASE 2 — Inertia Assessment

Phase 2 produces the verdict that determines the inertia-advocate's mandate text,
the anti-pattern category set, and the structural framing of org-chart.md.
This verdict is the primary gate output of this skill.

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1. Valid: [standard | deep].
MUST consume T1-SOURCE from PHASE-1. Valid: [repo | scan].
FORBIDDEN: executing Phase 2 before the PHASE-1 record block is emitted.

### Task Steps

**Sub-step SCAN:**
1. Examine repo or scan for structural signals: team size, coupling density,
   decision latency, escalation path length.

**Sub-step PRESSURE:**
2. Assign FLAT-CASE-PRESSURE from the closed set [NONE | LOW | MODERATE | HIGH | CRITICAL].

**Sub-step VERDICT:**
3. Derive T2-VERDICT. Apply exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
   Only one verdict. Both is an error. Neither is an error.

**Sub-step ANCHOR-SCOPE:**
4. Look up T2-PRESSURE in TABLE-A. Retrieve the verbatim scope text for the
   inertia-advocate. This text is the anchor from which the org is built.

### Constraints

MUST set T2-PRESSURE to exactly one value from [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST set T2-VERDICT to exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: beginning sub-step PRESSURE before completing sub-step SCAN.
FORBIDDEN: beginning sub-step VERDICT before completing sub-step PRESSURE.
FORBIDDEN: beginning sub-step ANCHOR-SCOPE before completing sub-step VERDICT.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED as T2-VERDICT. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED as T2-VERDICT. Neither is an error.
FORBIDDEN: enumerating any non-anchor roles before the PHASE-2 record block is emitted.
FORBIDDEN: beginning Phase 3 before the PHASE-2 record block is emitted.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-AP-REQUIRED: [cat-2,cat-3 | cat-1,cat-4]
T2-AP-FORBIDDEN: [cat-1,cat-4 | cat-2,cat-3]
T2-IA-GATE: FLAT-CASE-PRESSURE: {{T2-PRESSURE}}. VERDICT: {{T2-VERDICT}}.
            Only one verdict. Both is an error. Neither is an error.
===

**Boundary Guard — Phase 3 Inbound:**
FORBIDDEN: Phase 3 executes before the PHASE-2 record block above is emitted.

---

## PHASE 3 — Role Enumeration (Anchor-First)

Phase 3 opens with the inertia-advocate as the defined anchor role.
All remaining roles are enumerated as additional roles beyond the anchor.

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1. Valid: [standard | deep].
MUST consume T2-PRESSURE from PHASE-2. Valid: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2. Valid: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T2-AP-REQUIRED from PHASE-2. Valid: [cat-2,cat-3 | cat-1,cat-4].
FORBIDDEN: executing Phase 3 before the PHASE-2 record block is emitted.

### Task Steps

**Sub-step IA-ANCHOR (first):**
1. Define the inertia-advocate role as file zero under .roles/.
   Write scope field using verbatim text from TABLE-A keyed to T2-PRESSURE.
   All five fields required: orientation, lens, expertise, scope, collaborates_with.

**Sub-step COUNT:**
2. Enumerate additional roles beyond the anchor using T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = standard → enumerate 19–29 additional roles (total 20–30 including anchor).
   - T1-DEPTH-FLAG = deep → enumerate 49+ additional roles (total 50+ including anchor).

**Sub-step AREA-GROUPING:**
3. Group all roles including the anchor into area subdirectories.
   Create minimum 2 area subdirectories under .roles/{area}/.

**Sub-step CATEGORY-READ:**
4. Read TABLE-B using T2-VERDICT. Record required and FORBIDDEN categories for Phase 4.

### Constraints

MUST set T3-ROLE-OUTCOME to exactly one value from [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST write inertia-advocate in sub-step IA-ANCHOR before enumerating any other roles.
MUST copy TABLE-A scope text verbatim for inertia-advocate. Paraphrase is FORBIDDEN.
MUST create minimum 2 area subdirectories under .roles/.
FORBIDDEN: beginning sub-step COUNT before completing sub-step IA-ANCHOR.
FORBIDDEN: beginning sub-step AREA-GROUPING before completing sub-step COUNT.
FORBIDDEN: beginning sub-step CATEGORY-READ before completing sub-step AREA-GROUPING.
FORBIDDEN: beginning Phase 4 before the PHASE-3 record block is emitted.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-IA-PRESSURE-KEY: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-AP-REQUIRED: [cat-2,cat-3 | cat-1,cat-4]
T3-AP-FORBIDDEN: [cat-1,cat-4 | cat-2,cat-3]
===

**Boundary Guard — Phase 4 Inbound:**
FORBIDDEN: Phase 4 executes before the PHASE-3 record block above is emitted.

---

## PHASE 4 — Artifact Production

### Input Contract

MUST consume T2-PRESSURE from PHASE-2. Valid: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2. Valid: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T3-ROLE-OUTCOME from PHASE-3. Valid: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST consume T3-IA-PRESSURE-KEY from PHASE-3. Valid: [NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T3-AP-REQUIRED from PHASE-3. Valid: [cat-2,cat-3 | cat-1,cat-4].
MUST consume T3-AP-FORBIDDEN from PHASE-3. Valid: [cat-1,cat-4 | cat-2,cat-3].
FORBIDDEN: executing Phase 4 before the PHASE-3 record block is emitted.

### Task Steps

**Sub-step ORG-CHART:**
1. Write org-chart.md. The inertia assessment section MUST appear before the
   headcount table as the framing statement for the entire chart.
   Include:
   - Inertia assessment first: FLAT-CASE-PRESSURE: {{T2-PRESSURE}}.
     VERDICT: {{T2-VERDICT}}. Only one verdict. Both is an error. Neither is an error.
   - ASCII box/line hierarchy spanning minimum 2 org levels.
   - Headcount-by-area table: Area | Headcount | Key Roles | Decides | Escalates.
   - Operating rhythm table: ROB, shiproom, plus one governance meeting (minimum 3 rows).
     Each governance meeting gets a full charter with quorum as N of M.
   - Org Evolution Roadmap: Row 1 = headcount trigger; Row 2 = different category.
   - Anti-Pattern Watch: categories from T3-AP-REQUIRED only.
     Format citations as [element name] (cat-N) — {reason}.
     Mitigation cells = specific remediation actions.

**Sub-step ROLE-FILES:**
2. Write one .roles/{area}/{role}.md per role.
   The inertia-advocate file was drafted in Phase 3; write it out verbatim here.
   All additional role files include all five fields.

### Constraints

MUST position inertia assessment section before headcount table in org-chart.md.
MUST include ASCII hierarchy with minimum 2 levels.
MUST include Decides and Escalates columns in headcount table.
MUST include minimum 3 rows in operating rhythm table.
MUST include quorum as N of M in every governance charter.
MUST write all five charter fields per governance meeting.
MUST write FLAT-CASE-PRESSURE: {{T2-PRESSURE}} in inertia assessment.
MUST write exactly one verdict from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST include Evolution Roadmap with headcount trigger row and different-category trigger row.
MUST cite anti-patterns as [element name] (cat-N) — {reason}.
MUST write Mitigation cells as remediation actions.
MUST include all five fields in every role file.
MUST write inertia-advocate scope verbatim from TABLE-A.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in inertia assessment. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED in inertia assessment. Neither is an error.
FORBIDDEN: using categories from T3-AP-FORBIDDEN.
FORBIDDEN: writing Mitigation cells as format guidance.
FORBIDDEN: paraphrasing TABLE-A scope text in any role file.
FORBIDDEN: using advisory language (should, prefer, consider, typically) in any constraint.
FORBIDDEN: beginning sub-step ROLE-FILES before completing sub-step ORG-CHART.
FORBIDDEN: any output after this phase before the PHASE-4 record block is emitted.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no subsequent output begins before this block is emitted.
T4-ORG-CHART: [WRITTEN | MISSING]
T4-INERTIA-SECTION-POSITION: [FIRST | NOT-FIRST]
T4-ROLES-WRITTEN: [COMPLETE | INCOMPLETE]
T4-VERDICT-EMITTED: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-AP-COMPLIANCE: [COMPLIANT | NON-COMPLIANT]
===
```

---

## V-05 — Combined (Lifecycle + Output Format + Inertia Framing)

**Axes combined:**
- Lifecycle emphasis from V-01 (maximum boundary redundancy, verbose Input Contracts)
- Output format from V-03 (global skeleton TABLE-C, enum-typed record fields, Escalates-before-Decides)
- Inertia framing from V-04 (anchor-first sub-step ordering, inertia assessment section appears first in org-chart.md)

**Hypothesis:** Each axis independently reduces a failure mode; combining them targets all three simultaneously. The redundancy cost is low (prompt is longer) but the coverage gain is high.

---

```markdown
org-build

The inertia-advocate is the anchor role. All structural choices derive from the
locked verdict. The org-chart leads with the inertia assessment as framing context.

Generate a complete org from scan results or directly from a repo.

Produces:
- org-chart.md — inertia assessment first, then ASCII hierarchy, headcount-by-area
  table (Escalates | Decides order), operating rhythm, committee charters,
  evolution roadmap, anti-pattern watch
- .roles/{area}/{role}.md — one file per role with all five fields.
  Inertia-advocate is always enumerated first.

Depth modes: standard (20–30 roles) | deep (50+ roles via --depth deep)

---

## GLOBAL CONSTANTS

Declared once. Phase instructions reference by table name only.
No phase embeds any table's contents inline.

### TABLE-A — Verbatim IA Scope Templates

Inertia-advocate scope MUST contain verbatim text matching T2-PRESSURE.
Paraphrase is FORBIDDEN. Deviation of any kind fails C-17.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Monitor the status-quo bias in decisions that appear purely technical. The org is flat and healthy; your role is early-warning, not structural intervention. Flag when a team resists decomposition without articulating a complexity justification. |
| LOW | Identify the one load-bearing assumption keeping the current structure in place and surface it at the next planning cycle. The org can operate flat but carries a known structural debt; your role is to name it explicitly so the team can decide consciously. |
| MODERATE | Audit two to three decision points per quarter where flat structure introduces coordination overhead above the threshold for a three-person team. Produce a pressure memo after each audit. The org is approaching the zone where structure becomes load-bearing. |
| HIGH | Run a full structural case at the next program boundary. The inertia load is above the operational threshold. Your role shifts from monitor to advocate: build the affirmative case for the structural change and present it with evidence to the decision committee. |
| CRITICAL | Initiate the structural transition immediately. Flat operation is no longer viable at this scale and coupling density. Your role is transition architect: own the migration path, the committee charter, and the first-90-days operating model for the new structure. |

### TABLE-B — Anti-Pattern Category Derivation

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

### TABLE-C — Artifact Skeleton

Target shape for org-chart.md. Fill every [[SLOT: type]] from the corresponding
gate variable. A reader knowing only gate variable names MUST be able to fill every
slot without consulting any other section.

```
# Org Chart — [[REPO-NAME: string]]

## Inertia Assessment

FLAT-CASE-PRESSURE: [[T2-PRESSURE: NONE|LOW|MODERATE|HIGH|CRITICAL]]
VERDICT: [[T2-VERDICT: CAN-OPERATE-FLAT|STRUCTURE-WARRANTED]]
Only one verdict. Both is an error. Neither is an error.

## Hierarchy

[[ASCII-BOX-DIAGRAM: box-and-line, min 2 levels]]

## Headcount by Area

| Area | Headcount | Key Roles | Escalates | Decides |
|------|-----------|-----------|-----------|---------|
| [[AREA: string]] | [[N: int]] | [[ROLES: list]] | [[ESCALATES: string]] | [[DECIDES: string]] |

## Operating Rhythm

| Meeting | Cadence | Owner | Quorum |
|---------|---------|-------|--------|
| ROB | [[CAD: string]] | [[OWN: string]] | [[N of M: fraction]] |
| Shiproom | [[CAD: string]] | [[OWN: string]] | [[N of M: fraction]] |
| [[GOV: string]] | [[CAD: string]] | [[OWN: string]] | [[N of M: fraction]] |

### [[GOV]] Charter
- Name: [[GOV-NAME: string]]
- Cadence: [[GOV-CAD: string]]
- Owner: [[GOV-OWN: string]]
- Attendees: [[GOV-ATT: list]]
- Quorum: [[GOV-QUORUM: N of M]]
- Purpose: [[GOV-PURPOSE: string]]

## Org Evolution Roadmap

| Trigger | Trigger Type | Structural Change |
|---------|-------------|-------------------|
| [[TRIGGER-1: headcount-threshold]] | headcount | [[CHANGE-1: string]] |
| [[TRIGGER-2: non-headcount]] | [[TYPE-2: non-headcount-category]] | [[CHANGE-2: string]] |

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|--------------|----------|---------------------|------------|
| [[AP-NAME: string]] | [[CAT: T3-AP-REQUIRED]] | [[AP-NAME]] ([[CAT]]) — [[REASON: string]] | [[MIT: remediation-action]] |
```

---

## PHASE 1 — Input Gate

### Input Contract

_(No upstream phase. No prior gate variables required.)_

### Task Steps

1. Read the provided repo or scan results.
2. Determine depth mode from the invocation flag (--depth deep present or absent).
3. Classify input source type as repo or scan.

### Constraints

MUST set T1-DEPTH-FLAG to exactly one value from enum[standard | deep].
MUST set T1-SOURCE to exactly one value from enum[repo | scan].
FORBIDDEN: beginning Phase 2 before the PHASE-1 record block is emitted.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: enum[standard | deep]
T1-SOURCE: enum[repo | scan]
===

**Boundary Guard — Phase 2 Inbound:**
FORBIDDEN: Phase 2 executes before the PHASE-1 record block above is emitted.

---

## PHASE 2 — Inertia Assessment

This is the primary structural gate of this skill. The verdict it produces
determines the inertia-advocate scope text, anti-pattern categories, and the
framing statement that leads org-chart.md.

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid: enum[standard | deep].
MUST consume T1-SOURCE from PHASE-1 record block. Valid: enum[repo | scan].
FORBIDDEN: executing Phase 2 before the PHASE-1 record block is emitted.

### Task Steps

**Sub-step SCAN:**
1. Examine repo or scan for structural signals: team size, coupling density,
   decision latency indicators, escalation path length, communication topology.

**Sub-step PRESSURE:**
2. Assign FLAT-CASE-PRESSURE from the closed set in TABLE-A column T2-PRESSURE.
   Match observed signals to the closest tier.

**Sub-step VERDICT:**
3. Derive T2-VERDICT from the pressure rating.
   Produce exactly one value from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
   Only one verdict. Both is an error. Neither is an error.

**Sub-step ANCHOR-SCOPE:**
4. Look up T2-PRESSURE in TABLE-A. Retrieve the verbatim scope text.
   This text is the inertia-advocate scope value. It is set here, not in Phase 3.

**Sub-step CATEGORY-READ:**
5. Read TABLE-B using T2-VERDICT as key. Record required and FORBIDDEN categories.

### Constraints

MUST set T2-PRESSURE to exactly one value from enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST set T2-VERDICT to exactly one value from enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
FORBIDDEN: beginning sub-step PRESSURE before completing sub-step SCAN.
FORBIDDEN: beginning sub-step VERDICT before completing sub-step PRESSURE.
FORBIDDEN: beginning sub-step ANCHOR-SCOPE before completing sub-step VERDICT.
FORBIDDEN: beginning sub-step CATEGORY-READ before completing sub-step ANCHOR-SCOPE.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED as T2-VERDICT. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED as T2-VERDICT. Neither is an error.
FORBIDDEN: enumerating any role before the PHASE-2 record block is emitted.
FORBIDDEN: selecting anti-pattern categories before the PHASE-2 record block is emitted.
FORBIDDEN: beginning Phase 3 before the PHASE-2 record block is emitted.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: enum[NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-AP-REQUIRED: enum[cat-2,cat-3 | cat-1,cat-4]
T2-AP-FORBIDDEN: enum[cat-1,cat-4 | cat-2,cat-3]
T2-IA-GATE: FLAT-CASE-PRESSURE: [[T2-PRESSURE]]. VERDICT: [[T2-VERDICT]].
            Only one verdict. Both is an error. Neither is an error.
===

**Boundary Guard — Phase 3 Inbound:**
FORBIDDEN: Phase 3 executes before the PHASE-2 record block above is emitted.

---

## PHASE 3 — Role Enumeration (Anchor-First)

Phase 3 opens with the inertia-advocate as role zero before any additional roles
are enumerated. The anchor's scope text was locked in Phase 2; Phase 3 writes it out.

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid: enum[standard | deep].
MUST consume T2-PRESSURE from PHASE-2 record block. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2 record block. Valid: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T2-AP-REQUIRED from PHASE-2 record block. Valid: enum[cat-2,cat-3 | cat-1,cat-4].
MUST consume T2-AP-FORBIDDEN from PHASE-2 record block. Valid: enum[cat-1,cat-4 | cat-2,cat-3].
FORBIDDEN: executing Phase 3 before the PHASE-2 record block is emitted.

### Task Steps

**Sub-step IA-ANCHOR (first):**
1. Write the inertia-advocate role file as role zero under .roles/.
   Scope field: copy verbatim from TABLE-A using T2-PRESSURE as key.
   All five fields required: orientation, lens, expertise, scope, collaborates_with.

**Sub-step COUNT:**
2. Enumerate additional roles using T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = standard → enumerate 19–29 additional roles (total 20–30).
   - T1-DEPTH-FLAG = deep → enumerate 49+ additional roles (total 50+).

**Sub-step AREA-GROUPING:**
3. Group all roles including the anchor into area subdirectories.
   Create minimum 2 area subdirectories under .roles/{area}/.

### Constraints

MUST set T3-ROLE-OUTCOME to exactly one composite value from enum[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST write inertia-advocate as first role before any additional roles.
MUST copy TABLE-A scope text verbatim for inertia-advocate. Paraphrase is FORBIDDEN.
MUST create minimum 2 area subdirectories under .roles/.
FORBIDDEN: beginning sub-step COUNT before completing sub-step IA-ANCHOR.
FORBIDDEN: beginning sub-step AREA-GROUPING before completing sub-step COUNT.
FORBIDDEN: beginning Phase 4 before the PHASE-3 record block is emitted.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: enum[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-IA-PRESSURE-KEY: enum[NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-AP-REQUIRED: enum[cat-2,cat-3 | cat-1,cat-4]
T3-AP-FORBIDDEN: enum[cat-1,cat-4 | cat-2,cat-3]
===

**Boundary Guard — Phase 4 Inbound:**
FORBIDDEN: Phase 4 executes before the PHASE-3 record block above is emitted.

---

## PHASE 4 — Artifact Production

### Input Contract

MUST consume T1-DEPTH-FLAG from PHASE-1 record block. Valid: enum[standard | deep].
MUST consume T2-PRESSURE from PHASE-2 record block. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T2-VERDICT from PHASE-2 record block. Valid: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED].
MUST consume T3-ROLE-OUTCOME from PHASE-3 record block. Valid: enum[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS].
MUST consume T3-IA-PRESSURE-KEY from PHASE-3 record block. Valid: enum[NONE | LOW | MODERATE | HIGH | CRITICAL].
MUST consume T3-AP-REQUIRED from PHASE-3 record block. Valid: enum[cat-2,cat-3 | cat-1,cat-4].
MUST consume T3-AP-FORBIDDEN from PHASE-3 record block. Valid: enum[cat-1,cat-4 | cat-2,cat-3].
FORBIDDEN: executing Phase 4 before the PHASE-3 record block is emitted.

### Task Steps

**Sub-step ORG-CHART:**
1. Write org-chart.md using TABLE-C skeleton. Fill every [[SLOT]] from the
   corresponding gate variable or enumerated content.
   - Inertia Assessment section leads the document (first section after title).
     [[T2-PRESSURE]] → value from PHASE-2. [[T2-VERDICT]] → value from PHASE-2.
   - ASCII box/line hierarchy: minimum 2 org levels.
   - Headcount table column order: Area | Headcount | Key Roles | Escalates | Decides.
   - Operating rhythm: minimum 3 rows (ROB, shiproom, one governance meeting).
   - Each governance meeting charter: name, cadence, owner, attendees,
     quorum (as N of M fraction), purpose.
   - Org Evolution Roadmap: Row 1 = headcount trigger; Row 2 = different category trigger.
   - Anti-Pattern Watch: categories from T3-AP-REQUIRED only.
     Format: [[AP-NAME]] ([[CAT-N]]) — [[REASON]]. Mitigation = remediation action.

**Sub-step ROLE-FILES:**
2. Write one .roles/{area}/{role}.md per role.
   Every file includes all five fields.
   Inertia-advocate scope = verbatim TABLE-A text keyed to T3-IA-PRESSURE-KEY.

### Constraints

MUST position inertia assessment section as first section in org-chart.md.
MUST populate every [[SLOT]] in TABLE-C skeleton with a non-empty value.
MUST include ASCII hierarchy with minimum 2 org levels.
MUST use column order Area | Headcount | Key Roles | Escalates | Decides in headcount table.
MUST include minimum 3 rows in operating rhythm table.
MUST express quorum as N of M fraction in every governance charter row.
MUST include all six charter fields per governance meeting.
MUST write FLAT-CASE-PRESSURE: [[T2-PRESSURE]] in the inertia assessment section.
MUST write exactly one verdict from [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] in inertia assessment.
MUST include Org Evolution Roadmap with headcount trigger row and non-headcount trigger row.
MUST format anti-pattern citations as [element name] (cat-N) — {reason}.
MUST write Mitigation cells as specific remediation actions.
MUST include all five fields in every .roles/ file.
MUST write inertia-advocate scope verbatim from TABLE-A keyed to T3-IA-PRESSURE-KEY.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in inertia assessment. Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED in inertia assessment. Neither is an error.
FORBIDDEN: using anti-pattern categories from T3-AP-FORBIDDEN.
FORBIDDEN: writing Mitigation cells as format guidance or column descriptions.
FORBIDDEN: paraphrasing TABLE-A scope text in inertia-advocate role file.
FORBIDDEN: using advisory language (should, prefer, consider, typically) in any constraint context.
FORBIDDEN: beginning sub-step ROLE-FILES before completing sub-step ORG-CHART.
FORBIDDEN: any output after this phase before the PHASE-4 record block is emitted.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no subsequent output begins before this block is emitted.
T4-ORG-CHART: enum[WRITTEN | MISSING]
T4-IA-SECTION-POSITION: enum[FIRST | NOT-FIRST]
T4-ROLES-WRITTEN: enum[COMPLETE | INCOMPLETE]
T4-VERDICT-EMITTED: enum[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-AP-COMPLIANCE: enum[COMPLIANT | NON-COMPLIANT]
===
```

---

## Variation Summary

| Variation | Axis | Key Structural Difference | Hypothesis |
|-----------|------|--------------------------|------------|
| V-01 | Lifecycle emphasis | 4 phases; every boundary carries named outbound + inbound FORBIDDEN pair; maximum Input Contract verbosity | Redundant guards at every seam eliminate cross-phase contamination |
| V-02 | Role sequence | 3 phases; inertia assessment is Phase 1 (depth-gate demoted to sub-step 1a); T-variable prefixes shift throughout | Earlier structural lock forces all downstream choices to derive from a committed verdict |
| V-03 | Output format | TABLE-C skeleton declared as global constant; enum-typed record fields; Escalates-before-Decides column order | Pre-declaring the artifact shape as a constant eliminates mid-phase format improvisation |
| V-04 | Inertia framing | Anchor-first sub-step ordering in Phase 3 (IA-ANCHOR before COUNT); inertia assessment section leads org-chart.md | Foregrounding inertia forces scope derivation before structure-building begins |
| V-05 | Combined | V-01 boundary redundancy + V-03 typed skeleton + V-04 anchor-first ordering and leading section | Three independent failure modes addressed simultaneously; redundancy cost is prompt length |
