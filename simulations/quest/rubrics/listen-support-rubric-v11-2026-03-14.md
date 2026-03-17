Written to `simulations/quest/rubrics/listen-support-rubric-v11-2026-03-14.md`.

---

**What changed v10 -> v11:**

Four new criteria extracted from R10 above-ceiling signals:

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-32 | Decision-Adjacent Paraphrase Gate | C-30 | V-02, V-04, V-05 |
| C-33 | Structured Exception Sign-Off Block in Part C | C-31 | V-04, V-05 |
| C-34 | Paraphrase Double-Gate with Step-4 Recall | C-30, C-32 | V-05 |
| C-35 | Part C Paraphrase Consistency Confirmation | C-31, C-34 | V-05 |

**Tier:** Aspirational 23 / 115 pts -> 27 / 135 pts. Total ceiling **205 -> 225**.

---

**Signal extraction rationale:**

**C-32** comes from V-02, V-04, and V-05's decision-adjacent gate placement. C-30 requires a paraphrase gate with "do not proceed" language anywhere before ticket generation; V-03 satisfies that with a hard gate at STEP 2C (the rule-statement step). V-02 moves the gate to the Step 4 header -- the step where severity cells are filled -- so the paraphrase is the live preceding generation context when each severity value is assigned. The structural difference: when the gate is at STEP 2C, the model produces the paraphrase and then traverses Step 3 prose before reaching severity assignments; the paraphrase has decayed from live context. When the gate is at Step 4 header, no prose traverses between paraphrase and severity column. C-30 passes with any gate placement before ticket generation; C-32 passes only when the gate fires immediately before the severity-assignment step.

**C-33** comes from V-04 and V-05's structured EXCEPTION SIGN-OFF BLOCK in Part C sub-check (1). C-31 Part C sub-check (1) requires an explicit exception acknowledgment for any C-28 directional violation; V-01, V-02, and V-03 satisfy that with prose acknowledgment using outage/blocking test language. V-04 replaces prose with a structured block containing five named fields: Ticket ID, Phase, Assigned severity, Grounds, Disposition. The structural difference: prose acknowledgment can collapse multiple exceptions into one sentence with no field separation, making individual exception grounds unverifiable without parsing sentence structure. A structured block with named fields makes each exception independently checkable; a scorer reads the Grounds field per block without reading prose. The no-exception path must also be specified, preventing silent omission of the block when no violations exist. C-31 passes with any explicit exception acknowledgment; C-33 passes only when the acknowledgment mechanism is a structured block with at least four named fields per exception entry.

**C-34** comes from V-05's double-gate mechanism. C-32 requires one decision-adjacent gate at Step 4; V-05 adds a second gate at STEP 2C (the rule-statement step) with an explicit cross-reference at Step 4: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from 2C]". The word "confirmed" and the "restate from 2C" clause require the model to retrieve its STEP 2C commitment rather than produce a fresh paraphrase. The structural difference from C-32: a single Step 4 gate produces a paraphrase without the inference rule in live generation context (the rule text was at STEP 2C, not Step 4). The double-gate ensures encoding at the rule step (rule text is live) and re-confirmation at the decision step (severity assignment is live). The explicit cross-reference closes the divergence path: the Step 4 paraphrase cannot silently differ from the STEP 2C commitment when the gate instruction names the earlier step. C-32 passes with one decision-adjacent gate; C-34 passes only when gates fire at both positions with the Step 4 gate explicitly referencing the STEP 2C paraphrase by step name.

**C-35** comes from V-05's paraphrase consistency confirmation in Part C. C-34 creates a paraphrase commitment at STEP 2C; C-31 Part C sub-check (1) audits tickets for C-28 directional compliance. Without C-35, the paraphrase and the audit are structurally parallel but not cross-linked -- the paraphrase is a pre-generation commitment, the audit is a post-generation check, and neither references the other. V-05 closes this loop: after the exception scan, Part C quotes the Step 2C paraphrase verbatim and confirms the audit result is consistent with it. The structural consequence: a model that violated the directional rule in ticket generation cannot pass Part C sub-check (1) without flagging the contradiction between the audit findings and its own quoted paraphrase. The paraphrase becomes an auditable anchor cited inside the verification pass rather than a pre-generation ritual with no post-generation linkage. C-31 passes with both sub-checks present in Part C; C-35 passes only when Part C sub-check (1) additionally quotes the STEP 2C paraphrase and states whether the audit result is consistent with that commitment.

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

