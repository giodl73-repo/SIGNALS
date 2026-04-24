Now I have everything I need. Let me score each variation.

---

## flow-resilience — Round 16 Scoring (Rubric v15, 38 criteria)

**Baseline**: All R16 variations are built on R15 V-05 (37/38). They inherit:
- C-01 through C-08 (essential + recommended): all PASS
- C-09 through C-40 (aspirational, 32 criteria): all PASS
- C-41, C-42, C-43, C-44, C-46: PASS from R15 V-05 foundation

The single open axis entering R16: **C-45** (SLA Budget Placeholder Negation + Per-Row Invention Prohibition). Both mechanisms required:
- (1) explicit "TBD fails" statement
- (2) explicit per-row SLA invention named as a contract violation

---

### V-01 — Single-Axis: TBD Negation Placement

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 through C-40 | PASS | Inherited from R15 V-05 foundation — all 32 aspirational criteria intact |
| C-41 | PASS | Step 1a/1b/1c sub-part labels present; row descriptors cite "Step 1b, Class N" by label |
| C-42 | PASS | Step 1d is named SLA Budget sub-part; Column Contract references "Step 1d, class row, stage column"; row descriptor cites Step 1d by label |
| C-43 | PASS | Column Contract Failure Signature entry specifies actor-viewpoint fill requirement distinct from Trigger Condition and State; actor-differentiation explicit |
| C-44 | PASS | "Failure Signature Class Boundary Discriminator" blockquote — Class 2 (transaction-level anomaly, single write path) and Class 3 (node-A/node-B diverging state) specified separately |
| **C-45** | **PASS** | **Mechanism 1**: "Writing 'TBD', leaving any cell blank, or using any equivalent placeholder fails the SLA Budget requirement — the pre-commitment is void if any cell is deferred. Fill every cell." — explicit TBD negation at Step 1d header. **Mechanism 2**: "Per-row SLA invention is a contract violation against this pre-committed budget." — explicit invention prohibition in last line of Step 1d. Both mechanisms present as explicit statements. |
| C-46 | PASS | Single "Pre-Commitment Document: Resilience Commitment Matrix" with Steps 1a–1d; Row descriptors cite "Step 1b, Class N" (Status Quo Risk) AND "Step 1d, Class 1 row" (Recovery Path SLA) within same row |

**Score**: 38/38 → **100.00**

*Note*: Two mechanisms distributed across separate sentences (header vs. trailing line). Passes, but minimal structural coupling between the two enforcement statements.

---

### V-02 — Output Format Axis: Enforcement Blockquote

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 through C-40 | PASS | Inherited; 32 aspirational criteria intact |
| C-41 | PASS | Step 1a/1b/1c sub-part labels; row descriptors cite "Step 1b, Class N" by sub-part label |
| C-42 | PASS | Step 1d SLA matrix; Column Contract "SLA target from Step 1d, Class N row, stage column — do not author independently" |
| C-43 | PASS | Failure Signature fill requirement with actor-viewpoint specification; Class Boundary Discriminator present |
| C-44 | PASS | Named blockquote Class Boundary Discriminator with operationally distinct Class 2 (transaction-level anomaly, client + server + transaction-boundary viewpoints) and Class 3 (node-A inventory count / node-B inventory count / observability views) requirements |
| **C-45** | **PASS** | **Mechanism 1**: "(1) **Placeholder Negation**: Writing 'TBD', leaving any cell blank, or using any equivalent unfilled value in the matrix above fails the SLA Budget requirement. The pre-commitment is void if any cell is deferred — every cell must carry an actual time value at the point this document is authored." **Mechanism 2**: "(2) **Per-Row Invention Prohibition**: Independently authoring SLA target values per scenario row is a named contract violation against this pre-committed budget." Both co-located in a single named `> **SLA Budget Enforcement**` blockquote — single structural element, unambiguous co-location. |
| C-46 | PASS | Unified document Steps 1a–1d; row descriptors cross-reference both Step 1b (Status Quo Risk) and Step 1d (Recovery Path SLA) by label in same row |

