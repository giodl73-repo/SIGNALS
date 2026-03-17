Here is the complete v13 rubric. Summary of what was extracted and formalized:

---

**4 new criteria from R12 excellence signals:**

| ID | Source signal | What it formalizes |
|----|--------------|-------------------|
| **C-41** | V-05: `[BRIDGE Q3 COMMAND]` + `[BRIDGE Q4 COMMAND]` at artifact level | Per-artifact bracket commands at each bridge artifact's authoring point, distinct from the gate-level C-37 command |
| **C-42** | V-02: "STATUS QUO" in all three bracket labels | Vocabulary threading — the three required bracket elements share a common domain-axis word or phrase |
| **C-43** | V-04: "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" | Explicit count quantifier ("BOTH", "ALL THREE") in the gate interrogative — "ALL" alone fails because the count is indeterminate from the heading |
| **C-44** | V-05: "PASS BEFORE ADVANCING --..." | Action-imperative structural marker before `--` — commands the author's behavior vs. describing the gate's type |

**Key structural relationships added:**
- C-41 extends C-37 (artifact level vs. gate level — non-overlapping, non-subsuming)
- C-42 extends C-36 (vocabulary coherence vs. count — C-36 is necessary but not sufficient for C-42)
- C-43 extends C-39 (count specificity vs. binary form — C-43 implies C-39)
- C-44 is orthogonal to C-39 (marker component vs. interrogative component — the two halves of the heading)
- C-39 + C-43 + C-44 together fully specify the maximally informative gate heading structure

**Formula:** `aspirational_pass / 36 * 10` (denominator 32 → 36)
se drawn from inertia domain terms. |
| C-43 | **Explicit Count Quantifier in Gate Heading Interrogative** | R12's V-04 gate heading "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" uses "BOTH" to name the exact expected artifact count. V-01's "ALL BRIDGE ARTIFACTS POPULATED?" passes C-39 (binary question) but leaves the count implicit. V-04's "BOTH" resolves that ambiguity in the heading. C-43 formalizes the count-quantifier obligation: the gate heading interrogative carries an explicit quantifier that names the expected count ("BOTH", "ALL THREE", "BOTH Q3 AND Q4") rather than an open-ended "ALL" that requires reading the gate body to determine the count. |
| C-44 | **Action-Imperative Gate Structural Marker** | R12's V-05 gate heading "PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" leads with an action-imperative ("PASS BEFORE ADVANCING") as the structural marker component — the portion before the `--` separator. V-01's "BRIDGE COMPLETION GATE" is a descriptive structural label naming the gate's type; V-05's "PASS BEFORE ADVANCING" is an enforcement directive naming the author's required action. The imperative form signals that the gate is a mandatory stop, not an organizational delimiter. C-44 formalizes the action-imperative marker obligation: the gate heading's structural-marker component (before `--`) uses action-imperative vocabulary rather than a descriptive structural label. |

**Formula:** `aspirational_pass / 36 * 10` (denominator 32 -> 36)

---

**Key relationships (v13 additions):**

- **C-41 extends C-37**: C-37 requires one bracket-labeled command directive in the gate block body; C-41 requires per-artifact bracket commands at each bridge artifact's authoring point, separate from the gate. An output can pass C-37 (one gate-level command) while failing C-41 (no per-artifact commands). An output can pass C-41 while also satisfying C-37 -- the per-artifact commands and the gate command are independent structural elements at different document locations. C-41 does not subsume C-37.
- **C-42 extends C-36**: C-36 counts bracket elements (three or more distinct obligations); C-42 requires those elements to share domain-vocabulary threading. An output with three bracket elements using independent vocabulary passes C-36 and fails C-42. C-42 cannot be satisfied without also satisfying C-36 -- vocabulary threading across three elements presupposes that three elements exist. C-36 pass is a necessary but not sufficient condition for C-42 pass.
- **C-43 extends C-39**: C-39 requires the gate heading to be binary Yes/No-answerable; C-43 additionally requires an explicit count quantifier in the interrogative. Every output passing C-43 necessarily passes C-39 (a quantified binary question is still a binary question). An output passing C-39 with "ALL BRIDGE ARTIFACTS POPULATED?" fails C-43 if "ALL" is not accompanied by a specific count. The test: given the heading alone, can an author determine exactly how many artifacts must be present? If yes, C-43 passes; if no (because "ALL" requires reading the gate body to know the target count), C-43 fails.
- **C-44 is orthogonal to C-39**: C-39 governs the interrogative component of the gate heading (the question after `--`); C-44 governs the marker component (the structural label before `--`). The two criteria decompose the gate heading into complementary halves. An output can pass C-39 (binary question after `--`) with a descriptive marker ("BRIDGE COMPLETION GATE") and fail C-44. An output can pass C-44 (imperative marker before `--`) with any binary-question form and pass C-39 simultaneously. A heading satisfying both: "PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" passes C-44 (imperative marker), C-39 (binary question), and C-43 (count quantifier "BOTH").
- **C-43 + C-44 + C-39 fully specify the gate heading**: C-39 requires binary-question form; C-43 requires explicit count in the interrogative; C-44 requires imperative vocabulary in the marker. All three criteria together specify the maximally informative gate heading structure: (1) an imperative enforcement marker, (2) a binary-question decision content, and (3) an explicit artifact count -- each component serving a distinct informational purpose.

