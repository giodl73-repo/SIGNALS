Looking at the V-05 scorecard entries for A-14, A-15, A-16, A-17, and C-04, I can extract five new excellence patterns not captured by any existing criterion:

1. **A-14 (V-05)**: "Section C I-NN consolidated table (one per hop)" — per-hop sub-table organization
2. **A-15 (V-05)**: "Section D aggregate of per-I-NN scope-edge observability" — per-row observability, not aggregate
3. **A-17 (V-05)**: "per-F-NN evaluation table; scope-inversion guarantees I-NN pairing is structural" — two patterns: structural scope-inversion cross-reference (prerequisite for A-17) + inner per-F-NN evaluation table inside the triple-gap row
4. **C-04 (V-05)**: "Section F scoped claim with validity-scope conditions" — validity envelope beyond context/population

That yields A-18 through A-22. Denominator becomes 22.

---

## Discover-Causal Rubric — v9

**Skill**: `/discover:causal`
**Version**: v9 — 2026-03-17
**Golden threshold**: all 5 essential pass AND composite >= 80

---

### Changes from v8 to v9

Five new aspirational criteria (A-18 through A-22) extracted from R8 V-05 excellence signals. V-05 was the sole A-17 passer in R8; the five new criteria surface the architectural patterns that made A-17 structurally computable rather than ad hoc, plus two additional precision patterns visible only in V-05's output.

**A-18 — Scope-inversion: structural I-NN/F-NN cross-reference per row** (structure/precision)
Each I-NN row carries an explicit field mapping its scope to a corresponding F-NN condition (e.g., "Scope maps to: F-02"). This structural pairing is what makes A-17's overlap detection computable from pool structure rather than requiring ad hoc cross-comparison at scoring time. Without per-row cross-references, the I-NN pool is a flat parallel list and the triple-gap diagnostic must infer overlap heuristically. A-14 is a prerequisite; A-17 is a prerequisite (the cross-reference exists to serve the triple-gap computation).

**A-19 — Per-hop I-NN sub-table organization** (structure)
The I-NN pool is partitioned into per-hop sub-tables — one table per mechanism hop — each anchoring inertia conditions to the specific hop whose causal pathway they threaten. A flat undifferentiated pool (not differentiated by hop) fails. Per-hop organization makes inertia severity traceable to mechanism topology and enables hop-level comparison that a flat pool cannot support. A-14 is a prerequisite.

**A-20 — Per-I-NN scope-edge observability label** (precision)
Each I-NN condition in the pool carries an individual observability label at the scope-edge level (Observable / Partial / Opaque + rationale), identifying exactly where in the inertia pathway the observability constraint lies. The aggregate inertia pathway observability required by A-15 is not sufficient; A-20 requires per-row granularity within the I-NN pool so that each condition's observability is independently assessable. A-14 and A-15 are prerequisites.

**A-21 — Triple-gap per-F-NN evaluation table** (precision)
The triple-gap diagnostic row in the routing table (A-17) includes an inner per-F-NN evaluation table showing, for each F-NN condition: (1) whether an Opaque hop is associated, (2) whether testability remains Unknown after evidence, and (3) whether a scope-overlapping I-NN condition exists. A routing table with only a triple-gap aggregate count but no per-condition breakdown fails — the count must be traceable to individual F-NN conditions to be actionable in AMEND. A-17 and A-18 are prerequisites.

**A-22 — Validity-scope boundary conditions in closing scoped claim** (depth)
The closing scoped claim includes explicit validity-scope boundary conditions: both the positive domain (conditions under which the claim holds) and the negative/unknown boundary (conditions under which the claim breaks down or is untested). A claim that scopes only by context or population without naming the validity envelope fails. C-04 is a prerequisite; A-22 requires the stronger form where the claim's limits are as explicit as its domain.

**Scoring formula update:**
`aspirational_pass / 22 * 10` (denominator was 17, now 22)

