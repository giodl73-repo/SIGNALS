# org-build Skill — Round 9 Variations (V-01 through V-05)

---

## V-01 — Lifecycle Emphasis: Maximum Phase Boundary Explicitness

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Dedicating the most prompt real-estate to phase boundary mechanics — with named record blocks, input contracts, and per-boundary ordering FORBIDDENs — will maximize coverage of C-14, C-20, C-21, C-23, C-24 while leaving format criteria to terse but sufficient templates.

---

You are generating a complete org structure from a repository scan or scan results.

**Accepted inputs**
- `--from-scan <file>` — pre-generated scan results file
- `--from-repo <path>` — scan the repository directly
- `--depth standard|deep` — standard: 20–30 roles; deep: 50+ roles; default is standard

---

### PHASE 1 — Repository Analysis

**Execution**: Count distinct module, service, or area boundaries in the source. Classify the dominant structural topology.

**Phase 1 Gate**
FORBIDDEN: beginning Phase 2 before emitting this record block.

```
=== RECORD: PHASE-1 ===
T1-REPO-COUNT: <integer — number of distinct areas/modules>
T1-STRUCTURE-TYPE: <FLAT | LAYERED | MIXED>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 — Inertia Assessment

**Input contract**
MUST read `T1-REPO-COUNT` and `T1-STRUCTURE-TYPE` from the Phase 1 record block before executing.
FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

**Execution**: Assign a `FLAT-CASE-PRESSURE` rating using this table:

| Rating | Condition |
|---|---|
| LOW | T1-REPO-COUNT ≤ 5 AND T1-STRUCTURE-TYPE = FLAT |
| MODERATE | T1-REPO-COUNT ≤ 10 OR T1-STRUCTURE-TYPE = FLAT |
| ELEVATED | T1-REPO-COUNT > 10 AND T1-STRUCTURE-TYPE = LAYERED |
| CRITICAL | T1-REPO-COUNT > 20 OR coupling density is high across MIXED topology |

Then assign the verdict:
- `CAN-OPERATE-FLAT` — if FLAT-CASE-PRESSURE is LOW or MODERATE
- `STRUCTURE-WARRANTED` — if FLAT-CASE-PRESSURE is ELEVATED or CRITICAL

**Verdict guard**: Only one verdict applies. FORBIDDEN: writing both. FORBIDDEN: omitting both. Writing both is an error. Writing neither is an error.

**Phase 2 Gate**
FORBIDDEN: beginning Phase 3 before emitting this record block.

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: <LOW | MODERATE | ELEVATED | CRITICAL>
T2-VERDICT: <CAN-OPERATE-FLAT | STRUCTURE-WARRANTED>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 — Role Generation

**Input contract**
MUST read `T2-PRESSURE` and `T2-VERDICT` from the Phase 2 record block before executing.
FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

**Execution**: Generate roles across a minimum of these areas: Engineering, Product, Design, Data, Operations, and a cross-functional coordination layer. MUST include `inertia-advocate` in every generation.

Role count target — standard: 20–30 files; deep: 50+ files. Below lower bound fails.

**Inertia-Advocate scope**: MUST apply the verbatim template keyed to T2-PRESSURE. Paraphrase fails. Adaptation fails. Only the exact text below satisfies this criterion.

| T2-PRESSURE | Inertia-Advocate Scope (verbatim) |
|---|---|
| LOW | "Represents teams resisting structural change at low pressure. Reviews all proposals for scope creep or hierarchy inflation. Advocates for minimal overhead and autonomous team operation." |
| MODERATE | "Represents current-state teams operating under moderate structural pressure. Challenges each proposed role addition against headcount-to-coordination-overhead ratio. Advocates for flat resolution paths before any escalation tier is added." |
| ELEVATED | "Represents established teams facing elevated pressure to restructure. Reviews every coordination mechanism for flat-org equivalence. Blocks structural changes that can be handled by clarifying existing scope or adding a standing sync." |
| CRITICAL | "Represents an org under critical flat-case pressure where structural change has become operationally necessary. Focuses advocacy on preserving maximum flatness within the warranted structure. Ensures no layer is added without a documented decision-volume justification." |

**Phase 3 Gate**
FORBIDDEN: beginning Phase 4 before emitting this record block.

```
=== RECORD: PHASE-3 ===
T3-ROLE-COUNT: <integer — total role files>
T3-AREA-LIST: <comma-separated area subdirectory names>
=== END RECORD: PHASE-3 ===
```

---

### PHASE 4 — Output Assembly

**Input contract**
MUST read `T2-PRESSURE`, `T2-VERDICT`, `T3-ROLE-COUNT`, `T3-AREA-LIST` from their respective record blocks before executing.
FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.

---

#### Artifact 1: org-chart.md

**ASCII Hierarchy** — MUST contain a box-and-line diagram with at minimum 2 org levels. A flat name list fails.

Pre-print skeleton (fill {{slots}} from gate variables):

```
┌─────────────────────────────────────────┐
│             [TOP-ROLE]                  │
└──────────────┬──────────────────────────┘
               │
   ┌───────────┼───────────┐
   │           │           │
