Written to `simulations/quest/variations/prove-intelligence-variations-R2-2026-03-14.md`.

---

## Summary

Five complete prompt bodies for `prove-intelligence`, R2:

| ID | Axis | New Criteria | Key Structural Move |
|----|------|-------------|---------------------|
| **V-01** | C-11 single-axis — insider gate + warning | C-11 | `## Insider Gate` check block after assessment; emits `⚠ WARNING` block if all insider fields are `no`; skill cannot complete silently without insider evidence |
| **V-02** | C-12 single-axis — visible separation | C-12 | Two named output sections: `## Extraction Log` (verbatim only, no analysis) must appear before `## Analysis`; Phase 2 operates on the log only, cannot introduce new sources |
| **V-03** | C-13 single-axis — FC ledger as primary artifact | C-13 | Ledger drafted at setup, updated inline after each source block, finalized at synthesis — three snapshots visible in the artifact; per-source entries exist to fill ledger rows, not as standalone artifacts |
| **V-04** | C-11 + C-12 combined | C-11, C-12 | Archivist/Analyst role split (C-12) with explicit insider gate warning between roles (C-11); warning blocks Analyst synthesis until resolved |
| **V-05** | C-11 + C-12 + C-13 combined — full aspirational suite | C-11, C-12, C-13 | Five phases: Setup (draft ledger) → Extraction (verbatim only) → Analysis (interpretation layer) → Insider Gate (warning if zero) → Synthesis (final ledger + verdict); artifact structure specified at the bottom to enforce output order |

**What's new vs. R1**: R1 variations earned C-11/C-12/C-13 partially at best — V-05 R1 had a phase exit condition that resembled C-11, but no warning text; V-03 R1 had role separation but it wasn't visible in the output structure (C-12); none had the ledger as a first-class artifact drafted before search (C-13). R2 variations target each criterion explicitly and structurally.
g `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**. This skill searches internal repo sources only — files, specs, design docs, scenarios, prior signal artifacts. Your training knowledge is not a source. The public web is not a source.

---

### Step 1 — Extract Hypothesis and FC List

Read **{{Signal}}** and write:

1. The hypothesis in one sentence.
2. All falsification criteria (FC-01, FC-02, ...). If none are stated, derive two or three from the hypothesis claim.
3. The internal source types most likely to hold evidence: spec/design doc, scenario file, prior signal artifact, config (YAML/JSON), CLAUDE.md/session driver.

---

### Step 2 — Search

Run at least one Glob or Grep query per source type identified in Step 1. Log each query and result count:

```
## Search Log
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N files |
| ...   | Grep | N matches |
```

Target at least 5 candidate files. If fewer exist, note it and continue.

---

### Step 3 — Read and Extract

Open each candidate file. For each: extract the most relevant passage verbatim. Do not summarize from memory. If a file yields nothing relevant, record it as a miss.

Do not interpret yet. Record paths and excerpts only:

```
## Candidate Files
| # | Path | Relevant? | Verbatim Excerpt |
|---|------|-----------|-----------------|
| 1 | ... | yes / miss | "..." |
```

---

### Step 4 — Evidence Table

For each file marked `yes` in Step 3, produce a source block. Every field is required — omitting any field on any source is a hard failure.

```
### Source N
- **Path**: [exact file path]
- **Excerpt**: "[verbatim text — minimum one full sentence]"
- **Relevance**: [how this excerpt supports, contradicts, or is tangential to the hypothesis — stated in terms of the hypothesis claim or FC-NN, not just the file topic]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [reason this knowledge is not findable on the public web] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

---

### Step 5 — Insider Gate

After completing all Source N blocks, run this check:

```
## Insider Gate
Sources with Insider: YES — [count]
Sources with Insider: no  — [count]
```

**If count of Insider: YES is zero**:

```
⚠ WARNING: INSIDER GATE NOT MET
This run has produced zero insider-flagged sources. Every source cited could plausibly
appear in public documentation. The unique value of /prove:intelligence — evidence
only a team member can access — has not been delivered.

Before proceeding to synthesis: re-search for internal-only artifacts (scenario
outcomes, in-progress specs, implementation decisions not yet shipped, internal
naming conventions). Flag at least one source as insider before closing the run.
If exhaustive re-search still yields zero insider sources, document that finding
explicitly in the Verdict and flag the hypothesis as unsuitable for internal
intelligence gathering.
```