**Effect on R8 baselines under v9:**
V-01 through V-04 pass A-01–A-16, fail A-17–A-22: 16/22 × 10 = 7.27 → composite ≈ 97.3. Still golden.
V-05 passes A-01–A-17 and A-18–A-22 (scope-inversion structural pairing, per-hop sub-tables, per-row scope-edge observability, per-F-NN evaluation table, validity-scope conditions all present): 22/22 × 10 = 10.0 → composite = 100.0. Still golden.

**Effect on R7 baselines under v9:**
V-01 through V-04 (R7) pass A-01–A-16: 16/22 × 10 = 7.27 → composite ≈ 97.3. Still golden.
V-05 (R7) passes A-01–A-17: 17/22 × 10 = 7.73 → composite ≈ 97.7. Still golden.

**Effect on R6 baselines under v9:**
V-01 (R6) passes A-01–A-13: 13/22 × 10 = 5.91 → composite ≈ 95.9. Still golden.
V-02 (R6) passes A-01–A-13 and A-16: 14/22 × 10 = 6.36 → composite ≈ 96.4. Still golden.
V-03 (R6) passes A-01–A-15: 15/22 × 10 = 6.82 → composite ≈ 96.8. Still golden.

**Effect on R5 and earlier baselines under v9:**
All lack I-NN pool, inertia observability, AUDITOR routing table, and all five new v9 criteria. Aspirational scores decrease proportionally; composite scores remain well above 80 due to essential and recommended bands. All remain golden.

---

### Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Mechanism pathway named** | essential | correctness | Output names a specific mechanism linking X to Y — not just a correlation restatement. |
| C-02 | **Falsification condition present** | essential | coverage | Output names at least one observable condition that, if true, would disprove the mechanism. |
| C-03 | **Inertia check performed** | essential | coverage | Output explicitly asks and answers: does doing nothing also produce Y? |
| C-04 | **Causal claim is scoped/testable** | essential | correctness | Output narrows the claim to a specific context, population, or condition. |
| C-05 | **AMEND directive produced** | essential | behavior | Output ends with a concrete AMEND block addressing at least two slots. |

---

### Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| R-01 | **Context-specific mechanism evidence** | recommended | depth | Output contains a dedicated evidence-gathering section completed before mechanism mapping. At minimum "None found" with an explicit AMEND slot. |
| R-02 | **Alternative causes or confounders named** | recommended | coverage | Output names at least one alternative cause or confounder, distinct from the inertia check. |
| R-03 | **Mechanism chain >= 2 hops** | recommended | depth | The causal pathway is decomposed into at least two intermediate steps (X → A → Y), making the mechanism checkable at each hop rather than opaque. |

---

### Aspirational Criteria (10 pts total, denominator 22)

