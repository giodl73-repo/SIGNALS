# scout-inertia Rubric — v9

**Changes from v8 to v9:**

Three new aspirational criteria extracted from R8 excellence signals.

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-27 | **Constraint-Before-Site Placement** | The R8 gap in V-03: C-25/C-26 constraints were placed at the synthesis step *after* earlier requirement sites had already been written. Constraints placed after governed sites cannot retroactively repair them. This criterion requires every structural constraint to appear in the scaffold *before* any site it governs — at a phase boundary, in a manifest block, or as a preamble — not co-located with the final section. |
| C-28 | **Criterion-ID-Labeled Verification Scan** | V-05's pre-flight gate named `C-24`/`C-25`/`C-26` explicitly in its verification steps. Naming a criterion by ID converts it from a property to achieve into a property to verify and repair. An ID-labeled scan creates an audit path by criterion identifier, enabling mechanical completeness checking without content review. A scan that references the property ("check verbatim alignment") without the ID label does not pass; the ID is load-bearing. |
| C-29 | **Manifest-Bound Verbatim Directive** | V-01/V-02 placed the verbatim-alignment instruction *inside the manifest block* — "Section headers must reproduce these manifest entries character-for-character" — directly adjacent to the strings the model must copy. A model can know the verbatim rule as a general principle and still apply it incorrectly because it cannot apply the rule without the reference text in view. Binding the directive to the manifest block eliminates that failure mode: the model cannot read the constraint without simultaneously reading the strings it governs. |

**Formula:** `aspirational_pass / 21 * 10` (denominator 18 → 21)

**C-27/C-28/C-29 relationships:**
- C-27 upgrades C-25: C-25 requires per-site enforcement annotations at every structural-requirement site; C-27 requires those annotations — and the rules that mandate them — appear in the scaffold *before* the sections they govern. An output can satisfy C-25 (annotations present everywhere) while failing C-27 if the directive mandating annotations is placed after the first annotated site. The distinction is causal: C-25 checks coverage; C-27 checks that the scaffold structure makes coverage mandatory rather than coincidental.
- C-28 upgrades C-22/C-24/C-25/C-26 generically: Any structural requirement becomes auditable when the verification step names it by criterion ID rather than by property description. C-28 does not require every criterion to be ID-labeled in the scaffold output itself — it requires that the verification or pre-flight gate, where present, references criteria by their assigned IDs. An output can have a thorough checklist ("verify verbatim alignment, verify per-site annotations, verify exact-text quotation") and fail C-28 because none of those checklist items is traceable to a criterion ID.
- C-29 upgrades C-26: C-26 requires manifest entries and section headers to be verbatim identical; C-29 requires the instruction enforcing that identity to appear inside the manifest block alongside the entries being aligned. An output can satisfy C-26 (no divergence occurs) and fail C-29 if the verbatim directive is located in a preamble or global-rules section rather than in the manifest itself. The distinction is proximity: the directive must be readable at the moment the model encounters the reference strings, not before or after.

**Evaluator Notes additions (v9):**
- C-27 and retroactive repair impossibility: Once a section has been written, a constraint introduced afterward cannot change what was written. Scaffold design must treat constraint placement as a topological requirement — constraints are nodes with edges to the sites they govern, and all edges must point forward in document order. V-03's failure is the canonical example: synthesis-scoped constraints left COMPETITOR ZERO analysis sections — written earlier — unprotected. The fix is not to strengthen the synthesis constraint; it is to move the constraint before the first governed site.
- C-28 and the difference between a checklist and an audit: A checklist of property descriptions ("verify pairs present", "verify headers match") requires a human reviewer to map each item to the criterion it covers. An ID-labeled scan ("C-25: count annotation-site markers; C-26: confirm character-for-character identity at each manifest entry") creates a direct mapping. The audit path by ID means any criterion that fails the scan is unambiguously identified; no mapping step is required. This matters when rubric versions change: a criterion-ID label is version-stable; a property description may match multiple criteria or none after a version bump.
- C-29 and the co-location principle for reference-dependent constraints: Some constraints can be stated globally and applied locally (e.g., "use imperative mood throughout"). Verbatim-alignment is not this type: a model applying it correctly must have the reference strings in view at the moment of application. Co-location ensures the constraint and its reference strings are read together. A manifest block that lists entries and instructs "reproduce these character-for-character in section headers" is structurally superior to a preamble that says the same thing, because the model reads the directive and the strings it governs in a single pass.

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

