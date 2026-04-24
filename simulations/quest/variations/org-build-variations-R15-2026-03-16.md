## Quest Variate — org-build Skill, Round 15 (v11 Rubric)

---

## V-01 — Inertia-First Sequence

**Variation axis:** Role sequence — inertia assessment runs before role enumeration  
**Hypothesis:** Anchoring the structural verdict before any roles are enumerated forces verdict-coherent anti-pattern category selection, IA scope, and downstream constraint choices throughout the pipeline.

---

```markdown
You are executing the **org-build** skill. Generate a complete org from scan results or directly
from a repo.

**Primary outputs**
1. `org-chart.md` — ASCII box diagram, headcount by area, level distribution, inertia verdict
2. `.roles/{area}/{role}.md` — one file per role, five required fields each

FORBIDDEN: beginning any phase before the preceding phase RECORD block is emitted.

---

## Verbatim IA Scope Templates

Apply one of the following templates verbatim to the `scope` field of the inertia-advocate role.
Key selection to the T2-PRESSURE value from Phase 2 RECORD block.
FORBIDDEN: paraphrasing, adapting, or deviating from the template text in any way.

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | Structural health is nominal. No flat-case pressure detected. Monitor headcount distribution at next annual planning cycle. No restructuring signal present. |
| LOW | Low flat-case pressure detected. Span-of-control metrics within tolerance. Track semi-annually. No immediate restructuring action required. |
| MODERATE | Moderate flat-case pressure detected. Review hiring plan against current team span. Assess span of control at next planning cycle. Flag for VP visibility before headcount decisions. |
| HIGH | High flat-case pressure detected. Escalate structural review to VP. A formal structural proposal MUST be submitted before the next headcount decision is approved. |
| CRITICAL | Critical flat-case pressure detected. Immediate restructuring required. FORBIDDEN: approving additional headcount before org redesign is ratified and approved. |

---

## Anti-Pattern Category Derivation

The categories available for the Anti-Pattern Watch table are structurally keyed to T2-VERDICT.
FORBIDDEN: selecting categories independent of the verdict.

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## Phase 1 — Input Classification

### Task Steps
1. Locate input source: scan results file, repo directory, or task description.
2. Read `--depth` flag. If absent, default to `standard`.
3. Classify structure signal: `EXISTING` if scan results are present, `GREENFIELD` otherwise.

### Constraints
- MUST set T1-DEPTH-FLAG to exactly `standard` or `deep`.
- MUST set T1-STRUCTURE-SIGNAL to exactly `EXISTING` or `GREENFIELD`.
- FORBIDDEN: beginning Phase 2 before emitting the Phase 1 RECORD block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-STRUCTURE-SIGNAL: [EXISTING | GREENFIELD]
===
```

---

## Phase 2 — Inertia Assessment

### Input Contract
- T1-DEPTH-FLAG (Phase 1 RECORD block) — MUST be present before assessment begins.
- T1-STRUCTURE-SIGNAL (Phase 1 RECORD block) — MUST be `EXISTING` or `GREENFIELD`.
- FORBIDDEN: executing Phase 2 before Phase 1 RECORD block is emitted.

### Task Steps
1. Evaluate flat-case pressure across five dimensions: span of control, decision latency,
   role ambiguity, cross-team coordination cost, headcount trajectory.
2. Assign FLAT-CASE-PRESSURE from the closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
3. Derive verdict:
   - NONE or LOW pressure → `CAN-OPERATE-FLAT`
   - MODERATE, HIGH, or CRITICAL pressure → `STRUCTURE-WARRANTED`

### Constraints
- MUST assign FLAT-CASE-PRESSURE from the closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
- MUST issue exactly one verdict.
- FORBIDDEN: writing both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`. Both is an error.
- FORBIDDEN: omitting both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`. Neither is an error.
- FORBIDDEN: beginning Phase 3 before emitting the Phase 2 RECORD block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## Phase 3 — Role Enumeration

### Input Contract
- T1-DEPTH-FLAG (Phase 1 RECORD block) — MUST be present. Governs role count floor.
- T2-VERDICT (Phase 2 RECORD block) — MUST be present. Governs anti-pattern categories.
- T2-PRESSURE (Phase 2 RECORD block) — MUST be present. Governs IA scope template.
- FORBIDDEN: executing Phase 3 before Phase 2 RECORD block is emitted.

### Task Steps
1. Enumerate roles across primary expertise areas.
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles.
2. Group roles into min 2 named area subdirectories.
3. MUST include role named `inertia-advocate`.
4. Record total role count and area count.

### Constraints
- T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles. FORBIDDEN: fewer than 20.
- T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles. FORBIDDEN: fewer than 50.
- MUST include `inertia-advocate`. FORBIDDEN: omitting it.
- FORBIDDEN: fewer than 2 area groupings.
- FORBIDDEN: beginning Phase 4 before emitting the Phase 3 RECORD block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: [integer]
T3-AREA-COUNT: [integer ≥ 2]
===
```

---

## Phase 4 — Write Role Files

### Input Contract
- T2-PRESSURE (Phase 2 RECORD block) — MUST be present. Selects verbatim IA scope template.
- T2-VERDICT (Phase 2 RECORD block) — MUST be present.
- T3-ROLE-COUNT (Phase 3 RECORD block) — MUST be present.
- T3-AREA-COUNT (Phase 3 RECORD block) — MUST be ≥ 2.
- FORBIDDEN: executing Phase 4 before Phase 3 RECORD block is emitted.

### Task Steps
1. For every role enumerated in Phase 3, write `.roles/{area}/{role-name}.md`.
2. Every role file MUST contain exactly these five fields:
   ```
   orientation: <what this role is optimizing for>
   lens: <how this role evaluates decisions>
   expertise: <domain knowledge this role holds>
   scope: <what this role owns and is accountable for>
   collaborates_with: <list of roles this role works with>
   ```
3. For `inertia-advocate`, look up T2-PRESSURE in the Verbatim IA Scope Templates table above.
   Copy the template text into the `scope` field exactly as written.

### Constraints
- MUST write all five fields in every role file.
- FORBIDDEN: omitting `orientation`, `lens`, `expertise`, `scope`, or `collaborates_with`
  from any role file.
- MUST copy IA scope verbatim from template table, keyed to T2-PRESSURE.
- FORBIDDEN: paraphrasing or adapting the IA scope template text.
- MUST write role files under `.roles/{area}/`. FORBIDDEN: placing all files flat with
  no area subdirectory structure.
- FORBIDDEN: beginning Phase 5 before emitting the Phase 4 RECORD block.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-ROLE-FILE-STATUS: [COMPLETE | PARTIAL]
T4-IA-SCOPE-APPLIED: [YES | NO]
===
```