┌──┴──┐     ┌──┴──┐     ┌──┴──┐
│{{T3-AREA-LIST[0]}}│ │{{T3-AREA-LIST[1]}}│ │{{T3-AREA-LIST[2]}}│
└─────┘     └─────┘     └─────┘
```

**Headcount by Area Table** — MUST include exactly these columns: `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates`. A table missing Decides or Escalates fails.

| Area | Headcount | Key Roles | Decides | Escalates |
|---|---|---|---|---|
| {{T3-AREA-LIST[n]}} | {{count}} | {{key-roles}} | {{decision-domain}} | {{escalation-condition}} |

**Inertia Assessment Block** — MUST include both lines. One verdict only.

```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```

FORBIDDEN: writing both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED`. FORBIDDEN: omitting both.

**Operating Rhythm Table** — MUST include 3+ rows with distinct cadence types: one ROB, one shiproom, one governance body.

| Meeting | Cadence | Owner | Participants | Purpose |
|---|---|---|---|---|

**Committee Charters** — For each governance meeting in the rhythm table, MUST include a charter with all five fields. Quorum MUST be expressed as `N of M` (fraction form).

```
Name:
Purpose:
Participants:
Quorum: N of M
Owner:
```

**Org Evolution Roadmap** — MUST include 2+ rows. Row 1 MUST be a headcount threshold. Row 2 MUST be a different trigger category (coupling, decision latency, or dependency depth). Two headcount rows fails.

| Trigger Category | Condition | Recommended Change |
|---|---|---|
| Headcount | {{threshold}} | {{structural change}} |
| {{non-headcount category}} | {{condition}} | {{structural change}} |

**Anti-Pattern Watch** — Category selection is derived from T2-VERDICT:

- `CAN-OPERATE-FLAT` → MUST use cat-2 and cat-3. FORBIDDEN: cat-1. FORBIDDEN: cat-4.
- `STRUCTURE-WARRANTED` → MUST use cat-1 and cat-4. FORBIDDEN: cat-2. FORBIDDEN: cat-3.

MUST include 2+ rows. Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST contain a specific remediation action. Mitigation cells containing format guidance or column-structure instructions fail.

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|---|---|---|---|
| {{name}} | cat-{{N}} | [{{element}}] (cat-{{N}}) — {{reason tied to T2-VERDICT}} | {{remediation action}} |

---

#### Artifact 2: .craft/roles/ Files

MUST group role files under area subdirectories. Minimum 2 area subdirs. All roles flat with no grouping fails.

```
.craft/roles/
  {{T3-AREA-LIST[0]}}/
    {{role}}.md
  inertia/
    inertia-advocate.md
```

Every role file MUST contain all five fields. Any missing field fails.

```yaml
orientation: <inward | outward | cross-functional>
lens: <primary analytical frame>
expertise: <core skill domain>
scope: <decision and accountability boundary>
collaborates_with: <list of role names>
```

The `inertia-advocate` scope MUST contain the exact verbatim text from the T2-PRESSURE template table in Phase 3.

---

### Full Constraint Register

| Constraint | Scope |
|---|---|
| FORBIDDEN: beginning Phase N before Phase N-1 record block is emitted | All phase boundaries |
| FORBIDDEN: writing both verdicts | Phase 2 gate, Phase 4 inertia block |
| FORBIDDEN: omitting both verdicts | Phase 2 gate, Phase 4 inertia block |
| FORBIDDEN: paraphrasing inertia-advocate scope | Phase 3 assignment, Phase 4 role file |
| FORBIDDEN: cat-1 or cat-4 when CAN-OPERATE-FLAT | Phase 4 anti-pattern table |
| FORBIDDEN: cat-2 or cat-3 when STRUCTURE-WARRANTED | Phase 4 anti-pattern table |
| FORBIDDEN: format guidance in Mitigation cells | Phase 4 anti-pattern table |
| FORBIDDEN: advisory language (should, prefer, consider) in any constraint | All phases |

---

---

## V-02 — Inertia Framing: Inertia-Advocate as Primary Lens

**Variation axis**: Inertia framing
**Hypothesis**: Running the inertia assessment as the first output phase — before role generation — and framing the entire prompt as "building an org the inertia-advocate would approve" creates stronger natural derivation of C-08, C-11, C-12, C-17, C-18. The advocate's verdict drives role count targets directly rather than indirectly.

---

You are generating a complete org structure. Every design decision in this org MUST be defensible against the inertia-advocate role — the voice that represents teams and processes resisting structural change. The inertia-advocate is generated first and governs what follows.

**Accepted inputs**
- `--from-scan <file>` or `--from-repo <path>`
- `--depth standard|deep`

---

### PHASE 1 — Source Analysis

Analyze the source. Count distinct area or module boundaries. Classify topology.

**Phase 1 Gate**
FORBIDDEN: beginning Phase 2 before emitting this record block.

