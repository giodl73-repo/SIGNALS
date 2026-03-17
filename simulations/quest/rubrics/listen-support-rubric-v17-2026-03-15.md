**What changed v16 -> v17:** Three new criteria extracted from R17 above-ceiling signals:

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-50 | Sub-Check 3 Table Format | C-48 | V-01, V-04, V-05 |
| C-51 | Phase-2 Barrier Trigger-Event Field | C-49 | V-02, V-04, V-05 |
| C-52 | Per-Template Prohibited Sentinel in Entry 3 | C-49 | V-03, V-05 |

**Tier:** Aspirational 41 / 205 pts -> 44 / 220 pts. Total ceiling **295 -> 310**.

---

**Signal logic:**

- **C-50** (tightens C-48): C-48 requires Sub-check 3 post-body-generation to count Phase 1/2/3 card bodies and compare to the committed distribution, naming any discrepancy as generation-time drift. The failure mode C-48 leaves open: the count comparison can be prose sentences -- "Phase 1 bodies generated: 4. Committed: 4. MATCH. Phase 2 bodies generated: 2. Committed: 2. MATCH." A prose Sub-check 3 permits collapsing phases into a single sentence ("Phase 1 and Phase 2 match, 4 and 2 respectively") with counts embedded rather than independent. A MISMATCH in a prose Sub-check 3 is a clause to extract, not a cell value; a scorer must parse sentence structure to identify which phase has drifted. V-01 replaced prose Sub-check 3 with a 4-column table (Phase / Bodies generated / Committed (Step 5) / Match). In table form, a MISMATCH is a cell value in the Match column -- readable without parsing prose. Row count is self-verifying: three rows for three phases means all phases are independently represented and none can be silently collapsed into a sibling row. The structural independence mechanism is identical to C-15 (which converts prose ticket traces to table rows): table rows make per-phase count comparison checkable by cell value, not by clause extraction. C-48 passes when Sub-check 3 fires post-generation and counts per-phase in any format; C-50 passes only when Sub-check 3 uses a table format with one row per phase and at least four columns (Phase / Bodies generated / Committed / Match).

- **C-51** (tightens C-49): C-49 requires SWITCHING-FRICTION COUNT >= 3 with the third entry structurally constrained to a Phase 2 migration barrier. Pass 2 Sub-check 2 confirms the count and the third-entry type with a YES/NO outcome. The failure mode C-49 leaves open: the Sub-check 2 YES/NO is a declarative self-report. A model confirms "Third entry covers Phase 2 migration barrier: YES" without any field in Entry 3 that makes the Phase-2 character independently falsifiable. A scorer must read Entry 3's prose to evaluate whether the barrier described surfaces after partial commitment or at day one -- the judgment is prose-dependent. V-02 added a `Trigger event:` field to Entry 3. The trigger event is the specific action or moment when the barrier surfaces in a migration workflow. Sub-check 2 requires verbatim quote of the `Trigger event:` field value. A day-one trigger (e.g., "User first opens the feature") in the `Trigger event:` field fails the Phase 2 constraint without requiring prose evaluation -- the trigger event is independently falsifiable by reading one field value. The mechanism converts the declarative YES/NO into an evidence-backed property: Sub-check 2 quotes the trigger event and an evaluator confirms the trigger is post-commitment-specific by reading a single field. C-49 passes when count >= 3 and Sub-check 2 confirms the third-entry type constraint via YES/NO; C-51 passes only when Entry 3 additionally carries a `Trigger event:` field and Sub-check 2 quotes the `Trigger event:` value as the evidence base for the Phase-2 confirmation.

- **C-52** (tightens C-49): C-49 requires the third switching-friction entry to cover a Phase 2 migration barrier with an explicit prohibition on day-one entries. The prohibition is stated in the entry-type constraint instruction -- the instruction block that specifies what the third entry must be. The failure mode C-49 leaves open: the prohibition ("Prohibited: a barrier that day-one users would also encounter") is spatially separated from the content fields of Entry 3 by intervening template structure. A model generating Entry 3's content fields must retrieve the prohibition from a prior instruction block; if that block is contextually distant, the constraint is retrievable but not live at the moment content fields are written. V-03 moved the `Prohibited:` sentinel from the entry-specific guidance section into the Entry 3 template body, field-adjacent above `Expected behavior:`. The sentinel is present at the moment Entry 3's content fields are written -- it does not need to be retrieved from a prior block. The structural mechanism is identical to C-18 (which adds per-field `Prohibited:` sentinels to consequence component fields, making the disallowed form visible at field-write time rather than at instruction-read time). C-49 passes when the prohibition is stated anywhere in the entry-type constraint; C-52 passes only when the `Prohibited:` sentinel appears within the Entry 3 template body itself, field-adjacent to the content fields.

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

## Aspirational Criteria (220 pts total -- raises the bar above 90)

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

### C-27 -- Named Inertia Competitor Phase Framing
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The STATUS QUO section names a specific competing tool by product name (the inertia competitor), and the ticket body instructions are differentiated by adoption-curve phase: early-phase body templates name dual-tool parallelism; late-phase body templates name parity gaps. Three structural properties must hold simultaneously: (1) Tool-name fidelity -- the STATUS QUO names the inertia competitor by product name, producing a grep-checkable string rather than an interpretable phrase like "the legacy system" or "their existing tooling"; (2) Phase-differentiated body templates -- the instructions state two distinct body stances explicitly: a P1/early-phase template naming dual-tool tension ("I still have [tool] open in another tab..."; "I ran [tool] first and then tried this...") and a P3/late-phase template naming a parity gap ("In [tool] I could do X; here I cannot."; "The one thing [tool] had that I need here is..."); (3) Switching-friction gap reframe -- at least one gap sub-section is framed as a switching-friction gap (a specific barrier for users migrating from the named competitor) rather than a generic doc, design, or operational gap. C-11 passes with any concrete current-state description that anchors volume and body content; C-27 passes only when the current-state description names the specific tool, the body templates are phase-differentiated by adoption-curve position, and the gap inventory includes at least one switching-friction gap tied to the named competitor.
- **Pass condition**: (1) The STATUS QUO or equivalent current-state section names at least one specific competing tool by product name (a grep-checkable string, not a generic description); AND (2) the ticket body instructions include at least two explicitly stated phase-differentiated body templates -- one for early-phase (P1-range) tickets naming dual-tool tension with the named competitor, and one for late-phase (P3-range) tickets naming a parity gap with the named competitor; AND (3) the gap analysis includes at least one gap explicitly framed as a switching-friction gap naming the inertia competitor.
- **Round 7 evidence**: V-03 and V-05 (STATUS QUO names the inertia competitor by tool name; body instructions include P1 template: "I still have [tool] open in another tab..." and P3 template: "In [tool] I could do X; here I cannot."; gap analysis contains switching-friction gaps naming the competitor) score C-11 PASS+. V-01, V-02, V-04 (generic STATUS QUO scenario without named competitor) score C-11 PASS but fail C-27.

---

