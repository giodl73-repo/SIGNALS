Written to `simulations/quest/variations/discover-literature-variations-R9-2026-03-19.md`.

---

## discover-literature -- Variations R9

**5 variations targeting C-25 and C-26.**

### Variation Map

| ID | Axis | Base | Key change | Predicted v9 |
|----|------|------|------------|--------------|
| **V-01** | C-25 isolation | R8 V-04 | N-of-4 counter on all 4 tokens; C-24 via scattered pair annotations; no named independence block | 175/180 |
| **V-02** | C-26 isolation | R8 V-02 | Named independence block with all C-26 elements; only Phase 2+3 tokens (C-23 FAIL -> C-25 FAIL) | 175/180 |
| **V-03** | C-26 heading agnosticism | R8 V-04 | Block heading = "Dual-Path Redundancy Proof" instead of "C-24 Independence Verification" | 180/180? |
| **V-04** | C-25 + C-26 combination | R8 V-04 | N-of-4 counter + named block with all C-26 elements; no inertia front-loading | **180/180** |
| **V-05** | v9 ceiling synthesis | All axes | V-04 + inertia front-loading | **180/180** |

### Design logic

**Why V-01 misses C-26**: C-24 passes via scattered pair annotations, C-25 passes via N-of-4 counter. But without a named block that states "C-20 PASS for Pair N independently" and runs the remove-either-pair test verbatim, C-26 fails -- scattered compliance is not a single grep target.

**Why V-02 misses C-25**: C-25 depends on C-23. Only 2 lifecycle tokens means C-23 FAIL, which blocks C-25. V-02 isolates C-26 at the cost of C-23 + C-25.

**V-03 experiment**: C-26 pass condition says "e.g., 'C-24 Independence Verification'" -- predicts heading-agnosticism like C-22 and C-21. If C-26 PASSes with a neutral heading, confirmed. If FAILs, an implicit naming constraint exists.

**V-04**: C-25 and C-26 are orthogonal -- per-token scannability vs whole-infrastructure declaration. Minimal 180/180 design.

**V-05**: V-04 + inertia front-loading = full 26-criterion ceiling.
out C-23, C-25 cannot pass -- there is no four-token sequence to place an N-of-4 counter on. V-02 isolates C-26 at the cost of C-23 + C-25.

**The critical experiment (V-03)**: C-26 pass condition says "a named block (heading or labeled section, e.g., 'C-24 Independence Verification')". The "e.g." signals this is an example, not a requirement -- analogous to C-22 token-agnosticism (confirmed V-02 R7) and C-21 label-independence (confirmed V-02 R6). V-03 replaces the heading with "Dual-Path Redundancy Proof" and preserves all four structural elements. If C-26 PASSes: heading-agnosticism confirmed. If C-26 FAILs: an implicit criterion-ID naming constraint exists not signaled by the "e.g." language.

**Why V-04 reaches 180**: C-25 and C-26 are orthogonal. C-25 measures per-token scannability; C-26 measures whole-infrastructure declaration. Neither criterion's pass condition references the other. Adding both to a C-23 + C-24 compliant design is purely additive.

**V-05** adds inertia front-loading over V-04 -- the same final polish axis as R8 V-05.

**R8 V-04 already exhibits both patterns**: V-04 R8 introduced N-of-4 counter language and a C-24 Independence Verification block with remove-either-pair test and "C-20 PASS for Pair N independently" declarations. v9 formalizes those as C-25 and C-26. R9 isolates them to confirm independence, documents heading-agnosticism, and creates canonical 180/180 designs.

### Predicted scores under v9

| | v9 score | C-25 | C-26 | C-23 | C-24 | C-22 | C-21 | C-20 |
|--|----------|------|------|------|------|------|------|------|
| V-01 | 175 | PASS | FAIL | PASS | PASS | PASS | PASS | PASS |
| V-02 | 175 | FAIL | PASS | FAIL | PASS | PASS | PASS | PASS |
| V-03 | 180? | PASS | PASS? | PASS | PASS | PASS | PASS | PASS |
| V-04 | 180 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-05 | 180 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

V-03 carries the experimental uncertainty. V-04 is the first 180 attempt. V-05 adds inertia front-loading as the final polish dimension.

---

## V-01 -- C-25 Isolation (N-of-4 Counter, No C-26 Block)

