`simulations/quest/variations/prove-websearch-variations-R4-2026-03-14.md` written.

---

**R4 summary — 5 variations, 3 new mechanisms:**

| V | Axis | New mechanism | vs R3 V-05 |
|---|------|---------------|------------|
| V-01 | Phrasing register | Rule 7: verdict copy-forward token mandate | +token field in PHASE 3, copy-forward in PHASE 4 |
| V-02 | Output format | Rule 8: min 2 sources per SEARCH BLOCK | +supplemental search trigger |
| V-03 | Lifecycle emphasis | PHASE 3.5 citation pre-audit + GATE 3.5 | +admissibility registry before synthesis |
| V-04 | Phrasing + output | V-01 + V-02 | 8-rule RULES block |
| V-05 | Full synthesis | V-04 + V-03 + inertia framing in PRE-COMMIT | GATE 0/0.5/1/2/3/3.5 chain |

**The R4 thesis:** R3 V-05 scores 120/122. The remaining 2-pt gap is the PHASE 3 → PHASE 4 verdict chain-of-custody escape: "Must be consistent with PHASE 3" is advisory, not binding. Rule 7 (verdict copy-forward) converts the consistency check to a structural copy-forward mandate — the direct analog of C-21 applied to verdict propagation. If V-01 closes the gap, it's the minimal golden. V-04 is the likely composite golden regardless.
a model can independently re-assess in PHASE 4 and produce a different verdict, technically
violating "must be consistent" without a structural stop. This is the same escape pattern that
C-21 closed for C-16: the PRE-COMMIT → GATE 1 binding was advisory ("matches") until C-21
required copy-forward as the explicit mechanism.

A **verdict-copy-forward-binding** criterion (C-22 candidate) would require PHASE 3 to emit a
standalone verdict token (YES / NO / INCONCLUSIVE -- one word only), and require PHASE 4 to
copy that token verbatim rather than independently render it. GATE 3 enforces token presence;
PHASE 4 template enforces copy-forward at point of use.

Secondary escapes explored in V-02/V-03:
- **Evidence floor**: no minimum source count per SEARCH BLOCK (1-source queries technically satisfy structure)
- **Synthesis citation isolation**: Convergence/Conflict can introduce URLs not present in PHASE 2 evidence tables (new claim injection in synthesis)

---

## V-01: Verdict Copy-Forward Binding (Phrasing Register)

**Axis:** Phrasing register -- Rule 7 added to RULES block mandating that PHASE 4 Null-Attack
Verdict is a verbatim copy of the verdict token rendered in PHASE 3, not an independent
re-assessment. Base: R3 V-05. Single addition.
**Hypothesis:** R3 V-05's "Must be consistent with PHASE 3 null hypothesis verdict" admits silent
re-adjudication -- a model that reached YES in PHASE 3 can write a more hedged verdict in PHASE 4
without violating any structural gate. Rule 7 copy-forward mandate converts the verdict from an
advisory reference to a deterministic carry-through: PHASE 3 emits a standalone token; PHASE 4
copies it. This is the PHASE 3 -> PHASE 4 analog of C-21's PRE-COMMIT -> GATE 1 mechanism.
Adding "Omitting or changing the token is a Rule 3 violation" at RULES level removes the
re-assessment escape entirely.

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
  7. The Null-Attack Verdict in PHASE 4 MUST be the verbatim copy of the "Verdict token:"
     field set in PHASE 3. You may NOT independently re-assess the verdict in PHASE 4.
     The token travels forward unchanged. Omitting or changing the token is a Rule 3 violation.

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

Verdict token: [YES / NO / INCONCLUSIVE]
  [Write only the single matching token. This token is the authoritative verdict.
   It will be copied verbatim to PHASE 4 per Rule 7. Do not change it there.]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed. Verdict token is set to exactly one of
        YES / NO / INCONCLUSIVE. Balance result is filled (BALANCED or ONE-SIDED with
        documented follow-up). Do not proceed to PHASE 4 until all three fields are complete.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

Null-Attack Verdict:
  [Copy the Verdict token from PHASE 3 here verbatim -- per Rule 7. Do not re-assess.]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification of the
   PRE-COMMIT event.]

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