### C-28 -- Phase-Architecture Severity Inference Rule
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The INERTIA or STATUS QUO section states an explicit phase-to-severity inference rule before ticket generation: early-adoption-phase (P1 on the adoption curve) tickets produce lower severity (P2/P3) because adoption friction is expected and a workaround is available; late-adoption-phase (P3) tickets produce higher severity (P0/P1) because parity gaps block established users who have committed to the feature. This rule is stated as a directional architectural constraint derived from the adoption-curve phase, not as a per-ticket calibration note or a post-generation severity defense. C-22 requires a phase map table assigning severity ranges per phase window -- it does not require stating why those ranges apply in that direction. A model can satisfy C-22 by assigning any defensible severity range per phase without the directional logic. The inference rule closes this gap: stating explicitly that early-phase adoption pain yields lower severity (friction is normal and survivable) while late-phase parity gaps yield higher severity (missing capability blocks committed users) makes a directional reversal a structural violation rather than a calibration judgment call. C-22 passes with any phase-severity mapping table; C-28 passes only when the directional inference logic is stated explicitly before any ticket is generated.
- **Pass condition**: The output includes an explicit phase-to-severity inference rule before ticket generation stating (1) that early-adoption-phase tickets produce lower severity (P2/P3) because adoption friction is expected and workable, AND (2) that late-adoption-phase tickets produce higher severity (P0/P1) because parity gaps block established users. A phase map table that lists severity ranges without stating the directional reasoning does not pass.
- **Round 8 evidence**: V-04 ("P1 adoption pain maps to P2/P3 severity -- friction is expected, workaround available; P3 parity gaps map to P1/P0 -- blocking established use") satisfies C-28. V-01, V-02, V-03, V-05 (phase map tables with severity ranges, no directional inference rule) score C-22 PASS but fail C-28.

---

### C-29 -- Dedicated Switching-Friction Gap Sub-Section with Competitor Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The gap analysis includes a dedicated fourth sub-section for switching-friction gaps -- separated from the three sub-sections required by C-04 (doc, design, operational) -- where every gap entry carries a structured per-entry field naming the inertia competitor as the migration source (e.g., "Migrating from: [tool]" or "Competitor barrier: [tool] -- [capability]"). C-27 P3 requires at least one gap framed as a switching-friction gap naming the competitor, anywhere in the gap analysis; C-29 requires that all switching-friction gaps are structurally isolated in their own sub-section with per-entry competitor fields. A dedicated sub-section separates the switching-friction inventory structurally, making the count of competitor-specific gaps enumerable without reading across all three standard sub-sections. Per-entry competitor fields make every entry's migration-source reference grep-checkable by field. The sub-section is explicitly additive: it supplements C-04's three sub-sections, not replaces them.
- **Pass condition**: The gap analysis contains a fourth explicitly labeled sub-section for switching-friction or migration gaps (not merged with doc/design/operational sub-sections), AND each gap entry in that sub-section includes a structured field naming the inertia competitor by product name. The three C-04 sub-sections must remain present and non-empty. A switching-friction gap embedded inside a standard sub-section does not pass.
- **Round 8 evidence**: V-04 (gap analysis: doc / design / operational sub-sections intact; fourth "switching-friction" sub-section with "Migrating from: [tool]" per entry) satisfies C-29. V-01, V-02, V-03, V-05 (switching-friction gaps embedded inside standard sub-sections) score C-27 P3 PASS but fail C-29.

---

### C-30 -- Inference Rule Paraphrase-Before-Proceed Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The step containing the phase-to-severity inference rule required by C-28 includes a structural paraphrase gate: the model must restate the directional inference rule in its own words before any ticket is generated. The canonical form: "In your own words, state the directional rule before proceeding: [model paraphrase here]." C-28 requires that the inference rule be stated as a named imperative constraint before generation; C-30 requires that the model demonstrate conceptual encoding of that rule by paraphrasing it before proceeding. A paraphrase gate requires the model to produce a restatement in different words -- a model cannot paraphrase the inference rule correctly while misunderstanding the directional constraint. The paraphrase also creates an auditable trace: if a model generates a Phase 1 P0 ticket later, the scorer can compare the ticket to the paraphrase the model committed to earlier. C-28 passes when the directional rule is stated as an imperative checkpoint; C-30 passes only when that checkpoint additionally requires the model to produce a paraphrase in its own words before proceeding.
- **Pass condition**: The inference rule step includes an explicit paraphrase instruction requiring the model to restate the directional logic in its own words before proceeding, AND the instruction specifies that a verbatim copy of the rule does not satisfy the gate. A "confirm you understand" instruction without a paraphrase requirement does not pass.
- **Round 9 evidence**: V-05 (STEP 2C: "Paraphrase this rule in your own words before proceeding") satisfies C-30. V-04 (imperative rule + count-and-flag, no paraphrase gate) scores C-28 PASS but fails C-30.

---

### C-31 -- Inference Audit in Dual-Pass Part C
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Pass 2 of the dual-pass verification required by C-23 is extended with a structurally independent Part C (the inference audit) that verifies two properties: (1) C-28 directional compliance -- every Phase 1 ticket has severity P2/P3 and every Phase 3 ticket has severity P0/P1; any directional exception is named explicitly with a one-sentence justification; (2) C-29 sub-section completeness -- the dedicated switching-friction sub-section exists and every entry has the `Migrating from:` competitor field populated. C-23 requires two passes with non-overlapping failure surfaces; C-31 extends to three parts, adding a third failure surface: inference rule compliance and switching-friction field completeness. Part C is named and labeled as its own section. C-23 passes when two labeled passes cover coverage traces and frontmatter drift; C-31 passes only when Pass 2 additionally includes a Part C that explicitly audits C-28 inference compliance and C-29 field completeness, each as named sub-checks, with an exception acknowledgment gate for C-28 violations.
- **Pass condition**: Pass 2 includes an explicitly labeled Part C with two named sub-checks: (1) scan every ticket for C-28 directional compliance with a required exception acknowledgment for any violation; AND (2) confirm the switching-friction sub-section exists and every entry has the competitor field populated. A Part C covering only one sub-check does not pass. An output without C-23 cannot satisfy C-31.
- **Round 9 evidence**: V-05 (Pass 2 Part C: "(1) INFERENCE AUDIT -- scan every ticket: Phase 1 must be P2/P3, Phase 3 must be P0/P1; name any exception. (2) SWITCHING-FRICTION AUDIT -- confirm dedicated sub-section present; confirm every entry has Migrating from: field populated.") satisfies C-31. V-04 (STEP 4B count-and-flag; no C-29 verification) fails C-31.

---

### C-32 -- Decision-Adjacent Paraphrase Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The paraphrase gate required by C-30 fires immediately before the step where severity values are assigned -- not at the step where the inference rule is stated. The canonical placement: Step 4 header carries the gate instruction "Before filling any severity cell, state the inference rule from Step 2C in your own words. Do not fill the table until this line is written: INFERENCE RULE (stated): [...]". C-30 requires a paraphrase gate with "do not proceed" language placed anywhere before ticket generation; C-32 requires that the gate fire at the decision point. The distinction is temporal coupling: when the gate fires at Step 2C, Step 3 prose intervenes before severity assignments and the paraphrase is no longer live generation context when severity decisions are made. When the gate fires at Step 4 header, the paraphrase is the immediately preceding generation. C-30 passes with a paraphrase gate anywhere before ticket generation; C-32 passes only when the gate fires at or immediately before the severity-assignment step.
- **Pass condition**: The paraphrase gate instruction appears at the severity-assignment step, as the immediately preceding instruction before severity cells are filled, AND uses "do not fill" or equivalent language tied to the severity column or table. A paraphrase gate at the rule-statement step does not satisfy C-32 if prose or additional steps intervene before severity assignment. An output without C-30 cannot satisfy C-32.
- **Round 10 evidence**: V-02, V-04, V-05 (paraphrase gate at Step 4 header) satisfy C-32. V-03 (hard gate at STEP 2C) scores C-30 PASS but fails C-32. V-01 (named block at STEP 2C, no gate language) fails both.

---

