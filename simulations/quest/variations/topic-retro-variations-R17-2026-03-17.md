Now I have what I need. The R16 V-05 scored 126/148 = 85.1% and produced two new criteria (C-40, C-41) in rubric v15. R17 targets both for FULL pass — the partial conditions show exactly what falls short.

**C-40 PARTIAL**: tables exist without naming the manifest as their source
**C-41 PARTIAL**: gate describes what should exist without naming the exact artifact

Variation axes for R17:
- **Single-axis (3)**: C-40 derivation declarations | C-41 named-artifact gate format | phrasing register
- **Combined (2)**: C-40 + C-41 | full integration with bidirectional manifest citation

---

# topic-retro — Variations R17

**Date:** 2026-03-17
**Rubric:** v15 (C-01–C-41; denom = 152 non-AMEND standard)
**R16 top scorer:** V-05 (126/148 = 85.1%, rubric v14) — Manifest-First Derivation + Named-Criteria Phase Gate
**New criteria to target:** C-40 (manifest-first derivation, all downstream as derived views) and C-41 (named-criteria phase gate, aspiration criteria asserted by structural artifact name)
**Base used:** R16-V-05 topology — AUDIT MANIFEST in Phase 1, derived views in Phase 2, Phase 2 exit gate

**C-40 gap analysis:** R16-V-05 had the manifest topology and derivation relationships were structurally evident from the topology. C-40's PARTIAL trap is "a skill that states tables exist without naming the manifest as their source." FULL requires derivation relationships to be *stated* — not merely evident. The fix: each downstream section header must carry an explicit derivation declaration naming the AUDIT MANIFEST as source and stating the operation (filter / group / count).

**C-41 gap analysis:** R16-V-05's Phase 2 exit gate explicitly asserted "Backward Recovery Table A: PRESENT" as a checkpoint condition. C-41's PARTIAL trap is "a gate that describes intent without naming the artifact" or "a gate that references only rubric IDs, not structural artifact names." FULL requires the gate to assert at least one aspiration criterion by its structural artifact name. The distinction: "C-38 satisfied" = PARTIAL; "BACKWARD RECOVERY TABLE A — WRONG VERDICT INVENTORY: present as named table" = FULL. The fix: gate assertions use the exact TABLE NAMES in ALL-CAPS as they appear in the skill body — not rubric criterion IDs.

**Single-axis:** V-01 (C-40), V-02 (C-41), V-03 (phrasing register).
**Combined:** V-04 (C-40 + C-41), V-05 (C-40 + C-41 + bidirectional manifest citation).

---

## Summary Table

