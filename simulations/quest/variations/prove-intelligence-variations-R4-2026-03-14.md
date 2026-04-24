**prove-intelligence R4 variations written** to `simulations/quest/variations/prove-intelligence-variations-R4-2026-03-14.md`.

---

## Summary

| ID | Axis | Targets | Key Move | Expected Score |
|----|------|---------|----------|----------------|
| **V-01** | Phrasing register | C-19 | "STOP." as unconditional halt token; Option A / Option B resolution contract — no implicit continuation path | ~96.4 (fails C-15, C-16, C-17, C-18) |
| **V-02** | Output format | C-17 | Pre-declared Schema Contract (Permitted/Prohibited column lists) + post-population Schema Verification step before Analyst begins | ~98.2 (fails C-16, C-18) |
| **V-03** | Lifecycle emphasis | C-18 | IN-PROGRESS ledger emitted before gate fires; uncovered FCs generate named Redirect Agenda as a first-class artifact; gate fires against ledger state, not bare count | ~96.4 (fails C-15, C-17, C-19 — intentional) |
| **V-04** | Output format + Lifecycle | C-17 + C-18 | Schema Contract + pre-gate Redirect Agenda; advisory gate phrasing intentionally used to isolate C-19 as the V-05 differentiator | ~99.1 (fails C-19 only) |
| **V-05** | All three combined | C-17 + C-18 + C-19 | V-04 base with halt-semantics gate: "STOP. Do not proceed to Phase 4." + explicit Option A/B resolution contract; targets all 11 aspirationals | 100 |

**What's new vs. R3:**

- **C-19 (V-01)**: R3 V-01 had "STOP. Do not proceed to Step 6." but treated it as text to emit. R4 V-01 names the distinction explicitly — "advisory phrasing permits implicit continuation after a nominal attempt; halt semantics require explicit resolution" — and adds an Option A / Option B resolution contract. Proceeding without selecting one is named as a protocol violation.

- **C-17 (V-02)**: R3 V-02 had a schema constraint note at the end of the table declaration. R4 V-02 adds a pre-declared contract section (before table population) with explicit Permitted/Prohibited column lists, and a `## Schema Verification` step that checks for violations before the Analyst Section begins. The schema is a named contract, not just an instruction.

- **C-18 (V-03)**: R3 V-03 had IN-PROGRESS at Phase B exit with a generic "decide whether to redirect" instruction. R4 V-03 adds the `## Redirect Agenda` as a named artifact — each `open` FC generates one specific FC-targeted re-search action (query, tool, what to look for). The gate section shows `Open FCs at gate` and `Redirect items pending` drawn directly from the IN-PROGRESS ledger state.
ific FC-targeted re-search actions, not a generic "search more" instruction, and this agenda is visible as a named section before the gate fires.

---

## V-01: C-19 Single-Axis — Unconditional Halt Semantics

**Axis**: Phrasing register — the gate WARNING block uses unconditional halt semantics with "STOP." as the leading token, names the prohibited next section, and requires explicit Option A or Option B resolution before continuation

**Hypothesis**: A gate instruction that opens with "STOP." as an unconditional halt token and requires one of two named resolution paths (re-search or reclassify) is semantically distinct from advisory phrasing that permits continuation after a nominal attempt; the advisory form leaves an implicit continuation path open, the halt form does not

**Expected pass on v4 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-19 | **Expected fail**: C-15 (in-block ordering), C-16 (single ledger state), C-17 (no schema exclusion), C-18 (no pre-gate IN-PROGRESS with redirect agenda)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**. This skill searches internal repo sources only. Your training knowledge is not a source. The public web is not a source.

---

### Step 1 — Setup

Read **{{Signal}}** and write:

1. The hypothesis in one sentence.
2. All falsification criteria (FC-01, FC-02, ...). If none are stated, derive two or three from the hypothesis claim.
3. The internal source types most likely to hold evidence: spec/design doc, scenario file, prior signal artifact, config (YAML/JSON), CLAUDE.md/session driver.

---

### Step 2 — Search

Run at least one Glob or Grep query per source type from Step 1. Log each query and result count:

```
## Search Log
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N files |
| ...   | Grep | N matches |
```

Target at least 5 candidate files. If fewer exist, note it and continue.

---

### Step 3 — Extract

Open each candidate file. For each: copy-paste the most relevant passage verbatim. Do not summarize from memory. If a file yields nothing relevant, record it as a miss.

```
## Candidate Files
| # | Path | Relevant? | Verbatim Excerpt |
|---|------|-----------|-----------------|
| 1 | ...  | yes / miss | "..." |
```

---

### Step 4 — Assess Sources

