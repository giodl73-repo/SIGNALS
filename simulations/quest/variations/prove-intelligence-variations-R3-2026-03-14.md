**prove-intelligence R3 variations written** to `simulations/quest/variations/prove-intelligence-variations-R3-2026-03-14.md`.

---

## Summary

| ID | Axis | Targets | Key Move | Expected Score |
|----|------|---------|----------|----------------|
| **V-01** | Phrasing register | C-14 | `WARNING: INSIDER GATE NOT MET` + `STOP. Do not proceed` as a named structural section with unconditional gate status (PASS/BLOCKED); not a conditional inline note | ~98.75 (fails C-15, C-16) |
| **V-02** | Output format | C-15 | Archivist Evidence Table schema physically lacks Relevance/Strength/FC columns; Analyst blocks reference rows by number only; in-block ordering is impossible by schema, not by instruction | ~98.75 (fails C-16) |
| **V-03** | Lifecycle emphasis | C-16 | Ledger advances DRAFT (Phase A exit) → IN-PROGRESS (Phase B exit, search complete) → FINAL (Phase D exit); transitions are phase-gated not per-source; IN-PROGRESS state surfaces gaps before synthesis begins | ~97.5 (fails C-15 — intentional) |
| **V-04** | Role sequence + blocking gate | C-14 + C-15 | WARNING gate is the physical role boundary between Archivist and Analyst — model must traverse the gate section to advance from extraction to interpretation; gate cannot be skipped without skipping the role transition | ~98.75 (fails C-16) |
| **V-05** | All three combined | C-14 + C-15 + C-16 | Five phases with enforced exit conditions; each mechanism feeds the next — extraction-first (C-15) makes insider counting reliable for the gate (C-14), and IN-PROGRESS ledger at search completion (C-16) gives the model a concrete FC gap list before the gate fires | 100 (all 8 aspirationals) |

**What's new vs. R2:**
- **C-14**: V-01 R2 had the WARNING text but used a soft "before proceeding: re-search" framing. R3 V-01 adds explicit `STOP. Do not proceed to Step 6.` halt semantics and a named `Gate status: PASS | BLOCKED` field.
- **C-15**: V-04/V-05 R2 had Archivist/Analyst roles but Analyst source blocks still repeated the excerpt alongside interpretation (in-block co-location). R3 V-02/V-04/V-05 move the excerpt to the Archivist table and make Analyst blocks reference-only — structural gap is enforced by schema, not by instruction.
- **C-16**: V-05 R2 updated the ledger after each source (per-source granularity). R3 V-03/V-05 tie state transitions to named phase exits: DRAFT at Phase 1, IN-PROGRESS at Phase 2 (search complete), FINAL at Phase 5 — the IN-PROGRESS state at search completion is the key new lever, visible before the gate fires.
nalyst source blocks still repeated the excerpt alongside interpretation (in-block ordering). R3 variations close those two specific gaps.

---

## V-01: C-14 Single-Axis — HALT-Semantics WARNING Block

**Axis**: Phrasing register — the insider gate is a named structural section that emits verbatim blocking text with an explicit HALT instruction
**Hypothesis**: A WARNING block that says `STOP. Do not proceed.` is more effective at preventing silent failure than one that says `before proceeding: re-search`; the difference is between a conditional instruction (easily skipped) and a halt instruction (requires explicit resolution)
**Expected pass on v3 rubric**: C-09, C-10, C-11, C-12, C-13, C-14 | **Expected fail**: C-15 (source assessment blocks use in-block ordering), C-16 (single ledger state)

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

This section is required for every run. It either passes or fires. There is no third option.

```
## Insider Gate
Sources with Insider: YES — [count]
Sources with Insider: no  — [count]
Gate status: PASS (count >= 1) | BLOCKED (count = 0)
```

**If Gate status = BLOCKED, emit the following block verbatim. Do not skip it. Do not abbreviate it.**