**Score**: 38/38 → **100.00**

*Note*: Co-location in a single named blockquote is structurally stronger than V-01's distribution — both mechanisms are scored as a single evaluable unit. Strong C-45 structural signal.

---

### V-03 — Phrasing Register Axis: Formal Numbered Enforcement Clauses

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 through C-40 | PASS | Inherited; 32 aspirational criteria intact |
| C-41 | PASS | Clause 1a/1b/1c/1d sub-part labels (equivalent to alphanumeric); row descriptors cite "Clause 1b, Class N" and "Clause 1c, Class N" by clause label |
| C-42 | PASS | Clause 1d is SLA Budget sub-part; Column Contract Recovery Path entry references "SLA from Clause 1d, Class N, stage (citing by label — per Enforcement Clause E2, independently authored values are a contract violation)" |
| C-43 | PASS | Column Contract Failure Signature with actor-viewpoint fill requirement; Class Boundary Discriminator blockquote present |
| C-44 | PASS | Class Boundary Discriminator blockquote with Class 2 (transaction-level anomaly from single write path) and Class 3 (node-A/node-B diverging state) separately and explicitly specified |
| **C-45** | **PASS** | **Mechanism 1 — Enforcement Clause E1**: "Leaving any cell in the SLA Budget matrix above blank, writing 'TBD', writing 'N/A', or using any equivalent unfilled value fails the SLA Budget requirement. The pre-commitment is void if any cell is deferred. All twelve cells must carry actual time values at the time this document is authored." **Mechanism 2 — Enforcement Clause E2**: "Independently authoring SLA target values per scenario row — that is, writing TTD / TTC / TTR / TTV values in the Recovery Path column that are not drawn from the matrix in Clause 1d above — is a named contract violation." Both explicitly labeled as enforcement clauses. Maximum independent evaluability — each clause is named and unambiguous. |
| C-46 | PASS | Single pre-commitment document, Clause 1a–1d; row descriptors cite "Clause 1b, Class N" AND "Clause 1d, Class N" within same row (Row 3 descriptor cites both explicitly) |

**Score**: 38/38 → **100.00**

*Note*: Named clauses E1 and E2 are the most independently evaluable C-45 implementation — a scorer reading either clause in isolation can render a verdict without needing to infer relationship between distributed statements. Formal register also extends throughout, making clause-label cross-references verifiable.

---

### V-04 — Combined Axis: Inertia Framing Prominence + Document-Level Enforcement

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 through C-40 | PASS | Inherited; 32 aspirational criteria intact |
| C-41 | PASS | Step 1a (Status Quo Competitor framing) / 1b (carrying costs) / 1c (tipping points) / 1d (SLA Budget) — four labeled sub-parts; row descriptors cite "Step 1b, Class N" by sub-part label |
| C-42 | PASS | Step 1d SLA Budget sub-part; Column Contract Recovery Path: "SLA from Step 1d, Class N, stage (Rule B — independently authored values are a contract violation)" |
| C-43 | PASS | Column Contract Failure Signature with actor-viewpoint requirement; Class Boundary Discriminator blockquote present |
| C-44 | PASS | Class Boundary Discriminator blockquote — Class 2 (transaction-level anomaly, client/server/transaction-boundary viewpoints) and Class 3 (node-A/node-B diverging state) separately specified with fill-form examples |
| **C-45** | **PASS** | **Document Enforcement Contract preamble** (read before any sub-part): **Rule A — No Deferral**: "'TBD', blank cells, 'N/A', or any equivalent placeholder in any sub-part of this document fails the pre-commitment requirement. Every cell must carry an actual value when this document is authored." **Rule B — No Per-Row Invention**: "Independently authoring values per scenario row that are not drawn from the corresponding sub-part is a named contract violation." Inline reinforcement in Step 1d: "Rule A applies: no cell may be blank or TBD." "Rule B applies: Recovery Path SLA fills must reference 'Step 1d, Class N, stage' — per-row independently authored SLA values are a contract violation against this table." Both mechanisms present in two locations with explicit cross-reference labels. |
| C-46 | PASS | Single "Pre-Commitment Document: Resilience Commitment Matrix" with Step 1a–1d; row descriptors cite "Step 1b, Class N" (Status Quo Risk, Rule B) AND "Step 1d, Class N" (Recovery Path SLA, Rule B) within same row |

