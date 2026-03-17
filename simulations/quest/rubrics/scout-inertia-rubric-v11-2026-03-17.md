Now I have the complete v10 rubric. Let me extract the new criteria and produce v11.

The three R10 patterns map to two new criteria:
- Patterns 1+2 (format-invariant, format-agnostic) → **C-32: Format-Declared Manifest Pattern**
- Pattern 3 (C-29 as binding constraint) → **C-33: Canonical String Manifest Residency**

Denominator: 23 → 25.

---

# scout-inertia Rubric — v11

**Changes from v10 to v11:**

Two new aspirational criteria extracted from R10 excellence signals.

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-32 | **Format-Declared Manifest Pattern** | R10 confirmed C-30 and C-31 are format-invariant: V-03's prose manifest satisfies all three co-residence properties as surely as V-02's tabular manifest. C-32 captures the complementary obligation: the manifest block explicitly declares its format via a labeled block heading (e.g., "SCAFFOLD MANIFEST TABLE", "STRUCTURAL MANIFEST — PROSE FORMAT"). The declaration appears once, at the block's opening. The declared format is applied consistently to every entry — no mixed-format manifest. Format declaration enables format-native audit: an evaluator can determine from the heading whether to look for column headers (tabular) or bracket-prefix patterns (prose) without inferring from content. |
| C-33 | **Canonical String Manifest Residency** | R10's V-01 controlled ablation confirmed C-29 is C-31's binding constraint: preserving C-27/C-28/C-30 while removing verbatim strings from the manifest drops C-31 entirely. C-33 codifies the primary-definition obligation this reveals: every verbatim reference string that defines a pass/fail condition resides in the manifest block as its canonical definition. Governed sections may quote or apply these strings but do not define them. An auditor reading only the manifest can identify every pass/fail string without consulting any governed section. C-33 upgrades C-29: C-29 allows co-location anywhere including section bodies; C-33 requires the canonical strings themselves to be manifest-resident as primary definitions — governed sections are derivative, the manifest is authoritative. |

**Formula:** `aspirational_pass / 25 * 10` (denominator 23 → 25)

**C-32/C-33 relationships:**
- C-32 upgrades C-30: C-30 requires each manifest entry to state its governed sites; C-32 requires the manifest block itself to carry an explicit format declaration, and all entries to apply that format consistently. An output can satisfy C-30 (entries list governed sites) while failing C-32 if the manifest block has no heading that declares its format, or if some entries use column structure while others use prose paragraphs within the same block. The distinction is auditability of the manifest as a typed artifact vs. auditability of individual entries.
- C-33 upgrades C-29: C-29 requires verbatim-alignment directives to be co-located with their reference strings; C-33 requires the reference strings to be canonically defined in the manifest. C-29 is satisfiable by a section body that contains both the strings and a verbatim directive pointing at them (the R9 V-03 pattern before the pattern was refined); C-33 is satisfiable only when the manifest contains the strings as primary definitions with governed sections quoting them. V-01's R10 ablation makes the distinction precise: V-01 kept verbatim directives in section bodies, which satisfies C-29 at the section level but fails C-33 and C-31 because the manifest cannot serve as a standalone vocabulary source.

**Evaluator Notes additions (v11):**
- C-32 and format consistency: A manifest that uses a table for entries M-01 through M-04 and prose paragraphs for M-05 and M-06 is not format-consistent even if every entry individually satisfies C-28/C-29/C-30. The format declaration must govern all entries and the entries must honor it. A heading of "SCAFFOLD MANIFEST TABLE" followed by a mix of rows and prose blocks fails C-32. A heading of "STRUCTURAL MANIFEST — PROSE FORMAT" followed entirely by "CONSTRAINT-NN [criterion] governs Section N: verbatim..." paragraphs passes. No heading at all, even with a perfectly consistent format, fails C-32: the declaration is load-bearing, not just the consistency.
- C-32 and the R10 format-invariance finding: R10 established that no format is privileged — prose satisfies C-31 as well as tabular. C-32 does not reward one format over the other. It rewards the explicit commitment to a format. The practical consequence is that an author choosing prose must label the block "STRUCTURAL MANIFEST — PROSE" (or equivalent) and apply the "CONSTRAINT-NN [criterion] governs Section N:" prefix pattern to every entry; an author choosing tabular must label the block "SCAFFOLD MANIFEST TABLE" and include the same columns for every row. Either passes C-32. An unlabeled block, regardless of how consistent its entries are, fails.
- C-33 and the V-01 lesson: V-01 in R10 was a controlled ablation: it preserved C-27/C-28/C-30 and deliberately removed verbatim strings from the manifest, placing them in section bodies instead. The result was 23/25 (C-29 fail, C-31 fail, C-33 fail). The ablation established that verbatim co-location is the last and hardest step toward triple convergence — and that placing reference strings in governed sections rather than the manifest is the specific failure mode. C-33 codifies this: the manifest must be the verbatim vocabulary source. The practical check is: given the manifest alone, can an auditor state every pass condition and rejection condition verbatim? If any condition requires opening a governed section to retrieve the string, C-33 fails.
- C-33 and the distinction from C-29: C-29 asks "are verbatim directives co-located with their reference strings?" — it passes whether that co-location is in the manifest or in governed sections. C-33 asks "are the reference strings canonically defined in the manifest?" — it passes only when the manifest is the primary definition site. A scaffold where Section 3 contains both the switch-cost format strings and a verbatim directive ("reproduce exactly as formatted below") satisfies C-29 but fails C-33: the strings are defined in Section 3, not in the manifest. The manifest in that scaffold is a constraint-rule source but not a vocabulary source; C-33 requires it to be both.

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