### C-33 -- Structured Exception Sign-Off Block in Part C
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-31 Part C sub-check (1) requires an explicit exception acknowledgment for any ticket that violates the C-28 directional rule. C-33 requires that the acknowledgment mechanism be a structured EXCEPTION SIGN-OFF BLOCK with at least four named fields per exception: (1) Ticket ID; (2) Phase; (3) Assigned severity; (4) Grounds. The canonical five-field form additionally includes (5) Disposition. A no-exception path must be specified for cases where no tickets violate the directional rule. C-31 passes with any named exception acknowledgment; prose acknowledgment can collapse multiple exceptions into one sentence. A structured block makes each exception independently verifiable: the Grounds field is readable per block without parsing prose. The no-exception path prevents silent omission of the block when no violations are present. C-31 passes with any explicit exception acknowledgment; C-33 passes only when the mechanism is a structured per-ticket block with at least four named fields and the no-exception case is explicitly handled.
- **Pass condition**: Part C sub-check (1) uses a structured EXCEPTION SIGN-OFF BLOCK per exception with at least four named fields (Ticket ID, Phase, Assigned severity, Grounds), AND specifies the no-exception path explicitly. A prose exception acknowledgment does not pass. An output without C-31 cannot satisfy C-33.
- **Round 10 evidence**: V-04 and V-05 (EXCEPTION SIGN-OFF BLOCK with Ticket ID, Phase, Assigned severity, Grounds, Disposition; no-exception path explicitly specified) satisfy C-33. V-01, V-02, V-03 (prose exception acknowledgment) score C-31 PASS but fail C-33.

---

### C-34 -- Paraphrase Double-Gate with Step-4 Recall
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-30 requires one paraphrase gate before ticket generation; C-32 requires it to fire decision-adjacent at Step 4. C-34 requires both: a hard gate at the inference-rule step (STEP 2C) AND a separate paraphrase recall instruction at the decision step (Step 4 header) that explicitly references the earlier paraphrase by step name. The canonical Step 4 recall form: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from Step 2C]" -- the "restate from Step 2C" clause requires the model to retrieve and re-encode its STEP 2C commitment rather than produce a fresh independent paraphrase. The double-gate ensures encoding at the rule step (rule text is live) and re-confirmation at the decision step (severity assignment is live). The explicit cross-reference closes the divergence path: the Step 4 recall cannot silently diverge from the STEP 2C commitment when the gate instruction names the earlier step by number. C-32 passes with one decision-adjacent gate; C-34 passes only when gates fire at both positions, with the Step 4 gate explicitly referencing the STEP 2C paraphrase.
- **Pass condition**: (1) A hard paraphrase gate appears at the rule-statement step with "do not proceed" language and a named paraphrase slot; AND (2) a separate paraphrase recall instruction appears at the severity-assignment step that explicitly references the earlier paraphrase by step name. A single gate at either position does not satisfy C-34. An output without C-30 cannot satisfy C-34.
- **Round 10 evidence**: V-05 (STEP 2C: hard gate with own-words paraphrase slot AND Step 4 header: "INFERENCE RULE (confirmed): [restate from 2C]") satisfies C-34. V-02 and V-04 (Step 4 decision-adjacent gate, no gate at STEP 2C) satisfy C-32 but fail C-34.

---

### C-35 -- Part C Paraphrase Consistency Confirmation
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-34 creates a paraphrase commitment at STEP 2C that is recalled at Step 4; C-31 Part C sub-check (1) audits tickets for C-28 directional compliance. Without C-35, the paraphrase and the audit are structurally parallel but not cross-linked. C-35 requires that after the exception scan in Part C sub-check (1), the audit explicitly quotes the model's own Step 2C paraphrase and states whether the audit result is consistent with that commitment. The canonical form: a Part C closing statement that cites the Step 2C paraphrase verbatim and confirms the scan found no violations inconsistent with the paraphrase (or, if exceptions exist, shows the quoted paraphrase and exception grounds side by side). A model that violated the directional rule cannot pass Part C sub-check (1) without also flagging the contradiction between the audit findings and its own quoted paraphrase. C-31 passes when both Part C sub-checks are present; C-34 passes when the double-gate creates a Step 2C paraphrase commitment; C-35 passes only when Part C sub-check (1) additionally quotes the Step 2C paraphrase and confirms the audit result is consistent with that commitment.
- **Pass condition**: After performing the C-28 directional compliance scan in Part C sub-check (1), the output quotes the model's own paraphrase from Step 2C verbatim and states whether the audit finding is consistent with the quoted paraphrase. A Part C that audits directional compliance without citing the earlier paraphrase does not pass. An output without C-34 cannot satisfy C-35.
- **Round 10 evidence**: V-05 (Part C sub-check 1: EXCEPTION SIGN-OFF BLOCK followed by paraphrase consistency confirmation -- quotes Step 2C paraphrase value, confirms audit result is consistent) satisfies C-35. V-04 (structured block in Part C, no paraphrase citation) satisfies C-33 but fails C-35.

---

### C-36 -- Exception Block Paraphrase-Clause Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The EXCEPTION SIGN-OFF BLOCK required by C-33 includes a sixth named field -- "Paraphrase clause" -- that quotes the Step 2C inference-rule paraphrase governing the directional decision for that exception entry. C-33 requires at least four named fields; C-36 requires the block to additionally include the governing paraphrase so each exception entry cites both what the model committed to (the paraphrase) and why the exception is justified (the Grounds). Without the Paraphrase clause field, the Grounds are evaluated in isolation. The no-exception path is also extended: instead of "No Phase 1 P0/P1 exceptions. PASS.", the no-exception path states "No exceptions. Governing paraphrase clause for Phase 1: [quote]." -- the rule that held is cited, not just the outcome. C-33 passes when the block contains at least four named fields; C-36 passes only when the block additionally contains a Paraphrase clause field, and the no-exception path quotes the governing paraphrase.
- **Pass condition**: Part C sub-check (1) EXCEPTION SIGN-OFF BLOCK includes a named "Paraphrase clause" field per exception entry quoting the Step 2C paraphrase verbatim, AND the no-exception path quotes the governing paraphrase clause rather than stating only a pass/fail outcome. An output without C-33 cannot satisfy C-36.
- **Round 11 evidence**: V-02 and V-05 (six-field exception block including "Paraphrase clause: [quote Step 2C governing rule]"; no-exception path quotes governing paraphrase) satisfy C-36. V-01, V-03, V-04 (five-field block, no-exception path states outcome only) score C-33 PASS but fail C-36.

---

### C-37 -- Step-4 Verbatim Anchor Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate required by C-32 includes a dedicated "Verbatim anchor" field with explicit instruction to quote word for word from the Step 2C commitment rather than restate it. C-34 requires the Step 4 gate to cross-reference Step 2C by step name; C-37 requires that the cross-reference produce a verbatim quote -- not a restatement or compression. A restatement that "references Step 2C" can silently diverge from the STEP 2C text while satisfying C-34's step-name reference requirement. A verbatim quote produces a cross-checkable string: the Step 4 anchor must match the Step 2C text character for character, making divergence detectable by string comparison. The "do not paraphrase" clause in the verbatim anchor instruction makes the required form explicit. C-34 passes when the Step 4 gate references Step 2C by step name; C-37 passes only when the Step 4 gate additionally includes a dedicated verbatim anchor field with "word for word" or "do not paraphrase" language.
- **Pass condition**: The Step 4 gate includes a dedicated verbatim anchor field (labeled "Verbatim anchor", "Verbatim from 2C", or equivalent) with an explicit instruction to quote word for word (or equivalent "do not paraphrase" language) from the Step 2C commitment. A restatement field that references Step 2C by name satisfies C-34 but not C-37. An output without C-34 cannot satisfy C-37.
- **Round 11 evidence**: V-01 ("Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated) block in Step 2C]"), V-04 ("verbatim anchor block" at Step 4), and V-05 ("Verbatim anchor from 2C: [quote word for word, do not paraphrase]") satisfy C-37. V-02 and V-03 (restatement with step-name reference, no verbatim anchor field) satisfy C-34 but fail C-37.

