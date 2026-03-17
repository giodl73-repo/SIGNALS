---

## Quest Scorecard: listen-support Round 3

**Rubric**: v3 (14 criteria, 120 pts ceiling)

### Summary

| V | Description | C-13 | C-14 | Total |
|---|-------------|------|------|-------|
| **V-04** | C-13 table + C-14 flat fields (minimal upgrade) | PASS / 5 | PASS / 5 | **120 / 120** |
| **V-05** | Full synthesis R3 (table + flat + inertia framing) | PASS / 5 | PASS / 5 | **120 / 120** |
| V-01 | C-13 enumeration table (V-05 R2 consequence) | PASS / 5 | PARTIAL / 4 | **119 / 120** |
| V-02 | C-14 flat fields (V-05 R2 text check) | PARTIAL / 4 | PASS / 5 | **119 / 120** |
| V-03 | Inertia framing (V-05 R2 text + nested bullets) | PARTIAL / 4 | PARTIAL / 4 | **118 / 120** |

All essential and recommended criteria: PASS for all five variations (90/90 each).
V-05 R2 baseline on v3 rubric: 118 / 120 (C-13 partial/4, C-14 partial/4).

---

### Experiment results

**1. Does the table matter for C-13?** Yes, decisively. V-01 (table) scores 5/5; V-02 (text check) scores 4/5. V-05 R2's text-format check permits a model to write "T-01 and T-02 both trace to X. Count: 2. Passes." -- a compact summary that mentions IDs without independent per-ticket enumeration. The table forces one row per ticket; row count is self-verifying.

**2. Must consequence fields be flat for C-14?** Yes. V-02 (flat) scores 5/5; V-01 (nested bullets under `Consequence:`) scores 4/5. V-05 R2's nested bullets ARE structurally separate in content requirements, but the parent `Consequence:` container creates a semantic grouping -- a model treats it as one section rather than three independent fields. Flat sibling-level fields (at the same level as `Pattern name:`) are each independently checkable without the container.

**3. Does inertia framing risk C-01/C-02?** No. V-03 passes all essential criteria cleanly; controlled vocabulary is still enforced at the template top and inertia framing occupies separate fields that don't collide with card controlled fields. The quality improvements to C-07/C-08/C-12 are real but not rubric-measurable since those criteria were already at ceiling.

**4. V-04 ceiling test.** Confirmed: two field-format changes (text → table, nested → flat) are sufficient to reach 120/120. No new framing required.

**5. V-05 vs. V-04.** Both 120/120. V-05 produces better quality on C-07/C-08/C-10/C-12 via defection-risk calibration and named reversion paths in consequence fields -- real improvements, but invisible in rubric scoring since prior criteria were at ceiling.

---

### Excellence signals

1. **Enumeration table is the C-13 structural gate** -- text-format check with example permits paragraph collapse; table row-per-ticket makes collapse impossible and count self-verifying
2. **Flat sibling-level consequence fields are the C-14 structural gate** -- parent container creates semantic grouping that allows container-level compliance with component-level genericity; flat fields eliminate the container entirely
3. **Minimal upgrade path confirmed** -- table + flat fields alone closes the 118→120 gap, establishing the minimum-change path for teams on V-05 R2

