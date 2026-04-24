Written to `simulations/quest/rubrics/listen-support-rubric-v5-2026-03-14.md`.

---

**What changed from v4 to v5:**

**Three new aspirational criteria from Round 4 PASS+ signals:**

**C-17 -- Gap-Bridged Coverage Table** (5 pts, depth)
Tightens C-15. C-15 requires a 2-column table (ticket ID / STATUS QUO element); C-17 requires a 3rd column ("Gap traced to") linking each ticket row to a named gap from the Gap Analysis, plus an explicit no-orphan-gap check. The 2-column table verifies ticket-to-STATUS-QUO coverage but leaves gap-orphan failures invisible; the 3rd column makes any gap absent from every row structurally visible without parsing prose. V-01 and V-04 satisfy C-17. V-03 (2-column) fails it.

**C-18 -- Per-Field Prohibited Sentinel** (5 pts, behavior)
Tightens C-16. C-16 requires flat sibling consequence fields with no container; C-18 additionally requires each flat field to carry an immediately adjacent `Prohibited:` sentinel naming the generic fill pattern that field is designed to prevent. Flat fields without sentinels still permit surface-compliant but content-free answers ("Phase 1 adopters" as a segment with no pattern-specific meaning). The sentinel closes that by making the disallowed form explicit at the field level. V-02 and V-04 satisfy C-18. V-01 (flat, no sentinels) fails it.

**C-19 -- Performance-Mode Persona Declaration** (5 pts, behavior)
New branch. C-03 and C-08 pass with any field instruction for first-person voice; C-19 passes only when the instruction is a mode declaration ("You ARE [persona name]. Do not write 'the user' or 'they'.") -- a stance shift before the card is read, not a reminder inside it. The same mechanism improves C-11: a persona speaking from experience produces traceable STATUS QUO elements that analyst-mode cannot. The third-person prohibition makes violations grep-checkable. V-03 and V-05 satisfy C-19 and both scored PASS+ on C-03, C-08, and C-11 simultaneously.

**Tier restructure:**
- Aspirational: 8 criteria / 40 pts -> 11 criteria / 55 pts
- Total ceiling: 130 -> 145

**Criterion progression chains:**
- Depth: C-13 (gate) -> C-15 (table) -> C-17 (gap-bridged)
- Behavior: C-14 (fields) -> C-16 (no container) -> C-18 (per-field sentinels)
- Behavior: C-03/C-08 (field instruction) -> C-19 (mode declaration)
 The key failure mode field-instruction permits: a model reading a first-person instruction at card level can slip back into third-person framing ("the SRE notices the pod is restarting") without violating the card structure. A mode declaration shifts the generation stance before the card is read; the prohibition on third-person pronouns makes the failure mode explicit. The same mechanism also improves C-11: a persona speaking from experience ("I spent 40 minutes on step 3 before the token expired") produces a more traceable STATUS QUO than an analyst describing the persona's experience. C-03 and C-08 pass with any first-person body; C-19 passes only when the mechanism is a mode declaration with an explicit third-person prohibition. V-03 and V-05 (performance mode + prohibition) satisfy C-19.

**Relationship to prior criterion pairs:**
- C-13 (enumeration gate) -> C-15 (table format) -> C-17 (gap-bridged table): each round adds one column of structural verification
- C-14 (separate consequence fields) -> C-16 (no container) -> C-18 (per-field sentinels): each round removes one more hiding place for generic fill
- C-03/C-08 (field instruction for persona voice) -> C-19 (mode declaration): mechanism upgrade from reminder to stance change

**Tier restructure:**
- Aspirational: 8 criteria / 40 pts -> 11 criteria / 55 pts
- Total ceiling: 130 -> 145 (scores above 130 require all eleven aspirational criteria)
- Essential and Recommended tiers are unchanged

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

## Aspirational Criteria (55 pts total -- raises the bar above 90)

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

## Scoring Summary

| ID   | Text (short)                               | Weight       | Points | Category    |
|------|--------------------------------------------|--------------|--------|-------------|
| C-01 | All 5 ticket fields present                | essential    | 12     | correctness |
| C-02 | Controlled vocabulary compliance           | essential    | 12     | correctness |
| C-03 | Persona from stock roles, voiced body      | essential    | 12     | correctness |
| C-04 | Gap analysis with 3 sub-sections           | essential    | 12     | coverage    |
| C-05 | >= 5 tickets, >= 3 category types          | essential    | 12     | coverage    |
| C-06 | Severity calibration defensible            | recommended  | 10     | depth       |
| C-07 | Volume ratings differentiated              | recommended  | 10     | depth       |
| C-08 | Ticket bodies persona-authentic            | recommended  | 10     | behavior    |
| C-09 | Cross-ticket pattern identified            | aspirational | 5      | depth       |
| C-10 | Pre-launch gap closing prioritized         | aspirational | 5      | behavior    |
| C-11 | STATUS QUO scenario grounding              | aspirational | 5      | depth       |
| C-12 | Pattern consequence framing                | aspirational | 5      | behavior    |
| C-13 | Self-verification coverage gate            | aspirational | 5      | depth       |
| C-14 | Structurally enforced consequence fields   | aspirational | 5      | behavior    |
| C-15 | Table-form coverage enumeration            | aspirational | 5      | depth       |
| C-16 | Container-free consequence field format    | aspirational | 5      | behavior    |
| C-17 | Gap-bridged coverage table                 | aspirational | 5      | depth       |
| C-18 | Per-field prohibited sentinel              | aspirational | 5      | behavior    |
| C-19 | Performance-mode persona declaration       | aspirational | 5      | behavior    |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 145

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-14 | Added C-11 (STATUS QUO grounding) and C-12 (pattern consequence framing) from Round 1 excellence signals; aspirational tier grows from 10 to 20 pts, total ceiling 110 |
| v3 | 2026-03-14 | Added C-13 (self-verification coverage gate) and C-14 (structurally enforced consequence fields) from Round 2 excellence signals; aspirational tier grows from 20 to 30 pts, total ceiling 120 |
| v4 | 2026-03-14 | Added C-15 (table-form coverage enumeration) and C-16 (container-free consequence field format) from Round 3 excellence signals; aspirational tier grows from 30 to 40 pts, total ceiling 130 |
| v5 | 2026-03-14 | Added C-17 (gap-bridged coverage table), C-18 (per-field prohibited sentinel), and C-19 (performance-mode persona declaration) from Round 4 excellence signals; aspirational tier grows from 40 to 55 pts, total ceiling 145 |
