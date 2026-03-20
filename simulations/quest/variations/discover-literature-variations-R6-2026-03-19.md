Done. Written to `simulations/quest/variations/discover-literature-variations-R6-2026-03-19.md`.

---

## discover-literature -- Variations R6

**5 variations targeting C-21, with three new axes: phrasing register, inertia front-loading, lifecycle completion tokens.**

### Variation Map

| ID | Axis | Base | Key change | Predicted |
|----|------|------|------------|-----------|
| **V-01** | C-21 baseline | R5 V-04 | Identity -- dual schemas, no annotation PASS | 150 |
| **V-02** | Phrasing register (conversational) | R5 V-04 | Second-person investigative voice; schemas intact | 150 |
| **V-03** | Inertia framing (front-loaded) | R5 V-04 | INERTIA COMMITMENT gate after Phase 1; Phase 4 becomes verification | 150 |
| **V-04** | Lifecycle emphasis (completion tokens) | R5 V-04 | `PHASE 2 COMPLETE:` (C-09+C-16 PASS) + `PHASE 3 COMPLETE:` (C-13+C-16 PASS) -- tests if lifecycle tokens are a valid alternative C-18/C-20 path | 150 or **155** |
| **V-05** | Full synthesis | R5 V-05 | Dual schemas + explicit PASS on THRESHOLD NOT MET:/RECOVERY NOTE: + lifecycle tokens | **155** |

### The critical experiment: V-04

V-04 is the diagnostic. It deliberately avoids explicit PASS on the canonical `THRESHOLD NOT MET:`/`RECOVERY NOTE:` annotations and instead annotates two new tokens:

- `PHASE 2 COMPLETE:` -- covers **C-09** (threshold status visible in body) + **C-16** (named token), with `C-09 PASS. C-16 PASS.`
- `PHASE 3 COMPLETE:` -- covers **C-13** (empty-tier acknowledgment visible at boundary) + **C-16** (named token), with `C-13 PASS. C-16 PASS.`

**Two tokens, three distinct aspirational criteria (C-09, C-13, C-16).** If C-20 PASSes from this pair, it is token-agnostic -- any two annotated tokens with 3 distinct criteria qualify. If it FAILs, the rubric has an implicit constraint not written in the pass condition.

V-05 adds the traditional path on top for guaranteed coverage.
PASS on THRESHOLD NOT MET:/RECOVERY NOTE: annotations (C-20) + lifecycle completion tokens (V-04) |

**Key design questions for R6:**
- Does C-21 hold across phrasing register (V-02) and inertia framing (V-03) axis changes?
- Can PHASE N COMPLETE: tokens annotated as C-09+C-16 and C-13+C-16 constitute a valid C-18/C-20 path independent of the canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair? (V-04)
- V-04 PASS on C-20 would reveal C-20 is token-agnostic (any two tokens, any three aspirational criteria); FAIL would reveal an implicit constraint not stated in the rubric

Predicted scores under v6:

| | v6 score | C-21 | C-20 | C-18 |
|--|----------|------|------|------|
| V-01 | 150 | PASS | FAIL | FAIL |
| V-02 | 150 | PASS | FAIL | FAIL |
| V-03 | 150 | PASS | FAIL | FAIL |
| V-04 | 150 or 155 | PASS | PASS? | PASS? |
| V-05 | 155 | PASS | PASS | PASS |

---

## V-01 -- C-21 Baseline Confirmation

**Axis**: C-21 baseline isolation
**Hypothesis**: R5 V-04 already has dual typed schemas for both obligations. This variation reproduces it verbatim under v6. Under v6: C-21 PASS (5 pts), C-20 FAIL, C-18 PASS (from THRESHOLD NOT MET: dual-purpose annotation -- criterion names present but no explicit "C-NN PASS" confirmation). Expected score: 150/155.

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
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence explaining why the tier has no entries
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

## V-02 -- Conversational Register With Dual Schemas

**Axis**: Single-axis phrasing register (conversational / investigative second-person)
**Hypothesis**: C-21 is a structural criterion: it requires Token/Schema/Fields/Required when/Unacceptable blocks for both obligations. The surrounding instructional phrasing is irrelevant -- a schema block in conversational voice is still a schema block. If C-21 PASSes here with identical schema blocks embedded in conversational prose, it confirms the criterion is structure-dependent, not register-dependent. Under v6: C-21 PASS, C-20 FAIL, expected score 150/155.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You need to reach the source threshold for your active depth mode before moving to Phase 3.

---

## TWO NON-NEGOTIABLE RULES (read before you begin)

Before you search a single paper, internalize two rules that apply to everything you produce in this run. Neither rule can be skipped, abbreviated, or silently bypassed.

