# discover-literature Variations R20

**Criterion probed: Variation-axis study** -- phrasing register, lifecycle emphasis, inertia framing
**Rubric**: v19 (ceiling 235)

| V | Axis | Predicted |
|---|------|-----------|
| V-01 | Phrasing Register: conversational throughout, all tokens preserved | 235/235 |
| V-02 | Lifecycle Emphasis: C-29 consolidation block omitted | 195/235 |
| V-03 | Inertia Framing: Phase-0 commitment, PHASE 1 COMPLETE lacks inertia_committed field | 180/235 |
| V-04 | Combined (Phrasing Register + Lifecycle Emphasis): conversational + single-obligation preamble | 230/235 |
| V-05 | Full synthesis: conversational + expanded inertia framing + all tokens preserved | 235/235 |

---

## Axes Probed

**Phrasing Register** varies prose tone from formal/imperative ("You must reach the source threshold...") to conversational/descriptive ("Work toward the source threshold..."). All structural tokens, schemas, and annotation elements remain unchanged. Hypothesis: register is orthogonal to compliance -- a conversational prompt can satisfy C-01 through C-37 identically to a formal one.

**Lifecycle Emphasis** varies how much structural prose is given to phase-boundary consolidation blocks. The extreme test: remove the C-29 Operationalization Verification block entirely. The in-token C-28/C-29 annotations at Phase 1 and Phase 4 are preserved -- C-29 itself may PASS -- but without the named consolidation block, C-30 FAIL cascades through C-37. This tests whether the rubric's consolidation-block requirement adds value beyond the distributed annotations.

**Inertia Framing** tests what happens when the inertia commitment is moved to a dedicated PRE-PHASE INERTIA FRAME before Phase 1 rather than housed inside Phase 1. If the PHASE 1 COMPLETE token no longer carries `inertia_committed=[yes]`, C-27(a) fails. C-14 may still pass (inertia named somewhere), but the lifecycle-integration axis (C-27 through C-37) breaks from the Phase 1 boundary forward.

**Why these three axes:**
- Register (V-01) tests style-orthogonality: can the rubric be satisfied in a friendlier voice?
- Lifecycle emphasis (V-02) tests consolidation-block value: what does the C-30 block buy beyond C-29 annotations?
- Inertia framing (V-03) tests architectural sensitivity: what happens when a required field migrates out of its designated token?
- Combined (V-04): conversational register with a preamble covering only one obligation -- tests whether C-15's both-obligations requirement is independently binding from the register variation.
- Synthesis (V-05): best combination -- conversational, inertia expanded but still housed in Phase 1, full C-29 block, all tokens.

**Failure cascade analysis:**

| Failure at | Cascades to | Criteria lost | Points lost |
|---|---|---|---|
| C-30 (no block / bad block) | C-31, C-32, C-33, C-34, C-35, C-36, C-37 | 8 criteria | 40 pts |
| C-27 (inertia_committed missing) | C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-36, C-37 | 11 criteria | 55 pts |
| C-15 (single-obligation preamble) | none (C-15 is independent) | 1 criterion | 5 pts |

---

## V-01 -- Phrasing Register: Conversational, all tokens preserved

**Axis**: All formal/imperative prose rewritten in conversational/descriptive register. All lifecycle tokens, token schemas, C-29 block, and C-33 Compliance Declaration are structurally identical to the R19 V-05 canonical pass. The only change is the voice of the surrounding prose.
**Hypothesis**: C-36 PASS, C-37 PASS = 235/235

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

Reach the source threshold for the active mode before moving to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell needs real data or an explicit recovery note. If something is unknown at first pass, search again. If the follow-up also fails, record it using the schema below.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and needed a follow-up search
Unacceptable: a secondary search performed without a RECOVERY NOTE:; missing any of the three fields; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" with no recovery note

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map needs output. If a tier comes up empty, say so explicitly using the schema below.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence on why no sources made it in
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: a tier has zero qualifying entries
Unacceptable: a tier heading with no entries and no TIER EMPTY: token; a TIER EMPTY: missing any field

