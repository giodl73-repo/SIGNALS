Written to `simulations/quest/variations/prove-websearch-variations-R3-2026-03-14.md`.

---

## Round 3 Variations Summary

**5 variations, 3 single-axis + 2 combined, targeting C-16/C-17/C-18:**

| V | Axis | C-16 | C-17 | C-18 | Predicted |
|---|------|------|------|------|-----------|
| V-01 | Phrasing register | PASS | PASS | -- | ~110-112 |
| V-02 | Lifecycle emphasis | PASS | borderline | PASS | ~115-116 |
| V-03 | Role sequence | PASS+ | borderline | borderline | ~114-116 |
| V-04 | Lifecycle + phrasing | PASS | PASS | PASS | ~116 |
| V-05 | Full R3 synthesis | PASS+ | PASS | PASS | ~116 |

---

**Three R3 mechanisms:**

**C-17 (unconditional refinement):** V-01 adds `R-09 MUST be completed for every SEARCH record, unconditionally -- including when no refinement occurred.` V-04/V-05 add `Rule 6` to the RULES block with `"no exceptions"` + `"Omitting or skipping this field is a Rule 3 violation"`. The gap in R2 was that GATE 2's "every query has a refinement entry" was ambiguously conditional.

**C-18 (verdict propagation):** V-02/V-04/V-05 pull the null-attack verdict out of the Conclusion paragraph into a standalone `Null-Attack Verdict: [YES / NO / INCONCLUSIVE]` field that appears *before* Convergence in PHASE 4. R2 embedded it as item "(2)" in a prose paragraph template where it could be absorbed into narrative.

**C-16 sharpening:** V-03/V-05 add a `FALSIFICATION PRE-COMMIT` block as GATE 0, before query design. The model commits to the specific falsification event before seeing the query template -- front-loading adversarial commitment structurally, one step earlier than R2's GATE 1 target declaration.

**Key open question:** Does the PRE-COMMIT block (V-03/V-05) produce better Q2 quality than the GATE 1 target declaration (V-02/V-04)? If yes, V-05 is golden. If no, V-04 achieves 116/116 with less overhead.
bed into prose. C-18 pass
   condition requires a "required field or instruction that forces an explicit null hypothesis
   verdict." R3 pulls this into a standalone "Null-Attack Verdict: [YES / NO / INCONCLUSIVE]"
   field that appears *before* Convergence in PHASE 4 SYNTHESIS -- a dedicated decision artifact
   at the synthesis level, not a sub-point in a paragraph template.

3. **Falsification pre-commit block** (V-03, V-05) -- R2's target declaration lived inside GATE 1
   as part of Q2 query design. By the time the model writes the target declaration, it has already
   seen the hypothesis and (for some models) partially primed support framing while planning Q1.
   R3 adds a FALSIFICATION PRE-COMMIT block as GATE 0 -- before PHASE 1 query design. The model
   must commit to (a) the hypothesis in domain terms, (b) the falsification event (specific
   contrary result), (c) the null hypothesis -- before seeing the query template. GATE 1 then
   requires Q2's target declaration to match the PRE-COMMIT event. This front-loads adversarial
   commitment structurally, at the earliest possible point.

---

**Predicted scores under v3 rubric (max 116):**

| V | C-01 to C-15 | C-16 | C-17 | C-18 | Total |
|---|-------------|------|------|------|-------|
| V-01 | ~108 (lacks C-11, C-07 borderline) | +2 | +2 | 0 | ~110-112 |
| V-02 | ~112-114 (R2 V-03 base) | +2 | +1 | +2 | ~115-116 |
| V-03 | ~112-114 (R2 V-03 + GATE 0) | +2 | +1 | +1 | ~114-116 |
| V-04 | ~112-114 (R2 V-05 base) | +2 | +2 | +2 | ~116 |
| V-05 | ~112-114 (all R2 + R3) | +2 | +2 | +2 | ~116 |