## Aspirational Criteria (135 pts total -- raises the bar above 90)

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
- **Text**: The STATUS QUO section names a specific competing tool by product name (the inertia competitor), and the ticket body instructions are differentiated by adoption-curve phase: early-phase body templates name dual-tool parallelism; late-phase body templates name parity gaps. Three structural properties must hold simultaneously: (1) Tool-name fidelity -- the STATUS QUO names the inertia competitor by product name, producing a grep-checkable string rather than an interpretable phrase like "the legacy system" or "their existing tooling"; (2) Phase-differentiated body templates -- the instructions state two distinct body stances explicitly: a P1/early-phase template naming dual-tool tension ("I still have [tool] open in another tab..."; "I ran [tool] first and then tried this...") and a P3/late-phase template naming a parity gap ("In [tool] I could do X; here I cannot."; "The one thing [tool] had that I need here is..."); (3) Switching-friction gap reframe -- at least one gap sub-section is framed as a switching-friction gap (a specific barrier for users migrating from the named competitor) rather than a generic doc, design, or operational gap. C-11 passes with any concrete current-state description that anchors volume and body content; C-27 passes only when the current-state description names the specific tool, the body templates are phase-differentiated by adoption-curve position, and the gap inventory includes at least one switching-friction gap tied to the named competitor. The three properties are individually testable: tool names are grep-checkable; body templates are sentence-level and verifiable against the output; switching-friction gaps are identifiable by the presence of the competitor name in the gap description.
- **Pass condition**: (1) The STATUS QUO or equivalent current-state section names at least one specific competing tool by product name (a grep-checkable string, not a generic description); AND (2) the ticket body instructions include at least two explicitly stated phase-differentiated body templates -- one for early-phase (P1-range) tickets naming dual-tool tension with the named competitor, and one for late-phase (P3-range) tickets naming a parity gap with the named competitor; AND (3) the gap analysis includes at least one gap explicitly framed as a switching-friction gap naming the inertia competitor. A STATUS QUO describing parallel tool usage without naming the product does not pass. Phase-differentiated templates that do not reference the named competitor do not pass. A switching-friction gap framing that appears only in a post-generation summary does not pass.
- **Round 7 evidence**: V-03 and V-05 (STATUS QUO names the inertia competitor by tool name; body instructions include P1 template: "I still have [tool] open in another tab..." and P3 template: "In [tool] I could do X; here I cannot."; gap analysis contains switching-friction gaps naming the competitor) score C-11 PASS+. V-01, V-02, V-04 (generic STATUS QUO scenario without named competitor, no phase-differentiated body templates) score C-11 PASS but fail C-27. Named competitor closes the grep-checkability gap that generic scenario description leaves open; phase-differentiated templates close the adoption-curve signal gap that generic body instructions leave open; switching-friction gap reframe produces a qualitatively different gap inventory from the doc/design/operational taxonomy C-04 requires.

---

