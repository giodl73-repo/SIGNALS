Written to `simulations/quest/variations/prove-intelligence-variations-R1-2026-03-14.md`.

---

## Summary

Five complete prompt bodies for `prove-intelligence`, R1:

| ID | Axis | Key Bets |
|----|------|----------|
| **V-01** | Output format — structured table | Per-source `Source N` blocks with 5 explicit fields; Step-labeled phases with hard-failure warnings inline; falsification mapping and contradiction check as named steps |
| **V-02** | Lifecycle — single-pass, minimal | No phase headers; no role separation; continuous execution; format left open; strengths/insider inline with sources; verdict capped at 150 words |
| **V-03** | Role sequence — Archivist then Analyst | Hard separation: Archivist collects verbatim only (no interpretation), Analyst adds relevance/strength/insider/FC mapping in a second pass over the same evidence |
| **V-04** | Phrasing register — detective/investigative | "Lead" vocabulary instead of "source"; "case file entry" framing; "open threads" instead of "follow-up queries"; conversational second-person; same rubric coverage without bureaucratic structure |
| **V-05** | Combined: explicit lifecycle + table + insider prominence | Five phases with entry/exit conditions; insider advantage called out in the opening paragraph as the defining distinction from `prove-websearch`; FC ledger as a first-class synthesis artifact |

**Rubric coverage by variation**: All five cover C-01–C-05 (essential). V-01, V-03, V-05 explicitly drive C-06–C-10. V-02 and V-04 cover C-06–C-08 more lightly — leaving room to test whether the rubric rewards explicitness or just presence.
 web.

### Step 1 — Search

Use Glob and Grep to locate candidate files. Search strategies:

- Glob for files whose names match key terms from the hypothesis
- Grep for verbatim phrases from the hypothesis across `**/*.md` and `**/*.yaml`
- Glob across namespace directories: `simulations/scout/`, `simulations/draft/`, `simulations/prove/`, `simulations/trace/`
- Grep for related concept terms (synonyms, acronyms, adjacent concepts) if initial searches return few results

Collect at least 5 candidate files before moving to Step 2. If fewer than 5 exist, note it.

### Step 2 — Read and Extract

For each candidate file: read it, identify the most relevant passage, and record it verbatim (do not paraphrase from memory).

### Step 3 — Build the Evidence Table

Produce one row per source. Every row must contain all five fields. Omitting any field on any row is a hard failure.

| Field | Requirement |
|-------|-------------|
| **Path** | Exact file path as returned by Glob/Read — no paraphrase |
| **Excerpt** | Verbatim text from the file, long enough to verify the claim (minimum one full sentence) |
| **Relevance** | How this excerpt supports, contradicts, or is tangential to the hypothesis — stated in terms of the hypothesis claim, not the file topic |
| **Strength** | `strong` / `moderate` / `weak` — as its own field, not embedded in the Relevance column |
| **Insider** | `YES — [reason this knowledge is not on the public web]` or `no` |

Format:

```
### Source N
- **Path**: ...
- **Excerpt**: "..."
- **Relevance**: ...
- **Strength**: strong | moderate | weak
- **Insider**: YES — ... | no
```

### Step 4 — Falsification Mapping

For each falsification criterion extracted in Step 1, identify the source(s) most directly bearing on it. Add a mapping section:

```
### Falsification Mapping
| Criterion | Source(s) | Status |
|-----------|-----------|--------|
| FC-01: ... | Source 2, Source 4 | satisfies / violates / inconclusive |
```

If the signal artifact has no explicit falsification criteria, derive 2-3 from the hypothesis statement and map against those.

### Step 5 — Contradiction Check

Scan your source list: do any two sources disagree on the same claim? If yes, name them explicitly:

```
### Contradictions
Source A (path) and Source B (path) disagree on X: [what each says]
Status: resolved / unresolved
```

If no contradictions exist, write "No internal contradictions detected."

### Step 6 — Verdict

Close with a dedicated verdict section. It must:
- State the collective weight of internal evidence: **confirms** / **contradicts** / **inconclusive**
- Reference at least one source by file path
- State confidence: high / medium / low and why

```
## Verdict
**Collective finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph citing at least one source by path]
```

### Step 7 — Follow-Up Queries

List at least two specific follow-up internal queries for evidence gaps:

```
## Follow-Up Queries
1. **Query**: [what to search for] | **Where**: [directory or file pattern] | **Addresses**: [FC-NN]
2. ...
```

### Output

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-02: Lifecycle — Single-Pass, Minimal Structure

**Axis**: Lifecycle emphasis (single-pass, no explicit phase headers, findings inline)
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis from **{{Signal}}**. Your job is to search the internal repo and return a single, well-organized intelligence report on what the codebase knows about this hypothesis.

