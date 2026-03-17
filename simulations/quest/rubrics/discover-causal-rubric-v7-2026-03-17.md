Reading the scorecard carefully to identify new excellence patterns before writing the rubric.

The new patterns in R6 not yet captured as criteria:

**From V-03 (Inertia-Inclusive Aggregates):**
- C-03 evidence: "inertia check with severity, baseline rate, and **inertia observability**" — the inertia path itself carries an observability label, distinct from mechanism hop observability (A-10)
- A-07 evidence: "**F-NN table (S1) and I-NN table (S2)** both carry High/Medium/Low per row" — inertia conditions form a second structured falsification pool (I-NN), peer to F-NN
- A-08 evidence: "works across both pools" — mechanism hops cross-reference either pool

**From V-02 (AUDITOR Role):**
- A-12/A-13 evidence: "AUDITOR Diagnostic 1 … AMEND routing table row 1" / "AUDITOR Diagnostic 2 … AMEND routing table row 2" — a post-processing role consolidates all conditional AMEND decisions into a single structured routing table with quality labels per diagnostic

Three new criteria: **A-14** (inertia I-NN pool), **A-15** (inertia path observability), **A-16** (AMEND routing table). Denominator moves from 13 → 16.

---

## Discover-Causal Rubric — v7

**Skill**: `/discover:causal`
**Version**: v7 — 2026-03-17
**Golden threshold**: all 5 essential pass AND composite ≥ 80

---

### Changes from v6 to v7

Three new aspirational criteria extracted from R6 excellence signals. V-01 scored 100.0 (13/13 aspirational); V-02 and V-03 each scored 100.0 (13/13 aspirational). The new criteria surface structural patterns visible in V-02 and V-03 that V-01 does not implement.

**A-14 — Inertia pathway has a structured falsification sub-pool (I-NN)** (structure/precision)
From the V-03 Inertia-Inclusive Aggregates pattern. The inertia check generates inertia-specific falsification conditions catalogued as a structured I-NN pool, peer to the mechanism falsification pool (F-NN). I-NN conditions carry the same per-row labels as F-NN conditions (confidence, testability) and are eligible for cross-referencing by mechanism hops via A-08. An inertia check that produces only prose severity or a baseline rate without a structured I-NN table — with labeled rows — fails. C-03 is a prerequisite (inertia check must exist); A-07 is a prerequisite (per-row discrete labeling of falsification conditions must already be established before the I-NN pool can inherit that structure).

**A-15 — Inertia pathway observability labeled** (precision)
From the V-03 Inertia-Inclusive Aggregates pattern. The inertia check produces a discrete observability label (Observable/Partial/Opaque) for the inertia pathway itself, answering: "can we detect whether status quo alone produces Y?" This label is structurally independent of mechanism hop observability (A-10), which labels forward causal steps — the inertia path runs in parallel and may have different observability characteristics than any mechanism hop. An inertia section that carries severity and baseline rate without a discrete observability label for the inertia path fails. A-02 is a prerequisite (inertia baseline must be bounded before its observability can be meaningfully rated); A-10 is a prerequisite (the hop-level observability labeling pattern must already be established before being extended to the inertia path).

**A-16 — Post-processing role generates consolidated AMEND routing table** (structure)
From the V-02 AUDITOR Role pattern. A dedicated post-processing role runs after all analytical roles are complete and produces a structured routing table that consolidates all conditional AMEND slot decisions into a single artifact. Each row in the routing table identifies a named diagnostic (e.g., Observability, Testability), its result (e.g., Mixed, residual_count > 0), and a routing decision (Required / Not required) for the corresponding AMEND slot. This replaces or supplements scattered inline conditional declarations with a single auditable routing record, making the full set of AMEND triggers visible at a glance. An output that routes AMEND slots only through inline conditional logic — without a consolidated routing table produced by a named post-processing role — fails. A-12 and A-13 are prerequisites: at least two conditional AMEND routing decisions must exist before a routing table adds structural value over inline declarations.

**Scoring formula update:**
`aspirational_pass / 16 * 10` (denominator was 13, now 16 to absorb A-14, A-15, A-16)

**Effect on R6 baselines under v7:**
V-01 passes A-01–A-13, fails A-14/A-15/A-16 (no I-NN pool, no inertia observability, no AUDITOR routing table): 13/16 × 10 = 8.125 → composite ≈ 98.1. Still golden.
V-02 passes A-01–A-13 and A-16 (AUDITOR routing table), fails A-14/A-15 (no I-NN pool, no inertia observability in FRAMER): 14/16 × 10 = 8.75 → composite ≈ 98.75. Still golden.
V-03 passes A-01–A-13 and A-14/A-15 (I-NN pool, inertia observability), fails A-16 (no consolidated routing table): 15/16 × 10 = 9.375 → composite ≈ 99.4. Still golden.

