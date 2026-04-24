Written to `simulations/quest/variations/prove-websearch-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — prove-websearch

**5 variations across 3 single-axis + 2 combined:**

| V | Axis | C-11 | C-12 | C-13 | C-14 | C-15 | Key mechanism |
|---|------|------|------|------|------|------|---------------|
| V-01 | Output format | -- | -- | -- | PASS | PASS | Evidence in markdown tables; empty cells visually salient |
| V-02 | Phrasing register | -- | PASS | borderline | PASS | PASS | RFC 2119 MUST/SHALL; R-08 mandates sub-fields; R-09 mandates search-phase trail |
| V-03 | Inertia framing | PASS | PASS | PASS | PASS | PASS | Q2 = "NULL HYPOTHESIS ATTACK" + target declaration gate |
| V-04 | Inertia + format | PASS | PASS | PASS | PASS | PASS | Null attack + evidence tables + phase gates |
| V-05 | Full R2 synthesis | PASS | PASS | PASS | PASS | PASS | All axes + per-search trail in PHASE 2 SEARCH BLOCK |

---

**Three R2 innovations over R1-V-05:**

1. **Null hypothesis attack framing** (V-03+) — Q2 is renamed "NULL HYPOTHESIS ATTACK" with a required **target declaration**: one sentence naming what falsifying evidence looks like before the search runs. This closes the loophole where "refuting framing" allows a model to search for qualifications rather than genuine falsifiers. R1's gate said "Q2 explicitly targets the refutation side." R2's gate says "target declaration names a specific falsifying result."

2. **Evidence tables** (V-01+) — evidence stored in markdown tables (`Source URL | Credibility | Quote | Relevance | Strength`). An empty `Quote` column cell is more visually disruptive than a missing labeled line in a vertical block. Tests whether table format improves C-02 verbatim compliance.

3. **Per-search refinement trail** (V-03/V-04/V-05) — R1-V-05 placed the refinement trail in PHASE 3 (post-collection). R2-V-05 places it inside each individual SEARCH BLOCK in PHASE 2, capturing adjustment at the exact moment each search returns results — one phase earlier than R1's most live placement.

**Predicted scores:** V-01 ~94/110, V-02 ~104-106/110, V-03/V-04/V-05 target 110/110. V-01 and V-02 are single-axis tests; they deliberately sacrifice C-11 (no "do not proceed" gates) to isolate their axes.

**Key open question for live runs:** Does "NULL HYPOTHESIS ATTACK" + target declaration produce measurably better adversarial coverage than R1's "refutation side" framing? If yes, V-03 achieves 110/110 without table overhead. If no, V-05 (tables + null attack) is the ceiling.
 open question is whether the "null hypothesis attack" label + target declaration produces better adversarial coverage than R1's "refutation side" framing. If adversarial coverage improves, C-07 shifts from PARTIAL-pass to PASS with less structural scaffolding (V-03 vs V-04 gap).

---

## V-01: Evidence Markdown Tables

**Axis:** Output format -- evidence stored in markdown tables, not vertical block fields. Column
headers (Source URL | Credibility | Quote | Relevance | Strength) enforce field presence
structurally. An empty cell is visually disruptive in a way that a missing labeled line in a
prose block is not.
**Hypothesis:** Table columns enforce C-02 (Quote column), C-04 (Relevance column), C-05
(Strength column), and C-08 (Credibility column) by structural position. A model filling a
table row cannot satisfy the format without populating every column. Pre-printed synthesis
sub-fields (Convergence/Conflict/Conclusion) enforce C-14. Rules-first ordering enforces C-15.
Tests whether table format alone -- without phase gates -- can approach V-03/V-04 coverage
on essential and recommended criteria.

```
You are running /prove:websearch.

