Written to `simulations/quest/variations/discover-literature-variations-R1-2026-03-19.md`.

---

## discover-literature — Variations R1

### Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Role sequence | Search-before-extract prevents confirmation bias — evidence shapes claims, not the reverse |
| **V-02** | Output format | Evidence cards with confidence scores (High/Medium/Low) surface high-risk gaps faster than flat table rows |
| **V-03** | Lifecycle emphasis | Expanded Phase 3/4 scaffolding with mandatory sub-steps yields better CONTRARY and METHODOLOGICAL coverage |
| **V-04** | Phrasing register | Questions the model must answer elicit more complete responses than tasks it must perform |
| **V-05** | Combination (inertia + search-first) | Naming inertia upfront as the named competitor motivates thoroughness; search-first ordering prevents cherry-picking |

---

### Design notes

**Single-axis variations (V-01 through V-04)** each isolate one change:

- **V-01** reorders phases: Phase 1 becomes a broad sweep, Phase 2 extracts claims from what was found. Adds a targeted gap-search phase before mapping. Six phases total vs. five.
- **V-02** replaces the citation table with structured evidence cards — one card per source, each with a Confidence rating. The format change propagates through Phases 2-4.
- **V-03** keeps the five-phase structure but breaks Phase 3 into four mandatory sub-steps (3a-3d) and Phase 4 into four explicit inventory blocks. Most scaffolding weight goes to the phases that carry the most rubric weight.
- **V-04** rewrites all imperatives as questions. Every phase is a set of questions the model must answer before proceeding. No structural reordering — pure register shift.

**V-05 (combination)** stacks two axes: inertia framing appears in the preamble, after Phase 3, after Phase 5, and in the PROCEED check. Role sequence is search-first (borrowed from V-01). The inertia framing targets the specific failure modes the rubric guards against — hostile-reviewer citations, missing CONTRARY entries, premature PROCEED calls.

**Rubric coverage by variation:**

| Criterion | Baseline | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 claims extracted | Phase 1 | Phase 2 | Phase 1 | Phase 1 | Phase 1 | Phase 2 |
| C-02 citation table | Phase 2 | Phase 1 | Cards | Phase 2 | Phase 2 | Phase 1 |
| C-03 four-tier map | Phase 3 | Phase 4 | Phase 3 | Phase 3a-d | Phase 3 | Phase 4 |
| C-04 gap analysis + rec | Phase 4 | Phase 5 | Phase 4 | Phase 4 | Phase 4 | Phase 5 |
| C-05 artifact written | Phase 5 | Phase 6 | Phase 5 | Phase 5 | Phase 5 | Phase 6 |
| C-06 contrary→claim | implied | explicit | explicit | explicit | explicit | explicit |
| C-08 HIGH RISK block | conditional | conditional | conditional | mandatory block | explicit | mandatory + framing |
| C-10 precedent chain | implicit | explicit year check | Confidence field | year confirmation | year question | explicit year check |
tation table with claim numbers filled in immediately.

---

## PHASE 4 -- LITERATURE MAP

Organize all sources into four tiers:

**FOUNDATIONAL** (must cite — the field depends on these)
[list with one-sentence justification for why each is foundational]

**RECENT** (2020 or later — shows engagement with current work)
[list — prioritize highly-cited or published in top venues]

