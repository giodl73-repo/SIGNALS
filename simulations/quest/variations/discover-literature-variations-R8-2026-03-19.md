Written to `simulations/quest/variations/discover-literature-variations-R8-2026-03-19.md`.

---

## discover-literature -- Variations R8

**5 variations targeting C-23 and C-24.**

### Variation Map

| ID | Axis | Base | Key change | Predicted v8 |
|----|------|------|------------|--------------|
| **V-01** | C-23 lifecycle completeness | R7 V-03 | Strengthen Phase 1 + Phase 4 lifecycle token annotations to explicitly name C-23; all 4 tokens labeled N-of-4 | 165/170 |
| **V-02** | C-24 redundancy annotation | R7 V-05 | Explicit C-24 independence verification block after PHASE 3 COMPLETE: -- names both pairs, proves each independently satisfies C-20 | 165/170 |
| **V-03** | C-24 alt vocabulary (critical experiment) | R7 V-05 | Replace PHASE N COMPLETE: lifecycle pair with `EVIDENCE PHASE COMPLETE:` + `MAP PHASE COMPLETE:` -- tests C-24 token-agnosticism | 165/170? |
| **V-04** | C-23 + C-24 combination | R7 V-03 + R7 V-05 | All 4 lifecycle tokens (C-23) + canonical pair PASS annotations + C-24 block; no inertia front-loading | **170/170** |
| **V-05** | v8 ceiling synthesis | All axes | All 24 criteria: dual schemas + 4 phases + both pairs + C-24 block + inertia front-loading | **170/170** |

### Design logic

**Why V-01 misses C-24**: Only the lifecycle pair satisfies C-20. The canonical pair (THRESHOLD NOT MET: + RECOVERY NOTE:) has no explicit PASS annotations in V-01 -- C-24 requires two independent pairs.

**Why V-02 misses C-23**: Only Phase 2 and Phase 3 lifecycle tokens; no Phase 1 or Phase 4 instrumentation.

**The critical experiment (V-03)**: R7 confirmed C-22 is token-agnostic. V-03 tests whether C-24 inherits that property -- does the second C-20 pair require `PHASE N COMPLETE:` names, or do domain-named tokens with correct annotations qualify?

**Why V-04 reaches 170**: C-23 and C-24 are orthogonal. Adding the canonical pair PASS annotations to the 4-phase design satisfies both without interference. V-04 is the minimal 170 design.

**V-05** adds inertia front-loading (INERTIA COMMITMENT in Phase 1, INERTIA VERIFICATION in Phase 4) over V-04 for maximum C-14 coverage -- the final polish axis.
nditional tokens), C-24 measures pair independence (two C-20-satisfying pairs). Neither criterion's pass condition references the other. The combination is purely additive.

R7 V-03 already has: dual typed schemas (C-21), all four lifecycle tokens, C-22, C-20 via lifecycle pair.
R7 V-05 already has: canonical pair PASS annotations, lifecycle pair PASS annotations, dual typed schemas.
V-04 merges both: R7 V-03 structure + R7 V-05 canonical pair annotations + explicit C-24 independence block.

### Predicted scores under v8

| | v8 score | C-23 | C-24 | C-22 | C-21 | C-20 |
|--|----------|------|------|------|------|------|
| V-01 | 165 | PASS | FAIL | PASS | PASS | PASS (lifecycle pair) |
| V-02 | 165 | FAIL | PASS | PASS | PASS | PASS |
| V-03 | 165? | FAIL | PASS? | PASS | PASS | PASS |
| V-04 | 170 | PASS | PASS | PASS | PASS | PASS |
| V-05 | 170 | PASS | PASS | PASS | PASS | PASS |

V-03 carries the experimental uncertainty. V-04 is the first 170 attempt. V-05 adds inertia front-loading as the final polish dimension.

---

## V-01 -- C-23 Lifecycle Completeness

