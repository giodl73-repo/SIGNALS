Reading the R7 scorecard carefully to extract new excellence patterns before writing the rubric.

The R7 evidence notes surface three distinct patterns not yet captured by C-21/C-22/C-23:

1. **C-12 fix**: The scaffold now requires `NAMED CLAIM: "[exact text]"` — not just "anchor to a named claim" (C-12) but *quote the exact text* of the claim being rebutted. Paraphrase fails.
2. **C-22 V-02**: `[PAIR REQUIRED]` annotations at each individual site — not just a global statement that pairs are required, but every site individually marked so an unannotated site is a structural error.
3. **C-21 V-01/V-02**: "section headers match exactly" — the manifest text and header text must be verbatim identical, not just both present (C-23).

These become C-24, C-25, C-26. Denominator: 15 → 18.

---

# scout-inertia Rubric — v8

**Changes from v7 to v8:**

Three new aspirational criteria extracted from R7 excellence signals.

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-24 | **Exact-Text Quotation at Claim-Reference Steps** | V-01/V-02 C-12 fix required adding `NAMED CLAIM: "[exact text]"` as a structural label at the rebuttal step — not just naming the claim (C-12) but reproducing it verbatim. The R7 gap that remained in R6 was that an anchored rebuttal could still paraphrase the steelman and subtly shift what was being rebutted. Exact-text quotation closes that gap: the model cannot rephrase the claim it is rebutting. |
| C-25 | **Enforcement Annotations at Every Structural-Requirement Site** | V-02's `[PAIR REQUIRED]` pattern: each individual site in the scaffold where a structural requirement applies carries an inline annotation. A global rule ("pairs are required") allows the model to miss individual sites; per-site annotation makes every omission locally detectable. An unannotated site is a structural error independent of global rule compliance. |
| C-26 | **Manifest-to-Header Verbatim Alignment** | V-01/V-02 fix required that "section headers match exactly" — C-23 requires sub-protocol names appear in both manifest and section header; C-26 requires those texts be character-for-character identical. A name that is paraphrased between sites satisfies C-23 but introduces ambiguity about whether the manifest entry and the section header refer to the same protocol. Verbatim alignment eliminates that ambiguity: both verification paths resolve to identical text. |

**Formula:** `aspirational_pass / 18 * 10` (denominator 15 → 18)

**C-24/C-25/C-26 relationships:**
- C-24 upgrades C-12: C-12 requires the rebuttal be anchored to a named claim; C-24 requires the exact text of that claim to be quoted at the anchor point. An output can pass C-12 by referencing "the cost objection" and fail C-24 because it paraphrases rather than quotes. The distinction matters: paraphrase allows the model to shift the claim being rebutted; exact quotation does not.
- C-25 upgrades C-22: C-22 requires maximum density — every requirement with a failure condition receives a pass/fail pair; C-25 requires each such site to carry an explicit `[PAIR REQUIRED]`-style annotation, making the obligation locally visible. An output can satisfy C-22 by having pairs everywhere and fail C-25 because the pairs are present without structural markers forcing them. The difference is detectability: C-22 violation requires reading all sites; C-25 violation is detectable by scanning for unannotated sites.
- C-26 upgrades C-23: C-23 requires sub-protocol names appear at both manifest and section header (double-declaration); C-26 requires those names to be textually identical. An output can pass C-23 with "Anchored Rebuttal Protocol" in the manifest and "Rebuttal with Anchoring" in the header and fail C-26. Verbatim alignment means neither site can diverge without creating a falsifiable contradiction.

**Evaluator Notes additions (v8):**
- C-24 and the paraphrase failure mode: the danger of paraphrase at a claim-reference step is that the model can strengthen or weaken the steelman while appearing to engage it. "The claim that switching costs are high" is not the same as `NAMED CLAIM: "Migration requires rebuilding all existing pipeline configurations from scratch"`. Only exact quotation pins the rebuttal to the actual claim made.
- C-25 and the audit path: `[PAIR REQUIRED]` annotations create an audit path independent of reading the full output. A reviewer can scan for annotation-site count, count actual pairs, and detect any mismatch without exhaustive content review. This is structurally stronger than C-22's density requirement, which requires reading every requirement site to confirm coverage.
- C-26 and dual-path verification precision: C-23 established that two independent verification paths exist (manifest and header). C-26 ensures both paths resolve to the same string. When they diverge — even slightly — a reviewer must decide which site is authoritative. Verbatim alignment removes that judgment call: the manifest is always authoritative, and any header that diverges is a defect.

---

## Essential Criteria (60 pts total — all must pass)

