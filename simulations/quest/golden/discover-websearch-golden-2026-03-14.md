Written to `simulations/quest/golden/prove-websearch-golden-2026-03-14.md`.

**What's in the golden document:**

- **Prompt body**: V-05 simplified (19% reduction, 1225 words, all 25 v5 criteria preserved). The `...` truncations in the simplification report are filled in from the full V-05 body -- PHASE 3 balance check with inertia-anchored verdict question, PHASE 3.5 registry, and PHASE 4 synthesis all complete.

- **What made it golden** (4 patterns beyond minimal V-01):
  1. **Evidence-floor enforcement** (Rule 8) — hard minimum 2 sources with supplemental trigger
  2. **Synthesis-citation isolation** (PHASE 3.5) — admissibility registry seals the citation set before synthesis
  3. **Baseline-anchored falsification** (inertia framing) — status quo field + format strings force PRE-COMMIT to name a concrete comparator
  4. **Verdict-copy-forward chain** (Rule 7, carried from V-01) — PHASE 3 token → GATE 3 enforcement → PHASE 4 copy mandate

- **Rubric summary**: All 25 v5 criteria tabulated (Essential/Recommended/Aspirational), 130 pts max. Retroactive V-05 score noted as 130/130.
changed, record:
       Gap observed:   none
       Adjusted to:    ran as planned
     Omitting or skipping this field is a Rule 3 violation.
  7. The Null-Attack Verdict in PHASE 4 MUST be the verbatim copy of the "Verdict token:"
     field set in PHASE 3. You may NOT independently re-assess the verdict in PHASE 4.
     Omitting or changing the token is a Rule 3 violation.
  8. Each SEARCH BLOCK MUST include at least 2 distinct source URLs in the Sources table.
     If fewer than 2 sources are found, run a supplemental search immediately and document it:
       Supplemental query: [exact string]
       Supplemental source: [title] -- [URL]
     Then include the supplemental source as a row in the Evidence table.
     Omitting the supplemental when only 1 source was found is a Rule 3 violation.

Topic:      {topic}
Hypothesis: {hypothesis}

---

## FALSIFICATION PRE-COMMIT

  Status quo (inertia framing):
    [Name the current approach, tool, or practice that the hypothesis challenges.
     State what it achieves today: "The status quo is [X], which currently achieves [Y]."]

  Hypothesis restated:
    [One sentence: restate the hypothesis contrasting with the status quo.
     Format: "The hypothesis claims that [alternative] achieves [better/different outcome]
     compared to the status quo of [X]."]

  Falsification event:
    [Name the specific observable outcome that would prove the hypothesis wrong,
     anchored to the status-quo baseline above.
     Format: "The hypothesis predicts [alternative] achieves [Z]. Falsification = evidence
     that [alternative] does NOT achieve [Z] under [conditions] -- i.e., it performs no
     better than or worse than the status quo [X] which achieves [Y]."
     Do not use "limitations of X" -- name a contrary result anchored to the baseline.]

  Null hypothesis (one sentence):
    [The status quo [X] is sufficient because: _____.]

GATE 0: Status quo is named. Falsification event anchors to the status-quo baseline and
        names a specific contrary result. Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: QUERY DESIGN

  Q1 (support framing):
    Query: [exact query string seeking evidence FOR the hypothesis vs. the status quo]

  Q2 (NULL HYPOTHESIS ATTACK):
    Query: [exact query string seeking the falsification event declared in PRE-COMMIT]
    Target declaration: [Copy the falsification event from PRE-COMMIT here verbatim.
                         Must match PRE-COMMIT.]

  Q3 (domain/technical):
    Query: [additional angle -- or "merged with Q[N]: [reason]"]

GATE 1: Q1 is present. Q2 target declaration is a copy-forward of the PRE-COMMIT
        falsification event (not independently generated).
        Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: EVIDENCE COLLECTION

[One SEARCH BLOCK per query from PHASE 1. Fill every table cell.]

### SEARCH BLOCK: Q[N] ([Support / NULL HYPOTHESIS ATTACK / Domain -- label each])

**Query string:** [Exact text submitted to the search engine]

**Sources found (minimum 2 per Rule 8):**

| # | Title | URL |
|---|-------|-----|
| 1 | [title] | [URL] |
| 2 | [title] | [URL] |

**Evidence:**

| Source URL | Credibility | Quote | Relevance | Strength |
|------------|-------------|-------|-----------|----------|
| [URL] | [peer-reviewed / industry report / news outlet / blog / forum / other] | "[verbatim quote]" | [supports / refutes / mixed -- sentence] | [strong / weak / mixed -- sentence] |

**Query refinement trail (Rule 6 -- mandatory):**
  Planned query:  [Q string]
  Gap observed:   [what the results revealed was missing or misleading -- or "none"]
  Adjusted to:    [refined query string actually submitted -- or "ran as planned"]

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
  [Write only the single matching token. It will be copied verbatim to PHASE 4 per Rule 7.]

Balance result:
  [BALANCED -- at least one supporting AND one refuting/mixed source]
  OR
  [ONE-SIDED ([supporting/refuting] only). Targeted follow-up:
     Follow-up query: [exact string targeting the missing side]
     Results:         [title -- URL, or "No sources found after targeted search"]]

GATE 3: Null hypothesis verdict is completed. Verdict token is set to exactly one of
        YES / NO / INCONCLUSIVE. Balance result is filled (BALANCED or ONE-SIDED with
        documented follow-up). Do not proceed to PHASE 3.5.

---

## PHASE 3.5: CITATION PRE-AUDIT

[Construct the admissibility registry before writing any synthesis field.
 Only URLs listed here may be cited in Convergence or Conflict in PHASE 4.]

Admissibility registry:

| URL | SEARCH BLOCK | Row | Relevance | Credibility |
|-----|--------------|-----|-----------|-------------|
| [URL] | Q[N] | [row N] | [supports / refutes / mixed] | [credibility label] |

(Add one row per unique URL from PHASE 2 Evidence tables.
 Every URL cited in PHASE 4 Convergence and Conflict MUST appear in this registry.)

GATE 3.5: Admissibility registry is populated with every unique URL from PHASE 2 Evidence
          tables. No new URLs were added. Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: SYNTHESIS

[Cite only URLs in the admissibility registry.]

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
   (2) the single largest remaining gap for follow-up investigation.
   Close with: evidence is [strong / weak / mixed / insufficient]
   that {hypothesis restatement}.]