### C-28 -- Phase-Architecture Severity Inference Rule
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The INERTIA or STATUS QUO section states an explicit phase-to-severity inference rule before ticket generation: early-adoption-phase (P1 on the adoption curve) tickets produce lower severity (P2/P3) because adoption friction is expected and a workaround is available; late-adoption-phase (P3) tickets produce higher severity (P0/P1) because parity gaps block established users who have committed to the feature. This rule is stated as a directional architectural constraint derived from the adoption-curve phase, not as a per-ticket calibration note or a post-generation severity defense. C-22 requires a phase map table assigning severity ranges per phase window (e.g., "Phase 1: P0/P1 expected") -- it does not require stating why those ranges apply in that direction. A model can satisfy C-22 by assigning any defensible severity range per phase without the directional logic. The inference rule closes this gap: stating explicitly that early-phase adoption pain yields lower severity (friction is normal and survivable) while late-phase parity gaps yield higher severity (missing capability blocks committed users) makes a directional reversal a structural violation rather than a calibration judgment call. Phase-structured severity inference also changes how the phase body templates from C-27 interact with the ticket set: a P1 template framing dual-tool tension maps naturally to P2/P3 severity because the user still has the fallback tool; a P3 template framing a parity gap maps naturally to P0/P1 severity because the fallback is no longer in play. C-22 passes with any phase-severity mapping table; C-28 passes only when the directional inference logic is stated explicitly -- why early-phase maps to lower severity and why late-phase maps to higher severity -- as part of the INERTIA or phase framing architecture, before any ticket is generated.
- **Pass condition**: The output includes an explicit phase-to-severity inference rule before ticket generation stating (1) that early-adoption-phase tickets produce lower severity (P2/P3) because adoption friction is expected and workable, AND (2) that late-adoption-phase tickets produce higher severity (P0/P1) because parity gaps block established users. A phase map table that lists severity ranges without stating the directional reasoning does not pass. A per-ticket calibration note or post-generation severity explanation does not pass.
- **Round 8 evidence**: V-04 ("P1 adoption pain maps to P2/P3 severity -- friction is expected, workaround available; P3 parity gaps map to P1/P0 -- blocking established use") satisfies C-28 and scores C-06 PASS+. V-01, V-02, V-03, V-05 (phase map tables with severity ranges, no directional inference rule) score C-22 PASS but fail C-28. The directional rule makes severity reversals structurally implausible before generation; a phase map table alone cannot provide that constraint because it lists ranges without binding them to a reason.

---

### C-29 -- Dedicated Switching-Friction Gap Sub-Section with Competitor Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The gap analysis includes a dedicated fourth sub-section for switching-friction gaps -- separated from the three sub-sections required by C-04 (doc, design, operational) -- where every gap entry carries a structured per-entry field naming the inertia competitor as the migration source (e.g., "Migrating from: [tool]" or "Competitor barrier: [tool] -- [capability]"). C-27 P3 requires at least one gap framed as a switching-friction gap naming the competitor, anywhere in the gap analysis; C-29 requires that all switching-friction gaps are structurally isolated in their own sub-section with per-entry competitor fields. The failure mode C-27 P3 permits: a single competitor-named gap can be embedded inside the doc, design, or operational sub-sections, satisfying C-27's structural requirement while keeping switching-friction gaps mixed with standard taxonomy gaps. A dedicated sub-section separates the switching-friction inventory structurally, making the count of competitor-specific gaps enumerable without reading across all three standard sub-sections. Per-entry competitor fields make every entry's migration-source reference grep-checkable by field; a scorer can read down the competitor column and confirm that every switching-friction gap names a specific tool without parsing gap descriptions. The sub-section is explicitly additive: it supplements C-04's three sub-sections, not replaces them. An output that replaces one of the three required sub-sections with a switching-friction sub-section fails both C-04 and C-29. C-27 P3 passes with any competitor-named switching-friction gap anywhere in the gap analysis; C-29 passes only when switching-friction gaps occupy their own labeled fourth sub-section with per-entry structured format including a competitor-reference field for every gap listed.
- **Pass condition**: The gap analysis contains a fourth explicitly labeled sub-section for switching-friction or migration gaps (not merged with doc/design/operational sub-sections), AND each gap entry in that sub-section includes a structured field naming the inertia competitor by product name (a grep-checkable string). The three C-04 sub-sections must remain present and non-empty. A switching-friction gap embedded inside a standard sub-section does not pass. An unstructured list of competitor mentions without per-entry field structure does not pass. A gap analysis that replaces one of the three C-04 sub-sections with a switching-friction sub-section fails both C-04 and C-29.
- **Round 8 evidence**: V-04 (gap analysis: doc / design / operational sub-sections intact; fourth "switching-friction" sub-section with "Migrating from: [tool]" per entry; described as "additional, not replacement") satisfies C-29 and scores C-04 PASS+. V-01, V-02, V-03, V-05 (switching-friction gaps embedded inside standard sub-sections, no dedicated fourth sub-section) score C-27 P3 PASS but fail C-29. The dedicated sub-section makes switching-friction inventory separately enumerable; the per-entry field makes competitor references grep-checkable without reading gap prose.

