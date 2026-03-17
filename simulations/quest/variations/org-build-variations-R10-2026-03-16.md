Now I have full context on the existing org-chart.t3 baseline. Writing the 5 complete variations now.

---

# org-build — Round 10 Variations (V-01 through V-05)

**Single-axis**: Role Sequence (V-01), Output Format (V-02), Lifecycle Emphasis (V-03)  
**Combination**: Role Sequence × Lifecycle Emphasis (V-04), Output Format × Inertia Framing (V-05)

---

## Shared Reference Block (embedded verbatim in each variation)

**FLAT-CASE-PRESSURE closed set**: `LOW | MODERATE | ELEVATED | CRITICAL`  
**Verdict closed set**: `CAN-OPERATE-FLAT | STRUCTURE-WARRANTED`  
**Depth flag**: `standard` = 20–30 role files | `deep` = 50+ role files

**IA Scope Verbatim Templates** — copy the exact text for the rating. Paraphrase fails.

| Rating | Verbatim `scope` text |
|--------|----------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

**Anti-Pattern Category Matrix**

| Verdict | Required categories | FORBIDDEN categories |
|---------|--------------------|--------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

**Record Block Format**

```
=== RECORD: PHASE-N ===
VARIABLE-NAME: VALUE
...
=== END RECORD: PHASE-N ===
```

This construct simultaneously serves as the gate variable declaration, the ordering constraint anchor, and the materialization checkpoint. A reader who sees only this block MUST be able to derive: what typed outputs were declared, which phase boundary has been crossed, and that the checkpoint has been materialized.

---

## V-01 — Single-axis: Role Sequence

**Axis**: Area and role enumeration runs as the first phase before any structural verdict is computed. Role files are authored after the verdict is known.  
**Hypothesis**: Building the role inventory from evidence first grounds the structural assessment in concrete discovered roles rather than assumed org shapes, reducing synthetic role hallucination and tightening IA scope derivation.

---

You are running `org-build`. Produce two outputs: (1) `org-chart.md` at repo root, (2) `.craft/roles/{area}/{role}.md` for every role identified.

**PHASE BOUNDARY RULE — READ BEFORE WRITING ANYTHING**

Every phase ends by emitting a RECORD block. This block is the gate variable declaration, the ordering anchor, and the materialization checkpoint — unified in one construct. A phase is not complete until its RECORD block is present in the output.

FORBIDDEN: beginning any phase before the prior phase's RECORD block is present in the output.  
FORBIDDEN: beginning any phase before emitting the current phase's RECORD block at the boundary.

Both directions are independently enforced.

---

### Phase 1 — Area and Role Enumeration

Scan the input (scan results, repo, or spec). Enumerate functional areas and candidate roles without assessing structure.

MUST produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description]`. If no role files exist, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` instead.

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block assigning each role exactly one type from: `Engineering | PM | Design | Operations | Research | Other`. MUST follow three-tier ordering: Engineering first, then Operations, then remaining types. FORBIDDEN: interleaving tiers.

Determine depth flag: `standard` unless `--depth deep` is passed or signal count exceeds 40.

MUST enumerate at least one role with `inertia` or `advocate` in its name.

**FORBIDDEN: beginning Phase 2 before emitting this RECORD block:**

```
=== RECORD: PHASE-1 ===
T1-AREAS: [comma-separated area names]
T1-ROLE-LIST: [comma-separated role names]
T1-ROLE-COUNT: [integer]
T1-DEPTH-FLAG: standard | deep
=== END RECORD: PHASE-1 ===
```

---

### Phase 2 — Structural Assessment

**Input contract — FORBIDDEN: executing Phase 2 before RECORD: PHASE-1 is emitted.**  
MUST read: T1-AREAS, T1-ROLE-COUNT from RECORD: PHASE-1.

Run the four-sub-section inertia assessment in this exact order:

**Sub-section 1 — Case for Staying Flat**: Produce a three-column mechanism evidence table (`Mechanism Name | Type | Frequency / Participants`). Type MUST come from: `Channel | Informal Role | Recurring Cadence | Shared Artifact`. MUST include at least 2 data rows. After counting rows, emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---` FORBIDDEN: beginning Sub-section 2 before this separator.

**Sub-section 2 — How We Coordinate Today**: Inventory active coordination patterns. FORBIDDEN: re-listing entries from the Sub-section 1 table.

**Sub-section 3 — Rebuttal**: Name one specific coordination failure the flat structure cannot resolve. MUST reference an observable: a blocked decision, missed SLA, knowledge silo, or competing roadmap. FORBIDDEN: writing "the team is growing" without naming the failure mode.

**Sub-section 4 — VERDICT**: MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one sentence citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`. Rating MUST be exactly one of: `LOW | MODERATE | ELEVATED | CRITICAL`.

Then write exactly one verdict. FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error. FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.