---

### C-38 -- Dual-Field Step-4 Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate requires BOTH an own-words restatement field AND a verbatim anchor field (C-37) simultaneously, with explicit "do not fill the table until both fields are written" language enforcing that neither can be skipped. C-37 requires a verbatim anchor field; C-38 requires the verbatim anchor to coexist with a separate own-words restatement field as a dual requirement. A verbatim-anchor-only gate does not test encoding -- a model can reproduce the Step 2C text verbatim without understanding the directional logic. The dual-field gate forces both simultaneously: the restatement tests encoding, the verbatim anchor enables string-comparison verification. A single field that attempts to satisfy both requirements does not satisfy C-38. C-37 passes when a verbatim anchor field is present; C-38 passes only when both a restatement field AND a verbatim anchor field are present, with explicit "both fields" or "both lines" language making neither optional.
- **Pass condition**: The Step 4 gate contains two separately labeled fields: (1) an own-words restatement field, AND (2) a verbatim anchor field, with an explicit "do not fill the table until both fields/lines are written" instruction. A single field combining both requirements does not pass. An output without C-37 cannot satisfy C-38.
- **Round 11 evidence**: V-01 and V-04 (dual-field gate: INFERENCE RULE (confirmed) + Verbatim from 2C, "Do not fill the table until both lines are written") satisfy C-38. V-05 (verbatim anchor field present, but paired with scope confirmation rather than own-words restatement; no "both fields" language) satisfies C-37 but fails C-38.

---

### C-39 -- Step-4 Every-Assignment Scope Confirmation
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate closes with an explicit scope confirmation statement -- "Confirmation: this rule applies to every severity assignment in the table below" (or equivalent) -- following the paraphrase and/or verbatim anchor fields. C-32 requires a "do not fill" gate immediately before the severity table; C-37 and C-38 require the gate to produce a verbatim anchor and optionally a paired restatement. None of these criteria constrain the scope of the rule as stated at Step 4. The scope confirmation closes this gap: a model that has explicitly stated "this rule applies to every severity assignment in the table below" cannot generate a contradicting ticket later without violating a claim it made in its own words. C-32 passes with a gate that covers the first severity assignment; C-39 passes only when the gate additionally includes an explicit every-assignment scope confirmation covering all table cells.
- **Pass condition**: The Step 4 gate includes an explicit scope confirmation statement ("Confirmation: this rule applies to every severity assignment in the table below", or equivalent) following the paraphrase/anchor fields. A "do not fill" gate without a scope confirmation does not pass. An output without C-32 cannot satisfy C-39.
- **Round 11 evidence**: V-05 (Step 4 gate closes with "Confirmation: this rule applies to every severity assignment in the table below.") satisfies C-39. V-01, V-02, V-03, V-04 (dual-field or single-field gates without scope confirmation) satisfy C-32 and subsets of C-37/C-38 but fail C-39.

---

### C-40 -- Exception Block Verbatim-Clause Instruction
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Paraphrase clause field required by C-36 in the EXCEPTION SIGN-OFF BLOCK carries an explicit "copy it verbatim" or "do not paraphrase" instruction in the field prompt, parallel to the verbatim-instruction requirement C-37 imposed on the Step 4 anchor. C-36 requires the Paraphrase clause field to be present and to cite the governing Step 2C commitment; C-40 requires the field instruction to additionally mandate verbatim reproduction rather than permitting a compressed restatement. Without C-40, the Paraphrase clause field is satisfied by any reasonably faithful restatement -- the model selects wording, and compression is not prohibited. With C-40, the field instruction explicitly states "copy it verbatim from your Step 2C block," making the clause a string-retrieval requirement. C-36 passes when the Paraphrase clause field is present and quotes the governing commitment; C-40 passes only when the field instruction additionally prohibits paraphrase and mandates verbatim reproduction.
- **Pass condition**: The Paraphrase clause field in the EXCEPTION SIGN-OFF BLOCK carries an explicit "copy it verbatim", "do not paraphrase", "word for word", or equivalent instruction within the field prompt itself. A Paraphrase clause field that names the source step without a verbatim instruction does not pass. A verbatim instruction that appears outside the field prompt (e.g., in the block header) does not pass. An output without C-36 cannot satisfy C-40.
- **Round 13 evidence**: V-02 (`Paraphrase clause: [... copy it verbatim from your Step 2C block]`) satisfies C-40. V-04 and V-05 (Paraphrase clause field present, field instruction does not specify verbatim reproduction) satisfy C-36 but fail C-40.

---

### C-41 -- Imperative Dual-Field Gate Language
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The dual-field gate instruction at Step 4 uses imperative prohibition language -- "Do not fill the table until both lines are written" -- rather than declarative requirement language -- "Both need to be filled in before any row." C-38 accepts either form; C-41 requires the imperative prohibition form. The enforcement register distinction is load-bearing: declarative language states a requirement the model is expected to observe, leaving interpretive slack. Imperative prohibition states a structural constraint with no interpretive softening -- non-compliance is a direct structural violation detectable at the sentence level. A scorer can grep for "Do not fill" and confirm the imperative prohibition without reading the full gate instruction. C-38 passes with either declarative or imperative gate language; C-41 passes only when the gate uses "Do not fill" imperative prohibition form or equivalent construction with a negated imperative verb.
- **Pass condition**: The Step 4 dual-field gate instruction uses imperative prohibition form with a negated imperative verb directly governing table-filling ("Do not fill the table until both lines are written", "Do not populate any row until both fields are complete", or equivalent). A declarative form ("Both need to be filled in before any row") does not pass, even if it contains the words "before you fill." An output without C-38 cannot satisfy C-41.
- **Round 13 evidence**: V-01 ("Do not fill the table until both lines are written:") and V-04 satisfy C-41. V-05 ("Both need to be filled in before any row in the table is populated:") fails C-41 -- declarative form. V-03 (declarative throughout) fails C-41.

---

### C-42 -- Cell-Level Table-Fill Prohibition
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The imperative dual-field gate required by C-41 uses cell-level granularity -- "Do not fill any cell in the table until both items are written" -- rather than table-level granularity -- "Do not fill the table until both lines are written." C-41 passes with any imperative "Do not fill" prohibition form; C-42 passes only when the unit of prohibition is the individual cell, not the table or row. The failure mode C-41 leaves open: a table-level prohibition can be read as applying to the act of beginning the table. Once the first row is started, the constraint was satisfied at table-entry time; subsequent rows carry no structurally independent gate. A cell-level prohibition operates independently per cell and is checkable at every cell, not only at table entry. C-41 passes with either "Do not fill the table" or "Do not fill any cell"; C-42 passes only when the unit is "any cell" or equivalent per-cell granularity.
- **Pass condition**: The Step 4 dual-field gate uses a cell-level imperative prohibition in which the governed unit is explicitly "any cell" (or equivalent per-cell noun) rather than "the table" or "any row." An output without C-41 cannot satisfy C-42.
- **Round 14 evidence**: V-02 and V-04 ("Do not fill any cell in the table until both items are written:") satisfy C-42. V-01 and V-05 ("Do not fill the table until both lines are written:") satisfy C-41 but fail C-42 -- table-level prohibition.

---