**Score**: 38/38 → **100.00**

*Note*: Document-level enforcement preamble is structurally the widest scope — both mechanisms are read before the model encounters any sub-part, making them pre-read contract rather than inline reminders. Status-quo-as-named-competitor is a strong inertia framing axis not present in other variations.

---

### V-05 — Full Synthesis: All C-45 Axes Combined

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 through C-40 | PASS | Inherited; 32 aspirational criteria intact |
| C-41 | PASS | Step 1a/1b/1c/1d sub-part labels; row descriptors cite "Step 1b, Class N carrying cost" by sub-part label; Row 1 descriptor references "Step 1b, Class 1 carrying cost" explicitly |
| C-42 | PASS | Step 1d SLA Budget sub-part; Column Contract Recovery Path: "SLA target: reference Step 1d, Class N, stage column — per the SLA Budget Enforcement in Step 1d, independently authored SLA values are a contract violation"; row descriptors cite Step 1d by sub-part label in stage-level specifications |
| C-43 | PASS | Column Contract Failure Signature: "Observable behavioral fingerprint per actor during the failure. Distinct from Trigger Condition (entry threshold) and from State (pre-failure configuration). ≥2 named actor viewpoints. Class Boundary Discriminator — see below." |
| C-44 | PASS | Class Boundary Discriminator blockquote: Class 2 "transaction-level anomaly framing from a single write path… without requiring multi-node state divergence. Actor viewpoints: client view + server view + transaction boundary view. Node-A/node-B framing is incorrect for Class 2." Class 3 "node-A/node-B framing showing two nodes holding diverging last-write state simultaneously… visible across node boundaries. Single-transaction framing is incorrect for Class 3." Both class-specific fill requirements named with examples. |
| **C-45** | **PASS** | **Location 1 — Step 1d header sentence**: "Writing 'TBD', leaving any cell blank, or using any equivalent placeholder in the matrix below fails the SLA Budget requirement — the pre-commitment is void if any cell is deferred." **Location 2 — enforcement blockquote**: "(1) Placeholder Negation (restated for co-location): Every cell in the matrix above must carry an actual time value. 'TBD', blank, or any unfilled placeholder fails the SLA Budget requirement. This enforcement applies at the time of authoring this sub-part — not at the time of row construction." + "(2) Per-Row Invention Prohibition: Independently authoring SLA target values in the Recovery Path column that are not drawn from the matrix above is a named contract violation against this pre-committed SLA Budget." **Location 3 — row descriptor Recovery Path stage specifications**: "per the SLA Budget Enforcement in Step 1d, independently authored SLA values are a contract violation." Three independent locations; any one location independently satisfies the pass condition. |
| C-46 | PASS | Single "Pre-Commitment Document: Resilience Commitment Matrix" with Steps 1a–1d; row descriptors cross-reference Step 1b (Status Quo Risk — "reference by sub-part label") AND Step 1d (Recovery Path SLA — "cite Step 1d Class N by sub-part label") within same row; Row 2 descriptor cites both explicitly |

**Score**: 38/38 → **100.00**

*Note*: Three independent locations for both C-45 mechanisms. Enforcement blockquote labeled "both mechanisms required" makes it structurally impossible to score partial credit. Row descriptor back-reference creates a closed enforcement loop from pre-commitment through per-row execution.

---

## Comparative Ranking (all tied at 38/38)