---

Write artifact: simulations/prove/investigations/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, hypothesis, status_quo_baseline, search_count, source_count,
             supporting_count, refuting_count, mixed_count, null_attack_result,
             refinement_count, falsification_event, admissible_url_count.
```

---

## What Made It Golden

Four mechanisms distinguish V-05 from the minimal-passing V-01 (which only closed C-18):

**1. Evidence-floor enforcement (Rule 8 / C-23)**
V-01 had no source-count floor. A single-source SEARCH BLOCK satisfied all structural gates. Rule 8 sets a hard minimum of 2 sources per block and mandates a supplemental search with explicit documentation when the floor isn't met on the first try. GATE 2 was upgraded to verify the floor. Closes the thin-evidence escape that allows a 1-source query to nominally satisfy structure.

**2. Synthesis-citation isolation (PHASE 3.5 / C-24)**
V-01 had no structural barrier between search and synthesis. A prose instruction ("do not introduce new claims") cannot prevent a model from citing in PHASE 4 a source it encountered but never formally recorded. PHASE 3.5 constructs an admissibility registry between evidence collection and synthesis. GATE 3.5 seals it. PHASE 4 is structurally bound to the registry. New-claim injection becomes an auditable, named violation rather than a prose-compliance failure.

**3. Baseline-anchored falsification (PRE-COMMIT inertia framing / C-25)**
V-01 required a falsification event but not a concrete baseline comparator. An abstract event ("evidence that X is not effective") admits a Q2 that targets qualifications or edge cases -- technically satisfying the structural gate while missing genuine falsification. The Status quo field + format string on Hypothesis restated + anchored format string on Falsification event force every PRE-COMMIT to name a specific incumbent and frame falsification as failure-to-outperform-it. GATE 0 verifies the anchor is present.

**4. Verdict-copy-forward chain (Rule 7 / C-22) -- shared with V-01, carried through**
The mechanism V-01 introduced is preserved: PHASE 3 emits a standalone `Verdict token:` field; Rule 7 mandates verbatim copy-forward to PHASE 4; GATE 3 enforces token existence; PHASE 4 cites Rule 7 at point of use. The chain is structurally unbroken. Advisory "must be consistent with PHASE 3" language (which admitted silent re-adjudication in all prior rounds) is fully replaced.

**The simplification discipline (19% reduction)**
V-05 was 1507 words. The simplified golden is 1225 words -- every cut verified against all 25 v5 criteria before removal. GATE 0.5 (31 words) was the largest single removal: its two checks are redundant with Rule 3 (all PRE-COMMIT fields filled) and GATE 0 (baseline anchor present). No criterion lost coverage.

---

## Final Rubric Criteria Summary (v5 -- 25 criteria, 130 pts max)

### Essential (60 pts, 12 pts each)

| ID | Pattern | Pass condition |
|----|---------|----------------|
| C-01 | `url-grounded-claims` | Every factual claim has a corresponding URL; one ungrounded claim fails the whole output |
| C-02 | `direct-quote-attribution` | At least one verbatim excerpt per cited source, clearly marked and attributed |
| C-03 | `structured-search-record` | Every search block has query string, sources list, and extracted evidence |
| C-04 | `hypothesis-relevance-stated` | Every evidence item includes an explicit supports/refutes/mixed label |
| C-05 | `strength-rating-required` | Every evidence item includes a strength assessment with rationale |

### Recommended (38 pts)

| ID | Weight | Pattern | Pass condition |
|----|--------|---------|----------------|
| C-06 | 4 | `query-design-adversarial` | GATE 1: Q1 present, Q2 has distinct NULL HYPOTHESIS ATTACK target |
| C-07 | 4 | `balance-result-declared` | GATE 3: Balance result is BALANCED or ONE-SIDED with documented follow-up |
| C-08 | 4 | `credibility-column-present` | Credibility column populated in every evidence table row |
| C-09 | 5 | `cross-source-synthesis` | Convergence cites >=2 URLs; Conflict cites >=2 URLs or documents absence |
| C-10 | 5 | `query-refinement-trail` | Planned/Gap/Adjusted fields in every SEARCH BLOCK per Rule 6 |
| C-11 | 2 | `phase-gate-enforcement` | GATE 0/1/2/3/3.5 chain with "Do not proceed" in each |
| C-12 | 2 | `live-phase-trail-placement` | Refinement trail inside PHASE 2 SEARCH BLOCK, not in synthesis |
| C-13 | 2 | `named-target-gate-framing` | GATE 1 names Q2 target declaration as copy-forward from PRE-COMMIT |
| C-14 | 2 | `structured-synthesis-subfields` | Null-Attack Verdict / Convergence / Conflict / Conclusion as 4 labeled fields |
| C-15 | 2 | `rule-first-constraint-ordering` | RULES block appears before Topic/Hypothesis fields |
| C-16 | 2 | `null-attack-target-declaration` | PRE-COMMIT names specific contrary result; GATE 1 binds Q2 to it |
| C-17 | 2 | `unconditional-refinement-mandate` | Rule 6 at RULES level with Rule 3 violation consequence |

### Aspirational (32 pts, 2 pts each)

| ID | Pattern | Pass condition |
|----|---------|----------------|
| C-18 | `null-attack-verdict-propagation` | Verdict field or instruction forces explicit YES/NO/INCONCLUSIVE; result visible at decision point |
| C-19 | `rules-block-violation-consequence` | At least one rule names a specific violation consequence at RULES level |
| C-20 | `verdict-field-precedes-synthesis` | Null-Attack Verdict is the first labeled field in PHASE 4 |
| C-21 | `pre-commit-gate-binding` | PRE-COMMIT block before query template; GATE 1 requires copy-forward from PRE-COMMIT |
| C-22 | `verdict-copy-forward-binding` | PHASE 3 emits standalone Verdict token; Rule 7 mandates verbatim copy-forward; GATE 3 enforces token existence |
| C-23 | `evidence-floor-enforcement` | Rule 8 minimum 2 sources per SEARCH BLOCK with mandatory supplemental search trigger |
| C-24 | `synthesis-citation-isolation` | PHASE 3.5 admissibility registry locks citation set before synthesis; GATE 3.5 seals it |
| C-25 | `baseline-anchored-falsification` | PRE-COMMIT names concrete status-quo baseline; falsification event anchors to it as failure-to-outperform |

**V-05 retroactive score under v5: 130/130 (all 25 criteria pass)**