---

## Phase 5 — Write org-chart.md

### Input Contract
- T2-PRESSURE (Phase 2 RECORD block) — MUST be present for FLAT-CASE-PRESSURE entry.
- T2-VERDICT (Phase 2 RECORD block) — MUST be present for verdict block.
- T3-ROLE-COUNT (Phase 3 RECORD block) — MUST be present for headcount table.
- T4-ROLE-FILE-STATUS (Phase 4 RECORD block) — MUST be `COMPLETE`.
- FORBIDDEN: executing Phase 5 before Phase 4 RECORD block is emitted.

### Task Steps

Write `org-chart.md` with the following seven sections in order:

**Section 1 — ASCII Org Hierarchy**
Box-and-line diagram with min 2 org levels. FORBIDDEN: replacing the ASCII diagram with a
flat name list.

Example skeleton:
```
[Senior Org Unit]
 ├── [Area A Lead]
 │    ├── [{{role-name}}]
 │    └── [{{role-name}}]
 └── [Area B Lead]
      └── [{{role-name}}]
```

**Section 2 — Headcount by Area Table**

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

MUST include all five columns. FORBIDDEN: omitting `Decides` or `Escalates`.

**Section 3 — Level Distribution Table**

| Level | Count | % of Org |
|-------|-------|----------|

**Section 4 — Inertia Assessment Block**
```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```
FORBIDDEN: writing both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`.
FORBIDDEN: omitting both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`.

**Section 5 — Anti-Pattern Watch Table**

Select categories using the Category Derivation table. Required categories keyed to T2-VERDICT.
FORBIDDEN: using categories from the FORBIDDEN column for T2-VERDICT.

| Anti-Pattern | Why It Applies Here | Mitigation |
|-------------|---------------------|------------|

- MUST include min 2 rows.
- Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
- Every Mitigation cell MUST contain a specific remediation action.
- FORBIDDEN: format guidance, column-structure notes, or descriptive instructions in
  Mitigation cells.

**Section 6 — Operating Rhythm Table + Committee Charters**

| Cadence | Meeting | Owner | Participants | Quorum |
|---------|---------|-------|--------------|--------|

MUST include min 3 distinct rows: ROB, shiproom, and governance meeting.

For every governance meeting row, write a charter block:
```
Charter: [Meeting Name]
Purpose: [one sentence]
Owner: [role]
Participants: [list]
Quorum: N of M
Decision Rights: [what this committee decides]
```
FORBIDDEN: omitting Quorum from any charter.

**Section 7 — Org Evolution Roadmap**

| Trigger | Type | Action |
|---------|------|--------|

MUST include min 2 rows. Row 1 MUST be a headcount threshold trigger type.
Row 2 MUST be a different trigger type. FORBIDDEN: two headcount threshold rows.

### Constraints
- MUST write all seven sections.
- FORBIDDEN: omitting any section.
- MUST emit `FLAT-CASE-PRESSURE:` followed by a closed-set rating.
- MUST issue exactly one verdict in Section 4.
- FORBIDDEN: selecting anti-pattern categories from the FORBIDDEN column for T2-VERDICT.
```

---

## V-02 — Table-Dominant Format

**Variation axis:** Output format — all constraint declarations encoded in tables; prose replaced with structured rows  
**Hypothesis:** Tabular constraint encoding reduces missed constraints because each row is independently scannable and the side-by-side format naturally surfaces required/FORBIDDEN pairings without prose interpretation.

---

```markdown
You are executing the **org-build** skill. Generate a complete org from scan results or
directly from a repo.

**Primary outputs**
1. `org-chart.md` — ASCII box diagram, headcount by area, level distribution, inertia verdict
2. `.roles/{area}/{role}.md` — one file per role, five required fields each

FORBIDDEN: beginning any phase before the preceding phase RECORD block is emitted.

---

## Global Constraint Table

| ID | Constraint | Register |
|----|-----------|---------|
| G-01 | All five role fields present in every .roles/ file | MUST |
| G-02 | inertia-advocate role present | MUST |
| G-03 | Role files organized under area subdirectories (min 2) | MUST |
| G-04 | ASCII diagram with min 2 org levels in org-chart.md | MUST |
| G-05 | All prohibitions declared with FORBIDDEN: keyword | MUST |
| G-06 | Paraphrasing the IA scope template | FORBIDDEN |
| G-07 | Beginning any phase before preceding RECORD block emitted | FORBIDDEN |

---

## Verbatim IA Scope Templates

| T2-PRESSURE | Verbatim scope (copy exactly, no deviation) |
|-------------|---------------------------------------------|
| NONE | Structural health is nominal. No flat-case pressure detected. Monitor headcount distribution at next annual planning cycle. No restructuring signal present. |
| LOW | Low flat-case pressure detected. Span-of-control metrics within tolerance. Track semi-annually. No immediate restructuring action required. |
| MODERATE | Moderate flat-case pressure detected. Review hiring plan against current team span. Assess span of control at next planning cycle. Flag for VP visibility before headcount decisions. |
| HIGH | High flat-case pressure detected. Escalate structural review to VP. A formal structural proposal MUST be submitted before the next headcount decision is approved. |
| CRITICAL | Critical flat-case pressure detected. Immediate restructuring required. FORBIDDEN: approving additional headcount before org redesign is ratified and approved. |

---

## Anti-Pattern Category Derivation Table

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## Phase 1 — Input Classification

### Task Steps
| Step | Action |
|------|--------|
| 1 | Locate input source: scan results, repo directory, or task description |
| 2 | Read `--depth` flag; default to `standard` if absent |
| 3 | Classify structure: `EXISTING` (scan results present) or `GREENFIELD` |

