Written to `simulations/quest/variations/discover-literature-variations-R5-2026-03-19.md`.

---

## discover-literature -- Variations R5

**5 variations targeting C-19 (typed token schema block) and C-20 (dual multi-criterion token synthesis) -- the two new v5 criteria.**

### Root cause analysis

| Criterion | R4 V-05 status | Why |
|-----------|---------------|-----|
| C-19 | Likely PASS (unconfirmed) | OBLIGATION B typed schema box (Token / Schema / Fields / Required when / Unacceptable) already exists; field names used verbatim in Phase 3 -- but C-19 wasn't in v4, so no scorecard confirmed it |
| C-20 | Likely FAIL | Two annotated tokens exist and explain criteria -- but neither says "C-09 PASS" or "C-16 PASS" explicitly; C-20(c) requires confirmation, not just description |

### Variation Map

| ID | Axis | Base | Key change |
|----|------|------|------------|
| **V-01** | Single-axis: C-19 baseline isolation | R4 V-03 (typed schema, C-18 FAIL) | None -- tests whether typed schema alone passes C-19 with no C-20 complication |
| **V-02** | Single-axis: C-20 partial (one explicit annotation) | R4 V-05 | Add "C-09 PASS. C-16 PASS." to THRESHOLD NOT MET: annotation only; RECOVERY NOTE: left implicit |
| **V-03** | Single-axis: C-20 full (both annotations explicit) | R4 V-05 | Add explicit criterion PASS statements to both THRESHOLD NOT MET: and RECOVERY NOTE: annotations |
| **V-04** | Single-axis: C-19 extended (OBLIGATION A typed schema) | R4 V-05 | Add typed schema block for OBLIGATION A's RECOVERY NOTE: token -- dual typed schemas |
| **V-05** | Full synthesis | R4 V-05 | Dual typed schemas (V-04) + explicit PASS on both annotations (V-03). 150/150 attempt |

**Key design decisions:**
- V-02 vs V-03 tests whether C-20 is symmetric (does it need BOTH annotations explicit, or just one?) -- if V-02 PASSes C-20, the pass condition is weaker than written; if V-02 FAILs and V-03 PASSes, both annotations must declare PASS
- V-04 is the only variation that changes the OBLIGATION A structure; if C-19 PASSes in V-01 (from typed schema alone), V-04 demonstrates the pattern extends to a second obligation without raising the score
- V-05 is the v5 ceiling attempt: both obligations with typed schemas + both annotations with explicit PASS
---------------|------|------|------|------|------|
| C-01..C-16 | PASS | same | same | same | same | same |
| C-17 | PASS | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | FAIL | PASS | PASS | PASS | PASS |
| **C-19** | PASS (unconfirmed) | **PASS** | same | same | **PASS** | **PASS** |
| **C-20** | FAIL | FAIL | PARTIAL? | **PASS** | FAIL | **PASS** |

**Key insight**: C-20 is a declaration criterion like C-18 was -- the mechanism (two annotated dual-criterion tokens) already exists in R4 V-05. The gap is that the annotations describe criteria without confirming their pass status. V-03 tests whether adding "C-09 PASS. C-16 PASS." to each annotation is sufficient. V-02 tests whether partial coverage (one annotation explicit, one implicit) qualifies.

---

## V-01 -- C-19 Baseline Isolation (Typed Schema Without C-18 Annotation)