| ID | Primary Axis | C-40 Mechanism | C-41 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|------------|
| V-01 | C-40 (single) | Each downstream section header carries `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration naming source and operation | R16-V-05 gate unchanged | Explicit derivation declarations in section headers are what distinguishes C-40 FULL from PARTIAL — structural evidence is not enough when the manifest is not named as the source in the section itself |
| V-02 | C-41 (single) | R16-V-05 manifest topology unchanged; derivation relationships stated in prose only | Phase 2 exit gate is a named-artifact assertion table with structural artifact names in ALL-CAPS and presence conditions | Gate assertions using exact table names (not rubric IDs, not prose) are what C-41 requires; a gate row reads "BACKWARD RECOVERY TABLE A — WRONG VERDICT INVENTORY: present as named structural table" not "C-38: PRESENT" |
| V-03 | Phrasing register (single) | No structural change; derivation stated in inline parentheticals "(rows from AUDIT MANIFEST where Verdict = WRONG)" | No structural change; gate uses per-role exit contracts (role may not proceed until named outputs exist) | Role-based framing with named output obligations may produce equivalent structural enforcement with lower token overhead; tests whether phase numbers are load-bearing or cosmetic |
| V-04 | C-40 + C-41 (combined) | Section headers from V-01: `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` | Named-artifact assertion table from V-02: ALL-CAPS table names + presence conditions | C-40 lives in table headers, C-41 lives in gate block — structurally independent locations; combined variation tests zero-interference |
| V-05 | Full integration | V-04 derivation headers + AUDIT MANIFEST gains a `Derived Views` column naming which downstream table each row feeds | V-04 gate + PRE-EXECUTION CONTRACT gains a `Manifest column` field mapping each structural guarantee to the exact AUDIT MANIFEST column that sources it | Bidirectional audit trail: manifest → downstream (Derived Views column) and downstream → manifest (section headers); PRE-EXECUTION CONTRACT as navigation index for auditors; gate as completion assertion for scorers |

---

## V-01 — Explicit Derivation Declarations: C-40 via Named-Source Section Headers

**Axis:** C-40 (single). Every downstream table header carries a `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` declaration that names the manifest as source and states the derivation operation. All other phases unchanged from R16-V-05 base.

**Hypothesis:** R16-V-05's manifest topology made derivation structurally evident, but C-40 requires relationships to be *stated*. A section that presents a table without a derivation header fails C-40 FULL even if the manifest exists. Explicit headers create a named statement — not an inference — that each section is a view of the manifest.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, identify gaps, and name the one unexpected finding.
All downstream analysis tables are derived views of the AUDIT MANIFEST built in Phase 1.
No downstream section is independently authored.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this scope only.
Every table carries an explicit scope marker. Phase 2 includes an OOS supplementary table.{{/if}}

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [feature shipped / spec committed / decision made] |
| Signal window | [bounding date range or sprint scope for predictions evaluated] |
| Mode | FRESH or AMEND: [scope if AMEND] |

Read this block before executing Phase 1. All four fields must be populated before Phase 1 begins.

---

## PHASE 1 -- AUDIT MANIFEST

Construct the AUDIT MANIFEST. This is the only independently authored table in this retro.
All other tables are derived from it. No downstream phase may add or modify manifest rows.

{{#if amend}}[AMEND: {{amend}} only -- excluded signals appear in manifest with Verdict = N/A and
are excluded from accuracy counts. Add OOS_SCOPE column: IN or OUT.]{{/if}}

| Signal ID | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-----------|------------|----------------|---------|------|-----------------|
| [id] | [ns] | [what was predicted] | [what happened] | CORRECT / WRONG / N/A | YES / NO | YES / NO |

Rules:
- One row per signal with a directional prediction. Signals without predictions: Verdict = N/A.
- Echo Candidate? = YES: outcome was not predicted, not a named risk, not a known unknown.
- At most one row may have Echo Candidate? = YES. Select highest commit-decision impact.
- Echo Candidate? column is locked after Phase 1. No downstream phase may alter it.

PHASE 1 SEAL:
  [ ] AUDIT MANIFEST present with all 7 named columns
  [ ] At most one row has Echo Candidate? = YES
  [ ] All rows have Verdict = CORRECT, WRONG, or N/A

---

## PHASE 2 -- DERIVED TABLES

All tables in this phase are derived views of the AUDIT MANIFEST. No row in any table below
was independently authored. Section headers declare the derivation source and operation.

### BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Verdict = WRONG]
Row count must equal the count of WRONG rows in the AUDIT MANIFEST. Do not add rows.

| Signal ID | Namespace | Prediction | Actual Outcome | Why prediction failed |
|-----------|-----------|------------|----------------|-----------------------|
| [id -- must match an AUDIT MANIFEST row with Verdict = WRONG] | | | | [brief explanation] |

### BACKWARD RECOVERY TABLE B -- RECONCILIATION
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count rows by Verdict value]

| | Count |
|---|---|
| Total predictions in denominator (Verdict = CORRECT or WRONG) | N = ? |
| Correct (Verdict = CORRECT) | C = ? |
| Wrong (Verdict = WRONG) | W = ? |
| Forward check: C + W = N? | YES / NO -- must be YES before proceeding |
| N/A signals (excluded from denominator) | ? |
| Reconciled accuracy ratio | C / N = ?% |

### PHASE COVERAGE TABLE
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per namespace]

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout | | | COVERED / EMPTY |
| draft | | | COVERED / EMPTY |
| review | | | COVERED / EMPTY |
| flow | | | COVERED / EMPTY |
| trace | | | COVERED / EMPTY |
| prove | | | COVERED / EMPTY |
| listen | | | COVERED / EMPTY |
| program | | | COVERED / EMPTY |
| topic | | | COVERED / EMPTY |

PHASE 2 SEAL:
  [ ] BACKWARD RECOVERY TABLE A: row count = WRONG-count from AUDIT MANIFEST
  [ ] BACKWARD RECOVERY TABLE B: forward check = YES before proceeding
  [ ] PHASE COVERAGE TABLE: exactly 9 rows in canonical order
  [ ] Reconciled accuracy ratio C / N = ?% populated in Table B

---

## PHASE 3 -- ECHO AND DISQUALIFICATION GATE

### Echo Input
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Echo Candidate? = YES]

The Echo candidate was locked in Phase 1. This section reads that candidate. No new selection.
If zero rows have Echo Candidate? = YES: proceed directly to Echo: NONE.

### Echo Disqualification Gate

Before writing the Echo, confirm all three gates:

| Gate | Check | Result |
|------|-------|--------|
| 1. Not a WRONG prediction restated | Candidate does not appear in BACKWARD RECOVERY TABLE A | PASS / FAIL |
| 2. Not a named risk | Candidate was not listed as a known risk or acknowledged unknown at commit time | PASS / FAIL |
| 3. Not within signal bounds | No gathered signal, even partially, predicted this outcome | PASS / FAIL |

If any gate = FAIL: Echo = NONE. The wrong prediction may not be promoted to Echo.

### Echo Record

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|--------------------|------------------------|-----------------|
| [finding or "Echo: NONE -- reason"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A |

> **Systemic pattern**: [taxonomy label: adoption-assumption-gap | integration-surface-miss |
>   timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: name]
> **Why unexpected**: [which prior belief or assumption this finding contradicted; what was
>   expected and why reality diverged]
> **Actionable follow-up**: [one specific action: new skill / rubric amendment / threshold change]

PHASE 3 SEAL:
  [ ] Echo Candidate sourced from AUDIT MANIFEST Phase 1 lock -- not newly selected
  [ ] All three disqualification gate rows completed with PASS or FAIL
  [ ] Echo: NONE stated with reason if no qualifying candidate exists
  [ ] Systemic pattern and Why unexpected fields populated (not blank)

---

## PHASE 4 -- GAP ANALYSIS

List namespaces and signal types absent during the topic run that would have changed the
commit decision. Source: PHASE COVERAGE TABLE rows where Status = EMPTY.

| Gap ID | Namespace | Signal type absent | Decision impact | Priority |
|--------|-----------|-------------------|----------------|----------|
| G-01 | [ns] | [skill or signal type] | [unanswered question] | HIGH / MED / LOW |

If no absence had decision impact: state "No decision-critical gaps identified."

PHASE 4 SEAL:
  [ ] Gap Priority column present with HIGH / MED / LOW values
  [ ] Each gap row has a decision impact statement (not blank)

---

## PHASE 5 -- IMPROVEMENT RECOMMENDATION

State one practice change addressing the highest-priority gap or the Echo systemic pattern.

| What to change | Addresses | Practice change | Signal type affected |
|----------------|-----------|----------------|---------------------|
| [specific skill or process] | Gap: [G-ID] or Echo: [pattern name] | [specific change -- not "gather more signals"] | [namespace/skill] |

PHASE 5 SEAL:
  [ ] "Addresses" field names a specific Gap ID or Echo pattern -- not generic
  [ ] Practice change is specific and actionable

---

Write artifact to: simulations/{topic}/retro-{date}.md
Frontmatter: skill: topic-retro | topic: {topic} | date: {date}
```