### Constraints
| Constraint | Register |
|-----------|---------|
| T1-DEPTH-FLAG MUST be exactly `standard` or `deep` | MUST |
| T1-STRUCTURE-SIGNAL MUST be exactly `EXISTING` or `GREENFIELD` | MUST |
| Beginning Phase 2 before Phase 1 RECORD block is emitted | FORBIDDEN |

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-STRUCTURE-SIGNAL: [EXISTING | GREENFIELD]
===
```

---

## Phase 2 — Inertia Assessment

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | Phase 1 RECORD block | MUST be present before assessment begins |
| T1-STRUCTURE-SIGNAL | Phase 1 RECORD block | MUST be `EXISTING` or `GREENFIELD` |
| Executing Phase 2 before Phase 1 RECORD block emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Evaluate flat-case pressure: span of control, decision latency, role ambiguity, coordination cost, headcount trajectory |
| 2 | Assign FLAT-CASE-PRESSURE from closed set: `NONE \| LOW \| MODERATE \| HIGH \| CRITICAL` |
| 3 | NONE/LOW → `CAN-OPERATE-FLAT`; MODERATE/HIGH/CRITICAL → `STRUCTURE-WARRANTED` |

### Constraints
| Constraint | Register |
|-----------|---------|
| Assign FLAT-CASE-PRESSURE from closed set `NONE \| LOW \| MODERATE \| HIGH \| CRITICAL` | MUST |
| Issue exactly one verdict | MUST |
| Writing both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`. Both is an error. | FORBIDDEN |
| Omitting both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`. Neither is an error. | FORBIDDEN |
| Beginning Phase 3 before Phase 2 RECORD block is emitted | FORBIDDEN |

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## Phase 3 — Role Enumeration

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | Phase 1 RECORD block | MUST be present; governs role count floor |
| T2-VERDICT | Phase 2 RECORD block | MUST be present; governs anti-pattern categories |
| T2-PRESSURE | Phase 2 RECORD block | MUST be present; governs IA scope template |
| Executing Phase 3 before Phase 2 RECORD block emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Enumerate roles; apply depth-conditional count (see Constraints below) |
| 2 | Group into min 2 named areas |
| 3 | Include `inertia-advocate` |
| 4 | Record total role count and area count |

### Constraints
| Condition | Constraint | Register |
|-----------|-----------|---------|
| T1-DEPTH-FLAG = standard | 20–30 roles | MUST |
| T1-DEPTH-FLAG = standard | Fewer than 20 roles | FORBIDDEN |
| T1-DEPTH-FLAG = deep | 50+ roles | MUST |
| T1-DEPTH-FLAG = deep | Fewer than 50 roles | FORBIDDEN |
| Always | Include `inertia-advocate` | MUST |
| Always | Omitting `inertia-advocate` | FORBIDDEN |
| Always | Fewer than 2 area groupings | FORBIDDEN |
| Always | Beginning Phase 4 before Phase 3 RECORD block emitted | FORBIDDEN |

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: [integer]
T3-AREA-COUNT: [integer ≥ 2]
===
```

---

## Phase 4 — Write Role Files

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | Phase 2 RECORD block | MUST be present; selects IA scope template |
| T2-VERDICT | Phase 2 RECORD block | MUST be present |
| T3-ROLE-COUNT | Phase 3 RECORD block | MUST be present |
| T3-AREA-COUNT | Phase 3 RECORD block | MUST be ≥ 2 |
| Executing Phase 4 before Phase 3 RECORD block emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Write `.roles/{area}/{role-name}.md` for every role |
| 2 | Each file MUST include: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with` |
| 3 | For `inertia-advocate` scope: look up T2-PRESSURE in Verbatim IA Scope Templates; copy verbatim |

### Constraints
| Constraint | Register |
|-----------|---------|
| All five fields in every role file | MUST |
| Omitting any field from any role file | FORBIDDEN |
| IA scope copied verbatim from template, keyed to T2-PRESSURE | MUST |
| Paraphrasing or adapting IA scope template | FORBIDDEN |
| Role files under `.roles/{area}/` | MUST |
| All role files flat with no area subdirectory | FORBIDDEN |
| Beginning Phase 5 before Phase 4 RECORD block emitted | FORBIDDEN |

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-ROLE-FILE-STATUS: [COMPLETE | PARTIAL]
T4-IA-SCOPE-APPLIED: [YES | NO]
===
```

---

## Phase 5 — Write org-chart.md

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | Phase 2 RECORD block | MUST be present for FLAT-CASE-PRESSURE field |
| T2-VERDICT | Phase 2 RECORD block | MUST be present for verdict block |
| T3-ROLE-COUNT | Phase 3 RECORD block | MUST be present for headcount table |
| T4-ROLE-FILE-STATUS | Phase 4 RECORD block | MUST be `COMPLETE` |
| Executing Phase 5 before Phase 4 RECORD block emitted | — | FORBIDDEN |

### Section Specification Table

| Section | Required Elements | Constraints |
|---------|------------------|-------------|
| 1. ASCII Hierarchy | Box-and-line diagram, min 2 org levels | FORBIDDEN: flat name list |
| 2. Headcount by Area | Columns: Area, Headcount, Key Roles, Decides, Escalates | FORBIDDEN: omitting Decides or Escalates |
| 3. Level Distribution | Columns: Level, Count, % of Org | MUST include all roles |
| 4. Inertia Block | `FLAT-CASE-PRESSURE: {{T2-PRESSURE}}`, `VERDICT: {{T2-VERDICT}}` | FORBIDDEN: both verdicts. FORBIDDEN: neither verdict. |
| 5. Anti-Pattern Watch | Min 2 rows; cat-N citations; remediation actions | FORBIDDEN: categories from FORBIDDEN column; FORBIDDEN: format guidance in Mitigation |
| 6. Operating Rhythm | Min 3 rows (ROB, shiproom, governance); charter per governance meeting | FORBIDDEN: omitting Quorum from any charter |
| 7. Evolution Roadmap | Min 2 rows; Row 1 = headcount threshold; Row 2 = different type | FORBIDDEN: two headcount threshold rows |

### Anti-Pattern Watch — Row Format Requirement

| Anti-Pattern | Why It Applies Here | Mitigation |
|-------------|---------------------|------------|
| [name] | [element name] (cat-N) — [explanation] | [specific remediation action] |

MUST open every "Why It Applies Here" cell with `[element name] (cat-N) —` syntax.
FORBIDDEN: opening with plain prose.
MUST write a specific remediation action in every Mitigation cell.
FORBIDDEN: writing format guidance or column-structure notes in Mitigation cells.

### Constraints
| Constraint | Register |
|-----------|---------|
| All seven sections present in org-chart.md | MUST |
| Omitting any section | FORBIDDEN |
| Exactly one verdict in Section 4 | MUST |
| Writing both or neither verdict | FORBIDDEN |
| Anti-pattern categories from required column for T2-VERDICT | MUST |
| Anti-pattern categories from FORBIDDEN column for T2-VERDICT | FORBIDDEN |
```

---

## V-03 — Explicit Phase Segmentation

**Variation axis:** Lifecycle emphasis — maximum structural demarcation, each phase boundary carries both outbound and inbound guards, record blocks are verbose with full constraint derivation traces  
**Hypothesis:** Redundant bidirectional guards at every phase edge and self-describing record blocks with full type annotations reduce model skip behavior on long-context outputs.

---

```markdown
You are executing the **org-build** skill.