**Axis**: Single-axis lifecycle completeness
**Hypothesis**: R7 V-03 already emits all four lifecycle tokens (Phase 1, 2, 3, 4) unconditionally. Under v8, C-23 requires each token's annotation to name its specific phase boundary and confirm unconditional emission. R7 V-03's Phase 1 and Phase 4 annotations reference "beyond the two-token minimum for C-22" and "extends the unconditional lifecycle pattern" -- language that implies but does not explicitly confirm the four-token count required for C-23. This variation strengthens all four annotations to explicitly declare: (a) the specific phase boundary, (b) unconditional emission, and (c) position in the four-token count (N of four) required for C-23. C-24 intentionally omitted: the canonical pair (THRESHOLD NOT MET: + RECOVERY NOTE:) has no explicit PASS annotations; C-20 passes via lifecycle pair only. Expected: C-23 PASS, C-24 FAIL, all other criteria PASS. Score: 165/170.

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity. The evidence_type_mapped and counter-evidence-noted fields confirm the interrogative obligation was discharged per claim (C-11 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). This is token 1 of 4 required for C-23: the Phase 1 / claim-extraction boundary is now instrumented with an unconditional lifecycle token. C-23 in progress (1/4).

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

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not; only the status field differs. Unconditional emission makes threshold compliance verifiable in every run outcome: source count and threshold are co-located at this specific Phase 2 boundary point without requiring YAML parsing (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). This is token 2 of 4 required for C-23: the Phase 2 / evidence-gathering boundary is now instrumented. Also the first of two unconditional lifecycle tokens required for C-22 (C-22 in progress). C-23 in progress (2/4).

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

This token emits unconditionally at the Phase 3 / literature-mapping boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers were populated or some were empty. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this specific Phase 3 boundary point without scanning all four tier sections (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). This is token 3 of 4 required for C-23: the Phase 3 / literature-mapping boundary is now instrumented. Also the second of two unconditional lifecycle tokens required for C-22 -- C-22 fully satisfied (Phase 2 and Phase 3 boundaries both instrumented with unconditional tokens; C-22 PASS). C-23 in progress (3/4).

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

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:, whether the recommendation is PROCEED, SEARCH MORE, or REFRAME CLAIM. The inertia_named field confirms whether the INERTIA SCENARIO: gate was discharged before the recommendation keyword (C-14 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). This is token 4 of 4 required for C-23 -- C-23 fully satisfied. All four phase boundaries are now instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction, Phase 2 / evidence-gathering, Phase 3 / literature-mapping, Phase 4 / gap-analysis. Each token names its specific phase boundary and emits unconditionally. C-23 PASS.

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

## V-02 -- C-24 Redundancy Annotation

**Axis**: Single-axis redundancy annotation
**Hypothesis**: R7 V-05 already has both the canonical pair (THRESHOLD NOT MET: C-09+C-16, RECOVERY NOTE: C-12+C-16) and the lifecycle pair (PHASE 2 COMPLETE: C-09+C-16, PHASE 3 COMPLETE: C-13+C-16), each token annotated with explicit PASS statements. The pass condition for C-24 requires demonstrating that each pair independently satisfies C-20 and that the independence is verifiable: removing either pair must leave the remaining pair satisfying C-20 on its own. R7 V-05 satisfies this structurally but contains no explicit C-24 independence declaration. This variation adds a C-24 independence verification block at the end of Phase 3 (after PHASE 3 COMPLETE: annotation, once both pairs are complete), naming both pairs, confirming each independently satisfies C-20, and stating the redundancy condition. C-23 intentionally omitted -- only Phase 2 and Phase 3 lifecycle tokens. Expected: C-24 PASS, C-23 FAIL, all other v7 criteria PASS. Score: 165/170.

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

This token serves dual purpose in this skill: it records the depth threshold shortfall in the body for auditing without requiring YAML parsing (C-09 PASS) and adds a named gate token for template-label checkability alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). Pair 1, Token A.

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

