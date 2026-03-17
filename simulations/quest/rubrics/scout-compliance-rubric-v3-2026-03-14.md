Here is the complete updated rubric as written:

---

## What changed: v2 → v3

**1 new criterion: C-14 (3 pts)**

| ID | Pattern | What it tests |
|----|---------|--------------|
| C-14 | Verdict is the first named section heading | Closes C-11's displacement gap — verdict at position 2 passes C-11's letter but violates its spirit; C-14 requires VERDICT as the first `##`-level heading unconditionally |

**The gap it closes:**

- C-11 pass condition: "appears before any framework analysis table or findings section" — V-05 R2 placed a DEFAULT RISK section at position 1, VERDICT at position 2, and passed C-11. That is a displacement fail, not an omission fail.
- C-14 pass condition: "the first `##`-level heading in the output is the verdict section." Any section before it — framework catalog or not — is a fail.
- The two criteria are complementary: C-11 catches omission (verdict never appears); C-14 catches displacement (verdict appears, but not first).

**Why only one new criterion:**

The other two R2 patterns don't produce new output criteria:
- *Explicit C-13 planting* — a prompt design mechanism, not an output behavior. The output criterion (C-13) was already correct.
- *Section-contract portability* — a confirmation that C-11/C-12 are well-designed, not a gap.

**Scoring:**
- Max possible: **112 pts** (was 109)
- GOLDEN threshold: unchanged at **100**
- V-05 R2 retroactively scores 109/112 (C-14 FAIL confirmed)
- V-01..V-04 C-14 status: pending R3 measurement
 | C-01..C-05 | 60 pts | Hard correctness floor — any fail is a broken output |
| Recommended | C-06..C-08 | 30 pts | Depth and decision-quality — missing one is acceptable |
| Aspirational (core) | C-09..C-10 | 10 pts | Distinguishes excellent from merely correct |
| Aspirational (R1) | C-11..C-13 | 9 pts | Structural and proactive excellence signals from Round 1 |
| Aspirational (R2) | C-14 | 3 pts | Displacement-close from Round 2 gap analysis |
| **Max possible** | | **112 pts** | |
| **GOLDEN threshold** | | **100 pts** | All C-01..C-10 must pass; aspirational (R1/R2) may be absent |

---

## Essential Criteria (60 pts total)

*Any fail here is a broken output. Essential fails are disqualifying regardless of other scores.*

| ID | Criterion | Category | Tier | Points | Pass Condition |
|----|-----------|----------|------|--------|----------------|
| C-01 | **Framework inference without prompting** — Infers applicable regulatory frameworks (e.g., SOX, SOC 2, FINRA, SR 11-7, GDPR, PCI DSS, HIPAA) from repo context alone. Must not prompt the user to specify their domain or compliance requirements. Minimum 4 frameworks identified. | inference | essential | 12 | Output names >= 4 compliance frameworks without prompting the user. Frameworks must be plausibly inferred from repo signals (not random enumeration). |
| C-02 | **Scope boundary: Signal vs. Claude Code** — Identifies that the primary compliance surface is Claude Code (the tool sending repo content to the Anthropic API), not Signal (the methodology). Must not attribute Signal as a vendor risk. | correctness | essential | 12 | Output explicitly states that vendor assessment scope is Claude Code / Anthropic, not Signal, and does not treat Signal itself as an assessable vendor or data processor. |
| C-03 | **SR 11-7 scope: model vs. methodology** — Correctly identifies that SR 11-7 (model risk management) applies to Claude (the AI model), not to Signal (a structured prompt methodology). Misclassifying Signal as an AI model under SR 11-7 is a disqualifying error. | correctness | essential | 12 | Output explicitly states SR 11-7 applies to Claude / the model, not to Signal. Bonus if it notes that Signal's documented methodology improves SR 11-7 posture. |
| C-04 | **Git-native design surfaced as compliance-favorable** — Surfaces the absence of a server, SaaS layer, or external data persistence as a compliance advantage. Must connect git-native design to at least one specific compliance property (audit trail, data residency, or artifact persistence). | coverage | essential | 12 | Output identifies >= 1 specific compliance benefit of the git-native, no-server design and links it to a named framework or requirement category. |
| C-05 | **Findings register with severity** — Produces a structured findings register with IDs (e.g., SF-01...), finding descriptions, and severity or priority labels. Register must contain >= 4 entries. | format | essential | 12 | Output includes a table or list with finding IDs, descriptions, and severity / priority labels; >= 4 entries present. |

---

## Recommended Criteria (30 pts total)

*Output is meaningfully better with these. Missing one is acceptable; missing both signals shallow execution.*

