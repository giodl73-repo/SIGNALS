Done. Here is the v5 rubric summary:

---

**Two new criteria from R4:**

| # | Name | Source | Depends on |
|---|------|--------|------------|
| C-19 | Typed Token Schema Block | V-03/V-04/V-05 R4 | C-17 (extends it) |
| C-20 | Dual Multi-Criterion Token Synthesis | V-05 R4 | C-18 (extends it) |

**C-19** captures the typed schema box pattern: `Token:` / `Schema:` / `Fields:` / `Required when:` / `Unacceptable:` with authoritative variable names. This closes the slot-label mismatch that kept R3 V-05 at C-17 PARTIAL -- prose obligations allow abbreviation in output; a typed schema block does not. Dependency chain: C-15 -> C-17 -> C-19.

**C-20** captures the full-synthesis pattern from V-05: two distinct tokens each carry a dual-criterion annotation, covering at least three distinct criteria total. C-18 rewards one token doing double duty; C-20 requires two, making the coverage holistic rather than coincidental. C-18 FAIL blocks C-20.

**Scoring:**

| Tier | v4 | v5 |
|------|----|----|
| Aspirational | 10 / 50 pts | 12 / 60 pts |
| Total ceiling | 140 | 150 |
a stronger form of contract-to-token binding; C-17 FAIL/PARTIAL blocks C-19
- C-20 depends on C-18 -- dual-instance synthesis requires the single-instance pattern to already hold; C-18 FAIL blocks C-20
- C-19 and C-20 reward *precision* and *scale* respectively: C-19 closes the format gap in C-17 by making field names unambiguous; C-20 raises the bar from one multi-criterion token to two, forcing the output infrastructure to be designed holistically rather than as a one-off trick
- Together these continue the integration-quality trajectory started in v4: ceiling raises only when a variation can demonstrate synthesis across multiple design layers

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-20 | 5 | 60 |
| **Total** | | | **150** |

Composite score = points earned / 100 * 100 (capped at 100 for golden bar purposes). Golden bar = all essential pass AND composite >= 80.

---

## ESSENTIAL Criteria (60 points -- all must pass for golden bar)

### C-01 Claims Extracted Before Search
- **Category**: correctness
- **Weight**: essential
- **Text**: Phase 1 extracts a list of specific, falsifiable claims from the topic and identifies what contrary evidence would undermine each before any search begins.
- **Pass condition**: At least 3 distinct claims appear in Phase 1 output, each stated as a proposition (not a question). Each claim is accompanied by a note on what contrary evidence would undermine it.

### C-02 Citation Table Present
- **Category**: format
- **Weight**: essential
- **Text**: Phase 2 produces a citation table with all required columns for each source found.
- **Pass condition**: At least one Markdown table appears with columns Title, Authors, Year, Venue, Claim #, Position (supports/contradicts/qualifies), and Key finding. Rows contain non-placeholder values.

### C-03 Four-Tier Literature Map Built
- **Category**: correctness
- **Weight**: essential
- **Text**: Phase 3 organizes sources into FOUNDATIONAL, RECENT, CONTRARY, and METHODOLOGICAL tiers, each with at least one entry and a one-sentence justification.
- **Pass condition**: All four tier headings appear; each tier has >= 1 cited source with a justification sentence. RECENT tier entries are dated 2020 or later.

### C-04 Gap Analysis Recommendation Issued
- **Category**: correctness
- **Weight**: essential
- **Text**: Phase 4 states claims with strong vs. weak support, lists contrary evidence to address, and issues a PROCEED / SEARCH MORE / REFRAME CLAIM recommendation.
- **Pass condition**: Output contains a gap analysis block with counts of supported vs. unsupported claims, at least one item under contrary evidence (or explicit "none"), and a clearly stated recommendation keyword (PROCEED, SEARCH MORE, or REFRAME CLAIM).

### C-05 Artifact Written with Required Frontmatter
- **Category**: behavior
- **Weight**: essential
- **Text**: Skill writes a signal artifact to the correct path with all required frontmatter fields.
- **Pass condition**: A file exists at `signals/discover/literature/{topic}-literature-{date}.md` (or the `--output` path). Frontmatter contains skill, topic, date, claims_checked, sources_found, and high_risk_claims fields, all populated with non-null values.