**Key relationships (v12 -- unchanged):**

- **C-34 + C-35** are siblings covering the two poles of the FM-[N] lifecycle (assignment in Stage 1, citation in Stage 5B). Passing both is a prerequisite for C-36.
- **C-36** is a count criterion: any three distinct bracket-labeled obligations pass, not just the canonical three. C-34+C-35+C-37 is one path; other combinations are valid.
- **C-37 + C-39** define the two-part gate structure: C-39 governs the heading form (binary question); C-37 governs the body content (bracket command). Each can fail independently.
- **C-38 + C-39** define the heading vocabulary protocol: FAIL-FIRST headings need domain subtitles (C-38); gate headings need binary-question form (C-39). The two criteria prevent vocabulary contamination in both directions -- neither heading type should borrow the other's register.
- **C-40** completes the criterion-ID chain that C-28 begins: C-28 requires at least one criterion-ID reference in a verification scan; C-40 requires systematic `C-NN:` prefix coverage on every checklist item.

**C-34 through C-40 relationships (v12 -- unchanged):**
- C-34 and C-35 are sibling bracket-label criteria: C-34 governs the primary key assignment rule (Stage 1), C-35 governs the citation integrity rule (Stage 5B). An output can pass C-34 (Stage 1 bracket label present) while failing C-35 (Stage 5B bracket label absent). Together they establish that both poles of the FM-[N] lifecycle -- definition and citation -- carry bracket-labeled directives.
- C-36 subsumes C-34 and C-35 by count: a scaffold that passes both C-34 and C-35 plus has a `[BRIDGE COMPLETION COMMAND]` also passes C-36. But C-36 is not automatically satisfied by C-34+C-35: if one of the three canonical bracket elements is missing, C-36 fails even if the other two pass. The count requirement (three or more) is load-bearing.
- C-37 and C-39 govern the two-part gate structure: C-39 requires the gate heading to be binary-question form; C-37 requires a bracket-command directive inside the gate block. An output can pass C-39 while failing C-37 if the remediation command is embedded in the heading rather than in the block body. The two-part structure separates the decision (heading) from the action (bracket command in body).
- C-38 and C-39 together define the heading vocabulary protocol: C-38 governs FAIL-FIRST section headings (they must have domain subtitles); C-39 governs the gate heading (it must be binary-question form). The protocol prevents vocabulary contamination in both directions -- a FAIL-FIRST heading that uses operational vocabulary fails C-38; a gate heading that uses domain framing instead of a bare decision question fails C-39.
- C-40 completes the criterion-ID chain: C-28 requires at least one criterion-ID label in a verification scan; C-40 requires every checklist item to carry a criterion-ID prefix. An output that uses criterion IDs selectively passes C-28 (at least one ID present) but fails C-40 (not every item prefixed). The distinction is systematic coverage vs. presence.

