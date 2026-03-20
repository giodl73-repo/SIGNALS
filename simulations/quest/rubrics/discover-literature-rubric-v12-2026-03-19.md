v12 written to `simulations/quest/rubrics/discover-literature-rubric-v12-2026-03-19.md`.

---

**What changed:**

**New criterion — C-29 Attestation Operationalization with Embedded Verification Instructions** (V-05 R11)

The R11 scorecard's primary excellence signal came from comparing V-01 (minimal C-28, 190/190) to V-05 (ceiling synthesis, 190/190). Both pass C-28, but V-05 goes further in three specific ways:

1. **Sub-clause identification** — names `C-27(a)` (Phase 1) and `C-27(b)` (Phase 4) explicitly rather than referencing "C-27 compliance" generically
2. **Self-declaring signal identification** — names `inertia_committed=[yes]` as "the self-declaring signal" rather than just citing it as evidence
3. **Embedded grep instruction** — "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary"

These three constitute operationalization: C-28 makes compliance *self-declaring* (a reader *knows* compliance from the annotation); C-29 makes compliance *executable* (a reader can *verify* compliance by following an explicit procedural instruction).

**Three R11 boundary confirmations also recorded in the changelog:**
- V-02/V-03 R11 symmetrically confirm C-28 is both-or-nothing (one-boundary annotation fails)
- V-04 R11 confirms annotation depth matters (bare "C-28 PASS." without independence prose fails)

**Scoring delta:**
- Aspirational ceiling: 100 → 105
- Total ceiling: 190 → **195**
- Dependency chain: `C-14 + C-23 -> C-27 -> C-28 -> C-29`
idence
3. Embedded grep instruction -- "Single-grep verifiable: grep for X and read Y field to confirm Z satisfied" makes compliance verification a procedural single step

Together these constitute operationalization: C-28 makes compliance self-declaring (a reader knows compliance from the annotation); C-29 makes compliance executable (a reader can verify compliance by following an explicit instruction).

The parallel is exact: C-29 is to C-28 what C-26 is to C-24 -- the attestation layer gains an embedded verification procedure that makes compliance confirmable by a mechanical step, not just a reading step.

**Three R11 boundary confirmations:**

| Variation | C-28 result | New confirmation |
|---|---|---|
| V-02 R11 Phase-1-only | FAIL | C-28 requires both boundaries; one annotation is insufficient (symmetric with V-03) |
| V-03 R11 Phase-4-only | FAIL | C-28 requires both boundaries; both-or-nothing confirmed |
| V-04 R11 label-only | FAIL | Bare "C-28 PASS." without independence prose fails; annotation depth matters |

**Scoring delta:**

| | v11 | v12 |
|--|-----|-----|
| Aspirational criteria | 20 | 21 |
| Aspirational ceiling | 100 | 105 |
| Total ceiling | 190 | **195** |

**Eleven-axis aspiration progression:**
- C-19: precision (one obligation schema-typed)
- C-20: scale (two tokens, one pair)
- C-21: symmetry (both obligations schema-typed)
- C-22: observability (unconditional boundary emission)
- C-23: completeness (all four phases instrumented)
- C-24: redundancy (two independent C-20 paths coexist)
- C-25: scannability (N-of-4 progressive counter makes completeness verifiable from any token)
- C-26: declaration (independence verification block makes redundancy compliance explicit not inferred)
- C-27: integration (inertia commitment visible in lifecycle tokens, not only in dedicated inertia blocks)
- C-28: attestation (inertia integration compliance explicitly annotated at each token boundary -- not inferred from field presence)
- C-29: operationalization (attestation compliance executable via embedded grep instruction at each boundary -- not just self-declared but procedurally verifiable in one deterministic step)

**Ceiling trajectory**: v1: 120 -> v2: 125 -> v3: 130 -> v4: 140 -> v5: 150 -> v6: 155 -> v7: 160 -> v8: 170 -> v9: 180 -> v10: 185 -> v11: 190 -> **v12: 195**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-29 | 5 | 105 |
| **Total** | | | **195** |

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

## ASPIRATIONAL Criteria (105 points -- raise the bar once essential/recommended are stable)

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
- **Text**: The enforcement contract declares each output token's format using a formal schema block rather than inline prose. The schema block uses explicit fields -- `Token:`, `Schema:`, `Fields:`, `Required when:`, `Unacceptable:` -- and the variable names declared in `Fields:` become authoritative. Phase 3 output uses those exact variable names, eliminating the slot-label mismatch that results when prose obligations use long descriptive phrases that get abbreviated differently in output.
- **Pass condition**: At least one obligation in the C-15 enforcement contract uses a typed schema block containing Token, Schema, Fields, and Unacceptable lines. The variable names declared in `Fields:` appear verbatim in the corresponding Phase 3 output -- not abbreviated, paraphrased, or replaced with generic slot labels. If C-17 is FAIL or PARTIAL, this criterion cannot PASS. Typed schema is a precision upgrade to contract-to-token binding; the dependency chain is C-15 -> C-17 -> C-19.