For each file marked `yes` in Step 3, produce a source block. All fields are required:

```
### Source N
- **Path**: [exact file path]
- **Excerpt**: "[verbatim text — minimum one full sentence]"
- **Relevance**: [how this excerpt supports, contradicts, or is tangential to the hypothesis — stated in terms of the hypothesis claim or FC-NN]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why this knowledge is not findable on the public web] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

---

### Step 5 — Insider Gate

Count sources where `Insider: YES`.

```
## Insider Gate
Insider sources (Insider: YES): [N]
Non-insider sources: [N]
Gate status: PASS (count >= 1) | BLOCKED (count = 0)
```

**If Gate status = BLOCKED:**

The following WARNING block is a halt instruction, not an advisory. "STOP." is the halt token — it is not interchangeable with "Note:", "Warning:", or "Before proceeding:". Advisory phrasing ("before proceeding, re-search for insider sources") permits implicit continuation after a nominal attempt. Halt semantics require explicit resolution: one of Option A or Option B below must be selected and executed before the artifact continues. Proceeding to Step 6 without completing one of these options is a protocol violation.

Emit the following block verbatim:

```
WARNING: INSIDER GATE NOT MET

This run has produced zero insider-flagged sources. Every cited source could
plausibly appear in public documentation. The defining value of
/prove:intelligence — evidence accessible only to team members — has not been
delivered.

STOP. Do not proceed to Step 6. Do not write a verdict. Do not write synthesis.

Explicit resolution required — select and execute one of:

  Option A — Targeted re-search:
    Return to Step 2 and search specifically for internal-only artifacts:
    - Implementation decisions in unpublished specs
    - Internal naming conventions not reflected in any public doc
    - Scenario outcomes from unreleased test runs
    - In-progress work not yet merged or shipped
    After re-search: if Insider count >= 1, update this gate to PASS and proceed.

  Option B — Reclassify:
    If exhaustive re-search yields zero insider sources, document that finding
    here with the exact text: "Reclassification: public-evidence-only,
    confidence: low." Label every subsequent section header with
    [PUBLIC-EVIDENCE-ONLY]. Then proceed to Step 6.

There is no implicit continuation path. Proceeding without completing Option A
or Option B is a protocol violation.
```

**If Gate status = PASS:** proceed to Step 6.

---

### Step 6 — Falsification Ledger

```
## Falsification Ledger
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Source 2, Source 4 | satisfies / violates / inconclusive |
| FC-02 | ... | — | uncovered |
```

Every FC must appear. An FC with no sources is listed with status `uncovered` — not omitted.

---

### Step 7 — Contradiction Check

Scan the source list for conflicting claims:

```
## Contradictions
Source A ([path]) and Source B ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If no contradictions exist: "No internal contradictions detected."

---

### Step 8 — Verdict

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one source by path, grounded in the FC ledger]
```

---

### Step 9 — Follow-Up Queries

At least two, each tied to an uncovered FC or evidence gap:

```
## Follow-Up Queries
1. **Query**: [what to search for] | **Where**: [directory or file pattern] | **Addresses**: FC-NN
2. ...
```

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-02: C-17 Single-Axis — Declared Schema Contract

**Axis**: Output format — the Archivist Evidence Table has a named schema contract declared before population; the contract enumerates permitted columns and prohibited columns; a post-population schema verification step checks for violations before the Analyst Section begins

**Hypothesis**: Declaring the extraction schema as a named contract (Permitted/Prohibited column lists) before the table is populated makes interpretation column insertion a visible contract breach — a rogue Relevance or Strength column does not merely violate an instruction, it violates a named schema that any reader can verify by comparing the table against the declared contract

**Expected pass on v4 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-17, C-19 | **Expected fail**: C-16 (single ledger state), C-18 (no pre-gate IN-PROGRESS with redirect agenda)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill produces output in two named sections: **Archivist** and **Analyst**. Two structural contracts enforce the separation:

1. **Schema contract**: The Archivist Evidence Table has a declared schema. Columns outside the permitted list are schema violations — they merge extraction and interpretation into one phase.
2. **Reference contract**: The Analyst Section interprets Archivist rows by number. It does not re-read source files and does not introduce new sources.

Both contracts are verifiable by inspection against the declarations below.

---

## Archivist Section

**Mandate**: Locate and record internal sources. Extraction only. No analysis, no relevance judgments, no strength labels.

### A1 — Setup

From **{{Signal}}**:

- **Hypothesis**: [one sentence]
- **Falsification Criteria**: FC-01 through FC-N (derive from hypothesis if not stated)
- **Source types to target**: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver
- **Insider definition**: what qualifies as insider for this topic (files accessible only to team members)

### A2 — Query Log

```
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N       |
| ...   | Grep | N       |
```

Run at least four distinct queries across at least two source type categories.

### A3 — Schema Contract (declared before population)

```
## Archivist Evidence Table — Schema Contract
Permitted columns: #, Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?
Prohibited columns: Relevance, Strength, Verdict, Analysis, Confidence, Assessment, Quality
Enforcement: any prohibited column appearing in the table below is a schema violation
             and must be removed before the Analyst Section begins