```
=== RECORD: PHASE-1 ===
T1-REPO-COUNT: <integer>
T1-STRUCTURE-TYPE: <FLAT | LAYERED | MIXED>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 — Inertia Verdict (governs all subsequent phases)

**Input contract**: MUST read `T1-REPO-COUNT` and `T1-STRUCTURE-TYPE` from the Phase 1 record block. FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

Assess `FLAT-CASE-PRESSURE`:

| Rating | Condition |
|---|---|
| LOW | T1-REPO-COUNT ≤ 5 AND T1-STRUCTURE-TYPE = FLAT |
| MODERATE | T1-REPO-COUNT ≤ 10 OR topology is predominantly FLAT |
| ELEVATED | T1-REPO-COUNT > 10 AND T1-STRUCTURE-TYPE = LAYERED |
| CRITICAL | T1-REPO-COUNT > 20 OR high coupling across MIXED topology |

Assign exactly one verdict. FORBIDDEN: writing both. FORBIDDEN: omitting both. Writing both is an error. Writing neither is an error.

- `CAN-OPERATE-FLAT` — FLAT-CASE-PRESSURE is LOW or MODERATE
- `STRUCTURE-WARRANTED` — FLAT-CASE-PRESSURE is ELEVATED or CRITICAL

The verdict now governs:
1. Role count target: CAN-OPERATE-FLAT → lean to lower bound of depth range; STRUCTURE-WARRANTED → lean to upper bound
2. Inertia-advocate scope text (verbatim lookup below)
3. Anti-pattern category selection (category exclusion rules below)

**Phase 2 Gate**
FORBIDDEN: beginning Phase 3 before emitting this record block.

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: <LOW | MODERATE | ELEVATED | CRITICAL>
T2-VERDICT: <CAN-OPERATE-FLAT | STRUCTURE-WARRANTED>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 — Inertia-Advocate Role (generated before all other roles)

**Input contract**: MUST read `T2-PRESSURE` and `T2-VERDICT` from the Phase 2 record block. FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

Generate the inertia-advocate role file first. Its `scope` field MUST be set verbatim from this lookup. Paraphrase fails. Any deviation from the exact text fails.

| T2-PRESSURE | Scope text (verbatim — copy exactly) |
|---|---|
| LOW | "Represents teams resisting structural change at low pressure. Reviews all proposals for scope creep or hierarchy inflation. Advocates for minimal overhead and autonomous team operation." |
| MODERATE | "Represents current-state teams operating under moderate structural pressure. Challenges each proposed role addition against headcount-to-coordination-overhead ratio. Advocates for flat resolution paths before any escalation tier is added." |
| ELEVATED | "Represents established teams facing elevated pressure to restructure. Reviews every coordination mechanism for flat-org equivalence. Blocks structural changes that can be handled by clarifying existing scope or adding a standing sync." |
| CRITICAL | "Represents an org under critical flat-case pressure where structural change has become operationally necessary. Focuses advocacy on preserving maximum flatness within the warranted structure. Ensures no layer is added without a documented decision-volume justification." |

Emit the inertia-advocate role in `.craft/roles/inertia/inertia-advocate.md` with all five fields present: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

**Phase 3 Gate**
FORBIDDEN: beginning Phase 4 before emitting this record block.

```
=== RECORD: PHASE-3 ===
T3-IA-SCOPE-HASH: <first 8 words of scope text applied, for verification>
T3-IA-FILE: .craft/roles/inertia/inertia-advocate.md
=== END RECORD: PHASE-3 ===
```

---

### PHASE 4 — Full Role Generation

**Input contract**: MUST read `T2-VERDICT`, `T2-PRESSURE`, `T3-IA-SCOPE-HASH`, `T3-IA-FILE` from their record blocks. FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

Generate all remaining roles. Inertia-advocate was generated in Phase 3 — MUST NOT regenerate it with different scope text.

Role count target (standard): CAN-OPERATE-FLAT → 20–24 roles; STRUCTURE-WARRANTED → 25–30 roles. Deep adds 50+ in both cases.

Cover minimum areas: Engineering, Product, Design, Data, Operations, cross-functional coordination. MUST create area subdirectories under `.craft/roles/`. Minimum 2 area subdirs beyond `inertia/`.

Every role file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

**Phase 4 Gate**
FORBIDDEN: beginning Phase 5 before emitting this record block.

```
=== RECORD: PHASE-4 ===
T4-ROLE-COUNT: <integer>
T4-AREA-LIST: <comma-separated list>
=== END RECORD: PHASE-4 ===
```

---

### PHASE 5 — org-chart.md Assembly

**Input contract**: MUST read `T2-PRESSURE`, `T2-VERDICT`, `T4-ROLE-COUNT`, `T4-AREA-LIST` from their record blocks. FORBIDDEN: executing Phase 5 before Phase 4 record block is emitted.

**ASCII Hierarchy**: MUST include a box-and-line diagram with at minimum 2 org levels. A flat list fails.

Pre-print skeleton (slots keyed to gate variables):

```
┌───────────────────────────────────┐
│  [TOP-ROLE]                       │
└────────────┬──────────────────────┘
             │
  ┌──────────┼──────────┐
  ▼          ▼          ▼
{{T4-AREA-LIST[0]}}  {{T4-AREA-LIST[1]}}  {{T4-AREA-LIST[n]}}
```

**Headcount by Area Table** — columns: `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates`. Missing Decides or Escalates fails.

**Inertia Assessment Block** (derived from T2-PRESSURE and T2-VERDICT):

```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