## V-02: Evidence Floor Enforcement (Output Format)

**Axis:** Output format -- Rule 7 added to RULES block requiring a minimum of 2 distinct source
URLs per SEARCH BLOCK. GATE 2 enforces the floor. SEARCH BLOCK Sources table template shows 2
required rows. Base: R3 V-05. Single addition.
**Hypothesis:** R3 V-05 shows a Sources table with rows "1." and "2." as placeholders, but the
instruction "Add one row per source retrieved" allows a 1-row table. A SEARCH BLOCK with a
single source satisfies C-03 (structured search record) and the evidence table structure, but
produces thin evidence that makes cross-source synthesis (C-09) nominally satisfiable from a
single perspective. Rule 7 raises the source floor to 2 per query. If fewer than 2 sources are
found, the model must run a supplemental search and document it. This closes the thin-evidence
escape and ensures C-09 has genuine multi-source material.

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
  7. Each SEARCH BLOCK MUST include at least 2 distinct source URLs in the Sources table.
     A SEARCH BLOCK with only 1 source URL is incomplete. If fewer than 2 sources are found,
     run a supplemental search immediately and document it:
       Supplemental query: [exact string]
       Supplemental source: [title] -- [URL]
     Then include the supplemental source as a row in the Evidence table.
     Omitting the supplemental when only 1 source was found is a Rule 3 violation.

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

**Sources found (minimum 2 per Rule 7):**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

(If only 1 source found, document supplemental before filling Evidence table:
  Supplemental query: [exact string]
  Supplemental source: [title] -- [URL]
 Then add supplemental as row 2 above.)

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" | [supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?] | [strong / weak / mixed] -- [one sentence: why this rating?] |

(Add one row per source. Every column required. Minimum 2 rows per Rule 7.)

**Query refinement trail (Rule 6 -- mandatory, no exceptions):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK. Every SEARCH BLOCK has at least 2 source
        rows in the Sources table (supplemental documented if needed per Rule 7). All table
        cells are filled. Every refinement trail is completed per Rule 6.
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

## V-03: Synthesis Citation Pre-Audit (Lifecycle Emphasis)

**Axis:** Lifecycle emphasis -- a PHASE 3.5 CITATION PRE-AUDIT block is inserted between PHASE 3
and PHASE 4. Before writing any synthesis field, the model produces an admissibility registry
listing every URL from PHASE 2 evidence tables that is eligible for use in Convergence and
Conflict. URLs not in the registry are inadmissible. A gate stops synthesis until the registry
is complete. Base: R3 V-05. Single structural insertion.
**Hypothesis:** R3 V-05 synthesis instructions say "Reference sources by URL. Do not introduce
new claims." This is advisory. A model writing Convergence can cite a URL it read during search
but did not include in the PHASE 2 evidence table, or introduce a plausible-sounding URL not
retrieved in this session. PHASE 3.5 forces the model to construct the admissibility registry
from the evidence tables it already filled -- locking the citation set before synthesis begins.
Convergence and Conflict then operate on a closed set. This closes the new-claim-injection
escape in synthesis that "Do not introduce new claims" alone cannot structurally prevent.

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
        Do not proceed to PHASE 3.5 until both fields are complete.

---

## PHASE 3.5: CITATION PRE-AUDIT

[Construct the admissibility registry before writing any synthesis field.
 Only URLs listed here may be cited in Convergence or Conflict in PHASE 4.
 Any URL not in this registry is inadmissible for synthesis use.]

Admissibility registry:

| URL | SEARCH BLOCK | Row | Relevance | Credibility |
|-----|-------------|-----|-----------|-------------|
| [URL] | Q[N] | [row N in that SEARCH BLOCK Evidence table] | [supports / refutes / mixed] | [credibility label] |

(Add one row per unique URL appearing in PHASE 2 Evidence tables. Copy from those tables -- do
 not add new URLs here. Every URL cited in PHASE 4 Convergence and Conflict MUST appear in
 this registry.)