### C-01 · Current Workaround Mapped
- **Weight**: essential
- **Category**: coverage
- **Text**: The output describes in concrete detail what teams currently do instead of adopting the feature — the actual workflow, tools, manual steps, or conventions they rely on today.
- **Pass condition**: At least one specific workaround is named and described with enough detail that a reader can picture the workflow. Generic statements like "teams use manual processes" without specifics do not pass.

### C-02 · Switching Costs Quantified
- **Weight**: essential
- **Category**: correctness
- **Text**: Switching costs are estimated across at least two of the three required dimensions (time, training, disruption). Estimates must be numeric or range-based — not adjective-only descriptions like "significant" or "moderate."
- **Pass condition**: The output provides at least two quantified cost estimates (e.g., "2-4 hours of migration per project", "1-2 days of team onboarding") or explicit N/A with justification for any omitted dimension.

### C-03 · Inertia Threat Score Set to HIGH
- **Weight**: essential
- **Category**: correctness
- **Text**: The output explicitly assigns an inertia threat score and that score is HIGH (or equivalent — "critical", "severe"). Per skill spec, this is always HIGH by default. Any output that omits this score or sets it below HIGH without a documented exception fails.
- **Pass condition**: A threat score of HIGH appears explicitly in the output. Downgrading below HIGH requires a written justification; absence of score is an automatic fail.

### C-04 · "Why Inertia Loses" Answered
- **Weight**: essential
- **Category**: depth
- **Text**: The output identifies specific conditions under which the inertia option loses — the precise scenarios, thresholds, or events that make the current workaround worse than adopting the feature. This is the core deliverable of the skill.
- **Pass condition**: At least two distinct, concrete conditions are named (not restated feature benefits). Each condition must be falsifiable — a reader could check whether it applies to their situation.

### C-05 · Workaround Failure Modes Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: Per the AMEND directive, the output identifies specific ways the current workaround breaks down — edge cases, scaling limits, error-prone steps, or known failure scenarios. These are distinct from switching costs (costs are about moving; failure modes are about staying).
- **Pass condition**: At least two specific failure modes of the current workaround are described. "The workaround has limitations" does not pass. "The workaround silently drops events when queue depth exceeds 500" does pass.

---

## Recommended Criteria (30 pts total)

### C-06 · Switching Cost Dimensions Treated Separately
- **Weight**: recommended
- **Category**: depth
- **Text**: Time, training, and disruption are analyzed as separate line items rather than collapsed into a single "switching cost" number. Each dimension may affect different stakeholders (developer time vs. manager training budget vs. team coordination disruption).
- **Pass condition**: The output has three distinct cost entries — one per dimension — or explicitly explains why a dimension does not apply for this feature context.

### C-07 · Inertia-Loss Conditions Are Threshold-Based
- **Weight**: recommended
- **Category**: depth
- **Text**: Conditions under which inertia loses are framed as observable thresholds or triggers — not general preferences. "Teams with more than 3 concurrent projects" or "when onboarding frequency exceeds monthly" are thresholds. "When teams are frustrated" is not.
- **Pass condition**: At least one inertia-loss condition uses a measurable or observable threshold that a team could evaluate against their actual situation.

### C-08 · Long-Term Risk of Staying on Workaround
- **Weight**: recommended
- **Category**: depth
- **Text**: The output projects what happens to teams that do not adopt — compounding technical debt, increasing fragility, forced migration under worse conditions, or lock-in. The projection includes a time horizon (months/years) or a threshold event that triggers the risk.
- **Pass condition**: A specific long-term risk is described with either a time horizon or a threshold event. "The workaround will become harder to maintain" without a timeframe or trigger does not pass. "By month 6, manual reconciliation steps will exceed 8 hours/week as event volume scales" does pass.

---

## Aspirational Criteria (10 pts total, formula: aspirational_pass / 18 * 10)

### C-09 · Failure Modes Ranked by Severity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each failure mode of the current workaround is labeled by severity (critical, high, medium) or ranked relative to the others. Severity distinguishes a minor inconvenience from a data-loss or availability failure.
- **Pass condition**: At least two failure modes carry distinct severity labels or are explicitly ranked, with a brief rationale for the highest-severity designation.

### C-10 · Steelman of Inertia Presented
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output presents the strongest genuine case for staying on the current workaround before rebutting it. The steelman must be a real argument — not a strawman or a restated feature benefit in reverse.
- **Pass condition**: A steelman argument is identified that a skeptical team lead would actually make. A steelman that says "the workaround is free" when the workaround has documented hidden costs does not pass.