### C-07 · Forward-Looking Risk Identified
- **Weight**: recommended
- **Category**: depth
- **Text**: The output identifies at least one risk that grows over time if inertia is maintained — technical debt accumulation, compounding workaround complexity, or increasing divergence from the supported path. Static cost analysis alone does not pass; at least one dynamic risk vector must appear.
- **Pass condition**: One forward-looking risk is named with a mechanism (why it compounds) rather than just stated as a concern.

### C-08 · Adoption Trigger Conditions Specified
- **Weight**: recommended
- **Category**: actionability
- **Text**: The output names at least one concrete condition that, when met, should trigger adoption evaluation — a team size threshold, a failure frequency, a cost milestone, or an event type. This converts the analysis from descriptive to prescriptive.
- **Pass condition**: At least one trigger condition is stated in checkable terms ("when the team exceeds 5 developers", "when migration failures exceed one per sprint"). Vague triggers ("when the pain is high enough") do not pass.

---

## Aspirational Criteria (10 pts total)

### C-09 · Steelman of Inertia Position Constructed
- **Weight**: aspirational
- **Category**: rigor
- **Text**: The output constructs the strongest defensible case for maintaining the current workaround before arguing against it. A steelman acknowledges the genuine strengths of the inertia position — not strawman objections that are trivially answered.
- **Pass condition**: The steelman includes at least one argument that a reasonable defender of inertia would actually endorse — something that concedes partial merit to staying with the current approach.

### C-10 · Quantified Threshold for "Inertia Wins"
- **Weight**: aspirational
- **Category**: rigor
- **Text**: The output specifies explicit numeric or categorical thresholds under which inertia is the rational choice — small team sizes, low usage rates, short project lifetimes, or other falsifiable conditions. This is the complement of C-04: not just when inertia loses, but when it wins.
- **Pass condition**: At least one condition under which inertia is explicitly recommended (not merely acknowledged as possible) is stated in checkable terms.

### C-11 · Adoption Path Sketch Included
- **Weight**: aspirational
- **Category**: actionability
- **Text**: The output sketches a minimum viable adoption path — the fewest steps required to move from current workaround to feature use. This need not be exhaustive; it must be concrete enough that a team could start today.
- **Pass condition**: At least three concrete steps are named in sequence. "Evaluate the feature" does not count as a step; "run the migration script on a test project" does.

### C-12 · Rebuttal Anchored to Named Claim
- **Weight**: aspirational
- **Category**: rigor
- **Text**: Where the output rebuts an objection (e.g., from a steelman), the rebuttal is explicitly anchored to a named claim from the steelman — not a free-standing counter-argument. This prevents the output from arguing against a claim it did not explicitly state.
- **Pass condition**: At least one rebuttal includes a traceable reference to the specific steelman claim being rebutted (e.g., "In response to the claim that..."). A rebuttal that argues against a position without naming the claim it addresses fails.

### C-13 · Dual-Source Confidence Assessment
- **Weight**: aspirational
- **Category**: rigor
- **Text**: The output rates its own confidence in the switching cost estimates using at least two independent reasoning paths — for example, analogy to similar migrations plus first-principles time estimation. Single-source estimates (only analogy, or only decomposition) do not reach dual-source.
- **Pass condition**: Two distinct reasoning paths for at least one cost estimate are visible in the output. The paths must be independent — restating the same estimate in different words does not count.

### C-14 · Inertia Decay Curve Described
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output describes how the inertia advantage (switching cost vs. workaround cost) changes over time — not just the current snapshot. The decay curve identifies when the crossover point occurs: the moment at which the accumulated workaround cost exceeds the one-time switching cost.
- **Pass condition**: A crossover analysis is present, even if informal. It must name the direction of change (inertia advantage grows or shrinks over time) and at least one factor driving that change.