```
WARNING: INSIDER GATE NOT MET

This run has produced zero insider-flagged sources. Every cited source could
plausibly appear in public documentation. The defining value of
/prove:intelligence — evidence accessible only to team members — has not been
delivered.

STOP. Do not proceed to Step 6. Do not write a verdict. Do not write synthesis.

To unblock: return to Step 2. Re-search for internal-only artifacts:
  - Implementation decisions in unpublished specs
  - Internal naming conventions not reflected in any public doc
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

If exhaustive re-search still yields zero insider sources:
  1. Document that finding here explicitly.
  2. Reclassify this run as: public-evidence-only, confidence: low.
  3. Only then proceed to Step 6, with that reclassification labeled on every
     output section.
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

## V-02: C-15 Single-Axis — Table-Enforced Role Isolation

**Axis**: Output format — the Archivist output is a table whose column schema physically excludes interpretation fields; the table structure makes in-block ordering impossible rather than merely discouraged
**Hypothesis**: Formatting the Archivist output as a six-column table (Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?) makes C-15 structurally enforced rather than prompt-enforced — the model cannot add a "Relevance" column without visibly violating the declared schema
**Expected pass on v3 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15 | **Expected fail**: C-16 (single ledger state)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill produces output in two named sections. **The Archivist Section uses a fixed table schema that contains only extraction fields — no interpretation columns exist in it.** The Analyst Section interprets Archivist rows by reference — it may not re-read source files or introduce new sources. If you find an interpretation field appearing in the Archivist Section, or new sources appearing in the Analyst Section, stop and correct the structural violation before continuing.

---

## Archivist Section

**Mandate**: Locate and record internal sources. Extraction only. No analysis, no relevance judgments, no strength labels.

### A1 — Setup

From **{{Signal}}**, write:

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

### A3 — Archivist Evidence Table

Open each promising file. Record one row per file opened — include misses.

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | FCs Addressed | Insider? |
|---|------|-----------------|-------------|---------------|----------|
| 1 | ...  | "..."           | spec        | FC-01         | yes      |
| 2 | ...  | n/a (miss)      | —           | —             | —        |
```

**Schema constraint**: These six columns are the complete schema. Do not add Relevance, Strength, or FC Status columns. The Analyst Section owns those fields. Violating the schema merges two phases into one — structural failure.

**Archivist completion condition**: At least 5 rows logged (or source exhaustion documented). All excerpts verbatim. No analysis written anywhere in this section.

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

Zero insider sources found. Do not proceed to source analysis or synthesis.

Review the Archivist Evidence Table. Identify any row representing internal-only
knowledge (implementation decisions, internal conventions, unreleased outcomes,
in-progress work). Reclassify it as Insider: yes and state the reason.

If no row qualifies: document here and proceed with confidence: low, labeling
every subsequent section as public-evidence-only.
```

If Insider count >= 1: proceed.

### B2 — Source Analysis

For each non-miss row in the Archivist Evidence Table, produce an analysis block. Reference the row by number — do not re-excerpt from the file:

```
### Analysis of Row [#] — [short label]
- **Relevance**: [how the excerpt bears on the hypothesis — connect to FC-NN explicitly, not just the file topic]
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

Identify any pair of rows whose excerpts disagree on a fact:

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

Write the completed artifact — Archivist Section followed by Analyst Section — to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-03: C-16 Single-Axis — Phase-Exit Ledger Lifecycle

**Axis**: Lifecycle emphasis — the falsification ledger advances through three named states emitted at phase exit conditions; ledger state transitions are phase-gated, not per-source
**Hypothesis**: Tying ledger state transitions to named phase exits rather than per-source updates produces more meaningful intermediate states — the IN-PROGRESS state at search completion shows which FCs still have no evidence, giving the model an opportunity to redirect search before synthesis begins
**Expected pass on v3 rubric**: C-09, C-10, C-11, C-13, C-14, C-16 | **Expected fail**: C-15 (source assessment blocks use in-block ordering — intentional single-axis constraint)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

**Structural contract**: The falsification ledger is a living artifact that advances through three named lifecycle states, each emitted at a named phase exit. The three states are: DRAFT (before search), IN-PROGRESS (at search completion), FINAL (at synthesis). Each state is emitted at the specified point — not earlier, not later.

---

### Phase A — Setup

1. Write the hypothesis from **{{Signal}}** (one sentence).
2. List all FCs (FC-01 through FC-N; derive from hypothesis if not stated).
3. State what counts as an insider source for this topic.
4. Identify internal source types to target: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.

**Phase A exit — emit DRAFT state immediately before beginning any search:**

```
## Falsification Ledger — State: DRAFT  (Phase A exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
| FC-01 | [text] | open | — | — |
| FC-02 | [text] | open | — | — |
```

All FCs begin as `open`. This is the pre-search baseline. Emit before proceeding.

---