Generate a complete organizational structure from scan results or directly from a repo.

PRIMARY OUTPUTS:
  (1) org-chart.md — ASCII hierarchy, headcount table, inertia assessment, anti-patterns,
      operating rhythm, evolution roadmap
  (2) .roles/{area}/{role}.md — one file per role, five required fields

EXECUTION MODEL: This skill is phase-gated. Each phase produces a RECORD block. A phase
MUST NOT begin until the preceding phase RECORD block has been emitted. Every RECORD block
carries a PHASE-ORDERING-GUARD as its first named field — this guard IS the per-boundary
ordering constraint anchor.

---

## Reference: Verbatim IA Scope Templates

These templates are the exclusive source of scope text for the inertia-advocate role.
MUST copy the template corresponding to T2-PRESSURE exactly as written.
FORBIDDEN: any deviation, paraphrase, or adaptation of these templates.

```
NONE:
  Structural health is nominal. No flat-case pressure detected. Monitor headcount
  distribution at next annual planning cycle. No restructuring signal present.

LOW:
  Low flat-case pressure detected. Span-of-control metrics within tolerance.
  Track semi-annually. No immediate restructuring action required.

MODERATE:
  Moderate flat-case pressure detected. Review hiring plan against current team span.
  Assess span of control at next planning cycle. Flag for VP visibility before
  headcount decisions.

HIGH:
  High flat-case pressure detected. Escalate structural review to VP. A formal
  structural proposal MUST be submitted before the next headcount decision is approved.

CRITICAL:
  Critical flat-case pressure detected. Immediate restructuring required.
  FORBIDDEN: approving additional headcount before org redesign is ratified and approved.
```

---

## Reference: Anti-Pattern Category Derivation

Anti-pattern categories are structurally determined by T2-VERDICT.
FORBIDDEN: selecting categories independent of T2-VERDICT.

| Verdict | Required Categories | FORBIDDEN Categories |
|---------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## ═══ PHASE 1: Input Classification ═══

### ── Task Steps ──────────────────────────────────────

**T1.1** Locate input source.
  - Scan results file present → use as primary source
  - No scan results → read from repo directory or task description

**T1.2** Determine depth mode.
  - Read `--depth` flag from invocation.
  - If `--depth deep` → T1-DEPTH-FLAG = `deep`
  - If `--depth standard` or flag absent → T1-DEPTH-FLAG = `standard`

**T1.3** Classify structural signal.
  - Scan results present → T1-STRUCTURE-SIGNAL = `EXISTING`
  - No scan results → T1-STRUCTURE-SIGNAL = `GREENFIELD`

### ── Constraints ─────────────────────────────────────

  MUST assign T1-DEPTH-FLAG exactly from: [standard | deep]
  MUST assign T1-STRUCTURE-SIGNAL exactly from: [EXISTING | GREENFIELD]
  FORBIDDEN: beginning Phase 2 before the Phase 1 RECORD block below is emitted.

### ── Outbound Gate ───────────────────────────────────

Emit this record block before proceeding to Phase 2:

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-STRUCTURE-SIGNAL: [EXISTING | GREENFIELD]
===
```

---

## ═══ PHASE 2: Inertia Assessment ═══

### ── Input Contract ──────────────────────────────────

  T1-DEPTH-FLAG   source: Phase 1 RECORD block   binding: MUST be present
  T1-STRUCTURE-SIGNAL   source: Phase 1 RECORD block   binding: MUST be [EXISTING | GREENFIELD]
  FORBIDDEN: executing Phase 2 before Phase 1 RECORD block is emitted.

### ── Task Steps ──────────────────────────────────────

**T2.1** Evaluate flat-case pressure across five dimensions:
  - Span of control: average reports per manager
  - Decision latency: cycle time from decision to execution
  - Role ambiguity: overlap in responsibility across roles
  - Cross-team coordination cost: handoffs per delivery
  - Headcount trajectory: growth rate vs structural capacity

**T2.2** Assign FLAT-CASE-PRESSURE rating.
  - Select exactly one value from: NONE | LOW | MODERATE | HIGH | CRITICAL
  - Base selection on the dimension analysis above.

**T2.3** Derive verdict from FLAT-CASE-PRESSURE:
  - NONE → CAN-OPERATE-FLAT
  - LOW → CAN-OPERATE-FLAT
  - MODERATE → STRUCTURE-WARRANTED
  - HIGH → STRUCTURE-WARRANTED
  - CRITICAL → STRUCTURE-WARRANTED

### ── Constraints ─────────────────────────────────────

  MUST assign FLAT-CASE-PRESSURE from closed set: [NONE | LOW | MODERATE | HIGH | CRITICAL]
  MUST issue exactly one verdict from: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
  FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error.
  FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
  FORBIDDEN: beginning Phase 3 before the Phase 2 RECORD block below is emitted.

### ── Outbound Gate ───────────────────────────────────

Emit this record block before proceeding to Phase 3:

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## ═══ PHASE 3: Role Enumeration ═══

### ── Input Contract ──────────────────────────────────

  T1-DEPTH-FLAG   source: Phase 1 RECORD block   binding: MUST be present; governs count floor
  T2-VERDICT      source: Phase 2 RECORD block   binding: MUST be present; governs anti-pattern categories
  T2-PRESSURE     source: Phase 2 RECORD block   binding: MUST be present; governs IA scope template
  FORBIDDEN: executing Phase 3 before Phase 2 RECORD block is emitted.

### ── Task Steps ──────────────────────────────────────

**T3.1** Determine role count floor from T1-DEPTH-FLAG:
  - T1-DEPTH-FLAG = standard → target 20–30 roles
  - T1-DEPTH-FLAG = deep → target 50+ roles

**T3.2** Enumerate roles, grouped by functional area.
  - Name each area explicitly.
  - Group every role under exactly one area.
  - MUST create min 2 distinct area groupings.

**T3.3** Include `inertia-advocate` as a named role.
  - Place in the area that owns structural health review.
  - Record role name exactly as `inertia-advocate`.

**T3.4** Record final role count and area count.

### ── Constraints ─────────────────────────────────────

  T1-DEPTH-FLAG = standard → MUST enumerate 20–30 roles.
    FORBIDDEN: enumerating fewer than 20 roles when T1-DEPTH-FLAG = standard.
  T1-DEPTH-FLAG = deep → MUST enumerate 50+ roles.
    FORBIDDEN: enumerating fewer than 50 roles when T1-DEPTH-FLAG = deep.
  MUST include role `inertia-advocate`.
    FORBIDDEN: omitting `inertia-advocate`.
  FORBIDDEN: fewer than 2 area groupings.
  FORBIDDEN: beginning Phase 4 before the Phase 3 RECORD block below is emitted.

### ── Outbound Gate ───────────────────────────────────

Emit this record block before proceeding to Phase 4:

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: [integer]
T3-AREA-COUNT: [integer ≥ 2]
===
```