**Single-pass execution**: Do not announce phases. Search, read, assess, and report in one continuous operation. The report is the output.

---

**What to search**: Use Glob and Grep to find repo files that contain evidence — design docs, specs, CLAUDE.md files, scenario files, prior signal artifacts, YAML configs. Exclude your training knowledge. Exclude the public web. Every piece of evidence must be a file in this repo that you actually opened.

**What to report**: For each source you cite, include:
- The exact file path
- A verbatim excerpt (not a summary — copy the relevant passage)
- One sentence on how the excerpt bears on the hypothesis
- A strength label: **strong**, **moderate**, or **weak**
- Mark any source as **[Insider]** if it contains knowledge that could not be found via a web search — this is what makes `/prove:intelligence` distinct from `/prove:websearch`

Organize sources by strength (strong first, weak last). Use consistent formatting within your chosen style, but format is not specified — table, list, or numbered entries are all acceptable as long as every field is present.

**What to synthesize**: After the sources, write a short verdict. State whether the internal evidence collectively confirms, contradicts, or leaves inconclusive the hypothesis. Name at least one specific file. Keep the verdict under 150 words.

**What to surface**: Note any place where two sources conflict with each other. Note any gap — a falsification criterion in the hypothesis that no source addresses. For each gap, name one search that would close it.

Write the report to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-03: Role Sequence — Archivist First, then Analyst

**Axis**: Role sequence (Archivist gathers without interpretation; Analyst interprets; separation enforced)
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

Read the hypothesis and any falsification criteria from **{{Signal}}**.

This skill runs in two sequential roles. Complete Role 1 in full before beginning Role 2.

---

### Role 1: Archivist

Your job is evidence collection only. Do not interpret. Do not assess relevance. Do not label strength. Only find and quote.

**Instructions**:

1. Run at least four distinct Glob or Grep queries using key terms from the hypothesis. Log each query and the count of results returned.
2. Open every file that appears promising based on name or path alone.
3. For each file opened, extract the single most relevant passage verbatim. If nothing is relevant, note the file as a miss.
4. Record your findings in a raw evidence table:

```
## Archivist Log
### Query Log
| Query | Tool | Results |
|-------|------|---------|
| ... | Glob | N files |
| ... | Grep | N matches |

### Evidence Collected
| # | Path | Raw Excerpt |
|---|------|-------------|
| 1 | ... | "..." |
| 2 | ... | "..." |
```

**Archivist constraint**: Do not write any interpretation beyond the excerpt. The Analyst role will add relevance, strength, and insider flags in the next pass.

---

### Role 2: Analyst

You receive the Archivist's raw evidence table. Your job is interpretation and synthesis.

**For each source in the Archivist table**:

Add these fields (do not re-copy the excerpt — reference the entry by number):

```
### Source N — [short label]
- **Relevance**: How this excerpt bears on the hypothesis — state the connection in terms of the hypothesis claim or a specific falsification criterion
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why this is not on the public web] | no
- **FC mapping**: FC-NN satisfies / violates / inconclusive | n/a
```

**After all sources**:

1. **Contradiction report**: Name any two sources that disagree. If none, state so explicitly.
2. **Coverage map**: For each falsification criterion, list which source(s) address it. Flag uncovered criteria.
3. **Verdict**: Confirms / contradicts / inconclusive. Confidence: high / medium / low. One paragraph, at least one source cited by path.
4. **Follow-up queries**: Two or more specific internal queries for uncovered falsification criteria — each with: what to query, where to look, which FC it addresses.

Write the completed artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-04: Phrasing Register — Conversational Detective

**Axis**: Phrasing register (investigative/discovery framing, second-person casual, detective vocabulary)
**Also combines**: Role sequence (single investigator, no separation)
**Hypothesis**: (injected from Signal input at runtime)

---

You're investigating a hypothesis. Your beat is the internal repo — files, specs, design docs, prior signals. Your sources are what's actually in this codebase, not what you already know, not the web.

**Start here**: Open **{{Signal}}** and read it. Extract the hypothesis in one sentence. List the falsification criteria if any are stated. Write them at the top of your working notes.

---

**The investigation**

Go looking. Use Glob and Grep to track down files that know something about this hypothesis. Cast a wide net first — search by key terms, by related concepts, by file path patterns. Then narrow.

For every lead you follow (every file you open), document it like a case file entry:

```
### Lead N: [short label]
File: [exact path]
What it says: "[verbatim passage]"
What it means for the hypothesis: [connect it to the hypothesis claim directly — "this supports / undermines / complicates the claim because..."]
Weight: strong | moderate | weak
Exclusive intel: [is this something the web doesn't know? If yes, flag it: "Insider — this is only knowable from the internal repo because..."]
```

Don't write leads from memory. If you haven't opened the file, you don't have a lead.

---

**The case against the null**