Both obligations kick in before Phase 1 and stay active through Phase 5. "If unknown" questions require a follow-up action and a result. "If none found" questions require a TIER EMPTY: token -- silence is not an answer.

---

## PHASE 1 -- What claims need support?

Take a look at any prior signals for this topic (discover-hypothesis, specify-spec, paper draft) before answering.

1. What are the 3-5 key claims this work makes about {{topic}} that need literature backing?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: put yourself in a skeptic's seat -- what would they cite to push back?

### INERTIA COMMITMENT (required before Phase 2 starts)

Before searching a single paper, lock in what inertia looks like for this topic. Phase 4 will measure your evidence against this commitment.

Answer: what does a team do if they ignore this literature entirely?
Name the default path -- the behavior that costs them nothing to stay on.

INERTIA SCENARIO: [the default team behavior if this review is never done -- written before any search]

Hold this. Phase 4 will ask whether the literature gathered makes that default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27(a) satisfied -- inertia commitment is observable at the lifecycle token layer without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 needed. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

---

## PHASE 2 -- What does the literature actually say?

Work toward the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim, run these searches:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers push back on this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish methodological precedent? (WebSearch: "[claim topic] method")

If the threshold is still not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Keep going until the threshold is met or all angles are exhausted. If it cannot be met, note:
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer the per-source questions before entering it in the table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that needed a follow-up search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes the recovery step visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

Every cell needs real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally whether the threshold was met or not -- only the status field differs. Adds a named gate token (C-16 PASS). Token 2 of 4 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two unconditional lifecycle tokens required for C-22 (C-22 in progress). Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources push back?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 (C-23 in progress at 3/4). Second unconditional lifecycle token -- C-22 fully satisfied (Phase 2 + Phase 3 boundaries both instrumented unconditionally; C-22 PASS). Pair 2, Token B. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: covers C-09 + C-16. C-09 PASS, C-16 PASS.
- RECOVERY NOTE: covers C-12 + C-16. C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct criteria. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: covers C-09 + C-16. C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: covers C-13 + C-16. C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct criteria. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone covers C-09, C-13, C-16 -- C-20 PASS.
- Removing Pair 2: Pair 1 alone covers C-09, C-12, C-16 -- C-20 PASS.

C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many have weak or no support? Which ones?
3. Which contrary papers are the biggest threat? Most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Go back to the INERTIA SCENARIO you locked in at Phase 1. Now measure what you found against it.

