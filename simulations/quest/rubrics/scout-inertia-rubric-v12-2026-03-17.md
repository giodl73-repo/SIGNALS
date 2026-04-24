`scout-inertia-rubric-v12-2026-03-17.md` written.

---

# scout-inertia Rubric — v12

**Changes from v11 to v12:**

Seven new aspirational criteria extracted from R11 excellence signals. The R11 scorecard evaluated A-16, A-19, A-23, A-25, A-26, A-27, A-28 as candidate criteria. These formalize as C-34 through C-40.

| ID | Criterion | What it captures |
|----|-----------|-----------------|
| C-34 | **Primary Key Rule Label** | R11's V-01 places `[A-16 PRIMARY KEY RULE]` at the FM-[N] assignment directive in Stage 1. The bracket label makes the rule mechanically scannable without reading prose. C-34 formalizes the bracket-label obligation for primary key assignment. |
| C-35 | **Citation Integrity Rule Label** | R11's V-01 places `[A-19 CITATION INTEGRITY RULE]` in Stage 5B at the directive governing downstream FM-[N] citation. Distinct from C-34 (assignment vs. citation); establishes the second bracket-labeled audit checkpoint in the FM-[N] lifecycle. |
| C-36 | **Minimum Bracket-Prefix Label Count** | R11's V-01 carries three distinct bracket elements: `[A-16...]`, `[A-19...]`, `[BRIDGE COMPLETION COMMAND]`. Three or more labeled elements establish a systematic labeling convention rather than an isolated annotation. |
| C-37 | **Completion Command Inside Gate Block** | R11 distinguished V-01 (command inside gate block body — PASS) from V-02 (command embedded in gate heading — PARTIAL). C-37 requires the bracket command directive to appear in the block body, separating the decision (heading) from the remediation action (body). |
| C-38 | **FAIL-FIRST Domain Subtitle** | R11's clearest discriminating finding: V-01 fails (FAIL-FIRST heading has no subtitle); V-02 passes ("FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR"). C-38 requires every FAIL-FIRST heading to carry both a structural role marker and a domain-frame subtitle drawn from inertia domain vocabulary. |
| C-39 | **Binary-Question Gate Heading** | Both V-01 and V-02 pass with explicit binary-question headings. C-39 formalizes the binary Yes/No-answerable form as a requirement — distinguishing decision-point headings ("ALL ARTIFACTS POPULATED?") from descriptive labels ("COMPLETENESS CHECK"). |
| C-40 | **Criterion-ID Prefixes on Checklist Items** | R11's V-01 passes (Stage 6 items prefixed C-01 through C-05); V-02 partial; V-03 is the explicit control with no prefixes. C-40 requires every trailing checklist item to carry a `C-NN:` prefix, enabling criterion-ID audit without reading all items. |

**Formula:** `aspirational_pass / 32 * 10` (denominator 25 → 32)

---

**Key relationships:**

- **C-34 + C-35** are siblings covering the two poles of the FM-[N] lifecycle (assignment in Stage 1, citation in Stage 5B). Passing both is a prerequisite for C-36.
- **C-36** is a count criterion: any three distinct bracket-labeled obligations pass, not just the canonical three. C-34+C-35+C-37 is one path; other combinations are valid.
- **C-37 + C-39** define the two-part gate structure: C-39 governs the heading form (binary question); C-37 governs the body content (bracket command). Each can fail independently.
- **C-38 + C-39** define the heading vocabulary protocol: FAIL-FIRST headings need domain subtitles (C-38); gate headings need binary-question form (C-39). The two criteria prevent vocabulary contamination in both directions — neither heading type should borrow the other's register.
- **C-40** completes the criterion-ID chain that C-28 begins: C-28 requires at least one criterion-ID reference in a verification scan; C-40 requires systematic `C-NN:` prefix coverage on every checklist item.
AIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR", "THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY") and pass. C-38 codifies the obligation: every FAIL-FIRST section heading carries two components — (1) a structural marker ("FAIL-FIRST DECLARATION" or equivalent) establishing the section's role, and (2) a domain-frame subtitle phrase that names the content in inertia domain terms (competitor identity, failure modes, defeat conditions, etc.). A heading with only the structural marker fails. A heading with both components passes. |
| C-39 | **Binary-Question Gate Heading** | Both V-01 and V-02 pass A-27 with explicit binary-question headings: "BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?" and "-- READY TO PROCEED?". C-39 codifies the binary-question form as a formal criterion: the completeness gate must have a heading that is explicitly Yes/No-answerable with no interpretation required. The question form makes the gating decision explicit and separates it from descriptive or operational headings. A label like "COMPLETENESS CHECK" describes a section; a question like "ALL ARTIFACTS POPULATED?" names a decision point. C-39 requires the decision-point form. |
| C-40 | **Criterion-ID Prefixes on Checklist Items** | R11's V-01 passes with checklist items prefixed C-01, C-02, C-03, C-04, C-05. V-02 gets partial (prefix presence unconfirmed). V-03 is the explicit A-28 control variation — same lifecycle structure but no C-0N: prefixes on items. C-40 codifies the prefix obligation: every item in the trailing completeness checklist carries its criterion ID as a `C-NN:` prefix. The prefix makes the checklist mechanically auditable by criterion ID — an evaluator can locate the C-01 check without reading all items and can confirm that every essential criterion has a checklist entry. |