---

## RECOMMENDED Criteria (30 points -- output is better with these)

### C-06 Contrary Evidence Mapped to Claims
- **Category**: depth
- **Weight**: recommended
- **Text**: Phase 3 CONTRARY tier maps each contrary paper back to the specific claim it challenges, and Phase 5 identifies the single most dangerous contrary paper with a suggested response framing.
- **Pass condition**: Each CONTRARY entry references a claim number or label. Phase 5 item 2 names the contrary paper and proposes a rebuttal direction (scope qualification, methodological distinction, or domain limitation).

### C-07 WebSearch Evidence Visible
- **Category**: behavior
- **Weight**: recommended
- **Text**: The artifact shows evidence of actual WebSearch execution -- real titles, authors, years, and venues rather than generic placeholders.
- **Pass condition**: At least 5 distinct sources appear with real author names, publication years between 1990-2025, and venue names (journal, conference, or preprint server). No row contains placeholder text such as "Author et al." or "[title]".

### C-08 High-Risk Claims Flagged
- **Category**: coverage
- **Weight**: recommended
- **Text**: Any claim with no supporting literature and strong contrary evidence is explicitly flagged HIGH RISK with a scoping or reframing suggestion.
- **Pass condition**: If high_risk_claims >= 1 in frontmatter, the body contains a HIGH RISK block per flagged claim with a concrete suggestion (scope, qualify, or drop). If high_risk_claims = 0, the gap analysis explicitly states why no claim is at risk.

---

## ASPIRATIONAL Criteria (60 points -- raise the bar once essential/recommended are stable)

### C-09 Depth Mode Source Threshold Met
- **Category**: coverage
- **Weight**: aspirational
- **Text**: Source count meets the threshold for the active depth mode (quick >= 5, standard >= 15, deep >= 25).
- **Pass condition**: sources_found in frontmatter >= threshold for the active depth mode. Pass if threshold is met or exceeded.

### C-10 Methodological Precedent Chain
- **Category**: depth
- **Weight**: aspirational
- **Text**: The METHODOLOGICAL tier forms a traceable precedent chain -- each entry identifies the paper that established the method and its publication year, showing the method predates the current work.
- **Pass condition**: Each METHODOLOGICAL entry names the originating paper and includes a year. The chain shows the method was established before the current work (all years < current paper year).

### C-11 Interrogative Obligation Satisfied
- **Category**: correctness
- **Weight**: aspirational
- **Source**: V-04 R1 excellence signal
- **Text**: Every phase-gate is structured as questions the run must answer, not imperatives it may satisfy with vague prose. Each question receives a specific, non-generic answer.
- **Pass condition**: Each phase output contains numbered or labeled answers corresponding to the questions posed in the skill prompt. No question is skipped or deflected with a non-answer ("N/A", "see above", generic restatement of the question). Pass if >= 80% of questions receive specific answers.

### C-12 Anti-Placeholder Recovery Executed
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-04 + V-02 R1 excellence signal
- **Text**: When a citation cell is unknown at first pass, the skill searches again rather than leaving a placeholder. The recovery step is either successful (cell filled with real data) or explicitly acknowledged (noted as "not found after secondary search").
- **Pass condition**: Zero unacknowledged placeholder cells in the citation table. Any cell that could not be filled shows one of: (a) real data from a follow-up search, or (b) an explicit "not found after secondary search" note. A cell containing "Author et al.", "[title]", "TBD", or similar generic text with no recovery note is a failure.

### C-13 Empty-Tier Acknowledgment Present
- **Category**: coverage
- **Weight**: aspirational
- **Source**: V-04 R1 excellence signal
- **Text**: Any four-tier map tier with zero entries contains an explicit "NONE FOUND" statement and a one-sentence explanation of why no sources qualified -- preventing silent omission from being indistinguishable from a complete pass.
- **Pass condition**: For each of the four tiers (FOUNDATIONAL, RECENT, CONTRARY, METHODOLOGICAL), either: (a) at least one cited source appears, or (b) the tier contains "NONE FOUND" followed by a reason sentence. A tier heading with no entries and no acknowledgment is a failure.