| Rank | Variation | C-45 Structure | Distinguishing Property |
|---|---|---|---|
| 1 | **V-05** | Tri-location: header + blockquote + row descriptor cite | Maximum redundancy; enforcement loop from pre-commitment to per-row fill; expanded named stage specifications |
| 2 | **V-04** | Document-level preamble (pre-read) + inline Step 1d | Broadest scope — Rules A/B visible before any sub-part is encountered; status quo as named competitor |
| 3 | **V-03** | Named enforcement clauses E1 + E2 in Step 1d | Most independently evaluable — each clause stands alone; formal register maximizes unambiguity |
| 4 | **V-02** | Named blockquote co-locating both mechanisms | Single structural element covers both mechanisms — pass/fail verdict is atomic |
| 5 | **V-01** | TBD negation at header + invention prohibition as trailing line | Minimal coupling between two mechanisms; both present but distributed without structural binding |

All five reach **100.00**. Tie-breaking is purely on structural robustness, not raw score.

---

## Excellence Signals — Top Variation (V-05)

Three patterns from V-05 that V-01 through V-04 partially implement:

**1. Tri-location enforcement redundancy** — The TBD negation appears at the Step 1d header sentence, inside the enforcement blockquote (explicitly labeled "restated for co-location"), and back-referenced in row descriptors at the SLA fill point. Any single location independently satisfies the pass condition; scoring from any angle produces the same verdict. This is insurance against a scorer reading only one section and missing a distributed mechanism.

**2. Named blockquote with explicit coverage label** — "SLA Budget Enforcement — both mechanisms required" names the blockquote as a two-mechanism unit, making it structurally impossible to score mechanism 1 as passing without mechanism 2. The label "both mechanisms required" converts the blockquote from a content container into a contract assertion.

**3. Row descriptor enforcement back-reference creates a closed loop** — Row descriptors cite "per the SLA Budget Enforcement in Step 1d, independently authored SLA values are a contract violation" at the exact Recovery Path SLA annotation point. This creates a verifiable cross-reference chain: pre-commitment → Column Contract → row descriptor → recovery stage fill. A per-row invented SLA value is a violation traceable through all three reference points.

**4. Expanded per-stage Recovery Path sub-specifications** — Each stage listed as a discrete named sub-specification (Detect / Contain / Recover / Validate) with actor-chain, mechanism, SLA-reference, and named VS specified structurally rather than narratively. This is not a new C-45 mechanism but is V-05's second axis — it tightens the per-stage fill requirement below row granularity.

---

## Summary

| Variation | C-41 | C-42 | C-43 | C-44 | C-45 | C-46 | Aspirational (of 38) | Composite |
|---|---|---|---|---|---|---|---|---|
| V-01 | PASS | PASS | PASS | PASS | **PASS** | PASS | **38/38** | **100.00** |
| V-02 | PASS | PASS | PASS | PASS | **PASS** | PASS | **38/38** | **100.00** |
| V-03 | PASS | PASS | PASS | PASS | **PASS** | PASS | **38/38** | **100.00** |
| V-04 | PASS | PASS | PASS | PASS | **PASS** | PASS | **38/38** | **100.00** |
| V-05 | PASS | PASS | PASS | PASS | **PASS** | PASS | **38/38** | **100.00** |

R15 ceiling was 37/38 (99.74). R16 ceiling: **38/38 (100.00)** — achieved by all five variations. The C-45 gap was closed via five independent structural approaches; all five are valid.

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Tri-location enforcement redundancy: TBD negation at sub-part header + enforcement blockquote + row descriptor back-reference creates three independent scoring locations, any one of which independently satisfies the pass condition", "Named blockquote with explicit coverage label ('both mechanisms required') converts the enforcement block from a content container into a contract assertion — makes it structurally impossible to score one mechanism without the other", "Row descriptor enforcement back-reference creates a closed loop: pre-commitment document → Column Contract → row descriptor → recovery stage fill — a per-row invented SLA value is a violation traceable through all three reference points"]}
```