Rationale: prohibited columns belong to interpretation (Analyst mandate), not
           extraction (Archivist mandate); their presence in the extraction
           table merges two phases into one and defeats structural separation
```

### A4 — Archivist Evidence Table

Open each promising file. Record one row per file opened — include misses:

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | FCs Addressed | Insider? |
|---|------|-----------------|-------------|---------------|----------|
| 1 | ...  | "..."           | spec        | FC-01         | yes      |
| 2 | ...  | n/a (miss)      | —           | —             | —        |
```

**Completion condition**: At least 5 rows logged (or source exhaustion documented). All excerpts verbatim.

### A5 — Schema Verification

Before proceeding to the Analyst Section, verify the Archivist Evidence Table against the Schema Contract:

```
## Schema Verification
Columns present in table: [list them]
Any prohibited column found: yes (name it) | no
Verdict: CLEAN — no schema violations | VIOLATION — [column name] must be removed
```

If a violation is found: remove the prohibited column and re-emit the corrected table before continuing. Do not proceed with a violation present.

---

## Analyst Section

**Mandate**: Interpret the Archivist Evidence Table. Reference rows by number. Do not re-read source files. Do not introduce new sources.

### B1 — Insider Gate

Count rows where `Insider? = yes`.

```
## Insider Gate
Insider sources: [N]
Non-insider sources: [N]
```

If Insider count = 0:

```
WARNING: INSIDER GATE NOT MET

Zero insider sources found in the Archivist Evidence Table. Every cited source
could plausibly appear in public documentation. The defining advantage of
/prove:intelligence — evidence accessible only to team members — has not been
delivered.

STOP. Do not proceed to B2. Do not begin source analysis or synthesis.

Required: review the Archivist Evidence Table. Identify any row representing
internal-only knowledge:
  - Implementation decisions existing only in unpublished specs
  - Internal naming conventions absent from public documentation
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

Reclassify at least one row, state the reason, update the insider count, and
proceed.

If no row qualifies after thorough review: document that finding here.
Reclassify this run as: public-evidence-only, confidence: low. Label every
B2–B6 section header with [PUBLIC-EVIDENCE-ONLY]. Then proceed to B2.
```

If Insider count >= 1: proceed to B2.

### B2 — Source Analysis

For each non-miss row in the Archivist Evidence Table, produce an analysis block. Reference the row by number:

```
### Analysis of Row [#] — [short label]
- **Relevance**: [how the excerpt bears on the hypothesis — connect to FC-NN explicitly]
- **Strength**: strong | moderate | weak
- **FC assessment**: FC-NN [satisfies / violates / inconclusive]
```

### B3 — Falsification Ledger

```
## Falsification Ledger
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Row 1, Row 3 | satisfies |
| FC-02 | ... | — | uncovered |
```

Every FC must appear. Status: `satisfies` / `violates` / `inconclusive` / `uncovered`.

### B4 — Contradiction Check

```
## Contradictions
Row N ([path]) and Row M ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

### B5 — Follow-Up Queries

At least two, each naming: what to query, where to look, which FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

### B6 — Verdict

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph, at least one row cited by path from the Archivist Evidence Table, grounded in the FC ledger]
```

---

Write the completed artifact — Archivist Section (including Schema Contract, Schema Verification) followed by Analyst Section — to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-03: C-18 Single-Axis — Pre-Gate Redirect Agenda from IN-PROGRESS Ledger

**Axis**: Lifecycle emphasis — the IN-PROGRESS ledger is emitted at search completion before the gate fires; uncovered FCs generate a named Redirect Agenda as a first-class artifact visible at the gate decision point; the gate fires against the ledger state, not against a bare count

**Hypothesis**: Surfacing the IN-PROGRESS ledger before the gate fires converts a vague "search more" instruction into a specific FC-targeted redirect — the model sees exactly which FCs remain uncovered before deciding whether re-search is warranted; without this, coverage gaps are only discoverable after synthesis, when the opportunity for targeted re-search has passed