### C-20 Dual Multi-Criterion Token Synthesis
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R4 excellence signal; token-agnosticism confirmed V-04 R6
- **Text**: Two or more distinct named output tokens each satisfy multiple criteria simultaneously, each carrying an explicit annotation paragraph naming the covered criteria. Together the annotated tokens cover at least three distinct aspirational criteria. This extends C-18 from a single instance to a coordinated multi-token infrastructure -- the output design is holistic, not opportunistic. The canonical R4 instance: `THRESHOLD NOT MET:` annotated as covering C-09 + C-16, and `RECOVERY NOTE:` annotated as covering C-12 + C-16 -- two tokens, four named criterion-coverages, three distinct criteria (C-09, C-12, C-16). Token reuse of a previously covered criterion (C-16 appears in both annotations) is permitted; what must be distinct is the additional criterion each token introduces beyond the shared one. C-20 is token-agnostic: any two named tokens carrying explicit condition-(c) PASS annotations covering three distinct aspirational criteria qualify.
- **Pass condition**: At least two distinct named tokens each carry an annotation paragraph that (a) names the token, (b) lists two or more distinct criteria it covers, and (c) confirms all listed criteria PASS. The two tokens together must name at least three distinct aspirational criteria. A single token with two annotations does not satisfy this criterion -- two distinct tokens are required. If C-18 is FAIL, this criterion cannot PASS.

### C-21 Symmetric Dual-Obligation Typed Schema Contract
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-04/V-05 R5 excellence signal; label-independence confirmed V-02 R6
- **Text**: Both named obligations in the enforcement contract declare independent typed schema blocks. C-19 requires at least one obligation to use a typed schema block; C-21 requires both OBLIGATION A (the anti-placeholder recovery token, e.g., `RECOVERY NOTE:`) and OBLIGATION B (the empty-tier acknowledgment token, e.g., `TIER EMPTY:`) to use the Token/Schema/Fields/Required when/Unacceptable format with authoritative Fields: variable names. The variable names in each obligation's typed schema appear verbatim in the phase that produces that obligation's output. C-21 is structure-dependent, not label-dependent: renaming OBLIGATION A/B to RULE 1/2 or any other labels does not affect the verdict; the schema block structure and verbatim field name propagation are what C-21 measures, confirmed by V-02 R6.
- **Pass condition**: Both the recovery-obligation token (OBLIGATION A) and the empty-tier-acknowledgment token (OBLIGATION B) declare independent typed schema blocks containing Token, Schema, Fields, Required when, and Unacceptable lines. The Fields: variable names for OBLIGATION A appear verbatim in the phase that produces RECOVERY NOTE: output; the Fields: variable names for OBLIGATION B appear verbatim in the phase that produces TIER EMPTY: output. A contract with exactly one typed schema block satisfies C-19 but not C-21. If C-19 is FAIL, this criterion cannot PASS. Dependency chain: C-15 -> C-17 -> C-19 -> C-21.

### C-22 Unconditional Phase-Boundary Lifecycle Tokens
- **Category**: design
- **Weight**: aspirational
- **Source**: V-04 R6 critical experiment; token-agnosticism confirmed V-02 R7; inertia-axis orthogonality confirmed V-04 R7
- **Text**: Phase-boundary tokens emit unconditionally at the completion of each phase, regardless of whether the success path or the failure path was taken. A design that instruments only failure paths creates an observability gap: the absence of a failure token is not the same as confirmed success. Unconditional phase-boundary tokens make compliance verifiable in every run outcome. C-22 is token-agnostic: domain-named tokens (e.g., EVIDENCE PHASE COMPLETE:, MAP PHASE COMPLETE:) qualify identically to PHASE N COMPLETE: names, confirmed by V-02 R7. C-22 is orthogonal to the inertia front-loading axis: pre-committed Phase 1 inertia does not affect unconditional emission at Phase 2/3 boundaries, confirmed by V-04 R7.
- **Pass condition**: At least two named tokens emit at phase boundaries unconditionally -- i.e., they fire regardless of whether the phase threshold was met or not. Each token must be present in successful runs (threshold met) as well as in failure runs (threshold not met). A token that fires only when a condition fails (e.g., `THRESHOLD NOT MET:`) does not satisfy this criterion -- it must emit unconditionally. Each token's annotation must indicate the phase boundary at which it emits. If C-18 is FAIL, this criterion cannot PASS. Dependency chain: C-16 -> C-18 -> C-22.