**CONTRARY** (papers that challenge a claim — must address these)
[list — note which Claim # each paper challenges; these are the papers a hostile reviewer will cite]

**METHODOLOGICAL** (papers that justify the method)
[list — each entry names the originating paper and year; shows method predates current work]

---

## PHASE 5 -- GAP ANALYSIS

```
Claims with strong literature support: N/M
Claims with weak or no support: [list]
Contrary evidence that must be addressed: [list — most dangerous first]
Missing methodological precedents: [what needs to be found]

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

If a claim has no supporting literature and strong contrary evidence: flag as HIGH RISK — state whether to scope, qualify, or drop the claim.

---

## PHASE 6 -- AMEND

Three targeted additions:
1. [The claim most urgently needing more support — what to search for next]
2. [The contrary paper that must be addressed — what the response should be: scope qualification, methodological distinction, or domain limitation]
3. [The methodological gap — what precedent is needed to justify the method]

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 — Output Format: Evidence Cards

**Axis**: Output format
**Hypothesis**: Per-source evidence cards with an explicit confidence score (High / Medium / Low) make it harder to skip the quality assessment. High-risk gaps become visible immediately rather than buried in table rows.

```
You are running /discover-literature for: {{topic}}

Systematic literature review with citation management. Builds a structured literature map — not just a list of pages.

---

## PHASE 1 -- CLAIM EXTRACTION

Read any prior signals: discover-hypothesis, specify-spec, paper draft.
Extract the 3-5 key claims that require literature support.

For each claim:

**Claim C-[N]: [one-sentence statement]**
- Evidence type needed: empirical / theoretical / methodological
- Contrary evidence that would undermine it: [describe]

---

## PHASE 2 -- LITERATURE SEARCH

For each claim, search:
1. WebSearch: "[claim topic] seminal" — foundational works
2. WebSearch: "[claim topic] review 2020-2025" — current surveys
3. WebSearch: "[claim topic] criticism" — contrary evidence
4. WebSearch: "[claim topic] method" — methodological precedents

For each source found, produce one evidence card:

---
**SOURCE [N]**
Title: [full title]
Authors: [Last, F. et al. — no placeholders]
Year: [YYYY]
Venue: [journal / conference / preprint server]
Claim #: [which claim this bears on]
Position: supports / contradicts / qualifies
Key finding: [one sentence]
Confidence: High (top venue, high citation) / Medium (credible but limited) / Low (preprint, single study)
---

Do not use "Author et al." as a placeholder. If author names are unknown, continue searching.

---

## PHASE 3 -- LITERATURE MAP

Organize evidence cards into four tiers:

**FOUNDATIONAL** (must cite — the field depends on these)
[reference card numbers with one-sentence justification]

**RECENT** (2020 or later — shows engagement with current work)
[reference card numbers — note citation counts or venue tier if available]

**CONTRARY** (papers that challenge a claim — must address these)
[reference card numbers — include which Claim # each card challenges]

**METHODOLOGICAL** (papers that justify the method)
[reference card numbers — each must show year to confirm method predates current work]

---

## PHASE 4 -- GAP ANALYSIS

```
Claims with strong support (>= 2 High/Medium cards): [list]
Claims with weak or no support: [list]
Contrary evidence cards that must be addressed: [list SOURCE N — most dangerous first]
Missing methodological precedents: [describe gap]

HIGH RISK claims (no support + contrary evidence): [list or "none"]
  For each: scope / qualify / drop recommendation

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

---

## PHASE 5 -- AMEND

Three targeted additions:
1. [Claim most urgently needing more support — what to search for next]
2. [Contrary paper (SOURCE N) that must be addressed — rebuttal direction: scope qualification, methodological distinction, or domain limitation]
3. [Methodological gap — what precedent is needed and where to find it]

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 — Lifecycle Emphasis: Map and Gap Expanded

**Axis**: Lifecycle emphasis
**Hypothesis**: Phases 3 and 4 carry the most rubric weight (C-03, C-04, C-06, C-08, C-10) but receive the least structural guidance in the current skill. Expanding their scaffolding with explicit sub-steps yields better CONTRARY and METHODOLOGICAL tier coverage.

```
You are running /discover-literature for: {{topic}}

Systematic literature review with citation management. Builds the four-tier map and gap analysis a methods section needs.

---

## PHASE 1 -- CLAIM EXTRACTION (brief)

Read any prior signals. Extract 3-5 key claims.

For each: state the claim, the evidence type needed (empirical / theoretical / methodological), and what contrary evidence would undermine it.

---

## PHASE 2 -- LITERATURE SEARCH (brief)

Run WebSearch for each claim across four angles: seminal, recent review, criticism, method.

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|
| | | | | | supports/contradicts/qualifies | |

---

## PHASE 3 -- LITERATURE MAP (primary)

This phase has four mandatory sub-steps. Complete each before moving to the next.

### 3a. FOUNDATIONAL tier
For each foundational paper:
- Full citation (Title, Authors, Year, Venue)
- One sentence: why the field cannot be discussed without this work
- Which claim(s) it supports

Minimum: 1 paper. If none found, write "NOT FOUND — search required before proceeding."

### 3b. RECENT tier
For each paper from 2020 or later:
- Full citation
- One sentence: what current consensus or shift it represents
- Which claim(s) it supports

Minimum: 1 paper dated >= 2020. If none found, write "NOT FOUND — field may lack recent coverage."

### 3c. CONTRARY tier
For each paper that challenges a claim:
- Full citation
- Which Claim # it challenges (required — no entry without a claim reference)
- One sentence: the specific objection it raises
- Threat level: HIGH (directly refutes) / MEDIUM (qualifies) / LOW (tangential)

Minimum: 1 paper (or explicit "none — no contrary evidence found in search"). CONTRARY entries without a claim number are invalid.

### 3d. METHODOLOGICAL tier
For each paper that justifies the method:
- Full citation including year
- One sentence: what methodological precedent it establishes
- Confirm year is before the current work's claimed contribution date

Minimum: 1 paper. Each entry must include a year to anchor the precedent chain.

---

## PHASE 4 -- GAP ANALYSIS (primary)

Complete each block:

**Support inventory:**
- Claims with >= 2 supporting sources: [list]
- Claims with exactly 1 supporting source: [list — borderline]
- Claims with 0 supporting sources: [list — HIGH RISK candidates]

**Contrary evidence inventory:**
- HIGH threat contrary papers: [list with claim reference]
- MEDIUM threat: [list]
- Papers reviewer is likely to cite against us: [top 2]

**HIGH RISK block** (required if any claim has 0 support + HIGH threat contrary):
For each HIGH RISK claim:
```
CLAIM: [text]
RISK: [why it is unsupported]
RESPONSE: scope / qualify / drop
SUGGESTED FRAMING: [one sentence]
```

**Methodological coverage:**
- Methods covered by precedent: [list]
- Methods lacking precedent: [list — must search before submission]

**Recommendation:**
```
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence]
```

---

## PHASE 5 -- AMEND (brief)

Three targeted additions:
1. [Claim most urgently needing more support]
2. [Single most dangerous contrary paper — rebuttal direction]
3. [Methodological gap — what to find next]

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 — Phrasing Register: Interrogative

**Axis**: Phrasing register
**Hypothesis**: Framing each phase as a set of questions the model must answer — rather than tasks it must perform — elicits more complete and specific responses. Questions create an obligation to answer; imperatives create an option to skim.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

For each claim from Phase 1, search and answer:

1. What are the seminal works the field cites on this claim? (WebSearch: "[claim topic] seminal paper")
2. What reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the method being used? (WebSearch: "[claim topic] method")

Record answers in a citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|
| | | | | | supports/contradicts/qualifies | |

No placeholder entries. If a cell is unknown, note it and search again.

---

## PHASE 3 -- How does the literature organize?

Answer these questions by building the four-tier map:

1. Which sources are FOUNDATIONAL — works the field cannot discuss without citing? (justify each in one sentence)
2. Which sources are RECENT (2020+) — showing engagement with current work?
3. Which sources are CONTRARY — the ones a hostile reviewer will cite against your claims? (for each: which Claim # does it challenge?)
4. Which sources are METHODOLOGICAL — establishing that the method predates and validates this work? (for each: confirm the paper's year is before the current contribution date)

Every tier must have at least one answer. If a tier has no entries, write "NONE FOUND — explain why and what additional search is needed."

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these questions:

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the recommendation?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 — Combination: Inertia Framing + Search-First

**Axes**: Inertia framing (prominent) + Role sequence (search-before-extract)
**Hypothesis**: Naming the status-quo alternative upfront — "the alternative to this skill is no literature review at all" — motivates thoroughness because the model is competing against a named baseline. Search-first ordering prevents confirmation bias by letting evidence shape claims rather than claims filter evidence.

```
You are running /discover-literature for: {{topic}}

Systematic literature review with citation management.

**The alternative to this skill is no literature review.** Teams that skip this step submit claims that reviewers immediately refute with papers the authors never read. This skill exists because "I didn't know about that paper" is a preventable failure mode. Every phase below closes a gap that inertia leaves open.

---

## PHASE 1 -- LANDSCAPE SWEEP (before extracting claims)

The first move is to discover what the field has already said — before deciding what claims need support. This prevents the failure mode of extracting claims in a vacuum, then cherry-picking evidence to fit them.

Run four searches on {{topic}}:
1. WebSearch: "{{topic}} seminal" — what the field was built on
2. WebSearch: "{{topic}} review 2020-2025" — where the field stands now
3. WebSearch: "{{topic}} criticism" or "limitations of {{topic}}" — what the field disputes
4. WebSearch: "{{topic}} method" — how researchers do this

Record every source found:
| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|
| | | | | | supports/contradicts/qualifies | |

Claim # is blank for now. Fill it in after Phase 2.

---

## PHASE 2 -- CLAIM EXTRACTION (informed by the landscape)

Read any prior signals: discover-hypothesis, specify-spec, paper draft.

Now extract the 3-5 key claims that require literature support — with the landscape already in view. For each claim:
- What the claim asserts
- What evidence type it needs (empirical / theoretical / methodological)
- What contrary evidence would undermine it
- Which Phase 1 papers already bear on this claim? (back-reference)

Update the Claim # column in the Phase 1 table.

**Inertia check**: For each claim, ask: "Could a reviewer immediately cite a paper that contradicts this?" If yes, that paper should already appear in Phase 1. If it doesn't, search for it now.

---

## PHASE 3 -- TARGETED SEARCH (closing the gaps)

For any claim with fewer than 2 Phase 1 sources, run focused searches:
- WebSearch: "[specific claim term] evidence"
- WebSearch: "against [claim term]"
- WebSearch: "[claim term] replication"

Add new rows to the citation table with claim numbers filled in immediately.

**Why this phase exists**: Inertia says "the Phase 1 search is probably enough." It usually isn't for the CONTRARY and METHODOLOGICAL tiers. These are the tiers hostile reviewers know best.

---

## PHASE 4 -- LITERATURE MAP

Organize sources into four tiers:

**FOUNDATIONAL** (must cite — the field depends on these)
[list with one-sentence justification — if this tier is empty, the review is incomplete]

**RECENT** (2020 or later — shows the work is not behind the field)
[list — prioritize highly-cited or top-venue papers]

**CONTRARY** (papers that challenge a claim)
[list — each entry must name the Claim # it challenges; these are what a hostile reviewer will cite]

**METHODOLOGICAL** (papers that justify the method)
[list — each entry must include year; shows method predates current work; a missing precedent chain is a desk-rejection risk]

---

## PHASE 5 -- GAP ANALYSIS

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first, with Claim # reference]
Missing methodological precedents: [describe]

HIGH RISK claims (no support + contrary evidence): [list or "none"]
  For each: SCOPE / QUALIFY / DROP + one-sentence framing

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

**Inertia reminder**: A PROCEED recommendation means the literature review is complete enough that submission risk from missing citations is low. It does not mean "we found only supportive papers." If you are tempted to write PROCEED after finding only 3-4 sources, ask whether a hostile reviewer would agree.

---

## PHASE 6 -- AMEND

Three targeted additions:
1. [Claim most urgently needing more support — what to search for next]
2. [Contrary paper that must be addressed — name the paper; propose rebuttal direction: scope qualification, methodological distinction, or domain limitation]
3. [Methodological gap — what precedent is missing and where to find it]

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