**Expected pass on v4 rubric**: C-09, C-10, C-11, C-13, C-14, C-16, C-18 | **Expected fail**: C-12 (in-block ordering — intentional single-axis), C-15 (in-block ordering), C-17 (no schema exclusion), C-19 (advisory gate phrasing — intentional single-axis miss)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

**Structural contract**: The falsification ledger advances through three named lifecycle states emitted at phase exit conditions. The IN-PROGRESS state is emitted at search completion — before the insider gate check executes — so coverage gaps drive a named Redirect Agenda at the decision point.

---

### Phase A — Setup

1. Write the hypothesis from **{{Signal}}** (one sentence).
2. List all FCs (FC-01 through FC-N; minimum 2, maximum 5). Derive from hypothesis if not stated.
3. State what counts as an insider source for this topic.
4. Identify internal source types to target: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.

**Phase A exit — emit DRAFT ledger immediately before beginning any search:**

```
## Falsification Ledger — DRAFT  (Phase A exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
| FC-01 | [text] | open | — | — |
| FC-02 | [text] | open | — | — |
```

All FCs begin as `open`. This is the pre-search baseline. Do not begin Phase B until this ledger is emitted.

---

### Phase B — Search and Extract

For each source type from Phase A, run Glob and Grep queries. Log each:

```
## Search Log
| Query | Tool | Results |
|-------|------|---------|
```

For each promising result, open the file and produce a source block:

```
### Source N — [short label]
- **Path**: [exact file path]
- **Excerpt**: "[verbatim passage — minimum one full sentence]"
- **Insider**: YES — [why this is not findable on the public web] | no
- **FC addressed**: FC-NN
- **Relevance**: [how this excerpt bears on the hypothesis]
- **Strength**: strong | moderate | weak
```

Search until each FC has at least one source candidate or sources are exhausted.

**Phase B exit — three required steps, in this exact order:**

**Step B-1: Emit IN-PROGRESS ledger immediately after the last source block:**

```
## Falsification Ledger — IN-PROGRESS  (Phase B exit, search complete)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status: `covered` (>=1 source found in Phase B) / `open` (no source found for this FC).

**Step B-2: Emit Redirect Agenda from IN-PROGRESS gaps:**

```
## Redirect Agenda  (from IN-PROGRESS gaps)
```

For each `open` FC in the IN-PROGRESS ledger, write one targeted re-search action:

```
- FC-NN ([description]): search [specific file path pattern or keyword] using
  [Glob | Grep] — looking for [what evidence type would address this FC]
```

If all FCs are `covered`: write "No redirect — all FCs covered at search completion."

**Step B-3: Execute or decline each redirect action:**

For each item in the Redirect Agenda, decide: run the targeted query or decline with reason.

If run: add any new sources to Phase B and update the IN-PROGRESS ledger. Re-emit it as "(Phase B exit, after redirect)" to show the updated state.

If declined: record "Redirect declined — proceeding with gap" for that item.

---

### Phase C — Insider Gate

The gate fires after the IN-PROGRESS ledger and Redirect Agenda are complete and visible. Count sources where `Insider: YES`.

```
## Insider Gate
Insider sources (Insider: YES): [N]
Non-insider sources: [N]
Open FCs at gate (from IN-PROGRESS): [FC-NN, ... | none]
Redirect items pending: [FC-NN: declined | none]
```

If count = 0:

```
WARNING: INSIDER GATE NOT MET

Zero insider sources found. Before proceeding to Phase D synthesis, return to
Phase B and re-search specifically for internal-only artifacts:
  - Implementation decisions in unpublished specs
  - Internal naming conventions absent from public docs
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

If re-search still yields zero: document here. Reclassify as
public-evidence-only, confidence: low. Proceed to Phase D with that label.
```

If count >= 1: proceed to Phase D.

---

### Phase D — Synthesis

**Contradiction Check**: identify any two sources from Phase B whose excerpts disagree on a fact:

```
## Contradictions
Source A ([path]) and Source B ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

**Follow-Up Queries** — at least two, each tied to an `open` FC from the IN-PROGRESS ledger or a weakly-evidenced FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

**Verdict**:

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one source by path, grounded in the ledger state history]
```

**Phase D exit — emit FINAL ledger immediately after the Verdict:**

```
## Falsification Ledger — FINAL  (Phase D exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status at FINAL: `satisfies` / `violates` / `inconclusive` / `uncovered`

Every FC must appear. A FC that was `open` in IN-PROGRESS and is `uncovered` in FINAL confirms the Redirect Agenda was unresolved. A FC that was `covered` in IN-PROGRESS but is `inconclusive` in FINAL indicates the evidence was present but insufficient.

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