### C-43 -- Triple Verbatim-Prohibition Clause in Exception Block
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The verbatim instruction required by C-40 in the Paraphrase clause field of the EXCEPTION SIGN-OFF BLOCK uses all three distinct prohibition clauses simultaneously: "do not paraphrase, do not summarize, copy it verbatim word-for-word." C-40 passes when the field instruction includes any single clause that forecloses one compression path; C-43 passes only when all three clauses are present. The failure mode C-40 leaves open: "copy it verbatim, do not paraphrase" forecloses semantic substitution and approximate reproduction but does not explicitly prohibit condensation (summary). A summary condenses the rule to shorter form, dropping precision clauses. The three-clause instruction forecloses all three distinct failure modes: (1) semantic substitution via paraphrase, (2) condensation via summary, (3) approximate reproduction via near-verbatim. Each clause is independently checkable by lexical search. C-40 passes when any single prohibition or verbatim mandate is present; C-43 passes only when all three clauses appear within the same field instruction.
- **Pass condition**: The Paraphrase clause field instruction in the EXCEPTION SIGN-OFF BLOCK contains all three distinct clauses: (1) "do not paraphrase" or equivalent, (2) "do not summarize" or equivalent, AND (3) a verbatim mandate ("copy it verbatim word-for-word" or equivalent). Any combination missing one of the three clauses does not pass. An output without C-40 cannot satisfy C-43.
- **Round 14 evidence**: V-01, V-03, V-04, and V-05 ("-- do not paraphrase, do not summarize, copy it verbatim word-for-word") satisfy C-43. V-02 ("-- copy it verbatim from your Step 2C block, do not paraphrase") satisfies C-40 but fails C-43 -- the "do not summarize" clause is absent.

---

### C-44 -- No-Exception Path Triple-Clause
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The no-exception confirmation statements in Pass 2C (one for Phase 1 and one for Phase 3) carry all three distinct prohibition clauses simultaneously: "do not paraphrase, do not summarize, copy it verbatim word-for-word." C-43 requires the triple-clause form in the Paraphrase clause field instruction of the EXCEPTION SIGN-OFF BLOCK; C-44 requires that the same triple-clause standard applies to the no-exception confirmation paths. The failure mode C-43 leaves open: the no-exception path is the default path that fires when all tickets comply with the C-28 directional rule, covering the majority of Phase 1 and Phase 3 commitments in a well-formed output. A model satisfying C-43 applies the triple-clause verbatim standard to exception entries while the no-exception confirmation -- the common case -- may use only a single prohibition clause or a two-clause form without "do not summarize." C-44 requires that both no-exception confirmation statements in Pass 2C carry the triple-clause form, making the verbatim standard uniform across both the exception and no-exception structural paths. C-43 passes when the exception block Paraphrase clause field carries the triple-clause; C-44 passes only when both no-exception confirmation paths in Pass 2C also carry the triple-clause form.
- **Pass condition**: Both no-exception confirmation statements in Pass 2C (Phase 1 no-exception and Phase 3 no-exception) carry all three clauses: (1) "do not paraphrase" or equivalent, (2) "do not summarize" or equivalent, AND (3) a verbatim mandate. A no-exception path carrying only a single prohibition clause or a two-clause form missing "do not summarize" does not pass. An output without C-43 cannot satisfy C-44.
- **Round 15 evidence**: V-01 (both no-exception confirmation statements in Pass 2C upgraded to triple-clause) satisfies C-44. V-04 (V-01 axis inherited) satisfies C-44. V-05 (full synthesis including V-01 axis) satisfies C-44. V-02 and V-03 (no-exception paths not upgraded) satisfy C-43 but fail C-44.

---

### C-45 -- Phase Distribution Pre-Commitment
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate requires a third item -- a PHASE DISTRIBUTION committed block pre-declaring Phase 1, Phase 2, and Phase 3 ticket counts and a total -- in addition to the own-words restatement and verbatim anchor required by C-38. The gate language is upgraded from "both items" to "all three items." Step 4B gains constraint 0, which verifies that the final ticket set matches the pre-committed count before body generation proceeds. C-38 requires a dual-field gate locking the inference rule and verbatim anchor before severity cells are filled; the failure mode C-38 leaves open: even with the inference rule fully committed, there is no pre-commitment to how many tickets will occupy each lifecycle phase. A model satisfying C-38 can fill the severity table with all tickets as Phase 1 without any structural gate making the distribution implausible. The PHASE DISTRIBUTION committed block pre-commits the distribution before any cell is filled: if the block states "Phase 1: 4, Phase 2: 2, Phase 3: 2, Total: 8," any deviation is a structural violation detectable at Step 4B constraint 0 without reading individual card bodies. C-38 passes when the Step 4 gate produces two labeled fields before severity cells are filled; C-45 passes only when a third labeled item is required, the gate language upgrades to "all three items," and Step 4B constraint 0 verifies count compliance.
- **Pass condition**: The Step 4 gate requires three items, including a PHASE DISTRIBUTION committed block pre-declaring per-phase ticket counts and a total, AND the gate instruction uses "all three items" (or equivalent) making the block non-optional, AND Step 4B includes a constraint 0 that verifies the final ticket set matches the pre-committed count before body generation proceeds. An output without C-38 cannot satisfy C-45.
- **Round 15 evidence**: V-02 (Step 4 adds PHASE DISTRIBUTION committed block as third required item; gate language: "all three items written"; Step 4B constraint 0: count-match verification before body generation) satisfies C-45. V-04 (V-02 axis inherited) and V-05 (full synthesis including V-02 axis) satisfy C-45. V-01 and V-03 (Step 4 gate retains "both items" form, no PHASE DISTRIBUTION block) satisfy C-38 but fail C-45.

---

### C-46 -- Switching-Friction Minimum Count Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The dedicated switching-friction gap sub-section required by C-29 carries a pre-count declaration gate -- "SWITCHING-FRICTION COUNT: [N]" -- written before any gap entry, and the minimum count floor is raised from one to two. Pass 2B gains a count-match item (item 4) verifying that the final count of entries matches the declared value. C-29 requires a dedicated fourth sub-section with per-entry competitor fields; it does not specify a minimum count or a pre-commitment gate. The failure mode C-29 leaves open: a single competitor-named entry satisfies C-29 fully -- no floor count prevents a one-entry sub-section, and no pre-commitment gate makes count undercounting detectable before reading the entries. The minimum-two floor establishes that switching-friction coverage requires at least two distinct competitor barriers. The pre-count declaration gate makes the declared count an auditable commitment: a scorer reads the count declaration, counts the entries, and any discrepancy is a structural violation at Pass 2B item 4 without scanning entry prose. C-29 passes when the dedicated switching-friction sub-section exists with per-entry competitor fields; C-46 passes only when the sub-section additionally carries a pre-count declaration before entries, the minimum count is two or more, and Pass 2B item 4 verifies count compliance.
- **Pass condition**: The switching-friction gap sub-section carries a pre-count declaration ("SWITCHING-FRICTION COUNT: [N]" or equivalent) written before any gap entry, AND the declared count is at least two, AND Pass 2B includes an explicit count-match check verifying that the final entry count matches the declaration. A sub-section with a single entry does not pass regardless of entry quality. A count declaration that appears after entries does not pass. An output without C-29 cannot satisfy C-46.
- **Round 15 evidence**: V-03 (switching-friction sub-section: "SWITCHING-FRICTION COUNT: [N]" before entries; minimum two required; Pass 2B item 4: count-match check) satisfies C-46. V-05 (full synthesis including V-03 axis) satisfies C-46. V-01, V-02, and V-04 (no count gate) satisfy C-29 but fail C-46.

---