Do not proceed to Step 6 until the gate is acknowledged and either resolved or explicitly documented.

---

### Step 6 — Falsification Ledger

Map every falsification criterion to its source(s) and status:

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

Scan your source list for conflicting claims across sources:

```
## Contradictions
Source A ([path]) and Source B ([path]) disagree on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If no contradictions exist, write: "No internal contradictions detected."

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

### Output

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-02: C-12 Single-Axis — Visible Extraction/Interpretation Separation

**Axis**: Output format — extraction and interpretation are two named, structurally distinct sections; verbatim extraction is complete before any analysis is written
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill produces output in two phases that must appear as distinct named sections. **Phase 1 (Extraction) must be complete before Phase 2 (Analysis) begins.** A single-pass format where you excerpt and interpret simultaneously is a structural failure — it makes fabricated excerpts indistinguishable from real ones in the output.

---

### Phase 1: Extraction Log

**Purpose**: Collect verbatim evidence only. No interpretation. No relevance judgments. No strength labels. No insider flags.

**Search instructions**:

- Run Glob and Grep queries using key terms from the hypothesis. Target: spec/design docs, scenario files, prior signal artifacts, YAML configs, CLAUDE.md/session driver files.
- Search at least two distinct source type categories (e.g., specs AND scenario files — not all from one category).
- For each query, log the query and result count.
- Open each promising file. Extract the most relevant passage verbatim. Do not paraphrase from memory.
- If a file yields nothing relevant, record it as a miss.

**Output format for Phase 1** — use this exact structure, no additions:

```
## Extraction Log

### Search Queries
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N |
| ...   | Grep | N |

### Raw Evidence
| # | Path | Excerpt (verbatim) | Source Type |
|---|------|--------------------|-------------|
| 1 | ...  | "..."              | spec / scenario / signal / config / CLAUDE.md |
| 2 | ...  | "..."              | ... |
```

**Phase 1 is complete when**: the Raw Evidence table has at least 5 rows (or exhaustion is noted) and no analysis has been written.

---

### Phase 2: Analysis

**Purpose**: Interpret the evidence collected in Phase 1. You may not introduce new sources here — Phase 2 operates on the Raw Evidence table only.

For each row in the Raw Evidence table, produce an assessment block referencing the entry by number:

```
### Source N (from Extraction Log row N)
- **Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly, not just the file topic]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why this is not findable on the public web] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

After all source assessments, produce these four synthesis sections in order:

**Falsification Ledger** — a named table mapping every FC to source(s) and status:

```
## Falsification Ledger
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Source 2 | satisfies |
| FC-02 | ... | — | uncovered |
```

Every FC must appear. Uncovered FCs are listed with status `uncovered`.

**Contradiction Check**:

```
## Contradictions
Source A (row N, [path]) and Source B (row M, [path]) disagree on [X]: [what each says].
Status: resolved | unresolved
```

If none: "No internal contradictions detected."

