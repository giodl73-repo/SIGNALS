Written to `simulations/quest/rubrics/listen-support-rubric-v7-2026-03-14.md`.

---

**What changed v6 -> v7:**

Three new aspirational criteria from Round 6 above-ceiling signals:

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-24 | Summary Table Collective-Distribution Audit | C-20 | V-02, V-04 |
| C-25 | Action-Verb Third-Person Prohibition | C-21 | V-03, V-05 |
| C-26 | Explicit Mode-Switch Dual-Pass Delimiter | C-23 | V-05 only |

**Tier restructure:** Aspirational 15 / 75 pts -> 18 / 90 pts. Total ceiling **165 -> 180**.

**New progression chains added:**
- `C-20 -> C-24`: row-level pre-commitment -> table-level collective-distribution gate with correction loop
- `C-21 -> C-25`: noun-form prohibition -> verb-subject collocation prohibition (closes the "the SRE ran..." failure mode)
- `C-23 -> C-26`: labeled dual-pass -> mode-switch delimiter enforcing structural independence at the instruction level

The key structural logic for each:
- **C-24** catches what C-20 cannot: a table where every row is individually valid but the collective is all-P1 or all-how-to
- **C-25** catches what C-21 cannot: "the SRE ran kubectl" is third-person through verb construction, not noun reference
- **C-26** catches what C-23 cannot: PASS 1 / PASS 2 headers can be written as a single semantic block; "END OF PASS 1. Switch to [mode] mode." cannot
egory values; (3) Volume distribution -- all three volume levels represented; (4) Phase-character compliance -- each row's volume and severity match the phase map. A per-row-valid table can still be collectively biased (all eight rows P1, zero P3, or all categories "how-to") without any row-level violation. The collective audit is a separate gate with a self-enforcing correction requirement: "If any constraint fails, correct the summary table and re-run the audit before proceeding. Name the correction made." V-02 and V-04 satisfy C-24; V-01, V-03, V-05 fail it.

**C-25 -- Action-Verb Third-Person Prohibition** (5 pts, behavior)
Tightens C-21. C-21 prohibits named-role titles as standalone noun references ("the SRE", "the PM"); C-25 extends the prohibition to verb-subject collocations: "Prohibited verb-subject forms: 'the SRE ran', 'the PM reviewed', 'the engineer observed', 'the C-07 clicked', 'the Support agent opened', or any construction where a role title precedes a verb." The failure mode C-21 permits: a model in performance mode can write "The SRE ran kubectl and observed pod thrashing" -- no generic pronoun, no standalone role noun, but entirely third-person through verb construction. Enumerating prohibited collocations makes verb-subject violations grep-checkable by role title + verb pairing. "Every action in this ticket was taken by 'I'." closes the verb-form analyst-stance failure mode C-21 leaves open. V-03 and V-05 satisfy C-25; V-01, V-02, V-04 fail it.

**C-26 -- Explicit Mode-Switch Dual-Pass Delimiter** (5 pts, depth)
Tightens C-23. C-23 passes when both verification passes are present and explicitly labeled; C-26 requires that the boundary between the two passes carries an explicit mode-switch delimiter: "END OF PASS 1. Switch to frontmatter verification mode." (or equivalent). The failure mode labeled-sections permit: a model can apply PASS 1 / PASS 2 section headers while writing semantically unified content that spans both, satisfying C-23 structurally while maintaining a single conceptual block. An explicit mode-switch instruction makes single-block compliance impossible -- the declared stance change between passes is itself a structural constraint; a model cannot continue Pass 1 checks after "END OF PASS 1. Switch to [mode] mode." without violating the delimiter. C-23 passes with explicit labels on both passes; C-26 passes only when the boundary additionally carries an explicit "END OF PASS N. Switch to [mode] mode." delimiter naming both the mode exited and the mode entered. V-05 satisfies C-26; V-01 through V-04 fail it.

**Tier restructure:**
- Aspirational: 15 criteria / 75 pts -> 18 criteria / 90 pts
- Total ceiling: 165 -> 180

**Criterion progression chains:**
- Depth: C-02 (compliance) -> C-20 (pre-commitment table) -> C-24 (collective-distribution audit)
- Behavior: C-19 (generic third-person prohibition) -> C-21 (named-role prohibition) -> C-25 (verb-subject collocation prohibition)
- Depth: C-13 (gate) -> C-15 (table) -> C-17 (gap-bridged) -> C-23 (dual-pass) -> C-26 (mode-switch delimiter)

**Relationship to prior criterion pairs:**
- C-20 (vocabulary pre-commitment) -> C-24 (collective-distribution audit): moves distribution verification from per-row validity to table-level collective constraint before a single card body is written
- C-21 (named-role noun prohibition) -> C-25 (verb-subject collocation prohibition): closes the role-title verb-construction analyst-stance failure mode that noun-form prohibition leaves open
- C-23 (dual-pass with explicit labels) -> C-26 (mode-switch delimiter): replaces assumption of structural independence from section headers with enforced stance change between passes