**Key open question for live runs:** Does the FALSIFICATION PRE-COMMIT block (V-03/V-05) produce
measurably better adversarial search quality than GATE 1 target declaration alone (V-02/V-04)?
If Q2 produces stronger genuine falsifiers when the model committed to the falsification event
before seeing the query template, V-05 outscores V-04 on C-07 (balanced evidence) in live runs.
If not, V-04 achieves the same score with less structural overhead.

---

## V-01: Unconditional Refinement Mandate (RFC Normative Register)

**Axis:** Phrasing register -- R-09 replaced with an unconditional MUST mandate; R-10 added for
explicit target declaration. Base structure is R2 V-02 (RFC 2119 normative), extended to close
C-17 (conditional escape) and sharpen C-16 (named target). No phase gates; pure normative rules.
**Hypothesis:** A normative rule-block that says "MUST be completed for every SEARCH record,
unconditionally -- 'ran as planned' when unchanged, omitting is invalid" closes C-17 without
phase gate overhead. Adding R-10 (target declaration naming a specific falsifying result) closes
C-16 via normative instruction rather than a gate check. Tests whether RFC-style normative rules
can reach ~112/116 without structural phase scaffolding -- and identifies C-18 as the remaining
gap (no dedicated verdict field in synthesis).

```
You are running /prove:websearch.

RULES (RFC 2119 normative -- apply to all phases):

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
        search MUST target evidence refuting the hypothesis (the null hypothesis attack).
        If only one side is found, the output MUST document a targeted follow-up query.

  R-07  Each source MUST carry a credibility label:
        [peer-reviewed / industry report / news outlet / blog / forum / other].

  R-08  The synthesis section MUST contain three named sub-fields in this order:
        Convergence:, Conflict:, and Conclusion:. Each sub-field MUST be populated.
        A single undivided paragraph does not satisfy R-08.

  R-09  The query refinement trail MUST be completed for every SEARCH record,
        unconditionally -- including when no refinement occurred. When the original query
        ran unchanged, the SEARCH record MUST contain exactly:
          Planned query:  [the Q string as originally intended]
          Gap observed:   none
          Adjusted to:    ran as planned
        Omitting the refinement trail from any SEARCH record is a protocol violation
        regardless of whether refinement occurred.

  R-10  The null hypothesis attack query (Q2) MUST include a target declaration that names
        a specific falsifying result before the search runs -- not a category of doubt or
        qualification. The declaration MUST answer: "What would Q2 have to return for the
        hypothesis to be falsified?" A target of "limitations of X" does not satisfy R-10
        unless it names a specific contrary result (e.g., "evidence that X fails to
        achieve Y under condition Z").

Topic:      {topic}
Hypothesis: {hypothesis}

---

### SEARCH [N]

Query:      [Exact query string submitted to the search engine -- per R-03(a)]

Sources:
  1. [Title] -- [URL]
  2. [Title] -- [URL]

Evidence:

  Source URL:   [URL -- per R-01]
  Credibility:  [label per R-07]
  Quote:        "[Verbatim text in double quotation marks -- per R-02]"
  Relevance:    [supports / refutes / mixed] -- [one sentence -- per R-04]
  Strength:     [strong / weak / mixed] -- [one sentence -- per R-05]

  (Repeat Evidence block for each additional source from this search.)

  Refinement trail (required for every SEARCH, unconditionally -- per R-09):
    Planned query:  [Q string as originally intended]
    Gap observed:   [what the results revealed was missing -- or "none"]
    Adjusted to:    [refined query string -- or "ran as planned"]

(For Q2 -- NULL HYPOTHESIS ATTACK -- add target declaration per R-10:)
  Target declaration: [One sentence: what specific falsifying result is Q2 searching for?
                       Example: "Evidence that X does NOT achieve Y under condition Z."]

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
             supporting_count, refuting_count, mixed_count, null_attack_result.
```

---

## V-02: Dedicated Null-Attack Verdict Field (Synthesis Lifecycle Emphasis)