**RULE 1 (OBLIGATION A) -- No Blank Cells**
Every cell in your citation table must contain real data or an explicit recovery record. If you cannot fill a cell on the first try, run another search. If that search also fails, record the failure using the schema below. This schema is authoritative: the variable names here are the variable names you must use in Phase 2.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- which column failed (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short fragment to identify the source
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any cell was unknown at first pass and required a follow-up search
Unacceptable: leaving a cell blank; writing "Author et al.", "[title]", "TBD", "n/a", or "unknown" without a RECOVERY NOTE:; searching again without recording the outcome

**RULE 2 (OBLIGATION B) -- No Silent Tiers**
Every tier of your four-tier literature map must produce output. If a tier has no qualifying sources, write a TIER EMPTY: token -- do not leave the tier heading bare. The schema below is authoritative: these variable names govern what you write in Phase 3.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence: why nothing qualifies for this tier
  search_that_would_address_gap -- one concrete WebSearch you would try next
Required when: a tier produces zero qualifying source entries
Unacceptable: a tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: missing any of the three fields

Both rules start now and stay active through Phase 5. When a phase asks "if unknown" -- search, then record the result. When a phase asks "if none found" -- write the TIER EMPTY: token. Silence is not an answer.

---

## PHASE 1 -- What claims does this work make?

You are investigating literature for: {{topic}}

Work through these questions before you open a search window:

1. What are the 3-5 claims your work makes about {{topic}} that a reviewer would demand literature support for? State each as a proposition, not a question.
2. For each claim: what kind of evidence would a reviewer find convincing? An empirical study? A theoretical argument? A methodological precedent?
3. For each claim: what would a skeptic reach for? Name the type of challenge they would make.

Check any prior signals first (discover-hypothesis, specify-spec, paper draft) -- they may already frame these claims.

---

## PHASE 2 -- What does the literature actually say?

Your target: reach the threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, work through these four search angles:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish methodological precedent for this work? (WebSearch: "[claim topic] method")

Still short of threshold after all four angles? Keep going:
5. Search adjacent territory: (WebSearch: "[related concept] [claim topic]")
6. Follow citations: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Keep searching until you hit the threshold or exhaust all angles. If you cannot reach the threshold, record it:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose in this skill: it makes the threshold shortfall visible in the body without requiring YAML parsing, and it adds a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK:.

Before entering each source in the table, answer these questions:

- Full title? If you cannot find it after WebSearch "[fragment] full title", write: "not found after secondary search -- [query used]"
- Authors by real last name (no "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search -- [query used]"
- Publication year? If unknown after WebSearch "[title] publication year", write: "not found after secondary search -- [query used]"
- Venue (journal, conference, or preprint server)? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search -- [query used]"
- Which Claim # does this source bear on?
- Does it support, contradict, or qualify that claim?
- Key finding in one sentence?

Enter sources in the citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

After the table, for any cell that needed a secondary search, write a recovery note using the RULE 1 schema:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose in this skill: it makes your recovery step auditable in the body without re-running the search, and it adds a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK:.

No cell may contain a placeholder without a recovery note. (RULE 1)

---

## PHASE 3 -- How does the literature organize?

For each tier below, answer both questions. Neither can be left blank. (RULE 2 governs all four tiers -- produce TIER ENTRY: or TIER EMPTY: for each.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`

**Q: If you found none, explain why and what you would search next:**
`TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) -- evidence you are engaging with the current field?**
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`

**Q: If none:**
`TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- papers a hostile reviewer would cite against your claims?**
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection]`

**Q: If none -- "no contrary evidence" requires a reasoned justification, not silence:**
`TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish the methodological precedent -- showing your method predates this work?**
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`

**Q: If none:**
`TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

---

## PHASE 4 -- Where are the gaps and what do you do about them?

Work through these five questions, then make your commitment on the inertia scenario before you write a recommendation keyword.

1. How many of your claims have strong support (>= 2 sources)? Name them.
2. How many claims have weak or no support? Name them.
3. Which contrary papers are most dangerous? Order them from most to least threatening.
4. Do any claims have no support AND strong contrary evidence? For each HIGH RISK claim: scope, qualify, or drop?
5. Overall: how strong is your evidence position going into this work?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [most dangerous first]
HIGH RISK claims: [list or "none"]
  For each: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (write this before your recommendation keyword)

Before you decide PROCEED, SEARCH MORE, or REFRAME CLAIM, answer these:

**Q: What would your team do if they ignored this entire literature review?**
Name the default -- the path that takes zero effort.

**Q: What does the evidence you gathered reveal about why that default is dangerous?**
If recommending PROCEED: show why the evidence is strong enough to act over inertia. If recommending SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

```
INERTIA SCENARIO: [the default team behavior if this review is ignored]
INERTIA RISK: [why that default leads to a worse outcome]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support? What should you search for next?
2. Which contrary paper demands a direct response? What is your rebuttal direction? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing? Where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 -- Inertia Front-Loading (Commitment Gate in Phase 1)

**Axis**: Single-axis inertia framing (front-loaded commitment)
**Hypothesis**: In R5 variations, the inertia scenario first appears in Phase 4 as a gate before the recommendation keyword. Front-loading it to Phase 1 -- asking the team to commit to what inertia looks like BEFORE they see the literature -- creates a pre-search hypothesis that Phase 4 then tests against evidence. C-14 still PASSes: the inertia scenario governs the recommendation. C-16 still PASSes: INERTIA SCENARIO: and INERTIA RISK: tokens still appear. The design question: does Phase 4 analysis improve when the team cannot rationalize the inertia scenario post-hoc? Under v6: C-21 PASS, C-20 FAIL, expected score 150/155.

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
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence explaining why the tier has no entries
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

### INERTIA COMMITMENT (required before Phase 2 begins)

Before you see a single paper, commit to what inertia looks like for this topic. You will measure your evidence against this commitment in Phase 4.

Answer: what would a team do if they ignored this literature entirely?
Name the default path -- the behavior that requires no effort.

```
INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]
```

Hold this scenario. Phase 4 will ask whether the literature you find makes this default worse than acting.

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

Answer these five questions, then complete the inertia verification block before writing the recommendation keyword.

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

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO you committed in Phase 1. Measure the evidence you gathered against it.

**Q: Does the literature make the inertia default worse than acting on this evidence?**
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If recommending SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

```
INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]
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