---

## V-02 — Named-Artifact Assertion Gate: C-41 via Structural Presence Table

**Axis:** C-41 (single). Phase 2 exit gate is replaced by a named-artifact assertion table. Each row names an exact structural artifact in ALL-CAPS (matching the table names used in the skill body) and states a presence condition. The C-40 manifest topology is carried forward from R16-V-05 with prose derivation statements — no section headers changed.

**Hypothesis:** C-41 FULL requires the gate to reference artifacts by their structural artifact name, not by rubric ID or prose description. A gate row that says "C-38: PRESENT" fails because it cites a rubric ID. A gate row that says "BACKWARD RECOVERY TABLE A — WRONG VERDICT INVENTORY: present as named structural table, row count = manifest WRONG-count" passes because it names the exact artifact. The named-artifact assertion table is the minimal structural change that produces C-41 FULL.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, identify gaps, and name the one unexpected finding.
Phase 1 builds the AUDIT MANIFEST. Phase 2 derives all downstream tables from it.
No downstream section is independently authored.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this scope only.
Every table carries an explicit scope marker. Phase 2 includes an OOS supplementary table.{{/if}}

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [feature shipped / spec committed / decision made] |
| Signal window | [bounding date range or sprint scope for predictions evaluated] |
| Mode | FRESH or AMEND: [scope if AMEND] |

Read this block before executing Phase 1. All four fields must be populated before Phase 1 begins.

---

## PHASE 1 -- AUDIT MANIFEST

Construct the AUDIT MANIFEST. This is the primary artifact. All subsequent tables are derived
from it by filtering or grouping. Do not author any downstream table independently.

| Signal ID | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-----------|------------|----------------|---------|------|-----------------|
| [id] | [ns] | [what was predicted] | [what happened] | CORRECT / WRONG / N/A | YES / NO | YES / NO |

Rules:
- One row per signal with a directional prediction. No-prediction signals: Verdict = N/A.
- Echo Candidate? = YES: outcome was not predicted, not a named risk, not a known unknown.
- At most one row may have Echo Candidate? = YES.
- Echo Candidate? column is locked after Phase 1 SEAL. No downstream phase may alter it.

PHASE 1 SEAL:
  [ ] AUDIT MANIFEST present with all 7 named columns
  [ ] At most one row has Echo Candidate? = YES
  [ ] All rows have Verdict = CORRECT, WRONG, or N/A

---

## PHASE 2 -- DERIVED TABLES

Backward recovery tables derive from the AUDIT MANIFEST by filtering WRONG rows.
Coverage table derives from the AUDIT MANIFEST by grouping on Namespace.
No rows in these tables are independently authored.

### BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY

Rows: all AUDIT MANIFEST entries where Verdict = WRONG. Do not add entries not in the manifest.

| Signal ID | Namespace | Prediction | Actual Outcome | Why prediction failed |
|-----------|-----------|------------|----------------|-----------------------|
| [id -- manifest row, Verdict = WRONG] | | | | [brief explanation] |

### BACKWARD RECOVERY TABLE B -- RECONCILIATION

Counts derived from AUDIT MANIFEST verdict column.

| | Count |
|---|---|
| Total predictions (Verdict = CORRECT or WRONG) | N = ? |
| Correct (Verdict = CORRECT) | C = ? |
| Wrong (Verdict = WRONG) | W = ? |
| Forward check: C + W = N? | YES / NO -- stop if NO |
| N/A signals (outside denominator) | ? |
| Reconciled accuracy ratio | C / N = ?% |

### PHASE COVERAGE TABLE

Rows: one per namespace derived from AUDIT MANIFEST namespace column.

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout | | | COVERED / EMPTY |
| draft | | | COVERED / EMPTY |
| review | | | COVERED / EMPTY |
| flow | | | COVERED / EMPTY |
| trace | | | COVERED / EMPTY |
| prove | | | COVERED / EMPTY |
| listen | | | COVERED / EMPTY |
| program | | | COVERED / EMPTY |
| topic | | | COVERED / EMPTY |

### PHASE 2 EXIT GATE -- NAMED-ARTIFACT ASSERTIONS

Each row names the exact structural artifact that must be present before Phase 3 may begin.
A row may not be checked unless the named artifact is present with the stated condition met.

| Structural artifact | Presence condition | Assert |
|--------------------|--------------------|--------|
| AUDIT MANIFEST | Named table with 7 columns; rows locked (Phase 1 SEAL confirmed) | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY | Present as named structural table; row count = WRONG verdict count from AUDIT MANIFEST | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE B -- RECONCILIATION | Present as named structural table; forward check row = YES; reconciled accuracy ratio populated | PRESENT / ABSENT |
| PHASE COVERAGE TABLE | Present as named structural table; exactly 9 rows; Status column contains only COVERED or EMPTY | PRESENT / ABSENT |

All four rows must be PRESENT before Phase 3 begins.

---

## PHASE 3 -- ECHO AND DISQUALIFICATION GATE

Echo input: AUDIT MANIFEST rows where Echo Candidate? = YES. Candidate was locked in Phase 1.
If zero rows qualify: proceed directly to Echo: NONE.

### Echo Disqualification Gate

| Gate | Check | Result |
|------|-------|--------|
| 1. Not a WRONG prediction restated | Candidate not in BACKWARD RECOVERY TABLE A | PASS / FAIL |
| 2. Not a named risk | Not listed as known risk or acknowledged unknown at commit time | PASS / FAIL |
| 3. Not within signal bounds | No gathered signal predicted this outcome even partially | PASS / FAIL |