**Formula:** `aspirational_pass / 32 * 10` (denominator 25 → 32)

**C-34 through C-40 relationships:**
- C-34 and C-35 are sibling bracket-label criteria: C-34 governs the primary key assignment rule (Stage 1), C-35 governs the citation integrity rule (Stage 5B). They label different structural obligations at different document locations. An output can pass C-34 (Stage 1 bracket label present) while failing C-35 (Stage 5B bracket label absent). Together they establish that both poles of the FM-[N] lifecycle — definition and citation — carry bracket-labeled directives.
- C-36 subsumes C-34 and C-35 by count: a scaffold that passes both C-34 and C-35 plus has a `[BRIDGE COMPLETION COMMAND]` also passes C-36. But C-36 is not automatically satisfied by C-34+C-35: if one of the three canonical bracket elements is missing, C-36 fails even if the other two pass. The count requirement (three or more) is load-bearing — it rewards systemic labeling, not just bilateral coverage.
- C-37 and C-39 govern the two-part gate structure: C-39 requires the gate heading to be binary-question form; C-37 requires a bracket-command directive inside the gate block. An output can pass C-39 (gate has a Yes/No heading) while failing C-37 if the remediation command is embedded in the heading rather than in the block body. An output can pass C-37 (bracket command present inside the block) while failing C-39 if the heading is descriptive rather than binary-question. The two-part structure separates the decision (heading) from the action (bracket command in body).
- C-38 and C-39 together define the heading vocabulary protocol: C-38 governs FAIL-FIRST section headings (they must have domain subtitles); C-39 governs the gate heading (it must be binary-question form). The protocol prevents vocabulary contamination in both directions — a FAIL-FIRST heading that uses operational vocabulary (artifact counts, population status) instead of domain vocabulary fails C-38; a gate heading that uses domain framing instead of a bare decision question fails C-39. The combination ensures that each heading type carries exactly the vocabulary appropriate to its structural role.
- C-40 completes the criterion-ID chain: C-28 requires at least one criterion-ID label in a verification scan; C-40 requires every checklist item to carry a criterion-ID prefix. An output that uses criterion IDs selectively (some items labeled, some not) passes C-28 (at least one ID present) but fails C-40 (not every item prefixed). The distinction is systematic coverage vs. presence.