---

## Essential Criteria (60 pts total -- output fails below this line)

### C-01 -- All Five Ticket Fields Present
- **Weight**: essential
- **Points**: 12
- **Category**: correctness
- **Text**: Every predicted ticket contains all five required fields: title, category, persona most likely to file, predicted volume, and severity.
- **Pass condition**: Zero tickets are missing any of the five fields. A ticket with a blank or "N/A" field fails this criterion.

---

### C-02 -- Controlled Vocabulary Compliance
- **Weight**: essential
- **Points**: 12
- **Category**: correctness
- **Text**: Category values are drawn exclusively from {how-to, bug, feature-request, config, integration}. Severity values are drawn exclusively from {P0, P1, P2, P3}. Volume values are drawn exclusively from {high, medium, low}.
- **Pass condition**: No ticket uses an out-of-vocabulary value in any controlled field. Synonyms or variants (e.g., "configuration", "High", "blocker") do not pass.

---

### C-03 -- Persona Grounding in Stock Roles
- **Weight**: essential
- **Points**: 12
- **Category**: correctness
- **Text**: Every ticket's "persona most likely to file" is drawn from the stock role set: {Support, SRE, PM, UX, C-01 through C-12}. The sample ticket body is written in that persona's voice (vocabulary, concerns, and framing appropriate to the role).
- **Pass condition**: All ticket personas are valid stock roles, AND each sample body is written in first person from that persona's perspective with role-appropriate language. A generic body not tied to the named persona fails.

---

### C-04 -- Gap Analysis Present and Structured
- **Weight**: essential
- **Points**: 12
- **Category**: coverage
- **Text**: The output contains a gap analysis section with three explicitly labeled sub-sections: doc gaps, design gaps, and operational gaps. Each sub-section contains at least one identified gap.
- **Pass condition**: All three gap sub-sections exist and are non-empty. A single combined "gaps" section without sub-categorization does not pass.

---

### C-05 -- Minimum Ticket Count and Category Spread
- **Weight**: essential
- **Points**: 12
- **Category**: coverage
- **Text**: The output predicts at least five distinct tickets, and at least three of the five allowed categories (how-to, bug, feature-request, config, integration) are represented across the ticket set.
- **Pass condition**: Ticket count >= 5 AND at least 3 distinct category values present. An output with five how-to tickets and nothing else does not pass.

---

## Recommended Criteria (30 pts total -- output is better with these)

### C-06 -- Severity Calibration is Defensible
- **Weight**: recommended
- **Points**: 10
- **Category**: depth
- **Text**: Severity assignments are internally consistent and defensible. P0/P1 tickets describe scenarios where the feature is broken or inaccessible (not cosmetic or nice-to-have). P2/P3 tickets reflect lower-impact or workaround-available situations. The distribution is not uniformly P2 (severity washing).
- **Pass condition**: No P0/P1 ticket describes a cosmetic or low-impact issue, AND no obvious blocker is rated P2/P3, AND at least two different severity levels appear in the ticket set.

---

### C-07 -- Volume Ratings are Differentiated and Reasoned
- **Weight**: recommended
- **Points**: 10
- **Category**: depth
- **Text**: High/medium/low volume ratings vary across the ticket set (not all tickets are "high"). The relative assignments are plausible given the ticket category and the persona filing them (e.g., a configuration ticket from SRE would plausibly be lower volume than a how-to ticket from C-01 through C-12).
- **Pass condition**: All three volume levels appear, OR two levels appear with an explicit statement of why one level is absent. Uniform volume across all tickets fails.

---

### C-08 -- Sample Ticket Bodies Are Persona-Authentic
- **Weight**: recommended
- **Points**: 10
- **Category**: behavior
- **Text**: Each sample ticket body reads like it was written by the named persona. SRE tickets use operational/infra language. PM tickets reference roadmap, user impact, or metrics. Customer persona tickets (C-01 through C-12) reflect that persona's domain, role, and pain. Generic "I have a problem with X" bodies are insufficient.
- **Pass condition**: At least 75% of sample bodies contain role-specific vocabulary, framing, or concerns that would not fit a different persona. A body that reads identically well for any persona fails.

---

## Aspirational Criteria (90 pts total -- raises the bar above 90)

### C-09 -- Cross-Ticket Pattern Recognition
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The output identifies a systemic pattern across multiple predicted tickets (e.g., "Five of the eight tickets trace to missing onboarding docs for the config namespace" or "Three tickets suggest the error message for auth failure is ambiguous"). This pattern is stated explicitly and connected to specific tickets by ID or title.
- **Pass condition**: At least one named cross-ticket pattern with explicit ticket references is present in the output.