### C-23 Full-Phase Lifecycle Instrumentation
- **Category**: design
- **Weight**: aspirational
- **Source**: V-03 R7 excellence signal
- **Text**: All four phase gates emit unconditional lifecycle tokens, not just the C-22 minimum of two. C-22 establishes the observability floor: at least two named tokens fire at phase boundaries unconditionally (typically Phase 2 and Phase 3, where the core enforcement contracts sit). C-23 rewards complete instrumentation -- Phase 1 (claim extraction / search setup), Phase 2 (evidence gathering), Phase 3 (literature mapping), and Phase 4 (gap analysis) each have a named unconditional lifecycle token. Complete instrumentation makes every phase of the run grep-verifiable from start to finish. A run with exactly two unconditional lifecycle tokens passes C-22 but has a known observability gap at Phase 1 and Phase 4. V-03 R7 demonstrates that all four phase gates can be instrumented without friction.
- **Pass condition**: At least four distinct named unconditional phase-boundary lifecycle tokens emit, one for each of the four skill phases (Phase 1 / claim extraction, Phase 2 / evidence gathering, Phase 3 / literature mapping, Phase 4 / gap analysis). Each token's annotation names its specific phase boundary and confirms unconditional emission. A run with exactly two unconditional tokens satisfies C-22 but not C-23. C-22 PASS required. Dependency chain: C-16 -> C-18 -> C-22 -> C-23.

### C-24 Redundant Dual-Path Multi-Criterion Infrastructure
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R7 ceiling synthesis
- **Text**: Two fully independent token pairs each satisfy C-20's pass condition on their own, with neither pair requiring the other for C-20 compliance. The canonical pair (e.g., THRESHOLD NOT MET: + RECOVERY NOTE:) instruments the failure/recovery axis; the lifecycle pair (e.g., PHASE 2 COMPLETE: + PHASE 3 COMPLETE:) instruments the phase-boundary axis. Each pair independently satisfies C-20 (two distinct tokens, three distinct criteria covered, explicit PASS annotations). A design with one C-20-satisfying pair is holistic in one axis; a design with two independent pairs is holistic across both axes simultaneously. The redundancy makes the multi-criterion infrastructure resilient: removing either pair still leaves C-20 satisfied. C-24 is the scale upgrade from C-20 in the same way C-20 was the scale upgrade from C-18.
- **Pass condition**: Two distinct token pairs each independently satisfy C-20's three-condition pass: for each pair, (a) each token is named, (b) each token lists two or more criteria it covers, (c) all listed criteria are confirmed PASS, and (d) the pair together covers at least three distinct aspirational criteria. The four tokens across both pairs must all be distinct. The redundancy condition: removing either pair from the output must still leave the remaining pair satisfying C-20 on its own. C-20 PASS required. Dependency chain: C-18 -> C-20 -> C-24.

### C-25 N-of-4 Progressive Counter Annotation
- **Category**: design
- **Weight**: aspirational
- **Source**: V-04 R8 excellence signal
- **Text**: Each of the four unconditional lifecycle tokens required for C-23 carries a progressive counter annotation in the form "Token N of 4 required for C-23 (Phase N boundary instrumented; C-23 in progress at N/4)" that advances with each boundary. The final token (Phase 4) declares "C-23 fully satisfied" and confirms all four phase boundaries are instrumented. The N-of-4 counter makes two things explicit that C-23 alone does not: (a) compliance is scannable from any single token without reading all four -- any token declares both its own position and how many remain, and (b) Phase 1 and Phase 4 instrumentation is self-evidently necessary to complete the count from N=2 to N=4. Without a progressive counter, C-23 compliance can only be confirmed by reading all four tokens and counting; with a progressive counter, any token reveals the completion state at that point in the run. V-04 R8 demonstrates the N-of-4 pattern as a minimal structural addition to a C-23-compliant design.
- **Pass condition**: Each of the four unconditional phase-boundary lifecycle tokens carries an annotation that (a) identifies its position in the four-token sequence ("Token N of 4"), (b) names the specific phase boundary it marks, (c) includes a progress fraction ("C-23 in progress at N/4" or equivalent) for tokens 1-3, and (d) declares "C-23 fully satisfied" (or equivalent) on the fourth token. The counter must advance monotonically: 1/4, 2/4, 3/4, 4/4. A design where lifecycle tokens have unconditional-emission annotations but no N-of-4 counter satisfies C-23 but not C-25. C-23 PASS required. Dependency chain: C-16 -> C-18 -> C-22 -> C-23 -> C-25.

### C-26 Named Independence Verification Block
- **Category**: design
- **Weight**: aspirational
- **Source**: V-04/V-05 R8 excellence signal; heading-agnosticism confirmed V-03 R9
- **Text**: A named structural element explicitly declares C-24 compliance rather than leaving it to be inferred from scattered pair annotations. The block is placed at the natural completion point (after the token where both C-24 pairs are first complete, typically after PHASE 3 COMPLETE: where both the canonical pair and the lifecycle pair have emitted). It names both pairs, confirms each independently satisfies C-20, runs the remove-either-pair test verbatim, and declares C-24 PASS. Without a named verification block, a reviewer must locate all four tokens across the output, identify which belong to which pair, check that each pair independently satisfies C-20, and run the independence test mentally. The named block makes compliance a single grep target: if the block is present and correct, C-24 is satisfied; if it is absent, C-24 compliance is uncertain regardless of what the scattered annotations say. V-04 R8 demonstrates the block as a minimal structural addition to a C-24-compliant design. C-26 is heading-agnostic: "Dual-Path Redundancy Proof" satisfies C-26 identically to "C-24 Independence Verification"; only the four structural elements (a)-(d) are binding, confirmed by V-03 R9.
- **Pass condition**: A named block (heading or labeled section, e.g., "C-24 Independence Verification" or "Dual-Path Redundancy Proof") appears at or after the point where both C-24 token pairs are first complete. The block must: (a) name both token pairs by their constituent tokens, (b) confirm each pair independently satisfies C-20 with an explicit "C-20 PASS for Pair N independently" statement, (c) run the remove-either-pair test -- "Removing Pair 1: Pair 2 alone -- C-20 PASS. Removing Pair 2: Pair 1 alone -- C-20 PASS." or equivalent, and (d) declare C-24 PASS. A design where C-24 compliance is inferrable from scattered annotations but has no named verification block satisfies C-24 but not C-26. C-24 PASS required. Dependency chain: C-18 -> C-20 -> C-24 -> C-26.