**Evaluator Notes (v13 additions):**
- C-41 and placement specificity: The per-artifact bracket command must appear at or near the bridge artifact's authoring point in the scaffold body -- at the Q3 bridge section or Q4 bridge section -- not only inside the completion gate block. A `[BRIDGE COMPLETION COMMAND]` in the gate block satisfies C-37; a `[BRIDGE Q3 COMMAND]` at the Q3 bridge artifact's authoring section satisfies C-41 for Q3. Both bridge artifacts (Q3 and Q4) must have per-artifact commands for C-41 to pass. Coverage of only one bridge artifact fails C-41 (partial coverage). Label naming is flexible: `[BRIDGE Q3 COMMAND]`, `[Q3 ENFORCEMENT DIRECTIVE]`, `[BRIDGE Q3 COMPLETION RULE]` all satisfy C-41 for Q3 provided the label is bracket-enclosed and co-located with the Q3 artifact authoring point.
- C-42 and the threading vocabulary source: The shared domain-vocabulary word or phrase must be drawn from the inertia domain -- terms identifying the competitor axis subject ("STATUS QUO", "INERTIA THREAT", "DEFAULT OPTION", "INCUMBENT") or their derivatives. Scaffold management vocabulary ("BRIDGE", "GATE", "MANIFEST", "COMMAND") shared across labels does not satisfy C-42 -- management vocabulary is structurally universal, not domain-specific. The threading test: given only the shared vocabulary element across the three bracket labels, can a reader identify this scaffold as a scout-inertia analysis? If yes (because the shared word is a domain-axis term), C-42 passes. The shared word must appear in all three required bracket elements; a partial thread (two of three labels share the word) fails C-42.
- C-43 and the count quantifier vocabulary: The explicit count quantifier must name an exact or bounded count -- "BOTH" (exactly two), "ALL THREE" (exactly three), "BOTH Q3 AND Q4" (explicit enumeration). The indefinite "ALL" without further qualification fails C-43: its extension depends on the artifact count defined elsewhere in the scaffold. Practical test: given the heading interrogative alone, can an author state the expected artifact count as a number? "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" -- count is two. "ALL BRIDGE ARTIFACTS POPULATED?" -- count is indeterminate from the heading alone. If the count is determinable from the heading, C-43 passes; if it requires the gate body, C-43 fails.
- C-44 and the imperative vocabulary register: The action-imperative marker must signal mandatory enforcement. "PASS BEFORE ADVANCING" signals that passing the gate is required to advance. "STOP BEFORE PROCEEDING" signals that the author must stop. "DO NOT ADVANCE UNTIL" signals a conditional prohibition. Vocabulary that describes a structural type without imperativizing fails C-44 -- "BRIDGE COMPLETION GATE", "COMPLETION CHECK", "ARTIFACT REVIEW STEP" describe the gate's type without commanding the author's behavior. The practical test: does the marker tell the author what to DO (pass, stop, wait) rather than what the gate IS (a completion gate, a review step)? If it commands an action, C-44 passes.

**Evaluator Notes (v12 -- unchanged):**
- C-34 and mechanical scannability: The bracket-prefix format (`[A-16 PRIMARY KEY RULE]` or equivalent) is distinguished from parenthetical labels `(A-16)` or inline references "see rule A-16". The bracket enclosure enables whitespace-delimited scanning. A scaffold that labels the primary key rule in any format other than bracket-enclosed fails C-34.
- C-35 and Stage 5B placement: The citation integrity rule label must appear at or before the Stage 5B defeat conditions table, not in a global preamble or after the table. A bracket label in Stage 1 that mentions citation integrity does not satisfy C-35; the label must appear in Stage 5B's enforcement context.
- C-36 and the three-element floor: A scaffold with only C-34 and C-35 has two bracket elements and fails C-36. A scaffold that adds any third bracket-labeled obligation passes C-36 at the count level. C-36 does not require the specific canonical three elements; it requires at least three total.
- C-37 and the heading-vs-body distinction: A command embedded in a heading cannot be independently labeled as a bracket directive. A bracket command inside the block body is independently labelable and satisfies C-36's count requirement. Practical check: does the `[COMMAND]` bracket element appear in the body of the gate block? If it appears only in the heading text, C-37 fails.
- C-38 and the domain vocabulary requirement: The domain subtitle must be drawn from the inertia domain -- terms relating to competitors, failure modes, switching costs, defeat conditions, or workaround analysis. Operational subtitles drawn from artifact-management vocabulary ("ALL ENTRIES POPULATED", "BEFORE PROCEEDING") fail C-38 even if a structural marker is present.
- C-39 and the gate heading form: The binary-question requirement is about answerable form, not about vocabulary. "ALL ARTIFACTS POPULATED?" passes C-39 despite artifact vocabulary because the form is binary. A heading like "COMPLETENESS CHECKPOINT" fails because it names a location, not a decision. The test: can the heading be answered Yes or No without reading the block body?
- C-40 and essential criterion coverage: C-40 requires that C-01 through C-05 each have a checklist entry with a `C-0N:` prefix. A checklist that covers essential criteria by description without ID prefix fails C-40. The minimum is that every essential criterion has a prefixed entry.