---

### C-10 -- Prioritized Pre-Launch Gap Closing Signal
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The gap analysis concludes with a ranked or prioritized recommendation for which gaps to close before launch (not just a list). The ranking is tied to the severity and volume of tickets that the gap would prevent.
- **Pass condition**: The gap analysis section includes an explicit prioritization statement (e.g., "Close doc gap X first -- it drives the three high-volume P1 tickets") rather than an unordered list.

---

### C-11 -- STATUS QUO Scenario Grounding
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The output establishes a concrete current-state scenario before predicting tickets: what users are doing today, what workarounds exist, and where friction is highest. Volume ratings and ticket bodies reference this baseline. A high-friction STATUS QUO should produce high-volume early tickets; a smooth onboarding baseline should not. This grounding mechanism prevents both volume washing (C-07) and generic bodies (C-08) by giving the model a specific scenario to reason from rather than generating in the abstract.
- **Pass condition**: A STATUS QUO or equivalent current-state section exists, AND at least two ticket volume ratings or two ticket body framings are explicitly traceable to the described scenario. A STATUS QUO section that is not referenced anywhere in the ticket content does not pass.
- **Round 1 evidence**: V-05 achieved 10/10 on C-07 and 10/10 on C-08 entirely through STATUS QUO grounding. V-04 (no STATUS QUO) scored 9/10 on each -- the missing point in both cases was the absence of scenario-specific anchoring.

---

### C-12 -- Pattern Consequence Framing
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: Each identified cross-ticket pattern includes an explicit forward-looking consequence statement explaining what remains broken or costly if the pattern is not addressed (e.g., "Not closing this means: all Phase 1 adopters hit this wall before completing first setup"). This moves the output from diagnosis ("these tickets share a root cause") to impact framing ("here is what staying broken costs"). The consequence statement must be specific to the named pattern -- a generic "this will cause user confusion" does not pass.
- **Pass condition**: At least one cross-ticket pattern includes a named, specific consequence statement tied to user impact, adoption friction, or operational cost. A pattern that stops at root cause identification without a forward-looking consequence does not pass.
- **Round 1 evidence**: V-05's C-09 mechanism required "Not closing this means:" per pattern, producing the strongest cross-ticket pattern section in Round 1. V-04's C-09 required only Name/Tickets/Root cause -- no consequence framing -- and scored identically on C-09 but produced a shallower pattern section overall.

---

### C-13 -- Self-Verification Coverage Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The output includes an explicit post-generation self-check section that enumerates STATUS QUO traces by ticket before finalizing. The enumeration names specific tickets (by ID or title) and states which STATUS QUO element each references. This structural gate catches aggregate failures that per-card grounding instructions alone miss: a model following card-level instructions may produce individual tickets that mention STATUS QUO but fail to achieve the required distribution across the ticket set. The gate forces verification that the traces actually exist before the output is complete. A card-level instruction to reference STATUS QUO is necessary but not sufficient for this criterion.
- **Pass condition**: A coverage check or equivalent enumeration explicitly lists at least two ticket-to-STATUS-QUO traces by ticket identifier and scenario element. A summary statement ("all tickets reference STATUS QUO") without ticket-level enumeration does not pass.
- **Round 2 evidence**: V-01 and V-02 (COVERAGE CHECKS gate with enumerated traces) score 5/5 on C-11. V-03 and V-04 (card-level STATUS QUO instructions, no gate) score 4/5 on C-11. The gate is the load-bearing mechanism separating full from partial C-11 compliance.

---

### C-14 -- Structurally Enforced Consequence Specificity
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: Each cross-ticket pattern consequence is decomposed into structurally separate named components -- each component requiring a pattern-specific value that cannot be satisfied by a generic statement. The canonical three-part structure: (1) Affected segment -- a named role or cohort, not "users"; (2) Day-N scenario -- one specific event tied to this pattern, not "this will cause confusion"; (3) Adoption cost -- one sentence quantifying or qualifying the friction for the named segment. When each part is its own field, no single generic sentence can satisfy all three simultaneously: "this will cause user confusion" fails segment (names no cohort), fails scenario (names no event), and fails cost (quantifies nothing). A prohibition note appended to a single-sentence consequence field is not structural decomposition.
- **Pass condition**: At least one cross-ticket pattern consequence is decomposed into at least two structurally separate named fields, each requiring pattern-specific content. A single-sentence consequence -- even one with explicit specificity guidance -- does not pass.
- **Round 2 evidence**: V-03/V-04/V-05 (three structurally separate consequence fields) score 5/5 on C-12. V-01 (single sentence, named three components in instruction) scores 4/5. V-02 (single sentence, two named components) scores 3/5. Structural separation into fields -- not instruction guidance toward specificity -- is what makes generic statements impossible.

---

