## org-build — Quest Variate R7 (V-01 through V-05)

**Rubric version**: v6 (16 aspirational criteria, denominator 16)
**New constraints targeted**: C-23 (phase-ordering FORBIDDEN at every boundary), C-24 (materialized record-block checkpoints)

---

## V-01 — Single-axis: Role Sequence (Inertia-First Ordering)

**Variation axis**: Role sequence — inertia assessment runs before any structure or role design
**Hypothesis**: Forcing T1 to complete before T2 makes C-11 and C-17 violations structurally impossible: the FLAT-CASE-PRESSURE rating exists before any role file is written, so the IA scope template can only be applied after the rating is known.

---

You are executing the `org-build` skill. Generate a complete org design for the target repository. Produce two artifact sets: `org-chart.md` and `.roles/` role files. The inertia-advocate role MUST appear in every execution regardless of depth, verdict, or input source.

### Input Resolution

If `--from <scan-file>` is provided, read the scan file first. Otherwise scan the repository directly: read `CLAUDE.md`, `plugin-plan.md`, and directory structure to identify domain areas, expertise clusters, and scale signals.

Depth flag: `--depth deep` requires 50+ role files. Standard (default) requires 20–30 role files.

---

### Phase T1 — Inertia Assessment

**FORBIDDEN: reading any T2 input or beginning Phase T2 before the T1 Record Block is emitted.**

Run the inertia assessment before designing any structure. Determine whether this repository's coordination signals exceed what a flat org can handle without structural harm.

**Evidence signals to examine:**

| Signal | Flat-pressure contribution |
|--------|---------------------------|
| Distinct domain areas > 5 | MODERATE–ELEVATED |
| Tight cross-area coupling with no clear owner | ELEVATED–CRITICAL |
| Stated headcount > 15 in docs | MODERATE |
| Evidence of decision escalation failures | CRITICAL |
| Single-owner bottleneck for >3 areas | ELEVATED |

**Compute FLAT-CASE-PRESSURE** — closed set, pick exactly one:

- `NONE` — no coordination signals present
- `MODERATE` — 1–2 minor signals; flat org absorbs them
- `ELEVATED` — 3+ signals; flat org produces friction
- `CRITICAL` — clear evidence of coordination failure or impending structural collapse

**Derive verdict** — closed set, pick exactly one:

- `NONE` or `MODERATE` → `CAN-OPERATE-FLAT`
- `ELEVATED` or `CRITICAL` → `STRUCTURE-WARRANTED`

**Verdict guard:**
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Only one verdict. Both is an error. Neither is an error.

#### T1 Record Block — emit this block in full before proceeding

```
── T1 GATE ──────────────────────────────────────
T1-PRESSURE : [NONE | MODERATE | ELEVATED | CRITICAL]
T1-VERDICT  : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-EVIDENCE : [one sentence — the deciding signal]
─────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T2 before the T1 Record Block above is fully materialized.**

---

### Phase T2 — Org Structure Design

**Input contract**: MUST read `T1-VERDICT` and `T1-PRESSURE` from the T1 Record Block before any structure decision.

**FORBIDDEN: beginning Phase T2 without confirmed `T1-PRESSURE` and `T1-VERDICT` values from the emitted T1 Record Block.**

Design the org structure. Group roles into named areas. Each area becomes a subdirectory under `.roles/`. MUST produce minimum 2 area subdirectories.

**Operating rhythm** — MUST include 3+ distinct rows:

| Meeting | Cadence | Owner | Purpose |
|---------|---------|-------|---------|
| ROB | weekly or bi-weekly | [role] | leadership sync |
| Shiproom | weekly | [role] | delivery review |
| Governance forum | monthly or quarterly | [role] | strategic decisions |

For each governance meeting, produce a committee charter with all five fields: `Name`, `Purpose`, `Quorum` (as N of M fraction), `Cadence`, `Escalates-to`.

**FORBIDDEN: beginning Phase T3 before the T2 Record Block is fully materialized.**

#### T2 Record Block — emit this block in full before proceeding

```
── T2 GATE ──────────────────────────────────────
T2-AREA-COUNT   : [int]
T2-ROLE-TARGET  : [int — lower bound, e.g. 20 for standard / 50 for deep]
T2-AREAS        : [comma-separated area names]
T2-RHYTHM-ROWS  : [int — number of distinct rhythm entries ≥ 3]
─────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T3 before the T2 Record Block above is fully materialized.**

---

### Phase T3 — Role Generation

**Input contract**: MUST read `T2-AREAS` and `T2-ROLE-TARGET` from the T2 Record Block. MUST read `T1-PRESSURE` from the T1 Record Block to select the IA scope template.

**FORBIDDEN: beginning Phase T3 without confirmed `T2-AREAS` list and `T1-PRESSURE` from emitted record blocks.**

Generate all role files. Every role file MUST contain all five fields:

- `orientation` — primary stance (builder, guardian, connector, integrator, challenger)
- `lens` — dimension the role examines most closely
- `expertise` — technical or domain skill cluster
- `scope` — boundary of authority and accountability
- `collaborates_with` — named roles or areas this role coordinates with

**Inertia-advocate scope — verbatim template keyed to `T1-PRESSURE`** (paraphrase FAILS; apply verbatim):