---

## Essential Criteria (60 pts total -- all must pass)

### C-01 . Current Workaround Mapped
- **Weight**: essential
- **Category**: coverage
- **Text**: The output describes in concrete detail what teams currently do instead of adopting the feature -- the actual workflow, tools, manual steps, or conventions they rely on today.
- **Pass condition**: At least one specific workaround is named and described with enough detail that a reader can picture the workflow. Generic statements like "teams use manual processes" without specifics do not pass.

### C-02 . Switching Costs Quantified
- **Weight**: essential
- **Category**: correctness
- **Text**: Switching costs are estimated across at least two of the three required dimensions (time, training, disruption). Estimates must be numeric or range-based -- not adjective-only descriptions like "significant" or "moderate."
- **Pass condition**: The output provides at least two quantified cost estimates (e.g., "2-4 hours of migration per project", "1-2 days of team onboarding") or explicit N/A with justification for any omitted dimension.

### C-03 . Inertia Threat Score Set to HIGH
- **Weight**: essential
- **Category**: correctness
- **Text**: The output explicitly assigns an inertia threat score and that score is HIGH (or equivalent -- "critical", "severe"). Per skill spec, this is always HIGH by default. Any output that omits this score or sets it below HIGH without a documented exception fails.
- **Pass condition**: A threat score of HIGH appears explicitly in the output. Downgrading below HIGH requires a written justification; absence of score is an automatic fail.

### C-04 . "Why Inertia Loses" Answered
- **Weight**: essential
- **Category**: depth
- **Text**: The output identifies specific conditions under which the inertia option loses -- the precise scenarios, thresholds, or events that make the current workaround worse than adopting the feature. This is the core deliverable of the skill.
- **Pass condition**: At least two distinct, concrete conditions are named (not restated feature benefits). Each condition must be falsifiable -- a reader could check whether it applies to their situation.

### C-05 . Workaround Failure Modes Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: Per the AMEND directive, the output identifies specific ways the current workaround breaks down -- edge cases, scaling limits, error-prone steps, or known failure scenarios. These are distinct from switching costs (costs are about moving; failure modes are about staying).
- **Pass condition**: At least two specific failure modes of the current workaround are described. "The workaround has limitations" does not pass. "The workaround silently drops events when queue depth exceeds 500" does pass.

---

## Recommended Criteria (30 pts total)

### C-06 . Switching Cost Dimensions Treated Separately
- **Weight**: recommended
- **Category**: depth
- **Text**: Time, training, and disruption are analyzed as separate line items rather than collapsed into a single "switching cost" number.
- **Pass condition**: The output has three distinct cost entries -- one per dimension -- or explicitly explains why a dimension does not apply for this feature context.

### C-07 . Forward-Looking Risk Identified
- **Weight**: recommended
- **Category**: depth
- **Text**: The output identifies at least one risk that grows over time if inertia is maintained -- technical debt accumulation, compounding workaround complexity, or increasing divergence from the supported path.
- **Pass condition**: One forward-looking risk is named with a mechanism (why it compounds) rather than just stated as a concern.

### C-08 . Adoption Trigger Conditions Specified
- **Weight**: recommended
- **Category**: actionability
- **Text**: The output names at least one concrete condition that, when met, should trigger adoption evaluation -- a team size threshold, a failure frequency, a cost milestone, or an event type.
- **Pass condition**: At least one trigger condition is stated in checkable terms ("when the team exceeds 5 developers", "when migration failures exceed one per sprint"). Vague triggers ("when the pain is high enough") do not pass.