**Effect on R5 and earlier baselines under v7:**
All R5, R4, R3 variations lack I-NN pool, inertia observability, and AUDITOR routing table. They pass A-01–A-11 (or fewer). Under v7 their aspirational scores decrease proportionally but composite scores remain well above 80 due to essential and recommended bands. All remain golden.

---

### Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Mechanism pathway named** | essential | correctness | Output names a specific mechanism linking X to Y — not just a correlation restatement. "X is associated with Y" or "X predicts Y" without a mechanism fails. |
| C-02 | **Falsification condition present** | essential | coverage | Output names at least one observable condition that, if true, would disprove the mechanism. "We can't know" or no falsification statement fails. |
| C-03 | **Inertia check performed** | essential | coverage | Output explicitly asks and answers: does doing nothing (or the status quo) also produce Y? If the check is omitted entirely, criterion fails. |
| C-04 | **Causal claim is scoped/testable** | essential | correctness | The output narrows the original claim to a specific context, population, or condition under which the mechanism is expected to hold. A claim that is unfalsifiable by scope ("always causes") fails. |
| C-05 | **AMEND directive produced** | essential | behavior | Output ends with a concrete AMEND block that addresses at least two of: narrow the causal claim, add mechanism pathway, add falsification condition. A missing or empty AMEND fails. |

---

### Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| R-01 | **Context-specific mechanism evidence** | recommended | depth | Output cites at least one piece of evidence (prior result, analogous feature, domain knowledge) that the mechanism has operated or failed in this specific context — not just in theory. |
| R-02 | **Alternative causes or confounders named** | recommended | coverage | Output identifies at least one alternative explanation for Y that does not involve X, or one confounder that could produce the appearance of X→Y without a true causal link. |
| R-03 | **Mechanism chain has at least two hops** | recommended | depth | The causal pathway is decomposed into at least two intermediate steps (X → A → Y), making the mechanism checkable at each hop rather than opaque. |

---

### Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| A-01 | **Mechanism strength qualified** | aspirational | depth | Output assigns a directional confidence to the mechanism (Strong/Moderate/Weak, or equivalent discrete label) with a brief rationale — not just presence/absence. |
| A-02 | **Inertia baseline quantified or bounded** | aspirational | depth | The inertia check produces an estimate or bound on the baseline Y rate without X (e.g., "Y already occurs in ~30% of cases without this feature"), enabling a meaningful comparison. "Unknown" is an acceptable result but must be explicitly stated rather than omitted. |
| A-03 | **Adversarial section structurally separated** | aspirational | structure | Output contains a distinct challenge or skeptic section that is spatially and logically separated from the mechanism pathway analysis — not a caveat appended inline. A "however" clause or parenthetical doubt within the mechanism section fails. The adversarial content must stand alone as a named section or role output. |
| A-04 | **All classification outputs use discrete labels** | aspirational | precision | Every classification judgment in the output (mechanism strength, confidence level, inertia severity, observability, evidence quality) is expressed as a discrete label from a fixed set (Strong/Moderate/Weak, High/Medium/Low, Observable/Partial/Opaque, or equivalent) with a rationale line. Prose-only classifications ("seems fairly strong", "probably moderate") fail. A-01 is a prerequisite — A-04 additionally requires that the pattern holds for all classification-type outputs, not just mechanism strength. |
| A-05 | **Evidence section precedes mechanism mapping** | aspirational | structure | Output contains a dedicated evidence-gathering section or role that is completed and gated before the mechanism chain is constructed. Evidence annotated after mechanism mapping, or an evidence field appended to the end of the output, fails. "None found" is an acceptable evidence result but must appear before the mechanism section and must trigger a mandatory AMEND slot. |
| A-06 | **Dual mechanism strength rating present** | aspirational | depth | Output includes both a preliminary mechanism strength rating (assigned after the mechanism chain, before the adversarial challenge) and a final mechanism strength rating (assigned after the adversarial challenge). The pairing creates an observable signal for whether the adversarial section changed the assessment. A single rating, or two ratings without the pre/post adversarial framing, fails. A-01 and A-03 are prerequisites. |
| A-07 | **Falsification confidence per row uses discrete labels** | aspirational | precision | Every falsification condition in the output carries a row-level confidence or priority label (High/Medium/Low or equivalent discrete set) with a brief rationale. Section-level falsifiability ratings without per-condition granularity fail. This extends the dedicated-field principle from A-01 to row-level classification judgments — A-04 is a prerequisite. |
| A-08 | **Mechanism hops cross-reference falsification conditions** | aspirational | precision | Every mechanism hop in the causal chain carries a field identifying which pre-generated falsification condition it explains or refines. This bidirectional link makes the mechanism work serve a dual role: causal pathway explanation and falsification rationale. A mechanism section that generates falsification conditions only as a downstream output — without tracing each hop to a named, pre-existing condition — fails. C-02 and A-05 are prerequisites: falsification conditions must exist before mechanism construction begins for cross-referencing to be possible. |
| A-09 | **Structural gate checklists enforce transition completeness** | aspirational | structure | Output contains at least one transition gate — a named, binary checklist of observable completion conditions — positioned at a section or role boundary and required to be satisfied before the next section or role proceeds. The checklist converts structural requirements from prose instructions into verifiable checkpoints. A prose statement directing the reader to complete work before continuing, without a binary checklist, fails. A-03 is a prerequisite — at least one structurally separated section must exist for a gate to be positioned at its boundary. |
| A-10 | **Mechanism hop observability labeled** | aspirational | precision | Every mechanism hop in the causal chain carries a discrete observability label (Observable/Partial/Opaque) with a brief rationale indicating how directly the intermediate state can be measured or detected. This label is independent of the falsification cross-reference (A-08) and mechanism strength (A-01) — it answers "can we actually see this step happen?" A hop labeled only in prose without a discrete label fails. A-08 is a prerequisite — hops must already carry falsification cross-references before observability is added as a second dedicated per-hop field. |
| A-11 | **Falsification testability rated per condition** | aspirational | precision | Every falsification condition in the output carries a testability rating (Easy/Hard/Unknown) as a dimension distinct from its confidence or priority label (A-07). The testability rating answers "can we run this test given available resources?" while confidence answers "how likely is this condition to falsify the mechanism?" A falsification condition carrying only a confidence label, without a separate testability dimension, fails. A-07 is a prerequisite — per-condition discrete labeling must already be established before a second classification dimension per row is added. |
| A-12 | **Aggregate observability label with conditional AMEND routing** | aspirational | structure | After all per-hop observability labels (A-10) are assigned, the output computes a chain-level aggregate observability label (AllObservable/Mixed/PredominantlyOpaque) across the full mechanism chain. This aggregate label functions as a conditional AMEND trigger: if the chain is Mixed or PredominantlyOpaque, a mandatory AMEND Observability slot is required. The aggregate detects chain-level unobservability that per-hop inline fields cannot surface individually — a chain may contain no single Opaque hop yet still be predominantly unobservable due to cumulative partial observability. An output that carries per-hop observability labels without a chain-level summary label and conditional routing fails. A-10 is a prerequisite. |
| A-13 | **Testability refinement yield tracked as structured finding** | aspirational | depth | Unknown is treated as a first-class testability state, not a gap: conditions that begin as Unknown at genesis are actively tracked through the evidence phase. The output records `testability_refined_count` (conditions that moved from Unknown to Easy or Hard after evidence) and `testability_residual_unknown_count` (conditions that remain Unknown after evidence). Residual Unknowns route to a mandatory AMEND Testability slot as structured findings rather than implicit gaps. An output that marks conditions Unknown without tracking whether refinement occurred, or without routing residual Unknowns to AMEND, fails. A-11 is a prerequisite — per-condition testability rating must already be established before refinement events can be defined and counted. |
| A-14 | **Inertia pathway has a structured falsification sub-pool (I-NN)** | aspirational | structure | The inertia check generates inertia-specific falsification conditions catalogued as a structured I-NN pool, peer to the mechanism falsification pool (F-NN). I-NN conditions carry the same per-row labels as F-NN conditions (confidence, testability) and are eligible for cross-referencing by mechanism hops via A-08. An inertia check that produces only prose severity or a baseline rate without a structured I-NN table with labeled rows fails. C-03 is a prerequisite (inertia check must exist); A-07 is a prerequisite (per-row discrete labeling of falsification conditions must already be established before the I-NN pool can inherit that structure). |
| A-15 | **Inertia pathway observability labeled** | aspirational | precision | The inertia check produces a discrete observability label (Observable/Partial/Opaque) for the inertia pathway itself, answering: "can we detect whether status quo alone produces Y?" This label is structurally independent of mechanism hop observability (A-10) — the inertia path runs in parallel to the mechanism chain and may have different observability characteristics. An inertia section that carries severity and baseline rate without a discrete observability label for the inertia path fails. A-02 is a prerequisite (inertia baseline must be bounded before its observability can be meaningfully rated); A-10 is a prerequisite (the hop-level observability labeling pattern must be established before being extended to the inertia path). |
| A-16 | **Post-processing role generates consolidated AMEND routing table** | aspirational | structure | A dedicated post-processing role runs after all analytical roles are complete and produces a structured routing table that consolidates all conditional AMEND slot decisions into a single artifact. Each row identifies a named diagnostic (e.g., Observability, Testability), its result (e.g., Mixed, residual_count > 0), and a routing decision (Required / Not required) for the corresponding AMEND slot. This replaces or supplements scattered inline conditional declarations with a single auditable routing record, making the full set of AMEND triggers visible as a unit. An output that routes AMEND slots only through inline conditional logic — without a consolidated routing table produced by a named post-processing role — fails. A-12 and A-13 are prerequisites: at least two conditional AMEND routing decisions must exist before a routing table adds structural value over inline declarations. |