Q: Does the literature make the inertia default worse than acting?
Name the specific risk the inertia path creates given what you now know. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: front-loaded in Phase 1, verified in Phase 4). C-27 PASS: PHASE 1 COMPLETE: carries inertia_committed=[yes] (C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (C-27(b) satisfied). Additive design confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 needed. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

## C-29 Operationalization Verification

This block consolidates C-29 proof. Distributed Phase 1 and Phase 4 annotations satisfy C-29, but leave compliance inference-dependent. This block is a single grep target: all six confirmations here; C-29 PASS declared here.

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step.
CELL-SOURCE: All six cells draw from already-emitted content -- Phase 1 and Phase 4 token annotations both written before this block; no forward-references. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-34 is to C-33 what C-25 is to C-23: just as C-25 adds per-token N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making four-token completeness verifiable from any single token without reading all four), C-34 adds per-element designator confirmations to the four C-33 elements required within this closing declaration (making four-element compliance self-auditing from this labeled sub-section alone without reading the declaration's aggregate structure). The structural analogy motivates the C-34 design pattern: the recursive self-announcing principle is applied one level deeper, from the token layer (C-25) to the element-within-block layer (C-34).

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what is the response strategy?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 -- Lifecycle Emphasis: C-29 consolidation block omitted

**Axis**: All lifecycle tokens and their C-28/C-29 per-boundary annotations are preserved exactly. The `## C-29 Operationalization Verification` block is omitted entirely. C-29 is satisfied by the in-token annotations; C-30 fails because its named consolidation block is absent.
**Hypothesis**: C-30 FAIL cascades to C-31, C-32, C-33, C-34, C-35, C-36, C-37 = 8 × 5 = 40 pts lost = 195/235

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
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, record it using the schema below. This schema is authoritative.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and required a follow-up search
Unacceptable: performing a secondary search without writing RECOVERY NOTE:; RECOVERY NOTE: missing any of the three fields; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" without a RECOVERY NOTE:

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token using the schema below. This schema is authoritative.

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27(a) satisfied). C-16 PASS. Token 1 of 4 (C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal; no cross-reference to Phase 4 is required. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

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

C-09 PASS, C-16 PASS. Pair 1, Token A.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

Emits unconditionally. C-16 PASS. Token 2 of 4 (C-23 in progress at 2/4). C-22 in progress. Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4 (C-23 in progress at 3/4). C-22 PASS. Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification
Pair 1: THRESHOLD NOT MET: + RECOVERY NOTE: cover C-09, C-12, C-16. C-20 PASS independently.
Pair 2: PHASE 2 COMPLETE: + PHASE 3 COMPLETE: cover C-09, C-13, C-16. C-20 PASS independently.
Remove-either-pair test: Removing Pair 1: C-20 PASS. Removing Pair 2: C-20 PASS.
C-24 PASS.

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

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

Emits unconditionally. inertia_verified=[yes] confirms C-14 PASS. C-27 PASS. C-16 PASS. Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal; no cross-reference to Phase 1 required. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

[NOTE: The C-29 Operationalization Verification block is intentionally omitted. C-29 is satisfied by the per-boundary annotations above. C-30 requires a named consolidation block -- its absence is the axis under test in this variation.]

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 -- Inertia Framing: Phase-0 architecture, C-27(a) broken

**Axis**: A PRE-PHASE INERTIA FRAME section is added before Phase 1. The INERTIA COMMITMENT block is removed from Phase 1. The PHASE 1 COMPLETE token does not include an `inertia_committed` field -- the commitment was performed in the pre-phase section. C-27(a) requires the PHASE 1 COMPLETE token to carry `inertia_committed=[yes]`; its absence at this boundary fails C-27, cascading through C-37.
**Hypothesis**: C-27 FAIL cascades to C-28 through C-37 = 11 × 5 = 55 pts lost = 180/235

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
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, record it using the schema below. This schema is authoritative.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and required a follow-up search
Unacceptable: performing a secondary search without writing RECOVERY NOTE:; missing any field; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" without a RECOVERY NOTE:

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, output a TIER EMPTY: token. This schema is authoritative.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence explaining why the tier has no entries
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: any tier produces zero qualifying source entries
Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields

Both obligations apply before Phase 1 begins and remain in force through Phase 5.

---

## PRE-PHASE INERTIA FRAME (required before any phase begins)

This run tracks whether the literature gathered is strong enough to displace inertia -- the default path a team takes when they ignore this review entirely.

Before Phase 1 begins, commit to what inertia looks like for this topic:

Answer: what would a team do if this literature review never happened?
Name the default path -- the behavior that costs nothing to stay on.

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search or claim extraction]

This commitment is the baseline. Phase 4 will measure the evidence gathered against it. Every recommendation (PROCEED / SEARCH MORE / REFRAME CLAIM) must be judged against whether the literature makes this default worse than acting.

---

## PHASE 1 -- What are the claims that need support?

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.
The inertia commitment was recorded in the PRE-PHASE INERTIA FRAME above -- Phase 1 proceeds directly to claim extraction.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary. C-16 PASS. Token 1 of 4 (C-23 in progress at 1/4). Note: inertia commitment was performed in the pre-phase frame; this token does not carry an inertia_committed field -- the commitment precedes Phase 1 rather than being housed within it.

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