| ID | Criterion | Category | Tier | Points | Pass Condition |
|----|-----------|----------|------|--------|----------------|
| C-06 | **Requirements matrix with status** — Produces a matrix mapping compliance requirements to status (SATISFIED / ACTION / CONDITIONAL / N/A). Must distinguish pre-satisfied items (by design) from items requiring action. | depth | recommended | 10 | Output includes a requirements matrix or equivalent structure with >= 5 rows, each showing a requirement and its disposition. At least one row marked satisfied by design and at least one marked as requiring action. |
| C-07 | **Adoption-readiness verdict** — Delivers a clear verdict on whether the product is adoption-ready and for whom (e.g., "adoption-ready for teams where Claude Code is already approved"). Verdict must be actionable, not hedged to the point of uselessness. | behavior | recommended | 10 | Output contains an explicit verdict statement that names a condition or audience for adoption readiness. Must not be purely "it depends" without specifying what it depends on. |
| C-08 | **Conditional frameworks handled correctly** — Frameworks that are conditional on team behavior or data type (e.g., PCI DSS conditional on handling cardholder data; GDPR / CCPA conditional on EU / CA data subjects) are correctly flagged as conditional rather than universally applicable. | correctness | recommended | 10 | Output marks >= 1 framework as conditional and states the condition that triggers applicability. Does not assert PCI DSS applies universally. |

---

## Aspirational Criteria — Core (10 pts total)

*Raise the bar once essential and recommended are stable. These distinguish excellent outputs from merely correct ones.*

| ID | Criterion | Category | Tier | Points | Pass Condition |
|----|-----------|----------|------|--------|----------------|
| C-09 | **Key compliance reframe surfaced** — Surfaces the core insight that reframes how a compliance officer should think about Signal: "Approving Signal is approving a process, not a vendor." Or equivalent formulation that distinguishes methodology approval from vendor approval. | behavior | aspirational | 5 | Output contains a reframe statement that a compliance officer could use directly in an internal approval conversation. Must be quotable, not buried in caveats. |
| C-10 | **Data-sensitivity tiering or NPI gap identified** — Identifies that artifact content may contain non-public information and recommends a tiering model (e.g., GREEN / YELLOW / RED) or flags the policy gap. Connects the gap to a concrete remediation (policy update, tagging convention, workflow restriction). | depth | aspirational | 5 | Output identifies the NPI / data-sensitivity gap and proposes a tiering or policy action. Must name a specific control or remediation, not just flag the issue. |

---

## Aspirational Criteria — R1 Patterns (9 pts total)

*Derived from Round 1 scorecard analysis. These structural and proactive behaviors separate outputs that reliably hit 100+ from outputs that hit the floor inconsistently.*

| ID | Criterion | Category | Tier | Points | Pass Condition |
|----|-----------|----------|------|--------|----------------|
| C-11 | **Verdict-first output structure** — The adoption-readiness verdict and compliance reframe appear in the first substantive section, before any framework catalog, requirements matrix, or findings register. This ordering is a structural guarantee: C-07 and C-09 content cannot be crowded out by analysis volume. | format | aspirational-R1 | 3 | Adoption verdict (C-07 content) appears before any framework analysis table or findings section. Reframe statement (C-09 content) appears in the opening section or immediately following the verdict. **Note**: C-11 catches verdict *omission*; it does not catch verdict *displacement* (verdict at position 2, behind any non-framework section). See C-14. |
| C-12 | **Named sections for aspirational outputs** — The data-sensitivity tiering (C-10) and compliance reframe (C-09) appear as explicitly headed sections (e.g., `## REFRAME`, `## DATA-SENSITIVITY TIER`) rather than as incidental observations embedded in prose or trailing paragraphs. Named sections convert emergent insights into structural deliverables. | format | aspirational-R1 | 3 | C-09 content (reframe) and C-10 content (NPI tiering) each appear under a dedicated named section heading. Neither is an inline paragraph within another section. |
| C-13 | **SR 11-7 misapplication proactively flagged** — Beyond correctly scoping SR 11-7 to Claude the model (C-03), the output proactively characterizes SR 11-7 as a commonly misapplied framework in AI-adjacent tooling contexts and explains the distinction. Anticipates the compliance officer's likely objection before it is raised. | behavior | aspirational-R1 | 3 | Output names SR 11-7 AND describes it as frequently misapplied to prompt methodologies or AI-adjacent tools, with an explanation of why the misapplication occurs and why Signal falls outside its scope. Goes beyond simply stating the correct scope. |

---

## Aspirational Criteria — R2 Patterns (3 pts total)