### C-14 Inertia Guard on PROCEED
- **Category**: correctness
- **Weight**: aspirational
- **Source**: V-05 R1 excellence signal
- **Text**: The gap analysis explicitly considers the inertia scenario before issuing PROCEED -- acknowledging that teams may do nothing even with strong evidence, and that the recommendation accounts for what would make inertia the dominant path.
- **Pass condition**: The gap analysis block contains a sentence or subsection that names the inertia risk: why a team might ignore this literature and do nothing. If the recommendation is PROCEED, it must address why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM, inertia risk may be noted without counter-argument.

### C-15 Dual-Domain Obligation Preamble
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-05 R2 excellence signal
- **Text**: The skill output opens with a preamble (before Phase 1 content) that states both the anti-placeholder recovery obligation and the empty-tier acknowledgment obligation as non-optional constraints applying to every subsequent phase. A global enforcement contract is more reliable than per-phase rules because it cannot be silently dropped when a phase is skipped or abbreviated.
- **Pass condition**: A preamble section appears before Phase 1 output that explicitly names both: (a) the recovery obligation -- any unknown cell must be searched again or noted as "not found after secondary search", and (b) the empty-tier obligation -- any tier with no entries must state "NONE FOUND" with a reason. Both must be framed as non-optional. A preamble covering only one of the two obligations is a PARTIAL, not a PASS.

### C-16 Template-Label Checkability
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-05 R2 excellence signal
- **Text**: Structural gates produce named output tokens rather than prose descriptions, making compliance grep-verifiable rather than inference-dependent. Any gate that can be satisfied with vague prose is weaker than one that requires a specific labeled field in the output.
- **Pass condition**: At minimum, the C-14 inertia gate output contains the tokens `INERTIA SCENARIO:` and `INERTIA RISK:` as labeled fields. Any other structural gate introduced by the skill variant also uses a named token. A structural gate whose compliance must be inferred from surrounding prose is a failure for this criterion.

### C-17 Contract-to-Token Binding
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-05 R3 excellence signal
- **Text**: When the C-15 enforcement contract names an obligation (e.g., empty-tier acknowledgment), it also specifies the exact output token the obligation requires (e.g., `TIER EMPTY: [reason]`). Contract compliance then directly produces the verifiable token -- the obligation text and the token specification are the same instruction. A contract that declares an obligation without naming the output format leaves a gap: compliance can be claimed without producing anything grep-verifiable.
- **Pass condition**: The C-15 preamble (or enforcement contract) contains at least one explicit token format alongside the obligation text -- e.g., "OBLIGATION B requires output in the format `TIER EMPTY: [reason]`". The token named in the contract must match the token actually produced in Phase 3 output. If C-15 is FAIL or PARTIAL, this criterion cannot PASS.

### C-18 Multi-Criterion Token Reuse
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R3 excellence signal
- **Text**: A single named gate token covers more than one criterion simultaneously. The canonical example is `THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]`, which satisfies C-09 (threshold failure is observable) and extends C-16 (adds a named gate token beyond the inertia pair). Designing tokens that serve double duty reduces prompt complexity while increasing coverage. A variation qualifies if it introduces a token not already required by prior criteria whose presence satisfies an additional criterion.
- **Pass condition**: The skill variation contains at least one named output token that satisfies two or more distinct aspirational criteria. The token must be identified, both criteria it satisfies must be named, and both must score PASS for this criterion to PASS. A token that satisfies only one criterion is normal C-16 coverage, not multi-criterion reuse.

### C-19 Typed Token Schema Block
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-03/V-04/V-05 R4 excellence signal
- **Text**: The enforcement contract declares each output token's format using a formal schema block rather than inline prose. The schema block uses explicit fields -- `Token:`, `Schema:`, `Fields:`, `Required when:`, `Unacceptable:` -- and the variable names declared in `Fields:` become authoritative. Phase 3 output uses those exact variable names, eliminating the slot-label mismatch that results when prose obligations use long descriptive phrases that get abbreviated differently in output. A prose obligation such as "output in the format `TIER EMPTY: [reason why no sources qualified]`" allows Phase 3 to use `[reason]`; a typed schema block with `Fields: {why_no_sources_qualified}` forecloses all abbreviation variants.
- **Pass condition**: At least one obligation in the C-15 enforcement contract uses a typed schema block containing Token, Schema, Fields, and Unacceptable lines. The variable names declared in `Fields:` appear verbatim in the corresponding Phase 3 output -- not abbreviated, paraphrased, or replaced with generic slot labels. If C-17 is FAIL or PARTIAL, this criterion cannot PASS. Typed schema is a precision upgrade to contract-to-token binding; the dependency chain is C-15 -> C-17 -> C-19.