**FORBIDDEN: beginning Phase 3 before emitting this RECORD block:**

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: LOW | MODERATE | ELEVATED | CRITICAL
T2-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED
=== END RECORD: PHASE-2 ===
```

---

### Phase 3 — Role File Authoring

**Input contract — FORBIDDEN: executing Phase 3 before RECORD: PHASE-1 and RECORD: PHASE-2 are both emitted.**  
MUST read: T1-ROLE-LIST, T1-AREAS from RECORD: PHASE-1. MUST read: T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2.

Write one `.craft/roles/{area}/{role}.md` per role in T1-ROLE-LIST. MUST group files by area subdir.

**Each role file MUST contain exactly these five fields** — missing any field in any file is a hard failure:

```yaml
orientation: [contributor | manager | lead | executive]
lens:         [primary analytical frame]
expertise:    [domain knowledge held]
scope:        [boundaries of decision authority]
collaborates_with: [comma-separated role names]
```

**inertia-advocate `scope` field — verbatim copy from the IA Scope Template keyed to T2-PRESSURE.** Paraphrase fails. Derivation from the rating is necessary but not sufficient — the exact template text MUST appear verbatim:

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

**FORBIDDEN: beginning Phase 4 before emitting this RECORD block:**

```
=== RECORD: PHASE-3 ===
T3-ROLE-COUNT: [actual count of files written]
T3-IA-PRESENT: yes | no
T3-AREAS: [comma-separated area subdir names]
=== END RECORD: PHASE-3 ===
```

---

### Phase 4 — Org Chart Authoring

**Input contract — FORBIDDEN: executing Phase 4 before RECORD: PHASE-2 and RECORD: PHASE-3 are both emitted.**  
MUST read: T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. MUST read: T3-AREAS, T3-ROLE-COUNT from RECORD: PHASE-3.

Write `org-chart.md` with sections in this exact order:

**1 — ASCII Hierarchy Diagram**: MUST show at minimum 2 org levels. MUST use box-and-line ASCII. Flat name list fails.

**2 — Headcount by Area**: Table with columns `Area | Headcount | Key Roles | Decides | Escalates`. FORBIDDEN: merging Decides and Escalates into one column. MUST include `**Total**` row.

**3 — Operating Rhythm**: Table with columns `Cadence | Frequency | DRI / Owner | Purpose`. MUST include 3+ distinct rows covering ROB, shiproom, and at least one governance meeting. FORBIDDEN: combining two meetings into one row.

**4 — Committee Charters**: One charter per governance meeting. Each MUST include all five fields: `Name`, `Cadence`, `Owner`, `Members`, `Quorum`. Quorum MUST use format: `N of M` (e.g., `4 of 7`). FORBIDDEN: short-form quorum.

**5 — Inertia Assessment Summary**: MUST contain `FLAT-CASE-PRESSURE: [T2-PRESSURE value]` on its own line, then exactly one of:  
`CAN-OPERATE-FLAT: [one-sentence rationale referencing T2-PRESSURE]`  
`STRUCTURE-WARRANTED: [one-sentence rationale referencing T2-PRESSURE]`  
FORBIDDEN: writing both. Both is an error. FORBIDDEN: omitting both. Neither is an error.

**6 — ORG-ELEMENT REGISTER**: MUST appear before Org Evolution Roadmap. Four category entries required:  
`cat-1 (Areas)` — each area as `- [name] — headcount: [N]`  
`cat-2 (Committees/Cadences)` — each meeting as `- [name]`  
`cat-3 (Headcount)` — total as `- Total headcount: [N]`  
`cat-4 (DRI Roles)` — each DRI as `- [role name]`

**7 — Anti-Pattern Watch**: Derive required and FORBIDDEN categories from T2-VERDICT using the Anti-Pattern Category Matrix. Every `Why It Applies Here` cell MUST open with `[element name] (cat-N) —` syntax. MUST use MUST or FORBIDDEN in every Mitigation cell — advisory language fails. Every Mitigation cell MUST contain a specific remediation action. Descriptive format guidance fails.

| T2-VERDICT | Required | FORBIDDEN |
|-----------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: using cat-1 or cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: using cat-2 or cat-3 |

**8 — Org Evolution Roadmap**: Table with columns `Trigger | Category | Structural Change`. MUST include 2+ rows. Row 1 MUST be a headcount threshold. Row 2 MUST be a different category (workload signal, structural symptom, or milestone event). FORBIDDEN: two headcount thresholds.

**9 — Pre-print Skeleton**: Fill this template verbatim with gate variable values:

```
ORG-BUILD RESULT SUMMARY
Topic: {{TOPIC}}
Date: {{DATE}}
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Role count: {{T3-ROLE-COUNT}}
Areas: {{T3-AREAS}}
IA scope template applied: {{T3-IA-PRESENT}}
```

**FORBIDDEN: beginning Phase 5 before emitting this RECORD block:**

```
=== RECORD: PHASE-4 ===
T4-ORG-CHART-WRITTEN: yes | no
T4-SECTIONS-COMPLETE: [count of sections written]
=== END RECORD: PHASE-4 ===
```

---

### Phase 5 — Validation

**Input contract — FORBIDDEN: executing Phase 5 before all RECORD blocks PHASE-1 through PHASE-4 are emitted.**

Verify:
- T3-ROLE-COUNT is within range for T1-DEPTH-FLAG (standard: 20–30, deep: 50+). Below lower bound fails.
- T3-IA-PRESENT = yes. Absent inertia-advocate fails.
- T2-PRESSURE is exactly one of `LOW | MODERATE | ELEVATED | CRITICAL`.
- T2-VERDICT is exactly one of `CAN-OPERATE-FLAT | STRUCTURE-WARRANTED`.

If any check fails, emit `VALIDATION-FAILED: [reason]` and stop. Do not produce partial output.

---

## V-02 — Single-axis: Output Format (Table-Dominant)

**Axis**: Every requirement and every output section is expressed as a table. Phase specifications use `Phase | Input Contract | Output Variables | Guard` tables. Role files use a field-value table internally. The inertia assessment mechanism evidence is the primary organizing table.  
**Hypothesis**: Forcing uniform tabular format makes field-completeness checkable at a glance and reduces missing-field failures across C-02, C-05, C-07.

---

You are running `org-build`. Produce two outputs: (1) `org-chart.md`, (2) `.craft/roles/{area}/{role}.md` for every role.

**PHASE MAP** — execute phases in row order. FORBIDDEN: beginning any phase before all prior phases' RECORD blocks are emitted.

| Phase | Name | Key Input Variables | Key Output Variables | Guard |
|-------|------|--------------------|--------------------|-------|
| 1 | Role Inventory | (scan input) | T1-AREAS, T1-ROLE-LIST, T1-ROLE-COUNT, T1-DEPTH-FLAG | FORBIDDEN: beginning Phase 2 before RECORD: PHASE-1 emitted. FORBIDDEN: executing Phase 2 without reading T1-AREAS, T1-ROLE-COUNT. |
| 2 | Structural Assessment | T1-AREAS, T1-ROLE-COUNT | T2-PRESSURE, T2-VERDICT | FORBIDDEN: beginning Phase 3 before RECORD: PHASE-2 emitted. FORBIDDEN: executing Phase 3 without reading T2-PRESSURE, T2-VERDICT. |
| 3 | Role File Authoring | T1-ROLE-LIST, T2-PRESSURE, T2-VERDICT | T3-ROLE-COUNT, T3-IA-PRESENT, T3-AREAS | FORBIDDEN: beginning Phase 4 before RECORD: PHASE-3 emitted. FORBIDDEN: executing Phase 4 without reading T3-AREAS, T3-ROLE-COUNT. |
| 4 | Org Chart Authoring | T2-PRESSURE, T2-VERDICT, T3-AREAS | T4-SECTIONS-COMPLETE | FORBIDDEN: beginning Phase 5 before RECORD: PHASE-4 emitted. |
| 5 | Validation | All prior RECORD blocks | (pass/fail) | FORBIDDEN: executing validation before all prior RECORD blocks present. |

After completing each phase, emit:

```
=== RECORD: PHASE-N ===
[variable]: [value]
...
=== END RECORD: PHASE-N ===
```

This block is simultaneously the gate variable declaration, the ordering constraint anchor, and the materialization checkpoint.

---

**Phase 1 — Role Inventory**

Scan input. Produce `ROLES-LOADED:` or `ROLES-NOTE:` block (one role per line: `- [name] — [description]`). Then produce `ROLE-TYPE-CLASSIFICATION:` assigning each role one type from `Engineering | PM | Design | Operations | Research | Other`. Apply three-tier ordering: Engineering first, Operations second, remaining types last. FORBIDDEN: interleaving tiers.

Determine depth flag: `standard` unless `--depth deep` or signal count > 40. MUST include at least one `inertia` or `advocate` role.

**Role Type Summary Table** (emit after ROLE-TYPE-CLASSIFICATION):

| Domain Type | Roles |
|-------------|-------|
| Engineering | [list] |
| PM | [list] |
| Design | [list] |
| Operations | [list] |
| Research | [list] |
| Other | [list] |

Emit RECORD: PHASE-1 with T1-AREAS, T1-ROLE-LIST, T1-ROLE-COUNT, T1-DEPTH-FLAG.

---

**Phase 2 — Structural Assessment**

**Input contract**: MUST read T1-AREAS, T1-ROLE-COUNT from RECORD: PHASE-1. FORBIDDEN: executing Phase 2 before RECORD: PHASE-1 emitted.

**Mechanism Evidence Table** (Sub-section 1 — Case for Staying Flat):

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type MUST come from: `Channel | Informal Role | Recurring Cadence | Shared Artifact`. MUST include 2+ data rows. After reaching 2 rows, emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

**Coordination Inventory Table** (Sub-section 2):

| Pattern | Channel/Cadence/Artifact | Frequency | Participants |
|---------|--------------------------|-----------|--------------|

FORBIDDEN: re-listing rows from the Mechanism Evidence Table.

**Rebuttal** (Sub-section 3): Name one specific coordination failure with observable evidence. FORBIDDEN: "the team is growing" without naming the failure mode.

**Verdict Table** (Sub-section 4):

| Dimension | Value |
|-----------|-------|
| FLAT-CASE-PRESSURE | LOW \| MODERATE \| ELEVATED \| CRITICAL |
| Justification | [cites mechanism count + failure mode] |
| VERDICT | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |
| Re-assessment Trigger | [concrete named threshold] |

FORBIDDEN: writing both verdict values. Both is an error. FORBIDDEN: omitting both. Neither is an error.

Emit RECORD: PHASE-2 with T2-PRESSURE, T2-VERDICT.

---

**Phase 3 — Role File Authoring**

**Input contract**: MUST read T1-ROLE-LIST, T1-AREAS from RECORD: PHASE-1. MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. FORBIDDEN: executing Phase 3 before both RECORD blocks emitted.

Write `.craft/roles/{area}/{role}.md` for every role in T1-ROLE-LIST. MUST group by area subdir. Each file uses this field-value format:

```
| Field | Value |
|-------|-------|
| orientation | [contributor \| manager \| lead \| executive] |
| lens | [primary analytical frame] |
| expertise | [domain knowledge] |
| scope | [decision authority boundaries] |
| collaborates_with | [comma-separated role names] |
```

MISSING any field in any file is a hard failure.

**inertia-advocate `scope` field**: MUST be the verbatim text from the IA Scope Template keyed to T2-PRESSURE. Copy exact text — do not paraphrase:

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

Emit RECORD: PHASE-3 with T3-ROLE-COUNT, T3-IA-PRESENT, T3-AREAS.

---

**Phase 4 — Org Chart Authoring**

**Input contract**: MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. MUST read T3-AREAS, T3-ROLE-COUNT from RECORD: PHASE-3. FORBIDDEN: executing Phase 4 before RECORD: PHASE-2 and RECORD: PHASE-3 emitted.

Write `org-chart.md` with these sections expressed as tables where possible:

**ASCII Hierarchy Diagram**: MUST show 2+ levels. Box-and-line format. Flat name list fails.

**Headcount Table**: `Area | Headcount | Key Roles | Decides | Escalates`. FORBIDDEN: merging Decides/Escalates. MUST include `**Total**` row.

**Operating Rhythm Table**: `Cadence | Frequency | DRI / Owner | Purpose`. MUST include 3+ rows: ROB + shiproom + governance. FORBIDDEN: combining two meetings into one row.

**Committee Charters Table**: One row per governance meeting:

| Field | Value |
|-------|-------|
| Name | |
| Cadence | |
| Owner | |
| Members | |
| Quorum | N of M |

FORBIDDEN: omitting any field. FORBIDDEN: short-form quorum (must be N of M fraction).

**Inertia Summary Table**:

| Dimension | Value |
|-----------|-------|
| FLAT-CASE-PRESSURE | {{T2-PRESSURE}} |
| VERDICT | {{T2-VERDICT}} |

FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in VERDICT. FORBIDDEN: leaving VERDICT blank.

**ORG-ELEMENT REGISTER Table**:

| Category | Elements |
|----------|---------|
| cat-1 (Areas) | [area — headcount: N, ...] |
| cat-2 (Committees/Cadences) | [names] |
| cat-3 (Headcount) | Total: [N] |
| cat-4 (DRI Roles) | [role names] |

**Anti-Pattern Watch Table**: `Anti-Pattern | Why It Applies Here | Mitigation`. Every `Why It Applies Here` cell MUST open with `[element name] (cat-N) —`. Every Mitigation MUST use MUST or FORBIDDEN and contain a remediation action. Derive categories from T2-VERDICT:

| T2-VERDICT | MUST USE | FORBIDDEN |
|-----------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 — FORBIDDEN |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 — FORBIDDEN |

**Org Evolution Roadmap Table**: `Trigger | Category | Structural Change`. Row 1: headcount threshold. Row 2: different category. FORBIDDEN: two headcount thresholds.

**Pre-print Skeleton**:

```
ORG-BUILD RESULT SUMMARY
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Role count: {{T3-ROLE-COUNT}}
Areas: {{T3-AREAS}}
IA scope template applied: {{T3-IA-PRESENT}}
```

Emit RECORD: PHASE-4 with T4-SECTIONS-COMPLETE.

---

**Phase 5 — Validation**: FORBIDDEN: executing Phase 5 before all prior RECORD blocks emitted. Verify T3-ROLE-COUNT within depth range (standard: 20–30, deep: 50+). Verify T3-IA-PRESENT = yes. Verify T2-PRESSURE is one of the closed set. Verify T2-VERDICT is exactly one value. Any failure emits `VALIDATION-FAILED:` and stops.

---

## V-03 — Single-axis: Lifecycle Emphasis (Double-Guard as Primary Structure)

**Axis**: The record block construct definition and the double-guard pattern are introduced in the preamble, before any content guidance. Every phase section leads with its inbound guard before stating content requirements, and closes with its outbound guard before the RECORD block.  
**Hypothesis**: Foregrounding phase discipline constraints before content constraints makes models less likely to skip record blocks when generating long outputs — the ordering FORBIDDEN fires before the model reaches any output section.

---

You are running `org-build`. Produce: (1) `org-chart.md`, (2) `.craft/roles/{area}/{role}.md` for every role.

**THE RECORD BLOCK CONSTRUCT — READ BEFORE ANY OTHER INSTRUCTION**

Every phase boundary is governed by one construct: the `=== RECORD ===` block. This block unifies three properties:

1. **Gate variable declaration** — the named typed variables produced by this phase are declared here and nowhere else.
2. **Ordering constraint anchor** — the `FORBIDDEN: beginning the next phase` instruction is anchored to this block's presence. The ordering FORBIDDEN fires at the moment this block is emitted (outbound) and at the moment the consuming phase reads it (inbound).
3. **Materialization checkpoint** — this block is the auditable record that this phase completed. A gate variable appearing only in a prose sentence fails; it MUST appear here.

A reader who sees only the `=== RECORD: PHASE-N ===` block MUST be able to derive: (a) which typed outputs were declared, (b) that Phase N is complete, (c) that Phase N+1 is now authorized to begin. These three properties are inseparable and MUST be derivable from the record block alone without cross-referencing.

**FORMAT**:
```
=== RECORD: PHASE-N ===
VARIABLE-NAME: VALUE
...
=== END RECORD: PHASE-N ===
```

**DOUBLE-GUARD AT EVERY PHASE BOUNDARY**: Every transition carries two orthogonal FORBIDDENs:
- **Outbound** (at the gate): `FORBIDDEN: beginning Phase N+1 before this RECORD block is emitted.`
- **Inbound** (at the consuming phase): `FORBIDDEN: executing Phase N+1 before Phase N RECORD block is emitted.`

A guard in only one direction — outbound only or inbound only — fails. Both are required.

---

**Phase 1 — Role Inventory**

**Inbound guard — FORBIDDEN: executing Phase 1 before reading this instruction.** (Phase 1 has no prior gate; this is the unconditional entry point.)

Scan input. Produce `ROLES-LOADED:` block (`- [name] — [description]` per role), or `ROLES-NOTE:` if no role files exist. Produce `ROLE-TYPE-CLASSIFICATION:` block assigning each role one type from `Engineering | PM | Design | Operations | Research | Other`. MUST apply three-tier order: Engineering first, Operations second, remaining last. FORBIDDEN: interleaving tiers. MUST include at least one `inertia` or `advocate` role. Determine depth flag: `standard` (default) or `deep` (if `--depth deep` or signal count > 40).

**Outbound guard — FORBIDDEN: beginning Phase 2 before emitting this RECORD block.**

```
=== RECORD: PHASE-1 ===
T1-AREAS: [comma-separated]
T1-ROLE-LIST: [comma-separated]
T1-ROLE-COUNT: [integer]
T1-DEPTH-FLAG: standard | deep
=== END RECORD: PHASE-1 ===
```

---

**Phase 2 — Structural Assessment**

**Inbound guard — FORBIDDEN: executing Phase 2 before RECORD: PHASE-1 is emitted.** MUST read T1-AREAS, T1-ROLE-COUNT from RECORD: PHASE-1 before writing any content in this phase.

Run inertia assessment in four sub-sections:

**Sub-section 1**: Mechanism evidence table (`Mechanism Name | Type | Frequency / Participants`). Type from closed set: `Channel | Informal Role | Recurring Cadence | Shared Artifact`. MUST have 2+ data rows. After reaching 2 rows, emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows.] ---` FORBIDDEN: beginning Sub-section 2 before this separator.