## Aspirational Criteria (`aspirational_pass / 25 * 10` pts)

### C-09 · Competitor Zero Named
- **Weight**: aspirational
- **Category**: specificity

### C-10 · Adoption Cost Amortization Modeled
- **Weight**: aspirational
- **Category**: depth

### C-11 · Failure Mode Actor/Trigger Decomposition
- **Weight**: aspirational
- **Category**: structure

### C-12 · Inertia Threat Deviation Justification Path
- **Weight**: aspirational
- **Category**: correctness

### C-13 · Switching Cost Unit Column
- **Weight**: aspirational
- **Category**: precision

### C-14 · Defeat Condition Cross-Reference to Failure Modes
- **Weight**: aspirational
- **Category**: traceability

### C-15 · Synthesis Step Mandated
- **Weight**: aspirational
- **Category**: completeness

### C-16 · In-Flight Disruption Dimension Present
- **Weight**: aspirational
- **Category**: depth

### C-17 · Minimum Row Count Enforced on FM Inventory
- **Weight**: aspirational
- **Category**: structural completeness

### C-18 · Falsifiability Condition on Defeat Criteria
- **Weight**: aspirational
- **Category**: precision

### C-19 · Citation-Point Check at Section 5
- **Weight**: aspirational
- **Category**: verification

### C-20 · Deviation Justification Required for Below-HIGH Score
- **Weight**: aspirational
- **Category**: correctness

### C-21 · Scaffold-Level "Significant Without a Number Fails" Directive
- **Weight**: aspirational
- **Category**: precision

### C-22 · Structural Requirement Sites Annotated
- **Weight**: aspirational
- **Category**: traceability

### C-23 · Trailing Completeness Checklist Present
- **Weight**: aspirational
- **Category**: verification

### C-24 · Exact-Text Quotation Required for Workaround Name
- **Weight**: aspirational
- **Category**: precision

### C-25 · Per-Site Enforcement Annotations at Every Structural-Requirement Site
- **Weight**: aspirational
- **Category**: structural completeness

### C-26 · Manifest-to-Section-Header Verbatim Identity
- **Weight**: aspirational
- **Category**: precision

### C-27 · Constraint-Before-Site Placement
- **Weight**: aspirational
- **Category**: scaffold topology
- **Text**: Every structural constraint must appear in the scaffold before any site it governs — at a phase boundary, in a manifest block, or as a preamble — not co-located with the final section.
- **Pass condition**: The scaffold places all structural constraints (manifest blocks, enforcement rules, deviation-justification requirements) before the first section they govern. A constraint that first appears at or after the section it governs does not pass. Co-location with the governed section is an explicit fail.

### C-28 · Criterion-ID-Labeled Verification Scan
- **Weight**: aspirational
- **Category**: auditability
- **Text**: The verification or pre-flight gate names criteria by their assigned IDs (e.g., "C-25:", "[C-05-INT]") rather than by property description alone. An ID-labeled scan creates an audit path by criterion identifier, enabling mechanical completeness checking without content review.
- **Pass condition**: At least one verification step, checklist item, or pre-flight gate references a criterion by its assigned ID. A scan that references the property ("check verbatim alignment") without the ID label does not pass; the ID is load-bearing.

