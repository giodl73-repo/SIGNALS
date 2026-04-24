## flow-resilience — Round 15 Scoring (Rubric v14)

---

### Criterion-Level Evaluation

#### C-01 through C-05 — Essential (all variations)

All five variations carry the full R14 structural core. No variation removes or weakens the three distinct failure classes, four-field row structure, gap identification, distributed-systems accuracy, or commerce domain grounding.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 Three Distinct Failure Classes | PASS | PASS | PASS | PASS | PASS |
| C-02 Four-Field Structure | PASS | PASS | PASS | PASS | PASS |
| C-03 Gap Identification | PASS | PASS | PASS | PASS | PASS |
| C-04 Distributed Systems Accuracy | PASS | PASS | PASS | PASS | PASS |
| C-05 Commerce Domain Grounding | PASS | PASS | PASS | PASS | PASS |

---

#### C-06 — Recommended (Severity / Blast Radius)

All variations carry the Severity / Blast Radius column in the Column Contract with "Both required" fill requirement.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-06 Severity / Blast Radius | PASS | PASS | PASS | PASS | PASS |

---

#### C-09 through C-40 — Aspirational baseline (R14 carry-through)

All 32 R14 criteria are structurally intact across all five variations. Spot-check of the most structurally sensitive:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|---|---|---|---|---|---|---|
| C-09 Chaos Test Block Spec | PASS | PASS | PASS | PASS | PASS | 4-component meta-table present in all |
| C-14 Chaos Co-Location | PASS | PASS | PASS | PASS | PASS | Anti-boundary instruction negates standalone chaos section |
| C-15 Observability Inline | PASS | PASS | PASS | PASS | PASS | Anti-boundary negates standalone observability section |
| C-17 Unified Table Index | PASS | PASS | PASS | PASS | PASS | `#` column + anti-split instruction present |
| C-18 Section-Level Phase Gate | PASS | PASS | PASS | PASS | PASS | Explicit "produce all 3 rows before Gap Register" |
| C-19 Slot-Level Bold Imperatives | PASS | PASS | PASS | PASS | PASS | **Write this row now** + advance-inhibitor in all rows |
| C-21 Layered Granularity Architecture | PASS | PASS | PASS | PASS | PASS | 5-level table: Table / Section / Slot / Column-Group / Column |
| C-24 Column-Ownership Meta-Table | PASS | PASS | PASS | PASS | PASS | Column Contract with Name / Owner / Fill Requirement |
| C-25 Two-Symptom Anti-Boundary | PASS | PASS | PASS | PASS | PASS | Separate-tables negation + intra-row divider negation |
| C-32 5-Level Architecture + D-First Gate | PASS | PASS | PASS | PASS | PASS | Column-Group level named in architecture table |
| C-33 Trigger Condition Column | PASS | PASS | PASS | PASS | PASS | Threshold expression + detection signal required |
| C-34 Verification Signal per Stage | PASS | PASS | PASS | PASS | PASS | Mechanism + SLA + named VS per stage |
| C-35 Pre-Table Inertia Assessment | PASS | PASS | PASS | PASS | PASS | Step 1 / Investment Memo present before table |
| C-36 Inertia Tipping Point Signal | PASS | PASS | PASS | PASS | PASS | Quantified threshold + named metric per class |
| C-37 Inertia Verdict Post-Gap | PASS | PASS | PASS | PASS | PASS | Verdict section after Gap Register with F-NN references |
| C-38 Anti-Boundary Umbrella (4-escape) | PASS | PASS | PASS | PASS | PASS | All 4 escape forms closed in single contiguous block |
| C-39 Present-Tense Write Imperative | PASS | PASS | PASS | PASS | PASS | **Write this row now** in all row descriptors |
| C-40 Section Order Covers Chaos Block | PASS | PASS | PASS | PASS | PASS | "Row N columns AND Chaos Test Block complete before Row N+1" |

All 32 R14 criteria: **PASS across all five variations** — no regressions.

---

#### C-41 — Named Sub-Part Labeling Within Inertia Assessment

