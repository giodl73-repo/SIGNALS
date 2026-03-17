Looking at the V-01 scorecard evidence, two new patterns appear that aren't captured by existing criteria:

1. **A-04 evidence** lists "Observability (Observable/Partial/Opaque)" per mechanism hop — a distinct classification dimension not currently in any criterion.
2. **A-07 evidence** lists "testability guess (Easy/Hard/Unknown) per row" in the F-NN table — a second per-condition label separate from falsification confidence.

Both appear only in R4-V-01 (the first 100.0 scorer) and neither is implied by A-04 or A-07 in their current form. Here is the complete updated rubric:

---

## Discover-Causal Rubric — v5

**Skill**: `/discover:causal`
**Version**: v5 — 2026-03-17
**Golden threshold**: all 5 essential pass AND composite ≥ 80

---

### Changes from v4 to v5

Two new aspirational criteria extracted from R4 excellence signals (V-01 scored 100):

**A-10 — Mechanism hop observability labeled** (precision)
From the V-01 per-hop observability pattern. Each mechanism hop carries a discrete observability label (Observable/Partial/Opaque) with a brief rationale indicating how directly the intermediate state can be measured or detected. This label is independent of falsification cross-references and mechanism strength — it answers "can we actually see this step happen?" separately from "does this step explain a falsification condition?" A hop labeled only in prose ("difficult to observe directly") without a discrete label fails. A-08 is a prerequisite — hops must already carry falsification cross-references before observability is added as a second dedicated field per hop.

**A-11 — Falsification testability rated per condition** (precision)
From the V-01 per-F-NN testability pattern. Each falsification condition in the output carries a testability rating (Easy/Hard/Unknown) as a dimension distinct from its confidence or priority label (A-07). The testability rating answers "can we run this test given available resources?" while confidence answers "how likely is this condition to actually falsify the mechanism?" A falsification condition that carries only a confidence label, without a separate testability dimension, fails. A-07 is a prerequisite — per-condition discrete labeling must already be established before a second classification dimension per row is added.

**Scoring formula update:**
`aspirational_pass / 11 * 10` (denominator was 9, now 11 to absorb A-10 and A-11)

**Effect on R4 baselines under v5:**
V-01 retroactively passes both A-10 (Observability field per hop in A-04 evidence) and A-11 (testability guess per F-NN row in A-07 evidence) — composite stays 100.0.

**Effect on R3 baselines under v5:**
R3-V-04 passed A-08, failed A-09, A-10, A-11: 8/11 × 10 = 7.27 → composite ≈ 97.3. Still golden.
R3-V-05 passed A-09, failed A-08, A-10, A-11: 8/11 × 10 = 7.27 → composite ≈ 97.3. Still golden.
R3-V-01/V-02/V-03 passed A-01–A-07, failed A-08–A-11: 7/11 × 10 = 6.36 → composite ≈ 96.4. Still golden.
All R3 and R4 variations remain golden under v5.

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
