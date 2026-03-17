Rubric written to `simulations/quest/rubrics/scout-compliance-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (5, 60 pts)** — the hard correctness tests:
- C-01: Framework inference without prompting (>=4 frameworks from input alone)
- C-02: Scope boundary — Signal is not the vendor, Claude Code is
- C-03: SR 11-7 applies to Claude the model, not Signal the methodology (disqualifying error if wrong)
- C-04: Git-native design surfaced as compliance-favorable
- C-05: Findings register with IDs and severity (>=4 entries)

**Recommended (3, 30 pts)** — depth and decision-quality:
- C-06: Requirements matrix with SATISFIED / ACTION split
- C-07: Actionable adoption-readiness verdict (not hedged)
- C-08: Conditional frameworks (PCI DSS, GDPR) flagged as conditional, not universal

**Aspirational (2, 10 pts)** — raise the bar:
- C-09: The reframe — "approving Signal is approving a process, not a vendor"
- C-10: NPI/data-sensitivity tiering gap identified with concrete remediation

The trace artifact scores 100/100 and GOLDEN against this rubric.
ntifies that the primary compliance surface is Claude Code (the tool sending repo content to the Anthropic API), not Signal (the methodology). Must not attribute Signal as a vendor risk. | correctness | essential | Output explicitly states that vendor assessment scope is Claude Code / Anthropic, not Signal, and does not treat Signal itself as an assessable vendor or data processor. |
| C-03 | **SR 11-7 scope: model vs. methodology** -- Correctly identifies that SR 11-7 (model risk management) applies to Claude (the AI model), not to Signal (a structured prompt methodology). Misclassifying Signal as an AI model under SR 11-7 is a disqualifying error. | correctness | essential | Output explicitly states SR 11-7 applies to Claude/the model, not to Signal. Bonus if it notes that Signal's documented methodology IMPROVES SR 11-7 posture. |
| C-04 | **Git-native design surfaced as compliance-favorable** -- Surfaces the absence of a server, SaaS layer, or external data persistence as a compliance advantage. Must connect git-native design to at least one specific compliance property (audit trail, data residency, or artifact persistence). | coverage | essential | Output identifies >= 1 specific compliance benefit of the git-native, no-server design and links it to a named framework or requirement category. |
| C-05 | **Findings register with severity** -- Produces a structured findings register with IDs (e.g., SF-01...), finding descriptions, and severity or priority labels. Register must contain >= 4 entries. | format | essential | Output includes a table or list with finding IDs, descriptions, and severity/priority labels; >= 4 entries present. |

---

## Recommended Criteria (30 pts total)

*Output is meaningfully better with these. Missing one is acceptable; missing both signals shallow execution.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Requirements matrix with status** -- Produces a matrix mapping compliance requirements to status (SATISFIED / ACTION / CONDITIONAL / N/A). Must distinguish pre-satisfied items (by design) from items requiring action. | depth | recommended | Output includes a requirements matrix or equivalent structure with >= 5 rows, each showing a requirement and its disposition. At least one row marked satisfied by design and at least one marked as requiring action. |
| C-07 | **Adoption-readiness verdict** -- Delivers a clear verdict on whether the product is adoption-ready and for whom (e.g., "adoption-ready for teams where Claude Code is already approved"). Verdict must be actionable, not hedged to the point of uselessness. | behavior | recommended | Output contains an explicit verdict statement that names a condition or audience for adoption readiness. Must not be purely "it depends" without specifying what it depends on. |
| C-08 | **Conditional frameworks handled correctly** -- Frameworks that are conditional on team behavior or data type (e.g., PCI DSS conditional on handling cardholder data; GDPR/CCPA conditional on EU/CA data subjects) are correctly flagged as conditional rather than universally applicable. | correctness | recommended | Output marks >= 1 framework as conditional and states the condition that triggers applicability. Does not assert PCI DSS applies universally. |

---

## Aspirational Criteria (10 pts total)

*Raise the bar once essential and recommended are stable. These distinguish excellent outputs from merely correct ones.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Key compliance reframe surfaced** -- Surfaces the core insight that reframes how a compliance officer should think about Signal: "Approving Signal is approving a process, not a vendor." Or equivalent formulation that distinguishes methodology approval from vendor approval. | behavior | aspirational | Output contains a reframe statement that a compliance officer could use directly in an internal approval conversation. Must be quotable, not buried in caveats. |
| C-10 | **Data-sensitivity tiering or NPI gap identified** -- Identifies that artifact content may contain non-public information and recommends a tiering model (e.g., GREEN/YELLOW/RED) or flags the policy gap. Connects the gap to a concrete remediation (policy update, tagging convention, workflow restriction). | depth | aspirational | Output identifies the NPI/data-sensitivity gap and proposes a tiering or policy action. Must name a specific control or remediation, not just flag the issue. |

---

## Scoring Example (from trace artifact)

| Criterion | Result | Points |
|-----------|--------|--------|
| C-01 Framework inference | PASS (7 frameworks, no prompting) | 12 |
| C-02 Scope: Signal vs. Claude Code | PASS (explicit) | 12 |
| C-03 SR 11-7 scope | PASS (explicit + posture benefit noted) | 12 |
| C-04 Git-native surfaced | PASS (audit trail, residency, persistence) | 12 |
| C-05 Findings register | PASS (7 entries, SF-01..SF-07) | 12 |
| C-06 Requirements matrix | PASS (8 rows, SATISFIED / ACTION split) | 10 |
| C-07 Adoption-readiness verdict | PASS ("adoption-ready for teams where Claude Code is already approved") | 10 |
| C-08 Conditional frameworks | PASS (PCI DSS, GDPR/CCPA flagged conditional) | 10 |
| C-09 Reframe surfaced | PASS ("Approving Signal is approving a process, not a vendor") | 5 |
| C-10 NPI tiering identified | PASS (GREEN/YELLOW/RED tiering recommended) | 5 |
| **Composite** | **100/100** | **100** |

All essential criteria pass. Composite = 100. **GOLDEN.**

---

## Common Failure Modes

| Failure | Which Criterion | Impact |
|---------|----------------|--------|
| Treats Signal as the vendor under assessment | C-02 | Essential fail |
| Claims SR 11-7 applies to Signal's prompt methodology | C-03 | Essential fail |
| Lists frameworks but only after asking user to specify domain | C-01 | Essential fail |
| Omits git-native compliance advantage entirely | C-04 | Essential fail |
| Produces prose findings but no structured register | C-05 | Essential fail |
| Asserts PCI DSS applies unconditionally | C-08 | Recommended fail |
| Gives hedged verdict with no actionable condition | C-07 | Recommended fail |
