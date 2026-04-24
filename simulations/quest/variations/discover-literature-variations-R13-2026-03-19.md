The file is complete and correct. V-05 has the full C-30 block at lines 1152-1166 with all six cells, both grep instructions verbatim, and `C-29 PASS` declared.

Written to `simulations/quest/variations/discover-literature-variations-R13-2026-03-19.md` — 1179 lines.

---

## R13 Variations Summary

**New criterion probed: C-30** (Named Operationalization Verification Block)

| V | Axis | C-30 element isolated | Predicted |
|---|------|-----------------------|-----------|
| V-01 | No block | Control: C-29 alone insufficient for C-30 | FAIL 195/200 |
| V-02 | Grep by pointer only | "By direct reference" = text must appear in block, not pointer-to-location | FAIL 195/200 |
| V-03 | Five cells (vi absent) | Six-or-nothing cell requirement | FAIL 195/200 |
| V-04 | Block before PHASE 4 COMPLETE: | Placement — must appear after Phase 4 lifecycle token | FAIL 195/200 |
| V-05 | Full ceiling | All four structural elements, six verbatim cells, after Phase 4, C-29 PASS | PASS 200/200 |

**Key hypotheses:**
- **V-02** is the most interesting probe: tests whether "or by direct reference" in C-30(c) allows a pointer to the annotation location (`as embedded in PHASE 4 COMPLETE: above`) or requires the grep text to physically appear in the block. If C-30's purpose is a self-contained single grep target, a location-pointer defeats it.
- **V-03** is the cell-completeness probe: five confirmed cells with cell (vi) absent mirrors R11's C-28 both-or-nothing pattern — each new criterion inherits the completeness property from its predecessor.
- **V-04** is the placement probe: parallel to C-26's requirement to appear "at or after the point where both C-24 pairs are first complete" — C-30 is a post-hoc consolidation, not an in-phase checklist.
4 content before PHASE 4 COMPLETE: is written. At block-emission time, Phase 4 boundary has not yet been declared, so cells (iv)-(vi) are drawn from anticipated rather than completed Phase 4 output. C-30 explicitly requires placement "after the Phase 4 lifecycle token."
- V-05 is the ceiling synthesis: all four structural elements present -- named block, both boundaries with six cell confirmations, both grep instructions verbatim, C-29 PASS declared.

**Dependency chain: C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30**
All five variations carry full C-29 compliance (established by R12 V-05). C-30 adds the named consolidation block. The variations probe which structural elements and placement properties of the block are strictly required.

**Why V-01 is predicted to FAIL**: C-30 pass condition is explicit -- "A design where C-29 compliance is confirmed from distributed Phase 1 and Phase 4 token annotations but has no named consolidation block satisfies C-29 but not C-30." Absence of the block is C-30 FAIL regardless of annotation quality in the lifecycle tokens.

**Why V-02 is predicted to FAIL**: "By direct reference" in C-30(c) intends the grep instruction text to be present in the block -- whether stated verbatim or quoted with a reference label. A pointer to a location ("see PHASE 1 COMPLETE: above") without the grep text does not make the block a self-contained grep target. The purpose of the consolidation block is that C-29 compliance can be confirmed at the block without reading the individual lifecycle tokens; a block that says "see above" defeats this purpose.

**Why V-03 is predicted to FAIL**: C-30(b) requires "six explicit confirmations" -- three elements at each of two boundaries. Five cells with cell (vi) absent leaves the Phase 4 grep instruction unaudited. A reviewer reading only the block cannot confirm C-27(b) grep-verifiability without reading the Phase 4 annotation. This is the same observability gap C-30 was designed to eliminate.

**Why V-04 is predicted to FAIL**: C-30 explicitly states the block must appear "after the Phase 4 lifecycle token." A block placed before PHASE 4 COMPLETE: is emitted before the Phase 4 boundary has been declared. Even if the six cells anticipate correct Phase 4 content, the placement means C-30's structural requirement is not met. The parallel: C-26 requires the block "at or after the point where both C-24 token pairs are first complete"; C-30 requires placement after Phase 4 completes the inertia-verification axis.