### C-15 · Stakeholder-Differentiated Cost View
- **Weight**: aspirational
- **Category**: depth
- **Text**: Switching costs are presented from at least two distinct stakeholder perspectives — e.g., individual developer vs. team lead vs. engineering manager — with different cost profiles for each. A single undifferentiated cost view does not pass regardless of detail level.
- **Pass condition**: At least two named stakeholder types have distinct cost entries. Costs that apply identically to all stakeholders are shared costs, not stakeholder-differentiated.

---

## Structural Criteria (aspirational, no separate weight — scored within aspirational pool)

### C-16 · Protocol Manifest Present
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: The output includes an upfront manifest block listing all sub-protocols or major structural sections by name before the body begins. The manifest serves as a verification surface: a reviewer can confirm all declared sections are present without reading the full output.
- **Pass condition**: A manifest block exists before the first body section. It lists each sub-protocol/section by the name used in the section header.

### C-17 · Section-Level Verification Pairs
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Each major section includes at least one pass/fail verification pair — a stated requirement and its observable pass condition — enabling a reviewer to check section compliance without inferring what "good" looks like.
- **Pass condition**: At least three sections contain explicit pass/fail pairs. Implicit criteria ("this section should be detailed") do not count.

### C-18 · Replication Fidelity Instructions Present
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: The output includes explicit instructions for reproducing the analysis — what inputs are required, what steps to follow, what variation is acceptable — so a second evaluator could run the same skill on the same feature and produce a structurally comparable output.
- **Pass condition**: Replication instructions appear either in a dedicated section or as inline protocol steps throughout. They must be specific enough to constrain reproduction, not just describe what was done.

### C-19 · Failure Mode Enumeration Complete
- **Weight**: aspirational (structural)
- **Category**: coverage
- **Text**: The failure mode section (C-05) is exhaustively structured — a numbered list, table, or other enumeration format — rather than described in prose. Enumerated failure modes are individually checkable; prose descriptions are not.
- **Pass condition**: Failure modes appear as a list or table with at least two entries, each independently readable without surrounding context.

### C-20 · Threat Score With Confidence Interval
- **Weight**: aspirational (structural)
- **Category**: correctness
- **Text**: The HIGH threat score (C-03) is accompanied by a confidence interval or uncertainty qualifier — not just the score but the strength of evidence behind it. "HIGH (confidence: 80%, based on 3 analogous migrations)" passes; "HIGH" alone satisfies C-03 but not C-20.
- **Pass condition**: The threat score entry includes an explicit confidence qualifier or evidence count.

### C-21 · Sub-Protocol Names Double-Declared
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Each sub-protocol named in the manifest appears again as a section header in the body, providing two independent verification paths: manifest-to-section and section-to-manifest. A name that appears in the manifest but not in a section header (or vice versa) fails this criterion.
- **Pass condition**: Every manifest entry has a corresponding section header using the same name (see C-26 for exact-text requirement), and every section header has a corresponding manifest entry. No orphaned entries in either direction.

### C-22 · Maximum Pass/Fail Density
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Every structural requirement in the output that has an observable failure condition carries a pass/fail pair. This is the maximum-density version of C-17: not just three sections with pairs, but every requirement site that could have a pair does.
- **Pass condition**: No structural requirement site in the output is missing a pass/fail pair where one is logically possible. An evaluator scanning for unpaired requirements finds none.

### C-23 · Sub-Protocol Names in Both Manifest and Header
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Refinement of C-21. Each sub-protocol name appears verbatim in both the manifest block and the corresponding section header. A sub-protocol paraphrased between manifest and header satisfies C-21 (names present at both locations) but fails C-23 (names must be textually consistent).
- **Pass condition**: The manifest entry text and the section header text for each sub-protocol are the same string (see C-26 for character-for-character requirement).

### C-24 · Exact-Text Quotation at Claim-Reference Steps
- **Weight**: aspirational (structural)
- **Category**: rigor
- **Text**: At every step where a rebuttal references a steelman claim (C-12), the claim is quoted verbatim — the exact text of the claim as stated — not paraphrased. The scaffold must require `NAMED CLAIM: "[exact text]"` as a structural label at the rebuttal step. Paraphrase at the reference point is a structural failure regardless of how accurate the paraphrase is.
- **Pass condition**: Every rebuttal step that cites a steelman claim includes a `NAMED CLAIM:` label with the claim text reproduced verbatim from the steelman section. A rebuttal that says "the claim that switching costs are high" without quoting the exact steelman text fails even if the characterization is accurate.