**Evaluator Notes additions (v12):**
- C-34 and mechanical scannability: The bracket-prefix format (`[A-16 PRIMARY KEY RULE]` or equivalent) is distinguished from parenthetical labels `(A-16)` or inline references "see rule A-16". The bracket enclosure is load-bearing because it enables whitespace-delimited scanning — a regex for `\[A-16` finds the rule without false positives from inline references. A scaffold that labels the primary key rule in any format other than bracket-enclosed fails C-34.
- C-35 and Stage 5B placement: The citation integrity rule label must appear at or before the Stage 5B defeat conditions table, not in a global preamble or after the table. C-35 tests that the integrity rule is proximate to the site where citation integrity is enforced. A bracket label in Stage 1 that mentions citation integrity does not satisfy C-35; the label must appear in Stage 5B's enforcement context.
- C-36 and the three-element floor: The three canonical bracket elements for C-36 are: (1) primary key assignment rule (C-34), (2) citation integrity rule (C-35), (3) a command directive (C-37). A scaffold with only C-34 and C-35 has two bracket elements and fails C-36. A scaffold that adds any third bracket-labeled obligation — including `[BRIDGE COMPLETION COMMAND]`, `[VERBATIM ENFORCEMENT RULE]`, or any other `[LABEL]` element — passes C-36 at the count level. C-36 does not require the specific three elements above; it requires at least three total.
- C-37 and the heading-vs-body distinction: The distinction matters for auditability. A command embedded in a heading ("GATE: IF NO, RETURN TO STAGE 1") is visible at section-heading scan level but cannot be independently labeled as a bracket directive and cross-referenced. A bracket command inside the block body (`[BRIDGE COMPLETION COMMAND] If N: return to Stage 1 and complete missing entries.`) is independently labelable, scannable, and can satisfy C-36's count requirement. The practical check: does the `[COMMAND]` bracket element appear in the body of the gate block? If it appears only in the heading text, C-37 fails.
- C-38 and the domain vocabulary requirement: The domain subtitle must be drawn from the inertia domain — terms relating to competitors, failure modes, switching costs, defeat conditions, or workaround analysis. Operational subtitles drawn from artifact-management vocabulary ("ALL ENTRIES POPULATED", "BEFORE PROCEEDING") fail C-38 even if a structural marker is present. The practical test: given the subtitle alone, could a reader identify this section as part of a scout-inertia analysis? If yes (because the subtitle mentions a competitor, a failure mode, or an inertia-domain concept), C-38 passes. If the subtitle is domain-neutral or artifact-centric, C-38 fails.
- C-39 and the gate heading form: The binary-question requirement is about answerable form, not about vocabulary. "ALL ARTIFACTS POPULATED?" is a binary question using artifact vocabulary — it passes C-39 despite artifact vocabulary because the form is binary. "NAMING THE UNNAMED COMPETITOR: IS THE FM INVENTORY COMPLETE?" is a binary question using domain vocabulary — it also passes C-39. A heading like "COMPLETENESS CHECKPOINT" fails because it names a location, not a decision. The test: can the heading be answered Yes or No without reading the block body? If yes, C-39 passes.
- C-40 and essential criterion coverage: C-40's practical consequence is that C-01 through C-05 (the five essential criteria) must each have a checklist entry with a C-0N: prefix. An evaluator reading only the completeness checklist can verify that all essential criteria are gated. A checklist that covers essential criteria by description without ID prefix fails C-40. A checklist that covers all essential criteria with C-0N: prefixes and also covers recommended criteria (C-06, C-07, C-08) passes regardless of whether recommended items also carry ID prefixes — the minimum is that every essential criterion has a prefixed entry.

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

## Aspirational Criteria (`aspirational_pass / 32 * 10` pts)

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

### C-34 · Primary Key Rule Label
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold carries a bracket-prefix label (`[A-16 PRIMARY KEY RULE]` or equivalent) at the directive governing FM-[N] primary key assignment in the FM Inventory stage. R11's V-01 demonstrated this label in `[A-16 PRIMARY KEY RULE]` in Stage 1. The bracket enclosure makes the directive mechanically scannable: an auditor finds the primary key rule by scanning for the bracket token, not by reading surrounding prose. The label is distinct from the citation integrity label (C-35) and from any command directive (C-37).
- **Pass condition**: The scaffold contains a bracket-enclosed label at the FM-[N] assignment directive in the stage where failure modes are inventoried. Label format: `[LABEL-NAME]` with the label appearing on its own line or as a leading prefix. The label must be adjacent to the assignment rule, not in a preamble that is topographically separated from the FM Inventory stage. A rule stated as prose without a bracket-prefix element fails C-34.

### C-35 · Citation Integrity Rule Label
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold carries a bracket-prefix label (`[A-19 CITATION INTEGRITY RULE]` or equivalent) at the directive governing FM-[N] citation integrity in the defeat conditions stage. R11's V-01 demonstrated this in `[A-19 CITATION INTEGRITY RULE]` in Stage 5B. The label governs the downstream citation obligation: DC-[N] defeat conditions must cite FM-[N] identifiers that were defined in the FM Inventory. The bracket label makes this validation directive independently locatable without inspecting defeat condition entries.
- **Pass condition**: The scaffold contains a bracket-enclosed label at the citation-integrity directive in the defeat conditions stage (or the stage that cross-references FM-[N] identifiers). The label must appear at or before the first defeat condition entry, not after. A citation-integrity rule without a bracket label fails C-35. A bracket label for citation integrity placed in a global preamble rather than in the defeat conditions stage fails C-35.

### C-36 · Minimum Bracket-Prefix Label Count
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold contains at least three distinct bracket-prefix labeled elements across its full extent. Each labeled element governs a distinct structural obligation: primary key assignment (C-34), citation integrity (C-35), completion command (C-37), or any additional structural rule the scaffold defines. R11's V-01 confirmed three canonical elements: `[A-16 PRIMARY KEY RULE]`, `[A-19 CITATION INTEGRITY RULE]`, `[BRIDGE COMPLETION COMMAND]`. Three or more labeled elements establish that bracket-labeling is a convention in the scaffold rather than an isolated occurrence.
- **Pass condition**: Count distinct bracket-prefix elements across the full scaffold. Three or more distinct `[LABEL]` elements, each governing a different structural obligation, passes C-36. Two or fewer elements fail. The three elements need not be the canonical R11 examples — any three bracket-labeled obligations suffice, provided they label distinct structural rules.