---

### C-30 -- Inference Rule Paraphrase-Before-Proceed Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The step containing the phase-to-severity inference rule required by C-28 includes a structural paraphrase gate: the model must restate the directional inference rule in its own words before any ticket is generated. The canonical form: "In your own words, state the directional rule before proceeding: [model paraphrase here]." C-28 requires that the inference rule be stated as a named imperative constraint before generation; C-30 requires that the model demonstrate conceptual encoding of that rule by paraphrasing it before proceeding. The distinction is load-bearing: a read-and-apply instruction is satisfied by any model that writes the rule (or a verbatim copy of it) and advances to ticket generation. A paraphrase gate requires the model to produce a restatement in different words -- a model cannot paraphrase the inference rule correctly while misunderstanding the directional constraint. The paraphrase also creates an auditable trace: if a model generates a Phase 1 P0 ticket later, the scorer can compare the ticket to the paraphrase the model committed to earlier in its own output. That comparison is structurally self-contradicting -- the model violated a rule it demonstrably understood and restated. Without a paraphrase, the rule is a constraint the model read; with a paraphrase, it is a constraint the model encoded before generating any ticket. C-28 passes when the directional rule is stated as an imperative checkpoint before ticket generation; C-30 passes only when that checkpoint additionally requires the model to produce a paraphrase of the rule (in its own words, not a verbatim copy) before proceeding past the step.
- **Pass condition**: The inference rule step includes an explicit paraphrase instruction requiring the model to restate the directional logic (why early-phase maps to lower severity, why late-phase maps to higher severity) in its own words before proceeding, AND the instruction specifies that a verbatim copy of the rule does not satisfy the gate. A "confirm you understand" instruction without a paraphrase requirement does not pass. A paraphrase requirement added after the ticket generation section does not pass.
- **Round 9 evidence**: V-05 (STEP 2C: "Paraphrase this rule in your own words before proceeding") scores C-28 PASS+ and satisfies C-30. V-04 (STEP 2C: imperative rule + count-and-flag, no paraphrase gate) scores C-28 PASS but fails C-30. The paraphrase gate converts the inference rule from a read-and-apply instruction into a demonstrated encoding commitment; a model that has paraphrased the directional rule cannot assign Phase 1 P0 tickets later without contradicting a claim stated in its own words earlier in the output.

---