GATE 3.5: Admissibility registry is populated with every unique URL from PHASE 2 Evidence
          tables. No new URLs were added. Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3.5. Cite only URLs in the admissibility registry. Do not introduce
 new claims or URLs not present in the registry.]

Null-Attack Verdict:
  [YES / NO / INCONCLUSIVE]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification of the
   PRE-COMMIT event. Must be consistent with PHASE 3 null hypothesis verdict.]

Convergence:
  [Where two or more sources agree on the hypothesis. Cite at least two admissible URLs
   (must be in registry from PHASE 3.5).]

Conflict:
  [Where sources disagree. Cite at least two admissible URLs. Or: "No material conflict found --
  all [N] sources point [direction]; credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two admissible sources by URL. State:
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

## V-04: Verdict Copy-Forward + Evidence Floor (Phrasing Register + Output Format)

**Axes:** Phrasing register (Rule 7 verdict copy-forward token mandate) + Output format
(Rule 8 evidence floor, minimum 2 sources per SEARCH BLOCK). Base: R3 V-05.
**Hypothesis:** V-01 closes the PHASE 3->4 verdict chain-of-custody escape; V-02 closes the
thin-evidence escape. Both are independent structural additions to R3 V-05 with no interaction
effects. V-04 combines them to test whether the two targeted additions together reach 122/122
without the citation audit overhead of V-03. If yes, V-04 is the minimal-overhead golden
candidate for R4.

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
  7. The Null-Attack Verdict in PHASE 4 MUST be the verbatim copy of the "Verdict token:"
     field set in PHASE 3. You may NOT independently re-assess the verdict in PHASE 4.
     The token travels forward unchanged. Omitting or changing the token is a Rule 3 violation.
  8. Each SEARCH BLOCK MUST include at least 2 distinct source URLs in the Sources table.
     A SEARCH BLOCK with only 1 source URL is incomplete. If fewer than 2 sources are found,
     run a supplemental search immediately and document it:
       Supplemental query: [exact string]
       Supplemental source: [title] -- [URL]
     Then include the supplemental source as a row in the Evidence table.
     Omitting the supplemental when only 1 source was found is a Rule 3 violation.

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
        Rules 5 and 7 noted. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION

[Run each query from PHASE 1. One SEARCH BLOCK per query. Fill every table cell.]

### SEARCH BLOCK: Q[N] ([Support / NULL HYPOTHESIS ATTACK / Domain -- label each])

**Query string:** [Exact text submitted to the search engine]

**Sources found (minimum 2 per Rule 8):**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

(If only 1 source found, document supplemental:
  Supplemental query: [exact string]
  Supplemental source: [title] -- [URL]
 Then add as row 2 above per Rule 8.)

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" | [supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?] | [strong / weak / mixed] -- [one sentence: why this rating?] |

(Add one row per source. Every column required. Minimum 2 rows per Rule 8.)

**Query refinement trail (Rule 6 -- mandatory, no exceptions):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK. Every SEARCH BLOCK has at least 2 source
        rows (supplemental documented if needed per Rule 8). All table cells are filled.
        Every refinement trail is completed per Rule 6.
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

Verdict token: [YES / NO / INCONCLUSIVE]
  [Write only the single matching token. This token is the authoritative verdict.
   It will be copied verbatim to PHASE 4 per Rule 7. Do not change it there.]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed. Verdict token is set to exactly one of
        YES / NO / INCONCLUSIVE. Balance result is filled (BALANCED or ONE-SIDED with
        documented follow-up). Do not proceed to PHASE 4 until all three fields are complete.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3. Reference sources by URL. Do not introduce new claims.]

Null-Attack Verdict:
  [Copy the Verdict token from PHASE 3 here verbatim -- per Rule 7. Do not re-assess.]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification of the
   PRE-COMMIT event.]

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

## V-05: Full R4 Synthesis (All Axes)