**Axis**: Single-axis C-19 baseline test
**Hypothesis**: C-19 requires only a typed schema block in the enforcement contract. R4 V-03 already has Token / Schema / Fields / Required when / Unacceptable in OBLIGATION B, with field names `{why_no_sources_qualified}` and `{search_that_would_address_gap}` used verbatim in Phase 3. If C-19 PASSES here with no C-18 annotations present, it confirms C-19 is earned by schema precision alone, independent of the C-18/C-20 annotation infrastructure. Under v5: expected score 130 (C-01..C-16) + 5 (C-17) + 0 (C-18 FAIL) + 5 (C-19) + 0 (C-20 blocked by C-18 FAIL) = 140.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search -- [query used]". Acceptable cell values: real data, or "not found after secondary search -- [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a `TIER EMPTY:` token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                    -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified     -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY: token -- they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search -- [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that required a secondary search, append a recovery note immediately after the table using this format:
`RECOVERY NOTE: [field] for "[title fragment]" -- [outcome: filled / not found after secondary search -- [query]]`

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry, use this format:
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If none found -- produce a TIER EMPTY: token per the OBLIGATION B schema:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- showing engagement with the current state of the field?**
For each entry, use this format:
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none found:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite against your claims?**
For each entry, use this format:
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`

**Q: If none found -- "No contrary evidence" requires a reasoned justification -- silence is not acceptable for this tier:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent -- showing the method predates and validates this work?**
For each entry, use this format:
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none found:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path -- the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 -- C-20 Partial: One Annotation With Explicit PASS (THRESHOLD NOT MET Only)

**Axis**: Single-axis C-20 partial declaration test
**Hypothesis**: C-20 pass condition (c) requires each annotation to "confirm all listed criteria PASS". R4 V-05 annotations describe mechanism but never state PASS explicitly. This variation adds explicit criterion PASS statements to the THRESHOLD NOT MET: annotation only -- the RECOVERY NOTE: annotation is left in the R4 V-05 form. If C-20 still FAILS with one annotation explicit and one implicit, it confirms that both annotations must declare PASS. If C-20 somehow PASSES, it reveals the pass condition is asymmetric. Expected result: C-20 FAIL (one annotation insufficient) or PARTIAL, establishing the need for V-03's full dual-annotation approach.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search -- [query used]". Acceptable cell values: real data, or "not found after secondary search -- [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a `TIER EMPTY:` token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                    -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified     -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY: token -- they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose in this skill: it satisfies the depth threshold observability gate (the source shortfall is recorded in the body, not only in frontmatter, making it checkable without parsing YAML -- C-09 PASS) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS).

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search -- [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that required a secondary search, write a recovery note immediately after the table:
`RECOVERY NOTE: [field] for "[title fragment]" -- [outcome: filled / not found after secondary search -- [query]]`

This token serves dual purpose in this skill: it satisfies the anti-placeholder recovery gate (the recovery step is body-visible and auditable without re-running the search) and extends template-label checkability by adding a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK:.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry, use this format:
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If none found -- produce a TIER EMPTY: token per the OBLIGATION B schema:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- showing engagement with the current state of the field?**
For each entry, use this format:
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none found:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite against your claims?**
For each entry, use this format:
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`

**Q: If none found -- "No contrary evidence" requires a reasoned justification -- silence is not acceptable for this tier:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent -- showing the method predates and validates this work?**
For each entry, use this format:
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none found:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path -- the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 -- C-20 Full: Both Annotations With Explicit PASS Confirmation

**Axis**: Single-axis C-20 full declaration -- explicit PASS on both token annotations
**Hypothesis**: C-20 pass condition (c) says each annotation must "confirm all listed criteria PASS". R4 V-05 annotations name criteria and explain the mechanism but never state PASS. This variation adds explicit "C-09 PASS" / "C-16 PASS" statements to the THRESHOLD NOT MET: annotation and "C-12 PASS" / "C-16 PASS" statements to the RECOVERY NOTE: annotation. If C-20 is a declaration criterion (like C-18 was in R4), these two additions convert it from FAIL to PASS without any structural change. Under v5: expected score 130 + 5(C-17) + 5(C-18) + 5(C-19) + 5(C-20) = 150.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search -- [query used]". Acceptable cell values: real data, or "not found after secondary search -- [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a `TIER EMPTY:` token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                    -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified     -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY: token -- they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose in this skill: it satisfies the depth threshold observability gate (the source shortfall is recorded in the body, not only in frontmatter, making it checkable without parsing YAML -- C-09 PASS) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS).

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search -- [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that required a secondary search, write a recovery note immediately after the table:
`RECOVERY NOTE: [field] for "[title fragment]" -- [outcome: filled / not found after secondary search -- [query]]`

This token serves dual purpose in this skill: it satisfies the anti-placeholder recovery gate (the recovery step is body-visible and auditable without re-running the search -- C-12 PASS) and extends template-label checkability by adding a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS).

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry, use this format:
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If none found -- produce a TIER EMPTY: token per the OBLIGATION B schema:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- showing engagement with the current state of the field?**
For each entry, use this format:
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none found:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite against your claims?**
For each entry, use this format:
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`

**Q: If none found -- "No contrary evidence" requires a reasoned justification -- silence is not acceptable for this tier:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent -- showing the method predates and validates this work?**
For each entry, use this format:
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none found:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path -- the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 -- C-19 Extended: Dual Typed Schema Blocks (OBLIGATION A Schema)

**Axis**: Single-axis C-19 extension -- typed schema block for OBLIGATION A
**Hypothesis**: C-19 requires "at least one" typed schema block and R4 V-05 already satisfies this with OBLIGATION B. But OBLIGATION A uses prose. Adding a parallel typed schema block for OBLIGATION A's RECOVERY NOTE: token creates symmetry: both obligations declare token schemas with authoritative field names. This does not raise the C-19 score (one schema is sufficient) but tests whether dual schemas affect C-20 -- specifically, whether two typed schema tokens (TIER EMPTY: and RECOVERY NOTE:) strengthen the multi-criterion token infrastructure. Under v5: expected score identical to R4 V-05 (145 if C-20 FAIL, or confirms C-19 already passes).

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, record it using the schema below. This schema is authoritative -- the field names defined here govern what Phase 2 must produce for any recovery event.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column requiring secondary search (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and required a follow-up search
Unacceptable: performing a secondary search without writing RECOVERY NOTE:; RECOVERY NOTE: missing any of the three fields; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" without a RECOVERY NOTE:

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a `TIER EMPTY:` token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                    -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified     -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY: token -- they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose in this skill: it satisfies the depth threshold observability gate (the source shortfall is recorded in the body, not only in frontmatter, making it checkable without parsing YAML) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK:.

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search -- [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that required a secondary search, write a recovery note per the OBLIGATION A schema:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose in this skill: it satisfies the anti-placeholder recovery gate (the recovery step is body-visible and auditable without re-running the search) and extends template-label checkability by adding a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK:.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry, use this format:
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If none found -- produce a TIER EMPTY: token per the OBLIGATION B schema:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- showing engagement with the current state of the field?**
For each entry, use this format:
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none found:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite against your claims?**
For each entry, use this format:
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`

**Q: If none found -- "No contrary evidence" requires a reasoned justification -- silence is not acceptable for this tier:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent -- showing the method predates and validates this work?**
For each entry, use this format:
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none found:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path -- the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 -- Full Synthesis (Dual Typed Schemas + C-20 Explicit PASS Confirmation)

**Axes**: C-19 dual schema (OBLIGATION A typed schema for RECOVERY NOTE: -- V-04) + C-20 explicit PASS confirmation on both annotations (V-03)
**Hypothesis**: Theoretical ceiling of the v5 rubric. Both obligations declare typed token schemas with authoritative field names (C-19 max coverage). Both multi-criterion token annotations explicitly confirm criterion pass status (C-20 full compliance). OBLIGATION A's RECOVERY NOTE: schema extends C-19 to the second obligation and creates a parallel schema infrastructure -- the design is holistic. Explicit "C-12 PASS / C-16 PASS" and "C-09 PASS / C-16 PASS" in both annotations closes C-20's declaration gap. Under v5: target 150/150. The two designs are independent -- dual typed schemas and explicit PASS confirmation are orthogonal changes that together constitute the full v5 infrastructure.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, record it using the schema below. This schema is authoritative -- the field names defined here govern what Phase 2 must produce for any recovery event.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column requiring secondary search (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and required a follow-up search
Unacceptable: performing a secondary search without writing RECOVERY NOTE:; RECOVERY NOTE: missing any of the three fields; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" without a RECOVERY NOTE:

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a `TIER EMPTY:` token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                    -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified     -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY: token -- they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose in this skill: it satisfies the depth threshold observability gate (the source shortfall is recorded in the body, not only in frontmatter, making it checkable without parsing YAML -- C-09 PASS) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS).

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search -- [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that required a secondary search, write a recovery note per the OBLIGATION A schema:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose in this skill: it satisfies the anti-placeholder recovery gate (the recovery step is body-visible and auditable without re-running the search -- C-12 PASS) and extends template-label checkability by adding a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS).

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry, use this format:
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If none found -- produce a TIER EMPTY: token per the OBLIGATION B schema:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- showing engagement with the current state of the field?**
For each entry, use this format:
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none found:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite against your claims?**
For each entry, use this format:
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`

**Q: If none found -- "No contrary evidence" requires a reasoned justification -- silence is not acceptable for this tier:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent -- showing the method predates and validates this work?**
For each entry, use this format:
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none found:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path -- the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