Artifact must contain all three ledger states in order: DRAFT (Phase A exit), IN-PROGRESS with Redirect Agenda (Phase B exit), FINAL (Phase D exit).

---

## V-04: C-17 + C-18 Combined — Schema Contract + Pre-Gate Redirect Agenda

**Axes**: Output format (C-17: declared schema contract with prohibited column list) + Lifecycle emphasis (C-18: IN-PROGRESS ledger with Redirect Agenda before gate fires)

**Hypothesis**: Schema-enforced column exclusion and pre-gate coverage review reinforce each other — a clean extraction schema makes the insider count reliable (only truly-extracted rows are counted, not rows that leaked interpretation fields into the extraction block), and the Redirect Agenda derived from the IN-PROGRESS ledger converts the gate's "search more" from vague to FC-specific before synthesis begins; advisory gate phrasing is used here intentionally to isolate C-19 as the sole differentiator in V-05

**Expected pass on v4 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18 | **Expected fail**: C-19 (advisory gate phrasing — intentional miss to isolate V-05 differential)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill runs in five named phases. Each phase has a defined mandate, a declared structural contract, and a named exit condition. Do not merge phases. Do not proceed past an exit condition without emitting the required output.

---

## Phase 1: Setup

**Mandate**: Orient. Define scope. Emit the DRAFT ledger.

1. Write the hypothesis from **{{Signal}}** (one sentence).
2. List all FCs (FC-01 through FC-N; minimum 3). Derive from hypothesis if not stated in **{{Signal}}**.
3. State what counts as an insider source for this topic.
4. Identify internal source types to target: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.
5. Plan at least one Glob or Grep query per source type.

**Phase 1 exit condition — emit DRAFT ledger before beginning any search:**

```
## Falsification Ledger — DRAFT  (Phase 1 exit)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
| FC-01 | [text] | open | — |
| FC-02 | [text] | open | — |
```

All FCs begin as `open`. This captures the pre-search baseline.

---

## Phase 2: Archivist (Extraction)

**Mandate**: Locate and record internal sources. Verbatim excerpts only. No analysis. No relevance judgments. No strength labels.

**Structural contract — Schema Contract:**

```
## Archivist Evidence Table — Schema Contract
Permitted columns: #, Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?
Prohibited columns: Relevance, Strength, Verdict, Analysis, Confidence, Assessment
Enforcement: any prohibited column appearing in the table is a schema violation;
             remove it before Phase 3 begins
Rationale: interpretation fields belong to Phase 4 (Analyst); their presence
           in Phase 2 merges extraction and interpretation, defeating structural
           separation and making insider counting unreliable
```

If you find yourself writing "this suggests" or "this supports" or "this indicates" in the Archivist Evidence Table, stop — those phrases belong in Phase 4.

### 2a — Query Log

```
| Query | Tool | Results |
|-------|------|---------|
```

Run at least four distinct queries across at least two source type categories.

### 2b — Archivist Evidence Table

One row per file opened — include misses:

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | FCs Addressed | Insider? |
|---|------|-----------------|-------------|---------------|----------|
| 1 | ...  | "..."           | spec        | FC-01, FC-02  | yes      |
| 2 | ...  | n/a (miss)      | —           | —             | —        |
```

### 2c — Schema Verification

```
## Schema Verification (Phase 2 exit check)
Columns in table: [list them]
Prohibited column found: yes ([name]) | no
Schema status: CLEAN | VIOLATION — [corrective action taken]
```

Correct any violation before proceeding.

**Phase 2 exit condition — three steps, in order:**

**Step 2-E1: Emit IN-PROGRESS ledger after the last row is added and schema is verified clean:**

```
## Falsification Ledger — IN-PROGRESS  (Phase 2 exit, search complete)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
```

Status: `covered` (at least one row addresses this FC) / `open` (no row found for this FC).

**Step 2-E2: Emit Redirect Agenda from IN-PROGRESS gaps:**

```
## Redirect Agenda  (from IN-PROGRESS gaps)
```

For each `open` FC:

```
- FC-NN ([description]): search [specific path pattern or keyword] using
  [Glob | Grep] — looking for [what evidence type would address this FC]
```

If all FCs covered: "No redirect — all FCs covered at search completion."

**Step 2-E3: Execute or decline each redirect action:**

For each Redirect Agenda item: run the query or record "Redirect declined — proceeding with gap." If run and successful, add rows to the Archivist Evidence Table and re-emit the IN-PROGRESS ledger as "(after redirect)" to show the updated state.

---

## Phase 3: Insider Gate

**Mandate**: Count insider sources. Produce gate verdict. Gate fires against the IN-PROGRESS ledger state.

Count rows where `Insider? = yes`.

```
## Insider Gate
Insider sources (Insider? = yes): [N]
Non-insider sources: [N]
Open FCs at gate (from IN-PROGRESS ledger): [FC-NN, ... | none]
```

If Insider count = 0:

```
WARNING: INSIDER GATE NOT MET