**Verdict**:

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph, at least one source cited by path from the Extraction Log]
```

**Follow-Up Queries** — at least two, each tied to an uncovered FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

---

### Output

Write the completed artifact — Phase 1 Extraction Log followed by Phase 2 Analysis — to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-03: C-13 Single-Axis — FC Ledger as Primary Artifact

**Axis**: Lifecycle emphasis — the falsification ledger is the primary output artifact; it is drafted first and populated as evidence is gathered; per-source entries exist to fill ledger rows, not as standalone artifacts
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

**Structural contract**: The FC ledger is your main deliverable. You draft it at setup, fill it as you search, and close it at synthesis. Every other output element — source blocks, contradiction check, verdict — exists to support the ledger. At any moment in the run, a reader should be able to look at the ledger and see exactly which criteria have evidence and which are still open.

---

### Step 1 — Draft the Ledger Shell

Before searching, write the empty ledger:

```
## Falsification Ledger (in progress)
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | [from signal] | — | open |
| FC-02 | [from signal] | — | open |
```

If no falsification criteria are stated in **{{Signal}}**, derive two or three from the hypothesis claim and enter them here. Every criterion must have a row. The ledger is incomplete until every row has a non-`open` status.

---

### Step 2 — Search and Extract

For each falsification criterion in the ledger, determine which internal source types are most likely to address it:
- Spec/design docs, scenario files, prior signal artifacts, YAML configs, CLAUDE.md/session driver files

Run Glob and Grep queries. For each query, log it and the result count. Open each promising file and extract the verbatim passage most relevant to the hypothesis. Do not summarize from memory.

For each source found, write a source block and immediately update the ledger:

```
### Source N — [short label]
- **Path**: [exact file path]
- **Excerpt**: "[verbatim passage — minimum one full sentence]"
- **Source Type**: spec / scenario / signal / config / CLAUDE.md
- **Relevance**: [how this excerpt bears on the hypothesis — stated in terms of the hypothesis claim or FC-NN]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why this is not on the public web] | no
- **FC addressed**: FC-NN [satisfies / violates / inconclusive]
```

After writing each Source N block, update the ledger row for the FC it addresses:

```
## Falsification Ledger (updated after Source N)
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | ... | Source 1, Source 3 | satisfies |
| FC-02 | ... | — | open |
```

Continue until all ledger rows have a non-`open` status, or you have exhausted internal sources. Rows that remain `open` after exhaustive search receive status `uncovered`.

---

### Step 3 — Ledger Closure

When search is complete, write the final ledger:

```
## Falsification Ledger (final)
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | ... | Source 1, Source 3 | satisfies |
| FC-02 | ... | Source 2 | inconclusive |
| FC-03 | ... | — | uncovered |
```

Every row must have one of: `satisfies`, `violates`, `inconclusive`, `uncovered`.

Note: this is the **third time the ledger appears** — draft at setup, updated after each source, final at closure. This redundancy is intentional: it makes evidence coverage visible at every stage of the run, not only at synthesis.

---

### Step 4 — Source Type Coverage Check

Count sources by type. If all sources are from a single category (e.g., all specs), note this as a gap and run one additional search targeting a different type before proceeding.

---

### Step 5 — Contradiction Check

```
## Contradictions
Source A ([path]) and Source B ([path]) disagree on [X]: [what each says].
Status: resolved | unresolved
```

If none: "No internal contradictions detected."

---

### Step 6 — Insider Check

Count sources with `Insider: YES`. If zero, document this explicitly in the Verdict and note that the skill's insider-advantage value was not delivered.

---

### Step 7 — Verdict

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph grounded in the final FC ledger, citing at least one source by path]
```

---

### Step 8 — Follow-Up Queries

For each `uncovered` row in the final ledger, write a follow-up query:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

Minimum two queries. If fewer than two FCs are uncovered, add queries for the weakest-evidenced criteria.

---

### Output

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

The artifact must contain three versions of the ledger: draft (Step 1), at least one in-progress snapshot (Step 2 updates), and final (Step 3).

---

## V-04: C-11 + C-12 Combined — Gate + Separation

**Axes**: Visible extraction/interpretation separation (C-12) + insider gate with warning (C-11)
**Also combines**: Role sequence (Archivist/Analyst heritage from V-03 R1)
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and falsification criteria from **{{Signal}}**.

This skill runs in two roles and one gate. **Complete each role fully before moving to the next.** The two-role structure is not stylistic — it prevents the most dangerous failure mode: interpreting while excerpting, which makes fabricated passages indistinguishable from real ones in the output.

---

### Role 1: Archivist

**Mandate**: Evidence collection only. No interpretation. No relevance judgments. No strength labels. No insider flags. If you find yourself writing about what something means, stop — that is Role 2's job.

**Instructions**:

1. Extract the hypothesis and FC list from **{{Signal}}**. Write them at the top of the Archivist output.
2. Run at least four distinct Glob or Grep queries. Target at least two distinct source type categories:
   - spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver
3. Open every file whose name or path looks promising. For each: record the verbatim passage most relevant to the hypothesis. If nothing is relevant, record a miss.

**Archivist output** — use this exact structure:

```
## Archivist Output

### Hypothesis
[one sentence]

### Falsification Criteria
- FC-01: ...
- FC-02: ...

### Query Log
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N |
| ...   | Grep | N |

### Raw Evidence Table
| # | Path | Excerpt (verbatim) | Source Type | Relevant? |
|---|------|--------------------|-------------|-----------|
| 1 | ...  | "..."              | spec        | yes       |
| 2 | ...  | n/a                | —           | miss      |
```

