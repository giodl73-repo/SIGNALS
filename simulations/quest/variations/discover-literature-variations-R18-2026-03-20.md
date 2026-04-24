# discover-literature Variations R18

**Criterion probed: C-36** (Structural Analogy Named in C-34 Sub-Section)
**Rubric**: v18 (ceiling 230)

| V | Axis | Predicted |
|---|------|-----------|
| V-01 | Analogy statement outside C-34 sub-section boundary (surrounding prose) | C-36 FAIL = 225/230 |
| V-02 | Analogy inside sub-section -- current pair only (C-34/C-33 named, C-25/C-23 absent) | C-36 FAIL = 225/230 |
| V-03 | Analogy inside sub-section -- reference pair only (C-25/C-23 named, C-34/C-33 absent) | C-36 FAIL = 225/230 |
| V-04 | Combination: analogy outside sub-section AND only one pair named | C-36 FAIL = 225/230 |
| V-05 | Full synthesis -- both pairs named inside sub-section: "C-34 is to C-33 what C-25 is to C-23" | C-36 PASS = 230/230 |

---

## Axes Probed

**C-36** requires an explicit structural analogy statement inside the C-34 labeled sub-section with three binding properties:
- (a) names C-34 and C-33 as the current analogy pair
- (b) names C-25 and C-23 as the reference pair
- (c) appears within the C-34 labeled sub-section boundary

**Why each variation fails/passes:**

- **V-01** fails (c): the analogy names both pairs correctly but appears in surrounding prose immediately after the `#### C-33 Compliance Declaration` sub-section closes. The sub-section boundary is the binding constraint; analogy in trailing prose cannot be confirmed as sub-section content by grepping the sub-section heading.

- **V-02** fails (b): the analogy appears inside the sub-section but names only C-34 and C-33 -- "C-34 is the per-element annotation upgrade to C-33." The reference pair (C-25 / C-23) is absent. Without both pairs named, the structural equivalence is an assertion, not a demonstrated analogy.

- **V-03** fails (a): the analogy appears inside the sub-section but names only C-25 and C-23 -- "this follows the same pattern as C-25 is to C-23." The current pair (C-34 / C-33) is absent. The statement describes the reference pair without identifying which criterion the pattern is being applied to.

- **V-04** fails both (b) and (c): analogy names only C-25/C-23 and appears outside the sub-section boundary. Two independent failure modes; either alone would fail C-36.

- **V-05** passes all three sub-clauses: "C-34 is to C-33 what C-25 is to C-23" stated explicitly within the sub-section, naming both the current pair and the reference pair. C-36 PASS.

---

## V-01 -- Analogy outside C-34 sub-section boundary

**Axis**: Structural analogy names both pairs correctly but appears in prose after the `#### C-33 Compliance Declaration` sub-section closes -- outside the sub-section boundary
**Hypothesis**: C-34 PASS, C-35 PASS, C-36 FAIL = 225/230

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

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-09 PASS, C-16 PASS.

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

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above) -- the Phase 4 / gap-analysis lifecycle token has been declared before this block emits; no forward-reference to future Phase 4 content is possible. C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step.
CELL-SOURCE: All six cells below draw from already-emitted content -- Phase 1 and Phase 4 lifecycle token annotations have both been written before this block; no cell contains a forward-reference to output not yet produced at block-emission time; all sub-clause designations, self-declaring signal field names, and grep instructions were established in earlier annotations and are restated verbatim here. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (confirming cells (i)-(iii) draw from already-emitted PHASE 1 COMPLETE: content) and grep for PHASE 4 COMPLETE: annotation (confirming cells (iv)-(vi) draw from already-emitted PHASE 4 COMPLETE: content) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. Both grep instructions stated verbatim in cells (iii) and (vi) above. C-29 PASS. C-31 PASS: PLACEMENT labeled field (within this block) names PHASE 4 COMPLETE: as the Phase 4 lifecycle token emitted above this block -- C-31(a) satisfied; CELL-SOURCE labeled field (within this block) confirms all six cells draw from already-emitted content with no forward-references -- C-31(b) satisfied; both declarations appear as labeled fields within this structural block, not as prose in surrounding context -- C-31(c) satisfied. C-32 PASS: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step -- C-32(a) satisfied; CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step -- C-32(b) satisfied; both grep instructions are embedded within their respective labeled fields as field content, not as surrounding prose outside the fields -- C-32 both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete

[End of C-33 Compliance Declaration sub-section]

Note on recursive design logic: C-34 is to C-33 what C-25 is to C-23 -- just as C-25 adds N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making completeness verifiable from any single token), C-34 adds per-element designator confirmations to the four C-33 elements (making compliance self-auditing from the labeled sub-section alone). This structural analogy motivates the C-34 design pattern.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 -- Analogy inside sub-section, current pair only (C-25/C-23 absent)

**Axis**: Structural analogy appears inside `#### C-33 Compliance Declaration` but names only C-34 and C-33 -- the reference pair C-25/C-23 is absent
**Hypothesis**: C-34 PASS, C-35 PASS, C-36 FAIL = 225/230

The prompt is identical to V-01 through the Phase 4 lifecycle token annotation. Only the `#### C-33 Compliance Declaration` sub-section differs:

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

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-09 PASS, C-16 PASS.

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
- THRESHOLD NOT MET: -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 + C-16. C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 + C-16. C-13 PASS, C-16 PASS.
- Pair 2 together: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

Remove-either-pair test:
- Removing Pair 1: Pair 2 alone -- C-20 PASS.
- Removing Pair 2: Pair 1 alone -- C-20 PASS.

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

Q: Does the literature make the inertia default worse than acting on this evidence?

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS). C-27 PASS: PHASE 1 COMPLETE: carries inertia_committed=[yes] (C-27(a) satisfied) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (C-27(b) satisfied). Adds a named gate token (C-16 PASS). Token 4 of 4 required for C-23. C-23 fully satisfied. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal confirming C-27(b) compliance at this boundary. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

## C-29 Operationalization Verification

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied: Phase 4 lifecycle token named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction.
CELL-SOURCE: All six cells below draw from already-emitted content. No forward-references. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction.

Phase 1 / C-27(a) boundary:
- Cell (i): C-27(a) named. CONFIRMED.
- Cell (ii): inertia_committed=[yes] field identified. CONFIRMED.
- Cell (iii): "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv): C-27(b) named. CONFIRMED.
- Cell (v): inertia_verified=[yes] field identified. CONFIRMED.
- Cell (vi): "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT field carries embedded grep instruction (C-32(a) satisfied); CELL-SOURCE field carries embedded grep instruction (C-32(b) satisfied); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-34 is the per-element annotation upgrade to C-33 -- this labeled sub-section names each C-33 element individually by designator, making C-33 compliance self-auditing without reading the closing declaration's aggregate structure.

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 -- Analogy inside sub-section, reference pair only (C-34/C-33 absent)

**Axis**: Structural analogy appears inside `#### C-33 Compliance Declaration` but names only C-25 and C-23 -- the current pair C-34/C-33 is absent
**Hypothesis**: C-34 PASS, C-35 PASS, C-36 FAIL = 225/230

Phases 1-4 and the C-30 block (through C-32 PASS) are identical to V-02. Only the `#### C-33 Compliance Declaration` sub-section differs:

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