**Sub-section 2**: Coordination inventory. FORBIDDEN: re-listing Sub-section 1 entries.

**Sub-section 3**: Rebuttal — name one specific coordination failure with observable evidence. FORBIDDEN: "the team is growing" without naming the failure mode.

**Sub-section 4 — VERDICT**: MUST open with `FLAT-CASE-PRESSURE: [rating] — [one sentence]`. Rating MUST be exactly one of `LOW | MODERATE | ELEVATED | CRITICAL`. Then write exactly one verdict:

FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error.  
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.

Write re-assessment trigger citing a concrete named threshold. FORBIDDEN: "revisit as the team grows."

**Outbound guard — FORBIDDEN: beginning Phase 3 before emitting this RECORD block.**

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: LOW | MODERATE | ELEVATED | CRITICAL
T2-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED
=== END RECORD: PHASE-2 ===
```

---

**Phase 3 — Role File Authoring**

**Inbound guard — FORBIDDEN: executing Phase 3 before RECORD: PHASE-1 and RECORD: PHASE-2 are both emitted.** MUST read T1-ROLE-LIST, T1-AREAS from RECORD: PHASE-1. MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2 before writing any role file.

Write `.craft/roles/{area}/{role}.md` per role in T1-ROLE-LIST. MUST group by area subdir. Each file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Missing any field in any file is a hard failure.

**inertia-advocate `scope` field**: MUST be verbatim text from the template keyed to T2-PRESSURE. Copy exactly. Paraphrase fails:

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

**Outbound guard — FORBIDDEN: beginning Phase 4 before emitting this RECORD block.**

```
=== RECORD: PHASE-3 ===
T3-ROLE-COUNT: [count]
T3-IA-PRESENT: yes | no
T3-AREAS: [comma-separated subdir names]
=== END RECORD: PHASE-3 ===
```

---

**Phase 4 — Org Chart Authoring**

**Inbound guard — FORBIDDEN: executing Phase 4 before RECORD: PHASE-2 and RECORD: PHASE-3 are both emitted.** MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. MUST read T3-AREAS, T3-ROLE-COUNT from RECORD: PHASE-3.

Write `org-chart.md`. Sections in order:

1. **ASCII Hierarchy**: 2+ levels, box-and-line. Flat list fails.
2. **Headcount by Area**: `Area | Headcount | Key Roles | Decides | Escalates`. Both Decides and Escalates required. Total row required.
3. **Operating Rhythm**: `Cadence | Frequency | DRI / Owner | Purpose`. 3+ rows: ROB + shiproom + governance. FORBIDDEN: combining meetings.
4. **Committee Charters**: One per governance meeting. MUST include: Name, Cadence, Owner, Members, Quorum as `N of M`. FORBIDDEN: short-form quorum.
5. **Inertia Summary**: `FLAT-CASE-PRESSURE: [T2-PRESSURE]` then exactly one verdict line. FORBIDDEN: both. FORBIDDEN: neither.
6. **ORG-ELEMENT REGISTER**: cat-1 (Areas), cat-2 (Committees/Cadences), cat-3 (Headcount), cat-4 (DRI Roles). MUST appear before Org Evolution Roadmap.
7. **Anti-Pattern Watch**: `Anti-Pattern | Why It Applies Here | Mitigation`. Every `Why It Applies Here` cell MUST open with `[element name] (cat-N) —`. MUST use MUST or FORBIDDEN in every Mitigation. Every Mitigation MUST contain a remediation action — not format guidance. Apply category matrix:

| T2-VERDICT | MUST use | FORBIDDEN |
|-----------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

8. **Org Evolution Roadmap**: Row 1: headcount threshold. Row 2: different category. FORBIDDEN: two headcount rows.
9. **Pre-print Skeleton**: Fill verbatim: `FLAT-CASE-PRESSURE: {{T2-PRESSURE}}`, `VERDICT: {{T2-VERDICT}}`, `Role count: {{T3-ROLE-COUNT}}`, `Areas: {{T3-AREAS}}`, `IA scope template applied: {{T3-IA-PRESENT}}`.

**Outbound guard — FORBIDDEN: beginning Phase 5 before emitting this RECORD block.**

```
=== RECORD: PHASE-4 ===
T4-ORG-CHART-WRITTEN: yes | no
T4-SECTIONS-COMPLETE: [count]
=== END RECORD: PHASE-4 ===
```

---

**Phase 5 — Validation**

**Inbound guard — FORBIDDEN: executing Phase 5 before RECORD: PHASE-1, PHASE-2, PHASE-3, and PHASE-4 are all emitted.**

Verify: T3-ROLE-COUNT within depth range (standard 20–30, deep 50+). T3-IA-PRESENT = yes. T2-PRESSURE is one closed-set value. T2-VERDICT is exactly one value. T4-ORG-CHART-WRITTEN = yes. Any failure: emit `VALIDATION-FAILED: [reason]` and stop.

---

## V-04 — Combination: Role Sequence × Lifecycle Emphasis

**Axis**: Bottom-up area-first enumeration (V-01) combined with foregrounded double-guard phase discipline (V-03).  
**Hypothesis**: Starting with discovered role inventory (not assumed structure) while enforcing strict bidirectional gate guards produces the most coherent IA scope derivation — the verdict is grounded in actual roles and the template is applied at a clearly marked phase boundary.

---

You are running `org-build`. Produce: (1) `org-chart.md`, (2) `.craft/roles/{area}/{role}.md`.

**THE RECORD BLOCK AS UNIFIED CONSTRUCT — HIGHEST PRIORITY INSTRUCTION**

Before reading any other instruction, internalize this:

The `=== RECORD: PHASE-N ===` block is not a summary. It is a contract. It simultaneously declares gate variables (what was produced), anchors the ordering constraint (what is now permitted), and materializes the checkpoint (that this phase completed). You MUST be able to derive all three from the block definition alone. Any gate variable that appears only in prose — not in a RECORD block — is undeclared. Any phase that begins before reading the prior RECORD block has broken contract.

**EVERY phase boundary carries TWO orthogonal FORBIDDENs**:

- One outbound at the emitting gate: `FORBIDDEN: beginning Phase N+1 before emitting this RECORD block.`
- One inbound at the consuming phase: `FORBIDDEN: executing Phase N+1 before Phase N RECORD block is emitted.`

A guard in only one direction fails. Both are required at every boundary.

---

**Phase 1 — Area-First Role Discovery**

**Inbound**: Unconditional entry point.

The discovery-before-verdict order is intentional. Do not assess structure until role evidence is enumerated. This grounds the structural verdict in what actually exists, not in convention.

Scan input for role and functional area signals. For each signal, record the area and candidate role. Produce `ROLES-LOADED:` (or `ROLES-NOTE:` if no files exist). Produce `ROLE-TYPE-CLASSIFICATION:` in three-tier order: Engineering → Operations → remaining. FORBIDDEN: interleaving tiers. MUST include at least one `inertia` or `advocate` role. Assign depth flag: `standard` (default, 20–30 roles) or `deep` (50+ roles if explicitly flagged or signal count > 40).

**Outbound — FORBIDDEN: beginning Phase 2 before emitting:**

```
=== RECORD: PHASE-1 ===
T1-AREAS: [comma-separated area names]
T1-ROLE-LIST: [comma-separated role names, grounded in scan evidence]
T1-ROLE-COUNT: [integer]
T1-DEPTH-FLAG: standard | deep
=== END RECORD: PHASE-1 ===
```

---

**Phase 2 — Structural Verdict**

**Inbound — FORBIDDEN: executing Phase 2 before RECORD: PHASE-1 is emitted.** MUST read T1-AREAS, T1-ROLE-COUNT from RECORD: PHASE-1 before writing any content.

The structural verdict MUST be derived from the enumerated role evidence in RECORD: PHASE-1 — not from assumed org patterns.

Four-sub-section inertia assessment:

**Sub-section 1**: Mechanism evidence table (`Mechanism Name | Type | Frequency / Participants`). Type from: `Channel | Informal Role | Recurring Cadence | Shared Artifact`. 2+ rows. After row count ≥ 2: emit `--- [FLAT-CASE-CLOSED: {N} rows.] ---` FORBIDDEN: Sub-section 2 before this separator.

**Sub-section 2**: Coordination inventory. FORBIDDEN: re-listing Sub-section 1 entries.

**Sub-section 3**: Rebuttal — observable coordination failure. FORBIDDEN: generic growth language.

**Sub-section 4**: MUST open with `FLAT-CASE-PRESSURE: [rating] — [justification citing T1 evidence]`. Rating: `LOW | MODERATE | ELEVATED | CRITICAL`. Then exactly one verdict.

FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error.  
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.

**Outbound — FORBIDDEN: beginning Phase 3 before emitting:**

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: LOW | MODERATE | ELEVATED | CRITICAL
T2-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED
=== END RECORD: PHASE-2 ===
```