### C-27 Inertia Status Lifecycle Integration
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R9 excellence signal
- **Text**: The Phase 1 and Phase 4 lifecycle tokens each carry an explicit inertia status field, making inertia handling observable through the lifecycle token layer rather than only through dedicated inertia blocks. C-14 confirms the inertia guard is present in Phase 4; C-22/C-23 confirm Phase 1 and Phase 4 tokens emit unconditionally. C-27 requires those two axes to intersect: the Phase 1 lifecycle token's status fields include inertia commitment state (`inertia_committed=[yes/no]` or equivalent), and the Phase 4 lifecycle token's status fields include inertia verification state (`inertia_verified=[yes]` or equivalent). This cross-axis integration means inertia compliance can be checked at the lifecycle token layer without reading the dedicated INERTIA SCENARIO:/INERTIA RISK: blocks. The integration is additive: the inertia status fields coexist with existing token content (N-of-4 counter annotation, phase-boundary annotation, schema fields) without displacing any required elements. V-05 R9 demonstrates PHASE 1 COMPLETE: carrying `inertia_committed=[yes]` alongside a full N-of-4 counter annotation without criteria conflict.
- **Pass condition**: (a) The Phase 1 lifecycle token (PHASE 1 COMPLETE: or equivalent) carries an explicit `inertia_committed=[yes]` (or equivalent) status field confirming that Phase 1 produced an inertia commitment. (b) The Phase 4 lifecycle token (PHASE 4 COMPLETE: or equivalent) carries an explicit `inertia_verified=[yes]` (or equivalent) status field confirming that Phase 4 addressed inertia verification. Both status fields must coexist with the token's existing annotation content (N-of-4 counter, phase-boundary declaration, unconditional-emission confirmation) without replacing any required elements. A design where C-14 inertia gates are present but the Phase 1 and Phase 4 tokens carry no inertia status fields satisfies C-14 and C-23 but not C-27. C-14 and C-23 PASS required. Dependency chain: C-14 + C-23 -> C-27.

### C-28 Inertia Status Token Annotation Explicitness
- **Category**: design
- **Weight**: aspirational
- **Source**: V-03 R10 excellence signal
- **Text**: Each of the two lifecycle tokens carrying inertia status fields (Phase 1 and Phase 4) also carries an explicit C-27 compliance annotation, making inertia integration single-grep verifiable from either token independently. C-27 requires the Phase 1 and Phase 4 tokens to carry `inertia_committed=[yes]` and `inertia_verified=[yes]` status fields; C-28 requires those same tokens to explicitly annotate C-27 compliance at each boundary point rather than leaving compliance to be inferred from field presence alone. The canonical V-03 R10 form: Phase 1 annotation declares "C-27 Phase-1 status satisfied -- inertia commitment observable at lifecycle token layer without reading the INERTIA SCENARIO: block"; Phase 4 annotation declares "C-27 PASS: both Phase 1 and Phase 4 lifecycle tokens carry explicit inertia status fields; integration is additive and does not displace N-of-4 counter, C-16, or C-23 content." With explicit annotations, a reviewer reading either boundary token can confirm C-27 compliance without cross-referencing the other token or the dedicated inertia blocks. This is the annotation upgrade to C-27 in the same way C-25 is the annotation upgrade to C-23: the structural fact (tokens carry inertia status fields; four tokens emit) becomes self-declaring at each data point. V-03 R10 demonstrates this as a minimal additive change to a C-27-compliant design; V-01 R10, which carries the same status fields without explicit C-27 compliance annotations, confirms the distinction by passing C-27 but not reaching the explicit-annotation level.
- **Pass condition**: (a) The Phase 1 lifecycle token's annotation explicitly names C-27 compliance at the Phase 1 boundary -- stating that inertia commitment is observable from the lifecycle token layer (e.g., "C-27 Phase-1 status satisfied"). (b) The Phase 4 lifecycle token's annotation explicitly names C-27 compliance, declares that both Phase 1 and Phase 4 status fields are present, and confirms the additive design property -- that no required elements (N-of-4 counter, phase-boundary declaration, unconditional-emission confirmation) were displaced. Each annotation must be sufficient for a reviewer reading that token alone to confirm C-27 compliance at that boundary without reading the other token or the dedicated inertia blocks. A design where Phase 1 and Phase 4 tokens carry `inertia_committed=[yes]` and `inertia_verified=[yes]` but no explicit C-27 compliance annotations satisfies C-27 but not C-28. C-27 PASS required. Dependency chain: C-14 + C-23 -> C-27 -> C-28.