### C-15 -- Table-Form Coverage Enumeration
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The self-verification coverage gate (C-13) uses a table with one row per ticket -- not a text-format enumeration with ticket IDs embedded in prose. This distinction is load-bearing: a text-format check with an example permits a model to write "T-01 and T-02 both trace to X. Count: 2. Passes." -- two tickets collapsed into one sentence, with IDs present but per-ticket independence lost. A table row per ticket makes row count self-verifying without reading the text: the scorer counts rows. Single-sentence summaries spanning multiple tickets are structurally impossible in table form. C-13 passes with any enumeration that names ticket IDs; C-15 passes only when the enumeration is a table, with each ticket occupying its own row and its STATUS QUO element stated in a separate column.
- **Pass condition**: The coverage enumeration is a formatted table (not inline prose), with at least one row per ticket and at least two columns (ticket ID / STATUS QUO element traced). An enumeration that names ticket IDs in sentence form -- even with an example showing the desired format -- does not pass.
- **Round 3 evidence**: V-01 (table format) scores C-13 PASS/5 and satisfies C-15. V-02 (text-format check with example) scores C-13 PARTIAL/4 and fails C-15. The table eliminates the paragraph-collapse failure mode that the text-format check permits; row count is checkable without parsing sentence structure.

---

### C-16 -- Container-Free Consequence Field Format
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The consequence decomposition required by C-14 uses flat top-level fields with no parent "Consequence:" container -- each consequence component is a sibling-level field alongside "Pattern name:" and "Pattern root cause:", not a nested bullet under a parent label. This distinction is load-bearing: nested bullets under a "Consequence:" parent create a semantic grouping that allows a model to treat the three components as a single "Consequence section." The parent label anchors a generic response at the container level while appearing to satisfy each bullet. Flat sibling-level fields carry no parent anchor; each field is independently checkable without reference to the others, and no container exists for a generic sentence to hide behind. C-14 passes when components are in structurally separate named fields (including nested); C-16 passes only when those fields are flat top-level siblings with no parent container.
- **Pass condition**: Each consequence component field ("Consequence -- Affected segment:", "Consequence -- Day-90 scenario:", "Consequence -- Adoption cost:" or equivalently named variants) appears at the same structural level as other pattern fields with no enclosing "Consequence:" parent label. Nested bullets under a "Consequence:" label do not pass, even when the bullets carry separately labeled content requirements.
- **Round 3 evidence**: V-02 (flat fields, no container) scores C-14 PASS/5 and satisfies C-16. V-01 (three nested bullets under a "Consequence:" parent) scores C-14 PARTIAL/4 and fails C-16. The parent container is the mechanism that permits container-level compliance while allowing component-level genericity; removing it closes the failure mode.

---

### C-17 -- Gap-Bridged Coverage Table
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The coverage table required by C-15 adds a third column linking each ticket row to a named gap from the Gap Analysis (e.g., "Gap traced to: Doc Gap D-02 -- missing namespace config reference"). C-15 verifies that every ticket cites a STATUS QUO element; C-17 extends that to verify that every gap from the Gap Analysis is covered by at least one ticket row. The key failure mode a 2-column table permits: the scorer can confirm ticket-to-STATUS-QUO coverage but cannot identify orphaned gaps -- gaps that appear in the Gap Analysis section but drive no predicted tickets. A "Gap traced to" column makes orphan detection self-verifying: a scorer reads down the gap column and any gap absent from every row is structurally visible without parsing prose. The output should additionally include an explicit no-orphan-gap check confirming that every named gap maps to at least one table row. C-15 passes with a 2-column table; C-17 passes only when a third column bridges ticket traces to named gaps and the no-orphan check is present.
- **Pass condition**: The coverage table has at least three columns (ticket ID / STATUS QUO element / named gap), AND the output includes an explicit statement confirming that no gap from the Gap Analysis is absent from the table. A 2-column table with a separate prose note about gap coverage does not pass.
- **Round 4 evidence**: V-01 and V-04 (3-column gap-bridge tables with no-orphan-gap checks) score C-15 PASS+ and satisfy C-17. V-03 (2-column trace table, no gap column) scores C-15 PASS but fails C-17. The third column closes the gap-orphan failure mode that 2-column tables leave open.

---