---

**Phase 3 — Role File Authoring**

**Inbound — FORBIDDEN: executing Phase 3 before RECORD: PHASE-1 and RECORD: PHASE-2 are both emitted.** MUST read T1-ROLE-LIST from RECORD: PHASE-1. MUST read T2-PRESSURE from RECORD: PHASE-2 before writing any file.

The order matters: role files are authored after the verdict so the inertia-advocate `scope` can be derived from T2-PRESSURE.

Write `.craft/roles/{area}/{role}.md` per role. Group by area subdir. Every file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Missing any field is a hard failure.

**inertia-advocate `scope`**: MUST be verbatim text from the template keyed to T2-PRESSURE:

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

Derivation is necessary; verbatim copy is required. Any paraphrase fails.

**Outbound — FORBIDDEN: beginning Phase 4 before emitting:**

```
=== RECORD: PHASE-3 ===
T3-ROLE-COUNT: [count]
T3-IA-PRESENT: yes | no
T3-AREAS: [comma-separated subdirs]
=== END RECORD: PHASE-3 ===
```

---

**Phase 4 — Org Chart Authoring**

**Inbound — FORBIDDEN: executing Phase 4 before RECORD: PHASE-2 and RECORD: PHASE-3 are both emitted.** MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. MUST read T3-AREAS, T3-ROLE-COUNT from RECORD: PHASE-3.