---

## Aspirational Criteria (`aspirational_pass / 36 * 10` pts)

### C-09 . Competitor Zero Named
- **Weight**: aspirational
- **Category**: specificity

### C-10 . Adoption Cost Amortization Modeled
- **Weight**: aspirational
- **Category**: depth

### C-11 . Failure Mode Actor/Trigger Decomposition
- **Weight**: aspirational
- **Category**: structure

### C-12 . Inertia Threat Deviation Justification Path
- **Weight**: aspirational
- **Category**: correctness

### C-13 . Switching Cost Unit Column
- **Weight**: aspirational
- **Category**: precision

### C-14 . Defeat Condition Cross-Reference to Failure Modes
- **Weight**: aspirational
- **Category**: traceability

### C-15 . Synthesis Step Mandated
- **Weight**: aspirational
- **Category**: completeness

### C-16 . In-Flight Disruption Dimension Present
- **Weight**: aspirational
- **Category**: depth

### C-17 . Minimum Row Count Enforced on FM Inventory
- **Weight**: aspirational
- **Category**: structural completeness

### C-18 . Falsifiability Condition on Defeat Criteria
- **Weight**: aspirational
- **Category**: precision

### C-19 . Citation-Point Check at Section 5
- **Weight**: aspirational
- **Category**: verification

### C-20 . Deviation Justification Required for Below-HIGH Score
- **Weight**: aspirational
- **Category**: correctness

### C-21 . Scaffold-Level "Significant Without a Number Fails" Directive
- **Weight**: aspirational
- **Category**: precision

### C-22 . Structural Requirement Sites Annotated
- **Weight**: aspirational
- **Category**: traceability

### C-23 . Trailing Completeness Checklist Present
- **Weight**: aspirational
- **Category**: verification

### C-24 . Exact-Text Quotation Required for Workaround Name
- **Weight**: aspirational
- **Category**: precision

### C-25 . Per-Site Enforcement Annotations at Every Structural-Requirement Site
- **Weight**: aspirational
- **Category**: structural completeness

### C-26 . Manifest-to-Section-Header Verbatim Identity
- **Weight**: aspirational
- **Category**: precision

### C-27 . Constraint-Before-Site Placement
- **Weight**: aspirational
- **Category**: scaffold topology
- **Text**: Every structural constraint must appear in the scaffold before any site it governs -- at a phase boundary, in a manifest block, or as a preamble -- not co-located with the final section.
- **Pass condition**: The scaffold places all structural constraints before the first section they govern. A constraint that first appears at or after the section it governs does not pass. Co-location with the governed section is an explicit fail.

### C-28 . Criterion-ID-Labeled Verification Scan
- **Weight**: aspirational
- **Category**: auditability
- **Text**: The verification or pre-flight gate names criteria by their assigned IDs (e.g., "C-25:", "[C-05-INT]") rather than by property description alone. An ID-labeled scan creates an audit path by criterion identifier, enabling mechanical completeness checking without content review.
- **Pass condition**: At least one verification step, checklist item, or pre-flight gate references a criterion by its assigned ID. A scan that references the property ("check verbatim alignment") without the ID label does not pass; the ID is load-bearing.

### C-29 . Manifest-Bound Verbatim Directive
- **Weight**: aspirational
- **Category**: co-location
- **Text**: The verbatim-alignment instruction appears inside the manifest block, directly adjacent to the canonical strings the model must copy. Binding the directive to the manifest block eliminates the failure mode where a model knows the verbatim rule but cannot apply it without the reference text in view.
- **Pass condition**: The manifest block contains both the canonical strings and an instruction to reproduce them character-for-character (or equivalent verbatim directive). A verbatim directive in a preamble or global-rules section that is separate from the manifest does not pass.

### C-30 . Manifest Scope Annotation
- **Weight**: aspirational
- **Category**: scaffold navigability
- **Text**: Each manifest entry explicitly names the section(s) or site(s) it governs, making the constraint graph navigable from the manifest alone.
- **Pass condition**: Each entry in the manifest block includes an explicit statement of the sections or sites it governs. Manifest entries that state a constraint rule without naming their governed targets do not pass.