| T1-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| `NONE` | `Monitor org health metrics quarterly. No structural intervention warranted at current scale.` |
| `MODERATE` | `Audit each proposed structural change on demand. Document the flat-path alternative before any review proceeds.` |
| `ELEVATED` | `Own the flat-path register. Block structural proposals that lack a documented flat alternative and estimated coordination cost.` |
| `CRITICAL` | `Serve as standing objector in all org design reviews. Every structural change MUST receive written IA rebuttal before proceeding to the escalation gate. IA sign-off is a required artifact.` |

**FORBIDDEN: beginning Phase T4 before the T3 Record Block is fully materialized.**

#### T3 Record Block — emit this block in full before proceeding

```
── T3 GATE ──────────────────────────────────────
T3-ROLE-COUNT : [int]
T3-DEPTH      : [standard | deep]
T3-IA-SCOPE   : [exact verbatim template text from table above]
─────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T4 before the T3 Record Block above is fully materialized.**

---

### Phase T4 — Anti-Pattern Derivation

**Input contract**: MUST read `T1-VERDICT` from the T1 Record Block and `T3-ROLE-COUNT` from the T3 Record Block before computing anti-pattern categories.

**FORBIDDEN: beginning Phase T4 without confirmed `T1-VERDICT` from the emitted T1 Record Block.**

Derive anti-pattern categories from `T1-VERDICT`:

- `CAN-OPERATE-FLAT` → MUST include `cat-2` (premature structure), `cat-3` (flat-org failure modes). FORBIDDEN: `cat-1` (over-coordination), `cat-4` (over-centralization).
- `STRUCTURE-WARRANTED` → MUST include `cat-1` (over-coordination), `cat-4` (over-centralization). FORBIDDEN: `cat-2` (premature structure), `cat-3` (flat-org failure modes).

Anti-pattern category derivation is explicitly tied to the structural design choice. Category choices independent of structure FAIL.

**Anti-Pattern Watch table format** — every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax. Every Mitigation cell MUST contain a specific remediation action — not format guidance or column-structure instructions.

**FORBIDDEN: beginning artifact generation before the T4 Record Block is fully materialized.**

#### T4 Record Block — emit this block in full before proceeding

```
── T4 GATE ──────────────────────────────────────
T4-VERDICT-PATH   : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-REQUIRED-CATS  : [e.g. cat-2, cat-3]
T4-FORBIDDEN-CATS : [e.g. cat-1, cat-4]
T4-AP-COUNT       : [int]
─────────────────────────────────────────────────
```

**FORBIDDEN: beginning artifact generation before the T4 Record Block above is fully materialized.**

---

### Artifact Generation

#### org-chart.md

MUST contain:

1. **ASCII hierarchy** — min 2 org levels, box/line diagram, not a flat name list.
2. **Headcount by area table** — columns: `Area | Headcount | Key Roles | Decides | Escalates`. Missing `Decides` or `Escalates` columns FAILS.
3. **Inertia verdict block**:
   ```
   FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
   VERDICT: {{T1-VERDICT}}
   Only one verdict. Both is an error. Neither is an error.
   ```
4. **Org Evolution Roadmap** — 2+ rows. Row 1: headcount threshold trigger. Row 2: different trigger category (velocity, coupling, or governance signal). Two headcount thresholds FAILS.
5. **Anti-Pattern Watch table** — cat-N typed citations per C-10 format.
6. **Operating rhythm and committee charters** — as designed in T2.

#### .roles/ files

One file per role at `.roles/{area}/{role}.md`. Every file MUST contain all five fields. The inertia-advocate `scope` field MUST contain the verbatim T3-IA-SCOPE text from the T3 Record Block.

Depth enforcement: standard → 20–30 files. `--depth deep` → 50+ files. FORBIDDEN: falling below the lower bound.

---

## V-02 — Single-axis: Output Format (Table-Dominant)

**Variation axis**: Output format — every phase output, record block, and gate variable is expressed as a structured table row; prose is limited to rationale only
**Hypothesis**: Tabular record blocks (C-24) are less likely to be omitted or partially filled when they are formatted as tables the model must complete, reducing the dangling-output gap the R6 scorecard caught at the schema-comparison step.

---

You are executing the `org-build` skill. Generate `org-chart.md` and `.roles/` files for the target repository. The inertia-advocate role MUST appear in every execution.

### Input

Resolve input: scan file (`--from`) or direct repo scan. Depth: `--depth deep` → 50+ roles; standard → 20–30 roles.

---

### Phase T1 — Inertia Assessment

**FORBIDDEN: beginning Phase T2 before the T1 Gate Table is fully filled.**

Examine coordination signals. Fill the T1 Signal Table, then derive FLAT-CASE-PRESSURE and verdict.

**T1 Signal Table**

| Signal | Present? | Pressure Contribution |
|--------|----------|-----------------------|
| Distinct domain areas > 5 | [Y/N] | [NONE / MODERATE / ELEVATED] |
| Cross-area coupling without clear owner | [Y/N] | [NONE / MODERATE / ELEVATED] |
| Stated headcount > 15 | [Y/N] | [NONE / MODERATE] |
| Decision escalation failures documented | [Y/N] | [ELEVATED / CRITICAL] |
| Single-owner bottleneck for 3+ areas | [Y/N] | [ELEVATED] |

Aggregate to FLAT-CASE-PRESSURE (closed set: `NONE` / `MODERATE` / `ELEVATED` / `CRITICAL`).

Verdict rule: `NONE` or `MODERATE` → `CAN-OPERATE-FLAT`. `ELEVATED` or `CRITICAL` → `STRUCTURE-WARRANTED`.

Verdict guard: FORBIDDEN: writing both. FORBIDDEN: omitting both. Only one verdict. Both is an error. Neither is an error.

**T1 Gate Table — fill completely before any T2 work begins**

| Variable | Type | Value |
|----------|------|-------|
| T1-PRESSURE | enum{NONE,MODERATE,ELEVATED,CRITICAL} | |
| T1-VERDICT | enum{CAN-OPERATE-FLAT,STRUCTURE-WARRANTED} | |
| T1-EVIDENCE | string | |

**FORBIDDEN: beginning Phase T2 before every cell in the T1 Gate Table is filled.**

---

### Phase T2 — Structure Design

**Input contract**: MUST read `T1-PRESSURE` and `T1-VERDICT` from the T1 Gate Table. FORBIDDEN: proceeding with empty or unresolved T1 values.

Design areas and rhythm. Fill the T2 Gate Table.

**Area Design Table** (one row per area)

| Area Name | Subdirectory | Estimated Role Count | Key Decisions Owned |
|-----------|-------------|----------------------|---------------------|
| | | | |

MUST produce minimum 2 area rows.

**Operating Rhythm Table** (MUST have 3+ distinct rows)

| Meeting | Cadence | Owner Role | Purpose | Charter? |
|---------|---------|-----------|---------|---------|
| ROB | | | | — |
| Shiproom | | | | — |
| Governance Forum | | | | Yes |

For each row where Charter = Yes, produce a charter block with: `Name`, `Purpose`, `Quorum` (N of M), `Cadence`, `Escalates-to`.

**T2 Gate Table — fill completely before any T3 work begins**

| Variable | Type | Value |
|----------|------|-------|
| T2-AREA-COUNT | int | |
| T2-ROLE-TARGET | int | |
| T2-AREAS | string-list | |
| T2-RHYTHM-ROWS | int | |

**FORBIDDEN: beginning Phase T3 before every cell in the T2 Gate Table is filled.**

---

### Phase T3 — Role Generation

**Input contract**: MUST read `T2-AREAS` and `T2-ROLE-TARGET` from the T2 Gate Table. MUST read `T1-PRESSURE` from the T1 Gate Table for the IA scope template.

**FORBIDDEN: beginning Phase T3 with any unresolved T2 Gate Table cell.**

**Role File Schema** — every role file MUST contain all five fields:

| Field | Required | Notes |
|-------|----------|-------|
| `orientation` | MUST | builder / guardian / connector / integrator / challenger |
| `lens` | MUST | the dimension examined most closely |
| `expertise` | MUST | technical or domain skill cluster |
| `scope` | MUST | authority and accountability boundary |
| `collaborates_with` | MUST | named roles or areas |

**Inertia-Advocate Scope Templates** — apply the row matching `T1-PRESSURE` verbatim. Paraphrase FAILS.

| T1-PRESSURE | Verbatim scope field value |
|-------------|---------------------------|
| NONE | `Monitor org health metrics quarterly. No structural intervention warranted at current scale.` |
| MODERATE | `Audit each proposed structural change on demand. Document the flat-path alternative before any review proceeds.` |
| ELEVATED | `Own the flat-path register. Block structural proposals that lack a documented flat alternative and estimated coordination cost.` |
| CRITICAL | `Serve as standing objector in all org design reviews. Every structural change MUST receive written IA rebuttal before proceeding to the escalation gate. IA sign-off is a required artifact.` |

**T3 Gate Table — fill completely before any T4 work begins**

| Variable | Type | Value |
|----------|------|-------|
| T3-ROLE-COUNT | int | |
| T3-DEPTH | enum{standard,deep} | |
| T3-IA-SCOPE | string (verbatim template) | |

**FORBIDDEN: beginning Phase T4 before every cell in the T3 Gate Table is filled.**

---

### Phase T4 — Anti-Pattern Derivation

**Input contract**: MUST read `T1-VERDICT` from the T1 Gate Table. FORBIDDEN: computing categories before T1-VERDICT is confirmed.

**Category Derivation Table** — select row matching `T1-VERDICT`

| T1-VERDICT | MUST include | FORBIDDEN |
|-----------|-------------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

Category selection MUST be explicitly tied to the design decision. Category choices independent of structure FAIL.

**Anti-Pattern Watch Table** — every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST contain a specific remediation action.

**T4 Gate Table — fill completely before artifact generation begins**

| Variable | Type | Value |
|----------|------|-------|
| T4-VERDICT-PATH | enum{CAN-OPERATE-FLAT,STRUCTURE-WARRANTED} | |
| T4-REQUIRED-CATS | string-list | |
| T4-FORBIDDEN-CATS | string-list | |
| T4-AP-COUNT | int | |

**FORBIDDEN: beginning artifact generation before every cell in the T4 Gate Table is filled.**

---

### Artifact Generation

**Pre-print skeleton for `org-chart.md`** — fill all slots using gate table values:

```markdown
# Org Chart — {{REPO-NAME}}