Write `org-chart.md`. Produce sections in this order — FORBIDDEN: producing any section before its predecessor:

1. ASCII hierarchy (2+ levels, box-and-line, flat list fails)
2. Headcount by area (`Area | Headcount | Key Roles | Decides | Escalates`, Total row required)
3. Operating rhythm (3+ rows: ROB + shiproom + governance, FORBIDDEN: combining meetings)
4. Committee charters (one per governance meeting; Name, Cadence, Owner, Members, Quorum as N of M; FORBIDDEN: omitting any field)
5. Inertia summary (`FLAT-CASE-PRESSURE: [T2-PRESSURE]` + exactly one verdict; FORBIDDEN: both; FORBIDDEN: neither)
6. ORG-ELEMENT REGISTER (cat-1 through cat-4; MUST appear before Org Evolution Roadmap)
7. Anti-Pattern Watch (typed cat-N citations in every `Why It Applies Here`; MUST/FORBIDDEN in every Mitigation; remediation actions not format guidance; category derivation from T2-VERDICT with explicit forbidden sets)
8. Org Evolution Roadmap (Row 1: headcount threshold; Row 2: different category; FORBIDDEN: two headcount rows)
9. Pre-print skeleton (fill `{{T2-PRESSURE}}`, `{{T2-VERDICT}}`, `{{T3-ROLE-COUNT}}`, `{{T3-AREAS}}`, `{{T3-IA-PRESENT}}` verbatim)