### C-37 · Completion Command Inside Gate Block
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The completeness gate block contains an explicit bracket-labeled command directive in its body — below or after the binary gate question — specifying the remediation action when the gate condition fails. R11 distinguished two placements: V-01 places `[BRIDGE COMPLETION COMMAND]` inside the gate block body and passes; V-02 embeds the command in the gate heading and receives partial credit. The inside-block placement keeps the decision (heading) structurally separated from the action (body directive), and makes the command element bracket-labeled and independently scannable.
- **Pass condition**: The completeness gate block contains a bracket-enclosed command element (`[COMMAND-NAME]`) in its body text, after the binary gate question. The command names the remediation action: the target stage, the action to take, or both ("return to Stage 1 and complete missing entries"). A command that appears only inside the heading text fails C-37 regardless of whether it specifies the action. A command present in the body without bracket enclosure fails C-37 because it is not independently labelable.

### C-38 · FAIL-FIRST Domain Subtitle
- **Weight**: aspirational
- **Category**: heading vocabulary
- **Text**: Every FAIL-FIRST section heading in the scaffold carries two components: (1) a structural role marker ("FAIL-FIRST DECLARATION" or equivalent) that identifies the section's function, and (2) a domain-frame subtitle phrase that names the content in inertia-domain terms. R11's V-01 fails this criterion: its FAIL-FIRST heading carries only the structural marker with no domain subtitle. R11's V-02 passes: "FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR" and "THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY" carry both components. The domain subtitle makes the section navigable as domain content — a reader scanning headings can identify what the FAIL-FIRST section covers without entering the body.
- **Pass condition**: Every FAIL-FIRST section heading contains a domain-frame subtitle phrase drawn from inertia domain vocabulary: competitor naming, failure modes, switching costs, defeat conditions, or equivalent inertia-domain concepts. A heading with only a structural marker ("FAIL-FIRST DECLARATION") fails. A heading with an operational subtitle ("FAIL-FIRST: ALL ENTRIES REQUIRED") fails — operational vocabulary is not domain vocabulary. A heading with a domain subtitle ("FAIL-FIRST DECLARATION -- THE WORKAROUND FAILURE INVENTORY") passes.

### C-39 · Binary-Question Gate Heading
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The completeness gate heading is explicitly binary Yes/No-answerable — a question form that names a decision point rather than describing a location or task. R11's V-01 ("BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?") and V-02 ("-- READY TO PROCEED?") both pass. An operational label like "COMPLETENESS CHECK" names a section type but does not name a decision; a binary question like "ALL ARTIFACTS POPULATED?" names a decision with exactly two outcomes. The binary-question form makes gate semantics explicit: a reader encountering the heading knows immediately that the block is a branch point, not a description block.
- **Pass condition**: The completeness gate heading contains a binary question answerable Yes or No without reading the block body. The question can use any vocabulary (artifact-management or domain) provided the form is binary. A heading that states a task, a warning, or a location label fails C-39. A heading that asks a binary question — even a simple "READY TO PROCEED?" — passes. The Yes/No form is the only load-bearing requirement.

### C-40 · Criterion-ID Prefixes on Checklist Items
- **Weight**: aspirational
- **Category**: audit traceability
- **Text**: Every item in the trailing completeness checklist carries its criterion ID as a `C-NN:` prefix. R11's V-01 passes: Stage 6 items carry "C-01:", "C-02:", "C-03:", "C-04:", "C-05:" prefixes. V-02 receives partial credit (prefix presence unconfirmed). V-03 is the explicit control variation for A-28 — same lifecycle structure but no C-0N: prefixes on items. The ID prefix makes the checklist mechanically auditable by criterion: an evaluator can locate the C-01 gate without reading all items, and can confirm that every essential criterion has a checklist entry by scanning for C-0N: prefixes.
- **Pass condition**: Every item in the trailing completeness checklist is prefixed with its criterion ID in `C-NN:` format. At minimum, the five essential criteria (C-01 through C-05) must each have a prefixed entry. A checklist that uses descriptive item text without ID prefixes fails C-40 regardless of how complete the coverage is. A checklist with ID prefixes on some items but not all fails C-40. C-28 (at least one criterion-ID label in a verification scan) is satisfiable with fewer prefixes; C-40 requires systematic prefix coverage across all items.