**Anti-Pattern Watch** — categories are derived from T2-VERDICT, not chosen independently:

- T2-VERDICT = `CAN-OPERATE-FLAT` → MUST use cat-2 and cat-3. FORBIDDEN: cat-1. FORBIDDEN: cat-4.
- T2-VERDICT = `STRUCTURE-WARRANTED` → MUST use cat-1 and cat-4. FORBIDDEN: cat-2. FORBIDDEN: cat-3.

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST contain a remediation action. Cells with format instructions fail.

**Operating Rhythm Table** — 3+ rows: ROB, shiproom, governance. Each governance meeting MUST have a charter with Name, Purpose, Participants, Quorum (`N of M`), Owner.

**Org Evolution Roadmap** — 2+ rows, Row 1 headcount threshold, Row 2 different category.

---

---

## V-03 — Output Format: Table-Heavy Schema

**Variation axis**: Output format
**Hypothesis**: Defining every artifact and record block as an explicit named table with typed column schemas — and expressing all constraint rules as table rows — reduces format ambiguity, improves C-05, C-07, C-22 compliance, and makes template slots unambiguous. All phase gates are expressed as single-row emission tables.

---

You are generating a complete org structure artifact set. All outputs are defined below as typed table schemas. MUST produce every table. MUST fill every named slot. FORBIDDEN: omitting any required column or row.

**Inputs**: `--from-scan <file>` | `--from-repo <path>` | `--depth standard|deep`

---

### Phase 1 — Source Analysis

Scan the source. Emit the Phase 1 gate table before any further execution.

FORBIDDEN: executing Phase 2 before emitting the Phase 1 gate table.

**Phase 1 Gate Table**

| Variable | Type | Value |
|---|---|---|
| T1-REPO-COUNT | integer | `<fill>` |
| T1-STRUCTURE-TYPE | enum: FLAT \| LAYERED \| MIXED | `<fill>` |

---

### Phase 2 — Inertia Assessment

**Input contract**: MUST read `T1-REPO-COUNT` and `T1-STRUCTURE-TYPE` from the Phase 1 gate table. FORBIDDEN: executing Phase 2 before Phase 1 gate table is emitted.

**Pressure lookup table**:

| T1-REPO-COUNT | T1-STRUCTURE-TYPE | T2-PRESSURE |
|---|---|---|
| ≤ 5 | FLAT | LOW |
| ≤ 10 | FLAT or MIXED | MODERATE |
| > 10 | LAYERED | ELEVATED |
| > 20 | any | CRITICAL |

**Verdict derivation table**:

| T2-PRESSURE | T2-VERDICT |
|---|---|
| LOW | CAN-OPERATE-FLAT |
| MODERATE | CAN-OPERATE-FLAT |
| ELEVATED | STRUCTURE-WARRANTED |
| CRITICAL | STRUCTURE-WARRANTED |

**Single-verdict guard table** (apply before emitting gate):

| Condition | Status |
|---|---|
| Both verdicts written | FORBIDDEN — error |
| Neither verdict written | FORBIDDEN — error |
| Exactly one verdict written | PASS |

FORBIDDEN: executing Phase 3 before emitting the Phase 2 gate table.

**Phase 2 Gate Table**

| Variable | Type | Value |
|---|---|---|
| T2-PRESSURE | enum: LOW \| MODERATE \| ELEVATED \| CRITICAL | `<fill>` |
| T2-VERDICT | enum: CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED | `<fill>` |

---

### Phase 3 — Role Generation

**Input contract**: MUST read `T2-PRESSURE` and `T2-VERDICT` from the Phase 2 gate table. FORBIDDEN: executing Phase 3 before Phase 2 gate table is emitted.

**Role count schema**:

| Flag | Minimum | Maximum |
|---|---|---|
| standard | 20 | 30 |
| deep | 50 | — |

**Inertia-advocate scope lookup table** (verbatim — no paraphrase, no adaptation):

| T2-PRESSURE | Scope Text |
|---|---|
| LOW | "Represents teams resisting structural change at low pressure. Reviews all proposals for scope creep or hierarchy inflation. Advocates for minimal overhead and autonomous team operation." |
| MODERATE | "Represents current-state teams operating under moderate structural pressure. Challenges each proposed role addition against headcount-to-coordination-overhead ratio. Advocates for flat resolution paths before any escalation tier is added." |
| ELEVATED | "Represents established teams facing elevated pressure to restructure. Reviews every coordination mechanism for flat-org equivalence. Blocks structural changes that can be handled by clarifying existing scope or adding a standing sync." |
| CRITICAL | "Represents an org under critical flat-case pressure where structural change has become operationally necessary. Focuses advocacy on preserving maximum flatness within the warranted structure. Ensures no layer is added without a documented decision-volume justification." |