### C-47 -- Phase-2 No-Exception Triple-Clause
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Phase 2 no-exception confirmation path in Pass 2C carries the same triple-clause verbatim form ("do not paraphrase, do not summarize, copy it verbatim word-for-word") as the Phase 1 and Phase 3 paths required by C-44. C-44 requires both no-exception confirmation statements in Pass 2C (Phase 1 and Phase 3) to carry the triple-clause form. The failure mode C-44 leaves open: Pass 2C is structured around the two phases with the strongest directional rule -- Phase 1 (P2/P3 expected) and Phase 3 (P0/P1 expected). Phase 2 (partial-commitment / transition phase) has a less stark severity expectation and its no-exception confirmation path was not required by C-44 to carry the triple-clause. A model satisfying C-44 produces two no-exception scan paths (Phase 1 and Phase 3) with triple-clause verbatim standard, while the Phase 2 scan -- if present at all -- may use only a single prohibition clause or be absent entirely. Phase 2 tickets exist in a well-formed output and the governing paraphrase clause covering Phase 2 lifecycle assignments is as susceptible to condensation as Phase 1 and Phase 3. V-01 added a Phase 2 scan path to Pass 2C Sub-check 1: "No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback). Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]." The triple-clause form appears on all three phase scan paths, making the verbatim standard uniform across Phase 1, Phase 2, and Phase 3. C-44 passes when Phase 1 and Phase 3 no-exception paths carry the triple-clause; C-47 passes only when the Phase 2 no-exception path in Pass 2C additionally carries the triple-clause form, making all three phases structurally uniform.
- **Pass condition**: Pass 2C includes an explicit Phase 2 no-exception scan path carrying all three clauses: (1) "do not paraphrase" or equivalent, (2) "do not summarize" or equivalent, AND (3) a verbatim mandate ("copy it verbatim word-for-word" or equivalent). A Pass 2C with Phase 1 and Phase 3 scan paths but no Phase 2 path does not pass C-47 even when the Phase 1 and Phase 3 paths carry the triple-clause. An output without C-44 cannot satisfy C-47.
- **Round 16 evidence**: V-01 (Pass 2C Sub-check 1 adds Phase 2 scan: "No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback). Governing paraphrase clause: [... do not paraphrase, do not summarize, copy it verbatim word-for-word]") satisfies C-47. V-04 (V-01 axis inherited via V-01+V-02 combination; Pass 2C Sub-check 1 carries all three phase scans with triple-clause) satisfies C-47. V-05 (full synthesis; Pass 2C Sub-check 1 includes Phase 2 scan with triple-clause; paraphrase consistency confirmation: "All three phase Paraphrase clause fields carry triple-clause verbatim: YES") satisfies C-47. V-02 (Phase Distribution Pre-Commitment axis only; no Phase 2 scan in Pass 2C) and V-03 (Switching-Friction Count Gate axis only; no Phase 2 scan in Pass 2C) satisfy C-44 but fail C-47. The Phase 2 scan closes the blind-spot that a two-phase (Phase 1, Phase 3) scan structure leaves open; the triple-clause on the Phase 2 path closes the standard-asymmetry failure mode that C-44 closes only for Phase 1 and Phase 3.

---

### C-48 -- Post-Generation Phase Distribution Re-Verify
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: After body generation, Part C includes a Sub-check 3 that counts actual Phase 1/2/3 card bodies and compares to the committed distribution block from Step 4/5. A mismatch at Sub-check 3 that was not present at Step 4B constitutes generation-time drift, named explicitly. C-45 requires a PHASE DISTRIBUTION committed block at Step 4 pre-declaring per-phase counts and a Step 4B constraint 0 verifying the summary table count before body generation proceeds. The failure mode C-45 leaves open: the constraint 0 check fires before body generation -- it verifies that summary table ticket counts match the pre-committed distribution before any card body is written. However, body generation (Step 6) is a sequential prose process; a model can reframe a Phase 3 card as Phase 2 during prose generation, add an implicit extra Phase 2 body, or assign a different lifecycle label in the card body than the pre-committed table. No structural gate fires after body generation is complete. The generation-drift window spans from the Step 4B check (pre-body) to the completed output: two temporal checkpoints exist (Step 4 commitment, Step 4B verification), but neither operates post-generation. V-02 added Sub-check 3 in Part C: "Post-generation phase distribution: Phase 1 bodies generated: [n]. Committed: [n]. MATCH / MISMATCH. Phase 2 ... Phase 3 ... Total ..." A discrepancy not caught at Step 4B is generation-time drift. V-02's phase-organized output format (section headers mark phase boundaries) makes the post-generation count self-confirming without ticket-ID parsing. V-04 adds a three-way comparison (generated count / Step 5 committed / Step 1 target per phase). V-05 makes the architecture explicit: pre-generation commitment (Step 5) + pre-body audit (Step 5B constraint 0) + post-generation re-verify (Sub-check 3) close all three temporal windows for phase drift. C-45 passes when the PHASE DISTRIBUTION committed block is required at Step 4 with constraint 0 verifying count before body generation; C-48 passes only when Part C additionally includes a Sub-check 3 that counts actual Phase 1/2/3 card bodies post-generation, compares to the committed distribution, and explicitly names any discrepancy as generation-time drift.
- **Pass condition**: Part C (within the dual-pass verification) includes an explicit Sub-check 3 (or equivalent) that (1) counts actual Phase 1/2/3 card bodies after body generation, (2) compares that count to the committed distribution from the Step 4/5 block, AND (3) names any discrepancy as generation-time drift (or equivalent term identifying the temporal window in which the deviation arose). A pre-generation count check (Step 4B constraint 0) does not satisfy C-48 -- the check must fire post-generation. A summary statement ("phases balanced") without explicit per-phase count comparison does not pass. An output without C-45 cannot satisfy C-48.
- **Round 16 evidence**: V-02 (Part C Sub-check 3: explicit per-phase count comparison, MATCH / MISMATCH verdict per phase, discrepancy named as generation-time drift; phase-organized output format makes count self-confirming by section) satisfies C-48. V-04 (V-02 axis inherited; Sub-check 3 present with three-way comparison: body count vs Step 5 committed vs Step 1 target per phase) satisfies C-48. V-05 (Sub-check 3 with three-way comparison; final statement: "Post-generation phase distribution matches committed block and Step 1 target"; generation-drift detection architecturally complete: pre-generation commitment + pre-body audit + post-generation re-verify close all temporal windows) satisfies C-48. V-01 (Pass 2C has Sub-checks 1 and 2 only; no Sub-check 3 post-generation count; generation-drift window remains open) and V-03 (no Sub-check 3 in Pass 2C) satisfy C-45 but fail C-48. The post-generation re-verify closes the generation-drift window that the pre-body audit alone leaves open.

---