## ASCII Hierarchy
[min 2 levels, box/line diagram]

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
[one row per {{T2-AREAS}} entry]

## Inertia Assessment
FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
Only one verdict. Both is an error. Neither is an error.

## Org Evolution Roadmap
| Trigger | Category | Recommended Action |
|---------|----------|--------------------|
| Headcount > [N] | headcount-threshold | [action] |
| [non-headcount trigger] | [different category] | [action] |

## Anti-Pattern Watch
| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|
| {{T4-REQUIRED-CATS entry}} (cat-N) | [element name] (cat-N) — [reason] | [remediation action] |

## Operating Rhythm
[T2 rhythm table + charters]
```

Every `{{slot}}` MUST correspond to a named typed variable in a gate table. Slots MUST be filled from gate tables — not from re-derived values.

Role files: `.roles/{area}/{role}.md`, one per role, all five fields present. Inertia-advocate `scope` MUST equal `T3-IA-SCOPE` verbatim.

---

## V-03 — Single-axis: Lifecycle Emphasis (Maximum Explicit Boundaries)

**Variation axis**: Lifecycle emphasis — each phase boundary is a first-class section with its own header, ordering FORBIDDEN, checkpoint template, and advancement guard
**Hypothesis**: Treating phase transitions as named structural sections (not inline rules) maximizes C-23 compliance because the FORBIDDEN ordering constraint is impossible to overlook when it anchors its own heading.

---

You are executing the `org-build` skill. Produce `org-chart.md` and `.roles/` files. The inertia-advocate role MUST appear in every execution.

**Depth**: standard = 20–30 role files. `--depth deep` = 50+ role files.

**Global ordering rule**: Every phase MUST complete all output variables before the next phase begins. This rule is restated at each boundary — it is not sufficient to read it once here.

---

### ► PHASE T1 — Inertia Assessment

Scan the repository. Identify coordination signals. Assign FLAT-CASE-PRESSURE from the closed set: `NONE` / `MODERATE` / `ELEVATED` / `CRITICAL`. Derive verdict: `NONE`/`MODERATE` → `CAN-OPERATE-FLAT`; `ELEVATED`/`CRITICAL` → `STRUCTURE-WARRANTED`.

Verdict guard: FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Only one verdict. Both is an error. Neither is an error.

---

### ⛔ BOUNDARY: T1 → T2

**FORBIDDEN: beginning Phase T2 before emitting the T1 Checkpoint in full.**

**T1 Checkpoint** — materialize here before reading any T2 section:

```
╔══════════════════════════════╗
║ T1 CHECKPOINT                ║
╠══════════════════════════════╣
║ T1-PRESSURE : ______________ ║
║ T1-VERDICT  : ______________ ║
║ T1-EVIDENCE : ______________ ║
╚══════════════════════════════╝
```

All three fields MUST be filled. A checkpoint with any blank field does not satisfy this boundary. **FORBIDDEN: reading the Phase T2 section before this checkpoint is fully written.**

---

### ► PHASE T2 — Org Structure Design

**Input contract**: T1-PRESSURE (from T1 Checkpoint), T1-VERDICT (from T1 Checkpoint). MUST confirm both values before any structure decision.

Design areas (minimum 2). Design operating rhythm (minimum 3 distinct rows: ROB, Shiproom, Governance). Produce committee charters for governance meetings — each charter MUST include: `Name`, `Purpose`, `Quorum` (N of M fraction), `Cadence`, `Escalates-to`.

---

### ⛔ BOUNDARY: T2 → T3

**FORBIDDEN: beginning Phase T3 before emitting the T2 Checkpoint in full.**

**T2 Checkpoint** — materialize here before reading any T3 section:

```
╔══════════════════════════════════════════════════╗
║ T2 CHECKPOINT                                    ║
╠══════════════════════════════════════════════════╣
║ T2-AREA-COUNT   : _______________________________ ║
║ T2-ROLE-TARGET  : _______________________________ ║
║ T2-AREAS        : _______________________________ ║
║ T2-RHYTHM-ROWS  : _______________________________ ║
╚══════════════════════════════════════════════════╝
```

All four fields MUST be filled. **FORBIDDEN: reading the Phase T3 section before this checkpoint is fully written.**

---

### ► PHASE T3 — Role Generation

**Input contract**: T2-AREAS (from T2 Checkpoint), T2-ROLE-TARGET (from T2 Checkpoint), T1-PRESSURE (from T1 Checkpoint). MUST confirm all three before generating any role file.

Every role file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Missing any field FAILS.

**Inertia-advocate scope — apply verbatim from T1-PRESSURE, no paraphrase:**

| T1-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor org health metrics quarterly. No structural intervention warranted at current scale.` |
| MODERATE | `Audit each proposed structural change on demand. Document the flat-path alternative before any review proceeds.` |
| ELEVATED | `Own the flat-path register. Block structural proposals that lack a documented flat alternative and estimated coordination cost.` |
| CRITICAL | `Serve as standing objector in all org design reviews. Every structural change MUST receive written IA rebuttal before proceeding to the escalation gate. IA sign-off is a required artifact.` |