### C-11 · Verification Method Specified
- **Weight**: aspirational
- **Category**: actionability
- **Text**: The output specifies how a team can verify whether the inertia-loss conditions or failure modes apply to their situation — a concrete check, metric to measure, or diagnostic step they can execute.
- **Pass condition**: At least one verification method is named that is immediately actionable — a team could execute it without further research (e.g., "run `pipeline status --verbose` and check for queue-depth warnings").

### C-12 · Rebuttal Anchored to Named Claim
- **Weight**: aspirational
- **Category**: depth
- **Text**: The rebuttal step explicitly names the specific steelman claim it is rebutting. The reference is to the named claim text, not a category ("the cost objection") or an implicit reference.
- **Pass condition**: The rebuttal identifies a specific claim by name or quoted text and addresses that claim's strongest point directly. A rebuttal that argues against a general category without naming the claim does not pass.

### C-13 · Replication Fidelity Standard Named
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output specifies what aspects of the existing workaround must be replicated with full fidelity during migration, what can be approximated, and what is explicitly out of scope. The standard is named and scoped — not implicit.
- **Pass condition**: A replication fidelity expectation appears by name (e.g., "Replication Fidelity Standard") and specifies at minimum which workaround behaviors must be preserved exactly versus approximately.

### C-14 · Labeled Analytical Sections
- **Weight**: aspirational
- **Category**: structure
- **Text**: Each major analytical section carries a label that names its analytical function — not just the topic. "Switching Cost Profile" is a function label. "Costs" is not.
- **Pass condition**: All major sections have function-descriptive labels. A section labeled "Analysis" or by topic alone does not pass.

### C-15 · Trigger/Impact Decomposed per Failure Mode
- **Weight**: aspirational
- **Category**: depth
- **Text**: For each failure mode, the triggering condition is analyzed separately from its impact. "What causes it to fire" is distinct from "what happens when it fires." This decomposition enables teams to assess both exposure (trigger frequency) and consequence (impact severity) independently.
- **Pass condition**: At least two failure modes have separate trigger and impact entries — either in dedicated table columns or in labeled sub-items within the failure mode description.

### C-16 · Dedicated Table Columns per Data Type
- **Weight**: aspirational
- **Category**: structure
- **Text**: Tables use dedicated columns for each type of information rather than combining multiple dimensions in a single cell. A switching cost table has separate columns for dimension, estimate, and stakeholder — not a single "notes" column that conflates them.
- **Pass condition**: Every table uses dedicated columns per data type. A table with combined columns (e.g., "Cost and Stakeholder" merged into one cell) does not pass.

### C-17 · Section Heading Manifest
- **Weight**: aspirational
- **Category**: structure
- **Text**: The output includes a heading manifest — a pre-declaration of all section headings appearing before the sections themselves. The manifest serves as a structural contract: any section present in the output must appear in the manifest, and any section in the manifest must appear in the output.
- **Pass condition**: A manifest listing all section headings appears at the document level, before the first section body. The manifest entries must match the actual headings used.

### C-18 · Per-Table Column Manifest
- **Weight**: aspirational
- **Category**: structure
- **Text**: Each table is preceded by a column manifest — a declaration of the columns it will use before the table body. This allows verification that all declared columns are populated and no undeclared columns appear.
- **Pass condition**: Every table in the output has a pre-declared column list that matches the actual columns used. A table appearing without a preceding column declaration does not pass.

### C-19 · Named Sub-Protocol for Each Multi-Component Requirement
- **Weight**: aspirational
- **Category**: structure
- **Text**: At least one multi-step structural requirement is given a formal protocol name that appears in both the section heading and the skill instruction. Named protocols are referenceable and verifiable; unnamed multi-step requirements rely on contextual recall.
- **Pass condition**: At least one multi-step requirement has a formal name used consistently in both the instructions and the heading. The name must appear in at least two structural locations.

### C-20 · Inline Pass/Fail Pairs at Requirement Sites
- **Weight**: aspirational
- **Category**: correctness
- **Text**: For at least two requirements where failure is possible, the output includes an inline counter-example pair — a concrete passing case and a concrete failing case side by side. Pairs disambiguate borderline outputs by demonstrating the requirement boundary.
- **Pass condition**: At least two requirement sites include both a passing example and a failing example, labeled or clearly identifiable as such. A single example (pass only, or fail only) does not satisfy a pair.

### C-21 · All Multi-Component Requirements Named
- **Weight**: aspirational
- **Category**: structure
- **Text**: Every multi-component structural requirement has a formal protocol name — not just one. An output that names the Replication Fidelity Standard but leaves the anchored rebuttal requirement unnamed has one unnamed multi-component requirement and fails this criterion.
- **Pass condition**: Zero multi-component requirements are unnamed. Each must have a formal name appearing in both the heading manifest (C-17) and its section header. An output can pass C-19 (at least one named) while failing C-21 (others unnamed).
- **Relationship to C-19**: C-19 requires "at least one" named sub-protocol; C-21 requires every multi-component requirement to be named. The gap between them is the number of unnamed requirements — C-21 pass means that count is zero.

