## org-chart Quest Score — Round 4

**Rubric:** v4 (C-01 through C-18)
**Variations:** V-01 through V-05
**Reference:** R3 ceiling = 98.0 (V-01 and V-02 each, 8/10 aspirational); V-04/R3 not scored
**Scoring basis:** Prompt design evaluation (no trace artifact; scored against spec and rubric)

---

## V-01 — Full Aspirational Contract Under v4

**Axis:** lifecycle-emphasis (confirmed combined architecture — both Evolution + Anti-Pattern mandatory)

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Explicit: "DO write the Inertia Assessment before any org boxes. DO NOT write an org diagram as the first section." Section order enforces position 1. |
| C-02 | PASS | "DO show at minimum two levels. DO NOT produce a flat list of names without hierarchy." |
| C-03 | PASS | ROLES-LOADED/ROLES-NOTE block required before any other section. "DO NOT invent role names unless no roles files are found." |
| C-04 | PASS | Headcount table with Area/Headcount/Key Roles columns. "DO include at minimum two area rows with individual counts." |
| C-05 | PASS | "DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting. DO NOT combine two meetings into one row." |

**Essential: 5/5 (60 pts)**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Committee Charters section requires Purpose/Membership/Decides/Escalates. "DO NOT label this section optional." Charter required for each governance meeting. |
| C-07 | PASS | Section order list enumerates all eight sections. "DO NOT omit any of the eight sections." |
| C-08 | PASS | Five-column headcount table with explicit Decides and Escalates columns. "DO NOT write 'owns the area' or generic ownership phrases in either column." |

**Recommended: 3/3 (30 pts)**