---

## ═══ PHASE 4: Write Role Files ═══

### ── Input Contract ──────────────────────────────────

  T2-PRESSURE     source: Phase 2 RECORD block   binding: MUST be present; selects IA scope template
  T2-VERDICT      source: Phase 2 RECORD block   binding: MUST be present
  T3-ROLE-COUNT   source: Phase 3 RECORD block   binding: MUST be present
  T3-AREA-COUNT   source: Phase 3 RECORD block   binding: MUST be ≥ 2
  FORBIDDEN: executing Phase 4 before Phase 3 RECORD block is emitted.

### ── Task Steps ──────────────────────────────────────

**T4.1** For every role in the Phase 3 enumeration, write:
  Path: `.roles/{area-name}/{role-name}.md`

**T4.2** Each role file MUST contain exactly these five fields:

  ```yaml
  orientation: <what this role is optimizing for — one phrase>
  lens: <how this role evaluates decisions — one phrase>
  expertise: <domain knowledge this role holds — one to three areas>
  scope: <what this role owns and is accountable for>
  collaborates_with: <comma-separated list of role names>
  ```

**T4.3** For the `inertia-advocate` role specifically:
  a. Look up T2-PRESSURE in the Verbatim IA Scope Templates reference above.
  b. Copy the template text into the `scope` field exactly as written.
  c. Do not alter punctuation, capitalization, or wording.

### ── Constraints ─────────────────────────────────────

  MUST write all five fields in every role file.
  FORBIDDEN: omitting orientation, lens, expertise, scope, or collaborates_with
    from any role file.
  MUST copy IA scope verbatim from template, keyed to T2-PRESSURE.
  FORBIDDEN: paraphrasing, adapting, or abbreviating the IA scope template.
  MUST organize files under .roles/{area}/.
  FORBIDDEN: placing all files flat under .roles/ with no area subdirectory.
  FORBIDDEN: beginning Phase 5 before the Phase 4 RECORD block below is emitted.

### ── Outbound Gate ───────────────────────────────────

Emit this record block before proceeding to Phase 5:

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-ROLE-FILE-STATUS: [COMPLETE | PARTIAL]
T4-IA-SCOPE-APPLIED: [YES | NO]
===
```

---

## ═══ PHASE 5: Write org-chart.md ═══

### ── Input Contract ──────────────────────────────────

  T2-PRESSURE         source: Phase 2 RECORD block   binding: MUST be present
  T2-VERDICT          source: Phase 2 RECORD block   binding: MUST be present
  T3-ROLE-COUNT       source: Phase 3 RECORD block   binding: MUST be present
  T4-ROLE-FILE-STATUS source: Phase 4 RECORD block   binding: MUST be COMPLETE
  FORBIDDEN: executing Phase 5 before Phase 4 RECORD block is emitted.

### ── Task Steps ──────────────────────────────────────

Write `org-chart.md` with these seven sections in sequence:

**T5.1 — ASCII Org Hierarchy**
  Draw a box-and-line ASCII diagram. MUST show min 2 org levels.
  Slot: `[{{role-name}}]` per node.
  FORBIDDEN: replacing diagram with a flat name list.

**T5.2 — Headcount by Area Table**
  Columns: Area | Headcount | Key Roles | Decides | Escalates
  MUST include all five columns.
  FORBIDDEN: omitting Decides or Escalates.

**T5.3 — Level Distribution Table**
  Columns: Level | Count | % of Org

**T5.4 — Inertia Assessment Block**
  Write:
  ```
  FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
  VERDICT: {{T2-VERDICT}}
  ```
  Slot {{T2-PRESSURE}} with value from Phase 2 RECORD block.
  Slot {{T2-VERDICT}} with value from Phase 2 RECORD block.

**T5.5 — Anti-Pattern Watch Table**
  Select categories using Category Derivation table, keyed to T2-VERDICT.
  Format every row:
  | Anti-Pattern | Why It Applies Here | Mitigation |
  "Why It Applies Here" MUST open with: `[element name] (cat-N) —`
  Mitigation MUST contain a specific remediation action.

**T5.6 — Operating Rhythm Table + Committee Charters**
  Table columns: Cadence | Meeting | Owner | Participants | Quorum
  MUST include: ROB row, shiproom row, governance row (min 3 distinct rows).
  For every governance meeting, write a charter block:
  ```
  Charter: [Meeting Name]
  Purpose: [one sentence]
  Owner: [role]
  Participants: [list]
  Quorum: N of M
  Decision Rights: [what this committee decides]
  ```

**T5.7 — Org Evolution Roadmap**
  Table columns: Trigger | Type | Action
  Row 1: headcount threshold trigger type.
  Row 2: different trigger type.
  MUST include min 2 rows.

### ── Constraints ─────────────────────────────────────

  MUST write all seven sections in org-chart.md.
  FORBIDDEN: omitting any section.
  MUST emit FLAT-CASE-PRESSURE: label with closed-set value.
  MUST issue exactly one verdict.
  FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
  FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
  MUST select anti-pattern categories from required column for T2-VERDICT.
  FORBIDDEN: using categories from FORBIDDEN column for T2-VERDICT.
  MUST open every Why-It-Applies-Here cell with [element name] (cat-N) — syntax.
  FORBIDDEN: plain prose opening in Why-It-Applies-Here cells.
  MUST write specific remediation actions in Mitigation cells.
  FORBIDDEN: format guidance in Mitigation cells.
  MUST include Quorum in every committee charter.
  FORBIDDEN: omitting Quorum from any charter.
  Row 1 of Evolution Roadmap MUST be a headcount threshold trigger.
  FORBIDDEN: two headcount threshold rows in Evolution Roadmap.
```

---

## V-04 — Inertia-First + Table-Dominant (Combined)

**Variation axis:** Inertia-first sequence (V-01) combined with table-dominant constraint encoding (V-02)  
**Hypothesis:** Verdict-first ordering combined with tabular constraint declarations produces the highest constraint-compliance rate: the verdict is anchored early and all downstream constraint tables reference it directly by named variable, preventing both category drift and missed constraints.

---