If any gate = FAIL: Echo = NONE. Wrong prediction may not be promoted to Echo.

### Echo Record

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|--------------------|------------------------|-----------------|
| [finding or "Echo: NONE -- reason"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A |

> **Systemic pattern**: [taxonomy: adoption-assumption-gap | integration-surface-miss |
>   timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: name]
> **Why unexpected**: [which prior belief this finding contradicted; what was expected and why
>   reality diverged]
> **Actionable follow-up**: [one specific action: new skill / rubric amendment / threshold change]

PHASE 3 SEAL:
  [ ] Echo candidate sourced from Phase 1 AUDIT MANIFEST lock -- not newly selected
  [ ] All three disqualification gate rows completed PASS or FAIL
  [ ] Echo: NONE stated with reason if no qualifying candidate
  [ ] Systemic pattern and Why unexpected fields populated

---

## PHASE 4 -- GAP ANALYSIS

| Gap ID | Namespace | Signal type absent | Decision impact | Priority |
|--------|-----------|-------------------|----------------|----------|
| G-01 | [ns] | [skill or signal type] | [unanswered question at commit time] | HIGH / MED / LOW |

If no absence had decision impact: state "No decision-critical gaps identified."

PHASE 4 SEAL:
  [ ] Gap Priority column present with HIGH / MED / LOW values
  [ ] Each gap has a decision impact statement

---

## PHASE 5 -- IMPROVEMENT RECOMMENDATION

| What to change | Addresses | Practice change | Signal type affected |
|----------------|-----------|----------------|---------------------|
| [skill or process] | Gap: [G-ID] or Echo: [pattern name] | [specific change] | [namespace/skill] |

PHASE 5 SEAL:
  [ ] "Addresses" names a specific Gap ID or Echo pattern name
  [ ] Practice change is specific (not "gather more signals")

---

Write artifact to: simulations/{topic}/retro-{date}.md
Frontmatter: skill: topic-retro | topic: {topic} | date: {date}
```

---

## V-03 — Role-Based Framing: Phrasing Register via Named Output Obligations

**Axis:** Phrasing register (single). Replaces numbered phases with named roles. Each role has a defined output obligation: it may not hand off until its named outputs are present. The structural requirements (manifest topology, disqualification gate, accuracy reconciliation) are preserved; the framing shifts from imperative phase execution to role-bounded output contracts.

**Hypothesis:** Numbered phase headers enforce sequence but do not state what output each phase produces. Named role obligations make the output obligation legible without reading the phase body — the role name and its output contract appear in the same location. This tests whether role framing can achieve equivalent structural enforcement with different cognitive overhead.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Four roles run in sequence, each owning a named output.
No role modifies a prior role's output. Roles hand off by producing their output; the next
role reads that output, does not re-derive it.

{{#if amend}}AMEND SCOPE: {{amend}} -- all roles operate within this scope. Every table carries
a scope marker. The Surveyor includes an out-of-scope supplementary table.{{/if}}

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [feature shipped / spec committed / decision made] |
| Signal window | [bounding date range or sprint scope for predictions evaluated] |
| Mode | FRESH or AMEND: [scope if AMEND] |

Read this block before the Archivist begins. All four fields must be populated.

---

## ROLE 1 -- ARCHIVIST
Output obligation: AUDIT MANIFEST (primary artifact). All downstream roles read from this table.
The Archivist does not evaluate, interpret, or gap-analyze. Output = manifest rows only.

Construct the AUDIT MANIFEST from signal artifacts in simulations/{namespace}/:

| Signal ID | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-----------|------------|----------------|---------|------|-----------------|
| [id] | [ns] | [what was predicted] | [what happened] | CORRECT / WRONG / N/A | YES / NO | YES / NO |

Rules:
- One row per signal with a directional prediction. No-prediction signals: Verdict = N/A.
- Echo Candidate? = YES: outcome not predicted, not a named risk, not a known unknown.
- At most one row may have Echo Candidate? = YES (highest commit-decision impact).
- Echo Candidate? is locked when the Archivist hands off. No later role may alter it.

ARCHIVIST HANDOFF CONTRACT:
  [ ] AUDIT MANIFEST present with all 7 named columns
  [ ] At most one row has Echo Candidate? = YES
  [ ] All rows have Verdict in {CORRECT, WRONG, N/A}
  [ ] AUDIT MANIFEST locked -- no downstream role adds or modifies rows

---

## ROLE 2 -- ANALYST
Output obligation: BACKWARD RECOVERY TABLE A, BACKWARD RECOVERY TABLE B, PHASE COVERAGE TABLE.
The Analyst derives these three tables from the AUDIT MANIFEST. No row is authored independently.
The Analyst does not assess the Echo candidate or write gaps.

### BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY
Rows: AUDIT MANIFEST entries where Verdict = WRONG. Row count must match manifest WRONG-count.

| Signal ID | Namespace | Prediction | Actual Outcome | Why prediction failed |
|-----------|-----------|------------|----------------|-----------------------|
| [manifest row, Verdict = WRONG] | | | | [brief explanation] |

### BACKWARD RECOVERY TABLE B -- RECONCILIATION
Counts from AUDIT MANIFEST verdict column.

| | Count |
|---|---|
| Total predictions (Verdict = CORRECT or WRONG) | N = ? |
| Correct | C = ? |
| Wrong | W = ? |
| Forward check: C + W = N? | YES / NO -- must be YES before proceeding |
| N/A signals (outside denominator) | ? |
| Reconciled accuracy ratio | C / N = ?% |

### PHASE COVERAGE TABLE
One row per canonical namespace; counts from AUDIT MANIFEST namespace column.

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout | | | COVERED / EMPTY |
| draft | | | COVERED / EMPTY |
| review | | | COVERED / EMPTY |
| flow | | | COVERED / EMPTY |
| trace | | | COVERED / EMPTY |
| prove | | | COVERED / EMPTY |
| listen | | | COVERED / EMPTY |
| program | | | COVERED / EMPTY |
| topic | | | COVERED / EMPTY |

ANALYST HANDOFF CONTRACT:
  [ ] TABLE A row count = AUDIT MANIFEST WRONG-count
  [ ] TABLE B forward check = YES
  [ ] PHASE COVERAGE TABLE has exactly 9 rows
  [ ] Reconciled accuracy ratio C / N = ?% present in TABLE B

---

## ROLE 3 -- ECHO-JUDGE
Output obligation: ECHO RECORD with Systemic pattern, Why unexpected, Actionable follow-up.
The Echo-Judge reads the AUDIT MANIFEST (Echo Candidate? = YES row only) and runs the
disqualification gate. The Echo-Judge does not re-evaluate wrong verdicts or coverage.

Echo candidate: AUDIT MANIFEST row where Echo Candidate? = YES (locked by Archivist).
If zero rows qualify: output Echo: NONE and state reason. Skip gate.

### Echo Disqualification Gate

| Gate | Check | Result |
|------|-------|--------|
| 1. Not a WRONG prediction | Candidate does not appear in BACKWARD RECOVERY TABLE A | PASS / FAIL |
| 2. Not a named risk | Not listed as known risk or acknowledged unknown at commit time | PASS / FAIL |
| 3. Not within signal bounds | No gathered signal predicted this outcome, even partially | PASS / FAIL |

If any gate = FAIL: Echo = NONE. Wrong prediction may not be promoted.

### Echo Record

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|--------------------|------------------------|-----------------|
| [finding or "Echo: NONE -- reason"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A |

> **Systemic pattern**: [taxonomy: adoption-assumption-gap | integration-surface-miss |
>   timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: name]
> **Why unexpected**: [which prior belief or assumption this finding contradicted]
> **Actionable follow-up**: [one specific action: new skill / rubric amendment / threshold change]

ECHO-JUDGE HANDOFF CONTRACT:
  [ ] Echo candidate sourced from Archivist's AUDIT MANIFEST lock -- not newly selected
  [ ] All three gate rows completed PASS or FAIL
  [ ] Echo: NONE stated with reason if no qualifying candidate
  [ ] Systemic pattern, Why unexpected, Actionable follow-up all populated

---

## ROLE 4 -- CURATOR
Output obligation: GAP TABLE and IMPROVEMENT RECOMMENDATION.
The Curator reads PHASE COVERAGE TABLE (empty namespaces) and ECHO RECORD.
The Curator does not re-derive accuracy counts or revisit the Echo candidate.

### Gap Table

| Gap ID | Namespace | Signal type absent | Decision impact | Priority |
|--------|-----------|-------------------|----------------|----------|
| G-01 | [ns] | [skill or signal type] | [unanswered question at commit time] | HIGH / MED / LOW |

If no absence had decision impact: state "No decision-critical gaps identified."

### Improvement Recommendation

| What to change | Addresses | Practice change | Signal type affected |
|----------------|-----------|----------------|---------------------|
| [skill or process] | Gap: [G-ID] or Echo: [pattern name] | [specific change] | [namespace/skill] |

CURATOR HANDOFF CONTRACT:
  [ ] Gap Priority column present (HIGH / MED / LOW)
  [ ] Each gap has a decision impact statement
  [ ] "Addresses" field names a specific Gap ID or Echo pattern name
  [ ] Practice change is specific (not "gather more signals")

---

Write artifact to: simulations/{topic}/retro-{date}.md
Frontmatter: skill: topic-retro | topic: {topic} | date: {date}
```

---

## V-04 — Derivation Declarations + Named-Artifact Gate: C-40 + C-41 Combined

**Axis:** C-40 + C-41 (combined). V-01's derivation annotations in every downstream section header (C-40) + V-02's named-artifact assertion table in the Phase 2 exit gate (C-41). No other changes from the base. Zero-interference test: derivation headers live in table prefixes, gate assertions live in the exit gate block — independent structural locations.

**Hypothesis:** C-40 and C-41 target different structural locations. C-40 annotations are in section headers; C-41 assertions are in the gate. They do not conflict. Combining them should produce FULL pass on both without degrading any other criterion. The combined variation tests whether both can coexist cleanly in the same prompt.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, identify gaps, and name the one unexpected finding.
Phase 1 builds the AUDIT MANIFEST -- the primary artifact and sole source for all downstream tables.
No downstream table is independently authored.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this scope only.
Every table carries a scope marker. Phase 2 includes an OOS supplementary table.{{/if}}

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [feature shipped / spec committed / decision made] |
| Signal window | [bounding date range or sprint scope for predictions evaluated] |
| Mode | FRESH or AMEND: [scope if AMEND] |

Read this block before Phase 1. All four fields must be populated before Phase 1 begins.

---

## PHASE 1 -- AUDIT MANIFEST

Build the AUDIT MANIFEST. This is the only independently authored table.
Filtering WRONG rows from this table produces BACKWARD RECOVERY TABLE A.
Counting rows by Verdict produces BACKWARD RECOVERY TABLE B.
Grouping rows by Namespace produces the PHASE COVERAGE TABLE.
Filtering Echo Candidate? = YES from this table produces the Echo input for Phase 3.

| Signal ID | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-----------|------------|----------------|---------|------|-----------------|
| [id] | [ns] | [what was predicted] | [what happened] | CORRECT / WRONG / N/A | YES / NO | YES / NO |

Rules:
- One row per signal with a directional prediction. No-prediction signals: Verdict = N/A.
- Echo Candidate? = YES: outcome not predicted, not a named risk, not a known unknown.
- At most one row may have Echo Candidate? = YES.
- Echo Candidate? is locked after Phase 1 SEAL. No downstream phase may alter it.

PHASE 1 SEAL:
  [ ] AUDIT MANIFEST present with all 7 named columns
  [ ] At most one row has Echo Candidate? = YES
  [ ] All rows have Verdict in {CORRECT, WRONG, N/A}

---

## PHASE 2 -- DERIVED TABLES AND EXIT GATE

### BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Verdict = WRONG]
Row count must equal manifest WRONG-count. No independently authored rows.

| Signal ID | Namespace | Prediction | Actual Outcome | Why prediction failed |
|-----------|-----------|------------|----------------|-----------------------|
| [manifest row, Verdict = WRONG] | | | | [brief explanation] |

### BACKWARD RECOVERY TABLE B -- RECONCILIATION
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count rows by Verdict value]