Anti-pattern category matrix — apply exactly:

| T2-VERDICT | MUST use | FORBIDDEN |
|-----------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

**Outbound — FORBIDDEN: beginning Phase 5 before emitting:**

```
=== RECORD: PHASE-4 ===
T4-ORG-CHART-WRITTEN: yes | no
T4-SECTIONS-COMPLETE: [count]
=== END RECORD: PHASE-4 ===
```

---

**Phase 5 — Validation**

**Inbound — FORBIDDEN: executing Phase 5 before all RECORD blocks PHASE-1 through PHASE-4 emitted.**

Check: T3-ROLE-COUNT in range (standard 20–30, deep 50+) · T3-IA-PRESENT = yes · T2-PRESSURE one of closed set · T2-VERDICT exactly one value · T4-ORG-CHART-WRITTEN = yes. Failure → `VALIDATION-FAILED: [reason]`, stop.

---

## V-05 — Combination: Output Format × Inertia Framing

**Axis**: Inertia analysis is the first major section — the output leads with the verdict before the org diagram, and the verdict governs all downstream sections. All requirements and outputs are expressed as tables.  
**Hypothesis**: Treating inertia as the lede rather than an appendix makes FLAT-CASE-PRESSURE the organizing principle for the entire output; combined with tabular format, this maximizes scores on C-08, C-11, C-12, C-17, C-18 because the verdict is established before any section that depends on it.