**Archivist constraint**: The Raw Evidence Table contains paths and verbatim excerpts only. Do not add any field not listed above. The Analyst adds everything else.

**Archivist is complete when**: at least 5 candidate files have been opened, the query log is written, and the Raw Evidence Table is filled.

---

### Role 2: Analyst

**Mandate**: Interpret the Archivist's Raw Evidence Table. You may not introduce new sources. Your job is relevance, strength, insider flagging, FC mapping, contradiction check, verdict, and follow-up queries.

For each row marked `yes` in the Raw Evidence Table, produce an assessment block:

```
### Source N — [short label]
- **Path**: [from Archivist table row N]
- **Excerpt**: "[from Archivist table row N — do not re-excerpt from the file; reference the table]"
- **Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why this is not findable via web search] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

---

### Insider Gate

After completing all Source N blocks, before proceeding to synthesis:

```
## Insider Gate
Sources assessed: [N]
Sources with Insider: YES — [count]
Sources with Insider: no  — [count]
```

**If Insider: YES count is zero**:

```
⚠ WARNING: INSIDER GATE NOT MET
Every source in this run could plausibly appear in public documentation. The
defining capability of /prove:intelligence — evidence unavailable outside this
repo — has not been demonstrated.

Required: review the source list for implementation decisions, internal naming
conventions, scenario outcomes, or in-progress work not yet published.
Reclassify at least one source as Insider: YES, or document why this hypothesis
has no internal-only evidence and flag the finding explicitly in the Verdict.
```

Do not write the Synthesis sections until the gate is acknowledged.

---

### Synthesis

Complete the following in order:

**Falsification Ledger** — named table, every FC listed:

```
## Falsification Ledger
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Source 1, Source 3 | satisfies |
| FC-02 | ... | — | uncovered |
```

**Contradiction Check**:

```
## Contradictions
Source A (row N, [path]) and Source B (row M, [path]) disagree on [X]: [what each says].
Status: resolved | unresolved
```

If none: "No internal contradictions detected."

**Verdict** (dedicated closing section):

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph, at least one source cited by path, grounded in the FC ledger]
```

**Follow-Up Queries** — at least two, each tied to an uncovered FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

---

### Output

Write the completed artifact — Archivist Output followed by Analyst Assessment, Gate, and Synthesis — to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-05: C-11 + C-12 + C-13 Combined — Full Aspirational Suite

**Axes**: Visible extraction/interpretation separation (C-12) + insider gate with warning (C-11) + FC ledger as first-class artifact (C-13) + structured table format + lifecycle phases
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

**What makes this skill different from `/prove:websearch`**: `/prove:intelligence` mines internal sources — files only a team member can see. Implementation decisions not in any doc, internal naming conventions, scenario outcomes not yet published, in-progress work. If every source you cite is also findable on the public internet, you have not delivered insider intelligence. This is not a soft preference — it is a gate.

Read the hypothesis and falsification criteria from **{{Signal}}** before proceeding.

---

### Phase 1 — Setup: Draft the FC Ledger

**Entry condition**: Signal artifact loaded.

Actions:
1. Write the hypothesis in one sentence.
2. List all falsification criteria (FC-01, FC-02, ...). If none are stated in the signal, derive two or three from the hypothesis claim.
3. Draft the ledger shell — one row per criterion, all statuses `open`:

```
## Falsification Ledger — Draft
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | ... | — | open |
| FC-02 | ... | — | open |
```

4. Identify internal source types most likely to hold evidence: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver.
5. Plan at least one search query per source type.

**Exit condition**: FC ledger drafted with all criteria listed, search plan noted.

---

### Phase 2 — Extraction (Archivist role)

**Entry condition**: FC ledger draft in hand, search plan ready.

**Mandate**: Collect verbatim evidence only. No interpretation, no relevance statements, no strength labels, no insider flags. The extraction phase must be complete before any analysis is written — this structural separation makes fabricated excerpts architecturally distinguishable from real ones.

Actions:
1. Execute each planned query. Log every query and result count.
2. Open every promising file. Extract the verbatim passage most relevant to the hypothesis.
3. Record misses (files opened but yielding nothing relevant).