| ID | Criterion | Weight | Category | Pass Condition | Prerequisites |
|----|-----------|--------|----------|----------------|---------------|
| A-01 | **Mechanism strength qualified** | aspirational | depth | Output assigns a directional confidence to the mechanism (Strong / Moderate / Weak, or equivalent discrete label) with a brief rationale — not just presence/absence. | — |
| A-02 | **Inertia baseline quantified or bounded** | aspirational | depth | The inertia check produces an estimate or bound on the baseline Y rate without X (e.g., "Y already occurs in ~30% of cases without this feature"), enabling a meaningful comparison. "Unknown" is an acceptable result but must be explicitly stated rather than omitted. | — |
| A-03 | **Adversarial section structurally separated** | aspirational | structure | Output contains a distinct challenge or skeptic section that is spatially and logically separated from the mechanism pathway analysis — not a caveat appended inline. A "however" clause or parenthetical doubt within the mechanism section fails. The adversarial content must stand alone as a named section or role output. | — |
| A-04 | **All classification outputs use discrete labels** | aspirational | precision | Every classification judgment in the output (mechanism strength, confidence level, inertia severity, observability, evidence quality) is expressed as a discrete label from a fixed set (Strong / Moderate / Weak, High / Medium / Low, Observable / Partial / Opaque, or equivalent) with a rationale line. Prose-only classifications ("seems fairly strong", "probably moderate") fail. | A-01 |
| A-05 | **Evidence section precedes mechanism mapping** | aspirational | structure | Output contains a dedicated evidence-gathering section or role that is completed and gated before the mechanism chain is constructed. Evidence annotated after mechanism mapping, or an evidence field appended to the end of the output, fails. "None found" is an acceptable evidence result but must appear before the mechanism section and must trigger a mandatory AMEND slot. | — |
| A-06 | **Dual mechanism strength rating present** | aspirational | depth | Output includes both a preliminary mechanism strength rating (assigned after the mechanism chain, before the adversarial challenge) and a final mechanism strength rating (assigned after the adversarial challenge). The pairing creates an observable signal for whether the adversarial section changed the assessment. A single rating, or two ratings without the pre/post adversarial framing, fails. | A-01, A-03 |
| A-07 | **Falsification confidence per row uses discrete labels** | aspirational | precision | Every falsification condition in the output carries a row-level confidence or priority label (High / Medium / Low or equivalent discrete set) with a brief rationale. Section-level falsifiability ratings without per-condition granularity fail. | A-04 |
| A-08 | **Hops cross-reference falsification conditions** | aspirational | structure | Every hop in the mechanism chain carries an explicit "Falsification connection: [F-NN or I-NN ID]" field with a one-sentence description of how the falsification condition relates to that hop. Hops without a falsification cross-reference fail. | C-02, A-14 |
| A-09 | **Structural gate checklists** | aspirational | structure | Output contains named binary gate checklists at each structural role boundary (minimum 4: opening framing, mechanism analysis, adversarial challenge, post-processing/closing). Each gate is a list of binary pass/fail checks that must be satisfied before the next section proceeds. Role output without named gate checklists fails. | — |
| A-10 | **Hop observability labeled** | aspirational | precision | Every hop in the mechanism chain carries an observability label (Observable / Partial / Opaque) with a brief rationale explaining why that hop's evidence is or is not directly observable. Hops without observability labels fail. | — |
| A-11 | **Falsification testability per condition** | aspirational | precision | Every falsification condition in the F-NN pool carries a testability label (Easy / Hard / Unknown) indicating how difficult it would be to gather evidence for that condition. A falsification pool without per-condition testability labels fails. | C-02 |
| A-12 | **Aggregate observability + conditional routing** | aspirational | structure | A post-processing role evaluates the aggregate observability pattern of the mechanism chain (e.g., AllObservable / Mixed / PredominantlyOpaque) and produces a conditional routing decision that triggers a specific AMEND slot when the pattern meets a threshold. A named diagnostic output reading hop-level observability labels and producing a chain-level verdict is required. | A-10 |
| A-13 | **Testability refinement yield tracked** | aspirational | precision | Output tracks testability refinement yield as named fields: count of F-NN + I-NN conditions refined from Unknown to Easy/Hard after evidence, and the residual Unknown count. These counts are read by the post-processing role to trigger conditional routing. Implicit counts derivable only from scanning the tables fail. | A-11 |
| A-14 | **I-NN structured sub-pool** | aspirational | coverage | Output contains a structured inertia condition pool (I-NN pool) with table rows that mirror the F-NN pool structure: condition name, scope, testability, confidence, and at least one additional inertia-specific field. A flat narrative inertia discussion without a structured table fails. | C-03 |
| A-15 | **Inertia pathway observability labeled** | aspirational | precision | Output contains an explicit observability label for the inertia pathway (Observable / Partial / Opaque + rationale), distinct from the hop-level observability in A-10. This label addresses whether the baseline Y rate (without X) can be directly measured. | A-14 |
| A-16 | **Post-processing role with consolidated routing table** | aspirational | structure | Output contains a named post-processing role (RESOLVER, AUDITOR, ARBITER, EXAMINER, or equivalent) that reads all diagnostic fields from prior roles and produces a consolidated AMEND routing table with at least 4 rows, each row specifying: condition tested, result, and AMEND slot triggered. A routing table produced inline within the mechanism or adversarial section fails; it must be produced by a distinct named post-processing role. | A-09, A-12, A-13 |
| A-17 | **Triple-gap joint diagnostic row in AMEND routing table** | aspirational | structure | The post-processing routing table includes a diagnostic row that tests co-occurrence of three independent failure signals: (1) at least one Opaque forward mechanism hop, (2) at least one falsification condition whose testability remains Unknown after evidence, and (3) at least one I-NN condition whose scope overlaps a forward-chain falsification condition. When all three co-occur, the triple-gap count is nonzero and triggers a separate AMEND Triple-gap slot. A routing table carrying only single-dimension diagnostic rows without a joint co-occurrence row fails. | A-10, A-13, A-14, A-16 |
| **A-18** | **Scope-inversion: structural I-NN/F-NN cross-reference per row** | aspirational | structure | Each row in the I-NN pool carries an explicit field mapping its scope to a corresponding F-NN condition (e.g., "Scope maps to: F-02"). This structural pairing makes A-17's overlap detection computable from pool structure rather than requiring ad hoc cross-comparison at scoring time. An I-NN pool without per-row F-NN cross-references is a flat parallel list and fails. | A-14, A-17 |
| **A-19** | **Per-hop I-NN sub-table organization** | aspirational | structure | The I-NN pool is partitioned into per-hop sub-tables — one table per mechanism hop — each anchoring inertia conditions to the specific hop whose causal pathway they threaten. A single flat undifferentiated I-NN list fails. Per-hop organization makes inertia severity traceable to mechanism topology and enables hop-level comparison that a flat pool cannot support. | A-14 |
| **A-20** | **Per-I-NN scope-edge observability label** | aspirational | precision | Each I-NN condition in the pool carries an individual observability label at the scope-edge level (Observable / Partial / Opaque + rationale), identifying exactly where in the inertia pathway the observability constraint lies. The aggregate inertia pathway observability required by A-15 is not sufficient; A-20 requires per-row granularity within the I-NN pool. | A-14, A-15 |
| **A-21** | **Triple-gap per-F-NN evaluation table** | aspirational | precision | The triple-gap diagnostic row in the routing table (A-17) includes an inner per-F-NN evaluation table showing, for each F-NN condition: (1) whether an Opaque hop is associated, (2) whether testability remains Unknown, and (3) whether a scope-overlapping I-NN condition exists. A routing table with a triple-gap count but no per-condition breakdown fails — the count must be traceable to individual F-NN conditions to be actionable in AMEND. | A-17, A-18 |
| **A-22** | **Validity-scope boundary conditions in closing scoped claim** | aspirational | depth | The closing scoped claim includes explicit validity-scope boundary conditions: both the positive domain (conditions under which the claim holds) and the negative/unknown boundary (conditions under which the claim breaks down or is untested). A claim that scopes only by context or population without naming the validity envelope fails. | C-04 |