Rules (apply throughout -- read before proceeding):
  1. Every factual claim must have a URL retrieved in this session.
     Do not use training data as evidence. No URL = no claim.
  2. Evidence is verbatim text in quotation marks attributed to its source URL.
     If you paraphrase, label it "Paraphrase:" and still provide the source URL.
  3. Run at least 2 searches with distinct query framings (one supporting, one refuting).
  4. Fill in every table cell. Empty cells are disallowed.

Topic:      {topic}
Hypothesis: {hypothesis}

---

For each search, use the following structure:

### SEARCH [N]

**Query string:** [Exact text submitted to the search engine]

**Sources found:**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text from source -- in double quotation marks -- do not paraphrase]" | [supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?] | [strong / weak / mixed] -- [one sentence: why this rating?] |

(Add one row per source retrieved from this search. Every column is required.)

---

Repeat SEARCH blocks until you have at least 2 searches with distinct framings.

---

### SYNTHESIS

**Evidence inventory:**

| Source URL | Relevance | Strength |
|------------|-----------|----------|
| [URL] | [supports / refutes / mixed] | [strong / weak / mixed] |

**Balance check:**
  [ ] BALANCED -- at least one supporting AND one refuting/mixed source in inventory above
  [ ] ONE-SIDED ([supporting/refuting] only). Targeted follow-up query:
      Query: [exact string targeting missing side]
      Result: [title -- URL, or "no sources found after targeted search"]