### C-49 -- Switching-Friction Count Floor >= 3 with Phase-2 Barrier Constraint
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The switching-friction sub-section requires SWITCHING-FRICTION COUNT >= 3, with the third entry structurally constrained to cover a Phase 2 migration barrier (a friction that surfaces after partial commitment, not on day one). Pass 2B item 4 verifies count compliance; Pass 2 Sub-check 2 restates the count and confirms the third entry covers a Phase 2 barrier. C-46 requires a minimum of two switching-friction entries, a pre-count declaration gate, and Pass 2B item 4 count-match verification. The failure mode C-46 leaves open: with a minimum floor of two, both entries can describe day-one barriers -- friction any user encounters on first contact with the feature. Day-one friction is the most salient barrier and the easiest entry to write, but it does not represent the full migration-friction landscape. A user who has begun migrating workflows has crossed the day-one hurdle; the barriers they face arise after partial commitment, when they have invested in the feature but not fully detached from the competitor. A two-entry sub-section can satisfy C-46 entirely with two day-one entries without capturing this post-commitment friction class at all. V-03 raised the minimum to three and added a structural constraint on the third entry: it must cover a Phase 2 migration barrier -- a friction that surfaces after partial commitment, when the user has started migrating workflows but not fully detached from the competitor. Prohibited form explicitly stated: "a barrier that day-one users would also encounter." Pass 2 Sub-check 2 restates "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO." and confirms "Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO." The third-entry type constraint is not a content instruction but a structural pass condition: Sub-check 2 must confirm YES for C-49 to pass. C-46 passes when the sub-section carries a minimum of two entries with a pre-count gate and Pass 2B count-match verification; C-49 passes only when the minimum is three, the third entry is structurally constrained to a Phase 2 migration barrier (not day-one), and Pass 2 Sub-check 2 confirms the third-entry type constraint post-generation.
- **Pass condition**: (1) The switching-friction sub-section requires SWITCHING-FRICTION COUNT >= 3, with a pre-count declaration before entries; (2) the third entry carries an explicit structural constraint naming it as a Phase 2 migration barrier (surfaces after partial commitment, not day-one) with an explicit prohibition on day-one entries ("Prohibited: a barrier that day-one users would also encounter" or equivalent); AND (3) Pass 2 Sub-check 2 (or equivalent) confirms SWITCHING-FRICTION COUNT >= 3 AND confirms the third entry covers a Phase 2 migration barrier (not day-one friction) with a YES/NO outcome. A sub-section with three entries but no third-entry type constraint does not pass. A type constraint that appears only as a content instruction without a post-generation verification step does not pass. An output without C-46 cannot satisfy C-49.
- **Round 16 evidence**: V-03 (Step 5C item 4: "N must be >= 3. Do not proceed to Step 6 if N < 3. Third entry must cover a Phase 2 migration barrier -- a friction that only surfaces after partial commitment, when the user has started migrating workflows but not fully detached from the competitor. Prohibited: a barrier that day-one users would also encounter." Step 8: Entry 1 = primary day-one friction, Entry 2 = second most prominent barrier, Entry 3 = Phase 2 barrier only. Sub-check 2: "N >= 3: YES/NO ... Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.") satisfies C-49. V-05 (full synthesis including V-03 axis; Sub-check 2 confirming "SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.") satisfies C-49. V-01 (floor >= 2; no third-entry type constraint), V-02 (floor >= 2; no third-entry type constraint), and V-04 (V-01+V-02; no V-03 axis) satisfy C-46 but fail C-49. The Phase 2 barrier constraint closes the day-one-saturation failure mode that a two-entry floor permits; the Sub-check 2 verification converts the constraint from an instruction into a post-generation auditable property.

---

### C-50 -- Sub-Check 3 Table Format
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Sub-check 3 in Part C uses a table format with one row per phase -- not a prose sentence sequence -- to report the post-generation phase distribution comparison. C-48 requires Sub-check 3 to count actual Phase 1/2/3 card bodies, compare to the committed distribution, and name any discrepancy as generation-time drift; it does not constrain the format of the comparison. The failure mode C-48 leaves open: the count comparison can be prose sentences -- "Phase 1 bodies generated: 4. Committed: 4. MATCH." -- and phases can be collapsed into a single sentence ("Phase 1 and Phase 2 both match, 4 and 2 respectively") with counts embedded rather than independent. A MISMATCH in a prose Sub-check 3 is a clause to extract from the sentence, not a cell value; a scorer must parse sentence structure to identify which phase has drifted and what the deviation is. A table row per phase makes MISMATCH a cell value in the Match column -- readable without sentence parsing. Row count is self-verifying: three rows for three phases means all phases are independently represented and none can be silently collapsed into a sibling row. The structural independence mechanism is identical to C-15 (which converts prose ticket traces to table rows, making each ticket independently checkable by row). C-48 passes when Sub-check 3 fires post-generation and counts per-phase in any format; C-50 passes only when Sub-check 3 uses a table format with one row per phase and at least four columns (Phase / Bodies generated / Committed / Match).
- **Pass condition**: Sub-check 3 in Part C is a formatted table (not inline prose), with one row per lifecycle phase (at least three rows for Phase 1, Phase 2, Phase 3) and at least four columns including Phase, a bodies-generated count, a committed count, and a Match / MISMATCH verdict column. A prose comparison -- even one that names each phase separately and produces correct counts -- does not pass. An output without C-48 cannot satisfy C-50.
- **Round 17 evidence**: V-01 (Sub-check 3 replaced with a 4-column table: Phase / Bodies generated / Committed (Step 5) / Match; MISMATCH is a cell value in column 4, not a clause to extract from prose; row count self-verifies phase coverage without sentence parsing) satisfies C-50. V-04 (V-01 axis inherited; three-way comparison table: Phase / Bodies generated / Committed (Step 5) / Step 1 target / Match) satisfies C-50. V-05 (full synthesis; Sub-check 3 table format with MATCH/MISMATCH verdict column per phase row) satisfies C-50. V-02 (prose Sub-check 3 from V-05 R16 baseline retained -- MATCH/MISMATCH per phase in sentence form) and V-03 (no Sub-check 3 axis) satisfy C-48 but fail C-50. The table format closes the sentence-collapse failure mode that prose Sub-check 3 permits; cell-value MISMATCH detection does not require clause extraction.

---

### C-51 -- Phase-2 Barrier Trigger-Event Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Entry 3 in the switching-friction sub-section carries a `Trigger event:` field naming the specific action or moment when the Phase 2 barrier surfaces in a migration workflow. Sub-check 2 is extended to require verbatim quote of the `Trigger event:` field value as the evidence base for the Phase-2 confirmation. C-49 requires the third entry to be structurally constrained to a Phase 2 migration barrier with an explicit prohibition on day-one entries, and Sub-check 2 to confirm the third-entry type with a YES/NO outcome. The failure mode C-49 leaves open: the Sub-check 2 YES/NO is a declarative self-report. A model confirms "Third entry covers Phase 2 migration barrier: YES" without any field in Entry 3 that makes the Phase-2 character independently falsifiable. A scorer must read Entry 3's prose to evaluate whether the barrier described surfaces after partial commitment or at day one -- the judgment is prose-dependent and cannot be made from a single field value. The `Trigger event:` field converts the Phase-2 character judgment into an evidence-backed property: a day-one trigger (e.g., "User first opens the feature") in the `Trigger event:` field fails the Phase 2 constraint without requiring prose evaluation -- the field value is independently falsifiable. Sub-check 2 quotes the `Trigger event:` value, and an evaluator confirms the trigger is post-commitment-specific by reading one field. C-49 passes when count >= 3 and Sub-check 2 confirms the third-entry type via YES/NO; C-51 passes only when Entry 3 additionally carries a `Trigger event:` field and Sub-check 2 quotes the `Trigger event:` value as the evidence base for the Phase-2 confirmation.
- **Pass condition**: Entry 3 in the switching-friction sub-section includes an explicitly labeled `Trigger event:` field (or equivalent) naming the specific moment when the barrier surfaces, AND Sub-check 2 quotes the `Trigger event:` field value verbatim as evidence for the Phase-2 migration barrier confirmation. A Sub-check 2 that confirms the Phase-2 type with YES/NO without quoting a specific trigger event does not pass. An output without C-49 cannot satisfy C-51.
- **Round 17 evidence**: V-02 (Entry 3 gains `Trigger event:` field; Sub-check 2 extended to require verbatim quote: "Trigger event quoted: [value from Entry 3 Trigger event: field]. This trigger surfaces after partial commitment: YES / NO.") satisfies C-51. V-04 (V-01+V-02 combined; `Trigger event:` field in Entry 3 inherited from V-02 axis; Sub-check 2 quotes trigger event) satisfies C-51. V-05 (full synthesis; `Trigger event:` field in Entry 3; Sub-check 2 quotes trigger event and confirms post-commitment specificity) satisfies C-51. V-01 (no V-02 axis; Sub-check 2 YES/NO without trigger event quote) and V-03 (no V-02 axis) satisfy C-49 but fail C-51. The `Trigger event:` field converts the declarative YES/NO confirmation into an independently falsifiable structural property.

---