**Axes:** Phrasing register (Rule 7 verdict copy-forward) + Output format (Rule 8 evidence floor)
+ Lifecycle emphasis (PHASE 3.5 citation pre-audit gate) + Role sequence (inertia framing in
PRE-COMMIT: status-quo baseline named before falsification event) + Phase-gate enforcement
(GATE 0/0.5/1/2/3/3.5 full chain).
**Hypothesis:** V-05 incorporates every structural mechanism from R1-R4. The three R4 additions
over R3 V-05: (1) Rule 7 closes the PHASE 3->4 verdict chain-of-custody escape, (2) Rule 8 closes
the thin-evidence escape, (3) PHASE 3.5 closes the new-claim-injection escape in synthesis. The
inertia framing addition names the status-quo baseline explicitly in PRE-COMMIT: the model must
state what the current approach achieves before committing to the falsification event. This
sharpens the PRE-COMMIT by grounding the falsification in a concrete performance gap rather than
an abstract contrary result. GATE 0.5 verifies the inertia framing is populated before query
design proceeds. Full 8-rule RULES block + 6-gate lifecycle chain.

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
  7. The Null-Attack Verdict in PHASE 4 MUST be the verbatim copy of the "Verdict token:"
     field set in PHASE 3. You may NOT independently re-assess the verdict in PHASE 4.
     The token travels forward unchanged. Omitting or changing the token is a Rule 3 violation.
  8. Each SEARCH BLOCK MUST include at least 2 distinct source URLs in the Sources table.
     A SEARCH BLOCK with only 1 source URL is incomplete. If fewer than 2 sources are found,
     run a supplemental search immediately and document it:
       Supplemental query: [exact string]
       Supplemental source: [title] -- [URL]
     Then include the supplemental source as a row in the Evidence table.
     Omitting the supplemental when only 1 source was found is a Rule 3 violation.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## FALSIFICATION PRE-COMMIT
[Complete before designing any queries. Two stages: inertia framing, then falsification event.]

  Status quo (inertia framing):
    [Name the current approach, tool, or practice that the hypothesis challenges.
     State what it achieves today: "The status quo is [X], which currently achieves [Y]."]

  Hypothesis restated:
    [One sentence: restate the hypothesis in your own words, contrasting with the status quo.
     Format: "The hypothesis claims that [alternative] achieves [better/different outcome]
     compared to the status quo of [X]."]

  Falsification event:
    [Starting from the status-quo baseline above, name the specific observable outcome that
     would prove the hypothesis wrong.
     Format: "The hypothesis predicts [alternative] achieves [Z]. Falsification = evidence
     that [alternative] does NOT achieve [Z] under [conditions] -- i.e., it performs no
     better than or worse than the status quo [X] which achieves [Y]."
     Do not use "limitations of X" -- name a contrary result anchored to the baseline.]

  Null hypothesis (one sentence):
    [The status quo [X] is sufficient because: _____.]

GATE 0: Status quo is named. Falsification event references the status-quo baseline and
        names a specific contrary result, not a category of doubt.
        Do not proceed to GATE 0.5 until this gate is met.

GATE 0.5: Inertia framing is complete -- status quo baseline is stated, hypothesis is
          contrasted against it, and falsification event anchors to it. This contrast
          is the adversarial frame that Q2 will attack.
          Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: QUERY DESIGN

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis vs. the status quo]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking the falsification event declared in PRE-COMMIT]
    Target declaration: [Copy the falsification event from PRE-COMMIT here. Q2 is
                         searching for this specific result -- anchored to the status-quo
                         baseline. Must match PRE-COMMIT. Must NOT be independently generated.]

  Q3 (domain/technical):
    Query: [additional angle -- or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 target declaration matches the PRE-COMMIT falsification event
        (copy-forward from PRE-COMMIT, not independently generated). Rules 5 and 7 noted.
        Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION

[Run each query from PHASE 1. One SEARCH BLOCK per query. Fill every table cell.]

### SEARCH BLOCK: Q[N] ([Support / NULL HYPOTHESIS ATTACK / Domain -- label each])

**Query string:** [Exact text submitted to the search engine]

**Sources found (minimum 2 per Rule 8):**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

(If only 1 source found, document supplemental:
  Supplemental query: [exact string]
  Supplemental source: [title] -- [URL]
 Then add as row 2 above per Rule 8.)

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[Exact verbatim text from the source in double quotation marks. Do not paraphrase. Apply Rule 2.]" | [supports / refutes / mixed] -- [one sentence: how does this evidence relate to the hypothesis?] | [strong / weak / mixed] -- [one sentence: why this rating?] |

(Add one row per source. Every column required. Minimum 2 rows per Rule 8.)

**Query refinement trail (Rule 6 -- mandatory, no exceptions):**
  Planned query:  [Q string as designed in PHASE 1]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

(Repeat SEARCH BLOCK for Q2, Q3, and any additional queries from PHASE 1.)

GATE 2: Every PHASE 1 query has a SEARCH BLOCK. Every SEARCH BLOCK has at least 2 source
        rows (supplemental documented if needed per Rule 8). All table cells are filled.
        Every refinement trail is completed per Rule 6.
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: BALANCE CHECK

| Side | Count | Source URLs |
|------|-------|-------------|
| Supporting | [N] | [list] |
| Refuting | [N] | [list] |
| Mixed | [N] | [list] |

Null hypothesis verdict:
  Did Q2 find the falsification event declared in PRE-COMMIT (anchored to the status-quo
  baseline)?
  [YES        -- one sentence: what was found and why it matches the falsification event]
  [NO         -- one sentence: what was found instead; why it does not constitute falsification]
  [INCONCLUSIVE -- one sentence: what was found and what would resolve it]

Verdict token: [YES / NO / INCONCLUSIVE]
  [Write only the single matching token. This token is the authoritative verdict.
   It will be copied verbatim to PHASE 4 per Rule 7. Do not change it there.]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source in table above]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed. Verdict token is set to exactly one of
        YES / NO / INCONCLUSIVE. Balance result is filled (BALANCED or ONE-SIDED with
        documented follow-up). Do not proceed to PHASE 3.5 until all three fields are complete.

