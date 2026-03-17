Written to `simulations/quest/variations/prove-websearch-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- Summary

**5 variations across 3 single-axis + 2 combined:**

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Pre-printed search block template -- `Quote:`, `Relevance:`, `Strength:`, `Credibility:` fields; C-02/C-03/C-04/C-05 enforced by structural position |
| **V-02** | Phrasing register | Imperative/conversational style -- "Run the search. Copy the quote." -- reduces model inference overhead on what counts as evidence |
| **V-03** | Lifecycle emphasis | Named phases with explicit gates: QUERY DESIGN -> EVIDENCE COLLECTION -> BALANCE CHECK -> SYNTHESIS; C-06 enforced by GATE 1, C-07 by GATE 3 |
| **V-04** | Format + lifecycle (V-01 + V-03) | Template fields inside phase gates -- closes C-01 through C-07 via structural means; refinement trail appears as a PHASE 4 note |
| **V-05** | Full synthesis | All axes + pre-printed SYNTHESIS sub-fields (C-09) + PHASE 3 query refinement trail field (C-10 placed at the moment of observation, not retrospectively) |

---

**Key design decisions:**

- **C-02 (verbatim quotes)** is enforced via a pre-printed `Quote:` field in V-01/V-03/V-04/V-05. A model filling in a labeled field is structurally less likely to paraphrase than one following a prose rule.
- **C-07 (balance check)** gets its own dedicated gate phase in V-03 through V-05, surfacing the most common failure mode: pro-evidence exhausting the query budget before refutation is attempted.
- **C-10 placement**: V-05 puts the refinement trail in PHASE 3 (during search, before synthesis), not PHASE 4 (retrospective). This is a deliberate design bet -- open research question for live runs.

**Predicted V-golden:** V-05. All 10 criteria have structural homes. V-04 is the closest competitor, missing only the pre-printed synthesis sub-fields and PHASE 3 trail placement.
ence before attempting refutation.

**Predicted ceiling:** V-05 -- maximum structural coverage; no omission path for any essential
or recommended criterion. V-04 is the closest competitor (template + gates, without synthesis
surface pre-printing).

---

## V-01: Pre-Printed Search Block Template

**Axis:** Output format -- each search is a filled-in pre-printed template block, not freeform
prose. Every required field (query, sources, quote, relevance, strength) is a labeled line
the model must populate.
**Hypothesis:** Structural position enforces C-03 (search record) and C-02 (quote field) better
than instructional prose. A model filling in a pre-printed `Quote:` field is less likely to
paraphrase than one told "include a quote." Pre-printed `Strength:` and `Relevance:` fields
make C-04 and C-05 mechanically unavoidable. Tests whether template format alone is sufficient
for all 5 essential criteria without explicit phase gates.

```
You are running /prove:websearch.

Inputs:
  Topic:      {topic}
  Hypothesis: {hypothesis}

Rules (apply throughout):
- Every factual claim must have a source URL. Do not use training data as evidence.
- Evidence is verbatim text in quotation marks. If you paraphrase, label it explicitly as
  "Paraphrase:" and still provide the source URL.
- You must perform at least 2 searches with different query framings.

---

For each search, fill in this template exactly. Do not skip or rename any field.

### SEARCH [N]

Query:
  [Exact query string submitted to the search engine]

Sources found:
  1. [Title] -- [URL]
  2. [Title] -- [URL]
  (Add more rows as needed. Only list sources you actually retrieved content from.)

Evidence:
  Source: [URL from above]
  Credibility: [peer-reviewed / industry report / news outlet / blog / forum / other]
  Quote: "[Exact verbatim text from the source, in quotation marks]"
  Relevance: [supports / refutes / mixed] -- [One sentence explaining how this evidence
              relates to the hypothesis.]
  Strength: [strong / weak / mixed] -- [One sentence justifying the rating.]

  (Repeat the Evidence block for each additional source from this search.)

---

Run at least 2 searches. After completing all searches, write:

### SYNTHESIS

Evidence summary:
  Supporting: [List sources that support the hypothesis, one per line with URL]
  Refuting:   [List sources that refute the hypothesis, one per line with URL]
  Mixed:      [List sources with mixed evidence, one per line with URL]

