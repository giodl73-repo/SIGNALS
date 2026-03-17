Written. Here is the complete updated rubric:

---

## Discover-Causal Rubric -- v8

**Skill**: `/discover:causal`
**Version**: v8 -- 2026-03-17
**Golden threshold**: all 5 essential pass AND composite >= 80

---

### Changes from v7 to v8

One new aspirational criterion extracted from R7 excellence signals. All five R7 variations scored 100.0 (16/16 aspirational under v7). The new criterion surfaces a joint co-occurrence diagnostic visible only in V-05 that no individual v7 routing-table row can surface alone.

**A-17 -- Triple-gap joint diagnostic row in AMEND routing table** (structure/precision)
From the V-05 triple-gap pattern. The post-processing routing table (A-16) includes a diagnostic row that tests co-occurrence of three independent failure signals: (1) at least one Opaque forward mechanism hop, (2) at least one falsification condition remaining testability=Unknown after evidence, and (3) at least one I-NN condition whose scope overlaps a forward-chain falsification condition. When all three co-occur, the triple-gap count is nonzero and triggers a separate AMEND Triple-gap slot -- a joint severity signal that no single-dimension diagnostic row (Observability, Testability, Inertia individually) can surface. A routing table that carries only single-dimension diagnostic rows without a joint co-occurrence row fails. A-10 is a prerequisite (Opaque hop detection requires per-hop observability labels); A-13 is a prerequisite (residual Unknown detection requires testability refinement tracking); A-14 is a prerequisite (I-NN scope overlap requires a structured I-NN pool to exist); A-16 is a prerequisite (the triple-gap row must live inside a consolidated routing table produced by a named post-processing role).

**Scoring formula update:**
`aspirational_pass / 17 * 10` (denominator was 16, now 17 to absorb A-17)

**Effect on R7 baselines under v8:**
V-01 through V-04 pass A-01--A-16, fail A-17 (no triple-gap row in routing table): 16/17 x 10 = 9.412 -> composite ~99.4. Still golden.
V-05 passes A-01--A-17 (AUDITOR row 5 is the triple-gap diagnostic): 17/17 x 10 = 10.0 -> composite = 100.0. Still golden.

**Effect on R6 baselines under v8:**
V-01 (R6) passes A-01--A-13, fails A-14/A-15/A-16/A-17: 13/17 x 10 = 7.647 -> composite ~97.6. Still golden.
V-02 (R6) passes A-01--A-13 and A-16, fails A-14/A-15/A-17: 14/17 x 10 = 8.235 -> composite ~98.2. Still golden.
V-03 (R6) passes A-01--A-15, fails A-16/A-17: 15/17 x 10 = 8.824 -> composite ~98.8. Still golden.

**Effect on R5 and earlier baselines under v8:**
All R5, R4, R3 variations lack I-NN pool, inertia observability, AUDITOR routing table, and triple-gap row. Their aspirational scores decrease proportionally but composite scores remain well above 80 due to essential and recommended bands. All remain golden.

---

### Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Mechanism pathway named** | essential | correctness | Output names a specific mechanism linking X to Y -- not just a correlation restatement. |
| C-02 | **Falsification condition present** | essential | coverage | Output names at least one observable condition that, if true, would disprove the mechanism. |
| C-03 | **Inertia check performed** | essential | coverage | Output explicitly asks and answers: does doing nothing also produce Y? |
| C-04 | **Causal claim is scoped/testable** | essential | correctness | Output narrows the claim to a specific context, population, or condition. |
| C-05 | **AMEND directive produced** | essential | behavior | Output ends with a concrete AMEND block addressing at least two slots. |

### Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| R-01 | Context-specific mechanism evidence | recommended | depth |
| R-02 | Alternative causes or confounders named | recommended | coverage |
| R-03 | Mechanism chain >= 2 hops | recommended | depth |

### Aspirational Criteria (10 pts total, denominator 17)

A-01 through A-16 unchanged from v7. New:

| ID | Criterion | Weight | Category | Prerequisites |
|----|-----------|--------|----------|---------------|
| **A-17** | **Triple-gap joint diagnostic row in AMEND routing table** | aspirational | structure | A-10, A-13, A-14, A-16 |

---

**Key design decision for A-17:** The triple-gap is not simply "more rows" -- it is a qualitatively different diagnostic that tests *joint* failure. Individual rows in A-16 test single dimensions; A-17 requires that the routing table also answer the co-occurrence question. A V-05-style implementation produces a nonzero triple-gap count only when all three signals are simultaneously present, making it a higher-sensitivity trigger than any individual slot.
he causal pathway is decomposed into at least two intermediate steps (X -> A -> Y), making the mechanism checkable at each hop rather than opaque. |