**V-Golden**: V-05 (120/120, richest mechanisms across all 14 criteria). V-04 as minimal-overhead alternative for teams where prompt simplicity is the primary constraint.

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["enumeration table structurally enforces per-ticket independence for C-13 -- text-format check with example permits paragraph collapse; table form makes row count self-verifying and single-sentence summaries impossible", "flat top-level consequence fields with no parent container are the C-14 structural gate -- nested bullets under a Consequence: parent create a semantic grouping that allows container-level compliance with component-level genericity; flat sibling-level fields are each independently checkable", "minimal structural upgrade path (table + flat fields only) is sufficient to reach 120/120 without framing changes -- confirms field format is the deterministic mechanism for C-13/C-14"]}
```
urally enforced consequence specificity | aspirational | 5 | PARTIAL / 4 | V-05 R2 consequence structure inherited: three bullet points under a parent "Consequence:" label (- Affected segment: / - Day-90 scenario: / - Adoption cost:). The three bullets ARE separately labeled and require different named content -- no single generic sentence satisfies all three. However, the parent "Consequence:" container creates a semantic grouping that permits a model to treat the three bullets as a single "Consequence section" rather than as fully independent fields. The structural boundary is weaker than flat fields. Each bullet is addressable and labeled, producing stronger than FAIL behavior; the parent container prevents PASS. |

**V-01 Total: 119 / 120**

---

### V-02: C-14 Flat Consequence Fields

| Criterion | Weight | Points | Result | Evidence |
|-----------|--------|--------|--------|---------|
| C-01 All 5 ticket fields present | essential | 12 | PASS / 12 | All five fields present. V-05 R2 base unchanged. |
| C-02 Controlled vocabulary compliance | essential | 12 | PASS / 12 | Vocabulary enforced. |
| C-03 Persona from stock roles, voiced body | essential | 12 | PASS / 12 | Stock roles listed. Body requires STATUS QUO connection reference + role-specific vocabulary. |
| C-04 Gap analysis with 3 sub-sections | essential | 12 | PASS / 12 | Three sub-sections + Priority Close Order. |
| C-05 >= 5 tickets, >= 3 category types | essential | 12 | PASS / 12 | Phase minimums + COVERAGE CHECKS category gate. |
| C-06 Severity calibration defensible | recommended | 10 | PASS / 10 | P0/P1 vs P2/P3 criteria stated. Phase gradient separates severity. |
| C-07 Volume ratings differentiated | recommended | 10 | PASS / 10 | Three-layer volume enforcement inherited from V-05 R2. |
| C-08 Ticket bodies persona-authentic | recommended | 10 | PASS / 10 | Named STATUS QUO connection field + role-specific vocabulary requirement. |
| C-09 Cross-ticket pattern identified | aspirational | 5 | PASS / 5 | CROSS-TICKET PATTERN with phase-labeled ticket IDs. |
| C-10 Pre-launch gap closing prioritized | aspirational | 5 | PASS / 5 | Priority Close Order with gap-to-ticket-data ties. |
| C-11 STATUS QUO scenario grounding | aspirational | 5 | PASS / 5 | Named connection field + text traceability check (V-05 R2 mechanism). The text check requires naming at least two ticket IDs with STATUS QUO elements, same as V-05 R2. |
| C-12 Pattern consequence framing | aspirational | 5 | PASS / 5 | Four flat consequence fields ("Consequence -- Affected segment:", "Consequence -- Day-90 scenario:", "Consequence -- Adoption cost:") with explicit anti-generic fail condition. Flat format is at least as strong as V-05 R2's nested bullets for C-12. |
| C-13 Self-verification coverage gate | aspirational | 5 | PARTIAL / 4 | V-05 R2 text-format traceability check inherited (unchanged). Format: "List the ticket IDs whose STATUS QUO connection field names a specific STATUS QUO element... Example: 'T-01 -- traces to GitHub Issues channel gap; T-02 -- traces to missing setup doc. Count: 2. Passes.'" The example format shows per-ticket enumeration, but the text field allows a model to write: "T-01 and T-02 both trace to missing setup doc. Count: 2. Passes." -- this is a summary statement that mentions ticket IDs without truly independent per-ticket enumeration. Paragraph collapse is permitted by the format. Partial enumeration present; structural gate absent. |
| C-14 Structurally enforced consequence specificity | aspirational | 5 | PASS / 5 | CROSS-TICKET PATTERN consequence uses flat labeled fields at sibling level to "Pattern name:", "Pattern tickets:", "Pattern root cause:": "Consequence -- Affected segment:", "Consequence -- Day-90 scenario:", "Consequence -- Adoption cost:". No parent "Consequence:" container. Each field is independently checkable without reference to the others. A model filling these fields cannot satisfy all three with a single generic statement because: (1) Affected segment requires a named role/cohort; (2) Day-90 scenario requires a specific event and ticket IDs; (3) Adoption cost requires a quantified or qualified friction. The flat format makes structural separation unambiguous. |

**V-02 Total: 119 / 120**

---

### V-03: Inertia Framing -- STATUS QUO as Competing Solution

| Criterion | Weight | Points | Result | Evidence |
|-----------|--------|--------|--------|---------|
| C-01 All 5 ticket fields present | essential | 12 | PASS / 12 | All five fields present in every card. COMPETING SOLUTION section replaces STATUS QUO section as setup but does not remove any card fields. Controlled vocabulary header unchanged. |
| C-02 Controlled vocabulary compliance | essential | 12 | PASS / 12 | "Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration}; severity in {P0, P1, P2, P3}; volume in {high, medium, low}" stated at top. Competitor framing adds context to volume rationale but does not replace controlled values. |
| C-03 Persona from stock roles, voiced body | essential | 12 | PASS / 12 | Stock roles listed. Body instructions require reference to competing-solution context + role-specific vocabulary. Body grounding is stronger than V-05 R2 (persona tried competing solution first -- specific behavioral anchor). |
| C-04 Gap analysis with 3 sub-sections | essential | 12 | PASS / 12 | Doc, Design, Operational sub-sections present + Priority Close Order with reversion-risk ranking. Enhanced by competitor framing (each gap notes reversion path it leaves open). |
| C-05 >= 5 tickets, >= 3 category types | essential | 12 | PASS / 12 | Phase minimums unchanged. COVERAGE CHECKS category gate unchanged. |
| C-06 Severity calibration defensible | recommended | 10 | PASS / 10 | P0/P1 vs P2/P3 criteria stated. Severity rationale note: "if the competing solution is the available workaround, state that explicitly" -- this sharpens P2/P3 calibration. Competing-solution workaround IS the canonical workaround-available scenario for P2/P3 assignments. |
| C-07 Volume ratings differentiated | recommended | 10 | PASS / 10 | Inertia framing produces sharper volume calibration: volume rationale must answer "how many users will file this vs. revert?" (defection-risk framing) rather than just population size. Defection anchor names the specific persona most likely to revert, producing non-uniform volume assignments by construction. Phase gradient still present. |
| C-08 Ticket bodies persona-authentic | recommended | 10 | PASS / 10 | Body instructions require persona to reference what they did in the competing solution before filing. This is the strongest C-08 mechanism across all R3 variations -- it names a specific behavioral anchor (what workaround they tried) rather than just "reference STATUS QUO connection." |
| C-09 Cross-ticket pattern identified | aspirational | 5 | PASS / 5 | CROSS-TICKET PATTERN section with pattern name, phase-labeled ticket IDs, root cause traced to COMPETING SOLUTION element. |
| C-10 Pre-launch gap closing prioritized | aspirational | 5 | PASS / 5 | Priority Close Order with reversion-risk ranking: "A gap that leaves the competing solution's primary advantage intact ranks higher than a cosmetic gap, regardless of ticket volume alone." This is a stronger prioritization mechanism than V-05 R2's severity/volume ranking alone. |
| C-11 STATUS QUO scenario grounding | aspirational | 5 | PASS / 5 | COMPETING SOLUTION section is the equivalent current-state section. Named "STATUS QUO connection:" field required per card (pointing to competing-solution elements). Text traceability check in COVERAGE CHECKS requires listing ticket IDs with named competing-solution elements (same format as V-05 R2). Volume anchor in COMPETING SOLUTION section (Defection anchor + Volume anchor fields). C-11 pass condition is met. |
| C-12 Pattern consequence framing | aspirational | 5 | PASS / 5 | Three-part nested consequence structure with reversion-path framing: Affected segment must name "who is still at risk of reverting"; Adoption cost must name "what the competing solution retains." Inertia framing makes consequence specificity stronger than V-05 R2 because the reversion path is a named, concrete consequence distinct per pattern. |
| C-13 Self-verification coverage gate | aspirational | 5 | PARTIAL / 4 | V-05 R2 text-format traceability check inherited (renamed to reference "competing-solution elements" but same structural format). Example: "T-01 -- traces to defection anchor (C-04 SQL reversion threshold); T-02 -- traces to switching friction (high, competing solution is well-known). Count: 2. Passes." Competitor element naming in the example is richer than V-05 R2's example, which may produce better element naming in practice. However, the text format still permits paragraph collapse: "T-01 and T-02 both trace to high switching friction. Count: 2. Passes." No table row structure to enforce per-ticket independence. |
| C-14 Structurally enforced consequence specificity | aspirational | 5 | PARTIAL / 4 | V-05 R2 nested bullet consequence structure inherited (under "Consequence:" parent label). Inertia framing enriches content specificity -- each bullet now requires naming the reversion path explicitly, which makes generic statements harder in practice. However, the parent "Consequence:" container is still present; the fields are still nested bullets rather than flat top-level fields. Structural separation meets C-14's intent (three separately labeled bullets with different content requirements), but the parent container prevents a full structural pass. Same verdict as V-01: 4/5. |

**V-03 Total: 118 / 120**

---

### V-04: C-13 Table + C-14 Flat Fields (Minimal Upgrade)

| Criterion | Weight | Points | Result | Evidence |
|-----------|--------|--------|--------|---------|
| C-01 All 5 ticket fields present | essential | 12 | PASS / 12 | All five fields present. V-05 R2 base unchanged except two field-format changes in COVERAGE CHECKS and CROSS-TICKET PATTERN. |
| C-02 Controlled vocabulary compliance | essential | 12 | PASS / 12 | Vocabulary enforced at top of template. |
| C-03 Persona from stock roles, voiced body | essential | 12 | PASS / 12 | Stock roles listed. Named STATUS QUO connection field + role-specific body requirement. |
| C-04 Gap analysis with 3 sub-sections | essential | 12 | PASS / 12 | Three sub-sections + Priority Close Order with STATUS QUO root cause. |
| C-05 >= 5 tickets, >= 3 category types | essential | 12 | PASS / 12 | Phase minimums + COVERAGE CHECKS category gate. |
| C-06 Severity calibration defensible | recommended | 10 | PASS / 10 | P0/P1 vs P2/P3 criteria stated. Phase gradient separates severity. |
| C-07 Volume ratings differentiated | recommended | 10 | PASS / 10 | Three-layer volume enforcement (STATUS QUO volume anchor + phase gradient + COVERAGE CHECKS volume gate) inherited from V-05 R2. |
| C-08 Ticket bodies persona-authentic | recommended | 10 | PASS / 10 | Named STATUS QUO connection field + role-specific vocabulary requirement. |
| C-09 Cross-ticket pattern identified | aspirational | 5 | PASS / 5 | CROSS-TICKET PATTERN with phase-labeled ticket IDs and STATUS QUO root cause trace. |
| C-10 Pre-launch gap closing prioritized | aspirational | 5 | PASS / 5 | Priority Close Order with STATUS QUO root cause tied to ticket data. |
| C-11 STATUS QUO scenario grounding | aspirational | 5 | PASS / 5 | Named STATUS QUO connection field + STATUS QUO TRACE ENUMERATION table (V-01 mechanism). Table format provides stronger C-11 verification than V-05 R2's text check -- row count is self-evident and per-ticket enumeration is structurally enforced. |
| C-12 Pattern consequence framing | aspirational | 5 | PASS / 5 | Flat consequence fields with explicit anti-generic fail condition (same mechanism as V-02). "A statement that could be copied verbatim to any other pattern does not pass any consequence field." Three independently addressable fields + named fail condition. |
| C-13 Self-verification coverage gate | aspirational | 5 | PASS / 5 | STATUS QUO TRACE ENUMERATION table with one row per traced ticket (Ticket ID, STATUS QUO element named, Element type). Same structural mechanism as V-01. Row count is self-verifying. Single-sentence summaries are structurally impossible -- each ticket must occupy its own row. Gate: "If the table has fewer than 2 rows, revise those ticket cards before proceeding." |
| C-14 Structurally enforced consequence specificity | aspirational | 5 | PASS / 5 | Flat consequence fields ("Consequence -- Affected segment:", "Consequence -- Day-90 scenario:", "Consequence -- Adoption cost:") at sibling level to "Pattern name:", "Pattern tickets:", "Pattern root cause:". No parent "Consequence:" container. Same mechanism as V-02. Each field independently checkable; structural separation unambiguous. Explicit prohibition: "Do not nest these inside a 'Consequence:' parent block. Do not collapse into a single sentence." Pass condition met. |

**V-04 Total: 120 / 120**

---

### V-05: Full Synthesis R3

| Criterion | Weight | Points | Result | Evidence |
|-----------|--------|--------|--------|---------|
| C-01 All 5 ticket fields present | essential | 12 | PASS / 12 | All five fields present across all card sections. COMPETING SOLUTION replaces STATUS QUO setup section but does not remove any card fields. |
| C-02 Controlled vocabulary compliance | essential | 12 | PASS / 12 | Vocabulary enforced at top of template. Inertia framing adds context fields (Defection anchor, Volume anchor) that do not overlap with controlled vocabulary fields. |
| C-03 Persona from stock roles, voiced body | essential | 12 | PASS / 12 | Stock roles listed. Body requires competing-solution behavioral context + role-specific vocabulary. Strongest C-03 mechanism -- bodies must reference what the persona did in the old tool before filing, anchoring persona authenticity to a concrete pre-filing behavior. |
| C-04 Gap analysis with 3 sub-sections | essential | 12 | PASS / 12 | Doc, Design, Operational sub-sections + Priority Close Order with reversion-risk ranking. |
| C-05 >= 5 tickets, >= 3 category types | essential | 12 | PASS / 12 | Phase minimums + COMPETING SOLUTION TRACE ENUMERATION table + COVERAGE CHECKS category gate. |
| C-06 Severity calibration defensible | recommended | 10 | PASS / 10 | P0/P1 vs P2/P3 criteria stated. "If the competing solution is the available workaround, state that explicitly" in severity rationale -- produces defensible P2/P3 assignments where the competing solution is the named workaround. |
| C-07 Volume ratings differentiated | recommended | 10 | PASS / 10 | Sharpest volume mechanism across all R3 variations: "how many users will file this vs. revert to the competing solution?" forces non-uniform volume by referencing defection-risk per ticket. Defection anchor names the persona most likely to revert and their threshold, preventing uniform volume assignments. Phase gradient + volume gate present as secondary enforcement. |
| C-08 Ticket bodies persona-authentic | recommended | 10 | PASS / 10 | Strongest C-08 mechanism: bodies must reference "what the persona tried in the competing solution before filing -- what they did in the old tool, what failed to transfer." Competing-solution behavioral anchor is the most specific grounding mechanism across all variations. |
| C-09 Cross-ticket pattern identified | aspirational | 5 | PASS / 5 | CROSS-TICKET PATTERN with pattern name, phase-labeled ticket IDs, root cause traced to COMPETING SOLUTION element (switching friction, defection anchor, or current solution gap). |
| C-10 Pre-launch gap closing prioritized | aspirational | 5 | PASS / 5 | Priority Close Order with reversion-risk ranking: "A gap that leaves the competing solution's primary advantage intact ranks higher regardless of ticket volume alone." Sharpest prioritization mechanism across all variations. |
| C-11 STATUS QUO scenario grounding | aspirational | 5 | PASS / 5 | COMPETING SOLUTION section provides current-state grounding (named tool, switching friction, defection anchor). Named STATUS QUO connection field per card. COMPETING SOLUTION TRACE ENUMERATION table (strongest C-11 verifier: one row per ticket, structural enumeration, per-ticket independence enforced). |
| C-12 Pattern consequence framing | aspirational | 5 | PASS / 5 | Flat consequence fields with reversion-path framing: Affected segment must name who is "still at reversion risk"; Day-90 scenario must name "what reversion behavior is still active"; Adoption cost must name "what the competing solution retains." Every consequence field now names the competing solution explicitly -- a generic statement fails because it cannot name a reversion path that the pattern keeps open. Strongest C-12 mechanism across all variations. |
| C-13 Self-verification coverage gate | aspirational | 5 | PASS / 5 | COMPETING SOLUTION TRACE ENUMERATION table with one row per traced ticket (Ticket ID, Competing-solution element, Element type: current-solution / switching-friction / solution-gap / defection-anchor). Element types are extended for competitor framing, making the named element requirement richer than V-01/V-04's STATUS QUO element types. Row count is self-verifying. Explicit gate: "If the table has fewer than 2 rows, revise those ticket cards before proceeding." |
| C-14 Structurally enforced consequence specificity | aspirational | 5 | PASS / 5 | Flat consequence fields with reversion-path content requirements. Same structural format as V-02 and V-04. Additionally: each field now names the competing solution explicitly, making the content requirement more specific than V-04's neutral framing. "Consequence -- Adoption cost" must name "what the competing solution retains" -- this is a pattern-specific named element that no generic statement can satisfy. Strongest C-14 implementation: structural separation (flat fields) + content-level reversion-path specificity. |

**V-05 Total: 120 / 120**

---

## Experiment Results

### Experiment 1: Does the enumeration table matter for C-13, or does V-05 R2's text check already pass?

**V-01 (table) vs. V-02 (text check)**:
- V-01 C-13: PASS / 5
- V-02 C-13: PARTIAL / 4

**Conclusion: Table form is the load-bearing mechanism for C-13.** V-05 R2's text check, even with an example showing per-ticket enumeration, permits paragraph collapse: "T-01 and T-02 both trace to X. Count: 2. Passes." satisfies the text field's constraint while summarizing across tickets. The table forces one row per ticket -- structural row independence makes per-ticket enumeration mandatory and row count trivially verifiable.

---

### Experiment 2: Are V-05 R2's nested bullets structurally sufficient for C-14, or must the fields be flat?

**V-02 (flat fields) vs. V-01 (nested bullets)**:
- V-02 C-14: PASS / 5
- V-01 C-14: PARTIAL / 4

**Conclusion: Flat fields are necessary for a full C-14 pass.** V-05 R2's three labeled bullets under "Consequence:" parent ARE structurally separate (different content requirements per bullet, no single generic sentence satisfies all three). But the parent container creates a semantic grouping -- a model treats the Consequence section as a single unit rather than as three independently-addressable fields. Flat top-level fields (at sibling level to "Pattern name:", "Pattern tickets:", etc.) are each independently checkable without reference to the others or to a parent container. The flat format makes the structural separation unambiguous.

---

### Experiment 3: Does inertia framing improve C-07/C-12 quality without sacrificing C-01/C-02 compliance?

**V-03 vs. V-05 R2 baseline (118)**:
- V-03 C-01/C-02: PASS (no vocabulary compliance issues -- controlled vocabulary header unchanged; inertia framing occupies separate fields that do not collide with card controlled fields)
- V-03 C-07: PASS (defection-risk volume framing is sharper than population-size framing; volume anchor is enriched by defection anchor)
- V-03 C-08: PASS (strongest body grounding mechanism -- named competing solution produces most specific behavioral anchor for persona voices)
- V-03 C-12: PASS (reversion-path framing makes consequence statements more specific than V-05 R2 -- each consequence field names what the competing solution retains)

**Conclusion: Inertia framing improves C-07, C-08, and C-12 quality without introducing compliance risks.** V-03's 118/120 is not due to quality degradation on C-01-C-12 -- it matches V-05 R2's full 110 on those criteria. The 2-point gap to 120 comes entirely from inherited structural limitations on C-13 and C-14 (text check, nested bullets). The inertia framing's quality improvements are real but not rubric-measurable since the prior criteria were already at ceiling (10/10 each for C-06-C-08, 5/5 each for C-09-C-12).

---

### Experiment 4: V-04 ceiling test -- is the minimal structural upgrade sufficient to reach 120?

**V-04: 120 / 120**

**Conclusion: Yes.** Two field-format changes (text check → table; nested bullets → flat fields) are sufficient to move from V-05 R2's 118 to 120 with no other changes. This is the minimal-overhead path to the ceiling. Teams that want 120/120 without adopting competitor framing overhead can use V-04 directly.

---

### Experiment 5: Does inertia framing add value on top of the structural upgrades?

**V-05 (120) vs. V-04 (120)**:

**Conclusion: No measurable rubric delta; real quality improvement present.** Both score 120/120. The inertia framing in V-05 produces measurably better quality on C-07 (defection-risk calibration sharper than population framing), C-08 (competing-solution behavioral anchor is more specific than STATUS QUO connection field), C-10 (reversion-risk prioritization is stronger than severity/volume ranking alone), and C-12/C-14 (named reversion path in consequence fields prevents generic content by naming a specific thing the competing solution retains). These improvements are real but invisible in rubric scoring because C-07, C-08, C-10, C-12 were already at ceiling. V-05 is recommended for teams where consequence specificity and volume calibration quality matter beyond rubric compliance; V-04 is recommended for teams where prompt simplicity is the primary constraint.

---

## Excellence Signals

1. **Enumeration table as the C-13 structural gate**: The load-bearing mechanism for C-13 is structural row-independence, not the presence of ticket IDs in text. A markdown table with one row per ticket makes paragraph collapse impossible -- the table format itself enforces per-ticket enumeration. The row count is self-verifying and visible at a glance. Text-format checks with example formatting can be satisfied by compact prose that mentions IDs without truly enumerating them.

2. **Flat consequence fields (no parent container) as the C-14 structural gate**: The load-bearing mechanism for C-14 is field-level independence without a semantic parent container. Three nested bullets under "Consequence:" are structurally separate in content requirements but grouped by the parent label. Flat top-level fields (sibling-level to other pattern fields like "Pattern name:") are independently checkable and cannot be grouped. The flat format makes the structural separation unambiguous and eliminates the container-escape risk.

3. **Minimal structural upgrade path confirmed**: V-04 demonstrates that the two field-format changes (table + flat fields) are sufficient to close the 2-point gap from V-05 R2's 118/120 to 120/120. No new framing, no new sections, no new phases required. This establishes a minimal-overhead upgrade path for teams already using V-05 R2.

---

## V-Golden Candidate

**V-05** is the golden candidate. It achieves 120/120 and is structurally the strongest variation across all 14 criteria:
- C-13: COMPETING SOLUTION TRACE ENUMERATION table (richest element type vocabulary: current-solution / switching-friction / solution-gap / defection-anchor)
- C-14: Flat consequence fields with reversion-path content requirements (structural separation + content specificity combined)
- C-07/C-08: Defection-risk framing produces the sharpest volume calibration and most specific persona body anchors
- C-10: Reversion-risk prioritization ranks gaps by what the competing solution retains, not just ticket severity
- C-12: Named reversion path in every consequence field prevents generic statements at both structural and content level

**V-04** is the recommended minimal-overhead alternative for teams that want 120/120 without adopting competitor framing. V-04 reaches the rubric ceiling with two targeted field-format changes to V-05 R2 and no new sections or framing vocabulary.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["enumeration table structurally enforces per-ticket independence for C-13 -- text-format check with example permits paragraph collapse; table form makes row count self-verifying and single-sentence summaries impossible", "flat top-level consequence fields with no parent container are the C-14 structural gate -- nested bullets under a Consequence: parent create a semantic grouping that allows container-level compliance with component-level genericity; flat sibling-level fields are each independently checkable", "minimal structural upgrade path (table + flat fields only) is sufficient to reach 120/120 without framing changes -- confirms field format is the deterministic mechanism for C-13/C-14"]}
```
