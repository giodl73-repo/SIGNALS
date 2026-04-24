# flow-dataflow Rubric — v4

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from R1 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |
| v3 | 2026-03-14 | Added C-13..C-15 from R2 excellence signals: pre-declared staleness contract, additive elapsed time calculation, incumbent baseline section |
| v4 | 2026-03-14 | Added C-16..C-18 from R3 excellence signals: cross-role reference chain, immutability declaration, incremental boundary elapsed computation |

## Purpose

Score a `flow-dataflow` skill output: a data lineage trace covering source, transformation stages, and destination for a Finance, Operations, or Commerce pipeline scenario.

---

## Essential Criteria (weight: 60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Data lineage chain** | correctness | Every in-scope item has an unbroken source => stage(s) => destination chain. No item appears at a destination without an identified origin. |
| C-02 | **Boundary error handling** | correctness | Each boundary is annotated: either the mechanism (retry, dead-letter, rollback) or an explicit "no handling" flag. Silence is not acceptable. |
| C-03 | **Data loss point identification** | coverage | At least one concrete loss point is named per pipeline stage. Generic "errors may occur" does not qualify. |
| C-04 | **Schema state at each stage** | correctness | Schema at every stage entry/exit is described or diffed. A stage that changes field names or types with no schema note fails. |

---

## Recommended Criteria (weight: 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency characterization** | depth | Every stage has a latency annotation: value, range, or characterization (real-time / batch / daily). |
| C-06 | **Stale data windows** | depth | At least one stale window quantified. Failure-mode staleness addressed separately from normal-operation staleness. |
| C-07 | **Domain framing** | format | Domain-specific entity names appear in the lineage chain. Purely generic trace fails. |

---

## Aspirational Criteria (weight: 10 pts total) — **11 criteria in v4**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Recovery prescriptions** | depth | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion. |
| C-09 | **Pattern trade-off analysis** | behavior | Named alternative pattern with at least two quantified or qualified trade-off dimensions. |
| C-10 | **Pre-trace domain context gate** | format | A DOMAIN CONTEXT section appears before the first stage block, locking entity names, downstream consumer, and business cadence. At least two of those terms reappear verbatim in subsequent lineage or stale-window content. |
| C-11 | **Interleaved boundary gates** | behavior | A boundary check block appears between every consecutive stage pair — inline, not post-hoc. A trailing BOUNDARY SUMMARY alone does not satisfy this criterion. |
| C-12 | **Domain entity exposure per boundary** | format | Every boundary check that satisfies C-11 names a domain entity from the scenario vocabulary. "data" or "records" alone does not pass. |
| C-13 | **Pre-declared staleness contract** | depth | The stale threshold for at least one entity is declared as an explicit contract in DOMAIN CONTEXT before Stage 1 is written. The stale analysis derives its rows by evaluating actual elapsed time against this threshold. A stale window asserted or synthesized after the stages does not pass. |
| C-14 | **Additive elapsed time calculation** | depth | Latency annotations across stages and boundaries are accumulated into an explicit end-to-end elapsed total. This total appears in or immediately before the stale analysis, enabling direct numeric comparison against C-13's threshold. Per-stage annotations alone with no cumulative total do not pass. |
| C-15 | **Incumbent or manual-process baseline** | behavior | A named baseline section describes the incumbent or manual process this pipeline replaces. The baseline must surface at least one vocabulary term that reappears in C-10 DOMAIN CONTEXT, and must be referenced in C-08 (recovery prescriptions) or C-09 (trade-off analysis) to close the comparison loop. A baseline not connected to C-08 or C-09 does not pass. |
| C-16 | **Cross-role reference chain** | behavior | Each role or section explicitly cites a named output from at least one prior role or section — not a generic back-reference ("as established above") but a named citation (e.g., "Role 1's DOMAIN CONTEXT", "INCUMBENT BASELINE from Role 2"). A section that introduces vocabulary or analysis without attributing it to a prior named source does not pass. |
| C-17 | **Immutability declaration on pre-committed values** | depth | At least one pre-committed contract value (such as the staleness threshold from C-13) is accompanied by an explicit prohibition on post-trace revision. The prompt text must state that the value cannot be changed after a specified point (e.g., "This threshold is fixed. You may not revise it after Stage 1."). A request for early declaration alone — as required by C-13 — does not satisfy this criterion. |
| C-18 | **Incremental boundary elapsed computation** | behavior | The cumulative elapsed total required by C-14 is computed as a named field within each BOUNDARY CHECK block, incrementally updated at every boundary as a structural side effect of writing that block. A cumulative total that appears only in a post-stage summary section does not pass, even if numerically correct. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4    =>  (___ / 4)  * 60 = ___
Recommended passed:   ___ / 3    =>  (___ / 3)  * 30 = ___
Aspirational passed:  ___ / 11   =>  (___ / 11) * 10 = ___
                                     Composite       = ___

Golden: all 4 essential pass AND composite >= 80
```

---

## Criterion rationale — v4 additions

**C-16 (cross-role reference chain)** closes the vocabulary drift mechanism that C-07, C-12, and C-15 individually check outcomes of but do not structurally enforce. When each role is required to cite a prior role's named output, vocabulary propagation becomes a dependency chain rather than a coincidence. The distinction: C-07 checks whether domain terms appear; C-16 checks whether the *source of those terms* is named. A section that duplicates vocabulary from an earlier section without attribution may pass C-07 while still allowing silent divergence in later rounds.

**C-17 (immutability declaration)** is a strictly stronger form of C-13. C-13 requires that a threshold be declared before Stage 1 is written. C-17 requires that the prompt also prohibit post-trace revision of that threshold. The two criteria address different model behaviors: C-13 prevents the threshold from being synthesized retroactively; C-17 prevents the model from adjusting an honestly pre-declared threshold after observing the timing facts. Both failure modes are real. A variation can pass C-13 (early declaration present) while still allowing threshold drift post-trace if C-17 is absent.

**C-18 (incremental boundary elapsed computation)** is a strictly stronger form of C-14. C-14 requires that a cumulative elapsed total appear in or before the stale analysis. C-18 requires that this total be computed field-by-field at each boundary block rather than assembled in a post-stage summary. The structural distinction matters: a post-stage summary permits selective latency inclusion — the model can choose which stages to sum. An inline boundary field computed incrementally cannot omit a boundary without the output becoming structurally incomplete. The incremental pattern makes fabrication structurally harder, not merely prohibited.
