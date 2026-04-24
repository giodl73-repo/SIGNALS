Rubric written to `simulations/quest/rubrics/flow-dataflow-rubric-2026-03-14.md`.

**Structure:**
- **4 Essential (C-01..C-04)** — data lineage chain, boundary error handling, data loss points, schema state at each stage
- **3 Recommended (C-05..C-07)** — latency characterization, stale data windows, domain framing (Finance/Ops/Commerce vocab)
- **2 Aspirational (C-08..C-09)** — recovery prescriptions for every gap found, pattern trade-off analysis vs alternatives

The essential criteria are tightly coupled to the skill's stated outputs: source→transform→destination tracing, per-boundary error handling, and explicit data loss enumeration. Schema tracking was added as a fourth essential because schema mismatches are the skill's own named failure mode — a trace that ignores schema deltas can't catch mismatches.
m. | correctness | Every in-scope item has an unbroken source => stage(s) => destination chain. No item appears at a destination without an identified origin. |
| C-02 | **Boundary error handling** — At every stage boundary (source read, transform, destination write, sync handoff), the output states what error handling exists or explicitly marks it as absent. | correctness | Each boundary is annotated: either the mechanism (retry, dead-letter, rollback) or an explicit "no handling" flag. Silence is not acceptable. |
| C-03 | **Data loss point identification** — The output explicitly enumerates locations where data can be silently dropped, truncated, or not replayed -- not just failure modes that surface as errors. | coverage | At least one concrete loss point is named per pipeline stage. Generic "errors may occur" statements do not qualify. |
| C-04 | **Schema state at each stage** — The output tracks the schema (field names, types, or structure) entering and leaving each transformation. Where the schema changes, the delta is stated. | correctness | Schema at every stage entry/exit is described or diffed. A stage that changes field names or types with no schema note fails this criterion. |

---

## Recommended Criteria (weight: 30 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-05 | **Latency characterization** — For each stage, the output estimates or bounds the latency contribution (batch window, streaming lag, polling interval, propagation delay). | depth | Every stage has a latency annotation: either a concrete value, a range, or a characterization (real-time / near-real-time / batch / daily). |
| C-06 | **Stale data windows** — The output identifies the maximum staleness window visible to a downstream consumer for each data item under normal operation and under a single-stage failure. | depth | At least one stale-data window is quantified (e.g., "up to 24 hours stale if nightly batch misses"). Failure-mode staleness is addressed separately from normal-operation staleness. |
| C-07 | **Domain framing** — The trace uses Finance, Operations, or Commerce domain vocabulary consistent with the scenario (e.g., "invoice record", "inventory adjustment", "order line") rather than generic "records" or "rows". | format | Domain-specific entity names appear in the lineage chain. A purely generic trace with no domain terms fails this criterion. |

---

## Aspirational Criteria (weight: 10 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-08 | **Missing recovery prescriptions** — For each identified loss point or absent error handler, the output proposes a concrete recovery mechanism (idempotency key, saga compensation, replay log, schema registry) with a brief rationale. | depth | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired recovery suggestion. Suggestions must be specific, not "add retry logic". |
| C-09 | **Pattern trade-off analysis** — The output compares the current pipeline pattern (ETL / sync / CDX / dual-write) to at least one alternative and states the trade-off in terms of consistency, latency, and operational cost relevant to the domain. | behavior | A named alternative pattern appears with at least two quantified or qualified trade-off dimensions. "ETL is simpler" does not qualify without specifics. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4   =>  (___ / 4) * 60 = ___
Recommended passed:   ___ / 3   =>  (___ / 3) * 30 = ___
Aspirational passed:  ___ / 2   =>  (___ / 2) * 10 = ___
                                    Composite      = ___

Golden: all 4 essential pass AND composite >= 80
```