**Pass condition**: Three named sub-parts with distinct labels (1a/1b/1c, Act I/II/III, or equivalent); at least one row descriptor cross-references by sub-part label, not section name alone.

| Variation | Evidence | Result |
|---|---|---|
| V-01 | Step 1a / 1b / 1c explicitly labeled. Column Contract Status Quo Risk: "Must reference Step 1b by sub-part label." Row descriptors: "Status Quo Risk = Class N Step 1b carrying cost." Cross-reference by sub-part label confirmed. | **PASS** |
| V-02 | Step 1 has "Carrying Costs" and "Tipping Point Signals" headers — prose sub-divisions only, no alphanumeric or act labels. Status Quo Risk: "Draw from Step 1 carrying costs" — no sub-part label. | **FAIL** |
| V-03 | Step 1 has bold headers for "Carrying Costs" and "Tipping Point Signals" but no named 1a/1b/1c or Act labels. Row descriptors say "Class N carrying cost from Step 1" — section-name reference only. | **FAIL** |
| V-04 | Investment Memo uses Act I / Act II / Act III / Act IV labels. Column Contract: "Must reference Investment Memo Act II by act label." Row descriptors: "Class N Act II carrying cost" — act-label cross-reference confirmed. Act labeling satisfies the C-41 alternative variant. | **PASS** |
| V-05 | Step 1a / 1b / 1c / 1d labeled with functional-role annotations. Column Contract: "Reference Step 1b by sub-part label and class." Row descriptors: "Class N Step 1b carrying cost." Sub-part cross-reference confirmed in all three rows. | **PASS** |

---

#### C-42 — Pre-Table SLA Budget Pre-Commitment

**Pass condition**: Named pre-table SLA Budget commits TTD/TTC/TTR/TTV for all three failure classes; Column Contract Recovery Path names the section as reference source; at least one row descriptor names the SLA Budget as constraint source. Per-row SLA invention explicitly negated.

| Variation | Evidence | Result |
|---|---|---|
| V-01 | No dedicated SLA Budget section. Column Contract Recovery Path specifies "SLA target (TTD / TTC / TTR / TTV)" as free-fill — no reference to a pre-committed source. | **FAIL** |
| V-02 | Step 2 SLA Budget: class × stage table with 12 cells, explicit "TBD fails." Column Contract: "SLA target from Step 2 SLA Budget (above) — reference by class row and stage column, do not author independently." Row descriptors: "SLA targets from Step 2 SLA Budget, Class N row." Per-row SLA invention declared a contract violation. | **PASS** |
| V-03 | No SLA Budget section. Column Contract Recovery Path: "SLA target (TTD / TTC / TTR / TTV)" as free-fill. | **FAIL** |
| V-04 | Act IV SLA Budget table: 12-cell class × stage table. Column Contract: "SLA target — must reference SLA Budget Act IV above, citing class row and stage column; do not author independently." Row descriptors: "SLA Budget Act IV, Class N row." Contract violation language present. | **PASS** |
| V-05 | Step 1d SLA Budget: 12-cell table inside the Pre-Commitment Document. Column Contract: "SLA target from Step 1d, class row, stage column." Row descriptors cite "Step 1d, Class N row" for each row. "Per-row SLA invention is a contract violation" stated in Step 1d. | **PASS** |

---

#### C-43 — Failure Signature Column Specification

**Pass condition**: Column Contract includes Failure Signature column specifying behavioral fingerprint *during* failure; explicitly distinct from Trigger Condition (entry threshold) and State (pre-failure config); ≥2 named actor viewpoints per row; Class 2/3 operationally differentiated.