### Phase B — Search and Extract

For each source type identified in Phase A, run Glob and Grep queries. Log each query and result count. Open every promising file. For each source found:

```
### Source N — [short label]
- **Path**: [exact file path]
- **Excerpt**: "[verbatim passage — minimum one full sentence]"
- **Insider**: YES — [why this is not findable on the public web] | no
- **FC addressed**: FC-NN
- **Relevance**: [how this excerpt bears on the hypothesis]
- **Strength**: strong | moderate | weak
```

Search until every FC has at least one source or internal sources are exhausted.

**Phase B exit — emit IN-PROGRESS state immediately after the last Source N block:**

```
## Falsification Ledger — State: IN-PROGRESS  (Phase B exit, search complete)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status at IN-PROGRESS: `covered` (>=1 source found in Phase B) / `open` (no source found).

**Review the IN-PROGRESS state before proceeding**: any FC still `open` is a search gap visible now, before synthesis. Decide here — before synthesis — whether a targeted re-search is warranted. If yes, run it and update the IN-PROGRESS state. If no, accept the gap and proceed.

---

### Phase C — Insider Gate

Count sources from Phase B where `Insider: YES`.

```
## Insider Gate
Insider sources (Insider: YES): [N]
Non-insider sources: [N]
```

If count = 0:

```
WARNING: INSIDER GATE NOT MET

Zero insider sources found. Do not proceed to Phase D synthesis.

Return to Phase B and re-search for internal-only artifacts: implementation
decisions, internal naming conventions, unreleased scenario outcomes,
in-progress work not yet merged. If none exist, document here and proceed
with confidence: low.
```

If count >= 1: proceed to Phase D.

---

### Phase D — Synthesis

**Contradiction Check**: Identify any two sources from Phase B that disagree on a fact:

```
## Contradictions
Source A ([path]) and Source B ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

**Follow-Up Queries**: At least two, each targeting an `open` FC from the IN-PROGRESS state or a weakly-evidenced FC:

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
**Basis**: [one paragraph citing at least one source by path, grounded in the ledger states]
```

**Phase D exit — emit FINAL state immediately after the Verdict:**

```
## Falsification Ledger — State: FINAL  (Phase D exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status at FINAL: `satisfies` / `violates` / `inconclusive` / `uncovered`

Every FC must appear. Compare to IN-PROGRESS: any `covered` FC that becomes `inconclusive` in FINAL indicates the evidence was weaker than its mere presence suggested.

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

The artifact must contain all three ledger states in sequence: DRAFT (Phase A exit), IN-PROGRESS (Phase B exit), FINAL (Phase D exit).

---

## V-04: C-14 + C-15 Combined — Gate as Role Boundary

**Axes**: Blocking WARNING text (C-14) + named role isolation (C-15) — the WARNING gate is the structural boundary between the Archivist and Analyst named roles
**Hypothesis**: Placing the WARNING gate between two named roles makes it a structural gate rather than a conditional instruction — the model must emit the gate section to proceed from the Archivist role to the Analyst role; it cannot skip the gate without skipping the entire role transition
**Expected pass on v3 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15 | **Expected fail**: C-16 (single ledger state)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill has three sections in strict sequence: **Archivist -> Role Transition Gate -> Analyst**. Complete each section fully before starting the next. The Gate lives between the two roles — it is not optional, it does not have a fast path, and it cannot be acknowledged with a single sentence.

---

## Archivist

**Mandate**: Evidence collection only. No interpretation, no relevance judgments, no strength labels, no insider classification. Every evaluation field belongs to the Analyst. If you find yourself writing what something means, stop — that belongs in the Analyst section.

### 1 — Setup

From **{{Signal}}**:

- **Hypothesis**: [one sentence]
- **FCs**: FC-01 through FC-N
- **Insider definition**: what qualifies as insider for this topic
- **Source types to target**: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver

### 2 — Query Log

```
| Query | Tool | Results |
|-------|------|---------|
```

Run at least four distinct queries across at least two source type categories.

### 3 — Archivist Evidence Table