Phase 2 found zero insider sources. Every cited source could plausibly appear
in public documentation. The defining capability of /prove:intelligence —
evidence accessible only to team members — has not been delivered.

Before proceeding to Phase 4 (Analyst), return to Phase 2 and re-search
specifically for internal-only artifacts:
  - Implementation decisions in unpublished specs
  - Internal naming conventions not reflected in any public doc
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

If exhaustive re-search still yields zero insider sources:
  1. Document that finding here explicitly.
  2. Reclassify this run as: public-evidence-only, confidence: low.
  3. Label every Phase 4 and Phase 5 section header with [PUBLIC-EVIDENCE-ONLY].
  4. Proceed to Phase 4.
```

If Insider count >= 1: proceed to Phase 4.

**Phase 3 exit condition**: Insider count >= 1 (PASS), or WARNING emitted and run explicitly reclassified (RECLASSIFIED).

---

## Phase 4: Analyst (Interpretation)

**Mandate**: Interpret the Archivist Evidence Table. Reference rows by number. Do not re-read source files. Do not introduce new sources.

### 4a — Source Analysis

For each non-miss row:

```
### Analysis of Row [#]
- **Path**: [from table row #]
- **Excerpt ref**: row # — "[first few words of excerpt]..."
- **Relevance**: [how the excerpt bears on the hypothesis — connect to FC-NN explicitly]
- **Strength**: strong | moderate | weak
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

### 4b — Contradiction Check

```
## Contradictions
Row N ([path]) and Row M ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

### 4c — Follow-Up Queries

At least two, each tied to an `open` FC from the IN-PROGRESS ledger or a weakly-evidenced FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

**Phase 4 exit condition**: all non-miss rows analyzed, contradictions assessed, follow-up queries written.

---

## Phase 5: Synthesis

**Mandate**: Write the verdict. Close the ledger. Trace FC evolution from DRAFT to FINAL.

Write 2–4 paragraphs covering:
- What the internal evidence says collectively about the hypothesis
- How FC coverage evolved: compare DRAFT → IN-PROGRESS → FINAL
- Remaining gaps and which follow-up queries address them
- Overall finding: `confirmed` / `refuted` / `inconclusive`

**Phase 5 exit condition — emit FINAL ledger and Verdict:**

```
## Falsification Ledger — FINAL  (Phase 5 exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status: `satisfies` / `violates` / `inconclusive` / `uncovered`

A FC that was `covered` in IN-PROGRESS but becomes `inconclusive` in FINAL indicates evidence was present but insufficient. A FC that was `open` in IN-PROGRESS and is `uncovered` in FINAL confirms the Redirect Agenda gap was not resolved.

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one row by path from the Archivist Evidence Table, grounded in the FINAL ledger]
```

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

Artifact structure in order:
1. Hypothesis + FC list
2. `## Falsification Ledger — DRAFT` (Phase 1 exit)
3. Schema Contract declaration (Phase 2 opening)
4. `## Archivist Evidence Table` with Query Log (Phase 2)
5. `## Schema Verification` (Phase 2 exit check)
6. `## Falsification Ledger — IN-PROGRESS` + `## Redirect Agenda` (Phase 2 exit)
7. `## Insider Gate` (Phase 3)
8. Source Analysis + Contradictions + Follow-Up Queries (Phase 4)
9. Synthesis paragraphs + `## Falsification Ledger — FINAL` + `## Verdict` (Phase 5)

---

## V-05: C-17 + C-18 + C-19 Combined — Full R4 Aspirational Suite

**Axes**: Output format (C-17: declared schema contract) + Lifecycle emphasis (C-18: pre-gate IN-PROGRESS with Redirect Agenda) + Phrasing register (C-19: halt semantics in gate WARNING)

**Hypothesis**: The three mechanisms form a dependency chain: schema exclusion (C-17) makes extraction columns structurally clean so insider counting is reliable; the pre-gate IN-PROGRESS Redirect Agenda (C-18) converts vague "search more" to FC-specific re-search before the gate decision; halt semantics (C-19) ensures the gate cannot be satisfied by a nominal re-search attempt without explicit Option A or Option B resolution — together they close the three gaps left open by C-15, C-16, and C-14 respectively