---

You are running `org-build`. Produce: (1) `org-chart.md`, (2) `.craft/roles/{area}/{role}.md`.

**ORGANIZING PRINCIPLE**: The inertia verdict is the first output and the last word. Every downstream section derives from it. FORBIDDEN: writing any org artifact — diagram, role files, headcount table — before the inertia assessment is complete and T2-VERDICT is recorded.

**PHASE BOUNDARY RULE**: Every phase emits a RECORD block. This block declares gate variables, anchors the ordering constraint, and materializes the checkpoint — all three from one location. FORBIDDEN: beginning any phase before all prior RECORD blocks are present. At every boundary: outbound FORBIDDEN at the gate + inbound FORBIDDEN at the consuming phase.

---

**Phase 1 — Role Inventory**

**Inbound**: Unconditional entry.

Scan input. Produce `ROLES-LOADED:` or `ROLES-NOTE:` (one line per role). Produce `ROLE-TYPE-CLASSIFICATION:` in three-tier order (Engineering → Operations → remaining). FORBIDDEN: interleaving tiers. MUST include one `inertia` or `advocate` role. Determine depth flag.

**Role Summary Table** (emit immediately after ROLE-TYPE-CLASSIFICATION):

| Type | Role Names | Count |
|------|-----------|-------|
| Engineering | | |
| PM | | |
| Design | | |
| Operations | | |
| Research | | |
| Other | | |
| **Total** | | |

**Outbound — FORBIDDEN: beginning Phase 2 before emitting:**

```
=== RECORD: PHASE-1 ===
T1-AREAS: [comma-separated]
T1-ROLE-LIST: [comma-separated]
T1-ROLE-COUNT: [integer]
T1-DEPTH-FLAG: standard | deep
=== END RECORD: PHASE-1 ===
```

---

**Phase 2 — Inertia Assessment (LEADS THE OUTPUT)**

**Inbound — FORBIDDEN: executing Phase 2 before RECORD: PHASE-1 emitted.** MUST read T1-AREAS, T1-ROLE-COUNT from RECORD: PHASE-1.

This section produces the governing verdict for the entire output. FORBIDDEN: writing org diagrams, role files, or headcount tables before this phase completes and RECORD: PHASE-2 is emitted.

**Mechanism Evidence Table**:

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type from: `Channel | Informal Role | Recurring Cadence | Shared Artifact`. MUST have 2+ data rows. After 2+ rows: emit `--- [FLAT-CASE-CLOSED: {N} rows.] ---`

**Coordination Inventory Table**:

| Pattern | Channel/Cadence/Artifact | Frequency | Participants |
|---------|--------------------------|-----------|--------------|

FORBIDDEN: re-listing entries from Mechanism Evidence Table.

**Rebuttal**: One specific coordination failure with observable evidence. FORBIDDEN: generic growth statements.

**Verdict Declaration Table** (the governing output for all downstream phases):

| Dimension | Value | Derivation |
|-----------|-------|------------|
| FLAT-CASE-PRESSURE | LOW \| MODERATE \| ELEVATED \| CRITICAL | Mechanism count + failure mode |
| VERDICT | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED | One verdict only |
| Re-assessment Trigger | [concrete threshold] | Named observable |

FORBIDDEN: writing both verdict values in the VERDICT row. Both is an error.  
FORBIDDEN: leaving VERDICT row blank. Neither is an error.

**IA Scope Template Selection Table** (derived from verdict, governs Phase 3):

| T2-PRESSURE | Verbatim scope text to copy into inertia-advocate `scope` field |
|-------------|--------------------------------------------------------------|
| LOW | `Monitor adoption signals; flag if flat-structure friction surfaces in two or more consecutive retrospectives.` |
| MODERATE | `Facilitate coordination retrospectives each sprint; escalate findings to the area lead when friction recurs in consecutive cycles.` |
| ELEVATED | `Own cross-team coordination failure analysis; surface a written risk report to the steering committee each sprint and track resolution status.` |
| CRITICAL | `Drive the org restructure proposal; MUST block further headcount growth until structural issues are resolved and a remediation plan is ratified by steering.` |

**Anti-Pattern Category Selection Table** (derived from verdict, governs Phase 4):

| T2-VERDICT | MUST use | FORBIDDEN |
|-----------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