MUST include an `inertia-advocate` role. Its `scope` MUST be the exact text from the row matching T2-PRESSURE.

FORBIDDEN: executing Phase 4 before emitting the Phase 3 gate table.

**Phase 3 Gate Table**

| Variable | Type | Value |
|---|---|---|
| T3-ROLE-COUNT | integer | `<fill>` |
| T3-AREA-LIST | list of strings | `<fill>` |
| T3-IA-PRESSURE-APPLIED | enum: LOW \| MODERATE \| ELEVATED \| CRITICAL | `<fill>` |

---

### Phase 4 — Output Assembly

**Input contract**: MUST read all variables from Phase 2 and Phase 3 gate tables. FORBIDDEN: executing Phase 4 before Phase 3 gate table is emitted.

---

**Output Table A — org-chart.md: ASCII Hierarchy**

MUST contain a box-and-line diagram with minimum 2 levels. Template (fill slots from T3-AREA-LIST):

```
┌──────────────────────────────┐
│  [TOP-ROLE-NAME]             │
└──────────────┬───────────────┘
               │
┌──────────────┼──────────────┐
▼              ▼              ▼
{{T3-AREA-LIST[0]}}  {{T3-AREA-LIST[1]}}  {{T3-AREA-LIST[n]}}
```

---

**Output Table B — Headcount by Area**

Schema (MUST include all 5 columns):

| Area | Headcount | Key Roles | Decides | Escalates |
|---|---|---|---|---|
| {{T3-AREA-LIST[n]}} | `<int>` | `<names>` | `<decision domain>` | `<escalation condition>` |

Missing `Decides` or `Escalates` columns fails.

---

**Output Table C — Inertia Assessment**

MUST appear as this exact two-row table:

| Variable | Value |
|---|---|
| FLAT-CASE-PRESSURE | {{T2-PRESSURE}} |
| VERDICT | {{T2-VERDICT}} |

FORBIDDEN: writing both `CAN-OPERATE-FLAT` and `STRUCTURE-WARRANTED` in any form. FORBIDDEN: omitting both. Writing both is an error. Writing neither is an error.

---

**Output Table D — Operating Rhythm**

Schema (MUST include 3+ rows — one ROB, one shiproom, one governance):

| Meeting | Cadence | Owner | Participants | Purpose |
|---|---|---|---|---|

---

**Output Table E — Committee Charters**

One charter per governance meeting. MUST include all 5 fields. `Quorum` MUST be expressed as `N of M`.

| Field | Value |
|---|---|
| Name | `<meeting name>` |
| Purpose | `<purpose>` |
| Participants | `<list>` |
| Quorum | `<N of M>` |
| Owner | `<role name>` |

---

**Output Table F — Org Evolution Roadmap**

MUST include 2+ rows. Row 1 MUST be headcount. Row 2 MUST be a different trigger category.

| Trigger Category | Condition | Recommended Change |
|---|---|---|
| Headcount | `<threshold>` | `<change>` |
| `<non-headcount category>` | `<condition>` | `<change>` |

Two headcount rows fails.

---

**Output Table G — Anti-Pattern Watch**

Category derivation (from T2-VERDICT):

| T2-VERDICT | Required Categories | Forbidden Categories |
|---|---|---|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1 FORBIDDEN: cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2 FORBIDDEN: cat-3 |

Schema (MUST include 2+ rows):

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|---|---|---|---|
| `<name>` | cat-N | [element name] (cat-N) — `<reason>` | `<remediation action>` |

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation MUST be a remediation action, not format guidance.

---

**Output: .craft/roles/ Files**

Role file schema — all five fields MUST be present in every file:

| Field | Type |
|---|---|
| orientation | inward \| outward \| cross-functional |
| lens | string — primary analytical frame |
| expertise | string — core skill domain |
| scope | string — decision and accountability boundary |
| collaborates_with | list of role names |

Directory schema:

```
.craft/roles/
  {{T3-AREA-LIST[0]}}/
  {{T3-AREA-LIST[1]}}/
  inertia/
    inertia-advocate.md
```

MUST have 2+ area subdirs. The `inertia-advocate.md` scope MUST contain verbatim text from Output Table phase 3 lookup (T3-IA-PRESSURE-APPLIED row).

---

---

## V-04 — Role Sequence + Phrasing Register: Dependency-Ordered Roles, Uniform Imperative

**Variation axis**: Role sequence + phrasing register
**Hypothesis**: Generating roles in structural dependency order (governance tier first, then area leads, then ICs, then cross-functional, then inertia-advocate last as validator) while using MUST/FORBIDDEN uniformly for every sentence in every constraint context will maximize C-19, C-03, and produce a coherent hierarchy where the inertia-advocate's scope is always keyed to a settled verdict.

---

You are generating a complete org structure. MUST follow phases in exact order. MUST use MUST or FORBIDDEN for every constraint. FORBIDDEN: advisory language (should, prefer, consider, typically) in any constraint context.

**Inputs**: `--from-scan <file>` | `--from-repo <path>` | `--depth standard|deep`

---

### Phase 1 — Source Scan

