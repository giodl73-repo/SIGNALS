Reading the R9 scorecard to identify the excellence patterns before writing v10.

The scorecard surfaces two new patterns:

1. **V-01 excellence signal**: `each manifest entry labels its governed section(s)` — explicit scope annotation in the manifest itself, not just constraint-before-site ordering. V-04 has a manifest but its description doesn't confirm this directional labeling. This is distinct from C-27.

2. **R9 ceiling pattern**: No variation achieves C-27 + C-28 + C-29 simultaneously. V-01 achieves C-27+C-28; V-03 achieves C-29 via co-location inside sections (which violates C-27); V-04 achieves C-27+C-28 but misses C-29. The triple convergence — a manifest block that is pre-document, ID-labeled, AND contains verbatim directives — is the aspirational target no R9 variation reached.

These become C-30 and C-31. Denominator goes from 21 → 23.

---

# scout-inertia Rubric — v10

**Changes from v9 to v10:**

Two new aspirational criteria extracted from R9 excellence signals.

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-30 | **Manifest Scope Annotation** | V-01's manifest entries explicitly labeled which sections each entry governed ("MANIFEST-01 governs Sections 1, 3"). A manifest that states constraints without declaring their governed sites requires the reader — and the model applying it — to scan the full document to discover what each constraint covers. Explicit scope annotation makes the constraint graph navigable forward (manifest → governed site) and backward (site → governing constraint) without a document scan. |
| C-31 | **Triple-Constraint Manifest Convergence** | R9 showed three orthogonal constraint-quality dimensions can each be satisfied independently but no variation satisfied all three from a single manifest block: V-01/V-04 achieve C-27+C-28 but fail C-29; V-03 achieves C-29 via co-location inside sections, which violates C-27. Triple convergence requires a single manifest block that is (1) placed before all governed sites (C-27), (2) uses criterion-ID labels on its entries (C-28), and (3) contains verbatim-alignment directives co-located with the canonical strings it governs (C-29). The three properties must be satisfied by the same block — satisfying each at different document locations does not pass. |

**Formula:** `aspirational_pass / 23 * 10` (denominator 21 → 23)

**C-30/C-31 relationships:**
- C-30 upgrades C-27: C-27 requires structural constraints to appear in the scaffold before any site they govern; C-30 requires each constraint entry to additionally state its governed sites explicitly within the manifest. An output can satisfy C-27 (the constraint precedes Section 3) while failing C-30 if the manifest entry does not declare "governs Section 3." The distinction is navigability: C-27 enforces document order; C-30 enforces that the order is declared and auditable from the manifest alone.
- C-31 upgrades C-27/C-28/C-29 jointly: Those three criteria can be individually satisfied at different document locations without any single block satisfying all three. C-31 requires co-location of all three properties in one manifest block. V-03's approach of placing verbatim directives inside governed sections satisfies C-29 but violates C-27's prohibition on co-location of structural constraints. Triple convergence resolves this tension by placing the verbatim directive inside the manifest block rather than inside the governed section — the manifest precedes all governed sites, so the verbatim directive is simultaneously pre-document (C-27), ID-labeled (C-28), and co-located with the reference strings (C-29).

**Evaluator Notes additions (v10):**
- C-30 and navigability vs. ordering: C-27 establishes that the scaffold is topologically correct — constraints flow forward toward governed sites. C-30 establishes that the topology is legible — a reader can determine from the manifest alone what each constraint covers without tracing through the document. The practical consequence is mechanical auditability: given a list of sites, an evaluator can check C-30 by reading only the manifest and confirming each site appears as a declared target of at least one entry. No document scan required.
- C-31 and the tension between C-27 and C-29: C-29 requires verbatim-alignment directives to be co-located with their reference strings. C-27 requires structural constraints to precede governed sections rather than being co-located with them. These two requirements appear to conflict: co-location (C-29) suggests placing the directive where the strings appear; preceding (C-27) suggests extracting constraints to a preamble. The resolution is that the manifest block is the canonical location for reference strings. When a manifest lists canonical strings and the verbatim directive appears inside that same manifest block, the directive is both co-located with the strings (C-29) and pre-document relative to governed sections (C-27). V-03's failure is instructive: it placed the verbatim directive inside governed sections, which is co-location with the strings but not pre-document placement. The triple-convergence pattern requires the reference strings themselves to live in the manifest, not in the sections.
- C-31 and why "passing all three separately" is insufficient: A scaffold that places constraints in a preamble (C-27), uses ID labels in a trailing checklist (C-28), and embeds verbatim directives inside each governed section (C-29) satisfies each criterion at a different location. This creates three separate enforcement mechanisms that must all remain synchronized as the scaffold evolves. A unified manifest block that satisfies all three is structurally simpler — one block to update, one block to audit — and eliminates the coordination failure mode where preamble constraints diverge from section-level verbatim directives.

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

## Aspirational Criteria (`aspirational_pass / 23 * 10` pts)

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