**Axis**: Single-axis N-of-4 progressive counter annotation
**Hypothesis**: All four lifecycle tokens carry N-of-4 counter annotations with progress fractions ("Token N of 4 required for C-23; C-23 in progress at N/4") and final declaration ("C-23 fully satisfied" on token 4) -- satisfying C-25 strictly. C-26 intentionally omitted: pair PASS annotations appear inline in each phase (C-24 PASS via scattered compliance) but there is no dedicated named block with "C-20 PASS for Pair N independently" and the remove-either-pair test. Expected: C-25 PASS, C-26 FAIL, C-24 PASS, C-23 PASS. Score: 175/180.

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity. The evidence_type_mapped and counter-evidence-noted fields confirm the interrogative obligation was discharged per claim (C-11 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4).

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

This token serves dual purpose: records the depth threshold shortfall in the body for auditing without requiring YAML parsing (C-09 PASS) and adds a named gate token for template-label checkability alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). Pair 1, Token A. C-09 PASS, C-16 PASS.

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

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token for template-label checkability alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK: (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete. Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS.

Every cell must contain real data or "not found after secondary search -- [query used]". No other placeholder is acceptable. (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not. Unconditional emission makes threshold compliance verifiable in every run outcome (C-09 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers -- use TIER ENTRY: or TIER EMPTY: per the contract schema for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational -- works the field cannot discuss without citing?**
For each entry: `TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`
**Q: If none found:** `TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+)?**
For each entry: `TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`
**Q: If none found:** `TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary -- works a hostile reviewer would cite?**
For each entry: `TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`
**Q: If none found:** `TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent?**
For each entry: `TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`
**Q: If none found:** `TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary -- every run produces PHASE 3 COMPLETE:, whether all tiers populated or some empty. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage at this Phase 3 boundary point (C-13 PASS). Adds a named gate token for template-label checkability (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). Pair 2, Token B -- lifecycle pair complete. Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS.

Both pairs independently satisfy C-20. Pair 1 (THRESHOLD NOT MET: + RECOVERY NOTE:) covers C-09, C-12, C-16. Pair 2 (PHASE 2 COMPLETE: + PHASE 3 COMPLETE:) covers C-09, C-13, C-16. Removing either pair leaves the remaining pair satisfying C-20. C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK -- no support plus strong contrary evidence? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

**Q: What would a team do if they ignored this literature entirely?** Name the default path.
**Q: What in the evidence makes that default worse than acting?** Name the specific risk.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes/no] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_named field confirms the INERTIA SCENARIO: gate was discharged before the recommendation keyword (C-14 PASS for checking). Adds a named gate token for template-label checkability (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). C-23 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 -- C-26 Isolation (Named Block, No C-23)

**Axis**: Single-axis named independence verification block
**Hypothesis**: C-26 depends on C-24 but not on C-23. This variation uses only Phase 2 + Phase 3 lifecycle tokens (C-22 minimum; C-23 FAIL -> C-25 FAIL) to isolate C-26. The named "C-24 Independence Verification" block after PHASE 3 COMPLETE: carries all four required C-26 elements: (a) both pairs named by constituent tokens, (b) "C-20 PASS for Pair N independently", (c) remove-either-pair test verbatim, (d) C-24 PASS. Expected: C-26 PASS, C-25 FAIL, C-23 FAIL, C-24 PASS. Score: 175/180.

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

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in the table. For any unknown cell, perform a follow-up WebSearch. If still unknown: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete. Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not. Unconditional emission makes threshold compliance verifiable in every run outcome (C-09 PASS). Adds a named gate token (C-16 PASS). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

**Q: Which sources are foundational?**
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`
**Q: If none found:** `TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+)?**
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`
**Q: If none found:** `TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary?**
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`
**Q: If none found:** `TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent?**
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`
**Q: If none found:** `TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied. Pair 2, Token B -- lifecycle pair complete. Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

**C-24 Independence Verification**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 + C-16. C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 + C-16. C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.

Four tokens total, all distinct. Neither pair depends on the other for C-20 compliance. C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

**Q: What would a team do if they ignored this literature entirely?** Name the default path.
**Q: What in the evidence makes that default worse than acting?** Name the specific risk.

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

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 -- C-26 Heading Agnosticism (Critical Experiment)

**Axis**: Single-axis C-26 heading/label flexibility
**Hypothesis**: C-26 pass condition says "a named block (heading or labeled section, e.g., 'C-24 Independence Verification')". The "e.g." signals an example, not a requirement -- analogous to C-22 token-agnosticism (V-02 R7) and C-21 label-independence (V-02 R6). This variation replaces the heading with "Dual-Path Redundancy Proof". All four C-26 structural elements preserved verbatim: (a) both pairs named by constituent tokens, (b) "C-20 PASS for Pair N independently", (c) remove-either-pair test, (d) C-24 PASS. All other criteria unchanged (N-of-4 counter on all 4 tokens, dual typed schemas). If C-26 PASSes: heading-agnosticism confirmed. If FAILs: an implicit criterion-ID naming constraint exists. Expected: 180/180.

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

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]`

This token emits unconditionally at the Phase 1 / claim-extraction boundary. The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4).

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). Pair 1, Token A in the failure/recovery multi-criterion pair. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary. Unconditional emission makes threshold compliance verifiable in every run outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

**Q: Which sources are foundational?**
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`
**Q: If none found:** `TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+)?**
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`
**Q: If none found:** `TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary?**
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`
**Q: If none found:** `TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent?**
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`
**Q: If none found:** `TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied. Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

**Dual-Path Redundancy Proof**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.

Four tokens total, all distinct. Neither pair depends on the other for C-20 compliance. C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

**Q: What would a team do if they ignored this literature entirely?** Name the default path.
**Q: What in the evidence makes that default worse than acting?** Name the specific risk.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes/no] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 / gap-analysis boundary. The inertia_named field confirms the INERTIA SCENARIO: gate was discharged (C-14 PASS). Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). C-23 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 -- C-25 + C-26 First Combination (No Inertia Front-Loading)

**Axes**: N-of-4 progressive counter (C-25) + named independence verification block (C-26)
**Hypothesis**: C-25 and C-26 are orthogonal. C-25 measures per-token scannability; C-26 measures whole-infrastructure declaration. Adding both to a C-23 + C-24 compliant design is purely additive. This variation: (a) all 4 lifecycle tokens carry strict N-of-4 counter annotations with progress fractions and "C-23 fully satisfied" on token 4, (b) "C-24 Independence Verification" block carries all four C-26 elements. Dual typed schemas preserved (C-21). No inertia front-loading. Expected: C-25 PASS, C-26 PASS, all other criteria PASS. Score: 180/180.

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

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

At the end of Phase 1, write:
`PHASE 1 COMPLETE: claims=[n] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]`

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity. The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4).

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. Unconditional emission makes threshold compliance verifiable in every run outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

**Q: Which sources are foundational?**
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`
**Q: If none found:** `TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+)?**
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`
**Q: If none found:** `TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary?**
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`
**Q: If none found:** `TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent?**
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`
**Q: If none found:** `TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

**C-24 Independence Verification**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.

Four tokens total, all distinct. Neither pair depends on the other for C-20 compliance. C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

**Q: What would a team do if they ignored this literature entirely?** Name the default path.
**Q: What in the evidence makes that default worse than acting?** Name the specific risk.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must reference the inertia scenario]
```

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes/no] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_named field confirms the INERTIA SCENARIO: gate was discharged before the recommendation keyword (C-14 PASS). Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and emits unconditionally. C-23 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 -- v9 Ceiling Synthesis (All 26 Criteria)

