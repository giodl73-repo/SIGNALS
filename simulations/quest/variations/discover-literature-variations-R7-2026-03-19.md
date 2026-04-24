Done. Written to `simulations/quest/variations/discover-literature-variations-R7-2026-03-19.md`.

---

## discover-literature -- Variations R7

**5 variations targeting C-22. Two new axes: lifecycle token vocabulary, dense phase instrumentation.**

### Variation Map

| ID | Axis | Base | Key change | Predicted v7 |
|----|------|------|------------|--------------|
| **V-01** | C-22 baseline | R6 V-04 | Strengthen PHASE N COMPLETE: annotations to explicitly name unconditional emission + C-22 | **160** |
| **V-02** | Lifecycle vocabulary | R6 V-04 | Domain-named tokens (EVIDENCE PHASE COMPLETE: + MAP PHASE COMPLETE:) -- **critical experiment** | **160?** |
| **V-03** | Dense lifecycle (all 4 phases) | R6 V-05 | PHASE 1..4 COMPLETE: each annotated with boundary + criteria | **160** |
| **V-04** | C-22 + inertia front-loading | R6 V-03 + V-04 | Pre-committed inertia + lifecycle tokens -- tests C-22 orthogonal to inertia axis | **160** |
| **V-05** | v7 ceiling synthesis | R6 V-05 + V-04 | All 22 criteria: dual schemas + explicit PASS (both token paths) + inertia front-loading | **160** |

### The critical experiment: V-02

R6 confirmed C-20 is token-agnostic (any two annotated tokens with 3 distinct criteria). V-02 runs the same test for C-22: does it require `PHASE N COMPLETE:` specifically, or does any unconditional boundary token with a boundary-naming annotation qualify?

- `EVIDENCE PHASE COMPLETE:` at end of Phase 2 -- names the "Phase 2 boundary", covers C-09 + C-16
- `MAP PHASE COMPLETE:` at end of Phase 3 -- names the "Phase 3 boundary", covers C-13 + C-16

**C-22 PASS confirms token-agnosticism. C-22 FAIL reveals an implicit naming constraint not in the rubric text.**

### Key structural design notes across all 5

All variations preserve the dual typed schema contract (OBLIGATION A + OBLIGATION B with full Token/Schema/Fields/Required when/Unacceptable blocks) -- C-21 PASS floor is maintained. The only criterion gap from R6 is C-22; every variation targets it by ensuring at least two lifecycle tokens fire unconditionally at phase boundaries. V-01 is the minimum-change baseline; V-05 is the maximum-coverage ceiling.
rch)? (V-04)

### Predicted scores under v7

| | v7 score | C-22 | C-21 | C-20 | C-18 |
|--|----------|------|------|------|------|
| V-01 | 160 | PASS | PASS | PASS | PASS |
| V-02 | 160? | PASS? | PASS | PASS | PASS |
| V-03 | 160 | PASS | PASS | PASS | PASS |
| V-04 | 160 | PASS | PASS | PASS | PASS |
| V-05 | 160 | PASS | PASS | PASS | PASS |

V-02 carries the experimental uncertainty: C-22 PASS confirms token-agnosticism; C-22 FAIL reveals an implicit naming constraint not stated in the pass condition.

---

## V-01 -- C-22 Baseline Confirmation

**Axis**: C-22 baseline isolation
**Hypothesis**: R6 V-04 already has PHASE 2 COMPLETE: and PHASE 3 COMPLETE: tokens that fire unconditionally at phase boundaries. Under v7, these tokens should satisfy C-22 because they (a) emit regardless of threshold outcome, (b) are present in both MET and NOT MET runs, and (c) their annotations already name the phase boundary. This variation strengthens those annotations to explicitly state unconditional emission and name C-22. Expected score: 160/160 (C-22 PASS is the only criterion gap from R6 V-04's 155/155).

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

This token emits unconditionally at the Phase 2 boundary -- every run, whether the threshold was met or not, produces PHASE 2 COMPLETE:; only the status field differs. Unconditional emission makes threshold compliance verifiable in every run outcome: source count and threshold are always co-located at this specific Phase 2 boundary point, readable without scanning the full body or parsing frontmatter (C-09 PASS). Adds a fifth named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress).

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