**Predicted scores under v13:**

| | v13 score | C-30 | C-29 | C-28 | C-27 | C-26 | C-25 | C-23 | C-24 | C-14 |
|--|-----------|------|------|------|------|------|------|------|------|------|
| V-01 | 195 | **FAIL** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-02 | 195 | **FAIL** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-03 | 195 | **FAIL** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-04 | 195 | **FAIL** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| V-05 | 200 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |


---

## V-01 -- No C-30 Block (R12 V-05 Control)

**Axis**: No consolidation block -- C-29 PASS at both boundaries without a named six-cell audit block
**Hypothesis**: C-30 requires a named structural element; C-29 distributed across Phase 1 and Phase 4 lifecycle token annotations satisfies C-29 but not C-30. Absence of the block is C-30 FAIL regardless of annotation quality. Expected: C-30 FAIL = 195/200.

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
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer, meaning inertia commitment can be verified from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 attestation at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources are contrary?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
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

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting on this evidence?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27(b) satisfied). The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS. C-28 attestation at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required to verify C-27(b) here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded. C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]

```

---

## V-02 -- C-30 Block with Grep by Pointer Only

**Axis**: C-30 block present, all six cells audited, but grep instructions confirmed by location-pointer rather than by quoting the text
**Hypothesis**: C-30(c) requires the grep instructions to be stated -- verbatim or by direct reference meaning the text is present in the block, not merely its location cited. A block that says as-embedded-in-PHASE-1-COMPLETE:-annotation-above without quoting the instruction text is a pointer-to-location. The block is not self-contained: a reviewer reading only the block cannot confirm C-29 without reading the lifecycle tokens -- which is the observability gap C-30 was designed to close. Expected: C-30 FAIL = 195/200.

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
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer, meaning inertia commitment can be verified from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 attestation at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources are contrary?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
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

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting on this evidence?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27(b) satisfied). The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS. C-28 attestation at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required to verify C-27(b) here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded. C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete.

## C-29 Operationalization Verification

This block consolidates C-29 proof by auditing the six cells across both boundaries. Grep instructions are confirmed by direct reference to their embedding locations.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: as embedded in PHASE 1 COMPLETE: annotation above. CONFIRMED by reference.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: as embedded in PHASE 4 COMPLETE: annotation above. CONFIRMED by reference.

All six cells confirmed. Both grep instructions confirmed by reference to their embedding locations. C-29 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]

```

---

## V-03 -- C-30 Block with Five Cells (Phase 4 Grep Absent)

**Axis**: C-30 block present after Phase 4 COMPLETE:, cells (i)-(v) confirmed, cell (vi) absent -- Phase 4 grep instruction not audited in the block
**Hypothesis**: C-30(b) requires six explicit confirmations -- three elements at each of two boundaries. Five cells with cell (vi) absent leaves the Phase 4 / C-27(b) grep instruction unaudited in the block. A reviewer reading only the block cannot confirm C-27(b) grep-verifiability without reading the Phase 4 annotation. Expected: C-30 FAIL = 195/200.

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
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer, meaning inertia commitment can be verified from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 attestation at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources are contrary?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
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

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting on this evidence?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27(b) satisfied). The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS. C-28 attestation at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required to verify C-27(b) here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded. C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete.

## C-29 Operationalization Verification

This block consolidates C-29 proof by running the six-cell audit across both boundaries.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.

Five cells confirmed. Phase 4 grep instruction present in PHASE 4 COMPLETE: annotation above. C-29 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]