If threshold cannot be met, note:
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]
C-09 PASS, C-16 PASS. Pair 1, Token A.

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]
Emits unconditionally. C-16 PASS. Token 2 of 4 (C-23 in progress at 2/4). C-22 in progress. Pair 2, Token A.

---

## PHASE 3 -- How does the literature organize?

(OBLIGATION B governs all four tiers.)

### FOUNDATIONAL tier
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [justification]
If none: TIER EMPTY: FOUNDATIONAL -- {why} -- {search}

### RECENT tier (2020+)
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note]
If none: TIER EMPTY: RECENT -- {why} -- {search}

### CONTRARY tier
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [objection]
If none: TIER EMPTY: CONTRARY -- {why} -- {search}

### METHODOLOGICAL tier
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation]
If none: TIER EMPTY: METHODOLOGICAL -- {why} -- {search}

PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]
Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4 (C-23 in progress at 3/4). C-22 PASS. Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification
Pair 1: THRESHOLD NOT MET: + RECOVERY NOTE: cover C-09, C-12, C-16. C-20 PASS independently.
Pair 2: PHASE 2 COMPLETE: + PHASE 3 COMPLETE: cover C-09, C-13, C-16. C-20 PASS independently.
Remove-either-pair test: Removing Pair 1: C-20 PASS. Removing Pair 2: C-20 PASS.
C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong support (>= 2 sources)?
2. How many have weak or no support?
3. Which contrary papers are most dangerous?
4. Any HIGH RISK claims? scope / qualify / drop?
5. Overall evidence strength?

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list]
HIGH RISK claims: [list or "none"]

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in the PRE-PHASE INERTIA FRAME. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting?

INERTIA SCENARIO: [repeat the pre-phase commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

Emits unconditionally. inertia_verified=[yes] confirms Phase 4 returned to the pre-phase commitment and verified evidence against it (C-14 PASS: inertia named before search, verified here). C-16 PASS. Token 4 of 4. C-23 PASS.

[NOTE: C-27 requires PHASE 1 COMPLETE to carry inertia_committed=[yes]. In this design, the inertia commitment was performed in a pre-phase section; PHASE 1 COMPLETE does not carry this field. C-27(a) is therefore unmet. The C-29 Operationalization Verification block is present but cells (i)-(iii) cannot draw from a PHASE 1 COMPLETE inertia_committed field that was never established -- C-28(a) fails, C-29 fails by dependency, and the consolidation block cannot pass C-30. This is the axis under test.]

## C-29 Operationalization Verification

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction.
CELL-SOURCE: Cells (iv)-(vi) draw from PHASE 4 COMPLETE: annotation (already emitted). Cells (i)-(iii) draw from the PHASE 1 COMPLETE: annotation -- which in this design does not carry an inertia_committed field or C-27(a) attestation. C-31(b) cell-source provenance: cells (iv)-(vi) confirmed; cells (i)-(iii) reference absent content.

Phase 1 / C-27(a) boundary:
- Cell (i): C-27(a) -- not established at PHASE 1 COMPLETE: boundary; inertia_committed field absent from token. NOT CONFIRMED.
- Cell (ii): inertia_committed=[yes] field -- not present in PHASE 1 COMPLETE: token. NOT CONFIRMED.
- Cell (iii): grep instruction -- "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." Grep target does not carry the required field. NOT CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv): C-27(b) named. CONFIRMED.
- Cell (v): inertia_verified=[yes] field identified. CONFIRMED.
- Cell (vi): "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." CONFIRMED.

Cells (i)-(iii) not confirmed. C-29 FAIL at Phase 1 boundary. Block present but cannot declare C-29 PASS.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support?
2. Which contrary paper must be addressed?
3. What methodological precedent is missing?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 -- Combined: Phrasing Register + Single-Obligation Preamble