### Aspirational (10 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | ORG EVOLUTION ROADMAP section: "DO NOT label it optional. DO NOT omit it." Requires concrete triggers; "The org will evolve... does not pass." |
| C-10 | PASS | ANTI-PATTERN WATCH section: "DO NOT label it optional. DO NOT omit it." Named anti-patterns + domain-specific rationale required. |
| C-11 | PASS | Case for Staying Flat sub-section: "DO include at minimum two numbered reasons." Labeled sub-section with code block template. |
| C-12 | PASS | Separate Decides and Escalates columns explicitly required. "DO NOT use a single 'Decision Scope' column." |
| C-13 | PASS | VERDICT block template includes "Re-assessment trigger:" field. "DO NOT write 'revisit as the team grows' — the trigger must name a threshold." |
| C-14 | PASS | "Each reason must name a mechanism (channel, informal lead, decision pattern, cadence)." Negative example given: "DO NOT write generic statements like 'the team communicates well.'" |
| C-15 | PASS | Three labeled sub-sections (### Case for Staying Flat, ### Rebuttal, ### VERDICT) all required with explicit markdown header templates. |
| C-16 | PASS | "DO populate Escalates with decision types referred upward, naming the destination role or forum." Committee charters: "DO populate the Escalates field with a named destination." |
| C-17 | PASS | Evolution table requires two rows. "Each row must address a distinct trigger — two headcount thresholds phrased differently do not count as distinct." Distinctness guard present. |
| C-18 | PASS | Anti-Pattern table "Why It Applies Here" column: "must reference a specific element of the org just designed." "must reference this specific org — not a generic warning." Named elements listed. |

**Aspirational: 10/10 (10 pts)**

**V-01 Total: 100.0 — Golden**

---

## V-02 — Trigger-Dimension Diversity Guard

**Axis:** output format (C-17 trigger-dimension diversity guard added to V-01 base)

All criteria identical to V-01 except C-17, which is materially strengthened:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-17 | PASS | Explicit Row 1/Row 2 dimension split: "Row 1 — headcount threshold... Row 2 — workload signal or structural symptom: NOT a headcount number." "The same trigger dimension restated at a different threshold does not count as a distinct row." Dimension vocabulary list provided (on-call span, PR latency, coordination failure, milestone events). This is stronger than V-01's generic distinctness guard. |

All other 17 criteria: PASS (identical to V-01).

**V-02 Total: 100.0 — Golden**

*Note: V-02's dimension guard closes the gap that V-01 leaves open — a model could interpret "phrased differently" as permitting "headcount reaches 15" and "headcount exceeds 20." V-02 forecloses that path explicitly.*

---

## V-03 — Domain-Anchor Enforcement

**Axis:** output format (C-18 named-element back-reference enforcement added to V-01 base)

All criteria identical to V-01 except C-18, which is materially strengthened:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-18 | PASS | Anti-Pattern section restructured with explicit named-element list: "The rationale must name at least one of the following elements drawn directly from the output above: An area name from the Headcount by Area table / A committee or cadence name from the Operating Rhythm Table or Committee Charters / The total headcount or an area's headcount count / A specific DRI role from the rhythm table." Negative example present: "DO NOT write: 'with multiple areas, committee capture is a risk' — that applies to any multi-area org." Correct example shows committee name cited from charters. |

C-17 uses V-01-level distinctness guard (no dimension-diversity guard). Minor risk that same-dimension triggers are produced, but "phrased differently do not count as distinct" should prevent same-number gaming.

All other 17 criteria: PASS (identical to V-01).

**V-03 Total: 100.0 — Golden**

---

## V-04 — Both Guards Combined

**Axis:** lifecycle-emphasis + output format (C-17 dimension-diversity guard + C-18 domain-anchor, both active)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01–C-16 | PASS | Same foundation as V-01 through V-03. No criterion degraded by combining the two guards; Evolution Roadmap and Anti-Pattern Watch sections are orthogonal and do not share structure. |
| C-17 | PASS | Full dimension-diversity guard from V-02: Row 1 = headcount, Row 2 = workload/structural-symptom/milestone. "DO NOT write two headcount thresholds." |
| C-18 | PASS | Full domain-anchor guard from V-03: named-element back-reference required; negative example given; named-element list provided. |

No interaction effect observed in prompt design: the Evolution Roadmap guard applies to section 7, the Anti-Pattern guard applies to section 8, and the inertia section (C-11, C-14) is unchanged from V-01. The 4-part inertia trap does not apply — V-04 maintains the 3-part structure.

**V-04 Total: 100.0 — Golden**

---

## V-05 — Descriptive Register Variant

**Axis:** phrasing register (descriptive/narrative throughout; all DO/DO NOT guards replaced with framing and rationale)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "The org diagram appears after the inertia assessment — never before it." Section order stated as fixed. |
| C-02 | PASS | "The diagram shows a hierarchy with at minimum two levels." |
| C-03 | PASS | "The first step is reading .roles/ for roles relevant to {topic}...Nothing else is written until this block is complete." |
| C-04 | PASS | Headcount table format shown. "At minimum two area rows with individual counts." |
| C-05 | PASS | "The rhythm table has at minimum three rows: the Review of Business (ROB), a shiproom or gate review, and a governance meeting...Each row is its own entry — two meetings do not share a row." |
| C-06 | PASS | "The charter section is not optional — if a committee appears in the rhythm table, its charter must appear here." Four fields (Purpose/Membership/Decides/Escalates) all specified. |
| C-07 | PASS | "The order is fixed. No section is optional." Eight sections enumerated. |
| C-08 | PASS | Decides/Escalates columns described. "A single 'Decision Scope' column does not capture the split the artifact needs." |
| C-09 | PASS | "This section describes how the proposed structure should change as the team grows. It takes the form of a trigger table with at minimum two rows." No "optional" qualifier. |
| C-10 | PASS | "This section identifies org anti-patterns that represent specific risks given the structure just designed." "At minimum two named anti-patterns with domain-specific rationale." |
| C-11 | PASS | "At minimum two mechanism entries are needed before this sub-section is complete." ### Case for Staying Flat heading in template. |
| C-12 | PASS | "The Decides and Escalates columns are separate." "'Everything else' is not a valid Escalates entry." |
| C-13 | PASS | "The re-assessment trigger states the concrete condition that would flip this verdict: a headcount threshold, a coordination-failure event, or a named milestone. A trigger should be a condition, not a direction." |
| C-14 | PASS | "Each item names an observable mechanism. A statement like 'the team communicates well' is a claim about quality, not a description of a mechanism." Positive and negative examples both present. Explicit mechanism requirement survives register change. |
| C-15 | PASS | "The assessment has three labeled sub-sections." Template shows ### headers for all three. |
| C-16 | PASS | "The Escalates column carries decision types referred upward, and names the destination role or forum that receives the escalation. 'Everything else' is not a valid Escalates entry." Destination-naming requirement preserved in descriptive form. |
| C-17 | PASS | "Two headcount thresholds stated at different numbers address the same dimension — a genuinely distinct second trigger names a different kind of event." Dimension vocabulary examples (workload signal, structural symptom, milestone) present. "Should" framing is softer than V-04's "DO NOT write two headcount thresholds" but the content is explicit enough to prevent same-dimension gaming. |
| C-18 | PASS | "A useful 'Why It Applies Here' entry names something from the artifact above: an area name from the headcount table, a committee or cadence name from the rhythm table or charters, the total headcount, or a specific DRI role." Template placeholder: "[Domain-specific rationale naming an element from the org above]." The named-element list is present; "should not be able to copy the entry into a different org's anti-pattern table" is a clear test. |

**Register-sensitivity assessment:**
- C-14 and C-16: Not load-bearing on DO/DO NOT. The descriptive guidance is equivalent in content. No score drop predicted.
- C-17 and C-18: The guards survive register change. Named-element list in C-18 template placeholder is the key anchor; dimension vocabulary list in C-17 section provides equivalent guidance. "Should" language is weaker but the explanatory framing more than compensates.

**V-05 Total: 100.0 — Golden**

*Finding: Register is not a binding variable. The descriptive framing of all ten aspirational criteria — including both new guards — produces equivalent prompting force when the explanatory content is explicit.*

---

## Round 4 Scorecard Summary

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 5/5 (60) | 3/3 (30) | 10/10 (10) | 100.0 | Golden |
| V-02 | 5/5 (60) | 3/3 (30) | 10/10 (10) | 100.0 | Golden |
| V-03 | 5/5 (60) | 3/3 (30) | 10/10 (10) | 100.0 | Golden |
| V-04 | 5/5 (60) | 3/3 (30) | 10/10 (10) | 100.0 | Golden |
| V-05 | 5/5 (60) | 3/3 (30) | 10/10 (10) | 100.0 | Golden |

**R3 → R4 trajectory:** 98.0 (V-01/R3, 8/10) → 100.0 (V-01/R4, 10/10). Ceiling confirmed.

---

## Excellence Signals

**The primary finding of R4** is a ceiling confirmation: V-04/R3 was already at ceiling. V-01/R4 (structurally V-04/R3 rewritten under v4 context) produces 10/10 aspirational across all five variation axes. The two new guards (C-17 dimension diversity, C-18 domain anchor) are reliably elicited by explicit prompt language in both imperative and descriptive register.

**Patterns from the ceiling variations (V-04 as reference):**

1. **Trigger-dimension diversity is an axis guard, not a wording guard.** V-01's "two headcount thresholds phrased differently do not count as distinct" operates on wording similarity. V-02/V-04's "Row 2 must NOT be a headcount number" operates on dimension identity. The axis guard is harder to game because it defines what Row 2 *is* (workload signal, structural symptom, or milestone) rather than what it *isn't* (a rephrasing). This is the correct formulation for C-17.

2. **Named-element back-reference is the minimal anchor for C-18 compliance.** Requiring the "Why It Applies Here" cell to cite a specific recognizable element from the artifact above (area name, committee name, headcount count, DRI role) forces coupling to the actual output. The test "a reader should not be able to copy this cell into a different org's anti-pattern table without it sounding wrong" is a precise correctness criterion in descriptive form. Both V-03 and V-05 confirm this pattern holds independent of prompt register.

3. **Register does not bind at this specification density.** V-05 matches V-04 across all ten aspirational criteria. When descriptive framing is accompanied by explicit named-element lists, vocabulary guides, and concrete negative examples, imperative DO/DO NOT guards are redundant rather than load-bearing. This expands the prompt author's stylistic latitude without affecting output quality.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Trigger-dimension diversity guard (Row 1 = headcount threshold, Row 2 = workload-signal or structural-symptom; NOT a second headcount number) reliably produces C-17-compliant Evolution Roadmap tables; axis-identity guard is stronger than wording-similarity guard", "Named-element back-reference enforcement (Why It Applies Here must cite area name, committee name, headcount count, or DRI role drawn from the artifact above) reliably produces C-18-compliant Anti-Pattern tables in both imperative and descriptive register"]}
```