### C-31 -- Inference Audit in Dual-Pass Part C
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: Pass 2 of the dual-pass verification required by C-23 is extended with a structurally independent Part C (the inference audit) that verifies two properties not covered by Pass 1 or Pass 2: (1) C-28 directional compliance -- every Phase 1 ticket has severity P2/P3 and every Phase 3 ticket has severity P0/P1; any directional exception is named explicitly with a one-sentence justification; (2) C-29 sub-section completeness -- the dedicated switching-friction sub-section exists in the gap analysis and every entry has the `Migrating from:` competitor field populated. C-23 requires two passes with non-overlapping failure surfaces (coverage traces and frontmatter vocabulary drift); C-31 extends to three parts, adding a third failure surface: inference rule compliance and switching-friction field completeness. Without Part C, C-28 and C-29 are generation-time structural constraints -- satisfied or not at the point of generation, but never verified post-generation. A model can write a correct inference rule (C-28 PASS) and generate tickets; the tickets may drift from the rule without triggering any structural violation in Pass 1 or Pass 2. Similarly, a model can write the switching-friction sub-section (C-29 PASS) and populate most but not all competitor fields; Pass 1 and Pass 2 do not scan for field completeness within the sub-section. Part C closes both gaps: it explicitly scans for directional violations and sub-section field completeness, requiring an exception acknowledgment for any C-28 violation found. Part C is named and labeled as its own section, making it structurally independent from the frontmatter verify section and the coverage trace section. C-23 passes when two labeled verification passes cover coverage traces and frontmatter drift; C-31 passes only when Pass 2 additionally includes a Part C that explicitly audits C-28 inference compliance and C-29 field completeness, each as named sub-checks, with an exception acknowledgment gate for C-28 violations.
- **Pass condition**: Pass 2 of the dual-pass verification includes an explicitly labeled Part C that performs two named sub-checks: (1) scan every ticket for C-28 directional compliance (Phase 1 -> P2/P3, Phase 3 -> P0/P1) with a required exception acknowledgment for any violation found; AND (2) confirm the switching-friction sub-section exists and every entry has the competitor field populated. A single verification step that mentions inference rule compliance without structurally separating it as Part C of Pass 2 does not pass. An output without C-23 cannot satisfy C-31. A Part C that covers only one of the two named sub-checks does not pass.
- **Round 9 evidence**: V-05 (Pass 2 Part C: "(1) INFERENCE AUDIT -- scan every ticket: Phase 1 must be P2/P3, Phase 3 must be P0/P1; name any exception with one-sentence justification. (2) SWITCHING-FRICTION AUDIT -- confirm dedicated sub-section present; confirm every entry has Migrating from: field populated.") scores C-28 PASS+ and C-29 PASS+, converting both from structural assumptions to verified output properties. V-04 (STEP 4B count-and-flag for C-28; no C-29 verification) scores C-28 PASS and C-29 PASS but fails C-31. The inference audit in Part C is what separates "structurally correct generation" from "verified output property"; V-05 ranks above V-04 on identical numeric scores precisely because Part C makes C-28 and C-29 compliance auditable after generation rather than assumed from prompt structure.

---


### C-32 -- Decision-Adjacent Paraphrase Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The paraphrase gate required by C-30 fires immediately before the step where severity values are assigned -- not at the step where the inference rule is stated. The canonical placement: Step 4 header (the severity-assignment step) carries the gate instruction "Before filling any severity cell, state the inference rule from Step 2C in your own words. Do not fill the table until this line is written: INFERENCE RULE (stated): [...]". C-30 requires a paraphrase gate with explicit "do not proceed" language placed anywhere before ticket generation; C-32 requires that the gate fire at the decision point -- the step where severity cells are first filled. The distinction is temporal coupling: when the gate is at the rule-statement step (STEP 2C), the model produces the paraphrase and then traverses Step 3 prose before reaching severity assignments; the paraphrase is no longer live generation context when severity decisions are made. When the gate is at the decision step (Step 4 header), the paraphrase is the immediately preceding generation and is therefore live context when severity cells are written. No prose traverses between the paraphrase commitment and the first severity value. C-30 passes with a paraphrase gate anywhere before ticket generation with "do not proceed" language; C-32 passes only when the gate fires at or immediately before the step where severity values are first assigned, with a "do not fill" instruction tied specifically to severity column or table values.
- **Pass condition**: The paraphrase gate instruction appears at the severity-assignment step (not the rule-statement step), as the immediately preceding instruction before severity cells are filled, AND uses "do not fill" or equivalent language tied to the severity column or table. A paraphrase gate at the rule-statement step -- even with "do not proceed" language -- does not satisfy C-32 if prose or additional steps intervene before severity assignment. An output without C-30 cannot satisfy C-32.
- **Round 10 evidence**: V-02, V-04, V-05 (paraphrase gate at Step 4 header: "Before filling any severity cell, state the inference rule in your own words. Do not fill the table until this line is written.") satisfy C-30 and additionally satisfy C-32. V-03 (hard gate at STEP 2C: "Do not proceed to Step 3 until this block is filled") scores C-30 PASS but fails C-32 -- the gate fires at the rule step, and Step 3 prose intervenes before severity assignment. V-01 (named block at STEP 2C, no gate language) fails both C-30 and C-32.