### C-22 · Counter-Example Pairs at Every Failure Condition
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every requirement that admits a failure condition receives an inline pass/fail pair — not just two or more (C-20's floor). Maximum density means an evaluator can spot-check any individual requirement and find a contrast test; minimum density leaves some requirements judgment-dependent.
- **Pass condition**: Every requirement site where failure is possible has a pass/fail pair. An output can pass C-20 with two pairs and fail C-22 because other failure-admitting requirements have no contrast test.
- **Relationship to C-20**: C-20 requires "at least two" inline pairs; C-22 requires pairs at every failure-admitting site. Maximum density distinguishes adversarial robustness from minimum compliance.

### C-23 · Protocol Names Double-Declared in Manifest and Section Header
- **Weight**: aspirational
- **Category**: structure
- **Text**: Each sub-protocol name appears at two independent structural sites — in the global heading manifest and again as the section header. A protocol absent from either site is detectable from that verification path alone.
- **Pass condition**: Every sub-protocol name appears verbatim in both the heading manifest and the corresponding section header. Presence in one site but not the other fails this criterion.
- **Relationship to C-17 and C-19**: C-17 requires a heading manifest; C-19 requires protocols to be named within sections; C-23 requires those protocol names to also appear in the manifest. An output can satisfy both C-17 (manifest present) and C-19 (protocols named in sections) while failing C-23 (manifest does not include sub-protocol names).

### C-24 · Exact-Text Quotation at Claim-Reference Steps
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a scaffold step references an earlier claim — most critically when a rebuttal step references the steelman claim — the exact text of that claim is quoted inline at the reference point. A label like `NAMED CLAIM: "[exact text from earlier step]"` reproduces the claim verbatim rather than paraphrasing it.
- **Pass condition**: Every claim-reference step quotes the referenced claim with exact text, not a category label or paraphrase. "The claim that costs are prohibitive" does not pass. `NAMED CLAIM: "Migration requires rebuilding all existing pipeline configurations from scratch"` does pass.
- **Relationship to C-12**: C-12 requires the rebuttal be anchored to a named claim; C-24 requires the exact text of that claim to be quoted at the anchor point. An output can pass C-12 by naming a claim category and fail C-24 because the actual claim text is paraphrased. Paraphrase allows the model to subtly shift the claim being rebutted; exact quotation prevents that.

### C-25 · Enforcement Annotations at Every Structural-Requirement Site
- **Weight**: aspirational
- **Category**: structure
- **Text**: Each individual site in the scaffold where a structural requirement applies carries an inline enforcement annotation (e.g., `[PAIR REQUIRED]`, `[NAMED CLAIM REQUIRED]`). Global rules ("pairs are required throughout") are insufficient; every site must be individually marked. An unannotated site is a structural error detectable by annotation-count audit independently of content review.
- **Pass condition**: Every site where a structural requirement could be violated carries an explicit annotation. A reviewer can audit compliance by scanning for annotations and verifying each is satisfied, without reading the full output. Any requirement site without an annotation fails this criterion regardless of whether the requirement is actually met.
- **Relationship to C-22**: C-22 requires maximum density of pairs at every failure condition; C-25 requires each such site to carry an enforcement annotation making the obligation locally visible. An output can satisfy C-22 (pairs present everywhere) while failing C-25 (sites not individually annotated). The difference is audit path: C-22 requires reading all sites to confirm coverage; C-25 enables annotation-count verification.

### C-26 · Manifest-to-Header Verbatim Alignment
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The text of each sub-protocol name in the heading manifest matches the corresponding section header text character-for-character. Paraphrase or partial match between sites — even minor rewording — fails. When both sites carry identical text, the two verification paths established by C-23 resolve to the same string, eliminating ambiguity about which manifest entry corresponds to which section.
- **Pass condition**: Every sub-protocol name in the heading manifest matches its section header text exactly. "Anchored Rebuttal Protocol" in the manifest and "Rebuttal with Anchoring" in the header fail this criterion even if both C-17 and C-23 are otherwise satisfied.
- **Relationship to C-23**: C-23 requires sub-protocol names to appear at both manifest and section header (double-declaration); C-26 requires those texts to be identical. An output can satisfy C-23 (name present at both sites) while failing C-26 (texts differ). Verbatim alignment removes the judgment call of whether two slightly different strings refer to the same protocol: they must be the same string.
