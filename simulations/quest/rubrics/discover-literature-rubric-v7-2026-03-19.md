Done. v7 rubric written to `simulations/quest/rubrics/discover-literature-rubric-v7-2026-03-19.md`.

---

**One new criterion: C-22 Unconditional Phase-Boundary Lifecycle Tokens**

| Axis | What it captures |
|------|-----------------|
| Source | V-04 R6 critical experiment |
| Gap it closes | THRESHOLD NOT MET: fires only on failure; a passing run produces no grep-verifiable compliance signal. C-22 rewards tokens that emit at the phase boundary unconditionally, making compliance checkable in every run outcome -- not just when something goes wrong |
| Pass condition | At least two named tokens emit unconditionally at phase boundaries (present in both threshold-met and threshold-not-met runs); each token's annotation names the phase boundary; C-18 PASS required |
| Independence | C-22 is orthogonal to C-21 -- V-04 R6 PASS on C-22, and a variation could add lifecycle tokens without dual schemas |
| Dependency | C-16 -> C-18 -> C-22 |

**Two additional key-decisions updates (no new criteria -- confirmations):**

- **C-20 token-agnosticism** -- explicitly documented in C-20 text and key decisions. THRESHOLD NOT MET:/RECOVERY NOTE: is a valid instance, not the required pair. V-04 R6 confirms PHASE 2 COMPLETE:/PHASE 3 COMPLETE: as an independent valid path.
- **C-21 label-independence** -- V-02 R6 confirms that RULE 1/RULE 2 naming is structurally equivalent to OBLIGATION A/B. Documented in C-21 text and key decisions.

**Scoring delta:**

| | v6 | v7 |
|--|----|----|
| Aspirational criteria | 13 | 14 |
| Aspirational ceiling | 65 pts | 70 pts |
| Total ceiling | 155 | 160 |

**Four-axis aspiration progression:**
- C-19: precision (one obligation schema-typed, closes slot-label mismatch)
- C-20: scale (two tokens each multi-criterion, declared)
- C-21: symmetry (both obligations schema-typed)
- C-22: observability (tokens fire unconditionally at boundaries, not just on failure)

**Ceiling trajectory**: v1: 120 → v2: 125 → v3: 130 → v4: 140 → v5: 150 → v6: 155 → v7: 160
es a PROCEED / SEARCH MORE / REFRAME CLAIM recommendation.
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

## ASPIRATIONAL Criteria (70 points -- raise the bar once essential/recommended are stable)

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
- **Source**: V-05 R4 excellence signal; token-agnosticism confirmed V-04 R6
- **Text**: Two or more distinct named output tokens each satisfy multiple criteria simultaneously, each carrying an explicit annotation paragraph naming the covered criteria. Together the annotated tokens cover at least three distinct aspirational criteria. This extends C-18 from a single instance to a coordinated multi-token infrastructure -- the output design is holistic, not opportunistic. The canonical R4 instance: `THRESHOLD NOT MET:` annotated as covering C-09 + C-16, and `RECOVERY NOTE:` annotated as covering C-12 + C-16 -- two tokens, four named criterion-coverages, three distinct criteria (C-09, C-12, C-16). Token reuse of a previously covered criterion (C-16 appears in both annotations) is permitted; what must be distinct is the additional criterion each token introduces beyond the shared one. C-20 is token-agnostic: any two named tokens carrying explicit condition-(c) PASS annotations covering three distinct aspirational criteria qualify. The canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair is not required. V-04 R6 demonstrates that PHASE 2 COMPLETE:/PHASE 3 COMPLETE: is an independent valid path.
- **Pass condition**: At least two distinct named tokens each carry an annotation paragraph that (a) names the token, (b) lists two or more distinct criteria it covers, and (c) confirms all listed criteria PASS. The two tokens together must name at least three distinct aspirational criteria. A single token with two annotations does not satisfy this criterion -- two distinct tokens are required. If C-18 is FAIL, this criterion cannot PASS.