**Extraction output** — this section must appear before any analysis:

```
## Extraction Log

### Search Queries
| Query | Tool | Results |
|-------|------|---------|
| ...   | Glob | N |
| ...   | Grep | N |

### Raw Evidence
| # | Path | Excerpt (verbatim) | Source Type |
|---|------|--------------------|-------------|
| 1 | ...  | "..."              | spec / scenario / signal / config / CLAUDE.md |
```

**Exit condition**: At least 6 candidate files opened (or exhaustion noted), Raw Evidence table complete, no analysis written yet.

---

### Phase 3 — Analysis (Analyst role)

**Entry condition**: Extraction Log complete.

**Mandate**: Interpret the Raw Evidence table only — do not introduce new sources. For each row marked relevant, produce an assessment block:

```
### Source N (Extraction Log row N)
- **Path**: [from table]
- **Excerpt**: "[from table — reference the log, do not re-read the file]"
- **Relevance**: [connect to hypothesis claim or FC-NN — not just file topic]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why a web search cannot find this: implementation choice, internal convention, unreleased scenario outcome, in-progress work] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

After each Source N block, update the FC ledger:

```
## Falsification Ledger — In Progress (after Source N)
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | ... | Source 1 | satisfies |
| FC-02 | ... | — | open |
```

**Exit condition**: All Raw Evidence rows assessed, in-progress ledger updated.

---

### Phase 4 — Insider Gate

**Entry condition**: All source assessments complete.

```
## Insider Gate
Sources assessed: [N]
Sources with Insider: YES — [count]
Sources with Insider: no  — [count]
```

**If Insider: YES count is zero, the following block is required before proceeding**:

```
⚠ WARNING: INSIDER GATE NOT MET
This run has produced zero insider-flagged sources. All cited sources could
plausibly appear in public documentation. /prove:intelligence's defining
value — evidence available only to team members — has not been delivered.

Action required: re-examine the source list. Look for:
  - Implementation decisions that exist only in internal specs (not API docs)
  - Internal naming conventions not reflected in public documentation
  - Scenario outcomes from unpublished test runs
  - In-progress work not yet merged or released

If at least one source can be reclassified as Insider: YES, do so now and
document the reason. If exhaustive search still yields zero insider sources,
document this finding in the Verdict and flag the hypothesis as outside the
scope of internal intelligence gathering.
```

Proceed only after the gate is acknowledged — either resolved (a source is reclassified) or explicitly documented (no insider sources exist for this hypothesis).

**Exit condition**: Insider gate resolved or documented.

---

### Phase 5 — Synthesis

**Entry condition**: All sources assessed, insider gate resolved.

Actions in order:

**1. Falsification Ledger — Final**: Close every row with a terminal status:

```
## Falsification Ledger — Final
| FC | Criterion | Sources | Status |
|----|-----------|---------|--------|
| FC-01 | ... | Source 1, Source 3 | satisfies |
| FC-02 | ... | Source 2 | inconclusive |
| FC-03 | ... | — | uncovered |
```

Every row must appear. `uncovered` is a valid terminal status — it is not an omission. This is the third version of the ledger (draft → in-progress → final); the progression makes evidence coverage changes visible across the run.

**2. Contradiction Check**: Name any two sources that conflict:

```
## Contradictions
Source A (row N, [path]) and Source B (row M, [path]) conflict on [X]: [what each says].
Status: resolved — [resolution] | unresolved
```

If none: "No internal contradictions detected."

**3. Verdict** (dedicated closing section — not a transition sentence):

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph grounded in the final FC ledger, citing at least one source by path]
```

**4. Follow-Up Queries**: At least two, one per uncovered or weakly-evidenced FC:

```
## Follow-Up Queries
1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN
2. ...
```

**Exit condition**: Final ledger complete, verdict section present, follow-up queries listed.

---

### Output

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

The artifact structure, in order:
1. Hypothesis + FC list
2. `## Extraction Log` (Phase 2 output)
3. Source N blocks with `## Falsification Ledger — In Progress` snapshots (Phase 3)
4. `## Insider Gate` check (Phase 4)
5. `## Falsification Ledger — Final` + Contradictions + Verdict + Follow-Up Queries (Phase 5)