**Convergence:**
  [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

**Conflict:**
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  all [N] sources point [direction]; credibility variation noted."]

**Conclusion:**
  [One paragraph. Name at least two sources by URL. State aggregate verdict:
  evidence is [strong / weak / mixed / insufficient] that {hypothesis restatement}.
  Do not introduce claims without URLs.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count.
```

---

## V-02: RFC Normative Register (MUST/SHALL)

**Axis:** Phrasing register -- all constraints expressed as RFC 2119 normative requirements
(MUST, SHALL, MUST NOT). No procedural instructions, no phase gates, no template blocks -- pure
declarative requirements enumerated before content. Every criterion has a normative rule.
**Hypothesis:** RFC 2119 vocabulary creates a different compliance register than imperative prose
("copy the exact text") or gate structures ("do not proceed"). "The output MUST contain a
verbatim quote" states a requirement as a binary condition with no escape path. Tests whether
normative language alone -- without structural scaffolding -- achieves comparable coverage to
phase gates + pre-printed fields. Also tests C-12 (live trail placement) and C-14 (synthesis
sub-fields) via normative mandates rather than pre-printed slots.

```
You are running /prove:websearch.

RULES (RFC 2119 normative -- these are requirements, not guidance):

  R-01  Every factual claim in the output MUST be grounded in a URL retrieved during
        this session. Training-data knowledge MUST NOT be used as evidence.
        A claim without a URL is invalid and MUST NOT appear in the output.

  R-02  Evidence MUST be a verbatim quotation in double quotation marks attributed to
        its source URL. Paraphrase, if used, MUST be labeled "Paraphrase:" and MUST
        carry its source URL.

  R-03  The output MUST contain at least two search records, each with three fields:
        (a) the exact query string, (b) the list of sources found, (c) evidence extracted.

  R-04  For each evidence item, the output MUST state how the evidence relates to the
        hypothesis using the label [supports / refutes / mixed] followed by one sentence.

  R-05  For each evidence item, the output MUST include a strength rating [strong / weak /
        mixed] with a one-sentence justification.

  R-06  At least one search MUST target evidence supporting the hypothesis. At least one
        search MUST target evidence refuting the hypothesis. If only one side is found,
        the output MUST document a targeted follow-up query for the missing side.

  R-07  Each source MUST carry a credibility label:
        [peer-reviewed / industry report / news outlet / blog / forum / other].

  R-08  The synthesis section MUST contain three named sub-fields in this order:
        Convergence:, Conflict:, and Conclusion:. Each sub-field MUST be populated.
        A single undivided paragraph does not satisfy R-08.

  R-09  If any query was refined during the investigation, the refinement MUST be
        documented inside the search record where the refinement occurred -- not in a
        post-synthesis retrospective. Documentation MUST show: (a) the original planned
        query, (b) the gap observed, (c) the adjusted query used.

Topic:      {topic}
Hypothesis: {hypothesis}

---

### SEARCH [N]

Query:      [Exact query string submitted to the search engine -- per R-03(a)]

Sources:    [List of sources found -- per R-03(b)]
  1. [Title] -- [URL]
  2. [Title] -- [URL]

Evidence:   [Extracted from each source -- per R-03(c)]

  Source URL:   [URL -- per R-01]
  Credibility:  [label per R-07]
  Quote:        "[Verbatim text in double quotation marks -- per R-02]"
  Relevance:    [supports / refutes / mixed] -- [one sentence -- per R-04]
  Strength:     [strong / weak / mixed] -- [one sentence -- per R-05]

  Query refinement (per R-09):
    Planned query:  [Q string as originally designed]
    Gap observed:   [what the results revealed was missing -- or "none"]
    Adjusted to:    [refined query string -- or "no adjustment, ran as planned"]

(Repeat SEARCH block for each query. Minimum two searches per R-03.)

---

### SYNTHESIS

Convergence:
  [Where two or more sources agree on the hypothesis. Cite at least two URLs. Per R-08.]

Conflict:
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  [one-sentence note on directionality and credibility spread]." Per R-08.]

Conclusion:
  [One paragraph. Name at least two sources by URL. State aggregate verdict:
  evidence is [strong / weak / mixed / insufficient] that {hypothesis restatement}. Per R-08.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count.
```

---

## V-03: Null Hypothesis Attack Framing

**Axis:** Inertia framing -- Q2 is renamed from "refuting framing" to "NULL HYPOTHESIS
ATTACK" and requires a **target declaration**: one sentence naming what falsifying evidence
would look like before the search runs. The GATE for query design checks that the target
declaration is present, not just that Q2 has "distinct framing."
**Hypothesis:** "Refuting framing" allows a model to search for qualifications, hedges, or
limitations without finding genuine falsifiers. "NULL HYPOTHESIS ATTACK" with a target
declaration forces the model to commit to what falsification looks like before querying. This
closes the loophole where two slightly different pro-hypothesis queries satisfy C-06 ("distinct
framing") while C-07 (balanced evidence) scores PARTIAL because no genuine falsifier was sought.
Tests whether inertia framing alone -- without table format -- can achieve C-13 and improve C-07.
Baseline structure is phase-gated (R1 excellence signal carried forward) to isolate the inertia
axis.

```
You are running /prove:websearch.

Rules (read before proceeding):
  1. Every factual claim must have a URL from this session. No training data as evidence.
  2. Evidence is verbatim text in quotation marks. Label paraphrases "Paraphrase:" + URL.
  3. Fill in every pre-printed field. Do not skip or rename any field or section header.
  4. Every GATE must fire before the next phase begins.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## PHASE 1: QUERY DESIGN
[Plan all queries before running any searches.]

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking evidence that FALSIFIES the hypothesis --
            not qualifications or hedges, but evidence the hypothesis is wrong]
    Target declaration: [One sentence: what specific evidence would this search return
                         that would falsify the hypothesis?
                         Example: "A study showing X does NOT produce Y under conditions Z."]

  Q3 (domain/technical):
    Query: [additional angle, or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 is present with a target declaration that names a falsifying
        result -- not a qualification or hedge. Do not proceed to PHASE 2 until this gate
        is met.

---

## PHASE 2: EVIDENCE COLLECTION
[Run each query from PHASE 1. One block per query. Every field is required.]

### Query: [Q1 / Q2 NULL HYPOTHESIS ATTACK / Q3 -- label each]

  Query string:   [Exact text submitted to the search engine]

  Sources:
    1. [Title] -- [URL]
    2. [Title] -- [URL]

  Evidence:
    Source URL:   [URL]
    Credibility:  [peer-reviewed / industry report / news outlet / blog / forum / other]
    Quote:        "[Exact verbatim text from the source in double quotation marks.
                   Do not paraphrase. Apply Rule 2.]"
    Relevance:    [supports / refutes / mixed] -- [one sentence linking to hypothesis]
    Strength:     [strong / weak / mixed] -- [one sentence justification]

  (Repeat Evidence block for each additional source from this query.)

  Query refinement:
    Planned query:  [Q string from PHASE 1]
    Gap observed:   [what was missing after seeing results -- or "none"]
    Adjusted to:    [refined query string -- or "ran as planned"]

(Repeat this section for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: All PHASE 1 queries have been run. Every Evidence block has all fields. Every
        query has a refinement entry. Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK
[Review evidence before synthesis. If one side is missing, run a targeted follow-up now.]

  Supporting count:  [N] -- URLs: [list]
  Refuting count:    [N] -- URLs: [list]
  Mixed count:       [N] -- URLs: [list]

  Null hypothesis verdict:
    Did the NULL HYPOTHESIS ATTACK query (Q2) find falsifying evidence?
    [YES -- describe what was found and why it falsifies the hypothesis]
    [NO  -- describe what was found instead; note how it affects the hypothesis status]

  Balance result:
    [BALANCED -- at least one supporting AND one refuting/mixed source above]
    OR
    [ONE-SIDED ([side] only). Targeted follow-up:
       Follow-up query: [exact string targeting the missing side]
       Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Null hypothesis verdict is completed. Do not proceed to PHASE 4 until this
        gate is met.

---

## PHASE 4: SYNTHESIS
[Write after GATE 3. Reference sources by URL. No new claims without URLs.]

  Convergence:
    [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

  Conflict:
    [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
    all [N] sources point [direction]; credibility variation: [brief note]."]

  Conclusion:
    [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
     (1) what the aggregate evidence says about the hypothesis,
     (2) whether the null hypothesis attack found falsifying evidence (YES/NO + one sentence),
     (3) the single largest gap for a follow-up investigation.
     Close with: evidence is [strong / weak / mixed / insufficient]
     that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result.
```

---

## V-04: Null Hypothesis Attack + Evidence Tables (Axes 3+1)

**Axes:** Inertia framing (null hypothesis attack + target declaration) + Output format
(evidence in markdown tables).
**Hypothesis:** Null hypothesis framing (V-03 axis) closes the adversarial coverage loophole
for C-07 and C-13. Table format (V-01 axis) structurally enforces C-02/C-04/C-05/C-08 by
making empty cells visually disruptive. Together, the two mechanisms address the most common
failure patterns: model treats Q2 as a mild qualifier (inertia axis) and model paraphrases
evidence without flagging it (format axis). Phase gates from R1 are retained (R1 excellence
signal). Tests whether null attack + table is sufficient for golden + C-11-C-15 without the
full V-05 synthesis investment.

```
You are running /prove:websearch.

Rules (read before proceeding):
  1. Every factual claim must have a URL from this session. No training data as evidence.
  2. Evidence is verbatim text in double quotation marks attributed to its source URL.
     Paraphrases must be labeled "Paraphrase:" and carry a URL.
  3. Fill in every table cell and pre-printed field. Empty cells are disallowed.
  4. Every GATE must fire before the next phase begins.
  5. Q2 is the NULL HYPOTHESIS ATTACK -- it searches for evidence that FALSIFIES the
     hypothesis. Name what falsifying evidence looks like before running Q2.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## PHASE 1: QUERY DESIGN

| ID | Framing | Query string |
|----|---------|-------------|
| Q1 | Support | [query seeking evidence FOR the hypothesis] |
| Q2 | NULL HYPOTHESIS ATTACK | [query seeking evidence that FALSIFIES the hypothesis] |
| Q3 | Domain/technical | [additional angle -- or "merged with Q[N]: [reason]"] |

Q2 target declaration:
  [One sentence: what specific evidence would Q2 return that falsifies the hypothesis?]

GATE 1: Q2 is present. Target declaration names a falsifying result (not a hedge or
        qualification). Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION

### Search: Q[N] ([Support / NULL HYPOTHESIS ATTACK / Domain label])

**Query string:** [Exact text submitted to the search engine]

**Sources found:**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text in double quotation marks -- do not paraphrase]" | [supports / refutes / mixed] -- [one sentence: link to hypothesis] | [strong / weak / mixed] -- [one sentence: justification] |

(Add one row per source. Every column required. Apply Rule 2 to every Quote cell.)

**Query refinement:**
  Planned:      [Q string from PHASE 1]
  Gap observed: [what was missing after results returned -- or "none"]
  Adjusted to:  [refined string -- or "ran as planned"]

(Repeat Search section for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a Search section with all table cells filled and a
        refinement entry completed. Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK

| Side | Count | Source URLs |
|------|-------|-------------|
| Supporting | [N] | [list] |
| Refuting | [N] | [list] |
| Mixed | [N] | [list] |

Null hypothesis verdict:
  [Did Q2 find evidence that falsifies the hypothesis? YES / NO]
  [One sentence: what did Q2 find, and does it support or undermine the hypothesis?]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source above]
  OR
  [ONE-SIDED ([side] only). Targeted follow-up:
     Follow-up query: [exact string targeting missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Null hypothesis verdict is completed. Do not proceed to PHASE 4 until met.

---

## PHASE 4: SYNTHESIS

Convergence:
  [Where two or more sources agree. Cite at least two URLs.]

Conflict:
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  all [N] sources align; credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two sources by URL. State aggregate verdict:
  evidence is [strong / weak / mixed / insufficient] that {hypothesis restatement}.
  Include whether the null hypothesis attack succeeded or failed.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result.
```

---

## V-05: Full R2 Synthesis (All Axes)

**Axes:** Phrasing register (RFC-numbered rules) + Output format (evidence tables) + Inertia
framing (null hypothesis attack + target declaration) + Lifecycle emphasis (4-phase gates) +
Role sequence (rules parsed before content fields).
**Hypothesis:** R2 full synthesis incorporates every structural mechanism identified across R1
and R2 single-axis experiments. RFC-numbered rules before content fields ensures constraints are
parsed before topic and hypothesis are seen (C-15). Null hypothesis attack gate with target
declaration names the adversarial target precisely (C-13). "Do not proceed" gates enforce
multi-query and balance requirements (C-11). Per-search refinement trail in PHASE 2 SEARCH BLOCK
captures adjustment at the moment of observation -- one phase earlier than R1-V-05 (C-12).
Evidence tables make empty Quote cells visually salient (C-02 structural). Pre-printed synthesis
sub-fields require three distinct sub-answers (C-14). Key R2 innovations over R1-V-05: (1) null
attack framing sharpens adversarial gate beyond "refutation side", (2) evidence tables replace
vertical blocks, (3) refinement trail moved from PHASE 3 into PHASE 2 per-search.

```
You are running /prove:websearch.

RULES (read before proceeding -- apply to all phases):
  1. Every factual claim MUST have a URL retrieved in this session.
     Training-data knowledge is NOT evidence. No URL = no claim.
  2. Evidence is a verbatim quotation in double quotation marks attributed to its source URL.
     If you paraphrase, label it "Paraphrase:" and still provide the URL.
  3. Fill in every pre-printed field and table cell. Skipping or renaming any field
     is a violation of the output contract.
  4. Every GATE must fire before its next phase begins. "Do not proceed" means stop.
  5. Q2 is the NULL HYPOTHESIS ATTACK. It searches for evidence that FALSIFIES the
     hypothesis -- not qualifications, not hedges, but evidence the hypothesis is wrong.
     You MUST declare what falsifying evidence looks like before running Q2.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## PHASE 1: QUERY DESIGN

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking evidence that FALSIFIES the hypothesis]
    Target declaration: [One sentence: what specific evidence would Q2 return that
                         would falsify the hypothesis? Name the falsifying result,
                         not a category of doubt.]

  Q3 (domain/technical):
    Query: [additional angle -- or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 is present AND its target declaration names a specific
        falsifying result (not a hedge or qualification). Rule 5 is met.
        Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION

[Run each query from PHASE 1. One SEARCH BLOCK per query. Fill every table cell.]

### SEARCH BLOCK: Q[N] ([Support / NULL HYPOTHESIS ATTACK / Domain -- label each])

**Query string:** [Exact text submitted to the search engine]

**Sources found:**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" | [supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?] | [strong / weak / mixed] -- [one sentence: why this rating?] |

(Add one row per source retrieved. Every column required. Apply Rules 1-3 to every row.)

**Query refinement trail (complete for every SEARCH BLOCK):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK with all table cells filled AND a
        completed refinement trail entry. Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK

| Side | Count | Source URLs |
|------|-------|-------------|
| Supporting | [N] | [list] |
| Refuting | [N] | [list] |
| Mixed | [N] | [list] |

Null hypothesis verdict:
  [Did the NULL HYPOTHESIS ATTACK query (Q2) find falsifying evidence?]
  [YES -- one sentence: what evidence was found and why it falsifies the hypothesis]
  [NO  -- one sentence: what was found instead and what this means for the hypothesis]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Null hypothesis verdict is completed.
        Do not proceed to PHASE 4 until both fields are complete.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

Convergence:
  [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

Conflict:
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  all [N] sources point [direction]; credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
   (1) what the aggregate evidence says about the hypothesis,
   (2) whether the null hypothesis attack found falsifying evidence (YES/NO + one sentence),
   (3) the single largest remaining gap for a follow-up investigation.
   Close with: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result,
             refinement_count.
```

---

## Round 2 Design Notes

### Criteria coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | rule header | R-01 MUST | rule header | rule header | rule header (R-01 style) |
| C-02 | Quote column (table) | R-02 MUST + Quote: field | Quote: field | Quote column (table) | Quote column (table) |
| C-03 | SEARCH block: query + sources table + evidence table | R-03 MUST | SEARCH block: all fields | SEARCH block + tables | SEARCH BLOCK + tables |
| C-04 | Relevance column (table) | R-04 MUST + Relevance: | Relevance: field | Relevance column | Relevance column |
| C-05 | Strength column (table) | R-05 MUST + Strength: | Strength: field | Strength column | Strength column |
| C-06 | "at least 2 searches" rule | R-03 MUST (2 searches) + R-06 refuting MUST | GATE 1 (Q1+Q2 required) | GATE 1 | GATE 1 |
| C-07 | Balance check section (ungated) | R-06 MUST (one search per side) | GATE 3 (BALANCED or ONE-SIDED documented) | GATE 3 | GATE 3 |
| C-08 | Credibility column (table) | R-07 MUST + Credibility: | Credibility: field | Credibility column | Credibility column |
| C-09 | Convergence/Conflict/Conclusion sub-fields | R-08 MUST + named sub-fields | Convergence/Conflict/Conclusion | Convergence/Conflict/Conclusion | Convergence/Conflict/Conclusion |
| C-10 | not addressed | R-09 MUST (in search phase) | refinement: field in each query block | refinement: in each SEARCH | refinement trail in each SEARCH BLOCK |
| C-11 | no "do not proceed" gates | no explicit gates (MUST rules only) | GATE 1/2/3 with "do not proceed" | GATE 1/2/3 with "do not proceed" | GATE 1/2/3 with "do not proceed" |
| C-12 | not addressed | R-09 mandates search-phase trail | refinement in PHASE 2 query block | refinement in PHASE 2 SEARCH | refinement trail in PHASE 2 SEARCH BLOCK |
| C-13 | no Q2 target naming | R-06 requires refuting search but no Q2 naming | GATE 1: "target declaration names falsifying result" | GATE 1: target declaration | GATE 1: null attack target declaration |
| C-14 | Convergence/Conflict/Conclusion labeled fields | R-08 mandates three named sub-fields | Convergence/Conflict/Conclusion | Convergence/Conflict/Conclusion | Convergence/Conflict/Conclusion |
| C-15 | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis | Rules block before Topic/Hypothesis | Rules block before Topic/Hypothesis | RULES (numbered) before Topic/Hypothesis |

### R2 key innovation: per-search refinement trail

R1-V-05 placed the refinement trail in PHASE 3 (balance check -- post-collection, pre-synthesis).
R2-V-03/V-04/V-05 place the refinement trail inside each individual SEARCH BLOCK in PHASE 2.
This is one phase earlier: the trail is captured immediately after each individual search returns
results, before moving to the next query. This is the most live placement possible -- the model
documents adjustment at the exact moment the gap is visible, not after all searches complete.
Whether this produces better documentation quality than PHASE 3 placement is the R2 open question.

### C-11 gap in V-01 and V-02

V-01 (table format) has no "do not proceed" gates. V-02 (RFC normative) has MUST rules but no
explicit gate blocks. C-11 requires "GATE: do not proceed" checkpoints specifically. RFC MUST
language may satisfy the spirit of C-11 but not the letter. This gap is deliberate -- V-01 and
V-02 are single-axis variations testing whether table structure and normative language can reach
golden without gate overhead.

### Predicted scores under v2 rubric

| V | Essential (60) | Recommended (30) | C-09/C-10 (10) | C-11-C-15 (10) | Total |
|---|----------------|------------------|----------------|----------------|-------|
| V-01 | 60 | ~25 (C-07 ungated -- PARTIAL) | 5 + 0 | 0+0+0+2+2 | ~94 |
| V-02 | 60 | ~28 (C-06/C-07 MUST borderline -- no gate) | 5 + 5 | 0+2+0/2+2+2 | ~104-106 |
| V-03 | 60 | 30 | 5 + 5 | 2+2+2+2+2 | 110 |
| V-04 | 60 | 30 | 5 + 5 | 2+2+2+2+2 | 110 |
| V-05 | 60 | 30 | 5 + 5 | 2+2+2+2+2 | 110 |

V-01 likely misses C-10/C-12 (no refinement trail) and C-11 (no gates). C-07 is ungated, likely
PARTIAL. Estimated 94/110.

V-02 likely misses C-11 (MUST rules are not "do not proceed" gates) and C-13 (R-06 requires a
refuting search but does not name Q2 as a null attack target). Estimated 104-106/110.

V-03/V-04/V-05 all target 110/110 via distinct structural paths. Differentiation between them:
V-05 adds evidence tables on top of V-03's structure; V-04 tests the combination without V-03's
full phase prose overhead. Key open question: does V-03's vertical fields vs V-05's table format
produce different C-02 compliance rates under live execution?

### V-golden candidate

**V-05** and **V-03** are the R2 direct synthesis targets -- both address all 15 criteria.
V-05 adds evidence table format on top of V-03's null attack + phase gate structure. V-04 tests
the same combination with a slightly compressed structure. Key open question for live runs:
does the null hypothesis attack label + target declaration (V-03+) produce measurably better
adversarial coverage than R1's "refutation side" framing (R1-V-05)? If YES, V-03/V-04/V-05 will
out-score R1-V-05 on C-07 with less structural scaffolding. If NO, the naming difference is
cosmetic and R1-V-05 + table format is the ceiling.
