---
name: design
description: Multi-expert review of a design artifact through 6 standard disciplines and auto-selected domain experts. Auto-select 3-
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements; the output SHALL NOT proceed past a failed block until the failure is resolved.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

Read the full design document before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, record one row.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate F-13: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. The block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row; F-21: disposition row reason cell MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue, add one domain expert row per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [signal phrase from BLOCK 0 catalogue] | [expert title or role] | [one sentence: why this signal warrants this expert] |

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following MUST hold before BLOCK 1 closes:
1. A domain expert row exists with a matching Signal detected value, OR
2. A disposition row is present: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row fires F-18 -- the block SHALL NOT close until all signals are resolved. A disposition row with an empty reason cell fires F-21 -- the row SHALL NOT be accepted until the reason cell is populated.

After population: record `BLOCK 1 domain count = [n]` (count of domain expert rows, excluding "No signals detected" and disposition rows).

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row Reviewer name MUST exactly match an Expert added value from BLOCK 1 -- any deviation fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate -- both checks before BLOCK 2 begins:
1. Domain row count MUST equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. Every Domain Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts were added: the table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

Generate a finding table for every reviewer in BLOCK 1.5 order. Domain experts run first.

For each reviewer, produce one table:

**[Reviewer Name] ([Role] / [Source])**

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | [finding description] | P1/P2/P3 | [section name or "General"] | [action or "Accept as-is"] |

Sev definitions: P1 = blocks delivery; P2 = degrades quality or maintainability; P3 = nice-to-fix.
Minimum 2 findings per reviewer at standard depth; 4 at deep depth.
If no findings: row `| 1 | No findings at this depth | P3 | General | None |`

Repeat table for every reviewer in BLOCK 1.5 order.

---

**BLOCK 3 -- CONSENSUS ANALYSIS** *(F-04: consensus count MUST be >= 1 at standard depth; F-05: split opinions MUST be listed if any exist)*

After all per-reviewer tables are complete, produce:

**Consensus findings (flagged by 2+ reviewers):**

| Finding | Reviewers | Sev (highest) | Recommended action |
|---------|-----------|---------------|--------------------|
| [finding] | [list of reviewer names] | P1/P2/P3 | [action] |

If no consensus findings: row `| None | -- | -- | -- |`

**Split opinions (reviewers disagree on severity or recommendation):**

| Finding | Reviewer A | Reviewer B | Nature of split |
|---------|-----------|-----------|-----------------|
| [finding] | [view] | [view] | [why they differ] |

If no splits: "No split opinions."

**Unique catches (flagged by exactly one reviewer, high signal):**

| Finding | Reviewer | Sev | Why notable |
|---------|---------|-----|-------------|
| [finding] | [reviewer] | P1/P2/P3 | [why only one reviewer caught this] |

If none: "No unique catches."

---

**AMEND**

List 3 specific adjustments. For each: what the user changes AND what changes in the output.

Amend 1: Change [what] -> output [changes how]
Amend 2: Change [what] -> output [changes how]
Amend 3: Change [what] -> output [changes how]

---

Write artifact to: simulations/validate/design/{{topic}}-design-{{date}}.md
Include frontmatter: skill: validate-design, topic: {{topic}}, date: {{date}}, reviewer_count: [n], p1_count: [n], p2_count: [n], p3_count: [n]