```markdown
You are executing the **org-build** skill. Generate a complete org from scan results or
from a repo. The inertia assessment runs first — all downstream outputs are keyed to its verdict.

PRIMARY OUTPUTS:
  (1) org-chart.md — ASCII hierarchy, headcount table, inertia block, anti-patterns, rhythm,
      roadmap
  (2) .roles/{area}/{role}.md — one file per role, five required fields

FORBIDDEN: beginning any phase before the preceding phase RECORD block is emitted.

---

## Global Execution Table

| Phase | Inputs (from RECORD blocks) | Outputs (to RECORD block) |
|-------|-----------------------------|--------------------------|
| 1 — Input Classification | — | T1-DEPTH-FLAG, T1-STRUCTURE-SIGNAL |
| 2 — Inertia Assessment | T1-DEPTH-FLAG, T1-STRUCTURE-SIGNAL | T2-PRESSURE, T2-VERDICT |
| 3 — Role Enumeration | T1-DEPTH-FLAG, T2-VERDICT, T2-PRESSURE | T3-ROLE-COUNT, T3-AREA-COUNT |
| 4 — Role Files | T2-PRESSURE, T2-VERDICT, T3-ROLE-COUNT, T3-AREA-COUNT | T4-ROLE-FILE-STATUS, T4-IA-SCOPE-APPLIED |
| 5 — org-chart.md | T2-PRESSURE, T2-VERDICT, T3-ROLE-COUNT, T4-ROLE-FILE-STATUS | — |

---

## Reference Tables

### Verbatim IA Scope Templates

| T2-PRESSURE | Verbatim scope text — copy exactly, FORBIDDEN to deviate |
|-------------|----------------------------------------------------------|
| NONE | Structural health is nominal. No flat-case pressure detected. Monitor headcount distribution at next annual planning cycle. No restructuring signal present. |
| LOW | Low flat-case pressure detected. Span-of-control metrics within tolerance. Track semi-annually. No immediate restructuring action required. |
| MODERATE | Moderate flat-case pressure detected. Review hiring plan against current team span. Assess span of control at next planning cycle. Flag for VP visibility before headcount decisions. |
| HIGH | High flat-case pressure detected. Escalate structural review to VP. A formal structural proposal MUST be submitted before the next headcount decision is approved. |
| CRITICAL | Critical flat-case pressure detected. Immediate restructuring required. FORBIDDEN: approving additional headcount before org redesign is ratified and approved. |

### Anti-Pattern Category Derivation

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## Phase 1 — Input Classification

### Task Steps
| Step | Action |
|------|--------|
| 1 | Locate input source: scan results file, repo, or task description |
| 2 | Read `--depth` flag; default to `standard` if absent |
| 3 | Set T1-STRUCTURE-SIGNAL: `EXISTING` if scan results present; `GREENFIELD` otherwise |

### Constraints
| Constraint | Register |
|-----------|---------|
| T1-DEPTH-FLAG MUST be exactly `standard` or `deep` | MUST |
| T1-STRUCTURE-SIGNAL MUST be exactly `EXISTING` or `GREENFIELD` | MUST |
| Beginning Phase 2 before Phase 1 RECORD block emitted | FORBIDDEN |

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-STRUCTURE-SIGNAL: [EXISTING | GREENFIELD]
===
```

---

## Phase 2 — Inertia Assessment

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | Phase 1 RECORD block | MUST be present |
| T1-STRUCTURE-SIGNAL | Phase 1 RECORD block | MUST be `EXISTING` or `GREENFIELD` |
| Executing before Phase 1 RECORD emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Evaluate flat-case pressure: span of control, decision latency, role ambiguity, coordination cost, headcount trajectory |
| 2 | Assign FLAT-CASE-PRESSURE from: NONE / LOW / MODERATE / HIGH / CRITICAL |
| 3 | NONE or LOW → CAN-OPERATE-FLAT; MODERATE, HIGH, or CRITICAL → STRUCTURE-WARRANTED |

### Constraints
| Constraint | Register |
|-----------|---------|
| FLAT-CASE-PRESSURE from closed set `NONE \| LOW \| MODERATE \| HIGH \| CRITICAL` | MUST |
| Exactly one verdict from `CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED` | MUST |
| Writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error. | FORBIDDEN |
| Omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error. | FORBIDDEN |
| Beginning Phase 3 before Phase 2 RECORD block emitted | FORBIDDEN |

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## Phase 3 — Role Enumeration

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | Phase 1 RECORD block | MUST be present; governs count floor |
| T2-VERDICT | Phase 2 RECORD block | MUST be present; governs anti-pattern categories |
| T2-PRESSURE | Phase 2 RECORD block | MUST be present; governs IA scope template |
| Executing before Phase 2 RECORD emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Apply depth-conditional count (see Constraints) |
| 2 | Group roles into min 2 named area subdirectories |
| 3 | Include `inertia-advocate` |
| 4 | Record T3-ROLE-COUNT and T3-AREA-COUNT |

### Constraints
| Condition | Constraint | Register |
|-----------|-----------|---------|
| T1-DEPTH-FLAG = standard | Enumerate 20–30 roles | MUST |
| T1-DEPTH-FLAG = standard | Fewer than 20 roles | FORBIDDEN |
| T1-DEPTH-FLAG = deep | Enumerate 50+ roles | MUST |
| T1-DEPTH-FLAG = deep | Fewer than 50 roles | FORBIDDEN |
| Always | Include `inertia-advocate` | MUST |
| Always | Omitting `inertia-advocate` | FORBIDDEN |
| Always | Fewer than 2 area groupings | FORBIDDEN |
| Always | Beginning Phase 4 before Phase 3 RECORD emitted | FORBIDDEN |

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: [integer]
T3-AREA-COUNT: [integer ≥ 2]
===
```

---

## Phase 4 — Write Role Files

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | Phase 2 RECORD block | MUST be present; selects IA scope template |
| T2-VERDICT | Phase 2 RECORD block | MUST be present |
| T3-ROLE-COUNT | Phase 3 RECORD block | MUST be present |
| T3-AREA-COUNT | Phase 3 RECORD block | MUST be ≥ 2 |
| Executing before Phase 3 RECORD emitted | — | FORBIDDEN |

### Task Steps
| Step | Action |
|------|--------|
| 1 | Write `.roles/{area}/{role-name}.md` for every enumerated role |
| 2 | Include all five fields: orientation, lens, expertise, scope, collaborates_with |
| 3 | For `inertia-advocate`: look up T2-PRESSURE in Verbatim IA Scope Templates; copy scope verbatim |

### Constraints
| Constraint | Register |
|-----------|---------|
| All five fields in every role file | MUST |
| Omitting any field from any role file | FORBIDDEN |
| IA scope copied verbatim, keyed to T2-PRESSURE | MUST |
| Paraphrasing or adapting IA scope | FORBIDDEN |
| Files organized under .roles/{area}/ | MUST |
| All files flat with no area subdirectory | FORBIDDEN |
| Beginning Phase 5 before Phase 4 RECORD emitted | FORBIDDEN |

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-ROLE-FILE-STATUS: [COMPLETE | PARTIAL]
T4-IA-SCOPE-APPLIED: [YES | NO]
===
```

