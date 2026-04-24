Written to `simulations/quest/rubrics/listen-support-rubric-v2-2026-03-14.md`.

---

**What changed from v1 to v2:**

Two new aspirational criteria extracted from V-05's Round 1 performance:

**C-11 -- STATUS QUO Scenario Grounding** (5 pts, depth)
The single mechanism behind V-05's wins on both C-07 and C-08. A concrete current-state description (what users are doing today, what workarounds exist) anchors volume ratings and ticket bodies to a specific scenario instead of the abstract. Pass condition requires the STATUS QUO section to actually be referenced in ticket content -- a floating preamble that never connects to tickets doesn't count.

**C-12 -- Pattern Consequence Framing** (5 pts, behavior)
The distinguishing element of V-05's C-09 over V-04's. V-04 required Name + Tickets + Root cause. V-05 added "Not closing this means:" -- a forward-looking impact statement that turns diagnosis into cost framing. Pass condition requires the consequence to be specific to the named pattern; generic "this will cause confusion" fails.

**Tier restructure:**
- Aspirational: 2 criteria → 4 criteria, 10 pts → 20 pts
- Total ceiling: 100 → 110 (scores above 100 require all four aspirational criteria)
- Essential and Recommended tiers are unchanged
, predicted volume, and severity.
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

## Aspirational Criteria (20 pts total -- raises the bar above 100)

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

## Scoring Summary

| ID   | Text (short)                             | Weight       | Points | Category    |
|------|------------------------------------------|--------------|--------|-------------|
| C-01 | All 5 ticket fields present              | essential    | 12     | correctness |
| C-02 | Controlled vocabulary compliance         | essential    | 12     | correctness |
| C-03 | Persona from stock roles, voiced body    | essential    | 12     | correctness |
| C-04 | Gap analysis with 3 sub-sections         | essential    | 12     | coverage    |
| C-05 | >= 5 tickets, >= 3 category types        | essential    | 12     | coverage    |
| C-06 | Severity calibration defensible          | recommended  | 10     | depth       |
| C-07 | Volume ratings differentiated            | recommended  | 10     | depth       |
| C-08 | Ticket bodies persona-authentic          | recommended  | 10     | behavior    |
| C-09 | Cross-ticket pattern identified          | aspirational | 5      | depth       |
| C-10 | Pre-launch gap closing prioritized       | aspirational | 5      | behavior    |
| C-11 | STATUS QUO scenario grounding            | aspirational | 5      | depth       |
| C-12 | Pattern consequence framing              | aspirational | 5      | behavior    |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 110

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-14 | Added C-11 (STATUS QUO grounding) and C-12 (pattern consequence framing) from Round 1 excellence signals; aspirational tier grows from 10 to 20 pts, total ceiling 110 |