## V-04 -- Lifecycle Emphasis: Phase Completion Tokens as Alternative C-18/C-20 Path

**Axis**: Single-axis lifecycle emphasis (PHASE N COMPLETE: tokens at phase boundaries)
**Hypothesis**: C-20 requires two distinct named tokens each annotated as covering 2+ criteria with 3 distinct aspirational criteria named total. The canonical path uses THRESHOLD NOT MET: (C-09+C-16) and RECOVERY NOTE: (C-12+C-16). This variation introduces a new path: PHASE 2 COMPLETE: and PHASE 3 COMPLETE: tokens, each annotated with explicit PASS statements. PHASE 2 COMPLETE: makes threshold status verifiable at the phase boundary regardless of whether threshold was met or not (C-09 PASS for both cases) + adds a named token (C-16 PASS). PHASE 3 COMPLETE: makes empty-tier acknowledgment status verifiable at the phase boundary (C-13 PASS) + adds a named token (C-16 PASS). Together: two distinct tokens, three distinct aspirational criteria (C-09, C-13, C-16). If C-20 PASSes from this pair without explicit PASS on THRESHOLD NOT MET:/RECOVERY NOTE: annotations, C-20 is token-agnostic. Under v6: C-21 PASS (dual schemas), C-18 PASS?, C-20 PASS?, expected score 150 or 155.

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
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence explaining why the tier has no entries
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

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | counter-evidence-noted=[yes/no]`

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

This token records the threshold shortfall in the body for auditing without requiring YAML parsing, and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK:.

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

This token makes the recovery step body-visible and auditable without re-running the search, and adds a named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK:.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token serves dual purpose in this skill: it surfaces depth threshold compliance at the phase boundary -- whether threshold was met or not, the source count and threshold are co-located and checkable without parsing frontmatter (C-09 PASS), and it adds a fifth named gate token for template-label checkability (C-16 PASS).

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

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token serves dual purpose in this skill: it makes empty-tier acknowledgment compliance verifiable at the phase boundary -- `tiers_empty_acknowledged=[yes/no]` signals whether every empty tier produced a TIER EMPTY: token, eliminating the need to scan all tier sections individually (C-13 PASS), and it adds a sixth named gate token for template-label checkability (C-16 PASS).

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

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | high_risk_claims=[n]`

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

## V-05 -- Full Synthesis (Dual Typed Schemas + C-20 Explicit PASS + Lifecycle Tokens)

**Axes**: C-21 dual typed schemas (R5 V-04) + C-20 explicit PASS on canonical annotations (R5 V-05) + lifecycle PHASE N COMPLETE: tokens (R6 V-04)
**Hypothesis**: Ceiling attempt for v6. Three independent improvements are additive: (1) dual typed schemas close the asymmetric enforcement surface (C-21 PASS); (2) explicit "C-NN PASS" on both THRESHOLD NOT MET: and RECOVERY NOTE: annotations closes the declaration gap (C-20 PASS); (3) lifecycle tokens PHASE 2 COMPLETE: and PHASE 3 COMPLETE: provide observable phase-boundary checkpoints as belt-and-suspenders multi-criterion infrastructure. Under v6: all 21 criteria PASS, expected score 155/155.

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
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence explaining why the tier has no entries
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

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | counter-evidence-noted=[yes/no]`

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

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token surfaces depth threshold compliance at the phase boundary -- source count and threshold are co-located and checkable without parsing frontmatter (C-09 PASS), and adds a fifth named gate token for template-label checkability (C-16 PASS).

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

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token makes empty-tier acknowledgment compliance verifiable at the phase boundary -- `tiers_empty_acknowledged=[yes/no]` indicates whether every empty tier produced a TIER EMPTY: token (C-13 PASS), and adds a sixth named gate token for template-label checkability (C-16 PASS).

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

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | high_risk_claims=[n]`

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