### C-52 -- Per-Template Prohibited Sentinel in Entry 3
- **Weight**: aspirational
- **Points**: 5
- **Category**: behavior
- **Text**: The `Prohibited:` sentinel for the Phase 2 barrier constraint appears within the Entry 3 template body itself, field-adjacent above `Expected behavior:` (or the equivalent first content field) -- not only in the entry-type constraint instruction block. C-49 requires the third entry to carry an explicit structural constraint with a `Prohibited:` prohibition on day-one entries. The prohibition is stated in the entry-type constraint instruction that specifies what the third entry must be. The failure mode C-49 leaves open: the prohibition is in the instruction block, spatially separated from the content fields of Entry 3 by intervening template structure (the field prompts for Entry 1, Entry 2, and the opening of Entry 3 itself). A model generating Entry 3's content fields must retrieve the prohibition from the prior instruction context; if the instruction is contextually distant, the constraint is nominally present but not live at the moment content fields are written. V-03 moved the `Prohibited:` sentinel from the entry-specific guidance section into the Entry 3 template body, positioned field-adjacent above `Expected behavior:`. The sentinel is present at the moment Entry 3's content fields are written -- it does not need to be retrieved from a prior block. The structural mechanism is identical to C-18 (which moves per-field `Prohibited:` sentinels into the consequence field structure, making the disallowed form visible at field-write time rather than at instruction-read time). C-49 passes when the prohibition is stated anywhere in the entry-type constraint; C-52 passes only when the `Prohibited:` sentinel additionally appears within the Entry 3 template body itself, field-adjacent to the content fields.
- **Pass condition**: The Entry 3 template body includes a `Prohibited:` sentinel (or equivalent) positioned field-adjacent -- on the line immediately above a content field within the template (e.g., above `Expected behavior:`) -- naming the prohibited day-one entry form. A `Prohibited:` note that appears only in the instruction block above the Entry 3 template, and not inside the template body, does not pass. An output without C-49 cannot satisfy C-52.
- **Round 17 evidence**: V-03 (Entry 3 `Prohibited:` sentinel moved from entry-specific guidance section into the template body, field-adjacent above `Expected behavior:`: "Prohibited: a barrier that day-one users would also encounter." appears as a template-body element, visible at Entry-3 content-field write time) satisfies C-52. V-05 (full synthesis including V-03 axis; `Prohibited:` sentinel field-adjacent in Entry 3 template body) satisfies C-52. V-01 (no V-03 axis), V-02 (no V-03 axis), and V-04 (V-01+V-02; no V-03 axis; `Prohibited:` note in instruction block only) satisfy C-49 but fail C-52. The field-adjacent sentinel applies the C-18 spatial-adjacency mechanism to the switching-friction entry constraint: the disallowed form is visible at the moment the governed content fields are written.

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
| C-27 | Named inertia competitor phase framing         | aspirational | 5      | depth       |
| C-28 | Phase-architecture severity inference rule     | aspirational | 5      | depth       |
| C-29 | Dedicated switching-friction gap sub-section   | aspirational | 5      | depth       |
| C-30 | Inference rule paraphrase-before-proceed gate  | aspirational | 5      | depth       |
| C-31 | Inference audit in dual-pass Part C            | aspirational | 5      | depth       |
| C-32 | Decision-adjacent paraphrase gate              | aspirational | 5      | depth       |
| C-33 | Structured exception sign-off block in Part C  | aspirational | 5      | depth       |
| C-34 | Paraphrase double-gate with Step-4 recall      | aspirational | 5      | depth       |
| C-35 | Part C paraphrase consistency confirmation     | aspirational | 5      | depth       |
| C-36 | Exception block paraphrase-clause field        | aspirational | 5      | depth       |
| C-37 | Step-4 verbatim anchor field                   | aspirational | 5      | depth       |
| C-38 | Dual-field Step-4 gate                         | aspirational | 5      | depth       |
| C-39 | Step-4 every-assignment scope confirmation     | aspirational | 5      | depth       |
| C-40 | Exception block verbatim-clause instruction    | aspirational | 5      | depth       |
| C-41 | Imperative dual-field gate language            | aspirational | 5      | depth       |
| C-42 | Cell-level table-fill prohibition              | aspirational | 5      | depth       |
| C-43 | Triple verbatim-prohibition clause             | aspirational | 5      | depth       |
| C-44 | No-exception path triple-clause                | aspirational | 5      | depth       |
| C-45 | Phase distribution pre-commitment              | aspirational | 5      | depth       |
| C-46 | Switching-friction minimum count gate          | aspirational | 5      | depth       |
| C-47 | Phase-2 no-exception triple-clause             | aspirational | 5      | depth       |
| C-48 | Post-generation phase distribution re-verify   | aspirational | 5      | depth       |
| C-49 | Switching-friction count floor >= 3 w/ Phase-2 barrier | aspirational | 5 | depth  |
| C-50 | Sub-check 3 table format                       | aspirational | 5      | depth       |
| C-51 | Phase-2 barrier trigger-event field            | aspirational | 5      | depth       |
| C-52 | Per-template Prohibited sentinel in Entry 3    | aspirational | 5      | behavior    |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 310

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
| v8 | 2026-03-14 | Added C-27 (named inertia competitor phase framing) from Round 7 excellence signals; aspirational tier grows from 90 to 95 pts, total ceiling 185 |
| v9 | 2026-03-14 | Added C-28 (phase-architecture severity inference rule) and C-29 (dedicated switching-friction gap sub-section) from Round 8 excellence signals; aspirational tier grows from 95 to 105 pts, total ceiling 195 |
| v10 | 2026-03-14 | Added C-30 (inference rule paraphrase-before-proceed gate) and C-31 (inference audit in dual-pass Part C) from Round 9 excellence signals; aspirational tier grows from 105 to 115 pts, total ceiling 205 |
| v11 | 2026-03-14 | Added C-32 (decision-adjacent paraphrase gate), C-33 (structured exception sign-off block in Part C), C-34 (paraphrase double-gate with Step-4 recall), and C-35 (Part C paraphrase consistency confirmation) from Round 10 excellence signals; aspirational tier grows from 115 to 135 pts, total ceiling 225 |
| v12 | 2026-03-15 | Added C-36 (exception block paraphrase-clause field), C-37 (Step-4 verbatim anchor field), C-38 (dual-field Step-4 gate), and C-39 (Step-4 every-assignment scope confirmation) from Round 11 excellence signals; aspirational tier grows from 135 to 155 pts, total ceiling 245 |
| v13 | 2026-03-15 | Added C-40 (exception block verbatim-clause instruction) and C-41 (imperative dual-field gate language) from Round 13 excellence signals; aspirational tier grows from 155 to 165 pts, total ceiling 255 |
| v14 | 2026-03-15 | Added C-42 (cell-level table-fill prohibition) and C-43 (triple verbatim-prohibition clause in exception block) from Round 14 excellence signals; aspirational tier grows from 165 to 175 pts, total ceiling 265 |
| v15 | 2026-03-15 | Added C-44 (no-exception path triple-clause), C-45 (phase distribution pre-commitment), and C-46 (switching-friction minimum count gate) from Round 15 excellence signals; aspirational tier grows from 175 to 190 pts, total ceiling 280 |
| v16 | 2026-03-15 | Added C-47 (phase-2 no-exception triple-clause), C-48 (post-generation phase distribution re-verify), and C-49 (switching-friction count floor >= 3 with Phase-2 barrier constraint) from Round 16 excellence signals; aspirational tier grows from 190 to 205 pts, total ceiling 295 |
| v17 | 2026-03-15 | Added C-50 (sub-check 3 table format), C-51 (phase-2 barrier trigger-event field), and C-52 (per-template Prohibited sentinel in Entry 3) from Round 17 excellence signals; aspirational tier grows from 205 to 220 pts, total ceiling 310 |