**Expected pass on v4 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19 — all eleven aspirationals

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill runs in five named phases. Each phase has a defined mandate, a declared structural contract, and a named exit condition. Do not merge phases. Do not proceed past an exit condition without emitting the required output.

---

## Phase 1: Setup

**Mandate**: Orient. Define scope. Emit the DRAFT ledger.

1. Write the hypothesis from **{{Signal}}** (one sentence).
2. List all FCs (FC-01 through FC-N; minimum 3). Derive from hypothesis if not stated in **{{Signal}}**.
3. State what counts as an insider source for this topic.
4. Identify internal source types to target: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.
5. Plan at least one Glob or Grep query per source type.

**Phase 1 exit condition — emit DRAFT ledger before beginning any search:**

```
## Falsification Ledger — DRAFT  (Phase 1 exit)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
| FC-01 | [text] | open | — |
| FC-02 | [text] | open | — |
```

All FCs begin as `open`. This captures the pre-search baseline. Do not begin Phase 2 until this ledger is emitted.

---

## Phase 2: Archivist (Extraction)

**Mandate**: Locate and record internal sources. Verbatim excerpts only. No analysis. No relevance judgments. No strength labels.

**Structural contract — Schema Contract (declared before table population):**

```
## Archivist Evidence Table — Schema Contract
Permitted columns: #, Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?
Prohibited columns: Relevance, Strength, Verdict, Analysis, Confidence, Assessment
Schema violation: any prohibited column appearing in the table below
Corrective action: remove the column before Phase 3 begins and record the
                  correction in the Schema Verification section
Rationale: interpretation fields belong to Phase 4 (Analyst); their presence
           here merges extraction and interpretation, making insider counting
           unreliable and defeating structural separation
```

If you find yourself writing "this suggests", "this supports", "this indicates", or "this demonstrates" anywhere in the Archivist Evidence Table, stop — those phrases belong in Phase 4.

### 2a — Query Log

```
| Query | Tool | Results |
|-------|------|---------|
```

Run at least four distinct queries across at least two source type categories.

### 2b — Archivist Evidence Table

One row per file opened — include misses:

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | FCs Addressed | Insider? |
|---|------|-----------------|-------------|---------------|----------|
| 1 | ...  | "..."           | spec        | FC-01, FC-02  | yes      |
| 2 | ...  | n/a (miss)      | —           | —             | —        |
```

`Insider?` is a factual field: does this file exist only inside the repo, inaccessible via public web search or public documentation? `yes` / `no`. It is not an interpretation field.

### 2c — Schema Verification

```
## Schema Verification  (Phase 2 exit check)
Columns in table: [list them]
Prohibited column found: yes ([name]) | no
Schema status: CLEAN | VIOLATION — [corrective action taken]
```

Correct any violation before emitting the IN-PROGRESS ledger.

**Phase 2 exit condition — four steps, in this exact order:**

**Step 2-E1: Confirm Schema Verification = CLEAN.**

**Step 2-E2: Emit IN-PROGRESS ledger after schema is clean:**

```
## Falsification Ledger — IN-PROGRESS  (Phase 2 exit, search complete)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
```

Status: `covered` (at least one row addresses this FC) / `open` (no row found for this FC).

**Step 2-E3: Emit Redirect Agenda from IN-PROGRESS gaps:**

```
## Redirect Agenda  (from IN-PROGRESS gaps)
```

For each `open` FC in the IN-PROGRESS ledger, write one targeted re-search action:

```
- FC-NN ([description]): search [specific path pattern or keyword] using
  [Glob | Grep] — looking for [what evidence type would satisfy this FC]
```

If all FCs covered: "No redirect — all FCs covered at Phase 2 exit."

**Step 2-E4: Execute or decline each Redirect Agenda item:**

For each item: run the targeted query or record "Redirect declined — reason: [reason]." If run and successful, add rows to the Archivist Evidence Table, re-verify the schema, and re-emit the IN-PROGRESS ledger as "(Phase 2 exit, after redirect)" showing the updated state.

The IN-PROGRESS ledger and Redirect Agenda must be visible before Phase 3 begins. Phase 3 fires against this state.

---

## Phase 3: Insider Gate

**Mandate**: Count insider sources. Emit gate verdict. Fire WARNING with halt semantics if count = 0.

Count rows in the Archivist Evidence Table where `Insider? = yes`.

```
## Insider Gate
Insider sources (Insider? = yes): [N]
Non-insider sources: [N]
Open FCs at gate (from IN-PROGRESS ledger): [FC-NN, ... | none]
Redirect items pending (declined or unresolved): [FC-NN, ... | none]
```

**If Insider count = 0:**

The following block uses halt semantics. "STOP." is the halt token — it is not interchangeable with "Note:", "Warning:", or "Before proceeding:". Advisory phrasing ("before proceeding to synthesis, re-search for insider sources") permits implicit continuation after a nominal attempt. Halt semantics require explicit resolution: Option A or Option B must be completed before Phase 4 begins. There is no implicit continuation path.

Emit the following block verbatim:

```
WARNING: INSIDER GATE NOT MET