FORBIDDEN: paraphrase. FORBIDDEN: omission of the inertia-advocate role.

---

### ⛔ BOUNDARY: T3 → T4

**FORBIDDEN: beginning Phase T4 before emitting the T3 Checkpoint in full.**

**T3 Checkpoint** — materialize here before reading any T4 section:

```
╔══════════════════════════════════════════════════════════════════════════╗
║ T3 CHECKPOINT                                                            ║
╠══════════════════════════════════════════════════════════════════════════╣
║ T3-ROLE-COUNT : _________________________________________________________║
║ T3-DEPTH      : _________________________________________________________║
║ T3-IA-SCOPE   : _________________________________________________________║
║                 (copy verbatim text — not a paraphrase)                 ║
╚══════════════════════════════════════════════════════════════════════════╝
```

All three fields MUST be filled. The `T3-IA-SCOPE` value MUST match the verbatim template row exactly. **FORBIDDEN: reading the Phase T4 section before this checkpoint is fully written.**

---

### ► PHASE T4 — Anti-Pattern Derivation

**Input contract**: T1-VERDICT (from T1 Checkpoint). MUST confirm T1-VERDICT before computing categories.

Derive categories from T1-VERDICT:

- `CAN-OPERATE-FLAT`: MUST use cat-2, cat-3. FORBIDDEN: cat-1, cat-4.
- `STRUCTURE-WARRANTED`: MUST use cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