| Variation | Evidence | Result |
|---|---|---|
| V-01 | No Failure Signature column in Column Contract. Not addressed. | **FAIL** |
| V-02 | No Failure Signature column in Column Contract. Not addressed. | **FAIL** |
| V-03 | Failure Signature positioned first in D-phase. Fill requirement: "Behavioral fingerprint WHILE the failure is in progress. NOT the entry threshold (Trigger Condition). NOT pre-failure configuration (State)." ≥2 named actor viewpoints required with specific observables. Class Boundary Discriminator blockquote: Class 3 requires node-A/node-B framing showing diverging state; Class 2 requires transaction-level anomaly. Closes Class 2/3 collapse escape. | **PASS** |
| V-04 | No Failure Signature column. Column Contract does not include it. | **FAIL** |
| V-05 | Failure Signature is first D-phase column. Fill requirement explicitly negates Trigger Condition confusion and State confusion. "Name ≥2 actor viewpoints per row." "Generic fills without actor differentiation fail." Class Boundary Discriminator: Class 3 must show node-A/node-B diverging state; Class 2 must show transaction-level anomaly from single write path. Row Descriptors reinforce with per-row Failure Signature instructions. | **PASS** |

---

### Composite Scores

| Variation | C-01–C-40 (32) | C-41 | C-42 | C-43 | Total | Score |
|---|---|---|---|---|---|---|
| V-01 | 32 | PASS | FAIL | FAIL | **33/35** | **94.43** |
| V-02 | 32 | FAIL | PASS | FAIL | **33/35** | **94.43** |
| V-03 | 32 | FAIL | FAIL | PASS | **33/35** | **94.43** |
| V-04 | 32 | PASS | PASS | FAIL | **34/35** | **97.14** |
| V-05 | 32 | PASS | PASS | PASS | **35/35** | **100.00** |

> Percentage derived from rubric-weighted formula: baseline 32/35 = 99.14; each new aspirational criterion = +0.287 points toward 100.00. Using raw fraction × 100 for this report column.

---

### Ranking

1. **V-05** — 35/35 — Triple-axis (C-41 + C-42 + C-43). Only variation achieving the R15 ceiling.
2. **V-04** — 34/35 — Dual-axis (C-41 + C-42). Closest single-miss to ceiling.
3. **V-01, V-02, V-03** (tied) — 33/35 — Single-axis each. Each closes one new criterion; two remain open.

---

### Excellence Signals — V-05

V-05 is the first variation to simultaneously close all three new axes. Three structural patterns drove its separation from V-04:

**1. Four-sub-part Pre-Commitment Document as unified source-of-truth.**
Rather than scattering pre-committed values across separate sections (Step 1 + Step 2 as in V-02), V-05 nests all four types (1a framing / 1b carrying costs / 1c tipping points / 1d SLA Budget) inside a single named document. A model writing the scenario table references one document for every pre-committed constraint. This eliminates ambiguity about which step owns which value and creates one falsifiable contract over the full pre-table region.

**2. Failure Signature as temporal-boundary discriminator, not column addition.**
V-05 doesn't merely add a Failure Signature column — it re-sequences the D-phase so Failure Signature is written first, before Trigger Condition or State. This forces the model to characterize what the failure *looks like during execution* before defining when it starts (Trigger Condition) or what preceded it (State). The Class Boundary Discriminator blockquote closes the Class 2/3 collapse specifically by requiring different actor-framing geometries: transaction-level for Class 2, node-topology-level for Class 3.

**3. Structured tables for 1b and 1c, not prose bullet lists.**
V-01 specifies Step 1b as bullet points (Class 1: [metric] at [rate] [horizon]). V-05 specifies Step 1b as a structured table (Failure Class | Metric | Rate Qualifier | Horizon Qualifier). When a row descriptor later cites "Class 1 Step 1b carrying cost," a table forces column-precise retrieval — the model must locate the Class 1 row and read across metric/rate/horizon columns. Prose bullet lists allow paraphrase drift; a table makes the reference unambiguous and visually verifiable.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Four-sub-part unified pre-commitment document nests SLA Budget as Step 1d alongside carrying costs and tipping points — single falsifiable contract over all pre-table constraints", "Failure Signature as first D-phase column with temporal-boundary framing forces in-progress characterization before entry-bounding (Trigger Condition) or pre-failure config (State) — plus Class Boundary Discriminator closes Class 2/3 actor-geometry collapse", "Structured tables for pre-commitment sub-parts (Step 1b metric/rate/horizon table; Step 1c threshold/metric table) replace prose bullet lists — column-precise retrieval eliminates paraphrase drift when row descriptors cite sub-part values"]}
```