Phase 2 found zero insider sources. Every cited source could plausibly appear
in public documentation. The defining capability of /prove:intelligence —
evidence accessible only to team members — has not been delivered.

STOP. Do not proceed to Phase 4 (Analyst). Do not begin interpretation.
Do not write synthesis, contradiction checks, or follow-up queries.

Explicit resolution required — complete one of:

  Option A — Targeted re-search:
    Return to Phase 2. Search specifically for internal-only artifacts:
    - Implementation decisions in unpublished specs
    - Internal naming conventions not reflected in any public doc
    - Scenario outcomes from unreleased test runs
    - In-progress work not yet merged or shipped
    Add new rows to the Archivist Evidence Table. Re-verify schema. Re-emit
    the IN-PROGRESS ledger. If Insider count >= 1 after re-search: update this
    gate to PASS and proceed to Phase 4.

  Option B — Reclassify:
    If exhaustive re-search yields zero insider sources: document that finding
    here with the exact text: "Reclassification: public-evidence-only,
    confidence: low." Label every Phase 4 and Phase 5 section header with
    [PUBLIC-EVIDENCE-ONLY]. Then proceed to Phase 4.

There is no implicit continuation path. Proceeding without completing Option A
or Option B is a protocol violation.
```

**If Insider count >= 1:** proceed to Phase 4.

**Phase 3 exit condition**: Insider count >= 1 (PASS), or WARNING emitted and run explicitly reclassified via Option B (RECLASSIFIED).

---

## Phase 4: Analyst (Interpretation)

**Mandate**: Interpret the Archivist Evidence Table. Reference rows by number. Do not re-read source files. Do not introduce new sources.

### 4a — Source Analysis

For each non-miss row in the Archivist Evidence Table:

```
### Analysis of Row [#]
- **Path**: [from table row #]
- **Excerpt ref**: row # — "[first few words of excerpt]..."
- **Relevance**: [how the excerpt bears on the hypothesis — connect to FC-NN explicitly, not just the file topic]
- **Strength**: strong | moderate | weak
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

### 4b — Contradiction Check

```
## Contradictions
Row N ([path]) and Row M ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

### 4c — Follow-Up Queries

At least two, each tied to an `open` FC from the IN-PROGRESS ledger or a weakly-evidenced FC in Phase 4 analysis:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

**Phase 4 exit condition**: all non-miss rows analyzed, contradictions assessed, at least two follow-up queries written.

---

## Phase 5: Synthesis

**Mandate**: Write the verdict. Close the ledger. Trace FC evolution across all three ledger states.

Write 2–4 paragraphs covering:
- What the internal evidence says collectively about the hypothesis
- How FC coverage evolved: DRAFT (all open) → IN-PROGRESS (covered/open) → FINAL (satisfies/violates/inconclusive/uncovered)
- Remaining gaps and which follow-up queries address them
- Overall finding: `confirmed` / `refuted` / `inconclusive`

**Phase 5 exit condition — emit FINAL ledger and Verdict:**

```
## Falsification Ledger — FINAL  (Phase 5 exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status: `satisfies` / `violates` / `inconclusive` / `uncovered`

Every FC must appear. Traceability checks:
- FC that was `covered` in IN-PROGRESS but is `inconclusive` in FINAL: evidence was present but insufficient for a verdict
- FC that was `open` in IN-PROGRESS and is `uncovered` in FINAL: Redirect Agenda gap was unresolved

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one row by path from the Archivist Evidence Table, grounded in the FINAL ledger]
```

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

Artifact structure in order:
1. Hypothesis + FC list
2. `## Falsification Ledger — DRAFT` (Phase 1 exit)
3. Schema Contract declaration (Phase 2 opening)
4. Query Log + `## Archivist Evidence Table` (Phase 2)
5. `## Schema Verification` (Phase 2 exit check)
6. `## Falsification Ledger — IN-PROGRESS` + `## Redirect Agenda` (Phase 2 exit)
7. `## Insider Gate` with halt-semantics WARNING if triggered (Phase 3)
8. Source Analysis blocks + `## Contradictions` + `## Follow-Up Queries` (Phase 4)
9. Synthesis paragraphs + `## Falsification Ledger — FINAL` + `## Verdict` (Phase 5)