Category selection MUST be explicitly tied to the structural design choice. Categories selected independent of structure FAIL.

Anti-Pattern Watch table: every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST contain a specific remediation action, not format guidance.

---

### ⛔ BOUNDARY: T4 → ARTIFACTS

**FORBIDDEN: beginning artifact generation before emitting the T4 Checkpoint in full.**

**T4 Checkpoint** — materialize here before generating any artifact:

```
╔══════════════════════════════════════════════════════╗
║ T4 CHECKPOINT                                        ║
╠══════════════════════════════════════════════════════╣
║ T4-VERDICT-PATH   : _________________________________ ║
║ T4-REQUIRED-CATS  : _________________________________ ║
║ T4-FORBIDDEN-CATS : _________________________________ ║
║ T4-AP-COUNT       : _________________________________ ║
╚══════════════════════════════════════════════════════╝
```

**FORBIDDEN: generating any artifact before this checkpoint is fully written.**

---

### ► ARTIFACT GENERATION

Generate `org-chart.md`:

1. ASCII box/line diagram — minimum 2 org levels. Flat name list FAILS.
2. Headcount by area table: `Area | Headcount | Key Roles | Decides | Escalates`. Missing `Decides` or `Escalates` columns FAILS.
3. Inertia verdict block:
   ```
   FLAT-CASE-PRESSURE: [T1-PRESSURE from checkpoint]
   VERDICT: [T1-VERDICT from checkpoint]
   Only one verdict. Both is an error. Neither is an error.
   ```
4. Org Evolution Roadmap: 2+ rows, at least one headcount threshold and one different trigger category.
5. Anti-Pattern Watch table using T4-REQUIRED-CATS entries with cat-N typed citations.
6. Operating rhythm table and committee charters from T2.

Generate `.roles/{area}/{role}.md` — one file per role, all five fields, `inertia-advocate/scope` = verbatim T3-IA-SCOPE from checkpoint.

---

## V-04 — Combination: Formal Register + Inertia Prominence

**Variation axes**: Phrasing register (purely imperative — MUST/FORBIDDEN only) + Inertia framing (IA is the primary design constraint, introduced first)
**Hypothesis**: Leading with the inertia framing and then using exclusively imperative language throughout maximizes C-08 and C-19 compliance simultaneously because the model cannot drift into advisory register when the IA is positioned as the anchor of the entire design, not an appendix.

---

You are executing the `org-build` skill. The inertia-advocate is the primary structural lens of this design. Every org decision MUST be evaluated through the question: does this structure add coordination load the flat case could have avoided? The inertia-advocate role MUST appear in every execution, regardless of depth, input, or any other parameter.

---

### INERTIA-ADVOCATE: PRIMARY DESIGN CONSTRAINT

The inertia-advocate is not an optional appendix. The IA exists to:

1. Quantify the structural cost the flat case avoids
2. Rate FLAT-CASE-PRESSURE before any structure is proposed
3. Apply the STRUCTURE-WARRANTED or CAN-OPERATE-FLAT verdict to all downstream decisions
4. Produce a scope derived verbatim from the pressure rating — not from general reasoning

The IA role file MUST be generated first in Phase T3. Its `scope` field MUST be the verbatim text from the rating-keyed table. The IA MUST NOT be generated until T1-PRESSURE is known — it cannot be drafted in advance.

---

### Phase T1 — Inertia Pressure Assessment

**FORBIDDEN: beginning Phase T2 before the T1 Record Block is emitted.**

MUST examine repository signals. MUST compute FLAT-CASE-PRESSURE from the closed set:

- `NONE` — no coordination overhead signals
- `MODERATE` — minor signals, flat org sufficient
- `ELEVATED` — clear friction signals, flat org produces drag
- `CRITICAL` — structural failure signals present

MUST derive verdict from pressure:

| T1-PRESSURE | T1-VERDICT |
|-------------|-----------|
| NONE | CAN-OPERATE-FLAT |
| MODERATE | CAN-OPERATE-FLAT |
| ELEVATED | STRUCTURE-WARRANTED |
| CRITICAL | STRUCTURE-WARRANTED |

FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither verdict. Only one verdict. Both is an error. Neither is an error.

#### T1 Record Block

MUST emit this block completely before any T2 work:

```
── T1 RECORD ─────────────────────────────────────
T1-PRESSURE : [NONE | MODERATE | ELEVATED | CRITICAL]
T1-VERDICT  : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-EVIDENCE : [deciding signal in one sentence]
──────────────────────────────────────────────────
```

**FORBIDDEN: proceeding to Phase T2 before T1 Record Block is emitted with all three fields present.**

---

### Phase T2 — Structural Design

**Input contract**: MUST read T1-PRESSURE and T1-VERDICT from the T1 Record Block. FORBIDDEN: making any structural decision before confirming both T1 values.

MUST design area groupings (minimum 2 areas). MUST produce operating rhythm with minimum 3 distinct rows: ROB, Shiproom, Governance Forum. MUST produce committee charters for all governance-class meetings. Each charter MUST contain: Name, Purpose, Quorum (N of M fraction), Cadence, Escalates-to.

MUST size role target: standard → 20–30 roles. `--depth deep` → 50+ roles. FORBIDDEN: generating fewer than the lower bound.

#### T2 Record Block

MUST emit this block completely before any T3 work:

```
── T2 RECORD ─────────────────────────────────────
T2-AREA-COUNT  : [int]
T2-ROLE-TARGET : [int — lower bound of range]
T2-AREAS       : [comma-separated list]
T2-RHYTHM-ROWS : [int ≥ 3]
──────────────────────────────────────────────────
```

**FORBIDDEN: proceeding to Phase T3 before T2 Record Block is emitted with all four fields present.**

---

### Phase T3 — Role Generation

**Input contract**: MUST read T2-AREAS and T2-ROLE-TARGET from T2 Record Block. MUST read T1-PRESSURE from T1 Record Block. FORBIDDEN: generating any role file before all three values are confirmed.

MUST generate the inertia-advocate role file first. The `scope` field MUST use the verbatim template matching T1-PRESSURE — not derived reasoning, not paraphrase:

| T1-PRESSURE | scope (copy verbatim — deviations FAIL) |
|-------------|----------------------------------------|
| NONE | `Monitor org health metrics quarterly. No structural intervention warranted at current scale.` |
| MODERATE | `Audit each proposed structural change on demand. Document the flat-path alternative before any review proceeds.` |
| ELEVATED | `Own the flat-path register. Block structural proposals that lack a documented flat alternative and estimated coordination cost.` |
| CRITICAL | `Serve as standing objector in all org design reviews. Every structural change MUST receive written IA rebuttal before proceeding to the escalation gate. IA sign-off is a required artifact.` |

MUST apply the IA scope template verbatim. FORBIDDEN: paraphrase, adaptation, or any deviation.

MUST generate all remaining roles after the IA. Every role file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. FORBIDDEN: omitting any field from any role file.

MUST group role files by area under `.roles/{area}/`. FORBIDDEN: placing all roles flat with no area grouping.

#### T3 Record Block

MUST emit this block completely before any T4 work:

```
── T3 RECORD ─────────────────────────────────────
T3-ROLE-COUNT : [int]
T3-DEPTH      : [standard | deep]
T3-IA-SCOPE   : [verbatim scope text — must match table row exactly]
──────────────────────────────────────────────────
```

**FORBIDDEN: proceeding to Phase T4 before T3 Record Block is emitted with all three fields present.**

---

### Phase T4 — Anti-Pattern Derivation

**Input contract**: MUST read T1-VERDICT from T1 Record Block. FORBIDDEN: computing anti-pattern categories without confirmed T1-VERDICT.

Anti-pattern categories MUST be derived from T1-VERDICT. Category selection independent of structural design choice FAILS.

| T1-VERDICT | Categories MUST include | Categories FORBIDDEN |
|-----------|------------------------|---------------------|
| CAN-OPERATE-FLAT | cat-2 (premature structure), cat-3 (flat-org failure modes) | cat-1 (over-coordination), cat-4 (over-centralization) |
| STRUCTURE-WARRANTED | cat-1 (over-coordination), cat-4 (over-centralization) | cat-2 (premature structure), cat-3 (flat-org failure modes) |

MUST format every "Why It Applies Here" cell as: `[element name] (cat-N) — [reason]`. FORBIDDEN: plain prose without the typed citation prefix.

MUST write every Mitigation cell as a specific remediation action. FORBIDDEN: format guidance or column-structure instructions in Mitigation cells.

#### T4 Record Block

MUST emit this block completely before artifact generation:

```
── T4 RECORD ─────────────────────────────────────
T4-VERDICT-PATH   : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T4-REQUIRED-CATS  : [list]
T4-FORBIDDEN-CATS : [list]
T4-AP-COUNT       : [int]
──────────────────────────────────────────────────
```

**FORBIDDEN: proceeding to artifact generation before T4 Record Block is emitted with all four fields present.**

---

### Artifact Generation

**org-chart.md** — MUST contain:

1. ASCII org hierarchy (minimum 2 levels; flat name list FAILS)
2. Headcount by area table with columns: `Area | Headcount | Key Roles | Decides | Escalates`
3. Inertia assessment block:
   ```
   FLAT-CASE-PRESSURE: [T1-PRESSURE]
   VERDICT: [T1-VERDICT]
   Only one verdict. Both is an error. Neither is an error.
   ```
4. Org Evolution Roadmap: 2+ rows, minimum one headcount threshold trigger and one different trigger category
5. Anti-Pattern Watch table from T4
6. Operating rhythm and committee charters from T2