### C-21 Symmetric Dual-Obligation Typed Schema Contract
- **Category**: behavior
- **Weight**: aspirational
- **Source**: V-04/V-05 R5 excellence signal; label-independence confirmed V-02 R6
- **Text**: Both named obligations in the enforcement contract declare independent typed schema blocks. C-19 requires at least one obligation to use a typed schema block; C-21 requires both OBLIGATION A (the anti-placeholder recovery token, e.g., `RECOVERY NOTE:`) and OBLIGATION B (the empty-tier acknowledgment token, e.g., `TIER EMPTY:`) to use the Token/Schema/Fields/Required when/Unacceptable format with authoritative Fields: variable names. The variable names in each obligation's typed schema appear verbatim in the phase that produces that obligation's output. A contract where one obligation is schema-typed and the other is prose-specified creates an asymmetric enforcement surface: the prose obligation permits slot-label abbreviation in output; the schema obligation does not. V-04 R5 demonstrates that dual typed schemas constitute a valid design upgrade independent of the C-20 declaration axis -- C-21 PASS requires dual schemas, not explicit PASS annotations. V-05 R5 achieves both axes simultaneously, confirming their orthogonality. C-21 is structure-dependent, not label-dependent: renaming OBLIGATION A/B to RULE 1/2 or any other labels does not affect the verdict; the schema block structure and verbatim field name propagation are what C-21 measures, confirmed by V-02 R6.
- **Pass condition**: Both the recovery-obligation token (OBLIGATION A) and the empty-tier-acknowledgment token (OBLIGATION B) declare independent typed schema blocks containing Token, Schema, Fields, Required when, and Unacceptable lines. The Fields: variable names for OBLIGATION A appear verbatim in the phase that produces RECOVERY NOTE: output (typically Phase 2 or Phase 3); the Fields: variable names for OBLIGATION B appear verbatim in the phase that produces TIER EMPTY: output (typically Phase 3 tier instructions). A contract with exactly one typed schema block satisfies C-19 but not C-21. If C-19 is FAIL, this criterion cannot PASS. Dependency chain: C-15 -> C-17 -> C-19 -> C-21.

### C-22 Unconditional Phase-Boundary Lifecycle Tokens
- **Category**: design
- **Weight**: aspirational
- **Source**: V-04 R6 critical experiment
- **Text**: Phase-boundary tokens emit unconditionally at the completion of each phase, regardless of whether the success path or the failure path was taken. The canonical failure-path token `THRESHOLD NOT MET:` instruments only the exceptional case: a run that meets its threshold produces no grep-verifiable compliance signal for C-09. A lifecycle completion token such as `PHASE 2 COMPLETE:` fires at the phase boundary unconditionally, making threshold compliance checkable in the happy path as well as the failure path. A design that instruments only failure paths creates an observability gap: the absence of a failure token is not the same as confirmed success. A design with unconditional phase-boundary tokens makes compliance verifiable in every run outcome. V-04 R6 demonstrates that PHASE 2 COMPLETE: and PHASE 3 COMPLETE: each fire at the boundary unconditionally and each independently satisfy C-20's multi-criterion annotation requirement (PHASE 2 COMPLETE: covers C-09 + C-16; PHASE 3 COMPLETE: covers C-13 + C-16), confirming that superior observability and multi-criterion coverage are independently achievable in a single lifecycle token design. This criterion is independent of C-21: unconditional emission is an observability property; dual schema blocks are a precision property.
- **Pass condition**: At least two named tokens emit at phase boundaries unconditionally -- i.e., they fire regardless of whether the phase threshold was met or not. Each token must be present in successful runs (threshold met) as well as in failure runs (threshold not met). A token that fires only when a condition fails (e.g., `THRESHOLD NOT MET:`) does not satisfy this criterion -- it must emit unconditionally. Each token's annotation must indicate the phase boundary at which it emits. If C-18 is FAIL, this criterion cannot PASS (lifecycle tokens are a refinement of the multi-criterion token design pattern; unconditional emission without multi-criterion coverage is normal C-16 scope). Dependency chain: C-16 -> C-18 -> C-22.

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