---

## PHASE 3.5: CITATION PRE-AUDIT

[Construct the admissibility registry before writing any synthesis field.
 Only URLs listed here may be cited in Convergence or Conflict in PHASE 4.
 Any URL not in this registry is inadmissible for synthesis use.]

Admissibility registry:

| URL | SEARCH BLOCK | Row | Relevance | Credibility |
|-----|-------------|-----|-----------|-------------|
| [URL] | Q[N] | [row N in that SEARCH BLOCK Evidence table] | [supports / refutes / mixed] | [credibility label] |

(Add one row per unique URL appearing in PHASE 2 Evidence tables. Copy from those tables --
 do not add new URLs here. Every URL cited in PHASE 4 Convergence and Conflict MUST appear
 in this registry.)

GATE 3.5: Admissibility registry is populated with every unique URL from PHASE 2 Evidence
          tables. No new URLs were added. Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: SYNTHESIS

[Write after GATE 3.5. Cite only URLs in the admissibility registry. Do not introduce
 new claims or URLs not present in the registry.]

Null-Attack Verdict:
  [Copy the Verdict token from PHASE 3 here verbatim -- per Rule 7. Do not re-assess.]
  [One sentence: what Q2 found and whether it constitutes a genuine falsification of the
   PRE-COMMIT event (anchored to the status-quo baseline).]

Convergence:
  [Where two or more admissible sources agree on the hypothesis vs. status quo.
   Cite at least two admissible URLs (must be in registry from PHASE 3.5).]