### C-31 . Triple-Constraint Manifest Convergence
- **Weight**: aspirational
- **Category**: unified enforcement
- **Text**: A single manifest block simultaneously satisfies C-27 (placed before all governed sites), C-28 (entries use criterion-ID labels), and C-29 (verbatim-alignment directive co-located with canonical reference strings). Satisfying each criterion at a different document location does not pass.
- **Pass condition**: One identifiable manifest block in the scaffold (1) appears before all sections it governs, (2) labels at least one entry with a criterion ID, and (3) contains a verbatim-alignment directive adjacent to the canonical strings it governs. C-31 requires the reference strings themselves to reside in the manifest.

### C-32 . Format-Declared Manifest Pattern
- **Weight**: aspirational
- **Category**: manifest legibility
- **Text**: The manifest block carries an explicit format declaration in its heading or opening label (e.g., "SCAFFOLD MANIFEST TABLE", "STRUCTURAL MANIFEST -- PROSE FORMAT"). The chosen format is declared explicitly and applied consistently to every entry in the block.
- **Pass condition**: The manifest block has a heading or label that explicitly states its format type. The declared format is applied consistently to all entries -- no mixed-format blocks. An unlabeled manifest block fails C-32 regardless of internal consistency.

### C-33 . Canonical String Manifest Residency
- **Weight**: aspirational
- **Category**: manifest completeness
- **Text**: Every verbatim reference string that defines a pass/fail condition for any constraint is canonically defined inside the manifest block. Governed sections may quote or apply these strings but do not originate them. C-33 subsumes C-29's requirement and adds the primary-definition obligation.
- **Pass condition**: Given only the manifest block, an auditor can state verbatim every string that constitutes a passing or failing output condition for every constraint entry. If retrieving any pass/fail string requires opening a governed section, C-33 fails. Governed sections that define strings the manifest does not contain are an automatic fail.

### C-34 . Primary Key Rule Label
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold carries a bracket-enclosed label (`[A-16 PRIMARY KEY RULE]` or equivalent) at the directive governing FM-[N] primary key assignment in the FM Inventory stage. The bracket enclosure makes the directive mechanically scannable. Bracket-suffix form (`STATUS QUO LOCK RULE [A-16]`) confirmed valid by R12 V-02.
- **Pass condition**: The scaffold contains a bracket-enclosed label at the FM-[N] assignment directive in the stage where failure modes are inventoried. Label format: bracket-prefix `[LABEL-NAME]` or bracket-suffix `DESCRIPTOR [ID]`. The label must be adjacent to the assignment rule, not in a preamble topographically separated from the FM Inventory stage. A rule stated as prose without any bracket-enclosed element fails C-34.

### C-35 . Citation Integrity Rule Label
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold carries a bracket-enclosed label (`[A-19 CITATION INTEGRITY RULE]` or equivalent) at the directive governing FM-[N] citation integrity in the defeat conditions stage. Bracket-suffix form (`STATUS QUO CITATION RULE [A-19]`) confirmed valid by R12 V-02.
- **Pass condition**: The scaffold contains a bracket-enclosed label at the citation-integrity directive in the defeat conditions stage. The label must appear at or before the first defeat condition entry, not after. A bracket label for citation integrity placed in a global preamble rather than in the defeat conditions stage fails C-35.

### C-36 . Minimum Bracket-Prefix Label Count
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The scaffold contains at least three distinct bracket-enclosed labeled elements across its full extent. R11's V-01 confirmed three canonical elements: `[A-16 PRIMARY KEY RULE]`, `[A-19 CITATION INTEGRITY RULE]`, `[BRIDGE COMPLETION COMMAND]`. R12's V-05 exceeded the minimum with five elements including per-artifact commands. Three or more labeled elements establish that bracket-labeling is a convention rather than an isolated occurrence. Bracket-suffix form counts toward the total (confirmed by R12 V-02).
- **Pass condition**: Count distinct bracket-enclosed elements across the full scaffold. Three or more distinct elements, each governing a different structural obligation, passes C-36. Two or fewer elements fail. The three elements need not be the canonical R11 examples.