### C-18 -- Per-Field Prohibited Sentinel
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: Each flat consequence component field required by C-16 carries an immediately adjacent `Prohibited:` sentinel on the line directly below the field label, naming the generic fill pattern that field is designed to prevent. C-16 removes the parent container anchor, making each field independently checkable; C-18 adds per-field content guards that make the disallowed fill pattern explicit at the field level before the model writes a value. The key failure mode flat-field-without-sentinel permits: a model can write "Phase 1 adopters" as the Affected segment -- technically a cohort name, structurally compliant -- while carrying no content specific to the named pattern. A `Prohibited:` sentinel makes the disallowed form visible: "Prohibited: 'users in general', 'the team', or any unnamed group" eliminates the surface-compliant but content-free answer. The sentinel does not change the field structure (already flat); it adds a content guard at the field level that per-card instructions at any higher scope cannot provide. C-16 passes when consequence fields are flat siblings with no container; C-18 passes only when each flat field additionally carries an immediately adjacent `Prohibited:` sentinel.
- **Pass condition**: At least two consequence component fields each carry an explicitly labeled `Prohibited:` sentinel on the line immediately below the field label, naming one or more disallowed generic fill patterns for that specific field. A `Prohibited:` note appearing once at the pattern level (not per-field) does not pass. A per-field instruction that says "be specific" without naming the prohibited form does not pass.
- **Round 4 evidence**: V-02 and V-04 (per-field Prohibited: sentinels immediately below each flat field) score C-16 PASS+ and satisfy C-18. V-01 (flat fields, no sentinels) scores C-16 PASS but fails C-18. The per-field sentinel closes the surface-compliant generic fill failure mode that flat fields without sentinels leave open.

---

### C-19 -- Performance-Mode Persona Declaration
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The ticket body instruction uses a mode declaration that changes the generation stance for the entire ticket body, not a field instruction that reminds the model to write in first person. The canonical form: "You ARE [persona name]. Do not write 'the user', 'they', or any third-person reference to yourself." A field instruction ("Write in first person as this persona") is a reminder inside the card structure; a mode declaration is a stance shift before the card is read. The distinction is load-bearing: a model reading a first-person instruction at card level can still slip into third-person framing ("the SRE notices the pod is restarting") without violating any card field. A mode declaration prohibiting third-person pronouns makes that failure structurally visible -- a scorer can grep for "the user" or "they" and the violation is immediately apparent. The same mechanism improves C-11 compliance: a persona speaking from within experience ("I spent 40 minutes on step 3 before the token expired") produces a more traceable STATUS QUO element than an analyst describing the persona's experience from outside. C-03 and C-08 pass with any first-person body instruction; C-19 passes only when the mechanism is a mode declaration with an explicit third-person prohibition.
- **Pass condition**: The ticket body section includes a mode declaration (not a field instruction) in the form "You ARE [persona]" or equivalent, AND includes an explicit prohibition on third-person references to the filing persona ("the user", "they", "the SRE", etc.). A card-level instruction to write in first person without a mode declaration and explicit prohibition does not pass.
- **Round 4 evidence**: V-03 and V-05 (performance mode "you ARE the persona" + third-person prohibition) score C-03 PASS+, C-08 PASS+, and C-11 PASS+ simultaneously. V-01, V-02, V-04 (field instructions for first-person voice, no mode declaration) score each of C-03, C-08, C-11 PASS but not PASS+. The mode declaration is the mechanism that shifts all three criteria simultaneously; the third-person prohibition is the structural gate that makes violations checkable without reading for tone.

---

### C-20 -- Vocabulary Pre-Commitment Table
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Before full card bodies are written, the output generates a summary table that locks all controlled-vocabulary values -- Ticket ID, category, persona, volume, and severity -- in column-constrained cells. An explicit instruction follows: "Lock vocabulary values here. Full card bodies follow in Step N." No controlled-vocabulary value (category, volume, severity) is generated for the first time inside a narrative sentence. The failure mode C-02 permits: a model following per-card vocabulary instructions can write "configuration" (valid prose, invalid controlled-vocabulary) inside a body sentence without violating any field structure, and the violation is invisible until card bodies are read one by one. The pre-commitment table makes every controlled-vocabulary value checkable in a single pass before card bodies are read; post-generation vocabulary drift is detectable by comparing table cells to body text. C-02 passes with correct vocabulary values anywhere in the output; C-20 passes only when all controlled-vocabulary values are pre-committed in a table before prose card bodies are written.
- **Pass condition**: A summary table exists before full card body sections, containing at least the columns Ticket ID, category, persona, volume, and severity for every predicted ticket, AND the output includes an explicit instruction locking those values before card bodies. A vocabulary check performed after card bodies are written does not pass.
- **Round 5 evidence**: V-05 (Step 4 summary table pre-commits all controlled-vocabulary values; "Lock vocabulary values here. Full card bodies follow in Step 5.") scores C-02 PASS+. V-01 through V-04 (no pre-commitment table, vocabulary first appears in card bodies) score C-02 PASS but fail C-20. The pre-commitment table makes vocabulary drift detectable without reading sentence-level prose.

---