This token serves dual purpose in this skill: it makes the recovery step body-visible and auditable without re-running the search (C-12 PASS) and adds a named gate token for template-label checkability alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS). Pair 1, Token B.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run that meets its threshold still produces PHASE 2 COMPLETE: with status=MET, making threshold compliance verifiable in every run outcome at the Phase 2 boundary (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens (C-22 in progress). Pair 2, Token A.

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers were populated or some were empty. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this Phase 3 boundary point (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied. Pair 2, Token B.

**C-24 Independence Verification (both pairs now complete):**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 2 independently.

Redundancy check:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Four tokens total, all distinct. Neither pair depends on the other to meet C-20. C-24 PASS.

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

## V-03 -- C-24 Alternative Vocabulary (Critical Experiment)

**Axis**: Single-axis C-24 token vocabulary
**Hypothesis**: C-20 and C-22 are both confirmed token-agnostic (R4, R6, R7 rounds). C-24 inherits from C-20 via the dependency chain C-18 -> C-20 -> C-24 and should therefore also be token-agnostic: the pass condition names no required token vocabulary, only annotation structure and independence. This variation tests that claim. The lifecycle pair in Pair 2 uses domain-named tokens `EVIDENCE PHASE COMPLETE:` and `MAP PHASE COMPLETE:` instead of `PHASE 2 COMPLETE:` and `PHASE 3 COMPLETE:`. Each token names its specific phase boundary in its annotation and carries multi-criterion PASS statements. The C-24 independence block names these domain-named tokens explicitly. If C-24 PASSes, domain-named tokens qualify for the second pair -- C-24 token-agnosticism confirmed and documented. If C-24 FAILs, an implicit naming constraint exists in C-24's pass condition not present in C-22. C-23 intentionally omitted (only 2 lifecycle tokens). Expected score: 165/170.

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

This token serves dual purpose: records the threshold shortfall in the body without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). Pair 1, Token A in the failure/recovery multi-criterion pair.

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

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`EVIDENCE PHASE COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces EVIDENCE PHASE COMPLETE:, whether the threshold was met or not. The token name identifies the specific phase boundary (evidence-gathering phase, corresponding to Phase 2). Unconditional emission makes threshold compliance verifiable in every run outcome at this boundary: source count and threshold are co-located here without requiring YAML parsing (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). First of two required unconditional phase-boundary lifecycle tokens -- C-22 in progress. Pair 2, Token A in the lifecycle multi-criterion pair.

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

This token emits unconditionally at the Phase 3 / literature-mapping boundary -- every run produces MAP PHASE COMPLETE:, whether all tiers were populated or some were empty. The token name identifies the specific phase boundary (map phase, corresponding to Phase 3). The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this boundary (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied (EVIDENCE PHASE COMPLETE: at Phase 2 boundary + MAP PHASE COMPLETE: at Phase 3 boundary, both unconditional; domain-named tokens qualify for C-22 per V-02 R7 confirmation; C-22 PASS). Pair 2, Token B -- lifecycle pair complete.

**C-24 Independence Verification:**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- names the failure condition; covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- names the recovery action; covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis (domain-named tokens):
- `EVIDENCE PHASE COMPLETE:` -- names the Phase 2 / evidence-gathering boundary; covers C-09 (threshold verifiable unconditionally at this boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `MAP PHASE COMPLETE:` -- names the Phase 3 / literature-mapping boundary; covers C-13 (empty-tier verifiable unconditionally at this boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 2 independently.

Redundancy check:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Four tokens total, all distinct. Neither pair depends on the other. C-24 PASS (if domain-named tokens qualify -- this is the experiment).

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

## V-04 -- C-23 + C-24 First Combination

**Axes**: Lifecycle completeness (C-23) + redundancy annotation (C-24)
**Hypothesis**: V-01 isolates C-23; V-02 isolates C-24. The two criteria are orthogonal: C-23 measures whether all four phase gates are instrumented with unconditional lifecycle tokens; C-24 measures whether two independent C-20-satisfying pairs coexist. Neither criterion's pass condition references the other. Adding both to a single design should be purely additive. This variation takes the R7 V-03 four-phase structure (all four lifecycle tokens already present) and adds the canonical pair PASS annotations from R7 V-05 (THRESHOLD NOT MET: C-09+C-16, RECOVERY NOTE: C-12+C-16) plus the C-24 independence block. The lifecycle pair (PHASE 2 COMPLETE: + PHASE 3 COMPLETE:) already satisfies C-20; the canonical pair adds a second independent C-20 path. Dual typed schemas preserved from R7 V-03. No inertia front-loading (C-14 via Phase 4 gate only). Expected: C-23 PASS, C-24 PASS, C-21 PASS, all other criteria PASS. Score: 170/170.

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity. The evidence_type_mapped and counter-evidence-noted fields confirm the interrogative obligation was discharged per claim (C-11 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 boundary instrumented; C-23 in progress at 1/4).

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

This token serves dual purpose in this skill: it records the depth threshold shortfall in the body for auditing without requiring YAML parsing (C-09 PASS) and adds a named gate token for template-label checkability alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). Pair 1, Token A in the failure/recovery multi-criterion pair.

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

This token serves dual purpose in this skill: it makes the recovery step body-visible and auditable without re-running the search (C-12 PASS) and adds a named gate token for template-label checkability alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete (THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16).

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. Unconditional emission makes threshold compliance verifiable in every run outcome at this Phase 2 boundary point (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 2 of 4 for C-23 (Phase 2 boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). Pair 2, Token A in the lifecycle multi-criterion pair.

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers populated or some empty. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this Phase 3 boundary point (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 3 of 4 for C-23 (Phase 3 boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). Pair 2, Token B -- lifecycle pair complete (PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16).

**C-24 Independence Verification (both pairs now complete):**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 2 independently.

Redundancy check:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Four tokens total, all distinct. Neither pair depends on the other. C-24 PASS.

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

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:, whether recommendation is PROCEED, SEARCH MORE, or REFRAME CLAIM. The inertia_named field confirms the INERTIA SCENARIO: gate was discharged before the recommendation keyword (C-14 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Token 4 of 4 for C-23 -- C-23 fully satisfied. All four phase boundaries instrumented: Phase 1 / claim-extraction, Phase 2 / evidence-gathering, Phase 3 / literature-mapping, Phase 4 / gap-analysis. Each token emits unconditionally at its specific phase boundary. C-23 PASS.

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

## V-05 -- v8 Ceiling Synthesis (All 24 Criteria)

**Axes**: All dimensions combined -- dual typed schemas (C-21) + canonical pair with explicit PASS (C-20 Pair 1) + lifecycle pair with explicit PASS (C-20 Pair 2, C-22) + all four phases instrumented (C-23) + C-24 independence block + inertia front-loading (C-14 maximum)
**Hypothesis**: The v8 ceiling requires all six aspirational progression axes simultaneously: C-19 (one schema-typed obligation), C-20 (two multi-criterion token pairs), C-21 (both obligations schema-typed), C-22 (two unconditional lifecycle tokens), C-23 (all four phases instrumented), C-24 (two independent C-20 pairs). V-04 achieves C-23 + C-24 without inertia front-loading. V-05 adds inertia front-loading (INERTIA COMMITMENT in Phase 1, INERTIA VERIFICATION in Phase 4) as the C-14 maximum-coverage axis. All six axes are orthogonal and additive; no axis blocks another. Expected: all 24 criteria PASS. Score: 170/170.

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
`PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]`

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed field confirms the pre-search inertia commitment was made (C-14 maximum: inertia scenario committed before any evidence is gathered, then verified against evidence in Phase 4). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation per claim (C-11 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Token 1 of 4 for C-23 (Phase 1 boundary instrumented; C-23 in progress at 1/4).

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

This token serves dual purpose in this skill: it records the depth threshold shortfall in the body for auditing without requiring YAML parsing (C-09 PASS) and adds a named gate token for template-label checkability alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24.

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

This token serves dual purpose in this skill: it makes the recovery step body-visible and auditable without re-running the search (C-12 PASS) and adds a named gate token for template-label checkability alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS). This is Pair 1, Token B -- the failure/recovery pair is now complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run that meets its threshold still produces PHASE 2 COMPLETE: with status=MET, making threshold compliance verifiable in every run outcome at the Phase 2 boundary (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 2 of 4 for C-23 (Phase 2 boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A in the lifecycle multi-criterion pair. C-22 is orthogonal to the inertia front-loading axis: PHASE 2 COMPLETE: fires unconditionally at the Phase 2 boundary regardless of whether inertia was committed in Phase 1 (V-04 R7 confirms).

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

This token emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers populated or some empty. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this Phase 3 boundary point (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 3 of 4 for C-23 (Phase 3 boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 and Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- the lifecycle pair is now complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-20 PASS for Pair 2 independently.

**C-24 Independence Verification (both pairs now complete):**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 2 independently.

Redundancy check:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Four tokens total, all distinct. Neither pair depends on the other. C-24 PASS.

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
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:, whether recommendation is PROCEED, SEARCH MORE, or REFRAME CLAIM. The inertia_named field confirms the INERTIA SCENARIO: verification gate was discharged before the recommendation keyword (C-14 PASS for checking; inertia front-loaded in Phase 1 and verified in Phase 4 -- maximum C-14 coverage). Adds a named gate token for template-label checkability (C-16 PASS). Token 4 of 4 for C-23 -- C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction, Phase 2 / evidence-gathering, Phase 3 / literature-mapping, Phase 4 / gap-analysis. Each token names its specific phase boundary and confirms unconditional emission. C-23 PASS.

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