MUST count distinct module, service, and area boundaries visible in the source.
MUST classify the dominant structural topology as FLAT, LAYERED, or MIXED.
FORBIDDEN: proceeding to Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
T1-REPO-COUNT: <integer>
T1-STRUCTURE-TYPE: <FLAT | LAYERED | MIXED>
=== END RECORD: PHASE-1 ===
```

---

### Phase 2 — Pressure and Verdict

MUST read T1-REPO-COUNT and T1-STRUCTURE-TYPE from the Phase 1 record block.
FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

MUST assign FLAT-CASE-PRESSURE using:
- LOW: T1-REPO-COUNT ≤ 5 AND T1-STRUCTURE-TYPE = FLAT
- MODERATE: T1-REPO-COUNT ≤ 10 OR topology is predominantly FLAT
- ELEVATED: T1-REPO-COUNT > 10 AND T1-STRUCTURE-TYPE = LAYERED
- CRITICAL: T1-REPO-COUNT > 20 OR high coupling across MIXED

MUST assign exactly one verdict:
- CAN-OPERATE-FLAT: T2-PRESSURE is LOW or MODERATE
- STRUCTURE-WARRANTED: T2-PRESSURE is ELEVATED or CRITICAL

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Writing both is an error. Writing neither is an error.

FORBIDDEN: proceeding to Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
T2-PRESSURE: <LOW | MODERATE | ELEVATED | CRITICAL>
T2-VERDICT: <CAN-OPERATE-FLAT | STRUCTURE-WARRANTED>
=== END RECORD: PHASE-2 ===
```

---

### Phase 3 — Governance Tier Roles (generated first)

MUST read T2-VERDICT and T2-PRESSURE from the Phase 2 record block.
FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

MUST generate governance-tier roles first. Governance roles MUST include: one engineering lead, one product lead, one design lead, one data lead, one operations lead. If T2-VERDICT = STRUCTURE-WARRANTED, MUST add a cross-functional coordination role. If T2-VERDICT = CAN-OPERATE-FLAT, FORBIDDEN: adding a dedicated coordination management layer.

FORBIDDEN: proceeding to Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
T3-GOV-ROLE-COUNT: <integer>
T3-GOV-AREA-LIST: <comma-separated governance area names>
=== END RECORD: PHASE-3 ===
```

---

### Phase 4 — Area Lead and IC Roles

MUST read T3-GOV-ROLE-COUNT and T3-GOV-AREA-LIST from the Phase 3 record block.
FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.

MUST generate area lead roles under each governance area in T3-GOV-AREA-LIST.
MUST generate IC-level specialist roles under each area lead.
MUST target depth: standard = 20–30 total roles across all tiers; deep = 50+ total roles.

Every role file MUST contain all five fields: orientation, lens, expertise, scope, collaborates_with. FORBIDDEN: omitting any field.

FORBIDDEN: proceeding to Phase 5 before emitting the Phase 4 record block.

```
=== RECORD: PHASE-4 ===
T4-TOTAL-ROLE-COUNT: <integer — all roles excluding inertia-advocate>
T4-FULL-AREA-LIST: <comma-separated all area subdirectory names>
=== END RECORD: PHASE-4 ===
```

---

### Phase 5 — Inertia-Advocate Role (generated last, validates org structure)

MUST read T2-PRESSURE, T2-VERDICT, T4-TOTAL-ROLE-COUNT, T4-FULL-AREA-LIST from their record blocks.
FORBIDDEN: executing Phase 5 before the Phase 4 record block is emitted.

MUST generate the inertia-advocate role as the final role. MUST place the file at `.craft/roles/inertia/inertia-advocate.md`.

MUST set the `scope` field to the verbatim text below keyed to T2-PRESSURE. FORBIDDEN: paraphrasing. FORBIDDEN: adapting the template. FORBIDDEN: writing any scope text not in this table.

| T2-PRESSURE | Scope (verbatim — copy exactly) |
|---|---|
| LOW | "Represents teams resisting structural change at low pressure. Reviews all proposals for scope creep or hierarchy inflation. Advocates for minimal overhead and autonomous team operation." |
| MODERATE | "Represents current-state teams operating under moderate structural pressure. Challenges each proposed role addition against headcount-to-coordination-overhead ratio. Advocates for flat resolution paths before any escalation tier is added." |
| ELEVATED | "Represents established teams facing elevated pressure to restructure. Reviews every coordination mechanism for flat-org equivalence. Blocks structural changes that can be handled by clarifying existing scope or adding a standing sync." |
| CRITICAL | "Represents an org under critical flat-case pressure where structural change has become operationally necessary. Focuses advocacy on preserving maximum flatness within the warranted structure. Ensures no layer is added without a documented decision-volume justification." |

FORBIDDEN: proceeding to Phase 6 before emitting the Phase 5 record block.

```
=== RECORD: PHASE-5 ===
T5-IA-FILE: .craft/roles/inertia/inertia-advocate.md
T5-FINAL-ROLE-COUNT: <T4-TOTAL-ROLE-COUNT + 1>
=== END RECORD: PHASE-5 ===
```

---

### Phase 6 — org-chart.md Assembly

MUST read all prior record block variables.
FORBIDDEN: executing Phase 6 before the Phase 5 record block is emitted.

**ASCII Hierarchy** — MUST include a box-and-line diagram with minimum 2 org levels. FORBIDDEN: substituting a flat name list for the diagram.

Skeleton (slots keyed to gate variables — MUST fill all slots):

```
┌────────────────────────────────────────┐
│  [GOVERNANCE-TOP]                      │
└───────────────┬────────────────────────┘
                │
   ┌────────────┼────────────┐
   ▼            ▼            ▼
{{T4-FULL-AREA-LIST[0]}}  {{T4-FULL-AREA-LIST[1]}}  {{T4-FULL-AREA-LIST[n]}}
  ({{headcount}})          ({{headcount}})          ({{headcount}})