Open each promising file. Record verbatim excerpts. Include misses.

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | Insider? |
|---|------|-----------------|-------------|----------|
| 1 | ...  | "..."           | spec        | yes / no |
| 2 | ...  | n/a (miss)      | —           | —        |
```

**Archivist constraint**: The five columns above are the complete schema. `Insider?` is the only evaluation field because it is factual (does this file exist only inside the repo?), not interpretive. Relevance, Strength, and FC Status belong to the Analyst.

**Archivist completion condition**: At least 5 rows logged (or source exhaustion documented), all excerpts verbatim, no analysis written.

---

## Role Transition Gate

Count rows where `Insider? = yes`.

```
## Role Transition Gate
Insider sources (Insider? = yes): [N]
Non-insider sources: [N]
```

**If Insider count = 0, emit the following block in full. Do not skip it. Do not abbreviate it. The Analyst section cannot begin until this block is fully emitted and resolved.**

```
WARNING: INSIDER GATE NOT MET

The Archivist found zero insider sources — files accessible only to team
members and not findable via web search or public documentation.

STOP. The Analyst role cannot proceed.

Required action: review the Archivist Evidence Table. Identify any row that
represents internal-only knowledge:
  - Implementation decisions that exist only in unpublished specs
  - Internal naming conventions not reflected in any public doc
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

Reclassify at least one row as Insider: yes and state the reason explicitly.