**`.roles/` files** — MUST produce one file per role with all five fields. MUST use T3-IA-SCOPE verbatim for the inertia-advocate scope field.

---

## V-05 — Combination: Skeleton-First + Role Sequence

**Variation axes**: Output format (pre-print skeleton emitted first, before any phase runs) + Role sequence (inertia-first, as in V-01)
**Hypothesis**: Emitting the org-chart.md skeleton with all `{{PLACEHOLDER}}` slots named before phases begin simultaneously satisfies C-22 (named slots keyed to gate variables) and enforces correct phase ordering because a slot cannot be filled until the gate variable that names it is produced — making phase skipping observable by inspection.

---

You are executing the `org-build` skill. Before running any phase, emit the pre-print skeleton below. Then run phases T1 through T4 in order to fill every placeholder slot. The inertia-advocate role MUST appear in every execution.

**Depth**: standard = 20–30 roles. `--depth deep` = 50+ roles.

---

### Pre-Print Skeleton — Emit Before Any Phase Begins

Emit this skeleton in full as the first output. Do not fill any `{{...}}` slot yet — they are placeholders for gate variable values produced by phases T1–T4.

```markdown
# Org Chart — {{REPO-NAME}}

## Structural Overview

{{ASCII-HIERARCHY}}
[Minimum 2 org levels, box/line diagram. This section is filled during artifact generation.]

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{AREA-ROWS-FROM-T2-AREAS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
Only one verdict. Both is an error. Neither is an error.

## Inertia-Advocate Scope

> {{T3-IA-SCOPE}}

## Org Evolution Roadmap

| Trigger | Category | Recommended Action |
|---------|----------|--------------------|
| Headcount > {{HEADCOUNT-THRESHOLD}} | headcount-threshold | {{HEADCOUNT-ACTION}} |
| {{NON-HEADCOUNT-TRIGGER}} | {{NON-HEADCOUNT-CATEGORY}} | {{NON-HEADCOUNT-ACTION}} |

## Anti-Pattern Watch

Verdict path: {{T4-VERDICT-PATH}}
Required categories: {{T4-REQUIRED-CATS}}
FORBIDDEN categories: {{T4-FORBIDDEN-CATS}}

| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|
{{ANTI-PATTERN-ROWS}}

## Operating Rhythm

{{RHYTHM-TABLE-FROM-T2}}

## Committee Charters

{{CHARTERS-FROM-T2}}
```

Every `{{slot}}` corresponds to a named typed variable produced by a phase gate. FORBIDDEN: filling any slot before the phase that produces its variable has emitted its record block.

---

### Phase T1 — Inertia Assessment

**FORBIDDEN: beginning Phase T2 before the T1 Record Block is emitted and `{{T1-PRESSURE}}` and `{{T1-VERDICT}}` are resolved.**

Examine repository signals. Compute FLAT-CASE-PRESSURE from closed set: `NONE` / `MODERATE` / `ELEVATED` / `CRITICAL`.

Derive verdict: `NONE`/`MODERATE` → `CAN-OPERATE-FLAT`. `ELEVATED`/`CRITICAL` → `STRUCTURE-WARRANTED`.

Verdict guard: FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither verdict. Only one verdict. Both is an error. Neither is an error.

#### T1 Record Block

```
── T1 RECORD ─────────────────────────────────────────────────
T1-PRESSURE : [NONE | MODERATE | ELEVATED | CRITICAL]
  → fills skeleton slot: {{T1-PRESSURE}}
T1-VERDICT  : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
  → fills skeleton slot: {{T1-VERDICT}}
T1-EVIDENCE : [deciding signal, one sentence]
──────────────────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T2 before emitting this record block in full.**

---

### Phase T2 — Org Structure Design

**Input contract**: MUST read T1-PRESSURE and T1-VERDICT from T1 Record Block before any structure decision. FORBIDDEN: proceeding with unresolved T1 values.

Design area groupings (minimum 2). Design operating rhythm (minimum 3 distinct rows). Produce committee charters for governance meetings — each charter MUST include Name, Purpose, Quorum (N of M), Cadence, Escalates-to.

#### T2 Record Block

```
── T2 RECORD ─────────────────────────────────────────────────
T2-AREA-COUNT  : [int]
  → fills skeleton slot: [row count of {{AREA-ROWS-FROM-T2-AREAS}}]
T2-ROLE-TARGET : [int — lower bound]
T2-AREAS       : [comma-separated area names]
  → fills skeleton slot: {{AREA-ROWS-FROM-T2-AREAS}}
T2-RHYTHM-ROWS : [int ≥ 3]
  → fills skeleton slots: {{RHYTHM-TABLE-FROM-T2}}, {{CHARTERS-FROM-T2}}
──────────────────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T3 before emitting this record block in full.**

---

### Phase T3 — Role Generation

**Input contract**: MUST read T2-AREAS and T2-ROLE-TARGET from T2 Record Block. MUST read T1-PRESSURE from T1 Record Block to select IA scope template. FORBIDDEN: generating any role file before all three values are confirmed.

Generate the inertia-advocate role file first. Its `scope` field fills `{{T3-IA-SCOPE}}` in the skeleton.

**Inertia-Advocate Scope Templates — apply verbatim, keyed to T1-PRESSURE:**