### C-29 Attestation Operationalization with Embedded Verification Instructions
- **Category**: design
- **Weight**: aspirational
- **Source**: V-05 R11 excellence signal
- **Text**: Each of the two C-28 compliance annotations (Phase 1 and Phase 4) is operationalized: the annotation names the specific C-27 sub-clause it satisfies (C-27(a) at Phase 1, C-27(b) at Phase 4), identifies the self-declaring signal field by name (e.g., "the inertia_committed=[yes] field is the self-declaring signal"), and embeds an explicit grep instruction that makes C-27 compliance verification a single deterministic executable step (e.g., "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary"). C-28 makes compliance self-declaring: a reader knows compliance from the annotation. C-29 makes compliance executable: a reader can verify compliance by following an explicit procedural instruction without further interpretation. The parallel is exact: C-29 is to C-28 what C-26 is to C-24 -- the attestation layer gains an embedded verification procedure that makes compliance confirmable by a mechanical step, not just a reading step. V-01 R11 minimal form passes C-28 but does not include sub-clause designation or grep instruction; V-05 R11 synthesis form demonstrates all three additions as a cohesive operationalization pattern.
- **Pass condition**: (a) The Phase 1 lifecycle token's C-28 annotation explicitly names C-27(a) (or equivalent sub-clause label designating the Phase 1 dependency), identifies the specific field that carries the self-declaring signal (e.g., "the inertia_committed=[yes] field is the self-declaring signal"), and includes a grep instruction in the form "Single-grep verifiable: grep for [token name] and read [field name] field to confirm C-27(a) satisfied at this boundary." (b) The Phase 4 lifecycle token's C-28 annotation explicitly names C-27(b) (or equivalent sub-clause label designating the Phase 4 dependency), identifies the specific field that carries the self-declaring signal (e.g., "the inertia_verified=[yes] field is the self-declaring signal"), and includes a corresponding grep instruction. Both annotations must include all three elements: sub-clause identification, self-declaring signal identification, and embedded grep instruction. An annotation that names C-27 without clause designation, or that asserts single-grep verifiability without providing the grep instruction, satisfies C-28 but not C-29. C-28 PASS required. Dependency chain: C-14 + C-23 -> C-27 -> C-28 -> C-29.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-19 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-19 | Added C-11..C-14 from R1 excellence signals (V-04: interrogative obligation, anti-placeholder recovery, empty-tier acknowledgment; V-05: inertia guard on PROCEED) |
| v3 | 2026-03-19 | Added C-15..C-16 from R2 excellence signals (V-05: dual-domain obligation preamble, template-label checkability); aspirational ceiling 30 -> 40, total ceiling 120 -> 130 |
| v4 | 2026-03-19 | Added C-17..C-18 from R3 excellence signals (V-05: contract-to-token binding, multi-criterion token reuse); aspirational ceiling 40 -> 50, total ceiling 130 -> 140 |
| v5 | 2026-03-19 | Added C-19..C-20 from R4 excellence signals (V-03/V-04/V-05: typed token schema block, dual multi-criterion token synthesis); aspirational ceiling 50 -> 60, total ceiling 140 -> 150 |
| v6 | 2026-03-19 | Added C-21 from R5 excellence signal (V-04/V-05: symmetric dual-obligation typed schema contract); aspirational ceiling 60 -> 65, total ceiling 150 -> 155 |
| v7 | 2026-03-19 | Added C-22 from R6 critical experiment (V-04: unconditional phase-boundary lifecycle tokens); C-20 token-agnosticism confirmed and documented; C-21 label-independence confirmed (V-02 R6); aspirational ceiling 65 -> 70, total ceiling 155 -> 160 |
| v8 | 2026-03-19 | Added C-23..C-24 from R7 excellence signals (V-03: full-phase lifecycle instrumentation; V-05: redundant dual-path multi-criterion infrastructure); C-22 token-agnosticism confirmed (V-02 R7); C-22 inertia-axis orthogonality confirmed (V-04 R7); aspirational ceiling 70 -> 80, total ceiling 160 -> 170 |
| v9 | 2026-03-19 | Added C-25..C-26 from R8 excellence signals (V-04: N-of-4 progressive counter annotation; V-04/V-05: named independence verification block); C-23 annotation requirement confirmed (V-02/V-03 R8: unannotated tokens fail C-23); C-24 prose-annotation failure confirmed (V-01 R8: explicit "C-NN PASS" required for C-20 pass condition (c)); aspirational ceiling 80 -> 90, total ceiling 170 -> 180 |
| v10 | 2026-03-19 | Added C-27 from R9 excellence signal (V-05: inertia status lifecycle integration -- Phase 1 and Phase 4 lifecycle tokens carry explicit inertia commitment/verification status fields); C-26 heading-agnosticism confirmed (V-03 R9: "Dual-Path Redundancy Proof" satisfies C-26 identically to "C-24 Independence Verification"; only structural elements (a)-(d) are binding; completes the agnosticism meta-pattern: C-22 token-agnostic R7, C-21 label-independent R6, C-26 heading-agnostic R9); aspirational ceiling 90 -> 95, total ceiling 180 -> 185 |
| v11 | 2026-03-19 | Added C-28 from R10 excellence signal (V-03: inertia status token annotation explicitness -- Phase 1 and Phase 4 lifecycle tokens carry explicit C-27 compliance annotations making inertia integration single-grep verifiable from either token independently; stronger than V-01 R10's implicit structural satisfaction); C-27 "or equivalent" interpretation confirmed (V-02 R10: "or equivalent" protects structural equivalence not semantic approximation; `inertia_named=[yes]` fails C-27(b) as it names a weaker sub-act rather than confirming the verification act was performed); C-27 Phase 1 dependency confirmed absolute (V-04 R10: `inertia_committed=[no]` blocks C-27 even when C-14 PASSes; Phase-4-only C-14 does not satisfy C-27's Phase 1 front-loading requirement); aspirational ceiling 95 -> 100, total ceiling 185 -> 190 |
| v12 | 2026-03-19 | Added C-29 from R11 excellence signal (V-05: attestation operationalization -- each C-28 annotation names the specific C-27 sub-clause (C-27(a)/C-27(b)), identifies the self-declaring signal field, and embeds a grep instruction making C-27 compliance verification a single deterministic executable step; C-28 makes compliance self-declaring; C-29 makes compliance executable); V-04 R11 label-only failure confirmed (bare "C-28 PASS." without independence prose fails C-28; annotation depth matters -- must articulate the observability claim and independence property); V-02 R11 Phase-1-only failure and V-03 R11 Phase-4-only failure confirmed symmetrically (C-28 requires both boundary annotations independently; one token is insufficient; both-or-nothing property confirmed); aspirational ceiling 100 -> 105, total ceiling 190 -> 195 |