If no row qualifies after thorough review: document that finding here,
reclassify this run as public-evidence-only with confidence: low, and label
every Analyst output section with that classification before proceeding.
```

**If Insider count >= 1, emit:**

```
## Role Transition Gate
Gate status: PASS — [N] insider source(s) found. Proceeding to Analyst.
```

---

## Analyst

**Mandate**: Interpret the Archivist Evidence Table. Reference rows by number. Do not re-read source files. Do not introduce new sources. Your job is relevance, strength, FC mapping, contradiction check, verdict, and follow-up queries.

### 4 — Source Analysis

For each non-miss row in the Archivist Evidence Table:

```
### Analysis of Row [#]
- **Path**: [from table row #]
- **Excerpt**: "[from table row # — reference the table, do not re-read the file]"
- **Relevance**: [how the excerpt bears on the hypothesis — connect to FC-NN explicitly]
- **Strength**: strong | moderate | weak
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

### 5 — Falsification Ledger

```
## Falsification Ledger
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Row 1, Row 3 | satisfies |
| FC-02 | ... | — | uncovered |
```

Every FC must appear. Status: `satisfies` / `violates` / `inconclusive` / `uncovered`.

### 6 — Contradiction Check

```
## Contradictions
Row N ([path]) and Row M ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

### 7 — Follow-Up Queries

At least two, each naming: what to query, where to look, which FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

### 8 — Verdict

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph, at least one row cited by path, grounded in the FC ledger]
```

---

Write the completed artifact — Archivist, then Role Transition Gate, then Analyst — to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-05: C-14 + C-15 + C-16 Combined — Full R3 Aspirational Suite

**Axes**: Blocking WARNING text (C-14) + named phase isolation (C-15) + phase-exit ledger lifecycle (C-16)
**Hypothesis**: The three mechanisms reinforce each other: extraction-first (C-15) makes insider counting accurate (enabling reliable C-14 gate), and the IN-PROGRESS ledger at search completion (C-16) surfaces coverage gaps before the gate fires — giving the model a concrete agenda for targeted re-search rather than a vague "search more" instruction
**Expected pass on v3 rubric**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16 — all eight aspirationals

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill runs in five named phases. Each phase has a defined mandate, a constrained field schema, and a named exit condition. Do not merge phases. Do not proceed past an exit condition without emitting the required output.

---

## Phase 1: Setup

**Mandate**: Orient. Define scope. Emit the DRAFT ledger.

1. Write the hypothesis from **{{Signal}}** (one sentence).
2. List all FCs (FC-01 through FC-N; minimum 3, maximum 5). Derive from hypothesis if not stated in **{{Signal}}**.
3. State what counts as an insider source for this topic.
4. Identify internal source types to target: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.
5. Plan at least one Glob or Grep query per source type.

**Phase 1 exit condition: emit DRAFT ledger before beginning any search.**

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

**Permitted fields in this phase**: Path, Verbatim Excerpt, Source Type, FCs Addressed (factual topic mapping — not an assessment of whether it satisfies), Insider? (factual: is this file accessible only internally?).

If you find yourself writing "this suggests" or "this indicates" or "this supports", stop. Those phrases belong in Phase 4.

### 2a — Query Log

```
| Query | Tool | Results |
|-------|------|---------|
```

### 2b — Archivist Evidence Table

One row per file opened — include misses:

```
## Archivist Evidence Table
| # | Path | Verbatim Excerpt | Source Type | FCs Addressed | Insider? |
|---|------|-----------------|-------------|---------------|----------|
| 1 | ...  | "..."           | spec        | FC-01, FC-02  | yes      |
| 2 | ...  | n/a (miss)      | —           | —             | —        |
```

**Schema constraint**: Six columns only. Relevance, Strength, and FC Status are absent from this table by design. They belong to Phase 4.

**Phase 2 exit condition: emit IN-PROGRESS ledger at search completion — after the last row is added to the Archivist Evidence Table.**

```
## Falsification Ledger — IN-PROGRESS  (Phase 2 exit, search complete)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
```

Status at IN-PROGRESS: `covered` (at least one row addresses this FC) / `open` (no row found for this FC).

**Review the IN-PROGRESS state before proceeding**: any `open` FC is a search gap visible now, before synthesis. If warranted, run one targeted re-search query for that FC and add the result to the Archivist Evidence Table before emitting the final IN-PROGRESS state.

---

## Phase 3: Insider Gate

**Mandate**: Count insider sources. Fire WARNING if zero.

Count rows in the Archivist Evidence Table where `Insider? = yes`.

```
## Insider Gate
Insider sources (Insider? = yes): [N]
Non-insider sources: [N]
```

**If Insider count = 0, emit the following block in full. Do not abbreviate it. Phase 4 cannot begin until this block is emitted and resolved.**

```
WARNING: INSIDER GATE NOT MET

Phase 2 found zero insider sources. Every cited source could plausibly appear
in public documentation. The defining capability of /prove:intelligence —
evidence accessible only to team members — has not been delivered.

STOP. Phase 4 (Analyst) cannot proceed.

To resolve: return to Phase 2. Re-search for internal-only artifacts:
  - Implementation decisions in unpublished specs
  - Internal naming conventions not reflected in any public doc
  - Scenario outcomes from unreleased test runs
  - In-progress work not yet merged or shipped

If exhaustive re-search still yields zero insider sources:
  1. Document that finding here.
  2. Reclassify this run as: public-evidence-only, confidence: low.
  3. Label every Phase 4 and Phase 5 output section with that classification.
  4. Proceed to Phase 4.
```

**If Insider count >= 1:** proceed to Phase 4.

**Phase 3 exit condition**: Insider count >= 1 (PASS), or WARNING block emitted and run explicitly reclassified (RECLASSIFIED).

---

## Phase 4: Analyst (Interpretation)

**Mandate**: Interpret the Archivist Evidence Table. Reference rows by number. Do not re-read source files. Do not introduce new sources.

### 4a — Source Analysis

For each non-miss row in the Archivist Evidence Table:

```
### Analysis of Row [#]
- **Path**: [from table row #]
- **Excerpt**: "[from table row # — reference the table, do not re-read the file]"
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

At least two, each tied to an `open` FC from the IN-PROGRESS ledger or a weakly-evidenced FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

**Phase 4 exit condition**: all Archivist rows analyzed, contradictions assessed, follow-up queries written.

---

## Phase 5: Synthesis

**Mandate**: Write the verdict. Close the ledger.

Write 2-4 paragraphs:
- What the internal evidence says collectively about the hypothesis
- How the FC coverage evolved: compare DRAFT -> IN-PROGRESS -> FINAL
- Remaining gaps, and which follow-up queries address them
- Overall verdict: `supported` / `refuted` / `inconclusive`

**Phase 5 exit condition: emit FINAL ledger and Verdict section.**

```
## Falsification Ledger — FINAL  (Phase 5 exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status at FINAL: `satisfies` / `violates` / `inconclusive` / `uncovered`

Every FC must appear. A FC that was `covered` in IN-PROGRESS but becomes `inconclusive` in FINAL indicates evidence was present but insufficient. A FC that was `open` in IN-PROGRESS and is `uncovered` in FINAL confirms the search gap was not resolved.

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
3. `## Archivist Evidence Table` with Query Log (Phase 2)
4. `## Falsification Ledger — IN-PROGRESS` (Phase 2 exit)
5. `## Insider Gate` (Phase 3)
6. Source Analysis blocks + Contradictions + Follow-Up Queries (Phase 4)
7. Synthesis paragraphs + `## Falsification Ledger — FINAL` + `## Verdict` (Phase 5)