*Derived from Round 2 scorecard gap analysis. C-14 closes the displacement hole exposed by V-05 R2.*

| ID | Criterion | Category | Tier | Points | Pass Condition |
|----|-----------|----------|------|--------|----------------|
| C-14 | **Verdict is the first named section heading** — The adoption-readiness verdict (`## VERDICT` or equivalent) is the first `##`-level section heading in the output. No other named section — including risk preambles, scope statements, or framework warnings — may precede it. This closes the gap C-11 leaves open: C-11 allows verdict at position 2 if position 1 is not a framework catalog; C-14 does not. The verdict section must come first structurally, not merely earlier than the catalog. | format | aspirational-R2 | 3 | The first `##`-level heading in the output is the verdict or adoption-readiness section. Any other named section appearing before the verdict heading — regardless of whether it is a framework table — is a displacement fail. |

---

## Scoring Reference

### v1 Trace Artifact (100/100 GOLDEN)

| Criterion | Result | Points |
|-----------|--------|--------|
| C-01 Framework inference | PASS (7 frameworks, no prompting) | 12 |
| C-02 Scope: Signal vs. Claude Code | PASS (explicit) | 12 |
| C-03 SR 11-7 scope | PASS (explicit + posture benefit noted) | 12 |
| C-04 Git-native surfaced | PASS (audit trail, residency, persistence) | 12 |
| C-05 Findings register | PASS (7 entries, SF-01..SF-07) | 12 |
| C-06 Requirements matrix | PASS (8 rows, SATISFIED / ACTION split) | 10 |
| C-07 Adoption-readiness verdict | PASS ("adoption-ready for teams where Claude Code is already approved") | 10 |
| C-08 Conditional frameworks | PASS (PCI DSS, GDPR / CCPA flagged conditional) | 10 |
| C-09 Reframe surfaced | PASS ("Approving Signal is approving a process, not a vendor") | 5 |
| C-10 NPI tiering identified | PASS (GREEN / YELLOW / RED tiering recommended) | 5 |
| C-11 Verdict-first structure | not evaluated in v1 | — |
| C-12 Named sections for aspirationals | not evaluated in v1 | — |
| C-13 SR 11-7 misapplication flagged | not evaluated in v1 | — |
| C-14 Verdict is first named heading | not evaluated in v1 | — |
| **Composite** | **100/100 (GOLDEN)** | **100** |

---

### R1 Variation Scores (v2 rubric; C-14 added for reference)

| Variation | C-01..C-10 | C-11 | C-12 | C-13 | C-14 | v3 Total |
|-----------|-----------|------|------|------|------|----------|
| V-01: Baseline | 87 | FAIL | FAIL | FAIL | FAIL | 87 |
| V-02: Architect-first | 93 | FAIL | FAIL | PASS | FAIL | 96 |
| V-03: Verdict-first | 100 | PASS | PASS | PASS | PASS (inferred) | 109 |
| V-04: Formal register | 100 | FAIL | PASS | PASS | unknown | 106+ |
| V-05: Default-risk | 95 | FAIL | FAIL | FAIL | FAIL | 95 |

*C-14 scores above are inferred from R1 variation descriptions; not directly measured in R1.*

---

### R2 Variation Scores (v3 rubric — C-14 pending R3 measurement)

| Variation | C-01..C-10 | C-11 | C-12 | C-13 | C-14 | v3 Total |
|-----------|-----------|------|------|------|------|----------|
| V-01: Section-contract | 100 | PASS | PASS | PASS | pending | 109+ |
| V-02: Synthesis-gate | 100 | PASS | PASS | PASS | pending | 109+ |
| V-03: Terse imperative | 100 | PASS | PASS | PASS* | pending | 109+ |
| V-04: Architect + template | 100 | PASS | PASS | PASS | pending | 109+ |
| V-05: Risk + synthesis | 100 | PASS | PASS | PASS | **FAIL** | 109 |

*C-13 most fragile encoding in V-03 — terse but sufficient.*
*V-05 C-14 is a confirmed FAIL: VERDICT appears at position 2 (behind DEFAULT RISK section) per R2 scorecard.*
*C-14 for V-01..V-04 requires R3 direct measurement.*

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
| Verdict and reframe buried after 10-row framework catalog | C-11 | Aspirational-R1 miss |
| Reframe and tiering appear as trailing prose, no section headers | C-12 | Aspirational-R1 miss |
| States SR 11-7 does not apply but does not explain it is commonly misapplied | C-13 | Aspirational-R1 miss |
| Any named section precedes the verdict heading — verdict at position 2 or later | C-14 | Aspirational-R2 miss |