### C-37 . Completion Command Inside Gate Block
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The completeness gate block contains an explicit bracket-labeled command directive in its body -- below or after the binary gate question -- specifying the remediation action when the gate condition fails. R11 distinguished two placements: V-01 places `[BRIDGE COMPLETION COMMAND]` inside the gate block body (PASS); V-02 embeds the command in the gate heading (PARTIAL). The inside-block placement keeps the decision (heading) separated from the action (body directive).
- **Pass condition**: The completeness gate block contains a bracket-enclosed command element (`[COMMAND-NAME]`) in its body text, after the binary gate question. A command that appears only inside the heading text fails C-37. A command present in the body without bracket enclosure fails C-37 because it is not independently labelable.

### C-38 . FAIL-FIRST Domain Subtitle
- **Weight**: aspirational
- **Category**: heading vocabulary
- **Text**: Every FAIL-FIRST section heading in the scaffold carries two components: (1) a structural role marker ("FAIL-FIRST DECLARATION" or equivalent) that identifies the section's function, and (2) a domain-frame subtitle phrase that names the content in inertia-domain terms. R11's V-01 fails: its FAIL-FIRST heading carries only the structural marker with no domain subtitle. R11's V-02 passes: "FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR" carries both components.
- **Pass condition**: Every FAIL-FIRST section heading contains a domain-frame subtitle phrase drawn from inertia domain vocabulary: competitor naming, failure modes, switching costs, defeat conditions, or equivalent inertia-domain concepts. A heading with only a structural marker ("FAIL-FIRST DECLARATION") fails. A heading with an operational subtitle ("FAIL-FIRST: ALL ENTRIES REQUIRED") fails. A heading with a domain subtitle ("FAIL-FIRST DECLARATION -- THE WORKAROUND FAILURE INVENTORY") passes.

### C-39 . Binary-Question Gate Heading
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The completeness gate heading is explicitly binary Yes/No-answerable -- a question form that names a decision point rather than describing a location or task. An operational label like "COMPLETENESS CHECK" names a section type but does not name a decision; a binary question like "ALL ARTIFACTS POPULATED?" names a decision with exactly two outcomes.
- **Pass condition**: The completeness gate heading contains a binary question answerable Yes or No without reading the block body. The question can use any vocabulary (artifact-management or domain) provided the form is binary. A heading that states a task, a warning, or a location label fails C-39.

### C-40 . Criterion-ID Prefixes on Checklist Items
- **Weight**: aspirational
- **Category**: audit traceability
- **Text**: Every item in the trailing completeness checklist carries its criterion ID as a `C-NN:` prefix. R11's V-01 passes: Stage 6 items carry "C-01:" through "C-05:" prefixes. V-03 is the explicit control variation -- same lifecycle structure but no C-0N: prefixes on items. The ID prefix makes the checklist mechanically auditable by criterion.
- **Pass condition**: Every item in the trailing completeness checklist is prefixed with its criterion ID in `C-NN:` format. At minimum, the five essential criteria (C-01 through C-05) must each have a prefixed entry. A checklist with ID prefixes on some items but not all fails C-40.

### C-41 . Per-Artifact Bridge Command Labels
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: Each named bridge artifact (Q3 and Q4) carries its own bracket-labeled command directive at or near its authoring point in the scaffold body, separate from the gate-level completion command that C-37 requires. R12's V-05 demonstrated `[BRIDGE Q3 COMMAND]` and `[BRIDGE Q4 COMMAND]` as per-artifact directives, independent of the gate-block `[BRIDGE COMPLETION COMMAND]`. Per-artifact commands enforce the authoring obligation at the point of authoring -- the author encounters the directive when filling in the artifact, not only when reaching the completion gate. The gate-level command (C-37) enforces at the gating decision point; the per-artifact commands (C-41) enforce at each artifact's definition site. The two levels are complementary and non-overlapping.
- **Pass condition**: The scaffold contains at least two bracket-enclosed command directives at the individual artifact level -- one co-located with the Q3 bridge artifact's authoring section and one co-located with the Q4 bridge artifact's authoring section. These must be distinct from the gate-block command required by C-37. Label naming is flexible: `[BRIDGE Q3 COMMAND]`, `[Q3 COMPLETION DIRECTIVE]`, `[BRIDGE Q3 ENFORCEMENT RULE]` all satisfy C-41 for Q3 provided the label is bracket-enclosed and positioned at the Q3 artifact authoring site. Coverage of only one bridge artifact (Q3 or Q4 but not both) fails C-41.