**Axis:** Lifecycle emphasis -- the null hypothesis verdict is pulled OUT of the Conclusion
paragraph template and into a standalone labeled field in PHASE 4, appearing before Convergence.
Base structure is R2 V-03 (null hypothesis attack + phase gates). No changes to query design,
evidence collection, or RULES -- the only change is synthesis phase structure.
**Hypothesis:** R2's best embedded the null attack verdict as item "(2)" in a three-part
Conclusion paragraph instruction. An instruction embedded in prose can be satisfied by a sentence
that mentions the outcome without rendering a crisp binary verdict. A standalone
"Null-Attack Verdict: [YES / NO / INCONCLUSIVE]" field forces a dedicated decision artifact
before Convergence and Conflict are written -- propagating the adversarial result to the decision
point mechanically, not by prose convention. Tests whether C-18 can be achieved by synthesis
structure change alone, with no modification to the upstream phases.

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

  Balance result:
    [BALANCED -- at least one supporting AND one refuting/mixed source above]
    OR
    [ONE-SIDED ([side] only). Targeted follow-up:
       Follow-up query: [exact string targeting the missing side]
       Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: SYNTHESIS
[Write after GATE 3. Reference sources by URL. No new claims without URLs.]

  Null-Attack Verdict:
    [Did the NULL HYPOTHESIS ATTACK query (Q2) find a genuine falsifier of the hypothesis?]
    [YES        -- one sentence: what evidence was found and why it constitutes falsification]
    [NO         -- one sentence: what was found instead, and why it does not falsify]
    [INCONCLUSIVE -- one sentence: what was found and what additional evidence would resolve it]

  Convergence:
    [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

  Conflict:
    [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
    all [N] sources point [direction]; credibility variation: [brief note]."]

  Conclusion:
    [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
     (1) what the aggregate evidence says about the hypothesis,
     (2) reference the Null-Attack Verdict above (do not re-adjudicate),
     (3) the single largest gap for a follow-up investigation.
     Close with: evidence is [strong / weak / mixed / insufficient]
     that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result.
```

---

## V-03: Falsification Pre-Commit Block (Role Sequence Emphasis)

**Axis:** Role sequence -- a FALSIFICATION PRE-COMMIT block appears as the first output step
(GATE 0), before query design. The model must define the falsification event in domain terms
before the query template is visible. GATE 1 then checks that Q2's target declaration matches
the PRE-COMMIT event -- binding the adversarial query to the pre-committed falsification frame.
Base structure is R2 V-03 (phase gates + null attack). No changes to evidence collection or
synthesis structure.
**Hypothesis:** R2's target declaration lived in GATE 1 -- after the model has seen the
hypothesis and is mid-query-design. Support framing (Q1) is designed first, potentially priming
the model's perspective before Q2 is planned. Placing the falsification commitment BEFORE query
design -- at GATE 0 -- forces adversarial thinking as a prerequisite for any query work. GATE 1
then verifies Q2 references the PRE-COMMIT event rather than generating a new (possibly weaker)
target at query-design time. Tests whether earlier adversarial commitment changes Q2 quality.

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

## FALSIFICATION PRE-COMMIT
[Complete this block before designing any queries. This is your adversarial commitment.]

  Hypothesis restated:
    [One sentence: restate the hypothesis in your own words.]

  Falsification event:
    [Describe what the hypothesis predicts in domain-specific terms. Then name the specific
     observable outcome that would prove the prediction wrong.
     Format: "The hypothesis predicts [X]. Falsification = evidence that [NOT X] under [conditions]."
     Do not use "limitations of X" -- name a contrary result.]

  Null hypothesis (one sentence):
    [The hypothesis is wrong because: _____.]

GATE 0: Falsification event is specific -- it names an observable contrary result,
        not a category of doubt or caveat. "Limitations of X" does not satisfy GATE 0.
        "Evidence that X fails to achieve Y in context Z" satisfies GATE 0.
        Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: QUERY DESIGN
[Plan all queries before running any searches.]

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking the falsification event declared in PRE-COMMIT above]
    Target: [Copy the falsification event from PRE-COMMIT here. Q2 is searching for this.]

  Q3 (domain/technical):
    Query: [additional angle, or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 target matches the falsification event from PRE-COMMIT --
        not a restatement of the hypothesis with "limitations" appended.
        Do not proceed to PHASE 2 until this gate is met.

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
    Did Q2 find the falsification event declared in PRE-COMMIT?
    [YES        -- one sentence: what was found and how it matches the falsification event]
    [NO         -- one sentence: what was found instead; why it does not constitute falsification]
    [INCONCLUSIVE -- one sentence: what was found and what would resolve it]

  Balance result:
    [BALANCED -- at least one supporting AND one refuting/mixed source above]
    OR
    [ONE-SIDED ([side] only). Targeted follow-up:
       Follow-up query: [exact string targeting the missing side]
       Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed. Balance result is filled.
        Do not proceed to PHASE 4 until both fields are complete.

---

## PHASE 4: SYNTHESIS
[Write after GATE 3. Reference sources by URL. No new claims without URLs.]

  Convergence:
    [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

  Conflict:
    [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
    all [N] sources point [direction]; credibility spread: [brief note]."]

  Conclusion:
    [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
     (1) what the aggregate evidence says about the hypothesis,
     (2) whether the null hypothesis attack found the falsification event
         (YES / NO / INCONCLUSIVE per PHASE 3 verdict),
     (3) the single largest gap for a follow-up investigation.
     Close with: evidence is [strong / weak / mixed / insufficient]
     that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result.
```

---

## V-04: Unconditional Refinement Mandate + Verdict Field (Axes C-17 + C-18)

**Axes:** Phrasing register (Rule 6 unconditional refinement mandate in RULES block) +
Lifecycle emphasis (Null-Attack Verdict: as 4th dedicated synthesis sub-field). Base is R2 V-05
(tables + null attack + phase gates). Two targeted additions; no structural overhaul.
**Hypothesis:** R2 V-05's two remaining weak points are C-17 (refinement trail was labeled
"complete for every SEARCH BLOCK" but lacked a RULES-level unconditional mandate) and C-18
(verdict was embedded in Conclusion paragraph instruction, not a dedicated field). V-04 closes
both with minimal surgery: Rule 6 adds the unconditional mandate to the RULES block and names
omission as a Rule 3 violation; the dedicated Null-Attack Verdict field in PHASE 4 pulls the
verdict before Convergence. Tests whether these two targeted additions achieve 116/116 without
the structural overhead of the PRE-COMMIT block.

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
  6. The query refinement trail MUST be completed for every SEARCH BLOCK -- no exceptions.
     When the original query ran unchanged, record:
       Gap observed:   none
       Adjusted to:    ran as planned
     Omitting or skipping this field is a Rule 3 violation.

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

**Query refinement trail (Rule 6 -- mandatory for every SEARCH BLOCK):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK with all table cells filled AND a
        completed refinement trail entry (including "ran as planned" entries per Rule 6).
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK

| Side | Count | Source URLs |
|------|-------|-------------|
| Supporting | [N] | [list] |
| Refuting | [N] | [list] |
| Mixed | [N] | [list] |

Null hypothesis verdict:
  [Did the NULL HYPOTHESIS ATTACK query (Q2) find falsifying evidence?]
  [YES        -- one sentence: what was found and why it falsifies the hypothesis]
  [NO         -- one sentence: what was found instead and what this means for the hypothesis]
  [INCONCLUSIVE -- one sentence: what was found and what would resolve it]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Null hypothesis verdict is completed (YES / NO / INCONCLUSIVE).
        Do not proceed to PHASE 4 until both fields are complete.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

Null-Attack Verdict:
  [YES / NO / INCONCLUSIVE]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification.
   Must be consistent with the null hypothesis verdict in PHASE 3.]

Convergence:
  [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

Conflict:
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  all [N] sources point [direction]; credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
   (1) what the aggregate evidence says about the hypothesis,
   (2) the single largest remaining gap for a follow-up investigation.
   Close with: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.
   The Null-Attack Verdict is stated above -- reference it; do not re-adjudicate here.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result,
             refinement_count.
```

---

## V-05: Full R3 Synthesis (All Axes)

**Axes:** Role sequence (FALSIFICATION PRE-COMMIT block, GATE 0) + Phrasing register (Rule 6
unconditional mandate in RULES) + Lifecycle emphasis (Null-Attack Verdict: as 4th synthesis
sub-field) + Output format (evidence tables) + Phase-gate enforcement (GATE 0/1/2/3).
**Hypothesis:** V-05 incorporates every structural mechanism from R1, R2, and R3. Pre-commit
block (V-03 axis) front-loads adversarial commitment before query design. Rule 6 (V-01/V-04 axis)
closes the conditional refinement escape with a RULES-level unconditional mandate. Dedicated
Null-Attack Verdict field (V-02/V-04 axis) propagates the adversarial result to the synthesis
decision point as a standalone artifact. GATE 1 verifies that Q2's target declaration matches
the PRE-COMMIT event, binding query design to the pre-committed falsification frame. Three R3
innovations over R2 V-05: (1) GATE 0 PRE-COMMIT forces adversarial commitment before queries
are designed, (2) Rule 6 closes the silent-skip escape on C-17, (3) dedicated verdict field
closes the disappearing-adversarial-result problem on C-18.

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
     The falsification event MUST be declared in the PRE-COMMIT block before Q2 executes.
  6. The query refinement trail MUST be completed for every SEARCH BLOCK -- no exceptions.
     When the original query ran unchanged, record:
       Gap observed:   none
       Adjusted to:    ran as planned
     Omitting or skipping this field is a Rule 3 violation.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## FALSIFICATION PRE-COMMIT
[Complete before designing any queries.]

  Hypothesis restated:
    [One sentence: restate the hypothesis in your own words.]

  Falsification event:
    [Describe what the hypothesis predicts in domain-specific terms. Then name the specific
     observable outcome that would prove the prediction wrong.
     Format: "The hypothesis predicts [X]. Falsification = evidence that [NOT X] under [conditions]."
     Do not use "limitations of X" -- name a contrary result.]

  Null hypothesis (one sentence):
    [The hypothesis is wrong because: _____.]

GATE 0: Falsification event is specific -- names an observable contrary result.
        "Limitations of X" does not satisfy GATE 0.
        Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: QUERY DESIGN

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking the falsification event declared in PRE-COMMIT]
    Target declaration: [Copy the falsification event from PRE-COMMIT here. Q2 is
                         searching for this specific result. Must match PRE-COMMIT.]

  Q3 (domain/technical):
    Query: [additional angle -- or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 target declaration matches the PRE-COMMIT falsification event.
        Rule 5 is met. Do not proceed to PHASE 2 until this gate is met.

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

**Query refinement trail (Rule 6 -- mandatory, no exceptions):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK. All table cells are filled. Every
        refinement trail is completed (including "ran as planned" entries per Rule 6).
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK

| Side | Count | Source URLs |
|------|-------|-------------|
| Supporting | [N] | [list] |
| Refuting | [N] | [list] |
| Mixed | [N] | [list] |

Null hypothesis verdict:
  Did Q2 find the falsification event declared in PRE-COMMIT?
  [YES        -- one sentence: what was found and why it matches the falsification event]
  [NO         -- one sentence: what was found instead; why it does not constitute falsification]
  [INCONCLUSIVE -- one sentence: what was found and what would resolve it]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed (YES / NO / INCONCLUSIVE).
        Balance result is filled (BALANCED or ONE-SIDED with documented follow-up).
        Do not proceed to PHASE 4 until both fields are complete.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

Null-Attack Verdict:
  [YES / NO / INCONCLUSIVE]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification of the
   PRE-COMMIT event. Must be consistent with PHASE 3 null hypothesis verdict.]

Convergence:
  [Where two or more sources agree on the hypothesis. Cite at least two URLs.]

Conflict:
  [Where sources disagree. Cite at least two URLs. Or: "No material conflict found --
  all [N] sources point [direction]; credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two sources by URL. State:
   (1) what the aggregate evidence says about the hypothesis,
   (2) the single largest remaining gap for a follow-up investigation.
   Close with: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.
   The Null-Attack Verdict is declared above -- reference it; do not re-adjudicate here.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result,
             refinement_count, falsification_event.
```

---

## Round 3 Design Notes

### Criteria coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | R-01 MUST | rule 1 | rule 1 | rule 1 | rule 1 |
| C-02 | R-02 MUST + Quote: field | Quote: field | Quote: field | Quote column (table) | Quote column (table) |
| C-03 | SEARCH block: all three fields | SEARCH block: all three fields | SEARCH block: all three fields | SEARCH BLOCK + tables | SEARCH BLOCK + tables |
| C-04 | R-04 MUST + Relevance: field | Relevance: field | Relevance: field | Relevance column | Relevance column |
| C-05 | R-05 MUST + Strength: field | Strength: field | Strength: field | Strength column | Strength column |
| C-06 | R-06 MUST + R-03 (min 2) | GATE 1 (Q1+Q2 required) | GATE 1 (Q1+Q2) | GATE 1 | GATE 1 |
| C-07 | R-06 MUST (one search per side) | GATE 3 (BALANCED or ONE-SIDED documented) | GATE 3 | GATE 3 | GATE 3 |
| C-08 | R-07 MUST + Credibility: field | Credibility: field | Credibility: field | Credibility column | Credibility column |
| C-09 | Convergence/Conflict/Conclusion | Null-Attack Verdict + 3 sub-fields | Convergence/Conflict/Conclusion | Null-Attack Verdict + 3 sub-fields | Null-Attack Verdict + 3 sub-fields |
| C-10 | R-09 unconditional + Refinement: | refinement: field per query | refinement: field per query | refinement trail per SEARCH BLOCK | refinement trail per SEARCH BLOCK |
| C-11 | no "do not proceed" gates (MUST only) | GATE 1/2/3 "do not proceed" | GATE 0/1/2/3 "do not proceed" | GATE 1/2/3 "do not proceed" | GATE 0/1/2/3 "do not proceed" |
| C-12 | R-09 mandates in-search-record placement | refinement in PHASE 2 query block | refinement in PHASE 2 | refinement in PHASE 2 SEARCH BLOCK | refinement in PHASE 2 SEARCH BLOCK |
| C-13 | R-10 MUST: target names specific falsifying result | GATE 1: target declaration | GATE 0: PRE-COMMIT event + GATE 1 match | GATE 1: target declaration | GATE 0: PRE-COMMIT + GATE 1 match |
| C-14 | Convergence/Conflict/Conclusion labeled fields | 4 sub-fields (verdict + 3) | Convergence/Conflict/Conclusion | 4 sub-fields (verdict + 3) | 4 sub-fields (verdict + 3) |
| C-15 | RULES block before Topic/Hypothesis | Rules block before Topic/Hypothesis | Rules block before Topic/Hypothesis | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis |
| C-16 | R-10 MUST: target declaration names specific falsifying result | GATE 1: target declaration (same as R2 V-03) | PRE-COMMIT falsification event + GATE 1 enforcement (stronger) | GATE 1: target declaration (same as R2 V-05) | PRE-COMMIT + GATE 1 match (strongest) |
| C-17 | R-09 unconditional MUST + "ran as planned" mandatory fill | GATE 2 "every query" + "or 'ran as planned'" (borderline) | GATE 2 "every query" + "or 'ran as planned'" (borderline) | Rule 6 MUST + "no exceptions" + omission = Rule 3 violation | Rule 6 MUST + "no exceptions" + omission = Rule 3 violation |
| C-18 | no dedicated verdict field (FAIL) | Null-Attack Verdict: standalone 4th sub-field (PASS) | verdict in Conclusion "(YES/NO/INCONCLUSIVE per PHASE 3)" (borderline) | Null-Attack Verdict: standalone 4th sub-field (PASS) | Null-Attack Verdict: standalone 4th sub-field (PASS) |

### C-17 gap anatomy

C-17 pass condition: "The refinement trail instruction explicitly requires completion for
every SEARCH block with no conditional or 'if applicable' escape."

R2 V-03/V-05 had GATE 2: "Every query has a refinement entry" and "or 'ran as planned'" as
fill-in options. Close but ambiguous: "every query has a refinement entry" requires a field,
but does not explicitly say "including when no refinement occurred." A strict scorer could read
"refinement entry" as "an entry about what you refined" -- conditional.

R3 V-04/V-05 close this with Rule 6 in the RULES block: "MUST be completed for every SEARCH
BLOCK -- no exceptions. When the original query ran unchanged, record: [exact fill]. Omitting
or skipping this field is a Rule 3 violation." The unconditional mandate is in the RULES block
(parsed before content) and reinforced at the field label "(Rule 6 -- mandatory, no exceptions)."
No scorer ambiguity about conditionality.

R3 V-01 uses R-09 (normative rule) for the same effect, without phase gates. The rule reads
"MUST be completed for every SEARCH record, unconditionally." Same mechanism, different delivery.

### C-18 gap anatomy

C-18 pass condition: "The synthesis or conclusion section contains a required field or
instruction that forces an explicit null hypothesis verdict (YES / NO / INCONCLUSIVE)."

R2 V-03/V-05 had "(2) whether the null hypothesis attack found falsifying evidence
(YES/NO + one sentence)" embedded as item 2 in a three-part Conclusion paragraph template.
A model filling this can write "the null attack found only qualifications, which does not
fully falsify the hypothesis" -- technically mentioning YES/NO as prose, not a binary verdict
field. The adversarial result is absorbed into narrative.

R3 V-02/V-04/V-05 add a standalone "Null-Attack Verdict: [YES / NO / INCONCLUSIVE]" field
before Convergence in PHASE 4. This forces a binary verdict as a dedicated artifact, before
synthesis sub-fields are written. The Conclusion then references it ("reference the Null-Attack
Verdict above -- do not re-adjudicate here"), keeping synthesis clean and ensuring the verdict
is visible at the decision point.

### C-16 sharpening: pre-commit vs gate-time declaration

R2's target declaration was checked at GATE 1, after Q1 was designed. The model designed the
support query first, then wrote the target declaration for Q2. Possible ordering effect: Q1
design primes pro-hypothesis framing before adversarial commitment is required.

R3 V-03/V-05 add GATE 0 PRE-COMMIT before any query design. The model commits to the
falsification event before seeing the query template. GATE 1 then binds Q2's target declaration
to the PRE-COMMIT event -- the adversarial target is not generated fresh at query-design time
but copied from the pre-committed frame. Whether this changes Q2 quality in live runs is the
key empirical question for V-03 vs V-04.

### V-golden candidate for R3

**V-04** and **V-05** are the R3 synthesis targets. Both close C-16, C-17, and C-18
explicitly. V-04 does so with two targeted additions to R2 V-05 (Rule 6 + verdict field).
V-05 adds the PRE-COMMIT block for stronger C-16 and potential Q2 quality improvement.

Key question: does GATE 0 (PRE-COMMIT before query design) produce measurably better
adversarial search results than GATE 1 (target declaration at query-design time)? If YES,
V-05 is the golden candidate. If NO, V-04 achieves 116/116 with less structural overhead
and is the simpler golden.

**V-01** is the RFC normative ceiling test: can declarative MUST rules reach ~110-112/116
without phase gates? If V-01 approaches V-04 scores in live runs, the gate overhead in
V-04/V-05 is not load-bearing and a future R4 could target a hybrid (normative + verdict
field, no gate scaffolding). C-11 FAIL is the expected gap -- if C-11 scores do not
materially affect production behavior, normative-only is the simpler architecture.
