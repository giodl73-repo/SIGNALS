Rubric written to `simulations/quest/rubrics/listen-support-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (5) | C-01 field completeness, C-02 vocab compliance, C-03 persona grounding, C-04 gap analysis structure, C-05 ticket count + category spread | 60 |
| Recommended (3) | C-06 severity calibration, C-07 volume differentiation, C-08 persona-authentic bodies | 30 |
| Aspirational (2) | C-09 cross-ticket pattern, C-10 prioritized gap ranking | 10 |

The hardest essential to satisfy will be **C-03** — the model must both pick a valid stock role *and* write a body that sounds like that persona. The easiest failure mode for recommended is **C-07** — models tend to stamp everything "high" without differentiation.
uired fields: title, category, persona, predicted volume, and severity.
- **Pass condition**: Zero tickets are missing any of the five fields. A ticket with a blank or "N/A" field fails this criterion.

---

### C-02 -- Controlled Vocabulary Compliance
- **Weight**: essential
- **Category**: correctness
- **Text**: Category values are drawn exclusively from {how-to, bug, feature-request, config, integration}. Severity values are drawn exclusively from {P0, P1, P2, P3}. Volume values are drawn exclusively from {high, medium, low}.
- **Pass condition**: No ticket uses an out-of-vocabulary value in any controlled field. Synonyms or variants (e.g., "configuration", "High", "blocker") do not pass.

---

### C-03 -- Persona Grounding in Stock Roles
- **Weight**: essential
- **Category**: correctness
- **Text**: Every ticket's "persona most likely to file" is drawn from the stock role set: {Support, SRE, PM, UX, C-01 through C-12}. The sample ticket body is written in that persona's voice (vocabulary, concerns, and framing appropriate to the role).
- **Pass condition**: All ticket personas are valid stock roles, AND each sample body is written in first person from that persona's perspective with role-appropriate language. A generic body not tied to the named persona fails.

---

### C-04 -- Gap Analysis Present and Structured
- **Weight**: essential
- **Category**: coverage
- **Text**: The output contains a gap analysis section with three explicitly labeled sub-sections: doc gaps, design gaps, and operational gaps. Each sub-section contains at least one identified gap.
- **Pass condition**: All three gap sub-sections exist and are non-empty. A single combined "gaps" section without sub-categorization does not pass.

---

### C-05 -- Minimum Ticket Count and Category Spread
- **Weight**: essential
- **Category**: coverage
- **Text**: The output predicts at least five distinct tickets, and at least three of the five allowed categories (how-to, bug, feature-request, config, integration) are represented across the ticket set.
- **Pass condition**: Ticket count >= 5 AND at least 3 distinct category values present. An output with five how-to tickets and nothing else does not pass.

---

## Recommended Criteria (30 pts total -- output is better with these)

### C-06 -- Severity Calibration is Defensible
- **Weight**: recommended
- **Category**: depth
- **Text**: Severity assignments are internally consistent and defensible. P0/P1 tickets describe scenarios where the feature is broken or inaccessible (not cosmetic or nice-to-have). P2/P3 tickets reflect lower-impact or workaround-available situations. The distribution is not uniformly P2 (severity washing).
- **Pass condition**: No P0/P1 ticket describes a cosmetic or low-impact issue, AND no obvious blocker is rated P2/P3, AND at least two different severity levels appear in the ticket set.

---

### C-07 -- Volume Ratings are Differentiated and Reasoned
- **Weight**: recommended
- **Category**: depth
- **Text**: High/medium/low volume ratings vary across the ticket set (not all tickets are "high"). The relative assignments are plausible given the ticket category and the persona filing them (e.g., a configuration ticket from SRE would plausibly be lower volume than a how-to ticket from C-01 through C-12).
- **Pass condition**: All three volume levels appear, OR two levels appear with an explicit statement of why one level is absent. Uniform volume across all tickets fails.

---

### C-08 -- Sample Ticket Bodies Are Persona-Authentic
- **Weight**: recommended
- **Category**: behavior
- **Text**: Each sample ticket body reads like it was written by the named persona. SRE tickets use operational/infra language. PM tickets reference roadmap, user impact, or metrics. Customer persona tickets (C-01 through C-12) reflect that persona's domain, role, and pain. Generic "I have a problem with X" bodies are insufficient.
- **Pass condition**: At least 75% of sample bodies contain role-specific vocabulary, framing, or concerns that would not fit a different persona. A body that reads identically well for any persona fails.

---

## Aspirational Criteria (10 pts total -- raises the bar)

### C-09 -- Cross-Ticket Pattern Recognition
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output identifies a systemic pattern across multiple predicted tickets (e.g., "Five of the eight tickets trace to missing onboarding docs for the config namespace" or "Three tickets suggest the error message for auth failure is ambiguous"). This pattern is stated explicitly and connected to specific tickets by ID or title.
- **Pass condition**: At least one named cross-ticket pattern with explicit ticket references is present in the output.

---

### C-10 -- Prioritized Pre-Launch Gap Closing Signal
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The gap analysis concludes with a ranked or prioritized recommendation for which gaps to close before launch (not just a list). The ranking is tied to the severity and volume of tickets that the gap would prevent.
- **Pass condition**: The gap analysis section includes an explicit prioritization statement (e.g., "Close doc gap X first -- it drives the three high-volume P1 tickets") rather than an unordered list.

---

## Scoring Summary

| ID   | Text (short)                          | Weight       | Category    |
|------|---------------------------------------|--------------|-------------|
| C-01 | All 5 ticket fields present           | essential    | correctness |
| C-02 | Controlled vocabulary compliance      | essential    | correctness |
| C-03 | Persona from stock roles, voiced body | essential    | correctness |
| C-04 | Gap analysis with 3 sub-sections      | essential    | coverage    |
| C-05 | >= 5 tickets, >= 3 category types     | essential    | coverage    |
| C-06 | Severity calibration defensible       | recommended  | depth       |
| C-07 | Volume ratings differentiated         | recommended  | depth       |
| C-08 | Ticket bodies persona-authentic       | recommended  | behavior    |
| C-09 | Cross-ticket pattern identified       | aspirational | depth       |
| C-10 | Pre-launch gap closing prioritized    | aspirational | behavior    |