---

## Phase 5 — Write org-chart.md

### Input Contract
| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | Phase 2 RECORD block | MUST be present |
| T2-VERDICT | Phase 2 RECORD block | MUST be present |
| T3-ROLE-COUNT | Phase 3 RECORD block | MUST be present |
| T4-ROLE-FILE-STATUS | Phase 4 RECORD block | MUST be `COMPLETE` |
| Executing before Phase 4 RECORD emitted | — | FORBIDDEN |

### Section Specification Table

| # | Section | Required Elements | Key Constraints |
|---|---------|------------------|-----------------|
| 1 | ASCII Hierarchy | Box-and-line diagram, min 2 org levels | FORBIDDEN: flat name list |
| 2 | Headcount by Area | Area, Headcount, Key Roles, Decides, Escalates | FORBIDDEN: omitting Decides or Escalates |
| 3 | Level Distribution | Level, Count, % of Org | — |
| 4 | Inertia Block | `FLAT-CASE-PRESSURE: {{T2-PRESSURE}}`, `VERDICT: {{T2-VERDICT}}` | FORBIDDEN: both verdicts. FORBIDDEN: neither verdict. |
| 5 | Anti-Pattern Watch | Min 2 rows; cat-N citations; remediation Mitigations | FORBIDDEN: FORBIDDEN-column categories; FORBIDDEN: format guidance in Mitigation |
| 6 | Operating Rhythm | Min 3 rows (ROB, shiproom, governance); charter per governance mtg | FORBIDDEN: omitting Quorum |
| 7 | Evolution Roadmap | Min 2 rows; Row 1 = headcount threshold; Row 2 = different type | FORBIDDEN: two headcount threshold rows |

### Anti-Pattern Watch — Row Structure

| Column | Requirement |
|--------|------------|
| Anti-Pattern | Name of the anti-pattern |
| Why It Applies Here | MUST open with `[element name] (cat-N) —` |
| Mitigation | MUST contain a specific remediation action. FORBIDDEN: format guidance. |

### Constraints
| Constraint | Register |
|-----------|---------|
| All seven sections in org-chart.md | MUST |
| Omitting any section | FORBIDDEN |
| Exactly one verdict in Section 4 | MUST |
| Writing or omitting both verdicts | FORBIDDEN |
| Anti-pattern categories from required column for T2-VERDICT | MUST |
| Anti-pattern categories from FORBIDDEN column for T2-VERDICT | FORBIDDEN |
```

---

## V-05 — Compressed Lifecycle + Prominent Inertia Framing

**Variation axis:** Compressed to 3 phases (fewer phase transitions = less ordering-violation surface) with inertia advocate framed as the structural gatekeeper whose verdict is announced before role generation begins  
**Hypothesis:** Reducing phase count cuts the number of ordering-violation opportunities while foregrounding inertia increases the probability the model treats the verdict as a hard constraint rather than a formatting detail.

---

```markdown
You are executing the **org-build** skill.

## The Structural Gatekeeper

Before any role is named, before any area is drawn, the org-build skill asks one question:
**Can this org operate flat, or does its pressure profile warrant structure?**

The answer is not aesthetic. It is a verdict derived from observable signals. The inertia
advocate is the voice that computes this verdict and holds it. Every downstream output —
role count, role scope, anti-pattern categories, and the chart itself — is keyed to that
verdict. No output is produced before the verdict is recorded.

**Primary outputs**
1. `org-chart.md` — ASCII hierarchy, headcount table, inertia block, anti-patterns,
   operating rhythm, evolution roadmap
2. `.roles/{area}/{role}.md` — one file per role, five required fields

FORBIDDEN: beginning Phase 2 before Phase 1 RECORD block is emitted.
FORBIDDEN: beginning Phase 3 before Phase 2 RECORD block is emitted.

---

## Verbatim IA Scope Templates

Key selection to T2-PRESSURE. Copy the matching text verbatim into the `scope` field of the
inertia-advocate role file. FORBIDDEN: any deviation.

| T2-PRESSURE | Verbatim scope |
|-------------|----------------|
| NONE | Structural health is nominal. No flat-case pressure detected. Monitor headcount distribution at next annual planning cycle. No restructuring signal present. |
| LOW | Low flat-case pressure detected. Span-of-control metrics within tolerance. Track semi-annually. No immediate restructuring action required. |
| MODERATE | Moderate flat-case pressure detected. Review hiring plan against current team span. Assess span of control at next planning cycle. Flag for VP visibility before headcount decisions. |
| HIGH | High flat-case pressure detected. Escalate structural review to VP. A formal structural proposal MUST be submitted before the next headcount decision is approved. |
| CRITICAL | Critical flat-case pressure detected. Immediate restructuring required. FORBIDDEN: approving additional headcount before org redesign is ratified and approved. |

---

## Anti-Pattern Category Derivation

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

## Phase 1 — Classification and Verdict

This phase reads inputs, classifies the structural context, and produces the inertia verdict
that gates all subsequent output.

### Task Steps

1. **Classify inputs.**
   - Read `--depth` flag. If absent, default to `standard`.
   - Determine structure signal: `EXISTING` if scan results are present; `GREENFIELD` otherwise.

2. **Assess flat-case pressure.**
   Evaluate across: span of control, decision latency, role ambiguity, cross-team coordination
   cost, headcount trajectory.
   Assign FLAT-CASE-PRESSURE from: `NONE | LOW | MODERATE | HIGH | CRITICAL`.

3. **Derive verdict.**
   - NONE or LOW → `CAN-OPERATE-FLAT`
   - MODERATE, HIGH, or CRITICAL → `STRUCTURE-WARRANTED`

### Constraints

- MUST assign T1-DEPTH-FLAG exactly from: [standard | deep]
- MUST assign T1-STRUCTURE-SIGNAL exactly from: [EXISTING | GREENFIELD]
- MUST assign T1-PRESSURE from closed set: [NONE | LOW | MODERATE | HIGH | CRITICAL]
- MUST issue exactly one verdict: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error.
- FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
- FORBIDDEN: beginning Phase 2 before the Phase 1 RECORD block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-STRUCTURE-SIGNAL: [EXISTING | GREENFIELD]
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## Phase 2 — Role Enumeration and Role Files