| T1-PRESSURE | Verbatim scope text → fills {{T3-IA-SCOPE}} |
|-------------|---------------------------------------------|
| NONE | `Monitor org health metrics quarterly. No structural intervention warranted at current scale.` |
| MODERATE | `Audit each proposed structural change on demand. Document the flat-path alternative before any review proceeds.` |
| ELEVATED | `Own the flat-path register. Block structural proposals that lack a documented flat alternative and estimated coordination cost.` |
| CRITICAL | `Serve as standing objector in all org design reviews. Every structural change MUST receive written IA rebuttal before proceeding to the escalation gate. IA sign-off is a required artifact.` |

FORBIDDEN: paraphrase. FORBIDDEN: omitting the inertia-advocate role.

Generate all remaining role files. Every role file MUST contain all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Group by area under `.roles/{area}/`. Minimum 2 area subdirectories.

#### T3 Record Block

```
── T3 RECORD ─────────────────────────────────────────────────
T3-ROLE-COUNT : [int]
  → depth check: standard → 20–30; deep → 50+
T3-DEPTH      : [standard | deep]
T3-IA-SCOPE   : [verbatim scope text from table above]
  → fills skeleton slot: {{T3-IA-SCOPE}}
──────────────────────────────────────────────────────────────
```

**FORBIDDEN: beginning Phase T4 before emitting this record block in full.**

---

### Phase T4 — Anti-Pattern Derivation

**Input contract**: MUST read T1-VERDICT from T1 Record Block. FORBIDDEN: computing categories without confirmed T1-VERDICT.

Derive categories from T1-VERDICT:

| T1-VERDICT | MUST include → fills {{T4-REQUIRED-CATS}} | FORBIDDEN → fills {{T4-FORBIDDEN-CATS}} |
|-----------|------------------------------------------|----------------------------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

Category selection MUST be explicitly tied to the structural design choice. Independent selection FAILS.

Anti-Pattern Watch rows: every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`. Every Mitigation cell MUST contain a specific remediation action, not format guidance.

#### T4 Record Block

```
── T4 RECORD ─────────────────────────────────────────────────
T4-VERDICT-PATH   : [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
  → fills skeleton slot: {{T4-VERDICT-PATH}}
T4-REQUIRED-CATS  : [list]
  → fills skeleton slot: {{T4-REQUIRED-CATS}}
T4-FORBIDDEN-CATS : [list]
  → fills skeleton slot: {{T4-FORBIDDEN-CATS}}
T4-AP-COUNT       : [int]
  → row count of {{ANTI-PATTERN-ROWS}}
──────────────────────────────────────────────────────────────
```

**FORBIDDEN: beginning artifact generation before emitting this record block in full.**

---

### Artifact Generation — Fill the Pre-Print Skeleton

Replace every `{{slot}}` in the pre-print skeleton with the corresponding gate variable value from the record blocks:

| Skeleton Slot | Source Variable | Source Phase |
|--------------|-----------------|--------------|
| `{{T1-PRESSURE}}` | T1-PRESSURE | T1 Record Block |
| `{{T1-VERDICT}}` | T1-VERDICT | T1 Record Block |
| `{{T3-IA-SCOPE}}` | T3-IA-SCOPE | T3 Record Block |
| `{{AREA-ROWS-FROM-T2-AREAS}}` | T2-AREAS | T2 Record Block |
| `{{RHYTHM-TABLE-FROM-T2}}` | T2 rhythm design | T2 phase work |
| `{{CHARTERS-FROM-T2}}` | T2 charter design | T2 phase work |
| `{{T4-VERDICT-PATH}}` | T4-VERDICT-PATH | T4 Record Block |
| `{{T4-REQUIRED-CATS}}` | T4-REQUIRED-CATS | T4 Record Block |
| `{{T4-FORBIDDEN-CATS}}` | T4-FORBIDDEN-CATS | T4 Record Block |
| `{{ANTI-PATTERN-ROWS}}` | Anti-pattern table | T4 phase work |
| `{{ASCII-HIERARCHY}}` | Org design | T2 phase work |

FORBIDDEN: leaving any `{{slot}}` unfilled in the final `org-chart.md`. FORBIDDEN: filling a slot with a value not traceable to its named source variable. A skeleton slot filled with re-derived or assumed values rather than gate-recorded values FAILS.

Generate `.roles/{area}/{role}.md` files: one per role, all five fields, inertia-advocate `scope` = T3-IA-SCOPE verbatim from T3 Record Block.

---

## Variation Summary

| Variation | Axes | Primary Criterion Target | Key Structural Change |
|-----------|------|--------------------------|----------------------|
| V-01 | Role sequence (inertia-first) | C-11, C-17 | T1 runs before T2/T3; IA scope cannot be drafted pre-rating |
| V-02 | Output format (table-dominant) | C-24, C-22 | Gate tables replace prose record blocks; every variable is a table cell |
| V-03 | Lifecycle emphasis (max explicit boundaries) | C-23, C-24 | Each boundary is a named section with heading, FORBIDDEN guard, and boxed checkpoint |
| V-04 | Formal register + Inertia prominence | C-08, C-19 | IA is leading design frame; MUST/FORBIDDEN replaces all advisory language throughout |
| V-05 | Skeleton-first + Role sequence | C-22, C-14, C-23 | Pre-print skeleton with `{{named slots}}` emitted before any phase; slots keyed to gate variables |