This token emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27 Phase-1 status field satisfied -- inertia commitment observable at lifecycle token layer; C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending). Adds a named gate token (C-16 PASS). Token 1 of 4 required for C-23 (Phase 1 / claim-extraction boundary instrumented; C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: this token satisfies C-27(a). The inertia_committed=[yes] field is the self-declaring signal. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified, grep instruction embedded.

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

This token serves dual purpose: records threshold shortfall (C-09 PASS) and adds a named gate token (C-16 PASS). Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token: C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

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

Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4 (C-23 in progress at 3/4). C-22 PASS (Phase 2 + Phase 3 unconditional). Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification

Pair 1: THRESHOLD NOT MET: (C-09 + C-16) + RECOVERY NOTE: (C-12 + C-16). Together: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.
Pair 2: PHASE 2 COMPLETE: (C-09 + C-16) + PHASE 3 COMPLETE: (C-13 + C-16). Together: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.
Remove-either-pair test: Removing Pair 1: Pair 2 alone -- C-20 PASS. Removing Pair 2: Pair 1 alone -- C-20 PASS.
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

Emits unconditionally. inertia_verified=[yes] confirms C-14 PASS. C-27 PASS: PHASE 1 COMPLETE: inertia_committed=[yes] (C-27(a)) + PHASE 4 COMPLETE: inertia_verified=[yes] (C-27(b)). C-16 PASS. Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: C-27(b) satisfied. inertia_verified=[yes] is the self-declaring signal. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified, grep instruction embedded.

## C-29 Operationalization Verification

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction.
CELL-SOURCE: All six cells draw from already-emitted content. No forward-references. C-31(b) satisfied. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction.

Phase 1 / C-27(a) boundary:
- Cell (i): C-27(a) named. CONFIRMED.
- Cell (ii): inertia_committed=[yes] field identified. CONFIRMED.
- Cell (iii): "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv): C-27(b) named. CONFIRMED.
- Cell (v): inertia_verified=[yes] field identified. CONFIRMED.
- Cell (vi): "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

This follows the same structural pattern as C-25 is to C-23 -- C-25 adds per-token N-of-4 counter annotations to the four tokens required by C-23, making completeness verifiable from any single token without reading all four.

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 -- Combination: analogy outside sub-section AND only one pair named

**Axis**: Structural analogy appears in prose after the sub-section closes (fails sub-clause (c)) AND names only the reference pair C-25/C-23 -- the current pair C-34/C-33 is absent (fails sub-clause (a))
**Hypothesis**: C-34 PASS, C-35 PASS, C-36 FAIL = 225/230

Phases 1-4 and the C-30 block through C-32 PASS are identical to prior variations. The `#### C-33 Compliance Declaration` sub-section and the trailing prose differ:

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

INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

Emits unconditionally. inertia_committed=[yes] confirms C-14 front-loaded; C-27(a) satisfied -- inertia commitment observable at lifecycle token layer. C-16 PASS. Token 1 of 4 (C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: C-27(a) sub-clause identified, inertia_committed=[yes] is the self-declaring signal. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified, grep instruction embedded.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025? (WebSearch: "[claim topic] review 2020-2025")
3. What papers challenge this claim? (WebSearch: "[claim topic] criticism")
4. What papers establish methodological precedent? (WebSearch: "[claim topic] method")

If threshold not met: THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]
C-09 PASS, C-16 PASS. Pair 1, Token A.

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]
Emits unconditionally. C-16 PASS. Token 2 of 4. C-22 in progress. Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

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
Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4. C-22 PASS. Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification
Pair 1: THRESHOLD NOT MET: + RECOVERY NOTE: cover C-09, C-12, C-16. C-20 PASS independently.
Pair 2: PHASE 2 COMPLETE: + PHASE 3 COMPLETE: cover C-09, C-13, C-16. C-20 PASS independently.
Remove-either-pair test: Removing Pair 1: Pair 2 alone -- C-20 PASS. Removing Pair 2: Pair 1 alone -- C-20 PASS.
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

### Inertia verification

INERTIA SCENARIO: [repeat Phase 1 commitment -- unchanged]
INERTIA RISK: [why evidence makes the inertia default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence]

PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]
Emits unconditionally. inertia_verified=[yes] confirms C-14 PASS. C-27 PASS. C-16 PASS. Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: C-27(b) sub-clause identified, inertia_verified=[yes] is the self-declaring signal. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified, grep instruction embedded.

## C-29 Operationalization Verification

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction.
CELL-SOURCE: All six cells draw from already-emitted content. No forward-references. C-31(b) satisfied. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction.

Phase 1 / C-27(a) boundary:
- Cell (i): C-27(a) named. CONFIRMED.
- Cell (ii): inertia_committed=[yes] identified. CONFIRMED.
- Cell (iii): "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv): C-27(b) named. CONFIRMED.
- Cell (v): inertia_verified=[yes] identified. CONFIRMED.
- Cell (vi): "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete

[End of C-33 Compliance Declaration sub-section]

Design note: this labeled sub-section follows the same pattern as C-25 is to C-23, adding per-element attestations to the C-33 closing declaration in the same way C-25 adds N-of-4 counter annotations to the C-23 lifecycle tokens.

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 -- Full synthesis: both pairs named inside sub-section (C-36 PASS)

**Axis**: Structural analogy "C-34 is to C-33 what C-25 is to C-23" appears explicitly inside the `#### C-33 Compliance Declaration` sub-section, naming both pairs
**Hypothesis**: C-34 PASS, C-35 PASS, C-36 PASS = 230/230

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

This token serves dual purpose: records threshold shortfall without YAML parsing (C-09 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token A. C-09 PASS, C-16 PASS.

For each source, answer per-source questions before entering in table. For any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell requiring secondary search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}

This token serves dual purpose: makes recovery step body-visible and auditable (C-12 PASS) and adds a named gate token (C-16 PASS). This is Pair 1, Token B -- failure/recovery pair complete. Pair 1 summary: THRESHOLD NOT MET: covers C-09 + C-16; RECOVERY NOTE: covers C-12 + C-16; together: C-09, C-12, C-16 -- three distinct aspirational criteria. C-09 PASS, C-12 PASS, C-16 PASS. C-20 PASS for Pair 1 independently.

Every cell must contain real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]

This token emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE:, whether threshold met or not; only the status field differs. Adds a named gate token (C-16 PASS). Token 2 of 4 required for C-23 (Phase 2 / evidence-gathering boundary instrumented; C-23 in progress at 2/4). First of two required unconditional lifecycle tokens for C-22 (C-22 in progress). This is Pair 2, Token A. C-09 PASS, C-16 PASS.

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
- THRESHOLD NOT MET: -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- RECOVERY NOTE: -- covers C-12 + C-16. C-12 PASS, C-16 PASS.
- Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named. Both carry PASS annotations. C-20 PASS for Pair 1 independently.

Pair 2 -- lifecycle axis:
- PHASE 2 COMPLETE: -- covers C-09 + C-16. C-09 PASS, C-16 PASS.
- PHASE 3 COMPLETE: -- covers C-13 + C-16. C-13 PASS, C-16 PASS.
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

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above) -- the Phase 4 / gap-analysis lifecycle token has been declared before this block emits; no forward-reference to future Phase 4 content is possible. C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step.
CELL-SOURCE: All six cells below draw from already-emitted content -- Phase 1 and Phase 4 lifecycle token annotations have both been written before this block; no cell contains a forward-reference to output not yet produced at block-emission time; all sub-clause designations, self-declaring signal field names, and grep instructions were established in earlier annotations and are restated verbatim here. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (confirming cells (i)-(iii) draw from already-emitted PHASE 1 COMPLETE: content) and grep for PHASE 4 COMPLETE: annotation (confirming cells (iv)-(vi) draw from already-emitted PHASE 4 COMPLETE: content) in output above -- all six cells reference already-emitted content; C-31(b) cell-source confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. Both grep instructions stated verbatim in cells (iii) and (vi) above. C-29 PASS. C-31 PASS: PLACEMENT labeled field (within this block) names PHASE 4 COMPLETE: as the Phase 4 lifecycle token emitted above this block -- C-31(a) satisfied; CELL-SOURCE labeled field (within this block) confirms all six cells draw from already-emitted content with no forward-references -- C-31(b) satisfied; both declarations appear as labeled fields within this structural block, not as prose in surrounding context -- C-31(c) satisfied. C-32 PASS: PLACEMENT field carries embedded grep instruction making C-31(a) placement citation procedurally executable in a single deterministic step -- C-32(a) satisfied; CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in a single deterministic step -- C-32(b) satisfied; both grep instructions are embedded within their respective labeled fields as field content, not as surrounding prose outside the fields -- C-32 both-or-nothing confirmed.

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
2. Which contrary paper must be directly addressed, and what should the response strategy be?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