### C-20 Dual Multi-Criterion Token Synthesis
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R4 excellence signal
- **Text**: Two or more distinct named output tokens each satisfy multiple criteria simultaneously, each carrying an explicit annotation paragraph naming the covered criteria. Together the annotated tokens cover at least three distinct aspirational criteria. This extends C-18 from a single instance to a coordinated multi-token infrastructure -- the output design is holistic, not opportunistic. The canonical R4 instance: `THRESHOLD NOT MET:` annotated as covering C-09 + C-16, and `RECOVERY NOTE:` annotated as covering C-12 + C-16 -- two tokens, four named criterion-coverages, three distinct criteria (C-09, C-12, C-16). Token reuse of a previously covered criterion (C-16 appears in both annotations) is permitted; what must be distinct is the additional criterion each token introduces beyond the shared one.
- **Pass condition**: At least two distinct named tokens each carry an annotation paragraph that (a) names the token, (b) lists two or more distinct criteria it covers, and (c) confirms all listed criteria PASS. The two tokens together must name at least three distinct aspirational criteria. A single token with two annotations does not satisfy this criterion -- two distinct tokens are required. If C-18 is FAIL, this criterion cannot PASS.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-19 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-19 | Added C-11..C-14 from R1 excellence signals (V-04: interrogative obligation, anti-placeholder recovery, empty-tier acknowledgment; V-05: inertia guard on PROCEED) |
| v3 | 2026-03-19 | Added C-15..C-16 from R2 excellence signals (V-05: dual-domain obligation preamble, template-label checkability); aspirational ceiling 30 -> 40, total ceiling 120 -> 130 |
| v4 | 2026-03-19 | Added C-17..C-18 from R3 excellence signals (V-05: contract-to-token binding, multi-criterion token reuse); aspirational ceiling 40 -> 50, total ceiling 130 -> 140 |
| v5 | 2026-03-19 | Added C-19..C-20 from R4 excellence signals (V-03/V-04/V-05: typed token schema block, dual multi-criterion token synthesis); aspirational ceiling 50 -> 60, total ceiling 140 -> 150 |

---

**Key decisions:**

- **C-17 depends on C-15** -- contract-to-token binding is only meaningful if a C-15 enforcement contract exists. If C-15 is FAIL or PARTIAL, C-17 cannot PASS.
- **C-19 depends on C-17** -- typed schema is a precision upgrade to contract-to-token binding, not an independent mechanism. The dependency chain is C-15 -> C-17 -> C-19: contract exists, contract names tokens, contract declares token schemas with authoritative field names. C-17 FAIL/PARTIAL blocks C-19.
- **C-18 requires naming both criteria** -- a token that happens to be grep-verifiable is already C-16 coverage. C-18 triggers only when a token is explicitly designed to satisfy an additional criterion. The pass condition requires identifying the token and both criteria it covers.
- **C-20 depends on C-18** -- dual-instance synthesis presupposes the single-instance pattern. C-18 FAIL blocks C-20. C-20 adds a coverage floor (three distinct criteria total) and a count floor (two distinct tokens) that a single-instance design cannot meet.
- **C-19 and C-20 reward precision and scale** -- C-19 closes the format gap exposed by R3 C-17 PARTIAL (slot-label mismatch between prose obligation and abbreviated Phase 3 output); C-20 raises the multi-criterion bar from one token to two, requiring the output infrastructure to be designed as a system rather than exploiting a single coincidence.
- **Ceiling trajectory**: v1: 120 -> v2: 125 -> v3: 130 -> v4: 140 -> v5: 150. Each increment captures patterns that were achievable but not rewarded under the prior ceiling.