### C-21 -- Named-Role Third-Person Prohibition
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The performance-mode declaration required by C-19 extends its third-person prohibition to explicitly enumerate named-role forms: "Do not write 'the user', 'they', 'the SRE', 'the PM', 'the engineer', or any named-role title referring to yourself in third person." C-19 prohibits generic pronouns ("the user", "they"); C-21 closes the failure mode C-19 permits: a model in performance mode can substitute named-role titles for generic pronouns while maintaining analyst distance. "The SRE ran the kubectl command and observed pod thrashing" is third-person distancing and carries no first-person experience framing, but it contains neither "the user" nor "they" and therefore satisfies C-19 without violating its structural gate. Enumerating named-role forms in the prohibition makes role-title third-person grep-checkable; a scorer can search for "the SRE", "the PM", etc. and violations are immediately apparent. C-19 passes when the prohibition covers generic pronouns; C-21 passes only when the prohibition additionally enumerates at least two named-role forms by title.
- **Pass condition**: The performance-mode declaration includes an explicit list of prohibited third-person forms that names at least two role titles (e.g., "the SRE", "the PM", "the engineer") in addition to generic forms ("the user", "they"). A prohibition that covers only generic pronouns without naming role titles does not pass.
- **Round 5 evidence**: V-05 ("Do not write 'the user', 'they', 'the SRE', 'the PM'...") scores C-03 PASS+ and closes the named-role analyst-stance failure mode. V-01 through V-04 (prohibitions covering only "the user"/"they") score C-19 PASS but fail C-21. The named-role enumeration closes the substitution path from generic to role-title third-person that C-19 leaves open.

---

### C-22 -- Phase-Character Pre-Constraint Table
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Before tickets are generated, the output produces a phase map table that assigns severity range and volume character per lifecycle phase window (e.g., "Phase 1 -- Day 0-30: severity P0/P1 expected, volume high; Phase 3 -- Day 90+: severity P2/P3 expected, volume medium/low"). C-06 and C-07 pass when severity and volume assignments are defensible and differentiated after generation; C-22 requires that the constraint be pre-generated. The failure mode post-generation calibration permits: a model can assign uniform P2/medium across all tickets and construct prose defenses without any structure making the uniformity implausible before the assignments are written. A phase map table makes uniformity a structural violation before a single ticket is written: a Phase 1 row stating high volume expected makes uniform-medium across all Phase 1 tickets contradict a pre-committed constraint, not merely a prose defense. The phase map is generated before tickets, not derived from them; a phase summary appended after ticket generation does not satisfy this criterion.
- **Pass condition**: A phase map table appears before the ticket generation section, with at least one row per lifecycle phase, and columns assigning severity range (e.g., "P0/P1 expected") and volume character (e.g., "high") per phase. A post-generation phase summary does not pass. An output with no lifecycle phase axis does not pass.
- **Round 5 evidence**: V-01 (phase map table embeds severity character per window -- P1 expects P0/P1, P3 expects P2/P3 -- before ticket cards) scores C-06 PASS+ and C-07 PASS+. V-04 (phase + role combined axis) scores the same. V-02, V-03, V-05 (no phase axis) pass C-06 and C-07 but fail C-22. The phase map makes uniform-medium implausible before generation; post-generation calibration cannot provide the same structural constraint.

---

### C-23 -- Dual-Pass Frontmatter Verification
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The output includes two structurally independent verification passes, each targeting a non-overlapping failure surface. Pass 1 (coverage table): the 3-column gap-bridged table required by C-17, confirming STATUS QUO traces and no orphaned gaps. Pass 2 (frontmatter verify): an explicit confirmation that the pre-committed summary table from C-20 matches every ticket ID, phase label, category, persona, volume, and severity in the full card bodies -- field by field. The two passes have non-overlapping failure surfaces: Pass 1 catches missing STATUS QUO traces and gap orphans; Pass 2 catches post-generation vocabulary drift and phase/persona inconsistencies that the coverage table cannot detect. A model can produce a gap-bridged coverage table that checks out while a card body has quietly drifted from the pre-committed vocabulary (e.g., a category value written correctly in the summary table but as "configuration" in the body); only Pass 2 anchored to the pre-committed values catches this. C-17 passes with one verification pass; C-23 passes only when both passes are present and structurally independent, each explicitly labeled.
- **Pass condition**: The output contains two explicitly labeled verification passes: (1) a 3-column gap-bridged coverage table with no-orphan check, AND (2) a frontmatter verify step that names the pre-committed summary table as the reference and confirms that every Ticket ID, category, persona, volume, and severity in card bodies matches. A single verification step that attempts to cover both surfaces does not pass. An output without a pre-committed summary table (C-20) cannot satisfy C-23.
- **Round 5 evidence**: V-05 (Step 8: two independent verification passes -- (1) 3-column coverage trace table + no-orphan check; (2) "Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category, Persona, Volume, and Severity in the full card bodies") scores C-13 PASS+ and C-17 PASS+. V-01 through V-04 (single verification pass) score C-17 PASS but fail C-23. The second pass catches post-generation vocabulary drift that the coverage table alone cannot detect.

---