---

## Key Decisions

- **C-17 depends on C-15** -- contract-to-token binding is only meaningful if a C-15 enforcement contract exists. If C-15 is FAIL or PARTIAL, C-17 cannot PASS.
- **C-19 depends on C-17** -- typed schema is a precision upgrade to contract-to-token binding, not an independent mechanism. The dependency chain is C-15 -> C-17 -> C-19: contract exists, contract names tokens, contract declares token schemas with authoritative field names. C-17 FAIL/PARTIAL blocks C-19.
- **C-21 depends on C-19** -- symmetric dual-schema requires the single typed schema block to already exist. The dependency chain extends to C-15 -> C-17 -> C-19 -> C-21. C-19 FAIL blocks C-21.
- **C-21 is independent of C-20** -- dual typed schemas do not satisfy dual multi-criterion token declaration, and explicit PASS annotations do not satisfy typed schema coverage. V-04 R5 PASS on C-21 + FAIL on C-20 and V-03 R5 PASS on C-20 + FAIL on C-21 confirm orthogonality. V-05 R5 achieves both.
- **C-21 is structure-dependent, not label-dependent** -- renaming OBLIGATION A/B to RULE 1/2 or any other naming scheme does not affect C-21. The schema block structure (Token/Schema/Fields/Required when/Unacceptable) and verbatim field name propagation from Fields: to the producing phase are what C-21 measures. V-02 R6 confirms this.
- **C-22 depends on C-18** -- unconditional lifecycle tokens are a refinement of multi-criterion token design. A token that fires unconditionally but covers only one criterion is normal C-16 scope. C-22 requires the lifecycle token to also satisfy multi-criterion coverage (C-18). If C-18 is FAIL, C-22 cannot PASS. Dependency chain: C-16 -> C-18 -> C-22.
- **C-22 is independent of C-21** -- unconditional emission is an observability property; symmetric dual-schema is a precision property. A variation can add lifecycle tokens (C-22 PASS) without dual schemas (C-21 FAIL), and vice versa. V-04 R6 PASS on C-22 + all-essential PASS confirms the combination is achievable.
- **C-20 is token-agnostic** -- the C-20 pass condition does not require any specific tokens. The canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair from R4 V-05 is a valid instance, not the only instance. V-04 R6 confirms that PHASE 2 COMPLETE:/PHASE 3 COMPLETE: is an independent valid path: any two named tokens each carrying explicit condition-(c) PASS annotations covering three distinct aspirational criteria qualify. What matters is the annotation structure, not the token names.
- **C-18 requires naming both criteria** -- a token that happens to be grep-verifiable is already C-16 coverage. C-18 triggers only when a token is explicitly designed to satisfy an additional criterion. The pass condition requires identifying the token and both criteria it covers.
- **C-20 depends on C-18** -- dual-instance synthesis presupposes the single-instance pattern. C-18 FAIL blocks C-20. C-20 adds a coverage floor (three distinct criteria total) and a count floor (two distinct tokens) that a single-instance design cannot meet.
- **Precision vs. scale vs. symmetry vs. observability** -- C-19 closes the slot-label mismatch for one obligation (precision); C-20 raises the multi-criterion bar from one token to two (scale); C-21 extends schema precision to both obligations (symmetry); C-22 closes the happy-path observability gap by requiring unconditional emission at phase boundaries (observability). Each addresses a distinct enforcement gap.
- **Ceiling trajectory**: v1: 120 -> v2: 125 -> v3: 130 -> v4: 140 -> v5: 150 -> v6: 155 -> v7: 160. Each increment captures patterns that were achievable but not rewarded under the prior ceiling.