**Axes**: All dimensions combined -- dual typed schemas (C-21) + canonical pair with PASS (C-20 Pair 1) + lifecycle pair with PASS (C-20 Pair 2, C-22) + all four phases instrumented with N-of-4 counter (C-23, C-25) + named independence verification block with all C-26 elements (C-24, C-26) + inertia front-loading (C-14 maximum)
**Hypothesis**: V-04 achieves C-25 + C-26 without inertia front-loading. V-05 adds INERTIA COMMITMENT in Phase 1 and INERTIA VERIFICATION in Phase 4 as the C-14 maximum-coverage axis. All eight aspirational progression axes are orthogonal and additive. Expected: all 26 criteria PASS. Score: 180/180.

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed field confirms the pre-search inertia commitment was made (C-14 maximum: committed before any evidence, verified in Phase 4). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4).

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note:
`THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
`RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}`

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
`PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]`

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

**Q: Which sources are foundational?**
`TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]`
**Q: If none found:** `TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+)?**
`TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]`
**Q: If none found:** `TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### CONTRARY tier

**Q: Which sources are contrary?**
`TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]`
**Q: If none found:** `TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent?**
`TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]`
**Q: If none found:** `TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}`

At the end of Phase 3, write:
`PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]`

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

**C-24 Independence Verification**

Pair 1 -- failure/recovery axis:
- `THRESHOLD NOT MET:` -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `RECOVERY NOTE:` -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- `PHASE 2 COMPLETE:` -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- `PHASE 3 COMPLETE:` -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- three distinct criteria, two annotated tokens. C-20 PASS.

Four tokens total, all distinct. Neither pair depends on the other for C-20 compliance. C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
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
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

```
INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]
```

At the end of Phase 4, write:
`PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_named=[yes] | high_risk_claims=[n]`

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_named field confirms the INERTIA SCENARIO: verification gate was discharged before the recommendation keyword (C-14 PASS; inertia front-loaded in Phase 1 and verified in Phase 4 -- maximum C-14 coverage). Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