---

## Key Decisions

- **C-17 depends on C-15** -- contract-to-token binding is only meaningful if a C-15 enforcement contract exists. If C-15 is FAIL or PARTIAL, C-17 cannot PASS.
- **C-19 depends on C-17** -- typed schema is a precision upgrade to contract-to-token binding, not an independent mechanism. The dependency chain is C-15 -> C-17 -> C-19: contract exists, contract names tokens, contract declares token schemas with authoritative field names. C-17 FAIL/PARTIAL blocks C-19.
- **C-21 depends on C-19** -- symmetric dual-schema requires the single typed schema block to already exist. The dependency chain extends to C-15 -> C-17 -> C-19 -> C-21. C-19 FAIL blocks C-21.
- **C-21 is independent of C-20** -- dual typed schemas do not satisfy dual multi-criterion token declaration, and explicit PASS annotations do not satisfy typed schema coverage. V-04 R5 PASS on C-21 + FAIL on C-20 and V-03 R5 PASS on C-20 + FAIL on C-21 confirm orthogonality. V-05 R5 achieves both.
- **C-21 is structure-dependent, not label-dependent** -- renaming OBLIGATION A/B to RULE 1/2 or any other naming scheme does not affect C-21. The schema block structure (Token/Schema/Fields/Required when/Unacceptable) and verbatim field name propagation from Fields: to the producing phase are what C-21 measures. V-02 R6 confirms this.
- **C-22 depends on C-18** -- unconditional lifecycle tokens are a refinement of multi-criterion token design. A token that fires unconditionally but covers only one criterion is normal C-16 scope. C-22 requires the lifecycle token to also satisfy multi-criterion coverage (C-18). If C-18 is FAIL, C-22 cannot PASS. Dependency chain: C-16 -> C-18 -> C-22.
- **C-22 is independent of C-21** -- unconditional emission is an observability property; symmetric dual-schema is a precision property. A variation can add lifecycle tokens (C-22 PASS) without dual schemas (C-21 FAIL), and vice versa.
- **C-22 is token-agnostic** -- domain-named tokens (EVIDENCE PHASE COMPLETE:, MAP PHASE COMPLETE:) qualify identically to PHASE N COMPLETE: names. The pass condition names no specific vocabulary; what matters is unconditional boundary emission and explicit annotation. V-02 R7 confirms.
- **C-22 is orthogonal to the inertia front-loading axis** -- pre-committed Phase 1 inertia (C-14 front-loaded) does not affect unconditional lifecycle token emission at Phase 2/3 boundaries. The axes combine cleanly. V-04 R7 confirms.
- **C-23 depends on C-22** -- full-phase instrumentation presupposes the minimum-two-token design. C-22 FAIL blocks C-23. A run with two unconditional tokens satisfies C-22 but not C-23; the additional Phase 1 and Phase 4 tokens are required for C-23.
- **C-23 does not mandate specific phase-naming** -- as with C-22, C-23 is token-agnostic: domain-named tokens qualify as long as each names its specific phase boundary and confirms unconditional emission. The four-token count is the binding requirement, not token vocabulary.
- **C-23 annotation requirement is strict** -- a lifecycle token with no annotation paragraph does not satisfy C-23 even if it emits at a phase boundary. Each token must explicitly state its phase boundary and confirm unconditional emission. Two annotated tokens satisfies C-22; four annotated tokens required for C-23. V-02/V-03 R8 confirm: bare token lines for Phase 1 and Phase 4 cause C-23 FAIL.
- **C-24 depends on C-20** -- redundant dual-path synthesis presupposes the single-pair design. C-20 FAIL blocks C-24. C-24 adds a count floor (two distinct pairs) and an independence requirement (each pair must satisfy C-20 alone) that a single-pair design cannot meet.
- **C-24 independence requirement is strict** -- if the two pairs together cover exactly three distinct criteria (with no independent overlap), removing one pair may leave only one criterion for the remaining pair, failing C-20's three-criteria minimum. The pairs must be independently sufficient: each covers three distinct criteria on its own.
- **C-24 requires explicit PASS annotations** -- C-20 pass condition (c) requires annotations that "confirm all listed criteria PASS." Prose describing what a token does (e.g., "records the threshold shortfall for auditing") without explicit "C-09 PASS, C-16 PASS" language does not satisfy condition (c). V-01 R8 confirms: canonical pair with prose annotation fails C-20; one C-20-satisfying pair satisfies C-20 but not C-24.
- **C-20 is token-agnostic** -- the C-20 pass condition does not require any specific tokens. The canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair from R4 V-05 is a valid instance, not the only instance. V-04 R6 confirms that PHASE 2 COMPLETE:/PHASE 3 COMPLETE: is an independent valid path.
- **C-25 depends on C-23** -- the N-of-4 progressive counter is a scannability upgrade to the complete-instrumentation design. A run with fewer than four lifecycle tokens cannot satisfy N-of-4 counting. C-23 FAIL blocks C-25.
- **C-25 is independent of C-26** -- N-of-4 counting addresses per-token scannability; the named verification block addresses whole-infrastructure declaration. A design can add N-of-4 counters (C-25 PASS) without a verification block (C-26 FAIL), and vice versa. Both V-04 R8 and V-05 R8 achieve both, confirming their orthogonality.
- **C-26 depends on C-24** -- the named independence verification block is a declaration upgrade to the dual-path design. A run with only one C-20-satisfying pair cannot run the remove-either-pair test meaningfully. C-24 FAIL blocks C-26.
- **C-26 declaration requirement is strict** -- inferrable C-24 compliance from scattered annotations does not satisfy C-26. The named block must be present as a distinct structural element, run the remove-either-pair test verbatim, and declare C-24 PASS explicitly. Absence of the block is C-26 FAIL regardless of annotation quality elsewhere.
- **C-26 is heading-agnostic** -- any named heading or labeled section satisfies C-26 provided all four structural elements (a)-(d) are present. "Dual-Path Redundancy Proof" satisfies C-26 identically to "C-24 Independence Verification". The "e.g." in the pass condition heading is genuine: only the structural elements, not the label, are binding. V-03 R9 confirms. This completes the agnosticism meta-pattern: C-22 token-agnostic (R7), C-21 label-independent (R6), C-26 heading-agnostic (R9).
- **C-27 depends on C-14 and C-23** -- inertia status lifecycle integration requires both the inertia guard (C-14) and full-phase lifecycle instrumentation (C-23) to be in place. C-14 establishes what inertia commitment and verification mean; C-23 establishes the Phase 1 and Phase 4 tokens where the status fields are added. Either dependency failing blocks C-27.
- **C-27 is additive, not displacing** -- adding `inertia_committed=[yes]` to PHASE 1 COMPLETE: and `inertia_verified=[yes]` to PHASE 4 COMPLETE: does not affect any prior criterion. The status fields coexist with the N-of-4 counter annotation, phase-boundary declaration, and all other required content. V-05 R9 confirms no criteria conflict.
- **C-27 is independent of C-25 and C-26** -- inertia status fields are orthogonal to the N-of-4 counter (C-25) and to the independence verification block (C-26). A design can add inertia status fields (C-27 PASS) without a progressive counter (C-25 FAIL), and vice versa. The axes intersect without coupling.
- **C-27 "or equivalent" is structural equivalence, not semantic approximation** -- the "or equivalent" clause in C-27(b) protects a different token emitting the same information (structural equivalence), not a field name that describes a weaker sub-act of verification. `inertia_named=[yes]` fails C-27(b): it confirms the scenario was named, not that the verification act was performed. V-01 R10's sole change from R9 V-05 is this rename; if `inertia_named` already satisfied C-27(b) as equivalent, V-01 would be unnecessary -- the variation's own design logic confirms the distinction. V-02 R10 confirms.
- **C-27 Phase 1 dependency is absolute** -- `inertia_committed=[no]` in the Phase 1 lifecycle token blocks C-27 even when C-14 PASSes in Phase 4. C-27 depends on Phase 1 inertia front-loading specifically, not merely on C-14 existing in any form. A Phase-4-only C-14 design satisfies C-14 but cannot produce `inertia_committed=[yes]` in Phase 1, leaving C-27(a) unmet. V-04 R10 confirms: the isolation experiment succeeds -- C-14 PASS does not rescue C-27.
- **C-28 depends on C-27** -- inertia status token annotation explicitness presupposes the inertia status fields are present. C-27 FAIL blocks C-28. C-28 adds the annotation layer that makes C-27 compliance self-declaring at each token boundary rather than inferred from field presence.
- **C-28 is the annotation upgrade to C-27, parallel to C-25 as the annotation upgrade to C-23** -- just as C-25 adds N-of-4 counter annotations to the four tokens required by C-23 (making completeness verifiable from any single token), C-28 adds C-27 compliance annotations to the two tokens required by C-27 (making inertia integration verifiable from either token independently). The structural fact becomes self-declaring at each data point.
- **C-28 annotation sufficiency standard** -- each annotation must be independently sufficient: a reviewer reading the Phase 1 token alone must be able to confirm C-27 Phase-1 compliance; a reviewer reading the Phase 4 token alone must be able to confirm C-27 PASS including the additive design property. Annotations that confirm only field presence without naming C-27 compliance do not satisfy C-28.
- **C-28 annotation depth matters** -- bare label ("C-28 PASS.") without independence prose fails C-28. The pass condition requires articulating the observability claim: the annotation must state that inertia commitment is verifiable from this token alone without cross-referencing the other token. V-04 R11 confirms: "C-28 PASS." does not meet C-28(a) or C-28(b).
- **C-28 requires both boundary annotations independently** -- a Phase-1-only C-28 annotation (V-02 R11) and a Phase-4-only C-28 annotation (V-03 R11) each fail C-28 symmetrically. Both boundaries must carry independent attestations. The two failures together confirm there is no asymmetric design path: C-28 is a both-or-nothing criterion.
- **C-29 depends on C-28** -- attestation operationalization presupposes the attestation annotations are present. C-28 FAIL blocks C-29. C-29 adds sub-clause identification, self-declaring signal identification, and embedded grep instructions to the C-28 annotation layer -- making compliance not just self-declaring but procedurally executable.
- **C-29 is the operationalization upgrade to C-28, parallel to C-26 as the declaration upgrade to C-24** -- just as C-26 adds a named verification block to the C-24 dual-path infrastructure (making compliance confirmable in a single grep target), C-29 adds embedded grep instructions to the C-28 attestation annotations (making compliance confirmable in a single executable step). The structural pattern: fact (C-27/C-24) -> self-declaring annotation (C-28/C-25) -> executable verification (C-29/C-26).
- **C-29 requires all three elements at both boundaries** -- sub-clause designation alone (without grep instruction) satisfies C-28 at higher fidelity but not C-29. Self-declaring signal identification alone does not satisfy C-29. The grep instruction is the operationalization act; the sub-clause designation and signal identification are required context for the grep instruction to be interpretable. All three elements must appear in both the Phase 1 and Phase 4 annotations.
- **C-18 requires naming both criteria** -- a token that happens to be grep-verifiable is already C-16 coverage. C-18 triggers only when a token is explicitly designed to satisfy an additional criterion. The pass condition requires identifying the token and both criteria it covers.
- **C-20 depends on C-18** -- dual-instance synthesis presupposes the single-instance pattern. C-18 FAIL blocks C-20. C-20 adds a coverage floor (three distinct criteria total) and a count floor (two distinct tokens) that a single-instance design cannot meet.
- **Eleven-axis aspiration progression**: C-19 (precision: one obligation schema-typed), C-20 (scale: two tokens each multi-criterion, declared), C-21 (symmetry: both obligations schema-typed), C-22 (observability: tokens fire unconditionally at boundaries), C-23 (completeness: all four phase gates instrumented), C-24 (redundancy: two independent C-20-satisfying paths coexist), C-25 (scannability: N-of-4 counter makes completeness verifiable from any single token), C-26 (declaration: independence verification block makes redundancy compliance explicit not inferred), C-27 (integration: inertia commitment visible in lifecycle tokens, not only in dedicated inertia blocks), C-28 (attestation: inertia integration compliance explicitly annotated at each token boundary -- not inferred from field presence), C-29 (operationalization: attestation compliance executable via embedded grep instruction at each boundary -- not just self-declared but procedurally verifiable in one deterministic step). Each addresses a distinct enforcement, observability, or verifiability gap.
- **Ceiling trajectory**: v1: 120 -> v2: 125 -> v3: 130 -> v4: 140 -> v5: 150 -> v6: 155 -> v7: 160 -> v8: 170 -> v9: 180 -> v10: 185 -> v11: 190 -> v12: 195. Each increment captures patterns that were achievable but not rewarded under the prior ceiling.