After your leads, work through the falsification criteria. For each one, ask: does any lead answer it? Fill in a quick ledger:

```
FC-01: [criterion] — answered by Lead N / unanswered
FC-02: [criterion] — answered by Lead N / unanswered
```

---

**Contradictions**

Did any two leads tell you conflicting things? Name them: "Lead 2 says X; Lead 5 says Y — they can't both be right." If you can resolve it, resolve it. If you can't, flag it open.

---

**The call**

Close with a verdict. Make it a dedicated section, not a throwaway closing sentence:

```
## Verdict
The internal record [confirms / contradicts / leaves inconclusive] the hypothesis.
Confidence: [high / medium / low] — because [one sentence grounded in a specific lead, cited by path].
```

---

**What's still open**

End with two or more specific follow-up searches for any falsification criteria your leads didn't cover:

```
## Open Threads
- Search for [what], in [where], to address [FC-NN]
- ...
```

Write your case file to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.

---

## V-05: Combined — Explicit Lifecycle + Table Format + Insider Advantage Prominent

**Axes**: Lifecycle emphasis (explicit phase headers with entry/exit conditions) + Output format (structured table) + Insider framing (prominent, up-front distinction from prove-websearch)
**Hypothesis**: (injected from Signal input at runtime)

---

You are running `/prove:intelligence` for **{{Topic}}**.

**What makes this skill different from `/prove:websearch`**: `/prove:intelligence` mines internal sources — files only a team member can see. If every source you cite is also searchable on the public internet, you have not delivered insider intelligence. At least one source must be flagged as insider-only knowledge.

Read the hypothesis and falsification criteria from **{{Signal}}** before proceeding.

---

### Phase 1 — Setup

**Entry condition**: Signal artifact loaded, hypothesis extracted, falsification criteria listed.

Actions:
- Write the hypothesis in one sentence.
- List all falsification criteria (FC-01, FC-02, ...). If none are stated, derive two or three from the hypothesis claim.
- Identify the internal source types most likely to hold evidence: spec/design docs, scenario files, prior signal artifacts, YAML configs, CLAUDE.md files.
- Plan your search: at least one Glob query per source type identified.

**Exit condition**: Hypothesis written, FC list complete, search plan noted.

---

### Phase 2 — Search

**Entry condition**: Search plan in hand.

Actions:
- Execute each planned query. Log every query and result count.
- For sparse results: broaden terms, try synonyms, search by concept rather than exact phrase.
- Target: at least 6 candidate files before moving to Phase 3.

**Exit condition**: Candidate file list with at least 6 entries (or exhaustion noted if fewer exist).

---

### Phase 3 — Evidence Extraction

**Entry condition**: Candidate file list.

For each candidate: open it and extract the verbatim passage most relevant to the hypothesis. Do not summarize from memory. If a file yields nothing relevant, record it as a miss.

Build the evidence table:

```
| # | Path | Excerpt (verbatim) | Source Type |
|---|------|-------------------|-------------|
| 1 | ... | "..." | spec / scenario / signal / config / CLAUDE.md |
```

**Exit condition**: Evidence table complete, misses noted.

---

### Phase 4 — Assessment

**Entry condition**: Evidence table populated.

For each row in the evidence table, add an assessment block:

```
### Source N
- **Path**: [from table]
- **Excerpt**: "[from table]"
- **Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly]
- **Strength**: strong | moderate | weak
- **Insider**: YES — [why a web search could not find this] | no
- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a
```

Insider flag guidance: flag YES if the source contains decisions, constraints, or context that exist only in this repo — implementation choices not in public docs, internal naming conventions, in-progress work not yet shipped, scenario outcomes not published.

**Exit condition**: All sources assessed. At least one source carries Insider: YES.

---

### Phase 5 — Synthesis

**Entry condition**: All sources assessed.

Actions:

1. **Falsification ledger**: For each FC, list which source(s) address it and the status.

```
| FC | Criterion | Source(s) | Status |
|----|-----------|-----------|--------|
| FC-01 | ... | Source 2 | satisfies |
```

2. **Contradictions**: Identify any two sources that disagree. State: "Source A (path) and Source B (path) conflict on X: [what each says]. Status: resolved / unresolved." If none, state explicitly.

3. **Verdict** (required section, at the close):

```
## Verdict
**Finding**: confirms | contradicts | inconclusive
**Confidence**: high | medium | low
**Basis**: [one paragraph, at least one source cited by path, grounded in the FC ledger]
```

4. **Follow-up queries**: At least two, each tied to an uncovered FC:

```
## Follow-Up Queries
1. Query: [what] | Where: [path pattern] | Addresses: FC-NN
2. ...
```

**Exit condition**: Verdict section present, follow-up queries listed.

---

### Output

Write the complete artifact to `simulations/prove/investigations/{{topic}}-intelligence-{{date}}.md`.