**Axis**: Conversational register throughout (Axis 1: Phrasing Register). The ENFORCEMENT CONTRACT preamble covers only OBLIGATION A -- anti-placeholder recovery -- and omits OBLIGATION B (empty-tier acknowledgment). C-15 requires both obligations named as non-optional in the preamble; a preamble covering only one is a PARTIAL, not a PASS.
**Hypothesis**: C-15 FAIL = 5 pts lost = 230/235

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

Reach the source threshold for the active mode before moving to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

One obligation governs this entire run. It is non-optional and cannot be waived by phase, brevity, or topic difficulty.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell needs real data or an explicit recovery note. If something is unknown at first pass, search again. If the follow-up also fails, record it using the schema below. This schema is authoritative.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and needed a follow-up search
Unacceptable: a secondary search without a RECOVERY NOTE:; missing any field; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" with no recovery note

This obligation applies before Phase 1 begins and stays active through Phase 5. "If unknown" questions require a follow-up and a result.

[NOTE: OBLIGATION B -- Empty-Tier Acknowledgment is not included in this preamble. The TIER EMPTY: token schema appears in Phase 3 where it is used, but the dual-domain global enforcement contract is not established here. C-15 requires both obligations named as non-optional in the preamble; this preamble covers only one. C-15 PARTIAL -- the axis under test.]

---

## PHASE 1 -- What claims need support?

Check any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

1. What are the 3-5 key claims this work makes about {{topic}} that need literature backing?
2. For each claim: what would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to push back?

### INERTIA COMMITMENT (required before Phase 2 starts)

Before you search anything, lock in what inertia looks like for this topic. Phase 4 will measure the evidence against this commitment.

Answer: what does a team do if they ignore this literature entirely?
Name the default path -- the behavior that costs nothing to stay on.

INERTIA SCENARIO: [the default team behavior if this review is never done -- written before any search]

Hold this. Phase 4 will ask whether the literature gathered makes that default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27(a) satisfied). C-16 PASS. Token 1 of 4 (C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal; no cross-reference to Phase 4 needed. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

---

## PHASE 2 -- What does the literature say?

Work toward the source threshold for {{mode}} (quick >= 5, standard >= 15, deep >= 25).

For each claim, run these searches:

1. What seminal papers does the field cite? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers push back? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish methodological precedent? (WebSearch: "[claim topic] method")

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

If threshold cannot be met:
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]
C-09 PASS, C-16 PASS. Pair 1, Token A.

For each source, answer per-source questions before the table. Any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell needing follow-up:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]
Emits unconditionally. C-16 PASS. Token 2 of 4 (C-23 in progress at 2/4). C-22 in progress. Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier.

### FOUNDATIONAL tier
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020+)
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection]
If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]
Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4 (C-23 in progress at 3/4). C-22 PASS. Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification
Pair 1: THRESHOLD NOT MET: + RECOVERY NOTE: -- C-09, C-12, C-16. C-20 PASS independently.
Pair 2: PHASE 2 COMPLETE: + PHASE 3 COMPLETE: -- C-09, C-13, C-16. C-20 PASS independently.
Remove-either-pair test: either pair alone -- C-20 PASS.
C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong support (>= 2 sources)? Which ones?
2. How many have weak or no support? Which ones?
3. Which contrary papers are the biggest threat? Most-dangerous-first.
4. Any HIGH RISK claims? scope / qualify / drop?
5. Overall evidence strength?

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]

### Inertia verification (required gate before the recommendation keyword)

Go back to the INERTIA SCENARIO from Phase 1. Measure what you found against it.