This token emits unconditionally at the Phase 3 boundary -- every run, whether tiers were fully populated or contained empty entries, produces PHASE 3 COMPLETE:. Unconditional emission makes empty-tier compliance verifiable in every run outcome: `tiers_empty_acknowledged=[yes/no]` surfaces whether every empty tier produced a TIER EMPTY: token, eliminating the need to scan all four tier sections individually (C-13 PASS). Adds a sixth named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied.

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

## V-02 -- Lifecycle Token Vocabulary (Domain-Named Tokens)

**Axis**: Single-axis lifecycle vocabulary
**Hypothesis**: C-22 requires unconditional phase-boundary tokens with annotations naming the phase boundary and covering multiple criteria. The pass condition specifies no required token names. This variation replaces `PHASE 2 COMPLETE:` with `EVIDENCE PHASE COMPLETE:` and `PHASE 3 COMPLETE:` with `MAP PHASE COMPLETE:` -- domain-named alternatives that convey what happened at the boundary rather than where the run is. Each annotation names the phase boundary explicitly and carries multi-criterion PASS statements. If C-22 PASSes here, the criterion is token-agnostic: any unconditional boundary token with a boundary-naming annotation qualifies. If C-22 FAILs, there is an implicit naming constraint in the pass condition not visible in the rubric text. Under v7: C-21 PASS, C-20 PASS (lifecycle token path), C-22 PASS?, expected score 160/160.

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
`EVIDENCE PHASE COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces EVIDENCE PHASE COMPLETE:, whether the threshold was met or not. Unconditional emission at the Phase 2 boundary makes threshold compliance verifiable in every run outcome: source count and threshold are co-located at this specific boundary point (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress).

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
`MAP PHASE COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary -- every run produces MAP PHASE COMPLETE:, whether all tiers were populated or some were empty. Unconditional emission at the Phase 3 boundary makes empty-tier compliance verifiable in every run outcome: `tiers_empty_acknowledged=[yes/no]` surfaces TIER EMPTY: coverage at this specific Phase 3 boundary point without scanning all four tier sections (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied.

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

## V-03 -- Dense Phase Instrumentation (All 4 Phases)

**Axis**: Single-axis lifecycle emphasis (full phase instrumentation)
**Hypothesis**: R6 V-04/V-05 instrument only Phase 2 and Phase 3 with unconditional lifecycle tokens. C-22 requires only two such tokens, so Phase 2 and Phase 3 already satisfy it. Adding PHASE 1 COMPLETE: and PHASE 4 COMPLETE: tokens -- each annotated with the phase boundary and the additional criteria they cover -- increases observability across all phase gates. The design question: does full-phase instrumentation strengthen C-16 (more named tokens), C-11 (Phase 1 completeness visible at boundary), and C-14 (inertia compliance visible at Phase 4 boundary), without adding friction? Under v7: all 22 criteria PASS, expected score 160/160.

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
`PHASE 1 COMPLETE: claims=[n] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]`

This token emits unconditionally at the Phase 1 boundary -- every run produces PHASE 1 COMPLETE:, whether claims are simple or complex. Surfaces claim count and whether the interrogative obligation was discharged (evidence types and counter-evidence types mapped per claim), making Phase 1 completeness checkable at a single boundary point (C-11 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Emits unconditionally at the Phase 1 boundary -- beyond the two-token minimum for C-22, extending observability to the earliest phase gate.

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

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. Unconditional emission makes threshold compliance verifiable in every run outcome at this specific Phase 2 boundary point (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress).

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers were populated or some were empty. Unconditional emission makes empty-tier compliance verifiable in every run outcome at this specific Phase 3 boundary point (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied.

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
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes/no] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 boundary -- every run produces PHASE 4 COMPLETE:, whether the recommendation is PROCEED, SEARCH MORE, or REFRAME CLAIM. `inertia_named=[yes/no]` surfaces whether the required INERTIA SCENARIO: gate was discharged before the recommendation keyword, making inertia obligation compliance checkable at the Phase 4 boundary (C-14 PASS for checking; C-16 PASS). Emits unconditionally at the Phase 4 boundary -- extends the unconditional lifecycle pattern beyond the C-22 minimum, making all four phases fully instrumented.

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

## V-04 -- C-22 + Inertia Front-Loading

**Axis**: C-22 + inertia framing (pre-committed inertia scenario before any search)
**Hypothesis**: R6 V-03 tested inertia front-loading but had no lifecycle tokens and therefore C-22 FAIL. This variation merges R6 V-03's inertia front-loading axis with R6 V-04's lifecycle token infrastructure. The inertia scenario is committed in Phase 1 before any search; Phase 4 verifies the evidence against that commitment. The design question: is C-22 orthogonal to the inertia front-loading axis -- does pre-commitment in Phase 1 affect lifecycle token emission at Phase 2 and Phase 3 boundaries? It should not: lifecycle tokens fire at phase boundaries regardless of when the inertia scenario was named. C-20 is satisfied via the lifecycle token path (PHASE 2 COMPLETE: + PHASE 3 COMPLETE: with explicit PASS). Under v7: C-21 PASS, C-20 PASS, C-22 PASS, expected score 160/160.

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

### INERTIA COMMITMENT (required gate before Phase 2 begins)

Before searching a single paper, commit to what inertia looks like for this topic. Phase 4 will measure the evidence gathered against this commitment.

Answer: what would a team do if they ignored this literature entirely?
Name the default path -- the behavior that requires no effort.

```
INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]
```

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | counter-evidence-noted=[yes/no]`

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

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. Unconditional emission makes threshold compliance verifiable in every run outcome at the Phase 2 boundary (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress). This token is orthogonal to the inertia front-loading axis: whether the inertia scenario was committed before or after this phase, PHASE 2 COMPLETE: fires unconditionally at the Phase 2 boundary.

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers were populated or some were empty. Unconditional emission makes empty-tier compliance verifiable in every run outcome at the Phase 3 boundary (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied. This token is orthogonal to the inertia front-loading axis: PHASE 3 COMPLETE: fires unconditionally at the Phase 3 boundary regardless of the inertia framing design.

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

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

**Q: Does the literature make the inertia default worse than acting on this evidence?**
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If recommending SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

```
INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]
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

## V-05 -- v7 Ceiling Synthesis (All 22 Criteria)

**Axes**: All prior dimensions: dual typed schemas (C-21) + explicit PASS on canonical token annotations (C-20 first path) + unconditional lifecycle tokens with explicit C-22 annotation (C-22 + C-20 second path) + inertia front-loading (C-14 maximum)
**Hypothesis**: Ceiling attempt for v7. Four independent improvements are additive: (1) dual typed schemas close the asymmetric enforcement surface (C-21 PASS); (2) explicit "C-NN PASS" on canonical THRESHOLD NOT MET:/RECOVERY NOTE: annotations closes the declaration gap (C-20 first path); (3) unconditional lifecycle tokens PHASE 2 COMPLETE: and PHASE 3 COMPLETE: with C-22 annotation close the happy-path observability gap (C-22 PASS; C-20 second path); (4) inertia front-loading pre-commits the scenario before any search (C-14 maximum). Under v7: all 22 criteria PASS, expected score 160/160.

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

### INERTIA COMMITMENT (required gate before Phase 2 begins)

Before searching a single paper, commit to what inertia looks like for this topic. Phase 4 will measure the evidence gathered against this commitment.

Answer: what would a team do if they ignored this literature entirely?
Name the default path -- the behavior that requires no effort.

```
INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]
```

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | counter-evidence-noted=[yes/no]`

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

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run that meets its threshold still produces PHASE 2 COMPLETE: with status=MET, making threshold compliance verifiable in every run outcome at the Phase 2 boundary (C-09 PASS). Adds a fifth named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress).

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers were populated or some were empty. This is the decisive observability upgrade for empty-tier compliance: a run with all tiers populated still produces PHASE 3 COMPLETE: with tiers_empty=0, making compliance verifiable in every run outcome at the Phase 3 boundary (C-13 PASS). Adds a sixth named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied.

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

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

**Q: Does the literature make the inertia default worse than acting on this evidence?**
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If recommending SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

```
INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]
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
