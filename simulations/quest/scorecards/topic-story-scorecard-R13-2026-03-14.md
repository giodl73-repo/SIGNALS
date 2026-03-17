as an instructional prose requirement, not a labeled field like `**Reversal condition:**`. PARTIAL for all.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

### C-21 — Verbatim Hedge Patterns Named

V-01: No verbatim patterns. FAIL. V-02: No verbatim patterns. FAIL. V-03: "Do not open with 'The signals show...' followed by a list" — one verbatim pattern. PARTIAL. V-04: "Do not open with 'The signals show...'" — one verbatim pattern. PARTIAL. V-05: "Do not open paragraph 1 with 'The signals show...' or 'Across the namespaces...'" — two verbatim patterns. PARTIAL.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| FAIL | FAIL | PARTIAL | PARTIAL | PARTIAL |

### C-22–C-27 — Checklist Design Properties

No variation includes a pre-writing checklist. All six criteria FAIL for all variations.

### C-28 — Checklist States Design Invariant as Headed Block

FAIL for all — no checklist.

### C-29 — Required Labeled Fields in S4

V-01: Three numbered sub-items per S4a entry (question / signal type / definitive signal) but no colon-label format. PARTIAL. V-02: Three sub-items with prose description. PARTIAL. V-03: Three-part format per item (question / why signals don't resolve it / definitive signal), numbered but not labeled. PARTIAL. V-04: Compact slash-separated schema ("question / absent signal type / what a definitive signal looks like") — least explicit. PARTIAL. V-05: "Format per item: 1. Question: [text] Absent signal: [text] Definitive signal: [text]" — explicit colon-labeled fields, machine-extractable. PASS.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |

### C-30 — Recommendation Cross-References Prior Uncertainty Section

V-01: "Para 2: The strongest reason a reasonable team would resist this recommendation." — describes the opposing case but does not explicitly reference S4a by name. PARTIAL. V-02: "The strongest objection and how the current signals address or fail to address it." — same, no explicit S4a cross-reference. PARTIAL. V-03: "Para 2: The uncertainty item (S4a) that most directly threatens it." — explicit S4a cross-reference by name. PASS. V-04: "Para 2: The S4a item that most threatens it, and whether current signals address that threat." — explicit S4a reference. PASS. V-05: "Para 2: Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in Section 4b." — explicit S4b cross-reference. PASS.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PARTIAL | PARTIAL | PASS | PASS | PASS |

### C-31–C-34 — Navigability, Co-location, Inventory Annotation, Repair Template

No variation has checklist invariant blocks, anti-consolidation co-location constraints, inventory annotations, or parameterized repair templates. FAIL for all.

### C-35 — Section Directive Designates Inventory as Canonical Source

V-01: "The table is the canonical record." — designates S2 table as canonical but not in reference-chain terminology. PARTIAL. V-02: "A reviewer auditing completeness should need only the table, not the narrative." — same mechanism. PARTIAL. V-03: "The table is primary. S2 must not become a narrative account of signals." — same. PARTIAL. V-04: "Does not introduce table-eligible data that belongs in a column." — table as canonical container. PARTIAL. V-05: "The paragraph explains; the table records. Do not duplicate row data in the paragraph." — same. PARTIAL.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

### C-36–C-37 — Checklist Authority Declaration, Substitution Variable Labels

FAIL for all — no checklist, no repair template.

### C-38 — Cross-Reference Resolves to Exact Inventory Cell

Entry conditions name axis + row (two coordinates: "Signal inventory axis, S1 row") but not a column. C-38 requires row × column cell resolution. PARTIAL for all — more specific than a column reference but short of a cell reference.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

### C-39 — Propagation Rule and Authority Denial

FAIL for all — no checklist footer structure.

### C-40 — Entry Conditions Cross-Reference Inventory Axis Row

All entry conditions use the "axis, row — all fields complete" form. V-01 S2: "Signal inventory axis, S1 row — all fields complete." V-02 S2: "Signal inventory axis, S1 row — all fields complete." V-03/V-04/V-05: same pattern throughout S2, S3, S4 entry conditions. PASS for all.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-41 — Extension Procedure Names Entry-Condition Update

No variation includes an extension procedure. FAIL for all.

### C-42 — Checklist Footer Derives from Inventory

FAIL for all — no checklist.

### C-43 — Section Entry Conditions Are Dual-Anchored

Evidence per variation, all three entry conditions (S2, S3, S4):

**V-01**: S2: "Signal inventory axis, S1 row — all fields complete; **AND** Cartographer step S1 completed — all signal artifacts located and catalogued." S3: "Signal survey axis, S2 row — all key findings recorded and weights assigned; **AND** Synthesizer step S2 completed — all complete/partial artifacts read and findings tabulated." S4: "Pattern synthesis axis, S3 row — pattern statement recorded; **AND** Synthesizer step S3 completed — cross-signal pattern identified and written." All three dual-anchored. PASS.

**V-02**: S2: "Signal inventory axis, S1 row — all fields complete; AND S1 signal-location step completed — all artifact paths confirmed and recorded." S3: "Signal survey axis, S2 row — all key findings recorded and weights assigned; AND S2 signal-survey step completed — all artifacts read and tabulated." S4: "Pattern synthesis axis, S3 row — pattern statement recorded; AND S3 pattern-synthesis step completed." All dual-anchored. PASS.

**V-03**: S2: "Signal inventory axis, S1 row — all fields complete; AND S1 signal-location step completed." S3: "Signal survey axis, S2 row — all key findings recorded and weights assigned; AND S2 signal-survey step completed." S4a: "Pattern synthesis axis, S3 row — pattern statement recorded; AND S3 pattern-synthesis step completed." PASS.

**V-04**: S2: "Signal registry axis, S1 row — all fields complete; AND Cartographer step S1 completed — all namespaces checked, all artifacts located." S3: "Signal survey axis, S2 row — all key findings and evidence classes recorded; AND Synthesizer step S2 completed." S4: "Pattern synthesis axis, S3 row — pattern statement recorded, prediction made; AND Synthesizer step S3 completed." PASS.

**V-05**: S2: "Signal inventory axis, S1 row — all fields complete; AND Section 1 signal-location step completed — all namespaces checked and all located artifact paths confirmed." S3: "Signal survey axis, S2 row — all key findings and weights recorded; AND Section 2 signal-survey step completed." S4a: "Pattern synthesis axis, S3 row — pattern statement recorded; AND Section 3 pattern-synthesis step completed — cross-signal interpretation written and prediction stated." PASS.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-44 — Data-Collection Sections Lead with Table Before Narrative

V-01 S2: "Open S2 with the table below. Do not write any text before the table." PASS. V-02: "Open S2 with the survey table. No text before the table." + preamble declares "Table placement is non-negotiable — no text may precede the table in S1 or S2." PASS. V-03: "Lead with the S2 table. One row per S1 artifact." PASS. V-04: "S2 — Signal Survey (data-collection section — table leads, narrative follows). Open S2 with the survey table. No text precedes the table." PASS. V-05: "Produce the survey table immediately — no text precedes it." PASS.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

---

## Composite Scores

### Aspirational Tally

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-09 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-10 | FAIL | FAIL | FAIL | FAIL | PARTIAL |
| C-11 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-12 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-13 | FAIL | FAIL | FAIL | FAIL | PARTIAL |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-16 | PARTIAL | PARTIAL | PASS | PASS | PASS |
| C-17 | PASS | PARTIAL | PASS | PASS | PASS |
| C-18 | FAIL | PARTIAL | FAIL | PARTIAL | FAIL |
| C-19 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-20 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-21 | FAIL | FAIL | PARTIAL | PARTIAL | PARTIAL |
| C-22–C-28 | FAIL×7 | FAIL×7 | FAIL×7 | FAIL×7 | FAIL×7 |
| C-29 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-30 | PARTIAL | PARTIAL | PASS | PASS | PASS |
| C-31–C-34 | FAIL×4 | FAIL×4 | FAIL×4 | FAIL×4 | FAIL×4 |
| C-35 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-36–C-37 | FAIL×2 | FAIL×2 | FAIL×2 | FAIL×2 | FAIL×2 |
| C-38 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-39 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-40 | PASS | PASS | PASS | PASS | PASS |
| C-41 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-42 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-43 | PASS | PASS | PASS | PASS | PASS |
| C-44 | PASS | PASS | PASS | PASS | PASS |

### Aspirational Point Calculation

**V-01**:
- PASS: C-14, C-17, C-40, C-43, C-44 = 5 × 0.2703 = **1.3515**
- PARTIAL: C-08, C-09, C-11, C-12, C-16, C-20, C-29, C-30, C-35, C-38 = 10 × 0.1351 = **1.3510**
- Aspirational total: **2.70**

**V-02**:
- PASS: C-14, C-40, C-43, C-44 = 4 × 0.2703 = **1.0812**
- PARTIAL: C-08, C-09, C-11, C-12, C-16, C-17, C-18, C-20, C-29, C-30, C-35, C-38 = 12 × 0.1351 = **1.6212**
- Aspirational total: **2.70**

**V-03**:
- PASS: C-14, C-16, C-17, C-30, C-40, C-43, C-44 = 7 × 0.2703 = **1.8921**
- PARTIAL: C-08, C-09, C-11, C-12, C-20, C-21, C-29, C-35, C-38 = 9 × 0.1351 = **1.2159**
- Aspirational total: **3.11**

**V-04**:
- PASS: C-14, C-16, C-17, C-30, C-40, C-43, C-44 = 7 × 0.2703 = **1.8921**
- PARTIAL: C-08, C-09, C-11, C-12, C-18, C-20, C-21, C-29, C-35, C-38 = 10 × 0.1351 = **1.3510**
- Aspirational total: **3.24**

**V-05**:
- PASS: C-14, C-16, C-17, C-29, C-30, C-40, C-43, C-44 = 8 × 0.2703 = **2.1624**
- PARTIAL: C-08, C-09, C-10, C-11, C-12, C-13, C-20, C-21, C-35, C-38 = 10 × 0.1351 = **1.3510**
- Aspirational total: **3.51**

### Final Score Table

| Component | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| Essential (C-01–C-04) | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 |
| Recommended (C-05–C-07) | 30.0 | 30.0 | 30.0 | 30.0 | 30.0 |
| Aspirational (C-08–C-44) | 2.70 | 2.70 | 3.11 | 3.24 | 3.51 |
| **Total** | **92.70** | **92.70** | **93.11** | **93.24** | **93.51** |

---

## Ranking

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 | V-05 | 93.51 | Formal Register + Inertia Framing |
| 2 | V-04 | 93.24 | Role Sequence × Output Format |
| 3 | V-03 | 93.11 | Lifecycle Emphasis |
| 4 (tie) | V-01 | 92.70 | Role Sequence |
| 4 (tie) | V-02 | 92.70 | Output Format |

All variations clear the Golden threshold (90+). All essential criteria pass. The differential is entirely in aspirational criteria: V-05 gains over V-04 on C-29 (labeled fields in S4a) and C-30 (S4c explicitly cross-references S4b); V-03 and V-04 separate from V-01/V-02 on C-16 (prohibited-structures blocks) and C-30 (explicit S4a cross-reference in recommendation).

---

## Excellence Signals

Two structural patterns in V-05 produce higher aspirational coverage and are not captured by any existing criterion.

**Signal 1 — V-05: Inertia as named competitor section with two-paragraph evidence assessment**

V-05 introduces S4b (Inertia Analysis) as a required pre-recommendation section with a specific two-paragraph contract: (1) identify which current signals, read as evidence for the status quo, are strongest — what a team choosing inertia would cite from the existing signal set; (2) assess what signals indicate that deferral has a time-varying cost (market windows, competitive moves, team capacity decay). The recommendation that follows must then directly prefer one of {proceed, pause, pivot, abandon} over inertia by engaging the strongest inertia-supporting signal explicitly. C-10 fires on whether inertia is a per-signal selection filter in S2; C-13 fires on whether inertia habits appear in multiple non-synthesis sections; C-17 fires on anti-neutral instruction in collapse-risk sections. None fire on whether inertia is itself the subject of a formal two-paragraph evidence assessment as a named competitor option, with a mandatory head-to-head comparison requirement in the recommendation. The governance consequence: a recommendation that cannot demonstrate preference over inertia on the evidence is identified as structurally incomplete — the inertia section creates a named competitor whose evidence must be addressed, not merely a stylistic tendency to avoid.

**Signal 2 — V-05: Reversal condition extended to include inertia comparison at trigger point**

V-01–V-04's Para 3 in S4b names the reversal condition: the specific signal, threshold, or event that would change the recommendation, and to which of the four options. V-05's S4c Para 3 adds a third element: "whether that option is preferable to inertia at that trigger point." This makes the reversal condition forward-looking about the status-quo comparison: it does not merely name the trigger for change but pre-evaluates whether the changed recommendation still beats inertia in the triggered future state. A reversal condition that names "pivot if competitor ships equivalent feature" but doesn't assess whether "pivot" beats inertia at that trigger is incomplete — it changes the recommendation but doesn't close the analysis loop. C-20 fires on whether there's a labeled disproof field; C-30 fires on whether the recommendation cross-references the prior uncertainty section; no criterion fires on whether the reversal condition itself re-evaluates the inertia comparison in the triggered scenario.

---

```json
{"top_score": 93.51, "all_essential_pass": true, "new_patterns": ["Inertia as named competitor section with two-paragraph evidence assessment (which current signals support status quo / what signals indicate time-varying cost of deferral) required before recommendation — distinct from inertia as a signal-selection filter (C-10) or recurring inertia habit (C-13); recommendation must demonstrate explicit preference over inertia on the evidence", "Reversal condition extended to include inertia comparison at trigger point — Para 3 requires naming not only the specific signal/threshold/event that would change the recommendation and which option it would change to, but also whether that option is preferable to inertia in the triggered scenario, making the reversal condition forward-facing about the status-quo option"]}
```