### Input Contract

- T1-DEPTH-FLAG (Phase 1 RECORD block) — MUST be present. Governs role count floor.
- T1-VERDICT (Phase 1 RECORD block) — MUST be present. Governs anti-pattern categories.
- T1-PRESSURE (Phase 1 RECORD block) — MUST be present. Governs IA scope template.
- FORBIDDEN: executing Phase 2 before Phase 1 RECORD block is emitted.

### Task Steps

**T2.1 — Enumerate roles.**

Apply the depth-conditional count:
- T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles.
- T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles.

FORBIDDEN: enumerating fewer than 20 roles when T1-DEPTH-FLAG = standard.
FORBIDDEN: enumerating fewer than 50 roles when T1-DEPTH-FLAG = deep.

Group roles into min 2 named area subdirectories.
MUST include role `inertia-advocate`.
FORBIDDEN: omitting `inertia-advocate`.

**T2.2 — Write role files.**

Path: `.roles/{area}/{role-name}.md`

Every file MUST contain:
```yaml
orientation: <what this role is optimizing for>
lens: <how this role evaluates decisions>
expertise: <domain knowledge this role holds>
scope: <what this role owns and is accountable for>
collaborates_with: <list of roles>
```

FORBIDDEN: omitting orientation, lens, expertise, scope, or collaborates_with from any file.

**T2.3 — Apply IA scope template.**

Look up T1-PRESSURE in the Verbatim IA Scope Templates table. Copy the matching text verbatim
into the `scope` field of the `inertia-advocate` role file.
FORBIDDEN: paraphrasing, adapting, or abbreviating the template.

**T2.4 — Organize file structure.**

MUST place all role files under `.roles/{area}/`.
FORBIDDEN: placing all files flat under `.roles/` with no area subdirectory.

### Constraints

- MUST write all five fields in every role file.
- MUST apply IA scope verbatim from template keyed to T1-PRESSURE.
- MUST create min 2 area subdirectories.
- FORBIDDEN: beginning Phase 3 before the Phase 2 RECORD block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT: [integer]
T2-AREA-COUNT: [integer ≥ 2]
T2-ROLE-FILE-STATUS: [COMPLETE | PARTIAL]
T2-IA-SCOPE-APPLIED: [YES | NO]
===
```

---

## Phase 3 — Write org-chart.md

### Input Contract

- T1-PRESSURE (Phase 1 RECORD block) — MUST be present for FLAT-CASE-PRESSURE entry.
- T1-VERDICT (Phase 1 RECORD block) — MUST be present for verdict block and category derivation.
- T2-ROLE-COUNT (Phase 2 RECORD block) — MUST be present for headcount table.
- T2-ROLE-FILE-STATUS (Phase 2 RECORD block) — MUST be `COMPLETE`.
- FORBIDDEN: executing Phase 3 before Phase 2 RECORD block is emitted.

### Task Steps

Write `org-chart.md` containing all seven sections below.

**Section 1 — ASCII Org Hierarchy**

Box-and-line diagram with min 2 org levels. Slot each role as `[{{role-name}}]`.
FORBIDDEN: replacing diagram with a flat name list.

Example shape:
```
[Org Root]
 ├── [{{Area A Lead}}]
 │    ├── [{{role-name}}]
 │    └── [{{role-name}}]
 └── [{{Area B Lead}}]
      └── [{{role-name}}]
```

**Section 2 — Headcount by Area**

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

MUST include columns: Area, Headcount, Key Roles, Decides, Escalates.
FORBIDDEN: omitting Decides or Escalates.

**Section 3 — Level Distribution**

| Level | Count | % of Org |
|-------|-------|----------|

**Section 4 — Inertia Assessment**

```
FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
```

FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.

**Section 5 — Anti-Pattern Watch**

Select anti-pattern categories using the Category Derivation table keyed to T1-VERDICT.
FORBIDDEN: using categories from the FORBIDDEN column for T1-VERDICT.

| Anti-Pattern | Why It Applies Here | Mitigation |
|-------------|---------------------|------------|

- MUST include min 2 rows.
- Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
- FORBIDDEN: plain prose opening in "Why It Applies Here".
- Every Mitigation cell MUST contain a specific remediation action.
- FORBIDDEN: format guidance, column-structure notes, or descriptive instructions in
  Mitigation cells.

**Section 6 — Operating Rhythm + Committee Charters**

| Cadence | Meeting | Owner | Participants | Quorum |
|---------|---------|-------|--------------|--------|

MUST include min 3 distinct rows: ROB, shiproom, and governance.

For every governance meeting, write a charter block:
```
Charter: [Meeting Name]
Purpose: [one sentence]
Owner: [role]
Participants: [list]
Quorum: N of M
Decision Rights: [what this committee decides]
```
FORBIDDEN: omitting Quorum from any charter.

**Section 7 — Org Evolution Roadmap**

| Trigger | Type | Action |
|---------|------|--------|

MUST include min 2 rows. Row 1 type: headcount threshold. Row 2 type: different from Row 1.
FORBIDDEN: two headcount threshold rows.

### Constraints

- MUST write all seven sections.
- FORBIDDEN: omitting any section.
- MUST emit `FLAT-CASE-PRESSURE:` with a closed-set rating.
- MUST issue exactly one verdict.
- FORBIDDEN: writing both or neither verdict.
- MUST select anti-pattern categories from required column for T1-VERDICT.
- FORBIDDEN: using FORBIDDEN-column categories for T1-VERDICT.
- MUST include min 2 anti-pattern rows with cat-N citation opening syntax.
- MUST include Quorum in every committee charter.
- Row 1 of Evolution Roadmap MUST be a headcount threshold trigger.
```

---

### Variation Summary

| Variation | Axis | Hypothesis | Phase Count | Key Structural Difference |
|-----------|------|-----------|-------------|--------------------------|
| V-01 | Role sequence | Verdict-first prevents category drift | 5 | Phase 2 = inertia before roles |
| V-02 | Output format | Tables reduce missed constraints | 5 | All constraints in constraint tables |
| V-03 | Lifecycle emphasis | Explicit segmentation reduces skip behavior | 5 | ══ headers, separated Task/Constraints, verbose RECORD blocks |
| V-04 | V-01 + V-02 | Both axes compound compliance gains | 5 | Verdict-first + all-table constraints |
| V-05 | Compressed + inertia-prominent | Fewer transitions cut ordering violations; framing elevates verdict weight | 3 | Phases 1+2+3 collapsed; Phase 1 verdict gates Phase 2 roles |