### C-25 · Enforcement Annotations at Every Structural-Requirement Site
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Each site in the scaffold where a structural requirement applies carries an inline annotation (e.g., `[PAIR REQUIRED]`) marking the obligation locally. A global rule ("all requirement sites must have pairs") does not substitute for per-site annotations: the annotation must appear at each individual site so that an unannotated site is a locally detectable structural error.
- **Pass condition**: Every structural-requirement site carries an inline annotation. A reviewer scanning for annotation markers can identify any unannotated requirement site without reading the surrounding content for context.

### C-26 · Manifest-to-Header Verbatim Alignment
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Manifest entries and their corresponding section headers are character-for-character identical — not just textually consistent (C-23) but bit-for-bit the same string. A name that is abbreviated, reformatted, or otherwise altered between manifest and header satisfies C-23 but fails C-26. Verbatim alignment eliminates the judgment call about whether two near-identical strings refer to the same protocol.
- **Pass condition**: For each manifest entry, the corresponding section header reproduces it exactly. Any character-level difference — spacing, capitalization, punctuation — is a failure. The manifest is authoritative; any header that diverges is a defect.

### C-27 · Constraint-Before-Site Placement
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Every structural constraint in the scaffold appears *before* the first site it governs — at a phase boundary, in a manifest preamble, or as a section-opening directive — never after. A constraint placed after a governed site cannot retroactively repair outputs written before the constraint was read. The placement requirement is topological: in document order, each constraint node must precede all requirement-site nodes in its governance scope.
- **Pass condition**: No structural constraint appears after the first site it governs. An evaluator mapping constraint positions to site positions finds no constraint that is downstream of any site in its scope. V-03's synthesis-scoped C-25/C-26 constraints, placed after COMPETITOR ZERO analysis sections that contained requirement sites, are the canonical failure pattern this criterion rejects.

### C-28 · Criterion-ID-Labeled Verification Scan
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: Where the scaffold includes a verification or pre-flight gate, each check in that gate references the criterion it verifies by ID (e.g., "C-25: count annotation-site markers and confirm count matches requirement-site count"). A property-description check ("verify per-site annotations are present") without an ID label does not pass. Criterion-ID labels create an audit path by identifier, enabling mechanical completeness checking: a reviewer can confirm that every active criterion has a corresponding gate check by ID without reading the check descriptions.
- **Pass condition**: Every check in the verification gate names at least one criterion ID. The set of criterion IDs referenced in the gate covers all aspirational criteria that the scaffold targets. A gate that checks all properties but names no IDs fails; a gate that names some IDs but omits others fails for the omitted criteria.

### C-29 · Manifest-Bound Verbatim Directive
- **Weight**: aspirational (structural)
- **Category**: structure
- **Text**: The verbatim-alignment instruction (C-26) appears *inside the manifest block* — directly adjacent to the manifest entries the model must copy to section headers — rather than in a general preamble, global rules section, or anywhere separated from the reference strings. The constraint must be readable at the moment the model encounters the strings it governs. A model that knows the verbatim rule as a general principle but reads it before encountering the manifest entries may still fail C-26 through drift; co-location with the manifest entries eliminates that failure mode.
- **Pass condition**: The manifest block contains an explicit verbatim-identity instruction (e.g., "Section headers must reproduce these entries character-for-character") alongside the manifest entries. An equivalent instruction appearing only outside the manifest block does not pass, even if the instruction is unambiguous and the model complies.

---

## Scoring Summary

| Pool | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 pts (all must pass) |
| Recommended | C-06 through C-08 | 30 pts |
| Aspirational | C-09 through C-29 | 21 criteria |
| **Formula** | `aspirational_pass / 21 × 10` | — |

**Denominator history**: 5 (v1) → 8 (v2) → 11 (v3) → 13 (v4) → 15 (v5–v7) → 18 (v8) → **21 (v9)**