Conflict:
  [Where admissible sources disagree. Cite at least two admissible URLs. Or:
  "No material conflict found -- all [N] sources point [direction];
   credibility spread: [brief note]."]

Conclusion:
  [Paragraph of 3-5 sentences. Name at least two admissible sources by URL. State:
   (1) what the aggregate evidence says about the hypothesis relative to the status quo,
   (2) the single largest remaining gap for a follow-up investigation.
   Close with: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.
   The Null-Attack Verdict is declared above -- reference it; do not re-adjudicate here.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, status_quo_baseline, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result,
             refinement_count, falsification_event, admissible_url_count.
```

---

## Round 4 Design Notes

### Criteria coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | rule 1 | rule 1 | rule 1 | rule 1 | rule 1 |
| C-02 | rule 2 + Quote col | rule 2 + Quote col | rule 2 + Quote col | rule 2 + Quote col | rule 2 + Quote col |
| C-03 | SEARCH BLOCK + tables | SEARCH BLOCK + tables | SEARCH BLOCK + tables | SEARCH BLOCK + tables | SEARCH BLOCK + tables |
| C-04 | Relevance column | Relevance column | Relevance column | Relevance column | Relevance column |
| C-05 | Strength column | Strength column | Strength column | Strength column | Strength column |
| C-06 | GATE 1 (Q1+Q2) | GATE 1 (Q1+Q2) | GATE 1 (Q1+Q2) | GATE 1 (Q1+Q2) | GATE 1 (Q1+Q2) |
| C-07 | GATE 3 balance | GATE 3 balance | GATE 3 balance | GATE 3 balance | GATE 3 balance |
| C-08 | Credibility column | Credibility column | Credibility column | Credibility column | Credibility column |
| C-09 | 4 synthesis sub-fields | 4 synthesis sub-fields | 4 synthesis sub-fields + registry | 4 synthesis sub-fields | 4 synthesis sub-fields + registry |
| C-10 | refinement trail per SEARCH BLOCK | refinement trail per SEARCH BLOCK | refinement trail per SEARCH BLOCK | refinement trail per SEARCH BLOCK | refinement trail per SEARCH BLOCK |
| C-11 | GATE 0/1/2/3 | GATE 0/1/2/3 | GATE 0/1/2/3/3.5 | GATE 0/1/2/3 | GATE 0/0.5/1/2/3/3.5 |
| C-12 | refinement in PHASE 2 SEARCH BLOCK | refinement in PHASE 2 SEARCH BLOCK | refinement in PHASE 2 SEARCH BLOCK | refinement in PHASE 2 SEARCH BLOCK | refinement in PHASE 2 SEARCH BLOCK |
| C-13 | GATE 1: PRE-COMMIT match | GATE 1: PRE-COMMIT match | GATE 1: PRE-COMMIT match | GATE 1: PRE-COMMIT match | GATE 1: PRE-COMMIT match |
| C-14 | Null-Attack Verdict + 3 sub-fields | Null-Attack Verdict + 3 sub-fields | Null-Attack Verdict + 3 sub-fields | Null-Attack Verdict + 3 sub-fields | Null-Attack Verdict + 3 sub-fields |
| C-15 | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis | RULES block before Topic/Hypothesis |
| C-16 | PRE-COMMIT + GATE 1 binding | PRE-COMMIT + GATE 1 binding | PRE-COMMIT + GATE 1 binding | PRE-COMMIT + GATE 1 binding | PRE-COMMIT + GATE 1 binding |
| C-17 | Rule 6 MUST, no exceptions | Rule 6 MUST, no exceptions | Rule 6 MUST, no exceptions | Rule 6 MUST, no exceptions | Rule 6 MUST, no exceptions |
| C-18 | standalone Null-Attack Verdict field | standalone Null-Attack Verdict field | standalone Null-Attack Verdict field | standalone Null-Attack Verdict field | standalone Null-Attack Verdict field |
| C-19 | Rule 6 RULES-level, violation consequence | Rule 6 RULES-level, violation consequence | Rule 6 RULES-level, violation consequence | Rule 6 RULES-level, violation consequence | Rule 6 RULES-level, violation consequence |
| C-20 | Null-Attack Verdict first in PHASE 4 | Null-Attack Verdict first in PHASE 4 | Null-Attack Verdict first in PHASE 4 | Null-Attack Verdict first in PHASE 4 | Null-Attack Verdict first in PHASE 4 |
| C-21 | GATE 0 PRE-COMMIT + GATE 1 copy-forward | GATE 0 PRE-COMMIT + GATE 1 copy-forward | GATE 0 PRE-COMMIT + GATE 1 copy-forward | GATE 0 PRE-COMMIT + GATE 1 copy-forward | GATE 0 PRE-COMMIT + GATE 1 copy-forward |
| **C-22?** | **Rule 7: verdict token copy-forward (PASS)** | advisory "consistent with" (same as R3 V-05) | advisory "consistent with" (same as R3 V-05) | **Rule 7: verdict token copy-forward (PASS)** | **Rule 7: verdict token copy-forward (PASS)** |
| **C-23?** | advisory evidence floor | **Rule 8: min 2 sources, supplemental (PASS)** | advisory evidence floor | **Rule 8: min 2 sources, supplemental (PASS)** | **Rule 8: min 2 sources, supplemental (PASS)** |
| **C-24?** | no citation audit | no citation audit | **PHASE 3.5 admissibility registry + GATE 3.5 (PASS)** | no citation audit | **PHASE 3.5 admissibility registry + GATE 3.5 (PASS)** |

### New R4 mechanisms

**Verdict copy-forward binding (V-01, V-04, V-05):**
Rule 7 converts the PHASE 3 -> PHASE 4 verdict relationship from advisory ("must be consistent
with") to structural (copy-forward, same token, violation consequence named). PHASE 3 emits a
standalone "Verdict token:" field -- one word only (YES / NO / INCONCLUSIVE). GATE 3 requires
the token to be set before proceeding. PHASE 4 Null-Attack Verdict field says "Copy the Verdict
token from PHASE 3 here verbatim -- per Rule 7." This is the direct analog of C-21's PRE-COMMIT
-> GATE 1 mechanism applied to the verdict propagation chain. It closes the silent re-assessment
escape where a model can produce a different (often more hedged) verdict in PHASE 4 than PHASE 3.

**Evidence floor enforcement (V-02, V-04, V-05):**
Rule 8 sets a minimum of 2 source URLs per SEARCH BLOCK. If fewer than 2 are found, a
supplemental search is required and documented inline. GATE 2 checks the floor before PHASE 3
proceeds. This closes the thin-evidence escape: a 1-source Q2 technically satisfies the table
structure but cannot support Convergence (which requires "at least two sources" in synthesis).
The floor creates a source-count guarantee that C-09 cross-source synthesis can rely on.

**Synthesis citation pre-audit (V-03, V-05):**
PHASE 3.5 constructs an admissibility registry from PHASE 2 evidence tables before synthesis
begins. Every URL in Convergence and Conflict must appear in this registry. GATE 3.5 locks the
registry closed before PHASE 4. This closes the new-claim-injection escape: a model writing
Convergence can introduce a URL it read during search but did not include in PHASE 2 tables.
The advisory "Do not introduce new claims" cannot structurally prevent this; the admissibility
registry does.

**Inertia framing (V-05 only):**
PRE-COMMIT gains a "Status quo:" field naming the current approach and its baseline performance.
The falsification event must be anchored to this baseline: "evidence that [alternative] does NOT
outperform the status quo [X]." This sharpens the adversarial commitment from "a contrary result"
(abstract) to "evidence that the alternative fails to improve on the baseline" (concrete). GATE 0
and GATE 0.5 enforce the two-stage PRE-COMMIT completion. The inertia framing also propagates to
the frontmatter as `status_quo_baseline`.

### V-golden candidate for R4

**V-01** is the minimal R4 hypothesis: if verdict copy-forward closes the 2-pt gap in V-05,
V-01 achieves 122/122 with a single Rule 7 addition. V-02 and V-03 test two independent escapes.
**V-04** combines V-01 + V-02 for the two most structurally significant additions. **V-05** adds
citation audit and inertia framing for maximum structural coverage.

Key empirical question: does Rule 7 (verdict copy-forward) produce the 2-pt gain, or is the gap
from a different escape? If V-01 scores 122, it is the minimal golden. If V-01 still scores 120
(gap unresolved), V-02 and V-03 become the diagnostic tests for whether evidence floor or
citation audit closes it. V-04 is the likely 122 candidate regardless.

---

## Version History

| Round | Date | Top Score | Golden Candidate |
|-------|------|-----------|-----------------|
| R1 | 2026-03-14 | ~108-110 | V-05 (phase gates + target framing + tables) |
| R2 | 2026-03-14 | ~112-114 | V-03 (null attack + phase gates) |
| R3 | 2026-03-14 | 116/116 (120/122 under v4) | V-04 or V-05 (verdict field + Rule 6) |
| R4 | 2026-03-14 | TBD | V-01 or V-04 (verdict copy-forward as primary hypothesis) |