```

**Headcount by Area Table** — MUST include columns: `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates`. FORBIDDEN: omitting Decides. FORBIDDEN: omitting Escalates.

**Inertia Assessment** — MUST include:

```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```

FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither verdict.

**Operating Rhythm** — MUST include 3+ rows: one ROB row, one shiproom row, one governance row.

| Meeting | Cadence | Owner | Participants | Purpose |

**Committee Charters** — MUST include one charter per governance meeting. Every charter MUST contain Name, Purpose, Participants, Quorum (expressed as `N of M`), Owner.

**Org Evolution Roadmap** — MUST include 2+ rows. Row 1 MUST be headcount threshold. Row 2 MUST be a different trigger category. FORBIDDEN: two headcount threshold rows.

**Anti-Pattern Watch** — MUST derive category selection from T2-VERDICT:

- T2-VERDICT = CAN-OPERATE-FLAT → MUST use cat-2 and cat-3. FORBIDDEN: cat-1. FORBIDDEN: cat-4.
- T2-VERDICT = STRUCTURE-WARRANTED → MUST use cat-1 and cat-4. FORBIDDEN: cat-2. FORBIDDEN: cat-3.

Every "Why It Applies Here" cell MUST open: `[element name] (cat-N) —`. FORBIDDEN: plain prose without the typed citation opener. Every Mitigation cell MUST contain a remediation action. FORBIDDEN: format guidance in Mitigation cells.

---

---

## V-05 — Lifecycle Emphasis + Inertia Framing: Inertia Verdict as Hard Gate for Role Targets

**Variation axis**: Lifecycle emphasis + inertia framing (combined)
**Hypothesis**: Compressing phase descriptions to their essential constraints while using the inertia verdict as a hard binary gate condition on role count targets produces a shorter, more focused prompt. The combination forces the verdict to do structural work (it controls what comes next) rather than serving as a downstream annotation, strengthening C-11, C-12, C-14, and C-20 simultaneously.

---

You are generating a complete org structure. Phases execute in order. Each phase gate emits a named record block. The next phase MUST NOT begin before the preceding record block is emitted.

**Inputs**: `--from-scan <file>` | `--from-repo <path>` | `--depth standard|deep`

---

### Phase 1 — Scan

Count module and area boundaries. Classify topology.

FORBIDDEN: beginning Phase 2 before emitting:

```
=== P1 ===
T1-REPO-COUNT: <int>
T1-STRUCTURE-TYPE: <FLAT|LAYERED|MIXED>
=== /P1 ===
```

---

### Phase 2 — Inertia Verdict Gate

**Input contract**: MUST read T1-REPO-COUNT and T1-STRUCTURE-TYPE from `P1`.
FORBIDDEN: executing Phase 2 before `P1` is emitted.

**Pressure rating**:
- LOW: ≤5 areas, FLAT
- MODERATE: ≤10 areas or predominantly FLAT
- ELEVATED: >10 areas, LAYERED
- CRITICAL: >20 areas or high-coupling MIXED

**Verdict** (exactly one — both is error, neither is error):
- CAN-OPERATE-FLAT → T2-PRESSURE: LOW or MODERATE
- STRUCTURE-WARRANTED → T2-PRESSURE: ELEVATED or CRITICAL

The verdict is the gate condition for Phase 3 role targets. No downstream phase reads the verdict from prose — MUST read from the record block below.

FORBIDDEN: beginning Phase 3 before emitting:

```
=== P2 ===
T2-PRESSURE: <LOW|MODERATE|ELEVATED|CRITICAL>
T2-VERDICT: <CAN-OPERATE-FLAT|STRUCTURE-WARRANTED>
=== /P2 ===
```

---

### Phase 3 — Role Target Resolution

**Input contract**: MUST read T2-VERDICT and T2-PRESSURE from `P2`.
FORBIDDEN: executing Phase 3 before `P2` is emitted.

**Role count contract** (verdict-gated):

| T2-VERDICT | standard | deep |
|---|---|---|
| CAN-OPERATE-FLAT | 20–24 roles | 50–55 roles |
| STRUCTURE-WARRANTED | 25–30 roles | 55–65 roles |

**Inertia-advocate scope** (verbatim — verdict drives pressure which drives text selection):

| T2-PRESSURE | Scope text (verbatim — no paraphrase, no deviation) |
|---|---|
| LOW | "Represents teams resisting structural change at low pressure. Reviews all proposals for scope creep or hierarchy inflation. Advocates for minimal overhead and autonomous team operation." |
| MODERATE | "Represents current-state teams operating under moderate structural pressure. Challenges each proposed role addition against headcount-to-coordination-overhead ratio. Advocates for flat resolution paths before any escalation tier is added." |
| ELEVATED | "Represents established teams facing elevated pressure to restructure. Reviews every coordination mechanism for flat-org equivalence. Blocks structural changes that can be handled by clarifying existing scope or adding a standing sync." |
| CRITICAL | "Represents an org under critical flat-case pressure where structural change has become operationally necessary. Focuses advocacy on preserving maximum flatness within the warranted structure. Ensures no layer is added without a documented decision-volume justification." |

**Anti-pattern category contract** (verdict-gated, exclusive):

| T2-VERDICT | MUST use | FORBIDDEN |
|---|---|---|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

FORBIDDEN: beginning Phase 4 before emitting:

```
=== P3 ===
T3-ROLE-TARGET: <int — from verdict-gated table>
T3-IA-PRESSURE: <LOW|MODERATE|ELEVATED|CRITICAL — for scope text lookup>
T3-REQUIRED-CATS: <cat-N, cat-N>
T3-FORBIDDEN-CATS: <cat-N, cat-N>
=== /P3 ===
```

---

### Phase 4 — Role File Generation

**Input contract**: MUST read T3-ROLE-TARGET, T3-IA-PRESSURE, T3-REQUIRED-CATS, T3-FORBIDDEN-CATS from `P3`.
FORBIDDEN: executing Phase 4 before `P3` is emitted.

Generate roles across: Engineering, Product, Design, Data, Operations, and cross-functional coordination. MUST group under area subdirectories. Minimum 2 area subdirs. MUST include `inertia-advocate` at `.craft/roles/inertia/inertia-advocate.md`.

Every role file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Missing any field fails.

`inertia-advocate` scope MUST equal the verbatim text from the T3-IA-PRESSURE row in Phase 3 table. Copy exactly.

FORBIDDEN: beginning Phase 5 before emitting:

```
=== P4 ===
T4-ROLE-COUNT: <int>
T4-AREA-LIST: <comma-separated subdirectory names>
=== /P4 ===
```

---

### Phase 5 — org-chart.md Assembly

**Input contract**: MUST read T2-PRESSURE, T2-VERDICT, T3-REQUIRED-CATS, T3-FORBIDDEN-CATS, T4-ROLE-COUNT, T4-AREA-LIST from their record blocks.
FORBIDDEN: executing Phase 5 before `P4` is emitted.

**ASCII Hierarchy** — box-and-line diagram, minimum 2 org levels. Flat list fails.

Skeleton (slots are T4-AREA-LIST entries — fill all):

```
┌───────────────────────────────┐
│  [PROGRAM-LEAD]               │
└──────────────┬────────────────┘
               │
   ┌───────────┼───────────┐
   ▼           ▼           ▼
 {{T4-AREA-LIST[0]}}  {{T4-AREA-LIST[1]}}  {{T4-AREA-LIST[n]}}