INERTIA SCENARIO: [repeat Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence makes the inertia default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

Emits unconditionally. inertia_verified=[yes] confirms C-14 PASS. C-27 PASS. C-16 PASS. Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal; no cross-reference to Phase 1 needed. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

## C-29 Operationalization Verification

This block consolidates C-29 proof as a single grep target.

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction.
CELL-SOURCE: All six cells draw from already-emitted content. No forward-references. C-31(b) satisfied. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-34 is to C-33 what C-25 is to C-23: just as C-25 adds per-token N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making four-token completeness verifiable from any single token without reading all four), C-34 adds per-element designator confirmations to the four C-33 elements required within this closing declaration (making four-element compliance self-auditing from this labeled sub-section alone without reading the declaration's aggregate structure). The structural analogy motivates the C-34 design pattern: the recursive self-announcing principle is applied one level deeper, from the token layer (C-25) to the element-within-block layer (C-34).

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what is the response strategy?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 -- Full synthesis: Conversational + Expanded Inertia + All tokens preserved

**Axis**: Conversational register (Axis 1) + Inertia Framing as an expanded prominent section in Phase 1 (Axis 3) + Full lifecycle token annotations with C-29 block (Axis 2 positive pole). The inertia commitment remains housed in Phase 1 so PHASE 1 COMPLETE carries `inertia_committed=[yes]`. Inertia framing is given more prose real estate in both Phase 1 and Phase 4. All structural tokens, schemas, and the C-33 Compliance Declaration are preserved.
**Hypothesis**: C-36 PASS, C-37 PASS = 235/235

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

Reach the source threshold for the active mode before moving to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional -- they cannot be waived for any phase, for brevity, or because the topic is narrow.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell needs real data or an explicit recovery note. If something is unknown at first pass, search again. If the follow-up also fails, record it in the body using the schema below. This schema is authoritative -- these field names govern what Phase 2 must produce.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column needing secondary search (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and needed a follow-up search
Unacceptable: a secondary search performed without a RECOVERY NOTE:; a RECOVERY NOTE: missing any field; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" with no recovery note

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map needs output. If a tier comes up empty, say so explicitly using the schema below. This schema is authoritative -- these field names govern what Phase 3 must produce.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence on why no sources qualified
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: a tier has zero qualifying entries
Unacceptable: a tier heading with no entries and no TIER EMPTY: token; a TIER EMPTY: missing any field

Both obligations apply before Phase 1 begins and stay active through Phase 5. "If unknown" questions require a follow-up action and a reported result. "If none found" questions require a TIER EMPTY: token -- silence is not an acceptable answer.

---

## PHASE 1 -- What claims need support?

Check any prior signals for this topic (discover-hypothesis, specify-spec, paper draft) before answering.

1. What are the 3-5 key claims this work makes about {{topic}} that need literature backing?
2. For each claim: what would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: put yourself in a skeptic's seat -- what would they cite to push back?

### INERTIA COMMITMENT (required gate before Phase 2 starts)

The primary competitor for any literature-backed decision is inertia -- the default path teams take when they do nothing with the evidence. Before searching a single paper, get concrete about what inertia looks like for this specific topic.

Answer two questions:
- What does a team actually do if they never run this literature review?
- What does that cost them -- concretely?

Name the default path. Make it specific enough that Phase 4 can measure the evidence gathered against it.

INERTIA SCENARIO: [the specific default team behavior if this review never happens -- written before any search]

Hold this scenario. Phase 4 will return to it and ask: does the literature gathered make that default worse than acting? If yes, PROCEED. If not, SEARCH MORE or REFRAME CLAIM.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27(a) satisfied -- the inertia commitment is now observable at the lifecycle token layer, verifiable from this token alone without reading the INERTIA SCENARIO: block; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). Additive: inertia_committed=[yes] coexists with N-of-4 counter, C-11 fields, and C-16 gate token without displacing any required element. C-28 PASS at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal confirming C-27(a) compliance at this boundary; no cross-reference to Phase 4 is required to verify C-27(a) here. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

---

## PHASE 2 -- What does the literature actually say?

Work toward the source threshold for {{mode}} (quick >= 5, standard >= 15, deep >= 25).

For each claim, run these searches:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers push back on this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent? (WebSearch: "[claim topic] method")

If the threshold is not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

Keep going until the threshold is met or all angles are exhausted. If it cannot be met, record:
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer the per-source questions before entering it in the table. Any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell that needed a follow-up search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes the recovery step visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

Every cell needs real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally whether the threshold was met or not. Adds a named gate token (C-16 PASS). Token 2 of 4 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two unconditional lifecycle tokens required for C-22 (C-22 in progress). Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four.)