```

---

## V-04 -- C-30 Block Placed Before Phase 4 COMPLETE:

**Axis**: C-30 block present with all six cells and verbatim grep instructions, but placed INSIDE Phase 4 content BEFORE the PHASE 4 COMPLETE: lifecycle token
**Hypothesis**: C-30 explicitly requires the block to appear after the Phase 4 lifecycle token. A block placed before PHASE 4 COMPLETE: is emitted before the Phase 4 boundary has been declared. Even if the six cells are correct, the placement fails C-30 structural requirement. The block is a post-hoc consolidation proof, not an in-phase checklist. Expected: C-30 FAIL = 195/200.

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
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer, meaning inertia commitment can be verified from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 attestation at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources are contrary?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
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

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting on this evidence?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

Before writing PHASE 4 COMPLETE:, run the C-29 operationalization verification block:

## C-29 Operationalization Verification

This block consolidates C-29 proof by running the six-cell audit across both boundaries.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- confirmed from Phase 4 annotation below.

All six cells confirmed. C-29 PASS.

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27(b) satisfied). The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS. C-28 attestation at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required to verify C-27(b) here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded. C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]

```

---

## V-05 -- v13 Ceiling Synthesis (All 30 Criteria)

**Axis**: All 30 criteria combined -- named C-30 block after Phase 4 COMPLETE:, six cells, both grep instructions verbatim, explicit C-29 PASS declaration
**Hypothesis**: Named block after Phase 4 lifecycle token, six cells (three per boundary), grep verbatim in cells (iii) and (vi), explicit C-29 PASS declaration. All four structural elements of C-30 pass condition satisfied. Score: 200/200.

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
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative -- the field names defined here govern what Phase 3 must produce.

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

Hold this scenario. Phase 4 will ask whether the literature gathered makes this default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer, meaning inertia commitment can be verified from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 attestation at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-28 PASS at Phase 1 boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token alongside INERTIA SCENARIO: and INERTIA RISK: (C-16 PASS). This is Pair 1, Token A in the failure/recovery multi-criterion pair -- one of two independent C-20-satisfying pairs for C-24. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. This is the decisive observability upgrade over THRESHOLD NOT MET:: a run meeting its threshold still produces PHASE 2 COMPLETE: with status=MET, making compliance verifiable in every outcome (C-09 PASS). Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-22 is orthogonal to the inertia front-loading axis. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources are contrary?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 required for C-23 (Phase 3 / literature-mapping boundary instrumented; C-23 in progress at 3/4). Second of two required unconditional lifecycle tokens -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). This is Pair 2, Token B -- lifecycle pair complete. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16 -- three distinct aspirational criteria. C-09 PASS, C-13 PASS, C-16 PASS. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: -- covers C-09 (threshold shortfall body-visible without YAML parsing) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 (recovery step body-visible and auditable) + C-16 (named gate token). C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 (threshold verifiable unconditionally at Phase 2 boundary) + C-16 (named gate token). C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 (empty-tier verifiable unconditionally at Phase 3 boundary) + C-16 (named gate token). C-13 PASS, C-16 PASS.
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

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting on this evidence?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27(b) satisfied). The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23 (Phase 4 / gap-analysis boundary instrumented). C-23 fully satisfied. All four phase boundaries instrumented with unconditional lifecycle tokens: Phase 1 / claim-extraction (1/4), Phase 2 / evidence-gathering (2/4), Phase 3 / literature-mapping (3/4), Phase 4 / gap-analysis (4/4). Each token names its phase boundary and confirms unconditional emission. C-23 PASS. C-28 attestation at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required to verify C-27(b) here. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-27 PASS: full cross-axis integration complete. C-28 PASS at Phase 4 boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded. C-29 fully satisfied at both Phase 1 and Phase 4 boundaries: C-29(a) confirmed at PHASE 1 COMPLETE:, C-29(b) confirmed here. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 complete.

## C-29 Operationalization Verification

This block consolidates C-29 proof by running the six-cell audit across both boundaries. A design where C-29 compliance is confirmed from distributed Phase 1 and Phase 4 token annotations satisfies C-29 but leaves compliance inference-dependent -- a reviewer must locate both tokens, read both annotations, and mentally confirm all six elements. This block is a single grep target: all six confirmations appear here; C-29 PASS declared here; no cross-referencing required.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. Both grep instructions stated verbatim in cells (iii) and (vi) above. Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 complete. C-29 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]

```