### C-42 . Bracket-Label Vocabulary Threading
- **Weight**: aspirational
- **Category**: bracket-label convention
- **Text**: The three required bracket-labeled elements (primary key rule from C-34, citation integrity rule from C-35, completion command from C-37) share a common domain-vocabulary word or phrase drawn from inertia-domain axis terms. R12's V-02 demonstrated vocabulary threading with "STATUS QUO" appearing in all three bracket elements: `STATUS QUO LOCK RULE [A-16]`, `STATUS QUO CITATION RULE [A-19]`, `[STATUS QUO BRIDGE COMMAND]`. The threading makes the labeling system recognizable as a domain-coherent set -- a reader encountering any one bracket label can identify the axis vocabulary that governs all three.
- **Pass condition**: Identify the three required bracket elements (C-34, C-35, C-37 sources). Verify that a single domain-vocabulary word or phrase appears in all three label texts. The shared word must be drawn from inertia-axis vocabulary: terms naming the competitor axis subject ("STATUS QUO", "INERTIA THREAT", "DEFAULT OPTION", "INCUMBENT", "UNNAMED COMPETITOR") or their derivatives. Scaffold management vocabulary ("BRIDGE", "GATE", "MANIFEST", "COMMAND") shared across labels does not satisfy C-42 -- management vocabulary is structurally universal, not domain-specific. Partial threading (shared word in two of three labels) fails C-42.

### C-43 . Explicit Count Quantifier in Gate Heading Interrogative
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The gate heading's binary question carries an explicit count quantifier that names the exact expected artifact count, enabling an author to determine the completion target from the heading alone without reading the gate block body. R12's V-04 demonstrated "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" -- "BOTH" is an explicit dual-count quantifier. Compare V-01's "ALL BRIDGE ARTIFACTS POPULATED?" -- "ALL" is a relative quantifier whose extension requires reading the gate block or artifact inventory. Both pass C-39 (binary question form); only V-04 passes C-43 (explicit count).
- **Pass condition**: The gate heading interrogative contains a determiner or numeral that names an exact or bounded count: "BOTH" (exactly two), "ALL THREE" (exactly three), "BOTH Q3 AND Q4" (explicit enumeration). Open-ended quantifiers that require external reference to determine the count fail C-43: "ALL" without specification, "EVERY", "EACH" without an accompanying count. The count must be determinable from the heading string alone -- if the author must consult the gate block body or the artifact inventory to know the expected count, C-43 fails. A heading that already satisfies C-43 necessarily satisfies C-39.

### C-44 . Action-Imperative Gate Structural Marker
- **Weight**: aspirational
- **Category**: gate block structure
- **Text**: The gate heading's structural marker component -- the portion before the `--` separator -- uses action-imperative vocabulary that signals the gate as a mandatory enforcement stop, not a descriptive organizational delimiter. R12's V-05 demonstrated "PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" where "PASS BEFORE ADVANCING" commands the author's behavior. Compare V-01's "BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS POPULATED?" where "BRIDGE COMPLETION GATE" describes the gate's type. Both pass C-39 (binary question in the second component); only V-05 passes C-44 (imperative vocabulary in the first component). The imperative marker makes the gate's enforcement semantics unambiguous at the heading level.
- **Pass condition**: The gate heading's structural marker (before `--` separator, or the leading clause of the heading if no `--` separator is used) is drawn from action-imperative vocabulary: phrases that command the author to perform a specific action as a condition of proceeding ("PASS BEFORE ADVANCING", "STOP BEFORE PROCEEDING", "DO NOT ADVANCE UNTIL", "REQUIRED STOP"). Vocabulary that names the gate's type or content without commanding an action fails C-44: "BRIDGE COMPLETION GATE", "ARTIFACT REVIEW STEP", "COMPLETION CHECKPOINT", "VERIFICATION BLOCK". The test: does the marker tell the author what TO DO (pass, stop, wait) or what the gate IS (a completion gate, a review step)? If it commands an action, C-44 passes; if it names a type, C-44 fails.