### FOUNDATIONAL tier

Q: Which sources are foundational?
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
Q: If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)

Q: Which sources are recent (2020+)?
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
Q: If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier

Q: Which sources push back?
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
Q: If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier

Q: Which sources establish methodological precedent?
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
Q: If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]

This token emits unconditionally at the Phase 3 / literature-mapping boundary. The tiers_empty_acknowledged field confirms TIER EMPTY: coverage (C-13 PASS). Adds a named gate token (C-16 PASS). Token 3 of 4 (C-23 in progress at 3/4). Second unconditional lifecycle token -- C-22 fully satisfied (Phase 2 + Phase 3 both instrumented unconditionally; C-22 PASS). Pair 2, Token B. Pair 2 summary: PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16; together: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1 -- failure/recovery axis:
- THRESHOLD NOT MET: covers C-09 + C-16. C-09 PASS, C-16 PASS.
- RECOVERY NOTE: covers C-12 + C-16. C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct criteria. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: covers C-09 + C-16. C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: covers C-13 + C-16. C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16 -- three distinct criteria. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone -- C-20 PASS.
- Removing Pair 2: Pair 1 alone -- C-20 PASS.

C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong support (>= 2 sources)? Which ones?
2. How many have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? Most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (the gate that determines the recommendation)

Go back to the INERTIA SCENARIO you committed to in Phase 1. This is the moment of measurement: does the literature gathered actually make the inertia default worse than acting?

Be direct. Name the specific harm the inertia path creates given what you now know. Do not issue a PROCEED recommendation without showing that the evidence is strong enough to move a skeptical team. If the evidence is not strong enough, issue SEARCH MORE or REFRAME CLAIM and name exactly what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged, word for word]
INERTIA RISK: [the specific harm the inertia path creates given the literature gathered]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name the specific evidence that counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS: inertia front-loaded in Phase 1, verified in Phase 4 -- maximum C-14 coverage). C-27 PASS: PHASE 1 COMPLETE: carries inertia_committed=[yes] (C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (C-27(b) satisfied). Additive design confirmed. Adds a named gate token (C-16 PASS). Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary; no cross-reference to Phase 1 is required. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

## C-29 Operationalization Verification

This block consolidates C-29 proof as a single grep target. Distributed in-token C-28/C-29 annotations satisfy C-29 but leave compliance inference-dependent. This block eliminates that: all six confirmations appear here; C-29 PASS declared here; no cross-referencing required.

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above) -- the Phase 4 lifecycle token has been declared before this block emits; no forward-reference is possible. C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) citation procedurally executable in one step.
CELL-SOURCE: All six cells draw from already-emitted content -- Phase 1 and Phase 4 token annotations both written before this block; no forward-references; all sub-clause designations, signal field names, and grep instructions restated from earlier annotations. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in one step.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-34 is to C-33 what C-25 is to C-23: just as C-25 adds per-token N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making four-token completeness verifiable from any single token without reading all four), C-34 adds per-element designator confirmations to the four C-33 elements required within this closing declaration (making four-element compliance self-auditing from this labeled sub-section alone without reading the declaration's aggregate structure). The structural analogy motivates the C-34 design pattern: the recursive self-announcing principle is applied one level deeper, from the token layer (C-25) to the element-within-block layer (C-34).

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what is the response strategy?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