| | Count |
|---|---|
| Total predictions (Verdict = CORRECT or WRONG) | N = ? |
| Correct (Verdict = CORRECT) | C = ? |
| Wrong (Verdict = WRONG) | W = ? |
| Forward check: C + W = N? | YES / NO -- must be YES before proceeding |
| N/A signals (outside denominator) | ? |
| Reconciled accuracy ratio | C / N = ?% |

### PHASE COVERAGE TABLE
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per namespace]

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout | | | COVERED / EMPTY |
| draft | | | COVERED / EMPTY |
| review | | | COVERED / EMPTY |
| flow | | | COVERED / EMPTY |
| trace | | | COVERED / EMPTY |
| prove | | | COVERED / EMPTY |
| listen | | | COVERED / EMPTY |
| program | | | COVERED / EMPTY |
| topic | | | COVERED / EMPTY |

### PHASE 2 EXIT GATE -- NAMED-ARTIFACT ASSERTIONS

Each row names the exact structural artifact required before Phase 3 begins.
A row may not be checked unless the named artifact is present with the stated condition met.

| Structural artifact | Presence condition | Assert |
|--------------------|--------------------|--------|
| AUDIT MANIFEST | Named table with 7 columns; rows locked (Phase 1 SEAL confirmed) | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY | Present as named structural table; row count = manifest WRONG-count; no independently authored rows | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE B -- RECONCILIATION | Present as named structural table; forward check row = YES; reconciled accuracy ratio C / N = ?% populated | PRESENT / ABSENT |
| PHASE COVERAGE TABLE | Present as named structural table; exactly 9 rows in canonical order; Status column contains only COVERED or EMPTY | PRESENT / ABSENT |

