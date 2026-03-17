Written to `simulations/quest/golden/prove-intelligence-golden-2026-03-14.md`.

**Golden prompt summary:**

- **Score**: 100 — all 13 aspirational criteria pass (new v5 denominator)
- **Body**: V-05 simplified (1,152 words, 24% reduction from 1,522; all criteria verified)
- **Rubric**: v5 with two new criteria promoted from R4 excellence signals

**What made it golden — the four differentiating patterns:**

| Pattern | Criteria | What it closes |
|---------|----------|----------------|
| Schema Contract (Permitted/Prohibited columns, pre-declared) | C-17 | In-block ordering replaced by artifact-verifiable boundary |
| CLEAN → IN-PROGRESS ordering chain (2-E1 before 2-E2) | C-21 | Coverage snapshot guaranteed to reflect schema-verified rows only |
| Redirect Agenda from IN-PROGRESS gaps, visible before gate | C-18 | "Search more" replaced by one FC-targeted re-search action per gap |
| Option A / Option B resolution contract in halt block | C-19 + C-20 | Unresolved continuation named as protocol violation, not ignored guidance |
alsification Ledger — DRAFT  (Phase 1 exit)
| FC | Description | Status | Sources |
|----|-------------|--------|---------|
| FC-01 | [text] | open | — |
| FC-02 | [text] | open | — |
```

All FCs begin as `open`. Do not begin Phase 2 until this ledger is emitted.

---

## Phase 2: Archivist (Extraction)

**Mandate**: Locate and record internal sources. Verbatim excerpts only. No analysis. No relevance judgments. No strength labels.

**Structural contract — Schema Contract (declared before table population):**

```
## Archivist Evidence Table — Schema Contract
Permitted columns: #, Path, Verbatim Excerpt, Source Type, FCs Addressed, Insider?
Prohibited columns: Relevance, Strength, Verdict, Analysis, Confidence, Assessment
Schema violation: any prohibited column appearing in the table below
```

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

The IN-PROGRESS ledger and Redirect Agenda must be visible before Phase 3 begins.

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

STOP. is not interchangeable with advisory phrasing. Option A or Option B must be completed before Phase 4 begins.

Emit the following block verbatim:

```
WARNING: INSIDER GATE NOT MET

Phase 2 found zero insider sources. Every cited source could plausibly appear
in public documentation.

STOP. Do not proceed to Phase 4 (Analyst). Do not begin interpretation.
Do not write synthesis, contradiction checks, or follow-up queries.

Explicit resolution required — complete one of:

  Option A — Targeted re-search:
    Return to Phase 2. Search specifically for internal-only artifacts.
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

Write 2-4 paragraphs covering:
- What the internal evidence says collectively about the hypothesis
- How FC coverage evolved: DRAFT (all open) -> IN-PROGRESS (covered/open) -> FINAL (satisfies/violates/inconclusive/uncovered)
- Remaining gaps and which follow-up queries address them
- Overall finding: `confirmed` / `refuted` / `inconclusive`

**Phase 5 exit condition — emit FINAL ledger and Verdict:**

```
## Falsification Ledger — FINAL  (Phase 5 exit)
| FC | Description | Status | Sources | Notes |
|----|-------------|--------|---------|-------|
```

Status: `satisfies` / `violates` / `inconclusive` / `uncovered`

Every FC must appear.

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one row by path from the Archivist Evidence Table, grounded in the FINAL ledger]
```

---

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## What Made It Golden

**Four patterns that separate V-05 from the baseline (V-01):**

### 1. Extraction schema physically excludes interpretation columns (C-17)

V-01 has source blocks where Excerpt, Relevance, Strength, and FC appear in the same block — in-block ordering, not structural separation. V-05 declares a named **Schema Contract** before any table is populated, listing exactly which columns are `Permitted` and which are `Prohibited`. A `Schema Verification` step then checks for violations and requires `CLEAN` status before anything downstream proceeds. The schema makes structural separation a verifiable artifact property, not a reading convention.

### 2. CLEAN confirmation gates IN-PROGRESS emission (C-21)

V-05 introduces an explicit ordering chain: **Schema declared → Schema verified CLEAN (2-E1) → IN-PROGRESS emitted (2-E2)**. The IN-PROGRESS ledger is structurally guaranteed to reflect only schema-verified extraction rows. Without this chain (all prior variations), the coverage snapshot in IN-PROGRESS could be built from rows that leaked interpretation fields — making the insider count and FC coverage unreliable inputs to the gate decision.

### 3. IN-PROGRESS ledger surfaces before the gate fires, with a named Redirect Agenda (C-18)

V-01 has a single end-state ledger. V-05 emits the IN-PROGRESS ledger at Phase 2 exit, before the insider gate executes, and derives a **Redirect Agenda** directly from open FCs — one specific re-search action per uncovered FC (path pattern, tool, evidence type). The gate section shows `Open FCs at gate` and `Redirect items pending` drawn directly from that ledger state. Coverage gaps convert from vague "search more" instructions to FC-targeted re-search actions visible before the gate decision.

### 4. Halt instruction names an Option A / Option B resolution contract (C-19 + C-20)

V-01 emits "STOP." but advisory phrasing leaves an implicit continuation path: a model can nominally re-search and proceed. V-05 requires the executing agent to explicitly select and complete one of two named exits — **Option A** (re-search, re-verify schema, re-emit IN-PROGRESS, then gate re-evaluates) or **Option B** (proceed with inline reclassification text and `[PUBLIC-EVIDENCE-ONLY]` labels on all downstream headers). Proceeding without selecting one is named as a **protocol violation**, not merely ignored guidance.

---

## Final Rubric Criteria Summary (v5 -- 13 aspirational, /13)

| ID | Category | Criterion | V-05 |
|----|----------|-----------|------|
| C-09 | depth | Identifies at least one internal contradiction | PASS |
| C-10 | behavior | Recommends follow-up queries for evidence gaps | PASS |
| C-11 | behavior | Insider advantage treated as a hard exit condition | PASS |
| C-12 | correctness | Extraction and interpretation structurally separated | PASS |
| C-13 | coverage | Falsification ledger is a first-class named artifact | PASS |
| C-14 | behavior | Insider gate enforced by blocking WARNING text | PASS |
| C-15 | correctness | Structural separation via named roles/phases, not in-block ordering | PASS |
| C-16 | coverage | Falsification ledger exists in multiple lifecycle states | PASS |
| C-17 | correctness | Extraction table schema physically excludes interpretation columns | PASS |
| C-18 | coverage | IN-PROGRESS ledger surfaced before insider gate fires | PASS |
| C-19 | behavior | Insider gate uses halt semantics, not advisory semantics | PASS |
| C-20 | behavior | Halt instruction names exactly two valid exits (Option A / Option B contract) | PASS |
| C-21 | correctness | SCHEMA CLEAN confirmation emitted before IN-PROGRESS ledger state | PASS |

**Composite score**: 5/5 essential x 60 + 3/3 recommended x 30 + 13/13 aspirational x 10 = **100**