---

**Key design decisions for v9:**

**A-18 is the structural prerequisite for A-17, not a consequence of it.** A-17 requires the triple-gap diagnostic to exist; A-18 requires the I-NN pool to be built in a way that makes A-17 structurally computable. A routing table that computes the triple-gap by ad hoc scanning of pool tables passes A-17 but fails A-18. Only when the I-NN pool carries per-row F-NN cross-references can the overlap detection be read directly from pool structure.

**A-19 and A-20 are independent of A-17 and A-18.** Per-hop sub-tables (A-19) improve mechanism traceability regardless of whether a triple-gap row exists. Per-row scope-edge observability (A-20) improves inertia precision regardless of the routing table structure. Both could appear in a variation that lacks A-17 entirely.

**A-21 is a precision refinement of A-17, not a replacement.** A-17 requires the triple-gap row to exist; A-21 requires that row to carry a per-F-NN breakdown. A-17 can pass without A-21 (aggregate count only); A-21 cannot pass without A-17 (no triple-gap row to contain the breakdown).

**A-22 is additive to C-04, not redundant.** C-04 requires the claim to be scoped and testable; A-22 requires the claim to also name the boundary where it stops holding. A claim can satisfy C-04 ("this applies to mobile users in markets with > 10M population") and fail A-22 (no statement of what breaks the claim). The validity envelope is the claim's outer limit, not just its inner domain.