### C-29 · Manifest-Bound Verbatim Directive
- **Weight**: aspirational
- **Category**: co-location
- **Text**: The verbatim-alignment instruction appears inside the manifest block, directly adjacent to the canonical strings the model must copy. A model can know the verbatim rule as a general principle and still apply it incorrectly because it cannot apply the rule without the reference text in view. Binding the directive to the manifest block eliminates that failure mode.
- **Pass condition**: The manifest block contains both the canonical strings and an instruction to reproduce them character-for-character (or equivalent verbatim directive). A verbatim directive in a preamble or global-rules section that is separate from the manifest does not pass.

### C-30 · Manifest Scope Annotation
- **Weight**: aspirational
- **Category**: scaffold navigability
- **Text**: Each manifest entry explicitly names the section(s) or site(s) it governs, making the constraint graph navigable from the manifest alone. A manifest that states constraints without declaring their governed targets requires a full document scan to determine coverage. Explicit scope annotation enables forward navigation (manifest → governed site) and backward navigation (site → governing constraint) without scanning.
- **Pass condition**: Each entry in the manifest block includes an explicit statement of the sections or sites it governs (e.g., "MANIFEST-01 governs Sections 1 and 3", "applies to: FM Inventory table"). Manifest entries that state a constraint rule without naming its governed targets do not pass. An output can satisfy C-27 (constraint precedes governed sections) while failing C-30 if the manifest does not declare the governance relationship.

### C-31 · Triple-Constraint Manifest Convergence
- **Weight**: aspirational
- **Category**: unified enforcement
- **Text**: A single manifest block simultaneously satisfies C-27 (placed before all governed sites), C-28 (entries use criterion-ID labels), and C-29 (verbatim-alignment directive co-located with canonical reference strings). Satisfying each criterion at a different document location does not pass — the three properties must be co-resident in one block.
- **Pass condition**: One identifiable manifest block in the scaffold (1) appears before all sections it governs, (2) labels at least one entry with a criterion ID, and (3) contains a verbatim-alignment directive adjacent to the canonical strings it governs. An output that places C-27 in a preamble, C-28 in a trailing checklist, and C-29 inside governed sections satisfies each criterion separately and fails C-31. Note: C-31 requires the reference strings themselves to reside in the manifest — moving the verbatim directive to the manifest while leaving the reference strings in governed sections does not resolve the co-location requirement.

### C-32 · Format-Declared Manifest Pattern
- **Weight**: aspirational
- **Category**: manifest legibility
- **Text**: The manifest block carries an explicit format declaration in its heading or opening label (e.g., "SCAFFOLD MANIFEST TABLE", "STRUCTURAL MANIFEST — PROSE FORMAT"). R10 established that tabular and prose manifests are format-equivalent for C-28/C-29/C-30/C-31 — both formats satisfy the co-residence requirements. C-32 captures the complementary obligation: the chosen format is declared explicitly, not inferred from content, and is applied consistently to every entry in the block. A manifest with a declared format enables format-native audit: the evaluator knows from the heading whether to look for column headers or bracket-prefix patterns.
- **Pass condition**: The manifest block has a heading or label that explicitly states its format type. The declared format is applied consistently to all entries — no mixed-format blocks (e.g., some entries as table rows, some as prose paragraphs). An unlabeled manifest block fails C-32 regardless of internal consistency. A labeled block with mixed-format entries fails C-32 regardless of the label.

### C-33 · Canonical String Manifest Residency
- **Weight**: aspirational
- **Category**: manifest completeness
- **Text**: Every verbatim reference string that defines a pass/fail condition for any constraint is canonically defined inside the manifest block. Governed sections may quote or apply these strings but do not originate them. R10's V-01 controlled ablation established that this is C-31's binding property: preserving C-27/C-28/C-30 while relocating verbatim strings to section bodies drops C-29, C-31, and C-33 simultaneously, confirming that manifest-resident canonical strings are the final and hardest step toward a fully self-contained manifest.
- **Pass condition**: Given only the manifest block, an auditor can state verbatim every string that constitutes a passing or failing output condition for every constraint entry. If retrieving any pass/fail string requires opening a governed section, C-33 fails. Governed sections that quote manifest strings are permitted and expected; governed sections that define strings the manifest does not contain are an automatic fail. C-33 subsumes C-29's requirement and adds the primary-definition obligation: the manifest does not merely co-locate strings with directives, it originates them.