---

### C-33 -- Structured Exception Sign-Off Block in Part C
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-31 Part C sub-check (1) requires an explicit exception acknowledgment for any ticket that violates the C-28 directional rule. C-33 requires that the acknowledgment mechanism be a structured EXCEPTION SIGN-OFF BLOCK with at least four named fields per exception: (1) Ticket ID; (2) Phase (adoption-curve phase); (3) Assigned severity; (4) Grounds (the justification for the directional exception). The canonical five-field form additionally includes (5) Disposition (e.g., "retained as deliberate exception"). A no-exception path must be specified for cases where no tickets violate the directional rule. C-31 passes with any named exception acknowledgment in Part C sub-check (1); the minimum satisfying form is prose ("T-03 is Phase 1 P0 because of a complete outage scenario"). Prose acknowledgment can collapse multiple exceptions into one sentence without violating the criterion and does not make individual exception grounds independently checkable without parsing sentence structure. A structured block with named fields makes each exception independently verifiable: a scorer reads the Grounds field per block without parsing prose, and the Ticket ID field makes cross-referencing against the ticket set unambiguous. The no-exception path prevents silent omission of the block when no violations are present -- a model cannot skip the acknowledgment mechanism because no exceptions triggered it. C-31 passes with any explicit exception acknowledgment in Part C sub-check (1); C-33 passes only when the acknowledgment mechanism is a structured per-ticket block with at least four named fields, and the no-exception case is also explicitly handled.
- **Pass condition**: Part C sub-check (1) uses a structured EXCEPTION SIGN-OFF BLOCK per exception with at least four named fields (Ticket ID, Phase, Assigned severity, Grounds), AND specifies the no-exception path explicitly. A prose exception acknowledgment -- even a detailed one naming all four components in sentence form -- does not pass. An EXCEPTION SIGN-OFF BLOCK that omits any of the four required fields does not pass. An output without C-31 cannot satisfy C-33.
- **Round 10 evidence**: V-04 and V-05 (Part C sub-check 1: EXCEPTION SIGN-OFF BLOCK with Ticket ID, Phase, Assigned severity, Grounds, Disposition per exception; no-exception path explicitly specified) satisfy C-33 and score C-31 PASS+. V-01, V-02, V-03 (Part C uses prose exception acknowledgment with outage/blocking test language and explicit compliance state) score C-31 PASS but fail C-33. The structured block makes each exception's Grounds field independently verifiable without parsing sentence structure; prose acknowledgment collapses grounds into sentence form with no structural field separation.

---

### C-34 -- Paraphrase Double-Gate with Step-4 Recall
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-30 requires one paraphrase gate before ticket generation; C-32 requires it to fire decision-adjacent at Step 4. C-34 requires both: a hard gate at the inference-rule step (STEP 2C) AND a separate paraphrase recall instruction at the decision step (Step 4 header) that explicitly references the earlier paraphrase by step name. The canonical Step 4 recall form: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from Step 2C]" -- the word "confirmed" and the "restate from Step 2C" clause require the model to retrieve and re-encode its STEP 2C commitment rather than produce an independent fresh paraphrase. The structural difference from C-32 (one decision-adjacent gate): a single Step 4 gate produces a paraphrase without the inference rule text in live generation context -- the rule text was at STEP 2C, several steps earlier. The double-gate ensures encoding at the rule step (rule text is live) and re-confirmation at the decision step (severity assignment is live). The explicit cross-reference "restate from Step 2C" closes the divergence path: the Step 4 recall cannot silently diverge from the STEP 2C commitment when the gate instruction names the earlier step by number. C-32 passes with one decision-adjacent gate at Step 4; C-34 passes only when gates fire at both the rule-statement step AND the decision step, with the Step 4 gate explicitly referencing the STEP 2C paraphrase by step name or label.
- **Pass condition**: (1) A hard paraphrase gate appears at the rule-statement step (e.g., STEP 2C) with "do not proceed" language and a named paraphrase slot; AND (2) a separate paraphrase recall instruction appears at the severity-assignment step (e.g., Step 4 header) that explicitly references the earlier paraphrase by step name (e.g., "restate from Step 2C", "confirmed from 2C", or equivalent cross-reference). A single gate at either position does not satisfy C-34. A Step 4 gate that does not reference the earlier paraphrase by step satisfies C-32 but not C-34. An output without C-30 cannot satisfy C-34.
- **Round 10 evidence**: V-05 (STEP 2C: hard gate with own-words paraphrase slot AND Step 4 header: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from 2C]") satisfies both C-30 and C-32 and additionally satisfies C-34. V-02 and V-04 (Step 4 decision-adjacent gate, no gate at STEP 2C) satisfy C-32 but fail C-34 -- no STEP 2C paraphrase slot exists for the Step 4 recall to reference. V-03 (hard gate at STEP 2C, no Step 4 gate) satisfies C-30 but fails both C-32 and C-34.