---

### Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| A-01 | **Mechanism strength qualified** | aspirational | depth | Output assigns a directional confidence to the mechanism (Strong/Moderate/Weak, or equivalent discrete label) with a brief rationale -- not just presence/absence. |
| A-02 | **Inertia baseline quantified or bounded** | aspirational | depth | The inertia check produces an estimate or bound on the baseline Y rate without X (e.g., "Y already occurs in ~30% of cases without this feature"), enabling a meaningful comparison. "Unknown" is an acceptable result but must be explicitly stated rather than omitted. |
| A-03 | **Adversarial section structurally separated** | aspirational | structure | Output contains a distinct challenge or skeptic section that is spatially and logically separated from the mechanism pathway analysis -- not a caveat appended inline. A "however" clause or parenthetical doubt within the mechanism section fails. The adversarial content must stand alone as a named section or role output. |
| A-04 | **All classification outputs use discrete labels** | aspirational | precision | Every classification judgment in the output (mechanism strength, confidence level, inertia severity, observability, evidence quality) is expressed as a discrete label from a fixed set (Strong/Moderate/Weak, High/Medium/Low, Observable/Partial/Opaque, or equivalent) with a rationale line. Prose-only classifications ("seems fairly strong", "probably moderate") fail. A-01 is a prerequisite -- A-04 additionally requires that the pattern holds for all classification-type outputs, not just mechanism strength. |
| A-05 | **Evidence section precedes mechanism mapping** | aspirational | structure | Output contains a dedicated evidence-gathering section or role that is completed and gated before the mechanism chain is constructed. Evidence annotated after mechanism mapping, or an evidence field appended to the end of the output, fails. "None found" is an acceptable evidence result but must appear before the mechanism section and must trigger a mandatory AMEND slot. |
| A-06 | **Dual mechanism strength rating present** | aspirational | depth | Output includes both a preliminary mechanism strength rating (assigned after the mechanism chain, before the adversarial challenge) and a final mechanism strength rating (assigned after the adversarial challenge). The pairing creates an observable signal for whether the adversarial section changed the assessment. A single rating, or two ratings without the pre/post adversarial framing, fails. A-01 and A-03 are prerequisites. |
| A-07 | **Falsification confidence per row uses discrete labels** | aspirational | precision | Every falsification condition in the output carries a row-level confidence or priority label (High/Medium/Low or equivalent discrete set) with a brief rationale. Section-level falsifiability ratings without per-condition granularity fail. This extends the dedicated-field principle from A-01 to row-level classification judgments -- A-04 is a prerequisite. |
| A-08 | **Mechanism hops cross-reference falsification conditions** | aspirational | precision | Every mechanism hop in the causal chain carries a field identifying which pre-generated falsification condition it explains or refines. This bidirectional link makes the mechanism work serve a dual role: causal pathway explanation and falsification rationale. A mechanism section that generates falsification conditions only as a downstream output -- without tracing each hop to a named, pre-existing condition -- fails. C-02 and A-05 are prerequisites: falsification conditions must exist before mechanism construction begins for cross-referencing to be possible. |
| A-09 | **Structural gate checklists enforce transition completeness** | aspirational | structure | Output contains at least one transition gate -- a named, binary checklist of observable completion conditions -- positioned at a section or role boundary and required to be satisfied before the next section or role proceeds. The checklist converts structural requirements from prose instructions into verifiable checkpoints. A prose statement directing the reader to complete work before continuing, without a binary checklist, fails. A-03 is a prerequisite -- at least one structurally separated section must exist for a gate to be positioned at its boundary. |
| A-10 | **Mechanism hop observability labeled** | aspirational | precision | Every mechanism hop in the causal chain carries a discrete observability label (Observable/Partial/Opaque) with a brief rationale indicating how directly the intermediate state can be measured or detected. This label is independent of the falsification cross-reference (A-08) and mechanism strength (A-01) -- it answers "can we actually see this step happen?" A hop labeled only in prose without a discrete label fails. A-08 is a prerequisite -- hops must already carry falsification cross-references before observability is added as a second dedicated per-hop field. |
| A-11 | **Falsification testability rated per condition** | aspirational | precision | Every falsification condition in the output carries a testability rating (Easy/Hard/Unknown) as a dimension distinct from its confidence or priority label (A-07). The testability rating answers "can we run this test given available resources?" while confidence answers "how likely is this condition to falsify the mechanism?" A falsification condition carrying only a confidence label, without a separate testability dimension, fails. A-07 is a prerequisite -- per-condition discrete labeling must already be established before a second classification dimension per row is added. |
| A-12 | **Aggregate observability label with conditional AMEND routing** | aspirational | structure | After all per-hop observability labels (A-10) are assigned, the output computes a chain-level aggregate observability label (AllObservable/Mixed/PredominantlyOpaque) across the full mechanism chain. This aggregate label functions as a conditional AMEND trigger: if the chain is Mixed or PredominantlyOpaque, a mandatory AMEND Observability slot is required. The aggregate detects chain-level unobservability that per-hop inline fields cannot surface individually -- a chain may contain no single Opaque hop yet still be predominantly unobservable due to cumulative partial observability. An output that carries per-hop observability labels without a chain-level summary label and conditional routing fails. A-10 is a prerequisite. |
| A-13 | **Testability refinement yield tracked as structured finding** | aspirational | depth | Unknown is treated as a first-class testability state, not a gap: conditions that begin as Unknown at genesis are actively tracked through the evidence phase. The output records testability_refined_count (conditions that moved from Unknown to Easy or Hard after evidence) and testability_residual_unknown_count (conditions that remain Unknown after evidence). Residual Unknowns route to a mandatory AMEND Testability slot as structured findings rather than implicit gaps. An output that marks conditions Unknown without tracking whether refinement occurred, or without routing residual Unknowns to AMEND, fails. A-11 is a prerequisite -- per-condition testability rating must already be established before refinement events can be defined and counted. |
| A-14 | **Inertia pathway has a structured falsification sub-pool (I-NN)** | aspirational | structure | The inertia check generates inertia-specific falsification conditions catalogued as a structured I-NN pool, peer to the mechanism falsification pool (F-NN). I-NN conditions carry the same per-row labels as F-NN conditions (confidence, testability) and are eligible for cross-referencing by mechanism hops via A-08. An inertia check that produces only prose severity or a baseline rate without a structured I-NN table with labeled rows fails. C-03 is a prerequisite (inertia check must exist); A-07 is a prerequisite (per-row discrete labeling of falsification conditions must already be established before the I-NN pool can inherit that structure). |
| A-15 | **Inertia pathway observability labeled** | aspirational | precision | The inertia check produces a discrete observability label (Observable/Partial/Opaque) for the inertia pathway itself, answering: "can we detect whether status quo alone produces Y?" This label is structurally independent of mechanism hop observability (A-10) -- the inertia path runs in parallel to the mechanism chain and may have different observability characteristics. An inertia section that carries severity and baseline rate without a discrete observability label for the inertia path fails. A-02 is a prerequisite (inertia baseline must be bounded before its observability can be meaningfully rated); A-10 is a prerequisite (the hop-level observability labeling pattern must be established before being extended to the inertia path). |
| A-16 | **Post-processing role generates consolidated AMEND routing table** | aspirational | structure | A dedicated post-processing role runs after all analytical roles are complete and produces a structured routing table that consolidates all conditional AMEND slot decisions into a single artifact. Each row identifies a named diagnostic (e.g., Observability, Testability), its result (e.g., Mixed, residual_count > 0), and a routing decision (Required / Not required) for the corresponding AMEND slot. This replaces or supplements scattered inline conditional declarations with a single auditable routing record, making the full set of AMEND triggers visible as a unit. An output that routes AMEND slots only through inline conditional logic -- without a consolidated routing table produced by a named post-processing role -- fails. A-12 and A-13 are prerequisites: at least two conditional AMEND routing decisions must exist before a routing table adds structural value over inline declarations. |
| A-17 | **Triple-gap joint diagnostic row in AMEND routing table** | aspirational | structure | The post-processing routing table (A-16) contains a diagnostic row that tests co-occurrence of three independent failure signals: (1) at least one Opaque forward mechanism hop, (2) at least one falsification condition remaining testability=Unknown after evidence, and (3) at least one I-NN condition whose scope overlaps a forward-chain falsification condition. When all three co-occur the triple-gap count is nonzero and triggers a dedicated AMEND Triple-gap slot -- a joint severity signal that no single-dimension diagnostic row (Observability, Testability, or Inertia individually) can surface. A routing table that carries only single-dimension rows without a joint co-occurrence row fails. A-10 is a prerequisite (Opaque hop detection requires per-hop observability labels); A-13 is a prerequisite (residual Unknown detection requires testability refinement tracking); A-14 is a prerequisite (I-NN scope overlap requires a structured I-NN pool to exist); A-16 is a prerequisite (the triple-gap row must live inside a consolidated routing table produced by a named post-processing role). |