All four rows must read PRESENT before Phase 3 begins.

---

## PHASE 3 -- ECHO AND DISQUALIFICATION GATE

### Echo Input
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Echo Candidate? = YES]
Candidate was locked in Phase 1. This section reads that row. No new candidate selection.
If zero rows qualify: proceed directly to Echo: NONE with reason.

### Echo Disqualification Gate

| Gate | Check | Result |
|------|-------|--------|
| 1. Not a WRONG prediction | Candidate not in BACKWARD RECOVERY TABLE A | PASS / FAIL |
| 2. Not a named risk | Not listed as known risk or acknowledged unknown at commit time | PASS / FAIL |
| 3. Not within signal bounds | No gathered signal predicted this outcome, even partially | PASS / FAIL |

If any gate = FAIL: Echo = NONE. Wrong prediction may not be promoted to Echo.

### Echo Record

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|--------------------|------------------------|-----------------|
| [finding or "Echo: NONE -- reason"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A |

> **Systemic pattern**: [taxonomy: adoption-assumption-gap | integration-surface-miss |
>   timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: name]
> **Why unexpected**: [which prior belief this finding contradicted; what was expected and why
>   reality diverged]
> **Actionable follow-up**: [one specific action: new skill / rubric amendment / threshold change]

PHASE 3 SEAL:
  [ ] Echo candidate from AUDIT MANIFEST Phase 1 lock -- not newly selected
  [ ] All three disqualification gate rows: PASS or FAIL
  [ ] Echo: NONE with reason if no qualifying candidate
  [ ] Systemic pattern, Why unexpected, Actionable follow-up all populated

---

## PHASE 4 -- GAP ANALYSIS

| Gap ID | Namespace | Signal type absent | Decision impact | Priority |
|--------|-----------|-------------------|----------------|----------|
| G-01 | [ns] | [skill or signal type] | [unanswered question at commit time] | HIGH / MED / LOW |

If no absence had decision impact: state "No decision-critical gaps identified."

PHASE 4 SEAL:
  [ ] Gap Priority column: HIGH / MED / LOW
  [ ] Each gap has a decision impact statement

---

## PHASE 5 -- IMPROVEMENT RECOMMENDATION

| What to change | Addresses | Practice change | Signal type affected |
|----------------|-----------|----------------|---------------------|
| [skill or process] | Gap: [G-ID] or Echo: [pattern name] | [specific change] | [namespace/skill] |

PHASE 5 SEAL:
  [ ] "Addresses" names specific Gap ID or Echo pattern name
  [ ] Practice change is specific (not "gather more signals")

---

Write artifact to: simulations/{topic}/retro-{date}.md
Frontmatter: skill: topic-retro | topic: {topic} | date: {date}
```

---

## V-05 — Full Integration: C-40 + C-41 + Bidirectional Manifest Citation

**Axis:** Full integration. V-04's derivation headers + named-artifact gate + three additional bidirectional citation mechanisms:

1. **AUDIT MANIFEST gains a `Derived Views` column** naming which downstream table each row's Verdict value feeds, making the derivation graph explicit in the manifest itself.
2. **PRE-EXECUTION CONTRACT gains a `Manifest column` field** mapping each structural guarantee to the exact AUDIT MANIFEST column that sources it — converting the contract from a prose promise list into a navigable audit index.
3. **Phase 3 Echo disqualification gate references BACKWARD RECOVERY TABLE A by structural artifact name** as the lookup source for Gate 1, closing the bidirectional loop: manifest → Table A (via derivation header) and Table A → disqualification gate (via named reference).

**Hypothesis:** V-04 ensures derivation is declared (C-40 FULL) and the gate names artifacts (C-41 FULL). V-05 extends this into a complete audit trail: an auditor can enter from any direction — start from the manifest, follow the Derived Views column to Table A, confirm Table A is present via the Phase 2 Exit Gate, and trace back to the PRE-EXECUTION CONTRACT via the Manifest column field. The bidirectional structure makes each audit path independently navigable without reading phase specifications. This compound enforcement structure should score highest on the new aspiration criteria while preserving all prior criteria.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, identify gaps, and name the one unexpected finding.
The AUDIT MANIFEST is the primary artifact. All downstream tables are derived from it.
The PRE-EXECUTION CONTRACT maps each structural guarantee to its manifest source.
No downstream table is independently authored.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this scope only.
Every table carries a scope marker. Phase 2 includes an OOS supplementary table.{{/if}}

---

## PRE-EXECUTION CONTRACT

| Field | Value | Manifest column |
|-------|-------|-----------------|
| Topic | [topic name] | (pre-execution, no manifest column) |
| Commitment nature | [feature shipped / spec committed / decision made] | (pre-execution) |
| Signal window | [bounding date range or sprint scope for predictions evaluated] | (pre-execution) |
| Mode | FRESH or AMEND: [scope if AMEND] | (pre-execution) |

| Structural guarantee | What is enforced | Manifest column |
|---------------------|-----------------|-----------------|
| Echo lock | Echo Candidate? locked in Phase 1; no downstream phase may alter it | Echo Candidate? |
| Verdict integrity | All rows have Verdict = CORRECT, WRONG, or N/A | Verdict |
| Backward recovery | Filtering Verdict = WRONG from manifest produces TABLE A; no independent authoring | Verdict |
| Accuracy ratio | Counting manifest rows by Verdict value produces TABLE B reconciliation | Verdict |
| Coverage | Grouping manifest rows by Namespace produces PHASE COVERAGE TABLE | Namespace |
| Echo input | Filtering Echo Candidate? = YES produces the Phase 3 Echo input | Echo Candidate? |
| Gap flag | Gap? column identifies signals with decision-relevant absences | Gap? |

Read both blocks before Phase 1. All pre-execution fields and manifest column mappings must be
legible before proceeding. The Manifest column field names the exact AUDIT MANIFEST column
that enforces each guarantee -- use it to audit any guarantee without reading phase specifications.

---

## PHASE 1 -- AUDIT MANIFEST

Build the AUDIT MANIFEST. This is the only independently authored table.
The Derived Views column records which downstream artifact each manifest row contributes to.

| Signal ID | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? | Derived Views |
|-----------|-----------|------------|----------------|---------|------|-----------------|---------------|
| [id] | [ns] | [what was predicted] | [what happened] | CORRECT / WRONG / N/A | YES / NO | YES / NO | [TABLE A if WRONG; TABLE B count; COVERAGE if namespace counted; ECHO INPUT if YES] |

Rules:
- One row per signal with a directional prediction. No-prediction signals: Verdict = N/A.
- Echo Candidate? = YES: outcome not predicted, not a named risk, not a known unknown.
- At most one row may have Echo Candidate? = YES.
- Derived Views column: state which downstream tables this row feeds. Minimum entries:
    - All rows: "TABLE B count"
    - WRONG rows: add "TABLE A"
    - Echo Candidate? = YES rows: add "ECHO INPUT"
    - Each namespace's first row: add "COVERAGE"
- Echo Candidate? and all Derived Views entries are locked after Phase 1 SEAL.

PHASE 1 SEAL:
  [ ] AUDIT MANIFEST present with all 8 named columns (including Derived Views)
  [ ] At most one row has Echo Candidate? = YES
  [ ] All rows have Verdict in {CORRECT, WRONG, N/A}
  [ ] Derived Views column populated for all rows

---

## PHASE 2 -- DERIVED TABLES AND EXIT GATE

### BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Verdict = WRONG]
Row count must equal count of manifest rows with Verdict = WRONG. No independently authored rows.
Each row in this table has a corresponding AUDIT MANIFEST row with "TABLE A" in Derived Views.

| Signal ID | Namespace | Prediction | Actual Outcome | Why prediction failed |
|-----------|-----------|------------|----------------|-----------------------|
| [manifest row, Verdict = WRONG] | | | | [brief explanation] |

### BACKWARD RECOVERY TABLE B -- RECONCILIATION
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count rows by Verdict value]
All counts come from Verdict column. Do not recount from TABLE A.

| | Count |
|---|---|
| Total predictions (Verdict = CORRECT or WRONG) | N = ? |
| Correct (Verdict = CORRECT) | C = ? |
| Wrong (Verdict = WRONG) | W = ? |
| Forward check: C + W = N? | YES / NO -- must be YES before proceeding |
| N/A signals (outside denominator) | ? |
| Reconciled accuracy ratio | C / N = ?% |

### PHASE COVERAGE TABLE
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per namespace]
One row per canonical namespace. No namespace may be added or removed.

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout | | | COVERED / EMPTY |
| draft | | | COVERED / EMPTY |
| review | | | COVERED / EMPTY |
| flow | | | COVERED / EMPTY |
| trace | | | COVERED / EMPTY |
| prove | | | COVERED / EMPTY |
| listen | | | COVERED / EMPTY |
| program | | | COVERED / EMPTY |
| topic | | | COVERED / EMPTY |

### PHASE 2 EXIT GATE -- NAMED-ARTIFACT ASSERTIONS

Each row names the exact structural artifact required before Phase 3 begins.
A row may not be checked unless the named artifact is present with the stated condition met.
Gate rows reference structural artifact names as they appear in this document (ALL-CAPS headers).

| Structural artifact | Presence condition | Assert |
|--------------------|--------------------|--------|
| AUDIT MANIFEST | Named table with 8 columns (including Derived Views); rows locked; Derived Views column populated | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY | Present as named structural table; row count = count of manifest rows with Verdict = WRONG; each row maps to a manifest Derived Views entry containing "TABLE A" | PRESENT / ABSENT |
| BACKWARD RECOVERY TABLE B -- RECONCILIATION | Present as named structural table; forward check row = YES; reconciled accuracy ratio C / N = ?% populated; counts not recomputed from TABLE A | PRESENT / ABSENT |
| PHASE COVERAGE TABLE | Present as named structural table; exactly 9 rows in canonical order; Status column contains only COVERED or EMPTY | PRESENT / ABSENT |

All four rows must read PRESENT before Phase 3 begins.

---

## PHASE 3 -- ECHO AND DISQUALIFICATION GATE

### Echo Input
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter WHERE Echo Candidate? = YES]
The candidate was locked in Phase 1. Read the AUDIT MANIFEST row with Echo Candidate? = YES.
That row's Derived Views entry should contain "ECHO INPUT" (locked in Phase 1).
If zero rows have Echo Candidate? = YES: proceed directly to Echo: NONE with reason.

### Echo Disqualification Gate

| Gate | Lookup source | Check | Result |
|------|--------------|-------|--------|
| 1. Not a WRONG prediction | BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY | Echo candidate Signal ID does not appear in TABLE A | PASS / FAIL |
| 2. Not a named risk | Commit-time documentation | Not listed as known risk or acknowledged unknown at commit time | PASS / FAIL |
| 3. Not within signal bounds | AUDIT MANIFEST predictions | No gathered signal predicted this outcome, even partially | PASS / FAIL |

Gate 1 names BACKWARD RECOVERY TABLE A as the lookup source.
If any gate = FAIL: Echo = NONE. Wrong prediction may not be promoted to Echo.

### Echo Record

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|--------------------|------------------------|-----------------|
| [finding or "Echo: NONE -- reason"] | [artifact name or "none"] | HIGH / MEDIUM / LOW / N/A |

> **Systemic pattern**: [taxonomy: adoption-assumption-gap | integration-surface-miss |
>   timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: name]
> **Why unexpected**: [which prior belief this finding contradicted; what was expected and why
>   reality diverged]
> **Actionable follow-up**: [one specific action: new skill / rubric amendment / threshold change]

PHASE 3 SEAL:
  [ ] Echo candidate from AUDIT MANIFEST Phase 1 lock (Derived Views = ECHO INPUT) -- not newly selected
  [ ] Gate 1 lookup source named as BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY
  [ ] All three disqualification gate rows: PASS or FAIL
  [ ] Echo: NONE with reason if no qualifying candidate
  [ ] Systemic pattern, Why unexpected, Actionable follow-up all populated

---

## PHASE 4 -- GAP ANALYSIS

| Gap ID | Namespace | Signal type absent | Decision impact | Priority |
|--------|-----------|-------------------|----------------|----------|
| G-01 | [ns] | [skill or signal type] | [unanswered question at commit time] | HIGH / MED / LOW |

If no absence had decision impact: state "No decision-critical gaps identified."

PHASE 4 SEAL:
  [ ] Gap Priority column: HIGH / MED / LOW
  [ ] Each gap has a decision impact statement

---

## PHASE 5 -- IMPROVEMENT RECOMMENDATION

| What to change | Addresses | Practice change | Signal type affected |
|----------------|-----------|----------------|---------------------|
| [skill or process] | Gap: [G-ID] or Echo: [pattern name] | [specific change] | [namespace/skill] |

PHASE 5 SEAL:
  [ ] "Addresses" names specific Gap ID or Echo pattern name
  [ ] Practice change is specific (not "gather more signals")

---

Write artifact to: simulations/{topic}/retro-{date}.md
Frontmatter: skill: topic-retro | topic: {topic} | date: {date}
```

---

## Design Notes — R17

**Why V-05 extends beyond V-04:**

The `Derived Views` column in the AUDIT MANIFEST makes the derivation graph a first-class artifact. An auditor checking C-40 does not need to read section headers — they can read the manifest and see exactly which tables each row feeds. Combined with the Phase 2 Exit Gate naming those tables as exact structural artifacts (C-41), the two mechanisms form a closed audit loop: the manifest says where it goes, the gate confirms it arrived.

The PRE-EXECUTION CONTRACT `Manifest column` field serves a different auditor path: someone verifying that a structural guarantee is enforced can go from the contract row → manifest column → downstream derivation without reading any phase specification. This adds a second navigation axis that did not exist in V-04.

**C-40 vs C-41 independence test:**

V-01 and V-02 are single-axis to confirm that C-40 and C-41 can be satisfied independently before combining. If V-01 scores well on C-40 but poorly on C-41 (and V-02 the reverse), the axes are genuinely independent and V-04/V-05 combinations are justified. If either single-axis variation fails an essential criterion, the axis itself has a structural problem.

**V-03 role framing — expected failure mode:**

Role-based framing eliminates phase numbers, which may cause C-36 (Three-Pass Architectural Isolation as Structural Property) to fail if the rubric requires "named architectural phases with entry/exit criteria." Role handoff contracts are structurally equivalent but may not satisfy the phase-number pattern expected by C-36. This is the key hypothesis to watch in scoring.