### C-24 -- Summary Table Collective-Distribution Audit
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: After the summary table is generated (C-20) and before full card bodies are written, the output runs a collective-distribution audit checking four table-level constraints: (1) Phase distribution -- at least two Phase 1 tickets and one Phase 3 ticket (or equivalent for the feature's lifecycle shape); (2) Category spread -- at least three distinct category values; (3) Volume distribution -- all three volume levels represented; (4) Phase-character compliance -- each row's volume and severity match the phase map from C-22. If any constraint fails, the summary table is corrected and the audit is re-run before proceeding; the correction is explicitly named. C-20 pre-commits row-level vocabulary; a per-row-valid table can still be collectively biased (all eight rows P1, zero P3; all categories "how-to") without any row-level violation. The collective audit catches distribution failures that per-row checks cannot see. The gate is self-enforcing: "If any constraint fails, correct the summary table and re-run the audit before proceeding. Name the correction made." C-20 passes when all controlled-vocabulary values are pre-committed in a table; C-24 passes only when a collective-distribution audit step follows the summary table, checks at least three distribution constraints, and includes a correction gate before body generation.
- **Pass condition**: An explicit collective-distribution audit step appears after the summary table and before body generation, checking at least three of the four named distribution constraints (phase, category, volume, phase-character), AND includes a correction gate requiring table correction and re-audit if any constraint fails. A per-row vocabulary check does not pass. A distribution note appended after body generation does not pass.
- **Round 6 evidence**: V-02 and V-04 (Step 4B collective-distribution audit with four constraints and a "correct the table and re-run" gate before Step 5 body generation) score C-20 PASS+. V-01 (no Step 4B, pre-commitment table only), V-03, V-05 (no collective audit step) score C-20 PASS but fail C-24. The collective audit makes distribution bias detectable before any card body is written; C-20 row-level pre-commitment cannot catch it.

---

### C-25 -- Action-Verb Third-Person Prohibition
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The performance-mode declaration extends its named-role prohibition (C-21) to explicitly enumerate prohibited verb-subject collocations -- constructions where a role title precedes a verb: "Prohibited verb-subject forms: 'the SRE ran', 'the PM reviewed', 'the engineer observed', 'the C-07 clicked', 'the Support agent opened', or any construction where a role title precedes a verb." C-21 prohibits named-role titles as standalone noun references; a model in performance mode can still write "The SRE ran kubectl and observed pod thrashing" -- no generic pronoun, no standalone role noun, but entirely third-person through verb construction. Enumerating prohibited collocations makes verb-subject violations grep-checkable by role title + verb pairing; a scorer can search for "the SRE ran", "the PM reviewed", etc. without parsing for tone. The prohibition is supplemented by an affirmative constraint: "Every action in this ticket was taken by 'I'." -- closing the verb-form analyst-stance failure mode. C-21 passes when the prohibition names at least two role titles as standalone noun forms; C-25 passes only when the prohibition additionally enumerates at least two explicit role+verb collocations.
- **Pass condition**: The performance-mode declaration includes a prohibition that names at least two role+verb collocations (e.g., "the SRE ran", "the PM reviewed") as explicitly prohibited forms, AND includes an affirmative constraint stating that all actions belong to the first-person "I" (or equivalent). A prohibition covering only noun forms without named verb-subject constructions does not pass.
- **Round 6 evidence**: V-03 (body instruction enumerates "the SRE ran", "the PM reviewed", "the engineer observed", "the C-07 clicked", "the Support agent opened" as prohibited; "Every action in this ticket was taken by 'I'.") scores C-21 PASS+. V-05 also satisfies C-25. V-01, V-02, V-04 (noun-form prohibition only) score C-21 PASS but fail C-25. Enumerating verb collocations closes the role-title verb-subject analyst-stance path that noun-form prohibition leaves open.

---

### C-26 -- Explicit Mode-Switch Dual-Pass Delimiter
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Between the two structurally independent verification passes required by C-23, the output includes an explicit mode-switch delimiter: "END OF PASS 1. Switch to frontmatter verification mode." (or equivalent naming both the mode exited and the mode entered). C-23 passes when both passes are explicitly labeled; C-26 requires that the boundary carry an explicit mode-switch instruction. The failure mode labeled-sections permit: a model can apply PASS 1 / PASS 2 section headers while writing semantically unified content that spans both, satisfying C-23 structurally while maintaining a single conceptual block. An explicit mode-switch delimiter makes single-block compliance impossible -- a model cannot continue Pass 1 checks after "END OF PASS 1. Switch to [mode] mode." without violating the delimiter, while labeled headers carry no such enforcement. The structural independence of C-23 is assumed from section labels; the structural independence of C-26 is enforced at the instruction level before Pass 2 begins. C-23 passes with explicitly labeled passes; C-26 passes only when the boundary between the two passes additionally carries an explicit "END OF PASS N. Switch to [mode] mode." delimiter naming both the exited mode and the entered mode.
- **Pass condition**: The output contains an explicit "END OF PASS N." or equivalent delimiter between the two verification passes, naming the mode being exited and the mode being entered (e.g., "END OF PASS 1. Switch to frontmatter verification mode."). Section headers (PASS 1 / PASS 2) without an explicit mode-switch instruction do not pass. An output without C-23 cannot satisfy C-26.
- **Round 6 evidence**: V-05 (explicit "END OF PASS 1. Switch to frontmatter verification mode." delimiter between coverage trace pass and frontmatter verify pass) scores C-23 PASS and satisfies C-26. V-01 through V-04 (single verification block or labeled sections without mode-switch delimiter) fail both C-23 and C-26. The mode-switch delimiter makes the pass boundary structurally self-enforcing; section headers alone leave the single-block compliance path open.

---

## Scoring Summary

| ID   | Text (short)                                   | Weight       | Points | Category    |
|------|------------------------------------------------|--------------|--------|-------------|
| C-01 | All 5 ticket fields present                    | essential    | 12     | correctness |
| C-02 | Controlled vocabulary compliance               | essential    | 12     | correctness |
| C-03 | Persona from stock roles, voiced body          | essential    | 12     | correctness |
| C-04 | Gap analysis with 3 sub-sections               | essential    | 12     | coverage    |
| C-05 | >= 5 tickets, >= 3 category types              | essential    | 12     | coverage    |
| C-06 | Severity calibration defensible                | recommended  | 10     | depth       |
| C-07 | Volume ratings differentiated                  | recommended  | 10     | depth       |
| C-08 | Ticket bodies persona-authentic                | recommended  | 10     | behavior    |
| C-09 | Cross-ticket pattern identified                | aspirational | 5      | depth       |
| C-10 | Pre-launch gap closing prioritized             | aspirational | 5      | behavior    |
| C-11 | STATUS QUO scenario grounding                  | aspirational | 5      | depth       |
| C-12 | Pattern consequence framing                    | aspirational | 5      | behavior    |
| C-13 | Self-verification coverage gate                | aspirational | 5      | depth       |
| C-14 | Structurally enforced consequence fields       | aspirational | 5      | behavior    |
| C-15 | Table-form coverage enumeration                | aspirational | 5      | depth       |
| C-16 | Container-free consequence field format        | aspirational | 5      | behavior    |
| C-17 | Gap-bridged coverage table                     | aspirational | 5      | depth       |
| C-18 | Per-field prohibited sentinel                  | aspirational | 5      | behavior    |
| C-19 | Performance-mode persona declaration           | aspirational | 5      | behavior    |
| C-20 | Vocabulary pre-commitment table                | aspirational | 5      | depth       |
| C-21 | Named-role third-person prohibition            | aspirational | 5      | behavior    |
| C-22 | Phase-character pre-constraint table           | aspirational | 5      | depth       |
| C-23 | Dual-pass frontmatter verification             | aspirational | 5      | depth       |
| C-24 | Summary table collective-distribution audit    | aspirational | 5      | depth       |
| C-25 | Action-verb third-person prohibition           | aspirational | 5      | behavior    |
| C-26 | Explicit mode-switch dual-pass delimiter       | aspirational | 5      | depth       |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 180

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-14 | Added C-11 (STATUS QUO grounding) and C-12 (pattern consequence framing) from Round 1 excellence signals; aspirational tier grows from 10 to 20 pts, total ceiling 110 |
| v3 | 2026-03-14 | Added C-13 (self-verification coverage gate) and C-14 (structurally enforced consequence fields) from Round 2 excellence signals; aspirational tier grows from 20 to 30 pts, total ceiling 120 |
| v4 | 2026-03-14 | Added C-15 (table-form coverage enumeration) and C-16 (container-free consequence field format) from Round 3 excellence signals; aspirational tier grows from 30 to 40 pts, total ceiling 130 |
| v5 | 2026-03-14 | Added C-17 (gap-bridged coverage table), C-18 (per-field prohibited sentinel), and C-19 (performance-mode persona declaration) from Round 4 excellence signals; aspirational tier grows from 40 to 55 pts, total ceiling 145 |
| v6 | 2026-03-14 | Added C-20 (vocabulary pre-commitment table), C-21 (named-role third-person prohibition), C-22 (phase-character pre-constraint table), and C-23 (dual-pass frontmatter verification) from Round 5 excellence signals; aspirational tier grows from 55 to 75 pts, total ceiling 165 |
| v7 | 2026-03-14 | Added C-24 (summary table collective-distribution audit), C-25 (action-verb third-person prohibition), and C-26 (explicit mode-switch dual-pass delimiter) from Round 6 excellence signals; aspirational tier grows from 75 to 90 pts, total ceiling 180 |