Aggregate finding: [One paragraph. Reference at least two sources by name. State what the
combined evidence says about the hypothesis. Do not introduce claims without URLs.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count.
```

---

## V-02: Imperative / Conversational Register

**Axis:** Phrasing register -- instructions written as direct imperatives ("Run this search.
Paste the query. Copy the quote.") rather than formal/descriptive prose. The goal is to keep
the model in execution mode rather than meta-commentary mode.
**Hypothesis:** Imperative phrasing with short sentences reduces the model's tendency to
summarize or paraphrase evidence before outputting it. When instructions say "Copy the exact
text" rather than "evidence must be verbatim," the action is closer to the surface. Tests
whether register change alone improves C-01/C-02 compliance without pre-printed template
fields.

```
You are running /prove:websearch. Here is what you need to do.

Topic:      {topic}
Hypothesis: {hypothesis}

Before you start: Every piece of evidence needs a URL. Do not cite things you know from
training. If you can't find a URL, don't use it as evidence.

---

Step 1: Design your queries.

Write down at least 3 search queries before you run any of them. Frame them differently:
- One that looks for support ("X works because...")
- One that looks for criticism ("X fails when..." or "problems with X")
- One using domain-specific or technical terminology

List your planned queries here:
  Q1: [query]
  Q2: [query]
  Q3: [query]

Step 2: Run each search.

For each query, do this:
  - Run the search.
  - Write down the exact query you used.
  - List the URLs you got back (title + URL).
  - For each source you read, copy a direct quote. Use quotation marks. Do not paraphrase.
  - Say whether the quote supports, refutes, or is mixed on the hypothesis. One sentence.
  - Rate the source: strong, weak, or mixed. Say why in one sentence.
  - Note what kind of source it is (peer-reviewed paper, industry blog, news, forum, etc.).

Format for each search:

**Query used:** [exact string]
**Sources:**
  - [Title] ([URL])

**Evidence from [URL]:**
  "[Exact quote from source]"
  Relevance: [supports / refutes / mixed] -- [one sentence]
  Strength: [strong / weak / mixed] -- [one sentence]
  Source type: [peer-reviewed / industry report / news / blog / forum]

Step 3: Check your balance.

Do you have at least one source that supports the hypothesis AND at least one that refutes
or casts doubt on it? If not, run an additional search targeting the missing side. Write:
  Balance check: [have both sides / missing support / missing refutation -- ran query: Q]

Step 4: Synthesize.

Write a short paragraph (3-5 sentences) summing up what the web evidence says about the
hypothesis. Name at least two sources. State your overall confidence: the evidence is
[strong / weak / mixed] that [hypothesis restatement].

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count.
```

---

## V-03: Explicit Phase Gates

**Axis:** Lifecycle emphasis -- the skill is divided into named, gated phases. Each phase
must produce a declared output before the next phase begins. The gate structure makes the
lifecycle visible and prevents phases from collapsing into each other (e.g., query design
happening mid-search, or synthesis starting before balance is checked).
**Hypothesis:** Explicit phase gates improve C-06 (multi-query coverage) and C-07 (balanced
evidence) by forcing query planning before evidence collection begins. A BALANCE CHECK phase
between execution and synthesis surfaces the most common C-07 failure mode (pro-evidence
exhausts the query budget before refutation is attempted). Tests whether lifecycle structure
alone -- without pre-printed field templates -- drives essential criterion coverage.

```
You are running /prove:websearch.
All section headers are fixed. Every gate must fire before the next phase begins.
Do not reorder, rename, or remove any phase header.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## PHASE 1: QUERY DESIGN
[Complete before running any searches. List all planned queries here.]

Queries planned:
  Q1 (supporting framing):    [exact query string]
  Q2 (refuting framing):      [exact query string]
  Q3 (domain/technical):      [exact query string, or "N/A -- combined with Q1"]
  Q4+ (optional refinement):  [if needed after reviewing Q1-Q3 results]

Query design rationale:
  Q1 seeks evidence for the hypothesis because: [one sentence]
  Q2 seeks evidence against the hypothesis because: [one sentence]

GATE: Query design complete. At least 2 queries with distinct framings are present above.
      Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION
[Run each planned query. Record results below. Do not advance to PHASE 3 until all planned
queries from PHASE 1 are run. Every factual claim requires a URL -- no training-data evidence.]

### Query: Q1
  Query string: [exact string submitted]
  Sources:
    1. [Title] -- [URL]
    2. [Title] -- [URL]

  Evidence:
    Source URL: [URL]
    Quote: "[Verbatim text in quotation marks]"
    Relevance: [supports / refutes / mixed] -- [one sentence linking to hypothesis]
    Strength: [strong / weak / mixed] -- [one sentence justification]
    Credibility: [peer-reviewed / industry report / news / blog / forum]

  (Repeat Evidence block for each source retrieved.)

### Query: Q2
  Query string: [exact string submitted]
  Sources:
    1. [Title] -- [URL]

  Evidence:
    Source URL: [URL]
    Quote: "[Verbatim text in quotation marks]"
    Relevance: [supports / refutes / mixed] -- [one sentence]
    Strength: [strong / weak / mixed] -- [one sentence]
    Credibility: [peer-reviewed / industry report / news / blog / forum]

(Repeat this section for Q3 and any additional planned queries.)

GATE: Evidence collection complete. All planned queries from PHASE 1 have been run.
      Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK
[Before synthesis: verify coverage of both sides of the hypothesis.]

Supporting sources:  [count] -- [list URLs]
Refuting sources:    [count] -- [list URLs]
Mixed sources:       [count] -- [list URLs]

Balance verdict:
  [BALANCED -- at least one supporting and one refuting/mixed source present]
  OR
  [ONE-SIDED -- only [supporting/refuting] evidence found. Ran additional query:
   Query: [new query string targeting missing side]
   Result: [sources found / no sources found after targeted search]]

GATE: Balance check complete. Either balanced evidence exists or one-sided result is
      documented with a targeted follow-up query. Do not proceed to PHASE 4 until met.

---

## PHASE 4: SYNTHESIS
[Write after PHASE 3 GATE is met. Reference sources by URL, not by description alone.
 Do not introduce new claims not grounded in evidence from PHASE 2.]

Cross-source findings:
  Convergence: [Where sources agree -- cite at least two URLs]
  Conflict:    [Where sources disagree -- cite at least two URLs, or "No conflict found"]

Aggregate conclusion:
  [One paragraph. State what the web evidence says about the hypothesis in aggregate.
   Name at least two sources. Conclude: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, balance_result.
```

---

## V-04: Pre-Printed Template + Explicit Phase Gates (Axes 1+3)

**Axes:** Output format (pre-printed search block template) + lifecycle emphasis (explicit
phase gates with named outputs)
**Hypothesis:** Template fields (V-01 axis) close C-02/C-03/C-04/C-05 by structural position.
Phase gates (V-03 axis) close C-06/C-07 by forcing balance before synthesis and query design
before execution. Together, they address all 5 essential criteria and the two highest-value
recommended criteria (C-06, C-07) through structural means rather than instructional prose.
This is the strongest dual-mechanism approach before full synthesis. Tests whether all 7
highest-value criteria can be mechanically enforced without aspirational surfaces.

```
You are running /prove:websearch.
All phase headers are fixed. Every gate must fire before the next phase begins.
Fill in every template field -- do not skip, rename, or omit any field or section header.

Topic:      {topic}
Hypothesis: {hypothesis}

Rule: Every factual claim must have a source URL. Do not use training data as evidence.
      Evidence is verbatim text in quotation marks. Label any paraphrase explicitly.

---

## PHASE 1: QUERY DESIGN
[Complete before running any searches.]

  Q1 (supporting framing):    [exact query string]
  Q2 (refuting framing):      [exact query string]
  Q3 (additional angle):      [exact query string, or "merged with Q1: [reason]"]

GATE 1: At least Q1 and Q2 are present with distinct framings. Proceed to PHASE 2.

---

## PHASE 2: EVIDENCE COLLECTION
[Run each query from PHASE 1. Fill in one SEARCH BLOCK per query.
 Every claim in a SEARCH BLOCK must have a URL from that search.]

### SEARCH BLOCK: Q[N]

  Query:        [Exact query string submitted]

  Sources:
    1. [Title] -- [URL]
    2. [Title] -- [URL]

  --- Evidence Item ---
  Source URL:   [URL from sources list above]
  Credibility:  [peer-reviewed / industry report / news outlet / blog / forum]
  Quote:        "[Verbatim text copied from source, in quotation marks. Do not paraphrase.]"
  Relevance:    [supports / refutes / mixed] -- [One sentence: how does this quote relate
                to the hypothesis?]
  Strength:     [strong / weak / mixed] -- [One sentence: why this rating?]
  --- End Evidence Item ---

  (Repeat Evidence Item block for each additional source retrieved from this query.)

[Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.]

GATE 2: All queries from PHASE 1 have search blocks with filled-in fields.
        Proceed to PHASE 3.

---

## PHASE 3: BALANCE CHECK
[Check coverage before synthesis. Do not proceed to PHASE 4 until this gate is met.]

  Supporting count:   [N] -- [list source URLs]
  Refuting count:     [N] -- [list source URLs]
  Mixed count:        [N] -- [list source URLs]

  Balance result:
    [BALANCED -- at least one supporting and one refuting/mixed item present above]
    OR
    [ONE-SIDED: [side] only. Targeted follow-up query:
       Query:   [query string targeting the missing side]
       Sources: [title -- URL, or "no sources found"]]

GATE 3: Balance result is filled in (either BALANCED or ONE-SIDED with documented follow-up).
        Proceed to PHASE 4.

---

## PHASE 4: SYNTHESIS
[Complete after GATE 3. Reference sources by URL. No new claims without URLs.]

  Convergence:   [Where two or more sources agree -- cite URLs]
  Conflict:      [Where sources disagree -- cite URLs, or "No material conflict found"]

  Query refinement:
    [If any query was modified mid-investigation, document here:
     Original query: [Q string] | Gap revealed: [what was missing] | Refined to: [new Q]
     Or: "No refinement -- original queries returned sufficient coverage."]

  Conclusion: [One paragraph. Name at least two sources by URL. State aggregate verdict:
               evidence is [strong / weak / mixed / insufficient] that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, balance_result.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Pre-printed template blocks (V-01) + explicit phase gates (V-03) + conversational
rule framing (V-02 register for the header) + pre-printed synthesis surface (C-09) + pre-printed
query refinement trail field (C-10)
**Hypothesis:** Maximum structural coverage prevents omission of any criterion. The template
fields enforce C-01 through C-05. Phase gates enforce C-06 (query design before execution) and
C-07 (balance check before synthesis). The pre-printed SYNTHESIS section with named sub-fields
(Convergence, Conflict, Conclusion) enforces C-09. The pre-printed "Query refinement:" field
inside PHASE 4 enforces C-10 at the only location where refinement is visible -- after results
are in, before synthesis. The "Credibility:" field in every evidence block enforces C-08. No
surface where any of the 10 criteria should appear is left to model discretion. This is the
direct synthesis target for R1.

```
You are running /prove:websearch.

Rules first:
  1. Every factual claim needs a URL. Do not cite training data. If you don't have a URL,
     you don't have evidence.
  2. Evidence means a verbatim quote in quotation marks. Paraphrases must be labeled
     "Paraphrase:" and still carry a URL.
  3. Fill in every pre-printed field. Do not skip or rename any field or section header.
  4. Every phase gate must fire before the next phase begins.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## PHASE 1: QUERY DESIGN
[Plan your queries before running any. Include both pro and con framings.]

  Q1 (support framing):     [exact query string]
  Q2 (refutation framing):  [exact query string]
  Q3 (technical/domain):    [exact query string, or "N/A -- merged with: Q[N]"]

  Design note: [One sentence -- what angle does Q2 attack that Q1 misses?]

GATE 1: Q1 and Q2 are present with distinct framings. Q2 explicitly targets the refutation
        side. Proceed to PHASE 2 only after this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION
[One SEARCH BLOCK per query. Fill in every field -- no exceptions.]

### SEARCH BLOCK: Q[N]

  Query string:   [Exact text submitted to the search engine]

  Sources found:
    1. [Title] -- [URL]
    2. [Title] -- [URL]
    (Add rows as needed. Only list sources you retrieved content from.)

  --- Evidence Item [A] ---
  Source URL:   [URL]
  Credibility:  [peer-reviewed / industry report / news outlet / blog / forum / other]
  Quote:        "[Exact verbatim text from source in quotation marks. Do not paraphrase.]"
  Relevance:    [supports / refutes / mixed] -- [One sentence: connection to hypothesis]
  Strength:     [strong / weak / mixed] -- [One sentence: justification for rating]
  --- End Evidence Item [A] ---

  --- Evidence Item [B] ---
  Source URL:   [URL]
  Credibility:  [peer-reviewed / industry report / news outlet / blog / forum / other]
  Quote:        "[Verbatim text in quotation marks]"
  Relevance:    [supports / refutes / mixed] -- [One sentence]
  Strength:     [strong / weak / mixed] -- [One sentence]
  --- End Evidence Item [B] ---

  (Add more Evidence Items for additional sources from this query.)

[Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.]

GATE 2: Every query from PHASE 1 has a SEARCH BLOCK with all fields filled in.
        Proceed to PHASE 3 only after this gate is met.

---

## PHASE 3: BALANCE CHECK
[Review your evidence before synthesis. If one side is missing, run a targeted follow-up now.]

  Supporting count:   [N] -- URLs: [list]
  Refuting count:     [N] -- URLs: [list]
  Mixed count:        [N] -- URLs: [list]

  Balance result:
    [BALANCED]
    OR
    [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
       Follow-up query: [exact string targeting missing side]
       Results:         [title -- URL, or "No sources found after targeted search"]]

  Query refinement trail:
    [Document any query that was modified based on earlier results:
     Original: [Q string] | What was missing: [gap] | Refined to: [new string]
     Or: "No refinements -- original Q1/Q2/Q3 returned sufficient coverage on both sides."]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Refinement trail is filled. Proceed to PHASE 4 only after both fields are complete.

---

## PHASE 4: SYNTHESIS
[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

  Convergence:
    [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

  Conflict:
    [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
     all [N] sources point [direction], though credibility varies: [brief note]."]

  Overall conclusion:
    [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
     (1) what the evidence says about the hypothesis, (2) which side is stronger and why,
     (3) the single largest gap -- what a follow-up investigation should address.
     Close with: evidence is [strong / weak / mixed / insufficient] that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, balance_result,
             refinement_count.
```

---

## Round 1 Design Notes

### Criteria coverage by variation

| Criterion | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
|-----------|------|------|------|------|------|------|------|------|------|------|
| V-01 | field | Quote: field | template blocks | Relevance: field | Strength: field | "at least 2 searches" rule | SYNTHESIS table | Credibility: field | SYNTHESIS section | not addressed |
| V-02 | rule header | "copy a quote" imperative | step format | Relevance step | Strength step | Q1/Q2/Q3 planning step | Balance check step | Source type step | synthesis paragraph | query list pre-planned |
| V-03 | gate rule | Quote: field | SEARCH block | Relevance: field | Strength: field | GATE 1 (2 queries) | GATE 3 (balance) | Credibility: field | PHASE 4 synthesis | not explicitly addressed |
| V-04 | rule header | Quote: field | SEARCH BLOCK per query | Relevance: field | Strength: field | GATE 1 | GATE 3 | Credibility: field | PHASE 4 synthesis | refinement note in PHASE 4 |
| V-05 | rule header | Quote: field | SEARCH BLOCK per query | Relevance: field | Strength: field | GATE 1 | GATE 3 | Credibility: field | PHASE 4 named sub-fields | PHASE 3 pre-printed trail |

### C-10 placement rationale

Query refinement trail lives in PHASE 3 (V-05) rather than PHASE 4 because refinement happens
*during* the search process, not after synthesis. Placing the trail at the BALANCE CHECK phase --
where the model has all search results but has not yet written synthesis -- is the only point
where iterative query behavior is visible and documentable. Post-synthesis placement (V-04)
forces a retrospective that may be reconstructed rather than observed.

### Predicted differentiation

| Dimension | Strongest | Reasoning |
|-----------|----------|-----------|
| C-01/C-02 structural enforcement | V-01/V-04/V-05 | Template Quote: field beats rule prose |
| C-06/C-07 structural enforcement | V-03/V-04/V-05 | Phase gates beat instructions |
| C-10 placement accuracy | V-05 | PHASE 3 captures live refinement; PHASE 4 is retrospective |
| Template overhead | V-02 | Pure imperative prose, minimal structure |
| C-08 coverage | V-01/V-04/V-05 | Credibility: field in every evidence block |

### V-golden candidate

**V-05** is the direct synthesis target: every criterion has a structural home, no criterion
is left to prose instruction alone. **V-04** is the closest competitor -- missing only the
pre-printed synthesis sub-fields (C-09) and the PHASE 3 refinement trail placement (C-10).
Key open question for live runs: does the PHASE 3 refinement trail placement in V-05 produce
more accurate trail documentation than V-04's PHASE 4 note? If models reconstruct rather than
observe, the placement advantage may be negligible.