```

**Headcount by Area** — columns: `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates`. Missing Decides or Escalates fails.

**Inertia Assessment Block**:

```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both. Both is error. Neither is error.

**Operating Rhythm** — 3+ rows (ROB, shiproom, governance). Each governance meeting: charter with Name, Purpose, Participants, Quorum (`N of M`), Owner.

**Org Evolution Roadmap** — Row 1: headcount threshold. Row 2: different trigger category (coupling, decision latency, dependency depth, or similar). Two headcount rows fails.

**Anti-Pattern Watch** — 2+ rows. Categories MUST match T3-REQUIRED-CATS. FORBIDDEN: any row using T3-FORBIDDEN-CATS. Every "Why It Applies Here" cell MUST open `[element name] (cat-N) —`. Every Mitigation cell MUST contain a remediation action, not format guidance.

---

### Constraint Inventory

| ID | Constraint | Scope |
|---|---|---|
| OB-01 | FORBIDDEN: beginning Phase N before Phase N-1 record block emitted | All boundaries |
| OB-02 | FORBIDDEN: writing both verdicts | P2, Phase 5 block |
| OB-03 | FORBIDDEN: omitting both verdicts | P2, Phase 5 block |
| OB-04 | FORBIDDEN: paraphrasing inertia-advocate scope | Phase 4 role file |
| OB-05 | FORBIDDEN: using T3-FORBIDDEN-CATS in anti-pattern table | Phase 5 |
| OB-06 | FORBIDDEN: format guidance in Mitigation cells | Phase 5 |
| OB-07 | FORBIDDEN: advisory language in any constraint context | All phases |
| OB-08 | FORBIDDEN: two headcount rows in evolution roadmap | Phase 5 |
| OB-09 | FORBIDDEN: role count below lower bound of depth range | Phase 4 |
| OB-10 | FORBIDDEN: omitting any of the five role fields | Phase 4 |

---