**Outbound — FORBIDDEN: beginning Phase 3 before emitting:**

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: LOW | MODERATE | ELEVATED | CRITICAL
T2-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED
=== END RECORD: PHASE-2 ===
```

---

**Phase 3 — Role File Authoring**

**Inbound — FORBIDDEN: executing Phase 3 before RECORD: PHASE-1 and RECORD: PHASE-2 emitted.** MUST read T1-ROLE-LIST from RECORD: PHASE-1. MUST read T2-PRESSURE from RECORD: PHASE-2.

Write `.craft/roles/{area}/{role}.md` per role. Group by area subdir. Every file — all five fields required:

**Role File Schema Table**:

| Field | Constraint |
|-------|-----------|
| orientation | MUST be one of: `contributor \| manager \| lead \| executive` |
| lens | MUST name a specific analytical frame |
| expertise | MUST name a specific domain |
| scope | MUST be drawn from context; for inertia-advocate: MUST be verbatim template text |
| collaborates_with | MUST list 1+ role names |

**inertia-advocate `scope`**: MUST copy verbatim from Phase 2 IA Scope Template Selection Table for the applicable T2-PRESSURE row. The table in Phase 2 is the authoritative source. Copy exactly. Any deviation fails.

**Role File Generation Table** (emit this tracking table as roles are written):

| Area | Role | File Path | IA-Scope Applied |
|------|------|-----------|-----------------|

**Outbound — FORBIDDEN: beginning Phase 4 before emitting:**

```
=== RECORD: PHASE-3 ===
T3-ROLE-COUNT: [count]
T3-IA-PRESENT: yes | no
T3-AREAS: [comma-separated subdir names]
=== END RECORD: PHASE-3 ===
```

---

**Phase 4 — Org Chart Authoring**

**Inbound — FORBIDDEN: executing Phase 4 before RECORD: PHASE-2 and RECORD: PHASE-3 emitted.** MUST read T2-PRESSURE, T2-VERDICT from RECORD: PHASE-2. MUST read T3-AREAS, T3-ROLE-COUNT from RECORD: PHASE-3.

Write `org-chart.md`. The verdict established in Phase 2 governs every section. Produce sections in order:

**Section Order Table**:

| # | Section | Governed by | Hard failure if absent |
|---|---------|-------------|----------------------|
| 1 | ASCII Hierarchy | (structure) | Flat list, < 2 levels |
| 2 | Headcount by Area | T3-AREAS | Missing Decides or Escalates column |
| 3 | Operating Rhythm | (DRI roles) | < 3 rows, missing ROB/shiproom/governance |
| 4 | Committee Charters | (governance meetings) | Missing any of 5 fields, short-form quorum |
| 5 | Inertia Summary | T2-PRESSURE, T2-VERDICT | Both verdicts, neither verdict |
| 6 | ORG-ELEMENT REGISTER | (all prior sections) | Missing before Org Evolution Roadmap |
| 7 | Anti-Pattern Watch | T2-VERDICT → category matrix | Wrong categories, advisory Mitigations |
| 8 | Org Evolution Roadmap | (triggers) | < 2 rows, two headcount rows |
| 9 | Pre-print Skeleton | All T variables | Missing any `{{Txx}}` slot |

**Committee Charter Template** (one per governance meeting):

| Field | Value |
|-------|-------|
| Name | |
| Cadence | |
| Owner | |
| Members | |
| Quorum | N of M (e.g., 4 of 7) |

FORBIDDEN: omitting any field. FORBIDDEN: short-form quorum (must be N of M fraction).

**Anti-Pattern Watch** — apply category matrix from RECORD: PHASE-2 (T2-VERDICT). Every `Why It Applies Here` cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST use MUST or FORBIDDEN and contain a specific remediation action. Format guidance in Mitigation cells fails.

**Pre-print Skeleton** (fill verbatim):

```
ORG-BUILD RESULT SUMMARY
Topic: {{TOPIC}}
Date: {{DATE}}
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Role count: {{T3-ROLE-COUNT}}
Areas: {{T3-AREAS}}
IA scope template applied: {{T3-IA-PRESENT}}
```

**Outbound — FORBIDDEN: beginning Phase 5 before emitting:**

```
=== RECORD: PHASE-4 ===
T4-ORG-CHART-WRITTEN: yes | no
T4-SECTIONS-COMPLETE: [count]
=== END RECORD: PHASE-4 ===
```

---

**Phase 5 — Validation**

**Inbound — FORBIDDEN: executing Phase 5 before RECORD: PHASE-1 through PHASE-4 all emitted.**

**Validation Checklist Table**:

| Check | Expected | Source | Fail action |
|-------|----------|--------|-------------|
| Role count in range | standard: 20–30, deep: 50+ | T3-ROLE-COUNT vs T1-DEPTH-FLAG | VALIDATION-FAILED |
| IA present | yes | T3-IA-PRESENT | VALIDATION-FAILED |
| Pressure in closed set | LOW \| MODERATE \| ELEVATED \| CRITICAL | T2-PRESSURE | VALIDATION-FAILED |
| Verdict exactly one | one value only | T2-VERDICT | VALIDATION-FAILED |
| Org chart written | yes | T4-ORG-CHART-WRITTEN | VALIDATION-FAILED |

Any failed check: emit `VALIDATION-FAILED: [check name] — [observed value]` and stop.

---

## Summary of Variation Axes

| Variation | Axis 1 | Axis 2 | Key Hypothesis |
|-----------|--------|--------|----------------|
| V-01 | Role Sequence (area-first discovery) | — | Bottom-up role enumeration reduces synthetic hallucination |
| V-02 | Output Format (table-dominant) | — | Uniform tables make field-completeness checkable at a glance |
| V-03 | Lifecycle Emphasis (double-guard leads) | — | Foregrounding phase discipline reduces record-block skipping on long outputs |
| V-04 | Role Sequence | Lifecycle Emphasis | Area-first + strict double-guard produces tightest IA scope derivation |
| V-05 | Output Format | Inertia Framing (verdict leads) | Inertia as lede maximizes C-08/C-11/C-12/C-17/C-18 because verdict precedes all dependent sections |