---

### C-35 -- Part C Paraphrase Consistency Confirmation
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-34 creates a paraphrase commitment at STEP 2C that is recalled at Step 4; C-31 Part C sub-check (1) audits tickets for C-28 directional compliance. Without C-35, the paraphrase and the audit are structurally parallel but not cross-linked: the paraphrase is a pre-generation commitment, the Part C audit is a post-generation check, and neither references the other. C-35 requires that after the exception scan in Part C sub-check (1), the audit explicitly quotes the model's own Step 2C paraphrase and states whether the audit result is consistent with that commitment. The canonical form: a Part C closing statement that cites the Step 2C paraphrase verbatim and confirms the scan found no violations inconsistent with the paraphrase (or, if exceptions exist, shows the quoted paraphrase and exception grounds side by side). The structural consequence: a model that violated the directional rule in ticket generation cannot pass Part C sub-check (1) without also flagging the contradiction between the audit findings and its own quoted paraphrase. This makes the STEP 2C paraphrase an auditable anchor cited inside the verification pass rather than a pre-generation ritual with no post-generation linkage. The Part C audit can reference and verify the paraphrase only when C-34's double-gate has produced a commitment at STEP 2C; an output with a Step-4-only gate (C-32 without C-34) has no named Step 2C paraphrase for Part C to quote. C-31 passes when both Part C sub-checks are present; C-34 passes when the double-gate creates a Step 2C paraphrase commitment; C-35 passes only when Part C sub-check (1) additionally quotes the Step 2C paraphrase and confirms the audit result is consistent with that commitment, or explicitly flags the contradiction if exceptions are found.
- **Pass condition**: After performing the C-28 directional compliance scan in Part C sub-check (1), the output quotes the model's own paraphrase from the rule-statement step (Step 2C or equivalent) verbatim and states whether the audit finding is consistent with the quoted paraphrase. If exceptions exist, the quoted paraphrase and the exception grounds are shown in proximity so the consistency or contradiction is visible. A Part C that audits directional compliance without citing the earlier paraphrase does not pass. An output without C-34 cannot satisfy C-35.
- **Round 10 evidence**: V-05 (Part C sub-check 1: EXCEPTION SIGN-OFF BLOCK followed by paraphrase consistency confirmation -- quotes Step 2C paraphrase value, confirms audit result is consistent with the quoted paraphrase) satisfies C-35 and scores C-31 PASS+ and C-34 PASS+. V-04 (structured EXCEPTION SIGN-OFF BLOCK in Part C, no paraphrase citation) satisfies C-33 but fails C-35 -- the exception block is self-contained and carries no reference to the earlier paraphrase commitment. V-01, V-02, V-03 (prose exception acknowledgment, no structured block, no paraphrase citation) fail both C-33 and C-35. The paraphrase consistency confirmation closes the loop between the pre-generation commitment and the post-generation verification; without it, the paraphrase and the audit are structurally isolated events that do not mutually constrain each other.

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

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 225

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
